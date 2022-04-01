""" 
https://www.interviewbit.com/blog/maximum-subarray-sum/#:~:text=Kadane's%20Algorithm%20is%20an%20iterative,ending%20at%20the%20previous%20position.

 The key here is the max function. 
 
 The max() function returns the largest item in an iterable. It can also be used to find the largest item between two or more parameters.
 
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

A subarray is a contiguous part of an array.
 
Kaden's Algorithm O(N) time and space. 

The key here also is that we use a current tracker, and a max tracker. 


Kadane’s Algorithm is an iterative dynamic programming algorithm. 
It calculates the maximum sum subarray ending at a particular position by using the maximum sum subarray ending at the previous position. 
Follow the below steps to solve the problem.

1. Define two-variable currSum which stores maximum sum ending here and maxSum which stores maximum sum so far.

2. Initialize currSum with 0 and maxSum with INT_MIN.

3. Now, iterate over the array and add the value of the current element to currSum and check
    4. If currSum is greater than maxSum, update maxSum equals to currSum.
    5. If currSum is less than zero, make currSum equal to zero.
    
6. Finally, print the value of maxSum.

The key idea, is that, while you loop through, you continually add to curSum, whenever curSum is greater than maxSum, you save that

currSum will change through out the array, at the positions where it peaks and becomes greater, that's when you update/save the maxSum. 

 """


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        n = len(nums)
        
        #two trackers, maxSum, and currSum
        
        maxSum = -1e8
        currSum = 0
        
        for i in range(0, n):
            
            currSum = currSum + nums[i]
            
            if (currSum > maxSum):
                maxSum = currSum
                
            if (currSum < 0):
                currSum = 0
                
        return maxSum

