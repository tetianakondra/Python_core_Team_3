# PERSONAL ASSISTANT

## Installation

[Personal Assistant code on github](https://github.com/tetianakondra/Python_core_Team_3)

## Subprograms

![gjhgjh](https://github.com/aegirhall/console-menu/raw/develop/images/console-menu_screenshot1.png)
### Addressbook
Module for working with your contacts, contain and work with information about contact:
"name", "phones", "birthday", "email", "address". 


#### Commands:
 * **'add'** For using please input user's name and phone to add the user
 * **'birthday'** For using please input user's name and birthday in format DD.MM.YYYY to add the birthday
 * **'days_to_birthday'** For using please input user's name, calculate the quantity of days till user's birthday
 * **'get_birthdays'** For using please input user's name, calculate number for searching users with birthdays in number days                         
 * **'change'** For using please input user's name and phone for changing the phone number
 * **'phone'**  For using please input user's name to phone
 * **'email'**  For using please input user's name and email to add the email
 * **'address'**  For using please input user's name and address to add the address
 * **'show_all'** Show some quantity of users on page. For using input how many pages you want to  see
 * **'delete'** For using please input user's name to delete the contact
 * **'save'** For saving the address book to 'address_book.csv' in current folder
 * **'get_book'** To get the address book from 'address_book.csv' in current folder
 * **'find'** For using please input some symbols to show data in the contacts with this symbols

#### Exit commands:
'goodbye', 'close', 'exit'
### Notebook
Module for working with notes, contain and work with information about notes:
"text", "tag", "id" - it is a creation time of note. 
### Clean Folder
Clean folder is the application which helps to sort folders.
To start please enter the command "clean_folder".
..
It sorts:
*	images ('JPEG', 'PNG', 'JPG', 'SVG');
*	videos ('AVI', 'MP4', 'MOV', 'MKV');
*	documents ('DOC', 'DOCX', 'TXT', 'PDF', 'XLSX', 'PPTX');
*	music ('MP3', 'OGG', 'WAV', 'AMR');
*   archives ('ZIP', 'GZ', 'TAR');
*	unknown.

Additional functions:
*   normalize kirilic symbols to latin, other symbols to "_"
*   unpack all archives


