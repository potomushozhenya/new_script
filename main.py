import os
import zipfile
import shutil


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
        with zipfile.ZipFile(arch, 'r') as myzip:
            for item in myzip.namelist():
                if ".tex" in item and item.count('/') >= 2:
                    myzip.extract(item, unzipped_path)
    os.chdir(basedir)
    if not os.path.exists('result'):
        os.mkdir('result')
    os.chdir('result')
    unarch_list = os.listdir(unzipped_path)
    for unarch in unarch_list:
        curr_dir_path = unzipped_path + unarch
        shutil.make_archive(unarch, 'zip', curr_dir_path)


if __name__ == '__main__':
    main()

