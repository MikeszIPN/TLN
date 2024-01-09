from posixpath import split
import re
import random
from unidecode import unidecode
import unicodedata

def remove_accents(text):
    return ''.join(c for c in unicodedata.normalize('NFD', text)
                   if unicodedata.category(c) != 'Mn')

def get_response(user_input, already_ask, genero, user_options):
  user_input = remove_accents(user_input.lower())
  user_input = re.sub(r'[,:;.?!-_]', '', user_input)
  split_message = re.split(r'\s|[,:;.?!-_]\s', user_input)

  #print(split_message)
  response = check_all_messages(split_message, already_ask, genero, user_options)
  return response

def message_probability(user_message, recognized_words, single_response=False, required_word=[]):
  #
  matches = ''
  message_certainty = 0
  has_required_words = True

  for word in user_message:
    if word in recognized_words:
      #
      #matches = word
      message_certainty += 1

  percentage = float(message_certainty) / float(len(recognized_words))

  for word in required_word:
    if word not in user_message:
      has_required_words = False
      break

  if has_required_words or single_response:
    #
    return int(percentage * 100)
  else:
    return 0

peliculas_por_categoria = {
    'accion': ['Misión Imposible', 'Alien vs Depredador', 'Guerra de los Mundos', 'Los Vengadores', 'El Robo Maestro', 'Nacido para Matar', 'Top Gun', 'Interstellar', 'Rápidos y Furiosos'],
    'aventura': ['Titanic', 'Star Wars', 'El Diario de una Princesa', 'Los Vengadores', 'Maze Runner', 'Los Juegos del Hambre', 'Mi Pobre Angelito', 'Rápidos y Furiosos'],
    'comedia': ['Son Como Niños', 'Quieren Volverme Loco', 'Mi Pobre Angelito', 'Rápidos y Furiosos', 'El Diario de una Princesa', 'El Robo Maestro'],
    'drama': ['Titanic', 'El Diario de una Princesa', 'Nacido para Matar', 'Interstellar', 'Mi Pobre Angelito', 'Coraline'],
    'ciencia ficcion': ['Star Wars', 'Alien vs Depredador', 'Guerra de los Mundos', 'Interstellar', 'Maze Runner', 'Los Juegos del Hambre'],
    'fantasia': ['Star Wars', 'El Diario de una Princesa', 'Alien vs Depredador', 'Coraline', 'Maze Runner', 'Los Juegos del Hambre'],
    'terror': ['Alien vs Depredador', 'La Monja', 'Coraline', 'Maze Runner'],
    'misterio': ['El Robo Maestro', 'Coraline', 'Maze Runner'],
    'romance': ['Titanic', 'El Diario de una Princesa', 'Barbie'],
    'romanticas': ['Titanic', 'El Diario de una Princesa', 'Barbie'],
    'thriller': ['Misión Imposible', 'Alien vs Depredador', 'El Robo Maestro', 'Nacido para Matar', 'Guerra de los Mundos', 'Maze Runner', 'Los Juegos del Hambre'],
    'animadas': ['Barbie', 'Coraline', 'Monsters Inc', 'Tierra de Osos'],
    'musical': ['La La Land', 'El mago de Oz', 'Mamma Mia!', 'Singin in the Rain'],
    'musicales': ['La La Land', 'El mago de Oz', 'Mamma Mia!', 'Singin in the Rain'],
    'guerra': ['Nacido para Matar', 'Top Gun', 'Los Juegos del Hambre'],
    'superheroes': ['Star Wars', 'Los Vengadores', 'Interstellar'],
    'suspenso': ['Misión Imposible', 'El Robo Maestro', 'Los Juegos del Hambre'],
    'anime': ['Naruto', 'Your name', 'Demon Slayer']
}


other_options = {
    'accion': [
        "John Wick", "Mad Max: Furia en la carretera", "El caballero de la noche",
        "Kill Bill", "Origen", "Matrix", "Duro de matar", "El exterminador",
        "Gladiator"
    ],
    'aventura': [
        "Piratas del Caribe: La maldición del Perla Negra",
        "El Señor de los Anillos: La Comunidad del Anillo",
        "Indiana Jones y los cazadores del arca perdida", "Parque Jurásico", "Avatar",
        "La Momia", "Los Goonies", "El libro de la selva",
        "Las Crónicas de Narnia: El león, la bruja y el armario"
    ],
    'comedia': [
        "¿Qué pasó ayer?", "Supercool", "Anchorman: El reportero", "Damas en guerra",
        "Una pareja de idiotas", "El día de la marmota", "Chicas pesadas",
        "El Gran Hotel Budapest", "Napoleón Dynamite"
    ],
    'drama': [
        "Sueño de fuga", "Forrest Gump", "El padrino", "La lista de Schindler",
        "El indomable Will Hunting", "En busca de la felicidad", "Una mente brillante",
        "Milagros inesperados", "12 años de esclavitud"
    ],
    'ficcion': [
        "Blade Runner 2049", "El Quinto Elemento", "Eterno resplandor de una mente sin recuerdos",
        "Marte", "Ex Machina", "District 9", "La llegada", "Minority Report",
        "El Show de Truman"
    ],
    'fantasia': [
        "Harry Potter y la piedra filosofal",
        "El Hobbit: Un viaje inesperado", "El laberinto del fauno", "Alicia en el país de las maravillas",
        "Las Crónicas de Narnia: La travesía del Viajero del Alba",
        "Willow", "La princesa prometida", "La historia interminable", "Los niños del maíz"
    ],
    'terror': [
        "El Conjuro", "Déjame salir", "Un lugar tranquilo", "Hereditary", "El Babadook",
        "Insidious", "Sígueme el juego", "El Exorcista", "Poltergeist"
    ],
    'misterio': [
        "El Código Da Vinci", "Perdida", "Prisioneros", "Shutter Island", "Río Místico",
        "Seven", "Sexto sentido", "Zodiac", "El gran truco"
    ],
    'romance': [
        "El diario de Noa", "Orgullo y prejuicio", "La La Land", "Antes del amanecer",
        "500 días con ella", "Eterno resplandor de una mente sin recuerdos", "Romeo y Julieta",
        "Expiación", "Bajo la misma estrella"
    ],
    'thriller': [
        "El silencio de los inocentes", "No es país para viejos", "Fuego contra fuego", "Colateral",
        "La corte", "Memento", "Cisne negro", "Oldboy", "Los infiltrados"
    ],
    'animadas': [
        "Toy Story", "Buscando a Nemo", "Shrek", "Up", "Wall-E", "Los increíbles",
        "Cómo entrenar a tu dragón", "Kung Fu Panda", "El Rey León"
    ],
    'musical': [
        "La La Land", "Los miserables", "La novicia rebelde", "Moulin Rouge",
        "El gran showman", "Chicago", "Cantando bajo la lluvia", "West Side Story",
        "La bella y la bestia"
    ],
    'guerra': [
        "Rescatando al soldado Ryan", "Dunkerque", "Apocalypse Now", "La chaqueta metálica",
        "Hasta el último hombre", "Pelotón", "Corazón valiente", "En tierra hostil", "Corazones de acero"
    ],
    'superheroes': [
        "Los Vengadores", "Spider-Man: Un nuevo universo", "Black Panther",
        "Mujer Maravilla", "Iron Man", "El Caballero de la Noche", "Guardianes de la Galaxia",
        "Capitán América: El soldado de invierno", "Thor: Ragnarok"
    ],
    'suspenso': [
        "Sospechosos comunes", "Vértigo", "La ventana indiscreta", "Los otros", "El sexto sentido",
        "Cabo de miedo", "Shutter Island", "Perdida", "Misery"
    ],
    'anime': [
        "El viaje de Chihiro", "Akira", "Mi vecino Totoro", "Ghost in the Shell",
        "La tumba de las luciérnagas", "Your Name", "Neon Genesis Evangelion: The End of Evangelion",
        "La princesa Mononoke", "Cowboy Bebop: La película"
    ]
}

def check_all_messages(message, already_ask, genero, user_options):
  highest_prob = {}

  eAnimo = ['feliz', 'enojado', 'enojada', 'optimista', 'reflexivo', 'reflexiva', 'deprimida', 'deprimido', 'melancólico', 'melancólica', 'buena vibra', 'triste', 'alegre', 'motivado', 'motivada', 'orgulloso', 'orgullosa', 'entretenido', 'aterrorizado', 'divertido', 'romantico', 'romantica', 'desanimado', 'enamorado', 'contento', 'enamorada', 'contenta', 'decepcionado', 'decepcionada', 'aburrido', 'aburrida', 'cansado', 'cansada', 'estresado', 'estresada', 'sentimental', 'destrozado']
  plataformas = ['netflix', 'amazon', 'disney', 'paramount', 'hbo', 'youtube', 'star', 'apple', 'crunchyroll', 'viki', 'blim', 'prime', 'video', 'vix']
  saved_genres = ['accion', 'aventura', 'comedia', 'drama', 'ficcion', 'fantasia', 'terror', 'misterio', 'romance', 'thriller', 'animadas', 'musical', 'guerra', 'superheroes', 'suspenso', 'anime', 'romanticas']

  directores = ['spielberg', 'scorsese', 'tarantino', 'nolan', 'hitchcock', 'kubrick', 'coppola', 'cameron', 'scott', 'almodóvar', 'anderson', 'fincher', 'eastwood', 'toro', 'burton', 'coen', 'lee', 'aronofsky', 'coppola', 'lee', 'kurosawa',
                'miyazaki', 'allen', 'anderson', 'villeneuve', 'bay', 'snyder', 'jackson', 'stone', 'lucas', 'inarritu', 'soderbergh', 'donen', 'godard', 'truffaut', 'welles', 'lynch', 'leone','fellini', 'polanski', 'bertolucci', 'wilder', 'mann', 'ford', 'howard',
                'forman', 'trier', 'zemeckis', 'noe']

  actores = ['hanks', 'streep', 'washington', 'dicaprio', 'caprio', 'pitt', 'jolie', 'niro', 'johansson', 'depp', 'lawrence', 'day-lewis', 'stone', 'freeman', 'roberts', 'theron', 'smith', 'portman', 'jackson', 'winslet', 'jackman', 'blanchett', 'damon', 'hathaway', 'bale',
             'bullock', 'gosling', 'watson', 'gyllenhaal', 'davis', 'fassbender', 'adams', 'ford', 'kidman', 'connery', 'hemsworth', 'cruise', 'heston', 'pacino', 'aniston', 'foxx', 'redmayne', 'ronan', 'ruffalo', 'rancroft', 'travolta', 'keaton', 'law', 'watts', 'bardem', 'mirren']

  mov_saved = ['mamma', 'vengadores', 'alien', 'depredador', 'monsters', 'ninos', 'pobre' 'ninos', 'niños', 'land', 'naruto', 'guerra', 'mundos', 'interstellar', 'demon', 'slayer', 'matar', 'diario', 'monja', 'titanic', 'oz', 'imposible', 'gun', 'loco', 'coraline', 'robo ', 'maestro', 'barbie', 'osos', 'hambre', 'maze', 'furiosos', 'rain', 'wick', 'carretera', 'caballero', 'bill', 'origen', 'matrix', 'matar', 'exterminador', 'gladiator', 'piratas', 'anillos', 'indiana', 'momia', 'supercool', 'reportero', 'pareja', 'marmota', 'chicas', 'budapest', 'dynamite', 'fuga', 'forest', 'padrino', 'schindler', 'indomable', 'felicidad', 'brillante', 'milagros', 'esclavitud', '2049', 'quinto', 'eterno', 'marte', 'district', 'llegada', 'report', 'potter', 'hobbit', 'fauno', 'alicia', 'narnia', 'willow', 'prometida', 'interminable', 'maiz', 'conjuro', 'salir', 'tranquilo', 'hereditary', 'babadook', 'insidious', 'exorcista', 'poltergeist', 'vinci', 'perida', 'prisioneros', 'shutter', 'mistico', 'seven', 'zodiac', 'truco', 'noa', 'prejuicio', 'amanecer', '500', 'eterno', 'julieta', 'expiacion', 'estrella', 'inocentes', 'viejos', 'fuego', 'corte', 'memento', 'cisne', 'oldboy', 'infiltrados', 'story', 'nemo', 'shrek', 'up', 'wall-e', 'wall', 'increibles', 'dragon', 'panda', 'leon', 'miserables', 'novicia', 'moulin', 'showman', 'chicago', 'lluvia', 'west', 'bestia', 'ryan', 'dunkerque', 'apocalypse', 'chaqueta', 'ultimo', 'iron', 'guardianes', 'capitan', 'thor', 'vertigo', 'indiscreta', 'sexto', 'cabo', 'misery', 'chihiro', 'akira', 'totoro', 'ghost', 'luciernagas', 'name', 'evangelion', 'mononoke', 'bebop']
  #mov_saved = ['mamma', 'vengadores', 'alien', 'depredador', 'pobre' ,'monsters', 'pobre' 'ninos', 'land', 'naruto', 'guerra', 'mundos', 'interstellar', 'demon', 'slayer', 'matar', 'diario', 'monja', 'titanic', 'oz', 'imposible', 'gun', 'loco', 'coraline', 'robo ', 'maestro', 'barbie', 'osos', 'hambre', 'maze', 'furiosos', 'rain']

  # for categoria, peliculas in other_options.items():
  #     for pelicula in peliculas:
  #       movies_saved.append(pelicula)


  def response(bot_response, list_of_words, single_response=False, required_words = []):
    nonlocal highest_prob
    highest_prob[bot_response]= message_probability(message, list_of_words, single_response, required_words)

  for matches in message:
    if (matches in eAnimo or matches in plataformas or matches in saved_genres or matches in mov_saved) and 'Claro. Exactamente ¿cuál es tu estado de ánimo?' in already_ask or 'Claro, estaré encantado.' in already_ask:
      user_options.append(matches)
      break

  if 'Perfecto, entiendo. ¿Cuál es tu género de películas favorito?' in already_ask:
    flag = []
    opciones = ['tengo', 'se', 'ninguno']

    for palabra in message:
      if palabra in saved_genres:
        genero.append(palabra)
        flag = []
        already_ask.remove('Perfecto, entiendo. ¿Cuál es tu género de películas favorito?')
        already_ask.append('Excelente. ¿Cuál de las siguientes películas consideras que te gusta más?: ')
        return f"Excelente. ¿Cuál de las siguientes películas consideras que te gusta más?: {', '.join(peliculas_por_categoria[palabra])}"
      elif palabra in opciones:
          already_ask.append('Bueno, entre estas opciones cuál eliges: ')
          return best_match + ', '.join(rand_genres())
      else:
          flag.append(1)
    if len(flag) > 0:
      return "Lo siento, esa categoría de películas no está disponible en este momento."

  response('Hola, ¿cómo estas?', ['hola', 'klk', 'saludos', 'buenas', 'hello', 'onda', 'holi', 'holaa', 'holaaa', 'holaaaaa', 'ya', 'ver', 'ola'], single_response = True)
  response('Claro, estaré encantado.', ['recomendar', 'puedes', 'recomedarme', 'una'], single_response = True)
  response('Bien, ¿y tú?', ['como', 'tal'], required_words=['estas'])
  response('¿Quieres que te recomiende una película?', ['bien', 'muy', 'tan', 'mas', 'menos', 'excelente', 'buen', 'disfrutando'], single_response=True)
  response('Lo lamento. ¿Una pelicula mejoraría tu estado de ánimo?', ['mal', 'muy'], single_response=True)
  response('Lo lamento. ¿Una pelicula mejoraría tu estado de ánimo?', ['estoy', 'bien'], required_words=['no'])
  response('Igual, pero estaría mejor si viera una película. ¿Quieres que te recomiende una?', ['y'], required_words=['tu'])
  response('Claro. Exactamente ¿cuál es tu estado de ánimo?', ['gustaria', 'vale', 'adelante', 'encantaria', 'ok', 'okey', 'claro', 'si', 'aja', 'acuerdo', 'puesto', 'excelente', 'buena', 'bien', 'bueno', 'esta', 'agradaria'], single_response=True)
  response('Vale, vuelve la próxima vez que quieras ver una pelicula.', ['gracias', 'no'], required_words=['no'])
  response('Entiendo, antes me gustaría preguntarte si ¿utilizas alguna plataforma para ver películas?', eAnimo, single_response=True)
  response('Vale lo tengo. ¿Qué es lo que más disfrutas de una película?', plataformas, single_response = True)
  response('Bueno, sigamos con las preguntas. ¿Qué es lo que más disfrutas de una película?', ['no', 'pagarlas', 'pagar', 'puedo', 'dispuesto'], required_words=['no'])
  response('Perfecto, entiendo. ¿Cuál es tu género de películas favorito?', ['escenografía', 'historia', 'actuacion', 'musica', 'efectos', 'especiales', 'personajes', 'tema', 'ambientación', 'espacio', 'explosiones', 'enamoramiento', 'romance', 'screamer', 'saga', 'libro', 'tomas', 'cinematográficas', 'diálogo', 'actuales', 'finales', 'inesperados', 'final', 'trama', 'desarrollo', 'desarrolla', 'romance', 'inicio', 'soundtracks', 'musica', 'creditos'], single_response=True)
  response('Excelente elección.', ['mamma', 'vengadores', 'alien', 'depredador', 'monsters', 'pobre' 'ninos', 'land', 'naruto', 'guerra', 'mundos', 'interstellar', 'demon', 'slayer', 'matar', 'diario', 'monja', 'titanic', 'oz', 'imposible', 'gun', 'loco', 'coraline', 'robo ', 'maestro', 'barbie', 'osos', 'hambre', 'maze', 'furiosos', 'rain'], single_response=True)
  response('Entiendo.', ['ninguna', 'anteriores', 'gusta', 'agrada', 'ninguno'], single_response=True)
  response('Otra opcion..', ['otra', 'pelicula', 'opcion', 'recomienda', 'recomiendame', 'dame', 'sugerir', 'recomendar', 'recomendacion'], required_words=['otra'])
  response('Puede ser..', ['peliculas', 'opciones', 'recomienda', 'recomiendame', 'dame', 'sugerir', 'recomendar', 'recomendaciones'], required_words=['otras'])
  response('Quizas..', ['peliculas', 'opciones', 'recomienda', 'recomiendame', 'dame', 'sugerir', 'recomendar', 'recomendaciones'], required_words=['mas'])
  #response('Excelente. Si estas contento con el resultado, hablamos la próxima vez que quieras ver una película. Hasta pronto.', ['cool', 'vale', 'bueno', 'idea', 'agrada'], single_response=True)
  response('Adiós.', ['adios', 'nos', 'vemos', 'pronto', 'hasta', 'bye'], single_response=True)

  response('Muy bien, perfecto.', directores, single_response=True)
  response('Ohhh, también es mi favorito.', actores, single_response=True)

  # if best_match == 'Otra opcion..' and ('¿Tienes un director de películas favorito? Si es así, ¿Cuál es?' in already_ask or 'Si tuvieras que salir en una película con tu actor favorito, ¿Quién sería?' in already_ask or 'Te dan a elegir qué papel quisieras tomar en la película en donde actuarás con tu actor favorito, ¿Qué papel escoges?' in already_ask):
  #   return 'Vale, puede ser...' +generar_prediccion(usuario)

  best_match = max(highest_prob, key=highest_prob.get)
  print(best_match)
  #print(highest_prob)

  if best_match == 'Claro, estaré encantado.':
    already_ask.append('Claro, estaré encantado.')
    return best_match + '\n\tPrimero me gustaría preguntarte ¿cuál es tu estado de ánimo?'


  for palabra in message:
    if palabra in ['gracias', 'thx', 'thanks', 'cool', 'buena'] and 'Termina' in already_ask:
      return 'Si estas contento con el resultado, hablamos la próxima vez que quieras ver una película. Hasta pronto.'

  if ('Excelente elección.' in already_ask or 'Entiendo.' in already_ask) and 'Bueno, entre estas opciones cuál eliges: ' in already_ask and best_match != 'De nada, vuelve pronto':
    usuario = cod_user_options(user_options)
    return best_match + 'Entonces voy a recomendarte la pelicula ' + generar_prediccion(usuario)

  if '¿Tienes un director de películas favorito? Si es así, ¿Cuál es?' in already_ask and (best_match != 'Muy bien, perfecto.' and best_match != 'Entiendo.' and best_match != 'De nada, vuelve pronto'):
    user_options.append('ninguno')
    already_ask.append('Termina')
    usuario = cod_user_options(user_options)
    return 'Entonces te recomiendo ver la película ' + generar_prediccion(usuario)

  if 'Si tuvieras que salir en una película con tu actor favorito, ¿Quién sería?' in already_ask and (best_match != 'Muy bien, perfecto.' or best_match != 'Entiendo.' and best_match != 'De nada, vuelve pronto'):
    user_options.append('ninguno')
    already_ask.append('Termina')
    #user_options.append('ninguno')
    usuario = cod_user_options(user_options)
    return 'Bueno. Entonces te recomiendo ver la película ' + generar_prediccion(usuario)

  if 'Te dan a elegir qué papel quisieras tomar en la película en donde actuarás con tu actor favorito, ¿Qué papel escoges?' in already_ask and best_match != 'De nada, vuelve pronto':
    already_ask.remove('Te dan a elegir qué papel quisieras tomar en la película en donde actuarás con tu actor favorito, ¿Qué papel escoges?')
    user_options.append('ninguno')
    already_ask.append('Termina')
    usuario = cod_user_options(user_options)
    return 'Suena bien. Entonces voy a recomendarte la pelicula ' + generar_prediccion(usuario)

  if best_match == 'Muy bien, perfecto.' and best_match != 'De nada, vuelve pronto':
    for matches in message:
      if matches in directores:
        user_options.append(matches)
    user_options.append('ninguno')
    usuario = cod_user_options(user_options)
    return best_match + 'Entonces voy a recomendarte la película ' + generar_prediccion(usuario)

  if best_match == 'Ohhh, también es mi favorito.' and best_match != 'De nada, vuelve pronto':
    for matches in message:
      if matches in actores:
        user_options.append(matches)
    user_options.append('ninguno')
    usuario = cod_user_options(user_options)
    return best_match + 'Entonces voy a recomendarte la película ' + generar_prediccion(usuario)

  if best_match == 'Otra opcion..' or best_match == 'Puede ser..' or best_match == 'Quizas..':
    return best_match + rand_movie(genero)

  if best_match == 'Excelente elección.' or best_match == 'Entiendo.':
    return best_match + rand_question(already_ask)

  if best_match == 'Perfecto, entiendo. ¿Cuál es tu género de películas favorito?':
    already_ask.append(best_match)

  if best_match == 'Entiendo, antes me gustaría preguntarte si ¿utilizas alguna plataforma para ver películas?':
    already_ask.append('Entiendo, antes me gustaría preguntarte si ¿utilizas alguna plataforma para ver películas?')

  if best_match == 'Vale, vuelve la próxima vez que quieras ver una pelicula.' and 'Entiendo, antes me gustaría preguntarte si ¿utilizas alguna plataforma para ver películas?' in already_ask:
    user_options.append('ninguna')
    return 'Bueno, sigamos con las preguntas. ¿Qué es lo que más disfrutas de una película?'

  sentence = 'Claro. Exactamente ¿cuál es tu estado de ánimo?'
  if best_match == sentence and sentence in already_ask:
    return '¿Qué plataformas utilizas?'

  if best_match == 'Claro. Exactamente ¿cuál es tu estado de ánimo?':
    already_ask.append(best_match)

  sentence = '¿Quieres que te recomiende una película?'
  if best_match == sentence and sentence in already_ask:
    return 'Entiendo, antes me gustaría preguntarte si ¿utilizas alguna plataforma para ver películas?'

  if best_match == '¿Quieres que te recomiende una película?':
    already_ask.append(best_match)

  sentence = 'Igual, pero estaría mejor si viera una película. ¿Quieres que te recomiende una?'
  if best_match == sentence and sentence in already_ask:
    return 'Entiendo, antes me gustaría preguntarte si ¿utilizas alguna plataforma para ver películas?'

  if best_match == 'Igual, pero estaría mejor si viera una película. ¿Quieres que te recomiende una?':
    already_ask.append(best_match)

  #print(already_ask)

  return unknown() if highest_prob[best_match] < 1 else best_match

def unknown():
  response = ['¿Puedes decirlo de nuevo?', 'No estoy seguro de lo que quieres decir.', '¿Puedes escibirlo nuevamente?', 'Dilo de nuevo por favor.'][random.randrange(4)]
  return response

def rand_question(already_ask):
  response = ['¿Tienes un director de películas favorito? Si es así, ¿Cuál es?', 'Si tuvieras que salir en una película con tu actor favorito, ¿Quién sería?', 'Te dan a elegir qué papel quisieras tomar en la película en donde actuarás con tu actor favorito, ¿Qué papel escoges?'][random.randrange(3)]
  already_ask.append(response)
  return response

def rand_movie(generos):
  flag = []
  for genero in generos:
    for categoria, peliculas in other_options.items():
      all_movies = []
      if genero == categoria:
        for pelicula in peliculas:
          all_movies.append(pelicula)

        flag = []
        response = all_movies[random.randrange(len(all_movies))]
        return response
    else:
        flag.append(1)
  if len(flag) > 0:
    return "Lo siento, no hay más películas para esa categoría. Pero te voy a recomendar..." + generar_prediccion()

  response = ['¿Tienes un director de películas favorito? Si es así, ¿Cuál es?', 'Si tuvieras que salir en una película con tu actor favorito, ¿Quién sería?', 'Te dan a elegir qué papel quisieras tomar en la película en donde actuarás con tu actor favorito, ¿Qué papel escoges?'][random.randrange(3)]
  return response

def rand_genres():
  all_genres = []
  for categoria, peliculas in other_options.items():
    all_genres.append(categoria)
  random_genres = random.sample(all_genres, 3)
  return random_genres

import pandas as pd
df = pd.read_csv('./Final/pelis.csv')
#print(df.isnull().sum())
df = pd.get_dummies(df, columns=['Actores_o_Director', 'Estado', 'Plataformas', 'Genero'])

from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score

X = df.drop('Nombre', axis=1)  # Características de las películas
y = df['Nombre']  # Etiqueta: nombre de la película

svm_classifier = SVC(probability=True)
svm_classifier.fit(X, y)
columnas_entrenamiento = X.columns

def cod_user_options(options_list):
  options = {
    'Actores_o_Director': options_list[4],
    'Estado': options_list[0],
    'Plataformas': options_list[1],
    'Genero': options_list[2]
  }
  return options

def generar_prediccion(usuario):
  usuario_codificado = {
      'Actores_o_Director': usuario['Actores_o_Director'],
      'Estado': usuario['Estado'],
      'Plataformas': usuario['Plataformas'],
      'Genero': usuario['Genero']
  }

  usuario_df = pd.DataFrame(usuario_codificado, index=[0])
  usuario_df = pd.get_dummies(usuario_df)
  usuario_df_ajustado = usuario_df.reindex(columns=columnas_entrenamiento, fill_value=0)
  probabilidades = svm_classifier.predict_proba(usuario_df_ajustado)
  indice_pelicula_recomendada = probabilidades.argmax()
  pelicula_recomendada = df.iloc[indice_pelicula_recomendada]['Nombre']

  response = f"{pelicula_recomendada}"
  return response

already_ask = []
genero = []
user_options = []
while True:
  respuesta = get_response(input('You: '), already_ask, genero, user_options)
  #print(user_options)
  print("Bot: "+ respuesta)
  if str(respuesta) == 'Vale, vuelve la próxima vez que quieras ver una pelicula.' or str(respuesta) == 'Si estas contento con el resultado, hablamos la próxima vez que quieras ver una película. Hasta pronto.' or str(respuesta) == 'Adiós.':
    break