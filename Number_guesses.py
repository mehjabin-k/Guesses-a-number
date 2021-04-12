#number of guesses 9
#print number of guesses left
#after all try guesses print Game Over
i=0
ans=21
while i<=9 :
    num=int(input("Please Guesses a number :\n "))
    i+=1
    if num==ans:
        print("Congratulation!!!\n You Won The Game..\n Right Anwser....")
        break
    elif num>ans:
        print("Sorry!!!\n Wrong Input..\nNumebr is Grater than Anwser\n")
       # i=i-1
    elif num<ans:
        print("Sorry!!!\nWrong Input..\nNumber Less Than Anwser\n ")
        #i=i-1
    #bold_num="\033[1m" ,(9-i), "\033[0m"
    print("\nNumber Guesses Left : ",(9-i))
    if i==9:
        print("Game Over!!!")
        break
    #i=i+1

