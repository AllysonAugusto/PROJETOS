import pyqrcode
import png
from pyqrcode import QRCode
qrstring = "................" # url
url = pyqrcode.create (qrstring)
url.png ('Desktop\\qr.png', scale = 8)
