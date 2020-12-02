from tkinter import *
from PIL import ImageTk, Image
import random

root = Tk()
root.title('8-puzzel')
root.iconbitmap('numbers_img/N_symbol.ico')

#photos initialization 
number_1_photo = ImageTk.PhotoImage(Image.open('numbers_img/number-1.ico').resize((160,160)))
number_2_photo = ImageTk.PhotoImage(Image.open('numbers_img/number-2.ico').resize((160,160)))
number_3_photo = ImageTk.PhotoImage(Image.open('numbers_img/number-3.ico').resize((160,160)))
number_4_photo = ImageTk.PhotoImage(Image.open('numbers_img/number-4.ico').resize((160,160)))
number_5_photo = ImageTk.PhotoImage(Image.open('numbers_img/number-5.ico').resize((160,160)))
number_6_photo = ImageTk.PhotoImage(Image.open('numbers_img/number-6.ico').resize((160,160)))
number_7_photo = ImageTk.PhotoImage(Image.open('numbers_img/number-7.ico').resize((160,160)))
number_8_photo = ImageTk.PhotoImage(Image.open('numbers_img/number-8.ico').resize((160,160)))
snake_photo = ImageTk.PhotoImage(Image.open('numbers_img/snake.ico').resize((160,160)))
exit_photo = ImageTk.PhotoImage(Image.open('numbers_img/exit_photo.ico').resize((160,160)))
auto_photo = ImageTk.PhotoImage(Image.open('numbers_img/auto_photo.ico').resize((160,160)))
shuf_photo = ImageTk.PhotoImage(Image.open('numbers_img/shuf_photo.ico').resize((160,160)))
up_photo = ImageTk.PhotoImage(Image.open('numbers_img/up_photo.ico').resize((76,76)))
down_photo = ImageTk.PhotoImage(Image.open('numbers_img/down_photo.ico').resize((76,76)))
left_photo = ImageTk.PhotoImage(Image.open('numbers_img/left_photo.ico').resize((76,76)))
right_photo = ImageTk.PhotoImage(Image.open('numbers_img/right_photo.ico').resize((76,76)))
puzzle_photo = ImageTk.PhotoImage(Image.open('numbers_img/puzzle_photo.ico').resize((158,76)))
you_won_photo = ImageTk.PhotoImage(Image.open('numbers_img/You_won_photo.ico').resize((158,76)))

#List that keeps numbers position 
numbers_photos_list = [
    number_1_photo, 
    number_2_photo, 
    number_3_photo, 
    number_4_photo, 
    number_5_photo, 
    number_6_photo, 
    number_7_photo, 
    number_8_photo,
    snake_photo
    ]

numbers_photos_dictionary = {
    snake_photo: 0,
    number_1_photo: 1,
    number_2_photo: 2,
    number_3_photo: 3,
    number_4_photo: 4,
    number_5_photo: 5,
    number_6_photo: 6,
    number_7_photo: 7,
    number_8_photo: 8
}

random.shuffle(numbers_photos_list)

#This list is made to keep a 2 moves memory
snake_queue = [-1,-1]

counter = [0]

def start_game():
    snake_queue[0] = snake_queue[1]
    snake_queue[1] = numbers_photos_list.index(snake_photo)

    print(f'Round:{counter}')

    #frames initialization
    frame_0 = LabelFrame(root, text="")
    frame_1 = LabelFrame(root, text="")
    frame_3 = LabelFrame(root, text="")
    frame_4 = LabelFrame(root, text="")
    frame_2 = LabelFrame(root, text="")
    frame_5 = LabelFrame(root, text="")
    frame_6 = LabelFrame(root, text="")
    frame_7 = LabelFrame(root, text="")
    frame_8 = LabelFrame(root, text="")
    frame_9 = LabelFrame(root, text="")
    frame_10 = LabelFrame(root, text="")
    frame_11 = LabelFrame(root, text="")
    frame_12 = LabelFrame(root, text="")
    frame_13 = LabelFrame(root, text="")
    frame_14 = LabelFrame(root, text="")

    #frames layout
    frame_0.grid(row=0, column=0)
    frame_1.grid(row=0, column=1)
    frame_2.grid(row=0, column=2)
    frame_3.grid(row=1, column=0)
    frame_4.grid(row=1, column=1)
    frame_5.grid(row=1, column=2)
    frame_6.grid(row=2, column=0)
    frame_7.grid(row=2, column=1)
    frame_8.grid(row=2, column=2)
    frame_9.grid(row=4, column=0)
    frame_10.grid(row=4, column=1)
    frame_11.grid(row=4, column=2)
    frame_12.grid(row=3, column=0)
    frame_13.grid(row=3, column=1)
    frame_14.grid(row=3, column=2)

    def shuf_photos():
        random.shuffle(numbers_photos_list)
        check_if_solvable()
        start_game()
    
    def refresh_game():
        counter[0] = counter[0]+1  
        start_game()

    position_0, position_1, position_2, position_3, position_4, position_5, position_6, position_7, position_8 = numbers_photos_list

    def check_if_solvable(): #a random shuffle of numbers doesnt always make a solvable 8-puzzle game(i learned this with the hard way :) info https://www.geeksforgeeks.org/check-instance-8-puzzle-solvable/
        inversion_sum = 0
        counter=0
        #above i must initialize a new list with the numbers in the 8-puzzel ascending order
        ordenrd_list = [numbers_photos_list[0],numbers_photos_list[1],numbers_photos_list[2],numbers_photos_list[5],numbers_photos_list[8],numbers_photos_list[7],numbers_photos_list[6],numbers_photos_list[3],numbers_photos_list[4]]
        for i in range(len(ordenrd_list)):
            for j in range(8-counter):
                a = numbers_photos_dictionary.get(ordenrd_list[i])
                b = numbers_photos_dictionary.get(ordenrd_list[i+j+1])
                if a > b and ordenrd_list[i+j+1]!=snake_photo:
                    inversion_sum += 1
            counter +=1
        if inversion_sum%2==1:
            shuf_photos()
        else:
            pass

    if snake_queue[0] == -1:
        check_if_solvable()

    myLabel_0 = Label(frame_0, image=position_0).pack()
    myLabel_1 = Label(frame_1, image=position_1).pack()
    myLabel_2 = Label(frame_2, image=position_2).pack()
    myLabel_3 = Label(frame_3, image=position_3).pack()
    myLabel_4 = Label(frame_4, image=position_4).pack()
    myLabel_5 = Label(frame_5, image=position_5).pack()
    myLabel_6 = Label(frame_6, image=position_6).pack()
    myLabel_7 = Label(frame_7, image=position_7).pack()
    myLabel_8 = Label(frame_8, image=position_8).pack()

    def distance_from_original_place(photo_name): #manhattan distance
        if numbers_photos_dictionary.get(photo_name)==1:
            if numbers_photos_list.index(photo_name) == 0:
                return 0  
            elif numbers_photos_list.index(photo_name) == 1 or numbers_photos_list.index(photo_name) == 3:
                return 1
            elif numbers_photos_list.index(photo_name) == 2 or numbers_photos_list.index(photo_name) == 4 or numbers_photos_list.index(photo_name) == 6:
                return 2
            elif numbers_photos_list.index(photo_name) == 5 or numbers_photos_list.index(photo_name) == 7:
                return 3
            else:
                return 4
        elif numbers_photos_dictionary.get(photo_name)==2:
            if numbers_photos_list.index(photo_name) == 1:
                return 0
            elif numbers_photos_list.index(photo_name) == 0 or numbers_photos_list.index(photo_name) == 2 or numbers_photos_list.index(photo_name) == 4:
                return 1
            elif numbers_photos_list.index(photo_name) == 3 or numbers_photos_list.index(photo_name) == 5 or numbers_photos_list.index(photo_name) == 7:
                return 2
            else:
                return 3
        elif numbers_photos_dictionary.get(photo_name)==3:
            if numbers_photos_list.index(photo_name) == 2:
                return 0
            elif numbers_photos_list.index(photo_name) == 1 or numbers_photos_list.index(photo_name) == 5:
                return 1
            elif numbers_photos_list.index(photo_name) == 0 or numbers_photos_list.index(photo_name) == 4 or numbers_photos_list.index(photo_name) == 8:
                return 2
            elif numbers_photos_list.index(photo_name) == 3 or numbers_photos_list.index(photo_name) == 7:
                return 3
            else:
                return 4
        elif numbers_photos_dictionary.get(photo_name)==4:
            if numbers_photos_list.index(photo_name) == 5:
                return 0
            elif numbers_photos_list.index(photo_name) == 2 or numbers_photos_list.index(photo_name) == 4 or numbers_photos_list.index(photo_name) == 8:
                return 1
            elif numbers_photos_list.index(photo_name) == 1 or numbers_photos_list.index(photo_name) == 3 or numbers_photos_list.index(photo_name) == 7:
                return 2
            else:
                return 3
        elif numbers_photos_dictionary.get(photo_name)==5:
            if numbers_photos_list.index(photo_name) == 8:
                return 0
            elif numbers_photos_list.index(photo_name) == 5 or numbers_photos_list.index(photo_name) == 7:
                return 1
            elif numbers_photos_list.index(photo_name) == 2 or numbers_photos_list.index(photo_name) == 4 or numbers_photos_list.index(photo_name) == 6:
                return 2
            elif numbers_photos_list.index(photo_name) == 1 or numbers_photos_list.index(photo_name) == 3:
                return 3
            else:
                return 4
        elif numbers_photos_dictionary.get(photo_name)==6:
            if numbers_photos_list.index(photo_name) == 7:
                return 0
            elif numbers_photos_list.index(photo_name) == 4 or numbers_photos_list.index(photo_name) == 6 or numbers_photos_list.index(photo_name) == 8:
                return 1
            elif numbers_photos_list.index(photo_name) == 1 or numbers_photos_list.index(photo_name) == 3 or numbers_photos_list.index(photo_name) == 5:
                return 2
            else:
                return 3
        elif numbers_photos_dictionary.get(photo_name)==7:
            if numbers_photos_list.index(photo_name) == 6:
                return 0
            elif numbers_photos_list.index(photo_name) == 3 or numbers_photos_list.index(photo_name) == 7:
                return 1
            elif numbers_photos_list.index(photo_name) == 0 or numbers_photos_list.index(photo_name) == 4 or numbers_photos_list.index(photo_name) == 8:
                return 2
            elif numbers_photos_list.index(photo_name) == 1 or numbers_photos_list.index(photo_name) == 5:
                return 3
            else:
                return 4
        elif numbers_photos_dictionary.get(photo_name)==8:
            if numbers_photos_list.index(photo_name) == 3:
                return 0
            elif numbers_photos_list.index(photo_name) == 0 or numbers_photos_list.index(photo_name) == 4 or numbers_photos_list.index(photo_name) == 6:
                return 1
            elif numbers_photos_list.index(photo_name) == 1 or numbers_photos_list.index(photo_name) == 5 or numbers_photos_list.index(photo_name) == 7:
                return 2
            else:
                return 3
        else:
            return 0
            
    def heuristic():
        heuristic_sum_list = []
        heuristic_sum = 0
        for i in numbers_photos_list:
            heuristic_sum += distance_from_original_place(i)
        heuristic_sum_list += [heuristic_sum]
        return heuristic_sum_list[0]

    def next_step_heuristic(next_position):
        position_snake = numbers_photos_list.index(snake_photo)
        position_future = numbers_photos_list.index(next_position)
        numbers_photos_list[position_snake], numbers_photos_list[position_future] = numbers_photos_list[position_future], numbers_photos_list[position_snake]
        var_heuristic = heuristic()
        numbers_photos_list[position_snake], numbers_photos_list[position_future] = numbers_photos_list[position_future], numbers_photos_list[position_snake]
        return var_heuristic
    
    def change_position(nesxt_snake_position):
        position_snake = numbers_photos_list.index(snake_photo)
        position_snake_future = numbers_photos_list.index(nesxt_snake_position)
        numbers_photos_list[position_snake], numbers_photos_list[position_snake_future] = numbers_photos_list[position_snake_future], numbers_photos_list[position_snake]

    def find_min_heuristic(heuristic_val_list): #I takes a list of heuristic valeus and returns a list with the position numbers(at the heuristic values list) of the min heuristics 
        new_list = []
        val_list = heuristic_val_list
        min_val = min(val_list)
        for i in range(len(heuristic_val_list)):
            if heuristic_val_list[i] == min_val:
                new_list += [i]
        return new_list

    def number_of_tiles_in_correct_place(next_snake_pos):
        position_snake = numbers_photos_list.index(snake_photo)
        position_future = numbers_photos_list.index(next_snake_pos)
        numbers_photos_list[position_snake], numbers_photos_list[position_future] = numbers_photos_list[position_future], numbers_photos_list[position_snake]
        correct_tiles_sum = 0
        correct_tiles_list = [number_1_photo, number_2_photo, number_3_photo, number_8_photo, snake_photo, number_4_photo, number_7_photo, number_6_photo, number_5_photo]
        for i in range(len(numbers_photos_list)):
            if numbers_photos_list[i] == correct_tiles_list[i]:
                correct_tiles_sum +=1
        numbers_photos_list[position_snake], numbers_photos_list[position_future] = numbers_photos_list[position_future], numbers_photos_list[position_snake]
        return correct_tiles_sum 

    def auto():
        if snake_photo == position_0:
            val_1 = next_step_heuristic(position_1)
            dis_num_1 = number_of_tiles_in_correct_place(position_1)
            val_2 = next_step_heuristic(position_3)
            dis_num_2 = number_of_tiles_in_correct_place(position_3)
            if snake_queue[0]==1: #if snake in the previous move at this position i make the heuristic large to avoid a step back 
                val_1 = 50
                dis_num_1 = -1
            if snake_queue[0]==3:
                val_2 = 50
                dis_num_2 = -1
            print(f'Fidi deksia:Her {val_1}:Num {dis_num_1}, Fidi kato:Her {val_2}:Num {dis_num_2}')    
            if (val_1 > val_2) or (val_1 == val_2 and dis_num_2 > dis_num_1):
                change_position(position_3)
                refresh_game()
            else:
                change_position(position_1)
                refresh_game()

        elif snake_photo == position_1:
            val_1 = next_step_heuristic(position_0)
            dis_num_1 = number_of_tiles_in_correct_place(position_0)
            val_2 = next_step_heuristic(position_2)
            dis_num_2 = number_of_tiles_in_correct_place(position_2)
            val_3 = next_step_heuristic(position_4)
            dis_num_3 = number_of_tiles_in_correct_place(position_4)
            if snake_queue[0]==0:
                val_1 = 50
                dis_num_1 = -1
            if snake_queue[0]==2:
                val_2 = 50
                dis_num_2 = -1
            if snake_queue[0]==4:
                val_3 = 50
                dis_num_3 = -1
            min_heuristic_positions = find_min_heuristic([val_1,val_2,val_3])
            print(f'Fidi aristera:Her {val_1}:Num {dis_num_1}, Fidi deksia:Her {val_2}:Num {dis_num_2}, Fidi kato:Her {val_3}:Num {dis_num_3}')
            if (val_1>val_3 and val_2>val_3) or (val_1>val_3 and val_2==val_3 and dis_num_2<dis_num_3) or (val_1==val_3 and val_2>val_3 and dis_num_1<dis_num_3):
                change_position(position_4)
                refresh_game()
            elif (val_1>val_2 and val_3>val_2) or (val_1>val_2 and val_3==val_2 and dis_num_3<dis_num_2) or (val_1==val_2 and val_3>val_2 and dis_num_1<dis_num_2):
                change_position(position_2)
                refresh_game()
            elif (val_2>val_1 and val_3>val_1) or (val_2>val_1 and val_3==val_1 and dis_num_3<dis_num_1) or (val_2==val_1 and val_3>val_1 and dis_num_2<dis_num_1):
                change_position(position_0)
                refresh_game()
            else:
                position_number = int(random.choice(min_heuristic_positions)) # if two or more heuristics are equal(with equal dist_num) i randomize the choice of the path to avoid infinite loop 
                if position_number == 0:
                    change_position(position_0)
                    refresh_game()
                elif position_number == 1:
                    change_position(position_2)
                    refresh_game()
                else:
                    change_position(position_4)
                    refresh_game()

        elif snake_photo == position_2:
            val_1 = next_step_heuristic(position_1)
            dis_num_1 = number_of_tiles_in_correct_place(position_1)
            val_2 = next_step_heuristic(position_5)
            dis_num_2 = number_of_tiles_in_correct_place(position_5)
            if snake_queue[0]==1: 
                val_1 = 50
                dis_num_1 = -1
            if snake_queue[0]==5:
                val_2 = 50
                dis_num_2 = -1
            print(f'Fidi aristera:Her {val_1}:Num {dis_num_1}, Fidi kato:Her {val_2}:Num {dis_num_2}')    
            if (val_1 > val_2) or (val_1 == val_2 and dis_num_2 > dis_num_1):
                change_position(position_5)
                refresh_game()
            else:
                change_position(position_1)
                refresh_game()

        elif snake_photo == position_3:
            val_1 = next_step_heuristic(position_0)
            dis_num_1 = number_of_tiles_in_correct_place(position_0)
            val_2 = next_step_heuristic(position_4)
            dis_num_2 = number_of_tiles_in_correct_place(position_4)
            val_3 = next_step_heuristic(position_6)
            dis_num_3 = number_of_tiles_in_correct_place(position_6)
            if snake_queue[0]==0:
                val_1 = 50
                dis_num_1 = -1
            if snake_queue[0]==4:
                val_2 = 50
                dis_num_2 = -1
            if snake_queue[0]==6:
                val_3 = 50
                dis_num_3 = -1
            min_heuristic_positions = find_min_heuristic([val_1,val_2,val_3])
            print(f'Fidi pano:Her {val_1}:Num {dis_num_1}, Fidi deksia:Her {val_2}:Num {dis_num_2}, Fidi kato:Her {val_3}:Num {dis_num_3}')
            if (val_1>val_3 and val_2>val_3) or (val_1>val_3 and val_2==val_3 and dis_num_2<dis_num_3) or (val_1==val_3 and val_2>val_3 and dis_num_1<dis_num_3):
                change_position(position_6)
                refresh_game()
            elif (val_1>val_2 and val_3>val_2) or (val_1>val_2 and val_3==val_2 and dis_num_3<dis_num_2) or (val_1==val_2 and val_3>val_2 and dis_num_1<dis_num_2):
                change_position(position_4)
                refresh_game()
            elif (val_2>val_1 and val_3>val_1) or (val_2>val_1 and val_3==val_1 and dis_num_3<dis_num_1) or (val_2==val_1 and val_3>val_1 and dis_num_2<dis_num_1):
                change_position(position_0)
                refresh_game()
            else:
                position_number = int(random.choice(min_heuristic_positions)) 
                if position_number == 0:
                    change_position(position_0)
                    refresh_game()
                elif position_number == 1:
                    change_position(position_4)
                    refresh_game()
                else:
                    change_position(position_6)
                    refresh_game()
            
        #Im sorry for what you are going to see above
        elif snake_photo == position_4:
            val_1 = next_step_heuristic(position_1)
            dis_num_1 = number_of_tiles_in_correct_place(position_1)
            val_2 = next_step_heuristic(position_3)
            dis_num_2 = number_of_tiles_in_correct_place(position_3)
            val_3 = next_step_heuristic(position_5)
            dis_num_3 = number_of_tiles_in_correct_place(position_5)
            val_4 = next_step_heuristic(position_7)
            dis_num_4 = number_of_tiles_in_correct_place(position_7)
            if snake_queue[0]==1:
                val_1 = 50
                dis_num_1 = -1
            if snake_queue[0]==3:
                val_2 = 50
                dis_num_2 = -1
            if snake_queue[0]==5:
                val_3 = 50
                dis_num_3 = -1
            if snake_queue[0]==7:
                val_4 = 50
                dis_num_4 = -1
            min_heuristic_positions = find_min_heuristic([val_1,val_2,val_3,val_4])
            print(f'Fidi pano:Her {val_1}:Num {dis_num_1}, Fidi aristera:Her {val_2}:Num {dis_num_2}, Fidi deksia:Her {val_3}:Num {dis_num_3}, Fidi kato:Her {val_4}:Num {dis_num_4}')
            if (val_1 > val_4 and val_2>val_4 and val_3 > val_4) or (val_1>val_4 and val_2>val_4 and val_3==val_4 and dis_num_3<dis_num_4) or (val_2>val_4 and val_3>val_4 and val_1==val_4 and dis_num_1<dis_num_4) or (val_1>val_4 and val_2==val_4 and val_3==val_4 and dis_num_2<dis_num_4 and dis_num_3<dis_num_4) or (val_2>val_4 and val_1==val_4 and val_3==val_4 and dis_num_1<dis_num_4 and dis_num_3<dis_num_4) or (val_3>val_4 and val_2==val_4 and val_1==val_4 and dis_num_2<dis_num_4 and dis_num_1<dis_num_4) or (val_1==val_4 and val_2==val_4 and val_3==val_4 and dis_num_1<dis_num_4 and dis_num_2<dis_num_4 and dis_num_3<dis_num_4):
                change_position(position_7)
                refresh_game()
            elif (val_1 > val_3 and val_2>val_3 and val_4 > val_3) or (val_1>val_3 and val_2>val_3 and val_3==val_4 and dis_num_4<dis_num_3) or (val_2>val_3 and val_4>val_3 and val_1==val_3 and dis_num_1<dis_num_3) or (val_1>val_3 and val_2==val_4 and val_3==val_4 and dis_num_2<dis_num_3 and dis_num_4<dis_num_3) or (val_2>val_3 and val_1==val_3 and val_4==val_3 and dis_num_1<dis_num_3 and dis_num_4<dis_num_3) or (val_4>val_3 and val_2==val_3 and val_1==val_3 and dis_num_2<dis_num_3 and dis_num_1<dis_num_3) or (val_1==val_3 and val_2==val_3 and val_4==val_3 and dis_num_1<dis_num_3 and dis_num_2<dis_num_3 and dis_num_4<dis_num_3):
                change_position(position_5)
                refresh_game()
            elif (val_1 > val_2 and val_4>val_2 and val_3 > val_2) or (val_1>val_2 and val_4>val_2 and val_3==val_2 and dis_num_3<dis_num_2) or (val_4>val_2 and val_3>val_2 and val_1==val_2 and dis_num_1<dis_num_2) or (val_1>val_2 and val_4==val_2 and val_3==val_2 and dis_num_4<dis_num_2 and dis_num_3<dis_num_2) or (val_4>val_2 and val_1==val_2 and val_3==val_2 and dis_num_1<dis_num_2 and dis_num_3<dis_num_2) or (val_3>val_2 and val_4==val_2 and val_1==val_2 and dis_num_4<dis_num_2 and dis_num_1<dis_num_2) or (val_1==val_2 and val_4==val_2 and val_3==val_2 and dis_num_1<dis_num_2 and dis_num_4<dis_num_2 and dis_num_3<dis_num_2):
                change_position(position_3)
                refresh_game()
            elif (val_4 > val_1 and val_2>val_1 and val_3 > val_1) or (val_4>val_1 and val_2>val_1 and val_3==val_1 and dis_num_3<dis_num_1) or (val_2>val_1 and val_3>val_1 and val_4==val_1 and dis_num_4<dis_num_1) or (val_4>val_1 and val_2==val_1 and val_3==val_1 and dis_num_2<dis_num_1 and dis_num_3<dis_num_1) or (val_2>val_1 and val_4==val_1 and val_3==val_1 and dis_num_4<dis_num_1 and dis_num_3<dis_num_1) or (val_3>val_1 and val_2==val_1 and val_4==val_1 and dis_num_2<dis_num_1 and dis_num_4<dis_num_1) or (val_4==val_1 and val_2==val_1 and val_3==val_1 and dis_num_4<dis_num_1 and dis_num_2<dis_num_1 and dis_num_3<dis_num_1):
                change_position(position_1)
                refresh_game()
            else:
                position_number = int(random.choice(min_heuristic_positions))
                if position_number == 0:
                    change_position(position_1)
                    refresh_game()
                elif position_number == 1:
                    change_position(position_3)
                    refresh_game()
                elif position_number == 2:
                    change_position(position_5)
                    refresh_game()
                else:
                    change_position(position_7)
                    refresh_game()

        elif snake_photo == position_5:
            val_1 = next_step_heuristic(position_2)
            dis_num_1 = number_of_tiles_in_correct_place(position_2)
            val_2 = next_step_heuristic(position_4)
            dis_num_2 = number_of_tiles_in_correct_place(position_4)
            val_3 = next_step_heuristic(position_8)
            dis_num_3 = number_of_tiles_in_correct_place(position_8)
            if snake_queue[0]==2:
                val_1 = 50
                dis_num_1 = -1
            if snake_queue[0]==4:
                val_2 = 50
                dis_num_2 = -1
            if snake_queue[0]==8:
                val_3 = 50
                dis_num_3 = -1
            min_heuristic_positions = find_min_heuristic([val_1,val_2,val_3])
            print(f'Fidi pano:Her {val_1}:Num {dis_num_1}, Fidi aristera:Her {val_2}:Num {dis_num_2}, Fidi kato:Her {val_3}:Num {dis_num_3}')
            if (val_1>val_3 and val_2>val_3) or (val_1>val_3 and val_2==val_3 and dis_num_2<dis_num_3) or (val_1==val_3 and val_2>val_3 and dis_num_1<dis_num_3):
                change_position(position_8)
                refresh_game()
            elif (val_1>val_2 and val_3>val_2) or (val_1>val_2 and val_3==val_2 and dis_num_3<dis_num_2) or (val_1==val_2 and val_3>val_2 and dis_num_1<dis_num_2):
                change_position(position_4)
                refresh_game()
            elif (val_2>val_1 and val_3>val_1) or (val_2>val_1 and val_3==val_1 and dis_num_3<dis_num_1) or (val_2==val_1 and val_3>val_1 and dis_num_2<dis_num_1):
                change_position(position_2)
                refresh_game()
            else:
                position_number = int(random.choice(min_heuristic_positions))  
                if position_number == 0:
                    change_position(position_2)
                    refresh_game()
                elif position_number == 1:
                    change_position(position_4)
                    refresh_game()
                else:
                    change_position(position_8)
                    refresh_game()

        elif snake_photo == position_6:
            val_1 = next_step_heuristic(position_3)
            dis_num_1 = number_of_tiles_in_correct_place(position_3)
            val_2 = next_step_heuristic(position_7)
            dis_num_2 = number_of_tiles_in_correct_place(position_7)
            if snake_queue[0]==3: 
                val_1 = 50
                dis_num_1 = -1
            if snake_queue[0]==7:
                val_2 = 50
                dis_num_2 = -1
            print(f'Fidi pano:Her {val_1}:Num {dis_num_1}, Fidi deksia:Her {val_2}:Num {dis_num_2}')    
            if (val_1 > val_2) or (val_1 == val_2 and dis_num_2 > dis_num_1):
                change_position(position_7)
                refresh_game()
            else:
                change_position(position_3)
                refresh_game()
            
        elif snake_photo == position_7:
            val_1 = next_step_heuristic(position_4)
            dis_num_1 = number_of_tiles_in_correct_place(position_4)
            val_2 = next_step_heuristic(position_6)
            dis_num_2 = number_of_tiles_in_correct_place(position_6)
            val_3 = next_step_heuristic(position_8)
            dis_num_3 = number_of_tiles_in_correct_place(position_8)
            if snake_queue[0]==4:
                val_1 = 50
                dis_num_1 = -1
            if snake_queue[0]==6:
                val_2 = 50
                dis_num_2 = -1
            if snake_queue[0]==8:
                val_3 = 50
                dis_num_3 = -1
            min_heuristic_positions = find_min_heuristic([val_1,val_2,val_3])
            print(f'Fidi pano:Her {val_1}:Num {dis_num_1}, Fidi aristra:Her {val_2}:Num {dis_num_2}, Fidi deksia:Her {val_3}:Num {dis_num_3}')
            if (val_1>val_3 and val_2>val_3) or (val_1>val_3 and val_2==val_3 and dis_num_2<dis_num_3) or (val_1==val_3 and val_2>val_3 and dis_num_1<dis_num_3):
                change_position(position_8)
                refresh_game()
            elif (val_1>val_2 and val_3>val_2) or (val_1>val_2 and val_3==val_2 and dis_num_3<dis_num_2) or (val_1==val_2 and val_3>val_2 and dis_num_1<dis_num_2):
                change_position(position_6)
                refresh_game()
            elif (val_2>val_1 and val_3>val_1) or (val_2>val_1 and val_3==val_1 and dis_num_3<dis_num_1) or (val_2==val_1 and val_3>val_1 and dis_num_2<dis_num_1):
                change_position(position_4)
                refresh_game()
            else:
                position_number = int(random.choice(min_heuristic_positions))  
                if position_number == 0:
                    change_position(position_4)
                    refresh_game()
                elif position_number == 1:
                    change_position(position_6)
                    refresh_game()
                else:
                    change_position(position_8)
                    refresh_game()
            
        elif snake_photo == position_8:
            val_1 = next_step_heuristic(position_7)
            dis_num_1 = number_of_tiles_in_correct_place(position_7)
            val_2 = next_step_heuristic(position_5)
            dis_num_2 = number_of_tiles_in_correct_place(position_5)
            if snake_queue[0]==7: 
                val_1 = 50
                dis_num_1 = -1
            if snake_queue[0]==5:
                val_2 = 50
                dis_num_2 = -1
            print(f'Fidi aristera:Her {val_1}:Num {dis_num_1}, Fidi pano:Her {val_2}:Num {dis_num_2}')    
            if (val_1 > val_2) or (val_1 == val_2 and dis_num_2 > dis_num_1):
                change_position(position_5)
                refresh_game()
            else:
                change_position(position_7)
                refresh_game()
  
    def left_button_fun():
        if snake_photo == position_1:
            change_position(position_0)
            refresh_game()
        elif snake_photo == position_2:
            change_position(position_1)
            refresh_game()
        elif snake_photo == position_4:
            change_position(position_3)
            refresh_game()
        elif snake_photo == position_5:
            change_position(position_4)
            refresh_game()
        elif snake_photo == position_7:
            change_position(position_6)
            refresh_game()
        elif snake_photo == position_8:
            change_position(position_7)
            refresh_game()

    def right_button_fun():
        if snake_photo == position_1:
            change_position(position_2)
            refresh_game()
        elif snake_photo == position_0:
            change_position(position_1)
            refresh_game()
        elif snake_photo == position_4:
            change_position(position_5)
            refresh_game()
        elif snake_photo == position_3:
            change_position(position_4)    
            refresh_game()
        elif snake_photo == position_7:
            change_position(position_8)
            refresh_game()
        elif snake_photo == position_6:
           change_position(position_7)
           refresh_game()

    def up_button_fun():
        if snake_photo == position_5:
            change_position(position_2)
            refresh_game()
        elif snake_photo == position_4:
            change_position(position_1)
            refresh_game()
        elif snake_photo == position_8:
            change_position(position_5)
            refresh_game()
        elif snake_photo == position_7:
            change_position(position_4)
            refresh_game()
        elif snake_photo == position_3:
            change_position(position_0)
            refresh_game()
        elif snake_photo == position_6:
            change_position(position_3)
            refresh_game()

    def down_button_fun():
        if snake_photo == position_3:
            change_position(position_6)
            refresh_game()
        elif snake_photo == position_0:
            change_position(position_3)
            refresh_game()
        elif snake_photo == position_2:
            change_position(position_5)
            refresh_game()
        elif snake_photo == position_1:
            change_position(position_4)
            refresh_game()
        elif snake_photo == position_5:
            change_position(position_8)
            refresh_game()
        elif snake_photo == position_4:
            change_position(position_7)
            refresh_game()

    left_button = Button(frame_12, image=left_photo, command=left_button_fun)
    left_button.grid(row=0, column=0)
    right_button = Button(frame_12, image=right_photo, command=right_button_fun)
    right_button.grid(row=0, column=1)
    up_button = Button(frame_14, image=up_photo, command=up_button_fun)
    up_button.grid(row=0, column=0)
    down_button = Button(frame_14, image=down_photo, command=down_button_fun)
    down_button.grid(row=0, column=1)
    shuf_button = Button(frame_9, image=shuf_photo, command=shuf_photos)
    shuf_button.pack()
    exit_button = Button(frame_11, image=exit_photo, command=root.destroy)
    exit_button.pack()

    if numbers_photos_list == [number_1_photo, number_2_photo, number_3_photo, number_8_photo, snake_photo, number_4_photo, number_7_photo, number_6_photo, number_5_photo]:
        Button(frame_10, image=auto_photo, command=DISABLED).pack()
        Button(frame_13, image=you_won_photo , command='').pack()
        print('Congrats!!!')
    else:
        play_button = Button(frame_10, image=auto_photo, command=auto)
        play_button.pack()
        puzzle_button = Button(frame_13, image=puzzle_photo , command='')   
        puzzle_button.pack()

start_game()

root.resizable(0,0)
root.mainloop()