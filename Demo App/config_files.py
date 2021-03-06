from configparser import ConfigParser, ExtendedInterpolation

config = ConfigParser(interpolation=ExtendedInterpolation())

config['DEFAULT'] = {
    'created_by': 'Akhshy Ganesh',
    'version': '0.1',
    'app_title': 'demoApp',
}


def createConfig():
    print("Please enter the config data to create: \n")

    def sectionConfig():
        sec_name = input('Section name: ')
        config[sec_name] = {}
        nums_key = int(input('Total number of config key: values ? '))
        nums_key -= 1
        key = input("Please enter the key: ")
        value = input("Please enter the value: ")
        config[sec_name] = {
            key: value
        }

        for num_key in range(nums_key):
            key = input("Please enter the key: ")
            value = input("Please enter the value: ")
            config[sec_name][key] = value

    sectionConfig()
    with open('config.ini', 'w') as f:
        config.write(f)

    addSection = input("Want to add section? (Y/N): ").upper()
    while addSection == 'Y':
        sectionConfig()
        with open('config.ini', 'w') as f:
            config.write(f)
        addSection = input("Want to add section? (Y/N): ").upper()
