import os

cwd = os.getcwd()
print(cwd) # 获取当前工作目录路径
p = os.path.join(cwd, os.path.dirname(__file__), '../out')
print(p)

print(os.listdir(p))