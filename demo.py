from pyBulletSimRecorder import PyBulletRecorder
import pybullet as p
import pybullet_data

# Setup pyBullet
p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())
p.setRealTimeSimulation(0)
p.setGravity(0, 0, -9.81)
p.loadURDF('plane.urdf')

recorder = PyBulletRecorder()
urdf_path = 'assets/power_drill/power_drill.urdf'
body_id = p.loadURDF(
    fileName=urdf_path,
    basePosition=(0, 0, 0.4),
    baseOrientation=(0.4, 0.3, 0.2, 0.1))

# 1. Tell recorder to track a pybullet object
recorder.register_object(body_id, urdf_path)
for _ in range(500):
    p.stepSimulation()
    # 2. Take a snap shot of all registered link poses
    recorder.add_keyframe()
# 3. Dump simulation to a pickle file
recorder.save('demo.pkl')
