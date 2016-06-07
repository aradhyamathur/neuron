from django.core.management.base import BaseCommand
from model_mommy import mommy
from customsearch.models import University, Course, Students
import random
import names


class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('count', nargs=1, type=int)

    def handle(self, *args, **options):

        print 'creating dummy data'
        self.clear_db()
        self.make_universities()
        self.make_courses()
        self.make_students(options)
        self.connect_courses()

    def make_universities(self):
        university_names = ('MIT', 'MGU', 'Caltech', 'KPI', 'DPI', 'PSTU')
        self.universities = []
        for name in university_names:
            uni = mommy.make(University, name=name)
            self.universities.append(uni)

    def make_courses(self):
        template_options = ['CS%s0%s', 'MATH%s0%s', 'CHEM%s0%s', 'PHY%s0%s']
        self.courses = []
        for num in range(1, 4):
            for course_num in range(1, 4):
                for template in template_options:
                    name = template % (course_num, num)
                    course = mommy.make(Course, name=name)
                    self.courses.append(course)

    def make_students(self, options):
        self.students = []
        for _ in xrange(options.get('count')[0]):
            stud = mommy.prepare(
                Students,
                university=random.choice(self.universities),
                first_name=names.get_first_name(),
                last_name=names.get_last_name(),
                age=random.randint(17, 25)
            )
            self.students.append(stud)
        Students.objects.bulk_create(self.students)

    def connect_courses(self):
        ThroughModel = Students.courses.through
        stud_courses = []
        for student_id in Students.objects.values_list('pk', flat=True):
            courses_already_taken = []
            for _ in range(random.randint(0, 10)):
                index = random.randint(0, len(self.courses)-1)
                if index not in courses_already_taken:
                    courses_already_taken.append(index)
                else:
                    continue
                stud_courses.append(
                    ThroughModel(
                        id=student_id,
                        course_id=self.courses[index].pk
                    )
                )
            ThroughModel.objects.bulk_create(stud_courses)

    def clear_db(self):
        Students.objects.all().delete()
        University.objects.all().delete()
        Course.objects.all().delete()
