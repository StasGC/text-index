def delete_punctuation(word):
    """Данная функция предназначена для удаления нежелательных символов внутри слова, кроме того,
    мы не станем считать в индекс отдельные элементы пунктуации и цифры,
    которые не интересны для нашего анализа текста."""
    punctuation = ['.', ',', ':', ';', '!', '?', '(', ')', '"', '*', '', '[', ']',
                   '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    for i in punctuation:
        j = 0
        while j < len(word):
            if word[j] == i:
                word = word.replace(word[j], "")
                j -= 1
            j += 1
    return word


def make_stop_list():
    """Данная функция составляет массив из "стоп - слов", то есть слова, которые не будут засчитываться в индекс,
    в данный список входят часто встречающиеся предлоги, союзные слова, либо слова, индекс по которым вам не интересен
     (в таком случае, вы можете отредактировать текстовый файл "stop_words_russian.txt", добавить туда эти слова,
     и алгоритм не будет подсчитывать их)."""
    stop_list = []
    with open('stop_words_russian.txt', 'r', encoding='utf-8') as data:
        for tmp_stop_list in data.readlines():
            stop_list.append(tmp_stop_list.strip("\n"))
    return stop_list


def make_index(dictionary_of_words):
    """Эта функция, получая на вход словарь, в ключах которого все слова, встречающиеся в тексте,
     а значением каждого слова является массив с номерами страниц, на которых оно встречалось,
     при чем в значение записывалось всякое вхождение слова, то есть, страницы могут многократно повторяться.
     Тут мы делаем новый словарь, где для каждого слова имеем массив из всех страниц, на которых оно встречалось,
     каждая страница упоминается 1 раз. В принципе, данный словарь и является готовым индексом."""
    dictionary_of_words_with_single_pages = dict()
    for word in dictionary_of_words.keys():
        dictionary_of_words_with_single_pages[word] = list(set(dictionary_of_words[word]))
    return dictionary_of_words_with_single_pages


def make_top(dictionary_of_words):
    """Данная функция составляет словарь, где каждому слову сопоставлено число, равное количеству вхождений
    слова в текст. Выдает массив с порядком слов, который определяет топ."""
    frequency_dictionary = dict()
    keys_from_frequency = []
    for word in dictionary_of_words.keys():
        frequency_dictionary[word] = len(dictionary_of_words[word])
        if len(dictionary_of_words[word]) not in keys_from_frequency:
            keys_from_frequency.append(len(dictionary_of_words[word]))

    keys_from_frequency.sort(reverse=True)

    word_order_for_top = []
    for num in keys_from_frequency:
        for word in frequency_dictionary.keys():
            if frequency_dictionary[word] == num:
                word_order_for_top.append(word)

    return [word_order_for_top, frequency_dictionary]
