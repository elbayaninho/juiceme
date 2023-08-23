import Container from 'react-bootstrap/Container';
import Nav from 'react-bootstrap/Nav';
import Navbar from 'react-bootstrap/Navbar';
import logo from "../../assets/logo.svg"
import './index.scss'
const NavbarParent = () => {
   return(
      <Navbar expand="lg" className="bg-body-white">
      <Container>
        <Navbar.Brand href="#home"><img alt='Juiceme Logo' src={logo} /></Navbar.Brand>
        <Navbar.Toggle aria-controls="navbar-toggle" />
        <Navbar.Collapse id="basic-navbar-nav">
          <Nav  >
            <Nav.Link href="#home">Products</Nav.Link>
            <Nav.Link href="#link">Contact Us</Nav.Link>
            <Nav.Link href="signin">Sign In</Nav.Link>
          </Nav>
        </Navbar.Collapse>
      </Container>
    </Navbar>
   )
};

export default NavbarParent;
