from datacenter.models import Schoolkid, Mark, Chastisement, Lesson, Commendation
import random

commendation_text = ['Хвалю!', 'Молодец!', 'Старался']


def get_schoolkid(full_name):
    try:
        schoolkid = Schoolkid.objects.get(full_name__contains=full_name)
        return schoolkid
    except Schoolkid.DoesNotExist:
        print(f'Ученик {full_name} не существует')
    except Schoolkid.MultipleObjectsReturned:
        print(f'Найдено несколько учеников с именем {full_name}')
    return None


def get_lesson(schoolkid, subject):
    try:
        lessons = Lesson.objects.get(
            year_of_study=schoolkid.year_of_study,
            group_letter=schoolkid.group_letter,
            subject__title=subject
        ).order_by('-date')
        return lessons.first()
    except Lesson.DoesNotExist:
        print('Такой предмет не существует')
    return None


def fix_marks(full_name):
    schoolkid = get_schoolkid(full_name)
    if not schoolkid:
        return None
    Mark.objects.filter(schoolkid=schoolkid, points__in=[2, 3]).update(points=5)


def remove_chastisements(full_name):
    schoolkid = get_schoolkid(full_name)
    if not schoolkid:
        return None
    chastisements = Chastisement.objects.filter(schoolkid=schoolkid)
    chastisements.delete()


def create_commendation(full_name, subject):
    schoolkid = get_schoolkid(full_name)
    if not schoolkid:
        return None

    lesson = get_lesson(schoolkid, subject)
    if not lesson:
        return None

    Commendation.objects.create(
        text=random.choice(commendation_text),
        created=lesson.date,
        schoolkid=schoolkid,
        subject=lesson.subject,
        teacher=lesson.teacher
    )
