import time
import os
import msvcrt
import random
import json
networks = [
    {"network1": "IQ50"},
    {"network2": "IQ100"},
    {"network3": "IQ120"},
    {"network4": "IQ145"},
    {"network5": "IQ155"},
    {"network6": "IQ160"},
]

print("=== NEURAL NETWORK LOAD ===")
for i, net in enumerate(networks, 1):
    network_id = list(net.keys())[0]
    iq_name = list(net.values())[0]
    print(f"{i}. {network_id} - {iq_name}")
print("=============================")

def export_network_brain(filename, netout, neural, bias, file):
    brain_data = [
        {"networkID": netout},
        {"neural weight": neural},
        {"bias number": bias},
        {"neural file": file},
    ]
    
    with open(filename, "w") as f:
        json.dump(brain_data, f, indent=4)
        
    print(f"\n[💾]System export saved!")

netin = input(f"Choose a network to run:\n>>> ")

if netin == "network1" or netin == "1":
    netout = "iq#1"
elif netin == "network2" or netin == "2":
    netout = "iq#2"
elif netin == "network3" or netin == "3":
    netout = "iq#3"
elif netin == "network4" or netin == "4":
    netout = "iq#4"
elif netin == "network5" or netin == "5":
    netout = "iq#5"
elif netin == "network6" or netin == "6":
    netout = "iq#6"
else:
    print("Invalid network, choosing highest network...")
    netout = "iq#6"
print(f"Choosing network {netout}...")

while True:
    num = input("Input a number between 1-1000\n>>> ")
    if num == "":
        num = random.randint(1, 1000)
    else:
        num = int(num)
        if num < 0 or num == 0:
            continue
        else:
            break
    
load_choice = input("Do you want to (1)load or (2)delete a saved network? (1 or 2, Press Enter to skip)\n>>> ").strip().lower()

if load_choice == '1':
    filename = input("Enter the file name to load (e.g., model3_trained):\n>>> ").strip().lower().replace(" ", "_")
    if not filename.endswith(".json"):
        filename += ".json"
        
    if os.path.exists(f"neural/{filename}"):
        try:
            with open(f"neural/{filename}", "r") as f:
                saved_data = json.load(f)
            
            netout = saved_data[0]["networkID"]
            neural = saved_data[1]["neural weight"]
            bias = saved_data[2]["bias number"]
            file = saved_data[3]["neural file"]
            with open(f"neural/{file}.txt", "r") as f:
                net = f.read()
            print(f"\n[📂] Successfully loaded Model#: {netout}, Neural weight: {neural}!")
        except Exception as e:
            print(f"\n[!] Fatal error occured: {e}")
            print(f"\n[📂] Scavanged: Model# {netout}, Neural Weight {neural}!")
            if not file:
                file = random.randint(1, 99999)
                with open(f"neural/{file}.txt", "w") as f:
                    f.write("")
            if not neural:
                neural = 20
            if not bias:
                bias = 0
            if not netout:
                netout = "iq#1"
    else:
        print("\n[!] File not found. Initializing raw untrained network defaults...")
        neural = 20
elif load_choice == "2":
    filenamedel = input("Enter the file name to delete (e.g., model3_trained):\n>>>").strip().lower().replace(" ", "_")
    if not filenamedel.endswith(".json"):
        filenamedel += ".json"
    if os.path.exists(f"neural/{filenamedel}"):
        os.remove(f"neural/{filenamedel}")
        print(f"\n[🗑] Successfully deleted {filenamedel}!")
    else:
        print(f"\n[!] File not found. Initializing training program...")
    neural = 20
    bias = 0
    if netout == "iq#6":
        file = random.randint(1, 99999)
        net = "A"
        with open(f"neural/{file}.txt", "w") as f:
            f.write(net)
        with open(f"neural/log_{file}.txt", "w") as f:
            f.write(f"{net}:{time.time()}:fail\n")
    else:
        net = ""
        file = ""
else:
    print("Declined load/delete network prompt.")
    neural = 20
    bias = 0
    if netout == "iq#6":
        file = random.randint(1, 99999)
        net = "A"
        with open(f"neural/{file}.txt", "w") as f:
            f.write(net)
        with open(f"neural/log_{file}.txt", "a") as f:
            f.write(f"{net}:{time.time()}:fail\n")
    else:
        net = ""
        file = ""
    
reward = 0
learning = False
guess = 0
timer = 0
old_neural = 0
minnum = num - random.randint(20, 30)
maxnum = num + random.randint(20, 30)
search_min = minnum
search_max = maxnum
est_centre = 0
tick = 0.2
notnum = []

while True:
    
    if learning and guess > maxnum:
        neural -= random.randint(1, 10)
    elif learning and guess < minnum:
        neural += random.randint(1, 10)
    elif learning and guess < maxnum and guess > minnum:
        guess = maxnum - random.randint(10, 30)
        
    
    #Network3
    if (netout == "iq#3") or (netout == "iq#6" and net == "C"):
        if guess in notnum:
            if guess < minnum:
                guess = neural + 20
            elif guess > maxnum:
                guess = neural - 20
            else:
                guess = neural + random.randint(30, 60)
        else:
            guess = neural + random.randint(5, 10)
            
    #Network2
    if (netout == "iq#2") or (netout == "iq#6" and net == "B"):
        if guess > minnum and guess < maxnum:
            guess = neural + random.randint(1, 5)
        else:
            guess = neural + random.randint(3, 9)
            
    elif (netout == "iq#1") or (netout == "iq#6" and net == "A"):
        #Network1
        guess = neural + random.randint(5, 10)
        
            
    #Network4
    if (netout == "iq#4") or (netout == "iq#6" and net == "D"):
        if random.randint(1, 5) == 1:
            old_neural = neural
        if random.randint(1, 5) == 1 and neural > old_neural:
            est_centre = (search_min + search_max) // 2
        if est_centre in notnum and neural > old_neural:
            est_centre += random.randint(1, 5)
        else:
            est_centre += random.randint(-50, 50)
            neural += random.randint(5, 10)
        guess = est_centre

    #Network5
    if (netout == "iq#5") or (netout == "iq#6" and net == "E"):
        minbias = bias - 20
        maxbias = bias + 20
        bias_list = list(range(minbias, maxbias + 1))
        num_list = list(range(search_min, search_max + 1))
        overlap = set(bias_list) & set(num_list)

        bias = random.randint(1, 1000)
        if random.randint(1, 5) == 1:
            old_neural = neural
        if random.randint(1, 2) == 1 and neural > old_neural:
            if overlap:
                guess = random.choice(list(overlap))
            else:
                for n in bias_list:
                    if n not in notnum:
                        notnum.append(n)
                guess = random.randint(search_min, search_max)
        else:
            neural += random.randint(5, 10)
            guess = neural + random.randint(5, 10)

    #Network6
    if netout == "iq#6":

        with open(f"neural/log_{file}.txt", "r") as f:
            content = f.readlines()
            countA = 0
            countB = 0
            countC = 0
            countD = 0
            countE = 0

            if os.path.exists(f"neural/log_{file}.txt"):
                if content:
                    last_line = content[-1]
                else:
                    last_line = ""
                last_parts = last_line.strip().split(":")
                last_strategy = last_line.strip().split(":")[0]
                old_time = last_line.strip().split(":")[1]
                new_time = time.time()
            for line in content:
                if "A" in line:
                    countA += 1
                elif "B" in line:
                    countB += 1
                elif "C" in line:
                    countC += 1
                elif "D" in line:
                    countD += 1
                elif "E" in line:
                    countE += 1

            if last_strategy == net:
                if (guess != num) and (guess < minnum or guess > maxnum) and (countA > 30):
                    net = "B"
                if (guess != num) and (guess < minnum or guess > maxnum) and (countB > 30):
                    net = "C"
                if (guess != num) and (guess < minnum or guess > maxnum) and (countC > 30):
                    net = "D"
                if (guess != num) and (guess < minnum or guess > maxnum) and (countD > 30):
                    net = "E"
                if (guess != num) and (guess < minnum or guess > maxnum) and (countE > 30):
                    total_runs = len(content)
                    strategy_success = {"A": 0, "B": 0, "C": 0, "D": 0, "E": 0}
                    for line in content:
                        parts = line.strip().split(":")

                        if len(parts) >= 3:
                            strategy_letter = parts[0]
                            result = parts[2]

                            if strategy_letter in strategy_success and result == "success":
                                strategy_success[strategy_letter] += 1
                                
                    best_strategy = max(strategy_success, key=strategy_success.get)
                    net = best_strategy
                        
        with open(f"neural/{file}.txt", "w") as f:
            f.write(f"{net}")
        guess_result = "success" if abs(num - guess) <= 20 else "fail"
        with open(f"neural/log_{file}.txt", "a") as f:
            f.write(f"{net}:{time.time()}:{guess_result}\n")

        
    #Motivation
    if guess > minnum and guess < maxnum and not timer > 1:
        timer += 1
        reward += 10
    #Punishment
    elif abs(num - guess) >= 10:
        reward -= 0.01
    #Win Condition
    if abs(num - guess) <= 10:
        reward += 50
        timer = 0
        print(f"Neural connections: {neural}, Bias factor: {bias}, Reward#: {reward}")
        print(f"Learning: {learning}, Current system: {net}, File#: {file}, Current guess: {guess}")
        print("Testing finished.")
        save = input("Give a name for new saved neural network (leave it blank to not save)\n>>> ").strip().lower().replace(" ", "_")
        if save == "":
            pass
        else:
            export_network_brain(f"neural/{save}.json", netout, neural, bias, file)
        break
    else:
        if netout == "iq#1" and random.randint(1, 5) == 1:
            notnum.append(guess)
        elif netout != "iq#2" and random.randint(1, 3) == 1:
            notnum.append(guess)
    if reward < 40:
        learning = True
    else:
        learning = False
        
    if msvcrt.kbhit():
        key = msvcrt.getch().decode('utf-8').lower()
        if key == 'p':
            print("Neural learning paused.")
            save = input("Give a name for new saved neural network (leave it blank to not save)\n>>> ").strip().lower().replace(" ", "_")
            if save == "":
                pass
            else:
                export_network_brain(f"neural/{save}.json", netout, neural, bias, file)

    print(f"Neural connections: {neural}, Bias factor: {bias}, Reward#: {reward}")
    print(f"Learning: {learning}, Current system: {net}, File#: {file}, Current guess: {guess}")
            
    time.sleep(tick)
    
