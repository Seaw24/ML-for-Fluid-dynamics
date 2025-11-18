import nbformat

path = "src/Burger model 1-D (1 time-step input).ipynb"
nb = nbformat.read(path, as_version=4)
# Remove metadata.widgets if present
if "widgets" in nb.metadata:
    del nb.metadata["widgets"]
nbformat.write(nb, path)
