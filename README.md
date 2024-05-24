# ScrapyPriceMonitoring

To run web scraping and generate data.jsonl file(being on src folder):
```bash
scrapy crawl mercadolivre -o ../data/data.jsonl
```

To run the data processing(pandas script) and generate quotes.db file(being on src folder):
```bash
python transform/main.py
```
