class SchoolMember(object):
    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex
        self.enroll()

    def enroll(self):
        print("SchoolMember [%s] is enrolled!" % self.name)



class Teacher(SchoolMember):
    def __init__(self, name, age, sex, course, salary):
        super(Teacher, self).__init__(name, age, sex)
        #SchoolMember.__init___(self, name, age, sex)

    def teaching(self):
        print("Teacher [%s] is teaching [%s]" % (self.name, self.course))


class Student(SchoolMember):
    def __init__(self, name, age, sex, course, tuition):
        super(Student, self).__init__(name, age, sex)
        self.course = course
        self.tuition = tuition

    def pay_tuition(self):
        print("Student [%s] is paying tuition." % (self.name))

    def tell(self):
        print("My name is [%s]" % self.name)
