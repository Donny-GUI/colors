# colors
color codes and such


## Installation

```bash
cd <project directory>
git clone https://github.com/Donny-GUI/colors.git

```

```Python3
import colors

# add color to text 
print(f"{colors.fg.green}hello world{endc}")

```

## or

```Python3
from colors import fg, bg, font

# yellow italic text
print(f"{font.italic}{fg.yellow}hi mom{endc}")

# background green on bold
print(f"{bg.green}{font.bold}Ray Finkle Dolphins kicker{endc}")

```
