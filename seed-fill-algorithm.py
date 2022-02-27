#填充一个圆形图案
from PIL import Image
import random
import time
import sys  # 导入sys模块
sys.setrecursionlimit(3000000)
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
boundary_color=(255,0,0)
inter_color=(255,0,0)
circle(img2,200,100,100,boundary_color)

'''
#递归算法版本
def fill_color(x,y,boundary_color,inter_color,img2):
    if img2.getpixel((x,y))!=boundary_color and img2.getpixel((x,y))!=inter_color:
        img2.putpixel((x,y),boundary_color)
        fill_color(x,y+1,boundary_color,inter_color,img2)
        fill_color(x,y-1,boundary_color,inter_color,img2)
        fill_color(x+1,y,boundary_color,inter_color,img2)
        fill_color(x-1,y,boundary_color,inter_color,img2)
fill_color(200,100,boundary_color,inter_color,img2)
'''
s=[]
x=200
y=100
s.append((x,y))
while len(s)!=0:
    a=s.pop(-1)
    if img2.getpixel(a)!=inter_color and img2.getpixel(a)!=boundary_color:
        img2.putpixel(a,inter_color)
        s.append((a[0],a[1]+1))    
        s.append((a[0],a[1]-1))
        s.append((a[0]+1,a[1]))
        s.append((a[0]-1,a[1]))
img2.show() 
