import cvzone
from cvzone.ColorModule import ColorFinder
import cv2
import socket
sw=960
sh=540
cv2.namedWindow('Window_1',cv2.WINDOW_AUTOSIZE)
cap = cv2.VideoCapture(0)
cv2.resizeWindow('Window_1',sw,sh)
success,img = cap.read()
success,img=cv2.resize(success,(sw,sh)),cv2.resize(img,(sw,sh))
h,w,_=img.shape
myColorFinder = ColorFinder(False)
# #orange
# a={'hmin': 10, 'smin': 87, 'vmin': 152, 'hmax': 74, 'smax': 255,'vmax':255}
# blue
# a = {'hmin': 84, 'smin': 68, 'vmin': 136, 'hmax': 125, 'smax': 255,'vmax':255}
# a={'hmin': 31, 'smin': 100, 'vmin': 87, 'hmax': 56, 'smax': 250, 'vmax': 235}
#red
# a={'hmin': 32, 'smin': 0, 'vmin': 247, 'hmax': 147, 'smax': 255, 'vmax': 250}
#orange2
a={'hmin': 11, 'smin': 131, 'vmin': 218, 'hmax': 27, 'smax': 248, 'vmax': 255}
sock=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
IP_add=socket.gethostbyname(socket.gethostname())
serveradd = (IP_add,5052)
l=[0,0,0,0,0,0,0,0,0,0]
while True:
    if(cv2.waitKey(1)==48):
        break
    success,img = cap.read()  
    success,img=cv2.resize(success,(sw,sh)),cv2.resize(img,(sw,sh))
    imgColor,mask = myColorFinder.update(img,a)
    imgColor,mask = cv2.resize(imgColor,(sw,sh)),cv2.resize(mask,(sw,sh))
    ImgContour,counters=cvzone.findContours(img,mask,1,True)
    # ImgContour,counters=cv2.resize(ImgContour,(sw,sh)),cv2.resize(counters,(sw,sh))
    imgStack=cvzone.stackImages([img,imgColor,mask,ImgContour],2,0.5)
    k = 5
    sum1=0
    if counters:
        new1=counters[0]['area']
        l.append(new1)
        while(k):
            sum1+=l[-1] - l[-2]
            k=k-1
        if(k==0):
            if sum1/5 > 800:
                sum1=0
                k=5
                data = ((counters[0]['center'][0]) * 0.01203703703703703703703703703704)-6.5,\
                    min(((h-counters[0]['center'][1]))//180 + 1,3),\
                    1
            else:
                data = ((counters[0]['center'][0]) * 0.01203703703703703703703703703704)-6.5,\
                    min(((h-counters[0]['center'][1]))//180 + 1,3),\
                    0      
            print(data,new1)
            sock.sendto(str.encode(str(data)),serveradd)
    cv2.imshow("Window_1",imgStack)
