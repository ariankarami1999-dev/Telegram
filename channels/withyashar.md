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
<img src="https://cdn4.telesco.pe/file/t_for7lS4rNkINm1mIZdM0YJA5LlLz7L4jR4vODzfJwervoyEMKdwVn_pyTgmaALUtAbnpVyacThTR-5wZ4ywq7ud9AdXzqXDzIUZ-l7vJRlnlnLVYm8EgQ9eASerwQKmrTU3yaz1ij2JUpElWlVKcekbQO7W-qi8J70YncvLloKew8Eu2xDBvGxX71yzEaKIj2uULjIpm1XuaSCJAnls3dNWVZJqftWIsIfB_1DNYzol5mBjKfonJpIBJNxvSjQklkpR-EKkVCtM4wDbkVb1ITHGBLG-Mdizurb9-hLcC65BU9_fm6TZWl0AWh10vz2_RyUJ3o7YBr9XCH_qshEiA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 WarRoom with YASHAR</h1>
<p>@withyashar • 👥 442K عضو</p>
<a href="https://t.me/withyashar" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 چنل رسمی«اتاق جنگ با یاشار»اخبار لحظه ای و فوری از‌ جنگ با تحلیل📸instagram.com/yashar🐦x.com/yasharrapfa📺youtube.com/yasharrapfa⛑️paypal.com/paypalme/yasharrapfa</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-01 00:15:21</div>
<hr>

<div class="tg-post" id="msg-21360">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromM</strong></div>
<div class="tg-text">الان ما تخم مرغ لازم داریم چطوری تخم بزاریم. یه امار بگیر اگه کسی بلده به مام یاد بده</div>
<div class="tg-footer">👁️ 5.13K · <a href="https://t.me/withyashar/21360" target="_blank">📅 00:13 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21359">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">محسن کج بند رضایی : مردم خودشون در خانه‌ها و محلات شروع به تولید محصولات مورد نیاز جامعه باید بکنند.
@WarRoom
یاشار : یعنی‌کوکتل مولوتوف درست کنند ؟
😂
😂</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/withyashar/21359" target="_blank">📅 23:55 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21358">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f2d5b2a1a8.mp4?token=OnErIkDTeI21Anycforx8wsHH8xnw6QxbX5Nn8cp31E5WvyvqnYDQUS4GzpJQNOH7gfPn4754cgRhKGB11tt6WHlMbIoBBnVrI5sWDdS0m3QAf8E9PUrtUH0Y9mJYzJSMPoZ6el6DqPXPLvjWM9Kza6uwfDqxoehdDnV7cRTuz_bDRiek_nRrQFdSku3Lhf6DH9OXdlMQ14VBI3At1R_5Lp6bm-LkTqkkLWgz-1T8t_GCrkLUX4w-WiTHo-blOskHv_Gvr5lpRp8vIs2JiZHyuKvMwceLrcNR3ieyrmC-TDTLt48S2uYABUY84GWzGfrPyjkAsfcKkYLbPzo26I4xg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f2d5b2a1a8.mp4?token=OnErIkDTeI21Anycforx8wsHH8xnw6QxbX5Nn8cp31E5WvyvqnYDQUS4GzpJQNOH7gfPn4754cgRhKGB11tt6WHlMbIoBBnVrI5sWDdS0m3QAf8E9PUrtUH0Y9mJYzJSMPoZ6el6DqPXPLvjWM9Kza6uwfDqxoehdDnV7cRTuz_bDRiek_nRrQFdSku3Lhf6DH9OXdlMQ14VBI3At1R_5Lp6bm-LkTqkkLWgz-1T8t_GCrkLUX4w-WiTHo-blOskHv_Gvr5lpRp8vIs2JiZHyuKvMwceLrcNR3ieyrmC-TDTLt48S2uYABUY84GWzGfrPyjkAsfcKkYLbPzo26I4xg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اتشبازی برای اجرای‌حکم عروسکهای نتانیاهو و ترامپ بود
😂
@WarRoom</div>
<div class="tg-footer">👁️ 47.2K · <a href="https://t.me/withyashar/21358" target="_blank">📅 23:34 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21357">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">گزارش های زیاد از انفجار در تهران سمت انقلاب فعلا میترسم یهو میگن جشن امام ۱۸ ام بوده
😂
فقط بدونید @WarRoom
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 49.2K · <a href="https://t.me/withyashar/21357" target="_blank">📅 23:32 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21356">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Lj7_iDTiWWetFs9Ssh33RCy2qHlGLMLVHa74DT0MdEE82Jv33jN4tqxOEpqPRUw6nCzBH36F9e8eIOtBHb-7XRDSXC7MqPQcgHB8fLmaigvPCWYGg_inpK8hMZ0g0tT5l3qmQjys0KBJ9pwf67T6EEPbsu4M8XlcpAUdX5kIiC0WvZVyWJepYl5jYbBhrs2CXQ1moFzHq2tMsYa9fPzFaTGSvFIkH4REe2VdFiaQx8iue3F0uUF_HH5-Sgzccx9vFOx4vgmFo0fB54G-6yrEB-wsfJxK8Q6xGWOcTUOvaYzzoSIdZAevVxd3adPBv8fvpS7l3aCiz37A3irIBqpIbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گزارش های بسیار زیاد ، ستون دود تهران از زاویه دیگر
🚨
🚨
🚨
@WarRoom</div>
<div class="tg-footer">👁️ 60.5K · <a href="https://t.me/withyashar/21356" target="_blank">📅 23:20 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21355">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/01b588a12e.mp4?token=WalshWnyQ-f5LYMY0X1ZK22WdL_sGovLvpSxU6g21HUOgjPAZ_daaaSH_JcEHh1u2cbtQrHUbIxcI0H0EwwyF-kXA-tDT-WUaONWRXOvCnoMSiZ2Vi5SQxdYEkXR05UeRtiSi-NYHcivOZUcv9-pCWhBHvlsLYfnan32Cqi7dLNsPUSPGCd8lHZgDZXGpcJjJX1ivDVHGlBlHWaW7Rd-UJbAUZUTDrFEMEr81VhWf3icckNWJHtnByuR6l4Vlkw3GghIEkA0z-48SNSf8atsE0oiRXt_oS9_67i8gKZmutacmdt-2uFSPT2qPubtjPfFwCXEaxyReKOLtmK5g3cUEw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/01b588a12e.mp4?token=WalshWnyQ-f5LYMY0X1ZK22WdL_sGovLvpSxU6g21HUOgjPAZ_daaaSH_JcEHh1u2cbtQrHUbIxcI0H0EwwyF-kXA-tDT-WUaONWRXOvCnoMSiZ2Vi5SQxdYEkXR05UeRtiSi-NYHcivOZUcv9-pCWhBHvlsLYfnan32Cqi7dLNsPUSPGCd8lHZgDZXGpcJjJX1ivDVHGlBlHWaW7Rd-UJbAUZUTDrFEMEr81VhWf3icckNWJHtnByuR6l4Vlkw3GghIEkA0z-48SNSf8atsE0oiRXt_oS9_67i8gKZmutacmdt-2uFSPT2qPubtjPfFwCXEaxyReKOLtmK5g3cUEw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صدای انفجار و ستون دود تهران ، دقایقی پیش
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 63.5K · <a href="https://t.me/withyashar/21355" target="_blank">📅 23:17 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21354">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A3eUSLbcViolsO_Fbx8GEtEnHWB226K5iOIV090ERSphpuWqWIbz2Hfq7MiQIpUpnXXrY0PkkIrhHD2_fOLaa27TbtZMmf0y28j29-LbWoMdPUAUXnsqXte2gpVVz2xP0hZuMqdZXQYgnnIT2VEgFJipHjhb-eKblsBjaCwmO98G1PRs9J-7XteZU0OiKrD0xSBYZEwO8I54wCdYKSDq1vR00VLkVW5Q6D7PBdGlLvhK0S4lyQKR5wgMJ338NCthNS4VXfYUzGH-u6b_mS1u6N-L_pWJeGepglCTUA8gtc8xLn958XwVuiSRisk6mL7RnDyoLx5bLNxJh6NFCBkEkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینم دودش ولی احتمالا بخار مال خشکشویی عمو خشکخشکیاهو است
@WarRoom</div>
<div class="tg-footer">👁️ 63.5K · <a href="https://t.me/withyashar/21354" target="_blank">📅 23:12 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21353">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">گزارش های زیاد از انفجار در تهران سمت انقلاب فعلا میترسم یهو میگن جشن امام ۱۸ ام بوده
😂
فقط بدونید
@WarRoom
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 65.6K · <a href="https://t.me/withyashar/21353" target="_blank">📅 23:08 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21351">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">موشک های کروز ضد کشتی به سمت کشتی های بدون مجوز در تنگه هرمز شلیک شده @WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 66.6K · <a href="https://t.me/withyashar/21351" target="_blank">📅 23:05 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21350">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">محسن کج بند رضایی : ما با عمان روی مسیر تنگۀ هرمز توافق کردیم که یک مسیر میانی است اما این موضوع روی کاغذ است و تنگۀ هرمز زمانی باز می‌شود که آمریکایی‌ها به تعهداتشان عمل کنند
@WarRoom</div>
<div class="tg-footer">👁️ 66.7K · <a href="https://t.me/withyashar/21350" target="_blank">📅 23:03 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21349">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-footer">👁️ 67.6K · <a href="https://t.me/withyashar/21349" target="_blank">📅 23:00 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21348">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">گزارش های زیاد از صدای تیر اندازی در شهر اندیشه
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 69.7K · <a href="https://t.me/withyashar/21348" target="_blank">📅 22:55 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21347">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">محسن کج بند رضایی: در صورت ادامه محاصره اقتصادی شرکت های اقتصادی آمریکا را در منطقه خواهیم زد
@WarRoom</div>
<div class="tg-footer">👁️ 73.8K · <a href="https://t.me/withyashar/21347" target="_blank">📅 22:44 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21346">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">وزیر اقتصاد جمهوری اسلامی : احتمال انحلال چندین بانک در ایران وجود دارد
@WarRoom</div>
<div class="tg-footer">👁️ 82K · <a href="https://t.me/withyashar/21346" target="_blank">📅 22:23 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21345">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">آغاز موج جدید سنگین حملات هوایی اسرائیل به جنوب لبنان
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 85K · <a href="https://t.me/withyashar/21345" target="_blank">📅 22:09 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21344">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">گزارش های بسیار از صدای انفجار مهیب از تنگه  @WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 86.1K · <a href="https://t.me/withyashar/21344" target="_blank">📅 22:03 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21343">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">اورشلیم پست گزارش داده است که اسکات بسنت، وزیر خزانه‌داری آمریکا، قرار است روز دوشنبه ۲۴ اوت در یک نشست خبری جزئیات برنامه جدید دولت ترامپ برای تشدید فشار اقتصادی بر ایران را اعلام کند. این نشست ساعت ۲ بعدازظهر به وقت شرق آمریکا برگزار می‌شود که با توجه به…</div>
<div class="tg-footer">👁️ 88.1K · <a href="https://t.me/withyashar/21343" target="_blank">📅 21:56 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21342">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">گزارش های بسیار از صدای انفجار مهیب از تنگه
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 87.8K · <a href="https://t.me/withyashar/21342" target="_blank">📅 21:48 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21341">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">کانال 14 : تهران آماده است تا فهرست اهداف خود را گسترش داده و شبکه‌ها و تأسیسات انرژی منطقه‌ای را فراتر از مرزهای دریایی تنگه هرمز هدف قرار دهد
@WarRoom</div>
<div class="tg-footer">👁️ 87.2K · <a href="https://t.me/withyashar/21341" target="_blank">📅 21:45 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21340">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">نتانیاهو: تا زمانی که من نخست‌وزیر هستم اجازه نمی‌دهم هیچ کشور فلسطینی تحت کنترل ایران تشکیل شود
@WarRoom
🚨</div>
<div class="tg-footer">👁️ 91.1K · <a href="https://t.me/withyashar/21340" target="_blank">📅 21:13 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21339">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/anc5M80BZGWWqPnLTxLNwoIQ8FSpBFC7m62tZPDchyJ3na9ngPYxgzXZf7zUKUy2nTEBVXxgR3F3rSv8wK6Duj2fWis72q3uHFcFSc7Wken18BewVhuSiqh5MEi6Ejahzr5xbV1R-mE-FWkNfjOdyzzspechd6hhnChNT2SpZN07d1w1MF-0gQLY8k0bXatFxP9sSNfFCtV5T6DIR4jGxinkOo3zAKsewx_lhlsaYCBHL4RfdZG7woePRstC0xjsu3SKcMu_bJM2O9R1EgwGQHGCDN7hCuR_hxHiFnLNGwJLxtYambwDNE2xd1AL8zcgSXuKrxDy4nyP7mEQhKYK_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتش اسرائیل
یک فرمانده گروهان را که حملات تروریستی را هدایت می‌کرد و در تلاش‌ها برای بازسازی زیرساخت‌های زیرزمینی حماس شرکت داشت، از بین برد.
@WarRoom</div>
<div class="tg-footer">👁️ 96.5K · <a href="https://t.me/withyashar/21339" target="_blank">📅 20:21 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21338">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">جروزالم پست در یک یادداشت دیدگاه هشدار داده است که اسرائیل باید گسترش نظامی ترکیه در سوریه و شرق مدیترانه را یک تهدید راهبردی جدی تلقی کند. نویسنده با اشاره به حمله اخیر اسرائیل به پایگاهی نزدیک ادلب، مدعی است
ترکیه در حال ایجاد سامانه راداری و پدافندی در آن منطقه بوده است
. او با استناد به هشدارهای کمیسیون ناگل، حتی احتمال تبدیل‌شدن تهدید ترکیه و سوریه به خطری بزرگ‌تر از ایران را مطرح می‌کند و خواستار تقویت نیروی دریایی اسرائیل و تعیین خطوط قرمز برای آنکارا شده است. در پایان نیز با لحنی بسیار تند می‌نویسد:
«از ادلب تا استانبول، اسرائیل در صورت لزوم حمله خواهد کرد، نه دفاع.»
این موضع، دیدگاه نویسنده مقاله است و اعلام رسمی دولت یا ارتش اسرائیل نیست.
@WarRoom</div>
<div class="tg-footer">👁️ 97.8K · <a href="https://t.me/withyashar/21338" target="_blank">📅 19:43 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21337">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EkcZT8hxbri9jT-A5Fpzd7hGBhWWGki-D27B4_TATLbtDsjmbr7xVFZ5tzKqR5tX-5BlhAYHBcTUJcOZrvwHdyJ5SRj82-mh2PujUdd2mElLeC_M7JotLY6S7db9-ZibDYMW0v3NSAU-SD8Y7qrLh1y3VrwonZ3t4cC_DqVRcCVECP45VY91JCPKTosGFdYY3giRew775ix-hGSkmmXJy6kSS1Lwr9bEbilKbcWm1QSfJ8uJ8UfnRCsH26iuOHvVCMcb8h0XBzR5LERyO9rHk1zCiD6nTgNPo7KQ75Vr_HdTac1MJiIK7MFlLTQvP9Bdv_uR2mQlh86-Yb3rxuLXBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اورشلیم پست گزارش داده است که
اسکات بسنت، وزیر خزانه‌داری آمریکا، قرار است روز دوشنبه ۲۴ اوت در یک نشست خبری جزئیات برنامه جدید دولت ترامپ برای تشدید فشار اقتصادی بر ایران را اعلام کند
. این نشست ساعت ۲ بعدازظهر به وقت شرق آمریکا برگزار می‌شود که با توجه به اختلاف زمانی فعلی
، برابر با ۹:۳۰ شب دوشنبه به وقت تهران است.
بسنت پیش‌تر صراحتاً گفت:
«ما این رژیم را فرو خواهیم ریخت.»
@WarRoom</div>
<div class="tg-footer">👁️ 98.8K · <a href="https://t.me/withyashar/21337" target="_blank">📅 19:07 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21336">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">اکسیوس به نقل از مقامات آمریکایی: حدود 40 تانکر نفت شب جمعه از تنگه هرمز، به سمت مسیر عمان و مسیر آمریکایی، عبور کردند. این میزان معادل حدود 16 میلیون بشکه نفت است. @WarRoom</div>
<div class="tg-footer">👁️ 96.8K · <a href="https://t.me/withyashar/21336" target="_blank">📅 18:20 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21335">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">یاشار : کتاب اوستا ، یسنا ۴۳.۱ آمده: «اُشتا اَهمایی یَهمایی اُشتا کَهمایچیت»  «خوشبختی نصیب کسی می‌شود که برای دیگران خوشبختی بخواهد.»  @WarRoom</div>
<div class="tg-footer">👁️ 96.9K · <a href="https://t.me/withyashar/21335" target="_blank">📅 18:06 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21334">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/89d69f232e.mp4?token=PxU4G4zk3ymNZc4QDXtul76hJReqQ32YorT2N6jhtNw0XErIqrlF9o-uKd1H0WZb5Fo3UspL-oFD4pcPNJJnul1QegQsfp-gYN0wavS5txzBQoPRg7JX0o2tDuG8daMwPpDzjdMJxA66iUbDSRCFqvGk1mylEv5SLD_Jn1kJWCFJfFgMih1PwVF8RA3wLwyqXP1Sc6Y8zlz4LVBEwYMBKua6a_hYMZwyhX7z63SJhS3n-HfwbFrNEg0TBzHnS0nSUvdirN-bitblJ170yBKwlG-1I6Z2OmEWeV_je3A5CzsHhmSgSQs3C2bRmLv7BA_2rPeT3_TeTzUADkWXyY2svkvOUa2nismFFSmskKXPLcZEKkxfimWW6oR7L7w8_IZn8wwjT2QIJ3k9j38yHa6tCnX8Ji3X6ffYXaGj8xKQemlKB2Z_G7cERld135mnJyCzgMoie8o-kr2QgB0sfSWJPCHxOd5kERaenzaGlc7QvCOw89uYzLxwMCEHE15pjZUnefAvMVEQDDDxr_MvC35ODEhaoMEC0x-SWpiyIVd8Y2aNC2_r4EYOjRxskecxrfINCaFZWMW0IMaJv5fNdefM4UyFDUtnjK7DZdIt0DhIaUTDE4Cw-6J7y0tGLdrwAjaO0qzRQKSDWjZU-BipvI380We5eFfyuHQjG6z4qQybKoM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/89d69f232e.mp4?token=PxU4G4zk3ymNZc4QDXtul76hJReqQ32YorT2N6jhtNw0XErIqrlF9o-uKd1H0WZb5Fo3UspL-oFD4pcPNJJnul1QegQsfp-gYN0wavS5txzBQoPRg7JX0o2tDuG8daMwPpDzjdMJxA66iUbDSRCFqvGk1mylEv5SLD_Jn1kJWCFJfFgMih1PwVF8RA3wLwyqXP1Sc6Y8zlz4LVBEwYMBKua6a_hYMZwyhX7z63SJhS3n-HfwbFrNEg0TBzHnS0nSUvdirN-bitblJ170yBKwlG-1I6Z2OmEWeV_je3A5CzsHhmSgSQs3C2bRmLv7BA_2rPeT3_TeTzUADkWXyY2svkvOUa2nismFFSmskKXPLcZEKkxfimWW6oR7L7w8_IZn8wwjT2QIJ3k9j38yHa6tCnX8Ji3X6ffYXaGj8xKQemlKB2Z_G7cERld135mnJyCzgMoie8o-kr2QgB0sfSWJPCHxOd5kERaenzaGlc7QvCOw89uYzLxwMCEHE15pjZUnefAvMVEQDDDxr_MvC35ODEhaoMEC0x-SWpiyIVd8Y2aNC2_r4EYOjRxskecxrfINCaFZWMW0IMaJv5fNdefM4UyFDUtnjK7DZdIt0DhIaUTDE4Cw-6J7y0tGLdrwAjaO0qzRQKSDWjZU-BipvI380We5eFfyuHQjG6z4qQybKoM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ به فاکس‌نیوز : ایران در حال تغییر موضع است، در حالی که دولت او خود را برای اعمال موج جدیدی از فشارهای اقتصادی بر تهران آماده می‌کند.
آنها اکنون در حال تغییر موضع هستند، زیرا وقتی کشوری دیگر نیروی دریایی و هوایی ندارد، حرف چندانی برای گفتن ندارد.» او افزود که «نمی‌دانم اصلاً با چه کسی باید مذاکره کنم.»
@WarRoom</div>
<div class="tg-footer">👁️ 102K · <a href="https://t.me/withyashar/21334" target="_blank">📅 17:51 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21333">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">اکسیوس به نقل از مقامات آمریکایی:
حدود 40 تانکر نفت شب جمعه از تنگه هرمز، به سمت مسیر عمان و مسیر آمریکایی، عبور کردند. این میزان معادل حدود 16 میلیون بشکه نفت است.
@WarRoom</div>
<div class="tg-footer">👁️ 101K · <a href="https://t.me/withyashar/21333" target="_blank">📅 17:26 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21332">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">روزنامه معاریو: آلون بن داوید، خبرنگار مسائل نظامی این روزنامه، مدعی است که مقامات ارشد ارتش دفاعی اسرائیل  معتقدند که نخست‌وزیر نتانیاهو در تلاش است تا تنش‌ها را در غزه افزایش دهد تا انتخابات اکتبر را به تعویق بیندازد.مقامات ارتش اسرائیل گفته‌اند که نمی‌خواهند وارد یک جنگ جدید و غیرضروری شوند
@WarRoom</div>
<div class="tg-footer">👁️ 105K · <a href="https://t.me/withyashar/21332" target="_blank">📅 16:08 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21331">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lpIVaOOU5vYn6JxQdYnB43cuDNiWhYE_yHgEPb451M5JUiwNMsTQ5vr0wT-kXYiqoigRewlJzhNp8Nml0WV9muq_CHem3l-vsSIbNRYoie4HW-l6T_SLECNnfm1T3LKrzdpoVNeikECFM0mQS-qbzRvVTS350E8BqC-_7tJr8eGU1ZBJVpRRHcp3bnCYVEJ6x_5Cm-EvfL4QQUOkHHYvAsz_ojKDBfAnS_nFbH2hvK8Bw7BH9R-wPLXDCnrfv57dLVyWCV8PKSPM9qI_D713rr_fe8r6QIeGNSQfF_dWqlk-SctVbdXbKnEMGf1-AjgDLXakJnTJ2NNYbxD53KUNrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امروز صبح انتقال سه تانک از کمربندی یزد بسمت جنوب کشور
@WarRoom</div>
<div class="tg-footer">👁️ 116K · <a href="https://t.me/withyashar/21331" target="_blank">📅 12:53 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21330">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">رویترز : آمریکا روز دوشنبه تحریم‌های اقتصادی جدیدی علیه ایران اعلام می‌کند که احتمالاً خریداران بزرگ نفت ایران، از جمله شرکت‌های چینی، را نیز هدف قرار خواهد داد
@WarRoom</div>
<div class="tg-footer">👁️ 112K · <a href="https://t.me/withyashar/21330" target="_blank">📅 12:46 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21329">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qKnWTBCirpuSDjaGyVZWgEWOIah1xKNfqE18V4XJ44om26AefjcoL_skcraTj4fFs8T6p7XWfbANKCbHlCd4tUdAZRYFYA6oqWluzFhPV0dnriTGxNZxxjcZY9XbO3KTb95_oi-si8I--26hwDz3YjHsjGYZTOJJpYxzdiMm_8sh8gvHeqS9BUiBt4q7VX5Goq3Tc_yLXqaicW5GpYEz4XAtuK8nQGbPAyBuqr4EV4rVYppP1KUagIlOawXTi0-QFMZmRten0Ij-2GWFHl5_gBNvxwrXmNSPVHgsahMJFKzaVtg-QaRyVknRH0TRiTzLN2leVc615o5uV18ue48R6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">lكارنامه شاهزاده رضا پهلوی ، كتبى ١٨.٠٤ و معدل شفاهى ١٨.٧٢ ، انضباط ١٨!
@WarRoom</div>
<div class="tg-footer">👁️ 116K · <a href="https://t.me/withyashar/21329" target="_blank">📅 11:41 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21328">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EvWNHIM20BYV4FwigY12HUk_ekDJFSzeOdL3RCQFS5GsC908x4TuVd8YF9bClaykrjW5F2o1Hgx2p0nnEQlWIvstB8DDgu-KdHou7thotgtR0sUNSvSkQGl11TsqA8-XI6SQ-I4YYmL1gJMHxUB_hYxo2E_8fq1MLNrXTwlTTiaVMCU0_6wDgtpn9cnLmBUqqmC8SSjOqZCqSk8X1NbH_9Y7TdhPRP561TRgeJ7h3M27udFn6lzPwVI7KIONkrL4u7eaP_58tFmNRw2Befhw_OqPi2Vlz10rb3j6_iCXXzr8GbJys5nW3H-eh6JEr4PRXpbMwtVoIjEM1G8QYRD82A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک تانکر نفتی، با نام "ال ماقام"، شب گذشته تحت نظارت هوایی شدید نیروهای آمریکایی با موفقیت از تنگه هرمز عبور کرد، در حالی که سیستم AIS آن غیرفعال بود.
@WarRoom</div>
<div class="tg-footer">👁️ 113K · <a href="https://t.me/withyashar/21328" target="_blank">📅 11:38 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21327">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">یاشار : کتاب اوستا ، یسنا ۴۳.۱ آمده:
«اُشتا اَهمایی یَهمایی اُشتا کَهمایچیت»
«خوشبختی نصیب کسی می‌شود که برای دیگران خوشبختی بخواهد.»
@WarRoom</div>
<div class="tg-footer">👁️ 111K · <a href="https://t.me/withyashar/21327" target="_blank">📅 11:09 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21326">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">تابناک : گویا راه حل چهارمی برای بنزین پیدا کردن!
کیفیتو انقدر پایین آوردن که مردم از ترس خراب شدن ماشینشون دیگه بنزین نزنن… دولت با همین ترفند ساده، مصرف رو کنترل کرد.
@WarRoom</div>
<div class="tg-footer">👁️ 115K · <a href="https://t.me/withyashar/21326" target="_blank">📅 10:25 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21325">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">مدیرعامل شرکت نفـت ستاره خلیـج فارس استفاده از متانول در ترکیب بنزین این پالایشگاه را تایید کرد.
انجمن خودروسـازان ایران پیش از این در نامه‌ای هشدار داده بود که استفاده از متـانول در بنزین سیستم سوخت رسانی، باک، فیلتر و پمپ بنزین، لوله های فلزی، واشرها و قطعات پلاستیکی را دچار خوردگی شدید می‌کند.
مدیرعامل شرکت نفت ستاره خلیج فارس: استفاده از متانول در سوخت در کشورهایی مانند چین، آمریکا و اروپا تجربه شده و این ترکیب هیچ آسیبی به خودرو وارد نمی‌کند
@WarRoom</div>
<div class="tg-footer">👁️ 116K · <a href="https://t.me/withyashar/21325" target="_blank">📅 10:13 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21324">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">آمریکا و کانادا در تلاش خود برای دستیابی به توافق تجاری شکست خوردند و به همین دلیل واشنگتن از صبح امروز، 50 درصد تعرفه بر محصولات کانادایی به ارزش حدود 20 میلیارد دلار اعمال کرد. مارک کارنی، نخست وزیر کانادا، در پاسخ به این اقدام، تعلیق مذاکرات با آمریکا را اعلام کرد و گفت که کشورش به تعرفه‌های جدید «دلار در برابر دلار» پاسخ خواهد داد. این تصمیم پس از سه روز مذاکره متوالی در واشنگتن بین دومینیک لبلانک، وزیر کانادا، و جیمیسون گریر، نماینده تجاری ایالات متحده انجام شد ، تعرفه‌ها بر محصولاتی اعمال خواهد شد که حدود 5 درصد از صادرات کانادا به ایالات متحده را تشکیل می‌دهند.
@WarRoom</div>
<div class="tg-footer">👁️ 114K · <a href="https://t.me/withyashar/21324" target="_blank">📅 10:01 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21323">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">پاکستان برای هزینه میانجیگری بین ایران و امریکا ‌۱۰ میلیارد دلار درخواست کرد
@WarRoom</div>
<div class="tg-footer">👁️ 114K · <a href="https://t.me/withyashar/21323" target="_blank">📅 09:51 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21322">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4a8d76ce15.mp4?token=kkTbAGEEezKlCsPDbH6VhCTwaTxqgj71uQRA0pI3LMAOks2dag8VKloinbl3fXXfiV9r8MhU1r8E6yJoiOknBq6uHML4JSZ3vHYznrnCBehma-ovT039AhnQ7sLQH82hEFnBE9KlmC2LfAWFjuZtLUwbtNBviPMwp1NwdPLHxSrwD1Wi7e0jImDB0hUQlTo4Emi57qszoO1MLy6PZk0JzYN_wMFqtg063Ln8rsmOrlTcLq3h2T0jw6A7rz-znegc-hKXt9xorppn2vSRQ4vRb8eRtpT4mY3GP6gI-iEj540oL_u-WLe8-3vGFs26hd6nAAP8n_twKbS7UttPiwLbSw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4a8d76ce15.mp4?token=kkTbAGEEezKlCsPDbH6VhCTwaTxqgj71uQRA0pI3LMAOks2dag8VKloinbl3fXXfiV9r8MhU1r8E6yJoiOknBq6uHML4JSZ3vHYznrnCBehma-ovT039AhnQ7sLQH82hEFnBE9KlmC2LfAWFjuZtLUwbtNBviPMwp1NwdPLHxSrwD1Wi7e0jImDB0hUQlTo4Emi57qszoO1MLy6PZk0JzYN_wMFqtg063Ln8rsmOrlTcLq3h2T0jw6A7rz-znegc-hKXt9xorppn2vSRQ4vRb8eRtpT4mY3GP6gI-iEj540oL_u-WLe8-3vGFs26hd6nAAP8n_twKbS7UttPiwLbSw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رئیس جمهور ترامپ در مورد ایران:
ما مجبور بودیم سلاح هسته‌ای را از ایران بگیریم. ما مجبور بودیم این کار را انجام دهیم.
این باعث افزایش ناگهانی قیمت نفت شد، نه به آن بزرگی که مردم فکر می‌کردند، اما باعث افزایش ناگهانی قیمت نفت شد. قیمت‌ها خیلی زود حتی از قبل هم پایین‌تر خواهند آمد.
@WarRoom</div>
<div class="tg-footer">👁️ 114K · <a href="https://t.me/withyashar/21322" target="_blank">📅 09:22 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21321">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/db5a0b2336.mp4?token=E-EM9KVuDwAVmXAD7xCO5ixqbXMKqBuJepOuQvl4qyznR524DnF_5Ah3q9RkD37Ak-96oRmJg3mqreZSp6F2NXdEXZ0koDMp_JZa0kVMD-Y85MqPYsrZKCKbDj3Ud1fkZfWHvwjkP5UEphNYxXt3Dq6zzL_cqAVUZ9vxHcobkTitdgEh9I-NSMX2nASXhgYRQL2yp8r4BWg4CiSBbOnHK1XEYPatu5bRrZwSW8awO9nJdq0NtCZkhSECqJ_zhicYfYVHFlB6MuZPGLKgl1RQhz_sw_IUHIsRdKhKTbNgoueNGOkAdqSkmjV_Fb0Gqs353vbVs4tdVNqCgYZg7SmayA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/db5a0b2336.mp4?token=E-EM9KVuDwAVmXAD7xCO5ixqbXMKqBuJepOuQvl4qyznR524DnF_5Ah3q9RkD37Ak-96oRmJg3mqreZSp6F2NXdEXZ0koDMp_JZa0kVMD-Y85MqPYsrZKCKbDj3Ud1fkZfWHvwjkP5UEphNYxXt3Dq6zzL_cqAVUZ9vxHcobkTitdgEh9I-NSMX2nASXhgYRQL2yp8r4BWg4CiSBbOnHK1XEYPatu5bRrZwSW8awO9nJdq0NtCZkhSECqJ_zhicYfYVHFlB6MuZPGLKgl1RQhz_sw_IUHIsRdKhKTbNgoueNGOkAdqSkmjV_Fb0Gqs353vbVs4tdVNqCgYZg7SmayA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ: الان میگین چه غلطی باید بکنم؟
برگردم، کمی بیشتر ایران را بمباران کنم؟
جمعیت : آررررررررره
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 123K · <a href="https://t.me/withyashar/21321" target="_blank">📅 03:41 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21320">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3e05213aef.mp4?token=NvakRGOp3ypTehXSAIHcO4OE4x9rsvyPVkcvJr54JYrJ_OJzQZMa0dJoAfy6FyL-Mn4Ca0KYCw8HXVXLvNgP0dcD0mzFDw3G6JSRPOn1UYjwUZy4biQJzdg9vZjupUsmIxgoMw-p93RfKP9zzTc5KFAx6sGc8QObWE-o5prXfvBNJnpJX_HFmghwOZwMAlnHqEaCpGQRmuU_QusjfIw5S-nJUsxvi0ArGBSHqQ-Zs3PAnyas3F7RwZjZUDjxcqOgrgA2yLRmwS0LMV2DRGCxnOZivixoZM_rl_i_brfUMCavMGv8OpXQFaQbCBlk5m8UrTh-Jb1hrOLmDahGTJFhmg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3e05213aef.mp4?token=NvakRGOp3ypTehXSAIHcO4OE4x9rsvyPVkcvJr54JYrJ_OJzQZMa0dJoAfy6FyL-Mn4Ca0KYCw8HXVXLvNgP0dcD0mzFDw3G6JSRPOn1UYjwUZy4biQJzdg9vZjupUsmIxgoMw-p93RfKP9zzTc5KFAx6sGc8QObWE-o5prXfvBNJnpJX_HFmghwOZwMAlnHqEaCpGQRmuU_QusjfIw5S-nJUsxvi0ArGBSHqQ-Zs3PAnyas3F7RwZjZUDjxcqOgrgA2yLRmwS0LMV2DRGCxnOZivixoZM_rl_i_brfUMCavMGv8OpXQFaQbCBlk5m8UrTh-Jb1hrOLmDahGTJFhmg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره ایران:
آن بمب‌افکن‌های B-2 یک سال پیش به امید ایران برای دستیابی به سلاح هسته‌ای پایان دادند.
@WarRoom</div>
<div class="tg-footer">👁️ 119K · <a href="https://t.me/withyashar/21320" target="_blank">📅 03:26 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21319">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d33aa06c32.mp4?token=F0zmX0MpjPKR73PenA4h2C-qmVrBBVS7DofWt12ShOO1RdBDMlGuU6xfVcdLc_z_OVG1K0dbgNsIfqyLhJun2FsaDH3eFRKIJ4fiR4bJhRiZ6Z3JTB1J6hnfYA_r2mzTpH1TPSAgPuSZWqHxGHx7JKNwxUZDSXMnQ39niL8MSEq3IF3G_k1y8R_3omK7PLtYla-wk5zdXmwSzHYVdYQAHRIu46uQC3BQHOUq3UIOo-PRhZPOB6wWtW85vlC6P9aTyhhCGQxxFvrxXgntFnDuwnHr1IOn3flhO4sORZuX0zm5-oKsytTuXcNPKqhikX-hMn_l4oxiDIE_1p3mEYfqww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d33aa06c32.mp4?token=F0zmX0MpjPKR73PenA4h2C-qmVrBBVS7DofWt12ShOO1RdBDMlGuU6xfVcdLc_z_OVG1K0dbgNsIfqyLhJun2FsaDH3eFRKIJ4fiR4bJhRiZ6Z3JTB1J6hnfYA_r2mzTpH1TPSAgPuSZWqHxGHx7JKNwxUZDSXMnQ39niL8MSEq3IF3G_k1y8R_3omK7PLtYla-wk5zdXmwSzHYVdYQAHRIu46uQC3BQHOUq3UIOo-PRhZPOB6wWtW85vlC6P9aTyhhCGQxxFvrxXgntFnDuwnHr1IOn3flhO4sORZuX0zm5-oKsytTuXcNPKqhikX-hMn_l4oxiDIE_1p3mEYfqww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ: اگر من در انتخابات میان دوره ای شکست بخوریم، استیضاح می شوم.
قرار است من را استیضاح کنند. آنها خودشان هم نمیدانند چرا.‌‌
@WarRoom</div>
<div class="tg-footer">👁️ 119K · <a href="https://t.me/withyashar/21319" target="_blank">📅 03:15 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21318">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5060626161.mp4?token=Wyp84fYC3DbJtbyYiKfL_ZUWQrPvy_KGuRq9FmQ4NU_38qQx-L0EDAm1RhIOIHbLjcsgrgD-63A7vn5H4OO51yBOF0Z6Yyp-sCMe1Sg1c3xeSNzNVjpOGS-oAdN-hds4hMIkMqhoHm8lEpHRT44MOVP9cmyW6FdizMS40TyQGO8LHMRw4rgLllV_nTpB2HtRputBlhYoMLFi9i2vJQAVpOZvk6Qx4iTRg8kPyu-C4oV4F0Yg8SxEU5-E4T4vo0RlvHZmQ-Mi-McUJAz9IgjFaE7K7ceQ8hMyy7D3lrZjH2jLkt8vp-TEB7TiQ910rLV1_BQ5qMtSq6SIpveKG7wHzA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5060626161.mp4?token=Wyp84fYC3DbJtbyYiKfL_ZUWQrPvy_KGuRq9FmQ4NU_38qQx-L0EDAm1RhIOIHbLjcsgrgD-63A7vn5H4OO51yBOF0Z6Yyp-sCMe1Sg1c3xeSNzNVjpOGS-oAdN-hds4hMIkMqhoHm8lEpHRT44MOVP9cmyW6FdizMS40TyQGO8LHMRw4rgLllV_nTpB2HtRputBlhYoMLFi9i2vJQAVpOZvk6Qx4iTRg8kPyu-C4oV4F0Yg8SxEU5-E4T4vo0RlvHZmQ-Mi-McUJAz9IgjFaE7K7ceQ8hMyy7D3lrZjH2jLkt8vp-TEB7TiQ910rLV1_BQ5qMtSq6SIpveKG7wHzA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره ایران:
این در واقع یکی از بزرگترین مشکلات من است: نمی دانم با چه کسی در ایران برخورد کنم.
این تنها کشوری در جهان است که هیچ کس نمی خواهد رئیس جمهور شود.
آنها می گویند: "چه کسی می خواهد رئیس جمهور شود؟" نه، نه، من نمی خواهم رئیس جمهور شوم.»‌‌
@WarRoom</div>
<div class="tg-footer">👁️ 117K · <a href="https://t.me/withyashar/21318" target="_blank">📅 03:14 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21317">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">این خواهر پژی جمشیدی چه بی لولیه بی حیا دو زاری ، من ۹۹٪ فوتبالیستایی که دیدم دوزاری بودن ! این جماعت چرا اینجورین !</div>
<div class="tg-footer">👁️ 114K · <a href="https://t.me/withyashar/21317" target="_blank">📅 03:03 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21316">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">سنت‌کام : نیروهای ایالات متحده از زمان تقویت محاصره بنادر ایران، ۶۷ کشتی تجاری را تغییر مسیر داده‌اند، ۳ کشتی را غیرفعال کرده‌اند و ۲ کشتی را برای اطمینان از رعایت مقررات به بازجویی و بازرسی برده‌اند. @WarRoom</div>
<div class="tg-footer">👁️ 116K · <a href="https://t.me/withyashar/21316" target="_blank">📅 02:48 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21315">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">تکزاس زیر 1942 و Azul قبول نیستاااا</div>
<div class="tg-footer">👁️ 118K · <a href="https://t.me/withyashar/21315" target="_blank">📅 02:17 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21314">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromJoshua Milani</strong></div>
<div class="tg-text">داش یاشار از کف تکزاس با تکیلااااا جات خالی</div>
<div class="tg-footer">👁️ 118K · <a href="https://t.me/withyashar/21314" target="_blank">📅 02:16 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21313">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QtJXWs_2SZz7DCte3Z77UqFN7xG4ysfzvOzssSqEBveGcRUkPNs2JNeGgH6vHfmOpx-15dODJ7BM91nLLV_Q-F-wDBTTzV30UdovkJNt8XN6gPAuaAvCwLEfq2JrxtMUta1bLU5QvoUcp4pzUxasJKsJqZi3K_1uMF7gsAnhOiO6HLXQ0sjWPTFT88eGYqVnQMvtUcy3ZqWcQSVfL9m4zXi8folR-Ggk46hw574XrQse7F_KyUP27Z43gWy-9JHA3XZLufY-V2ApMK1l7bDHn-7gEvlMEqays1ZdM5ymxO8lHe43rBcMSHxMqS8CxSRDK6s4-FkhMUoJLlwLCzGaSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تنگه شلوغ شد
🚨
🚨
🚨
@WarRoom</div>
<div class="tg-footer">👁️ 120K · <a href="https://t.me/withyashar/21313" target="_blank">📅 02:07 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21312">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">جنگی
⚔️
⚔️
⚔️</div>
<div class="tg-footer">👁️ 114K · <a href="https://t.me/withyashar/21312" target="_blank">📅 02:01 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21311">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBaba barghi</strong></div>
<div class="tg-text">اقا یاشار گل مرد مردا
مارو از جنی واکرا بینصیب نکن مشتی
کاکو شیراز یه لشکری هوادارتن
🫡
🫡
🫡</div>
<div class="tg-footer">👁️ 117K · <a href="https://t.me/withyashar/21311" target="_blank">📅 02:00 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21310">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from؛)</strong></div>
<div class="tg-text">یاشار ماهم داریم راکی میخوریم از غرب تهران مستیم مستت
🥃</div>
<div class="tg-footer">👁️ 120K · <a href="https://t.me/withyashar/21310" target="_blank">📅 02:00 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21309">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">اتاق جنگ با یاشار : اول از همه باید به تغییر رژیم در افکار بوجود بیاد ، بعد اینام میرن ..</div>
<div class="tg-footer">👁️ 118K · <a href="https://t.me/withyashar/21309" target="_blank">📅 01:58 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21308">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-footer">👁️ 119K · <a href="https://t.me/withyashar/21308" target="_blank">📅 01:52 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21307">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">۲ ساعت دیگه میرم بالای منبر اگه بیدارین
😎</div>
<div class="tg-footer">👁️ 120K · <a href="https://t.me/withyashar/21307" target="_blank">📅 00:58 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21306">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Nznd0hdd6-g76KFsXzxbHNvitOyDceLlm9PVm24YlIz1GCy25Wlfh__oW_FFqI--Jw1SSJzVgeVG-C1n0lvmFcVr-iJE_7AeQ5ns8ydHvHrpAscCOZ3USbDLyyr_XHh-fKkrbzSWvnBLwobZ3YXWlPk8au760Xjny1c2ADA6QIAah4_mgmajcnqGjAFYXooX8opusnQDqY4_2EXGj9feKkhptrye40lcmL5ZIgnmPZt2bPh_c3KSLcttjdQBx_ik8xp8U-DfFaBQaIPlR5GvLa05mewaMu0qHpJK7SLkT2mjD_C6h06JC6-Fma4FTXFB1Ia20oE456F4hV3NriH3Yg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دقایقی پیش، یک جت جنگنده F-35A Lightning II نیروی هوایی ایالات متحده هنگام فرود اضطراری کد اضطراری ۷۷۰۰  اعلام کرد…
@WarRoom</div>
<div class="tg-footer">👁️ 124K · <a href="https://t.me/withyashar/21306" target="_blank">📅 00:43 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21305">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a6b4cd2471.mp4?token=RhAGRWnSmY27oxSgoNrftPkFT5bCOSrrxjDt8m-nhltV62QWIjytd8cU9wKecVlWUoS_AbWWoSTztUiQCGR8tUY5FbZD5tGTIoWAsun1dASIaz3Md1qvjsIupHt2TX9SAI0rrUseesy0m0AD13ZvYFEARtzQVAHL3fr08qL_yUe14rqpuAyaNbN3i-sA5TZvjPkG9U-zU4_IeCmoPFAYF17M29JQ3vIFCyMOe6BCZVlgndSUw-U1h13I2XNBXfoOPjlL-oHF_IcS9zs6wGa4kiK7y26FX3GSWsOxEICl2zjUdxwypD6kX4-wbr63JmMfUqPuZZJla1BlMHHzy9R73g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a6b4cd2471.mp4?token=RhAGRWnSmY27oxSgoNrftPkFT5bCOSrrxjDt8m-nhltV62QWIjytd8cU9wKecVlWUoS_AbWWoSTztUiQCGR8tUY5FbZD5tGTIoWAsun1dASIaz3Md1qvjsIupHt2TX9SAI0rrUseesy0m0AD13ZvYFEARtzQVAHL3fr08qL_yUe14rqpuAyaNbN3i-sA5TZvjPkG9U-zU4_IeCmoPFAYF17M29JQ3vIFCyMOe6BCZVlgndSUw-U1h13I2XNBXfoOPjlL-oHF_IcS9zs6wGa4kiK7y26FX3GSWsOxEICl2zjUdxwypD6kX4-wbr63JmMfUqPuZZJla1BlMHHzy9R73g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرنگار: درباره حرکت ایران به سمت
جنگ اقتصادی
؛ آیا این به این معناست که گزینه‌های نظامی آمریکا محدود شده‌اند؟
ترامپ:
نه، به هیچ‌وجه.
ما
کنترل کامل بر تمام آن منطقه مرتبط با تنگه هرمز
داریم؛ و منظورم حتی مناطق خشکی در داخل آن محدوده هم هست.
آن‌ها بسیار مایل‌اند به توافق برسند، اما به نظر من هنوز آماده پذیرش
توافق درست
نیستند.
من فقط توافق‌های خوب (تسلیم کامل )انجام می‌دهم.
@WarRoom</div>
<div class="tg-footer">👁️ 117K · <a href="https://t.me/withyashar/21305" target="_blank">📅 00:35 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21304">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">تنگه دعوا شده ، گزارش چند صدای انفجار / شلیک از غرب جاسک
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 115K · <a href="https://t.me/withyashar/21304" target="_blank">📅 00:18 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21303">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e56ecd2c26.mp4?token=rdhMGafiPuiJc8l8NrCXKzUow-NSBDEIrtTqGo4n73gUlzH30E6tFNhalarBSO-f7_K4DA7R-rCk085O8MSXN7lhjuZwotYhVQDn89vw3miTV99x61cDoIjDOQne5YpFpzXuewnTj4zG9VxEhiQL2CSGuAnH5BzpxlTeG3k_xGSqJylCCxt5Ggt85fldWFPl0flF0Vo9ZVtmHQ7zX76a1Ot9ammzNpCvyd0AptYvhRfHACGsspROAoMDj4kM9caYWXVECE8f4DsjGCTctCQMIBJbA89gFQs-RuHsn0g7Kivj3_m1hniFe1MZriNn2eVN-7YskeU6Q8jjmbIMIcwY5Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e56ecd2c26.mp4?token=rdhMGafiPuiJc8l8NrCXKzUow-NSBDEIrtTqGo4n73gUlzH30E6tFNhalarBSO-f7_K4DA7R-rCk085O8MSXN7lhjuZwotYhVQDn89vw3miTV99x61cDoIjDOQne5YpFpzXuewnTj4zG9VxEhiQL2CSGuAnH5BzpxlTeG3k_xGSqJylCCxt5Ggt85fldWFPl0flF0Vo9ZVtmHQ7zX76a1Ot9ammzNpCvyd0AptYvhRfHACGsspROAoMDj4kM9caYWXVECE8f4DsjGCTctCQMIBJbA89gFQs-RuHsn0g7Kivj3_m1hniFe1MZriNn2eVN-7YskeU6Q8jjmbIMIcwY5Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 117K · <a href="https://t.me/withyashar/21303" target="_blank">📅 00:16 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21302">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3b84ef4f3f.mp4?token=R9oqXd5A0_h5DkoAf3d9paweK7h4ASAaFrOj9eIkHtnESG5mskPQka1iym0P2sW0g3R5UhpZmfnghubI3bjkAGnYRZN10XehU7U7csEh-_tYFx-WDh-Z3J8DrOFmqONqLOSpCgzC_LKYJCQKVdA9cBYnD1CC47jKXbzpj5rGGZOmCoWZliVCqBGbudOHkeAR164__b_hDW5MKjn0F8Tg08E3rNan_8_XcwxTmp0woiMWkjdMNZt6N5jO_Af1iAUGuZEO8iVbokI0nxXxjKL-jb-opV1CKMvpVSCe2kQGoeCjJXl8ycyXyK_Rq087JLlomlZ93cCmNhSLgxaqmjkwnw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3b84ef4f3f.mp4?token=R9oqXd5A0_h5DkoAf3d9paweK7h4ASAaFrOj9eIkHtnESG5mskPQka1iym0P2sW0g3R5UhpZmfnghubI3bjkAGnYRZN10XehU7U7csEh-_tYFx-WDh-Z3J8DrOFmqONqLOSpCgzC_LKYJCQKVdA9cBYnD1CC47jKXbzpj5rGGZOmCoWZliVCqBGbudOHkeAR164__b_hDW5MKjn0F8Tg08E3rNan_8_XcwxTmp0woiMWkjdMNZt6N5jO_Af1iAUGuZEO8iVbokI0nxXxjKL-jb-opV1CKMvpVSCe2kQGoeCjJXl8ycyXyK_Rq087JLlomlZ93cCmNhSLgxaqmjkwnw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فرماندهی مرکزی ایالات متحده، تصاویری را منتشر کرده است که نشان می‌دهد جنگنده‌های F/A-18E و F/A-18F Super Hornet همچنین E/A18 Growler نیروی دریایی ایالات متحده، که بر روی ناو هواپیمابر کلاس نیمیتز به نام USS George Washington در دریای مکران مستقر هستند، در حال آماده‌سازی برای انجام عملیات‌های شبانه هستند
@WarRoom</div>
<div class="tg-footer">👁️ 120K · <a href="https://t.me/withyashar/21302" target="_blank">📅 00:11 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21301">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">خبرگزاری فارس در یادداشتی با انتقاد از صحبت پزشکیان درمورد لزوم پایان جنگ نوشت: ایران جنگ را آغاز نکرده که پایان دادنش با ایران باشد!
@WarRoom</div>
<div class="tg-footer">👁️ 118K · <a href="https://t.me/withyashar/21301" target="_blank">📅 00:00 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21300">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">رویترز : فرسودگی پایانه‌های نفتی ونزوئلا نفتکش‌ها را تا یک ماه معطل می‌کند
پایانه‌های فرسوده بنادر نفتی ونزوئلا عملاً باعث محدودیت صادرات نفت خام این کشور شده‌اند و نفتکش‌ها به دلیل زیرساخت‌های فرسوده، قطعی برق و مشکلات کیفی، مجبورند تا ۳۰ روز برای بارگیری منتظر بمانند.
@WarRoom</div>
<div class="tg-footer">👁️ 122K · <a href="https://t.me/withyashar/21300" target="_blank">📅 23:37 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21299">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">همکنون
موج شدیدحمله هوایی اسرائیل و بمباران در جنوب لبنان کوه علی الطاهر
@WarRoom</div>
<div class="tg-footer">👁️ 121K · <a href="https://t.me/withyashar/21299" target="_blank">📅 23:35 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21298">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">شما هر صدای که بگی‌ در تهران داره گزارش میشه
🤠
@WarRoom</div>
<div class="tg-footer">👁️ 122K · <a href="https://t.me/withyashar/21298" target="_blank">📅 23:28 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21297">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">به گزارش گاردین ترامپ برای هرگونه اقدام اقتصادی جدید علیه ایران، ناگزیر خواهد شد شرکای تجاری ایران، به‌ویژه چین، را هدف قرار دهد؛ همین مسئله رویکرد آمریکا را دشوار می‌کند
سفر رئیس‌جمهور چین به آمریکا در ماه آینده نیز ممکن است تلاش‌ها برای اعمال فشار بر پکن درباره واردات نفت ایران را پیچیده‌تر کند
@WarRoom</div>
<div class="tg-footer">👁️ 123K · <a href="https://t.me/withyashar/21297" target="_blank">📅 23:15 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21296">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">چند گزارش از صدای تیراندازی در غرب تهران
@WarRoom</div>
<div class="tg-footer">👁️ 125K · <a href="https://t.me/withyashar/21296" target="_blank">📅 22:39 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21295">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">جی دی
ونس به اسکای نیوز : حضور ارتش آمریکا در خاورمیانه ادامه دارد!
واشنگتن ابزارهای فشار لازم برای مقابله با ایران را دارد
@WarRoom</div>
<div class="tg-footer">👁️ 125K · <a href="https://t.me/withyashar/21295" target="_blank">📅 21:53 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21294">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fbc6763df7.mp4?token=pd76uzLtHo0hozBof6oGoYQu9BVOxzpFCXF8IMGNBuClDuOwSLcHowj62Vn5oagqnj3d5R_FmqOdvEemKKMzcfv8HUsIAQTsjHqE2VP_ubyAgr7xuHqaCx0bdCRJUjEeBLEIDCFzAt75hBMyyurPqK4CCowCC3SVgbWyrk1Rr8JOwaPW0e8oHXqmX4RkXsPUuSvnwxI0FtbzK5P843pF0bzTqY9EYB2MWj1cw78RzW6jcNo_F6qIUE6nWHbUiPr6mjcWeV7vYYzf_u3jj28wdmBHmCmBjiwQEcjUR9C5VLlkQ3ACELIXoLBfqapsLbMaF4xTvUrZsDK-M5JF949LRA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fbc6763df7.mp4?token=pd76uzLtHo0hozBof6oGoYQu9BVOxzpFCXF8IMGNBuClDuOwSLcHowj62Vn5oagqnj3d5R_FmqOdvEemKKMzcfv8HUsIAQTsjHqE2VP_ubyAgr7xuHqaCx0bdCRJUjEeBLEIDCFzAt75hBMyyurPqK4CCowCC3SVgbWyrk1Rr8JOwaPW0e8oHXqmX4RkXsPUuSvnwxI0FtbzK5P843pF0bzTqY9EYB2MWj1cw78RzW6jcNo_F6qIUE6nWHbUiPr6mjcWeV7vYYzf_u3jj28wdmBHmCmBjiwQEcjUR9C5VLlkQ3ACELIXoLBfqapsLbMaF4xTvUrZsDK-M5JF949LRA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پشت صحنه فوتوشوت از ترامپ
@WarRoom
😁</div>
<div class="tg-footer">👁️ 126K · <a href="https://t.me/withyashar/21294" target="_blank">📅 21:39 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21293">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nBIRDCJvPk_hJX1fdhN2zeEuGp0rg_YQD5ZhueJ3NfWwbTFbrAEmDyMa9U6PT_FzOr082EDcs7dJGSIfwEA1579Mnr_gYwLMb_W6W00m9kxWjU6Fd5iPuvcf7O9oXQD6yQq5nNeN-DVf3AgVYpFM2ZEdK5gTPZxB_MMOwL-bjZhkRaancRHWxxDaGTidkVDE19mITSWb5R5vwBGrg48flned_r8v1bpcShwU3WuxE9HTNoxxQ7P_SerUIeuo0q-ALjH8xM-nVj_xfsDmFkWlRL_DDCqggycef1LaydIT7MEEfKY7BLm1YqfS_pSHF7ehYrA8y7FoEPtsUrWKeERZSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در تروث این مقاله را بازنشر کرد :
ترامپ از فشار همه‌جانبه بر ایران می‌گوید: «الحمدلله!»
دونالد ترامپ مدعی شد آمریکا
کنترل کامل تنگه هرمز
را در دست دارد و محاصره دریایی این کشور به یک «
دیوار فولادی
» تبدیل شده است. او گفت ایران دیگر
نیروی دریایی و نیروی هوایی مؤثری ندارد، بخشی از نیروهایش حقوق نمی‌گیرند، سپاه پاسداران به‌شدت تضعیف شده و در حال فرار است
و رهبری جمهوری اسلامی نیز در وضعیت نامشخصی قرار دارد. ترامپ همچنین از
بی‌پولی و تورم ۳۰۰ درصدی
ایران گفت و مدعی شد جمهوری اسلامی دیگر «قلدر خاورمیانه» نیست و فقط حرف می‌زند. او تأکید کرد
آخرین کسی است که به ایران اعتماد می‌کند
و گفت اگر ایران اقدامی انجام دهد، با واکنش بسیار شدید آمریکا روبه‌رو خواهد شد. ترامپ در پایان گفت آمریکا اکنون در
«موقعیت بسیار خوبی»
قرار دارد و ایران پس از حدود ۵۰ سال دیگر «قلدر خاورمیانه» نیست و پیام خود را با عبارت
«الحمدلله!»
به پایان رساند.
@WarRoom</div>
<div class="tg-footer">👁️ 124K · <a href="https://t.me/withyashar/21293" target="_blank">📅 20:44 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21292">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">رئیس کمیسیون امنیت ملی مجلس:
به زودی با قدرت به محاصره دریایی آمریکا علیه ایران پاسخ خواهیم داد و آمریکا منطقه را ترک خواهد کرد.
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 119K · <a href="https://t.me/withyashar/21292" target="_blank">📅 19:53 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21291">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">آکسیوس:
بازار نفت دیگر صرفاً با تهدید، وعده یا پست ترامپ معامله نمی‌کند؛
واقعیت میدانی تنگه هرمز، میزان واقعی اختلال در صادرات و عبور نفتکش‌ها اکنون تعیین‌کننده‌تر شده‌اند.
این موضوع همچنین برای ترامپ از نظر سیاسی اهمیت دارد، چون کاهش واکنش بازار به اظهاراتش می‌تواند توان او برای تأثیرگذاری فوری بر انتظارات انرژی را کاهش دهد.
@WarRoom</div>
<div class="tg-footer">👁️ 123K · <a href="https://t.me/withyashar/21291" target="_blank">📅 19:40 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21290">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b07a22b837.mp4?token=AleHvfXjNCfFYPM0o8cHxkrkc6mlcFE9YfArpmCjxCJ7nN01C4lU7DYZ6QYVn8rML8-V88-IC67ukALxFL8eOM2xfyXYY_nNZ5-B0T_iYgft14sOOw510mY5d2iJE-nIgh-aSXBYg4rZasQbUQgEkB1v0UftbngFKA5t-3gerkLFUSUHmUVAkQoZKkpxm5czdIEyUhCMZuntSYNuRKyoqfGCGNpnux4XGN9NlihJ1Aun0_aRzFrLaobxRwSI8X-Su3hNu_QYlXtakWb-QervJWcMHBChrnXaPkDlYzZyikglnuIyvdGnA4hjjCFjripc84q2paxRXx96FvZzAqT1lH6LEg_hcjwa7Etd7UWtXsMnGuYHGV71RLAt5l8fzcuO5Z7WjNrytCHFpCNtppZ9pg8V2ol5nZnR6T9ShT7pM-WbDD2aRg53dSQTo88HR-C2ZsNF4Em1gPq2jUodc2XlKrMUFpzfvWQ1KdSD3q-kHsixfJhMRhfpZX4ynYs6COxT9-6GJ30nmgXoWIbt820Ku9stWa_Gvlt39olkfM8mFzhkcIPolUXtVPXwfIpfclHve6EVjkYMFNwze7nN3WRY_q9TvdbMGzy-bpiHpaMMUT6QIciXAlXPjNa4NExYO8k57a4XAsvXgBE3fBlVuJJjMiBg2v3-TIgaoF5E96dQotk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b07a22b837.mp4?token=AleHvfXjNCfFYPM0o8cHxkrkc6mlcFE9YfArpmCjxCJ7nN01C4lU7DYZ6QYVn8rML8-V88-IC67ukALxFL8eOM2xfyXYY_nNZ5-B0T_iYgft14sOOw510mY5d2iJE-nIgh-aSXBYg4rZasQbUQgEkB1v0UftbngFKA5t-3gerkLFUSUHmUVAkQoZKkpxm5czdIEyUhCMZuntSYNuRKyoqfGCGNpnux4XGN9NlihJ1Aun0_aRzFrLaobxRwSI8X-Su3hNu_QYlXtakWb-QervJWcMHBChrnXaPkDlYzZyikglnuIyvdGnA4hjjCFjripc84q2paxRXx96FvZzAqT1lH6LEg_hcjwa7Etd7UWtXsMnGuYHGV71RLAt5l8fzcuO5Z7WjNrytCHFpCNtppZ9pg8V2ol5nZnR6T9ShT7pM-WbDD2aRg53dSQTo88HR-C2ZsNF4Em1gPq2jUodc2XlKrMUFpzfvWQ1KdSD3q-kHsixfJhMRhfpZX4ynYs6COxT9-6GJ30nmgXoWIbt820Ku9stWa_Gvlt39olkfM8mFzhkcIPolUXtVPXwfIpfclHve6EVjkYMFNwze7nN3WRY_q9TvdbMGzy-bpiHpaMMUT6QIciXAlXPjNa4NExYO8k57a4XAsvXgBE3fBlVuJJjMiBg2v3-TIgaoF5E96dQotk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آخوندی در تجمعات شبانه: هنوز که از بغل بیت رهبری رد میشیم بوی گوشت سوخته آقا میاد!
@WarRoom</div>
<div class="tg-footer">👁️ 129K · <a href="https://t.me/withyashar/21290" target="_blank">📅 18:43 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21289">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">دفتر نخست‌وزیری اسرائیل:
اردوغان یک دیکتاتور یهودی ستیز است که کردها را قتل عام کرده، تروریست های حماس را در خود جای داده است، نیمی از قبرس را اشغال کرده است، و تعداد روزنامه نگاران و سیاستمداران مخالف خود را به زندان انداخته است.
او اکنون به دنبال گسترش تجاوزات خود به اسرائیل به سوریه است. اسرائیل آن را تحمل نخواهد کرد.
@WarRoom</div>
<div class="tg-footer">👁️ 116K · <a href="https://t.me/withyashar/21289" target="_blank">📅 18:16 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21288">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JB5V7NnNz16nFLkDj4uMiMj7luMLZUkozRZHY2MYSRHz4FauJqy_ZQtxIUaY8aDaoTvKqTyKr4jt_k-Vrp79iVDi31mMe6N2ij0jeIabXIRY3W1xEzIqnIyzuHGv2yNc_WeGVM_0Cvz30wezGOrcnT16lwH1f2pKXh-04QMMj1SreqCA1VeVJwUXvkl35024dhfslc7YfVm1dOl20owwifZdno_I9ceA__4ZOKdmrR24JDKt2EgO5e7EFmfX22_id1Jpl46Cdv3I2rUjjPhT5GkgJNXyMcfHlA49p8z-fUbmsw4CMq_JobApHO6_TSZcXDZQnB-90XBlx9Pck3eeHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تحرکات جدید در العدید؛ ۴ سوخت‌رسان آمریکایی و ۵ فروند C-17 قطر در پایگاه
تصاویر ماهواره‌ای Sentinel-2 که امروز ثبت شده، حضور چهار هواپیمای سوخت‌رسان نیروی هوایی آمریکا در پایگاه هوایی العدید قطر را نشان می‌دهد.همچنین پنج فروند هواپیمای ترابری راهبردی C-17 گلوبمستر III نیروی هوایی قطر به العدید بازگشته‌اند؛
این نخستین بار از ۱۲ ژوئیه است که حضور این هواپیماها در پایگاه مشاهده می‌شود.
بازگشت همزمان هواپیماهای ترابری قطری و تداوم حضور سوخت‌رسان‌های آمریکایی، از ادامه فعالیت‌های هوایی در العدید حکایت دارد.
@WarRoom</div>
<div class="tg-footer">👁️ 119K · <a href="https://t.me/withyashar/21288" target="_blank">📅 17:35 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21287">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">امام جمعه رشت : برای افزایش جمعیت از مردم میخوام دست به دست هم بدن و به همدیگه کمک کنیم
@WarRoom</div>
<div class="tg-footer">👁️ 120K · <a href="https://t.me/withyashar/21287" target="_blank">📅 16:59 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21286">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0e7e5ce77a.mp4?token=GN0n2dimQGodlcJ0MwCvYgMU8x3ZMLsdhySQ2JE9yx-cWO6jm22MjFdMCpRZqLV4Axww7B_f6i5Hdg2cARoq8smHGsC2lNevqFzyqxuVXUJowfNH839EvdnqAawaIQ3bgtD-jJcog4zFNaHYYeRkbl3F5GMFfVLQWy66F2Qgz2qHqqksMotpHZD9Qt7ncW0KXDemp2_flAUtv3UdCiYhfJ5ql56eEjoB-nFKIgA03hRv1jtvUMva5UO7W_kfgHKOestgwgDRurgL4eLI5Q1OVUJE0tS-6zmWAKtGEDfUVxgfHsXjWaI90R7OT1UFuIg2TydZoz0AwNnvNzUBEU3OADaN9yPcr8WRpV7oFmQl1An3y_5LWS8OkADgwAeW7Qgapv03_9_HHaTK8GXpeSFJHFNWD3xYOCiBolEPcY_-0_hS7rQXtM_2G1F5YgqSXBqS_PQm4e_7E0-eJzkGIoveh3mqN9Ef8ecKZiinoI2x0pv_jqnLJnOhOH1RuKiy_ji3BZZt3lThpwYNYpzhexyN9j8jA2jveDg4WifLucVs6fJxYLGEpFevJ5n6z0AN-gxRYaEBuyHFPxG1LaAaOJ1YawjH7G_mbjujhsoPDh-BNSOUIopSDvAkCXmLMwT5vqPqvGnUi-rEtVY0WFC8eNdw16FJk6hsvtMksunUHcQO5us" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0e7e5ce77a.mp4?token=GN0n2dimQGodlcJ0MwCvYgMU8x3ZMLsdhySQ2JE9yx-cWO6jm22MjFdMCpRZqLV4Axww7B_f6i5Hdg2cARoq8smHGsC2lNevqFzyqxuVXUJowfNH839EvdnqAawaIQ3bgtD-jJcog4zFNaHYYeRkbl3F5GMFfVLQWy66F2Qgz2qHqqksMotpHZD9Qt7ncW0KXDemp2_flAUtv3UdCiYhfJ5ql56eEjoB-nFKIgA03hRv1jtvUMva5UO7W_kfgHKOestgwgDRurgL4eLI5Q1OVUJE0tS-6zmWAKtGEDfUVxgfHsXjWaI90R7OT1UFuIg2TydZoz0AwNnvNzUBEU3OADaN9yPcr8WRpV7oFmQl1An3y_5LWS8OkADgwAeW7Qgapv03_9_HHaTK8GXpeSFJHFNWD3xYOCiBolEPcY_-0_hS7rQXtM_2G1F5YgqSXBqS_PQm4e_7E0-eJzkGIoveh3mqN9Ef8ecKZiinoI2x0pv_jqnLJnOhOH1RuKiy_ji3BZZt3lThpwYNYpzhexyN9j8jA2jveDg4WifLucVs6fJxYLGEpFevJ5n6z0AN-gxRYaEBuyHFPxG1LaAaOJ1YawjH7G_mbjujhsoPDh-BNSOUIopSDvAkCXmLMwT5vqPqvGnUi-rEtVY0WFC8eNdw16FJk6hsvtMksunUHcQO5us" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کارشناس صداوسیما: نتانیاهو خیلی مرده؛ نه خسته شده از جنگ با ما، نه پشیمونه و هرآن ممکنه بهمون حمله کنه و بنظرم خیلی مرده.
@WarRoom</div>
<div class="tg-footer">👁️ 125K · <a href="https://t.me/withyashar/21286" target="_blank">📅 15:43 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21285">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">ترکیه، حکم بازداشت اینترپل قرمز برای  نتانیاهو صادر کرد و او را به عنوان متهم در ارتباط با حادثه "ناوگان مقاومت" عنوان کرد
@WarRoom</div>
<div class="tg-footer">👁️ 121K · <a href="https://t.me/withyashar/21285" target="_blank">📅 15:40 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21284">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0ba907831b.mp4?token=ow7cuxgtHy8QRSgJAEIKD8h8bFSk1wRxGSqDMcGo3MAUs3_qB3WCxdBhueSd3xgdPPmFdKkhcL7Tf_ztblVhy_8g6vlukaVyMznh9uaA8TF-H47mtibhU_YAFKyTrmYmGrpZWEC-LVjU7mTKikEecbygdrbPVf3lEZ_l1fVgb42kT9kG87fkKzLfej9bcEH608iXb64e7rZj3R8h7ds0cmlOs7eQIUu-2c9iAnLzb5t2-jwsO-gVMLPWL9Xpsz70eTCXkDloB7gX7mx_eSEMMubUDLsxC7H-zIDPu5bnGJfa1-lPhlgU09hN7zqQ3jaothQY0OW-q0WiNBGjc1MPTw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0ba907831b.mp4?token=ow7cuxgtHy8QRSgJAEIKD8h8bFSk1wRxGSqDMcGo3MAUs3_qB3WCxdBhueSd3xgdPPmFdKkhcL7Tf_ztblVhy_8g6vlukaVyMznh9uaA8TF-H47mtibhU_YAFKyTrmYmGrpZWEC-LVjU7mTKikEecbygdrbPVf3lEZ_l1fVgb42kT9kG87fkKzLfej9bcEH608iXb64e7rZj3R8h7ds0cmlOs7eQIUu-2c9iAnLzb5t2-jwsO-gVMLPWL9Xpsz70eTCXkDloB7gX7mx_eSEMMubUDLsxC7H-zIDPu5bnGJfa1-lPhlgU09hN7zqQ3jaothQY0OW-q0WiNBGjc1MPTw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فاکس نیوز : ایران کم‌کم متوجه می‌شود که رئیس‌جمهور ترامپ و ارتش آمریکا در خارج کردن مخفیانه نفت از تنگه هرمز تا سقف ۱۰ میلیون بشکه موفق هستند.
بعضی شب‌ها به ۱۵ تا ۲۰ میلیون بشکه می‌رسد... این جریان قبل از جنگ است!
حتی سی‌ان‌ان هم مجبور شد اعتراف کند: ایران در حال از دست دادن کنترل خود است
همچنین رئیس‌جمهور ترامپ جبهه دیگری را باز می‌کند و کشورهایی را که به تهران کمک کردند تا سرپا بماند، تهدید می‌کند.
چیزی از ایران باقی نخواهد ماند.
ملاها این را خواستند.
@WarRoom</div>
<div class="tg-footer">👁️ 127K · <a href="https://t.me/withyashar/21284" target="_blank">📅 14:06 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21283">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">ای‌بی‌سی‌نیوز: FBI از احتمال حمله پهپادی ایران به کالیفرنیا خبر داد
@WarRoom</div>
<div class="tg-footer">👁️ 119K · <a href="https://t.me/withyashar/21283" target="_blank">📅 13:00 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21282">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">کارشناس صداوسیما:
علی خامنه‌ای یک پله از امام علی پایین‌تر بود و معجزه هم میکرد.
@WarRoom
😁</div>
<div class="tg-footer">👁️ 124K · <a href="https://t.me/withyashar/21282" target="_blank">📅 12:40 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21281">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">بیتکوین 77,000$ را شکست و در چند روز 15000$ گران شد @WarRoom</div>
<div class="tg-footer">👁️ 117K · <a href="https://t.me/withyashar/21281" target="_blank">📅 12:32 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21279">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TwkYSRuo8wSRSiEVvUW2OTzwdOAh2tMY6nS1Ro3ZEPyG-uMkw0QZ3nfyaaIi2B9-s7wn0X4ZOewhhsaqMfkKkIUNaRQNREtLUTGzsDYN0CUiHbp9ueL1IEP_vyWq4nnbEu1z_foPvpk3fWtb7Pnl8pQsvNgmXyr-EmD53v4VsyiNn2El4-6bXWAJfri0Rw8znQsAHrJF9t-eMf3KvtoWtsJ9oZlOooft3ZU4WjUT_UysMnoC7FWz0dDPUoH6ifSEH8bfi_G_ZIVkiojv-4lWkweRNt3tOzQU9kQtR7C1kxmMLebeYMpkdCuHVkOYG1HkUg7m8qtuXRnbSyPSR_XPQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qRFQZHoLTYjUjkd5UNojliwgCr6QgGQILwRcrREqh0SuutlA6PNPLVzWth-0fa5Oa7uX8mdRcU5NkBiVCFWUJ38k88ffBB4jP_IZ3HJTDCcRod5idA60KhaBvkuOg3X7z3nt6tu4bizz4Sf3ztqeEV2BjWWsb23jlKqnD5h5Z9zWXDuNX-YlsgCOqq7qb_7MWbkkGbf1Efmpim93cNSVZaT0MUVgqtZY1GTzQzfEQAAeI-Y8MbM0UjyfdYirZb7GkHoVwfGGhtRCisx6FehkBPi2KcUilcngDq2WkMrdf419Q-gJlGgkSOejDPn74GCnL9Kg9bLizRGk6wHPd8DoJg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">دیشب یک هواپیمای بویینگ E-3B سنتری  AWACS آلارم 7700 وضعیت اضطراری روشن کرد. ولی اکنون یک هواپیمای دیگر با همان مدل و مشخصات به پرواز در آمده که نشان می‌دهد که آمریکا تجهیزات کافی پشتیبانی در منطقه بسیار دارد.
@WarRoom</div>
<div class="tg-footer">👁️ 119K · <a href="https://t.me/withyashar/21279" target="_blank">📅 12:20 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21278">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">بیتکوین 77,000$ را شکست و در چند روز 15000$ گران شد
@WarRoom</div>
<div class="tg-footer">👁️ 112K · <a href="https://t.me/withyashar/21278" target="_blank">📅 11:56 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21277">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UA0-6NdTgGaqO9jVb7Uuso0pTdLxMAQzAsbTIjfp0UsC4BGGsV9qKlaFLGsQFeYZdyx0NLBd-mGAPR61ykqC8dWa7oNmSdCMB3F7QmTTE9dRN6H-yn10AmC1T7YVT2Ilekw8fnBODPG7S6N5hbDd1kPozsLxu-fRZs6IpZruuqVFIgYmaI_9pLo_djIbK3s3w8jqyld0WZ2ptkKYzYMzr0uvJgrhCon2XaroMhjY2xdl4qdp026a8UAp0cIG8S1jlTGpOpiMiVzuc_uM6KNr0Vw_b80CnvFyuTbxLjY5Ci-GQbi0P3uF7TzHUH4oiIsqKIF2V_p4YcsIHbjxESqvgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ایالات متحده، دومین هواپیمای تانکر سوخت‌رسان را از مجموع شش فروند هواپیمای جدید، به نیروی هوایی اسرائیل تحویل داد.
@WarRoom</div>
<div class="tg-footer">👁️ 117K · <a href="https://t.me/withyashar/21277" target="_blank">📅 11:36 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21276">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">گزارش های بسیار از چندین صدای پرتاب از سیریک ، خونه ها لرزیدن و صدای انفجار از تنگه و صدای جنگنده ، همون فرمولی که گفتم جمهوری اسلامی میزنه نفت بره بالا  @WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 114K · <a href="https://t.me/withyashar/21276" target="_blank">📅 11:23 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21275">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">‏سقوط چشمگیر تردد در تنگه هرمز؛ تنها ۷ کشتی باری در روز پنجشنبه عبور کردند.
‏داده‌های شرکت ردیابی دریایی کپلر نشان می‌دهد تردد کشتی‌ها در تنگه هرمز روز پنجشنبه به نصف روز چهارشنبه کاهش یافت و تنها ۷ کشتی باری، شامل ۴ کشتی ورودی و ۳ کشتی خروجی، از این گذرگاه راهبردی عبور کردند. هیچ‌یک از این شناورها نفتکش یا حامل گاز طبیعی مایع نبودند، هرچند یک کشتی بسیار بزرگ حامل پروپان و بوتان از مسیر ایران از تنگه خارج شد. پرزیدنت ترامپ نیز طی روزهای اخیر بارها تأکید کرده است که ایالات متحده کنترل تنگه هرمز را در اختیار دارد.
@WarRoom</div>
<div class="tg-footer">👁️ 114K · <a href="https://t.me/withyashar/21275" target="_blank">📅 10:57 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21274">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">‏کانال ۱۴ اسرائیل: ترکیه با وجود هشدارهای نتانیاهو، محموله نظامی دیگری به سوریه فرستاد.
‏بر اساس این گزارش، ترکیه محموله تازه‌ای شامل حدود ۲۰۰ خودروی نظامی، از جمله ۲۰ تانک، به سوریه اعزام کرده است؛ اقدامی که با وجود هشدارهای نتانیاهو درباره تحرکات نظامی ترکیه در سوریه انجام شده است.
@WarRoom</div>
<div class="tg-footer">👁️ 112K · <a href="https://t.me/withyashar/21274" target="_blank">📅 10:34 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21273">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">رویترز: در تهدید ترامپ علیه کسانی که به ایران کمک می‌کنند، حتی متحدان واشنگتن که در میانجیگری مذاکرات صلح نقش داشته‌اند هم ممکن است در این دایره قرار بگیرند و آن را شامل هر کشور یا نهادی کرده است که به تهران آنچه را او «شریان حیاتی» توصیف کرده، ارائه دهد.
@WarRoom</div>
<div class="tg-footer">👁️ 111K · <a href="https://t.me/withyashar/21273" target="_blank">📅 10:15 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21272">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-footer">👁️ 109K · <a href="https://t.me/withyashar/21272" target="_blank">📅 09:52 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21271">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromDr.t</strong></div>
<div class="tg-text">کجایی ؟ داشتم نگران میشدم</div>
<div class="tg-footer">👁️ 109K · <a href="https://t.me/withyashar/21271" target="_blank">📅 09:51 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21270">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">ترامپ : ما گزینه دیگه‌ای جز جنگ با جمهوری اسلامی نداشتیم و اگه لازم باشه ۱۰۰ بار دیگه‌ هم اینکارو تکرار میکنم چون آنها نباید به سلاح هسته‌ای برسند!
جمهوری اسلامی به کشورهای بی‌طرف مثل عربستان، قطر، امارات، کویت و بحرین حمله کرده!
اگه برجام رو پاره نمیکردم، الان سلاح هسته‌ای داشتند و ازش علیه همه کشورها استفاده میکرد!
رسیدن به توافق با آنها اصلا آسون نیست چون درحال حاضر هیچکس نمیدونه دقیقا چه کسی داره رهبری میکنه!
@WarRoom</div>
<div class="tg-footer">👁️ 112K · <a href="https://t.me/withyashar/21270" target="_blank">📅 09:40 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21269">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">سخنگوی پنتاگون به وال استریت ژورنال: ما تمام امکانات لازم را برای شروع حملات به ایران  را در زمان و مکانی که رئیس جمهور تعیین می‌کند، در اختیار داریم و هیچ کمبودی نداریم
@WarRoom</div>
<div class="tg-footer">👁️ 113K · <a href="https://t.me/withyashar/21269" target="_blank">📅 09:37 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21268">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fRdZJZ80HY_IMD7ePqga3-6jeWk5v1tQpk6XKstV9q0zEKKLWZVMheqacq7j_fx4Plo3gQ26Hv1hLj__cF1pQs8_IwMI4GfdNiwMMY_f5qy2zQxjKe5KI-K-xIUwH5ZEOIMHIYvH6BTp_JY9jXudvI_ZcFRKplZnTp1agh27yd6s7zJ93nJ22HcHMkRLCsRGwbtt4Z8HUSUfI-zqGdJTcsFf--I5jtr_c9gu7E6sP3skageVisfexr5WLfMwYXOZ5Qw496PamPkypHPTmwuRjxU4lLxeRZzVc4ybAiwOZrMsoYe7pZUsCxXvt_l_RO-MDQSzacKNEl4QWVpfnnIipA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فرزند مرفه رژیم جنایتکار ایران برای فرار از بازداشت ICE و بازگشت به زندگی لوکس در لس‌آنجلس پول جمع می‌کنند.
یک فعال ایرانی‌تبار که در جریان اعتراضات ایران بر اثر شلیک سپاه یک چشم خود را از دست داده، از
سید عیسی هاشمی، پسر معصومه ابتکار، معروف به «مریم جیغ‌زن»
، انتقاد کرده است. هاشمی ۴۳ ساله که از سال ۲۰۱۰ در آمریکا زندگی می‌کند، چند ماه پیش توسط
ICE
در کالیفرنیا بازداشت شده و روند لغو گرین‌کارت و اخراج او در جریان است؛ اقدامی که بنا بر گزارش با دستور
مارکو روبیو
انجام شده است. او اکنون با راه‌اندازی کمپین
GoFundMe
از مردم آمریکا کمک مالی می‌خواهد تا بتواند در این کشور بماند و به زندگی خود در لس‌آنجلس ادامه دهد
@WarRoom</div>
<div class="tg-footer">👁️ 122K · <a href="https://t.me/withyashar/21268" target="_blank">📅 09:30 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21267">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">ترامپ در تروث بازنشر صحبتهای مقام ارشد کاخ سفید ، استفن میلر: او (ترامپ) ناامن‌ترین مرز تاریخ آمریکا را تحویل گرفت و ۱۵ ماه پیاپی، ورود غیرقانونی به کشور را به صفر رساند؛ برای انرژی و زنجیره‌های تأمین آمریکا دستاوردی تاریخی رقم زد، با کارتل‌های مواد مخدر مقابله کرد و آن‌ها را سازمان‌های تروریستی خارجی اعلام کرد؛ مانع دستیابی ایران به سلاح هسته‌ای شد؛ با ساخت خطوط لوله و افزایش تولید انرژی، قیمت بنزین را کاهش داد؛ تورم را به ۲ درصد رساند و با تصویب بزرگ‌ترین کاهش مالیاتی تاریخ آمریکا، مالیات بر انعام، تأمین اجتماعی و اضافه‌کاری را لغو کرد؛ یک پیروزی بزرگ و تمام‌عیار.
@WarRoom</div>
<div class="tg-footer">👁️ 127K · <a href="https://t.me/withyashar/21267" target="_blank">📅 00:59 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21266">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">یک مسئول دولت ترامپ به واشنگتن پست:
ایران "کاملاً ورشکسته" است و ترامپ ابزارهای متعددی در اختیار دارد که می‌تواند در هفته‌ها و ماه‌های آینده از آن‌ها به شکلی قوی‌تر استفاده کند.
@WarRoom</div>
<div class="tg-footer">👁️ 128K · <a href="https://t.me/withyashar/21266" target="_blank">📅 00:48 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21265">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">حملۀ هوایی اسرائیل به ارتفاعات علی‌الطاهر در جنوب لبنان
@WarRoom</div>
<div class="tg-footer">👁️ 128K · <a href="https://t.me/withyashar/21265" target="_blank">📅 00:46 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21264">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">کانال 14 اسرائیل: مجتبی خامنه‌ای «
ایزوله
» شده و سپاه کشور را اداره می‌کند.
@WarRoom</div>
<div class="tg-footer">👁️ 130K · <a href="https://t.me/withyashar/21264" target="_blank">📅 00:15 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21263">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">ارسالی تایید نشده : یاشار همین الان اهواز صدای شلیک موشک میومد قشنگ ی دودی توی هوا معلوم بود ولی دوربین گوشی اینقدر قوی نیست که بتونه دود رو بگیره
@WarRoom</div>
<div class="tg-footer">👁️ 130K · <a href="https://t.me/withyashar/21263" target="_blank">📅 23:42 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21261">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/75cf8ca15a.mp4?token=uRNwUHUetL5B2mfvBh6BruoaOlYNHBPpPW008VHtB4DqMNDpcM9E8_F8aHSYNeA69mQWG5R96-5c3i84P9TssTd5R2k9vcV_k0sfYCsnJWABHzLXQJz67z7qrtdcxGsfet22kwO_4skrbE5KlOTLWznQm6oSqTvC6-lD0EewvHzcSztO6ZVFwF2x1Txg_F56v1RTD_rfSZVhav3H7wL54jnqcE3ZIFVfaepctfDZEdf8nrBk-2aV5vgp-DskwpIT52ADvP050K5dkCrwUs07gYtAlSwuiNzwMMImgTxRJVBs3Wy5a-xT1FvupGYA-dyp6xFx2pBZLrUeCZS3hlbOEQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/75cf8ca15a.mp4?token=uRNwUHUetL5B2mfvBh6BruoaOlYNHBPpPW008VHtB4DqMNDpcM9E8_F8aHSYNeA69mQWG5R96-5c3i84P9TssTd5R2k9vcV_k0sfYCsnJWABHzLXQJz67z7qrtdcxGsfet22kwO_4skrbE5KlOTLWznQm6oSqTvC6-lD0EewvHzcSztO6ZVFwF2x1Txg_F56v1RTD_rfSZVhav3H7wL54jnqcE3ZIFVfaepctfDZEdf8nrBk-2aV5vgp-DskwpIT52ADvP050K5dkCrwUs07gYtAlSwuiNzwMMImgTxRJVBs3Wy5a-xT1FvupGYA-dyp6xFx2pBZLrUeCZS3hlbOEQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ملانیا ترامپ، بانوی اول: شنیدم دلتان برایم تنگ شده بود. من اینجا هستم.به کاخ سفید خوش آمدید
@WarRoom</div>
<div class="tg-footer">👁️ 128K · <a href="https://t.me/withyashar/21261" target="_blank">📅 23:34 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21260">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">‏تانکر ترکرز:‏ دلیل اینکه دیگر در خارک شاهد بارگیری‌های زیادی نیستیم، این است که تولید نفت خام ایران در ماه‌های اخیر به سطحی کاهش یافته که فقط اندکی بالاتر از میزان مصرف پالایش داخلی این کشور است. این یعنی ایران در حال حاضر فشار چندانی برای صادرات نفت ندارد.
‎
@WarRoom</div>
<div class="tg-footer">👁️ 125K · <a href="https://t.me/withyashar/21260" target="_blank">📅 23:24 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21259">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/471bef475d.mp4?token=n1SKnYfvq6ZWa90FfDFC9LWnRbwhCQkoc2e2sHnmF4SCZkSNgdlUCC6JLz3pg8JPVW1T-TkPCSVT9D5kFLoISwKrABAAIZ-dHIzqJ6r06OZuEPml07yPNjnsbT-Qyuvew9N4YQEkNAXe_iqpKeDqfchwIsvy_TfPZedTMHjGZX1zRtpcJO4UR_r6cvcMYWzIwC1SK_F3Ego45czLcNNfh2BEaMpnJVtUv59GB6haExCsTdbya58cAz8DzRSgExagHHCja_V6yzbRWMZ15VMpHjaICRD_LhyUC2-rOFDVITNZa7nH3RPUfWpZ7e9kHGWfxsXER7woF8iQvxODdDgN1g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/471bef475d.mp4?token=n1SKnYfvq6ZWa90FfDFC9LWnRbwhCQkoc2e2sHnmF4SCZkSNgdlUCC6JLz3pg8JPVW1T-TkPCSVT9D5kFLoISwKrABAAIZ-dHIzqJ6r06OZuEPml07yPNjnsbT-Qyuvew9N4YQEkNAXe_iqpKeDqfchwIsvy_TfPZedTMHjGZX1zRtpcJO4UR_r6cvcMYWzIwC1SK_F3Ego45czLcNNfh2BEaMpnJVtUv59GB6haExCsTdbya58cAz8DzRSgExagHHCja_V6yzbRWMZ15VMpHjaICRD_LhyUC2-rOFDVITNZa7nH3RPUfWpZ7e9kHGWfxsXER7woF8iQvxODdDgN1g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جی‌دی ونس، معاون رئیس‌جمهور آمریکا، گفت واشینگتن وارد مرحله جدیدی در قبال ایران شده که در آن
فشار اقتصادی مؤثرترین ابزار آمریکا
است. ونس گفت ایران در دو هفته گذشته فشار اقتصادی بیشتری نسبت به آمریکا متحمل شده و واشینگتن قصد دارد این فشار را ادامه دهد. او تأکید کرد تأسیسات هسته‌ای ایران نابود شده‌اند، اما هدف آمریکا ایجاد
«واقعیتی جدید»
است
@WarRoom</div>
<div class="tg-footer">👁️ 123K · <a href="https://t.me/withyashar/21259" target="_blank">📅 23:15 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21258">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5c77add985.mp4?token=bYsFxEFTnlWmtS8fq-ksAFOaVZYYJo78QkGIt4IG_qG4ePdiseyVzjozwZ8i9WlBWApYsW4QIwtCMoVf1P1Uef7SY2E1pZK8RdQDcIw7T2drKbg_RA3mMrI755kbKJwxIrHglEw_ct1xjQjlTXEdmAuxez7isTsfWPi0WyGOsDuK8Kmt647yIHQvd1I_zFVPWRlnQoOuwkucCdEqI9QsNvPq2giZe0RQTjY3yUwRWBouYMIuuKDlSQTvZqD8fucxJK3kl9_cQW2Dxy7V4FbPO6inwfC8gqbgLOQG0byCweCBfSBSXJcPRZDI_7ddyDn3v0dUpNnXFcfVsHuRtQKSyA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5c77add985.mp4?token=bYsFxEFTnlWmtS8fq-ksAFOaVZYYJo78QkGIt4IG_qG4ePdiseyVzjozwZ8i9WlBWApYsW4QIwtCMoVf1P1Uef7SY2E1pZK8RdQDcIw7T2drKbg_RA3mMrI755kbKJwxIrHglEw_ct1xjQjlTXEdmAuxez7isTsfWPi0WyGOsDuK8Kmt647yIHQvd1I_zFVPWRlnQoOuwkucCdEqI9QsNvPq2giZe0RQTjY3yUwRWBouYMIuuKDlSQTvZqD8fucxJK3kl9_cQW2Dxy7V4FbPO6inwfC8gqbgLOQG0byCweCBfSBSXJcPRZDI_7ddyDn3v0dUpNnXFcfVsHuRtQKSyA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ارتش اسرائیل و شاباک فاش می کنند: سازمان تروریستی حماس در بیمارستان «ناصر» در خان‌یونس بازجویی‌های امنیتی و شکنجه انجام می‌دهد
@WarRoom</div>
<div class="tg-footer">👁️ 118K · <a href="https://t.me/withyashar/21258" target="_blank">📅 23:08 · 29 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
