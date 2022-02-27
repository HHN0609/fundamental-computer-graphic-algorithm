from PIL import Image
import random
import time
# def swap(a,b):
#     m=a
#     a=b
#     b=m
def midpoint_line(img,x0,y0,x1,y1,color):
    if x0>x1:
        t=x0
        x0=x1
        x1=t
        t=y0
        y0=y1
        y1=t
    steep=abs(y1-y0)>abs(x1-x0)
    if steep == True:
        t=x0
        x0=y0
        y0=t
        t=x1
        x1=y1
        y1=t
    if y0>y1:
        t=-1
    else:
        t=1                        
    dx=x1-x0
    dy=y1-y0
    dm=2*dy-t*dx
    dmp1=2*dy
    dmp2=2*dy-2*t*dx
    y=y0
    for x in range(x0,x1):
        if steep == True:
            img.putpixel((y, x), color)
        else:
            img.putpixel((x, y), color)
        
        if t*dm<=0: 
            dm=dm+dmp1
        else:
            dm=dm+dmp2 
            y=y+t

img2 = Image.new("RGB", (300,300))
start = time.time()
midpoint_line(img2, 30, 40, 80, 60, (255, 0, 0))
midpoint_line(img2, 80, 60, 30, 40, (255, 0, 0))
midpoint_line(img2, 40, 30, 60, 80, (255, 0, 0))
midpoint_line(img2, 60, 80, 40, 30, (255, 0, 0))
midpoint_line(img2, 80, 40, 30, 60, (255, 0, 0))
midpoint_line(img2, 30, 80, 100, 40, (255, 0, 0))
midpoint_line(img2, 30, 40, 80, 40, (255, 0, 0))
midpoint_line(img2, 30, 40, 30, 60, (255, 0, 0))
tb = time.time() - start
print("midpoint_line:", tb)

img2.show()        


