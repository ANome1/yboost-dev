import { Link } from 'react-router'

function Navbar() {
  return (
    <header className="sticky top-0 border-b border-orange-100 bg-white">
      <nav className="mx-auto flex max-w-5xl items-center gap-4 px-4 py-3">
        <Link to="/" className="mr-auto text-xl font-bold text-orange-600">
          🌍 WorldRecipes
        </Link>
        <Link to="/" className="hover:text-orange-600">Recettes</Link>
      </nav>
    </header>
  )
}

export default Navbar
