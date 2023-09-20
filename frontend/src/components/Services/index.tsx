import { Badge, Button } from 'react-bootstrap'
import service1 from '../../assets/services1.svg'
import service2 from '../../assets/service2.svg'
import service3 from '../../assets/service3.svg'
import './index.scss'

const Services = () => {

    return (
        <div id="services">
            <div className="service">
                <img src={service1} alt='Service one'/>
                <div className='content'>
                <Badge>Providing earned wages access</Badge>    
                <h4>Anyday is Payday</h4>
                <p>Does you employee have an expense that can’t wait until payday? By providing this solution at zero cost to your organization with no charges to your payroll structure. Your become an employer of choice, attracts and retains top talents and boots productivity.</p>
                <Button>Apply Now</Button>
                </div>
            </div>
            <div className="service">
            <img src={service2} alt='Service one'/>
            <div className='content'>
                <Badge>HR and Payroll management</Badge>    
                <h4>Leveraging WhatsApp to improve your HR and payroll system</h4>
                <p>Our holistic HR system caters to both desk and deskless employees by leveraging the power of convenience.</p>
                <Button>Get Started</Button>
                </div>
            </div>
            <div className="service">
            <img src={service3} alt='Service one'/>

            <div className='content'>
                <Badge>Working capital financing</Badge>    
                <h4>Supporting SMEs grow their bussinesses</h4>
                <p>Juice enables your business to turn your unpaid invoices into cash so that you can pay your supplier and cover operational expenses with no downtime. Let’s say you got an order to make school uniforms and you don’t have the money..</p>
                <Button>Get Started</Button>
                </div>
            </div>
        </div>
    )

}

export default Services;