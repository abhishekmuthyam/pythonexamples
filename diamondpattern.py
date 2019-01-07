class DiamondPattern:
    def diaFun(num):
        j=num
        for i in range(1,num+1,2):
            print(' '*j+'*'*i)
            j=j-1

        k=int(num/2+1.5)
        for i in range(num-2,0,-2):
            print(' '*k+'*'*i)
            k=k+1


DiamondPattern.diaFun(9)
