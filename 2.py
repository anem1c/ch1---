class Person:
    def __init__(self, name, gender, age):
        self.name = name
        self.gender = gender
        self.age = age

    def display(self):
        print(f"이름: {self.name}, 성별: {self.gender}")
        print(f"나이: {self.age}")

    def greet(self):
        if self.age >= 20:
            print(f"안녕하세요, {self.name}님! 성인이시군요!")
        else:
            print(f"안녕하세요, {self.name}님, 좋을 떄네요.")

def get_person_info():
    while True:
        name = input("이름: ")
        if name.isalpha():
            break
        print("이름은 문자열만 입력할 수 있습니다.")

    while True:
        gender = input("성별: ")
        if gender in ["male", "female"]:
            break
        print("성별은 'male' 또는 'female'이어야 합니다.")

    while True:
        age = input("나이: ")
        try:
            age = int(age)
            if age >= 0:
                break
            print("나이는 0 이상의 정수여야 합니다.")
        except ValueError:
            print("나이는 숫자여야 합니다.")

    return Person(name, gender, age)

person = get_person_info()
person.display()
person.greet()
