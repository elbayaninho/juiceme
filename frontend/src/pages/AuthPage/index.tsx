import { Col, Image, Row } from "react-bootstrap"
import logo from "../../assets/logo-white.svg"
import dashboard from "../../assets/dashboard.svg"
import './index.scss'
import Auth from "../../components/Auth"
const AuthPage = () => {

    return(
            <Row id="row" >
                <Col id="col-left" sm={6} md={4} lg={4}>
                 <Image src={logo} alt="logo" className="logo"/>
                 <p className="typograph">Empower your employees with early wage access, seamless communication, and effortless employee management. </p>
                 <div className="imageContainer">
                 <Image src={dashboard} className="dashboardImg"/>
                 </div>
                </Col>
                <Col sm={6} md={8} lg={8}>
                    <Auth/>
                </Col>

            </Row>

    )

}

export default AuthPage