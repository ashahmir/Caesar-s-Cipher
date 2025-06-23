from art import art
alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
             'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def caesar(direction, messagep, shiftp):
    output_text = ""
    for x in messagep:
        letter = False
        for alphabet in alphabets:
            if x == alphabet:
                letter = True
        if letter:
            to_shift = alphabets.index(x)
            if direction == "encode":
                final_shift = (to_shift + shiftp) % 26
            else:
                final_shift = (to_shift - shiftp) % 26
            output_text += alphabets[final_shift]
        else:
            output_text += x
    print(f"Your {direction}d message is: {output_text}")


print(art)
game_loop = 'yes'
while game_loop != 'no':
    task = input("Do you want to 'encode' or 'decode' a message?\n").lower()
    if task != "encode" and task != "decode":
        print("Invalid input")
    else:
        message = input(f"Type in the message you want to {task}\n").lower()
        shift = int(input("Type the shift number\n"))
        caesar(task, message, shift)
        game_loop = input("Do you want to use the ancient system again?\n").lower()
        while game_loop != "yes" and game_loop != "no":
            game_loop = input("Enter Correctly Please.\nDo you want to use the ancient system again?\n").lower()
