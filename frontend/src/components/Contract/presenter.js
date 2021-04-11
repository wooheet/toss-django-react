import React from 'react';
import styles from "./styles.module.scss";
import ContractCreateForm from "components/ContractCreateForm";
import ContractConfirmForm from "components/ContractConfirmForm";

const Contract = (props, context) => (
    <main className={styles.auth}>

        <div className={styles.column}>
            <div className={`${styles.whiteBox} ${styles.formBox}`}>
                <img src="https://static.toss.im/tds/icon/svg/logo.svg" alt="logo" width={95}/>
                {props.action === "contract" && <ContractCreateForm />}
                {props.action === "confirm" && <ContractConfirmForm />}
            </div>
            <div className={styles.whiteBox}>
                {props.action === "contract" && (
                    <p className={styles.text}>
                        <span className={styles.changeLink} onClick={props.changeAction}>
                            조회
                        </span>
                    </p>
                )}
                {props.action === "confirm" &&(
                    <p className={styles.text}>
                        <span className={styles.changeLink} onClick={props.changeAction}>
                            생성하기
                        </span>
                    </p>
                )}
            </div>
        </div>
    </main>
);

export default Contract;
