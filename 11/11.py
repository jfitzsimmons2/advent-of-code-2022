from decimal import Decimal
import sys
from functools import reduce

class Monkey:
    items = []
    operation = []
    inspects = 0

    def add_item(self, num):
        self.items.append(num)

    def do_operation(self, old):
        global mod;
        res = 0
        str = " ".join(self.operation[2:]);
        res = eval(str)
        res = res%mod
        divisible = not res % int(self.test[2])

        if (divisible):
            monkeys[int(self.if_true[3])].add_item(res)
        else:
            monkeys[int(self.if_false[3])].add_item(res)

    def inspect_items(self):
        while self.items:
            self.inspects += 1
            old = self.items.pop(0)
            self.do_operation(old)

mod = 1
monkeys = []
monkey = Monkey()


def parse_line(parts):
    global monkey
    global monkeys

    if (len(parts)==0):
        return;
    if (parts[0] == "Monkey"):
        monkey = Monkey()
    if (parts[0] == "Starting"):
        p = [int(i.strip(",")) for i in parts[2:]]
        setattr(monkey, 'items', p)
    if (parts[0] == "Operation:"):
        o = parts[1:]
        setattr(monkey, 'operation', o)
    if (parts[0] == "Test:"):
        t = parts[1:]
        setattr(monkey, 'test', t)
    if (parts[0] == "If"):
        if (parts[1].strip(":") == "true"):
            setattr(monkey, "if_true", parts[2:])
        elif (parts[1].strip(":") == "false"):
            setattr(monkey, "if_false", parts[2:])
            monkeys.append(monkey)
        
    
with open(sys.argv[1], "r") as f:
    
    lines = f.read().splitlines()
    for i,line in enumerate(lines):    
        parse_line(line.split())

for i,monkey in enumerate(monkeys):    
    # calculate mod that won't affect tests
    mod *= int(monkey.test[2])

for _ in range(10000):
    for i,monkey in enumerate(monkeys):
        monkey.inspect_items()
        
monkey_inspect_counts = []
for i,monkey in enumerate(monkeys):
    print("Monkey", i, monkey.inspects)
    monkey_inspect_counts.append(monkey.inspects);

print(sorted(monkey_inspect_counts))
print(sorted(monkey_inspect_counts)[-2:])
print(reduce((lambda x, y: x * y), sorted(monkey_inspect_counts)[-2:]))