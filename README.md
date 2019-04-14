### Test TextFSM 

Companion repository to the posts on [The Gratuitous Arp site](http://gratuitousarp.info/).

- [A quick example of using TextFSM to parse data from Cisco show commands - Python3 Version](http://gratuitousarp.info/a-quick-example-of-using-textfsm-to-parse-data-from-cisco-show-commands-python3-version/)
- [Building a Custom TextFSM Template](http://gratuitousarp.info/building-a-custom-textfsm-template/)

The test_textfsm.py script helps with template development and also in understanding what is returned.  Use the --verbose option for additional information.

### Test TextFSM for a given set of data and template

```
(txtfsm3) Claudias-iMac:textfsm3 claudia$ python test_textfsm.py -h

usage: test_textfsm.py [-h] [-v] template_file output_file

This script applys a textfsm template to a text file of unstructured data
(often show commands). The resulting structured data is saved as text
(output.txt) and CSV (output.csv).

positional arguments:
  template_file  TextFSM Template File
  output_file    Device data (show command) output

optional arguments:
  -h, --help     show this help message and exit
  -v, --verbose  Enable all of the extra print statements used to investigate
                 the results

Usage: ' python textfsm.py <template file> <show output file>'
(txtfsm3) Claudias-iMac:textfsm3 claudia$
```

### Examples
Download or git clone

```
(txtfsm3) Claudias-iMac:textfsm3 claudia$ tree
.
├── README.md
├── cisco-ios-show-stack-power-nei.template
├── cisco_ios_show_version.template
├── junos_show_route_summary.template
├── junos_show_route_summary.txt
├── lab-swtich-show-cmds.txt
├── output.csv
├── output.txt
├── requirements.txt
├── show-stack-power-neighbors-output.txt
└── test_textfsm.py

0 directories, 11 files
```

#### Using the junos\_show\_route\_summary.template

```
(txtfsm3) Claudias-iMac:textfsm3 claudia$ python test_textfsm.py
usage: test_textfsm.py [-h] [-v] template_file output_file
test_textfsm.py: error: the following arguments are required: template_file, output_file

(txtfsm3) Claudias-iMac:textfsm3 claudia$ python test_textfsm.py junos_show_route_summary.template junos_s
how_route_summary.txt


TextFSM Results Header:
['ASN', 'RTRID', 'INT', 'DEST', 'ROUTES', 'ACTIVE', 'HOLDDOWN', 'HIDDEN', 'SOURCE', 'SRC_ROUTES', 'SRC_ACT
IVE']
========================================
['2495', '164.113.193.221', 'inet.0', '762484', '1079411', '762477', '0', '12', '', '', '']
['2495', '164.113.193.221', 'inet.0', '', '', '', '', '', 'Direct', '1', '1']
['2495', '164.113.193.221', 'inet.0', '', '', '', '', '', 'Local', '1', '1']
['2495', '164.113.193.221', 'inet.0', '', '', '', '', '', 'BGP', '1079404', '762470']

['2495', '164.113.193.221', 'inet.0', '', '', '', '', '', 'Static', '5', '5']
['2495', '164.113.193.221', 'inet.2', '3073', '3073', '3073', '0', '0', '', '', '']
['2495', '164.113.193.221', 'inet.2', '', '', '', '', '', 'BGP', '3073', '3073']
['2495', '164.113.193.221', 'small.inet.0', '116371', '116377', '116371', '0', '0', '', '', '']
['2495', '164.113.193.221', 'small.inet.0', '', '', '', '', '', 'BGP', '116377', '116371']
['2495', '164.113.193.221', 'inet6.0', '66912', '103194', '66897', '0', '30', '', '', '']
['2495', '164.113.193.221', 'inet6.0', '', '', '', '', '', 'Direct', '3', '3']
['2495', '164.113.193.221', 'inet6.0', '', '', '', '', '', 'Local', '2', '2']
['2495', '164.113.193.221', 'inet6.0', '', '', '', '', '', 'BGP', '103185', '66888']
['2495', '164.113.193.221', 'inet6.0', '', '', '', '', '', 'Static', '4', '4']
['2495', '164.113.193.221', 'small.inet6.0', '31162', '31162', '31162', '0', '0', '', '', '']
['2495', '164.113.193.221', 'small.inet6.0', '', '', '', '', '', 'BGP', '31162', '31162']
['2495', '164.113.193.221', 'small.inet6.0', '', '', '', '', '', '', '', '']
========================================

```


#### Using the cisco\_ios\_show\_version.template

```
txtfsm3) Claudias-iMac:textfsm3 claudia$ python test_textfsm.py cisco_ios_show_version.template lab-swtic
h-show-cmds.txt


TextFSM Results Header:
['VERSION', 'ROMMON', 'HOSTNAME', 'UPTIME', 'RELOAD_REASON', 'RUNNING_IMAGE', 'HARDWARE', 'SERIAL', 'CONFI
G_REGISTER', 'MAC']
========================================
['15.2(2)E3', 'Bootstrap', 'artic-sw01', '4 days, 14 hours, 2 minutes', 'Reload command', 'c2960s-universalk9-mz.152-2.E3.bin', ['WS-C2960S-24TS-S'], ['FOC1709W1DT'], '0xF', ['70:10:5C:53:D4:80']]
========================================
```