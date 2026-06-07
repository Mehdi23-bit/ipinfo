import  sys,requests,ipaddress 
from  colorama import init ,Fore,Style
init()
argv=sys.argv
try:
    if len(argv) !=2:
        raise ValueError("Usage : ipinfo <ip> ")
    ip_addr=ipaddress.ip_address(argv[1])
    if ip_addr.is_loopback:
        raise ValueError(f"{ip_addr} is a loopback addr")
    if ip_addr.is_private:
        raise ValueError(f"{ip_addr} is a private addr")
    res = requests.get(f"https://ipinfo.io/{ip_addr}/json",timeout=5)
    res.raise_for_status()
    data = res.json()
    print(f'{Fore.CYAN}──────────────────────────')
    print('IP Info')
    print(f'──────────────────────────{Style.RESET_ALL}')
    print(f"{Fore.MAGENTA}    ip : {Fore.WHITE} {data.get('ip')} ")
    print(f"{Fore.MAGENTA}    city : {Fore.WHITE} {data.get('city')}")
    print(f"{Fore.MAGENTA}    country : {Fore.WHITE} {data.get('country')}")
    print(f"{Fore.MAGENTA}    org :  {Fore.WHITE} {data.get('org')}")
    print(f"{Fore.MAGENTA}    timezone : {Fore.WHITE} {data.get('timezone')}")
    print(f'{Fore.CYAN}──────────────────────────')
except requests.exceptions.ConnectionError:
    print(f"{Fore.RED} Connection Error (check your internet connection)")
except Exception as e:
    print(f"{Fore.RED}{e}{Style.RESET_ALL}")





