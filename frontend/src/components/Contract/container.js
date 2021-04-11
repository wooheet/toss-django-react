import React, { Component } from "react";
import Contract from './presenter';

class Container extends Component {
    state = {
        action : "contract"
    };
    render(){
        const { action } = this.state;
        return <Contract action={action} changeAction={this._changeAction}/>;
    }
    _changeAction = () => {
        this.setState(prevState => {
            const { action } = prevState;
            if(action === "contract"){
                return {
                    action: "confirm"
                };
            } else if(action === "confirm"){
                return {
                    action: "contract"
                };
            }
        });
    };
}

export default Container;
