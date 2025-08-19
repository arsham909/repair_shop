# inventory/factories.py
import factory
from factory import  fuzzy


from .models import InventoryItem


class InventoryItemFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = InventoryItem

    name = factory.Faker('word')
    part_number = factory.Sequence(lambda n: f"PART-{n:04d}")
    quantity = fuzzy.FuzzyInteger(1, 100)
    description = factory.Faker('sentence', nb_words=6)
    location = factory.Faker('word')
    
    # Use a random choice from the Category enum
    category = fuzzy.FuzzyChoice([choice[0] for choice in InventoryItem.Category.choices])
    
    is_active = True
    trigger = fuzzy.FuzzyInteger(0, 10)