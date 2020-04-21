from timer import Timer
from reader import feed

def main():
    """Print the latest tutorial from Real Python"""
    t = Timer()
    t.start()
    tutorial = feed.get_article(0)
    t.stop()

    print(tutorial)

if __name == "__main__":
    main()
