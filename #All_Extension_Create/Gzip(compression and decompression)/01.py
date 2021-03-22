#compression 
import gzip
data = b'Python - Batteries included'
with gzip.open("test.txt.gz", "wb") as f:
    f.write(data)
#############################################################
#decompression
with gzip.open("test.txt.gz", "rb") as f:
    data = f.read()
print(data)