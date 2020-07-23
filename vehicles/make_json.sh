for split in train val
do
    python voc2coco.py \
        --ann_dir vehicles/xml_files \
        --ann_ids vehicles/img_ids/${split}.txt \
        --labels vehicles/labels.txt \
        --output vehicles/outputs/${split}.json \
        --ext xml
done