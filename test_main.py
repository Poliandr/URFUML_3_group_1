from PIL import Image
from main import run_classification

def test_run_classification():
    # загрузка тестового изображения
    image = Image.open("test_image.jpg")

    # вызов функции run_classification
    run_classification(image)

def test_invalid_image_input():
    # тест на некорректный ввод изображения
    invalid_image_path = "invalid_image.jpg"
    try:
        invalid_image = Image.open(invalid_image_path)
        run_classification(invalid_image)
    except Exception as e:
        assert type(e) == FileNotFoundError

def test_output_format():
    # тест на формат вывода функции run_classification
    image = Image.open("test_image.jpg")
    output = run_classification(image)
    assert isinstance(output, str)

if __name__ == "__main__":
    test_run_classification()
    test_invalid_image_input()
    test_output_format()
