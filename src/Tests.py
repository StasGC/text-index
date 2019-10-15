from Eviction import delete_punctuation, make_index, make_stop_list
import logging

logging.basicConfig(
    level=logging.DEBUG,
    format="%(levelname)s: %(message)s"
)


def check(text, expected):
    stop_list = make_stop_list()

    arr_of_words = []
    dictionary_of_words = dict()
    num_of_line = 0
    page = 1
    with open(text, "r", encoding="utf-8") as data:
        for tmp_line in data.readlines():
            tmp_line = list(map(str, tmp_line.split()))
            if not tmp_line:
                continue
            num_of_line += 1
            for word in tmp_line:
                word = delete_punctuation(word)
                if (word in stop_list) or (not word):
                    continue
                if word not in arr_of_words:
                    arr_of_words.append(word)
                if word in dictionary_of_words.keys():
                    dictionary_of_words[word] += [page]
                else:
                    dictionary_of_words[word] = [page]
            if num_of_line == 5:
                num_of_line = 0
                page += 1

    arr_of_words.sort()

    dictionary_of_words_with_single_pages = make_index(dictionary_of_words)
    assert dictionary_of_words_with_single_pages == expected


def test_make_index():
    logging.debug("Running make_index test")

    check("text1.txt", {'Желаю': [1], 'крепкого': [1], 'здоровья': [1], 'Улыбок': [1], 'преданных': [1], 'друзей': [1],
                        'Финансов': [1], 'полные': [1], 'карманы': [1], 'И': [1], 'добрых': [1], 'новостей': [1],
                        'пусть': [1], 'беда': [1], 'обходит': [1], 'Тебя': [2], 'дом': [2], 'твой': [2],
                        'стороной': [2], 'А': [2], 'радость': [2], 'молодость': [2], 'веселье': [2], 'Останутся': [2],
                        'тобой': [2], 'В': [2], 'день': [2], 'тебе': [2], 'желаю': [2], 'Море': [2], 'счастья': [2],
                        'добра': [2], 'Чтоб': [3], 'мечты': [3], 'сбывались': [3], 'С': [3], 'днем': [3],
                        'рождения': [3]})
    check("text2.txt", {'Advertisements': [1], 'want': [1], 'to': [1, 2, 3], 'persuade': [1], 'us': [1], 'buy': [1],
                        'particular': [1], 'products': [1], 'How': [1], 'do': [1, 2], 'they': [1, 3], 'it': [1, 2],
                        'Let’s': [1], 'imagine': [1], '…You’re': [1], 'watching': [1], 'TV': [1], 'It’s': [1],
                        'a': [1, 2, 3], 'hot': [1], 'evening': [1], 'You': [1], 'feel': [1], 'thirsty': [1],
                        'see': [1, 2], 'an': [1, 2], 'advert': [1, 2], 'for': [1, 2, 3], 'refreshing': [1, 2],
                        'drink': [1, 2], 'people': [1], 'looking': [1], 'cool': [1, 2], 'and': [1, 2, 3],
                        'relaxed': [1], 'notice': [1], 'the': [1, 2, 3], 'name': [1, 2], 'of': [1, 2, 3],
                        'because': [1, 3], 'you': [1, 2], 'think': [1], 'could': [1], 'be': [1, 2, 3], 'useful': [1],
                        'satisfy': [1], 'your': [1], 'thirst': [1], 'Advertisers': [1], 'study': [1], 'how': [1],
                        'learn': [1, 3], 'so': [1], 'that': [1, 3], 'can': [1, 2, 3], '‘teach’': [1], 'them': [1],
                        'respond': [1], 'their': [1], 'advertising': [1, 3], 'They': [1], 'interested': [2], 'try': [2],
                        'something': [2], 'then': [2], 'again': [2], 'These': [2], 'are': [2, 3], 'elements': [2],
                        'learning': [2], 'interest': [2], 'experience': [2], 'repetition': [2, 3], 'If': [2, 3],
                        'achieve': [2], 'this': [2], 'is': [2, 3], 'successful': [2, 3], 'works': [2], 'well': [2, 3],
                        'same': [2], 'technique': [2], 'used': [2], 'advertise': [2], 'different': [2, 3],
                        'things': [2], 'So': [2, 3], 'example': [2, 3], 'in': [2, 3], 'winter': [2], 'if': [2],
                        'weather': [2], 'cold': [2], 'family': [2], 'having': [2], 'warming': [2], 'cup': [2],
                        'tea': [2, 3], 'feeling': [2], 'cosy': [2], 'may': [2, 3], 'note': [2], '…': [2], 'Here': [2],
                        'being': [2], 'as': [2], 'with': [2], 'advertisements': [3], 'he': [3], 'learned': [3],
                        'there': [3], 'need': [3], 'lots': [3], 'But': [3], 'advertisers': [3], 'have': [3],
                        'careful': [3], 'too': [3], 'much': [3], 'result': [3], 'consumer': [3], 'tiredness': [3],
                        'message': [3], 'fall': [3], 'on’deal': [3], 'ears’': [3], 'Consumers': [3], 'generalize': [3],
                        'from': [3], 'what': [3], 'sometimes': [3], 'copy': [3], 'highly': [3], 'idea': [3], 'has': [3],
                        'been': [3], 'by': [3], 'consumers': [3], 'For': [3], '‘Weston': [3], 'Tea': [3],
                        'Country’': [3], 'led': [3], '‘DAEWOO': [3], 'automobile': [3], 'dealers': [3], '‘Cadbury': [3],
                        'chocolate': [3], 'bars': [3]})
    logging.debug("make_index test completed")


if __name__ == '__main__':
    logging.debug("Внимание!!! Для удобства написания тестов, 1 страница = 5 строк")
    logging.debug("Running tests")

    test_make_index()

