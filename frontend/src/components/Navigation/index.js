import { connect } from "react-redux";
import Container from "./container";
import { actionCreators as userActions } from "redux/modules/user";


const mapDispatchToProps = (dispatch, ownProps) => {
  return {
    goToSearch: searchTerm => {
      dispatch(userActions.searchByTerm(searchTerm));
    }
  };
};

export default connect(null, mapDispatchToProps)(Container);
