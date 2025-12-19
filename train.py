from ultralytics import RTDETR
model = RTDETR('E:/pmy/RT_Detr/ultralytics-main/ultralytics-main/ultralytics/cfg/models/rt-detr/l-h-HRAMi.yaml')
results = model.train(data="E:/pmy/RT_Detr/ultralytics-main/ultralytics-main/ultralytics/cfg/datasets/personcar.yaml", epochs=370,
                      batch=4,save=True, resume=True,amp=False,name="",save_dir="E:/pmy/RT_Detr/ultralytics-main/ultralytics-main/ultralytics/experiment2",workers=0)