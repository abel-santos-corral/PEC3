# PEC3

Repositorio de Github para hacer la PEC3 de la asignatura de Inteligencia artificial 

# Table of Contents
1. [Configuración de VS Code](#configuracion-de-vs-code)
2. [Ejecutar analisis](#ejecutar-analisis)

# Configuración de VS Code

Para configurar VS Code y tener el entorno listo, sigue estos pasos.

## Crear el entorno virtual

Primero, ve a la carpeta del proyecto y ejecuta:

``` 
python -m venv venv
```

## Activar el entorno virtual

Depende del sistema operativo (OS).

__Linux__

```
source venv/bin/activate
```

__Windows (Power shell)__

```
venv\Scripts\Activate.ps1
```

__Windows (Command prompt)__

```
venv\Scripts\activate
```

## Instalar dependencias

En este caso no es necesario, pero lo dejamos comentado para reutilizarlo en otros proyectos:

```
pip install -r requirements.txt
```

# Ejecutar analisis

Para ejecutar el programa haremos desde la terminal:

```
python3 main.py
```

Esto va a ejecutar todos los scripts de la PEC3.
