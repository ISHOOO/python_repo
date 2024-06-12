class node:
    def __init__(self,value):
        self.data=value
        self.next=None
a=node(103)
b=node(86)
c=node(75)
a.next=id(b)
b.next=id(c)
c.next=id(a)
print(a.next,b.next,c.next,sep=" ,")