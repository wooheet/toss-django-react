import React, { Component } from "react";
import PropTypes from "prop-types";
import SignupForm from "./presenter";

class Container extends Component {
  state = {
    email: "",
    fullName: "",
    username: "",
    password: ""
  };
  static propTypes = {
    createAccount: PropTypes.func.isRequired
  };
  render() {
    const { email, fullName, username, password } = this.state;
    return (
      <SignupForm
        emailValue={email}
        fullNameValue={fullName}
        usernameValue={username}
        passwordValue={password}
        handleInputChange={this._handleInputChange}
        handleSubmit={this._handleSubmit}
      />
    );
  }
  _handleInputChange = event => {
    const { target: { value, name } } = event;
    this.setState({
      [name]: value
    });
  };
  _handleSubmit = event => {
    const { username, password, email } = this.state;
    const { createAccount } = this.props;
    event.preventDefault();
    createAccount(username, password, email);
  };
}

export default Container;
