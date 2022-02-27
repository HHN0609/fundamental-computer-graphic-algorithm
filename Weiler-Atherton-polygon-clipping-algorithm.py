from PIL import Image
import time
import math
#本算法的裁剪边框只能是矩形，能力有限，其他形状的求交点太麻烦了

color=(255, 0, 0)
img2 = Image.new("RGB", (500,500))

#引入中点画线算法
def midpoint_line(img,x0,y0,x1,y1,color):
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
    return 1


def Liang_barsky(xmin,ymin,xmax,ymax,x1,y1,x2,y2):
    if(x2<x1):
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
                    if x1>xmax:
                        n=1
                        break
                    if y1>y2:
                        t=y2
                        y2=y1
                        y1=t
                    #是一条竖直的直线
                    y1=max(y1,ymin)
                    y2=min(y2,ymax)
                    midpoint_line(img2,x1,y1,x2,y2,color)
                    n=1
                    break

                if(k==3 or k==4):
                    if y1>ymax:
                        n=1
                        break
                    #是一条水平的直线
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



# 边框坐标
bkzb=[[50,50],[50,150],[250,150],[150,50]]
y_max=max(bkzb,key=lambda k: k[1])[1]
x_max=max(bkzb,key=lambda k: k[0])[0]
y_min=min(bkzb,key=lambda k: k[1])[1]
x_min=min(bkzb,key=lambda k: k[0])[0]
# print(x_min,x_max,y_min,y_max)

#画一个外边框
midpoint_line(img2, 50, 50, 250,50, color)
midpoint_line(img2, 250, 50, 250, 150, color)
midpoint_line(img2, 50, 150, 250, 150, color)
midpoint_line(img2, 50, 50, 50, 150, color)

# 被裁剪多边形的顶点坐标
# ddzb=[[110,160],[110,110],[150,110],[150,200],[0,200],[0,0],[220,0],[220,90],[180,90],[180,40],[40,40],[40,160]]
# 顺时针
ddzb=[[40,160],[40,40],[180,40],[180,90],[220,90],[220,0],[0,0],[0,200],[150,200],[150,110],[110,110],[110,160]]
n=len(ddzb)
for i in range(0,n):
    # midpoint_line(img2,ddzb[(i+n)%n][0],ddzb[(i+n)%n][1],ddzb[(i+n+1)%n][0],ddzb[(i+n+1)%n][1],color)
    Liang_barsky(x_min,y_min,x_max,y_max,ddzb[(i+n)%n][0],ddzb[(i+n)%n][1],ddzb[(i+n+1)%n][0],ddzb[(i+n+1)%n][1])


img2.show()
# print(t)

