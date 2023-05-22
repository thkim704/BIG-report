import sys
import gc
import psutil

#레퍼런스 카운팅
def print_gc_refcnt():
    a = ['my string']
    print('변수 a의 레퍼런스 카운팅 :', sys.getrefcount(a))
    b = [a]
    c = { 'key': a }
    print('변수 a의 레퍼런스 카운팅 :', sys.getrefcount(a))
    print()
    del a

#세대 기반 가비지 컬렉터
def print_gc_generation():
    print('각 세대에 설정된 임계값')
    print(gc.get_threshold(), '\n')
    
    print('각 세대에 속한 객체 수')
    print(gc.get_count(), '\n')
    
    #수동으로 가비지 컬렉터 실행한 후
    gc.collect()
    print('가비지 컬렉터 실행 후\n각 세대에 속한 객체 수')
    print(gc.get_count(), '\n')

#메모리 사용량 출력함수
def print_memory_usage():
    process = psutil.Process()
    mem_info = process.memory_info()
    print(f"Memory Usage: {mem_info.rss / 1024 / 1024} MB")

class dumyobj:
    def __init__(self):
        self.data = [0] * 1000000

def create_objects():
    objects = []
    for i in range(100):
        obj = dumyobj()
        objects.append(obj)
    print_memory_usage()

#가비지 컬렉션 사용 중 메모리 누수 발생
def print_gc_memleak():
    for i in range(100):
        print(i+1, "번째 측정")
        create_objects()
        gc.collect()  # 가비지 컬렉션 수행
