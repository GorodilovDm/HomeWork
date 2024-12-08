from time import sleep


class User:
    users = {}

    def __init__(self, nickname: str, password: int, age: int):
        self.users[nickname] = {'password': password, 'age': age}


class Video:
    def __init__(self, title, duration, time_now=0, adult_mode=False):
        self.title = title
        self.duration = duration
        self.time_now = time_now
        self.adult_mode = adult_mode


class UrTube:
    def __init__(self):
        self.users = User.users
        self.current_user = None
        self.videos_ = {}
        self.videos = []

    def log_in(self, nickname, password):
        if nickname in self.users:
            if hash(password) == self.users[nickname]['password']:
                self.current_user = nickname
            else:
                print('Неверный пароль')

    def register(self, nickname, password, age):
        if nickname in self.users:
            print(f'Пользователь {nickname} уже существует')
        else:
            user = User(nickname, hash(password), age)
            self.log_in(nickname, password)

    def log_out(self):
        print(self.current_user)
        self.current_user = None
        print('delet')
        print(self.current_user)
        pass

    def add(self, *video):
        for i in video:
            if i.title not in self.videos:
                self.videos.append(i.title)
                self.videos_[i.title] = {'duration': i.duration, 'time_now': i.time_now, 'adult_mode': i.adult_mode}

    def get_videos(self, string):
        get_vid = []
        for i in range(len(self.videos)):
            if string.upper() in self.videos[i].upper():
                get_vid.append(self.videos[i])
        return get_vid

    def watch_video(self, title):
        if self.current_user != None:
            if title in self.videos:
                if not self.videos_[title]['adult_mode'] or self.users[self.current_user]['age'] >= 18:

                    for i in range(self.videos_[title]['time_now'], self.videos_[title]['duration']):
                        sleep(1)
                        print(i + 1, end=' ')
                        self.videos_[title]['time_now'] = i + 1
                    print('Конец видео')
                    self.videos_[title]['time_now'] = 0
                else:
                    print('Вам нет 18 лет, пожалуйста покиньте страницу')
            else:
                print('Нет видео')
        else:
            print('Войдите в аккаунт, чтобы смотреть видео')


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
