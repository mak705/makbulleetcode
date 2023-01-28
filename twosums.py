Link https://leetcode.com/problems/two-sum/



The Solution is provided in python

Question 

Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

 

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]
 

Constraints:

2 <= nums.length <= 104
-109 <= nums[i] <= 109
-109 <= target <= 109
Only one valid answer exists.
 

Follow-up: Can you come up with an algorithm that is less than O(n2) time complexity?


Answer

First approach (o(n^2))

You have a worst-case run time of O(n2). This is the problem. You would have to go over each number more than once, once in the "X" loop and once for each of the two numbers you are looking for if they are near the end of the list.


Algorithm

for each number X in list of numbers: 
    for each number Y in list of numbers starting from X: 
        if X+Y equal target number, return indices

1. Python Brut force solution

# Define the function taking 2 args(nums which is list and target which is integer)
def twoSum(self, nums: List[int], target: int) -> List[int]:
        #Looping elements taking the range
        for i in range(len(nums)):
            #Looping from i+1 to total nums list
            for j in range(i+1, len(nums)):
                #conditional check to check target
                if nums[i] + nums[j] == target:
                    #return the indices
                    return [i, j]

2. Hashmap Solution

Algorithm

instantiate an empty dictionary
for each number in list of numbers:
    result = subtract number from target number
    look for result in the dictionary (instant lookup)
    if found:
        return index of number and index of dictionary lookup result
    else:
        add number to dictionary as key with value being the index


Code

 def twoSum(nums: list[int], target: int) -> list[int]:
        #create an empty dictionary
        d = {}   
        #enumerate the list of nums     
        for index, firstvalue in enumerate(nums):
            #now get the second number using the below formula
            secondnumber = target - firstvalue
            #check condition if number present return
            if secondnumber in d: return [d[secondnumber], index]
            #if not present update the d with index
            d[firstvalue] = index
nums = [2,7,2,11,15,4,5]
target = 4
twoSum(nums, target)

without enumerate

def twoSum(nums: list[int], target: int) -> list[int]:
        #instantiate dictionary
        dictionary = {}
        #iterate through range of len of num list        
        for index in range(len(nums)):
            #find the second number using below formulae
            secondNumber = target-nums[index]
            #condition check if second number in d
            if secondNumber in dictionary:
                #if found extract from dictionary
                secondIndex = nums.index(secondNumber)
                return sorted([index, secondIndex])
                
            #if not found update the dictionary with new value    
            dictionary[nums[index]] = index
twoSum(nums, target)

