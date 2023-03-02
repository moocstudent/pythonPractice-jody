

if __name__ == "__main__":
    name = 'aaa'
    city = "bbb"
    text = """ccc"""
    print(name, city, text)

    # 转义符
    s = "a\nb\tc"
    print(s)
    print(len(s))

    # 索引切片遍历
    name = "jody"
    print(name[0]) # 获取字符串第一个字符
    print(name[1:3]) # 截取字符串数组从下标几到几
    for char in name:
        print(char)

    # 改变字符串
    s = "hello"
    s = 'H' + s[1:]
    print(s)
    s = s.replace('H','h')
    print(s)

    # 字符串拼接，时间复杂度O(N)
    s = ''
    for n in range(0,100000):
        s += str(n)
    print(s)

    # join函数 时间复杂度O(N)
    l = []
    for n in range(0,100000):
        l.append(str(n))
    l = ' '.join(l)
    print(l)

    path = "hive://ads/training_table"
    namespace = path.split('//')[1].split('/')[0] # 字符串分段并获取某个组数据
    table = path.split('//')[1].split('/')[1]
    print(namespace,table)

    # strip函数
    s = " my name is jody "
    print(s.strip())

    # 字符串格式化函数
    print("我的名字叫{},年龄{}".format("jody",str(32)))
