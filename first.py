from collections import Counter
import csv
import re


def count_words(source_file):
    pattern = re.compile('([^\s\w]|_)+')
    with open(source_file) as fp:
        words_in_book = pattern.sub('', fp.read()).split()
    return Counter(words_in_book)


names_to_count = [
    'Paris',
    'Helen',
    'Hector',
    'Achilles',
    'Agamemnon'
]

with open('iliadcounts.csv', 'w', newline='') as csvfile:
    name_count_writer = csv.writer(csvfile, delimiter=';', quoting=csv.QUOTE_MINIMAL)
    for name in names_to_count:
        name_count_writer.writerow([name + ' ', ' ' + str(count_words('pg2199.txt').get(name))])
