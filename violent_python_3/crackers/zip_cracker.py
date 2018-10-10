import zipfile
import argparse
from threading import Thread

def extract_file(protected_zipfile, password):
    try:
        protected_zipfile.extractall(pwd=password)
        print('Found password ' + password.decode() + '\n')
    except Exception as e:
        pass

def main():
    parser = argparse.ArgumentParser("-f <zipfile> -d <dictionary file>")
    parser.add_argument("-f", dest='zipname', help='specify zip file')
    parser.add_argument("-d", dest='dictname', help='specify dictionary file')
    args = parser.parse_args()
    if (args.zipname == None) | (args.dictname == None):
        print("-h for help")
        exit(0)
    else:
        zipname = args.zipname
        dictname = args.dictname
    protected_zipfile = zipfile.ZipFile(zipname)
    password_file = open(dictname)
    for line in password_file.readlines():
        password = line.strip('\n')
        password = password.encode()
        t = Thread(target=extract_file, args=(protected_zipfile, password))
        t.start()

if __name__ == '__main__':
    main()
