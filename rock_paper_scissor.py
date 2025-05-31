# Aisha
# import random 
# rock = '''
#    ------(""""")
#    -----------(""""")
#   ------------(""""")
#   -----------(""""")
#   -----------("""")
# '''
# paper = '''
#   -----(""""")
#  ----------------(""""")
# --------------------(""""")
#  ------------------(""""")
#   -------------(""""")
# '''

# scissor = '''
#   -----(""""")
#  --------------------(""""")
# -------------------------(""""")
# ---------(""""")
# --------(""""")
# '''
# wrong = '''
# ...      ...
#  ...    ...
#    ... ... 
#     ....  
#   ...  ...   
#  ...    ...   
# ...      ...
# '''
# game = [rock,paper,scissor]
# user_choice =int( input ("wellcome to rock paper scissor\n\nFor rock enter 0\nFor paper enter 1\nFor scissor enter 2\nSo. what is your choice :"))

# if user_choice > 2 :
#     print (f"wrong input\n{wrong}")
# else:
#     computer_choice = random.randint(0,2)
#     print(game[user_choice])
#     print ("computer choice")
#     print (game[computer_choice])

#     if user_choice == computer_choice:
#         print("draw")
#     elif user_choice == 0 and computer_choice == 2:
#         print("you are the winner")
#     elif user_choice == 2 and computer_choice == 0:
#         print("you are the losser")
#     elif user_choice > computer_choice:
#         print("you are the winner")
#     elif user_choice < computer_choice:
#         print("you are the losser")
