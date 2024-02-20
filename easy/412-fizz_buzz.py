"""
Given an integer n, return a string array answer (1-indexed) where:

answer[i] == "FizzBuzz" if i is divisible by 3 and 5.
answer[i] == "Fizz" if i is divisible by 3.
answer[i] == "Buzz" if i is divisible by 5.
answer[i] == i (as a string) if none of the above conditions are true.
 

Example 1:

Input: n = 3
Output: ["1","2","Fizz"]
Example 2:

Input: n = 5
Output: ["1","2","Fizz","4","Buzz"]
Example 3:

Input: n = 15
Output: ["1","2","Fizz","4","Buzz","Fizz","7","8","Fizz","Buzz","11","Fizz","13","14","FizzBuzz"]
"""

class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        answer = [""] * n
        for i in range(n):
            v = i + 1
            if (v % 3) == 0 and (v % 5) == 0:
                answer[i] = "FizzBuzz"
            elif (v % 3) == 0:
                answer[i] = "Fizz"
            elif (v % 5) == 0:
                answer[i] = "Buzz"
            else:
                answer[i] = str(v)
        return answer