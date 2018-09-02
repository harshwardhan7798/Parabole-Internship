import logging
import os

#Reads and returns the list of files from a directory
def read_directory(mypath):
    current_list_of_files = []




    while True:
        for (_, _, filenames) in os.walk(mypath):
            current_list_of_files = filenames
        logging.info("Reading the directory for the list of file names")
        return current_list_of_files



from urllib import urlopen, urlencode
from re import search
import sys
def omega():
    data = urlencode({"hash":hashvalue, "decrypt":"Decrypt"})
    html = urlopen("http://md5decrypt.net/en/Sha256/", data).read()
    match = search (r'<b>[^<]*</b><br/><br/>', html)
    if match:
        print "\n\033[1;32m[+] Hash cracked by Omega:\033[1;m", match.group().split('<b>')[1][:-14]
    else:
        print "\033[1;31m[-]\033[1;m Sorry this hash is not present in our database."
def Lambda():
    html = urlopen("http://md5decrypt.net/Api/api.php?hash="+hashvalue+"&hash_type=sha256&email=deanna_abshire@proxymail.eu&code=1152464b80a61728").read()
    if len(html) > 0:
        print "\n\033[1;32m[+] Hash cracked by Lambda:\033[1;m", html
    else:
        print "\033[1;31m[-]\033[1;m Sorry this hash is not present in our database."
def beta():
    data = urlencode({"auth":"8272hgt", "hash":hashvalue, "string":"","Submit":"Submit"})
    html = urlopen("http://hashcrack.com/index.php" , data).read()
    match = search (r'<span class=hervorheb2>[^<]*</span></div></TD>', html)
    if match:
        print "\n\033[1;32m[+] Hash cracked by Beta:\033[1;m", match.group().split('hervorheb2>')[1][:-18]
    else:
        omega()
hashvalue = raw_input('\033[97mEnter your hash: \033[1;m').lower()
if len(hashvalue) == 32:
    data = urlencode({"hash":hashvalue,"submit":"Decrypt It!"})
    html = urlopen("http://md5decryption.com", data).read()
    match = search(r"Decrypted Text: </b>[^<]*</font>", html)
    if match:
        print "\n\033[1;32m[+] Hash cracked by Alpha:\033[1;m", match.group().split('b>')[1][:-7]
    else:
        data = urlencode({"md5":hashvalue,"x":"21","y":"8"})
        html = urlopen("http://md5.my-addr.com/md5_decrypt-md5_cracker_online/md5_decoder_tool.php", data).read()
        match = search (r"<span class='middle_title'>Hashed string</span>: [^<]*</div>", html)
        if match:
            print "\n\033[1;32m[+] Hash cracked by Delta:\033[1;m", match.group().split('span')[2][3:-6]
        else:
            url = "http://www.nitrxgen.net/md5db/" + hashvalue
            purl = urlopen(url).read()
            if len(purl) > 0:
                print "\n\033[1;32m[+] Hash cracked by Gamma:\033[1;m", purl
            else:
                sys.exit()
if len(hashvalue) == 40:
    beta()
if len(hashvalue) == 64

def __bool__(self):
        return self.found

    def __call__(self, row, col):
        if self:
            self.master.quit()
        distance = int(round(math.hypot(row-self.row, col-self.col)))
        self.buttons[row][col].configure(text = '{}'.format(distance), bg = 'yellow', fg = 'red')
        self.cost += 1
        if not distance:
            print('You win!  At the cost of {} sonar devices.'.format(self.cost))
            self.found = True
            
def create_knowledge_graph(contents_of_input_file, name_of_input_file):

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, format='%(asctime)s:%(levelname)s:%(message)s')

    mypath = "data//input"
    list_of_input_files = read_directory(mypath)
    logging.debug(list_of_input_files)
    for each_file in list_of_input_files:
        with open(os.path.join(mypath,each_file), "r") as f:
            file_contents = f.read()

            create_knowledge_graph(file_contents, each_file)
            # end of code