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
<img src="https://cdn4.telesco.pe/file/N1ksmM6v4ExDRe4-5KDQv2cmX_3UwduZK601kx-mACInKHXSs_teYpIo6VKQ5JlF0kxSyuk0Qfr7DXdXSohCgxaolsoIRpPSIsSrco8L--Xk3V8G-2DSc-FyJTuFec6u5CN7DDHNM1eZnga0mGlQ1Nnupi9_GLHDEBOaMMaG25aJmKHMio-UGGvLwjqJe3c_l_en1n8MD0DWN3XJkgGJqmaAgs38Zg5FHYfxKhEEWgrLQcIT59wDDgs7XEdNSnfWobuwMXvbRtWtnOyFe11UbVd_7002cRwZuF8qqR-ANKOecY3c-qvSItV-4p9HdrwPD9D5uNcWwyvhetyjmQB2_A.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 130K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-18 14:29:34</div>
<hr>

<div class="tg-post" id="msg-69786">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🚨
🇮🇷
🇮🇷
ادعای فارس:رئیس‌جمهور با رهبر معظم انقلاب دربارهٔ مسائل اقتصادی و نظامی کشور دیدار و گفت‌وگو کرد.
پزشکیان همزمان با شروع سومین سال ریاست‌جمهوری با حضرت آیت‌الله سیدمجتبی حسینی خامنه‌ای دیدار و گفت‌وگو کرد.
در این دیدار به‌تفصیل دربارهٔ مسائل و مشکلات کشور به‌ویژه تأمین نیازهای معیشتی مردم، شرایط موجود جنگ تحمیلی سوم و آیندهٔ پیش‌رو، تحولات حوزهٔ نظامی، راهکارهای ناظر به تأمین منابع و مدیریت مصارف «ریالی، ارزی و انرژی» و همچنین تعامل اقتصادی با طرف‌های خارجی تبادل نظر شد.
@News_Hut</div>
<div class="tg-footer">👁️ 2.02K · <a href="https://t.me/news_hut/69786" target="_blank">📅 14:23 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69785">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">‼️
صحبتای این خانم در مورد کافه رفتن و پیدا کردن پسرای پولدار، خیلی وایرال و جنجالی شده.
@News_Hut</div>
<div class="tg-footer">👁️ 4.88K · <a href="https://t.me/news_hut/69785" target="_blank">📅 14:01 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69784">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8ab9ff0322.mp4?token=pFgH-0RojWgOdYgDWhcYfnX-PSRdhJPoCylYnhn_TnXtZIFmLKNze_ZyfyRTAkyF-GEuPIY3mjoMbafoftBQBUzLV2iZKkcQSbdECnulswpUyaEWEkyQAzPu1q8ZVnIaowpW9m9fKkku2GCIMlWLNmTwt23eqzO7HKYeyaTkoFxIxctGaSO9l-SKWAprFqKluJcEjDCOADhZQ4TMyIuZJpxtHlIOWPJ-PUl2nJVGbFc4DfbEecZbevCd2R2y8r0F7YSRARJfur3D-fhIzjQgtrXrFTUwpZGQSF6JLsjJUhOYUu7DiyckXDerctehSfTAfozC7U-QBmQ2rA5PRqgMUxabWCzRcraRvOESo9xI5oCgMX5Gbt4lvFCRImNTueZUjRHmMRmA6DPJxG-eoV5ly_ir4G9qCw9Hddd7QDSdzqoT1RnkNObY9XpGCZQdrYGyl4WoX4aNNQWmuHEGeA8tteP89k53ysyzDfqThcza751LIPaXK6uV0rM7HXt-MGStibo31VmCQBYuNQccWoUsWi_gp-Bqf-HyXlm710qRgm5XsQVka70EBVpR-gq5dwBi30oS8qdrXlPqtkP6Tm3Rtx1TTJz1cl8wGvgkrT26tlaMdc9GI-HK_AVMYtJyXxInSZQoDRg2EztKSGJuhbkFX3SnHcC1_6ExQlZHWeucQKw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8ab9ff0322.mp4?token=pFgH-0RojWgOdYgDWhcYfnX-PSRdhJPoCylYnhn_TnXtZIFmLKNze_ZyfyRTAkyF-GEuPIY3mjoMbafoftBQBUzLV2iZKkcQSbdECnulswpUyaEWEkyQAzPu1q8ZVnIaowpW9m9fKkku2GCIMlWLNmTwt23eqzO7HKYeyaTkoFxIxctGaSO9l-SKWAprFqKluJcEjDCOADhZQ4TMyIuZJpxtHlIOWPJ-PUl2nJVGbFc4DfbEecZbevCd2R2y8r0F7YSRARJfur3D-fhIzjQgtrXrFTUwpZGQSF6JLsjJUhOYUu7DiyckXDerctehSfTAfozC7U-QBmQ2rA5PRqgMUxabWCzRcraRvOESo9xI5oCgMX5Gbt4lvFCRImNTueZUjRHmMRmA6DPJxG-eoV5ly_ir4G9qCw9Hddd7QDSdzqoT1RnkNObY9XpGCZQdrYGyl4WoX4aNNQWmuHEGeA8tteP89k53ysyzDfqThcza751LIPaXK6uV0rM7HXt-MGStibo31VmCQBYuNQccWoUsWi_gp-Bqf-HyXlm710qRgm5XsQVka70EBVpR-gq5dwBi30oS8qdrXlPqtkP6Tm3Rtx1TTJz1cl8wGvgkrT26tlaMdc9GI-HK_AVMYtJyXxInSZQoDRg2EztKSGJuhbkFX3SnHcC1_6ExQlZHWeucQKw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇷
عباس عراقچی:
اکنون هیچ مذاکره ای با آمریکا نداریم و نخواهیم داشت
شروع مذاکرات بدون پایبندی آمریکا به شروط تفاهم‌نامه غیرممکنه
ملت ما تسلیم اراده یک عده خاص نمیشه
بدون تحقق حق ملت ایران کوتاه نخواهیم آمد
@News_Hut</div>
<div class="tg-footer">👁️ 8.62K · <a href="https://t.me/news_hut/69784" target="_blank">📅 13:15 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69783">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/34556823e0.mp4?token=h8lkU1WeHB_RoyDFGx2UDDr0VEX6g3PxPxUUfH9eJtlGGQi4ywSn5sWJL0DzWm8FYau5d0oq8tj5DKlPFZzT_7WWLAdRYXi1MGJmAbN1HUnI0xRCqoefd7Z_zaeQrxUzbhImnvyFACeVrSBjN5n24nTkBDp9w-uI336BWKefOl7nZGB8BPCYvPn8POK9QJ4yLRJzC_KY3gW7OsXCzD7o9mO-UKBx4c7jcrSribVawOFXmF-Qw2OtodVZubbrP-lmOT5QbnvZDEjhcx6Iq0Sp81f31WNuTQ571_qaHhRWrQv85fdIenXpDw-Ezz-D1590ZGX1TC7tuxT5f6RraR-ZMg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/34556823e0.mp4?token=h8lkU1WeHB_RoyDFGx2UDDr0VEX6g3PxPxUUfH9eJtlGGQi4ywSn5sWJL0DzWm8FYau5d0oq8tj5DKlPFZzT_7WWLAdRYXi1MGJmAbN1HUnI0xRCqoefd7Z_zaeQrxUzbhImnvyFACeVrSBjN5n24nTkBDp9w-uI336BWKefOl7nZGB8BPCYvPn8POK9QJ4yLRJzC_KY3gW7OsXCzD7o9mO-UKBx4c7jcrSribVawOFXmF-Qw2OtodVZubbrP-lmOT5QbnvZDEjhcx6Iq0Sp81f31WNuTQ571_qaHhRWrQv85fdIenXpDw-Ezz-D1590ZGX1TC7tuxT5f6RraR-ZMg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
این ویدیو رو ببینید تا متوجه بشید با قیمت الانِ یک نوشابه، تو سال ۹۵ می‌شد چه چیزایی خرید...
@News_Hut</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/news_hut/69783" target="_blank">📅 12:30 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69779">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MO2qIZTXAnq9I5ODez8gqY6hdvdnGrWl_YexxC2q1gcXGZdrvtF_dErU9AGc50OOHD-ATD4lSzujsAb76ubRvuLMeRAbL-KlDYdADlunc0VfX7zKPr4_AuvvchygC5A_WGCYKkzWBjoQdoRCIB1HviRLtd2V_5fv5YSzgUzWqupBnn23ZGiPQWOqQKRBQVuodWex5aE4YNxXC9Bzm1ExeVFGr41S-4UNP6lWkHNarsfgkbkzFrSYUwbC5Bw4evBeX-BQVx6mHyHnlQxhOwcixxhyve89NBHCKHkntJFviL6PE2g2wGRJgpvTwc3rfWWeG6PEALzGuKxfnOESHXhUoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6e5f1aeb56.mp4?token=i30fPSl_8WKe21Uh_mN2kGv7O_P44xYAp6YEdsSOADZDi1CfErpmJMfCNe7bmDl-ZRvFHLAGTI3-gCWVhhT_zOzFRUXOSWaUErjMVivs7CBe6ey_E8wo_7PMQIwJXUPKxJvXUGUGQPIj75O0aztRnjKdK2dChP5SG8Jr5sZ8jgOfHbIdwV0jKueFrz-RbbFpPiyiJYDB0F0ZJ9Bo8b06b64ePkr9DhF-3mNnxganKO9gkTKWHWdLS09AhGnvMiDrh5zEquvQ418MEx65yiaLysL1_sHBMCfU07E4CoKt-DeWKh58RISxlwGGwB64wyA-4mTjlXbs4s8qzpDAzQxItg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6e5f1aeb56.mp4?token=i30fPSl_8WKe21Uh_mN2kGv7O_P44xYAp6YEdsSOADZDi1CfErpmJMfCNe7bmDl-ZRvFHLAGTI3-gCWVhhT_zOzFRUXOSWaUErjMVivs7CBe6ey_E8wo_7PMQIwJXUPKxJvXUGUGQPIj75O0aztRnjKdK2dChP5SG8Jr5sZ8jgOfHbIdwV0jKueFrz-RbbFpPiyiJYDB0F0ZJ9Bo8b06b64ePkr9DhF-3mNnxganKO9gkTKWHWdLS09AhGnvMiDrh5zEquvQ418MEx65yiaLysL1_sHBMCfU07E4CoKt-DeWKh58RISxlwGGwB64wyA-4mTjlXbs4s8qzpDAzQxItg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
حمله پهپادی اوکراین به بلگورود
نیروهای اوکراینی شب گذشته حمله گسترده‌ای پهپادی به شهر بلگورود روسیه انجام دادند که در پی آن چندین ساختمان مسکونی هدف قرار گرفت.
@News_Hut</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/news_hut/69779" target="_blank">📅 12:30 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69778">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">melbet.apk</div>
  <div class="tg-doc-extra">53.8 MB</div>
</div>
<a href="https://t.me/news_hut/69778" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🇩🇪
آپ اندروید سایت جهانی Melbet
💥
🎁
بونوس ورزشی هر چهارشنبه
🔥
💸
واریز و برداشت متنوع
💵
⭕️
بدون نیاز به فیلتر شکن
⭕️
r18
🎁
کد هدیه ثبت نام Melbet90
✌️
✔
https://t.me/+x60dZGAgXTUxM2U0</div>
<div class="tg-footer">👁️ 8.35K · <a href="https://t.me/news_hut/69778" target="_blank">📅 12:29 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69777">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G-mv3jKK5Ihi_OSM90Q4Kg4aHWWZHNlh8hn9lbOtzsrEH-KjSgGdvqyLcgjCKTdHs8mN9QjPrdFT4h9hUfpTvAbCnnmkswQP3waJ7ZoiwNSCNNrMIemPg8CSc7c_s5aVCzgT0WvC5oyu5BWa6eyck6VoyR0xgdaW4X1WmUR-Xq8xe_B5er33v3oDrCxqmlg7A_mD725TEwmC1ZUIdk1B3sl8-xepfcowOHYuYm2aTSiUiN3UlycP3X-5yvucic18a2lI4HOqbDR1CwodIwGS95aAFYirM82QZ8uPw9HZSMpLmHafZUWJaNCgZqp2pDs9MCrf7Zx-TEw-pjK8cmrWvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
دنبال سایت معتبر برای شرطبندی می‌گردید
⁉️
🎲
سایت بین المللی و معتبر Melbet
👍
😁
😊
🙂
🥇
واریز و برداشت ارزی و ریالی
‼️
🔥
بونوس 100% اولین واریز
‼️
⚽️
بونوس ورزشی هرچهارشنبه
‼️
🆗
کازینو و انفجار با ضرایب جهانی
‼️
🎁
کد هدیه ثبت نام :Melbet90
🇩🇪
دانلود اپلیکیشن MELBET
👉
🔗
لینک وبسایت
👉
⭕️
جهت استفاده از vpn از IP های آسیایی یا کانادا استفاده کنید.
🇨🇦
🇹🇷
r18
✔
https://t.me/+x60dZGAgXTUxM2U0</div>
<div class="tg-footer">👁️ 8.17K · <a href="https://t.me/news_hut/69777" target="_blank">📅 12:29 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69775">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7c93de8243.mp4?token=SOQWS1s2psMDE6FdUR-igl8RdRf0h4BiCMILCx_4Su1z3GKyPTekOyGK1taKnCu4w2bRo1DJOttFuxbjkyLCRPmbCnImJJZl01_lqVlbfltCwYVGJErETW9rWvC7qs0XldsqiHuYRMqvpjxkNDdjdECAOooV6UwqR1lhDdJKFlu9IHhzYaja4OXNy2SOOPGYKz8j9WRRXk0ZhRKwuVBztr9OZWNo1OZp7htgr_EwOFEbCEwMPJtDzVvy20MA6b-jTOoba0bb0jXPk_YDU6bfIJgL0mzX4vjI87HSRBP1J7sbTLWgJhrwj-_SiHaBxfGjssSK0KjU3QlfHiFOrt5PkQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7c93de8243.mp4?token=SOQWS1s2psMDE6FdUR-igl8RdRf0h4BiCMILCx_4Su1z3GKyPTekOyGK1taKnCu4w2bRo1DJOttFuxbjkyLCRPmbCnImJJZl01_lqVlbfltCwYVGJErETW9rWvC7qs0XldsqiHuYRMqvpjxkNDdjdECAOooV6UwqR1lhDdJKFlu9IHhzYaja4OXNy2SOOPGYKz8j9WRRXk0ZhRKwuVBztr9OZWNo1OZp7htgr_EwOFEbCEwMPJtDzVvy20MA6b-jTOoba0bb0jXPk_YDU6bfIJgL0mzX4vjI87HSRBP1J7sbTLWgJhrwj-_SiHaBxfGjssSK0KjU3QlfHiFOrt5PkQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚠️
⚡️
تصاویر جالب از لحظه برخورد رعد و برق به ساختمان مرکز تجارت جهانی «اسپیرز» در نیویورک؛
@News_Hut</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/news_hut/69775" target="_blank">📅 12:04 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69774">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6b13fec044.mp4?token=JTvjMj8qR6pGPzpLHnRbRLAAwY1YF7p_e_Y_LHSgataSzkPrgsZg76cD0CVoOMT_HGXZ7UOqaLBMXXBkx5lfcBuF76dQOCkpjrak6aEHcQC0RqV7nMJdUNYz8IXGK5oC2h3y1BVfh0OUghf9b-E8KcFHOpCMvcRmVANwRoibW6XXtHhjmiD1M074Ui6USd1wJj17OSyliBhZY_A9P-ci1_fW7bqZ1KmM5DeoHGnnjTeMo1jlC21x86oydnVGdX-7bBXDPn97zduNV9sSUjbQTLHfxV8cSMv2H71g_G5UfsaSAgo8lg4oYVecejqEW8XSRSV4p7nq1VwUtbT1x9ZvIw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6b13fec044.mp4?token=JTvjMj8qR6pGPzpLHnRbRLAAwY1YF7p_e_Y_LHSgataSzkPrgsZg76cD0CVoOMT_HGXZ7UOqaLBMXXBkx5lfcBuF76dQOCkpjrak6aEHcQC0RqV7nMJdUNYz8IXGK5oC2h3y1BVfh0OUghf9b-E8KcFHOpCMvcRmVANwRoibW6XXtHhjmiD1M074Ui6USd1wJj17OSyliBhZY_A9P-ci1_fW7bqZ1KmM5DeoHGnnjTeMo1jlC21x86oydnVGdX-7bBXDPn97zduNV9sSUjbQTLHfxV8cSMv2H71g_G5UfsaSAgo8lg4oYVecejqEW8XSRSV4p7nq1VwUtbT1x9ZvIw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
گوشه‌ای از سخنان وایرال شده خرازی، برادرزن مسعود خامنه‌ای:
جمهوری اسلامی یه موشکی به اسم «رستاخیز» داره که میتونه یه دور کامل دور زمین بچرخه و به راحتی خاک آمریکا رو بزنه.
@News_Hut</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/news_hut/69774" target="_blank">📅 11:32 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69773">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0189fef147.mp4?token=ss03E-5sTzdAXx_VwERyBdXa-w6lJNYxUKExmsCub_kdXIC4yYBsDOgz84ukLh7-7tWwHwKAYps4bsXwThgSF3nINk7nqyLsEDNqnc0s6CaXFSAnXB-GU6XLE5ZHRvlDpLAs6_nCKS9w0AbmXEbvKgv9iAshqMLEQZzyyyuYnWii4vtn7C0-SdPXByLEzprdVNPg0LoZyqcB3yXJTQj8W9tsLTj_YIfC-5L0qm7ILtZdF6SsbI3kNf0mL6MTNtYmLGGi2uzbgW1nwPevS1NiRXQvKy8VnX8eEI1qtaW4s2QOrw39XGYdctfI1z053fvL-7vEypqzEnpxDz0txhkE2kXJQbcUbRF8RQa83LG1xUOquBX4diDn8YWdEX3nx9fB0TNSb9WX7Q8x5S9YGvGlgj-vxI00fTerQIkSN6v7kTJYb7Lg65iPLkzpU681LXcMwQCsQTl_OaJ7qxS0Hd6UzBfxRhD94sVsuPmcHq-_aeIuf2auL1seGRqWcm1pMIpAfVzbnnU1jyzuuAn2C-qocdPfwqM9uO6PG7gfCI930Lm-tcwlpBZykitoieE5iJd0_zGB3S22vgzn2ImwV5LKcUHn16zmEiFq5r17lkOeBvqzU8DvtdHigL9McEn-1Pei4pGPXT2bnJk7At2_TWxsMDzS673mC_1xEvMQMVHSENE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0189fef147.mp4?token=ss03E-5sTzdAXx_VwERyBdXa-w6lJNYxUKExmsCub_kdXIC4yYBsDOgz84ukLh7-7tWwHwKAYps4bsXwThgSF3nINk7nqyLsEDNqnc0s6CaXFSAnXB-GU6XLE5ZHRvlDpLAs6_nCKS9w0AbmXEbvKgv9iAshqMLEQZzyyyuYnWii4vtn7C0-SdPXByLEzprdVNPg0LoZyqcB3yXJTQj8W9tsLTj_YIfC-5L0qm7ILtZdF6SsbI3kNf0mL6MTNtYmLGGi2uzbgW1nwPevS1NiRXQvKy8VnX8eEI1qtaW4s2QOrw39XGYdctfI1z053fvL-7vEypqzEnpxDz0txhkE2kXJQbcUbRF8RQa83LG1xUOquBX4diDn8YWdEX3nx9fB0TNSb9WX7Q8x5S9YGvGlgj-vxI00fTerQIkSN6v7kTJYb7Lg65iPLkzpU681LXcMwQCsQTl_OaJ7qxS0Hd6UzBfxRhD94sVsuPmcHq-_aeIuf2auL1seGRqWcm1pMIpAfVzbnnU1jyzuuAn2C-qocdPfwqM9uO6PG7gfCI930Lm-tcwlpBZykitoieE5iJd0_zGB3S22vgzn2ImwV5LKcUHn16zmEiFq5r17lkOeBvqzU8DvtdHigL9McEn-1Pei4pGPXT2bnJk7At2_TWxsMDzS673mC_1xEvMQMVHSENE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
بابای این دختره چون دخترش توی امتحان گواهینامه قبول شده براش BMW 225 خریده ناقابل ۱۲ میلیارد.
@News_Hut</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/news_hut/69773" target="_blank">📅 11:04 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69772">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/973161bf95.mp4?token=DRVT49RA9Cweoqk8bjo0xI2cgjBsxw9Hpr8xsx3Tn64u4-5UKS4YtkR3F7tl47wD6fAnyByv-MubhzS8TvipRw0JeyaFXu6vCIQN5dfKizgrkog5TFUwdhOMRUpSzcdQCUxQ2lfOAiARduP0RnHTDq9ahZO3qseqB9aCVhASjyasnZRwWPEhyOMoaTPNJ_QKFA80Lck_A6bb075HcKrhIORNN_AfDs1_YI4dWgsIoqr_Ue0Dfg92J36HLn31rmVl17JqOe6KgwjThytS2P65GSGcqDZ3y7fX3xv_nrs3UwDlRp3-bgG0gyHkVnBhyW2qvzNtQoBv5P9SpnvT6aZMUQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/973161bf95.mp4?token=DRVT49RA9Cweoqk8bjo0xI2cgjBsxw9Hpr8xsx3Tn64u4-5UKS4YtkR3F7tl47wD6fAnyByv-MubhzS8TvipRw0JeyaFXu6vCIQN5dfKizgrkog5TFUwdhOMRUpSzcdQCUxQ2lfOAiARduP0RnHTDq9ahZO3qseqB9aCVhASjyasnZRwWPEhyOMoaTPNJ_QKFA80Lck_A6bb075HcKrhIORNN_AfDs1_YI4dWgsIoqr_Ue0Dfg92J36HLn31rmVl17JqOe6KgwjThytS2P65GSGcqDZ3y7fX3xv_nrs3UwDlRp3-bgG0gyHkVnBhyW2qvzNtQoBv5P9SpnvT6aZMUQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
علی مطهری، نایب‌رئیس پیشین مجلس شورای اسلامی:
از همان ابتدا، هدف ما ساخت بمب‌های هسته‌ای بود و باید تا پایان ادامه می‌دادیم.»
@News_Hut</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/news_hut/69772" target="_blank">📅 10:32 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69768">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/c32fad0f32.mp4?token=pEOBKxOSfd4AwIxb64E2Zl_meK7mHOb63RQIqxHwqmpMWX1lZNb6uamNo_qQ3eDPZDjJ2UX57PIngqxyTjla4AL4L4yaneG03mg9sV2kZJMwFRWHr27bJaqwrdwk5TIquzB4z398kH9m009Li8mgfOSVzpVpBKtAwNDKGbq_yM0DttQRXR85mTBpGfGLaH42FJwgIpe0EMRoMfiCWMmM7DAzph0kjf5l6EcaYkkqo_26hU2mQ3IOWQoXe9BHDdB3CTFKNq7dsI_4Y9KinQrG-Mn1gbazKsh1JQCJpv4U6Lg-gfgi8xVVO4vCM4VDbG75YlHRB4dReo-6-AzNZ61KRw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/c32fad0f32.mp4?token=pEOBKxOSfd4AwIxb64E2Zl_meK7mHOb63RQIqxHwqmpMWX1lZNb6uamNo_qQ3eDPZDjJ2UX57PIngqxyTjla4AL4L4yaneG03mg9sV2kZJMwFRWHr27bJaqwrdwk5TIquzB4z398kH9m009Li8mgfOSVzpVpBKtAwNDKGbq_yM0DttQRXR85mTBpGfGLaH42FJwgIpe0EMRoMfiCWMmM7DAzph0kjf5l6EcaYkkqo_26hU2mQ3IOWQoXe9BHDdB3CTFKNq7dsI_4Y9KinQrG-Mn1gbazKsh1JQCJpv4U6Lg-gfgi8xVVO4vCM4VDbG75YlHRB4dReo-6-AzNZ61KRw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
ایشون به اسم آرش، خودشو اولین:
همجنس‌بازه، شیعه، پادشاهی خواه، دو رگه تُرک و لر معرفی کرده که پشمای همه ریخته
😐
@News_Hut</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/news_hut/69768" target="_blank">📅 10:02 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69767">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c4c02b892b.mp4?token=ebc97Tsag_GvHZGwbkLEkyuODYmAZUxzg4s2QJYV16ZwL0R9zB-mXo6eSIBjp9ZxPY44fQueJrC9ywXMIBrVvijqIHIwhf-CkBDtWlYG2wgMVbEJHv5fLP_s3tAsEC0t0TuK1awmnKYGMnUUS7MQ7eFUMLRtAO8M2QtuDe3OzC2ZNekVEeKnnRCAwmoOV42cfmQGApByn0NBCimBpUBmkgqYVcBw3-_oTtovziygFMdCraIUgZ9TXbVUJvE-tiZCRYd0Fj5J5ssk3Ni6vuqGvK4P9iBv-GosZTkbFLOXSgksp8Lfe9i1z4gJOl2-YpnadvDHNbkSLJ2sdSIBiP3Obg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c4c02b892b.mp4?token=ebc97Tsag_GvHZGwbkLEkyuODYmAZUxzg4s2QJYV16ZwL0R9zB-mXo6eSIBjp9ZxPY44fQueJrC9ywXMIBrVvijqIHIwhf-CkBDtWlYG2wgMVbEJHv5fLP_s3tAsEC0t0TuK1awmnKYGMnUUS7MQ7eFUMLRtAO8M2QtuDe3OzC2ZNekVEeKnnRCAwmoOV42cfmQGApByn0NBCimBpUBmkgqYVcBw3-_oTtovziygFMdCraIUgZ9TXbVUJvE-tiZCRYd0Fj5J5ssk3Ni6vuqGvK4P9iBv-GosZTkbFLOXSgksp8Lfe9i1z4gJOl2-YpnadvDHNbkSLJ2sdSIBiP3Obg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
حرفای یه طرفدار حکومت درباره حجاب:
آقای پزشکیان واقعا مرسی که گفتی نمیتونم قانون حجاب رو رعایت بکنم
مجلسی که ناظر هستی توام دمت گرم که اصلا فکری برا حجاب نمیکنی
پزشکیان داره میگه ععععععع مگه هنوزم گشت ارشاد هست؟؟
بحث دیگه حجاب نیست بحث پوششه پوشش و اصالت ما داره از بین میره
تو خود اروپا هم قانونی برا پوشش هست نه اینکه لخت بریزن خیابون
@News_Hut</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/news_hut/69767" target="_blank">📅 09:31 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69766">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bed36a1671.mp4?token=eqtAXPPEYdkHmdlDkY3XFF71FWNNz4m_8jfO7lFr4QOmvDGakNY_JfaJYllspUv1fVu9fV4PifIbvzN1Zhj5S_ojKM5cC7i2K0MkRS0Ls-PkSPU89fTLJ97-6j4NGWGpXiZqeklP8-tR3h1zxMZXZiGCGhP-sIPFFotMafFTpVKgli-2r3SfsU8P2YFfJdD-oIXpdaW7iUUQegLOuLOhheV5ms2VW42qsc4ngIuFTq8NEjLeSCSzgTFHowWqsYzr0K2Fd4L9XNXGXupetc1H0jXc5F9fqJXKS3MbxEP8qAhtBHgeTcwiF2mgAUxPo6Xwun4MMcXGRhA7X67wo26x2w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bed36a1671.mp4?token=eqtAXPPEYdkHmdlDkY3XFF71FWNNz4m_8jfO7lFr4QOmvDGakNY_JfaJYllspUv1fVu9fV4PifIbvzN1Zhj5S_ojKM5cC7i2K0MkRS0Ls-PkSPU89fTLJ97-6j4NGWGpXiZqeklP8-tR3h1zxMZXZiGCGhP-sIPFFotMafFTpVKgli-2r3SfsU8P2YFfJdD-oIXpdaW7iUUQegLOuLOhheV5ms2VW42qsc4ngIuFTq8NEjLeSCSzgTFHowWqsYzr0K2Fd4L9XNXGXupetc1H0jXc5F9fqJXKS3MbxEP8qAhtBHgeTcwiF2mgAUxPo6Xwun4MMcXGRhA7X67wo26x2w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
ویدیو وایرال شده از فردی که در زمان رفراندوم سال 57 حضور داشته
:
وقتی من روز رفراندوم رفتم بیرون و دیدم گفتن ۲۰ میلیون نفر رای دادن زنگ زدن آدما بهم گفتن بیا ببین چخبره.
اونجا رئیس حوزه آخوند بود و این بیجک های صدتایی رو میدادن دست مردم میگفتن بنداز صندوق بگو مرگ بر شاه.
جمعیت ایران اون زمان ۳۷ میلیون و ۲۰۰ هزار نفر بود.
کل کسانی که بالای ۱۶ سال بودنو و میتونستن رای بدن ۱۸ میلیون و ۷۳۲ هزار نفر بود.
آمار رو با خنده اعلام کردن ۳۰ میلیون نفر رای دادن.
توی وزارت کشور گفتن که اینطور نمیشه پس گفتن ۲۲ میلیون و ۴۰۰ هزار نفر رای دادن و ۲۰ میلیون و ۴۰۰ هزار نفر به جمهوری اسلامی بله گفتن.
اینو حساب کنید دیگه از کل ۱۸ میلیون نفر واجد شرایط مخالف بود مریض بود زندانی بود و.... از اینجا بود که من راهمو از اینا جدا کردم.
@News_Hut</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/news_hut/69766" target="_blank">📅 08:57 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69765">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">app-release.apk</div>
  <div class="tg-doc-extra">4.5 MB</div>
</div>
<a href="https://t.me/news_hut/69765" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🎲
همین امشب با اولین شارژ
🤩
🤩
🤩
درصد شارژ بیشتر بگیر
همین الان شانست رو با موجودی اضافی امتحان کن حتما بزنده میشی
👌
👇🏻
👇🏻
🌐
Telegram
🎲
🌐
winro.io
🎲</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/news_hut/69765" target="_blank">📅 01:46 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69764">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KuAEa6YOP3Du7O8oR54GtqjKzE0qYqMST4LCV7VQPXuyuV3LqIYFsWgnZ_f0tyW0e9DzM3E5YVUlq1BpTHXe3Tvgyy1VNNJV8y8C19ORP5C36mx89UdcmK78i0LYxR8AzqeBzGVDgNmcbTB1YkbNp6qfzJ4VdF_injxv0Ps7onxdRN0wYe0kL_LC4YXp4600BWU1d2ycuOOgixxZu1Z38Fe5WD7aN-eeh8X96qc76SartUMuTua4DMjorIT9Tl8jWdXjfYKs3mgij5uJyhTjY-014p2xjjgmg9TmO2k5e90jnNgOhpmfXP62JX5R_ujRbXzkwyq4fPfQfvYaNrUBsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚠️
همین حالا موجودیتو
🤩
برابر کن
❌
☑️
۲/۵ میلیون شارژ کن ۱۰ میلیون شارژ شو
✅
برای اولین واریز تا 15 شهریور ،
0️⃣
0️⃣
3️⃣
درصد بیشتر در وینرو شارژ شو
🎁
✅
به ازای هر واریز در وینرو به ترتیب 300 ، 150 ، 75 درصد بیشتر شارژ شوید
.
🔊
با شارژ اضافی بدون ریسک بازی کن سرمایتو چند برابر کن
⚡️
🎲
ثبت نام آسان و سریع کلیک کنید
✅
پخش زنده‌ی تمام مسابقات
کلیک کنید
🎰
✅
درگاه اختصاصی برای کاربران
💰
🔊
اپلیکیشن حرفه ای
📱
🎲
معتبرترین سایت ایران
📱
کانال اخبار و هدایــا a17
🌟
📩
@winro_io
🎲</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/news_hut/69764" target="_blank">📅 01:46 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69763">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/20cf5580ad.mp4?token=MGIwvHZ28hAGHBwtDra4_4SG4w0Qa0_6imUxVFZmq3-w30iglKFEr_o9vQWaIWcXb4BFC6T7mEmpot8niImhHREueI7FYKzB9XAkt_yD_4WmHto4zVxda1UNuGskgWnQaw6qz6z_VWGUCWGJvKEBb7tlFacwWcj8D2Yarlc8grLdcm-CV-sZ15BNewt45HGMZ9k-V4vr1_a-9VSUdbydUeXFOJCKvPv-v8-ZBWPz7ZiumOvtxVraQrb_F0LfRfQXNlqNkCG11faqLGQGiCYqzYk948KvkIMb4lsN_vt_mOFJEcoAOLf1J_muL8zEUd0ypykW-Rrgy4dTZOJVxB95Qg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/20cf5580ad.mp4?token=MGIwvHZ28hAGHBwtDra4_4SG4w0Qa0_6imUxVFZmq3-w30iglKFEr_o9vQWaIWcXb4BFC6T7mEmpot8niImhHREueI7FYKzB9XAkt_yD_4WmHto4zVxda1UNuGskgWnQaw6qz6z_VWGUCWGJvKEBb7tlFacwWcj8D2Yarlc8grLdcm-CV-sZ15BNewt45HGMZ9k-V4vr1_a-9VSUdbydUeXFOJCKvPv-v8-ZBWPz7ZiumOvtxVraQrb_F0LfRfQXNlqNkCG11faqLGQGiCYqzYk948KvkIMb4lsN_vt_mOFJEcoAOLf1J_muL8zEUd0ypykW-Rrgy4dTZOJVxB95Qg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇷🇺
سربازان روس با تفنگ موفق شدند پهباد اوکراینی رو سرنگون کنند.
@News_Hut</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/69763" target="_blank">📅 01:08 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69762">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🚨
‼️
حمیدرضا رجب زاده یکی از مداح های حکومتی بوده که چند هفته پیش به قتل می‌رسه، حالا یه کانال تلگرامی مدعی شده اونا این قتل رو انجام دادن دلیلشون هم اینه بوده که این مداح تو دی‌ماه جز نیرو های سرکوبگر بوده و به سمت مردم تیر می‌زده  ویدیوی قتل که قلبشو از سینش…</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/69762" target="_blank">📅 00:35 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69760">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jdKyGV2NDlMmeJ3IkdGKC2FcXNpQq3AXu76M5XRuVDqGLOFlD1Y8iP5E8CgHcD9fk-qtGVDi2lRupeCioXcNYb3-sAgnem9rSrpn5eO1hZkuHjEASoz_FZ4BPj_jIIoOtkwTGqV4sr7CRIr-vPjsW4iOlhJzkGTAoEmBjIW7KI8ZEn2QDizE-Hq43Fpqo5aPe0H5p9VtTqUxZfNhjcWY5h374Jz1ZibY-ragzSQmu4X4LKcFrksT6sr20E9n_eYEQgt2HWO8ymif1UkHzBmfTy4mfAma8URbM8RjqUytzSfjP9QMx7KiUg-uiZzU5-1WNLKLz1baTBJEBGbwCGEPBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f5e8a9ce1b.mp4?token=E6VtmXQ3UNPJ0NZjXnSUHIL_G08rJNLkdzth_oNDuPLd9RXfLo_IyYpDxZDaVPWb41LSv1GjfSX7OSe-8tQw43YVMDDabhZTZIz64zCjZ1V14KwTVq_XTBNbGZ4O0uEmePf6_rI9Fyj6nlOOvVuspHm6XI1ItF_JDsQ52bZAef7xntK-Nz0sIxAo6M6WqO-RrAZt_iOZ880YqFSvpFkLotosDiCzszfqwrJDUyJfC4KdWoESxPrYL8uXD50jCKQfm7v5mizk76GWkJSIFut1geeRoYVdXAb_a0Y6YJOUZ7PGzd9sYh0OUndqbW6p2wC3qvD5INgdtvLuklSKYPMV7Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f5e8a9ce1b.mp4?token=E6VtmXQ3UNPJ0NZjXnSUHIL_G08rJNLkdzth_oNDuPLd9RXfLo_IyYpDxZDaVPWb41LSv1GjfSX7OSe-8tQw43YVMDDabhZTZIz64zCjZ1V14KwTVq_XTBNbGZ4O0uEmePf6_rI9Fyj6nlOOvVuspHm6XI1ItF_JDsQ52bZAef7xntK-Nz0sIxAo6M6WqO-RrAZt_iOZ880YqFSvpFkLotosDiCzszfqwrJDUyJfC4KdWoESxPrYL8uXD50jCKQfm7v5mizk76GWkJSIFut1geeRoYVdXAb_a0Y6YJOUZ7PGzd9sYh0OUndqbW6p2wC3qvD5INgdtvLuklSKYPMV7Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
حمیدرضا رجب زاده یکی از مداح های حکومتی بوده که چند هفته پیش به قتل می‌رسه، حالا یه کانال تلگرامی مدعی شده اونا این قتل رو انجام دادن دلیلشون هم اینه بوده که این مداح تو دی‌ماه جز نیرو های سرکوبگر بوده و به سمت مردم تیر می‌زده
ویدیوی قتل که قلبشو از سینش در میارن و رو صورتش خودارضایی می‌کنند رو هم منتشر کردند و بعد برای خونوادش فرستادن؛ چند ساعت پیش هم اعلام شد که قاتلین دستگیر شدند
🔞
مشاهده‌ی ویدیوی اول
⚠️
⚠️
مشاهده‌ی ویدیوی دوم
🔞
@News_Hut</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/69760" target="_blank">📅 00:08 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69758">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a034d8d108.mp4?token=UB2rF7hm5FX69E-hFGm3K1xtwvNGEEFf81u9zkkI-rTQA2lmhVSsp_-7bFyL835YkBQyn_PIGaOL-RpJMghyxEuJSmwrNOaTrFZQBy7eGf808YjWLV7jl8BsyPwwQT-NsF2j_7c-dIw1QtJbLkL3P8ClmisH7s1zcQJaF_jMrmHlsW76upvZjQDhrVs5CdOOlIvI5yVeBz3-lDcrQoss-LhAEm6PNR51a0VzSAx1GYfKUL42qlZkVgIaXGrubknADBhmV5IRwo_cgXdDOjaQ6uN-AboxilFfQQFW4NRGLFof-C1wi2SBZVrWYTF1MAAsI5zpMSn7oNtvekGOxQKQ6lz-6-GXsqangSLR2aoZtyNkBT4RkBDxdBU6AD3h1oPlV3JbckjCWTwLZ7MRLWWGxSWSWPjzCfu2VMV4RdqrZQ2ImsG5GPmeJSAz70M_8XA8R5UFPB6oT1KhA8kP0P1L7vqpUjOL4FesGR3njSkHCJA8irNSCn8K5rBX43Bhz9eb19M3iU2uDgqjeZjwJNyZwbzBUhr503CVRJUOfcOHiWeC4ffCsFUtG0Pu1pZKINUpRE4Yh_aUttM-46fEwSrjtA7bt8aUq8edhY491rR8n26boV-Zr3toi0zX9DBFdORYqEONJVR2usUoyDWKmZjizB_xI-3LhtvXQJcGr0k6lIU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a034d8d108.mp4?token=UB2rF7hm5FX69E-hFGm3K1xtwvNGEEFf81u9zkkI-rTQA2lmhVSsp_-7bFyL835YkBQyn_PIGaOL-RpJMghyxEuJSmwrNOaTrFZQBy7eGf808YjWLV7jl8BsyPwwQT-NsF2j_7c-dIw1QtJbLkL3P8ClmisH7s1zcQJaF_jMrmHlsW76upvZjQDhrVs5CdOOlIvI5yVeBz3-lDcrQoss-LhAEm6PNR51a0VzSAx1GYfKUL42qlZkVgIaXGrubknADBhmV5IRwo_cgXdDOjaQ6uN-AboxilFfQQFW4NRGLFof-C1wi2SBZVrWYTF1MAAsI5zpMSn7oNtvekGOxQKQ6lz-6-GXsqangSLR2aoZtyNkBT4RkBDxdBU6AD3h1oPlV3JbckjCWTwLZ7MRLWWGxSWSWPjzCfu2VMV4RdqrZQ2ImsG5GPmeJSAz70M_8XA8R5UFPB6oT1KhA8kP0P1L7vqpUjOL4FesGR3njSkHCJA8irNSCn8K5rBX43Bhz9eb19M3iU2uDgqjeZjwJNyZwbzBUhr503CVRJUOfcOHiWeC4ffCsFUtG0Pu1pZKINUpRE4Yh_aUttM-46fEwSrjtA7bt8aUq8edhY491rR8n26boV-Zr3toi0zX9DBFdORYqEONJVR2usUoyDWKmZjizB_xI-3LhtvXQJcGr0k6lIU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تو این مملکت اگه پول داشته باشی، حتی کمپ ترک اعتیاد هم می‌تونه شبیه هتل چندستاره باشه!
● بعضی کمپ‌های لاکچری خدماتی مثل:
🍽️
غذای رستورانی
🏊
استخر، سونا و جکوزی
🎱
بیلیارد و پلی‌استیشن
👨‍⚕️
پزشک عمومی و روانشناس
📱
موبایل و لپ‌تاپ آزاد
🛏️
اتاق‌های VIP
ارائه میدن؛جایی که دیگه از کمپ های معمولی خیلی فاصله گرفته!
@News_Hut</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/news_hut/69758" target="_blank">📅 23:15 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69757">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d2a2b2f82e.mov?token=YcTlSxjjFbjLDDUP5rmC1OHw0tSfnluNJ6cdX8ssk6JdiIM_iE204NxGJt3gugsrWZE3BAAd4YFMB3HrXkzGJq5lxt9y2QP5SbCq_X_l3_6VewUhLbEiTLCXx9HjyjS_IdacHGAWqCJStkiQt9Hn2otVRGTkqC1aH5Wi8qgHmRk6nEN2rvOw8xUbN0R_gPM-HQbmycFjvbZO1-QDQdQF14MNaSrS5mMidFBUu6a7AMusEL17-MH2gA2fgUfqwjZvn0SvcCmpcYNsUKngnC-QgJhFAmpkL10tD5T0fX0PN5Ny2GDcCQdGiYyUF9GpmJ2BUpJ1b3hJtyJZFi8NPYpn-Eng05sHUyorUlcpN9sjQ84PJ_H-YbNJvFh7WXRm63YROEXmLqr-8M3cATEv-pw9YWCoFCvi0XrM-Zl-7BNwkmCA5Aw0zudczIFiTxsRj4D7phUUqaDkUcPUQ4cqG8ayMqQy2PekTxqAajohDTo-3xqVLvluT4GHOroClrarW2UZ7ocJus9mFCtjNnlfxLLSQCfC30dLlAq67Oop1oZ-4mtp16_xxDmePZiL0IM4OCi-UjQq4s5CxwJ5GaJpZ6kdsDhyAc9JAsNXkMS8J1yFsIEbLKJOBEvBWWS4t3ena3txMs9qP9lFAJcmuyKRKQStREm01dGkQ1tv3skHeiJXgSs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d2a2b2f82e.mov?token=YcTlSxjjFbjLDDUP5rmC1OHw0tSfnluNJ6cdX8ssk6JdiIM_iE204NxGJt3gugsrWZE3BAAd4YFMB3HrXkzGJq5lxt9y2QP5SbCq_X_l3_6VewUhLbEiTLCXx9HjyjS_IdacHGAWqCJStkiQt9Hn2otVRGTkqC1aH5Wi8qgHmRk6nEN2rvOw8xUbN0R_gPM-HQbmycFjvbZO1-QDQdQF14MNaSrS5mMidFBUu6a7AMusEL17-MH2gA2fgUfqwjZvn0SvcCmpcYNsUKngnC-QgJhFAmpkL10tD5T0fX0PN5Ny2GDcCQdGiYyUF9GpmJ2BUpJ1b3hJtyJZFi8NPYpn-Eng05sHUyorUlcpN9sjQ84PJ_H-YbNJvFh7WXRm63YROEXmLqr-8M3cATEv-pw9YWCoFCvi0XrM-Zl-7BNwkmCA5Aw0zudczIFiTxsRj4D7phUUqaDkUcPUQ4cqG8ayMqQy2PekTxqAajohDTo-3xqVLvluT4GHOroClrarW2UZ7ocJus9mFCtjNnlfxLLSQCfC30dLlAq67Oop1oZ-4mtp16_xxDmePZiL0IM4OCi-UjQq4s5CxwJ5GaJpZ6kdsDhyAc9JAsNXkMS8J1yFsIEbLKJOBEvBWWS4t3ena3txMs9qP9lFAJcmuyKRKQStREm01dGkQ1tv3skHeiJXgSs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇷🇺
❌
🇺🇦
نیروهای روسی به هدف قرار دادن تدارکات اوکراین ادامه می‌دهند و یک لوکوموتیو دیگر را در نزدیکی ایستگاه راه‌آهن «لوزووا» در استان خارکیف منهدم کردند؛
منطقه‌ای که یک کانون کلیدی برای کی‌یف جهت انتقال تجهیزات نظامی و نیروهای کمکی به سمت دونباس محسوب می‌شود.
@News_Hut</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/69757" target="_blank">📅 22:32 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69756">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/da63e2e1aa.mp4?token=E2i8lT9LFYNM3p-X-glUE-1jlvw85DZbi_XcsgP5VX_KNuJW29Dyf_r7IaY_lJw2jDcjGJIaZx9NluoGryoLIrMYr54UzJKEoxvTh2cOy8etA40yvRutq7SUWDQssALLfi0yi4VVOLKwQ0ERUyFebYrk59_SPG_uWsl5Ysxzap9JfVQOQFe22U4pMu0OKLqr5V1eBdjjq1fAne2Yt8eNF5UIlPQCh8k1MtDUvEl2SRRyRu2FXjN3Hj8yB8Y-BQnjTn7dlF-ApYj_QTiINUzOnF6MpCoN9aKzPSaZwVUrYPFz74v5XNmcmDjsqHrfurrgTgaudJajNTZ6LyaZwhmZwKPHpV70ErqG7mgEY06_XtgSNUo_rADAdWSEzayE7SfO7RR34_0hlXtydcFREMSItpvSAYmcZVyU3NF9trEl-0e8_p_eZlW0nuaOofi9yS0PY1BIg5pP8Q9F0l-alWXOgdXHdB9dLmbne4bbHckEwjIjA4_40GxdadFRAAu_jjv4V_cFaN_gSAV2WyuqQaJnzz4EkR4ST1SIjvAjxgjJ2VAxNYTwj6W8alaNhv8-SyQX0g9AZf3hSvWv3oyoEMRn6Ko0y-pokJZluXa8oVih2KYz-f1c1ksRRPZLGmXiHXQ9mkLRoXxM8b0Xv3h_q0DFvUYpRDJAFi1rVi4O6cuVL-c" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/da63e2e1aa.mp4?token=E2i8lT9LFYNM3p-X-glUE-1jlvw85DZbi_XcsgP5VX_KNuJW29Dyf_r7IaY_lJw2jDcjGJIaZx9NluoGryoLIrMYr54UzJKEoxvTh2cOy8etA40yvRutq7SUWDQssALLfi0yi4VVOLKwQ0ERUyFebYrk59_SPG_uWsl5Ysxzap9JfVQOQFe22U4pMu0OKLqr5V1eBdjjq1fAne2Yt8eNF5UIlPQCh8k1MtDUvEl2SRRyRu2FXjN3Hj8yB8Y-BQnjTn7dlF-ApYj_QTiINUzOnF6MpCoN9aKzPSaZwVUrYPFz74v5XNmcmDjsqHrfurrgTgaudJajNTZ6LyaZwhmZwKPHpV70ErqG7mgEY06_XtgSNUo_rADAdWSEzayE7SfO7RR34_0hlXtydcFREMSItpvSAYmcZVyU3NF9trEl-0e8_p_eZlW0nuaOofi9yS0PY1BIg5pP8Q9F0l-alWXOgdXHdB9dLmbne4bbHckEwjIjA4_40GxdadFRAAu_jjv4V_cFaN_gSAV2WyuqQaJnzz4EkR4ST1SIjvAjxgjJ2VAxNYTwj6W8alaNhv8-SyQX0g9AZf3hSvWv3oyoEMRn6Ko0y-pokJZluXa8oVih2KYz-f1c1ksRRPZLGmXiHXQ9mkLRoXxM8b0Xv3h_q0DFvUYpRDJAFi1rVi4O6cuVL-c" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
از مردم پرسیدن "چه فکریه که نمیذاره شب‌ها بخوابین؟"جواب‌هایی که دادن جالب و دردناک بود؛
میدونم پول دار شدن زمان‌بره ، ولی خب به این فکر میکنم که مامانم داره پیر میشه...
من چی کم داشتم که بهم خیانت کرد؟
برادرم که فوت شده، هنوز مراقبمه یا نه؟ دوسم داره یا اینکه واقعا ولم کرده؟
اینکه الان من بهش دارم فکر میکنم، اون داره به کی فکر میکنه؟
یه دختری هست که میخوام خوشبختش کنم، امیدوارم لیاقتشو داشته باشم..
@News_Hut</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/69756" target="_blank">📅 22:03 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69755">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">⏺
ژنرال برد کوپر، فرمانده فرماندهی مرکزی ایالات متحده، در اسرائیل فرود آمد تا جلساتی را با ژنرال زمیر، رئیس ستاد، و مقامات ارشد نظامی اسرائیل برگزار کند. این مقام آمریکایی پس از برگزاری جلساتی در بحرین و امارات متحده عربی، به اسرائیل سفر کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/69755" target="_blank">📅 21:19 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69754">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d11c35a859.mp4?token=vySfTbo6Ji0K3H9RLMlaP8lRxKF8fDeyRsSVJxQTUVMYRrYSEBNv0yCHl5i0gNLyvddTSxNDvZoALSMtLH0wj1EmafTmj9ZM1xULxvlUs5QBUMUocqim9eOFc3STmHW9_yiTA1M-XSdOErDKn8IPZhxcA_DdhU-a6Ew9qsg_-sMHx0FpmkdUtnjTWgOQ_Aqgk5sgfntVuzDmCX55AmR2DDboaCX2hOp4vUY0ChH54t4yuycCTTTWODtFHHSltYFcHZWUaqXesPXlD7tq0kZMBy9ryjgq7TtHYCy5JXrGAbiWDnm5z3r_AQOPEMomrU5kKRJnzBYZv-xvbGuOt_EPAlWbjSWuSXin0YHTFrOkuj-OOjyNHuyiPUPkvpePGnrxev5MmHdapazitVm3qAnW1jYuXawVGOTKYIEaqVAU-Qq0m36PsMSRTVDbq4LKFpX5mkwhFkTC5GaPLzdP306lzwx6nSStOYNNI0TgOeNsyWHEgSP3Yqe4EefoqINEUqKtYdDb_zoslpGE4MQHxEtGLcgHq_NycwVXCKO96RhDYFiD01CirOUTevFr-c-NdFhKrz7SO2YPDplHTnLAn0rOiQcIKBGfgdJ83EZwDVqSo1qqLwyNAe-nzAM0eDPBHrSs8jFFpl9KTWx7y5aHwRUebWaK96UGYlCpZXIutno2Njg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d11c35a859.mp4?token=vySfTbo6Ji0K3H9RLMlaP8lRxKF8fDeyRsSVJxQTUVMYRrYSEBNv0yCHl5i0gNLyvddTSxNDvZoALSMtLH0wj1EmafTmj9ZM1xULxvlUs5QBUMUocqim9eOFc3STmHW9_yiTA1M-XSdOErDKn8IPZhxcA_DdhU-a6Ew9qsg_-sMHx0FpmkdUtnjTWgOQ_Aqgk5sgfntVuzDmCX55AmR2DDboaCX2hOp4vUY0ChH54t4yuycCTTTWODtFHHSltYFcHZWUaqXesPXlD7tq0kZMBy9ryjgq7TtHYCy5JXrGAbiWDnm5z3r_AQOPEMomrU5kKRJnzBYZv-xvbGuOt_EPAlWbjSWuSXin0YHTFrOkuj-OOjyNHuyiPUPkvpePGnrxev5MmHdapazitVm3qAnW1jYuXawVGOTKYIEaqVAU-Qq0m36PsMSRTVDbq4LKFpX5mkwhFkTC5GaPLzdP306lzwx6nSStOYNNI0TgOeNsyWHEgSP3Yqe4EefoqINEUqKtYdDb_zoslpGE4MQHxEtGLcgHq_NycwVXCKO96RhDYFiD01CirOUTevFr-c-NdFhKrz7SO2YPDplHTnLAn0rOiQcIKBGfgdJ83EZwDVqSo1qqLwyNAe-nzAM0eDPBHrSs8jFFpl9KTWx7y5aHwRUebWaK96UGYlCpZXIutno2Njg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👑
شاهنشاه آریامهر: اون روز دیگه من نیستم ولی حقیقت هست
.
@News_Hut</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/69754" target="_blank">📅 21:15 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69753">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X32PRAaogoqrXnuzo48YsDuCSVERQ87ItdgDLSJ3eXJljgR3FHWk6fgUESAA9ZueBG7OXwXWwganxmiznet5OKes3rQI4GxZt6OYjgZmPCXKo4d1cvSxJCWCMD_cDjLkEO03qwhmBqRQqWGHnYPA1xgeelyeNa70MScwUYOh3NA6Jl4sfoOGHS50QU97fQ1w8_vmeOvx2VDeGrhKGLV4OYn2w4KHjrBEX-dP4m5a6c2Ab4M4vqKN-LDLX3R1j3hRv5zjCju5fpaYSFQqVmkfKxe3PNe0PlHzamO2Wonq7hPgIIm7yk70Ak_PtW5hnhc5l9QW1YWcwC04rX5LmyNrZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
کانال ۱۳ اسرائیل:
اسرائیل خود را برای احتمال اقدام یک‌جانبه علیه ایران آماده می‌کند.
@News_Hut</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/69753" target="_blank">📅 20:56 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69752">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e1727b3200.mp4?token=AYYWSyPUCW5OXeOWUc1BM_1Z5GEvdc339aeDcUWO2GViYQ8BzRlD0ZpPehjLwsEYQlkgEZmm93zw2X-fpOixIkBiFHfjOfvQUMZG_Zo7BlBs-_XYJ3g-Wdje1mmzf-Yo2WcrmWeg9pHHxYVK-4lEtmoefZpiFj8MCQnODeJZHvDwXACoO5WVFqCRqQt3YYzM5rKqhKKUmOL4mFpNO0QreUizgsQ-PpQCYGn6I0AYuNtozag4XTK-edu3j8zVlC83OfoOL3ast5QsyTjQtpejRGu2FCr60FUSGnkmMnPPtz-_VGegMk5bhMmWBSJoXv5C-tAMY00qWLXASEHRMQpc7Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e1727b3200.mp4?token=AYYWSyPUCW5OXeOWUc1BM_1Z5GEvdc339aeDcUWO2GViYQ8BzRlD0ZpPehjLwsEYQlkgEZmm93zw2X-fpOixIkBiFHfjOfvQUMZG_Zo7BlBs-_XYJ3g-Wdje1mmzf-Yo2WcrmWeg9pHHxYVK-4lEtmoefZpiFj8MCQnODeJZHvDwXACoO5WVFqCRqQt3YYzM5rKqhKKUmOL4mFpNO0QreUizgsQ-PpQCYGn6I0AYuNtozag4XTK-edu3j8zVlC83OfoOL3ast5QsyTjQtpejRGu2FCr60FUSGnkmMnPPtz-_VGegMk5bhMmWBSJoXv5C-tAMY00qWLXASEHRMQpc7Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
حاجی‌دلیگانی، نماینده مجلس:
قدرت چهارم جهانیم و حق وتو می‌خوایم!
@News_Hut</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/69752" target="_blank">📅 20:32 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69751">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e8f98a7872.mp4?token=HSXWjD6YbXsz7e8WmvADIHsMEw6GW1C-jwxB1X7ly8vkpYtbSkY1X1e8OM7ZPQyZtoM_M3-9kHhJeuUp32soBG5PW4_iqSYKJKEYJlOLht8746QVOqfk59kWWpI4aSkVL7CyWg07QgPCJEbHTwrWBE77aAs9qEghbcUroyHQgdOPE0Bd82DZrTF_4JylFvo_P5aLf5QVtGlNfjpwmyUWnvNTmEIM4Y185sNRz_YPMHsdmxAq7YK0I5zlWSCWEf0_xtirepk5GLdWtY0XCpdVqwDKr6i2vZBl0tX7it7GunfJHKI4bN3C0CHcXKNRqnnqreG1MAPoCoUDWzXao6vw5Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e8f98a7872.mp4?token=HSXWjD6YbXsz7e8WmvADIHsMEw6GW1C-jwxB1X7ly8vkpYtbSkY1X1e8OM7ZPQyZtoM_M3-9kHhJeuUp32soBG5PW4_iqSYKJKEYJlOLht8746QVOqfk59kWWpI4aSkVL7CyWg07QgPCJEbHTwrWBE77aAs9qEghbcUroyHQgdOPE0Bd82DZrTF_4JylFvo_P5aLf5QVtGlNfjpwmyUWnvNTmEIM4Y185sNRz_YPMHsdmxAq7YK0I5zlWSCWEf0_xtirepk5GLdWtY0XCpdVqwDKr6i2vZBl0tX7it7GunfJHKI4bN3C0CHcXKNRqnnqreG1MAPoCoUDWzXao6vw5Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
معاون رئیس جمهور آمریکا آیت‌الله جی‌دی ونس:
در کنفرانسی، لحظه‌ای پیش آمد که من و یکی از دوستانم داشتیم درباره مسیحیت و مذهب کاتولیک صحبت می‌کردیم.
درست در همان حینِ گفتگو، لیوانی از روی دیوار پایین افتاد.
می‌دانید، فکر می‌کنم یک فرد خداناباور (آتئیست) احتمالاً آن را این‌طور نادیده می‌گرفت که: «خب، چه اهمیتی دارد؟ لیوانی از روی دیوار افتاده است.»
اما در آن لحظه، احساس کردم که گویی خداوند سعی دارد پیامی برایم بفرستد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/69751" target="_blank">📅 19:38 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69750">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b83cf8ea7b.mp4?token=R-Q1Dxa4v4tUplZe7A69uhJGm8Bc5xAiDqDHL20i-QGJDTC0abZ9tkK5FepEaRIK8HVgCFnZFIr-9R3cv585DA4PUpScoOAUMJt7qqOJTKLIYvx9RgdYP13MKaWOcWrUgKXeBR9m9wa8-7ty4btfI2-NM-ooefbH_XoY6eZfReV7m9N6tJgj7i2tzxfcrLtzIArNwCAdEsNUI9En1Xj17XspItoOydG32VAE23c5NHtmwgP_a6PJMY32pfW-3VZ_BAOxz88tG_lQEE1b3PdZISjuiGQOM_HQHbbdGjpfegT9pBbCzF2EzSZiFkq9-rxXKJC6g3e67zdnm4CR2HROnA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b83cf8ea7b.mp4?token=R-Q1Dxa4v4tUplZe7A69uhJGm8Bc5xAiDqDHL20i-QGJDTC0abZ9tkK5FepEaRIK8HVgCFnZFIr-9R3cv585DA4PUpScoOAUMJt7qqOJTKLIYvx9RgdYP13MKaWOcWrUgKXeBR9m9wa8-7ty4btfI2-NM-ooefbH_XoY6eZfReV7m9N6tJgj7i2tzxfcrLtzIArNwCAdEsNUI9En1Xj17XspItoOydG32VAE23c5NHtmwgP_a6PJMY32pfW-3VZ_BAOxz88tG_lQEE1b3PdZISjuiGQOM_HQHbbdGjpfegT9pBbCzF2EzSZiFkq9-rxXKJC6g3e67zdnm4CR2HROnA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
صداوسیما تصاویر مربوط به هواگرهای آمریکایی و اسرائیلی که توسط سپاه منهدم شدن رو منتشر کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/69750" target="_blank">📅 19:38 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69749">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">app (7).apk</div>
  <div class="tg-doc-extra">53.1 MB</div>
</div>
<a href="https://t.me/news_hut/69749" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
با این سایت به راحتی میتونی کل ضرر های جام جهانی رو جبران کنی
بونوس هاش واقعا عالیه
👌🏼
بدون قیدوشرط
❌
با هر 1 میلیون شارژ ،
🤩
🤩
🤩
هزارتومان شارژ اضافی بگیر
🅰️
❌
❌
طرح شارژ رایگان فقط تا پایان مرداد ماه</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/news_hut/69749" target="_blank">📅 19:38 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69748">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PI8-XCVQhaxjYG_PLzRpqfcGsdcW6wRiU44f-wn3N28MNyKq3tOOhEBKLGYDoA6XRrLf_CgRpszbaNVg6Mi9-j2RpPJ23_O6yC1ofkEFCIGPVTLv79ddzWhoZr2ekBpJXo1dlPWc0hYObhMbUlWO_GyT1KhT61eoCD6waMNaZEkEiXDh7wv_snTMBlfvWPH5vd_QQkAn-9RGFY-e0Pn4HAKcw5RNCFhyOFTgamuDt6Yy9AMMzbJHunoRRtAsrDHgP3Yej7Vd9qpNZCRm_YafmrFV3g-P2KSxAR5X1HI34P2JiReK2ZJAzVgJ0-lnKkR46PhEmThRtJeh5ttlf91W5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🛍
#اتلتیکو
Vs
#منچستر_سیتی
💰
🛍
#لیورپول
Vs
#موناکو
💰
زمان: یکشنبه ساعت ۱۴
🚨
تجربه پیشبینی مطمئن با
🤩
🤩
🅰️
شارژ اضافی و ریسک خیلی پایین در
#بت_اینجا
رو از دست نده
❌
🤩
🤩
درصد برگشت وجه در  صورت باخت:
🌐
betinja.bet
🌐
betinja.bet
کانال بونوس های رایگان
g17
@betinjabet</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/news_hut/69748" target="_blank">📅 19:38 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69747">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c5pMvcpPXZ6xc3Vtecdc8qmzFIkBsN7n0w4Wp2iaIk7j0h8KWUFn-FC-9a4WRF4pFEmujlzfZkuN5KKrxinac_7ETv9v8Yu4WWaVcvf-V60gbQQS0fIK4puJGh2CHfuKQ5ij3L-qaJeKpQEXh5jr87X43Jb78TWb-B4Xa5vzXM5tM18yhXzBBA7gEL4b0Y4-z_ZXjjbe1Pw9Wf-pru-Z1j8qLsLQsXKaUgp3Qesj7DNaw91UpYuTe-gAU0EVjWUaFSZA6jzfnmQK-Kx-90miwlp3wb1nbZF05i0k3w47juvKSwTC-IBQWg9xRjhy07tjXznCWk3WQeAXFJDBRJz0qA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
بیانیه دبیرخانه شورای عالی امنیت ملی:
🔴
اگر ایالات متحده رفتار خود را اصلاح نکند، تنگه هرمز باز نخواهد شد.
اصلاح رفتار به معنای موارد زیر است:
عدم تهدید ایران به هیچ شکلی و به هیچ زبانی، و عدم توهین به مقدسات مردم ایران.
پایان دادن به جنگ و تجاوز علیه ایران و متحدان آن در لبنان، فلسطین، یمن و عراق، برای همیشه.
رفع محاصره دریایی و عقب‌نشینی نیروهای نظامی دریایی و هوایی از اطراف ایران.
پرداخت کامل غرامت خسارات وارده از دو جنگ تجاوزکارانه علیه ایران.
رفع تحریم‌های ظالمانه و غیرقانونی اعمال شده بر مردم ایران.
آزادسازی بدون قید و شرط وجوه مسدود شده و ضبط شده متعلق به مردم ایران.
🔴
اینها مطالبات مردم ایران هستند که در طول ۱۶۰ روز حضور مستمر در میدان‌های جنگ و خیابان‌ها، فریاد زده‌اند.
شورای عالی امنیت ملی هرگز عقب‌نشینی نخواهد کرد، نه در جنگ و نه در مذاکرات.
@News_Hut</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/news_hut/69747" target="_blank">📅 19:11 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69746">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromARAD GROUP |‎ سیگنال آکادمی اراد</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WTDCOUmTlYFGvp1XTMewZes1vRwLvKPzoMI3__aF-32ecigpXBgUWAoZbSJ7HJ9_yjl7oBfUBIUm71SB_6nK6yuQVrzHBppSqiPRm6ZpapFWDhFj3fAgcH1PiNMCjJGauQ5EH9cmPwB0uG4Ref5UZt4ZslOQb1LHSJvUTanrEdGS-7XAydbqVSDT11xcusZRhlPEZVevv2qqZzixDfMm3pxozt3j4iqB-7-RnKKdqs6MSJuktAFrpecBHOeo0MQTHYn8xHAa2RCd3A_4A8nPG-Zrd9HQjSOeocYvu_TH8sF7i3A6iAkwWIGuR2ATFd_p232v0-CK-TD2RBvtrHmDIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
غیرفعال شدن تراست ولت و فریز تتر برای ایرانیان !
بعداجرایی شدن تحریم ها جدید امریکا و بستن حسابای بانکی حال نوبت شناسایی و غیرفعال کردن ولت های ایرانی هست و طبق اعلام مقامات امریکایی ، به گفته انها این کار برای جلوگیری از پولشویی دولت ایران انجام میشود و بیش از ۱ میلیون ولت شناسایی شده است که به زودی مسدود خواهند شد
نکات مهم برای ایمن نگه داشتن دارای های شما تو کانال قرار دادیم حتما رعایت کنید
آموزش رفع مشکل
https://t.me/arrad_group/2450</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/news_hut/69746" target="_blank">📅 19:10 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69744">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vJeV5X0CvFOPBYTy9WC5IAP4lPm2j3aA9FMjt19a8m295_1HrfY_CsCOXNBLyC-qmu67V71MglZD-KeKfekd8VjO9e3xxNnRdUAOGP-dcx3ey7tM1WYLaxauioZDCVgHrLOJl2eIhT7rFO9_rca3k9BrceYKQnC128K3hZYCXHCsvSwgmLHjdzn2VME7VHLFluOo00c6TJR8EnZfskpoFJ4YB_U-bP2ZcW_CO-a4z0sObm6Z_-8y1fGvdo9ITjw9dVWl7dwLX6RWu7GWPDyi6kd6m98t6-QYOy3VPilsjRFkAwcNVYYaov3wdH1sUrfzz4cAKV_yYs8NRNQZf6hCFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
نیویورک تایمز:
ایران فهرستی از خواسته‌ها را ارائه کرد که این موضوع، امیدها را برای بازگشایی تنگه هرمز کمرنگ‌تر می‌کند.
@News_Hut</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/news_hut/69744" target="_blank">📅 18:58 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69743">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uT2GkZBXk6oFZyiqllCOEMBoH-8ekMIO4MgO-Y0iMvF7Vww3pMkUGjrMgVir2I_WuLXFGY5TG1dM8lTOs5n20L7kOtO5-NONcbmtMa8QSVDWr8vUyXDqf5DfgWhijr5Xr2ws27IEcpXZaLxBxU2KV5lcsgikolLYgpfgkEOxgoRKmjX1GreBpIfTgDbZNkTrM_YsMowbSgmWudDyxRW3LozzuDNpD-X3Ym3FzWI-BPa6C_30d11lPB3ArXFBRROexQWk38e_ZgogYlRLEI7S-pl9O2Hg7wm3CM6lUJyCdV5fWhjLxV1e5896DiX7nWdqCpiVBo65wfHb_lqPMlnHJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
سازمان حمل و نقل دریایی بریتانیا (UKMTO):
گزارشی از حادثه‌ای در ۱۸ مایل دریایی شرق خصب، عمان دریافت کرده است.
یک منبع موثق گزارش داده است که یک کشتی مورد اصابت یک پرتابه ناشناخته قرار گرفته که باعث آتش‌سوزی شده و آتش  خاموش شده است.
هیچ گونه آسیب زیست‌محیطی گزارش نشده است. کشتی و خدمه در سلامت گزارش شده‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/69743" target="_blank">📅 18:36 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69742">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/43af7e53e1.mp4?token=OAPg-TlbuyJzaV6vlgfcsNFRH5xvQdq3qYVoc_TpcNQyzdAFIjNixVOCBB-17ncixFbXAke6gC398cRev3H7cQJGtKfzTKIZmqwfMvJQ3OxGVJmrPBK6UZA1tVYoYPSSSJUTltb2fUSpQ5_UBb536E02NwdoaKImEOGkQmpAtBXC227a7H2zZjzK53yJLRE0WLg1xL-5bs1eS1NsoN9Pa69ugRlik2o9vrrrOlsiEX1j4O-zKdRdAyLu1QA9Ztut3xqPu0glPHVJoyE_RZp4N690UxBxbrXbC7MHajWX-v7ZaJtVGMNg34Tk8FEUEbMXB_EOSCzZ5PjZK6wDYHTxJg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/43af7e53e1.mp4?token=OAPg-TlbuyJzaV6vlgfcsNFRH5xvQdq3qYVoc_TpcNQyzdAFIjNixVOCBB-17ncixFbXAke6gC398cRev3H7cQJGtKfzTKIZmqwfMvJQ3OxGVJmrPBK6UZA1tVYoYPSSSJUTltb2fUSpQ5_UBb536E02NwdoaKImEOGkQmpAtBXC227a7H2zZjzK53yJLRE0WLg1xL-5bs1eS1NsoN9Pa69ugRlik2o9vrrrOlsiEX1j4O-zKdRdAyLu1QA9Ztut3xqPu0glPHVJoyE_RZp4N690UxBxbrXbC7MHajWX-v7ZaJtVGMNg34Tk8FEUEbMXB_EOSCzZ5PjZK6wDYHTxJg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
صحبتای یه وکیل مرد:
توی تمام این سال‌ها به این نتیجه رسیدم که نود، برای پسرا معجزه می‌کنه.
پسرا عاشق اینن پارتنرشون بهشون نود بده، اصلا هم براشون مهم نیست کجان، سرکار، خونه و...
من خودم یه بار وسط دادگاه بودم و دوس دخترم برام نود فرستاد، منم گفتم این واقعا محشره، مرسی.
@News_Hut</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/69742" target="_blank">📅 18:05 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69740">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/v2uldnpHb595ZAU8PRadbHABeShpnmkKc78I7EBTSfxHpaEGt_IQZE_85xYe_BgfkZUKT1t-_iYGe6OnZVw0FapLYLV6PJ7tWMf8OSmbxks6anjPmUywIkUDga3p0B9kCFblRY3qjPZNdccBIxqM95O9sZEAXfomp9A1B-Zej8VxsNNh4GqFCVoVNPpUSi9cPV6NHJXGbu_QOPg0hIPEqKQOYUgyln-si-gXXnYHzpjfTs7zLIzRwFlWl__hjSKpAvPHTHHY22Lc7q6ELqSN5OYZuxrM1nZhz8nnaEVPc5VyjBnBI6kC_39cCBpBDYoV72cFsEZXtMlNCPgEv2DZoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/c7e1449f7f.mp4?token=nMFEg5H2vERTLSDeWXMnKhpV9RzaJMmI8yAMqf3cbc4x1ZHnudUWIKL9724Qrpuviu-7qCpQG2TFMW2cVTObbZNQp8zsp_l0jg-fRP30mNVtaJ0Kmj65pIsTYLyaXXyFzcl08OpueIJIy5pI_KKHqgXoQBQhhycjd0j1DNZWjQ-6nMDAfaI7FGxO1FgtYEy-qffy7zxKZVrSI_pK1MrII22ETVCgYeDn1oMiH5EOkgRFk9EPWeBDpdF6iECuCCVUst1zK68tDumJOlkwtqwqEfrfRjCrRwNvi9VJJYiZjQTf11gepElF_eHS3mU9-NDzGZDKj6Xs2YhAz9X7_BfxhQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/c7e1449f7f.mp4?token=nMFEg5H2vERTLSDeWXMnKhpV9RzaJMmI8yAMqf3cbc4x1ZHnudUWIKL9724Qrpuviu-7qCpQG2TFMW2cVTObbZNQp8zsp_l0jg-fRP30mNVtaJ0Kmj65pIsTYLyaXXyFzcl08OpueIJIy5pI_KKHqgXoQBQhhycjd0j1DNZWjQ-6nMDAfaI7FGxO1FgtYEy-qffy7zxKZVrSI_pK1MrII22ETVCgYeDn1oMiH5EOkgRFk9EPWeBDpdF6iECuCCVUst1zK68tDumJOlkwtqwqEfrfRjCrRwNvi9VJJYiZjQTf11gepElF_eHS3mU9-NDzGZDKj6Xs2YhAz9X7_BfxhQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
حمله پهپادی اوکراین به دو پالایشگاه نفت در روسیه
پهپادهای اوکراینی بار دیگر پالایشگاه نفت سیزران در استان سامارا را هدف قرار دادند که در پی آن، آتش‌سوزی گسترده‌ای در این پالایشگاه رخ داد.
در حمله‌ای جداگانه نیز پهپادهای اوکراینی به پالایشگاه نفت ایلسکی در منطقه کراسنودار حمله کردند که باعث وقوع آتش‌سوزی شد.
@News_Hut</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/69740" target="_blank">📅 17:32 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69739">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b6b8444e04.mp4?token=KufL6PitJ2_Cnq6CsGzi7LAvv0neueaQKB0YnM7ZfhDPg5x3jo_XWzyZTn-pdY3fl9vE9XTMEupeuZAglyh7K8hppYb52XpXU0y2HPQuKDbWO2W8RRwVZwnQdMN8GzImh9rzVgIsQqnwTW3IsNGkMzJYzH_nqYxosakzT2APqozBjjTXAkijjdGnVfMs93GJokLtvfwsZP9QeFqb3f5dyuyqSRsj9kWlOgyxkVIY24Ze_VJT6dwoUovdTj2quWupsQGPVIGaIHo7W3GqeW8mBY9GB9IzmKbQmM2u9C6kpv5saZVrVZBLM1mEs9UHUrPz0r_b7TivZS7jB5iI2tOdc4QL-AR89WuqCHziONdAHgMCzsJqiYB17LZaGsghOiRBVlYd8nMPP8Fs9uIaalpgXvQivwN6vcZEkA6QFIv1zLxfzlW2VvaXAPvm6ggxLAQ87kHE9G2_EGJeTRZzNPfyEkMnWXxSAxneZgep27S1XLaPX7G-qZc7V4PR9rjL-29o7exq8gNPEi7ymDAYWgV4nxiewsdVRiSodg0ch7opR6-BC_70llcl4P2OKhqgmu87e9Yq8UGzZimQZknrL8RP7MhX86gzteiYb0brZAd1p-lsnGuehp7iTvmcpirbUpeHB-a0EWpDM0wQe5tLsloMSmOI-wRJb4HLJ5QQSAMipuk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b6b8444e04.mp4?token=KufL6PitJ2_Cnq6CsGzi7LAvv0neueaQKB0YnM7ZfhDPg5x3jo_XWzyZTn-pdY3fl9vE9XTMEupeuZAglyh7K8hppYb52XpXU0y2HPQuKDbWO2W8RRwVZwnQdMN8GzImh9rzVgIsQqnwTW3IsNGkMzJYzH_nqYxosakzT2APqozBjjTXAkijjdGnVfMs93GJokLtvfwsZP9QeFqb3f5dyuyqSRsj9kWlOgyxkVIY24Ze_VJT6dwoUovdTj2quWupsQGPVIGaIHo7W3GqeW8mBY9GB9IzmKbQmM2u9C6kpv5saZVrVZBLM1mEs9UHUrPz0r_b7TivZS7jB5iI2tOdc4QL-AR89WuqCHziONdAHgMCzsJqiYB17LZaGsghOiRBVlYd8nMPP8Fs9uIaalpgXvQivwN6vcZEkA6QFIv1zLxfzlW2VvaXAPvm6ggxLAQ87kHE9G2_EGJeTRZzNPfyEkMnWXxSAxneZgep27S1XLaPX7G-qZc7V4PR9rjL-29o7exq8gNPEi7ymDAYWgV4nxiewsdVRiSodg0ch7opR6-BC_70llcl4P2OKhqgmu87e9Yq8UGzZimQZknrL8RP7MhX86gzteiYb0brZAd1p-lsnGuehp7iTvmcpirbUpeHB-a0EWpDM0wQe5tLsloMSmOI-wRJb4HLJ5QQSAMipuk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌐
تریلر اولین فیلم ساخته شده با هوش مصنوعی
!
فیلم Hell Grind
اولین فیلم بلند سینمایی است که تماماً و بدون دخالت ابزارهای دیگر توسط هوش مصنوعی ساخته شده.
@News_Hut</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/69739" target="_blank">📅 17:00 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69738">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X9UI60CK1kcB5ihWJlqovHbgu8JciVtZIUUZkxlcL-gB7H5Ox_JWX2Puy1TlaP6kL2fJBSXBDZJxZg2PTpHRPtVTdgn0xPY-bubTBlZgApmyWYh5av8H0s4TyEk8CvNvc5WAsFO7N4k_bGy4_MBlBjnnMgs1W_-lvpbcxUqui4nRoVfLXJ7kjTwyRtYIGblcLyJMj-r8FvXHQxWe2HqPJIDki5EbEy9QkyaidWrDa8uvC8wbXTn3ZmpyudPKFe3eIxak4gn-p4iEAqagNisXGNf9E9xBvZq_tgzB3AIXOS1qEbTYdnuTwFU4Xnt-t4PtBijQi6cHMobr62m6YHUHgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
🇦🇪
طبق گزارش الجزیره، ایران امروز صبح به یک تانکر نفتی دیگر متعلق به امارات متحده عربی حمله کرد.
این چهارمین تانکری است که متعلق به شرکت ملی نفت ابوظبی (ADNOC) است و تنها در این هفته مورد هدف قرار گرفته است.
@News_Hut</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/69738" target="_blank">📅 16:33 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69737">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a24c34d2da.mp4?token=Ly5f1DtoYIJynpFY0NMdTSTEawI2mqj-pVWtRP_lrlv18iH9FAwFVFrP1XOA40TOuqtvXyOTV5xosD8ZfQQPD2eRJ4mgIkFOopGqRssuWqr9sWSRyc53X9VMyFOcH_PAHsCcvci99S7tGVzDB1YzQijJEv3hVfqXWlnYpzaLEPwk5xtq1XjpRgBfiqWFGMK2zF56yHCltzsf0WfI5CZTIb7kS96wsvzSeX8imrTogxBKdmzvnEyukPfoXuWGtId2-rhi_69WIbp_5C27zPp3MnXkvx14dT9Dnthglyh3Sd1hj4fc5XT6mLKj6pewLLCNxkZ6oFaOuicmVmgjGeSXKw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a24c34d2da.mp4?token=Ly5f1DtoYIJynpFY0NMdTSTEawI2mqj-pVWtRP_lrlv18iH9FAwFVFrP1XOA40TOuqtvXyOTV5xosD8ZfQQPD2eRJ4mgIkFOopGqRssuWqr9sWSRyc53X9VMyFOcH_PAHsCcvci99S7tGVzDB1YzQijJEv3hVfqXWlnYpzaLEPwk5xtq1XjpRgBfiqWFGMK2zF56yHCltzsf0WfI5CZTIb7kS96wsvzSeX8imrTogxBKdmzvnEyukPfoXuWGtId2-rhi_69WIbp_5C27zPp3MnXkvx14dT9Dnthglyh3Sd1hj4fc5XT6mLKj6pewLLCNxkZ6oFaOuicmVmgjGeSXKw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صحبت های ظریف درباره سهم ایران از دریای خزر:
@News_Hut</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/69737" target="_blank">📅 16:03 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69736">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/a9432f087c.mp4?token=i61hkNvTx9nym-SHioO0D9NxmsAyn-CCEa5iILxqkVdIXspmBZ4QZNcqOzMpneZ1yMi0L9w9-sFX1MTx-3i1cpkCeQJBn9nzBWmGgxKr6I4EhmEjC-ZNZfwYt3URNlIJkMX_6IwBm2mA2TXo8BLBE99Ul5f5hcjesG7qPYCQtWgIU0fELkTB2iaLTrllFuDcP1jKD2rdqJCJG3Fx1fYunbR6Ecuc_iFpH5Z5uOOs3lNMleuAXF1mrxheItWV-8FZug--ZsUQ9zP9Iz7hMfyAuyZuFmraMtqsEOd6UwvSzFot633IUTIvmdDnWcxfmhYJZu7KuByznxM0pGWSVVepoQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/a9432f087c.mp4?token=i61hkNvTx9nym-SHioO0D9NxmsAyn-CCEa5iILxqkVdIXspmBZ4QZNcqOzMpneZ1yMi0L9w9-sFX1MTx-3i1cpkCeQJBn9nzBWmGgxKr6I4EhmEjC-ZNZfwYt3URNlIJkMX_6IwBm2mA2TXo8BLBE99Ul5f5hcjesG7qPYCQtWgIU0fELkTB2iaLTrllFuDcP1jKD2rdqJCJG3Fx1fYunbR6Ecuc_iFpH5Z5uOOs3lNMleuAXF1mrxheItWV-8FZug--ZsUQ9zP9Iz7hMfyAuyZuFmraMtqsEOd6UwvSzFot633IUTIvmdDnWcxfmhYJZu7KuByznxM0pGWSVVepoQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یه سکانس از فیلمای قبل انقلاب و داستانِ شب جمعه
😂
اسم فیلم: لج و لجبازی
@News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/69736" target="_blank">📅 15:30 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69735">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🇮🇷
🔴
⏺
‌وزارت خارجه جمهوری اسلامی : کنوانسیون خزر منافع ایران را از بین نمی‌برد
🇮🇷
معاون وزیر خارجه:
در پی تصمیم برخی کشورهای ساحلی، پای بیگانگان در حال باز شدن به منطقه خزر است.
تصویب کنوانسیون رژیم حقوقی دریای خزر به معنای از دست رفتن منافع ایران نیست.
این کنوانسیون حضور نیروهای مسلح کشورهای غیرساحلی در خزر را ممنوع می‌کند.
تعیین خط مبدأ و حدود بستر و زیر‌بستر ایران موضوعی جداگانه است و در این کنوانسیون تعیین تکلیف نشده است.
به گفته غریب‌آبادی، اجرایی شدن کنوانسیون می‌تواند چارچوب حقوقی و امنیتی خزر را تقویت کند
@News_Hut</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/69735" target="_blank">📅 14:50 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69734">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🚨
🇮🇷
سخنگوی سپاه پاسداران:
بازگشایی تنگه هرمز تابع سازوکارها و شرایط تعیین‌شده توسط جمهوری اسلامی ایران است و ارتباطی با مذاکرات ایران و عمان ندارد.
بازگشایی آن منوط به پذیرش کامل شرایط ما از سوی ایالات متحده است.
@News_Hut</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/69734" target="_blank">📅 14:32 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69733">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🔴
قوه قضاییه:
آیت‌الله خرازی به دلیل حرف های کذب و دروغش تحت تعقیب قرار گرفت و براش تشکیل پرونده دادیم.
@News_Hut</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/69733" target="_blank">📅 13:54 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69732">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e778f30e9c.mp4?token=KWWZlgevLgHhTNSnByNLJOficaPebv4YxzGze4agNPWVXnitTekMVe2CONqa-ke7ryUxDFbbK_xZy5jrL8fPojwB0Y0w1dmoJDL455uv3IL0ekIBot4kGIHGGtu8cbjpo8oNiPzWnkKnEGQ5wsKssHM68TG4dmPdMgvIOrkghkJU7iBm0n4BNNJnQ4X8ixN_bCgYddDBrlULKdiUi0lUYzgAqkDBUdNJ45wxQVf7_zdzhuaU-U2qV7T0F8DTjupPbOEDgJlCYC6JRCkzhb11AQ-QQblje2v_GJp7kaFLwB2xun84cgY4Dl0PMceII_-2eDmnpWRsVj4TnvXaeZenTw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e778f30e9c.mp4?token=KWWZlgevLgHhTNSnByNLJOficaPebv4YxzGze4agNPWVXnitTekMVe2CONqa-ke7ryUxDFbbK_xZy5jrL8fPojwB0Y0w1dmoJDL455uv3IL0ekIBot4kGIHGGtu8cbjpo8oNiPzWnkKnEGQ5wsKssHM68TG4dmPdMgvIOrkghkJU7iBm0n4BNNJnQ4X8ixN_bCgYddDBrlULKdiUi0lUYzgAqkDBUdNJ45wxQVf7_zdzhuaU-U2qV7T0F8DTjupPbOEDgJlCYC6JRCkzhb11AQ-QQblje2v_GJp7kaFLwB2xun84cgY4Dl0PMceII_-2eDmnpWRsVj4TnvXaeZenTw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
مقایسهٔ قیمت های سال 1400 با 1405:
@News_Hut</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/69732" target="_blank">📅 13:51 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69731">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Snsi0BJBmtbMYHKr_g1F-wzOOgEqL3AhtFqCIjx90LsiK4C89LjZappvHAsrV0PSet48HTyqbwHuuQkCvLD5arTCuXunmSiNOKRvoM6cdK9WDIjqRQN4A38Xb9OiOcyy5LZWTod-CVJ8JfjiP7nu0oWCM4vzPAieaMbRqPj_17_DjUAmZ4UxYKSnHWxqD6oDjfvk9LwsFAjRWlBY-NY4JMqbT20MoLeUjMRTpz3LeQmjTXaoDjjQ1vTSnmGUj3bfm_lYkALFWyidRErM99IXwWm7jxeTE2_SAChotzHtAj2HDTAz3fkEslYVbRgqPM6f3BP80FIXP0sk8EgMz8cZFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
⏺
تعداد زیادی از سوخت‌رسان های آمریکا از ایالات متحده و اروپا در حال حرکت به سمت خاورمیانه هستند.
@News_Hut</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/69731" target="_blank">📅 13:01 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69730">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fb80381b74.mp4?token=CKCMGOyH7ab4SQ6tam3Y_7Alw-RnVLHwHKdK1eRjzoKNjIioRpCb2q_-YFGFx1l4jbGxaRd70ySltBRDX9QLB0bnX7I828aNWRjsnl7f1Le5Jy94CSF9QQ022L_BApb6n_81qPwniGM1itTXFPq3suVzBLlD_H3gzRZByMqkffSIA_Chog-OCRPS_mLphDfRAkfXRIHLbjm8VQyOG-tcoL9thf0stiqqemnkn-ziRiDdSPZgCz-Z0iSRfbE8fIbsAfQR7om2sLu0o8tsZHnSOlKdgNHTuVVZxKZCQZEv7u0-MbfA7vqvlW2wsQwnmzY3b1r_bNEWsirinTbABc3uUw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fb80381b74.mp4?token=CKCMGOyH7ab4SQ6tam3Y_7Alw-RnVLHwHKdK1eRjzoKNjIioRpCb2q_-YFGFx1l4jbGxaRd70ySltBRDX9QLB0bnX7I828aNWRjsnl7f1Le5Jy94CSF9QQ022L_BApb6n_81qPwniGM1itTXFPq3suVzBLlD_H3gzRZByMqkffSIA_Chog-OCRPS_mLphDfRAkfXRIHLbjm8VQyOG-tcoL9thf0stiqqemnkn-ziRiDdSPZgCz-Z0iSRfbE8fIbsAfQR7om2sLu0o8tsZHnSOlKdgNHTuVVZxKZCQZEv7u0-MbfA7vqvlW2wsQwnmzY3b1r_bNEWsirinTbABc3uUw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یه آخوند
:
قبل از انقلاب باید شب و روز میدویدی تا خودتو خانوادت از گشنگی نمیرید،الان وضع مردم خوبه.
وسط جنگ با ابرقدرت ها واسه خودشون میرن تفریح و در آسایش و آرامش و کاملا شاد هستن.
@News_Hut</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/69730" target="_blank">📅 12:31 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69729">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fce1bb2a9c.mp4?token=gOKKmyKy2RTyIq8tgPKFNoGWid-ftOO2a7q26qO1ruoXEcCG0LVDUiajubGwP8KecQWVrbsYKGC315MaHZrAPR1tma-h_5yixVLK2ASPCKqk2h1SejO4OPpHKRHfus6TaqN7ehZDdJ2ZIf0YSFfML57cPlIjTPWU1aIo6_Cp1d3wCVL-HiGNyEkAx0D7uU1PzErP7dTk_T0I95G9E_pQnk7pw-EEY6T3GUR8XsUBvZm-wMWovkTX0k6u7iMHhrf9F_aYAg6V0Hwdz6JadSPBC6s7schTiSVYLZYOKaa0wsd07bSCuvgADF9oLTz1DURwPjlr8WMUtqmljNgZXBS2fg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fce1bb2a9c.mp4?token=gOKKmyKy2RTyIq8tgPKFNoGWid-ftOO2a7q26qO1ruoXEcCG0LVDUiajubGwP8KecQWVrbsYKGC315MaHZrAPR1tma-h_5yixVLK2ASPCKqk2h1SejO4OPpHKRHfus6TaqN7ehZDdJ2ZIf0YSFfML57cPlIjTPWU1aIo6_Cp1d3wCVL-HiGNyEkAx0D7uU1PzErP7dTk_T0I95G9E_pQnk7pw-EEY6T3GUR8XsUBvZm-wMWovkTX0k6u7iMHhrf9F_aYAg6V0Hwdz6JadSPBC6s7schTiSVYLZYOKaa0wsd07bSCuvgADF9oLTz1DURwPjlr8WMUtqmljNgZXBS2fg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
📰
مراد ویسی تحلیلگر ارشداینترنشنال: جنگ جهانی سوم در راهه!
هر چقدر اتفاقات و شرایط رو بررسی میکنم، دقیقا مثلِ قبل از جنگ جهانی اول و دومه.
توافق و تفاهم نامه همش کشکه، هیچکس تو خاورمیانه حاضر نیست سلاحش رو تحویل بده، یه جنگ عظیم و جنگ جهانی سوم در راهه!
@News_Hut</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/69729" target="_blank">📅 11:58 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69728">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/41f0d554f1.mp4?token=HFhR9pkGXz7t5EK1Tai-9_1AuCpfauHVahDCYYi7fHotvhSvqnq3MTPX2JfRR75TxdquT4wnhur9iKudOE_dyv9pYL_s7-WeBxYkEC8SGdzjmUbQ2vjyHc03wKiEh4SEjjh4Wo-dJCcmaDznPawwx99h16fJiMNoCVNr9B0mfmcTGzcu4Fy9IatnKf4_NkobVLJt9LJkSBcGctJ692evoTUDMNYAUVPsaAxB48AxapDVKm2I9M4mEl11AxnVD6nhEQtZDcmhOl_KfPaFj_0LIkbX-4fFJCmjD0fPb1jP9KXA6cHt3e0CQcXDEaIWBSkIwnshAWI2ylqXe0C1A4KImA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/41f0d554f1.mp4?token=HFhR9pkGXz7t5EK1Tai-9_1AuCpfauHVahDCYYi7fHotvhSvqnq3MTPX2JfRR75TxdquT4wnhur9iKudOE_dyv9pYL_s7-WeBxYkEC8SGdzjmUbQ2vjyHc03wKiEh4SEjjh4Wo-dJCcmaDznPawwx99h16fJiMNoCVNr9B0mfmcTGzcu4Fy9IatnKf4_NkobVLJt9LJkSBcGctJ692evoTUDMNYAUVPsaAxB48AxapDVKm2I9M4mEl11AxnVD6nhEQtZDcmhOl_KfPaFj_0LIkbX-4fFJCmjD0fPb1jP9KXA6cHt3e0CQcXDEaIWBSkIwnshAWI2ylqXe0C1A4KImA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
نویسنده امریکایی
:
ایران مهم ترین مهره روی صفحه شطرنجه
!
@News_Hut</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/69728" target="_blank">📅 11:31 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69727">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🇺🇦
❌
🇷🇺
نیروهای ویژه دریایی اوکراین از تاریخ ۶ جولای تاکنون، به ۲۱۸ شناور در دریای سیاه و دریای آزوف حمله کرده‌اند. همچنین، بین ۱ تا ۸ آگوست، ۱۲ شناور دیگر از ناوگان سایه مورد هدف قرار گرفتند.
@News_Hut</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/69727" target="_blank">📅 11:30 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69726">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">app (7).apk</div>
  <div class="tg-doc-extra">53.1 MB</div>
</div>
<a href="https://t.me/news_hut/69726" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">⚠️
#پیشنهاد_ویژه
⚠️
🔥
حتما ویدیو‌ آموزشی بالا رو‌ببینید بازی ساده و بسیار شیرینی که راحت میشه میشه ازش کلی پول درآورد
👌🏼
دنیای سرگرمی و بازی های جذاب رو در این‌اپلیکیشن تجربه کنید
⭐</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/news_hut/69726" target="_blank">📅 11:29 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69725">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dc7f1c8ee4.mp4?token=Q9xnvaSFcYLUihe13a_HGpXjJzXKaQ_CPbM_G9vTDCcTXDqDMVuivJE_Hk6A0pmZtPRgBaZkuCLfsZNQWdkrYEHikmZpUy3aEpSyYCGoJemd5phwUWkkK5l4hQZxIkaBQ5uD7sg9i-rwit7ejmn5u-alTfBa_xWRNW9lIpZw0ytuftbRmy7hfcstrL4BZqyLHQfJAELdvQCHffIz6GQbjTSkw2HLlwxF5JW16B9e88U-X-6ztftc4KntVu4DPGl4PIY677QuNpMi3TYa_IpaBCAYo-AOlKHKkT1yZRGwLIOIJeKAWac7ugRHrSk1t205qPOhX_DZJ_Lg06gPIlNm1g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dc7f1c8ee4.mp4?token=Q9xnvaSFcYLUihe13a_HGpXjJzXKaQ_CPbM_G9vTDCcTXDqDMVuivJE_Hk6A0pmZtPRgBaZkuCLfsZNQWdkrYEHikmZpUy3aEpSyYCGoJemd5phwUWkkK5l4hQZxIkaBQ5uD7sg9i-rwit7ejmn5u-alTfBa_xWRNW9lIpZw0ytuftbRmy7hfcstrL4BZqyLHQfJAELdvQCHffIz6GQbjTSkw2HLlwxF5JW16B9e88U-X-6ztftc4KntVu4DPGl4PIY677QuNpMi3TYa_IpaBCAYo-AOlKHKkT1yZRGwLIOIJeKAWac7ugRHrSk1t205qPOhX_DZJ_Lg06gPIlNm1g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🖱
اگر
#تندو
تیز هستی اینو ببین
💵
💰
✊
این بازی فقط سرعت عمل بالا میخواد
😍
🟢
ویدیو
#آموزش
بازی AVI رو براتون گذاشتم خیلی راحت با سرعت عمل بالا بدون ریسک کلی پول دراورد به همراه
🤩
🤩
% شارژ اضافی
🔥
💖
حتما ویدیو رو تا انتها ببینید
💻
لینک سایت بازی:
💻
betinja.bet
💻
betinja.bet
🌐
کانال بونوس های رایگان
r17
@betinjabet</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/news_hut/69725" target="_blank">📅 11:29 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69721">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6dab2dda1d.mp4?token=l-ruCIEjcWMBVJySHVF3VYyxqD_7Zocz1mS3fCXm342iW4Z1m3rIsnz4q7uBBjAxcyTfoHnBBIfbrvwr139fzibrsGtPyVcQvMj9XsyKPsHy-3WJsmk9S7Qr7VSxBySuSO4n3x11TCFglVOxWHiMYxvp_Djp3iVlEcl4l2YqP2OPXBB0QmUyFjeOuF0cXmzHdfDIB6LTtQbNstPmFLG4D-GBSbAlkfFDIBZ_tp6N3RCW0TJLRIoRtfqJfofVJA5-OSwCtjRZIR20R0fDC4ZbKEbLp8Otp6Vml2R2u1GGCKr_53wLCEd8DyyEqs8UGyktPyC6R0bORAgQicRyCJ0oyQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6dab2dda1d.mp4?token=l-ruCIEjcWMBVJySHVF3VYyxqD_7Zocz1mS3fCXm342iW4Z1m3rIsnz4q7uBBjAxcyTfoHnBBIfbrvwr139fzibrsGtPyVcQvMj9XsyKPsHy-3WJsmk9S7Qr7VSxBySuSO4n3x11TCFglVOxWHiMYxvp_Djp3iVlEcl4l2YqP2OPXBB0QmUyFjeOuF0cXmzHdfDIB6LTtQbNstPmFLG4D-GBSbAlkfFDIBZ_tp6N3RCW0TJLRIoRtfqJfofVJA5-OSwCtjRZIR20R0fDC4ZbKEbLp8Otp6Vml2R2u1GGCKr_53wLCEd8DyyEqs8UGyktPyC6R0bORAgQicRyCJ0oyQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این روزها قبل از ورود به هر بالا پشت بومی، سعی کنید در بزنيد؛
چون قطعا یکی اونجا هست که داره سعی میکنه سیاه بشه
😔
@News_Hut</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/69721" target="_blank">📅 11:00 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69720">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7aa229942a.mp4?token=s5uoDoh-jePzlNjxHGRS8262SoSl62fci6nlOsSYi0mOUqBn47MFXaORjNtQFhHq-junF_6YxfjYqtQasFGbW1xDTdmaokIKr6ti1u0GG6af0lpSTw-H24YWhZQSCeFf1njJp9j95sYd3AXEjhU3fNNqeJSNS6wzjCAY4Ewrpo8k5pUovmSyYwbFLy87FtrBDKmA0AnzO3wBIQZh8JZEYOpxQ4iSFlJIv-EqucwGrLLyRQQc3pWUjwBDaxKRsv83uRDxXiNKB5TPWKDEI-JEogwCjqEGeMLeRASpKyb3IKNy7HovJfIm_6wT4dI8M4iOEDL7_Kg7xzjebWR-ktTUvA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7aa229942a.mp4?token=s5uoDoh-jePzlNjxHGRS8262SoSl62fci6nlOsSYi0mOUqBn47MFXaORjNtQFhHq-junF_6YxfjYqtQasFGbW1xDTdmaokIKr6ti1u0GG6af0lpSTw-H24YWhZQSCeFf1njJp9j95sYd3AXEjhU3fNNqeJSNS6wzjCAY4Ewrpo8k5pUovmSyYwbFLy87FtrBDKmA0AnzO3wBIQZh8JZEYOpxQ4iSFlJIv-EqucwGrLLyRQQc3pWUjwBDaxKRsv83uRDxXiNKB5TPWKDEI-JEogwCjqEGeMLeRASpKyb3IKNy7HovJfIm_6wT4dI8M4iOEDL7_Kg7xzjebWR-ktTUvA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
رجب صفروف، عضو تیم روسیه در مذاکرات رژیم حقوقی دریای خزر، (مرداد1397):
همه ما انتظار داشتیم ایران درخواست پنجاه درصد بکند. قانونی هم بود.
اما جلسه اول یکباره جمهوری اسلامی گفت تقسیم برابر بین پنج کشور، یعنی کمتر از بیست درصد.
برای ما عجیب‌ و غریب بود که چجور ایران دارد از حقوق خودش گذشت می‌کند.
@News_Hut</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/69720" target="_blank">📅 10:33 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69719">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NKePf7_ES0YQuML-NOR3HQgdX2n5_ZtG3takVn83vKo6yXknhlabx5ewkFBBApVf7D2pc-4o0kHVjovCCaIOn9wdFtel2HXQkfIQIQZaehD71n1w79x-YSUGp6Ek68w-jZXxwkXiLUPwqgTTQmRTBzqad7L0HRzjkXyenTgodwzLh0Yu5it17NiPI41b-o69bP6-l17o6DPCV9TtPeL3cLP3gpJmP_YQ80i8BJy7bMqdiEGDlK0ezOpuLMKX1p2sW6k1BOy2Ku5ODIBE89cJHLprbxcoyieISelHa0NI6Sw3d58PyJ0RezucWbAz0lUL6WZYyt9SgiSgXKbM7L1FJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
سپاه ساعاتی قبل یک کشتی دیگه رو توی تنگه هرمز هدف قرار داده؛
گزارش‌ها حاکی از آن است که ایران به کشتی‌ای در تنگه هرمز و نزدیکی سواحل عمان که قصد عبور بدون مجوز را داشت، حمله کرد
ه
است.
یک شناور تخصصی که برای مقابله با نشت نفت و اطفای حریق طراحی شده، در منطقه‌ای که نفتکش هدف قرار گرفته، در حال فعالیت است.
@News_Hut</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/69719" target="_blank">📅 10:14 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69718">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e9bc484b9d.mp4?token=S68NhGdN_8PRQ-Krj1Gf5A23F9omq8q6H4CGCCnpM5wVdsGjBWjOL9Sxseq5akbOroXDJhigxzzAqoR3MyUJ4FZVPM8F5UDpJUebuw9YBOQEqoml6mBqH5kly_c9qfMg6UY3nkVAdL8ocpsZXD-p7xRrigb-9jpkxoeNw-0RNrJQvYtTpbUe1tOdsJBsbB9NX7Ds2Ho7ctxWiA5jGl3Lh3-m0KT1lDa1NaDh0O7yZoyMJz4_k-esxMyCxj4dMicolzieL9dkOLOwfMDVxu1Xgq4kNJ-tmna0ZznMHHBWvLQBQj5BjlxRavI7-G4Gep5FGnXz_SoTg4fBJp4dUUphaQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e9bc484b9d.mp4?token=S68NhGdN_8PRQ-Krj1Gf5A23F9omq8q6H4CGCCnpM5wVdsGjBWjOL9Sxseq5akbOroXDJhigxzzAqoR3MyUJ4FZVPM8F5UDpJUebuw9YBOQEqoml6mBqH5kly_c9qfMg6UY3nkVAdL8ocpsZXD-p7xRrigb-9jpkxoeNw-0RNrJQvYtTpbUe1tOdsJBsbB9NX7Ds2Ho7ctxWiA5jGl3Lh3-m0KT1lDa1NaDh0O7yZoyMJz4_k-esxMyCxj4dMicolzieL9dkOLOwfMDVxu1Xgq4kNJ-tmna0ZznMHHBWvLQBQj5BjlxRavI7-G4Gep5FGnXz_SoTg4fBJp4dUUphaQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
شادمهر عقیلی، قطعه‌ی گل یاس از البوم مسافر رو که سال 1377 منتشر کرده بود، بعد از 28 سال دوباره بازخوانی کرد و تو اینستاگرام منتشر کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/69718" target="_blank">📅 09:58 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69717">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0959732695.mp4?token=XKpaTZAZtTcNxpXQhdAj0u7O0SayBQbAa7RZMTBQBaVtZAq0CMqQH8I1PUywmR55lt6F67p5N39VXdieHadnovMohCb8hPL7pquI76jjWkFk5-wf3-DOh80NaWvDn8GDd3tEZeVzxAoMO8hEJhKH4gy1zXkdoi1JsJgnNxAURqN2k0NjAXRkBKFC8NH6FRLHi73bspsfdSKq5yx5hWSondAe2htx5P-DYz2lt_iy6TkwOrX7k2Pbd4o1oPTKMsbd_IjbSZndwyVkvF8aOyt_p46eib2sI-1jEHkKjvdyF8Azm1MPjSG1dNJOUyz_LNTlJUOC50VWNoPAIWLW60u6Sg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0959732695.mp4?token=XKpaTZAZtTcNxpXQhdAj0u7O0SayBQbAa7RZMTBQBaVtZAq0CMqQH8I1PUywmR55lt6F67p5N39VXdieHadnovMohCb8hPL7pquI76jjWkFk5-wf3-DOh80NaWvDn8GDd3tEZeVzxAoMO8hEJhKH4gy1zXkdoi1JsJgnNxAURqN2k0NjAXRkBKFC8NH6FRLHi73bspsfdSKq5yx5hWSondAe2htx5P-DYz2lt_iy6TkwOrX7k2Pbd4o1oPTKMsbd_IjbSZndwyVkvF8aOyt_p46eib2sI-1jEHkKjvdyF8Azm1MPjSG1dNJOUyz_LNTlJUOC50VWNoPAIWLW60u6Sg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
مسعود پزشکیان:
تا وقتی میشه حرف زد چرا جنگ؟
ما با همین گفت و گو تونستیم جلوی جنگ لبنان رو بگیریم. (اسرائیل از همون موقع تا الان تقریبا هر روز داره لبنان رو میزنه).
تونستیم محاصره رو برداریم. (ایران درحال حاضر تحت محاصره دریاییه)
تونستیم پول‌هامون رو برگردونیم. (هیچ پولی از پول‌های بلوکه شده به کشور برنگشت)
تونستیم قسمتی از تحریم‌ها رو حذف کنیم! (درحال حاضر تحریم ها بیشتر از قبل جنگ شده)
بعضی‌ها تو داخل کشور فقط میخوان که ما بجنگیم
،
اتفاقا اسرائیل هم همین رو میخواد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/69717" target="_blank">📅 09:32 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69716">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">👑
آخرین مصاحبه شاهنشاه آریامهر محمدرضا پهلوی با دیوید فراست (پاناما1980) زیرنویس فارسی:
@News_Hut</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/69716" target="_blank">📅 09:01 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69715">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">app (7).apk</div>
  <div class="tg-doc-extra">53.1 MB</div>
</div>
<a href="https://t.me/news_hut/69715" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">⚠️
#گل_با_پوچ
راحترین بازی پولساز
⚠️
🔥
حتما ویدیو‌ آموزشی بالا رو‌ببینید راحتو سریع برنده شو
👌🏼
💖
مرجع
بازی های روز دنیا در ‌پلتفرم جهانی بت اینجا
⭐</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/69715" target="_blank">📅 02:07 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69714">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c15f45ab1f.mp4?token=oZv-kdTK_hxws2HJYNeuyFDD0hCGHhnfKgeiK6-Rjdu3q-gDs1s4vHTovYH1WXUOMji-bNZZ3pCQWRb524CUpS4l378bvetpDyn195zusbm9SKh7kW2_PWg8yKylYH3KoOmLCr1X9CRHkgd-M7ommoSxy9JFinPCKBeU4nTCbCEaV_KUGPtfHKEAXDRURH7h_fSY8GzMLqV_djCO8h6EY6LSynOx-l45oFp-Xd0NXLyzNvCD08fNEtRFNINmOVZLgiOdxuCqAxqiUO0j5eRQ6eD7h9FtkDtIeO-9YM5tfTjUhfaiczo6m3LHUmheCiJfoZ42gvfCQ34zxHMnFCZTxw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c15f45ab1f.mp4?token=oZv-kdTK_hxws2HJYNeuyFDD0hCGHhnfKgeiK6-Rjdu3q-gDs1s4vHTovYH1WXUOMji-bNZZ3pCQWRb524CUpS4l378bvetpDyn195zusbm9SKh7kW2_PWg8yKylYH3KoOmLCr1X9CRHkgd-M7ommoSxy9JFinPCKBeU4nTCbCEaV_KUGPtfHKEAXDRURH7h_fSY8GzMLqV_djCO8h6EY6LSynOx-l45oFp-Xd0NXLyzNvCD08fNEtRFNINmOVZLgiOdxuCqAxqiUO0j5eRQ6eD7h9FtkDtIeO-9YM5tfTjUhfaiczo6m3LHUmheCiJfoZ42gvfCQ34zxHMnFCZTxw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚠️
#آموزش
گل یا پوچ آنلاین با افراد واقعی
🟢
حتما وبدیو آموزشی رو‌تا انتها ببنید راحتتربن بازی پولساز بدون ریسک و بدون پول گل یا پوچ بازی کن
با هر شارژ
2️⃣
1️⃣
🔣
موجودی خالص میگیری و با موجودی اضافیت میتونی کلی پول دربیاری
🔥
💻
آدرس سایت مورد
#‌اعتماد
ما:
🌐
betinja.bet
🌐
betinja.bet
کانال بونوس های رایگان
a16
@betinjabet</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/news_hut/69714" target="_blank">📅 02:07 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69713">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/srubNq0gDrQ0nHfNShjJeD1L3FsZTO6LByN63alMwxRSqjpsYcBShqRwQSvrYZj-bF-0Iev_7KxgJJxHYIrI1ALu4vxPnx0ivbCjzbZicnW4UySTG128KjUDe7pCIFEbMsmhkGNuvDnMMcPprkJhUERAraJcQGOkHvBIaw23w2W_v8OxvPbacQcwrKV4vn-uQX-qNGzinTpN6MIu6IjlKVGYhfC0sG0WA6oPJAQ3BfwgTTrfRLce3hZGuT6HWtMQbFmJa8cOjRaSr4llQniTnbbGwYMQPMZhJc6Lcan6jZQpNhJGqqEgctwvHBCst7AYr-oynu0keu4S372-LSfyHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
توییت لارا لومر در جواب قالیباف:
"جمهوری اسلامی رئیس جمهور ترامپ را مسخره می‌کند!"
یادآوری روزانه شما مبنی بر اینکه مسلمانان بازیگران بدذات هستند و نمیشود با آنها مذاکره کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/news_hut/69713" target="_blank">📅 01:40 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69712">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/66931f1c30.mp4?token=RitnBZDlFB7Go9zViJ54CY8TVwHEpi3VpX1cMYteLdkrWhsUpidw_sLQAPnpkvTm4cc_AVdNEbdyzRZLd6BQqerjFws5zcL47JA_eZAtYAmah7fHd0qcMV0tXVt2zSI2nzQPucuJ85ndCpPXDFm19jXB0vz6AyC9xwMx9ppfG-IFARzqR3rUm9MHXYbOQ7O1jDzTPBmaM4tlXDU_BIOJU0EyJUnSpqULOXU0a45ewslqdqP9bDEMI1tF8WLKL1JjCl0Dk6OyK7LnKctpkC7vaC6I4hc4ij11SiUf0ANgvJRb_80EqrK1IhlCkXP2fc9daRTleBioYwU01GnU5IDkUg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/66931f1c30.mp4?token=RitnBZDlFB7Go9zViJ54CY8TVwHEpi3VpX1cMYteLdkrWhsUpidw_sLQAPnpkvTm4cc_AVdNEbdyzRZLd6BQqerjFws5zcL47JA_eZAtYAmah7fHd0qcMV0tXVt2zSI2nzQPucuJ85ndCpPXDFm19jXB0vz6AyC9xwMx9ppfG-IFARzqR3rUm9MHXYbOQ7O1jDzTPBmaM4tlXDU_BIOJU0EyJUnSpqULOXU0a45ewslqdqP9bDEMI1tF8WLKL1JjCl0Dk6OyK7LnKctpkC7vaC6I4hc4ij11SiUf0ANgvJRb_80EqrK1IhlCkXP2fc9daRTleBioYwU01GnU5IDkUg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
مسعود پزشکیان:
ما هیچ امتیازی به آمریکا ندادیم!
آمریکا به تعهداتش عمل نمی‌کنه؟ خب اون موقع ما هم نمی‌کنیم.
تو جلسه شورای امنیت، 12 نفر از 13 نفر از این توافق دفاع کردن و رای دادن، چرا؟ چون منطق و عقل اینو حکم می‌کنه.
کسی که نمی‌فهمه همینجوری میگه بزن! خب این تبعات داره...
من از شهادت نمی‌ترسم که هیچ، واسم افتخارم هست ولی اینکه نتونم مشکل مردم رو حل کنم، واسم قابل قبول نیست.
@News_Hut</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/69712" target="_blank">📅 00:49 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69711">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/372d7e9f3e.mp4?token=UPPPJ1xuYTDz46cpn7P7EO1b0N9Ny5AoetTmIj4u2sey0UBm7Y0BfWmQAU09KeLAC-1a2NkBOIbfGMeV3sUiyiYLzJ392wZvTwVjVxp-MzZPPfDHw6Sdhq4LoMfZ7eQyPYjePojkN7jp2-k3XgJP_4FnaRZXAiKmeqFHE_XYNmgoNSJuo2I0FoxYvRQEDIfaDwMLUeaBgPSo36oAQWuq6L8dTmOaJyh9QILvBeOdWVsx0gBl1IvIlFSy1ZnSwnD5SYq7cy731wkb5KSrBEfCBQtXZyLqLgh80JQWc4eU-NQaNjpvVR4aJS8vGn4He-aOChlje1ZqgKvs3FJOr5Qyzw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/372d7e9f3e.mp4?token=UPPPJ1xuYTDz46cpn7P7EO1b0N9Ny5AoetTmIj4u2sey0UBm7Y0BfWmQAU09KeLAC-1a2NkBOIbfGMeV3sUiyiYLzJ392wZvTwVjVxp-MzZPPfDHw6Sdhq4LoMfZ7eQyPYjePojkN7jp2-k3XgJP_4FnaRZXAiKmeqFHE_XYNmgoNSJuo2I0FoxYvRQEDIfaDwMLUeaBgPSo36oAQWuq6L8dTmOaJyh9QILvBeOdWVsx0gBl1IvIlFSy1ZnSwnD5SYq7cy731wkb5KSrBEfCBQtXZyLqLgh80JQWc4eU-NQaNjpvVR4aJS8vGn4He-aOChlje1ZqgKvs3FJOr5Qyzw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
ارژنگ امیرفضلی
:
بالا برید پایین بیاید، برید چپ برید راست، مذاکره کنید جنگ کنید نکنید:
🔻
هیچ چیزی به قبل از ۱۸ و ۱۹ دی برنمیگرده
.
@News_Hut</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/69711" target="_blank">📅 00:03 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69710">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🇺🇸
ترامپ در گفتگو با خبرنگاران:
ما افراد بسیار زیادی داریم، اگر بخواهم درباره همه صحبت کنم، تمام روز طول می‌کشد.
اگر بتوانید به سرعت سوالات خود را مطرح کنید، از شما سپاسگزار خواهم بود، زیرا ما یک جنگ را پیش می‌بریم، متوجه هستید؟
این عذری است که من برای ترک این جلسه کمی زودتر ارائه می‌دهم.
@News_Hut</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/news_hut/69710" target="_blank">📅 00:00 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69708">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/55d4300472.mp4?token=P9h9mzBAlhQ3i0EQBSuQAVOE1dXQYcGKaoFsPog2O50HwXVpxQCwBLcpvIWW9nQrMBDtP15wCVzbh8qXiGnu_PQRlkassFAmLOpgm1tljxhgnKshddVoM6gPUQjTm-MmAjeWS43DaLFwDpTyc6oX6s9U0NfTss0nxXXMaVqIRDSX0KbMG1nbxgPsVAJ1nQshx4RrZ66BTwbU46bm-Cr2S4-P--8vA1Qj_QvwJPb7CjY_fS9G6oCn6Z2wH5tLUIU8O6HogqB_b5M2pGs5DDOvxxJ1LEYqQ8QLbRItfKRR9j3MS-pkT1u8dlZV101Iqg5itsDteMYTdBor7AD9vmY3Jw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/55d4300472.mp4?token=P9h9mzBAlhQ3i0EQBSuQAVOE1dXQYcGKaoFsPog2O50HwXVpxQCwBLcpvIWW9nQrMBDtP15wCVzbh8qXiGnu_PQRlkassFAmLOpgm1tljxhgnKshddVoM6gPUQjTm-MmAjeWS43DaLFwDpTyc6oX6s9U0NfTss0nxXXMaVqIRDSX0KbMG1nbxgPsVAJ1nQshx4RrZ66BTwbU46bm-Cr2S4-P--8vA1Qj_QvwJPb7CjY_fS9G6oCn6Z2wH5tLUIU8O6HogqB_b5M2pGs5DDOvxxJ1LEYqQ8QLbRItfKRR9j3MS-pkT1u8dlZV101Iqg5itsDteMYTdBor7AD9vmY3Jw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
خرازی(برادر زن مسعود خامنه‌ای):
فتوا میدم بی حجاب هارو بکشید اصلا رحمی نکنید
.
هرکی خواست مقابله بکنه اونارم بکشید
.
این دولت شیطانیه اینارو هم جلو اومدن بکشید
.
این دولت شیطانی شده زیر نظر آمریکا ما باید به حکومت اسلامی سابق برگردیم
.
اسلام همینه باید ضربه بزنیم و ضربه رو دریافت کنیم
.
@News_Hut</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/news_hut/69708" target="_blank">📅 23:53 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69707">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a717b4bbc3.mp4?token=YJb7JG1hNbZRBajeYzVdgB3_e5VC7SbufVz90vLlQVzWoAPagBqkADFtopJPv6SIpTzZCzaBrncPqOzY3feOzB5XXkqcIyo1hV8YSd0NLSN2nvUfos_AhjIt1J3FOFkNyoQVQJMUEnTvImRxcXvtA1OIhucyQv5R1qB2xoRe8ucOhER5nsdk2RDUlchn_cC202PU9xUuMmIam0smfU3Pp-ueTXpALO7eMYqSPmRaFaD-BM0yCO17KftmlSSQYK8lc0_3Uwz8g45GrU08bszRItaG4BkTMuNimDoJTH_u9jBCPcUxpV4r2lrMwwR7Q2L6M3Oxek82dDTaRJ6ykWc84Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a717b4bbc3.mp4?token=YJb7JG1hNbZRBajeYzVdgB3_e5VC7SbufVz90vLlQVzWoAPagBqkADFtopJPv6SIpTzZCzaBrncPqOzY3feOzB5XXkqcIyo1hV8YSd0NLSN2nvUfos_AhjIt1J3FOFkNyoQVQJMUEnTvImRxcXvtA1OIhucyQv5R1qB2xoRe8ucOhER5nsdk2RDUlchn_cC202PU9xUuMmIam0smfU3Pp-ueTXpALO7eMYqSPmRaFaD-BM0yCO17KftmlSSQYK8lc0_3Uwz8g45GrU08bszRItaG4BkTMuNimDoJTH_u9jBCPcUxpV4r2lrMwwR7Q2L6M3Oxek82dDTaRJ6ykWc84Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
تحلیل جدید محمد باقر خرازی از حمله مسلمانان به هند و چین در آینده:
@News_Hut</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/news_hut/69707" target="_blank">📅 23:15 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69706">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/6ea65bf65c.mp4?token=DppzahPxWmLf5c16XEg_iaj5W_qJMOIqXcteb-7isI8KfuMzgeJgi2nAUi9bGMQL9ewDdC6hb2b0zfT3Sp5a6dusNj_2AEn988ed5IdMz4P4IC_nX8xG4QQvO1GNAqQjjfn0cVqINecrn5z8x_2fVSLecDwj59m0yz7DqdDz35Z7rrDtR0bv1vsdJTbwi8isH09HOjVulR_39fKtuxie32sB0GrQmJmWbYDw7HAiLlhFoyWG6KSXLa1QN6gB95n0ufuV2brPGAbrH8NNyjhbFMAzx-2mPYcO3fUZzXUTURzaBNCrfzHFE302huAr27ggU-oB0cQCjEVLPFJkcx19bw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/6ea65bf65c.mp4?token=DppzahPxWmLf5c16XEg_iaj5W_qJMOIqXcteb-7isI8KfuMzgeJgi2nAUi9bGMQL9ewDdC6hb2b0zfT3Sp5a6dusNj_2AEn988ed5IdMz4P4IC_nX8xG4QQvO1GNAqQjjfn0cVqINecrn5z8x_2fVSLecDwj59m0yz7DqdDz35Z7rrDtR0bv1vsdJTbwi8isH09HOjVulR_39fKtuxie32sB0GrQmJmWbYDw7HAiLlhFoyWG6KSXLa1QN6gB95n0ufuV2brPGAbrH8NNyjhbFMAzx-2mPYcO3fUZzXUTURzaBNCrfzHFE302huAr27ggU-oB0cQCjEVLPFJkcx19bw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏸
یکی از قشنگ‌ترین ویدیوهایی که درباره توصیف وضعیت جامعه در حال وایرال شدنه:
@News_Hut</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/69706" target="_blank">📅 22:27 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69705">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SdGNqVqbkYK228xg0V8-JCcXmrfvRwclO_T_zPmNfcOVuaaJcqE0mZG6Y4teyQjbHKujaUokhWWTMBAAnFptLzv1zVG0wDrlLy0dpTvw-gVDO4ps1_6B2Wgros5OGkwE64OttB2DJjWMZRaJ0nJKiho1rUlnRhwsop9pumCrctlLju8WIwOvQpdtHGEaPaoXXDveZaT73TFns0enmmJEHxDCY1hsSQNXdxCy7JSsLUfxOmqXnbD52qGvPqPCoHT1UiJaQdO9c5Xur5qN0pjoBAKs_hf6bQXki1wT5x148Ak4WzVVkGysOuDne5oz7QINW-geV4mHZuuSPv_EdIfnag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
عباس عراقچی:
نیروهای مسلح قدرتمند ایران امادگی و اقتدار خودشونو درباره بهترین ارتش جهان نشون دادن
هنگامی ک مسلمون ها کنار هم متحد باشن میتونن درباره هرچالشی از بیگانه با قدرت و قاطعیت ایستادگی بکنن
زمانش فرا رسیده که تنها بخودمون متکی باشیم و برادری واقعی رو در پیش بگیریم
@News_Hut</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/69705" target="_blank">📅 22:25 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69704">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-text">6 شب و 6 برد پشت هم
✅
من به پول هیچکدومتون نیاز ندارم و قرار نیست چیزی بهتون بفروشم  آماری رو رقم زدم که حتی تازه وارد هم میفهمه این آمار کار هرکس نیست
🚀
g16 https://t.me/+5fvta-uF4QA3ZDY0 https://t.me/+5fvta-uF4QA3ZDY0</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/69704" target="_blank">📅 22:25 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69703">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ufmmAbJ8ZGowHNs99PaUt5g2FjcyuvR5JyAOQUrUA4HzXgkw6EU7E4IOPX8Tn_cx6nL6zsPjDjVeDE275TCLCRsMlpP-fXoEgB1jfgcjoF0OHsG9lDMr_Swr52Fu9UaYHMCqcm_GHnll0-KfljZZFqbGp6P74SiAPwUn8fUkGpz6BrTn74aUXQUCyTXZr65irISCN0nfPTvx7olFqaGAS2r2zqj3ILwJU5b0aaFXqjtpW4sYATpX02X0yW6742kUv2GYwG8cHeWli8vqA-lBH_WFtva3Ekek4GP0r1NYHuo-ckdwama1dmDdqiBuDfQ4hSGH-wpX9LAN6WZr8vUOPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">6 شب و 6 برد پشت هم
✅
من به پول هیچکدومتون نیاز ندارم و قرار نیست چیزی بهتون بفروشم
آماری رو رقم زدم که حتی تازه وارد هم میفهمه این آمار کار هرکس نیست
🚀
g16
https://t.me/+5fvta-uF4QA3ZDY0
https://t.me/+5fvta-uF4QA3ZDY0</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/news_hut/69703" target="_blank">📅 22:25 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69702">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B-8_yn7uVRMGBGHKlTrGMYq20qEWYnH9kf5nJ7Hd9dvQsDEJ6B2mMsY39QNgtEhzdojWkDAXIWhYq4sbXMx4-unwUINVqbnJEtd0Ii9eb2NOEb4RPDUaJM8w8Daq7k-sDchndLMmNT3VXb8OIccSv-0XRjbo5NLtMpCAGxW7eoTNMslevmfZkqSg2g2PSBBcFYNpBDlXsT0ZAn6m_BKd8VQtRMZ7lhZ5nlk_mCDrkAR9q0QHsS2rO_AK_NbYAi-5WUiuLvsVYpJmooiwuWMcSb1zroiWED88DzCMT94HNAKQY5HKUGGTGqTiwB2qOBL--Y41n5xj4nTAM0hfjLyVYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
باراک راوید:
مذاکره‌کنندگان ایرانی منتظر تایید نهایی از سوی شورای عالی امنیت ملی ایران در مورد توافق آتی با عمان و ایالات متحده هستند. این دیپلمات ادعا می‌کند که انتظار می‌رود شورای عالی امنیت ملی این توافق را تصویب کند.
@News_Hut</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/69702" target="_blank">📅 21:40 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69699">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gFVBBcXo6WEwS53QLXcab3m-msRGPwA_-OTxP5R5-ElIr6BdqOUeHu0JayeAjSuJdZ51gTQYGScyYw2KD5DyygEfeFuARzlsfH8Q87Q-tsMgaHEcuJ4mZzghcPLt1GvAI5Tqh3xeMJ3tWaAcH6SVGUnHvKqgSj7vdB1v0vPI6GWGSw5aKOE5aeOyYVckLHSj0Og1ABZc2Jxul2irBlXrKZf5nmqG3Rn1I3AtjhlZP4cBrLK7u1bZZc1dfx15WMl7SHCePbt63LP5-LSQnCvbt6rBkZQYhPnL-4LFApfHCfNhB2dEdE0L4q6dKx0aOGZNG1P2K04hy4fDElSiRFi9Qg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PwEgqPDaPc0eYvVvAdCxDOkvxiy99PhFZZ6MGarPkcG0xyCY7YSx8WrufM9zcDb41_dQ5hJIseyfVJ4gt05LUDLQKMJhz78ugPqhGTMPFI8rEYUQhnqOdMH0T7oPs3FecbSVSUmXIzugbWo7IbsfH1ElYFlHHTu6ZUrpn6WUetp6rtc9PnDfYrXBlyrAwSU_jB6H1aZwAglsadwqF9FAYnwXhKmJIFQ9oE2eIgBt3MP9D5CsYSjadqxaXP_3a0N_P5Xm15-T3bQ6TvLc9XBrprv8PbghVVeDpK1h5TZeop_QfvHDfYrHCks9KIP-_TQwdpiJ3xWAxhCq02uIvvzQDg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f7ab8e5c4f.mp4?token=NjR5jS316E-h8L2bqnCbyypCgII7NDK46nU9wfW3O-6tV67nruRePAt0NHwA-wMcbOMm_yCzyxD9aoTN4872tMvSK8hPw3X858GTe-cTrYbf35iuhlU9bkpuXiE5xcYpFsX5Jr91Kj3OeCQ2PwTlcAz3zI9LU1JbFGHpBivHz1DGeeppe1NSNwm0LrMjM5pXqw4lobZoIfsm4zzviYDnJ-y3yOLfl6cCBZfItbQm7FI8n9vmD9gN_7nl5dCV-5i0YSHHNGPBbF3E1uXfmvB6G0cYUDWJ9MzO3ny7CCZMrdqwCLGcFN5m84v8QftfDYzbNuHcPC4XUIg5xsV5jOaD2g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f7ab8e5c4f.mp4?token=NjR5jS316E-h8L2bqnCbyypCgII7NDK46nU9wfW3O-6tV67nruRePAt0NHwA-wMcbOMm_yCzyxD9aoTN4872tMvSK8hPw3X858GTe-cTrYbf35iuhlU9bkpuXiE5xcYpFsX5Jr91Kj3OeCQ2PwTlcAz3zI9LU1JbFGHpBivHz1DGeeppe1NSNwm0LrMjM5pXqw4lobZoIfsm4zzviYDnJ-y3yOLfl6cCBZfItbQm7FI8n9vmD9gN_7nl5dCV-5i0YSHHNGPBbF3E1uXfmvB6G0cYUDWJ9MzO3ny7CCZMrdqwCLGcFN5m84v8QftfDYzbNuHcPC4XUIg5xsV5jOaD2g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
ویدیویی از محل اصابت بمب‌های GBU-39 آمریکایی به سایت پدافندی رژیم در جزیره خارک:
ویدیوی منتشرشده محل اصابت بمب‌های هدایت‌شونده GBU-39 ساخت آمریکا به یکی از سایت‌های پدافندی رژیم جمهوری اسلامی در جزیره خارک و محل استقرار توپ ضد هوایی قدیمی ZU-23 در جریان جنگ را نشان می‌دهد.
@News_Hut</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/69699" target="_blank">📅 21:14 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69696">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/thz8CZTrvAcBs3Xd1QCRzwg5_qy6YxOqDcboTx1aUe72ISibZQi1YgjBip-onUlvP8FWJq52T0P3Fr1Ddk9S7YWRNZ2UclojpJOLfaG_H7nxZZaencFV7mIGWFzF2PahHON3gpDzlc1m5JfiN6U4cutpgyQZLxYmXyglOpF3CzmVAtk4BlQBaarYLolfEIn36f4-7tx7e-G7h3vq3UsRC2RpjOpzUY6JI6mg2UfpBjhBbJR-6KwR3RgyYTPtmGGSNQ6hZkYKUHAueoofKy1Lo7dVI7fi4nJYXbwM1HXf_hH3aiNjl4bF1-ZYFuuxuxeNmPyK3W-BhjZhJa4xDGj3HQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/7ed553c5ba.mp4?token=IHL9rNtPabgmbh6Ya-O3f0lDSlQ5JuuscMb0fcsiXTV1GzYQt5xGy-KdQQTlx2a3hl22fnlBy-lUFdapI7DfAriIRCVqJfTDLv_z_EhAuPLf5uXoXQxe-rOkown8PvRkhwSTq-jeRbx7sSqIlQxv8fQ48keYJM-WDeM3dNbbSnbuAqRfdmRRZZecdEFsk31vuElEyPhD2wsfSonCWnGaMcV0hqWojQoj5WXOuxSbckE0nE8ZIIqBFPoZb0Vo1ot68ofQtKbi4JCBIMnD2wd3VY9BPkWXfse-LfCZmCigncFU3f_cEBg6g_WXp9zbX1CyMn_6cguCZugOCMW1IUXBqA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/7ed553c5ba.mp4?token=IHL9rNtPabgmbh6Ya-O3f0lDSlQ5JuuscMb0fcsiXTV1GzYQt5xGy-KdQQTlx2a3hl22fnlBy-lUFdapI7DfAriIRCVqJfTDLv_z_EhAuPLf5uXoXQxe-rOkown8PvRkhwSTq-jeRbx7sSqIlQxv8fQ48keYJM-WDeM3dNbbSnbuAqRfdmRRZZecdEFsk31vuElEyPhD2wsfSonCWnGaMcV0hqWojQoj5WXOuxSbckE0nE8ZIIqBFPoZb0Vo1ot68ofQtKbi4JCBIMnD2wd3VY9BPkWXfse-LfCZmCigncFU3f_cEBg6g_WXp9zbX1CyMn_6cguCZugOCMW1IUXBqA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">امروز ۱۶ ام مرداد، سالروز درگذشت فریدون فرخزاد هست.
مجری، خواننده، بازیگر و سیاستمدار ایرانی، متفکر، میهن پرست و آینده نگر.
به قدری کلامش پرنفوذ بود، که جمهوری اسلامی احساس خطر کرد و در نهایت ترورش کردن.
اون همیشه دغدغه‌اش، آگاهی و آزادی مردم بود و همیشه مردم رو به مطالعه و مقابله با خرافات تشویق میکرد.
از جملات معروفش میشه اشاره کرد به:
«یک روزی ملت ما آزاد میشود و این روز زیاد دور نیست. فرهنگ همیشه بر زور، ستم و قلدری پیروز می‌شود.»
@News_Hut</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/69696" target="_blank">📅 20:33 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69695">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pX8p0p488BUJQRS_2yd2hKo0wEnRZV_DLbRxOL28Ou5Jv_ejGYWiQJkHnnCX4--i22Y6WcBZcW81UtJnH45sBWKdEeDeYeHOFoGYyzbXvPbjpiLp1DHv2UHHbRIDpMs60aRIOMpU32mEfd04iYo4iSkuvyZ5mOIjfTL-Rw_OLsYKRbCGWmcmirmgKZUXI7zwNkHvvJtBdpGVAnJSqCkHuMmKtPo4gt7sOMeuv2jS4B7eqvsp7xWN7MOt7dNcInKHMJR0aZJ1hUNLYZuOrVQWg0OvBPbj1WvgaVgkBDx-PYhgAcHRkvBhA37fgpLnYlYeVn1rMvu-DCCNQPczkJxlYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
🇺🇸
تسنیم تصویری از لاشه جنگنده آمریکایی F-15E Strike Eagle (با شماره ثبت 00-3000) منتشر کردند که متعلق به «بال ۴۸ جنگنده» (48th Fighter Wing) بود.
این جنگنده F-15E در ماه آوریل سرنگون شد و منجر به آغاز یک عملیات نجات گسترده از سوی ایالات متحده گردید که طی آن هر دو خلبان با موفقیت نجات یافتند.
@News_Hut</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/69695" target="_blank">📅 19:58 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69694">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2bedb477ce.mp4?token=OiBXcCsHsv0Kx6Ry9YL5Fq4EJayVbty8FIeAZPS8WH-nJWGzDrAzdF1RyNk9LdtfAoVMXxMY2ELZA8mYZaH1rFUONa3sr8sk7twlQJZMEAas_3mLUlVJM2Z6LsbDLIOpLDl3aCb5aI7KeQhCCdp7hP5TWsm5GwNKQmm27XEVfTE9p4LtWDt8QrfkZ1qtkLAkvo1SZAkSSJpIi3U8gLoDN05K1PBv3_A3kwUA60NBg99LR6Z9T0ZN-VB7ypLcNz1HXTMOWPHW-haU3zVnHC9zbO3OgYfz36xl0fT-BH45Lttod6B_0Wo_8-ewfQvXF7LAe6FV8lWQ7oNJhmNoNcmjFg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2bedb477ce.mp4?token=OiBXcCsHsv0Kx6Ry9YL5Fq4EJayVbty8FIeAZPS8WH-nJWGzDrAzdF1RyNk9LdtfAoVMXxMY2ELZA8mYZaH1rFUONa3sr8sk7twlQJZMEAas_3mLUlVJM2Z6LsbDLIOpLDl3aCb5aI7KeQhCCdp7hP5TWsm5GwNKQmm27XEVfTE9p4LtWDt8QrfkZ1qtkLAkvo1SZAkSSJpIi3U8gLoDN05K1PBv3_A3kwUA60NBg99LR6Z9T0ZN-VB7ypLcNz1HXTMOWPHW-haU3zVnHC9zbO3OgYfz36xl0fT-BH45Lttod6B_0Wo_8-ewfQvXF7LAe6FV8lWQ7oNJhmNoNcmjFg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⌛
چند روز پیش یه خانوم معلم به برنامه شهبازی وصل شد و این حرفا رو نثار شهبازی کرد :
من معلم دانش آموزان ایرانی هستم و خیلی رندوم مجری حال بهم زنی مثل شما دیدم
اسمتو از گوگل سرچ کردم دیدم حالم از ادبیاتت بهم میخوره از لفظ و گفتارش و از عدم اگاهیش حالم بهم میخوره
همه میدونه این مسخره بازیو که ایران گذشته چطور بود و الان چطوره حالم از دروغ هاتون بهم میخوره
واقعا صداوسیما انقد بیچارس افرادی مثل تورو بزارن مجری و وقت مردم رو بگیرن؟؟
البته دیگه افرادی براشون نمونده باید دست به دامان چنین افراد مزخرفی بشن
🇮🇷
حالا واکنش شهبازی: اینایی ک از سلمونی و کوچه خیابون گذرا مارو می‌بینید بهتره یه چند قسمت ببینید بعد مارو قضاوت بکنید
👍
@News_Hut</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/69694" target="_blank">📅 19:38 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69693">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Anw9SV-BY3xLkWNarlIJr4QqPjXywWnM6mQuVqhLUSYu7bwIVvwzV71NZW9LEOEqAlFUdoCDT0tKX4muctXyYX8ohCfr40VPshTiblls4DORJVUmgi7WoJ1KsxcO9O4BAmZrpCh17XNKsq5NO9QGNEBSpSJgFN9Yr71rFZA594zBcn1AAdVpBY_r2t3nsSEhpTmPzW4v_Pw4dExsN3k0MIv4LaUOyAwyFQhR9k8VpEENqkJfaZNwsC0iBk4B1GUPQeruc4t1NbFJJXRhx5CLNBXhqP_MPZr8NuCzIHXBFifdqUajo7Epa_wav8MEmgYD7oj_n5P8a5kNKJ0fxkMB_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
🇺🇸
به نظر می‌رسد که محاصره دریایی ایالات متحده، صادرات نفت خام ایران را متوقف کرده است.
تقریباً یک هفته است که هیچ تانکری در جزیره خارک، اصلی‌ترین پایانه صادرات نفت ایران، بارگیری نشده است. این طولانی‌ترین دوره اختلال از زمان آغاز جنگ است.
اطلاعات ماهواره‌ای و کشتیرانی نشان می‌دهد که اسکله‌های بارگیری خالی هستند و ترافیک کشتی‌ها به طور کلی متوقف شده است.
ایران همچنان درآمدی از نفت‌هایی که قبل از محاصره ارسال شده‌اند، کسب می‌کند، اما این محموله‌ها رو به اتمام هستند.
به جای پر کردن مخازن ذخیره، به نظر می‌رسد که ایران تولید نفت را کاهش داده است تا از تجاوز به ظرفیت ذخیره‌سازی جلوگیری کند.
﻿
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/69693" target="_blank">📅 19:04 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69692">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/af32e5c900.mp4?token=qtB4UqhGeYM15C1dcxtGKGA8aWwr8ke8yGn8hhWJZzUSsD40Q_4AN6YAs0FlyRrL18ti4xlPzXVmi9DF6aVronH1tZCuMKpIFDJxAqjP1cmoz-h8qDukrcZ58YtI9mX8eiCWHurjnelh3MZ6xACI1e6MBO9POClWEtgkRGrrSP67kWbGTaYSrTOyTmDf9Xk0faz09CAfmC5lJmudsQv8PuyiZkHOwANmJgwG9YtixeCdbz25oWvNL8DXG0WFE3B22LrpluDzLNYiuKH_BS0TIyhdZaPx5BC2XV3qypzLkvRZ7_otGo9htec4J5P7-Onpf4lwxiTVOcYr-IlcFg0-wA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/af32e5c900.mp4?token=qtB4UqhGeYM15C1dcxtGKGA8aWwr8ke8yGn8hhWJZzUSsD40Q_4AN6YAs0FlyRrL18ti4xlPzXVmi9DF6aVronH1tZCuMKpIFDJxAqjP1cmoz-h8qDukrcZ58YtI9mX8eiCWHurjnelh3MZ6xACI1e6MBO9POClWEtgkRGrrSP67kWbGTaYSrTOyTmDf9Xk0faz09CAfmC5lJmudsQv8PuyiZkHOwANmJgwG9YtixeCdbz25oWvNL8DXG0WFE3B22LrpluDzLNYiuKH_BS0TIyhdZaPx5BC2XV3qypzLkvRZ7_otGo9htec4J5P7-Onpf4lwxiTVOcYr-IlcFg0-wA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
اسکات بسنت، وزیر خزانه‌داری آمریکا:
«ما آن‌ها را کاملاً تحت فشار قرار داده‌ایم و آن‌ها با تورم ۱۵۰ تا ۱۸۰ درصدی مواد غذایی روبه‌رو هستند و حتی توان پرداخت حقوق نیروهای نظامی خود را ندارند.
فکر می‌کنم به‌زودی، شاید حتی امروز یا فردا، شاهد دستیابی به یک توافق و برقراری آتش‌بس ۳۰ تا ۶۰ روزه باشیم و تنگه هرمز نیز بازگشایی شود.
در این صورت، قیمت انرژی باید کاهش پیدا کند.»
@News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/69692" target="_blank">📅 18:32 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69691">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eac71f40e4.mp4?token=vHGB1GCwA7sQCFDyNPqu8-eEew60T-nhv6IIhFh-Xu-PkuI_dbJgNkI8w0tLsjwM9m4R09T24cImPV8Br8DbyeiRnNPIchXrJQYVmIivFncRIhxl4jHSGam21nnTA8tfjAkF4-ArvagSweG9RCdTqK9-FkeDFuUEJctbMOgACsRUl-IUcw6IekAXQum35yz3c1Bde6YuN2-BisSv-ojy3_nvpavwMZ346VOh2zooRatet6antPfwSrx7KWgzI40Niw0Y7wC4uvYH1XU8honxsZYt-re2iuvIP5NQqv1AYzBbvf21Vs-Kv7UsHd6YVE35pIXCVUFEBRfQrO7V4EyKRQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eac71f40e4.mp4?token=vHGB1GCwA7sQCFDyNPqu8-eEew60T-nhv6IIhFh-Xu-PkuI_dbJgNkI8w0tLsjwM9m4R09T24cImPV8Br8DbyeiRnNPIchXrJQYVmIivFncRIhxl4jHSGam21nnTA8tfjAkF4-ArvagSweG9RCdTqK9-FkeDFuUEJctbMOgACsRUl-IUcw6IekAXQum35yz3c1Bde6YuN2-BisSv-ojy3_nvpavwMZ346VOh2zooRatet6antPfwSrx7KWgzI40Niw0Y7wC4uvYH1XU8honxsZYt-re2iuvIP5NQqv1AYzBbvf21Vs-Kv7UsHd6YVE35pIXCVUFEBRfQrO7V4EyKRQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
صحبت های یک حامی حکومت:
دیدید واسه اربعین چجوری از پول شما مردم خرج کردیم و کباب آهو دادیم به زائرا؟
براندازا بسوزید، بسوزید که هرچقد پول دارید و ندارید باید خرج امام حسین کنید، تا ابد خرج امام حسین و دینمون میکنیم یا الله!
@News_Hut</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/69691" target="_blank">📅 17:52 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69688">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/266f0707c9.mp4?token=fcrcxwg0l42o3qOR7FODmU61zvt1EUSzoVIIyZS35H04bCKWVKFOWaiQB0xTuhqWvX03dsT23GaEKLNBFSbJFsLQ_ToaVWo2uCTFzRn3pQ-sU9aCFbIB1tXwPjSK10PFTzSr1koT_0m6-aKwHdjqBxi6y-lh0JYw2RBbOJHYRcpa5iLJVaB5bIyHaYLrxO37AF6Ffe3N4HZibr7wJvwvYa7ZeuDOwiBpP_nhfTyqloJPUiX3b--Qa0XbF8HkyQkspQfbcRL6pia7T6FGYk-Srjkd03jinlE7WFeRH6EebrNDS-tT84OegIIUDPgwlIR5TBr7RN1Z0jjUeY9qulUpDA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/266f0707c9.mp4?token=fcrcxwg0l42o3qOR7FODmU61zvt1EUSzoVIIyZS35H04bCKWVKFOWaiQB0xTuhqWvX03dsT23GaEKLNBFSbJFsLQ_ToaVWo2uCTFzRn3pQ-sU9aCFbIB1tXwPjSK10PFTzSr1koT_0m6-aKwHdjqBxi6y-lh0JYw2RBbOJHYRcpa5iLJVaB5bIyHaYLrxO37AF6Ffe3N4HZibr7wJvwvYa7ZeuDOwiBpP_nhfTyqloJPUiX3b--Qa0XbF8HkyQkspQfbcRL6pia7T6FGYk-Srjkd03jinlE7WFeRH6EebrNDS-tT84OegIIUDPgwlIR5TBr7RN1Z0jjUeY9qulUpDA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
‼️
🛸
وزارت جنگ ایالات متحده، پنجمین مجموعه از اسناد مربوط به پدیده‌های هوایی ناشناخته را منتشر کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/69688" target="_blank">📅 17:14 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69686">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/727c872e40.mp4?token=DeHTJd7KGJ_9TPGKQN5Hh1TFtLwyD-NM8A4zvpI8FLU_Bzwz_v9sEzDWxyBl1HcmaHcLmcokbkTc9ukoFwUf59RPPnjPI5_wwMwMru277SW0GRswdb10k7JdUq_q1e1ixx-vwQ6_LQprhRhg37M_zKwex30Pk1s8CZJooojTRm1uG6T3qOV3TqNEpZDTVaPGLRr977XI1FRzN6lMYHUpDmhoH7HS29p-xYJzoYvYfgvM2n-nQUHp9-WTsiV-iNNTKLKHT2QIOpmMeY0E7-Kd1oryTGEkz9ru799r63EBQQNdnIg9tdZpN9oPm5meT2paX69c9-OpgxJIMacDHZ2Bdg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/727c872e40.mp4?token=DeHTJd7KGJ_9TPGKQN5Hh1TFtLwyD-NM8A4zvpI8FLU_Bzwz_v9sEzDWxyBl1HcmaHcLmcokbkTc9ukoFwUf59RPPnjPI5_wwMwMru277SW0GRswdb10k7JdUq_q1e1ixx-vwQ6_LQprhRhg37M_zKwex30Pk1s8CZJooojTRm1uG6T3qOV3TqNEpZDTVaPGLRr977XI1FRzN6lMYHUpDmhoH7HS29p-xYJzoYvYfgvM2n-nQUHp9-WTsiV-iNNTKLKHT2QIOpmMeY0E7-Kd1oryTGEkz9ru799r63EBQQNdnIg9tdZpN9oPm5meT2paX69c9-OpgxJIMacDHZ2Bdg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏸
ویدیو ای از یک مصاحبه قدیمی با روح الله زم :
من با بالایی ها ارتباط دارم و بهم امار میدن کاملا
اینا پشت بیسیم هرچی میگن من میفهمم
هیچکس نمیتونه بفهمه منابع من کیه
همه مکالمه های بی سیم، سیستم ایران شنود میکنم
@News_Hut</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/69686" target="_blank">📅 16:33 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69685">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/b41beaa653.mp4?token=faFcZbCaSKBHCmnugk2232AEfAd3cSjA2qV0ciqwh7UKCT0bF0HUDeD8udV9c22JkIJhu78-rdl0mPQtfmptcuZcCN391szTNI4n_ZaB1GAoqcoLxJ8bUhMEx_8NRd-Y2-IF5Dim2nSjopiYbWEGhODo_NwI2Mxr5NpDK8W0i8h6bwt1Tm1EbRRG3p4Kqtkp5oSAb7U6uRfUP8pmEeNrCtBmxSYExUvmdfq5_biX_093YPYjpCa91rgN7JsQtHaLihlP66giGlF51w8l3DQBv5APRulX9FAUE9FDZOLIbFDhvg0g8uDcftmc9e2ctBY5kL2QtS_I0-n5_TXU8S-JoQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/b41beaa653.mp4?token=faFcZbCaSKBHCmnugk2232AEfAd3cSjA2qV0ciqwh7UKCT0bF0HUDeD8udV9c22JkIJhu78-rdl0mPQtfmptcuZcCN391szTNI4n_ZaB1GAoqcoLxJ8bUhMEx_8NRd-Y2-IF5Dim2nSjopiYbWEGhODo_NwI2Mxr5NpDK8W0i8h6bwt1Tm1EbRRG3p4Kqtkp5oSAb7U6uRfUP8pmEeNrCtBmxSYExUvmdfq5_biX_093YPYjpCa91rgN7JsQtHaLihlP66giGlF51w8l3DQBv5APRulX9FAUE9FDZOLIbFDhvg0g8uDcftmc9e2ctBY5kL2QtS_I0-n5_TXU8S-JoQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
فیلم وایرال شده از مرکز ترک اعتیاد توی بالاشهر تهران؛
اینجا ترک کردن کمپ، سخت‌تر از ترک مواده
😂
@News_Hut</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/69685" target="_blank">📅 15:57 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69682">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rv8ldM4Loh-2ug2oP79f0wWFQXg-nxbh_tT4nHBsHDis1Ys_u3b_HRSposrmG2-KfgfrsEMlrhuNnfP3xl91pGuiMIYbES-wS7v0y5ZWZ14iowApXSYNpuN_mSt-jYXujL8es6TgtvZUyHzGgddZTBFllkV3fTqr5JZw02uDLeUuP_d3tXgkWnitizHRX7gfh6VszUQ5-TFPaL6iypd7EMym9knbxnVmDJ0ShtcyQhInhxy9rJf29k8HFpAl7XBU7NqlPk3WfhD9qGgCnJq-5YQKdgnThrAYX2WzDKO9vhYOoepWp3LC4N6eWYewV25I-ENrDwdWrfjourh677NvGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/taX2U4Lng5p3Pi29EeWQkNjA7qMfc9LP2SgGnMbTCkLrK7C8m6x-91pOg278hoVSjHV3dP-8zw_vvdYJ-fB-VqIyrcgVnKgxMY6USvPD6L8j5EGKlKKmztmWuViCND3K3m022d4i9lVjo4jliF1TeMU_FKsDZMOMAFt9TqM2gVzkIXR014p9Cjks8ScCKnnZP9sDgMYjT7ItU_B0lIbZtyIEjw64-JFQRvyj_6xv_KFDtsS7sCcfqywHm0TeVNihaNG1zgt3NYtuyZqCWu0jNqHR363-nlMnkyfZKt6WQS0mVzYjOTQSZAA7pe-Gi9NaQ2OGgpZLKfqSK7FE450Tyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qaFiTdabI_U_DjIK80J3P3qyAilUF92sBaeRG-d03nP1oKtr-sx9XVqm2DuykpdrYyYobgMCYakUiL0TYfiF2ozIjP5f_DLdi6xCZ0N9YBZe18cSfVnSdeauuq_yf9_f-VvgasrtxgtE8m0fLojJNG55TjR77M5AsJq-nvn6AAXopjnO8DNV84PUdbmnFQAQxxt8g_rwQPe2O4QLz-RW7rCgAtphmkbgMv64MCbF943VxLuecL3KzkS-WDysdwiz9LOJEpmBcwWzv7t22IXRGFq3_p-emInm6dIkQgmawA7DcjVewMZKAzKOeAw99dPlGPoSD-iHIYMe_xll0jieJg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
🇮🇷
خبرگزاری تسنیم وابسته به سپاه پاسداران تصاویری از یک «انبار» هواگردها منتشر کرده و مدعی شده این تجهیزات متعلق به هواگردهای اسرائیلی و آمریکایی هستند که در جریان جنگ سرنگون شده‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/69682" target="_blank">📅 15:46 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69681">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5020dac98e.mp4?token=i-TbTYPreZefw494cA91zBC7ZO-v46prArizrp3L-bIpXkGuoYisme8aXXTfStNG6IK4sRmM0qEmmFO1iIlkswYvT6TiqzU_Lwg9QR12dWYp4v7OMsrV4_viematM1KD-xNw7e0ktDJ-S2lTTT4B1GCNA-OyJRmD-UFjHoGqWAx4Yki6IDXiPuZnjbcQnJIegjhiPgfg-TvKW8bNNg9bWnEY9FUbbVpJCDPP_TpxBLq9wg8FJbkGd3bgubwlt0nOe-hS3gxHYWyx_zcOp3bRzqsmkQF81z3NHASO5zKmM9Tg_OdYadAlddyfZ0RGWg1RrnS7tkcULoCgS-QOP4kh7A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5020dac98e.mp4?token=i-TbTYPreZefw494cA91zBC7ZO-v46prArizrp3L-bIpXkGuoYisme8aXXTfStNG6IK4sRmM0qEmmFO1iIlkswYvT6TiqzU_Lwg9QR12dWYp4v7OMsrV4_viematM1KD-xNw7e0ktDJ-S2lTTT4B1GCNA-OyJRmD-UFjHoGqWAx4Yki6IDXiPuZnjbcQnJIegjhiPgfg-TvKW8bNNg9bWnEY9FUbbVpJCDPP_TpxBLq9wg8FJbkGd3bgubwlt0nOe-hS3gxHYWyx_zcOp3bRzqsmkQF81z3NHASO5zKmM9Tg_OdYadAlddyfZ0RGWg1RrnS7tkcULoCgS-QOP4kh7A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
سردار کوثری، عضو کمیسیون امنیت ملی مجلس:
ما هنوز که هنوزه موندیم چرا شمخانی با اون همه سابقه نظامی، اصرار داشت اون روزِ حمله جلسه بذاره!
رادان گفت نمیام و رضائیان، رئیس سازمان اطلاعات فراجا رو فرستاد.
پاکپور، فرمانده سپاه گفت من نمیام دارم میرم اهواز، ولی به اصرار شمخانی اومد.
وزیر دفاع رو هم با معاون‌هاش دعوت کرده بود.
الانم چون کسی از اون جلسه زنده نمونده، نمی‌تونیم بفهمیم چرا شمخانی انقدر اصرار به برگزاری جلسه سران داشت.
@News_Hut</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/69681" target="_blank">📅 15:15 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69679">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WZoaH68QXOxvPxyf8uqLol2WiABSD1-96I6miZVkACZZ0wmQ1qdIPaKbVXsvDh9AyGpj0y0TPkgOI5QFxBOAK3d_p9nwtDlqTAvHetfL0slOXJ3bUNvGb1DDAYlcA52mgKhSwAihiia3Eh4sdy8FXFMWZh87AGnq12h33JxSMwJUq-Wd2oTnIUq9jK5nWFq-qJ79vYnr8QPxdzzxQvBYazbq-ymyCr3fbdjPVfegJcF-dwgCgivuDmH08yMFJ7rRJEgWN6XfYM1CtJiharJJ1k9HA0sCXMXHqReDslgDz-IVY9-UZLwZjGPRjgbnAJ5jrzz2bgSeW9RfRqh4mUlNiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FfLh7p5uaA9y4gebhjIbX3rIurAMLMn2Dzjzz6qiM-JZo55Y9B0akwo2zpJK4mzF-ZqLvSD5DVDw863nt-nEyRyWTIiDONjHDY3U74QnFyfLvBdOWwqCUxHcH4vPYBYYOb-TLOqXKKKRQ_3PAa4_i0VDqQam47slBfwJdniRsZyyu5jqxZrGlcsWiMpwd9KJZ5pQWHHNvRgDxKtdCL0-dmR9IQ4CztPu6YEqloFs4ZBD6xZNXZD21sE3Alr723N9r9nFKJqjJHC-DusJ_83bxYJsQbDKEA-slOHOr2hrxJaKRGyZxJlSudZQANAmf8oPxOcQFKh3nbia_fS7HoPE-g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
⭕️
🇸🇦
🇹🇷
🇵🇰
ترکیه، عربستان سعودی و پاکستان پیمان دفاعی «توافق‌نامه مکه» را امضا کردند: «هرگونه حمله نظامی علیه هر یک از این سه کشور، به منزله حمله به هر سه آن‌ها تلقی خواهد شد.»
این توافق که مذاکرات آن از سال گذشته در جریان بود، چارچوب نظامی سه‌جانبه و مهمی را در بحبوحه بحران منطقه‌ایِ رو به تشدید — که پس از حملات اسرائیل و آمریکا به ایران پدید آمده است — ایجاد می‌کند.
@News_Hut</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/69679" target="_blank">📅 14:27 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69677">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b215003af2.mp4?token=BCDjFaWJMC4HpJ74JfXGc7JI2DIDYu3TyGeTSOSICBTF-EzWKCvPJ2iIV30AHVBZQwn4fZ7OwB69ptUZgFIRRCT_vizwKy5hhMg4XW23yTXITsNlaFfefPots91X_lwA-tmEqcjlthcyjbgNcLbMkUiO40qbrJY4zd89i_9XUvT5-9e78Bm1BjNlRbk_w1gkyZFPs5Ky8erjnONDiRBxVV_Fwm1MYpxQnQu05ZwgYJNIJPB4D2pYc0AlhxIHgWrenwvgVxNjE8wzEEIS9drAFU4iY86nUj3JAh3MFsNVApWD-LAJOxug8-nXPWVuWtqd0ecjjSNXhto6mTFKYEFgxg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b215003af2.mp4?token=BCDjFaWJMC4HpJ74JfXGc7JI2DIDYu3TyGeTSOSICBTF-EzWKCvPJ2iIV30AHVBZQwn4fZ7OwB69ptUZgFIRRCT_vizwKy5hhMg4XW23yTXITsNlaFfefPots91X_lwA-tmEqcjlthcyjbgNcLbMkUiO40qbrJY4zd89i_9XUvT5-9e78Bm1BjNlRbk_w1gkyZFPs5Ky8erjnONDiRBxVV_Fwm1MYpxQnQu05ZwgYJNIJPB4D2pYc0AlhxIHgWrenwvgVxNjE8wzEEIS9drAFU4iY86nUj3JAh3MFsNVApWD-LAJOxug8-nXPWVuWtqd0ecjjSNXhto6mTFKYEFgxg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇸🇦
🇹🇷
🇵🇰
رجب طیب اردوغان، رئیس‌جمهور ترکیه، و شهباز شریف، نخست‌وزیر پاکستان، به همراه مارشال عاصم منیر، فرمانده ارتش پاکستان، امروز وارد مکه در عربستان سعودی شدند تا در مراسم امضای توافق‌نامه دفاعی سه‌جانبه شرکت کنند.
@News_Hut</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/69677" target="_blank">📅 14:13 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69676">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/637fe07403.mp4?token=d4RARjL_2HkNw5ufutCI_GBDl8mm0to05KBzdr8AMSUgcZLWQINuLR687JtffEXBN38t53JuXOrAafrP0HSWy5co4PjwM9-rbu4V5nANXI3kKSRQmm1tEnHfljl2xcCGpVulB-R5zaAjc_i-R0ppmAR7hpX6WKE8rC72qTBGVgmUeiVrmIoXoaSleIKwfRDj72Ow04kqyMtlu2YrEIslvIVqtgsuz0E72oQjNc-kh8fFX9BUaYE-JmOr7CfziH2owSvHmm_bvUCqtAYWF-pDzZnp-2acFWePVu0c1yqpepv-f2u7--pVKssrVFqpvBvhFluoTxU7CffGrb9k22zB1w" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/637fe07403.mp4?token=d4RARjL_2HkNw5ufutCI_GBDl8mm0to05KBzdr8AMSUgcZLWQINuLR687JtffEXBN38t53JuXOrAafrP0HSWy5co4PjwM9-rbu4V5nANXI3kKSRQmm1tEnHfljl2xcCGpVulB-R5zaAjc_i-R0ppmAR7hpX6WKE8rC72qTBGVgmUeiVrmIoXoaSleIKwfRDj72Ow04kqyMtlu2YrEIslvIVqtgsuz0E72oQjNc-kh8fFX9BUaYE-JmOr7CfziH2owSvHmm_bvUCqtAYWF-pDzZnp-2acFWePVu0c1yqpepv-f2u7--pVKssrVFqpvBvhFluoTxU7CffGrb9k22zB1w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
بخش هایی از صحبت های ترامپ درباره ایران به زیرنویس فارسی:
@News_Hut</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/69676" target="_blank">📅 13:24 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69675">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a0a5084b0f.mp4?token=Le0n4RIu3qzxfyiDr7fJJL67q4I11nqUsHAYuRXr33ftXUwctRQ0PWVuoMh2dxYQIjHg_KcthmMB7bnUAzz-koB6HHL-JuSCASLFoQmIx7OS6xoMkF7TbDno4H8Y3_p6BiIKIE9-4sk2g4PY7sTOw8co60Q1k9IWnr6Bi17HAEnU2JIuowR-mg44ZWLASWOcCxD85KbqS5ZFT4JpMTd1DrpqHsCSUjizOJwI2TqYWuaDcghL1pQslqM--f9DUzf-r4ZrXF4q-YlUASQSTlo4zKB76Rpfr0Au1KcRhGG62EBA7vtpICGCUGRf3iVcIny7B9zwnZHg7luL_iIc35ZTHA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a0a5084b0f.mp4?token=Le0n4RIu3qzxfyiDr7fJJL67q4I11nqUsHAYuRXr33ftXUwctRQ0PWVuoMh2dxYQIjHg_KcthmMB7bnUAzz-koB6HHL-JuSCASLFoQmIx7OS6xoMkF7TbDno4H8Y3_p6BiIKIE9-4sk2g4PY7sTOw8co60Q1k9IWnr6Bi17HAEnU2JIuowR-mg44ZWLASWOcCxD85KbqS5ZFT4JpMTd1DrpqHsCSUjizOJwI2TqYWuaDcghL1pQslqM--f9DUzf-r4ZrXF4q-YlUASQSTlo4zKB76Rpfr0Au1KcRhGG62EBA7vtpICGCUGRf3iVcIny7B9zwnZHg7luL_iIc35ZTHA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
روایت کوثری نماینده مجلس از عملیات اطلاعاتی موساد؛ «رد لاریجانی از طریق گوشی زده شد»
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/69675" target="_blank">📅 13:17 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69674">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">melbet.apk</div>
  <div class="tg-doc-extra">53.8 MB</div>
</div>
<a href="https://t.me/news_hut/69674" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🇩🇪
آپ اندروید سایت جهانی Melbet
💥
🎁
بونوس ورزشی هر چهارشنبه
🔥
💸
واریز و برداشت متنوع
💵
⭕️
بدون نیاز به فیلتر شکن
⭕️
r16
🎁
کد هدیه ثبت نام Melbet90
✌️
✔
https://t.me/+x60dZGAgXTUxM2U0</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/news_hut/69674" target="_blank">📅 13:17 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69673">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e_6gusRA_uT8yHsPRi8GqLu8OE1uJ_Rg1WruiH8zF2J1ecvgTt39z70tie1bIv-FdCPWmLbgjSaVy2Ykc91Hr1yrwr0GcDY4Rnh_WNw7vj8ozYOJXN3auEonCevAkv9uxK-CzAPctlvCe9cTLAFHe9hy5y60FOPo47p2EdGs7qg2Q0aIaXafV2LwrtyG0AO6mSpdx3Am5PEkTF3l7kwpoWib1tuMdmV9xXWIx8U7OW1yy0RLoYS4kAJLc3fA_taFQgwUs8uUYALe4OIFjQUJs1LfiODVoUhWvaSryKerTGu4gGOpvlh1Re2xRyTyTt3GPz0wiuVKUkqQjcEwGirC_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
دنبال سایت معتبر برای شرطبندی می‌گردید
⁉️
🎲
سایت بین المللی و معتبر Melbet
👍
😁
😊
🙂
🥇
واریز و برداشت ارزی و ریالی
‼️
🔥
بونوس 100% اولین واریز
‼️
⚽️
بونوس ورزشی هرچهارشنبه
‼️
🆗
کازینو و انفجار با ضرایب جهانی
‼️
🎁
کد هدیه ثبت نام :Melbet90
🇩🇪
دانلود اپلیکیشن MELBET
👉
🔗
لینک وبسایت
👉
⭕️
جهت استفاده از vpn از IP های آسیایی یا کانادا استفاده کنید.
🇨🇦
🇹🇷
r16
✔
https://t.me/+x60dZGAgXTUxM2U0</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/news_hut/69673" target="_blank">📅 13:17 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69671">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6e0c63da7c.mp4?token=StjFpsGqQBrj4U-9rGjdtou5oS2i_fEqJWfl_N9dIefH3hy-kGa02qrqy37m3I7gOVT9kpNN5T2OYEshPiPMsjmvfqqqw3ULv1xi1ycbI3fkRwBk03t3bDzkXSGGE035SDSIxMgqhOuOmMEo3nFjWQRV1sjWml0GZmdyDP6tMLfXcFy54BITbOMR4KHwLRB5QyqRma_QrcNP3QOh49q3_GIbfgugSabeUksdPT792OSrX1dKaeY0_0fEPQYaSjwgTCfPTBJoq0zUzx4ls8rXTq_AZoeAexZ5xXkrMoklLsVATEkSEQo_-lMKrIwNY9A8-GqQFHyzH0QlztREeKcrmw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6e0c63da7c.mp4?token=StjFpsGqQBrj4U-9rGjdtou5oS2i_fEqJWfl_N9dIefH3hy-kGa02qrqy37m3I7gOVT9kpNN5T2OYEshPiPMsjmvfqqqw3ULv1xi1ycbI3fkRwBk03t3bDzkXSGGE035SDSIxMgqhOuOmMEo3nFjWQRV1sjWml0GZmdyDP6tMLfXcFy54BITbOMR4KHwLRB5QyqRma_QrcNP3QOh49q3_GIbfgugSabeUksdPT792OSrX1dKaeY0_0fEPQYaSjwgTCfPTBJoq0zUzx4ls8rXTq_AZoeAexZ5xXkrMoklLsVATEkSEQo_-lMKrIwNY9A8-GqQFHyzH0QlztREeKcrmw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تا حالا نوک قله دماوند و کاسه قله دماوند رو دیده بودین؟
۸ مرداد ۱۴۰۵
@News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/69671" target="_blank">📅 12:51 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69668">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/10354b943b.mp4?token=Qx495VYZaex90RsclrRt2EvABPGVV1gkMuxZoXgaoaDRNF_F2gDiqII3yCmXeXeQ3OVhw4svF_XOIF9WgWr1YjoqHQ4M1zs6eMG-6TKiRadlCT-G-I3prmOTxQ4BOBv1PLKVJFl60_i3lIYRUTj5S_J9g6mQyATPHb7zg8lNNz73J84cAx6iQ4cbGcJo3GB6Om6kPmjzcfwWnK_sc4cI0sJ8_J6M9kg7ZPcNsPA_Sm9RAJuA0Z5BzXK0aXJwmE_jUnbS-1ZWc1WBbNM1hw0vPoEjg6Q24c3Jz3W4A2NLYCu_mGRE6t7flxe3T1-CpBbC-TO5SnYK8y49Rzhv3XeLGA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/10354b943b.mp4?token=Qx495VYZaex90RsclrRt2EvABPGVV1gkMuxZoXgaoaDRNF_F2gDiqII3yCmXeXeQ3OVhw4svF_XOIF9WgWr1YjoqHQ4M1zs6eMG-6TKiRadlCT-G-I3prmOTxQ4BOBv1PLKVJFl60_i3lIYRUTj5S_J9g6mQyATPHb7zg8lNNz73J84cAx6iQ4cbGcJo3GB6Om6kPmjzcfwWnK_sc4cI0sJ8_J6M9kg7ZPcNsPA_Sm9RAJuA0Z5BzXK0aXJwmE_jUnbS-1ZWc1WBbNM1hw0vPoEjg6Q24c3Jz3W4A2NLYCu_mGRE6t7flxe3T1-CpBbC-TO5SnYK8y49Rzhv3XeLGA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇦
❌
🚀
🇷🇺
پهپادهای دوربرد اوکراینی در حال حمله به انبار شرکت روسی "وایلدبریز" در شهر یکاترینبورگ، واقع در منطقه سوردلوفسک، هستند. این انبار حدود ۱۷۰۰ کیلومتر از مرز اوکراین فاصله دارد.
@News_Hut</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/69668" target="_blank">📅 12:14 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69667">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ff4cea8c93.mp4?token=kcDIwwq-LCFVR70aJRwxfdrG1LNZCjsRoBlt7tTlke3rJv590vKmELxhCd10YJv8kSC1PU0lTdCjQ4T-1J25FXAkoBIBr7d4hUT_1V2C7AXU8DsoG8QtHh_Cf5sKrUsy9NTWGPSbOz_rRAXeHovtTZKy4r9Tvq5SuwiCOceCeE2csU0rfE81OytpJYS_LiHARPT2t9II1dh_I3cRVaZTvz_tWFafLs6d8GcypIqvMSgnSgzwNWYC1P7qd9fgPysM02n3xc_lNCpxehJWEZznp2CWJ1HspQqCDSJJrTO9iebXjX-rapY1Y_aB9zsSjgZSyNX1SPJe0j9ShH40NF5bUA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ff4cea8c93.mp4?token=kcDIwwq-LCFVR70aJRwxfdrG1LNZCjsRoBlt7tTlke3rJv590vKmELxhCd10YJv8kSC1PU0lTdCjQ4T-1J25FXAkoBIBr7d4hUT_1V2C7AXU8DsoG8QtHh_Cf5sKrUsy9NTWGPSbOz_rRAXeHovtTZKy4r9Tvq5SuwiCOceCeE2csU0rfE81OytpJYS_LiHARPT2t9II1dh_I3cRVaZTvz_tWFafLs6d8GcypIqvMSgnSgzwNWYC1P7qd9fgPysM02n3xc_lNCpxehJWEZznp2CWJ1HspQqCDSJJrTO9iebXjX-rapY1Y_aB9zsSjgZSyNX1SPJe0j9ShH40NF5bUA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
پسره رفته خواستگاری، بهش گفتن 114 تا سکه باید مهریه بدی؛
🗣️
اینم قبول نکرده و گفته کمه و من اینارو میدم؛
369 تا سکه
1382 تا گل رز سفید
کل طلافروشی رو می‌زنم به نام دخترتون
یه سهام کوچیک هم تو یه کافه دارم که اونم میدم
امیدوارم راضی بوده باشین.
@News_Hut</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/69667" target="_blank">📅 12:04 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69666">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">‼️
🇺🇸
🇨🇭
آمریکا حتی به سوییس هم اجازه ساخت بمب اتم رو نداد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/69666" target="_blank">📅 11:15 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69665">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/00ca70a3a5.mp4?token=SslAVvSGd-cU-iwhoYy_lHFKSdQHOUP0m1TBmLA9XZuxmPBD5tqC7DY2pHpgfwo5W9xZe7gYsozCcMCGRRDaJDe9I0je2yZ1oRjsexb_BMRdvzW6VU-Rdl0ME1Z0hFw6uzESpgdRt8OTAVhp79hoHHNnPudpq8YxEaCe-deA0pNT_7gRgwVoEWbEp0OS7pX6lVBOdjgDmIhTRl4m1lOxecjHpM-j0LDaIQnS2-4rmt5kQguou-YTSwJFAaBYUZqVIEgIbEpg1J4ZXUpUNOy_BlQS0ebs31BuAV4fwpwBAKFp9Y9NNut30Hl9IVRpVLlqvaBPatqz-mX4c-3txRW4dzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/00ca70a3a5.mp4?token=SslAVvSGd-cU-iwhoYy_lHFKSdQHOUP0m1TBmLA9XZuxmPBD5tqC7DY2pHpgfwo5W9xZe7gYsozCcMCGRRDaJDe9I0je2yZ1oRjsexb_BMRdvzW6VU-Rdl0ME1Z0hFw6uzESpgdRt8OTAVhp79hoHHNnPudpq8YxEaCe-deA0pNT_7gRgwVoEWbEp0OS7pX6lVBOdjgDmIhTRl4m1lOxecjHpM-j0LDaIQnS2-4rmt5kQguou-YTSwJFAaBYUZqVIEgIbEpg1J4ZXUpUNOy_BlQS0ebs31BuAV4fwpwBAKFp9Y9NNut30Hl9IVRpVLlqvaBPatqz-mX4c-3txRW4dzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این ویدیو از شعبه بازی این پیرمرد، قراره هر لحظه بیشتر سورپرایزت کنه
😳
@News_Hut</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/69665" target="_blank">📅 10:31 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69664">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sFBPrdymTlt2hIPnpFk1N05i3RCBhSQJ0BIbLI5F4HAYzjQZrSLTtxvjLW-c4BeRQN7oVYeZsgPwMq8thHSOdALgFvlJMvYZjXupDV9I4PFbpcLO_0AAh80vq7YPcBxkIccgS30LDCuKm2UGIbp1M5v3FunEjzL3MeVPbk4ZNKvO00pEkFZ0BLeyvBp4MUc_tIukl5EnLqkUK6N4ntIhXGERB45JoG2mvuCf2ZjhSp7UiC1pA8mD7yXbthR1ScQRjZvZ33fqhggwvQbqknMlQ3xGsi-O003fcpjVF7aO3iytPCNlyPf2RhC8tkoTVW0onMklNtVAzkjHGJ0ZbrEXNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
عنوان مقاله ای که ترامپ در تروث سوشال منتشر کرده؛ دونالد ترامپ در جنگ با ایران پیروز شد!!!!
@News_Hut</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/69664" target="_blank">📅 10:22 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69663">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c98f66ca27.mp4?token=J2PupCoMrmcw5ssIWIbNRXtd900wKh_JA-RPRCCEMrfO26ZHg3lW5JnLvJFzSMUEuMq3fhl_pVL7cv-fc9lwvDMGJbFS8fBF0dn_i9h0u_01QUOzf8J_5zDtt-A9Rhqw7qGsViI_7pA9LaT1l_VVbL3UMZTULwWPojE7A7cmd8Q15QM-hl8aLYdCzVwh467ojSHUw1ZZcDjw5mtrIZnSv9zKd-dQZoUqXWMVN_b1erj1VuyXo6kHEsgUEnxQGOao9P8zLMaBo6awnrWwTfAaUuBuDVOci40yoEaJEz86ydR3Dpgs3LsNhqWL_ESKUy8ZVzOmrgHSj3nG5tXsyiCfrA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c98f66ca27.mp4?token=J2PupCoMrmcw5ssIWIbNRXtd900wKh_JA-RPRCCEMrfO26ZHg3lW5JnLvJFzSMUEuMq3fhl_pVL7cv-fc9lwvDMGJbFS8fBF0dn_i9h0u_01QUOzf8J_5zDtt-A9Rhqw7qGsViI_7pA9LaT1l_VVbL3UMZTULwWPojE7A7cmd8Q15QM-hl8aLYdCzVwh467ojSHUw1ZZcDjw5mtrIZnSv9zKd-dQZoUqXWMVN_b1erj1VuyXo6kHEsgUEnxQGOao9P8zLMaBo6awnrWwTfAaUuBuDVOci40yoEaJEz86ydR3Dpgs3LsNhqWL_ESKUy8ZVzOmrgHSj3nG5tXsyiCfrA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇨🇳
این شما و این مجهزترین اتوبوس های مسافرتی چینی!
@News_Hut</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/news_hut/69663" target="_blank">📅 10:03 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69662">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8d6484080b.mp4?token=h3mLoXgNXB3Wt0R3l-my02NXtfJym2amVn48pCiNdH7Lfiup_e-HrCJtC_hQodCbxIuzmdVmTyWSW4Sh1vaS9QkHFr3kL-VPbv2Eq-VtyOyKQOoDwMTB7EWmGC8BXY63gVbZpjLkF1bT2Maqm94_9tdS3sPQPcJ071SQ1m6BfSGEraSl6rgURhwMD_rB178gCvuJprP0qRJ9xm2yIEC_PSW1Ks5zjjd4_OQQXsEu-cyfqW0LBB6ITMfKBq1IjmFgPYeZxWjPk9J8Dk7bfl2mTRARyyO6JgBPKppEMiQrsZ8CRZxAncFWcBUtLEnNBjTRVyP54ymZv9poeG1E7WWfOw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8d6484080b.mp4?token=h3mLoXgNXB3Wt0R3l-my02NXtfJym2amVn48pCiNdH7Lfiup_e-HrCJtC_hQodCbxIuzmdVmTyWSW4Sh1vaS9QkHFr3kL-VPbv2Eq-VtyOyKQOoDwMTB7EWmGC8BXY63gVbZpjLkF1bT2Maqm94_9tdS3sPQPcJ071SQ1m6BfSGEraSl6rgURhwMD_rB178gCvuJprP0qRJ9xm2yIEC_PSW1Ks5zjjd4_OQQXsEu-cyfqW0LBB6ITMfKBq1IjmFgPYeZxWjPk9J8Dk7bfl2mTRARyyO6JgBPKppEMiQrsZ8CRZxAncFWcBUtLEnNBjTRVyP54ymZv9poeG1E7WWfOw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚠️
ویدیو دیده نشده از لحظه حمله به بیت رهبری و ترور خامنه ای:
@News_Hut</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/69662" target="_blank">📅 09:15 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69661">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">app-release.apk</div>
  <div class="tg-doc-extra">4.5 MB</div>
</div>
<a href="https://t.me/news_hut/69661" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🎲
همین امشب با اولین شارژ
🤩
🤩
🤩
درصد شارژ بیشتر بگیر
همین الان شانست رو با موجودی اضافی امتحان کن حتما بزنده میشی
👌
👇🏻
👇🏻
🌐
Telegram
🎲
🌐
winro.io
🎲</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/69661" target="_blank">📅 02:00 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69660">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WCgz2Z0z8HUiKK5LSSF9GwX8mogcROM1ZFsq0qKZCmXpZu0L7G6PWweOFsIeO0HCBvou7v-7w-RsJq8xD61fe0QdlxDvdWchBVR8qRQrjOqdM7N9CTXVNil5ecvmJmFUZL7LqmUivu1KwnOIvGPhya0QMo7NMawqhePXaxDs4Km1eycxDibuRQZqmwiEQ0KeTwdfPBj-Rb9ecKawZrn7tOE7LdyOy1aQaQpjbOkeU0cdT4cCMshBbAtXydWted_vBrvsj4d7YsGZOAmnLNFbOuKHvOt3rJp4ZVYGt1q9iHDv9rMt-P2HA869PY57DM0DpTfNWkb2pe0MPSrNjOUovA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚠️
همین حالا موجودیتو
🤩
برابر کن
❌
☑️
۲/۵ میلیون شارژ کن ۱۰ میلیون شارژ شو
✅
برای اولین واریز تا 15 شهریور ،
0️⃣
0️⃣
3️⃣
درصد بیشتر در وینرو شارژ شو
🎁
✅
به ازای هر واریز در وینرو به ترتیب 300 ، 150 ، 75 درصد بیشتر شارژ شوید
.
🔊
با شارژ اضافی بدون ریسک بازی کن سرمایتو چند برابر کن
⚡️
🎲
ثبت نام آسان و سریع کلیک کنید
✅
پخش زنده‌ی تمام مسابقات
کلیک کنید
🎰
✅
درگاه اختصاصی برای کاربران
💰
🔊
اپلیکیشن حرفه ای
📱
🎲
معتبرترین سایت ایران
📱
کانال اخبار و هدایــا a15
🌟
📩
@winro_io
🎲</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/69660" target="_blank">📅 02:00 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69659">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RZy1sWyr8dgToAUx6veZUCSv42DqOxSY5HvpRqpNqKhrI00YxrAHMOd4oNY4SvoNmfSH7MYluwIca7BQOdgX163ofhFBE4uM6OHzkQVczcwECWfHvCN-vVX-EopXPY-RF8K0H-ZCc7_W6eCkqsvkyelSHOjgR6H8A_E1HV15FTNCnmIG5a3Y4GPb5gz99tGu4vkMZm0HFpQGjZLXkgdTxv-hbnWq0_3aORxut1q_TPauHElz6VdLTFQeW0wxV_X3CAqC5v7UKzxv3RHbbSQS8IYEloy0HPku3dDThW4DV9OiePZlpULJrXUtIAXPiH234z6YLOzR3CzkDjNeC-mCdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇸🇦
🇹🇷
🇵🇰
رویترز:
ترکیه، عربستان سعودی و پاکستان قرار است روز جمعه یک توافق‌نامه دفاعی مشترک امضا کنند.
@News_Hut</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/69659" target="_blank">📅 01:59 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69658">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qUc3_qyHpavKp8dR_A-njlK1he3OBp-oBhcDcLIZy9m-YePYTI_s7w7fWahhjZjDQNN_HR8VLi6tpz5uO_wM9cv5mB5aFoB_H9ldF0KnhO9vmJiFL-szMhJjJgWQuwhWOBQtoT6VB0a4x9TYrkxt4ta5yPluOhFVqg97vYeJVdmEYUG9q4kvRBHGRGEeoy4mbewt9Wc6V_CcYMXz_1Yk7cPuWWi-QXqcshXfsoL7jL2-lcwvJY4F1_45ksEANfCvXq1u2v1Lea0Oiz026HujW6gmiUzhtOCsWyYnuKgw-ZEmVlfbikADqcphsfdZaTZ8Ql3nAXERiOKZV_IVe7tmfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
سی‌ان‌ان:
🔴
یک مقام ارشد سعودی؛
اطلاعات موجود نشان می‌دهد سپاه پاسداران ایران در حال هماهنگی با شبه‌نظامیان مورد حمایت ایران در عراق و حوثی‌ها (انصارالله) در یمن برای تدارک حملاتی علیه عربستان سعودی است.
این مقام اظهار داشت که این گزارش‌ها به‌ویژه نگران‌کننده هستند، زیرا در شرایطی منتشر می‌شوند که ریاض در پی کاهش تنش و انجام مذاکرات صلح‌آمیز است؛
روندی که به گفته او، پیشرفتی مثبت داشته است. وی افزود که پادشاهی سعودی «برای اتخاذ تمامی تدابیر لازم جهت مقابله با هرگونه تجاوزی، درنگ نخواهد کرد.»
@News_Hut</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/69658" target="_blank">📅 01:48 · 16 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
