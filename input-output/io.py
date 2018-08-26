# I/O

# 读取文件
f = None
try:
    f = open("D:/test.txt", 'r')
finally:
    if f is not None:
        f.close()

# 读取并自动关闭
with open("D:/test.txt", 'r') as file:
    print(file.read())

# 按行读取文件

with open("D:/test.txt", 'r') as file:
    for line in file.readlines():
        print("this is: ", line.strip())

# 写入文件

origin = None
target = None

try:
    origin = open("D:/test.txt", 'r')
    target = open("D:/test2.txt", 'w')

    for line in origin.readlines():
        target.write(line)

finally:
    if origin is not None:
        origin.close()
    if target is not None:
        target.close()

# 写入字节文件

origin = None
target = None

try:
    origin = open("D:/head_img.jpg", 'rb')
    target = open("D:/head_img2.jpg", 'wb')

    for b in origin.readlines():
        target.write(b)

finally:
    if origin is not None:
        origin.close()
    if target is not None:
        target.close()