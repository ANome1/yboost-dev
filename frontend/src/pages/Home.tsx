import { useState } from 'react'
import { recipes, countries } from '@/data'
import RecipeCard from '@/components/RecipeCard'

function Home() {
  const [search, setSearch] = useState('')
  const [country, setCountry] = useState('')

  const filteredRecipes = recipes.filter((recipe) => {
    const matchSearch = recipe.title.toLowerCase().includes(search.toLowerCase())
    const matchCountry = country === '' || recipe.country === country
    return matchSearch && matchCountry
  })

  return (
    <div>
      <h1 className="mb-4 text-2xl font-bold">Recettes du monde entier</h1>

      <div className="mb-6 flex flex-col gap-2 sm:flex-row">
        <input
          value={search}
          onChange={(e) => setSearch(e.target.value)}
          placeholder="Rechercher une recette..."
          className="flex-1 rounded-lg border border-orange-200 bg-white px-3 py-2"
        />
        <select
          value={country}
          onChange={(e) => setCountry(e.target.value)}
          className="rounded-lg border border-orange-200 bg-white px-3 py-2"
        >
          <option value="">Tous les pays</option>
          {countries.map((c) => (
            <option key={c} value={c}>{c}</option>
          ))}
        </select>
      </div>

      {filteredRecipes.length === 0 && <p className="text-stone-500">Aucune recette trouvée.</p>}

      <div className="grid gap-4 sm:grid-cols-2 lg:grid-cols-3">
        {filteredRecipes.map((recipe) => (
          <RecipeCard key={recipe.id} recipe={recipe} />
        ))}
      </div>
    </div>
  )
}

export default Home
