import React from 'react';
import { useNavigate } from 'react-router-dom';
import classes from "./area.module.css";

import mockPhoto from "../assets/image 3.png";


const AreaPhoto = ({link,imgPath,active,name,floors}) => {
    
    const navigate = useNavigate();

    const handleClick = () => {
      navigate(link,{state:{active:active , floors:floors}});
    };
        
    return(<div className={classes.area} onClick={handleClick}>
        <div className={classes.name}>{name}</div>
        <img src={imgPath} className={classes.imageArea}></img>
        {active ? <div className={classes.here}>You are here!</div> : null}
    </div>)
}

export default AreaPhoto;