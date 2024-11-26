import PropTypes from "prop-types";
import styles from "./PasswordLabels.module.css";

const PasswordLabels = ({ className = "" }) => {
  return (
    <div className={[styles.passwordLabels, className].join(" ")}>
      <div className={styles.memberType}>
        <div className={styles.memberTypeOptions}>
          <div className={styles.membershipTypesParent}>
            <div className={styles.membershipTypes}>
              <div className={styles.membershipTypeLabels}>
                <img
                  className={styles.membershipTypeLabelsChild}
                  loading="lazy"
                  alt=""
                  src="/group-15.svg"
                />
                <div className={styles.membershipNames}>
                  <div className={styles.div}>개인 회원</div>
                </div>
              </div>
              <div className={styles.membershipTypeLabels1}>
                <img
                  className={styles.membershipTypeLabelsChild}
                  loading="lazy"
                  alt=""
                  src="/ellipse-4.svg"
                />
                <div className={styles.membershipNames}>
                  <div className={styles.div}>디자이너 회원</div>
                </div>
              </div>
            </div>
            <h3 className={styles.information}>Information</h3>
          </div>
          <div className={styles.requiredLabel}>
            <div className={styles.div}>*필수입력사항</div>
          </div>
        </div>
        <div className={styles.idInput}>
          <input
            className={styles.input}
            placeholder="아이디 * (영문소문자/숫자, 4~16자)"
            type="text"
          />
          <div className={styles.idInputChild} />
        </div>
      </div>
      <div className={styles.idInput}>
        <input
          className={styles.input1}
          placeholder="비밀번호 * (영문 대소문자/숫자/특수문자 중 2가지 이상 조합, 8자~16자)"
          type="text"
        />
        <div className={styles.idInputChild} />
      </div>
      <div className={styles.passwordLabelValues1}>
        <input
          className={styles.input2}
          placeholder="비밀번호 확인 *"
          type="text"
        />
        <div className={styles.idInputChild} />
      </div>
      <div className={styles.passwordLabelValues1}>
        <input className={styles.input3} placeholder="이름 *" type="text" />
        <div className={styles.idInputChild} />
      </div>
      <div className={styles.phoneInput}>
        <div className={styles.phoneFields}>
          <input
            className={styles.phoneNumberValues}
            placeholder="010"
            type="text"
          />
          <div className={styles.phoneFieldsChild} />
        </div>
        <div className={styles.phoneFields1}>
          <div className={styles.div3}>-</div>
        </div>
        <div className={styles.phoneFields2}>
          <input
            className={styles.input4}
            placeholder="휴대전화*"
            type="text"
          />
          <div className={styles.phoneFieldsItem} />
        </div>
        <div className={styles.phoneFields1}>
          <div className={styles.div3}>-</div>
        </div>
        <input className={styles.phoneInputChild} type="text" />
      </div>
      <div className={styles.passwordLabelValues1}>
        <input className={styles.input5} placeholder="이메일 *" type="text" />
        <div className={styles.idInputChild} />
      </div>
    </div>
  );
};

PasswordLabels.propTypes = {
  className: PropTypes.string,
};

export default PasswordLabels;
