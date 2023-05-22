import re

def print_re_mat():
    print('문자열 검색\n')

    p = re.compile('[a-z]+')

    ##match메소드
    print('match메소드')

    print('정규식에 부합되는 경우')
    m = p.match("python")
    print(m)

    print('정규식에 부합되지 않는 경우')
    m = p.match("3 python")
    print(m)
    print()
    
    ##search메소드
    print('search메소드')
    
    print('정규식에 전부 부합되는 경우')
    m = p.search("python")
    print(m)
    
    print('정규식에 일부 부합되는 경우')
    m = p.search("3 python")
    print(m)
    print()
    
    ##findall메소드
    print('findall메소드')
    result = p.findall("life is too short")
    print(result)
    print()
    
    ##finditer메소드
    print('finditer메소드')
    result = p.finditer("life is too short")
    print(result)
    for r in result: print(r)
    print()


def print_re_sub():
    print("문자열 교체")
    data = """
    park 800905-1049118
    kim  700905-1059119
    """
    
    ##정규표현식을 사용하지 않은 코드
    print('정규표현식 미사용')
    result = []
    for line in data.split("\n"):
        word_result = []
        for word in line.split(" "):
            if len(word) == 14 and word[:6].isdigit() and word[7:].isdigit():
                word = word[:6] + "-" + "*******"
            word_result.append(word)
        result.append(" ".join(word_result))
    print("\n".join(result))
    
    ##정규표현식을 사용한 코드
    print('정규표현식 사용')
    pat = re.compile("(\d{6})[-]\d{7}")
    print(pat.sub("\g<1>-*******", data))
