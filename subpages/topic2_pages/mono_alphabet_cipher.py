from main import mainframe
from tkinter import Label, Text, Button, Message, Frame, RAISED
from subpages import clear_screen


class Mono_alphabet_cipher:
    def mono_alphabet_cipher_page():
        clear_screen(mainframe)
    # ? Title
        Label(mainframe, text="Monoalphabet Cipher").grid(
            row=0, column=0, columnspan=3)
    # ?
    # ? Plaintext Frame
        plaintext_frame = Frame(mainframe)
        plaintext_frame.grid(row=1, column=0)
        plaintext = Label(plaintext_frame, text="Plaintext:")
        plaintext.grid(row=0, column=0, padx=10, pady=10)
        plaintext_input = Text(plaintext_frame, width=20, height=10)
        plaintext_input.grid(row=1, column=0, padx=10, pady=10)
    # ?
    # ? Ciphertext Frame
        ciphertext_frame = Frame(mainframe)
        ciphertext_frame.grid(row=1, column=2)
        ciphertext = Label(ciphertext_frame, text="Ciphertext:")
        ciphertext.grid(row=0, column=0, padx=10, pady=10)
        ciphertext_input = Text(ciphertext_frame, width=20, height=10)
        ciphertext_input.grid(row=1, column=0, padx=10, pady=10)
    # ?
    # ? Key Frame
        key_frame = Frame(mainframe)
        key_frame.grid(row=1, column=1)
        Label(key_frame, text="Plaintext Alphabet").grid(row=3, column=0)
        Label(key_frame, text="Ciphertext Alphabet").grid(row=4, column=0)

        Message(key_frame, text="ABCDEFGHIJKLMNOPQRSTUVWXYZ", relief=RAISED,
                width=260).grid(row=3, column=1, columnspan=2)
        key = Text(key_frame, width=27, height=1)
        key.grid(row=4, column=1, columnspan=2)
    # ?
    # ? Button Frame
        button_frame = Frame(mainframe)
        button_frame.grid(row=2, column=0, columnspan=3)
        Button(button_frame, text="Encrypt").grid(
            row=0, column=0, padx=10, pady=10)
        Button(button_frame, text="Decrypt").grid(
            row=0, column=1, padx=10, pady=10)
    # ?
