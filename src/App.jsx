// import React from 'react';
import Navbar from "./components/Navbar.jsx";
import ParallaxHero from "./components/ParallaxHero.jsx";
import Footer from "./components/Footer.jsx";
import WhoWeAre from "./components/WhoWeAre.jsx";
import ServicesOffered from "./components/ServicesOffered.jsx";
import Partnerships from "./components/Partnerships.jsx";
import WhyChooseUs from "./components/WhyChooseUs.jsx";

function App() {
  return (
    <div className="min-h-screen bg-gray-100">
      <Navbar />
      <ParallaxHero />
      <WhoWeAre />
      <ServicesOffered />
      <Partnerships />
      <WhyChooseUs />
      <Footer />
    </div>
  );
}

export default App;
