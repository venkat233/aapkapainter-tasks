"""
Write a code that prints out individual scores of two players in a game of cricket where score
is given as runs per ball in an array. In a game of cricket a person changes strike if he scores
an odd number, and keeps strike with him if he scores an even number. No need to consider changing
strike after every 6 balls or an over
"""
runs = [1,2,3,2,1]
p1 = 0
p2 = 0
check = True
for i in runs:
    if check == True:
        p1 = p1+i
        if i in [1,3,5]:
            check = False
    else:
        p2 = p2+i
        if i in [1,3,5]:
            check = True
print(p1, p2)