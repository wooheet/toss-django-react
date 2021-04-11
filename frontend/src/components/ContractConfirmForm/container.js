import React, { Component } from "react";
import PropTypes from "prop-types";
import ContractConfirmForm from "./presenter";

class Container extends Component {
  state = {
    email: "",
    fullName: "",
    username: "",
    password: ""
  };
  render() {
    const { email, fullName, username, password } = this.state;
    return (
      <ContractConfirmForm
        emailValue={email}
        fullNameValue={fullName}
        usernameValue={username}
        passwordValue={password}
        handleInputChange={this._handleInputChange}
      />
    );
  }
  _handleInputChange = event => {
    const { target: { value, name } } = event;
    this.setState({
      [name]: value
    });
  };
}

export default Container;
