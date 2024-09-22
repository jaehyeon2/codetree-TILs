from collections import deque

n, m, fuel = map(int, input().split())

array = []
dx=[-1, 0, 0, 1]
dy=[0, -1, 1, 0]
passenger_count = 0
passenger_num = 0

s_array = [[0]*n for _ in range(n)]
e_array = [0]

for _ in range(n):
    array.append(list(map(int, input().split())))

tx, ty = map(int, input().split())
tx-=1
ty-=1

for num in range(1, m+1):
    sx, sy, ex, ey = map(int, input().split())
    s_array[sx-1][sy-1]=num
    e_array.append([ex-1, ey-1])


def find_start():
    temp = []
    q=deque()
    visited=[[-1]*n for _ in range(n)]
    visited[tx][ty]=0
    q.append((tx, ty))
    if s_array[tx][ty]!=0:
        return tx, ty, 0, s_array[tx][ty]
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if (nx<0 or ny<0 or nx>n-1 or ny>n-1):
                continue
            if (array[nx][ny]==1):
                continue
            if visited[nx][ny]!=-1:
                continue
            visited[nx][ny] = visited[x][y]+1
            q.append((nx, ny))
            if (s_array[nx][ny]!=0):
                temp.append((nx, ny, visited[nx][ny], s_array[nx][ny]))

    if (len(temp)==0):
        return -1, -1, -1, -1
    temp.sort(key=lambda x:(x[2], x[0], x[1]))

    return temp[0][0], temp[0][1], temp[0][2], temp[0][3]

def find_destination(dest_num):
    q=deque()
    visited=[[-1]*n for _ in range(n)]
    visited[tx][ty]=0
    q.append((tx, ty))
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if (nx<0 or ny<0 or nx>n-1 or ny>n-1):
                continue
            if (array[nx][ny]==1):
                continue
            if visited[nx][ny]!=-1:
                continue
            visited[nx][ny] = visited[x][y]+1
            q.append((nx, ny))
            if (nx==e_array[dest_num][0] and ny==e_array[dest_num][1]):
                return nx, ny, visited[nx][ny]
    return -1, -1, -1


while True:
    if (passenger_count==m):
        break
    tx, ty, l, snum = find_start()
    if tx==-1:
        fuel=-1
        break
    else:
        if fuel<l:
            fuel=-1
            break
        else:
            fuel-=l
            s_array[tx][ty]=0
    tx, ty, l = find_destination(snum)
    if tx==-1:
        fuel=-1
        break
    else:
        if fuel<l:
            fuel=-1
            break
        else:
            fuel+=l
            passenger_count+=1

if passenger_count!=m:
    fuel=-1
print(fuel)