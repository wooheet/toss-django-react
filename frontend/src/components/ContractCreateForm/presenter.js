import React from "react";
import PropTypes from "prop-types";
import formStyles from "shared/formStyles.module.scss";

const ContractCreateForm = (props, context) => (
  <div className={formStyles.formComponent}>
    <h3 className={formStyles.signupHeader}>
      {context.t("Create Contract")}
    </h3>
    <span className={formStyles.divider}>o</span>
    <form className={formStyles.form} onSubmit={props.handleSubmit}>
      <input
        type="text"
        placeholder={context.t("Contractor")}
        className={formStyles.textInput}
        onChange={props.handleInputChange}
        name="username"
        value={props.usernameValue}
      />
      <input
        type="email"
        placeholder={context.t("Email")}
        className={formStyles.textInput}
        onChange={props.handleInputChange}
        name="email"
        value={props.emailValue}
      />
      <input
        type="submit"
        value={context.t("계약 조항 추가")}
        className={formStyles.button}
        onChange={props.handleInputChange}
        onClick={props.changeAction}
      />
    </form>

  </div>
);

ContractCreateForm.propTypes = {
  handleInputChange: PropTypes.func.isRequired,
  usernameValue: PropTypes.string.isRequired,
  emailValue: PropTypes.string.isRequired,
  handleSubmit: PropTypes.func.isRequired,
};

ContractCreateForm.contextTypes = {
  t: PropTypes.func.isRequired
};

export default ContractCreateForm;
