# colors
Colors for inline use to transform your terminal output


![Screenshot from 2022-12-23 20-11-37](https://user-images.githubusercontent.com/108424001/209420922-e1427e80-b5f7-4c5a-8268-b9305ffbab9e.png)



![Screenshot from 2022-12-23 20-13-38](https://user-images.githubusercontent.com/108424001/209420920-608dfe3c-5846-4c47-8e7c-fecac576866e.png)

Tested on MacOS and Linux

## Installation

```bash
cd <project directory>
git clone https://github.com/Donny-GUI/colors.git

```

## Use inside program

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
