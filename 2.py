class Person:
    def __init__(self, name, gender, age):
        # Person 클래스의 초기화 메서드
        self.name = name    # 이름
        self.gender = gender  # 성별
        self.age = age      # 나이

    def display(self):
        # 개인 정보 출력 메서드
        print(f"이름: {self.name}, 성별: {self.gender}")
        print(f"나이: {self.age}")

    def greet(self):
        # 나이에 따라 인사 메시지를 다르게 출력
        if self.age >= 20:
            print(f"안녕하세요, {self.name}님! 성인이시군요!")
        else:
            print(f"안녕하세요, {self.name}님, 좋을 떄네요.")

def get_person_info():
    # 사용자로부터 개인 정보 입력 받기
    while True:
        name = input("이름: ")
        # 이름이 문자열인지 확인
        if name.isalpha():
            break
        print("이름은 문자열만 입력할 수 있습니다.")

    while True:
        gender = input("성별: ")
        # 성별이 'male' 또는 'female'인지 확인
        if gender in ["male", "female"]:
            break
        print("성별은 'male' 또는 'female'이어야 합니다.")

    while True:
        age = input("나이: ")
        # 나이가 유효한 정수인지 확인
        try:
            age = int(age)
            if age >= 0:
                break
            print("나이는 0 이상의 정수여야 합니다.")
        except ValueError:
            print("나이는 숫자여야 합니다.")

    # 입력된 정보를 바탕으로 Person 객체 생성
    return Person(name, gender, age)

# 사용자로부터 정보를 받아 Person 객체 생성
person = get_person_info()
# 개인 정보 출력
person.display()
# 인사 메시지 출력
person.greet()
