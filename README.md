# WhatsBot
simple WhatsBot using yowsup

### install [yowsup2](https://github.com/tgalal/yowsup)

```bash
pip install yowsup2
```
WhatsApp registration involves 2 steps. First you need to request a registration code. And then you resume the registration with code you got.

#### step 1

 ```bash
 yowsup-cli registration --requestcode sms --phone 49XXXXXXXX --cc 49 --mcc 123 --mnc 456
 ```
 #### step 2
 
 ```bash
 yowsup-cli registration --register 123456 --phone 49XXXXXXXX --cc 49  
 ```
 
 #### edit the `run.py` (credentials)
 
 #### Running the bot
 
```bash
python run.py
```
