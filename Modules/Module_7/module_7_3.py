class WordsFinder:

    def __init__(self, *files):
        self.file_names = files
        for file_name in files:
            file = open(file_name, encoding='utf-8')
            file.close()

    def get_all_words(self):
        all_words = {}
        for file_name in self.file_names:
            with (open(file_name, encoding='utf-8') as file):
                words = []
                for line in file:
                    cleaned_line = line.lower().replace(',', '').replace('.', '').replace('=', '').replace('!', ''
                                ).replace('?', '').replace(';', '').replace(':', '').replace(' - ', '')
                    words += cleaned_line.split()
                all_words[file_name] = words
        return all_words

    def find(self, word):
        result = {}
        all_words = self.get_all_words()
        for file_name, words in all_words.items():
                index = words.index(word.lower())
                result[file_name] = index + 1
        return result

    def count(self, word):
        result = {}
        all_words = self.get_all_words()
        for file_name, words in all_words.items():
            count = words.count(word.lower())
            result[file_name] = count
        return result

finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words())
print(finder2.find('TEXT'))
print(finder2.count('teXT'))