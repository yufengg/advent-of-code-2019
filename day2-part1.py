from typing import List
import math

def readFile(filename: str) -> List[int]:
      filecontents = []
      with open(filename) as f:
        line = f.readline()
        # line = "2,4,4,5,99,0"
        while line:
          filecontents = line.split(',')
          # filecontents.append(int(c))
          line = f.readline()
      
      int_list = []
      for s in filecontents:
        int_list.append(int(s))
      
      return int_list

class Solution:
    def intdecode(self, codelist: List[int]) -> int:
      # replace position 1 with the value 12 and replace position 2 with the value 2. 
      codelist[1] = 12
      codelist[2] = 2

      codelen = len(codelist)
      # print(codelist, codelen)

      for i in range(0,codelen, 4):
        action = codelist[i]
        if action == 99:
          break
        val1 = codelist[i+1]
        val2 = codelist[i+2]
        out_loc = codelist[i+3]
        print(f'processing i={i}, vals: {codelist[i:i+4]}')
        
        if action == 1:
          codelist[out_loc] = codelist[val1] + codelist[val2]
        if action == 2: 
          codelist[out_loc] = codelist[val1] * codelist[val2]
        
        
        print(f'wrote to {out_loc} val {codelist[out_loc]}')
      
      print(codelist)
      return codelist[0]



s = Solution()
filecontents = readFile("input2.txt")
print(filecontents)
print(len(filecontents))
output = s.intdecode(filecontents)
print(output)
