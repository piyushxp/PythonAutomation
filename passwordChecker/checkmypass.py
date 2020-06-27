import requests
imort hashlib


def request_api_data(query_char):
    url = 'https://api.pwnedpasswords.com/range/' + 'CBFDA'
    res = requests.get(url)
    # print(res)
    if res.status_code != 200:
        raise RuntimeError(
            f'Error Fetching:{res.status_code},check the API and try again')


def pwned_api_check(password):
    # check password ,if it exists in API response
    sha1passsword = hashlib.sha1(password.encode('utf-8').hexdigest.upper())
    return sha1passsword


request_api_data("123")

# Learned about k-anonymity
# learned about Indempotent
# learnt about hash functions
# learnt about hash hashlib
