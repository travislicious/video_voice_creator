import os

def generate_intro(text, name):
    os.system(f"py talker/main.py -v en_us_001 -f {text} -n intros/{name.lower()}.mp3 --session 1cf91506cd266c46ffc7a30895a7be4e")
    os.remove(text)

    print("Intro Created.")