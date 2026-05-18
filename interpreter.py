class GradeCoreInterpreter:

    def __init__(self):
        # Store students and their marks
        self.students = {}

    def execute(self, code):

        # Split program using semicolon
        statements = code.split(';')

        # Loop through each statement
        for stmt in statements:

            stmt = stmt.strip()

            # Skip empty statements
            if not stmt:
                continue

            # Split statement into words
            parts = stmt.split()

            # ADD STUDENT John
            if parts[0].upper() == "ADD" and parts[1].upper() == "STUDENT":

                name = parts[2]

                self.students[name] = None

                print(f"Student {name} added.")

            # SET MARK John 85
            elif parts[0].upper() == "SET" and parts[1].upper() == "MARK":

                name = parts[2]
                mark = int(parts[3])

                if name in self.students:

                    self.students[name] = mark

                    print(f"Mark {mark} set for {name}.")

                else:
                    print(f"Student {name} not found.")

            # SHOW STUDENTS
            elif parts[0].upper() == "SHOW" and parts[1].upper() == "STUDENTS":

                print("Students List:")

                for name, mark in self.students.items():

                    print(f"{name} -> {mark}")

            # CHECK RESULT John
            elif parts[0].upper() == "CHECK" and parts[1].upper() == "RESULT":

                name = parts[2]

                if name in self.students:

                    mark = self.students[name]

                    if mark is None:

                        print(f"{name} has no mark yet.")

                    elif mark >= 50:

                        print(f"{name} PASSED with {mark}")

                    else:

                        print(f"{name} FAILED with {mark}")

                else:
                    print(f"Student {name} not found.")

            # INVALID COMMAND
            else:

                print("Invalid command:", stmt)


# TEST PROGRAM
if __name__ == "__main__":

    program = """
    ADD STUDENT John;
    ADD STUDENT Ali;
    SET MARK John 85;
    SET MARK Ali 40;
    SHOW STUDENTS;
    CHECK RESULT John;
    CHECK RESULT Ali;
    """

    interpreter = GradeCoreInterpreter()

    interpreter.execute(program)