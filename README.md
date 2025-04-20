
# 🧼 AutoDQ – Automated Data Quality Monitoring Pipeline

AutoDQ is a plug-and-play, modular data quality monitoring pipeline that automatically ingests datasets dropped into a folder, performs essential data validation checks, logs results, and triggers real-time alerts when issues are found.

Whether you're a data analyst, data engineer, or business analyst, AutoDQ ensures your data is clean, reliable, and production-ready before it flows into dashboards or machine learning models.

---

## 📌 Key Features

- ✅ Drop-and-check workflow — just drop a dataset into the folder, and AutoDQ does the rest
- 📂 File-based ingestion (CSV/XLSX)
- 📊 Validation checks: missing values, schema mismatches, duplicates (with more rules planned)
- 🧾 Structured logging for transparency
- 📣 Real-time alerts via Slack or email
- 🐳 Dockerized for consistent execution environments
- ⏰ Optional orchestration using Airflow (Phase 6+)

---

## 🛠️ Project Structure

```
AutoDQ/
├── datasets/           # Drop raw input files here
├── configs/            # JSON configs for validation rules (optional)
├── secrets/            # .env file for API keys, DB passwords (not committed)
├── logs/               # Auto-generated log files
├── output/             # (Optional) Cleaned or validated outputs
├── pipeline/           # Core logic scripts (ingestion, validation, alerting)
├── docker/             # Dockerfile and dependencies
├── airflow/            # (Optional) Airflow DAGs
├── run_pipeline.sh     # One-click runner script
├── docker-compose.yml  # For multi-container orchestration
└── README.md           # This file
```

---

## 🧱 Project Phases

| Phase | Description | Status |
|-------|-------------|--------|
| **Phase 1** | File-based ingestion (CSV/XLSX) from `datasets/` folder | ✅ Completed |
| **Phase 2** | Basic data validation (missing values, duplicates) | ✅ Completed |
| **Phase 3** | Logging results and issues | 🔜 Upcoming|
| **Phase 4** | Alert system via Slack or Email | 🔜 |
| **Phase 5** | Dockerize entire pipeline with `.env` support | 🔜 |
| **Phase 6** | Optional scheduling with Airflow or Cron | 🔜 |
| **Phase 7** | Productionization and CI/CD integration | 🔜 |

---

## 🐳 Docker Usage

### Build the Docker image

```bash
docker build -f docker/Dockerfile -t autodq .
```

### Run the container

```bash
docker run --rm autodq
```

---

## 🔒 Environment Variables

Add your secrets and credentials to `secrets/.env`:

```
DB_HOST=localhost
DB_USER=user
DB_PASSWORD=password
SLACK_WEBHOOK=https://hooks.slack.com/services/your/webhook/url
```

> Make sure `secrets/.env` is included in `.gitignore`.

---

## 📌 License

This project is open-source and available for personal and professional use.
