import os, fileinput, markdown

# read markdown file
with open('README.md', 'r') as f:
  readmeMarkdown = f.read()

# read destination html file
with open('index.html', 'r') as f:
  destinationLines = f.readlines()
  for line in destinationLines:
    # check if marker exists
    if line.find('data-readme-insert') != -1:
      insertTarget = destinationLines.index(line) + 2
      break;

# turn the markdown into html
readmeHTML = markdown.markdown(readmeMarkdown)

# insert rendered HTML into destination
destinationLines.insert(insertTarget, readmeHTML)

# write to destination html file
with open('index.html', 'w') as f:
  destinationLines = "".join(destinationLines)
  f.write(destinationLines)
