# EncryptPassword
A simple script to request and encrypt a password or any text
## Run
```
./EncryptPass.py --help
usage: EncryptPass.py [-h] [-k path] [-p path]

Encrypt password/text in file

optional arguments:
  -h, --help            show this help message and exit
  -k path, --key_path path
                        the path to encryption key. If not given, a new one
                        will be created ~/.key.key
  -p path, --encrypted_path path
                        the path to save encryption password. If not given, it
                        will be saved in ~/.pass.enc
```

## Setup
### On Milton
To run on milton, use environement in `/stornext/System/data/apps/rc-tools/rc-tools-1.0/bin/tools/envs/py_analysis/bin/python3`
```
module purge
module load anaconda3/latest

python3 EncryptPass.py
```

or 

If the fist line in EncryptPass.py is `#!/stornext/System/data/apps/rc-tools/rc-tools-1.0/bin/tools/envs/py_analysis/bin/python3`, you can run script directly
```
./EncryptPass.py
```

### On your local machine or another environment

Required:
* Python > 3.6
* pip
* cryptography





