import { useRef, useEffect } from "react";

// Import partner logos
import HCL from "../assets/HCL.png";
import HSBC from "../assets/HSBC.png";
import llyodsBank from "../assets/llyodsBank.png";
import softtek from "../assets/softtek.png";
import TechM from "../assets/TechM.png";
import wipro from "../assets/wipro.png";

const partnerLogos = [
  { src: HCL, alt: "HCL" },
  { src: HSBC, alt: "HSBC" },
  { src: llyodsBank, alt: "Lloyds Bank" },
  { src: softtek, alt: "Softtek" },{ src: TechM, alt: "Tech Mahindra" },{ src: wipro, alt: "Wipro" },
];

export default function Partnerships() {
  const scrollRef = useRef(null);

  useEffect(() => {
    const scrollContainer = scrollRef.current;
    if (scrollContainer) {
      let animationFrameId;
      let scrollAmount = 0;

      const scroll = () => {
        scrollAmount += 1; // Adjust speed as needed
        if (scrollAmount >= scrollContainer.scrollWidth / 2)
        
        
        
        
        
        
        
        
        
        {
          scrollAmount = 0; // Reset scroll position
        }
        scrollContainer.scrollLeft = scrollAmount;
        animationFrameId = requestAnimationFrame(scroll);
      };

      animationFrameId = requestAnimationFrame(scroll);

      return () => {
        if (animationFrameId) {
          cancelAnimationFrame(animationFrameId);
        }
      };
    }
  }, []);

  return (
    <section className="py-16 bg-white">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <h2 className="text-3xl font-extrabold text-gray-900 text-center mb-8">
          Our Partnerships
        </h2>
        <div className="relative overflow-hidden" style={{ maxWidth: "100%" }}>
          <div
            ref={scrollRef}
            className="flex overflow-x-hidden whitespace-nowrap"
          >
            <div className="flex items-center space-x-8">
              {partnerLogos.map((partner, index) => (
                <div key={index} className="flex-shrink-0">
                  <img
                    src={partner.src}
                    alt={partner.alt}
                    className="h-20 w-40 object-contain"
                  />
                </div>
              ))}
              {partnerLogos.map((partner, index) => (
                <div key={`clone-${index}`} className="flex-shrink-0">
                  <img
                    src={partner.src}
                    alt={partner.alt}
                    className="h-20 w-40 object-contain"
                  />
                </div>
              ))}
            </div>
          </div>
        </div>
      </div>
    </section>
  );
}
