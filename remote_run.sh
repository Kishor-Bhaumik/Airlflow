
gcloud compute ssh --zone us-central1-a shobdokutir-gpu-2 -- "bash run.sh"
gcloud compute scp shobdokutir-gpu-2:DeepLearningExamples/PyTorch/SpeechSynthesis/Tacotron2/out.txt  /home/kishore/NLP 