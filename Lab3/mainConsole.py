from library.calc import *
from UI.inputHandler import *
from UI.outputHandler import *

input = HandleInputConsole()
HandleOutputConsole(input,LinearList(input))