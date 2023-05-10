# This code is renaming all files in a directory that contain the string "2020" in their name to have
# "2021" instead. It does this by using the `os` module to list all files in the directory, iterating
# through each file name, replacing "2020" with "2021" in the name, and then using `os.rename` to
# change the file name.
import os

# 获取当前文件夹的路径
path = r""
# 获取当前文件夹下的所有文件
excel_list = os.listdir(os.path.join(path))

# 遍历文件列表
for i in excel_list:
    # 将2020替换为2021
    newname = i.replace("2020", "2021")
    # 获取当前文件夹下的文件路径
    oldpath = os.path.join(path, i)
    # 获取新文件夹的路径
    newpath = os.path.join(path, newname)
    # 重命名文件
    os.rename(oldpath, newpath)