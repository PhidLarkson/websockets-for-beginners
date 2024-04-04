import socket
import random
import json

# default variables
HEADER = 64
PORT = 5055
FORMAT = 'utf-8'
BREAK = '!e'
SERVER = socket.gethostbyname(socket.gethostname())     # get the server address automatically
ADDR = (SERVER, PORT)                             # specify the address: the server address and port

#  specify server as 192.168.173.50
SERVER = '192.168.173.50'

# clients
CLIENTS = {
    'master': ''
}
# available letters
ID_ALT = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']

# generate id
def addr_cv(id):
    char_len = len(str(id))  
    # trimmer
    while char_len:
        id = str(id)
        if char_len >= 5:
            id = id[:5]
            break
        elif char_len < 5:
            id = int(id)
            id += 0
        char_len = len(str(id))
    
    # conversion
    for marker in range(0, 2):
        id = id.replace(id, ID_ALT[marker])
        print(id)
    return id


# error handling
ERR = KeyboardInterrupt | Exception | SystemExit | ConnectionResetError| ConnectionAbortedError | ConnectionRefusedError | ConnectionError | ConnectionResetError | ConnectionAbortedError | ConnectionRefusedError | ConnectionError | TypeError | ValueError | OSError | TimeoutError

# STANDARD FORMATS: for the format parameter which specifies the encoding of the message
"""
    'ascii', 'utf-16', 'utf-8', 'utf-16-be', 'utf-16-le',
    'utf-7', 'utf-32', 'utf-32-be', 'utf-32-le', 'cp037', 
    'cp424', 'cp437', 'cp500', 'cp720', 'cp737', 'cp775', 
    'cp850', 'cp852', 'cp855', 'cp856', 'cp857', 'cp858', 
    'cp860', 'cp861', 'cp862', 'cp863', 'cp864', 'cp865', 
    'cp866', 'cp869', 'cp874', 'cp875', 'cp932', 'cp949', 
    'cp950', 'cp1006', 'cp1026', 'cp1140', 'cp1250', 'cp1251', 
    'cp1252', 'cp1253', 'cp1254', 'cp1255', 'cp1256', 'cp1257', 
    'cp1258', 'euc_jp', 'euc_jis_2004', 'euc_jisx0213', 'euc_kr', 
    'gb2312', 'gbk', 'gb18030', 'hz', 'big5', 'big5hkscs', 
    'shift_jis', 'shift_jis_2004', 'shift_jisx0213', 'iso2022_jp', 
    'iso2022_jp_1', 'iso2022_jp_2', 'iso2022_jp_2004', 
    'iso2022_jp_3', 'iso2022_jp_ext', 'latin_1', 'iso8859_2', 
    'iso8859_3', 'iso8859_4', 'iso8859_5', 'iso8859_6', 
    'iso8859_7', 'iso8859_8', 'iso8859_9', 'iso8859_10', 
    'iso8859_13', 'iso8859_14', 'iso8859_15', 'iso8859_16', 'johab', 
    'koi8_r', 'koi8_u', 'mac_cyrillic', 'mac_greek', 'mac_iceland', 
    'mac_latin2', 'mac_roman', 'mac_turkish', 'ptcp154', 'viscii', 
    'utf_32_be', 'utf_32_le', 'z
"""


