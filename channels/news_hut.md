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
<img src="https://cdn4.telesco.pe/file/vUmC49vl6pGnpCEUl8hOqJf0S-cfXGkzQI3wQ0ASwSLcSn4sSNRvs3m7IEVl3nHzxgJjMQj4cgtzUMsSy3lSot_5Ne3czpGAhB9--qa4_DPhRRBpqNQAGnu9InomOJ_SB5z_lq9d5gUABdcqocttMte7zdc7xqw1kIVo0tMc9tLvEnAuGj5XgkhTFh-ldsFl_YhtdYKmFgPlVn8DUJYlT19wCGse8xC3ZYxZh2K30JxLBbxq-lvViNONd-wDCs1CdSIH3p1IZm2ectMjEgiqcSzvvkUjqblCg26pQm_5gm4X3hEUh7aM8Ce92MMeqZN0d9urzvYcK-xWzqaL4nZVSQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 106K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-28 15:29:19</div>
<hr>

<div class="tg-post" id="msg-71885">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Bz1fbC8rOuwh6n0ufRiicBOrhJ2W3GuhOd-6bzfdvBf_I_D4nD1TI0vQP6oP-FZGbD_zNQVkaHIiUCcdmOCMg_g4eieU-uS5aidRe13riK14zs-2YEl4VFJsw8eeKLH1erZb0GVyjYpAp3-mx86O9zit3Idi-OOR7Hf4BReRwOzCMiDnm63WXxGRxNSEftQIJxb8UpkikrQu2-Wq0DUOYimfDtK2oupy86mTG5jfgUw4ETWNOSOIzOJdUXU8expj5TnYGX3IBuSk_NLdbY-TcLTHWZ-XYaFCwlvS7IefCGW1dMgG7ObwEJR-MRg6iMRbPgcmHWXwwJLyBPXadJXfWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/U-AY3qFZ7yNGq_Ff4WAoGPw_WOHStATIZuZESOadQzx-3tT8Qr_cg6lti_GbkeYdo4RS5kv_6c-321S1Vi9Tz5f7k5dyqR2ypTI2X4Bn5NfMkgbXgQaFe36ymnsnqRhFicf18y5Yc8Ts_zaV4gjlY9i4vdd4S5B_4ZxdrDMVFqabjBwZVyxTyF9jIARnncq7F53MOIcygzskM-42GYDiGPo8g6Vi_usVd_c-_ymm-A7cy6-VVBYDU5EOHZ37i1QLtunXgvtzMQRIISERH6dNVWLH13NHu7xxi9uwft28s_lK5NBatqTgJRmWMz35bNQ00zS1qL3aL6iLyEM0CqrzOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/O5-b5b95OC08KmPDvL5LosIF3smD0JmMMIAQ_r3t8wQrhlnOGRC7-fVZ0k0MfhACQQzWlTMQ-B40JgpGNq1EdAGPH_dJir-dTY6t_yfrRYSTVVNBWiGXHXb8iHFviVvvPN7YvTz-xrRO5IyERW_Gz8XW-IbliPGY5V9WxqgVhJFlqPZ4idyEI7DoacQBYX5_hhi6zk_oAdTfzzHdHq-Hjn8Trha6ew3dtTBNkpz68dp4som4eXq9RU5N7qyBhTo10BacqSCzFSUBE2Ao4Pl-xRoEMZig2Riv37ODOsSvYE1Ja7jdGSPo3Sx6-Gu07L3kQHbsbwZdbvknEw6V7GEqNg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">انفجارهای پیاپی در نزدیکی فرودگاه بین‌المللی ملک خالد در ریاض
@News_Hut</div>
<div class="tg-footer">👁️ 4.24K · <a href="https://t.me/news_hut/71885" target="_blank">📅 14:51 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71884">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/974e7b2cdf.mp4?token=W5TMRFPmKmR2tNH-5JTkolfOLAjJ98VGPt4RRTniRj0RRZ3nuMbm5sh9l1kv71EzXpCG0jihs0RJBySS6a1Nfod4AwmGUMXUqYvngej4FL0f2RNoLVBa_koohr1qK-raMcihSq30iuwBjBdPrIHHZE8NVj75tzqwN1m5diIDoasrQnhh4RcnJASE8Rw1fBuJd9YMYQmzbnX50x71JG5ZewD0jA9RE9FnYdHYab6R20-7ZgmHnEvQkpxeDEs610f3oYKVSys2HPYaMOKAqRTgHa-mi_WvXMWZsIMhRYn5QRfRvknhpp1PAddUpw1gYHCKT9fSlo0v2iLHExI56h3piA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/974e7b2cdf.mp4?token=W5TMRFPmKmR2tNH-5JTkolfOLAjJ98VGPt4RRTniRj0RRZ3nuMbm5sh9l1kv71EzXpCG0jihs0RJBySS6a1Nfod4AwmGUMXUqYvngej4FL0f2RNoLVBa_koohr1qK-raMcihSq30iuwBjBdPrIHHZE8NVj75tzqwN1m5diIDoasrQnhh4RcnJASE8Rw1fBuJd9YMYQmzbnX50x71JG5ZewD0jA9RE9FnYdHYab6R20-7ZgmHnEvQkpxeDEs610f3oYKVSys2HPYaMOKAqRTgHa-mi_WvXMWZsIMhRYn5QRfRvknhpp1PAddUpw1gYHCKT9fSlo0v2iLHExI56h3piA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">طرف سوال پرسیده: سخت‌ترین قسمت پسر بودن چیه؟
جوابا جالب و دردناک بود:
@News_Hut</div>
<div class="tg-footer">👁️ 5.93K · <a href="https://t.me/news_hut/71884" target="_blank">📅 14:31 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71880">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/95e492d945.mp4?token=qHIJn0QecIDFgUDq1VAH6tGIT3_tof6t9pzt346nyxraVPRioLujXUszK2R9x04Y4Bq4mpDpISjWYZygCK2zHxAClSZ0Z6ZGqWkpnXlcDfczmCeqXrY3rmw15WL5yt7Y6gfjSjmVq9ABIvbacKrui0CRU1exszHV0xvFxEFFgLNo1W-Y28sm8gDpGGloNlh2IcGMDk53in0R_ov-kA4NIS4gnG3dTh-92Kj6lAf26X658vRgdOQ0a8eJPboKYJHGn77t0M0xqgfeT2BSs-S30xRxrWU2NVnE8W-_FJhe1m7mWlU5UGQLgZMBbyKpTuQK2LO2HUlsi8Sbh2xiH3YG4w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/95e492d945.mp4?token=qHIJn0QecIDFgUDq1VAH6tGIT3_tof6t9pzt346nyxraVPRioLujXUszK2R9x04Y4Bq4mpDpISjWYZygCK2zHxAClSZ0Z6ZGqWkpnXlcDfczmCeqXrY3rmw15WL5yt7Y6gfjSjmVq9ABIvbacKrui0CRU1exszHV0xvFxEFFgLNo1W-Y28sm8gDpGGloNlh2IcGMDk53in0R_ov-kA4NIS4gnG3dTh-92Kj6lAf26X658vRgdOQ0a8eJPboKYJHGn77t0M0xqgfeT2BSs-S30xRxrWU2NVnE8W-_FJhe1m7mWlU5UGQLgZMBbyKpTuQK2LO2HUlsi8Sbh2xiH3YG4w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نیروهای امنیتی پاکستان عملیاتی را علیه یک هسته تروریستی — که گفته می‌شود متشکل از شبه‌نظامیان «تی‌تی‌پی» (TTP) است — در منطقه «کوهات» واقع در استان خیبر پختونخوا آغاز کردند.
در پی حملات بمب‌گذاری روز گذشته علیه مسجد شهر، شبه‌نظامیان مسلح یک مقر پلیس را به تصرف خود درآوردند که منجر به درگیری‌ای ۲۰ ساعته شد.
نیروهای پاکستانی اکنون این مقر را به‌طور کامل پاکسازی کرده و تمامی شبه‌نظامیان را از پای درآورده‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 7.48K · <a href="https://t.me/news_hut/71880" target="_blank">📅 14:02 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71879">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6895254ca3.mp4?token=NSrGMbpb8OMObJ2CnwmthfApIqfDxbRwINb0fv3VtfWKPysOYngByNku8cgRZG0amOMHTD-yBsT3wTuph3CTJzQy4D80OOUOoxAwzw920UYUtmosu8KwPIcSSYtnt9EVE5uikRHVilCQ6LaM4Rx5HwhcKpZrZSudUDImZJ5-tOISdCPy0KeYmjWM2YG1wrBTCGe4MbDkaC-pNNkjkLtdlCtRDXUZjxgVWtLFRxUMqbnx4mnhp0vJ92VWw1NSu-Y85VVQB3PXEWpNxawhbXM9g6j1hNO0YJm3ctoax5G85CrZj46jpfBHBhXGe2arGZwsSnQdqAA8yh0mv6a2ro1zAA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6895254ca3.mp4?token=NSrGMbpb8OMObJ2CnwmthfApIqfDxbRwINb0fv3VtfWKPysOYngByNku8cgRZG0amOMHTD-yBsT3wTuph3CTJzQy4D80OOUOoxAwzw920UYUtmosu8KwPIcSSYtnt9EVE5uikRHVilCQ6LaM4Rx5HwhcKpZrZSudUDImZJ5-tOISdCPy0KeYmjWM2YG1wrBTCGe4MbDkaC-pNNkjkLtdlCtRDXUZjxgVWtLFRxUMqbnx4mnhp0vJ92VWw1NSu-Y85VVQB3PXEWpNxawhbXM9g6j1hNO0YJm3ctoax5G85CrZj46jpfBHBhXGe2arGZwsSnQdqAA8yh0mv6a2ro1zAA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قبیله‌ای در جنگل‌های آمازون که با دنیای بیرون تماسی نداشته، از هوا فیلم‌برداری شد.
@News_Hut</div>
<div class="tg-footer">👁️ 8.91K · <a href="https://t.me/news_hut/71879" target="_blank">📅 13:31 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71878">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9fe570c529.mp4?token=EFx8L5WHAKrToZ3G9YmGuw1NqJ2vQrmHn-zcVjh2HHxSe-kLJvPlvD9oj7FyNI8WPqwqU4E6NSb9O9MqaYGLmICb5WicOQ5Vqab2xaXJCi8Hrws4MgghXPeyIUXA2OV-lQoLp8wnXLVujSfHQuxPiD5Oh7AnNQi4xQTfB57edZc6XKlCwdftTCasVr5gjLYxFVtpbFn544GuauUjQWGgEKkJ_JnxjBe95SUPDK9OUlvtwj37c9XbfwkXo_uADtOZsLu0AYgwjztck-jpCq-0ibTWaijKD1VSyctSOr8kYuohhg2Az6jGW8p6aaiVUgyX3yOnHrfa8tZBGWyUH-7WSA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9fe570c529.mp4?token=EFx8L5WHAKrToZ3G9YmGuw1NqJ2vQrmHn-zcVjh2HHxSe-kLJvPlvD9oj7FyNI8WPqwqU4E6NSb9O9MqaYGLmICb5WicOQ5Vqab2xaXJCi8Hrws4MgghXPeyIUXA2OV-lQoLp8wnXLVujSfHQuxPiD5Oh7AnNQi4xQTfB57edZc6XKlCwdftTCasVr5gjLYxFVtpbFn544GuauUjQWGgEKkJ_JnxjBe95SUPDK9OUlvtwj37c9XbfwkXo_uADtOZsLu0AYgwjztck-jpCq-0ibTWaijKD1VSyctSOr8kYuohhg2Az6jGW8p6aaiVUgyX3yOnHrfa8tZBGWyUH-7WSA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بیبی می‌نوازد:
«نصرالله کجاست؟ بعد از من تکرار کنید: حذف شد!»
جمعیت: «حذف شد!»
بیبی: «سنوار کجاست؟»
جمعیت: «حذف شد!»
بیبی: «هنیه کجاست؟»
جمعیت: «حذف شد!»
بیبی: «با خامنه‌ای چه کار کردیم؟»
جمعیت: «حذف شد!»
@News_Hut</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/news_hut/71878" target="_blank">📅 13:09 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71877">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/71877" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 9.39K · <a href="https://t.me/news_hut/71877" target="_blank">📅 13:09 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71876">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lerTSedMnYIHbUqzfrxWOC1gfnUAPV4W_6AcanVfVtjtwZRqQEfhgKMWdPPYL_PEfYW4zj2U1lSAWxhmIJaSOILwQZDGMN5NvavVWfuoT_x1CR9D42N15K1lKLUoKHS9X7HU5Lew9i60RYd3vg-uOuyJ61qe9EzRVjqFl_6q8Q-gdSNMyO8uI5aC15pkNHBCofQmLjBSHRW2XEqVU5ufV6iCI90BXWmetWIR3jb4zP4OR4QSK4_VbIXGLoFQlidtXP_ZmD7Bvd7fUpx5n6i1kneYNaAztaLHZ1yWJ5ETL3lwaRKqtG-TOaoqYSOeSLwICQdWvC3K4_LCgyJQtUV8cQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
مچ‌های مهم امروز در سایت بین‌المللی
TrexBet
استون ویلا
🆚
تاتنهام
آرسنال
🆚
برایتون
بارسلونا
🆚
سویا
دورتموند
🆚
اشتوتگارت
اینتر
🆚
رم
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
انتخابت رو انجام بده و آماده‌ی هیجان باش!
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 9.49K · <a href="https://t.me/news_hut/71876" target="_blank">📅 13:09 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71875">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e25ecc6de4.mp4?token=AY33DIeiNs8SaHcNcVmMANXSlN7qGFVEtrI-Pi0iDltArys-lvj6QSWZ_JJVu41zIxm_Kr7PvY_3iCxW2gkyaSawT5U43w0ms-fm_7HwZX6ejc0lTSKUXI2LIK-m5ZCGb871Hi-4LXXiIK5_cglz13NIjhUhVLZHe58neH2dX20HVPEY7al640wDHQUQrTFg4-cg83ct78hPR7XiR_aRTQ7AM_5EX3Z5l-2Y1AHseYiXAIV8kaNaQh70-hSb_Ofitc1JWKo55qIlDOlbyGEx6J5yiNFZSxexUX2ZlMHJhagCesC81s186rOtWs01kpRyMlv8mQU0Z91-xVXSnp5CHhm_haTS2MvGcfqgbsbzh_T1ZM4rtWSe742znAOwMGHppQnG8RIOlPVB7uC_JkAazZNNrQvyJBhRpF3MFEbdLUeSMiJhE1vQsxRHN0RoDAxnkbuVLoUOpL3QFGi4w2UV-sBX4Nh6LUKi2AIZF3NAFi5UOZSeoXm9aIFRWGS0MAd6NiCz9VPEawC_YQvaGCFcwNU1bZN9Hza3eQb-SExDdcvTJDmmIye2f1-c3V1wCdn8CjSW89ZDj2_ark4YHkCd8ttJyXOp2uegBmX-TqBqBqpTnBaiVoMLQqvjCHpRemPgJyfIsH8HZbDhDgUUrGfi-MqTOQjA43nLi985lPwDY7o" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e25ecc6de4.mp4?token=AY33DIeiNs8SaHcNcVmMANXSlN7qGFVEtrI-Pi0iDltArys-lvj6QSWZ_JJVu41zIxm_Kr7PvY_3iCxW2gkyaSawT5U43w0ms-fm_7HwZX6ejc0lTSKUXI2LIK-m5ZCGb871Hi-4LXXiIK5_cglz13NIjhUhVLZHe58neH2dX20HVPEY7al640wDHQUQrTFg4-cg83ct78hPR7XiR_aRTQ7AM_5EX3Z5l-2Y1AHseYiXAIV8kaNaQh70-hSb_Ofitc1JWKo55qIlDOlbyGEx6J5yiNFZSxexUX2ZlMHJhagCesC81s186rOtWs01kpRyMlv8mQU0Z91-xVXSnp5CHhm_haTS2MvGcfqgbsbzh_T1ZM4rtWSe742znAOwMGHppQnG8RIOlPVB7uC_JkAazZNNrQvyJBhRpF3MFEbdLUeSMiJhE1vQsxRHN0RoDAxnkbuVLoUOpL3QFGi4w2UV-sBX4Nh6LUKi2AIZF3NAFi5UOZSeoXm9aIFRWGS0MAd6NiCz9VPEawC_YQvaGCFcwNU1bZN9Hza3eQb-SExDdcvTJDmmIye2f1-c3V1wCdn8CjSW89ZDj2_ark4YHkCd8ttJyXOp2uegBmX-TqBqBqpTnBaiVoMLQqvjCHpRemPgJyfIsH8HZbDhDgUUrGfi-MqTOQjA43nLi985lPwDY7o" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هنری کیسینجر و توضیح سه مسیر تاریخی ایران:
دولت–ملت
امپراتوری
ایدئولوژی خمینی.
@News_Hut</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/news_hut/71875" target="_blank">📅 12:30 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71874">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/beaae9822a.mp4?token=k4TXoXqPxcnZTC91Kwx6iximDeqzVjEB0QFlH8tdgDHgxQHH7z5oXn6vZaMB0wgVEp9GZRQSuX-7JQd37Ff2DOE4FRSq-_xsmCpJLhb62_kjEdv4ZRDDMwzPF2Qpj-mRYbZBuDxXvr3Cs1vG1BoEC1KmnFkQoTMZFo-4zI-35XM-gS3sSLbD2DUaHjti5FNl-mkUyjCebz74JovN0JzrFf_s98W7CEXWvfIojgm0pznTsEior4d6Sr2yBJMD6cXAaDa8A3J8VT-1TX9BoL5Yoz2GiH3szCq9zxXpxXrFfqf7vh5aRQJY7p9HEoy1MNPZOTmOklRCDbqg-vKwz1Socw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/beaae9822a.mp4?token=k4TXoXqPxcnZTC91Kwx6iximDeqzVjEB0QFlH8tdgDHgxQHH7z5oXn6vZaMB0wgVEp9GZRQSuX-7JQd37Ff2DOE4FRSq-_xsmCpJLhb62_kjEdv4ZRDDMwzPF2Qpj-mRYbZBuDxXvr3Cs1vG1BoEC1KmnFkQoTMZFo-4zI-35XM-gS3sSLbD2DUaHjti5FNl-mkUyjCebz74JovN0JzrFf_s98W7CEXWvfIojgm0pznTsEior4d6Sr2yBJMD6cXAaDa8A3J8VT-1TX9BoL5Yoz2GiH3szCq9zxXpxXrFfqf7vh5aRQJY7p9HEoy1MNPZOTmOklRCDbqg-vKwz1Socw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تئاترهای مملکت این روزا تو وضعیت عجیبی قرار گرفتن؛ گویا شوخی های جنسی برای تئاتر ها آنلاک شده.
@News_Hut</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/news_hut/71874" target="_blank">📅 12:02 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71873">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/77deac1aa1.mp4?token=d9cPwO5dCSkJcJ8a-Wt3V5-YCRVy3j4j2mjT3TmIiAoal99xXRNMIEQECqvVViwTNPgiIamOoPDAeEDyMuXPONXxyfeiIdAQasqSpkilOBnmbOjasjvqGScA5VAJxr-9sMCADtnWxhlMvn9AZiwD3pKp11Ds4Cu_opRc3myzxu9Q3J6gP4pwx24Mo57xDE5csW2fveEKLFIUfOEbMs5l8zwMlMUvS6KmZB3380M44oXfLDwbWF67wGccj3QFAnHGdYOvzPxbljAYhgKQ8KE6GECELAeqaIOn-NOo5iyaup-2uLEQ2VeRmm-gSGy6-heBD2VKLeBKCQDJDxisgznhWA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/77deac1aa1.mp4?token=d9cPwO5dCSkJcJ8a-Wt3V5-YCRVy3j4j2mjT3TmIiAoal99xXRNMIEQECqvVViwTNPgiIamOoPDAeEDyMuXPONXxyfeiIdAQasqSpkilOBnmbOjasjvqGScA5VAJxr-9sMCADtnWxhlMvn9AZiwD3pKp11Ds4Cu_opRc3myzxu9Q3J6gP4pwx24Mo57xDE5csW2fveEKLFIUfOEbMs5l8zwMlMUvS6KmZB3380M44oXfLDwbWF67wGccj3QFAnHGdYOvzPxbljAYhgKQ8KE6GECELAeqaIOn-NOo5iyaup-2uLEQ2VeRmm-gSGy6-heBD2VKLeBKCQDJDxisgznhWA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یه شغلی در کانادا هست به اسم آتش‌بان. طرف باید فصل تابستان رو در کابینی بالای کوه بگذرونه و هر وقت آتش‌سوزی جنگلی دید گزارش کنه. عمیقا حس میکنم من میتونم خیلی تو این شغل موفق باشم.
@News_Hut</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/news_hut/71873" target="_blank">📅 11:33 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71872">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d090aca4d2.mp4?token=LoDEQx3tY-2xutJZ5j76c83vwwmcAuuKCfGwXJlXXeYsr_wfhrVZrnSc5vDFKiDoPcs-0ms9gd6z4TkQO0YlGtkk5ZeiDJlpX9XIc8dfZQ8wpOBxEzlggkqsYFX6CZ-v6sgs3t8ojB0lDiYe26lv-JOjCfo2O5xV4Z65fzO-cUytqRkoyIj-Nw1RwrkpM_sLCAoE6Tj5Q5X_TNu9t224J_oJJtrWqqzs_hwUKdOB9SZzq3MNABnMdnYxDhL5oqRk9INbrwA8zwsme9eWywSpBoydxaljEXJGogRZVG6IxlxZE3L7TDr38LjRXVCTiwHyIiDFRFxWFhq_PeCd-KPg-A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d090aca4d2.mp4?token=LoDEQx3tY-2xutJZ5j76c83vwwmcAuuKCfGwXJlXXeYsr_wfhrVZrnSc5vDFKiDoPcs-0ms9gd6z4TkQO0YlGtkk5ZeiDJlpX9XIc8dfZQ8wpOBxEzlggkqsYFX6CZ-v6sgs3t8ojB0lDiYe26lv-JOjCfo2O5xV4Z65fzO-cUytqRkoyIj-Nw1RwrkpM_sLCAoE6Tj5Q5X_TNu9t224J_oJJtrWqqzs_hwUKdOB9SZzq3MNABnMdnYxDhL5oqRk9INbrwA8zwsme9eWywSpBoydxaljEXJGogRZVG6IxlxZE3L7TDr38LjRXVCTiwHyIiDFRFxWFhq_PeCd-KPg-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رائفی‌پور:
رهبر شهید به رئیسی گفتند چرا به امیر تتلو نزدیک‌تر نشدی
@News_Hut</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/news_hut/71872" target="_blank">📅 11:05 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71871">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/400c93a6ac.mp4?token=md6TyJlCg4zQXmSjrvrGu3IIgooD6bVp8xVB-D2ddneJw1FPsxuc_GcbkEkGA9nwo47-dUR97KH5ZbAHaB6Az1sttSXpJBmZW8IpwsF_bi9gcfYqH6ibSAUrgx0UdxX2Og3oyFr_Nfptcx4eioM8ZuSVVJMTghG5fGVFQ80I_5g0X9oSv3rjY-74dmbT9dUMlR6f-_m6TrFaHHgGvlwK9zTLimAa0Ouxy3OWncSlecOXzNamYixe5LESnZiM8rZn5JT2jp9if1Bbwum_noExkU55A2z18hQtrRezaIYryxU9oVVSsUzZjS6xOFSaByovjrbILLryfot7MDZWex-5iQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/400c93a6ac.mp4?token=md6TyJlCg4zQXmSjrvrGu3IIgooD6bVp8xVB-D2ddneJw1FPsxuc_GcbkEkGA9nwo47-dUR97KH5ZbAHaB6Az1sttSXpJBmZW8IpwsF_bi9gcfYqH6ibSAUrgx0UdxX2Og3oyFr_Nfptcx4eioM8ZuSVVJMTghG5fGVFQ80I_5g0X9oSv3rjY-74dmbT9dUMlR6f-_m6TrFaHHgGvlwK9zTLimAa0Ouxy3OWncSlecOXzNamYixe5LESnZiM8rZn5JT2jp9if1Bbwum_noExkU55A2z18hQtrRezaIYryxU9oVVSsUzZjS6xOFSaByovjrbILLryfot7MDZWex-5iQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پورن استار معروف ایرانی ملقب به «شیر ایرانی» با انتشار این ویدیو اعلام کرده که مسلمون شده و از خدا طلب بخشش کرده :
کاری به هیچی ندارم ، چرا وقتی میگه بسم‌الله ، با دستاش صلیب میکشه
@News_Hut</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/news_hut/71871" target="_blank">📅 10:33 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71870">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/40d28238ee.mp4?token=ZuQ5Ihi_2iuhJbOtDhglBOoiGuAit24XHcdlGQDtXXuevF_05nCChealQqoyWTPEFxZigTBcJagK7eaope_Tqq2tYeWSw4U0eAV-4Ok91X29XDvqHMnQ7hhjohV5nPiwLVTN7TEdIpyS2McVTRIMUEW54tsETVVZ8EJDxIJlJmZeLUsY3kPKDBkLJS2nNJHzx-1oPGardQhk4A7w2CT_DLm-FIKL_Dqlol0H9HALeUSRzDZaH4F3_p1yEpebY-wYufVYFyXqu35zXB-yHIAej4QORpZW_jYOxcfZichboDMOEatiUsHYSSVMxdzxU0RNxQo1-FYKp0VIjNcY9EQ2hQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/40d28238ee.mp4?token=ZuQ5Ihi_2iuhJbOtDhglBOoiGuAit24XHcdlGQDtXXuevF_05nCChealQqoyWTPEFxZigTBcJagK7eaope_Tqq2tYeWSw4U0eAV-4Ok91X29XDvqHMnQ7hhjohV5nPiwLVTN7TEdIpyS2McVTRIMUEW54tsETVVZ8EJDxIJlJmZeLUsY3kPKDBkLJS2nNJHzx-1oPGardQhk4A7w2CT_DLm-FIKL_Dqlol0H9HALeUSRzDZaH4F3_p1yEpebY-wYufVYFyXqu35zXB-yHIAej4QORpZW_jYOxcfZichboDMOEatiUsHYSSVMxdzxU0RNxQo1-FYKp0VIjNcY9EQ2hQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تو اسلامشهر ی موتوری خیلی ریلکس و بدون پوشوندن صورتش میاد گوشی ی دختر جوونو به زور ازش میگیره و فرار میکنه :
@News_Hut</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/news_hut/71870" target="_blank">📅 10:04 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71866">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/6655905e8b.mp4?token=pPptVCpzwQSzyTPnJvHDXkZ_wG4PbIyRLryqsgDuXGq2HRxCbeapPB_I9rf6mOQrZWxVQvnQJdaG24IGD3iDwGAJKWUuDq7xt_mhnv1mEDbI_7O9HD0ks0WQxPQaTq9wgno9AadU5S6gB8dg0_RYCVKV9wUhQP1pNhpshHQbOSsbypJjZymYOHwPee0n6lvkvibgEKD-A0Za1i8W_-LDJoj_84wtsRaeqKZ5VehSa3w31uMA6C-1mfK2PLCbD5gH4V2ZrxyXugYJBY60bgyaVKz4LUwU3E3ausz4uOcybDZZPErUILAgoOlBF_59jSdPdf6Hie24sGyVqmqBdNvSTQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/6655905e8b.mp4?token=pPptVCpzwQSzyTPnJvHDXkZ_wG4PbIyRLryqsgDuXGq2HRxCbeapPB_I9rf6mOQrZWxVQvnQJdaG24IGD3iDwGAJKWUuDq7xt_mhnv1mEDbI_7O9HD0ks0WQxPQaTq9wgno9AadU5S6gB8dg0_RYCVKV9wUhQP1pNhpshHQbOSsbypJjZymYOHwPee0n6lvkvibgEKD-A0Za1i8W_-LDJoj_84wtsRaeqKZ5VehSa3w31uMA6C-1mfK2PLCbD5gH4V2ZrxyXugYJBY60bgyaVKz4LUwU3E3ausz4uOcybDZZPErUILAgoOlBF_59jSdPdf6Hie24sGyVqmqBdNvSTQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شاید باورتون نشه ولی ایشون دختر نیست و یه فمبوی(پسر) ایرانیه که خیلیا روش کراش زدن و توی تله‌اش افتادن.
@News_Hut</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/news_hut/71866" target="_blank">📅 09:32 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71865">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cbf20c1179.mp4?token=LR23HCrn7oKwnnfI6IrpzVOtmMjhehr2yCm9p0E-dl0Zx072i8-lUbTdeYNHxnZIcRsenkv0UaD6eFBf080PydrYhsNe_CqC7zI9lFrT-3_plIMz9la3rUyVXcH1ysYuTJG6krwRZQeLKkcnYF_Cxx8Rg1gSEioeib9E1qbH8fSoHrTBgNg_L4FwUsUbEi3ogNxsQFdzjBzvhBiQJt6KbIrIHUQpmXj7X82ZzLypymzjIfGGvDFXEYAvATZyDVUauOsE43uZR5rOs1Fi8USPPXaaCRrbW_cWceHANsa7voAq2BjI1HmFF9R4MjSXGBiF-f5V25HrzZzojAPF-g2NY6xWf6V0ABmWNOmyOQaOlRSw6Ez6Tra5K910ylimu3ksOgXyOXOXmXEyf4_wpzdFJo0b4u18_vRFP4iSL_1iYoSBFEXLS1p7yVBkSXeRNiqafZfLvbZSD_R2sBdVBq8mELE7F2L9bLixfNLxqNs3mlsGhY6A-GPh0Cggq7O856gpZVFQFH4ZY32XhbaseF-IcPGblQUTqY8LWWOIZz5u3jMkG0TFNJqtZTBv-SbXLK9vGquwD7p6037mRtSSPcfrPvUiyLxVX7oA6-Ri0BODNWHZ3CpyuxqzqDKtLt0IAlcaTg9KfkDCThU0Rg-VAFWyMnVnvO8wRDtSzlUfF7dtVN4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cbf20c1179.mp4?token=LR23HCrn7oKwnnfI6IrpzVOtmMjhehr2yCm9p0E-dl0Zx072i8-lUbTdeYNHxnZIcRsenkv0UaD6eFBf080PydrYhsNe_CqC7zI9lFrT-3_plIMz9la3rUyVXcH1ysYuTJG6krwRZQeLKkcnYF_Cxx8Rg1gSEioeib9E1qbH8fSoHrTBgNg_L4FwUsUbEi3ogNxsQFdzjBzvhBiQJt6KbIrIHUQpmXj7X82ZzLypymzjIfGGvDFXEYAvATZyDVUauOsE43uZR5rOs1Fi8USPPXaaCRrbW_cWceHANsa7voAq2BjI1HmFF9R4MjSXGBiF-f5V25HrzZzojAPF-g2NY6xWf6V0ABmWNOmyOQaOlRSw6Ez6Tra5K910ylimu3ksOgXyOXOXmXEyf4_wpzdFJo0b4u18_vRFP4iSL_1iYoSBFEXLS1p7yVBkSXeRNiqafZfLvbZSD_R2sBdVBq8mELE7F2L9bLixfNLxqNs3mlsGhY6A-GPh0Cggq7O856gpZVFQFH4ZY32XhbaseF-IcPGblQUTqY8LWWOIZz5u3jMkG0TFNJqtZTBv-SbXLK9vGquwD7p6037mRtSSPcfrPvUiyLxVX7oA6-Ri0BODNWHZ3CpyuxqzqDKtLt0IAlcaTg9KfkDCThU0Rg-VAFWyMnVnvO8wRDtSzlUfF7dtVN4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بنیامین نتانیاهو، نخست‌وزیر اسرائیل:
«آیا خواهان جناح چپ هستید؟ (جمعیت: نه!)
آیا خواهان جناح راست هستید؟ (جمعیت: بله!)»
«آیا خواهان تشکیل کشور فلسطین هستید؟ (جمعیت: نه!)
آیا خواهان کشوری یهودی هستید؟ (جمعیت: بله!)»
«آیا می‌خواهید تسلیم شوید؟ (جمعیت: نه!)
آیا می‌خواهید بجنگید؟ (جمعیت: بله!)»
«این جوهره‌ی این انتخابات است: یا چپ، یا راست.»
ما در جناح راست هستیم.
@News_Hut</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/news_hut/71865" target="_blank">📅 08:54 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71864">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">🦖
اینجا فقط ضری ب‌ها نیستن که می‌درخشن...
🦖
چندتا Star آماده‌ست برای کسایی که توی قرعه‌کشی شرکت کردن. شاید قرعه به اسم تو بخوره؛ امتحان کردنش که هزینه‌ای نداره!</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/news_hut/71864" target="_blank">📅 01:36 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71863">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTrexBet IR</strong></div>
<div class="tg-footer">👁️ 3.4K · <a href="https://t.me/news_hut/71863" target="_blank">📅 01:36 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71862">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">#فوری؛دونالد ترامپ، رئیس‌جمهور، «قانون لیندزی او. گراهام برای اعمال تحریم علیه روسیه و ایران (مصوب ۲۰۲۶)» را امضا و به قانون تبدیل کرد.  این قانون، تحریم‌های قانونی، تعرفه‌ها و ممنوعیت‌های اعمال‌شده علیه روسیه را گسترش می‌دهد و تحریم‌های موجود علیه ایران را…</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/news_hut/71862" target="_blank">📅 01:27 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71861">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/apiee6y2ZPrSJbu1xKkiYldxCVUGd6qUJdg3YWe1OKZHoQGil0GapJeX21kBO-Kbbow4m6fYLtPeIozPZ5RFuUvifGXVsR3BfUHXU5qatgMd3nbzUXbVDFXQwdBASlG4Z4FRrdKbZSfY6FboHupM_sOyOzK-iqvF7j5P7UZKPFlciXFWWdvrZX6YX-X65MsJl61Pe316ittdTgX0YIturYuT2PiY96KcraFn2WsXkNBkZZibuXojbIodICSTOMFgtSyJ-sl7ljLZJu0XeAykFHX28VxuxluJttpdBscnT5JPSZFARn1DAkiNZbN1PxlbLkFhMPcZou5WbVIBhw3osg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#فوری
؛دونالد ترامپ، رئیس‌جمهور، «قانون لیندزی او. گراهام برای اعمال تحریم علیه روسیه و ایران (مصوب ۲۰۲۶)» را امضا و به قانون تبدیل کرد.
این قانون، تحریم‌های قانونی، تعرفه‌ها و ممنوعیت‌های اعمال‌شده علیه روسیه را گسترش می‌دهد و تحریم‌های موجود علیه ایران را تمدید می‌کند.
@News_Hut</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/news_hut/71861" target="_blank">📅 01:24 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71860">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">ترامپ اعلام کرد که ایالات متحده با دانمارک و گرینلند به توافقی دست یافته است که بر اساس آن، واشنگتن اختیار دائمی در خصوص الزامات امنیتی آمریکا در گرینلند خواهد داشت، در حالی که گرینلند همچنان تحت حاکمیت دانمارک باقی می‌ماند.  ترامپ این توافق را توافقی با «عمر…</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/news_hut/71860" target="_blank">📅 01:05 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71859">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NjXEzXm5OpVFVaE_db-WtyWrLeGqJd8nxMYt64JSushTsEihaqeBZRqYQhZOtj213c55grFdIHmBbbX4l2nDGoeS_7Vk1CWFbsZCEW42Gc2Ik4a5iKl1ilGmS_WndW6s4Yps2E__8W56unq6jgF6OO9FcdnoI2CJinh0U16gN1Rjs2OKac0mgEBGqDL0jqn15XF51-675B2QXWb9w4CQRmO9jBU_7pDl1EwPLyq49T4Soq7qvPwwxlAArkuQXek6dEnkEJujHG5AnudO6__M7yrfth1L5hhGtY7d7ad1Veq6jdAVTolKC16XlPeQ5wnFphImzcPDZI3v_TiadBbfhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ اعلام کرد که ایالات متحده با دانمارک و گرینلند به توافقی دست یافته است که بر اساس آن، واشنگتن اختیار دائمی در خصوص الزامات امنیتی آمریکا در گرینلند خواهد داشت، در حالی که گرینلند همچنان تحت حاکمیت دانمارک باقی می‌ماند.
ترامپ این توافق را توافقی با «عمر نامحدود» و «بدون تاریخ انقضا» توصیف کرد و اظهار داشت که ایالات متحده قادر خواهد بود اقداماتی را که برای دفاع از گرینلند و آمریکا ضروری می‌داند، انجام دهد.
وی همچنین تأکید کرد که هیچ‌یک از دشمنان ایالات متحده اجازه نخواهند داشت بدون تأیید آمریکا، در گرینلند حضور نظامی داشته باشند، پایگاهی دایر کنند یا سرمایه‌گذاری‌های حساسی انجام دهند.
او می‌گوید این توافق برای ایالات متحده «هیچ هزینه‌ای» در بر نخواهد داشت و واشنگتن بلافاصله روند گسترش حضور نظامی خود در گرینلند را آغاز کرده و در زمینه ساخت‌وساز و توسعه با مردم گرینلند همکاری خواهد کرد.
ترامپ این توافق را «تاریخی» و «تحقق یک رویا برای ایالات متحده» خواند.
@News_Hut</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/news_hut/71859" target="_blank">📅 01:03 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71855">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SAcPkJOZ8ke2Ek6OATSFXP1eSUXYhiL35catWjo59ej6Mcey9W6G_0VH4yGJryrwVm9rkYu2z2R6aRWL-LhdHqWEIr9Gz7GV-7-NITUMCJlKqwybPvjHvER26_obS53-zcXUzgMBC72nAUNvoBQwgONlpXZoufVh06s5r_m-8jrAztd9BoQMUHxtAZ20v76mCD8imwmOWJH5CZVzoD_-ZzGDrgfXftEkTWWqXBWbb3eEJYQjkFlukY8mFfU7xJ6EGwDsFskKVUdOQddZxcwSoaG-ofD32pxnBeYPoLePPTxULqh3rAkNSei1mQ_Bpu3SlQF-MgwocSj5nfKcwBzctA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ojR7vSyCB-2nGq7gOgUtstA-guKpfUhftYST-FYRwKofTH9Nlobz3VgK3UPVFX1z_VEwb5bBewbykNzkJrsgL1cwmHq5WGall0QzNtqvdFn3Fhn3LGGmPgayqib3YisGZYCq768lcfadTxoiIbu0k2Yvjdi0lvcWEYl5O8hvLOv7Y84FE3MqfOvLuwPS5zSP4HUCRNn7GVKYw2nk-WUXq5Nq5toYxnTLrvB3t4dQsNZY5hoDxL0PE_krJQumzIux1HtSHx6bt3AU33hH3aGmjU-wX5vYX0LK6P2NWoc2G47KcJ3jd8GChlXuOHLqqPRbNvbnoDt3B865vzpo3r7WJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SpZHDr4jJVnvyuJtVWgivT3M7jrfJMXzD_NSqH7oqKbRrH901E1YHmLyw2Ybih0fI34fzGanvBlgWZvzeawjMtFk7gCsBz6qyt-mttt9_bFlkgUnEsrBDjXLZ4WhsTg8FwRXvhY_HMmdaYFuJS_8Mvc-8wzZPZKo7LYcihmTkokfiRrJRS73R0dkCRO12oyFycmFkWapNbw2HqL8uOAXQLN7j70H9ywtIEPc9wXHEe4yrNg5kw36ICRlbcAfqwUHY3vygpq8OsiljFK2gaZgi2Do70Yg5zSw43P9RifPYd5z9pmA08ZXXsW0Mo55ZnuZkfsULe3JYy1UENAucmDtsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pp2YOb79Nlou4tE64usHV5LayFbZxOlBYfkvHYSW8VZsRtXcIyM_aTf5mJelC7jwKZ48AMF8JtmFhLlgQi1AljM23tFPmbccnpf9Q6VcUhPJ-0TfROZYUeWyOQU7pIihMCAvlSBFEhkF-ALAFeAMEZfx5lsdpiYODZ2XtBokfR2bc2dwk5YKiCIqiGB4n9GNbYRtfOFgeAwXo73VI9BoHTmcMEbJa5lyHdZ9GuEkhtb0wq4GTvMDpI5fH4rA_y9qzmrwxO526sbdo6scJoB34u7et1GeHWkfDuVAvgyXTejyUvDEj02NY-jcKaw7EqeVWLgrcqxtkAqhDWRB386mzg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">سنتکام:
تفنگداران دریایی ایالات متحده، وابسته به «یازدهمین یگان اعزامی تفنگداران دریایی» مستقر در ناو «یو‌اس‌اس باکسر» (LHD 4)، هم‌زمان با حرکت این کشتی در دریای عرب، به تمرین هنرهای رزمی می‌پردازند.
@News_Hut</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/news_hut/71855" target="_blank">📅 00:31 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71854">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4866c3cddb.mp4?token=RFYOI9ff1f99GRl1LaFJJCBibPuVqbipcUQAJNXi4CzSBP9kquCrct4cmcbPnqKC1VO0j2sXVEplAUL2TOR1HXD0NHJChG77p8pb3V5M2-6PBtq_j8loRr91DwiPmo4oUvJ97wDMfzxjo7Qc7mU15Hn9hc28wFP_DKmt6nlvwLNtV7zy7MLyaUWwn04yDCq5SxB6LFze7ZsHVg58Jr_RS6-hIgyLJgPJVX2pUZym61DXIT57jB4UI9mX_ZhxUKvBpzNla0_pMgRSW7iIbrajzfm9VnX2B7ECm9g1pLRNAMVxxp4rUQyX7e5T8YjujvXpO-8kLQApcnL6GfdiF_nHkw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4866c3cddb.mp4?token=RFYOI9ff1f99GRl1LaFJJCBibPuVqbipcUQAJNXi4CzSBP9kquCrct4cmcbPnqKC1VO0j2sXVEplAUL2TOR1HXD0NHJChG77p8pb3V5M2-6PBtq_j8loRr91DwiPmo4oUvJ97wDMfzxjo7Qc7mU15Hn9hc28wFP_DKmt6nlvwLNtV7zy7MLyaUWwn04yDCq5SxB6LFze7ZsHVg58Jr_RS6-hIgyLJgPJVX2pUZym61DXIT57jB4UI9mX_ZhxUKvBpzNla0_pMgRSW7iIbrajzfm9VnX2B7ECm9g1pLRNAMVxxp4rUQyX7e5T8YjujvXpO-8kLQApcnL6GfdiF_nHkw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرنگار: آزادی مطبوعات در متمم اول قانون اساسی تضمین شده است.
ترامپ: ممنون که این را به من گفتید.
خبرنگار: آیا سعی دارید با ارعاب، مانع از انجام وظیفه مطبوعات شوید؟
ترامپ: نه، نه، نه. من از مطبوعاتِ غیرصادقی مثل شما خوشم نمی‌آید. به نظرم شما افتضاح هستید.
@News_Hut</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/news_hut/71854" target="_blank">📅 00:04 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71851">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0c6db95143.mp4?token=bkn3a06KhFzW4QKmqwt2VMfchXgx7QBkZcwwf6ClKPEXazvIrMGFhDUJ6_L74YVA4rEhpEt-cCmhiGCXYNEW53mAeEvlNnGmUEHzq_VuQCRYznOBvc_Ip8nTsXlktVlL-CAbdNDTO2dNXaz3epOqNQK6Hz29eRDUq8HKzDkPvlWYCbv2-WKavNRB_yi3EHR51mPpKycY_8EMKhrWrmvJino8ohHb198TdPPJZgeggFy436sKL349ozEaX1BN6V2FKqsNZzTDl7oWkc_gSsMyPiflX2T6SrSUqgSbzisKgpeSqDR5KJ-FR19n83CGBNhMLnvVfF3WrlYDMlPGFPdOpQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0c6db95143.mp4?token=bkn3a06KhFzW4QKmqwt2VMfchXgx7QBkZcwwf6ClKPEXazvIrMGFhDUJ6_L74YVA4rEhpEt-cCmhiGCXYNEW53mAeEvlNnGmUEHzq_VuQCRYznOBvc_Ip8nTsXlktVlL-CAbdNDTO2dNXaz3epOqNQK6Hz29eRDUq8HKzDkPvlWYCbv2-WKavNRB_yi3EHR51mPpKycY_8EMKhrWrmvJino8ohHb198TdPPJZgeggFy436sKL349ozEaX1BN6V2FKqsNZzTDl7oWkc_gSsMyPiflX2T6SrSUqgSbzisKgpeSqDR5KJ-FR19n83CGBNhMLnvVfF3WrlYDMlPGFPdOpQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره ایران:
اگر قرار بود رأی‌گیری‌ای میان «کاهش قیمت بنزین» و «اجازه دادن به ایران برای دستیابی به سلاح هسته‌ای» برگزار شود، نتیجه آن یک پیروزی قاطع و چشمگیر می‌بود.
مردم نمی‌خواهند ایران سلاح هسته‌ای داشته باشد.
@News_Hut</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/news_hut/71851" target="_blank">📅 00:02 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71848">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JMULTtC3_8un0139AVoPCzBDTc7gsMUfNkTJpSmQ5x_Hiwu04XuXG2P8VwKL5PdmaGc1QxfBuoUXVQzUqJzjQzGIV_7parcQbg-rvcafVs7Ve8MvKTxYx1UplZ319TKhhf64R2mJ7SXAoTWa-ZiRe6eXuoDHlU28Q1_JlXnucegRGn1XA3EqSaRdg6mS4gqyGYfEqM3Y6bFd6-Y7zOec7qAqtMUUMPguXIXwGXemh95uY3wzlvRS8qbxPXo7SAtUpglTocY3L31wKPHeIvz0rTK-erq0H3RKuCwsmwACPOHEXsMLVbTKD1YVKSR52t-MZ5HTmzVW-GawC5ceRNGqRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WaMGNr1xAd17aqBzCG_jGb-M3i7BrDHlAYONHrC2kJCRz4Q4Ph4B77tGEU6p_OzRoeyEyD0Y0TGMYKC5VztZBgCiLLFdnKFNb_fx81-ESWkVFPjGWlNK2HVsVwlGlctg86d14zJXXnvZdXxd7tAmp_FR4_ncbEZNPF_cvWq6uUlVcQSoN_4UOUU6VgJAkfM2RjywqCnpm62DV-YgXkXr2Y51tp55a1gUaUFOFvBjcF2dxpk4HtlcCR61JND8sthjza8b2k_JG-xbiyHARWZTUePPEAmX8t5SVn-tqinfnqpmmKaHB3nlcFC13S0eT8PA53au3QT76bMBLe4dMsth1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BYFjyFCN9n59r0kxDcTPo4pesMjIYPRP50y5GuyJbpUXmna_d3pBXSO5DinVbsIfIWp4LJorAXSJLIeGeIuOJp2ejP5UdRxWAc91ZHoDm0GER3MB-4dP8ZrG5YzFybEDTPqWyI33m8-HP3LUj_TIkA3XaphZwlAXbRU-zp9mIQssGlsTpI4oJ6lIWlQmQYTwwou6sSSjhQHwS72ITkDrB6tA1uDumfjS5Ca6Tm_hSVoOb2v0SZYrd7uIGGRcaZq2P-SgM8xHKVjfQIdDNWhlcBu-zufFN5TdVp8UbHEQLP-kl01r66-5ERUBubh7hKkwegAoEYu_XqOvXWMfNhi4cg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">گردان های بانوان جانفدا تو همایش امروز:
@News_Hut</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/news_hut/71848" target="_blank">📅 23:34 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71847">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7102741190.mp4?token=kDd-FL77X8lD0DCl40Aq8ZIg4o5gDQGAnBQLtxsALNMkNj_dpGgPg8iRMnFu5wRVoez3WgRHGf-Ufkqf51AzOKNWOHvRZ9rVqmKgIBBHt4b0Cq7n1GC2HGyAxfUaQE_NNVZtkrHsV3zbRi2pUnEfNyjn6_mjb1HAcYFKA6l-9xUbSDpu9PclvLzPgZNCwcn2Se-WZ4WdFesJNSsX4FIOzC8oyFkUu8ivmuM_YJ1ExhkY27YBjwHaQjaLt9Evwhtqi-JI91peDR9I69XAIgU1d7hrme-tJYaQ_V8SKyI9pcB_MijgrbFJYc0_YSlouT0NswPDcCJIu1cXNdeUovzRPw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7102741190.mp4?token=kDd-FL77X8lD0DCl40Aq8ZIg4o5gDQGAnBQLtxsALNMkNj_dpGgPg8iRMnFu5wRVoez3WgRHGf-Ufkqf51AzOKNWOHvRZ9rVqmKgIBBHt4b0Cq7n1GC2HGyAxfUaQE_NNVZtkrHsV3zbRi2pUnEfNyjn6_mjb1HAcYFKA6l-9xUbSDpu9PclvLzPgZNCwcn2Se-WZ4WdFesJNSsX4FIOzC8oyFkUu8ivmuM_YJ1ExhkY27YBjwHaQjaLt9Evwhtqi-JI91peDR9I69XAIgU1d7hrme-tJYaQ_V8SKyI9pcB_MijgrbFJYc0_YSlouT0NswPDcCJIu1cXNdeUovzRPw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این خانم تو بخش پذیرش یه مطب کار میکنه. حالا به یه بیماری برخورد کرده که یه فامیلی شاهکار داره و باید از بلندگو صداش کنه:
@News_Hut</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/news_hut/71847" target="_blank">📅 23:03 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71846">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/edd80b92b5.mp4?token=CasySSJugveuLCEjW2_Ry27Glj9_zhAfObQ9zTzou7Sd78l_brthCJLFk1EVROVjpz69fEThoGw0ATSAQlFPmdquZdYnbK19TLNz5y4-_wlojK95OsGLKCrOu1a9plUgMyG_7CcIdbbKB6WkN6G0isH3WTyeK9D9KUfL1hq4KRan3folIBGRMTcrrMklaoysQ3R3rF2CeRxttmHJJhsAl17WsFn2us1iOtp7V_le7obRQKLbSKDvvVKnSITcsTeB4Kj-ln4U9N7aFp8TklkEbDp9lzH7OoXQCVTXoAran6DQiwCTbTk3MEUzmNI_43Q8MUTsBzvLOqsTmJ3WMOGUeA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/edd80b92b5.mp4?token=CasySSJugveuLCEjW2_Ry27Glj9_zhAfObQ9zTzou7Sd78l_brthCJLFk1EVROVjpz69fEThoGw0ATSAQlFPmdquZdYnbK19TLNz5y4-_wlojK95OsGLKCrOu1a9plUgMyG_7CcIdbbKB6WkN6G0isH3WTyeK9D9KUfL1hq4KRan3folIBGRMTcrrMklaoysQ3R3rF2CeRxttmHJJhsAl17WsFn2us1iOtp7V_le7obRQKLbSKDvvVKnSITcsTeB4Kj-ln4U9N7aFp8TklkEbDp9lzH7OoXQCVTXoAran6DQiwCTbTk3MEUzmNI_43Q8MUTsBzvLOqsTmJ3WMOGUeA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حرکات عجیب مجری شبکه‌سه برای توضیح عملی دفع سنگ‌کلیه در برنامه زنده!
@News_Hut</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/news_hut/71846" target="_blank">📅 22:15 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71845">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/46fca26fda.mp4?token=YZYNVUuPEQjciXiKghlKB8wXaE4XfEPsDrJECn3Np5nZhYsUcCbAWprkLTRt-LpFo4ZhXPaPNFwXAtBPTMBXqAD2lWsDMJMehLRvlP6iZK-J_rI5Pbz9_1sk2nsCVuJ__Nqb4S4E7bv0iO7GT4bbE-fclzeGHZSWlV-c2dca_-MqHIM0YYEgJT2kXAJP2EqbV0XgRBOyrhOZeGPq_Wbw0oGbYXw7xaBONvuQBpQAqGqu0SqI1x8ofUsNnRTZXmKSkU73q8woZniGkpLunIhneTx-VVE3DpEy8ik7gv2fZTYZ_HZEWxE8FFHGgvbk12qetH0avRa33FXAtiqOqDg5ug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/46fca26fda.mp4?token=YZYNVUuPEQjciXiKghlKB8wXaE4XfEPsDrJECn3Np5nZhYsUcCbAWprkLTRt-LpFo4ZhXPaPNFwXAtBPTMBXqAD2lWsDMJMehLRvlP6iZK-J_rI5Pbz9_1sk2nsCVuJ__Nqb4S4E7bv0iO7GT4bbE-fclzeGHZSWlV-c2dca_-MqHIM0YYEgJT2kXAJP2EqbV0XgRBOyrhOZeGPq_Wbw0oGbYXw7xaBONvuQBpQAqGqu0SqI1x8ofUsNnRTZXmKSkU73q8woZniGkpLunIhneTx-VVE3DpEy8ik7gv2fZTYZ_HZEWxE8FFHGgvbk12qetH0avRa33FXAtiqOqDg5ug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گفته شده بعد از انتشار این کلیپ، ترامپ از ترس ۳ روزه رفته تو اتاق درو بسته و فقط داره می‌خنده.
@News_Hut</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/71845" target="_blank">📅 21:34 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71844">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/K0XuCmFUZIPN5oY-BYEQ-G3nxh9a7EUH_3PX3EZ4Z2qYFv6Bx2srQlMLW-TlEFEoloQGLlSJXWQwJTJAzMNtJezPrt8rfdTrEry9Z6ymXQJzWq65BsJLizRGKB5sllQ24i2Zp24uCu3tJcOXNgg-M59CBj3Np--lqBWkvI6kPwsVDaSdwoOYyP-OuUAHMC_8UoPdqGxb2ky-RYGrKE8TY8Y3nZ0fvp9NRl38yLke7miYREQdyiOVHFq0Wsy3Y39mCXjurZRWT9qM86M0Sab-RUNmlonNWnGsAfMRqaw14mNYuHzZCqpEawJ9O4KJ2FK1DBKOwVx0q7QCxgRy31AbUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امروز September 18، روزِ عشق اوله
❤️
این روز بهانه‌ای برای یادآوری و زنده کردن خاطرات نخستین تجربه عاشقی در زندگی است.
به عشق اول و آخر زندگیت تبریک بگو و این پست رو بفرست براش
@News_Hut</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/news_hut/71844" target="_blank">📅 21:25 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71843">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">نیروهای «ارتش ملی یمن» (تحت حمایت عربستان) تصاویری از انهدام ۹ دستگاه خودروی نظامی حوثی‌ها (انصارالله) با استفاده از موشک‌های ضدزره (ATGM) در جبهه غربی مأرب منتشر کردند و مدعی شدند که تمامی سرنشینان این خودروها کشته شده‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/news_hut/71843" target="_blank">📅 20:50 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71842">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gws3pY34YWPQlAzmvRhtQrjgMloYRWVF1nAY9mN43xaFqoUJpNUxfhQ0BdRldAqMYx8h1hAdedXtC-xr5pA3zyCEabE3hGirNK93xdnqixe5AM2ngv0SWMOF-dTKkfHu_8W0pq8bbJyNSnvNheov_WiBLQD4TBepom3E_V6FcecMH5B9ow3woxfVCKTTubaghBHLSPof6ezvQMkFhS7RdvaJpcDE6lBOmEfWkpgibfcLIZleBcpOqRd1yN9wHqtc4pS4T-QaJtiDviIUlMEa21keXqn1BnyiAzeIIsKddoLPSNslsRS__cmGECDxu1Pq5W8dPv4_3aWC92k_sPh2sQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دونالد ترامپ، رئیس‌جمهور آمریکا، در پاسخ به پرسش شبکه «نیوزنیشن» درباره اظهارات اخیرش مبنی بر اینکه احتمال «نابودی» ایران را بررسی می‌کرده است، گفت: «باید دید چه پیش می‌آید.»
ترامپ اظهار داشت که ایران در حال حاضر خواهان توافق است و افزود: «اگر توافق، توافق درستی نباشد، حتی به آن فکر هم نمی‌کنم. اما در حال حاضر، آن‌ها می‌خواهند توافق کنند، چرا که در همه زمینه‌ها در حال باختن هستند.»
@News_Hut</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/news_hut/71842" target="_blank">📅 20:25 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71841">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">ترامپ به «نیوزنیشن»: آمریکا با حوثی‌ها در حال گفتگو است.
حوثی‌ها نیز مایل به دستیابی به توافق هستند.
@News_Hut</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/news_hut/71841" target="_blank">📅 20:16 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71839">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/429ba373cd.mp4?token=WcyEq6vMoCItyufT55TP0eKHNjaOliAkhiJUQ5gAIUEMu1b67OoEl1b9yNyl3QMzwFKmOf6gtqGkWwPcgfX0CtI5ujDN3ipUH8lQcOrl6PF3r1BdLEkbFGUA3MJTgKdyajyiW3kak--cYZHyUzEmdTQIOnJVt4WCh3I1bbh_mqxl2QtvIfvJHMGrYQzWbAcbTvKGr5MldkYNih9mibaaNDaif7toVtvSyWz6FVd2c536vZza0vw2EY6_Ymz2DQB4wwoYPWd4_Kib6nJHqbKVs9YI_Nka5haMhzSizeee8tqpjYDhFC1KalXV4wzK27mgKq1eScMTSS2L41WzSCFA0w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/429ba373cd.mp4?token=WcyEq6vMoCItyufT55TP0eKHNjaOliAkhiJUQ5gAIUEMu1b67OoEl1b9yNyl3QMzwFKmOf6gtqGkWwPcgfX0CtI5ujDN3ipUH8lQcOrl6PF3r1BdLEkbFGUA3MJTgKdyajyiW3kak--cYZHyUzEmdTQIOnJVt4WCh3I1bbh_mqxl2QtvIfvJHMGrYQzWbAcbTvKGr5MldkYNih9mibaaNDaif7toVtvSyWz6FVd2c536vZza0vw2EY6_Ymz2DQB4wwoYPWd4_Kib6nJHqbKVs9YI_Nka5haMhzSizeee8tqpjYDhFC1KalXV4wzK27mgKq1eScMTSS2L41WzSCFA0w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یاشار سلطانی روزنامه‌نگار و فعال رسانه‌ای:
ما انگلیسی‌ها رو از ایران خارج کردیم ولی الان کشور افتاده دست چندتا بچه اطلاعاتی!
تشکیل مافیای فروش نفت هم از دوره روحانی و توسط زنگنه (شیخ الوزرا و وزیر نفت سابق) شروع شد.
درحال حاضر چهارنفر دارن نفت ایران رو میفروشن [حسین شمخانی، روح‌الله رضوی (دامادِ سخنگوی جریان پایداری)، علی بایندریان و محمد‌هادی مومنین].
پسر شمخانی(حسین) تو این چند سال، بالای 30 میلیارد دلار یعنی چندین برابر ثروت ترامپ فقط نفت فروخته!!
این چهارتا فقط تو فروش اخیر نفت ایران، 1.5 میلیارد دلار پول به جیب زدن!
@News_Hut</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/71839" target="_blank">📅 19:30 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71838">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C79Xm2cRyEvTsKHtUTVbGB6k-5cS2aqxiAaAbCUh1Ckojw55ers68mQMaPN1x4kaFJ_Xbw-Vo6YqH36CDEHkC_jCvkp8bWpLeGNcJj3R_-58cQ5Ub1lx_hLyVv2WHiqPy9_P9lcdRr2HnXGc8w9HV4eXP-lNYCQ3nx8_yBY6tHs4r3Bcl0wClIElCC3kvfXiag_5-MrA6qX8hTZ8VgHQP_KzwQ5uKhMH3rFS5QeaUZHUUY-x7UffSdv64UenHjLfzlGR1H51QBIZrGckNY-ptDmN9dJlvU8ju7qF4Hm4yLQ2oxbqP9dn7JlcU30XlYGJd6nSJANKxoPvec0_zNJ98g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حساب تلگرام در پلتفرم ایکس این تصویرو از ایلان‌ماسک منتشر کرده و نوشته:
ثروت کاذب:
🛩️
💰
🏎️
ثروت واقعی:ممه‌های ۸۵ ایلان ماسک
😂
@News_Hut</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/news_hut/71838" target="_blank">📅 18:56 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71837">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/915a75db7b.mp4?token=p2DtrAVnE7RFR3y5NT-0FPyU3oNer6hKQtLAwngOrFodbume4ICfXsa7FuMYG3kgk8HMRk4ppOU8XWjaKS7-pASG_SlSKmjZYoFXRW-4n4RweohBT2XGfXjRpnctijVnfC5nuPdEcFnnzB6at5pz4SFzXi_BZFPrXjsdt5AuLJo5rTA--IDzT_XQjuOvdmFzkV1UcCxJTI_rKkduhmGUFx9iB0LGyOWd80GGJscJj_zgG0qzYJmfu5JTxWB4EEl4rd015xPJ8MKGI6k1__4HWTueb-zv-9NGA9cvapV_u9nRigCU2UjHApmLNQlrLhDCXAk9lxtJ6COm78-YyRsDKg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/915a75db7b.mp4?token=p2DtrAVnE7RFR3y5NT-0FPyU3oNer6hKQtLAwngOrFodbume4ICfXsa7FuMYG3kgk8HMRk4ppOU8XWjaKS7-pASG_SlSKmjZYoFXRW-4n4RweohBT2XGfXjRpnctijVnfC5nuPdEcFnnzB6at5pz4SFzXi_BZFPrXjsdt5AuLJo5rTA--IDzT_XQjuOvdmFzkV1UcCxJTI_rKkduhmGUFx9iB0LGyOWd80GGJscJj_zgG0qzYJmfu5JTxWB4EEl4rd015xPJ8MKGI6k1__4HWTueb-zv-9NGA9cvapV_u9nRigCU2UjHApmLNQlrLhDCXAk9lxtJ6COm78-YyRsDKg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مجلس نمایندگان آمریکا «قانون لیندزی او. گراهام برای تحریم روسیه و ایران (مصوب ۲۰۲۶)» را با ۲۶۲ رأی موافق در برابر ۱۵۹ رأی مخالف تصویب کرد و این مصوبه را برای امضا نزد رئیس‌جمهور ترامپ فرستاد.
این لایحه «ناوگان سایه» روسیه را هدف تحریم قرار می‌دهد، اعمال تعرفه‌هایی تا سقف ۱۰۰ درصد بر پنج خریدار بزرگ محصولات انرژی روسیه را مجاز می‌سازد و «قانون تحریم‌های ایران (مصوب ۱۹۹۶)» را تمدید می‌کند؛ این موارد در کنار سایر اقداماتی است که روسیه و ایران را هدف قرار داده‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/news_hut/71837" target="_blank">📅 18:33 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71836">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/71836" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/news_hut/71836" target="_blank">📅 18:33 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71835">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EqwwSrDFsdwCN9X2ggC605G0c8JJkrIlrhuV37jRw_R9nI4AQEdpvAHHqSFsgUhuUKCv-vDli2yO17K2k9xudP34oE9K9kF-31mG3uVpV1xkTaKWJc1ZezqTPN-GceggSX53Z_ZAkIAZjN2wu53CcL34hvy4k4-pvqoEecfJC_3NxctOkrWD0SEhxHeYvpKajJaRDg1eAWmeupVyrO9aETj_4XYPiY47OmxnbJXEpW9bacODu3yqCXqh5GuJUwqpic_hoKjpWbZ8D7BcqlZ2gPZdrKCB2QciUqScl8D8A5BdSB_r_cYgfV7uC945LMePLkw3K4n7fHv94zFAtsJ0VA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/news_hut/71835" target="_blank">📅 18:33 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71834">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b71f8c82b6.mp4?token=rWMPMkV-URE3QrTq1VxwmrkccTVJ7Ef__HlikSdtzNKOVYo82iFN3eAKLA_FXHj7jgBa98l2C9oukAFmpqFh0D4SnmVsi1bbgJ3MHArT4AhoWGmScKipyBvG70AyGXQJA8v_cOhhqWWBJKkL6bBLha62YvpfCK5orR6ealonahLDhPawYmH2Ze_oRfIh9AN1Y6JpHcrYkCStYnjly_zUPab00f0ZLXLKvgXazJhDmBIM1H22i2DASsbK_AkHvHwX7Sx7fJtmLBc9fU4NZ5X71nxEF7HQEaSFmh3Ac9SfaYvpgDbUDbyVaAni8dJRwKuO7-o4qsL8dPkcc8HfSRg4Lw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b71f8c82b6.mp4?token=rWMPMkV-URE3QrTq1VxwmrkccTVJ7Ef__HlikSdtzNKOVYo82iFN3eAKLA_FXHj7jgBa98l2C9oukAFmpqFh0D4SnmVsi1bbgJ3MHArT4AhoWGmScKipyBvG70AyGXQJA8v_cOhhqWWBJKkL6bBLha62YvpfCK5orR6ealonahLDhPawYmH2Ze_oRfIh9AN1Y6JpHcrYkCStYnjly_zUPab00f0ZLXLKvgXazJhDmBIM1H22i2DASsbK_AkHvHwX7Sx7fJtmLBc9fU4NZ5X71nxEF7HQEaSFmh3Ac9SfaYvpgDbUDbyVaAni8dJRwKuO7-o4qsL8dPkcc8HfSRg4Lw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرنگار:
این جانفدا‌ها چجوری میتونن به دولت کمک کنن؟
پزشکیان:
ما باید کاری بکنیم که چرخ کارخونه‌ها بچرخه. برای این کار باید مصرف گازمون رو کنترل کنیم، بنزین رو کنترل کنیم. با همون حمل و نقل عمومی بیاییم بالا تا بتونیم دشمن رو ناامید کنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/news_hut/71834" target="_blank">📅 18:23 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71830">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fefe1a2487.mp4?token=QFWiqBYGz02En5oYDO1lPO2u4PIYLUjLhaD4o7d6QThctRaRH1WwjyHtnJb51kbAfgIMtbxvpG7QK-wnm9ZsQneQCMPHf1yuB2FT6hDhTnY8tGW-qjltNrZXhwGDFu0uDMoa1k_O3AQpV8S3PqSRiZQDPT_EQjzcg8YFtWsNT3IPLhf_RcK-ha8YylR-OJAeB2tJae1vXinrER542O_Y17eBdDFfFHEDcOXyJ99Q1823n-mvZwV-FT4wCcRIuHhcormC6NEZ3pPtfGlsrCJaQevagzd3zz7hHNgevdNKty1nvyiESjRwuT0UphCcncr17ydRRnHHJHHbUyPduXyqIg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fefe1a2487.mp4?token=QFWiqBYGz02En5oYDO1lPO2u4PIYLUjLhaD4o7d6QThctRaRH1WwjyHtnJb51kbAfgIMtbxvpG7QK-wnm9ZsQneQCMPHf1yuB2FT6hDhTnY8tGW-qjltNrZXhwGDFu0uDMoa1k_O3AQpV8S3PqSRiZQDPT_EQjzcg8YFtWsNT3IPLhf_RcK-ha8YylR-OJAeB2tJae1vXinrER542O_Y17eBdDFfFHEDcOXyJ99Q1823n-mvZwV-FT4wCcRIuHhcormC6NEZ3pPtfGlsrCJaQevagzd3zz7hHNgevdNKty1nvyiESjRwuT0UphCcncr17ydRRnHHJHHbUyPduXyqIg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مسجدی در شهر کوهات، واقع در ایالت خیبر پختونخوا پاکستان، هدف حمله یک بمب‌گذار انتحاری قرار گرفت که در پی آن بیش از ۱۰ نفر کشته و بیش از ۹ تن دیگر زخمی شدند.
@News_Hut</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/news_hut/71830" target="_blank">📅 17:36 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71829">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">دقایقی قبل صدای دو انفجار از سمت تنگه‌هرمز شنیده شد.
@News_Hut</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/news_hut/71829" target="_blank">📅 17:33 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71827">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">ارتش اسرائیل روز پنج‌شنبه اعلام کرد که نیروی دریایی اسرائیل و یونان دو هفته پیش یک رزمایش دریایی مشترک در دریای مدیترانه برگزار کردند.
این رزمایش با مشارکت دو ناو موشک‌انداز اسرائیلی و دو ناوچه یونانی انجام شد و بر تقویت هماهنگی عملیاتی میان نیروهای دریایی دو کشور تمرکز داشت.
شناورهای حاضر در این رزمایش، سناریوهای متعددی از جمله اجرای پروتکل‌های اضطراری و همچنین شناسایی و مقابله با تهدیدات دریایی را تمرین کردند.
@News_Hut</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/news_hut/71827" target="_blank">📅 17:01 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71826">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/00efcbd138.mp4?token=TeF0_lG-ScmHEs71y0lFaplCcc-VoSEPlS-t-OKZ-tEQlKYFeDk60-kjjaH1ozJKOarZgKOyEWzXv8ZjxBcW6lbbSI-3PV6qWS6Q5vVZbRcIdGwDFXTeEEOAjp6Z2tQAYqQb87Sayi-u01ILqZspqyW-f9emW4DkIJuftLXpQ8y5Xnwhs8SuhrDwWMRD9Kewh4s4zGIqt27HDl9t0HbudWqObV4cuEtvzBTRC95XiHH18xLdDaIlzFK6n_B9w2gLbNG0tRf6pSHMthK4PX2Ktdhhr8CIU-e7IhcV7texl51j_u1UjF4vzIeNuvZyr2xC-gdRw9Vg_2vuIxGVJV8HTw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/00efcbd138.mp4?token=TeF0_lG-ScmHEs71y0lFaplCcc-VoSEPlS-t-OKZ-tEQlKYFeDk60-kjjaH1ozJKOarZgKOyEWzXv8ZjxBcW6lbbSI-3PV6qWS6Q5vVZbRcIdGwDFXTeEEOAjp6Z2tQAYqQb87Sayi-u01ILqZspqyW-f9emW4DkIJuftLXpQ8y5Xnwhs8SuhrDwWMRD9Kewh4s4zGIqt27HDl9t0HbudWqObV4cuEtvzBTRC95XiHH18xLdDaIlzFK6n_B9w2gLbNG0tRf6pSHMthK4PX2Ktdhhr8CIU-e7IhcV7texl51j_u1UjF4vzIeNuvZyr2xC-gdRw9Vg_2vuIxGVJV8HTw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چند‌روز قبل حدود هزاران تریان که عمدتا سگ، گرگ، گربه، شغال و روباه بودن روبه روی پارلمان آلمان در شهر برلین تجمع کردن و خواستار به رسمیت شناختن حقوق جامعه تریان ها به عنوان شهروند عادی شدند
به آدم هایی که رفتارشون مثل گرگ، گربه، سگ و ... هست تریان می‌گن.
@News_Hut</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/news_hut/71826" target="_blank">📅 16:33 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71825">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2db0ed7cac.mp4?token=RJ2rZ_ytxb4DGzjairw484aHJ1o1j-7c0lTCtpF3YsWyCzMMhYSD0w0lLMwY0jNIgeeeuS-tI3KwN41dHCiM8iwiYN2MJ8Bb5uR-7ikztIOaMrjFn8AZjauJgs976z20lsaBB1-fWZF7gWrALp9YGkgK7AnnlrMl5BF-_lH6BXVuIX9IZB_5SpLUFGGBTniHV-lcOpv4dWf1yrxAUVqknOFmSakShk9SCIyNEsegKVtqjVW3X1DtjTbxHx4d9Qp5pHR5_CexKSMySDpmLsRJrrinb3cSLDSOH8o9Nn8_OWGJ0RC9C7Zkk6zjH2vdplJkJNH_pUmMSHp_hQxINsRBhDjds5uu4MIWpp3Z2aOEVeprLKYplthNmN3YBdGqnnpYORv7gK6ReCjbOpkKjnaQ95ZeO7OTGme7qMF050SEvp1HvQbU5r90SIn7WpInYOanR5HxxtIt9vaIXQdypCPi6_s1Myp_qm-aNk-Jyq288tTrJl_rX0WQAP_jZyynb7e46UwYlasOvGnjLDrPoruIQAkwIy-oDuJTdPQPC_2_K6QNF9g-zxGINoKPf3rMiGBjQ16T54gexj5P45l08h4KbdtgiKBFh8X-FwqHs3ONrvw-hAlJtNj5iHMx-jEqn9BvYrZqlN8bmGPKgr4H6b4Ge93nDrhhFuVxTf_wxKh_5T8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2db0ed7cac.mp4?token=RJ2rZ_ytxb4DGzjairw484aHJ1o1j-7c0lTCtpF3YsWyCzMMhYSD0w0lLMwY0jNIgeeeuS-tI3KwN41dHCiM8iwiYN2MJ8Bb5uR-7ikztIOaMrjFn8AZjauJgs976z20lsaBB1-fWZF7gWrALp9YGkgK7AnnlrMl5BF-_lH6BXVuIX9IZB_5SpLUFGGBTniHV-lcOpv4dWf1yrxAUVqknOFmSakShk9SCIyNEsegKVtqjVW3X1DtjTbxHx4d9Qp5pHR5_CexKSMySDpmLsRJrrinb3cSLDSOH8o9Nn8_OWGJ0RC9C7Zkk6zjH2vdplJkJNH_pUmMSHp_hQxINsRBhDjds5uu4MIWpp3Z2aOEVeprLKYplthNmN3YBdGqnnpYORv7gK6ReCjbOpkKjnaQ95ZeO7OTGme7qMF050SEvp1HvQbU5r90SIn7WpInYOanR5HxxtIt9vaIXQdypCPi6_s1Myp_qm-aNk-Jyq288tTrJl_rX0WQAP_jZyynb7e46UwYlasOvGnjLDrPoruIQAkwIy-oDuJTdPQPC_2_K6QNF9g-zxGINoKPf3rMiGBjQ16T54gexj5P45l08h4KbdtgiKBFh8X-FwqHs3ONrvw-hAlJtNj5iHMx-jEqn9BvYrZqlN8bmGPKgr4H6b4Ge93nDrhhFuVxTf_wxKh_5T8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">امانوئل مکرون، رئیس‌جمهور فرانسه:
تنگه هرمز عملاً مسدود باقی مانده و هیچ توافقی برای بازگشایی آن وجود ندارد.
در واقع، وضعیت تردد نسبت به چند هفته پیش بدتر شده است.
@News_Hut</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/news_hut/71825" target="_blank">📅 15:58 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71824">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7fb0b52718.mp4?token=eN6WN8LfoJx6iW3OsA7hdPj6kJf-NeSGHvdPXNd2l3r-6yfume6m8nZ_Iu6qp7B1PqFZHn5zlqPqmR1VAMu8oy5iAo-dX2K_l41vdjdFm2rrVRkSJP1Mn18Y7vAFd0qQjMHyeHnF_lyDEgb0TZP109vOVFnIz0jDlzvFwYUVBv7knBy0mUTQDLekjMWiZIrhkAVaymUCMk789n1-YHx4Z93FCen4-mSyEt14H7o2zHQou9oOU4qMdBBaR1ew6VofhPAYvNfjISyjLX3hM_GbIk-2CCg0O4mGj5dbrpUjIQ8M381RSi5Aw_luxPjoZ-yig3E3HTxkdpsHPS-uivmRog" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7fb0b52718.mp4?token=eN6WN8LfoJx6iW3OsA7hdPj6kJf-NeSGHvdPXNd2l3r-6yfume6m8nZ_Iu6qp7B1PqFZHn5zlqPqmR1VAMu8oy5iAo-dX2K_l41vdjdFm2rrVRkSJP1Mn18Y7vAFd0qQjMHyeHnF_lyDEgb0TZP109vOVFnIz0jDlzvFwYUVBv7knBy0mUTQDLekjMWiZIrhkAVaymUCMk789n1-YHx4Z93FCen4-mSyEt14H7o2zHQou9oOU4qMdBBaR1ew6VofhPAYvNfjISyjLX3hM_GbIk-2CCg0O4mGj5dbrpUjIQ8M381RSi5Aw_luxPjoZ-yig3E3HTxkdpsHPS-uivmRog" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سباستین گورکا، مسئول ارشد مبارزه با تروریسم در کاخ سفید:
قیمت بنزین برایم اهمیتی ندارد، چرا که وقتی پیروز شویم — که به‌زودی هم خواهد بود — قیمت بنزین ارزان خواهد شد.
مسئله، انتخابات میان‌دوره‌ای نیست؛ مسئله، نابود کردن کسانی است که قصد کشتن آمریکایی‌ها را دارند.
اگر فکر می‌کنید این موضوع اهمیت کمتری نسبت به قیمت بنزین دارد، شما آمریکایی نیستید. تمام.
@News_Hut</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/news_hut/71824" target="_blank">📅 15:23 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71823">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9b2eeaeb9e.mp4?token=sr4hQx4QthXxUGCAX3YfYLhnE9Qnts69efkzPRSDOoDTX4YaN8tmcbk6LayUikXj3yhakvgzx8655WUZ5D5FqJEduj6upbEOM3Hbn0q_IXgFMjSDSRC4XwSAq3Cv-RnQEVB7EG70Z9haVmvPiohRWjoqKAmgFmM_jj1Ek8XSfecxfXleZp4DZFULLfvKJwIKIlFJ1CjTf64UVgu0SmqeH1S6AU-JCsaR4g024wgsb47yfKl5b2QfbwSZfQV-g3Xx1TYTO8FV88gSi2CyIhKj3c59mhx6JO2aE2OsST7nR8wdM1QoTL4d_kjRI5wwz4z0xM7ubpHlPjtoIaNPmFlwBQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9b2eeaeb9e.mp4?token=sr4hQx4QthXxUGCAX3YfYLhnE9Qnts69efkzPRSDOoDTX4YaN8tmcbk6LayUikXj3yhakvgzx8655WUZ5D5FqJEduj6upbEOM3Hbn0q_IXgFMjSDSRC4XwSAq3Cv-RnQEVB7EG70Z9haVmvPiohRWjoqKAmgFmM_jj1Ek8XSfecxfXleZp4DZFULLfvKJwIKIlFJ1CjTf64UVgu0SmqeH1S6AU-JCsaR4g024wgsb47yfKl5b2QfbwSZfQV-g3Xx1TYTO8FV88gSi2CyIhKj3c59mhx6JO2aE2OsST7nR8wdM1QoTL4d_kjRI5wwz4z0xM7ubpHlPjtoIaNPmFlwBQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سازمان نظام وظیفه:
از مشمولان غایب تقاضا داریم بیان خدمت ، هر ارگانی خودشون دوست داشته باشن پذیرششون ‌میکنیم!
@News_Hut</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/news_hut/71823" target="_blank">📅 15:04 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71822">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bc25aa2680.mp4?token=L23Q73C5CWquvYVcPh-vbGj_gJftCUwrrfMrF3-pGxw-yFDsHJW6N-v2wdBXH3V6hK8hR5G89SeWAB5Ja5i4m5_Op-_1uQ8y0iOXortx42cDEsiGR79mmReCMrdFcrjbVsGMpJCaMlpZB4EaECyVJuqkTcqGdhWjT-prJHT8PL4ZYaluT1VPzN8mUPJJxvBbpFB5nBGcxOADb1TRPTH6MQ0E-KjOfMQDZTTl6FbOLmdUMEHKKWPIPD0UHe3W7IFpEN6J0LYICNWvDfxH37lUBgCHjBoX6xki1mCtc0aTVXlWCu1hlvD72fkGhgkYiymxJ57ciOKY6N0Zu5PnvYz-qoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bc25aa2680.mp4?token=L23Q73C5CWquvYVcPh-vbGj_gJftCUwrrfMrF3-pGxw-yFDsHJW6N-v2wdBXH3V6hK8hR5G89SeWAB5Ja5i4m5_Op-_1uQ8y0iOXortx42cDEsiGR79mmReCMrdFcrjbVsGMpJCaMlpZB4EaECyVJuqkTcqGdhWjT-prJHT8PL4ZYaluT1VPzN8mUPJJxvBbpFB5nBGcxOADb1TRPTH6MQ0E-KjOfMQDZTTl6FbOLmdUMEHKKWPIPD0UHe3W7IFpEN6J0LYICNWvDfxH37lUBgCHjBoX6xki1mCtc0aTVXlWCu1hlvD72fkGhgkYiymxJ57ciOKY6N0Zu5PnvYz-qoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مدرسه لاکچری؛ شهریه سالی ۳۰۰ میلیون!
@News_Hut</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/news_hut/71822" target="_blank">📅 14:35 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71819">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/387a49d38d.mp4?token=Bc9f7Xy0_pMeipQb9voGpdD3LzY7WdO21QSxrqWvNlri8kgxrUprgscS3ncEzZCDEFjQHBCifj8POUVa4IQcWNRtKByvswU8lAkUYauogg29_YCZt_6LhCAGKgFhl7nGK6DzBsHFBKGRudYTqO2Uwkl8UF9RS6OhxhWOGWIGYk4WT9RlE_TDsQTpMAHDphFGBqZqn5llXu3z2TAGQ1Dtr_fItnYqeEZVBTDVu4pCq_sWV1GtJBEEXMHFZovbZfJHqaj7r5BW8uR9HGLzxinne5Tgz49enYD3t9dxO3e-Ewxg0drZdMZRpjAj53io3av_2CN8RtyQdh9shFkzHadF7g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/387a49d38d.mp4?token=Bc9f7Xy0_pMeipQb9voGpdD3LzY7WdO21QSxrqWvNlri8kgxrUprgscS3ncEzZCDEFjQHBCifj8POUVa4IQcWNRtKByvswU8lAkUYauogg29_YCZt_6LhCAGKgFhl7nGK6DzBsHFBKGRudYTqO2Uwkl8UF9RS6OhxhWOGWIGYk4WT9RlE_TDsQTpMAHDphFGBqZqn5llXu3z2TAGQ1Dtr_fItnYqeEZVBTDVu4pCq_sWV1GtJBEEXMHFZovbZfJHqaj7r5BW8uR9HGLzxinne5Tgz49enYD3t9dxO3e-Ewxg0drZdMZRpjAj53io3av_2CN8RtyQdh9shFkzHadF7g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یاشار سلطانی روزنامه‌نگار و فعال رسانه‌ای فروشندگان نفت را لو داد!
از داماد سخنگوی پایداری‌ها تا خانواده شمخانی
@News_Hut</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/news_hut/71819" target="_blank">📅 14:05 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71817">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7d2b23b11f.mp4?token=AuRonrt4mUlZIK1Uw65u_XlBFVgkTZdIvIlqFBdLwvUqHXOgX1r6mVVSxB1NqgY61My2jG072z1_LACto7uTIiWYYu0I3z3AyzVDNajJ3bzT5zWuW8MLvkDhM9QdG7ZAlOcjBP79_Fv7Ej09hyiP2YhYWz81LQyKsyEhQ0jvnJMzJ59NNUACsYUKsCWRBJIAvesL4-pc_u5Tk62I9Vmx9584u1tOfRXXM5W_KAWAHnVOXRvMHY4sxP3qWNLtk6Wi2EdT3YEQ1Qod-BioF5u6yVwzZzm3bd0LfWnpAhrEjdOGgwRfAycTL9dzI-gHnNwEFhbRTVrcA8IpA5zF2opbcA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7d2b23b11f.mp4?token=AuRonrt4mUlZIK1Uw65u_XlBFVgkTZdIvIlqFBdLwvUqHXOgX1r6mVVSxB1NqgY61My2jG072z1_LACto7uTIiWYYu0I3z3AyzVDNajJ3bzT5zWuW8MLvkDhM9QdG7ZAlOcjBP79_Fv7Ej09hyiP2YhYWz81LQyKsyEhQ0jvnJMzJ59NNUACsYUKsCWRBJIAvesL4-pc_u5Tk62I9Vmx9584u1tOfRXXM5W_KAWAHnVOXRvMHY4sxP3qWNLtk6Wi2EdT3YEQ1Qod-BioF5u6yVwzZzm3bd0LfWnpAhrEjdOGgwRfAycTL9dzI-gHnNwEFhbRTVrcA8IpA5zF2opbcA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرگزاری مهر:
هزاران نفر در رژه «جانفدا» در تهران شرکت کردند و از میدان امام حسین تا میدان انقلاب راهپیمایی کردند.
@News_Hut</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/news_hut/71817" target="_blank">📅 13:12 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71816">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c319028d9f.mp4?token=iOy2El2nNDoDeoocRgVNXhCa1mKZuG9ljb86T_JITe3TXkjZf9yBi7hXta8bESqx-ES8OPftc6H44CNMKBLndVqicftCisyo8Jw1E1ukK9dIWXxJ7_5g9SyxIhHf5B-V98RIFh_WIYvzXCdyKjBHUhKVbjaq21EV58TQ_ow9-rT-0_rYebB0-pACiTCKeqGLE_NB21mBP00DRG7qijFYUv-bheEp6_qiALHWir0NBi1axMBHskaJNAuFpsrcfFKWJR95MqT-2TT6FaNGvmMdn8ZoaT9f5NprAj634FsE5ObmDzCrM2p_-tY_o9APFoyCAbRIlOShC5I7tST8adkDgQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c319028d9f.mp4?token=iOy2El2nNDoDeoocRgVNXhCa1mKZuG9ljb86T_JITe3TXkjZf9yBi7hXta8bESqx-ES8OPftc6H44CNMKBLndVqicftCisyo8Jw1E1ukK9dIWXxJ7_5g9SyxIhHf5B-V98RIFh_WIYvzXCdyKjBHUhKVbjaq21EV58TQ_ow9-rT-0_rYebB0-pACiTCKeqGLE_NB21mBP00DRG7qijFYUv-bheEp6_qiALHWir0NBi1axMBHskaJNAuFpsrcfFKWJR95MqT-2TT6FaNGvmMdn8ZoaT9f5NprAj634FsE5ObmDzCrM2p_-tY_o9APFoyCAbRIlOShC5I7tST8adkDgQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عادی ترین شوخی پسرا
@News_Hut</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/news_hut/71816" target="_blank">📅 12:41 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71813">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">«تصمیم بزرگی در پیش دارم. آیا می‌خواهم وارد عمل شوم و آن‌ها [رژیم ایران] را نابود کنم یا نه؟ تصمیم بزرگی است. هر احتمالی از جانب من وجود دارد.»</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/news_hut/71813" target="_blank">📅 12:05 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71812">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">سازمان عملیات دریایی انگلیس: امروز یک شناور دیگر در آب‌های تنگه هرمز، مورد اصابت یک پرتابه نامشخص قرار گرفته و در آتش می‌سوزد.
@News_Hut</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/news_hut/71812" target="_blank">📅 11:09 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71811">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a6831b24b0.mp4?token=Z4XSNj9o6gnlsmlYkP0CX4xJ06SauiTKUZE-USfbVA9kBVJZW8s4PFr4Abdz_FWb89MiEI4OoMQwX6BNf3kyQhfIW5yVlOZ9b1M_ftzfcmeSNP7oSqYjk0DMFOKcX1aMAHpwGlbrMgJiGMFn8Yvbf6KFiNXmrGo6AMkBItvKPGW003gbjUXObXzql5vj7FTSXQNey94BxiTp8RoJHQfKbof77_IKmZZLGM6Icw34BhRGhYNSPt4-VjH7cA21fvWxaHsK6unBdvHPYAXB_hoR2w11PyJYb6qm2vXxQGJO02Fgr0_Eg3ji-PM2_AY4lEKs9dsEQwHxI4Xp9S7xYfPaCQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a6831b24b0.mp4?token=Z4XSNj9o6gnlsmlYkP0CX4xJ06SauiTKUZE-USfbVA9kBVJZW8s4PFr4Abdz_FWb89MiEI4OoMQwX6BNf3kyQhfIW5yVlOZ9b1M_ftzfcmeSNP7oSqYjk0DMFOKcX1aMAHpwGlbrMgJiGMFn8Yvbf6KFiNXmrGo6AMkBItvKPGW003gbjUXObXzql5vj7FTSXQNey94BxiTp8RoJHQfKbof77_IKmZZLGM6Icw34BhRGhYNSPt4-VjH7cA21fvWxaHsK6unBdvHPYAXB_hoR2w11PyJYb6qm2vXxQGJO02Fgr0_Eg3ji-PM2_AY4lEKs9dsEQwHxI4Xp9S7xYfPaCQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قائم‌پناه، معاون پزشکیان:
حساب کردم اگر بنزین ۸۰ هزار تومان شود و برق و گاز و ... را هم گران کنیم، می‌شود ۷میلیون یارانه در ماه به هر نفر داد‌.
@News_Hut</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/news_hut/71811" target="_blank">📅 11:00 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71810">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dGUBu74FbcSngzepdZ9nkcqZwH6nZTROoSI0duke_Koz-nrIaOcJo1-xW535nF75FU--vzQ3tDur0q_DgBUljWs_iFq6r8u2YzmjhaKl7JA4IGKBRPdfO9RJEnpyvAtJX5qNDhxHOZlviPw-zNM-S2bfYUh9-pboTuaT3TvDcZj4H8BSjVVg1j2vqFSja9bV6-4VUV85jXPMVlWmOr_U9jModNvMJ3Z5G2uKF1Jr8Y1VKwKwdF31gWKHbKxgPcCKknncTW3SV7GjA-7AABWHb79TK7jfcKYuFAmQdxgdtTmawO4KeCfd4KXDqnxZ9kiLfhEVwnLsfATQxcmgH-njDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
🇸🇦
🇨🇳
—مقام‌های اطلاعاتی آمریکا ابراز نگرانی کرده‌اند که در صورت نهایی شدن فروش برنامه‌ریزی‌شده ۲۴ میلیارد دلاری ۴۸ فروند جنگنده F-35 و یک موتور یدکی به عربستان سعودی از سوی دولت ترامپ، چین ممکن است به فناوری‌های حساس این جنگنده دسترسی پیدا کند.
بر اساس گزارش نیویورک تایمز، یک ارزیابی اخیر از سوی آژانس اطلاعات دفاعی آمریکا (DIA) بر دسترسی چین به تأسیسات نظامی عربستان، روابط دفاعی پکن و ریاض و همچنین استفاده گسترده از فناوری‌های مخابراتی چینی در عربستان تأکید کرده است.
تحلیلگران این پرسش را مطرح کرده‌اند که آیا آمریکا و عربستان می‌توانند تأسیسات مرتبط با F-35 را به اندازه کافی ایمن کنند و مانع دسترسی نیروهای نظامی یا اطلاعاتی چین به فناوری‌های حساس شوند؛ به‌ویژه رادار پیشرفته و سامانه‌های شناسایی و نظارتی این جنگنده.
نگرانی‌های مشابهی پیش‌تر درباره فروش احتمالی F-35 به امارات متحده عربی نیز مطرح شده بود؛ به‌خصوص پس از گسترش روابط نظامی، اطلاعاتی و فناوری ابوظبی با چین. آن قرارداد در نهایت به مرحله اجرا نرسید.
@News_Hut</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/news_hut/71810" target="_blank">📅 10:34 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71806">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/44d9bc13c5.mp4?token=fmmvaE_om8syv1FVoAPmwkLYjsd55gRD9JyOmVHobzK5XVGhWEt0kWocil4puNMAXeD9pzoJnSRia03o0QHutPPHH2mwmbGRRztB-ht13-A5tOAg68wZO2hAbYbALvoO0PwdrMZNHBvMlZLukQItvY61kbyaGNy5yn97QmU8H1wE2GAAxkxbDxSfW8V-rf6EemtTnnQfFPBgIzqFkSfVEDPJBfuWHkXR_3htWk7cJVkNlWwabxxLUfmIHNmlwzhUvV40E48ZyNc0vrPC5YCGjIZCOtn3XEo25BZTe2FAi9IrjUoiVVPkQjkDRixGRUR7crFjiyzvjADjiIYapQNdUg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/44d9bc13c5.mp4?token=fmmvaE_om8syv1FVoAPmwkLYjsd55gRD9JyOmVHobzK5XVGhWEt0kWocil4puNMAXeD9pzoJnSRia03o0QHutPPHH2mwmbGRRztB-ht13-A5tOAg68wZO2hAbYbALvoO0PwdrMZNHBvMlZLukQItvY61kbyaGNy5yn97QmU8H1wE2GAAxkxbDxSfW8V-rf6EemtTnnQfFPBgIzqFkSfVEDPJBfuWHkXR_3htWk7cJVkNlWwabxxLUfmIHNmlwzhUvV40E48ZyNc0vrPC5YCGjIZCOtn3XEo25BZTe2FAi9IrjUoiVVPkQjkDRixGRUR7crFjiyzvjADjiIYapQNdUg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پول که باشه، اسنوپ داگ هم واست قِر میده؛
دیروز تو‌ مراسم ازدواج یه زوج ایرانی تو لس‌آنجلس، اسنوپ داگ هم به عنوان مهمان ویژه حضور داشت که هم خوند و هم رقصید!
@News_Hut</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/news_hut/71806" target="_blank">📅 10:03 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71805">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/102dbc4ee1.mp4?token=lI4vBHdJqnu-aFBICYSHW99dBNuZjwNDKt396s4nt-PUzc8eBsM5k3K2lPmXzS-bJo_ZPm742chktU_RILANs8ydCpuoBn7bxC4RTfl9xdaJAo8mYcJgyTt_LaI6a-YeSMAEMeaMj0IPjh4_mk2vAmeknoCRBJ9B4KOsjYeqcEBAjElyJTrx7MOQCzOvOrsAzZXO5MKNEGAoMlA5bdL-KhJyM8uI9SSDg4pAQnH87F8wkiD0Qsb190wLEnkiXPYwdutrsPBbCffMOv5K0plz9nhnkpvFQPRhHOpr8QJydqnwElAVSyShU4M69z0C1CucAqOE6Ws-ZMavNxl94Lu3DRwt6i-TUxnJNpA000azxPGDk7_Ojm74E_PxMpoum7W86wJA8iqHjYyhkKPbkywJamdQ1b_VNDmbmJdIrQNvqoHF_UFaIl5ifDAhplz0XRtU-WGiJ7Ajvyo-o_SHYGQMzpCG9WooX9erAmPu7zzfd1Ui6fiQgrhGo1A1_LMpZ4G8Zy7rlzqTcIdd_uet4XrtZHp4ecBk7NyPuJr5rSpznbF98ThAhw6PHJ6KI8j4tmp2U_XrKo8_Wkld7MM-dJAglfkjGYrf5E9uke04G2RpqIDZ_YOX6GFwaHDG5oNkLY35DLEBSyK5ilzczBOYy8YVxgbFo1gLGAngPd4R2pIEf0A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/102dbc4ee1.mp4?token=lI4vBHdJqnu-aFBICYSHW99dBNuZjwNDKt396s4nt-PUzc8eBsM5k3K2lPmXzS-bJo_ZPm742chktU_RILANs8ydCpuoBn7bxC4RTfl9xdaJAo8mYcJgyTt_LaI6a-YeSMAEMeaMj0IPjh4_mk2vAmeknoCRBJ9B4KOsjYeqcEBAjElyJTrx7MOQCzOvOrsAzZXO5MKNEGAoMlA5bdL-KhJyM8uI9SSDg4pAQnH87F8wkiD0Qsb190wLEnkiXPYwdutrsPBbCffMOv5K0plz9nhnkpvFQPRhHOpr8QJydqnwElAVSyShU4M69z0C1CucAqOE6Ws-ZMavNxl94Lu3DRwt6i-TUxnJNpA000azxPGDk7_Ojm74E_PxMpoum7W86wJA8iqHjYyhkKPbkywJamdQ1b_VNDmbmJdIrQNvqoHF_UFaIl5ifDAhplz0XRtU-WGiJ7Ajvyo-o_SHYGQMzpCG9WooX9erAmPu7zzfd1Ui6fiQgrhGo1A1_LMpZ4G8Zy7rlzqTcIdd_uet4XrtZHp4ecBk7NyPuJr5rSpznbF98ThAhw6PHJ6KI8j4tmp2U_XrKo8_Wkld7MM-dJAglfkjGYrf5E9uke04G2RpqIDZ_YOX6GFwaHDG5oNkLY35DLEBSyK5ilzczBOYy8YVxgbFo1gLGAngPd4R2pIEf0A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بهترین خواننده جهان به ۱۶پرومکس راضی نشد رفت برا خودش و داداشش ۱۷ پرومکس خرید
حالا حرفای مغازه دار:
آقا محمد مرسی که افتخار دادی اومدی از ما خرید بکنی
واقعا شهر ما خوش شانسه که چنین هنرمندی داره
ایشالا آلبوم های جدیدت رو با این گوشی ضبط بکنی بدی بیرون
@News_Hut</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/news_hut/71805" target="_blank">📅 09:33 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71804">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mxQ4eZeLg2TFx8Rrkqg2IMWX5wAgboMG_auC9a7SzeBsRfPbg02w-jCAPOUp1ajnqhHveApKkmBwEufimFgbN6lBV-fUHOy757qNvUDhEFYpvxVCv6xjikZAeKTeDsq9W7nSlGyHn_dYMVu7fS4_jBj7zRZRQu7_6990BX8uB61XaLpWdDYDpn38Hd4I0DqtJ__YGev21MTdr7f4VmN3cwyGTrbuQ2u3aL5NEzsIZSw0mAIryuDeO7msnWd18oK7u4kC9ck-B7AHPbdBAhOGIgmoyBh5TnYkFEC4Mq307VCcSeS5VqppCDbyzWPJ41Nc0qvQghWsxP2zgfMtCkNsiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تامی پیگات، معاون سخنگوی وزارت امور خارجه آمریکا:
در حالی که مردم عادی ایران با سرکوب بی‌رحمانه، کمبود آب و برق و تورم سرسام‌آور دست‌وپنج نرم می‌کنند، مقامات رژیم می‌خواهند در نیویورک به خریدهای کلان و لوکس بپردازند. ما اجازه چنین کاری را نخواهیم داد.
ما اجازه نخواهیم داد که نخبگان رژیم ایران از فرصت مجمع عمومی سازمان ملل برای خریدهای لوکس و پرهزینه — که به بهای رنج مردم ایران تأمین می‌شود — سوءاستفاده کنند؛ آن هم در شرایطی که رژیم ثروت ایران را صرف حمایت از گروه‌های نیابتی تروریستی خود می‌کند.
ایالات متحده همچنان مقامات نمایندگی ایران در سازمان ملل، مقامات بازدیدکننده و وابستگان آن‌ها را از خرید عضویت در فروشگاه‌های عمده‌فروشی (مانند «کاستکو») یا کالاهای لوکس در اینجا منع خواهد کرد.
فروشندگان منطقه نیویورک: هوشیار باشید و در ارتکاب این تخلفات شریک نشوید.
@News_Hut</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/news_hut/71804" target="_blank">📅 09:00 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71803">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e0d036df0a.mp4?token=CA2QtT8t9UQ95Mj--9lw9vUvw5TfAzxXzlRaqHdpFWgalDt3-74hXNFiggMeac4jv-jaC7adVd2epB3297AfoMFQmchDEhOW0eVRnVc8egyPwcckTI-6zotfc39HmbW74f1iKiVQY2kPJmc4IqzodQeXbBSPbab4UImuNC7mRZh7wgTYw0ldzEUUH1ZqsqE6hijM7HXeATLhNR3X0eBg3BaI2JdEe5ykvN8zdcK4pqWlVhn-plJ34JTWaLTu9nhtyMd5LacH2wYnyZMYpCI6FzUPLqsnN3GKoR8G-36aRzBvr3zNMC0dD7bInYdrE2Xp8yV1PV9HCNjnHOeGqc1Xtw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e0d036df0a.mp4?token=CA2QtT8t9UQ95Mj--9lw9vUvw5TfAzxXzlRaqHdpFWgalDt3-74hXNFiggMeac4jv-jaC7adVd2epB3297AfoMFQmchDEhOW0eVRnVc8egyPwcckTI-6zotfc39HmbW74f1iKiVQY2kPJmc4IqzodQeXbBSPbab4UImuNC7mRZh7wgTYw0ldzEUUH1ZqsqE6hijM7HXeATLhNR3X0eBg3BaI2JdEe5ykvN8zdcK4pqWlVhn-plJ34JTWaLTu9nhtyMd5LacH2wYnyZMYpCI6FzUPLqsnN3GKoR8G-36aRzBvr3zNMC0dD7bInYdrE2Xp8yV1PV9HCNjnHOeGqc1Xtw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره ایران:
به گمانم آن‌ها در آستانه فروپاشی هستند. می‌دانید، وضعیت فعلی اقتصادشان بی‌سابقه است؛ بدترین وضعیتی که تا به حال داشته‌اند. تورمشان از ۳۰۰ درصد فراتر رفته است. حقوق سربازان، نیروهای نظامی و پلیسشان را نمی‌پردازند. اوضاعشان به‌هم‌ریخته و آشفته است. باید دید چه پیش می‌آید.
@News_Hut</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/news_hut/71803" target="_blank">📅 07:32 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71797">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4759c454c5.mp4?token=HAwCpoGA0T0R5b3HHR8CQ_jZ5llsuO05AIx4kbYby93Df6gXzVE0IDYsTj9Q_JhGMOfyMbtJX7_jszASoLpHtJCatyXoj9ExEcp3fhHXhlcZz-GqeaEKsMnz7QIiMCClLG0MgoA37qoriIVo6m9-dJBlnNiJxyy5qO-2bXiu2TEvTtdojirkMTkxXcetTyIMXWe5iOXv1jjsv-sqeJyXGY8BvbERyHym8rfiQ3eeF2oEKUtQDCHhBWN9fmmotITUUFYQF9g7olc3wtzlwt7XEb9Jpp41rkgY6h6zLHXk4ZUEyBRUtYZtDShBoOYjgCJ7x-a8NIKTFeYwbHMFHS9Edw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4759c454c5.mp4?token=HAwCpoGA0T0R5b3HHR8CQ_jZ5llsuO05AIx4kbYby93Df6gXzVE0IDYsTj9Q_JhGMOfyMbtJX7_jszASoLpHtJCatyXoj9ExEcp3fhHXhlcZz-GqeaEKsMnz7QIiMCClLG0MgoA37qoriIVo6m9-dJBlnNiJxyy5qO-2bXiu2TEvTtdojirkMTkxXcetTyIMXWe5iOXv1jjsv-sqeJyXGY8BvbERyHym8rfiQ3eeF2oEKUtQDCHhBWN9fmmotITUUFYQF9g7olc3wtzlwt7XEb9Jpp41rkgY6h6zLHXk4ZUEyBRUtYZtDShBoOYjgCJ7x-a8NIKTFeYwbHMFHS9Edw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یک اتوبوس غیرنظامی اوکراینی در زاپوریژیا هدف حمله پهپاد انتحاری (FPV) روسیه قرار گرفت که منجر به مجروح شدن ۳ سرنشین آن شد.
محل این حمله در مختصات 47.7794347, 35.2161182 واقع شده است.
این منطقه پیش‌تر نیز در اوایل ماه اوت (طی بمباران یک گل‌فروشی در آن خیابان) و همچنین در ۲۱ اوت (در جریان حمله به یک مینی‌بوس) هدف پهپادهای انتحاری روسیه قرار گرفته بود.
@News_Hut</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/71797" target="_blank">📅 00:34 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71796">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e097e163aa.mp4?token=pLcgJ6XJtQ5Zm8rpNQHBTQ6OgStsbk_Y-I1JN0G_ESIGr7naY-6jPQD5Mb2PLt-4JJNgzGfNR2-mipTnXsqNGBXpmeMLBup5qvuEFPJG03J9VCsxytjXMHzKXUJWb2M2jMSfJHwY92LQGVL8c0mZInKOiTF8Cj7pURdKRJuUuNitLjGDGEmzNz8C7kvCQDR8WrHumz6mOffarNDH4hQgayDczSE3qvQiT1sH3San7CHhKMiPz5UqtHoV9YfRTxE2cT38FW7ypYIGG4zpH-QJMmVgXCKZKjb_DgKktTxWRukityvTMKb1kelJLEKvkMZRsRdenQOn--iBfTWI-gGkZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e097e163aa.mp4?token=pLcgJ6XJtQ5Zm8rpNQHBTQ6OgStsbk_Y-I1JN0G_ESIGr7naY-6jPQD5Mb2PLt-4JJNgzGfNR2-mipTnXsqNGBXpmeMLBup5qvuEFPJG03J9VCsxytjXMHzKXUJWb2M2jMSfJHwY92LQGVL8c0mZInKOiTF8Cj7pURdKRJuUuNitLjGDGEmzNz8C7kvCQDR8WrHumz6mOffarNDH4hQgayDczSE3qvQiT1sH3San7CHhKMiPz5UqtHoV9YfRTxE2cT38FW7ypYIGG4zpH-QJMmVgXCKZKjb_DgKktTxWRukityvTMKb1kelJLEKvkMZRsRdenQOn--iBfTWI-gGkZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سردار حسن زاده فرمانده سپاه تهران:
فردا ساعت 4 صبح رده های سپاه،
یگان های بسیج و گردان های جانفدا از میدان انقلاب تا میدان امام حسین چینش میشوند.
@News_Hut</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/71796" target="_blank">📅 23:55 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71795">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">بی‌بی نتانیاهو درباره ایران:
پیش از هر چیز، باید رژیم ایران را سرنگون کنیم.
این مأموریت من و مأموریت اصلی ماست.
@News_Hut</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/71795" target="_blank">📅 23:32 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71794">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">ساعت ۲۲:۴۰ پنجشنبه؛ ملوان‌ها در اطراف جزیره لارَک، از چندین انفجار در نزدیک کشتی خود خبر دادند.
@News_Hut</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/71794" target="_blank">📅 23:28 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71793">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IVIUxxy8DdvK6GGOnnAAfkZE_TRCgPFXj1-vmYcKDCHQEWArT1f6Di08HpNmxFz9UTE-TElxJpzt1e8BCfe2QMT7h3XGeZUev6DZUKzlMspDt4aI_aj3a92ePU-hARNVLS9PKu2c3dzJsO_tfjlqWpx4AyFvf54DrQXDvvUgURi8RTzoxE-efEML7A67MctZYSqHZgO0RDp8k_Ozz8j7bZ6PF9heeOlQo2zeOFOWnA3ZxMIT6C1uWnXntakVGfqJgQVIbrJ0M--ZUj5yo-4FZnT_jv7v5yKGZcOVMXuzjEIhEI5AyzttGsU8V-y9jDXBOLr6z_aTxOkWqCG51cE0qw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سازمان عملیات تجارت دریایی بریتانیا (UKMTO) از وقوع یک «حادثه امنیتی» در فاصله ۱۶ مایل دریایی شمال شرقی «خصب» عمان خبر داد که شامل حمله به یک شناور در تنگه هرمز بوده است.
هیچ‌گونه خسارتی به شناور یا جراحتی میان خدمه گزارش نشده است.
@News_Hut</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/71793" target="_blank">📅 23:22 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71792">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eduHcW9MnoByPNpsprIVSknUAHZwN-g6gFahIevgOMf3xvUHwD2ZYHlicIBTLZFAF9YzqSdSlTFAhrtObpCB5wMEg-lOOha-qvdAAhGZP1qbcPRqgu8kqWiAwKV80OaLru3GSa9GGAZEejchNENdk8yZ7bsWgvzQl4hNtJtdEVt3oOwJuO7fWWyeXzT5TIPFyVmOuQr6SZ53TFbi4NpbxQBhXWn1mCWSbHOG74C_LYR84JT9wIqOcl5InUuRu1K81XW49zFnDPennSrTZ5aApE9k3yxPASgQ1Soa2r2kDOFbW5HGWV0CMypZ3VknGC25Pdd63Jlaoyw_e2MgQ3-MUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزارت خزانه‌داری آمریکا «بیت‌بانک» (BitBank) — یک شرکت فعال در حوزه دارایی‌های دیجیتال در ایران که تحت کنترل بابک زنجانی، سرمایه‌دارِ پیش‌تر تحریم‌شده، قرار دارد — را به اتهام تسهیل دور زدن تحریم‌ها و انجام فعالیت‌های مالی غیرقانونی، تحریم کرد.
این اقدامات همچنین شرکت «تجارت الکترونیک پیشتاز سیمرغ» (توسعه‌دهنده بیت‌بانک) و سه تن از همکاران بابک زنجانی — شامل حسین‌علی ذاکر حسین، محمدمهدی ذاکر حسین و سید عادل حیدری — را هدف قرار داده است.
@News_Hut</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/71792" target="_blank">📅 22:59 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71790">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ubg4OilVQO4YxkHDyu1YhPe4cEvLlA7S8emlz4jUUzzf2Cws4auZvfNUTcddD_N4H67NggxeD0L-N7HxjsyJ-30BDF32mA2Z7ot0QXlUvk-0XTp_3CGZDalgS_RIaXels6TBOqkBWaZkM4K-Doq4d4zovw5oPnngQZfauTEgs4uIwev0Dfali1gwTQW5Ve7BbQU5f_9VxJnJEZWTDMURoNJXn_iHHN-YZ8BTxPMkPRMyxdPUwxGM0R8tnEqGbXU0_PgjEM_MOW5GW0K5PhSXT6pp_AWHKCqYRl0xHQYhTCr7wW10NPqTZ1HSF_SLxAhRaJLH8kVVGITmS8F39XD25A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sTSziBieXVEmWKgYBRcAhe_NksdSuTpaX8A5OqQtVt4kYxN-FTlrkfgdYvHc-4nZq9Bmu84CFsmLblAUr1Hl5Phora1Okeqax29m03hGXTsMzoFgdGTAFMPGMYYpKWI-a-FVmoa9qeJkge6oyQzOGJMP-hAWP0AvcMfcjR0NlHfCdHvRx7Op7J5rK-bHnSVJYaucQ99A225u7clYxvz0PbQT_OWKU_-47_h2sriBB4ktXzNGz1lByZIKplG2fhygTtSkIdgJslar0MqPXTpi0b4SzArXKDqKIbru_gmWdUg4Vs8nqvCeE-l0HQ1Eb0XtAfnHRdyhrY1QE-snhVxDWg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">ایران به سرعت در حال بازسازی تأسیسات طالقان ۲ در مجتمع نظامی پارچین است - یک سایت سابق برنامه سلاح‌های هسته‌ای در ۳۰ کیلومتری جنوب شرقی تهران.
ایران یک برزنت بزرگ روی این سایت کشیده است تا کار را از ماهواره‌ها پنهان کند، و در زیر آن ساخت و سازهای سنگینی مانند کامیون‌های کمپرسی، بولدوزرها، پمپ‌های بتنی، جرثقیل‌ها و دیوارهای تقویت انفجاری جدید قرار دارد.
این سومین چرخه بازسازی است. اسرائیل در اکتبر ۲۰۲۴ به ساختمان اصلی حمله کرد.
ایران آن را با یک مخزن مهار انفجاری جدید که در زیر یک تابوت بتنی دفن شده بود، بازسازی کرد.
اسرائیل در مارس ۲۰۲۶ دوباره با بمب‌های سنگرشکن به آن حمله کرد و سه سوراخ در محفظه ایجاد کرد و ساختار داخلی را تخریب کرد.
ایران تعمیرات را تا ژوئن ۲۰۲۶ آغاز کرد و اکنون به طور پنهانی در حال سرعت بخشیدن به آن است.
ISIS (موسسه علوم و امنیت بین‌المللی) بازسازی مکرر یک سایت آزمایش انفجاری قوی سابق برنامه سلاح‌های هسته‌ای AMAD را "عمیقا نگران‌کننده" می‌نامد
@News_Hut</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/71790" target="_blank">📅 22:35 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71787">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vx5u2uxKDj1CsPV9g3GETF2SLaTMccgtv_vUEkgRqzK4q-GvdHzXDYkiyfKHKQyqqp5lYL4LHK49K59eZFZoGk2-y34JOaqekV9nXT60ICo7PGVYXO6f5qtGdSsH_T8Z9VQqvEyTVjpB4KPoli-3fuONI6Om11wnUoHxJWdiTNrlDuxVXpwUR5gBBZqcfnHXH1D64Vl9iETvFynV6jH26VnqkQ3Pe8tXRqbrONU-MfcXq-buDZyBZpQqz8l3u3KA3kZkLEExMCtOCPlBUJh5UdE7bR1u5ao238XUIiNYbqOMJIe2GQRiDjNYZmo3diLqtpqJrjDBEn9R7GiUJ7sfRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TauAbnJEubqAk2qDfKpzkSH2hl3eCS9ipXEzmvJyuwyCcSVeCiMhpkAiVf3QU-PhI5RuQ1sTcKhTOtp2Ww1N2IluBc67FKc0cmK9LOy7MHHwio8Crp0zbZ01Y3xC_SIdSnTPCqI678jEWC55mKBF83ahiVN556l-IunBHPxQF2PZ_71d0WNfybyjGmVKOAe9cyHQKlxYPChlQ75dXWvD0RTB2vB83dZ9SmccV6GjxDeoLuK4P1YBJh8QGU9oMPs1MBJGWbCR372138MV3NEu3K5nDYCbh_t_aqZAf8hqbGH5Siv5lR4mbEbt5drnBz1XpaiU-JhnNRBkKn-WbibF0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dZy_-GCUpotIlKlQaMQViBn34wLD9A7sCBnsNxOzecQ3XMqRQtkBDSaRRnMOoMfb1wcFXOzXFXF_Q6TzYR3oW9G3Kg9yTitnsOSh1vD2jOV92-Gdg2S3G14mMUhSCc21cnkrTUK4tj2sN4h17GzJX9YJAGqjNeUB4TfliUxJMdlPUJ7x6IYx2oHDvLKdvidl6hvCdCxv_ugG0PHdJmUUON82JCb3bTGmg0pFHzQuRJQNY65tnw0N7VQLzyoXTYLj63v3E84ktO75lM82Hfa-di5oTMWvGAsocWqYBLn3Jvdu53AJ7v2rkGlDMi_6BxoN5B1DQ7e3Dnu_MuolT4zhbA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">عکس های وایرال شده از علی ضیا و زیدی در فلورانس ایتالیا!
@News_Hut</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/71787" target="_blank">📅 22:15 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71786">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4e44acb8ce.mp4?token=TuwdxobclOOrGC3gfMPLGxpemYs7_hsoy6zkeBVhNhK3bB-rzpvEVvpz53bXYUJmiILWHP_AUIWz4izKv93xKAPO5OtrIXNT6pDOkpZ-MAC_KTl3HH3p06CrvTGBcJhiNs26IU9b9qwj4g-J2CbDrocuDrMvsQUW9951oNDI-hdAYP8Cny9fYyg8vBpWF085jsfut3Z13qKR7Vph495j2uqUx_QJqlWGJbsCPRPEUnKtx08TcSQNDVmC9fxgcbJQuI0D94Mb67z-shthCwAf9vfMjCiP_mzJHWSSYxa9OK1XcGnjAya8ND6Aj-HzBGx3NebZsCsNWZ_yQ7NxobjkuQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4e44acb8ce.mp4?token=TuwdxobclOOrGC3gfMPLGxpemYs7_hsoy6zkeBVhNhK3bB-rzpvEVvpz53bXYUJmiILWHP_AUIWz4izKv93xKAPO5OtrIXNT6pDOkpZ-MAC_KTl3HH3p06CrvTGBcJhiNs26IU9b9qwj4g-J2CbDrocuDrMvsQUW9951oNDI-hdAYP8Cny9fYyg8vBpWF085jsfut3Z13qKR7Vph495j2uqUx_QJqlWGJbsCPRPEUnKtx08TcSQNDVmC9fxgcbJQuI0D94Mb67z-shthCwAf9vfMjCiP_mzJHWSSYxa9OK1XcGnjAya8ND6Aj-HzBGx3NebZsCsNWZ_yQ7NxobjkuQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">واجير الونگکورن، پادشاه تایلند به همراه ملکه این کشور در جریان سفر رسمی به هانوی، پایتخت ویتنام شخصاً خلبانی هواپیمای اختصاصی خود را بر عهده گرفتند.
@News_Hut</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/71786" target="_blank">📅 21:34 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71785">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">#فووووری؛ترامپ به وب‌سایت «اکسیوس» گفت که در آستانه اتخاذ تصمیمی حیاتی است: اینکه آیا عملیات نظامی گسترده‌ای را علیه ایران از سر بگیرد یا مسیری دیگر را برای پایان دادن به این مناقشه در پیش گیرد.  «تصمیم بزرگی در پیش دارم. آیا می‌خواهم وارد عمل شوم و آن‌ها…</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/71785" target="_blank">📅 20:56 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71784">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NFt-tdiY8bVcgBdB_1g8qDJTXSkaFlWQhWs6nr5Q3qrrsslOmwYXDzuK5vnWkDs-L8lR6pxWx-firSgNLERYtabKfy8DmfkqovWDia8SUuVhPhvXeKEaupolsc36VXFDZnazhV_QWKQ9CCy-q1DCjVi3qE2t0-NorpXxLK995smKDbqEXBTSvNypRtYWHAyHvfZQgZpq7Dut27iugt-ZzYQ3RWFOzR2oyU3FoitYIDbwxiiaCki3EZbweVumD2M0uJvcVMuuBrywRRQmUUl1uOmKzss9u0h8KYEgko-Fc0Cl-zMluqqHcnVIEb1Qbm5oIF0st-FvND7dDHeH0QZOjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#فووووری
؛ترامپ به وب‌سایت «اکسیوس» گفت که در آستانه اتخاذ تصمیمی حیاتی است: اینکه آیا عملیات نظامی گسترده‌ای را علیه ایران از سر بگیرد یا مسیری دیگر را برای پایان دادن به این مناقشه در پیش گیرد.
«تصمیم بزرگی در پیش دارم. آیا می‌خواهم وارد عمل شوم و آن‌ها [رژیم ایران] را نابود کنم یا نه؟ تصمیم بزرگی است. هر احتمالی از جانب من وجود دارد.»
ترامپ اظهار داشت که قصد دارد از فرصت دیدار با رهبران شش کشور حوزه خلیج فارس در حاشیه مجمع عمومی سازمان ملل، برای گفتگو درباره گام‌های بعدی استفاده کند.
«می‌خواهم بدانم موضع آن‌ها چیست و در چه وضعیتی قرار دارند. ما همواره حامی و محافظ آن‌ها بوده‌ایم.»
@News_Hut</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/71784" target="_blank">📅 20:45 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71783">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7b5d03539b.mp4?token=CRnrbLU9HTh8FvjmL7BZNP2TuwHPIAoKoY790pE4fqovjDzClYpW0mr9b6yLhdAz5kkvl09HX7ZUoyjgCo-EGTEOMw-aso7GcKeF_2LUH-vaBEjM02bQ__3RjiDBhvgfTiJb8sn6gpUd3GCtlXmwxaYB_cBiX_HfmggIqSZf3qprAN7YvUBofHsjo2ghcXgw6Y-XPsWWs2RRLY92aSr0gQOc-_MfkLT3iZrEnVxkS4WXbJh5_Y7ySxOIlRuMKNRzSPOANlZF8aswzE69XKuUtDnU6XuHwpMzBxrM2OagRc1Wz9QfUo0Rn2rU3G8q7Y7QKULuW422blilZdR9Nvjb-A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7b5d03539b.mp4?token=CRnrbLU9HTh8FvjmL7BZNP2TuwHPIAoKoY790pE4fqovjDzClYpW0mr9b6yLhdAz5kkvl09HX7ZUoyjgCo-EGTEOMw-aso7GcKeF_2LUH-vaBEjM02bQ__3RjiDBhvgfTiJb8sn6gpUd3GCtlXmwxaYB_cBiX_HfmggIqSZf3qprAN7YvUBofHsjo2ghcXgw6Y-XPsWWs2RRLY92aSr0gQOc-_MfkLT3iZrEnVxkS4WXbJh5_Y7ySxOIlRuMKNRzSPOANlZF8aswzE69XKuUtDnU6XuHwpMzBxrM2OagRc1Wz9QfUo0Rn2rU3G8q7Y7QKULuW422blilZdR9Nvjb-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دیروز در شهر ری جانفداها با جمعیتی میلیونی رزمایش برگزار کردن تا آمادگیشونو به رخ آمریکا و اسرائیل بکشن!
@News_Hut</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/71783" target="_blank">📅 20:14 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71782">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JGthuotQsVdiyGTSgh1foOynvwZ0I804CbuGvaYvE9h8iwozuazO6Ub_3JbXxlnx0YPnrGHR2AKezB33M8PTICya9uvumy-a8JvJwszB5CsySOrRUlmnm9O10OL1l2lIRya3B_q2oWmk8WxVDNr0zMLJjrb57Mlb87G78Ux3WF54SNH_W-jP_g_1WabR4jvuwIgNjkoDs7yT8_xrqghZhKSg3kf1b56FLjw76gc6uQm6_VS3a11_dPBl-z2VOLAm16WZbhXpPkfMzZ4OntVG44aTSojh-NrkI6-q8qVtk0YSPAy-NsT098IaJaqfYzB8Hj_xsUpkRcCsrQ7isB8GKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به گزارش رویترز، چین در پی درخواست عربستان سعودی از پکن — که پس از پیشروی‌های موفقیت‌آمیز حوثی‌ها (انصارالله) در امتداد سواحل دریای سرخ و پیرامون باب‌المندب صورت گرفت — به‌طور خصوصی از ایران خواسته است تا به مهار حوثی‌های یمن کمک کند.
پکن به‌طور علنی خواستار خویشتنداری، گفتگو و ایمنی کشتیرانی شده، اما در گفتگوهای خصوصی با تهران فراتر از این مواضع عمل کرده است. ایران در پاسخ اعلام کرده که ثبات منطقه به پایان جنگ آمریکا و اسرائیل علیه ایران بستگی دارد و همچنان مشخص نیست که آیا تهران به درخواست چین عمل خواهد کرد یا خیر.
چین هیچ‌گونه تهدیدی مبنی بر اعمال فشار اقتصادی مطرح نکرده است؛ با این حال، روابط این کشور با ایران از وزن اقتصادی و راهبردی قابل‌توجهی برخوردار است. در همین راستا، یک دیپلمات غربی اظهار داشته است: «تهران و پکن به یکدیگر نیاز دارند. چین عاملی است که تهران نمی‌تواند آن را نادیده بگیرد و پکن نیز خواهان بازگشایی تنگه هرمز و تأمین امنیت کشتیرانی در دریای سرخ است.»
@News_Hut</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/71782" target="_blank">📅 19:35 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71781">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a7347b9d41.mp4?token=WO22Gjlc1Vk3sz-RePjhmWC1MFq6fXQJKppvwx8ss7XaMUUPk8b3tHoljmGxUpzBzfUukATWqAES9J28dh8PLVSu2D-aneBc1zMtfIsQV-TbzEOU64PsMYDsKkTiQL4m30TbSV5gRLTlb0QzlwBIYqgA6fM_sbv__UD9UL9l-Msdn9paXGQsccm8ub7m7KUyKlZ-TSJ5qsOvqqtAAjb4HksZ2qKZWnYyj3cV7bSDauJ68dqe9YNz1YtsQQhvqplI_GX5UFlrWFFrkUkZpgiFjmtSr2O7tORv6lFpIErTcKpHaUlJ3_2PjZt7HyW37DM6r7GPF5BbGZYe7UOg4XB4Dg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a7347b9d41.mp4?token=WO22Gjlc1Vk3sz-RePjhmWC1MFq6fXQJKppvwx8ss7XaMUUPk8b3tHoljmGxUpzBzfUukATWqAES9J28dh8PLVSu2D-aneBc1zMtfIsQV-TbzEOU64PsMYDsKkTiQL4m30TbSV5gRLTlb0QzlwBIYqgA6fM_sbv__UD9UL9l-Msdn9paXGQsccm8ub7m7KUyKlZ-TSJ5qsOvqqtAAjb4HksZ2qKZWnYyj3cV7bSDauJ68dqe9YNz1YtsQQhvqplI_GX5UFlrWFFrkUkZpgiFjmtSr2O7tORv6lFpIErTcKpHaUlJ3_2PjZt7HyW37DM6r7GPF5BbGZYe7UOg4XB4Dg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عارف:شرمنده مردم عزیزمون هستیم
واقعا از مردم عذرخواهی می‌کنیم، شرمنده‌ایم که امروز دخل و خرج مردم با هم نمی‌خواند
نمیدانیم چه کنیم، نمیشود تورم ۲۰ درصدی داشت و رشد حقوق ۵ درصدی!
واقعا شرایط زندگی سخت شده و مردم رو درک میکنیم
@News_Hut</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/news_hut/71781" target="_blank">📅 19:01 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71780">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4fff9dea68.mp4?token=AhgbRUqNlMHl-4RXKA9Abmm5A1Spcq5XzqN9S8CEFCT-QeQPjpKl3DneuDjq8yJe4dqE-d92ditdzdn_AwjdUYiD21tVpy4lQ1m917SkfU6657c4NiPrAknYn5mDCJzOBEvUMx7m8CaY7f2ai6jRRVhpzkJgBgD1e4iYd60ErissTI5Yoqkfq8QUf6N7IChDjlnwADY-WzrNU8jc8KPcRmOttxvGXedFs-lk_XQcGDbtmg7bBZRldvkM0iGykQTYAtBjjnSXV1L_d73pJYm23I8lgpMhO4F_uFkfYtw9rXOkY2XHySlVEkUB6aPuPgt9LA-qfzJiryHk-8e4fdO1AA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4fff9dea68.mp4?token=AhgbRUqNlMHl-4RXKA9Abmm5A1Spcq5XzqN9S8CEFCT-QeQPjpKl3DneuDjq8yJe4dqE-d92ditdzdn_AwjdUYiD21tVpy4lQ1m917SkfU6657c4NiPrAknYn5mDCJzOBEvUMx7m8CaY7f2ai6jRRVhpzkJgBgD1e4iYd60ErissTI5Yoqkfq8QUf6N7IChDjlnwADY-WzrNU8jc8KPcRmOttxvGXedFs-lk_XQcGDbtmg7bBZRldvkM0iGykQTYAtBjjnSXV1L_d73pJYm23I8lgpMhO4F_uFkfYtw9rXOkY2XHySlVEkUB6aPuPgt9LA-qfzJiryHk-8e4fdO1AA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">طلافروشی از اون مشاغله که نکات دارک زیاد داره
@News_Hut</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/71780" target="_blank">📅 18:15 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71779">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6caef19c8a.mp4?token=kqrvlP1VqGINduxmEOSNwwNU6Kbm80O1WuWTiVk6CgXolJCNCsZZxBwQhZGlmltavMR5Mavl3am2TwRi5CQM4kAbCaCsYpGR5DYe9OCq6CJloJ5iClUIFzsHx7yVUWmOleN82YXiJRK-At70XkSKx8RQZ5_kDihGsnUdohKFmevQ0E-n7Mi9QCiFxBLXbkRrSte9kSUFUGY2EX5gGVTY5njWykjgxRwPeovoGyx3_hhNP7X2TSgAK7iAQ4nUAJ1iDVYG8cAcRu0X09a7Y8nfDbXPc0LxK6I6DAUoEHoOj4tFt8ZBLSFBk-iFIqnNQ-brmpdoP16ijFIOIghMmqrSyQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6caef19c8a.mp4?token=kqrvlP1VqGINduxmEOSNwwNU6Kbm80O1WuWTiVk6CgXolJCNCsZZxBwQhZGlmltavMR5Mavl3am2TwRi5CQM4kAbCaCsYpGR5DYe9OCq6CJloJ5iClUIFzsHx7yVUWmOleN82YXiJRK-At70XkSKx8RQZ5_kDihGsnUdohKFmevQ0E-n7Mi9QCiFxBLXbkRrSte9kSUFUGY2EX5gGVTY5njWykjgxRwPeovoGyx3_hhNP7X2TSgAK7iAQ4nUAJ1iDVYG8cAcRu0X09a7Y8nfDbXPc0LxK6I6DAUoEHoOj4tFt8ZBLSFBk-iFIqnNQ-brmpdoP16ijFIOIghMmqrSyQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چند روز پیش اهالی یه روستا تو هند که حدود 2 سال از وضعیت بدِ اینترنت و شبکه 5G کلافه شده بودن؛
زنگ میزنن تکنسینِ شرکت مخابراتی بیاد و وقتی طرف واسه بررسی دکل اومد، گرفتن و به همون دکل بستنش و گفتن تا مشکل حل نشه، آزادش نمی‌کنیم :))
آخرسر پلیس اومد و 6 نفر از اهالی اون روستا رو بازداشت کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/news_hut/71779" target="_blank">📅 17:38 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71778">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/71778" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/news_hut/71778" target="_blank">📅 17:38 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71777">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UxN5cEkXmRRV26Bd0Xx2f-TuyBUykYp6QHCgbm6h4Er0P_Z5oGynTgvhW3SYUyeUUiYog6LsWWRU9bsZhONHCLRO2gxY8522cqDdqb05tpW20nP-UrsFtXoDhdnSyrp4CXrcJag7_OGl9ag85qW-7lOjgkCjW7nqGw13_hJ9K3XadDLdn2BuaPsfyvbpgqdmMWbdjVC1LVfA9MB9UpILdNeUMpuSYl2_IIZjelxuSN46DXnclucbl7zspB_dqZ_ZL5SbaGxA6xcn-bOOxOjd-VZxAEwFQlS7FeneS4ySXvgBK9y0e4ktysGTyV9j6VHf-i7k2jm2fYFvJxmASghS-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
وقتشه هیجان رو به اوج برسونی!
🦖
با
TrexBet
مجموعه‌ای متنوع از بازی‌های کازینو‌ی زنده، و اسلات‌های جذاب رو میتونی تجربه کنی
🦖
تجربه‌ای سریع و روان
🦖
دسترسی سریع و راحت
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
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/news_hut/71777" target="_blank">📅 17:38 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71775">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4bd5052dd8.mp4?token=opH4CIbXTYeAJ-jicco0smvpnRvEI5R2UI9r5PcJ64qys0Nay4dE3CT1xIbEk6h3AGHP5afFD2QKwREkrrdCtgeHyW3TTIwA-vts9J5-NcrsUdCYy7io5GNUnDiS6FHpP51D_h6BrVYt3v9Is82pINHkJBargVBZWR6DiHHj7lHdI0h6fgPDAG45vfPc4DCKv4dlmt3dia1l3bsIxkltNQmXn9M-VCsX9pTRYVnf2mqSBJ157heHgmFFmHr7JGLfNSzumOCeWKv3rKV9Xb9cf-JCDp0qQbIlriyY6K5suxHndD0Yc_HOMNr-BvBVvc0ei3t4faeJBBHdBLidWzCpNA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4bd5052dd8.mp4?token=opH4CIbXTYeAJ-jicco0smvpnRvEI5R2UI9r5PcJ64qys0Nay4dE3CT1xIbEk6h3AGHP5afFD2QKwREkrrdCtgeHyW3TTIwA-vts9J5-NcrsUdCYy7io5GNUnDiS6FHpP51D_h6BrVYt3v9Is82pINHkJBargVBZWR6DiHHj7lHdI0h6fgPDAG45vfPc4DCKv4dlmt3dia1l3bsIxkltNQmXn9M-VCsX9pTRYVnf2mqSBJ157heHgmFFmHr7JGLfNSzumOCeWKv3rKV9Xb9cf-JCDp0qQbIlriyY6K5suxHndD0Yc_HOMNr-BvBVvc0ei3t4faeJBBHdBLidWzCpNA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تگزاس اونم وسط قم
@News_Hut</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/news_hut/71775" target="_blank">📅 17:32 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71774">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1104cb463a.mp4?token=oAEmD6XYRchaVwiXg8I-9ajviJKe53A4WlWr0TlJTWC6jxnBbgi8CcQi_FYSwQoBB7RtnJLYA-h6fog-B0motBc_vXk1RTx6lOqFnK_YJYdK53wKMMeofZOJw1_CDgp1SrfX9SyGuRThdZR97jU07fCylefevcYwMxQqxL5QgzgYhqwz2kn2T7h4CNCRxsDQrOLPimbCqVn_NB29e65UQL5j6yt7HfQpY9MNKdDk4W_NWyvXDrbwAzCguWwPTjbAVGwcEq4akFdBLjd--GqdlKk7XusZkO2B3fDZ8P1y61FZoTISBStGitsjpSoIuArdRDucBFn_kluVNQ_cO8J9kA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1104cb463a.mp4?token=oAEmD6XYRchaVwiXg8I-9ajviJKe53A4WlWr0TlJTWC6jxnBbgi8CcQi_FYSwQoBB7RtnJLYA-h6fog-B0motBc_vXk1RTx6lOqFnK_YJYdK53wKMMeofZOJw1_CDgp1SrfX9SyGuRThdZR97jU07fCylefevcYwMxQqxL5QgzgYhqwz2kn2T7h4CNCRxsDQrOLPimbCqVn_NB29e65UQL5j6yt7HfQpY9MNKdDk4W_NWyvXDrbwAzCguWwPTjbAVGwcEq4akFdBLjd--GqdlKk7XusZkO2B3fDZ8P1y61FZoTISBStGitsjpSoIuArdRDucBFn_kluVNQ_cO8J9kA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نتانیاهو درباره ایران:
میل ایران و نیروهای نیابتی‌اش برای نابودی دولت اسرائیل از بین نرفته است؛ تنها تضعیف شده است.
تواناییِ عملی کردنِ این هدف، عملاً به‌شدت آسیب دیده است. ما به وظیفه خود عمل کرده‌ایم، اما هنوز کارهای ناتمامی باقی مانده است که آن‌ها را به سرانجام خواهیم رساند.
ما حماس را نابود خواهیم کرد. همچنین، پیش از هر چیز، رژیم ایران را شکست خواهیم داد. ما آن را سرنگون خواهیم کرد؛ این رژیم سقوط خواهد کرد. با حزب‌الله نیز مقابله خواهیم کرد و آن هم سقوط خواهد کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/news_hut/71774" target="_blank">📅 17:03 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71773">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cb11cb6bb5.mp4?token=BNgiqC_eWS_-6QZmCHa48c686g-i325KrHQ9Z5wAYos4hSwcICO0xrUu2R6MuKsflQrFInF1LU7j6K4k0f6CtmkYY21U1eA6_1XB6XQXpf89WfF64bmvclqRucscYB5zEWHJGiwdAqfoDsmJSGmCz8tVY6djUYRgVLkfjTY8K9289FK3FvX9IJsWKTgPpTlcMAl7MZHQgsC_L6h9preKCd3fISm3BoxvsMc92Z8ZbGypAj3ssIYnzR8ynUbHXn-y2WTo8gRSLTkvyhDEJ9wjyRa3bx7omseOxR064xTUzMavWR7Xf1TTZJzR_Y-BrdNb9VWOPRYe4niuMQSePNxjhw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cb11cb6bb5.mp4?token=BNgiqC_eWS_-6QZmCHa48c686g-i325KrHQ9Z5wAYos4hSwcICO0xrUu2R6MuKsflQrFInF1LU7j6K4k0f6CtmkYY21U1eA6_1XB6XQXpf89WfF64bmvclqRucscYB5zEWHJGiwdAqfoDsmJSGmCz8tVY6djUYRgVLkfjTY8K9289FK3FvX9IJsWKTgPpTlcMAl7MZHQgsC_L6h9preKCd3fISm3BoxvsMc92Z8ZbGypAj3ssIYnzR8ynUbHXn-y2WTo8gRSLTkvyhDEJ9wjyRa3bx7omseOxR064xTUzMavWR7Xf1TTZJzR_Y-BrdNb9VWOPRYe4niuMQSePNxjhw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دیروز تو یکی از خیابون های همدان یه مرد به یه دختر تعرض کرده، مردمم متوجه شدن لباس و‌شلوارشو از پاش درآوردن.
@News_Hut</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/71773" target="_blank">📅 16:31 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71772">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/142ff032d7.mp4?token=eVikp04xwpR9sq9ZaE6EXafgFLuDm9mnHFnzTlrHdTqb7cY1cQK2I3-16lsv02cHOGTNZ1MxtOcodJog9mnmKAyIB646PFmZsc_8jX260nV4t_gD10ZP4wqCO8AGlNyNWNmv5MS7VYaVMxPDIc_y8sxbiPdFGYBCFX8RmuI-xK-TMSKcLZsPzQwtrwPadP6xOwCwjrcIAKUWXTKmRG8cmMk6NQekN-W9vXktr0i64SiRpsOTivtCX4Rt7TBsIVtwjgpWezHOJFuq2E1ZnePbW0F9lQZgjw7yhhVldLi5gMp2ZS5VlLhwtVe9s3DP3CCr4lLFswHLDPlN724ZCAbk_Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/142ff032d7.mp4?token=eVikp04xwpR9sq9ZaE6EXafgFLuDm9mnHFnzTlrHdTqb7cY1cQK2I3-16lsv02cHOGTNZ1MxtOcodJog9mnmKAyIB646PFmZsc_8jX260nV4t_gD10ZP4wqCO8AGlNyNWNmv5MS7VYaVMxPDIc_y8sxbiPdFGYBCFX8RmuI-xK-TMSKcLZsPzQwtrwPadP6xOwCwjrcIAKUWXTKmRG8cmMk6NQekN-W9vXktr0i64SiRpsOTivtCX4Rt7TBsIVtwjgpWezHOJFuq2E1ZnePbW0F9lQZgjw7yhhVldLi5gMp2ZS5VlLhwtVe9s3DP3CCr4lLFswHLDPlN724ZCAbk_Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بانو سیدنی سویینی برای اولین بار تبلیغ عظیم خود در میدان تایمز را می‌بیند.
@News_Hut</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/71772" target="_blank">📅 16:02 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71771">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/50d6312725.mp4?token=IJcPm7ZKzU4pwOquHQ0vHqu0-iwBCeUAY1zQGUa2awOZDicV7YyXi_d993oAjYRuHbllzmmLojWgaWbwoFqR1AO5c2YhMMetjdr0QKHjkigiBqkaoSAVSHVcXiQEr8OpSDJhkZ_PPRJlsQM7r3rhbA1OztrKloqityqCHvIaOPWqhDs5jH9Z-fg23M_OWX9gYX-w9jMoFzodWzmjJMPWqHlxyoQdmXfH7xStS1UoKPLUiluRu7V_YDCEqubSIhxrkQOMSSoImaJ0Il-MUZ_1QxBYipBGpJAkl7BJIpp1WKMRyaqCJYVUzRdQ95JMLu75BQXsfyTnZgoS3_QJGhPhTw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/50d6312725.mp4?token=IJcPm7ZKzU4pwOquHQ0vHqu0-iwBCeUAY1zQGUa2awOZDicV7YyXi_d993oAjYRuHbllzmmLojWgaWbwoFqR1AO5c2YhMMetjdr0QKHjkigiBqkaoSAVSHVcXiQEr8OpSDJhkZ_PPRJlsQM7r3rhbA1OztrKloqityqCHvIaOPWqhDs5jH9Z-fg23M_OWX9gYX-w9jMoFzodWzmjJMPWqHlxyoQdmXfH7xStS1UoKPLUiluRu7V_YDCEqubSIhxrkQOMSSoImaJ0Il-MUZ_1QxBYipBGpJAkl7BJIpp1WKMRyaqCJYVUzRdQ95JMLu75BQXsfyTnZgoS3_QJGhPhTw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جبرائیلی:
ایران ظرفیت گنجایش ۱ میلیارد نفر داره، میتونیم به هر فرد ۴۰۰ متر زمین بدیم تا به ایران احساس تعلق کنه.
@News_Hut</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/news_hut/71771" target="_blank">📅 15:30 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71770">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/edf947f98b.mp4?token=FLwMO2Pgq0H2dmmmi1t6x_Kz3lq8NMxXP0arzpjg6awNsKGk2C9zs5O0WjpIVhsW1bhmT-sfcBhKVVJZZVtWP2doUvqyftT9Yx9gBj5loRsl4EjpGopvuGmtooBGdZBSTSuLlCoiTFkCiZC4j53D_29zwlYUP0KJ3cvzd-IaKv1i2Fw95o-HWO5HA23F1Y1sA9vuZHcZd9Bsa-qR5T5tU-Q6ywemK4sZXYUwqMjM6yQa-Nnp2ugzORQtr9w5ns91A7aZ1v4kGVfAx2j3ZIKv7wfqbvSSWCKhtMv1nsiHMDuDf_PSbwCnVLg3d-152Kh2dvGL46HoWyvSbqbaGXF0KQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/edf947f98b.mp4?token=FLwMO2Pgq0H2dmmmi1t6x_Kz3lq8NMxXP0arzpjg6awNsKGk2C9zs5O0WjpIVhsW1bhmT-sfcBhKVVJZZVtWP2doUvqyftT9Yx9gBj5loRsl4EjpGopvuGmtooBGdZBSTSuLlCoiTFkCiZC4j53D_29zwlYUP0KJ3cvzd-IaKv1i2Fw95o-HWO5HA23F1Y1sA9vuZHcZd9Bsa-qR5T5tU-Q6ywemK4sZXYUwqMjM6yQa-Nnp2ugzORQtr9w5ns91A7aZ1v4kGVfAx2j3ZIKv7wfqbvSSWCKhtMv1nsiHMDuDf_PSbwCnVLg3d-152Kh2dvGL46HoWyvSbqbaGXF0KQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این گربه به محض اینکه براش موزیک میذارن، شروع میکنه هد زدن :))
@News_Hut</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/71770" target="_blank">📅 15:00 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71769">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">حال و هوای تهران در ایام تاجگذاری  شاهنشاه محمدرضا پهلوی، سال 1346 خورشیدی.
@News_Hut</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/71769" target="_blank">📅 14:34 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71768">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DHhMiredvPTMAtkaFgJUL6vq7S39FfgOHmm7x8w8b04Q24YeeQowYp02n7pTeE1Cj4tGzgYpXIphiaIjWxaKK_plytzHMG1PG04jy1Nh3uVqmtLjWSo_WoQI-uhclj476iTc110CfKjBzbF3Aqif0vUQkTMqUjbe8MJGmnksvzRtALYrTWLCrlmPHPHFCtWxnTImgnfYPXx_cyPUPnYwwOTZeu5-hiIHJNEBFY4LSZq_Zv42jCOtBpNZLQSxLnoLRvE4SyGGe1i1WEiHG8XbrXx96X5iEqcXnU1bdX7m9MwIIZC6UHqLtj27UIGmNiuoagFStTRaGvSDKCQVVhIuaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ده فروند جنگنده اف-۱۶ ایالات متحده، به همراه چندین هواپیمای سوخت‌رسان، صبح امروز پایگاه هوایی «لاجس» در پرتغال را به مقصد منطقه عملیاتی فرماندهی مرکزی ایالات متحده در خاورمیانه ترک کردند.
@News_Hut</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/71768" target="_blank">📅 13:46 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71767">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/phOpDXgh0SmM65neADr1Y53z3EUqLd9PIik8uvlrxU6P4AOfa5QpUOJTZzXtk9b2z2ajiD1Gh-sRFnwDdSJnwvn2jqmEdguD3NUao7VSQ2mptDoSkC_ttSv_JtsEKvu8ASdTtybHGViheYAEjO7tEt6m_seXyAW2eGUVnIgUciycjN6WPV2lzjz24Xk6OpC6GGT1ezeJ-dem8uzR0n9bynD-mwZA0gI6w5jehoouQ5D1UEmPzNSnfN6bICgwCfjD9xSfddAruUkhdcPq4jWwoH2vyhs8U422vIWi4X7i_79dXy2FUktEzR_yfgri-pyM9MNN3Rs2h_mwEBEjI2nvlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بلو بانک به اونایی که بالای یک میلیارد تو حسابشون پول دارن، کارت سفید میده!
@News_Hut</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/71767" target="_blank">📅 12:50 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71763">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/olnmfmY3koZscvTJ3Ff8gu3GSaJZjCWc9WMCR2V6RQtOxjQF3jPhtaFbF6tKyoazvP-1VfuXJNfgvAlsS2enR04r-gOigjn2hF8cP8hk1vgtMT4S552FLhWJN3IOCOxTTIe9jQbkDBY7s8JeHNIoU2976VwzfgdbCDFrwaVbKj96D5JV50HALDSTzefXo-IP0EM1OSCRhCA_X4Yjd_-PTqlJrJJMzvEcqDvIFyHJLjpexeE1TbtVHXe9EYKSNEVweCQMhXNGTja_berv0YUwbvT-IUE3eUHbYXX8syHJvASAz_zhmOPBUPv7wWDaVJyAn76jo38l6-3EbHIfdsAvJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/W5Y-nxt6drML9bhz0avh9Mk20KTuNyauDm_f5L6ABTddXOL_5NvJ2FXWGZxCqY_XbYRMKOFSdFzllZqrefjD_uaS5a2E4YFn-7gS5zEENEqIfAtNvg0yPGs3Q8qW3Zgln03YBwTkDwzFjQZxyVwPtTwDfR5Vyd26rqrD03bHjt7hLofy7pSopR8pgQMsJcvtS4IZeATq_7mL0mXTn1DipumWwK2ctP1k1tcwBcA6zBQ702OWV4S_V4-05kynID9tVYxuFCe5t6dvDFJEjgC7uz35lBT91MNe1iVUOOBeX0M2CdRDxW_FEL30tmLS1z-hLbCK89VnIXbICzrXLSqCNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Cdd5-hIXxg2BYKtwy69qdzBeXv_YlD0dNhtfpMkTW0cEo5cUZm5ckUgbyqfUkHCqT7OQtPim9v_Ri3nCB5UKo7RyuzpFDC3F760eA-lNBqzjN-OAGsZ0YvYe6Z2BXACCMQtLNUEf_xqEurlO6ScisXf611VbVioQcEsNOWjDzaBSemZ_QaEfnmHuyONCG2YIkAi8j2_ooIZssuZ_rZRcVGveiZ3bfSPq-W6Q0zkU7P8jnsVjWHtjD8gvU3fExWrezl8ExlUZiuouNM__bGZfL7rYXre9tS00RupqtwGRCVS5a_7veZcN1oaVY01j-3i-vznS5L2HAlJWEjxet4CCRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nHAwbOGg3R4F2_VJmbt-1JqDbzvwOGPYvDbLDXhW0vHdx3uoQPCK3R_3lOAnckPh1ZouZQI6lZ1Wx5sdxvRdJtYNbBYQP3oVgqcNn92q4GyIO-Goat02-IHg8ZsXnj9AoM6PNnQlyRG3Rc4AOdtu2C6vGVnhLU33GK-AvULxPoFmXWzbqxvXF1xMRtK7EXAk-sq1xjrzFT3S_NjnZ8fPgr2xgspZmIJL7ZURHCmoXmlQcWOY3gujB1aAZ4L9oKQ39OHXmaJFrm2WF0DTJPqxew8lprxM8MRB0ZPcokMn9L3PhZNTOXjUQ9yURsHL0VIuE3EJxla31_mZI_WJsixGkA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">امروز ۲۶ شهریور،تولد کمبوجیه پسر کوروش بزرگ و روز پسره.
26شهریور؛ زادروز کمبوجیه دوم، پادشاه هخامنشی
کمبوجیه دوم، فرزند کوروش بزرگ و دومین پادشاه شاهنشاهی هخامنشی بود.
کمبوجیه پس از پدرش به پادشاهی رسید و راه گسترش قلمرو هخامنشی را ادامه داد.
مهم‌ترین دستاورد نظامی او، فتح مصر در سال ۵۲۵ پیش از میلاد بود.
@News_Hut</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/71763" target="_blank">📅 11:59 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71761">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P5k11mV7fysm-ym-dRp2dvwBpDIgYHKyAwQRX3ulEyXwkwpnYzHplAWVzUwYGnqizDgmFOUmOAc1C-RTy05wNYvReq7-GKXAB2Yic1zVsG0a2A8ny-BRV41yzr_8OJu-uGxZUiu97DR-7bEmUl1YuRl1rbJpaKBkIao4txplWZPuult43wbuC_UqFSZJIcPDHS5CqDJwlZPTURoIiTDSJYKtfuQCFBmdn7Oo0xUaQIqfREJ14Ig62meYTpz4-TabiHYCK2UpyTZDxcAQO0klyWJFrQQKvQK8MAwMMULmwSZpwOQoK6z9LbT70heqy0wJLBXzOqsS2iOGrY33VbFxVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7fca98f341.mp4?token=hm6lGqSgTau8FxluixXtG8V4Vh1i7J74jEoLVw9cOQIFmu1gUOdfoeHdJiK_LUeAToIWj4Y3BSDqFsL3nxUDn4KFaP15Tz0E70f1whl071fTzbbaK6KwpujZ0TTaesE15tIH5rzmBRwtWCXYanndkp0B0WKBrcKST3wp4tO487XfgG0fMcRHLKEx8THfPtYZOFX0PsGJxak_7ktDW3qcH3mOB9OF2Dgm4XZTBcIvyaWSI7w7xAGGvNWkZ8t58pMs6AgYNrV90PG32S5ujWRU5x2yko3uzl8GY5KIdu8_eFdeAbaZx6hqBJ9IHt_QyvmePR808sc_0Pbc4f9Jljvzvw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7fca98f341.mp4?token=hm6lGqSgTau8FxluixXtG8V4Vh1i7J74jEoLVw9cOQIFmu1gUOdfoeHdJiK_LUeAToIWj4Y3BSDqFsL3nxUDn4KFaP15Tz0E70f1whl071fTzbbaK6KwpujZ0TTaesE15tIH5rzmBRwtWCXYanndkp0B0WKBrcKST3wp4tO487XfgG0fMcRHLKEx8THfPtYZOFX0PsGJxak_7ktDW3qcH3mOB9OF2Dgm4XZTBcIvyaWSI7w7xAGGvNWkZ8t58pMs6AgYNrV90PG32S5ujWRU5x2yko3uzl8GY5KIdu8_eFdeAbaZx6hqBJ9IHt_QyvmePR808sc_0Pbc4f9Jljvzvw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نیروهای اوکراینی شبانه به یک پایگاه هوایی نظامی در منطقه روستوف حمله کردند که منجر به وقوع انفجار و آتش‌سوزی شد.
حملات پهپادی همچنین پالایشگاه نفت یاروسلاول را هدف قرار داد و باعث آتش‌سوزی در محوطه صنعتی آن شد.
این پالایشگاه یکی از بزرگ‌ترین پالایشگاه‌های روسیه است و ظرفیت فرآوری بیش از ۱۵ میلیون تن نفت خام در سال را دارد.
@News_Hut</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/news_hut/71761" target="_blank">📅 11:44 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71760">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/71760" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/news_hut/71760" target="_blank">📅 11:44 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71759">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uBWds2C38LgzgcGXst_ZqA8OHj98NNqMm2r6kIwdwGu73ZIPFebT3EUTcun8UplDxMVIhOv89yfR_YoS4UXSUdDQWhLxHGmQNajORz9nJy0_PA_cMvqJUZFqBLYzt9IUN_V5rgTgTrf5b998-FgK2Y0UPGRAIJVDtO-3fTqwgl4UBZ4z0Z5cd06lt88a9eWJ56K3Zi6dXd8lgem9PzCPqAD3S_elOpntnB-jyptvYPEpJSvuUScQSTFdy2iIFX5vByey5M2qMAumR-ybkp6d7tNQaDhk4k5x2dyTvMt0sBcnixZBKaWruQZnCioppR-SpfjdbixAlieQueosrSSaBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
مچ‌های مهم امروز در سایت بین‌المللی
TrexBet
ان‌ئی‌سی نیمیخن
🆚
یونتوس
نوریچ
🆚
منچستر سیتی
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
انتخابت رو انجام بده و آماده‌ی هیجان باش!
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/news_hut/71759" target="_blank">📅 11:44 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71758">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/40e05b335a.mp4?token=vDWDBquPq4I_ZwAXlLCgzWmxDN5rCz5JPl-rRCCVekpYMIEeMQiCqayFezw--VyaMa6o32Hpz1cPGNuvSuBovGt1liem29J5fbospkieVaZCx2ehpEdNrGvtpR1_gSXag_qt-Do13HrcH9QiixnkTJSjpyJ5DrQJjEqhovOEPTTo8vVIb7-nkDlC2KZp7uG1fXp_jflsDc3Oa4B2Mno0wkH_MK3MUIz0bPZFq_7v8qttUUZfcEz3y3VhezQrpQOnvEAtTSsqNs4KJCJOPAES2WMddjuny9ycYtKQMnvbbyfaN9RuHFNs4gwHylx6a_IiVoPVAtOm6VQcHzIQK08W_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/40e05b335a.mp4?token=vDWDBquPq4I_ZwAXlLCgzWmxDN5rCz5JPl-rRCCVekpYMIEeMQiCqayFezw--VyaMa6o32Hpz1cPGNuvSuBovGt1liem29J5fbospkieVaZCx2ehpEdNrGvtpR1_gSXag_qt-Do13HrcH9QiixnkTJSjpyJ5DrQJjEqhovOEPTTo8vVIb7-nkDlC2KZp7uG1fXp_jflsDc3Oa4B2Mno0wkH_MK3MUIz0bPZFq_7v8qttUUZfcEz3y3VhezQrpQOnvEAtTSsqNs4KJCJOPAES2WMddjuny9ycYtKQMnvbbyfaN9RuHFNs4gwHylx6a_IiVoPVAtOm6VQcHzIQK08W_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هنرنمایی یک تک‌تیرانداز در رقابت‌های ایرسافت!
خوبه که این یارو تفنگ واقعی دستش نیست!
همه رو هدشات کرد!
@News_Hut</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/news_hut/71758" target="_blank">📅 11:35 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71757">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8cdb06a1cb.mp4?token=LLfMCfv4xCJyShHvF9f_Fv_xxfz9nWF8P6mAXHLXvyRAvd89Y1w68hU4B5B4snhPbXsbcjyduC7bfqAOG4YFbctJcW-exakHJQiPDYPLu5CoDWzjNRFyNxlPQ7gZY5V1iFXD8Wm6wVWYVD-OidGjmfQsH5icLHC2XUcWAPfPRFnqqHVQjmjWkDHKR5JMhFOddj7YyWPzYTpbBhB1UD7qRm4-0dEgOo8BMWjQajco4eaCtQ2V3RBmNLzfykjSfj-ayHVo1H6DasOVLTeYXV-4xUpqO-KjlqnIvCZEvwt65k5XFrRv7IYclPOqXX7IWL1Do9zSY2zgp4RfuPcRlr_Rkw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8cdb06a1cb.mp4?token=LLfMCfv4xCJyShHvF9f_Fv_xxfz9nWF8P6mAXHLXvyRAvd89Y1w68hU4B5B4snhPbXsbcjyduC7bfqAOG4YFbctJcW-exakHJQiPDYPLu5CoDWzjNRFyNxlPQ7gZY5V1iFXD8Wm6wVWYVD-OidGjmfQsH5icLHC2XUcWAPfPRFnqqHVQjmjWkDHKR5JMhFOddj7YyWPzYTpbBhB1UD7qRm4-0dEgOo8BMWjQajco4eaCtQ2V3RBmNLzfykjSfj-ayHVo1H6DasOVLTeYXV-4xUpqO-KjlqnIvCZEvwt65k5XFrRv7IYclPOqXX7IWL1Do9zSY2zgp4RfuPcRlr_Rkw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تفریحات سالم در تیمارستان یمن
@News_Hut</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/news_hut/71757" target="_blank">📅 11:04 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71756">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/69f5632d9a.mp4?token=ejGz2jQJ3c1_6Q4mYIilEPWp3PSWHGU1MHREoYCqKcWe91x4fSikErPodnwYUaWn2c4HNulIIMwS8LfmuektTAXV1ALhaLrF7aXyfgzvkcoL4hfc_lCmiLK25Dlxvnm-ZySd5cvuvnCCsN9G-Rh6QwjLCNyyhYzvE0N583O5dDFoki--eEY__YBFZ-U-1tSgCiY4816GtnujqFr0Ng1qiivdX6h2ZgZCCfL4xBSRBD_P1NzySVnDg1osd_gBcWTGD5DtNgjGtklcxbJeF18JMmTnUpHwz9Y0019KOfsoNsWu07xAFUWLnIrj4Dwi2S-P3A2_3d2PZNhV1vTyRb5buw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/69f5632d9a.mp4?token=ejGz2jQJ3c1_6Q4mYIilEPWp3PSWHGU1MHREoYCqKcWe91x4fSikErPodnwYUaWn2c4HNulIIMwS8LfmuektTAXV1ALhaLrF7aXyfgzvkcoL4hfc_lCmiLK25Dlxvnm-ZySd5cvuvnCCsN9G-Rh6QwjLCNyyhYzvE0N583O5dDFoki--eEY__YBFZ-U-1tSgCiY4816GtnujqFr0Ng1qiivdX6h2ZgZCCfL4xBSRBD_P1NzySVnDg1osd_gBcWTGD5DtNgjGtklcxbJeF18JMmTnUpHwz9Y0019KOfsoNsWu07xAFUWLnIrj4Dwi2S-P3A2_3d2PZNhV1vTyRb5buw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره ایران:
قیمت بنزین برای شما بالاتر رفته است؛ اما این بهایی بسیار ناچیز در قبال کاری است که ما انجام داده‌ایم. این را به خاطر داشته باشید.
ایران نمی‌تواند به این وضعیت ادامه دهد. کشورشان ویران شده است.
ببینید چه اتفاقی برای ایران خواهد افتاد. نتیجه‌ای واقعاً خوب در کار خواهد بود.
@News_Hut</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/news_hut/71756" target="_blank">📅 10:27 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71755">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">اکسیوس:
انتظار می‌رود ترامپ هفته آینده در حاشیه مجمع عمومی سازمان ملل در نیویورک با رهبران کشورهای حوزه خلیج فارس دیدار و درباره جنگ با ایران و برنامه‌های مربوط به دوران پس از آن گفتگو کند.
پیش‌بینی می‌شود که در این نشست مقاماتی از عربستان سعودی، امارات متحده عربی، قطر، بحرین، کویت و عمان حضور داشته باشند.
﻿
@News_Hut</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/71755" target="_blank">📅 10:22 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71753">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jE0v7n1GdwyKMtjCscUtw3cPm0nHK05jA0RgKMt8FQOqOKNoafHLHezA8HACBdJVGYuVSGbpNprplIlwN13b9jOactvLYq-nyNtvd2vU7KsbpIEqgPYlwYEyPsFRzAC8Gmu2ibKYW5mMoDrQG7mI_6dH9GaZnDIDkn-YqdwLPhkCSvm1uLGPQylWg1HWgVUEAle0bDgWvxZy-Ydytqh7J_Fmn4LHnWMxD8evUQiXzbUuxuDshVYF4iOtip69odBEZrhjGQBOggfOFwox3ANorKj7MYKy46oez_U5XNkFPcIwX4C4bNi51vZDKqRAbB7POgpWlqA1QRaVPJ17zVCK8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5cba858231.mp4?token=DBXTOoRiQ_qDJXjNjpLwd2BNtTsA97QRM0hfUMl8hw1HUHv3HAnhrluzR01HSyahMaUBvtJQpjMgWLyx_nMDcGvFlxix7Rsu-LBZ30LuL7d9YimnzRtlp1M9GJ1zv2LnUPLI-5YIzF7AxwN_QhvZHAXTnEMjdQcg1Uw0FPfRl1qar_cQUkFXVn8NiRgZdPoCOGknB-Vs54HDwYoPuCaZ4--x9Gl7_jwWCHfMhK0o7mtID_3qcbpIB4l1xoO8wP553wvmUanEjPh2_EsQxLu8bQn7faShdFsBWxMAjxZOcCPSgE50s2knnG8QcXXzl98jVkVubToTdzN4dYRekqL7DYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5cba858231.mp4?token=DBXTOoRiQ_qDJXjNjpLwd2BNtTsA97QRM0hfUMl8hw1HUHv3HAnhrluzR01HSyahMaUBvtJQpjMgWLyx_nMDcGvFlxix7Rsu-LBZ30LuL7d9YimnzRtlp1M9GJ1zv2LnUPLI-5YIzF7AxwN_QhvZHAXTnEMjdQcg1Uw0FPfRl1qar_cQUkFXVn8NiRgZdPoCOGknB-Vs54HDwYoPuCaZ4--x9Gl7_jwWCHfMhK0o7mtID_3qcbpIB4l1xoO8wP553wvmUanEjPh2_EsQxLu8bQn7faShdFsBWxMAjxZOcCPSgE50s2knnG8QcXXzl98jVkVubToTdzN4dYRekqL7DYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">« امیر نوری » بازیگر؛ چند روز قبل یه مصاحبه کرد گفت خیلی پولدارم و فقط میخورم و میخوابم و از زندگی لذت میبرم. حالا دو روز قبل چنان تصادفی کرده که با سطح هوشیاری پایین باید سریعا جراحی بشه.
@News_Hut</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/71753" target="_blank">📅 10:03 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71752">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CPEjWuOQAXcp1epas8m1ORynCsGapyjV6G0G7Cn5U3Tl_B8zORdfjbpS_3BsByoEtNTGr8m3fgBOWQ1pnrGROF0ULPCesv9THtxQgnI81fhlDGIpz7rnTkFdiOZPB0-E8YDD_8zx2qyb4UDSFAtZt2Ir5n6oAJ-zEw9Os2C5txYifN3gymkg4cLUfNxw8FhxA4qFxFJLyz6Hl6_Z54oOfJoUXGUHuFi77PC9cZB1ZOrqQO5KZTFKzRGHBjBqNVy34xpKCRKW1ig8oEggTy6lBtQJd4frmCeOIGnez2J5I5W_t8yHHobohjXuah5e9kbGmZ4C4IgenGzs9fjQSEh3pA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتش آمریکا بعد رزمایش جانفدا ها توی شهرری عقب نشینی رسمی خود رو از خاورمیانه اعلام کرد
اونی که اسلحه اسنایپر رو برعکس گرفته فقط
😂
@News_Hut</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/71752" target="_blank">📅 09:32 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71751">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3e567a1f2d.mp4?token=VKMEUZepv3qnbqlfsaqHpDj_RnkGrBoCvOSmFxVg-S9xfqWzMNy4UMK9qWPWrmW9or83wfOHh6qylJsfiJcQEZeiiudmx_Gvbnn66NUTdG4UmSWf-EeW1gZMcUElwUKTGr5zP6wvJUkvnaVgjW-B1ZGeG_DDS3dlG50pWlLYaI69fvp5SnkjGczlu7pHfsy6sE5fAoQNhLq2KjfrmZevVl342F2smwQ1lZEGmDCwPi9WTD4iQsRN2zJNJ2YFsmhk9mdo8V-qZXwzlmW1xd1hZhOm2kDBBRngp1rdHJvkq5IZtwgF0GVc7F7zjYP9TxaWn_hJOPccZE_EafcXvdltsg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3e567a1f2d.mp4?token=VKMEUZepv3qnbqlfsaqHpDj_RnkGrBoCvOSmFxVg-S9xfqWzMNy4UMK9qWPWrmW9or83wfOHh6qylJsfiJcQEZeiiudmx_Gvbnn66NUTdG4UmSWf-EeW1gZMcUElwUKTGr5zP6wvJUkvnaVgjW-B1ZGeG_DDS3dlG50pWlLYaI69fvp5SnkjGczlu7pHfsy6sE5fAoQNhLq2KjfrmZevVl342F2smwQ1lZEGmDCwPi9WTD4iQsRN2zJNJ2YFsmhk9mdo8V-qZXwzlmW1xd1hZhOm2kDBBRngp1rdHJvkq5IZtwgF0GVc7F7zjYP9TxaWn_hJOPccZE_EafcXvdltsg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نتانیاهو در میان مردم اسرائیل با استقبالی باشکوه
@News_Hut</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/71751" target="_blank">📅 09:02 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71750">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/65c03c4e5b.mp4?token=FRVqMNpkmm84wL8hFMXyQDn8vhJRNfIDqEaLnSitBbqa_eTNMbSboiTcw6A5LBJlca2HHuU7O9jdMgrGEz_TXAhdAj9GZzP5Yz8pOoX9mjxCk2S_Gz23BPOnbnfoiu1OF5Ub9yb9VerlgxbemIsTwO1jN4f66QVypyeIn2UOxtatriu_UpYoVloYz8JDnzmWeFSvCtKHoSZnE29g0dyO6HnC5N-lZMZ65fYPpkCejC5JaosoOjZxmUrx80tgfmz2q9Nvw_vGqzE4Ad_azF28Pz2jgKgVjl1xdqEKZR4Bj71Rt12_NtXd2jK4wF-ZnC2NUsfhnvpzHzkgD2eVu46AXA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/65c03c4e5b.mp4?token=FRVqMNpkmm84wL8hFMXyQDn8vhJRNfIDqEaLnSitBbqa_eTNMbSboiTcw6A5LBJlca2HHuU7O9jdMgrGEz_TXAhdAj9GZzP5Yz8pOoX9mjxCk2S_Gz23BPOnbnfoiu1OF5Ub9yb9VerlgxbemIsTwO1jN4f66QVypyeIn2UOxtatriu_UpYoVloYz8JDnzmWeFSvCtKHoSZnE29g0dyO6HnC5N-lZMZ65fYPpkCejC5JaosoOjZxmUrx80tgfmz2q9Nvw_vGqzE4Ad_azF28Pz2jgKgVjl1xdqEKZR4Bj71Rt12_NtXd2jK4wF-ZnC2NUsfhnvpzHzkgD2eVu46AXA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرنگار: آیا قبول دارید که آن‌ها به خاطر جنگ در ایران، نرخ‌ها را بالا می‌برند تا قیمت‌ها را پایین بیاورند؟
ترامپ: نه، آن‌ها نرخ‌ها را بالا می‌برند تا عملکرد ترامپ تا حد ممکن بد به نظر برسد. مشکل آن‌ها این است که ما بهترین اقتصاد تاریخ را داریم.
@News_Hut</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/71750" target="_blank">📅 07:25 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71749">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5ad35ceb68.mp4?token=X2xC71rVYZ4vfWiXkaV_mT_btznWENyebxo9Vp12NbYaxPtFKK1zohJnqEx7bRn3zPG9T9bpI8nj45M4KEYEYqW2zedHin_QBavmckOflF-yaLYfg5h6ZF1w6Suny4tMNBcqxQweZ9TRGPe-HmU4uMYzx_FWVt6fiAEzs8YOAPZ3tLAyvcmgV-A1etguDIaGZTzD0PTe-P8FLd9mfYYpoF7PEcHaerXqeRRldrl-oHaUaFX8I-Hk4hx0efK5tgYj9NDsemzSo9j-5P8d9eAAOdwfEiHLaAs-8gWwfewawGoBV-FjnYIyvU_JO1CQtlMJ9Hajb-UMX4ngDQH5vrItzA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5ad35ceb68.mp4?token=X2xC71rVYZ4vfWiXkaV_mT_btznWENyebxo9Vp12NbYaxPtFKK1zohJnqEx7bRn3zPG9T9bpI8nj45M4KEYEYqW2zedHin_QBavmckOflF-yaLYfg5h6ZF1w6Suny4tMNBcqxQweZ9TRGPe-HmU4uMYzx_FWVt6fiAEzs8YOAPZ3tLAyvcmgV-A1etguDIaGZTzD0PTe-P8FLd9mfYYpoF7PEcHaerXqeRRldrl-oHaUaFX8I-Hk4hx0efK5tgYj9NDsemzSo9j-5P8d9eAAOdwfEiHLaAs-8gWwfewawGoBV-FjnYIyvU_JO1CQtlMJ9Hajb-UMX4ngDQH5vrItzA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ: امیدواریم که به پایان ماجرای جنگ با ایران نزدیک شده باشیم. ایران خواهان دستیابی به توافق است.
خبرنگار: آیا مستقیماً از آن‌ها خبری دریافت کرده‌اید؟
ترامپ: بله.
@News_Hut</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/71749" target="_blank">📅 07:15 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71748">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">😶
🚨
🚨
این کانال باعث ورشکستگی خیلی از سایتای بت شده و پلیس FBI برای دستگیری ادمینای این چنل جایزه تعیین کرده
🔥
https://t.me/+bDapVmvigDhmYzZk https://t.me/+bDapVmvigDhmYzZk</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/71748" target="_blank">📅 01:37 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71747">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/tZadx1M8NcG3-t2wxpiGmy84bej7kbsQkcEc_ZZUjVKRu6E5eVo7uUvJyOduIJMMi1tfjTCazlShDybdUYXe2O8ScHAMjHpI2JXtLZjSxnVxzlZ-8ipAPKyI9w1oRPLq5LdnLPJiv2j8c3E1sfaexbFi4bV1KYIDPUx_FIAPpsESBlFjZISD7EbEFswaFmbItVCwZrR6GCZ-kIwKbuqYS0Zz-yAlnhOKx7z4Zk7UTUMaKIm3jNHEbjMuIav09WwVgXgv47DD9ukzrbYFX0vy5m8YqEQHn1Ux8h8_J64_r9ibKkRk5ghgaVIBjyADPzXZHnUE5lsLcYzHWhnBZQTZVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😶
🚨
🚨
این کانال باعث ورشکستگی خیلی از سایتای بت شده و پلیس FBI برای دستگیری ادمینای این چنل جایزه تعیین کرده
🔥
https://t.me/+bDapVmvigDhmYzZk
https://t.me/+bDapVmvigDhmYzZk</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/71747" target="_blank">📅 01:37 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71746">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cef2cf6cff.mp4?token=D8onb0BsX7f1HSobc_UP5G6I0WPSNRKjBBbwfeGF5t0Qv7V0y-AbBBvCPsSSAlH7Cxv1lsTYW3FI93fo8jzn1HWs88MDTcyNRbIIi22UTwfEOkggSCfO0Je9vcfAgabIJbGCs_wLTaUUUwZJWrAkoch5uGPVZD_Sbp-mVxDvw5_e2KRZCcnfVu8NAQZsYuW-Snt5DONlvTGI_Rfr9XI6cBhmsU6V1snq7ty6MYwT0S7aepsdxk5eOxX6c6sLrH33EI9Ns2naHY7uBUZY7yJG9Y8c5aimgYHaDxU8hAjc_nVgPKUruR5NGPBphAoOtPXY3l3GDttG8efekYWuFCnbfw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cef2cf6cff.mp4?token=D8onb0BsX7f1HSobc_UP5G6I0WPSNRKjBBbwfeGF5t0Qv7V0y-AbBBvCPsSSAlH7Cxv1lsTYW3FI93fo8jzn1HWs88MDTcyNRbIIi22UTwfEOkggSCfO0Je9vcfAgabIJbGCs_wLTaUUUwZJWrAkoch5uGPVZD_Sbp-mVxDvw5_e2KRZCcnfVu8NAQZsYuW-Snt5DONlvTGI_Rfr9XI6cBhmsU6V1snq7ty6MYwT0S7aepsdxk5eOxX6c6sLrH33EI9Ns2naHY7uBUZY7yJG9Y8c5aimgYHaDxU8hAjc_nVgPKUruR5NGPBphAoOtPXY3l3GDttG8efekYWuFCnbfw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مواضع حوثی‌ها و تجهیزات نظامی آنها بار دیگر در مناطق خط مقدم شمالی استان تعز و اطراف المخا هدف حملات قرار گرفت.
@News_Hut</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/71746" target="_blank">📅 01:07 · 26 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
