# difference between variable inside and outside the class
class DemoClass:
    a=10
    b=20
    def myfunction(self):
        self.c=self.a*self.b
        print(self.c)

    def myfunction1(self,a,b):
        print(a*b)


obj=DemoClass()
obj.myfunction()
obj.myfunction1(100,200)