## add the median Util


def findMedian(arr, n):
    global a
    global b
    a = -1
    b = -1
#if n is odd
if (n % 2 ==1):
    MedianUtil(0, n - 1 ,n // 2, a , b); 
    ans = b;

    #if n is even
else:
    MedianUtil(arr, 0, n - 1, n // 2, a, b)
    ans = (a + b)// 2

    print(ans)





arr = [ 12, 3, 5, 7, 4, 19, 26 ];
n = len(arr);
findMedian(arr, n);


## This is not correct re do it.