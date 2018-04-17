class Person(object):
    def __init__(self, name, age, work):
        self.name = name
        self.age = age
        self.work = work

    def work_self(self):
        print("%s goes back to work." % self.name)

    def name_self(self):
        print("%s went to work." % self.name)


class Employee(Person):
    def __init__(self, name, age, work, job):
        super(Employee, self).__init__(name, age, work)
        self.job = job


worker = Employee("PLAYER", 15, "Programmer", "Programming")
worker.work_self()
worker.name_self()


class Programmer(Employee):
    def __init__(self, name, age, work, job):
        super(Programmer, self).__init__(name, age, work, job)

    def age_self(self):
        print("You're %d years old." % self.age)

    def job_self(self):
        print("You're job is %s and you are a" % self.job, self.work)


student = Programmer("Player", 15, "Programmer", "Programming")
student.age_self()
student.job_self()
