from django.db.models import Count
import datetime

from student.models import Student, Group, Group_Student
from .models import Product


def distribution(student_id: int, product_id: int) -> str:
    #Запросы к БД
    product = Product.objects.get(pk=product_id) #Получаем продукт
    groups = Group.objects.filter(product_id=product_id)# Получаем список групп, которые относятся к продукту
    check_group = list(map(lambda x: x.pk, groups))# вытаскиваем индексы групп
    check_student = Group_Student.objects.filter(student_id=student_id, group__in=groups)# Вытаскиваем группы курса, к которым студент может относиться

    # Проверка на наличие доступа к продукту
    if check_student:
        if check_student[0].visibility:
            return f'У студента уже есть курс {product.title}'
        else:
            return f'Студент востановлен ан курсе'

    # Получаем кол-во студентов в каждой группе
    student_group = list(Group_Student.objects.select_related('group').filter(group__in=check_group, visibility=True).values(
        'group_id').annotate(count=Count('visibility')))

    #Получаем flag о старте продукта True - стартовал, иначе False
    sgtTimeDelta = datetime.timedelta(hours=0)
    sgtTZObject = datetime.timezone(sgtTimeDelta, name="SGT")
    flag_start = product.date_start > datetime.datetime.now().astimezone(sgtTZObject)

    # Получаем информацию о максимальных и минимальных размерах групп,
    # А так же переменная min_count, которая поможет найти группу с минимальным кол-вом людей (index_group, count)
    size_group = (getattr(product, 'min_size_group'), getattr(product, 'max_size_group'))
    min_count = (-1, size_group[1])

    # Поиск групп, где нет людей и минимального кол-ва людей в группе
    for element in student_group:
        check_group.remove(element['group_id']) # Удаляем непустые группы
        if element['count'] < min_count[1]:
            min_count = element.values()

    #Распределение на группы, если курс ещё не начался
    if flag_start:
        # Если в переменной check_group есть индексы, значит человека кидаем в пустую группу
        if check_group:
            min_count = (check_group[0],0)
        group_student = Group_Student(group_id=min_count[0], student_id=student_id)

    # Если курс начался, то людей раскидываем по непустым группам
    else:
        count_not_full = len(groups)
        for element in student_group:
            # Проверяем группу на заполненность
            if element['count'] == size_group[1]:
                count_not_full -= 1
                continue

            # Сначала заполняем недоборы в группах
            if element['count'] < size_group[0]:
                group_student = Group_Student(group_id=element['group_id'], student_id=student_id)
                break

        #Теперь раскидываем равномерно в непустых группах.
        else:
            # Проверка на заполненность групп
            if min_count[1] == size_group[1]:
                # Проверка на наличие пустых групп
                if check_group:
                    group_student = Group_Student(group_id=check_group[0], student_id=student_id)
                else:
                    return 'Все группы заполнены'
            else:
                group_student = Group_Student(group_id=min_count[0], student_id=student_id)

    group_student.save()
    return 'Студент добавлен'
