import time
hour = int(time.strftime('%H'))

if 0 <= hour < 12:
    print("Good morning")
elif 12 <= hour < 17:
    print("Good afternoon")
elif 17 <= hour < 21:
    print("Good evening")
else:
    print("Good night")

    
#     import time
# t = time.strftime('%H:%M:%S')
# hour = int(time.strftime('%H'))
 
# if(hour>=0  and hour<12):
#  print("good morning")
# elif(hour>13 and hour<20):
#  print("good after noon")
# elif(hour>21 and hour<23):
#  print("good night")