import socket

class Assignment2:
    # Task 1
    def __init__(self, year: int):
        self.year = year

    # Task 2
    def tellAge(self, currentYear: int):
        age = currentYear - self.year
        print(f"Your age is {age}")

    # Task 3
    def listAnniversaries(self):
        current_year = 2022 # Assuming today is year 2022
        anniversaries = [i for i in range(10, current_year - self.year + 1, 10)]
        return anniversaries

    # Task 4
    def modifyYear(self, n):
        num = self.year
        res = ""
        arr = str(num)
        for i in range(n):
            res += arr[:2]
        num = num * n
        lst = str(num)
        arr_temp = lst[::2]
        res += arr_temp
        return res        

    # Task 5
    @staticmethod
    def checkGoodString(string):
        if len(string) < 9:
            return False
        if not string[0].islower() or string[0] < 'a' or string[0] > 'z':
            return False
        count_numbers = sum(c.isdigit() for c in string)
        if count_numbers == 1:
            return True
        else:
            return False

    # Task 6
    @staticmethod
    def connectTcp(host, port) -> bool:
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
                sock.connect((host, port))
                return True
        except Exception as e:
            return False
