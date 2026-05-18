class GradeCoreParser:

    def __init__(self, tokens):
        self.tokens = tokens

    def parse(self):

        if self.tokens[0][0] == "ADD":
            return "Valid ADD statement"

        return "Invalid syntax"


tokens = [
    ('ADD', None),
    ('STUDENT', None),
    ('IDENTIFIER', 'John'),
    ('DELIMITER', ';')
]

parser = GradeCoreParser(tokens)

print(parser.parse())