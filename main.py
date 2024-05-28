import pkg_resources


# * MENU CLASS
class Menu:
    def __init__(self):
        pass

    # ? METHOD THAT PRINTS THE MENU TO THE CONSOLE
    def __str__(self) -> str:
        pass


if "__main__" == __name__:

    installed_packages = pkg_resources.working_set
    for package in installed_packages:
        print(f"{package.key}=={package.version}")
