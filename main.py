import reex
import gabcol

#문자열 검색
reex.print_re_mat()

#주민등록번호를 포함하고 있는 텍스트에서 모든 주민등록번호의 뒷자리를 * 문자로 변경
reex.print_re_sub()

#가비지 컬렉션
##레퍼런스 카운팅
gabcol.print_gc_refcnt()

##순환 참조
l = []
l.append(l)
del l    #참조 횟수는 1이지만 객체에는 더 이상 접근할 수 없는 가비지가 된다.

##세대 기반 가비지 컬렉터
gabcol.print_gc_generation()

##가비지 컬렉션 사용 중 메모리 누수 발생
gabcol.print_gc_memleak()
