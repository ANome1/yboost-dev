import { Link } from 'react-router'
import type { Recipe } from '@/data'

type Props = {
  recipe: Recipe
}

function RecipeCard({ recipe }: Props) {
  return (
    <Link
      to={`/recette/${recipe.id}`}
      className="block rounded-xl border border-orange-100 bg-white p-4 shadow-sm hover:shadow-md"
    >
      <div className="mb-2 text-3xl">{recipe.flag}</div>
      <h2 className="font-semibold">{recipe.title}</h2>
      <p className="mb-3 text-sm text-stone-500">{recipe.description}</p>

      <div className="flex gap-3 text-xs text-stone-500">
        <span>⭐ {recipe.rating}</span>
        <span>⏱ {recipe.time} min</span>
        <span>{recipe.difficulty}</span>
      </div>
    </Link>
  )
}

export default RecipeCard
