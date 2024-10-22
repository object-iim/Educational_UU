def send_email(message, recipient, *, sender="university.help@gmail.com"):
    if '@' not in sender and '@' not in recipient:
        print(f"Невозможно отправить письмо с адреса {sender} на адрес {recipient}")

    if not recipient.endswith('.com') or not recipient.endswith('.ru') or not recipient.endswith('.net'):
        flag = True
    else:
        print(f"Невозможно отправить письмо с адреса {sender} на адрес {recipient}")

    if not sender.endswith('.com') and not sender.endswith('.ru') and not sender.endswith('.net'):
        print(f"Невозможно отправить письмо с адреса {sender} на адрес {recipient}")

    if sender == 'university.help@gmail.com' and recipient != sender:
        print(f"Письмо успешно отправлено с адреса {sender} на адрес {recipient}")

    if recipient == sender:
        print("Нельзя отправить письмо самому себе!")

    elif sender != 'university.help@gmail.com' and sender.endswith('.com') or sender.endswith('.ru') or sender.endswith('.net'):
        print(f"НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}")

send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')

# Вторая версия

def send_email(message, recipient, *, sender="university.help@gmail.com"):

    if not '@' in sender or not '@' in recipient: # or возвращает Т, если @ нет хоть в одном адресе
        print(f"Невозможно отправить письмо с адреса {sender} на адрес {recipient}")

    if not sender.endswith('.com') and not sender.endswith('.ru') and not sender.endswith('.net'): # and возвращает Т, если нет ни одного из этих доменов
        print(f"Невозможно отправить письмо с адреса {sender} на адрес {recipient}")

    elif not recipient.endswith('.com') and not recipient.endswith('.ru') and not recipient.endswith('.net'):  # and возвращает Т, если нет ни одного из этих доменов
        print(f"Невозможно отправить письмо с адреса {sender} на адрес {recipient}")

    elif recipient == sender:
        print("Нельзя отправить письмо самому себе!")

    elif sender != 'university.help@gmail.com' and sender.endswith('.com') or sender.endswith('.ru') or sender.endswith('.net'):
        print(f"НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}")

    else:
        print(f"Письмо успешно отправлено с адреса {sender} на адрес {recipient}")

send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')