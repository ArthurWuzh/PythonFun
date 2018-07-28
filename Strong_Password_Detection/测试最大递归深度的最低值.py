import sys

for i in range(1,20):
    try:
        sys.setrecursionlimit(i)
    except RecursionError as e:
        print(e)
        continue
    else:
        print('python3递归最小深度:',i)
        break




