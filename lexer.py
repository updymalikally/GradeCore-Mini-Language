class GradeCoreLexer:

    keywords = {
        'ADD', 'SET', 'SHOW', 'CHECK',
        'STUDENT', 'MARK', 'RESULT'
    }

    delimiters = {';'}

    def __init__(self, source):
        self.source = source

    def tokenize(self):
        tokens = []

        words = self.source.replace(';', ' ;').split()

        for word in words:

            upper = word.upper()

            if upper in self.keywords:
                tokens.append((upper, None))

            elif word == ';':
                tokens.append(('DELIMITER', ';'))

            elif word.isdigit():
                tokens.append(('INTEGER', int(word)))

            else:
                tokens.append(('IDENTIFIER', word))

        return tokens


source = "ADD STUDENT John;"

lexer = GradeCoreLexer(source)

print(lexer.tokenize())