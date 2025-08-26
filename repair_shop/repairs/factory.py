from factory.django import DjangoModelFactory
import factory
from factory.faker import faker
from .models import Company , Device

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
    
class DeviceFactory(DjangoModelFactory):
    class Meta:
        model = Device
        
    brand = factory.Faker('name')
    device_name = factory.Faker('name')
    part_number = factory.Faker('password')
    serial_number = factory.Faker('password')
    complain = factory.Faker('text')
    description = factory.Faker('text')
    #created_by = factory.Faker('pyint', min_value=1, max_value=3) 
    shipped_from = factory.Faker("address")
    phone_numnber = factory.Faker("phone_number")
    postal_code = factory.Faker("postcode")