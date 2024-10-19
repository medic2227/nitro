import ctypes
import string
import os
import time

try:
    import requests
except ImportError:
    os.system('pip install requests')
    import requests

try:
    import numpy
except ImportError:
    os.system('pip install numpy')
    import numpy

try:
    import art
    from art import text2art
except ImportError:
    os.system('pip install art')
    import art
    from art import text2art
try:
    import colorama
    from colorama import Fore
except ImportError:
    os.system('pip install colorama')
    import colorama
    from colorama import Fore

colorama.init()

class NitroGen:
    def __init__(self):
        self.fileName = "Nitro.txt"

    def main(self):
        os.system('clear')
        print(f'\33]0;Nitro Generator and Checker\a', end='', flush=True)
        banner = text2art("Nitro Generator")
        print(Fore.GREEN + banner)
        try:
            num = int(input(Fore.YELLOW + "[?] How many Nitro links do you want to generate and check: "))
        except ValueError:
            print(Fore.RED + "Invalid input.")
            exit()

        valid = []
        invalid = 0
        chars = []
        chars[:0] = string.ascii_letters + string.digits

        c = numpy.random.choice(chars, size=[num, 16])
        for s in c:
            try:
                code = ''.join(x for x in s)
                url = f"https://discord.gift/{code}"

                result = self.quickChecker(url)

                if result:
                    valid.append(url)
                else:
                    invalid += 1
            except KeyboardInterrupt:
                break
            except Exception as e:
                print(f" Error | {url} ")

    def quickChecker(self, nitro: str):
        url = f"https://discordapp.com/api/v9/entitlements/gift-codes/{nitro}?with_application=false&with_subscription_plan=true"
        response = requests.get(url)

        if response.status_code == 200:
            print(Fore.GREEN)
            print(f"[!] Valid | {nitro} ", flush=True, end="" if os.name == 'nt' else "\n")
            with open("Nitro.txt", "w") as file:
                file.write(nitro)
            return True
        else:
            print(Fore.RED)
            print(f"[?] Invalid | {nitro} ", flush=True, end="" if os.name == 'nt' else "\n")
            return False

if __name__ == '__main__':
    Gen = NitroGen()
    Gen.main()
