from classes import Employee, session
import subprocess
# Create a new Employee instance without specifying the email


def do_add(self, args):
        """Add a new employee. Usage: add firstname lastname age pay [email]"""
        try:
            args = args.split()
            firstname, lastname, age, pay = args[:4]
            email = args[4] if len(args) > 4 else None
            age = int(age)
            pay = int(pay)
            emp = Employee(firstname=firstname, lastname=lastname, age=age, pay=pay, email=email)
            session.add(emp)
            session.commit()
            print(f"Added employee: {emp}")
        except Exception as e:
            print(f"Error adding employee: {e}")

def do_list(self, args):
        """List all employees."""
        employees = session.query(Employee).all()
        if employees:
            for emp in employees:
                print(emp)
        else:
            print("No users found")

def do_search(self, args):
        """Search for an employee by firstname. Usage: search firstname"""
        firstname = args.strip()
        emp = session.query(Employee).filter(Employee.firstname == firstname).first()
        if emp:
            print(f"Employee found: {emp}")
        else:
            print(f"No employee found with firstname {firstname}")

def do_command(self, args):
        """Execute a shell command. Usage: command <shell_command>"""
        if args:
            try:
                result = subprocess.run(args, shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
                print(result.stdout)
            except subprocess.CalledProcessError as e:
                print(f"Error executing command: {e.stderr}")

def do_user_id(self, args):
        """Get user ID by email. Usage: user_id [email]"""
        if args:
            email = args.strip()
            user = session.query(Employee).filter(Employee.email == email).first()
            if user:
                print(f"User with email: {email}\nID = {user.id}")
            else:
                print(f"No user found with this email: {email}")

def do_delete(self, args):
        """Delete user by email. Usage: delete [email]"""
        if args:
            email = args.strip()  # Extract the email string
            user = session.query(Employee).filter(Employee.email == email).first()
            if user:
                choice = input(f"User {user.firstname} found.\nAre you sure you want to delete it? (y/n): ")
                if choice.lower() == 'y':
                    session.delete(user)
                    session.commit()  # Commit the transaction to delete the user
                    print(f"User {user.firstname} deleted.")
                else:
                    print("Deletion cancelled.")
            else:
                print(f"No user found with this email: {email}")
