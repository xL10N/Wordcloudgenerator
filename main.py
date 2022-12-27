from PIL import Image
import wordcloud    # pip install wordcloud
import docx2txt      # pip install docx2txt

print("Welcome to the wordcloudgenerator!")
while True:
    path = input("Please paste the path of the file from which you want to create a Wordcloud (docx or txt): ")

# open the file
    try:
        if "docx" in path:
            words = docx2txt.process(path)
        else:
            f = open(path, "r", encoding="utf-8")
            words = f.read()
            f.close()
        break
    except FileNotFoundError:
        print("There is not such a file or dictionary")
        print("Try it again")

# check if there is a file with words tha should be eliminated
while True:
    check = input("Do you have a docx or txt file with words, that should not be in the wordcloud(Y/N): ")
    if "Y" in check:
        # open the file
       file_name = input("Enter the path of the file (docx, txt): ")
       if "docx" in file_name:
           Stopwords = docx2txt.process(path)
       else:
           f_ = open(file_name, "r", encoding="utf-8")
           Stopwords = f_.read()
           f_.close()
       w = wordcloud.WordCloud(
           width=int(input("Enter the width of the wordcloud: ")),
           height=int(input("Enter the height of the wordcloud: ")),
           stopwords=set(Stopwords.split())

       )
       break
    if "N" in check:
        w = wordcloud.WordCloud(
            width=int(input("Enter the width of the wordcloud: ")),
            height=int(input("Enter the height of the wordcloud: "))
        )
        break
w.generate(words)
# where to save the wordcloud
save_path = input("Where do you want to save the wordcloud(Enter the path please): ")
w.to_file(save_path)
p = Image.open(save_path)
p.show()
