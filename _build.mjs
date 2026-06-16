import fs from "fs";
const dir = process.argv[1];
fs.writeFileSync(dir+"/PRD.md", "# Job Tracker AI — Product Requirements Document

## 1. Project Goal

Build a production-ready...");
console.log("ok");