from typing import List
import math

class Solution:
    def readFile(self, filename: str) -> List[int]:
      filelist = []
      with open(filename) as f:
        line = f.readline()
        while line:
          filelist.append(int(line))
          line = f.readline()


      return filelist

    

    def countFuel(self, masslist: List[int]) -> int:

      def computeFuel(mass: int) -> int:
        if mass == 0: return 0

        fuel = math.floor(mass/3) - 2
        
        # if part1, return fuel now

        if fuel < 0:
          return 0
        else:
          return computeFuel(fuel) + fuel


      total = 0
      # Specifically, to find the fuel required for a module, take its mass, divide by three, round down, and subtract 2.
      for m in masslist:
        total += computeFuel(m)

      return total



s = Solution()
masslist = s.readFile("input1.txt")
print(len(masslist))
fueltotal = s.countFuel(masslist)
print(fueltotal)
