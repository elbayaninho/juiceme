import { Form } from "react-bootstrap"
import  './index.scss'
import countryCode from  './countries-code.json'
import { SetStateAction } from "react"
import { IUser } from "../Shared/types/IUser"
interface ICountryCodeSelect{
   formData: IUser,
   setFormData: React.Dispatch<SetStateAction<IUser>> ,
   value: string
}
const CountryCodeSelect = ({setFormData, formData, value}: ICountryCodeSelect) => {

     return (
        <Form.Select onChange={(e) => setFormData({...formData, countryCode: e.target.value})} value={value}>
           {countryCode.map((country) => (
            <option value={country.dial_code} key={country.name}>
            {country.dial_code}</option>
           ))}
        </Form.Select>
    )

}

export default CountryCodeSelect