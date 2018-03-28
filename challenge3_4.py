# -*- coding: utf-8 -*-

import re
from datetime import datetime

def open_parser(filename):
    with open(filename) as logfile:
        pattern = (r''
                    '(\d+.\d+.\d+.\d+)\s-\s-\s'
                    '\[(.+)\]\s'
                    '"GET\s(.+)\s\w+/.+"\s'
                    '(\d+)\s'
                    '(\d+)\s'
                    '"(.+)"\s'
                    '"(.+)"'
                 )
        parsers = re.findall(pattern, logfile.read())
    return parsers

def main():

    logs = open_parser('nginx.log')
    ip_dict = {}
    url_dict = {}

    #TODO
    #('216.244.66.231', '09/Jan/2017:06:34:01 +0800', '/robots.txt', '502', '181', '-',
    # 'Mozilla/5.0 (compatible; DotBot/1.1; http://www.opensiteexplorer.org/dotbot, help@moz.com)')
    for i in logs:
        s1 = datetime.strptime(i[1], '%d/%b/%Y:%H:%M:%S %z')
        s2 = datetime(2017,1,11)
        if s1.date() == s2.date():
             if i[0] in ip_dict.keys():
                ip_dict[i[0]] += 1
             else:
                ip_dict[i[0]] = 1
    ip_dict = max(ip_dict.items(), key=lambda x: x[1])

    for i in logs:
        if i[3] == '404':
            if i[2] in url_dict.keys():
                url_dict[i[2]] += 1
            else:
                url_dict[i[2]] = 1
    url_dict = max(url_dict.items(), key=lambda x: x[1])

    return ip_dict,url_dict

if __name__ == '__main__':

    ip_dict,url_dict = main()
    print(ip_dict, url_dict)

