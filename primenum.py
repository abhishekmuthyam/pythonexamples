class PrimeNumber:
    
    def primeFun(x,y):

        for curNum in range(x,y):
            if curNum > 1:
                for i in range(2,curNum):
                    if(curNum % i) == 0 :
                        break
                else:
                    print(curNum)
  

PrimeNumber.primeFun(1,999)
