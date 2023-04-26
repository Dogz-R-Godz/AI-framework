from game_importer import *
steps_taken=0
gone_through=[]
gone_through_points=0
apple_eaten=False
def run_frame(head_pos,apple_pos,body={},inputs="",hunger=0,size=(50,50),training_mode=False,AI_visual_mode=False):
    global steps_taken,apple_eaten,gone_through,gone_through_points
    safeguard_direction={(0,1):"Up",(0,-1):"Down",(1,0):"Left",(-1,0):"Right"}
    new_head_pos=list(head_pos)
    alive=True
    let_the_younglings_live=False
    steps_taken+=1
    instructions={"lines":[],"circles":[],"text":[],"rects":[],"tape":[]}
    if inputs=="Left":
        new_head_pos[0]-=1
        if tuple(new_head_pos)!=apple_pos:
            body_pos=body.pop()
            instructions["rects"].append(((body_pos[0]*10+4,body_pos[1],(body_pos[0]+1)*10,(body_pos[1]+1)*10),(255,255,255)))
            hunger+=1
            if new_head_pos not in gone_through:
                gone_through.append(new_head_pos)
                gone_through_points+=0.3
            else:
                gone_through_points-=0.5
        else:
            apple_eaten=True
            hunger=0
            gone_through=[]
            gone_through_points=0
            steps_taken=0
            if len(body)!=size[0]*size[1]:
                apple_pos=(random.randint(1,size[0]),random.randint(1,size[1]))
                while apple_pos in body or apple_pos == new_head_pos:
                    apple_pos=(random.randint(1,size[0]),random.randint(1,size[1]))
        if new_head_pos[0]>=size[0] or new_head_pos[1]>=size[1] or new_head_pos[0]<=0 or new_head_pos[1]<=0:
            if let_the_younglings_live:
                found_safeguard=False
                for x,y in [(0,1),(1,0),(0,-1),(-1,0)]:
                    if not found_safeguard:
                        if head_pos[0]+x<size[0] and head_pos[1]+y<size[1] and head_pos[0]+x>0 and head_pos[1]+y>0:
                            if (head_pos[0]+x,head_pos[1]+y) not in body:
                                found_safeguard=True
                                new_head_pos=[head_pos[0]+x,head_pos[1]+y]
                                inputs=safeguard_direction[(x,y)]

                if not found_safeguard:
                    alive=False
            else:
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
            if new_head_pos not in gone_through:
                gone_through.append(new_head_pos)
                gone_through_points+=0.3
            else:
                gone_through_points-=0.5
        else:
            apple_eaten=True
            hunger=0
            gone_through=[]
            gone_through_points=0
            steps_taken=0
            if len(body)!=size[0]*size[1]:
                apple_pos=(random.randint(1,size[0]),random.randint(1,size[1]))
                while apple_pos in body or apple_pos == new_head_pos:
                    apple_pos=(random.randint(1,size[0]),random.randint(1,size[1]))
        if new_head_pos[0]>=size[0] or new_head_pos[1]>=size[1] or new_head_pos[0]<=0 or new_head_pos[1]<=0:
            if let_the_younglings_live:
                found_safeguard=False
                for x,y in [(0,1),(1,0),(0,-1),(-1,0)]:
                    if not found_safeguard:
                        if head_pos[0]+x<size[0] and head_pos[1]+y<size[1] and head_pos[0]+x>0 and head_pos[1]+y>0:
                            if (head_pos[0]+x,head_pos[1]+y) not in body:
                                found_safeguard=True
                                new_head_pos=[head_pos[0]+x,head_pos[1]+y]
                                inputs=safeguard_direction[(x,y)]
                if not found_safeguard:
                    alive=False
            else:
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
            if new_head_pos not in gone_through:
                gone_through.append(new_head_pos)
                gone_through_points+=0.3
            else:
                gone_through_points-=0.1
        else:
            apple_eaten=True
            hunger=0
            gone_through=[]
            gone_through_points=0
            steps_taken=0
            if len(body)!=size[0]*size[1]:
                apple_pos=(random.randint(1,size[0]),random.randint(1,size[1]))
                while apple_pos in body or apple_pos == new_head_pos:
                    apple_pos=(random.randint(1,size[0]),random.randint(1,size[1]))
        if new_head_pos[0]>=size[0] or new_head_pos[1]>=size[1] or new_head_pos[0]<=0 or new_head_pos[1]<=0:
            if let_the_younglings_live:
                found_safeguard=False
                for x,y in [(0,1),(1,0),(0,-1),(-1,0)]:
                    if not found_safeguard:
                        if head_pos[0]+x<size[0] and head_pos[1]+y<size[1] and head_pos[0]+x>0 and head_pos[1]+y>0:
                            if (head_pos[0]+x,head_pos[1]+y) not in body:
                                found_safeguard=True
                                new_head_pos=[head_pos[0]+x,head_pos[1]+y]
                                inputs=safeguard_direction[(x,y)]
                if not found_safeguard:
                    alive=False
            else:
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
            if new_head_pos not in gone_through:
                gone_through.append(new_head_pos)
                gone_through_points+=0.3
            else:
                gone_through_points-=0.1
        else:
            apple_eaten=True
            hunger=0
            gone_through=[]
            gone_through_points=0
            steps_taken=0
            if len(body)!=size[0]*size[1]:
                apple_pos=(random.randint(1,size[0]),random.randint(1,size[1]))
                while apple_pos in body or apple_pos == new_head_pos:
                    apple_pos=(random.randint(1,size[0]),random.randint(1,size[1]))
        if new_head_pos[0]>=size[0] or new_head_pos[1]>=size[1] or new_head_pos[0]<=0 or new_head_pos[1]<=0:
            if let_the_younglings_live:
                found_safeguard=False
                for x,y in [(0,1),(1,0),(0,-1),(-1,0)]:
                    if not found_safeguard:
                        if head_pos[0]+x<size[0] and head_pos[1]+y<size[1] and head_pos[0]+x>0 and head_pos[1]+y>0:
                            if (head_pos[0]+x,head_pos[1]+y) not in body:
                                found_safeguard=True
                                new_head_pos=[head_pos[0]+x,head_pos[1]+y]
                                inputs=safeguard_direction[(x,y)]
                if not found_safeguard:
                    alive=False
            else:
                alive=False
        else:
            if tuple(new_head_pos) in body:
                alive=False
            
    
    

    five_by_five=[(2,2),(1,2),(0,2),(-1,2),(-2,2),
                  (2,1),(1,1),(0,1),(-1,1),(-2,1),
                  (2,0),(1,0),(0,0),(-1,0),(-2,0),
                  (2,-1),(1,-1),(0,-1),(-1,-1),(-2,-1),
                  (2,-2),(1,-2),(0,-2),(-1,-2),(-2,-2)]
    nine_by_nine=[]
    for x in range(9):
        for y in range(9):
            x2,y2=x-4,y-4
            nine_by_nine.append((x2,y2))
    nine_by_nine_positions=[]
    for x,y in nine_by_nine:
        new_grid_pos_x,new_grid_pos_y=new_head_pos[0]+x,(new_head_pos[1]+y)
        if new_grid_pos_x<size[0] and new_grid_pos_x>=0 and new_grid_pos_y<size[1] and new_grid_pos_y>=0:
            nine_by_nine_positions.append((new_grid_pos_x,new_grid_pos_y))
        
    if AI_visual_mode==1 or AI_visual_mode==2:
        instructions["rects"].append(((0,0,500,500),(128,128,128)))

    for x in range(size[0]):
        for y in range(size[1]):
            if AI_visual_mode==1:
                if (x,y) in nine_by_nine_positions:
                    if (x,y) in body:
                        instructions["rects"].append(((x*10,y*10,(x+1)*10,(y+1)*10),(255,0,0)))
                    elif [x,y]==new_head_pos:
                        instructions["rects"].append(((x*10,y*10,(x+1)*10,(y+1)*10),(255,150,150)))
                    elif (x,y)==apple_pos:
                        instructions["rects"].append(((x*10,y*10,(x+1)*10,(y+1)*10),(0,255,0)))
                    else:
                        instructions["rects"].append(((x*10,y*10,(x+1)*10,(y+1)*10),(255,255,255)))
                else:
                    if (x,y) in body:
                        instructions["rects"].append(((x*10,y*10,(x+1)*10,(y+1)*10),(128,0,0)))
                    elif [x,y]==new_head_pos:
                        instructions["rects"].append(((x*10,y*10,(x+1)*10,(y+1)*10),(128,75,75)))
                    elif (x,y)==apple_pos:
                        instructions["rects"].append(((x*10,y*10,(x+1)*10,(y+1)*10),(0,128,0)))
            elif AI_visual_mode==2:
                if (x,y) in nine_by_nine_positions:
                    if (x,y) in body:
                        instructions["rects"].append(((x*10,y*10,(x+1)*10,(y+1)*10),(255,0,0)))
                    elif [x,y]==new_head_pos:
                        instructions["rects"].append(((x*10,y*10,(x+1)*10,(y+1)*10),(255,150,150)))
                    elif (x,y)==apple_pos:
                        instructions["rects"].append(((x*10,y*10,(x+1)*10,(y+1)*10),(0,255,0)))
                    else:
                        instructions["rects"].append(((x*10,y*10,(x+1)*10,(y+1)*10),(255,255,255)))
                else:
                    if (x,y)==apple_pos:
                        instructions["rects"].append(((x*10,y*10,(x+1)*10,(y+1)*10),(0,128,0)))
            elif AI_visual_mode==0:
                if (x,y) in body:
                    instructions["rects"].append(((x*10,y*10,(x+1)*10,(y+1)*10),(255,0,0)))
                elif [x,y]==new_head_pos:
                    instructions["rects"].append(((x*10,y*10,(x+1)*10,(y+1)*10),(255,150,150)))
                elif (x,y)==apple_pos:
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
        else:
            for DX,DY in [(1,0),(1,1),(0,1),(-1,1),(-1,0),(-1,-1),(0,-1),(1,-1)]:
                curr_pos=new_head_pos.copy()
                line_drawn_pos=()
                found_line_thing=False
                found_thing=False
                while not found_thing:
                    curr_pos=(curr_pos[0]+DX,curr_pos[1]+DY)
                    if curr_pos==apple_pos:
                        AI_inputs[input_up_to]=1
                    if curr_pos in body:
                        AI_inputs[input_up_to+8]=(math.sqrt(curr_pos[0]^2+curr_pos[1]^2)/25)
                    if curr_pos[0]>=size[0]-1 or curr_pos[1]>=size[1]-1 or curr_pos[0]<=0 or curr_pos[1]<=0:
                        AI_inputs[input_up_to+16]=(math.sqrt(curr_pos[0]^2+curr_pos[1]^2)/25)
                        found_thing=True
                        input_up_to+=1
    AI_inputs[34]=1
    AI_inputs[33]=1-(0.014*math.sqrt(((new_head_pos[0]-apple_pos[0])*(new_head_pos[0]-apple_pos[0]))+((new_head_pos[1]-apple_pos[1])*(new_head_pos[1]-apple_pos[1]))))
    if hunger>=2700:
        alive=False
    AI_inputs={}
    
    #three_by_three=[(1,1),(1,0),(1,-1),(0,1),(0,-1),(-1,-1),(-1,0),(1,0),(0,0)]
    counter=1
    for x,y in nine_by_nine:
        new_grid_pos_x,new_grid_pos_y=new_head_pos[0]+x,(new_head_pos[1]+y)
        if new_grid_pos_x<=size[0] and new_grid_pos_x>0 and new_grid_pos_y<=size[1] and new_grid_pos_y>0:
            if (new_grid_pos_x,new_grid_pos_y) in body:
                AI_inputs[counter]=1
            elif (new_grid_pos_x,new_grid_pos_y)==apple_pos:
                AI_inputs[counter]=0.5
            else:
                AI_inputs[counter]=0
        else:
            AI_inputs[counter]=1
        counter+=1
    new_head_pos_2=tuple(new_head_pos)
    apple_direction=(round(max(min(apple_pos[0]-new_head_pos_2[0],1),-1)),round(max(min(apple_pos[1]-new_head_pos_2[1],1),-1)))
    AI_inputs[82],AI_inputs[83],AI_inputs[84],AI_inputs[85]=0,0,0,0
    if apple_direction[0]==1:
        AI_inputs[82]=1
    elif apple_direction[0]==-1:
        AI_inputs[83]=1
    elif apple_direction[1]==1:
        AI_inputs[84]=1
    elif apple_direction[1]==-1:
        AI_inputs[85]=1

    AI_inputs[86]=1

    
    
    #if hunger>=200:
    apples=len(body)-3
    #score=(steps_taken+((2^apples)+((apples*(1+apples*0.1))*500))-(apples*((0.25*steps_taken)*(1+(0.25*steps_taken)*0.33333)))) #score=steps+((2^apples)+(apples^2.1)*500)-(apples*((0.25*steps)^1.3))
    score=gone_through_points+apples*500
        #score=(((len(body)-3)*1000))
    #else:
        #score=(((len(body)-3)*1000))+steps_taken*10

    #if new_head_pos[0]>=size[0] or new_head_pos[1]>=size[1] or new_head_pos[0]<=0 or new_head_pos[1]<=0:
       # if len(body)==3:
            #score=0
    
    
    if not alive:
        steps_taken=0
        gone_through=[]
        gone_through_points=0
        apple_eaten=False


    #Ai inputs are raycast distances to apples, the snakes body, and the wall, the direction of the tail, and the direction it was just going in.



    return tuple(new_head_pos_2),apple_pos,instructions,body,hunger,AI_inputs,alive,score
