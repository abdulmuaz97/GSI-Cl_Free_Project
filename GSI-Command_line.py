#! usr/bin/python2
import datetime
import platform
import socket
import webbrowser
import sys as system
import os as operating_system
from subprocess import call
import shutil
import base64
import hashlib
import getpass
WHITE = '\033[0m'
RED = '\033[31m'
GREEN = '\033[32m'
BLUE = '\033[34m'
#___________________________________________________________________
#__Author__: AbdulMuaz Aqeel ^_^
#__Job__: Security Programmer.
#__Country__: Iraq-Baghdad
#__Social__: facebook.com/AbdulMuaz.Aqeel.SSP
#--------------------------------------------------------------------
GSI = '''GSI-Cl For Security Developers Team(S.D.T) [Version 2.1] ^_^'''
commands_help = [  'base16-enc        |  Convert regular text to hash using base16...[Encoding].'
                 , 'base16-dec        |  Convert hash(base16) to regular text...[Decoding].'
                 , 'base32-enc        |  Convert regular text to hash using base32...[Encoding].'
                 , 'base32-dec        |  Convert hash(base32) to regular text...[Decoding].'
                 , 'base64-enc        |  Convert regular text to hash using base64...[Encoding].'
                 , 'base64-dec        |  Convert hash(base64) to regular text...[Decoding].'
                 , 'cd                |  Change the current directory of your work.'
                 , 'cdir              |  Set [default directory] [only directory].'
                 , 'clear             |  Clear the terminal.'
                 , 'color             |  Change work station color system.'
                 , 'copy              |  Copying a file to directory of specific path.'
                 , 'cpath             |  Set [defualt path] [full path].'
                 , 'current-path      |  Getting the current path of the program.'
                 , 'date              |  Getting the real time of your computer.'
                 , 'device-name       |  Getting the device name.'
                 , 'echo              |  Printing a regular message.'
                 , 'exit              |  Exiting the program.'
                 , 'find              |  Find a file or a directory in the current path.'
                 , 'hostname          |  Getting the hostname.'
                 , 'help              |  Help and explaining the commands.'
                 , 'is-dir            |  Checking if the path is a directory..returns True if it does.'
                 , 'is-file           |  Checking if the path is a file..returns True if it does.'
                 , 'ip-name           |  Getting the public name of your ip.'
                 , 'ls                |  Display a list with the content of the current directory with every thing.'
                 , 'md5-enc           |  Convert regular text to hash using MD5 hash...[Encoding].'
                 , 'mkdir             |  Making a directory with specific name in the current path of the program.'
                 , 'mkfile            |  Making a file in the current path and should be writable file like [ww.txt].'
                 , 'move              |  Moving a file or directory to another location or path.'
                 , 'os-name           |  Getting the operating system name.'
                 , 'path-exist        |  Check for the path if exists or not.'
                 , 'platform          |  Getting the type of your operating system.'
                 , 'processor         |  Getting the real processor of your computer.'
                 , 'read              |  Read file and should be readable file like [rr.txt].'
                 , 'rm                |  Removing a file..[Note: will not go to trash...means delete for ever].'
                 , 'rmdir             |  Removing a directory..[Note: will not go to trash...means delete for ever].'
                 , 'rename            |  Rename file or directory.'
                 , 'run               |  Run an executable file or program.'
                 , 'sha1-enc          |  Convert regular text to hash using SHA1 hash...[Encoding].'
                 , 'system-paths      |  Getting the current paths you are working now and the system.'
                 , 'time              |  Getting the current time using 24h mode.'
                 , 'url               |  Opening a specific url in new tab if possible.'
                 , 'username          |  Getting the real name of the username.'
                 , 'version           |  Getting the system version.'
                   ]

print(GSI)
print('['+RED+'+'+WHITE+'] Copyright(c)2016 Security Developers Team, Open Source Project.\n')
Target = 1
input_target = ''
now = datetime.datetime.now()
d = 'cdir'
col = 'normal'
while True:
    if d == 'cdir':
        if col == 'normal':
            __os_path__ = operating_system.path.basename(operating_system.getcwd())
            input_target = raw_input(RED+getpass.getuser()+'@'+socket.gethostname()+':~'+BLUE+
                                     str('/'+__os_path__)+WHITE+' [Target Set %s]'% Target+GREEN+'$ '+WHITE)
        elif col == 'blue':
            __os_path__ = operating_system.path.basename(operating_system.getcwd())
            input_target = raw_input(BLUE+getpass.getuser()+'@'+socket.gethostname()+':~'+
                                     str('/'+__os_path__)+' [Target Set %s]'% Target+'$ ')
        elif col == 'red':
            __os_path__ = operating_system.path.basename(operating_system.getcwd())
            input_target = raw_input(RED+getpass.getuser()+'@'+socket.gethostname()+':~'+
                                     str('/'+__os_path__)+' [Target Set %s]'% Target+'$ ')
        elif col == 'green':
            __os_path__ = operating_system.path.basename(operating_system.getcwd())
            input_target = raw_input(GREEN+getpass.getuser()+'@'+socket.gethostname()+':~'+
                                     str('/'+__os_path__)+' [Target Set %s]'% Target+'$ ')
        elif col == 'white':
            __os_path__ = operating_system.path.basename(operating_system.getcwd())
            input_target = raw_input(WHITE+getpass.getuser()+'@'+socket.gethostname()+':~'+
                                     str('/'+__os_path__)+' [Target Set %s]'% Target+'$ ')
    else:
        if col == 'normal':
            input_target = raw_input(RED+getpass.getuser()+'@'+socket.gethostname()+':~'+BLUE+
                                 str(operating_system.getcwd())+WHITE+
                                 ' [Target Set %s]'% Target+GREEN+'$ '+WHITE)
        elif col == 'blue':
            input_target = raw_input(BLUE+getpass.getuser()+'@'+socket.gethostname()+':~'+
                                 str(operating_system.getcwd())+
                                 ' [Target Set %s]'% Target+'$ ')
        elif col == 'red':
           input_target = raw_input(RED+getpass.getuser()+'@'+socket.gethostname()+':~'+
                                 str(operating_system.getcwd())+
                                 ' [Target Set %s]'% Target+'$ ')
        elif col == 'green':
            input_target = raw_input(GREEN+getpass.getuser()+'@'+socket.gethostname()+':~'+
                                 str(operating_system.getcwd())+
                                 ' [Target Set %s]'% Target+'$ ')
        elif col == 'white':
            input_target = raw_input(WHITE+getpass.getuser()+'@'+socket.gethostname()+':~'+
                                 str(operating_system.getcwd())+
                                 ' [Target Set %s]'% Target+'$ ')
    if input_target == '':
        continue
    elif input_target.startswith('cpath'):
        cpath = input_target.split()
        if cpath[0] == 'cpath':
            if len(cpath) == 1:
                d = 'cpath'
            else:
                print('Error: cpath [none]')
        else:
            print(RED+'[Error] '+WHITE+cpath[0]+' : Command not found.')
    elif input_target.startswith('cdir'):
        cdir = input_target.split()
        if cdir[0] == 'cdir':
            if len(cdir) == 1:
                d = 'cdir'
            else:
                print('Error: cdir [none]')
        else:
            print(RED+'[Error] '+WHITE+cdir[0]+' : Command not found.')
    elif input_target.startswith('exit'):
        exit_1 = input_target.split()
        if exit_1[0] == 'exit':
            if len(exit_1) == 1:
                print('Targets: %s' % Target)
                print('Exiting...'+GREEN+'OK'+WHITE)
                break
            else:
                print('Error: exit [none]')
        else:
            print(RED+'[Error] '+WHITE+exit_1[0]+' : Command not found.')
    elif input_target.startswith('help'):
        help_1 = input_target.split()
        if help_1[0] == 'help':
            if len(help_1) == 1:
                print('Commands                 Description\n-----------------------------------------------------')
                for i in range(len(commands_help)):
                     print(WHITE+'['+GREEN+'+'+WHITE+'] '+ str(commands_help[i]))
                print('\n['+RED+'+'+WHITE+'] Total: '+str(len(commands_help)))
                print('['+RED+'+'+WHITE+'] Copyright(c)2016 Security Developers Team, All Rights Reserved.')
            else:
                print('Error: help [none]')
        else:
            print(RED+'[Error] '+WHITE+help_1[0]+' : Command not found.')
    elif input_target.startswith('platform'):
        platform_1 = input_target.split()
        if platform_1[0] == 'platform':
            if len(platform_1) == 1:
                print(platform.system())
            else:
                print('Error: platform [none]')
        else:
            print(RED+'[Error] '+WHITE+platform_1[0]+' : Command not found.')
    elif input_target.startswith('version'):
        version_1 = input_target.split()
        if version_1[0] == 'version':
            if len(version_1) == 1:
                print(platform.platform())
            else:
                print('Error: version [none]')
        else:
            print(RED+'[Error] '+WHITE+version_1[0]+' : Command not found.')
    elif input_target.startswith('date'):
        date_1 = input_target.split()
        if date_1[0] == 'date':
            if len(date_1) == 1:
                print(str(now.year)+'/'+str(now.month)+'/'+str(now.day))
            else:
                print('Error: date [none]')
        else:
            print(RED+'[Error] '+WHITE+date_1[0]+' : Command not found.')
    elif input_target.startswith('time'):
        time_1 = input_target.split()
        if time_1[0] == 'time':
            if len(time_1) == 1:
                print(str(now.hour)+':'+str(now.minute)+':'+str(now.second)+'.'+str(now.microsecond))
            else:
                print('Error: time [none]')
        else:
            print(RED+'[Error] '+WHITE+time_1[0]+' : Command not found.')
    elif input_target.startswith('username'):
        username_1 = input_target.split()
        if username_1[0] == 'username':
            if len(username_1) == 1:
                print(getpass.getuser())
            else:
                print('Error: username [none]')
        else:
            print(RED+'[Error] '+WHITE+username_1[0]+' : Command not found.')
    elif input_target.startswith('processor'):
        processor_1 = input_target.split()
        if processor_1[0] == 'processor':
            if len(processor_1) == 1:
                print(platform.processor())
            else:
                print('Error: processor [none]')
        else:
            print(RED+'[Error] '+WHITE+processor_1[0]+' : Command not found.')
    elif input_target.startswith('current-path'):
        current_path_2 = input_target.split()
        if current_path_2[0] == 'current-path':
            if len(current_path_2) == 1:
                print(operating_system.getcwd())
            else:
                print('Error: current-path [none]')
        else:
            print(RED+'[Error] '+WHITE+current_path_2[0]+' : Command not found.')
    elif input_target.startswith('hostname'):
        hostname_1 = input_target.split()
        if hostname_1[0] == 'hostname':
            if len(hostname_1) == 1:
                print(socket.gethostname())
            else:
                print('Error: hostname [none]')
        else:
            print(RED+'[Error] '+WHITE+hostname_1[0]+' : Command not found.')
    elif input_target == 'url':
        url_1 = input_target.split()
        if url_1[0] == 'url':
            if len(url_1) == 2:
                webbrowser.open_new_tab(str(url_1[1]))
            else:
                print('Error: url [link address]')
        else:
            print('['+GREEN+'+'+WHITE+'] '+'url\nUsage: url [link address]\nExample: url http://www.google.com')
    elif input_target.startswith('path-exist'):
        path_exist = input_target.split()
        if path_exist[0] == 'path-exist':
            if len(path_exist) == 2:
                if operating_system.path.exists(str(path_exist[1])):
                    print('True.')
                else:
                    print('False.')
            else:
                print('['+GREEN+'+'+WHITE+'] '+'path-exist\nUsage: path-exist [path]\nExample: path-exist /usr/bin')
        else:
            print(RED+'[Error] '+WHITE+path_exist[0]+' : Command not found.')
    elif input_target.startswith('device-name'):
        device_name_1 = input_target.split()
        if device_name_1[0] == 'device-name':
            if len(device_name_1) == 1:
                print(platform.node())
            else:
                print('Error: device-name [none]')
        else:
            print(RED+'[Error] '+WHITE+device_name_1[0]+' : Command not found.')
    elif input_target.startswith('os-name'):
        os_name_1 = input_target.split()
        if os_name_1[0] == 'os-name':
            if len(os_name_1) == 1:
                print(operating_system.name)
            else:
                print('Error: os-name [none]')
        else:
            print(RED+'[Error] '+WHITE+os_name_1[0]+' : Command not found.')
    elif input_target.startswith('ip-name'):
        ip_name = input_target.split()
        if ip_name[0] == 'ip-name':
            if len(ip_name) == 2:
                try:
                    print(socket.getfqdn(str(ip_name[1])))
                except:
                    print('Error: Somthing went wrong in the ip!')
            else:
                    print('['+GREEN+'+'+WHITE+'] '+'ip-name\nUsage: ip-name [IP Address]\nExample: ip-name 127.0.0.1')
        else:
            print(RED+'[Error] '+WHITE+ip_name[0]+' : Command not found.')
    elif input_target.startswith('mkfile'):
        make_file = input_target.split()
        if make_file[0] == 'mkfile':
            if len(make_file) == 2:
                    if operating_system.path.exists(str(make_file[1])):
                        print('Error: '+str(make_file[1])+' is already exist.')
                    else:
                        create_file = open(str(make_file[1]), 'w')
            else:
                print('['+GREEN+'+'+WHITE+'] '+'mkfile >> Make file\nUsage: mkfile [filename]\nExample: mkfile Test.txt')
        else:
            print(RED+'[Error] '+WHITE+make_file[0]+' : Command not found.')
    elif input_target.startswith('read'):
        read_file = input_target.split()
        if read_file[0] == 'read':
            if len(read_file) == 2:
                try:
                    readable = open(str(read_file[1]), 'r')
                    print(readable.read())
                    readable.close()
                except (OSError, IOError, UnicodeError) as e:
                    print("Error: '"+e.filename+"' "+e.strerror+".")
            else:
                print('['+GREEN+'+'+WHITE+'] '+'read\nUsage: read [filename]\nExample: read Test.txt')
        else:
            print(RED+'[Error] '+WHITE+read_file[0]+' : Command not found.')
    elif input_target.startswith('mkdir'):
        make_dir = input_target.split()
        if make_dir[0] == 'mkdir':
            if len(make_dir) == 2:
                try:
                    current_path = operating_system.getcwd()
                    operating_system.mkdir(current_path+'/'+str(make_dir[1]))
                except (OSError, IOError) as e:
                        print("Error: '"+e.filename+"' "+e.strerror+".")
            else:
                print('['+GREEN+'+'+WHITE+'] '+'mkdir >> make directory\nUsage: mkdir [Directory name]\nExample: mkdir Test')
        else:
            print(RED+'[Error] '+WHITE+make_dir[0]+' : Command not found.')
    elif input_target.startswith('rmdir'):
        remove_dir = input_target.split()
        if remove_dir[0] == 'rmdir':
            if len(remove_dir) == 2:
                try:
                    operating_system.rmdir(str(remove_dir[1]))
                except (OSError, IOError) as e:
                        if e.errno == 39:
                            print("Error: '"+e.filename+"' "+e.strerror+".")
                            rm_anyway = str(raw_input("Remove directory and all content anyway (Y / N)? ")).upper()
                            if rm_anyway == 'N' or rm_anyway == '':
                                print('N: Canceling...Done.')
                            elif rm_anyway == 'Y':
                                print('Y: Removing all files...')
                                try:
                                    shutil.rmtree(str(remove_dir[1]))
                                except (IOError, OSError, shutil) as e:
                                    print(e.errno, e.strerror, e.filename)
                            else:
                                    print('None: Canceling...Done.')
                        else:
                            print("Error: '"+str(e.filename)+"' "+e.strerror+".")
            else:
                print('['+GREEN+'+'+WHITE+'] '+'rem-dir >> remove directory\nUsage: rem-dir [Directory name]\nExample: rem-dir Test')
        else:
            print(RED+'[Error] '+WHITE+remove_dir[0]+' : Command not found.')
    elif input_target.startswith('rm'):
        remove_file = input_target.split()
        if remove_file[0] == 'rm':
            if len(remove_file) == 2:
                if operating_system.path.exists(str(remove_file[1])):
                    if operating_system.path.isfile(str(remove_file[1])):
                        try:
                            operating_system.remove(str(remove_file[1]))
                        except OSError:
                            print('Error: Can not remove this file.')
                    else:
                        print('Error: The file you trying to remove is a directory.')
                else:
                    print('Error: File name not found.')
            else:
                print('['+GREEN+'+'+WHITE+'] '+'rem-file >> remove file\nUsage: rem-file [Filename]\nExample: rem-file Test.txt')
        else:
            print(RED+'[Error] '+WHITE+remove_file[0]+' : Command not found.')
    elif input_target.startswith('rename'):
        rename = input_target.split()
        if rename[0] == 'rename':
            if len(rename) == 3:
                if operating_system.path.exists(str(rename[1])):
                    try:
                        operating_system.renames(str(rename[1]), str(rename[2]))
                    except IOError:
                        print('Error: Something went wrong.')
                else:
                    print('Error: Old file name not exist.')
            else:
                print('['+GREEN+'+'+WHITE+'] '+'rename\nUsage: rename [Old Filename] [New Filename]\nExample: rename Test.txt NewTest.txt')
        else:
            print(RED+'[Error] '+WHITE+rename[0]+' : Command not found.')
    elif input_target.startswith('is-dir'):
        is_dir = input_target.split()
        if is_dir[0] == 'is-dir':
            if len(is_dir) == 2:
                if operating_system.path.exists(str(is_dir[1])):
                    if operating_system.path.isdir(str(is_dir[1])):
                        print('True.')
                    else:
                        print('False.')
                else:
                    print('Error: Directory name not found.')
            else:
                print('['+GREEN+'+'+WHITE+'] '+'is-file\nUsage: is-dir [Directory Name]\nExample: is-dir Test')
        else:
            print(RED+'[Error] '+WHITE+is_dir[0]+' : Command not found.')
    elif input_target.startswith('is-file'):
        is_file = input_target.split()
        if is_file[0] == 'is-file':
            if len(is_file) == 2:
                if operating_system.path.exists(str(is_file[1])):
                    if operating_system.path.isfile(str(is_file[1])):
                        print('True.')
                    else:
                        print('False.')
                else:
                    print('Error: File name not found.')
            else:
                print('['+GREEN+'+'+WHITE+'] '+'is-file\nUsage: is-file [Filename]\nExample: is-file Test.txt')
        else:
            print(RED+'[Error] '+WHITE+is_file[0]+' : Command not found.')
    elif input_target.startswith('echo'):
        echo_1 = input_target.partition('echo ')
        echo_list = list(echo_1)
        if echo_list[1] == 'echo ':
            print(echo_list[2])
        else:
            print('['+GREEN+'+'+WHITE+'] '+'echo\nUsage: echo [Message]\nExample: echo Hello world')
    elif input_target.startswith('system-paths'):
        sys_ph = input_target.split()
        if sys_ph[0] == 'system-paths':
            if len(sys_ph) == 1:
                for paths in system.path:
                    print(paths)
            else:
                print('Error: system-paths [none]')
        else:
            print('[Error] '+sys_ph[0]+' : Command not found.')
    elif input_target.startswith('cd'):
        cd = input_target.split()
        try:
            if cd[0] == 'cd':
                    try:
                        operating_system.chdir(str(cd[1]))
                    except OSError as e:
                        if e.errno == 20:
                            print("Error: '"+e.filename+"' "+e.strerror+'.')
                        elif e.errno == 2:
                            print("Error: '"+e.filename+"' "+e.strerror+'.')
                        else:
                            print('Error: Somthing went wrong.')
            else:
                print(RED+'[Error] '+WHITE+cd[0]+' : Command not found.')
        except:
            print('['+GREEN+'+'+WHITE+'] '+'cd >> Change Directory\nUsage: cd [Path]\nExample: cd /usr/bin')
    elif input_target.startswith('ls'):
        ls = input_target.split()
        if ls[0] == 'ls':
            if len(ls) == 1:
                print(GREEN)
                call(['ls', '-al'])
                print(WHITE)
            else:
                print('Error: ls [None]')
        else:
            print(RED+'[Error] '+WHITE+ls[0]+' : Command not found.')
    elif input_target.startswith('find'):
        find = input_target.split()
        if find[0] == 'find':
            if len(find) == 2:
                if str(find[1]) in operating_system.listdir(operating_system.getcwd()):
                    if operating_system.path.isdir(str(find[1])):
                        print('Found: True.')
                        print('Type: Directory.')
                        print('Name: '+str(find[1]))
                    elif operating_system.path.isfile(str(find[1])):
                        print('Found: True.')
                        print('Type: File.')
                        print('Name: '+str(find[1]))
                    else:
                        pass
                else:
                    print('Found: False.')
                    print('Type: Unknown.')
                    print('Name: '+str(find[1]))
            else:
                print('['+GREEN+'+'+WHITE+'] '+'find\nUsage: find [Filename or Directory]\nExample: find Test.txt')
        else:
            print(RED+'[Error] '+WHITE+find[0]+' : Command not found.')
    elif input_target.startswith('copy'):
        copy_1 = input_target.split()
        if copy_1[0] == 'copy':
            if len(copy_1) == 3:
                mo_1 = str(copy_1[1])
                mo_2 = str(copy_1[2])
                if operating_system.path.exists(mo_1) and operating_system.path.isfile(mo_1):
                    if operating_system.path.exists(mo_2):
                        try:
                            shutil.copy(mo_1, mo_2)
                        except IOError:
                            print('Error: Can not copy...the same file was found or somthing else.')
                    else:
                        print('Error: Path not found.')
                else:
                    print('Error: Either you trying to copy a directory or the file not found.')
            else:
                print('['+GREEN+'+'+WHITE+'] '+'copy\nUsage: copy [Filename] [Path]\nExample: copy Test.txt usr/bin')
        else:
            print(RED+'[Error] '+WHITE+copy_1[0]+' : Command not found.')
    elif input_target.startswith('clear'):
        clear = input_target.split()
        if clear[0] == 'clear':
            if len(clear) == 1:
                call('clear')
            else:
                print('Error: clear [none]')
        else:
            print(RED+'[Error] '+WHITE+clear[0]+' : Command not found.')
    elif input_target.startswith('run'):
        run = input_target.split()
        if run[0] == 'run':
            if len(run) == 2:
                try:
                    call('./'+str(run[1]))
                except (OSError, IOError, NameError, TypeError, SyntaxError, SystemError) as e:
                    print("Error: '"+str(e.filename)+"' "+str(e.strerror)+'.')
            else:
                print('['+GREEN+'+'+WHITE+'] '+'run\nUsage: run [executable_file]\nExample: run program.sh')
        else:
            print(RED+'[Error] '+WHITE+run[0]+' : Command not found.')
    elif input_target.startswith('base64-enc'):
        bs64_1 = input_target.split()
        if bs64_1[0] == 'base64-enc':
            if len(bs64_1) == 1:
                base64_enc = raw_input(GREEN+'Encode Using[Base64] $ '+WHITE)
                if base64_enc == '':
                    print('Text: Nothing!\nCanceling...Done.')
                else:
                    print('\nText Encoded: '+GREEN+base64.b64encode(str(base64_enc))+WHITE)
            else:
                print('Error: base64-enc [none]')
        else:
            print(RED+'[Error] '+WHITE+bs64_1[0]+' : Command not found.')
    elif input_target.startswith('base64-dec'):
        bs64_2 = input_target.split()
        if bs64_2[0] == 'base64-dec':
            if len(bs64_2) == 1:
                base64_enc = raw_input(GREEN+'Decode Using[Base64] $ '+WHITE)
                if base64_enc == '':
                    print('Text: Nothing!\nCanceling...Done.')
                else:
                    try:
                       print('\nHashCode Decoded: '+GREEN+base64.b64decode(str(base64_enc))+WHITE)
                    except TypeError as df:
                        print("Error: '"+df.strerror+".")
            else:
                print('Error: base64-dec [none]')
        else:
            print(RED+'[Error] '+WHITE+bs64_2[0]+' : Command not found.')
    elif input_target.startswith('base16-enc'):
        bs16_1 = input_target.split()
        if bs16_1[0] == 'base16-enc':
            if len(bs16_1) == 1:
                base16_enc = raw_input(GREEN+'Encode Using[Base16] $ '+WHITE)
                if base16_enc == '':
                    print('Text: Nothing!\nCanceling...Done.')
                else:
                    print('\nText Encoded: '+GREEN+base64.b16encode(str(base16_enc))+WHITE)
            else:
                print('Error: base16-enc [none]')
        else:
            print(RED+'[Error] '+WHITE+bs16_1[0]+' : Command not found.')
    elif input_target.startswith('base16-dec'):
        bs16_2 = input_target.split()
        if bs16_2[0] == 'base16-dec':
            if len(bs16_2) == 1:
                base16_dec = raw_input(GREEN+'Decode Using[Base16] $ '+WHITE)
                if base16_dec == '':
                    print('Text: Nothing!\nCanceling...Done.')
                else:
                    try:
                        print('\nHashCode Decoded: '+GREEN+base64.b16decode(str(base16_dec))+WHITE)
                    except TypeError:
                        print('Error: Wrong typing...check your hash code.')
            else:
                print('Error: base16-dec [none]')
        else:
            print(RED+'[Error] '+WHITE+bs16_2[0]+' : Command not found.')
    elif input_target.startswith('base32-enc'):
        bs32_1 = input_target.split()
        if bs32_1[0] == 'base32-enc':
            if len(bs32_1) == 1:
                base32_enc = raw_input(GREEN+'Encode Using[Base32] $ '+WHITE)
                if base32_enc == '':
                    print('Text: Nothing!\nCanceling...Done.')
                else:
                    print('\nText Encoded: '+GREEN+base64.b32encode(str(base32_enc))+WHITE)
            else:
                print('Error: base32-enc [none]')
        else:
            print(RED+'[Error] '+WHITE+bs32_1[0]+' : Command not found.')
    elif input_target.startswith('base32-dec'):
        bs32_2 = input_target.split()
        if bs32_2[0] == 'base32-dec':
            if len(bs32_2) == 1:
                base32_dec = raw_input(GREEN+'Decode Using[Base32] $ '+WHITE)
                if base32_dec == '':
                    print('Text: Nothing!\nCanceling...Done.')
                else:
                    try:
                        print('\nHashCode Decoded: '+GREEN+base64.b32decode(str(base32_dec))+WHITE)
                    except TypeError:
                        print('Error: Wrong typing...check your hash code.')
            else:
                print('Error: base32-dec [none]')
        else:
            print(RED+'[Error] '+WHITE+bs32_2[0]+' : Command not found.')
    elif input_target.startswith('md5-enc'):
        md5_enc = input_target.split()
        if md5_enc[0] == 'md5-enc':
            if len(md5_enc) == 1:
                text_to_md5 = raw_input(GREEN+'Encode Using[MD5] $ '+WHITE)
                if text_to_md5 == '':
                    print('Text: Nothing!\nCanceling...Done.')
                else:
                    set_md5 = hashlib.md5()
                    set_md5.update(str(text_to_md5))
                    result = set_md5.hexdigest()
                    print('\nText Encoded: '+GREEN+str(result)+WHITE)
            else:
                print('Error: md5-enc [none]')
        else:
            print(RED+'[Error] '+WHITE+md5_enc[0]+' : Command not found.')
    elif input_target.startswith('sha1-enc'):
        sha1_enc = input_target.split()
        if sha1_enc[0] == 'sha1-enc':
            if len(sha1_enc) == 1:
                text_to_sha1 = raw_input(GREEN+'Encode Using[Sha1] $ '+WHITE)
                if text_to_sha1 == '':
                    print('Text: Nothing!\nCanceling...Done.')
                else:
                    set_sha1 = hashlib.sha1()
                    set_sha1.update(str(text_to_sha1))
                    result = set_sha1.hexdigest()
                    print('\nText Encoded: '+GREEN+str(result)+WHITE)
            else:
                print('Error: sha1-enc [none]')
        else:
            print(RED+'[Error] '+WHITE+sha1_enc[0]+' : Command not found.')
    elif input_target.startswith('move'):
        move_1 = input_target.split()
        if move_1[0] == 'move':
            if len(move_1) == 3:
                try:
                    shutil.move(str(move_1[1]), str(move_1[2]))
                except (OSError, IOError, shutil) as e:
                    print("Error: '"+e.filename+"' "+e.strerror+".")
            else:
                print('['+GREEN+'+'+WHITE+'] '+'move\nUsage: move [old: file or dir] [new: file or dir]\nExample: move test.txt /usr/bin')
        else:
            print(RED+'[Error] '+WHITE+move_1[0]+' : Command not found.')
    elif input_target.startswith('color'):
        color_1 = input_target.split()
        if color_1[0] == 'color':
            if len(color_1) == 2:
                if color_1[1] == '-r' or color_1[1] == '-red':
                    col = 'red'
                elif color_1[1] == '-b' or color_1[1] == '-blue':
                    col = 'blue'
                elif color_1[1] == '-g' or color_1[1] == '-green':
                    col = 'green'
                elif color_1[1] == '-w' or color_1[1] == '-white':
                    col = 'white'
                elif color_1[1] == '-n' or color_1[1] == 'normal':
                    col = 'normal'
                else:
                    print('['+GREEN+'+'+WHITE+'] '+'color\nUsage: color [Option]...\n'
                                                   'Options are: \n'
                                                   '-b  or  -blue   : Change system to blue type.\n'
                                                   '-r  or  -red    : Change system to red type.\n'
                                                   '-g  or  -green  : Change system to green type.\n'
                                                   '-w  or  -white  : Change system to white type.\n'
                                                   '-n  or  -normal : Reset colors as normal.\n\n'
                                                   'Example: color -blue')
            else:
                print('['+GREEN+'+'+WHITE+'] '+'color\nUsage: color [Option]...\n'
                                                   'Options are: \n'
                                                   '-b  or  -blue   : Change system to blue type.\n'
                                                   '-r  or  -red    : Change system to red type.\n'
                                                   '-g  or  -green  : Change system to green type.\n'
                                                   '-w  or  -white  : Change system to white type.\n'
                                                   '-n  or  -normal : Reset colors as normal.\n\n'
                                                   'Example: color -blue')
        else:
            print(RED+'[Error] '+WHITE+color_1[0]+' : Command not found.')
    else:
            print(RED+'[Error] '+WHITE+input_target+' : Command not found.')

    Target += 1







# Done
