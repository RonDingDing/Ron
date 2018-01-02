import xml.etree.ElementTree


tree = xml.etree.ElementTree.parse("test.xml") #解析一个xml并存到tree变量中
root = tree.getroot()                          #获取根节点
print(root.tag)                                #根节点的标签

"""
for child in root:                             #遍历根节点
    print(child.tag, child.attrib)             #打印子节点标签和属性
    for i in child:
        print("---->", i.tag, i.text)          #打印子节点的子节点的标签和属性
"""

"""
for node in root.iter("year"):                 #只遍历year节点
    print(node.tag, node.text)
"""

"""
for node in root.iter("year"):          #修改
    new_year = int(node.text) + 1
    node.text = str(new_year)
    node.set("updated", "yes")          #加入updated = "yes"属性
tree.write("xmltest.xml")
"""


"""
for country in root.findall('country'):        #删除
    rank = int(country.find('rank').text)
    if rank > 50:
        root.remove(country)
tree.write("xmltest.xml")
"""
import xml.etree.ElementTree


new_xml = xml.etree.ElementTree.Element("namelist")                                   #根节点
name = xml.etree.ElementTree.SubElement(new_xml, "name", attrib={"enrolled":"yes"})   #子节点1
age = xml.etree.ElementTree.SubElement(name, "age", attrib={"checked":"no"})          #子节点1的子节点
sex = xml.etree.ElementTree.SubElement(name, "sex")                                   #子节点2
age.text = "33"
sex.text = "Male"

name2 = xml.etree.ElementTree.SubElement(new_xml, "name", attrib={"enrolled":"no"})
age = xml.etree.ElementTree.SubElement(name2, "age")
sex = xml.etree.ElementTree.SubElement(name2, "sex")
age.text = "19"
sex.text = "Female"

with open("1.xml", "wb") as f:
    f.write(xml.etree.ElementTree.tostring(new_xml))                                 #写入文件
xml.etree.ElementTree.dump(new_xml)                                                  #打印new_xml
