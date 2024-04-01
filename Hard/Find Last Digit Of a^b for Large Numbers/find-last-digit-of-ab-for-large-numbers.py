#User function Template for python3

class Solution:
    def getLastDigit(self, a, b):
        # code here 
        a=int(a)
        b=int(b)
        if a==0 and b==0:
            return 1
        if b==0:
            return 1
        if a==0:
            return 0
            
        if b%4 ==0:
            res= 4
        else:
            res = b%4
            
        num = pow(a,res)
        return num%10
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        a,b=map(str,input().split())
        
        ob = Solution()
        print(ob.getLastDigit(a,b))
# } Driver Code Ends