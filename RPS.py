import customtkinter as ctk
import random

user_score = 0
comp_score = 0
user_name = ""

def start_game():
    global user_name
    user_name = name_entry.get()
    if user_name:
        welcome_label.configure(text=f"Welcome, {user_name}! Let's play Rock-Paper-Scissors!")
        name_entry.destroy()
        start_button.destroy()
        create_game()

def play_round(user_choice):
    global user_score, comp_score

    options = ["Rock", "Paper", "Scissors"]
    comp_choice = random.choice(options)

    if user_choice == comp_choice:
        result = "It's a tie!"
    elif (user_choice == "Rock" and comp_choice == "Scissors") or \
         (user_choice == "Scissors" and comp_choice == "Paper") or \
         (user_choice == "Paper" and comp_choice == "Rock"):
        result = "You win!"
        user_score += 1
    else:
        result = "You lose!"
        comp_score += 1

    result_label.configure(text=f"User: {user_choice}\nComputer: {comp_choice}\n{result}")
    user_score_label.configure(text=f"{user_name} Score: {user_score}")
    comp_score_label.configure(text=f"Computer Score: {comp_score}")

    if user_score == 5:
        result_label.configure(text=f"Congratulations, {user_name}! You won the game!")
        disable_buttons()
    elif comp_score == 5:
        result_label.configure(text="Sorry, the computer won the game!")
        disable_buttons()

def disable_buttons():
    rock_button.configure(state="disabled")
    paper_button.configure(state="disabled")
    scissors_button.configure(state="disabled")

def reset_game():
    global user_score, comp_score
    user_score = 0
    comp_score = 0
    user_score_label.configure(text=f"{user_name} Score: 0")
    comp_score_label.configure(text="Computer Score: 0")
    result_label.configure(text="")
    enable_buttons()

def enable_buttons():
    rock_button.configure(state="normal")
    paper_button.configure(state="normal")
    scissors_button.configure(state="normal")

def create_game():
    global result_label, user_score_label, comp_score_label, rock_button, paper_button, scissors_button

    main_frame.pack_forget()
    main_frame_game = ctk.CTkFrame(window, corner_radius=0)
    main_frame_game.pack(fill="both", expand=True)

    title_label = ctk.CTkLabel(main_frame_game, text="Rock-Paper-Scissors", font=("Arial", 20))
    title_label.pack(pady=20)

    result_label = ctk.CTkLabel(main_frame_game, text="", font=("Arial", 16))
    result_label.pack(pady=10)

    user_score_label = ctk.CTkLabel(main_frame_game, text=f"{user_name} Score: 0", font=("Arial", 14))
    user_score_label.pack()

    comp_score_label = ctk.CTkLabel(main_frame_game, text="Computer Score: 0", font=("Arial", 14))
    comp_score_label.pack()

    button_frame = ctk.CTkFrame(main_frame_game)
    button_frame.pack(pady=20)

    rock_button = ctk.CTkButton(button_frame, text="Rock", command=lambda: play_round("Rock"))
    rock_button.grid(row=0, column=0, padx=10)

    paper_button = ctk.CTkButton(button_frame, text="Paper", command=lambda: play_round("Paper"))
    paper_button.grid(row=0, column=1, padx=10)

    scissors_button = ctk.CTkButton(button_frame, text="Scissors", command=lambda: play_round("Scissors"))
    scissors_button.grid(row=0, column=2, padx=10)

    reset_button = ctk.CTkButton(main_frame_game, text="Play Again", command=reset_game)
    reset_button.pack(pady=10)

def create_main_window():
    global window, main_frame, welcome_label, name_entry, start_button

    window = ctk.CTk()
    window.title("Rock-Paper-Scissors")
    window.geometry("500x400")
    window.resizable(False, False)

    main_frame = ctk.CTkFrame(window, corner_radius=0)
    main_frame.pack(fill="both", expand=True)

    welcome_label = ctk.CTkLabel(main_frame, text="Enter your name to start the game:", font=("Arial", 16))
    welcome_label.pack(pady=20)

    name_entry = ctk.CTkEntry(main_frame, width=200)
    name_entry.pack(pady=10)

    start_button = ctk.CTkButton(main_frame, text="Start Game", command=start_game)
    start_button.pack(pady=10)

if __name__ == "__main__":
    create_main_window()
    window.mainloop()
