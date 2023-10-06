import os
import zipfile
import rarfile


def main():
    basedir = os.getcwd()
    print(basedir)
    if not os.path.exists('source'):
        print("Создайте папку source и положите туда архивы")
        return 1
    os.chdir('source')
    zips = [f for f in os.listdir() if os.path.isfile(os.path.join('', f))]
    if not os.path.exists('unzipped'):
        os.mkdir('unzipped')
    unzipped_path = basedir + "\\source\\unzipped\\"
    for arch in zips:
        bad_name = ""
        if ".zip" in arch:
            with zipfile.ZipFile(arch, 'r') as myzip:
                bad_name = (myzip.namelist()[0]).split('/')[0]
                for item in myzip.namelist():
                    if ".tex" in item and item.count('/') >= 2:
                        myzip.extract(item, unzipped_path)
        if ".rar" in arch and ".part2" not in arch:
            with rarfile.RarFile(arch, 'r') as myrar:
                bad_name = (myrar.namelist()[0]).split('/')[0]
                for item in myrar.namelist():
                    if ".tex" in item and item.count('/') >= 2:
                        myrar.extract(item, unzipped_path)
        os.chdir('unzipped')
        os.rename(bad_name, os.path.splitext(arch)[0])
        os.chdir('..')


if __name__ == '__main__':
    main()
