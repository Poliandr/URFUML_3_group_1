import streamlit as st
from transformers import pipeline
from io import BytesIO
from PIL import Image

def main():
    st.title("Поиск информации о достопримечательностях")

    # создаем форму для загрузки изображения
    uploaded_file = st.file_uploader("Загрузка изображения", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        # сохраняем изображение в байтовом формате
        image_bytes = uploaded_file.read()

        # используем PIL для открытия изображения из байтов
        image = Image.open(BytesIO(image_bytes))

        # отображаем изображение в приложении
        st.image(image, caption="Uploaded Image", use_column_width=True)

        # используем модель для классификации изображения
        run_classification(image)

def run_classification(image):
    """
    Функция запускает классификацию изображения с помощью модели
    и выводит результаты предсказания в приложении.
    image: PIL.Image, изображение для классификации
    """
    # загружаем модель
    pipe = pipeline("image-classification", model="mmgyorke/vit-world-landmarks")
    # находим максимальный результат предсказания
    result = max(pipe(image), key=lambda x: x['score'])
    # выводим результаты предсказания в приложении
    st.title(result['label'])

if __name__ == "__main__":
    main()
