guests = ['Brendon', 'Bruce','Lee']
print(guests[0] + ' Will you go to my meet up ')
print(guests[1] + ' Will you go to my meet up ')
print(guests[2] + ' Will you go to my meet up \n')

print(guests[0])
guests[0] = 'Jo'
print(guests[0] + ' Will you go to my meet up ')
print(guests[1] + ' Will you go to my meet up ')
print(guests[2] + ' Will you go to my meet up \n')

guests.insert(0, 'John')
guests.insert(2, 'Week')
guests.append('Blitz')
print(guests[0] + ' Will you go to my meet up ')
print(guests[1] + ' Will you go to my meet up ')
print(guests[2] + ' Will you go to my meet up ')
print(guests[3] + ' Will you go to my meet up ')
print(guests[4] + ' Will you go to my meet up ')
print(guests[5] + ' Will you go to my meet up \n')
print(len(guests))
popped_guest = guests.pop()
print(popped_guest + " i'm so sorry")
popped_guest = guests.pop()
print(popped_guest + " i'm so sorry")
popped_guest = guests.pop()
print(popped_guest + " i'm so sorry")
popped_guest = guests.pop()
print(popped_guest + " i'm so sorry")
print(guests[0] + ' Will you go to my meet up ')
print(guests[1] + ' Will you go to my meet up \n')
del guests[:2]
print(guests)



