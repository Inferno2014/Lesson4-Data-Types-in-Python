rname = input('Enter your real name: ')
aname = input('Enter your code/agent name: ')
gadget = input('Enter your favourite gadget: ')
anum = int(input('Enter your agent number: '))
sr = input('Enter the rating out of 1 - 10 on how fast you finish your secret mission: ')
active = input('Are you active? Yes / No: ')
print('Name:',rname)
print('Agent Name:',aname)
print('Favourite Gadget:',gadget)
print('Agent Number:',anum)
print('Speed Rating:',sr)
if active=='yes':
    print('Status: Active')
elif active=='no':
    print('Status: Inactive')

