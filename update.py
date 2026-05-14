import os
import random
import shutil

# Путь к папке с твоими 83 артами
source_dir = "gallery"
# Файл, который отображается в README
target_file = "arturia_vibe.jpg"

def update_art():
    if not os.path.exists(source_dir):
        print("Папка gallery не найдена!")
        return

    # Ищем картинки и твою гифку
    extensions = ('.png', '.jpg', '.jpeg', '.gif')
    images = [f for f in os.listdir(source_dir) if f.lower().endswith(extensions)]
    
    if not images:
        print("В папке gallery пусто!")
        return

    # Выбираем рандомный арт
    random_image = random.choice(images)
    
    # Копируем её в главный файл профиля
    shutil.copy(os.path.join(source_dir, random_image), target_file)
    print(f"Сейчас установлена: {random_image}")

if __name__ == "__main__":
    update_art()
