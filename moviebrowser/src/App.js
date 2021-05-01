import './App.css';
import Navbar from './components/Navbar'
import Home from './components/Home'
import AboutView from './components/AboutView'
import SearchView from './components/SearchView'
import MovieDetails from './components/MovieDetails'
import NotFoundPage from './components/NotFoundPage';
import SearchPage from './components/SearchPage';
import {Switch, Route, Redirect} from 'react-router-dom'
import { useState, useEffect } from 'react';


function App(){

  const [searchResults, setSearchResults] = useState([])
  const [searchText, setSearchText] = useState('')

  useEffect(() => {
    if (searchText)
    {
      fetch(`https://api.themoviedb.org/3/search/movie?api_key=ba2e3df5c2848b37c23d0ac454f72926&language=en-US&query=${searchText}&page=1&include_adult=false`).then(response => response.json()).then(data => {
        setSearchResults(data.results)
      })
    }
  }, [searchText])


  return (
    <div>
      <Navbar searchText = {searchText} setSearchText={setSearchText}/>
      <Switch>
        <Route path="/" exact>
           <Home />
        </Route>
        <Route path="/about" component={AboutView} />
        <Route path="/search">
          <SearchView keyword={searchText} searchResults={searchResults} />
        </Route>
        <Route path="/movies/:id" component={MovieDetails} />
        <Route path="/404" component={NotFoundPage} />
        <Route path="/searchPage">
            <SearchPage keyword={searchText} />
        </Route>
        <Redirect to="/404" />
      </Switch>
    </div>
  )
}

export default App;
