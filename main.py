# from utils.video_utils import read_video, save_video
# from trackers.trackers import Tracker
# import cv2
# from team_assigner.team_assigner import TeamAssigner
# from player_ball_assigner.player_ball_assigner import PlayerBallAssigner
# import numpy as np
# from camera_movement_estimator.camera_movement_estimator import CameraMovementEstimator
# from view_transformer.view_transformer import ViewTransformer
# from speed_and_distance_estimator import SpeedAndDistance_Estimator

# def main():
#     # Đọc video
#     video_frames = read_video('input_video/t.png')

#     # Tracker
#     tracker = Tracker('models/best.pt')
#     tracks = tracker.get_object_tracks(video_frames,
#                                        read_from_stub=True,
#                                        stub_path='stubs/track_stubs.pkl')
#     # get object positions first (needed by camera adjustment)
#     tracker.add_position_to_tracks(tracks)

#     # camera movement estimator
#     camera_movement_estimator= CameraMovementEstimator(video_frames[0])
#     camera_movement_per_frame = camera_movement_estimator.get_camera_movement(video_frames,
#                                                                                 read_from_stub=True,
#                                                                                 stub_path='stubs/camera_movement_stub.pkl')
#     camera_movement_estimator.add_adjust_positions_to_tracks(tracks,camera_movement_per_frame)
    
#     #get obj positions
#     tracker.add_position_to_tracks(tracks)

#     #view transformer
#     view_transformer = ViewTransformer()
#     view_transformer.add_transformed_position_to_tracks(tracks)
    
#     #interpolate ball positions
#     tracks["ball"]=tracker.interpolate_ball_positions(tracks["ball"])

#     #Speed and distance
#     speed_and_distance_estimator = SpeedAndDistance_Estimator()
#     speed_and_distance_estimator.add_speed_and_distance_to_tracks(tracks)

#     # Assign Player Teams
#     team_assigner = TeamAssigner()
#     team_assigner.assign_team_color(video_frames[0],
#                                     tracks['players'][0])

#     for frame_num, player_track in enumerate(tracks['players']):
#         for player_id, track in player_track.items():
#             team = team_assigner.get_player_team(video_frames[frame_num],
#                                                  track['bbox'],
#                                                  player_id)
#             tracks['players'][frame_num][player_id]['team'] = team
#             tracks['players'][frame_num][player_id]['team_color'] = team_assigner.team_colors[team]

#     # assign ball acquisition
#     player_assigner = PlayerBallAssigner()
#     team_ball_control= []
#     for frame_num, player_track in enumerate(tracks['players']):
#         ball_bbox = tracks['ball'][frame_num][1]['bbox']
#         assigned_player = player_assigner.assign_ball_to_player(player_track, ball_bbox)

#         if assigned_player != -1:
#             tracks['players'][frame_num][assigned_player]['has_ball'] = True
#             team_ball_control.append(tracks['players'][frame_num][assigned_player]['team'])
#         else:
#             team_ball_control.append(team_ball_control[-1])
#     team_ball_control= np.array(team_ball_control)

#     # Save cropped
#     for track_id, player in tracks['players'][0].items():
#         bbox = player['bbox']
#         frame = video_frames[0]

#         cropped_image = frame[int(bbox[1]):int(bbox[3]),
#                               int(bbox[0]):int(bbox[2])]
#         cv2.imwrite(f'output_videos/cropped_{track_id}.jpg', cropped_image)
#         break

#     # Vẽ output
#     output_video_frames = tracker.draw_annotations(video_frames, tracks,team_ball_control)

#     # draw camera movement
#     output_video_frames = camera_movement_estimator.draw_camera_movement(output_video_frames,camera_movement_per_frame)

#     ## Draw Speed and Distance
#     speed_and_distance_estimator.draw_speed_and_distance(output_video_frames,tracks)

#     # Lưu video
#     save_video(output_video_frames, 'output_videos/output_t.avi')

# if __name__ == '__main__':
#     main()



from utils.video_utils import read_video, save_video
from trackers.trackers import Tracker
import cv2
from team_assigner.team_assigner import TeamAssigner
from player_ball_assigner.player_ball_assigner import PlayerBallAssigner
import numpy as np
from camera_movement_estimator.camera_movement_estimator import CameraMovementEstimator
from view_transformer.view_transformer import ViewTransformer
from speed_and_distance_estimator import SpeedAndDistance_Estimator


def main():
    print("📂 Đang đọc video...")
    video_frames = read_video('input_video/test (6).mp4')  # 👉 đổi tên file video nếu cần
    print(f"✅ Đã đọc {len(video_frames)} frames")

    print("🎯 Khởi tạo tracker...")
    tracker = Tracker('models/best.pt')

    # 👉 Đọc tracking từ cache nếu có, tránh tốn thời gian detect lại
    tracks = tracker.get_object_tracks(
        video_frames,
        read_from_stub=True,
        stub_path='stubs/track_stubs.pkl'
    )
    print("✅ Tracking hoàn tất")

    # 👉 Thêm toạ độ cho mỗi object (rất quan trọng)
    tracker.add_position_to_tracks(tracks)

    print("📷 Ước lượng chuyển động camera...")
    camera_movement_estimator = CameraMovementEstimator(video_frames[0])
    camera_movement_per_frame = camera_movement_estimator.get_camera_movement(
        video_frames,
        read_from_stub=True,
        stub_path='stubs/camera_movement_stub.pkl'
    )

    # 👉 Điều chỉnh lại vị trí object theo chuyển động camera
    camera_movement_estimator.add_adjust_positions_to_tracks(tracks, camera_movement_per_frame)
    print("✅ Camera movement OK")

    print("🌍 Chuyển toạ độ sang view cố định (ViewTransformer)...")
    view_transformer = ViewTransformer()
    view_transformer.add_transformed_position_to_tracks(tracks)

    print("⚽ Nội suy vị trí bóng...")
    tracks["ball"] = tracker.interpolate_ball_positions(tracks["ball"])

    print("⏱️ Tính tốc độ và khoảng cách di chuyển...")
    speed_and_distance_estimator = SpeedAndDistance_Estimator()
    speed_and_distance_estimator.add_speed_and_distance_to_tracks(tracks)

    print("👕 Gán team cho cầu thủ...")
    team_assigner = TeamAssigner()
    team_assigner.assign_team_color(video_frames[0], tracks['players'][0])

    # Gán team cho từng cầu thủ trong từng frame
    for frame_num, player_track in enumerate(tracks['players']):
        for player_id, track in player_track.items():
            team = team_assigner.get_player_team(video_frames[frame_num], track['bbox'], player_id)
            tracks['players'][frame_num][player_id]['team'] = team
            tracks['players'][frame_num][player_id]['team_color'] = team_assigner.team_colors[team]

    print("⚽ Gán cầu thủ đang giữ bóng...")
    player_assigner = PlayerBallAssigner()
    team_ball_control = []

    for frame_num, player_track in enumerate(tracks['players']):
        if len(tracks['ball'][frame_num]) == 0:
            team_ball_control.append(team_ball_control[-1] if len(team_ball_control) > 0 else 0)
            continue

        ball_bbox = tracks['ball'][frame_num][1]['bbox']
        assigned_player = player_assigner.assign_ball_to_player(player_track, ball_bbox)

        if assigned_player != -1:
            tracks['players'][frame_num][assigned_player]['has_ball'] = True
            team_ball_control.append(tracks['players'][frame_num][assigned_player]['team'])
        else:
            team_ball_control.append(team_ball_control[-1] if len(team_ball_control) > 0 else 0)
    team_ball_control = np.array(team_ball_control)

    print("✂️ Lưu ảnh crop cầu thủ (1 mẫu)...")
    for track_id, player in tracks['players'][0].items():
        bbox = player['bbox']
        frame = video_frames[0]
        cropped_image = frame[int(bbox[1]):int(bbox[3]), int(bbox[0]):int(bbox[2])]
        cv2.imwrite(f'output_videos/cropped_{track_id}.jpg', cropped_image)
        break

    print("🖼️ Vẽ annotation lên video...")
    output_video_frames = tracker.draw_annotations(video_frames, tracks, team_ball_control)

    print("📷 Vẽ vector chuyển động camera...")
    output_video_frames = camera_movement_estimator.draw_camera_movement(
        output_video_frames, camera_movement_per_frame
    )

    print("⏱️ Vẽ tốc độ và khoảng cách di chuyển...")
    speed_and_distance_estimator.draw_speed_and_distance(output_video_frames, tracks)

    print("💾 Lưu video kết quả...")
    save_video(output_video_frames, 'output_videos/output_result.avi')
    print("✅ Hoàn tất! Video lưu tại: output_videos/output_result.avi")


if __name__ == '__main__':
    main()


# from utils.video_utils import read_video, save_video
# from trackers.trackers import Tracker
# import cv2
# from team_assigner.team_assigner import TeamAssigner
# from player_ball_assigner.player_ball_assigner import PlayerBallAssigner
# import numpy as np
# from camera_movement_estimator.camera_movement_estimator import CameraMovementEstimator
# from view_transformer.view_transformer import ViewTransformer
# from speed_and_distance_estimator import SpeedAndDistance_Estimator

# def main():
#     print("📂 Đang đọc video...")
#     # video_frames = read_video('input_video/08fd33_4.mp4')
#     video_frames = read_video('input_video/test (6).mp4')
#     print(f"✅ Video đã load: {len(video_frames)} frames")

#     print("🎯 Khởi tạo tracker...")
#     tracker = Tracker('models/best.pt')
#     tracks = tracker.get_object_tracks(
#         video_frames,
#         read_from_stub=True,
#         stub_path='stubs/track_stubs.pkl'
#     )
#     print("✅ Tracker đã xử lý xong")

#     print("📷 Tính toán camera movement...")
#     camera_movement_estimator = CameraMovementEstimator(video_frames[0])
#     camera_movement_per_frame = camera_movement_estimator.get_camera_movement(
#         video_frames,
#         read_from_stub=True,
#         stub_path='stubs/camera_movement_stub.pkl'
#     )
#     camera_movement_estimator.add_adjust_positions_to_tracks(tracks, camera_movement_per_frame)
#     print("✅ Camera movement OK")

#     print("📌 Thêm vị trí object...")
#     tracker.add_position_to_tracks(tracks)

#     print("🌍 View Transformer...")
#     view_transformer = ViewTransformer()
#     view_transformer.add_transformed_position_to_tracks(tracks)

#     print("⚽ Nội suy vị trí bóng...")
#     tracks["ball"] = tracker.interpolate_ball_positions(tracks["ball"])

#     print("⏱️ Tính tốc độ và khoảng cách...")
#     speed_and_distance_estimator = SpeedAndDistance_Estimator()
#     speed_and_distance_estimator.add_speed_and_distance_to_tracks(tracks)

#     print("👕 Gán team...")
#     team_assigner = TeamAssigner()
#     team_assigner.assign_team_color(video_frames[0], tracks['players'][0])

#     for frame_num, player_track in enumerate(tracks['players']):
#         for player_id, track in player_track.items():
#             team = team_assigner.get_player_team(video_frames[frame_num], track['bbox'], player_id)
#             tracks['players'][frame_num][player_id]['team'] = team
#             tracks['players'][frame_num][player_id]['team_color'] = team_assigner.team_colors[team]

#     print("⚽ Gán bóng cho cầu thủ...")
#     player_assigner = PlayerBallAssigner()
#     team_ball_control = []
#     for frame_num, player_track in enumerate(tracks['players']):
#         ball_bbox = tracks['ball'][frame_num][1]['bbox']
#         assigned_player = player_assigner.assign_ball_to_player(player_track, ball_bbox)

#         if assigned_player != -1:
#             tracks['players'][frame_num][assigned_player]['has_ball'] = True
#             team_ball_control.append(tracks['players'][frame_num][assigned_player]['team'])
#         else:
#             team_ball_control.append(team_ball_control[-1])
#     team_ball_control = np.array(team_ball_control)

#     print("✂️ Lưu ảnh crop cầu thủ...")
#     for track_id, player in tracks['players'][0].items():
#         bbox = player['bbox']
#         frame = video_frames[0]
#         cropped_image = frame[int(bbox[1]):int(bbox[3]), int(bbox[0]):int(bbox[2])]
#         cv2.imwrite(f'output_videos/cropped_{track_id}.jpg', cropped_image)
#         break

#     print("🖼️ Vẽ annotation...")
#     output_video_frames = tracker.draw_annotations(video_frames, tracks, team_ball_control)

#     print("📷 Vẽ camera movement...")
#     output_video_frames = camera_movement_estimator.draw_camera_movement(output_video_frames, camera_movement_per_frame)

#     print("⏱️ Vẽ tốc độ và khoảng cách...")
#     speed_and_distance_estimator.draw_speed_and_distance(output_video_frames, tracks)

#     print("💾 Lưu video...")
#     save_video(output_video_frames, 'output_videos/output_video6.avi')
#     print("✅ Hoàn tất! File đã lưu tại: output_videos/output_video1.avi")

# if __name__ == '__main__':
#     main()
