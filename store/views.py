from django.shortcuts import render
from .models import GPU, cpu, Cooler, Memory, PowerSupply, Case, Motherboard, RAM
from django.http import HttpResponse, HttpResponseNotFound
from .forms import GpuFilterForm, CpuFilterForm, CoolerFilterForm, PsuFilterForm, MotherboardFilterForm, MemoryFilterForm, CaseFilterForm, RamFilterForm
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

        if sertificate:
            psu = psu.filter(certificate__in=sertificate)

        if fans:
            psu = psu.filter(brand__in=fans)

        if price_min is not None:
            psu = psu.filter(price__gte=price_min)

        if price_max is not None:
            psu = psu.filter(price__lte=price_max)

        if watt_min is not None:
            psu = psu.filter(watt__gte=watt_min)

        if watt_max is not None:
            psu = psu.filter(watt__lte=watt_max)
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


def search_products(request):

    query = request.GET.get('search', '').strip()
    print(f"Search query: '{query}'")
    results = []
    CPU = cpu.objects.all()

    if query:
        # Ищем во всех категориях товаров
        cpus = cpu.objects.filter(
            Q(product_name__icontains=query) |
            Q(brand__icontains=query)

        )

        gpus = GPU.objects.filter(
            Q(product_name__icontains=query) |
            Q(brand__icontains=query)

        )

        motherboards = Motherboard.objects.filter(
            Q(product_name__icontains=query) |
            Q(brand__icontains=query) |
            Q(socket__icontains=query)
        )
        Coolers = Cooler.objects.filter(
            Q(product_name__icontains=query) |
            Q(brand__icontains=query)
            )

        Memorys = Memory.objects.filter(
            Q(product_name__icontains=query) |
            Q(brand__icontains=query)
            )

        PowerSupplyS = PowerSupply.objects.filter(
            Q(product_name__icontains=query) |
            Q(brand__icontains=query)
            )

        Cases = Case.objects.filter(
            Q(product_name__icontains=query) |
            Q(brand__icontains=query)
            )

        RAMS = RAM.objects.filter(
            Q(product_name__icontains=query) |
            Q(brand__icontains=query)
            )
        # Объединяем результаты
        results = list(cpus) + list(gpus) + list(motherboards)+ list(RAMS) + list(Cases) + list(PowerSupplyS) + list(Memorys) + list(Coolers)
        print(f"Total results: {len(results)}")
    return render(request, 'store/search_results.html', {'results': results, 'query': query, 'cpu': CPU})