# This code is importing the `glob` module in Python, which provides a way to search for files and
# directories in a specified path. The `glob.glob()` function is then used to search for files and
# directories that match a specified pattern (in this case, an empty string). The `recursive=True`
# argument tells the function to search for files and directories recursively in all subdirectories.
# Finally, the code prints out the names of all the files and directories that match the specified
# pattern. However, since the pattern is an empty string, the code will not find any files or
# directories and will not print anything.
import glob

# 遍历当前目录下的所有文件
for i in glob.glob(
        r'',
        recursive=True):
    # 打印文件名
    print(i)
