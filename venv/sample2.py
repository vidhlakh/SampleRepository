
class Stringcount:
    def stingmethod(self,lst,order):
       print(lst,order)
       newlist=[]
       temp=[]
       for i,l in enumerate(lst):
           if i<order:
               temp.append(l)
           elif i==order:
               temp.reverse()
               newlist.append(temp)
               order+=3
           temp.clear()
           print(newlist,"temp:",temp)
       print(newlist,temp)
if __name__ =="__main__":
    object=Stringcount()
    lst=list(map(int,input().split()))
    order = int(input())
    object.stingmethod(lst,order)