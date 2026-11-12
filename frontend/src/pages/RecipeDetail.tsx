import { useState } from 'react'
import { Link, useParams } from 'react-router'
import { recipes } from '@/data'

function RecipeDetail() {
  // On récupère l'id dans l'URL : /recette/:id
  const { id } = useParams()
  const recipe = recipes.find((r) => r.id === Number(id))

  // Note donnée par l'utilisateur (0 = pas encore noté)
  const [myRating, setMyRating] = useState(0)

  if (!recipe) {
    return <p>Recette introuvable. <Link to="/" className="text-orange-600">Retour</Link></p>
  }

  function share() {
    navigator.clipboard.writeText(window.location.href)
    alert('Lien copié !')
  }

  return (
    <div className="rounded-xl bg-white p-6 shadow-sm">
      <Link to="/" className="text-sm text-orange-600 hover:underline">← Retour</Link>

      <div className="mt-4 text-4xl">{recipe.flag}</div>
      <h1 className="text-3xl font-bold">{recipe.title}</h1>
      <p className="mb-4 text-stone-500">
        {recipe.country} · ⏱ {recipe.time} min · {recipe.difficulty} · ⭐ {recipe.rating} ({recipe.votes} avis)
      </p>
      <p className="mb-6">{recipe.description}</p>

      {/* Actions : partage, note */}
      <div className="mb-6 flex flex-wrap items-center gap-2">
        <button onClick={share} className="rounded-lg border border-orange-300 px-4 py-2 hover:bg-orange-50">
          🔗 Partager
        </button>

        <div className="sm:ml-auto">
          <span className="text-sm text-stone-500">Votre note : </span>
          {[1, 2, 3, 4, 5].map((star) => (
            <button key={star} onClick={() => setMyRating(star)} className="text-2xl text-amber-400">
              {star <= myRating ? '★' : '☆'}
            </button>
          ))}
        </div>
      </div>

      <div className="grid gap-6 md:grid-cols-2">
        <div>
          <h2 className="mb-2 text-lg font-semibold">Ingrédients</h2>
          <ul className="list-inside list-disc">
            {recipe.ingredients.map((ingredient) => (
              <li key={ingredient}>{ingredient}</li>
            ))}
          </ul>
        </div>
        <div>
          <h2 className="mb-2 text-lg font-semibold">Préparation</h2>
          <ol className="list-inside list-decimal">
            {recipe.steps.map((step) => (
              <li key={step}>{step}</li>
            ))}
          </ol>
        </div>
      </div>
    </div>
  )
}

export default RecipeDetail
