from sys import argv
import sty

def gradient(text: str, r1: int, g1: int, b1: int, r2: int, g2: int, b2: int) -> str:
    """Prints text in a gradient. The starting color is (r1, g1, b1), and the ending color is (r2, g2, b2)."""
    to_return = ''
    # Get the step size
    size = len(text)
    
    # Get the step size for each color
    r_step = (r2 - r1) / size
    g_step = (g2 - g1) / size
    b_step = (b2 - b1) / size
    
    # Initialize the colors
    r = r1
    g = g1
    b = b1
    for character in text:
        # Add the escape code for the next color, and then add the character that will be that color
        to_return += sty.fg.rgb_call(int(r), int(g), int(b)) + character
        
        # Increment the colors for next character
        r += r_step
        g += g_step
        b += b_step
    # Reset the color at the end of the loop
    to_return += sty.rs.fg
    
    return to_return

if __name__ == '__main__':
    
    if len(argv) != 8:
        print("Usage: gradient to_print r1 g1 b1 r2 g2 b2")
        raise SystemExit(0)
    
    to_print = argv[1]
    r1 = int(argv[2])
    g1 = int(argv[3])
    b1 = int(argv[4])
    r2 = int(argv[5])
    g2 = int(argv[6])
    b2 = int(argv[7])
    
    
    print(gradient(to_print, r1, g1, b1, r2, g2, b2))




