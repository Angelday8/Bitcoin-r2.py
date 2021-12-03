from bit import *
from bit.format import bytes_to_wif
import smtplib, time, json, requests, atexit, random, codecs, sys
from rich.console import Console
gmail_user = 'youremail@gmail.com'
gmail_password = 'yourpassword'
console = Console()
console.clear()

W  = '\033[0m'  # white (normal)
R  = '\033[31m' # red
G  = '\033[32m' # green
O  = '\033[33m' # orange
B  = '\033[34m' # blue
P  = '\033[35m' # purple

my_colours = [W, R, G, O, B, P]

icons= ['⏳', 'ℹ️', '✅', '⛔️', '🔁', '🔑', '💸', '😔', '🌍', '✍️', '🚌', '👇', '📋', '📣', '🤩','😀', '😃', '😄', '😁', '😆', '😅', '😂', '🤣', '🥲', '☺️', '😊', '😇', '🙂', '🙃', '😉', '😌', '😍', '🥰', '😘', '😗', '😙', '😚', '😋', '😛', '😝', '😜', '🤪', '🤨', '🧐', '🤓', '😎', '🥸', '🤩', '🥳', '😏', '😒', '😞', '😔', '😟', '😕', '🙁', '☹️', '😣', '😖', '😫', '😩', '🥺', '😢', '😭', '😤', '😠', '😡', '🤬', '🤯', '😳', '🥵', '🥶', '😱', '😨', '😰', '😥', '😓', '🤗', '🤔', '🤭', '🤫', '🤥', '😶', '😐', '😑', '😬', '🙄', '😯', '😦', '😧', '😮', '😲', '🥱', '😴', '🤤', '😪', '😵', '🤐', '🥴', '🤢', '🤮', '🤧', '😷', '🤒', '🤕', '🤑', '🤠', '😈', '👿', '👹', '👺', '🤡', '💩', '👻', '💀', '☠️', '👽', '👾', '🤖', '🎃', '😺', '😸', '😹', '😻', '😼', '😽', '🙀', '😿', '😾', '👋', '🤚', '🖐', '✋', '🖖', '👌', '🤌', '🤏', '✌️', '🤞', '🤟', '🤘', '🤙', '👈', '👉', '👆', '🖕', '👇', '☝️', '👍', '👎', '✊', '👊', '🤛', '🤜', '👏', '🙌', '👐', '🤲', '🤝', '🙏', '✍️', '💅', '🤳', '💪', '🦾', '🦵', '🦿', '🦶', '👣', '👂', '🦻', '👃', '🫀', '🫁', '🧠', '🦷', '🦴', '👀', '👁', '👅', '👄', '💋', '🩸', '🐒', '🐔', '🐧', '🐦', '🐤', '🐣', '🐥', '🦆', '🦅', '🦉', '🦇', '🐺', '🐗', '🐴', '🦄', '🐝', '🪱', '🐛', '🦋', '🐌', '🐞', '🐜', '🪰', '🪲', '🪳', '🦟', '🦗', '🕷', '🕸', '🦂', '🐢', '🐍', '🦎', '🦖', '🦕', '🐙', '🦑', '🦐', '🦞', '🦀', '🐡', '🐠', '🐟', '🐬', '🐳', '🐋', '🦈', '🐊', '🐅', '🐆', '🦓', '🦍', '🦧', '🦣', '🐘', '🦛', '🦏', '🐪', '🐫', '🦒', '🦘', '🦬', '🐃', '🐂', '🐄', '🐎', '🐖', '🐏', '🐑', '🦙', '🐐', '🦌', '🐕', '🐩', '🦮', '🐕‍🦺', '🐈', '🐈‍⬛', '🪶', '🐓', '🦃', '🦤', '🦚', '🦜', '🦢', '🦩', '🕊', '🐇', '🦝', '🦨', '🦡', '🦫', '🦦', '🦥', '🐁', '🐀', '🐿', '🦔', '🐾', '🐉', '🐲', '🌵', '🎄', '🌲', '🌳', '🌴', '🪵', '🌱', '🌿', '☘️', '🍀', '🎍', '🪴', '🎋', '🍃', '🍂', '🍁', '🍄', '🐚', '🪨', '🌾', '💐', '🌷', '🌹', '🥀', '🌺', '🌸', '🌼', '🌻', '🌞', '🌝', '🌛', '🌜', '🌚', '🌕', '🌖', '🌗', '🌘', '🌑', '🌒', '🌓', '🌔', '🌙', '🌎', '🌍', '🌏', '🪐', '💫', '⭐️', '🌟', '✨', '⚡️', '☄️', '💥', '🔥', '🌪', '🌈', '☀️', '🌤', '⛅️', '🌥', '☁️', '🌦', '🌧', '⛈', '🌩', '🌨', '❄️', '☃️', '⛄️', '🌬', '💨', '💧', '💦', '☔️', '☂️', '🌊', '🌫', '⏰', '💰', '🎅🏻', '🎄', '🎁', '🎶']

animation = ["[■□□□□□□□□□□□□□□□□□□□]","[■□□□□□□□□□□□□□□□□□□□]","[■■□□□□□□□□□□□□□□□□□□]","[■■■□□□□□□□□□□□□□□□□□]", "[■■■■□□□□□□□□□□□□□□□□]", "[■■■■■□□□□□□□□□□□□□□□]", "[■■■■■■□□□□□□□□□□□□□□]", "[■■■■■■■□□□□□□□□□□□□□]", "[■■■■■■■■□□□□□□□□□□□□]", "[■■■■■■■■■□□□□□□□□□□□]", "[■■■■■■■■■■□□□□□□□□□□]", "[■■■■■■■■■■■□□□□□□□□□]", "[■■■■■■■■■■■■□□□□□□□□]", "[■■■■■■■■■■■■■□□□□□□□]", "[■■■■■■■■■■■■■■□□□□□□]", "[■■■■■■■■■■■■■■■□□□□□]", "[■■■■■■■■■■■■■■■■□□□□]", "[■■■■■■■■■■■■■■■■■■□□]", "[■■■■■■■■■■■■■■■■■■■□]", "[■■■■■■■■■■■■■■■■■■■■]"]

console.print(" [yellow]----------------------------------------------------[/yellow]")
console.print("[yellow]                 Starting search...[/yellow]")
console.print("[yellow]                Using So Chain API...[/yellow]")
console.print(" [yellow]----------------------------------------------------[/yellow]")
console.print("[yellow] ℹ️ Start search... Pick Range to start (Min=0 Max=256) ℹ️ [/yellow] ")
x=int(input(" ✅ Start range in BITs (Puzzle StartNumber) ✍️ -> "))
a = 2**x
y=int(input(" ⛔️ Stop range Max in BITs (Puzzle StopNumber)✍️ -> "))
b = 2**y
console.print("[purple]⏳Starting search... Please Wait ⏳[/purple]")
console.print("==========================================================")
counter = 0
total = 0
while True:       
    ran= random.randint(a,b)
    key = Key.from_int(ran)
    seed=str(ran)
    wif = bytes_to_wif(key.to_bytes(), compressed=False)
    wif1 = bytes_to_wif(key.to_bytes(), compressed=True)
    key1 = Key(wif)
    khex = key.to_hex()
    caddr = key.address #Legacy compressed address
    uaddr = key1.address #Legacy uncompressed address  
    contents1 = requests.get('https://sochain.com/api/v2/get_address_balance/BTC/' + caddr, timeout=10)
    contents2 = requests.get('https://chain.so/api/v2/get_address_balance/BTC/' + uaddr, timeout=10)
    res1 = contents1.json()
    res2 = contents2.json()
    response1 = (contents1.content)
    response2 = (contents2.content)
    balance1 = dict(res1['data'])['confirmed_balance']
    balance2 = dict(res2['data'])['confirmed_balance']
    counter += 1
    total += 2
    ammount = 0.00000000
    lol= random.choice(icons)
    lol1= random.choice(icons)
    lol2= random.choice(icons)
    lol3= random.choice(icons)
    colour = random.choice(my_colours)
    if float (balance1) > ammount or float (balance2) > ammount:
        console.print('[red] [' + str(counter) + '] ------------------------[/red]')
        console.print('[red] Total Checked [' + str(total) + '] [/red]')
        print('💸💰🤩💸💰🤩💸💰🤩💸💰🤩💸💰🤩💸💰🤩💸💰🤩💸💰🤩💸💰🤩💸💰🤩💸💰🤩💸💰🤩💸💰🤩💸💰')
        console.print('🤩 Address Compressed 🤩 : ' + caddr, ' [bold green]💸Balance💸 : ' + balance1)
        console.print('🤩 Address Uncompressed 🤩 : ' + uaddr, ' [bold green]💸Balance💸 : ' + balance2)
        print('🔑 PrivateKey (WIF) Compressed : ' + wif1)
        print('🔑 PrivateKey (WIF) UnCompressed : ' + wif)
        print('🔑 Private Key (HEX) : ' + khex)
        print('🔑 Private Key (DEC) : ' + seed)
        print('💸💰🤩💸💰🤩💸💰🤩💸💰🤩💸💰🤩💸💰🤩💸💰🤩💸💰🤩💸💰🤩💸💰🤩💸💰🤩💸💰🤩💸💰🤩💸💰')
        f=open('winner.txt','a')
        f.write('\n=====Bitcoin Address with Total Balance Ammount=====' + '\nPrivateKey (hex): ' + key.to_hex() + '\nPrivateKey (dec): ' + str(seed) + '\nBitcoin Address Compressed : ' + caddr + '  : Balance = ' + str(balance1) + '\nBitcoin Address UnCompressed :' + uaddr + '  : Balance = ' + str(balance2) + '\nPrivateKey (wif) Compressed : ' + wif1 + '\nPrivateKey (wif) UnCompressed : ' + wif + '\n =====Made by mizogg.co.uk Donations 3P7PZLbwSt2bqUMsHF9xDsaNKhafiGuWDB  =====\n')
        f.close()
        sent_from = gmail_user
        to = ['youremail@gmail.com']
        subject = 'OMG Super Important Message'
        body = '\n=====Bitcoin Address with Total Balance Ammount=====' + '\nPrivateKey (hex): ' + key.to_hex() + '\nPrivateKey (dec): ' + str(seed) + '\nBitcoin Address Compressed : ' + caddr + '  : Balance = ' + str(balance1) + '\nBitcoin Address UnCompressed :' + uaddr + '  : Balance = ' + str(balance2) + '\nPrivateKey (wif) Compressed : ' + wif1 + '\nPrivateKey (wif) UnCompressed : ' + wif + '\n =====Made by mizogg.co.uk Donations 3P7PZLbwSt2bqUMsHF9xDsaNKhafiGuWDB  =====\n'
        
        email_text = """\
            From: %s
            To: %s
            Subject: %s

            %s
            """ % (sent_from, ", ".join(to), subject, body)

        try:
            server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
            server.ehlo()
            server.login(gmail_user, gmail_password)
            server.sendmail(sent_from, to, email_text)
            server.close()
        
            print ('Email sent!')
        except:
            print ('Something went wrong...')
        
        break
    else:
        console.print('[red] [' + str(counter) + '] ------------------------[/red]')
        console.print('[red]🔁 Total Checked 👇[' + str(total) + '] [/red]')
        console.print('😔 Address Compressed   : ' + caddr, ' [red]😔Balance😔 : ' + balance1)
        console.print('😔 Address Uncompressed : ' + uaddr, ' [red]😔Balance😔 : ' + balance2)
        print('🔑 PrivateKey (WIF) Compressed : ' + wif1)
        print('🔑 PrivateKey (WIF) UnCompressed : ' + wif)
        print('🔑 Private Key (HEX) : ' + khex)
        print('🔑 Private Key (DEC) : ' + seed)
        console.print(lol, lol1, lol2, lol3, "[purple]⏳ Sleeping for 0.5 seconds... Please Wait ⏳[/purple]", lol3, lol2, lol1, lol)
        for i in range(len(animation)):
            time.sleep(0.025)
            sys.stdout.write("\r" + colour + lol + "Loading:" + animation[i % len(animation)])
            sys.stdout.flush()