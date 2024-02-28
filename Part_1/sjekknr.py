from decimal import Decimal

i_0 = 300
i = i_0
sum = 0
total = 0

latlng = 720 * 360

while (i > 1):
    sum += i
    i = i -1

print("Number of n + m combinations:", sum , "with n =", i_0)

total = sum * latlng

print("Number of longitude and latitude combinations:", latlng )

total2 = '%.2E' % Decimal(total)
print("Number of problems to be solved:", total2)

total3 = total / (10**7 * 60)

print("Number of minutes it will take to compute for all coordinates:" , total3)