from game_importer import *
import perlin_noise as Perlin_Noise


map_coordinates=[]
def initialise_coordinates(seed=876785687236876,starting_num=0,difficulty=1):
    global map_coordinates
    map_coordinates_2=[]
    noise = Perlin_Noise.PerlinNoise(octaves=max(1,difficulty),seed=seed)
    lowest_coord=0
    for x in range(100):
        map_coordinates_2.append(round(noise([(x+starting_num)/8,1/8])*8,5))
        if map_coordinates_2[x]<lowest_coord:
            lowest_coord=map_coordinates_2[x]
    for x in range(len(map_coordinates_2)):
        map_coordinates.append(round((map_coordinates_2[x]-lowest_coord+5)*4,5))
    map_coordinates
    return map_coordinates


def roller_physics(curr_position=[50,50],curr_velocity=[0,0],ground_gradient=0,ground_height=40,button_pressed=False):
    new_position=list(curr_position)
    new_velocity=[0,0]
    
    if new_position[1]!=round(ground_height,3):
        on_ground=False
        new_velocity[1]=max(min(curr_velocity[1]-0.02,5),-5)
        if curr_position[1]+min(new_velocity[1],5)<round(ground_height,3):
            new_position[1]=round(ground_height,3)
            new_velocity[1]=0
        else:
            new_position[1]=curr_position[1]+min(new_velocity[1],5)
    else:
        if ground_gradient>0:
            new_velocity[1]+=max(min(curr_velocity[0]*(curr_velocity[1]+round(ground_gradient*0.001,2)),5),-5)
        on_ground=True
        new_position[1]=max(round(ground_height,3),curr_position[1]+min(new_velocity[1]*0.001,5))
    if button_pressed:
        if on_ground:
            new_velocity[0]=max(min(curr_velocity[0]+0.1,5),-2)
            new_position[0]=max(curr_position[0]+new_velocity[0],50)
        else:
            new_velocity[0]=max(min(curr_velocity[0]-(curr_velocity[0]*0.001),5),-1)
            new_velocity[0]=max(min(new_velocity[0],5),-1)
            new_position[0]=max(curr_position[0]+new_velocity[0],50)
    else:
        if on_ground:
            new_velocity[0]+=max(min(curr_velocity[0]-0.05,5),0)
            new_position[0]=max(curr_position[0]+new_velocity[0],50)
        else:
            new_velocity[0]=max(min(curr_velocity[0]-(curr_velocity[0]*0.001),5),-1)
            new_velocity[0]=max(min(new_velocity[0],5),-1)
            new_position[0]=max(curr_position[0]+new_velocity[0],50)

    return [round(new_position[0],3),round(new_position[1],3)],[round(new_velocity[0],3),round(new_velocity[1],3)],on_ground
battery_counter=0
charger_on_screen=False
time_since_last_charger=0
distance_between_chargers=500
def run_frame(curr_pos,curr_vel,button_pressed,difficulty=1,battery=1,charger_pos=(500,50)):
    global map_coordinates
    global distance_between_chargers
    global charger_on_screen
    global battery_counter
    global time_since_last_charger
    instructions={"lines":[],"circles":[],"charger":[],"text":[],"walls":[],"rects":[]}
    ground_grad={0:(),1:()} #Fix the bug where it runs out of track to check
    find=True
    for x in range(5):
        x2=(curr_pos[0]/20)+x-2
        x_coord=((x2)*20)-curr_pos[0]%20
        if x_coord<curr_pos[0]:
            ground_grad[0]=x_coord
        if x_coord>=curr_pos[0] and find==True:
            ground_grad[1]=x_coord
            find=False
    for x in range(25):
        instructions["lines"].append((math.floor((x*20)-curr_pos[0]%10),round(map_coordinates[(x+int(math.floor((curr_pos[0]-50)/10)))*2])))
    if ground_grad[1]>=len(map_coordinates):
        map_coordinates=initialise_coordinates(876785687236876,ground_grad[0],difficulty)
    
    ground_gradient=round((map_coordinates[int(ground_grad[0])]-map_coordinates[int(ground_grad[1])]*2),8)
    bigger=max(ground_grad[1]/20,ground_grad[0]/20)
    smaller=min(ground_grad[1]/20,ground_grad[0]/20)
    ground_gradient_2=round((1/((map_coordinates[int(round(bigger))]-map_coordinates[int(round(smaller))])*200)),8)
    battery_counter+=1
    if battery_counter==100:
        battery=round(battery-0.01,3)
        battery_counter=0

    ground_height=round(map_coordinates[int(max(ground_grad[1],ground_grad[0])/20)]-(map_coordinates[int(max(ground_grad[1],ground_grad[0])/20)]*2-map_coordinates[int(min(ground_grad[1],ground_grad[0])/20)])*math.tan(math.radians(ground_gradient_2)),5)
    new_pos,new_vel,on_ground=roller_physics(curr_pos,curr_vel,ground_gradient,ground_height,button_pressed)
    
    if battery<=0:
        new_pos,new_vel=curr_pos,curr_vel
    if time_since_last_charger>3900+distance_between_chargers:
        if charger_pos[0]<50:
            distance_between_chargers+=50
            time_since_last_charger=0
            battery=1
            charger_pos=(-50,50)
        charger_on_screen=True
        instructions["charger"].append((charger_pos[0]-2,charger_pos[1]))
    else:
        time_since_last_charger+=max(min(new_vel[0],1),0)
    instructions["circles"].append(((50,new_pos[1]+10),10))
    if len(instructions["charger"])==1:
        inputs={1:1/new_pos[1],2:1/ground_height,3:{True:1,False:0}[on_ground],4:1-1/max(new_vel[0],1),5:1-1/max(new_vel[1],1),6:1-1/max(battery,1),7:1-1/max(instructions["charger"][0][0]-50,1),8:{True:1,False:0}[button_pressed],9:1,10:1} #inputs are: curr_y, ground_y, on_ground, curr_x_vel, curr_y_vel, battery_percentage, distance to next charger, button_pressed, bias 1, bias 2
    else:
        inputs={1:1/new_pos[1],2:1/ground_height,3:{True:1,False:0}[on_ground],4:1-1/max(new_vel[0],1),5:1-1/max(new_vel[1],1),6:1-1/max(battery,1),7:0,8:{True:1,False:0}[button_pressed],9:1,10:1} #inputs are: curr_y, ground_y, on_ground, curr_x_vel, curr_y_vel, battery_percentage, distance to next charger, button_pressed, bias 1, bias 2
    instructions["text"].append(f"Battery: {battery}, Score: {new_pos[0]}")
    alive=True
    if battery<0.01:
        alive=False
    return new_pos,new_vel,instructions,inputs,battery,alive

    

#pos=(100,100)
#vel=(0,0)
#on_ground=False
#while not on_ground:
    #print(f"{pos},{vel},{on_ground}")
    #pos,vel,on_ground=roller(pos,vel,-0.25,False)
#for _ in range(20):
    #print(f"{pos},{vel},{on_ground}")
    #pos,vel,on_ground=roller(pos,vel,0.25,False)