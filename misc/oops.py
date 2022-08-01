class Animal:
    def dog(self):
        print('dog barks')


class B(Animal):
    def cat(self):
        print('cat comes in Animals')


class c( B):
    def inheritance(self):
        print("Pass")


c = c()
c.cat()
c.dog()
c.inheritance()
