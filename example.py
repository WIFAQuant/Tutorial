# -*- coding: utf-8 -*-
'''
@ Author: WIFA Quant
Created on Tuesday, March 26, 2019
WIFA Quant Tutorial Answer Example
'''

# 导入所需模块。
import os
path = os.getcwd()
import pandas as pd

# 读取本地数据。
data = pd.read_csv(path + "\\example.csv", index_col=0)
data.columns = ["Stock Codes", "Month", "Monthly Return"]
data["Month"] = pd.to_datetime(data["Month"], format='%m/%d/%Y')
months_data = pd.DataFrame(data["Month"].unique(), columns=["Month"])

report_dataframe = pd.DataFrame(
    index = months_data["Month"], 
    columns = ["Monthly Return", "Annualized Return", "Equity"]
)

# 编写策略逻辑，并得到每个月的收益率。
for i in range(len(months_data)):
    time = months_data["Month"][i]
    monthly_data = data[data["Month"] == time].dropna()

    if i == 0:
        print("%s年%s月，交易策略开始。" % (time.year, time.month))
        portfolio = list(monthly_data["Stock Codes"].sample(n=100))
        monthly_performance = monthly_data[monthly_data["Stock Codes"].isin(portfolio)].sort_values(by="Monthly Return")
        worst_stock = monthly_performance["Stock Codes"].iloc[0]

    else:
        new_stock = list(monthly_data["Stock Codes"].sample(n=1))[0]
        portfolio.remove(worst_stock)
        portfolio.append(new_stock)
    
    monthly_performance = monthly_data[monthly_data["Stock Codes"].isin(portfolio)].sort_values(by="Monthly Return")
    monthly_return = monthly_performance["Monthly Return"].mean()
    report_dataframe.loc[time, "Monthly Return"] = monthly_return
    print("%s年%s月当月投资组合收益率为%s，剔除上月最差股票，随机买入一支新股票。" % (time.year, time.month, round(monthly_return, 3)))

    worst_stock = monthly_performance["Stock Codes"].iloc[0]

report_dataframe["Equity"] = (report_dataframe["Monthly Return"] + 1).cumprod()

