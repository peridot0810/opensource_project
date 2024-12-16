import React, { useEffect } from "react";
import {
  Routes,
  Route,
  useNavigationType,
  useLocation,
} from "react-router-dom";
import Homepage from "./pages/Homepage";
import LogIn from "./pages/LogIn";
import CategoryPage from "./pages/CategoryPage";
import ProductDetailPage from "./pages/ProductDetailPage";
import SignUp from "./pages/SignUp";
import Cart from "./pages/Cart";

function App() {
  const action = useNavigationType();
  const location = useLocation();
  const pathname = location.pathname;

  // 페이지 이동 시 스크롤 위치 초기화
  useEffect(() => {
    if (action !== "POP") {
      window.scrollTo(0, 0);
    }
  }, [action, pathname]);

  // 동적으로 제목 및 메타 설명 변경
  useEffect(() => {
    let title = "";
    let metaDescription = "";

    switch (pathname) {
      case "/":
        title = "홈페이지";
        metaDescription = "이곳은 홈페이지입니다.";
        break;
      case "/log-in":
        title = "로그인";
        metaDescription = "로그인 페이지입니다.";
        break;
      case "/category-page":
        title = "카테고리";
        metaDescription = "카테고리 페이지입니다.";
        break;
      case "/product-detail-page":
        title = "상품 상세";
        metaDescription = "상품 상세 페이지입니다.";
        break;
      case "/sign-up":
        title = "회원가입";
        metaDescription = "회원가입 페이지입니다.";
        break;
      case "/cart":
        title = "장바구니";
        metaDescription = "장바구니 페이지입니다.";
        break;
      default:
        title = "React와 Flask 연동";
        metaDescription = "React와 Flask를 연동한 애플리케이션입니다.";
    }

    if (title) {
      document.title = title;
    }

    if (metaDescription) {
      const metaDescriptionTag = document.querySelector(
        'head > meta[name="description"]'
      );
      if (metaDescriptionTag) {
        metaDescriptionTag.content = metaDescription;
      }
    }
  }, [pathname]);

  return (
    <Routes>
      <Route path="/" element={<Homepage />} />
      <Route path="/log-in" element={<LogIn />} />
      <Route path="/category-page" element={<CategoryPage />} />
      <Route path="/product-detail-page" element={<ProductDetailPage />} />
      <Route path="/sign-up" element={<SignUp />} />
      <Route path="/cart" element={<Cart />} />
    </Routes>
  );
}

export default App;


// import React, { useEffect, useState } from "react";
// import axios from "axios";

// function App() {
//     const [data, setData] = useState(null);

//     useEffect(() => {
//         // Flask API 호출
//         axios.get("http://localhost:5000/api/data")
//             .then((response) => {
//                 setData(response.data.message); // "Hello from Flask!" 가져오기
//             })
//             .catch((error) => {
//                 console.error("Error fetching data:", error);
//             });
//     }, []);

//     return (
//         <div>
//             <h1>React와 Flask 연동</h1>
//             {data ? <p>Flask 응답: {data}</p> : <p>Loading...</p>}
//         </div>
//     );
// }

// export default App;


// // import { useEffect } from "react";
// import {
//   Routes,
//   Route,
//   useNavigationType,
//   useLocation,
// } from "react-router-dom";
// import Homepage from "./pages/Homepage";
// import LogIn from "./pages/LogIn";
// import CategoryPage from "./pages/CategoryPage";
// import ProductDetailPage from "./pages/ProductDetailPage";
// import SignUp from "./pages/SignUp";
// import Cart from "./pages/Cart";

// function App() {
//   const action = useNavigationType();
//   const location = useLocation();
//   const pathname = location.pathname;

//   useEffect(() => {
//     if (action !== "POP") {
//       window.scrollTo(0, 0);
//     }
//   }, [action, pathname]);

//   useEffect(() => {
//     let title = "";
//     let metaDescription = "";

//     switch (pathname) {
//       case "/":
//         title = "";
//         metaDescription = "";
//         break;
//       case "/log-in":
//         title = "";
//         metaDescription = "";
//         break;
//       case "/category-page":
//         title = "";
//         metaDescription = "";
//         break;
//       case "/product-detail-page":
//         title = "";
//         metaDescription = "";
//         break;
//       case "/sign-up":
//         title = "";
//         metaDescription = "";
//         break;
//       case "/cart":
//         title = "";
//         metaDescription = "";
//         break;
//     }

//     if (title) {
//       document.title = title;
//     }

//     if (metaDescription) {
//       const metaDescriptionTag = document.querySelector(
//         'head > meta[name="description"]'
//       );
//       if (metaDescriptionTag) {
//         metaDescriptionTag.content = metaDescription;
//       }
//     }
//   }, [pathname]);

//   return (
//     <Routes>
//       <Route path="/" element={<Homepage />} />
//       <Route path="/log-in" element={<LogIn />} />
//       <Route path="/category-page" element={<CategoryPage />} />
//       <Route path="/product-detail-page" element={<ProductDetailPage />} />
//       <Route path="/sign-up" element={<SignUp />} />
//       <Route path="/cart" element={<Cart />} />
//     </Routes>
//   );
// }
// export default App;
