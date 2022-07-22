graph = {'M1':
             ['You a cop?',
              ('No, I’m a claims adjuster.', 'M3'),
              ('Private investigator. I have a few questions.', 'M2'),
              ('Yeah, I’m a plain-clothes cop. I’ve got questions for you.', 'M2')],
         'M2':
             ['Nah, you’re dressed too smart. I reckon you work for the insurers.',
              ('Lucky guess.', 'M3'),
              ('That’s for me to know, and you to guess at', 'M3')],
         'M3':
             ['I reckon this counts as an act of God.',
              ('What happened?', 'M4'),
              ('I''m outta here!', 'END')],
         'M4':
             ['You have no choice anymore, this ends now!',
              ('Goodbye.', 'END')]
        }

for scene in graph:
    print(graph[scene][0]
              
              
