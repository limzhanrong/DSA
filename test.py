# def solve(string):
#    for i in range (0, len(string)):
#       if (string[i] == string[i + 1]):
#          return True
#    return False
# s = "afternoon"
# print(solve(s))
mySet = set()

def testFunction(ok, i):
    if i <= 5:
        ok.add(i)
        testFunction(ok,i + 1)

testFunction(mySet, 0)
print(mySet)