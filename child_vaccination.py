import datetime

# Sample data storage (for simplicity, using dictionaries)
users = {}
children = {}

def register_user():
    username = input("enter username: ")
    password = input("enter password: ")
    if username in users:
        print("username already exists.")
    else:
        users[username] = password
        print("registration successful!")

def login_user():
    username = input("enter username: ")
    password = input("enter password: ")
    if username in users and users[username] == password:
        print("login successful!")
        return username
    else:
        print("invalid credentials.")
        return None

def add_child(username):
    child_name = input("enter child's name: ")
    dob = input("enter child's date of birth (yyyy-mm-dd): ")
    children[child_name] = {
        'dob': dob,
        'vaccinations': [],
        'appointments': []
    }
    print("child added successfully!")

def view_children():
    for child_name, info in children.items():
        print(f"name: {child_name}, date of birth: {info['dob']}")
        print("vaccinations:", info['vaccinations'])
        print("appointments:", info['appointments'])

def schedule_appointment():
    child_name = input("enter child's name: ")
    if child_name in children:
        date = input("enter appointment date (yyyy-mm-dd): ")
        children[child_name]['appointments'].append(date)
        print("appointment scheduled!")
    else:
        print("child not found.")

def view_reminders():
    today = datetime.date.today()
    for child_name, info in children.items():
        for appointment in info['appointments']:
            appointment_date = datetime.datetime.strptime(appointment, "%Y-%m-%d").date()
            if appointment_date == today:
                print(f"reminder: {child_name} has an appointment today!")

def main():
    username = None
    while True:
        print("\n1. register")
        print("2. login")
        print("3. add child")
        print("4. view children")
        print("5. schedule appointment")
        print("6. view reminders")
        print("7. exit")
        
        choice = input("enter choice: ")
        
        if choice == '1':
            register_user()
        elif choice == '2':
            username = login_user()
        elif choice == '3':
            if username:
                add_child(username)
            else:
                print("you need to log in first.")
        elif choice == '4':
            view_children()
        elif choice == '5':
            if username:
                schedule_appointment()
            else:
                print("you need to log in first.")
        elif choice == '6':
            view_reminders()
        elif choice == '7':
            break
        else:
            print("invalid choice, please try again.")

if __name__ == "__main__":
    main()
