import glob
import json
from datetime import datetime


def do_merge():
    merged = []
    for infile in glob.glob("data/*.json"):
        with open(infile, 'r') as infp:
            data = json.load(infp)
            merged.extend(data)
    with open(f"merged/merged_{datetime.now()}.json", 'w', encoding="utf-8") as outfp:
        json.dump(merged, outfp, indent=4, ensure_ascii=False)

    print(f"Смерджено {len(merged)} постов")


if __name__ == '__main__':
    do_merge()