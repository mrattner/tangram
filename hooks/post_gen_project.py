if __name__ == "__main__":
    import os

    PROJECT_DIRECTORY = os.path.realpath(os.path.curdir)
    
    if "{{ cookiecutter.use_bulma_and_sass|lower }}" != "y":
        os.rmdir(os.path.join(PROJECT_DIRECTORY, "resources", "scss"))