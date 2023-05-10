# This code is using the pandas library to read an Excel file and then split the data by class and
# save each class's data into a separate Excel file.
import pandas as pd

# 导入Excel模块
import pandas as pd

# 读取Excel文件
df = pd.read_excel(
    r"C:\Temp\43634快学Python_代码合集\第3章 学习Python，可以自动化处理数据\三年级总成绩.xlsx")

# 遍历班级
for i in df["班级"].unique():
    # 将班级按照空格分割，并将空格替换为.xlsx
    df[df["班级"] == i].to_excel(f"{i}.xlsx", index=False)