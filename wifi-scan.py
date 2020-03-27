import objc
from pprint import pprint


def scan():
    bundle_path = '/System/Library/Frameworks/CoreWLAN.framework'
    objc.loadBundle('CoreWLAN',
                    bundle_path=bundle_path,
                    module_globals=globals())

    iface = CWInterface.interface()
    print(iface.bssid())
    print()
    # 查找指定的 网络sid
    concrete_ssid = None

    networks = iface.scanForNetworksWithName_includeHidden_error_(concrete_ssid, True, None)

    return_result =  {
        i.ssid(): {
            'RSSI': i.rssiValue(),
            'BSSID': i.bssid()
        }
        for i in networks[0].allObjects() if i.ssid() is not None
    }
    return_result["_connected_"] = {
        'SSID' : iface.ssid(),
        'BSSID': iface.bssid(),
        "RSSI" : iface.rssiValue(),
    }
    return return_result

pprint(scan())



