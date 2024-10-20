"""This is homework 4."""


import logging

SEPARATOR = '=' * 75
# Configure logging
logging.basicConfig(level=logging.INFO, format='')
_log = logging.getLogger(__name__)
adwentures_of_tom_sawer = """\
Tom gave up the brush with reluctance in his .... face but alacrity
in his heart. And while
the late steamer
"Big Missouri" worked ....
and sweated
in the sun,
the retired artist sat on a barrel in the .... shade close by,
dangled his legs,
munched his apple, and planned the slaughter of more innocents.
There was no lack of material;
boys happened along every little while;
they came to jeer, but .... remained to whitewash. ....
By the time Ben was fagged out,
Tom had traded the next chance to Billy Fisher for
a kite, in good repair;
and when he played
out, Johnny Miller bought
in for a dead rat and a string to swing it with—and so on, and so on,
hour after hour. And when the middle of the afternoon came, from being a
poor poverty, stricken boy in the .... morning, Tom was literally
rolling in wealth."""

# ПЕРЕЗАПИСУЙТЕ зміст змінної adwentures_of_tom_sawer у завданнях 1-3
# task 01 ==
""" Дані у строці adwentures_of_tom_sawer
розбиті випадковим чином, через помилку.
треба замінити кінець абзацу на пробіл .replace("\n", " ")"""

_log.info(adwentures_of_tom_sawer)
str_result = adwentures_of_tom_sawer.replace('\n', ' ')
_log.info(str_result)
_log.info(SEPARATOR)

# task 02 ==
""" Замініть .... на пробіл
"""

str_result2 = str_result.replace(' .... ', ' ')
str_result2 = str_result.replace(' ....', ' ')
_log.info(str_result2)
_log.info(SEPARATOR)

# task 03 ==
""" Зробіть так, щоб у тексті було не більше одного пробілу між словами.
"""

str_result3 = str_result2.replace('  ', ' ')
_log.info(str_result3)
_log.info(SEPARATOR)


# task 04
""" Виведіть, скількі разів у тексті зустрічається літера "h"
"""

letter_appears = str_result3.count('h')
_log.info(f'h letter appears: {letter_appears} times')
_log.info(SEPARATOR)

# task 05
""" Виведіть, скільки слів у тексті починається з Великої літери?
"""

words = str_result3.split()
counter = 0
for word in words:
    if word.istitle():
        counter += 1
_log.info(f'Upper letter appears: {counter} times')
_log.info(SEPARATOR)

# task 06
""" Виведіть позицію, на якій слово Tom зустрічається вдруге
"""

name = str_result3.find('Tom', 1)
_log.info(f'Second time Tom appears in {name} position')
_log.info(SEPARATOR)

# task 07
""" Розділіть змінну adwentures_of_tom_sawer по кінцю речення.
Збережіть результат у змінній adwentures_of_tom_sawer_sentences
"""

adwentures_of_tom_sawer_sentences = None
adwentures_of_tom_sawer_sentences = str_result3.split('. ')
_log.info(adwentures_of_tom_sawer_sentences)
_log.info(SEPARATOR)

# task 08
""" Виведіть четверте речення з adwentures_of_tom_sawer_sentences.
Перетворіть рядок у нижній регістр.
"""

_log.info(adwentures_of_tom_sawer_sentences[3].lower())
_log.info(SEPARATOR)

# task 09
""" Перевірте чи починається якесь речення з "By the time".
"""

_log.info(adwentures_of_tom_sawer_sentences[3].startswith('By the time'))
_log.info(SEPARATOR)

# task 10
""" Виведіть кількість слів останнього речення
з adwentures_of_tom_sawer_sentences.
"""

_log.info(len(adwentures_of_tom_sawer_sentences[-1].split()))
_log.info(SEPARATOR)
