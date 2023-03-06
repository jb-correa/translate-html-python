if __name__ == '__main__':
  from googletrans import Translator, constants
  from bs4 import BeautifulSoup as bs
  from bs4 import NavigableString
  import os
  import shutil
  
  current_dir = os.path.dirname("C:/Users/jbaut/Downloads/")
  
  for filename in os.listdir(current_dir):
    if filename.endswith(".html"):
      html = open(current_dir+"/"+filename, encoding="utf8").read()
      soup = bs(html, 'html.parser')
      tags = soup.find_all(["p","ul", "li","h1","h2","h3","h4","h5","h6","td", "a", "span"])
      translator=Translator()
      for tag in tags:
        if tag.text:
          translation=translator.translate(tag.string,dest="hi").text
          tag.string=translation
          with open(filename, "wb") as f:
            f.write(soup.prettify("utf-8"))
  print("All done!")
  
  

