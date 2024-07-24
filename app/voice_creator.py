import comments_extractor
import intro_creator
import os

intro_txt = input("Enter the intro text: ")
video_name = input("Enter video name: ")

if intro_txt and len(intro_txt) <= 200:

    if not os.path.exists("temp"):
        os.mkdir("temp")
    
    if not os.path.exists("intros"):
        os.mkdir("intros")


    with open(f"temp/{video_name.replace(" ", "_")}.txt", "w", encoding='utf-8') as f:
        f.write(intro_txt)
        f.close()

    intro_creator.generate_intro(f"temp/{video_name.replace(" ", "_")}.txt", video_name.replace(" ", "_"))


path = input("Enter program path: ")

if path:
    comments_extractor.generate_text(path)