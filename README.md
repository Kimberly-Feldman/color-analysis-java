This library contains several methods to aid in color analysis of a picture hosted on imgix.


1.suggested_font_color(user_url, color_modifier = "black")

user_url is required
color_modifier is optional, the default being black

user_url must be a imgix link to a jpg
valid color_modifier values are "black", "emerald", "mauve", "indigo", "olive", "violet", "teal"


Purpose: Intake a palette of colors from a imgix jpg URL link and output a suggested font color that will contrast with the background image.  The color will typically be some form of grey, but in the case of a moderately grey background image the color modifier will be implemented to ensure the text still stays legible.


2.color_values(user_url)

user_url is required
user_url must be a imgix link to a jpg

Purpose: Intake a palette of colors from a imgix jpg URL link and output a list containing the six main palette color hex values




