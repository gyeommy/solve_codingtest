def solution(video_len, pos, op_start, op_end, commands):
    answer = ''

    def split_time(time):
        a, b = time.split(":")
        return int(a)*60 + int(b)
    
    def fill_zero(num):
        if int(num) < 10:
            return num.zfill(2)
        
    def to_timestr(num):
        a = int(num/60)
        b = int(num%60)
        if a < 10:
            a = fill_zero(str(a))
        if b < 10:
            b= fill_zero(str(b))
        return f"{a}:{b}"

    video_len = split_time(video_len)
    pos = split_time(pos)
    op_start = split_time(op_start)
    op_end = split_time(op_end)
    
    for comm in commands:
        print(f"command: {comm}")
        if comm == 'prev':
            if op_start <= pos <= op_end:
                pos = op_end
                print(f"end로이동: {pos}")
            pos = pos - 10
            if pos < 0:
                pos = 0
            print(f"prev:{pos}")
        elif comm == 'next':
            if op_start <= pos <= op_end:
                pos = op_end
            pos = pos + 10
            if pos > video_len:
                pos = video_len
            print(f"next:{pos}")
    
    if op_start <= pos <= op_end:
        pos = op_end
        print(f"for문 종료 후:{pos}")
    
    
    if pos < 0:
        answer = "00:00"
    elif pos > video_len:
        answer = to_timestr(video_len)
    else:
        answer = to_timestr(pos)
    print(answer)
    return answer


'''
동영상의 길이 video_len
현재 재생위치 pos
오프닝 시작 시각 op_start
오프닝 끝 시각 op_end
사용자 입력 commands

len(video_len), len(pos), len(op_start), len(op_end)=5
"mm:ss" 분, 초가 한자리일 경우 0을 붙여 두자리로 나타냄

만약 commands가 prev이면 10초 앞으로
commands가 next이면 10초 뒤로
op_start< pos < op_end 일때 next 이면 op_end로 자동으로 건너뛴 후 10초를 더해주라고 함


ex) 01:05 → prev → 00:55
05:52 → next → 06:02

숫자가 10보다 작으면 앞에 0을 붙여주는 함수
def fill_zero(self):
    if int(self) < 10:
        self.zfill(2)

if op_start< pos < op_end:
    post = op_end

for com in command:
    if command == 'prev':

pos를 분, 초로 나누어 문자열로 반환

def split_pos(pos)
    a, b = pos.split(":")
    return a, b


def solution(video_len, pos, op_start, op_end, commands):
1. pos가 op_start와 op_end 사이에 있는 값인지 확인한다.
pos가 사이에 있으면 pos를 op_end로 이동한다.
2. commands를 확인한다.
prev시 00:00 보다 작으면 00:00을 return
next시 video_len보다 크면 video_len을 return

전부 초단위로 환산해서 계산하면 편하다.
1. pos를 분, 초로 나눈다.
2. op_start와 op_end를 분 초로 나눈다.

solution에서 return할 때에도 /60 %60 으로 pos를 만들어서 return한다.

pccp기출 1번 동영상 재생기 문제를 풀며
- 업무시간에 틈틈히 했다고는 하지만 한문제를 푸는데 2시간 이상 소요하였음
소회, 느낀점
1. 어떤 순서로 코드를 짜야할지 빠르게 생각해내는 능력이 부족하다.
- 머리속으로 순서도 그리는 능력?
2. 조건을 어떻게, 어떤식으로 세워야 할지 생각하지 못하는 경우가 있다.
→ 질문하기의 질문들을 보면서 알게된 조건문들
3. 테스트케이스에서 조건문을 빠뜨려 틀리는 경우가 있었다.
→ 질문하기의 6,7,9 테스트 케이스 틀렸다는 글의 경우와 똑같은 실수를 했음
'''