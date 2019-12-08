from typing import List
import math

def readFile(filename: str) -> List[int]:
      filecontents = []
      with open(filename) as f:
        line = f.readline()
        while line:
          for c in line:
            if c not in '0123456789': continue
            filecontents.append(int(c))
            line = f.readline()


      return filecontents

class Solution:
    def countZeros(self, codelist: List[int]) -> int:
      count = [0,0,0]
      mins = [6*25, 6*25 , 6*25]
      layer_count = 0
      for val in codelist:
        layer_count += 1
        if val == 0: count[0] += 1
        if val == 1: count[1] += 1
        if val == 2: count[2] += 1

        if layer_count == 6*25:
          if count[0] < mins[0]:
            mins[0] = count[0]
            mins[1] = count[1]
            mins[2] = count[2]
            print(f'new mins: {mins}')
          print(f'layer done. counts: {count}')
          layer_count = 0
          count = [0,0,0]

      return mins[1] * mins[2]



s = Solution()
masslist = readFile("input8.txt")
print(len(masslist))
fueltotal = s.countZeros(masslist)
print(fueltotal)
