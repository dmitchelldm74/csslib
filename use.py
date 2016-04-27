from csslib import css

CSS = css.CSS3("$favcol:purple;/* comment */body{background-color:$favcol;}") # input as string
CSS.parse() # parses string
# __help__ for help
print CSS.get("__comments__") # gets the comments of the css
print CSS.get("__tree__") # gets complete tree
print CSS.get("__vars__") # gets the variables of the css
print CSS.getItem("body") # gets an item with the name 

# CSS.getIds() gets all ids
# CSS.getClasses gets all classes
# CSS.getAllStartWith(<startswith>) gets all items that start with <startswith>
