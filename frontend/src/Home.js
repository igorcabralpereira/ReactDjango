import React, { Component } from 'react';
import logo from './homepage.svg';

export class Home extends Component {
    render() {
        return (
            <div>
                <br/>
                <h5>Welcome to Homepage</h5>
                <img src={logo} />
            </div>
        )
    }
}

export default Home;