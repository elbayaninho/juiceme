import { Badge } from "react-bootstrap"
import  Sage300  from '../../assets/Sage300.svg'
import SAP  from '../../assets/SAP.svg'
import PAYSPACE  from '../../assets/Payspace.svg'
import  Workday  from '../../assets/workday.svg'
import {MdOutlineSecurity} from 'react-icons/md'
import {BsBank} from 'react-icons/bs'
import './index.scss'

const SoftwareAddOn = () => {

    interface SoftwareAddOn {
        name: string,
        img: string,
    }

    const softwares: SoftwareAddOn[] = [
        {
            name: "Sage300",
            img: Sage300
        },
        {
            name: "SAP",
            img: SAP
        },
        {
            name: "PAYSPACE",
            img: PAYSPACE
        },
        {
            name: "Workday",
            img: Workday
        },
    ]

    return (
        <div id="software-add-on">
            <div>
            <Badge>A software add-on</Badge>
            <h4>Juiceme works with all HR systems</h4>
            <h6>Juiceme is an HR & Payroll add-on, compatible with any system to enhance its functionalities. </h6>
            </div>
            <div>
                {softwares.map((element, index) =>(
                 <img src={element.img} alt={element.name} key={index}/>
                ))}
            </div>

            <div>
                <div>
                    <h5><BsBank/> Bank Level Security</h5>
                    <p>All application traffic is encrypted and protected by using 256-bit AES bank level encryption. This provides security between devices and our servers ensuring personal and transactional details are always kept private.</p>
                </div>

                <div>
                    <h5> <MdOutlineSecurity/> Data Privacy</h5>
                    <p>We prioritize protecting your data. Our secure servers ensure that no third party is granted access to your personal information. We collect and use your personal data to constantly improve your user experience.</p>
                </div>
            </div>
        </div>
    )
}

export default SoftwareAddOn