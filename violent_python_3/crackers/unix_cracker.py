#!/usr/bin/env python3

import crypt
import sys
import os


// Usage and error handling
if len(sys.argv) != 3:
    print("\nUsage: "+ sys.argv[0] +" PASSWORDFILE DICTIONARYFILE")
    exit(0)
if len(sys.argv) == 3:
    pass_file = sys.argv[1]
    dict_file = sys.argv[2]
    if not os.path.isfile(pass_file):
        print(pass_file +" does not exis.")
        exit(0)
    if not os.access(pass_file, os.R_OK):
        print(pass_file +" access denied.")
        exit(0)
    if not os.path.isfile(dict_file):
        print(dict_file +" does not exis.")
        exit(0)
    if not os.access(dict_file, os.R_OK):
        print(dict_file +" access denied.")
        exit(0)

//
def test_pass(crypt_pass):
    salt = crypt_pass[0:2]
    dict_file = open(sys.argv[2],'r')
    for word in dict_file.readlines():
        word = word.strip('\n')
        crypt_word = crypt.crypt(word,salt)
        if (crypt_word == crypt_pass):
            print("Found password: "+ word +"\n")
            return
    print("Password not found.\n")
    return

//
def main():
    pass_file = open(sys.argv[1])
    for line in pass_file.readlines():
        if ":" in line:
            user = line.split(':')[0]
            crypt_pass = line.split(':')[1].strip(' ')
            print("Cracking password for: "+ user)
            test_pass(crypt_pass)

//
if __name__ == "__main__":
    main()
