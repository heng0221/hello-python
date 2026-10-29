import sys

print("=" * 30)
print("  Python 跑起来了！")
print("=" * 30)
print("版本:", sys.version.split()[0])

name = input("你叫什么名字？ ")
print(f"你好, {name}! 欢迎开始学 Python 🎉")

print("\n算个小例子:")
for i in range(1, 6):
    print(f"  {i} 的平方 = {i ** 2}")
