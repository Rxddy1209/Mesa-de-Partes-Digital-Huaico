# Mesa de Partes Digital - Huayco

## Integrantes del grupo:
Ruddy Raraz, Leonel Morales, Mateo Oroche, Valentino Oroche, Mishel Vilcayaury

## Profesor:
WILLIAMS ALFONSO CHULLO VILLAGARAY

## ¿De qué trata el proyecto?

Este proyecto es un prototipo académico hecho en Python para el curso de Fundamentos de Programación. La idea es representar una forma sencilla de registrar reportes de ciudadanos sobre huaicos o deslizamientos y revisar el estado de cada reporte.

El proyecto está relacionado con el proceso de mesa de partes de la Municipalidad Distrital de Santa Anita, pero **no es un sistema oficial ni está conectado con la municipalidad**.

## Objetivo

Registrar la información de un reporte, asignarle un código y permitir buscarlo o cambiar su estado.

## ¿Qué puede hacer el programa?

- Registrar un reporte ciudadano.
- Pedir los datos obligatorios.
- Crear un código como `EXP-0001`.
- Guardar los reportes en `expedientes.json`.
- Buscar un expediente usando su código.
- Mostrar todos los expedientes guardados.
- Cambiar el estado entre Pendiente, En proceso y Atendido.

## Datos que solicita

Nombre, DNI u otro documento, teléfono, ubicación del incidente y descripción. También guarda el código y el estado del expediente.

Para las pruebas se deben usar datos inventados. No se deben subir datos personales reales a GitHub.

## Herramientas utilizadas

- Python para programar el prototipo.
- JSON para guardar la información en un archivo.
- GitHub para guardar el proyecto y mostrar los cambios realizados.

## Cómo ejecutar el programa

1. Tener instalado Python 3.
2. Descargar este repositorio.
3. Abrir una terminal en la carpeta del proyecto.
4. Ejecutar `python main.py`.
5. Elegir una opción del menú.

El archivo `expedientes.json` se crea cuando se registra el primer reporte.

## Archivos del proyecto

- `main.py`: contiene el código del programa.
- `PRUEBAS.md`: contiene los casos de prueba.
- `.gitignore`: indica algunos archivos que no se deben subir al repositorio.
- `evidencias/`: carpeta para colocar capturas de las pruebas, si se necesitan.

## Limitaciones

Por ahora, el programa funciona en la consola. Todavía no tiene una página web, no se conecta con la municipalidad y no clasifica automáticamente los reportes por nivel de emergencia. Estas funciones podrían agregarse más adelante.

## Control de versiones

Se usarán commits en GitHub para registrar los cambios que se vayan haciendo al código y a la documentación.
