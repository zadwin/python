# -*- coding: utf-8 -*-#

#-------------------------------------------------------------------------------
# Name:         drawCluster
# Description:  这个文件主要用于绘制图像，需要传入指定的文本(csv或者txt)
#                   且必须为三种数据，原始数据集合、中心点、点的标签
# Author:       adwin
# Date:         2020-10-18
#-------------------------------------------------------------------------------
import matplotlib.pyplot as plt#约定俗成的写法plt
from numpy import *
# 加载数据，注意区分加载的文件是csv还是txt文件。
def loadDataSet(fileName):  # 解析文件txt，按tab分割字段，得到一个浮点数字类型的矩阵(解析csv文件一般用','作为分隔符)
    dataMat = []              # 文件的最后一个字段是类别标签
    fr = open(fileName)
    for line in fr.readlines():
        curLine = line.strip().split(',')
        fltLine = list(map(float, curLine))    # 将每个元素转成float类型，注意这里一定要转成列表类型。
        dataMat.append(fltLine)
    return dataMat

#图像的绘制，
# data：数据集合,
# center：中心点,
# labels：标签，用于区分数据属于哪一簇,
# k：聚类的数量。
def draw(data,center,labels,k):
    length=len(center)
    # fig=plt.figure
    data1 = []
    data2 = []
    data3 = []
    for i in range(k):
        for j in range(len(labels)):
            if labels[j] == i:
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

#数据加载，转化成列表的形式。
myCentroids = mat(loadDataSet('质心.csv'))   #质心
datMat = mat(loadDataSet('ban.csv'))  #数据集
labels = mat(loadDataSet('标签.csv'))   #数据标签
draw(array(datMat),myCentroids,labels,2)


