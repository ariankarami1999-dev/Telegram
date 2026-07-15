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
<img src="https://cdn4.telesco.pe/file/HgkoQVlOyRrj3YgIiyBX1ZAUiF7bDbh8fW_S10At4-li5FNmrdSrgjlxr9heuiCmt-RiJmfAEuC_mJRkXfnL4sIDto9Gpak3xlBY9TSSDwv2vFO9dAKabIqBNsQAr3j7kp5jv_bsWQ3celvuTdUIWti89KTIj4G7HyCTPh21Jx4OP-TLyVWgqoZbfDTXuKUFDVJNCzT_GbA4m9eWSeL7WAxsMoFNw9sEcdYgTwgoZd6UETxmPp2uvIQxBJy5pbw8NjFUJudH_jiwBOdDhfEeHBWMPSWxlkoRHmXWLhrBTPncWLb-TF5dJXjKw2JTDA051HhJJh8RNNGz0eKidst52g.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 172K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-24 18:12:16</div>
<hr>

<div class="tg-post" id="msg-68179">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1331c1b8f5.mp4?token=c-uTsU-WPI0tOl5U4RUllpgsQr2xXh3E5t1wrEVpX1xaHoIs74tRJ2pMusrfZKi_q6L0-nSD05ZRawYAbhDOgw9IGwJ4zlZFZ6iDEbM51hsuIl_F2Jkvr91HH96NDAX00aWxcKt2DVjff3HIUDdjNAi6sploGUz9Clt4HVigT5Fyg58jK2ZEngpLk-CbOH2k5qsflUoIfudonz-EMleDl4oB8KhVfMCa_7cqclrLBJSezmt1z_0-kQ0LR1hiD8q-RuIbz53yien37YgVmYkP70pNtp7UVzpUtbHEb1uNSHERmuVewVckrphjFH0drZIFffqeZK3fPFWA8qW2IuPdBA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1331c1b8f5.mp4?token=c-uTsU-WPI0tOl5U4RUllpgsQr2xXh3E5t1wrEVpX1xaHoIs74tRJ2pMusrfZKi_q6L0-nSD05ZRawYAbhDOgw9IGwJ4zlZFZ6iDEbM51hsuIl_F2Jkvr91HH96NDAX00aWxcKt2DVjff3HIUDdjNAi6sploGUz9Clt4HVigT5Fyg58jK2ZEngpLk-CbOH2k5qsflUoIfudonz-EMleDl4oB8KhVfMCa_7cqclrLBJSezmt1z_0-kQ0LR1hiD8q-RuIbz53yien37YgVmYkP70pNtp7UVzpUtbHEb1uNSHERmuVewVckrphjFH0drZIFffqeZK3fPFWA8qW2IuPdBA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تمسخر لهستان و شوروی توسط چپ‌کش اعظم رونالد ریگان فقید:
@News_Hut</div>
<div class="tg-footer">👁️ 6.12K · <a href="https://t.me/news_hut/68179" target="_blank">📅 17:32 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68178">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f7f97b887b.mp4?token=eajqB25EjJmRSfrZ1uBbZ0hseEB1JE3l8KHutTBOKWNWHOVPg9d2xj_HJvV5YNCCjBLFhIob59IDH848aHaTHY9qcJKIAbVr4WDkAudk23Iz3Q-uOBD8xsusjjomaBbpe7Pt6ah4F74ZQtQg7EU68ouhfwogX1sOxbouwtE31E27oqpugX1m-JajP4tpe8IHRNVffoKqH6rLLOMU2EzLZrKhyMFCDMOy-NsOtLKZy4OjDca3m1k7oBg1So56v5399iqaRpJMsT8fmDJBO_PI39sxU_Mm45RCUYjYslaOPiT_NYe3Gam1luxkW4_xfa8bGG7GN97fDfAh5Fd9NAV-UQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f7f97b887b.mp4?token=eajqB25EjJmRSfrZ1uBbZ0hseEB1JE3l8KHutTBOKWNWHOVPg9d2xj_HJvV5YNCCjBLFhIob59IDH848aHaTHY9qcJKIAbVr4WDkAudk23Iz3Q-uOBD8xsusjjomaBbpe7Pt6ah4F74ZQtQg7EU68ouhfwogX1sOxbouwtE31E27oqpugX1m-JajP4tpe8IHRNVffoKqH6rLLOMU2EzLZrKhyMFCDMOy-NsOtLKZy4OjDca3m1k7oBg1So56v5399iqaRpJMsT8fmDJBO_PI39sxU_Mm45RCUYjYslaOPiT_NYe3Gam1luxkW4_xfa8bGG7GN97fDfAh5Fd9NAV-UQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یکی از وایرال‌ترین ویدیو ها در 24ساعت اخیر در توییتر فارسی
😂
@News_Hut</div>
<div class="tg-footer">👁️ 9.47K · <a href="https://t.me/news_hut/68178" target="_blank">📅 17:00 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68174">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/reX_HdEnuXf3Un24NHzgo9X6ruzriFMWKEsa7QYNUMT0ysAw1R63l9qCF59jUDgssLahTtDCKNnIttmw8u_NgrGd0ULaPq3xEe-tk1q0fQ8vFb3716iZ9yQ6eYqReum5I1wZpDdTSDP6Nw6WzBmeN4LgAWKyd2Ku7y679XNveuxd6juBNIjyWoZZ0kRLeayWRLUCxJ3x7_0z7BosUFLLktV7QYP6E0ayGfUAEG2NlD0LjwDwTOZo_2oY_Ghl-cehM8YtwWK-V7IhenFZyU1eFwbY6EtQMXuIzN6ygXEMW_vgclUoS-yQeXconHbVa-e-dFT_GNP_Hzeme14MSbk9DA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c5effcc1b8.mp4?token=wAuTyie6caxrmKj457tUEvo6DmdyHhtHFos7Eo4yVf9TwVXSCMbEnU8Li8Q4qjxPf8s77X5qywfW4BPxDpj6BTuPqCFyhn5q8oNTNotHs5HujCmNrEHheJ8l8mH8s_DXWSu83LcGQTWoVsGmeEMXwSI3Fkii_hL-K5_aPIzj4ryQGRRQNJ2QiMyIyOq7L4sWufBpPlBNWqxO6FaSA-ZjqRCWlK5eIT1Bl62WErPstHpVSAHoFSiSQq7jeuBqnzGq8xO0pfmVKt-AXmwkfwiTc73ksciaGDz96ry0AsfvlkomJPnJeRm6JoTMsjPrzS2YeRdkOg9XzimKgVzZB121wg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c5effcc1b8.mp4?token=wAuTyie6caxrmKj457tUEvo6DmdyHhtHFos7Eo4yVf9TwVXSCMbEnU8Li8Q4qjxPf8s77X5qywfW4BPxDpj6BTuPqCFyhn5q8oNTNotHs5HujCmNrEHheJ8l8mH8s_DXWSu83LcGQTWoVsGmeEMXwSI3Fkii_hL-K5_aPIzj4ryQGRRQNJ2QiMyIyOq7L4sWufBpPlBNWqxO6FaSA-ZjqRCWlK5eIT1Bl62WErPstHpVSAHoFSiSQq7jeuBqnzGq8xO0pfmVKt-AXmwkfwiTc73ksciaGDz96ry0AsfvlkomJPnJeRm6JoTMsjPrzS2YeRdkOg9XzimKgVzZB121wg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
ویدیوی منتشر شده از انفجار در چابهار صبح امروز
@News_Hut</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/news_hut/68174" target="_blank">📅 16:15 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68173">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3d7965cf40.mp4?token=N4lXkAEW7-4abtyWuo2Doca0JrqisR8H6O6aF8a0Mm1w2wkdRsYRLFzYHR4Cl32bBokf2QLkq8bYjy7NF0WEtjSKXODVVwF3HEnaV4goodS7P9t5JyKJyFRzfaF2LNQD-zZ23TDB3rE3lsxYmV_Tb7u9ZEeU5yfA2C6l9xlik6risOrLT-er9QBjo8tgBfc8zdg1YdmrhggKFZJAyGCfQKC7PFi9JGS0mu4xfxomJgoqt3jaO8EDA87CZXV6D4P_deola93FUfIVcDUImPFH8UvntnzJYRs7QQ2cHbCMFJN-KE8FYei-sHjBjQTztIePQP4MYDNpYkhiuJhNyFopRQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3d7965cf40.mp4?token=N4lXkAEW7-4abtyWuo2Doca0JrqisR8H6O6aF8a0Mm1w2wkdRsYRLFzYHR4Cl32bBokf2QLkq8bYjy7NF0WEtjSKXODVVwF3HEnaV4goodS7P9t5JyKJyFRzfaF2LNQD-zZ23TDB3rE3lsxYmV_Tb7u9ZEeU5yfA2C6l9xlik6risOrLT-er9QBjo8tgBfc8zdg1YdmrhggKFZJAyGCfQKC7PFi9JGS0mu4xfxomJgoqt3jaO8EDA87CZXV6D4P_deola93FUfIVcDUImPFH8UvntnzJYRs7QQ2cHbCMFJN-KE8FYei-sHjBjQTztIePQP4MYDNpYkhiuJhNyFopRQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
فرماندهی مرکزی ایالات متحده:
فرماندهی مرکزی ایالات متحده (سنتکام) در ساعت ۷:۳۰ صبح به وقت شرقی روز ۱۵ ژوئیه، دور دیگری از حملات علیه ایران را به انجام رساند.
سنتکام در جریان این موج عملیاتی ۹۰ دقیقه‌ای، با استفاده از مهمات دقیق‌زن، سامانه‌های پدافند ساحلی و همچنین محل‌های نگهداری و سکوهای پرتاب موشک‌های کروز در جزیره تنب بزرگ را هدف قرار داد.
این حملات توانایی ایران برای حمله به کشتی‌های تجاری در تنگه هرمز را بیش از پیش تضعیف کرد
@News_Hut</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/news_hut/68173" target="_blank">📅 15:46 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68172">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from[ 𝐇𝐨𝐭𝐍𝐞𝐰𝐬➕]</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e23686eac2.mp4?token=jJybG_j8CZIMRmM95r6w7_AXS8H4fZZz7oprod7rvGQYHHp4FxZWztIl3xTEB11UU-buAWzrlLaCmrStBj337nPx0gK3OSe5Gi_g7mZtSU7Zzj_A64Vif4pGRZVbNwSpWORrz_eCi0PEN3Fn2vcc7w-kocDOeB752DYTizgX_YV8m7lpwfxQdo40IFkvUMLOGAZTTAOrRrZEMDc5nvRfvlBaZmCb4voz-H0iYHu8wrFOlb5aNlDRLl_r5pj9jFGPq9h3bUMcbjtAr1M5Ye8nGN0Mlt61CiDThGvV5jzboOSu_sFls736oZGKZyzNlJcksVtnqx1bgPnIrJQfL3sZvA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e23686eac2.mp4?token=jJybG_j8CZIMRmM95r6w7_AXS8H4fZZz7oprod7rvGQYHHp4FxZWztIl3xTEB11UU-buAWzrlLaCmrStBj337nPx0gK3OSe5Gi_g7mZtSU7Zzj_A64Vif4pGRZVbNwSpWORrz_eCi0PEN3Fn2vcc7w-kocDOeB752DYTizgX_YV8m7lpwfxQdo40IFkvUMLOGAZTTAOrRrZEMDc5nvRfvlBaZmCb4voz-H0iYHu8wrFOlb5aNlDRLl_r5pj9jFGPq9h3bUMcbjtAr1M5Ye8nGN0Mlt61CiDThGvV5jzboOSu_sFls736oZGKZyzNlJcksVtnqx1bgPnIrJQfL3sZvA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">از جنایت ۱۸ و ۱۹ دی ماه؛
تا مدرسه میناب و پادگان بمپور؛
نام‌ها عوض می‌شوند
اما قاتل یکی‌ست:
جمهوری اسلامی؛
حکومتی که برای ماندن؛
ایران را می‌سوزاند
و جوانانش را قربانی می‌کند.
#hjAly‌
@News_Hut
|
@HutNewsPlus</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/news_hut/68172" target="_blank">📅 15:28 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68171">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YH2YB2xHWxPkLmVM5QmmIqa9C0SUNHL5X9GPnC4_A01lE8ccI5iOqnrfXyoYwjZy0TeAqDUW89PApUftrKvP9iyM6prqZVBa_gULQvvRshlogE7kHVlv6_pC10ztL0efZNKq3V8KI1MJFBM5nI9jCOrlVcu89CtK6w0uZT6LqexBENaWk49SHLzFkLaX-cv4B46jpcs5oPsBLDPS4BvN7n9BBx1kmCQ9TcwgnAwV6s1wDe7lxu4_krXeWNzwoidHvKlGa7K_Pq7twzNmMe73oI83d2l-AfxXF5SnbH9VSUioEQ_Hw6twq0uCWT2yJ7NRqN_mQdaatR0bHQBkvNxyKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استوری حامد‌لک:
@News_Hut</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/news_hut/68171" target="_blank">📅 15:07 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68170">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O9X-czq37V2TTSOYic44sVS16_l0-200VEJF7diyHqlcSEiOMMGrcsHKEEVwbWbVQo9Zv13Ej7QdkY5xFk1MXlTiqaXxDZiiGfmvuCvQUpQe8pxnJDRnwy0z6cw_yLqBCWETR7W-Iolw2nFUnRaGTBYEJsFY7eHXnwBTO96mQsU8QZR7uYz0HZviIdUvYaHfzj0xVTGugaiBRZxWoLouW97gCsMQb6dVC06z8y5XXHRvNmjHhbvD2Vttxufxkyf9AJvFm_xLz9y5SoIPGO4IlZPMVjGh7actWM2PS_XyQJM9LLWlkRt-8xxUSRsy0ul09YdRWYuKXBMlJbh9yxMsag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
چهارشنبه ۲۴ تیر ۱۴۰۵ جام جهانی ۲۰۲۶ مرحله نیمه‌نهایی
🏴󠁧󠁢󠁥󠁮󠁧󠁿
- انگلیس - آرژانتین
🇦🇷
ساعت ۲۲:۳۰
ورزشگاه؛ مرسدس بنز آتلانتا
@News_Hut</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/news_hut/68170" target="_blank">📅 14:45 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68169">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🚨
پنج انفجار در بندرعباس
@News_Hut</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/news_hut/68169" target="_blank">📅 14:43 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68168">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">علاوه بر اینکه سوالات یکیه و باید همزمان امتحات گرفته شه، تسنیم اومده گفته فقط نهایی دوازدهمیا تو روز ۲۵ و ۲۷ لغو شده، این درحالیه که دوازدهمیا اصلا ۲۷‌ام امتحان ندارند و یازدهمیا دارن!  باید منتظر واکنش رسمی اموزش و پرورش باشید @News_Hut</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/news_hut/68168" target="_blank">📅 14:27 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68167">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mob3k5bTCFsYS5Lw6jMlkYTV6BkVwbphH5EpTBWgk-b4FGqv1okbsDBGonMdia6sbs97Xb3Je-Z3KR6njnPU4D5eVlbtHFY_f0sBAcTmr60mcBiTdfy5_sFa7LMwUl3XgzZKBrchtGcTwUcVV5WpEwAUNnra-MeNM9-0StHsfm8dHOtxTwX7w13A94GZa8Cmvq4NXNF99eBVhySHgz50uPzuUYZGBCr05kd5KDdKyPfHokgy7j14RXjGWccxKChn4JSSoVkjkijq13vDq386TNNvRcZkzYDqI4EwSFsBxrIFdGOU4idXjdJFvlm02rUAbYkhNMMRL4x5vDHBrgYd5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چطوری نهایی رو فقط برا چند منطقه لغو کردین، کاش این دو روز کل ایران رو لغو می‌کردین تا فاجعه‌ای دوباره مثل میناب رخ نده... #hjAly‌</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/news_hut/68167" target="_blank">📅 14:24 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68166">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ce063673b4.mp4?token=gzfBSuBd8qCsD1gm6qjFONEVJ12y7zrp7ruBtSzsfJ3QIos9Yi9KiBpEyxNnuoGEeY-AV044HtlVHEh7Ak59v_1O7QYPtwGejaH7KuRtPb8wLwI6foW3MZAMtSi7lb2IZdqEAW0hT4-yVWprhtwxzPcdLiisFiJkNCVvrPoX81DVulnY-aMjfOGVw3zThs-JmyN5PAQd63LGdyBY174oJuovU2n8n7kMXBXr6_sVlykLVGYcE9JeC6VwSkGFFSOlpvpd_onfAtn3f8d8etbS82E-VM1f8ksrMmJrcUiEV-P6D9KBZ-dFQVH8wBhoOsLjVij7GJZNILzehi3tZ7Qhjw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ce063673b4.mp4?token=gzfBSuBd8qCsD1gm6qjFONEVJ12y7zrp7ruBtSzsfJ3QIos9Yi9KiBpEyxNnuoGEeY-AV044HtlVHEh7Ak59v_1O7QYPtwGejaH7KuRtPb8wLwI6foW3MZAMtSi7lb2IZdqEAW0hT4-yVWprhtwxzPcdLiisFiJkNCVvrPoX81DVulnY-aMjfOGVw3zThs-JmyN5PAQd63LGdyBY174oJuovU2n8n7kMXBXr6_sVlykLVGYcE9JeC6VwSkGFFSOlpvpd_onfAtn3f8d8etbS82E-VM1f8ksrMmJrcUiEV-P6D9KBZ-dFQVH8wBhoOsLjVij7GJZNILzehi3tZ7Qhjw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
خسارت وارد شده به یک دکل مخابراتی در بندرعباس پس از حمله آمریکا
@News_Hut</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/news_hut/68166" target="_blank">📅 14:20 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68165">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">🔴
#فوری؛ امتحانات نهایی رشته های تحصیلی پایه دوازدهم در ۴ استان لغو شد.  وزارت آموزش و پرورش:  بر اساس تصمیم ستاد عالی آزمون های این وزارتخانه و با توجه به شرایط خاص کشور در استان های هرمزگان، بوشهر، خوزستان و سیستان و بلوچستان، امتحانات نهایی تمامی رشته های…</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/news_hut/68165" target="_blank">📅 14:11 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68164">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🔴
#فوری
؛ امتحانات نهایی رشته های تحصیلی پایه دوازدهم در ۴ استان لغو شد.
وزارت آموزش و پرورش:
بر اساس تصمیم ستاد عالی آزمون های این وزارتخانه و با توجه به شرایط خاص کشور در استان های هرمزگان، بوشهر، خوزستان و سیستان و بلوچستان، امتحانات نهایی تمامی رشته های تحصیلی پایه دوازدهم در روز پنجشنبه 25 تیر و شنبه 27 تیر لغو و به زمان دیگری که متعاقباً اعلام خواهد شد، موکول می شود.
@News_Hut</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/68164" target="_blank">📅 14:01 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68163">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vTREpeG0WWP1u_9yHIJyRZ8bnr_v8JluCYPU5_Q1lw_CZHkaH10aTqy5yl5df8DyChhY2HrRIq22TlEE0tvdXB3PWS4NsThBv72xvf1HkCs7WT0w5R-A4co8ja0vYFMvf8Vb2tKaKGcXQ3dInkk2GnZSUUm0_TOZrcR_nB7cw4uPc7vgDO0Rn_hg0aVebKoV1JV-zNHlgSn1eMVTrFDZYeZ0UZkQZRSbyijCOpv9AzqcCrZmL6TTaycIlYtVvhr45H9EinAvNIpxhc9MMh3OXldd9UPaw0xrTRRF2CKRY8EaBLoVN608fO-MLzkC6QjQz8IaEHtBZ-lEcPlYEidDPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
فرماندهی مرکزی ایالات متحده:
امروز ساعت ۶ صبح به وقت شرقی، نیروهای فرماندهی مرکزی ایالات متحده (سنتکام) موجی از حملات را علیه ایران آغاز کردند. هدف از این حملات، تضعیف هرچه بیشتر توانمندی‌های نظامی‌ای است که نیروهای ایرانی برای حمله به کشتی‌های تجاری در تنگه هرمز به کار گرفته‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/news_hut/68163" target="_blank">📅 14:00 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68160">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/O5ulyIA5lgEjKoVDcgr42_Z8UHT8ZC9JOBYKfYRC8cZs1Mjgr8fMVilKXmLsniOXMdySzOiAS5qmaiIhN63P7eV8kIsE_gLahIjdp2yXGW07XlZOWMhTTPg-IHQl5WTQ9ifidtNJuAqRORwPfQuwtuE8b1EGNi-iL_gmm7OkmUMesn5snSEgjvTlGbCNgEYoHMrTbGBfJrBPnCwEZrobIO1dWjXTbxkhhdLbxoomUo0fY3doOWTPviVW_ddqAmMi2rVq3uIREBrIWq2EQlP00zzfpbcGEPKXQ2o_FiBzG0l5XFc8Q3c1vbxBZmzHTY84eniRMStSCRnUGd1DOMoqww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Xqq6frW29p1hT0w_pGQZ_gAl48N3MdaG4E2wM_sOuZSirvXNJNBN0zVWyafLktktr2h_Y-b0L-xABv1YfthG0HMbS8tJL-CYCF5HlvG7ujotFl_SAfVvzAJd8WRSL9_MxEB3PyCWvQH3T1x2VW78WAyH1u5porKKxWj5_IXDsQ685wKlR3xmCZHnKhqvLguxhKmnx-QZ0L9JjFq8scyTxYUcYXeS8dXrg4-_7czo3LS2E_H8mZBrH1K3BZ8XNs706rmxZZUIOGtgHxqvVrDGRYzqIA1BOhSfSWRvF6Wq4FcLylDiBmoAmEadP_mo43IFVmczZiFahTkIOVytcYI1lQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a57f3aee50.mp4?token=qmuglpwepclI_3JhYCaTIMGPcCVPbc7KxpKOjJJSTNezzfFCftgktFwmqa1POlpYn_C0Fa7L9fX-XwizjLX5_sYJiWxNZq3XBc5nDqPoufy70PGjtbhO6qZ1TPDq7NwOwB2RheF-3DKSn9zBcju0tG8KsV5gLrmBSCpC9XAMkOEPMlm7PhEXiZ8sRJE3jhMm_tVQMCYFD8MvX9jh2gIRiEOkwRUP3HcKChd5jY69JhW8iQi1Nc20V54blbeObEqLYD5RpG6XbwCJcvK_R3WmeVAr-RzTwCQ_jZaC3XADDRV5cC3ku0fZdzFbAIiqs_cWohF9Ml9nVC0_rmXJTiS3zQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a57f3aee50.mp4?token=qmuglpwepclI_3JhYCaTIMGPcCVPbc7KxpKOjJJSTNezzfFCftgktFwmqa1POlpYn_C0Fa7L9fX-XwizjLX5_sYJiWxNZq3XBc5nDqPoufy70PGjtbhO6qZ1TPDq7NwOwB2RheF-3DKSn9zBcju0tG8KsV5gLrmBSCpC9XAMkOEPMlm7PhEXiZ8sRJE3jhMm_tVQMCYFD8MvX9jh2gIRiEOkwRUP3HcKChd5jY69JhW8iQi1Nc20V54blbeObEqLYD5RpG6XbwCJcvK_R3WmeVAr-RzTwCQ_jZaC3XADDRV5cC3ku0fZdzFbAIiqs_cWohF9Ml9nVC0_rmXJTiS3zQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
تصاویر منتسب به شیراز
@News_Hut</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/68160" target="_blank">📅 13:33 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68159">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Cgl-FE-AId9EfE33vkQmh03MiX3Zm7SO_EeRRybQJJWz4aUOnPc01Uo2TsRpzuG5hmNny0SrOjFS9VI2ZBeqLN-QpZpAvv-tQI2SbVfUPU19CpmgJAyQOcdidJ0iHScYVnYYbPod3XomQxdX2uqIPW4VC2bNX4A5tIgEKRAEuOMgbJ_WH3Q3IOh6vGSY07IwlKjHrSU0jeW5syn1rZAcAcGTEEdZOOBcX2rXkI5ljQnd-ygsWaKtA8p2KxL0tqmteO7Vkf0M-aQO024L2_bmLOEukYV-nhBuAB6sEfJ5TRcT2ascs2rgb0JUVvdVmdbVvtj-OdYr5CIL1jQ7Yfbhgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
گزارش های اولیه از انفجار در شیراز
@News_Hut</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/68159" target="_blank">📅 13:27 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68158">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DSb6YbkDsdjsf2xE6FyrG54zwlSnCPYREhjz-fdJWdRPJDmYgyv9WOsCKCd_gFQ770U75nLd3WLtDQHsz5Ve8aGi0rt9DxWtF99o-YqVmuIzpUtGX5e_Ql4rPSXQFqw7xigekGtuJ_HmFgor9mUeYrK1yLXs9VGNT1X4rxzKENXPdvEkrZirNHPkHa7KrmAauZo1a4Lk888E1CEppoCtXVhjjhXwqZAkUaVrcvJvDKeUfN4CDvefzgjiSd1MEQWsoQtleCwDdJvvVqDyAGjy_P3XQl9tMdmNL19TzNDgXIgmUQ0ELAvBIvQNdjp7OGf8-SyYpskqTF7Raaa6fkhFAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مادرِ داریوش فرضیایی (عمو پورنگ)، بعد از تحمل یه دوره بیماری، تو سن 90 سالگی درگذشت.
@News_Hut</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/68158" target="_blank">📅 13:04 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68157">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">‼️
امریکن گات تلنت یا همون عصر جدید آمریکایی ها
یک شعبده بازی توش انجام شده که حسابی وایرال ‌شده
👀
@News_Hut</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/68157" target="_blank">📅 12:37 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68156">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UUycoNi1XiH2PJW-FETCaRowVvaTZkXcLvnXpR2Xs6n-RbumbHVhJ1_K1TSwhcW0IXdk-CDL7M7KQsFPwZRehs4NrRFKXlDtMzafyaySMGeZ_s602U2X8B_tHoZvjd0D1LA-yGP_xJZ33eQCR-k6aaN3nlp2-8NDBJhP6nKL5Z4FGWGcIdQh2wj6AntTnkA9HjqSNHNNgcFgKLdAXGfJyKq1Gipjhjy15Oab_dM8j0-JHgu-Cqzm5fxUVs12IS0Ms12mJCVswwkf-KfazcRcTfBo6W5KEMYPD8Z1CJ5PvT0CeSi1p1-1VRu04xleiF6SQmEpM4eKigFL_PiI3mTA7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
ا
کسیوس:ترامپ در «اتاق وضعیت» جلسه‌ای درباره حملات جدید و گسترده علیه ایران برگزار کرد.
به گفته سه منبع آگاه، رئیس‌جمهور ترامپ روز سه‌شنبه جلسه‌ای را در «اتاق وضعیت» (Situation Room) برگزار کرد تا درباره یک عملیات تهاجمی گسترده علیه ایران گفتگو کند؛ عملیاتی که دامنه آن وسیع‌تر از حملات کنونی در اطراف تنگه هرمز خواهد بود.
به نظر می‌رسد ترامپ مایل است جنگ را تا حدی تشدید کند که خسارات کافی به بار آید و در نتیجه، حکومت ایران تنگه هرمز را باز کرده و خواسته‌های هسته‌ای ترامپ را بپذیرد.
ترامپ این نشست را در حالی برگزار کرد که ارتش آمریکا برای چهارمین روز پیاپی، حملاتی را در منطقه تنگه هرمز و در امتداد سواحل جنوبی ایران انجام می‌داد.
@News_Hut</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/68156" target="_blank">📅 11:59 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68154">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eb5c420396.mp4?token=Fa2TVgepk4k9bKciLZRdGcr9X3xoAu74Eyx16eq5P_J2ntj56mvDOD68z04vEoMigiTxmIhaiCfsytfEAMai1_roTznuF7LD1IUoHm-Ox85Kxe5wEwQ98okBx_i9Ek-APVVJ36qJvfk5A-3I6OkHyfp_dfzigSmqgVKuRkzQ3J_cBReelqPN70gboCGuJ_FU5-dTHbiTN1ezbxjrAujNfi6pJqJIfdhi_w_RDPz0kFr6j86jlf-pgdyHpDsXWfSEfRyc_DyorN3l-GvAHHuu4Tf8rIW6UESkufbdlOFjZpFVwE_2nRsW9NMtSIuHxZdBygZqr3hWBEhMJ1aTd5Bd5A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eb5c420396.mp4?token=Fa2TVgepk4k9bKciLZRdGcr9X3xoAu74Eyx16eq5P_J2ntj56mvDOD68z04vEoMigiTxmIhaiCfsytfEAMai1_roTznuF7LD1IUoHm-Ox85Kxe5wEwQ98okBx_i9Ek-APVVJ36qJvfk5A-3I6OkHyfp_dfzigSmqgVKuRkzQ3J_cBReelqPN70gboCGuJ_FU5-dTHbiTN1ezbxjrAujNfi6pJqJIfdhi_w_RDPz0kFr6j86jlf-pgdyHpDsXWfSEfRyc_DyorN3l-GvAHHuu4Tf8rIW6UESkufbdlOFjZpFVwE_2nRsW9NMtSIuHxZdBygZqr3hWBEhMJ1aTd5Bd5A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
لحظه برخورد پهپادشاهد ، به طور مستقیم به یک انبار در کویت
@News_Hut</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/68154" target="_blank">📅 11:15 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68153">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C_7LcqiU8Wb7cycX4oKC9CtrAMEqb_nkDlkBtyail6s4jkadw5BJEJTLHE-zNWc6SKiFYSNBNDuuSbQM0HA3gFZTP0mmzsz4s80jhEFeokC32paFz_sJ5eHjdgrYZcMhHiROckb5K1fG3sqzk2OGp5bHS_LKK4l8RU6T0Zl5fgtCUu3QllIpxwSGNJVgdmrVM3QLJF-xTs0WFmYIXisvoJBMCEmTXu1kGd3IzquJ_o73baPlKpN1grgkJNKd9tpSRRf11Exlw98t6R2OK6RlIIlTke_tf4qbpwFywyf2xfFTqAWgsAk_nt2iAs7z5fFK_89ov0sVa-J61nVZOKixMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عقل بچه‌ شیعه‌ی آخوندپرست
🤯
🤯
🤯
🤯
:
#hjAly‌</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/news_hut/68153" target="_blank">📅 10:52 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68152">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/31c4cf4b27.mp4?token=UpbnVsr3-9iZPvbFpNTlC2jXb6x4EIVHevgha63hdCDdCMAfz9AHBcMKbWJrk4dA8EsrToOC77-QcrJLAQ7l0NzfpsqQoPQFQAR8bOl3b7j7tG43O8-gaOYlH4m6ALpCfKnlBGrgwuTGse5J4f-dvwe9qGxQAtKDUQxoGY-1s5b7wiDeB2EaoV5tH17RT_BwHuiJO19Clfi2Zlj8I8ZBTdVwzDSWJwgpciAz0ZK6lY7N4p2yELXmA2nBLOKvSktXpqVERHg9IIa9UX_-uMVLnXZxYQd-wwr3mIl5VP0PjQEoNl787uAsJCm-2MUN_yvf9Hp8diU0VInbPN276pv57GaO3-QYHx5yC-lquL6C-GejEhA9AvoJ9eXgxC2whSbm9pdXCfYn2ACsicIkGFwf0ZidVSO4IDvHBzzPK5lvp-7IoSFM1BOCUhq_RF3bN3mJ5ZrHoIeyo7fb6Cpa6coDld_Lz_8JkMBE8bpFiREIthUpnNtt30cfKeDzLxUQXfmbivDPcfvR2IUfRLua03JZCd3rzgtz33WoJNFHfU4-O4Va26KeYs1z7ZtDryo7dRLNMKRFJEWTbqEZC8koM8s60kUrcnFe7NK6y0Rg1wZFKgeOf2NQI8FqdVzG3xYTq0pTow7fU81bAZoG7nKoUqx8GgnCYisgYznfMOAjKFWOiO4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/31c4cf4b27.mp4?token=UpbnVsr3-9iZPvbFpNTlC2jXb6x4EIVHevgha63hdCDdCMAfz9AHBcMKbWJrk4dA8EsrToOC77-QcrJLAQ7l0NzfpsqQoPQFQAR8bOl3b7j7tG43O8-gaOYlH4m6ALpCfKnlBGrgwuTGse5J4f-dvwe9qGxQAtKDUQxoGY-1s5b7wiDeB2EaoV5tH17RT_BwHuiJO19Clfi2Zlj8I8ZBTdVwzDSWJwgpciAz0ZK6lY7N4p2yELXmA2nBLOKvSktXpqVERHg9IIa9UX_-uMVLnXZxYQd-wwr3mIl5VP0PjQEoNl787uAsJCm-2MUN_yvf9Hp8diU0VInbPN276pv57GaO3-QYHx5yC-lquL6C-GejEhA9AvoJ9eXgxC2whSbm9pdXCfYn2ACsicIkGFwf0ZidVSO4IDvHBzzPK5lvp-7IoSFM1BOCUhq_RF3bN3mJ5ZrHoIeyo7fb6Cpa6coDld_Lz_8JkMBE8bpFiREIthUpnNtt30cfKeDzLxUQXfmbivDPcfvR2IUfRLua03JZCd3rzgtz33WoJNFHfU4-O4Va26KeYs1z7ZtDryo7dRLNMKRFJEWTbqEZC8koM8s60kUrcnFe7NK6y0Rg1wZFKgeOf2NQI8FqdVzG3xYTq0pTow7fU81bAZoG7nKoUqx8GgnCYisgYznfMOAjKFWOiO4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
آخوندها عُمر طولانی دارند و بیشتر از عمر متوسط ایرانیان زندگی می‌کنند:
@News_Hut</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/68152" target="_blank">📅 10:32 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68151">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a1084df804.mp4?token=Q1BGC3O5EmxISNXLm56qBHbz0sgVMyKmW8Pfzaw1TgLiNKWWptbSNfB-RNeSE2kogBcwwbdItabXHwDd8uF-zOC7siNLVHvU6Y6-fePt5OIpZGnghf_Ud-yskwchsdlfymwZH2cNlvmWY1FCj3u192XpO3ab8qn6L9XGsFuqvYeG2k8KplfI7jDGbEpfHAvc3lpQuIyn61L0e0wN-uT_MXL3e2M-MS69epuz8-HXcu10OoyrparSmbFh-EDb1MdN1mIy0n8qaganoNm-N57qxUZ967bDrYUY2EB1IWSpLQoBpjvIEOHjyYezvhNMYL6ENwzxGTdc5Z9oIakMqkF0fA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a1084df804.mp4?token=Q1BGC3O5EmxISNXLm56qBHbz0sgVMyKmW8Pfzaw1TgLiNKWWptbSNfB-RNeSE2kogBcwwbdItabXHwDd8uF-zOC7siNLVHvU6Y6-fePt5OIpZGnghf_Ud-yskwchsdlfymwZH2cNlvmWY1FCj3u192XpO3ab8qn6L9XGsFuqvYeG2k8KplfI7jDGbEpfHAvc3lpQuIyn61L0e0wN-uT_MXL3e2M-MS69epuz8-HXcu10OoyrparSmbFh-EDb1MdN1mIy0n8qaganoNm-N57qxUZ967bDrYUY2EB1IWSpLQoBpjvIEOHjyYezvhNMYL6ENwzxGTdc5Z9oIakMqkF0fA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
پیش‌بینی پروفسور جیانگ از تهاجم زمینی به ایران
:
پروفسور «جیانگ» تحلیل‌گر سیاسی مشهور در گفتگو با «پیرز مورگان»، مجری معروف انگلیسی، پیش‌بینی می‌کند که «نیروهای زمینی» آمریکایی از اوایل ماه دسامبر در ایران مستقر خواهند شد
.
@News_Hut</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/68151" target="_blank">📅 10:02 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68150">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sVdJ435VMxio0Hatvl7G7CPS6tOuVa1e6AEVJMl5uksUvq0c0RiZCg3kakIqUKOaqDBUF95glsGS2dka3_hzkPmYGI1aPE_lpggYyhsjkmyVOUw9SU9yac9LG6N_w59wif1Pwr_X4j8aGNoC3jOLszGW8GGEDFyiiQTw-8n_uZn5wARr2NtIoOAlVQGCcyRu6g66xX1e4RcYV2TBHVsboqUgrg6i_8tutOMclWKcjQfp9Ybwi9_pwtBkA7LAraGwh3gNITx6Xpq39BPATaiEgWRerUhHwgV-gUeCYe2Oj6Fvjmo9rlamSB3idbBTC7PkXBor8YoiHdt09vIFiz_P9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
ترامپ: کوه کلنگ ممکن است یک هدف احتمالی برای یک ضربه بزرگ و سنگین، درست به درِ ورودی باشد.
کلنگ گزلا (یا کوه کلنگ) در استان اصفهان و در نزدیکی شهرستان نطنز واقع شده است.
روزنامه تلگراف پیشتر گزارش داده بود که تأسیسات تازه‌ای در مجاورت کارخانه هسته‌ای نطنز احداث شده است.
این مجموعه در عمق ۱۴۰ متری زمین و در دل کوهی به ارتفاع حدود ۱۶۰۰ متر، موسوم به کوه کلنگ گزلا یا همان کوه کلنگ قرار .
ارتفاع این کوه تقریباً دو برابر کوهی است که سایت هسته‌ای فردو در آن ساخته شده است
.
@News_Hut</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/news_hut/68150" target="_blank">📅 09:15 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68149">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/93235f7cc4.mp4?token=DVLHCT_R4pZW8iWbVD8xNhMf7Q12We0-INHhaedB5Tuu6_0Fl89N86PeOFF3ZuazAMStSnmKoC-jYDu7fGmI4kCS0mowUhfxY9GPvPAKkJUZyG1CKUQeHBqnWS8mWAvV695m5D33ZZsHNZ5MZzjHvsDnVttJXrBmuRLQHz3lzn9tFawzjknh1mmNPBZkx7ftiHM3y2YqUKaQoMfjYbUWIYTUlBA_vFXyBVcDr1HWBELAeo-qq03RbUs7TFewbg8OPZ0RHjSkkAqNrjXRUyO8RbRiVTYRlqLpPZBkSJ7-2tm5XoULjp1kYhLKNjLZFKWSGoMEpT-uoFL5whUREf76uA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/93235f7cc4.mp4?token=DVLHCT_R4pZW8iWbVD8xNhMf7Q12We0-INHhaedB5Tuu6_0Fl89N86PeOFF3ZuazAMStSnmKoC-jYDu7fGmI4kCS0mowUhfxY9GPvPAKkJUZyG1CKUQeHBqnWS8mWAvV695m5D33ZZsHNZ5MZzjHvsDnVttJXrBmuRLQHz3lzn9tFawzjknh1mmNPBZkx7ftiHM3y2YqUKaQoMfjYbUWIYTUlBA_vFXyBVcDr1HWBELAeo-qq03RbUs7TFewbg8OPZ0RHjSkkAqNrjXRUyO8RbRiVTYRlqLpPZBkSJ7-2tm5XoULjp1kYhLKNjLZFKWSGoMEpT-uoFL5whUREf76uA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
رسانه حال‌وش: شدت انفجار به قدری شدید بوده که در لحظه اول حداقل ۱۰ نفر کشته شده است  @News_Hut</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/news_hut/68149" target="_blank">📅 03:30 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68148">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">🚨
تا این لحظه ۲۰ نفر زخمی و ۲ نفر کشته شده  @News_Hut</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/news_hut/68148" target="_blank">📅 03:22 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68147">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🚨
تلفات امشب نیروی نظامی در بمپور</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/news_hut/68147" target="_blank">📅 03:06 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68146">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🚨
تا این لحظه ۲۰ نفر زخمی و ۲ نفر کشته شده
@News_Hut</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/news_hut/68146" target="_blank">📅 03:04 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68144">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7a28218ed6.mp4?token=gIr3DT7l8mKcD4pOkQHUMKS7I1zt6XXuLbSHEqFCWBCSDIBXUlWF0y0rpL1pFdte1wuOIpHrBdK8YduSoqUuxfkRves14v7HJKpe8lID5pEfjDWqfxstg6ncobhDARcU5JqJ7R2bBMvzjwdclWMOZ24d9wCalSge6d_yfhVQ5AKExfbHBF22rQBWWPgU7cqfai5Z_l642XmizVxJeddl4pA7SIXPM8MBNK0EfsDdockPvUH-2cAHBpBAyDrfb3DlH8bYwhL1kT8e3AD6341CwwTNXaHl0k7esvzEEfpAvdPN_WUmdiT0_fIiq6WJ1PTYTO2P02I8QmbnANpyAogqZg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7a28218ed6.mp4?token=gIr3DT7l8mKcD4pOkQHUMKS7I1zt6XXuLbSHEqFCWBCSDIBXUlWF0y0rpL1pFdte1wuOIpHrBdK8YduSoqUuxfkRves14v7HJKpe8lID5pEfjDWqfxstg6ncobhDARcU5JqJ7R2bBMvzjwdclWMOZ24d9wCalSge6d_yfhVQ5AKExfbHBF22rQBWWPgU7cqfai5Z_l642XmizVxJeddl4pA7SIXPM8MBNK0EfsDdockPvUH-2cAHBpBAyDrfb3DlH8bYwhL1kT8e3AD6341CwwTNXaHl0k7esvzEEfpAvdPN_WUmdiT0_fIiq6WJ1PTYTO2P02I8QmbnANpyAogqZg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
تلفات امشب نیروی نظامی در بمپور
@News_Hut</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/news_hut/68144" target="_blank">📅 02:57 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68143">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">حرفای امشب ترامپ رو گوش کردم، یجا گفت فعلا نمی‌خوام باهاشون مذاکره کنم، تهش گفت اگه تا هفته بعد نیان برا مذاکره پل و نیروگاه‌هاشونو می‌زنیم
😐
#hjAly‌</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/news_hut/68143" target="_blank">📅 02:55 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68142">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">از تبریز دارن اردن رو می‌زنن، جالبه از پایتخت اردن تا مرز اسرائیل فقط ۵۰ کیلومتره، ببینید آخوندِ گنده‌گوز که ۵۰ ساله می‌گه اسرائیلو نابود می‌کنیم، امشب جرئت نداره ۵۰ کیلومتر موشکش رو اونور تر بزنه :))))
#hjAly‌</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/news_hut/68142" target="_blank">📅 02:38 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68141">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/43530d8c1f.mp4?token=MHEcUmOHZy5qZJHshAL1WCUrShmopCmfyZBvNEKgJ0m4Qk9futuin7Un2qEF200C46RTMRakp5VywjcriG3PaA7089tDff98dnCWsc21UFQ2vQt5LG769gjYuoNxmfrtq-PJLTmN2xDvnp8z8iEP5HMijURLwFjmlspyujHwxBL-lwCqXUU6MmSUCkz4bTXrloRmsj9O2zByfYhcgbvcA6Jag69USaGYbruVGVSZJbiPV-2RLilwaKhamWz10qG4L2n0S-jJHUbUzCCaie3bIOjUhFwZCoDE6bhqqqJJP7WgKJz-dFGMUYRv7OI2mk3VQ2_tCOjixQ2hndJDM0qNDg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/43530d8c1f.mp4?token=MHEcUmOHZy5qZJHshAL1WCUrShmopCmfyZBvNEKgJ0m4Qk9futuin7Un2qEF200C46RTMRakp5VywjcriG3PaA7089tDff98dnCWsc21UFQ2vQt5LG769gjYuoNxmfrtq-PJLTmN2xDvnp8z8iEP5HMijURLwFjmlspyujHwxBL-lwCqXUU6MmSUCkz4bTXrloRmsj9O2zByfYhcgbvcA6Jag69USaGYbruVGVSZJbiPV-2RLilwaKhamWz10qG4L2n0S-jJHUbUzCCaie3bIOjUhFwZCoDE6bhqqqJJP7WgKJz-dFGMUYRv7OI2mk3VQ2_tCOjixQ2hndJDM0qNDg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
فعال شدن پدافند اردن
@News_Hut</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/news_hut/68141" target="_blank">📅 02:35 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68140">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/453748b7ef.mp4?token=RvyEdQ-viOmEBmE411gLjTNlzB9g0adYmmFP8RNuno7t2LUMv9boixiHHYnyuYAVOUd09IhvhewaA0iPXnF3I3TLlOPr5-xq-08h4P3vLDoXOd3AbA3VqM2KneK4gQuN5iRjRT_Ae3VSB6Lz23Vw92rAFowkvMkxOBhxArhlCkOGwt4uO1bTMcZ-I-MymZEmg7FI6oj1r1VIw60dBFYNKzFzAdpVIu0yf-4F9TgrGOaag_b5VHf2zsimJ-tnrIgjkqc8uUcMJMaHlS2MyyCwHSBOoaybS9vxWMvghP3kaa-IoiepyjFtWhtg2CYaU3-9K5LjXQQlsm1kFXKrri_vAQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/453748b7ef.mp4?token=RvyEdQ-viOmEBmE411gLjTNlzB9g0adYmmFP8RNuno7t2LUMv9boixiHHYnyuYAVOUd09IhvhewaA0iPXnF3I3TLlOPr5-xq-08h4P3vLDoXOd3AbA3VqM2KneK4gQuN5iRjRT_Ae3VSB6Lz23Vw92rAFowkvMkxOBhxArhlCkOGwt4uO1bTMcZ-I-MymZEmg7FI6oj1r1VIw60dBFYNKzFzAdpVIu0yf-4F9TgrGOaag_b5VHf2zsimJ-tnrIgjkqc8uUcMJMaHlS2MyyCwHSBOoaybS9vxWMvghP3kaa-IoiepyjFtWhtg2CYaU3-9K5LjXQQlsm1kFXKrri_vAQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
ویدیو ای دیگر از شلیک موشک‌های سپاه به سمت پایگاه های آمریکایی در منطقه
@News_Hut</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/news_hut/68140" target="_blank">📅 02:23 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68139">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1073ff30f0.mp4?token=K-TA_GNmNleThsKfK98GuHkRudOWdNcT0vQ_Qx4r174RSG82-4ewfEDoqgRzlnKiG_YAk5LfO8dLaMpDpEdqjTiP3V9QI-aXKkwry7Ny4-JgsrqG78grrWoajF9UKzsSnV8gW2zHgLcZekS48i-LySP0WmQ7qGfUgo-mC8UJVeJ3MfBPyKp8SHIN-zs1GuONTah-Ff5lc580qcCsu5-mm15ETJZVYEA5mHfnHBmEuuYxMgsurcwSZol68AVqqqqzFk3WLz5hbS8i-wqvapN_XSbBFCk872zWczacjbKBLrQ8y0KWIEpVkqTRxJy5CNKzY21N7gyiVp75K8gB5ykBBg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1073ff30f0.mp4?token=K-TA_GNmNleThsKfK98GuHkRudOWdNcT0vQ_Qx4r174RSG82-4ewfEDoqgRzlnKiG_YAk5LfO8dLaMpDpEdqjTiP3V9QI-aXKkwry7Ny4-JgsrqG78grrWoajF9UKzsSnV8gW2zHgLcZekS48i-LySP0WmQ7qGfUgo-mC8UJVeJ3MfBPyKp8SHIN-zs1GuONTah-Ff5lc580qcCsu5-mm15ETJZVYEA5mHfnHBmEuuYxMgsurcwSZol68AVqqqqzFk3WLz5hbS8i-wqvapN_XSbBFCk872zWczacjbKBLrQ8y0KWIEpVkqTRxJy5CNKzY21N7gyiVp75K8gB5ykBBg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
شلیک موشک از تبریز
@News_Hut</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/news_hut/68139" target="_blank">📅 02:19 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68138">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">🚨
🚨
💪
گزارش های اولیه از شلیک موشک از تبریز
@News_Hut</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/68138" target="_blank">📅 02:14 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68137">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/682a3eeafc.mp4?token=Ngb6_pG9gjvzAhDEi0Gq9zXL4nlT4mkXNutmNoQcZO_Iymlv--qwhZWjpd68zyuKxQ3AzUiyqT1Zey6JvjpPqITBQJzvpORMys0Rk9A3kXtfmJGZceRa8wxytk8Fkrl4uPXwc5_DQjIyWl9UX-P-2wwdhRYeSZlWB3whpKIjhSAHOCc16GaRzAR8v9sK7e0PanP9xrIxgbS1Y_i83u6D7j5AVPQijVFWSmZ792NeGE1IHuwLOYSvAFFrSy5GIMIDW8Npx00MomyJtwsuIrqtYM3uhUiAn8tYOrPQPWSY1HOPUI7jt7M1XZuZbMhm6ZWlx1iFGsju7MAU5-IknIx9vA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/682a3eeafc.mp4?token=Ngb6_pG9gjvzAhDEi0Gq9zXL4nlT4mkXNutmNoQcZO_Iymlv--qwhZWjpd68zyuKxQ3AzUiyqT1Zey6JvjpPqITBQJzvpORMys0Rk9A3kXtfmJGZceRa8wxytk8Fkrl4uPXwc5_DQjIyWl9UX-P-2wwdhRYeSZlWB3whpKIjhSAHOCc16GaRzAR8v9sK7e0PanP9xrIxgbS1Y_i83u6D7j5AVPQijVFWSmZ792NeGE1IHuwLOYSvAFFrSy5GIMIDW8Npx00MomyJtwsuIrqtYM3uhUiAn8tYOrPQPWSY1HOPUI7jt7M1XZuZbMhm6ZWlx1iFGsju7MAU5-IknIx9vA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
مجری:
آیا همچنان قصد دارید جزیره خارگ را تصرف کنید؟
⏺
ترامپ:
خب، نمی‌توانم چنین چیزی به شما بگویم، چون اگر بگویم حماقت است. اما کار جالبی می‌شد و کمی هم خبرساز می‌شد.
⏺
مجری:
آیا احتمال عملیات زمینی را رد می‌کنید؟
⏺
ترامپ:
می‌گویم نه؛ البته اگر شرایط اقتضا کند [رد نمی‌کنم]. گاهی اوقات به عملیات زمینی نیاز است، اما ما افراد دیگری را داریم که عملیات زمینی را برایمان انجام دهند.
@News_Hut</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/news_hut/68137" target="_blank">📅 02:09 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68136">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/25d7e536a1.mp4?token=YMhnyofurJnfbJrY-EIuWxeklkIxOIr4WlqgWc_X_82lE6z_KZDfdZ2p0m3gT-a11MUXbN1AWhoZw5ZE8iG2Fxww9z1Jf-LYyGo0lhwqgl10oqKuJKGNxWk5hQio64SaBoc1YsOfQLYnN_w0mC8ALdZzIzQjrDQbLoWdas5_TilzZ2HNERA-C_ofVGkuGBi8jirJ4wwC7fdfGIkBhDcql5nOZi_cicMYIvYnpzaIGx5zVNOTwfG7Mo-8UBHi7v202QxLmenpc2ZzVQlr35gVG488DCjTTw79ILAPFXgyQjgsdYg2jQITxrPkfTl-7P2-vsweDLnRgBFlbHBDoI828Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/25d7e536a1.mp4?token=YMhnyofurJnfbJrY-EIuWxeklkIxOIr4WlqgWc_X_82lE6z_KZDfdZ2p0m3gT-a11MUXbN1AWhoZw5ZE8iG2Fxww9z1Jf-LYyGo0lhwqgl10oqKuJKGNxWk5hQio64SaBoc1YsOfQLYnN_w0mC8ALdZzIzQjrDQbLoWdas5_TilzZ2HNERA-C_ofVGkuGBi8jirJ4wwC7fdfGIkBhDcql5nOZi_cicMYIvYnpzaIGx5zVNOTwfG7Mo-8UBHi7v202QxLmenpc2ZzVQlr35gVG488DCjTTw79ILAPFXgyQjgsdYg2jQITxrPkfTl-7P2-vsweDLnRgBFlbHBDoI828Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
پرزیدنت ترامپ:
ما در حال رصد «کوه پیک‌اکس» هستیم، چرا که گزارش‌هایی مبنی بر وجود اندکی فعالیت در آنجا دریافت کرده‌ایم. ما دوربین‌هایی در اختیار داریم که قادرند نام و نشان شناسایی افراد را حتی از فضا تشخیص دهند؛ این دوربین‌ها تمام بخش‌های «پیک‌اکس» را پوشش می‌دهند. اگر آن‌ها کوچک‌ترین حرکتی انجام دهند، ما بی‌درنگ وارد عمل شده و هر اقدامی که لازم باشد را انجام خواهیم داد.
@News_Hut</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/news_hut/68136" target="_blank">📅 02:05 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68135">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b3f1669520.mp4?token=ASZg6F4SCn0zdxOPZx69lWBKjC1JDUdMRo7DOORY8vFJxzvR4iwpVgPyofRiAFZ5Mz0-Tz_8hQt50VYBFHFH94xOmmSfBLlxy37T0KPtSTrP0T-hhruFjikBYdBhYP0Ng8iCupM_ByrcL39OnAhYxUjCkHR9KFOBzlImG0LGezp9T7bfsrW2VDRT8E6mP6EF0oncUHkOf9UCZYQ51RYHPAPxtaTBnhv0j3g0wDhxo0u5fuEX7Y15GJ9WW3bQIp7sA7yG-ah-I6Vu4WCdtqDy3G-zAAcenBvnaRhR5df68KbvJlAnQMZ8YN4iK-IQuQHR7-oHpSy0B-XNJhHlDi9rvA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b3f1669520.mp4?token=ASZg6F4SCn0zdxOPZx69lWBKjC1JDUdMRo7DOORY8vFJxzvR4iwpVgPyofRiAFZ5Mz0-Tz_8hQt50VYBFHFH94xOmmSfBLlxy37T0KPtSTrP0T-hhruFjikBYdBhYP0Ng8iCupM_ByrcL39OnAhYxUjCkHR9KFOBzlImG0LGezp9T7bfsrW2VDRT8E6mP6EF0oncUHkOf9UCZYQ51RYHPAPxtaTBnhv0j3g0wDhxo0u5fuEX7Y15GJ9WW3bQIp7sA7yG-ah-I6Vu4WCdtqDy3G-zAAcenBvnaRhR5df68KbvJlAnQMZ8YN4iK-IQuQHR7-oHpSy0B-XNJhHlDi9rvA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
مجری:
«۱۰ فروند کشتی روز دوشنبه از تنگهٔ هرمز عبور کردند — کمتر از ۱۰ درصد چیزی که معمولاً از این آبراههٔ حیاتی عبور می‌کند. وقتی می‌گویید «تنگه باز است»، منظورتان چیست؟»
⏺
ترامپ:
«اگر مردم بخواهند از آن عبور کنند، باز است. ما آن را برای ایران باز نمی‌کنیم… الان باز است.»
@News_Hut</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/68135" target="_blank">📅 02:01 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68134">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
مجری فاکس : آیا انجام یک عملیات زمینی محدود را منتفی می‌دانید؟
ترامپ : «نه. گاهی اوقات به عملیات زمینی نیاز است.»
@News_Hut</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/68134" target="_blank">📅 01:59 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68133">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bbabff277a.mp4?token=FtV04H_9jMa2MUqSIRadtfKHWj5krKT7UeFZpx9h-jkLkFHHxxmg6jf5BaOz0lYVMgWTpWiqGZxh2aPupxFD0g3o1E1-zcOPohXDkXt_C8ZMBp-1CtwsvRZGDarHkK7HlQsUEFkrLqXjqjGi-0835v4BzFMhx_QWGxy3yq-VIcgd5almPFGG_FIp5TVnrGRzrwsTeEuMV9NOLv5yhXDWVvoxwoo41loIBf3bfKcCU1jL3M10hz6ev25BCLA3iSZIMLBndVbrMmUYgla9ZJRKreVqSaUJ1YoEWDWGD87iytWg6WWhPArl84_y35VjsvmJnS7OWnzGpTl3oJjbIansag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bbabff277a.mp4?token=FtV04H_9jMa2MUqSIRadtfKHWj5krKT7UeFZpx9h-jkLkFHHxxmg6jf5BaOz0lYVMgWTpWiqGZxh2aPupxFD0g3o1E1-zcOPohXDkXt_C8ZMBp-1CtwsvRZGDarHkK7HlQsUEFkrLqXjqjGi-0835v4BzFMhx_QWGxy3yq-VIcgd5almPFGG_FIp5TVnrGRzrwsTeEuMV9NOLv5yhXDWVvoxwoo41loIBf3bfKcCU1jL3M10hz6ev25BCLA3iSZIMLBndVbrMmUYgla9ZJRKreVqSaUJ1YoEWDWGD87iytWg6WWhPArl84_y35VjsvmJnS7OWnzGpTl3oJjbIansag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
خبرنگار:
آیا اطلاعات خاصی وجود داشت که باعث شد تصمیم به آغاز این عملیات بگیرید؟
⏺
ترامپ:
ما می‌دانستیم که آن‌ها خواهان سلاح هسته‌ای هستند.
⏺
خبرنگار:
آن‌ها می‌گفتند که خواهان سلاح هسته‌ای نیستند.
🔴
ترامپ:
هر چه می‌گویند دروغ است. آن‌ها دروغ می‌گویند.
@News_Hut</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/news_hut/68133" target="_blank">📅 01:56 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68132">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5d1f31387d.mp4?token=WiFLdhG9-AlnYi_qrfNfHbT1BfSZaIAA59sMiL4o8tGDo_PRxDiOs49hGs26alxATDGnSOmZYsQSFSaQQ4xZamRcYK9UxnrLl8kQy8UKUsG50MZzOBP_PbMsxO9iSNPk5HO9-u-lpQRrsf8et9PVsigtKU4sxtDJ7pZiIIClD-9GF0cpPraN19wP6SWjOGCrC77SIknoSjaTriPq1RrwgOQVUObjF6yETIM0oCCq9US0C6mvkUC7_9YU2cd5UEJ0rNEVY4duugAI6JpU0kr11l7gMVBfJsg4ryd-EqtCukwLVzkDdqvXZPtXihCKlodUDNERBys9WUYVMjzThxmmHg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5d1f31387d.mp4?token=WiFLdhG9-AlnYi_qrfNfHbT1BfSZaIAA59sMiL4o8tGDo_PRxDiOs49hGs26alxATDGnSOmZYsQSFSaQQ4xZamRcYK9UxnrLl8kQy8UKUsG50MZzOBP_PbMsxO9iSNPk5HO9-u-lpQRrsf8et9PVsigtKU4sxtDJ7pZiIIClD-9GF0cpPraN19wP6SWjOGCrC77SIknoSjaTriPq1RrwgOQVUObjF6yETIM0oCCq9US0C6mvkUC7_9YU2cd5UEJ0rNEVY4duugAI6JpU0kr11l7gMVBfJsg4ryd-EqtCukwLVzkDdqvXZPtXihCKlodUDNERBys9WUYVMjzThxmmHg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
پرزیدنت ترامپ:
«همان‌طور که می‌دانید، ما پیش‌تر دو بار به جزیره خارگ حمله کرده‌ایم... اما در مورد تصرف آن، اگر بتوانیم توان آن‌ها را به اندازه‌ای کافی و عمیق تضعیف کنیم، این کار را انجام خواهم داد.»
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/68132" target="_blank">📅 01:52 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68131">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🚨
🚨
🇺🇸
پرزیدنت ترامپ:
حملات به ایران ادامه خواهند داشت تا زمانی که من بگویم کافیست.
@News_Hut</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/68131" target="_blank">📅 01:51 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68130">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f264ca5d25.mp4?token=JVm1ndEmT6DbB_Hc0hieeqG3EMzQOm3w5-4BfXwIOot4TP9OPCq6_iP6EqntVkXu9iSuKMbx6C3T-yFQgQLCv89E-DkdyD_hBHmosC7Tebvjqh9O-c6kpYKndT1dDg7dM_B98mXzKm2cvJqQM_pwzZNomeZtVQqLaX3Ubgb-2CYDuhPzdahSNxb4CQCTfstDypQLQfdAa5KN0QBbgFCtvAF6Isz4wDogXotRaqSGkGwgfY-UlBHT3oqqot5bhNCA8rItijl1wrrCwpJ5Ci6Nxvomq-UzIQ87mgz52qMwlPFCnxTCcufz8L6y2xGwC9J5mtIIB2TigvAiUWoXbPBRRg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f264ca5d25.mp4?token=JVm1ndEmT6DbB_Hc0hieeqG3EMzQOm3w5-4BfXwIOot4TP9OPCq6_iP6EqntVkXu9iSuKMbx6C3T-yFQgQLCv89E-DkdyD_hBHmosC7Tebvjqh9O-c6kpYKndT1dDg7dM_B98mXzKm2cvJqQM_pwzZNomeZtVQqLaX3Ubgb-2CYDuhPzdahSNxb4CQCTfstDypQLQfdAa5KN0QBbgFCtvAF6Isz4wDogXotRaqSGkGwgfY-UlBHT3oqqot5bhNCA8rItijl1wrrCwpJ5Ci6Nxvomq-UzIQ87mgz52qMwlPFCnxTCcufz8L6y2xGwC9J5mtIIB2TigvAiUWoXbPBRRg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
پرزیدنت ترامپ:
«در نهایت، اهداف حوزه انرژی در ایران را هدف قرار خواهیم داد. نوبت به پل‌ها می‌رسد؛ هفته آینده سراغ آن‌ها می‌رویم. ما تمام نیروگاه‌هایشان را از کار خواهیم انداخت. تمام پل‌هایشان را نابود خواهیم کرد، مگر اینکه پای میز مذاکره بیایند.»
@News_Hut</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/68130" target="_blank">📅 01:49 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68129">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/36032be115.mp4?token=G2CDS4eDzAiihvfvc0qWeqAMqApwlxohTWGGoYlCZMt7iIMS6bljFa3PaWR0v6N3FqVslYy9hh2g7cWOvHmRYkaoZp1GQoZjM6hQA1YHA44IVeiaNE5NIazh5gDQMaT-UNhd7q1MREcYT1VXYgklPQ0TRghHc_uBzUF5wWw9P6Ss405KAgVL4jBTMIOE0bFgsqfIVQQqNF7aNTv87wJW72XZ4fows_3inQqbdx-dHPBWRdWiewsIKYkNxUKJG-ACBOUupd7EWSaet-COnENR2nf0zZHvxFbBTOq2HdXYaOYNUxxIgpbSrKj52ldBhtK3MG6YOy8DyFU_l2t87UTZKQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/36032be115.mp4?token=G2CDS4eDzAiihvfvc0qWeqAMqApwlxohTWGGoYlCZMt7iIMS6bljFa3PaWR0v6N3FqVslYy9hh2g7cWOvHmRYkaoZp1GQoZjM6hQA1YHA44IVeiaNE5NIazh5gDQMaT-UNhd7q1MREcYT1VXYgklPQ0TRghHc_uBzUF5wWw9P6Ss405KAgVL4jBTMIOE0bFgsqfIVQQqNF7aNTv87wJW72XZ4fows_3inQqbdx-dHPBWRdWiewsIKYkNxUKJG-ACBOUupd7EWSaet-COnENR2nf0zZHvxFbBTOq2HdXYaOYNUxxIgpbSrKj52ldBhtK3MG6YOy8DyFU_l2t87UTZKQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
خبرنگار:
آیا جنگ با ایران از سر گرفته شده است؟
⏺
ترامپ:
خب، گمان می‌کنم بتوانید هر طور که می‌خواهید آن را تعریف کنید، اما قطعاً ما داریم ضربات بسیار سختی به آن‌ها وارد می‌کنیم. آن‌ها باید ضربه بخورند.
@News_Hut</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/68129" target="_blank">📅 01:48 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68128">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c4323d3fd2.mp4?token=artgeZk-mkchU2UeADRqLO3QU-R-keCi6UZiDwTmo4Yn0CUVk1sv-WCJbJXKdB8Wu6bmspVtvcj63jOltS52dWsUxh8wbqQcpJq6gXTcKlD9xZ0LU1vq_-dGZ1PLgAtD8wdbP2qNedsNqCpcZi9izwCT-_0YOVKyv2ZAFY9c_T_VbWCZHaeQ9rZzSDAxxd8olRC_64O8YxCF2hH5atXItMwAkcGh3Fni33tnGxhjT3IdwWpNgTViqXDDfLZqWm_RkuYoGaZQlQGFOuxESXvipSxweRWKlyyTj-ke4Ob9LG9VW9AvdfPdxQaW1py-sTsh2azF2ABBxEX8g89a9AvNBA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c4323d3fd2.mp4?token=artgeZk-mkchU2UeADRqLO3QU-R-keCi6UZiDwTmo4Yn0CUVk1sv-WCJbJXKdB8Wu6bmspVtvcj63jOltS52dWsUxh8wbqQcpJq6gXTcKlD9xZ0LU1vq_-dGZ1PLgAtD8wdbP2qNedsNqCpcZi9izwCT-_0YOVKyv2ZAFY9c_T_VbWCZHaeQ9rZzSDAxxd8olRC_64O8YxCF2hH5atXItMwAkcGh3Fni33tnGxhjT3IdwWpNgTViqXDDfLZqWm_RkuYoGaZQlQGFOuxESXvipSxweRWKlyyTj-ke4Ob9LG9VW9AvdfPdxQaW1py-sTsh2azF2ABBxEX8g89a9AvNBA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇷
‏ارتش جمهوری اسلامی:
در مرحله هفتم عملیات «صاعقه» محل استقرار جنگنده‌های اف ۱۸ و سایت نگهداری تجهیزات ارتش آمریکا در پایگاه الازرق اردن را هدف حملات قرار دادیم.
@News_Hut</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/68128" target="_blank">📅 01:21 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68127">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">🚨
حمله به جزیره هنگام
@News_Hut</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/news_hut/68127" target="_blank">📅 01:02 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68126">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🚨
بندرعباس و سیریک بوووم
@News_Hut</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/news_hut/68126" target="_blank">📅 01:02 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68125">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dddea8a9d1.mp4?token=n1yzz-BMvpzlLCvPn6tkDFa5dohomA15ouvT4oOVUD5Non19YpvXjjmRCs43SzkYAj_LKAyestGT9Y2-NBy87TCvcdZ2YqN8YZTB5Fb1er__3yDihA_tIg7GLeuLjREZkGumUD6DqcBosxa_ISyeV7Js-itTAZOSwQWPBCoHT4mddC5BvxpXF8mVWZHeCDIUQoGXHJxeLKBLhg3A7KDluq-Blq6bhUc1crbvc8457xgSVWzDU97x0AgyXN7rkT7kKovhBWd7DIJi18V-HPFnFiTpN-I0QjIRRxchs_a6WhFYUn0U1xyAk6VOv1USbjLcBo9sTS9HL-EygP0HOT5d8A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dddea8a9d1.mp4?token=n1yzz-BMvpzlLCvPn6tkDFa5dohomA15ouvT4oOVUD5Non19YpvXjjmRCs43SzkYAj_LKAyestGT9Y2-NBy87TCvcdZ2YqN8YZTB5Fb1er__3yDihA_tIg7GLeuLjREZkGumUD6DqcBosxa_ISyeV7Js-itTAZOSwQWPBCoHT4mddC5BvxpXF8mVWZHeCDIUQoGXHJxeLKBLhg3A7KDluq-Blq6bhUc1crbvc8457xgSVWzDU97x0AgyXN7rkT7kKovhBWd7DIJi18V-HPFnFiTpN-I0QjIRRxchs_a6WhFYUn0U1xyAk6VOv1USbjLcBo9sTS9HL-EygP0HOT5d8A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
هم‌اکنون دارلین گراهام نوردون، خواهر لیندسی گراهام، در حال ادای سوگند برای گرفتن جای برادرش به عنوان سناتور کارولینای جنوبی است.
@News_Hut</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/news_hut/68125" target="_blank">📅 00:53 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68124">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🏆
اسپانیا با پیروزی در برابر فرانسه راهی فینال جام‌جهانی 2026شد.  @News_Hut</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/news_hut/68124" target="_blank">📅 00:49 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68123">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">🚨
انفجار چابهار
@News_Hut</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/news_hut/68123" target="_blank">📅 00:47 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68122">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Za4WkbDTNyIQHy2-Tk7q6h1DGGW2mXr8isyjJP4buSBhEgrYys-vHnc7S56Gu97fhUJCKd82YCa9FdYTUEVAYKk2fKF55nuxF1MIt5WUfmTXwOR6nstzJ-5fxc7sC-jtCYq-aywFHH-aM8u61M-55nGCTPwEs1BZatdLh90JbQnyf77YryFLMcV4VS0JTZ2amvhQRUTN1H5JZlJio1p9glm0M-TE77mgERmSEXFUrgNMq4KIwU81gbTljJHqNY_GuD0XcSW4u04aivgB-0-KagwIqGsjNAFdiwy1hDmYRDy8xlYAHUhXw71USAeM8gQUH3X-qqh3ADCUTWv8pLHo6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
اسپانیا با پیروزی در برابر فرانسه راهی فینال جام‌جهانی 2026شد.
@News_Hut</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/news_hut/68122" target="_blank">📅 00:41 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68121">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/08a5f1d44f.mp4?token=ElZFpppPRqG-LyLEVsGwKeaKv8l1wMnIsWbSh7TyCrWv4IEgyGi3nomIEwgo90z0cxYD_w8WqAWMrFQNu7nMOfT3QB_naqZ6bzH9lqdLJilFilLB4vcmS06BLofpsz8PGvt83p2IrX2ZlovWh5pIjEcG2pkBpplH4YH1UwlMPBHcpY82hOu3FNGxpYM4ynNUDxmdTMhu0TrP5LZZDtbMEUssmkxkHgOxNGJ3WuHfANTMfsMYZxZZE3bGF2XJcf9SwF3KJgGepTR6uharNVAiVw3Jibg4qQ_L0JddMvbu-Jx1WOMIVxru1SV84HomrILZ6g63E3IMsHUqR6psGjMHjA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/08a5f1d44f.mp4?token=ElZFpppPRqG-LyLEVsGwKeaKv8l1wMnIsWbSh7TyCrWv4IEgyGi3nomIEwgo90z0cxYD_w8WqAWMrFQNu7nMOfT3QB_naqZ6bzH9lqdLJilFilLB4vcmS06BLofpsz8PGvt83p2IrX2ZlovWh5pIjEcG2pkBpplH4YH1UwlMPBHcpY82hOu3FNGxpYM4ynNUDxmdTMhu0TrP5LZZDtbMEUssmkxkHgOxNGJ3WuHfANTMfsMYZxZZE3bGF2XJcf9SwF3KJgGepTR6uharNVAiVw3Jibg4qQ_L0JddMvbu-Jx1WOMIVxru1SV84HomrILZ6g63E3IMsHUqR6psGjMHjA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ایران تنها جاییه که بتمن هم به گا میره
😂
@News_Hut</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/news_hut/68121" target="_blank">📅 00:34 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68120">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/urGk3OFdOLLGDV0GMOPvpkXqtVQM0evwgEHrCB2_d8On4aKQ7gIEBA2Zd4nw88qlN8EBeyTuY5AnkHyYv3st0i-L52ZHf79fz8rxLrUvhfSK-5cOMTQvW5nW9q7uS6t5iUdNVtsoGalVJeS15_u2p1M8QaWQWsqBdIGfimbOK-Id7VT1uApLi1zlA_dDgSnE6xw_l6jDw0Bi9X2EIwUJwl4nbftRBflh8OU4YRE0czw_jYYrOLWFmafj-zLWHtiZeAxW7AhUTzDmQmdLMCz-8woOvoUaY8KMRZsZgQ6wHCZeps3_2R1aQw9metQYxGRRdqjjSZQVUsBhtR4IxNc1VQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
فرماندهی مرکزی ایالات متحده:
نیروهای ایالات متحده امروز ساعت ۱۶:۰۰ به وقت شرقی، محاصره دریایی شناورهایی را که به مقصد بنادر و مناطق ساحلی ایران و یا از مبدأ آن‌ها در تردد بودند، از سر گرفتند. در حال حاضر، بیش از ۲۰ فروند ناو جنگی نیروی دریایی ایالات متحده و صدها فروند هواپیمای نظامی در سراسر خاورمیانه مشغول فعالیت هستند. نیروهای آمریکایی همچنان هوشیار، دارای توان رزمی مرگبار و آماده‌به‌کار هستند.
@News_Hut</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/news_hut/68120" target="_blank">📅 23:54 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68119">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🇪🇸
گل دوم اسپانیا به فرانسه توسط پدرو پورو</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/news_hut/68119" target="_blank">📅 23:52 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68118">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c993da0a01.mp4?token=B8sCXvGzwU3EAMCsfc9wj4cCkMqntXjDjmWpmAqP8Z9Cu6xvgJOwyyhYY4Z590B8ZxXMWKZEbHCF-lqkK5HGek9qHitLQzKqFYqCjwdyrdpkGrNfCvZDm3eDJxbjIFKI4at-fR1BiNV9tK1SS1s2aj5_wgs6XmsL02rqOHNZ2f6UOdsz0qf4DSNHcTAWGFsbcIb5x_7ue6pHYqnFrwR4oR_37UP0BnvkTLj468SIznOqn3Iy7kxWdrDI3auirZ0FUp5iICI_WJk8haK5_ChSiCJ9Ltbevqjsd3OJtrVfhHRowzZCiGPZli43ySAAe8QeSRtoTm1mamvXV_FPKmW1WQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c993da0a01.mp4?token=B8sCXvGzwU3EAMCsfc9wj4cCkMqntXjDjmWpmAqP8Z9Cu6xvgJOwyyhYY4Z590B8ZxXMWKZEbHCF-lqkK5HGek9qHitLQzKqFYqCjwdyrdpkGrNfCvZDm3eDJxbjIFKI4at-fR1BiNV9tK1SS1s2aj5_wgs6XmsL02rqOHNZ2f6UOdsz0qf4DSNHcTAWGFsbcIb5x_7ue6pHYqnFrwR4oR_37UP0BnvkTLj468SIznOqn3Iy7kxWdrDI3auirZ0FUp5iICI_WJk8haK5_ChSiCJ9Ltbevqjsd3OJtrVfhHRowzZCiGPZli43ySAAe8QeSRtoTm1mamvXV_FPKmW1WQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
🇮🇷
علی خامنه‌ای، (19 دی 1404):
ترامپ که با نخوت و غرور نشسته آنجا راجع به همه‌ی دنیا قضاوت میکند بداند که مستبدین و مستکبران عالم، از قبیل فرعون و نمرود وقتی که در اوج غرور بودند سرنگون شدند، این هم سرنگون خواهد شد.
⏺
🇺🇸
دونالد ترامپ، (10 اسفند 1404):
آیت‌الله خامنه‌ای ایز دد.
@News_Hut</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/news_hut/68118" target="_blank">📅 23:52 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68117">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🚨
🚨
⭕️
محاصره دریایی علیه ایران آغاز شد
@News_Hut</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/68117" target="_blank">📅 23:32 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68114">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/d9HmYOpG-deIkXy2VmOreNpAr5G2J6KzYfiIm-spnDKXbR9J-hzCqLzlswnj1yG2Ywjieh69h-JUOsvDMHZPlu4SGVKCbZtNUQvGyVG66A4705tXO_dPX3T3Bn40Hy6sOQqBJF1cdeXB8C2pxnnGi6ZO_LjYfApKTEwrSPSrC1hWk067webwRS-xnO2PhEyP8F0Lun5benRjddOVS1SfcevVjlrxyfhna_976Pnf2LViHKQQXksY0mPzdSMhEX3m3PiLFTEEeLgyMAnnaR99SGvwQPj00bwrAxLRKagpO8nkQD2NCRQm_50axYempvyBe3qKZALAWSEjhQs2GM8N3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/R_fT_L2GpyKUOG0culCjUQ7sweJkzQAdVNHQZpmPcRvqsniuWiLfZ5yqjMIcy8iCVkzbU3mbpP8VLZNi-YYsM50XjbaU2OIDDQv58jPKyRSqqkUwGsTbvnOhNL2gwblzIfdmy-iJmuGrLRPzD9QkaKnHW_vz8BBeTHKMWz1-BTAzpCYOkn9UCORa8AKZGOagx5xhZVkviMzJQLFh93poY1vsbh7A2g-ZQ9l29rWzBQANAUiMdN55MQ2xc60RzVg4xRxiMOd-U4NbcDlMgeiGSlytBm5Z65IP6O_Uao_m7EnH-hszQrMC-LBo7wYhUUCnyw2WA4Q8zvbghYr3nZB-cA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">تازه می‌خواستیم نودای نیلی افشارم بزاریم، پس هر وقت بابای مانی لفت داد می‌ذاریم #hjAly‌</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/news_hut/68114" target="_blank">📅 23:26 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68113">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">🚨
🚨
🚨
سیریک بیش از ده انفجار
@News_Hut</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/news_hut/68113" target="_blank">📅 23:25 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68112">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🚨
🚨
🚨
🚨
انفجارهای جدید در خوزستان
@News_Hut</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/news_hut/68112" target="_blank">📅 23:13 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68111">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🚨
‼️
تصاویر جدید سپاه از حملات موشکی‌ش
@News_Hut</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/news_hut/68111" target="_blank">📅 23:05 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68110">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">ماشالاااا اسپانیاااا، اینا بیان فینال مسی راحت تر قهرمان می‌شه
#hjAly‌</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/news_hut/68110" target="_blank">📅 22:53 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68109">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🚨
🚨
سه انفجار شدید در بندرعباس
@News_Hut</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/news_hut/68109" target="_blank">📅 22:48 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68108">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🚨
🚨
🚨
چندین انفجار سنگین در اهواز
@News_Hut</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/news_hut/68108" target="_blank">📅 22:45 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68107">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">بابا نکن من چنلت رو دادم بابام
😂</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/news_hut/68107" target="_blank">📅 22:10 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68106">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMani</strong></div>
<div class="tg-text">بابا نکن من چنلت رو دادم بابام
😂</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/news_hut/68106" target="_blank">📅 22:10 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68104">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from⁪⁬⁮⁮⁮⁮⁪⁬⁮⁮⁮⁪⁬⁮⁮ᴹᴬᶻᵞᴬᴿ</strong></div>
<div class="tg-text">مرسی که تک خور نبودی
💙</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/news_hut/68104" target="_blank">📅 22:07 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68103">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MihiREt4yA-oxUdsKhFBAf3zwtYeBnURGBxyzutK0r8y14PO609wNNQnm8_6Ywk-xrtxognBv8rg2wagw_aJcW0gQKN5OVoeRwtGV1KuZ_l3gNlGG-H00aynK0ok5AWhD3jKjZ9oZept8wLs-KoESTLDhi4TJl5y1jmCg19FXCtCrhLj38TI1CgqhVKyQdB1cE6vpVL7_vjXUoO23rl9Ao5JuW8FE8isy_ytqzMkVdoIxhnD1XftB_Nll0IGcOgB_R9sQDU4cR04h5PAVupcIT4Kt7XuNNrNAl8zumjbWfjgRBPO2hhQQ_s4hq4gsSPqvJp-8xlAmu45TUYQ3aDHlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امروز، روز جهانی نود فرستادنه
🙂
#hjAly‌</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/news_hut/68103" target="_blank">📅 22:05 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68102">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">⏺
رسانه‌های حکومتی:
دقایقی قبل نقطه‌ای در جزیره قشم مورد اصابت پرتابه‌های دشمن آمریکایی قرار گرفت که گزارش تکمیلی پس از ارزیابی‌های اولیه اعلام خواهد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/news_hut/68102" target="_blank">📅 21:56 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68100">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/W4KgbAyXGWj1TwTglt8qhgE495GgzXluyEWTQnHOKKeoakLCGRsEqbmnhNJW3zclHqb7GVeZpaeSMUEFL_Vz-N0WIX80uGIy7lCHII9ftVxt-fnX_pOI3oWo-7ofSyeZQowhdhrGb6TzBsBVrlBY09K_BvNoxEF7SVjAIWniZmHOBndCe_fbsFKCHRw1XDFhGzoe-AgI-H1RZWysZQqOYuLt8agG6uH_FnbsxiuSg6OSvQnlryK3i9rk34EIi8njHIpopfBktGIM1389HP8C1mbQSsNy7O6UV7V2vCa_EuX1dE7zSbuLgZhLtkNsI8xXPtlo2yCC3TmCsrzpzARAgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/u7Nuq6YEddw2EVXVVUUuwQrwfIr8jsqGuRDy12bCDKqhiJyIo4w3RcTcjzqkbXNVTpDak6YYKjAHjxnlacN0re-yebzLecUhwditSBgmhypHhB-gPHO4Im3TwMtjuGniZNaQCpn89UCGGc1-_0uNRzNGJbtKJA6LaRzkVli75d2uk4PhL_0yqySxXhGQBkMU_2A46XNk6L63tmJSei92eRYJSheOBtFHK-onAQrHeZUcz2Tk4TK4LLMaTpIFlXf9HLfxdPMUPbyCagLWwlpdBhIVoxeTXwunlof4lTWHan6h66dtN76fuvuab7gtPaqXcbtDBPSmJqukCQtiKnm28w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏆
نیمه نهایی جام جهانی؛ شماتیک ترکیب دو تیم ملی اسپانیا
🆚
فرانسه؛ ساعت 22:30
@News_Hut</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/news_hut/68100" target="_blank">📅 21:54 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68099">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aAtvE36ZE7rNUHpUgMH2Lw-z2oSr-5RgxE6Ai955YQC7JD-nNBwsbiEEpYdatcExlLA4LDjV2dR28_Wdz1SHVh4ncWK3co_mXy3ZV_FI6CJdqf35FmM15F6sfjAV9wmQBzSPIo7mxBFwObEZ4Zoaf1sdx1maOdXDqtMLH9ymI_GM3Vnh1F8evlfhC0pxETEBLgnoKgTBPZUo6WHrRl5ijGb1H1G-RuqSPbD6EnZNi_45-WcNNJhyfgdIUvDiJMPzZpT-zC7K3uNfDreIs4Hgrp2D4f__fIVHjSirU8Q8FBiFd-itmxraAQYg8R6t_MS9yDE_zkeGWIhxHSbezc001w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
پزشکیان:
‏در تاریخ، جنوب ایران همواره نماد مقاومت در برابر استعمار و پاسداری از استقلال بوده است. امروز نیز مردم نجیب این دیار با صبوری، ایستادگی و پایمردی، روزهای سخت ناشی از تجاوز دشمن را با عزت پشت سر می‌گذارند. در کنار و قدردان این مردم وفادار و مقاوم هستم.
همه جای ایران، سرای من است.
@News_Hut</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/68099" target="_blank">📅 21:41 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68098">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from𝗔𝗱𝗺𝗶𝗻 VPN</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OApWs2PTDpMFr78e9_tOZdEALHKWPUam7gszIxQtlyyuo27jygW_oqHSj1HQI5VjLdN_xCZ4QYxdgKemvQSZyvDfIqRF5cATyj__H2chbozIIJwXICRQ5Ov1Nt5fze3lVbHK-GXvO2LwIreDpFH526Lnjb68iQUDcClOtcDm-rMSXyLkFPqcKU_tU6WtZnHYnXdzycklDt80qa0uym0fckVa6T3SKVsC6vgDOs9uMFgU_IBBMO8BJBDh56vGdzIAc-TDdUSpsggZrCQYKyGheWR7QYN0YtDlUSEVIXN1BzLiwppXyif3OzHkfHkiKrSVkSwm7ZYGD7hrzWKjuRiieg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🆓
رفقا
توجه توجه
✅
درآمد تضمینی روزانه 35 میلیون در منزل
🌟
تمامی ضرر هایی که این چند وقت بخاطر جنگ دادی  رو جبران کن
✔️
🚨
⚡
⚡
⚡
⚡
⚡
⚡
https://t.me/+ArmBt6ZWMF84ZDlk
https://t.me/+ArmBt6ZWMF84ZDlk</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/68098" target="_blank">📅 21:41 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68097">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d22e49214c.mp4?token=dzRPVHAO0TAfnfb-VuVCX5IsFsiGYBeHU1rDqL4KKj0W3UduAzqrjF6BExvnaDH-RmCv4BUU_QxQ0jFyYBd0wOZy79QMRyeF8Q5tzKfTr3t8dvdgfmcfYPf6CKRNe1SnE41DI5wzCe8oslRZreG94sZZPQ0OaivTBO7K89Dly2dLx98QQEfkkbvuV6nFCFV3ouS1sTUEcEXhuqNfVU-fuGzQiKpFwJKgc08dz1kb9JG__Zu0KF4WbwCmY2g3TNvgXpxiLeGTUpvE_W207Xv4mRbYE4U7QhNj8SYZyCV9uzIxIaI4pz1rJlgcsPu-rxVOEXXKS6Rngc1tbNxV9OL66w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d22e49214c.mp4?token=dzRPVHAO0TAfnfb-VuVCX5IsFsiGYBeHU1rDqL4KKj0W3UduAzqrjF6BExvnaDH-RmCv4BUU_QxQ0jFyYBd0wOZy79QMRyeF8Q5tzKfTr3t8dvdgfmcfYPf6CKRNe1SnE41DI5wzCe8oslRZreG94sZZPQ0OaivTBO7K89Dly2dLx98QQEfkkbvuV6nFCFV3ouS1sTUEcEXhuqNfVU-fuGzQiKpFwJKgc08dz1kb9JG__Zu0KF4WbwCmY2g3TNvgXpxiLeGTUpvE_W207Xv4mRbYE4U7QhNj8SYZyCV9uzIxIaI4pz1rJlgcsPu-rxVOEXXKS6Rngc1tbNxV9OL66w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇷
👈
مهمات خوشه ای شلیک شده توسط سپاه در آسمان بحرین
@News_Hut</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/68097" target="_blank">📅 21:32 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68096">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">🚨
🇮🇷
دقایقی قبل سپاه پاسداران به بحرین و کویت حملات موشکی و پهبادی کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/news_hut/68096" target="_blank">📅 21:19 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68095">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">امروز، روز جهانی نود فرستادنه
🙂
#hjAly‌</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/news_hut/68095" target="_blank">📅 21:03 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68094">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0f9cda20a0.mp4?token=kCHLZ-9J3-2tF-qwNT0HPYAn3qA_F-1VJhvlj_0QGq-jrjajG99wgucUTztUO-uWAtSfrTJ0IS5EocGnfdG91vcSlXYSDEJ5AZ7vKMmXBdnrQTuVvk5WqSbXCxaxxLnr5m-KFIBjqFHnQIo3_5Hmm0idpodr7GpPLeEfJnO5fu3L7IivrE3Vb5bjt1ZhKI0N9GXFPr8hROd2AFbMkIi8X22ZVFgxYnVfvHF7nS1sfz_NR_f2Jr9RjxJ9LmiPIyelJTHp5ppDVH_bpzTgxd7jHj4rCEk54_ncYJp7-joYhwMj-Se-zMO5zdTK_c1wGOR8fzVe1wxVBMtEx1uUqSn6iQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0f9cda20a0.mp4?token=kCHLZ-9J3-2tF-qwNT0HPYAn3qA_F-1VJhvlj_0QGq-jrjajG99wgucUTztUO-uWAtSfrTJ0IS5EocGnfdG91vcSlXYSDEJ5AZ7vKMmXBdnrQTuVvk5WqSbXCxaxxLnr5m-KFIBjqFHnQIo3_5Hmm0idpodr7GpPLeEfJnO5fu3L7IivrE3Vb5bjt1ZhKI0N9GXFPr8hROd2AFbMkIi8X22ZVFgxYnVfvHF7nS1sfz_NR_f2Jr9RjxJ9LmiPIyelJTHp5ppDVH_bpzTgxd7jHj4rCEk54_ncYJp7-joYhwMj-Se-zMO5zdTK_c1wGOR8fzVe1wxVBMtEx1uUqSn6iQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
سر دادن شعار مرگ بر سازشگر در مصلی تهران
صداوسیما هم چندین بار صدا رو قطع کرد
🤣
﻿
@News_Hut</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/news_hut/68094" target="_blank">📅 20:32 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68093">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d01c7f855d.mp4?token=B8R065S5OjAeCeC3hfXPLNu-uZnEo1yWXVHVqUVfZIT7vzUkIJIMGBr8sw3KsnWAt2MwjwUUxS0_o56QwPjST8F6HqFy3M_fEmAjrTP7Z5uZtQgdG8c7pFwa06avGMB4eCyj89apiNC3aZ8bG9-qMHbbgiFzl60WdTElCA4qyuL4m-PnFRKPi2k1Wpn4FbQ9SUnyN5F3TAaPTZI_L0v-qa8keMTcYzyOmyztjLPfoupW4CrYejPPQozd7kluFWPJkGwdDJYxc--fLH1ISVzPvd3Cv6w2SolPK3am4EohMPz-UEDN3MlaLYphR9mR_WlJl62LrDOOVnjMrPlBo5qNmg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d01c7f855d.mp4?token=B8R065S5OjAeCeC3hfXPLNu-uZnEo1yWXVHVqUVfZIT7vzUkIJIMGBr8sw3KsnWAt2MwjwUUxS0_o56QwPjST8F6HqFy3M_fEmAjrTP7Z5uZtQgdG8c7pFwa06avGMB4eCyj89apiNC3aZ8bG9-qMHbbgiFzl60WdTElCA4qyuL4m-PnFRKPi2k1Wpn4FbQ9SUnyN5F3TAaPTZI_L0v-qa8keMTcYzyOmyztjLPfoupW4CrYejPPQozd7kluFWPJkGwdDJYxc--fLH1ISVzPvd3Cv6w2SolPK3am4EohMPz-UEDN3MlaLYphR9mR_WlJl62LrDOOVnjMrPlBo5qNmg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تعجب ترامپ درباره تحقیقات اف‌بی‌آی درباره مرگ لیندسی گراهام
⏺
خبرنگار:
«آیا می‌دانید چرا اف‌بی‌آی در حال بررسی مرگ سناتور گراهام است؟»
⏺
ترامپ:
«نمی‌دانم چرا، چون فکر می‌کنم او مشکلی داشته... من شرارت زیادی در آن نمی‌بینم. می‌دانم که انواع و اقسام تئوری‌های توطئه وجود دارد. فکر می‌کنم اف‌بی‌آی وقتش را تلف می‌کند.»
@News_Hut</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/news_hut/68093" target="_blank">📅 19:58 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68092">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1047876eb4.mp4?token=SsQO2925F0ikAHWKRcp1R0QDo9oRed3ujkL3hbMC0jl5rtI55cBPcrUwKIysIQHIOlzS2m_rkmZ-BhJCLtAh6VxwJJv--7oi-f844y3RLQ2Q0m785DcD_wvWM_X62rVM2VdtoYm5gQ9X8nOuhrdMWlpO4W4OOT4omJyCe67lwVcm9RP5FFeQdrGeUzM91hW7kYvmcYSSB5I1qE7imH0L7spBFT4zElpMUjYBddRvhq7uEdm0I5q1-Lx4PniTEh3GsOwhcAjm-AKWaOmsGpWVl_xyfj9mI2ruNCC1eANATBD67RtrrqFxgPFmVkTojt3AEvNtlO9c9RQRAee7IgtG7w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1047876eb4.mp4?token=SsQO2925F0ikAHWKRcp1R0QDo9oRed3ujkL3hbMC0jl5rtI55cBPcrUwKIysIQHIOlzS2m_rkmZ-BhJCLtAh6VxwJJv--7oi-f844y3RLQ2Q0m785DcD_wvWM_X62rVM2VdtoYm5gQ9X8nOuhrdMWlpO4W4OOT4omJyCe67lwVcm9RP5FFeQdrGeUzM91hW7kYvmcYSSB5I1qE7imH0L7spBFT4zElpMUjYBddRvhq7uEdm0I5q1-Lx4PniTEh3GsOwhcAjm-AKWaOmsGpWVl_xyfj9mI2ruNCC1eANATBD67RtrrqFxgPFmVkTojt3AEvNtlO9c9RQRAee7IgtG7w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
پرزیدنت
ترامپ درباره لغو عوارض گرفتن از تنگه هرمز
:
«آنها (کشورهای عربی)گفتند: "ما ترجیح می‌دهیم سرمایه‌گذاری کنیم تا عوارض پرداخت کنیم." و من این را دوست دارم چون هیچ‌کس نباید بتواند برای تنگه عوارض دریافت کند.
«در مقابل این سرمایه‌گذاری، کشورهای حوزه خلیج‌فارس مبلغ بسیار زیادی در آمریکا سرمایه‌گذاری خواهند کرد. این در واقع خیلی بهتر است!»
@News_Hut</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/news_hut/68092" target="_blank">📅 19:52 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68091">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🚨
🚨
شنیدن صدای انفجار در قشم
@News_Hut</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/news_hut/68091" target="_blank">📅 19:12 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68090">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LANa6l8vfJilw9y6lpq-MakJWspORY48AsSWbGuq6H5S7HkgySd92L-nafxv7ubbUyyOMULXKgYyjeZCDYBzSrPHkVhxbSRBVS2TFQtCDHkPql3k88OPlV-y5z3Ho2fMXPktq1ae-JERdlGwr_Vh1w0XCJt8fCYq4eOGu-Jjd4iQ7aewyxVkzGuUJzCJCR_dQe8Y42JRcxnQAaNaMAqw9RkJ_feVm7aaYXiWWX8Cf6soX2T7n9opFx79k4DPfeCIpdQSyDGfx3YHruSBrgnaUIt52qcDqHvufDAmNfawpBHAFnW0d9DunmkIzh6k8IeLCjED9n9qTXq6nHEme0uoMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
🇺🇸
پرزیدنت ترامپ در تروث سوشال:
به لطف قدرت فوق‌العاده ارتش ایالات متحده، نفت بیش از هر زمان دیگری در جریان است. درود ویژه می‌فرستم به وزیر دفاع، پیت هگسث؛ رئیس ستاد مشترک ارتش، دن کین؛ و فرمانده ستاد فرماندهی مرکزی ایالات متحده (سنتکام)، دریاسالار برد کوپر. به واسطه تلاش‌های آن‌ها و تمامی اعضای قدرتمندترین ارتش جهان — که بی‌رقیب است — تنگه هرمز برای تردد تمامی کشتی‌ها باز است، مگر برای ایران؛ و این استثنا به دلیل رهبری دروغگو، خشن و بدخواه ایران است که کشورشان را به سوی نابودی کامل سوق می‌دهد. بنابراین، ما یک محاصره کامل اعمال خواهیم کرد، اما تنها برای کشتی‌هایی که به بنادر ایران می‌آیند یا از آنجا خارج می‌شوند، و یا محموله‌هایی مرتبط با ایران حمل می‌کنند. بر اساس گفتگوهای بسیار سازنده با رهبران خاورمیانه، تصمیم گرفته‌ام که «هزینه بازپرداخت ۲۰ درصدی به ایالات متحده» را با توافق‌نامه‌های تجاری و سرمایه‌گذاری جایگزین کنم؛ توافق‌هایی که کشورهای مختلف حوزه خلیج فارس در ایالات متحده انجام خواهند داد. این سرمایه‌گذاری‌ها عظیم خواهند بود، اما در عین حال برای خود آن کشورها و آینده‌شان فوق‌العاده سودمند خواهند بود. همان‌طور که همگان می‌دانند، ما در مقایسه با هر کشور دیگری در طول تاریخ، بیشترین حجم سرمایه‌گذاری دلاری را در ایالات متحده داریم؛ اما این سرمایه‌گذاری‌های جدید آن رقم را حتی بزرگ‌تر خواهد کرد. ما شاهد سرازیر شدن کارخانه‌ها، تأسیسات و تجهیزات به ایالات متحده در سطحی بی‌سابقه خواهیم بود که میلیون‌ها شغل جدید و پردرآمد برای آمریکایی‌ها ایجاد خواهد کرد! آمریکا دوباره در حال پیروزی است؛ پیروزی‌ای که نظیر آن هرگز دیده نشده است. دوران کشتار صدها هزار نفر — از جمله ۵۲ هزار معترض — توسط ایران به پایان رسیده است و مهم‌تر از همه اینکه: ایران هرگز به سلاح هسته‌ای دست نخواهد یافت! از توجه شما به این موضوع سپاسگزارم. رئیس‌جمهور
دونالد جی. ترامپ»
@News_Hut</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/news_hut/68090" target="_blank">📅 19:11 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68089">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kks1VOdzvEdiUM8PKh2sDTpzkYm-hw3oUADxrLGp9eVsj6TCcKe8LNBRRFWbqz-C8H7iFu4npHBolf-AcVkXak4Ng-OZNsh_8e_HNvJKfb-o1OWokHO1bYYm3mE11JhtcTKe_PvpWPGep8isJqjSSqBoG55K7P1sOpXgwVURZz2Iz50EDjJDN1jDfmjT7TP3cM8RzkWpP6raiQ9xqnvJSOICnrFPquZB4hluUuJuVlN8EF9iqLAI7MuDfuO3H8dlJZDNH6_QrCb7zzsvUOPsAJOwwGg3-4QfnEIHXcFn9YfDUxyajl2BlbuQpF4oA8SkADpNg2CMHcibabRFXLl1qg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇺🇸
ترامپ پستی از کاربری که متنی از مصاحبه او با روزنامه گاردین است را بازنشر کرد.
کاربر : «وای خدای من!
اصلاً نمی‌دانستم ترامپ این را گفته است.
آن هم در سال ۱۹۸۸!
جزیره خارک را تصرف کنید!»
متن مصاحبه ترامپ با گاردین ۱۹۸۸:
«اگه من بودم در قبال ایران بسیار سخت‌گیر می‌بودم. آن‌ها از نظر روانی ما را شکست داده‌اند و باعث شده‌اند مثل یک مشت احمق به نظر برسیم. اگر حتی یک گلوله به سمت یکی از نیروها یا کشتی‌های ما شلیک می‌شد، یه بلایی  بر سر جزیره خارک می‌آوردم و وارد عمل می‌شدم و آن را تصرف می‌کردم. ایران حتی از پس عراق هم برنمی‌آید، اما ایالات متحده را به بازی گرفته است. حمله به آن‌ها به نفع جهان خواهد بود.
@News_Hut</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/news_hut/68089" target="_blank">📅 18:28 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68088">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f0d70b0c17.mp4?token=R62CnZl8XIemTpzQEX4RzW4tOY7VhR4ZgobUIUBqicc0Xg9lI2iglsu-2jZAH2pAalfsKAO7VLj6n_DfHU3xxk4xDY-_3zT3Pt0nI8F0pJ-ALkq8tJUOR8Yfc74ev-7vIXfJ9gBk3AakQxNW9fpgImoBI7GRjAbZkHDQnyRVWXhHVs-HIxlWpmaO2ferYCHpTFw5I9Rk5HKwqYVFbcu8ZA5x3n1CkmwYumVJJqxKzpbBxqmkP5K9ISEDjKRNQQXlR9KN9BJK4CC0UXHSrCvm6dyN42aOddEt1siDyAm4sWtuqW9iUWZ5rrFVHAdRbw2vVkS2KEuSPm0-qVbYh9plGQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f0d70b0c17.mp4?token=R62CnZl8XIemTpzQEX4RzW4tOY7VhR4ZgobUIUBqicc0Xg9lI2iglsu-2jZAH2pAalfsKAO7VLj6n_DfHU3xxk4xDY-_3zT3Pt0nI8F0pJ-ALkq8tJUOR8Yfc74ev-7vIXfJ9gBk3AakQxNW9fpgImoBI7GRjAbZkHDQnyRVWXhHVs-HIxlWpmaO2ferYCHpTFw5I9Rk5HKwqYVFbcu8ZA5x3n1CkmwYumVJJqxKzpbBxqmkP5K9ISEDjKRNQQXlR9KN9BJK4CC0UXHSrCvm6dyN42aOddEt1siDyAm4sWtuqW9iUWZ5rrFVHAdRbw2vVkS2KEuSPm0-qVbYh9plGQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
نظر مراد ویسی در پاسخ به مخاطبی که گفت باید حرم امام‌رضا هدف باشد:
@News_Hut</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/news_hut/68088" target="_blank">📅 18:13 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68087">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🇺🇦
❌
🇷🇺
پهپادهای اوکراینی شبانه به ۱۱ شناور در دریای آزوف — شامل پنج نفت‌کش، پنج کشتی باری و یک یدک‌کش — حمله کردند؛ اقدامی که نهمین روز پیاپی از کارزار حملات گسترده علیه ناوگان کشتیرانی روسیه را رقم زد. نیروهای سامانه‌های بدون‌سرنشین اوکراین اعلام کردند که در بازه زمانی ۶ تا ۱۴ ژوئیه، به ۱۱۶ شناور روسی حمله کرده‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/news_hut/68087" target="_blank">📅 17:34 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68086">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4fc10f2868.mp4?token=g1SrYQJBa0qBdriOMeZo2m7fxjJ1kjpsnA5zvNZ0tbR6QnyHSoIDsH5ymf_1sdVo_fKfAKx8hCv8dWSE1KfdwlV_MrDDEV_Eft9C6w_Z3IEOlSM-FSg4TQYRVnaD_-HbL1zA8hI0Zb9K88Rzm-ZuYX0LHB_2LVt7D12siqb6CVJVKtUhI12mK1VjazfH2xb4gmzx7pgEQBbfG1l1Eh1pvoTV9rJlSG9XEzs6TQVPLoCHOPBbTI7Oa3cAlKVc_IjOMsnvwyLxlB5J84ZaJ_PSUcJMZloXaFFYjqqCxXIVNkRo0DCAl0KtmxwElSeOH8UMd9UIiJZSALc5d1rVhd5vj07COwWJqBg3HOShEhlXld-QBbh-U4VjKiWuxZN83qLKZF4w3K-uQd_J432cbNySHXK703AYKkqEyrg23l_hGw_yi_EJMsQDkgrcbodwQVFSezIvLHQQT5CgE58wN2hrnFF5FvDkNoA9p0Z1IUyfzzwqiEUtYo7jybYCPQGYhapDeolF4WL5OIRVK2BpYhonTtfQUn5_VNtS4fSL13JkM5zNJ8ic96siK0lJ75qU1w39s3r6Q0ZtzdecXTTm8Y_arpTnrBqjxVa9Gde8JZ3SfL0qM5VxGNHJERXDdYVV68c3_ss48eMlPutklP-uwuFv1Z2TVPauhaed3YUbk0d5ICQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4fc10f2868.mp4?token=g1SrYQJBa0qBdriOMeZo2m7fxjJ1kjpsnA5zvNZ0tbR6QnyHSoIDsH5ymf_1sdVo_fKfAKx8hCv8dWSE1KfdwlV_MrDDEV_Eft9C6w_Z3IEOlSM-FSg4TQYRVnaD_-HbL1zA8hI0Zb9K88Rzm-ZuYX0LHB_2LVt7D12siqb6CVJVKtUhI12mK1VjazfH2xb4gmzx7pgEQBbfG1l1Eh1pvoTV9rJlSG9XEzs6TQVPLoCHOPBbTI7Oa3cAlKVc_IjOMsnvwyLxlB5J84ZaJ_PSUcJMZloXaFFYjqqCxXIVNkRo0DCAl0KtmxwElSeOH8UMd9UIiJZSALc5d1rVhd5vj07COwWJqBg3HOShEhlXld-QBbh-U4VjKiWuxZN83qLKZF4w3K-uQd_J432cbNySHXK703AYKkqEyrg23l_hGw_yi_EJMsQDkgrcbodwQVFSezIvLHQQT5CgE58wN2hrnFF5FvDkNoA9p0Z1IUyfzzwqiEUtYo7jybYCPQGYhapDeolF4WL5OIRVK2BpYhonTtfQUn5_VNtS4fSL13JkM5zNJ8ic96siK0lJ75qU1w39s3r6Q0ZtzdecXTTm8Y_arpTnrBqjxVa9Gde8JZ3SfL0qM5VxGNHJERXDdYVV68c3_ss48eMlPutklP-uwuFv1Z2TVPauhaed3YUbk0d5ICQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
بخشی از مستند "عمامه صورتی" که در سال ۱۴۰۲ تولید شد.
@News_Hut</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/news_hut/68086" target="_blank">📅 17:03 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68085">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e3a6a36a19.mp4?token=O8gvHiIwVB5fnUo4TLjqFs_mS9m6-0JoPg3JvkQlPC-K7mPj3UPjSTucRkz9KB73_O1irFwGbSoRYFEUShvge_hBMBlkeNFDNGEG7Tnl3LMh6Yg3BGtzwP1S0Ku9RsS6-mnu08ee9zS3sQIgPXsPm5iXkF1Di-jf_YXLGm_WdJSOYnAnAxQfUQEOOf7bU5U3RgjPY5_KicAojX8zBwMYZ5zDqTyrCvEyRYmWOoI71jOOmBrHoLUp3g_mtNQYEdOTCshmyVAwk8byC8NeceJb2J0w8mMBsXPW-SV7koWrCl4g3s5oUBNBppp3TjNqSYBz1voJI4MgFHIWBtxPGhYuxg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e3a6a36a19.mp4?token=O8gvHiIwVB5fnUo4TLjqFs_mS9m6-0JoPg3JvkQlPC-K7mPj3UPjSTucRkz9KB73_O1irFwGbSoRYFEUShvge_hBMBlkeNFDNGEG7Tnl3LMh6Yg3BGtzwP1S0Ku9RsS6-mnu08ee9zS3sQIgPXsPm5iXkF1Di-jf_YXLGm_WdJSOYnAnAxQfUQEOOf7bU5U3RgjPY5_KicAojX8zBwMYZ5zDqTyrCvEyRYmWOoI71jOOmBrHoLUp3g_mtNQYEdOTCshmyVAwk8byC8NeceJb2J0w8mMBsXPW-SV7koWrCl4g3s5oUBNBppp3TjNqSYBz1voJI4MgFHIWBtxPGhYuxg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
سنتکام ویدیو ای از حملات به ایران در طول شب منتشر کرد.
در اواسط ویدیو نشان میدهد که لانچرها در فضای باز هدف قرار میگیرند.
@News_Hut</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/news_hut/68085" target="_blank">📅 16:15 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68084">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NzRm6QXeLf7hFbvhzxtCiiJSS5cD3aWW8tAi21VQxbRYwdl7IZBrdq5nH0ZZA8cFQ84W4rciAZ8WaVwPKN9tcJtR3n4wKduwn0gRBjQ4irh_Sp7IRZavanKV0eH9XEKcs8YDyfu-CffPAczZjLEdwEcBcylTFFwZL9HRQCH5n23iDxtUF_OP41ixDrmM0iq5RMcQoSHkjrYP53vcbzWh8ltyXnl9Kte2LMgNGZ0aPL6o36F1RXJn1sO9pHaYDzJj4K9YKJN5uia-bHKpiJJOolJ4kE1DdBfIdjtaiaNh9Fe-RuP-doX5TAJ8dP5Daeo8nKCLq6kcREP8hzwBwZUnBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
دیکتاتور قالیباف
؛
سید محمود نبویان نائب رئیس کمیسیون امنیت ملی مجلس و ابراهیم عزیزی سخنگوی کمیسیون را که از مخالفان سرسخت توافق بودند از هیأت رئیسه کمیسیون امنیت ملی حذف کرد.
عباس مقتدایی نماینده اصفهان و از حامیان دوآتشه عراقچی به عنوان نایب رئیس اول و حسن قشقاوی از دیپلماتهای حامی برجام به عنوان سخنگوی این کمیسیون انتخاب شدند
.
بهنام سعیدی از نمایندگان نزدیک به قالیباف و یعقوب رضازاده نماینده سلماس که اخیرا در مناظره‌ای با ثابتی از توافق با امریکا حمایت کرده بود نیز به عنوان دبیران اول و دوم این کمیسیون انتخاب شدند.
@News_Hut</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/news_hut/68084" target="_blank">📅 15:31 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68083">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/311dccf46f.mp4?token=oMa9QmSQMiuUNgVBZyBylPnxa1duRflFOg1ECwOhLhQCKwJpAflwXjovi1KwQkksxTmDlg0FsLfasptfrOK1RrEWM8H-dtG_LPfHKUlIWXSaP918NHWJ3O9f3pEWud7GF9EtKS-TUR28AFWjIUICVQKSuKuM-pSOH9k86XYQP5AarGu1ELFCfNDKnSNqSKbUog9MRo0CZJ3yVI9f49SCkppMwwPz1pOh3py9l-XTdLFpnPyvrYYiaG8RdusykbU6fvmWZhiwMc5Y6PuOA_gJaLmpPQmggNRwMaKoiHl1F6h1SMJCgZMHQRbt-v0b1XwVG6m46HfmtVXMW__1NJjVeA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/311dccf46f.mp4?token=oMa9QmSQMiuUNgVBZyBylPnxa1duRflFOg1ECwOhLhQCKwJpAflwXjovi1KwQkksxTmDlg0FsLfasptfrOK1RrEWM8H-dtG_LPfHKUlIWXSaP918NHWJ3O9f3pEWud7GF9EtKS-TUR28AFWjIUICVQKSuKuM-pSOH9k86XYQP5AarGu1ELFCfNDKnSNqSKbUog9MRo0CZJ3yVI9f49SCkppMwwPz1pOh3py9l-XTdLFpnPyvrYYiaG8RdusykbU6fvmWZhiwMc5Y6PuOA_gJaLmpPQmggNRwMaKoiHl1F6h1SMJCgZMHQRbt-v0b1XwVG6m46HfmtVXMW__1NJjVeA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
فرماندهی مرکزی ایالات متحده(سنتکام):
ملوانان آمریکایی بر روی ناو «یو‌اس‌اس جورج اچ. دابلیو. بوش» (CVN 77) عملیات پروازی انجام می‌دهند.
@News_Hut</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/news_hut/68083" target="_blank">📅 15:08 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68082">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IRUWbADyl0UKPQx1c7cTqGdM1QxISW1fEUQ8Da75gf6W5dNsT1lF4TOyvX1NvL9bjumy53P_S7PJawoC1ek0efvqyH0vaeyBAi95nsHz-h5-OJekJZH80nFSjbZ2T_CMdQHHPx5n0L5BFU0VuXlqFyoHf_U2sCHmlhfYohsKZG0Xgc0lJ-iHsw2ul6CWT49TGeH5C2bLcQcg57kFl27_5b8310JZLoS_-QaCIrHNegOCKXv_Z_yfChUaAyqSFkOAdJjbnwzjnkciZ25-Xmb6FiKdrdYWQXLE78R7kaCsMjVn7mRtoJGiNu03D0K4TNwiqHd6XvY4i5tGvtK66ywsog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
لبنان و اسرائیل مذاکرات خود را در رم از سر گرفتند؛ در حالی که لبنان به پیشرفت در جهت عقب‌نشینی ارتش اسرائیل و اسرائیل به پیشرفت در جهت خلع سلاح حزب‌الله امید دارند.
@News_Hut</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/news_hut/68082" target="_blank">📅 14:33 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68081">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1fec092b37.mp4?token=tjf6s6dcZmz-B_1YySOejjQDzIaSNaQIPWlYY3csgAFJFTEzBDmbsQ-LqQRVziEDKzsan4z9uuKC3G-YMLFpgYCPkF7PlTfiluq34vgtQmj7JIocB8H3YWIgWYhLFjjVE36QA1p0deB0b9Fe84yy6oXBrhThbpbD7apzkvP2kRDrUaCmVEjyrh3rS2wofUjfpZwBMxn0DELgZfjkZ9zw9MYTXNYxgKiFkjGMT-Pkd_HnAGNxktZzxuhtEXWMqudEm-yhbq43UtO4eT1DT3o-6p7yCsc2hQAScjc7z4ZRSEA1Fbz5Knxry3_-K0adkmRmChdCoiB1eKvEOWskK6s6eg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1fec092b37.mp4?token=tjf6s6dcZmz-B_1YySOejjQDzIaSNaQIPWlYY3csgAFJFTEzBDmbsQ-LqQRVziEDKzsan4z9uuKC3G-YMLFpgYCPkF7PlTfiluq34vgtQmj7JIocB8H3YWIgWYhLFjjVE36QA1p0deB0b9Fe84yy6oXBrhThbpbD7apzkvP2kRDrUaCmVEjyrh3rS2wofUjfpZwBMxn0DELgZfjkZ9zw9MYTXNYxgKiFkjGMT-Pkd_HnAGNxktZzxuhtEXWMqudEm-yhbq43UtO4eT1DT3o-6p7yCsc2hQAScjc7z4ZRSEA1Fbz5Knxry3_-K0adkmRmChdCoiB1eKvEOWskK6s6eg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
‏بر اساس گزارش نیویورک تایمز:  اسرائیل سال‌ها تلاش کرده بود محمود احمدی‌نژاد، رئیس‌جمهور پیشین ایران، را به‌عنوان یک منبع اطلاعاتی بالقوه و همچنین گزینه‌ای برای رهبری ایران پس از تغییر حکومت پرورش دهد. در چارچوب این تلاش، مأموران اطلاعاتی اسرائیل در سفرهای…</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/news_hut/68081" target="_blank">📅 13:41 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68080">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🔴
معاون استاندار بوشهر:
چهار نقطه در شهر بوشهر مورد اصابت بمباران آمریکا قرار گرفت.
@News_Hut</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/news_hut/68080" target="_blank">📅 13:31 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68079">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D3BSr_HcCJ1UcT-Cxpzn0PSIJ8o_klmbw0fJseeYzXSl85ZNW_LsGL5rLAn-AFuHgsOzEntC0zjOF1ItSyBNX_I4Iq76fhNnQucFzboqgc2eN5t4WFiYdbB_abRWZvW_iuZ_aSDtiZ_3qlJnWtjSFi2JA6l4DTWZhxHwkklaKNLFuvvc8H25dm0631ebXScauptB7FCc-RgmmjwxaR4_Bxu9rNNQgKH35pPSXiAIg8Iam0lMFsARxLNlOpECbcBfXkXzP-FbIWMU7B4nPbV6NVZJ4rBuytICRZUAyXRMiGOwsh177m4XPhDo5_3zrG-QoP0zIMFeuwuzatxn2U5JlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
نمایی دیگر از بوشهر
@News_Hut</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/news_hut/68079" target="_blank">📅 13:02 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68078">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aqGK8KzdgPHFQc8bbbK4_FEb4-pF482uEfdWvXZPvDwWpzDelhwig192HkWmG_UV16qgyq5Jl-apciZPWKwTbhIWXDXzF-9QmjFgmdyxN4g5t8RQNXv4WPUDd9ARKx75Mfqsmk4TYBTv-UOLdPy8tZCFtkCAI2GITWRllIne2RIvfLBwa6kbrERcZf7m0YSCY9PuQeLwb47zJ54K-kdDQAwey3B3T0rYSwQ1oSKLhY3P9Qn_xMMzAsNK_hvnv84_Qny9rnrmMJM6oBp7qKm4gOh8_X3fEvzHxP3X5RE6AtVbE0Wn3nTASSJundcfRyk1-A4wl-jyibauvh5HmO02Jw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
سه انفجار در بوشهر  @News_Hut</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/news_hut/68078" target="_blank">📅 12:53 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68077">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🚨
🚨
🚨
سه انفجار در بوشهر
@News_Hut</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/news_hut/68077" target="_blank">📅 12:50 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68076">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🚨
🚨
🚨
پنج انفجار در بندرعباس
@News_hut</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/news_hut/68076" target="_blank">📅 12:49 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68075">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🚨
🚨
🚨
انفجار شدید در بحرین
@News_hut</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/news_hut/68075" target="_blank">📅 12:47 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68074">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🚨
🚨
🚨
#مهم؛ گزارش های اولیه و #غیررسمی از حمله سپاه به سفارت اسرائیل در بحرین  @News_Hut</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/news_hut/68074" target="_blank">📅 12:45 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68073">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">🚨
🚨
🚨
#مهم
؛ گزارش های اولیه و
#غیررسمی
از حمله سپاه به سفارت اسرائیل در بحرین
@News_Hut</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/news_hut/68073" target="_blank">📅 12:45 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68072">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3e106612ba.mp4?token=KtvJqLZHPBLtkDjxAFC02nyjTMbp1Qz8qRNQMJkSYOtB0cynkiYD8Kb3UsJE_qS-yZb1Gh_8Mz04-ggABSY0sU7LUzHuWQNFss-OzuTWAArFAwYsO40Cez2cgL7t4_RGmhkQsbFH-SZPcOneibZK7mEDLUNF-omd4ggSur0V1vkj_y6idGs3FGsoak16sMU6Yg8vsMqfiMSIkxeIorYdxorudutC7ZaFnXpwRWN-F6-OUoFIsFNSBiYVLddn_iOi5SOi9sLzjm_KJ1j-NvZPV9GR_zHsT97gGwtQkdC5D7iwhS8udYyYQ0npVxEAOA4nOFa1C5innYx0HdUYF8XhXA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3e106612ba.mp4?token=KtvJqLZHPBLtkDjxAFC02nyjTMbp1Qz8qRNQMJkSYOtB0cynkiYD8Kb3UsJE_qS-yZb1Gh_8Mz04-ggABSY0sU7LUzHuWQNFss-OzuTWAArFAwYsO40Cez2cgL7t4_RGmhkQsbFH-SZPcOneibZK7mEDLUNF-omd4ggSur0V1vkj_y6idGs3FGsoak16sMU6Yg8vsMqfiMSIkxeIorYdxorudutC7ZaFnXpwRWN-F6-OUoFIsFNSBiYVLddn_iOi5SOi9sLzjm_KJ1j-NvZPV9GR_zHsT97gGwtQkdC5D7iwhS8udYyYQ0npVxEAOA4nOFa1C5innYx0HdUYF8XhXA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
صداسیما داشت خلاصه‌ی یه سریال رو پخش میکرد که تو یه تیکش اگه فقط صدارو گوش کنید، فکرمیکنید صداسیما در حال پخش پورنه:
@News_Hut</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/news_hut/68072" target="_blank">📅 12:15 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68071">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e0c3704c1a.mp4?token=dnUxSI5mmjm2BJ0QIQjX6cfeCkNaUc13Kqu77I5tci6K99EjInfdtJnGOH1hWrm89BTRUP4n3blFe4KgC2nxA7XydW4oWmyRIviEn7tg4v-6JIw6Tk1Amk9b8fc3FpOgubr7XhRuH-Hdz_g7-5ehJWgRrsTWrF-sEl9xRSrpNKwP0axuKTj-CSDSdxAXl4-x-RvLnaQv2jnaMkCrnnqh53Jo_P3nqiPicgMesk3c-RYGbz_mwiON0FYkP2Od36wDlKcXMTbCLAYm5Z9YLW169DqKRpJMmie_T41zkVfqVH6bJ8g9_zX5hJ53_jA-6CBhhVxkRzZoj9yEYitC04XJvg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e0c3704c1a.mp4?token=dnUxSI5mmjm2BJ0QIQjX6cfeCkNaUc13Kqu77I5tci6K99EjInfdtJnGOH1hWrm89BTRUP4n3blFe4KgC2nxA7XydW4oWmyRIviEn7tg4v-6JIw6Tk1Amk9b8fc3FpOgubr7XhRuH-Hdz_g7-5ehJWgRrsTWrF-sEl9xRSrpNKwP0axuKTj-CSDSdxAXl4-x-RvLnaQv2jnaMkCrnnqh53Jo_P3nqiPicgMesk3c-RYGbz_mwiON0FYkP2Od36wDlKcXMTbCLAYm5Z9YLW169DqKRpJMmie_T41zkVfqVH6bJ8g9_zX5hJ53_jA-6CBhhVxkRzZoj9yEYitC04XJvg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
چمران رئیس شورای شهر تهران به سوالی درباره قطعی برق بدون اطلاع قبلی:
اگر می‌دانستید دو روز پیش چه تعداد تاسیسات برقی را زدند دیگر این سوال را نمی‌کردید.
@News_Hut</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/news_hut/68071" target="_blank">📅 11:31 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68070">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aNUdgqL8nQQ9pw1-uF9Cjo2XQAdk1koVVyJZUiS3r-HfMA2gKpyRc1oUiuNGKBb-J_TlXzYAMbN9qqJchvNB8L8vOO6MQxpws2aTEwGWXT-REzudZ9Zi0HH4-NpgFIsn0c2cYI-pANdZI18BTUjU8M1Qdzq3tWYCjz3D24kNTvq2SR6ON-SPY1G3XzJv8AUjUYUqiwXbHd5JPD9Bh3OT0m0s3ChQ1wN5zzXAxpz0dtpqQk9bp8ODhNvmmw8VytXbARCEcPIH8OfasQXvMro4JSIiqNTlcRa9IEcqYBjrmYviBDtPshlNfP31_J9kXmnLbe7QX0Lt_oEUJN1lfBFXNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
سازمان تجارت دریایی بریتانیا:
گزارشی از یک حادثه در فاصله ۱۳ مایل دریایی جنوب شرقی لیماه، عمان، دریافت کردیم
یک نفتکش گزارش داده است که هنگام تردد در مسیر جنوبی به سمت خارج، مورد اصابت موشک قرار گرفته است.
@News_Hut</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/news_hut/68070" target="_blank">📅 11:18 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68069">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/17cbe780cf.mp4?token=VrsdDl_tG6oObrnJMm1ODMYUqzIN5MoH_079k-MCd7H8TlfBSDbG5NFPJjr_SPQbQ-NWPqDH4N3F65Z8e5ayrsG-fXVxkH5tyUayx5VsoRmak7PC53krVLAKZDJfQnwN6hp2efHbgoGgfTVc56gVz39TlWQD47bOXv9y0s0SX1zx8ZZskT2oR052OXXKr4alf-AyGlP6Khv2oo-dGmsqL94I_1D7jdgAIvoI1GkuiDvFU4Gn9_n0oV0pZ1rVFcrHU081B0APMpISi15XBkT_SPLI8iBWS-qz3tHQpOhsnpkMKK6B6K41b4gm6gQp0Z1Boz_7BckkOA_Mn9DMUwOv4w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/17cbe780cf.mp4?token=VrsdDl_tG6oObrnJMm1ODMYUqzIN5MoH_079k-MCd7H8TlfBSDbG5NFPJjr_SPQbQ-NWPqDH4N3F65Z8e5ayrsG-fXVxkH5tyUayx5VsoRmak7PC53krVLAKZDJfQnwN6hp2efHbgoGgfTVc56gVz39TlWQD47bOXv9y0s0SX1zx8ZZskT2oR052OXXKr4alf-AyGlP6Khv2oo-dGmsqL94I_1D7jdgAIvoI1GkuiDvFU4Gn9_n0oV0pZ1rVFcrHU081B0APMpISi15XBkT_SPLI8iBWS-qz3tHQpOhsnpkMKK6B6K41b4gm6gQp0Z1Boz_7BckkOA_Mn9DMUwOv4w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
مراد ویسی،تحلیلگر ارشد اینترنشنال:
چشم انداز موجود تشدید جنگه،پاکستانم دیگه نمیتونه بین ایران و آمریکا میانجیگری کنه.
جنگ سوم بین دو کشور تو روزای آینده شروع میشه.
اگه اسرائیلم وارد بشه یه لایه دیگه از سران جمهوری اسلامی رو حذف میکنه.
@News_Hut</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/news_hut/68069" target="_blank">📅 11:00 · 23 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
