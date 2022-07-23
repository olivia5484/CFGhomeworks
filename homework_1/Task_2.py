class Student:

    def __init__(self, name, age, id):
        self.name = name
        self.age = age
        self.id = id
        self.subjects = dict()

# add a new subject and it's grade
    def add_subject(self, subject_and_grade):
        self.subjects.update(subject_and_grade)

# remove a subject
    def remove_subject(self, subject):
        self.subjects.pop(subject)

# view all subjects
    def view_subjects(self):
        # print(f"The subjects taken by {self.name} are: {self.subjects}")
        for key, value in self.subjects.items():
            print(key, ':', value)

# find overall (average) score
    def average_grade(self):
        total_grade = int(sum(self.subjects.values()))
        number_of_subjects = int(len(self.subjects.keys()))
        average_grade = total_grade / number_of_subjects
        return average_grade

# has the student passed the course?
    def pass_or_fail(self):
        def average_grade():
            total_grade = int(sum(self.subjects.values()))
            number_of_subjects = int(len(self.subjects.keys()))
            average = total_grade / number_of_subjects
            return average
        if average_grade() > 70:
            print("This student has passed the course.\n")
        else:
            print("This student has not passed the course. \n")


class CFGStudent(Student):

    def __init__(self, name, age, id):
        super().__init__(name, age, id)


# add a student called Jane - this is NOT a CFG student
jane = Student("Jane", 18, 1)

# add subjects for Jane
print(f"Jane's Subjects:")
jane.add_subject({'English': 70})
jane.add_subject({'Maths': 90})
jane.add_subject({'History': 85})
jane.add_subject({'Biology': 90})

# remove a subject for jane
jane.remove_subject("Maths")

# show all jane's subjects
jane.view_subjects()

# show jane's overall (average) grades
print(f"The student's overall grade is {jane.average_grade():.2f} \n")

# show whether the student has passed their course
jane.pass_or_fail()

# class CFGStudent(<should inherit from Student>)

# add a new CFG student called Olivia - on the software stream
olivia = CFGStudent("Olivia", 28, 2)

# add subjects for CFG student Olivia
print("Olivia's Subjects:")
olivia.add_subject({"SQL": 99})
olivia.add_subject({"Python": 90})
olivia.add_subject({"HTML": 84})
olivia.add_subject({"C#": 60})
olivia.add_subject({"Software specialisation": 90})

# remove subjects for CFG Student Olivia
olivia.remove_subject("C#")

# view all of CFG student Olivia's subjects
olivia.view_subjects()

# show CFG Student Olivia's overall (average) grades
print(f"The student's overall grade is {olivia.average_grade():.2f} \n")

# show whether the student has passed their course
olivia.pass_or_fail()


# class CFGStudent(<should inherit from Student>)

# add another CFG student called Cassandra - she is on the data stream
cassandra = CFGStudent("Cassandra", 28, 3)

# add subjects for CFG student Olivia
print("Cassandra's Subjects:")
cassandra.add_subject({"SQL": 60})
cassandra.add_subject({"Python": 40})
cassandra.add_subject({"HTML": 50})
cassandra.add_subject({"Data Specialisation": 30})

# remove subjects for CFG Student Cassandra
cassandra.remove_subject("HTML")

# view all of CFG student Cassandra's subjects
cassandra.view_subjects()

# show CFG Student Cassandra's overall (average) grades
print(f"The student's overall grade is {cassandra.average_grade():.2f} \n")

# show whether the student has passed their course
cassandra.pass_or_fail()