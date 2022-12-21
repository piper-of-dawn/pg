from collections import deque
import re

class SupplyStacks:
    def __init__(self, path):
        self.Stacks, self.count()Instructions = re.split("\n\n", open(path).read())
        CARGO = {}
        for i in range(1,4):
            CARGO[i] = deque()
        print(f"The answer to Day 5 Part 1 is {self.main_part1()}")    

    def CreateCargoStructure (self):
    # 💀 DANGER 💀: 🤯 Mindfuck regex stuff ahead
        for s in re.split("\n", self.STACKS):
            for stack, crate in enumerate(re.findall("\s\s\s|\w", s)):
                crates = re.findall("[A-Z]+", crate)
                len(crates) and self.CARGO[stack+1].append(crates[0])
            
    def simulate_crane(self):     
        for line in self.Instructions.splitlines():
            N, From, To = map(int, re.findall("\d+",line))
            for i in range(N):
                x = self.CARGO[From].popleft()
                print(x)
                self.CARGO[To].appendleft(x)

    def main_part1(self):
        self.simulate_crane()
        message = ""
        for stack in self.CARGO:
            message += self.CARGO[stack][0]
        return message

SupplyStacks("day5_test.txt").Instructions