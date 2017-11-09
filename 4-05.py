#created by raymond octavious
#created on november
#created for isc3u

import ui

#constant
PI = 3.14
def calculate_volume(radius, height):
    #calculated volume
    
    
    
    volume = 2 * PI * radius ** 2 * height
    return volume
    
def calculate_button(sender):

    radius = float(view['radius_textfield'].text)
    height = float(view['height_textfield'].text)
    answer = calculate_volume(radius, height)
    view['answer_label'].text = str(answer)

view = ui.load_view()
view.present('sheet')
