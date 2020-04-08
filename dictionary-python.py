#Contoh cara membuat Dictionary pada Python

dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}

print ("dict['Name']: ", dict['Name'])

print ("dict['Age']: ", dict['Age'])

#Update Nilai Dalam Dictionary Python

dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'} 
dict['School'] = "DPS School"
dict['Age'] = 8;

print ("dict['Age']: ", dict['Age'])

print ("dict['School']: ", dict['School'])



#Hapus Elemen Dictionary Python

dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}
dict['School'] = "DPS School"
print ("dict['Age']: ", dict['Age'])
print ("dict['School']: ", dict['School'])
del dict['Name']
dict.clear()
del dict
