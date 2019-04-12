import logo from './assets/banner1.jpg';
import React, { Component } from 'react';
import zIndex from '@material-ui/core/styles/zIndex';

function Header() {
  return <img style={{position:"absolute", top:0, left:0, right:0, width:"100%", height:"100%", zIndex:-1}} src={logo} alt="Logo" />;
}

export default Header;