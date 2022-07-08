num = 0 #입력 받는 숫자(1,2,3 중 하나)
cnt = 1 #1부터 31까지 카운트 누적

while(cnt <= 31):
    # player A
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
  for i in range(0, num):
    if cnt > 31:
      break;
    else: 
      print("playerA : " , cnt)
      cnt += 1
  if(cnt > 31):
    break;
    # player B
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
  for i in range(0, num):
    if cnt > 31:
      break;
    else: 
      print("playerB : ", cnt)
      cnt += 1
  if(cnt > 31):
    break;