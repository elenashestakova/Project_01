# Задача 1.1.

# Есть строка с перечислением песен

my_favorite_songs = 'Waste a Moment, Staying\' Alive, A Sorta Fairytale, Start Me Up, New Salvation'

# Выведите на консоль с помощью индексации строки, последовательно: первый трек, последний, второй, второй с конца
# Нельзя переопределять my_favorite_songs и запятая не должна выводиться.

# Первый трек
first_song = my_favorite_songs.split(',')[0]

# Последний трек
last_song = my_favorite_songs.split(',')[-1].lstrip()

# Второй трек
second_song = my_favorite_songs.split(',')[1].lstrip()

# Второй с конца трек
second_from_the_end_song = my_favorite_songs.split(',')[-2].lstrip()

print(first_song, last_song, second_song, second_from_the_end_song, sep ='\n')