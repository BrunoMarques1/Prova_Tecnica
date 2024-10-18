texto = 'Lorem ipsum dolor sit amet. Non beatae magni eos minima exercitationem quo accusantium eius quo nihil autem et quos esse. Eos quidem molestias eum laboriosam corrupti et laborum eveniet id necessitatibus eligendi eum culpa consectetur et perspiciatis architecto. Et fugit odio cum nihil repellendus est galisum labore et praesentium labore qui laudantium sint. Rem nulla soluta sed quis minima ut harum dolorum ex aperiam reprehenderit non dolorum saepe 33 vitae harum non atque adipisci.'
#texto = 'aaAddd'
def contar_A(t):
    letras = []
    quantidade_A = 0
    for i in t:
        letras.append(i.lower())
    
    for i in letras:
        if i == 'a':
            quantidade_A += 1

    print(quantidade_A)



contar_A(texto)