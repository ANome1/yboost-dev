export type Recipe = {
  id: number
  title: string
  country: string
  flag: string
  time: number
  difficulty: 'Facile' | 'Moyen' | 'Difficile'
  description: string
  ingredients: string[]
  steps: string[]
  rating: number
  votes: number
}

export type User = {
  name: string
  email: string
  favoriteCountry: string
}

export const recipes: Recipe[] = [
  {
    id: 1,
    title: 'Pad Thaï',
    country: 'Thaïlande',
    flag: '🇹🇭',
    time: 30,
    difficulty: 'Moyen',
    description: 'Nouilles de riz sautées, cacahuètes, citron vert et sauce tamarin.',
    ingredients: ['200 g de nouilles de riz', '2 œufs', '150 g de crevettes', 'Pousses de soja', 'Cacahuètes', 'Sauce tamarin', 'Citron vert'],
    steps: ['Faire tremper les nouilles.', 'Saisir les crevettes au wok.', 'Ajouter les œufs puis les nouilles et la sauce.', 'Servir avec cacahuètes et citron vert.'],
    rating: 4.6,
    votes: 128,
  },
  {
    id: 2,
    title: 'Tacos al pastor',
    country: 'Mexique',
    flag: '🇲🇽',
    time: 45,
    difficulty: 'Moyen',
    description: 'Porc mariné aux piments et ananas dans des tortillas de maïs.',
    ingredients: ["500 g d'échine de porc", 'Piments guajillo', 'Ananas', 'Tortillas de maïs', 'Oignon', 'Coriandre'],
    steps: ['Mariner le porc 2 h.', "Griller la viande et l'ananas.", 'Émincer et garnir les tortillas.', 'Ajouter oignon et coriandre.'],
    rating: 4.8,
    votes: 214,
  },
  {
    id: 3,
    title: 'Risotto aux champignons',
    country: 'Italie',
    flag: '🇮🇹',
    time: 40,
    difficulty: 'Moyen',
    description: 'Riz arborio crémeux, champignons et parmesan.',
    ingredients: ['300 g de riz arborio', '250 g de champignons', '1 L de bouillon', '1 oignon', 'Parmesan', 'Beurre'],
    steps: ["Faire revenir l'oignon.", 'Nacrer le riz.', 'Ajouter le bouillon louche par louche.', 'Incorporer champignons, beurre et parmesan.'],
    rating: 4.5,
    votes: 97,
  },
  {
    id: 4,
    title: 'Ramen shoyu',
    country: 'Japon',
    flag: '🇯🇵',
    time: 90,
    difficulty: 'Difficile',
    description: 'Bouillon à la sauce soja, nouilles, œuf mollet et porc braisé.',
    ingredients: ['Nouilles ramen', 'Bouillon de volaille', 'Sauce soja', 'Poitrine de porc', 'Œufs', 'Cébette', 'Nori'],
    steps: ['Préparer le bouillon.', 'Braiser le porc.', 'Cuire les œufs 6 min 30.', 'Assembler le bol.'],
    rating: 4.9,
    votes: 302,
  },
  {
    id: 5,
    title: 'Tajine de poulet aux citrons',
    country: 'Maroc',
    flag: '🇲🇦',
    time: 75,
    difficulty: 'Facile',
    description: 'Poulet mijoté, citrons confits et olives vertes.',
    ingredients: ['1 poulet', '2 citrons confits', 'Olives vertes', 'Oignons', 'Gingembre', 'Safran', 'Coriandre'],
    steps: ['Mariner le poulet aux épices.', 'Faire revenir avec les oignons.', 'Mijoter 1 h avec citrons et olives.'],
    rating: 4.7,
    votes: 156,
  },
  {
    id: 6,
    title: 'Butter chicken',
    country: 'Inde',
    flag: '🇮🇳',
    time: 50,
    difficulty: 'Moyen',
    description: 'Poulet mariné dans une sauce tomate au beurre et à la crème.',
    ingredients: ['600 g de poulet', 'Yaourt', 'Garam masala', 'Tomates concassées', 'Beurre', 'Crème', 'Ail, gingembre'],
    steps: ['Mariner le poulet au yaourt et épices.', 'Griller le poulet.', 'Préparer la sauce tomate-beurre.', 'Réunir et ajouter la crème.'],
    rating: 4.8,
    votes: 241,
  },
  {
    id: 7,
    title: 'Ratatouille',
    country: 'France',
    flag: '🇫🇷',
    time: 60,
    difficulty: 'Facile',
    description: "Légumes du soleil mijotés à l'huile d'olive et aux herbes.",
    ingredients: ['Aubergine', 'Courgettes', 'Poivrons', 'Tomates', 'Oignon', 'Ail', 'Herbes de Provence'],
    steps: ['Couper les légumes.', 'Les saisir séparément.', 'Mijoter ensemble 40 min.'],
    rating: 4.3,
    votes: 88,
  },
  {
    id: 8,
    title: 'Feijoada',
    country: 'Brésil',
    flag: '🇧🇷',
    time: 120,
    difficulty: 'Difficile',
    description: 'Ragoût de haricots noirs et viandes fumées.',
    ingredients: ['500 g de haricots noirs', 'Saucisse fumée', 'Lard', 'Oignon', 'Ail', 'Feuilles de laurier', 'Riz blanc'],
    steps: ['Faire tremper les haricots la veille.', 'Cuire avec les viandes 2 h.', 'Servir avec du riz et des tranches d\'orange.'],
    rating: 4.4,
    votes: 64,
  },
]

export const countries = [...new Set(recipes.map((r) => r.country))].sort()
