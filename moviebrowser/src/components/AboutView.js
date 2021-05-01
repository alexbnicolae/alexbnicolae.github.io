import Hero from './Hero'


const AboutView = () => {
    return (
        <>
            <Hero text="About us"/>
            <div className="container">
                <div className="row">
                    <div className="col-lg-8 offset-lg-2 my-5">
                        <p> 
                        Lorem ipsum dolor sit amet consectetur adipisicing elit. Ipsa perspiciatis est obcaecati cumque culpa atque recusandae, quia vero dolore libero tempora aliquam aut enim quisquam.
                        </p>
                    </div>
                </div>
            </div>
        </>
    )
  }

  export default AboutView;