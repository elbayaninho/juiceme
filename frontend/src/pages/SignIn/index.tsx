import { Col, Container, Image, Row } from "react-bootstrap"
import logo from "../../assets/logo-white.svg"
import dashboard from "../../assets/dashboard.svg"
import './index.scss'
const Login = () => {

    return(
        <Container>
            <Row>
                <Col className="col-left">
                 <Image src={logo} alt="logo" />
                 <p>Empower your employees with early wage access, seamless communication, and effortless employee management. </p>
                 <Image src={dashboard} />
                </Col>
                <Col></Col>

            </Row>

        </Container>
    )

}

export default Login