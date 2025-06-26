#common.pyよりコピー　＆　手直し    ファイルの読み込みを行う
def read_input(filename):
    point_counter = 1
    with open(filename) as f:
        cities = []
        for line in f.readlines()[1:]: 
            xy = line.split(',')
            cities.append([point_counter,float(xy[0]), float(xy[1])])
            point_counter += 1
        return cities
#[ [1,x1,y1], [2,x2,y2] ... ]というように、[インデックス,x座標,y座標]のリストが作成される。




def distance(route):        #ルートの距離の2乗を計算
    dis = 0
    for i in range(1,len(route)):
        dis += (route[i][1] - route[i-1][1])*(route[i][1] - route[i-1][1]) + (route[i][2] - route[i-1][2])*(route[i][2] - route[i-1][2])
    dis += (route[0][1] - route[-1][1])*(route[0][1] - route[-1][1]) + (route[0][2] - route[-1][2])*(route[0][2] - route[-1][2])
    return dis
#### OK

import random
def make_random_route(pointlist):       #pointlistは[ [1,x1,y1,d1], [2,x2,y2,d2] ... ]のリスト
    return random.sample(pointlist, k=len(pointlist))       #シャッフルされたリスト
#### OK



def make_new_route(route_1,route_2):
    new_route = []
    half = len(route_1) // 2

    new_route.extend(route_1[:half])        #new_routeにroute_1の前半50%を追加
    for item in route_2:
        if item not in new_route:
            new_route.append(item)
            #route_2の順かつ、まだ含まれていないものをnew_routeに追加
    return new_route
#### OK

def check_destance(parent_route_1,parent_route_2,new_route):      #new_routeが元のルート以上の長さだった場合、False
    if distance(parent_route_1) and parent_route_2 > new_route:
        return True
    else:
        return False
#### OK


def make_genaration(route):
    generation = []
    for i in range(len(route)):
        generation[i] = make_random_route(route)        #第一世代の生成(経路のリスト)

    for i in range(len(route)):
        

    next_generation = []
    half = len(route) // 2.5
    

    #元の世代の上位40%を次世代に引き継いだリスト
    next_generation.append()   

    for i in range(len(route)):
    make_new_route(,)



# ----test-----

test_route = [ [1, float(1), float(1)],[5, float(5), float(5)],  [2,  float(2), float(2)],  [3,  float(3), float(3)], [4, float(4),float(4)]
              ]


print(test_route)
print(distance(test_route))

maked= make_random_route(test_route)
print(maked)
print(distance(maked))

new= make_new_route(test_route,maked)
print(new)
print(distance(new))

print(check_destance(test_route,maked,new))

print(make_genaration(test_route))
