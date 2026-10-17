# Online Messaging Socket

Un chat de terminal entre dos equipos, construido con sockets TCP en Python para Windows. Un equipo crea la partida y el otro se conecta usando la IP pública del anfitrión y el puerto 8050.

## Cómo funciona

1. Ambos equipos ejecutan el programa.
2. El anfitrión elige crear una partida y comparte su IP pública en privado.
3. El invitado elige unirse e introduce esa IP.
4. Cuando se establece la conexión, ambos pueden intercambiar mensajes desde la terminal. Escribe `exit` para salir.

Al iniciar, el programa consulta la IP pública, intenta configurar el reenvío del puerto mediante UPnP y prepara reglas del Firewall de Windows. Incluye el ejecutable `upnpc/upnpc-static.exe` para la gestión de UPnP.

## Requisitos

- Windows y Python 3.
- La dependencia `requests`.
- Un router con UPnP habilitado y una conexión que permita conexiones entrantes.
- Permisos de administrador de Windows para crear reglas del firewall.

## Instalación y uso

Instala la dependencia:

    python -m pip install requests

Ejecuta el programa en ambos equipos:

    python main.py

En el equipo anfitrión, selecciona `2` y comparte la IP pública que aparece en pantalla. En el invitado, selecciona `1` e introduce esa IP.

## Límites y seguridad

Es un prototipo experimental para intercambiar texto entre un anfitrión y un invitado. La conexión TCP no cifra ni autentica los mensajes: comparte la IP solo con alguien de confianza y no envíes información sensible. La conexión puede no funcionar si el router no admite UPnP, si el proveedor usa CGNAT o si la red bloquea conexiones entrantes.

El programa intenta cerrar el mapeo UPnP al salir con normalidad. Las reglas que añade al Firewall de Windows permanecen instaladas. Solo admite un invitado por sesión.

---

README redactado con asistencia de IA. El código del proyecto no se modificó para esta documentación.
