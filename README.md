![Demo Image 1](https://i.ibb.co/0YXmPDN/test01mod10-1.jpg)
![Demo Image 2](https://i.ibb.co/Jn4jryq/astronaut-spacesuit-reflection-144426-3840x21601.jpg)

# VatySiArt

VatySiArt is a simple program to generated an **ASCII art** from an *image* like the above one.

Avaiable for MacOS, Window and Linux.

## Requirements

- Python 3.x installed
- PILLOW package installed
You can install via:
```bash
pip install PILLOW
#or
pip3 install PILLOW
```

## Installation

Clone this repository to your computer

```bash
git clone https://github.com/LamkQmobile/VatySiArt.git
cd VatySiArt
```

## Usage

```bash
python3 vatisiart.py --i [Inputfile] --o [Outfile] --sc [Scale factor] --ft [Font size] --w [Word] --m [Mode]
```

- Input file and Out file are required. Others arguments if not input will be the default value.

- Scale factor: the ratio to scale the image, default value is 0.15.

- Font size: the size of the letter, default value is 15pt.

- Word: the character list to fill the image, default value is "01".

- Mode: 0 for sequential (like test1.jpg), 1 for random (like test2.1.jpg), default value is 1.

See the test file for easier understanding.

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
This project is released under GNU GPLv3 license. Read the link for more!

[GNU GPLv3](https://choosealicense.com/licenses/gpl-3.0/)

## Author

This project is created by **LamkQmobile** aka **Vatylcan**

> No such thing is useless, but there are thing you don't know how to use in a usefull way.