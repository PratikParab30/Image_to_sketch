import cv2
import os
import re

def imgcvt(path,nf):
    imr=cv2.imread(path)
    gray=cv2.cvtColor(imr,cv2.COLOR_BGR2GRAY)
    gray2=255-gray
    blr=cv2.GaussianBlur(gray2,(21,21),0) 
    blr2=255-blr 
    sketch=cv2.divide(gray,blr2,scale=256.0)
    svpath=nf+"/"+path
    cv2.imwrite(svpath,sketch)

while True:
    folpath=input("Enter folder path:")
    if os.path.isdir(folpath):
        break
    else:
        print("This is not  valid folder,try again!")
        
os.chdir(folpath)
nf="MySketch"
os.mkdir(nf)
dirr=os.listdir()
flct=0
for path in dirr:
    if os.path.isfile(path):
            if (re.match(".*.jpg",path) or re.match(".*.png",path)):
                imgcvt(path,nf)
                flct+=1
                
if flct !=0:
    print(f"Total {flct} file are created")
else:
    print("Zero file created,please check original file location")