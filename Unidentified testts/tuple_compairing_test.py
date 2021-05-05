Tuple = ('Taha', 'Munawar','14','Rawalpindi')
*names, age, city = Tuple
x = ''
for i in names:
    if i != 'Taha':
        x = x + ' ' + i
    else:
        x = x + i

full_name = x

print(full_name)