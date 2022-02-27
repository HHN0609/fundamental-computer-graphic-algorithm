from PIL import Image
import time
import math

def midpoint_line(img,x0,y0,x1,y1,color):
    #用中点算法画一条直线
    if x0>x1 or (x0==x1 and y0>y1):
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

def draw_rectangle(img,xmin,ymin,xmax,ymax,color):
    #画一个矩形，锚点为左上角的点
    for i in range(xmin,xmax+1):
        img.putpixel((i,ymin),color)
        img.putpixel((i,ymax),color)
    for i in range(ymin,ymax+1):
        img.putpixel((xmin,i),color)
        img.putpixel((xmax,i),color)

xmin=50
ymin=50
xmax=250
ymax=150
color=(255,0,0)
img2 = Image.new("RGB", (500,500))
draw_rectangle(img2,xmin,ymin,xmax,ymax,color)

x1=int(input())
y1=int(input())
x2=int(input())
y2=int(input())
if(x1>x2):
    t=x2
    x2=x1
    x1=t
    t=y2
    y2=y1
    y1=t
u1=[0]
u2=[1]
dx=x2-x1
dy=y2-y1
n=0
if dy<0:
    m=-1
else:
    m=1
p=[0,-dx,dx,-dy,dy]
q=[0,x1-xmin,xmax-x1,y1-ymin,ymax-y1]
for k in range(1,5):
    if p[k]==0:
        if q[k]<0:
            n=1
            break
        else:
            if(k==1 or k==2):
                #是一条竖直的直线
                if y1>y2:
                    t=y2
                    y2=y1
                    y1=t
                if x1>xmax:
                    n=1
                    break
                y1=max(y1,ymin)
                y2=min(y2,ymax)
                midpoint_line(img2,x1,y1,x2,y2,color)
                n=1
                break

            if(k==3 or k==4):
                #是一条水平的直线
                if y1>ymax:
                    n=1
                    break
                x1=max(x1,xmin)
                x2=min(x2,xmax)
                midpoint_line(img2,x1,y1,x2,y2,color)
                n=1
                break

if n==0 :
    for k in range(1,5):
        u=round(q[k]/p[k],2)
        if p[k]<0:
            u1.append(u)
        else:
            u2.append(u)

    if max(u1)>min(u2):
        pass
    else:
        x2=int(x1+min(u2)*dx)
        y2=int(y1+min(u2)*dy)
        x1=int(x1+max(u1)*dx)
        y1=int(y1+max(u1)*dy)
        midpoint_line(img2,x1,y1,x2,y2,color)
print(x1,y1,x2,y2)
print(u1,u2)
print(n)
img2.show()
