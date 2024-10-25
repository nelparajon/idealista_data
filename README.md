# Idealista Data Extraction

Este proyecto extrae y procesa datos de propiedades en alquiler de la API de Idealista en función de la provincia seleccionada en España. Incluye autenticación OAuth para la API, consulta de datos según parámetros de búsqueda, procesamiento y exportación de resultados en un archivo CSV.
El archivo CSV se guarda en el propio proyecto, en una carpeta llamada datasets que se crea automáticamente si no existe.

## Tabla de Contenidos
- [Tecnologías Utilizadas](#tecnologías-utilizadas)
- [Requisitos](#requisitos)
- [Instalación](#instalación)
- [Configuración](#configuración)
- [Uso](#uso)
- [Estructura del Proyecto](#estructura-del-proyecto)
- [Contribuciones](#contribuciones)
- [Licencia](#licencia)

## Tecnologías Utilizadas

- **Python 3.7+**: Lenguaje de programación para la extracción y manipulación de datos.
- **Requests**: Librería para realizar solicitudes HTTP y conectarse a la API de Idealista.
- **Dotenv**: Librería para cargar variables de entorno desde un archivo `.env`.
- **Os**: Si quieres utilizar directamente variables de entorno de tu sistema.
- **Pandas**: Utilizado para la manipulación y análisis de datos, en especial para convertir los datos JSON en DataFrames y exportarlos a CSV.
- **Idealista API**: Servicio externo que proporciona datos de propiedades en venta y alquiler en España.

## Requisitos

- Python 3.7+
- [Idealista API Access](https://developers.idealista.com/access-request)
- Paquetes necesarios:
  - requests
  - dotenv
  - pandas
  - numpy

## Instalación

1. Clona este repositorio:
    ```bash
    git clone https://github.com/nelparajon/idealista_data.git
    ```

2. Instala las dependencias:
    ```bash
    pip install -r requirements.txt
    ```

## Configuración

1. **Obtén tus credenciales de la API de Idealista.**  
2. **Configura las variables de entorno** creando un archivo `.env` en el directorio raíz con tus credenciales de API:
    ```env
    IDEALISTA_API_KEY=tu_api_key
    IDEALISTA_API_SECRET=tu_api_secret
    #Se pueden obviar las variables de entorno y usar las credenciales directamente o en un archivo .config
    ```
    

## Uso

Para ejecutar el programa, abre una terminal y ejecuta:

```bash
python main.py
#Introduce el nombre de la provincia de la cuál quieras extraer el dataset. Ten en cuenta que Idealista solo permite 100 solitudes al mes.
```

## Estructura del Proyecto
- main.py: Archivo principal que ejecuta el proceso completo.
- token_generate.py: Contiene la función get_oauth_token() para autenticarse con la API de Idealista.
- searching.py: Contiene funciones para definir URLs de búsqueda y realizar peticiones a la API.
- process_data.py: Contiene funciones para procesar datos (convertir a DataFrame, concatenar resultados y guardar en CSV).
- params_api.py: Define los parámetros para la API (base URL, operaciones, tipos de propiedad, etc.).
- datasets/: Carpeta donde se almacenarán los archivos CSV resultantes.
- codigos_postales_espana.json: Archivo JSON con los códigos postales por provincia.

## Contribuciones
Las contribuciones son bienvenidas. Si deseas mejorar alguna funcionalidad, no dudes en crear un pull request o abrir un issue.

## Licencia
**Este proyecto está bajo la Licencia MIT.**

