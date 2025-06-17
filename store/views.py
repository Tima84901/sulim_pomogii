from django.shortcuts import render
from .models import GPU, cpu, Cooler, Memory, PowerSupply, Case, Motherboard, RAM
from django.http import HttpResponse, HttpResponseNotFound
from .forms import GpuFilterForm, CpuFilterForm, CoolerFilterForm, PsuFilterForm, MotherboardFilterForm, MemoryFilterForm, CaseFilterForm, RamFilterForm, SearchForm
from django.template.loader import render_to_string
from django.db.models import Q

# Create your views here.
def index(request):
    data = {'title': 'Главная страница'}
    return render(request, 'store/index.html', data)

def categories(request, cat_id):
    return HttpResponse("kat 1")

def about(request):   ### раздел "О сайте"
    return render(request, 'store/about.html', {'title': 'О нас'})

def page_not_found(request, exception):
    return HttpResponseNotFound("<h1>Страница не найдена</h1>")

def warranty(request):   ### раздел Гарантия"
    return render(request, 'store/warranty.html')

def delivery(request):   ### раздел "О сайте"
    return render(request, 'store/delivery.html')

def contacts(request):   ### раздел "О сайте"
    return render(request, 'store/contacts.html')

def gpu(request):
    gpu = GPU.objects.all()

    form = GpuFilterForm(request.GET or None)


    if form.is_valid():
        search = form.cleaned_data.get('search')
        memory = form.cleaned_data.get('memory')
        interface = form.cleaned_data.get('interface')
        fans = form.cleaned_data.get('fans')
        price_min = form.cleaned_data.get('price_min')
        price_max = form.cleaned_data.get('price_max')

        if search:
            gpu = gpu.filter(name__icontains=search)

        if memory:
            gpu = gpu.filter(vram__in=memory)

        if interface:
            gpu = gpu.filter(pci__in=interface)

        if fans:
            gpu = gpu.filter(brand__in=fans)

        if price_min is not None:
            gpu = gpu.filter(price__gte=price_min)

        if price_max is not None:
            gpu = gpu.filter(price__lte=price_max)
    context = {
        'form': form,
        'gpu': gpu,
    }
    return render(request, 'store/gpu.html', context)



def cpus(request):
    CPU = cpu.objects.all()
    form = CpuFilterForm(request.GET or None)

    if form.is_valid():
        socket = form.cleaned_data.get('socket')
        cores = form.cleaned_data.get('cores')
        fans = form.cleaned_data.get('fans')
        price_min = form.cleaned_data.get('price_min')
        price_max = form.cleaned_data.get('price_max')

        if socket:
            CPU = CPU.filter(socket__in=socket)

        if cores:
            CPU = CPU.filter(cores__in=cores)

        if fans:
            CPU = CPU.filter(brand__in=fans)

        if price_min is not None:
            CPU = CPU.filter(price__gte=price_min)

        if price_max is not None:
            CPU = CPU.filter(price__lte=price_max)

    context = {
        'form': form,
        'cpu': CPU,
    }
    return render(request, 'store/cpu.html', context)

def cooler(request):
    cooler = Cooler.objects.all()
    form = CoolerFilterForm(request.GET or None)
    if form.is_valid():
        socket = form.cleaned_data.get('socket')
        cooler_type = form.cleaned_data.get('cooler_type')
        fans = form.cleaned_data.get('fans')

        price_min = form.cleaned_data.get('price_min')
        price_max = form.cleaned_data.get('price_max')

        if socket:
            cooler = cooler.filter(socket__in=socket)

        if cooler_type:
            cooler = cooler.filter(cooler_type__in=cooler_type)

        if fans:
            cooler = cooler.filter(brand__in=fans)


        if price_min is not None:
            cooler = cooler.filter(price__gte=price_min)

        if price_max is not None:
            cooler = cooler.filter(price__lte=price_max)

    context = {
        'form': form,
        'cooler': cooler,
    }
    return render(request, 'store/cooler.html', context)

def memory(request):
    memory = Memory.objects.all()
    form = MemoryFilterForm(request.GET or None)
    if form.is_valid():
        digital_storage = form.cleaned_data.get('digital_storage')
        interface_pci = form.cleaned_data.get('interface_pci')
        fans = form.cleaned_data.get('fans')

        price_min = form.cleaned_data.get('price_min')
        price_max = form.cleaned_data.get('price_max')

        if digital_storage:
            memory = memory.filter(digital_storage__in=digital_storage)

        if interface_pci:
            memory = memory.filter(interface_pci__in=interface_pci)

        if fans:
            memory = memory.filter(brand__in=fans)

        if price_min is not None:
            memory = memory.filter(price__gte=price_min)

        if price_max is not None:
            memory = memory.filter(price__lte=price_max)

    context = {
        'form': form,
        'memory': memory,
    }
    return render(request, 'store/memory.html', context)



def psu(request):
    psu = PowerSupply.objects.all()
    form = PsuFilterForm(request.GET or None)

    if form.is_valid():

        sertificate = form.cleaned_data.get('sertificate')
        fans = form.cleaned_data.get('fans')
        price_min = form.cleaned_data.get('price_min')
        price_max = form.cleaned_data.get('price_max')
        watt_min = form.cleaned_data.get('watt_min')
        watt_max = form.cleaned_data.get('watt_max')
        watt = form.cleaned_data.get('watt')
        if sertificate:
            psu = psu.filter(certificate__in=sertificate)

        if fans:
            psu = psu.filter(brand__in=fans)

        if price_min is not None:
            psu = psu.filter(price__gte=price_min)

        if price_max is not None:
            psu = psu.filter(price__lte=price_max)

        if watt is not None:
            psu = psu.filter(watt__gte=watt)


    context = {
        'form': form,
        'psu': psu,
    }
    return render(request, 'store/psu.html', context)

def case(request):
    case = Case.objects.all()
    form = CaseFilterForm(request.GET or None)
    if form.is_valid():
        type_size = form.cleaned_data.get('type_size')
        form_factor = form.cleaned_data.get('form_factor')
        fans = form.cleaned_data.get('fans')

        price_min = form.cleaned_data.get('price_min')
        price_max = form.cleaned_data.get('price_max')

        if type_size:
            case = case.filter(type_size__in=type_size)

        if form_factor:
            case = case.filter(form_factor__in=form_factor)

        if fans:
            case = case.filter(brand__in=fans)

        if price_min is not None:
            case = case.filter(price__gte=price_min)

        if price_max is not None:
            case = case.filter(price__lte=price_max)
    else:
        print(form.errors)
    context = {
        'form': form,
        'case': case,
    }
    return render(request, 'store/case.html', context)

def motherboard(request):
    motherboard = Motherboard.objects.all()
    form = MotherboardFilterForm(request.GET or None)
    if form.is_valid():
        socket = form.cleaned_data.get('socket')
        form_factor = form.cleaned_data.get('form_factor')
        fans = form.cleaned_data.get('fans')

        price_min = form.cleaned_data.get('price_min')
        price_max = form.cleaned_data.get('price_max')

        if socket:
            motherboard = motherboard.filter(socket__in=socket)

        if form_factor:
            motherboard = motherboard.filter(form_factor__in=form_factor)

        if fans:
            motherboard = motherboard.filter(brand__in=fans)

        if price_min is not None:
            motherboard = motherboard.filter(price__gte=price_min)

        if price_max is not None:
            motherboard = motherboard.filter(price__lte=price_max)

    context = {
        'form': form,
        'motherboard': motherboard,
    }
    return render(request, 'store/motherboard.html', context)


def ram(request):
    ram = RAM.objects.all()
    form = RamFilterForm(request.GET or None)
    if form.is_valid():
        memory_type = form.cleaned_data.get('memory_type')
        memory = form.cleaned_data.get('memory')
        fans = form.cleaned_data.get('fans')

        price_min = form.cleaned_data.get('price_min')
        price_max = form.cleaned_data.get('price_max')

        if memory_type:
            ram = ram.filter(memory_type__in=memory_type)

        if memory:
            ram = ram.filter(memory__in=memory)

        if fans:
            ram = ram.filter(brand__in=fans)

        if price_min is not None:
            ram = ram.filter(price__gte=price_min)

        if price_max is not None:
            ram = ram.filter(price__lte=price_max)

    context = {
        'form': form,
        'ram': ram,
    }
    return render(request, 'store/ram.html', context)



def detect_category(query):
    query_lower = query.lower()


    if any(kw in query_lower for kw in ['i3', 'i5', 'i7', 'i9', 'ryzen', 'intel', '12400', '9800x3d', '13100']):
        return 'cpu'


    elif any(kw in query_lower for kw in ['rtx', 'gtx', 'rx', 'geforce', 'radeon', '5060','4069','7700','4070']):
        return 'GPU'


    elif any(kw in query_lower for kw in ['motherboard', 'mobo', 'b550', 'z490', 'a520']):
        return 'Motherboard'

    elif any(kw in query_lower for kw in ['корпус', 'h510', 'ck560', 'inwin', 'define']):
        return 'case'

    elif any(kw in query_lower for kw in ['оперативная память', 'ram', 'g skill', 'viper', 'fury']):
        return 'ram'

    elif any(kw in query_lower for kw in ['бп', 'straight power', 'supernova', 'focus', 'rm750', 'блок питания', 650, '750', 850]):
        return 'psu'

    elif any(kw in query_lower for kw in ['ssd', 'ссд', 'adata', 'samsung', 'a2000']):
        return 'memory'

    elif any(kw in query_lower for kw in ['frozn', 'hyper', 'nh', 'dark', 'water']):
        return 'cooler'
    else:
        return None


def search_products(request):
    query = request.GET.get('search', '').strip()
    cat = None
    results = []
    filter_form = None

    # Инициализация всех queryset
    gpus = GPU.objects.filter(
        Q(product_name__icontains=query) |
        Q(brand__icontains=query)
    )
    cpus = cpu.objects.filter(
        Q(product_name__icontains=query) |
        Q(brand__icontains=query)
    )
    motherboards = Motherboard.objects.filter(
        Q(product_name__icontains=query) |
        Q(brand__icontains=query) |
        Q(socket__icontains=query)
    )
    rams = RAM.objects.filter(
        Q(product_name__icontains=query) |
        Q(brand__icontains=query)
    )
    psus = PowerSupply.objects.filter(
        Q(product_name__icontains=query) |
        Q(brand__icontains=query)
    )
    cases = Case.objects.filter(
        Q(product_name__icontains=query) |
        Q(brand__icontains=query)
    )
    memorys = Memory.objects.filter(
        Q(product_name__icontains=query) |
        Q(brand__icontains=query)
    )
    coolers = Cooler.objects.filter(
        Q(product_name__icontains=query) |
        Q(brand__icontains=query)
    )

    # Определяем категорию и применяем фильтры
    if gpus.exists():
        cat = 'gpu'
        filter_form = GpuFilterForm(request.GET or None)
        results = gpus

        if filter_form.is_valid():
            data = filter_form.cleaned_data

            # Фильтрация по памяти (если поле раскомментировано)
            if 'memory' in filter_form.fields and data.get('memory'):
                results = results.filter(vram__in=data['memory'])

            # Фильтрация по интерфейсу (если поле раскомментировано)
            if 'interface' in filter_form.fields and data.get('interface'):
                results = results.filter(pci__in=data['interface'])

            # Фильтрация по бренду (fans)
            if data.get('fans'):
                results = results.filter(brand__in=data['fans'])

            # Фильтрация по цене
            if data.get('price_min'):
                results = results.filter(price__gte=data['price_min'])
            if data.get('price_max'):
                results = results.filter(price__lte=data['price_max'])

    elif cpus.exists():
        cat = 'cpu'
        filter_form = CpuFilterForm(request.GET or None)
        results = cpus

        if filter_form.is_valid():
            data = filter_form.cleaned_data

            if 'socket' in filter_form.fields and data.get('socket'):
                results = results.filter(socket__in=data['socket'])

            if 'cores' in filter_form.fields and data.get('cores'):
                results = results.filter(cores__in=data['cores'])

            if data.get('fans'):
                results = results.filter(brand__in=data['fans'])

            if data.get('price_min'):
                results = results.filter(price__gte=data['price_min'])
            if data.get('price_max'):
                results = results.filter(price__lte=data['price_max'])

    # Аналогичные блоки для остальных категорий (motherboard, ram, psu, case, memory, cooler)
    # Шаблон такой же, меняются только названия полей

    elif motherboards.exists():
        cat = 'motherboard'
        filter_form = MotherboardFilterForm(request.GET or None)
        results = motherboards

        if filter_form.is_valid():
            data = filter_form.cleaned_data

            if data.get('socket'):
                results = results.filter(socket__in=data['socket'])

            if data.get('form_factor'):
                results = results.filter(form_factor__in=data['form_factor'])

            if data.get('fans'):
                results = results.filter(brand__in=data['fans'])

            if data.get('price_min'):
                results = results.filter(price__gte=data['price_min'])
            if data.get('price_max'):
                results = results.filter(price__lte=data['price_max'])

    elif rams.exists():
        cat = 'ram'
        filter_form = RamFilterForm(request.GET or None)
        results = rams

        if filter_form.is_valid():
            data = filter_form.cleaned_data

            if data.get('memory_type'):
                results = results.filter(memory_type__in=data['memory_type'])

            if data.get('memory'):
                results = results.filter(one_module_memory__in=data['memory'])

            if data.get('fans'):
                results = results.filter(brand__in=data['fans'])

            if data.get('price_min'):
                results = results.filter(price__gte=data['price_min'])
            if data.get('price_max'):
                results = results.filter(price__lte=data['price_max'])

    elif psus.exists():
        cat = 'psu'
        filter_form = PsuFilterForm(request.GET or None)
        results = psus

        if filter_form.is_valid():
            data = filter_form.cleaned_data

            if data.get('sertificate'):
                results = results.filter(certificate__in=data['sertificate'])

            if data.get('fans'):
                results = results.filter(brand__in=data['fans'])

            if data.get('watt'):
                results = results.filter(wattage__gte=data['watt'])

            if data.get('price_min'):
                results = results.filter(price__gte=data['price_min'])
            if data.get('price_max'):
                results = results.filter(price__lte=data['price_max'])




    elif cases.exists():
        cat = 'case'
        filter_form = CaseFilterForm(request.GET or None)
        results = cases

        if filter_form.is_valid():
            data = filter_form.cleaned_data

            if data.get('type_size'):
                results = results.filter(type_size__in=data['type_size'])

            if data.get('form_factor'):
                results = results.filter(form_factor__in=data['form_factor'])

            if data.get('fans'):
                results = results.filter(brand__in=data['fans'])

            if data.get('price_min'):
                results = results.filter(price__gte=data['price_min'])
            if data.get('price_max'):
                results = results.filter(price__lte=data['price_max'])

    elif memorys.exists():
        cat = 'memory'
        filter_form = MemoryFilterForm(request.GET or None)
        results = memorys

        if filter_form.is_valid():
            data = filter_form.cleaned_data

            if data.get('digital_storage'):
                results = results.filter(digital_storage__in=data['digital_storage'])

            if data.get('interface_pci'):
                results = results.filter(interface_pci__in=data['interface_pci'])

            if data.get('fans'):
                results = results.filter(brand__in=data['fans'])

            if data.get('price_min'):
                results = results.filter(price__gte=data['price_min'])
            if data.get('price_max'):
                results = results.filter(price__lte=data['price_max'])

    elif coolers.exists():
        cat = 'cooler'
        filter_form = CoolerFilterForm(request.GET or None)
        results = coolers

        if filter_form.is_valid():
            data = filter_form.cleaned_data

            if data.get('socket'):
                results = results.filter(socket__in=data['socket'])

            if data.get('cooler_type'):
                results = results.filter(cooler_type__in=data['cooler_type'])

            if data.get('fans'):
                results = results.filter(brand__in=data['fans'])

            if data.get('price_min'):
                results = results.filter(price__gte=data['price_min'])
            if data.get('price_max'):
                results = results.filter(price__lte=data['price_max'])

    return render(request, 'store/search_results.html', {
        'query': query,
        'category': cat,
        'results': results,
        'form': filter_form,
    })

def azov(request):
    return render(request, 'store/product.html')
