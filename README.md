#Категории и товары

##Описание

## Основной функционал

- Создание и управление товарами с базовыми характеристиками: название, описание, цена и количество.
- Специализированные классы товаров с дополнительными свойствами (например, смартфоны и газонная трава).
- Категории для группировки товаров с возможностью добавления новых продуктов.
- Контроль корректности цены товара с помощью сеттера.
- Поддержка сложения товаров одного типа для подсчёта общей стоимости.
- Логирование создания объектов для удобства отладки


### Запуск тестов и проверка покрытия

Для запуска тестов используйте:

```bash
pytest --cov=src