from django.db import models
from django.urls import reverse
from django.contrib.contenttypes.models import ContentType
from store.mixins import WithContentTypeMixin
class ComponentURLMixin(models.Model):

    class Meta:
        abstract = True

    def get_absolute_url(self):
        return reverse('component_detail',
                       args=[self._meta.model_name, self.pk])

class GPU(WithContentTypeMixin, ComponentURLMixin, models.Model):

    category = models.CharField(max_length=20, null=True)
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
    article = models.CharField(null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)  # Цена в валюте
    image = models.ImageField(upload_to='store/images/')
    performance_score = models.PositiveIntegerField(
        default=0, help_text="Synthetic benchmark index"
    )
    length_mm = models.PositiveIntegerField(
        default=0, help_text="Card length, mm (for case compatibility)"
    )
    power_draw_w = models.PositiveIntegerField(
        default=0, help_text="Typical board power (W)"
    )
    ray_tracing_support = models.BooleanField(default=False)
    release_year = models.PositiveIntegerField(null=True, blank=True)
    def __str__(self):
        return f"{self.brand} {self.gpu_brand} - {self.product_name}"

class cpu(WithContentTypeMixin, ComponentURLMixin, models.Model):
    category = models.CharField(max_length=20, null=True)
    product_name = models.CharField(max_length=100, unique=True)  # Название продукта
    brand = models.CharField(max_length=100)  # Бренд процессора
    product_line = models.CharField(max_length=100)  # Линейка продуктов
    socket = models.CharField(max_length=50)  # Тип сокета
    cores = models.PositiveIntegerField()  # Количество ядер
    potok = models.PositiveIntegerField()  # Количество потоков
    cpu_clock = models.PositiveIntegerField()  # Тактовая частота в МГц
    warranty = models.IntegerField()  # Гарантия в месяцах
    article = models.CharField(null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)  # Цена в валюте
    tdp = models.IntegerField(null=True)
    image = models.ImageField(upload_to='store/images/', null=True)
    benchmark_score = models.PositiveIntegerField(
        default=0, help_text="Synthetic benchmark index"
    )
    integrated_graphics = models.BooleanField(default=False)
    release_year = models.PositiveIntegerField(null=True, blank=True)
    lithography_nm = models.PositiveIntegerField(null=True, blank=True)


    def __str__(self):
        return f"{self.brand} {self.product_name}"


class Cooler(WithContentTypeMixin, ComponentURLMixin, models.Model):
    category = models.CharField(max_length=20, null=True)
    brand = models.CharField(max_length=100)  # Бренд
    product_name = models.CharField(max_length=100)
    cooler_type = models.CharField(max_length=100)  # Тип кулера
    socket = models.CharField(max_length=50)  # Тип сокета
    tdp = models.PositiveIntegerField()  # TDP в ваттах
    cooler_size = models.CharField(max_length=50)  # Размер кулера
    connector_type = models.CharField(max_length=50)  # Тип подключения
    article = models.CharField(null=True)
    weight = models.DecimalField(max_digits=5, decimal_places=2)  # Вес в кг
    warranty = models.IntegerField()  # Гарантия в месяцах
    price = models.DecimalField(max_digits=10, decimal_places=2)  # Цена
    image = models.ImageField(upload_to='store/images/', null=True)
    height_mm = models.PositiveIntegerField(
        default=0, help_text="Cooler height for case clearance, mm"
    )
    noise_level_db = models.PositiveIntegerField(
        default=0, help_text="Noise level at max RPM, dB"
    )
    rgb = models.BooleanField(default=False)
    def __str__(self):
        return f"{self.brand} {self.cooler_type}"

class Memory(WithContentTypeMixin, ComponentURLMixin, models.Model):
    category = models.CharField(max_length=20, null=True)
    brand = models.CharField(max_length=100)  # Бренд
    memory_type = models.CharField(max_length=100)
    product_name = models.CharField(max_length=100)  # Название продукта
    interface_pci = models.CharField(max_length=50)  # Интерфейс PCI
    digital_storage = models.PositiveIntegerField()  # Объем в ГБ
    article = models.CharField(null=True)
    compatible_devices = models.CharField(max_length=200)  # Совместимые устройства
    warranty = models.IntegerField()  # Гарантия в месяцах
    price = models.DecimalField(max_digits=10, decimal_places=2)  # Цена
    image = models.ImageField(upload_to='store/images/', null=True)
    read_speed = models.PositiveIntegerField(
        default=0, help_text="Sequential read, MB/s"
    )
    write_speed = models.PositiveIntegerField(
        default=0, help_text="Sequential write, MB/s"
    )
    tbw = models.PositiveIntegerField(
        default=0, help_text="Endurance (Total Bytes Written), TB"
    )
    def __str__(self):
        return f"{self.brand} {self.product_name}"

class Motherboard(WithContentTypeMixin, ComponentURLMixin, models.Model):
    category = models.CharField(max_length=20, null=True)
    brand = models.CharField(max_length=100)  # Бренд
    product_name = models.CharField(max_length=100)  # Название продукта
    socket = models.CharField(max_length=50)  # Тип сокета
    chipset = models.CharField(max_length=100)  # Чипсет
    memory_type = models.CharField(max_length=50)  # Тип памяти
    article = models.CharField(null=True)
    form_factor = models.CharField(max_length=50)  # Форм-фактор
    warranty = models.IntegerField()  # Гарантия в месяцах
    price = models.DecimalField(max_digits=10, decimal_places=2)  # Цена
    image = models.ImageField(upload_to='store/images/', null=True)
    max_memory_gb = models.PositiveIntegerField(
        default=0, help_text="Maximum supported memory, GB"
    )
    m2_slots = models.PositiveIntegerField(default=0)
    pcie_version = models.CharField(
        max_length=10, default="4.0", help_text="Highest PCIe version supported"
    )
    wifi_onboard = models.BooleanField(default=False)
    max_ram_speed = models.PositiveIntegerField(
        default=0, help_text="Max RAM speed (MHz) without OC"
    )
    def __str__(self):
        return f"{self.brand} {self.product_name}"

class PowerSupply(WithContentTypeMixin, ComponentURLMixin, models.Model):
    category = models.CharField(max_length=20, null=True)
    brand = models.CharField(max_length=100)  # Бренд
    product_name = models.CharField(max_length=100)  # Название продукта
    wattage = models.PositiveIntegerField()  # Мощность в ваттах
    watt = models.IntegerField(null=True)
    formfactor = models.CharField(max_length=50)  # Форм-фактор
    pins = models.CharField(max_length=40, null=True)
    article = models.CharField(null=True)
    item_weight = models.DecimalField(max_digits=5, decimal_places=2)  # Вес в кг
    certificate = models.CharField(max_length=100)  # Сертификат
    warranty = models.IntegerField()  # Гарантия в месяцах
    price = models.DecimalField(max_digits=10, decimal_places=2)  # Цена

    image = models.ImageField(upload_to='store/images/', null=True)
    efficiency_rating = models.CharField(
        max_length=20,
        default="80+ Bronze",
        help_text="Efficiency certificate label",
    )
    modular = models.BooleanField(default=False)
    pcie_8pin_count = models.PositiveIntegerField(default=0)
    length_mm = models.PositiveIntegerField(
        default=0, help_text="PSU length for case compatibility"
    )
    def __str__(self):
        return f"{self.brand} {self.product_name}"

class Case(WithContentTypeMixin, ComponentURLMixin, models.Model):

    category = models.CharField(max_length=20, null=True)
    brand = models.CharField(max_length=100)  # Бренд
    product_name = models.CharField(max_length=100)  # Название продукта
    type_size = models.CharField(max_length=50)  # Размер корпуса
    form_factor = models.CharField(max_length=50)  # Форм-фактор
    psu_place = models.CharField(max_length=50)  # Место для БП
    body_material = models.CharField(max_length=50)  # Материал корпуса
    coolers_in = models.PositiveIntegerField()  # Количество кулеров
    article = models.CharField(null=True)
    size = models.CharField(max_length=50)  # Размер
    warranty = models.IntegerField()  # Гарантия в месяцах
    price = models.DecimalField(max_digits=10, decimal_places=2)  # Цена
    image = models.ImageField(upload_to='store/images/', null=True)
    max_gpu_length_mm = models.PositiveIntegerField(
        default=0, help_text="Max GPU length supported, mm"
    )
    max_cooler_height_mm = models.PositiveIntegerField(
        default=0, help_text="Max CPU cooler height, mm"
    )
    max_psu_length_mm = models.PositiveIntegerField(
        default=0, help_text="Max PSU length, mm"
    )
    drive_slots_25 = models.PositiveIntegerField(
        default=0, help_text="Number of 2.5'' drive mounts"
    )
    drive_slots_35 = models.PositiveIntegerField(
        default=0, help_text="Number of 3.5'' drive bays"
    )
    front_radiator_support = models.BooleanField(default=False)
    rgb_lighting = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.brand} {self.product_name}"

class RAM(WithContentTypeMixin, ComponentURLMixin, models.Model):
    category = models.CharField(max_length=20, null=True)
    brand = models.CharField(max_length=100)  # Бренд
    product_name = models.CharField(max_length=100)  # Название продукта
    form_factor = models.CharField(max_length=50)  # Форм-фактор
    memory_type = models.CharField(max_length=50)  # Тип памяти
    memory = models.PositiveIntegerField()  # Объем в ГБ
    one_module_memory = models.PositiveIntegerField()  # Объем одной планки в ГБ
    moduls_in = models.PositiveIntegerField()  # Количество модулей
    hertz = models.PositiveIntegerField()  # Частота в МГц
    article = models.CharField(null=True)
    timings = models.CharField(max_length=50)  # Тайминги
    xmp_support = models.BooleanField(default=False)  # Поддержка XMP
    price = models.DecimalField(max_digits=10, decimal_places=2, default=3000)
    image = models.ImageField(upload_to='store/images/', null=True)
    latency_cl = models.PositiveIntegerField(
        default=0, help_text="CAS latency (CL) value"
    )
    voltage = models.DecimalField(
        max_digits=4,
        decimal_places=2,
        default=1.35,
        help_text="Operating voltage, V",
    )
    ecc = models.BooleanField(default=False)
    def __str__(self):
        return f"{self.brand} {self.product_name}"


 # JSON правила совместимости