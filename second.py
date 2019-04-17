import csv

from first import count_words


def main():
    print('Please enter name of the source file')
    source_file = input()
    if not check_if_file_exists(source_file):
        return

    print('Please enter the name of the file with strings to search')
    file_with_strings_to_search = input()
    if not check_if_file_exists(file_with_strings_to_search):
        return

    with open(file_with_strings_to_search) as fp:
        words_to_count = [w.strip() for w in fp.readlines()]

    words_counts = count_words(source_file)

    with open('wordcounts.csv', 'w', newline='') as csvfile:
        word_count_writer = csv.writer(csvfile, delimiter=';', quoting=csv.QUOTE_MINIMAL)
        for word in words_to_count:
            word_count = words_counts.get(word)
            if word_count >= 10:
                word_count_writer.writerow([word + ' ', ' ' + str(word_count)])


def check_if_file_exists(source_file):
    try:
        with open(source_file):
            return True
    except FileNotFoundError:
        print('The file %s does not exist!' % source_file)
        return False


if __name__ == "__main__":
    main()
