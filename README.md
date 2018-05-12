# Event Bot
[![Build Status](https://api.travis-ci.org/TGmeetup/eventbot.svg?branch=master)](https://travis-ci.org/TGmeetup/eventbot/)
[![Donate](https://img.shields.io/badge/Donate-PayPal-green.svg)](https://www.paypal.me/tgmeetup/5)  

This is a bot who create event issue on [**TGmeetup/TGevents**](https://github.com/TGmeetup/TGevents/issues) repo.  

## Table of Contents
- [Install](#install)
- [Usage](#usage)
- [Development setup](#development-setup)
    - [Guide](#guide)
    - [Code style](#code-style)
    - [Tests](#tests)
- [Contributors](#contributors)
- [License](#license)

## Install
This project uses python3 on Unix-like and MacOS. Go check them out if you don't have them locally installed.
- Preinstall TGmeetup
```sh
$ sudo apt install python-setuptools
$ cd ~/ && git clone https://github.com/TGmeetup/TGmeetup.git
$ cd TGmeetup
$ cp API.cfg.sample API.cfg
$ make install
```
- Install eventbot
```sh
$ cd ~/ && git clone https://github.com/TGmeetup/eventbot.git
$ cd ~/eventbot
$ cp AuthKey.cfg.sample AuthKey.cfg
$ pip3 install -r requirements.txt
```

## Usage
```sh
$ cd ~/eventbot
$ python3 eventbot/eventbot.py
```

## Development setup
### Guide
```sh
$ sudo apt install python-setuptools
$ python3 -m venv venv
$ source venv/bin/activate
$ pip3 install -r requirements.txt
```

### Code style
Follow PEP 8
```sh
$ autopep8 --in-place --aggressive --max-line-length=90 <filename>
$ flake8 --exclude=venv,setup.py --max-line-length=90
```

### Tests
Using `pytest`.

## Contributors
Thanks to these contributors, you can see them all here: https://github.com/TGmeetup/eventbot/graphs/contributors

## License
MIT

