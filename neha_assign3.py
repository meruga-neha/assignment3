
def test_str(s):
    d = {'upper_letter' : 0, 'lower_letter': 0}
    for c in s:
        if c.isupper():
            d['upper_letter'] += 1
        elif c.islower():
            d['lower_letter'] += 1
        else:
            pass
    print('the orignal string:',s)
    print('number of uppercase letters:', d['upper_letter'])
    print('number of lowercase letters:', d['lower_letter'])
test_str('The quick Brow Fox')