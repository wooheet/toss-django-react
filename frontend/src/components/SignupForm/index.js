import { connect } from "react-redux";
import Container from "./container";
import { actionCreators as userActions } from "redux/modules/contract";

const mapDispatchToProps = (dispatch, ownProps) => {
  return {
    createAccount: (username, password, email) => {
      dispatch(userActions.createAccount(username, password, email));
    }
  };
};

export default connect(null, mapDispatchToProps)(Container);
