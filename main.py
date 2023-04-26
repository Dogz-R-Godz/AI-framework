from main_importer import *





game_rotator={"snake":"minesweeper","minesweeper":"roller","roller":"donkery kong","donkery kong":"pong","pong":"tetris","tetris":"snake"} #impliment this properly later
game_requirements={"snake":[86,4],"minesweeper":[81,160],"roller":[5,2],"donkery kong":[30,3],"pong":[9,2],"tetris":[208,6]} #inputs and outputs for different games #snake is usially 34 inputs.
output_decoder={"snake":{1:"Left",2:"Up",3:"Down",4:"Right",0:"Right"},"minesweeper":{},"roller":{1:(1,0),2:(0,1)}}
backwards_decoder={"Left":"Right","Right":"Left","Up":"Down","Down":"Up"}
curr_game="snake"
bot=neat.NEAT(game_requirements[curr_game][0],game_requirements[curr_game][1])

AI_visual_mode=0 #0 is off, 1 is on (depending on the game, where the AI can see), 2 is just a better 1
evolving_neurons=False

oreintation="up"
if oreintation=="up":
    neurons_rows_columns=[15,3]
else:
    neurons_rows_columns=[3,15]
spacing=[500/neurons_rows_columns[0],300/neurons_rows_columns[1]]

if not evolving_neurons:
    for y in range(neurons_rows_columns[1]):
        for x in range(neurons_rows_columns[0]):
            bot.middle[len(bot.middle)+1]=((spacing[0]*x)+(spacing[0]/2)+500,(spacing[1]*y)+(spacing[1]/2)+100)
#textures
bots=bot.start(100,True,evolving_neurons,neurons_rows_columns)
screen = pygame.display.set_mode((1000, 500))
clock = pygame.time.Clock()
tape = pygame.image.load("tape.png").convert() #400,200
tape = pygame.transform.scale(tape, (40,20))
cool_mode=True

speed=5
warnings=[]
for x in range(len(bots)):
    warnings.append(0)
#testing_output=bot.get_output(test_inputs,bots[0])
#print(testing_output)
#curr_bot["score"]=1
#bots[5]["score"]=1
#bot.get_offspring([curr_bot,bots.pop(5)],True,1000,True) #never activate this again, This is why everything messed up.
curr_bot=bots.pop(0)
def run_correct_game(curr_game,pos,rotation,vel,inputs,death_laser_distance,training_mode,AI_visual_mode):
    if curr_game=="roller":
        new_pos,new_vel,instructions,death_laser_distance,new_rotation,inputs_for_AI,alive,score=roller.run_frame(pos,rotation,vel,inputs,death_laser_distance)
    elif curr_game=="snake":
        new_pos,new_rotation,instructions,new_vel,death_laser_distance,inputs_for_AI,alive,score=snake.run_frame(pos,rotation,vel,inputs,death_laser_distance,training_mode=training_mode,AI_visual_mode=AI_visual_mode) #rotation is the apple pos, vel is the body, and death_laser_distance is the hunger

    return new_pos,new_vel,instructions,death_laser_distance,new_rotation,inputs_for_AI,alive,score
pygame.init()
def start_new_game(curr_game):
    global speed,pos,vel,death_laser_distance,rotation,generation,generation_counter,proper_output,training_mode,AI_visual_mode
    if curr_game=="roller":
        #speed=10
        proper_output=(0,0)
        pos=(150,100)
        death_laser_distance=150
        vel=(0,0)
    elif curr_game=="snake":
        pos=(23,25)
        proper_output="Right"
        vel=[(23,25),(22,25),(21,25)]
        #apple_positions=random.randint(0,1)
        #if apple_positions==0:
            #rotation=random.choice([(random.randint(28,48),25),(random.randint(2,22),25),(25,random.randint(28,48)),(25,random.randint(2,22))])
        #else:
            #thing=random.choice([random.randint(28,48),random.randint(2,22)])
            #rotation=(thing,thing)
        rotation=(random.randint(1,50),random.randint(1,50))
        while rotation in vel or rotation == pos:
            rotation=(random.randint(1,50),random.randint(1,50))
            
        death_laser_distance=0
    elif curr_game=="minesweeper":
        vel={}
        free_spots=[]
        for x in range(50):
            for y in range(50):
                x2=x+1
                y2=y+1
                vel[x2,y2]="free"
                free_spots.append((x2,y2))
        for x in range(100):
            vel[free_spots.pop(random.randint(0,len(free_spots)-1))]="mine"
        #while rotation in vel or rotation == pos:
            #rotation=(random.randint(1,50),random.randint(1,50))
        
        death_laser_distance=0
    input_locations={}
    output_locations={}
    middle_locations={}
    connections={}

    #rotation=0
    curr_bot_2=curr_bot.copy()
    curr_bot_2.pop("identifier")
    #proper_output=(0,0)
    screen.fill((255,255,255))

    font = pygame.font.SysFont(None, 20)
    fps_text=f"Generation {generation}, bots left in curr generation: {generation_counter-(generation_counter-len(bots))}, FPS: {round(clock.get_fps(),2)}"
    pygame.draw.rect(screen,(255,255,255),[970-font.size(fps_text)[0],0,font.size(fps_text)[0]+30,25])
    fps=font.render(fps_text,True,(0,0,0))
    screen.blit(fps,(990-font.size(fps_text)[0],1))

    pos,vel,instructions,death_laser_distance,rotation,AI_inputs,alive,score=run_correct_game(curr_game,pos,rotation,vel,proper_output,death_laser_distance,training_mode=training_mode,AI_visual_mode=AI_visual_mode)#max(5-math.floor(pos[0]/4000),0)
    output1=bot.get_output(AI_inputs,bots[0])
    output=output1[1]
    for x in range(bot.inputs):
        input_locations[x]=((500+(x*(500/bot.inputs)))+(500/bot.inputs)/2,50)
        pygame.draw.circle(screen,((50*(1-round(AI_inputs[x+1])))+100,255,(50*(1-round(AI_inputs[x+1])))+100),input_locations[x],(min((500/bot.inputs)/3,15)))
    for x in range(bot.outputs):
        output_locations[x]=((500+(x*(500/bot.outputs)))+(500/bot.outputs)/2,450)
        if output[1]:
            pygame.draw.circle(screen,(50,255,50),output_locations[x],(min((500/bot.outputs)/2,25)))
        else:
            pygame.draw.circle(screen,(50,150,50),output_locations[x],(min((500/bot.outputs)/2,25)))
    for x in bot.middle:
        if evolving_neurons:
            position=[0,0]
            if bot.middle[x][0]>bot.inputs:
                x=x #first connection is from another middle neuron
                position[0]=middle_locations[bot.middle[x][0]-bot.inputs-bot.outputs]
            else:
                x=x #first connection is from an input
                position[0]=input_locations[bot.middle[x][0]-1]
            if bot.middle[x][1]>bot.outputs+bot.inputs:
                x=x #second connection is to another middle neuron
                position[1]=middle_locations[bot.middle[x][1]-bot.inputs-bot.outputs]
            else:
                x=x #second connection is to an output
                position[1]=output_locations[bot.middle[x][1]-bot.inputs-1]
                
            middle_locations[x]=(position[1][0]-round((position[1][0]-position[0][0])/2),position[1][1]-round((position[1][1]-position[0][1])/2))
            curr_bot_with_actual_neurons={}
            for y in curr_bot:
                if type(y)!=str:
                    try:curr_bot_with_actual_neurons[bot.identifiers[y]]=curr_bot[y]
                    except:curr_bot_with_actual_neurons[curr_bot["identifier"][y]]=curr_bot[y]
            for y in curr_bot_with_actual_neurons:
                if x+bot.inputs+bot.outputs in y:
                    pygame.draw.circle(screen,(0,255,0),middle_locations[x],5)
        else:
            pygame.draw.circle(screen,(0,255,0),bot.middle[x],5)

    curr_bot_2=curr_bot.copy()
    curr_bot_2.pop("identifier")
    if "warnings" in curr_bot_2.keys():curr_bot_2.pop("warnings")
    if "score" in curr_bot_2.keys():curr_bot_2.pop("score")

    for x in curr_bot_2:
        try:connections[bot.identifiers[x]]=curr_bot_2[x]
        except:connections[curr_bot["identifier"][x]]=curr_bot_2[x]
    for x in connections:
        point_1,point_2=0,0
        if x[1]<bot.inputs+bot.outputs+1:
            point_2=output_locations[x[1]-bot.inputs-1] #connection 2 is to an output
        else:
            if not evolving_neurons:
                point_2=bot.middle[x[1]-bot.inputs-bot.outputs] #connection 2 is to a middle neuron
            else:
                point_2=middle_locations[x[1]-bot.inputs-bot.outputs]
        if x[0]<bot.inputs+1:
            point_1=input_locations[x[0]-1] #connection 1 is from an input neuron
        else:
            if not evolving_neurons:
                point_1=bot.middle[x[0]-bot.inputs-bot.outputs] #connection 1 is from a middle neuron
            else:
                point_1=middle_locations[x[0]-bot.inputs-bot.outputs]

        if connections[x]<0:
            x=x
            pygame.draw.line(screen,((50*(1-(0-connections[x])))+100,(50*(1-(0-connections[x])))+100,255),point_1,point_2)
        elif connections[x]>0:
            x=x
            pygame.draw.line(screen,(255,(50*(1-(0-connections[x])))+100,(50*(1-(0-connections[x])))+100),point_1,point_2)
    x=x

generation=1
training_mode=False
generation_counter=len(bots)
start_new_game(curr_game)
boosted=2
curr_gen_best_bot=[]
best_score=-10000000000000000
alivent=0
running=True
dead=False



fps_timer=0
bot_brains=[]

bot_scores=[]
speed=10
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_SPACE:
                if boosted==0:
                    boosted=1
                    speed=250
                elif boosted==1:
                    boosted=2
                    speed=1000
                else:
                    boosted=0
                    speed=10
            if event.key==pygame.K_v:
                if AI_visual_mode==0:
                    AI_visual_mode=1
                elif AI_visual_mode==1:
                    AI_visual_mode=2
                else:
                    AI_visual_mode=0
            if event.key==pygame.K_p:
                if training_mode:training_mode=False
                else:training_mode=True
            if event.key==pygame.K_r:
                bot_name=input("Input the name of the bot you want to load: ")
                if bot_name!="nvm":
                    path=f"Bots\\{curr_game}\\{bot_name}.pkl"
                    file = open(path, 'rb')
                    data = pickle.load(file)
                    file.close()
                    for item in data:
                        bots.append(item)
                    print("All the bots you asked for have been included in the end of this generation")
                    generation_counter=len(bots)
                else:
                    print("Okay, voiding request.")
            #if event.key==pygame.K_t:
                #bot.add_neurons(5)
    #test_inputs={}
    
    old_pos=(pos[0],pos[1])
    pos,vel,instructions,death_laser_distance,rotation,AI_inputs,alive,score=run_correct_game(curr_game,pos,rotation,vel,proper_output,death_laser_distance,training_mode=training_mode,AI_visual_mode=AI_visual_mode)#max(5-math.floor(pos[0]/4000),0)
    
    #print(AI_inputs)

    output=bot.get_output(AI_inputs,bots[0])[1]
    if output[1]==0:
        if alivent>50:
            alivent=0
            alive=False
        else:
            alivent+=1
        #proper_output=(0,0)
        if backwards_decoder[output_decoder[curr_game][output[0]]]!=proper_output:
            proper_output=output_decoder[curr_game][output[0]]
    else:
        if backwards_decoder[output_decoder[curr_game][output[0]]]!=proper_output:
            proper_output=output_decoder[curr_game][output[0]]
        alivent=0
    #proper_output=(0,0) #for testing purposes only

    if not alive:
        dead=True
    else:
        dead=False

    
    

        
    
    if dead:
        if len(bots)!=1:
            if score==best_score:
                curr_gen_best_bot.append(curr_bot)
                best_score=score
            elif score>best_score:
                curr_gen_best_bot=[curr_bot]
                best_score=score
                
            
            bot_brains.append(curr_bot)
            bot_scores.append(score)
            curr_bot=bots.pop(0)
        else:
            warnings_2=warnings.copy()
            for x in range(len(bot_brains)-len(warnings)):
                warnings_2.append(0)
            bots_with_scores=bot.get_bots_with_score(bot_brains,bot_scores,warnings_2)
            species=bot.sort_bots(bots_with_scores,True)
            new_bots,new_bots_mutations=bot.breed_species(750,species,bots_with_scores,evolving_neurons)
            f = open(f"Bots\\{curr_game}\\{generation}_{best_score}.pkl","wb")
            pickle.dump(curr_gen_best_bot,f)
            curr_gen_best_bot=[]
            best_score=-10000000000000000
            f.close()

            bots=new_bots.copy()
            curr_bot=bots.pop(0)
            generation_counter=len(bots)
            test=0
            bot_brains=[]
            bot_scores=[]
            print("Created new generation")
            generation+=1
        if training_mode:
            pygame.display.update()
        start_new_game(curr_game)
        alivent=0
            #new_bots=bot.breed_species(1000,species,bots_with_scores)
            
        dead=False
    
    
    
    #if max(5-math.floor(pos[0]/4000),0)<starting_difficulty:            #relic of the past
        #print(f"New starting difficulty: {max(5-math.floor(pos[0]/4000),0)}")
        #starting_difficulty=max(5-math.floor(pos[0]/4000),0)
    font = pygame.font.SysFont(None, 20)
    if not training_mode:
        #pygame.draw.rect(screen,(255,255,255),[502,0,298,25])

        pygame.draw.rect(screen,(255,255,255),[0,0,500,500])
        pygame.draw.rect(screen,(0,0,0),[0,0,500,500],2)

        for x in instructions["rects"]:
            pygame.draw.rect(screen,x[1],[x[0][0],x[0][1],x[0][2]-x[0][0],x[0][3]-x[0][1]])
        
        for x in instructions["lines"]:
            pygame.draw.line(screen,x[2],(x[0][0],x[0][1]),(x[1][0],x[1][1]),x[3])
        
        

        for x in instructions["circles"]:
            pygame.draw.circle(screen,(0,255,0),(x[0][0],x[0][1]),x[1])
            
        for x in instructions["tape"]:
            screen.blit(tape,(x[0],x[1]))
        
        for x in instructions["text"]:
            img = font.render(x,True,(0,0,255))
            screen.blit(img, (510, 2))


        connections={}
        input_locations={}
        output_locations={}
        middle_locations={}
        connections={}
        for x in range(bot.inputs):
            input_locations[x]=((500+(x*(500/bot.inputs)))+(500/bot.inputs)/2,50)
            #pygame.draw.circle(screen, (175*(1-AI_inputs[x+1]),255,175*(1-AI_inputs[x+1])),((500)+(input_locations*(x+0.5)),40),3,0)
            pygame.draw.circle(screen,(175*(1-AI_inputs[x+1]),255,175*(1-AI_inputs[x+1])),input_locations[x],(min((500/bot.inputs)/3,15)))
        
    if fps_timer>50:
        fps_text=f"Generation {generation}, bots left in curr generation: {generation_counter-(generation_counter-len(bots))}, FPS: {round(clock.get_fps(),2)}"
        pygame.draw.rect(screen,(255,255,255),[970-font.size(fps_text)[0],0,font.size(fps_text)[0]+30,25])
            
        fps=font.render(fps_text,True,(0,0,0))
        screen.blit(fps,(990-font.size(fps_text)[0],1))
        fps_timer=0
    else:
        fps_timer+=1
    if not training_mode:
        pygame.display.update()
    clock.tick(speed)
    
    #new_pos,new_vel,instructions=run_correct_game(curr_game,pos,vel,inputs)
    #for x in instructions
    
        
