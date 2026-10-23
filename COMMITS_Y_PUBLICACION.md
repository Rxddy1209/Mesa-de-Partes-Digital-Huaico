# Guía para el historial de commits

Un commit guarda un cambio realizado en el proyecto. Los mensajes deben explicar qué se agregó o corrigió.

## Ejemplos de mensajes

1. `Crear estructura inicial del proyecto`
2. `Agregar código principal en Python`
3. `Agregar casos de prueba del programa`
4. `Documentar resultados de las pruebas`

Estos mensajes son ejemplos y deben corresponder a cambios reales. Si se suben todos los archivos de una sola vez, el primer commit será el estado inicial. Después se pueden registrar mejoras reales.

## Desde la página de GitHub

1. Abrir el repositorio.
2. Usar **Add file** para crear o subir un archivo.
3. Bajar hasta **Commit changes**.
4. Escribir un mensaje que describa el cambio.
5. Confirmar el commit.

## Desde la terminal

```bash
git init
git add README.md .gitignore PRUEBAS.md
git commit -m "Crear estructura inicial del proyecto"

git add main.py
git commit -m "Agregar código principal en Python"

git status
```

Para subir los cambios, sigue la URL que GitHub muestra al crear el repositorio. No publiques archivos con datos personales reales.
