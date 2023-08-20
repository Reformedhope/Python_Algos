#Print two space-separated long integers denoting the respective minimum and maximum values 
#that can be calculated by summing exactly four of the five integers. 
#(The output can be greater than a 32 bit integer.)
#


def miniMaxSum(arr):
    
    
  min_holder = sorted(arr)
   
   
  max_holder = sorted(arr)
  max_holder.reverse()
  min_sum = 0
  max_sum = 0
   
   
   
  for i in range(4):
    element = min_holder[i]
    min_sum += element
    
    element2 = max_holder[i]
    max_sum += element2

    
    
    
  print (min_sum, max_sum)

    
   
   
      
     
    # Write your code here

if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)