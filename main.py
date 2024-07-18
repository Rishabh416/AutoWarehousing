import barcode
from barcode.writer import ImageWriter

from pyzbar.pyzbar import decode
import cv2

code128 = barcode.get_barcode_class("code128")

def generateBarcode(data):
    genCode = code128(data, writer=ImageWriter())
    genCode.save(data)

MODE = "SCAN"

if MODE == "GENERATE":
    generateBarcode("location 04 02")
else:
    vid = cv2.VideoCapture(0)
    while(True): 
        ret, frame = vid.read()
        scanned = decode(frame)
        try:
            print(scanned[0].data.decode('utf-8'))
        except:
            print("No Barcode") 

