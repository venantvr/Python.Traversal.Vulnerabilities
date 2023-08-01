# dotdotslash, forked from https://github.com/jcesarstef/dotdotslash

A tool to help you search for Directory Traversal Vulnerabilities.

Disclaimer : I needed something less focused on the use-case...

Made to run for many Linux VMs as possible. Still need to check for Windows.
Tested on the https://www.vulnhub.com/entry/zico2-1,210/ image from www.vulnhub.com.

## Benchmarks

Platforms that I tested to validate tool efficiency :

* [DVWA](https://github.com/ethicalhack3r/DVWA) (low/medium/high)
* [bWAPP](http://www.itsecgames.com/) (low/medium/high)

## Screenshots

![Screenshot](https://raw.githubusercontent.com/jcesarstef/dotdotslash/master/poc1.png)

![Screenshot](https://raw.githubusercontent.com/jcesarstef/dotdotslash/master/poc2.png)

![Screenshot](https://raw.githubusercontent.com/jcesarstef/dotdotslash/master/poc3.png)

## Installation

You can download the last version cloning this repository.

```
git clone https://github.com/jcesarstef/dotdotslash/
```

This tool was made to work with Python3.

## Usage

```
> python3 dotdotslash.py --help
usage: dotdotslash.py [-h] --url URL --string STRING [--cookie COOKIE]
                      [--depth DEPTH] [--verbose]

dot dot slash - A automated Path Traversal Tester. Created by @jcesrstef.

optional arguments:
  -h, --help            show this help message and exit
  --url URL, -u URL     Url to attack.
  --string STRING, -s STRING
                        String in --url to attack. Ex: document.pdf
  --cookie COOKIE, -c COOKIE
                        Document cookie.
  --depth DEPTH, -d DEPTH
                        How deep we will go?
  --verbose, -v         Show requests
```

## Example

```
> python3 dotdotslash.py \
--url "http://192.168.58.101/bWAPP/directory_traversal_1.php?page=a.txt" \
--string "a.txt" \
--cookie "PHPSESSID=089b49151627773d699c277c769d67cb; security_level=3"
```

## Todo

Take FuzzDb Payloads...
