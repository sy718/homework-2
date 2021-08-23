# △-Y转换
def turn2(R1, R2, R3):
    r1 = R1 * R3 / (R1 + R2 + R3)
    r2 = R1 * R2 / (R1 + R2 + R3)
    r3 = R2 * R3 / (R1 + R2 + R3)
    return r1,r2,r3


def calculate2(R1, R2, R3, R4, U):

    # 等效电阻具体计算过程
    r1, r2, r3 = turn2(R1, R2, R3)
    Rp = 1 / (1 / (r2 + R4) + r3)  # 并联
    R = Rp + r1

    # 电流计算过程
    I = U / R

    # 返回，用于交互界面
    return I