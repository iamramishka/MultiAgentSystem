class StudentRegistrationAgent:
    def __init__(self):
        self.student_data = {}

    def register_student(self):
        print("Student Registration Agent: Please enter your name and student ID.")
        name = input("Name: ")
        student_id = input("Student ID: ")
        self.student_data['name'] = name
        self.student_data['student_id'] = student_id
        print(f"Student Registration Agent: Welcome, {name} (ID: {student_id}). Proceeding to course selection.")
        return self.student_data


class CourseSelectionAgent:
    def __init__(self):
        self.courses = {
            "Data Structures": 300,
            "Algorithms": 350,
            "Machine Learning": 400
        }

    def select_courses(self):
        print("Course Selection Agent: Available courses are:")
        for i, (course, price) in enumerate(self.courses.items(), 1):
            print(f"{i}. {course} - ${price}")
        print("Please type the courses you want to register for (separate by commas).")
        selected_courses = input("Courses: ").split(",")
        selected_courses = [course.strip() for course in selected_courses]
        total_cost = sum(self.courses.get(course, 0) for course in selected_courses)
        print(f"Course Selection Agent: You have selected {', '.join(selected_courses)}. Total cost: ${total_cost}.")
        return selected_courses, total_cost


class PaymentAgent:
    def process_payment(self, total_cost):
        print("Payment Agent: Please make the payment of ${:.2f}.".format(total_cost))
        payment = float(input("Enter payment amount: "))
        if payment >= total_cost:
            print(f"Payment Agent: Payment of ${payment:.2f} successful. Registration complete!")
            return True
        else:
            print(f"Payment Agent: Payment failed. Insufficient amount.")
            return False


# Main program
if __name__ == "__main__":
    print("Student: I want to register for courses.")
    student_agent = StudentRegistrationAgent()
    course_agent = CourseSelectionAgent()
    payment_agent = PaymentAgent()

    student_info = student_agent.register_student()
    selected_courses, total_cost = course_agent.select_courses()
    payment_status = payment_agent.process_payment(total_cost)

    if payment_status:
        print(f"Student: Thank you for registering, {student_info['name']}!")
    else:
        print("Student: I will try again.")
