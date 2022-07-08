import random

cnt = 1 #1부터 31까지 카운트 누적

def brGame():
  num = 0 #입력 받는 숫자(1,2,3 중 하나)
  while(True):
    try:
      num = int(input("부를 숫자의 개수를 입력하세요(1, 2, 3만 입력 가능) : "))
    except ValueError:
      print("정수를 입력하세요")
    else : 
      if(num != 1 and num != 2 and num != 3):
        print("1, 2, 3 중 하나만 입력하세요")
      else:
        break;
  return num  

while(cnt <= 31):
    # Computer
  comNum = random.randint(1,3)
  for i in range(0, comNum):
    if cnt > 31:
      break;
    else: 
      print("computer : " , cnt)
      cnt += 1
  if(cnt > 31):
    print("player win!")
    break;
    
    # player
  playNum = brGame()
  for i in range(0, playNum):
    if cnt > 31:
      break;
    else: 
      print("player : ", cnt)
      cnt += 1
  if(cnt > 31):
    print("computer win!")
    break;