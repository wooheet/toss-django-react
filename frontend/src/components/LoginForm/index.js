import { connect } from "react-redux";
import Container from "./container";
import { actionCreators as contractActions } from "redux/modules/contract";

const mapDispatchToProps = (dispatch, ownProps) => {
  return {
    usernameLogin: (username, email) => {
      dispatch(contractActions.usernameLogin(username, email));
    }
  };
};

export default connect(null, mapDispatchToProps)(Container);
