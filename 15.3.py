from random import *

answers = ['Бесспорно', 'Предрешено', 'Никаких сомнений',
           'Определённо да', 'Можешь быть уверен в этом',
           'Мне кажется - да', 'Вероятнее всего', 'Хорошие перспективы',
           'Знаки говорят - да', 'Да', 'Пока неясно, попробуй снова', 'Спроси позже',
           'Лучше не обращаться', 'сейчас нельзя предсказать', 'Сконцентрируйся и спроси опять',
           'Даже не думай', 'Мой ответ - нет', 'По моим данным - нет', 'Перспективы не очень хорошие',
           'Весьма сомнительно']
print('Привет Мир, я магический шар, и я знаю ответ на любой твой вопрос.')
name = input('Введите имя')
print(f'привет {name}')
while True:
    question = input('Задайте вопрос!')
    print(choice(answers), end='\n')
    question_again = input('Хотите ли вы задать еще один вопрос?')
    ans_yes = ('да', 'yes', 'y', 'д')
    if question_again.lower() in ans_yes:
        continue
    else:
        print('Возвращайся если возникнут вопросы!')
        break
