import {
  CloudIcon,
  CogIcon,
  ServerIcon,
  ShieldCheckIcon,
  CommandLineIcon,
  CpuChipIcon,
  FingerPrintIcon,
} from "@heroicons/react/20/solid";

const services = [
  {
    icon: CloudIcon,
    name: "Salesforce",
    description:
      "Leverage the power of Salesforce to streamline your business processes and enhance customer relationships.",
  },
  {
    icon: CogIcon,
    name: "Azure Cloud Developer and Admin (AI)",
    description:
      "Harness the potential of Azure cloud and AI technologies to drive innovation and efficiency in your organization.",
  },
  {
    icon: ServerIcon,
    name: "Splunk",
    description:
      "Gain valuable insights from your data with Splunk's powerful analytics and monitoring capabilities.",
  },
  {
    icon: CommandLineIcon,
    name: "Integration",
    description:
      "Seamlessly connect your systems and applications to improve workflow and data consistency across your enterprise.",
  },
  {
    icon: ShieldCheckIcon,
    name: "Cybersecurity",
    description:
      "Protect your digital assets with our comprehensive cybersecurity solutions and best practices.",
  },
  {
    icon: CpuChipIcon,
    name: "Full Stack Development",
    description:
      "Build robust, scalable applications with our expert full stack development services.",
  },
  {
    icon: CloudIcon,
    name: "Cloud Technologies (GCP, Azure, AWS)",
    description:
      "Leverage the power of leading cloud platforms to enhance your infrastructure and application deployment.",
  },
  {
    icon: FingerPrintIcon,
    name: "Identity Access Management",
    description:
      "Secure your organization with advanced identity and access management solutions using Sailpoint IIQ and ForgeRock.",
  },
];

export default function ServicesOffered() {
  return (
    <section className="py-16 bg-gray-50">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <h2 className="text-3xl font-extrabold text-gray-900 text-center mb-8">
          Services Offered
        </h2>
        <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-8">
          {services.map((service, index) => (
            <div
              key={index}
              className="bg-white rounded-lg shadow-md p-6 flex flex-col items-center justify-center text-center transform transition duration-500 hover:scale-105"
            >
              <service.icon className="h-12 w-12 text-indigo-600 mb-4" />
              <h3 className="text-lg font-semibold text-gray-900 mb-2">
                {service.name}
              </h3>
              <p className="text-gray-600 text-sm">{service.description}</p>
            </div>
          ))}
        </div>
      </div>
    </section>
  );
}
