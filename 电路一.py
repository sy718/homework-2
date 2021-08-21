#输入，用于交互界面
a=eval(input("输入电路代号:"))
R1=eval(input("输入R1电阻值(单位欧姆):"))
R2=eval(input("输入R2电阻值(单位欧姆):"))
R3=eval(input("输入R3电阻值(单位欧姆):"))
R4=eval(input("输入R4电阻值(单位欧姆):"))
U=eval(input("输入电源电压(单位伏):"))

if (a==1):
    #Y转三角形函数
    def Turn1(x,y,z):
        R1,R2,R3=x,y,z
        R12=R1+R2+R1*R2/R3
        R23=R2+R3+R2*R3/R1
        R31=R3+R1+R3*R1/R2
        return R12,R23,R31

    #等效电阻具体计算过程
    R12,R23,R31=Turn1(R1,R2,R3)
    Rp=R4*R23/(R4+R23)
    R=R12*Rp/(R12+Rp)

    #电流计算过程
    I=U/R

    #输出，用于交互界面
    print("I=",I)
else:
    print("不是电路一")#此行无用，只是为了代码能够运行，交互界面做出电路选择即可