import Hero from './Hero'


const NotFoundPage = () => {
    return (
        <>
            <Hero text="Error 404: Page not found!"/>
            <h1 className="fs-1 position-absolute top-50 start-50 translate-middle">Search something else!</h1>
        </>
    )
  }

  export default NotFoundPage;