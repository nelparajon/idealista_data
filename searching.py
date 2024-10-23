from token_generate import get_oauth_token
import requests
import json
import params_api


def get_location_id(province):
    """Get the location ID for the province.
    Args:
        province (str): The province to get the location ID for.
    Returns:
        int: The location ID for the province.
    Raises:
        ValueError: If the province is not a string or if the location ID cannot be found.
        FileNotFoundError: If the JSON file with postal codes cannot be found.
        json.JSONDecodeError: If the JSON file cannot be parsed.
    """
    if not isinstance(province, str):
        raise ValueError("The province must be a string.")
    
    try:
        with open('codigos_postales_espana.json', 'r', encoding='utf-8') as file:
            codigos_postales_espana = json.load(file)
    except FileNotFoundError:
        raise FileNotFoundError("The file 'codigos_postales_espana.json' was not found.")
    except json.JSONDecodeError:
        raise json.JSONDecodeError("The file 'codigos_postales_espana.json' could not be parsed.")
    
    for p in codigos_postales_espana:
        if p['provincia'].lower() == province.lower():
            location_id = p['codigo_postal']
            return location_id
    
    raise ValueError(f"Location ID for province '{province}' not found.")

def define_search_url(province):
    """
    Constructs the search URL and parameters for querying real estate data in Asturias.
    Args:
        province (str): The province to search for.
    Returns:
        tuple: A tuple containing the base URL (str) and a dictionary of query parameters (dict).
    Raises:
        ValueError: If the province is not a string or if the location ID cannot be found.
    """
    if not isinstance(province, str):
        raise ValueError("The province must be a string.")
    
    location_id = get_location_id(province)
    
    url = params_api.base_url + params_api.country + '/search'
    params = {
        'operation': params_api.operation[2],
        'maxItems': params_api.max_items,
        'order': params_api.order,
        'locationId': f'0-EU-ES-{location_id}',
        'propertyType': params_api.property_type[1],
        'sort': params_api.sort,
        'numPage': 1,
        'language': params_api.language
    }
    return url, params


def search_api(url, params):
    """Searches the API using the provided URL.
    Args:
        url (str): The URL to send the POST request to.
    Returns:
        dict: The JSON response from the API, parsed into a dictionary.
    Raises:
        requests.exceptions.RequestException: If there is an issue with the HTTP request.
        json.JSONDecodeError: If the response cannot be parsed into JSON.
    """
    try:
        token = get_oauth_token()
        headers_dict = {
            'Content-Type': 'application/x-www-form-urlencoded',
            'Authorization': 'Bearer ' + token}
        content = requests.post(url, headers=headers_dict, data=params)
        content.raise_for_status()
        result = json.loads(content.text)
        return result
    except requests.exceptions.HTTPError as http_err:
        print(f"Error HTTP: {http_err}")  # errores relacionados con la respuesta HTTP
    except requests.exceptions.ConnectionError as conn_err:
        print(f"Error de conexión: {conn_err}")  # errores de conexión
    except requests.exceptions.Timeout as timeout_err:
        print(f"Error de tiempo de espera: {timeout_err}")  # errores de tiempo de espera
    except requests.exceptions.RequestException as req_err:
        print(f"Error en la solicitud: {req_err}")  # otro error de solicitud
    except Exception as e:
        print(f"Un error inesperado ocurrió: {e}")  # otro tipo de excepción
    
    return None  #si hubo algún error, devolver None

def processing_search(province):
    """Process the search API and return the result
    Args:
        province (str): The province to search for.
        url (str): The URL to send the POST request to.
        params (dict): The parameters to include in the POST request.
    Returns:
        dict: The JSON response from the API, parsed into a dictionary.
    """
    url, params = define_search_url(province)
    result = search_api(url, params)
    return result



    

