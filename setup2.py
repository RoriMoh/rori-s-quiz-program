import os

from aiohttp import AsyncResolver



a = input('FILE PATH : ')
a = open(a,'r')

o = a.read().rstrip('\n').split('\n')
print(o)




answer1 = input('answer1:')
answer2 = input('answer2: ')
answer3 = input('answer3: ')
answer4 = input('answer4:')
answer5 = input('answer5: ')
answer6 = input('answer6: ')
answer7 = input('answer7:')
answer8 = input('answer8: ')
answer9 = input('answer9: ')
answer10 = input('answer10:')
answer11 = input('answer11: ')
answer12 = input('answer12: ')
answer13 = input('answer13:')
answer14 = input('answer14: ')
answer15 = input('answer15: ')
answer16 = input('answer16:')
answer17 = input('answer17: ')
answer18 = input('answer18: ')
answer19 = input('answer19:')
answer20 = input('answer20: ')

answers = [answer1,answer2,answer3,answer4,answer5,answer6,answer7,answer8,answer9,answer10,answer11,answer12,answer13,answer14,answer15,answer16,answer17,answer18,answer19,answer20]
points = 0
for i in range(len(answers)):
    if answers[i].startswith('p'):
        points += 1
        print(str(answers[i])+' is true')
        




print('you had '+ str(points)+' from 20')