import re
class Stringcount:
    def stingmethod(self,string):
        #pattern="Hello"
        #result= re.search(pattern,string)
        #print(result.group())
        lst = list(string.split())
        dct={}
        for st in lst:
           if st not in dct:
               dct[st]=1
           else:
               dct[st]+=1
        print(dct)
if __name__ =="__main__":
    object=Stringcount()
    string=input()
    object.stingmethod(string)