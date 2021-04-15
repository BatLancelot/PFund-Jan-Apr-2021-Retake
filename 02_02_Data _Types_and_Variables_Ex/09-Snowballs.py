number_of_snowballs = int(input())

bigest_Snow = 0
bigest_Time = 0
bigest_Quality = 0
snowballValue = 0

for i in range(number_of_snowballs):
    snowballSnow = int(input())
    snowballTime = int(input())
    snowballQuality = int(input())
    value = (snowballSnow // snowballTime) ** snowballQuality
    if value > snowballValue:
        snowballValue = value
        bigest_Snow = snowballSnow
        bigest_Time = snowballTime
        bigest_Quality = snowballQuality

print(f'{bigest_Snow} : {bigest_Time} = {snowballValue} ({bigest_Quality})')
