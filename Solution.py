import sys
import os
import operator
from itertools import chain

import re
from statistics import mean, median, mode


def main():
    file_path = ""
    try:
        file_path = sys.argv[1]
        list_of_words = read_file(file_path)
        evaluate(list_of_words)
    except Exception as fnf:
        print(
            ' ----No input file found along with the run command and picking file(s) from the default location---' + str(
                fnf))
        if len(file_path) == 0:
            folder_name = './Input/'
            for filename in os.listdir(folder_name):
                print('-------------------- Test begins for the file - ' + filename + '--------------------')
                file_path = folder_name + filename
                list_of_words = read_file(file_path)
                evaluate(list_of_words)
                print('-------------------- Test completed for the file - ' + filename + '--------------------' + '\n')


def read_file(f_path) -> []:
    sequence_of_words = []
    fp = None
    try:
        print(' ------ Reading the input file -------')
        if not os.path.isfile(f_path):
            print("Given file path does not exists !!!".format(f_path))
            sys.exit()

        sequence_of_words = []
        with open(f_path) as fp:
            for line in fp:
                sequence_of_words.append(line.strip())
        print(' ------ File reading is done !!! -------')
    except Exception as rf:
        print('Unexpected error while reading the file!!!!!' + str(rf))
    finally:
        fp.close()
    return sequence_of_words


def evaluate(list_of_words):
    try:
        print('1. What is the first word in the list? ' + list_of_words[0])
        print('2. the last word? ' + list_of_words[len(list_of_words) - 1])
        print('3. the middle word? ' + list_of_words[round((len(list_of_words) / 2)) - 1])
        print('4. the longest word? ' + str(max(list_of_words, key=len)))
        print('5. the shortest word? ' + str(min(list_of_words, key=len)))
        words_begin_with_a = [word for word in list_of_words if word.startswith('a')]
        words_second_letter_a = [word for word in list_of_words if re.match(r".a", word)]
        print('6. How many words begin with a? ' + str(len(words_begin_with_a)))
        first_letter = "".join(item[0] for item in list_of_words)
        all_letter = "".join(item for item in list_of_words)

        dic_first_letter = dict(
            map(lambda letter: (letter, len(first_letter) - len(first_letter.replace(letter, ''))), first_letter))
        dic_all_letter = dict(
            map(lambda letter: (letter, len(all_letter) - len(all_letter.replace(letter, ''))), all_letter))
        print('7. Which letter is most common as a first letter? '
              + max(dic_first_letter.items(), key=operator.itemgetter(1))[0])

        print('8. Are there more words that start with a, or that have a as as their second letter?')
        if len(words_begin_with_a) > 0:
            print(' Found word(s) starts with a - ' + str(words_begin_with_a) + '\n')
        else:
            print(' No word begin with a')
        if len(words_second_letter_a) > 0:
            print(' Found word(s) second character a - ' + str(words_second_letter_a) + '\n')
        else:
            print(' No word which contains the second character a')
        lengths = list(chain(*((len(word) for word in line.split()) for line in list_of_words)))
        print('9. What is the mean word length? ' + str(round(mean(lengths), 2)))
        print('10. the median word length? ' + str(round(median(lengths), 2)))
        print('11. and the mode word length? ' + str(round(mode(lengths), 2)))
        duplicates_words = set([word for word in list_of_words if list_of_words.count(word) > 1])
        print('12. Are there any duplicates in the list?  If so, what words are repeated?')
        if len(duplicates_words) > 0:
            print(str(duplicates_words))
        else:
            print(' No duplicates found')
        print('13. Out of all the letters in all the words in the list, which letter appears most often? '
              + max(dic_all_letter.items(), key=operator.itemgetter(1))[0])
        print('14. Which letter is the rarest? ' + min(dic_all_letter.items(), key=operator.itemgetter(1))[0])
        # case sensitive scenarios not included, in case it has to consider then UPPER() method needs to be added in the applicable places
    except Exception as de:
        print('Unexpected error while evaluating the file!!!!!' + str(de))


if __name__ == "__main__":
    main()
