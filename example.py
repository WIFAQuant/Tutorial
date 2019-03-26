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
# 导入绘图工具包。
import seaborn as sns
sns.set(style="darkgrid")
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# 读取本地数据。
data = pd.read_csv(path + "\\Data\\example.csv", index_col=0)
# 重命名列名以
data.columns = ["Stock Codes", "Month", "Monthly Return"]
data["Month"] = pd.to_datetime(data["Month"], format='%m/%d/%Y')
data = data[data["Month"] > pd.to_datetime("2006", format='%Y')]
months_data = pd.DataFrame(data["Month"].unique(), columns=["Month"]).sort_values(by="Month")

report_dataframe = pd.DataFrame(
    index = months_data["Month"], 
    columns = ["Monthly Return", "Annualized Return", "Equity"]
)

monthly_return_list = []
# 编写策略逻辑，并得到每个月的收益率。
for i in range(len(months_data)):
    time = months_data["Month"][i]
    monthly_data = data[data["Month"] == time].dropna()

    if i == 0:
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
    monthly_return_list.append(monthly_return)
    worst_stock = monthly_performance["Stock Codes"].iloc[0]

# 参考基准。
benchmark_data = pd.read_csv(path + "\\Data\\HS300.csv")
benchmark_data = benchmark_data[benchmark_data["Indexcd"] == 300]
benchmark_data = benchmark_data[["Month", "Idxrtn"]]
benchmark_data.columns = ["Month", "Benchmark Return"]
benchmark_data["Month"] = pd.to_datetime(benchmark_data["Month"], format='%Y-%m')
benchmark_data = benchmark_data[benchmark_data["Month"].isin(report_dataframe.index)]
benchmark_data.set_index("Month", inplace=True)

report_dataframe = report_dataframe.join(benchmark_data)
report_dataframe["Annualized Return"] = (report_dataframe["Monthly Return"] + 1) ** 12
report_dataframe["Excess Return"] = report_dataframe["Monthly Return"] - report_dataframe["Benchmark Return"]
report_dataframe["Equity"] = (report_dataframe["Monthly Return"] + 1).cumprod()
report_dataframe["Benchmark Equity"] = (report_dataframe["Benchmark Return"] + 1).cumprod()

average_monthly_return = report_dataframe["Monthly Return"].mean()
print("策略的平均月度收益率为：", round(average_monthly_return * 100, 2), "%；")
print("策略的平均年化收益率为：", round(((average_monthly_return+1)**12-1) * 100, 2), "%；")
total_year = round(len(report_dataframe)/12, 1)
print("策略%s年的平均净值为：%s；" % (total_year, round(report_dataframe["Equity"].mean(), 2)))
print("策略%s年的复合年化收益率为：%s" % (total_year, round((report_dataframe["Equity"][-1]**(1/total_year)-1) * 100, 2)), "%；")
print("策略的夏普值为：%s；" % round(((average_monthly_return+1)**12-1) / report_dataframe["Monthly Return"].std(), 2))

report_dataframe.to_excel(path + "\\Results\\report.xlsx")

plt.figure(figsize=(8, 5))
plt.plot(report_dataframe.index, report_dataframe["Equity"], label="策略净值")
plt.plot(report_dataframe.index, report_dataframe["Benchmark Equity"], label="HS300净值")
plt.legend()
plt.title("策略与HS300净值对比图")
plt.savefig(path + "\\Results\\equity_plot.png")

plt.figure(figsize=(8, 5))
plt.plot(report_dataframe.index, report_dataframe["Monthly Return"], label="策略月度收益率")
plt.plot(report_dataframe.index, report_dataframe["Benchmark Return"], label="HS300月度收益率")
plt.plot(report_dataframe.index, report_dataframe["Excess Return"], label="策略超额收益")
plt.legend()
plt.title("策略与HS300月度收益率对比图")
plt.savefig(path + "\\Results\\return_plot.png")