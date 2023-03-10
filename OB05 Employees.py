employees = []

class Employees():
    def __init__(self, FirstName: str, LastName: str):
        self.__fullname = FirstName + " " + LastName #string
        self.__email = FirstName.lower() + "." + LastName.lower() + "@company.com" #string

    def get_employee_email(self, employeeID: str):
        self.__employeeID = employeeID #string
        print(self.__email)

    def print_details(self, employeeID: str):
        print("EmployeeID: ", employeeID)
        print("Employee Full Name: ",self.__fullname)
        print("Employee Email: ",self.__email)

file = open('emailList.txt','r')
content = file.readlines()
file.close()

for i in range(9):
    employees.append(Employees(content[i*2].strip(),content[i*2+1].strip()))

