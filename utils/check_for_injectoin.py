def check_for_injection(querry):
    words = querry.split()
    keywords = ['SELECT', 'UPDATE', 'DELETE', 'CREATE', 'DROP', 'JOIN', 'WITH', 'INSERT']
    for i in range(1, len(words)):
        prev = words[i-1]
        if prev[-1] == ';' and words[i] in keywords:
            return False
    return True