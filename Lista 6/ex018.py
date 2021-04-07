def shut_down(comando):
    if comando == 'yes':
        return 'Shutting down'
    elif comando == 'no':
        return 'Shutdown aborted'
    else:
        return 'Sorry'

print(shut_down('no'))