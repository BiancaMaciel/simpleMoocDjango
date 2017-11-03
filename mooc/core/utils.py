'''
chave randomica, para quando o usuário quiser trocar a senha manda um link para o email dele
ai verifica se esta chave está cadastrada no banco. essa chave tem que ser única

def random_key cria caracteres randomico. 

generate -> vai dar um salt texto randominco + email para não correr o risco de criar a chave duas vezes 
'''

import hashlib
import string
import random

def random_key(size=5):
    chars = string.ascii_uppercase + string.digits
    return ''.join(random.choice(chars) for x in range(size))

def generate_hash_key(salt, random_str_size=5):
    random_str = random_key(random_str_size)
    text = random_str + salt
    return hashlib.sha224(text.encode('utf-8')).hexdigest()