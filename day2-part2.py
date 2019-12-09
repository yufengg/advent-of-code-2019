from typing import List
import math

def readFile(filename: str) -> List[int]:
      filecontents = []
      with open(filename) as f:
        line = f.readline()

        while line:
          filecontents = line.split(',')

          line = f.readline()
      
      int_list = []
      for s in filecontents:
        int_list.append(int(s))
      
      return int_list

class Solution:
    # returns [noun, verb] given a desired value at codelist[0]
    def findNounVerb(self, desired:int, codelist: List[int]) -> List[int]:
      for noun in range(100):
        for verb in range(100):
          output = self.intdecode(noun, verb, codelist[:])
          print(f'got output {output}')
          if output == desired:
            return [noun, verb]


    def intdecode(self, noun: int, verb: int, codelist: List[int]) -> int:

      codelist[1] = noun
      codelist[2] = verb
      print(f'trying {noun, verb}')

      codelen = len(codelist)
      # print(codelist, codelen)

      for i in range(0,codelen, 4):
        action = codelist[i]
        if action == 99:
          break
        val1 = codelist[i+1]
        val2 = codelist[i+2]
        out_loc = codelist[i+3]
        # print(f'processing i={i}, vals: {codelist[i:i+4]}')

        try:
          if action == 1:
              codelist[out_loc] = codelist[val1] + codelist[val2]
          if action == 2: 
            codelist[out_loc] = codelist[val1] * codelist[val2]
        except:

          return -1
        
        # print(f'wrote to {out_loc} val {codelist[out_loc]}')
      
      # print(codelist)
      # print(noun, verb)
      return codelist[0]



s = Solution()
filecontents = readFile("input2.txt")
print(filecontents)
print(len(filecontents))
# output = s.intdecode(12, 2, filecontents)
output = s.findNounVerb(19690720, filecontents)
print(output)
