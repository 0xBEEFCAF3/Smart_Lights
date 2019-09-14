import React, { Component } from 'react';
import { SketchPicker  } from 'react-color';
import reactCSS from 'reactcss'
import axios from 'axios';


import './App.css';

class App extends Component {
  state = {
    BE_URL: window.location.hostname,
    BE_port:5000,
    displayColorPicker: false,
    color: {
      r: '241',
      g: '112',
      b: '19',
      a: '1',
    },
  };

  constructor(){
    super();
  }

  handleClick = () => {
    this.setState({ displayColorPicker: !this.state.displayColorPicker })
  };

  handleClose = () => {
    this.setState({ displayColorPicker: false })
  };

  handleChange = (color) => {
    this.setState({ color: color.rgb })
  };

  handleSetColor = () => {
    const r = this.state.color.r;
    const g = this.state.color.g;
    const b = this.state.color.b;
    console.log('http://'+this.state.BE_URL+':'+this.state.BE_port);
    axios.get('http://'+this.state.BE_URL+':'+this.state.BE_port+'/rgb/'+r+'/'+g+'/'+b)
      .then(function (response) {
        console.log(response);
      })
      .catch(function (error) {
        console.log(error);
      });

  }

  handleOn = () => {
    console.log('http://'+this.state.BE_URL+':'+this.state.BE_port);
    axios.get('http://'+this.state.BE_URL+':'+this.state.BE_port+'/on')
      .then(function (response) {
        console.log(response);
      })
      .catch(function (error) {
        console.log(error);
      });

  }

  handleOff = () => {
    console.log('http://'+this.state.BE_URL+':'+this.state.BE_port);
    axios.get('http://'+this.state.BE_URL+':'+this.state.BE_port+'/off')
      .then(function (response) {
        console.log(response);
      })
      .catch(function (error) {
        console.log(error);
      });

  }

  handleBlueify = () => {
    axios.get('http://'+this.state.BE_URL+':'+this.state.BE_port+'/blueify')
      .then(function (response) {
        console.log(response);
      })
      .catch(function (error) {
        console.log(error);
      });

  }

  handleRedify = () => {
    axios.get('http://'+this.state.BE_URL+':'+this.state.BE_port+'/redify')
      .then(function (response) {
        console.log(response);
      })
      .catch(function (error) {
        console.log(error);
      });

  }

  handleGreenify = () => {
    axios.get('http://'+this.state.BE_URL+':'+this.state.BE_port+'/greenify')
      .then(function (response) {
        console.log(response);
      })
      .catch(function (error) {
        console.log(error);
      });

  }

  handleYellowify = () => {
    axios.get('http://'+this.state.BE_URL+':'+this.state.BE_port+'/yellowify')
      .then(function (response) {
        console.log(response);
      })
      .catch(function (error) {
        console.log(error);
      });

  }

  handleMagentify = () => {
    axios.get('http://'+this.state.BE_URL+':'+this.state.BE_port+'/magentify')
      .then(function (response) {
        console.log(response);
      })
      .catch(function (error) {
        console.log(error);
      });

  }

  handleCyanify = () => {
    axios.get('http://'+this.state.BE_URL+':'+this.state.BE_port+'/cyanify')
      .then(function (response) {
        console.log(response);
      })
      .catch(function (error) {
        console.log(error);
      });

  }

  handleRainbow = () => {
    axios.get('http://'+this.state.BE_URL+':'+this.state.BE_port+'/rainbow')
      .then(function (response) {
        console.log(response);
      })
      .catch(function (error) {
        console.log(error);
      });
  }

  exHandleRainbow = () => {                                                                                     
    axios.get('http://'+this.state.BE_URL+':'+this.state.BE_port+'/exrainbow')                                  
      .then(function (response) {                                                                               
        console.log(response);                                                                                  
      })                                                                                                        
      .catch(function (error) {                                                                                   
        console.log(error);                                                                                      
      });                                                                                                        
  }

  render() {
    const styles = reactCSS({
      'default': {
        color: {
          width: '100px',
          height: '70px',
          borderRadius: '2px',
          background: `rgba(${ this.state.color.r }, ${ this.state.color.g }, ${ this.state.color.b }, ${ this.state.color.a })`,
        },
        swatch: {
          padding: '5px',
          background: '#fff',
          borderRadius: '1px',
          boxShadow: '0 0 0 1px rgba(0,0,0,.1)',
          display: 'inline-block',
          cursor: 'pointer',
        },
        popover: {
          position: 'absolute',
          zIndex: '2',
        },
        cover: {
          position: 'fixed',
          top: '0px',
          right: '0px',
          bottom: '0px',
          left: '0px',
        },
      },
    });
    return (
      <div className="App">
         <div className="page-header"> <h1> Welcome to ArmLights </h1></div>
         <div className="container picker">
	  <span> <b> R : {this.state.color.r} | G : {this.state.color.g} | B : {this.state.color.b} </b> </span>
          <div>
            <div style={ styles.swatch } onClick={ this.handleClick }>
              <div style={ styles.color } />
            </div>
              { this.state.displayColorPicker ? <div style={ styles.popover }>
            <div style={ styles.cover } onClick={ this.handleClose }/>
              <SketchPicker color={ this.state.color } onChange={ this.handleChange } />
            </div> : null }
            </div>
         </div>
        <div className="btn-group">
          <button className="btn btn-primary" onClick={ this.handleSetColor }> Set Color </button>
          <button className="btn btn-primary" onClick={ this.handleOn }> ON </button>
          <button className="btn btn-primary" onClick={ this.handleOff }> OFF </button>
        </div>
        <br />
        <div className="btn-group">
          <button className="btn btn-success" onClick={ this.handleGreenify }> Greenify </button>
          <button className="btn btn-danger" onClick={ this.handleRedify }> Redify </button>
          <button className="btn btn-info" onClick={ this.handleBlueify }> Blueify </button>
        </div>
        <br />
        <div className="btn-group">
          <button className="btn btn-primary" onClick={ this.handleYellowify }> Yellowify </button>
          <button className="btn btn-primary" onClick={ this.handleMagentify }> Magentify </button>
          <button className="btn btn-primary" onClick={ this.handleCyanify }> Cyanify </button>
        </div>
        <br />
        <div className="btn-group">
          <button className="btn btn-primary" onClick={ this.handleRainbow }> Vibeify </button>
          <button className="btn btn-primary" onClick={ this.exHandleRainbow }> Extra-Vibeify </button>
        </div>
      </div>
    );
  }
}

export default App;
