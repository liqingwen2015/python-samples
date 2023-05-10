# This code is importing the `glob` module, which provides a way to find all the pathnames matching a
# specified pattern according to the rules used by the Unix shell.
import glob

# 定义一个空的DataFrame
df_all = pd.DataFrame()

# 遍历每一个文件夹中的文件
for i in glob.glob(r"三年*班.xlsx", recursive=True):
    # 读取文件
    df = pd.read_excel(i)
    # 将读取的文件合并到DataFrame中
    df_all = df_all.append(df)

# 将DataFrame写入文件
df_all.to_excel("三年级总成绩单.xlsx", index=False)