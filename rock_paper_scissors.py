import tkinter as tk
from tkinter import ttk
import random
from PIL import Image, ImageTk, ImageDraw
import io

class ModernRockPaperScissorsGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("🎮 Rock Paper Scissors 🎮")
        self.root.geometry("900x700")
        self.root.configure(bg='#667eea')
        self.root.resizable(False, False)
        
        # Game variables
        self.player_score = 0
        self.computer_score = 0
        self.current_round = 1
        self.max_rounds = 5
        self.is_playing = False
        
        # Emoji mappings
        self.emojis = {'rock': '🪨', 'paper': '📄', 'scissors': '✂️'}
        self.choices = ['rock', 'paper', 'scissors']
        
        # Colors matching the web design
        self.colors = {
            'primary_gradient_start': '#667eea',
            'primary_gradient_end': '#764ba2',
            'battle_gradient_start': '#f093fb',
            'battle_gradient_end': '#f5576c',
            'gameover_gradient_start': '#fa709a',
            'gameover_gradient_end': '#fee140',
            'white': '#ffffff',
            'text_dark': '#555555',
            'shadow': 'rgba(0, 0, 0, 0.3)'
        }
        
        self.create_gradient_background()
        self.setup_ui()
    
    def create_gradient_background(self):
        """Create gradient background effect"""
        # Create a canvas for gradient background
        self.bg_canvas = tk.Canvas(self.root, width=900, height=700, highlightthickness=0)
        self.bg_canvas.place(x=0, y=0)
        
        # Create gradient effect with rectangles
        for i in range(700):
            # Calculate color interpolation
            ratio = i / 700
            r1, g1, b1 = 102, 126, 234  # #667eea
            r2, g2, b2 = 118, 75, 162   # #764ba2
            
            r = int(r1 + (r2 - r1) * ratio)
            g = int(g1 + (g2 - g1) * ratio)
            b = int(b1 + (b2 - b1) * ratio)
            
            color = f"#{r:02x}{g:02x}{b:02x}"
            self.bg_canvas.create_line(0, i, 900, i, fill=color, width=1)
    
    def create_rounded_rectangle(self, canvas, x1, y1, x2, y2, radius=25, **kwargs):
        """Create a rounded rectangle on canvas"""
        points = []
        for x, y in [(x1, y1 + radius), (x1, y1), (x1 + radius, y1),
                     (x2 - radius, y1), (x2, y1), (x2, y1 + radius),
                     (x2, y2 - radius), (x2, y2), (x2 - radius, y2),
                     (x1 + radius, y2), (x1, y2), (x1, y2 - radius)]:
            points.extend([x, y])
        return canvas.create_polygon(points, smooth=True, **kwargs)
    
    def setup_ui(self):
        # Main container frame with rounded corners effect
        main_frame = tk.Frame(self.root, bg='white', relief=tk.RAISED, bd=0)
        main_frame.place(x=50, y=50, width=800, height=600)
        
        # Title
        title_label = tk.Label(
            main_frame,
            text="🎮 Rock Paper Scissors 🎮",
            font=("Segoe UI", 28, "bold"),
            bg='white',
            fg='#667eea'
        )
        title_label.pack(pady=(30, 10))
        
        # Round info
        self.round_label = tk.Label(
            main_frame,
            text=f"Round {self.current_round} of {self.max_rounds}",
            font=("Segoe UI", 16),
            bg='white',
            fg='#555555'
        )
        self.round_label.pack(pady=(0, 20))
        
        # Score board
        score_frame = tk.Frame(main_frame, bg='white')
        score_frame.pack(pady=(0, 30))
        
        # Player score box
        player_score_frame = tk.Frame(score_frame, bg='#667eea', relief=tk.RAISED, bd=3)
        player_score_frame.pack(side=tk.LEFT, padx=20, ipadx=30, ipady=15)
        
        tk.Label(
            player_score_frame,
            text="Your Score",
            font=("Segoe UI", 12),
            bg='#667eea',
            fg='white'
        ).pack()
        
        self.player_score_label = tk.Label(
            player_score_frame,
            text="0",
            font=("Segoe UI", 36, "bold"),
            bg='#667eea',
            fg='white'
        )
        self.player_score_label.pack()
        
        # Computer score box
        computer_score_frame = tk.Frame(score_frame, bg='#764ba2', relief=tk.RAISED, bd=3)
        computer_score_frame.pack(side=tk.RIGHT, padx=20, ipadx=30, ipady=15)
        
        tk.Label(
            computer_score_frame,
            text="Computer Score",
            font=("Segoe UI", 12),
            bg='#764ba2',
            fg='white'
        ).pack()
        
        self.computer_score_label = tk.Label(
            computer_score_frame,
            text="0",
            font=("Segoe UI", 36, "bold"),
            bg='#764ba2',
            fg='white'
        )
        self.computer_score_label.pack()
        
        # Choices container
        self.choices_frame = tk.Frame(main_frame, bg='white')
        self.choices_frame.pack(pady=20)
        
        # Choose weapon label
        tk.Label(
            self.choices_frame,
            text="Choose Your Weapon!",
            font=("Segoe UI", 20, "bold"),
            bg='white',
            fg='#667eea'
        ).pack(pady=(0, 20))
        
        # Choice buttons
        buttons_frame = tk.Frame(self.choices_frame, bg='white')
        buttons_frame.pack()
        
        self.choice_buttons = {}
        button_configs = [
            ('rock', '🪨', 0),
            ('paper', '📄', 1),
            ('scissors', '✂️', 2)
        ]
        
        for choice, emoji, col in button_configs:
            btn_frame = tk.Frame(buttons_frame, bg='white', relief=tk.RAISED, bd=4)
            btn_frame.grid(row=0, column=col, padx=15, pady=10)
            
            btn = tk.Button(
                btn_frame,
                text=emoji,
                font=("Segoe UI", 48),
                bg='white',
                fg='black',
                relief=tk.FLAT,
                bd=0,
                cursor='hand2',
                command=lambda c=choice: self.play_round(c),
                width=3,
                height=2
            )
            btn.pack(padx=10, pady=10)
            self.choice_buttons[choice] = btn
            
            # Add hover effects
            btn.bind("<Enter>", lambda e, b=btn: self.on_button_hover(b, True))
            btn.bind("<Leave>", lambda e, b=btn: self.on_button_hover(b, False))
        
        # Battle area (initially hidden)
        self.battle_frame = tk.Frame(main_frame, bg='#f093fb', relief=tk.RAISED, bd=3)
        
        tk.Label(
            self.battle_frame,
            text="Battle!",
            font=("Segoe UI", 24, "bold"),
            bg='#f093fb',
            fg='white'
        ).pack(pady=(15, 10))
        
        # Battle choices display
        battle_choices_frame = tk.Frame(self.battle_frame, bg='#f093fb')
        battle_choices_frame.pack(pady=10)
        
        self.player_choice_label = tk.Label(
            battle_choices_frame,
            text="",
            font=("Segoe UI", 60),
            bg='#f093fb',
            fg='white'
        )
        self.player_choice_label.pack(side=tk.LEFT, padx=20)
        
        tk.Label(
            battle_choices_frame,
            text="VS",
            font=("Segoe UI", 24, "bold"),
            bg='#f093fb',
            fg='white'
        ).pack(side=tk.LEFT, padx=20)
        
        self.computer_choice_label = tk.Label(
            battle_choices_frame,
            text="",
            font=("Segoe UI", 60),
            bg='#f093fb',
            fg='white'
        )
        self.computer_choice_label.pack(side=tk.LEFT, padx=20)
        
        # Result message
        self.result_message_label = tk.Label(
            self.battle_frame,
            text="",
            font=("Segoe UI", 18, "bold"),
            bg='#f093fb',
            fg='white'
        )
        self.result_message_label.pack(pady=(10, 20))
        
        # Game over frame (initially hidden)
        self.game_over_frame = tk.Frame(main_frame, bg='#fa709a', relief=tk.RAISED, bd=3)
        
        self.final_message_label = tk.Label(
            self.game_over_frame,
            text="",
            font=("Segoe UI", 28, "bold"),
            bg='#fa709a',
            fg='white'
        )
        self.final_message_label.pack(pady=(20, 10))
        
        self.final_score_label = tk.Label(
            self.game_over_frame,
            text="",
            font=("Segoe UI", 18),
            bg='#fa709a',
            fg='white'
        )
        self.final_score_label.pack(pady=10)
        
        # Play again button
        self.play_again_button = tk.Button(
            self.game_over_frame,
            text="Play Again!",
            font=("Segoe UI", 16, "bold"),
            bg='white',
            fg='#667eea',
            relief=tk.RAISED,
            bd=3,
            cursor='hand2',
            command=self.reset_game,
            padx=30,
            pady=10
        )
        self.play_again_button.pack(pady=(10, 20))
        
        # Add hover effect to play again button
        self.play_again_button.bind("<Enter>", lambda e: self.play_again_button.config(bg='#f0f0f0'))
        self.play_again_button.bind("<Leave>", lambda e: self.play_again_button.config(bg='white'))
    
    def on_button_hover(self, button, is_entering):
        """Handle button hover effects"""
        if is_entering:
            button.config(bg='#f0f0f0', relief=tk.RAISED, bd=2)
        else:
            button.config(bg='white', relief=tk.FLAT, bd=0)
    
    def play_round(self, player_choice):
        """Play a round of the game"""
        if self.is_playing:
            return
        
        self.is_playing = True
        
        # Disable choice buttons
        for btn in self.choice_buttons.values():
            btn.config(state=tk.DISABLED)
        
        # Hide choices and show battle area
        self.choices_frame.pack_forget()
        self.battle_frame.pack(pady=20, padx=50, fill=tk.X)
        
        # Get computer choice
        computer_choice = random.choice(self.choices)
        
        # Display choices
        self.player_choice_label.config(text=self.emojis[player_choice])
        self.computer_choice_label.config(text=self.emojis[computer_choice])
        
        # Determine winner after a short delay
        self.root.after(500, lambda: self.determine_winner(player_choice, computer_choice))
    
    def determine_winner(self, player_choice, computer_choice):
        """Determine the winner and update the game state"""
        winner = self.get_winner(player_choice, computer_choice)
        
        # Update result message
        if winner == 'player':
            self.result_message_label.config(text="You Win This Round! 🎉")
            self.player_score += 1
        elif winner == 'computer':
            self.result_message_label.config(text="Computer Wins This Round! 😢")
            self.computer_score += 1
        else:
            self.result_message_label.config(text="It's a Tie! 🤝")
        
        # Update score display
        self.player_score_label.config(text=str(self.player_score))
        self.computer_score_label.config(text=str(self.computer_score))
        
        # Check if game is over
        if self.current_round >= self.max_rounds:
            self.root.after(2000, self.end_game)
        else:
            self.current_round += 1
            self.round_label.config(text=f"Round {self.current_round} of {self.max_rounds}")
            self.root.after(2000, self.continue_game)
    
    def get_winner(self, player, computer):
        """Determine the winner of a round"""
        if player == computer:
            return 'tie'
        elif (player == 'rock' and computer == 'scissors') or \
             (player == 'paper' and computer == 'rock') or \
             (player == 'scissors' and computer == 'paper'):
            return 'player'
        else:
            return 'computer'
    
    def continue_game(self):
        """Continue to the next round"""
        # Hide battle area and show choices
        self.battle_frame.pack_forget()
        self.choices_frame.pack(pady=20)
        
        # Re-enable choice buttons
        for btn in self.choice_buttons.values():
            btn.config(state=tk.NORMAL)
        
        self.is_playing = False
    
    def end_game(self):
        """End the game and show final results"""
        # Hide battle area and choices
        self.battle_frame.pack_forget()
        self.choices_frame.pack_forget()
        
        # Show game over screen
        self.game_over_frame.pack(pady=20, padx=50, fill=tk.X)
        
        # Set final message
        if self.player_score > self.computer_score:
            self.final_message_label.config(text="🎊 You Won the Game! 🎊")
        elif self.computer_score > self.player_score:
            self.final_message_label.config(text="💻 Computer Won! Better Luck Next Time! 💻")
        else:
            self.final_message_label.config(text="🤝 It's a Tie Game! 🤝")
        
        # Set final score
        self.final_score_label.config(
            text=f"Final Score: {self.player_score} - {self.computer_score}"
        )
    
    def reset_game(self):
        """Reset the game to initial state"""
        # Reset game variables
        self.current_round = 1
        self.player_score = 0
        self.computer_score = 0
        self.is_playing = False
        
        # Update displays
        self.round_label.config(text=f"Round {self.current_round} of {self.max_rounds}")
        self.player_score_label.config(text="0")
        self.computer_score_label.config(text="0")
        
        # Hide game over screen and show choices
        self.game_over_frame.pack_forget()
        self.choices_frame.pack(pady=20)
        
        # Re-enable choice buttons
        for btn in self.choice_buttons.values():
            btn.config(state=tk.NORMAL)

if __name__ == "__main__":
    root = tk.Tk()
    game = ModernRockPaperScissorsGUI(root)
    root.mainloop()
