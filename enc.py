import cryptography
from cryptography.fernet import Fernet
import string
import os 
import sys


def read_key():
	f = open("key.key","rb").read()
	return f


def generate_key():
	key = Fernet.generate_key()
	file = open("key.key","wb")
	file.write(key)
	file.close


#the key has been generated and saved in key.key
#print(generate_key())

def encrypt():
	key = read_key()

	Pass = "Part of the text is missing: D"

	encodePass = Pass.encode()
	FernetKey = Fernet(key)
	encrypt = FernetKey.encrypt(encodePass)
	return encrypt



#you will found the cipher in ciphertext.txt
cipher = encrypt()
