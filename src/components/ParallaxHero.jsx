import { useState, useEffect }  from "react";

const words = ["Secure", "Efficient", "Scalable"];

export default function ParallaxHero() {
  const [currentWord, setCurrentWord] = useState(0);
  const [scrollY, setScrollY] = useState(0);

  useEffect(() => {
    const interval = setInterval(() => {
      setCurrentWord((prev) => (prev + 1) % words.length);
    }, 2000);

    const handleScroll = () => setScrollY(window.pageYOffset);
    window.addEventListener("scroll", handleScroll);

    return () => {
      clearInterval(interval);
      window.removeEventListener("scroll", handleScroll);
    };
  }, []);

  return (
    <div className="relative h-screen flex items-center justify-center overflow-hidden">
      <div
        className="absolute w-full h-full bg-cover bg-center"
        style={{
          backgroundImage:
            "url('https://images.unsplash.com/photo-1451187580459-43490279c0fa?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=2072&q=80')",
          transform: `translateY(${scrollY * 0.5}px)`,
        }}
      ></div>
      <div className="absolute inset-0 bg-gray-900 bg-opacity-50"></div>
      <div className="relative z-10 text-center text-white">
        <h1 className="text-4xl sm:text-5xl md:text-6xl font-bold mb-4">
          Empowering Your Business with Middleware
        </h1>
        <h2 className="text-3xl sm:text-4xl md:text-5xl font-semibold">
          <span className="inline-block min-w-[200px] transition-all duration-500 ease-in-out transform">
            {words[currentWord]}
          </span>
          Solutions
        </h2>
      </div>
    </div>
  );
}
