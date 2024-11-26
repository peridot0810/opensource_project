import FrameComponent from "../components/FrameComponent";
import NavigationPanel from "../components/NavigationPanel";
import Footer from "../components/Footer";
import styles from "./CategoryPage.module.css";

const CategoryPage = () => {
  return (
    <div className={styles.categoryPage}>
      <FrameComponent
        frame="/frame.svg"
        frame1="/frame-1.svg"
        frame2="/frame-2.svg"
      />
      <main className={styles.mainContentWrapper}>
        <section className={styles.mainContent}>
          <NavigationPanel />
          <div className={styles.virtualTryonBanner}>
            <h1 className={styles.h1}>
              <span>
                <span>{`👕 어울릴지 고민된다면? → `}</span>
                <span className={styles.span}>가상 피팅</span>
                <span className={styles.span1}>{`으로 확인해요! 🩳  `}</span>
              </span>
            </h1>
          </div>
        </section>
      </main>
      <Footer
        badge="/badge.svg"
        badge1="/badge-1.svg"
        badge2="/badge-2.svg"
        badge3="/badge-3.svg"
        badge4="/badge-4.svg"
      />
    </div>
  );
};

export default CategoryPage;
