# Senior Web Developer

1. Backend (Python y SQL)

## Backend
Esta parte evalúa tus conocimientos en diseño de software orientado a objetos usando el framework Django. Lo que necesitamos es lo siguiente:

Imagina que comienzas el desarrollo de InstantSalon. La funcionalidad principal es la generación de reservas por parte de los usuarios, contratando un determinado servicio en un salón. Las entidades que interactúan básicamente son las siguientes:

* Usuario (nombre, apellido, fecha de nacimiento, user, pass)
* Salón (Nombre, dirección)
* Servicio (Nombre, precio, duración)

Lo que necesitamos es que diseñes un servicio web que reciba la información necesaria para que el usuario genere una reserva. Los datos que contiene la reserva, así como el modelo, quedan a tu disposición para ser `supuestos`, es decir, si crees que falta información sobre los datos o el proceso, imagina que eres tú el dueño del producto y tú decides, solo necesitamos que dejes todas las suposiciones en comentarios dentro del código para poder entender tu razonamiento al diseñar la aplicación.

Recibirás puntos extra si creas el ambiente en docker para levantar el proyecto.
Además, cuéntanos qué cambios harías en el proyecto/infraestructura si sabes que recibirás un millón de request diarios (Esto lo respondi al final de este documento).

# Suponiendo el negocio

Dada esta información :
`InstantSalon te permite encontrar a tu profesional de la belleza ideal para reservar con él en el salón o pedir un delivery inmediato de sus servicios a domicilio.`
del link **http://lvs.meetliquid.com/career/fullstack-developer**
se creo los siguientes apps:

# Explicación de los modelos!

# Services (instasalon_test_django/services/models.py)
- Services (Servicios que ofrece Instasalon)
El modelo `Services` se refiere a los servicios que Instasalon ofrecera a sus clientes.

# Professional (instasalon_test_django/professional/models.py)
- Professional (profesionales de la belleza)
- ProfessionalService (servicios que ofrecen cada profesional de la belleza)

El modelo `Professional` se refiere a los trabajadores que realizan
la labor de Profesionales de la belleza.
El modelo `ProfessionalService` se refiere a los servicios que cada profesional
puede ofrecer.

# Rooms (instasalon_test_django/rooms/models.py)
- Rooms (Salones de la belleza, ubicados en diferentes puntos de alguna localidad)
- RoomProfessionalService (Servicios de cada Profesional que seran ofrecidos en cada salón)

El modelo `Rooms` se refiere a los salones que albergaran a los profesionales de la belleza.
El modelo `RoomProfessionalService` se refiere a los servicios que seran ofrecidos en los salones segun cada profesional de la belleza.

# Users (instasalon_test_django/users/models.py)
- Users
El modelo `Users` se refiere a los usuarios registrados que podran hacer uso de la reserva de servicios de Instasalon.

# Bookings (instasalon_test_django/bookings/models.py)
- Bookings
- BookingState
El modelo `Bookings` sera la tabla donde se almacenaran las reservas hechas por los clientes.
El modelo `BookingState` sera la tabla que identifique el estado en el que se encuentra la reserva (Si fue atendido, rechazado, o esta en espera).

# Que cambios haría en el proyecto/infraestructura si sabes que recibirás un millón de request diarios?
- Pues, a veces no todo depende del lenguaje de programación, asi este programado
con las mejores practicas del mundo, eso te no te garantiza que si un dia hay demasiada
concurrencia, tu codigo lo pueda sostener. Al realizar una aplicación web, para que la
performance sea correcta se necesita de un código bien hecho, de una base de datos bien normalizada, 
y lo mas importante que la arquitectura del servidor de aplicaciones donde estara
alojado sea de alta disponibilidad.
Para que sea de alta disponiblidad, se podria disponer de balanceadores de carga, el cual esto
es casi lo mismo que poner uno o varios servidores espejos, el cual el balanceador de carga
escogera a quien mandarle alguna petición que podria venir de la interacción del usuario 
con el sistema.
Para que se asegure aún mas la performance, se podria separar la aplicación web, 
de la base de datos, y poner cada uno en un servidor propio, y cada servidor implementaria
los balancedores de carga. Esto ya depende como es que tu aplicación consume la memoria del servidor.