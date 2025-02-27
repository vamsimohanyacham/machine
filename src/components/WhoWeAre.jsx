import { useState, useEffect } from "react";
import PropTypes from "prop-types";

// NumberTicker component with prop validation
const NumberTicker = ({ end, duration }) => {
  const [count, setCount] = useState(0);

  useEffect(() => {
    let start = 0;
    const increment = end / (duration / 16);
    const timer = setInterval(() => {
      start += increment;
      setCount(Math.floor(start));
      if (start >= end) {
        clearInterval(timer);
        setCount(end);
      }
    }, 16);

    return () => clearInterval(timer);
  }, [end, duration]);

  return <span>{count}</span>;
};

// PropTypes validation for NumberTicker component
NumberTicker.propTypes = {
  end: PropTypes.number.isRequired, // 'end' should be a number
  duration: PropTypes.number.isRequired, // 'duration' should be a number
};

// StatsItem component to avoid code repetition
const StatsItem = ({ end, label }) => (
  <div>
    <p className="text-4xl font-bold text-indigo-600">
      <NumberTicker end={end} duration={2000} />+
    </p>
    <p className="mt-2 text-lg font-medium text-gray-700">{label}</p>
  </div>
);

StatsItem.propTypes = {
  end: PropTypes.number.isRequired,
  label: PropTypes.string.isRequired,
};

// WhoWeAre component
export default function WhoWeAre() {
  return (
    <section className="py-16 bg-white">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <h2 className="text-3xl font-extrabold text-gray-900 text-center mb-8">
          Who We Are
        </h2>
        <p className="text-xl text-gray-600 text-center mb-12">
          Middleware is a leading IT consulting firm dedicated to providing
          innovative solutions that drive business growth and digital
          transformation.
        </p>
        <div className="grid grid-cols-1 md:grid-cols-3 gap-8 text-center">
          <StatsItem end={5} label="Global Locations" />
          <StatsItem end={50} label="Certified Industry Experts" />
          <StatsItem
            end={30}
            label="Microsoft Azure's Developer and Admin Certifications"
          />
        </div>
      </div>
    </section>
  );
}
