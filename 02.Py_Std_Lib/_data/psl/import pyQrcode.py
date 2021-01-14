import pyqrcode
def qrcode():
    q=pyqrcode.create("hello friend")
    q.png('myQR.png',scale=6)
    print("QR Genereted..")
qrcode()
