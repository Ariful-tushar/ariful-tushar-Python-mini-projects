import requests
import hashlib
import sys

file_name = input ("Please enter the text file name: ")


def request_api_data (char):
    '''
    Get Api request and return the response
    '''
    url = 'https://api.pwnedpasswords.com/range/' + char
    res = requests.get(url)
    if res.status_code != 200:
        raise RuntimeError (f"Error fetching: {res.status_code}")
    return res


def get_pass_leaks_count (hashes, hash_to_check):
    '''
    Count the password laeks
    '''

    hashes = (line.split(":") for line in hashes.text.splitlines())
    for h,count in hashes:
        #print (h)
        if h == hash_to_check:
            return count
    return 0
    

def pwned_api_check (password):
    sha1pass = hashlib.sha1(password.encode("utf-8")).hexdigest().upper()
    first5_char , tail = sha1pass[:5], sha1pass [5:]
    response = request_api_data (first5_char)
    return get_pass_leaks_count(response, tail)
    

def read_text (file_name):
    file = open (f"text/{file_name}.txt", "r")
    return file.read().split(" ")



def main(args):
    for password in args:
        count = pwned_api_check(password)
        if (count):
            print (f"{password} was found {count} times. Please change it")
        else:
            print (f"{password} was not found. You are good to go")
    


if __name__ == "__main__":
    try:
        main (read_text (file_name))
    except: 
        print (f"No text file was found in the text directory named {file_name}")

