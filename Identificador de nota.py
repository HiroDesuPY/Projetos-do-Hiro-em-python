#Bem Vindo ao meu programa de identificador de acordes!
#Este programa irá pedir para você inserir as notas de um acorde e, em seguida, irá identificar o nome do acorde para você e uma sequencia de notas que formam o acorde.

nota = int(input("Digite a nota do acorde (0-11, onde 0 = C, 1 = C#, 2 = D, ..., 11 = B): "))

        


while True:
    if nota < 0 or nota > 11:
        print('x' * 5, "ERRO: Nota inválida!", 'x' * 5)
        print("Nota inválida! Por favor, digite um número entre 0 e 11.")
        print('=' * 50)
        nota = int(input("Digite a nota do acorde (0-11, onde 0 = C, 1 = C#, 2 = D, ..., 11 = B): "))
    else:
        if nota == 0:
            print("O acorde é C (Dó maior) e as notas são: C, E, G")
            print("O acorde é Cm (Dó menor) e as notas são: C, D#, G")
            print("O acorde é C7 (Dó com sétima) e as notas são: C, E, G, A#")
            print("O acorde é Cm7 (Dó menor com sétima) e as notas são: C, D#, G, A#")
        elif nota == 1:
            print("O acorde é C# (Dó sustenido maior) e as notas são: C#, F, G#")
            print("O acorde é C#m (Dó sustenido menor) e as notas são: C#, E, G#")
            print("O acorde é C#7 (Dó sustenido com sétima) e as notas são: C#, F, G#, B")
            print("O acorde é C#m7 (Dó sustenido menor com sétima) e as notas são: C#, E, G#, B") 
            break
        elif nota == 2:
            print("O acorde é D (Ré maior) e as notas são: D, F#, A")
            print("O acorde é Dm (Ré menor) e as notas são: D, F, A")
            print("O acorde é D7 (Ré com sétima) e as notas são: D, F#, A, C")
            print("O acorde é Dm7 (Ré menor com sétima) e as notas são: D, F, A, C")
            break
        elif nota == 3:
            print("O acorde é D# (Ré sustenido maior) e as notas são: D#, G, A#")
            print("O acorde é D#m (Ré sustenido menor) e as notas são: D#, F#, A#")
            print("O acorde é D#7 (Ré sustenido com sétima) e as notas são: D#, G, A#, C#")
            print("O acorde é D#m7 (Ré sustenido menor com sétima) e as notas são: D#, F#, A#, C#")
            break
        elif nota == 4:
            print("O acorde é E (Mi maior) e as notas são: E, G#, B")
            print("O acorde é Em (Mi menor) e as notas são: E, G, B")
            print("O acorde é E7 (Mi com sétima) e as notas são: E, G#, B, D")
            print("O acorde é Em7 (Mi menor com sétima) e as notas são: E, G, B, D")
            break
        elif nota == 5:
            print("O acorde é F (Fá maior) e as notas são: F, A, C")
            print("O acorde é Fm (Fá menor) e as notas são: F, G#, C")
            print("O acorde é F7 (Fá com sétima) e as notas são: F, A, C, D#")
            print("O acorde é Fm7 (Fá menor com sétima) e as notas são: F, G#, C, D#")
            break
        elif nota == 6:
            print("O acorde é F# (Fá sustenido maior) e as notas são: F#, A#, C#")
            print("O acorde é F#m (Fá sustenido menor) e as notas são: F#, A, C#")
            print("O acorde é F#7 (Fá sustenido com sétima) e as notas são: F#, A#, C#, E")
            print("O acorde é F#m7 (Fá sustenido menor com sétima) e as notas são: F#, A, C#, E")
            break
        elif nota == 7:
            print("O acorde é G (Sol maior) e as notas são: G, B, D")
            print("O acorde é Gm (Sol menor) e as notas são: G, A#, D")
            print("O acorde é G7 (Sol com sétima) e as notas são: G, B, D, F")
            print("O acorde é Gm7 (Sol menor com sétima) e as notas são: G, A#, D, F")
            break
        elif nota == 8:
            print("O acorde é G# (Sol sustenido maior) e as notas são: G#, C, D#")
            print("O acorde é G#m (Sol sustenido menor) e as notas são: G#, B, D#")
            print("O acorde é G#7 (Sol sustenido com sétima) e as notas são: G#, C, D#, F#")
            print("O acorde é G#m7 (Sol sustenido menor com sétima) e as notas são: G#, B, D#, F#")
            break
        elif nota == 9:
            print("O acorde é A (Lá maior) e as notas são: A, C#, E")
            print("O acorde é Am (Lá menor) e as notas são: A, C, E")
            print("O acorde é A7 (Lá com sétima) e as notas são: A, C#, E, G")
            print("O acorde é Am7 (Lá menor com sétima) e as notas são: A, C, E, G")
            break
        elif nota == 10:
            print("O acorde é A# (Lá sustenido maior) e as notas são: A#, D, F")
            print("O acorde é A#m (Lá sustenido menor) e as notas são: A#, C#, F")
            print("O acorde é A#7 (Lá sustenido com sétima) e as notas são: A#, D, F, G#")
            print("O acorde é A#m7 (Lá sustenido menor com sétima) e as notas são: A#, C#, F, G#")
            break
        elif nota == 11:
            print("O acorde é B (Si maior) e as notas são: B, D#, F#")
            print("O acorde é Bm (Si menor) e as notas são: B, D, F#")
            print("O acorde é B7 (Si com sétima) e as notas são: B, D#, F#, A")
            print("O acorde é Bm7 (Si menor com sétima) e as notas são: B, D, F#, A")
            break
        



    
