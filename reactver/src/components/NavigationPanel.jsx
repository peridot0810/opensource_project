import { useCallback } from "react";
import FrameComponent1 from "./FrameComponent1";
import { useNavigate } from "react-router-dom";
import Button from "./Button";
import PaginationNumberBase from "./PaginationNumberBase";
import PropTypes from "prop-types";
import styles from "./NavigationPanel.module.css";

const NavigationPanel = ({ className = "" }) => {
  const navigate = useNavigate();

  const onTextClick = useCallback(() => {
    navigate("/product-detail-page");
  }, [navigate]);

  const onVirtualTryonContainerClick = useCallback(() => {
    // Please sync "VTON1" to the project
  }, []);

  return (
    <div className={[styles.navigationPanel, className].join(" ")}>
      <img className={styles.frameIcon} alt="" src="/frame-5.svg" />
      <div className={styles.navigationLinks}>
        <div className={styles.homeLink}>
          <div className={styles.homeButton}>
            <a className={styles.home}>Home</a>
          </div>
          <div className={styles.bestLink}>
            <img
              className={styles.emptyHomeLink}
              alt=""
              src="/frame-6@2x.png"
            />
          </div>
          <div className={styles.best}>BEST</div>
        </div>
        <div className={styles.filterItem}>
          <div className={styles.filtersParent}>
            <a className={styles.filters}>Filters</a>
            <img className={styles.emptyFilterIcon} alt="" src="/frame-7.svg" />
          </div>
          <div className={styles.menuDivider} />
          <div className={styles.categoryLinks}>
            <div className={styles.filtersParent}>
              <div className={styles.top}>Top</div>
              <img
                className={styles.emptyCategoryIcon}
                alt=""
                src="/frame-8@2x.png"
              />
            </div>
            <div className={styles.filtersParent}>
              <div className={styles.outers}>Outers</div>
              <img
                className={styles.emptyCategoryIcon}
                alt=""
                src="/frame-8@2x.png"
              />
            </div>
            <div className={styles.filtersParent}>
              <div className={styles.pants}>Pants</div>
              <img
                className={styles.emptyCategoryIcon}
                alt=""
                src="/frame-8@2x.png"
              />
            </div>
            <div className={styles.filtersParent}>
              <div className={styles.dress}>Dress</div>
              <img
                className={styles.emptyCategoryIcon}
                alt=""
                src="/frame-8@2x.png"
              />
            </div>
          </div>
          <div className={styles.filterItemChild} />
          <div className={styles.filterItemChild} />
          <div className={styles.filterItemChild} />
          <button className={styles.applyFilterWrapper}>
            <div className={styles.applyFilter}>Apply Filter</div>
          </button>
        </div>
      </div>
      <div className={styles.productListing}>
        <div className={styles.productGrid}>
          <div className={styles.productRow}>
            <div className={styles.productItem}>
              <div className={styles.productBadge}>
                <h1 className={styles.best1}>BEST</h1>
              </div>
              <div className={styles.productDetails}>
                <div className={styles.productImageNames}>
                  <img
                    className={styles.image52Icon}
                    loading="lazy"
                    alt=""
                    src="/image-52@2x.png"
                  />
                </div>
              </div>
              <div className={styles.productDetails1}>
                <FrameComponent1
                  secondStar="/star-2.svg"
                  thirdStar="/star-3.svg"
                  star5="/star-5.svg"
                />
              </div>
              <div className={styles.productDetails2}>
                <div className={styles.image8Wrapper}>
                  <img
                    className={styles.image8Icon}
                    alt=""
                    src="/image-8@2x.png"
                  />
                </div>
              </div>
              <div className={styles.productDetails3}>
                <div className={styles.parent}>
                  <div className={styles.div}>스키니 핏 청바지</div>
                  <div className={styles.productContentParent}>
                    <div className={styles.productContent}>
                      <div className={styles.starParent}>
                        <img
                          className={styles.frameChild}
                          alt=""
                          src="/star-1.svg"
                        />
                        <img
                          className={styles.frameChild}
                          alt=""
                          src="/star-2.svg"
                        />
                        <img
                          className={styles.frameChild}
                          alt=""
                          src="/star-3.svg"
                        />
                        <img
                          className={styles.starIcon}
                          alt=""
                          src="/star-5.svg"
                        />
                      </div>
                      <div className={styles.emptyStarTwoContainer}>
                        <span>3.5/</span>
                        <span className={styles.span}>5</span>
                      </div>
                    </div>
                    <div className={styles.productItem1}>
                      <div className={styles.wrapper}>
                        <div className={styles.div2}>39,000원</div>
                      </div>
                      <div className={styles.virtualTryOnWrapper}>
                        <div className={styles.virtualTryOn}>
                          Virtual Try on
                        </div>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
              <div className={styles.productDetails}>
                <div className={styles.image8Wrapper}>
                  <img
                    className={styles.image56Icon}
                    loading="lazy"
                    alt=""
                    src="/image-56@2x.png"
                  />
                </div>
              </div>
              <div className={styles.productName}>
                <div className={styles.typeWrapper}>
                  <div className={styles.type}>라메스 무스탕 (2TYPE)</div>
                </div>
                <div className={styles.starContainerParent}>
                  <div className={styles.starContainer}>
                    <div className={styles.firstRating}>
                      <img
                        className={styles.frameChild}
                        alt=""
                        src="/star-1.svg"
                      />
                      <img
                        className={styles.frameChild}
                        alt=""
                        src="/star-2-2.svg"
                      />
                      <img
                        className={styles.frameChild}
                        alt=""
                        src="/star-3-2.svg"
                      />
                      <img
                        className={styles.frameChild}
                        loading="lazy"
                        alt=""
                        src="/star-4.svg"
                      />
                      <img
                        className={styles.starIcon}
                        alt=""
                        src="/star-5-2.svg"
                      />
                    </div>
                    <div className={styles.emptyRating}>
                      <span>4.5/</span>
                      <span className={styles.span}>5</span>
                    </div>
                  </div>
                  <div className={styles.productPrice}>
                    <div className={styles.frameParent}>
                      <div className={styles.container}>
                        <div className={styles.div2}>169,000원</div>
                      </div>
                      <div className={styles.virtualTryOnWrapper}>
                        <div className={styles.virtualTryOn}>
                          Virtual Try on
                        </div>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
            </div>
            <div className={styles.productCount}>
              <div className={styles.sortingOptions}>
                <div className={styles.dress}>Showing 1-10 of 100 Products</div>
                <div className={styles.dress}>
                  <span>{`Sort by: `}</span>
                  <span className={styles.mostPopular}>Most Popular</span>
                </div>
              </div>
              <div className={styles.productGridContainer}>
                <div className={styles.productGridRow}>
                  <div className={styles.firstProductDetails}>
                    <div className={styles.firstRatingAndPrice}>
                      <div className={styles.secondProductImages}>
                        <img
                          className={styles.image51Icon}
                          loading="lazy"
                          alt=""
                          src="/image-51@2x.png"
                        />
                      </div>
                      <div className={styles.gridItemInfo}>
                        <div className={styles.div4} onClick={onTextClick}>
                          레트로 후드집업
                        </div>
                        <div className={styles.gridRatingContainer}>
                          <div className={styles.productContent}>
                            <div className={styles.starParent}>
                              <img
                                className={styles.frameChild}
                                alt=""
                                src="/star-1.svg"
                              />
                              <img
                                className={styles.frameChild}
                                alt=""
                                src="/star-2.svg"
                              />
                              <img
                                className={styles.frameChild}
                                alt=""
                                src="/star-3.svg"
                              />
                              <img
                                className={styles.frameChild}
                                alt=""
                                src="/star-4-1.svg"
                              />
                              <img
                                className={styles.starIcon}
                                alt=""
                                src="/star-5-3.svg"
                              />
                            </div>
                            <div className={styles.emptyStarTwoContainer}>
                              <span>4.5/</span>
                              <span className={styles.span}>5</span>
                            </div>
                          </div>
                          <div className={styles.group}>
                            <div className={styles.div5}>98,000원</div>
                            <div
                              className={styles.virtualTryonContainer}
                              onClick={onVirtualTryonContainerClick}
                            >
                              <div className={styles.firstTryonButton}>
                                <div className={styles.virtualTryOn}>
                                  Virtual Try on
                                </div>
                              </div>
                            </div>
                          </div>
                        </div>
                      </div>
                    </div>
                    <div className={styles.firstRatingAndPrice}>
                      <div className={styles.secondProductImages}>
                        <img
                          className={styles.imageIcon}
                          loading="lazy"
                          alt=""
                          src="/image@2x.png"
                        />
                      </div>
                      <div className={styles.gridItemInfo}>
                        <div className={styles.div}>데님 홀터 드레스</div>
                        <div className={styles.gridRatingContainer}>
                          <div className={styles.productContent}>
                            <div className={styles.starParent}>
                              <img
                                className={styles.frameChild}
                                alt=""
                                src="/star-1.svg"
                              />
                              <img
                                className={styles.frameChild}
                                alt=""
                                src="/star-2.svg"
                              />
                              <img
                                className={styles.frameChild}
                                alt=""
                                src="/star-3.svg"
                              />
                              <img
                                className={styles.frameChild}
                                alt=""
                                src="/star-4-1.svg"
                              />
                              <img
                                className={styles.frameChild}
                                alt=""
                                src="/star-5-4.svg"
                              />
                            </div>
                            <div className={styles.emptyStarTwoContainer}>
                              <span>5.0/</span>
                              <span className={styles.span}>5</span>
                            </div>
                          </div>
                          <div className={styles.productItem1}>
                            <div className={styles.frame}>
                              <div className={styles.div2}>82,000원</div>
                            </div>
                            <div className={styles.virtualTryOnWrapper}>
                              <div className={styles.virtualTryOn}>
                                Virtual Try on
                              </div>
                            </div>
                          </div>
                        </div>
                      </div>
                    </div>
                  </div>
                  <div className={styles.productItem2}>
                    <div className={styles.productContent1}>
                      <div className={styles.firstRatingAndPrice}>
                        <div className={styles.secondProductImages}>
                          <img
                            className={styles.imageIcon1}
                            alt=""
                            src="/image-1@2x.png"
                          />
                        </div>
                        <div className={styles.gridItemInfo}>
                          <div className={styles.div9}>
                            인디고 생지 데님 부츠컷 팬츠
                          </div>
                          <div className={styles.productContentParent}>
                            <div className={styles.productContent}>
                              <div className={styles.starParent}>
                                <img
                                  className={styles.frameChild}
                                  alt=""
                                  src="/star-1.svg"
                                />
                                <img
                                  className={styles.frameChild}
                                  alt=""
                                  src="/star-2.svg"
                                />
                                <img
                                  className={styles.frameChild}
                                  alt=""
                                  src="/star-3.svg"
                                />
                                <img
                                  className={styles.frameChild}
                                  alt=""
                                  src="/star-4-1.svg"
                                />
                                <img
                                  className={styles.starIcon}
                                  alt=""
                                  src="/star-5-3.svg"
                                />
                              </div>
                              <div className={styles.emptyStarTwoContainer}>
                                <span>4.5/</span>
                                <span className={styles.span}>5</span>
                              </div>
                            </div>
                            <div className={styles.group}>
                              <div className={styles.div5}>54,000원</div>
                              <div className={styles.virtualTryonButtonWrapper}>
                                <div className={styles.firstTryonButton}>
                                  <div className={styles.virtualTryOn}>
                                    Virtual Try on
                                  </div>
                                </div>
                              </div>
                            </div>
                          </div>
                        </div>
                      </div>
                      <div className={styles.firstRatingAndPrice}>
                        <div className={styles.secondProductImages}>
                          <img
                            className={styles.imageIcon2}
                            alt=""
                            src="/image-2@2x.png"
                          />
                        </div>
                        <div className={styles.productNameAndRating1}>
                          <div className={styles.div11}>카모 울프 후드</div>
                          <div className={styles.productContentParent}>
                            <div className={styles.productContent}>
                              <div className={styles.starParent}>
                                <img
                                  className={styles.frameChild}
                                  alt=""
                                  src="/star-1.svg"
                                />
                                <img
                                  className={styles.frameChild}
                                  alt=""
                                  src="/star-2.svg"
                                />
                                <img
                                  className={styles.frameChild}
                                  alt=""
                                  src="/star-3.svg"
                                />
                                <img
                                  className={styles.frameChild}
                                  alt=""
                                  src="/star-4-1.svg"
                                />
                                <img
                                  className={styles.starIcon}
                                  alt=""
                                  src="/star-5-3.svg"
                                />
                              </div>
                              <div className={styles.emptyStarTwoContainer}>
                                <span>4.5/</span>
                                <span className={styles.span}>5</span>
                              </div>
                            </div>
                            <div className={styles.priceAndVirtualTryon1}>
                              <div className={styles.wrapper}>
                                <div className={styles.div2}>148,000원</div>
                              </div>
                              <div className={styles.virtualTryOnWrapper}>
                                <div className={styles.virtualTryOn}>
                                  Virtual Try on
                                </div>
                              </div>
                            </div>
                          </div>
                        </div>
                      </div>
                    </div>
                  </div>
                  <div className={styles.firstProductDetails}>
                    <div className={styles.firstRatingAndPrice}>
                      <div className={styles.secondProductImages}>
                        <img
                          className={styles.imageIcon3}
                          alt=""
                          src="/image-3@2x.png"
                        />
                      </div>
                      <div className={styles.gridItemInfo}>
                        <div className={styles.div}>버건디 가죽 자켓</div>
                        <div className={styles.starContainerParent}>
                          <div className={styles.productContent}>
                            <div className={styles.firstRating}>
                              <img
                                className={styles.frameChild}
                                alt=""
                                src="/star-1.svg"
                              />
                              <img
                                className={styles.frameChild}
                                alt=""
                                src="/star-2-2.svg"
                              />
                              <img
                                className={styles.frameChild}
                                alt=""
                                src="/star-3-2.svg"
                              />
                              <img
                                className={styles.frameChild}
                                alt=""
                                src="/star-4.svg"
                              />
                            </div>
                            <div className={styles.firstRatingCountContainer}>
                              <span>4.0/</span>
                              <span className={styles.span}>5</span>
                            </div>
                          </div>
                          <div className={styles.priceVirtualContent}>
                            <div className={styles.container}>
                              <div className={styles.div2}>178,000원</div>
                            </div>
                            <div className={styles.virtualTryOnWrapper}>
                              <div className={styles.virtualTryOn}>
                                Virtual Try on
                              </div>
                            </div>
                          </div>
                        </div>
                      </div>
                    </div>
                    <div className={styles.firstRatingAndPrice}>
                      <div className={styles.secondProductImages}>
                        <img
                          className={styles.imageIcon4}
                          alt=""
                          src="/image-4@2x.png"
                        />
                      </div>
                      <div className={styles.gridItemInfo}>
                        <div className={styles.div15}>아가일 니트 가디건</div>
                        <div className={styles.starContainerParent}>
                          <div className={styles.productContent}>
                            <div className={styles.starParent}>
                              <img
                                className={styles.frameChild}
                                alt=""
                                src="/star-1.svg"
                              />
                              <img
                                className={styles.frameChild}
                                alt=""
                                src="/star-2-2.svg"
                              />
                              <img
                                className={styles.frameChild}
                                alt=""
                                src="/star-3-2.svg"
                              />
                            </div>
                            <div className={styles.emptyStarTwoContainer}>
                              <span>3.0/</span>
                              <span className={styles.span}>5</span>
                            </div>
                          </div>
                          <div className={styles.group}>
                            <div className={styles.container}>
                              <div className={styles.div5}>33,000원</div>
                            </div>
                            <div className={styles.virtualTryOnWrapper}>
                              <div className={styles.virtualTryOn}>
                                Virtual Try on
                              </div>
                            </div>
                          </div>
                        </div>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
          <div className={styles.pagination}>
            <div className={styles.paginationContent}>
              <div className={styles.menuDivider} />
              <div className={styles.paginationControls}>
                <div className={styles.leftButtonContainer}>
                  <Button
                    destructive={false}
                    hierarchy="Secondary gray"
                    icon="Leading"
                    size="sm"
                    state="Default"
                  />
                </div>
                <div className={styles.pageNumberContainer}>
                  <PaginationNumberBase
                    shape="Square"
                    state="Default"
                    number="1"
                    numberWidth="10px"
                  />
                  <PaginationNumberBase
                    shape="Square"
                    state="Default"
                    number="2"
                  />
                  <PaginationNumberBase
                    shape="Square"
                    state="Default"
                    number="3"
                    numberWidth="10px"
                  />
                  <PaginationNumberBase
                    shape="Square"
                    state="Default"
                    number="..."
                    numberWidth="14px"
                  />
                  <PaginationNumberBase
                    shape="Square"
                    state="Default"
                    number="8"
                    numberWidth="10px"
                  />
                  <PaginationNumberBase
                    shape="Square"
                    state="Default"
                    number="9"
                    numberWidth="10px"
                  />
                  <PaginationNumberBase
                    shape="Square"
                    state="Default"
                    number="10"
                    numberWidth="18px"
                  />
                </div>
                <div className={styles.leftButtonContainer}>
                  <button className={styles.button}>
                    <div className={styles.buttonBase}>
                      <div className={styles.text}>Next</div>
                      <img
                        className={styles.arrowRightIcon}
                        alt=""
                        src="/arrowright.svg"
                      />
                    </div>
                  </button>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};

NavigationPanel.propTypes = {
  className: PropTypes.string,
};

export default NavigationPanel;
