import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
logo='''
 __          __  _ _                                          
 \ \        / / | | |                                         
  \ \  /\  / ___| | | ___   ___ ___  _ __ ___   ___           
   \ \/  \/ / _ | | |/ _ \ / __/ _ \| '_ ` _ \ / _ \          
    \  /\  |  __| | | (_) | (_| (_) | | | | | |  __/          
     \/  \/ \___|_|_|\___/ \___\___/|_| |_| |_|\___|          
     _                                                        
    | |                                                       
    | |_ ___                                                  
    | __/ _ \                                                 
    | || (_) |                written by:Amarjeet                                   
     \__\___/                                                 
       _____       _____                                    _ 
      |  __ \     |  __ \                                  | |
      | |__) _   _| |__) __ _ ___ _____      _____  _ __ __| |
      |  ___| | | |  ___/ _` / __/ __\ \ /\ / / _ \| '__/ _` |
      | |   | |_| | |  | (_| \__ \__ \\ V  V | (_) | | | (_| |
      |_|    \__, |_|   \__,_|___|___/ \_/\_/ \___/|_|  \__,_|
              __/ |                                           
             |___/                                            
'''
print(logo)
n_letters=int(input("How many letters would you like in your password? "))
n_numbers=int(input("How many numbers would you like in your password? "))
n_sybolls=int(input("How many symbolls would you like in your password? "))
password_list=[]
for char in range(0,n_letters):
    password_list.append(random.choice(letters))
for char in range(0,n_numbers):
    password_list.append(random.choice(numbers))
for char in range(0,n_sybolls):
    password_list+=random.choice(symbols)
random.shuffle(password_list)
password=""
for key in password_list:
    password+=key
print(f"Your password is: {password}")
