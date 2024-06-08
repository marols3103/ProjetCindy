import { NavLink } from 'react-router-dom';
import '../../css/nav.css';
export default function Nav(){
   return(
    <>
        <div className='row shadow'>
            <div className='col-sm-1' ></div>
            <div className='col-sm-4 text-center'>
                <img src='./logo_fstm.png' id='logo'></img>
            </div>
            <div className='image2 col-sm-4 text-center'>
                <img src='./Logo_UHIIC.png' id='logo'></img>
            </div>
            
        </div>
        <div className='row'>
            <div className='col-sm-6'></div>
            <div className='col-sm-6'>
                <nav>

                    <ul>
                        <li><NavLink to ="/">home</NavLink></li>
                        <li><NavLink to= "/interfaceViews">Demonstration</NavLink></li>
                       
                        
                    </ul>
                    
                </nav>
            </div>
           
        </div>
    </>
        
       
   ) ;
}