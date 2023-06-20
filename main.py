""" Списки и циклы """
questions = ["My name ___  Vova", "I ___ a coder", "I live ___ Moscow"]
answers = ["is", "am", "in"]
true_answer = 0
all_answers = 3
result = 0
user_input = input('Привет! Предлагаю проверить свои знания английского! Наберите "ready", чтобы начать: ')

if user_input == "ready":
    for i, question in enumerate(questions):
        answer = answers[i]
        print(question)
        user_input = input("Ваш ответ: ")
        if user_input == answer:
            print("Правильно")
            true_answer += 1
        else:
            print(f"Неправильно, верный ответ {answer}")

    if true_answer == 3:
        result += 100
    elif true_answer == 2:
        result += 66
    else:
        result += 33

    print(f'Вот и все! Вы ответили на {true_answer} вопросов из {all_answers} верно, это {result} процентов.')

else:
    print("Пока")
