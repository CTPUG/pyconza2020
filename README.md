# PyConZA 2020 Conference Website

Based on [wafer](https://github.com/CTPUG/wafer).

# Running

1. Run `pip install -r requirements.txt`.
1. Create a `localsettings.py` containing secrets and database credentials.
1. Run `npm install`.
1. Run `./manage.py collectstatic`.
1. Run `./manage.py migrate`.
1. Run `./manage.py createcachetable wafer_cache_table`.
1. Run `./manage.py runserver`.
