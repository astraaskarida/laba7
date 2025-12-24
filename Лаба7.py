class Employee:
    def __init__(self, name: str, emp_id: int):
        self.name = name
        self.id = emp_id

    def get_info(self):
        return f"Сотрудник: {self.name} (ID: {self.id})"


class Manager(Employee):
    def __init__(self, name: str, emp_id: int, department: str):
        super().__init__(name, emp_id)
        self.department = department

    def manage_project(self, project_name: str):
        return f"{self.name} управляет проектом: {project_name}"

    def get_info(self):
        return f"{super().get_info()}, Отдел: {self.department}"


class Technician(Employee):
    def __init__(self, name: str, emp_id: int, specialization: str):
        super().__init__(name, emp_id)
        self.specialization = specialization

    def perform_maintenance(self, system_name: str):
        return f"{self.name} выполняет тех. обслуживание: {system_name}"

    def get_info(self):
        return f"{super().get_info()}, Специализация: {self.specialization}"


class TechManager(Manager, Technician):
    def __init__(self, name: str, emp_id: int, department: str, specialization: str):

        Employee.__init__(self, name, emp_id)
        self.department = department
        self.specialization = specialization

        self.__team = []

    def add_employee(self, employee: Employee):
        self.__team.append(employee)

    def team_info(self):
        print(f"Команда TechManager: {self.name} (подчинённых: {len(self.__team)})")
        for emp in self.__team:
            print(" -", emp.get_info())

    def get_info(self):
        return (f"{Employee.get_info(self)}, Отдел: {self.department}, "
                f"Специализация: {self.specialization}")



emp = Employee("Иван Петров", 101)
mgr = Manager("Ольга Смирнова", 102, "Разработка")
tech = Technician("Дмитрий Кузнецов", 103, "Сети")

tech_mgr = TechManager("Роман Чекин", 104, "Инфраструктура", "DevOps")

print(emp.get_info())
print(mgr.get_info())
print(tech.get_info())
print(tech_mgr.get_info())

print(mgr.manage_project("CRM-система"))
print(tech.perform_maintenance("Серверный кластер"))
print(tech_mgr.manage_project("Миграция в облако"))
print(tech_mgr.perform_maintenance("CI/CD пайплайн"))

tech_mgr.add_employee(emp)
tech_mgr.add_employee(mgr)
tech_mgr.add_employee(tech)

tech_mgr.team_info()
