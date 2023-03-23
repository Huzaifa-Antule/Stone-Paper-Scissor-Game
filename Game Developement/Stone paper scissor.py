import time
import random
from playsound import playsound
L=["1]-""Stone","2]-""Paper","3]-""Scissor"]
# S = random.choice(L)
# print(S)
# print("\t" "*** Welcome To  The Game ***")
# for item in L:
#        print("\t""\t",item)
print("\t" "*** Welcome To The Game ***")
def sps():
 cs=[]
 ps=[]
 a=1
 while(a<=3):
    L_2=["Stone","Paper","Scissor"]


    comp= random.choice(L_2)
    while(True):
      for item in L:
          print("\t""\t",item)
      player= int(input("Its' Your Turn Pick Any of them [Enter The Number Only] " "\n"))
     # player=str(input(f"Enter Your Choice :-")
      if(player==1):
        print(f"Your Choice is :{L_2[0]}")
        playsound('C:\\Users\\Huzaifa\\Desktop\\Python Learning\\Game Developement\\stone-dropping-6843.mp3')
        break
      elif(player==2):
        print(f"Your Choice is : {L_2[1]}")
        playsound('C:\\Users\\Huzaifa\\Desktop\\Python Learning\\Game Developement\\mixkit-paper-slide-1530.wav')
        break
      elif(player==3):
        print(f"Your Choice is : {L_2[2]}")
        playsound('C:\\Users\\Huzaifa\\Desktop\\Python Learning\\Game Developement\\mixkit-player-jumping-in-a-video-game-2043.wav')
        break
      else:
         print("Invalid Choice, Please Try Again.")
    if(comp==L_2[0]):
        print(f"Computer's Choice is: {comp}")
        time.sleep(0.1)
        playsound('C:\\Users\\Huzaifa\\Desktop\\Python Learning\\Game Developement\\stone-dropping-6843.mp3')
    if(comp==L_2[1]):
        print(f"Computer's Choice is: {comp}")
        time.sleep(0.1 )
        playsound('C:\\Users\\Huzaifa\\Desktop\\Python Learning\\Game Developement\\mixkit-paper-slide-1530.wav')
    if(comp==L_2[2]):
        print(f"Computer's Choice is: {comp}")
        time.sleep(0.1)
        playsound('C:\\Users\\Huzaifa\\Desktop\\Python Learning\\Game Developement\\mixkit-player-jumping-in-a-video-game-2043.wav')
    else:
         None
    
    
# L_2=["Stone","Paper","Scissor"]
    if(player==1):
        if(L_2[0]==comp):
             print("\t"f"***| Tied |***")
        elif(comp ==L_2[1]):
             if a==1:
              print("\t"f" Computer Won {a}st Game.")
              cs.append(a)
             if a==2:
              print("\t"f" Computer Won {a}nd Game.")
              cs.append(a)
             if a==3:
              print("\t"f" Computer Won {a}rd Game.")
              cs.append(a)
        elif(comp ==L_2[2]):
             if a==1:
              print("\t"f"*** You Won {a}st Game ***")
              ps.append(a)
             if a==2:
              print("\t"f"*** You Won {a}nd Game ***")
              ps.append(a)
             if a==3:
              print("\t"f"*** You Won {a}rd Game ***")
              ps.append(a)
        else:
            None
    elif(player==2):
        if(L_2[1]==comp):
             print("\t"f"***| Tied |***")
        elif(comp ==L_2[0]):
             if a==1:
              print("\t"f"*** You Won {a}st Game ***")
              ps.append(a)
             if a==2:
              print("\t"f"*** You Won {a}nd Game ***")
              ps.append(a)
             if a==3:
              print("\t"f"*** You Won Game ***")
              ps.append(a)

        
        elif(comp ==L_2[2]):
             if a==1:
              print("\t"f" Computer Won {a}st Game.")
              cs.append(a)
             if a==2:
              print("\t"f" Computer Won {a}nd Game.")
              cs.append(a)
             if a==3:
              print("\t"f" Computer Won {a}rd Game.")
              cs.append(a)
        
        else:
            None
    elif(player==3):
        if(L_2[2]==comp):
             print("\t"f" ***| Tied |***")
        elif(comp ==L_2[1]):
             if a==1:
              print("\t"f"*** You Won {a}st Game ***")
              ps.append(a)
             if a==2:
              print("\t"f"*** You Won {a}nd Game ***")
              ps.append(a)
             if a==3:
              print("\t"f"*** You Won {a}rd Game ***")
              ps.append(a)
        elif(comp ==L_2[0]):
             if a==1:
              print("\t"f" Computer Won {a}st Game.")
              cs.append(a)
             if a==2:
              print("\t"f" Computer Won {a}nd Game.")
              cs.append(a)
             if a==3:
              print("\t"f" Computer Won {a}rd Game.")
              cs.append(a)
        
        else:
            None
    else:  
          pass
    if(a==3):
      if(len(cs)>len(ps)):
        print("\t""  Computer Won The Game δ")
        print("\t"f"Computer Won The Game {len(cs)} Times.")
        playsound('C:\\Users\\Huzaifa\\Desktop\\Python Learning\\Game Developement\\gameover-86548.mp3')
      elif(len(cs)==len(ps) ):
          print("\t""***| Match Draw ↨|***")
      elif(len(cs)<len(ps)):
          print("\t""\t""ßooyah ¢")
          print("\t"f"You Won The Game {len(ps)} Times.")
          playsound('C:\\Users\\Huzaifa\\Desktop\\Python Learning\\Game Developement\\mixkit-clapping-male-crowd-439.wav')
    else:
          None 
    # break
    a=a+1
sps()
while(True):
 ask=str(input("Want To Play Again..??" "\n""Enter Y For Playing" "\n""\t""Or""\n""Enter N For Exit ""\n"))
 if(ask=="Y"): sps()
 elif(ask=="N"): exit()
 else:
     print("Please Try Again.")
