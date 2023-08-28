import { useEffect, useState } from "react";
import { NavLink, useLocation} from "react-router-dom"
import { Form, Container, Button, Row, Col } from "react-bootstrap";
import './index.scss'

const SignIn = () => {
  const [signIn, setSignIn] = useState(true)
  const [signUp, setSignUp] = useState(false)
  const location = useLocation();

  useEffect(() =>{
   if(location.pathname === '/signin'){
    setSignIn(true)
    setSignUp(false)
   }else if(location.pathname === '/signup'){
    setSignUp(true)
    setSignIn(false)
   }
  }, [location])

  const typographyInfo = {
    signUp: {
      "title": "Create your account",
      "description": "Let’s help you get started on Juiceme"
    },
    signIn: {
      "title": "Log in to your account",
      "description": "Welcome back to Juiceme"
    }
  }

  return (
    <Container>
      {signIn && (
        <div>
          <h1>{typographyInfo.signIn.title}</h1>
          <p>{typographyInfo.signIn.description}</p>
        </div>
      )}
      {signUp && (
        <div>
          <h1>{typographyInfo.signUp.title}</h1>
          <p>{typographyInfo.signUp.description}</p>
        </div>
      )}

      <Form>
        {signUp && (<Form.Group className="mb-3" controlId="fullName">
          <Form.Label>Full Name</Form.Label>
          <Form.Control type="text" placeholder="John Doe" />
        </Form.Group>)}
        {signUp && (<Form.Group className="mb-3" controlId="phoneNumber">
          <Form.Label>Phone Number</Form.Label>
          {/* need to add the location dropdown */}
            <Form.Control type="tel" placeholder="8287938745" />
        </Form.Group>)}
        <Form.Group className="mb-3" controlId="email">
          <Form.Label>{signIn ? "Representative Email" : "Email"}</Form.Label>
          <Form.Control type="email" placeholder="example@gmail.com" />
        </Form.Group>
        <Form.Group className="mb-3" controlId="password">
          <Form.Label>Password</Form.Label>
          <Form.Control type="password" placeholder="********" />
        </Form.Group>

        {signUp && (<Form.Group className="mb-3" controlId="confirmPassword">
          <Form.Label>Confirm Password</Form.Label>
          <Form.Control type="password" placeholder="********" />
        </Form.Group>)}
        {signIn && <Row className="signIn">
          <Col md={5}>
          <Form.Check type='checkbox' id="rememberMe" label="Remember me"/>
          </Col>
          <Col  md={7}>
          <p>Forgot password? <NavLink to="/reset">Reset</NavLink></p>
          </Col>
        </Row>}
        <Button variant="primary" >{signIn? "Sign In" : "Sign Up"}</Button>
        {signIn && (<p>Don't have an account? <NavLink to="/signup">Sign Up</NavLink></p>)}
        {signUp && (<p>Have an account? <NavLink to="/signin">Sign In</NavLink></p>)}
      </Form>

    </Container>
  )

}

export default SignIn;