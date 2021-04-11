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
    const { contractId, contractor, email, term, article, associate } = this.state;
    return (
      <ContractConfirmForm
        contractIdValue={contractId}
        contractorValue={contractor}
        emailValue={email}
        termValue={term}
        articleValue={article}
        associateValue={associate}
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
