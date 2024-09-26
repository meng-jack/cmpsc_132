# HW2
# REMINDER: The work in this assignment must be your own original work and must be completed alone.

import random
import os


class Course:
    """
    >>> c1 = Course('CMPSC132', 'Programming in Python II', 3)
    >>> c2 = Course('CMPSC360', 'Discrete Mathematics', 3)
    >>> c1 == c2
    False
    >>> c3 = Course('CMPSC132', 'Programming in Python II', 3)
    >>> c1 == c3
    True
    >>> c1
    CMPSC132(3): Programming in Python II
    >>> c2
    CMPSC360(3): Discrete Mathematics
    >>> c3
    CMPSC132(3): Programming in Python II
    >>> c1 == None
    False
    >>> print(c1)
    CMPSC132(3): Programming in Python II
    """

    def __init__(self, cid, cname, credits):
        self.cid: str = cid
        self.cname: str = cname
        self.credits: int = credits

    def __str__(self):
        return f"{self.cid}({self.credits}): {self.cname}"

    __repr__ = __str__

    def __eq__(self, other):
        return isinstance(other, Course) and other.cid == self.cid


class Catalog:
    """
    >>> C = Catalog()
    >>> C.courseOfferings
    {}
    >>> C._loadCatalog("cmpsc_catalog_small.csv")
    >>> C.courseOfferings
    {'CMPSC 132': CMPSC 132(3): Programming and Computation II, 'MATH 230': MATH 230(4): Calculus and Vector Analysis, 'PHYS 213': PHYS 213(2): General Physics, 'CMPEN 270': CMPEN 270(4): Digital Design, 'CMPSC 311': CMPSC 311(3): Introduction to Systems Programming, 'CMPSC 360': CMPSC 360(3): Discrete Mathematics for Computer Science}
    >>> C.removeCourse('CMPSC 360')
    'Course removed successfully'
    >>> C.courseOfferings
    {'CMPSC 132': CMPSC 132(3): Programming and Computation II, 'MATH 230': MATH 230(4): Calculus and Vector Analysis, 'PHYS 213': PHYS 213(2): General Physics, 'CMPEN 270': CMPEN 270(4): Digital Design, 'CMPSC 311': CMPSC 311(3): Introduction to Systems Programming}
    >>> isinstance(C.courseOfferings['CMPSC 132'], Course)
    True
    """

    def __init__(self):
        self.courseOfferings: dict[str, Course] = {}

    def addCourse(self, cid, cname, credits):
        if cid in self.courseOfferings:
            return "Course already added"
        self.courseOfferings[cid] = Course(cid, cname, credits)
        return "Course added successfully"

    def removeCourse(self, cid):
        if cid in self.courseOfferings:
            del self.courseOfferings[cid]
            return "Course removed successfully"
        return "Course not found"

    def _loadCatalog(self, file):
        target_path = os.path.join(os.path.dirname(__file__), file)
        with open(target_path, "r") as f:
            course_info = f.readlines()
        for course in course_info:
            course = course.split(",")
            self.addCourse(course[0], course[1], course[2].replace("\n", ""))


class Semester:
    """
    >>> cmpsc131 = Course('CMPSC 131', 'Programming in Python I', 3)
    >>> cmpsc132 = Course('CMPSC 132', 'Programming in Python II', 3)
    >>> math230 = Course("MATH 230", 'Calculus', 4)
    >>> phys213 = Course("PHYS 213", 'General Physics', 2)
    >>> econ102 = Course("ECON 102", 'Intro to Economics', 3)
    >>> phil119 = Course("PHIL 119", 'Ethical Leadership', 3)
    >>> spr22 = Semester()
    >>> spr22
    No courses
    >>> spr22.addCourse(cmpsc132)
    >>> isinstance(spr22.courses['CMPSC 132'], Course)
    True
    >>> spr22.addCourse(math230)
    >>> spr22
    CMPSC 132; MATH 230
    >>> spr22.isFullTime
    False
    >>> spr22.totalCredits
    7
    >>> spr22.addCourse(phys213)
    >>> spr22.addCourse(econ102)
    >>> spr22.addCourse(econ102)
    'Course already added'
    >>> spr22.addCourse(phil119)
    >>> spr22.isFullTime
    True
    >>> spr22.dropCourse(phil119)
    >>> spr22.addCourse(Course("JAPNS 001", 'Japanese I', 4))
    >>> spr22.totalCredits
    16
    >>> spr22.dropCourse(cmpsc131)
    'No such course'
    >>> spr22.courses
    {'CMPSC 132': CMPSC 132(3): Programming in Python II, 'MATH 230': MATH 230(4): Calculus, 'PHYS 213': PHYS 213(2): General Physics, 'ECON 102': ECON 102(3): Intro to Economics, 'JAPNS 001': JAPNS 001(4): Japanese I}
    """

    def __init__(self):
        self.courses: dict[str, Course] = {}

    def __str__(self):
        return (
            "; ".join(self.courses.keys())
            if len(self.courses.keys()) > 0
            else "No courses"
        )

    __repr__ = __str__

    def addCourse(self, course: Course) -> None | str:
        if course.cid not in self.courses:
            self.courses[course.cid] = course
        else:
            return "Course already added"

    def dropCourse(self, course) -> None | str:
        if course.cid in self.courses:
            del self.courses[course.cid]
        else:
            return "No such course"

    @property
    def totalCredits(self):
        t = 0
        for cid in self.courses:
            t += int(self.courses[cid].credits)
        return t

    @property
    def isFullTime(self):
        return self.totalCredits >= 12


class Loan:
    """
    >>> import random
    >>> random.seed(2)  # Setting seed to a fixed value, so you can predict what numbers the random module will generate
    >>> first_loan = Loan(4000)
    >>> first_loan
    Balance: $4000
    >>> first_loan.loan_id
    17412
    >>> second_loan = Loan(6000)
    >>> second_loan.amount
    6000
    >>> second_loan.loan_id
    22004
    >>> third_loan = Loan(1000)
    >>> third_loan.loan_id
    21124
    """

    def __init__(self, amount):
        self.loan_id = self.__getloanID
        self.amount = amount

    def __str__(self):
        return f"Balance: ${self.amount}"

    __repr__ = __str__

    @property
    def __getloanID(self):
        return random.randrange(10000, 99999)


class Person:
    """
    >>> p1 = Person('Jason Lee', '204-99-2890')
    >>> p2 = Person('Karen Lee', '247-01-2670')
    >>> p1
    Person(Jason Lee, ***-**-2890)
    >>> p2
    Person(Karen Lee, ***-**-2670)
    >>> p3 = Person('Karen Smith', '247-01-2670')
    >>> p3
    Person(Karen Smith, ***-**-2670)
    >>> p2 == p3
    True
    >>> p1 == p2
    False
    """

    def __init__(self, name, ssn):
        self.name = name
        self.ssn = ssn

    def __str__(self):
        return f"Person({self.name}, ***-**-{self.ssn[-4:]})"

    __repr__ = __str__

    def get_ssn(self) -> str:
        return self.ssn

    def __eq__(self, other):
        return isinstance(other, Person) and other.get_ssn() == self.ssn


class Staff(Person):
    """
    >>> C = Catalog()
    >>> C._loadCatalog("cmpsc_catalog_small.csv")
    >>> s1 = Staff('Jane Doe', '214-49-2890')
    >>> s1.getSupervisor
    >>> s2 = Staff('John Doe', '614-49-6590', s1)
    >>> s2.getSupervisor
    Staff(Jane Doe, 905jd2890)
    >>> s1 == s2
    False
    >>> s2.id
    '905jd6590'
    >>> p = Person('Jason Smith', '221-11-2629')
    >>> st1 = s1.createStudent(p)
    >>> isinstance(st1, Student)
    True
    >>> s2.applyHold(st1)
    'Completed!'
    >>> st1.registerSemester()
    'Unsuccessful operation'
    >>> s2.removeHold(st1)
    'Completed!'
    >>> st1.registerSemester()
    >>> st1.enrollCourse('CMPSC 132', C)
    'Course added successfully'
    >>> st1.semesters
    {1: CMPSC 132}
    >>> s1.applyHold(st1)
    'Completed!'
    >>> st1.enrollCourse('CMPSC 360', C)
    'Unsuccessful operation'
    >>> st1.semesters
    {1: CMPSC 132}
    """

    def __init__(self, name, ssn, supervisor=None):
        super().__init__(name, ssn)
        self.supervisor = supervisor

    def __str__(self):
        return f"Staff({self.name}, {self.id})"

    __repr__ = __str__

    @property
    def id(self):
        return f"905{''.join([initial[0].lower() for initial in self.name.split(' ') if initial])}{self.get_ssn()[-4:]}"

    @property
    def getSupervisor(self):
        return self.supervisor

    def setSupervisor(self, new_supervisor) -> None | str:
        if isinstance(new_supervisor, Staff):
            self.supervisor = new_supervisor
            return "Completed!"

    def applyHold(self, student) -> None | str:
        if isinstance(student, Student):
            student.hold = True
            return "Completed!"

    def removeHold(self, student) -> None | str:
        if isinstance(student, Student):
            student.hold = False
            return "Completed!"

    def unenrollStudent(self, student) -> None | str:
        if isinstance(student, Student):
            student.active = False
            return "Completed!"

    def createStudent(self, person: Person):
        return Student(person.name, person.ssn, "Freshman")


class StudentAccount:
    """
    >>> C = Catalog()
    >>> C._loadCatalog("cmpsc_catalog_small.csv")
    >>> s1 = Student('Jason Lee', '204-99-2890', 'Freshman')
    >>> s1.registerSemester()
    >>> s1.enrollCourse('CMPSC 132', C)
    'Course added successfully'
    >>> s1.account.balance
    3000
    >>> s1.enrollCourse('CMPSC 360', C)
    'Course added successfully'
    >>> s1.account.balance
    6000
    >>> s1.enrollCourse('MATH 230', C)
    'Course added successfully'
    >>> s1.enrollCourse('PHYS 213', C)
    'Course added successfully'
    >>> print(s1.account)
    Name: Jason Lee
    ID: jl2890
    Balance: $12000
    >>> s1.account.chargeAccount(100)
    12100
    >>> s1.account.balance
    12100
    >>> s1.account.makePayment(200)
    11900
    >>> s1.getLoan(4000)
    >>> s1.account.balance
    7900
    >>> s1.getLoan(8000)
    >>> s1.account.balance
    -100
    >>> s1.enrollCourse('CMPEN 270', C)
    'Course added successfully'
    >>> s1.account.balance
    3900
    >>> s1.dropCourse('CMPEN 270')
    'Course dropped successfully'
    >>> s1.account.balance
    1900.0
    >>> s1.account.loans
    {27611: Balance: $4000, 84606: Balance: $8000}
    >>> StudentAccount.CREDIT_PRICE = 1500
    >>> s2 = Student('Thomas Wang', '123-45-6789', 'Freshman')
    >>> s2.registerSemester()
    >>> s2.enrollCourse('CMPSC 132', C)
    'Course added successfully'
    >>> s2.account.balance
    4500
    >>> s1.enrollCourse('CMPEN 270', C)
    'Course added successfully'
    >>> s1.account.balance
    7900.0
    """

    CREDIT_PRICE: int = 1000

    def __init__(self, student):
        self.student = student
        self.balance: int = 0
        self.loans: dict[int, Loan] = {}

    def __str__(self):
        return f"Name: {self.student.name}\nID: {self.student.id}\nBalance: ${self.balance}"

    __repr__ = __str__

    def makePayment(self, amount):
        self.balance -= amount
        return self.balance

    def chargeAccount(self, amount: int):
        self.balance += amount
        return self.balance


class Student(Person):
    """
    >>> C = Catalog()
    >>> C._loadCatalog("cmpsc_catalog_small.csv")
    >>> s1 = Student('Jason Lee', '204-99-2890', 'Freshman')
    >>> s1
    Student(Jason Lee, jl2890, Freshman)
    >>> s2 = Student('Karen Lee', '247-01-2670', 'Freshman')
    >>> s2
    Student(Karen Lee, kl2670, Freshman)
    >>> s1 == s2
    False
    >>> s1.id
    'jl2890'
    >>> s2.id
    'kl2670'
    >>> s1.registerSemester()
    >>> s1.enrollCourse('CMPSC 132', C)
    'Course added successfully'
    >>> s1.semesters
    {1: CMPSC 132}
    >>> s1.enrollCourse('CMPSC 360', C)
    'Course added successfully'
    >>> s1.enrollCourse('CMPSC 465', C)
    'Course not found'
    >>> s1.semesters
    {1: CMPSC 132; CMPSC 360}
    >>> s2.semesters
    {}
    >>> s1.enrollCourse('CMPSC 132', C)
    'Course already enrolled'
    >>> s1.dropCourse('CMPSC 360')
    'Course dropped successfully'
    >>> s1.dropCourse('CMPSC 360')
    'Course not found'
    >>> s1.semesters
    {1: CMPSC 132}
    >>> s1.registerSemester()
    >>> s1.semesters
    {1: CMPSC 132, 2: No courses}
    >>> s1.enrollCourse('CMPSC 360', C)
    'Course added successfully'
    >>> s1.semesters
    {1: CMPSC 132, 2: CMPSC 360}
    >>> s1.registerSemester()
    >>> s1.semesters
    {1: CMPSC 132, 2: CMPSC 360, 3: No courses}
    >>> s1
    Student(Jason Lee, jl2890, Sophomore)
    >>> s1.classCode
    'Sophomore'
    """

    def __init__(self, name: str, ssn: str, year: str):
        random.seed(1)
        super().__init__(name, ssn)
        self.classCode = year
        self.hold = False
        self.active = True
        self.semesters: dict[int, Semester] = {}
        self.account = self.__createStudentAccount()

    def __str__(self):
        return f"Student({self.name}, {self.id}, {self.classCode})"

    __repr__ = __str__

    def __createStudentAccount(self) -> None | StudentAccount:
        if self.active:
            return StudentAccount(self)

    @property
    def id(self):
        return f"{''.join([initial[0].lower() for initial in self.name.split(' ') if initial])}{self.get_ssn()[-4:]}"

    def registerSemester(self) -> None | str:
        if self.hold or not self.active:
            return "Unsuccessful operation"
        semester = len(self.semesters) + 1
        self.semesters[semester] = Semester()
        self.classCode = (
            "Freshman"
            if semester <= 2
            else (
                "Sophomore"
                if semester > 2 and semester < 5
                else "Junior" if semester > 4 and semester < 7 else "Senior"
            )
        )

    def enrollCourse(self, cid, catalog: Catalog):
        if self.hold or not self.active:
            return "Unsuccessful operation"
        if cid in catalog.courseOfferings:
            curr = max(self.semesters.keys())
            if cid in self.semesters[curr].courses:
                return "Course already enrolled"
            else:
                self.semesters[curr].addCourse(catalog.courseOfferings[cid])
                if not self.account == None:
                    self.account.chargeAccount(
                        StudentAccount.CREDIT_PRICE
                        * int(catalog.courseOfferings[cid].credits)
                    )
                return "Course added successfully"
        else:
            return "Course not found"

    def dropCourse(self, cid):
        if self.hold or not self.active:
            return "Unsuccessful operation"
        curr = max(self.semesters.keys())
        if cid in self.semesters[curr].courses:
            if not self.account == None:
                self.account.makePayment(
                    StudentAccount.CREDIT_PRICE * int(self.semesters[curr].courses[cid].credits) / 2)
            self.semesters[curr].dropCourse(self.semesters[curr].courses[cid])
            return "Course dropped successfully"
        return "Course not found"

    def getLoan(self, amount) -> None | str:
        if not self.active:
            return "Unsuccessful operation"
        curr = max(self.semesters.keys())
        if not self.semesters[curr].isFullTime:
            return "Not full-time"
        loan = Loan(amount)
        if not self.account == None:
            self.account.loans[loan.loan_id] = loan
            self.account.makePayment(amount)


def run_tests():
    import doctest

    # Run tests in all docstrings
    # doctest.testmod(verbose=True)

    # Run tests per function - Uncomment the next line to run doctest by function. Replace Course with the name of the function you want to test
    #doctest.run_docstring_examples(
    #    StudentAccount, globals(), name="HW2", verbose=True)


if __name__ == "__main__":
    run_tests()
