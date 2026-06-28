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
<img src="https://cdn4.telesco.pe/file/I4aHwKbs0rQ6BbiQKC5zczX10670ykBkK0copiM2clwhZTrmfDGnA09aCgXaYlAA9P8G2sZxHRPoPgdHOA75O0XdxO3DRDd2jzsQoQgVGUOwmJERA-Igelhss8akD7FlPsRwswqBUn1Zj8HEniBl5RCV3hRhXfk0CsG5kDQeFdsPWwdpkgfvDnHHW-JUT9owANJxOQNv2ZHi2hC-wvdYzD_mQRubXccffui-45VDM6D6qeucbJLm9Gvsz1UlLnG_xro4hROlkHy--PrutSMfM-jJ71-Nnr4XtHjkprS-6rqBl79OmwoiLr7b-XctKqs-qYiYeD81SG_7tQyWHwLl4A.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 218K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-07 17:50:05</div>
<hr>

<div class="tg-post" id="msg-67000">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VYCDizrkm7F0QVQGygRuz8lDk3HO_q0O9LdnTwIcdRvn7VmIIcCuKkjkoRPi8wSJEW4i8BSlcs_Eeb7fdOpLJWzgKPF30bIRHG0f4MKBAB_3SmalopIdKLqUKY_dCvhpVJvv6PmzH2t4DMC7f1DUwaynmNM7E8apSNcN_oUa56Dy6PBRsu53_Mfu91X2OrWwIXOS7X9A1fl5BlZspgUMq8VhZnqYY319HPJzKhnp77Orz5e7ORcwdLfoaOa-0htLJ70uzE9XVVP8GyOWEoCjIF-8M2VDT3AkLenUEnEsvr2Xo5nybgx8cIFR6f1vXNRzfY4jcscyoD5dlXZYAOQv2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
سخنگوی کمیسیون امنیت ملی مجلس:
پول‌های مسدودشده مردم در بانک‌های داخلی را آزاد کنید، خارجی پیشکش.
@News_Hut</div>
<div class="tg-footer">👁️ 2.74K · <a href="https://t.me/news_hut/67000" target="_blank">📅 17:34 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66999">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4c972b464a.mp4?token=iWJvxx-JqrMxyM48BJ70lWBvZNBy8Rv9eOvydf7UPMFp5GnpnXDRHGZ1DQILyzf4iFSyz-kLwMXFObXeLrqgWD5XJKH4KfRU6wXOjlnYM9bmryeZyu8eArTX9HzuTqd1mO8-67gYv5719cbFJEyOUSEI0LIhKT_y2XVSx9vrucXONMRzcuXLqthVjjU6GXmjS8tujqel6y3NjUsUKu6ibBWej18_oZcjSygN1HzyyNoWu1JjA90x3z-LMNb8YLlcp9p0OPgFfbiY6LPPbs45_jVrOebRPE_GEvqKdF24PZ0x0MhJ8h-16lQA6-6vjIZey0G8oaSuWW7w5NYFAPuytQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4c972b464a.mp4?token=iWJvxx-JqrMxyM48BJ70lWBvZNBy8Rv9eOvydf7UPMFp5GnpnXDRHGZ1DQILyzf4iFSyz-kLwMXFObXeLrqgWD5XJKH4KfRU6wXOjlnYM9bmryeZyu8eArTX9HzuTqd1mO8-67gYv5719cbFJEyOUSEI0LIhKT_y2XVSx9vrucXONMRzcuXLqthVjjU6GXmjS8tujqel6y3NjUsUKu6ibBWej18_oZcjSygN1HzyyNoWu1JjA90x3z-LMNb8YLlcp9p0OPgFfbiY6LPPbs45_jVrOebRPE_GEvqKdF24PZ0x0MhJ8h-16lQA6-6vjIZey0G8oaSuWW7w5NYFAPuytQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
عراقچی:«بر اساس تفاهم‌نامه، تنگه هرمز ظرف ۳۰ روز و تحت سازوکار مدیریتی مورد تصویب ایران، پس از رفع موانع از سوی جمهوری اسلامی ایران، به ظرفیت عملیاتی پیش از جنگ بازخواهد گشت.
🔴
این ترتیبات هم‌اکنون در حال اجراست و مسئولیت کامل آن صرفاً بر عهده جمهوری اسلامی ایران است. هیچ نهاد یا کشور دیگری در این زمینه مسئولیتی ندارد.
🔴
مطابق تفاهم‌نامه امضاشده میان ایران و ایالات متحده، هرگونه مداخله در این موضوع یا هرگونه تلاش برای ایجاد سازوکارهای جدید یا جداگانه، غیر از ترتیباتی که اکنون از سوی جمهوری اسلامی ایران در حال اجراست، تنها موجب پیچیده‌تر شدن وضعیت، به تأخیر افتادن بازگشایی تنگه هرمز و افزایش تنش‌ها خواهد شد.
🔴
همان‌گونه که طی دو شب گذشته شاهد بودیم، رخدادهای تنگه هرمز از پیش به افزایش تنش‌ها و رویارویی‌ها دامن زده است.
🔴
از همه طرف‌ها می‌خواهم در مدیریت تنگه هرمز یا در ترتیباتی که جمهوری اسلامی ایران برای بازگشایی آن در حال اجرا دارد، مداخله نکنند.
@News_Hut</div>
<div class="tg-footer">👁️ 5.47K · <a href="https://t.me/news_hut/66999" target="_blank">📅 17:04 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66998">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/96542aaa83.mp4?token=r2yQae6oEcArODVBh38Bkj1Fd3deAh-EIy67Jv-J3-L_1cdjLHjO0HVYW-IA0-QDZrK8SZVPvzuvI6YCnw4jtQhZ--QHXI8W2eB0XxoDVM9ha_M3wXzSTuE7SUnx1L4G8zmvotCV6i8QYI2h061a6FPVewlsxkagtDsGhRhdgCxC7g29hrgTzVhAxNdAIy3sv_HA4Gnd-xVrfEd1arYiUXczpGaBjafp_GxhJ3Vhubc1jJZCvsH9UCXPTZGSmDaPQEtzZpciA_oA_4RjLM1cs2Kpg5dYagfTuhrcH13BLVMB4ruHvKiKhR38Bhdksu9fea6S_UNZejuyLYey4o42YQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/96542aaa83.mp4?token=r2yQae6oEcArODVBh38Bkj1Fd3deAh-EIy67Jv-J3-L_1cdjLHjO0HVYW-IA0-QDZrK8SZVPvzuvI6YCnw4jtQhZ--QHXI8W2eB0XxoDVM9ha_M3wXzSTuE7SUnx1L4G8zmvotCV6i8QYI2h061a6FPVewlsxkagtDsGhRhdgCxC7g29hrgTzVhAxNdAIy3sv_HA4Gnd-xVrfEd1arYiUXczpGaBjafp_GxhJ3Vhubc1jJZCvsH9UCXPTZGSmDaPQEtzZpciA_oA_4RjLM1cs2Kpg5dYagfTuhrcH13BLVMB4ruHvKiKhR38Bhdksu9fea6S_UNZejuyLYey4o42YQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇱
نتانیاهو:
می‌خواهم به شما یادآوری کنم که در لبنان چه بود. حزب‌الله ۱۵۰٬۰۰۰ موشک و راکت داشت. و ما حدود ۹۰٪ از این انبار عظیم را از بین بردیم.
ما آنها را با بیپرها شوکه کردیم، نصرالله را از بین بردیم، فرماندهان نیروی رضوان را کشتیم.
فقط در دو هفته گذشته بیش از ۲۰۰ تروریست را کشتیم.
@News_Hut</div>
<div class="tg-footer">👁️ 8.25K · <a href="https://t.me/news_hut/66998" target="_blank">📅 16:27 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66993">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from[ 𝐇𝐨𝐭𝐍𝐞𝐰𝐬➕]</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/icxYaxT0dPbYtk6Ex6DJiTIGM33z2zh0Gae5ldKlw6uB7EGb9E8Rv3B7fFu-mkrK59Gy4PSM_ZxGM-xZ-RfkFLsNzGyXa8wjKpn22kUKKGcpJijQl9Fr_dWZDdbHGY49uwLopaUj7JNkZ4SbGuVq6NDVm_SCc76v8YRIDtjrdsz0O8KT2YBB1g9o4kfT0L3Pw_BCVbfLc-t7wFXzvwKXHbf8_qfq2SFLMTsk07jQ_JqDDe6oYshl1VvFncGeH3lCE9cmle2V3sBX82fhxtH3ToWKyNeCTuo9R2Co9c-2joLPP4E_ZmmmaiDnrkDAZH_R8OjsH4EhW6-7LmfaPmf7ew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/b2Bytnx-JfVnaEo-4uyRYhFQNMi7Zc30JVlMSC_oVWkt9EhG3iunWi7jeBLufd806y1-voY3xna4mbyLYmaZVY80xNaiytoDdyCIbFs1yAVEZMbTWER3Ol1vsAffIlOca0meS32LOyGcD7A6G77tdrseGZMNflqQJjv2aQuE1cfXpttbBrxv75Pt3rShApg1BLAIwg939ZscvsDR_ptso-h0BhjQVIv5JrQ0gryJPqCkRaVNWCJKT1OMt2UZJJ6RqT-0n8Ks7U9D_GXGn00Eh4qtivukcr_iiPJMso5JTCV1QLdbbM5I15Ff-mhsAMhS-tZk6399vL8Ro82t5NQcCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AMMB4Bm5kr1_zorJPOi0MCcWf5jq53bsPm5V6QD66n7ZotwBUmGhEcUl5W7W7pXrDhSG4xb33xCInPGjIpEyPwwGmdXCYxm3dI3uKXMAALDDFXHPFdCK-uvriTA1ed3lPraE-ZEm_TWORFJnTRAtdR4l4-_A95i9bhlMP2y3pxnjILwv0CDOAHV-rXDD6v1ihMRFhqIfM6bKmvel0Cqh8TcLO4GXnRhYtAow4M2RoBB3_nIKHrRi9IoR3qvkbaNDWFugmJWw5bbei6S_5_8m-v315EoYKhjcvHCTaLHa9eUGS-1pHXEct6Xzi-PNDpUbWlaMLkY8NUV8xOj390za9A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e2d278e2c9.mp4?token=JxsmW1O5EgT39huAoUIZmEjW0tNIq0UI3r1zQEqLxgrQRzGylseU2Xp999zJwpKTHsMpb3hoNnlaHzk3kp8UyqZifJCiRxKiv2nbOusyNVb4eQuC-SuvPFHJ47nwxK-TGEx5BhGT0wUT7sCpbHebYwscS0rPIzp2A4sZDh0ZxhLDUwAatgHAa3qprwlVRkzn7mFv7RfJWvIrbkYXpuqa3IfC79jqNuUx0ePY3uyOnkGJf_wy730TKh8Ech7i2zYuvOc4uhJkCyFYiKSLghBQfeWkmfHsPTpGwcMZeD7M6pwodcmqaQn0kehM7l3VR5W2_em2lLPyJhS1jA3l7aKv0A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e2d278e2c9.mp4?token=JxsmW1O5EgT39huAoUIZmEjW0tNIq0UI3r1zQEqLxgrQRzGylseU2Xp999zJwpKTHsMpb3hoNnlaHzk3kp8UyqZifJCiRxKiv2nbOusyNVb4eQuC-SuvPFHJ47nwxK-TGEx5BhGT0wUT7sCpbHebYwscS0rPIzp2A4sZDh0ZxhLDUwAatgHAa3qprwlVRkzn7mFv7RfJWvIrbkYXpuqa3IfC79jqNuUx0ePY3uyOnkGJf_wy730TKh8Ech7i2zYuvOc4uhJkCyFYiKSLghBQfeWkmfHsPTpGwcMZeD7M6pwodcmqaQn0kehM7l3VR5W2_em2lLPyJhS1jA3l7aKv0A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
بیاین یه نگاهی بندازیم ببینیم چه بلایی سر تیم به‌ظاهر ملی اومد؛ قبلش بریم سراغ مصاحبه های بازیکنان این تیم تو تجمعات شبانه حکومتی‌ها:
شجاع خلیل زاده :
حسم نسبت به رهبر شهید ؟ افتخار ایران ؛ گل اگه زدم به رهبر و شهدا تقدیم میکنم
رهبر عزیزمون شهید شد همون چیزی که خودش میخواست بهش رسید
گل بزنم به  رهبر شهیدم تقدیم میکنم و ما فوتبالیست ها همه دوستش داشتیم ، افتخار نداشتم با رهبر دیدار داشته باشم و دوستش دارم
حسین کنعانی :
حسم نسبت به سید مجید نقطه زن ؟ بزن که خوب میزنی ،حسم نسبت به رهبر ؟ بزرگی
رامین رضاییان :
شهادت رهبر انقلاب رو تسلیت میگم تو تیم ملی به عنوان سرباز برای کشورم می جنگم
اتفاقات داخل ایران { دی ماه } به خودمون ربط داره و به خارجیا ربطی نداره
علیرضا بیرانوند:
چه بهتر که تو آمریکا بازی کنیم می‌تونیم تو اون کشور برای اولین بار در تاریخ فوتبال کشورمون به دور بعد جام  جهانی صعود کنیم
روزبه چشمی :
حسم به رهبر شهید ؟ بزرگ همه مردم ایران !
سعادت دیدار با رهبر عزیزمون نداشتیم ولی بزرگ همه مردم بودن و این راهی که مردم دارن میرن ادامه راه ایشونه
و بعد از این اظهار نظر ها بریم سراغ دیدن نتایج، تو بازی اول از ضعیف ترین تیم جام یعنی نیوزیلند دوبار عقب افتادن و در نهایت با سختی یک امتیاز کسب کردند، تو بازی دوم فقط چند سانتی‌متر از باسن مهدی طارمی تو آفساید بود و گلش مقابل بلژیک مردود شد، تو بازی سوم بازم همون طارمی پنالتی رو خراب کرد و در دقیقه ۹۳ شجاع خلیل‌زاده گل زد و خوشحالی‌ای کرد که در تمام جهان سوژه شد، ولی بعد از چند ثانیه کل دنیا روی سرش خراب شد چون فقط دستش ۵ سانتی‌متر تو آفساید بود، نکته جالب اینه که شجاع گفته بود گلم رو تقدیم به رهبر جمهوری اسلامی خواهم کرد
دقت کنید برای اولین بار در تاریخ این جام جهانی ۴۸ تیمی بود و ۳۲ تیم صعود می‌کنند، یعنی در واقع به اندازه‌ی همه‌ی تیم های حاضر در جام های جهانی قبلی، این بار تیم‌ها به دور بعد صعود می‌کردند (علاوه بر تیم های اول و دوم، هشت تیم سوم هم صعود می‌کنه) و بعد از مساوی با مصر، سه شرط برای صعود تیم به‌ظاهر ملی وجود داشت:
۱.بردغنا
۲.نباختن ازبکستان
۳.مساوی نشدن بازی الجزایر و اتریش
ولی در کمال تعجب یک معجزه رخ داد، غنا نبرد، ازبکستان باخت، و در دقیقه ۹۴ بازی الجزایر، ج.ا صعود کرد و در دقیقه ۹۵ با گل اتریش، ج.ا حذف شد، این واقعا یکی از بزرگترین تحقیر های تاریخ بود
...
می‌بینم یک سری افراد با توجیه های احمقانه می‌گن اینا مجبورن و فلان، نه عزیزان دارین اشباه می‌کنید، میانگین سنی این بازیکنا بالای سی ساله و عملا فوتبالشون تموم شده و رسیدن به آخر خط، اینا فقط دنبال باج حکومتی‌ان و حکومت به عنوان حق‌السکوت بهشون مجوز واردات خودروی لوکس می‌ده که می‌تونن ۱۰۰ میلیارد ازش سود کنن، یعنی عملا یک رانت ۵۷۰ هزار دلاری هر شخص بابت حق‌السکوت دریافت می‌کنه، جالبه که تیم های بزرگ جهان مثل آلمان و اسپانیا حتی اگه تیمشون قهرمان هم بشه مبلغ کمتری رو می‌دن به بازیکنا (۴۳۰ هزار دلار)، خلاصه که جام جهانی بزرگترین رویداد برای شنیدن صدای مردم مظلومه، همونطور که تو سال ۱۹۷۸ کاراسکوسا کاپیتان آرژانتین بخاطر جنایت های حکومتش از تیم ملی استعفا داد و...
ودرآخر، از اون ضربه‌ی تیر دقیقه ی ۱۲۰ جهانبخش تو جام ملت ها، تا پنالتی‌ای که طارمی خراب، تا پنج سانتی که شجاع تو آفساید بود، از پنج سانتی که بازیکن کنگو جلو ازبکستان تو آفساید نبود، از پرچم کرنر تو بازی الجزایر، از گل دقیقه ۹۴ الجزایر تا گل دقیقه ۹۵ اتریش، هیچکدوم اتفاقی نبود و همشون کارما بود، کارمای حرفایی که نباید می‌زدین و زدین، کارمای کارایی که نباید می‌کردین و کردین، اینا همه صداهای مردم و آه‌ناله هاشون تو گوشتونه، مردمی که دلشون باهاتون صاف نیست، حالا هی بیاین بگید تبانی بود، نه تبانی نبود، اون بالاسری خواست تا شما به عنوان بی‌غیرت ترین و بی‌شرف ترین نسل تاریخ ایران با حقارت‌آمیز ترین نحوه‌ی تاریخ از جام جهانی حذف بشید :)
#hjAly‌
@HutNewsPlus
|
@News_Hut</div>
<div class="tg-footer">👁️ 8.77K · <a href="https://t.me/news_hut/66993" target="_blank">📅 16:14 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66992">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eIQM-uPy12KcyYUgBE3mioISFRhNqun5z3f6disfdg44e3bYVbWojHThe-CY98_dScLumV5cced1GZQVUMDXeYDe_z3i6lZu5l6tVgtMxO0nDv5CZ0dzmbPQy81CeBTvkaWyAb9dFY8lnxrx8CXtQrdRG0ksYi4gG9mSBpLItMqLxgSKup3ruOArsuPQvmJhmfJlrJO9Cb-S5WxiaUAsWjMnd-QyCd-hXq_iCr2Bz6epsViQAK7D_nBDenYssmCGRf5q07LC9aa6q9CPPRKlaFdZAGEPB-jWxXyhwpdgWKDz3FRrbppX8xhpWtqXmblmP19YcASm4JHbz3h1yx92bw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هواداران حزب‌الله دیشب تابلوهای «لبنان اول» را در جاده منتهی به فرودگاه بیروت به آتش کشیدند.
@News_Hut</div>
<div class="tg-footer">👁️ 9.21K · <a href="https://t.me/news_hut/66992" target="_blank">📅 16:05 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66991">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromHossein ️</strong></div>
<div class="tg-text">🇨🇭
ایران - سوئیس
🇮🇷
مرحله حذفی یک شانزدهم جام جهانی
سشنبه ساعت ۲۰:۳۰
محل بازی : گیم نت محلمون در بازی اف سی۲۶</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/news_hut/66991" target="_blank">📅 15:31 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66990">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">‼️
هنوز تیم جمهوری اسلامی صد در صد حذف نشده
:
تیم های اتریش و الجزیره الان تو امریکا هستند و باید برن کانادا. طبق براورد، احتمال سقوط یک هواپیما 0.00004 درصده که اگر اتفاق بی افته ایران جایگزین می‌شه. یعنی همین درصد ایران شانس صعود داره
😂
😂
@News_Hut</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/news_hut/66990" target="_blank">📅 15:15 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66989">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/572c331047.mp4?token=LQlSYHueaBX-cPCcBsf0uzgqMw-93j2Fa_mk5_pOjfAN9mpYPJvQ2N7Wydx9c2KYGMBvd1VkALBKCoKlB3IElxfo5EYtT_hjpRggojLYeOShrIHJ55vj381C4UXNzh2bXLSGyyYGZI1T6qLqatzldWaqFYwbwteKzGrTL9LxaFGDTo4LNNtOC_mL6cG1Fi54iZPfXDkuO6R3zlY5X2e_bzK-aiJ5E4tWJ2K_2uMXsXe87FEpN27JHqKsmC_dIpfGvEAMA_kqGQL7AAyXUr8lYc9yHE_m87xgpTCLCyTzm_pnOQf_nta8yXn-QheO4gBR_1_5nd0e8VJAGRMUJ4U5NA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/572c331047.mp4?token=LQlSYHueaBX-cPCcBsf0uzgqMw-93j2Fa_mk5_pOjfAN9mpYPJvQ2N7Wydx9c2KYGMBvd1VkALBKCoKlB3IElxfo5EYtT_hjpRggojLYeOShrIHJ55vj381C4UXNzh2bXLSGyyYGZI1T6qLqatzldWaqFYwbwteKzGrTL9LxaFGDTo4LNNtOC_mL6cG1Fi54iZPfXDkuO6R3zlY5X2e_bzK-aiJ5E4tWJ2K_2uMXsXe87FEpN27JHqKsmC_dIpfGvEAMA_kqGQL7AAyXUr8lYc9yHE_m87xgpTCLCyTzm_pnOQf_nta8yXn-QheO4gBR_1_5nd0e8VJAGRMUJ4U5NA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
#hjAly‌
@News_Hut</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/news_hut/66989" target="_blank">📅 14:44 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66988">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d74845b1c1.mp4?token=vZ8zd1JT_hU7av4jYl5RNZzuTMNnZcQmDt2K3b6cX3hJNYMekZq666kiJ6tEE47_iO2SCjQ5bGssTR_pmMtVe-zR5cHfd1KtsYq5TiHS0MfJ-DlJ6ipy1_yCvhx52Z2Vsb6bAygCHkcPxJa8gnNc2qQKbRxHnfSzd86HuqbN3fDejs7PnRzNtJf1II_qG-LiNuKcqYicvU5uAkEwHKRp1Ph2FXA30hn24na-hzOF8RCJG8DoEC3Dz5EszhocTVz2dsKhNKaNsaxiPxFOH93nNOtp_ioXBif8pKA_tsXACfPWaRmb0Ilqe62M3PUS3DBII4pNZAJ9S6sGUqJN0uBUUA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d74845b1c1.mp4?token=vZ8zd1JT_hU7av4jYl5RNZzuTMNnZcQmDt2K3b6cX3hJNYMekZq666kiJ6tEE47_iO2SCjQ5bGssTR_pmMtVe-zR5cHfd1KtsYq5TiHS0MfJ-DlJ6ipy1_yCvhx52Z2Vsb6bAygCHkcPxJa8gnNc2qQKbRxHnfSzd86HuqbN3fDejs7PnRzNtJf1II_qG-LiNuKcqYicvU5uAkEwHKRp1Ph2FXA30hn24na-hzOF8RCJG8DoEC3Dz5EszhocTVz2dsKhNKaNsaxiPxFOH93nNOtp_ioXBif8pKA_tsXACfPWaRmb0Ilqe62M3PUS3DBII4pNZAJ9S6sGUqJN0uBUUA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
خداداد عزیزی دیشب:
ایران با این احتمالات قطعا صعود میکنه اگه هر ۳ تا بازی طوری رقم بخوره که ایران حذف بشه؛
فقط معنیش اینه که خدا خواسته این تیمو بزنه و تنبیه کنه
@News_Hut</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/news_hut/66988" target="_blank">📅 14:29 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66987">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f10176bb5b.mp4?token=YdgQzL6lSgoQ4_9-j3avo_aH9ugoOntoBkWIjCIB2BRvoRTGbMFVlltvDaLouWo3SSME1nyfnyR3X-ojtmVnTWcqC2CUEtACYHaZoiftCzbscYIXljMg-x289Yr_5ZIdJtrjKj4po2raGbDPUlgRzHP3CttUfMqGEQu4mLFvtJC0WxAJMr8ASEsoDQXLZBNVNiOQYoNOjpRoYLAV-huez6PpcGSOaLOirAwt3zF5Nf6eyVlMbV_jQRtlOh-vDBpPhxj5xbEUeIKtPaZ0FLnwteHLyqDnbevs8uokuWxVwB7K3aHidJBak9AO1U1YADsnb7sw2E02Wiz2ZIvAP04LxQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f10176bb5b.mp4?token=YdgQzL6lSgoQ4_9-j3avo_aH9ugoOntoBkWIjCIB2BRvoRTGbMFVlltvDaLouWo3SSME1nyfnyR3X-ojtmVnTWcqC2CUEtACYHaZoiftCzbscYIXljMg-x289Yr_5ZIdJtrjKj4po2raGbDPUlgRzHP3CttUfMqGEQu4mLFvtJC0WxAJMr8ASEsoDQXLZBNVNiOQYoNOjpRoYLAV-huez6PpcGSOaLOirAwt3zF5Nf6eyVlMbV_jQRtlOh-vDBpPhxj5xbEUeIKtPaZ0FLnwteHLyqDnbevs8uokuWxVwB7K3aHidJBak9AO1U1YADsnb7sw2E02Wiz2ZIvAP04LxQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
سخنگوی سپاه پاسداران:
«از اینکه دولت به سپاه نفت داده باشد، اطلاعی ندارم و بعید می دانم چنین موضوعی صحت داشته باشد.» او اضافه کرد: «سپاه برای تجهیز و پشتیبانی از یگان های مختلف خود به بودجه نیاز دارد و دولت موظف است این بودجه را تامین کند.»
مسعود پزشکیان، اخیرا در یک سخنرانی گفت: «اگر ما پشتیبانی نمی کردیم، رزمندگان نمی توانستند بجنگند و ما 20 میلیون بشکه نفتی که به دولت تعلق داشت، به هوافضای سپاه دادیم».
@News_Hut</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/news_hut/66987" target="_blank">📅 13:36 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66986">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/00001b2a3d.mp4?token=Tk9H2xyG7qZdF1Bpd2Pn-XzT1m-oEg5R3e2YSCndA31DLL-3Q7vCtk2EHoUQvAiHol0J9EJVq5WTFqwboj_WApb6NTXnEzlq_p8FCxsy7RANR7rM7G6-XS5eOytQCTi3x4WktQbDh9zkC89prVn4JKg383U9uxAun-p0-Jjshq2HQCBbe85cCQkm0v4deBHOrIyL2tRuAYW3CTw-Blt3zO1L-EQfIOsnLH72GUZYLlR06oG9Dt9WM4I9yDjGJpzDsDG9OAt3ojk-Io9HDE7bT-cFV7N048tpvxQ4PUM8zdS8i0avrJUKq6G7B_LzsbTqd2dODzEy-RMgT5KKLve89g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/00001b2a3d.mp4?token=Tk9H2xyG7qZdF1Bpd2Pn-XzT1m-oEg5R3e2YSCndA31DLL-3Q7vCtk2EHoUQvAiHol0J9EJVq5WTFqwboj_WApb6NTXnEzlq_p8FCxsy7RANR7rM7G6-XS5eOytQCTi3x4WktQbDh9zkC89prVn4JKg383U9uxAun-p0-Jjshq2HQCBbe85cCQkm0v4deBHOrIyL2tRuAYW3CTw-Blt3zO1L-EQfIOsnLH72GUZYLlR06oG9Dt9WM4I9yDjGJpzDsDG9OAt3ojk-Io9HDE7bT-cFV7N048tpvxQ4PUM8zdS8i0avrJUKq6G7B_LzsbTqd2dODzEy-RMgT5KKLve89g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تصاویری از حملات اوکراین به پالایشگاه یاروسلاول در روسیه
@News_Hut</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/news_hut/66986" target="_blank">📅 12:59 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66985">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C210IUSQPHmJrC0gHd6J40wi18_0DQ_Dd6BhKb3cnIjAhlUtpkoQg80Q62fOjF7tS8cblSsaJb5CYjuRssu-GAEoDmdJXcBHGlvQN7JzzAMYdLlp3GLSW7DzvF-0CUVjIWoRh96rwcO7nMJztamMoVsY1okB52jONOZC_5Id50unheNuA4pssY5mIHyeWzJs-WXuFO2khaOGD7IimuQrquAZ52ZRJWpGtV1c2y0XKsyNHiE6FSNbZMUyTDF_DaQFrm4w3cXo-gwIWA0NN_hLMB_ts3qjcmVPsE7aUDMWSWlRUM6Q6ONHYZOfLFdXnJhnioMqUctZVEnsqb_YQuB5OA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚠️
وزارت خارجه جمهوری اسلامی در بیانیه ای حملات هوایی آمریکا به مناطقی در سواحل جنوبی ایران را به شدت محکوم کرد و آن را نقض آشکار منشور سازمان ملل و نقض صریح بند اول یادداشت تفاهم با آمریکا دانست.
@News_Hut</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/news_hut/66985" target="_blank">📅 12:38 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66984">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">‼️
کارشناس برنامه دیالوگ:
این جنگ به مسئولین نظامی و سیاسی نشون داد که توانایی نابودی اسرائیل رو ندارند و چشمشون به واقعیت های میدان بیشتر باز شد.
@News_Hut</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/news_hut/66984" target="_blank">📅 12:15 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66983">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VNcoPS50F0sYADlqbDiN-3LaXvD32AzvGmd-rt4QAV-FHU1OoyHRDv39BOr2Gl44qM5xq8oVr6F0pufSzEQ2liUFMsHgW6e34iNXrC11HmsPptFJ_wHNt7mU-hn_isSiUPOiZEA3d71_1dHO8HH9XmtFNXgxbOlqQxAu29JE41LFzaPlsDG9BymSx8yhgG82B-RBCEzIYskSFRZWaOnOoabDh2d3Vo_wz6r7icfFh49eUNlkPAkvKwIKTUyRSz8s5A0AxEH5Tioy9z7WVH2vAk8XgMkDsLlx3tBHSJfGabBdzPKN6pR0HlSG5IzsUxtAjCrGLLSjAvWnDXjIKo8JCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚠️
۶۸,۹۰۰ نفر در ونزوئلا سه روز پس از دو زلزله کم‌عمق پشت سر هم (با بزرگای ۷.۲ و ۷.۵) که کشور را ویران کردند، به‌ویژه ایالت ساحلی لا گوارا، گم‌شده گزارش شدند.
۱,۴۳۰ کشته، تلفات در حال افزایش است.
نجات‌دهندگان با ماشین‌آلات و دست‌های برهنه در میان آوار جستجو می‌کنند؛ پنجره بقای ۴۸ تا ۷۲ ساعته در حال بسته شدن است.
گرما تجزیه را تسریع کرده است؛ شرایط بسیار وخیم است.
@News_Hut</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/news_hut/66983" target="_blank">📅 11:45 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66982">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8c0f8ca35e.mp4?token=eK1YlnYAPK6X7bno0JjDP7Rm-NVer74xLu_puONCFoD05Y3oC4xm8NUGeC4VGpMlOMK_F2HrngOMBWoKVGzY0hseWkyfVLXbb0Eb7QcEQd-0kXBerhft509p5Z20VtGIgBeFwWl1MPag4-p6Ne7owyYeKZaxcku5S9ZyGWUftlWSku3zkH-dVUadWdtyuUuvB1U0UuIh7NigZlZxje6912ot_M3m-OPNXXvIWO6exqqbF7-VMH0vAPKJbJ_jUKz9-wHpuip8We8F9OOW0kvmoL9f62YKFgZw3ifbAHQTbAb8aJLHqzlVAcV9U_rC44JjFuFvcmAfpoMHEK_Vvb_kdA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8c0f8ca35e.mp4?token=eK1YlnYAPK6X7bno0JjDP7Rm-NVer74xLu_puONCFoD05Y3oC4xm8NUGeC4VGpMlOMK_F2HrngOMBWoKVGzY0hseWkyfVLXbb0Eb7QcEQd-0kXBerhft509p5Z20VtGIgBeFwWl1MPag4-p6Ne7owyYeKZaxcku5S9ZyGWUftlWSku3zkH-dVUadWdtyuUuvB1U0UuIh7NigZlZxje6912ot_M3m-OPNXXvIWO6exqqbF7-VMH0vAPKJbJ_jUKz9-wHpuip8We8F9OOW0kvmoL9f62YKFgZw3ifbAHQTbAb8aJLHqzlVAcV9U_rC44JjFuFvcmAfpoMHEK_Vvb_kdA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⁉️
سعید لیلاز: فکر می‌کنم آمریکا در بهمن یا اسفند دوباره به ایران حمله می‌کند، تفاهم‌نامه یک وقفه است
@News_Hut</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/news_hut/66982" target="_blank">📅 11:15 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66981">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">‼️
گزارشگر صداوسیما وقتی گل سوم الجزایر زد
خدا صدای مردم ایران شنید
😂
خدا دقیقه ۹۵ و حتی یک دقیقه از بازی گذشته بود گل مساوی زد
😂
@News_Hut</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/66981" target="_blank">📅 10:49 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66980">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">‼️
مجلس خبرگان بیانیه‌ای در حمایت از مجتبی خامنه‌ای صادر کرد:
🔴
1. مذاکره‌کننده‌ها باید حواسشون جمع باشه و تحت هیچ شرایطی از خطوط قرمز رهبر عبور نکنن.
🔴
2. تأکید میکنیم که انتقام خون رهبر گرفته بشه و ترامپ و نتانیاهو به مجازات برسن.
🔴
3. اگر طرف مقابل توافق رو نقض کرد، باید سریع جواب داده بشه؛ همچنین باز کردن تنگه هرمز در شرایط فعلی اشتباه راهبردیه.
🔴
4. موضوع برنامه هسته‌ای ایران اصلاً نباید وارد مذاکرات بشه.
🔴
5. کنترل تنگه هرمز، گرفتن غرامت جنگ، آزاد شدن پول‌های بلوکه‌شده، لغو کامل تحریم‌ها و خروج آمریکا از منطقه باید حتماً دنبال بشه.
🔴
6. مسئولان نباید حرفی بزنن که دشمن احساس کنه ایران ضعیف شده.
🔴
7. در نهایت، حرف آخر با رهبره و هیچ مسئولی نباید برخلاف نظر ایشون عمل کنه.
🔴
8. گفته شده دشمن فقط دنبال خریدن زمانه و احتمال حمله دوباره وجود داره؛ برای همین نباید مذاکرات طولانی بشه.
🔴
9. از مردم میخوایم حضورشون رو در صحنه حفظ کنن، اتحادشون رو به هم نزنن و به حرف‌های تفرقه‌انگیز توجه نکنن.
🔴
10.  کنار رهبر و مردم می‌مونیم و در صورت نیاز به وظیفه خودمون عمل می‌کنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/66980" target="_blank">📅 10:33 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66979">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0478c4d3f1.mp4?token=ZTW3mOHtqn8YK7SFQHXpc4fytArdbaQzwq7FEyTUw9FBeXUbBuwvPk4PudRedEUTKJAdeH621esbnDpe3UXeh--TQBh_WznuV35A2ctm4XIriMyPn8JIAROvUjD3kK48RW5Zmc6HvSNkZ7EJngi1RgAmHgqh8km71Q7nxtXTGso6Jt00upKD3XpIyaN__7ecN33Y0VxCs1phoUECdrE23eTSHsRxTrAFRK7Tv9tni9lORmnCvDj-XpNx-nC7JMeTyxnVhx9GtdWl-ulk-goATDDbF3rrBbjBPlCYop4Z7bu2M-dQiES3XwLSy-rOcG9otEeq6cMosW5iYFPdWoJCqA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0478c4d3f1.mp4?token=ZTW3mOHtqn8YK7SFQHXpc4fytArdbaQzwq7FEyTUw9FBeXUbBuwvPk4PudRedEUTKJAdeH621esbnDpe3UXeh--TQBh_WznuV35A2ctm4XIriMyPn8JIAROvUjD3kK48RW5Zmc6HvSNkZ7EJngi1RgAmHgqh8km71Q7nxtXTGso6Jt00upKD3XpIyaN__7ecN33Y0VxCs1phoUECdrE23eTSHsRxTrAFRK7Tv9tni9lORmnCvDj-XpNx-nC7JMeTyxnVhx9GtdWl-ulk-goATDDbF3rrBbjBPlCYop4Z7bu2M-dQiES3XwLSy-rOcG9otEeq6cMosW5iYFPdWoJCqA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
❌
سنتکام:
جت‌های جنگنده نیروی دریایی و هوایی ایالات متحده امشب به دنبال حمله پهپادی ایران به کشتی ام/تی کیکو، به ۱۰ هدف نظامی ایران در چندین مکان در داخل و نزدیکی تنگه هرمز حمله کردند.
@News_Hut</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/66979" target="_blank">📅 10:03 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66978">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🚨
🚨
🇮🇷
روابط عمومی سپاه پاسداران
:
فرزندان شجاع شما در نیروهای دریایی و هوافضای سپاه پاسداران انقلاب اسلامی، در یک عملیات مشترک موشکی و پهپادی در ساعت ۰۲:۰۰ تا ۰۳:۰۰ بامداد، هشت هدف مهم آمریکایی از جمله پایگاه هوایی علی السالم در کویت و مقر ناوگان پنجم نیروی دریایی آمریکا در بحرین را هدف قرار دادند.
دشمن متجاوز که خیانت و نقض معاهدات بخشی از ذات اوست، بامداد امروز تحت عنوان مقابله با نیروی دریایی سپاه، پنج نقطه ساحلی در ایران را مورد حمله قرار داد.
بر اساس تفاهم‌نامه اسلام‌آباد درباره تنظیم تردد در تنگه هرمز با جمهوری اسلامی، از این پس با کشتی‌های متخلف با قدرت بیشتری برخورد خواهد شد و هرگونه تجاوز احتمالی دشمن به هر بهانه‌ای، حتی مشابه حملات دیشب به اهداف کم‌اهمیت، با پاسخی ویرانگر مواجه خواهد شد.
دشمن باید بداند که نقض آتش‌بس برخلاف بند ۱ تفاهم‌نامه اسلام‌آباد است و منجر به توقف کامل مذاکرات خواهد شد.»
@News_Hut</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/66978" target="_blank">📅 09:27 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66977">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p6w2g2W4e01xU4gGGrQ8BB390hTfO805-te3RdWdMZnuBlW29Wt32p3z9uQAmRcCFpRPHG-mMK1QmZgGETJkdT01jD5_kaE6oK5FE9dB7QX9x_82LDsstSuEv9Kd3JStEMWVi2Gx5Kjtit_qcbYRURrZsv-XBIl52vg1KPaVstiO4W00PW99MU7Ht4uz4NFi-aS1kzUphbmRPryDym9BzltleYtbscYHSXTkWuNmGqlDrFX2wrRR4A_0jZCVn0o0bfu-EFl0ddhxKXQkdievmxZiHuKlsuMYZNJwUSRCeBucg9m3u2JrtsFu1zG58ANrMAFDht7OHB1iXGrU-6PQfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇺🇸
پرزیدنت ترامپ:
هواپیماهای ایالات متحده به تازگی به دلیل نقض توافق آتش بس، به انبارهای موشک و پهپاد ایران و سایت‌های رادار ساحلی حمله کردند! بسیار محتمل است که آنها هرگز درس نگیرند! ممکن است زمانی فرا برسد که دیگر نتوانیم منطقی باشیم و مجبور شویم کاری را که با موفقیت آغاز کرده‌ایم، به صورت نظامی تکمیل کنیم. اگر این اتفاق بیفتد، جمهوری اسلامی ایران دیگر وجود نخواهد داشت!
@News_Hut</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/66977" target="_blank">📅 09:05 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66976">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">حداقل تا اونجا رفتید صد کیلو از اون ذرتای ترامپو بیارید الکی نرفته باشید.
😂
@News_Hut</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/66976" target="_blank">📅 08:43 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66975">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/df26bad47c.mp4?token=ApQDuf-14p1LsOOdjp2V-uds7W03fgvGHO4JqP3OEC0ownbegu5zCRXnuumpboS3D-ykjfARNO_fQXBb5O8yVgSJThpr9CyEy3t1UUbQ5nc9K5CieJR1IzFtyHsdVFN3Js2YofgKTx2VkV_CaeifcecocOdCf5o6lCgQpQmZqa8-_gqvg-vC4ruCei_G4phY87O6UrhJdS87oXJM2VsfPAgjikj_8-aAaZ5jdo42xQP-Mjhujy6gWMifXMfJL6B71kZ5Ss0eSP5e1yv0nPwWpwAAearYrAxRau4PIrzQG41sK3H3oSvW9hy_456LXAvjYIM15w4M371KdxhnOe9PsQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/df26bad47c.mp4?token=ApQDuf-14p1LsOOdjp2V-uds7W03fgvGHO4JqP3OEC0ownbegu5zCRXnuumpboS3D-ykjfARNO_fQXBb5O8yVgSJThpr9CyEy3t1UUbQ5nc9K5CieJR1IzFtyHsdVFN3Js2YofgKTx2VkV_CaeifcecocOdCf5o6lCgQpQmZqa8-_gqvg-vC4ruCei_G4phY87O6UrhJdS87oXJM2VsfPAgjikj_8-aAaZ5jdo42xQP-Mjhujy6gWMifXMfJL6B71kZ5Ss0eSP5e1yv0nPwWpwAAearYrAxRau4PIrzQG41sK3H3oSvW9hy_456LXAvjYIM15w4M371KdxhnOe9PsQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">من دور خونه بعد از گل سوم اتریش:
#haa4m
@News_Hut</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/66975" target="_blank">📅 08:43 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66974">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">خانواده ۴۰ هزار جاوید‌نام امروز خوشحال شدند، میلیون ها ایرانی باشرف امروز رو می‌رقصند، روحت شاد مهران عزیز، امروز رو خوشحال باشید، بزنید و برقصید که عزیزای ما تو آسمونا خوشحالن، تا می‌تونید این بیناموسارو ترول کنید، خوب و بد ندارن همشون یه گوهن، نفرین میلیون…</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/66974" target="_blank">📅 08:37 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66973">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e8a4cb5436.mp4?token=m2h7xm_t65kOvhxv2d7UZTwhwP9TQ0tts12pQre1AZGiP41O9lktTW6Mk1RwF_giZagBYzqP7O2C_FkLYa5CnyBoaZH3OFz2iW0pZv7DDjeV7qWuA6o51P5xB5Zr14CL50bG1MNQGmalEg6duXvfd0ebZUuMqtzNIC2fG4QliGOOl_TNgBxLcSp7qttV6EXcWYvczBjUY2Y_Xo-RiZi8wldIw45y4NoX22QrrkvIokxRrUTRRCtvUC6MvOUwZrzH9TALYlnEwy4N-V3SUFXDoRyJuAkNQytERzLk9VDpSEugdDrw6CDe8sOGtpjqT0vZvCOAI327s8V0jjtxbUFDpw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e8a4cb5436.mp4?token=m2h7xm_t65kOvhxv2d7UZTwhwP9TQ0tts12pQre1AZGiP41O9lktTW6Mk1RwF_giZagBYzqP7O2C_FkLYa5CnyBoaZH3OFz2iW0pZv7DDjeV7qWuA6o51P5xB5Zr14CL50bG1MNQGmalEg6duXvfd0ebZUuMqtzNIC2fG4QliGOOl_TNgBxLcSp7qttV6EXcWYvczBjUY2Y_Xo-RiZi8wldIw45y4NoX22QrrkvIokxRrUTRRCtvUC6MvOUwZrzH9TALYlnEwy4N-V3SUFXDoRyJuAkNQytERzLk9VDpSEugdDrw6CDe8sOGtpjqT0vZvCOAI327s8V0jjtxbUFDpw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تا ابد موندگار شد این سکانس
😂
😂
😂
😂
😂
😂
😂
😂
@News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/66973" target="_blank">📅 08:24 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66972">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn5.telesco.pe/file/b5b527c33c.mp4?token=gJxuJsSJmoBmMWwHuMpKa-MjHDsBYLv_wAsWwN2YSViDc1b5y_IAYrWcU_VofhGZcA87Io20KiFT1fmKx5lF0j3B5sQPYHCk5xaFhIlX4VE54UsyGw56jNYGdCENmfJY1q0a7F6W6Tf0wzv3xDIRTt-pn3HgwuxwumTegEmMQ8T4mQCRUP3GuH7qq7fewjp4_ovb42CKxGWN1x9_LcOKbc_E1VfjqMsCLYDCJ5ab5YzlfS3mXA1ITdkkyUpcvJ0DbGLKhdsiIWqp-bVj_smps9VSnSEbDfuJ8yFsR4yB1kczFn0xWMxTmSPuUL0IXwG9g-JT9iadxH70s9HMXluSeg" type="video/mp4">
</video>
<br>
<a href="https://cdn5.telesco.pe/file/b5b527c33c.mp4?token=gJxuJsSJmoBmMWwHuMpKa-MjHDsBYLv_wAsWwN2YSViDc1b5y_IAYrWcU_VofhGZcA87Io20KiFT1fmKx5lF0j3B5sQPYHCk5xaFhIlX4VE54UsyGw56jNYGdCENmfJY1q0a7F6W6Tf0wzv3xDIRTt-pn3HgwuxwumTegEmMQ8T4mQCRUP3GuH7qq7fewjp4_ovb42CKxGWN1x9_LcOKbc_E1VfjqMsCLYDCJ5ab5YzlfS3mXA1ITdkkyUpcvJ0DbGLKhdsiIWqp-bVj_smps9VSnSEbDfuJ8yFsR4yB1kczFn0xWMxTmSPuUL0IXwG9g-JT9iadxH70s9HMXluSeg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خانواده ۴۰ هزار جاوید‌نام امروز خوشحال شدند، میلیون ها ایرانی باشرف امروز رو می‌رقصند، روحت شاد مهران عزیز، امروز رو خوشحال باشید، بزنید و برقصید که عزیزای ما تو آسمونا خوشحالن، تا می‌تونید این بیناموسارو ترول کنید، خوب و بد ندارن همشون یه گوهن، نفرین میلیون…</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/news_hut/66972" target="_blank">📅 08:15 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66971">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EBU7RwmWLYFhOfkdWQUz-qxadcSZm_WW13_u8wLSte_UdXHMc1fWlkrhEeGlM4r129F_4pDNfkblsH-JhGmYFWwJxUA4yIniZKtdkyN-H4PKkBLRz8S90XCSj1ZwmNmOPoninLFFOMo-_AXCK8VMHMA0q6QG77MOUka6mZhA6JYxGCXTPbubb1GySDAr8HljVhQTo0M0ICZRGDW7sxsvJ-txWTP3B766okZDrsDoPCZGc4OuCFazoESSJhrBesjTC6vR0E9zJIZ7O8IRVOnx3Ni-l09G9X1G35usCwAtCv2sLM5Iprd9wg2qGAVDE8ztDSRaLdpzqLSPLSLdq4bAVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خانواده ۴۰ هزار جاوید‌نام امروز خوشحال شدند، میلیون ها ایرانی باشرف امروز رو می‌رقصند، روحت شاد مهران عزیز، امروز رو خوشحال باشید، بزنید و برقصید که عزیزای ما تو آسمونا خوشحالن، تا می‌تونید این بیناموسارو ترول کنید، خوب و بد ندارن همشون یه گوهن، نفرین میلیون…</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/news_hut/66971" target="_blank">📅 08:15 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66970">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">‼️
🇮🇷
خبرگزاری سپاه پاسداران(فارس): بازی اتریش و الجزایر تبانی بود!!!!  @News_Hut</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/66970" target="_blank">📅 08:12 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66969">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nZ6feZKRmim8_1D6bAI87hfhFQK8m1-Z2T_42D83E223J3BsUABoxPHMv0hPAId_NSvSfT0oIOnX7_1rPxgEjDbtQ71vHg_jHlk3KIHb7F2LsE4DwsJi50cXNtAPLfZBF3296FWahY6Xb-dJgl2Aps0vrjLg5DTAy2z-h6zn8IZ3jl7TWPDmgwWwf0t8i5hwn_209ESxK8qAnyrFI1xDfb-llRAUqrXej9L0AHX4QIagVhCGLPXn-IVWlEWzrn4EWye0cIb-GDqJs5yc7sbbf3oO2ejQ_Go44gKHov81KdgTG4OGwvqj9kTeTUgKXWwtReCEU2zIHf_YuDqQD6oICQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وای
😂
😂
😂
😂
یکک دقیقه مونده بود
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
اتریش
😂
😂
😂
😂
😂
دقیققققه ۹۴
😂
😂
😂
زدددددد
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
#hjAly‌</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/66969" target="_blank">📅 08:05 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66968">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UqoxwBOVH3bZ4NE3ZnEiYRC5O2jJNFNiKapyqUpZmJmylhsLKMyRZqfLwFksBlDqkn8XxNfiQGWG_kHEJWx_jLFbVA_z8C0Czz-OXjFU7ozk2cFjO9ws7aAsCcE0ddneF55Xv-HU8mNPceNh5MXtXTq5aXKjHtzlAc7O4-ezU3M-38LR0c8T0Zk1n-suJYi0Z4fkQEzxcqZ71QoMtcA2xQHAYkn0aNXi1PaeUtCuzlbWx7A9w5R_KObljadmKvqkmFrPfFfFuNUrdeojC20w5wnw_LaL7Hju1q57AEdZCu-0wGQx9EQVawD-cwVoqxFhqAOJYVSgYKSbJPCdl1VOjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برادران دست به‌یکی کنید نتیجه همین بمونه، درود خدا بر شما شیرمردان مساوی‌خواه
😂
#hjAly‌</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/66968" target="_blank">📅 07:40 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66967">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jqerpUu2DIWjPn0g3f5QHHmBX2b8e1UMs_NcHPzLCGh5gwnYRuBz8mpcqnhx9MY79FR56vRg3FHcXKj1o6cz_drcHZ40nDd8_lnvljCF11G77Licrs_aKnW8idfgbLFcGS1JRMM8pW8eQ1Ey1XL8smhbp_jnM7eDCdIxaoMvxb-FAmKbeaBU6smF4H0ZWf2jwvnThk4M7DCIpGZEIdiQF3pOihceMcTU7diGopxRK1W2hnBsMVyngh-9wJHl3r-LF0BphRtY-rz6bD-DoRhpY_RnAH8p9DKKuHGk6F-_3INh3DA5IUkSz_MUuiwvO19PNI3XDpeAssqTJRwB6zngyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برادران دست به‌یکی کنید نتیجه همین بمونه، درود خدا بر شما شیرمردان مساوی‌خواه
😂
#hjAly‌</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/news_hut/66967" target="_blank">📅 07:38 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66966">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a46a2e94ef.mp4?token=jhcBBzy1JLM3LrKgAk61erAWgdZgyyYtzbdrHIKNgpiU32r7w3akEeRrmb1pQlgrjiGjPrupEfUPXzPbOggbMUqX-Ivqd3OcPgInbKmsVVvYdGbnUw64jm4Id3qAUXE0dk3dylPS-67qGeqBOy6Mwr8Ikr8OfIIYGcOMflSmgl3vfXEOJqzSuAMOAymaTKhy11W5gXDhuXl0QuTJj_7QY2_WeoJvdlnzID-AHCdLvvHgY0f2UPwa1jq2o98wRhwlnQ0fJw6R8P9DzOPiUfsYxvLhAXB0N_Tg7--64lcPujNC9jHPV6wR6t4z44bTEVrqbA_jLVwuWt7fy6pxqxi5uw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a46a2e94ef.mp4?token=jhcBBzy1JLM3LrKgAk61erAWgdZgyyYtzbdrHIKNgpiU32r7w3akEeRrmb1pQlgrjiGjPrupEfUPXzPbOggbMUqX-Ivqd3OcPgInbKmsVVvYdGbnUw64jm4Id3qAUXE0dk3dylPS-67qGeqBOy6Mwr8Ikr8OfIIYGcOMflSmgl3vfXEOJqzSuAMOAymaTKhy11W5gXDhuXl0QuTJj_7QY2_WeoJvdlnzID-AHCdLvvHgY0f2UPwa1jq2o98wRhwlnQ0fJw6R8P9DzOPiUfsYxvLhAXB0N_Tg7--64lcPujNC9jHPV6wR6t4z44bTEVrqbA_jLVwuWt7fy6pxqxi5uw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">برادران دست به‌یکی کنید نتیجه همین بمونه، درود خدا بر شما شیرمردان مساوی‌خواه
😂
#hjAly‌</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/66966" target="_blank">📅 07:30 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66963">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">ریدم تو هرچی الجزایریه، دقیقه ۹۳ گل زدن و تیم منتخب ج.ا صعود کرد #hjAly‌</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/news_hut/66963" target="_blank">📅 07:29 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66962">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">باااازی مساوی شد، دروووود بر شیرمرددددان الجزایرییی، فرزندان برحق رباااح ماجر #hjAly‌</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/66962" target="_blank">📅 07:26 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66961">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">ریده شد توش و اتریش زد
😂
با این نتیجه منتخبِ ج.ا صعود می‌کنه #hjAly‌</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/66961" target="_blank">📅 07:00 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66960">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">برادران دست به‌یکی کنید نتیجه همین بمونه، درود خدا بر شما شیرمردان مساوی‌خواه
😂
#hjAly‌</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/66960" target="_blank">📅 06:48 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66959">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I_Uuek9i9C2ohqhJBKm63Rjh_GqEOGWqWvJJ66fTuHsWEA78-iA00JSEJKcBnQ4FJ7UEbv0ecWPQrRE7r-K02hmkMJ_V_m7z9rwQGDNqZ1-Pw2YuCVcqLs_ZiPd2KyH_S_zXWvX_L0b1Bdsm9xw0MxFubm3dg7eAlDO3Jeq86raD1oreDAJHItMbPBxUNcm1ta7ITqzqKtiCYbs8mcqaTXlslQNKOVCdKsBKqaI4ZD0gwaU3uoeBZVQQaNCFuGSylB92MUItdRXE8CwnxUZ12Xj-gtWh7qjV__8ewEFm1xKqD86yhNbX3DgxtwgXWKcYUxWx75YW6BnT_sL58kW-4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برادران دست به‌یکی کنید نتیجه همین بمونه، درود خدا بر شما شیرمردان مساوی‌خواه
😂
#hjAly‌</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/66959" target="_blank">📅 06:38 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66958">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet @FutballFuckBet @FutballFuckBet @FutballFuckBet</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/66958" target="_blank">📅 02:30 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66957">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/iJwKChUIat7pnRdob9lS3hG31d-IYIRrmvfiGn7PESzwTrZmhWujJuVP8ND9_qa7CU72TVae_3nXcJeieEfBJQ47zuqa2PwwZQpIpaJSGB-gfAw9yrUARcw62kw_hTWt3z9LiJenPvnEqFPPf1iCUBmiAdrzIldktWbugWjcE8m7g8nra2rcL7tB3h6CtNPUDcwhe57DAdC4nolaGM2psUx6XQPLLjziguNClHWlJoo1kxMz1oIJDCnFiIpyf07CqlyU_BbXKhz3lcOhKEtq96Z0xbCBAyiViHUo4nR5QTzjBh5CJqwIFjkOwQqa6l_U35Cd9Fho4Jh6_PJwIVAvUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/66957" target="_blank">📅 02:30 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66956">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">‼️
❌
صداوسیما:
جزئیات عملیات امشب نیروی دریایی سپاه علیه دشمن آمریکایی تا ساعتی دیگر به طور رسمی منتشر خواهد شد
@News_Hut</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/66956" target="_blank">📅 02:07 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66955">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">‼️
❌
مقام آمریکایی:
ارتش آمریکا سامانه‌های پدافند هوایی، انبارهای نگهداری پهپاد، موشک‌های کروز، رادارهای هدایت آتش، توانمندی‌های مین‌گذاری و سامانه‌های موشکی زمین به هوا را هدف قرار داد
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/66955" target="_blank">📅 01:49 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66954">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🚨
🚨
🟥
فاکس نیوز به نقل از مقام آمریکایی:
حملات هوایی امشب به اهدافی در ایران به پایان رسید
@News_Hut</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/66954" target="_blank">📅 01:44 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66953">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🚨
🚨
خبرگزاری مهر:
شنیده شدن صدای چند انفجار در بندر لنگه و بندر‌کنگ
@News_Hut</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/66953" target="_blank">📅 01:35 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66952">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🚨
🚨
🚨
🟥
فاکس نیوز به نقل از مقام آمریکایی:
نیروهای آمریکایی و بحرینی ۹پهباد ایرانی را که به سمت نیرو‌های آمریکایی در بحرین شلیک شده بود سرنگون کردند.
@News_Hut</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/66952" target="_blank">📅 01:30 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66951">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🚨
🚨
🟥
فاکس نیوز:
حمله کنونی آمریکا بزرگتر از حمله ای است که دیشب رخ داده.
@News_Hut</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/66951" target="_blank">📅 01:27 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66950">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N0NxHREaodpwG4MNN570EhCeEFrStaciEBsdl4pSmV2hK8BL2v1n9HSkkAPGeSUY-Fp_sjR-JHA1KXyeVF09O_IytDIFmhzjoE7wmc3AkOUhyRB6xg3v96zuhCzn-FjYJwtqYy3eBSFjUwzpNMxjrr-tX-WR6uREWmLHlsTpT75aKPsYOqBol7m88LLQ4AWm-oaxg63h2IAau6SsV24SwHIH48RFbxu6RVpCWXLagObWR0VqLMHBwpTNkueMLwmWo17r9BqBRmkqPmaja86G6TU-ZYg7asov4kSz8jEiVvd-XYZqPQFuVqcWWBW7LvOrYf3qjPH-lJsPRf-eH9LPOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
#فوری
؛سنتکام:
پس از حملات دیروز ایالات متحده در پاسخ به حمله ایران به کشتی ام/وی اور لاولی، به ایران فرصتی داده شد تا به توافق آتش‌بس پایبند باشد، اما وقتی نیروهایش ساعت ۴:۳۰ صبح به وقت شرق آمریکا یک پهپاد تهاجمی یک‌طرفه را به سمت کشتی ام/تی کیکو شلیک کردند، این فرصت را از دست دادند. این نفتکش با پرچم پاناما در نزدیکی تنگه هرمز با بیش از دو میلیون بشکه نفت خام در حال عبور بود.
نیروهای فرماندهی مرکزی ایالات متحده امروز در پاسخ مستقیم به ادامه تجاوز ایران به کشتی‌های تجاری، حملاتی را انجام دادند. هواپیماهای نظامی ایالات متحده زیرساخت‌های نظارتی نظامی، سیستم‌های ارتباطی، سایت‌های پدافند هوایی، تأسیسات ذخیره‌سازی پهپاد و قابلیت‌های مین‌ریزی ایران را هدف قرار دادند.
@News_Hut</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/66950" target="_blank">📅 01:21 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66949">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">🚨
🚨
🚨
خبرگزاری فارس:
صدای انفجار در سواحل سیریک
دقایقی پیش مردم در سواحل و محدودۀ ساحلی منطقۀ طاهروییه سیریک صدای چند انفجار شنیدند.
همچنین اهالی مسن در قشم نیز از شنیده‌شدن صدای چند انفجار در این منطقه خبر می‌دهند.
@News_Hut</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/66949" target="_blank">📅 01:14 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66948">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EsLpWkvZaQPZ94jeAo1Tmt_wQ4G25d_GrNv6KQNIRP1FZGf-kCueIG-iiiPcCDxyztIfPAcHz8cIyj9ay-JRmBTXz0FF5_Bevn7BWHeV6njqkL-uefyK3LXWGGQcYr7DYu0yOGkZ0AYZNbX20Q-mp9mufGMw2ilbNwYUSfotQdTIKKsljMxamYAzkzL1VvqySAaH0tc6qNC_ANbfFdqO1Dj_qxaWki8Mun-SpFWiFfRKkeaY-6HnShcNxwPp5KQe_FxONoSFYVtcsElEzto2q6rVN3XLjSRM48IqeKPML5JxBp4MoaF15BLIWmpUi12aFhGBW88nrK0DliSOs1pLoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
باراک راوید اکسیوس:
یک مقام آمریکایی اعلام کرد که ارتش آمریکا در تلافی حمله صبح امروز ایران به یک نفتکش تجاری، در حال انجام حملاتی به اهداف ایرانی در منطقه تنگه هرمز است.
@News_Hut</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/66948" target="_blank">📅 01:09 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66946">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🚨
🚨
🚨
صداوسیما:
شنیده شدن صدای چند انفجار در سیریک هرمزگان
@News_Hut</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/66946" target="_blank">📅 00:55 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66945">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DVBpksfzHuLkPKC7k6BpAhud7u3i36zA2wnqAuOTQpyVnhvxsQWfHIgD-eeaxJVBsUKROTYjLBw82WKvVfNcFKwQTCY67YXfb_jW2cjyOLR8ppSrL9AE6p475MxWcjtX95sVTkONE7ZM8iB11s0yDHnpgW1MBlNkoIRTAQYKHVdsEgHLakvlP6EHJb47vuesxfdrPrLdLsEPvQ7TIvEBVv7U7BzYmlyMP_Bvx4ggawvo6Q9Xd35kAx6JnOxdlxwfzjsg-o2I_2X5HbUNHJQDPrFpbEkUTvhcXeUKZD28CdqAUQqh8dmzKCNJDmYsOR7KN-K5By5-iA3BeEYx1i7_Lg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚠️
به گزارش وال‌استریت ژورنال، یک مقام آمریکایی اعلام کرده است:
🔴
در جریان حمله روز شنبه به بحرین، دو پهپاد ایرانی شناسایی شدند.
🔴
یکی از آن‌ها توسط سامانه‌های پدافند هوایی زمینی سرنگون شد.پهپاد دوم بدون اینکه هدفی را مورد اصابت قرار دهد، در منطقه‌ای دورافتاده از یک فرودگاه به زمین نشست.
🔴
این مقام همچنین مدعی شد که:
یک پهپاد ایرانی به یک نفتکش حامل ۲ میلیون بشکه نفت خام در نزدیکی تنگه هرمز برخورد کرده است.
🔴
نیروهای آمریکایی نیز دو پهپاد دیگر را که به سمت کشتی‌های تجاری در حرکت بودند، رهگیری و متوقف کرده‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/66945" target="_blank">📅 00:26 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66944">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f6515f9747.mp4?token=PhXu3JIjfBlTjKaWmyuUSiwLpo7JBqM7b8hrWocUtEMxKdaR_JlZh_4AYIAuDBTE1QNC3RYp72jAd1VJfyc2VhBTRPLymA2rdvUENb7_Toc4MGUCLQiVakdNSAWtay44pK1IMi6ZZZe9iFObaSen6TQZoshQxSRYH_WlICJe9L8GO3lUym5zwYJ3hdSXeC76vYL8FTc5qnIooNCAlc1UOB7xWQJ_gPPbzfQ_i2rgNlXUN0gTji7fbqSk03h1Bgu_6QviYThKnf1hYyStKlcKZBrp0gufJVR8bHfmu0_LoeYUm0rXowqA6UPzUDfUWbLvvwwmLjkSqFbTLImcEDHmnw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f6515f9747.mp4?token=PhXu3JIjfBlTjKaWmyuUSiwLpo7JBqM7b8hrWocUtEMxKdaR_JlZh_4AYIAuDBTE1QNC3RYp72jAd1VJfyc2VhBTRPLymA2rdvUENb7_Toc4MGUCLQiVakdNSAWtay44pK1IMi6ZZZe9iFObaSen6TQZoshQxSRYH_WlICJe9L8GO3lUym5zwYJ3hdSXeC76vYL8FTc5qnIooNCAlc1UOB7xWQJ_gPPbzfQ_i2rgNlXUN0gTji7fbqSk03h1Bgu_6QviYThKnf1hYyStKlcKZBrp0gufJVR8bHfmu0_LoeYUm0rXowqA6UPzUDfUWbLvvwwmLjkSqFbTLImcEDHmnw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ویدئوی مسخره کردن خوشحالی بعد گل آفساید شجاع خلیل‌زاده توسط مصری‌ها به سرعت در فضای مجازی در حال وایرال شدنه
😂
😂
@News_Hut</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/66944" target="_blank">📅 00:03 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66943">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e4f9e086cf.mp4?token=nqPEOzzazXWE8qDGS0LpXKu42vxhoNrgAJCo573gBuVm0EEcDW0isuV5xwwemy8fuUBX-g4-9fr1_J7yu-1FjBqsLhVxZHnsyshbz0sIuvtRaAXqTe8ENHBCPCLlsYf8o4fAybqSRymwq7SwusKOoHs-eMZ98FceV60MTMUhW84TqDCePBCP7a78ARvqFERZUZuss8Z-T2_4A7Et0ocMmtQa4sMp4l-kppi6vXt4SnUOdkTSW1z_BfXshkkCYOrJiNPISQEnyW7LW3e79V8hqZmyEgOcf-WT_S97f7t2I8P2-Vw7C5EZP02KyGGtoKm0-hqhvFmaZTc0UESrM0vkwA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e4f9e086cf.mp4?token=nqPEOzzazXWE8qDGS0LpXKu42vxhoNrgAJCo573gBuVm0EEcDW0isuV5xwwemy8fuUBX-g4-9fr1_J7yu-1FjBqsLhVxZHnsyshbz0sIuvtRaAXqTe8ENHBCPCLlsYf8o4fAybqSRymwq7SwusKOoHs-eMZ98FceV60MTMUhW84TqDCePBCP7a78ARvqFERZUZuss8Z-T2_4A7Et0ocMmtQa4sMp4l-kppi6vXt4SnUOdkTSW1z_BfXshkkCYOrJiNPISQEnyW7LW3e79V8hqZmyEgOcf-WT_S97f7t2I8P2-Vw7C5EZP02KyGGtoKm0-hqhvFmaZTc0UESrM0vkwA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
⭕️
صادق خرازی: یک سرویس اطلاعاتی خارجی مدعی شده کمال خرازی در بیمارستان هدف ترور قرار گرفته!| کمال خرازی را به صورت استنشاقی در بخش عمومی ترور کردند
@News_Hut</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/66943" target="_blank">📅 00:02 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66942">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/02e1890541.mp4?token=lPwaHDl0sOjY588K-7TJAlhSRzyGA0yqLrOW2IZdJK0inCyBHtsNsEHFX07fnOcxc6EJcHr241ISv_5lCJPpsFhXt_ShcY5kY5X5y43-cJIG_8uOr8CJ8RgzcH0ybvOgqItCMd7gWi4jKhPkVVAflyzUQvC1vA9aBxHUiDPQ3tazvh0N_oIclu_ehdCXbHNytFz0g88WYjcrw7U8pfuHIxXCNFlrpCNF78gHtrktpnAvLvPRZXBVKmtkBjvcc72QHPWCKFIJiwAkNxOBZfz6Bhr3yri4YSFXoQQIgMdMK94DCJw91sn2RtP9ylFrjKipvHtqtwkymwXwVxllgSXydA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/02e1890541.mp4?token=lPwaHDl0sOjY588K-7TJAlhSRzyGA0yqLrOW2IZdJK0inCyBHtsNsEHFX07fnOcxc6EJcHr241ISv_5lCJPpsFhXt_ShcY5kY5X5y43-cJIG_8uOr8CJ8RgzcH0ybvOgqItCMd7gWi4jKhPkVVAflyzUQvC1vA9aBxHUiDPQ3tazvh0N_oIclu_ehdCXbHNytFz0g88WYjcrw7U8pfuHIxXCNFlrpCNF78gHtrktpnAvLvPRZXBVKmtkBjvcc72QHPWCKFIJiwAkNxOBZfz6Bhr3yri4YSFXoQQIgMdMK94DCJw91sn2RtP9ylFrjKipvHtqtwkymwXwVxllgSXydA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
قالیباف گرفت رو تندروها؛
اینایی که سوپرانقلابی و تندرون؛ هیچ غلطی برای این انقلاب نکردن. پس حق ندارن حرف بزنن و طلبکار باشن. دهنشونو باز نکنن و سرشون تو کار خودشون باشه
😂
😂
@News_Hut</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/66942" target="_blank">📅 23:24 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66941">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">⚠️
🔴
مارک لوین خبرنگار نزدیک ترامپ:
اگر این رژیم در ایران می توانست، تک تک شما را که در این اتاق نشسته اید بکشد، تک تک شما را می کشت.
هر زن که در این اتاق بود به آنها تجاوز می کرد. تک تک.
اگر اینجا نوه داشتی آنها را می کشتند.
آنها را سلاخی می کردند، تک تک شما در اینجا میکشتند چون یهودی هستید یا مسیحی یا فقط یکی از آنها نیستید.
@News_Hut</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/66941" target="_blank">📅 22:58 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66940">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0c163cfe19.mp4?token=odBSejMltU0AbiivnB3ex3raXcMDla6e98ulYZZaVZu8qbyIZ8QqjoO8jhg7RUmjImEXSLc-W83lubKUSRSxjEgEdngOm6AbkqEt23XVfUOHiomwePEltrED2tRzkWyJPx9BxmG9mInwfofprFpco6pnD0e30Huml1Y3vSArk_xDWUI3ph3JZtr4UQFnkqREuRX6vg-7YP8_1Oq_qcS3_4FyKyKk7hqrI3GD_rq0jLZDNCp2MKjhxvhVTvltMpjmcmDqNILTTegiu-UpVYfgNZqicm2gvoNwGryRcVJBDiD-hKt_ktw2nYMnaYUDYo0xhH9gfp-ySuz24xzvzRkwS4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0c163cfe19.mp4?token=odBSejMltU0AbiivnB3ex3raXcMDla6e98ulYZZaVZu8qbyIZ8QqjoO8jhg7RUmjImEXSLc-W83lubKUSRSxjEgEdngOm6AbkqEt23XVfUOHiomwePEltrED2tRzkWyJPx9BxmG9mInwfofprFpco6pnD0e30Huml1Y3vSArk_xDWUI3ph3JZtr4UQFnkqREuRX6vg-7YP8_1Oq_qcS3_4FyKyKk7hqrI3GD_rq0jLZDNCp2MKjhxvhVTvltMpjmcmDqNILTTegiu-UpVYfgNZqicm2gvoNwGryRcVJBDiD-hKt_ktw2nYMnaYUDYo0xhH9gfp-ySuz24xzvzRkwS4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇮🇱
بنیامین نتانیاهو:
دیروز تهدیدی بسیار دورتر از سربازان ما وجود داشت - نه در برد فوری.
آن‌ها هفت تروریست را دیدند که وارد خانه‌ای می‌شوند. آن‌ها هنوز شلیک نکرده بودند و هنوز خود را سازماندهی نکرده بودند.
اما آن خانه نابود شد و آن هفت تروریست حذف شدند.
@News_Hut</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/66940" target="_blank">📅 22:30 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66939">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b35c79910d.mp4?token=t1gvIQhcrCBxk8jEnh8ypRm1RevsR1TyRA85k9w4XXJuRq8tYKNKz9D9lasCjGZtq9Ap_DHqBQ1LBOZ_RJphmdovmWNY8fJkLq-GhYnWmXJYFGfcpNZLkCij6Nf4AlAnfem8TcWgYM-CeoeLQoDxGY9RCKpifdw1gVUfUexncvYfe4qThboDKfAE80fXCzjHyOZhaZOZ4zHCbxeyzK7275aEb7jD9o4vai1jsfCl0j21mdjtWKS061lzgWQvE0Fv8Bm6nUt63v7CVH4_v7AF0v2DKTK9mYMN37ITvwZO6csQsmk2zCJqiMqsu_nXk2THe9ILeJ-5bfQVPlljWlWej4L_JgXowkzb3lFmYDGWrTg2sA0lzfD1ywe92SgDrMd8t1aZ0JIrbIeEcUsK5UUjEBmPRKND8FYPgTYPl6btGLfuphuBVDKcGCedKrlQl-nC63kr7hJNR6POcsLNHzrMmeQGS46Rw4MhcEn1VOgZ45YII4EAGSc3C7Jle5FU3qyS0m_KaMUladQbOcrU93P5MZcxK6HtJ8Whqf26Fc_3vATNF4tdLDiJ1hCevIkWEWzoCMGRNiBTaYkwtdus6XWbwOKhOoINl7SR4jttlMg3AzZcrx4sBeEJ9FOVG9_EgFOF7z0zG9u0rmu2wXvLRMgl2Hg133_K9DeBIIj05N9cas0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b35c79910d.mp4?token=t1gvIQhcrCBxk8jEnh8ypRm1RevsR1TyRA85k9w4XXJuRq8tYKNKz9D9lasCjGZtq9Ap_DHqBQ1LBOZ_RJphmdovmWNY8fJkLq-GhYnWmXJYFGfcpNZLkCij6Nf4AlAnfem8TcWgYM-CeoeLQoDxGY9RCKpifdw1gVUfUexncvYfe4qThboDKfAE80fXCzjHyOZhaZOZ4zHCbxeyzK7275aEb7jD9o4vai1jsfCl0j21mdjtWKS061lzgWQvE0Fv8Bm6nUt63v7CVH4_v7AF0v2DKTK9mYMN37ITvwZO6csQsmk2zCJqiMqsu_nXk2THe9ILeJ-5bfQVPlljWlWej4L_JgXowkzb3lFmYDGWrTg2sA0lzfD1ywe92SgDrMd8t1aZ0JIrbIeEcUsK5UUjEBmPRKND8FYPgTYPl6btGLfuphuBVDKcGCedKrlQl-nC63kr7hJNR6POcsLNHzrMmeQGS46Rw4MhcEn1VOgZ45YII4EAGSc3C7Jle5FU3qyS0m_KaMUladQbOcrU93P5MZcxK6HtJ8Whqf26Fc_3vATNF4tdLDiJ1hCevIkWEWzoCMGRNiBTaYkwtdus6XWbwOKhOoINl7SR4jttlMg3AzZcrx4sBeEJ9FOVG9_EgFOF7z0zG9u0rmu2wXvLRMgl2Hg133_K9DeBIIj05N9cas0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
نتانیاهو درباره لبنان:
اسرائیل در منطقه امنیتی زرد باقی می‌ماند که ما را ایمن نگه می‌دارد. و این یک دستاورد بزرگ است. بزرگ!
چون آنها چه کردند؟ آنها تلاش کردند ما را از آنجا با انواع روش‌ها و فشارها بیرون بکشند. البته این اتفاق نیفتاد.
از رئیس‌جمهور ترامپ و وزیر امور خارجه روبیو برای مشارکت و کمک‌هایشان تشکر می‌کنم
@News_Hut</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/66939" target="_blank">📅 22:02 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66938">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/67074bb47c.mp4?token=niT99btNIHEo094o4uxdIDpvXnekD3haYVurdCO917iWzRRJ5VgLEDhUJ1hTbjlvqEicG3E1fgzAf_6qg2gUrNxtvwhYwdfMvytEECKwndaFYnhh7dsRCqj0WoeNF3omHLVaCCjlCGanfboOQNunM8nVZwgKMtsdljPpyfMZqiQxlo7ENkavGaqbYMXjI7G0ZpZ7tasSuHK5yJb6CwoUSpijO-D364YA1hvF89yakUClK8MsK_OP_ZHHVv-eIoXQQZNmfaG2-K3xH9Cu8-ymDIDugOiGc761LxS2yNkq85Iw4QGMpLbuaLxfzqK2dJrvwRsOm6euPADR7gCilf27ZA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/67074bb47c.mp4?token=niT99btNIHEo094o4uxdIDpvXnekD3haYVurdCO917iWzRRJ5VgLEDhUJ1hTbjlvqEicG3E1fgzAf_6qg2gUrNxtvwhYwdfMvytEECKwndaFYnhh7dsRCqj0WoeNF3omHLVaCCjlCGanfboOQNunM8nVZwgKMtsdljPpyfMZqiQxlo7ENkavGaqbYMXjI7G0ZpZ7tasSuHK5yJb6CwoUSpijO-D364YA1hvF89yakUClK8MsK_OP_ZHHVv-eIoXQQZNmfaG2-K3xH9Cu8-ymDIDugOiGc761LxS2yNkq85Iw4QGMpLbuaLxfzqK2dJrvwRsOm6euPADR7gCilf27ZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇮🇱
‏کاتز وزیر جنگ اسرائیل:
اگر ایران برای جلوگیری از اجرای این توافق تلاش کند به اسرائیل حمله کند، ما با قدرتی قاطع و کوبنده پاسخ خواهیم داد و شکاف موجود در توان نظامی میان دو طرف را به نمایش خواهیم گذاشت.
این توافق «ضربه‌ای راهبردی» به محور تحت رهبری ایران وارد می‌کند. اسرائیل در منطقه امنیتی خود در جنوب لبنان باقی خواهد ماند و تا زمانی که حزب الله به طور کامل در سراسر لبنان خلع سلاح نشود، نیروهای اسرائیلی از آن منطقه عقب‌نشینی نخواهند کرد
@News_Hut</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/66938" target="_blank">📅 21:22 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66937">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K6LT_2I3PtzY-Mt6WCoKAqWPnoutXDOoEUhnwJ0s5W2lfq4-2QY5r0Y1NksILTImnKBha_HW7opzIPrKX89-_MMEdVY7ihbQc5l57bw3q2UjZeBjrFf6nUZrgOKfGDMrfO_0-zLqN1oIAIV39C9rrvKr_iQ1Bt6za0v3Lb6_MWUy7fR3uEVsR6xDYw3H29fTOScAlDQiM05ySIAaifFmWzTb9X4kYjb2fgTBEZUeoCsZYLnQ0PTGTZfMWYMSPGjjztqGKmCMMJuYFUXme7mzdBBmX4ERAyjlebto81festWkJ3JEOsO2hNgmbPnXpMJlbJ0zi33VYckCgeyvG-CPSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚠️
مرندی:
همانطور که انتظار می‌رفت، رژیم ترامپ چندین ماده از تفاهم‌نامه را نقض می‌کند. در نتیجه، ایران نیز مجبور به انجام همین کار است. جمهوری اسلامی تا زمانی که تمام تعهدات ایالات متحده به طور کامل اجرا نشود، به اعمال فشار اقتصادی و نظامی ادامه خواهد داد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/66937" target="_blank">📅 21:05 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66935">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AvjpL1v1o2PGIKwk1VWU-qdZLSMtY7mz6l7DwmOG-PCQ_LbUh2lcrxIbN2saFF8-xzeCXtf3oCsI5WyFAB7w1i0HXIEsjkhKrKOLY1Vix_I0aNFykTUpPfDPF_BxhACB1uro60pqOfF3s-1ChexsNV8UhPsZmZ9t_PIIYdPT4e2nYwLEMZk_7KWKjyWiMGmDoFBOQ-Rw9ZmCs9pwv1UK9zPImQ3lHcV2ucwFlnHJ0FbN7V2GZeZybRLIfT7Ox9OkFSUUq_DA6fFcXJATY65dswnaQp61wjQKkbun99aoQv8EsfeGkdqQzllUoTNw0bdT2UpOr4Otg7aNOzWxnvssaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hkf5mem2KZ2BOgi6Rv0-XY8KXriA3qD71pOGca-WLIdNiiQKjdBLY50M_EmEBeORX7K-QS6lEQxAhRyU_OWvm5BWcz16pSAtF8pk4hEyyi6y7l2ML-rHlIimxLgTqzPZRNv9-AtUEw1xt2q7zL9w7CtbNNhRWXVyKioRWdls3NHf3N5k9Gzg6jwYkZGLTnACN42HyyG9WEEjngqODrl5whXjASgkTID1A_meEyYGKDAs_O27N7a4cyC9gcmbEI3p2ad168H9zGHuj2znLjQIU30fAWs36-D1Hr4n3wNgjfXfyjdPeALVj6H7n6m-SUW-OqXDnqmBKRGr6YrG0XcWQA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
ترامپ در تروث سوشال
😂
😂
@News_Hut</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/66935" target="_blank">📅 20:35 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66934">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O3BC3UHLD87F-WNd5B70vvCmBy5mmA-g5IWQSHfc3OEarIaAAsGCuuqDOD8EWsqcyky2-Q1kgsM9gycbUau6-r-dKwARUPred4SnT60dBnGbRwwlpKMkpS9zzl-Z8YJmGbBrEN4k9Dy7LX96xJKWWVivoQEOl_P426tExX6VSWV4pDTf1V9PLL1vcAodpxE6cWFP50NX18sTCzy1Gvrj0bd-refpIC26VOleCLRs5aYtXJ1b80VCtePTXq5HrJ-CmyxjFVnm3gq-jnatnwaxtMWh79GPpzPks_eB9GL5-XE0j8KeQ6rfIhy3k-RYZ6erm9TDkM-0r27zUx_qUqjMzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
کامران غضنفری، نماینده مجلس:
گویا قرار شده هر موقع آمریکا یا اسرائیل تفاهم را نقض کردند، قالیباف ۴۸ ساعت اخم کند.
@News_Hut</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/66934" target="_blank">📅 20:10 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66932">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h6L0tpQiyrHq81DWlLg7zICgDccrJeDi7dutccfsNteVqrbKxaXZzksc3gc3NMkKrFQTlWj8MadfA9MduaBRMOWlhGJDzKy-y8KIS2wErgU6MENP0g-LJvsvst_9PVG_yWU9cBmt4W2nxkOOs0I3Rua_JuHdO4sgR-MHgBaX3JHdgSvBTi5-M9nV3pcVNla51mEIryGTUij2iKfNHnYYY4tbRsHObzrekAYyJZLs2fDZ2_GBF7TVfcJWmgFEbsb5xidoXgvzkjCc0DMpQDHPf-tJ_QK46GwigLlQI-5W8W5I9SV6nQQf2ulknqnR04t7ML9f0U85J8A0Us2dOZ4kEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/25ed09978b.mp4?token=jBvfmGLHg61J1RGU6c3JmqTvZjwO-hkF5JyiX8SNkprsqc4Aviyx116q5jKT1XvRB3hi40UoMSdOTjGxSVygxVhKJa2WLEWVtS5svcXHEPr9FtLtVu_q-29C2jiXdarMBlQigG_XOAPvpan1wRM1Y9AayagRm1PVuazG9woqatEYj1pZ_uFnvb3pcX-5Mxxj8YiqIZ94B-08DNdGYYW5bt-T6xQ0U9aeEI7vRNupxSidPy7f6JDeHSbvMYJDRCBl1MiVbLV3Ca5g0AUdkthMuGUBlKlDYaa2fgSazIz1K0BfRRx2NpaTX3RQohIeSGW6APPYSdH8j9IJFl-Scze0jA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/25ed09978b.mp4?token=jBvfmGLHg61J1RGU6c3JmqTvZjwO-hkF5JyiX8SNkprsqc4Aviyx116q5jKT1XvRB3hi40UoMSdOTjGxSVygxVhKJa2WLEWVtS5svcXHEPr9FtLtVu_q-29C2jiXdarMBlQigG_XOAPvpan1wRM1Y9AayagRm1PVuazG9woqatEYj1pZ_uFnvb3pcX-5Mxxj8YiqIZ94B-08DNdGYYW5bt-T6xQ0U9aeEI7vRNupxSidPy7f6JDeHSbvMYJDRCBl1MiVbLV3Ca5g0AUdkthMuGUBlKlDYaa2fgSazIz1K0BfRRx2NpaTX3RQohIeSGW6APPYSdH8j9IJFl-Scze0jA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
حملات اسرائیل به نبطیه در جنوب لبنان
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/66932" target="_blank">📅 19:42 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66931">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/97e8d5b77f.mp4?token=YGhc625y1BcIW36kBnU2Jfut_VrtDiH2EPlc8pdnNHUody7yhUw52_oh1ykgYwBPJmq0qpQrvDnLgVb1v3g7tFxoFys3kC0HLvwxyADBOD3JE6LZpBcY6F5wGweb6qypTecUBkHUj9xOQPZYr_ogR-AfWp5r1LjSZxKGaIMV6wOi9IgFol1kycrwQMeSv1ZSHAWZ8mE7MPCcu5kQdQ-6icmbhB-Mi_kCVVXccisS8PFrh2SGEYJqXg3Aw5qKmt2ghIUaato0G3EPww1DhRnbx94dUzF7kKAVtDmq5HTiRZANbhxBLeouc-8lJMA7ainzlSRGfZTP-Po0wuVNKVDxkg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/97e8d5b77f.mp4?token=YGhc625y1BcIW36kBnU2Jfut_VrtDiH2EPlc8pdnNHUody7yhUw52_oh1ykgYwBPJmq0qpQrvDnLgVb1v3g7tFxoFys3kC0HLvwxyADBOD3JE6LZpBcY6F5wGweb6qypTecUBkHUj9xOQPZYr_ogR-AfWp5r1LjSZxKGaIMV6wOi9IgFol1kycrwQMeSv1ZSHAWZ8mE7MPCcu5kQdQ-6icmbhB-Mi_kCVVXccisS8PFrh2SGEYJqXg3Aw5qKmt2ghIUaato0G3EPww1DhRnbx94dUzF7kKAVtDmq5HTiRZANbhxBLeouc-8lJMA7ainzlSRGfZTP-Po0wuVNKVDxkg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
نفهمیدند رفتنش فقط پایانِ یک پادشاه نبود؛
شروع رقص طنابِ دار و بوسه مرگ بود.
عکسش رو از اسکناس‌ها پاره کردن،
و از همون لحظه سقوط شروع شد
و نسلی که خیال می‌کرد وارثِ آزادی می‌شه،
وارثِ تحقیر و فقر و چوبه‌های دار شد...
@News_Hut</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/66931" target="_blank">📅 19:26 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66930">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/10face1c1a.mp4?token=eKLJKXpPXawCGghwTXKmxrgllqWQb0DoKLDqEil8WbSzJ1HWJXLF_hi31zyhFud5rXnRTlILObUC1IkfLkLZkn-Zlj8uI_JRU0afcqrJldrKCzHcUiYlDd8RwP210UXoWZkS60TiXJ30xUHLCVjsaGNpfvVsWszRW6vPiHvCCJh7dWZMoueVW4gQswjQw-X0U0GIdQpv8Al7jqyYxaYpvv2J_i9uXZemM31980Clw58kvQEmthVLhHWGPyuxE0svtmF7s7GnJt1TWF0TE6V_Oa8WVTMNN5BwflWDkuShoNve_EuRBNdj2PF1Be4DgF9x8ztLmK0E3VJO2vC2cgHjPA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/10face1c1a.mp4?token=eKLJKXpPXawCGghwTXKmxrgllqWQb0DoKLDqEil8WbSzJ1HWJXLF_hi31zyhFud5rXnRTlILObUC1IkfLkLZkn-Zlj8uI_JRU0afcqrJldrKCzHcUiYlDd8RwP210UXoWZkS60TiXJ30xUHLCVjsaGNpfvVsWszRW6vPiHvCCJh7dWZMoueVW4gQswjQw-X0U0GIdQpv8Al7jqyYxaYpvv2J_i9uXZemM31980Clw58kvQEmthVLhHWGPyuxE0svtmF7s7GnJt1TWF0TE6V_Oa8WVTMNN5BwflWDkuShoNve_EuRBNdj2PF1Be4DgF9x8ztLmK0E3VJO2vC2cgHjPA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
گزارش تلویزیون الجزیره از خوشحالی مردم مظلوم غزه بعد از گل مصر به ایران
@News_Hut</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/66930" target="_blank">📅 19:02 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66929">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SZCLQ33Q6X9YswABF03ESNv92mCGigamW8s6GWcR7uD5T54jPgkgh9eLZrLHgac5YV6su2kGLXyJqn1roIXNNtvhET-YvBEDKrJH5L14xIwmjRgnmboTLBVh10uBwfz209hDMHAbBb0WxWvVYdSY8g19fDlNKSLjqWGILB2gFa5j--1i7QXISkNdaIT-sk4yOGVTh2g68I2tFDqoDwinsDVqPkCBpyRPvraPqgG2nnJVKcvhoMo0JTj6l_j1UhT4qz6tRPV4ZeRfwnbcslzuM7ufLUdd-PP5ivwKDeniQVkicNlwgInOCWwHVwpvBRLZJ1mwjqmttDDi6T7Irnfnug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
العربیه به نقل از سنتکام:
حملات ایران به کشتی های تجاری را نادیده نخواهیم گرفت.
@News_Hut</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/66929" target="_blank">📅 18:42 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66928">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/843a55c77d.mp4?token=WU4tLSaCowl9wiGqOWVUGcEbEgzJnDbI3x6EMSjWxUHzKE11XuDGiHr3Pk-7SmY6mdmVMsF0aHrFs_IN3e4ffiKv8tH0unHtYyN2odmDcqRdqin5jEzwZ201cSFvLMY-H7upWQiJxdHamfxcBEgAt3e3c9lRDLTkiJ0ujjQS0hISlrX0636zB4lAHDCOTywOicdlD1CQYrJuBOe2wHFkwB_pPQNDuSq9cyJCqq1Ok7vRrQYV0I_KGHTmDlvwBxJNS7mQZnjweqR6mSG0WU_jb3gi3YXVH1bes4Ut6g-Jo8H_fBQzjCslO3XzhCnHAnK58EaacCmgwYu8UxSv6KDNvA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/843a55c77d.mp4?token=WU4tLSaCowl9wiGqOWVUGcEbEgzJnDbI3x6EMSjWxUHzKE11XuDGiHr3Pk-7SmY6mdmVMsF0aHrFs_IN3e4ffiKv8tH0unHtYyN2odmDcqRdqin5jEzwZ201cSFvLMY-H7upWQiJxdHamfxcBEgAt3e3c9lRDLTkiJ0ujjQS0hISlrX0636zB4lAHDCOTywOicdlD1CQYrJuBOe2wHFkwB_pPQNDuSq9cyJCqq1Ok7vRrQYV0I_KGHTmDlvwBxJNS7mQZnjweqR6mSG0WU_jb3gi3YXVH1bes4Ut6g-Jo8H_fBQzjCslO3XzhCnHAnK58EaacCmgwYu8UxSv6KDNvA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚠️
صادق خرازی برادرزاده کمال خرازی اعلام کرد عموش بعد بمبارون خونش زنده میمونه و تو بیمارستان بستری میشه که موساد میره بالا سرش و با گاز خفش میکنه.
@News_Hut</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/66928" target="_blank">📅 18:08 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66927">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2861d69191.mp4?token=XTpmROOuG9abKgo93GqE67OxLCed4iX8VDMgd-8x4f1sktt-yxsUVQAqgxyJScpOSRClFwPi5OXHiYWdieUCRJgFXDn-rFZ_NqGTkEdrikHpBVvjfyeZ4v-5c-CDvPhBqWvaBaJRxjut6_ta90U6-8ajTJ6dloPSScH6_bcvGhrx63CO6xDlg1bcI3hNtC5yoaICXTIqBjwdjCyUY6j-6To2qk2T9wLm5D6RicPiYHdAFwKAbqUm_1whCWWG6S7DPpKncaLmVUynaFs1TWkamtyYIkSL473dWgBfAyvdEfCeuYGANaLSpKeB4EzcnneAqJ_8tHCgj2YvdATptYVA1g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2861d69191.mp4?token=XTpmROOuG9abKgo93GqE67OxLCed4iX8VDMgd-8x4f1sktt-yxsUVQAqgxyJScpOSRClFwPi5OXHiYWdieUCRJgFXDn-rFZ_NqGTkEdrikHpBVvjfyeZ4v-5c-CDvPhBqWvaBaJRxjut6_ta90U6-8ajTJ6dloPSScH6_bcvGhrx63CO6xDlg1bcI3hNtC5yoaICXTIqBjwdjCyUY6j-6To2qk2T9wLm5D6RicPiYHdAFwKAbqUm_1whCWWG6S7DPpKncaLmVUynaFs1TWkamtyYIkSL473dWgBfAyvdEfCeuYGANaLSpKeB4EzcnneAqJ_8tHCgj2YvdATptYVA1g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
سلیمی، نماینده مجلس:
اگر حزب الله در بیروت نجنگد، ما باید در تهران و کرمانشاه با اسرائیل بجنگیم.
@News_Hut</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/66927" target="_blank">📅 17:40 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66926">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🚨
🚨
🇱🇧
نعیم قاسم دبیر کل حزب‌الله:
این توافق باطل و بی‌اثر است و مفاد تفاهم‌نامه ایران و آمریکا باید اجرا شود.
این تشکیلات، ادامه اشغال را برای سال‌های متمادی مشروعیت می‌بخشد، امری که می‌تواند به الحاق این سرزمین‌ها به رژیم صهیونیستی منجر شود.
ربط دادن عقب‌نشینی اسرائیل به خلع سلاح مقاومت، پیشنهادی بسیار خطرناک است که از تمام خطوط قرمز عبور می‌کند.
ما به مقامات لبنان می‌گوییم: وقت آن رسیده که از اقداماتی که لبنان را ویران می‌کند، دست بردارید.
@News_Hut</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/66926" target="_blank">📅 16:52 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66925">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/23291f5586.mp4?token=gUb28qinQpgDdBhXfSu-3bL7qS3N7bpej44oeKqobe-MqEZVrAWl_KaFYtUlhDstDlFHeB5XJ44S9c1oLBs1W0Toy8XN7UUsXTCTfOAnfY7ZB9rHZ-f1B-fOTEShbQ19Hu9YApKi_4Xbl1jCHcaqzOioL0OyLEazFOgaNKCO7Hs29EXfDeeV7kG8Um2DdQR2hOXZ5LrgD6VYyGU_tx2T08ThD9DoN_hSmWrGTbUxWrsg0NzWf03w-GuuYiN8VdtEGnyQZ4AacDkKcoqKPiph6n-319ZEHSVmsGtqiV4GKsx7WTynjMKcImOPUR82OYyn45ulZ--7b5yts9PLDYRdvA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/23291f5586.mp4?token=gUb28qinQpgDdBhXfSu-3bL7qS3N7bpej44oeKqobe-MqEZVrAWl_KaFYtUlhDstDlFHeB5XJ44S9c1oLBs1W0Toy8XN7UUsXTCTfOAnfY7ZB9rHZ-f1B-fOTEShbQ19Hu9YApKi_4Xbl1jCHcaqzOioL0OyLEazFOgaNKCO7Hs29EXfDeeV7kG8Um2DdQR2hOXZ5LrgD6VYyGU_tx2T08ThD9DoN_hSmWrGTbUxWrsg0NzWf03w-GuuYiN8VdtEGnyQZ4AacDkKcoqKPiph6n-319ZEHSVmsGtqiV4GKsx7WTynjMKcImOPUR82OYyn45ulZ--7b5yts9PLDYRdvA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تو پخش زنده ورزش سه چخبره؟!
به جوادخیابانی میگن چرا انقدر الکی از قلعه‌نویی انتقاد کردی؟ جواد هم قهر کرد و کلا از برنامه زد بیرون
🤦‍♂
🤦‍♂
@News_Hut</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/66925" target="_blank">📅 16:08 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66924">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/516c2865c1.mp4?token=SrnvbuqN5nevXHPz9L-d7vTht6BOBpGByPkaWaIn7G4Kz7EQxN2Rugo4ATLw1-uwjdlEfI3Xgm5PTQCcYH8agv6qPjKeuou6KZ1fsjZHnXr92pZlqQ0_QaPQeb17bp1f5IS7TNUlRtGG_aTjz3_W7mtbiHYklgaS3bjH8aZ4Z6kMpFy455sahg-kXef-F4RLTbK2Qw6ngUcEzuuB97rUA_U2-AqxlVpPw1aYBxlGobnLPeTLIA_fhRtoiUtEw6PwRy_MDYzwIKbmCmzEYMkObJDzyx4IHADx4_XXj90shr-QewysC9r2crb1OaRmIcAaN6yaVR__gllfcT4lkXVvaw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/516c2865c1.mp4?token=SrnvbuqN5nevXHPz9L-d7vTht6BOBpGByPkaWaIn7G4Kz7EQxN2Rugo4ATLw1-uwjdlEfI3Xgm5PTQCcYH8agv6qPjKeuou6KZ1fsjZHnXr92pZlqQ0_QaPQeb17bp1f5IS7TNUlRtGG_aTjz3_W7mtbiHYklgaS3bjH8aZ4Z6kMpFy455sahg-kXef-F4RLTbK2Qw6ngUcEzuuB97rUA_U2-AqxlVpPw1aYBxlGobnLPeTLIA_fhRtoiUtEw6PwRy_MDYzwIKbmCmzEYMkObJDzyx4IHADx4_XXj90shr-QewysC9r2crb1OaRmIcAaN6yaVR__gllfcT4lkXVvaw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
صحبت‌های ونس درمورد سه قطب قدرت در سیستم جمهوری اسلامی
@News_Hut</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/news_hut/66924" target="_blank">📅 15:33 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66923">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/097bf86cd1.mp4?token=fLqK57JsprdeV7vZpsaQYtTxJUz2ekRmHPwsrcW7iqYQwSrphZ_4ZIguHDqkxwlDERGymlL536GFvKu5ITJ_3UjmoQM6Y-7bOZ_x4nBPRH8j0vZoNdK8Ydhzhhi8ejI4nMEWPS0petJCNp2vQOUSbP7k_s5TNLrDSR7mo3AOPdsPf8oF6r0qT3Z-91Rhk4__vegQrsS1IwOcho3ZvALKIAe4k8SMf0xnYhd7ejERWHvl3iMTDWsF7Ny585_3Amk8UupUeTNGLpPV6JAvRsXnAQvBoD8eb-zINr7U3Bu4BxjfmWzeNCXg5jAd6oQNCL0Kj5yqkCQXtM9GmQ2uL492Tw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/097bf86cd1.mp4?token=fLqK57JsprdeV7vZpsaQYtTxJUz2ekRmHPwsrcW7iqYQwSrphZ_4ZIguHDqkxwlDERGymlL536GFvKu5ITJ_3UjmoQM6Y-7bOZ_x4nBPRH8j0vZoNdK8Ydhzhhi8ejI4nMEWPS0petJCNp2vQOUSbP7k_s5TNLrDSR7mo3AOPdsPf8oF6r0qT3Z-91Rhk4__vegQrsS1IwOcho3ZvALKIAe4k8SMf0xnYhd7ejERWHvl3iMTDWsF7Ny585_3Amk8UupUeTNGLpPV6JAvRsXnAQvBoD8eb-zINr7U3Bu4BxjfmWzeNCXg5jAd6oQNCL0Kj5yqkCQXtM9GmQ2uL492Tw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚠️
تصاویر ماهواره‌ای از قبل و بعداز زلزله‌ مهیب ونزوئلا
@News_Hut</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/66923" target="_blank">📅 14:55 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66922">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lUsqaCXaZGUv9VUdLpFgV1jxKU3gZQbZ9Ny7Qke70ssc0Rp0DYN6sDkD0G2m3JbDmFdgZ8p8YoLFI3kZ96nqlZec54ojiq8eWkp_2vP90kIxq9ea-6u_H1B7tg7oKXBjDHRWg901AQ0UxoIJAwqxEJYgn3xCunA1YD5THi9K2QsrvVoi_q3x2-s39HulCZxVwZWBK4tfCIm0iHo7Yq4ZduySfo270I9xhgCQ6rdUDOPvHOys4Hi_IeGmjoSnBwW9lJPI8M7ZJCUzms1NuU8plRh3p0V_8CJ21BZSKIUAkO5Wr848r9ztbuyYmjR00DWjXlNuI9xUsAOHYNLqXrAmkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
محسن رضایی:
پاسخ به ناقضان تفاهم‌نامه سریع و کوبنده خواهد بود.
@News_Hut</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/66922" target="_blank">📅 14:17 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66921">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🚨
🚨
⚠️
صابرین نیوز:
این نفتکش، برخلاف مسیرهای اعلام‌ شده از سوی نیروی دریایی سپاه پاسداران، قصد تغییر مسیر و عبور از آب‌ های عمان را داشت که در پی بی‌توجهی به هشدارهای مکرر، مورد اصابت قرار گرفت.
@News_Hut</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/news_hut/66921" target="_blank">📅 13:38 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66920">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OkDDwtrEBYjOOv5wuAP1Ezq9KCBoe52f9oin4AA-G5dnQD_60MIUhUTHjUPHD8A9OTb5uzyC8DFfd95_OCzN13VfrBteY7n5Ek2615DuGDMnDXPyl_f0jezPKr4F0hX_upc6mVId2yqFLascWEb-c73S8QGKLiKpE8q30ifUoINFXiO-_rBL8sHUCim_ppERttJlaw6sPTuLBgFptgeNIwbydkE-X77h8Cml7odGYUBp5j2ZBz5pV1aIa6keO6nWQIWfpmuF_L0eqWD4gnYnwVyBDdgAe7D6lH481ez0E2kwVuSwOUNhW8ct7exDISuAFXYWWS1kZDogDE6lZJOP2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
#فوری
؛لحظاتی پیش اکانت عملیات تجارت دریایی بریتانیا اعلام کرد یک تانکر در شمال کشور عمان و در ورودی خلیج فارس مورد اصابت یک پرتابه‌ی ناشناس قرار گرفته و عرشه فرماندهی کشتی دچار آسیب و خسارت شده.
@News_Hut</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/news_hut/66920" target="_blank">📅 13:20 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66919">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">🚨
🚨
🚨
بحرین:
صبح امروز جمهوری اسلامی با تعدادی پهباد به ما حمله کرد.
ما این حملات را با شدیدترین عبارت محکوم میکنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/66919" target="_blank">📅 13:05 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66918">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l00P9HwZ0Ghd0ARIAPhsW_MmRU6fKyEfZbXd720vWntzZP68l2WRWvV3wQ_aTs_O3isPKKqjqufUopkStWv-EMt93yzFhcO5XPZu_AYkTXxvuXZBu3hCYvEXM99LMNuIkwBYNWaYqs92zz_xUXt7ECEC4IDzIfCX3JYgkc8ofNf42xbv-57qWfMdO3vMYT9o9Qt59pq6gfPI_CRm2aGjMY6YUtFjBZq1xt5QxzS6wOkesnJFh7JRtZCIUfr-dGZNGTLAQud3bWNvjF_FE9c31a39rAYW3yH0TJXETn556V4vixF6qO2UbORvt2ENFgKMSuqtW1aQhW88KU514Ur7vg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
نبویان:
ضمن تشکر از سپاه قهرمان ما به خاطر پاسخ به تجاوز دیشب رژیم امریکا و در نتیجه نقض بند یک تفاهم‌نامه، مطابق بند ۱۳ قبل از عمل به بندهای۱،۴،۵،۱۰،۱۱هیچ مذاکره‌ای نسبت به سایر بندها نباید آغاز شود.
منتظر تحقق شروط و واکنش شفاف و پشیمان کننده‌ی مسئولان مذاکرات نسبت به نقض تفاهم هستیم.
@News_Hut</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/news_hut/66918" target="_blank">📅 12:35 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66917">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c6e496d9ac.mp4?token=fhcT3wwsAdsd8UFcYn_8JqaKnvAqABblUiSWru7AZh9I9w4RxijorQ5NCjOGL4VS6kuIGHo4C1Bj6dk5P9BhVRPQK1V77wErfZrI9ybZPKsdqzQO92IjmMQMc5TsNQK7C9HGY1_qPEZ3Q4gfXxFalwU9BHqxyq7EjWhBQMYJKEaGWTQgtEm42IKlPXfs7y9c7g5Aj1IiQSYkDC13omkVrNTUdnCPXUsXLzIQYCptaueRRbNQTrzDJBoSui54Eru78BomrjOcpbUepaFOaxiy4ZgnJG7XK9so1qeTk9haCmwyBvG4D9KrqvciIbkCrcbm5r-MT6bL8vV4GIMlF8RnHw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c6e496d9ac.mp4?token=fhcT3wwsAdsd8UFcYn_8JqaKnvAqABblUiSWru7AZh9I9w4RxijorQ5NCjOGL4VS6kuIGHo4C1Bj6dk5P9BhVRPQK1V77wErfZrI9ybZPKsdqzQO92IjmMQMc5TsNQK7C9HGY1_qPEZ3Q4gfXxFalwU9BHqxyq7EjWhBQMYJKEaGWTQgtEm42IKlPXfs7y9c7g5Aj1IiQSYkDC13omkVrNTUdnCPXUsXLzIQYCptaueRRbNQTrzDJBoSui54Eru78BomrjOcpbUepaFOaxiy4ZgnJG7XK9so1qeTk9haCmwyBvG4D9KrqvciIbkCrcbm5r-MT6bL8vV4GIMlF8RnHw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حمله شیر تعذیه به جمعیت
😂
😂
@News_Hut</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/66917" target="_blank">📅 11:49 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66916">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e02aab4b18.mp4?token=phVzcuziKnmqFuNLcnbAh9FMa2VNUgthej5sL6zLIh0skj8vpmYs_YCcgQqaJp4HEaQNY5KPLgUyfmsw77O642i_-pi_9XWcrnqpJoNWcTe_hjP5HfVOY33AYdTduLH27CLaEpBvRjXWWrunEBbcW3EGtIAm6YK83cXhmAAUS1Cy5PqL88dOO6mpz-F9LiZP90pwzcp_Agz5h26tKMe1bFDTiqtd_o0GgDPBYsrSMpoporMkLCr-XXtPNPh32eIEzlmYJg87_zS7-H9-trOPkXeQk6xHfwn1uT7ASQ2mafil0GNHvof-dFsfCvObqudig2wYM4hxQ9pvSNFeL0yHkKJMew6dU2MxjX7cYdsgoHbm5YvIB7BOB-xCzQmA0NdG0_EADjzE9qWyCh-RABk9tUE05FEf82APawLJTi2NDyKDEWPCLctKaf33QMYpEsU597rnd4fr-L_8W4o2cSsDaHCt9s28VkK_1W-C3XRRtdlMLb5fomiv16exIp3hu1CYeo_XkCBIXGcWTxVmRZojUXOW7LHDqbN9vn2rJmYyXg1TnRTqWg9GOpvaZ3169v_N3ZlxDUcPL8gHAadiyCzVIumxBANNAN--_xBkc7fImHRwwnt5ZEjnG4fKz2f7ZtxZMLtg_X0ssbFgjEIa9EaYYXmF29KBHPqpugJ_x47101Y" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e02aab4b18.mp4?token=phVzcuziKnmqFuNLcnbAh9FMa2VNUgthej5sL6zLIh0skj8vpmYs_YCcgQqaJp4HEaQNY5KPLgUyfmsw77O642i_-pi_9XWcrnqpJoNWcTe_hjP5HfVOY33AYdTduLH27CLaEpBvRjXWWrunEBbcW3EGtIAm6YK83cXhmAAUS1Cy5PqL88dOO6mpz-F9LiZP90pwzcp_Agz5h26tKMe1bFDTiqtd_o0GgDPBYsrSMpoporMkLCr-XXtPNPh32eIEzlmYJg87_zS7-H9-trOPkXeQk6xHfwn1uT7ASQ2mafil0GNHvof-dFsfCvObqudig2wYM4hxQ9pvSNFeL0yHkKJMew6dU2MxjX7cYdsgoHbm5YvIB7BOB-xCzQmA0NdG0_EADjzE9qWyCh-RABk9tUE05FEf82APawLJTi2NDyKDEWPCLctKaf33QMYpEsU597rnd4fr-L_8W4o2cSsDaHCt9s28VkK_1W-C3XRRtdlMLb5fomiv16exIp3hu1CYeo_XkCBIXGcWTxVmRZojUXOW7LHDqbN9vn2rJmYyXg1TnRTqWg9GOpvaZ3169v_N3ZlxDUcPL8gHAadiyCzVIumxBANNAN--_xBkc7fImHRwwnt5ZEjnG4fKz2f7ZtxZMLtg_X0ssbFgjEIa9EaYYXmF29KBHPqpugJ_x47101Y" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یک آخوند:
غلات آمریکایی آلوده هستن و میخوان ژن مردم ایران رو تغییر بدن. آمریکا قبلا شکر شوروی و برنج ویتنام رو آلوده کرده. خون هایی که قبلا برای ایران فرستادن هم آلوده به ایدز بود.
@News_Hut</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/66916" target="_blank">📅 11:10 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66915">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ENivU0TRubNFfJ6pM2nxZ3haXANTc0R6kZ0JYh05tDNtvYOw7AvMRyidj-PEQIruEPrtuxl_Nn4iXdWM7lLyrYssJFYd4BiDpsTaOng5Xu8U7xii-ur1P2PjreMpA8aGiaUblHkVosSIOmCSKyCs1SDatZb6jyTwkqTE-gz-K2R_IN1irK10umhnUhbVgClxNonbY7VJ0ZAwWr3txBB0mMk0R8DsKA2an_eYiFKQBtZbrHnZ_Jj117ipJfhFlSvK8R2b4NmjGYsuWIC0CpDlYSmDqNa0yzjQJR-Gbor-V-JX7qkE7TI2hp_m2lsI6QM6V2pIggKsJ8UgkWznhVMPrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇺🇸
پرزیدنت ترامپ در تروث سوشال:
نمایش هوایی چهارم ژوئیه، در آسمان واشنگتن دی‌سی، پایتخت بزرگ ما، بزرگ‌ترین نمایش هوایی در تاریخ ایالات متحده آمریکا خواهد بود.
صدها هواپیما از انواع، اندازه‌ها و سرعت‌های مختلف به نمایش درخواهند آمد. من حدود ساعت ۹ شب سخنرانی خواهم کرد که پیش از آتش‌بازی است که باز هم، مانند نمایش هوایی، تقریباً ده برابر بزرگ‌ترین آتش‌بازی در تاریخ کشورمان خواهد بود.
پس اگر هواپیماها، آتش‌بازی و دونالد ترامپ را دوست دارید، آنجا باشید!
@News_Hut</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/66915" target="_blank">📅 10:40 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66912">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uxc6AeMVjmuV-2XmAE2j_VpFhU9orIHWyRqteC0-FX8o65MrTe2rqoOJB-QsVA1B3P4dBMiJlV4XlsZvVKnpUh0qz7pFquWbKKpirE4lm6xF7Nxx160WZAt-Ht-bjelj89LecSO3N4-V2trZCAcJgn6BvsNOkBeIUqPyjZ-YbYANI5wKATjUVnM6MgnsGagTtmJIdQx9P_7HkeM1nD843mN1qR7EaNHXRE44lPCmuq6AQyKOM1d6tFnOTB_1Svz4IVivAN8S_ybm17Jt4ecl8_hUlud-6QgZiMFlPSYJmWKEc9182OdICtYWXTm7uDIK8KvHFQFOBI17jywpZkqXOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ai0t7z1IjDkP31woXt5wyvtlo-jJG_RxtVsbr0qnI30QQEcpTRs1vtMqsBD_NL2iG4Mba9iSJl2V-drDTL1TAo4013ASu1U4NXzBJa4O8ea_0JtBtELHLRfIYZrjUxjqZ1GfO3xY10iMDoBLwXbZ4zCcBMZOD9JxJCMaBgy6h36Q7NZfC2wxdavMeU3zC5Dw9taVh2aE5S3JBnQYaxoKdZpSNq6yVwjGiVeMO9yGZquUv_3jvX8RL3XAUVMvhQKHP4WDa_WD0ufnfln4ZEJEOr3zZUAF7LZKpX2f8b4Dam8mvLG4K6S7_33ix8LzAbmfayJyMXtoCSedG5c-v-4Dnw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/812712f3b6.mp4?token=OOCZb-N2BlUsarZJXcbRxHyqnY2ztjQ5o5Mbga7G7D8I_puzw_ISyq8J6BmYJgtd7WNuMHyHzlaVMa5HUhD3Ft9wEjcKef0kv6XHtKVVw9FiWqm3QhiIX4WMYDigl4xgb6LgZGudtniqqxJoFyyrCvImhIjldoGA8L0jbTYE50qeYL5MPJZs1-R7RLPv-VeIB5GaQJq2IsszPJAl0dVdthmfeZ3Zu2JYmw3v4a83hDJ9dWMW4ZIQ6ThMLmtvbg0RaFnM8hB6FtUvbBg7DvaK87nEOiugJm5mal40V4MJAMYSgJLjkGFmvoPiTVWXh7hQliJSqwudXyB2uXV8YbgiuQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/812712f3b6.mp4?token=OOCZb-N2BlUsarZJXcbRxHyqnY2ztjQ5o5Mbga7G7D8I_puzw_ISyq8J6BmYJgtd7WNuMHyHzlaVMa5HUhD3Ft9wEjcKef0kv6XHtKVVw9FiWqm3QhiIX4WMYDigl4xgb6LgZGudtniqqxJoFyyrCvImhIjldoGA8L0jbTYE50qeYL5MPJZs1-R7RLPv-VeIB5GaQJq2IsszPJAl0dVdthmfeZ3Zu2JYmw3v4a83hDJ9dWMW4ZIQ6ThMLmtvbg0RaFnM8hB6FtUvbBg7DvaK87nEOiugJm5mal40V4MJAMYSgJLjkGFmvoPiTVWXh7hQliJSqwudXyB2uXV8YbgiuQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
برخورد هواپیما به آسمان‌خراش ۵۱۸ متری در پکن
یک هواپیما با آسمان‌خراشی به ارتفاع ۱۷۰۰ فوت (حدود ۵۱۸ متر) در پکن برخورد کرد و سپس به زمین سقوط کرد که منجر به تخلیه ساختمان شد.
در اثر این برخورد، دو پنجره ساختمان شکسته شد و هواپیما کاملاً متلاشی گردید.
دود غلیظی از طبقه همکف ساختمان، جایی که لاشه هواپیما پراکنده شده بود، به هوا برخاست.
شمار تلفات هنوز مشخص نیست
@News_Hut</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/66912" target="_blank">📅 10:15 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66911">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jFh7uMtEg0OHeGym3gX7sYrX6ZeZ4NHpJgE41QpIIXh9UEPlclPaoh3cZtEM68OalXoq_aSfpRkNJooPxKjZf9whdy56njzP4ztosQS_J5xsDTXBsx9ORBohZt5pgYx3_HzmAVyBXHAJoStcAPOsSj6ZUZDMCQdM-mm4JAmGxeyE9SWmMi_SToLzEsunlIohSihikQFhmYOfRe59mwGCs7iOkshtLkXq0T1O6WfuTeY54dq0OS-Sv5-KBT9W0LhftXQG8ftV5K3cxSh67uPEAolBCXExNIPExTAeSc2HYXaK5dBc-HU6ToQy0P6-OUhaTDj4J3unR8_cLFS0VVF7WA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
❌
🇺🇸
آیت‌الله جی‌دی‌ونس:
ایران توافقنامه آتش بس امضا کرد. ما آن را گرامی داشته ایم. اگر آنها در مورد نحوه اعمال تفاهم نامه اختلاف نظر دارند، می توانند تلفن را بردارند.
اما خشونت با خشونت روبرو خواهد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/66911" target="_blank">📅 10:10 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66910">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/01b5404ad7.mp4?token=ENjjHVIvrQL77_gFDdgGEHVJzHKl_K7NPsxHnJBUoUhcflDH1N6R61fYMYEGhZF5KA33JkM75H2ZxbAyhHQLtnO17nQQYklNyncxuxQqTPZ-Hyqv89fkmluQehFnde18A-pIk2xFmDvEJT-xrCnkgTn8LgHVM2bAg29JLfscpuhbO7WDVHpBf4h4YCrVqBnq7ZdUzQXhpLcNrncTGPPEsettf4J680TE06eiLe-62vgmrXWb-KaylWvO-qtj8cgwH64FlZoa9YVn7ttKiCOFjXgaCrJrXJNjMASXabpy0Lv48NCR-zmOCu_ENWF8hRdTR9g7HuWrezJBev60OWIVmQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/01b5404ad7.mp4?token=ENjjHVIvrQL77_gFDdgGEHVJzHKl_K7NPsxHnJBUoUhcflDH1N6R61fYMYEGhZF5KA33JkM75H2ZxbAyhHQLtnO17nQQYklNyncxuxQqTPZ-Hyqv89fkmluQehFnde18A-pIk2xFmDvEJT-xrCnkgTn8LgHVM2bAg29JLfscpuhbO7WDVHpBf4h4YCrVqBnq7ZdUzQXhpLcNrncTGPPEsettf4J680TE06eiLe-62vgmrXWb-KaylWvO-qtj8cgwH64FlZoa9YVn7ttKiCOFjXgaCrJrXJNjMASXabpy0Lv48NCR-zmOCu_ENWF8hRdTR9g7HuWrezJBev60OWIVmQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قلعه نویی:
اینم یه ازمایشه؛خدا داره منو میکنه
🤣
🤣
@News_Hut</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/66910" target="_blank">📅 09:42 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66909">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e70e539fa9.mp4?token=ZnSk6lvOq_pfQ8EAIORrv9J3l0ehYqrClbq80g0gsQWKhi1DHpvibVenjQRIIx-iD1Y5XrdG5ZiIgiwLBy7nXjJN2sei8H_b5fL8sSBhvAxca3msNQmABKuZL9FQc9Ux3kd881wUgFVQxoV_Tccl-D6_ku52Mp777AvFMnAHLijY5WhKthOUuig5wrjpTEmtpXtH9MqBsZrpfpV-89pEeBT-TSyszuEoPB8fK7w8qlOTFMV-_D9qhJrUfCKyn8Bvp-i4P_G2uk_jvKCLltHKmPYphU1eTEcBWTV1j0volSfJZ5_MlXp4KrwYKEu2dO_gIWvTrc_StgBDuTCyP730mA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e70e539fa9.mp4?token=ZnSk6lvOq_pfQ8EAIORrv9J3l0ehYqrClbq80g0gsQWKhi1DHpvibVenjQRIIx-iD1Y5XrdG5ZiIgiwLBy7nXjJN2sei8H_b5fL8sSBhvAxca3msNQmABKuZL9FQc9Ux3kd881wUgFVQxoV_Tccl-D6_ku52Mp777AvFMnAHLijY5WhKthOUuig5wrjpTEmtpXtH9MqBsZrpfpV-89pEeBT-TSyszuEoPB8fK7w8qlOTFMV-_D9qhJrUfCKyn8Bvp-i4P_G2uk_jvKCLltHKmPYphU1eTEcBWTV1j0volSfJZ5_MlXp4KrwYKEu2dO_gIWvTrc_StgBDuTCyP730mA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
مصاحبه رامین رضاییان بعد بازی
@News_Hut</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/news_hut/66909" target="_blank">📅 09:32 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66908">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/449f3cb5a2.mp4?token=DQGelvVitNMGUQtj_BkGNB8dmjwm3BObKnqssO78vZfAv1lrDdbKpGxZC574FLbbJ6GtRUY6782jZSjxrMMtkea613m5QpOH7wE4Hqvvf0iu1ABYHJcoAWJkVT07CFI0x-recmtP9krixPnaoXC_hmbiFb83-UsoTDJ869lSq-Ya0a6XO00G2sygMpEVeyWVRa9AoZWWouxpuEYYT_WDDHLpbdS4v6ALU7y6BkZkDPK4sTwZJTGUmdgqAwchR7xKWPXBEA4rCDJXBdukeaIhBQ6QWnzHUSPNOeVdBeLeDaqRXaSrlJPgfzqAEqFf0uhEH3bASD1vkW8Fqt8Vy7MLhA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/449f3cb5a2.mp4?token=DQGelvVitNMGUQtj_BkGNB8dmjwm3BObKnqssO78vZfAv1lrDdbKpGxZC574FLbbJ6GtRUY6782jZSjxrMMtkea613m5QpOH7wE4Hqvvf0iu1ABYHJcoAWJkVT07CFI0x-recmtP9krixPnaoXC_hmbiFb83-UsoTDJ869lSq-Ya0a6XO00G2sygMpEVeyWVRa9AoZWWouxpuEYYT_WDDHLpbdS4v6ALU7y6BkZkDPK4sTwZJTGUmdgqAwchR7xKWPXBEA4rCDJXBdukeaIhBQ6QWnzHUSPNOeVdBeLeDaqRXaSrlJPgfzqAEqFf0uhEH3bASD1vkW8Fqt8Vy7MLhA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚠️
فرماندهی مرکزی ایالات متحده (سنتکام) ویدیویی از حمله نیروهای آمریکایی به یکی از اهداف مورد‌نظر در ایران را منتشر کرد.
حملات سنتکام در واکنش به حمله پهپادی پنج‌شنبه سپاه پاسداران به یک کشتی انجام شد.
@News_Hut</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/news_hut/66908" target="_blank">📅 09:10 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66907">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">‼️
بازی تیم جمهوری اسلامی و مصر با تساوی ۱/۱ به پایان رسید
@News_Hut</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/news_hut/66907" target="_blank">📅 08:51 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66906">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet @FutballFuckBet @FutballFuckBet @FutballFuckBet</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/news_hut/66906" target="_blank">📅 02:25 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66904">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/LL7WtNpkneB_VcvaKu4aRt8xOcYUWw6nxPIaiw-HQ-m60e3kUFoltF9CoySg_4qxlKIxfvkFGmIeAMRpV7TSOu6OEFuODCl2yiK1sxB0PfIfgNrEij1-KykFX968kEPiV6ZEB6s_7oAjUmPPpMluPMXLt8W9YKBnG_KUIOiNLAmkkgM1O4dmdSbvJfmDw3ueQfwnPXULvaN5h39bRvSp6Id1rgLRZvxd4AxynlGESEJbUlcXMjU-as-sEBwym0SmbHgjK1FVxU4egdNRwcaCreSH4ANFFho0XrnWzJc7Y4gVOFarebBpJzuRDIpj5wrzIxBTF6jukCdDacQMzgC2VA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/news_hut/66904" target="_blank">📅 01:25 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66903">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🚨
🚨
سی‌ان‌ان به نقل از یک مقام آمریکایی:
حملات آمریکا در ایران اکنون به پایان رسیده است.
@News_Hut</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/news_hut/66903" target="_blank">📅 01:13 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66902">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🚨
🚨
🇮🇷
بیانیه سپاه پاسداران در واکنش به حمله آمریکا به سیریک:
نیروهای ما موفق شدند این حمله را خنثی کنند و نیروهای مهاجم را وادار به عقب‌نشینی کنند
ما تأکید می‌کنیم که این تهاجم بدون پاسخ نخواهد ماند و پاسخ ما در زمان و مکانی که انتخاب می‌کنیم، سریع و قاطع خواهد بود. هرگونه حماقت جدید با پاسخی سخت مواجه خواهد شد
.
@News_Hut</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/news_hut/66902" target="_blank">📅 01:08 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66900">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/378d83ba5f.mp4?token=CZsXxWTBFVkYxRs2KBbYe8cYRN8D9lYIWeau4RB3yFzeJkHOjkCEL5VwS5W-KfQbxsgLpidEJ9CxvhQfzmF6InwowY3AwjaX31t1ZQpqwsiOI4_W4EWpSJd4TAdgw_FPG5PDN5iiIK9zhvAfxblCpN42Xzz6Wfcy36bTk8JFDqMXJG4QDTz8mW5q9MjJIMSI7rlfg_KFKWoIxK-2DG636QbCDTxwE9fyjXJcNIouzZBz8Bw6K9P4CBOITc7G2W0BwfAYyeCG7fWu80W1f0nNWaot7dsD_YeC1bR0YgeWsBzBacjrOc_FmWw3rMrb8QwfyLuUh3VgnA4r_9QI3FX1uQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/378d83ba5f.mp4?token=CZsXxWTBFVkYxRs2KBbYe8cYRN8D9lYIWeau4RB3yFzeJkHOjkCEL5VwS5W-KfQbxsgLpidEJ9CxvhQfzmF6InwowY3AwjaX31t1ZQpqwsiOI4_W4EWpSJd4TAdgw_FPG5PDN5iiIK9zhvAfxblCpN42Xzz6Wfcy36bTk8JFDqMXJG4QDTz8mW5q9MjJIMSI7rlfg_KFKWoIxK-2DG636QbCDTxwE9fyjXJcNIouzZBz8Bw6K9P4CBOITc7G2W0BwfAYyeCG7fWu80W1f0nNWaot7dsD_YeC1bR0YgeWsBzBacjrOc_FmWw3rMrb8QwfyLuUh3VgnA4r_9QI3FX1uQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
❌
اغتشاشگران در حال حرکت به سمت مقر های دولتی در بیروت
@News_Hut</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/news_hut/66900" target="_blank">📅 01:04 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66899">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🚨
🤯
🇲🇽
پشماتوووون فر بخوره؛ یه‌زن مکزیکی برا اینکه شوهرش رو سوپرایز کنه و بلیت جام‌جهانی بخره، یک هفته قبل مسابقات عکس پاهای خودش رو‌ به مردان کشورهای مختلف می‌فروخته و از این طریق تونسته درآمد زیادی کسب کنه و علاوه بر کیر زدن به مردان هول خریدار، شوهرش رو به…</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/news_hut/66899" target="_blank">📅 01:01 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66897">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WSoC4DJpCTzFEw-EK-zFP_gwvw806NLwaN6wPV_dut8_zXP_HTad9lkyrtDpzho_cOSezj_6zIu7LerK2iXRJQzCuv9cRvgohbdXAPtdyBDAgX2a4RGCXgW8rUDnoDu9orsNM-u_grhKWciquEITCRBrVGR0JixZydGF0MfQ9tSHYxGrYN1s9QS758ZEVlPWS1FKJir5CbTGz2UKQCLOhupUdFkq4qsBai7VH8QvuiNT5lBjzKoQLXB62YI990P1FwUZSeYeupup-xg_AOLX6l05nO6SslZ1zXy70luCwGxoBxdFlrUQr4fBe86vCWvFp3fYDHr9IRGKg2Lnq5Rw0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c146777e05.mp4?token=d_BHkUCwoMe5-MxkMIpSMjN12g5N2MqYzPG4z3QC8ZcD-drx2IrVAgZFniRlQhxilNY72j5Q3rnGykmKgHIaq8qHzH8U04jHGF81z8ac9oZ6dHNa3KrMspz47L7tM-N7xRPgpMn2J5BDdjAA290vZGn8x1qc7H6PV50zh8GpvFkRoxFeQy7ugUMDDUGK-o9_rb8rogJo_SvCD82AFmizIs6uatLLFiKjiS6EswWgQvu0uNCxxfQuihhg4H_wDQEFsvRblCAPOHy7dVaHz8hc916bOvC-QNVaNROFAHifYYBig8ZHIi5NGHYd6z33sO0H85aGhlvXJh2iL2oQL-z3Pw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c146777e05.mp4?token=d_BHkUCwoMe5-MxkMIpSMjN12g5N2MqYzPG4z3QC8ZcD-drx2IrVAgZFniRlQhxilNY72j5Q3rnGykmKgHIaq8qHzH8U04jHGF81z8ac9oZ6dHNa3KrMspz47L7tM-N7xRPgpMn2J5BDdjAA290vZGn8x1qc7H6PV50zh8GpvFkRoxFeQy7ugUMDDUGK-o9_rb8rogJo_SvCD82AFmizIs6uatLLFiKjiS6EswWgQvu0uNCxxfQuihhg4H_wDQEFsvRblCAPOHy7dVaHz8hc916bOvC-QNVaNROFAHifYYBig8ZHIi5NGHYd6z33sO0H85aGhlvXJh2iL2oQL-z3Pw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
اغتشاش هواداران حزب الله در بیروت در پی امضای توافق اولیه میان دولت لبنان و اسرائیل
@News_Hut</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/news_hut/66897" target="_blank">📅 00:41 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66896">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🚨
🚨
🟥
فاکس نیوز به نقل از مقام آمریکایی:
حملات آمریکا به اهداف ایرانی همچنان ادامه دارد.
@News_Hut</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/news_hut/66896" target="_blank">📅 00:31 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66895">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dZucBkuKXraEPVdN3Dn9HjhQIs1TqrcDvvycmqn4XM0AhM6pusYcTmC6nCvv7g8ImpA0_B7clWCxrHTzY_vVpcd9MjtagErCkNfbutrpbiQvbFrOa9Lyuavmsjx8b43Hqew67R_wndK3tpvRez_YoVsq6k6Ze3ueMtr2jnUaQobGOU4g-bb-JjJbWmNbsjka_RDSIwdk4pZVCCdrF1unMZ62vlp-nlBNQwU055VmaYtTh5cbvmk0_lTXSOooFDBpwMX_41Cna40edNFox9XHK-CXCxEgx2FYEIcQ7VrplJPbH-uRKijtB6iWWtgSL2k4olWf19eJnhd3A2eV0cs0gQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
سنتکام:
نیروهای فرماندهی مرکزی ایالات متحده (CENTCOM) در ۲۶ ژوئن، به عنوان پاسخی قدرتمند به حمله دیروز به یک کشتی تجاری که در حال عبور از تنگه هرمز بود، حملاتی را علیه ایران انجام دادند.
هواپیماهای آمریکایی پس از آنکه ایران در ۲۵ ژوئن با یک پهپاد تهاجمی یک طرفه، کشتی M/V Ever Lovely را هدف قرار داد، به محل‌های نگهداری موشک و پهپاد و سایت‌های رادار ساحلی ایران حمله کردند. این کشتی باری با پرچم سنگاپور در زمان حمله ایران در حال خروج از تنگه هرمز در امتداد ساحل عمان بود.
@News_Hut</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/news_hut/66895" target="_blank">📅 00:14 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66894">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🚨
🚨
🚨
#فوووری
؛باراک راوید به نقل از منابع آمریکایی:
ارتش آمریکا به اهداف ایرانی در منطقه تنگه هرمز حمله کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/news_hut/66894" target="_blank">📅 00:06 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66893">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🚨
❌
صدای انفجار ها به «طاهرویه» در سیریک هرمزگان مربوط بوده.
@News_Hut</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/news_hut/66893" target="_blank">📅 23:58 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66892">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c003ad7ec2.mp4?token=BIEAy3vdmluZN5SNWPblxj-OosM7qBY3JLLQ8ZT51eruVBCU0vFrQ1oCwkXxzHlGVfIe3LnnnFhhm1hZw1OwFcb_-q2Z-os0mDMB0VO5aedC1-Y2qtNi0HcUrw-JEEiv57sWVr8zhX68ThZGU8-rmtnan4lPU2yzQucmVGC2fq6__osioO9LEPcAVjR5mtiqUBpJVOyVU3xdhdfgDzMYEfhbEwiJcdCWWC5oSM0Gic1Qg6j__BiX1nMPsQLGab6uy5GRfxlCm-XlUos1Umo5vKn-qfRlqjFMvfbjqnSKER_aowUo73bM2Ei8DgFCFp-s8LINdicnk4FP2tQ9u4D0rA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c003ad7ec2.mp4?token=BIEAy3vdmluZN5SNWPblxj-OosM7qBY3JLLQ8ZT51eruVBCU0vFrQ1oCwkXxzHlGVfIe3LnnnFhhm1hZw1OwFcb_-q2Z-os0mDMB0VO5aedC1-Y2qtNi0HcUrw-JEEiv57sWVr8zhX68ThZGU8-rmtnan4lPU2yzQucmVGC2fq6__osioO9LEPcAVjR5mtiqUBpJVOyVU3xdhdfgDzMYEfhbEwiJcdCWWC5oSM0Gic1Qg6j__BiX1nMPsQLGab6uy5GRfxlCm-XlUos1Umo5vKn-qfRlqjFMvfbjqnSKER_aowUo73bM2Ei8DgFCFp-s8LINdicnk4FP2tQ9u4D0rA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
ترامپ: از اینکه ایران پهپاد شلیک کرده اصلا راضی نیستم!
خبرنگار: شما گفتید که ایران آتش‌بس را نقض کرده. آیا این کار عواقبی برای آن‌ها خواهد داشت؟
ترامپ: خب، به‌زودی متوجه خواهید شد.
خبرنگار: آیا آتش‌بس همچنان برقرار خواهد ماند؟
ترامپ: از اینکه دیروز شلیک کردند، اصلاً راضی نیستم. در واقع ۴ شلیک انجام شد که ما ۳ تای آن‌ را ساقط کردیم.
@News_Hut</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/news_hut/66892" target="_blank">📅 23:43 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66891">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">🚨
🚨
🚨
صداوسیما: صدای چند انفجار در سیریک شنیده شده
@News_Hut</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/news_hut/66891" target="_blank">📅 23:38 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66890">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">❌
🚨
🚨
🚨
گزارش ها از انفجار در سیریک
@News_Hut</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/news_hut/66890" target="_blank">📅 23:34 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66888">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d178038cac.mp4?token=D7vSFAuJ1hspZZ4R9fWlnTKQNHHIr3BDTRucig38uTamiIYsY2EyyJ3Ut9VI-zUwu1fg0ydDSlzSL_ZOuX-MpTsm1sQQGpIwqp8o0NADOEy2f7tFCz-5DUVa9-xgYshcJcWemk9TDaV6CGjBmMkendMJqG7n9wsrLo1FAbU9G7qW5xTuvI3I6Hlimv7178aSCJZZmbKTdrjr9R6hM2tWD5BlFcRKM7bOt0LyS8D-9BKxFeBCcLeRxU73OwTe-QZ-CU7Zm-kTskCKxJVBPjRVZKShth1ztorZhJf1V1djsnhbN2EgTwgnIIivjMHOSl3FMDCr9fu9YDtUN9XXIs6jRQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d178038cac.mp4?token=D7vSFAuJ1hspZZ4R9fWlnTKQNHHIr3BDTRucig38uTamiIYsY2EyyJ3Ut9VI-zUwu1fg0ydDSlzSL_ZOuX-MpTsm1sQQGpIwqp8o0NADOEy2f7tFCz-5DUVa9-xgYshcJcWemk9TDaV6CGjBmMkendMJqG7n9wsrLo1FAbU9G7qW5xTuvI3I6Hlimv7178aSCJZZmbKTdrjr9R6hM2tWD5BlFcRKM7bOt0LyS8D-9BKxFeBCcLeRxU73OwTe-QZ-CU7Zm-kTskCKxJVBPjRVZKShth1ztorZhJf1V1djsnhbN2EgTwgnIIivjMHOSl3FMDCr9fu9YDtUN9XXIs6jRQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
وزیر مسکن و توسعه شهری ایالات متحده، اسکات ترنر:
خداوند تنها دو جنس آفرید، مرد و زن.
و زمان آن رسیده است که این حقیقت را یک‌بار برای همیشه در کشورمان تثبیت کنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/news_hut/66888" target="_blank">📅 23:17 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66887">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Dx0Btz8riW5TmIIjcEb6JQmgcQYWgg9Ie8x7ND2s-aLgvU1QU5k65I0a9QgAabda9LgdOF92AYOaFFyD5ippDu3CW66BxFgpe5CKmSbv3yPsq1rvyREqDTOtO7Glhg4oUaFuZYHEUbJPHrRCvKNrg7uyRIBraKP7udf4MeTW78f_0PijGjC6JyDW6bRedq10bB6_W0PbuybDSA9rdpXqY-9MRkYl9o6WL47XiUSvVWfwKLEg8g0mY6fuvxvfNLZjBNvA1FgpaeWZ7nvyk4wj0tiHqKqC_kTkjAk4ff9RuxwEnWo0KGuCLcNwDGd88I0-noGi-gd9Db40oS6siNPSeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
فروش کانفیگ‌های نامحدود
💵
قیمت: 380 تومان
✅
سازگار با تمام اپراتورها
✅
سرعت بالا و پایداری واقعی
✅
مناسب برای گیم
✅
تحویل آنی
❗️
پشتیبانی 24 ساعته
جهت خرید اشتراک پیام بدید
⬇️
@kaviani_vpn
@kaviani_vpn</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/news_hut/66887" target="_blank">📅 23:14 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66886">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b4fe545d1f.mp4?token=h0ewTieyGM-fgbtqwWIXuH-0YtlbBJ_lyRhVH9f_g7iqgT7Bgx9lvrHuoBrVfBkDZ8dCHsKP29ZceMYrdupgQc8len1iX5QRXtKXpLZAjsV6ApS645CrKcoPWRk0zLRt8FsrFN1kZD-CuRO5CdRLA48kVPCFYcljQiI8qv2aXv8I0ZGsvaHmFzpyZZKrNJFtiq1bOkkTJ2P0SIAmP0vgZj4DXcaXo83DnMSN877UBNFNPOKPOJMzDF06INoaQ0WIdYuwrMJyeIagrTGuVGI7mycUjzDnjOxh3RnuKhXhSCHUM0npdioRGbrgk-DfgpQXddlPBCEZzg9yciXLHdo93Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b4fe545d1f.mp4?token=h0ewTieyGM-fgbtqwWIXuH-0YtlbBJ_lyRhVH9f_g7iqgT7Bgx9lvrHuoBrVfBkDZ8dCHsKP29ZceMYrdupgQc8len1iX5QRXtKXpLZAjsV6ApS645CrKcoPWRk0zLRt8FsrFN1kZD-CuRO5CdRLA48kVPCFYcljQiI8qv2aXv8I0ZGsvaHmFzpyZZKrNJFtiq1bOkkTJ2P0SIAmP0vgZj4DXcaXo83DnMSN877UBNFNPOKPOJMzDF06INoaQ0WIdYuwrMJyeIagrTGuVGI7mycUjzDnjOxh3RnuKhXhSCHUM0npdioRGbrgk-DfgpQXddlPBCEZzg9yciXLHdo93Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
ترامپ:
کشته شدن سلیمانی یکی از بزرگترین اتفاقاتی بود که تاکنون در خاورمیانه رخ داده است.فکر می‌کنم خامنه ای و دیگران در ایران از کشتن سلیمانی توسط من خوشحال بودند.
چون آنها هم از او می‌ترسیدند.
@News_Hut</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/66886" target="_blank">📅 22:48 · 05 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
