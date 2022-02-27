from PIL import Image
import time
import math

def midpoint_line(img,x0,y0,x1,y1,color):
    #用中点算法画一条直线
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

def draw_rectangle(img,xmin,ymin,xmax,ymax,color):
    #画一个矩形，锚点为左上角的点
    for i in range(xmin,xmax+1):
        img.putpixel((i,ymin),color)
        img.putpixel((i,ymax),color)
    for i in range(ymin,ymax+1):
        img.putpixel((xmin,i),color)
        img.putpixel((xmax,i),color)

def out_code(xx,yy):
    #计算出某个点相对于所画的矩形的out_code,0说明在里面
    out_code=0
    if yy>ymax:
        out_code+=2**3
    else:
        pass
    if yy<ymin:
        out_code+=2**2
    else:
        pass
    if xx>xmax:
        out_code+=2
    else:
        pass
    if xx<xmin:
        out_code+=1
    else:
        pass    
    return out_code

img2 = Image.new("RGB", (500,500))
xmax=300
ymax=200
xmin=100
ymin=50
x0=int(input())
y0=int(input())
x1=int(input())
y1=int(input())
start=out_code(x0,y0)
end=out_code(x1,y1)

k=1
if start|end==0:#起点和终点都在矩形里面
    pass
elif start&end!=0:#起点和终点都在矩形的外面
    x0=y0=x1=y1=0
else:
    if x1-x0!=0:
        m=(y1-y0)/(x1-x0)
    else:
        k=0
        m=1
    if start==0 and end!=0:#起点在矩形里面，终点在外面
        new_x1=x0
        new_y1=y0
        if abs(m)<=1:
            while out_code(int(new_x1+0.5),int(new_y1+0.5))==0:
                if(k!=0):
                    new_x1=new_x1+1
                new_y1=new_y1+m
        else:
            while out_code(int(new_x1+0.5),int(new_y1+0.5))==0:
                if(k!=0):
                    new_y1=new_y1+1    
                new_x1=new_x1+1/m
        x1=int(new_x1)
        y1=int(new_y1)
    if start!=0 and end==0:#起点在矩形外面，终点在里面
        if abs(m)<=1:
            while out_code(int(x0+0.5),int(y0+0.5))!=0:
                if(k!=0):
                    x0=x0+1
                y0=y0+m
        else:
            while out_code(int(x0+0.5),int(y0+0.5))!=0:
                if(k!=0):
                    y0=y0+1
                x0=x0+1/m
        x0=int(x0)
        y0=int(y0)

    if start!=0 and end!=0:#起点和终点都在矩形外面但是直线还是穿过了矩形
        if abs(m)<=1:
            while out_code(int(x0+0.5),int(y0+0.5))!=0:
                if(k!=0):
                    x0=x0+1
                y0=y0+m
        else:
            while out_code(int(x0+0.5),int(y0+0.5))!=0:   
                if(k!=0):
                    y0=y0+1
                x0=x0+1/m
        x0=int(x0)
        y0=int(y0)
        new_x1=x0+1
        new_y1=y0
        if abs(m)<=1:
            while out_code(int(new_x1+0.5),int(new_y1+0.5))==0:
                if(k!=0):
                    new_x1=new_x1+1
                new_y1=new_y1+m
        else:
            while out_code(int(new_x1+0.5),int(new_y1+0.5))==0:   
                if(k!=0):
                    new_y1=new_y1+1
                new_x1=new_x1+1/m
        x1=int(new_x1)
        y1=int(new_y1)


#midpoint_line(img2,100,150,300,150,(255,0,0))
draw_rectangle(img2,xmin,ymin,xmax,ymax,(255,0,0))
midpoint_line(img2,x0,y0,x1,y1,(255,0,0))
print(start)
print(end)
img2.show()
