from homebrew import menu_library
from homebrew import database_library


class CrossWord:

    def __init__(self):
        self.output_menu_instance = menu_library.OutputMenus()
        self.dal_instance = database_library.Dal()

    def start_session(self, library):
        self.output_menu_instance.start_crossword_session()
        reason = library[0] + '_training_'
        self.dal_instance.load_a_file(reason)
        self.output_menu_instance.work_in_progress()
