import os
import django
import json
from django.core import serializers

# Настройка Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from catalog.models import Category, Product


def create_fixtures():
    # Создаем папку fixtures если её нет
    os.makedirs('fixtures', exist_ok=True)

    # Получаем данные
    categories = Category.objects.all()
    products = Product.objects.all()

    # Проверяем, есть ли данные
    if categories.count() == 0:
        print("❌ Нет категорий! Сначала создайте их в Django shell.")
        return

    # Сохраняем категории в правильном формате
    with open('fixtures/categories.json', 'w', encoding='utf-8') as f:
        data = serializers.serialize('json', categories, indent=4, use_natural_foreign_keys=False)
        f.write(data)

    # Сохраняем продукты в правильном формате
    with open('fixtures/products.json', 'w', encoding='utf-8') as f:
        data = serializers.serialize('json', products, indent=4, use_natural_foreign_keys=False)
        f.write(data)

    print(f"✅ Категории сохранены: {categories.count()} записей")
    print(f"✅ Продукты сохранены: {products.count()} записей")

    # Выводим первые 2 строки для проверки
    print("\nПервые строки categories.json:")
    with open('fixtures/categories.json', 'r', encoding='utf-8') as f:
        for i, line in enumerate(f):
            if i < 3:
                print(line.strip())

    print("\nПервые строки products.json:")
    with open('fixtures/products.json', 'r', encoding='utf-8') as f:
        for i, line in enumerate(f):
            if i < 3:
                print(line.strip())


if __name__ == "__main__":
    create_fixtures()