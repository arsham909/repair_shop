from factory.django import DjangoModelFactory
import factory
from factory.faker import faker
from .models import Company

class CompanyFactory(DjangoModelFactory):
    class Meta:
        model = Company
        
    name = factory.Sequence(lambda n: f"Company {n}")  
    address = factory.Faker("address")
    phonenumber = factory.Faker("phone_number")
    postal_code = factory.Faker("postcode")
    notes = factory.Faker("sentence", nb_words=10) 
    email = factory.Faker("company_email")
    contact_person = factory.Faker("name")
    is_active = True