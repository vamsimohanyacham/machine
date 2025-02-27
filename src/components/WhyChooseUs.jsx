//import React from 'react';//
import {
  LightBulbIcon,
  ShieldCheckIcon,
  ChartBarIcon,
  CubeTransparentIcon,
  UserGroupIcon,
} from "@heroicons/react/20/solid";

const reasons = [
  {
    icon: LightBulbIcon,
    title: "Innovative Solutions",
    description:
      "We deliver cutting-edge technologies tailored to your business needs.",
  },
  {
    icon: ShieldCheckIcon,
    title: "Robust Security",
    description:
      "Our solutions prioritize data protection and compliance with industry standards.",
  },
  {
    icon: ChartBarIcon,
    title: "Proven Track Record",
    description:
      "We have a history of successful implementations across various industries.",
  },
  {
    icon: CubeTransparentIcon,
    title: "Scalable Architecture",
    description:
      "Our solutions grow with your business, ensuring long-term success.",
  },
  {
    icon: UserGroupIcon,
    title: "Expert Team",
    description:
      "Our certified professionals bring years of experience to every project.",
  },
];

export default function WhyChooseUs() {
  return (
    <section className="py-16 bg-gray-50">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <h2 className="text-3xl font-extrabold text-gray-900 text-center mb-8">
          Why Choose Us
        </h2>
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
          {reasons.map((reason, index) => (
            <div key={index} className="bg-white rounded-lg shadow-md p-6">
              <reason.icon className="h-12 w-12 text-indigo-600 mb-4" />
              <h3 className="text-xl font-semibold text-gray-900 mb-2">
                {reason.title}
              </h3>
              <p className="text-gray-600">{reason.description}</p>
            </div>
          ))}
        </div>
      </div>
    </section>
  );
}
