"""
Calendar app
Version 1.0.0(1)
"""
from time import sleep, strftime

NAME = "YourName"

calendar = {}

def welcome ():
  print "Welcome back " + NAME
  print "Calendar is opening now"
  sleep(1)
  print "Today is: " + strftime("%A %B %d, %Y")
  print "Current time is: " + strftime("%H:%M:%S")
  sleep (1)
  print "What would you like to do?"
  
def start_calendar():
  welcome()
  start = True
  while start:
    user_choice = raw_input("A to Add, U to Update, V to View, D to Delete, X to Exit: ")
    user_choice = user_choice.upper()
    if user_choice == "V":
      if len(calendar.keys()) < 1:
        print "Calendar empty."
      else:
        print calendar
    elif user_choice == "U":
      date = raw_input("What date?")
      update = raw_input("Enter the update:")
      if calendar[date] == None:
        print "Wrong date, try again."
        try_again = raw_input("Try again? Y for Yes, N for No: ")
        try_again = try_again.upper()
        if try_again == "Y":
          continue
        else:
          start = False
      else:
        calendar[date] = update
        print "Update complete"
        print calendar
    elif user_choice == "A":
      event = raw_input("Enter event: ")
      date = raw_input("Enter date (MM/DD/YYYY): ")
      if (len(date) > 10 or int(date[6:]) < int(strftime("%Y"))):
        print "Wrong date, try again"
        try_again = raw_input("Try again? Y for Yes, N for No: ")
        try_again = try_again.upper()
        if try_again == "Y":
          continue
        else:
          start = False
      else:
        calendar[date] = event
        print calendar
    elif user_choice == "D":
      if len(calendar.keys()) < 1:
        print "Calendar is empty"
      else:
        event = raw_input("What event?")
        for date in calendar.keys():
          if event == calendar[date]:
            del calendar[date]
            print "Event deleted"
            if len(calendar.keys()) < 1:
              print "Calendar is empty"
            else:
              print calendar
          else:
            print "There's no events like this."
    elif user_choice == "X":
      start = False
    else:
      print "Wrong command. Exit."
      start = False
  
start_calendar()