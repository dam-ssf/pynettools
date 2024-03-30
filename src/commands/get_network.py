import sys
from pynettools.ip import IP
from pynettools.get_netmask import get_netmask

def main():

    prog = sys.argv[0]
    args = sys.argv[1:]

    if len(args) == 0:
        print(f"Uso: {prog} [<ip> <netmask>|<cidr>]")
        sys.exit(1)

    if len(args) == 1 and IP.include_cidr(args[0]):
        ip, bits = args[0].split('/')
        try:
            netmask = get_netmask(int(bits))
        except ValueError as e:
            print("Número de bits de la máscara de red incorrecto")
            sys.exit(1)
    else:
        ip = args[0]
        netmask = args[1]

    try:
        ip = IP(ip)
    except ValueError as e:
        print("Dirección IP no válida")
        sys.exit(1)
    try:
        netmask = IP(netmask)
    except ValueError as e:
        print("Máscara de red no válida")
        sys.exit(1)

    network = ip.get_network(netmask)

    print(f"Red            : {network.to_bin()} ({network})")
    print(f"Máscara de red : {netmask.to_bin()} ({netmask})")
    print(f"Broadcast      : {(network | ~netmask).to_bin()} ({network | ~netmask})")

if __name__ == '__main__':
    main()