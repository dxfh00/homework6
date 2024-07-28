my_dict={'Anton':1980,'Denis':1981,'Nikita':1999}
print(my_dict)
print(my_dict['Anton'])
print(my_dict.get('0000','No key'))
my_dict.update({'Lera':2004,'Kirill':2008})
print(my_dict)
my_dict.pop('Nikita')
print(my_dict)
#
my_set={1,1,'a','a',False,False,2}
print(my_set)
my_set.add(3)
my_set.remove(False)
print(my_set)
