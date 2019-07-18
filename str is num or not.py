# str-is-numeric-or-not
i=list(input())
count=0
for j in i:
    if j.isnumeric():
        count+=1
if count==len(i):
    print('yes')
else:
    print('no')
