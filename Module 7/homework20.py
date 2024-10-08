class WordsFinder:
    def __init__(self, *file_names):
        self.file_names = file_names

    def get_all_words(self):
        all_words = {}
        for file_name in self.file_names:
            with open(file_name, 'r', encoding = 'utf-8'):
                for line in file_name:
                    word_list = []
                    line.lower()
                    for char in [',', '.', '=', '!', '?', ';', ':', ' - ']:
                        line = line.replace(char, ' ')
                    words = line.split()
                    word_list.extend(words)
            all_words[file_name] = word_list
    def find(self, word):
        find_dict = {}
        for file_name, words in self.all_words.items():
            if word in words:
                find_dict[file_name] = words.index(word)
        return find_dict
    def count(self, word):
        count_dict = {}
        for file_name, words in self.all_wards.items():
            count_dict[file_name] = words.count(word)
        return count_dict

finder2 = WordsFinder('test_file.txt')
print(finder2.file_names)
print(finder2.get_all_words())
print(finder2.find('TEXT'))
print(finder2.count('teXT'))