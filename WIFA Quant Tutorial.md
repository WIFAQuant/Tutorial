# WIFA Quant Tutorial

> 你可以使用任何你想要的软件来实现以下任务（Excel、MATLAB、R、Python等）。但我推荐学习python，也仅给出python的对应提示。
>
> 全文名词解释皆用英文，建议掌握英文，因为计算机术语的中文翻译很混乱。

# 1. 准备：认识你的工作区

进入数据分析的准备工作。

## 1.1 Text Editor（文本编辑器）

一旦面对相对复杂的数据分析任务，text editor就是一个必不可少的工具了，无论你是使用excel的VBA、R的R Script......即使是用手计算🙂，你也需要一个“草稿纸”来记录自己的计算思路和过程对吗？——在电脑里，这个草稿纸就是text editor。

任何可以显示纯文本、缩进、换行的东西都可以算作text editor，最简单的就是Windows自带的“记事本” (Notepad)。

但不要小看“纯文本”、“缩进”、“换行”这些看似理所当然的细节，实际上不正确的使用导致的错误可以让代码完全无法运行。

- “纯文本”：指UTF-8编码编译的Unicode字符，从一些应用/网站直接复制的不一定符合，于是粘贴可能出现乱码；
- “缩进”：就是键盘上的“Tab”键，实际上是若干个空格，在python语境下指四个空格，在其他语言下是不同数量的空格，空格数量不对也会导致编译错误；
- “换行”：换行只是展示给人看的视觉效果，实际上对于电脑是用"\r", "\n"等字符表示的。在Windows下指CRLF式换行，在Mac/Unix/Linux下指LF式换行

如果你们不想在日后遇到上述这些听着就头疼的问题，请使用一个专业的文本编辑器，而不是在随便一个地方打字复制粘贴过去运行。

> 但实际上多了解这些电脑底层知识对你们日后更深入的学习有一些帮助。

主流的文本编辑器：

- Windows自带的记事本 (Notepad)
- 最轻量的[Notepad++](https://notepad-plus-plus.org/)
- 颜值轻量功能平衡的[Sublime Text](https://www.sublimetext.com/)
- Github出品，高颜值开源的[atom](https://atom.io/)
- 微软出品的[VScode](https://code.visualstudio.com/)

文本编辑器的基础功能：

- 打字、换行、缩进
- 自动补全代码
- 语法高亮

文本编辑器可以通过安装扩展实现一些其它功能，例如支持其它语言。

> 实际上还有Vim，Emacs等“上古编辑器”，网上关于哪个Text editor最好的争论亘古不衰，希望大家不要卷入🙂，能把活儿干好的就是最好的。

## 1.2 Terminal（终端）

在Windows下叫Command Prompt（或Power Shell），在MacOS下叫Terminal，就是看上去就很极客的那个全命令行操作界面。

它实际上就是你的电脑系统的一个shell（一个壳，让你可以通过它操作电脑），和你平时用鼠标键盘（GUI）是一样的，在某些场景甚至更高效，对terminal有一定了解有助于你优化你的workflow。

> 未来假如你接触到多线程优化、并行计算等，你会需要更多这方面的知识。

基础操作例如ls (listing) 显示文件列表，cd (change directory) 切换文件夹等建议掌握，因为：

- 当你想要把你的数据分析和电脑系统本身整合起来时，需要在程序脚本中包含这些命令；
- 许多模块的安装是只能用命令行界面的，所以这方面的知识在你遇到问题时很有用

现在就打开你的terminal认识一下它吧😀。

## 1.3 Script（脚本）

你在text editor里面写的东西，可以拿来运行的就叫script，也就是前文比喻的“记录运算过程的草稿纸”。

## 1.4 Interactive Environment（交互式环境）

在terminal里输入python、R等就会带你进入该语言的interactive environment，即输入一次命令，回车，就会返回一次结果。

interactive environment是程序语言最基础的操作界面，适合简单快速的操作。

>  其中最推荐掌握的是ipython。其中的自动补全和魔法命令使得它非常方便。

## 1.5 Module/Library/Package（包）

每个语言的叫法不同，但都可以理解为“安装一个功能包”，安装后你就可以在该语言的交互环境内调用（import/install）这个包提供的功能。通俗的说，许多功能别人已经帮我们写好了，直接运行别人写的函数可以为我们省很多事儿。

> 在python中主要用pip install安装包。

## 1.6 IDE（Integrated Develop Environment，集成式开发环境）

上述所有东西的综合体，外加一大堆其它功能（变量观察窗、绘图区、错误日志等）。你可以理解为编程的“一站式学生服务中心”，在一个地方解决所有问题。

我不建议新手入门就直接使用IDE，因为这会让你忽视我上面介绍的底层知识，而当你遇到问题的时候，只有底层知识/客服可以救你。我建议的学习路径是“挨个儿了解我上面介绍的→能够用上面介绍的方式进行基础操作→使用IDE熟练操作→回到text editor+Interactive Environment或其他方式进行高效率的开发迭代”。

IDE 在大型工程有其存在意义，但对于我们这种数据分析、金融分析来说，最大需求是“快速迭代、频繁修改”，故IDE并非必须。

但仍然建议你主要学习阶段在IDE中度过，一是提高效率，二是熟悉workflow。

主流的IDE：

- [R Studio](https://www.rstudio.com/)，R最好用的IDE

- [Pycharm](https://www.jetbrains.com/pycharm/)，Jet Brain出品必属精品，对Jupyter、Git、数据分析的支持非常完美

- [Visual Studio](https://visualstudio.microsoft.com/)，微软出品，很老牌了，对所有语言的支持都很不错

> 其中Visual Studio安装自带的CPP开发工具是许多python包的依赖项。

## 1.7 Jupyter Notebook

数据分析特有的“代码-图片-文字介绍”模式使得传统的“代码、图片与文档分离”不太适合，所以有这个专门为数据分析而设计的项目。

前身是你们会经常用到的ipython笔记本。

支持多数数据分析语言，例如Python，Ruby，Julia。可以在同一个页面展示markdown文档、Latex数学公式（这个也希望你们能掌握）、代码和相应图片。

我们[上一次课题的部分报告](https://nbviewer.jupyter.org/github/WIFAQuant/HS300/blob/master/HS300.ipynb)就是用jupyter notebook完成介绍的。

若是你日后经常接触网上的量化平台，你会发现jupyter notebook是一个很常用的研究工具，在学术界也是这样。

> 假如你这次作业使用python完成，希望最后的形式是一个.ipynb的Jupyter notebook文件。

# 2. 关于不同的语言

各种语言各有优劣势（否则何必存在），建议以下语言全部都要掌握，至少了解个大概。

不必惧怕学习语言，不用把数十年学英语还没学好的恐惧代入编程语言，实际上掌握一门之后融会贯通另一门的时间往往不超过一星期。倘若有魄力精通一门底层语言，基本上任意一种新语言你都不必惧怕。

也不要以为你现在掌握一门语言就能一招鲜吃遍天了，永远有新的语言出现代替旧的，时刻要思考自己为何使用这门语言，在什么时候换别的工具会带来更大的收益，不断地革新自己才能保持竞争力。

请**务必**掌握：

- 查找各个语言/模块/接口的**官方文档**来解决自己遇到的问题；
- 用**英文**搜索自己的问题；
- 熟练使用[StackOverflow](https://stackoverflow.com/)和[CSDN](https://www.csdn.net/)这两个论坛解决自己的问题；

## 2.1 Excel （VBA）：

无法处理太大的数据，会卡（若你电脑神仙配置当我没说）。对各种扩展包的支持也很差，仅限数据处理。

但作为快速分析数据的观察、作图工具堪称神器。

建议必须掌握：

- 基础运算操作：SUM, AVERAGE, DATE, MIN, MAX, STDEV, VAR等

- 基础作图操作：散点图、折线图、柱状图、Combo（两个Y轴）等，会对图表元素进行操作（图例、坐标轴交叉点、坐标轴刻度与单位、标注等）

  >  知道展示什么应该用什么统计图是很重要的基本功。
  >
  > 对图表的颜值追求会大大增加你的报告易读性。😀

- 基础函数操作：IF, VLOOKUP, MATCH, INDEX等

- 特殊操作：数据透视表，制作表格、筛选与排序、去除重复值、快速分析、从网上获取数据等

  > VBA语言的编写不要求掌握，但我很推荐大家去学习。

推荐教材：网上自己找教程/报个选修课

## 2.2 R

专为数理统计设计的语言，在统计方面非常好用。

建议必须掌握：

- R Studio使用方法

- base或ggplot绘图

- 基础函数、for循环编写

- 至少熟练一种数据操作包（dplyr/tidyverse/data.frame），能进行基础数据操作

- 统计回归（lm等）

推荐教材：[R4DS](https://r4ds.had.co.nz/)

## 2.3 Python

胶水语言，啥都不是最好但啥都能做，在量化领域应用最广泛的语言（几乎所有的量化平台、几乎所有的金融数据接口、几乎所有的新兴研究领域首选），也因为其在人工智能、爬虫、性能优化、与其他语言整合的优势、极其丰富的包而在近几年比较火。

>  我希望组里有志做量化/数据分析的都熟练掌握这门语言，其他语言的重要性相比没那么重要。目前我们组的所有工作都是用python完成的。

建议必须掌握：

- 基础python操作：list，tuple，dict，函数编写，slice

- math模块的主要数学计算函数

- numpy模块：矩阵、数列的基础操作，随机数、随机分布的基础操作，numpy不同数据类型的理解(np.int64, np.nan等)

  > numpy对你将来更深入的学习pandas包和未来进行性能优化有很大帮助。

- pandas模块：精通dataframe的操作（这可能是你数据分析中最常面对的家伙），数据读写(pd.read_csv, pd.read_excel等)，pandas中的主要数据类型(pd.Series, pd.MultiIndex, pd.datetime等)

- scipy模块：数理统计，相当于取代R的部分功能

- matplotlib模块：绘图，建议掌握

  > 编程绘图实际上有些复杂，入门亦可先跳过绘图，输出数据到excel后用excel绘图

> 建议阅读PEP8语法规范，规范的语法排版可以大大减少别人和你自己读你的代码时的困难。

推荐教材：[廖雪峰的python教程](https://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000)，[Learn Python the Hard Way](https://learnpythonthehardway.org/)

## 2.4 Stata，MATLAB，Eviews等

这一类老统计软件使用十分友好，功能亦十分强大，适合处理的任务是那些“对excel来说太复杂，对R来说太简单”。

> 全部都要求至少用过，其中MATLAB值得花功夫去学，依然很有生命力，功能之强大可以让你不用R。

推荐教材：计量经济学课程实验课本。

## 2.5 数据库

SQL要求掌握基础语句（SELECT FROM）。

> 学有余力的话MongoDB，HDF5，Hadoop等也推荐了解，对使用KDB，Spark等高端工具有帮助。

建议教材：网上自己找教程/报个选修课。

## 2.5 典型workflow

1. 从网上/API/本地/爬虫获取数据，用excel或python/R浏览数据长啥样；
2. 用excel或python/R快速分析，对数据有个大概的印象和了解；
3. 使用excel或python/R进行简单的数据操作、清洗；
4. 使用python/R进行复杂的数据分析（此时excel多半已无法胜任）；
5. 使用excel或python/R生成图表和结果；
6. 使用word/markdown/jupyter notebook/PPT撰写最终报告；

> 这也是为何推荐python的原因之一，它能覆盖上述最多的步骤。

# 3. 任务一

布置一个最简单的任务给大一大二同学练手入门，

要求：

- DDL下周（2019年3月24日零点，由于不确定对你们来说的难度，若难度太大可推迟）
- 完成后发到群里相互交流（我会检查并告诉你是否有优化空间）
- 每一行代码都写注释
- 可以交代码+报告，也可以交jupyter notebook

## 3.1 获取数据

从以下几个数据源获取**全部A股和沪深300**的2009-2018的月度收益率数据（按照优先度排序，倘若你没有该数据源权限才考虑下一个）：

- [WindPy API](http://www.dajiangzhang.com/document)（关于WindPy，也要求掌握基本语法）
- [国泰安数据库](www.gtarsc.com/Home
  )
- [tushare接口](http://tushare.org/)
- 找学长学姐要数据

你可能会用到的命令：

```python
import WindPy as w
from WindPy import *
w.start()
w.isconnected()
import pandas as pd
pd.read_csv(
	path=file_path, 
    index_col=[0]
)
with open(file_path, 'w', encode="utf-8") as f:
    pd.read_csv(f)
    f.close()
```

> 无论你是否用到以上命令，都希望你弄明白这些代码的含义。

## 3.2 编写交易策略

定义一个函数，里面包含你的交易策略。

作为第一次作业，我们的交易策略很简单：

- 第一个月的第一天随机选择A股的100支股票，全部买入；

- 之后的每一个月卖出上一个月的投资组合表现最差（也就是跌得最惨）的那一支股票，再随机挑选一支股票进入我的投资组合，其它的继续保留；

  > 也就是说，投资组合始终有100支股票。
  >
  > 可选任务：这个挑选方法可能会选到若干个月前曾经抛弃的股票，你可以想一个办法避免选到曾经选过的股票。

- 假设你有无限的初始资金，并每个月按照这样的策略调仓一次

- 计算这样的策略每个月的收益率，并换算为年化收益率

- 计算按照每个月的收益率得到的净值变化

- 最后整合成一个这样的数据表：

  |         | Monthly Return | Annualized Return | Equity |
  | ------- | -------------- | ----------------- | ------ |
  | 2009-01 |                |                   |        |
  | ...     |                |                   |        |
  | 2018-12 |                |                   |        |

  > 可选任务：按照“双向千分之二”收取手续费减去交易成本。

- 计算这样一个投资策略的：

  - 平均月度收益率
  - 平均年化收益率
  - 平均净值
  - CAGR (Compound Annualized Growth Rate)
  - Sharpe Ratio

  > 可选任务：计算Max Drawdown和Tracking Error。

你可能会用到的命令：

```python
import numpy as np
np.random.randint(
	low=0, 
    high=len(data), 
    size=(100)
)
list(range(len(data)))
import pandas as pd
pd.DataFrame(data, index, columns)
def my_function(parameters):
    return result
pd.to_datetime(date, format="%Y-%m")
data[(data.index > start) & (data.index < end)]
data["Column"].cumsum()
data["Column"].cumprod()
data["Column"].std()
data.dropna(inplace=True)
```

## 3.3 绘图

绘制两幅图：

- 策略和沪深300的月度收益率折线图，包含图例、标题、各轴标题；
- 策略和沪深300的净值折线图，包含元素同上

## 3.4 报告

整理成报告，讲述你的思维，你采取的做法，你的发现，你对这个策略的想法。

包含：

- 你的代码，其中尽可能在每一行都写上注释；
- 必要的文字描述
- 那两张图
- 你对这个策略的想法，做的过程中有什么发现
- （可选：任务过程中你遇到的最大的困难）

标准答案会在大家都交上来之后发给你们。

> Have Fun! :smiley: