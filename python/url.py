from urllib.parse import parse_qs

url = 'https://www.youtube.com/watch?v=RWVk4_uLlFA&index=12&list=PLOtl7M3yp-DX32N0fVIyvn7ipWKNGmwpp'
url = url.split('?')
my_values = parse_qs(url[1], keep_blank_values = True)
print(url, '\n', repr(my_values), '\n')
print(type(my_values))
print('v:    ', my_values.get('v'))
print('list: ', my_values.get('list'))
print('index:', my_values.get('index'))


