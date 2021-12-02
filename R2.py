from bit import *
from bit.format import bytes_to_wif
import smtplib, random, codecs
from rich.console import Console
gmail_user = 'youremail@gmail.com'
gmail_password = 'yourpassword'
console = Console()
console.clear()
icons= ['⏳', 'ℹ️', '✅', '⛔️', '🔁', '🔑', '💸', '😔', '🌍', '✍️', '🚌', '👇', '📋', '📣', '🤩','😀', '😃', '😄', '😁', '😆', '😅', '😂', '🤣', '🥲', '☺️', '😊', '😇', '🙂', '🙃', '😉', '😌', '😍', '🥰', '😘', '😗', '😙', '😚', '😋', '😛', '😝', '😜', '🤪', '🤨', '🧐', '🤓', '😎', '🥸', '🤩', '🥳', '😏', '😒', '😞', '😔', '😟', '😕', '🙁', '☹️', '😣', '😖', '😫', '😩', '🥺', '😢', '😭', '😤', '😠', '😡', '🤬', '🤯', '😳', '🥵', '🥶', '😱', '😨', '😰', '😥', '😓', '🤗', '🤔', '🤭', '🤫', '🤥', '😶', '😐', '😑', '😬', '🙄', '😯', '😦', '😧', '😮', '😲', '🥱', '😴', '🤤', '😪', '😵', '🤐', '🥴', '🤢', '🤮', '🤧', '😷', '🤒', '🤕', '🤑', '🤠', '😈', '👿', '👹', '👺', '🤡', '💩', '👻', '💀', '☠️', '👽', '👾', '🤖', '🎃', '😺', '😸', '😹', '😻', '😼', '😽', '🙀', '😿', '😾', '👋', '🤚', '🖐', '✋', '🖖', '👌', '🤌', '🤏', '✌️', '🤞', '🤟', '🤘', '🤙', '👈', '👉', '👆', '🖕', '👇', '☝️', '👍', '👎', '✊', '👊', '🤛', '🤜', '👏', '🙌', '👐', '🤲', '🤝', '🙏', '✍️', '💅', '🤳', '💪', '🦾', '🦵', '🦿', '🦶', '👣', '👂', '🦻', '👃', '🫀', '🫁', '🧠', '🦷', '🦴', '👀', '👁', '👅', '👄', '💋', '🩸', '🐒', '🐔', '🐧', '🐦', '🐤', '🐣', '🐥', '🦆', '🦅', '🦉', '🦇', '🐺', '🐗', '🐴', '🦄', '🐝', '🪱', '🐛', '🦋', '🐌', '🐞', '🐜', '🪰', '🪲', '🪳', '🦟', '🦗', '🕷', '🕸', '🦂', '🐢', '🐍', '🦎', '🦖', '🦕', '🐙', '🦑', '🦐', '🦞', '🦀', '🐡', '🐠', '🐟', '🐬', '🐳', '🐋', '🦈', '🐊', '🐅', '🐆', '🦓', '🦍', '🦧', '🦣', '🐘', '🦛', '🦏', '🐪', '🐫', '🦒', '🦘', '🦬', '🐃', '🐂', '🐄', '🐎', '🐖', '🐏', '🐑', '🦙', '🐐', '🦌', '🐕', '🐩', '🦮', '🐕‍🦺', '🐈', '🐈‍⬛', '🪶', '🐓', '🦃', '🦤', '🦚', '🦜', '🦢', '🦩', '🕊', '🐇', '🦝', '🦨', '🦡', '🦫', '🦦', '🦥', '🐁', '🐀', '🐿', '🦔', '🐾', '🐉', '🐲', '🌵', '🎄', '🌲', '🌳', '🌴', '🪵', '🌱', '🌿', '☘️', '🍀', '🎍', '🪴', '🎋', '🍃', '🍂', '🍁', '🍄', '🐚', '🪨', '🌾', '💐', '🌷', '🌹', '🥀', '🌺', '🌸', '🌼', '🌻', '🌞', '🌝', '🌛', '🌜', '🌚', '🌕', '🌖', '🌗', '🌘', '🌑', '🌒', '🌓', '🌔', '🌙', '🌎', '🌍', '🌏', '🪐', '💫', '⭐️', '🌟', '✨', '⚡️', '☄️', '💥', '🔥', '🌪', '🌈', '☀️', '🌤', '⛅️', '🌥', '☁️', '🌦', '🌧', '⛈', '🌩', '🌨', '❄️', '☃️', '⛄️', '🌬', '💨', '💧', '💦', '☔️', '☂️', '🌊', '🌫']
console.print(" [yellow]----------------------------------------------------[/yellow]")
console.print("[yellow]                 Starting search...[/yellow]")
console.print("[yellow]                Using BIT API...[/yellow]")
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
    lol= random.choice(icons)
    lol1= random.choice(icons)
    lol2= random.choice(icons)
    lol3= random.choice(icons)
    lol4= random.choice(icons)
    lol5= random.choice(icons)
    lol6= random.choice(icons)
    lol7= random.choice(icons)
    counter+=1
    total+=2
    ran=random.randrange(a,b)
    key = Key.from_int(ran)
    seed=str(ran)
    wif = bytes_to_wif(key.to_bytes(), compressed=False) # Uncompressed WIF
    wif1 = bytes_to_wif(key.to_bytes(), compressed=True) # Compressed WIF
    key1 = Key(wif)
    caddr = key.address #Legacy compressed address
    uaddr = key1.address #Legacy uncompressed address
    contents = key.get_balance('btc')
    contents2 = key1.get_balance('btc')
    
    if float (contents) or float (contents2) > 0:
        print('💸🤩💸🤩💸🤩💸🤩💸🤩💸🤩💸🤩💸🤩💸🤩💸🤩💸🤩💸🤩💸🤩💸🤩💸🤩💸🤩💸🤩💸🤩💸🤩💸🤩💸🤩💸🤩')
        console.print('[red] [' + str(counter) + '] ------------------------[/red]')
        console.print('[red]🔁 Total Checked 👇[' + str(total) + '] [/red]')
        console.print('🤩Address Compressed  🤩: ', caddr, ' [bold green]💸Balance💸: ' + contents2)
        console.print('🤩Address Uncompressed🤩: ', uaddr, ' [bold green]💸Balance💸: ' + contents)
        print('🔑 PrivateKey (WIF) Compressed   : ' + wif1)
        print('🔑 PrivateKey (WIF) UnCompressed : ' + wif)
        print('🔑 Private Key (HEX) : ' + key.to_hex())
        print('🔑 Private Key (DEC) : ' + seed)
        print('💸🤩💸🤩💸🤩💸🤩💸🤩💸🤩💸🤩💸🤩💸🤩💸🤩💸🤩💸🤩💸🤩💸🤩💸🤩💸🤩💸🤩💸🤩💸🤩💸🤩💸🤩💸🤩')
        print('\nMatch Found')
        f=open(u"winner.txt","a")
        f.write('\nPrivateKey (hex): ' + key.to_hex())
        f.write('\nPrivateKey (dec): ' + seed)
        f.write('\nBitcoin Compressed Address : ' + caddr + ' Balance : ' + contents2)
        f.write('\nBitcoin Uncompressed Address : ' + uaddr + ' Balance : ' + contents)
        f.write('\nPrivateKey (wif)UnCompressed : ' + wif)
        f.write('\nPrivateKey (wif)Compressed : ' + wif1)
        f.write('\n =====Made by mizogg.co.uk Donations 3P7PZLbwSt2bqUMsHF9xDsaNKhafiGuWDB =====' ) 
        f.close()
        sent_from = gmail_user
        to = ['youremail@gmail.com']
        subject = ['OMG Super Important Message']
        body = '\nPrivateKey (dec): ' + seed + '\nPrivateKey (hex): ' + key.to_hex() + '\nBitcoin Address Compressed : ' + caddr + ' : Balance : ' + contents2 +'\nBitcoin Address UnCompressed :' + uaddr + ' Balance : ' + contents + '\nPrivateKey (wif) Compressed : ' + wif1 + '\nPrivateKey (wif) UnCompressed : ' + wif +'\n =====Made by mizogg.co.uk Donations 3P7PZLbwSt2bqUMsHF9xDsaNKhafiGuWDB =====\n'
        
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
            print('Something went wrong...')
            break
               
    else: 
        console.print('[red] [' + str(counter) + '] ------------------------[/red]')
        console.print('[red]🔁 Total Checked 👇[' + str(total) + '] [/red]')
        console.print('😔 Address Compressed  : ', caddr, ' [red]😔Balance😔 : ' + contents2)
        console.print('😔Address Uncompressed : ', uaddr, ' [red]😔Balance😔 : ' + contents)
        print('🔑 PrivateKey (WIF) Compressed : ' + wif1)
        print('🔑 PrivateKey (WIF) UnCompressed : ' + wif)
        print('🔑 Private Key (HEX) : ' + key.to_hex())
        print('🔑 Private Key (DEC) : ' + seed)
        console.print(lol, lol1, lol2, lol3, lol4, lol5, lol6, lol7, "[purple]🤞 Good Luck Happy Hunting 🤗[/purple]", lol7, lol6, lol5, lol4, lol3, lol2, lol1, lol)
