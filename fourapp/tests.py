from django.test import TestCase
from fourapp.models import *


class Category(TestCase):
    def setUp(self):
        Category.objects.create(name="name")
        Category.objects.create(name="alias")

    def shcaf(self):
        name = Category.objects.get(name="name")
        alias = Category.objects.get(name="alias")