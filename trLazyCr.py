import os, random, struct
from Crypto.Cipher import AES
import base64
import binascii


	
def aes(plaintext, mode=0, key = None, iv = None, fn_out=None, fn_in=None):
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
		obj = AES.new(key, AES.MODE_CBC, iv)
		ciphertext = obj.encrypt(plaintext)
		wr=open("".join([fn_out,".eaes"]) ,"w")
		wr.write(binascii.b2a_base64(ciphertext).decode("ascii"))
		print("texto = ",binascii.b2a_base64(ciphertext).decode("ascii"))
		print("iv = ",binascii.b2a_base64(iv).decode("ascii"))
		print("key = ",binascii.b2a_base64(key).decode("ascii"))
		
		wr.close()
		return [ciphertext,iv,key]
		
	elif mode==1:
		obj = AES.new(binascii.a2b_base64(key), AES.MODE_CBC, binascii.a2b_base64(iv))
		ciphertext = obj.decrypt(binascii.a2b_base64(plaintext))
		wr=open("".join([fn_out,".daes"]) ,"w")
		wr.write((ciphertext).decode("ascii"))
		print((ciphertext).decode("ascii"))
		wr.close()
		return [ciphertext,iv,key]
		
	elif mode==2:
		print(2.1)
		if not iv:
			iv = os.urandom(16)
		else:
			iv = binascii.a2b_base64(iv)
		if not key:
			key = os.urandom(32)
		else:
			key = binascii.a2b_base64(key)
		encryptor = AES.new(key, AES.MODE_CBC, iv)
		filesize = os.path.getsize(fn_in)
		print(2.2)
		with open(fn_in, 'rb') as inp:
			with open(fn_out + ".out", 'wb') as otp:
				otp.write(struct.pack('<Q', filesize))

				while True:
					chunk = inp.read(64*1024)
					if len(chunk) == 0:
						break
					elif len(chunk) % 16 != 0:
						chunk += os.urandom(16 - len(chunk) % 16)

					otp.write(encryptor.encrypt(chunk))
		print("iv = ",binascii.b2a_base64(iv).decode("ascii"))
		print("key = ",binascii.b2a_base64(key).decode("ascii"))
		return "OK"
					
					
	elif mode==3:
		with open(fn_in, 'rb') as inp:
			origsize = struct.unpack('<Q', inp.read(struct.calcsize('Q')))[0]
			decryptor = AES.new(binascii.a2b_base64(key), AES.MODE_CBC, binascii.a2b_base64(iv))
			with open(fn_out + ".out", 'wb') as otp:
				while True:
					chunk = inp.read(64*1024)
					if len(chunk) == 0:
						break
					otp.write(decryptor.decrypt(chunk))
				otp.truncate(origsize)
plain = ""

key=""
iv=""

fn_out = ""

#0 para encrypt text | 1 para decrypt text | 2 para encrypt file | 3 para decrypt file

modo=3

fn_in=""


en=aes(plain,modo,key,iv,fn_out,fn_in)
