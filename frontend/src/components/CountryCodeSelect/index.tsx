import { Form } from "react-bootstrap"
import  './index.scss'
import countryCode from  './countries-code.json'

const CountryCodeSelect = () => {

     return (
        <Form.Select>
           {countryCode.map((country) => (
            <option value={country.dial_code} key={country.name}>
            {country.dial_code}</option>
           ))}
        </Form.Select>
    )

}

export default CountryCodeSelect