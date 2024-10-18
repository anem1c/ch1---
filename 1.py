import random

def num_guess():
    num = random.randint(1, 10)
    print("1과 10 사이의 숫자를 하나 정했습니다.")
    
    while True:
        try:
            guessed_num = int(input("예상 숫자: "))
            if guessed_num < 1 or guessed_num > 10:
                print("유효한 범위 내의 숫자를 다시 입력하세요.")
            elif guessed_num < num:
                print("너무 작습니다. 다시 입력하세요.")
            elif guessed_num > num:
                print("너무 큽니다. 다시 입력하세요.")
            else:
                print("정답입니다!")
                break
        except ValueError as e:
            print(f"입력 오류: {e}. 유효한 숫자를 입력하세요.")
# 게임 시작
num_guess()
while True:
    restart = input("게임을 다시 하시곘습니까? (y/n): ").strip().lower()
    if(restart == 'y'):
        num_guess()
    elif(restart == 'n'):
        print("게임을 종료합니다. 감사합니다!")
        break    
    else:
        continue