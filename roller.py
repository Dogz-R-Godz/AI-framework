from game_importer import *

def update_ball_position(ball_position, head_rotation, ball_velocity=(0,0), input_controls=(0,0), death_laser_distance=250, death_laser_speed=1):
    '''This is to fins the new ball position. The head rotation is in degrees, with 0 being straight up.'''
    gravity=1.02
    floor_height=40
    is_alive=True
    new_rotation=head_rotation
    head_rotation=0-head_rotation
    head_rotation+=90
    ball_radius=10
    head_radius=5
    distance=ball_radius+head_radius #distance from middle of head to middle of body
    head_position=(round(ball_position[0]+(distance*math.cos(math.radians(head_rotation)))),round(ball_position[1]+(distance*math.sin(math.radians(head_rotation))))) #current head position         

    new_rotation*=gravity

    on_ground=ball_position[1]-ball_radius<=floor_height

    new_velocity=(
        ball_velocity[0],
        max(min(ball_velocity[1]-gravity,3),-3)
    )
    if on_ground:
        if input_controls[0]==1:
            new_velocity=(new_velocity[0]-0.1,new_velocity[1])
            new_rotation+=0.07
        elif input_controls[1]==1:
            new_velocity=(new_velocity[0]+0.1,new_velocity[1])
            new_rotation-=0.07
        else:
            new_velocity=(round(new_velocity[0]*0.03,5),new_velocity[1])

    new_velocity=(round(max(min(new_velocity[0],death_laser_speed+0.25),0-(death_laser_speed+0.25)),8),round(new_velocity[1],8))

    new_position=(
        round(ball_position[0]+new_velocity[0],8),
        max((ball_position[1]+new_velocity[1]),floor_height+ball_radius) #capping the ball position to the floor
    )
    new_rotation=round(new_rotation,8)

    head_position_new=(round(new_position[0]+(distance*math.cos(math.radians(0-new_rotation+90)))),round(new_position[1]+(distance*math.sin(math.radians(0-new_rotation+90)))))

    if head_position_new[1]-head_radius<=floor_height:
        is_alive=False

    distance_moved=(min(new_position[0]+ball_radius,head_position_new[0]+head_radius)-min(ball_position[0]+ball_radius,head_position[0]+head_radius))
    death_laser_distance=death_laser_distance-death_laser_speed+distance_moved

    if death_laser_distance-ball_radius*2<=0:
        is_alive=False
    score=ball_position[0]
    

    return is_alive, new_position, new_rotation, head_position_new, new_velocity, death_laser_distance, score
#_,pos,rotation,_,vel,death,=update_ball_position((250,50),1,(0,0),(0,1))
#while True:
    #_,pos,rotation,_,vel,death,=update_ball_position(pos,rotation,vel,(0,1),death)

def run_frame(ball_position, head_rotation, ball_velocity, input_controls, death_laser_distance, death_laser_speed=3):

    instructions={"lines":[],"circles":[],"text":[],"rects":[],"tape":[]}
    alive,ball_position,head_rotation,head_position,ball_velocity,death_laser_distance,score=update_ball_position(ball_position, head_rotation, ball_velocity, input_controls, death_laser_distance, death_laser_speed)

    instructions["circles"].append(((150,ball_position[1]),10))
    instructions["circles"].append(((150+(head_position[0]-ball_position[0]),head_position[1]),5))


    for x in range(13):
        instructions["tape"].append((0-(ball_position[0]%40)+x*40,40))
    

    if death_laser_distance<=255:
        instructions["lines"].append(((155-death_laser_distance,40),(155-death_laser_distance,500),(255,0,0),5))

    head_rotation_2=head_rotation
    ball_velocity_2=ball_velocity
    death_laser_distance_2=death_laser_distance
    if head_rotation!=0:
        head_rotation_2=1/head_rotation_2
    if ball_velocity[0]!=0:
        ball_velocity_2=(max(min(1/ball_velocity_2[0],1),-1),max(min(ball_velocity_2[1],1),-1))
    if ball_velocity[1]!=0:
        ball_velocity_2=(max(min(ball_velocity_2[0],1),-1),max(min(1/ball_velocity_2[1],1),-1))
    if death_laser_distance!=0:
        death_laser_distance_2=1/death_laser_distance_2

    AI_inputs={1:head_rotation_2,2:ball_velocity_2[0],3:ball_velocity_2[1],4:death_laser_distance_2,5:1}
    #print(ball_position)
    #print(ball_velocity)
    #print(alive)

    return ball_position,ball_velocity,instructions,death_laser_distance,head_rotation,AI_inputs,alive,score
