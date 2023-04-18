#!/stornext/System/data/apps/rc-tools/rc-tools-1.0/bin/tools/envs/py_analysis/bin/python3
import argparse
import getpass
import os

from cryptography.fernet import Fernet


def write_key(keypath):
    """
    Generates a key and save it into a file
    """
    key = Fernet.generate_key()
    with open(keypath, "wb") as key_file:
        key_file.write(key)
def load_key(keypath):
    """
    Loads the key from the current directory named `key.key`
    """
    return open(keypath, "rb").read()

def enc_pass(keypath=None,encpath=None):
    if not keypath:
        keypath=f"{os.path.expanduser('~')}/.key.key"
    if not os.path.exists(keypath):
        write_key(keypath)
    if not encpath:
        encpath=f"{os.path.expanduser('~')}/.pass.enc"

    key=load_key(keypath)
    usr = getpass.getuser()
    pwd = getpass.getpass("enter password for user %s: " % usr).encode()
    f = Fernet(key)
    encrypted = f.encrypt(pwd)
    with open(encpath, "wb") as pass_file:
            pass_file.write(encrypted)
    decrypted_encrypted = f.decrypt(open(encpath, "rb").read())
    if (pwd==decrypted_encrypted):print(f"Password encrypted and validated in {encpath}")
    else : print(f"Password encrypted and validated failed.")

def main(args=None):
    if not args:
        parser = argparse.ArgumentParser(description='Encrypt password in file')
        parser.add_argument('-k','--key_path', metavar='path', required=False,
                            help='the path to encryption key. If not given, a new one will be created ~/.key.key')
        parser.add_argument('-p','--encrypted_path', metavar='path', required=False,
                            help='the path to save encryption password. If not given, it will be saved in ~/.pass.enc')
                           
        args = parser.parse_args()
        enc_pass(args.key_path,args.encrypted_path)
        

if __name__ == "__main__":
    main()