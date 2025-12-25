class Employee:
    def __init__(self, name, emp_id):
        self.name = name
        self.id = emp_id

    def get_info(self):
        return f"Сотрудник: {self.name} (ID: {self.id})"


class Manager(Employee):
    def __init__(self, name, emp_id, department):
        super().__init__(name, emp_id)
        self.department = department
    def manage_project(self, project_name):
        return f"{self.name} управляет проектом: {project_name}"

    def get_info(self):
        return f"{super().get_info()}, Отдел: {self.department}"


class Technician(Employee):
    def __init__(self, name, emp_id, specialization):
        super().__init__(name, emp_id)
        self.specialization = specialization

    def perform_maintenance(self, system_name):
        return f"{self.name} выполняет тех. обслуживание: {system_name}"

    def get_info(self):
        return f"{super().get_info()}, Специализация: {self.specialization}"


class TechManager(Manager, Technician):
    def __init__(self, name, emp_id, department, specialization):
        Employee.__init__(self, name, emp_id)
        self.department = department
        self.specialization = specialization
        self.__team = []

    def add_employee(self, employee):
        self.__team.append(employee)

    def team_info(self):
        print(f"\nКоманда TechManager: {self.name}")
        for emp in self.__team:
            print(" -", emp.get_info())

    def get_info(self):
        return f"{Employee.get_info(self)}, Отдел: {self.department}, Специализация: {self.specialization}"


emp = Employee("Иван", 101)
mgr = Manager("Ольга", 102, "Разработка")
tech = Technician("Дмитрий", 103, "Сети")
tm = TechManager("Роман", 104, "Инфраструктура", "DevOps")

tm.add_employee(emp)
tm.add_employee(mgr)
tm.add_employee(tech)

print(emp.get_info())
print(mgr.get_info())
print(tech.get_info())
print(tm.get_info())
tm.team_info()
