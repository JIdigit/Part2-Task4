time1=[int(input()),int(input()),int(input())]
time2=[int(input()),int(input()),int(input())]
if time1[1]==time2[1] and time1[2]==time2[2]:
    print("No space between")
elif time2[1]>time1[1]:
    seconds=(time2[1]-time1[1])*60+time2[2]-time1[2]
print(seconds)