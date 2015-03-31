from cx_Freeze import setup, Executable
# NOTE: you can include any other necessary external imports here aswell

includefiles = [] # include any files here that you wish
includes = []
excludes = []
packages = ['pygame', 'random', 'os', 'math', 'pygame.freetype']

exe = Executable(
 # what to build
   script = "knight2.py", # the name of your main python script goes here 
   initScript = None,
   base = "Win32GUI", # if creating a GUI instead of a console app, type "Win32GUI"
   targetName = "Knight vs Ninja 2.exe", # this is the name of the executable file
   copyDependentFiles = True,
   compress = True,
   appendScriptToExe = True,
   appendScriptToLibrary = True,
   icon = "art/favicon.ico" # if you want to use an icon file, specify the file name here
)

setup(
 # the actual setup & the definition of other misc. info
    name = "Knight vs Ninja 2", # program name
    version = "0.4.2",
    description = 'Knights',
    author = "Anti Otaku Prod.",
    options = {"build_exe": {"excludes":excludes,"packages":packages,
      "include_files":includefiles}},
    executables = [exe]
)