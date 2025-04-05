import numpy.random as random
#import os
#import sys
#sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

import pokemon_lists



def GeneratePokemon():
    """Generate a pokemon with a 
    -powerlevel (regular, convergent evo, starter, god, fossil, legendary, pseudo legendary, mythical)
    -0 to 2 evolutions (plus split evo chance)
    -2 types (selected from 20)
    -X factor (None, Mega Evo, Additional form, signature move, signature ability, new mechanic, corrupted form)
    """
    #evolutions = 0
    #typing = ["", ""]
    #x_factor = ""

    power = PowerLevel()

    if power == "regular":
        evolutions = RegularEvos()
        typing = RegularTypes()
        x_factor = RegularX()
        RevealRegularPokemon(power, evolutions, typing, x_factor)
    elif power == "convergent evolution":
        generation = Generation()
        pokemon = SelectPokemon(generation)
        typing = RegularTypes()
        RevealConvergentPokemon(power, generation, pokemon, typing)
    elif power == "fossil":
        evolutions = FossilEvos()
        foss_type = GetType()
        x_factor = RegularX()
        RevealFossilPokemon(power, evolutions, foss_type, x_factor)
    elif power == "legendary":
        evolutions = LegendEvos()
        typing = RegularTypes()
        x_factor = LegendX()
        RevealLegendPokemon(power, evolutions, typing, x_factor)
    elif power == "starter":
        starter_type = StarterTypes()
        second_type = StarterSecondTypes()
        RevealStarter(power, starter_type, second_type)
    elif power == "pseudo legendary":
        evolutions = PseduoEvos()
        typing = RegularTypes()
        x_factor = RegularX()
        RevealPseudoPokemon(power, evolutions, typing, x_factor)
    else:
        print(f"You are a {power} pokemon! That's not implemented yet. Womp Womp.")
        

    return

    
    

def PowerLevel():
    return random.choice(pokemon_lists.power_levels, p=[0.5, 0.2, 0.05, 0.001, 0.059, 0.05, 0.06, 0.08])
    

def RegularEvos():
    return random.choice(pokemon_lists.reg_evolutions, p=[0.2, 0.4, 0.3, 0.1])


def GetType():
    return random.choice(pokemon_lists.reg_types)


def RegularTypes():
    type_1 = GetType()
    type_2 = GetType()
    return [type_1, type_2]


def RegularX():
    coin_flip = random.choice([0, 1])
    if coin_flip == 0:
        return "None"
    else:
        return random.choice(pokemon_lists.regular_x_factor)
    

def Generation():
    a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    return random.choice(a)

def SelectPokemon(generation):
    if generation == 1:
        return pokemon_lists.ReturnGen1()
    elif generation == 2:
        return pokemon_lists.ReturnGen2()
    elif generation == 3:
        return pokemon_lists.ReturnGen3()
    elif generation == 4:
        return pokemon_lists.ReturnGen4()
    elif generation == 5:
        return pokemon_lists.ReturnGen5()
    elif generation == 6:
        return pokemon_lists.ReturnGen6()
    elif generation == 7:
        return pokemon_lists.ReturnGen7()
    elif generation == 8:
        return pokemon_lists.ReturnGen8()
    else:
        return pokemon_lists.ReturnGen9()
     
    

def FossilEvos():
    return random.choice(pokemon_lists.fos_evolutions, p=[0.45, 0.45, 0.1])


def LegendEvos():
    return random.choice(pokemon_lists.reg_evolutions, p=[0.91, 0.03, 0.03, 0.03])


def LegendX():
    return random.choice(pokemon_lists.regular_x_factor)


def StarterTypes():
    return random.choice(pokemon_lists.starter_types)

def StarterSecondTypes():
    return random.choice(pokemon_lists.sec_types)

def PseduoEvos():
    return random.choice(pokemon_lists.reg_evolutions, p=[0.01, 0.01, 0.96, 0.02])


def RevealRegularPokemon(power, evolutions, typing, x_factor):
    stage = ""
    is_split = False

    if evolutions == 0:
        stage = "base"
    elif evolutions == 1:
        stage = "two-stage"
    elif evolutions == 2:
        stage = "full three-stage"
    else:
        stage = "split evolution"
        is_split = True

    type_1 = typing[0]
    type_2 = typing[1]
    womp_womp = False
    pure_typing = False
    dual_typing = False

    if (type_1 == "None") or (type_2 == "None"):
        if type_1 == type_2:
            womp_womp = True
        else:
            pure_typing = True
    else:
        if type_1 == type_2:
            pure_typing = True
        else:
            dual_typing = True

    print(f"You got a {power} pokemon!")
    if is_split == True:
        print(f"Wow, your pokemon has a split evolution line! That means it can evolve into different pokemon depending on certain things such as gender, evolution stone exposure, or even time of day. How Rare!")
    else:
        print(f"Your pokemon can evolve {evolutions} time(s), making it a {stage} pokemon. Nice!")
    print(f"Your first type is {type_1}, and your second type is {type_2}.")
    if dual_typing == True:
        print(f"This makes you a {type_1}/{type_2} dual-type pokemon. Cool!")
    elif pure_typing == True:
        if type_1 == "None":
            type_1 = type_2
        print(f"This makes you a pure {type_1} type pokemon!")
    else:
        print("...Huh. You have no type. Weird.") 
        print("There is only a %0.25 chance of that, here!")
        print("I guess you're a pokemon with some serious involvement in the plot of the game.")
        print("Go forth, you unlikely creature, you!")
    if x_factor == "None":
        print("You didn't get an X-factor, but that's okay!")
    else:
        a = "a"
        if x_factor == "additional form":
            a = "an"
        print(f"Congratulations, you got an X-factor! You have {a} {x_factor}! Exciting!")

    #pokemon = input("What will you call your new pokemon?")
    print("Welcome to the world!")
    
    return


def RevealConvergentPokemon(power, generation, pokemon, typing):
    type_1 = typing[0]
    type_2 = typing[1]
    womp_womp = False
    pure_typing = False
    dual_typing = False

    if (type_1 == "None") or (type_2 == "None"):
        if type_1 == type_2:
            womp_womp = True
        else:
            pure_typing = True
    else:
        if type_1 == type_2:
            pure_typing = True
        else:
            dual_typing = True

    print(f"You got a {power} pokemon!")
    print(f"It looks like you're going to be a generation {generation} pokemon, nice!")
    print(f"Out of all the generation {generation} pokemon, it looks like you convergently evolved with...")
    print(f"{pokemon}!")
    print(f"(Remember, if your pokemon is part of an evolution line, that means you get all of them!)")
    print(f"Now, let's see what your typing will be...")
    print(f"Your first type is {type_1}, and your second type is {type_2}.")
    if dual_typing == True:
        print(f"This makes you a {type_1}/{type_2} dual-type pokemon. Cool!")
    elif pure_typing == True:
        if type_1 == "None":
            type_1 = type_2
        print(f"This makes you a pure {type_1} type pokemon!")
    else:
        print("...Huh. You have no type. Weird.") 
        print("There is only a %0.25 chance of that, here!")
        print("I guess you're a pokemon with some serious involvement in the plot of the game.")
        print("Go forth, you unlikely creature, you!")
    print("Welcome to the world!")
    return


def RevealFossilPokemon(power, evolutions, foss_type, x_factor):
    is_split = False

    pure_typing = False
    if (foss_type == "Rock") or (foss_type == "None"):
        pure_typing = True

    stage = ""
    if evolutions == 0:
        stage = "base"
    elif evolutions == 1:
        stage = "two-stage"
    else:
        stage = "split evolution"
        is_split = True
    
    print(f"You got a {power} pokemon!")
    if is_split == True:
        print(f"Wow, your pokemon has a split evolution line! That means it can evolve into different pokemon depending on certain things such as gender, evolution stone exposure, or even time of day. How Rare!")
    else:
        print(f"Your pokemon can evolve {evolutions} time(s), making it a {stage} pokemon. Nice!")
    print(f"Since you are a fossil, you automatically have a rock typing. Your other type will be...")

    if pure_typing:
        print(f"{foss_type}! That makes you a pure rock type!")
    else:
        print(f"{foss_type}!")
        print(f"This makes you a Rock/{foss_type} dual-type pokemon. Wow!")
    
    if x_factor == "None":
        print("Finally, you didn't get an X-factor, but that's okay!")
    else:
        a = "a"
        if x_factor == "additional form":
            a = "an"
        print(f"Congratulations, you got an X-factor! You have {a} {x_factor}! Exciting!")
    print("Welcome to the world!")
    return


def RevealLegendPokemon(power, evolutions, typing, x_factor):
    stage = ""
    is_split = False
    is_base = False

    if evolutions == 0:
        stage = "base"
        is_base = True
    elif evolutions == 1:
        stage = "two-stage"
    elif evolutions == 2:
        stage = "full three-stage"
    else:
        stage = "split evolution"
        is_split = True

    type_1 = typing[0]
    type_2 = typing[1]
    womp_womp = False
    pure_typing = False
    dual_typing = False

    if (type_1 == "None") or (type_2 == "None"):
        if type_1 == type_2:
            womp_womp = True
        else:
            pure_typing = True
    else:
        if type_1 == type_2:
            pure_typing = True
        else:
            dual_typing = True

    print(f"You got a {power} pokemon! That's awesome!")
    print(f"Usually legendary pokemon don't evolve...")
    if is_split == True:
        print(f"But wow, it looks like your legendary has a split evolution line! That means it can evolve into different pokemon depending on certain things such as gender, evolution stone exposure, or even time of day. How Rare!")
    elif is_base == True:
        print("...And it looks like you don't, either.")
    else:
        print(f"But it looks like your legendary can evolve {evolutions} time(s), making it a {stage} pokemon. Incredible!")
    print(f"Your first type is {type_1}, and your second type is {type_2}.")
    if dual_typing == True:
        print(f"This makes you a {type_1}/{type_2} dual-type pokemon. Cool!")
    elif pure_typing == True:
        if type_1 == "None":
            type_1 = type_2
        print(f"This makes you a pure {type_1} type pokemon!")
    else:
        print("...Huh. You have no type. Weird.") 
        print("There is only a %0.25 chance of that, here!")
        print("I guess you're a pokemon with some serious involvement in the plot of the game. Especially as a legendary, holy cow!")
        print("Go forth, you unlikely creature, you!")

    a = "a"
    if x_factor == "additional form":
        a = "an"
    print(f"Here's the cool part: all legendaries have an X Factor! As for you, you have {a} {x_factor}! Exciting!")

    #pokemon = input("What will you call your new pokemon?")
    print("Welcome to the world!")
    return


def RevealStarter(power, starter_type, second_type):
    print(f"You got a {power} pokemon! That's awesome!")
    print("There are only ever 3 starter pokemon per region, so you're super rare! Wow!")
    print("Starter pokemon are always either Fire, Grass, or Water type, and they always evolve 3 times!")
    print(f"It looks like you are the {starter_type} starter pokemon! Neat!")
    print("Often, starter pokemon gain a secondary typing upon leveling up. Let's see if you have one...")
    
    if (second_type == starter_type) or (second_type == "None"):
        print("Well, it doesn't look like you have a second typing, but that's okay! It means you're just like the OGs!")
    else:
        print(f"It looks like you are also going to be a {second_type} type pokemon! That makes you a {starter_type}/{second_type}. That's so cool!")

    print("Welcome to the world!")
    return


def RevealPseudoPokemon(power, evolutions, typing, x_factor):
    stage = ""
    is_split = False
    is_base = False

    if evolutions == 0:
        stage = "base"
        is_base = True
    elif evolutions == 1:
        stage = "two-stage"
    elif evolutions == 2:
        stage = "full three-stage"
    else:
        stage = "split evolution"
        is_split = True

    type_1 = typing[0]
    type_2 = typing[1]
    womp_womp = False
    pure_typing = False
    dual_typing = False

    if (type_1 == "None") or (type_2 == "None"):
        if type_1 == type_2:
            womp_womp = True
        else:
            pure_typing = True
    else:
        if type_1 == type_2:
            pure_typing = True
        else:
            dual_typing = True

    print(f"You got a {power} pokemon! Just like Salamance, cool!")
    print(f"All pseudo-legendaries so far have 3-stage evolution lines, but there's a small chance of something different...")
    if is_split == True:
        print(f"Wow, your pokemon has a split evolution line! That means it can evolve into different pokemon depending on certain things such as gender, evolution stone exposure, or even time of day. How Rare!")
    elif stage != "full three-stage":
        print(f"Your pokemon can evolve {evolutions} time(s), making it a {stage} pokemon. How Rare!")
    else:
        print("It looks like you also have 3 stages. Classic!")

    print(f"Your first type is {type_1}, and your second type is {type_2}.")
    if dual_typing == True:
        print(f"This makes you a {type_1}/{type_2} dual-type pokemon. Cool!")
    elif pure_typing == True:
        if type_1 == "None":
            type_1 = type_2
        print(f"This makes you a pure {type_1} type pokemon!")
    else:
        print("...Huh. You have no type. Weird.") 
        print("There is only a %0.25 chance of that, here!")
        print("I guess you're a pokemon with some serious involvement in the plot of the game.")
        print("Go forth, you unlikely creature, you!")
    
    if x_factor == "None":
        print("You didn't get an X-factor, but that's okay!")
    else:
        a = "a"
        if x_factor == "additional form":
            a = "an"
        print(f"Congratulations, you got an X-factor! You have {a} {x_factor}! Exciting!")

    print("Welcome to the world!")
    return


GeneratePokemon()