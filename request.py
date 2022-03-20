import requests as req


def system_node():
    pass


def system_user_ip():
    pass


def system_platform():
    pass


def system_processor():
    pass


def getScreenshot(namef='screen', typef='png'):
    pass


def delateScreenshot(namef='screen', typef='png'):
    pass


def getCpu(c='cpu'):
    pass


def closeProg():
    pass


def shutdownPc():
    pass


def rebootPc():
    pass


def sleepPc():
    pass


# def system_node():
#     systemNode = platform.node()
#     return systemNode
#
#
# def system_user_ip():
#     userIp = socket.gethostbyname(socket.gethostname())
#     return userIp
#
#
# def system_platform():
#     systemPlatform = platform.platform()
#     return systemPlatform
#
#
# def system_processor():
#     systemProcessor = platform.processor()
#     return systemProcessor
#
#
# def getScreenshot(namef='screen', typef='png'):
#     try:
#         pg.screenshot(f"{namef}.{typef}")
#     except ValueError:
#         error = 'Allowed photo types: png, jpg, jpeg'
#         return error
#
#
# def delateScreenshot(namef='screen', typef='png'):
#     path = os.path.join(os.path.abspath(os.path.dirname(__file__)), f'{namef}.{typef}')
#     os.remove(path)
#
#
# def getCpu(c='cpu'):
#     if c == 'cpu':
#         cpu = psutil.cpu_percent()
#         return cpu
#     elif c == 'help':
#         return 'I help you!!!'
#
#
# def closeProg():
#     pg.hotkey("altleft", "f4")
#
#
# def shutdownPc():
#     os.system('shutdown /s')
#
#
# def rebootPc():
#     os.system('shutdown /r')
#
#
# def sleepPc():
#     os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")
