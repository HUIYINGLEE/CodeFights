def simplifyPath(path):
    ss=path.split("/");
    stack=[]
    for x in ss:
        if x=='.':
            continue
        if x== '..':
            if len(stack):
                stack.pop()
            continue
        if len(x)<1:
            continue
        stack.append(x)
    p=''
    for x in stack:
        p+='/'+x
    if p=='':
        return '/'
    return p

