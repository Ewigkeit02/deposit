'''
Copyright 2022 Ewigkeit02
License: GNU GPLv3 http://www.gnu.org/licenses/gpl.html
'''
def structure_checker(x, n=0):
    type_name = type(x).__name__

    if isinstance(x, (list, tuple, set, dict)):
        if not x:
            return f'{type_name} of nothing'

        n += 1
        if isinstance(x, dict):
            expression = lambda item, n: f'{structure_checker(item[0], n)} -> {structure_checker(item[1], n)}'
            s = counter(x.items(), expression, n)
        else:
            s = counter(x, structure_checker, n)
        return f'{type_name} of {s}'

    else:
        return type_name

def counter(iterable, expression, n):
    l = []
    d = {}
    get_key = lambda x: expression(x, n)

    for item in iterable:
        d[get_key(item)] = d.get(get_key(item), 0) + 1
    for k, v in d.items():
        v = str(v) + ' ' if v > 1 else ''
        l.append(f'{v}{k}')

    if len(l) > 1:
        sep = lambda x:'\n' + '    ' * x
        return '(' + sep(n) + (',' + sep(n)).join(l) + sep(n - 1) + ')'
    else:
        return l[0]

def structure_show(*args):
    s = structure_checker(args, -1)
    if s[:11] == 'tuple of (\n':
        print(structure_checker(args, -1)[11:-2])
    else:
        print(structure_checker(args, -1)[9:])
    return None
  
if __name__ == '__main__':
	print('case 1\n')
	structure_show(1, None, 'yes', False, (1, ), (()), ((), ()))
	print('\ncase 2\n')
	structure_show(False, True, 0., -5, 'apple', -5, [0., 1, 1., ('string', print)], [], {2: 3, 3: 4})
	print('\ncase 3\n')
	structure_show([1, {'123': 6, 9: False, True: None, '22': 22, 'rt': False}], {}, {})
	print('\ncase 4\n')
	structure_show()
	print('\ncase 5\n')
	structure_show([{(1, 2): 3, (1, ): 4 ,(0, 0): 5, (): 6}, {(22, 11): 90 ,(0, ): 2, (): 5, (7, 8): 9}])
	print('\ncase 6\n')
	structure_show({(1, ), (2, ), 1, 2, '1', 3}, {(1, ), (2, ), 1, 2, 3, '2'})
	print('\ncase 7\n')
	structure_show({(0, 'z'): ['a', [len, str]], (1, '2'): ['', [eval, bool]]})
	
'''
case 1

int,
NoneType,
str,
bool,
tuple of int,
tuple of nothing,
tuple of 2 tuple of nothing

case 2

2 bool,
float,
2 int,
str,
list of (
    2 float,
    int,
    tuple of (
        str,
        builtin_function_or_method
    )
),
list of nothing,
dict of 2 int -> list of (
        str,
        int
    )

case 3

list of (
    int,
    dict of (
        2 str -> int,
        int -> bool,
        bool -> NoneType,
        str -> bool
    )
),
2 dict of nothing

case 4

nothing

case 5

list of 2 dict of (
        2 tuple of 2 int -> int,
        tuple of int -> int,
        tuple of nothing -> int
    )

case 6

2 set of (
    3 int,
    2 tuple of int,
    str
)

case 7

dict of 2 tuple of (
        int,
        str
    ) -> list of (
        str,
        list of (
            builtin_function_or_method,
            type
        )
    )
'''
    
