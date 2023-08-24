// find the median

 findMedian(arr,n)
{
    let ans = 0
    GFG.a = -1;
    GFG.b = -1;
    //if n is odd
    if (n % 2 == 1)
    {
        GFG.MedianUtil(arr, 0, -1, parseInt (n/2));
        ans = GFG.b
    }
    else
    {
        //if it is even
        GFG.MedianUtil(arr,0,n-1,parseInt(n/2));
        ans = parseInt((GFG.a + GFG.b) / 2 );
    }
}







    main(args)
    {
        var arr = [12, 3, 5, 7, 4, 19, 26];
        var n = arr.length;
        GFG.findMedian(arr, n);
    }

