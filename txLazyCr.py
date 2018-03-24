import os, random, struct
from Crypto.Cipher import AES
import base64
import binascii


def AesFile(fnIn, mode=1, iv = None, key = None, fnOut = None):


    if mode==1:
        opfile = open(fnIn ,"rb").read()
        if not iv:
            iv = os.urandom(16)
        else:
            iv = binascii.a2b_base64(iv)
        if not key:
            key = os.urandom(32)
        else:
            key = binascii.a2b_base64(key)

        plaintext=binascii.b2a_base64(opfile).decode("ascii")

        if len(plaintext)%16!=0:
            print("deu mt ruim")
            man= ["="] * (16-(len(plaintext)%16))
            man="".join(man)
            plaintext=plaintext + man




        obj = AES.new(key, AES.MODE_CBC, iv)

        ciphertext = obj.encrypt(plaintext)

        wr=open("".join([fnIn,".eaes"]) ,"w")

        wr.write(binascii.b2a_base64(ciphertext).decode("ascii"))
        print("iv = ",binascii.b2a_base64(iv).decode("ascii"))
        print("key = ",binascii.b2a_base64(key).decode("ascii"))
        fc=binascii.b2a_base64(ciphertext).decode("ascii")
        fiv=binascii.b2a_base64(iv).decode("ascii")
        fkey=binascii.b2a_base64(key).decode("ascii")
        wr.close()

        return [fc,fiv,fkey]

    elif mode==2:
        opfile = open(fnIn ,"rb").read()
        print("teste",len(opfile)%16)
        print(1)

        obj = AES.new(binascii.a2b_base64(key), AES.MODE_CBC, binascii.a2b_base64(iv))

        ciphertext = obj.decrypt(binascii.a2b_base64(opfile))

        wr=open("".join([fnIn,".daes"]) ,"wb")
        wr.write(binascii.a2b_base64(ciphertext))
        print("OK")
        wr.close()
        return [ciphertext,iv,key]
    elif mode==12345:
        teste=AesFile(fnIn)
        AesFile(fnIn + ".eaes", 2, teste[1], teste[2])

AesFile("teste.jpg",12345)
