#输入，用于交互界面
a=eval(input("输入电路代号:"))
R1=eval(input("输入R1电阻值(单位欧姆):"))
R2=eval(input("输入R2电阻值(单位欧姆):"))
R3=eval(input("输入R3电阻值(单位欧姆):"))
R4=eval(input("输入R4电阻值(单位欧姆):"))
U=eval(input("输入电源电压(单位伏):"))

if (a==2):
    #三角形转Y函数
    def Turn1(x,y,z):
        R1,R2,R3=x,y,z
        r1=R1*R3/(R1+R2+R3)
        r2=R1*R2/(R1+R2+R3)
        r3=R2*R3/(R1+R2+R3)
        return r1,r2,r3

    #等效电阻具体计算过程
    r1,r2,r3=Turn1(R1,R2,R3)
    Rp=1/(1/(r2+R4)+r3)  #并联
    R=Rp+r1

    #电流计算过程
    I=U/R

    #输出，用于交互界面
    print("I=",I)
else:
    print("不是电路一")#此行无用，只是为了代码能够运行，交互界面做出电路选择即可