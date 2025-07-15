from netmiko import ConnectHandler

device_info = {
    'device_type':'cisco_ios_telnet',
    'username':'admin',
    'password':'pass',
    'secret':'pass',
    'host':'10.32.1.2'
}

# configs = [
#     'int lo 0',
#     'ip add 1.1.1.1 255.255.255.255',
    
# ]

ctconfigs = [
    'int lo 1',
    'ip add 2.2.2.2 255.255.255.255',
    
]

# print(configs[0])

## print(device_info['device_type'])


access_cli = ConnectHandler(**device_info)
access_cli.enable()
# show_ip = access_cli.send_command('show ip int br')
# print(show_ip)

output = access_cli.send_config_set(ctconfigs)
print(output)