# Copyright 2023 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from __future__ import annotations

import os

from vertexai.language_models import TextGenerationModel

PROJECT_ID = os.getenv("GOOGLE_CLOUD_PROJECT")


def tuning() -> TextGenerationModel:
    # [START generativeaionvertexai_tuning]
    import vertexai
    from vertexai.language_models import TextGenerationModel

    # TODO(developer): Update and un-comment below line
    # PROJECT_ID = "your-project-id"

    # Initialize Vertex AI
    vertexai.init(project=PROJECT_ID, location="us-central1")

    model = TextGenerationModel.from_pretrained("text-bison@002")

    # TODO(developer): Update the training data path
    tuning_job = model.tune_model(
        training_data="gs://cloud-samples-data/ai-platform/generative_ai/headline_classification.jsonl",
        tuning_job_location="europe-west4",
        tuned_model_location="us-central1",
    )

    print(tuning_job._status)
    # Example response:
    # pipeline_job = aiplatform.PipelineJob.get('projects/1234567890/locations/europe-west4/pipelineJobs/tune...
    # View Pipeline Job:
    # ...
    # PipelineState.PIPELINE_STATE_PENDING

    # [END generativeaionvertexai_tuning]
    return model


if __name__ == "__main__":
    tuning()
