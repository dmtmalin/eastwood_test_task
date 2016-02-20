from employees.forms import EmployeeFilter
from employees.models import Employee


def get_minded_filter(request):
    f = request.GET
    if bool(request.GET):
        request.session['filter'] = f
    else:
        f = request.session.get('filter', request.GET)
    return EmployeeFilter(f, queryset=Employee.objects.all().order_by('surname'))
