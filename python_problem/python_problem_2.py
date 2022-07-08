class Student:
  def __init__(self, name, midscore, finalscore, grade):
    self.name = name
    self.midscore = midscore
    self.finalscore = finalscore
    self.grade = grade
  
  def calc_av(self):
    average = (self.midscore + self.finalscore) / 2
    return average
  
  def grading(self):
    average = self.calc_av()
    if average >= 90 :
      self.grade = 'A'
    elif 80 <= average < 90 :
      self.grade = 'B'
    elif 70 <= average < 80 :
      self.grade = 'C'
    else:
      self.grade = 'D'

##############  menu 1 (학생 정보 저장)
def Menu1(name, midscore, finalscore) :
    grade = 0
    student_list.append(Student(name, midscore, finalscore, grade))


##############  menu 2 (학점 부여)
def Menu2() :
  for i in range(len(student_list)):
    if(student_list[i].grade == 0):
      student_list[i].grading()


##############  menu 3 (학생 정보 출력)
def Menu3() :
  print("------------------------------")
  print("name    mid    final    grade" )
  print("------------------------------")
  for i in range(len(student_list)):
    print(student_list[i].name,'\t',student_list[i].midscore, '\t',student_list[i].finalscore, '\t',student_list[i].grade)

##############  menu 4 (학생 정보 삭제)
def Menu4(index):
  del student_list[index]

# 저장된 학생 정보 유우 체크
def check_empty(student_list):
  if(len(student_list) == 0):
        return True
  else:
    return False

# 리스트의 마지막 인덱스 반환
def last_index(student_list):
  return len(student_list) - 1

#학생 정보를 저장할 변수 초기화
student_list = []

print("*Menu*******************************")
print("1. Inserting students Info(name score1 score2)")
print("2. Grading")
print("3. Printing students Info")
print("4. Deleting students Info")
print("5. Exit program")
print("*************************************")
while True :
    choice = input("Choose menu 1, 2, 3, 4, 5 : ")
    if choice == "1":
      #학생 정보 입력받기
      #예외사항 처리(데이터 입력 갯수, 이미 존재하는 이름, 입력 점수 값이 양의 정수인지)
      #예외사항이 아닌 입력인 경우 1번 함수 호출 
      while(True):
        try:
          name, midscore, finalscore = input("Enter name mid-score final-score : ").split()
        except ValueError:
          print("Num of data is not 3!")
          break;
        else:
          exist = False;
          for i in range (len(student_list)):
            if student_list[i].name == name:
              print("Already exist name!")
              exist = True;
              break;
          if exist == True:
            continue
          else:
            try: 
              ms = int(midscore)
              fs = int(finalscore)
            except ValueError:
              print("Score is not positive integer!")
              break;
            else:
              if (ms < 0 and fs < 0):
                print("Score is not positive integer!")
                break;
              else:
                Menu1(name, ms, fs)
                break;        

    elif choice == "2" :
      #예외사항 처리(저장된 학생 정보의 유무)
      #예외사항이 아닌 경우 2번 함수 호출
      #"Grading to all students." 출력
      if(check_empty(student_list) == True):
        print("No student data!")
      else:
        Menu2()
        print("Grading to all students") 

    elif choice == "3" :
      #예외사항 처리(저장된 학생 정보의 유무, 저장되어 있는 학생들의 학점이 모두 부여되어 있는지)
      #예외사항이 아닌 경우 3번 함수 호출
      if(check_empty(student_list)==True):
        print("No student data!")
      else:
        for i in range(len(student_list)):
          if(student_list[i].grade == 0):
            print("There is a student who didn't get grade")
            break;
          else: 
            index = last_index(student_list)
            if i == index:
              Menu3()

    elif choice == "4" :
      #예외사항 처리(저장된 학생 정보의 유무)
      #예외사항이 아닌 경우, 삭제할 학생 이름 입력 받기
      #입력 받은 학생의 존재 유무 체크 후, 없으면 "Not exist name!" 출력
      #있으면(예를 들어 kim 이라 하면), 4번 함수 호출 후에 "kim student information is deleted." 출력
      if(check_empty(student_list) == True):
        print("No student data!")
      else:
        delete_name = input("Enter the name to delete : ")
        for i in range(len(student_list)):
          if(student_list[i].name == delete_name):
            Menu4(i)
            print(f"{delete_name} student information is deleted.")
            break;
          else:
            index = last_index(student_list)
            if i == index:
              print("Not exist name!")
              break;

    elif choice == "5" :
      #프로그램 종료 메세지 출력
      #반복문 종료
      print("Exit program!")
      exit()

    else :
      #"Wrong number. Choose again." 출력
      print("Wrong number. Choose again.")
