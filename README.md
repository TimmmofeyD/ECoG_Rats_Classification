# Международный хакатон 2024 Цифровой прорыв (сезон ИИ)

## Описание кейса

### Название 
**«Система классификации электрокортикограмм» от ФГБУ «НМИЦ ТПМ» Минздрава России**

### Постановка задачи
Сегодня фундаментальная и клиническая наука рассматривает сон как сложный физиологический процесс, который обеспечивает протекание процессов восстановления организма. Структура сна здорового человека хорошо известна. Большинство системных заболеваний сопровождаются нарушением структуры сна. Анализ сна и его нарушений является ключевым элементом в диагностике и прогнозировании различных психических и нервных заболеваний. Изучение структуры сна позволяет не только диагностировать существующие расстройства, но и предсказывать их развитие. Существует тесная взаимосвязь между патогенезом генерализованных эпилепсий и нарушениями сна на уровне таламо-кортикальной системы. Крысы WAG/Rij являются надежной моделью абсанс-эпилепсии человека и широко используются в доклинических исследованиях.

Участникам хакатона предлагается создать программный модуль для распознавания фазы глубокого сна и промежуточной фазы сна по данным электрокортикограмм у крыс WAG/Rij, используемых в доклинических исследованиях абсанс-эпилепсии.

## Решение кейса

### Как это работает

1. **Подготовка данных**: 
    - Преобразование данных в вектора со скользящим окном данных
    - Использование преобразования Фурье для выделения коллебательной коммпоненты, и мощности ряда

2. **Сверточная нейронная сеть**:
   - Модель построена на свертках (CNN), что позволяет выделять нелинейные паттерны в данных
   - Модель предсказывает сразу 4 класса: 3 основных класса и шум

3. **Разметка**:
   - Использование окон данных и дробление ряда на батчи позволяет сильно ускорить как обучение модели так и разметку файлов
   - После загрузки edf файла в приложение, модели нужно от 1 до 3 минут, чтобы его обработать и выдать пользователю уже размечанный edf файл


### Видео работы exe файла
https://drive.google.com/drive/folders/1zOB--4MJkA5IubsTXLgKbP0Be7s7PRSj?usp=sharing

### Инструкция для запуска exe
Для запуска скомпилированного приложения переходим по ссылке на гугл диск: https://drive.google.com/drive/folders/1zOB--4MJkA5IubsTXLgKbP0Be7s7PRSj?usp=sharing
Файл называется PriMat_v2.zip
Далее скачиваем zip файл, разархивируем его и запускаем ECS.exe
После этого выбираем edf файл с вашего устройства и запускаем модель
В течении 1-3 минут вы сможете скачать размеченный edf файл, который можно открыть в браузере для просмотра edf файлов.

## Наша команда

### Название 
**ПриМат**

Мы студенты кафедры РТУ МИРЭА, кафедра Прикладной математики

### Состав
- **Закирова Екатерина**: 
  - Роль в команде: Дизайнер
  - О себе: 3-й курс бакалавриата
  - Стек технологий: Python (Pandas/Matlotlib/Sklearn/PyTorch/Streamlit), SQL (PostgreSQL/ClickHouse), PowerPoint
- **Казакова Анна**: 
  - Роль в команде: Разработчик приложения
  - О себе: 2-й курс магистратуры
  - Стек технологий: Python (Pandas/Matlotlib/Sklearn/PyTorch/Streamlit), SQL (PostgreSQL/ClickHouse), Loginom, BPMN
- **Лищенко Тимофей**: 
  - Роль в команде: ML-инженер
  - О себе: 3-й курс бакалавриата
  - Стек технологий: Python, R, Pandas, NumPy, SQL, Hadoop, Git, Streamlit
- **Попов Артем**:
  - Роль в команде: Капитан команды, ML-инженер
  - О себе: 2-й курс магистратуры, работаю в Автомакон ДатаЛаб дата-сайнтистом, занимаюсь прогнозированием спроса для компании ВкусВилл, прокачиваю свои навыки в класическом ML и прогнозировании временных рядов
  - Стек технологий: Python (Pandas/Matlotlib/Sklearn/PyTorch/Numpy), SQL (PostgreSQL/ClickHouse), Класические ML модели/Нейронные сети/Базовый NLP (TimeToVec)
- **Филиппенко Данил**:
  - Роль в команде: ML-инженер
  - О себе: 2-й курс магистратуры. DS в Казначействе Альфа Банка. Занимаюсь разработкой различных прогнозных и финансовых моделей.
  - Стек технологий: Стек Python, классический ML, математическая статистика.
