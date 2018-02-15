import os, random
from Crypto.Cipher import AES
import base64
import binascii


	
def aes(plaintext, mode=0, key = None, iv = None, fn_out=None):
	if mode==0:
		if not iv:
			iv = os.urandom(16)
		else:
			iv = binascii.a2b_base64(iv)
		if not key:
			key = os.urandom(32)
		else:
			key = binascii.a2b_base64(key)
		if len(plaintext)%16!=0:
			man= [" "] * (16-(len(plaintext)%16))
			man="".join(man)
			plaintext=plaintext + man
		aes_mode = AES.MODE_CBC
		obj = AES.new(key, aes_mode, iv)
		ciphertext = obj.encrypt(plaintext)
		wr=open("".join([fn,".eaes"]) ,"w")
		wr.write(binascii.b2a_base64(ciphertext).decode("ascii"))
		print("texto = ",binascii.b2a_base64(ciphertext).decode("ascii"))
		print("iv = ",binascii.b2a_base64(iv).decode("ascii"))
		print("key = ",binascii.b2a_base64(key).decode("ascii"))
		
		wr.close()
		return [ciphertext,iv,key]
		
	elif mode==1:
		aes_mode = AES.MODE_CBC
		obj = AES.new(binascii.a2b_base64(key), aes_mode, binascii.a2b_base64(iv))
		ciphertext = obj.decrypt(binascii.a2b_base64(plaintext))
		wr=open("".join([fn,".daes"]) ,"w")
		wr.write((ciphertext).decode("ascii"))
		print((ciphertext).decode("ascii"))
		wr.close()
		return [ciphertext,iv,key]
plain = ""

key=""
iv=""

fn_out = ""



en=aes(plain,1,key,iv,fn_out)
