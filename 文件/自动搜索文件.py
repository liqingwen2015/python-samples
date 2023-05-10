# This code is searching for all files in the current working directory and its subdirectories that
# have a filename containing the string "2021" and ending with ".xlsx". It then prints the full file
# path of each matching file. The `os` module is used to interact with the operating system and
# perform file system operations. The `os.walk()` function is used to recursively traverse the
# directory tree and return the paths of all files and directories within it.
import os

# 获取当前工作目录
path = r''

# 遍历当前工作目录下的所有文件
for dirPath, dirnames, filenames in os.walk(path):
    # 遍历文件
    for name in filenames:
        # 判断文件是否以2021开头，以.xlsx结尾
        if '2021' in name and '.xlsx' in name:
            # 获取文件路径
            file_path = os.path.join(dirPath, name)
            print(file_path)


