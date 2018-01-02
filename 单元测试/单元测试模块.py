 
#单元测试开始
import unittest

from mydict import Dict

class TestDict(unittest.TestCase):

    def test_init(self):    #检查init方法
        d = Dict(a=1, b='test') 
        self.assertEqual(d.a, 1)   #d.a应该等于1
        self.assertEqual(d.b, 'test') #d.b应该等于2
        self.assertTrue(isinstance(d, dict)) #d应该是一个字典

    def test_key(self):
        d = Dict()
        d['key'] = 'value'
        self.assertEqual(d.key, 'value')

    def test_attr(self):
        d = Dict()
        d.key = 'value'
        self.assertTrue('key' in d)
        self.assertEqual(d['key'], 'value')

    def test_keyerror(self):
        d = Dict()
        with self.assertRaises(KeyError):
            value = d['empty']

    def test_attrerror(self):
        d = Dict()
        with self.assertRaises(AttributeError):
            value = d.empty

            
if __name__ == '__main__':
    unittest.main()
