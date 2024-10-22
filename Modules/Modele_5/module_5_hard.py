import time


class UrTube:

    def __init__(self):
        self.users = [] # как атрибуты экземпляра
        self.videos = [] # как атрибуты экземпляра
        self.current_user = None # как атрибут экземпляра

    def log_in(self, nickname, password):
        for new_user in self.users:
            if new_user.nickname == nickname and new_user.password == password:
                self.current_user = new_user
                return True
        return False

    def register(self, nickname, password, age):
        if any(user.nickname == nickname for user in self.users):
            print(f"Пользователь {nickname} уже существует")
        else:
            self.users.append(User(nickname, password, age))
            self.current_user = self.users[-1]
            # print(f"Пользователь {nickname} зарегистрирован") # доп.


    def log_out(self, current_user):
        self.current_user = current_user
        current_user = None

    def add(self, *videos):
        for video in videos:
            if video not in self.videos:
                self.videos.append(video) # or videos.extend(video)?..

    def get_videos(self, search):
        self.search = search
        search = search.upper()
        result = []
        for video in self.videos:
            if search in video.title.upper():
                result.append(video.title)
            if result == []:
                result = f"Видео не найдено" # доп.
        return result

    def watch_video(self, video_title):
        if self.current_user == None:
            print("Войдите в аккаунт, чтобы смотреть видео")
        elif self.current_user.age < 18 and any([video.adult_mode for video in self.videos if video.title == video_title]):
            print("Вам нет 18 лет, пожалуйста покиньте страницу")
        elif self.current_user.age >= 18 and not any([video.adult_mode for video in self.videos if video.title == video_title]):
            # print("Видео с таким названием не найдено") # доп.
            pass
        else:
            for video in self.videos:
                if video.title == video_title:
                    for sec in range(video.duration):
                        print(sec+1, end=" ")
                        time.sleep(1)
                    print("Конец видео")


class Video:

    def __init__(self, title: str, duration: int, time_now=0, adult_mode=False): # А time_now=0 тут вообще нужен? 🤔
        self.title = title
        self.duration = duration
        self.time_now = time_now
        self.adult_mode = adult_mode


class User:

    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = hash(password)
        self.age = age

    def __str__(self):
        return f"{self.nickname}"


#Код для проверки:
ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

# Добавление видео
ur.add(v1, v2)

# Проверка поиска
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))

# Проверка на вход пользователя и возрастное ограничение
ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')

# Проверка входа в другой аккаунт
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user)

# Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2024 года!')

# доп.
# print(ur.get_videos('еанаераромолгенлорае'))