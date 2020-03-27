# wifi_scanner
做一个 wifi 定位功能的时候需要测试，采集自己本机上的 wifi 热点信息。

----
一开始有一个**scapy** 这个包，可以[监控wifi](https://scapy.readthedocs.io/en/latest/usage.html#wireless-sniffing) 然后嗅探 热点信息，但是 mac 上试了下。

>The following command will display information similar to most wireless sniffers:
>
> ``` sniff(iface="ath0", monitor=True, prn=lambda x:x.sprintf("{Dot11Beacon:%Dot11.addr3%\t%Dot11Beacon.info%\t%PrismHeader.channel%\t%Dot11Beacon.cap%}"))```
>
>Note the monitor=True argument, which only work from scapy>2.4.0 (2.4.0dev+), that is cross-platform. It will in work in most cases (Windows, OSX), but might require you to manually toggle monitor mode.
>
>The above command will produce output similar to the one below:
>
>00:00:00:01:02:03 netgear      6L   ESS+privacy+PBCC
>
>11:22:33:44:55:66 wireless_100 6L   short-slot+ESS+privacy
>
>44:55:66:00:11:22 linksys      6L   short-slot+ESS+privacy
>
>12:34:56:78:90:12 NETGEAR      6L   short-slot+ESS+privacy+short-preamble
>

本地复现的时候发现循环发包 获取信息的时候 mac 地址和 强度 都是 `？？` 而且一直循环取。 在文档中也没找到合适的方法，
就换了个思路 找到一个  将python 转换成 objc 去调用 mac 自己的工具获取热点信息.[点击原文](https://clburlison.com/macos-wifi-scanning/)
