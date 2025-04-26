import sys
from time import sleep

def animate():
    baris_kalimat = [
        [("abc def ", 0.10), ("ghi jkl", 1)],  # Baris pertama
        [("mno pqr ", 0.3), ("stu vwx", 0.8)]  # Baris kedua
    ]

    for baris in baris_kalimat:
        for kata, jeda in baris:
            for huruf in kata:
                print(huruf, end='', flush=True)
                sleep(jeda)
        print()
animate()    
