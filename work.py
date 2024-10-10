from collections import deque

# Global variables
available_instructors = []  # List to manage available instructors
lesson_stack = []           # Stack to undo lesson bookings
class_queue = deque()       # Queue to schedule music classes

# Function to add an instructor
def add_instructor(instructor_name):
    """Add an instructor to the list of available instructors."""
    available_instructors.append(instructor_name)
    print(f"Instructor {instructor_name} added.")

# Function to remove an instructor
def remove_instructor(instructor_name):
    """Remove an instructor from the list of available instructors."""
    if instructor_name in available_instructors:
        available_instructors.remove(instructor_name)
        print(f"Instructor {instructor_name} removed.")
    else:
        print(f"Instructor {instructor_name} not found.")

# Function to book a lesson
def book_lesson(instructor_name, student_name):
    """Book a lesson with an instructor and store it in the stack to allow undo."""
    if instructor_name in available_instructors:
        lesson = f"Lesson booked with {instructor_name} for {student_name}"
        lesson_stack.append(lesson)
        print(lesson)
    else:
        print(f"Instructor {instructor_name} is not available.")

# Function to undo the last lesson booking
def undo_booking():
    """Undo the last lesson booking."""
    if lesson_stack:
        last_booking = lesson_stack.pop()
        print(f"Undoing: {last_booking}")
    else:
        print("No bookings to undo.")

# Function to schedule a music class
def schedule_class(class_name):
    """Schedule a music class by adding it to the queue."""
    class_queue.append(class_name)
    print(f"Class '{class_name}' scheduled.")

# Function to start the next scheduled class
def start_next_class():
    """Start the next scheduled music class."""
    if class_queue:
        next_class = class_queue.popleft()
        print(f"Starting class: {next_class}")
    else:
        print("No classes scheduled.")

# Function to display the list of available instructors
def display_instructors():
    """Display the list of available instructors."""
    if available_instructors:
        print("Available Instructors:")
        for instructor in available_instructors:
            print(f"- {instructor}")
    else:
        print("No instructors available.")

# Function to display the list of upcoming scheduled classes
def display_upcoming_classes():
    """Display the list of upcoming scheduled classes."""
    if class_queue:
        print("Upcoming Classes:")
        for music_class in class_queue:
            print(f"- {music_class}")
    else:
        print("No classes scheduled.")

# Function to display all booked lessons
def display_bookings():
    """Display the list of all bookings."""
    if lesson_stack:
        print("Booked Lessons:")
        for lesson in lesson_stack:
            print(f"- {lesson}")
    else:
        print("No lessons booked.")

# Example usage of the functions
if __name__ == "__main__":
    # Add some instructors
    add_instructor("John")
    add_instructor("Sarah")
    add_instructor("Emma")

    # Display available instructors
    display_instructors()

    # Book some lessons
    book_lesson("John", "Alice")
    book_lesson("Sarah", "Bob")

    # Display bookings
    display_bookings()

    # Undo the last booking
    undo_booking()

    # Schedule some music classes
    schedule_class("Guitar 101")
    schedule_class("Piano Basics")
    schedule_class("Singing Techniques")

    # Display upcoming classes
    display_upcoming_classes()

    # Start the next class
    start_next_class()

    # Remove an instructor
    remove_instructor("Emma")

    # Display updated list of instructors
    display_instructors()

    # Display remaining bookings
    display_bookings()

    # Start remaining classes
    start_next_class()
    start_next_class()
    start_next_class()
