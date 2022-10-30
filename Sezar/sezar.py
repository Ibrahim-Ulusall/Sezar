import os
import time
import optparse

"""
    Sezar Algorithm
    Created By: İbrahim Ulusal
    Created Date : 30-10-2022 00:27 Sunday

"""
class Color:
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    WHITE = '\033[37m'
    BG_RED = '\033[41m'
    BOLD_TEXT = '\033[1m'
    NORMAL_TEXT = ['\0330m']
class Sezar:

    tr_alpabet = ['a','b','c','ç','d','e','f','g','ğ','h','ı','i','j','k','l','m','n','o','ö','p','r','s','ş','t','u','ü','v','y','z']
    en_alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','r','s','t','u','v','y','z','w','x']

    def __init__(self) -> None:
            
        self.parser = optparse.OptionParser()
        self.color = Color()
        self.config_parser()
    def Get_User_Inputs(self):
        self.parser.add_option('-e',"--encrypt",dest="encryption",help="Password Encryption")
        self.parser.add_option('-d','--decrypt',dest='decryption',help="Password Decryption")
        self.parser.add_option('-k','--key',dest='key',help="Encryption or Decryption Key")
        self.parser.add_option('--file-encryption',dest='fileEncryption',help="File Password Encryption")
        self.parser.add_option('--file-decryption',dest='fileDecryption',help="File Password Decryption")
        self.parser.add_option('-l','--language',dest='language',help="Encrypt or Decrypt Password Language (Requeried!!!)")
        self.parser.add_option('-v','--verbose',dest='verbose',help='Verbose')
        self.parser.add_option('-o','--output',dest='output',help='Txt format Writer')
        return self.parser.parse_args()

    def config_parser(self):
        help_format = """usage : sezar.py [options]\n\npython3 sezar.py -l 'language['tr or en]' -k [key<int>] -e or -d '[message]'"""
        (user_inputs,arguments) = self.Get_User_Inputs()
        self.encryption = user_inputs.encryption
        self.decryption = user_inputs.decryption
        self.file_encryption = user_inputs.fileEncryption
        self.file_decryption = user_inputs.fileDecryption
        self.language = user_inputs.language
        self.key = user_inputs.key
        self.output = user_inputs.output
        self.verbose = user_inputs.verbose
    def password(self,format,message,key):
        """
            format: e [Encrypt]
                    d [Decrypt]
        """
        if format == 'e':
            encryption_message = ''
            self.key = key
            try:
                for m in message:
                    if self.language == 'tr' or self.language == 'TR':
                        if m not in Sezar.tr_alpabet:
                            encryption_message += m
                        else:
                            encryption_message += Sezar.tr_alpabet[(Sezar.tr_alpabet.index(m)+int(self.key)) % len(Sezar.tr_alpabet)]

                    elif self.language == 'en' or self.language == 'EN':
                        if m not in Sezar.en_alphabet:
                            encryption_message += m
                        else:
                            encryption_message += Sezar.en_alphabet[(Sezar.en_alphabet.index(m) + int(self.key) ) % len(Sezar.en_alphabet)]
                    else:
                        self.errorBox('Language Not in System')

            except KeyboardInterrupt:
                self.errorBox(error_message='[ CTRL + C ] Detected!',error_format='w')
            except Exception as e:
                self.errorBox(e)
            return encryption_message
        else:
            dec_message = ''
            self.key = key
            try:
                for d in message:
                    if self.language == 'tr' or self.language == 'TR':
                        if d not in Sezar.tr_alpabet:
                            dec_message += d
                        else:
                            dec_message += Sezar.tr_alpabet[(Sezar.tr_alpabet.index(d) - int(self.key)) % len(Sezar.tr_alpabet)]

                    elif self.language == 'en' or self.language == 'EN':
                        if d not in Sezar.en_alphabet:
                            dec_message += d
                        else:
                            dec_message += Sezar.en_alphabet[(Sezar.en_alphabet.index(d) - int(self.key) ) % len(Sezar.en_alphabet)]
                    else:
                        self.errorBox('Language Not in System')

            except KeyboardInterrupt:
                self.errorBox(error_message='[ CTRL + C ] Detected!',error_format='w')
            except Exception as e:
                self.errorBox(e)
            return dec_message
        
    def Encryption(self):
        if self.encryption is not None:
            return self.password(format='e',message=self.encryption,key=self.key)
        return None
    
    def Decryption(self):
        if self.decryption is not None:  
            return self.password(format='d',message=self.decryption,key=self.key)
        return None
    
    def fileEncryption(self):
        enc_list = []
        if self.file_encryption is not None:
            if os.path.isfile(self.file_encryption):
                file_name = self.file_encryption.split('/')[-1]
                with open(file_name,mode='r',encoding='utf-8') as file_enc:
                    content = file_enc.readlines()
                    for i in content:
                        enc_list.append(i.replace('\n',''))
                    print("  "+ '-' *50 )
                    print('  | Password'+' '*17+ '| Encrypt'+' '*13 + '|')
                    print('  '+ '-'*50)
                    for e in enc_list:
                        print(f'  | {e.upper()}'+ " "*(25-len(e)) +": "+ self.color.BOLD_TEXT + self.color.GREEN+self.password(format='e',message=e,key=self.key) +self.color.WHITE+ " "*(20 - len(e)) + "|")
                        self.writer_file(format='e',file_name=self.output,content=self.password(format='e',message=e,key=self.key))
                    print("  "+'-' * 50)

        return None    

    def fileDecryption(self):
        dec_list = []
        if self.file_decryption is not None:
            if os.path.isfile(self.file_decryption):
                file_name = self.file_decryption.split('/')[-1]
                with open(file_name,mode='r',encoding='utf-8') as file_dec:
                    content = file_dec.readlines()
                    for i in content:
                        dec_list.append(i.replace('\n',''))
                    print("  "+ '-' *50 )
                    print('  | Password'+' '*17+ '| Decrypt'+' '*13 + '|')
                    print('  '+ '-'*50)
                    for e in dec_list:
                        print(f'  | {e.upper()}'+ " "*(25-len(e)) +": "+ self.color.BOLD_TEXT + self.color.GREEN+self.password(format='d',message=e,key=self.key) +self.color.WHITE+ " "*(20 - len(e)) + "|")
                    print("  "+'-' * 50)

        return None    


    def writer_file(self,file_name,format,content):
        if format == 'e':
            if os.path.isdir('enclog'):
                os.chdir('enclog')
                with open(file_name,mode='a+',encoding='utf-8') as en_file:
                    for text in content:
                        en_file.writelines(text)
            else:
                os.mkdir('enclog')
                os.chdir('enclog')
                with open(file_name,mode='w',encoding='utf-8') as en_file:
                    for text in content:
                        en_file.writelines(text)
        else:
            if os.path.isdir('declog'):
                os.chdir('declog')
                with open(file_name,mode='w',encoding='utf-8') as dec_file:
                    for text in content:
                        dec_file.writelines(text)
            else:
                os.mkdir('declog')
                os.chdir('enclog')
                with open(file_name,mode='w',encoding='utf-8') as dec_file:
                    for text in content:
                        dec_file.writelines(text)
    def clearTerminal(self):
        if os.name == 'nt':
            os.system('cls')
        elif os.name == 'posix':
            os.system('clear')
        else:
            pass
    def errorBox(self,error_message,error_format='c'):
        """
            Error Format
            default : c
            -w : Warning
            -c : Critical        
        """
        error_format.lower()
        # self.clearTerminal()
        if error_format == 'w':
            print(f'{self.color.YELLOW + self.color.BOLD_TEXT } {error_message}')
        else:
            print(f'{self.color.BG_RED + self.color.BOLD_TEXT} {error_message}')

if __name__ == '__main__':
    sezar = Sezar()
    enc = sezar.Encryption()
    dec = sezar.Decryption()
    file_enc = sezar.fileEncryption()
    file_dec = sezar.fileDecryption()
    if enc != None:
        print('Encryption : '+ enc)
    if dec != None:
        print('Decryption: ' + dec)
       
