W ramach pierwszego etapu utworzono i skonfigurowano projekt Google Cloud Platform, który stanowi podstawę całego środowiska CI/CD oraz GKE.
Wykonane czynności:


Utworzono projekt:

devops-gke-12345


Skonfigurowano Cloud Shell oraz ustawiono projekt jako aktywny:
gcloud config set project devops-gke-12345


Aktywowano wymagane usługi Google Cloud:
gcloud services enable \
    container.googleapis.com \
    artifactregistry.googleapis.com \
    cloudbuild.googleapis.com \
    secretmanager.googleapis.com


Efekt: środowisko GCP gotowe do budowy klastra oraz automatyzacji procesów CI/CD.


Przygotowanie infrastruktury Terraform
W repozytorium skonfigurowano katalog terraform/, zawierający definicje infrastruktury jako kodu.

W ramach konfiguracji przygotowano:


provider Google (main.tf)


zmienne wejściowe (variables.tf)


definicję klastra GKE Autopilot (gke.tf)


Kluczowe komponenty:

Provider i konfiguracja:
terraform {
  required_providers {
    google = {
      source  = "hashicorp/google"
      version = "~> 5.0"
    }
  }
}

provider "google" {
  project = var.project
  region  = var.region
}

Definicja klastra GKE:
resource "google_container_cluster" "gke" {
  name                = var.cluster_name
  location            = var.region
  enable_autopilot    = true
  deletion_protection = false
}
Efekt: repozytorium zawiera kompletny zestaw plików Terraform umożliwiający automatyczne utworzenie klastra Kubernetes.


 Utworzenie klastra GKE
Po zdefiniowaniu plików Terraform wykonano proces provisioningu:
terraform init
terraform plan
terraform apply
Terraform wygenerował klaster GKE w regionie:
us-east1
Po zakończeniu tworzenia pobrano konfigurację kubeconfig:
gcloud container clusters get-credentials <cluster_name> --region us-east1
Efekt: w pełni działający klaster GKE Autopilot, dostępny poprzez kubectl.


 Utworzenie Artifact Registry (Docker)
W celu przechowywania obrazów kontenerów (budowanych przez Cloud Build) utworzono repozytorium Artifact Registry w regionie us-east1:
gcloud artifacts repositories create app \
  --repository-format=docker \
  --location=us-east1 \
  --description="Docker repository for CI/CD"
Repozytorium dostępne pod adresem:
us-east1-docker.pkg.dev/devops-gke-12345/app
Efekt: środowisko gotowe do przechowywania kontenerów aplikacji, które będą wykorzystywane podczas deploymentu na GKE.

Monitoring dashboard (GKE)

W Google Cloud Monitoring zaimportowano gotowy dashboard dla klastra GKE Autopilot. Pokazuje on:

1.Container CPU Usage (cores)
-CPU per kontener w czasie.
-Niski bazowy poziom + krótkie piki podczas deploymentów/testów.
2.Container Memory Usage (bytes)
-Zużycie RAM per kontener.
-Stabilne wartości, wzrost przy uruchomieniu nowych podów.
3.Container Restart Count (last 5 min)
-Restart kontenerów w ostatnich 5 minutach.
-Zwykle 0; pojedynczy pik przy rolloutach → brak chronicznych problemów.
4.Pod Count per Namespace
-Liczba podów w namespace’ach (default, kube-system, gke-*).
-Stała liczba podów systemowych, wzrost w default po wdrożeniu aplikacji.

Dashboard służy jako szybki przegląd zdrowia klastra (CPU, RAM, restarty, liczba podów) i pozwala powiązać skoki metryk z konkretnymi wdrożeniami w CI/CD.

<img width="2860" height="1558" alt="image (1)" src="https://github.com/user-attachments/assets/81d9a201-91f0-40d1-ad7e-fdd7c94bb918" />





