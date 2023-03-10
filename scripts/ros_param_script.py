import rospy

rospy.init_node('params_study')

distro = rospy.get_param('/rosdistro')

rospy.set_param('~ros_priv_param', 'Hi, I am private =)')
rospy.set_param('ros_loc_param', 'Hi, I am local =)')
rospy.set_param('/ros_glob_param', 'Hi, I am global =)')

not_exist_param = rospy.get_param('i_do_not_exist')

try:
    not_exist_param = rospy.get_param('i_do_not_exist')
except:
    # Not exist or any kind of other problem - set default
    not_exist_param = 'Okay, now it`s default time =0'

not_exist_param = rospy.get_param('i_do_not_exist', 'default_value')

# Мы этот параметр ставили ранее
param_name_2_delete = '/ros_glob_param'

# Проверим список параметров, только уже через Python
param_list = rospy.get_param_names()
rospy.loginfo(param_list)

# Наличие можно проверить через функционал ROS    
if rospy.has_param(param_name_2_delete):
    rospy.loginfo('[ROSWay] Parameter exist')
else:
    rospy.loginfo('[ROSWay] Parameter not exist')
    
# И с проверкой удаляем его
if rospy.has_param(param_name_2_delete):
    rospy.delete_param(param_name_2_delete)
    
# Еще раз проверим:
if rospy.has_param(param_name_2_delete):
    rospy.loginfo('[ROSWay] Parameter exist')
else:
    rospy.loginfo('[ROSWay] Parameter not exist')