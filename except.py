# 异常处理 如何提高程序的稳定性

# 自定义异常类
class MyInputError(Exception):
    def __init__(self,value):
        self.value = value

    def __str__(self):
        # repr 返回规范的对象字符串表示形式
        return("{} is invalid input".format(repr(self.value)))

if __name__ == "__main__":
    # try except语句
    try:
        s = input("输入数字，以,分隔:")
        num1 = int(s.split(",")[0].strip())
        num2 = int(s.split(",")[1].strip())

    # 是否是发生了这个异常？是的话执行下面一句
    except ValueError as err:
        print("值错误异常:{}".format(err))
    except Exception as err:
        print("异常:{}".format(err))

    print("继续")

    #自定义异常
    try:
        raise MyInputError(1)
    except MyInputError as err:
        print("error:{}".format(err))
    print("继续2")
