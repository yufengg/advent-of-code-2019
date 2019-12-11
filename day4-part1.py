from typing import List, Tuple
import math
import sys

class Solution:
    # returns [noun, verb] given a desired value at codelist[0]
    def rangeCheck(self, lower: int, upper: int):
      counter = 0
      for i in range(lower, upper+1):
        if self.checkVal(i):
          # print(i)
          counter += 1

      return counter

    def checkVal(self, val:int) -> bool:
#Two adjacent digits are the same (like 22 in 122345).
#Going from left to right, the digits never decrease; they only ever increase or stay the same (like 111123 or 135679).

      str_val = str(val)
      doublenum = False

      for i in range(len(str_val)-1):
        if str_val[i] == str_val[i+1]:
          doublenum = True
          
        if int(str_val[i]) > int(str_val[i+1]):
          return False

      return doublenum


s = Solution()

output = s.rangeCheck(137683, 596253)
print(output)
