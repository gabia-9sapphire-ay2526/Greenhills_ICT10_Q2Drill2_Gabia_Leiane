# Candidate Verification System
from pyscript import display, document


def name_finder(e):
    document.getElementById('result').innerHTML = ' '
    first_name = document.getElementById('firstname').value
    last_name = document.getElementById('surname').value
    candidate_name = first_name + ' ' + last_name
    candidates_name = ['Leiane Gabia', 'Alexa Agnote', 'Bonnie Nubla', 'Keane Pacaña', 'Almakram Arbison', 'Sebastian Uclaray', 'Franco Deocampo',]
    student_checker = candidate_name in candidates_name

    display_message = (
        f'Sorry {candidate_name}, your name is not on the list.', f'Congratulations {candidate_name}! You are now part of the ICT club.')

    display(display_message[student_checker], target='result')

