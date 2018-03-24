Install
pip install -r requirments.txt


trLazyCr:
aes(plain, mode, key, iv, fn_out, fn_in)

plain = plain text for encryption
mode = 0 encrypt text | 1 decrypt text | 2 encrypt file | 3 decrypt file

key = key *necessary for decrypt
key = iv *necessary for decrypt
fn_in = input filename *necessary for mode 2 & 3
fn_out = output filename 

txLazyCr
def AesFile(fnIn, mode = 1, iv = None, key = None, fnOut = None):
fnIn = input filename

mode = 1 encrypt file | 2 decrypt file
key = key *necessary for decrypt
key = iv *necessary for decrypt
fnOut = output filename 

