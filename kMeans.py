#!/usr/bin/python
# coding=utf-8
import matplotlib.pyplot as plt#约定俗成的写法plt
from numpy import *
import datetime
# 导入CSV安装包
import csv

starttime = datetime.datetime.now()
# 加载数据，注意区分加载的文件是csv还是txt文件。
def loadDataSet(fileName):  # 解析文件，按tab分割字段，得到一个浮点数字类型的矩阵
    dataMat = []              # 文件的最后一个字段是类别标签
    fr = open(fileName)
    for line in fr.readlines():
        curLine = line.strip().split('\t')
        fltLine = list(map(float, curLine))    # 将每个元素转成float类型，注意这里一定要转成列表类型。只是换了里面的类型。
        dataMat.append(fltLine)
    return dataMat

# 计算欧几里得距离
def distEclud(vecA, vecB):
    return sqrt(sum(power(vecA - vecB, 2))) # 求两个向量之间的距离

# 构建聚簇中心，取k个(此例中为4)随机质心
def randCent(dataSet, k):
    n = shape(dataSet)[1]
    centroids = mat(zeros((k,n)))   # 每个质心有n个坐标值，总共要k个质心
    for j in range(n):
        minJ = min(dataSet[:,j])
        maxJ = max(dataSet[:,j])
        rangeJ = float(maxJ-minJ)
        centroids[:,j] = minJ + rangeJ * random.rand(k, 1)
    return centroids

# k-means 聚类算法
def kMeans(dataSet, k, distMeans =distEclud, createCent = randCent):
    m = shape(dataSet)[0]   #它的作用是可以得到数据的维数，此处是（80*2）。
    clusterAssment = mat(zeros((m,2)))    # 用于存放该样本属于哪类及质心距离
    # clusterAssment第一列存放该数据所属的中心点，第二列是该数据到中心点的距离
    centroids = createCent(dataSet, k)
    clusterChanged = True   # 用来判断聚类是否已经收敛
    while clusterChanged:
        clusterChanged = False;
        for i in range(m):  # 把每一个数据点划分到离它最近的中心点
            minDist = inf;  # 最小距离（记录数据离k个质心的距离）
            minIndex = -1;  # 最小距离的下标（记录数据离哪一个质心最近）
            for j in range(k):
                distJI = distMeans(centroids[j,:], dataSet[i,:])
                if distJI < minDist:
                    minDist = distJI; minIndex = j  # 如果第i个数据点到第j个中心点更近，则将i归属为j
            if clusterAssment[i,0] != minIndex: clusterChanged = True;  # 如果分配发生变化，则需要继续迭代
            clusterAssment[i,:] = minIndex,minDist**2   # 并将第i个数据点的分配情况存入字典
        for cent in range(k):   # 重新计算中心点
            ptsInClust = dataSet[nonzero(clusterAssment[:,0].A == cent)[0]]   # 去第一列等于cent的所有列
            centroids[cent,:] = mean(ptsInClust, axis = 0)  # 算出这些数据的中心点
    return centroids, clusterAssment

# 保存csv文件。
def saveAsCsv(data,fileName):
    # 1. 创建文件对象，这里主要用于将标签数据存入文件中。
    f = open(fileName,'w', encoding='utf-8', newline="")
    labels = []
    # 2. 基于文件对象构建 csv写入对象
    csv_writer = csv.writer(f)
    for item in data:
        i = []
        item = array(item)
        i.append(item[0])
        labels.append(item[0])
        csv_writer.writerow(i)
    # 5. 关闭文件
    f.close()
    return labels


#图像的绘制，
# data：数据集合,
# center：中心点,
# labels：标签，用于区分数据属于哪一簇,
# k：聚类的数量。
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
    # 绘制原始数据的散点图
    for item in data2:
        item = array(item)
        count = count % 4
        c = color[count]
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




# --------------------测试----------------------------------------------------
# 用测试数据及测试kmeans算法
k = 4
datMat = mat(loadDataSet('testSet.txt'))
myCentroids,clustAssing = kMeans(datMat,k)
print(myCentroids)
labels = []
data = array(clustAssing)
fileName = '标签p.csv'
labels = saveAsCsv(data,fileName)
endtime = datetime.datetime.now()
print((endtime - starttime))
draw(array(datMat),myCentroids,labels,k)
