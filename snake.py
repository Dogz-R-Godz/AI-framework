from game_importer import *
steps_taken=0
apple_eaten=False
def run_frame(head_pos,apple_pos,body={},inputs="",hunger=0,size=(50,50),training_mode=False):
    global steps_taken,apple_eaten
    new_head_pos=list(head_pos)
    alive=True
    was_apple_eaten=apple_eaten
    steps_taken+=1
    instructions={"lines":[],"circles":[],"text":[],"rects":[],"tape":[]}
    if inputs=="Left":
        new_head_pos[0]-=1
        if tuple(new_head_pos)!=apple_pos:
            body_pos=body.pop()
            instructions["rects"].append(((body_pos[0]*10+4,body_pos[1],(body_pos[0]+1)*10,(body_pos[1]+1)*10),(255,255,255)))
            hunger+=1
        else:
            apple_eaten=True
            hunger=0
            steps_taken=0
            if len(body)!=size[0]*size[1]:
                apple_pos=(random.randint(1,size[0]),random.randint(1,size[1]))
                while apple_pos in body or apple_pos == new_head_pos:
                    apple_pos=(random.randint(1,size[0]),random.randint(1,size[1]))
        if new_head_pos[0]>=size[0] or new_head_pos[1]>=size[1] or new_head_pos[0]<=0 or new_head_pos[1]<=0:
            alive=False
        else:
            if tuple(new_head_pos) in body:
                alive=False
    elif inputs=="Right":
        new_head_pos[0]+=1
        if tuple(new_head_pos)!=apple_pos:
            body_pos=body.pop()
            instructions["rects"].append(((body_pos[0]*10+4,body_pos[1],(body_pos[0]+1)*10,(body_pos[1]+1)*10),(255,255,255)))
            hunger+=1
        else:
            apple_eaten=True
            hunger=0
            steps_taken=0
            if len(body)!=size[0]*size[1]:
                apple_pos=(random.randint(1,size[0]),random.randint(1,size[1]))
                while apple_pos in body or apple_pos == new_head_pos:
                    apple_pos=(random.randint(1,size[0]),random.randint(1,size[1]))
        if new_head_pos[0]>=size[0] or new_head_pos[1]>=size[1] or new_head_pos[0]<=0 or new_head_pos[1]<=0:
            alive=False
        else:
            if tuple(new_head_pos) in body:
                alive=False
    elif inputs=="Up":
        new_head_pos[1]-=1
        if tuple(new_head_pos)!=apple_pos:
            body_pos=body.pop()
            instructions["rects"].append(((body_pos[0]*10+4,body_pos[1],(body_pos[0]+1)*10,(body_pos[1]+1)*10),(255,255,255)))
            hunger+=1
        else:
            apple_eaten=True
            hunger=0
            steps_taken=0
            if len(body)!=size[0]*size[1]:
                apple_pos=(random.randint(1,size[0]),random.randint(1,size[1]))
                while apple_pos in body or apple_pos == new_head_pos:
                    apple_pos=(random.randint(1,size[0]),random.randint(1,size[1]))
        if new_head_pos[0]>=size[0] or new_head_pos[1]>=size[1] or new_head_pos[0]<=0 or new_head_pos[1]<=0:
            alive=False
        else:
            if tuple(new_head_pos) in body:
                alive=False
    elif inputs=="Down":
        new_head_pos[1]+=1
        if tuple(new_head_pos)!=apple_pos:
            body_pos=body.pop()
            instructions["rects"].append(((body_pos[0]*10+4,body_pos[1],(body_pos[0]+1)*10,(body_pos[1]+1)*10),(255,255,255)))
            hunger+=1
        else:
            apple_eaten=True
            hunger=0
            steps_taken=0
            if len(body)!=size[0]*size[1]:
                apple_pos=(random.randint(1,size[0]),random.randint(1,size[1]))
                while apple_pos in body or apple_pos == new_head_pos:
                    apple_pos=(random.randint(1,size[0]),random.randint(1,size[1]))
        if new_head_pos[0]>=size[0] or new_head_pos[1]>=size[1] or new_head_pos[0]<=0 or new_head_pos[1]<=0:
            alive=False
        else:
            if tuple(new_head_pos) in body:
                alive=False
            
    
    

    

    for x in range(size[0]):
        for y in range(size[1]):
            if (x,y) in body:
                instructions["rects"].append(((x*10,y*10,(x+1)*10,(y+1)*10),(255,0,0)))
            if [x,y] == new_head_pos:
                instructions["rects"].append(((x*10,y*10,(x+1)*10,(y+1)*10),(255,100,100)))
            elif (x,y) == apple_pos:
                instructions["rects"].append(((x*10,y*10,(x+1)*10,(y+1)*10),(0,255,0)))
    body.insert(0,tuple(new_head_pos))
    



    
    AI_inputs={}
    for x in range(32):
        AI_inputs[x+1]=0
    input_up_to=1
    if alive:
        if not training_mode:
            for DX,DY in [(1,0),(1,1),(0,1),(-1,1),(-1,0),(-1,-1),(0,-1),(1,-1)]:
                curr_pos=new_head_pos.copy()
                line_drawn_pos=()
                found_line_thing=False
                found_thing=False
                while not found_thing:
                    curr_pos=(curr_pos[0]+DX,curr_pos[1]+DY)
                    if curr_pos==apple_pos:
                        AI_inputs[input_up_to]=1
                        if not found_line_thing:
                            found_line_thing=True
                            instructions["lines"].append(((curr_pos[0]*10+4,curr_pos[1]*10+4),(new_head_pos[0]*10+4,new_head_pos[1]*10+4),(0,0,255),2))
                    if curr_pos in body:
                        AI_inputs[input_up_to+8]=(math.sqrt(curr_pos[0]^2+curr_pos[1]^2)/25)
                        if not found_line_thing:
                            found_line_thing=True
                            instructions["lines"].append(((curr_pos[0]*10+4,curr_pos[1]*10+4),(new_head_pos[0]*10+4,new_head_pos[1]*10+4),(0,0,255),2))
                    if curr_pos[0]>=size[0]-1 or curr_pos[1]>=size[1]-1 or curr_pos[0]<=0 or curr_pos[1]<=0:
                        AI_inputs[input_up_to+16]=(math.sqrt(curr_pos[0]^2+curr_pos[1]^2)/25)
                        found_thing=True
                        input_up_to+=1
                        if not found_line_thing:
                            found_line_thing=True
                            instructions["lines"].append(((curr_pos[0]*10+4,curr_pos[1]*10+4),(new_head_pos[0]*10+4,new_head_pos[1]*10+4),(0,0,255),2))
    AI_inputs[34]=1
    AI_inputs[33]=1-(0.014*math.sqrt(((new_head_pos[0]-apple_pos[0])*(new_head_pos[0]-apple_pos[0]))+((new_head_pos[1]-apple_pos[1])*(new_head_pos[1]-apple_pos[1]))))
    if hunger>=200:
        alive=False
    
    #if hunger>=200:
    apples=len(body)-3
    score=(steps_taken+((2^apples)+((apples*(1+apples*0.1))*500))-(apples*((0.25*steps_taken)*(1+(0.25*steps_taken)*0.33333)))) #score=steps+((2^apples)+(apples^2.1)*500)-(apples*((0.25*steps)^1.3))
        #score=(((len(body)-3)*1000))
    #else:
        #score=(((len(body)-3)*1000))+steps_taken*10

    #if new_head_pos[0]>=size[0] or new_head_pos[1]>=size[1] or new_head_pos[0]<=0 or new_head_pos[1]<=0:
       # if len(body)==3:
            #score=0
    
    
    if not alive:
        steps_taken=0
        apple_eaten=False


    #Ai inputs are raycast distances to apples, the snakes body, and the wall, the direction of the tail, and the direction it was just going in.



    return tuple(new_head_pos),apple_pos,instructions,body,hunger,AI_inputs,alive,score