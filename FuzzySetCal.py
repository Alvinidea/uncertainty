import numpy as np
from tkinter import *


def CFRM():
    LSD1 = v1.get().split(',')
    LSD2 = v2.get().split(',')
    i = -1
    j = -1
    for x in LSD1:
        i = i+1
        LSD1[i] = float(LSD1[i])
    for x in LSD2:
        j = j+1
        LSD2[j] = float(LSD2[j])
    # 声明为全局变量
    global FRM
    # 初始化长为 len(LSD1)，宽为 len(LSD1))的矩阵
    FRM = np.mat(np.zeros((len(LSD1), len(LSD1))))
    i = 0
    while i < len(LSD1):
        j = 0
        while j < len(LSD1):
            FRM[i, j] = max([min([LSD1[i], LSD2[j]]), 1-LSD1[i]])
            j = j+1
        i = i + 1
    print(FRM)
    # 一个文本框
    t = Text(frm1, width=30, height=5)
    t.grid(row=2, column=1)
    t.insert(END, FRM)


def CD():
    global FRM
    LSD3 = v3.get().split(',')
    i = -1
    for x in LSD3:
        i = i + 1
        LSD3[i] = float(LSD3[i])
    D = np.mat(np.zeros((1, len(LSD3))))
    i = 0
    while i < len(LSD3):
        j = 0
        while j < len(LSD3):
            D[0, i] = max(min([FRM[j, i], LSD3[j]]), D[0, i])
            j = j + 1
        i = i + 1
    v4.set(D[0])



root = Tk()
frm1 = LabelFrame(root, text=" 计算模糊规则(从 从 A 到 到 B)", padx=40, pady=30)
frm2 = LabelFrame(root, text=" 输入事实并得到结论", padx=40, pady=30)
frm1.pack()
frm2.pack()
root.title(" 模糊推理")
v1 = StringVar()
v2 = StringVar()
v3 = StringVar()
v4 = StringVar()
Label(frm1, text=" 输入 A:").grid(row=0, column=0)
Label(frm1, text=" 输入 B:").grid(row=1, column=0)
Label(frm2, text=" 输入 A:").grid(row=3, column=0)
Button(frm1, command=CFRM, text="点击计算").grid(row=2, column=0)
Button(frm2, command=CD, text="点击计算").grid(row=4, column=0)
e1 = Entry(frm1, textvariable=v1).grid(row=0, column=1, padx=10, pady=10)
e2 = Entry(frm1, textvariable=v2).grid(row=1, column=1, padx=10, pady=10)
e3 = Entry(frm2, textvariable=v3).grid(row=3, column=1, padx=10, pady=10)
e4 = Entry(frm2, textvariable=v4).grid(row=4, column=1, padx=10, pady=10)
root.mainloop()