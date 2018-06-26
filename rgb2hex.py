def rgb_hex():
  invalid_msg = "Ivalid value."
  try:
    red = int(raw_input("Enter red (R) value: "))
  except ValueError:
    print "Not a number!"
    return
  if red < 0 or red > 255:
    print invalid_msg
    return
  try:
    green = int(raw_input("Enter green (G) value: "))
  except ValueError:
    print "Not a number!"
    return
  if green < 0 or green > 255:
   print invalid_msg
   return
  try:
    blue = int(raw_input("Enter blue (B) value: "))
  except ValueError:
    print "Not a number!"
    return
  if blue < 0 or blue > 255:
   print invalid_msg
   return
  val = (red << 16) + (green << 8) + blue
  if len(hex(val)[2::]) <= 6:
    x = 6 - len(hex(val)[2::])
    print "Your hexadecimal value: %s" % (hex(val)[2::]).upper() + "0" * x

def hex_rgb():
  hex_val = raw_input("Enter your hexadecimal value (without # symbol): ")
  if len(hex_val) != 6:
    print "Ivalid value."
    return
  else:
    hex_val = int(hex_val, 16)
  
  two_hex_digits = 2 ** 8
  blue = hex_val % two_hex_digits
  hex_val = hex_val >> 8 
  green = hex_val % two_hex_digits
  hex_val = hex_val >> 8
  red = hex_val % two_hex_digits
  print "Red: %s Green: %s Blue: %s" % (red,green,blue)

def convert():
  while True:
    option = raw_input("Enter 1 to convert RGB to HEX. Enter 2 to convert HEX to RGB. Enter X to Exit: ")
    if option == "1":
      print "RGB to HEX..."
      rgb_hex()
    elif option == "2":
      print "HEX to RGB..."
      hex_rgb()
    elif option == "X" or option == "x":
      break
    else:
      print "Error"

convert()
