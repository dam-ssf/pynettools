# PyNetTools

Herramientas de redes desarrolladas en Python para el módulo profesional SSF (Sistemas Informáticos).

## Comandos

El paquete `pynettools` contiene los siguientes comandos:

| Comando         | Descipción                                                                                                                    |
| --------------- | ----------------------------------------------------------------------------------------------------------------------------- |
| `calc_subnet`   | Calcula las subredes a partir de la red indicada y el número de subredes deseado.                                             |
| `get_netmask`   | Devuelve la máscara de red y la máscara wildcard a partir del número de bits de la misma (notación CIDR).                     |
| `get_network`   | Obtiene información de una red.                                                                                               |
| `ip_to_bin`     | Convierte una dirección IP en su representación binaria.                                                                      |
| `list_nics`     | Lista todas las interfaces de red del sistema.                                                                                |
| `mac_vendor`    | Devuelve el fabricante asociado a una dirección MAC (física).                                                                 |
| `web_server`    | Inicia un servidor web ofreciendo los recursos de la carpeta indicada.                                                        |
| `which_network` | A partir de una dirección IP y una máscara de red (o notación CIDR), muestra la dirección de la red a la que pertenece la IP. |

> [!NOTE] 
> Todos los comandos que requieran parámetros mostrarán una ayuda si estos no se especifican.

## Requerimientos

- Python >= 3.11

## Instalación

Para instalar este paquete directamente desde el repositorio Git:

```bash
pip install git+https://github.com/dam-ssf/pynettools.git
```

## Para desarrolladores

En caso de que queramos desarrollar este paquete, ya sea para modificar o añadir nuevas funcionalidades, debemos clonar el repositorio y entrar en el directorio:

```bash
git clone https://github.com/dam-ssf/pynettools
cd pynettools
```

Creamos un entorno virtual:

```bash
python -m venv venv
```

Instalamos el paquete en el entorno virtual en modo de edición:

```bash
pip install -e .
```

¡Y a programar!

```bash
code .
```

> [!IMPORTANT]
> Para generar el fichero de dependencias (si fuera necesario, porque hemos añadido una dependencia nueva o cambiado alguna versión):
> 
> ```bash
> pip freeze --exclude-editable > requirements.txt
> ```
