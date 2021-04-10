import React from "react";
import styles from "./styles.module.scss";
import propTypes from "prop-types";

class Footer extends React.Component {
    static contextTypes = {
        t: propTypes.func.isRequired
    };
    render() {
        console.log(this.context)
        return (
            <footer className={styles.footer}>
                <div className={styles.column}>
                    <nav className={styles.nav}>
                        <ul className={styles.list}>
                            <li className={styles.listItem}>{this.context.t("About Us")}</li>
                            <li className={styles.listItem}>{this.context.t("Support")}</li>
                            <li className={styles.listItem}>{this.context.t("Blog")}</li>
                            <li className={styles.listItem}>{this.context.t("Press")}</li>
                            <li className={styles.listItem}>{this.context.t("API")}</li>
                            <li className={styles.listItem}>{this.context.t("Jobs")}</li>
                            <li className={styles.listItem}>{this.context.t("Privacy")}</li>
                            <li className={styles.listItem}>{this.context.t("Terms")}</li>
                            <li className={styles.listItem}>{this.context.t("Directory")}</li>
                            <li className={styles.listItem}>{this.context.t("Language")}</li>
                        </ul>
                    </nav>
                </div>
                <div className={styles.column}>
                    <span className={styles.copyright}>© 2021 Toss</span>
                </div>
            </footer>
        )
    }
}

export default Footer;
