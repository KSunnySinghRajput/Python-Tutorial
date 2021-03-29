with open('mssqltip_bytes.bin', 'rb') as file_object:
    for line in file_object:
        encryptedpwd = line
print(encryptedpwd)