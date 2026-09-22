<div dir="rtl" align="right">

<style>
.tg-channel-box {
  max-width: 800px;
  margin: 0 auto;
  padding: 16px;
  font-family: system-ui, -apple-system, 'Segoe UI', 'Vazirmatn', Tahoma, sans-serif;
  background: #fafafa;
  border-radius: 20px;
  line-height: 1.7;
}

/* حالت دارک برای کسانی که تم دارک دارن */
@media (prefers-color-scheme: dark) {
  .tg-channel-box {
    background: #1a1a2e;
    color: #eee;
  }
  .tg-post {
    background: #16213e;
    border-color: #0f3460;
  }
  .tg-post-header {
    background: #0f3460;
  }
  .tg-footer {
    color: #aaa;
  }
  .tg-text a {
    color: #7eb6ff;
  }
}

/* کارت پست */
.tg-post {
  background: white;
  border-radius: 20px;
  padding: 18px 22px;
  margin: 20px 0;
  box-shadow: 0 2px 8px rgba(0,0,0,0.08);
  border: 1px solid #e5e7eb;
  transition: box-shadow 0.2s;
}
.tg-post:hover {
  box-shadow: 0 8px 20px rgba(0,0,0,0.1);
}
.tg-post-header {
  background: #f3f4f6;
  margin: -18px -22px 16px -22px;
  padding: 10px 22px;
  border-radius: 20px 20px 0 0;
  font-size: 13px;
  color: #4b5563;
  border-bottom: 1px solid #e5e7eb;
}

/* نقل قول / فوروارد */
.tg-forward {
  background: #eef2ff;
  border-right: 4px solid #3b82f6;
  padding: 8px 14px;
  border-radius: 12px;
  margin: 12px 0;
  font-size: 13px;
  color: #1e40af;
}

/* متن */
.tg-text {
  font-size: 16px;
  margin: 14px 0;
}
.tg-text a {
  color: #2563eb;
  text-decoration: none;
}
.tg-text a:hover {
  text-decoration: underline;
}

/* تصاویر */
.tg-photo {
  margin: 12px 0;
  text-align: center;
}
.tg-photo img {
  max-width: 100%;
  border-radius: 16px;
  box-shadow: 0 2px 8px rgba(0,0,0,0.1);
}

/* آلبوم */
.tg-album {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(150px, 1fr));
  gap: 8px;
  margin: 12px 0;
}
.tg-album-item {
  overflow: hidden;
  border-radius: 12px;
}
.tg-album-item img {
  width: 100%;
  height: 150px;
  object-fit: cover;
  transition: transform 0.2s;
}
.tg-album-item img:hover {
  transform: scale(1.02);
}

/* ویدیو */
.tg-video {
  margin: 12px 0;
}
.tg-video video {
  width: 100%;
  border-radius: 16px;
  background: black;
}
.tg-dl-btn {
  display: inline-block;
  background: #3b82f6;
  color: white;
  padding: 6px 14px;
  border-radius: 24px;
  font-size: 13px;
  text-decoration: none;
  margin-top: 6px;
}
.tg-dl-btn:hover {
  background: #2563eb;
}

/* فایل */
.tg-doc {
  background: #f9fafb;
  border: 1px solid #e5e7eb;
  border-radius: 16px;
  padding: 12px 16px;
  margin: 12px 0;
  display: flex;
  align-items: center;
  gap: 12px;
}
.tg-doc-icon {
  font-size: 32px;
}
.tg-doc-info {
  flex: 1;
}
.tg-doc-title {
  font-weight: 600;
}
.tg-doc-extra {
  font-size: 12px;
  color: #6b7280;
}
.tg-doc-link {
  background: #3b82f6;
  color: white;
  padding: 6px 12px;
  border-radius: 20px;
  font-size: 12px;
  text-decoration: none;
}

/* نظرسنجی */
.tg-poll {
  background: #fef9e3;
  border: 1px solid #fde047;
  border-radius: 20px;
  padding: 12px 18px;
  margin: 12px 0;
}
.tg-poll h4 {
  margin: 0 0 10px 0;
  color: #854d0e;
}
.tg-poll ul {
  margin: 0;
  padding-right: 20px;
}
.tg-poll li {
  margin: 6px 0;
  color: #a16207;
}

/* فوتر پست (تاریخ و بازدید) */
.tg-footer {
  font-size: 12px;
  color: #9ca3af;
  margin-top: 12px;
  padding-top: 8px;
  border-top: 1px solid #e5e7eb;
  display: flex;
  gap: 12px;
  justify-content: flex-end;
}
.tg-footer a {
  color: #6b7280;
  text-decoration: none;
}
.tg-footer a:hover {
  color: #3b82f6;
}

/* هدر کانال */
.tg-channel-header {
  text-align: center;
  padding: 20px;
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  border-radius: 28px;
  color: white;
  margin-bottom: 24px;
}
.tg-avatar {
  width: 80px;
  height: 80px;
  border-radius: 50%;
  border: 4px solid white;
  margin-bottom: 12px;
}
.tg-channel-header h1 {
  margin: 8px 0 4px;
  font-size: 24px;
}
.tg-channel-header p {
  margin: 4px 0;
  opacity: 0.9;
}
.tg-channel-desc {
  background: #f3f4f6;
  padding: 14px 20px;
  border-radius: 20px;
  margin: 16px 0;
  font-size: 14px;
  color: #374151;
}
.tg-last-update {
  text-align: center;
  font-size: 12px;
  color: #9ca3af;
  margin: 16px 0;
}
.tg-telegram-btn {
  display: inline-block;
  background: #1e88e5;
  color: white;
  padding: 8px 18px;
  border-radius: 30px;
  text-decoration: none;
  margin: 12px 0;
  font-weight: 500;
}
.tg-telegram-btn:hover {
  background: #0b5e8a;
}
@media (prefers-color-scheme: dark) {
  .tg-channel-desc {
    background: #1f2937;
    color: #d1d5db;
  }
  .tg-post {
    background: #1e1e2f;
    border-color: #2d2d44;
  }
  .tg-post-header {
    background: #2a2a3b;
    color: #bbb;
    border-color: #3a3a52;
  }
  .tg-doc {
    background: #252535;
    border-color: #3a3a52;
  }
  .tg-forward {
    background: #1f2a3a;
    color: #90cdf4;
  }
}
</style>

<div class="tg-channel-box">

<div class="tg-channel-header">
<img src="https://cdn5.telesco.pe/file/Rxp8Jq9QvP9p3SkvCpTHyogW1RcAwetaXZ9QozbjxXtqt2WklehWBWAZD0pXzBgQf38ftqx7Nf8zir0TntWrpp2iFvHyDW7NXhhVvNA0HBB1WJrdkMzSmJ9dDwAPaXDqOq6FSwcGnZxbjYo_wQD_H9099OR10x0oj5eR-Z-mol5l5qeALhCjH7mXw9ItxijRKKPM8pyCYESskuhdSAWglqCn2STWpxJUj4e5A-fBuJAbkSJsScdnUpMDlsDq-HKskEl0cXazeXG_H467uKlISMRKXfRuOWvVUBwcNFoz8IVSFYxwjLqBnVGSJfLNOvpb-vY-P66mry8nZe6Gszneaw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فوتبال 180</h1>
<p>@Futball180TV • 👥 405K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-31 13:38:24</div>
<hr>

<div class="tg-post" id="msg-107060">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/548065ddaf.mp4?token=uhlI1_lKCjwriiVu4VDdjkVZz2LHSLABGN7l6vJWeo_wxssD-XSeKGsbB419yxNAjDkQW1fD2ghpRFFvena4ranGrsLQXeipv20hvJrRr91QUWn-YZPSUKU7kAbOUPIgU087m0bdxMAXv5ZiI-FErwpd6BQkgDDsBFzTG4w6TbKWXeNWOaGHgGGyhVA430TpXP0ab8uSAiDbXVjJFgXtjTiuxP1vkO-78yvFNJMJIL57aqo5x1oXe74Lp4bt1gc7OJl8OSAeAXDQgcjMCD-IoLCFMPqDrfpjTJDo9A3B46at7NbXk0ggxeMH2jjAr7rSN0wb5mnJrMH25ysXhACP0w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/548065ddaf.mp4?token=uhlI1_lKCjwriiVu4VDdjkVZz2LHSLABGN7l6vJWeo_wxssD-XSeKGsbB419yxNAjDkQW1fD2ghpRFFvena4ranGrsLQXeipv20hvJrRr91QUWn-YZPSUKU7kAbOUPIgU087m0bdxMAXv5ZiI-FErwpd6BQkgDDsBFzTG4w6TbKWXeNWOaGHgGGyhVA430TpXP0ab8uSAiDbXVjJFgXtjTiuxP1vkO-78yvFNJMJIL57aqo5x1oXe74Lp4bt1gc7OJl8OSAeAXDQgcjMCD-IoLCFMPqDrfpjTJDo9A3B46at7NbXk0ggxeMH2jjAr7rSN0wb5mnJrMH25ysXhACP0w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🙂
علت جدایی ابوطالب از عادل فردوسی‌پور
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 1.22K · <a href="https://t.me/Futball180TV/107060" target="_blank">📅 13:35 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107059">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b38289f78f.mp4?token=s0QGHYJcWSWaRk4KJg8BQ8DjdjFA-RLGvaHAzGpj8LCdVRpO_ZZs6c8O9ClK7E27KV0opBv6fTys1cvWl9YEd_z0GiWxu_4ZVn5yNibebqdDuJxvLB-MgsrVBF5LVj2QNnMU0TawSZAK64SeIjCixqHDE_0zd1axiSvS9hTId_q55uZ0BaRDJ6vPpsNOadW4n0pyTgaotHWZgWCgq5XJE5goxjZha4XKGS4jn7004tCTIwA7CgXYJFhOigHZKvknybERaDhwsBfCjNtPXBW4FM2aHF8WCcFM7wIAkJX4d7jm03nda2V4ssRDzsrcaENkjrJZaBZtLl-SAQTyxzs_6A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b38289f78f.mp4?token=s0QGHYJcWSWaRk4KJg8BQ8DjdjFA-RLGvaHAzGpj8LCdVRpO_ZZs6c8O9ClK7E27KV0opBv6fTys1cvWl9YEd_z0GiWxu_4ZVn5yNibebqdDuJxvLB-MgsrVBF5LVj2QNnMU0TawSZAK64SeIjCixqHDE_0zd1axiSvS9hTId_q55uZ0BaRDJ6vPpsNOadW4n0pyTgaotHWZgWCgq5XJE5goxjZha4XKGS4jn7004tCTIwA7CgXYJFhOigHZKvknybERaDhwsBfCjNtPXBW4FM2aHF8WCcFM7wIAkJX4d7jm03nda2V4ssRDzsrcaENkjrJZaBZtLl-SAQTyxzs_6A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
❤️
‼️
دیس سنگین ابوطالب به خداداد عزیزی: قلب آدم صاف باشه نه پاهاش، شما قلبت پرانتزیه آقای خداداد عزیزی!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.55K · <a href="https://t.me/Futball180TV/107059" target="_blank">📅 13:08 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107058">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/19fc9edd61.mp4?token=T4pWRefd2-auLeYzncGuQuGkTJoBLXoE5QdQv2KAhw_Nob8_wGKvMqn1SfETLMRTjcnUMrmJQgak5w0NVLl--0pFhQWfHqO-52ZAS7Hntb0LPipNjk0g5_PU7qqFb70jMqPblK1BDOADjL3VlgLLc0kWu1iwj652L1MBRVHUqjG1yr66x_1RnaZnQeBPvyXZ8NDWy5wd-wr20vsVyJGhrz2l9baK4X6OMYyWQw2YL0X6IQLwIov6U77HUIXAIJZZPSPoyY9bdClK_alFZKFYcck78BoUx8-o15CVHu0cjQzA_v1473kRmolXvzyzg-2YQV6ZHD7AUKey5dvqvPmgHQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/19fc9edd61.mp4?token=T4pWRefd2-auLeYzncGuQuGkTJoBLXoE5QdQv2KAhw_Nob8_wGKvMqn1SfETLMRTjcnUMrmJQgak5w0NVLl--0pFhQWfHqO-52ZAS7Hntb0LPipNjk0g5_PU7qqFb70jMqPblK1BDOADjL3VlgLLc0kWu1iwj652L1MBRVHUqjG1yr66x_1RnaZnQeBPvyXZ8NDWy5wd-wr20vsVyJGhrz2l9baK4X6OMYyWQw2YL0X6IQLwIov6U77HUIXAIJZZPSPoyY9bdClK_alFZKFYcck78BoUx8-o15CVHu0cjQzA_v1473kRmolXvzyzg-2YQV6ZHD7AUKey5dvqvPmgHQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
😆
‼️
ابوطالب حسینی ویس لو رفته خداداد عزیزی رو مودبانه ترجمه کرده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.29K · <a href="https://t.me/Futball180TV/107058" target="_blank">📅 12:37 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107057">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Nxu1REMRxhqvMrVb4RafdpYlqSIjNtBkfU2o4cTAZALYlmZSnCuoG_dT6Mu7Eeo2jmWbF1JpZQgE0yCy-I5ebfYPA_3ty2myRc3fci4xkURdgdozyshiDMM7ROh5G82_MmuIzCMslfXfWP2G_y-gM6hoJEzozFgkmXk6mupXtrGF-RJyJ49EEH7MUT6YDkwN6htQVV2bMt0_L3gNpqAVy29jQjzR4ssduo4joPKEaRO6pKMzbKE52T3xSwqGQt64FBtw23Ije4bMDz5Y1so5zxMNMJ_2IGkoP5nRSM6-Lb69EW8Gvdk3JLoxQva-DXPKllx-5ECub_saIV9bOJ4Jcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آقای ابوالفضل جلالی فکر کرده در عصر قاجاریه داریم زندگی می‌کنیم. چطور اینقدر راحت دروغ میگن
😆
😆
😆
😆
😆
😆
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.89K · <a href="https://t.me/Futball180TV/107057" target="_blank">📅 12:30 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107056">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H_Se-SuPYTTCVElS_1Re-ngyhptFqgaMkqUtBbkkjO28pxnA7TMXtjFyMvuxZfAczfMd5TrEs_i3KgL-Fft5lnir1Pil6YllufS5ziTAkQswyoyaf0zpepVQ1HxMxoBiCbADQnI_lPJ-b_6wZlxGt_AjVT-6gUpXJE6PmxyvGeXvSMi4GJGoQtgjJhQyflXCWaiUG9CF2VhtpJu6NxVtPNgb0dXmw93_FLKWmHTRQYKftuPgklDhWtTZzfDo-LPSK7dchW7dzcPdlju8VPeIeTOLx0vS0IIdjyXA1jmAF4Dw_wE5xlhrxv3I-0dfV2TJBMUZRrcUB-SXDqHk21yudw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
جمع سن سه نفر جلو: 110 سال
احتمال فیکس شدن هر سه بازیکن تو جام ملتهای آسیا هم زیاده. جوان‌گرایی بی‌نظیر امیر قلعه نویی بعد از سال چهارم مربیگریش در تیم ملی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.41K · <a href="https://t.me/Futball180TV/107056" target="_blank">📅 12:20 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107055">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1aa420985a.mp4?token=h5QHsx2ApRpJMVR4BV5dM39c4Oju8AolqNLq7zqOPkBESCDWCheJ2BzVT_PKxR91H9qHy1033IZ7tEs7-n59j1OcL11RThkhHSJUBuldJ6er-6bkQd9ANDAfzL3dT0cs8Qwwxb5y1iX14XMuNQWn7MJxRwFM0u1EXU4H74h28bb_YhC5Amw1SgsVPOJTB7Dz4jZSTsLjj4qrn8XfwC8wNN9tu00KlaaWNg2NW_7GtANCjp7IoKAcMdEjIb7BcjIx_S8OQRvQCcAq4Yz55hvckxuVM8OpJTAkicjegCeSbXmNxLDcvlJNBwFvrthSg6FjSS_-qoCo17xkUKse_4DPUA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1aa420985a.mp4?token=h5QHsx2ApRpJMVR4BV5dM39c4Oju8AolqNLq7zqOPkBESCDWCheJ2BzVT_PKxR91H9qHy1033IZ7tEs7-n59j1OcL11RThkhHSJUBuldJ6er-6bkQd9ANDAfzL3dT0cs8Qwwxb5y1iX14XMuNQWn7MJxRwFM0u1EXU4H74h28bb_YhC5Amw1SgsVPOJTB7Dz4jZSTsLjj4qrn8XfwC8wNN9tu00KlaaWNg2NW_7GtANCjp7IoKAcMdEjIb7BcjIx_S8OQRvQCcAq4Yz55hvckxuVM8OpJTAkicjegCeSbXmNxLDcvlJNBwFvrthSg6FjSS_-qoCo17xkUKse_4DPUA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شما هم از فیفادی بدتون میاد
🙄
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.95K · <a href="https://t.me/Futball180TV/107055" target="_blank">📅 11:55 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107054">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3c092ad06d.mp4?token=SIXfExxcTp2Hs4NaJw8RHAY8suqzhj89IMgxlqkuovHmBQfr1mcDC1TOVVDBLjQpvTuVFJsN5TUDDUnNmOIhlIhEje0WbKEH_EP1PzbMRxzx_PhRJ2s2UmB1tzQb6Co-JJycIWIb30D4SYYpr3bnMXO0ls_WjfB52QAH-07XhES2HRusYywgeluKsbqBDDlo-_XW1QbG1141-Se5RwIB94hOak9ug9TNjTU23xCYnDkperogIuTePZ5iZde5XYx9rHh2-XUOCnxmc8f-jcUtH7eiLstgIodvwN39INBAHtK6WpJKoOK6JMQTxCdDPOIV6-lYYnhcK3kYl1QWuQdVxA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3c092ad06d.mp4?token=SIXfExxcTp2Hs4NaJw8RHAY8suqzhj89IMgxlqkuovHmBQfr1mcDC1TOVVDBLjQpvTuVFJsN5TUDDUnNmOIhlIhEje0WbKEH_EP1PzbMRxzx_PhRJ2s2UmB1tzQb6Co-JJycIWIb30D4SYYpr3bnMXO0ls_WjfB52QAH-07XhES2HRusYywgeluKsbqBDDlo-_XW1QbG1141-Se5RwIB94hOak9ug9TNjTU23xCYnDkperogIuTePZ5iZde5XYx9rHh2-XUOCnxmc8f-jcUtH7eiLstgIodvwN39INBAHtK6WpJKoOK6JMQTxCdDPOIV6-lYYnhcK3kYl1QWuQdVxA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🇳🇱
اولین تمرین لاله‌های نارنجی زیر نظر ژاوی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.75K · <a href="https://t.me/Futball180TV/107054" target="_blank">📅 11:40 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107053">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/Futball180TV/107053" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 8.28K · <a href="https://t.me/Futball180TV/107053" target="_blank">📅 11:39 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107052">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pvs4FKoB-KAIoZCyB70qNE1-x6W1ImzMd05VYSNAKh5CCkqrdJ-AW_QkbtnLWerWZI0aWbPX25sr4QM31bkmPYN9vxdoufoLCSlX15W4frcT0pqZssXfkZ3npelpBgP8XbUI9Ayg18h3Pd2I7YhKBCSJhPgkVdAw10C0IdGecCG1mBGDw4UhNeP5G72m85I3A5j9Yxp1aCglZxB7ICj531BozJWoe075E3PVEvCZNcpKhihAnWTY6fjBevXgx54xiLVvopGpcwnJoIJR6_hHPktpNtDDgI7whZFKmOcK_ysWgFXJUfdqpCLKgiMNjXE5xbMMV_ejrlZrhI0xrMg80Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
با اولین واریز، بیشتر دریافت کن!  فقط در سایت جهانی
TrexBet
🦖
بسته خوش‌آمدگویی ویژه
TrexBet
تا ۱۰۰٪ بونوس واریز
🦖
تا ۱۵۰ چرخش رایگان در ۴ واریز اول
🥇
واریز اول: ۱۰۰٪ بونوس + ۳۰ چرخش رایگان
🥈
واریز دوم: ۵۰٪ بونوس + ۳۵ چرخش رایگان
🥉
واریز سوم: ۲۵٪ بونوس + ۴۰ چرخش رایگان
🏅
واریز چهارم: ۲۵٪ بونوس + ۴۵ چرخش رایگان
🦖
🦖
🦖
🦖
🦖
🦖
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 8.28K · <a href="https://t.me/Futball180TV/107052" target="_blank">📅 11:39 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107051">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O5JSOOLoajzxOpFU5rKmpViaKxE5gTd6UlD9HbdlUiBNsuYWajI9ihENo3f9sDQUmMHbS-MXRlUF_89gVjYxRpcfIZi1nYxc1jpWDsd8FuBnVndsRB-arpqtw6sWqZ1cx7WDMJc-PlQBZnp7xknQUhg5JbGHbrSzcO6FMM4mlbGfPr2jOnrZRcBDUuc-VCyvljfuZQrTtpMPWtbaKnr3Wi45beelz2K3fIHGl387x7Ug-XLiTHu3DOs-ikw1caM6APtFrzdSqbssXMgZ3U9tX7OGsp1wH63VZLPP52JaE-J5LILRQ-z18X4kwKCdCx1GfVa0HDcoRn4nX0J7av9yXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
لیونل مسی ۲.۶ میلیون یورو برای کمک به ساخت مرکز مراقبت و درمان کودکان مبتلا به سرطان در شهر بارسلونا اهدا کرد.
✅
این مرکز تخصصی سرطان کودکان در بیمارستان سنت خوآن دِ دئو بارسلونا قرار دارد و ظرفیت رسیدگی به حدود ۴۰۰ بیمار در سال را دارد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.11K · <a href="https://t.me/Futball180TV/107051" target="_blank">📅 11:32 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107050">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b26eae7147.mp4?token=qRHopVpmjKRcGewJxQsDN-xPkczp8FmLeD0vgpaKM0wvMNF9Mu2mMgO3lh8qrVa3ETyjp82MJ90jksdwuchGyBdmcRpfWEY9iPHSqPh8sj54M5-3Emj1B9Rw6h_3783aeb3_S2evcblGY-fn5i0xQD97JvkH_cHq2vIPcFRpGle2MGkg3TEWiFGurMkycxc-1NYVtEnQsfmaDPKNqtwPEwhyeEU7Hmb-SvlV7tNMHg1maJq15sTh5s_N16ozbj3xgaWh8YgGfBVWcohpChS5UBt-TL6yY3IrEiwnQ2Xy193Usp7i117zTaI9iI6-yme-KNC7IEDi8uxkXo8SLztACA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b26eae7147.mp4?token=qRHopVpmjKRcGewJxQsDN-xPkczp8FmLeD0vgpaKM0wvMNF9Mu2mMgO3lh8qrVa3ETyjp82MJ90jksdwuchGyBdmcRpfWEY9iPHSqPh8sj54M5-3Emj1B9Rw6h_3783aeb3_S2evcblGY-fn5i0xQD97JvkH_cHq2vIPcFRpGle2MGkg3TEWiFGurMkycxc-1NYVtEnQsfmaDPKNqtwPEwhyeEU7Hmb-SvlV7tNMHg1maJq15sTh5s_N16ozbj3xgaWh8YgGfBVWcohpChS5UBt-TL6yY3IrEiwnQ2Xy193Usp7i117zTaI9iI6-yme-KNC7IEDi8uxkXo8SLztACA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
▶️
در این ویدیو پیرترین موجود زنده دنیا را مشاهده ‌می‌کنید، کوسه گرینلند که بیش از 390 ساله که در اعماق اقیانوس زندگی میکنه؛ این کوسه زمانی متولد شد که آیزاک نیوتون، موتسارت و چارلز داروین هنوز متولد نشده بودن؛ البته که گالیله 70 ساله و شکسپیر چندین سال قبل از دنیا رفته بود.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.12K · <a href="https://t.me/Futball180TV/107050" target="_blank">📅 11:05 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107049">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7b6b29a98b.mp4?token=pzo8_zY93H1vfF6hR7zCf068LMYJyyiSveYKA_cxB2BSNSVG6htfrAwiCq1UZACYfEQ6wr_5YcV5628ILwd2JDKyarNb8AU0_oo86i1uqQqrU0qtXynK_MpIZ1gHwhgALl873pM6uYOlDqaPKui-a0RgesLFQtMaXZ5JSj6IP2I8s-NWVJojZezDmKThrW-YJLXws4ewXrNEIeX9z6JYY9KpdbUZPSeSn91HOVYRNcePugK5bZrP2wtosizkbdMMqcpsh8QyE-EjrsHdtPu-qAAGFVjWwGEYaMS8yKCGm7dbjEJsthi5WIC-i16jbLGwup5NkSpjn2u4ZV5XSHusKQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7b6b29a98b.mp4?token=pzo8_zY93H1vfF6hR7zCf068LMYJyyiSveYKA_cxB2BSNSVG6htfrAwiCq1UZACYfEQ6wr_5YcV5628ILwd2JDKyarNb8AU0_oo86i1uqQqrU0qtXynK_MpIZ1gHwhgALl873pM6uYOlDqaPKui-a0RgesLFQtMaXZ5JSj6IP2I8s-NWVJojZezDmKThrW-YJLXws4ewXrNEIeX9z6JYY9KpdbUZPSeSn91HOVYRNcePugK5bZrP2wtosizkbdMMqcpsh8QyE-EjrsHdtPu-qAAGFVjWwGEYaMS8yKCGm7dbjEJsthi5WIC-i16jbLGwup5NkSpjn2u4ZV5XSHusKQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پاییز با بوی نو کتاب فارسی شروع می‌شه
🍁
✏️
حتی زمان ما، شروع مدرسه ها صفای دیگه ای داشت ...
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.77K · <a href="https://t.me/Futball180TV/107049" target="_blank">📅 10:40 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107048">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b6ef37fb80.mp4?token=gTAcPOsRnvuvX5d1ByEPo2UjkrDyyaLO4iYKdVjuv_nckHLUAKoXoEZVqwf7T7n-SN0MXqo3ySucQvz38N9gvmHyokEY-HuhNCh6iRvrqEvzCHc7924386dgFDLPwOL2RpQlHKeK9L_65xph4_PQcNM2FHctIAMz2JXyjr_OdS9gAh_z9rrgUmgOnx1brOlIGUxVh2obIAJEbb5IC8X2f1T-yHssYqYPri5f59RPNAHDmkLMTShfBEl-nvffLs7mFap3IsTAJYhC7Q4A1B12j2ZsbghLQ7neP4JYGmT0ZoGeWMc7P1FgYtcx9ULDP4gTBGEnabbh6g8P8KkeUbIEdA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b6ef37fb80.mp4?token=gTAcPOsRnvuvX5d1ByEPo2UjkrDyyaLO4iYKdVjuv_nckHLUAKoXoEZVqwf7T7n-SN0MXqo3ySucQvz38N9gvmHyokEY-HuhNCh6iRvrqEvzCHc7924386dgFDLPwOL2RpQlHKeK9L_65xph4_PQcNM2FHctIAMz2JXyjr_OdS9gAh_z9rrgUmgOnx1brOlIGUxVh2obIAJEbb5IC8X2f1T-yHssYqYPri5f59RPNAHDmkLMTShfBEl-nvffLs7mFap3IsTAJYhC7Q4A1B12j2ZsbghLQ7neP4JYGmT0ZoGeWMc7P1FgYtcx9ULDP4gTBGEnabbh6g8P8KkeUbIEdA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آقای ابوالفضل جلالی فکر کرده در عصر قاجاریه داریم زندگی می‌کنیم. چطور اینقدر راحت دروغ میگن
😆
😆
😆
😆
😆
😆
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/Futball180TV/107048" target="_blank">📅 10:15 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107047">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/090ef42156.mp4?token=mAydgFE1JTizWLCkyLKxzhF8IYegg7hkUZqXh7QVraci0TtA2G9Z56IerZiq_mMPeG6LKqLAld3sZFthcCw-4WPvLhZkyWnkJ3SzoJGr-YoL1fruGuQ09D_EPM05lUJH_z-QsmWGymNEYiiiFaXWZR6gsSFLBGGVCKSpO_68VEnqhVXiSuvOp5BwSmddmUgu3gtDGSE3g1jdOkMhleR864EhbcI0XZyL2a0YsjahYCe8Y_ei3uV4UT_7vJ__YHmqq40ZPBPSmA91OoZSeCjKZIioSu3Wt1zrdOMANXM9BShO6ED_3rWMYs1xHRKwQMc5Y5GdZILc0IEhe5KyFKbb5w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/090ef42156.mp4?token=mAydgFE1JTizWLCkyLKxzhF8IYegg7hkUZqXh7QVraci0TtA2G9Z56IerZiq_mMPeG6LKqLAld3sZFthcCw-4WPvLhZkyWnkJ3SzoJGr-YoL1fruGuQ09D_EPM05lUJH_z-QsmWGymNEYiiiFaXWZR6gsSFLBGGVCKSpO_68VEnqhVXiSuvOp5BwSmddmUgu3gtDGSE3g1jdOkMhleR864EhbcI0XZyL2a0YsjahYCe8Y_ei3uV4UT_7vJ__YHmqq40ZPBPSmA91OoZSeCjKZIioSu3Wt1zrdOMANXM9BShO6ED_3rWMYs1xHRKwQMc5Y5GdZILc0IEhe5KyFKbb5w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
🇮🇷
بابک مرادی: مربی داشتیم (کمک فرهاد مجیدی) که آدم بسیار فاسدی بود. همه فوتبالی‌ها میدونن فاسده اما هنوز داره مربیگری می‌کنه
+احتمالا این شخص فراز کمالوند هست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/Futball180TV/107047" target="_blank">📅 09:50 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107046">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d781ba027e.mp4?token=R-zp3Vz_eeiZp99CCHJpI8wOiSPDe33b9ABQQEW-VOrI6lpImNKAR8b_OGt_RA1APmwE3bMWf-IHUUeq0MkclLLT0yKcs2966PJ_sDcyg-SU9QTsJOr7ZERaxKWalG7awR_RdAn7R2A0ebKVWHBQ1PpGFWcYUwXjt1EXL9u-ns1VmNABOFctJROvY4pqpeVz_ZrOxxH0upuMthy1lSoAha3i9LLbjQEN0EVuOGmJxCJkeEZbNymqDaS5jME9ywJ2t0byoPzkmAR9QCR-6rvRtJZax0S_R1hbc3SlEpEnzadDHVoCe49UuTe2V7p73tuVNaDoAqh2xSzz8XWRb4u1qw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d781ba027e.mp4?token=R-zp3Vz_eeiZp99CCHJpI8wOiSPDe33b9ABQQEW-VOrI6lpImNKAR8b_OGt_RA1APmwE3bMWf-IHUUeq0MkclLLT0yKcs2966PJ_sDcyg-SU9QTsJOr7ZERaxKWalG7awR_RdAn7R2A0ebKVWHBQ1PpGFWcYUwXjt1EXL9u-ns1VmNABOFctJROvY4pqpeVz_ZrOxxH0upuMthy1lSoAha3i9LLbjQEN0EVuOGmJxCJkeEZbNymqDaS5jME9ywJ2t0byoPzkmAR9QCR-6rvRtJZax0S_R1hbc3SlEpEnzadDHVoCe49UuTe2V7p73tuVNaDoAqh2xSzz8XWRb4u1qw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✔️
🇮🇷
🇮🇷
تعریف و تمجید حمید مطهری سرمربی فولاد خوزستان از سهراب بختیاری زاده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/Futball180TV/107046" target="_blank">📅 09:25 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107045">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5ed15f390e.mp4?token=TksvfNhaY6BqMBRtkEMl_0SVkOt2V_myxI9DiTNoOArQhyCPbrslsiFXHnofQFx8Qha7FBuAtnMHaH_SJa4lnnZc41BMscvVD2Y0Nv7hgy--Djy4A56dbjARUO5hPdM6W5eEXPDGl5qaKu0cnUMdKxutqNEi70dqL-nRJVgV2sJnus8FW-oXnskX3zkx0d-pmrA1-OWWATvxvDHJftOlvz0SsxjL6ZIDsiqFVtiOTCSytXu2_WU-SkJsMMRgXMMn_Z7RFnsSG6fA8jrEjH1zlEguxoh8s_Vhn5Xh2ntnIFuidOWhdYLfaECNS30ehnKGrqE-Alve5M4WxjPBdFCBnw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5ed15f390e.mp4?token=TksvfNhaY6BqMBRtkEMl_0SVkOt2V_myxI9DiTNoOArQhyCPbrslsiFXHnofQFx8Qha7FBuAtnMHaH_SJa4lnnZc41BMscvVD2Y0Nv7hgy--Djy4A56dbjARUO5hPdM6W5eEXPDGl5qaKu0cnUMdKxutqNEi70dqL-nRJVgV2sJnus8FW-oXnskX3zkx0d-pmrA1-OWWATvxvDHJftOlvz0SsxjL6ZIDsiqFVtiOTCSytXu2_WU-SkJsMMRgXMMn_Z7RFnsSG6fA8jrEjH1zlEguxoh8s_Vhn5Xh2ntnIFuidOWhdYLfaECNS30ehnKGrqE-Alve5M4WxjPBdFCBnw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⚠️
فوش ناموسی بلینگهام به مادر داور بازی با اتلتیکو که شکار رسانه‌ها شد!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/Futball180TV/107045" target="_blank">📅 09:01 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107044">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a69b72fb04.mp4?token=AqyI9jhV_bwvvhaxmlVfrIYt_SUPLgZrt_jO-EcPQ0KyslMzNoPldr0NR4dxVeTpvvLkN06WIh9IngphUnSsbXOlzGL-jYSAoczZpRrZOLeCI68RsYzovsbT5TFWiKsRmaeK0FOLTLBMoe-dM-2ehsPZrLLAHQFjhHTcGxKLFTkqP3XOdQ6eLmnC7Lw43EJpKflFUDtKejLxFprJp6P17YZ-DHx1jBLYxSUYvmVor9lq09z5JZj-tv2UiZq56lArjwZj4xA9KYzZKHLk0IRtDxNx4dzv1xJ-cGWszABCmXY6ilhdEg-tu7wtnpPtysTgPMySP1tyBx97paMQ-X1znQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a69b72fb04.mp4?token=AqyI9jhV_bwvvhaxmlVfrIYt_SUPLgZrt_jO-EcPQ0KyslMzNoPldr0NR4dxVeTpvvLkN06WIh9IngphUnSsbXOlzGL-jYSAoczZpRrZOLeCI68RsYzovsbT5TFWiKsRmaeK0FOLTLBMoe-dM-2ehsPZrLLAHQFjhHTcGxKLFTkqP3XOdQ6eLmnC7Lw43EJpKflFUDtKejLxFprJp6P17YZ-DHx1jBLYxSUYvmVor9lq09z5JZj-tv2UiZq56lArjwZj4xA9KYzZKHLk0IRtDxNx4dzv1xJ-cGWszABCmXY6ilhdEg-tu7wtnpPtysTgPMySP1tyBx97paMQ-X1znQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🙂
شعر خوانی جالب قیاسی:
«مثل رابطه سهراب بختیاری‌زاده و صالح حردانی
مثل حال دروازه‌بان بعد از تک به تک شدن با یاسر آسانی
یا مثل حال اتوبوس تیم ملی بعد از جریان کنعانی»
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/Futball180TV/107044" target="_blank">📅 08:03 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107043">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/Futball180TV/107043" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/Futball180TV/107043" target="_blank">📅 01:16 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107042">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VPTJGHGRLoG3dZszpT0lGqNyHwEVeSbrk5Rn8MGwEj_Jp4EnvXyEcV_8I8TOwSq-JtmAMeRJttWKOfOxgdxMqTRI7y4e6Lo2d0CemLJs4Bq9IS5P0o7S-w0aZocvVOi6mnn5v2lwDMAlM7HGhSLk-Iwptl1hSp6F9MIbDfQgibnP5e9fJikS0zoeBafVm2tBfLn6oyAxeACC7DNPk8T6IChE4FuqLe59R9GzjB27BGrGH5Tulgegj3OnTxXZ3xS09x59b2CR250DpJEMzsP_FVG9tNvvJGG1rD3rhPQWCv7vbI-akwArAPhOLRE28v9G80gMq-NfM_tGn9TCee0uHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
آماده‌ای هیجان واقعی رو تجربه کنی؟
🦖
در
TrexBet
، دنیایی از اسلات‌های جذاب، بازی‌های کازینوی زنده و لحظه‌های هیجان‌انگیز منتظر توئه!
🦖
صدها بازی متنوع
🦖
تجربه‌ای سریع و روان
🦖
هیجان در هر اسپین
🦖
🦖
🦖
🦖
🦖
🦖
🦖
🦖
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/Futball180TV/107042" target="_blank">📅 01:16 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107041">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a32c5c8c60.mp4?token=Bw8AT4cAuC-na5ivkPkPr9Has40BxGRP2Htp3LDQdgX9LQ1r46yUZfJ92bi1eKap66ayY7a8uWkXj1oFlmdIgslC0yHVFY2_eEnSuHFyqGzTVXs5dHQcy9Bdse54CzZHA6OpiVyJBJyt1g7tejV3CbEO8XtHBUGJrtakkwfBImKO4wMHa_6OFx99zzjgZwmq0_apdB0TPcuV3e1RwNGvJ6vQPMzZ8BF8sOARZGgHiE2I7Zsb8TZMkHrAiyzpVDsEv1dXZdGZ3pvvHPIF37F3uZSwPrGL5qVHV45e6t5P_9j_lnS9VSDL5eutx2_AP1j_i1aio4bBNrLsCdoco4JH_Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a32c5c8c60.mp4?token=Bw8AT4cAuC-na5ivkPkPr9Has40BxGRP2Htp3LDQdgX9LQ1r46yUZfJ92bi1eKap66ayY7a8uWkXj1oFlmdIgslC0yHVFY2_eEnSuHFyqGzTVXs5dHQcy9Bdse54CzZHA6OpiVyJBJyt1g7tejV3CbEO8XtHBUGJrtakkwfBImKO4wMHa_6OFx99zzjgZwmq0_apdB0TPcuV3e1RwNGvJ6vQPMzZ8BF8sOARZGgHiE2I7Zsb8TZMkHrAiyzpVDsEv1dXZdGZ3pvvHPIF37F3uZSwPrGL5qVHV45e6t5P_9j_lnS9VSDL5eutx2_AP1j_i1aio4bBNrLsCdoco4JH_Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🐐
🇦🇷
رونمایی‌رسمی لیونل‌مسی از پیراهن ویژه خودش در آخرین بازی ملی با آرژانتین
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/Futball180TV/107041" target="_blank">📅 00:55 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107040">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0b37185041.mp4?token=n0YyOWsI4y-b1DY8WZTOwAlBDIJnDnFx88APASe8JHWag5fy6FzeJcXKxB8cgbdEevBC5A5Ls0c6oENM9gBSYmSWh_StVHYw80ysajTkyyoFjRMm5qaEohAdNNL6XtFr0gLEDVa_Z79gIBE1uRClb2U3LwF1beI2PhwfESg-1xQd38lXYEjbncqvIIqGKLn18NX1ZOqTPGGOKyR7fdNXm9j6XE7xZkCZPO7TS3C0AHzKkezGyhjTNvkmOFMng-QkkoKn8sz1tKjaxZ5zsJ5pdKoInw6lyE4fxNCavFwwnE44WC1fKxm7WbQU7mbqlido3BeLxT9so3X5hMVs9LTLWw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0b37185041.mp4?token=n0YyOWsI4y-b1DY8WZTOwAlBDIJnDnFx88APASe8JHWag5fy6FzeJcXKxB8cgbdEevBC5A5Ls0c6oENM9gBSYmSWh_StVHYw80ysajTkyyoFjRMm5qaEohAdNNL6XtFr0gLEDVa_Z79gIBE1uRClb2U3LwF1beI2PhwfESg-1xQd38lXYEjbncqvIIqGKLn18NX1ZOqTPGGOKyR7fdNXm9j6XE7xZkCZPO7TS3C0AHzKkezGyhjTNvkmOFMng-QkkoKn8sz1tKjaxZ5zsJ5pdKoInw6lyE4fxNCavFwwnE44WC1fKxm7WbQU7mbqlido3BeLxT9so3X5hMVs9LTLWw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
پیام علیرضا بیرانوند به میثاقی روی آنتن زنده: اگر نظام وظیفه اعلام کند من چه زمانی باید به سربازی بروم به جان 2 تا بچه ام فردا می روم سربازی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/Futball180TV/107040" target="_blank">📅 00:45 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107038">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vNusIgU0QQjhz0w-KSLAJurBa2sWsKvUcMFij9ELBoDHq_F9_3evgjKb7oUUl4FFKPwA78j6HRMH1uxFk1gsRjo9b5ewfV3mSG_MF9bkS6_oerouexChtFotf_Bh000QBOUrfdW_F2XWkshOO04JrN10k4CIeOM33yaEwC6mLxVfCqfDV350zW-UZBlYKlM39hWMhpdHef1bWFyRnRnFRmBwyyumrUx9Q-One7XPl8oFsu0Tvul0Rk0zifHYc31JzHzXS6jXlwHowO7OGPAFR8FwGWpa20gihMjl0AnVMcyOOEaigHqVU0BwkwNPlQCrQpe1iC15_UwqgvD0yuzU4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rtPraDYdJY3aH1szWVL_ZmXB3psm6WJ2yYT6QmwRtxN54L_isd6H9BarE5oBMpuhSJGb6EwxOmNXP2mqU2pDa1jIzWqFTWIuIUK7Y8wsqN5-1-GFcUckU5uzUyVnFZiBdVXpIfcXjZ3mRibQq32osDnQO2cs8yphlo-pO-ZxSiUAr4nHnhr75nRWmZaSZyT2sxXMcCeGWWOzzBrEukEVLJm9Lh9xoiKZhiJkT1mBntnexYwrXjWpxTfPYU-g7TTlEegDDdHqFOu-MLiYfpmcj4nZ0AJJen-Un_s9s_sz3mz6JX_nOFgkw50xay_mH8GyaHa14GuKT0g5J9vnpu1DmA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
❌
دلیل عدم دعوت اللهیار صیادمنش انتشار این استوری در ایام اعتراضات سراسری دی‌ماه ۱۴۰۴ است که باعث شده حداقل تا چند سال قید حضور در تیم‌ملی را بزند مگر اینکه به مانند سردار آزمون دست به پاچه‌خواری بزند!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/107038" target="_blank">📅 00:24 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107037">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🚨
⭕️
‼️
اللهیار صیادمنش: در اردوها به بازیکن احترام نمی‌گذاشتند. حرف‌هایی که جوان‌ها نمی‌توانند بزنند را می‌گویم. در این چهار سال ۱۰ بازی دوستانه روی نیمکت بودم، ۲۰ دقیقه هم بازی نکردم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/Futball180TV/107037" target="_blank">📅 00:22 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107036">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🚨
⭕️
🎙
اللهیار صیادمنش: تا این افراد در تیم‌ملی باشند حتی اگر بخواهند هم دیگر برایشان بازی نمی‌کنم. در اردوهایی که زیر دست این آقا(قلعه‌نویی) دعوت شدم هم چیزی به من اضافه نشد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/Futball180TV/107036" target="_blank">📅 00:09 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107035">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🚨
⭕️
‼️
🎙
گلایه تند اللهیار صیادمنش بابت ربط‌دادن عدم دعوت به تیم ملی، به مسائل اخلاقی: می‌دانستم قلعه‌نویی هیچ اعتقادی به من ندارد چون اصلا هیچ مسابقه‌ای را از لژیونرها نمی‌بیند!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/Futball180TV/107035" target="_blank">📅 00:07 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107034">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SsfNAnx9uRnC0MNPmfqiVLkD5cEhks0mBnKENJ6FpOY9pPUP_Z_yFoTC5H86VNJrGNSRS5swbrgrILudS-dkgM5lQs5BRhHTgvKWDzeh-FsZzNMmMsGa59OMrAqmKOtOKD54jJcKIbVyMeR_1Q__Mn5p3MatGRWQwsleYrjThdIf9juGPy-7wbU-o1iOXxbkKcrvtIAo5JaqTDv7TjM091zpLisZlcklhEHD9CQAoWveBCIjs56ALGcAFbFbGj7SVbkeJ45F06YfljOGPIDrHFWsThAF5G4d9aYqhTU438Xo5-VJtlzqiXjfTo3Tqb5d2DE2f0PC4lH_JyxRQMBiSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
🇪🇸
خاویر‌تباس رئیس لالیگا:
🔹
باخت دیروز رئال مقابل اتلتیکو صرفا جنبه فنی داشت. درست است که اخراج یک بازیکن حریف نادیده گرفته شد اما اینها بهانه خوبی برای باختن نیست. امیدواریم رئال‌مادرید واقعیت تیمش را ببیند و دست از جنجال بردارد!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/Futball180TV/107034" target="_blank">📅 00:06 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107033">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8238d2e025.mp4?token=TUut6RswOxmo624kKraGk2sHmOfPMdFy-NqShg9JEeeVFj20KdrKej98qYqMIcyKQgilu84qlxO606ju8NPD6APFwGp4K0xeXbSVjkDiGfVXESJxEEfrQCUHeY4jHEE6mN3Kl64jRGAGNx2U3a2vpDF7bpWlR1yYH7BRyHWVMxUMZ6213Omsq37RTeTHWDwWronN59g5dfZu_9P-YWKJi3C1DZHdRRujw0gjteO_OKYAXMc_hdhpYZGndmTIj6wHo8NuuQD058fmKw9_Jzp-lyr_VwXdSLC-WRa3ZHYH5YVDCD2X-fEmErDe-_YTzKynV0tMBgo2pOurrgdEuNC4EA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8238d2e025.mp4?token=TUut6RswOxmo624kKraGk2sHmOfPMdFy-NqShg9JEeeVFj20KdrKej98qYqMIcyKQgilu84qlxO606ju8NPD6APFwGp4K0xeXbSVjkDiGfVXESJxEEfrQCUHeY4jHEE6mN3Kl64jRGAGNx2U3a2vpDF7bpWlR1yYH7BRyHWVMxUMZ6213Omsq37RTeTHWDwWronN59g5dfZu_9P-YWKJi3C1DZHdRRujw0gjteO_OKYAXMc_hdhpYZGndmTIj6wHo8NuuQD058fmKw9_Jzp-lyr_VwXdSLC-WRa3ZHYH5YVDCD2X-fEmErDe-_YTzKynV0tMBgo2pOurrgdEuNC4EA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
میثاقی: اردوی تیم ملی تمام شود سربازی علیرضا بیرانوند تعین تکلیف می‌شود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/Futball180TV/107033" target="_blank">📅 23:58 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107032">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/37e4355f95.mp4?token=i25aS632vrVFW-zzOVKdinnczfmfh4kHidpCqKB6n80RHeRLYd1iYOBljauMcvU0hBWOJnOVqMyRAtu8tKfAnlOI4gjOyGIbLDE-aHqEk33iNo1SwpXNRJTmZwizW_ykIoo9pEh1vke6cPjiAyPUamWB3w_kkvJp-TDMmGM6hjsvZDAMKaqZUoZrGOGaxQ1uj-zfWqdRxZ4euT4meHKL7QkOPXm4gohoSSFLZz0ZUsnUCEkyt6oSH5mIUSQZha7rn5eBYJPNoPj3HhvyUH1YD4Ykydt-yBQfAONesRV5_rxGLZHUzZ4MJevJegfeUjOfWywkeZGwrZJY7tn4E-a4UQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/37e4355f95.mp4?token=i25aS632vrVFW-zzOVKdinnczfmfh4kHidpCqKB6n80RHeRLYd1iYOBljauMcvU0hBWOJnOVqMyRAtu8tKfAnlOI4gjOyGIbLDE-aHqEk33iNo1SwpXNRJTmZwizW_ykIoo9pEh1vke6cPjiAyPUamWB3w_kkvJp-TDMmGM6hjsvZDAMKaqZUoZrGOGaxQ1uj-zfWqdRxZ4euT4meHKL7QkOPXm4gohoSSFLZz0ZUsnUCEkyt6oSH5mIUSQZha7rn5eBYJPNoPj3HhvyUH1YD4Ykydt-yBQfAONesRV5_rxGLZHUzZ4MJevJegfeUjOfWywkeZGwrZJY7tn4E-a4UQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇷
ابوالفضل جلالی بازیکن پرسپولیس: برای هواداران استقلال احترام قائل هستم. آنها زمانی که در تیمشان بودم به من انرژی دادند. در استقلال بهترین عملکرد را داشتم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/107032" target="_blank">📅 23:50 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107031">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a19a96e43d.mp4?token=B0IZ2SZK9IzT5qhIQ4n37IrtWUd6xaPaXXWxO6UYsjQaWAX2BPVaFiHH1TpxH72jzzrofu39t2PCob1cHwFu42NlWJRdAIPycvsi1_cTor2at763qEHHREf175cQk3P78oQkH9DN0TZHPNrbXkrcwHC4JM4jh7jf5HazKrpUVd4xSST8PfS5wUWvSnZaYxeQRrhdGAY4F1sJga88Nz7cMIoFyUkzjAI8yes1F9bUi63EFIpX9i8DXdUf0cwAudhQnzIjBifNQV9hoJtq-Ivg7_6SGjcfNdPHzRVOzgR6C_atGxQEWxq5mTeBxMNG6S1boZEd0XS-FR7GpzOIDL1-_w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a19a96e43d.mp4?token=B0IZ2SZK9IzT5qhIQ4n37IrtWUd6xaPaXXWxO6UYsjQaWAX2BPVaFiHH1TpxH72jzzrofu39t2PCob1cHwFu42NlWJRdAIPycvsi1_cTor2at763qEHHREf175cQk3P78oQkH9DN0TZHPNrbXkrcwHC4JM4jh7jf5HazKrpUVd4xSST8PfS5wUWvSnZaYxeQRrhdGAY4F1sJga88Nz7cMIoFyUkzjAI8yes1F9bUi63EFIpX9i8DXdUf0cwAudhQnzIjBifNQV9hoJtq-Ivg7_6SGjcfNdPHzRVOzgR6C_atGxQEWxq5mTeBxMNG6S1boZEd0XS-FR7GpzOIDL1-_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🎙
🇮🇷
ابوالفضل جلالی مدافع پرسپولیس: الان طرفدار پرسپولیس هستم، عاشق پرسپولیس هستم و سرباز این تیم هستم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/Futball180TV/107031" target="_blank">📅 23:44 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107030">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f6fa04dad9.mp4?token=r-xYtudgE9d_yqVsARCiZsbv3ci9VRDqXQtBC7ihXkQ9u5N1-7PSwaYiw8J43grWg6ifyPuLXelzvfmOhKz2yqQRh-NbUJBlR_J4FqJoOh_6FIVsLjKMOJ7WyrDoqQrLXbdV2fSNHpERTA3_ovA3GeZk46xflk0pN5CoOwXnRPClV7jowZfajUO9nljwv5aRWS9w2yzjLBQtYuBsGmpvEMyOFiVkq13GRNZetsMNxA6Qu1JSNT5n9XacjAyqYdLQZ-ZYTHtMcEx9u66Wo0MAwJzYdX6HHJ-sF9ulyxVksaA7VpxjnX46z6q5YfbdPY6GWUQg_aE6NtKnC3Abcd9OKw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f6fa04dad9.mp4?token=r-xYtudgE9d_yqVsARCiZsbv3ci9VRDqXQtBC7ihXkQ9u5N1-7PSwaYiw8J43grWg6ifyPuLXelzvfmOhKz2yqQRh-NbUJBlR_J4FqJoOh_6FIVsLjKMOJ7WyrDoqQrLXbdV2fSNHpERTA3_ovA3GeZk46xflk0pN5CoOwXnRPClV7jowZfajUO9nljwv5aRWS9w2yzjLBQtYuBsGmpvEMyOFiVkq13GRNZetsMNxA6Qu1JSNT5n9XacjAyqYdLQZ-ZYTHtMcEx9u66Wo0MAwJzYdX6HHJ-sF9ulyxVksaA7VpxjnX46z6q5YfbdPY6GWUQg_aE6NtKnC3Abcd9OKw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
💙
ابوالفضل جلالی: ساپینتو شاید از قیافه من خوشش نمی آمد که به من بازی نمی داد چون از نظر فنی مورد تایید او بودم/ جالب است رامین رضاییان هم همین مشکل را با ساپینتو داشت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/107030" target="_blank">📅 23:43 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107029">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/11cbab4a72.mp4?token=GHu3zOZtAHDAEjl3ND3QCNHQ0AtcFxYn4ugA26PfkqBmGZw2wn3fSYwttGnwOBCiiFrlhxWfolWMpoFqEIr-tGMBqtkoUXMlsFBJjwZ-thE7VkENvJmHYblNHj9RklolDnptyHxep0_oixUtgTTsoVV_WpqDNzOWP-OVeJOUbq4nDa-kk9rGeMzvDS97M66jXjC4f0RikR502t4n70RtIkZO3r4pQzJJdWJq4Kqzo9REw0dHBD0ZDSlfk94tALt5dvrplqdh0TkqG37qbMYMSnG6GzXBFnkLn99DCvVLhViguiGFWlLsMSqHV7x9Or33Dlo-vhiufsvJgtbOg6Sqow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/11cbab4a72.mp4?token=GHu3zOZtAHDAEjl3ND3QCNHQ0AtcFxYn4ugA26PfkqBmGZw2wn3fSYwttGnwOBCiiFrlhxWfolWMpoFqEIr-tGMBqtkoUXMlsFBJjwZ-thE7VkENvJmHYblNHj9RklolDnptyHxep0_oixUtgTTsoVV_WpqDNzOWP-OVeJOUbq4nDa-kk9rGeMzvDS97M66jXjC4f0RikR502t4n70RtIkZO3r4pQzJJdWJq4Kqzo9REw0dHBD0ZDSlfk94tALt5dvrplqdh0TkqG37qbMYMSnG6GzXBFnkLn99DCvVLhViguiGFWlLsMSqHV7x9Or33Dlo-vhiufsvJgtbOg6Sqow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
سعید الهویی مربی تیم ملی: درخواست کرده ایم که از اول دی ماه اردوی آماده سازی تیم ملی جهت حضور در جام ملتهای آسیا را برگزار کنیم
🔴
میثاقی: با این وضعیت بعید می دانم تیم های لیگ برتری بازیکن به تیم ملی بدهند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/107029" target="_blank">📅 23:26 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107028">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/12081ba765.mp4?token=cSTIQdQBp64SmL12fDgUMuHhQGB3dhUqpTOWj7Glv8U5dFlURNP3Yod9h626NF8dgouW4AIEULLdF6iqrwE_PpMBE9F9FJ9sCsE7EuHJiuvkGYpMDKkW09NjAOuJGtOkXhRVX1KyH7Vm6pZ8YrSxsDNsqeaCPocEJ8XcHd77DP8EV-k5Fh4eXjYuTCAz08MWvaTV1RBCpcuj0fzXASn8s2bcVjYnSbLOH4-B19De_xswWGTQZfQVNYYubqHml8qd12ZUe-uvx4HYUCOq24COmtEiBP_Isl3yKFc4gpdaotyselcBFcAoXtURbicFc647dsxEgn7jL2EelhzDwDTAhQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/12081ba765.mp4?token=cSTIQdQBp64SmL12fDgUMuHhQGB3dhUqpTOWj7Glv8U5dFlURNP3Yod9h626NF8dgouW4AIEULLdF6iqrwE_PpMBE9F9FJ9sCsE7EuHJiuvkGYpMDKkW09NjAOuJGtOkXhRVX1KyH7Vm6pZ8YrSxsDNsqeaCPocEJ8XcHd77DP8EV-k5Fh4eXjYuTCAz08MWvaTV1RBCpcuj0fzXASn8s2bcVjYnSbLOH4-B19De_xswWGTQZfQVNYYubqHml8qd12ZUe-uvx4HYUCOq24COmtEiBP_Isl3yKFc4gpdaotyselcBFcAoXtURbicFc647dsxEgn7jL2EelhzDwDTAhQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
⭕️
سعید الهویی: پرونده حضور احمد نوراللهی در تیم ملی کلا بسته شده است و این بازیکن خواب و خیال تیم‌ملی با حضور قلعه‌نویی را از سر خود بیرون کند
!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/Futball180TV/107028" target="_blank">📅 23:08 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107027">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ogWULGuuCmMSmqyEf1bQOje9z9kD__pZ-97pWR7jTeGeQ2rjP-Hj6a9MfQfvVxPiE8bbBqciaTjbdlsYrOas2NvHBwzsBYxCLUyAtvS2hXAx82RCYe0npSEQCDrWms2h7nf515a5DKbeiM0MGUhJf1kf2Q8mnumMJTUz476ZdS2QQ063d1rlUhxmOfdmA0aVlTMnqaIiTejwUGRJ-aWlgMDVmYxPdLuObGyixVKFeDulJd5eqhobRGEIUemz1wVbZ0G6Urp1GyVUAc6LSvo_z3PtDoI5C369WxOqJF7wlER5EmJlHviGw9CS7WDdfuexR7x9HYPgK_DcOh83PGhi5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
سعید الهویی: الهیار صیادمنش به دلیل یک سری رفتارهایش به تیم ملی فوتبال ایران دعوت نشده است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/Futball180TV/107027" target="_blank">📅 23:05 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107026">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c45095faec.mp4?token=T_M5UO0moSWZA-2k-_2HoKhbgXsUJc1fDB2S8YSXHCvgODP2PZUM4D2Ij-kxhQyBk8NvrEj4OIdz-dZyAL0HAUWjzo4_rvkS2Qn-2SwCmb43QJc9wmS_tfZ-d_BMq94XCsU_d1NjyR4OVEgnC0bdf3OnbEIHlRt2kc3sGfaRLPfwV9sj907DzdM1ZY7J5AvbOojNRAX0S--tcOUb9TEVvAN_95HSXmbgpcAEnJM2Hk9msdkIuOhWqYD4NKUaIJj-vj6YJhNdVl17aJP2GUgAdN8JOowaHUyor40T4Zl1UrglIZPgAfu7cPhB87BBEDPzcHq9KjwQ1bG_Qh8LE3YM6g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c45095faec.mp4?token=T_M5UO0moSWZA-2k-_2HoKhbgXsUJc1fDB2S8YSXHCvgODP2PZUM4D2Ij-kxhQyBk8NvrEj4OIdz-dZyAL0HAUWjzo4_rvkS2Qn-2SwCmb43QJc9wmS_tfZ-d_BMq94XCsU_d1NjyR4OVEgnC0bdf3OnbEIHlRt2kc3sGfaRLPfwV9sj907DzdM1ZY7J5AvbOojNRAX0S--tcOUb9TEVvAN_95HSXmbgpcAEnJM2Hk9msdkIuOhWqYD4NKUaIJj-vj6YJhNdVl17aJP2GUgAdN8JOowaHUyor40T4Zl1UrglIZPgAfu7cPhB87BBEDPzcHq9KjwQ1bG_Qh8LE3YM6g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
سعید الهویی: الهیار صیادمنش به دلیل یک سری رفتارهایش به تیم ملی فوتبال ایران دعوت نشده است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/Futball180TV/107026" target="_blank">📅 22:58 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107025">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">‼️
🙂
🎙
به مالکوم گفتم Bro, Easy Football!
کلماتی که از درگیری شدید علیرضا علیزاده با بازیکن سابق بارسا جلوگیری کرد!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/Futball180TV/107025" target="_blank">📅 22:46 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107024">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🚨
‼️
انتقاد تند عادل فردوسی‌پور: پدرمون در اومد این‌قدر با ازبکستان بازی کردیم!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/Futball180TV/107024" target="_blank">📅 22:11 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107023">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5ee3019bfd.mp4?token=qtog0vlaxWBGycKsw6x7n7DPKORP-X0CiiWllL3EyV9yl2Ryoz9FY_qrEy6UN2jbFatZefJZn5XvvTZeGjHiHDxQTnFZ5TVU5AUa0BPhwPXN-9mBAlorNMF7ecQMRkh12aBum06LXbsuPPGu3PtCjRztSLhDAv8cBTjgzmAogJCDhQCVpAkEQyO2wu1s5BOBCQmrmVsTgLQ0DRgfEF2zkHBhdoN8ygUcIOy2z0nZPsJyB487Nja8-2cLVD6gUwWCUv3N0VTrIfwvN90Vp9R_UAi7mWpdEnjha2Jpd4IQ_2KZWdOMHU45TUpqWim9uITjnFGAl_hcMzZWc5xGHcghOA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5ee3019bfd.mp4?token=qtog0vlaxWBGycKsw6x7n7DPKORP-X0CiiWllL3EyV9yl2Ryoz9FY_qrEy6UN2jbFatZefJZn5XvvTZeGjHiHDxQTnFZ5TVU5AUa0BPhwPXN-9mBAlorNMF7ecQMRkh12aBum06LXbsuPPGu3PtCjRztSLhDAv8cBTjgzmAogJCDhQCVpAkEQyO2wu1s5BOBCQmrmVsTgLQ0DRgfEF2zkHBhdoN8ygUcIOy2z0nZPsJyB487Nja8-2cLVD6gUwWCUv3N0VTrIfwvN90Vp9R_UAi7mWpdEnjha2Jpd4IQ_2KZWdOMHU45TUpqWim9uITjnFGAl_hcMzZWc5xGHcghOA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در ادامه شاهکارهای داورای لالیگا این صحنه رو هم دیروز داور بازی دپورتیوو و بتیس کارت قرمز تشخیص نداد!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/Futball180TV/107023" target="_blank">📅 21:30 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107022">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🚨
‼️
🇮🇷
باشگاه تراکتور با تهیه مستنداتی درحال رایزنی با نظام‌وظیفه برای کسری یا معافیت علیرضا بیرانوند است. تبریزی‌ها مدعی شدند که بیرانوند دچار مشکلات روانی است و به همین دلیل خالکوبی کرده و باید از ادامه خدمت معاف شود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/Futball180TV/107022" target="_blank">📅 20:53 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107021">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y0JcNqL3JyxoBpwlbyMpawDxC80Y0-rl-VVqbbpqGEFkmnF09tRCYdpWgjEuCqDOgqPnceKUrAm-ro3-cVha3jHOBHjmTrYiulh-t7Z1p3C9l80WqusDnzmRW8G8QQAzis-BeD_7Qt1rJpcUuoXsTD9GZMhpJsGDnWHm85AaelN8-4bL_Z3CQiWjQ-TfUOiaemtQ2UHBR65jBsR4LxRbVVfwWubq4O3YpQ2S4WFrQCTxxSk6kAK-UBvXA4tdC00dxWVve5dMdMNkoTgrkSaV8Yfvi7Q35-Vu_taICaTTvE92ACegiurReyz-SN_4VFA_PmT5K1bP1jd5M6U95_WO2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
📊
مقایسه آمار نیمار و رافینیا در بارسلونا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/Futball180TV/107021" target="_blank">📅 20:45 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107020">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/690c7befaf.mp4?token=O45DNC4cTf3HxyTxydjtpXOdsjr8YRzm1juGjlUH8uUqtaD9bXuxgbh1g9V30qjfZrqbHUh8WVZ1om1Ze4s-AvxT4k2NHh1vc9OPJ60eQrnbAmF3ItVLi2iaQgixCdwIeQk5FbNS-nUgkIRVMx8vQwDI_fzNqSu1b4tnsSUc8zGb1kAUf3aGSOqY3bLMFDvMGmoOY7hjJIPyotgxgfOmdWQnClnYYGRlkSnfuuCe46C3yRBAyX4sBujmj158yvWFslKRJccfHiL12WSUm2wudJDkwH0ovb-wZjRylnaJIkYhZMXWqliMQSlxh30igI--errkKbbYaznp2gIlwLc14Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/690c7befaf.mp4?token=O45DNC4cTf3HxyTxydjtpXOdsjr8YRzm1juGjlUH8uUqtaD9bXuxgbh1g9V30qjfZrqbHUh8WVZ1om1Ze4s-AvxT4k2NHh1vc9OPJ60eQrnbAmF3ItVLi2iaQgixCdwIeQk5FbNS-nUgkIRVMx8vQwDI_fzNqSu1b4tnsSUc8zGb1kAUf3aGSOqY3bLMFDvMGmoOY7hjJIPyotgxgfOmdWQnClnYYGRlkSnfuuCe46C3yRBAyX4sBujmj158yvWFslKRJccfHiL12WSUm2wudJDkwH0ovb-wZjRylnaJIkYhZMXWqliMQSlxh30igI--errkKbbYaznp2gIlwLc14Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⚠️
واکنش اتلتیکو مادرید به عکس‌های پرینت شده مورینیو در کنفرانس خبری
: «همین حالا به آزار و اذیت داوران پایان دهید!»
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/Futball180TV/107020" target="_blank">📅 20:09 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107019">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0863a4f870.mp4?token=h6zM61MPML26WvrC2lWEsDwny3X1sh6G8VJOw51MKov18SH9KonbFtXWD3R3uLHTmINXTHmE84_Pag8r_DT12LA4LPwOdnWs4Tlv6ioX-_N2DHfPx3LXKwEwwynqYGKP45kgVqP9xbeCz29e5nk2EHSCP1jFxB5YRcFIv3kCFSmNhq7EorYFPsDVCXYAEflpYqT2iIgzulnQF-XqtcwTn028aQgltMOhiSkjJ6iVGuYNK9HQHjwzQqBHoYfsrXzQkefLMJuq2kxIWETBsyHqlMLhAuGq3RBjs3-ggNGPyNp6BEea4rFxyR87nV2ZPf0gowbWsm2cRJ_HYSZmTE9Gbg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0863a4f870.mp4?token=h6zM61MPML26WvrC2lWEsDwny3X1sh6G8VJOw51MKov18SH9KonbFtXWD3R3uLHTmINXTHmE84_Pag8r_DT12LA4LPwOdnWs4Tlv6ioX-_N2DHfPx3LXKwEwwynqYGKP45kgVqP9xbeCz29e5nk2EHSCP1jFxB5YRcFIv3kCFSmNhq7EorYFPsDVCXYAEflpYqT2iIgzulnQF-XqtcwTn028aQgltMOhiSkjJ6iVGuYNK9HQHjwzQqBHoYfsrXzQkefLMJuq2kxIWETBsyHqlMLhAuGq3RBjs3-ggNGPyNp6BEea4rFxyR87nV2ZPf0gowbWsm2cRJ_HYSZmTE9Gbg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇪🇸
وضعیت رختکن تیم‌فوتبال رئال‌مادرید بعد از شکست دیشب جلو اتلتیکو!
😆
😆
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/Futball180TV/107019" target="_blank">📅 19:45 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107018">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/beecf6e577.mp4?token=S_40_nspWMeE1smUbxPf7oFElhnrsGvK_0VEFn_h6wnrLbkWLBjBRHdR3Itm7g9OQjsn-jP81ZOIDGAL1b4Uhf3PQbCiDSma4qzOkv_m7nslXr0HDUM2YUSorDI0zwzeH_YyTMJh6yFAcFvkASmq1GcO3piKdk-cVTD3KFazCBfiMSQt3LwaUL3bOchyMx3EDg1DqX0BKfEj2O_gBlmRw-RHHgoSgLjMop2wFhEMZ5VYCqo8a6l_x6H2JtfRS853k9Kpq6X0DyCIIRH3xhm-fKSjrErLfLzLY8oCvlDXof0VTVoBbhdlBZPDZc9V0mGAMvmFFki__h27JV-9hUu_RA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/beecf6e577.mp4?token=S_40_nspWMeE1smUbxPf7oFElhnrsGvK_0VEFn_h6wnrLbkWLBjBRHdR3Itm7g9OQjsn-jP81ZOIDGAL1b4Uhf3PQbCiDSma4qzOkv_m7nslXr0HDUM2YUSorDI0zwzeH_YyTMJh6yFAcFvkASmq1GcO3piKdk-cVTD3KFazCBfiMSQt3LwaUL3bOchyMx3EDg1DqX0BKfEj2O_gBlmRw-RHHgoSgLjMop2wFhEMZ5VYCqo8a6l_x6H2JtfRS853k9Kpq6X0DyCIIRH3xhm-fKSjrErLfLzLY8oCvlDXof0VTVoBbhdlBZPDZc9V0mGAMvmFFki__h27JV-9hUu_RA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🙂
دیشب «محسن نامجو» که به تازگی برگشته ایران، شروع کرد وسط خیابون با صدای بلند آواز خوندن که یه هموطن با دو کلمه «ک…، خفه‌شو» دهنشو بست و این شاهکار رو خلق کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/Futball180TV/107018" target="_blank">📅 19:15 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107017">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c34f1b0314.mp4?token=V8gxZRj7Rwy3d52TTYeg6-dDd2G7kU6JKlkptp-A3Y6jGNRRdU8eGOzO-CvNOPPKwBBc1knS1jAC9C9iiAVpmjIGtpYqTU5vd5gD3TmJNkwjpXkQpcoWO9Rbv4S9cXcsWzlRF3B1PINse673EJELBEfvAhNiq-Ehxs2wV0yt4Mqtu_2V5ZlI-K232TI9PrvIGMVIrfaIMn5PesneGUloFdkwASNsRz5_uffYBUpnigZY6YSn16JkQBv2iY0a8dCKs-jvo7XAeaWQlkRt0Gjpk0gk0gY6C2IUDNqAnKA__p0NmCGKDrP1I9HUv8JhANz9iz9znpLqtxmo6-TQfaBcMQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c34f1b0314.mp4?token=V8gxZRj7Rwy3d52TTYeg6-dDd2G7kU6JKlkptp-A3Y6jGNRRdU8eGOzO-CvNOPPKwBBc1knS1jAC9C9iiAVpmjIGtpYqTU5vd5gD3TmJNkwjpXkQpcoWO9Rbv4S9cXcsWzlRF3B1PINse673EJELBEfvAhNiq-Ehxs2wV0yt4Mqtu_2V5ZlI-K232TI9PrvIGMVIrfaIMn5PesneGUloFdkwASNsRz5_uffYBUpnigZY6YSn16JkQBv2iY0a8dCKs-jvo7XAeaWQlkRt0Gjpk0gk0gY6C2IUDNqAnKA__p0NmCGKDrP1I9HUv8JhANz9iz9znpLqtxmo6-TQfaBcMQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
روایت هاشم‌بیک‌زاده از استخدام مربی خصوصی رونالدو برای رساندن مدافع تیم‌ملی به جام‌جهانی ۲۰۱۴ برزیل
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/Futball180TV/107017" target="_blank">📅 18:45 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107016">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/beeb6137f6.mp4?token=YuWjvaYbIwaNlqFQySwG1TG2S5Um1zYfw5W1Y2Z3pssrb0pHizkkQbmpBMy0pRs23i-nB3FMNrR7Q7MuRwSubkqQktYWJH86XzPvSY-gDqBRRCW7wYXy8iXgqJZ_PUNXxB3z4RjsEv03q0Crazb7Z1IJOUbPNjZr52cxrilWq1vMriobJ-uoXb4wi8djxBXDJEM5LwMcPzvC3757eFEKnM_PFxgYWF-N7VppdfJkdP8s9bu0F70rjJ1IoWokHOboFD37pagPgV857Mxm8yW0v3O3a_IrwHMDoWR6Oa_xvrnxwadGpHydM36s6QjTLyAn_MBcrbqaETqx1xfCR--UhQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/beeb6137f6.mp4?token=YuWjvaYbIwaNlqFQySwG1TG2S5Um1zYfw5W1Y2Z3pssrb0pHizkkQbmpBMy0pRs23i-nB3FMNrR7Q7MuRwSubkqQktYWJH86XzPvSY-gDqBRRCW7wYXy8iXgqJZ_PUNXxB3z4RjsEv03q0Crazb7Z1IJOUbPNjZr52cxrilWq1vMriobJ-uoXb4wi8djxBXDJEM5LwMcPzvC3757eFEKnM_PFxgYWF-N7VppdfJkdP8s9bu0F70rjJ1IoWokHOboFD37pagPgV857Mxm8yW0v3O3a_IrwHMDoWR6Oa_xvrnxwadGpHydM36s6QjTLyAn_MBcrbqaETqx1xfCR--UhQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
امیرحسین قیاسی: مهران مدیری برای حضور در برنامه من اصلا هیچ پول نگرفت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/Futball180TV/107016" target="_blank">📅 18:12 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107015">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/Futball180TV/107015" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/107015" target="_blank">📅 18:12 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107014">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UzumOeOGnsqUXvWQsNg3V7rKUCpkj2NipPSfOvMsQnPoPZTJezI-uKUM2PmMcrMtZCJFrhmH7y-zFaF7nu2e4OxijYrU5C_JnMx_xzItuCPuQsv47PF41waVrkIVWK0HazEuNsi9KSQhL6WfD0-tgQhCIfZEpQ9_7jBZZYM2E_s4uBgQPPpoNNeyHtJP617qxRzFlwKVJqRTPnxk89mHCg7KQPYmBwZcM-dUJ7K6RCuNRcyLNfJ-dBZRfI6b0nFyVr4RpggV8JHZG6fBM6Ux52504BBHt_teMXGVGB_PLtsrsmr38_HqKD9iaae1ZYlhhNiABviR46yiY-A92zvhEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
فقط یک بازی از میکس‌ت لوز شده؟
پولت برمی‌گرده!
میکس می‌بندی، هیجان بالا میره، اما یکی از انتخاب‌هات خراب می‌شه؟
با پیشنهاد ویژه
TrexBet
، در صورت رعایت شرایط، می‌تونی
۱۰۰٪ مبلغ شرطت رو پس بگیری
.
همین الان وارد سایت شو و شرایط آسان‌ش رو مطالعه کن!
💰
🦖
🦖
🦖
🦖
🦖
بونوس صدرصدی اولین واریز
🦖
واریز آسان، برداشت سریع
🦖
سرعت بالا، طراحی حرفه ای و تجربه ای متفاوت
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/Futball180TV/107014" target="_blank">📅 18:12 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107013">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/037abe05f9.mp4?token=UKiEIaG9xMgNX5whfylBV6NMleeJx9Gr1lcWBymVTW-j4BYIIGBe0tFzbebxTB-uz3-GBG_igmIczJaRIyi9Nwwtlq65ShXE70FAkl72QHi5FhxbxTLOWKUV68LX883rmN6f4QI3RLpF0AP_A3bwCSAAQNEbsZAtUizZQVab1Cj2zR4erEJRLz0hcQtP3_Racc7o3-2dmh2Ng9xdzXlQKXII-tivOBHFZwD4QGfohVt15yxXR6pAuOYbXiVzc4oRRupPZir35HXJf7xFIwXZH-TOSy4HQ4jLXauN-_-19V5WrAM7inGhuc9qfWbP8RLpp_WWwG75MlBz3VQ5ox37_Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/037abe05f9.mp4?token=UKiEIaG9xMgNX5whfylBV6NMleeJx9Gr1lcWBymVTW-j4BYIIGBe0tFzbebxTB-uz3-GBG_igmIczJaRIyi9Nwwtlq65ShXE70FAkl72QHi5FhxbxTLOWKUV68LX883rmN6f4QI3RLpF0AP_A3bwCSAAQNEbsZAtUizZQVab1Cj2zR4erEJRLz0hcQtP3_Racc7o3-2dmh2Ng9xdzXlQKXII-tivOBHFZwD4QGfohVt15yxXR6pAuOYbXiVzc4oRRupPZir35HXJf7xFIwXZH-TOSy4HQ4jLXauN-_-19V5WrAM7inGhuc9qfWbP8RLpp_WWwG75MlBz3VQ5ox37_Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⁉️
🎙
بهترین گل‌ دوران فرشید اسماعیلی کدام است؟
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/Futball180TV/107013" target="_blank">📅 17:45 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107012">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QfpnvsRhOzefhvmqckA9tJLjg5hj4BCJLXhagx08gaNJZiEICf2E0Q6eHmWhIUA0LjJnkoQj0wjZ_OTfC4edYYsdHC1-NZI_gPwb8C-Di5AtZBc48QCo0LqJMH7Uv4WkodwFqYiGl-5OYNKvQhnR39Bb4GMaVsFK7LYKPfi-bLMXC4B7icL5DW7UbKdjoL-dE9XW4zTnLanBTnHTVuQwZBt1ZyNyYHLIQw-fCXS88cYkbQYnvENvQagPDWvOZcoyCpWAZd5cZf6ZUEH1MtdS304eBL3L7DuN7_g9qp8HGqEjadfIvRNmlMcsN7Bx3-gzOpywt5E31dwsjDwtW3i_Ww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
✔️
🏴󠁧󠁢󠁥󠁮󠁧󠁿
سه سرمربی آخر منچسترسیتی همشون پنج بازی اولشون تو PL رو بردن.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/107012" target="_blank">📅 17:20 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107011">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/226cc241a7.mp4?token=BGr9-4MPSVrdCJcnfMTkqbThyW09MlfsmUkANByrCWdGzTkfpbPWs_Dk-q_wW3ezs03C4DR6Fvt4K2o_TyuIKnztneDIdAGvzUkoPXnelCEe9QL44bX4EuUuykf-BAdJ0zWjVzT5pygisaHx3x1flFnCUqg4yuxryNOXL8rsRrcWkFiXOOu4-4PdEFRqGgwh3teK9YnlikODJq1PsrlxiueKcmA7jkap_kEDH3F8igrDQD4dhwpAESxP0crq3__o8OhUySHy2qj_cPYss2AmOKLhzQqD56670CVX-jAvc5bV-K6RghB1Un0sExVQZBcX6xhD9RpOjkP1y1y3o4_F_g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/226cc241a7.mp4?token=BGr9-4MPSVrdCJcnfMTkqbThyW09MlfsmUkANByrCWdGzTkfpbPWs_Dk-q_wW3ezs03C4DR6Fvt4K2o_TyuIKnztneDIdAGvzUkoPXnelCEe9QL44bX4EuUuykf-BAdJ0zWjVzT5pygisaHx3x1flFnCUqg4yuxryNOXL8rsRrcWkFiXOOu4-4PdEFRqGgwh3teK9YnlikODJq1PsrlxiueKcmA7jkap_kEDH3F8igrDQD4dhwpAESxP0crq3__o8OhUySHy2qj_cPYss2AmOKLhzQqD56670CVX-jAvc5bV-K6RghB1Un0sExVQZBcX6xhD9RpOjkP1y1y3o4_F_g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
🔥
چند شروع جذاب و یک خداحافظی تلخ. این فیفا دی رو از دست ندین.
👀
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/Futball180TV/107011" target="_blank">📅 16:55 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107010">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">🚨
⭕️
⭕️
⭕️
🇺🇸
وزیر خزانه‌داری آمریکا: تمام شرکت‌های هواپیمایی ایرانی از ۲۳ سپتامبر فعالیت خود را در سراسر جهان متوقف خواهند کرد و از پرواز به تمامی مقاصد بین‌المللی منع خواهند شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/Futball180TV/107010" target="_blank">📅 16:20 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107009">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lTLwL6DGFMxgbDkKTvIJ8DW6mQk9yBpqXGqJnSLe8LJEsrctmTolgtGpkrT4GUafVrivj3gcte5ePWebcM7hSJ45MF3v7UPTAjD3J3PRbDcIrStEW_yzS0LEHLmcs7YEjE2i36l2NUadAWBpcOZQkKkBC9cPQzqpu_e9qQzQdbq8oTL8jfJ9qZs0NmIrvkLYzp8YU-vvRZFnyMiBGj1_sEzQfGVjl3tTZXblhylN3c8A5C2IH-kzAMSySMtfo7YujDFq2Kt_8-hkQotVaW_eLYuQVb-UKfztpUwCoaYWBbA01TB-pxScqWQXXfBRC2O-FcSWf8J8VJZsQR3JBVPa2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
📊
آمار درخشان اللهیار صیادمنش در لخ‌پوزنان لهستان که نتیجه آن عدم دعوت به تیم‌ملی بود:
🔴
۱۵ بازی؛ ۷ گل؛ ۲ پاس گل
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/Futball180TV/107009" target="_blank">📅 16:19 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107008">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/12d7084572.mp4?token=OreVuD1S8lehy7FzfsQj1pf2wHr8YHS_V9OGcHhBhYsz0iQ5RVbI1OL8_RWR17DUSFjCZ_qLHkFrcWrwBO0mSPptQVY81V3VTZVN8t9k8FWzOl4QP_X20l9aCaxjMVKTd268qxa0h3NdqoUhHu9qsYDDR5Kj-Jz5xC2KYjsUOxafHEX8Lnp4IFMYUls__z_Uj3tJe3X9VTZD47ZdvcJ4Ju6mNWTKuWeE2dVghwYkIlFAyQ0p18XOoHU0Q6KYI-r5OwmC9fXjRii-xOv56m9IKAVyOoJAfZUHgLPQOzjeGkxyNAvPaejxadzJ29oR3JeUfOvbM7p48Uh5PkN3jb0ung" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/12d7084572.mp4?token=OreVuD1S8lehy7FzfsQj1pf2wHr8YHS_V9OGcHhBhYsz0iQ5RVbI1OL8_RWR17DUSFjCZ_qLHkFrcWrwBO0mSPptQVY81V3VTZVN8t9k8FWzOl4QP_X20l9aCaxjMVKTd268qxa0h3NdqoUhHu9qsYDDR5Kj-Jz5xC2KYjsUOxafHEX8Lnp4IFMYUls__z_Uj3tJe3X9VTZD47ZdvcJ4Ju6mNWTKuWeE2dVghwYkIlFAyQ0p18XOoHU0Q6KYI-r5OwmC9fXjRii-xOv56m9IKAVyOoJAfZUHgLPQOzjeGkxyNAvPaejxadzJ29oR3JeUfOvbM7p48Uh5PkN3jb0ung" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⚠️
افشاگری یاشار سلطانی خبرنگار: روح‌الله رضوی کشمیری، مجری جنجالی شبکه خبر ۱۷ میلیارد نفت از ایران فروخته!!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/Futball180TV/107008" target="_blank">📅 16:05 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107007">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JBo25NXVEm1ybXZF6cYwtJCl8Rp0S0f6LyEHHm2WRnDTKfxZpRA-O0cpWa_3hZtBAuEUP_s5fWFQti5ryIXKCwrKV58_lt6iomf44PGGHnqUzwL8534sJISZyyGG8Srl9fNcB9917EikUfxcO0PEKNjxXdOSX-9qQ1wUY4GD5idhDSkPvcBcZdIttizf5njZGxp5Yrv86-2i8b2qOUXAdq_7EEgMZJLF0uuXPf96wc9Jl3jVhSW6R_0Uw9GaxKmk-NHeHYLCIYbTF-2xCTnJfpaOPueCCkQTtfy3Vkm08j3sJGBuBOhUs0r7psBGJkr3v2UMqQSPYAJKfh5KW_0zXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
⚠️
🙂
دیدار دو اسطوره محبوب و مردمی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/Futball180TV/107007" target="_blank">📅 16:03 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107006">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6e35b261cd.mp4?token=jwZNttxMLv73dRJBUeaKrG_z9eik14TqgW_Xmvr3gPa55DcL-nmUcA7EGSU0481qliM2MMjDiy8YksbQ9HTXsXcbJ4jk25aSfupGJ4mNT2X1mZKBiiQxqQX_VZEMLMxhXbH6XO4_3KBxaEWjm7C66Mt0mosXARpETvFIaAWQ7UNxINPF1xbb27n7Ck6t785u_ntJjtsr1f-u2ejf6bOLRs3EerPQX_MLbuIyHLX1aGg_3OVDlFFi8K7VivTf0oF_Y8hLVBgll_AYs8J-touiHYHXRAiS4nBHA02rfR5JsYtV8nCTpMcUiurDUxudmV7u2EtN57c1WlzVDxbmBR7OZTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6e35b261cd.mp4?token=jwZNttxMLv73dRJBUeaKrG_z9eik14TqgW_Xmvr3gPa55DcL-nmUcA7EGSU0481qliM2MMjDiy8YksbQ9HTXsXcbJ4jk25aSfupGJ4mNT2X1mZKBiiQxqQX_VZEMLMxhXbH6XO4_3KBxaEWjm7C66Mt0mosXARpETvFIaAWQ7UNxINPF1xbb27n7Ck6t785u_ntJjtsr1f-u2ejf6bOLRs3EerPQX_MLbuIyHLX1aGg_3OVDlFFi8K7VivTf0oF_Y8hLVBgll_AYs8J-touiHYHXRAiS4nBHA02rfR5JsYtV8nCTpMcUiurDUxudmV7u2EtN57c1WlzVDxbmBR7OZTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت مانوئل نویر در بازی بایرن جلو یونیون که انگار خودش رو دروازه‌بان نمیدونه
😂
😳
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/107006" target="_blank">📅 15:40 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107005">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4379faf506.mp4?token=hLtdsdY2bQBMrOC5XSejD0mS33_M_zZjjnG_rIM-2FeMa9earK_R70x63qQiJY03sSs-IEb-6f_zYTbf2mOuWGTdBMemu7P6yEhvP-NxhU-_ffLPSmbhXX49qymNcTGPFgxSg96_21zgJ48EnHpoNJ_CtfCMtbu5j7jMjV3dij7X50X7wk8U11R98ww-CWMQqZQaiQw6B7HNPXmzz1naNMDi4APwSZiF-7ynC9QRYk3VbTji1SCWhlCO25W79pLzCGhELBbYEaR7-fMCivCYfx1skr2Fw02iQhVHMZ8NaXX40M_rTsXvV3NrSj0TtmWo5k9sepHmcAx9gCYQu6nZ2w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4379faf506.mp4?token=hLtdsdY2bQBMrOC5XSejD0mS33_M_zZjjnG_rIM-2FeMa9earK_R70x63qQiJY03sSs-IEb-6f_zYTbf2mOuWGTdBMemu7P6yEhvP-NxhU-_ffLPSmbhXX49qymNcTGPFgxSg96_21zgJ48EnHpoNJ_CtfCMtbu5j7jMjV3dij7X50X7wk8U11R98ww-CWMQqZQaiQw6B7HNPXmzz1naNMDi4APwSZiF-7ynC9QRYk3VbTji1SCWhlCO25W79pLzCGhELBbYEaR7-fMCivCYfx1skr2Fw02iQhVHMZ8NaXX40M_rTsXvV3NrSj0TtmWo5k9sepHmcAx9gCYQu6nZ2w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
⚠️
تمسخر امید عالیشاه توسط مجری صداوسیما پس از فحاشی زشت خداداد عزیزی!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/Futball180TV/107005" target="_blank">📅 15:15 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107004">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DxbgHsiuAOqCBjUkWec-nMkxIhSRAxH_R_fn6AHWirJD-fPAPsLeld__Ja4ti3-2eoYiE7j56JcoFShcY3HfWwk__ed0a7yxmxKpFHGwxKDoyuyrcaPE8IFrvL1rjI6h912VBbaVsjUst_p8olsUrvGFzQLMvk2qotdJjGcwEhSbv4E7TAGNeTEzoCQ0R62X3HhTu1Pst0OPVu5fHsYqoSf5EnhJHzbwW39C1wVoReZwVA-JLkkNmdwu0y575FKijvWpDrS3fZKJsFFQDryJQdYSSmLiPbF01wv_8kBie84XEfkFnE_7SoqGZIV9I-jgsrrYsFxZdXlFulwxq0TqIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
📱
پست جدید سردار آزمون بعد از دعوت مجدد به تیم‌ملی: دلم برای شنیدن دوباره سرود کشورم و پوشیدن پیراهن تیم‌ملی تنگ شده بود.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/Futball180TV/107004" target="_blank">📅 14:46 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107003">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sBJ8fP96VsY-JupBNKMAEiDfFZ_B477T6B84z6k1x0vqirSCpAvynT5PMXixPGSjCjBigChpJtN1JmKuWmcBsqpNgF7bymwA57P35U10Q1ce6nvhJ3dwAc-rFmFMmwx6OlMf8wZz2FMyIekNxCx432pcrvACeu2vxWxVVlfnskUArGjYW3aAE4hEyaNGInxx9usaoQQpk2F3za6RULnv58a2acpYNHL0fSUip84SkNxkfOISTygT3M3pyJ9iwWz40TIa1iTqTfULGB_Bxd2zRXNcRjDHHL9mxPd4CV_kSFYoP7jpqJjQlGD0HLZd71Cr4aL5dQanzb2lLGQ_OMM7lg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
قرارداد تیم‌ملی اسپانیا با دلافوئنته تا سال ۲۰۳۲ میلادی تمدید شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/Futball180TV/107003" target="_blank">📅 14:36 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107002">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1b0213635d.mp4?token=Iw0LMjvC3jA4RJN6xd37YEcjW5fEO9qUlODOeOT2uh0-xeRF4PtRlhTnfXTP0s3mBGPRbgvX2mkchcFvksViKJ58BZ3mqhUnXGqyos7PblCm5FQrIo7aSMBkh4RcQVL21CkwN7QT6KNniMIAfYZsvvrOKnnNLqGHC9gWKQlxzT2OrCqcyFoj7Xq7oG73BBFmpD_3w2jcHKoRyN_fAcOhDtyFpMk_WNuP22BaT6w6jAD_AfYFG4b6v_6_ZuqbuHJgbWc6U6T3pg66cYNoqMRgyclAL7rXROG1MXDcqGz5PIwpz8Dg4gfXPjByr24nQrSztDaAYDkHqwbKc5xR3TISKA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1b0213635d.mp4?token=Iw0LMjvC3jA4RJN6xd37YEcjW5fEO9qUlODOeOT2uh0-xeRF4PtRlhTnfXTP0s3mBGPRbgvX2mkchcFvksViKJ58BZ3mqhUnXGqyos7PblCm5FQrIo7aSMBkh4RcQVL21CkwN7QT6KNniMIAfYZsvvrOKnnNLqGHC9gWKQlxzT2OrCqcyFoj7Xq7oG73BBFmpD_3w2jcHKoRyN_fAcOhDtyFpMk_WNuP22BaT6w6jAD_AfYFG4b6v_6_ZuqbuHJgbWc6U6T3pg66cYNoqMRgyclAL7rXROG1MXDcqGz5PIwpz8Dg4gfXPjByr24nQrSztDaAYDkHqwbKc5xR3TISKA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
💥
🇪🇸
بازیکنان رئال‌مادرید و زیدی‌هاشون
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/Futball180TV/107002" target="_blank">📅 14:25 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107001">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XH1oGu_fQOVg9jEyg3G5JCgJA076OxqakPr6Ogm504Au5QisNegppNzG23kNbTinAyf2bRgT98-sr1nbG7FvOs8LZVFISdPKgY_DlZ5yCRsLwI34RTTLpRIa5iIiVaZFp3nlje7ruKKddE19zgFx9EQz8Fbt7XG6ws30tKyO99sk6YCIH70Qg6U-SxvmDA5lUTmNGJBDmQ5hZd3zwYWybREIF7dnHbJnmuYc5yVlNYmbRSnYInlJAUF3pAAmOIuZZUYZ5Zhm6L73z_d-b6_339tzcTrAZFya5cOE5ejmhi4zQhxutRGo653NADICcC86gC_q1kk7gnoSRStWhyOaWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
بیشترین تعداد گل رافینیا، مسی و کریستیانو پس از گذشت ۷ هفته نخست لیگ.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/Futball180TV/107001" target="_blank">📅 14:04 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107000">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u8URwB0K8UEHjV7p6Qqa3X2ZOcm7jMgWNRSzqKbtpfruA4OOmiyOpBU1Jt96Q2IQeHr13nWxAAXMsd54Qk6bAZHMofAiV_bNd29PhWmUnf6SaVT2RmcryhPcG4KgQeJuMqVFdDcrBqU1kGswYaWsbOeIKOjtSfcTCjENUPGOU0cBUJlibNjaJTARsy8im5hRodmhTbGtLEUYbbVA3vVYwuCoHRcleUxZ6iU4fKD22y9xQ_7hOU8cI6rox1QChAfYutxPLzW-KXaJ85raZ7Xi23TOzAo50Bf1RZYlIqp4f9f9eMqDNPWb1e6x-TlPtuiGbFu9NAv7Ng3Mmgo3qw8izw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
📱
پست جدید سردار آزمون بعد از دعوت مجدد به تیم‌ملی: دلم برای شنیدن دوباره سرود کشورم و پوشیدن پیراهن تیم‌ملی تنگ شده بود.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/Futball180TV/107000" target="_blank">📅 13:42 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106999">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bf7b6d21da.mp4?token=qmfwT8TVDt-DvUs2YbI33nJ6iJaBx1PZOIRj1wXlHGzOr0afwjomP1rhb6G171z1S9a--yHv_GBJr8PrgezDbkyg9zkVpr3LVXO4etDC4VvQOTwvwzSULXx183EAfXWLq9PTJrD945_iS-0Zi66QLMYL7pHCircxJdkAUk181ykg05JNgsWv3BAiNqpRkw9DutzZWQnzZlfUdznJo8LBArLb1nycYUHeuurXdYfq5YgrsMylTBc3urbPH2uERJuimjdMGjGlvtwrpJv1JK3tXaL4SAdeu1DQwejYw0GO4oEb6iLG0I6CloV65bEJgK0lLTg6u1WTBUeattFw8hcVVw3Y-Ua_tbMktpmTzpmxvQeAWFYV_9SooEGJt-Avpq1B3O1WESnDf9LiCUdyjLuk4aUjhnrJwIjw73L7gLg983uaPcdVNzBdTA79STwk_XPiFeyUmWnHzz4gSQIz19bkDCyqMNR9k_W0O-ELTJO7w3qIxe9eNwI2_47RKuoHmkpHexpxqDWdPkFVbBM2XK0qa0qu1caprqa7lDBoOPSamycymwPv4zLfzNbwecdyKawve2CIgVwtJo0ej3SRXyhTmEQLjn6bJMKflOQmM7juvcpyUQ7bZDBiUO9It7fqQxj4eI_N1Xe9t2zhsSvXSXX10WwKNsTxJ4fuA25kQsPIah0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bf7b6d21da.mp4?token=qmfwT8TVDt-DvUs2YbI33nJ6iJaBx1PZOIRj1wXlHGzOr0afwjomP1rhb6G171z1S9a--yHv_GBJr8PrgezDbkyg9zkVpr3LVXO4etDC4VvQOTwvwzSULXx183EAfXWLq9PTJrD945_iS-0Zi66QLMYL7pHCircxJdkAUk181ykg05JNgsWv3BAiNqpRkw9DutzZWQnzZlfUdznJo8LBArLb1nycYUHeuurXdYfq5YgrsMylTBc3urbPH2uERJuimjdMGjGlvtwrpJv1JK3tXaL4SAdeu1DQwejYw0GO4oEb6iLG0I6CloV65bEJgK0lLTg6u1WTBUeattFw8hcVVw3Y-Ua_tbMktpmTzpmxvQeAWFYV_9SooEGJt-Avpq1B3O1WESnDf9LiCUdyjLuk4aUjhnrJwIjw73L7gLg983uaPcdVNzBdTA79STwk_XPiFeyUmWnHzz4gSQIz19bkDCyqMNR9k_W0O-ELTJO7w3qIxe9eNwI2_47RKuoHmkpHexpxqDWdPkFVbBM2XK0qa0qu1caprqa7lDBoOPSamycymwPv4zLfzNbwecdyKawve2CIgVwtJo0ej3SRXyhTmEQLjn6bJMKflOQmM7juvcpyUQ7bZDBiUO9It7fqQxj4eI_N1Xe9t2zhsSvXSXX10WwKNsTxJ4fuA25kQsPIah0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
اولین گزارش سعید زلفی در پلتفرم اینترنتی پس از جدایی از صداوسیما
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/Futball180TV/106999" target="_blank">📅 13:35 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106998">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PsyDhZVygtINj9VwaJm6u-bgcyKnPUd8yTDSvXmTVqsrzYCf4zTofkBdr4wG80-xCuU_5Y4Kww2iWKSfg_YHKzwe9RhWyTzhE78JIF0IqLGZ90sDJWEmNL6clkBrY_BbZsvS3czi1VPVmB3NJN8M0-ToiqBX4yEeOG8ClS56nzZOePwgqEymTgWWnzXxSZ3026wYBAVrd3-5X-EfmQyBwORyhtEFPJQcDyxkrgVvwC_S7qDjfRHz5Df4d-CVlQnoBIIFM6fdIy_AZeuXhlaEFr22m7mbMt4XWxQmPYyxpPR3RoHViHyj1jxzxbcMAuFIIfICgTuZu4vCuQVq1Qr1yA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📱
🔴
اینو حتماً تو اینستاگرامتون فعال کنید!
برید:
Settings → Data usage and media quality → Data Saver
با فعال کردنش، اینستاگرام مصرف اینترنت کمتری برای لود عکس و ویدیو داره یه تنظیم کوچیکه، ولی اگه زیاد اینستا می‌رید، تو مصرف حجمتون حسابی اثر می‌ذاره!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/Futball180TV/106998" target="_blank">📅 13:28 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106997">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ix_iSSHN4B_VAMo3sTAma9MkKlKFCCgYKmAjMGYSPYu0AKghu-6hHDnHNL2R3-3_13AsZnrxhBhUV_TpWFBWLJixWGuKIbsBpAzzJvIT004ic33KGb1ljjme48lMvsn53_mLtifQGMR1WEc4gFCcafyA2xDmTfoI7AZ3eWMAgqlzTGYyt5OwOxD7ZVEZccX9Xdrl1CV_birzaNCsFR8iXZoeERu-HWAtp1SR8vQUeqfJkmZlypvxijeiLvnPhf3IEjVGfNKPNq40XXmRYJD5w7r8uiZMFGaWG_i4yqwjV1Dxd5ATeWiBmzk0gOS-jXrpTrKYSfCc4KvxaTRtl0AZ9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🙂
استاد گودرزی
: متاسفانه پارسال نزاشتن پیاده تا آرامگاه کوروش بزرگ برم؛ اما امسال دیگه میرم
هموطن راه در جهان یکیست و آن راه راستیست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/106997" target="_blank">📅 13:04 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106996">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/35dfd98213.mp4?token=v1znBRTnM4i3ERO_CaPWzwDqzS9zHh_Kw1M4nfXe4UC72t-UVhUU8Jocem1I3fT40yg023qpFosoz13xjdl_JTOKJ9RGuk2SPpVlKIyx4MY1wFQZ5iAhbjY2XilUvce5XaH0lt-Y75fHzOQoHqrlo0CucScjdj8PV-m4ElGbGGhfYgzTDnjYSgsj5GaZjj5d9q_v7bQrNnyOGxLnd3_fcSrN6VEgmHUwaJ0Xrc7nCYy6zEpcRTM01gwolzIzsgWvM50NVt0MmQdq4gHaIqqiqSPYN9K395J65h-4VqDbpc2_K3iWf1eUum6gwJpSgtLtltP8e2GYKlfaUZSbJFxw9zzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/35dfd98213.mp4?token=v1znBRTnM4i3ERO_CaPWzwDqzS9zHh_Kw1M4nfXe4UC72t-UVhUU8Jocem1I3fT40yg023qpFosoz13xjdl_JTOKJ9RGuk2SPpVlKIyx4MY1wFQZ5iAhbjY2XilUvce5XaH0lt-Y75fHzOQoHqrlo0CucScjdj8PV-m4ElGbGGhfYgzTDnjYSgsj5GaZjj5d9q_v7bQrNnyOGxLnd3_fcSrN6VEgmHUwaJ0Xrc7nCYy6zEpcRTM01gwolzIzsgWvM50NVt0MmQdq4gHaIqqiqSPYN9K395J65h-4VqDbpc2_K3iWf1eUum6gwJpSgtLtltP8e2GYKlfaUZSbJFxw9zzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🏆
لامین‌یامال از مدعیان اصلی توپ‌طلا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/Futball180TV/106996" target="_blank">📅 12:45 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106995">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kZlVK3BgriTnjcPzFIZbZ8A-BAnpkITMqzRQS_5WviKewRUGfMuWN19DDW5xmlDeKFomHIqVI8JWPuUzr9TjL9Mz43h64cr_cOBCw1GV98TFlpspJm9BGqmAnPEe_BA3SIqNhuhuka_nWygft6EwWOn-BQgxJhpeRjsOXwliDzdW7r3xv8xbsm2Ew4hhvwSEW3iAiHolikiAFjJKxAc-xM3Aq9vxTWlTWVyVYPfe0A-mE2bWx3x62FgEY4NAAsyoY3VWqq3ek9C0utgDBZ1rvCBRXLhUCKMda_pX5COKP4wTfjerZ1I6sCbpmTlW1vsIc0MYGXpN-ppoc7SxZJf0vA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🇮🇷
باشگاه تراکتور با تهیه مستنداتی درحال رایزنی با نظام‌وظیفه برای کسری یا معافیت علیرضا بیرانوند است. تبریزی‌ها مدعی شدند که بیرانوند دچار مشکلات روانی است و به همین دلیل خالکوبی کرده و باید از ادامه خدمت معاف شود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/Futball180TV/106995" target="_blank">📅 12:37 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106994">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IBqd9mvPPucAr_dtJtB-PED2ODIj_ea0e8hEiinlWPkWehlEhMs0Eund5ntd1J3Amu5XvZlXfBi9C7VqUDh6lKTZdnj61Ks3a2fgjGjwJae9ERTG2DGx5j3iZEMqZXMfXvfBrDV8iL_GFjPMbGL2YdIlQ3BhTuof4sWJ5b7nRCWDjhxK9n9BERaOuoAiQVgmiznptefPD-qhxnZ9YyznbHRhex0d0akz4yyN8nPHukevdcXk3kdssoSmHfdyVjXazMENWhTfxXbk6rfXbmlj_wrYZJItsrlLEWpR5X8vdkOx0viC-eZ7CWiHL19qEtdWOyIaEZuk3Yf3B3fFQjIAtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🫡
🔥
بهترین بازیکن فعلی فوتبال اروپا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/Futball180TV/106994" target="_blank">📅 12:20 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106993">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8c1dd2f2cd.mp4?token=Jd_fR59BbqZyKbg4PJMwj6hrJQTArlxb4QBjTGvFgjGSa72m2yCnM1ALRHl3mdR0hkY4_HNyCl9ZHI6EKFnwHri8r-z42IUmT0sDANWz6BmdH6Tkdqu0pe_yLxOTT6jcJ35rhAxtpLAv4lWll1lsj1l9vNFZE76xfHLmqJjqmVdBoi3_C0TiaX2zzkKDqMfcWm-zmwv286kr_JACFJu18yI6Cc87tP7SBR0pOJn4EhYglaZBm30nhJg0AnzqbDME93Rvbft02YyejNZZ5dqAOhc8OjJMDN7HWQat3FyCFb5NB2xPiUaXf36qm4F-5-D74Uh3G9VnqsWEreAsSB9cMg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8c1dd2f2cd.mp4?token=Jd_fR59BbqZyKbg4PJMwj6hrJQTArlxb4QBjTGvFgjGSa72m2yCnM1ALRHl3mdR0hkY4_HNyCl9ZHI6EKFnwHri8r-z42IUmT0sDANWz6BmdH6Tkdqu0pe_yLxOTT6jcJ35rhAxtpLAv4lWll1lsj1l9vNFZE76xfHLmqJjqmVdBoi3_C0TiaX2zzkKDqMfcWm-zmwv286kr_JACFJu18yI6Cc87tP7SBR0pOJn4EhYglaZBm30nhJg0AnzqbDME93Rvbft02YyejNZZ5dqAOhc8OjJMDN7HWQat3FyCFb5NB2xPiUaXf36qm4F-5-D74Uh3G9VnqsWEreAsSB9cMg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هالند ویدیو معروفش که با هوش مصنوعی درست شده بود را بازسازی کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/106993" target="_blank">📅 11:55 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106992">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/huB_ucJomwymcd9ZLuNxRWE62ne8P10uDRN_SASekCC1gDUCsdoZgc9dLpzsJTYvO1hfk7pW70ejVFU0F9l1HP4H7e-gImAbVTO3lnVCwbbVG41Tfl9DBNHtxfXew-0LQpyUyXEhBwHMVAss8DrJ5Tdw9zCE5iRfeskdOzcm9r043Of_3_Si0MW-TM6c091Hz7ONFwIyO46V2XxL7LHiKVeq1NXRxh3SbtzeanGBxUB_g-tKmQvcjoY4nT4AwkiBq6OqB_82dq38VnAWTtsZgkcXaNqnrgop2eeADB9hn1t6g1Y5ppAWtc1n0r3syDM5UhAQ7XxHCxo_ZiUXFnw2xA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
✔️
‼️
اعلام رأی کمیته استیناف:‌ اعتراض تراکتور رد و محرومیت 4 ماهه خداداد عزیزی تأیید شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/106992" target="_blank">📅 11:33 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106991">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b0476c7864.mp4?token=DFPr1N4KK0i1P0E4nT-seDL7jUgBQrcTEEG7FZmDjDX71yp5ePHnuYMbPfGeCSQDiZEv9tRg3cNzKYYPJ9H_xtBS0KvApL0YxeQJW1q3EA0UHBsXjmswvNPjkqY9yKTQcDuZ6n3A29NuMukwatRLwtN7trbdWcA0fPQAb53myPqkuMGwmkYlcJLKPyDaHEvErQT-g-Xsw8WF0BcRBM3UnDWs7jNIns56RPRqdCodwsW62VQGrm2RjQrtGtDOBWWaZfgVPlUEnrVtq-mWu7M8qQ1XiCjrdKSwUYwyAJYFWvhbZbaOcA9RTLB_PFFIKhedA53Qdg-Od1_ezl_lPUyQIQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b0476c7864.mp4?token=DFPr1N4KK0i1P0E4nT-seDL7jUgBQrcTEEG7FZmDjDX71yp5ePHnuYMbPfGeCSQDiZEv9tRg3cNzKYYPJ9H_xtBS0KvApL0YxeQJW1q3EA0UHBsXjmswvNPjkqY9yKTQcDuZ6n3A29NuMukwatRLwtN7trbdWcA0fPQAb53myPqkuMGwmkYlcJLKPyDaHEvErQT-g-Xsw8WF0BcRBM3UnDWs7jNIns56RPRqdCodwsW62VQGrm2RjQrtGtDOBWWaZfgVPlUEnrVtq-mWu7M8qQ1XiCjrdKSwUYwyAJYFWvhbZbaOcA9RTLB_PFFIKhedA53Qdg-Od1_ezl_lPUyQIQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🗓
‼️
🇪🇸
ویدیو سال ۲۰۲۳ بارسلونا وقتی که یامال ۱۵ سالش بود و شماره ۱۰ بارسلونا به آنسو فاتی رسید و براش جشن گرفتن!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/Futball180TV/106991" target="_blank">📅 11:30 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106990">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/Futball180TV/106990" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/Futball180TV/106990" target="_blank">📅 11:30 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106989">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G7J4v9n-MPCCedXwWIrIYtw2TgN_nqoCqbjdhtLsnSwfsd8hUaIPuXvlKyNgjWp9i932spJseKNsmELQm2JxYtcvoZrTkDvPJ6oHHraDw15GOt5MNjSkysqMO6lWJwLMYgGP0t2rSTPrDHFBhN5CInTouU_0YjhmKnJS5O9I5p88jKwfqhfT5ZdW2hhER0y4E7bxlWZo70K1KgYOTWQ_nvzQRunEOp3-iwatNAeeU6KI30GSdZYGk443MSE4R06JwuOSOKfcoos0vS5ytoelITsr9UHMRo-3zhO5I7T-iorzoQwEN-6GqqVBbY74De7Yeo5loThVHv0YxrYCyakEZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
مسابقات
UFC Fight Night
شروع شد!
🦖
یک شب پر از مبارزات هیجان‌انگیز، رقابت‌های نزدیک و لحظه‌هایی که نتیجه می‌تونه در چند ثانیه تغییر کنه.
مبارزات رو زنده دنبال کن، عملکرد فایترها رو بررسی کن و پیش‌بینی خودت رو در
TrexBet
ثبت کن.
🦖
🦖
🦖
🦖
🦖
بونوس اولین واریز تا سقف ۱۰۰ یورو
🦖
بهترین ضرایب بین تمام سایت‌ها
🦖
واریز آسان و امن از طریق کارت به کارت
🦖
هیجان بازی، وقتی بیشتره که انتخابت حساب‌شده باشه!
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/Futball180TV/106989" target="_blank">📅 11:30 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106988">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/60ee4811fc.mp4?token=NNQuf6rDgOd6-E31NLXJP-zrhPBLdReZe_j7CtldQAOhAqUoB2bi3mownLCOX_K9zuXAOPz1fJspfUqrnUuj1i93mTkwC1FQJTT_JwpnO9aPM3CY1qbb6NG29H16Ksiv2kJWX9sLIj_Ph-dDp03Ylw5ApJ8WDlKjp_IncFvYFUu4L7uXgycbU71m5elhUSypIiDnW4K_gJNUkpSjlKf1bVGbPWjmvwYaoD0gszMotOwTDzxuVW_38yHzj-I_qZZ7iakK5Xqpmry3GEoNVEQ4EICE7u3o_YfS-jYw94x2DT_bgb8pL6fR_xec8oNzIReD_7U0guj5VRDOqeJhPYuGdQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/60ee4811fc.mp4?token=NNQuf6rDgOd6-E31NLXJP-zrhPBLdReZe_j7CtldQAOhAqUoB2bi3mownLCOX_K9zuXAOPz1fJspfUqrnUuj1i93mTkwC1FQJTT_JwpnO9aPM3CY1qbb6NG29H16Ksiv2kJWX9sLIj_Ph-dDp03Ylw5ApJ8WDlKjp_IncFvYFUu4L7uXgycbU71m5elhUSypIiDnW4K_gJNUkpSjlKf1bVGbPWjmvwYaoD0gszMotOwTDzxuVW_38yHzj-I_qZZ7iakK5Xqpmry3GEoNVEQ4EICE7u3o_YfS-jYw94x2DT_bgb8pL6fR_xec8oNzIReD_7U0guj5VRDOqeJhPYuGdQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">با صدای کم‌گوش بدید
😆
😆
😆
😆
😆
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/Futball180TV/106988" target="_blank">📅 11:05 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106987">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9186ccb478.mp4?token=Am2k5iDOODbzHIup4NC2ALig0t1IQa8uCu0Ub8Nij-ZubYRi8iyRc8PE1V-3TtxO3vE8li6sSkNhFxqlXXBgGCYDiLdCa4q-Nd-Y7SB3Xkhm6b1rtNeYLlorvmHARzunSWMqJRVI2jhsUwbfHliCcidBqg94OxjN-z_nI9DXbjVINoQRhXCLtk4rU7CAEjAGcJxKFloB7ASzY61kPcmmmKCAbkZi5PUN-ZvdUFKRbbwCzbC6aJM4iMn6FQ6ZM-_B_958B6m0d43rLS3DUeTUvTiwa4LU1Mmtb9hQppadsiJwUG1RXA3f9O2qj8XBHK2t8f2rXfbhRnzPbygUn_N_sA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9186ccb478.mp4?token=Am2k5iDOODbzHIup4NC2ALig0t1IQa8uCu0Ub8Nij-ZubYRi8iyRc8PE1V-3TtxO3vE8li6sSkNhFxqlXXBgGCYDiLdCa4q-Nd-Y7SB3Xkhm6b1rtNeYLlorvmHARzunSWMqJRVI2jhsUwbfHliCcidBqg94OxjN-z_nI9DXbjVINoQRhXCLtk4rU7CAEjAGcJxKFloB7ASzY61kPcmmmKCAbkZi5PUN-ZvdUFKRbbwCzbC6aJM4iMn6FQ6ZM-_B_958B6m0d43rLS3DUeTUvTiwa4LU1Mmtb9hQppadsiJwUG1RXA3f9O2qj8XBHK2t8f2rXfbhRnzPbygUn_N_sA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📊
🔥
تعداد‌گل‌های این فصل رافینیا در مقایسه با چند تیم مطرح اروپا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/Futball180TV/106987" target="_blank">📅 10:40 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106986">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gWrIv-CSyx-NMUOxBa0s4O0IKTv8k_EclxNcQcC6jaiNIYDRXLhl1vITbaB1o4ddACh_Yo2M0syOh2wLfwBoNzMsh8vA6VMOGCxGe9tSciRDJSQDypO6y2hCMVy3umLkJ6DH_raoyaOytu9Tdgruyp7EiLhLkV2MCFlUxSomeAaBjULZqXcZ93RGmrA0R1d1VlYG92to4vWnsp-At6DzWqBxq9zfR8GwF_XFqUZVbT8ZVxGD4o3wF_ppkwibw1lU4nw0NmB2o5n8fQjDz27WpULMXFmwl2JZVRKZGThk9wegDnGD1BwtqhXv-BzShE_MCnoz_F-XUxcmMy7UoracSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
⚠️
احمد ایراندوست از بازگشت شادمهر عقیلی به ایران در آبان امسال خبر داد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/Futball180TV/106986" target="_blank">📅 10:25 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106985">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4a7263425c.mp4?token=o6ElsggpGgq3afjlUKCQ_BJa69o2u9-uSkeTs5HX7RwYSnFKXxMd17T_ekJTlhyLSQblRJ_nKJE34PGtqdPfTwWLoFT4VbdRlK4PNmqBT-zO8-KB-E9cvvfd_JNt2CyIKVtbkT7YO-0zrcPQnizxemeUR_8XBHPLX04YUvMmYGl3yCnR7kEISHwsQzOj397KBgGwdTDQQA-rVui9behjXaGZQ7ny5oIOA_fSFEbMYoTHJZEL2Q9jdMq33ru9MUteqb0pQd0chz-677zyJN5BQTI2G5OVH5oleciiPe2GdZNWh8A9schXUgRvtb9zeKCpneRnm49P3lqAj8UqWwzqIw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4a7263425c.mp4?token=o6ElsggpGgq3afjlUKCQ_BJa69o2u9-uSkeTs5HX7RwYSnFKXxMd17T_ekJTlhyLSQblRJ_nKJE34PGtqdPfTwWLoFT4VbdRlK4PNmqBT-zO8-KB-E9cvvfd_JNt2CyIKVtbkT7YO-0zrcPQnizxemeUR_8XBHPLX04YUvMmYGl3yCnR7kEISHwsQzOj397KBgGwdTDQQA-rVui9behjXaGZQ7ny5oIOA_fSFEbMYoTHJZEL2Q9jdMq33ru9MUteqb0pQd0chz-677zyJN5BQTI2G5OVH5oleciiPe2GdZNWh8A9schXUgRvtb9zeKCpneRnm49P3lqAj8UqWwzqIw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✔️
🟣
گل‌تماشایی لیونل‌مسی از روی ضربه کاشته در بازی بامداد امروز اینترمیامی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/Futball180TV/106985" target="_blank">📅 10:12 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106984">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1a81f86f53.mp4?token=H9tiBB7km1dQn9heqInarm6f0tERt5rhALk_ATE-ArZbbHug5gtVLNR6QWJ72892o5BCOouj3pinKv7g-8APz2zERE5CcXbRDzWrxI03U2fq100pvldBg0vkx0c1IfWzGxUgR8L0vhu-GGKtlX6JQuykdmNgK6F7p1EzhNUxCkrCNjxuvro9p5UMVme114avoU-uemjwYA-lfzXSEx9Wtie8cY6P7PLu0uTdKiFWoSXNsNef3n4dRzJ3teNrwLwweVmGFqzrZ859oAIL9ehxLAxe83dqM3rnnG5NjnL-7f_OfMuWMNi8OVyv6ogxZqfnhmykqvfXPUu35PecLD-czQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1a81f86f53.mp4?token=H9tiBB7km1dQn9heqInarm6f0tERt5rhALk_ATE-ArZbbHug5gtVLNR6QWJ72892o5BCOouj3pinKv7g-8APz2zERE5CcXbRDzWrxI03U2fq100pvldBg0vkx0c1IfWzGxUgR8L0vhu-GGKtlX6JQuykdmNgK6F7p1EzhNUxCkrCNjxuvro9p5UMVme114avoU-uemjwYA-lfzXSEx9Wtie8cY6P7PLu0uTdKiFWoSXNsNef3n4dRzJ3teNrwLwweVmGFqzrZ859oAIL9ehxLAxe83dqM3rnnG5NjnL-7f_OfMuWMNi8OVyv6ogxZqfnhmykqvfXPUu35PecLD-czQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇪🇸
🇪🇸
لوئیس گارسیا پلازا، سرمربی سویا، پس از شکست ۳–۱ مقابل بارسلونا:⁣
اونا خیلی، خیلی، خیلی، خیلی خوبن. همین که تونستیم باهاشون رقابت کنیم، کار بزرگی کردیم؛ چون بقیه تیما رو جارو کرده بودن.⁣
توی فوتبال یه‌سری اتفاقات هست که نمی‌تونم درکشون کنم؛ اینکه رافینیا جزو نامزدهای توپ طلا نیست هم یکی از همون اتفاقاته.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/Futball180TV/106984" target="_blank">📅 09:50 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106983">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5061d27e31.mp4?token=q8VKF7ST2LttTjOc_vjHnpR625tyYACu8Fvc7KajdQxpcctjVkAPfG93WtFzB7XiK880eoTb2UsvUnYmUYD2KlFg7A29ITFOQNlfz8gCGVK7ngRov-Ze2qmo0PV1elMJQPjjdNfwVMewDGYPGh3jfn7lMr3muudHn8Du7ebe42hZqAyF8aP6NGygEB4LROjd7jEaFbpXQrA1oWUNSnryA9sQc1hdT0569ndtB7CATc1txCFtU0Aisf_B-KiIPPy-AKT1UXutrSXcB0eQyYItB9C1ipRL7SnEN1O_TVGRGMAn9PAyvgdC3aOo_xrIpxBYqcdrt_D-dv-xm1-2xoW5623NyljTasXbD1nWTcbD_6nc-ATjczu_Bm3kNDn77OrGizyPczjb1Ar8CAwhsZoiOYyJOnuS4QIxpuzxjfpvEbSmvW1GYiLVF_Yrfmq4T9mBPOc8j1WItpJ5zugBnfADEjQ2KRSPIXUwlijngh7VxTbPZZD9N3oYmofgJzt5Tfyol32fGt3Sc1ANoPWWf466tJv605gMN9rgWqnsnP474gSahdwD_orPkZpz0eEFQf85XQXwtfFIr9pWZryzB155EXiybEFAfLjEYsKoqTvX1ZFVDq7DV7uNJnrYrj50I7a7ZZ7t9OjOz_UregwhI2cpLbN_1zf8WyfrFH9xmklqWMQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5061d27e31.mp4?token=q8VKF7ST2LttTjOc_vjHnpR625tyYACu8Fvc7KajdQxpcctjVkAPfG93WtFzB7XiK880eoTb2UsvUnYmUYD2KlFg7A29ITFOQNlfz8gCGVK7ngRov-Ze2qmo0PV1elMJQPjjdNfwVMewDGYPGh3jfn7lMr3muudHn8Du7ebe42hZqAyF8aP6NGygEB4LROjd7jEaFbpXQrA1oWUNSnryA9sQc1hdT0569ndtB7CATc1txCFtU0Aisf_B-KiIPPy-AKT1UXutrSXcB0eQyYItB9C1ipRL7SnEN1O_TVGRGMAn9PAyvgdC3aOo_xrIpxBYqcdrt_D-dv-xm1-2xoW5623NyljTasXbD1nWTcbD_6nc-ATjczu_Bm3kNDn77OrGizyPczjb1Ar8CAwhsZoiOYyJOnuS4QIxpuzxjfpvEbSmvW1GYiLVF_Yrfmq4T9mBPOc8j1WItpJ5zugBnfADEjQ2KRSPIXUwlijngh7VxTbPZZD9N3oYmofgJzt5Tfyol32fGt3Sc1ANoPWWf466tJv605gMN9rgWqnsnP474gSahdwD_orPkZpz0eEFQf85XQXwtfFIr9pWZryzB155EXiybEFAfLjEYsKoqTvX1ZFVDq7DV7uNJnrYrj50I7a7ZZ7t9OjOz_UregwhI2cpLbN_1zf8WyfrFH9xmklqWMQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💥
✔️
سوپرگل فوق‌العاده در لیگ‌کشور مکزیک!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/106983" target="_blank">📅 09:25 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106982">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d9b6fbcb00.mp4?token=dLA0SYHbkvg7ibQhpPSBjb5Bq3dsZ9zdXfGdeBOvWVhlN6BvY_T0Dtjc43CNLWB_Cle3EZpNMxm1GMGulKt3hCbyGXymGLz8pQ86zvR9pjDLVtqcnwwEomQHZO9Kv4fXz1U3Yxi5_ks8UmjAMh7usbL5CDQqrdlU7OAvcvN_X3JgPwRVuyL6y_LCAbzCgw4xmMhok_anUakCEPs3t2y5IxxAt7iNRDM-dtctVBBOc3uD9YiuuT95lwKll0a6_QjpBR4ZqyhOd6Ya84mcSu7aFI710Vo1xMSje9WNOVI4uGEh4wlrezvIFqiP0hMlRIfn59EfM4-x0bpN2KtAcvTYqw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d9b6fbcb00.mp4?token=dLA0SYHbkvg7ibQhpPSBjb5Bq3dsZ9zdXfGdeBOvWVhlN6BvY_T0Dtjc43CNLWB_Cle3EZpNMxm1GMGulKt3hCbyGXymGLz8pQ86zvR9pjDLVtqcnwwEomQHZO9Kv4fXz1U3Yxi5_ks8UmjAMh7usbL5CDQqrdlU7OAvcvN_X3JgPwRVuyL6y_LCAbzCgw4xmMhok_anUakCEPs3t2y5IxxAt7iNRDM-dtctVBBOc3uD9YiuuT95lwKll0a6_QjpBR4ZqyhOd6Ya84mcSu7aFI710Vo1xMSje9WNOVI4uGEh4wlrezvIFqiP0hMlRIfn59EfM4-x0bpN2KtAcvTYqw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
فاصله بارسا و رئال به شش امتیاز رسید.
👀
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/Futball180TV/106982" target="_blank">📅 08:00 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106979">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b27BPoitUdFHxt8hMeMMzPHDeAsASe0TRm6yeCzN-UKMZ8p2fmmKa3ASgIiclswoe96bGZ9t9zunM43JyHvtFe9YANz8zH_f3K0pA1zgJBWrIVE2OigbJdBEbNMYtQNwHGaAq0wzZhmbzxUC1dKKbytLX1NiL96yF-HBN-VW9355seB-7YpXR18js13nWo0aqbPuyGMkRXg_aZ_Hmpfvl7NJdm8c7FvVd3FiA7QXCHWvbYEvq_YiQ9qOx4rnoa0mms-BdUPA2aUGeZFGTheeh90GwIz2fR6mNinT8PVwXzfsVudbDOfQ6NS9MGHZYNkVWrzC6s6RIIbcS0IuwktJOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🇪🇸
سیمئونه درباره بارسلونا:
🔻
انگار اونا دارن یه ورزش دیگه‌ای رو بازی می‌کنن، نه همونی که ما بازی می‌کنیم. مهاجم شماره ۹ نداشتن، ولی یهو رافینیا از راه رسید و ۱۲ گل زد. یامال هم اگه اشتباه نکنم ۷ گل زده.
🔻
توی زمین خودت بهت فشار میارن، زمان رو ازت می‌گیرن و از ریسک کردن و گل خوردن هم نمی‌ترسن. حتی انگار گل خوردن باعث میشه بهتر بازی کنن. اونا الان بهترین تیم هستن.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/Futball180TV/106979" target="_blank">📅 00:45 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106978">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XUMpON4uhGfK5yOTdH3Qq9YIh5iGAPDZXsRIuxccRr8IwTx63VFUlzbKOPuKFfpi4vmRQP1QJ7Bhu2oHe3s3Ud4_MfFg_wF2qqolr5T3x7D13HpB4-pjdhx7a36YhgBHhIq1yGTyU392ADmn9e_WK97ZCgvXtU4RWJQkWUqQ7EWrUYhzbxObx8N2lAK7NHSxzNXARcsHJAjDfSZNX52T6oGbbxkf4fZPTJMzbrhn5a4kbn5SMc1O5PV8dxxMfRMxJtJZAOmifcdyWH0zUhhk0t9zKbWZEeLWjWzkUUHADS469xOL3pQk7Rpu_zTtYk_fxFmLetQQWBXjKX0WOKh2MQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
⭕️
شبیری‌زنجانی از مراجع تقلید شیعیان دقایقی پیش در بستر بیماری درگذشت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/Futball180TV/106978" target="_blank">📅 00:36 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106977">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J2atZonxP-uWPbnnFB_dHQtRpFzjqfy3biABiIjbrYmkG8g9DVTVasOVizWDKrX09AhHaueEFOChzr4rP0cHF_GkizDOwJWGNPdEHm6oOTw_UXtIFapWNwoUAarN_x3Q6K5dbI4b-ngyCYf8gQ_WrwgyGKx_-iXRu3tiz9vRGAlCD9FA4PZVTEhDa21xsEu4gbYlnbMuuMwZUmXKKYmlAwtO9BIjdSDhpyAHpMpwX3NbP8lu1qABcrzwI4aYjijQS0m0lWxHY4DBXA-1pjEZeduNgtgmQQW1keNSswL25-6cSoCsWdvWpMSclFPq52k6OCL0AJYDDkoOHCyI5nitCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🇪🇸
خوزه مورینیو: به کمیته داوران تبریک می‌گویم. آن‌ها باید از این نتیجه بسیار راضی باشند. همه‌چیز بسیار عجیب بود. بازی باید ۱۱ در برابر ۹ دنبال می‌شد؛ چرا که اتلتیکو از دریافت دو کارت قرمزِ مسلم قسر در رفت.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/Futball180TV/106977" target="_blank">📅 00:14 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106976">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i-Mrw5AA4pZhE1Xc5o_MdnXNxswM-L-5rF7GxAlvL-8iDmku_Z1dGsnDkTuL9EosoRc-DGPFcPsiyQ5l8AyWbrafvXoFjnq3fQ71kvFkq-qjkxwaAzuhQJgUooWgPhKgnYlLsk8Q4KK8mXNbzbumBoLIYGatu00iZzzXa057jPPCE5yKi2nt0sDcn7yatSLyBBJNSFIZ5jtr_RCaLB0tV2HpCFeH90CkPRO9ulVWwGBru1d2aNda-UJqu-NR9vHb36HL-CFTs021ExRYXCEuwCGxwwb3yeshg7hJW-Fcj8c5nAccGftF9pkk_w_JZ5Tyqve9Fyr-8GYjjwenN5BbCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
بارسلونا در فصل ۲۰۲۶/۲۷ تا اینجا :
⚽️
۸ بازی: ۸ برد، ۰ مساوی، ۰ باخت
⚽️
۳۶ گل زده
🥅
۸ گل خورده
🇧🇷
رافینیا: ۱۷ (
⚽️
۱۴ گل،
🅰️
۳ پاس گل)
🇪🇸
لامین: ۱۴ (
⚽️
۸ گل،
🅰️
۶ پاس گل)
🇪🇸
فرمین: ۶ (
⚽️
۴ گل،
🅰️
۲ پاس گل)
🇩🇪
آدیمی: ۵ (
⚽️
۳ گل،
🅰️
۲ پاس گل)
🏴󠁧󠁢󠁥󠁮󠁧󠁿
گوردون: ۴ (
⚽️
۰ گل،
🅰️
۴ پاس گل)
🇪🇸
پدری: ۳ (
⚽️
۱ گل،
🅰️
۲ پاس گل)
🇪🇸
اسپارت: ۳ (
⚽️
۱ گل،
🅰️
۲ پاس گل)
🇪🇸
اولمو: ۳ (
⚽️
۰ گل،
🅰️
۳ پاس گل)
🇧🇷
ژسوس: ۲ (
⚽️
۲ گل،
🅰️
۰ پاس گل)
🇵🇹
کانسلو: ۲ (
⚽️
۱ گل،
🅰️
۱ پاس گل)
🇪🇸
برنال: ۲ (
⚽️
۰ گل،
🅰️
۲ پاس گل)
🇩🇰
کریستنسن: ۱ (
⚽️
۰ گل،
🅰️
۱ پاس گل)
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/Futball180TV/106976" target="_blank">📅 00:10 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106975">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/773fad15d7.mp4?token=iwlQyoZklEJQXb9mL9fpETzBprR4LzolgiC0eBoBzC1niNvCY1fy-kee0l8ttpOH7qWl55P-gD2lccjIWBaKigYpEBzrjAcrMiNBkXCTkS-Ieb4YmkwwKwJUyqgFh1Gn_pqmiWAyiOxzuFzBSSEVCH2TMXAoxbZCKA-pV4kofgnaCfj2I1I1es0UFY9TAtmmpXQajcG5TH_hDDrwaonyMXYCz8V7FcYLZmxgmxbUTPIMDSxzitFSGjdWz-as0iI1eEjPGpZSiZLC2IJCTuqy8a8baDGscRAt23VbT72zs8ZlpouUyO1Nu3mZ9cyD9AirsFzXjjhrWLw8d0G7-IdTfg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/773fad15d7.mp4?token=iwlQyoZklEJQXb9mL9fpETzBprR4LzolgiC0eBoBzC1niNvCY1fy-kee0l8ttpOH7qWl55P-gD2lccjIWBaKigYpEBzrjAcrMiNBkXCTkS-Ieb4YmkwwKwJUyqgFh1Gn_pqmiWAyiOxzuFzBSSEVCH2TMXAoxbZCKA-pV4kofgnaCfj2I1I1es0UFY9TAtmmpXQajcG5TH_hDDrwaonyMXYCz8V7FcYLZmxgmxbUTPIMDSxzitFSGjdWz-as0iI1eEjPGpZSiZLC2IJCTuqy8a8baDGscRAt23VbT72zs8ZlpouUyO1Nu3mZ9cyD9AirsFzXjjhrWLw8d0G7-IdTfg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گل‌دوم پاری‌سن‌ژرمن به مارسی توسط مارکینیوش
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/Futball180TV/106975" target="_blank">📅 23:58 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106974">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/f22d5f48d9.mp4?token=CGdHGQisrL-CSvTT-xxXhYTaO4Csa3knPpKX-bC_xawO32vqT2jL9L5WAfl1Lo7iTE_51N1AHLfS6XNAc9ySO6Wra8lsvkzPrzTKQjWMPHYeP9f8hyEroXynOQR9j2o2JSRVP7Tm-rOHMVo1oFPrDud_SlWrL68a85k4a_xJE90IU3aMGQLq80w_ovQF5EEhW-cSd39ugYgg0-SUVVwNIsxaeaRKepWu5lQuIypVajhsZ09b3OSNwq4YfILrejuJi7OA5h7uxbDVZ8A5E0KNbSC4b1Pe_BWFB8ULejUrBqUKMx1LNO7bEwTwKEXv7QxM9FVY9mVjeLxNCgc7IbTjug" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/f22d5f48d9.mp4?token=CGdHGQisrL-CSvTT-xxXhYTaO4Csa3knPpKX-bC_xawO32vqT2jL9L5WAfl1Lo7iTE_51N1AHLfS6XNAc9ySO6Wra8lsvkzPrzTKQjWMPHYeP9f8hyEroXynOQR9j2o2JSRVP7Tm-rOHMVo1oFPrDud_SlWrL68a85k4a_xJE90IU3aMGQLq80w_ovQF5EEhW-cSd39ugYgg0-SUVVwNIsxaeaRKepWu5lQuIypVajhsZ09b3OSNwq4YfILrejuJi7OA5h7uxbDVZ8A5E0KNbSC4b1Pe_BWFB8ULejUrBqUKMx1LNO7bEwTwKEXv7QxM9FVY9mVjeLxNCgc7IbTjug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گل‌تساوی مارسی به پاری‌سن‌ژرمن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/Futball180TV/106974" target="_blank">📅 23:53 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106973">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/ed04c10225.mp4?token=dfHpig_NDxN3HQ2TLzcIIWgB4kum2ocQicB_pst92m3qxNWmjTE59wusTmOeTB6Hsuw3xNrAsyESvAL0exQJcO8ZNyEVAhXodv6H5pL4viWFrwjm1nvHq9vd2BUgwxhE2xOFHk0R2X39PGPqaGSK9WInIHw19w8BqSUnt3_Ga2cW7ds2tk1ayAuOBtbl4z9mMYIjv0ufy3b3W45Fy5sE9L-QjpKnzMtjxzxN5MStuoyWYzPF9NERfb2msWAba1R-_14-42Ik2f4GooVbdUbdIjMpZifY02W37TxVzb2vX0zs62757hTD_YpD6k7-R-fa1HM8P6UB6m37EbWvFjCHhFH6HuunA6KdvweM6FWDv1QGywkv5ssqB0WP_8uOKwTiCh-Bm8Q9BqRJsFcMWVbWqjswhtMb76TSK1gW-B0DX2T4e93ddWRLRjkYKy8A_61zh6pli397qYtvbP_2fZW2mPbJSLYLSZetfvPgwRClJRKzFkY96UJzRdG5DbSHI2xrQQ73w7RecK5IjFkiLb7C_T6UCoIMRvlBv_JIlfpMLrOOkKgX5NH2zSyusbZzYhHzBPr7Wvbi6GmU2XT3kAvgbbFzPoN6cHNRDoMyIa7x8LhabGJwdqjWlG0V-IbFpOtfbXpmxcXEFuIw94pPYPZTGlZmqxm9oea0HSmDyWz6qFA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/ed04c10225.mp4?token=dfHpig_NDxN3HQ2TLzcIIWgB4kum2ocQicB_pst92m3qxNWmjTE59wusTmOeTB6Hsuw3xNrAsyESvAL0exQJcO8ZNyEVAhXodv6H5pL4viWFrwjm1nvHq9vd2BUgwxhE2xOFHk0R2X39PGPqaGSK9WInIHw19w8BqSUnt3_Ga2cW7ds2tk1ayAuOBtbl4z9mMYIjv0ufy3b3W45Fy5sE9L-QjpKnzMtjxzxN5MStuoyWYzPF9NERfb2msWAba1R-_14-42Ik2f4GooVbdUbdIjMpZifY02W37TxVzb2vX0zs62757hTD_YpD6k7-R-fa1HM8P6UB6m37EbWvFjCHhFH6HuunA6KdvweM6FWDv1QGywkv5ssqB0WP_8uOKwTiCh-Bm8Q9BqRJsFcMWVbWqjswhtMb76TSK1gW-B0DX2T4e93ddWRLRjkYKy8A_61zh6pli397qYtvbP_2fZW2mPbJSLYLSZetfvPgwRClJRKzFkY96UJzRdG5DbSHI2xrQQ73w7RecK5IjFkiLb7C_T6UCoIMRvlBv_JIlfpMLrOOkKgX5NH2zSyusbZzYhHzBPr7Wvbi6GmU2XT3kAvgbbFzPoN6cHNRDoMyIa7x8LhabGJwdqjWlG0V-IbFpOtfbXpmxcXEFuIw94pPYPZTGlZmqxm9oea0HSmDyWz6qFA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گل‌اول پاری‌سن‌ژرمن به مارسی توسط فران تورس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/Futball180TV/106973" target="_blank">📅 23:46 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106972">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2832d49487.mp4?token=AXvJ-dyeIIAmjLuy3X67rjh0euziDJdTQRoE9Mxos-CaHt_KKBx8RMxhQ23OBe0epYndoQcSene4x-ALzpD_EYaKr2OD4gRqh6a2szwqjG4MDIRKpS7BSLACEJGBA4QCrUH3v-ibLmtQfDq0NdIiwNXhBzTiPKKmnISObjSnGKZbpCc244EhrwLsJFHAiILjxhIXuNl23zi4UiMcMqec5yBZAQsLLpburAOmB_qzVIj22SqOayDeRpk1Oj2udD9VB_tw2Dc6x_4Rs0ffm0bfdp6RVS86_Nr4ltzaX_JR-kats5J-rPVqx09IGb_WKG7XD1Zv2_c5IalrHKk_CGh3Hw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2832d49487.mp4?token=AXvJ-dyeIIAmjLuy3X67rjh0euziDJdTQRoE9Mxos-CaHt_KKBx8RMxhQ23OBe0epYndoQcSene4x-ALzpD_EYaKr2OD4gRqh6a2szwqjG4MDIRKpS7BSLACEJGBA4QCrUH3v-ibLmtQfDq0NdIiwNXhBzTiPKKmnISObjSnGKZbpCc244EhrwLsJFHAiILjxhIXuNl23zi4UiMcMqec5yBZAQsLLpburAOmB_qzVIj22SqOayDeRpk1Oj2udD9VB_tw2Dc6x_4Rs0ffm0bfdp6RVS86_Nr4ltzaX_JR-kats5J-rPVqx09IGb_WKG7XD1Zv2_c5IalrHKk_CGh3Hw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گل سوم لخ پوزنان به رادومیاک توسط اللهیار صیادمنش
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/Futball180TV/106972" target="_blank">📅 23:23 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106971">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cjKEJ7LDLmp8KpeVZlWJZIG8k2pEREgCbJMv9mYWV8oWYqMjUxxNzSSNS47aDOJVYAkOvvZysuPGHiAWPp1TwOLbxCHvRcCoWfUZGcpYLltfmIMXqVZY5o0h182OKO91POMPfQKn0_4gs0sxY6kOzZ530Py6xkCq4qcI6md6TbyFvT6OzpjDztdanDj8tidlCRFGb2Uv8c-tnttuCt5HKqYJMV3hVwo7t-TmhN6Ln1BDjG55QwM3ERBtO8DoOQb9RFAiyM1PiMMpu_LYGCaDIXKYVG6MZpG_EAWssqfHhjAtEnF42uVKJLfWTW2BvleibajxiVTiV5gfjse_1jc0ug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
ترکیب پاری‌سن‌ژرمن مقابل مارسی؛ ساعت ۲۲:۳۰
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/Futball180TV/106971" target="_blank">📅 21:42 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106970">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/19a38b8192.mp4?token=UsOE6u-6HJxYrQpqgrrxdMCmGAx4xzOTzQb-_aec5jeZFqebH-Umu1oVRuff6FQirOCAbWln1VXRs8a5kn-MdvJyZhPQBrce6GmaYmAdidqEgLllgLCO68y8qyl7k82WSHQ-wRdVu_Lay8W2c3c8pC0iO0TJ_QlKrJRE9j19It5evky5t8oSHCW65d55PQS44rvzO4NZ9BsVBJVyRLmC666APpkxmsXJ7G4Dc_fMTpDKnSFDd3vICZNQ_g75173qEeMV0C45zl7E6viVs3HMqYmZdLvwbbq_amiAbENuu-w8OGlGLxw5Tp_awr3R8ObbyV2P8cF61x5Va3FwmmvJdQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/19a38b8192.mp4?token=UsOE6u-6HJxYrQpqgrrxdMCmGAx4xzOTzQb-_aec5jeZFqebH-Umu1oVRuff6FQirOCAbWln1VXRs8a5kn-MdvJyZhPQBrce6GmaYmAdidqEgLllgLCO68y8qyl7k82WSHQ-wRdVu_Lay8W2c3c8pC0iO0TJ_QlKrJRE9j19It5evky5t8oSHCW65d55PQS44rvzO4NZ9BsVBJVyRLmC666APpkxmsXJ7G4Dc_fMTpDKnSFDd3vICZNQ_g75173qEeMV0C45zl7E6viVs3HMqYmZdLvwbbq_amiAbENuu-w8OGlGLxw5Tp_awr3R8ObbyV2P8cF61x5Va3FwmmvJdQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⚠️
توی آلمان یه دختر تریان (انسان‌های که فکر می‌کنن حیوانن) به یه خانم حمله می‌کنه و گازش می‌گیره، به پلیس اطلاع داده شد، هر چقدر از دختر اسم و فامیل پرسیدن فقط پارس کرد، پلیس هم اون رو برد مرکز نگهداری از حیوانات
😂
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/Futball180TV/106970" target="_blank">📅 21:20 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106969">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WXrGeiF3zzz6EZKTPl-ARKhO3ybOQoD0Eksv5FyVnLpqWvl1l5Q27CFA5UTX5qwEep-AXRUHx3oyTniOZf3hEix6kp7UxJ2H4370YejKRwXTRX_8FGH5LuYxxo4INytZX_ykRHG-OaqJl8K2DWCK9ArH5DMsXvoiSIZGjp3y06OZeIeoEEXL7KTR-aLrv4tRJcwaOcx1_3NT8Gl8rMTTOSZ1wH8NXrvprFW9un-kqd0UgmpZN7p-e8ySQzhvbOrBZ91xNPySdiiQ0w2LVgbbparu9E5k8cu2aVA-F8-ao7rUToM6D0-T9AjCSV0Bf50DjHozXX2dlJxIL2GRahw-0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مورینیو در ۱۶ فوریه ۲۰۲۶ که مربی بنفیکا بود:
تو یادداشت داور نوشته شده بود که شوامنی، کارراس و هویسن نباید کارت زرد بگیرن، چون بازی برگشت رو از دست می‌دادن! من خودم سرمربی رئال مادرید بودم، واسه همین خوب می‌دونم اونجا اوضاع چطوری پیش میره.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/Futball180TV/106969" target="_blank">📅 21:04 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106968">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ovSkFpD6p1QCra811GytuxUUDm4X1J8Ym8VRC5oUimY7DE5BpI3xnNfYC8IJhmt6oG6tKzc6pg0T9ySIRjqg4S-8NjdanrGPW-HbvPYsN1XXtSCFaaygK0x46aAoL_4ms2YTVO-LxrgBkr8wtlJ_8-fbSeWzBNYKjmBRXZp4_pCxEMY1M7ZiuxBMKDodkztXmtVSt5z35eFfkwLVMA6qsWqZoXguNGEdndcnY6Vd_2iexJs08GPuCuemYksLVaq-zGcpsi8-FL9-xMVWeLfxBvVG4JjGa0rkkMR_QC6o1u5PuoVyDl0D93f-6bAKyU156nj9VPngVzWXvPRIjlCFfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
📊
🏴󠁧󠁢󠁥󠁮󠁧󠁿
نتایج درخشان منچستریونایتد در پریمیرلیگ؛ عجب کسشری شدن بعد فرگوسن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/106968" target="_blank">📅 20:58 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106967">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2b23f273f1.mp4?token=q14jsc9aKiR-MegT7cwWD80omvUDxfb4TCQ5xAgmqxj1CNvJqvgF9HBkB3gIwEiLYGV_EkRz41eugz5d_dGyXVOzgueO_lDBHudkKvMZZvy_z8hml1NuGsRLJxmK2RH_5w1GJTTWfGpNi4TKsTCGiv-BtRQjt0Tjy6G0uGscVj3N6JeIaGwY-E3lBPuxxdQz6FgZ2rFoKVxIM99ydGrQkKRSs2QkEZ24GBjsYPVyjBU57LGkL5kvG30uBRgpsMCtcD3Gefla-MIoOQVFyd8W-Ngvi6dhsaEskdif8H-LjlEpvv0xDvaeMVYsuTqEJyVCfDBiG9B1L1tZa7pTMMCyfw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2b23f273f1.mp4?token=q14jsc9aKiR-MegT7cwWD80omvUDxfb4TCQ5xAgmqxj1CNvJqvgF9HBkB3gIwEiLYGV_EkRz41eugz5d_dGyXVOzgueO_lDBHudkKvMZZvy_z8hml1NuGsRLJxmK2RH_5w1GJTTWfGpNi4TKsTCGiv-BtRQjt0Tjy6G0uGscVj3N6JeIaGwY-E3lBPuxxdQz6FgZ2rFoKVxIM99ydGrQkKRSs2QkEZ24GBjsYPVyjBU57LGkL5kvG30uBRgpsMCtcD3Gefla-MIoOQVFyd8W-Ngvi6dhsaEskdif8H-LjlEpvv0xDvaeMVYsuTqEJyVCfDBiG9B1L1tZa7pTMMCyfw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گل اول منچستریونایتد به فولام توسط متئوس کونیا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/Futball180TV/106967" target="_blank">📅 20:49 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106966">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p1XrBF-pZuOCF-nCVz_God73Y7y-TsBqKI4Ylc2sq01fv8qGKgWRCNCr1PvtL0Z_fUaUgnPyVhkoGUnkw1igfzcW4B6o3tMo1TAWvumirAQT2XG511JIeVHcipBst_hVKV-ASpHhEWXqdLdLYo066bIeczpmqDbUPzonRwq7ZonBJv0zHim8-Dvl9wFASGVcRndWoYecLMVnqs5GtpirpBXp8wvmb6FrEbmHe63zA9lK9Dv1eJwXkB6SJbPXSCIb0eiTGQ7VDJ3yorqv503pxtzJWGCJTbDl2bpBqsAU2LNE4k6_oms7I9U3B800tXKKpe75j7ffw0ORQLi6VhX7wg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
‼️
🇪🇸
رئال مادرید Tv:
🔹
وقتی پای رئال مادرید وسط میاد، برخوردها کاملاً متفاوته.
🔹
لالیگا و فدراسیون فوتبال اسپانیا اجازه نمی‌دن رئال مادرید رقابت کنه... اون‌ها یه نقشه و برنامه از قبل طراحی‌شده دارن.
🔹
دیدن همه این جریان‌ها حالت تهوع به آدم میده... اصلاً براتون مهم نیست که کثافت و مزخرفات تمام لالیگای خاویر تباس رو برداشته.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/Futball180TV/106966" target="_blank">📅 20:40 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106965">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/34da8be998.mp4?token=uoRl0GZvuwvtIIZaacD4OsY_TP9rZOk2IZvKDYYEaqHx1jTBo4I9gq4EjAvx08ri1VTwFvAIRYmuZHSPgFgqTup7_QTOkT_WNvnOlqCDVKinldrMbi4sLPfgzWv53UkRocl-BqZeOKla6ITBmvMk8HCp3qf8exLFQDCrYgPMSsDYcLdTGFfEu1k34DWrr7uJ2LGk_1rxs0xF8HadIM6VPaz8raGneegdQqOynDjM8ZfdmZBatRTZloLTMnx1uXA5x44bYMkfh4ZqJOi_hxYlZz18nKUg7PbW53Hhk924ESbuBdie3lXkRbMnV8uzxmVdH5y9T6uV4WHTII-QRaAicA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/34da8be998.mp4?token=uoRl0GZvuwvtIIZaacD4OsY_TP9rZOk2IZvKDYYEaqHx1jTBo4I9gq4EjAvx08ri1VTwFvAIRYmuZHSPgFgqTup7_QTOkT_WNvnOlqCDVKinldrMbi4sLPfgzWv53UkRocl-BqZeOKla6ITBmvMk8HCp3qf8exLFQDCrYgPMSsDYcLdTGFfEu1k34DWrr7uJ2LGk_1rxs0xF8HadIM6VPaz8raGneegdQqOynDjM8ZfdmZBatRTZloLTMnx1uXA5x44bYMkfh4ZqJOi_hxYlZz18nKUg7PbW53Hhk924ESbuBdie3lXkRbMnV8uzxmVdH5y9T6uV4WHTII-QRaAicA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🙂
حالا که بحث جنگ دوباره داغ شده؛
اگه تو آسمون یه جنگنده دیدید، سعی نکنید بهش شلیک کنید یا سمتش سنگ پرت کنید، فقط این فن استاد رو بزنید تا خود به خود به آشیانه‌ش برگرده :
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/Futball180TV/106965" target="_blank">📅 20:35 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106964">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/5cd75fe80e.mp4?token=Xk2OEsaKnEl2miIL9k1XwT7jF76wjSt3uUItgVLk1VwUrUveaxA5NW3vUFMdO-H_2B_tuAclUTN0-1WAlLkl0NQr_9w399PL6rBGyp669OP5AWk1ZAJNVPs1Hy9kn72yKxUs2eS8-P_ovAiWOWQJT_LiWg8gea3j1RzKzVTHWzCPhm-diTDzMpffL4-UVDQvaJ_-LsXgq1mj9iAskrutvc584bLmglXEsnbZtb4ZkRwrjMix7d3zy8fC0u9E2lv2JD2A_kt1n29vRK7k1nk6sYpwimoUNBAeJaWpKTlcqD7feaBGRqnMxmqfaHHUIl5gbVhddemI9I5wIWfurPvVDDMJdPiviNcW0NmINJNPiGfp44G0nWKW72VborA8BCGTUS-gXR65Z2S2IbUVq0abuMssipLy3dH6YbXUWvwyaUhKYIdi1n3BHaf5gm9PeCDiZ_UZVA4Bzgg4PIKnqMiCG28MS-zV541bloWJOT9zNRt6m6JldSBkitea2ik8fDVLLmdAXDImUEWydHLv4lk34XurbuMSC6qZw-RiTNGE0LqgZHSM1Rs_508Fh2UXyHIZ9jii5iEJ6mUVMgH7LLbVtozQnqK0MYJNFhB8TNor-SkJqscIpNm8REEptASUJ2W78JDMl7zG_jhOoCjsvcdS0fJEGAeIenlo5mCp8n_3ZKg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/5cd75fe80e.mp4?token=Xk2OEsaKnEl2miIL9k1XwT7jF76wjSt3uUItgVLk1VwUrUveaxA5NW3vUFMdO-H_2B_tuAclUTN0-1WAlLkl0NQr_9w399PL6rBGyp669OP5AWk1ZAJNVPs1Hy9kn72yKxUs2eS8-P_ovAiWOWQJT_LiWg8gea3j1RzKzVTHWzCPhm-diTDzMpffL4-UVDQvaJ_-LsXgq1mj9iAskrutvc584bLmglXEsnbZtb4ZkRwrjMix7d3zy8fC0u9E2lv2JD2A_kt1n29vRK7k1nk6sYpwimoUNBAeJaWpKTlcqD7feaBGRqnMxmqfaHHUIl5gbVhddemI9I5wIWfurPvVDDMJdPiviNcW0NmINJNPiGfp44G0nWKW72VborA8BCGTUS-gXR65Z2S2IbUVq0abuMssipLy3dH6YbXUWvwyaUhKYIdi1n3BHaf5gm9PeCDiZ_UZVA4Bzgg4PIKnqMiCG28MS-zV541bloWJOT9zNRt6m6JldSBkitea2ik8fDVLLmdAXDImUEWydHLv4lk34XurbuMSC6qZw-RiTNGE0LqgZHSM1Rs_508Fh2UXyHIZ9jii5iEJ6mUVMgH7LLbVtozQnqK0MYJNFhB8TNor-SkJqscIpNm8REEptASUJ2W78JDMl7zG_jhOoCjsvcdS0fJEGAeIenlo5mCp8n_3ZKg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🏴󠁧󠁢󠁥󠁮󠁧󠁿
گل‌اول فولام به منچستریونایتد با گل‌بخودی لیساندرو مارتینز
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/Futball180TV/106964" target="_blank">📅 20:22 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106963">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Eez4MwGMrEWn0BcjEXLu3PUJsDYovgOONy3T9SsEJkqmVzz3p53YxJX6srKCI07hsMN6UAK54M5hOCmIoh-xSCoZaYlZk595nNze4a88SjI4AMpPR_9B6y3qGLMTOjwI7iyH2b6vSHc9-JMh_nla5bIXnP3emyejzHeAF_8_aZykLgV2s7Fn3gYbDVY0xWsFFW-oaHGcss-ss82gd5Mw1rdVGcTfFH58HHK5wjY_cJz6kAeoK7b_zUN6dtK9ecxoAs0qiKmk8bTP5EL2ivU9GAAGjD-U8TlTWAnE-gO6vpO2YqaG8huj-WPpJQH-lyOlvLmF_Is9vAE10axGHMBoIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🇪🇸
خوزه مورینیو
: به کمیته داوران تبریک می‌گویم. آن‌ها باید از این نتیجه بسیار راضی باشند. همه‌چیز بسیار عجیب بود. بازی باید ۱۱ در برابر ۹ دنبال می‌شد؛ چرا که اتلتیکو از دریافت دو کارت قرمزِ مسلم قسر در رفت.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/Futball180TV/106963" target="_blank">📅 20:20 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106962">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h24peNpc9RdUdcU2XdsPTZYHtONA2yK4qZxXXN343kGbgDrVxSyFLNSn2KDCT-rmZsQcPfkl5_Lt8K3l_6PEXI98L_ZPASaC_60HMQ4IUmYzU6SQeR53UjgfJCu5_OcvBRon7zPmuo49iBVYUsv6cdImUFAubTvY5Z8-yHdHPZUlSmgc6vVAVjIppMFzzsY1jWSGBDips6kKKts09h5wHsbpX_dGh_7MxD_Ga1ZSXfz7U3mdNXyXoCQMHFwDSeJhmxp4mIuFXRK2d0YcXQSpGJGWyCYoKU2j7Lmndsy-uWGb-uFE4QklaU9GuS4D6OLm7GB8-1Z5i5PjMun5Gnzb2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
‼️
🇪🇸
کانال رسمی رئال مادرید:
اورتیز آریاس داور بازی، رفیقِ لامین یاماله…
😆
😆
😆
😆
😆
😆
😆
😆
😆
😆
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/106962" target="_blank">📅 19:53 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106961">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c_0FRQypukm6I-naqJLyvDGT_n8xdpEr84dAMfZmY6HWmf_GSE_g5bewDkxEk2fV4x1PcMlrMi9842Ilfn0YuCOM65vgOvhYVM-9om8LmOrsJV-aCje4V1rHv2otPjfys6ou2TKiuSLsxQs6kH3bAqmpaE7o63CQkJzUPDN-MQVXNWocAxBC8R0cBZo68vu3vmnHg8w2B_1BV7ANUBJoJ3yoIG2zMVgFIapCSyZwxvPuZ_maS9xw80CrZH1nL3YtkZYdDnOJ8zw3Ga3tcCkSEz-c12VeKG_dliWn03Ws9X2yw3dDkn_NC-7GQDxQVw_GAGiSoox81PUUhjJBPARijQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
هفته‌هفتم لالیگا؛ دربی مادرید به سود بارسلونا شد؛ رئال بازهم شکست خورد و فاصله تیم مورینیو و فلیک به ۶ امتیاز رسید!
🇪🇸
رئال‌مادرید
😃
-
😀
اتلتیکومادرید
🇪🇸
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/Futball180TV/106961" target="_blank">📅 19:51 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106960">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Afx-2J8o2WcQse0K5iPQxncuKq3hllYkKOhwTW5xVvsFhCIDw_kOowY2cq7vvy_05f4Xr6pAgW-SpFag1HEVcyiJP2fOrSWmb2ZSvE9RM1UFFfz06psj6INKe_keeD7P4vUEVHchdV-3aJPf3MbEt_il7CGJhmCyI13DLKtifHtY-tG4KZGplknLMRu1xdwM5JFCi3HU0Fph0zCHx_KsnFO_vnZX66iUqCarYdyvQLmfCotcs4SeB-diCPETIp2Vg-nHerI7S5-DKbpI5cLYWlegMNLagtslyr8ft-Y5kqv2Q0rbEn7xZVOsdhnKWRTns9IeqclZOAZKgNjtjgQWcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
هفته‌هفتم لالیگا؛ دربی مادرید به سود بارسلونا شد؛ رئال بازهم شکست خورد و فاصله تیم مورینیو و فلیک به ۶ امتیاز رسید!
🇪🇸
رئال‌مادرید
😃
-
😀
اتلتیکومادرید
🇪🇸
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/Futball180TV/106960" target="_blank">📅 19:48 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106959">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tzLG5SkqKspwuf2Yzv3xMNfyu9NhLsJQWPUL5LuSoZGujPCuq1-cLxuVMyBK5jhR28clLOLsLhuxOS3cmv2Mo2KsxRnhtaTLuU-GH33FJLYeqwYx2o9hq8-uatYjbng0e2u5qKo9_2ztlI9MHO_GTntSuOrQ_b6yapCRU0nczJdD71ipKBplGgG3VPT4ofOmpes93H0N4PmFlUJPx83Bc4xLNu9lcbNMneClA8NIgNLTZbkFNIRV0NRW7fwMSZ7x0klmEJb7J53oRhX60bq0uRExAi8zO4IsT8Ng8Fjnt8PYtdGcKhsdAHUtWT6XfcR0IRSvxB8fIOb0VCwvdRuXDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
هفته‌هفتم لالیگا؛ دربی مادرید به سود بارسلونا شد؛ رئال بازهم شکست خورد و فاصله تیم مورینیو و فلیک به ۶ امتیاز رسید!
🇪🇸
رئال‌مادرید
😃
-
😀
اتلتیکومادرید
🇪🇸
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/Futball180TV/106959" target="_blank">📅 19:45 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106958">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">۶ دقیقه وقت اضافهههههه</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/Futball180TV/106958" target="_blank">📅 19:40 · 29 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
