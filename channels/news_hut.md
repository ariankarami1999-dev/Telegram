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
<img src="https://cdn4.telesco.pe/file/kSSYCMxRQ3ZabGWMtc8p1Rp023JJtPm5kAYcFjrM9zVT4SNACixkbA8cdT66mQUl8UzwYU3Yl_VqRYa4UOO-PDssssI3tJNoAA020W5ucMEWtF7GIpQreeoqVJgzfsqyYbuLF4ziGCfXo7xxBUN7Ff-xuuu1gGB5KFa_YP7K1pewm4WbRJCiCWRmKOeG0sxqGo9cqqPBVqCrLwEGfL_Mo5mT_0zYjj81ndUiW6M497nJmFq5O7h3G8NPhWB45e9xKj745-t3NUhMVSehJ-Y100deKGTZOIx5SB2hQVpToM23XjDeMNTyUrr1_EqDVjGzkSeM39Y7G9Wl038qciBeAw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 223K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-26 12:10:17</div>
<hr>

<div class="tg-post" id="msg-66278">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🚨
🚨
عراقچی:
ما واشنگتن و اسرائیل را یک طرف این یادداشت تفاهم می‌دانیم، در حالی که ایران و حزب‌الله طرف دیگر را نمایندگی می‌کنند.
پایان جنگ در لبنان بخش جدایی‌ناپذیر پایان جنگ در ایران است و شامل خروج اسرائیل از خاک لبنان نیز می‌شود.
هرگونه حمله نظامی اسرائیل به لبنان و ادامه اشغال، نقض تفاهم‌نامه است.
@News_Hut</div>
<div class="tg-footer">👁️ 2.76K · <a href="https://t.me/news_hut/66278" target="_blank">📅 12:00 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66277">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d988cc6faa.mp4?token=kbz_Shmuq78nRQ0fCfj_bqphJmE42sco-ycBLfCZ7RR3z2fflrt0OrZTEwRl49n4UpYuNnwYRhHs6ZIfcxpmE6Qd4nfOIiK7kM_CINCHxuFkJtj5tuIZuDaKqwpa0wEpzw3eZRjfrzzzhX-3JVxHyzfzwt5cmkbFmZm73mrddf52BHBVl5rVsW06-m-5W0gPbr6wRlsLnjKWfSvWwN0be7QOJP7imBAwHMPDJ4voKJ1CTsO3xVLA_IDEoYAuNqcSjl0g9t4Qti4c5g7tRkxT9wPELTweA0Y3v6TdouRuO-W-9NaT1nLXJfdAn25Lqn9jUsVyfHpmyM9Dh72NS4sD9A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d988cc6faa.mp4?token=kbz_Shmuq78nRQ0fCfj_bqphJmE42sco-ycBLfCZ7RR3z2fflrt0OrZTEwRl49n4UpYuNnwYRhHs6ZIfcxpmE6Qd4nfOIiK7kM_CINCHxuFkJtj5tuIZuDaKqwpa0wEpzw3eZRjfrzzzhX-3JVxHyzfzwt5cmkbFmZm73mrddf52BHBVl5rVsW06-m-5W0gPbr6wRlsLnjKWfSvWwN0be7QOJP7imBAwHMPDJ4voKJ1CTsO3xVLA_IDEoYAuNqcSjl0g9t4Qti4c5g7tRkxT9wPELTweA0Y3v6TdouRuO-W-9NaT1nLXJfdAn25Lqn9jUsVyfHpmyM9Dh72NS4sD9A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ایرانیان وطن پرست سنگ تموم گذاشتن و اینقد پرچم شیروخورشید زیاد بوده که میساکی فشاری شده و پرچم جمهوری اسلامی نشون میده میگه این پرچم ایرانه.
@News_Hut</div>
<div class="tg-footer">👁️ 8.38K · <a href="https://t.me/news_hut/66277" target="_blank">📅 11:05 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66276">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/944350c2ea.mp4?token=uaMnEDLyFA2TE2NUJF4CQweqOKdBq0_oCt3Tu2jgCsEriQrzI0t6V6xL7YBRga_VvUO1fPrDSm6sGzVd7zaXR52FtQG5kgLB34z8u_2PnGLDUYLA6Um_cwfQibSLaufRFWOj-7Be05gwkK8hkGOPyM6Ql9vouSHGtanEVGSIxlivmv2jkEV4UnE4IZyGhBLUNqnvUfgnVQnDeNM1br6w3XZ3y0wJvLQSknPDjxhAo6BvInYQRPC3TwmLRQtH_8bzLWC2NHicZ_H-_BorevMHFZEir6y_EbDRpAPi7XZSxtjpLfKIbtYZ5xc9MOe3EZNDtA-jZdg24OqjyR0PKuqZvw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/944350c2ea.mp4?token=uaMnEDLyFA2TE2NUJF4CQweqOKdBq0_oCt3Tu2jgCsEriQrzI0t6V6xL7YBRga_VvUO1fPrDSm6sGzVd7zaXR52FtQG5kgLB34z8u_2PnGLDUYLA6Um_cwfQibSLaufRFWOj-7Be05gwkK8hkGOPyM6Ql9vouSHGtanEVGSIxlivmv2jkEV4UnE4IZyGhBLUNqnvUfgnVQnDeNM1br6w3XZ3y0wJvLQSknPDjxhAo6BvInYQRPC3TwmLRQtH_8bzLWC2NHicZ_H-_BorevMHFZEir6y_EbDRpAPi7XZSxtjpLfKIbtYZ5xc9MOe3EZNDtA-jZdg24OqjyR0PKuqZvw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
دلیل سود نکردن من تو بازار بعد چندسال
😂
.
@News_Hut</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/news_hut/66276" target="_blank">📅 10:30 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66275">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/78c971246f.mp4?token=I0D4yI8qp3xJP1wcIh0GvWfsyMgmGAqaseF9kjRtCaW6PohNi4qOGjLZdtO4SM-DmK8a39rZFMHVUNbtqfAQoqMWSWMY7Q1ZbhcPDfVQ5SaJ_EB5Nu0OZz2sBXinkU2qHfJClfoATkS7AhV2xDbZIBnuWWXv7MgMJxOjSkqc7wxC5piEudHMIUvHma41NRDV2YNKKJVYGt_A1zRgauGMkmI4e78MIY5CDFGRyeEzGZGYUSNnJ_gnK54YkUUqHIjPDlQ2UhDFNVTc8pL8j2H14ZTwgW3n-hwX6uxerz_ZtJlfLvPaiFp2aFWIEwcFbir1jnVpcJd3ZEcvA67Dvn4qeQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/78c971246f.mp4?token=I0D4yI8qp3xJP1wcIh0GvWfsyMgmGAqaseF9kjRtCaW6PohNi4qOGjLZdtO4SM-DmK8a39rZFMHVUNbtqfAQoqMWSWMY7Q1ZbhcPDfVQ5SaJ_EB5Nu0OZz2sBXinkU2qHfJClfoATkS7AhV2xDbZIBnuWWXv7MgMJxOjSkqc7wxC5piEudHMIUvHma41NRDV2YNKKJVYGt_A1zRgauGMkmI4e78MIY5CDFGRyeEzGZGYUSNnJ_gnK54YkUUqHIjPDlQ2UhDFNVTc8pL8j2H14ZTwgW3n-hwX6uxerz_ZtJlfLvPaiFp2aFWIEwcFbir1jnVpcJd3ZEcvA67Dvn4qeQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
تصاویری از پالایشگاهی در حومه مسکو که در اثر حمله پهبادی اوکراین دچار آتش سوزی شده.
@News_Hut</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/news_hut/66275" target="_blank">📅 10:05 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66274">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/696afa1a70.mp4?token=OYUHcBZdx5obrgNIl9jOcoLcBHD7rWdvQ5gqEy8Xwd4mnuBI9whkGVAMXPVV9W5hg9RlmppiD9pnr4mcn5yITR3qNxaGSv1nLFSnQppMNLHLVYUr0ghJGJyGgz9sOa3y69NfvlPGOy9Kis6JCla4rYJZva1sj_AoVuEqwgJbLzWTL3PFYTw0T1gB-KVA7XG0NdmBRZe809w2L5MAU1wWJfFI8L2SPRBEFwUk0qLorALyKVcNNP7MlwTJoDEMpQhTEuURHBK2RHfU-N-y4l3dXMrmawoKQB3c5bvBhRO-uNky_x6fRUOFN6SdN7wMFVVP15FWhCyDEiNxWuGTV4JefQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/696afa1a70.mp4?token=OYUHcBZdx5obrgNIl9jOcoLcBHD7rWdvQ5gqEy8Xwd4mnuBI9whkGVAMXPVV9W5hg9RlmppiD9pnr4mcn5yITR3qNxaGSv1nLFSnQppMNLHLVYUr0ghJGJyGgz9sOa3y69NfvlPGOy9Kis6JCla4rYJZva1sj_AoVuEqwgJbLzWTL3PFYTw0T1gB-KVA7XG0NdmBRZe809w2L5MAU1wWJfFI8L2SPRBEFwUk0qLorALyKVcNNP7MlwTJoDEMpQhTEuURHBK2RHfU-N-y4l3dXMrmawoKQB3c5bvBhRO-uNky_x6fRUOFN6SdN7wMFVVP15FWhCyDEiNxWuGTV4JefQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
هو کردن هوادارن حاضر در ورزشگاه هنگام پخش شدن سرود تیم جمهوری اسلامی.
@News_Hut</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/news_hut/66274" target="_blank">📅 09:31 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66273">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/44f96ea995.mp4?token=IGwXKiunaLt8egegqeXFNEkymOfkpaWWBq_qGVbdU45fPjjWA8Ct2kx4BkSMs_pOKqMmyxE_xGRZt3f_01I1dpG361If0ckoBEajxTLZWuVDWT2neikHBh9R4n3G-zVC6aSc6lFa10OVQN4y1jTDTJHBvFoJyRkbZBMo_ctfqqCVzHzNZO3r1qgzlVrLtiGbVTwzLDeLMcQnsTrHFfPRhUuQNRW_UOznLHGP3jjsC2Ex97JPrS9-4F3plE_qlc934ab3fFsw_hVdOYDCh2PA4yACwHa8glaxbFg4Q2B80qtnmEGGbi2hLxtcRr96nSd93hNPiQ5ttlKWN5LHYi5DYw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/44f96ea995.mp4?token=IGwXKiunaLt8egegqeXFNEkymOfkpaWWBq_qGVbdU45fPjjWA8Ct2kx4BkSMs_pOKqMmyxE_xGRZt3f_01I1dpG361If0ckoBEajxTLZWuVDWT2neikHBh9R4n3G-zVC6aSc6lFa10OVQN4y1jTDTJHBvFoJyRkbZBMo_ctfqqCVzHzNZO3r1qgzlVrLtiGbVTwzLDeLMcQnsTrHFfPRhUuQNRW_UOznLHGP3jjsC2Ex97JPrS9-4F3plE_qlc934ab3fFsw_hVdOYDCh2PA4yACwHa8glaxbFg4Q2B80qtnmEGGbi2hLxtcRr96nSd93hNPiQ5ttlKWN5LHYi5DYw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ثابتی نماینده مجلس:
عراقچی نوچه و اراذل اوباش آمریکا در کشور است.
@News_Hut</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/news_hut/66273" target="_blank">📅 09:01 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66272">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JWeYWhsk020aTnvipDsL3K8BdUE6Yd5ODW3x_mfNgMs6Hn-xWgbliQvbTG1s7GIs5fc6bPa7Zn3pGLDfZ3k09DzwemKdpWjvAxlJmiWHKi31SMxyLvrk8a_fkzimyQ21c2KwNUZlo_fBkXb-mojglkaN8nmlZX6CO8d0mHnJ-bDk2VREXH_4rlhFSvFTpp66aAyxrGAwfC9V62J-YWc23BKoEzpXoCaauvFJXJ3YImBGUtOvFraIBWTPX1XmwSosIzZoi3Z-c2nUaI5rBmu2qNXHEOtnTcLNAdVLKjJurYHV2dHdoSonejQOY1CAxLHEMdp8IdkqRtrqgsWTVP4tdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
🏆
پایان‌بازی
🇳🇿
نیوزیلند
😀
-
😀
ایران
🇮🇷
@News_Hut</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/news_hut/66272" target="_blank">📅 06:38 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66266">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">گل دوم محبی
#hjAly‌</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/news_hut/66266" target="_blank">📅 06:01 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66263">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🚨
🇳🇿
گل‌دوم نیوزیلند به منتخب ایران دقیقه ۵۵
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/news_hut/66263" target="_blank">📅 05:55 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66258">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">🚨
سخنگوی قرارگاه خاتم‌الانبیا: گل زدن نیوزلند به ایران قطعا بی پاسخ نخواهد ماند
@News_Hut</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/66258" target="_blank">📅 05:34 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66257">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">پایان نیمه اول
فرزندان برحق وینتون روفرو ۱
کاکولد های گروهبان قندلی ۱
@News_Hut</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/66257" target="_blank">📅 05:26 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66255">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">یه حسی بم‌ می‌گه بازی مساوی تموم می‌شه
#hjAly‌</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/66255" target="_blank">📅 05:11 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66254">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🚨
🏆
گل‌تساوی توسط رامین‌رضاییان
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/66254" target="_blank">📅 05:10 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66251">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/njDHnPrK7fMTOzwJJXrDBkpZfBR9Vt79Ha-pxFH-0qw2IFEf9du4Q1EyG97sosnPBmHrxVLAKbORmrmeVukHjI7D3PrfpvHeSb7EmtasbQmCa2Z8Idal8V8uZIKyoH8P3RvPbZaMq8PXDEWo6z3epymUQIKI-RZrhMUFZWls6PN5_LZWkEc3ctDND9opFl7H7auEqrkwjc4DzkeySLWNy26XD-w2iwXNUqSJhj68Gkuz5Grh2mslXyD4H5xszc7oW5QFvl7TSYZ8s1lhDNfJfANGwTMt6RMbzzKbUY7Hgps5HRNwqnhiwEvvAaQOhHClTeswHSewtugvTQ6QxCQPbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لحظه بازگشایی تنگه بیرانوند
@News_Hut</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/66251" target="_blank">📅 05:04 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66248">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🚨
🇳🇿
گل‌اول نیوزیلند به منتخب قلعه‌نویی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/news_hut/66248" target="_blank">📅 04:45 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66244">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-poll">
<h4>📊 دوست دارین کدوم تیم ببره؟</h4>
<ul>
<li>✓ تیم منتخب امیرقلعه‌نویی🇮🇷</li>
<li>✓ تیم ملی نیوزلند🇳🇿</li>
</ul>
</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/news_hut/66244" target="_blank">📅 04:25 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66243">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P2cyxvU3eQRZXB3phKAU8a4D2bR5BdlosbIIMB8RlsBD9bDZ5YANjuqz1npDroxtpFDgG2zGhFXS_mx0Ikw_RCY7TJwxxfMvx5ssAXtaTx6GmnFw76bRnupp4TvR97sVGPFGz9KiHe8AuBvJW7D6xU053YqVXNit4Er_KwN1-JKSZ2Z-YxvLraTbFJfp81KvU1JPoBL_h2JjxmJCQ_L9SFPlUqMRxmGgrTc-_MYVb_P5lZEeOQ5wHed-yqyn1uKs9kD_0FdO4WdhpP2IlyGHf2CJ1tRl51tF7R_1smFiGu39S-6g6i88-_6GTCaDysFYRMEsES-FjW4V8cIwG_iMPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قبل بازی
@News_Hut</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/news_hut/66243" target="_blank">📅 03:50 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66242">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">حاج علی یکمی تحلیل کن</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/news_hut/66242" target="_blank">📅 03:45 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66241">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAmirhossein ؛)</strong></div>
<div class="tg-text">حاج علی یکمی تحلیل کن</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/news_hut/66241" target="_blank">📅 03:44 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66240">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🇮🇷</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/news_hut/66240" target="_blank">📅 03:28 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66239">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🇮🇷</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/news_hut/66239" target="_blank">📅 03:27 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66238">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/a-T7nqDgQgiUUsnWT7n-p3lbPz_X_vRKqsQ8gXL0tPPqlTvovwGZh8lKuO6xLnIzjL6OS1pOd17lx6Sz9TXYrZTZjZI4Vzc7JQt34WgEp7kj_OBzobo4xKNW91CySVp57ANcMAKqFyHK6Atsl19d79bAUF-o5aaDpK5qngYPVtHjRR_NJhbpH2R_A6rASsrwUMZkF3VdqUvS1udN3C5jK8vaBhlzDmEtuiqDRZwfKRweaZ9kVmbfYUlnWd30kpAuOnZo2xBuyZBeDx6HamQKPsxR3MNDUCFmN1_LPnjtYci3EAyFs74yaJAMk_xB8sq11NXyQGmqO_Gr59vnydRA1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
👌
تصویر تراز امشب:
@News_Hut</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/news_hut/66238" target="_blank">📅 03:21 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66237">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
صحبت‌های ایرانیان مقیم آمریکا قبل ورود به استادیوم
@News_Hut</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/news_hut/66237" target="_blank">📅 03:07 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66236">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AKT7v87L_L3zQigWSxFwbDTaudfLpvEo3aI21H14PdkgMN2n33eC2Hj_MFWGTSWVLCgRe4p8VmeXgaMN9j0yTdLBOiq-B-eguSdAE8HCmJUJEdZIf9ClTfzA-2L57Bx6mx8Ts3ycDm-1GI2REP8AkqNJcRX118adSNR1jCFjDwIdu9woZUdaFeDbI9itx9JyV-jkGu1S9Hc_jj28wQSt4UulBwgnwVs4JBhzhjr2VT6m2mwvst9NM3Zq5kRAUgj_KXUAEobores4MTFn5h49yWU_T9_Nn3EJ_mFlu4RLvGVNg1SV_lIx8AexBnpC2SLm7gkiYKSX3jSqe2Ciyn5eGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تیم ملی از اسمش مشخصه، باید برای ملت باشه، من نمی‌تونم رو این تیم، پسوند ملی بزارم، یه مشت آدم منفعت‌طلب جیر‌ه‌خورن که برای ۱۰ دلار بیشتر ناموسشونم در اختیار ج.ا می‌زارن همونطور که تو ۲۰۲۲ وقتی مردم داشتن کشته می‌شدن اینا دنبال حواله خودرو بودن.  آخرین باری…</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/news_hut/66236" target="_blank">📅 03:03 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66234">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c366b2c0bb.mp4?token=pqTeHLWevD4fPsAhIdg1HdckOBRsskZ4x3hPdqZSxbPEja8ua40VRExfRgbxnTePtq1BbfVBvh2yvzkKnEguQmT8GjMingpsKVFffycFSSWnxxm-EoYG-xqIPGOFJvuLszMC-uZIucaLWC-Q9OGstBkd1SLG_Fi_Yxy-f1_nUJKfK72IVfsznqemmSzIURYqXnFIsmsqY_NiG01gzhNihcSt8T7uecH0Y3bkyQUZq8JYL0blqJZyaa_lwFUHHqeWMwLmIIskkoFQP6q6XwazexnYw_0KEX8KHd2X3ZpZOO-cs5ASeIRE8QGH1cqEaigR7tDd52VNuBAq9DB48rJPuQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c366b2c0bb.mp4?token=pqTeHLWevD4fPsAhIdg1HdckOBRsskZ4x3hPdqZSxbPEja8ua40VRExfRgbxnTePtq1BbfVBvh2yvzkKnEguQmT8GjMingpsKVFffycFSSWnxxm-EoYG-xqIPGOFJvuLszMC-uZIucaLWC-Q9OGstBkd1SLG_Fi_Yxy-f1_nUJKfK72IVfsznqemmSzIURYqXnFIsmsqY_NiG01gzhNihcSt8T7uecH0Y3bkyQUZq8JYL0blqJZyaa_lwFUHHqeWMwLmIIskkoFQP6q6XwazexnYw_0KEX8KHd2X3ZpZOO-cs5ASeIRE8QGH1cqEaigR7tDd52VNuBAq9DB48rJPuQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
تجمع هموطنان خارج از کشور مقابل ورزشگاه محل بازی تیم جمهوری اسلامی:
@News_Hut</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/news_hut/66234" target="_blank">📅 02:59 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66232">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XzDWZFqw_64tQ1OxvKsyOepW48DHJqCSoUwtAyVTG4VP3fbD82N30UFL-ekpjk9euYBkTi5ZtE7mpxZiJNeccUi8X7hB9BnJEdDEtbejcYK5-62wKx4ITYt6vU21-d-85Bz5wObKHUnJQQ5rud7B5hErss-dhaebZhgVB7XsYiPYAtlrTFiGUv-MoZDXN4zJ3XcxcvvGh5AUq5_4lHqJrbs5wWnVo1ZfpXLlEHIJfMSC_l0LhmtZTw4hBjx_R8L4kOysgBz9kvE6INX2Yb0scLNpy4wt5AnRjGt1w0Pb-sZY6MHbD1qbc-GiBwqnP7pXstkejOxsNx6-xoNXK4GVkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تیم ملی از اسمش مشخصه، باید برای ملت باشه، من نمی‌تونم رو این تیم، پسوند ملی بزارم، یه مشت آدم منفعت‌طلب جیر‌ه‌خورن که برای ۱۰ دلار بیشتر ناموسشونم در اختیار ج.ا می‌زارن همونطور که تو ۲۰۲۲ وقتی مردم داشتن کشته می‌شدن اینا دنبال حواله خودرو بودن.  آخرین باری…</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/news_hut/66232" target="_blank">📅 02:57 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66231">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🚨
🚨
#فوری
؛ترامپ:
ایران موافقت کرده که هرگز سلاح هسته ای نداشته باشد.
همچنین ادعایی مبنی بر اینکه واشنگتن مبلغ ۳۰۰میلیون دلار به ایران پرداخت میکند جعلی است و توسط دموکرات های احمق تبلیغ شده است.
@News_Hut</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/news_hut/66231" target="_blank">📅 02:57 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66230">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🚨
🚨
🚨
صف ایرانیان مقیم آمریکا برای دریافت تیشرت مخصوص ورود به استادیوم که تصاویر جاویدنامان انقلاب دی‌ماه روش حک شده  @News_Hut</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/news_hut/66230" target="_blank">📅 02:55 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66229">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d10adb291f.mp4?token=If8fHKeazc7JSpEIt1DGCcp8JE7fwIp2AQgA0tnnR3SD4b9aoq9ZD4C_cPhO7wMxbjmOGzDnhzCyWp7JHx2e2Fz3tJJj-rHR-pxLDmScgMtS1b1Iq-T2nh6mAxa3uPPIQecHgmaq-8ogCPBLoGuWUSpSA5dYHjBXtagVJP6n7yCLHP7BymHZY_JFvQ0T41lfIfytwRqvZlzrycSpL7YOKutT99XsSm7wVmrpD7aBJ8vXaCrSvLKyI36ExcZ1KrmQxgytHCEbdXoW_01XTqJuTPb8U_I0LoQDMHVlYxq2-uvE3JFFYCrwJIWz2dr4bbYncE-jtFJFAr5ObEDhiSt6vw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d10adb291f.mp4?token=If8fHKeazc7JSpEIt1DGCcp8JE7fwIp2AQgA0tnnR3SD4b9aoq9ZD4C_cPhO7wMxbjmOGzDnhzCyWp7JHx2e2Fz3tJJj-rHR-pxLDmScgMtS1b1Iq-T2nh6mAxa3uPPIQecHgmaq-8ogCPBLoGuWUSpSA5dYHjBXtagVJP6n7yCLHP7BymHZY_JFvQ0T41lfIfytwRqvZlzrycSpL7YOKutT99XsSm7wVmrpD7aBJ8vXaCrSvLKyI36ExcZ1KrmQxgytHCEbdXoW_01XTqJuTPb8U_I0LoQDMHVlYxq2-uvE3JFFYCrwJIWz2dr4bbYncE-jtFJFAr5ObEDhiSt6vw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
صف ایرانیان مقیم آمریکا برای دریافت تیشرت مخصوص ورود به استادیوم که تصاویر جاویدنامان انقلاب دی‌ماه روش حک شده
@News_Hut</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/news_hut/66229" target="_blank">📅 02:52 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66228">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b0QWKxlURGJ7FkWuRPhf2F8pQ9Ej_j16kWUP13S9W_D6rpBhUMnwSdg7414oznakqkqtGaZdPlyHnlZLMBbuQjaeHp3DJ7BLO4a3j96fPQMLSFvjF79UcPDys2FCMTcXUzMgFrWV3VVL29tXIefnUbUrhBME7ntXpsm-pBhsE7yEdN2WrLFM-vDLEvFcDRGxVq4qjF0v_UQouTCFy245Nii91eu_bQJOam7jBZA0xXJn5W3UUYjmhyLq9bSCsDwcC00pK6Wlyu5Ab5iu7sfx3iAfpuYeC0cy7Byhmy39LbaoSdufqQVa6kq_JWbdHL9Yh_EGLevAoileum06MqTZoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
باراک راوید:
رتکلیف، مدیر سازمان سیا، به رئیس جمهور ترامپ و دیگر مقامات گفت که اطلاعات جمع‌آوری‌شده توسط ایالات متحده، تردیدهای جدی در مورد تمایل ایران به دادن امتیازات هسته‌ای مورد نظر ایالات متحده در هرگونه توافق نهایی ایجاد کرده است.
@News_Hut</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/news_hut/66228" target="_blank">📅 02:17 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66227">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ByUG0ysWKL5E_DhoxzrScTQVFR9kfv4ivFplsijykqo-fJqNLXE8wA_28BcoLDPsiDtq5VCedbTI1WwccaTYAjd6jVeH2C0juVYFU5eoPAR0eCw4C7MJ16yKc8vBcpeYHQAtTDrZTQ5oc72--5uKFsl9mgl5VxXQJOu8BJCgcV6HbqoKDV9jhj_OxohH2mk_ojh5vwy_3rGfSpmfbldPHElkMPWwpVz0OkSNJKIihW3rlD8y4f0Ur93ehFT3R9nHtp72t2ncYobVRJhc00sM9O9eMMsUOQrq1sWhs-XbPSAPIJf2qdExZlD4AhiZqgCpiuQnbXzaiCdA8uRDAOQOIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
فاکس نیوز:
نیروی هوایی ایالات متحده روز دوشنبه اعلام کرد که معتقد است هشت خدمه در پی سقوط یک بمب‌افکن B-52 اندکی پس از برخاستن در پایگاه نیروی هوایی ادواردز در کالیفرنیا کشته شده‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/news_hut/66227" target="_blank">📅 02:04 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66226">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">‼️
ونس به سی‌ان‌ان:
یادداشت تفاهم با ایران حدود یک صفحه و نیم است و به همین دلیل یک سند عمومی محسوب می‌شود.
@News_Hut</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/news_hut/66226" target="_blank">📅 01:54 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66225">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c31d4a9328.mp4?token=jhY_n-hn2gTPMPNM-p1USkrjezhC5H_TvwRnZotSng-ueTZzfquytXU0L7uBwMgxxmVpE4XJKa_6oNpZdSllBUNLOU68SAIyp2dYzH7xKO9Iam1S18T_XaWGVWVUhp1U4riD9WOznAX-7z02YGsfbJvLBTuVRjOpFlGjCrzZbpnhDDMYVi6kBvwZ61ECH-rPGX8nzWkEmypEfl--LxbeUdc074mMbwHid3_Ncz59AXMrrFZkgwGvz-18MqSQv92ImDlXIdNneD859w00kFwdOGdGl0jcopg9RQacTHtJ6Z3OQqDMxVcynBGv4v4eN6rhSgfuaPsWsgqk5lViXkO5bw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c31d4a9328.mp4?token=jhY_n-hn2gTPMPNM-p1USkrjezhC5H_TvwRnZotSng-ueTZzfquytXU0L7uBwMgxxmVpE4XJKa_6oNpZdSllBUNLOU68SAIyp2dYzH7xKO9Iam1S18T_XaWGVWVUhp1U4riD9WOznAX-7z02YGsfbJvLBTuVRjOpFlGjCrzZbpnhDDMYVi6kBvwZ61ECH-rPGX8nzWkEmypEfl--LxbeUdc074mMbwHid3_Ncz59AXMrrFZkgwGvz-18MqSQv92ImDlXIdNneD859w00kFwdOGdGl0jcopg9RQacTHtJ6Z3OQqDMxVcynBGv4v4eN6rhSgfuaPsWsgqk5lViXkO5bw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خامنه ای خطاب به قالیباف و عراقچی
🤣
:
@News_Hut</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/news_hut/66225" target="_blank">📅 01:40 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66224">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8b930a8766.mp4?token=UPzsY3M69yIdr3u4Op-jT547RUWkPndU5mSabv9ylxWFO-i0joMtpsuKfthbRPshqtnUm-3dMnsQ-kO6mU1YblVHQXEc-phiKx7F0eBzO3okGRRRC4eXo3u_B8VW2-lmQFplc2bMAQUnXH5Zf0tMp3ED-kKfO9EO74dpA1pysl95iiEJAee-kMXUsXRr7WTuu3LzWb9e86Unkiaz8Pdi0M20X402WbyOJz9KPkLO5sKmgwFv71rTFV7ai9_ahE802Lwq_yMtxzt1vRim2FZCHSX1ogP7IELFb8LgkpvmT2mrBdGF-GjHadKPcJkW1f7lyPzVTr8d9Ue2Skj9MYsAcw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8b930a8766.mp4?token=UPzsY3M69yIdr3u4Op-jT547RUWkPndU5mSabv9ylxWFO-i0joMtpsuKfthbRPshqtnUm-3dMnsQ-kO6mU1YblVHQXEc-phiKx7F0eBzO3okGRRRC4eXo3u_B8VW2-lmQFplc2bMAQUnXH5Zf0tMp3ED-kKfO9EO74dpA1pysl95iiEJAee-kMXUsXRr7WTuu3LzWb9e86Unkiaz8Pdi0M20X402WbyOJz9KPkLO5sKmgwFv71rTFV7ai9_ahE802Lwq_yMtxzt1vRim2FZCHSX1ogP7IELFb8LgkpvmT2mrBdGF-GjHadKPcJkW1f7lyPzVTr8d9Ue2Skj9MYsAcw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
حرف های متناقض اسماعیل قاآنی
😂
@News_Hut</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/news_hut/66224" target="_blank">📅 00:57 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66223">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/news_hut/66223" target="_blank">📅 00:57 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66221">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromProxy MTProto | پروکسی(|•𝓗𝓸𝓼𝓼𝓮𝓲𝓷🥀•|)</strong></div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/news_hut/66221" target="_blank">📅 00:51 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66220">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">‼️
قاآنی فرمانده نیروی قدس سپاه پاسداران:
هیچ کس نمی‌تواند در مقابل حزب‌الله در لبنان بایستد و هر آنچه از حزب‌الله در لبنان دیده‌اید، تنها نوک کوه یخ است.
@News_Hut</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/66220" target="_blank">📅 00:11 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66219">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2752783b15.mp4?token=t0BYKCKSxCW-GPeAeflSTECzf5B4sMPRjRc9M5AgqqRhqIu46KemUSVNd0f2GDSWcy7G8bzmJ-cadKCyiyn9n2g8tZq4ep422JppHxoB-0M_iYpIOPsBcdhhOO1HrzUz_U-907deGXmPg7gnSvhEoEi3Sb3BIvIuDsFGzX2qCoJULpKWRIVJP_yBOlvmzcHXKxGGnjPdKdBp3p_aLejenoQ-uIKzgsiOFnTCdJwa_I-CB4jzGhGs1oPzArzqQ8UpD1aYxQwi9I6AhFDGObDRLt_Qmhb1PlM2RpfZzELfsNslaUQ2Ul8CZuBA4IOZ1ZNnfniyHfCmDm2HD52Hyp_64Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2752783b15.mp4?token=t0BYKCKSxCW-GPeAeflSTECzf5B4sMPRjRc9M5AgqqRhqIu46KemUSVNd0f2GDSWcy7G8bzmJ-cadKCyiyn9n2g8tZq4ep422JppHxoB-0M_iYpIOPsBcdhhOO1HrzUz_U-907deGXmPg7gnSvhEoEi3Sb3BIvIuDsFGzX2qCoJULpKWRIVJP_yBOlvmzcHXKxGGnjPdKdBp3p_aLejenoQ-uIKzgsiOFnTCdJwa_I-CB4jzGhGs1oPzArzqQ8UpD1aYxQwi9I6AhFDGObDRLt_Qmhb1PlM2RpfZzELfsNslaUQ2Ul8CZuBA4IOZ1ZNnfniyHfCmDm2HD52Hyp_64Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😂
😂
😂
شبیه سازی سیستم عوارضی تنگه هرمز:
@News_Hut</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/66219" target="_blank">📅 00:00 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66218">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f287535d76.mp4?token=dBQW6CIO8h3awS9GF6FKVF8fwCJadHzGi3TyM1zs5DaWzjRwCo68XnL3IqTHu5b_e7blUy08gUeUUmSfQY_gr-GfSUpUl_kFMtUYjAqk0u03Hq4WjNXPW_nCpy_Gq2Q60OYNFPMkpzGjxM-bXgjK5B-0rvH2i56xgcExqOJPFGFnwPGYdIY92mQOIH-qVi-YT7rIobs_OP1pl6rYyK7nhn5SM5DzGsDtpE_Nqq947_zbvewkoq9e9XygBE2q70qXIRiibaIVK1mXzdPTN_2dow8dwVFMO7Bi9nRv0h6se2AcwIMfW9NnLURlTeDoo-9FPx-lMGvta95FEBOnUIbFlw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f287535d76.mp4?token=dBQW6CIO8h3awS9GF6FKVF8fwCJadHzGi3TyM1zs5DaWzjRwCo68XnL3IqTHu5b_e7blUy08gUeUUmSfQY_gr-GfSUpUl_kFMtUYjAqk0u03Hq4WjNXPW_nCpy_Gq2Q60OYNFPMkpzGjxM-bXgjK5B-0rvH2i56xgcExqOJPFGFnwPGYdIY92mQOIH-qVi-YT7rIobs_OP1pl6rYyK7nhn5SM5DzGsDtpE_Nqq947_zbvewkoq9e9XygBE2q70qXIRiibaIVK1mXzdPTN_2dow8dwVFMO7Bi9nRv0h6se2AcwIMfW9NnLURlTeDoo-9FPx-lMGvta95FEBOnUIbFlw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
عراقچی:
جمعه در سوئیس تفاهم امضا می‌شود و پس از آن اولین دور مذاکرات بعدی را خواهیم داشت.
@News_Hut</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/news_hut/66218" target="_blank">📅 23:49 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66217">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">تو فاک بت یجوری وین میدن انگار بت زدن ساده ترین کار دنیاست
🔥
از جام جهانی تا تنیس های کصشر دنیا !  هیچ فوتبال و ورزشی و از دست گروه انالیز حرفه ای ما در فاک بت در نمیره !
💵
@FutballFuckBet
💵
@FutballFuckBet
💵
@FutballFuckBet</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/news_hut/66217" target="_blank">📅 23:49 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66216">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/djHeIdWuKXcbl2nVMMVRL5nhF7CPREC07yz9OuyBRmKQKC8UhcVSqGok7E_4rnTvQPA9VjPBDxwrO1N7jrg2RRe9QWMHxeAsxOToeRYlbtzeWMlBVstM5-IgoHhp8fVPOBHLlnWKCGqsOPncxDB51KsTbq1KkwYvzUBMSz10kKnFyS1wv3BXIh8j9G7wxl1-kjvjdPSmZAsLEzhRZLUbil4ju67L2ia4rzon1bFy6TtuLM9LMgV9M_jDhdxH4QGPnwg0IsBC9AxFQJwBWmOqHnTDajamzbjQYqz9V4oIe9a_ajrZ3ozA9rMmxlUQmNjLyxj-AHujM7NngFeWxDHcMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تو فاک بت یجوری وین میدن انگار بت زدن ساده ترین کار دنیاست
🔥
از جام جهانی تا تنیس های کصشر دنیا !
هیچ فوتبال و ورزشی و از دست گروه انالیز حرفه ای ما در فاک بت در نمیره !
💵
@FutballFuckBet
💵
@FutballFuckBet
💵
@FutballFuckBet</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/66216" target="_blank">📅 23:49 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66213">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Oh1vqstunqHlsh4XqVltuG6-MY9gFJxKVT-GMTO5GQzB_oQ3h993QMjbyG2YS3MlReu17tbh02Anc_gAhVCjx1sD1poBQxB_46NLSCFpgETa-7D8bVRWYf-p5C7KWYlzmRHTHJuQBdNRM2hKQJ7U6K7tqCLd7psx_HckooOQcTIhyl7-VoiFVuBkcj7tDNjT29xYiXZBcEHrVt-zPPECyxDLnxJHx3ffwpsGKaTIS70bgE536dAym7b3VX0DGIzVSG9NEC74gBHYx0yJbut1jzGEUaJuWEDusLYNmT63ClaXJ4Tf3bzel1It6Rktmig02YJX20RS3OrX6X4t9YnFZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WIZq2Q0G93_SpTAi0k6NrkaVw-REreilue61otD3ACkbjrcD5qpUGR1wX5x1jfIeagqWpOFcoPtNAJXoGF74O-T5Ye4FEZUzlkQk-yjKjTrf8ULhddFSMhalqlcH482I8RckDBQkyyqfDQjMDrsJ1ToJnNiEAzdw4vD2w-fFWx-ClQQ2t8du-AfuFzP_4Udo4B1Fly0NIXlQ6sxHFq8EH4s9FdABzxOllQINzPj2RxltoF45M4WnTR0rm6EyTjxjAEIKRQjVSECSAvOKg8P1M6Fb_K0meD0lB9jcgU8VjjARqFfKakMbG41CJthM0l3o3TmgojagwwxJa2zVx8BpZw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/df8fefe1cb.mp4?token=Xzcd1k2kxvM5K2wgBe3mmBQ4txYMwmgXc_9y19_JnXdZ1WBvVizBchs9hd1Y49kfKvaZ15R__TQXZ4_V9iceTuJj_5TR2W9tMb-hrd4osOM4L4AZ8SzaLufA3iDnUohgUchSb5Hfkk_TUsDa75v6c4-xaMJb2fsPyFrMUoMulOsjlsewmOt_J1H-ZzAq3WcYsHgDaW1FgSG_5U6vROJGEkjcbUsk1LC6DECI5rB6YzkHQ20lixVC-wpYQyg4pWG4FXVVTSjs4Fs2D92C7nEAFzL_QlVig15O_0YCZ3e0WUChrAaaPlGtGza-QNigyKuEC49h1tUiYx6cuYBNVQ9eLQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/df8fefe1cb.mp4?token=Xzcd1k2kxvM5K2wgBe3mmBQ4txYMwmgXc_9y19_JnXdZ1WBvVizBchs9hd1Y49kfKvaZ15R__TQXZ4_V9iceTuJj_5TR2W9tMb-hrd4osOM4L4AZ8SzaLufA3iDnUohgUchSb5Hfkk_TUsDa75v6c4-xaMJb2fsPyFrMUoMulOsjlsewmOt_J1H-ZzAq3WcYsHgDaW1FgSG_5U6vROJGEkjcbUsk1LC6DECI5rB6YzkHQ20lixVC-wpYQyg4pWG4FXVVTSjs4Fs2D92C7nEAFzL_QlVig15O_0YCZ3e0WUChrAaaPlGtGza-QNigyKuEC49h1tUiYx6cuYBNVQ9eLQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
گزارش‌ها از سقوط یک بمب‌افکن استراتژیک B-52 آمریکا در کالیفرنیا خبر میدن.
این بمب‌افکن دقایقی پس از برخاستن از پایگاه هوایی ادواردز دچار سانحه و سقوط شد.
@News_Hut</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/news_hut/66213" target="_blank">📅 23:33 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66212">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMain Online پشتیبانی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y6jsAkb-dEmMxu0eALZDx86TR2bPeiJYZdd_idT0mQx6-phlGs5jYRo9sBrtanJLp0xyNwKyQp5cZwlaFzwoeCkPM6LxIZcEJwBpba7S8AdmTySWv45kj77N3uf2JN09X4wjORMKbVyS9cv4UUQC9hC_E2YDPq7coxCDWI3msbeYkhPtRzKhTBOR1Y2sm0DgVXCt35NC5po4qDlA8JkPCPJ1rdQxYe05iZ5XJfre5mIsFT7ENUqdmnG_86ZuzRrkgP9YzmYS6OYpr5_TCZH8bzobLwmIi9FTUkCozLF2DyyicyN8tL8MiYcSMmfIMJxXUOU8FYQ2NsVmWSY-SzJOtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
فیلترشکن فقط گیگی ۵ هزار تومان
✅
👥
| بدون محدودیت کاربر 999+ نفر
🔥
| بالاترین کیفیت یعنی تانل شده
🎁
| کد تخفیف : 50
▫️
5 گیگ 25 هزار تومان
▫️
10 گیگ 50 هزار تومان
▫️
15 گیگ 75 هزار تومان
▫️
20 گیگ 100 هزار تومان
▫️
30 گیگ 150 هزار تومان
▫️
40 گیگ 200 هزار تومان
▫️
50 گیگ 250 هزار تومان
⚠️
| تنها راه خرید مراجعه به ربات
🤖
| ربات :
@YOUPINGROBOT
⚡️
| ارزون ترین قیمت بالاترین کیفیت</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/news_hut/66212" target="_blank">📅 23:33 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66211">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/007bf57d46.mp4?token=u_dlhkx8qYd5SdP2OBY78wf37KKh4rxadJD45qCNhEOtVZ97KPbkT5aasZOJg0FgtCOK3F1njDKrGe0pPA7Hv7FdQvEjPo-6T4LbDwTTRGfN2h_M43e8DBzXXAsochG0nVOmlXHu69qj5ikzUJ9An-wEpPPw85ueAman_kn48mmauUsJlgJIKJZEeOJRP41StVO3cCSpow0r52YDZA8QndBgDxstWwxQ2sPPbjWL5Tasn9i43tTnulcUOtaioH8S_daSZwUnSMLkzyzgAmahaZ6zxIefVC65YK2FYmHvHCmYwvfICkG6wN3SoD2HQsf6IsgGsxjJ62Em6HggjdN-axHb82hkph0VJmgm6mF9yCCNwIsps2_L0oWLS4zMRnugDrJYc5RKiOUpJnXH2Jf3fRcN-pe31yD8JgLKeJL6IURqeMGsmwPbAx6mXNuG994XZqXr2kd1OdkeuMJs2P4FHIly64-eJgld1JfWBnlefkUvRHRBAa1u6BEQS6XfkGsadlEhynOig5kARs66152Eqyc64dbjdwe5XR2nE-FTKMm6NYjQ1cnPmLW0JcDce8LxAtBo7rLxDOEoogmVtA8YzLvXiYRX7ZKwPKXkGzI6Dc9bcyb3f4uPwoVQbCwtBwtgGejFcSpm5QLODrjpMlC-_LKL8GUTeYnxMH0Ek8ZrwZM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/007bf57d46.mp4?token=u_dlhkx8qYd5SdP2OBY78wf37KKh4rxadJD45qCNhEOtVZ97KPbkT5aasZOJg0FgtCOK3F1njDKrGe0pPA7Hv7FdQvEjPo-6T4LbDwTTRGfN2h_M43e8DBzXXAsochG0nVOmlXHu69qj5ikzUJ9An-wEpPPw85ueAman_kn48mmauUsJlgJIKJZEeOJRP41StVO3cCSpow0r52YDZA8QndBgDxstWwxQ2sPPbjWL5Tasn9i43tTnulcUOtaioH8S_daSZwUnSMLkzyzgAmahaZ6zxIefVC65YK2FYmHvHCmYwvfICkG6wN3SoD2HQsf6IsgGsxjJ62Em6HggjdN-axHb82hkph0VJmgm6mF9yCCNwIsps2_L0oWLS4zMRnugDrJYc5RKiOUpJnXH2Jf3fRcN-pe31yD8JgLKeJL6IURqeMGsmwPbAx6mXNuG994XZqXr2kd1OdkeuMJs2P4FHIly64-eJgld1JfWBnlefkUvRHRBAa1u6BEQS6XfkGsadlEhynOig5kARs66152Eqyc64dbjdwe5XR2nE-FTKMm6NYjQ1cnPmLW0JcDce8LxAtBo7rLxDOEoogmVtA8YzLvXiYRX7ZKwPKXkGzI6Dc9bcyb3f4uPwoVQbCwtBwtgGejFcSpm5QLODrjpMlC-_LKL8GUTeYnxMH0Ek8ZrwZM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😔
مصاحبه با رکورددار عمل جراحی در ایران: بالای ده میلیارد خرج عمل کردم که همشو دوست پسرم میداد!
@News_Hut</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/news_hut/66211" target="_blank">📅 23:25 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66210">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/64b5122b70.mp4?token=T6jWOuF1XaXpVUu6Hk0ocYWyvLg-c5geFydFTx321CO7PeTY_LRbgHrMk5V2wvS9b_q-hL__04Wfb6uSLITW52KwuAcEwuAC75xO5_eSU8zg_RiOwJCdt403BBsL89BlZifb8KROaJ6cjGRaKGLZG7_56QIFOolk_UZmGp3m7HmsFddGOOHsjUYBPB8pIdrROBpSzBBVZCZ0JpJeR9nmAYvGuHpbHKn7hFHvSjPD1TTHB2voz81aR_yy5V-BGm0ogp1ZIM3fRGfQWw52R8BXGe2jpGDpCh-q8HPHps8Uw3NWGWiLbVq6Xa7hVxEIp0sH4R9luOfKCOmPerq3wUqgjQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/64b5122b70.mp4?token=T6jWOuF1XaXpVUu6Hk0ocYWyvLg-c5geFydFTx321CO7PeTY_LRbgHrMk5V2wvS9b_q-hL__04Wfb6uSLITW52KwuAcEwuAC75xO5_eSU8zg_RiOwJCdt403BBsL89BlZifb8KROaJ6cjGRaKGLZG7_56QIFOolk_UZmGp3m7HmsFddGOOHsjUYBPB8pIdrROBpSzBBVZCZ0JpJeR9nmAYvGuHpbHKn7hFHvSjPD1TTHB2voz81aR_yy5V-BGm0ogp1ZIM3fRGfQWw52R8BXGe2jpGDpCh-q8HPHps8Uw3NWGWiLbVq6Xa7hVxEIp0sH4R9luOfKCOmPerq3wUqgjQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ترامپ پای تلفن به دستیار نتانیاهو:
@News_Hut</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/66210" target="_blank">📅 23:04 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66209">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">این BISS کد جدید شبکه سه و ورزش رو Starsat چیه شبای اول جام جهانی اوکی بود الان پریده! دایرکت بدین  #hjAly</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/66209" target="_blank">📅 22:51 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66208">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">‏
🚨
🚨
نتانیاهو برای استقلال نظامی ارتش اسرائیل بودجه دیوانه کننده ۱۲۱ میلیارد دلاری اختصاص داد!
@News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/66208" target="_blank">📅 22:43 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66207">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">این BISS کد جدید شبکه سه و ورزش رو Starsat چیه شبای اول جام جهانی اوکی بود الان پریده! دایرکت بدین
#hjAly</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/66207" target="_blank">📅 22:41 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66206">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5bb332cca2.mp4?token=f1cA-hrf9p8YhuOTWKrWJn7U2-7jTieuaghrt7mcth-8owZcUAQ-kHh-Xkz1_nXZdFPhw_gamQ1cIZ8qu_LIrSFeBfUs8cDJHTe-sbug4-btAf7sPL_UtfrRycZrwFlKo_NYux846k-33_Qm_SngvqBQq0SSNRsyMho2yKmjyz6Q39ddLev2sNSH9ibiM_nEpswKE2LvNbnlEYmCNyl9su7WArB3cr9MvuDgaXZUwSQHusojeYGqy6O1FyVmL_6hUhLB7aJ4FWvXdYISFg6jKOPYNbUqQl0qmDn1Y_K4vx87eWhlrUWRHl2EHsMJR06-xaS3OqpHQ4XJdMiZrugn4A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5bb332cca2.mp4?token=f1cA-hrf9p8YhuOTWKrWJn7U2-7jTieuaghrt7mcth-8owZcUAQ-kHh-Xkz1_nXZdFPhw_gamQ1cIZ8qu_LIrSFeBfUs8cDJHTe-sbug4-btAf7sPL_UtfrRycZrwFlKo_NYux846k-33_Qm_SngvqBQq0SSNRsyMho2yKmjyz6Q39ddLev2sNSH9ibiM_nEpswKE2LvNbnlEYmCNyl9su7WArB3cr9MvuDgaXZUwSQHusojeYGqy6O1FyVmL_6hUhLB7aJ4FWvXdYISFg6jKOPYNbUqQl0qmDn1Y_K4vx87eWhlrUWRHl2EHsMJR06-xaS3OqpHQ4XJdMiZrugn4A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
خبرنگار: چرا ترامپ مانند بایدن عمل کرد و چنین توافقی را امضا کرد؟
نتانیاهو: من این مقایسه را نمی‌کنم.
ما هنوز نمی‌دانیم توافق چه خواهد بود.
همچنین نتانیاهو درباره انتخابات گفت که قصد دارم نامزد شوم و همچنین قصد پیروز شدن را دارم.
@News_Hut</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/66206" target="_blank">📅 22:30 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66205">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">🚨
🚨
نتانیاهو درباره توافق ایران ترامپ:
این توافق توسط ایالات متحده، توسط رئیس جمهور ایالات متحده، حاصل شده است و او معتقد است که می‌تواند هم به نظارت و هم به برچیدن برنامه هسته‌ای دست یابد.
گفتم: این تصمیم اوست. تکرار می‌کنم: این تصمیم اوست. او آن را رهبری می‌کند.
البته، من نظراتم را در گفتگوهای مختلف بیان کردم.
از سوی دیگر، گفتم که ما منافع خودمان را داریم.
@News_Hut</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/66205" target="_blank">📅 22:21 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66204">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🚨
🚨
نتانیاهو:
ما ضیف، هنیه و بسیاری از رهبران حماس را کشتیم ، تقریباً همه آنها را.
فکر می‌کنم هنوز یک نفر باقی مانده است؛ او هم کشته خواهد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/66204" target="_blank">📅 22:20 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66203">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🚨
🚨
نتانیاهو:
در ایالات متحده، می‌گویند که رئیس جمهور ترامپ هر کاری را که من بخواهم انجام می‌دهد، و در اسرائیل، برعکس می‌گویند که من هر کاری را که او بخواهد انجام می‌دهم. بنابراین این درست نیست، و این درست نیست.
این رابطه بین شرکایی است که مدت‌هاست یکدیگر را می‌شناسند.
بسیاری از اوقات ما موافقیم؛ گاهی اوقات نیز مخالفیم. این در بهترین خانواده‌ها اتفاق می‌افتد
@News_Hut</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/66203" target="_blank">📅 22:19 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66202">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🚨
🚨
نتانیاهو:
من نگفتم هدف ما سرنگونی رژیم ایران است
بلکه گفتم که می‌خواهیم به ایرانی‌ها در انجام این کار کمک کنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/66202" target="_blank">📅 22:14 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66201">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🚨
🚨
نتانیاهو رسما اعلام کرد که عقب نشینی نخواهد کرد؛ نتانیاهو، در پاسخ به یک سؤال:
«جمهوری اسلامی می‌خواست ما از جنوب لبنان عقب‌نشینی کنیم، اما من بسیار، بسیار، بسیار قاطعانه امتناع کردم—و ما این کار را نخواهیم کرد»
@News_Hut</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/66201" target="_blank">📅 22:12 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66200">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🚨
🚨
نتانیاهو:
ترامپ توافق را با جمهوری اسلامی منعقد کرد و این تصمیم اوست و ما منافع خود را داریم
آمریکا به تصمیم ما در مورد منطقه حائل در لبنان احترام می‌گذارد.
روابط ما با ترامپ مبتنی بر مشارکت است و نه بر اساس تصمیمات تحمیلی
ترامپ رئیس جمهور آمریکا است، من نخست وزیر اسرائیل هستم - من از منافع خود دفاع می کنم.
مواردی وجود دارد که من و ترامپ با هم اختلاف نظر داریم.
مهم است که از منافع امنیتی اسرائیل به طور متفکرانه و مسئولانه دفاع کنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/66200" target="_blank">📅 22:11 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66199">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ReG875V2EpPuFomwUI1EPWed0kjmo0vahy66L0czmLEfjkEk9qlWyCXJZNED3qKrJMQQgAaws2Yt385g1XJjCMTqDJIgoqu0u4ERbr5vzfPVg3ASFqJpg8VWAwTJQYNneAp6U1AkzuvTjUOYcz3-E_NRWlSySIGo1h6i6VDTWg9vCwOfCNXrwK_LG0HOTnHJbPcMlW7UAKqiGjOlB9mC3Mwr6mZXSN46n0gIdIaUBOIL3kXJCOq7PjcLerH65ZTcMlNzROvpyVRokqWveOhB_trQjxg4bVw9yv50cJQdQbP4gtFBV70xeKV9byvdnF1e1wfp_dKdCOBO5CKj6XtfrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
فرانسه
🇫🇷
-
🇸🇳
سنگال
🏆
جام جهانی ۲۰۲۶ - گروه I
⏰
سه‌شنبه ساعت ۲۲:۳۰
🏟
ورزشگاه نیوجرسی (متلایف)
🎲
با بیش از ۸۵۰ نوع آپشن پیش‌بینی
⚡️
ضرایب شگفت‌انگیز
📝
نگاهی به آمار دو تیم:
- فرانسه برای
هفدهمین
بار در جام جهانی حاضر می‌شود و
دو عنوان قهرمانی
در سال‌های ۱۹۹۸ و ۲۰۱۸ در کارنامه خود  دارد.
- فرانسه در جام جهانی
۲۰۲۲
در یک فینال دراماتیک از مسی و یارانش شکست خورد و
نایب قهرمان
شد.
- سنگال پیش از این در
۳ دوره
جام جهانی حضور داشته است.
- سنگال در جام جهانی ۲۰۰۲ موفق شد به جمع
۸ تیم برتر
صعود کند اما در جام جهانی ۲۰۲۲ در مرحله گروهی
حذف
شد.
🧠
تصمیمی که برای جلبِ توجه گرفته می‌شود، خوب نیست.
🌐
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
💻
@BetForward</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/66199" target="_blank">📅 22:06 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66198">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e33dfcb5d1.mp4?token=g5QtvjPURbCPaYDijp8KbMPZljSEWIZqpnFJEL2s_NilBMNoB58cef8ip5IpWBZP01DXRXhzWBuIo7SR1DLQxnIn2-4Jo54vbpiP5BJnD8d8nZUi5n_FSVnsll7JzsJtUnIChM9XoRREHprgjRiyJBMqGembEXxnkBvfK5yHxDsKZUetxp9nDFXMOn-puv4i2vdOMQUEOajpCX9rSMedWTbbJIrFCiIMgPypDFlRdu5ayUl6KGiDh6p0hkib81NckxIcga8BQL7R_64umWdSB8uATJEpdfLJSGo-MSKXAZJLWNeaRyxhL-49xFoe9RhfZ6kyN1Z-csywxs9JwOe1ew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e33dfcb5d1.mp4?token=g5QtvjPURbCPaYDijp8KbMPZljSEWIZqpnFJEL2s_NilBMNoB58cef8ip5IpWBZP01DXRXhzWBuIo7SR1DLQxnIn2-4Jo54vbpiP5BJnD8d8nZUi5n_FSVnsll7JzsJtUnIChM9XoRREHprgjRiyJBMqGembEXxnkBvfK5yHxDsKZUetxp9nDFXMOn-puv4i2vdOMQUEOajpCX9rSMedWTbbJIrFCiIMgPypDFlRdu5ayUl6KGiDh6p0hkib81NckxIcga8BQL7R_64umWdSB8uATJEpdfLJSGo-MSKXAZJLWNeaRyxhL-49xFoe9RhfZ6kyN1Z-csywxs9JwOe1ew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
نتانیاهو:
ما آسیب عظیمی به اقتصاد ایران وارد کردیم؛ برخی این خسارت رو یک تریلیون دلار تخمین میزنند.
@News_Hut</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/66198" target="_blank">📅 22:01 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66197">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bd3fc5d08d.mp4?token=L1yuNWLkDF8w-LzYWgtx2fdunBqacwkn5384WErpV_tOJo_zicx_lBYqhSlvRvhu8ovxgiCR0wOdqJ8eh_m3v72C7yQneIPn_qpZtOjoyRCXD1jCq7V6g4UOcWACN1DDb8kPHGQGblDaO6jBxgduAXrHtee9vvXdukkCihgU1JHJNa2Hbul91IYjIopKaRmFtMycOtl-HvH0IMc3G3ElbcwKzl5PieZOqAKsrb15cS4uL6sBGtaOI1zQTPU98_0PGWFr6V35iIQUJslTdZkEGo4c86GY_JN35bjUvaxKy_UaBwthbP85m4HVQBoWUdkJ-BvV_VJJi8uBDPWSPMRwKA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bd3fc5d08d.mp4?token=L1yuNWLkDF8w-LzYWgtx2fdunBqacwkn5384WErpV_tOJo_zicx_lBYqhSlvRvhu8ovxgiCR0wOdqJ8eh_m3v72C7yQneIPn_qpZtOjoyRCXD1jCq7V6g4UOcWACN1DDb8kPHGQGblDaO6jBxgduAXrHtee9vvXdukkCihgU1JHJNa2Hbul91IYjIopKaRmFtMycOtl-HvH0IMc3G3ElbcwKzl5PieZOqAKsrb15cS4uL6sBGtaOI1zQTPU98_0PGWFr6V35iIQUJslTdZkEGo4c86GY_JN35bjUvaxKy_UaBwthbP85m4HVQBoWUdkJ-BvV_VJJi8uBDPWSPMRwKA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
نتانیاهو:
هر زمان که لازم باشد اقدام خواهیم کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/66197" target="_blank">📅 21:58 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66196">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/50e4d0c9fa.mp4?token=uGnIoWK7LwUQInzHX5BL4hpZRcerpZTvUKTLV9NziV6vcND_4TRaszg47Y4m-5sIqbd4OutGTYFKSnQJ952GUWv46zo_XmxE2FQunzQcIbm3MrdFafTVpe42FG8ZOm9UZqf2n_axI36J1Y9dTgV5pLpzK6QOuPYnxBPAsDu1hUWpf-kAEEaOuom_6Qwaqj7ijq-fq17N8nVgxjCVhgR_mgOoT3bxJWw9gbOshYbGBXQN3K48Cmp65aLf4Blj697BZltRqwJ-TA0pYhEfaqRJwXW6zajDOdgghBOg2NOcYmJA1JFavokmcSfJaSzkmWHIjGIWcx3Dd3aioCVYYQ4oDQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/50e4d0c9fa.mp4?token=uGnIoWK7LwUQInzHX5BL4hpZRcerpZTvUKTLV9NziV6vcND_4TRaszg47Y4m-5sIqbd4OutGTYFKSnQJ952GUWv46zo_XmxE2FQunzQcIbm3MrdFafTVpe42FG8ZOm9UZqf2n_axI36J1Y9dTgV5pLpzK6QOuPYnxBPAsDu1hUWpf-kAEEaOuom_6Qwaqj7ijq-fq17N8nVgxjCVhgR_mgOoT3bxJWw9gbOshYbGBXQN3K48Cmp65aLf4Blj697BZltRqwJ-TA0pYhEfaqRJwXW6zajDOdgghBOg2NOcYmJA1JFavokmcSfJaSzkmWHIjGIWcx3Dd3aioCVYYQ4oDQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
نتانیاهو: ما در لبنان خواهیم ماند.
کار با ایران ممکن است همچنان تمام نشده باشد
ماموریت زندگی من مبارزه با برنامه هسته ای ایران است.
با توافق یا بدون توافق، ایران سلاح هسته ای نخواهد داشت.
اگر برای حمله به ایران عجله نکرده بودیم، به بمب هسته ای دست می یافت.
ما رهبران ایران را کشتیم، به سرویس‌های امنیتی آن آسیب شدیدی زدیم و اسرائیل را از تهدید هسته‌ای ایران نجات دادیم.
@News_Hut</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/66196" target="_blank">📅 21:55 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66195">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🚨
🚨
درگیری شدید طرفداران تیم ایران با مخالفان تیم قلعه‌نویی در لس‌آنجلس ساعاتی قبل بازی
@News_Hut</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/66195" target="_blank">📅 21:03 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66194">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0695d77536.mp4?token=nuuimaZC0RlmfynZC5ouWL3pnm1htlQ3TkVxCOfPq54LSuUPx0lpWezocxcv2YAo1k8bTOt9dLIfDM4vLQjGusdob7WHxW1-Xg2W6ttbe76rP8FJSw-kHTWUWcg1xB9B9yV95xLCD_ocaeeWteWvcrormur4kroJSn63XF8aM-YroRVE8HP8_nekwz_DcF3RD8BcX5eY17p59FI1Of3b-6CiOAbj10n3eZevlkbG8KyA54YQBNvEihWx6c_t6ddjAnYPAWFFl2ITAZv3BrOu0uMY1wolKmgcL9_q55gPWdlFLBrmnxvRhYTKd-UZ4sa5ccaA1t251RrB1c3ZdgDnlQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0695d77536.mp4?token=nuuimaZC0RlmfynZC5ouWL3pnm1htlQ3TkVxCOfPq54LSuUPx0lpWezocxcv2YAo1k8bTOt9dLIfDM4vLQjGusdob7WHxW1-Xg2W6ttbe76rP8FJSw-kHTWUWcg1xB9B9yV95xLCD_ocaeeWteWvcrormur4kroJSn63XF8aM-YroRVE8HP8_nekwz_DcF3RD8BcX5eY17p59FI1Of3b-6CiOAbj10n3eZevlkbG8KyA54YQBNvEihWx6c_t6ddjAnYPAWFFl2ITAZv3BrOu0uMY1wolKmgcL9_q55gPWdlFLBrmnxvRhYTKd-UZ4sa5ccaA1t251RrB1c3ZdgDnlQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نه جنگ خواهد شد نه مذاکره خواهیم کرد
😂
.
@News_Hut</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/66194" target="_blank">📅 21:02 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66193">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WxvIznaGkBErJZDoPjWPF9iF3dtWBdkXFRPixonCYn4Zx4ErcbZqMb0q-TTdNQFELE4sff58Z_xw1ORdnWKg5Q2MHbhTevi1eo9OGnUHX3MjeUe8tougMpOuPKqBZ57x0zuX6scu144751l_NEwfDrmZGqPzPfhDNoJaEvP5tEdQa5NTsfeTSBy_L2kn0SMSa3ZGJH2gRef9UMGVpbjvNuBeUV3v9EduFrPB5FQ59-69xd85WB_FtRrISZ8GaLes2W2_Dchj8g3GbqZnPvH-mVM6g14NnuGY7iWz0zeUx6C01iJoCAVktH3rWBT6mEsd1jaq7acb2XRivFhaqODbCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">درآمد از تلگرام بدون نیاز به ممبر و تولید محتوا؟
سیستمی به اسم MTP وجود داره که باهاش میتونی وارد پروژه‌های واقعی بشی و درآمد کسب کنی.
✅
بدون نیاز به ممبر
✅
بدون نیاز به فالوور
✅
بدون نیاز به تولید محتوا
✅
شروع سریع
✅
آموزش کامل و پشتیبانی
🎁
فقط برای ۳۰ نفر اول:
سه پروژه اولیه بهت داده میشه
مبلغ هر پروژه ۲۵ میلیون تومنه
یعنی از همون ابتدا امکان رسیدن به درآمدهای بالا برات فراهمه
اگر میخوای جزو ۳۰ نفر اول باشی، وارد کانال شو و شمارت رو ارسال کن:
👇
👇
👇
https://t.me/+QpsFnjSfC382MGQ0</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/66193" target="_blank">📅 21:02 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66192">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/24683d102e.mp4?token=I2-m90nEXb1gdmITK7gOqjU04hRumVXaOOz5g7Izt8mSqd9bQiIi2RO7RYnMGKAooKlWMvV3N4Bl9VAZUGC3JX9t44fma0_MEdPVzh14ERQbWZ7S1PYTgVzCDUJCSK4y2xqp2k-8nUg-9PxwykfYVMmbz1JQ4nJo85lnL5RdCnXT-5lkPsCXFUJfzeH8VyDqcA0dadpzSfZ9qu262t5IjrDRc4tici9TPqnHCOmKUKzzWJb6TSopseNaq96CO5NzF-Mhg09vFfIbaSdl-6pekOtVFI1SGQtvR7SPf_ECoroZCDENjLUrz7LQalUpAE48Wgmg2LK-oLqGFRmXo2OKZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/24683d102e.mp4?token=I2-m90nEXb1gdmITK7gOqjU04hRumVXaOOz5g7Izt8mSqd9bQiIi2RO7RYnMGKAooKlWMvV3N4Bl9VAZUGC3JX9t44fma0_MEdPVzh14ERQbWZ7S1PYTgVzCDUJCSK4y2xqp2k-8nUg-9PxwykfYVMmbz1JQ4nJo85lnL5RdCnXT-5lkPsCXFUJfzeH8VyDqcA0dadpzSfZ9qu262t5IjrDRc4tici9TPqnHCOmKUKzzWJb6TSopseNaq96CO5NzF-Mhg09vFfIbaSdl-6pekOtVFI1SGQtvR7SPf_ECoroZCDENjLUrz7LQalUpAE48Wgmg2LK-oLqGFRmXo2OKZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😂
آخرین مکالمه ترامپ و نتانیاهو بعد توافق:
@News_Hut</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/66192" target="_blank">📅 20:41 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66191">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a708e029d7.mp4?token=gksD6Fg7roh0MNVoyi7Ne561gchIe_GI4xaAAHA-KJwS6QqlvdjlWRuCgiCf4ht58IsppIlQrwpWgzyrW_TfjIdUzAjk3fm3ZoiY3eynluvLclanngHYI4HQkTjxmn46SnxZyB6U7WL2lkS9hTRdJUp_gzAaEFLAIw-oD94gO4CrY8_6OVEyCqSKHqAs31eW0hJDj9OdM4wQSLXBvbJxLNxWjtpb7shExUEOZCI0WoadHmBjFjAn4PIihw8C5yhsEhfd_g6MNdmAo8FmCnDOBoBqXy7ICqEgaBwINtwrTFbgdxjTEtDpV2BPa--0VPCRnkMGxjyAdCoF3d2ZOfLabQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a708e029d7.mp4?token=gksD6Fg7roh0MNVoyi7Ne561gchIe_GI4xaAAHA-KJwS6QqlvdjlWRuCgiCf4ht58IsppIlQrwpWgzyrW_TfjIdUzAjk3fm3ZoiY3eynluvLclanngHYI4HQkTjxmn46SnxZyB6U7WL2lkS9hTRdJUp_gzAaEFLAIw-oD94gO4CrY8_6OVEyCqSKHqAs31eW0hJDj9OdM4wQSLXBvbJxLNxWjtpb7shExUEOZCI0WoadHmBjFjAn4PIihw8C5yhsEhfd_g6MNdmAo8FmCnDOBoBqXy7ICqEgaBwINtwrTFbgdxjTEtDpV2BPa--0VPCRnkMGxjyAdCoF3d2ZOfLabQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
ترامپ: توافق شامل هیچ‌گونه تسهیل زودهنگام تحریم‌ها برای رژیم تروریستی جمهوری اسلامی نمی‌شود.
ترامپ در پاسخ به پرسشی درباره احتمال کاهش یا تعلیق زودهنگام تحریم‌ها علیه رژیم تروریستی جمهوری اسلامی تأکید کرد چنین موضوعی در توافق وجود ندارد و افزود این مسئله در نهایت به رفتار رژیم تروریستی جمهوری اسلامی بستگی دارد.
@News_Hut</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/66191" target="_blank">📅 20:31 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66190">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">53.8 MB</div>
</div>
<a href="https://t.me/news_hut/66190" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/66190" target="_blank">📅 20:31 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66189">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DFIGEed8lkXyt4bGjFqzVvYVSk9m8RcBxNMc1u16zlIz2W0Km__GDTPENIhpfYrcjP7NWAwerwinB5adaElwUpYwiBecjYDl0UkLSI9hA0GBFG1RUYYAD4n_0ciJBKy88zxQPr94JQY1jz4UA3C24iik0jEHBbFZxAvempTGKFQs4jt7VZIXqCkbsUtDl4UINSO2VYBdZgrajU4aNeirWAIkFLgImXkX5qCH_r46aYKHHpVrd_0k6BoY7eQibgJvdlQLstoWKBn9Xfj46g8-qFJNiCV72ww44IC057DigBeMSXquvy34VDCi7TYvXCDZHLwGD8w5VD-paoykj6n-ig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
وان‌ ایکس بت برترین و خفن ترین سایت پیشبینی بین المللی که به کاربران  ایرانی خدمات میدهد
🔥
🎁
با افتتاح حساب در 1XBET از طریق کد هدیه
1x_1566529
تا سقف ۱۳۰ درصد به شما کاربران گرانقدر  بازپرداخت هدیه میدهد
🌐
Link:
bitly.uk/connect1xbet
🌐
Link:
bitly.uk/connect1xbet
🔑
برای ورود به سایت از کشور های اسیایی یا کانادا یا ترکیه استفاده کنید
⬇️
⬇️
اپلیکیشن وان‌ایکس بت
🔽
🔽</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/66189" target="_blank">📅 20:31 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66187">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/27ad63d98d.mp4?token=g_8q2OcoSqLxZ1j75pXvL9fLb23M7fADT0QRufEtJ_zV5DfLk4aiYx1YkurDE5Q6lv-3OWNoroIBIOWXBAjPOgIFJJcUaJ5TRE-An1JnfCaY_Tv6qwlTp9hPdKWF-n7c1DJowhmZO-hCCx06O56FfGNXFEEb_Oq7YohmqGwv-yDUFT8ajYTf1MoHXGDtOp9wrVWTbZSBrUBq8IUnj_g-u2lUErR-T2cIoeUNoJHaEgFomTVip4kpMKC87Y7QiU3KrWp_6qhh6tzPV9DtPrw7NUo4ZHDOvi4MTR9-qOVkhnmPmAQcZqgVtYUFuUeZWxOQZrjaK6Cj5IxZ1P-Qx_cwNw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/27ad63d98d.mp4?token=g_8q2OcoSqLxZ1j75pXvL9fLb23M7fADT0QRufEtJ_zV5DfLk4aiYx1YkurDE5Q6lv-3OWNoroIBIOWXBAjPOgIFJJcUaJ5TRE-An1JnfCaY_Tv6qwlTp9hPdKWF-n7c1DJowhmZO-hCCx06O56FfGNXFEEb_Oq7YohmqGwv-yDUFT8ajYTf1MoHXGDtOp9wrVWTbZSBrUBq8IUnj_g-u2lUErR-T2cIoeUNoJHaEgFomTVip4kpMKC87Y7QiU3KrWp_6qhh6tzPV9DtPrw7NUo4ZHDOvi4MTR9-qOVkhnmPmAQcZqgVtYUFuUeZWxOQZrjaK6Cj5IxZ1P-Qx_cwNw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
ترامپ:
متن تفاهم‌نامه به زودی منتشر خواهد شد و سندی بسیار قدرتمند است
ترامپ در پاسخ به پرسشی درباره زمان انتشار متن تفاهم‌نامه گفت این سند احتمالاً خیلی زود منتشر می‌شود، زیرا مایل است افکار عمومی آن را مشاهده کنند. او همچنین تأکید کرد این تفاهم‌نامه سندی بسیار قدرتمند است و آن را با توافق دولت اوباما مقایسه کرد که به گفته او سندی بسیار بد بود. پرزیدنت ترامپ افزود انتشار متن احتمالاً در مقطعی پس از روز جمعه انجام خواهد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/news_hut/66187" target="_blank">📅 20:24 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66186">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/da891bd3ed.mp4?token=Km-3q0WR6HF1B1sJvWNRj6eYUQ07RI8i54KUdVPN3XaZiXSlq6ARpFcPBnyXShz-oZBYuD-gL93KJQEGzZDGUvDNqCkv7trGPP6BltMrfHjbdH_0XUNmzBbJz-KTmFCY0FZV3yHvIB6oRfu1YaM9H4ke7BOob2Lz_KS24laNcvFRvLHpkRfVMlLUwVWI_ubAMf4YA31iE3vfCFGvdF_nFmiuNQ9_hFM79mPXA2jalY9Eym7e3E7F7YH0kZ2vBfDOEjU_o4LhEJqeBi3W6AdpKIroDWspiabGfTDikP2w1nR07nIfjy8MF2qPoEXUmdmXW8BTMjPHnm1ldDCU51JeYw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/da891bd3ed.mp4?token=Km-3q0WR6HF1B1sJvWNRj6eYUQ07RI8i54KUdVPN3XaZiXSlq6ARpFcPBnyXShz-oZBYuD-gL93KJQEGzZDGUvDNqCkv7trGPP6BltMrfHjbdH_0XUNmzBbJz-KTmFCY0FZV3yHvIB6oRfu1YaM9H4ke7BOob2Lz_KS24laNcvFRvLHpkRfVMlLUwVWI_ubAMf4YA31iE3vfCFGvdF_nFmiuNQ9_hFM79mPXA2jalY9Eym7e3E7F7YH0kZ2vBfDOEjU_o4LhEJqeBi3W6AdpKIroDWspiabGfTDikP2w1nR07nIfjy8MF2qPoEXUmdmXW8BTMjPHnm1ldDCU51JeYw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
ترامپ: می‌خواهیم مسئله لبنان را حل کنیم.
آمریکا به دنبال آن است که ببیند آیا می‌تواند مسئله لبنان را سامان دهد، زیرا این بحران به نظر می‌رسد هرگز پایان نمی‌یابد. او افزود این موضوع در مقایسه با سایر پرونده‌ها نباید دشوار باشد و درباره گروه تروریستی حزب‌الله نیز گفت باید گفت‌وگوهایی در این خصوص انجام شود.
@News_Hut</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/news_hut/66186" target="_blank">📅 20:20 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66185">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/46bc16471f.mp4?token=fIdmvqtaUlsw_8SeMDRrsBjLNv9thaaGjBCAT3NFoXcUIte3OpSda_3KE5w90O8JIALEpdT0a6w3STk1tD8r79DUWHkOll0J3dT7Mng0ltHLHC9MEKaqeUYNjDgfwbbuILihyi4f6OQ-ehPdElsuSKdn9DAsuFtXPn9OmajaatuonvzG9u-iZZipG4fMRIVWcYZJ_lCfE84vDxYcZGMRYOU3n0m1KdrgI1gMFzHju2fub-zTe0-vnyb8XSrKFmGJZqlHPslCIArzYzT2-v2Hcj6wRB3B3dI2lQNKSfF6CedBKPyqqAmhH0W2KnnCYuD9U7wqo3I9GxtF42IJDkvI7w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/46bc16471f.mp4?token=fIdmvqtaUlsw_8SeMDRrsBjLNv9thaaGjBCAT3NFoXcUIte3OpSda_3KE5w90O8JIALEpdT0a6w3STk1tD8r79DUWHkOll0J3dT7Mng0ltHLHC9MEKaqeUYNjDgfwbbuILihyi4f6OQ-ehPdElsuSKdn9DAsuFtXPn9OmajaatuonvzG9u-iZZipG4fMRIVWcYZJ_lCfE84vDxYcZGMRYOU3n0m1KdrgI1gMFzHju2fub-zTe0-vnyb8XSrKFmGJZqlHPslCIArzYzT2-v2Hcj6wRB3B3dI2lQNKSfF6CedBKPyqqAmhH0W2KnnCYuD9U7wqo3I9GxtF42IJDkvI7w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
ترامپ:
درباره باز بودن تنگه هرمز اختلاف‌نظرهایی وجود داشت، اما در نهایت عبور و مرور از این گذرگاه راهبردی بدون دریافت عوارض انجام خواهد شد. او افزود آمریکا احتمالاً به کمک زیادی نیاز نخواهد داشت، اما حضور یک یا دو کشتی از چند کشور دیگر می‌تواند مفید باشد و فرانسه نیز یکی از گزینه‌های مناسب برای مشارکت در این مأموریت است. پرزیدنت ترامپ همچنین تأکید کرد هیچ‌گاه نمی‌توان از تحولات آینده کاملاً مطمئن بود، اما به باور او تنگه هرمز باز خواهد ماند و رفت‌وآمد دریایی در آن آزادانه ادامه پیدا خواهد کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/news_hut/66185" target="_blank">📅 20:17 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66184">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/13b0fceee3.mp4?token=SfSt9NshWs-5sEOp422xiAXQAXfOVRVr4QT1e2rng-rMEB139Bp5TM9X-tnkMOe1GmmHAfk-UFHEN_nRbyU5YG1AVxG7gRwfMwHOYFLq3q78UUfQzSqKsxWOEyXJz9GrB9fUMV8_FC9SO-utqKil_F5JG61v-MSIbgMXE75OS3CaOBc39yTu9g8CWbPuJfRfPfxe3Hpo__aydNhqUMS-QvEPsEe7DnXldiaRh8beffWpSBKC0hKj3YZVf7A68IpWJHRxoH8Pb9o5jaX9p5_Yj_yJDmV13a-4Xh0dYvcFuFPLcYWP3clyREdm5ffS5VLrbjPiKhUvnUFRGOAeCAHVcg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/13b0fceee3.mp4?token=SfSt9NshWs-5sEOp422xiAXQAXfOVRVr4QT1e2rng-rMEB139Bp5TM9X-tnkMOe1GmmHAfk-UFHEN_nRbyU5YG1AVxG7gRwfMwHOYFLq3q78UUfQzSqKsxWOEyXJz9GrB9fUMV8_FC9SO-utqKil_F5JG61v-MSIbgMXE75OS3CaOBc39yTu9g8CWbPuJfRfPfxe3Hpo__aydNhqUMS-QvEPsEe7DnXldiaRh8beffWpSBKC0hKj3YZVf7A68IpWJHRxoH8Pb9o5jaX9p5_Yj_yJDmV13a-4Xh0dYvcFuFPLcYWP3clyREdm5ffS5VLrbjPiKhUvnUFRGOAeCAHVcg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
ترامپ درباره حضور در مراسم امضای روز جمعه:
پرزیدنت ترامپ در پاسخ به پرسشی درباره حضورش در مراسم امضای روز جمعه گفت این موضوع به شرایط بستگی دارد و در ابتدا قرار بود جی دی ونس این مسئولیت را بر عهده بگیرد. او افزود ممکن است تا آن زمان برنامه‌های دیگری داشته باشد، زیرا قرار است تا دیروقت مشغول باشد و هنوز تصمیم نهایی درباره حضورش گرفته نشده است.
@News_Hut</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/news_hut/66184" target="_blank">📅 20:13 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66183">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/722077d2f4.mp4?token=KskkP1Y6tkRC696IE86w8cQ4CZyNw-4CcyzarkLHO6PAHOiE9yI_uxaBb6nLvmXQaPexcabwdImj_nSTsvbYNlWiJ-tXzmnZXGN5QC3s_q1HIFQG-kNpgAy91zoKocYGavNL9cSx0v37vjpH-aWyVMGNtLZuq_fsIBgJj0hkWDakUvt4pfx3dJjk2z--A9Hn7w6T8BJ0HVrRfMEfIviB2VDoX-Ln-787wMRjFRqY4MEwFyXp2dg6D7D-WNLyaG96Jjuc0lROvHwAEdgoNEhRtBorzf4Nut8X33durwJKJOnMaJaSe7J3ZnQ5cpHHnVjoPnNXE5oKpiR14O2SM-PEoA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/722077d2f4.mp4?token=KskkP1Y6tkRC696IE86w8cQ4CZyNw-4CcyzarkLHO6PAHOiE9yI_uxaBb6nLvmXQaPexcabwdImj_nSTsvbYNlWiJ-tXzmnZXGN5QC3s_q1HIFQG-kNpgAy91zoKocYGavNL9cSx0v37vjpH-aWyVMGNtLZuq_fsIBgJj0hkWDakUvt4pfx3dJjk2z--A9Hn7w6T8BJ0HVrRfMEfIviB2VDoX-Ln-787wMRjFRqY4MEwFyXp2dg6D7D-WNLyaG96Jjuc0lROvHwAEdgoNEhRtBorzf4Nut8X33durwJKJOnMaJaSe7J3ZnQ5cpHHnVjoPnNXE5oKpiR14O2SM-PEoA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
ترامپ:
پرزیدنت ترامپ گفت آمریکا کار بزرگی انجام داده و امیدوار است روابط خوبی با رژیم تروریستی جمهوری اسلامی شکل بگیرد و دو طرف بتوانند با یکدیگر کنار بیایند. او افزود اگر این روند موفق نباشد، شرایط به نقطه شروع بازخواهد گشت، اما معتقد است نیازی به چنین سناریویی نخواهد بود. پرزیدنت ترامپ همچنین تأکید کرد توافق انجام‌شده با رژیم تروریستی جمهوری اسلامی می‌تواند دستاورد بزرگی برای جهان به همراه داشته باشد، زیرا برای مدتی جریان نفت در منطقه با محدودیت و اختلال مواجه شده بود.
@News_Hut</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/news_hut/66183" target="_blank">📅 20:09 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66182">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SjRZY6oB5BP8qtjDPErDRICBfb6S4hqFkN0nSZYPgt-iFbz7rJpg2kgdtqvUk-t1mTD0pK-Kct7GEXUEtVyCp_xtdvhUQcIKzLJULbnZNrD_VITsNODEp7WEtSeS2AuSZELwl5uLKBY5aJVqre59i1ciCuYm79awMUg582_Afm7QlO_9Q8LoeDGp-_Po2wccRKnyJDc3pUJl-wbfS-VUfwnqD7ur6syeCiuumWAG5HLNW5PgHsmQOgW10TBHuaUxUDjAwNjTv2fDFkAQVN00YBc08AdiRFmvis20ZCuiTyBvT7VicsJwNQ_JZNEhSsq3RyfEiDI_Bpa5a4ms4NDy2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
قالیباف:
ملت دوست‌داشتنی و سروقامت ایران! با مقاومت تاریخی شما و رشادت نیروهای مسلح دربرابر آنان که قصد جان این ملت و نابودی و تسلیم این مملکت را کرده بودند، ایران گامی بلند به سوی پیروزی نهایی برداشت. می‌خواستند و نتوانستند.
ایستاده‌ایم و در نهایت ‎
#ایران_ما
پیروز خواهد شد، به لطف خدا.
@News_Hut</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/news_hut/66182" target="_blank">📅 19:56 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66181">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cf026052c0.mp4?token=dwAS55lHT9Ln5g84esP0PAXzi7zasWj0GPvZ6tGNAQxCpLUN7qB4C6PHSXvU_3WplHL1FEdlednUFIzfnQVrFbQ_toCWfRhn1jCijc5WnAmn3r9wjbrcJ0oF4cgv1itF198kEzz8fOGBaJh8KBun4aY04_hprg2WBRlEA2nht1gZBHf3v9ygjSl3ADqrxKbDrclbqMxeO8FIU74ww_3B8m_vZUDIiVsC08hH78D9VautEFCu8SzWpYBd0cIwV7EUQW79k6ctpkNtJvbK_MGtF3jhzyhxYgf8xg_I7pI239-Z47cnsUMqS2RWe-v0hAAWVyoxDXROxxz5X4HKONrI4A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cf026052c0.mp4?token=dwAS55lHT9Ln5g84esP0PAXzi7zasWj0GPvZ6tGNAQxCpLUN7qB4C6PHSXvU_3WplHL1FEdlednUFIzfnQVrFbQ_toCWfRhn1jCijc5WnAmn3r9wjbrcJ0oF4cgv1itF198kEzz8fOGBaJh8KBun4aY04_hprg2WBRlEA2nht1gZBHf3v9ygjSl3ADqrxKbDrclbqMxeO8FIU74ww_3B8m_vZUDIiVsC08hH78D9VautEFCu8SzWpYBd0cIwV7EUQW79k6ctpkNtJvbK_MGtF3jhzyhxYgf8xg_I7pI239-Z47cnsUMqS2RWe-v0hAAWVyoxDXROxxz5X4HKONrI4A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
قالیباف بعد تعطیل کردن مجلس و انجام هر کاری که دلش میخواد
😂
:
@News_Hut</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/news_hut/66181" target="_blank">📅 19:36 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66180">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🔴
ما هرکسیو تضمین نمیکنیم اما تیم کاویانی واقعا کارشون خوبه و دارن کل فیلترشکن ادمینای مارو ساپورت میکنن
❗️
پشتیبانی 24 ساعته
😈
همراه با تست رایگان
💵
تعرفه‌ها 10 گیگ — 170 تومان 20 گیگ — 340 تومان نامحدود — 450 تومان (ترکیه)  برای خرید بهشون پیام بدین
⬇️
…</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/news_hut/66180" target="_blank">📅 19:36 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66179">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">🔴
ما هرکسیو تضمین نمیکنیم اما تیم کاویانی واقعا کارشون خوبه و دارن کل فیلترشکن ادمینای مارو ساپورت میکنن
❗️
پشتیبانی 24 ساعته
😈
همراه با تست رایگان
💵
تعرفه‌ها
10 گیگ — 170 تومان
20 گیگ — 340 تومان
نامحدود — 450 تومان (ترکیه)
برای خرید بهشون پیام بدین
⬇️
@kaviani_vpn
@kaviani_vpn</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/66179" target="_blank">📅 19:36 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66174">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Li_ZfRPZeLVJz2fNtIt4PywaFdi-KzhsLW_Beu5Z3KvqSbwEv8Xa70-nZEndbiB2LaswUpXUqQW6qpKzK_ji8Ik6pm_zo9W_D2CO-Bw4LVvWVKe3DWzLflzf4IZmuhk9UDzyu6zp7vM-uAX3VWEq_GOPyuCLRgzuLDswOSdsqgk0SQdCV6a_53NsCXeMdDsljqtj11mGjxzDAX2kbUAJQMNeMvYwyvc45otVcEgikUuRCAC8IlJIPtFZplrSHHClhuSG-Aw41AUHXGOR422usGBbbheUUVPlFz8qBSmIK7IjiatfQWzAaXEC0T1XYWJiOYQSFpGhw1_5jj02ZmysAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WrX3qZNjV52UETy4omy8XLgXIIVdRzW-QghNMejI9PFMdN1gjijqeIIqOkLbF8R9zKnOG4_f1OzniFtFbtJWpYwU84pvLyXC-ypkjtXKYUrvlC5A3aYHP7vMgkxBhcRQFMLm8TtgawLQ2jGOlMblelKnnTe_y0p4OOjLBMEFOwGIclWfe-gkapUcRbPjd3JL89WxWaT7Wb67wDS5SqEyerH287Jx_a3EvcavzsYPkoFNdyz_q4s1UhEW2f-xO0yYrMdVq89F4IXJ3Jh75ubDmqwu3q5jki5sIBIC8mlwyrwJYLOcgKvoBKuVzju0UwhcrgpmwLOjzUGPW6Q3R4EkrA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b5cd54e998.mp4?token=Lp5xuIDZK38Y4PNGd4uOP7ckzxMMj3lCiaYw2MSa7UGx1dxO86N5o4oQWXCxZzeFb2Fa00fD2tWSdimVl1Q9jdS-yow0p3n1uD2G8o86Oh5jMgcsL_UyV0BLLvaTpaHJbYKGYaK63p_D3_opmKBCC4Eh6-5J15jseXwCtHW2Q5JOh-S6hYxJWsi9ZhPzM3lCIg_1K4D1An_StXUjTQ-ORVL3p5P_yind9OMSRwj0EdPoLKEnWXjH_GABJo7xrUCD9roqr4YCla3nc8AxEbGSUT3DLRTpY3GEBG-zFgyua8zeQKcW5vOhpFb1ouYbCERSTq8Du8HaanhlLTVGMz2zDg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b5cd54e998.mp4?token=Lp5xuIDZK38Y4PNGd4uOP7ckzxMMj3lCiaYw2MSa7UGx1dxO86N5o4oQWXCxZzeFb2Fa00fD2tWSdimVl1Q9jdS-yow0p3n1uD2G8o86Oh5jMgcsL_UyV0BLLvaTpaHJbYKGYaK63p_D3_opmKBCC4Eh6-5J15jseXwCtHW2Q5JOh-S6hYxJWsi9ZhPzM3lCIg_1K4D1An_StXUjTQ-ORVL3p5P_yind9OMSRwj0EdPoLKEnWXjH_GABJo7xrUCD9roqr4YCla3nc8AxEbGSUT3DLRTpY3GEBG-zFgyua8zeQKcW5vOhpFb1ouYbCERSTq8Du8HaanhlLTVGMz2zDg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تصاویری از آتش سوزی گسترده، میدان تجریش تهران
@News_Hut</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/66174" target="_blank">📅 19:20 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66173">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">🚨
نتانیاهو قراره تا چند ساعت دیگه سخنرانی کنه و این اولین واکنش اون نسبت به توافق هست.
@News_Hut</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/66173" target="_blank">📅 18:54 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66172">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">‼️
ونس درباره ایران:
ما کاملاً آماده‌ایم که کشورهای خلیج فارس در بازسازی ایران سرمایه‌گذاری هنگفتی کنند.
@News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/66172" target="_blank">📅 18:45 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66171">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">‼️
ونس درباره ایران:
ما دیروز به صورت دیجیتالی قرارداد را امضا کردیم و هیچ پولی آزاد نشده است. این موضوع تغییر نخواهد کرد،
این یک مسئله مبتنی بر عملکرد است.
@News_Hut</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/66171" target="_blank">📅 18:33 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66170">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3cbb12962f.mp4?token=QDIzrLyBsZFuDbDpq6I-vN4cWL83rv0TPdF4RtsCoJO6VPEQ0WeESRuQvEwNX4NujjXNxPD4tDAdYL3Mu-K-rxhWqXsNmae8RrnwRKDzPN_WD4wegOBk05d6-vsx_CxUm05XggeeWHZYodAmPL1onLAv1ooWQlsJGBhlwNczX5xzl2IY7ALthar52Japba2MCd4PcVsr8PuaeK_Y8r95xj3pA9mPHaTMACpchrhm5h3HNYZvsYSJhB3HjaPhYy9jOsDqkMw4D4Mksffti2N1XRampSkv0AHkoFDtnM1fAXE8b6fI5RiEbW3GsrVPU-lfXNxO2uBJmAduDB7UYUuXeg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3cbb12962f.mp4?token=QDIzrLyBsZFuDbDpq6I-vN4cWL83rv0TPdF4RtsCoJO6VPEQ0WeESRuQvEwNX4NujjXNxPD4tDAdYL3Mu-K-rxhWqXsNmae8RrnwRKDzPN_WD4wegOBk05d6-vsx_CxUm05XggeeWHZYodAmPL1onLAv1ooWQlsJGBhlwNczX5xzl2IY7ALthar52Japba2MCd4PcVsr8PuaeK_Y8r95xj3pA9mPHaTMACpchrhm5h3HNYZvsYSJhB3HjaPhYy9jOsDqkMw4D4Mksffti2N1XRampSkv0AHkoFDtnM1fAXE8b6fI5RiEbW3GsrVPU-lfXNxO2uBJmAduDB7UYUuXeg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ونس:
تمام ائتلاف کشورهای حاشیهٔ خلیج فارس از توافق هسته‌ای اوباما با ایران متنفر بودند، چون احساس می‌کردند این توافق به ایران قدرت می‌دهد که نقش یک بازیگر بد را ایفا کند
حالا ائتلاف خلیج فارس دربارهٔ توافق صلح ترامپ چه می‌گوید؟ آنها عاشق این توافق هستند، چون آن را فرصتی برای ساختن و آفریدن خاورمیانه‌ای جدید می‌بینند.
@News_Hut</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/66170" target="_blank">📅 18:15 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66169">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b420a810e3.mp4?token=iso6tNJg9AvuVWeSm513_X5EEP9loVknaBAKx3yL9N16Jn6f9YUEm_i-wMIC37EjcAe_VZAYvc0A3ORz-QDr8r6yz6dLlZHOZeNL-ZsnobJ_6OKNJ1VebQFVuSj6qe9BO3lIQ0t2LMkSqozkQrNfWc6ElBpE65cZhQk7e9lzYs-59nS-DCp-ShQhpxr06fBBVuIl545sA00E4mZfnBIvBQLarvhtylK2LcUTAmSzRZnce8ERkg7nNSrJNXJLND4eNgZLiD9T4KUaldzRJvkvUGobGQVLPXYzXD79K0A7S60g2p2pR3jEbZ2Fezs5IlDuBjMMpK94BNMwTPRqoQG6Qw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b420a810e3.mp4?token=iso6tNJg9AvuVWeSm513_X5EEP9loVknaBAKx3yL9N16Jn6f9YUEm_i-wMIC37EjcAe_VZAYvc0A3ORz-QDr8r6yz6dLlZHOZeNL-ZsnobJ_6OKNJ1VebQFVuSj6qe9BO3lIQ0t2LMkSqozkQrNfWc6ElBpE65cZhQk7e9lzYs-59nS-DCp-ShQhpxr06fBBVuIl545sA00E4mZfnBIvBQLarvhtylK2LcUTAmSzRZnce8ERkg7nNSrJNXJLND4eNgZLiD9T4KUaldzRJvkvUGobGQVLPXYzXD79K0A7S60g2p2pR3jEbZ2Fezs5IlDuBjMMpK94BNMwTPRqoQG6Qw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
جی‌دی ونس درباره ایران:
ما اکنون مستقیماً با نظام ایران صحبت می‌کنیم. روابط خوبی در آنجا داریم
دیگر پیام‌ها را از طریق کانال‌های پشتی منتقل نمی‌کنیم؛ در واقع با آن‌ها صحبت می‌کنیم.
وقتی با آن‌ها صحبت می‌کنید، متوجه می‌شوید چه چیزی واقعی است، چه چیزی جعلی است، درباره چه چیزی جدی هستند و درباره چه چیزی جدی نیستند.
@News_Hut</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/66169" target="_blank">📅 18:00 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66168">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/41a8610027.mp4?token=azBbJBZiYbnlGhGOBJ3oL-PseatHnqMpmasyeX_aDAGk2tb18t34bC2edfdHyAY3Ai9zNGvoKBDFLhWpSErj12u5QiPjG3byuTQ9yNHPXZE4uRvQ0zMTesdPyjY9Ss8_y0w1ulgnDuX_Uuplnr3bO2ZWc1rNp1GPtKyNRDuvKOXYsYlRjd5MBHv9-qrIo5VSAUByyKJM_W50f3HUGdRxuCw3jp7twxo3cu1AfCiOGOv6zsRJjrm7SLbh1z72zVnhCvOOwEaFBosWuWvI9UuW-f2gcN29iGT9Lqq8FcOwo7bKPlfc1KST-P3kRvEX9kZ2n-p6gmrkfo54PcLqJWnsig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/41a8610027.mp4?token=azBbJBZiYbnlGhGOBJ3oL-PseatHnqMpmasyeX_aDAGk2tb18t34bC2edfdHyAY3Ai9zNGvoKBDFLhWpSErj12u5QiPjG3byuTQ9yNHPXZE4uRvQ0zMTesdPyjY9Ss8_y0w1ulgnDuX_Uuplnr3bO2ZWc1rNp1GPtKyNRDuvKOXYsYlRjd5MBHv9-qrIo5VSAUByyKJM_W50f3HUGdRxuCw3jp7twxo3cu1AfCiOGOv6zsRJjrm7SLbh1z72zVnhCvOOwEaFBosWuWvI9UuW-f2gcN29iGT9Lqq8FcOwo7bKPlfc1KST-P3kRvEX9kZ2n-p6gmrkfo54PcLqJWnsig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
جی دی ونس در مورد ایران:
ما دستمان را به سوی ایران دراز می‌کنیم. اگر آنها بخواهند رابطه‌شان را با ما تغییر دهند، ما هم رابطه‌مان را با ایران تغییر خواهیم داد.
این پیشنهاد ماست.
@News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/66168" target="_blank">📅 17:45 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66167">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/362abac9d7.mp4?token=YcYkOkv_sML9k6wILNQzlICFTaCEsWTyXvlQLDie5PM9qn2AXrfOLC5d2mXS6AClylXmBfJ_xMzIbAeKlC_FdQjBg1YrR0UtH_7m_FiziOWvAkbfTcYoTJhv4un7lxfDJ_P_xCs5nT3Od2qVClKUxLpwq1iRrk4MNTNmF4wPsMS7XHAk5nvCVFDm6_WwED5DGbVcSHrKFADzZUHe8UP4FbKZutjl5mxmzXVnIvJQ6ZAVR6dFjY3ainJa9vamN6_SDyTy6AQf7PHjMBdvt10PXa48MZbMj_4iE3gP9eM-rQ2XXIKDvgLDY_PAmLrd_RAOctz2d7LXKPXjMC1xd-OryQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/362abac9d7.mp4?token=YcYkOkv_sML9k6wILNQzlICFTaCEsWTyXvlQLDie5PM9qn2AXrfOLC5d2mXS6AClylXmBfJ_xMzIbAeKlC_FdQjBg1YrR0UtH_7m_FiziOWvAkbfTcYoTJhv4un7lxfDJ_P_xCs5nT3Od2qVClKUxLpwq1iRrk4MNTNmF4wPsMS7XHAk5nvCVFDm6_WwED5DGbVcSHrKFADzZUHe8UP4FbKZutjl5mxmzXVnIvJQ6ZAVR6dFjY3ainJa9vamN6_SDyTy6AQf7PHjMBdvt10PXa48MZbMj_4iE3gP9eM-rQ2XXIKDvgLDY_PAmLrd_RAOctz2d7LXKPXjMC1xd-OryQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گزارش شده یک فروند بمب افکن Tu-22M3 نیروی هوایی در منطقه ایرکوتسک سقوط کرده و به گزارش وزارت دفاع روسیه تمام خدمه موفق شده اند با موفقیت اجکت کنند.
@News_Hut</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/66167" target="_blank">📅 17:29 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66166">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">‼️
پرزیدنت پزشکیان:
فقط یک نفر از اعضای شورای عالی امنیت ملی مخالف توافق بود.
@News_Hut</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/66166" target="_blank">📅 17:26 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66165">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/bI7NoAIClapcI7vSWfXJzuvfdUuKpKEv0g9vGlsYTF3Hj9zSFUAfNOVJJ31gwdf9OPn643rVZQmG8xxe4xoBRFSbmn7fFk6Icppa0VCqzgXq8aEpoSZH2I-xnM9XRubGkyTtnb305kplBeP_YTFUe4tr_UXV1vEI3AstrOaXxjoZTaGKKYsQzhJUKEwheaPcT9RFIjWqCWPjUYfLprsaPtgrhA_YMnuf3Z-96nK7tzoT9RnY6Cr_DRdQYWAYCXG5N_GgydpSxwF9BkBdmQh0dtdqnqBIOYx5u9aJw8to5KJtyQE-MHowl1dBPTxM-NIAZcjsSWIgOSo7PViWHnroiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قبل شروع بازی اسپانیا و کیپ ورده فاک بت اومده لاین داده ضریب ۲.۲۰ الانم میخواد آنالیز بزاره از بازی های جام جهانی نمیخوای بیایی سود کنی؟
💵
@FutballFuckBet
💵
@FutballFuckBet</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/66165" target="_blank">📅 17:25 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66164">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bGCMiRrouDbPCpM5HjAvR4uZWKyAXjv8nAALKYfD9qxyfgDX5AxUWDxIKIp7FuoEOmQkDBbcCNtQr3sBQYC4AC3rP2SIWFhrSVmgd3ee0ZxWwOsbGxSYEDzoTmYykDy7co4TsId57oEFqoZPipAfdtLjlREaj6YM-hOO0KWBLAGR-1Wk12WJ2ImBJGJevWHG4Iubq45wK8XZie2ZzZ5eGE7Gz1XlhMVTtEhFKfq7H2Sq_TeECwfsBdp6s6uxHOGbyJDBqKF_ptMYTJ2nIrfH8CFc4bHXU5Uys_Lpw1fyZAmXO5XE3aUX06MURlhRPztg6tQ4INi0txkZ-4FjaWR0xQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
ترامپ در تروث سوشال :
پس از توافق تاریخی حاصل شده با ایران در آخر هفته، کشتی‌ها شروع به خروج از تنگه هرمز کرده‌اند، که بسیاری از آنها «پر از نفت» هستند
@News_Hut</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/66164" target="_blank">📅 17:19 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66163">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">‼️
صداوسیما:
تنگه هرمز تا اطلاع ثانوی بسته است و سپاه بیش از ۹۶ساعت هستش که اجازه عبور به هیچ شناوری رو نداده.
@News_Hut</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/66163" target="_blank">📅 16:45 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66162">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5f9664d2e7.mp4?token=jfYw0FM9nBIdzN-f1atLgZPhePuPoZEsKhXUA1fjhNuYtBUksMinR9TpffwSvsCTeC4pLSdGnh8LsVAeyJTeLxBilB8wYr-K_8kD6PxbTmJhrtghTLs_aDTUC5nx2B6F7EZfoaEyE0nX8qzXtBHCBpI6_M0Ia-qk3awIJThhhTL_1gYHiRptlLwt7v5M9HoMw0J9SaM9OFucNpw1bP_uVhrf8fjL-M67LSUHuwKjwKK58Sgi9KjAJkwPoMb7A-xR7SgcYfYHUePC6MF5_U_z4wmGF2uXL_9LCBMkCNJeFVQZdpE7u8L6fvNi_GYSrjik-PhXO4tG8mEZjt9Sox9ESg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5f9664d2e7.mp4?token=jfYw0FM9nBIdzN-f1atLgZPhePuPoZEsKhXUA1fjhNuYtBUksMinR9TpffwSvsCTeC4pLSdGnh8LsVAeyJTeLxBilB8wYr-K_8kD6PxbTmJhrtghTLs_aDTUC5nx2B6F7EZfoaEyE0nX8qzXtBHCBpI6_M0Ia-qk3awIJThhhTL_1gYHiRptlLwt7v5M9HoMw0J9SaM9OFucNpw1bP_uVhrf8fjL-M67LSUHuwKjwKK58Sgi9KjAJkwPoMb7A-xR7SgcYfYHUePC6MF5_U_z4wmGF2uXL_9LCBMkCNJeFVQZdpE7u8L6fvNi_GYSrjik-PhXO4tG8mEZjt9Sox9ESg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ممدباقر۲۰بهمن۱۴۰۳:
با قاتلین قاسم سلیمانی مذاکره نمیکنیم.
😂
@News_Hut</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/news_hut/66162" target="_blank">📅 16:15 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66161">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f3b04717ec.mp4?token=JOWJFdBTdE6QW5hpA84-vw-rZqC_HjCXO3zWFjWRZDmzy2jNxC1DHzpo30TNW0dwZv8NB6ZQho8lk_WkMQ5Si3M37BqLalm_Up_shp4fK99kxEzWfQ2o1xhKA7XfVmDh00HSMEIjLSoiDcSw1x5_BjU4_lrwqotp_2__k6_Z0mMos5BSSiXatrd_DbgbmWV3XqBJVXGo8L1CfzUhnBwfxO0vnSNDtwpAfZxU2l1LiaRSsy37qP3RCnqQMzNi_GXWL-PCuKA1lPSA6N3Opqekd5YZOkgCobYW6JWvl3mWJTWCCaCZI-_0EtvyPxqhPfAGHf3mZBmaaBB_O3ReRJeyNw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f3b04717ec.mp4?token=JOWJFdBTdE6QW5hpA84-vw-rZqC_HjCXO3zWFjWRZDmzy2jNxC1DHzpo30TNW0dwZv8NB6ZQho8lk_WkMQ5Si3M37BqLalm_Up_shp4fK99kxEzWfQ2o1xhKA7XfVmDh00HSMEIjLSoiDcSw1x5_BjU4_lrwqotp_2__k6_Z0mMos5BSSiXatrd_DbgbmWV3XqBJVXGo8L1CfzUhnBwfxO0vnSNDtwpAfZxU2l1LiaRSsy37qP3RCnqQMzNi_GXWL-PCuKA1lPSA6N3Opqekd5YZOkgCobYW6JWvl3mWJTWCCaCZI-_0EtvyPxqhPfAGHf3mZBmaaBB_O3ReRJeyNw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
حمله پزشکیان به منتقدان و اراذل صداوسیما
@News_Hut</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/news_hut/66161" target="_blank">📅 15:45 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66160">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XsfFBFOx8_wsrrX8XiOiLsrjaonX8WKrs-6gtypPbAw-FDuMJpwU_tAVJgdJDgceUN6ZbWsdn81YmPTpVZDJXoeG8zUCyYzykLA6y2Az2NFoMyLAKQqeScUaf0fF7-xaRlx51fjrHXt5eihhOXfpukwYfV3WAk83D3ifduFFLT3MMGnp5WWVGcn4n7P-BFTvy_8LGSCPNRWH8J9HvG8ooYnapJg6d4uDPb8IBRecHXkACA9YPdEXY93V97lJMkubEjKY-gsrz1BKFXTzTqKyVppWIy8ineKaEjX7n-ZFJSSWl22udGBa-zT_-KYjRAbGxgARizTDeOwGhqsdinzdYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
ابوالفضل ابوترابی، نماینده مجلس:
استیضاح مسعود پزشکیان مطرح نیست، شاید خدا شهیدش کنه.
@News_Hut</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/news_hut/66160" target="_blank">📅 15:15 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66159">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/74d00f0f51.mp4?token=gXnS4CE--wJIuLZuwNavQlv2SK8g5KYV2tbf_12ukUvSG0Cbseb5lWb5bOU6fLuxYywWQ-GZss-NdeNVlSshsaeImoShldMrVmR85k2yxolxI3lXmxDMUkbRmBo24SZqoTkJMFpjBf5oQfrDwS7sJS3BRCyXUssys4PUhtTcnEJevf7N4BvxjGVsFvhOumKM5Kre7bptHnSdao17__CCSlP8QkvjXQqZNf2rWFeCu1udetCVY80SpjpzJ2o8Bkm1_OXP2dvWDIM7j0nQZ3VN-S-xjxc5Fhc7K92-CrRAPT1kS6xXHw9-F398tmP49jWCTDR20YXqev1sn1O-W0L6KQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/74d00f0f51.mp4?token=gXnS4CE--wJIuLZuwNavQlv2SK8g5KYV2tbf_12ukUvSG0Cbseb5lWb5bOU6fLuxYywWQ-GZss-NdeNVlSshsaeImoShldMrVmR85k2yxolxI3lXmxDMUkbRmBo24SZqoTkJMFpjBf5oQfrDwS7sJS3BRCyXUssys4PUhtTcnEJevf7N4BvxjGVsFvhOumKM5Kre7bptHnSdao17__CCSlP8QkvjXQqZNf2rWFeCu1udetCVY80SpjpzJ2o8Bkm1_OXP2dvWDIM7j0nQZ3VN-S-xjxc5Fhc7K92-CrRAPT1kS6xXHw9-F398tmP49jWCTDR20YXqev1sn1O-W0L6KQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
ترامپ برای شرکت در اجلاس گروه هفت به فرانسه سفر کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/news_hut/66159" target="_blank">📅 14:45 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66158">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A6p43-33e2q8FKh7IsgTzPNIlWxgaTo3kFNxyi8saC1FaLxo86R4e1YZlFN1YLHqzIf9W1q7Vt7uVEtpj0v0otQGcg_o0SHeP_jHrk8GzoF3SJP6KlIs_Sasa8QI1ok_stSdLV6PZNRjQBq6jN1ZkcXDwKdN3DKzz8Tg5nhYCyMYM0nveRQ2PZcw-07RBsq4y0gHWOEfvT4PrqwoptH_LvQA_4wBhxa2MFDx6RX2nwK_6T76zN566AV7VjjWSwtoycSUTkAPGI2iUW1TtjyTmvjvoCApn-EhgB45TULChJcn7LVfrSUsyuHjsnOjPXI7mX0eMbW5ZyUJ5ss3UHOPFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
توییت جدید حساب اسرائیل به فارسی:
یک سال پیش در چنین روزی جمهوری اسلامی با ساقط کردن چند فروند F35خلبانان اسرائیلی را به اسارت گرفت و ما همچنان در انتظار پخش اعترافات آنها در صداوسیما هستیم.
@News_Hut</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/news_hut/66158" target="_blank">📅 14:19 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66157">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c2defa37b1.mp4?token=txrCWYUUA6KZUV0-tIYR5ftbIR9AaNKEF-JMvVRNrB1P2bx-4KVf2TKMU-Kb5xJKksOyo96xkLqJc1JZadDvhvImq7BVYkyfgmusOYkSp4vaHzF8QE--buTDc9Fx9WCLELSD99hRw42zoZsXO2qu-HaU2KUEXYRc13iOUltra58Fw-LE63bM8REnewWmcRUKKaq3AdikkSczLrkwKH1RhRMFm32KeLsHcGvSIO5UXFwnZ8RcQF6XxSJ_0yN4k02kLihLfVXpH4cJXXrV0EfJ7ytf2jUNsbo3UoGkjlURyI-0_IxtPdQwAg-jf3nITz48KeqEbgmA5vbxljP5IlgFmg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c2defa37b1.mp4?token=txrCWYUUA6KZUV0-tIYR5ftbIR9AaNKEF-JMvVRNrB1P2bx-4KVf2TKMU-Kb5xJKksOyo96xkLqJc1JZadDvhvImq7BVYkyfgmusOYkSp4vaHzF8QE--buTDc9Fx9WCLELSD99hRw42zoZsXO2qu-HaU2KUEXYRc13iOUltra58Fw-LE63bM8REnewWmcRUKKaq3AdikkSczLrkwKH1RhRMFm32KeLsHcGvSIO5UXFwnZ8RcQF6XxSJ_0yN4k02kLihLfVXpH4cJXXrV0EfJ7ytf2jUNsbo3UoGkjlURyI-0_IxtPdQwAg-jf3nITz48KeqEbgmA5vbxljP5IlgFmg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
روایت«
ال ریسیتاس
» بازیگر اسپانیایی از اتفاقات جنگ
😂
😂
@News_Hut</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/news_hut/66157" target="_blank">📅 13:57 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66156">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8dca54ea3d.mp4?token=AZ6KRDO7obnamkSpkVblQ_bG69aShD1EPdVWRxDqAy-FgurfVanv8na3mlICJxGC39Uad3-wAq-XesHzPsjyQY239b0PyEPtez7FnknVYmV7dWcSWb4X4OBppzXRVMiSO-k1lLLGXA3QEj8ToKAvgrJ-r_wwumIBcBpJ6grQ04eUoi_y8RjAyDG_WKt-kBS8sHMKon7YbZD9xhWUXxnJCoKIM-LQwQN2kFJOJh2G0-rd32eMcmpbYz-AEiOXYH3SywGxte665JSHQIxds6Bk8Igb2tSF-z9y7DOJgPgRX0YVuHRVfFLEcSSiDQoDhlrYPkBj3oAgmDATkP5U8sbTWg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8dca54ea3d.mp4?token=AZ6KRDO7obnamkSpkVblQ_bG69aShD1EPdVWRxDqAy-FgurfVanv8na3mlICJxGC39Uad3-wAq-XesHzPsjyQY239b0PyEPtez7FnknVYmV7dWcSWb4X4OBppzXRVMiSO-k1lLLGXA3QEj8ToKAvgrJ-r_wwumIBcBpJ6grQ04eUoi_y8RjAyDG_WKt-kBS8sHMKon7YbZD9xhWUXxnJCoKIM-LQwQN2kFJOJh2G0-rd32eMcmpbYz-AEiOXYH3SywGxte665JSHQIxds6Bk8Igb2tSF-z9y7DOJgPgRX0YVuHRVfFLEcSSiDQoDhlrYPkBj3oAgmDATkP5U8sbTWg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تصاویری از حمله اسرائیل به جنوب لبنان
@News_Hut</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/news_hut/66156" target="_blank">📅 13:10 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66155">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BwOh2k8kThuTH9Avo6RksjEdwGzIBWWkwB0Fve4AhqZQ7DEDj-pk9vhnVSrwzGfvut8TC37oWvUaRe6ETkBt-udG3Fahm2GFfjADki2_ALEkk6allhxGR_mQVdES4wMMrUG9Pk9Kp0eEXDMkCQxVXXfe9KyCRVrMb6FJMuWCJPQWS_FWR-vxMuduPCcM-xD7o2GGFEpyukntg2lNhgGJgOozEBmRfVKkQWNrel63J-hBInPPxe6ETEsDvQXnP5cMrt718w6SQH9dIozN14Ik_6Q-MYtdNj5tBOIeriOx7CHmmqGjQEAP_lBL5mWhnUQHWiHhrB9XuYxgXD4_g4l6EQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
دیس پزشکیان به تندروها:
متأسفم که به کسانی که دارن با مأموریت قانونی برای حفظ منافع و عزت کشور کار می‌کنن، برچسب خیانت و وطن‌فروشی می‌زنن. انتقاد کردن حق همه‌ست، ولی تخریب و له کردن این آدما کار مردونه و عادلانه‌ای نیست.
دولت باید از نیروهای خط مقدم که جونشون رو برای امنیت مردم کف دست گذاشتن کامل حمایت کنه. نمی‌شه ازشون انتظار فداکاری داشت ولی امکانات و نیازهاشون رو فراموش کرد.
ما جلوی هیچ قدرتی سر خم نمی‌کنیم، اما در برابر همهٔ مردم ایران و خواسته‌های درستشون پاسخگو و مسئول هستیم؛ نه فقط یه گروه خاص.
@News_Hut</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/news_hut/66155" target="_blank">📅 13:04 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66153">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EJXM6_8zJAaRmzWUaDuwnATcFufW84UngxNdJcvYaZu3N3jQHdldKYQCIi4DWhebA95el2sZMtySm9IULtT8Uc1pDFhJZta2fgniLY0t1DfCPZGQJnC60uaAdTri14Ck1_u1Sox24vjMAuRxCTOrRNmnaabGkxlijOBiQsoHK0y3g51PbtnrNipnr7-YYSGxDpkBPP9P03rkfFb8OjKY8OClGl54W4oB4yy2d4VMV8wVhbHH0SvAAMa4FqQ8dYgm96v3YL_1-tTunFXtEqTSWd6McBo2Z-obmTf23DMS4l_cY5k-V7Ss3hp1orypNGDEUtHPi-ZYvDMENV_rdGYhUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qUgPtVgq7EZtEMUEBtPExPbUI9qAA8S9UpnYUlh4kuFkMXhvobE7bvzCi8kAgtO6jGYxmxT4YYXdkC1EtebUjGIcgppsUsH2TJSPC1PStGi2w3qKPYpQRuC3TXLAV1jGZCDAi1EWRk-fjIuSLndRaBxWAtmCVIvtwjTXf6YVyWaYzoi0EPdBLfF03i55Nfa1VJ5RrNwUy0d6dOEbMq3SRLkz1OtjlAx005xRp53WKDrYj_nhwKN2hQ-t1gNQ9Y4BEE__yKF6r3ZNawZJkMBVkkPFl_wapvKU5CYqJRD_DqYTMLZQwXRPaoUkS00x6K30BVNeeiUX2THiEZuvyz4_gg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
حمله هوایی ارتش اسرائیل به الخیام جنوب لبنان!
@News_Hut</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/66153" target="_blank">📅 12:51 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66152">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">53.8 MB</div>
</div>
<a href="https://t.me/news_hut/66152" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید
🎁
اپلیکیشن رو دانلود کردید موقع ثبت‌نام، کد هدیه 1x_1566529 رو وارد کن و تا
100یورو
هدیه بگیر!</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/66152" target="_blank">📅 12:51 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66151">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ongi1jxZEzRdaLjDW_gF9ndXHk3mDnPWRcMAbRmoQg9lKzVd74P4e0MBKkQymkakmUTZdhx60emCK0XJ1iSWY7i88eArwa8B1fADUgN7E2sBBi6TSqYdg_DOuzquFd83-hnKjsKN2p4z-wtg-fIvPztMpOXFppm7bsqj8_a2deAdmYCkYhpHfgmNeAkv0RZPc1DCqRYGsmHC2BKlF3p_b4bRa-4ni7gifJrJhIkqRG7SkaiMD04rtm47TQXM5xiHb4O0awYcDmk-D1ChDhYNYh9J7WAoenBXXTbiIls0mkwFJTpsCllKOgUGij1xBTVtmkrEiHrAgPTGMgQ_7aEM7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
جام جهانی ۲۰۲۶ فقط یک تورنمنت نیست؛
جاییه که رویاها ساخته می‌شن، ستاره‌ها متولد می‌شن و تاریخ دوباره نوشته می‌شه…
🌍
⚽️
از نبرد غول‌های فوتبال تا شگفتی تیم‌های کوچک،
دنیا دوباره برای بزرگ‌ترین جشن فوتبال آماده می‌شه
🔥
┅━━━━━━━━━━━━┅
🟦
آدرس وان‌ایکس‌بت:
🌐
bitly.uk/connect1xbet
🌐
bitly.uk/connect1xbet
🔓
برای ورود به سایت از فیلترشکن کشور های اسیایی یا کانادا یا ترکیه استفاده کنید
⬇️
فایل نصب اندروید 1XBET
⬇️</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/news_hut/66151" target="_blank">📅 12:51 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66150">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mwLc3E_kd6omMJ9FfZhZgiLpiztWVGomChWEVh_v3ZNOHS_1MNCoNMpUHPm1ZUzoFMKf-ZNL3HQVtDP4TY1hr77gGI-LOFAb1b_YIQ1avtFDXeOTcYb7G3rcs_Uhavc9OShNa0HT_P1_TvEBh1GEufq1nSpOWr4BebMPMqtdoxQiYFvrRjdqW45FCAaxGiXEnxQ4RFHo0EEySbnmBp_sDCvo94o_uJbToZ_PyMzYmdAi_sfmvAVssSHPPt8yohauwLyfvDTqvuXyW6x_D4sw-2jg9RMUFjaid9so2MsX4ZFPR4T9w15q-yD5W6OcS8QaLttXoJIltsOgQO0PN9_a5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
دیده شده در تجمعات
@News_Hut</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/news_hut/66150" target="_blank">📅 12:31 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66149">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OzoFA4-aZ4efdTfNZDO1gWn8j7M1sFjUFUKzKVpLhvMsmN4Uugdu2lqvZ9J6Fh3wVUnU6a7yhkJEuuq8P7h1MXDC_23sZZz8pWQSciXKpLWk5J6_ma2Vqf9lml2M2ldYRECpn7uWWt2yUTp7V1jzy5oMpU_IfG9oKHjh9GaMlxcB1jz5TLNax3zEOx_8TboMRV_85iS7796fKh1BHJbkBWx8KqdFre3EmPjnEZ3baR5QI7PURLdaFzB-UPiluVvBzKJmlP4dAnzSWUHcPT-cH4fhdH3nJRfsFba2v-kuXN8B2lSygvLgSNyqM99hwnzT5KUeSWkTm1aZS01QU0MiWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
وزیر دفاع اسرائیل, کاتز:
وزیر دفاع اسرائیل، با رد فشارهای بین‌المللی و هشدار به تهران مبنی بر اینکه هرگونه حمله‌ای به اسرائیل با نیرویی کوبنده مواجه خواهد شد، اعلام کرد که نیروهای دفاعی اسرائیل به طور نامحدود در مناطق امنیتی در سراسر غزه، لبنان و سوریه باقی خواهند ماند.
@News_Hut</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/news_hut/66149" target="_blank">📅 11:56 · 25 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
