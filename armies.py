import pandas as pd
# import time

visited = {1}
# army = []
# class faction:
#     def __init__(self):
#         self.name = None
#         self.region = 

class faction:
    def __init__(self,name,region):
        self.name = name
        self.region = region

class region:
    def __init__(self):
        self.action = [[1,0],[0,1],[0,-1],[-1,0], 'back']
        self.act_ind = 0

    def act(self, decission):
        if (decission):
            if self.act_ind <=2:
                self.act_ind = 0
            # elif self.act_ind == 3:
            #     self.act_ind = 1
            else:
                self.act_ind = 1
        else:
            if self.act_ind == 4:
                self.act_ind = 0
            else:
                self.act_ind += 1
    def search(self, data):
        row = len(data)
        col = len(data[0])
        area = [[]]
        index = 0
        i = 0
        j = 0
        newPos = [0,0]
        army = []
        for i in range(0,row):
            for j in range(0,col):
                # print('j: ', j, 'i: ', i, 'logic: ', ((j,i)not in visited))
                if (data[i][j] != '#') and ((j,i) not in visited):
                    # print("======")
                    self.act_ind = 0
                    area = [[]]
                    index+=1
                    node = 1
                    last_node = 0
                    newPos[0] = j
                    newPos[1] = i
                    visited.add((newPos[0],newPos[1]))
                    area[0].append(newPos[0])
                    area[0].append(newPos[1])
                    first = 0
                    if data[i][j] != '.':
                        army.append(faction(data[i][j], index))
                            
                    while (node>0):
                        # time.sleep(0.25)
                        if self.act_ind == 4:
                            self.act(0)
                            if first == 0:
                                last_node = node
                                first = 1 
                            node-=1
                            # print("BACK", 'node: ', node)
                            # for i in area:
                            #     print(i)
                            if node != 0:
                                newPos[0] = area[node][0]
                                newPos[1] = area[node][1]
                            
                            continue
                        newPosbef = [newPos[0],newPos[1]]
                        newPos[0] = newPos[0] + self.action[self.act_ind][0]
                        newPos[1] = newPos[1] + self.action[self.act_ind][1]
                        
                        if (newPos[1]<0) or (newPos[1]>(row-1))\
                            or ((col-1)<newPos[0]) or (newPos[0]<0) or\
                            (data[newPos[1]][newPos[0]] == '#') or \
                            ((newPos[0],newPos[1]) in (visited)):
                            newPos[0] = newPosbef[0]
                            newPos[1] = newPosbef[1]
                            self.act(0)
                            
                        # elif data[newPos[1]][newPos[0]] == '#':
                        #     newPos[0] = newPosbef[0]
                        #     newPos[1] = newPosbef[1]
                        #     self.act(0)
                        
                        # elif ((newPos[0],newPos[1]) in (visited)):
                        #     newPos[0] = newPosbef[0]
                        #     newPos[1] = newPosbef[1]
                        #     self.act(0)
                        
                        else:
                            self.act(1)
                            visited.add((newPos[0],newPos[1]))
                            if data[newPos[1]][newPos[0]] != '.':
                                army.append(faction(data[newPos[1]][newPos[0]], index))
                            area.append([])
                            
                            if first == 1:
                                area[last_node].append(newPos[0])
                                area[last_node].append(newPos[1])
                                node = last_node+1
                                first = 0
                            else:
                                area[node].append(newPos[0])
                                area[node].append(newPos[1])
                                node+=1
                    # for sa in area:
                    #     print(sa)
        # for i in army:
        #     print(i.name, i.region)
        return(army)

df = pd.read_csv('input_exmpl.in')

for i in df:
    head = i
    data_count = int(i)

count=0
case=0
region_obj = []
result = {}
data_string = []
while case < data_count:
    visited = {1}
    data = []
    army = []
    N = int(df[head][count])
    count+=1
    M = int(df[head][count])
    count+=1
    
    
    for i in range(count,count+N):
        data.append(df[head][i])
        count+=1
        
    # #         if (df[head][count][j] not in {'#'}):
    # for qa in data:
    #     print(qa)
    region_obj.append(region())
    army_temp = region_obj[case].search(data)
    
    count_i = 0
    count_j = 0
    same_set ={1}
    contested_set = {1}
    not_zero = {1}
    state = 0
    result = {}
    # print("======")
    # for i in army_temp:
    #     print(i.name, i.region)
    #     print(i.region)
    #     print()
    for i in army_temp:
        for j in army_temp:
            if j != i:
                if (i.name,i.region) == (j.name,j.region):
                    if (i.name,i.region) in same_set:
                        state = 2
                        break
                    same_set.add((i.name,i.region))
                    state = 0
                elif (i.region == j.region):
                    state = 1
                    break
                else:
                    state = 0
        if state == 1:
            contested_set.add(i.region)
        elif state == 0:
            if i.name not in not_zero:
                not_zero.add(i.name)
                result[i.name] = 1
            else:
                result[i.name] += 1
        else:
            continue
    
    
    # f = open('out1.txt', 'a+')
    
    case+=1
    print('Case',str(case)+':')
    # f.write("Case " + str(case)+ ':' + '\n')
    for i in result:
        print(i,result[i])
        # f.write(str(i) + ' ' + str(result[i]) + '\n')
    print('contested', len(contested_set)-1)
    # f.write('contested' + ' ' + str(len(contested_set)-1)+ '\n')
    # f.close()