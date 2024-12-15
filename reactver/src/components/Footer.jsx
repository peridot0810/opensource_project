import { useMemo } from "react";
import PropTypes from "prop-types";
import styles from "./Footer.module.css";

const Footer = ({
  className = "",
  footerMarginLeft,
  hELPMENUTextDecoration,
  badge,
  badge1,
  badge2,
  badge3,
  badge4,
}) => {
  const footerStyle = useMemo(() => {
    return {
      marginLeft: footerMarginLeft,
    };
  }, [footerMarginLeft]);

  const hELPMENUStyle = useMemo(() => {
    return {
      textDecoration: hELPMENUTextDecoration,
    };
  }, [hELPMENUTextDecoration]);

  return (
    <footer
      className={[styles.footer, className].join(" ")}
      style={footerStyle}
    >
      <div className={styles.footerChild} />
      <div className={styles.helpMenuContainer}>
        <div className={styles.fitMeDescription}>
          <h1 className={styles.fitme}>Fit.Me</h1>
          <div className={styles.descriptionContent}>
            <div className={styles.youCanVirtually}>
              You can virtually try on any outfit you want online.
            </div>
            <div className={styles.ellipsisContainer}>
              <img
                className={styles.dotsIcon}
                loading="lazy"
                alt=""
                src="/1.svg"
              />
              <img
                className={styles.dotsIcon}
                loading="lazy"
                alt=""
                src="/2.svg"
              />
              <img
                className={styles.dotsIcon}
                loading="lazy"
                alt=""
                src="/3.svg"
              />
              <img
                className={styles.dotsIcon}
                loading="lazy"
                alt=""
                src="/4.svg"
              />
            </div>
          </div>
        </div>
        <div className={styles.helpMenuImage}>
          <div className={styles.helpMenuContent}>
            <div className={styles.helpMenu}>APP</div>
          </div>
          <div className={styles.imageContainer}>
            <img className={styles.imageIcon} alt="" src="/image-5@2x.png" />
          </div>
          <div className={styles.aboutFeaturesWorksContainer}>
            <p className={styles.youCanQuickly}>{`You can quickly receive `}</p>
            <p className={styles.youCanQuickly}>{`notifications about `}</p>
            <p className={styles.youCanQuickly}>various benefits.</p>
          </div>
        </div>
        <div className={styles.helpMenuImage}>
          <div className={styles.helpMenu}>Help</div>
          <div className={styles.aboutFeaturesWorksContainer1}>
            <p className={styles.youCanQuickly}>Customer Support</p>
            <p className={styles.youCanQuickly}>&nbsp;</p>
            <p className={styles.youCanQuickly}>Delivery Details</p>
            <p className={styles.youCanQuickly}>&nbsp;</p>
            <p className={styles.youCanQuickly}>{`Terms & Conditions`}</p>
            <p className={styles.youCanQuickly}>&nbsp;</p>
            <p className={styles.youCanQuickly}>Privacy Policy</p>
          </div>
        </div>
        <div className={styles.helpMenuTitles1}>
          <a className={styles.helpMenu2} style={hELPMENUStyle}>
            FAQ
          </a>
          <div className={styles.aboutFeaturesWorksContainer2}>
            <p className={styles.youCanQuickly}>Account</p>
            <p className={styles.youCanQuickly}>&nbsp;</p>
            <p className={styles.youCanQuickly}>Manage Deliveries</p>
            <p className={styles.youCanQuickly}>&nbsp;</p>
            <p className={styles.youCanQuickly}>Orders</p>
            <p className={styles.youCanQuickly}>&nbsp;</p>
            <p className={styles.youCanQuickly}>Payments</p>
          </div>
        </div>
      </div>
      <div className={styles.footerItem} />
      <div className={styles.copyrightAndBadges}>
        <div className={styles.copyright}>
          <div className={styles.allRightsReserved}>
            Shop.co © 2024-2034, All Rights Reserved
          </div>
        </div>
        <div className={styles.ellipsisContainer}>
          <img className={styles.badgeIcon} loading="lazy" alt="" src={badge} />
          <img className={styles.badgeIcon} alt="" src={badge1} />
          <img className={styles.badgeIcon} alt="" src={badge2} />
          <img className={styles.badgeIcon} alt="" src={badge3} />
          <img className={styles.badgeIcon} alt="" src={badge4} />
        </div>
      </div>
    </footer>
  );
};

Footer.propTypes = {
  className: PropTypes.string,
  badge: PropTypes.string,
  badge1: PropTypes.string,
  badge2: PropTypes.string,
  badge3: PropTypes.string,
  badge4: PropTypes.string,

  /** Style props */
  footerMarginLeft: PropTypes.string,
  hELPMENUTextDecoration: PropTypes.string,
};

export default Footer;
