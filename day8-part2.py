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
      image = []
      mins = [6*25, 6*25 , 6*25]

      layer = []
      row = []

      for val in codelist:
        row.append(val)
        if len(row) == 25:
          layer.append(row)
          row = []
        
        if len(layer) == 6:
          image.append(layer)
          layer = []
      # go through each position and print it's val if black?
      image_row = []
      for c in range(6):
        for r in range(25):
          for i in range(100):
            pix = image[i][c][r]
            if pix != 2:
              if pix == 1:
                image_row.append('8')
              elif pix == 0:
                image_row.append(' ')
              break
          else:
            image_row.append(' ')
        print(''.join(image_row))
        image_row = []

      return 



s = Solution()
masslist = readFile("input8.txt")
print(len(masslist))
fueltotal = s.countZeros(masslist)
print(fueltotal)
