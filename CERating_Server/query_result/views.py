from django.shortcuts import render
from django.http import JsonResponse
from decimal import *
from django.http import HttpResponse
from django.core import serializers
from query_result.models import level_result
# Create your views here.
from enterprise_simurate.models import Enterprise
import numpy as np
import pandas as pd

w = np.array([0.167,0.167,0.071,0.063,0.056,0.071,0.071,0.167,0.167])

#计算企业矩阵
# data = (1，2，3，4，5，6，7，8，9)1*9矩阵   指标要与临界值矩阵指标对齐，临界值x1~x5从小到大排序
# 临界值 =(X1,X2,X3,X4,X5)9*5矩阵
_no_value = object()
def mat(data,linjiezhi,u = _no_value):
    matrix = np.array([[0,0,0,0,0],
                      [0,0,0,0,0],
                      [0,0,0,0,0],
                      [0,0,0,0,0],
                      [0,0,0,0,0],
                      [0,0,0,0,0],
                      [0,0,0,0,0],
                      [0,0,0,0,0],
                      [0,0,0,0,0]])
    for i in range(9):
        if i == 0:
            if data[0]==1:
                matrix[i][1] = 1
            elif data[0] == 0:
                matrix[i][4] = 1
        #2，8，9行红色字体，运算顺序从第一个到第五个，i代表矩阵第i行，j代表第j列定位矩阵元素，临界值矩阵
        elif i ==1 or i ==7 or i ==8:
            for j in range(5):
                if j ==0:
                    if data[i] >= linjiezhi[i][4]:
                        matrix[i][j] = 1
                    elif data[i] >= linjiezhi[i][3] and data[i] < linjiezhi[i][4]:
                        matrix[i][j] = (data[i] - linjiezhi[i][3]) / (linjiezhi[i][4] - linjiezhi[i][3])
                    elif data[i] < linjiezhi[i][3]:
                        matrix[i][j] = 0
                elif j ==1:
                    if data[i] >= linjiezhi[i][3] and data[i]<linjiezhi[i][4]:
                        matrix[i][j] = (linjiezhi[i][4] - data[i]) / (linjiezhi[i][4] - linjiezhi[i][3])
                    elif data[i] >= linjiezhi[i][2] and data[i] < linjiezhi[i][3]:
                        matrix[i][j] = (data[i] - linjiezhi[i][2]) / (linjiezhi[i][3] - linjiezhi[i][2])
                    else:
                        matrix[i][j] = 0
                #从这里往下改，框架已经搭好了
                elif j ==2:
                    if data[i] >= linjiezhi[i][2] and data[i]<linjiezhi[i][3]:
                        matrix[i][j] = (linjiezhi[i][3] - data[i]) / (linjiezhi[i][3] - linjiezhi[i][2])
                    elif data[i] >= linjiezhi[i][1] and data[i] < linjiezhi[i][2]:
                        matrix[i][j] = (data[i] - linjiezhi[i][1]) / (linjiezhi[i][2] - linjiezhi[i][1])
                    else:
                        matrix[i][j] = 0

                elif j ==3:
                    if data[i] >= linjiezhi[i][1] and data[i]<linjiezhi[i][2]:
                        matrix[i][j] = (linjiezhi[i][2] - data[i]) / (linjiezhi[i][2] - linjiezhi[i][1])
                    elif data[i] >= linjiezhi[i][0] and data[i] < linjiezhi[i][1]:
                        matrix[i][j] = (data[i] - linjiezhi[i][0]) / (linjiezhi[i][1] - linjiezhi[i][0])
                    else:
                        matrix[i][j] = 0

                elif i ==4:
                    if data[i] <=linjiezhi[i][0]:
                        matrix[i][j] = 1
                    elif data[i] > linjiezhi[i][1]:
                        matrix[i][j] = 0
                    elif data[i] > linjiezhi[i][0] and data[i]<=linjiezhi[i][1]:
                        matrix[i][j] = (linjiezhi[i][1] - data[i]) / (linjiezhi[i][1] - linjiezhi[i][0])
        #3~7为紫色字体，运行计算顺序应当逆序
        elif i>=2 and i<=6:
            for j in range(5):
                if j == 4:
                    if data[i] >= linjiezhi[i][4]:
                        matrix[i][j] = 1
                    elif data[i] >= linjiezhi[i][3] and data[i] < linjiezhi[i][4]:
                        matrix[i][j] = (data[i] - linjiezhi[i][3]) / (linjiezhi[i][4] - linjiezhi[i][3])
                    elif data[i] < linjiezhi[i][3]:
                        matrix[i][j] = 0
                elif j == 3:
                    if data[i] >= linjiezhi[i][3] and data[i] < linjiezhi[i][4]:
                        matrix[i][j] = (linjiezhi[i][4] - data[i]) / (linjiezhi[i][4] - linjiezhi[i][3])
                    elif data[i] >= linjiezhi[i][2] and data[i] < linjiezhi[i][3]:
                        matrix[i][j] = (data[i] - linjiezhi[i][2]) / (linjiezhi[i][3] - linjiezhi[i][2])
                    else:
                        matrix[i][j] = 0
                # 从这里往下改，框架已经搭好了
                elif j == 2:
                    if data[i] >= linjiezhi[i][2] and data[i] < linjiezhi[i][3]:
                        matrix[i][j] = (linjiezhi[i][3] - data[i]) / (linjiezhi[i][3] - linjiezhi[i][2])
                    elif data[i] >= linjiezhi[i][1] and data[i] < linjiezhi[i][2]:
                        matrix[i][j] = (data[i] - linjiezhi[i][1]) / (linjiezhi[i][2] - linjiezhi[i][1])
                    else:
                        matrix[i][j] = 0

                elif j == 1:
                    if data[i] >= linjiezhi[i][1] and data[i] < linjiezhi[i][2]:
                        matrix[i][j] = (linjiezhi[i][2] - data[i]) / (linjiezhi[i][2] - linjiezhi[i][1])
                    elif data[i] >= linjiezhi[i][0] and data[i] < linjiezhi[i][1]:
                        matrix[i][j] = (data[i] - linjiezhi[i][0]) / (linjiezhi[i][1] - linjiezhi[i][0])
                    else:
                        matrix[i][j] = 0

                elif i == 0:
                    if data[i] <= linjiezhi[i][0]:
                        matrix[i][j] = 1
                    elif data[i] > linjiezhi[i][1]:
                        matrix[i][j] = 0
                    elif data[i] > linjiezhi[i][0] and data[i] <= linjiezhi[i][1]:
                        matrix[i][j] = (linjiezhi[i][1] - data[i]) / (linjiezhi[i][1] - linjiezhi[i][0])
        # print(matrix,"第",i+1,"个指标")
    return matrix
#矩阵相乘np.DOT(matrix,w)=>1*5矩阵
#f返回评级矩阵取最大值exemple.max()用这个方法
def matrixMultiply(A, B):
    # 获取A的行数和列数
    if len(np.shape(A))>1:
        (A_row, A_col) = (np.shape(A))[0], (np.shape(A))[1]
    else:
        (A_row, A_col) = 1,(np.shape(A))[0]
    # 获取B的行数和列数
    if len(np.shape(B))>1:
        (B_row, B_col) = (np.shape(B))[0], (np.shape(B))[1]
    else:
        (B_row, B_col) = 1,(np.shape(B))[0]
    # print(np.shape(A))
    # print(np.shape(B))
    # print(A_row, A_col)便于理解
    # print(B_row, B_col)
    # 不能运算情况的判断
    if (A_col != B_row):
        raise ValueError

    # 最终的矩阵
    result = []
    rowItem = []
    # zip 解包后是转置后的元组，强转成list, 存入result中
    BT = [list(row) for row in zip(*B)]
    # print(A)
    # print(BT)

    # 开始做乘积运算
    for A_index in range(A_row):
        # 用于记录新矩阵的每行元素
        for B_index in range(len(BT)):
            # num 用于累加
            # num = 0
            for Br in range(len(BT[B_index])):
                # print(A_index,B_index,Br)这个特别直观理解模型
                if A_index>=1:
                    rowItem.append(A[A_index][Br] * BT[B_index][Br])
                elif A_index == 0:
                    rowItem.append(A[Br] * BT[B_index][Br])
            result.append(max(rowItem))
            rowItem.clear()
    return result
def query_result(request):
    em = request.POST.get('email')  # 相关负责人邮箱地址
    oob = Enterprise.objects.get(email=em) #获取余额
    st = request.POST.get('session')   #获取登陆状态
    # le = request.POST.get('level')  # 企业评级
    # 用户未登录返回code：1
    if st != 1:
        data = {"code": 1}
        return JsonResponse(data)
    else:
        # 余额不足返回code:2
        if (oob.simulate_count <= 0 or oob.simulate_count is None):
            data = {"code": 2}
            return JsonResponse(data)
        else:
            if request.method == 'POST':
                one = request.POST.get('The_level_of_concern')
                two = request.POST.get('environmental_policies')
                three = request.POST.get('CO2_emissions')
                four = request.POST.get('Waste_discharge')
                five = request.POST.get('Discharge_wastewater')
                six = request.POST.get('COD_emissions')
                seven = request.POST.get('Combined_energy_consumption')
                eight = request.POST.get('R&D_investment')
                nine = request.POST.get('Environmental_investment')
                A = np.array([one,two,three,four,five,six,seven,eight,nine])
                E = np.array([
        [1, 1, 1, 1, 1],
        [4, 5, 6, 11, 17],
        [130, 280, 445, 950, 8500],
        [3, 22, 35, 140, 14000],
        [30, 350, 1500, 4000, 8500],
        [10, 20, 55, 1500, 20000],
        [15.5, 85, 220, 550, 2500],
        [22, 122, 345, 450, 720],
        [4, 10, 20, 54, 150],

    ])
                matrix = mat(A, E)
                w = np.array([0.167, 0.167, 0.071, 0.063, 0.056, 0.071, 0.071, 0.167, 0.167])
                # 开始运算，得出结果，返回评级，和code：0 要把函数放在这里吗
                # 运算...
                # 返回运算值
                result = matrixMultiply(w, matrix)
                data = {"code": 0}
                return JsonResponse(result,data)





