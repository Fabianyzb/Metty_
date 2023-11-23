import {Link} from 'react-router-dom'

const Start = () => {
  return (
    <>
      <div className="centrado">

        <p className='h-6'>Esta es la página de inicio que lo deriva a crear cuenta o inciar sesion</p>
        
        <Link to='/create-acount' className='button-text-large'>¡Comenzar ahora!</Link>
        <Link to='/login'>Ya tengo una cuenta</Link> 
     

      </div>
    </>
  )
}

export default Start
