# Y-△角转换
def turn1(R1, R2, R3):
    R12 = R1 + R2 + R1 * R2 / R3
    R23 = R2 + R3 + R2 * R3 / R1
    R31 = R3 + R1 + R3 * R1 / R2
    return R12, R23, R31


def calculate1(R1, R2, R3, R4, U):

    # 等效电阻具体计算过程
    R12, R23, R31 = turn1(R1, R2, R3)
    Rp = R4 * R23 / (R4 + R23)
    R = R12 * Rp / (R12 + Rp)

    #电流计算过程
    I = U / R

    #返回，用于交互界面
    return I

