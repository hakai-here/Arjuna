import requests
import hashlib

def web_api_data(query_char):
    url = 'https://api.pwnedpasswords.com/range/' + query_char
    res = requests.get(url)
    if res.status_code != 200:
        raise RuntimeError(
            f'Error fetching:{res.status_code}, please check you API and try again with correct API.')
    return res


def leak_count(hashes, hash_to_check):
    hashes = (line.split(':') for line in hashes.text.splitlines())
    for h, count in hashes:
        if h == hash_to_check:
            return count
    return 0  


def CheckPos(password):
    sha1password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    first5_cha, tail = sha1password[:5], sha1password[5:]
    response = web_api_data(first5_cha)
    return leak_count(response, tail)


def nemopass(passwords):
    
    passwords = passwords.split(",")
    for password in passwords:
        count = CheckPos(password)
        if count:
            print(
                f'{password} is found {count} times in breach directory. It is heighly reccomended for you to change the password.')
        else:
            print(f'{password} looks safe as it was not found in password breach directory.')
    return "checked"




