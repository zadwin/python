# -*- coding: utf-8 -*-#

#-------------------------------------------------------------------------------
# Name:         drawCluster
# Description:
# Author:       adwin
# Date:         2020-10-18
#-------------------------------------------------------------------------------
import matplotlib.pyplot as plt#约定俗成的写法plt
from numpy import *
# 加载数据
def loadDataSet(fileName):  # 解析文件，按tab分割字段，得到一个浮点数字类型的矩阵
    dataMat = []              # 文件的最后一个字段是类别标签
    fr = open(fileName)
    for line in fr.readlines():
        curLine = line.strip().split('\t')
        fltLine = list(map(float, curLine))    # 将每个元素转成float类型，注意这里一定要转成列表类型。
        dataMat.append(fltLine)
    return dataMat

def draw(data,center,label,k):
    length=len(center)
    fig=plt.figure
    data1 = []
    data2 = []
    data3 = []
    for i in range(k):
        for j in range(len(label)):
            if label[j] == i:
                data1.append(data[j,:])
        data2.append(data1)
        data1 = []
    color = ["#0c0d0b","#640ff0","#0f7ef0","#3ce50e"]
    # s = [13,5,19,25]
    count = 0
    #data2 = array(data2)
    # print(data2)
    # 绘制原始数据的散点图
    for item in data2:
        item = array(item)
        count = count % 4
        c = color[count]
        print(c)
        plt.scatter(item[:, 0], item[:, 1], c=c, s=25, alpha=0.4)
        count = count + 1
    # plt.scatter(data2[:, 0], data2[:, 1], c='#20CED1', s=25, alpha=0.4)
    # plt.scatter(data3[:, 0], data3[:, 1], c='#EECED1', s=25, alpha=0.4)

    # 绘制簇的质心点
    for i in range(length):
        # 不知道这个函数是做什么的？
        plt.annotate('center',xy=(center[i,0],center[i,1]),xytext=\
        (center[i,0]+1,center[i,1]+1),arrowprops=dict(facecolor='red'))
    plt.show()


datMat1 = mat(loadDataSet('数据1.txt'))   #质心
datMat2 = mat(loadDataSet('testSet2.txt'))  #数据集
datMat3 = mat(loadDataSet('数据3.txt'))   #数据标签
draw(array(datMat2),datMat1,datMat3,3)
#draw(datMat2,datMat1)

'''[[ 2.93386365  3.12782785]
 [-2.94737575  3.3263781 ]
 [-0.45965615 -2.7782156 ]]'''