# INSTASALON TEST

- run migrations
`python manage.py migrate`

- cargar fixture
`python manage.py loaddata fixture.json`

- correr django
`python manage.py run server`

- entrar a: **http:localhost:8000**
y se podra ver los servicios creados

- para crear una reserva, entrar a **http://localhost:8000/bookings/**
y hacer un POST, este servicio esta validado para que las reservas no se crucen con otras.
(**`instasalon_test_django/bookings/serializers.py linea 28`**)




