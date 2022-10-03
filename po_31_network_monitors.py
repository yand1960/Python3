import os


def host_is_valid(host: str) -> bool:
    command = f"ping {host} -4"
    result = os.popen(command).read().encode("windows-1251").decode("866")
    return result.find("TTL") > 0


def progress_bar(current: int, total: int, scale: int = 60) -> None:
    display = "*" * int(scale * current / total)
    print(f"\r{display}", end="")


if __name__ == "__main__":

    print("Start checking hosts")
    hosts = ["127.0.0.1", "ya.ru", "192.168.22.2", "orsk", "trpr"]
    counter = 1
    bad_hosts = []
    for host in hosts:
        # print(f"\rChecking {counter} of {len(hosts)}", end = "")
        progress_bar(counter, len(hosts), 20)
        counter += 1
        if not host_is_valid(host):
            print(f"\nHOST {host} IS BAD")
            bad_hosts.append(host)

    print("***************** RESULTS: Bad host ****************")
    for host in bad_hosts:
        print(host)
    print("****************************************************")