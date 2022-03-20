def helpCmd():
    return 'i help you!!!'


def timeInfoCheck():
    txt = open('settings\\timeInfo.txt')
    text = txt.read()
    txt.close()
    return text


def timeInfo(statusTime):
    if statusTime == 'True':
        txt = open('settings\\timeInfo.txt')
        text = txt.read()
        txt.close()

        if text == 'True':
            txt = open('settings\\timeInfo.txt', 'w')
            txt.write('True')
            txt.close()
            status = open('settings\\timeInfo.txt')
            f = status.read()
            txt.close()
            return f'Your status has been changed from "{text}" to "{f}"'
        elif text == 'False':
            txt = open('settings\\timeInfo.txt', 'w')
            txt.write('True')
            txt.close()
            status = open('settings\\timeInfo.txt')
            f = status.read()
            txt.close()
            return f'Your status has been changed from "{text}" to "{f}"'
        else:
            return 'If you have a problem that cannot be solved, use the reset all settings using this command ""'

    elif statusTime == 'False':
        txt = open('settings\\timeInfo.txt')
        text = txt.read()
        txt.close()

        if text == 'True':
            txt = open('settings\\timeInfo.txt', 'w')
            txt.write('False')
            txt.close()
            status = open('settings\\timeInfo.txt')
            f = status.read()
            txt.close()
            return f'Your status has been changed from "{text}" to "{f}"'
        elif text == 'False':
            txt = open('settings\\timeInfo.txt', 'w')
            txt.write('False')
            txt.close()
            status = open('settings\\timeInfo.txt')
            f = status.read()
            txt.close()
            return f'Your status has been changed from "{text}" to "{f}"'
        else:
            return 'If you have a problem that cannot be solved, use the reset all settings using this command ""'
