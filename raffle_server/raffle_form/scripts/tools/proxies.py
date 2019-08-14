def load_proxies():
        raffle_proxies = []
        with open(r"/app/raffle_form/scripts/tools/config/proxies.txt","r") as proxies:
                if proxies.mode == "r":
                        for proxy in proxies:
                                proxy = proxy.strip()
                                raffle_proxies.append(proxy)
                proxies.close()
        return raffle_proxies


