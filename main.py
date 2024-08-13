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

MODE = "UPDATE"
stage = 2

storedCodes = []
location = ""
tempProduct = ""

if MODE == "GENERATE":
    generateBarcode("l 0101")
    generateBarcode("p 1234")
    generateBarcode("p 235123")
    generateBarcode("l 0102")
    generateBarcode("p 1248907")
    generateBarcode("p 18044")
    generateBarcode("l 0201")
    generateBarcode("p 1234152")
    generateBarcode("p 13255634")
    generateBarcode("l 0202")
    generateBarcode("p 846532")
    generateBarcode("p 89465132")
elif MODE == "LOCATION":
    vid = cv2.VideoCapture(3)
    vid.set(cv2.CAP_PROP_FRAME_WIDTH, 1920)
    vid.set(cv2.CAP_PROP_FRAME_HEIGHT, 1080)
    while(True): 
        ret, frame = vid.read()
        cv2.imshow("scanner", frame)
        scanned = decode(frame)
        try:
            for barcodes in scanned:
                scannedCode = barcodes.data.decode('utf-8')
            if not(scannedCode in storedCodes):
                print(scannedCode)
                storedCodes.append(scannedCode)
                if "l" in scannedCode:
                    location = scannedCode.split(" ")[1]
                    print(location)
                elif "p" in scannedCode:
                    tempProduct = scannedCode.split(" ")[1]
                    print(f"product {tempProduct} is at location {location}")
                    response = (
                        supabase.table("warehouse")
                        .insert({"product": tempProduct, "location": location, "stage":1})
                        .execute()
                    )
        except:
            # print("No Barcode") 
            pass
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
else:
    vid = cv2.VideoCapture(3)
    vid.set(cv2.CAP_PROP_FRAME_WIDTH, 1920)
    vid.set(cv2.CAP_PROP_FRAME_HEIGHT, 1080)
    while(True): 
        ret, frame = vid.read()
        cv2.imshow("scanner", frame)
        scanned = decode(frame)
        try:
            for barcodes in scanned:
                scannedCode = barcodes.data.decode('utf-8')
                if "product" in scannedCode:
                    tempProduct = scannedCode.split(" ")[1]
                    response = (
                        supabase.table("warehouse")
                        .update({ "stage": stage })
                        .eq("product", tempProduct)
                        .execute()
                    )
            time.sleep(1)
        except:
            # print("No Barcode") 
            pass
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
