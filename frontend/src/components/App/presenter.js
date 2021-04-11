import React from 'react';
import propTypes from "prop-types";
import { Route, Switch } from "react-router-dom";
import './styles.module.scss';
import Contract from "components/Contract";
import ContractConfirm from "components/ContractConfirmForm";

const App = props => [
  props.isLoggedIn ? <PrivateRoutes key={2} /> : <PublicRoutes key={2} />
];

App.propTypes = {
  isLoggedIn: propTypes.bool.isRequired
};

const PrivateRoutes = props => (
  <Switch>
    <Route exact path = "/" component = { ContractConfirm } />
  </Switch>
);

const PublicRoutes = props => (
  <Switch>
    <Route exact path = "/" component = { Contract } />
  </Switch>
);

export default App;
