# 基础篇 列表和元组

import numpy as np

if __name__ == "__main__":
    l = [1,2,"hello","world"]
    tup = ("jody",32)
    print(l)
    print(tup)

    l = [1,2,3,4]
    l[3] = 40
    print(l)
    tup = (1,2,3,4)
    # tup[3] = 40 tuple can not do this action
    print(tup)
    # add elements
    new_tup = tup + (5,)
    print(new_tup)
    l.append(5)
    print(l)

    # 片切操作
    l = [1,2,3,4]
    print(l[1:3])
    tup = (1,2,3,4)
    print(tup[1:3])

    # 嵌套
    l = [[1,2,3],[4,5]]
    tup = ((1,2,3),(4,5,6))
    print(l)
    print(tup)

    # 相互转换
    print(list((1,2,3)))
    print(tuple([1,2,3]))

    # 内置函数
    l = [3,2,3,7,8,1]
    print(l.count(3))
    print(l.index(7))
    l.reverse() # 反转
    print(l)
    l.sort() # 排序(ASC)
    print(l)

    tup = (3,2,3,7,8,1)
    print(tup.count(3))
    print(tup.index(7))
    print(list(reversed(tup)))
    print(sorted(tup))

    # 列表和元组的存储差异
    l = [1,2,3]
    tup = (1,2,3)
    print(l.__sizeof__())
    print(tup.__sizeof__())

    l = []
    print(l.__sizeof__())
    l.append(1)
    print(l.__sizeof__())
    l.append(2)
    print(l.__sizeof__())
    l.append(3)
    print(l.__sizeof__())
    l.append(4)
    print(l.__sizeof__())
    l.append(5)
    print(l.__sizeof__())