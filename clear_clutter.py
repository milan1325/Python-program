import os

def make_dir(folder):
    if not os.path.exists(folder):
        os.makedirs(folder)

def move(folderName,files):
    for file in files:
        os.replace(file,f"{folderName}/{file}")



files = os.listdir()
files.remove("main.py")
# print(files)
make_dir('Images')
make_dir('Medias')
make_dir('Docs')
make_dir('Others')
make_dir('Musics')

ImgExts = [".gif",".jpeg",".jpg",".png"]
Images = [file for file in files if os.path.splitext(file)[1].lower() in ImgExts]
# print(ImgExts)

MediaExts = [".avi",".mp4",".flv",".mkv"]
Medias = [file for file in files if os.path.splitext(file)[1].lower() in MediaExts]

DocExts = [".xlsx",".doc",".pdf","docx",".tiff",".txt",".docx"]
Docs = [file for file in files if os.path.splitext(file)[1].lower() in DocExts]

MusicExts = [".aac",".mp3",".wma"]
Musics = [file for file in files if os.path.splitext(file)[1].lower() in MusicExts]

Others = []

for file in files:
    ext = os.path.splitext(file)[1].lower()
    if (ext not in ImgExts) and (ext not in MediaExts) and (ext not in DocExts) and (ext not in MusicExts) and os.path.isfile(file):
        Others.append(file)
# print(Othes)


move("Images",Images)
move("Medias",Medias)
move("Docs",Docs)
move("Musics",Musics)
move("Others",Others)
