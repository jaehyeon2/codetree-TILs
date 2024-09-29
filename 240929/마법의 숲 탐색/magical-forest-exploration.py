from collections import deque

n, m, k = map(int, input().split())
n+=3

array=[]

down = [[2, 0], [1, -1], [1, 1]]
left = [[-1, -1], [0, -2], [1, -1], [1, -2], [2, -1]]
right = [[-1, 1], [0, 2], [1, 1], [2, 1], [1, 2]]
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def init_array():
    global array
    array = [[0]*m for _ in range(n)]

def check_down(x, y):
    for a, b in down:
        nx=x+a
        ny=y+b
        if nx<0 or ny<0 or nx>n-1 or ny>m-1:
            return False
        if array[nx][ny]!=0:
            return False
    return True

def check_left(x, y):
    for a, b in left:
        nx=x+a
        ny=y+b
        if nx<0 or ny<0 or nx>n-1 or ny>m-1:
            return False
        if array[nx][ny]!=0:
            return False
    return True

def check_right(x, y):
    for a, b in right:
        nx=x+a
        ny=y+b
        if nx<0 or ny<0 or nx>n-1 or ny>m-1:
            return False
        if array[nx][ny]!=0:
            return False
    return True

def move_golem(x, y, d):
    while True:
        if check_down(x, y):
            x+=1
        elif check_left(x, y):
            x+=1
            y-=1
            d = (d-1)%4
        elif check_right(x, y):
            x+=1
            y+=1
            d = (d+1)%4
        else:
            break
    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]
        if i==d:
            array[nx][ny]=3
        else:
            array[nx][ny]=1
    array[x][y]=2
    return x, y, d

def check_golem():
    if sum(array[0])!=0 or sum(array[1])!=0 or sum(array[2])!=0:
        return False
    return True

def escape_golem(x, y):
    q=deque()
    visited = [[False]*m for _ in range(n)]
    q.append((x, y))
    visited[x][y]=True
    max_v = 0
    while q:
        x, y = q.popleft()
        max_v = max(max_v, x)
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if nx<0 or ny<0 or nx>n-1 or ny>m-1:
                continue
            if visited[nx][ny]:
                continue
            if array[nx][ny]==0:
                continue
            if array[x][y]==1:
                if array[nx][ny]!=2:
                    continue
            visited[nx][ny]=True
            q.append((nx, ny))
    
    return max_v-2

init_array()
result=0
for _ in range(k):
    gy, gd = map(int, input().split())
    gx=1
    gy-=1
    gx, gy, gd = move_golem(gx, gy, gd)
    
    if check_golem()!=True:
        init_array()
        continue
    max_row = escape_golem(gx, gy)
    result+=max_row
    # break

print(result)