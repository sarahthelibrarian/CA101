#import necessary libraries

import csv, re, random, pandas as pd

#reading our dataframe from our clean data so we can do our game!
df = pd.read_csv("cleanrankings_data2020.csv", delimiter = ",")

#INSTRUCTIONS FOR OUR GAME
print("Congrats! You've been drafted to the Boston Massacre, the A-team for Boston Roller Derby ranked 36 in the world. It's going to be a great season!")
print("When you're ready, type Yes or yes!")
print("When you need a break, type Stop or stop!")
ready = input("Are you ready to play? ")

#while loop
while ready == 'Yes' or ready == 'yes':
    #get random ranking to generate other opponent
    opp_rank = random.randint(1, 351)
    #parse that data for information on our other team
    opp_team = df.loc[df['rank'] == opp_rank]
    opp_team_name = opp_team['league']
    opp_weight = float(opp_team['weight'])
    opp_gpa = opp_team['gpa']
    opp_gpa = opp_gpa.replace(',', '')
    opp_gpa = float(opp_gpa)
    
    #separate out our boston data... I know I could do this all at once later but it hurts my brain to do it like that, even though it makes more code this way
    #i think it's easier to read
    bos_gpa = float(boston_data['gpa'])
    bos_weight = float(boston_data['weight'])
    
    #generate some random scores!! woooooo
    bos_score = float(random.randint(5, 500))
    opp_score = float(random.randint(5, 500))
    
    #calculate the actual game points using the complicated WFTDA equation
    bos_gp = (bos_score/(bos_score + opp_score)) * 300 * float(opp_weight)
    opp_gp = (opp_score/(bos_score + opp_score)) * 300 * float(opp_weight)
    
    #give our player some information and separate it out just for usability
    print("You are playing " + opp_team_name)
    print("They are ranked: " + str(opp_rank))
    print("Are you done warming up?")
    lets_go = input("Type Yes if you're ready to play! ")
    
    if lets_go == 'Yes' or lets_go == 'yes':
        #scenario 1, you won!
        if bos_score > opp_score:
            #give user information
            print("Boston won! And you got awarded MVP! The final score was " + str(bos_score) + " vs " + str(opp_score))
            print("The total game points for you are: " + str(bos_gp))
            print('The total game points for ' + opp_team_name + " are: " + str(opp_gp))
            
            #gpa determines rankings in the WFTDA, so calculate how this game affected yours
            #you want this to be POSITIVE
            gpa_change = bos_gp - bos_gpa
            #scenario 1 part a
            if gpa_change > 0:
                #best thing that could happen! 
                print('GPA change was: ' + str(gpa_change))
                print("Your GPA was positively affected by this game, meaning you will likely go up in rankings! Yay! You killed it!")
                #scenario 1 part b
            elif gpa_change < 0:
                #this isn't ideal, even though you 'won' your rankings will be hurt
                print('GPA change was: ' + str(gpa_change))
                print("Unfortunately, even though you won, your GPA was negatively affected by this game. You could end up going down in the rankings. There will be other games, though!")
        
        #scenario 2, you lost
        elif opp_score > bos_score:
            print("Oh no, you lost. You played great, though! The final score was " + str(opp_score) + " vs " + str(bos_score))
            print("The total game points for you are: " + str(bos_gp))
            print('The total game points for ' + opp_team_name + " are: " + str(opp_gp))
            #gpa determines rankings in the WFTDA, so calculate how this game affected yours
            #you want this to be POSITIVE
            gpa_change = bos_gp - bos_gpa
            
            #scenario 2 part a
            if gpa_change > 0:
                #if you lose, this is still good!!
                print('GPA change was: ' + str(gpa_change))
                print("Even though you lost, your GPA was positively affected by this game, meaning you will could go up in rankings! Yay! You killed it!")
            #scenario 2 part b
            elif gpa_change < 0:
                #your rankings will be hurt
                print('GPA change was: ' + str(gpa_change))
                print("Unfortunately, your GPA was negatively affected by this game. You could end up going down in the rankings. There will be other games, though!")
    #decide if we want to come out of our loop  
    ready = input("Are you ready to play? ")

#close out the game 
if ready == "Stop" or ready == "stop":
    print("Thanks for playing! Congrats on your first season with the Boston Massacre.")

