# This code is moving all files in a specified directory to subdirectories based on their file
# extension. It uses the `os` and `shutil` modules to manipulate files and directories. The
# `os.listdir()` function is used to get a list of all files in the specified directory, and then each
# file is checked to see if it is a file (not a directory) using `os.path.isfile()`. If it is a file,
# a new subdirectory is created based on the file extension using `os.makedirs()`, and then the file
# is moved to that subdirectory using `shutil.move()`.
import os
import shutil

# 定义函数 move_files，用于将文件从指定路径移动到指定路径
# 参数：path：指定的路径
# 返回值：无

path = r""

# 遍历指定路径下的文件
for file_name in os.listdir(path):
    # 获取文件路径
    file_path = os.path.join(path, file_name)

    # 判断文件是否是文件夹
    if os.path.isfile(file_path):
        # 获取文件名
        folder_name = file_name.split(".")[-1]
        # 获取文件夹路径
        folder_path = os.path.join(path, folder_name)

        # 判断文件夹路径是否存在
        if not os.path.exists(folder_path):
            # 如果不存在，则创建文件夹路径
            os.makedirs(folder_path)

        # 将文件从指定路径移动到指定路径
        shutil.move(file_path, folder_path)
