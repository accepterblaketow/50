import math
import matplotlib
import matplotlib.pyplot as plt
from numpy import mat
m,C,p=0.145,0.5,1.2
g=9.8
A=math.pi*math.pow(0.0366,2)
D=p*C*A/2
t,dt,tmax=0,0.0001,40

v=float(input('輸入初速度m/s^2\n'))
theta=float(input('輸入角度θ\n'))
x=0
y=float(input('輸入高度m\n'))
vx=v*math.cos(math.radians(theta))
vy=v*math.sin(math.radians(theta))
xxl=[]
yyl=[]
plt.xlabel('x(m)')
plt.ylabel('y(m)')
ax=-(D/m)*v*vx
yy=y
while(t <= tmax):
        xx=vx*t
        yy=y+vy*t-g*math.pow(t,2)/2
        xxl.append(xx)
        yyl.append(yy)
        if(yy<=0 and t>0):
                print("不含空氣阻力射程為"+str(round(xx,2))+"m")
                break
        t+=dt
plt.plot(xxl,yyl,label='Without drag')
t=0
bth=math.acos((g*y/(math.pow(v,2)+g*y)))/2
bx=v*math.cos(bth)
by=v*math.sin(bth)
bxl=[]
byl=[]
yy=y
print("最佳角度為"+str(round(math.degrees(bth),3)))
while(t <= tmax):
        xx=bx*t
        yy=y+by*t-g*math.pow(t,2)/2
        bxl.append(xx)
        byl.append(yy)
        if(yy <= 0 and t>0):
                print("最佳角度射程為"+str(round(xx,2))+"m")
                break
        t+=dt
plt.plot(bxl,byl,label='Best angle')
xl=[0]
yl=[y]
t=0
while(t<=tmax):
        ax=-(D/m)*v*vx
        ay=-g-(D/m)*v*vy   
        vx+=ax*dt
        vy+=ay*dt
        x+=vx*dt+ax*math.pow(dt,2)/2
        y+=vy*dt+ay*math.pow(dt,2)/2
        xl.append(x)
        yl.append(y)
        if(y<=0):
                print("含空氣阻力射程為"+str(round(x,2))+"m")
                break
        t+=dt
plt.plot(xl,yl,label='With drag')
plt.legend(['Without drag','Best angle','With drag'])
plt.show()





