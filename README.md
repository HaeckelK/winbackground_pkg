# winbackground_pkg

Basic functions to change Windows wallpaper.

## Installation

stop_and_search_api is not yet a package and cannot be installed via pip. Instead the repository may be cloned.

```bash
git clone https://github.com/HaeckelK/winbackground_pkg.git
```

## Requirements
Windows 10

## Usage

Assuming you have a folder called wallpapers with files test_image1.jpg to test_image4.jpg.

Choose background at random from files in a folder:
```python
from background.background import Background

bk = Background()
bk.change('testing\\test_image.jpg')
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](LICENSE.md)