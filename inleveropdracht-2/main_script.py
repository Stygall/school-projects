from homebrew import menu_library

if __name__ == '__main__':
    input_menu_instance = menu_library.InputMenus()
    output_menu_instance = menu_library.OutputMenus()
    output_menu_instance.startup()
    input_menu_instance.login_or_register()
