# Folder Cloner
Short script to duplicate ('clone') a directory and its contents. However, clones never come out exactly like their source material, so this script allows for text-based changes to be built into all Word files contained in the cloned directory.


# GRE Calculator
 Personal project to develop and design a calculator application that looks and functions like the classic on-screen calculator used on the Quantitative Measures section of the Graduate Records Examinations (GRE).

<!-- ABOUT THE PROJECT -->
## About The Project

[![GRE Calculator][use-gif-1]](https://github.com/asa-holland/GRE-calculator)

Ever had the tedious task of duplicating a Microsoft Word file and making small changes to the text throughout the document? Find and Replace is a valuable friend.

But what if your task requires multiple Word Docs to be changed? You'd need to open each document to use our friend Find and Replace. Not challenging, just time-consuming.

Let's add another layer to this onion. Let's say that instead of duplicating a set of Word files once, you needed to make multiple duplicates, each with small changes throughout. Now the time you're spending searching and replacing the text in all those documents has become quite the chore.

Sure, you could use Word's [Templating System](https://docs.microsoft.com/en-us/power-platform/admin/using-word-templates-dynamics-365), but that requires time and effrot to build a template to be made for each base file you want to duplicate. Maybe you've been passed a set of files that you didn't create, but the changes need to be made throughout.

Enter the Folder Cloner.

The Folder Cloner is a small script that abstracts away all those steps of finding and replacing so you can focus on getting your updated information where it needs to go. Provide the Folder Cloner a directory to clone and a dictionary of terms to replace, and it does the rest.

**Note: The Folder Cloner only supports the Windows platform at the moment.**


<!-- ### Built With -->

<!-- * [Kivy](https://kivy.org/doc/stable/): a Python framework for developing user interface applications  -->


<!-- GETTING STARTED -->
## Getting Started

To get a local copy up and running follow these simple steps.

### Prerequisites

In order to use the Folder Cloner, you must first have Python and pip installed on your system. If you need assistance installing these prerequisites, see the folowing steps:
* Python is a programming language. The majority of this project's code base is written in Python. Download the latest version of [Python](https://www.python.org/downloads/) and install onto your local machine.

* Pip is the package installer for Python. Once Python is installed, open your local machine's command line and use the following command to utilize Python to install Pip:
```sh
python get-pip.py -g
```

* Git is a version control system. In this project, Git is used to clone (copy) the most up-to-date project files from GitHub to your local machine. Download the latest version of [git](https://git-scm.com/download/win) and install on your local machine.

* This project also relies on the underlying function of Microsoft Word to edit `.doc` and `.docx` files. A local installation of Microsoft Word is required to run this script. 


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

Run the Folder Cloner by opening command line, navigating to the installation folder and running:
`python main.py`


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
[contributors-shield]: https://img.shields.io/github/contributors/github_username/repo.svg?style=flat-square
[contributors-url]: https://github.com/asa-holland/GRE-calculator/graphs/contributors
[forks-shield]: https://github.com/asa-holland/GRE-calculator.svg?style=flat-square
[forks-url]: https://github.com/asa-holland/GRE-calculator/network/members
[stars-shield]: https://github.com/asa-holland/GRE-calculator.svg?style=flat-square
[stars-url]: https://github.com/asa-holland/GRE-calculator/stargazers
[issues-shield]: https://github.com/asa-holland/GRE-calculator.svg?style=flat-square
[issues-url]: https://github.com/asa-holland/GRE-calculator/issues
[license-shield]: https://github.com/asa-holland/GRE-calculator.svg?style=flat-square
[license-url]: https://github.com/asa-holland/GRE-calculator/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=flat-square&logo=linkedin&colorB=555
[linkedin-url]: https://www.linkedin.com/in/asa-holland-a2a0b5b7/
[product-screenshot]: images/screenshot.png
[old-calculator-screenshot]: images/gre_calculator_old_version.JPG
[use-gif-1]: images/arithmetic1.gif
[use-gif-2]: images/arithmetic2.gif
[use-gif-3]: images/arithmetic3.gif
[use-gif-memory]: images/memory.gif
[use-gif-cce]: images/cce.gif