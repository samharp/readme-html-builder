import markdown

# read markdown file
with open('README.md', 'r') as f:
  tempMD = f.read()

# read destination html file
with open('index.html', 'r') as f:
  destHTML = f.readlines()

# turn the markdown into html
tempHTML = markdown.markdown(tempMD)

# insert rendered HTML into destination
destHTML.insert(11, tempHTML)

# write to destination html file
with open('index.html', 'w') as f:
  destHTML = "".join(destHTML)
  f.write(destHTML)
