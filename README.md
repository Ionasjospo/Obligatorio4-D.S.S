# Cuarto obligatorio de Desarrollo de Software Seguro

Este proyecto incluye 2 scripts diseñados para probar y demostrar la seguridad en el sistema de inicio de sesión de AltoroJ.

## Uso

Para ejecutar el script, sigue estos pasos:

1. Abre una terminal en tu sistema.

2. Navega al directorio donde se encuentra el script.

3. Ejecuta el script con el siguiente comando: python script1.py


## Prueba 1: Inyección SQL en el inicio de sesión

El primer script pide al usuario que ingrese un nombre de usuario y una contraseña. Si se ingresan datos conocidos como `admin`/`admin`, el script devuelve `1`, lo que indica una autenticación válida.
Si se ingresa un usuario no válido el script devuelve `0`, lo que indica una autenticación no válida.

Finalmente, si se intenta una inyección SQL como `' or 1=1 --`, el script aún devuelve `0`. Esto demuestra que la consulta está correctamente parametrizada y que la vulnerabilidad de inyección SQL está ausente.


