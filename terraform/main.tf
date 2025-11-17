provider "google" {
  project = var.project_id
  region  = var.region
}

resource "google_project_service" "svc" {
  for_each = toset([
    "container.googleapis.com",
    "artifactregistry.googleapis.com",
    "cloudbuild.googleapis.com"
  ])
  service = each.value
}
