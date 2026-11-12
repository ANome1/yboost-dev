import { Routes, Route } from 'react-router'
import Navbar from '@/components/Navbar'
import Home from '@/pages/Home'
import RecipeDetail from '@/pages/RecipeDetail'

function App() {
  return (
    <div className="min-h-screen bg-orange-50 text-stone-800">
      <Navbar />

      <main className="mx-auto max-w-5xl px-4 py-6">
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/recette/:id" element={<RecipeDetail />} />
        </Routes>
      </main>
    </div>
  )
}

export default App
