# blockThread

This python program makes use of the [LunarCRUSH API](https://lunarcrush.com/developers/docs) and [Messari API](https://messari.io/api) to show data about different crypto-currencies, like tweets by influencer\[s\], market changes in a currency using a graph based solution and currently best performing currency. 

## Usage

```bash
git clone https://github.com/equiknoxx/blockThread
cd blockThread
chmod +x crypto-news.py
python3 -m pip install -r requirements.txt
./crypto-news.py -h
```

### Example usage
```bash
./crypto-news.py -d feeds --key YourLunarAPIKey --sources twitter -s doge
```
```bash
./crypto-news.py -d price-ticker -s doge
```

## ToDo
+ ~~Ability to specify time interval for the price ticker(Currrently shows the last 30 days changes)
+ Store api key in a file
+ Add more functionality
+ Better documentation
