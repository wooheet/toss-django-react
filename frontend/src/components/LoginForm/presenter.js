import React from "react";
import PropTypes from "prop-types";
import formStyles from "shared/formStyles.module.scss";

const LoginForm = (props, context) => (
  <div className={formStyles.formComponent}>
    <form
      className={formStyles.form}
      onSubmit={props.handleSubmit}
      method="post"
    >
      <input
        type="text"
        placeholder={context.t("Username")}
        className={formStyles.textInput}
        onChange={props.handleInputChange}
        name="username"
        value={props.usernameValue}
      />
      <input
        type="password"
        placeholder={context.t("Password")}
        className={formStyles.textInput}
        onChange={props.handleInputChange}
        name="password"
        value={props.passwordValue}
      />
      <input
        type="submit"
        value={context.t("Log in")}
        className={formStyles.button}
      />
    </form>
    <span className={formStyles.divider}>{context.t("or")}</span>
    <span className={formStyles.forgotLink}>
      {context.t("Forgot password?")}
    </span>
  </div>
);

LoginForm.propTypes = {
  handleInputChange: PropTypes.func.isRequired,
  usernameValue: PropTypes.string.isRequired,
  passwordValue: PropTypes.string.isRequired,
  handleSubmit: PropTypes.func.isRequired,
  handleFacebookLogin: PropTypes.func.isRequired
};

LoginForm.contextTypes = {
  t: PropTypes.func.isRequired
};

export default LoginForm;
