# 条件与循环

if __name__ == "__main__":
    # 条件语句
    x = -3
    if x < 0:
        y = -x
    else:
        y = x
    print(y)

    # elif语句
    id = 2
    if id == 0:
        print("red")
    elif id == 1:
        print("yellow")
    else:
        print("green")

    # 循环
    l = [1,2,3,4]
    for item in l:
        print(item)

    # 字典循环
    d = {
        "name":"jody",
        "dob":"2000-01-01",
        "gender":"male"
    }
    for k in d:
        print(k)

    for v in d.values():
        print(v)

    for k,v in d.items():
        print("keys:{},values:{}".format(k,v))

    l = [1,2,3,4,5,6,7]
    for index in range(0,len(l)):
        if index < 5:
            print(l[index])

    # 用索引和元素来循环
    l = [1,2,3,4,5,6,7]
    for index,item in enumerate(l):
        if index < 5:
            print(item)

    # 用索引和元素来循环
    l = [1,2,3,4,5,6,7]
    for index,item in enumerate(l):
        if index < 5:
            print(item)

    # break和continue
    name_price = {"一":100,"二":10,"三":10000}
    name_color = {"一":"红","二":"蓝","三":"红"}

    # 不用continue
    for name,price in name_price.items():
        if price < 1000:
            if name in name_color:
                for color in name_color[name]:
                    if color != "红":
                        print("name:{},color:{}".format(name,color))
                    else:
                        print("name:{},color:{}".format(name,None))

    # 用continue name,price对应取值键值对
    for name,price in name_price.items():
        if price >= 1000:
            continue
        if name not in name_color:
            print("name:{},color:{}".format(name,None))
            continue
        for color in name_color[name]:
            if color == "red":
                continue
            print("name:{},color:{}".format(name,color))

    # while循环
    l = [1,2,3,4]
    index = 0
    while index < len(l):
        print(l[index])
        index += 1

    # 测试for和while的效率
    import time
    start_for = time.perf_counter()
    for i in range(0,100_0000):
        pass
    end_for = time.perf_counter()
    print("for循环{}秒".format(end_for-start_for))
    start_while = time.perf_counter()
    i = 0
    while i < 100_0000:
        i += 1
    end_while = time.perf_counter()
    print("while循环{}秒".format(end_while-start_while))

    # 思考题
    attributes = ['name','dob','gender']
    values = [
        ['jody','2000-01-01','male'],
        ['lucy','1999-01-01','female'],
        ['andy','1998-02-01','male'],
    ]

    #多行循环语句
    result = []
    for index in range(0,len(values)):
        temp = {}
        for j in range(3):
            # 组合成键值对的形式
            temp[attributes[j]]=values[index][j]
        result.append(temp)
    print(result)
    # 一行条件循环语句 哈哈
    result = [dict(zip(attributes,v)) for v in values]
    print(result)