from PIL import Image
from main import run_classification

def test_run_classification():
    # загрузка тестового изображения
    image = Image.open("test_image.jpg")

    # вызов функции run_classification
    run_classification(image)

test_run_classification()
