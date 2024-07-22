# Imports and Setup
import cv2
from inference import InferencePipeline
from inference.core.interfaces.stream.sinks import render_boxes
import supervision as sv
import numpy as np

api_key = "...."

def on_prediction(predictions, video_frame):
  selected_class = [0, 1, 2, 3, 5, 7]
  
  detections = sv.Detections.from_inference(predictions)
  
  detections = detections[np.isin(detections.class_id, selected_class)]
  annotated_frame = sv.BoundingBoxAnnotator().annotate(video_frame.image, detections)

  labels = [
    f"{class_name} {confidence:.2f}"
    for class_name, confidence
    in zip(detections['class_name'], detections.confidence)
]
  annotated_frame = sv.LabelAnnotator().annotate(annotated_frame,detections,labels)
  cv2.imshow("results",annotated_frame)

pipeline = InferencePipeline.init(
  model_id="...",
  max_fps=0.5,
  confidence=0.3,
  video_reference="......",
  on_prediction=on_prediction, 
  api_key=api_key
)

pipeline.start()
pipeline.join()