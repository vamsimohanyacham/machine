import { defineConfig } from "eslint-define-config";
import react from "eslint-plugin-react";
import reactHooks from "eslint-plugin-react-hooks";
import reactRefresh from "eslint-plugin-react-refresh";
import globals from "globals";

export default defineConfig({
  files: ["**/*.js", "**/*.jsx"],
  languageOptions: {
    ecmaVersion: 2020,
    globals: {
      ...globals.browser,
      test: "readonly", // Jest globals
      expect: "readonly", // Jest globals
      module: "readonly", // Jest globals
    },
    parserOptions: {
      ecmaVersion: "latest",
      ecmaFeatures: { jsx: true },
      sourceType: "module",
    },
  },
  settings: {
    react: {
      version: "18.3",
    },
  },
  plugins: {
    react,
    "react-hooks": reactHooks,
    "react-refresh": reactRefresh,
  },
  rules: {
    // ESLint rules here
  },
});
