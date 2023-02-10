import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')

import django
django.setup()

# import ==>

from faker import Faker
import random

from products.models import Product , Brand , Category

def seed_brand(n):
    fake = Faker()
    images = ['1.png','2.jpg','3.jpg','4.jpg','5.png','6.png']

    for _ in range(n):
        name = fake.name()
        image = f"brand/{images[random.randint(0,5)]}"
        Brand.objects.create(
            name = name,
            image = image
        )
    print(f'Successfully seeded {n} Brand')


def seed_category(n):
    fake = Faker()
    images = ['1.png','2.jpg','3.jpg','4.jpg','5.png','6.png']

    for _ in range(n):
        name = fake.name()
        image = f"category/{images[random.randint(0,5)]}"
        Category.objects.create(
            name = name,
            image = image
        )
    print(f'Successfully seeded {n} Category')


def seed_products(n):
    fake = Faker()
    images = ['1.png','2.jpg','3.png','4.png','5.png','6.png','7.png','8.png','9.png','10.png']
    flag_type = ['New','Feature','Sale']

    for _ in range(n):
        name = fake.name()
        sku = random.randint(1,100000)
        subtitle = fake.text(max_nb_chars=300)
        desc = fake.text(max_nb_chars=10000)
        flag = flag_type[random.randint(0,2)]
        price = round(random.uniform(20.99,99.99),2)
        image = f"products/{images[random.randint(0,9)]}"
        category = Category.objects.get(id=random.randint(1,10))
        brand = Brand.objects.get(id=random.randint(1,5))
        Product.objects.create(
            name = name,
            sku = sku,
            subtitle = subtitle,
            desc = desc,
            flag = flag,
            price = price,
            image = image,
            category = category,
            brand = brand,
            video_url="https://youtu.be/uer_uSjItWM"

        )
    print(f'Successfully seeded {n} Product')



# seed_brand(10)
# seed_category(10)
seed_products(15)



