from get_data import get_raw_news
import datetime 

str_format = "%d-%m-%Y"

def get_last_update(path):
    last_update = datetime.datetime.now()
    try:
        with open(path, 'r') as f:
            last_update = datetime.datetime.strptime(f.read().strip(), str_format)
    except:
        pass
    save_last_update(path)
    return last_update

def save_last_update(path):
    now = datetime.datetime.now()
    with open(path, 'w') as f:
        print(now.strftime(str_format), file=f)

def get_all_new(last_update_path):
    last_update = get_last_update(last_update_path)

    dt = datetime.timedelta(days=1)

    data = []

    now = datetime.datetime.now()
    while last_update <= now:
#        print('update:', last_update)
        tmp = get_raw_news(last_update).split('\n')[:-1]
        data += tmp
        last_update += dt

    def parse(raw):
        raw = raw.split('|')
        date_format = '%Y-%m-%d %H:%M:%S'
        try:
            out = {
                'file': raw[0],
                'do': raw[1],
                'timestamp': datetime.datetime.strptime(raw[2], date_format),
                'title': raw[3],
                'author': raw[4],
                'annot': raw[7],
                'update': raw[10]
            }
        except:
            out = None
        return out
    out = []
    for line in data:
        x = parse(line)
        if x:
            out.append(x)
    
    return out
