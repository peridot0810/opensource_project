import { useCallback } from "react";
import FrameComponent from "../components/FrameComponent";
import FrameComponent2 from "../components/FrameComponent2";
import Footer from "../components/Footer";
import styles from "./ProductDetailPage.module.css";

const ProductDetailPage = () => {
  const onFrameContainerClick = useCallback(() => {
    // Please sync "VTON1" to the project
  }, []);

  return (
    <div className={styles.productDetailPage}>
      <FrameComponent
        frame="/frame1.svg"
        frame1="/frame-11.svg"
        frame2="/frame-21.svg"
      />
      <main className={styles.productDetailPageInner}>
        <section className={styles.frameParent}>
          <FrameComponent2 />
          <div className={styles.frameGroup}>
            <div className={styles.tryonMessageWrapper}>
              <div className={styles.tryonMessage}>
                <b className={styles.b}>
                  <span className={styles.txt}>
                    <span
                      className={styles.span}
                    >{`이 옷, 내 스타일일까..🤔?                       `}</span>
                    <span className={styles.span1}>{`미리 입어보기 `}</span>
                    <span>→</span>
                  </span>
                </b>
                <div
                  className={styles.virtualTryonButtonWrapper}
                  onClick={onFrameContainerClick}
                >
                  <div className={styles.virtualTryonButton}>
                    <div className={styles.virtualTryOnWrapper}>
                      <div className={styles.virtualTryOn}>Virtual Try on</div>
                    </div>
                  </div>
                </div>
              </div>
            </div>
            <div className={styles.frameWrapper}>
              <div className={styles.frameContainer}>
                <div className={styles.detailsAndReviewsLinksWrapper}>
                  <div className={styles.detailsAndReviewsLinks}>
                    <div className={styles.productDetails}>Product Details</div>
                    <div className={styles.ratingReviewsWrapper}>
                      <div
                        className={styles.ratingReviews}
                      >{`Rating & Reviews`}</div>
                    </div>
                    <div className={styles.faqs}>FAQs</div>
                  </div>
                </div>
                <div className={styles.lineParent}>
                  <div className={styles.frameChild} />
                  <div className={styles.frameItem} />
                </div>
              </div>
            </div>
            <div className={styles.image63Wrapper}>
              <img
                className={styles.image63Icon}
                loading="lazy"
                alt=""
                src="/image-63@2x.png"
              />
            </div>
            <div className={styles.frameDiv}>
              <div className={styles.checkPointParent}>
                <h1 className={styles.checkPoint}>CHECK POINT</h1>
                <div className={styles.container}>
                  <div className={styles.innerContainer}>
                    <h1 className={styles.cpContainer}>
                      <p className={styles.cp}>
                        - 면/폴리 혼용의 CP 쭈리 원단으로 부드럽고 탄탄한 핏감
                        연출
                      </p>
                      <p className={styles.cp}>
                        - 페일제이드 베스트 제품의 리뉴얼 버전으로, 새로운 로고
                        패치 디자인과 배색
                      </p>
                      <p className={styles.cp}>- 레트로 무드의 후드 집업</p>
                      <p className={styles.cp}>
                        - 후드 안감 와플 원단으로 마감하여 후드의 핏감 유지와
                        배색 디테일 연출
                      </p>
                      <p className={styles.cp}>
                        - 슬림하게 라인을 잡아주는 핏감
                      </p>
                      <p className={styles.cp}>- 페일제이드 로고 투웨이 지퍼</p>
                      <p className={styles.cp}>
                        - 크고 깊은 후드 핏으로 페일제이드만의 핏감
                      </p>
                      <p className={styles.cp}>
                        - 두가지 사이즈로 디테일한 핏감 완성
                      </p>
                      <p className={styles.cp}>
                        - 주머니 전문 공장에서 공정을 거친 깔끔한 라인의 포켓
                        디자인
                      </p>
                    </h1>
                    <button className={styles.viewAllButton}>
                      <div className={styles.viewAll}>View All</div>
                    </button>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </section>
      </main>
      <Footer
        footerMarginLeft="-1px"
        hELPMENUTextDecoration="unset"
        badge="/badge1.svg"
        badge1="/badge-11.svg"
        badge2="/badge-21.svg"
        badge3="/badge-31.svg"
        badge4="/badge-41.svg"
      />
    </div>
  );
};

export default ProductDetailPage;
