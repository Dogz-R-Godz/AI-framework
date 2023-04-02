for bot_num in range(bots):
                if bot_num%bots_percentage==0:
                    print(f"{math.floor(bot_num/bots_percentage)*10}% done")
                curr_bot={}
                for input_thing in range(self.inputs):
                    output_used=random.randint(1,self.outputs)
                    if (input_thing,self.inputs+output_used+1) not in self.identifiers.values():
                        self.identifiers[len(self.identifiers)+1]=(input_thing,self.inputs+output_used+1)
                        if input_thing+1 in self.connections.keys():
                            self.connections[input_thing+1].append((len(self.identifiers),(input_thing,self.inputs+output_used+1)))
                        else:
                            self.connections[input_thing+1]=[(len(self.identifiers),(input_thing,self.inputs+output_used+1))]
                        identifier=len(self.identifiers)
                    else:
                        identifier=[k for k,v in self.identifiers.items() if v==(input_thing,self.inputs+output_used+1)]
                        identifier=int(identifier[0])
                    curr_bot[identifier]=round(random.randint(-200,200)/100,3)
                    if random.randint(0,10)==0:
                        output_2=random.randint(1,self.outputs)
                        while output_2==output_used:
                            output_2=random.randint(1,self.outputs)
                        if (input_thing,self.inputs+output_2+1) not in self.identifiers.values():
                            self.identifiers[len(self.identifiers)+1]=(input_thing,self.inputs+output_2+1)
                            if input_thing+1 in self.connections.keys():
                                self.connections[input_thing+1].append((len(self.identifiers),(input_thing,self.inputs+output_2+1)))
                            else:
                                self.connections[input_thing+1]=[(len(self.identifiers),(input_thing,self.inputs+output_2+1))]
                            identifier=len(self.identifiers)
                        else:
                            identifier=[k for k,v in self.identifiers.items() if v==(input_thing,self.inputs+output_2+1)]
                            identifier=int(identifier[0])
                        curr_bot[identifier]=round(random.randint(-200,200)/100,3)
                curr_bot["identifier"]=self.identifiers
                all_bots.append(curr_bot)