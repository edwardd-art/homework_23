from django.core.management.base import BaseCommand
from django.core.management import call_command
from catalog.models import Category, Product


class Command(BaseCommand):
    help = 'Загружает тестовые данные из фикстур'

    def handle(self, *args, **options):
        self.stdout.write(self.style.WARNING('Начинается загрузка тестовых данных...'))

        # 1. Удаляем существующие данные
        self.stdout.write('Удаление существующих данных...')
        products_count = Product.objects.count()
        categories_count = Category.objects.count()

        Product.objects.all().delete()
        Category.objects.all().delete()

        self.stdout.write(f'Удалено продуктов: {products_count}')
        self.stdout.write(f'Удалено категорий: {categories_count}')

        # 2. Загружаем данные из фикстур
        self.stdout.write('Загрузка данных из фикстур...')
        call_command('loaddata', 'fixtures/categories.json', verbosity=0)
        self.stdout.write('✓ Категории загружены')
        call_command('loaddata', 'fixtures/products.json', verbosity=0)
        self.stdout.write('✓ Продукты загружены')

        # 3. Проверяем результат
        new_products = Product.objects.count()
        new_categories = Category.objects.count()

        self.stdout.write(self.style.SUCCESS(
            f'\nДанные успешно загружены!\n'
            f'Загружено категорий: {new_categories}\n'
            f'Загружено продуктов: {new_products}'
        ))