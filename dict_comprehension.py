temp={"mon":25,"tue":30,"wed":35}
a_temp={day:tem +5 for day,tem in temp.items()}
print(a_temp)

#num_square

n={n:n**2 for n in range(1,11)}
print(n)

#even_square

e={e:e**2 for e in range(2,21) if e%2==0}
print(e)

#day_&_lenght

days=("monday","tuesday","wednesday","thursday")
d_lenght={x:len(x) for x in days}
print(d_lenght)

#word_vowels
a=("apple","banana","Orange","yellow")
v={x:len(x) for x in a if x[0].lower() in('a','e','i','o','u')}
print(a)
print(v)

#prime_square

ps={x:x**2 for x in range(1,51) if x%range(2,x-1)!=0}
print(ps)
