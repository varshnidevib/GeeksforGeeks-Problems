#User function Template for python3


class Solution:
    def evenlyDivides (self, N):
        temp = N
        count = 0
        while(temp!=0):
            d = temp%10
            temp = temp//10
            if (d>0 and N%d==0):
                count+=1
        return count

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N = int(input())
       

        ob = Solution()
        print(ob.evenlyDivides(N))
# } Driver Code Ends