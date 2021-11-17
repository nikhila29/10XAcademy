def remove_first_alphabet(alpha):
    for i in range(len(alpha)):
        alpha[i]=alpha[i][1:]
    return alpha



            




if __name__ == "__main__":
    alpha = [i for i in input().split(' ')]
    removed_list = remove_first_alphabet(alpha)
    [print(i) for i in removed_list]