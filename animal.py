# 定义 Animal 类
# add print by joe
# add print by scott
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        raise NotImplementedError("子类必须实现这个方法")

# 定义 Cat 子类
class Cat(Animal):
    def speak(self):
        return f"{self.name} says Meow!"

# 定义 Dog 子类
class Dog(Animal):
    def speak(self):
        return f"{self.name} says Woof!"

# 测试代码
if __name__ == "__main__":
    # 创建 Cat 实例
    my_cat = Cat("Tom")
    # 打印输出
    print(my_cat.speak())
    print("good")
