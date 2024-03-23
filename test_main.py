from PIL import Image
from main import run_classification

def test_run_classification():
    # Загрузка тестового изображения
    image = Image.open("test_image.jpg")

    # Вызов функции run_classification
    run_classification(image)

def test_invalid_image_input():
    # Тест на некорректный ввод изображения
    invalid_image_path = "invalid_image.jpg"
    try:
        invalid_image = Image.open(invalid_image_path)
        run_classification(invalid_image)
    except Exception as e:
        assert type(e) == FileNotFoundError

def test_output_format():
    # Тест на формат вывода функции run_classification
    image = Image.open("test_image.jpg")
    output = run_classification(image)
    assert isinstance(output, str)

def test_classification_result():
    # Тест на корректность результата классификации
    image = Image.open("test_image.jpg")
    expected_result = "cat"  # Предполагаемый ожидаемый результат классификации
    result = run_classification(image)
    assert result == expected_result

if __name__ == "__main__":
    test_run_classification()
    test_invalid_image_input()
    test_output_format()
    test_classification_result()
