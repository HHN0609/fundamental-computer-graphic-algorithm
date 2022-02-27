from PIL import Image
import time
import math
    
AET=[]#活性边表
bianbiao=[]#总边表
ddzb=[]#顶点坐标
e=[]#小边表
ymax=0
img2 = Image.new("RGB", (500,500))
color=(255,0,0)

n=int(input()) #输入顶点的个数
# 输入顶点坐标
for i in range(0,n):
    ddzb.append([int(input()),int(input())])
# print(ddzb)

#最大的y和最小的y
y_max=max(ddzb,key=lambda k: k[1])
y_min=min(ddzb,key=lambda k: k[1])

#建立边表
for i in range(y_min[1],y_max[1]):
    e=[]
    for j in range(0,n):
        if ddzb[j][1]==i:
            #遍历到的坐标为极小值，算两个点，相邻的两个坐标的y值都大于它的y值
            if ddzb[(j+1+n)%n][1]>=ddzb[j][1] and ddzb[(j-1+n)%n][1]>=ddzb[j][1]:
                #先算一侧的数据
                ymax=ddzb[(j+1+n)%n][1]
                xi=min(ddzb[j],ddzb[(j+1+n)%n],key=lambda k: k[1])[0]
                if ddzb[j][1]-ddzb[(j+1+n)%n][1]==0:
                    pass
                else:
                    m=(ddzb[j][0]-ddzb[(j+1+n)%n][0])/(ddzb[j][1]-ddzb[(j+1+n)%n][1])#dx/dy
                    e.append([ymax,xi,round(m,2)])
                #再算另一侧的数据
                ymax=ddzb[(j-1+n)%n][1]
                xi=min(ddzb[j],ddzb[(j-1+n)%n],key=lambda k: k[1])[0]
                if ddzb[j][1]-ddzb[(j-1+n)%n][1]==0:
                    pass
                else:
                    m=(ddzb[j][0]-ddzb[(j-1+n)%n][0])/(ddzb[j][1]-ddzb[(j-1+n)%n][1])#dx/dy
                    e.append([ymax,xi,round(m,2)])
            #遍历到的值为普通点，算一个点
            if  (ddzb[(j+1+n)%n][1]-ddzb[j][1])*(ddzb[(j-1+n)%n][1]-ddzb[j][1])<0:

                if ddzb[(j+1+n)%n][1]>ddzb[(j-1+n)%n][1]:
                    ymax=ddzb[(j+1+n)%n][1]
                    xi=min(ddzb[j],ddzb[(j+1+n)%n],key=lambda k: k[1])[0]
                    if ddzb[j][1]-ddzb[(j+1+n)%n][1]==0:
                        pass
                    else:
                        m=(ddzb[j][0]-ddzb[(j+1+n)%n][0])/(ddzb[j][1]-ddzb[(j+1+n)%n][1])#dx/dy
                        e.append([ymax,xi,round(m,2)])
                else:
                    ymax=ddzb[(j-1+n)%n][1]
                    xi=min(ddzb[j],ddzb[(j-1+n)%n],key=lambda k: k[1])[0]
                    if ddzb[j][1]-ddzb[(j-1+n)%n][1]==0:
                        pass
                    else:
                        m=(ddzb[j][0]-ddzb[(j-1+n)%n][0])/(ddzb[j][1]-ddzb[(j-1+n)%n][1])#dx/dy
                        e.append([ymax,xi,round(m,2)])
    if  e!=[]:
        e.sort(key=lambda k: k[1])
        bianbiao.append(e)
    else:
        bianbiao.append([])
# print(bianbiao)
AET=bianbiao[0]
# print(AET)
c=0
for i in range(y_min[1],y_max[1]):
    y_now=i
    index=i-y_min[1]#对映边表中的下标

    #判断AET中有没有要删除的边的数据结构
    ATE_lenght=len(AET)
    mark=[]#用来记录可以留下来的边的下标
    for j in range(0,ATE_lenght):
        if y_now < int(AET[j][0]):
            mark.append(j)
    AET_unreal=[]
    for t in range(0,len(mark)):
        AET_unreal.append(AET[mark[t]])
    AET=AET_unreal

    #判断AET中有没有添加的边的数据结构
    if bianbiao[index]!=[] and index!=0:
        for k in range(0,len(bianbiao[index])):
            AET.append(bianbiao[index][k])
   #开始填充
    if AET!=[]:
        AET.sort(key=lambda k: k[1])
        for k in range(0,len(AET),2):
            for m in range(int(AET[k][1]+0.5),int(AET[k+1][1])+1):
                img2.putpixel((m,y_now),color)        
            AET[k][1]=AET[k][1]+AET[k][2]
            AET[k+1][1]=AET[k+1][1]+AET[k+1][2]
            
img2.show()
               
        
        






