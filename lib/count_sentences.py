class MyString:
    def __init__(self, value=''):
        if not isinstance(value, str):
            print("The value must be a string.")
        self.value = value

    def is_sentence(self):
        return self.value.endswith('.')

    def is_question(self):
        return self.value.endswith('?')

    def is_exclamation(self):
        return self.value.endswith('!')

    def count_sentences(self):
        sentences = self.value.split('.')
        sentences = [s for s in sentences if s.strip()]
        return len(sentences)
