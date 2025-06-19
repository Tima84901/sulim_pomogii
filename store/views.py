from django.shortcuts import render, get_object_or_404
from .models import GPU, cpu, Cooler, Memory, PowerSupply, Case, Motherboard, RAM
from django.http import HttpResponse, HttpResponseNotFound, Http404
from .forms import GpuFilterForm, CpuFilterForm, CoolerFilterForm, PsuFilterForm, MotherboardFilterForm, MemoryFilterForm, CaseFilterForm, RamFilterForm, SearchForm
from django.template.loader import render_to_string, select_template
from django.db.models import Q
import logging
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
    qs = GPU.objects.all()
    form = GpuFilterForm(request.GET or None)

    if form.is_valid():
        data = form.cleaned_data
        if data['search']:    qs = qs.filter(product_name__icontains=data['search'])
        if data['memory']:    qs = qs.filter(vram__in=data['memory'])
        if data['interface']: qs = qs.filter(pci__in=data['interface'])
        if data['fans']:      qs = qs.filter(brand__in=data['fans'])
        if data['price_min']: qs = qs.filter(price__gte=data['price_min'])
        if data['price_max']: qs = qs.filter(price__lte=data['price_max'])

    return render(request, 'store/gpu.html',
                  {'form': form, 'products': qs})



def cpus(request):
    # CPU = cpu.objects.all()
    # form = CpuFilterForm(request.GET or None)
    # if form.is_valid():
    #     socket = form.cleaned_data.get('socket')
    #     cores = form.cleaned_data.get('cores')
    #     fans = form.cleaned_data.get('fans')
    #     price_min = form.cleaned_data.get('price_min')
    #     price_max = form.cleaned_data.get('price_max')
    #
    #     if socket:
    #         CPU = CPU.filter(socket__in=socket)
    #
    #     if cores:
    #         CPU = CPU.filter(cores__in=cores)
    #
    #     if fans:
    #         CPU = CPU.filter(brand__in=fans)
    #
    #     if price_min is not None:
    #         CPU = CPU.filter(price__gte=price_min)
    #
    #     if price_max is not None:
    #         CPU = CPU.filter(price__lte=price_max)
    #
    # context = {
    #     'form': form,
    #     'cpu': CPU,
    #     'component': 'cpu',
    #
    # }
    # return render(request, 'store/cpu.html', context)
    qs = cpu.objects.all()
    form = CpuFilterForm(request.GET or None)

    if form.is_valid():
        data = form.cleaned_data
        if data['socket']:     qs = qs.filter(socket__in=data['socket'])
        if data['cores']:      qs = qs.filter(cores__in=data['cores'])
        if data['fans']:       qs = qs.filter(brand__in=data['fans'])
        if data['price_min']:  qs = qs.filter(price__gte=data['price_min'])
        if data['price_max']:  qs = qs.filter(price__lte=data['price_max'])

    return render(request, 'store/cpu.html',
                  {'form': form, 'products': qs})

def cooler(request):
    qs = Cooler.objects.all()
    form = CoolerFilterForm(request.GET or None)

    if form.is_valid():
        data = form.cleaned_data
        if data['socket']:       qs = qs.filter(socket__in=data['socket'])
        if data['cooler_type']:  qs = qs.filter(cooler_type__in=data['cooler_type'])
        if data['fans']:         qs = qs.filter(brand__in=data['fans'])
        if data['price_min']:    qs = qs.filter(price__gte=data['price_min'])
        if data['price_max']:    qs = qs.filter(price__lte=data['price_max'])

    return render(request, 'store/cooler.html',
                  {'form': form, 'products': qs})

def memory(request):
    qs = Memory.objects.all()
    form = MemoryFilterForm(request.GET or None)

    if form.is_valid():
        data = form.cleaned_data
        if data['digital_storage']: qs = qs.filter(digital_storage__in=data['digital_storage'])
        if data['interface_pci']:   qs = qs.filter(interface_pci__in=data['interface_pci'])
        if data['fans']:            qs = qs.filter(brand__in=data['fans'])
        if data['price_min']:       qs = qs.filter(price__gte=data['price_min'])
        if data['price_max']:       qs = qs.filter(price__lte=data['price_max'])

    return render(request, 'store/memory.html',
                  {'form': form, 'products': qs})



def psu(request):
    qs = PowerSupply.objects.all()
    form = PsuFilterForm(request.GET or None)

    if form.is_valid():
        data = form.cleaned_data
        if data['sertificate']: qs = qs.filter(certificate__in=data['sertificate'])
        if data['fans']:        qs = qs.filter(brand__in=data['fans'])
        if data['watt']:        qs = qs.filter(wattage__gte=data['watt'])
        if data['price_min']:   qs = qs.filter(price__gte=data['price_min'])
        if data['price_max']:   qs = qs.filter(price__lte=data['price_max'])

    return render(request, 'store/psu.html',
                  {'form': form, 'products': qs})


def case(request):
    qs = Case.objects.all()
    form = CaseFilterForm(request.GET or None)

    if form.is_valid():
        data = form.cleaned_data
        if data['type_size']:   qs = qs.filter(type_size__in=data['type_size'])
        if data['form_factor']: qs = qs.filter(form_factor__in=data['form_factor'])
        if data['fans']:        qs = qs.filter(brand__in=data['fans'])
        if data['price_min']:   qs = qs.filter(price__gte=data['price_min'])
        if data['price_max']:   qs = qs.filter(price__lte=data['price_max'])

    return render(request, 'store/case.html',
                  {'form': form, 'products': qs})

def motherboard(request):
    qs = Motherboard.objects.all()
    form = MotherboardFilterForm(request.GET or None)

    if form.is_valid():
        data = form.cleaned_data
        if data['socket']:      qs = qs.filter(socket__in=data['socket'])
        if data['form_factor']: qs = qs.filter(form_factor__in=data['form_factor'])
        if data['fans']:        qs = qs.filter(brand__in=data['fans'])
        if data['price_min']:   qs = qs.filter(price__gte=data['price_min'])
        if data['price_max']:   qs = qs.filter(price__lte=data['price_max'])

    return render(request, 'store/motherboard.html',
                  {'form': form, 'products': qs})


def ram(request):
    qs = RAM.objects.all()
    form = RamFilterForm(request.GET or None)

    if form.is_valid():
        data = form.cleaned_data
        if data['memory_type']: qs = qs.filter(memory_type__in=data['memory_type'])
        if data['memory']:      qs = qs.filter(memory__in=data['memory'])
        if data['fans']:        qs = qs.filter(brand__in=data['fans'])
        if data['price_min']:   qs = qs.filter(price__gte=data['price_min'])
        if data['price_max']:   qs = qs.filter(price__lte=data['price_max'])

    return render(request, 'store/ram.html',
                  {'form': form, 'products': qs})




def search_products(request):
    query = request.GET.get('search', '').strip()
    category = request.GET.get('category', '').strip()
    filter_form = None
    results = []

    # Подготовка слов из запроса
    keywords = query.lower().split()

    # Получение queryset'ов с учетом ключевых слов
    def keyword_filter(model, *fields):
        q_objects = Q()
        for word in keywords:
            for field in fields:
                q_objects |= Q(**{f"{field}__icontains": word})
        return model.objects.filter(q_objects)

    gpus = keyword_filter(GPU, 'product_name', 'brand')
    cpus = keyword_filter(cpu, 'product_name', 'brand')
    motherboards = keyword_filter(Motherboard, 'product_name', 'brand', 'socket')
    rams = keyword_filter(RAM, 'product_name', 'brand')
    psus = keyword_filter(PowerSupply, 'product_name', 'brand')
    cases = keyword_filter(Case, 'product_name', 'brand')
    memorys = keyword_filter(Memory, 'product_name', 'brand')
    coolers = keyword_filter(Cooler, 'product_name', 'brand')

    # Определяем категорию, если не указана
    if not category:
        if cpus.exists():
            category = 'cpu'
        elif gpus.exists():
            category = 'gpu'
        elif motherboards.exists():
            category = 'motherboard'
        elif rams.exists():
            category = 'ram'
        elif psus.exists():
            category = 'psu'
        elif cases.exists():
            category = 'case'
        elif memorys.exists():
            category = 'memory'
        elif coolers.exists():
            category = 'cooler'

    # Применяем фильтры к выбранной категории
    if category == 'cpu':
        results = cpus
        filter_form = CpuFilterForm(request.GET)
        if filter_form.is_valid():
            data = filter_form.cleaned_data
            if data.get('socket'):
                results = results.filter(socket__in=data['socket'])
            if data.get('cores'):
                results = results.filter(cores__in=data['cores'])
            if data.get('fans'):
                results = results.filter(brand__in=data['fans'])
            if data.get('price_min'):
                results = results.filter(price__gte=data['price_min'])
            if data.get('price_max'):
                results = results.filter(price__lte=data['price_max'])

    elif category == 'gpu':
        results = gpus
        filter_form = GpuFilterForm(request.GET)
        if filter_form.is_valid():
            data = filter_form.cleaned_data
            if data.get('memory'):
                results = results.filter(vram__in=data['memory'])
            if data.get('interface'):
                results = results.filter(pci__in=data['interface'])
            if data.get('fans'):
                results = results.filter(brand__in=data['fans'])
            if data.get('price_min'):
                results = results.filter(price__gte=data['price_min'])
            if data.get('price_max'):
                results = results.filter(price__lte=data['price_max'])

    elif category == 'motherboard':
        results = motherboards
        filter_form = MotherboardFilterForm(request.GET)
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

    elif category == 'ram':
        results = rams
        filter_form = RamFilterForm(request.GET)
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

    elif category == 'psu':
        results = psus
        filter_form = PsuFilterForm(request.GET)
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

    elif category == 'case':
        results = cases
        filter_form = CaseFilterForm(request.GET)
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

    elif category == 'memory':
        results = memorys
        filter_form = MemoryFilterForm(request.GET)
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

    elif category == 'cooler':
        results = coolers
        filter_form = CoolerFilterForm(request.GET)
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
        'results': results,
        'query': query,
        'category': category,
        'form': filter_form,
    })
MODEL_MAP = {
    'cpu': cpu,
    'gpu': GPU,
    'ram': RAM,
    'psu': PowerSupply,
    'powersupply': PowerSupply,
    'cooler': Cooler,
    'memory': Memory,
    'case': Case,
    'motherboard': Motherboard

}
logger = logging.getLogger(__name__)
def component_detail(request, component, pk):
    logger.warning(f"component_detail called with component={component}, pk={pk}")
    Model = MODEL_MAP.get(component)
    if Model is None:
        logger.error(f"MODEL_MAP does not contain component={component}")
        raise Http404("Component not found")

    product = get_object_or_404(Model, pk=pk)

    related = Model.objects.exclude(pk=pk)[:4]
    logger.warning(f"Found product: {product}")
    template = select_template([
        f"store/product_detail/{component}_product_detail.html",
        "store/product_detail/product_detail.html",
    ])
    logging.warning("USING template=%s", template.template.name)

    return render(request, template.template.name,
                  {'product': product, 'related': related})
