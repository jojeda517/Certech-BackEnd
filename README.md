<a name="pst-skip-link"></a>[Saltar al contenido principal](#main-content) 

Back to top <a name="__primary"></a> FORMCHECKBOX <a name="__secondary"></a> FORMCHECKBOX 

<a name="q"></a>*      Ctrl+K

[documentación de Certech - 1.0.0](index.html)

- [api package ]()
- [CertechBakend package ](CertechBakend.html)
- [CertechBakend ](modules.html)
- [api package ]()
- [CertechBakend package ](CertechBakend.html)
- [CertechBakend ](modules.html)

Navegación del sección

- [CertechBakend package](CertechBakend.html)
- [api package]()
- [manage module](manage.html)
- [](index.html)
- api package
# <a name="api-package"></a>**api package[#**](#api-package "Link to this heading")**
## <a name="submodules"></a>**Submodules[#**](#submodules "Link to this heading")**
## <a name="module-api.models"></a>**api.models module[#**](#module-api.models "Link to this heading")**
*class* api.models.Administrador(*\*args*, *\*\*kwargs*)[#](#api.models.administrador "Link to this definition")

Bases: Model

Modelo para representar un administrador en el sistema.

Atributos:

- id\_administrador (AutoField): Identificador único del administrador (clave primaria). 
- usuario (CharField): Nombre de usuario del administrador.
- clave (CharField): Contraseña del administrador.
- cedula (CharField): Número de cédula del administrador.
- correo (CharField): Dirección de correo electrónico del administrador.
- celular (CharField): Número de teléfono celular del administrador.

Meta:

- managed (bool): Indica si Django manejará la creación de la tabla en la base de datos (False en este caso).
- db\_table (str): Nombre de la tabla en la base de datos (“administradores” en este caso).

Ejemplo de uso:

admin = Administrador( usuario=”nombre\_usuario”, clave=”contraseña\_segura”, cedula=”1234567890”, [correo=”admin@example.com](mailto:correo='admin%40example.com)”, celular=”1234567890” ) 

admin.save()

*exception* DoesNotExist[#](#api.models.administrador.doesnotexist "Link to this definition")

Bases: ObjectDoesNotExist

*exception* MultipleObjectsReturned[#](#api.models.administrador.multipleobjectsreturned "Link to this definition")

Bases: MultipleObjectsReturned

cedula[#](#api.models.administrador.cedula "Link to this definition")

A wrapper for a deferred-loading field. When the value is read from this object the first time, the query is executed.

celular[#](#api.models.administrador.celular "Link to this definition")

A wrapper for a deferred-loading field. When the value is read from this object the first time, the query is executed.

clave[#](#api.models.administrador.clave "Link to this definition")

A wrapper for a deferred-loading field. When the value is read from this object the first time, the query is executed.

correo[#](#api.models.administrador.correo "Link to this definition")

A wrapper for a deferred-loading field. When the value is read from this object the first time, the query is executed.

id\_administrador[#](#api.models.administrador.id_administrador "Link to this definition")

A wrapper for a deferred-loading field. When the value is read from this object the first time, the query is executed.

objects *= <django.db.models.manager.Manager object>[#](#api.models.administrador.objects "Link to this definition")*

usuario[#](#api.models.administrador.usuario "Link to this definition")

A wrapper for a deferred-loading field. When the value is read from this object the first time, the query is executed.

*class* api.models.Certificado(*\*args*, *\*\*kwargs*)[#](#api.models.certificado "Link to this definition")

Bases: Model

Modelo para representar un certificado en el sistema.

Atributos:

- id\_certificado (AutoField): Identificador único del certificado (clave primaria).
- id\_administrador (IntegerField): Identificador del administrador asociado al certificado.
- id\_participante (IntegerField): Identificador del participante asociado al certificado. 
- id\_evento (IntegerField): Identificador del evento asociado al certificado.
- id\_plantilla (IntegerField): Identificador de la plantilla asociada al certificado.
- fecha (DateTimeField): Fecha y hora de creación del certificado (se actualiza automáticamente al crear el certificado).
- url (CharField): Ruta o enlace al certificado.
- codigo\_unico (UUIDField): Código único asociado al certificado (generado automáticamente).

Meta:

- managed (bool): Indica si Django manejará la creación de la tabla en la base de datos (False en este caso).
- db\_table (str): Nombre de la tabla en la base de datos (“certificados” en este caso). 

Ejemplo de uso:

certificado = Certificado( id\_administrador=1, id\_participante=2, id\_evento=3, id\_plantilla=4, url=”ruta\_o\_enlace\_al\_certificado”, )

certificado.save()

*exception* DoesNotExist[#](#api.models.certificado.doesnotexist "Link to this definition")

Bases: ObjectDoesNotExist

*exception* MultipleObjectsReturned[#](#api.models.certificado.multipleobjectsreturned "Link to this definition")

Bases: MultipleObjectsReturned

codigo\_unico[#](#api.models.certificado.codigo_unico "Link to this definition")

A wrapper for a deferred-loading field. When the value is read from this object the first time, the query is executed.

fecha[#](#api.models.certificado.fecha "Link to this definition")

A wrapper for a deferred-loading field. When the value is read from this object the first time, the query is executed.

get\_next\_by\_fecha(*\**, *field=<django.db.models.fields.DateTimeField: fecha>*, *is\_next=True*, *\*\*kwargs*)[#](#api.models.certificado.get_next_by_fecha "Link to this definition")

get\_previous\_by\_fecha(*\**, *field=<django.db.models.fields.DateTimeField: fecha>*, *is\_next=False*, *\*\*kwargs*)[#](#api.models.certificado.get_previous_by_fecha "Link to this definition")

id\_administrador[#](#api.models.certificado.id_administrador "Link to this definition")

A wrapper for a deferred-loading field. When the value is read from this object the first time, the query is executed.

id\_certificado[#](#api.models.certificado.id_certificado "Link to this definition")

A wrapper for a deferred-loading field. When the value is read from this object the first time, the query is executed.

id\_evento[#](#api.models.certificado.id_evento "Link to this definition")

A wrapper for a deferred-loading field. When the value is read from this object the first time, the query is executed.

id\_participante[#](#api.models.certificado.id_participante "Link to this definition")

A wrapper for a deferred-loading field. When the value is read from this object the first time, the query is executed.

id\_plantilla[#](#api.models.certificado.id_plantilla "Link to this definition")

A wrapper for a deferred-loading field. When the value is read from this object the first time, the query is executed.

objects *= <django.db.models.manager.Manager object>[#](#api.models.certificado.objects "Link to this definition")*

url[#](#api.models.certificado.url "Link to this definition")

A wrapper for a deferred-loading field. When the value is read from this object the first time, the query is executed.

*class* api.models.Detalle\_Certificado(*\*args*, *\*\*kwargs*)[#](#api.models.detalle_certificado "Link to this definition")

Bases: Model

Modelo para representar los detalles asociados a un certificado en el sistema.

Atributos:

- id\_detalle (AutoField): Identificador único del detalle (clave primaria).
- id\_certificado (IntegerField): Identificador del certificado asociado al detalle.
- id\_firma (IntegerField): Identificador de la firma asociada al detalle.

Meta:

- managed (bool): Indica si Django manejará la creación de la tabla en la base de datos (False en este caso).
- db\_table (str): Nombre de la tabla en la base de datos (“detalle\_certificados” en este caso).

*exception* DoesNotExist[#](#api.models.detalle_certificado.doesnotexist "Link to this definition")

Bases: ObjectDoesNotExist

*exception* MultipleObjectsReturned[#](#api.models.detalle_certificado.multipleobjectsreturned "Link to this definition")

Bases: MultipleObjectsReturned

id\_certificado[#](#api.models.detalle_certificado.id_certificado "Link to this definition")

A wrapper for a deferred-loading field. When the value is read from this object the first time, the query is executed.

id\_detalle[#](#api.models.detalle_certificado.id_detalle "Link to this definition")

A wrapper for a deferred-loading field. When the value is read from this object the first time, the query is executed.

id\_firma[#](#api.models.detalle_certificado.id_firma "Link to this definition")

A wrapper for a deferred-loading field. When the value is read from this object the first time, the query is executed.

objects *= <django.db.models.manager.Manager object>[#](#api.models.detalle_certificado.objects "Link to this definition")*

*class* api.models.Evento(*\*args*, *\*\*kwargs*)[#](#api.models.evento "Link to this definition")

Bases: Model

Modelo para representar un evento en el sistema.

Atributos:

- id\_evento (AutoField): Identificador único del evento (clave primaria).
- nombre\_evento (CharField): Nombre del evento.
- tipo\_evento (CharField): Tipo o categoría del evento.
- descripcion\_evento (TextField): Descripción detallada del evento.
- portada (CharField): Ruta o enlace a la imagen de portada del evento.
- logo (CharField): Ruta o enlace al logo del evento.
- fecha\_creacion (DateTimeField): Fecha y hora de creación del evento (se actualiza automáticamente al crear el evento).

Meta:

- managed (bool): Indica si Django manejará la creación de la tabla en la base de datos (False en este caso).
- db\_table (str): Nombre de la tabla en la base de datos (“eventos” en este caso).

Ejemplo de uso:

evento = Evento( nombre\_evento=”Nombre del Evento”, tipo\_evento=”Tipo de Evento”, descripcion\_evento=”Descripción detallada del evento.”, portada=”ruta\_o\_enlace\_a\_la\_imagen\_de\_portada”, logo=”ruta\_o\_enlace\_al\_logo”, )

evento.save()

*exception* DoesNotExist[#](#api.models.evento.doesnotexist "Link to this definition")

Bases: ObjectDoesNotExist

*exception* MultipleObjectsReturned[#](#api.models.evento.multipleobjectsreturned "Link to this definition")

Bases: MultipleObjectsReturned

descripcion\_evento[#](#api.models.evento.descripcion_evento "Link to this definition")

A wrapper for a deferred-loading field. When the value is read from this object the first time, the query is executed.

fecha\_creacion[#](#api.models.evento.fecha_creacion "Link to this definition")

A wrapper for a deferred-loading field. When the value is read from this object the first time, the query is executed.

get\_next\_by\_fecha\_creacion(*\**, *field=<django.db.models.fields.DateTimeField: fecha\_creacion>*, *is\_next=True*, *\*\*kwargs*)[#](#api.models.evento.get_next_by_fecha_creacion "Link to this definition")

get\_previous\_by\_fecha\_creacion(*\**, *field=<django.db.models.fields.DateTimeField: fecha\_creacion>*, *is\_next=False*, *\*\*kwargs*)[#](#api.models.evento.get_previous_by_fecha_creacion "Link to this definition")

id\_evento[#](#api.models.evento.id_evento "Link to this definition")

A wrapper for a deferred-loading field. When the value is read from this object the first time, the query is executed.

logo[#](#api.models.evento.logo "Link to this definition")

A wrapper for a deferred-loading field. When the value is read from this object the first time, the query is executed.

nombre\_evento[#](#api.models.evento.nombre_evento "Link to this definition")

A wrapper for a deferred-loading field. When the value is read from this object the first time, the query is executed.

objects *= <django.db.models.manager.Manager object>[#](#api.models.evento.objects "Link to this definition")*

portada[#](#api.models.evento.portada "Link to this definition")

A wrapper for a deferred-loading field. When the value is read from this object the first time, the query is executed.

tipo\_evento[#](#api.models.evento.tipo_evento "Link to this definition")

A wrapper for a deferred-loading field. When the value is read from this object the first time, the query is executed.

*class* api.models.Firma(*\*args*, *\*\*kwargs*)[#](#api.models.firma "Link to this definition")

Bases: Model

Modelo para representar una firma en el sistema.

Atributos:

- id\_firma (AutoField): Identificador único de la firma (clave primaria).
- propietario\_firma (CharField): Nombre del propietario de la firma.
- cargo\_propietario (CharField): Cargo del propietario de la firma.
- firma (CharField): Representación de la firma (puede ser una ruta de archivo, URL o datos de imagen, dependiendo de la implementación).
- estado\_firma (CharField): Estado actual de la firma (por ejemplo, activa, inactiva, pendiente).

Meta:

- managed (bool): Indica si Django manejará la creación de la tabla en la base de datos (False en este caso).
- db\_table (str): Nombre de la tabla en la base de datos (“firmas” en este caso).

Ejemplo de uso:

firma = Firma( propietario\_firma=”Nombre Propietario”, cargo\_propietario=”Cargo del Propietario”, firma=”ruta\_o\_datos\_de\_firma”, estado\_firma=”Activa” )

firma.save()

*exception* DoesNotExist[#](#api.models.firma.doesnotexist "Link to this definition")

Bases: ObjectDoesNotExist

*exception* MultipleObjectsReturned[#](#api.models.firma.multipleobjectsreturned "Link to this definition")

Bases: MultipleObjectsReturned

cargo\_propietario[#](#api.models.firma.cargo_propietario "Link to this definition")

A wrapper for a deferred-loading field. When the value is read from this object the first time, the query is executed.

estado\_firma[#](#api.models.firma.estado_firma "Link to this definition")

A wrapper for a deferred-loading field. When the value is read from this object the first time, the query is executed.

firma[#](#api.models.firma.firma "Link to this definition")

A wrapper for a deferred-loading field. When the value is read from this object the first time, the query is executed.

id\_firma[#](#api.models.firma.id_firma "Link to this definition")

A wrapper for a deferred-loading field. When the value is read from this object the first time, the query is executed.

objects *= <django.db.models.manager.Manager object>[#](#api.models.firma.objects "Link to this definition")*

propietario\_firma[#](#api.models.firma.propietario_firma "Link to this definition")

A wrapper for a deferred-loading field. When the value is read from this object the first time, the query is executed.

*class* api.models.Participante(*\*args*, *\*\*kwargs*)[#](#api.models.participante "Link to this definition")

Bases: Model

Modelo para representar a un participante en el sistema.

Atributos:

- id\_participante (AutoField): Identificador único del participante (clave primaria).
- cedula (CharField): Número de cédula del participante.
- nombre\_apellido (CharField): Nombre y apellido del participante.
- celular (CharField): Número de teléfono celular del participante.
- correo (CharField): Dirección de correo electrónico del participante.

Meta:

- managed (bool): Indica si Django manejará la creación de la tabla en la base de datos (False en este caso).
- db\_table (str): Nombre de la tabla en la base de datos (“participantes” en este caso). 

Ejemplo de uso:

participante = Participante( cedula=”1234567890”, nombre\_apellido=”Nombre Apellido”, celular=”1234567890”, [correo=”participante@example.com](mailto:correo='participante%40example.com)” ) 

participante.save()

*exception* DoesNotExist[#](#api.models.participante.doesnotexist "Link to this definition")

Bases: ObjectDoesNotExist

*exception* MultipleObjectsReturned[#](#api.models.participante.multipleobjectsreturned "Link to this definition")

Bases: MultipleObjectsReturned

cedula[#](#api.models.participante.cedula "Link to this definition")

A wrapper for a deferred-loading field. When the value is read from this object the first time, the query is executed.

celular[#](#api.models.participante.celular "Link to this definition")

A wrapper for a deferred-loading field. When the value is read from this object the first time, the query is executed.

correo[#](#api.models.participante.correo "Link to this definition")

A wrapper for a deferred-loading field. When the value is read from this object the first time, the query is executed.

id\_participante[#](#api.models.participante.id_participante "Link to this definition")

A wrapper for a deferred-loading field. When the value is read from this object the first time, the query is executed.

nombre\_apellido[#](#api.models.participante.nombre_apellido "Link to this definition")

A wrapper for a deferred-loading field. When the value is read from this object the first time, the query is executed.

objects *= <django.db.models.manager.Manager object>[#](#api.models.participante.objects "Link to this definition")*

*class* api.models.Plantilla(*\*args*, *\*\*kwargs*)[#](#api.models.plantilla "Link to this definition")

Bases: Model

Modelo para representar una plantilla en el sistema.

Atributos:

- id\_plantilla (AutoField): Identificador único de la plantilla (clave primaria).
- plantilla (CharField): Ruta o enlace a la plantilla.

Meta:

- managed (bool): Indica si Django manejará la creación de la tabla en la base de datos (False en este caso).
- db\_table (str): Nombre de la tabla en la base de datos (“plantillas” en este caso).

Ejemplo de uso:

plantilla = Plantilla( plantilla=”ruta\_o\_enlace\_a\_la\_plantilla”, ) plantilla.save()

*exception* DoesNotExist[#](#api.models.plantilla.doesnotexist "Link to this definition")

Bases: ObjectDoesNotExist

*exception* MultipleObjectsReturned[#](#api.models.plantilla.multipleobjectsreturned "Link to this definition")

Bases: MultipleObjectsReturned

id\_plantilla[#](#api.models.plantilla.id_plantilla "Link to this definition")

A wrapper for a deferred-loading field. When the value is read from this object the first time, the query is executed.

objects *= <django.db.models.manager.Manager object>[#](#api.models.plantilla.objects "Link to this definition")*

plantilla[#](#api.models.plantilla.plantilla "Link to this definition")

A wrapper for a deferred-loading field. When the value is read from this object the first time, the query is executed.
## <a name="module-api.views"></a>**api.views module[#**](#module-api.views "Link to this heading")**
*class* api.views.AdministradorView(*\*\*kwargs*)[#](#api.views.administradorview "Link to this definition")

Bases: View

Vista para manejar operaciones relacionadas con administradores.

dispatch(*request*, *\*args*, *\*\*kwargs*)[#](#api.views.administradorview.dispatch "Link to this definition")

Despacha la solicitud, excluyendo la verificación CSRF.

get(*request*, *usuario=None*, *clave=None*)[#](#api.views.administradorview.get "Link to this definition")

Maneja las solicitudes GET para recuperar información sobre administradores.

Parámetros:

- **request** – Objeto de solicitud Django.
- **usuario** – Nombre de usuario (opcional).
- **clave** – Clave (opcional).

Devuelve:

JsonResponse con los datos del administrador o una respuesta de error.

*class* api.views.CertificadoParticipanteView(*\*\*kwargs*)[#](#api.views.certificadoparticipanteview "Link to this definition")

Bases: View

Vista para obtener los certificados asociados a un participante mediante su número de cédula. 

Métodos admitidos:

- GET: Obtiene la lista de certificados asociados al participante.

Atributos:

- NOT\_DATA\_MESSAGE (dict): Mensaje de respuesta cuando no se encuentra el participante o sus certificados.
- ERROR\_MESSAGE (dict): Mensaje de respuesta cuando ocurre un error durante la solicitud. 

dispatch(*request*, *\*args*, *\*\*kwargs*)[#](#api.views.certificadoparticipanteview.dispatch "Link to this definition")

Despacha la solicitud, excluyendo la verificación CSRF.

get(*request*, *cedula*)[#](#api.views.certificadoparticipanteview.get "Link to this definition")

Maneja las solicitudes GET para obtener la lista de certificados asociados a un participante mediante su número de cédula.

Parámetros:

- **request** – Objeto de solicitud Django.
- **cedula** – Número de cédula del participante.

Devuelve:

JsonResponse con la lista de certificados asociados al participante o una respuesta de error.

*class* api.views.CertificadoValidoView(*\*\*kwargs*)[#](#api.views.certificadovalidoview "Link to this definition")

Bases: View

Vista para verificar la validez de un certificado mediante su código único.

Métodos admitidos:

- GET: Obtiene detalles del certificado válido asociado al código único proporcionado. 

Atributos:

- NOT\_DATA\_MESSAGE (dict): Mensaje de respuesta cuando no se encuentra el certificado. 
- ERROR\_MESSAGE (dict): Mensaje de respuesta cuando ocurre un error durante la solicitud. 

dispatch(*request*, *\*args*, *\*\*kwargs*)[#](#api.views.certificadovalidoview.dispatch "Link to this definition")

Despacha la solicitud, excluyendo la verificación CSRF.

get(*request*, *codigo\_unico*)[#](#api.views.certificadovalidoview.get "Link to this definition")

Maneja las solicitudes GET para obtener detalles del certificado válido asociado al código único proporcionado.

Parámetros:

- **request** – Objeto de solicitud Django.
- **codigo\_unico** – Código único asociado al certificado.

Devuelve:

JsonResponse con detalles del certificado válido o una respuesta de error.

*class* api.views.CertificadoView(*\*\*kwargs*)[#](#api.views.certificadoview "Link to this definition")

Bases: View

Vista para manejar operaciones relacionadas con certificados.

Métodos admitidos:

- POST: Crea un nuevo certificado con las firmas proporcionadas y genera el certificado en formato PDF.

Atributos:

- ERROR\_MESSAGE (dict): Mensaje de respuesta cuando ocurre un error durante la solicitud. 

dispatch(*request*, *\*args*, *\*\*kwargs*)[#](#api.views.certificadoview.dispatch "Link to this definition")

Despacha la solicitud, excluyendo la verificación CSRF.

post(*request*, *id\_firma1*, *id\_firma2*)[#](#api.views.certificadoview.post "Link to this definition")

Maneja las solicitudes POST para crear un nuevo certificado con las firmas proporcionadas y generar el certificado en formato PDF.

Parámetros:

- **request** – Objeto de solicitud Django.
- **id\_firma1** – ID de la primera firma asociada al certificado.
- **id\_firma2** – ID de la segunda firma asociada al certificado.

Devuelve:

JsonResponse con detalles del certificado creado o una respuesta de error.

*class* api.views.EventoUpdate(*\*\*kwargs*)[#](#api.views.eventoupdate "Link to this definition")

Bases: View

Vista para manejar la actualización de eventos.

Métodos admitidos:

- POST: Actualiza un evento existente según el ID proporcionado.

Atributos:

- NOT\_DATA\_MESSAGE (dict): Mensaje de respuesta cuando no hay datos disponibles.
- ERROR\_MESSAGE (dict): Mensaje de respuesta cuando ocurre un error durante la solicitud. 
- SUCCESS\_MESSAGE (dict): Mensaje de respuesta exitosa.

dispatch(*request*, *\*args*, *\*\*kwargs*)[#](#api.views.eventoupdate.dispatch "Link to this definition")

Despacha la solicitud, excluyendo la verificación CSRF.

post(*request*, *id\_evento*)[#](#api.views.eventoupdate.post "Link to this definition")

Maneja las solicitudes POST para actualizar un evento existente.

Parámetros:

- **request** – Objeto de solicitud Django.
- **id\_evento** – ID del evento a actualizar.

Devuelve:

JsonResponse con detalles del evento actualizado o una respuesta de error.

*class* api.views.EventoView(*\*\*kwargs*)[#](#api.views.eventoview "Link to this definition")

Bases: View

Vista para manejar operaciones relacionadas con eventos.

Métodos admitidos:

- GET: Recupera información sobre eventos, ya sea un evento específico o todos los eventos disponibles.
- POST: Crea un nuevo evento a partir de los datos proporcionados en la solicitud.
- DELETE: Elimina un evento específico según el ID proporcionado.

Atributos:

- NOT\_DATA\_MESSAGE (dict): Mensaje de respuesta cuando no hay datos disponibles.
- ERROR\_MESSAGE (dict): Mensaje de respuesta cuando ocurre un error durante la solicitud. 
- SUCCESS\_MESSAGE (dict): Mensaje de respuesta exitosa.

delete(*request*, *id\_evento=None*)[#](#api.views.eventoview.delete "Link to this definition")

Maneja las solicitudes DELETE para eliminar un evento.

Parámetros:

- **request** – Objeto de solicitud Django.
- **id\_evento** – ID del evento a eliminar.

Devuelve:

JsonResponse con un mensaje de éxito o una respuesta de error.

dispatch(*request*, *\*args*, *\*\*kwargs*)[#](#api.views.eventoview.dispatch "Link to this definition")

Despacha la solicitud, excluyendo la verificación CSRF.

get(*request*, *id\_evento=None*)[#](#api.views.eventoview.get "Link to this definition")

Maneja las solicitudes GET para recuperar información sobre eventos.

Parámetros:

- **request** – Objeto de solicitud Django.
- **id\_evento** – ID del evento (opcional).

Devuelve:

JsonResponse con detalles del evento o una respuesta de error.

post(*request*)[#](#api.views.eventoview.post "Link to this definition")

Maneja las solicitudes POST para crear un nuevo evento.

Parámetros:

**request** – Objeto de solicitud Django.

Devuelve:

JsonResponse con detalles del evento creado o una respuesta de error.

*class* api.views.FirmaUpdateView(*\*\*kwargs*)[#](#api.views.firmaupdateview "Link to this definition")

Bases: View

Vista para gestionar la actualización de una firma existente en el sistema.

Métodos admitidos:

- POST: Actualiza los detalles de una firma existente utilizando datos proporcionados en la solicitud.

Atributos:

- NOT\_DATA\_MESSAGE (dict): Mensaje de respuesta cuando no hay datos disponibles.

dispatch(*request*, *\*args*, *\*\*kwargs*)[#](#api.views.firmaupdateview.dispatch "Link to this definition")

Despacha la solicitud, excluyendo la verificación CSRF.

post(*request*, *id\_firma=None*)[#](#api.views.firmaupdateview.post "Link to this definition")

Maneja las solicitudes POST para actualizar una firma existente.

Parámetros:

- **request** – Objeto de solicitud Django.
- **id\_firma** – Identificador único de la firma a actualizar (opcional).

Devuelve:

JsonResponse con detalles de la firma actualizada o una respuesta de error.

*class* api.views.FirmaView(*\*\*kwargs*)[#](#api.views.firmaview "Link to this definition")

Bases: View

Vista para gestionar operaciones relacionadas con firmas en el sistema.

Métodos admitidos:

- GET: Obtiene detalles de las firmas. Puede obtener todas las firmas activas o una firma específica por su ID.
- POST: Crea una nueva firma utilizando datos proporcionados en la solicitud.
- DELETE: Desactiva (cambia el estado a “Inactivo”) una firma existente por su ID.

Atributos:

- NOT\_DATA\_MESSAGE (dict): Mensaje de respuesta cuando no hay datos disponibles.
- ERROR\_MESSAGE (dict): Mensaje de respuesta cuando ocurre un error durante la solicitud. 
- SUCCESS\_MESSAGE (dict): Mensaje de respuesta exitosa.

delete(*request*, *id\_firma=None*)[#](#api.views.firmaview.delete "Link to this definition")

Maneja las solicitudes DELETE para desactivar una firma existente.

Parámetros:

- **request** – Objeto de solicitud Django.
- **id\_firma** – Identificador único de la firma a desactivar (opcional).

Devuelve:

JsonResponse indicando el resultado de la operación o una respuesta de error.

dispatch(*request*, *\*args*, *\*\*kwargs*)[#](#api.views.firmaview.dispatch "Link to this definition")

Despacha la solicitud, excluyendo la verificación CSRF.

get(*request*, *id\_firma=None*)[#](#api.views.firmaview.get "Link to this definition")

Maneja las solicitudes GET para recuperar información sobre firmas.

Parámetros:

- **request** – Objeto de solicitud Django.
- **id\_firma** – Identificador único de la firma (opcional).

Devuelve:

JsonResponse con detalles de las firmas o una respuesta de error.

post(*request*)[#](#api.views.firmaview.post "Link to this definition")

Maneja las solicitudes POST para crear una nueva firma.

Parámetros:

**request** – Objeto de solicitud Django.

Devuelve:

JsonResponse con detalles de la nueva firma creada o una respuesta de error.

*class* api.views.ParticipanteFileView(*\*\*kwargs*)[#](#api.views.participantefileview "Link to this definition")

Bases: View

Vista para manejar la carga de participantes desde un archivo Excel.

Métodos admitidos:

- POST: Procesa un archivo Excel enviado en la solicitud y crea participantes en base a los datos del archivo.

Atributos:

- NOT\_DATA\_MESSAGE (dict): Mensaje de respuesta cuando no hay datos disponibles.
- ERROR\_MESSAGE (dict): Mensaje de respuesta cuando ocurre un error durante la solicitud. 
- SUCCESS\_MESSAGE (dict): Mensaje de respuesta exitosa.

dispatch(*request*, *\*args*, *\*\*kwargs*)[#](#api.views.participantefileview.dispatch "Link to this definition")

Despacha la solicitud, excluyendo la verificación CSRF.

post(*request*)[#](#api.views.participantefileview.post "Link to this definition")

Maneja las solicitudes POST para procesar un archivo Excel y crear participantes.

Parámetros:

**request** – Objeto de solicitud Django.

Devuelve:

JsonResponse con detalles de los participantes creados o una respuesta de error.

*class* api.views.ParticipanteView(*\*\*kwargs*)[#](#api.views.participanteview "Link to this definition")

Bases: View

Vista para gestionar operaciones relacionadas con participantes en el sistema.

Métodos admitidos:

- GET: Obtiene detalles de los participantes. Puede obtener todos los participantes o un participante específico por su ID.
- POST: Crea un nuevo participante utilizando datos proporcionados en la solicitud.
- PUT: Actualiza los detalles de un participante existente utilizando datos proporcionados en la solicitud.
- DELETE: Elimina un participante existente por su ID.

Atributos:

- NOT\_DATA\_MESSAGE (dict): Mensaje de respuesta cuando no hay datos disponibles.
- ERROR\_MESSAGE (dict): Mensaje de respuesta cuando ocurre un error durante la solicitud. 
- SUCCESS\_MESSAGE (dict): Mensaje de respuesta exitosa.

delete(*request*, *id\_participante*)[#](#api.views.participanteview.delete "Link to this definition")

Maneja las solicitudes DELETE para eliminar un participante existente.

Parámetros:

- **request** – Objeto de solicitud Django.
- **id\_participante** – Identificador único del participante a eliminar. 

Devuelve:

JsonResponse indicando el resultado de la operación o una respuesta de error.

dispatch(*request*, *\*args*, *\*\*kwargs*)[#](#api.views.participanteview.dispatch "Link to this definition")

Despacha la solicitud, excluyendo la verificación CSRF.

get(*request*, *id\_participante=None*)[#](#api.views.participanteview.get "Link to this definition")

Maneja las solicitudes GET para recuperar información sobre participantes.

Parámetros:

- **request** – Objeto de solicitud Django.
- **id\_participante** – Identificador único del participante (opcional). 

Devuelve:

JsonResponse con detalles de los participantes o una respuesta de error.

post(*request*)[#](#api.views.participanteview.post "Link to this definition")

Maneja las solicitudes POST para crear un nuevo participante.

Parámetros:

**request** – Objeto de solicitud Django.

Devuelve:

JsonResponse con detalles del nuevo participante creado o una respuesta de error.

put(*request*, *id\_participante*)[#](#api.views.participanteview.put "Link to this definition")

Maneja las solicitudes PUT para actualizar un participante existente.

Parámetros:

- **request** – Objeto de solicitud Django.
- **id\_participante** – Identificador único del participante a actualizar.

Devuelve:

JsonResponse con detalles del participante actualizado o una respuesta de error.

*class* api.views.ParticipantesEventoView(*\*\*kwargs*)[#](#api.views.participanteseventoview "Link to this definition")

Bases: View

Vista para obtener la lista de participantes asociados a un evento mediante su identificador. 

Métodos admitidos:

- GET: Obtiene la lista de participantes asociados al evento.

Atributos:

- NOT\_DATA\_MESSAGE (dict): Mensaje de respuesta cuando no se encuentran certificados o participantes asociados al evento.
- ERROR\_MESSAGE (dict): Mensaje de respuesta cuando ocurre un error durante la solicitud. 

dispatch(*request*, *\*args*, *\*\*kwargs*)[#](#api.views.participanteseventoview.dispatch "Link to this definition")

Despacha la solicitud, excluyendo la verificación CSRF.

get(*request*, *id\_evento*)[#](#api.views.participanteseventoview.get "Link to this definition")

Maneja las solicitudes GET para obtener la lista de participantes asociados a un evento mediante su identificador.

Parámetros:

- **request** – Objeto de solicitud Django.
- **id\_evento** – Identificador del evento.

Devuelve:

JsonResponse con la lista de participantes asociados al evento o una respuesta de error.

*class* api.views.PlantillaView(*\*\*kwargs*)[#](#api.views.plantillaview "Link to this definition")

Bases: View

Vista para manejar operaciones relacionadas con plantillas.

Métodos admitidos:

- GET: Recupera información sobre plantillas o descarga una plantilla específica.
- POST: Crea una nueva plantilla o actualiza una existente.
- DELETE: Elimina una plantilla existente.

Atributos:

- NOT\_DATA\_MESSAGE (dict): Mensaje de respuesta cuando no hay datos disponibles.
- ERROR\_MESSAGE (dict): Mensaje de respuesta cuando ocurre un error durante la solicitud. 
- SUCCESS\_MESSAGE (dict): Mensaje de respuesta exitosa.

delete(*request*, *id\_plantilla*)[#](#api.views.plantillaview.delete "Link to this definition")

Maneja las solicitudes DELETE para eliminar una plantilla existente.

Parámetros:

- **request** – Objeto de solicitud Django.
- **id\_plantilla** – ID de la plantilla a eliminar.

Devuelve:

JsonResponse con mensaje de éxito o una respuesta de error.

dispatch(*request*, *\*args*, *\*\*kwargs*)[#](#api.views.plantillaview.dispatch "Link to this definition")

Despacha la solicitud, excluyendo la verificación CSRF.

get(*request*, *id\_plantilla=None*)[#](#api.views.plantillaview.get "Link to this definition")

Maneja las solicitudes GET para recuperar información sobre plantillas o descargar una plantilla específica.

Parámetros:

- **request** – Objeto de solicitud Django.
- **id\_plantilla** – ID de la plantilla a recuperar o descargar (opcional).

Devuelve:

JsonResponse con detalles de la plantilla o una respuesta de error.

post(*request*, *id\_plantilla=None*)[#](#api.views.plantillaview.post "Link to this definition")

Maneja las solicitudes POST para crear una nueva plantilla o actualizar una existente.

Parámetros:

- **request** – Objeto de solicitud Django.
- **id\_plantilla** – ID de la plantilla a actualizar (opcional).

Devuelve:

JsonResponse con detalles de la plantilla creada o actualizada o una respuesta de error.

api.views.generar\_certificado\_pdf(*certificado*, *plantilla\_path*, *detalle\_certificado1*, *detalle\_certificado2*)[#](#api.views.generar_certificado_pdf "Link to this definition")

Genera un certificado en formato PDF combinando la información del certificado, la plantilla, y las firmas proporcionadas.

Parámetros:

- **certificado** – Objeto Certificado que contiene la información necesaria para generar el certificado.
- **plantilla\_path** – Ruta del archivo PDF de la plantilla del certificado. 
- **detalle\_certificado1** – Objeto Detalle\_Certificado que contiene la información de la primera firma.
- **detalle\_certificado2** – Objeto Detalle\_Certificado que contiene la información de la segunda firma.

[anterior](index.html "página anterior")

[Welcome to Certech’s documentation!](index.html "página anterior")[](CertechBakend.html "siguiente página")

[siguiente](CertechBakend.html "siguiente página")

[CertechBakend package](CertechBakend.html "siguiente página")

En esta página 

- [Submodules](#submodules)
- [api.models module](#module-api.models) 
  - [Administrador](#api.models.administrador) 
    - [Administrador.DoesNotExist](#api.models.administrador.doesnotexist)
    - [Administrador.MultipleObjectsReturned](#api.models.administrador.multipleobjectsreturned)
    - [Administrador.cedula](#api.models.administrador.cedula)
    - [Administrador.celular](#api.models.administrador.celular)
    - [Administrador.clave](#api.models.administrador.clave)
    - [Administrador.correo](#api.models.administrador.correo)
    - [Administrador.id_administrador](#api.models.administrador.id_administrador)
    - [Administrador.objects](#api.models.administrador.objects)
    - [Administrador.usuario](#api.models.administrador.usuario)
  - [Certificado](#api.models.certificado) 
    - [Certificado.DoesNotExist](#api.models.certificado.doesnotexist)
    - [Certificado.MultipleObjectsReturned](#api.models.certificado.multipleobjectsreturned)
    - [Certificado.codigo_unico](#api.models.certificado.codigo_unico)
    - [Certificado.fecha](#api.models.certificado.fecha)
    - [Certificado.get_next_by_fecha()](#api.models.certificado.get_next_by_fecha)
    - [Certificado.get_previous_by_fecha()](#api.models.certificado.get_previous_by_fecha)
    - [Certificado.id_administrador](#api.models.certificado.id_administrador)
    - [Certificado.id_certificado](#api.models.certificado.id_certificado)
    - [Certificado.id_evento](#api.models.certificado.id_evento)
    - [Certificado.id_participante](#api.models.certificado.id_participante)
    - [Certificado.id_plantilla](#api.models.certificado.id_plantilla)
    - [Certificado.objects](#api.models.certificado.objects)
    - [Certificado.url](#api.models.certificado.url)
  - [Detalle_Certificado](#api.models.detalle_certificado) 
    - [Detalle_Certificado.DoesNotExist](#api.models.detalle_certificado.doesnotexist)
    - [Detalle_Certificado.MultipleObjectsReturned](#api.models.detalle_certificado.multipleobjectsreturned)
    - [Detalle_Certificado.id_certificado](#api.models.detalle_certificado.id_certificado)
    - [Detalle_Certificado.id_detalle](#api.models.detalle_certificado.id_detalle)
    - [Detalle_Certificado.id_firma](#api.models.detalle_certificado.id_firma)
    - [Detalle_Certificado.objects](#api.models.detalle_certificado.objects)
  - [Evento](#api.models.evento) 
    - [Evento.DoesNotExist](#api.models.evento.doesnotexist)
    - [Evento.MultipleObjectsReturned](#api.models.evento.multipleobjectsreturned)
    - [Evento.descripcion_evento](#api.models.evento.descripcion_evento)
    - [Evento.fecha_creacion](#api.models.evento.fecha_creacion)
    - [Evento.get_next_by_fecha_creacion()](#api.models.evento.get_next_by_fecha_creacion)
    - [Evento.get_previous_by_fecha_creacion()](#api.models.evento.get_previous_by_fecha_creacion)
    - [Evento.id_evento](#api.models.evento.id_evento)
    - [Evento.logo](#api.models.evento.logo)
    - [Evento.nombre_evento](#api.models.evento.nombre_evento)
    - [Evento.objects](#api.models.evento.objects)
    - [Evento.portada](#api.models.evento.portada)
    - [Evento.tipo_evento](#api.models.evento.tipo_evento)
  - [Firma](#api.models.firma) 
    - [Firma.DoesNotExist](#api.models.firma.doesnotexist)
    - [Firma.MultipleObjectsReturned](#api.models.firma.multipleobjectsreturned)
    - [Firma.cargo_propietario](#api.models.firma.cargo_propietario)
    - [Firma.estado_firma](#api.models.firma.estado_firma)
    - [Firma.firma](#api.models.firma.firma)
    - [Firma.id_firma](#api.models.firma.id_firma)
    - [Firma.objects](#api.models.firma.objects)
    - [Firma.propietario_firma](#api.models.firma.propietario_firma)
  - [Participante](#api.models.participante) 
    - [Participante.DoesNotExist](#api.models.participante.doesnotexist)
    - [Participante.MultipleObjectsReturned](#api.models.participante.multipleobjectsreturned)
    - [Participante.cedula](#api.models.participante.cedula)
    - [Participante.celular](#api.models.participante.celular)
    - [Participante.correo](#api.models.participante.correo)
    - [Participante.id_participante](#api.models.participante.id_participante)
    - [Participante.nombre_apellido](#api.models.participante.nombre_apellido)
    - [Participante.objects](#api.models.participante.objects)
  - [Plantilla](#api.models.plantilla) 
    - [Plantilla.DoesNotExist](#api.models.plantilla.doesnotexist)
    - [Plantilla.MultipleObjectsReturned](#api.models.plantilla.multipleobjectsreturned)
    - [Plantilla.id_plantilla](#api.models.plantilla.id_plantilla)
    - [Plantilla.objects](#api.models.plantilla.objects)
    - [Plantilla.plantilla](#api.models.plantilla.plantilla)
- [api.views module](#module-api.views) 
  - [AdministradorView](#api.views.administradorview) 
    - [AdministradorView.dispatch()](#api.views.administradorview.dispatch)
    - [AdministradorView.get()](#api.views.administradorview.get)
  - [CertificadoParticipanteView](#api.views.certificadoparticipanteview) 
    - [CertificadoParticipanteView.dispatch()](#api.views.certificadoparticipanteview.dispatch)
    - [CertificadoParticipanteView.get()](#api.views.certificadoparticipanteview.get)
  - [CertificadoValidoView](#api.views.certificadovalidoview) 
    - [CertificadoValidoView.dispatch()](#api.views.certificadovalidoview.dispatch)
    - [CertificadoValidoView.get()](#api.views.certificadovalidoview.get)
  - [CertificadoView](#api.views.certificadoview) 
    - [CertificadoView.dispatch()](#api.views.certificadoview.dispatch)
    - [CertificadoView.post()](#api.views.certificadoview.post)
  - [EventoUpdate](#api.views.eventoupdate) 
    - [EventoUpdate.dispatch()](#api.views.eventoupdate.dispatch)
    - [EventoUpdate.post()](#api.views.eventoupdate.post)
  - [EventoView](#api.views.eventoview) 
    - [EventoView.delete()](#api.views.eventoview.delete)
    - [EventoView.dispatch()](#api.views.eventoview.dispatch)
    - [EventoView.get()](#api.views.eventoview.get)
    - [EventoView.post()](#api.views.eventoview.post)
  - [FirmaUpdateView](#api.views.firmaupdateview) 
    - [FirmaUpdateView.dispatch()](#api.views.firmaupdateview.dispatch)
    - [FirmaUpdateView.post()](#api.views.firmaupdateview.post)
  - [FirmaView](#api.views.firmaview) 
    - [FirmaView.delete()](#api.views.firmaview.delete)
    - [FirmaView.dispatch()](#api.views.firmaview.dispatch)
    - [FirmaView.get()](#api.views.firmaview.get)
    - [FirmaView.post()](#api.views.firmaview.post)
  - [ParticipanteFileView](#api.views.participantefileview) 
    - [ParticipanteFileView.dispatch()](#api.views.participantefileview.dispatch)
    - [ParticipanteFileView.post()](#api.views.participantefileview.post)
  - [ParticipanteView](#api.views.participanteview) 
    - [ParticipanteView.delete()](#api.views.participanteview.delete)
    - [ParticipanteView.dispatch()](#api.views.participanteview.dispatch)
    - [ParticipanteView.get()](#api.views.participanteview.get)
    - [ParticipanteView.post()](#api.views.participanteview.post)
    - [ParticipanteView.put()](#api.views.participanteview.put)
  - [ParticipantesEventoView](#api.views.participanteseventoview) 
    - [ParticipantesEventoView.dispatch()](#api.views.participanteseventoview.dispatch)
    - [ParticipantesEventoView.get()](#api.views.participanteseventoview.get)
  - [PlantillaView](#api.views.plantillaview) 
    - [PlantillaView.delete()](#api.views.plantillaview.delete)
    - [PlantillaView.dispatch()](#api.views.plantillaview.dispatch)
    - [PlantillaView.get()](#api.views.plantillaview.get)
    - [PlantillaView.post()](#api.views.plantillaview.post)
  - [generar_certificado_pdf()](#api.views.generar_certificado_pdf)

[Mostrar el código ](_sources/api.rst.txt)

© Copyright 2024, José Ojeda, Karen Moyolema, Eduardo Pila, Anthony Solis, Jonathan Villafuerte. 

Creado usando [Sphinx](https://www.sphinx-doc.org/) 7.2.6. 

Construido con el [Tema PyData Sphinx](https://pydata-sphinx-theme.readthedocs.io/en/stable/index.html) 0.15.1. 
