import Hero from './Hero';
import {Link} from 'react-router-dom';

//https://api.themoviedb.org/3/search/movie?api_key=ba2e3df5c2848b37c23d0ac454f72926&language=en-US&query=star%20wars&page=1&include_adult=false

const MovieCard = ({movie}) => {
    var posterUrl = `https://image.tmdb.org/t/p/w500${movie.poster_path}`
    if (movie.poster_path === null) {
        posterUrl = "https://upload.wikimedia.org/wikipedia/commons/a/ac/No_image_available.svg"
    }
    const detailUrl = `/movies/${movie.id}`
    return (
        <div class="col-lg-3 col-md-3 col-2 my-4">
            <div className="card">
                <img src={posterUrl} className="card-img-top" alt={movie.original_title} style={{height:400}}/>
                <div className="card-body">
                    <h5 className="card-title">{movie.original_title}</h5>
                    <Link to={detailUrl} className="btn btn-primary">Show details</Link>
                </div>
            </div>
        </div>
    )
}

const SearchView = ({keyword, searchResults}) => {
    const title = `You searched for ${keyword}`
    if(searchResults.length === 0)
    {
        return (
            <>
                <div className="fs-1 position-absolute top-50 start-50 translate-middle">There is no movie with the name: <strong>{keyword}</strong>!
                <br />
                <div className="fs-1" style={{textAlign: 'center'}}>Try again!</div>
                </div>
            </>
        )
    }
    else{
        var resultsHtml = searchResults.map((obj, i) => {
            return <MovieCard movie={obj} key={i}/>
        })
    }

    return (
      <>
        <Hero text={title} />
         <div className="container">
                <div className="row">
                    {resultsHtml}
                </div>
        </div>
            
        
    
      </>
    )
}

  export default SearchView;