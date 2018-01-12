def tag(name, *content, cls=None, **attrs):
    """生成一个或多个HTML标签"""
    if cls is not None:
        attrs['class'] = cls
    if attrs:
        attr_str = ''.join(' %s="%s"' % (attr, value)
                     for attr, value in sorted(attrs.items()))
    else:
        attr_str = ''
    if content:
        return '\n'.join('<%s%s>%s</%s>' %
        (name, attr_str, c, name) for c in content)
    else:
        return '<%s%s />' % (name, attr_str)


print(tag)
#<function tag at 0x10206d1e0>  
from functools import partial
picture = partial(tag, 'img', cls='pic-frame') 
print(picture(src='wumpus.jpeg'))
#'<img class="pic-frame" src="wumpus.jpeg" />' ➌
print(picture)
#functools.partial(<function tag at 0x10206d1e0>, 'img', cls='pic-frame') ➍
print(picture.func)
#<function tag at 0x10206d1e0>
print(picture.args)
#('img',)
print(picture.keywords)
#{'cls': 'pic-frame'}
