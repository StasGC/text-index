from Eviction import delete_punctuation, make_index, make_stop_list, make_top
import argparse

stop_list = make_stop_list()

arr_of_words = []
dictionary_of_words = dict()
num_of_line = 0
page = 1

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-call", type=str, choices=["index", "top", "all"], default="all")
    parser.add_argument("-i", type=str, default="input.txt")
    args, unknown = parser.parse_known_args()
    if args.call == "index":
        parser.add_argument("-o", type=str, default="output_index.txt")
    elif args.call == "top":
        parser.add_argument("-w", type=str, default="output_top.txt")
        parser.add_argument("-nt", "--num_top", type=int)
    else:
        parser.add_argument("-o", type=str, default="output_index.txt")
        parser.add_argument("-w", type=str, default="output_top.txt")
        parser.add_argument("-nt", "--num_top", type=int)

    args, unknown = parser.parse_known_args()

    with open(args.i, "r", encoding="utf-8") as data:
        for tmp_line in data.readlines():
            tmp_line = list(map(str, tmp_line.split()))
            if not tmp_line:
                continue
            num_of_line += 1
            for word in tmp_line:
                word = word.lower()
                word = delete_punctuation(word)
                if (word in stop_list) or (not word):
                    continue
                if word not in arr_of_words:
                    arr_of_words.append(word)
                if word in dictionary_of_words.keys():
                    dictionary_of_words[word] += [page]
                else:
                    dictionary_of_words[word] = [page]
            if num_of_line == 45:
                num_of_line = 0
                page += 1

    arr_of_words.sort()

    dictionary_of_words_with_single_pages = make_index(dictionary_of_words)

    if args.call == "index" or args.call == "all":
        with open(args.o, "w", encoding="utf-8") as index_ans:
            for word in arr_of_words:
                index_ans.write(word + ": " + str(dictionary_of_words_with_single_pages[word]) + "\n")

    word_order_for_top = make_top(dictionary_of_words)[0]
    frequency_dictionary = make_top(dictionary_of_words)[1]

    if args.call == "top" or args.call == "all":
        with open(args.w, "w", encoding="utf-8") as top_ans:
            if args.num_top > len(word_order_for_top):
                args.num_top = len(word_order_for_top)
            for word in word_order_for_top[:args.num_top]:
                top_ans.write(word + ": " + str(frequency_dictionary[word]) + "\n")


