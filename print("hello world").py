import random
import time
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

computer_number = random.randrange(0, 100)
secret_code = 69
credit_card = range(1, 68)
credit_card2 = range (0, 100000000)

guessed = False

while True:
  if not guessed:
      answer = input("Guess the number: ")
      if int(answer) == computer_number:
          guessed = True
          print(bcolors.BOLD + "YOU WIN 1 GAZILLION $$$" + bcolors.ENDC)
          time.sleep(0.5)
          print(bcolors.OKGREEN + "ENTER CREDIT CARD INFO TO GET YOUR CASH PRIZE1!!!")
          time.sleep(0.3)
          info = input("enter info here: ")
          if int(info) == secret_code:
            print(bcolors.FAIL + "fuck you")
          if int(info) < secret_code:
             print(bcolors.OKCYAN + "WAHOO FREE M- i mean thank you kind sir")
          if int(info) > secret_code:
             print(bcolors.OKCYAN + "WAHOO FREE M- i mean thank you kind sir")
          break
      elif int(answer) > computer_number:
          print(bcolors.WARNING + "dumbass too high!!" + bcolors.ENDC)
      else:
          print(bcolors.WARNING + "dumbass too low!!" + bcolors.ENDC)
  else:
      break