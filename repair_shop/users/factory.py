import factory
from factory.django import DjangoModelFactory
from .models import Users


class UsersFactory(factory.Factory):
    class Meta:
        model = Users