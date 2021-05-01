import Hero from './Hero'
import {useParams} from 'react-router-dom'
import { useState, useEffect } from 'react'


const MovieDetails = () => {
    const {id} = useParams()
    const [movieDetails, setMovieDetails] = useState({})
    const [isLoading, setIsLoading] = useState(true)

    useEffect(() => {
        fetch(`https://api.themoviedb.org/3/movie/${id}?api_key=ba2e3df5c2848b37c23d0ac454f72926&language=en-US
        `).then(response => response.json()).then(data => {
            setMovieDetails(data)
            setIsLoading(false)
        })
    }, [id])

    function renderMovieDetails() {
        if(isLoading) {
            return <Hero text="Loading..."/>
        }
        if(movieDetails) {
            var posterPath = `https://image.tmdb.org/t/p/w500${movieDetails.poster_path}`
            if (movieDetails.poster_path === null) {
                posterPath = "https://upload.wikimedia.org/wikipedia/commons/a/ac/No_image_available.svg"
            }
            const backdropURL = `https://image.tmdb.org/t/p/original${movieDetails.backdrop_path}`
            return (
                <>
                    <Hero text={movieDetails.original_title} backdrop={backdropURL}/>
                    <div className="container my-5">
                        <div className="row">
                            <div className="col-md-3">
                                <img src={posterPath} alt="..." className="img-fluid shadow rounded" />
                            </div>
                            <div className="col-md-9">
                                <h2>{movieDetails.original_title}</h2>
                                <p className="lead">
                                    {movieDetails.overview}
                                </p>
                            </div>
                        </div>
                    </div>
                </>
            ) 
        }
    }

    return renderMovieDetails()
  }
  export default MovieDetails;