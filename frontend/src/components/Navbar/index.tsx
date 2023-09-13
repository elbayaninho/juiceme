import Nav from 'react-bootstrap/Nav';
import Navbar from 'react-bootstrap/Navbar';
import logo from "../../assets/logo.svg"
import './index.scss'
import { Button } from 'react-bootstrap';
const NavbarParent = () => {
   return(
      <Navbar expand="lg" className="bg-body-white">
        <Navbar.Brand href="/">
          <img alt='Juiceme Logo' src={logo} />
        </Navbar.Brand>
        <Navbar.Toggle aria-controls="navbar-toggle" />
        <Navbar.Collapse>
          <Nav  >
            <Nav.Link href="#home">Products</Nav.Link>
            <Nav.Link href="#link">Contact Us</Nav.Link>
            <Button className="btn" type="submit">
              <Nav.Link href="/signin">Sign In</Nav.Link>
            </Button>
          </Nav>
        </Navbar.Collapse>
    </Navbar>
   )
};

export default NavbarParent;
