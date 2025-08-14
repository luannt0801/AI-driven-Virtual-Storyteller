import subprocess
import os

def run_story_generator(prompt):
    bat_file = r'd:\2025\Master BKHN\Ky thuat lap trinh noi dung so\AI-driven-Virtual-Storyteller\run.bat'
    command = [bat_file]
    env = dict(**os.environ)
    env['PROMPT'] = prompt
    process = subprocess.Popen(command, shell=True, env=env)
    process.communicate()

if __name__ == "__main__":
    user_prompt = input("Enter your story prompt: ")
    run_story_generator(user_prompt)