from core import models
from django.db.models import Q


def query_all_states():
    all_states = models.State.objects.all()
    print(all_states)


def query_values_employee():
    all_values_employee = models.Zone.objects.values('id', 'name', 'created_at')
    print(all_values_employee)


def query_states_order_by_name():
    all_states = models.State.objects.order_by('name')
    print(all_states)


def query_states_order_by_name_desc():
    all_states = models.State.objects.order_by('-name')
    print(all_states)


def query_customer_order_by_name_and_income():
    all_customers = models.Customer.objects.order_by('name', '-income').values('name', 'income')
    print(all_customers)


def get_employee_ana_luiza():
    result = models.Employee.objects.filter(name='Ana Luiza Cunha')
    print(result)


def get_employee_by_pk():
    result = models.Employee.objects.filter(pk=42)
    print(result)


def get_employee_by_id():
    result = models.Employee.objects.filter(id=42)
    print(result)


def get_customer_by_gender():
    result = models.Customer.objects.filter(gender=models.Customer.Gender.MALE)
    print(result)


def get_salary_gt_2000():
    result = models.Employee.objects.filter(salary__gt=2000).order_by('salary').values('name', 'salary')
    print(result)


def get_male_employees_salary_gte_2284():
    result = (models.Employee.objects
              .filter(salary__gte=2284, gender=models.Customer.Gender.MALE)
              .order_by('salary').values('name', 'salary'))
    print(result)


def get_salary_range():
    conditions = Q()
    conditions.add(Q(salary__gte=2000), Q.AND)
    result = models.Employee.objects.filter(conditions).values('name', 'salary')
    print(result)
