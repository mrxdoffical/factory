from classes import Employee, session
from cmd import Cmd
import subprocess
class EmployeeCLI(Cmd):
    prompt = 'bero/\n> '
    
    def do_add(self, args):
        """add new Employee. usage: add firstname lastname age pay [email]"""
        try:
            args = args.split()
            firstname, lastname, age, pay = args[:4]
            email = args[4] if len(args) > 4 else None
            age = int(age)
            pay = int(pay)
            emp = Employee(firstname=firstname, lastname=lastname, age=age, pay=pay, email=email)
            session.add(emp)
            session.commit()
            print(f"added employee {emp}")
        except Exception as e:
            print(f"error adding employee {emp}")

    def do_list(self, args):
        """List all employ. Usage: list"""
        employees = session.query(Employee).all()
        if employees:
            for emp in employees:
                print(emp)
        else:
            print("no employee have been added yet")

    def do_search(self, args):
        """search for employee by firstname. Usage: search [firstname]"""
        firstname = args.strip()
        emp = session.query(Employee).filter(Employee.firstname == firstname).first()
        if emp:
            print(f"Employee found:\n{emp}")
        else:
            print(f"no Employee found with this firstname {firstname}")

    def do_clear(self, args):
        """excute clear command. Usage: clear"""
        try:
                result = subprocess.run('clear', shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
                print(result.stdout)
        except subprocess.CalledProcessError as e:
                print(f"Error executing command: {e.stderr}")
    
    def do_user_id(self, args):
        """get's user id by email. usage: user_id [email]"""
        if args:
                email = args.strip()
                user = session.query(Employee).filter(Employee.email == email).first()
                if user:
                    print(f"user with email: {email}\nid = {user.id}")
                else:
                    print(f"no user found with this email: {user.email}")

    def do_delete(self, args):
        """deletes user by email. Usage: delete [email]"""
        if args:
            email = args.strip()
            user = session.query(Employee).filter(Employee.email == email).first()
            if user:
                choice = input(f"user {user.firstname} found.\nare you sure you want to delete it\ny/n?")
                if choice == 'y' or choice == 'Y':
                    session.delete(user)
            else:
                print(f"user with this email: {user.email}\n not found")

    def do_exit(self, args):
        """EXIT the CLI."""
        print("Exiting...")
        return True

if __name__ == "__main__":
    EmployeeCLI().cmdloop()