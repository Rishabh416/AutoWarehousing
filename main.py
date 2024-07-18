import barcode
from barcode.writer import ImageWriter

from pyzbar.pyzbar import decode
import cv2

import time

import os
from dotenv import load_dotenv
from supabase import create_client, Client

load_dotenv()
url: str = os.getenv("SUPABASE_URL")
key: str = os.getenv("SUPABASE_KEY")
supabase: Client = create_client(url, key)

code128 = barcode.get_barcode_class("code128")

def generateBarcode(data):
    genCode = code128(data, writer=ImageWriter())
    genCode.save(data)

MODE = "SCAN"

storedCodes = []

if MODE == "GENERATE":
    generateBarcode("location 04 02")
else:
    vid = cv2.VideoCapture(3)
    while(True): 
        ret, frame = vid.read()
        cv2.imshow("scanner", frame)
        scanned = decode(frame)
        try:
            scannedCode = scanned[0].data.decode('utf-8')
            if not(scannedCode in storedCodes):
                print(scannedCode)
                storedCodes.append(scannedCode)
        except:
            print("No Barcode") 
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

vid.release()
cv2.destroyAllWindows()

location = ""
tempProduct = ""

for code in storedCodes:
    if "location" in code:
        location = code.split(" ")[1]
        print(location)
    elif "product" in code:
        tempProduct = code.split(" ")[1]
        print(f"product {tempProduct} is at location {location}")
        response = (
            supabase.table("warehouse")
            .insert({"product": tempProduct, "location": location})
            .execute()
        )