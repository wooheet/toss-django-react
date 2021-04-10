import { connect } from "react-redux";
import { actionCreators as photoActions } from "redux/modules/photos";
import Container from "./container";

const mapStateToProps = (state, ownProps) => {
  // const { photos: { feed } } = state;
  // return {
  //   feed
  // };
  return null;
};

const mapDispatchToProps = (dispatch, ownProps) => {
  return {
    getFeed: () => {
      dispatch(photoActions.getFeed());
    }
  };
};

export default connect(mapStateToProps, mapDispatchToProps)(Container);
