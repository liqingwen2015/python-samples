# This code is reading an Excel file, grouping the data by unique values in the "班级" column, and then
# creating separate Excel sheets for each group in a new Excel file. The new Excel file has one sheet
# with the overall data and additional sheets for each group. The pandas library is used for reading
# and writing Excel files.
import pandas as pd

df = pd.read_excel('.xlsx')

# 对每一个班级进行分组
for i in df["班级"].unique():
	# 读取三年级总成绩.xlsx文件
	df = pd.read_excel('三年级总成绩.xlsx')
	# 创建一个新的Excel文件，文件名为三年级总成绩.xlsx
	writer = pd.ExcelWriter('三年级总成绩.xlsx')
	# 将总成绩写入新的Excel文件
	df.to_excel(writer, sheet_name='总成绩', index=False)

# 对每一个班级进行分组
for i in df["班级"].unique():
    # 将每一个班级的数据写入新的Excel文件
    df[df["班级"] == i].to_excel(writer, index=False, sheet_name=i)

# 保存新的Excel文件
writer.save()