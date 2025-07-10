import requests

# API Key de Smoobu
api_key = 'tQDynPBXzaKXoDJdhZHdXOw2eE6zF4Y5'

# URL base de la API
base_url = 'https://login.smoobu.com/api/v1'

# Cabeceras de autenticación
headers = {
    'Authorization': f'Bearer {api_key}'
}

# Petición a la API para listar propiedades
response = requests.get(f'{base_url}/properties', headers=headers)

# Mostrar resultado
if response.status_code == 200:
    data = response.json()
    for property in data.get('data', []):
        print(property.get('name', 'Sin nombre'))
else:
    print(f'Error: {response.status_code} - {response.text}')
