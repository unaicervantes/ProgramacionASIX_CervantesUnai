#!/usr/bin/python3
# _*_ coding: utf-8 _*_

import sys, crypt

__author__   = "Unai Cervantes"
__email__    = "cf19unai.cervantes@iesjoandaustria.org"
__license__  = "GPL V3"

"""
Endevina passwords numérics al estil shadow
Mode d'ús:
    time python3 endevina_password.py `openssl passwd -6 -salt UnPessicDeSal 99`
"""


def main(pwd_shadow):
    """
    >>> print(main('$6$bfNlqcskvKPcprPr$B6NH9YTQ1kbFo/xJ09Gi6PFbDE/iorH77qlGC.W/XipUwgH2mMRxsX32wxLUY6xrbm0utU5XzTfnXeHvktaO10'))
    1234
    >>> print(main('$6$UnPessicDeSal$motDspO44FaSqzWRfB7IxzUPMim6xIKYWod8KG4CkKED1ziVSdmZOUAlmNaD9LIcEWodTYMUn.k0NpqT1iZEk.'))
    99
    """
    camps = pwd_shadow.split('$')
    password = ""
    method = camps[1]
    salt = camps[2]
    pwd_hashed = camps[3]
    comptador = 0000
    while password == "": 
        for n1 in range(10):
            for n2 in range(10):
                for n3 in range(10):
                    for n4 in range(10):
                         possible_password = crypt.crypt(str(comptador), '$' + method + '$' + salt)
                         if possible_password == pwd_shadow:
                             password = str(comptador)
                         comptador = str(n1)+str(n2)+str(n3)+str(n4)
    return password

if __name__ == "__main__":
    print(main(sys.argv[1]))
