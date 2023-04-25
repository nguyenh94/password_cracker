import string
from itertools import permutations, product
import time
import hashlib

def main():
    # open the file
    file = open("hashes.txt")

    # read in each line from the file
    hashes = file.readlines()

    count = 1
    # crack password
    for password in hashes:
        if count < len(hashes):  # delete the null character 
            password = password[:-1]
            pass_cracker(password)
        count += 1


    # close the file
    file.close()

def pass_cracker(original):
    password = ""
    found = 0
    length = 1
    start_time = time.time()

    while not found:
        for permutation in permutations(string.ascii_uppercase, length):
            for pwd in product(*permutation):
                password = ''.join(pwd)
                hashed_pass = hashlib.md5(password.encode()).hexdigest()
                # print(hashed_pass)
                if hashed_pass == original:
                    end_time = time.time()
                    print(password)
                    print("%ds" % (end_time-start_time))
                    return
        for permutation in permutations(string.ascii_lowercase, length):
            for pwd in product(*permutation):
                password = ''.join(pwd)
                hashed_pass = hashlib.md5(password.encode()).hexdigest()
                if hashed_pass == original:
                    end_time = time.time()
                    print(password)
                    print("%ds" % (end_time-start_time))
                    return
        for permutation in permutations(zip(string.ascii_uppercase, string.ascii_lowercase), length):
            for pwd in product(*permutation):
                password = ''.join(pwd)
                hashed_pass = hashlib.md5(password.encode()).hexdigest()
                if hashed_pass == original:
                    end_time = time.time()
                    print(password)
                    print("%ds" % (end_time-start_time))
                    return
        for permutation in permutations(zip(string.ascii_uppercase,string.ascii_lowercase, string.digits), length):
            for pwd in product(*permutation):
                password = ''.join(pwd)
                hashed_pass = hashlib.md5(password.encode()).hexdigest()
                if hashed_pass == original:
                    end_time = time.time()
                    print(password)
                    print("%ds" % (end_time-start_time))
                    return
        length += 1

main()