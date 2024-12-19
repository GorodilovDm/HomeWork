class WordsFinder:
    def __init__(self, *file_names):
        self.file_names = file_names

    def get_all_words(self):
        all_words = {}
        znaki = [',', '.', '=', '!', '?', ';', ':', ' - ']
        for file in self.file_names:
            with open(file, encoding='utf-8') as file_:
                string = file_.read().lower()
                string = ''.join(char for char in string if char not in znaki)
                all_words[file] = string.split()
        return all_words

    def find(self, word):
        first_word = {}
        for name, words in self.get_all_words().items():
            if word.lower() in words:
                first_word[name] = words.index(word.lower()) + 1
        return first_word

    def count(self, word):
        count_word = {}
        for name, words in self.get_all_words().items():
            if word.lower() in words:
                count_word[name] = words.count(word.lower())
        return count_word


finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words())
print(finder2.find('TEXT'))
print(finder2.count('teXT'))