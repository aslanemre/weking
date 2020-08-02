# -*- coding: utf-8 -*-
import requests

source_url = "https://www.usom.gov.tr/url-list.txt" ## you can change this (in TR)

r = requests.get(source_url)

file = open("source.txt", "w")

file.write(str(r.content))

file.close()

print("")
print('''

.-._                                                    _,-,
  `._`-._         WEKING BAD DOMAIN CONTROLLER      _,-'_,'
     `._ `-._                                   _,-' _,'
        `._  `-._        __.-----.__        _,-'  _,'
           `._   `#==="""           """===#'   _,'
              `._/)  ._               _.  (\_,'
               )*'     **.__     __.**     '*(
               #  .==..__  ""   ""  __..==,  #
               #   `"._(_).       .(_)_."'   #

      ''')
print("")

def control():
    url = str(input("[ ? ] Entry a domain : "))
    print("")
    source = open("source.txt", "r")
    bads = source.read()
    source.close()
    if str(url) in str(bads):
        print("[ ! ] Bad url detected." )
    else:
        print("[ + ] Its not bad url." )
control()
