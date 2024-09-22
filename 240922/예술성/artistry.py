from collections import deque

n=int(input())
half = n//2
array=[]
for _ in range(n):
    array.append(list(map(int, input().split())))
visited=[[False]*n for _ in range(n)]
group_numbering = [[0]*n for _ in range(n)]

dx=[-1, 1, 0, 0]
dy=[0, 0, -1, 1]

def rotate_square(num):
    before_array = [[0] * half for _ in range(half)]
    after_array = [[0] * half for _ in range(half)]

    if (num==1):
        ax, ay = 0, 0
    elif (num==2):
        ax, ay = 0, half+1
    elif (num==3):
        ax, ay = half+1, 0
    else:
        ax, ay = half+1, half+1
    
    for i in range(half):
        for j in range(half):
            before_array[i][j] = array[i+ax][j+ay]
    
    for i in range(half):
        for j in range(half):
            after_array[j][half-1-i] = before_array[i][j]

    for i in range(half):
        for j in range(half):
            array[i+ax][j+ay] = after_array[i][j]

def rotate_cross():
    
    after_array = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            after_array[n-j-1][i] = array[i][j]

    for i in range(n):
        array[half][i] = after_array[half][i]
        array[i][half] = after_array[i][half]

def rotate():
    rotate_square(1)
    rotate_square(2)
    rotate_square(3)
    rotate_square(4)
    rotate_cross()


def bfs(x, y, num):
    q=deque()
    init_num = array[x][y]
    q.append((x, y))
    visited[x][y]=1
    group_numbering[x][y]=num
    count=1
    while q:
        x, y = q.popleft()
        group_numbering[x][y]=num-1
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if nx<0 or ny<0 or nx>n-1 or ny>n-1:
                continue
            if visited[nx][ny]==True:
                continue
            if array[nx][ny]!=init_num:
                continue
            count+=1
            visited[nx][ny]=True
            
            q.append((nx, ny))
    return num, init_num, count

def cal_score():
    global visited, group_numbering
    group_info = []
    number = 1
    group_numbering = [[0]*n for _ in range(n)]
    visited=[[False]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if visited[i][j]==True:
                continue
            x, y, z = bfs(i, j, number)
            group_info.append([x-1, y, z])
            number+=1
    group_line = [[0]*len(group_info) for _ in range(len(group_info))]

    for x in range(n):
        for y in range(n):
            for i in range(4):
                nx=x+dx[i]
                ny=y+dy[i]
                if nx<0 or ny<0 or nx>n-1 or ny>n-1:
                    continue
                now = group_numbering[x][y]
                next = group_numbering[nx][ny]
                if now!=next:
                    if now<next:
                        group_line[now][next]+=1
                    else:
                        group_line[next][now]+=1
    
    score = 0
    for a in range(len(group_info)):
        for b in range(a+1, len(group_info)):
            score+=(group_info[a][2]+group_info[b][2])*group_info[a][1]*group_info[b][1]*(group_line[a][b]//2)
    
    return score

result = 0
# rotate()
result+=cal_score()
rotate()
result+=cal_score()
rotate()
result+=cal_score()
rotate()
result+=cal_score()
print(result)