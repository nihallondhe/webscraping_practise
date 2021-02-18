class Employe:
    def __init__(self,Name,Amount):
        self.Name=Name
        self._Amount=Amount
    def display(self):
        print(f'Salary{self._Amount}')

emp=Employe('nihal',54000)
emp.display()

class salary(Employe):
    def __init__(self,Name):
        Employee. __init__(self,Name)
        print(f'{Name}')
sal=salary()
