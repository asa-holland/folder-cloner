# Folder Cloner
Short script to duplicate ("clone") a directory and its contents. However, clones never come out exactly like their source material, so this script allows for text-based changes to be built into all Word files contained in the cloned directory.


<!-- ABOUT THE PROJECT -->
## About The Project

![Folder Cloner Example Use][example-use]

Ever had the tedious task of duplicating a Microsoft Word file and making small changes to the text throughout the document? Find and Replace is a valuable friend.

But what if your task requires multiple Word Docs to be changed? You'd need to open each document to use our friend Find and Replace. Not challenging, just time-consuming.

Let's add another layer to this onion. Let's say that instead of duplicating a set of Word files once, you needed to make multiple duplicates, each with small changes throughout. Now the time you're spending searching and replacing the text in all those documents has become quite the chore.

Sure, you could use Word's [Templating System](https://docs.microsoft.com/en-us/power-platform/admin/using-word-templates-dynamics-365), but that requires time and effort to build a template for each base file you want to duplicate. Maybe you've been given a set of files that you didn't create, but the changes need to be made throughout.

Enter the Folder Cloner.

The Folder Cloner is a small script that abstracts away all those steps of finding and replacing strings in Word documents so you can focus on getting your updated information where it needs to go. Provide the Folder Cloner a directory to clone and a dictionary of terms to replace, and it does the rest.

The Folder Cloner applies changes to all `.doc` and `.docx` files in a provided directory, but all cloned files are rewritten in `.doc` format only. 

Replacement string changes are made:
* in the newly cloned folder name 
* in the file names of all newly cloned documents
* inside the main body of all newly cloned documents
* inside all headers and footers of all newly cloned documents
* inside all tables and nested tables of all newly cloned documents

**Note: The Folder Cloner only supports the Windows platform at the moment.**


<!-- ### Built With -->

<!-- * [Kivy](https://kivy.org/doc/stable/): a Python framework for developing user interface applications  -->


<!-- GETTING STARTED -->
## Getting Started

To get a local copy up and running follow these simple steps.

### Prerequisites

In order to use the Folder Cloner, you must first have Python and pip installed on your system. If you need assistance installing these prerequisites, see the folowing steps:
* Python is a programming language. All of this project's code base is written in Python. Download the latest version of [Python](https://www.python.org/downloads/) and install onto your local machine.

* Pip is the package installer for Python. Once Python is installed, open your local machine's command line and use the following command to utilize Python to install Pip:
```sh
python get-pip.py -g
```

Git is a version control system. In this project, Git is used to clone (copy) the most up-to-date project files from GitHub to your local machine. Download the latest version of [git](https://git-scm.com/download/win) and install on your local machine.

This project also relies on the underlying function of Microsoft Word to edit `.doc` and `.docx` files. A local installation of Microsoft Word is required to run this script. All other filetypes are duplicated into the cloned folders, but are not modified.


### Installation

1. Open the command line on your local machine.

2. Enter the following command to use Git to clone this repository to your local machine.
```sh
git clone https://github.com/asa-holland/folder-cloner.git
```
3. Enter the following command to use Pip to install this repository's dependencies.
```sh
pip install -r requirements.txt
```



<!-- USAGE EXAMPLES -->
## Usage

To use the Folder Cloner once installed, open the `main.py` file and add the following line item to the file:

```sh
clone_folder(directory="", replacement_dict_list=[])
```

Replace the path of the directory you want to clone, and a list of dictionaries of changes you want to make to the text of your cloned files and folders (see usage example below for further information on dictionary setup).


Run the Folder Cloner by opening command line, navigating to the installation folder and running:
```sh
python main.py
```

Voila, your folder and its contents have been successfully cloned and changed!


## Usage Example with Sample Files

To see an example of the Folder Cloner, navigate to the `//sample test` directory of this project. This folder contains a subfolder that we want to clone. This subfolder contains a few Word files filled with boilerplate text.

![Folder Cloner Use Example Original File][use-files-before]


Then, navigate to the root directory of this project and open up the `clone_test.py` file.

Inside, the `rep_list` variable is what is used to set the changes we want to make on the cloned folders and files. `rep_list` contains a list of dictionaries. Each element of the list (each dictionary) represents a single cloned/duplicate folder we want to create. So, in the example of the `rep_list` in the `//sample test` directory, we will be creating three folders from our root directory, each which will receive unique changes to the file names, folder name, and content.

```sh
rep_list = [
	{'Ipsum': 'Python\'s Something Completely Different', 'Lorem': 'Monty ', '123': 'foobar'}, 
	{'Ipsum': 'Python\'s Life of Brian', 'Lorem': 'Monty', '123': 'barfoo'},
	{'Ipsum': 'Python\'s Holy Grail', 'Lorem': 'Monty', '123': 'foofoo'}, 
]
```

Each dictionary in the `rep_list` contains key:value pairs separated by commas. Each key is a string that will be searched for in the document, and each corresponding value is a replacement string that will be used whenever the key is matched. So, in the first dictionary of `rep_list`:
```sh
{'Ipsum': 'Python\'s Something Completely Different', 'Lorem': 'Monty ', '123': 'foobar'}, 
```
... we can see that the string `'Ipsum'` will be replaced by the string `'Python\'s Something Completely Different'`, and so on.

Finally, to see the Folder Cloner in action, open the command line, navigate to the installation folder and run:
```sh
python clone_test.py
```

This duplicates our original folder (incorporating replacements into the folder name)...

![Folder Cloner Use Example Folders Result][use-folders-after]

...as well as making all desired replacements to the file names and content within each word document:

![Folder Cloner Use Example Files Result][use-files-after]

<!-- ROADMAP -->
## Roadmap

See the [open issues](https://github.com/asa-holland/folder-cloner/issues) for a list of proposed features (and known issues).



<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to be learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request



<!-- LICENSE -->
## License

Distributed under the MIT License. See [LICENSE](https://github.com/asa-holland/folder-cloner/LICENSE.txt) for more information.



<!-- CONTACT -->
## Contact

Asa Holland - [@AsaHolland404](https://twitter.com/AsaHolland404) - hollandasa@gmail.com

Project Link: [https://github.com/asa-holland/folder-cloner](https://github.com/asa-holland/folder-cloner)



<!-- ACKNOWLEDGEMENTS -->
## Acknowledgements

* [Eric Fossum](https://github.com/fossum) on GitHub solved a [particularly tricky issue](https://gist.github.com/rdapaz/63590adb94a46039ca4a10994dff9dbe/) encountered while jumpstarting Word to open desired files.
* [othneildrew](https://github.com/othneildrew) for creating the [template README file](https://github.com/othneildrew/Best-README-Template) that was used as the starting point for the README for this project. 





<!-- MARKDOWN LINKS & IMAGES -->
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=flat-square&logo=linkedin&colorB=555
[linkedin-url]: https://www.linkedin.com/in/asa-holland-a2a0b5b7/
[example-use]: images/example-use-folder-cloner.gif
[use-files-after]: images/sample_files_after.JPG
[use-files-before]: images/sample_files_before.JPG
[use-folders-after]: images/sample_folders_after.JPG
