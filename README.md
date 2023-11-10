# Place README content inside a webpage

Certain projects require the same (or close to the same) content in the project `README` and `index.html` page. Think working examples, proof-of-concepts, and other development needs. Markdown makes content writing easy - but managing content in your project's `README` *and* `index` file can quickly become a hassle.

### Solution? Python build process that turns a `README.md` file into HTML (and places it in your home page).

## Before we begin...

This program is built in Python, meaning that you will need Python installed to run it. If you do not have Python installed on your machine, you can get it [here](https://www.python.org/downloads/).

**NOTE:** Your files DO NOT have to be named the same as what is included in this documentation. To change the file names or paths, simply change the values inside the `with` statements in the `readme-build.py` file:

```
with open('/yourPath/yourFileName.md', 'r', ...)...

with open('/yourPath/yourFileName.html', 'r', ...)...

with open('/yourPath/yourFileName.html', 'w', ...)...

```

## Getting set up

Running the program is straight-forward as long as some things are accounted for:

### Folder Structure

The `readme-build.py` file is set up to automatically read in a project `README.md` file and an `index.html` file. The default setup requires all three files to be at the same hierarchy level. Putting these files in the project root meets this requirement:

```
/projectFolder
  // project files
  ...
  index.html
  readme-build.py
  README.md
```

### Setting a "marker"

Within your HTML file, you will now need to create an HTML element to hold the README content. This can be any unique element (no other elements like this should exist on the page!), **but must include** the custom attribute `data-readme-marker`.

Example:

```
<!DOCTYPE html>
...
  <body>
    ...
    <section data-readme-marker>
      <!-- Here is where the Markdown will go -->

    </section>
    ...
  </body>
</html>
```

**NOTE:** The content within this element will be deleted and re-rendered each time the program is run. This means that changes should **ONLY** be made to the README, and not to this section.

## Ready to go!

You're all set! To run the `readme-build.py` file, either double click on the file in your file explorer or `cd` to the folder where these files reside in Terminal/PowerShell. From there, you can run the file by entering:

```
python readme-build.py
```

**NOTE:** This process does not automatically run when you make changes to the README. After making changes to the README, you will have to run the program to get those changes to show on the `index.html` page.