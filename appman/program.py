import sources
import os


def main():
    print(os.path.dirname(os.path.abspath(os.path.join(__file__, os.pardir))))
    obsidianmd = sources.get_appman_data("obsidianmd")
    print(obsidianmd)


if __name__ == "__main__":
    main()
