class Employee:
    def __init__(self, name, emp_id):
        self.name = name
        self.id = emp_id

    def get_info(self):
        return f"Сотрудник: {self.name}, ID: {self.id}"


class Manager(Employee):
    def __init__(self, name, emp_id, department):
        Employee.__init__(self, name, emp_id)
        self.department = department

    def manage_project(self, project_name):
        return f"{self.name} управляет проектом: {project_name} (отдел: {self.department})"

    def get_info(self):
        return f"{Employee.get_info(self)}, Отдел: {self.department}"


class Technician(Employee):
    def __init__(self, name, emp_id, specialization):
        Employee.__init__(self, name, emp_id)
        self.specialization = specialization

    def perform_maintenance(self, equipment):
        return f"{self.name} выполняет обслуживание: {equipment} (специализация: {self.specialization})"

    def get_info(self):
        return f"{Employee.get_info(self)}, Специализация: {self.specialization}"


class TechManager(Manager, Technician):
    def __init__(self, name, emp_id, department, specialization):
        Employee.__init__(self, name, emp_id)
        self.department = department
        self.specialization = specialization
        self.team = []

    def add_employee(self, employee):
        self.team.append(employee)

    def get_team_info(self):
        if not self.team:
            return "Подчинённых нет."
        result = ["Подчинённые:"]
        for i, emp in enumerate(self.team, 1):
            result.append(f"{i}. {emp.get_info()}")
        return "\n".join(result)

    def manage_project(self, project_name):
        return f"{self.name} управляет проектом: {project_name} (отдел: {self.department})"

    def perform_maintenance(self, equipment):
        return f"{self.name} выполняет обслуживание: {equipment} (специализация: {self.specialization})"

    def get_info(self):
        return f"{Employee.get_info(self)}, Отдел: {self.department}, Специализация: {self.specialization}"


employee = Employee("Иван Петров", 101)
manager = Manager("Анна Смирнова", 102, "Разработка")
technician = Technician("Олег Кузнецов", 103, "Сети")
tech_manager = TechManager("Мария Волкова", 104, "ИТ", "Серверы")

print(employee.get_info())
print(manager.get_info())
print(manager.manage_project("CRM система"))
print(technician.get_info())
print(technician.perform_maintenance("Маршрутизатор"))

print(tech_manager.get_info())
print(tech_manager.manage_project("Миграция в облако"))
print(tech_manager.perform_maintenance("Серверная стойка"))

tech_manager.add_employee(employee)
tech_manager.add_employee(manager)
tech_manager.add_employee(technician)

print(tech_manager.get_team_info())

