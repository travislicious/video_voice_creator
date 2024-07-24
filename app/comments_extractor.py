from pathlib import Path
import os
import srt

def generate_text(path):

    PATH = path
    name = Path(PATH).stem

    with open(PATH, 'r', encoding='utf-8') as f:
        content = f.read()
        lines = content.strip().splitlines()
        comments = []

        count = 1
        pos = 0

        for line in lines:
            if '#' in line:
                pos = line.index('#')
                print(f'Line {count} - Position {pos}: {line[pos + 1:].strip()}')
                comments.append(line[pos + 1:].strip())
            else:
                pass

            count += 1

    if os.path.exists('texts'):
        pass
    else:
        os.mkdir('texts')

    filepath = f'texts/{name}.txt'
    
    with open(filepath, 'w+', encoding='utf-8') as f:
        for comment in comments:
            f.write(comment + '\n\n')

        f.close()

    os.system(f"py talker/main.py -v en_us_001 -f texts/{name}.txt --name voices/{name}.mp3 --session 1cf91506cd266c46ffc7a30895a7be4e")

    srt.generate_captions(f"voices/{name}.mp3", name)

    print("Generation ended successfully.")



