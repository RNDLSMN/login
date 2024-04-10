import requests

def add_scheme(url):
    if not url.startswith('http://') and not url.startswith('https://'):
        return 'https://' + url
    return url

def login_to_website(url, username, password):
    url = add_scheme(url)
    login_url = url + '/login'
    login_data = {'username': username, 'password': password}
    session = requests.Session()

    try:
        response = session.post(login_url, data=login_data, verify=False)
        if response.ok:
            print(f"Login berhasil ke {url}")
            # Membuka file dalam mode 'a' dan menulis hasil yang berhasil langsung ke file
            with open(output_filename, 'a') as output_file:
                output_file.write(f"{url}:{username}:{password} Berhasil\n")
    except requests.exceptions.RequestException as e:
        print(f"Gagal mengakses {url}: {e}")

filename = 'urls.txt'
output_filename = 'login_berhasil.txt'

# Memastikan file output bersih/segar setiap kali script dijalankan
with open(output_filename, 'w') as output_file:
    output_file.write('')

with open(filename, 'r') as file:
    credentials = [line.strip() for line in file.readlines()]

for credential in credentials:
    url, username, password = credential.split(':')
    login_to_website(url, username, password)
