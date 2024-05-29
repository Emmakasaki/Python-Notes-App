# Notes App

This is a simple Notes application built with Python using the `tkinter` and `customtkinter` libraries.

## Features

- Create a new note
- Save a note
- Load an existing note

## How it works

The application uses a simple GUI built with `tkinter` and `customtkinter`. 

When you start the application, it opens a window where you can write your notes. 

The `save` function saves the note with the title provided in the title field. If no title is provided, it saves the note as "Untitled". The note is saved as a `.txt` file.

The `load` function allows you to open and load an existing note. It opens a file dialog where you can choose the note to load. The note's content is then displayed in the text field and the title field is updated with the note's title.

## How to run

To run the application, simply execute the `notes.py` script with Python.

```bash
python notes.py
```

## Requirements

- Python
- tkinter
- customtkinter

Please make sure to install the required Python libraries using pip:

```bash
pip install tkinter customtkinter
```

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License

[MIT](https://choosealicense.com/licenses/mit/)
