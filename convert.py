import sys
import re

# dirty paste  . .)
header = """<!DOCTYPE html>
<html xmlns="http://www.w3.org/1999/xhtml">
 <head>
  <title>{}</title>
  <meta charset="utf-8"/>
 </head>
<body>
"""

footer = """ </body>
</html>
"""


def parse(txt):
    replaced = txt

    # parse Heading
    replaced = re.sub('^([A-Z., ]{9,})\n\n', r'<h1>\1</h1>', replaced)
    replaced = re.sub('([A-Z., ]{9,})\n\n', r'<h2>\1</h2>', replaced)

    # Bullet
    replaced = re.sub('([IVX]+).\n\n', r'<h2>\1.</h2>', replaced)

    # return to <br/>
    replaced = re.sub('\n', r'<br/>', replaced)

    # make code beautiful
    replaced = re.sub('(</h1>|</h2>)', r'\1\n\n', replaced)
    replaced = re.sub('(<br/>)', r'\1\n', replaced)

    # put header
    replaced = re.sub('<h1>(.*)</h1>', header.format(r'\1') + r'<h1>\1</h1>', replaced)

    # put footer
    replaced = re.sub('(\n)$', r'\1' + footer, replaced)

    return replaced


def io(file, action, data=''):
    f = open(file, action)
    if action in 'w':
        f.write(data)
        return True
    elif action in 'r':
        return f.read()
    f.close()


if __name__ == "__main__":
    try:
        txt_file = sys.argv[1]
        out_file = '.'.join(txt_file.split('.')[:-1]) + '.html'

        data = io(file=txt_file, action='r')
        result = parse(txt=data)
        io(file=out_file, action='w', data=result)
        sys.exit("OK. check {}".format(out_file))
    except IndexError:
        sys.exit("Please input filename.\nex) python3 {} rime.txt".format(sys.argv[0]))
    except IOError:
        sys.exit("I can't find {}!".format(sys.argv[1]))
else:
    sys.exit()
