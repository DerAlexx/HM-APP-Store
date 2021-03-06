import SearchAppBar from "./MenueBar.js";
import SideNavPage from "./SideNavigation"
import SimpleCardNotPopular from "./Cards_notpopular"
import logo from "./assets/apps_banner.jpg"
import ButtonDrop from "./ButtonDropdown"
import React from "react";

export default class AppShowNotPopular extends React.Component{
  render(){
    return (
    <div> 
      <SearchAppBar/>
      <SideNavPage/>
      <img style={{position:"absolute", top:0, left:0, right:0, width:"100%", height:"60%", zIndex:-1}} src={logo} alt="Logo" />;
      <div style = {{position: "absolute", top:'70%', left:'15%', right:'15%'}}>
        <h1 style={{textAlign: 'center', fontFamily: 'Montserrat', paddingTop: 0, color:'#fff'}}>Unsere Apps</h1>
        <ButtonDrop/>  
        <hr style={{backgroundColor:'#fff'}}></hr>
        <br></br><br></br>
        <SimpleCardNotPopular/> 
      </div> 
    </div>
    )
  }
} 