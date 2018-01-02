import configparser

config = configparser.ConfigParser()
config['DEFAULT'] = {
    'ServerAliveInterval':'45',
    'Compression':'yes',
    'CompressionLevel':'9'
}

config['bitbucket.org'] = {}
config['bitbucket.org']['User'] = 'hg'


topsecret = config['topsecret.server.com'] = {}
topsecret['Host Port'] = '50022'
topsecret['ForwardX11'] = 'no'

config['DEFAULT']['ForwardX11'] = 'yes'

with open('example.ini', 'w') as configfile:    #生成example.ini
    config.write(configfile)


"""
#读取配置文件
>>> import configparser
>>> config = configparser.ConfigParser()
>>> config.sections()
[]
>>> config.read('example.ini')
['example.ini']
>>> config.sections()
['bitbucket.org', 'topsecret.server.com']
>>> config.defaults()
OrderedDict([('serveraliveinterval', '45'), ('compression', 'yes'), ('compressionlevel', '9'), ('forwardx11', 'yes')])
>>> 'bitbuck.org' in config.sections()
False
>>> 'bitbucket.org' in config.sections()
True
>>> config['bitbucket.org']['User']
'hg'
>>> for key in config['bitbucket.org']:
...     print(key)
...
user
serveraliveinterval
compression
compressionlevel
forwardx11


#这里DEFAULT的配置是默认分发到其他所有节点中的，而且要用config.defaults()读取
>>> config['bitbucket.org']['compression']
'yes'

"""



#增删改查
#查
config = configparser.ConfigParser()
config.read('example.ini')
sections = config.sections()
print(sections)                             ##>>>['bitbucket.org', 'topsecret.server.com']
options = config.options('bitbucket.org')
print(options)                              ##>>>['user', 'serveraliveinterval', 'compression', 'compressionlevel', 'forwardx11']

#改
config.remove_section('bitbucket.org')      #删掉'bitbucket.org'节点


has_section = config.has_section('ron')     #判断是否存在'ron'节点
if not has_section:                         #没有则添加
    ron = config.add_section('ron')
ron['ron'] = 25
config.write(open('changed.ini', 'w'))
