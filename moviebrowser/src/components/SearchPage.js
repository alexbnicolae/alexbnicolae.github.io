const SearchPage = ({keyword}) => {

    return (
        <header className="bg-dark text-white p-5 hero-container">
            <h1 className="hero-text" style={{textAlign:'center'}}>You are searching for <u>{keyword}</u></h1>    
        </header>
    )
}

  export default  SearchPage;