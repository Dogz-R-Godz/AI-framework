from game_importer import *
class NEAT:
    def __init__(self,inputs,outputs):
        self.inputs=inputs
        self.outputs=outputs
        self.middle={} #if there are middle neurons, then they get the identifier of inputs+outputs+middle_neuron_number+1
        self.middle_2={}
        self.identifiers={}
        self.connections={}
        self.neuron_rows=0
    def start(self,bots=500,use_all_inputs=False,evolving_neurons=True,neurons_rows_columns=[0,0]): #neurons_rows_columns is 20,2
        all_bots=[]
        bots_percentage=bots/10
        if use_all_inputs:
            for bot_num in range(bots):
                if bot_num%bots_percentage==0:
                    print(f"{math.floor(bot_num/bots_percentage)*10+10}% done")
                curr_bot={}
                if evolving_neurons:
                    for output in range(self.outputs):
                        for input_thing in range(self.inputs):
                            output_2=output+self.inputs+1
                            input_2=input_thing+1
                            if (input_2,output_2) not in self.identifiers.values():
                                self.identifiers[len(self.identifiers)+1]=(input_2,output_2)
                                if input_2 in self.connections.keys():
                                    self.connections[input_2].append((len(self.identifiers),(input_2,output_2)))
                                else:
                                    self.connections[input_2]=[(len(self.identifiers),(input_2,output_2))]
                                identifier=len(self.identifiers)
                            else:
                                identifier=[k for k,v in self.identifiers.items() if v==(input_2,output_2)]
                                identifier=int(identifier[0])
                            curr_bot[identifier]=round(random.randint(-200,200)/100,3)
                    curr_bot["identifier"]=self.identifiers
                    all_bots.append(curr_bot)
                else:
                    for curr_input in range(self.inputs):
                        for middle in range(neurons_rows_columns[0]):
                            middle_2=middle+self.inputs+self.outputs+1
                            input_2=curr_input+1
                            if (input_2,middle_2) not in self.identifiers.values():
                                self.identifiers[len(self.identifiers)+1]=(input_2,middle_2)
                                if input_2 in self.connections.keys():
                                    self.connections[input_2].append((len(self.identifiers),(input_2,middle_2)))
                                else:
                                    self.connections[input_2]=[(len(self.identifiers),(input_2,middle_2))]
                                identifier=len(self.identifiers)
                            else:
                                identifier=[k for k,v in self.identifiers.items() if v==(input_2,middle_2)]
                                identifier=int(identifier[0])
                            curr_bot[identifier]=round(random.randint(-200,200)/100,3)

                            #self.connections[(curr_input,row)]
                    for column in range(neurons_rows_columns[1]):
                        if column==neurons_rows_columns[1]-1:
                            for row in range(neurons_rows_columns[0]):
                                for output in range(self.outputs):
                                    neuron_1=(row+(column*neurons_rows_columns[0]))+self.inputs+self.outputs+1
                                    output_1=output+1+self.inputs
                                    if (neuron_1,output_1) not in self.identifiers.values():
                                        self.identifiers[len(self.identifiers)+1]=(neuron_1,output_1)
                                        if neuron_1 in self.connections.keys():
                                            self.connections[neuron_1].append((len(self.identifiers),(neuron_1,output_1)))
                                        else:
                                            self.connections[neuron_1]=[(len(self.identifiers),(neuron_1,output_1))]
                                        identifier=len(self.identifiers)
                                    else:
                                        identifier=[k for k,v in self.identifiers.items() if v==(neuron_1,output_1)]
                                        identifier=int(identifier[0])
                                    curr_bot[identifier]=round(random.randint(-200,200)/100,3)
                        else:
                            for row in range(neurons_rows_columns[0]):
                                for row_2 in range(neurons_rows_columns[0]):
                                    neuron_1=(row+(column*neurons_rows_columns[0]))+self.inputs+self.outputs+1
                                    neuron_2=(row_2+((column+1)*neurons_rows_columns[0]))+self.inputs+self.outputs+1
                                    if (neuron_1,neuron_2) not in self.identifiers.values():
                                        self.identifiers[len(self.identifiers)+1]=(neuron_1,neuron_2)
                                        if neuron_1 in self.connections.keys():
                                            self.connections[neuron_1].append((len(self.identifiers),(neuron_1,neuron_2)))
                                        else:
                                            self.connections[neuron_1]=[(len(self.identifiers),(neuron_1,neuron_2))]
                                        identifier=len(self.identifiers)
                                    else:
                                        identifier=[k for k,v in self.identifiers.items() if v==(neuron_1,neuron_2)]
                                        identifier=int(identifier[0])
                                    curr_bot[identifier]=round(random.randint(-200,200)/100,3)
                curr_bot["identifier"]=self.identifiers
                all_bots.append(curr_bot)
        else:
            for bot_num in range(bots):
                if bot_num%bots_percentage==0:
                    print(f"{math.floor(bot_num/bots_percentage)*10+10}% done")
                curr_bot={}
                for output in range(self.outputs):
                    input_used=random.randint(1,self.inputs)
                    if (input_used,output+self.inputs+1) not in self.identifiers.values():
                        self.identifiers[len(self.identifiers)+1]=(input_used,output+self.inputs+1)
                        if input_used in self.connections.keys():
                            self.connections[input_used].append((len(self.identifiers),(input_used,output+self.inputs+1)))
                        else:
                            self.connections[input_used]=[(len(self.identifiers),(input_used,output+self.inputs+1))]
                        identifier=len(self.identifiers)
                    else:
                        identifier=[k for k,v in self.identifiers.items() if v==(input_used,output+self.inputs+1)]
                        identifier=int(identifier[0])
                    curr_bot[identifier]=round(random.randint(-200,200)/100,3)
                    if random.randint(0,10)==0:
                        input_2=random.randint(1,self.inputs)
                        while input_2==input_used:
                            input_2=random.randint(1,self.inputs)
                        if (input_2,self.inputs+1) not in self.identifiers.values():
                            self.identifiers[len(self.identifiers)+1]=(input_2,self.inputs+1)
                            if input_2 in self.connections.keys():
                                self.connections[input_2].append((len(self.identifiers),(input_2,self.inputs+1)))
                            else:
                                self.connections[input_2]=[(len(self.identifiers),(input_2,self.inputs+1))]
                            identifier=len(self.identifiers)
                        else:
                            identifier=[k for k,v in self.identifiers.items() if v==(input_2,self.inputs+1)]
                            identifier=int(identifier[0])
                        #curr_bot[identifier]=round(random.randint(-200,200)/100,3)
                curr_bot["identifier"]=self.identifiers
                all_bots.append(curr_bot)
        return all_bots
    def get_output(self,inputs_new,curr_bot):
        network_status={}
        for x in inputs_new:
            network_status[x]=inputs_new[x]
        curr_connections={}
        neuron_queue=list(inputs_new.keys())
        curr_bot_1=curr_bot.copy()
        if "identifier" in curr_bot_1.keys():
            curr_bot_1.pop("identifier")
        if "score" in curr_bot_1.keys():
            curr_bot_1.pop("score")
        if "warnings" in curr_bot_1.keys():
            curr_bot_1.pop("warnings")
        for x in curr_bot_1:
            try:
                curr_connections[self.identifiers[x]]=curr_bot[x]
            except:
                try:
                    curr_connections[curr_bot["identifier"][x]]=curr_bot[x]
                except:
                    print("An unexpected near fatal error occured. The error is at line 88.")
        while len(neuron_queue)>0:
            curr_neuron=neuron_queue.pop(0)
            network_status[curr_neuron]=round(min(max(network_status[curr_neuron],0),1))
            if curr_neuron>self.inputs and curr_neuron<self.inputs+self.outputs+1:
                x=x
            else:
                for x in self.connections[curr_neuron]:
                    if x[0] in curr_bot.keys():
                        if x[1][1] not in network_status.keys():
                            if x[1][1]>self.inputs+self.outputs:
                                neuron_queue.append(x[1][1])
                            
                            try:network_status[x[1][1]]=round(network_status[curr_neuron]*curr_connections[x[1]],5)
                            except:
                                try:network_status[x[1][1]]=round(network_status[curr_neuron]*curr_connections[x[1]],5)
                                except:print("An unexpected near fatal error occured. The error is at line 105.")
                        else:
                            try:network_status[x[1][1]]+=round(network_status[curr_neuron]*curr_connections[x[1]],5)
                            except:
                                try:network_status[x[1][1]]+=round(network_status[curr_neuron]*curr_connections[x[1]],5)
                                except:print("An unexpected near fatal error occured. The error is at line 110.")
        network_status_rounded={}
        network_status_unrounded={}
        for neuron in network_status:
            network_status_rounded[neuron]=round(min(max(network_status[neuron],0),1))
            network_status_unrounded[neuron]=min(max(network_status[neuron],0),1)
        final_output=[0,0]
        for neuron in network_status_rounded:
            if neuron>self.inputs and neuron<self.inputs+self.outputs+1:
                if network_status_rounded[neuron]>=final_output[1]:
                    final_output=[neuron-self.inputs,network_status_rounded[neuron]]
        if final_output==[0,0]:
            final_output=[self.outputs,0]
            
        return [network_status, network_status_rounded, network_status_unrounded],final_output
    

    def get_offspring(self,bots_to_combine=[],do_mutation=True,bots_to_make=10,include_parents=True,mutation_neuron=True,mutation_chances=2):
        """bots_to_combine must have the bots in a list. Each bot must be a dictionary with its score at the end. There must be an even number of bots to combine, or just one."""
        if len(bots_to_combine)>1:
            parent_1,p1_score=bots_to_combine[0].copy(),bots_to_combine[0]["score"]
            parent_2,p2_score=bots_to_combine[1].copy(),bots_to_combine[1]["score"]
        else:
            parent_1,p1_score,parent_2,p2_score=bots_to_combine[0],bots_to_combine[0]["score"],bots_to_combine[0],bots_to_combine[0]["score"]
        all_offspring=[]
        for _ in range(bots_to_make): #making all bots to be a perfect offspring of the two parents
            dominant_parent={}
            other_parent={}
            offspring_genes={}
            if p1_score>p2_score:
                if "score" in parent_1.keys():parent_1.pop("score")
                if "score" in parent_2.keys():parent_2.pop("score")
                if "warnings" in parent_1.keys():parent_1.pop("warnings")
                if "warnings" in parent_2.keys():parent_2.pop("warnings")
                dominant_parent=parent_1.copy()
                other_parent=parent_2.copy()
                for x in parent_1:
                    if x in parent_2.keys():
                        offspring_genes[x]=random.choice([parent_1[x],parent_1[x],parent_1[x],parent_2[x]]) #
                    else:
                        offspring_genes[x]=random.choice([parent_1[x],parent_1[x],parent_1[x]])
                for x in parent_2:
                    if x not in parent_1.keys():
                        if random.randint(0,2)==0:offspring_genes[x]=parent_2[x]
            elif p2_score>p1_score:
                if "score" in parent_1.keys():parent_1.pop("score")
                if "score" in parent_2.keys():parent_2.pop("score")
                if "warnings" in parent_1.keys():parent_1.pop("warnings")
                if "warnings" in parent_2.keys():parent_2.pop("warnings")
                dominant_parent=parent_2.copy()
                other_parent=parent_1.copy()
                for x in parent_2:
                    if x in parent_1.keys():
                        offspring_genes[x]=random.choice([parent_2[x],parent_2[x],parent_2[x],parent_1[x]]) #
                for x in parent_1:
                    if x not in parent_2.keys():
                        if random.randint(0,2)==0:offspring_genes[x]=parent_2[x]
            else:
                if "score" in parent_1.keys():parent_1.pop("score")
                if "score" in parent_2.keys():parent_2.pop("score")
                if "warnings" in parent_1.keys():parent_1.pop("warnings")
                if "warnings" in parent_2.keys():parent_2.pop("warnings")
                dominant_parent.update(parent_1)
                dominant_parent.update(parent_2)
                other_parent.update(parent_1)
                other_parent.update(parent_2)
                for x in parent_2:
                    if x in parent_1.keys():
                        offspring_genes[x]=random.choice([parent_2[x],parent_1[x]]) #
            for x in dominant_parent:
                if x not in offspring_genes:
                    offspring_genes[x]=dominant_parent[x]
            if other_parent!={}:
                other_parent_2=other_parent.copy()
                if "score" in other_parent_2.keys():other_parent_2.pop("score")
                if "identifier" in other_parent_2.keys():other_parent_2.pop("identifier")
                if "warnings" in other_parent_2.keys():other_parent_2.pop("warnings")
                for x in other_parent_2:
                    dominant_parent_2=dominant_parent.copy()
                    if "score" in dominant_parent_2.keys():dominant_parent_2.pop("score")
                    if "identifier" in dominant_parent_2.keys():dominant_parent_2.pop("identifier")
                    if "warnings" in dominant_parent_2.keys():dominant_parent_2.pop("warnings")
                    if x<max(list(dominant_parent_2.keys())):
                        if random.randint(0,2)!=0:
                            if x not in offspring_genes:
                                offspring_genes[x]=other_parent[x]
            all_offspring.append(offspring_genes)

        children_mutations={}
        if include_parents:
            children_mutations[0]=[]
            children_mutations[1]=[]
            for x in range(bots_to_make):
                children_mutations[x+2]=[]
        else:
            for x in range(bots_to_make):
                children_mutations[x+1]=[]
        mutation_decrypter={1:"new connection",2:"add neuron",3:"shift strength",4:"randomise strength",5:"alt+f4 a connection"}
        #print("do_mutation value in get_offspring:", do_mutation)
        if do_mutation:
            if "warnings" in other_parent.keys():other_parent.pop("warnings")
            if "warnings" in dominant_parent.keys():dominant_parent.pop("warnings")
            starting_identifiers=other_parent["identifier"].copy()
            starting_identifiers.update(dominant_parent["identifier"])
            for x in range(len(all_offspring)):
                mutations_done=0
                if mutation_neuron:mutations_possible=[1,2,3,4,5]
                else:mutations_possible=[1,3,4,5]
                while mutations_done!=-1:
                    if mutations_possible!=[]:
                        if len(all_offspring[x])>1:
                            if random.randint(0,(mutations_done+1)*mutation_chances)==0:
                                mutation=random.choice(mutations_possible)
                                if include_parents:children_mutations[x+2].append(mutation_decrypter[mutation])
                                else:children_mutations[x].append(mutation_decrypter[mutation])
                                if mutation==1: #new random connection
                                    if len(all_offspring[x])<len(starting_identifiers):
                                        connection_to_choose_from=set(starting_identifiers.keys())-set(all_offspring[x].keys())
                                        all_offspring[x][random.choice(list(connection_to_choose_from))]=round(random.randint(-100,200)/100,5)
                                        x=x
                                        mutations_possible.remove(1)
                                elif mutation==2: #add neuron
                                    connection_neuron=random.choice(list(all_offspring[x].keys()))
                                    possible=len(all_offspring[x])
                                    while connection_neuron=="identifier" and possible>1 or connection_neuron=="warnings":
                                        connection_neuron=random.choice(list(all_offspring[x].keys()))
                                    identifier_to_use=[]
                                    if self.identifiers[connection_neuron] not in self.middle.values():
                                        self.middle[len(self.middle)+1]=self.identifiers[connection_neuron] #add neuron to bot variables
                                        self.middle_2[len(self.middle)]=connection_neuron
                                    
                                    self.identifiers[len(self.identifiers)+1]=(self.identifiers[connection_neuron][0],self.inputs+self.outputs+len(self.middle))
                                    try:thing=all_offspring[x]["identifier"][connection_neuron][0]
                                    except:thing=self.identifiers[connection_neuron][0]
                                    if (thing,self.inputs+self.outputs+len(self.middle)) not in self.identifiers.values():
                                        self.identifiers[len(self.identifiers)+1]=(self.identifiers[connection_neuron][0],self.inputs+self.outputs+len(self.middle)) #identify neuron connections made
                                    else:
                                        identifier_to_use.append([k for k,v in self.identifiers.items() if v==(self.identifiers[connection_neuron][0],self.inputs+self.outputs+len(self.middle))])
                                    self.identifiers[len(self.identifiers)+1]=(self.inputs+self.outputs+len(self.middle),self.identifiers[connection_neuron][1])
                                    try:thing=all_offspring[x]["identifier"][connection_neuron][1]
                                    except:thing=self.identifiers[connection_neuron][1]
                                    if (self.inputs+self.outputs+len(self.middle),thing) not in self.identifiers.values():
                                        self.identifiers[len(self.identifiers)+1]=(self.inputs+self.outputs+len(self.middle),self.identifiers[connection_neuron][1]) #identify neuron connections made 2
                                    all_offspring[x][len(self.identifiers)-1]=1.0 #first connection to neuron being strength 1
                                    all_offspring[x][len(self.identifiers)]=all_offspring[x][connection_neuron] #second connection to neuron being the same strength as original connection
                                    all_offspring[x].pop(connection_neuron) #delete original connection
                                    mutations_possible.remove(2)
                                elif mutation==3: #shift strength
                                    connection_to_target=random.choice(list(all_offspring[x].keys()))
                                    possible=len(all_offspring[x])
                                    while connection_to_target=="identifier" and possible>1 or connection_to_target=="warnings":
                                        connection_to_target=random.choice(list(all_offspring[x].keys()))
                                    if possible>1:
                                        all_offspring[x][connection_to_target]=round(all_offspring[x][connection_to_target]+round(random.randint(-10,10)/1000,5),5)
                                    mutations_possible.remove(3)
                                elif mutation==4: #randomise strength
                                    connection_to_target=random.choice(list(all_offspring[x].keys()))
                                    possible=len(all_offspring[x])
                                    while connection_to_target=="identifier" and possible>1 or connection_to_target=="warnings":
                                        connection_to_target=random.choice(list(all_offspring[x].keys()))
                                    all_offspring[x][connection_to_target]=round(random.randint(-100,200)/100,5)
                                    mutations_possible.remove(4)
                                elif mutation==5: #delete a connection
                                    connection_to_alt_f4=random.choice(list(all_offspring[x].keys()))
                                    possible=len(all_offspring[x])
                                    while connection_to_alt_f4=="identifier" and possible>1 or connection_to_alt_f4=="warnings":
                                        connection_to_alt_f4=random.choice(list(all_offspring[x].keys()))
                                    all_offspring[x].pop(connection_to_alt_f4)
                                    mutations_possible.remove(5)
                                mutations_done+=1
                            else:mutations_done=-1
                    else:
                        mutations_done=-1
                all_offspring[x]["identifier"]=self.identifiers
        #print(parent_1)
        #print(parent_2)
        #print(all_offspring)
        if include_parents:
            all_offspring.insert(0,parent_1)
            all_offspring.insert(0,parent_2)
        #for x in all_offspring:

        
        return all_offspring,children_mutations
                           


    def sort_bots(self,bots,warn_bots=False):
        species={}#1:[list(bots.pop(0).keys())]
        warnings=[]
        found_home=False
        for x in range(len(bots)):
            found_home=False
            for y in species:
                if tuple(bots[x].keys())==y:
                    species[y].append([list(bots[x].keys()),list(bots[x].values())]) #connections, strengths of connections, score, warnings
                    found_home=True
            if not found_home:
                species[tuple(bots[x].keys())]=[[list(bots[x].keys()),list(bots[x].values())]] #connections, strengths of connections, score, warnings
                found_home=True
        if warn_bots:
            species_score_averages={}
            for x in species:
                curr_species_average=0
                curr_species_brains=0
                for y in species[x]:
                    curr_species_average+=y[1][0]
                    curr_species_brains+=1
                species_score_averages[x]=(curr_species_average/curr_species_brains)
            for x in species:
                for y in range(len(species[x])-1):
                    if species[x][y][1][0]<=species_score_averages[x]:
                        if species[x][y][1][1]>=3:
                            species[x].pop(y)
                            if species[x]==[]:
                                species.pop(x)
                        else:
                            
                            species[x][y][1][1]+=2
                    else:
                        if species[x][y][1][1]>=1:
                            species[x][y][1][1]-=1

        return species
    

    def breed_species(self,ammount_of_new_bots=100,species=[],bots_with_score=[],mutation_neuron=True):
        combos=[]
        species_2_organised={}
        all_bots_in_order={}
        identifiers={}
        bots_percentage=ammount_of_new_bots/10
        scores=[]
        for x in bots_with_score:
            if tuple(x.keys()) in identifiers.keys():identifiers[tuple(x.keys())]+=1
            else:identifiers[tuple(x.keys())]=0
            x2=x.copy()
            x2["warnings"]=species[tuple(x.keys())][identifiers[tuple(x.keys())]][1][1]
            if x2["score"] in all_bots_in_order.keys():all_bots_in_order[x2["score"]].append(x2)
            else:all_bots_in_order[x2["score"]]=[x2]
        scores=sorted(all_bots_in_order.keys())
        scores.reverse()
        for x in scores:
            species_2_organised[x]=all_bots_in_order[x]
        done_breeding=False
        curr_combo=[]
        final_bots=[]
        final_bots_mutations=[]
        bot_score_number=list(species_2_organised.keys())
        while len(final_bots)<10:
            for x in species_2_organised[bot_score_number[0]]:
                final_bots.append(x)
            bot_score_number.pop(0)
        while len(final_bots)>10:
            final_bots.pop()
        bots_number=0
        while done_breeding==False:
            for x in species_2_organised:
                for y in species_2_organised[x]:
                    if bots_number<ammount_of_new_bots:
                        if bots_number%bots_percentage==0:
                            print(f"{math.floor(bots_number/bots_percentage)*10+10}% done")
                        if curr_combo==[]:
                            curr_combo.append(y)
                        else:
                            curr_combo.append(y)
                            curr_bot_thing=self.get_offspring(curr_combo,do_mutation=True,bots_to_make=8,include_parents=True,mutation_neuron=mutation_neuron,mutation_chances=10) #(curr_combo,True,8,True,mutation_neuron)
                            final_bots+=curr_bot_thing[0]
                            final_bots_mutations.append(curr_bot_thing[1])
                            bots_number+=10
                            combos.append([curr_combo[0],curr_combo[1]])
                            curr_combo=[]
                    else:
                        done_breeding=True

            #species_2_organised_2

        return final_bots,final_bots_mutations
    def get_bots_with_score(self,bots,score=[],warnings=[]):
        bots_with_scores=[]
        for x in range(len(bots)-1):
            dict_with_score={"score":score[x]}
            dict_with_score.update({"warnings":warnings[x]})
            dict_with_score.update(bots[x])
            bots_with_scores.append(dict_with_score)
        return bots_with_scores
        #for x in species:
        #    for y in species[x]:
        #        if x in species_2.keys():
        #            species_2[x].append(dict(zip(y[0],y[1])))
        #        else:species_2[x]=[dict(zip(y[0],y[1]))]
        #for x in species_2:
        #    species_curr={0:{},1:{},2:{},3:{}}
        #    for y in species_2[x]:
        #        if y["score"] in species_curr[y["warnings"]]:
        #            species_curr[y["warnings"]][y["score"]].append(y)
        #        else:
        #            species_curr[y["warnings"]][y["score"]]=[y]
        #   x=x
        #    species_2_organised[x]=[species_curr]
        #    for thing in species_curr:
        #        keys=sorted(species_curr[thing].keys())
        #        keys.reverse()
        #        species_2_organised[x].append(keys)
        #curr_combo=[]
        #for x in range(ammount_of_new_bots):
        #    for y in species_2_organised:
        #        score_things=species_2_organised[y].copy()
        #        score_copy=score_things.copy()
        #        for a in score_things[0]:
        #            if len(score_things[0][a])<2:
        #                a=a
        #            else:
        #                if curr_combo==[]:
        #                    combos[score_copy[0][a]]





    

#starting_time=time.time()
#print(f"started at {time.time()-starting_time} seconds")

#bot=NEAT(3,2)

#print(f"initialised starting bot at {time.time()-starting_time} seconds")

#bots=bot.start()

#print(f"Got all starting bots at at {time.time()-starting_time} seconds")

#print(bot.get_output({1:0.2,2:0.8,3:-0.6},bots.pop(5)))
##scores=[]
#warnings=[]
#for x in range(len(bots)):
    #scores.append(random.randint(0,100))
    #warnings.append(0)

#print(f"Got all random scores for bots to test the sorting at {time.time()-starting_time} seconds")


#bots_with_scores=bot.get_bots_with_score(bots,scores,warnings)


#species=bot.sort_bots(bots_with_scores,scores,True)

#print(f"Finished sorting bots at {time.time()-starting_time} seconds")

    #species[tuple(x.keys())]=random.randint(0,1000)
#new_bots=bot.get_offspring([bots_with_scores[0].copy(),bots_with_scores[4].copy()],True,998)[0]

#new_bots=bot.breed_species(1000,species,bots_with_scores)
#print(f"Got offspring of bots at {time.time()-starting_time} seconds")
print("Thank you for using my NEAT AI library")
#x=0