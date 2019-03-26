# -*- coding: utf-8 -*-
'''
@ Author: WIFA Quant
Created on Tuesday, March 26, 2019
WIFA Quant Tutorial Answer Example
'''

# 导入所需模块。
import os           # 系统模块
path = os.getcwd()  # 当前工作路径
import pandas as pd # 数据表操作
# 导入绘图工具包。
import seaborn as sns                                      # 绘图包
sns.set(style="darkgrid")                                  # 设置绘图风格
import matplotlib.pyplot as plt                            # 绘图包
plt.rcParams['font.sans-serif'] = ['SimHei']               # 显示简体中文 
plt.rcParams['axes.unicode_minus'] = False                 # 显示负号
from pandas.plotting import register_matplotlib_converters # 自动在绘图时转换日期
register_matplotlib_converters()                           # 注册日期转换器

# 读取本地数据。
data = pd.read_csv(path + "\\Data\\example.csv", index_col=0)
# 重命名列名，看起来舒服些。
data.columns = ["Stock Codes", "Month", "Monthly Return"]
# 将字符串格式的日期转换为日期格式，方便进行时间序列操作。
data["Month"] = pd.to_datetime(data["Month"], format='%m/%d/%Y')
# 只取2006年之后的数据。
data = data[data["Month"] > pd.to_datetime("2006", format='%Y')]
# 生成一个包含每个月的数据表，这一步也可通过pd.date_range手工生成所需日期，这里采用原始数据取集合得到。
months_data = pd.DataFrame(data["Month"].unique(), columns=["Month"]).sort_values(by="Month")

# 生成最终报告的数据表，方便后续填写。
report_dataframe = pd.DataFrame(
    index = months_data["Month"], 
    columns = ["Monthly Return", "Annualized Return", "Equity"]
)

# 开始编写策略逻辑，遍历每个月。
for i in range(len(months_data)):

    time = months_data["Month"][i] # 当前月份是几月，存储为time变量
    monthly_data = data[data["Month"] == time].dropna() # 当前月份的数据，剔除NA数据

    # 如果是第一个月。
    if i == 0:
        # 那么随机抽取100支股票作为初始投资组合。
        portfolio = list(monthly_data["Stock Codes"].sample(n=100))
        # 取出我们的投资组合的对应数据，并按照收益率排序。（假如刚刚没有剔除NA数据，在这里NA会被排序在哪里？）
        monthly_performance = monthly_data[monthly_data["Stock Codes"].isin(portfolio)].sort_values(by="Monthly Return")
        # 并得到这个月表现最差的股票。
        worst_stock = monthly_performance["Stock Codes"].iloc[0]

    # 假如不是第一个月。
    else:
        # 剔除上个月表现最差的股票。（对for循环的理解：这里的worst_stock是在哪里定义的？）
        portfolio.remove(worst_stock)
        # 在新的一个月的数据中随机选取一支股票作为投资组合的新成员。
        new_stock = list(monthly_data["Stock Codes"].sample(n=1))[0]
        portfolio.append(new_stock) # 并把它添加到投资组合中。
    
    # 获取我们的投资组合的对应数据来计算投资表现。
    monthly_performance = monthly_data[monthly_data["Stock Codes"].isin(portfolio)].sort_values(by="Monthly Return")
    # 计算这个月我们的投资组合的收益率。
    monthly_return = monthly_performance["Monthly Return"].mean()
    # 把我们得到的这个月的收益率填写到最终报告的数据表的对应位置。
    report_dataframe.loc[time, "Monthly Return"] = monthly_return
    # 并得到这个月表现最差的股票，作为下一次循环（下一个月）的被剔除股票。
    worst_stock = monthly_performance["Stock Codes"].iloc[0]

# 获取参考基准的数据，此处以沪深300为例。
benchmark_data = pd.read_csv(path + "\\Data\\HS300.csv")
# 原始数据包含沪深300和上证综指，只要前者。
benchmark_data = benchmark_data[benchmark_data["Indexcd"] == 300]
# 只留下我们需要的列。
benchmark_data = benchmark_data[["Month", "Idxrtn"]]
benchmark_data.columns = ["Month", "Benchmark Return"] # 重命名列名
benchmark_data["Month"] = pd.to_datetime(benchmark_data["Month"], format='%Y-%m') # 同上转换日期格式
benchmark_data = benchmark_data[benchmark_data["Month"].isin(report_dataframe.index)] # 只要我们观察样本期内的数据
benchmark_data.set_index("Month", inplace=True) # 把日期设置为index，方便下一步的join操作

# 合并策略数据和基准数据。
report_dataframe = report_dataframe.join(benchmark_data)
# 计算年化收益率列。
report_dataframe["Annualized Return"] = (report_dataframe["Monthly Return"] + 1) ** 12
# 计算超额收益列。
report_dataframe["Excess Return"] = report_dataframe["Monthly Return"] - report_dataframe["Benchmark Return"]
# 计算净值。
report_dataframe["Equity"] = (report_dataframe["Monthly Return"] + 1).cumprod()
# 计算基准的净值。
report_dataframe["Benchmark Equity"] = (report_dataframe["Benchmark Return"] + 1).cumprod()
# 把我们得到的数据表保存到本地excel文件。
report_dataframe.to_excel(path + "\\Results\\report.xlsx")

# 计算平均月度收益率。
average_monthly_return = report_dataframe["Monthly Return"].mean()
# 返回平均月度收益率。
print("策略的平均月度收益率为：", round(average_monthly_return * 100, 2), "%；")
# 返回平均年化收益率。
print("策略的平均年化收益率为：", round(((average_monthly_return+1)**12-1) * 100, 2), "%；")
total_year = round(len(report_dataframe)/12, 1) # 总共有多少年
# 返回平均净值。
print("策略%s年的平均净值为：%s；" % (total_year, round(report_dataframe["Equity"].mean(), 2)))
# 返回复合年化收益率。
print("策略%s年的复合年化收益率为：%s" % (total_year, round((report_dataframe["Equity"][-1]**(1/total_year)-1) * 100, 2)), "%；")
# 返回夏普值。
print("策略的夏普值为：%s；" % round(((average_monthly_return+1)**12-1) / report_dataframe["Monthly Return"].std(), 2))

# 绘图。
plt.figure(figsize=(8, 5)) # 设置图片大小
plt.plot(report_dataframe.index, report_dataframe["Equity"], label="策略净值")            # 画策略净值图
plt.plot(report_dataframe.index, report_dataframe["Benchmark Equity"], label="HS300净值") # 画基准净值图
plt.legend() # 显示图例
plt.title("策略与HS300净值对比图") # 图表标题
plt.savefig(path + "\\Results\\equity_plot.png") # 保存本地为png文件
# 同上，绘制月度收益率图。
plt.figure(figsize=(8, 5))
plt.plot(report_dataframe.index, report_dataframe["Monthly Return"], label="策略月度收益率")
plt.plot(report_dataframe.index, report_dataframe["Benchmark Return"], label="HS300月度收益率")
plt.plot(report_dataframe.index, report_dataframe["Excess Return"], label="策略超额收益")
plt.legend()
plt.title("策略与HS300月度收益率对比图")
plt.savefig(path + "\\Results\\return_plot.png")