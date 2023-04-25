import rclpy
from rclpy.node import Node
import cv2
import numpy as np
from geometry_msgs.msg import Twist
import mediapipe as mp
import time
from std_msgs.msg import Int32, Float32
from sensor_msgs.msg import Image, LaserScan
from cv_bridge import CvBridge
import matplotlib.pyplot as plt 
from matplotlib.animation import FuncAnimation
import numpy
from scipy.signal import convolve, firwin


from geometry_msgs.msg import Twist
import pickle
import mediapipe as mp
import time
MEMORY = 50

my_frame  = numpy.zeros((MEMORY,2))


class TBDriver(Node):
    def __init__(self):
        super().__init__('subscriber')
        # self.subscription = self.create_subscription(Image,'/color/preview/image', self.listener_callback, 1)
        self.publisher = self.create_publisher(Twist, '/cmd_vel', 10)
        self.twist_msg = Twist()
        self.twist_msg.linear.x = 0.0  # 0.0 m/s
        self.twist_msg.angular.z = 0.4  # 0.4 rad/s
        
        # self.gest_subscription = self.create_subscription(
        #         Int32,
        #         '/gesture',
        #         self.gesture_callback,
        #         1)
        
        self.scan_subscribtion = self.create_subscription(
            LaserScan,
            '/scan',
            self.scan_callback,
            1)
        self.scan_subscribtion
        self.t0 = None
        self.history = None
        self.fig  = None
        self.i = 0
        
        self.image_subscription = self.create_subscription(
            Image,
            '/color/preview/image',
            self.image_callback,
            1)
        
        self.bridge = CvBridge()
        
        self.model_dict = pickle.load(open("/home/architjain/Downloads/Sign_Language_Grey_classifier_2.p", 'rb'))

        self.model = self.model_dict['model']
        self.cap = cv2.VideoCapture(0)
        self.key = [0,1,2,3,4,5,6,7,8,9]


        self.mp_hands = mp.solutions.hands
        self.mp_drawing = mp.solutions.drawing_utils
        self.mp_drawing_styles = mp.solutions.drawing_styles

        self.hands = self.mp_hands.Hands(static_image_mode=True, min_detection_confidence=0.7)
        timer_period = 0.1  # seconds
       
        # Create the timer
        self.timer = self.create_timer(timer_period, self.timer_callback)

        # initialize random variables
        self.front_range = 10.097986976
        self.gesture = 9
        self.tb_view = np.zeros((480, 640, 3), dtype=np.uint8)

        
    def timer_callback(self):
        data_aux = []
        x_ = []
        y_ = []

        ret, image = self.cap.read()
        
        H, W, _ = image.shape
        
        # Detection implementation #############################################################
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

        # image.flags.writeable = False
        # # results = hands.process(image)
        # image.flags.writeable = True


        # # Initialize the Mediapipe Hands model
        # mp_hands = mp.solutions.hands
        # hands = mp_hands.Hands(static_image_mode=False, max_num_hands=2, min_detection_confidence=0.85)

        # # Process the current frame with Mediapipe Hands model
        results = self.hands.process(image)

        if results.multi_hand_landmarks:
            count = 0
            for hand_landmarks in results.multi_hand_landmarks:
                # Extract the cx and cy coordinates of the landmarks and store them in a list
                if count < 1:
                    self.mp_drawing.draw_landmarks(
                        image,  # image to draw
                        hand_landmarks,  # model output
                        self.mp_hands.HAND_CONNECTIONS,  # hand connections
                        self.mp_drawing_styles.get_default_hand_landmarks_style(),
                        self.mp_drawing_styles.get_default_hand_connections_style())
                    count += 1
            count = 0
            for hand_landmarks in results.multi_hand_landmarks:
                if count < 1:
                    for i in range(len(hand_landmarks.landmark)):
                        x = hand_landmarks.landmark[i].x
                        y = hand_landmarks.landmark[i].y

                        x_.append(x)
                        y_.append(y)

                    for i in range(len(hand_landmarks.landmark)):
                        x = hand_landmarks.landmark[i].x
                        y = hand_landmarks.landmark[i].y
                        data_aux.append(x - min(x_))
                        data_aux.append(y - min(y_))
                    count += 1

            x1 = int(min(x_) * W) - 10
            y1 = int(min(y_) * H) - 10

            x2 = int(max(x_) * W) - 10
            y2 = int(max(y_) * H) - 10

            prediction = self.model.predict([np.asarray(data_aux)])

            predicted_character = self.key[int(prediction[0])]

            cv2.rectangle(image, (x1, y1), (x2, y2), (0, 0, 0), 4)
            cv2.putText(image, str(predicted_character), (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 1.3, (0, 0, 0), 3,
                        cv2.LINE_AA)

            print(predicted_character)
            self.gesture = int(predicted_character)
            
            

        cv2.imshow('User Video', image)
        cv2.waitKey(1)


    def publish_twist(self):
        self.publisher.publish(self.twist_msg)
        self.get_logger().info('Publishing Twist message: linear=%f, angular=%f' %
                                    (self.twist_msg.linear.x, self.twist_msg.angular.z))
        
    def scan_callback(self, msg):
            # Get the range at the center of the scan
        range_index = len(msg.ranges) // 4
        range_value = msg.ranges[range_index]

        # Print the range in front of the robot
        self.get_logger().info(f'Range in front of the robot: {range_value:.6f}')
        current_time = msg.header.stamp.sec+msg.header.stamp.nanosec*1e-9
        if not self.t0:
            self.t0 = current_time

        t = current_time-self.t0


        if self.history is None:
            self.history = numpy.zeros((MEMORY,2))

        self.history[:-1,:] = self.history[1:,:]
        self.history[-1,:] = numpy.array([t, range_value])
        self.update(self.i)

    def update(self,i):

        if self.fig is None:
            first = True
            self.fig = plt.figure()
            self.ax = plt.subplot(111)
        else:
            first = False
        

        # #Apply FIR Filter
        x = self.history[:,1]
        time = self.history[:, 0]

        # Define the filter coefficients using the firwin function
        filter_order = 10
        cutoff_freq = 0.1
        b = firwin(filter_order, cutoff_freq)

        # Apply the filter using the convolve function
        y = convolve(x, b, mode='valid')

        
        self.front_range = y[-1]
        self.get_logger().info(f'Range in front: {y[-1]:.2f}')

        # Plot Everything
        self.ax.cla()
        self.ax.plot(self.history[filter_order:,0],self.history[filter_order:,1], label="Scan Range")
        self.ax.plot(time[filter_order-1:], y, label = "FIR Filtered Data")
        # self.ax.set_ylim(self.history[:,1].min(),self.history[:,1].max())    # plot memory
        self.fig.canvas.draw()
        if first:
            plt.ion()
            plt.show()
    
    def gesture_callback(self, msg):
            self.gesture = msg.data
    
    def image_callback(self, msg):
        # Store the image data from the /image topic
        self.tb_view = self.bridge.imgmsg_to_cv2(msg)

    def process_data(self):
        # Do something with the data from all three topics
        
    
        tb_view2 = self.tb_view
        
        if self.gesture == 1:
            if self.front_range > 0.35:
                self.twist_msg.linear.x = 0.2
                self.twist_msg.angular.z = 0.0
            else:
                self.twist_msg.linear.x = 0.0
                self.twist_msg.angular.z = 0.0
                tb_view2[:,:,2] = np.clip(tb_view2[:,:,2] + 100, 0, 255)
                # Add text to the image
                font = cv2.FONT_HERSHEY_SIMPLEX
                bottomLeftCornerOfText = (10, 50)
                fontScale = 1
                fontColor = (0, 0, 255) # red
                lineType = 2
                cv2.putText(tb_view2, 'Robot will crash into object', 
                    bottomLeftCornerOfText, font, fontScale, fontColor, lineType)

        elif self.gesture == 2:
            self.twist_msg.linear.x = -0.2
            self.twist_msg.angular.z = 0.0
        elif self.gesture == 3:
            self.twist_msg.linear.x = 0.0
            self.twist_msg.angular.z = -0.4
        elif self.gesture == 4:
            self.twist_msg.linear.x = 0.0
            self.twist_msg.angular.z = 0.4
        elif self.gesture == 5:
            self.twist_msg.linear.x = 0.0
            self.twist_msg.angular.z = 0.0
        self.publish_twist()
        cv2.imshow('Turtlebot Live View', tb_view2)
        cv2.waitKey(1)



def main(args=None):
    rclpy.init(args=args)
    tbdriver = TBDriver()
    
    plt.ion()
    plt.show()
    
    while rclpy.ok():
        tbdriver.process_data()
        rclpy.spin_once(tbdriver)

    tbdriver.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()