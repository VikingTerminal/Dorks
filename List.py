import time
from colorama import Fore, Style
import random

def type_effect(text, speed):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(speed)
    print()

def save_to_file(content):
    try:
        with open("output.txt", 'w') as file:
            file.write(content)
        print(f"{Fore.CYAN}Contenuto salvato con successo in 'output.txt'.{Style.RESET_ALL}")
    except Exception as e:
        print(f"{Fore.RED}Errore durante il salvataggio del file: {e}{Style.RESET_ALL}")

def read_and_display(file_path, speed):
    try:
        with open(file_path, 'r') as file:
            content = file.read()

            
            save_response = input(f"{Fore.CYAN}Vuoi salvare il contenuto in un file di testo? (yes/no): {Style.RESET_ALL}")
            if save_response.lower() == 'yes':
                save_to_file(content)
            elif save_response.lower() != 'no':
                print(f"{Fore.RED}Risposta non valida. Il contenuto non è stato salvato.{Style.RESET_ALL}")
                return

            lines = content.split('\n')

            
            start_index = lines.index('Google Dorks Updated Database:') if 'Google Dorks Updated Database:' in lines else 0

            for i in range(start_index + 1, len(lines)):
                
                random_color = random.choice([Fore.RED, Fore.GREEN, Fore.WHITE])
                colored_line = f"{random_color}{lines[i]}{Style.RESET_ALL}"
                type_effect(colored_line, speed)
                print()  # Aggiunge uno spazio vuoto dopo ogni riga

            
            symbols = ['-', '\\', '|', '/']
            for _ in range(20):
                for symbol in symbols:
                    print(f"\r{Fore.MAGENTA}{symbol}{Style.RESET_ALL}", end='', flush=True)
                    time.sleep(0.1)
            print()

            
            progress_bar_length = 30
            for i in range(progress_bar_length + 1):
                progress = i / progress_bar_length
                bar_color = f"{Fore.BLUE}{Style.BRIGHT}"
                space_color = f"{Style.RESET_ALL}"
                bar = int(progress * progress_bar_length)
                progress_bar = f"{bar_color}[{'#' * bar}{' ' * (progress_bar_length - bar)}]{space_color}"
                print(f"\r{progress_bar}", end='', flush=True)
                time.sleep(speed)

            print(f"\n{Fore.CYAN}Grazie per aver provato questo tool! Visita t.me/VikingTerminal per altri strumenti.{Style.RESET_ALL}")

    except FileNotFoundError:
        print(f"{Fore.RED}Errore: Il file '{file_path}' non esiste.{Style.RESET_ALL}")

if __name__ == "__main__":
    file_name = "dorks.txt"
    speed = 0.01
    read_and_display(file_name, speed)
