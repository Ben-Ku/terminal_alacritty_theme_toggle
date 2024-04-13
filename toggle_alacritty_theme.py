
import os
from os.path import expanduser
HOME_PATH = expanduser("~")



# NOTE: we assume that the first line of the alacritty_config contains the import
# and that the current theme will exist in the THEMES variable defined below

ALACRITTY_CONFIG_PATH = f"{HOME_PATH}/.config/alacritty/alacritty.toml"
THEMES = [
    f"{HOME_PATH}/.config/alacritty/themes/themes/solarized_dark.toml",
    f"{HOME_PATH}/.config/alacritty/themes/themes/solarized_light.toml"
]
OUR_FILE_PATH = os.getcwd() + __file__


def main():
    try:
        with open(ALACRITTY_CONFIG_PATH, 'r') as file:
            lines = file.read().splitlines()

            line = lines[0]
            if "import" in line:
                a = line.find('[') + 2
                b = line.find(']')-1
                current_theme = line[a:b]

                n = len(THEMES)
                for i in range(n):
                    if current_theme == THEMES[i]:

                        new_theme = THEMES[(i+1) % n]
                        new_line = line[:a] + new_theme + line[b:]
                        lines[0] = new_line

                        with open(ALACRITTY_CONFIG_PATH , 'w') as file:
                            for line in lines:
                                file.write(line)
                                file.write("\n")
                        exit(0)
                print(f"could not switch theme in {OUR_FILE_PATH }")
    except Exception as e:
        print(f"something failed in {OUR_FILE_PATH }")
        print(e)


if __name__ == "__main__":
    main()
