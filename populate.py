import os, django
import random

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "instasalon_test.settings")
django.setup()

from django_seed import Seed
from professional.models import Professional, ProfessionalService
from rooms.models import Rooms, RoomProfessionalService
from services.models import Services
from users.models import Users

populator = Seed.seeder()

particular_data = {
    'nombre': lambda x: populator.faker.name(),
    'apellido_paterno': lambda x: populator.faker.name(),
    'apellido_materno': lambda x: populator.faker.name(),
    'edad': lambda x: random.randint(18, 100),
}

populator.add_entity(Rooms, 10)
populator.add_entity(Services, 6)
populator.add_entity(Users, 20, {**particular_data,
                                 **{'usuario': lambda x: populator.faker.email(),
                                    'password': lambda x: '123456'}})
populator.add_entity(Professional, 20, particular_data)

insertedPks = populator.execute()

# llenando servicios de profesionales, y rooms de profesionales servicios
profesionals = Professional.objects.all()
services = Services.objects.all()
rooms = Rooms.objects.all()

for p in profesionals:
    for s in services:
        ps = ProfessionalService()
        ps.profesional = p
        ps.service = s
        ps.save()

profesionalservices = ProfessionalService.objects.all()
for ps in profesionalservices:
    for r in rooms:
        psr = RoomProfessionalService()
        psr.profesional_service = ps
        psr.room = r
        psr.save()
