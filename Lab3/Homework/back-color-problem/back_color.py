from random import *

shapes = [
    {
        'text': 'blue',
        'color': '#3F51B5',
        'rect': [20, 60, 100, 100]
    },
    {
        'text': 'red',
        'color': '#C62828',
        'rect': [140, 60, 100, 100]
    },
    {
        'text': 'yellow',
        'color': '#FFD600',
        'rect': [20, 180, 100, 100]
    },
    {
        'text': 'green',
        'color': '#4CAF50',
        'rect': [140, 180, 100, 100]
    }
]


def get_shapes():
    return shapes


def generate_quiz():
    a = choice(shapes)
    t = a['text']
    b = choice(shapes)
    c = b['color']
    d = choice(shapes)
    # r = d['rect']
    ra = randint(0,1) # 0 : meaning, 1: color
    return [
                t,
                c,
                ra,
            ]
# t = generate_quiz()
# print(t)
def mouse_press(x, y, text, color, quiz_type):
    text,color,quiz_type = generate_quiz()
    if quiz_type == 0:
        if text == "blue":
            if 20 <= x <= 120 and 60 <= y <= 160:
                if quiz_type == 0:
                    return True
                else: 
                    return False
            else:
                return False 
        elif text == "red":
            if 140 <= x <= 240 and 60 <= y <= 160:
                if quiz_type == 0:
                    return True
                else:
                    return False
            else:
                return False
        elif text == "yellow":
            if 20 <= x <= 120 and 180 <= y <= 280:
                if quiz_type == 0:
                    return True
                else: 
                    return False
            else:
                return False
        elif text == "green":
            if 140 <= x <= 240 and 180 <= y <= 280:
                if quiz_type == 0:
                    return True
                else: 
                    return False
            else:
                return False
    elif quiz_type == 1:
        if color == "#3F51B5":
            if 20 <= x <= 120 and 60 <= y <= 160:
                if quiz_type == 1:
                    return True
                else:
                    return False
            else: 
                return False
        elif color == "#C62828":
            if 140 <= x <= 240 and 60 <= y <= 160:
                if quiz_type == 1:
                    return True
                else:
                    return False
            else: 
                return False
        elif color == "#FFD600":    
            if 20 <= x <= 120 and 180 <= y <= 280:
                if quiz_type == 1:
                    return True
                else:
                    return False
            else: 
                return False
        elif color =="#4CAF50":
            if 140 <= x <= 240 and 180 <= y <= 280:
                if quiz_type == 1:
                    return True
                else:
                    return False
            else: 
                return False