if class_name in ["person", "cat", "dog"]:
                        self.get_logger().warn(f"Living thing ({class_name}) → Moving Away!")
                    elif class_name in ["bottle", "cup"]:
                        self.get_logger().info(f"Useful object ({class_name}) → Approaching")
                    else:
                        self.get_logger().info(f"{class_name} detected.")

        msg = self.bridge.cv2_to_imgmsg(img, encoding='bgr8')
        self.image_pub.publish(msg)


def main(args=None):
    rclpy.init(args=args)
    node = ME6_DualImage_Robot()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        node.get_logger().info('Shutting down...')
    finally:
        node.destroy_node()
        rclpy.shutdown()


if name == 'main':
    main()