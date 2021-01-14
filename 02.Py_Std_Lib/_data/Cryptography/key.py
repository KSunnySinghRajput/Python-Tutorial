from cryptography.fernet import Fernet
#1.key
#key = Fernet.generate_key()    //key generate
#print(key)

#2.key o/p
key = b'8hGlMoDn54h3eKM8p7j9aLOmPc4kG88_srSbEIgBcC8='# Example key

#3.encrypt
#cipher_suite = Fernet(key)
#input_msg="SuperSecretPassword"
#ciphered_text = cipher_suite.encrypt(b"SuperSecretPassword")   #required to be bytes
#print(ciphered_text) 

#4.encrypt output
ciphered_text=b'gAAAAABeagjdWQkmU12BdmX3KSP4dFulCrdWdzgqCyAkXT_K9bm9gyBdYfMJXD4ZoVPUTlfZZRrvp7KrqqXpfkGxn6EB_pMVb9nMQpxyjKojt-3-AsoAI4s='


#5.decryp
#cipher_suite = Fernet(key)
#unciphered_text = cipher_suite.decrypt(ciphered_text)
#print(unciphered_text)

#6.decryp output
output_msg=b'SuperSecretPassword'
print(output_msg )
with open('mssqltip_bytes.bin', 'wb') as file_object:  file_object.write(ciphered_text)