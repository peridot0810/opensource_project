import { useEffect } from "react";
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

  useEffect(() => {
    if (action !== "POP") {
      window.scrollTo(0, 0);
    }
  }, [action, pathname]);

  useEffect(() => {
    let title = "";
    let metaDescription = "";

    switch (pathname) {
      case "/":
        title = "";
        metaDescription = "";
        break;
      case "/log-in":
        title = "";
        metaDescription = "";
        break;
      case "/category-page":
        title = "";
        metaDescription = "";
        break;
      case "/product-detail-page":
        title = "";
        metaDescription = "";
        break;
      case "/sign-up":
        title = "";
        metaDescription = "";
        break;
      case "/cart":
        title = "";
        metaDescription = "";
        break;
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
