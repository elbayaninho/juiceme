import { Badge } from 'react-bootstrap'
import shoprite from '../../assets/shoprite.svg'
import './index.scss'
const Home = () => {

    return (
        <div id="home">
            <div id="call-to-action">
                <div>
                    <h2>Customer-centric technology for African Employees and SMEs.</h2>
                    <p>Streamline your business operations, financing and people management with our integrated solution and the power of WhatsApp.</p>
                    <button>Book Demo</button>
                    <button>Learn more</button>
                </div>
                <div>

                </div>
            </div>
            <div id="svg">

            </div>
            <div id="mission">
                <div id="partners">
                    <img src={shoprite} alt="shoprite" />
                    <img src={shoprite} alt="shoprite" />
                </div>
                <Badge>Our Mission</Badge>
                <h4>Unlocking economic value for African employees and SMEs</h4>
                <div>
                    <p>Africa will have the world’s largest workforce in 10 years</p>
                    <p>+80% workforce will be deskless in manufacturing, construction, agriculture etc...</p>
                    <p>70% of employees earn less than $500 a month</p>
                    <p>Middle income earners spend up to 80% of their salary within 5 days of payday</p>
                </div>
            </div>

        </div>
    )

}

export default Home