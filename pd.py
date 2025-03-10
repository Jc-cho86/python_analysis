import pandas as pd
# data=pd.Series([20,10,15])
# # print("最大值",data.max())
# # print("中位數",data.median())
# # data=data*2
# # print(data)
# data=data==20
# print(data)

# data=pd.DataFrame({
#     "name":["Amy","John","Bob"],
#     "salary":[30000,50000,40000]
# })
# print(data)
# print("=================")
# # print(data['name'])
# print(data.iloc[1])


data={"姓名":["小明","曉華","小美"],
      "年齡":[20,22,21],
      "分數":[85,90,88]
}
df=pd.DataFrame(data)
print(df)
