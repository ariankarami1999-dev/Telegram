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
<img src="https://cdn4.telesco.pe/file/IiwktjHCndONpWMQmVILs3yArRzo5kcY5jRWi9tZXtuIiWKdvPtwsbbjHhpz1yNQ9TfdvH_zGZlT1-kECSoX2mHVQJkFbfVsA-QgiNQCKbJovCWiqCzhnU682-710FkBaLeItKLj6Q-eKd0-cDART6ryllTXGBkauIJQqsxytB5G8ak2XVfT_MsQ4_o_07SBmyYsIVO4HwwOf0tFHg9jIq9FVZ7vPuGrV4gZwwrv1P7DkRSQGim36w55DBiW1aS0hvBJI8mj0bmPSppEhRUneW7ao1uyQHWaRyHkDRnXSu7GK8_4zDtsqullixtph6BMbSJKCDiS0WaoATp4Shxbow.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 176K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-22 17:39:15</div>
<hr>

<div class="tg-post" id="msg-67998">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3ebd104df8.mp4?token=p5wZs0zZQ8jdFDJBjyr1mX0YziJqvQ87wBgsVZBK2fQxYAaH27CJAihtXV45Rvt6d-tt56cswMilykO1GrGqxdyOvMtlvkB5dVrU1vjq0kdYr_6BC0jveuL9Itl7j_ZLdpaAgJ4mh7bGNq22jD7eSHbokZfQcvTI8jPhSj6tbe5FbwYA79OyzLFsxXqmLGJsO0wmarTbOR5jlNTRm7l14iPqBMTi5dZpouyd2Rf0xzsEm6Eb9QffCTUkx-Huch5uaP-FYQe6v9f8KfwDRjT6sRDPdDWlEmVAfYpurdVm6YWY2VTkk9zZBixtPRzKDOln52uf4vhGhUJW3_O4_ZOq7Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3ebd104df8.mp4?token=p5wZs0zZQ8jdFDJBjyr1mX0YziJqvQ87wBgsVZBK2fQxYAaH27CJAihtXV45Rvt6d-tt56cswMilykO1GrGqxdyOvMtlvkB5dVrU1vjq0kdYr_6BC0jveuL9Itl7j_ZLdpaAgJ4mh7bGNq22jD7eSHbokZfQcvTI8jPhSj6tbe5FbwYA79OyzLFsxXqmLGJsO0wmarTbOR5jlNTRm7l14iPqBMTi5dZpouyd2Rf0xzsEm6Eb9QffCTUkx-Huch5uaP-FYQe6v9f8KfwDRjT6sRDPdDWlEmVAfYpurdVm6YWY2VTkk9zZBixtPRzKDOln52uf4vhGhUJW3_O4_ZOq7Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
پرزیدنت ترامپ درباره ایران:
ایالات متحده شب گذشته ضربات سنگینی به تجهیزات آن‌ها وارد کرده و ممکن است کنترل دائمی عملیات‌های امنیتی در خاورمیانه را بر عهده بگیرد.
«بیشتر تجهیزاتشان از بین رفته است. ما دیشب ضربات بسیار سختی به سامانه‌های ضدهوایی آن‌ها وارد کردیم.
«هر بار که پهپادی می‌فرستند، ضربه سختی به آن‌ها می‌زنیم
.
«اما ما توافقی داشتیم... و آن‌ها آن را نقض کردند. آن‌ها همیشه توافق را زیر پا می‌گذارند.
بنابراین ما هم ضربات سختی به آن‌ها وارد خواهیم کرد، کنترل تنگه را حفظ می‌کنیم و احتمالاً خودمان اداره امور را در دست می‌گیریم
.
@News_Hut</div>
<div class="tg-footer">👁️ 1.69K · <a href="https://t.me/news_hut/67998" target="_blank">📅 17:36 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67997">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/060cc64d0d.mp4?token=tWNf8LBDIfTsy7nYotGM9xutzXZgCZdydQCAZEKA5LcFTAJpiotcnHsGHNXvX28RzT78TIsdqI4guVwc8syWIzjSWhlEuw8SZX4M14K6a-UfT2QC5E5uj82t9rAQJrLl56eU5EMsBisn7TcuBi0Jc98aPK8WcrNYd0U3acG88s7G84-ZBp28CUlHysJ0gbS14c7dChRu77_tC14bduNQZv5YTViO6Ohk0pOFXuWLavfCWqutQmut78fFQU0mZ3aXXJXVYlUtWItZYPwbdWIyhrflq8-Cre_TVHls9hPQf80EtZD--5Tyc8wOKHmU6RpA_zt4JZpfu5AdD09yPrV8IA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/060cc64d0d.mp4?token=tWNf8LBDIfTsy7nYotGM9xutzXZgCZdydQCAZEKA5LcFTAJpiotcnHsGHNXvX28RzT78TIsdqI4guVwc8syWIzjSWhlEuw8SZX4M14K6a-UfT2QC5E5uj82t9rAQJrLl56eU5EMsBisn7TcuBi0Jc98aPK8WcrNYd0U3acG88s7G84-ZBp28CUlHysJ0gbS14c7dChRu77_tC14bduNQZv5YTViO6Ohk0pOFXuWLavfCWqutQmut78fFQU0mZ3aXXJXVYlUtWItZYPwbdWIyhrflq8-Cre_TVHls9hPQf80EtZD--5Tyc8wOKHmU6RpA_zt4JZpfu5AdD09yPrV8IA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
⭕️
🇬🇧
دولت بریتانیا رسما سپاه پاسداران انقلاب اسلامی(IRGC) رو در فهرست سازمان‌های تروریستی قرار داد.
در حال حاضر، ایالات متحده، اتحادیه اروپا، بریتانیا، کانادا و استرالیا سپاه پاسداران را به عنوان سازمان تروریستی ثبت کرده‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 5.4K · <a href="https://t.me/news_hut/67997" target="_blank">📅 17:19 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67996">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/4923d848c0.mp4?token=G1Xe-VyJGFbPffAg7TOumyhPMYXxO3JI5zbs1Ruwb1a6VTPoBuhhQfG5Pzjquqk3JgimQAuxrcxgGLfoaUseoo0tZDsAb92LEXC6ZtpV6EBiiasd6isnIWnuyJwA_wEx-j8x_1VkZJhYceM-zgMwWCsA7GJzZgNRaHUVnSsC3y2AHc74yzOU1cU9X5ExeLHjaXiCi8XxOtMldPgtkv8IJA2g5L9ZcZiah-y63J4aBBSyGlZfK81P5sLNG8tfvGvtazSwozYxbyN_WKRI_-yDQAijC2PFuCHulnLz7__RPtWJa0SFG5Y-xiqjTwC-gUcxgx_l6nlvdgcIHdddJDAimg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/4923d848c0.mp4?token=G1Xe-VyJGFbPffAg7TOumyhPMYXxO3JI5zbs1Ruwb1a6VTPoBuhhQfG5Pzjquqk3JgimQAuxrcxgGLfoaUseoo0tZDsAb92LEXC6ZtpV6EBiiasd6isnIWnuyJwA_wEx-j8x_1VkZJhYceM-zgMwWCsA7GJzZgNRaHUVnSsC3y2AHc74yzOU1cU9X5ExeLHjaXiCi8XxOtMldPgtkv8IJA2g5L9ZcZiah-y63J4aBBSyGlZfK81P5sLNG8tfvGvtazSwozYxbyN_WKRI_-yDQAijC2PFuCHulnLz7__RPtWJa0SFG5Y-xiqjTwC-gUcxgx_l6nlvdgcIHdddJDAimg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
بیرانوند
:
اونجا وقت برا دوش گرفتن هم بهمون نمیدادن.
از بس بهمون سخت گذشت که تعداد زیادی از بچه ها شورتشون اونجا موند.
مثلا من خودم شورتم جا مونده آمریکا.
@News_Hut</div>
<div class="tg-footer">👁️ 7.87K · <a href="https://t.me/news_hut/67996" target="_blank">📅 17:03 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67995">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c34b88bf07.mp4?token=Yzuy-74qYP957UiM7OqRxXnO19rdYFfODMZMFXJv3na7nlpnlQ7JjT57c8zbXCb-VGG4F6DO2icqnj1Bv7UAFAfM5YFGptPf8jXW8eB8-VVJOFPqOM1NVY7zUyY61cYrJPHP8uv6LOhtA_6cxBW-hNIPNDC6hKgPJBeJZ6L-eeVIL0nZ4JVheUmYFjYk5iOQq5t6Wn85MJKTcjPUeNI4VAD8EN3SSMLuSXCeBGl_hN_w6CqW13Jfu6oths9bAWggh0R6gEhNhq98mvCLeNFqQUxdniLLYc0Ndbt0GyMtDjROXI36O7P-212KGOvFm_nnATvSXX_tQts8OmtYdt4kKw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c34b88bf07.mp4?token=Yzuy-74qYP957UiM7OqRxXnO19rdYFfODMZMFXJv3na7nlpnlQ7JjT57c8zbXCb-VGG4F6DO2icqnj1Bv7UAFAfM5YFGptPf8jXW8eB8-VVJOFPqOM1NVY7zUyY61cYrJPHP8uv6LOhtA_6cxBW-hNIPNDC6hKgPJBeJZ6L-eeVIL0nZ4JVheUmYFjYk5iOQq5t6Wn85MJKTcjPUeNI4VAD8EN3SSMLuSXCeBGl_hN_w6CqW13Jfu6oths9bAWggh0R6gEhNhq98mvCLeNFqQUxdniLLYc0Ndbt0GyMtDjROXI36O7P-212KGOvFm_nnATvSXX_tQts8OmtYdt4kKw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
🇮🇷
🇺🇸
سپاه ویدیو ای از حملات موشکی بامداد امروز به پایگاه های آمریکا در منطقه منتشر کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/news_hut/67995" target="_blank">📅 16:14 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67994">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8627adc5f4.mp4?token=GeS4Dt_rEdKzJsAnARbKOZg79rlFazfpA53Cds_asgmd8h0-HeNEitejQUMRieHc5o9sHLtBwEGsmHr1OzMKlqjAYECwX1ABETjUz9DTIoMptHe86mu-Htjf52KUjgayWRg5V4-UuOSfZaNoOksKNQemojX4nTXqHA7pOpvTS1MxGra53DdNFttlh2KTNFbvLHigItvksg1yGUt7nSzM6tPrNmJFUZtRqGnQzwddYNPPYDj4tjNJtROvzGTm_c_TdUfauYtvc2vimoPv33SK8a_TBmntVmaYUxVluUTIwaeGjCRI1UFexRSAejopDAoT5iwX1PEDvVmcMrrVzmuqvA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8627adc5f4.mp4?token=GeS4Dt_rEdKzJsAnARbKOZg79rlFazfpA53Cds_asgmd8h0-HeNEitejQUMRieHc5o9sHLtBwEGsmHr1OzMKlqjAYECwX1ABETjUz9DTIoMptHe86mu-Htjf52KUjgayWRg5V4-UuOSfZaNoOksKNQemojX4nTXqHA7pOpvTS1MxGra53DdNFttlh2KTNFbvLHigItvksg1yGUt7nSzM6tPrNmJFUZtRqGnQzwddYNPPYDj4tjNJtROvzGTm_c_TdUfauYtvc2vimoPv33SK8a_TBmntVmaYUxVluUTIwaeGjCRI1UFexRSAejopDAoT5iwX1PEDvVmcMrrVzmuqvA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
لیندسی گراهام، دوست وفادار ملت آزادی‌خواه ایران
🖤
@News_Hut</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/news_hut/67994" target="_blank">📅 15:29 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67993">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/57a38d8e8e.mp4?token=K_mg-Bfw2HGFYq6Zu4jgonQqrtPCWLku633aTV37lpfTLev_1jcHISUNHamkeCKv1MOujl-wiX6O9PwnInEv7z-ftmVFegPqMkfotKv2Gl2ifAz6bg0GA_FzvjaqoWT8-GUYWxQlOmAR4qssI6O0qMsWBz5EU5Aj_t_88S2ype7krXRi7dUpDGz1indSlVYej2Alv2x8YvAocDaaL6Qjshza3lNNrpZXSxNh6cFsoh4vzTzGXPDfZw2azwQ8Yk_WtT6dBKNqLichD45CNbKOS5HSjQIl4q82z4agBMl6MKr5vK9LeVr_ZyytquA9mVahRZ3vQ2N1rx9I0pZo_SSkHw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/57a38d8e8e.mp4?token=K_mg-Bfw2HGFYq6Zu4jgonQqrtPCWLku633aTV37lpfTLev_1jcHISUNHamkeCKv1MOujl-wiX6O9PwnInEv7z-ftmVFegPqMkfotKv2Gl2ifAz6bg0GA_FzvjaqoWT8-GUYWxQlOmAR4qssI6O0qMsWBz5EU5Aj_t_88S2ype7krXRi7dUpDGz1indSlVYej2Alv2x8YvAocDaaL6Qjshza3lNNrpZXSxNh6cFsoh4vzTzGXPDfZw2azwQ8Yk_WtT6dBKNqLichD45CNbKOS5HSjQIl4q82z4agBMl6MKr5vK9LeVr_ZyytquA9mVahRZ3vQ2N1rx9I0pZo_SSkHw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
🇺🇸
سنتکام ویدیو‌ ای از حملات دیشب ارتش آمریکا به اهداف نظامی جمهوری اسلامی منتشر کرد.
در این عملیات سامانه‌های پدافندی، رادارهای ساحلی، توان موشکی و پهپادی و شناورهای نظامی هدف قرار گرفتند
.
همچنین برای نخستین بار از پهپادهای انتحاری دریایی استفاده شد.
@News_Hut</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/news_hut/67993" target="_blank">📅 14:59 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67992">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3e3c5be180.mp4?token=a5bPe4AhiUI2yvLBIdZFxBo5twJX_px6H4lbQipzwkzU0gWB_zi7mqcrnVgLDbk29wvV5SVrHw0zXt43tu7nz-iDEkuQwqJmLFs2FP4ZKuB8w2wg7JN5S4uQozNo_pVG-yhYUUjI7I0v5t2U_-H6WB6bai3_oPq3wsv8b6OIyWm4rmqtnda6I4Cf36AhcW-WnJODZUopWOuyER-UkfYOetPwlKWkUVN75v4mY1rTTeddtIGdmVnvbWqCKKAKaBW67WtDtK34Lnb59LXd1qZ1Naa32d2KslsRgWl0By28oMKlrVt5vLcSOR3OF-VbpYmoBWu2vdgzlsiPi1oFIc-DkQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3e3c5be180.mp4?token=a5bPe4AhiUI2yvLBIdZFxBo5twJX_px6H4lbQipzwkzU0gWB_zi7mqcrnVgLDbk29wvV5SVrHw0zXt43tu7nz-iDEkuQwqJmLFs2FP4ZKuB8w2wg7JN5S4uQozNo_pVG-yhYUUjI7I0v5t2U_-H6WB6bai3_oPq3wsv8b6OIyWm4rmqtnda6I4Cf36AhcW-WnJODZUopWOuyER-UkfYOetPwlKWkUVN75v4mY1rTTeddtIGdmVnvbWqCKKAKaBW67WtDtK34Lnb59LXd1qZ1Naa32d2KslsRgWl0By28oMKlrVt5vLcSOR3OF-VbpYmoBWu2vdgzlsiPi1oFIc-DkQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
تازه‌ترین ویدئو از حمله هوایی به فرودگاه صنعا
@News_Hut</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/news_hut/67992" target="_blank">📅 14:47 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67991">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SbYr0IKYL8l-zp0C9RSDh8ZELAE0N_eAdDFkMSoz711-okHflwgTdzk7ViJuOvNqlPNJdRkzrJDen-VdAoGh7yeIFYXcvRB-d4-rPKuEbHTRr_Kn0IshdgVWVJeWrX9-3TF9AkfFvCDsLewLKiFuDSGN1DuXgYdQf7DqR3F2ygVjuCYefCm_KCEhcMmXj4-LnEvCQKpkyu27HXLgFg2Bh2J0b3L20A_skI1DF3ARuSLr7PGdmKErFcwEJkje2S1L8qAXaya1aa8PXv57u0bbozrIVLg7cO4OMqNmINCnz7tDqT11fNdeaq-9Fg9jpijWu9vB5KtMjvGtQ6f40mybDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
هواپیما جمهوری اسلامی داشت میرفت سمت فرودگاه صنعا، این فرودگاه بلافاصله توسط جنگنده های عربستانی بمباران شد.
@News_Hut</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/news_hut/67991" target="_blank">📅 14:43 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67990">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZsuLfZ12zNeQhTpgMU_OGRsAvW8sNGaZ7OtYBb7YfNWAlNNMzkRSMMBq024J8TFpJ8Mpnm_rUTsXGZR3Ru1jF54axGnvNoOIokgkL8eCs9r2HZw-ChKu9GnnAQ8EHfQlJ9z23oiiSHaHY9hb9UOMGgUpKE09XD8q9SDjKIP1PjNHL0eDon0gMxw6CF8Ijw7Zdpvjj7FanUN_AUS0va0v68NpYm_T7fi4HfO3VFkuUWPthpKH7p0SzjeimrAY_hmrDE4Q1p752urlFmQDj8aeToaFqAhoyLtiTLa1qJm_SMFTcL-xd5MCidHv5dD1qMF4ZPa5S5oshSSCTjXMo0d8Tg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بیژن مرتضوی، خواننده وآهنگساز ایرانی، با تصمیم فیفا در بین دو نیمه فینال جام جهانی ۲۰۲۶ به اجرای زنده ۱۱ دقیقه‌ای خواهد پرداخت.
جاستین بیبر، شکیرا، مدونا و گروه بی‌تی‌اس در این اجرا حضور خواهند داشت.
@News_Hut</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/news_hut/67990" target="_blank">📅 14:36 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67989">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Gui1c7A-sQqyB81MPbEncYkeeG23LYJSwZ0avX06LMC49XVA8SGDglFSVLJLO4D3iyQ4HCqwnWi6uoMfjr7uJu8wpmIm1wuo84U_Z_MncUNoKGMsDnngnyIBLWPwI2whM1rzKmza6HIOd3akqzUfpYexv1F_QAeU9nm9r3FkswN2u3fp4fyGV1hJ67TvYMy1dz90tRez86vWRXMgRZdf-4Y09M-zxtJU1fadlF2azTGDIE9J_4odr_8IHKqaDTArsMrAq3ccDLYGoPQM8aBMVU6KyGv5O54e3FXC_GnDkeiQEb9yqTjZ05S9gPFrZXoIlXFJ0UHdQFscOz6pSpwntg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
رسانه‌های داخلی وابسته حکومت این لیست ترور رو منتشر کردن و نوشتن لیندزی گراهام اولیش بود تا نفر آخر بی‌خیال نمی‌شیم
@News_Hut</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/67989" target="_blank">📅 13:51 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67988">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🚨
تنگه هرمز دعوا شده
@News_Hut</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/67988" target="_blank">📅 13:12 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67987">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6c7891d1b9.mp4?token=MxHBDEqVNSGDNIMyXdltAt-A_oERz96Te3cfw65FGxZjQkz6-by62V2Vjdwhe62y4EZWBfR_PSBgBA3JPUDBixuQdjy0o0FdqUO105VcbvaIVgNHONlb9TFKkGIqS_LySv7kMpgtsDgBbJTK46j7qmpOv-yp9HsErlMPdNLZNX01Shn58dgSthRAuaYEw8ccc5tVRjBmxwyPJRyvfr6TyzNFFkkxPBXcQKkHFDr0_HOEumEzqyxS1bMZKVeZNnxC_wfcGWyQm6aDqE9pFEINV28DCYAgD0bt9IF-h_rTHdBX2Vy_fmc8n88A-I4nDQvRyCnROxnENPGBRiRzCgjlCQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6c7891d1b9.mp4?token=MxHBDEqVNSGDNIMyXdltAt-A_oERz96Te3cfw65FGxZjQkz6-by62V2Vjdwhe62y4EZWBfR_PSBgBA3JPUDBixuQdjy0o0FdqUO105VcbvaIVgNHONlb9TFKkGIqS_LySv7kMpgtsDgBbJTK46j7qmpOv-yp9HsErlMPdNLZNX01Shn58dgSthRAuaYEw8ccc5tVRjBmxwyPJRyvfr6TyzNFFkkxPBXcQKkHFDr0_HOEumEzqyxS1bMZKVeZNnxC_wfcGWyQm6aDqE9pFEINV28DCYAgD0bt9IF-h_rTHdBX2Vy_fmc8n88A-I4nDQvRyCnROxnENPGBRiRzCgjlCQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
خبرنگار:با درخواست گروسی برای بازدید از تاسیسات هسته‌ای موافقت میکنید؟
🔴
بقایی:خیر
@News_Hut</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/67987" target="_blank">📅 12:54 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67986">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🚨
🚨
گزارش ها از وقوع انفجار در بندرعباس
@News_Hut</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/67986" target="_blank">📅 12:41 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67985">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2b2159365f.mp4?token=GUAexAA7iMNVwRp2I3RZDLcDMPq_jm3N0hSF7qoCKGbADcLiYzNt9G7fb05U_NxC5K2-7ne1HwMTBXtl5ZoV2INJGN9LFiKaYyp6YPZj7ci9l1JuiItLOXmDPHgIWr1TqtCIoOU3lpRkopIHNraCOXKI-tOFNUywDpqt3W3Wn94ojatUuhr-HSsELZGMRvKBf5sPYGcItR3vBWGT1BxolbJhKkRKSMmEdrKE0okYaYDI_GphKv7DStN9Zg3jABVJ_Cs1qF8seKrDlRoHGPXbyIS8_vdmETfNfvFo2xMruFj_7D_eq012Rv99XDKl4mpscZa224QV_JlkVzu1V_f7Dw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2b2159365f.mp4?token=GUAexAA7iMNVwRp2I3RZDLcDMPq_jm3N0hSF7qoCKGbADcLiYzNt9G7fb05U_NxC5K2-7ne1HwMTBXtl5ZoV2INJGN9LFiKaYyp6YPZj7ci9l1JuiItLOXmDPHgIWr1TqtCIoOU3lpRkopIHNraCOXKI-tOFNUywDpqt3W3Wn94ojatUuhr-HSsELZGMRvKBf5sPYGcItR3vBWGT1BxolbJhKkRKSMmEdrKE0okYaYDI_GphKv7DStN9Zg3jABVJ_Cs1qF8seKrDlRoHGPXbyIS8_vdmETfNfvFo2xMruFj_7D_eq012Rv99XDKl4mpscZa224QV_JlkVzu1V_f7Dw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
اسماعیل بقایی، سخنگوی وزارت خارجه جمهوری اسلامی:
ایالات متحده مسئولیت مستقیم تحولات اخیر در تنگه هرمز را بر عهده دارد. آمریکایی‌ها از همان روز نخست زیر قول خود زدند؛ آن‌ها تلاش می‌کنند مسیر امنِ هماهنگ‌شده با ایران را دور بزنند.
@News_Hut</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/67985" target="_blank">📅 12:15 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67984">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/48c1ae996e.mp4?token=iNQiN_32D5p-9a0Rs0K3S7rPpDqaBGHte66V3wZVTNXneQJT8y2e4RAFy_luJO4bZLHN5YX19FpeaJj0-9MQ1A0QrmldkiP7GjVhwHbZ9dIDpn_mFpL6x3l4uWsMHBxsv8NJJFul61aHkoc6qsKZI9JiwF9hLsWTgiG96iWXmft5nQNjUZ32Fx4-pDFkNJihCK3Yf6pxtYb0dj1HZ0MNx-VGVY32YSZbeMT2h9EkvaQr_ygVc-Ivok4zQsEwxtGo5anzsVI1cW0SpXiq4gKkv9HBFNORWTL1_sGUtHvDN9ulE_7990NnAZV8BJgAfqgpyjvUY4lJv8latR-VDJ9xRg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/48c1ae996e.mp4?token=iNQiN_32D5p-9a0Rs0K3S7rPpDqaBGHte66V3wZVTNXneQJT8y2e4RAFy_luJO4bZLHN5YX19FpeaJj0-9MQ1A0QrmldkiP7GjVhwHbZ9dIDpn_mFpL6x3l4uWsMHBxsv8NJJFul61aHkoc6qsKZI9JiwF9hLsWTgiG96iWXmft5nQNjUZ32Fx4-pDFkNJihCK3Yf6pxtYb0dj1HZ0MNx-VGVY32YSZbeMT2h9EkvaQr_ygVc-Ivok4zQsEwxtGo5anzsVI1cW0SpXiq4gKkv9HBFNORWTL1_sGUtHvDN9ulE_7990NnAZV8BJgAfqgpyjvUY4lJv8latR-VDJ9xRg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
اسماعیل بقایی، سخنگوی وزارت خارجه جمهوری اسلامی:
پیگیری عدالت برای رهبر شهید، یک اصل جدی و مطالبه‌ای همگانی است.
@News_Hut</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/67984" target="_blank">📅 12:09 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67983">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fb543b9b84.mp4?token=kG3kMyx8DoyTWCW7jB6_Fr11UM-WkcL1Y-s3I47lrmDQCowMfmjuBOVdv_IijvQYNYJahU-cmbHmNB8zMGwP3wCavZft5-Pzau_86BnxerGKcpnmm0uSHRPFjXTKbDZyqrIGhQcygbuU0IpKgd1NSi_2uOozkgHkfPAro4iWmLatY0gB-SpqMo9j6xFXkDtZXwx4xwtSBAZ_z540dAhkCCFS7nERO_52UMciNZQ2UpIuYCwLsqXEGK7msw7QuYgB9o_bfSJzsIVwD5U8jeOGclnc-YqowoHz1nwsQ-UlHOjVQxP_AssbBv8xeZYt91qLYffP3N09m1gL_Os6N7V5fg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fb543b9b84.mp4?token=kG3kMyx8DoyTWCW7jB6_Fr11UM-WkcL1Y-s3I47lrmDQCowMfmjuBOVdv_IijvQYNYJahU-cmbHmNB8zMGwP3wCavZft5-Pzau_86BnxerGKcpnmm0uSHRPFjXTKbDZyqrIGhQcygbuU0IpKgd1NSi_2uOozkgHkfPAro4iWmLatY0gB-SpqMo9j6xFXkDtZXwx4xwtSBAZ_z540dAhkCCFS7nERO_52UMciNZQ2UpIuYCwLsqXEGK7msw7QuYgB9o_bfSJzsIVwD5U8jeOGclnc-YqowoHz1nwsQ-UlHOjVQxP_AssbBv8xeZYt91qLYffP3N09m1gL_Os6N7V5fg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚠️
نیروهای آمریکایی با استفاده از مهمات سنگرشکن، یک تأسیسات موشکی زیرزمینی در پایگاه چهارم شکاری تاکتیکی ایران در نزدیکی دزفول را هدف قرار دادند.
@News_Hut</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/67983" target="_blank">📅 11:29 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67982">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JgUtZu77c33mr6hYVjs45HDMe3Joeh_ftkGpEbgUDMZHWmKnZ9Q1Z_9ywUfk5kRtLHOzXNmi9MrzCnAhGW5WweXgVlWWwGRC9XIx5wXP4ujtciC40JGWKDRxx7LvIjwv4d6F59MukGFsUR5klWFPLHHDqpOHyAsSEuZguk8umhogGfgCmI8QYjgPMb9oa1N4BYhz4vjLBt01-vB98bDI1F26ikoZPPS8D7mmUfWC6Mec6mtaQdFI9rYJtV7pTdRnX8c3zeXU02y32g71hX4VbXFTE0g1kmZ-Zd2PnO8otZ7Y8N42ocw-95Z9XcDag2UkaibTdJ-WcuNhC5ZRhKc1Qw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
🇺🇸
پرزیدنت ترامپ در تروث سوشال تصویری از لیندسی گراهام منتشر کرده با کلاه معروف:
Make Iran Great Again
ایران را دوباره با عظمت کن.
@News_Hut</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/67982" target="_blank">📅 11:04 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67980">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fAQFv2J4l3BsbjxgbIxiVuGc23GlgoL_6t45ifoFVJ2KFbDB2ppUZlgTYCHZN44pr80JEdZuUQcwE1kTmFLXpAIzYT_bjekJ_ElFKmbO254JzrG076uP3qmRN9-r-nmOmCQTpx36tdv8u4SyPu0HHXUlPt1e2Blq_hrE4ZvEB8bcLN_Wy8LJUtXFmpr9W6cI9ioSzWTm33AQhlZ8BK2ChyTDlaAXijKZWyseCeTDAcfgfIhmCxLWe99Ig315O-Y6_vrAGw6_9cJkXCvOvE4k7-jOfcEZ0h5oS0CSO6r4Ce0aPRv17g3c9bRB9sXUhRT646LCJQt4ygAC8_QN5gGpEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fd5R2HjAuMZbHy2_OqjcvmrX0hSpZUIlCVeE5IDanSdMYPqHnbsunK-ipGyeHo1tvDXjwgBk-VjeUOyOoXAwW4dfNZMSKiKo9IORstma8n6pZtOsVm6l2Gl_wfmtd4F9qXa2HwR6jjd5Fq-Sg7-hauhRv2RJMuM08KKnZQuJKlKBS8eZzc7Lb9SWKU5QZ2Hp7msfaLZafRStI_RckwpQuAWp0GvknCHnOTzs6H-uyykWLmVBqSnyB-tA3YAJB8kkaJG2I7I6pb5D8DGHFatsAmneGQEWPSgQMgd-erbzSdt8Sba3I2HSRmHYC0-3us1SDIlvOtQ7cNLNh8D5jWOESQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">❌
انهدام پهپاد انتحاری لوکاس آمریکایی توسط پدافند رژیم در بندرعباس.
آمریکا در بامداد امروز برخی مواضع نظامی جمهوری اسلامی را با پهپاد لوکاس هدف قرار داد.
@News_Hut</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/67980" target="_blank">📅 10:22 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67979">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dddd337574.mp4?token=IwC_qqZALDbXZK-piKZA7-ihDV4rovCtaSHN_fE-MSgRyjT6ihsNNuqYKJXEngqQA_6IZsyDU0_4JpbDYLExu3iwkEWiPaFFrGugH7GvPPVC1kafiQ4XWTtfj0wlmbnmoYJ8Fnz0UIVRR_DguF7exILyRlfNi5u2kca656WlFQEi6MBkvIV4MTXMNa0jtGkwsw_MR2XkpU375oY0fYP3HMpkvhEW9j6F-J7dW3LLAbeBk7q31yJKmMthsBO_uLhPwvZgK8_wM9dQoDwSXet_Q-Gn3x-VidMDokMysoyt7TPmNUPpYuRdhed4htLqNw7xP4sFSU2vqwsPVfBKO6rDNg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dddd337574.mp4?token=IwC_qqZALDbXZK-piKZA7-ihDV4rovCtaSHN_fE-MSgRyjT6ihsNNuqYKJXEngqQA_6IZsyDU0_4JpbDYLExu3iwkEWiPaFFrGugH7GvPPVC1kafiQ4XWTtfj0wlmbnmoYJ8Fnz0UIVRR_DguF7exILyRlfNi5u2kca656WlFQEi6MBkvIV4MTXMNa0jtGkwsw_MR2XkpU375oY0fYP3HMpkvhEW9j6F-J7dW3LLAbeBk7q31yJKmMthsBO_uLhPwvZgK8_wM9dQoDwSXet_Q-Gn3x-VidMDokMysoyt7TPmNUPpYuRdhed4htLqNw7xP4sFSU2vqwsPVfBKO6rDNg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جاوید شاه
👑
🫡
@News_Hut</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/67979" target="_blank">📅 10:15 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67978">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a5afa19317.mp4?token=ZfRqTxktr8AKFpOVZzg1q7oKtY-GwQeD6wmH803Qb1Gx4V1_CGT217L73EWnvRHSmQ3nvcdVO-IlJfKcOcK8QNvvcDC7xkbT3aASavT1KFIdXjz2GQqPY0noSlCt0FAPWdF_5zfVtWiKe7wPnIqVjqUGDYVYvV-AVCjPClosjETyOzCBy2nS2q-zdzfdnRilkizVn5c2zhCMoKBPABMGysemnKJ-HbU1VDWxunJS4GXD5F1qY3_pMk7oyxGinYD3WamNohLncrnRgLFn62i4bnT5X-NjaDMAzzIvUxfbZcSstq5GrAP5piF1JvaQ4VWtIjeshnclvyu882PrWYP_Hg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a5afa19317.mp4?token=ZfRqTxktr8AKFpOVZzg1q7oKtY-GwQeD6wmH803Qb1Gx4V1_CGT217L73EWnvRHSmQ3nvcdVO-IlJfKcOcK8QNvvcDC7xkbT3aASavT1KFIdXjz2GQqPY0noSlCt0FAPWdF_5zfVtWiKe7wPnIqVjqUGDYVYvV-AVCjPClosjETyOzCBy2nS2q-zdzfdnRilkizVn5c2zhCMoKBPABMGysemnKJ-HbU1VDWxunJS4GXD5F1qY3_pMk7oyxGinYD3WamNohLncrnRgLFn62i4bnT5X-NjaDMAzzIvUxfbZcSstq5GrAP5piF1JvaQ4VWtIjeshnclvyu882PrWYP_Hg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دستتو اینجوری کن
🫴🏻
لباتو لوله
😢
@News_Hut</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/67978" target="_blank">📅 09:33 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67977">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/14b2083eb1.mp4?token=E6r9iERejzQZSmx1DOHqnFcDLe7j2tyWBYsbv54amW2x6io5Dn_AQNrxASn5t-5qPVA1TDb7AyS31SIPO6ai5zecFC3hwo1wWe7NqW5YlJZ1tqJ-lDVPUHkiHzUIvpdaScv5FhvOX-vgi-fPHMJTdM3eRmxRjRz9wiS0gUJZmB5qIti2tOabGTmaNmKGL3S6Y5BWeCNlm7GIP8eAh6j7g-lod8VRDMkw35ALIjqLSWHPX9zLxk2uGTurl2qKH0YOAaDo7hoA7OIdxNCQv37omesNcHBCf9H6iUxSJxcI8OY21BcHZnt8PlJqhruZ88qGiNnAulBxstzpLoRdPCTGvw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/14b2083eb1.mp4?token=E6r9iERejzQZSmx1DOHqnFcDLe7j2tyWBYsbv54amW2x6io5Dn_AQNrxASn5t-5qPVA1TDb7AyS31SIPO6ai5zecFC3hwo1wWe7NqW5YlJZ1tqJ-lDVPUHkiHzUIvpdaScv5FhvOX-vgi-fPHMJTdM3eRmxRjRz9wiS0gUJZmB5qIti2tOabGTmaNmKGL3S6Y5BWeCNlm7GIP8eAh6j7g-lod8VRDMkw35ALIjqLSWHPX9zLxk2uGTurl2qKH0YOAaDo7hoA7OIdxNCQv37omesNcHBCf9H6iUxSJxcI8OY21BcHZnt8PlJqhruZ88qGiNnAulBxstzpLoRdPCTGvw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
پهپادهای شاهد سپاه درحال حرکت به سوی پایگاه‌های آمریکایی در حوزه خلیج‌فارس
@News_Hut</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/news_hut/67977" target="_blank">📅 08:50 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67976">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🚨
🚨
⭕️
گزارش‌ها از آغاز موج جدید حملات سپاه به پایگاه‌های آمریکایی در کشورهای عربی  @News_Hut</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/67976" target="_blank">📅 08:48 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67975">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🚨
🚨
⭕️
گزارش‌ها از آغاز موج جدید حملات سپاه به پایگاه‌های آمریکایی در کشورهای عربی
@News_Hut</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/news_hut/67975" target="_blank">📅 08:46 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67974">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">app (7).apk</div>
  <div class="tg-doc-extra">53.1 MB</div>
</div>
<a href="https://t.me/news_hut/67974" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">👌🏼
تنها
#سایت
با بونوس های واقعی
😮
به ازای هر 1,000,000 تومان واریز بهتون 1,200,000 تومان شارژ میده
💰
✅
نصب اپلیکیشن بدون فیلتر
🚫</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/news_hut/67974" target="_blank">📅 03:03 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67973">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IEIKVvR2clldp5Zw-xpY5S7ULzN9kYgZAe2307rjIA2k1nsu_8WCFZ3se-Vv9-_XGMlgDTN1C_t3ychNV14Yf3gwus1G4cZ0W50zLgsgVHPF1YZD5_KNfKNWXznKRP26WGMaHPdsYOp6F_HnzxYnpzV2W-pbfxmN9P557a2TzpKcJZQ-luPKwUlnDjzCqHxeuLL3d_CZM6OaceHGUPwFrfKXfhu1faUVQjAPTopoST7E-WkL3MYyDREKKNfB-QwofcS85Y8909ZI-p7QisonUoI7Nzzk71XjBbIK6f_DKV11RrWJN6PVhaDfXNkd-T-WLaP-44GsN2E5R6S2AC41Qw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
هر
1,000,000
شارژ مساوی با 1,200,000 شارژ در سایت بدون قیدو شرط
💖
💵
هر بار حسابتو شارژ کنی
0️⃣
2️⃣
🅰️
شارژ اضافی میگیری بدون محدودیت
🔴
اگر هم باخت بدی همون لحظه
0️⃣
2️⃣
درصد  مبلغ باخت به حسابت برمیگرده.
⌛
همه بونوس ها بی قیدوشرطن:
🌐
betinja.bet
🌐
betinja.bet
کانال بونوس های رایگان
a22
@betinjabet</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/news_hut/67973" target="_blank">📅 03:03 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67972">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1a1a4493a9.mov?token=VtZ-B3zgxpA8lgbOo7rD0oGbreBEOxryTvIS0MFiibEeiOGsienWSXuWAFeImVGoPU7FoOmdDviMCqEHV7ZKbz1Un3VavNzkG7OftmIilVnaCVC982IRPfzzuVFzWxfpIlUmF9R-a_XFn_zrKxHfBIUkQ-BJzG_4MIqJKlVzevEEL2ePhCqxkUM6O3k9t0goj62FwKbh4KK7JUQsXaxbeweJ8kvLBlNlCWCiQfpOYVntkxEi6TSDAQVAbJ2g-3t5j1eXHOuIVN7b5qBpcW00xg9eYLOTKA-TiFlDWJr_xSJUibAyGw7f7AhueMstn0Xv0bVfGYB-GZVvow4-_DhEkg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1a1a4493a9.mov?token=VtZ-B3zgxpA8lgbOo7rD0oGbreBEOxryTvIS0MFiibEeiOGsienWSXuWAFeImVGoPU7FoOmdDviMCqEHV7ZKbz1Un3VavNzkG7OftmIilVnaCVC982IRPfzzuVFzWxfpIlUmF9R-a_XFn_zrKxHfBIUkQ-BJzG_4MIqJKlVzevEEL2ePhCqxkUM6O3k9t0goj62FwKbh4KK7JUQsXaxbeweJ8kvLBlNlCWCiQfpOYVntkxEi6TSDAQVAbJ2g-3t5j1eXHOuIVN7b5qBpcW00xg9eYLOTKA-TiFlDWJr_xSJUibAyGw7f7AhueMstn0Xv0bVfGYB-GZVvow4-_DhEkg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
ویدیو منتسب به اهواز بعد از حملات ارتش آمریکا
@News_Hut</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/news_hut/67972" target="_blank">📅 02:59 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67971">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🔴
نیویورک تایمز:
مقام آمریکایی گفت که انتظار دارد موج بزرگ‌تری از حملات آمریکا علیه اهداف نظامی ایران در یکشنبه شب (به‌وقت آمریکا) نسبت به حملات اوایل همان روز رخ دهد.
@News_Hut</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/news_hut/67971" target="_blank">📅 02:53 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67970">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🔴
فارس:
دقایقی پیش چهار نقطه در شهرستان‌های امیدیه و ماهشهر مورد اصابت پرتابه‌های دشمن قرار گرفت.
@News_Hut</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/news_hut/67970" target="_blank">📅 02:36 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67969">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🚨
دزفول رو چندین بار سنگین زدن
@News_Hut</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/news_hut/67969" target="_blank">📅 02:21 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67968">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">🚨
چندین انفجار شدید در قشم
@News_Hut</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/news_hut/67968" target="_blank">📅 02:13 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67967">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c88de9c653.mp4?token=e6VMDo3tV5cOSnrUBtaCtACl2UfhyKMBS1G3ZPnBPDiET0p51KtdaVlqjw4X8qE3a3z-BUVduRFLXKUhJymnkkSeaeCApTlA1SqlMxg6cqA2DJg0q5heysXdjK9cEDHYx9cP32gpCb3At_BGukaosHmh39CukzEqDwM2yaRVR8xbEzsQYPMMJxG74tyQNvCkFhJOaxrve9JXgx2nn71HzQyloC_xvKGqqScCb9ueh29lH_UGBCxJg-SHVgF1bp58TRDK4ezoQRd9a84w89Dza7433Xw4KDrUvsmpYy6lVnCB5EOCEx0o1JC5fQgChy-rvDoCcWiXEWQ4Tj0iQAtBzw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c88de9c653.mp4?token=e6VMDo3tV5cOSnrUBtaCtACl2UfhyKMBS1G3ZPnBPDiET0p51KtdaVlqjw4X8qE3a3z-BUVduRFLXKUhJymnkkSeaeCApTlA1SqlMxg6cqA2DJg0q5heysXdjK9cEDHYx9cP32gpCb3At_BGukaosHmh39CukzEqDwM2yaRVR8xbEzsQYPMMJxG74tyQNvCkFhJOaxrve9JXgx2nn71HzQyloC_xvKGqqScCb9ueh29lH_UGBCxJg-SHVgF1bp58TRDK4ezoQRd9a84w89Dza7433Xw4KDrUvsmpYy6lVnCB5EOCEx0o1JC5fQgChy-rvDoCcWiXEWQ4Tj0iQAtBzw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
فعال شدن پدافند در کرمانشاه
@News_Hut</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/news_hut/67967" target="_blank">📅 02:12 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67966">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f56a15f1b4.mp4?token=rVTPSDrLmnic_g6DktW_Rk8ii3mZArI06aNGM8Tn2Ot-PQCGj7151s1313lJnu0X0yKazltGLlC-lenO038dG6QHYFCSmo-dAlUYhKtAs4oa_IGldAJLdNrwpU80vUyWCaTb9g6u-5q6ZcL9ivByNpcpU0zgzYMdIHNHxEMOeVYJQRmIQ_0tuW2itwM0X9Nq5n0prk192B6p9pul6axs2-93wIc1QjgFf5FPy-ohDfhNYtuVA7jOh6NXXkjE26p05HJobE6nKEeFghsTgZDbrjv8PtcD2mJG0EVTg5Dit7cZ5A1gZC7X5i5uFMA0L-L-WR21eeYVCCGeUqjfQbOYFA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f56a15f1b4.mp4?token=rVTPSDrLmnic_g6DktW_Rk8ii3mZArI06aNGM8Tn2Ot-PQCGj7151s1313lJnu0X0yKazltGLlC-lenO038dG6QHYFCSmo-dAlUYhKtAs4oa_IGldAJLdNrwpU80vUyWCaTb9g6u-5q6ZcL9ivByNpcpU0zgzYMdIHNHxEMOeVYJQRmIQ_0tuW2itwM0X9Nq5n0prk192B6p9pul6axs2-93wIc1QjgFf5FPy-ohDfhNYtuVA7jOh6NXXkjE26p05HJobE6nKEeFghsTgZDbrjv8PtcD2mJG0EVTg5Dit7cZ5A1gZC7X5i5uFMA0L-L-WR21eeYVCCGeUqjfQbOYFA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
تصاویری که ظاهراً پرتاب ATACMS با استفاده از HIMARS در کویت به سمت ایران را نشان می دهد.
@News_Hut</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/67966" target="_blank">📅 02:07 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67965">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🔴
حیاتی معاون استاندار خوزستان:
در ساعت یک و ۴۰ دقیقه بامداد امروز دوشنبه ۲۲ تیرماه نقاطی در شهرستان های بهبهان و دزفول مورد اصابت پرتابه های دشمن آمریکایی قرار گرفت.
@News_Hut</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/67965" target="_blank">📅 02:02 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67964">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🚨
🚨
مسئولی در استان خوزستان ایران:
دو نقطه در اطراف شهر اهواز مورد حمله با موشک‌هایی قرار گرفت که توسط دشمن آمریکایی شلیک شده بود.
@News_Hut</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/67964" target="_blank">📅 01:58 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67963">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">🔴
مهر:
معاون استاندار مرکزی در گفتگو با مهر حمله دشمن به مناطقی خارج از شهر خنداب را تایید کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/67963" target="_blank">📅 01:56 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67962">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/234339e6d8.mp4?token=Jk9ERvCHzg-af-MI7Nqhu72fDIIsGKDFtecAI4JqbGPTVfMyWZRPsXD2hxfuOqEKBhCMomZVfYem9gonyepvaU2HsWxqqfidOVfCvdicB3w7PpV7Zc8uGn-yGPBFp8agnlvREBZ6Tfa4ZupRnO8A0QWQAbttJ6fPAx3LbslxUrVkOu_OO9JPuNjBYBBmig-l3qmgBT6ej27EE6jPXVdqSE-vB0x3TV1dyBj_qRdluOd1hOA6KtlTp5GENjP-Zu4ZE0gS9qsEtepR5P_q0zogiMHDYGNLRikIMZBNNrQ148vN4qbdIEyIhgM-VtiLXjqGK35ihvIriJODvwFJnpzHTw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/234339e6d8.mp4?token=Jk9ERvCHzg-af-MI7Nqhu72fDIIsGKDFtecAI4JqbGPTVfMyWZRPsXD2hxfuOqEKBhCMomZVfYem9gonyepvaU2HsWxqqfidOVfCvdicB3w7PpV7Zc8uGn-yGPBFp8agnlvREBZ6Tfa4ZupRnO8A0QWQAbttJ6fPAx3LbslxUrVkOu_OO9JPuNjBYBBmig-l3qmgBT6ej27EE6jPXVdqSE-vB0x3TV1dyBj_qRdluOd1hOA6KtlTp5GENjP-Zu4ZE0gS9qsEtepR5P_q0zogiMHDYGNLRikIMZBNNrQ148vN4qbdIEyIhgM-VtiLXjqGK35ihvIriJODvwFJnpzHTw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
لحظه انفجار در اهواز
@News_Hut</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/67962" target="_blank">📅 01:53 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67961">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c4d6d7e5a4.mp4?token=Tw8Fp49mJbXrAx0yneZP3utzvXPrYsYEQfhmZ2HuYicWX54BVCbuOyqHkwNFHn1d5uaTeTnnwxdTHogA_a9phOikoV8tNknMFL7q1K7FtSXKaFPBSWMqdryIXELaDALiYBGXAa2GpjUu3yCoUgm4VgDN4YxROTw5RpCf8p45ltEIYfATebetRYaPbEKBhlnu2eK6pTIeh6ITE8mEIJzKwlke0JY8H7S7UAU9JVIfyJ7Y-XAXgX0mNX6O8CBA6I2jAEfUTfywbNndbwSJMgN61MChVerKlj4DK__WAnkII7j3TObCSvBIfsIW02MrwqDNej-Pe-qKWn3OyPpbLvQ9Gw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c4d6d7e5a4.mp4?token=Tw8Fp49mJbXrAx0yneZP3utzvXPrYsYEQfhmZ2HuYicWX54BVCbuOyqHkwNFHn1d5uaTeTnnwxdTHogA_a9phOikoV8tNknMFL7q1K7FtSXKaFPBSWMqdryIXELaDALiYBGXAa2GpjUu3yCoUgm4VgDN4YxROTw5RpCf8p45ltEIYfATebetRYaPbEKBhlnu2eK6pTIeh6ITE8mEIJzKwlke0JY8H7S7UAU9JVIfyJ7Y-XAXgX0mNX6O8CBA6I2jAEfUTfywbNndbwSJMgN61MChVerKlj4DK__WAnkII7j3TObCSvBIfsIW02MrwqDNej-Pe-qKWn3OyPpbLvQ9Gw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
منبع عراقی:
موشک‌های آمریکایی از کویت پرتاب شده و وارد فضای عراق می‌شوند، به سمت ایران.
@News_Hut</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/67961" target="_blank">📅 01:45 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67960">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qwAovJINdmdxiejZTKofXcoEvoECMXwBkiw0qJ4z-hAlOuUylPSYkkkMAIMJ0EIQYcbs2dsinUvqeUS658hfgS4YgtLwRT8pY9Ow2U4id4J1Ewdzo6xUkjrIl6kX8dqp1CYPi4p0y8jFDdfYlTspXHzn2FhZSRLsqY-3B4FGiXgaBwurh-xMQND6QanK8UN9ZiCtoZiluE6Tj-mNgBAtVzBBINcdwtx_XhNm2iJV7ZF2k2Ti2yVZ3nwSmxUfP9qsYJFt5whZt_E3ZbkGIPFn89In-efAk9-LxNeXjD1RedEkT2QLA5vY7wObuUmR9j8BqLRLs0I2Yb6d-X3UWpaaLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
باراک راوید:
ناخدا دوم تیم هاوکینز، سخنگوی سنت‌کام، به من می‌گوید: «در یک ساعت گذشته، نیروهای سپاه پاسداران به سوی شناورهای تجاری در حال عبور از تنگه هرمز شلیک کردند. هواپیماهای آمریکایی تاکنون موفق شده‌اند یک موشک کروز و یک پهپاد تهاجمی انتحاری ایرانی را رهگیری کنند.»
@News_Hut</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/67960" target="_blank">📅 01:41 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67959">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">❌
اهواز رو دارن شدید میزنن
@News_Hut</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/67959" target="_blank">📅 01:36 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67958">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">🚨
گزارش های از وقوع چندین انفجار در اهواز
@News_Hut</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/67958" target="_blank">📅 01:33 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67956">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DbSVPaF-dofIzdDgJmTpqwX5kj8sWHokFk6xT72yQyHtNBpRGdpy3Zc1EWv-YhEFiRr5mKn45UZZvzJt0NdI22rUyhwqh3rdQGDPupAdTswtPKMfCCf8f3SlnYGucM_Hj5MK_2-Rf9Cn2ggWEvI8sHfRaKuRxx1cavD-PUO_zCjd_lGsq1gq1py82KNdrkDK4erYO-rpHQfDHVgcc_8kGiHLGyuXK8nJHzLbdT0lOeSpazHmFOiJJr6WKoLcjGzxeL_vg85_IAoYeLDv7IZmgXHkuDFUZa9Eo09SOBP844kZaaQzIDaYODHP3ppl7GKM1JoGgYLCyncKl0gQJcFiSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5306540b7f.mp4?token=lEEuzTaf8d6bnYA-FsPnTlXmIg52S0FNgvzlEiRZdMYllF0gXDIFVq8g1_NUMlydV2xcjzNCp6MvLRW7FZQNFneYVyxVp7AgzJHkzhvUfCCVRaHBMXgB1DwQ8yrN-brl8lm03_n7PovckwH2mCUWBBi2cuWecEt4RXdspsITMNf7Q0tEtws62-e3RA0xOAEUHXfXqNklmWB4GRmAbWrSgnBkhGSubcjRZFWuybWuaLwAcg7yalrPhHzWR07tm1RW-B7T915beWDokOFw8L_rhs4y0rz-55PjuCl_22Mrsa0YdJuXhk9auwmqcqkvd0qBvq8n5PV48aXyRR-92I_5Sw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5306540b7f.mp4?token=lEEuzTaf8d6bnYA-FsPnTlXmIg52S0FNgvzlEiRZdMYllF0gXDIFVq8g1_NUMlydV2xcjzNCp6MvLRW7FZQNFneYVyxVp7AgzJHkzhvUfCCVRaHBMXgB1DwQ8yrN-brl8lm03_n7PovckwH2mCUWBBi2cuWecEt4RXdspsITMNf7Q0tEtws62-e3RA0xOAEUHXfXqNklmWB4GRmAbWrSgnBkhGSubcjRZFWuybWuaLwAcg7yalrPhHzWR07tm1RW-B7T915beWDokOFw8L_rhs4y0rz-55PjuCl_22Mrsa0YdJuXhk9auwmqcqkvd0qBvq8n5PV48aXyRR-92I_5Sw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
تصاویر مربوط به بندرعباس
@News_Hut</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/67956" target="_blank">📅 01:24 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67955">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBeHrAd🇦🇷</strong></div>
<div class="tg-text">توالت + دکل = برنامه طوفانی پیتِ پرس زن</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/67955" target="_blank">📅 01:22 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67954">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🚨
🚨
دکل مخابراتی سیریک که هفته ای یه بار مورد حمله آمریکا قرار میگیره :  @News_Hut</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/67954" target="_blank">📅 01:21 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67953">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🚨
گزارش ها از انفجار در چابهار
@News_Hut</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/67953" target="_blank">📅 01:14 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67952">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/epitolfx0mxN7h_ya1W53vdXWkOvoQrl3bUr5l3SBgNjYnm5V4_mo6lGn51kYZVSIv8eovHJHYtfCAXumF8-cyxQ9k58DpE5VJ3weFs5wDEoX1QYI8d4aVwqf_WURISYo24P4ka6_bfQdQRPahn5nvKpky50AVA7CKEaQGlwHdnI0_9ij1koJvT4qo_vB_SC30RVw22WqG19XuJ5brdvONcTH-cb1EJVPtMDdKdiRIkvO0Bhj8pG0twiLg1HPW4agPGGAxHKcVyg6U2UDS321uIkxQPKESRjE2GTxFn822gl_YnxNfU8wPwsWAgvt4j8i5x7S5S7ugfW3L04o6kodA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
9 سوخت‌رسان آمریکا در حال حاضر در حال پرواز در آسمان خلیج فارس هستند
@News_Hut</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/news_hut/67952" target="_blank">📅 01:09 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67951">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HfQLGipuWLAUwSscOpSPg1Glerai7lA_cmXor3RbJvRYbEsZ7XJ2cBYfUSHUFIFDgAn6c5vAHDlmy6_ifrd6DTMALfo-tDjAgUFs8sVNh_xZAvtbDeF8gu4pkc2BUTOfbeYb8BO8MWT5DxTirFPhs1Q0DRp7guAVOI_qHq4kL2eoAi8t9XGYa8f9TT6E7L6y2-2vCANJoJ2xKIvafRTR_XAlr59I4KoYQUeiPRtajNiiPKFddEqGVnVAbpGDV8qdXDlT5XJD43fWEEpFtJLE-P1N3nyRe1ioK4cxQRK6i7L1FEey4SnJReICN_ZeOMbElBIZX8ltxhIfJH7novk2RA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
تصویر منتسب به انفجار در سیریک
@News_Hut</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/67951" target="_blank">📅 01:05 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67950">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UwfS4yJgeJ3o2mrSJX2hhtSmcqWuLy79LJQdNZkvR69eIYBUknILA8oanJPQo6Q6ISo0nQODjtqcGXobK48LUB_-Nc64lonhBfpQ4lyaWEpDWD5TeH_KWs3FXjajhytHxuCs9C8BSZIKbXm2VAnBeqHokuifuC4p2CIqA98CMOXLFtWcVIEWxUjxCDJ82qmuXGiOjUuwztcWr4oJ-7xcwRq8OohL6PUEIYUY_K8q9kn0A4UbbxH1UvQe68k__gzmkEZ19c9iLq4Ni6hT7rbh3No1cWAzZs3Gp9Pae-u97zVFm6rMRutDKu8oKXrbZgb6ahAHtVG59Gv6fu_ZF5L3-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بنظر من زود تموم می‌شه، چون:  صرفا حملات جنوب کشور هستند دلیل حمله هم حملات سپاه به کشتی هاست و این یه حمله ی انتقامیه، مثل چیزایی که دیده بودیم قبلا   یعنی در واقع حملات، کنشی نیستند و واکنشی‌اند  #hjAly‌ @News_Hut</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/67950" target="_blank">📅 00:59 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67949">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🚨
❌
دو انفجار شدید در جاسک
@News_Hut</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/67949" target="_blank">📅 00:56 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67948">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🚨
🚨
انفجار در بوشهر
@News_Hut</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/67948" target="_blank">📅 00:51 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67947">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aeeiJQC6cs210mDhT17aa_qziFXaOB5avL1rpSfCnE3ey8onEQnKmB7nGPzg72EGAOPhFrxVVScb4FR7IJ03LVfyINAFB8nlzl7nFNG0dJHoxZ-5-cxpa5syz8zEvMWv5USVKgwcuqWbWtyXlPVTu5zlMWqflpJbhcmTNBJgJgEUTMwtVUo4pW690jazYPQRUb9TCn11enjr_RTox92zAgyEmu7L08fXw0ZIA11UuyzVleH2Gl3dFMJGA_IDezh_i4SOVv3l48Fuh9rQyBeINeJo3AkElxqai5ujAaR4ddekQEOa_z_JI5C_zM9xHMIdSvOeXfvHTpUDamW8FVFCFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
فرماندهی مرکزی ایالات متحده:
ساعت 5 بعد از ظهر امروز، نیروهای فرماندهی مرکزی ایالات متحده حملات بیشتری را علیه ایران آغاز کردند تا به توانایی خود در حمله به کشتی‌های دریایی غیرنظامی و کشتی‌های تجاری که آزادانه از تنگه هرمز عبور می‌کنند، ادامه دهند.
فرمانده کل قوا دستور داده است تا به نیروهای ایرانی پاسخگو باشند.
@News_Hut</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/67947" target="_blank">📅 00:50 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67946">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Czy3L1MIFdUcuyBHw_FcTJIWZLmdhkh13zXAWt5KILrWwdaCdslBxOYvyYsqd57db-f899qlil8Xx5rdl2hQVky4Q7owe8T2Pz4IiD9k7s-iZ9TBhARZ_xz6msCDzVzPwzYCHOQ0Fmkyv1x_Kx8MwG3Fdkvm2G5TSzgRtBw3lSWW6jVq_iYGO72oxLkxd4T6OIVFkewonAcEl8f_DoPqnKlNLT1nsMUVlhYHYJH1A1WUxSuQrSsQ-K3isaWFPl3cBttppljm2k3BUm9xQ0Dw8T79r98vKVxOJFXPzx8IcjN8YYoYU7BoPZNV42nYOpG9224WefFyoC4wa3CaqwgPOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Ah Shit Here We Go Again
😂
#hjAly‌</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/67946" target="_blank">📅 00:47 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67945">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🚨
🇮🇷
ممد سامتینگ:
اگه نمیتونی جنوب لبنان رو امن کنی،
پس جنوب ایران رو ناامن کن.
@News_Hut</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/67945" target="_blank">📅 00:47 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67944">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">Ah Shit Here We Go Again
😂
#hjAly‌</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/67944" target="_blank">📅 00:45 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67943">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🚨
🚨
❌
گزارش های اولیه از انفجار در بندر کنگان
@News_Hut</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/67943" target="_blank">📅 00:43 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67942">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🚨
بندرعباس رو شدید دارن میزنن
@News_Hut</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/67942" target="_blank">📅 00:43 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67941">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🚨
🚨
🇺🇸
رسما حملات ارتش آمریکا به خط ساحلی جنوب کشور آغاز شد
@News_Hut</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/news_hut/67941" target="_blank">📅 00:41 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67940">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🚨
🚨
پنج انفجار در قشم
@News_Hut</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/67940" target="_blank">📅 00:41 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67939">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">🚨
❌
سه انفجار شدید در بندرعباس
@News_Hut</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/67939" target="_blank">📅 00:40 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67938">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🚨
🚨
صدای چندین انفجار شدید در سیریک شنیده شده
@News_Hut</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/67938" target="_blank">📅 00:37 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67937">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🚨
🚨
🚨
خب مثل اینکه شروع شد
@News_Hut</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/news_hut/67937" target="_blank">📅 00:36 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67936">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cce49929e0.mp4?token=AlOLfOnRRvtviT5DYD1p2GEA-XvhXAlVIWvKkInHyHKXl-2IjYFcrlt2H8_AKaPeUWvnuTTkFp1SAhpwx1u26YpqsaWBHUnadWLFmnzMXQVx9-X45yesxEYwjCgH4t_XsJziCMjLpgg7RGWny9s7Fr0AnFLStdK4eRedJmqLhYQJKvv1SBzqC9C2zNAmzpML1lJjlC1xyqXH3IAHITAq3DQ5rU7rZbbS53G_WBXew5W9fR730wyxblM93d7UZruKmY-4yZ2I3SjYHW3PTYKFfoV2C41kWxDXvSciu9vDd8C2hIqZqBvZW2aWeWI2xUYAnCBSHv01kevQwmbMHsjCLA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cce49929e0.mp4?token=AlOLfOnRRvtviT5DYD1p2GEA-XvhXAlVIWvKkInHyHKXl-2IjYFcrlt2H8_AKaPeUWvnuTTkFp1SAhpwx1u26YpqsaWBHUnadWLFmnzMXQVx9-X45yesxEYwjCgH4t_XsJziCMjLpgg7RGWny9s7Fr0AnFLStdK4eRedJmqLhYQJKvv1SBzqC9C2zNAmzpML1lJjlC1xyqXH3IAHITAq3DQ5rU7rZbbS53G_WBXew5W9fR730wyxblM93d7UZruKmY-4yZ2I3SjYHW3PTYKFfoV2C41kWxDXvSciu9vDd8C2hIqZqBvZW2aWeWI2xUYAnCBSHv01kevQwmbMHsjCLA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">#Rip
🫡
🖤
@News_Hut</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/news_hut/67936" target="_blank">📅 00:28 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67935">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZlSJU4d0pZnZ5lsb5peAxt-pAWCJu8sSW3pY0SsTxHVAUVRiVg0PGD0_dV05IRVClVZov7PR6vOYCzS_df4PWmZr1aWBod7XYsO9mCZusdVJZYaHwpL-peHD47pKr8Yw95vGEUUrCK5QnywOQ-pdaLULt29P_ZmYfxcfq2o3Zj6u1ec9loLJrvsscZIN28BzA19oBTaoR7SjVr3YJsm6JOOryZWDhIGiWUDBTbE7b-mZMc1l65vGkORQt09kutdvnxgTsVGEGmV7lm3PYv7QtDfJyLoDAYcWuNbkQEqQNMsbnv0Jio9FcH9vAW1hExA2ajn6d63ZPvMZ6TBg6LI44g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
فرماندهی مرکزی ایالات متحده:
❌
ادعا: دستگاه تبلیغاتی ایران امروز مدعی شد که سه تن از نیروهای نظامی آمریکا در کویت بر اثر حملات ایران کشته شده‌اند. این ادعا نادرست است.
✔️
واقعیت: هیچ‌گونه گزارشی مبنی بر کشته یا زخمی شدن نیروهای نظامی آمریکا در منطقه وجود ندارد و وضعیت تمامی پرسنل مشخص و ایمن است.
@News_Hut</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/67935" target="_blank">📅 00:14 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67934">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e96a5b8a48.mp4?token=ugOST3mQmRYPnKmwJmxXMAa1ZHEQgbPjlOhLoekPLoYc6kAP5kT-hlDq9jMkf6B4HIv_c4QyE-rlvzJiZbokORUuXsUag6XT-LNTTERCNYfb-astrDlQWveqBCAwS_C0DpMaiUTxIW1ZxffbbQNovQRKvrAgCr6SY04Thm_4DXKh07sCwP6D1lZOkAogp_ccYt8LjSDlvnc_n6brwCKNwCQmoHCQg6sJWfxy4SWFYAQBhpLExI_qn_qVKwycJJPzZhR_Vc31IASWYZnXL2nObngrHocRjSjbBq-aLSt8ULX6zRBMTepV7q4-oo3aj0q_LjgjI9eGL7sjE40VBC3dvQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e96a5b8a48.mp4?token=ugOST3mQmRYPnKmwJmxXMAa1ZHEQgbPjlOhLoekPLoYc6kAP5kT-hlDq9jMkf6B4HIv_c4QyE-rlvzJiZbokORUuXsUag6XT-LNTTERCNYfb-astrDlQWveqBCAwS_C0DpMaiUTxIW1ZxffbbQNovQRKvrAgCr6SY04Thm_4DXKh07sCwP6D1lZOkAogp_ccYt8LjSDlvnc_n6brwCKNwCQmoHCQg6sJWfxy4SWFYAQBhpLExI_qn_qVKwycJJPzZhR_Vc31IASWYZnXL2nObngrHocRjSjbBq-aLSt8ULX6zRBMTepV7q4-oo3aj0q_LjgjI9eGL7sjE40VBC3dvQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
‼️
سخنان قدیمی زنده‌یاد مانوک خدابخشیان در مورد لیندزی گراهام:
گراهام کسیه که به کنفرانس های محرمانه بیلدربرگ می‌ره
کسی که می‌ره چنین کنفرانسی یعنی از پشت پرده باخبره ولی اجازه نداره چیزی بگه
بخاطر همین لیندزی با هشتگ Make Iran Great Again می‌خواد به مردم ایران نشونه بفرسته
@News_Hut</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/67934" target="_blank">📅 00:02 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67933">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I-hwL0LmTeBhAYPsrao6IsKPruFhO14LD3ON7bADvE37wh2rWfNr0bCokbo9RCCvEdc8p9G1UcBOFavPCJSTxSsE73-4AvNsDQfd-bHVWDo4Iw1TJu4MqpX1TvNNQ5BpF5UOBQ_xYLsaC3Xh8s4YvyOR73O7ljrl0QbBWkoP_s9uriUXF9gRMrCJApm9mKYgqZAoAdes4BaWjqROCfnFWVRqMX7-3O38sjLHgNJJQl2dCnnuH6f0HX3pWkhQaS1XFliTsNTMcmQLquzgiMGDJpTuXsuwWW9PYznp02ZtEfEPaDqz-JFRZVn2hdypePzOoFMV3seNlUrGJYunqYsNdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
پست جدید ترامپ در تروث سوشال   @News_Hut</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/67933" target="_blank">📅 23:46 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67931">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/W7X--_f6mL08LJlTj3Lt3bVID9cTVQ1-pr-Mcp7wvy2AoUlQVhrP40ktUkUhZw8fWSLulEN05Vw-84RJBnBy75Euxj4T9HEx-7i4Jdpc5X3qc_JHOU2NStD2w2knAkp-inzTpwraMpOwcrn5_NhmrTfc-5zWin2VIsLZJufJDnwPrrR_2lukrJqDvq2TIwxRAfCeUsAXIDbkiQzH1b4mqLsFewYJlNFNhCSD7L6OYCGN95W4DcpFERcdz8NpBUClDQ4Mw0L7M2g-Pyis2N1l-WFF7SdmR8VN19CjBjylwJmaFifJo6ELMfb39hy_udtriw8NByRvZK1QlO-_8qaT2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dZ2duSdQhJL6XwzdzO4fJKZfFdWuAMEzpvY41MI97JKpkyPWpJB1RD3xA36RkNVIuH4B8MtI2FW3N7g9TXrGaW0NRbsLqCUG7Wf7lSW5eFX709rAaZprscThNL6EQI4PXdRo34UApIlfMM6zhmJvRZ3xfcqAjJmmfNvgCuvR4EbqcXrA80_JAsigpfDlAAsa61GaxMV2Y4T2_hXHB0dxLWQHjhtYLYxHCI1Bx6hfF0lu_1UxAiwwJ0ok9yRjE0NaJn5-T2Qghp0Qln-w58FaEz92TFanfsDJ_8CDE65m23jliA5BSnzWhi-55ZC8v4DCFpX_1YnUNJTcPCE_Lk1BTg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
پست جدید ترامپ در تروث سوشال
@News_Hut</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/news_hut/67931" target="_blank">📅 23:42 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67929">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BGJMU12eJy2SBC8njMyqwUJZ2r6NSF2dq3uIkQt5iSmW6vCIt60FdB8Jd_mFYcr7fXDKzRlzxqrvKNeKIQeDVOAaYWQQgL46Cjqo_sQx4P1JI86k9TVt4oc8etGHCRNtmrQrJHOjXNHrp3sL7lsGYEteyeKTaETvYfh82mUr64_ORnq-G5cYKMKB_8QCnolVIkeNqkztLvtoLiu29qAa4FVx1vlomTg9o8fBXvrBH-H_NZS_G8wSEeuk12eDCnY_vyEIQGCZg-qS6706nbSbrTdUZlEx-F0T_hhf-r2CQc7r8A9iUM4EuYipSjFo3-VkNrmk8GgSozOzHQByQiAogA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tOxPF3ga8D87enqL-m5AgGVa9ie4OZNlFjIoSl84HuJ_WcCU3UY-3e2WX4zZLl5o3FOaNu2M0L99aUjE66nT7DiG36DzrebjxYcDeYAXRwSR-uIbXoH-bJH6m8wzSqjTcMNP_mHzYih0p9DNPF9A1qOs3mjE9O1C6bEYXE7fxOhN1b-Ta1fl3zfVWqq6fihb9WA20K9-yGmv4Q1rqf7UaSplN9EHko4vnScvmX5LNup_8S7HsplgGQs5O-NwTaNFnGYSVMxZoCHqApvfp7z2Mp0wU21ASp51FSrMvnONkqCU9e5vTw-ZdNfg1yk929NaYgPLhAeLEcS0uG-McdDIAg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🇺🇸
🇮🇷
🇷🇺
لومر، خبرنگار جمهوری‌خواه: ممکنه ایران و روسیه لیندزی گراهام رو کشته باشند، باید تحقیقات صورت بگیره
همچنین FBI هم وارد تحقیقات شده
@News_Hut</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/news_hut/67929" target="_blank">📅 23:35 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67928">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/e7a73bd81e.mp4?token=PTFjHdoZM6PdwztZz1sPx6LsE29P9cARlZ8tup0E7OwY_wBgz007lvLi7BLn-Fm3vxw0-SrASaYaoZbCn6hKWbllxn3p0yUDwfk8psX2lOb9nAtE9WUuL-OC85ASRKqhcMHg703wfYNMmFRpoB9YtU9aYRHKGN18HQa0hvn3qBIIfLEXpukCs2SMQJEcK-XJoVGXnLmNwInb-oBPxYuN7coxcVolZ5bN6RVP9WZh1u6-SEf_y-hP8lHCDOeLTyxY3sZWUX8PK189jrfb-g26XJSY_blyj1psbT5kYQCyiH872RQNtIlm5Rr67IYYnBwupyHwESp3vrWke2gcVTjkSA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/e7a73bd81e.mp4?token=PTFjHdoZM6PdwztZz1sPx6LsE29P9cARlZ8tup0E7OwY_wBgz007lvLi7BLn-Fm3vxw0-SrASaYaoZbCn6hKWbllxn3p0yUDwfk8psX2lOb9nAtE9WUuL-OC85ASRKqhcMHg703wfYNMmFRpoB9YtU9aYRHKGN18HQa0hvn3qBIIfLEXpukCs2SMQJEcK-XJoVGXnLmNwInb-oBPxYuN7coxcVolZ5bN6RVP9WZh1u6-SEf_y-hP8lHCDOeLTyxY3sZWUX8PK189jrfb-g26XJSY_blyj1psbT5kYQCyiH872RQNtIlm5Rr67IYYnBwupyHwESp3vrWke2gcVTjkSA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یه خرگوش نر به تازگی جفتش مُرده بود و میخواستن وفاداریش رو نشون بدن که اتفاقای جالبی رقم خورد
😂
@News_Hut</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/news_hut/67928" target="_blank">📅 22:59 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67927">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HKhgIOTTAwHL69tYn8N2LPFq-f_bboCmbS87eAl9o9rlLX29gmy7zvDsew9sU70rNx5KZzADx2uiI47tFoiwPcHrLgpdUeFLfETGg6qRJwe6wZAU1L4PGIg2GvyPF9oVEwMNlM7MXUh4gXRA9l4bp1rffKXLfZwVtaKLo-bAEhpwsdZnKloPHoNOR4IoIuiqTGgqjNl5RjXTMkPrvnllk0kQmSimaWsXQeA2qyzvaXCLk8bFBNFoP8kk4FQFIMfFz1xct-qb5ny23S9q74aTS6JroGKxHmqSQLDIsZLPxUl4OwxzXt6GrJp1EaeNwk-IpJXGzTfKaEfTAXvvPhG-Sw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
رسانه های عربی وابسته به حکومت؛به تمامی شهروندان و مقیمان کویت، بحرین و امارات متحده عربی:
با توجه به وابستگی حاکمان شما و استفاده از برخی مناطق مسکونی در کشورهای مذکور برای پرتاب موشک‌های زمین به هوا به سمت ایران، از شما درخواست می‌کنیم که نهایت احتیاط را به عمل آورید.
در صورتی که هرگونه سیستم یا سکوی موشکی را در اطراف محل سکونت خود مشاهده کردید، لطفاً در اسرع وقت منطقه را تخلیه کنید و از نزدیک شدن به پایگاه‌ها و تاسیسات نظامی آمریکایی نیز خودداری کنید و از تردد یا عبور در اطراف آنها اجتناب نمایید.
از تمامی شهروندان و مقیمان درخواست می‌شود که این مناطق را فوراً تخلیه کرده و به مکان‌های امن دور شوند، بدون هیچ گونه تأخیر، به منظور حفظ جان و سلامتی خود.
پیش از این، هشدارهای واضح و مکرری را به حاکمان شما در مورد خطرات دخالت در این مسیر و درگیر کردن مردمشان در یک قمار بزرگ با سرنوشتشان، ارائه کرده‌ایم.
با این حال، آنها تصمیم گرفتند که در مسیر وابستگی کورکورانه پیش بروند و تصمیمی بگیرند که بازتاب اراده مردمشان نباشد، بلکه از خارج از مرزهایشان بر آنها تحمیل شود، در غیاب هرگونه حاکمیت واقعی.
بنابراین، آنها مسئولیت کامل تمامی عواقب ناشی از این مسیر را بر عهده می‌گیرند.
@News_Hut</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/news_hut/67927" target="_blank">📅 22:27 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67926">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/evK3MGJxf9-eDy6A1V8QWs55Kg8gD4sIRE-j7XQSY9QDu78xN8lqZ33hRn8nPN9iqiHhi9QzYg3n1B16jeVxof9aiw-VRKoROgjd-JmHszMrtb9uySs13xNbvcwFuRYK3g_6Srw_RyFG_lLxubnVS4rQ9gu5eUc_ql6GuckneYkFdj0QgkWmjOKDbbpfpjhvnW-p0MSxRygR9l_9_1zpvUm6JRgqSMdfRciuShsmCXoFv4M-cKxGBWdwBwq6sVaY4xPLTJw5pymSLaPIeL9Kzq897imaZc0IQQYRl5UjBoIKnivRSW7VsDqmi0XrEj0HTG6xvZW-l3l_Sn9pO6xoCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
آکسیوس:
اندکی پس از تماس تلفنی با پرزیدنت ترامپ در شامگاه شنبه، سناتور فقید لیندزی گراهام در گفت‌وگو با فردی دیگر از وخامت حال خود خبر داد، اما گفت تصمیم دارد مراجعه به پزشک را تا صبح یکشنبه و پس از حضور برنامه‌ریزی‌شده‌اش در برنامه «Meet the Press» شبکه ان‌بی‌سی به تعویق بیندازد.
وقتی به او توصیه شد فوراً تحت مراقبت پزشکی قرار گیرد، گراهام با شوخی پاسخ داد: «الان نمی‌توانم بمیرم.
هنوز باید تحریم‌های روسیه را پیش ببرم، تکلیف رژیم جمهوری اسلامی را روشن کنم و روند عادی‌سازی روابط اسرائیل و عربستان را به سرانجام برسانم.»
سناتور فقید لیندزی گراهام تنها چند ساعت پس از این گفت‌وگو درگذشت.
@News_Hut</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/news_hut/67926" target="_blank">📅 21:49 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67925">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8b34de9065.mp4?token=bsniVGBFi1rHIpCs4LfQ3hxc-pwIinT9tvivCF7hjxUZDXzOlsBqIhqeBJP9CJ5FAP0yY-Qm-K8JXRTkX-jZOitdlTTijcCOaCphOMEbvvzSP2gXOlOB6Ui3OeKDybbewnRnNbIXaZxsFysg81v89-69NB4ll4EJD76q4rrINN3mSDpLAermnc5zHZgl8m3CwF2dAmIoTnUUYn3U-YihJZAMRy6KfdsTv9-33b0XEBukwH1w5n1vuRUrORCXK-tKKm14oQTSkARgDXdom1EsToXLB6xAdbKMO_Tr2VFB2Nyqvm2NKJ4zaqZ1aNrGIbtt_rKBUfrn1gsqrIDSxMvcag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8b34de9065.mp4?token=bsniVGBFi1rHIpCs4LfQ3hxc-pwIinT9tvivCF7hjxUZDXzOlsBqIhqeBJP9CJ5FAP0yY-Qm-K8JXRTkX-jZOitdlTTijcCOaCphOMEbvvzSP2gXOlOB6Ui3OeKDybbewnRnNbIXaZxsFysg81v89-69NB4ll4EJD76q4rrINN3mSDpLAermnc5zHZgl8m3CwF2dAmIoTnUUYn3U-YihJZAMRy6KfdsTv9-33b0XEBukwH1w5n1vuRUrORCXK-tKKm14oQTSkARgDXdom1EsToXLB6xAdbKMO_Tr2VFB2Nyqvm2NKJ4zaqZ1aNrGIbtt_rKBUfrn1gsqrIDSxMvcag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
کانال 15 عبری:
ارتش اسرائیل با همکاری همتای آمریکایی خود، در حال تمرین سناریوهای مشارکت در حملات علیه ایران است.
ارتش در حالت آماده‌باش دفاعی برای مقابله با سناریوهای مختلف قرار دارد.
@News_Hut</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/news_hut/67925" target="_blank">📅 20:50 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67924">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">ترامپ: امشب به طرز ویران کننده ای به ایران ضربه می‌زنیم
👎
خبر بالا فیکه و ترامپ با هیچ رسانه‌ای چنین حرفی رو نزده
@News_Hut</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/news_hut/67924" target="_blank">📅 20:17 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67923">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🔴
❌
وزارت دفاع کویت:
۳ پایگاه مرزی زمینی کویت هدف حمله قرار گرفت.
‌همچنین یکی از سکوهای حفاری دریایی شرکت نفت کویت هدف حملهٔ یک پهپاد قرار گرفت.
@News_Hut</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/news_hut/67923" target="_blank">📅 20:17 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67922">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QUAzP5z0-yPSTtysJtIA6QdvW7cTL-Wijyayff2bk8HvS_aQWqRZBBzTAw7ybXab-mmyEQb-6rnRKPXY-kcCTF38JMZ_4fgIxX5RnYPRIZeQnj07R8E4kcUwSMObKiOcfzUs_qtMix6UXWwxxsMNIkwMfVct488cR0uexYUGRzFKumQdwEnxhxl9jk8njCN_ZJ4i6QMPxdTaCDSZr1u2V8AyCERXwy9s_cEWIPbf7jYQN_LTkwEIrc9-xexPG1Iq1MLuQCyJeeCqiXubk36gAdcBrXkdbQpKl64JN6P3Oh7i6OZOOhFJOSk0vR315ZXQTjOaR0J-pgn-rjecOfmNaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
آکسیوس:
ارتش ایالات متحده چند حمله را علیه سامانه‌های موشکی و پدافند هوایی، و همچنین قایق‌های کوچک متعلق به سپاه پاسداران انقلاب اسلامی در چند نقطه در نزدیکی تنگه هرمز انجام داد.
@News_Hut</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/news_hut/67922" target="_blank">📅 20:15 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67921">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🚨
🚨
🚨
فارس:
خبرهایی درباره کشته شدن 3 نظامی آمریکا در حملات موشکی به کویت
@News_Hut</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/news_hut/67921" target="_blank">📅 20:03 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67920">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">🚨
🚨
منابع خبری آمریکایی:
یک حادثه امنیتی بسیار جدی در یک پایگاه نظامی آمریکایی در کویت، پس از حمله ایران، رخ داد.
@News_Hut</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/news_hut/67920" target="_blank">📅 20:02 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67919">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">🚨
🚨
🚨
منابع امنیتی به نیویورک تایمز:
ارتش ایالات متحده، مجروحان جدی را در پی حملات اخیر ایران، به بیمارستان پایگاه رامشتاین در اروپا منتقل کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/news_hut/67919" target="_blank">📅 20:01 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67918">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jwq2nc5i1Y0VYM7rZddu6ptMs_5DlvxaYfj0pg4Kj6u5jadweFx7lZckj2n3EcSNo070dWUaSIXziNSU5MlLcX9suZpIaShpXtKyZVWoPug_oreofJ6WzNrMydx2cX713XMoM90o4LlX427ViSX3IVIPkk76GEpHbPW7kGxl2LMFQexVjVnTN1nUm2sAYPea0BkymPMiod3m-XBuYI6KRdwahQOKa6go7_RAhrKisov3kWHeobY-jakn1Q2i_xIskLjQz0MizopIk_kjgGwzgJQJx1fSlPsAFT5GvbQYeaxwT1hziPOvabOTFmgbTILYynXJLCSSNVOctY9OVqyXbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
قشم همین الان
@News_Hut</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/news_hut/67918" target="_blank">📅 19:50 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67916">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c7c182d343.mp4?token=ug0TYJL6i25oPJFtQXn71wVZIuGG6Dew2J-Bo5llKBLrOUJ8hbJicgXp1kZZ0buPrdLHE1OmnVM2hcL5bDuXUZzkGCQkXwL_SLknx2P8StVFsowq_IV9_ErRn79XT_wMqJwVUZmC22E6DdVxPy3mky4zI8rnK57yB3GWM_3MTUu4lXrIIgDqOW6K2UIOCpCv64t2yQxZdqjDnElbE5ICLLcbxsB6duUH_VicXdqkAYL1prCBi5kwoaZEA-W8_iR5P7tvpvTLmc0Rh2eajU3CyGCbztzzMKWPVt9qj1QzV-wpGQLrWMivQLzWd4JJ1wPbkl5Rqr8dOOTFrS4kQhhkYg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c7c182d343.mp4?token=ug0TYJL6i25oPJFtQXn71wVZIuGG6Dew2J-Bo5llKBLrOUJ8hbJicgXp1kZZ0buPrdLHE1OmnVM2hcL5bDuXUZzkGCQkXwL_SLknx2P8StVFsowq_IV9_ErRn79XT_wMqJwVUZmC22E6DdVxPy3mky4zI8rnK57yB3GWM_3MTUu4lXrIIgDqOW6K2UIOCpCv64t2yQxZdqjDnElbE5ICLLcbxsB6duUH_VicXdqkAYL1prCBi5kwoaZEA-W8_iR5P7tvpvTLmc0Rh2eajU3CyGCbztzzMKWPVt9qj1QzV-wpGQLrWMivQLzWd4JJ1wPbkl5Rqr8dOOTFrS4kQhhkYg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
منتسب به قشم
@News_Hut</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/news_hut/67916" target="_blank">📅 19:46 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67915">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🚨
🚨
🇮🇷
نایا:
نیروی قدس سپاه پاسداران انقلاب اسلامی، کشتی‌ها و شناورهای آمریکایی را که در منطقه "کیلومتر ۲۰" در تنگه هرمز فعالیت دارند، هدف قرار داده است.
@News_Hut</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/news_hut/67915" target="_blank">📅 19:33 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67914">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🚨
🚨
فارس:
شنیده‌شدن صدای چند انفجار در بندرعباس و قشم
@News_Hut</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/news_hut/67914" target="_blank">📅 19:31 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67913">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ErvMUcNyc7LNzuyJGeAAMcxREwmHTGoUuzeFb4lZgoc2FXeM-wTtmiD0-vGSAiYS2zNV2yud6xks8SWny23IL2oU1bSu3f-zlxcWGx9rh_PETPPR8EXU6VbEJ35iuI2-hKHpeQu5O_-t8bsX0yJN1MZPRpa7hxOjOKRydchDzm8btAXJ_7AzigsBZr5FMQDp4IPstovCCgaYySHo56hefUZvlYkCzvI-gze9E11P6a3UMwqqknitrv5Um0pNB5-Pq_sQa-ZbCJJKsZKORkozosCA3LhZz1dRs8fDraHFVARbvdVU8HcQADvFnVtNxSDYEVN5ijryV0Q06Qv7ocMKEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
لیست تروری که روزنامه همشهری منتشر کرده.
@News_Hut</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/news_hut/67913" target="_blank">📅 19:20 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67912">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/491f5ab181.mp4?token=V8jix_ShhhzRVZ0Cpw35hYOR2S6P_pN7MVryyHwyzztx1PT8CzgIEr7bHPttRd5SLvYyhmRsbRdtwu5DQrS_U23M0u5iJLPr6YszrEp2WuNRjvrVbJZOZNZR26GzEQkv2uOLre8DJS4JveYYu_-3Eoveb5fLi8rm2d1r7R2uqGqUMyCJb8_Y51fPu2mnPYq67H7_1ikYLll_q4yLQ99c-Db8UfHaYd1AYgqRWxUWQY40lNgMioqbV0VhXyDuFap2EjWBg1-Z2PAsnunCMSBBhXNxSUkwkqxiMuHoUEDGnAw2JKb_QE190YHgr8FbBKfP-dkt4x22tQD_WBukCk9dUA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/491f5ab181.mp4?token=V8jix_ShhhzRVZ0Cpw35hYOR2S6P_pN7MVryyHwyzztx1PT8CzgIEr7bHPttRd5SLvYyhmRsbRdtwu5DQrS_U23M0u5iJLPr6YszrEp2WuNRjvrVbJZOZNZR26GzEQkv2uOLre8DJS4JveYYu_-3Eoveb5fLi8rm2d1r7R2uqGqUMyCJb8_Y51fPu2mnPYq67H7_1ikYLll_q4yLQ99c-Db8UfHaYd1AYgqRWxUWQY40lNgMioqbV0VhXyDuFap2EjWBg1-Z2PAsnunCMSBBhXNxSUkwkqxiMuHoUEDGnAw2JKb_QE190YHgr8FbBKfP-dkt4x22tQD_WBukCk9dUA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
🇺🇸
پرزیدنت ترامپ:
دقایقی قبل از فوت سناتور لیندسی گراهام با او صحبت کردم و "او به جز خستگی حال خوبی داشت"
@News_Hut</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/67912" target="_blank">📅 19:18 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67911">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🚨
🚨
خبرگزاری مهر:
حمله موشکی ایران به موقعیت یگان موشکی نیرو زمینی ارتش آمریکا در کویت.
گفته می‌شود این یگان در حمله دیشب به جنوب ایران حضور گسترده داشت.
@News_Hut</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/67911" target="_blank">📅 18:52 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67910">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fb024df7a1.mp4?token=aF7U3Dxwv5n2-keWWfHSowEsuVQDSGrB9WEaV-RKl8ixAzJi-OFY4fdpmQ7F9FNVdNReyQq1Rdqr67sc73vZ7tlI9X0HOEX6qKPVcJbuTL4-q4T2WXBhZ7U5QNgsbTpUY8KVMpaMZs6HnkZ6Zss1T2BqYEKC3_TF9DFk1s3QAWfT4xMUu9Lodc97xzYNa6y0fDec1vBgyKg0I3bmogQb1JPUNZ34SiciVRY0cb1A-xjI-BX-sTc-ujoH6gWxOrncwHNKjbaN0nNk3QJ8S5BoB3_U_hTisw40HsUAcoT9JHisJ8HwoOr5MghlnoRNeQxhgi2dyWNoJG4Js5Zqqxm9YQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fb024df7a1.mp4?token=aF7U3Dxwv5n2-keWWfHSowEsuVQDSGrB9WEaV-RKl8ixAzJi-OFY4fdpmQ7F9FNVdNReyQq1Rdqr67sc73vZ7tlI9X0HOEX6qKPVcJbuTL4-q4T2WXBhZ7U5QNgsbTpUY8KVMpaMZs6HnkZ6Zss1T2BqYEKC3_TF9DFk1s3QAWfT4xMUu9Lodc97xzYNa6y0fDec1vBgyKg0I3bmogQb1JPUNZ34SiciVRY0cb1A-xjI-BX-sTc-ujoH6gWxOrncwHNKjbaN0nNk3QJ8S5BoB3_U_hTisw40HsUAcoT9JHisJ8HwoOr5MghlnoRNeQxhgi2dyWNoJG4Js5Zqqxm9YQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
کویت کمی قبل
@News_Hut</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/news_hut/67910" target="_blank">📅 18:51 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67909">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eWrd3Pw-k7tzntZnqHQC6h2BwzaYHRamI9UnO9bo4YcAxCl0FiPGNLDLp8YGJ9yyRr5SY18JWMwG8y4YL-x7KRBWshZTQAhomxxSXTtIWnsZECHEgyY74RQLW8TDrMN7yW4YIOaERPVM90O_l5N9V0SWmPNC4b5RFNRKUOjwoEx1_-5r01bfLFf0-bjxypZN1SS-QrVQrin3z2qHFtyXXNcZcDI-wkvK7jR70qYIauEKNY_R0oVf1TbX9nIhG-XLo8L6iDHDTuIny5HpcdA-oAMFfoIM6o3EJrqEoYGfBtxw2EOCq_n3hKyt8bzlVq-fvyUtA-5d4o4K49VznyB0XA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
دو انفجار در کویت و برخواستن ستون دود
@News_Hut</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/67909" target="_blank">📅 18:45 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67908">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/09b038fd4d.mp4?token=YIY5eGQiddmCCPQWK6OQtoNkjamUuTM-F-ONFtppmoDwHcNz89MzHEbkWF8rn2zQ-eSDcQjI7InbPT-IuL1ElYIJ5AyUTsUhBtij3YpX7PQPRTGq6IOUX-bYFH5-s9xPDPjMbWsGFbRgwhwsFEJwFlETtlav6RcxNsi68-pIjjTbliLlDyE4rtgflfGsVD1GoBRmIrykfaSnyS3ZgCL25NzHkxDakEc3fw-M6Aj3s-e7zlPLGu6pyBNBtQ6uKmUEJjbnOBYxjQAZuOB2TanWveeVc-LYFWGXsBOnxUNeO1aChUH_PJTfRUJIjeo_Zkc_or2ZofT_RW46AXKQsNfZOw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/09b038fd4d.mp4?token=YIY5eGQiddmCCPQWK6OQtoNkjamUuTM-F-ONFtppmoDwHcNz89MzHEbkWF8rn2zQ-eSDcQjI7InbPT-IuL1ElYIJ5AyUTsUhBtij3YpX7PQPRTGq6IOUX-bYFH5-s9xPDPjMbWsGFbRgwhwsFEJwFlETtlav6RcxNsi68-pIjjTbliLlDyE4rtgflfGsVD1GoBRmIrykfaSnyS3ZgCL25NzHkxDakEc3fw-M6Aj3s-e7zlPLGu6pyBNBtQ6uKmUEJjbnOBYxjQAZuOB2TanWveeVc-LYFWGXsBOnxUNeO1aChUH_PJTfRUJIjeo_Zkc_or2ZofT_RW46AXKQsNfZOw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
پرزیدنت ترامپ:
ما آخرین جلسه را با آنها داشتیم، آنها دیروز با یک توافق موافقت کردند، یک توافق عالی برای ما. نه هسته ای، نه این، نه آن، نه هیچ چیز. آنها همه چیز را رها کردند.
و بعد از آن اتاق را ترک کردند. و سپس در عرض یک ساعت یک پهپاد و یک کشتی را به آب انداختند.
گفتم شما افراد مریض هستید. شما افرادی مریض هستید
.
@News_Hut</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/news_hut/67908" target="_blank">📅 18:25 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67907">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/550c5fbdb2.mp4?token=bkRrmFUrsEOYGYcHuE27V7mu_XKvi6St7TiJzMFGeFQPAMXjQWHdwSFA67KIb_AMfUuTXQpJlFElgnPzBXB-Yf1Tm6ZjwBezPM1YgXoomjummNOHkMHhSNARWHQQ8_fKD6C0gxx9HOLa8sEk8uDhMHHDugdGYvOiL_MzxXoD1d0aSULBv7qC-wta-znXli5mZq9N3zphS1VTVUR8OnLgQak66W_AbK2XOuqFBXmywB5l4I8XIams4fKhGEOLNuwu7-3QUmzdGEvhreXsILy6xwfG1_QOgVqMkGlq6XOLOt17vewLjzRmGw8r3sV60qNVcP2J2IpA0Vj4V5N2M8LILL-UQ300ni2qqdCkmJeR8OQwIpG5vfe5-VfSoSdrO-LUqNcfVcfYG-4VuzPyTP3GIdukjibPm_hI5kyidUEOAqY8CMpPt_lCYuAJVrWcvSAEAeykW5r4mEb4QCTdSVlMN_7XmKkAep1HYpbSA5mnwgYoD0d7pnp9T6_wo-CumTaBaCYEQrw9i7JzoGXFpAnqiSmiB-iUaa2Qa_EuyFGnO5FyczwZUgw_Q3K6h0mM5zc2EzWKEyQBqyfx-nrzhaWDgg6hLm61Z8IF003kT7mrnOqgomDxeqtnvQhAHoGHeQ6O9VMF7lp4zRK6iunLVRN-i6nfDMXYqWIOjnpRud8SNLw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/550c5fbdb2.mp4?token=bkRrmFUrsEOYGYcHuE27V7mu_XKvi6St7TiJzMFGeFQPAMXjQWHdwSFA67KIb_AMfUuTXQpJlFElgnPzBXB-Yf1Tm6ZjwBezPM1YgXoomjummNOHkMHhSNARWHQQ8_fKD6C0gxx9HOLa8sEk8uDhMHHDugdGYvOiL_MzxXoD1d0aSULBv7qC-wta-znXli5mZq9N3zphS1VTVUR8OnLgQak66W_AbK2XOuqFBXmywB5l4I8XIams4fKhGEOLNuwu7-3QUmzdGEvhreXsILy6xwfG1_QOgVqMkGlq6XOLOt17vewLjzRmGw8r3sV60qNVcP2J2IpA0Vj4V5N2M8LILL-UQ300ni2qqdCkmJeR8OQwIpG5vfe5-VfSoSdrO-LUqNcfVcfYG-4VuzPyTP3GIdukjibPm_hI5kyidUEOAqY8CMpPt_lCYuAJVrWcvSAEAeykW5r4mEb4QCTdSVlMN_7XmKkAep1HYpbSA5mnwgYoD0d7pnp9T6_wo-CumTaBaCYEQrw9i7JzoGXFpAnqiSmiB-iUaa2Qa_EuyFGnO5FyczwZUgw_Q3K6h0mM5zc2EzWKEyQBqyfx-nrzhaWDgg6hLm61Z8IF003kT7mrnOqgomDxeqtnvQhAHoGHeQ6O9VMF7lp4zRK6iunLVRN-i6nfDMXYqWIOjnpRud8SNLw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
خبرنگار:
و شما بدیهی است که یک شبه دور جدیدی از حملات را آغاز کردید. ایران یک شبه گفت تنگه هرمز بسته است.
سنتکام امروز صبح بیرون آمد و گفت تنگه هرمز باز است. کدام است، آقای رئیس جمهور، و چگونه می خواهید پاسخ دهید؟»
🔴
ترامپ:
"این باز است، و من نمی خواهم در مورد آن صحبت کنم زیرا می خواهم زندگی لیندسی گراهام را گرامی بدارم، بنابراین نمی خواهم در مورد آن صحبت کنم. قبل از تماس به شما گفتم.
آره بازه ما دیشب آنها را بمباران کردیم. آنها افراد بسیار بسیار شرور و بیمار هستند.
@News_Hut</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/67907" target="_blank">📅 18:18 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67906">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">‼️
یک فایل پنج‌ساعته از مکالمات بی‌سیم نیروهای سرکوب‌گر در اصفهان به ایران اینترنشنال رسیده که نشان می‌دهد نیروی انتظامی با مجوز استفاده از سلاح جنگی، در ۱۸ و ۱۹ دی‌ماه با کلاشنیکف و وینچستر به معترضان شلیک کردند.
دقایقی از مکالمات نیروهای انتظامی در بی‌سیم را در این ویدیو بشنوید.
@News_Hut</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/news_hut/67906" target="_blank">📅 18:04 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67905">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4f43409a1c.mp4?token=KURaaj-9v0xAl_8filEm0F1dNrEx7GRBo04kp5UrAkh-WTZPaNCergYkZaOY8fN1c_B5r6K6o9pDlBNh1nQ7k4wz9LgSE4U9bvOZZxnqK6Loh2zVal8kFAGTbaBTKlIrpBl1M8nm3qljNhYCayGU02GZukPU-XYXYGa41XX0VrL5xpO1naAesl2QW1DgzGl6Sg2Gsr-gYplwfUArbv-8qqsuj2jRguscOuU3a6AX-3srJUSm46ZNu9URB35X10igvMe7zzgWT6slIwbEsqDsuA7VEb8QjM9tMeJxZptKkj_y9RzV1oW6-j9eqcEM1OMfrPIOQpI9y6gZyHmgGDkXl3stcG8CdCmf76cOm7SvN1vN-QQRVyzWpmmuLAa76BDQTMYwS3NhAt_K1BYH2l8b-OiJnzE3bYYrhMxFumqn1nOiGDnguuoURNxo7Z-4PnXLP8OrDJckNiWBD2jSC7DTEpIuQgoDlQ4qosWAJQMRU68vYa8YICQyiBOzNFvizq4flGTRymNYh_Y2-xMOht1VAdCZ7eNGPojZEcnJcQ2h5t0kHguAmwbJmOIsxq56S3l0P-HJPW9JWv5fzR28vSXivXPmMRET6GIsVnCDLWK7ZSGmV-gKulwtkq1FeSogvRPdCCyPwaCgY6UsWddGu5E9UYS3hB2bLIY8ZS_9X1GsB_Y" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4f43409a1c.mp4?token=KURaaj-9v0xAl_8filEm0F1dNrEx7GRBo04kp5UrAkh-WTZPaNCergYkZaOY8fN1c_B5r6K6o9pDlBNh1nQ7k4wz9LgSE4U9bvOZZxnqK6Loh2zVal8kFAGTbaBTKlIrpBl1M8nm3qljNhYCayGU02GZukPU-XYXYGa41XX0VrL5xpO1naAesl2QW1DgzGl6Sg2Gsr-gYplwfUArbv-8qqsuj2jRguscOuU3a6AX-3srJUSm46ZNu9URB35X10igvMe7zzgWT6slIwbEsqDsuA7VEb8QjM9tMeJxZptKkj_y9RzV1oW6-j9eqcEM1OMfrPIOQpI9y6gZyHmgGDkXl3stcG8CdCmf76cOm7SvN1vN-QQRVyzWpmmuLAa76BDQTMYwS3NhAt_K1BYH2l8b-OiJnzE3bYYrhMxFumqn1nOiGDnguuoURNxo7Z-4PnXLP8OrDJckNiWBD2jSC7DTEpIuQgoDlQ4qosWAJQMRU68vYa8YICQyiBOzNFvizq4flGTRymNYh_Y2-xMOht1VAdCZ7eNGPojZEcnJcQ2h5t0kHguAmwbJmOIsxq56S3l0P-HJPW9JWv5fzR28vSXivXPmMRET6GIsVnCDLWK7ZSGmV-gKulwtkq1FeSogvRPdCCyPwaCgY6UsWddGu5E9UYS3hB2bLIY8ZS_9X1GsB_Y" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ویدیویی از  فعالیت موشک‌های رهگیر پاتریوت بر علیه موشک‌های ایرانی در پایگاه موفق السلطی اردن از دید سرباز آمریکایی طی درگیری‌های روز‌های اخیر
@News_Hut</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/67905" target="_blank">📅 17:15 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67904">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/12b2f989ab.mp4?token=beyh1zvFFtu-8_l-wW6mVjMS8Vq6O1Ta3F1e3H0qbEsbhO9N5ocnMecHs4lCVL4814f6Q2U7mj8lVutZzaoXp4Zxx-JgYyf2M6g-PHC5_Ouq6Ydm6_qYD8pL5lfZAg-_KZcDuZCg3xIf2XFLtdZHxHzAndCol5WApBGPM87OAhAhAAmZhde47v5OzbM2Nf2MagYX0UJ8exNWNsZ1c_DgqN8ZnXO-saLB_Ng99XRXB2HmxYbX_0sbv_OhNa6RtbALvGyXD0LWTX3X-WfZ9OcVc5ljyAxGV-i_b4tN9InNXglWsPxeNDR2oLMIRki9E8bvz0F1get3YS5xfUiKfpkudw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/12b2f989ab.mp4?token=beyh1zvFFtu-8_l-wW6mVjMS8Vq6O1Ta3F1e3H0qbEsbhO9N5ocnMecHs4lCVL4814f6Q2U7mj8lVutZzaoXp4Zxx-JgYyf2M6g-PHC5_Ouq6Ydm6_qYD8pL5lfZAg-_KZcDuZCg3xIf2XFLtdZHxHzAndCol5WApBGPM87OAhAhAAmZhde47v5OzbM2Nf2MagYX0UJ8exNWNsZ1c_DgqN8ZnXO-saLB_Ng99XRXB2HmxYbX_0sbv_OhNa6RtbALvGyXD0LWTX3X-WfZ9OcVc5ljyAxGV-i_b4tN9InNXglWsPxeNDR2oLMIRki9E8bvz0F1get3YS5xfUiKfpkudw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پرتاب شدن سرباز بر اثر انفجار اشتباهی در تمرین پدافند هوایی روسیه(نزدیک بود همرزمش رو هم بگا بده)
👅
👅
@News_Hut</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/news_hut/67904" target="_blank">📅 16:31 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67903">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KM_cRfK0o8zV6c8C8GWf9pbgIacby5jpaOta2QwmFzJnpSdGpwrlJJerE0p5LiZHj3Mms3vB1aMvfa0Neo7dzXFpYNs_doqp21Zz4375jIMwwOoPl19Jfp4Zv8qCdQyDZL2858luCxyXKdallvAXRU1RS22-6cHjiFvV9atJfSamd5j-f691BBifdfpQo3jy95MXeOBSOgzTr3Jw0Rl9YAlykAjoKO6C__S_Y8HZerpuc2x2IDwJhr2jS1CHOyNhke0W7zci6ca9jAS9FzVpZdfRbFPhkeeXpvn1I4W7ZiAPXSS67mpSV299Cz6NkP33PBXCjIicnHT41hw8eolWWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
فرماندهی مرکزی ایالات متحده:
تنگه هرمز برای تمامی کشتی‌هایی که قصد عبور قانونی از این آبراه بین‌المللی را دارند، باز است. نیروهای آمریکایی در این منطقه مستقر هستند و آماده‌اند تا از آزادی تردد دریایی اطمینان حاصل کنند، علی‌رغم اقدامات تهاجمی، آزار و اذیت، تهدیدها و اظهارات غیرمنطقی ایران. ایران کنترل این تنگه را بر عهده ندارد. ترددها به روال عادی خود ادامه دارد.
@News_Hut</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/news_hut/67903" target="_blank">📅 16:14 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67901">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ME0oFqbkjW9M9UILL0nqqGctKGG8cZWCQJAFT7O3b9rjSZHXoKZcMRo2Wr1298ACMoExVgv8CWj0f7Knr4Ior0aNTWIO4jgOxQ5_fTbnInBQJpXhUf0Sn3ZiF90C3LEG1XNJEbF2TskMDwwW1DCGNg0LaJxp_OsK0fUYGg9typJ0vn-02gqlibehlfK8-EC8C0IoEX9Pw2i1kTKicqt9aAgwZ-F2sg0BhUzOvqIFyjZ5TOfr3vdXLBAj58mgNHOMm8R54-G4i81Ex3qTqD8sxyiCYLmms0O_WCF5Cr3dVYwMyLr746g56wjpwVhPZpGpMb6ZoJLjxPJ32wU7YBqapQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aaa15fb6f3.mp4?token=FlkNQnJzxVfAcLi7HCg0auSWmCejE56OJDbPJ5MR8s1kVuAcDzVoouxinxVq8uBk15C3fl3-dOtEo9r9q1_qZv0L09OEaoHMsr9tGUeSHDGIMvBNJ7J8mNg3ApTh5m0KqfpXJP3PtCeknnNGEzVT_4RErDuAoJ9Aqq5J3x5H1Yfm5t8jdSlC9u-qVp4Wab2vZeDEcOHS1XWOPyPVCiFHbdFaSdrdYy6uB51_44RyMZdaqsBfV3Y8MmQZxpMr30xDVz_rKiIusDRbGa4g4JIpD0yN4NO0IOcDBPd_qY933bWGa99vyeqwrZuFOcdd9mHwEtezn5Og7PEtzApcYndqLQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aaa15fb6f3.mp4?token=FlkNQnJzxVfAcLi7HCg0auSWmCejE56OJDbPJ5MR8s1kVuAcDzVoouxinxVq8uBk15C3fl3-dOtEo9r9q1_qZv0L09OEaoHMsr9tGUeSHDGIMvBNJ7J8mNg3ApTh5m0KqfpXJP3PtCeknnNGEzVT_4RErDuAoJ9Aqq5J3x5H1Yfm5t8jdSlC9u-qVp4Wab2vZeDEcOHS1XWOPyPVCiFHbdFaSdrdYy6uB51_44RyMZdaqsBfV3Y8MmQZxpMr30xDVz_rKiIusDRbGa4g4JIpD0yN4NO0IOcDBPd_qY933bWGa99vyeqwrZuFOcdd9mHwEtezn5Og7PEtzApcYndqLQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
بعد از اینکه صداسیما رسما مرگ لیندزی گراهام رو تبریک گفت
فیلم تبریکش بشدت در رسانه های جهانی وایرال شده و گویا برخی دنبال ربط دادن مرگش به جمهوری اسلامی هستند.
@News_Hut</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/news_hut/67901" target="_blank">📅 15:55 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67900">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q49gt-DrN9G7EEeaVuyyLWE9JYz5afnnBKuuQPhFfelm24piUCjBrMlSaoa2XIszrsO54s7LRl5WzIZGW3u0k1wFMihjRiB395X5IwMAfzgzFintZ3xzma-k08dUiU3IFxDQ4wjOMLNMVTUARW57G7aOXBtq1GLPYOEIEj3EB700ytW5pM23FAl3ZQ16_1UFVcRDsVYZXiuKA6cLvGfJ5HtlGpFVnkN6YgyrxmJbyAGLq1Po6k4iuH6l4hZ2JRGMSwPkMgRdfBLiLcuJ0C3NB09dL9C-ketqk-5N-Uwi511QyJgPlzaI897iSEu0QDiEFOZD8786ucEuGvRZECxwqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
پس از شلیک چندین موشک بالستیک به کشور قطر در طول شب گذشته، عباس عراقچی، وزیر امور خارجه جمهوری اسلامی، ضمن ابراز همدردی صمیمانه، به خانواده و مردم قطر تسلیت گفت و مراتب تسلیت خود را به مناسبت درگذشت امیر سابق قطر اعلام کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/news_hut/67900" target="_blank">📅 15:30 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67899">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f465c542d7.mp4?token=bGWbnuJOWXDxO5tGh-T1dd-HNGOGGqbrlHEtxUSdiu6nJmVSu1EPOeRLe_56u0zzSkDhSRlCH-ymidJqhXLoT0lnRDC9t1xDKuhr6phij1Cm0p6OB3ql2K2sDURKC4XrulDv7XqvvIcPer80J7W6ZBAPlqSUSxV273g5quIbqCTRb8QpJKdM72HlIS1UEpZYh4tbqAWaXJjDCwY4f8w7hNciPmO2i3Wkq7UuN2CEcq_K7p0xbclpaqdhlqwz9rQ6jObYpQtMPqAJb2RMZEG5zuxNPHviiQ8fW5pV8HzKdoY2aOnkYhN4ezQ1m2AublnUuY1YtW6XhkA5eBJbzIShTg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f465c542d7.mp4?token=bGWbnuJOWXDxO5tGh-T1dd-HNGOGGqbrlHEtxUSdiu6nJmVSu1EPOeRLe_56u0zzSkDhSRlCH-ymidJqhXLoT0lnRDC9t1xDKuhr6phij1Cm0p6OB3ql2K2sDURKC4XrulDv7XqvvIcPer80J7W6ZBAPlqSUSxV273g5quIbqCTRb8QpJKdM72HlIS1UEpZYh4tbqAWaXJjDCwY4f8w7hNciPmO2i3Wkq7UuN2CEcq_K7p0xbclpaqdhlqwz9rQ6jObYpQtMPqAJb2RMZEG5zuxNPHviiQ8fW5pV8HzKdoY2aOnkYhN4ezQ1m2AublnUuY1YtW6XhkA5eBJbzIShTg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
واکنش ممد سامتینگ در حالی که تندرو ها دارن شعار
«مذاکره با دشمن خیانت است به میهن»
میدن در مراسم چالسپاری خامنه‌ای
😂
@News_Hut</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/news_hut/67899" target="_blank">📅 14:25 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67898">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🚨
🚨
نتانیاهو در حال بررسی سفر به منظور شرکت در مراسم خاکسپاری لیندی گراهام است. احتمالاً ترامپ نیز در آنجا حضور خواهد داشت.
@News_Hut</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/news_hut/67898" target="_blank">📅 13:43 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67897">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZHs03zBQGIcGU_D47Xb-peqjeds0J8wRwGn1EVtjhUYfIct1AnyTlEBenC_oB1g1R5uFskrt5HlERBkw-eAiRjhSZ5y3cxWamWOIkJouTCyy_8pE3aJt1rKLAXwdmNea1xCE8M_R_mMQbmR8aXc5RdC4bme1QXaA-_-d9oK5PUwxAdMGVadlcPykSVu82UEF0Ud_vEsPP3snK0sbYQgSYvQxiNKC_H7Qx1YR4ZaoGfxJDWWuafQ4qkdiN_Lve2eLhVQO2yXPnWgfdOKCHFJTC-Y9LM7zIJGp-lWd1CUG7nyA5AI50YhiOsnqX5RC0KZpA-HkNaAm0a4dCBULnpmW2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
حمیدرضا دهقان از اعضای پدافند ارتش در منطقه جاسک طی حمله بامداد امروز ارتش امریکا کشته شد.
@News_Hut</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/news_hut/67897" target="_blank">📅 12:59 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67896">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hw_mlDkpfTnA8E8qVaUSoxf472FhjCzsYQSgitBZqVbKE3cVLRT8-bkCCr_BlH5daH0DkjkYYa4FRwOL1Zky154PO23nshoQaHY3yJ-qhDjw_1KvkLJOhaubQky1PEE82bo032uDMdf4g8kSPcayleSciBs-aEDwBgcKiWv1Enb6O8nN8YwJh-InNMXWjCmio6DVedRmVXbtYdUMI0cL-sXRZ1nGqdlyPBp6SQwnoq3daZTBt4BC3cHjB0SX1RA07OoF0WOfF9HO5qPyGPwv9RwCEvipWb8ct8ZlYmE92jdLgxlxk4X8taWxPzJ7ZN5XhGFvCoW3vgq4F1_oSw6KTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
واکنش مرندی عضو تیم مذاکره کننده به درگذشت سناتور لیندسی گراهام:
چقدر بد؛ من میخواستم او قبل از رفتن به جهنم قیمت بازار نفت را ببیند.
@News_Hut</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/news_hut/67896" target="_blank">📅 12:33 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67895">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TwHzoRkgz8KUi3mF3ig9JTrV4Ir0B7iWMggVSEMHQDZpoj3KDS97ZEB0DHYKnjzsFJlzPXs8UXrEiJ7d_P5FxXvUpN84i2jyu8SCn9TsFPGW48a0ghlyKSAFVTdzQxO2le7g2tP9L9Ibf-0Mt9N9wP_88koJAFxcJn3AFuFIpE-UcDJT5jFW7V1_8-SpRik709gc-bMBprX1KOGbQF3KlDoQzvu_DKk1P7dT1Y4EBGgaSNL2balNRA3D55u3Y5heW7LLlDd2rcWp26Mt1CONYaTO47vhTb32vVWvxP-xRY3ty4qip_uYRW_RCDFUtSxPMbiEcwqC6rKlmGz38v_daA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
👑
شاهزاده رضا پهلوی:
از درگذشت ناگهانی سناتور لیندزی گراهام، دوستی ثابت‌قدم برای مردم ایران و مدافعی سرافراز برای آزادی، عمیقاً اندوهگینم.
در لحظاتی که نیاز به موضع‌گیری اخلاقیِ صریح و درست بود، سناتور گراهام در جانب حق ایستاد. آنگاه که دوستانِ واقعی کمیاب بودند، او در مبارزه علیه استبداد، در کنار مردم ایران ایستاد.
او از صدای خود بهره گرفت تا اطمینان حاصل کند که صدای مبارزانِ راه عدالت در راهروهای قدرت شنیده می‌شود.
حمایت او از «انقلاب شیر و خورشید» ایران، لقب «عمو لیندزی» را در میان ایرانیان برایش به ارمغان آورد.
یاد او همواره با سپاس و احترامی عمیق گرامی داشته خواهد شد. ما مراتب تسلیت عمیق خود را به خانواده، عزیزان و همکاران سناتور گراهام، و همچنین به مردم کارولینای جنوبی و ایالات متحده ابراز می‌داریم.
روحش شاد و یادش گرامی باد؛ و باشد که دیگران راه مبارزه برای آزادی را ادامه دهند.
@News_Hut</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/news_hut/67895" target="_blank">📅 11:39 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67894">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DSMqCFrB_0PsT8GLa_JuzMhb-YDpdOYICdbup7TF2qQZuwC3Ny5Q8p8rSCuOzNpOlDn8CUzhAIco9YjyEF4nfiZ1klIjr6MrzwkhF1Z_4Px9gGpON56tfZonZ0eabX9aklbPbpsDV7JSG0bYrAQHpF8xK1uHFMryPApjsr3DgpKeKLM9cBwl3vu2OvQUC2lFiot7Rxo9bEH4sftBJyNNr4aXRNAXUGacEISFGR0AolBWulkdPLstsUiPRGkAMSAAHwLqDF03-cr-UMDNnQfvCWWWpAFoA-YUsyiqbVmVVQqDmZVU_UzxMTd3j322UIIaD8Kkw3lMzW2ios0fTu2GSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇱
بنیامین نتانیاهو نخست وزیر اسرائیل در سوگ مرگ لیندسی گراهام:
من و سارا با مردم آمریکا به خاطر از دست دادن دوست عزیزمان، سناتور لیندزی گراهام، غمگین هستیم.
در ملاقات اخیرمان گفتم: "لیندسی دوست بزرگ اسرائیل و دوست عزیز من است. ما هیچ دوستی بهتر از لیندسی نداریم.
لیندزی فهمید که امنیت اسرائیل و آمریکا جدایی ناپذیر هستند. او زندگی خود را وقف دفاع از آمریکا، تقویت اتحاد ما و ایستادگی برای جهان آزاد کرد.
اسرائیل یکی از بزرگترین دوستان خود را از دست داده است. آمریکا یک میهن پرست بزرگ را از دست داده است. من یک دوست عزیز را از دست داده ام
.
قلب ما با خانواده لیندزی و با مردم آمریکا در این زمان سخت است. باشد که ارزش ها و ابتکارات او همچنان ما را به سوی پیروزی و صلح رهنمون سازد و یادش همیشه پر برکت باد.
@News_Hut</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/news_hut/67894" target="_blank">📅 11:18 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67893">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KxlahrMqtJJCB4-CaIjOdG4pO0jL2wiw2iksJ4cF905s8mrN5hSVfZMSslFpXF3-EYqVOTN5MfhEgR7Hi9JhF_4b7tbKheQDhXCvgEBAK3nVMqVaMt-NKIrUlfeJcl-SzBjHvVkLVZ3i6-3fy0qk9mRIlJ5gL1_7EFEHicipL8ysvBgmBsj6VPz-uHS6OrMf9rS9WFqMRx0jIJ6YUnFa4m7MyyZT0XW79RU1Vp3zzX2qMYsyjZ0QEPS4Y7nPorxLZ6YeA1kXX05PI1rXbFUdzcCNEvUYo8vasPz6Lgw5vcP4iwhDlYaA2l3vuO8uSl9YbSc6f33leRB2cFmQrixcgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
🇺🇸
پرزیدنت ترامپ:
سناتور لیندی گراهام، یکی از بزرگترین شخصیت‌ها و سناتورهایی که تا به حال می‌شناختم، از دنیا رفت. او همیشه فعال بود و یک آمریکایی واقعی بود. ما لیندی را بسیار دلتنگ خواهیم شد. جزئیات و برنامه‌های مراسم تشییع پیکر او متعاقباً اعلام خواهد شد. چه خبر غم‌انگیزی!
@News_Hut</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/news_hut/67893" target="_blank">📅 10:59 · 21 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
