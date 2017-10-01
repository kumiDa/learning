import hashlib
import re
from time import time


def check_runtime(input_str):
    i_cntr = 1
    time_start = time()
    hash = hashlib.sha256(input_str.encode('ascii'))
    hash_digest = hash.hexdigest()
    while (not bool(re.search(r'^0{10}.*', hash_digest))):
        input_str += str(i_cntr)
        i_cntr = i_cntr + 1
        hash = hashlib.sha256(input_str.encode('ascii'))
        hash_digest = hash.hexdigest()
    time_end = time()
    print(i_cntr)
    print(input_str, hash_digest)
    print('the time taken to find the hash is: {}'.format(time_end - time_start))


check_runtime('abcdefghij')
