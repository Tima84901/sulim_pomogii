# forms.py
from django import forms

class GpuFilterForm(forms.Form):

    memory = forms.MultipleChoiceField(
        required=False,
        widget=forms.CheckboxSelectMultiple,
        choices=[


            ('8GB', '8 ГБ'),
            ('12GB', '12 ГБ'),
            ('16GB', '16 ГБ')
        ]
    )
    interface = forms.MultipleChoiceField(
        required=False,
        widget=forms.CheckboxSelectMultiple,
        choices=[
            ('PCIe 4.0', 'PCI-E 4.0'),
            ('PCIe 5.0', 'PCI-E 5.0'),
        ]
    )
    fans = forms.MultipleChoiceField(
        required=False,
        widget=forms.CheckboxSelectMultiple,
        choices=[
            ('NVIDIA', 'NVIDIA'),
            ('AMD', 'AMD'),
        ]
    )
    price_min = forms.FloatField(
        required=False,
        widget=forms.NumberInput(attrs={'placeholder': 'Минимальная цена'}),
    )
    price_max = forms.FloatField(
        required=False,
        widget=forms.NumberInput(attrs={'placeholder': 'Максимальная цена'}),
    )


class CpuFilterForm(forms.Form):

    socket = forms.MultipleChoiceField(
        required=False,
        widget=forms.CheckboxSelectMultiple,
        choices=[


            ('LGA 1700', 'LGA 1700'),
            ('AM4', 'AM4'),
            ('AM5', 'AM5')
        ]
    )
    cores = forms.MultipleChoiceField(
        required=False,
        widget=forms.CheckboxSelectMultiple,
        choices=[
            (4, '4'),
            (6, '6'),
            (8, '8'),
        ]
    )
    fans = forms.MultipleChoiceField(
        required=False,
        widget=forms.CheckboxSelectMultiple,
        choices=[
            ('INTEL', 'Intel'),
            ('AMD', 'AMD'),
        ]
    )
    price_min = forms.FloatField(
        required=False,
        widget=forms.NumberInput(attrs={'placeholder': 'Минимальная цена'}),
    )
    price_max = forms.FloatField(
        required=False,
        widget=forms.NumberInput(attrs={'placeholder': 'Максимальная цена'}),
    )

class CoolerFilterForm(forms.Form):

    socket = forms.MultipleChoiceField(
        required=False,
        widget=forms.CheckboxSelectMultiple,
        choices=[


            ('LGA 1151', 'LGA 1151'),
            ('AM4', 'AM4'),
            ('LGA 1200', 'LGA 1200')
        ]
    )
    cooler_type = forms.MultipleChoiceField(
        required=False,
        widget=forms.CheckboxSelectMultiple,
        choices=[
            ('Воздушное охлаждение', 'Воздушное охлаждение'),
            ('Водяное охлаждение', 'Водяное охлаждение'),

        ]
    )
    fans = forms.MultipleChoiceField(
        required=False,
        widget=forms.CheckboxSelectMultiple,
        choices=[
            ('ID-COOLING', 'ID-COOLING'),
            ('Cooler Master', 'Cooler Master'),
            ('Noctua', 'Noctua'),
            ('Corsair', 'Corsair'),
            ('be quiet!', 'be quiet!'),
            ('Thermaltake', 'Thermaltake'),
        ]
    )

    price_min = forms.FloatField(
        required=False,
        widget=forms.NumberInput(attrs={'placeholder': 'Минимальная цена'}),
    )
    price_max = forms.FloatField(
        required=False,
        widget=forms.NumberInput(attrs={'placeholder': 'Максимальная цена'}),
    )

class PsuFilterForm(forms.Form):

    sertificate = forms.MultipleChoiceField(
        required=False,
        widget=forms.CheckboxSelectMultiple,
        choices=[
            ('80 PLUS Gold', '80+ GOLD'),
            ('80 PLUS Platinum', '80+ PLATINUM'),
        ]
    )
    fans = forms.MultipleChoiceField(
        required=False,
        widget=forms.CheckboxSelectMultiple,
        choices=[
            ('Corsair', 'Corsair'),
            ('Seasonic', 'Seasonic'),
            ('EVGA', 'EVGA'),
            ('Cooler Master', 'Cooler Master'),
            ('be quiet!', 'be quiet!'),
        ]
    )
    watt = forms.MultipleChoiceField(
        required=False,
        widget=forms.CheckboxSelectMultiple,
        choices=[
            (650, '650'),
            (750, '750'),
            (850, '850'),

        ]
    )
    price_min = forms.FloatField(
        required=False,
        widget=forms.NumberInput(attrs={'placeholder': 'Минимальная цена'}),
    )
    price_max = forms.FloatField(
        required=False,
        widget=forms.NumberInput(attrs={'placeholder': 'Максимальная цена'}),
    )





class MotherboardFilterForm(forms.Form):

    socket = forms.MultipleChoiceField(
        required=False,
        widget=forms.CheckboxSelectMultiple,
        choices=[


            ('AM5', 'AM5'),
            ('AM4', 'AM4'),
            ('LGA1700', 'LGA 1700')
        ]
    )
    form_factor = forms.MultipleChoiceField(
        required=False,
        widget=forms.CheckboxSelectMultiple,
        choices=[
            ('ATX', 'ATX'),
            ('E-ATX', 'E-ATX'),

        ]
    )
    fans = forms.MultipleChoiceField(
        required=False,
        widget=forms.CheckboxSelectMultiple,
        choices=[
            ('ASUS', 'ASUS'),
            ('Gigabyte', 'Gigabyte'),
            ('MSI', 'MSI'),
            ('ASRock', 'ASRock'),

        ]
    )

    price_min = forms.FloatField(
        required=False,
        widget=forms.NumberInput(attrs={'placeholder': 'Минимальная цена'}),
    )
    price_max = forms.FloatField(
        required=False,
        widget=forms.NumberInput(attrs={'placeholder': 'Максимальная цена'}),
    )


class MemoryFilterForm(forms.Form):

    digital_storage = forms.MultipleChoiceField(
        required=False,
        widget=forms.CheckboxSelectMultiple,
        choices=[


            (250, '250 ГБ'),
            (500, '500 ГБ'),
            (1000, '1000 ГБ'),
        ]
    )
    interface_pci = forms.MultipleChoiceField(
        required=False,
        widget=forms.CheckboxSelectMultiple,
        choices=[
            ('PCIe 4.0', 'PCIe 4.0'),
            ('NVMe PCIe 3.0', 'NVMe PCIe 3.0'),
            ('SATA III', 'SATA III'),

        ]
    )
    fans = forms.MultipleChoiceField(
        required=False,
        widget=forms.CheckboxSelectMultiple,
        choices=[
            ('ADATA', 'ADATA'),
            ('Samsung', 'Samsung'),
            ('Crucial', 'Crucial'),
            ('Western Digital', 'Western Digital'),
            ('Kingston', 'Kingston'),

        ]
    )

    price_min = forms.FloatField(
        required=False,
        widget=forms.NumberInput(attrs={'placeholder': 'Минимальная цена'}),
    )
    price_max = forms.FloatField(
        required=False,
        widget=forms.NumberInput(attrs={'placeholder': 'Максимальная цена'}),
    )

class CaseFilterForm(forms.Form):

    type_size = forms.MultipleChoiceField(
        required=False,
        widget=forms.CheckboxSelectMultiple,
        choices=[

            ('Mini Tower', 'Mini Tower'),
            ('Mid Tower', 'Mid Tower'),
            ('Full Tower', 'Full Tower'),
        ]
    )
    form_factor = forms.MultipleChoiceField(
        required=False,
        widget=forms.CheckboxSelectMultiple,
        choices=[
            ('ATX', 'ATX'),
            ('E-ATX', 'E-ATX'),
            ('Micro-ATX', 'Micro-ATX'),

        ]
    )
    fans = forms.MultipleChoiceField(
        required=False,
        widget=forms.CheckboxSelectMultiple,
        choices=[
            ('NZXT', 'NZXT'),
            ('Fractal Design', 'Fractal Design'),
            ('Deepcool', 'Deepcool'),
            ('InWin', 'InWin'),


        ]
    )

    price_min = forms.FloatField(
        required=False,
        widget=forms.NumberInput(attrs={'placeholder': 'Минимальная цена'}),
    )
    price_max = forms.FloatField(
        required=False,
        widget=forms.NumberInput(attrs={'placeholder': 'Максимальная цена'}),
    )

class RamFilterForm(forms.Form):

    memory_type = forms.MultipleChoiceField(
        required=False,
        widget=forms.CheckboxSelectMultiple,
        choices=[

            ('DDR4', 'DDR4'),
            ('DDR5', 'DDR5'),

        ]
    )
    memory = forms.MultipleChoiceField(
        required=False,
        widget=forms.CheckboxSelectMultiple,
        choices=[
            (16, '16'),
            (32, '32'),

        ]
    )
    fans = forms.MultipleChoiceField(
        required=False,
        widget=forms.CheckboxSelectMultiple,
        choices=[
            ('Corsair', 'Corsair'),
            ('G.Skill', 'G.Skill'),
            ('Kingston', 'Kingston'),
            ('Patriot', 'Patriot'),


        ]
    )

    price_min = forms.FloatField(
        required=False,
        widget=forms.NumberInput(attrs={'placeholder': 'Минимальная цена'}),
    )
    price_max = forms.FloatField(
        required=False,
        widget=forms.NumberInput(attrs={'placeholder': 'Максимальная цена'}),
    )

class SearchForm(forms.Form):
    query = forms.CharField(label='Поиск', max_length=100)