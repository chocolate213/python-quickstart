
# map: Python里叫dict
# map初始化
map = {
    'k1': 'v1',
    'k2': 'v2',
    'k3': 'v3'
}

print("map: ", map)

print("k1", map['k1'])

# map put操作

map['k4'] = 'v4'

print('current map: ', map, '==')

# map 直接取不存在的key将会报错：

# map['k5']
# map 键相同值覆盖

# map get方法：第二个参数为没有key的默认值
n = map.get('k5', 'undefined')
print(n)

# map 判断map中是否存在key

exist = 'k6' in map
exist2 = 'k1' in map

print('key6 in map? ', exist)
print('key1 in map? ', exist2)

# map 删除

map.pop('k1')

print('current map: ', map)

# map 移除一个不存在的元素同样会报错：

# map.pop('k111')
# map放入顺序与存储顺序无关（HashMap）
