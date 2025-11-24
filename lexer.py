import re
TOKEN_RE = re.compile(r'\s*(?:(\d+)|([A-Za-z_]\w*)|(.))')
def tokenize(src):
    for num, ident, other in TOKEN_RE.findall(src):
        if num: yield ('NUM', int(num))
        elif ident: yield ('ID', ident)
        elif other and not other.isspace(): yield (other, other)
