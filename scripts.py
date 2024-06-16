from datacenter.models import Schoolkid, Mark, Chastisement, Lesson


def get_schoolkid(full_name):
    try:
        schoolkid = Schoolkid.objects.get(full_name__contains=full_name)
        return schoolkid
    except Schoolkid.DoesNotExist:
        print(f'Ученик {full_name} не существует')
    except Schoolkid.MultipleObjectsReturned:
        print(f'Найдено несколько учеников с именем {full_name}')
    return None


def fix_marks(full_name):
    schoolkid = get_schoolkid(full_name)
    if not schoolkid:
        return None
    for mark in Mark.objects.filter(schoolkid=schoolkid, points__in=[2, 3]):
        mark.points = 5
        mark.save()


def remove_chastisements(full_name):
    schoolkid = get_schoolkid(full_name)
    if not schoolkid:
        return None
    chastisements = Chastisement.objects.filter(schoolkid=schoolkid)
    chastisements.delete()


def create_commendation(full_name, lesson):
    schoolkid = get_schoolkid(full_name)
    if not schoolkid:
        return None

    lesson = Lesson.objects.filter(year_of_study=6, group_letter='А', subject__title='Математика').first()

    Commendation.objects.create(text='Хвалю!', created=lesson.date, schoolkid=schoolkid, subject=lesson.subject, teacher=lesson.teacher)

