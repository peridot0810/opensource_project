import TopFirst from "../components/TopFirst";
import BodyFirst from "../components/BodyFirst";
import ProductFirst from "../components/ProductFirst";
import TopSelling from "../components/TopSelling";
import Footer from "../components/Footer";
import styles from "./Homepage.module.css";

const Homepage = () => {
  return (
    <div className={styles.homepage}>
      <img className={styles.homepageChild} alt="" src="/rectangle-2@2x.png" />
      <div className={styles.frameParent}>
        <div className={styles.parent}>
          <div className={styles.div}>200+</div>
          <div className={styles.internationalBrands}>International Brands</div>
        </div>
        <div className={styles.frameChild} />
        <div className={styles.parent}>
          <div className={styles.div}>2,000+</div>
          <div className={styles.internationalBrands}>
            High-Quality Products
          </div>
        </div>
        <div className={styles.frameChild} />
        <div className={styles.parent}>
          <div className={styles.div}>30,000+</div>
          <div className={styles.internationalBrands}>Happy Customers</div>
        </div>
      </div>
      <img
        className={styles.image53Icon}
        loading="lazy"
        alt=""
        src="/image-52@2x.png"
      />
      <section className={styles.homepageTop}>
        <TopFirst />
        <BodyFirst />
      </section>
      <section className={styles.rectangleParent}>
        <div className={styles.frameInner} />
        <h1 className={styles.h1}>
          마이페이지에 내 사진 등록하고 가상 피팅해보세요!
        </h1>
      </section>
      <section className={styles.newArrivalFirstWrapper}>
        <div className={styles.newArrivalFirst}>
          <div className={styles.newArrivalTitle}>
            <h1 className={styles.newArrivals}>NEW ARRIVALS</h1>
          </div>
          <ProductFirst />
          <div className={styles.newArrivalFirstChild} />
          <TopSelling />
        </div>
      </section>
      <Footer
        footerMarginLeft="unset"
        hELPMENUTextDecoration="none"
        badge="/badge2.svg"
        badge1="/badge-12.svg"
        badge2="/badge-22.svg"
        badge3="/badge-32.svg"
        badge4="/badge-42.svg"
      />
    </div>
  );
};

export default Homepage;
