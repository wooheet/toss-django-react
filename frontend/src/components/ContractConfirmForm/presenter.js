import React from "react";
import PropTypes from "prop-types";
import formStyles from "shared/formStyles.module.scss";

const ContractConfirmForm = (props, context) => (
  <div className={formStyles.formComponent}>
    <h3 className={formStyles.signupHeader}>
      {context.t("Confirm Contract")}
    </h3>
    <span className={formStyles.divider}>o</span>
    <form className={formStyles.form} onSubmit={props.handleSubmit}>
        <p className={formStyles.terms}>
          {context.t("Contract ID")}
        </p>
      <input
        type="text"
        placeholder={context.t("Contract ID")}
        className={formStyles.textInput}
        value={props.emailValue}
        onChange={props.handleInputChange}
        name="contractId"
      />
      <p className={formStyles.terms}>
          {context.t("Contractor")}
      </p>
      <input
        type="text"
        placeholder={context.t("Contractor")}
        className={formStyles.textInput}
        value={props.fullNameValue}
        onChange={props.handleInputChange}
        name="contractor"
      />
      <p className={formStyles.terms}>
          {context.t("Email")}
      </p>
      <input
        type="email"
        placeholder={context.t("Email")}
        className={formStyles.textInput}
        value={props.usernameValue}
        onChange={props.handleInputChange}
        name="email"
      />
      <p className={formStyles.terms}>
          {context.t("Term")}
      </p>
      <input
        type="text"
        placeholder={context.t("Term")}
        className={formStyles.textInput}
        value={props.passwordValue}
        onChange={props.handleInputChange}
        name="term"
      />
      <p className={formStyles.terms}>
          {context.t("Article")}
      </p>
      <input
        type="text"
        placeholder={context.t("Article")}
        className={formStyles.textInput}
        value={props.passwordValue}
        onChange={props.handleInputChange}
        name="article"
      />
      <p className={formStyles.terms}>
          {context.t("Associate Contract")}
      </p>
      <input
        type="text"
        placeholder={context.t("Associate Contract")}
        className={formStyles.textInput}
        value={props.passwordValue}
        onChange={props.handleInputChange}
        name="associate"
      />
    </form>
  </div>
);

ContractConfirmForm.propTypes = {
  contractIdValue: PropTypes.string.isRequired,
  contractorValue: PropTypes.string.isRequired,
  emailValue: PropTypes.string.isRequired,
  termValue: PropTypes.string.isRequired,
  articleValue: PropTypes.string.isRequired,
  associateValue: PropTypes.string.isRequired,
  handleInputChange: PropTypes.func.isRequired,
  handleSubmit: PropTypes.func.isRequired,
};

ContractConfirmForm.contextTypes = {
  t: PropTypes.func.isRequired
};

export default ContractConfirmForm;
