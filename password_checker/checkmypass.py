import requests
import hashlib

def request_api_data(query_char):
    url = 'https://api.pwnedpasswords.com/range/' + query_char
    res = requests.get(url) 
    if res.status_code != 200:
        raise RuntimeError(f'Error: {res.status_code}, check the API' )
    return res

def get_password_leaks_count(hashes, hash_to_check):
    hashes = (line.split(':') for line in hashes.text.splitlines())
    for h, count in hashes:
        if h==hash_to_check:
            return count
    return 0

def pwned_api_check(password):
    # Check if password is in the API response
    sha1password = (hashlib.sha1(password.encode('utf-8')).hexdigest().upper())
    first5, tail = sha1password[:5], sha1password[5:]
    response = request_api_data(first5)
    print(get_password_leaks_count(response, tail))

    return sha1password

def main(password):
    pwned_api_check(password)
    pass

if __name__ == __main__:
    password = '123'
    main(password)