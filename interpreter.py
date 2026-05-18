class GradeCoreInterpreter:

    def __init__(self):
        self.students = {}

    def execute(self, code):

        statements = code.split(';')

        for stmt in statements:

            stmt = stmt.strip()

            if not stmt:
                continue

            parts = stmt.split()

            # ADD STUDENT
            if parts[0].upper() == "ADD" and parts[1].upper() == "STUDENT":

                name = parts[2]

                self.students[name] = None

                print(f"Student {name} added.")


program = """
ADD STUDENT John;
"""

interpreter = GradeCoreInterpreter()

interpreter.execute(program)