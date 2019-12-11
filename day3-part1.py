from typing import List, Tuple
import math

def readFile(filename: str) -> List[List[str]]:
      filecontents = []
      with open(filename) as f:
        line = f.readline()

        while line:
          filecontents.append(processLine(line))

          line = f.readline()
      
      return filecontents

def processLine(line: str) -> List[str]:
  return line.split(',')

class Solution:
    # returns [noun, verb] given a desired value at codelist[0]
    def convertMove(self, moveStr: str):
      direction = moveStr[0]
      distance = int(moveStr[1:])
      return (direction, distance)

    def getMovePoints(self, startXY: Tuple[int], moveStr: str):
      direction, distance = self.convertMove(moveStr)
      # X, Y = startXY
      visited = set() # (x,y)
      steppiece = 1

      if direction == 'L' or direction == 'D':
        # distance *= -1
        steppiece = -1
      if direction == 'L' or direction == 'R':
        # X += distance
        step = (steppiece, 0)
      if direction == 'U' or direction == 'D':
        # Y += distance
        step = (0, steppiece)

      newXY = startXY
      for i in range(abs(distance)):
        # startXY += step
        newXY = tuple(sum(x) for x in zip(newXY, step))
        # print(f'adding {newXY}')
        visited.add(newXY)
      
      # print(startXY, newXY)
      return visited, newXY

    def getPathPoints(self, path:List[str]) -> int:
      visited = set() # (x,y)

      startPoint = (0, 0)
      for p in path:
        old_vi, startPoint = self.getMovePoints(startPoint, p)
        visited = visited.union(old_vi)

      return visited

    def nearestInter(self, paths:List[List[str]]) -> int:
      line1 = paths[0]
      line2 = paths[1]
      # visited = set() # (x,y)
      # print(line1, line2)

      visited1 = self.getPathPoints(line1)
      visited2 = self.getPathPoints(line2)

      overlap = visited1.intersection(visited2)

      shortest_dist = 5000
      for o in overlap:
        dist = abs(o[0]) + abs(o[1])
        if dist < shortest_dist:
          shortest_dist = dist
          closest_inter = o

      return shortest_dist, closest_inter



s = Solution()
filecontents = readFile("input3.txt")

test = ["R8,U5,L5,D3", "U7,R6,D4,L4"]
test = ["R75,D30,R83,U83,L12,D49,R71,U7,L72",
"U62,R66,U55,R34,D71,R55,D58,R83"]
test = [
  "R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51",
"U98,R91,D20,R16,D67,R40,U7,R15,U6,R7"
]
inputlist = []
for l in test:
  linecontents = processLine(l)
  inputlist.append(linecontents)

# print(inputlist)
# filecontents = inputlist
## end of test
print(filecontents)

print(len(filecontents[0]), len(filecontents[1]))

# output = s.intdecode(12, 2, filecontents)
output = s.nearestInter(filecontents)
print(output)
