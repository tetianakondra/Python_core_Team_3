# Import the necessary packages
import Python_core_Team_3
import Clean_folder
from consolemenu import *
from consolemenu.items import *

a_b = "Address Book - застосунок, що дозволяє створювати контакти та редагувати їх.\nДетально дивись Help застосунку."
n = "Notes- застосунок, що дозволяє створювати нотатки та редагувати їх.\nДетально дивись Help застосунку."
c_f = "Clean Folder - застосунок, що сортує файли в зазнеченій теці.\nВ поле вводу необхідно ввести шлях до теки в " \
      "якій будуть відсортовані файли"


# Create the menu
menu = ConsoleMenu("CLI Assistant", "Subtitle")

# Create some items

# MenuItem is the base class for all items, it doesn't do anything when selected
menu_item = MenuItem("Menu Item")

# A FunctionItem runs a Python function when selected
address_book = FunctionItem("Address Book", Python_core_Team_3.main, [])
clean_folder = FunctionItem("Clean Folder", Clean_folder.main, [])
notes = FunctionItem("Notes", input, [">>>"])

# A CommandItem runs a console command
command_item = CommandItem("Run a console command",  "clear")

# A SelectionMenu constructs a menu from a list of strings
selection_menu_about = SelectionMenu([a_b, n, c_f])
selection_menu_creators = SelectionMenu(["creator_1", "creator_2", "creator_3", "creator_4", "creator_5"])

# A SubmenuItem lets you add a menu (the selection_menu above, for example)
# as a submenu of another menu
submenu_info = SubmenuItem("Information", selection_menu_about, menu)
submenu_creators = SubmenuItem("Creators", selection_menu_creators, menu)

# Once we're done creating them, we just add the items to the menu
menu.append_item(address_book)
menu.append_item(notes)
menu.append_item(clean_folder)
menu.append_item(submenu_info)
menu.append_item(submenu_creators)

# Finally, we call show to show the menu and allow the user to interact
menu.show()