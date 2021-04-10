import React from 'react';
import styles from "./styles.module.scss";
// import { LoginForm, SignupForm } from 'components/AuthForms'
import { SignupForm } from 'components/AuthForms'
import LoginForm from "components/LoginForm";
// import SignupForm from "components/SignupForm";

const Auth = (props, context) => (
    <main className={styles.auth}>

        <div className={styles.column}>
            <div className={`${styles.whiteBox} ${styles.formBox}`}>
                <img src="https://static.toss.im/tds/icon/svg/logo.svg" alt="logo" width={95}/>
                {props.action === "login" && <LoginForm />}
                {props.action === "signup" && <SignupForm />}
            </div>
            <div className={styles.whiteBox}>
                {props.action === "login" && (
                    <p className={styles.text}>
                        Don't have an account?{" "}
                        <span className={styles.changeLink} onClick={props.changeAction}>
                            Sign up
                        </span>
                    </p>
                )}
                {props.action === "signup" &&(
                    <p className={styles.text}>
                        Have an account?{" "}
                        <span className={styles.changeLink} onClick={props.changeAction}>
                            Log in
                        </span>
                    </p>
                )}
            </div>
        </div>
    </main>
);

export default Auth;
