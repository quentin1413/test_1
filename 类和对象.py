""" class Parrot:
    #类属性
    species="鸟"
    #示例属性
    def __init__(self,name,age):
        self.name=name
        self.age=age
        
#示例化Parrot类
blu=Parrot("麻雀",10)
woo=Parrot("鹦鹉",15)

#访问类属性
print("麻雀是{}".format(blu.__class__.species))
print("鹦鹉也是{}".format(woo.__class__.species))

#访问示例属性
print("{}有{}岁".format(blu.name,blu.age))
print("{}有{}岁".format(woo.name,woo.age)) """

""" class Parrot:
    #静电场
    def __init__(self,name,age):
        self.name=name
        self.age=age
    #示例方法
    def sing(self,song):
        return "{} sings {}".format(self.name,song)
    def dance(self):
        return "{} is now dancing".format(self.name)
#示例化对象
blu=Parrot("Blu",10)
#调用我们的示例方法
print(blu.sing("Happy"))
print(blu.dance()) """

#在Python中使用继承
#基类
""" class Bird:
    def __init__(self):
        print("鸟准备好了")
    def whoisThis(self):
        print("鸟")
    def swim(self):
        print("游得更快")
        
#子类
class Penguin(Bird):
    def __init__(self):
        #call super() functhion
        super().__init__()
        print("企鹅准备好了")
    def whoisThis(self):
        print("企鹅")
    def run(self):
        print("跑得更快")
        
peggy=Penguin()
peggy.whoisThis()
peggy.swim()
peggy.run() """


#采用OOP,使用__来表示私有属性，防止数据直接修改
#Python中的数据封装
""" class Computer:
    def __init__(self):
        self.__maxprice=900
    def sell(self):
        print("售价：{}".format(self.__maxprice))
    def setMaxPrice(self,price):
        self.__maxprice=price
    
c=Computer()
c.sell()

#改变价格
c.__maxprice=1000#无法更改，因为Python将__maxprice视为私有属性
c.sell()

#使用setter函数
c.setMaxPrice(1000)#要改变必须使用内部定义的setter函数
c.sell()  """


#多态性(在OOP中)，可以将公共接口用于多种形式(数据类型)
#假设我们需要给一个形状上色，有多个形状选项（矩形，正方形，圆形）。但是，我们可以使用相同的方法为任何形状着色。这个概念称为多态。
#在Python中使用多态
""" class Parrot:
    def fly(self):
        print("鹦鹉会飞")
    def swim(self):
        print("鹦鹉不会游泳")
        
class Penguin:
    def fly(self):
        print("企鹅不会飞")
    def swim(self):
        print("企鹅会游泳")
        
#通用接口
def flying_test(bird):
    bird.fly()
    
#示例化对话
blu=Parrot()
peggy=Penguin()

#传递对象
flying_test(blu)
flying_test(peggy) """


#构造复数函数
class ComplexNumber:
    def __init__(self,r=0,i=0):
        self.real=r
        self.imag=i
        
    def getData(self):
        print("{0}+{1}".format(self.real,self.imag))
        
#创建一个新的ComplexNumber对象
c1=ComplexNumber(2,3)

#调用getData()函数
#输出：2+3j
c1.getData()

#创建另一个ComplexNumber对象
#并创建一个新的属性"attr"
c2=ComplexNumber(5)
c2.attr=10

#输出：(5,0,10)
print((c2.real,c2.imag,c2.attr))

#但c1对象没有属性"attr"
#AttributeError:'ComplexNumber'对象没有属性'attr'


