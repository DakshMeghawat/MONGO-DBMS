class Employee():

    def __init__(self, name, tasks):
        self.name = name
        self.tasks = tasks

    def add_tasks(self, task):
        self.tasks.append(task)

        return self.tasks


bob = Employee('Bobbyhadz', ['develop', 'test'])
print(bob.tasks)  # 👉️ ['develop', 'test']

bob.add_tasks('ship')

print(bob.tasks)  # 👉️ ['develop', 'test', 'ship']