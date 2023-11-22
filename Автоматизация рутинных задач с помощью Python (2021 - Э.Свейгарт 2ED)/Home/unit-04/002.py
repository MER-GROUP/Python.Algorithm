import random as rd

number_of_streaks = 0

for experiment_number in range(1000):
    s = ''.join(str(rd.randint(0,1)) for _ in range(100))
    number_of_streaks += s.count('000000') + s.count('111111')

print('Вероятность появления серии: %s%%' %(number_of_streaks/100))