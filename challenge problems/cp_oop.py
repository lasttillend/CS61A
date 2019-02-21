# OOP

# 1 Defining a Class

# (a)
class Student:
    students_enrolled = 0
    student_years = {}
    how_popular = {}  # name: number of crushes on him/her

    def __init__(self, name, grade):
        self.name = name
        self.grade = grade
        self.fave_subject = "No favorite"
        self.crush = None
        Student.how_popular[name] = 0
        Student.students_enrolled += 1
        if grade in Student.student_years:
            Student.student_years[grade] += 1
        else:
            Student.student_years[grade] = 1

    def set_favorite_subject(self, subject):
        self.fave_subject = subject

    def students_in_grade(grade):
        return Student.student_years.get(grade, 0)

    def develop_crush(self, crush):
        self.crush = crush
        Student.how_popular[crush] += 1

    def crush_on(student):
        if student not in Student.how_popular:
            return "This student does not exist."
        return Student.how_popular[student]


print("1 Defining a Class")
print("Problem(a):")
tiffany = Student("Tiffany", 9)  # a student by default has no favorite subject
print(tiffany.name)
print(tiffany.grade)
mike = Student("Michael", 11)
mike.set_favorite_subject("Biology")
print(mike.fave_subject)
print(tiffany.fave_subject)
print(Student.students_in_grade(9))
print(Student.students_in_grade(10))
zack = Student("Zackary", 11)
print(Student.students_in_grade(11))
print(Student.students_enrolled)

# (b)
print("Problem(b):")
print(mike.students_enrolled)

# (c)
print("Problem(c):")
print(Student.student_years[9])

# (d)
print("Problem(d):")
mary = Student("Mary", 9)
amy = Student("Amy", 10)

tiffany.develop_crush("Mary")
mary.develop_crush("Zackary")
zack.develop_crush("Mary")
amy.develop_crush("Tiffany")
mike.develop_crush("Amy")

print(tiffany.crush)

# (e)
print("Problem(e):")
print(Student.how_popular)

# (f)
print("Problem(f):")
print(Student.crush_on("Mary"))

# 2 Special Method

class Molecule:
    def __init__(self, formula, name, weight):
        self.formula = formula
        self.name = name
        self.weight = weight

    def __eq__(self, other):
        return self.name == other.name

    def __lt__(self, other):
        return self.weight < other.weight

    def __gt__(self, other):
        return self.weight > other.weight

    def __str__(self):
        return self.formula + ": " + self.name

    def __repr__(self):
        return "Molecule('{0}', '{1}', '{2}')".format(self.formula, self.name, self.weight)


# (a)
print("2 Special Method")
print("Problem(a):")
ethanol = Molecule("C2H6O", "Ethanol", 46.07)
alcohol = Molecule("C2H6O", "Ethanol", 46.07)
dimethyl_ether = Molecule("C2H6O", "Dimenthyl Ether", 46.07)
print(ethanol == alcohol)
print(ethanol == dimethyl_ether)

# (b)
print("Problem(b):")
ammonia = Molecule("NH3", 'Ammonia', 17.03)
print(ammonia < ethanol)
print(ammonia > dimethyl_ether)

# (c)
print("Problem(c):")

# (d)
print(ammonia)
ethanol
str(alcohol)
repr(ammonia)
eval(repr(ethanol))  # eval evaluates a string as native Python
print(repr(ethanol))



