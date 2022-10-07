class list_ADT():
    def _init_(self):
        l=l
        self.l=[]
    def insert_at_end(self,a,l):
        l=l
        self.l.append(a)
    def insert_at_begininning(self,a,l):
        l=l
        self.l.insert(0,a)
    def insert_at_middle(self,ind,a,l):
        l=l
        self.l.insert(ind,a)
    def remove(self,b,l):
        l=l
        self.l.remove(b,l)
    def display(self,l):
        l=l
        return (self.l)
print("Implementation of List using Python Class")
l=[1,2,3]
obj=list_ADT()
while(1):
    print("1.INSERT AT BEGINNING")
    print("2.INSERT AT MIDDLE")
    print("3.INSERT AT END")
    print("4.DELETE AN ELEMENT")
    print("5.DISPLAY THE LIST")
    print("6.Exit")
    choice=int(input("Enter choice: "))
    if choice==1:
        n=int(input("Enter element to insert: "))
        obj.insert_at_begininning(n,l)
    
    elif choice==2:
        n=int(input("Enter element to insert: "))
        pos=int(input("Enter at which index element to insert:"))
        obj.insert_at_middle(pos,n,l)
    elif choice==3:
        n=int(input("Enter element to append: "))
        obj.insert_at_end(n,l)
    elif choice==4:
        n=int(input("Enter element to remove: "))
        obj.remove(n,l)
    elif choice==5:
        print("List is ",obj.display(l))
    else:
        print("PROGRAM EXIT")
        break
