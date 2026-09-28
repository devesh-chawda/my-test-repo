#x= [c for c in range(2,20) if c%2==0]
#print(x)
#y=[y **2 for y in range(0,10) if y%2!=0]
#print(y)

x={num:num**2 for num in range(1,11)}
print(x)

x={num:num**2 for num in range(1,11) if num%2==0}
print(x)

week=("monday","tuesday","wednesday","thursday","friday","saturday","sunday")
y={day:len(day) for day in week}
print(y)