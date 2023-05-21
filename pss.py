from PIL import Image
from sprites import *
import io

# Открываем изображение с ошибкой в цветовом профиле
img = Image.open(Sprites.BACKGROUND_MENU)

# Проверяем формат изображения
if img.format != 'PNG':
    print('Формат изображения не поддерживается.')
    exit()

# Проверяем наличие цветового профиля и его корректность
if 'icc_profile' in img.info:
    if img.info['icc_profile'] != None:
        try:
            img_with_profile = Image.open(io.BytesIO(img.info['icc_profile']))
            if img_with_profile.info.get('ICC Profile').startswith(b'acsp'):
                img.info.pop('icc_profile')
        except IOError:
            print('Ошибка при обработке цветового профиля.')
            exit()

# Сохраняем исправленное изображение
img.save('новое_имя_изображения.png')
