from django.db import models

class GPU(models.Model):
    product_name = models.CharField(max_length=100, unique=True)  # Идентификатор продукта
    vram = models.CharField(max_length=100)  # Объём видеопамяти в МБ
    brand = models.CharField(max_length=100)  # Бренд устройства
    gpu_brand = models.CharField(max_length=100)  # Бренд GPU
    pci = models.CharField(max_length=50)  # Тип PCI (например, PCIe 4.0)
    vram_type = models.CharField(max_length=50)  # Тип видеопамяти (например, GDDR6)
    memory_interface = models.CharField(max_length=100)  # Ширина шины памяти в битах
    output_type = models.CharField(max_length=100)  # Типы выходов (например, HDMI, DisplayPort)
    gpu_clock = models.CharField(max_length=100)  # Тактовая частота GPU в МГц
    warranty = models.CharField(max_length=100)  # Гарантия в месяцах
    dlss = models.CharField(max_length=20, null=True)
    fg = models.CharField(max_length=30, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)  # Цена в валюте
    image = models.ImageField(upload_to='store/images/')

    def __str__(self):
        return f"{self.brand} {self.gpu_brand} - {self.product_name}"

class cpu(models.Model):
    product_name = models.CharField(max_length=100, unique=True)  # Название продукта
    brand = models.CharField(max_length=100)  # Бренд процессора
    product_line = models.CharField(max_length=100)  # Линейка продуктов
    socket = models.CharField(max_length=50)  # Тип сокета
    cores = models.PositiveIntegerField()  # Количество ядер
    potok = models.PositiveIntegerField()  # Количество потоков
    cpu_clock = models.PositiveIntegerField()  # Тактовая частота в МГц
    warranty = models.IntegerField()  # Гарантия в месяцах
    price = models.DecimalField(max_digits=10, decimal_places=2)  # Цена в валюте
    tdp = models.IntegerField(null=True)
    image = models.ImageField(upload_to='store/images/', null=True)
    def __str__(self):
        return f"{self.brand} {self.product_name}"


class Cooler(models.Model):
    brand = models.CharField(max_length=100)  # Бренд
    product_name = models.CharField(max_length=100)
    cooler_type = models.CharField(max_length=100)  # Тип кулера
    socket = models.CharField(max_length=50)  # Тип сокета
    tdp = models.PositiveIntegerField()  # TDP в ваттах
    cooler_size = models.CharField(max_length=50)  # Размер кулера
    connector_type = models.CharField(max_length=50)  # Тип подключения
    weight = models.DecimalField(max_digits=5, decimal_places=2)  # Вес в кг
    warranty = models.IntegerField()  # Гарантия в месяцах
    price = models.DecimalField(max_digits=10, decimal_places=2)  # Цена
    image = models.ImageField(upload_to='store/images/', null=True)
    def __str__(self):
        return f"{self.brand} {self.cooler_type}"

class Memory(models.Model):
    brand = models.CharField(max_length=100)  # Бренд
    memory_type = models.CharField(max_length=100)
    product_name = models.CharField(max_length=100)  # Название продукта
    interface_pci = models.CharField(max_length=50)  # Интерфейс PCI
    digital_storage = models.PositiveIntegerField()  # Объем в ГБ
    compatible_devices = models.CharField(max_length=200)  # Совместимые устройства
    warranty = models.IntegerField()  # Гарантия в месяцах
    price = models.DecimalField(max_digits=10, decimal_places=2)  # Цена
    image = models.ImageField(upload_to='store/images/', null=True)

    def __str__(self):
        return f"{self.brand} {self.product_name}"

class Motherboard(models.Model):
    brand = models.CharField(max_length=100)  # Бренд
    product_name = models.CharField(max_length=100)  # Название продукта
    socket = models.CharField(max_length=50)  # Тип сокета
    chipset = models.CharField(max_length=100)  # Чипсет
    memory_type = models.CharField(max_length=50)  # Тип памяти
    form_factor = models.CharField(max_length=50)  # Форм-фактор
    warranty = models.IntegerField()  # Гарантия в месяцах
    price = models.DecimalField(max_digits=10, decimal_places=2)  # Цена
    image = models.ImageField(upload_to='store/images/', null=True)
    def __str__(self):
        return f"{self.brand} {self.product_name}"

class PowerSupply(models.Model):
    brand = models.CharField(max_length=100)  # Бренд
    product_name = models.CharField(max_length=100)  # Название продукта
    wattage = models.PositiveIntegerField()  # Мощность в ваттах
    watt = models.IntegerField(null=True)
    formfactor = models.CharField(max_length=50)  # Форм-фактор
    pins = models.CharField(max_length=40, null=True)
    item_weight = models.DecimalField(max_digits=5, decimal_places=2)  # Вес в кг
    certificate = models.CharField(max_length=100)  # Сертификат
    warranty = models.IntegerField()  # Гарантия в месяцах
    price = models.DecimalField(max_digits=10, decimal_places=2)  # Цена

    image = models.ImageField(upload_to='store/images/', null=True)
    def __str__(self):
        return f"{self.brand} {self.product_name}"

class Case(models.Model):
    brand = models.CharField(max_length=100)  # Бренд
    product_name = models.CharField(max_length=100)  # Название продукта
    type_size = models.CharField(max_length=50)  # Размер корпуса
    form_factor = models.CharField(max_length=50)  # Форм-фактор
    psu_place = models.CharField(max_length=50)  # Место для БП
    body_material = models.CharField(max_length=50)  # Материал корпуса
    coolers_in = models.PositiveIntegerField()  # Количество кулеров
    size = models.CharField(max_length=50)  # Размер
    warranty = models.IntegerField()  # Гарантия в месяцах
    price = models.DecimalField(max_digits=10, decimal_places=2)  # Цена
    image = models.ImageField(upload_to='store/images/', null=True)
    def __str__(self):
        return f"{self.brand} {self.product_name}"

class RAM(models.Model):
    brand = models.CharField(max_length=100)  # Бренд
    product_name = models.CharField(max_length=100)  # Название продукта
    form_factor = models.CharField(max_length=50)  # Форм-фактор
    memory_type = models.CharField(max_length=50)  # Тип памяти
    memory = models.PositiveIntegerField()  # Объем в ГБ
    one_module_memory = models.PositiveIntegerField()  # Объем одной планки в ГБ
    moduls_in = models.PositiveIntegerField()  # Количество модулей
    hertz = models.PositiveIntegerField()  # Частота в МГц
    timings = models.CharField(max_length=50)  # Тайминги
    xmp_support = models.BooleanField(default=False)  # Поддержка XMP
    image = models.ImageField(upload_to='store/images/', null=True)
    def __str__(self):
        return f"{self.brand} {self.product_name}"
