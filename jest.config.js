// jest.config.js
export default {
  testMatch: [
    "**/?(*.)+(spec|test).[tj]s?(x)", // Matches test files
  ],
  testPathIgnorePatterns: ["/node_modules/"], // Ignores node_modules during tests

  reporters: [
    'default', // Default reporter
    ['jest-junit', {
      outputDirectory: 'test-results', // Output directory for JUnit report
      outputName: 'test-results.xml'   // Output filename for JUnit report (optional)
    }]
  ],
};
