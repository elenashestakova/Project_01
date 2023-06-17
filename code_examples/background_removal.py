import os

from rembg import remove
from PIL import Image


def remove_bg(place):
    if not os.path.isdir('images_without_bg'):
        os.mkdir('images_without_bg')
    for pict in os.listdir(place):
        if pict.endswith('.png') or pict.endswith('.jpg') or pict.endswith('.jpeg'):
            print(f'[+] Удаляю фон: "{pict}"...')
            output = remove(Image.open(os.path.join(place, pict)))
            output.save(os.path.join('images_without_bg', f'{pict.split(".")[0]}.png'))
        else:
            continue


def get_target_path():
    while not os.path.isdir(user_input := input("[+] Введите путь к папке с изображениями: ")):
        print(f'Папка "{user_input}" не найдена\n')
    print(f"\nРаботаем с папкой {user_input}\n")
    return user_input


def main():
    remove_bg(get_target_path())
    print('\n[+] Удаление завершено!')


if __name__ == "__main__":
    main()

