import re


def greeting_msg():
    print('''Welcome to madlib-cli. You will be prompted to enter certain types of words.
     These words will then be used to fill in blanks of a narrative''')



def read_template(path):

    #This function will read a template madlib file
    try:
        with open(path, 'r') as file:
            content = file.read()
            return content
    except FileNotFoundError as fnf_error:
        raise fnf_error



def parse_template(string):
    '''
    This function will parse the template that was read in the read_template
    function.
    '''
    new_string = string

    parts = tuple(re.findall(r"\{(.*?)\}", new_string))
    string = re.sub(r"\{(.*?)\}", "{}", new_string)

    print(string, parts)
    return string, parts


def merge(narrative, user_input):
    """
     This function will combine user input with the given story and return it.
     """
    complete_narrative = narrative.format(*user_input)
    return complete_narrative


def main(path):
    template = read_template(path)

    string, parts = parse_template(template)

    new_parts = []

    for word in parts:
        new_word = input(f"Enter a {word}. ")
        new_parts.append(new_word)

    madlib = merge(string, new_parts)

    with open('../assets/new_file.txt', 'w') as file:
        file.write(madlib)


    print(f'Your madlib is: {madlib}')


if __name__ == '__main__':
    greeting_msg()
    path = '../assets/make_me_a_video_game_template.txt'
    main(path)