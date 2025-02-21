import numpy as np
# ndarr=np.array([3,4,-5])
# print(ndarr)
# # print(ndarr.size)#資料的數量
# data=np.array([3,2,6,4,])
# print(data)
# data=np.empty(4)#創造一個四個資料的一維陣列，資料未指定
# print(data)
# data=np.zeros(3)
# print(data)
# data=np.ones(3)
# print(data)
# data=np.arange(8)
# print(data)
# data=np.array([ #3x3的二維陣列
#     [2,3,2],
#     [1,5,2],
#     [4,2,1]
# ])
# print(data)
# data=np.empty([3,3])
# print(data)
# data=np.ones([2,3])
# print(data)
# data=np.array([ #2x2x2三維陣列
# #     [
#         [3,1],[1,2]
#     ],
#     [
#         [2,5],[10,2]
#     ]
# ])
# print(data)
# data=np.zeros([3,1,3]) #3x1x3三維陣列
# # print(data)
# data=np.array([ #1x1x2x3四維陣列
# #     [
#         [
#             [3,2,1],
#             [5,5,10]
#         ]
#     ]
# ])
# print(data)
# data=np.ones([2,1,1,2])  #2x1x1x2 四維陣列
# print(data)
# data=np.zeros([2,2,1,2])  #2x2x1x2 四維陣列
# print(data)


# data1=np.array([3,2,10])
# data2=np.array([1,3,6])
# result=data1+data2
# print("加法",result)
# result=data1*data2
# print("乘法",result)
# result=data1>data2
# print("大於",result)
# result=data1==data2
# print("是否相等",result)

# data1=np.array([
#     [1,3]
# ]) #1x2
# data2=np.array([
#     [2,-1,3],
#     [-2,4,1]
# ]) #2x3
# result=data1.dot(data2)
# print(result)
# result=data1@(data2)
# print("內積",result) 
# result=np.outer(data1,data2)
# print("外積",result)


# data=np.array([
#     [2,1,7],
#     [-5,3,8]
# ]) #2x3

# result=data.cumsum(axis=0)  #針對第一個維度逐值累加  colum
# print(result)

# result=data.cumsum(axis=1)  #針對第一個維度逐值累加  row
# print(result)

# result=data.sum(axis=0) #針對第一個維度做總和  欄colum
# print(result)
# result=data.sum(axis=1) #針對第二個維度做總和  列row
# print(result)

# result=data.max(axis=0)
# print(result)

# result=data.max(axis=1)
# print(result)

# result=data.mean(axis=1)
# print(result)

# result=data.sum()
# print("總和",result)
# result=data.max()
# print("最大值",result)
# result=data.mean()
# print("平均數",result)
# result=data.std()
# print("標準差",result)

# data=np.ones(10)
# print(data.shape)
# data=np.array([
#     [3,1,5],
#     [1,2,3]
# ])
# print(data.shape)

# data=np.array([
#     [2,4,1],
#     [1,5,0]
# ])
# print(data.shape)
# # print(data.T.shape)

# data=np.array([
#     [
#         [2,1,3],[1,2,3]
#     ],
#     [
#         [0,2,1],[8,9,10]
#     ]
# ])
# # newsata=data.ravel()
# # print(newsata)
# # print(newsata.shape)

# newdata=data.reshape(1,2,6)
# print(newdata)
# print(newdata.shape)

# data=np.zeros(18).reshape(3,2,3)
# print(data)

# data=np.arange(9).reshape(3,3)
# print(data)
# print(data.T)

# data=np.array([1,5,2,10])
# print(data[1])

# data=np.array([
#     [0,1,],
#     [10,-5],
#     [2,6]
# ])
# print(data[0,1])
# print(data[1,0])
# print(data[2,0])

# data=np.array([-1,-5,2,3])
# print(data[0:3])
# print(data[0:2])
# print(data[2:])

# data=np.array([
#     [0,1,2],[3,4,5,],
#     [5,4,3],[2,1,0]
# ])
# print(data[1:3,0:2])
# print(data[0:2,1])

# data=np.array([
#     [
#         [8,1,3],
#         [-5,5,2]
#     ],
#     [
#         [0,1,6],
#         [4,4,-3]
#     ]
# ])
# print(data[0,...])
# print("=============")
# # print(data[...,1:3])

# arrl=np.array([
#     [1,2,3],
#     [4,5,6]
# ])
# arr2=np.array([
#     [7,8,9],
#     [10,11,12]
# ])
# arr3=np.array([
#     [13,14],
#     [15,16]
# ])

# # result1=np.vstack((arrl,arr2))
# # print(result1)

# result2=np.hstack((arrl,arr2,arr3))
# print(result2)

# arr=np.array([
#     [2,4,6,8,10,12],
#     [1,3,5,7,9,11]
# ])
# # result=np.vsplit(arr,2)
# # print(result)

# # result2=np.hsplit(arr,2)
# # print(result2)
# result=np.hsplit(arr,3)
# print(result)
