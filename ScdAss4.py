'''

Question – 1:   
Develop a class hierarchy for a university management system. Include classes for students, 
professors, and courses. Implement methods for enrolling students in courses, grading, and 
calculating GPA. Ensure proper use of the concepts of inheritance and polymorphism.  
'''
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id
        self.courses = {}

    def enroll(self, course):
        self.courses[course.course_code] = course

    def calculate_gpa(self):
        total_credits = 0
        total_grade_points = 0
        for course in self.courses.values():
            total_credits += course.credits
            total_grade_points += course.credits * course.get_grade(self.student_id)
        if total_credits == 0:
            return 0
        return total_grade_points / total_credits

class Professor(Person):
    def __init__(self, name, age, employee_id):
        super().__init__(name, age)
        self.employee_id = employee_id

class Course:
    def __init__(self, course_code, course_name, credits):
        self.course_code = course_code
        self.course_name = course_name
        self.credits = credits
        self.students = {}

    def enroll_student(self, student):
        self.students[student.student_id] = student

    def get_grade(self, student_id):
        # Implement a method to get the grade for a student
        pass

'''
Question – 2:  
You are working on a social media platform. Design a class structure for users and posts. Include 
classes for regular users and admins. Implement methods for creating posts, liking posts, and 
managing user roles. Ensure proper use of access modifiers for security.
'''

class User:
    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password
        self.posts = []

    def create_post(self, content):
        post = Post(content, self)
        self.posts.append(post)
        return post

    def like_post(self, post):
        post.add_like(self)

class Admin(User):
    def __init__(self, username, email, password):
        super().__init__(username, email, password)

    def manage_user_roles(self, user, role):
        # Implement method to manage user roles (e.g., admin, moderator, etc.)
        pass

class Post:
    def __init__(self, content, author):
        self.content = content
        self.author = author
        self.likes = []

    def add_like(self, user):
        self.likes.append(user)
