#User function Template for python3

class Solution:
    #Complete this function
    def power(self,N,R):
        MOD = 10**9 + 7
        if (N==0):
            return 0
        if (R==0):
            return 1
        if (R==1):
            return N
        ans=0
        if(R%2==0):
            ans =self.power(N,R//2)
            return (ans%MOD *ans%MOD)%MOD
        
        else:
            ans = self.power(N,(R-1)//2)
            return (ans%MOD *ans%MOD * N%MOD)%MOD
       

#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math

def main():
    
    T=int(input())
    
    while(T>0):
        
        N=input()
        R=N[::-1]
        
        ob=Solution();
        ans=ob.power(int(N),int(R))
        print(ans)
        
        T-=1

if __name__=="__main__":
    main()
# } Driver Code Ends