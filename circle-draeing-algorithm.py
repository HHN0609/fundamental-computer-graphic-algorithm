from PIL import Image
import random
import time
def point(img,x,y,xc,yc,color):
    img.putpixel((xc+x,yc+y),color)
    img.putpixel((xc+x,yc-y),color)
    img.putpixel((xc-x,yc+y),color)
    img.putpixel((xc-x,yc-y),color)
    img.putpixel((xc+y,yc+x),color)
    img.putpixel((xc+y,yc-x),color)
    img.putpixel((xc-y,yc+x),color)
    img.putpixel((xc-y,yc-x),color)


def circle(img,x0,y0,r,color):
    hm=1-r
    x=0
    y=r
    img.putpixel((x0, y0+r), color)
    img.putpixel((x0, y0-r), color)
    img.putpixel((x0+r, y0), color)
    img.putpixel((x0-r, y0), color)
    while x<y:
        if hm<0:
            hm=hm+2*x+3
        else:
            hm=hm+2*x-2*y+5
            y=y-1
        x=x+1  
        point(img,x,y,x0,y0,color)

img2 = Image.new("RGB", (500,500))
circle(img2,200,100,50,(255, 0, 0))
circle(img2,280,100,60,(255, 0, 0))
img2.show() 
