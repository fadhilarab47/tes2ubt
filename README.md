<p align="center">

<img src="https://telegra.ph//file/75acabea0a9cc6679c2d4.jpg">

</p>

## Multi Client Fix


## Deploy on Heroku
<h3 align="center">Click The Button</h3>
<a href="https://dashboard.heroku.com/new?template=https://github.com/naya1503/Naya-Pyro"><img src="https://www.herokucdn.com/deploy/button.svg"></a>
</div>

## Deploy On VPS
```
$ apt-get update -y && apt-get upgrade -y
$ git clone https://github.com/naya1503/Naya-Pyro && cd Naya-Pyro
$ pip3 install -r req*
## ISI VARS API_ID, API_HASH, BOT_TOKEN, SESSION1, DAN OPENAI_API JIKA PERLU DENGAN CARA : ##
$ nano .env
## KALAU SUDAH SAVE DENGAN MENEKAN CTRL + S LALU CTRL + X ##
$ screen -S naya
$ bash start.sh
## DETACH SCREEN CTRL + A LALU CTRL + D ###
```

## Deploy Via Docker
```
$ apt install docker-ce docker-ce-cli containerd.io
$ systemctl start docker && systemctl enable docker
$ git clone https://github.com/naya1503/Naya-Pyro && cd Naya-Pyro
## ISI VARS API_ID, API_HASH, BOT_TOKEN, SESSION1, DAN OPENAI_API JIKA PERLU DENGAN CARA : ##
$ nano .env
## KALAU SUDAH SAVE DENGAN MENEKAN CTRL + S LALU CTRL + X ##
$ docker build . -t naya
$ docker run --name naya --env-file .env naya
## CLOSE VPS ###

## Thanks to 💖

- [Zaid](https://github.com/ITZ-ZAID)

- [OnlyMeriz](https://github.com/Onlymeriz)

- [Team Tiger](https://github.com/TeamTiger)

- [Tomi Setiawan](https://github.com/XtomiX)

- [Geez-Pyro](https://github.com/hitoizzy)

## Credit 💖

- Zaid Userbot

- Ayra X Userbot

- Team Tiger X

- Tomi Setiawan

- Xtsea


- Geez-Pyro