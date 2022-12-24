
class fg:
	black = '\033[30m'
	red = '\033[31m'
	green = '\033[32m'
	yellow = '\033[33m'
	magenta = '\033[34m'
	blue = '\033[35m'
	cyan = '\033[36m'
	white = '\033[37m'
	endc = '\033[0m'
	color = {'black': '\x1b[30m', 'red': '\x1b[31m', 'green': '\x1b[32m', 'yellow': '\x1b[33m', 'magenta': '\x1b[34m', 'blue': '\x1b[35m', 'cyan': '\x1b[36m', 'white': '\x1b[37m'}

class bg:
	black = '\033[40m'
	red = '\033[41m'
	green = '\033[42m'
	yellow = '\033[43m'
	magenta = '\033[44m'
	blue = '\033[45m'
	cyan = '\033[46m'
	white = '\033[47m'
	endc = '\033[0m'
	color = {'black': '\x1b[40m', 'red': '\x1b[41m', 'green': '\x1b[42m', 'yellow': '\x1b[43m', 'magenta': '\x1b[44m', 'blue': '\x1b[45m', 'cyan': '\x1b[46m', 'white': '\x1b[47m'}

class font:
	bold = '\033[1m'
	dim = '\033[2m'
	italic = '\033[3m'
	underline = '\033[4m'
	blink = '\033[5m'
	endc = '\033[0m'
	style = {'bold': '\x1b[1m', 'dim': '\x1b[2m', 'italic': '\x1b[3m', 'underline': '\x1b[4m', 'blink': '\x1b[5m'} 

class Names:
	colors = ['black', 'red', 'green', 'yellow', 'magenta', 'blue', 'cyan', 'white']
	fonts = font_names = ['bold', 'dim', 'italic', 'underline', 'blink']

class Codes:
	fg = [fg.black, fg.red, fg.green, fg.yellow, fg.magenta, fg.blue, fg.cyan, fg.white] 
	bg = [bg.black, bg.red, bg.green, bg.yellow, bg.magenta, bg.blue, bg.cyan, bg.white]
	font = [font.bold, font.dim, font.italic, font.underline, font.blink]

foreground = {'black': '\x1b[30m', 'red': '\x1b[31m', 'green': '\x1b[32m', 'yellow': '\x1b[33m', 'magenta': '\x1b[34m', 'blue': '\x1b[35m', 'cyan': '\x1b[36m', 'white': '\x1b[37m'}
background = {'black': '\x1b[40m', 'red': '\x1b[41m', 'green': '\x1b[42m', 'yellow': '\x1b[43m', 'magenta': '\x1b[44m', 'blue': '\x1b[45m', 'cyan': '\x1b[46m', 'white': '\x1b[47m'}
fonts = {'bold': '\x1b[1m', 'dim': '\x1b[2m', 'italic': '\x1b[3m', 'underline': '\x1b[4m', 'blink': '\x1b[5m'}
