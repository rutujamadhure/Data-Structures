#There are 'N' petrol pumps in a circle.A car needs to travel all these petrol pumps in circular manner. Each petrol pump is an element pair of the list 'lis'.
#First element of the pair is amount of petrol available at the petrol pump and second element is the
#distance it has to travel to reach next petrol pump. Assume, for 1 litre of petrol car travels 1 unit of distance. Return the index of the first pair from where the truck can complete
#a circular tour.

#Consider 'T' test cases.Each Test case contains 2 lines. The first line will contain an integer N denoting the number of petrol pumps and in the next line are N space
#separated values petrol and distance denoting the amount of petrol every petrol pump has and the distance to next petrol pump respectively.
# Question by Amit Khandelwal,Harshit Sidhwa(GeeksforGeeks)

#Input:
#1
#4
#4 6 6 5 7 3 4 5
#Output:
#1

def tour(lis, n):
    new=[]
    for i in range(n):
        if lis[i][0]>=lis[i][1]:
            new.append(i)
    balance=0
    if len(new)==0:
        return -1
    else:    
        for x in new:
            balance=0
            flag=True
            for i in range(n):
                balance=balance+lis[(x+i)%n][0]
                balance=balance-lis[(x+i)%n][1]
                if balance<0:
                    flag=False
                    break
            
            if flag==True:
                return x
            
        return -1       


T = int(input())
for i in range(T):
    n = int(input())
    arr=list(map(int, input().strip().split()))
    lis=[]
    for i in range(1, 2*n, 2):
        lis.append([ arr[i-1], arr[i] ])
    #print n, arr
    print(tour(lis, n))

