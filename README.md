# Проект «Составление индекса для текстового файла»

## Описание предметной области

Этот проект посвящён обработке текстовых файлов (в формате txt). Текстовые файлы состоят из строк, строки собираются в страницы (можно считать, что каждая страница содержит ровно 45 строк, пустые строки при этом не учитываются). 

Индексом текстового файла называется алфавитный перечень использованных в тексте слов с указанием для каждого слова номеров страниц, на которых оно встречается. Предлоги, союзы, местоимения и междометия при составлении индекса можно игнорировать. Словоформы одного слова (например, слова, отличающиеся падежными окончаниями) можно считать разными словами.

Пример текстового файла можно найти в подкаталоге `add`. Можно также работать с любыми другими текстовыми файлами.

## Задание

Написать программу со следующей функциональностью:

* составление индекса по заданному файлу в формате txt
* вывод списка из заданного количества наиболее часто встречающихся слов по заданному файлу с индексом

Данные для программы должны задаваться в параметрах командной строки. Все функции должны быть протестированы. 

### Требования к реализации

* Язык программирования: Julia (СП), Python (МААД)
* Внешние библиотеки: нет
* Корректность: да
* Производительность: нет
* Срок выполнения: 3 октября (мягкий дедлайн), 10 октября (жёсткий дедлайн)

### Самостоятельно принимаемые решения

* формат вывода результатов
* модульная структура, разбиение на компоненты

## Критерии оценивания

Проект оценивается исходя из 12 баллов с учётом критериев качества, сформулированных во второй лекции.