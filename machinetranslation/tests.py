from transcription import english_to_french
from transcription import french_to_english


translate1 = english_to_french('')
print("Hello in french is "+translate1)

translate2 = french_to_english('')
print("Bounjour means "+translate2)

translate1 = english_to_french('Hello')
print("Hello in french is "+translate1)

translate2 = french_to_english('Bonjour')
print("Bounjour means "+translate2)