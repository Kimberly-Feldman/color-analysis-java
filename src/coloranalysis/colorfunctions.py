import urllib.request, json
from . import colorfunctionshelper as cfh







#uses dictionary of palette colors to suggest a color for overlaying font
#calculates the inverse of the average value of the colors, converts to grey scale
#resulting hex will be some varient of grey, with a contrasting darkness
def suggested_font_color(user_url, color_modifier = "black"):

    colors = cfh.imgix_json(user_url)
    num_of_colors = 0

    red_sum = 0
    blue_sum = 0
    green_sum = 0

    #128 is chosen because it is the median value
    grey_color = False
    grey_value = 128
    grey_cutoff = 90

    #values can be adjusted if more contrast is needed
    red_modifier = 0
    green_modifier = 0
    blue_modifier = 0
    modify_amount = 0
    
    if (color_modifier == "teal"):
        red_modifier = modify_amount
    elif (color_modifier == "violet"):
        green_modifier = modify_amount
    elif (color_modifier == "olive"):
        blue_modifier = modify_amount


    elif (color_modifier == "indigo"):
        red_modifier = modify_amount
        green_modifier = modify_amount   
    elif (color_modifier == "mauve"):
        green_modifier = modify_amount
        blue_modifier = modify_amount
    elif (color_modifier == "emerald"):
        red_modifier = modify_amount
        blue_modifier = modify_amount

    else:
        color_modifier == "black"
        red_modifier = modify_amount
        green_modifier = modify_amount
        blue_modifier = modify_amount

    for i in colors:
        num_of_colors += 1
        curr_red = i.get("red", "none")
        curr_green = i.get("green", "none")
        curr_blue = i.get("blue", "none")

        #values are originally 0-1
        red_sum += (255*curr_red)
        green_sum += (255*curr_green)
        blue_sum += (255*curr_blue)

        #if the colors in the palette are mostly medium grey, then inverting the colors won't provide enough contrast
        #a slightly different approach will be implemented
        if grey_color is False:
            curr_sum = abs(grey_value - curr_red)
            curr_sum += abs(grey_value - curr_green)
            curr_sum += abs(grey_value - curr_blue)

            if (curr_sum < grey_cutoff):
                grey_color = True

    
    red = int((red_sum//num_of_colors))
    green = int((green_sum//num_of_colors))
    blue = int((blue_sum//num_of_colors))

    inverse_red = 255-red
    inverse_green = 255-green
    inverse_blue = 255-blue


    average_value = (red + green + blue)//3
    average_inverse_value = 255-average_value

    ##grey_color becomes False, because the grey values will contrast
    if (abs(average_inverse_value - grey_value) > grey_cutoff//3):
        grey_color = False

    if grey_color:
        pass
    #### add


    suggested_value = average_inverse_value

    red_hex_value = hex(suggested_value-red_modifier) + ""
    red_hex_value = red_hex_value[2:]
    if len(red_hex_value) == 1:
        red_hex_value =  "0" + red_hex_value

    green_hex_value = hex(suggested_value-green_modifier) + ""
    green_hex_value = green_hex_value[2:]
    if len(green_hex_value) == 1:
        green_hex_value =  "0" + green_hex_value

    blue_hex_value = hex(suggested_value-blue_modifier) + ""
    blue_hex_value = blue_hex_value[2:]
    if len(blue_hex_value) == 1:
        blue_hex_value =  "0" + blue_hex_value

    full_hex_value = "#" + red_hex_value + green_hex_value + blue_hex_value

    return full_hex_value

def color_values(user_url):

    colors = cfh.imgix_json(user_url)
    hex_colors = []

    for i in colors:
        curr_hex = i.get("hex", "none")
        hex_colors.append(curr_hex)


    return hex_colors


