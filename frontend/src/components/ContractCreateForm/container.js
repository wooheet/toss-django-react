import React, { Component } from "react";
import PropTypes from "prop-types";
import ContractCreateForm from "./presenter";

class Container extends Component {
  state = {
    username: "",
    email: ""
  };
  static propTypes = {
    usernameLogin: PropTypes.func.isRequired
  };
  render() {
    const { username, email } = this.state;
    return (
      <ContractCreateForm
        handleInputChange={this._handleInputChange}
        handleSubmit={this._handleSubmit}
        usernameValue={username}
        emailValue={email}
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
    const { usernameLogin } = this.props;
    const { username, email } = this.state;
    event.preventDefault();
    usernameLogin(username, email);
  };
}

export default Container;
