import os
from matplotlib import pyplot as plt

with open("eextFile.txt", "rb") as file:
    text_string = file.read()
    text_lines = text_string.splitlines()
    

e = 0
frequency = {}
lines = len(text_lines)

def count_alpha(line):
    text_test = (str(line))
    text_test = text_test.lower()
    i = 0
    alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    while i <= 25:
        letter = alphabet[i]
        if letter == 'a':
            frequency_a.append(text_test.count(letter))
        if letter == 'b':
            frequency_b.append(text_test.count(letter))
        if letter == 'c':
            frequency_c.append(text_test.count(letter))
        if letter == 'd':
            frequency_d.append(text_test.count(letter))
        if letter == 'e':
            frequency_e.append(text_test.count(letter))
        if letter == 'f':
            frequency_f.append(text_test.count(letter))
        if letter == 'g':
            frequency_g.append(text_test.count(letter))
        if letter == 'h':
            frequency_h.append(text_test.count(letter))
        if letter == 'i':
            frequency_i.append(text_test.count(letter))
        if letter == 'j':
            frequency_j.append(text_test.count(letter))
        if letter == 'k':
            frequency_k.append(text_test.count(letter))
        if letter == 'l':
            frequency_l.append(text_test.count(letter))
        if letter == 'm':
            frequency_m.append(text_test.count(letter))
        if letter == 'n':
            frequency_n.append(text_test.count(letter))
        if letter == 'o':
            frequency_o.append(text_test.count(letter))
        if letter == 'p':
            frequency_p.append(text_test.count(letter))
        if letter == 'q':
            frequency_q.append(text_test.count(letter))
        if letter == 'r':
            frequency_r.append(text_test.count(letter))
        if letter == 's':
            frequency_s.append(text_test.count(letter))
        if letter == 't':
            frequency_t.append(text_test.count(letter))
        if letter == 'u':
            frequency_u.append(text_test.count(letter))
        if letter == 'v':
            frequency_v.append(text_test.count(letter))
        if letter == 'w':
            frequency_w.append(text_test.count(letter))
        if letter == 'x':
            frequency_x.append(text_test.count(letter))
        if letter == 'y':
            frequency_y.append(text_test.count(letter))
        if letter == 'z':
            frequency_z.append(text_test.count(letter))
            
        i = i + 1

def create_hist():
    figure, ax = plt.subplots()
    ax.plot(frequency_a, color='black')
    ax.plot(frequency_b, color='black')
    ax.plot(frequency_c, color='black')
    ax.plot(frequency_d, color='black')
    ax.plot(frequency_e, color='black')
    ax.plot(frequency_f, color='black')
    ax.plot(frequency_g, color='black')
    ax.plot(frequency_h, color='black')
    ax.plot(frequency_i, color='black')
    ax.plot(frequency_j, color='black')
    ax.plot(frequency_k, color='black')
    ax.plot(frequency_l, color='black')
    ax.plot(frequency_m, color='black')
    ax.plot(frequency_n, color='black')
    ax.plot(frequency_o, color='black')
    ax.plot(frequency_p, color='black')
    ax.plot(frequency_q, color='black')
    ax.plot(frequency_r, color='black')
    ax.plot(frequency_s, color='black')
    ax.plot(frequency_t, color='black')
    ax.plot(frequency_u, color='black')
    ax.plot(frequency_v, color='black')
    ax.plot(frequency_w, color='black')
    ax.plot(frequency_x, color='black')
    ax.plot(frequency_y, color='black')
    ax.plot(frequency_z, color='black')

    plt.xlabel("Lines")
    plt.ylabel("Frequency")
    plt.title('Letter frequency histogram')
    plt.show()


while e < len(text_lines):
    line = text_lines[e]
    count_alpha(line)
    e = e + 1
    
create_hist()