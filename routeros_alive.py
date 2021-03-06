import os
# Configure settings for project
# Need to run this before calling models from application!
os.environ.setdefault('DJANGO_SETTINGS_MODULE','learning_templates.settings')

import django
# Import settings
django.setup()

import napalm
from napalm_ros import ros
import requests
import socket
import routeros_api
from basic_app.models import Class_Model_Model1

def RouterOs_Query(cmd='/system/idenity',router_ip='8.8.8.8',username='azhe',password='sdlnet'):

    try:
        connection = routeros_api.RouterOsApiPool(router_ip, username, password)
        api = connection.get_api()
        print("\n################ connecting router #################\n")
        result = api.get_resource(cmd).get()
        connection.disconnect()
        print(result)

        return result

    except:
        print ('\nsomething goes wrong while deal with Router, please check')


try:


    router_ip = '198.19.1.21'
    router_port = 8728 # Use 8729 for api-ssl
    router_user = 'azhe'
    router_pass = 'sdlnet'

    driver = napalm.get_network_driver('ros')

    print('Connecting to', router_ip, "on port", router_port, "as", router_user)

    device = driver(hostname=router_ip, username=router_user,
                    password=router_pass, optional_args={'port': router_port})

    print('Opening ...')
    device.open()

    is_alive = device.is_alive()['is_alive']
    print(is_alive)

    device.close()

    # cmd1 = '/system/license'
    # cmd2 = '/system/identity'
    # cmd3 = '/system/resource'
    #
    # systemlicense = RouterOs_Query(cmd1,router_ip,username,password)
    # systemidentity = RouterOs_Query(cmd2,router_ip,username,password)
    # systemresource = RouterOs_Query(cmd3,router_ip,username,password)
    #
    # router_name = systemidentity[0]['name']
    # mgtIP = router_ip
    # # licenselevel = systemlicense[0]['nlevel']
    # version = systemresource[0]['version']
    # cpu = systemresource[0]['cpu']
    # cpu_frequency = systemresource[0]['cpu-frequency']
    # architecture_name = systemresource[0]['architecture-name']
    # board_name = systemresource[0]['board-name']
    #
    print("\n################ updating database #################\n")
    obj = Class_Model_Model1.objects.get(router_name = 'HK-GOIP')
    obj.alive = is_alive
    obj.save()

    print("\n################   complete!   ######################\n")

except:
    print ('\nsomething goes wrong while dealing with Router and updating database, please check')
