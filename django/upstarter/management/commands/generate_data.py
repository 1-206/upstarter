import random
import faker

from django.core.management.base import BaseCommand

from upstarter.models import User, Project


def random_choice(array, start=1, end=5):
    "Function for random choice with random len"
    out = set(random.choice(array) for _ in range(random.randint(start, end)))
    return list(out)


def generate_text(length=100):
    fake = faker.Faker('en_US')
    return fake.text(length)


def generate_projects(amount=10, min_name_len=2, max_name_len=3, min_tag_len=3,
                      max_tag_len=7, min_invest=100, max_invest=10000,
                      text_len=500):
    projects = []
    with open('upstarter/management/project_names.txt', 'r') as f:
        names = [i.strip() for i in f.readlines()]
    with open('upstarter/management/tags.txt', 'r') as f:
        _tags = [i.strip() for i in f.readlines()]
    for _ in range(amount):
        name = ''.join(random_choice(names, min_name_len, max_name_len))
        tags = ' '.join(random_choice(_tags, min_tag_len, max_tag_len))
        required_investments = random.randint(min_invest, max_invest)
        text = generate_text(text_len)
        projects.append({
            'name': name,
            'tags': tags,
            'description': text,
            'required_investments': required_investments
        })
    return projects


def generate_name():
    fake = faker.Faker('en_US')
    return fake.name().split()[0]


def generate_persons(amount=10, min_len_skills=3, max_len_skills=6):
    persons = []
    with open('upstarter/management/skills.txt', 'r') as f:
        _skills = [i.strip() for i in f.readlines()]
    for _ in range(amount):
        name = generate_name()
        surname = generate_name()
        email = faker.Faker().email()
        skills = ' '.join(
            random_choice(_skills, min_len_skills, max_len_skills))
        location = faker.Faker().country()
        birthday = faker.Faker().date()
        biography = generate_text(200)
        persons.append({
            'name': name,
            'surname': surname,
            'email': email,
            'skills': skills,
            'location': location,
            'birthday': birthday,
            'biography': biography,
        })
    return persons


class Command(BaseCommand):
    help = "Fills database with randomly generated data"

    def handle(self, *args, **options):
        # Create users
        users_data = generate_persons(amount=100)
        users = [
            User.objects.create_user(
                password='qwerty123',
                **user_data,
            ) for user_data in users_data
        ]

        # Create projects
        projects_data = generate_projects(amount=10000)
        Project.objects.bulk_create(
            Project(
                founder=random.choice(users),
                **project_data,
            ) for project_data in projects_data
        )
