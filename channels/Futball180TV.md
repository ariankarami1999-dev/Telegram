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
<img src="https://cdn5.telesco.pe/file/VS9ycGDwkyM_LDGem8vnhrOOE_jlRKoWlSvqrL5s9crBUtc3-N1H-8ySSq4148fhEGpNwbvHMVLnC_1szn2mA1JbssfugsO3mb2CPgqS_plD4h6oSqDVO-klBkDNRey1aXTvw5yuANzyF_B0HDPYU825v4W9jnSkSLpYzBQYGJQvIVYas2oMig9nyFIe08Q5nS46tJExidY7wJtlb3nbRkSjRW9X-FwoSpk0FkeQi7UygY3t22kaMe-7XP0ZyjjdM9AAWkYXVbPbTVkRzKifefZUmYEXV50atURcd48OhDXcTlAna_SA5ANxVBmDUULS2GseMjcOHjxRyykyIg2j8w.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فوتبال 180</h1>
<p>@Futball180TV • 👥 424K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-16 04:01:21</div>
<hr>

<div class="tg-post" id="msg-105769">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/Futball180TV/105769" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 5.17K · <a href="https://t.me/Futball180TV/105769" target="_blank">📅 00:32 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105768">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AjJcXfc7PBbsulDmJrr6LLhAPqdV3RDdptwEfT7fkswwWmgINi_H91LezdbQXLt8L_WtrIkoFSY_yzlbzYv2rZ4Lcnz56Zva1Sccuk-uPRIzBXaXSQZMDD-52sRPckGBAStSRxLe2bCkHCfPTfUg3GcLdjlXL_rlXnLH4ZyXhe0n1XxFl7OinNzdpPur9wUhxJR-hv3P5AGbY9UiD76i4mEis3rtJysGPrj9XW9ETputT2sjSr0gPQo-qGwAbAvI7Hw40VFyldfONFFELGBz1mYWZktCj3I-46ej_Lb3eX1zmveopQzt77TI86dX_iDNh53G5ey3br9uUxCWzq3ojw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 5.26K · <a href="https://t.me/Futball180TV/105768" target="_blank">📅 00:32 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105767">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-footer">👁️ 5.48K · <a href="https://t.me/Futball180TV/105767" target="_blank">📅 00:29 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105766">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4e26f7c6c2.mp4?token=rB8-ARWLaKEzQ9KEQY3wm4uKzQ95cspBJennnTLUfPH7N6lL7byZNnH428l9_Ob9xDYcdOXUvpdjg30Nx_trks44SPPma9YRwo6STpQWpVlaARD_u1SVXBc_a0sSc71lFQMBlGOul6ohI8zWsd4_oHMk0p2Xes62QICzFestfRy6rTwO4mqmvrgK87klMfuknJHBXjdlMh34yZPEm3L2f0aDtErVGruBAGHhIP6Nypi6WclLsn7dQrkGfdsB8Iv_m-2n0FnVBvdAwub_MJMq4uGfLw01-pkCxz4SBUrZ8CA9bczJQoVpph2vqjrd6RHyrn4yENa5u1xuamCijC3CqA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4e26f7c6c2.mp4?token=rB8-ARWLaKEzQ9KEQY3wm4uKzQ95cspBJennnTLUfPH7N6lL7byZNnH428l9_Ob9xDYcdOXUvpdjg30Nx_trks44SPPma9YRwo6STpQWpVlaARD_u1SVXBc_a0sSc71lFQMBlGOul6ohI8zWsd4_oHMk0p2Xes62QICzFestfRy6rTwO4mqmvrgK87klMfuknJHBXjdlMh34yZPEm3L2f0aDtErVGruBAGHhIP6Nypi6WclLsn7dQrkGfdsB8Iv_m-2n0FnVBvdAwub_MJMq4uGfLw01-pkCxz4SBUrZ8CA9bczJQoVpph2vqjrd6RHyrn4yENa5u1xuamCijC3CqA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
‼️
🇮🇷
🇮🇷
سجده جیمی‌جامپ امشب نقش‌جهان با پرچم استقلال مقابل سیدحسین‌حسینی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.44K · <a href="https://t.me/Futball180TV/105766" target="_blank">📅 00:19 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105765">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Euv0MaNobX4O2MI4wNMG496ZI7d8FsU4eFRfQCdnpd_EauZoQTAl391hRO7Jo8JORCR0oK6n6HA2K1mMOFu3erk75zRdBNhSCk4YzSQDiY1fsBKocfIhpLYyuKePGBohGQGZt7Uc-Fpv3UJX1HZH0GfsHtm7sMpLXwEzDfetrMtrBrbsjNb_kUenxpPu2hTNp5HATIUWw9zpKrRxxkFtq1yaNMJOK_VzCFqtAV0iLD4g_lsXY9I5mBE-7q9CKzdC_Mrhfv-VYF4zd_FALPvCHH7QnDdw5nw-tYmAXUbIvWsun8o3QkOZcyVcJrNj-WRh-PMezRVxt6C8BbSJadI1Hg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یووه لحظات آخر مساویو زدددد</div>
<div class="tg-footer">👁️ 7.74K · <a href="https://t.me/Futball180TV/105765" target="_blank">📅 00:12 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105764">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">🇮🇹
گل‌اول میلان به یوونتوس توسط سیسه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.07K · <a href="https://t.me/Futball180TV/105764" target="_blank">📅 00:08 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105763">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/a702f2c4b3.mp4?token=MSaYAnQd4MMZM1GppG_Y8kBRBi3WQQ3OV6vH1Xal_O1t7SwiluPBhJ4Znx-7Q6UrfTE29r9_9CGIubr7x2x4KVJtq_yVqJYi6P3NyWJErPlI4XP7KXF-hmy-xd-nRI4QJ3GOF4jkEQHDKUO69dT6m_a7YRLAvhlkfb1vMFmET9lllmpxtRRMdAV-eYOAqECQVIQyMfPk429PY8k3JsW0-evhPQjKHBr0I0Ujb_Lq6rio5_68Lwf-5qb11k-XO7LIWE3v5qjAu8nY2kVBBo8cLaDzAtVc78aN3ASBQpWBDCPY3MMZ6HobFqnTZshEHEfBBWUMxKtP7vj3lIw3s3GylA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/a702f2c4b3.mp4?token=MSaYAnQd4MMZM1GppG_Y8kBRBi3WQQ3OV6vH1Xal_O1t7SwiluPBhJ4Znx-7Q6UrfTE29r9_9CGIubr7x2x4KVJtq_yVqJYi6P3NyWJErPlI4XP7KXF-hmy-xd-nRI4QJ3GOF4jkEQHDKUO69dT6m_a7YRLAvhlkfb1vMFmET9lllmpxtRRMdAV-eYOAqECQVIQyMfPk429PY8k3JsW0-evhPQjKHBr0I0Ujb_Lq6rio5_68Lwf-5qb11k-XO7LIWE3v5qjAu8nY2kVBBo8cLaDzAtVc78aN3ASBQpWBDCPY3MMZ6HobFqnTZshEHEfBBWUMxKtP7vj3lIw3s3GylA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇹
گل‌اول میلان به یوونتوس توسط سیسه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.36K · <a href="https://t.me/Futball180TV/105763" target="_blank">📅 23:52 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105762">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🚨
🚨
🚨
🚨
‼️
🇮🇷
🇮🇷
پیروز قربانی: من به توافقات قبلی کاری ندارم، خلیفه و گودرزی رو نیم فصل به استقلال نمی‌دم.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/Futball180TV/105762" target="_blank">📅 23:45 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105761">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/02ce7af3d1.mp4?token=uEQ1UDYvyW1ccS5RysolhJrF2IwUd92w81KPtL-X_shVHibgza_iaXK7S2nzEmtLpmox_t6E7berzkmHNheObqG6wPywc57e9k6Y8N7kdK1XR6atRiwHhmN4SnNaWHPfbcvoktAd2kqj8RLZr9sRi4OAlWgqaOVnk2vH6r-tEvyLMnuwoCTwKCa5XnerVFLydqrgEeCqqTndMUVM_1GxMnvVm0obJ_q6bk85Tnq4etYjoZAXNTjy_ud_QnJCBXda0loYCWOz2MHGymFHAuqSHnw3Y6QFyhZVNpysyksHBR5l5PCjIQOkrhSPUtbOe2kxEE5Dt0xGgbvbHkGlfrFmQg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/02ce7af3d1.mp4?token=uEQ1UDYvyW1ccS5RysolhJrF2IwUd92w81KPtL-X_shVHibgza_iaXK7S2nzEmtLpmox_t6E7berzkmHNheObqG6wPywc57e9k6Y8N7kdK1XR6atRiwHhmN4SnNaWHPfbcvoktAd2kqj8RLZr9sRi4OAlWgqaOVnk2vH6r-tEvyLMnuwoCTwKCa5XnerVFLydqrgEeCqqTndMUVM_1GxMnvVm0obJ_q6bk85Tnq4etYjoZAXNTjy_ud_QnJCBXda0loYCWOz2MHGymFHAuqSHnw3Y6QFyhZVNpysyksHBR5l5PCjIQOkrhSPUtbOe2kxEE5Dt0xGgbvbHkGlfrFmQg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇷
🇮🇷
واکنش عارف حاجی‌عیدی به جنجال در بازی با استقلال: والا یه ۱۰ نفر بهم فوش ناموسی دادن!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/Futball180TV/105761" target="_blank">📅 23:36 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105760">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1098753ac8.mp4?token=nwioSKSdolqezthpb55UEr7iVkUVQH7C2h6wxBnMxazYG_06nPFtRrrfLLQhKzJalci1bSOL-iHBGNUUjLUNxTlDUgVWp1DxGqHPBGy1B9h0BArIGx6f2Q2xSVyDEIWkkNCFqqQU0pGB80SmPq0YaOPTWz_1A1c-OqZHIbHpUk5XIf9IH879_gcQsDPqyM5QFS7YATbIdsDltGcBDjUXApmqVWe3FMxv3KdxsQhxaR4bErc1w2Bf0ez-MChRFA6bjS2sHcfJ5isGAW28xiP5A9VLST2f-6KcXcM_NLyDG9zHhjEQPbYfrTDxQdI6LqyXN3jZft7XlSqRsu4ys-XttA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1098753ac8.mp4?token=nwioSKSdolqezthpb55UEr7iVkUVQH7C2h6wxBnMxazYG_06nPFtRrrfLLQhKzJalci1bSOL-iHBGNUUjLUNxTlDUgVWp1DxGqHPBGy1B9h0BArIGx6f2Q2xSVyDEIWkkNCFqqQU0pGB80SmPq0YaOPTWz_1A1c-OqZHIbHpUk5XIf9IH879_gcQsDPqyM5QFS7YATbIdsDltGcBDjUXApmqVWe3FMxv3KdxsQhxaR4bErc1w2Bf0ez-MChRFA6bjS2sHcfJ5isGAW28xiP5A9VLST2f-6KcXcM_NLyDG9zHhjEQPbYfrTDxQdI6LqyXN3jZft7XlSqRsu4ys-XttA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🙂
واکنش پیروز قربانی به پخش آهنگ "نصرالله معین" در نشست خبری بعد از بازی با استقلال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/Futball180TV/105760" target="_blank">📅 23:16 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105759">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">‼️
🚨
🇮🇷
🇮🇷
محمد خلیفه: تفاهم‌نامه بین استقلال و آلومینیوم خیلی صددرصد نیست چون ممکن است استقلال مرا نخواهد یا یکسری اتفاقات بیفتد. حتی اگر قرار شد بیرانوند به استقلال بیاید، با او رقابت می‌کنم.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/Futball180TV/105759" target="_blank">📅 22:52 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105758">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e1b9ee8002.mp4?token=KhUMfLY8bKZHZ1n-ZD8IuxWKGDos0ZPg5GloZZK0SwTuqkj0mhdS7SkNig2gQCz7ONvo2yHWaPGNLGTMxYORYf9mZ99nAEwtWCr9lqjb8g2nLIxl8Y_qtjA3Tg-hbYgX-xLCpsbws2QMPKdjIePO_C5qsfv-ySyz4W50V9sXMGZPNiQJEfejrV3YN3xAFc8plj3P-qPrSc7NDT28QYsGhd18j5gKTx6A3GFfnrEduMbU2cTQ5dAi-bMuSPL1wcUhp3n2HpJ87GPgr8ltZzlGEpHnlc2j6UOBUMVQ6MoN52H0Te3QVAfX97oHqSjCMOHakEw5tDhgw09BRQJoYUa7VA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e1b9ee8002.mp4?token=KhUMfLY8bKZHZ1n-ZD8IuxWKGDos0ZPg5GloZZK0SwTuqkj0mhdS7SkNig2gQCz7ONvo2yHWaPGNLGTMxYORYf9mZ99nAEwtWCr9lqjb8g2nLIxl8Y_qtjA3Tg-hbYgX-xLCpsbws2QMPKdjIePO_C5qsfv-ySyz4W50V9sXMGZPNiQJEfejrV3YN3xAFc8plj3P-qPrSc7NDT28QYsGhd18j5gKTx6A3GFfnrEduMbU2cTQ5dAi-bMuSPL1wcUhp3n2HpJ87GPgr8ltZzlGEpHnlc2j6UOBUMVQ6MoN52H0Te3QVAfX97oHqSjCMOHakEw5tDhgw09BRQJoYUa7VA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🚨
‼️
🇮🇷
🇮🇷
پیروز قربانی: من به توافقات قبلی کاری ندارم، خلیفه و گودرزی رو نیم فصل به استقلال نمی‌دم
.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/Futball180TV/105758" target="_blank">📅 21:57 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105757">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/juKIVo_4KAZnj0Kw-j6dMKKXWem2X88pJpvuenRiilGx4OsEUKWfpZn-FC_kr0F4fWSVDxURtWCgDUvYOADoQ0BGNHXJtyNQbf6v6CgVKnf0w4kAChT5gek2c2PpfhzqM6WBTQjtkqzelMrUNBqNyGWALR9GzvXm5SBe4pyHHGDK0IC11CClk_pn_uRn724ZoPjCRMq2Bo73HuBb91r9OjszfQK7ckWmhfoDpPRNlwkV4D9cX264efM6vXOwdFU90HqZcB_I-YbohSshTsUJB2Ksysnv_MP6GyPb2XpNA-wKmvYpYtoFXtHA8duMmVz3Hz3J0HgfQoisVkHZpcUmCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📊
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#فکت
؛ آرسنال در ده بازی متوالی لیگ‌برتر مقابل چلسی شکست‌ناپذیر بوده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/Futball180TV/105757" target="_blank">📅 21:31 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105756">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">‼️
🚨
💙
بیزاتی مربی استقلال: ما هم از نتیجه خوشحال نیستیم. قطعا مشکل گلزنی را حل می‌کنیم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/Futball180TV/105756" target="_blank">📅 21:26 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105754">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/09d4a38935.mp4?token=L8GlpZ2kW-duBpQsdTprfVM3FFHs9buGOvP0gpC_MAbLAoFFjdya8rlNWoT2SAUlpm9W2myDnoKsj-AQKnUx7AVA7FdaMzY9gB4UK62QFAEpmZfruBrePdY3wdxQ47sPVDwDz4otXOPNi06xFPUm6r-8z55wkgV0zD8Wyu0r4fKZd7Tig61SA45u-MHNu_XmhGkbokyEOYEP3npFMrexUEG-Ss-LHC-_EDVyQOGjEd8-gQAJdErlK_o1ZiHndSQXsWi0CdsUn8VYLJ8mcDPsbgwCrxSqPdxmfMkrcNnM7WCxJJAUOphZ3TIECTzR8ZMBLd2h57sIQiIeJ6F6AIE10g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/09d4a38935.mp4?token=L8GlpZ2kW-duBpQsdTprfVM3FFHs9buGOvP0gpC_MAbLAoFFjdya8rlNWoT2SAUlpm9W2myDnoKsj-AQKnUx7AVA7FdaMzY9gB4UK62QFAEpmZfruBrePdY3wdxQ47sPVDwDz4otXOPNi06xFPUm6r-8z55wkgV0zD8Wyu0r4fKZd7Tig61SA45u-MHNu_XmhGkbokyEOYEP3npFMrexUEG-Ss-LHC-_EDVyQOGjEd8-gQAJdErlK_o1ZiHndSQXsWi0CdsUn8VYLJ8mcDPsbgwCrxSqPdxmfMkrcNnM7WCxJJAUOphZ3TIECTzR8ZMBLd2h57sIQiIeJ6F6AIE10g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
⭕️
⭕️
⭕️
نرخ سوم بنزین به مبلغ 10 هزار تومان تغییر کرد؛ سهمیه اول و دوم بدون تغییر
سخنگوی دولت جمهوری اسلامی: نرخ کارت جایگاه سوخت از بامداد ۱۷ شهریور به ۱۰ هزار تومان افزایش خواهد یافت.
در جلسات کارشناسی اعداد متفاوتی گفته می‌شد اما چون رئیس‌جمهور به مردم قول داده بود همان ۱۰ هزار تومان تعیین شد.
۶۰ لیتر بنزین ۱۵۰۰ تومان و ۵۰ لیتر بنزین ۳۰۰۰ تومان همچنان بدون تغییر ماند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/Futball180TV/105754" target="_blank">📅 21:18 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105753">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eDB7L1An7lCNMD4kyPhtvF6UpUhArhE7HxO4rlc980HSs54hS7z9wWlCwLTBiclg5_fgLjnF25FITKCjq5otQmMUUNIKRVMyD3IPat5RObl3a5rEms8CekjqrpURYkpoHGGktRVIWGN4wHwZ0A4NM-b3RS93QNCXvIaeK4RrUr1Uc-UCbHzbpEuDnXpFth3yfYS6CzzvsR-HciUcl_Y1YmeojC1oCOGkia-4BwMo5iFDaEpYwTxcKH-rShAweS9-ovH_QBkoC9yqmoPNm_xr4i71tUlRr4mbg4NyCldHu5ldfXmGp2HwthSw-7l0E06w-uTdYiqMU_K2vT5S4RrOGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
هفته‌ششم‌لیگ‌برتر فوتبال؛ به یاد دوران مساوی‌های متوالی با فرهاد مجیدی؛ استقلال و سهراب در آستانه به صدا در آمدن زنگ خطر قرار گرفتند!
🇮🇷
استقلال
😏
-
😏
آلومینیوم
🇮🇷
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/Futball180TV/105753" target="_blank">📅 20:57 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105752">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DW08QMxxV-xjOaFcJIHvy7WN6kBE-9L1hscQ-IBdPoeFQcJK0wmp1rBfs2iqXUp2ZwFUGbQBcGLzp6UcQV7_5pLFzWUwD8-kpNyALwiPlH-_SEI6Tzhj5lLpIsR1mwlOzuBfIG8h-XJReOEz-xVmX3rRZPOAKRCit1cYjsVZkYdgF9UivZisLef8dTx9B4XyhrMmuIjF80ef6IZHik1TDwQrB8819IactIGhw85JGp-S48UcLx9nEPMyAUTDJtjFDcG6FriXt2LkwS4Sx2rkv_qSyqsDabpjOwpdwjE6THkwqCHIY4N7b_j_HiiNcVQs2cODwZZctMnZBKYZwxbkLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
هفته‌ششم‌لیگ‌برتر فوتبال؛ به یاد دوران مساوی‌های متوالی با فرهاد مجیدی؛ استقلال و سهراب در آستانه به صدا در آمدن زنگ خطر قرار گرفتند!
🇮🇷
استقلال
😏
-
😏
آلومینیوم
🇮🇷
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/Futball180TV/105752" target="_blank">📅 20:53 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105751">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">مرحوم ماشاریپوف برای استقلال به زمین اومد</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/Futball180TV/105751" target="_blank">📅 20:36 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105750">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">مرحوم ماشاریپوف برای استقلال به زمین اومد</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/Futball180TV/105750" target="_blank">📅 20:36 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105749">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7c5e1fcdc1.mp4?token=hRcS6gAiyz-2gMSZbEciu8zi0Psq9Yz5cNz0CPkeFOa8MGA4Yffbpz_630p66qEhXKnMPDvbWygrDzfU0yyYnI21bhIO9mmbpSXJtKdjuJP8IfOtilbI2OaHW50_E7zONROAZRkp9ik8EYuxT-EQiZ94sQiKvoLRSlv4I1Wd4UWK77dm6j759DZGHtMyMDHNB6kxQZicAViy3IvLhOow_4cai-73Co03RJOV0W0l4msnn7lSOMZ2LpURNgueN1EMQb30KWt6Syj9A8qHIpxQq8KRQKCAfK_R1iGjbVgG-wCkuP146SSDvcdhTvaP_36v9lPUusUUrZpvOqiSbvPASA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7c5e1fcdc1.mp4?token=hRcS6gAiyz-2gMSZbEciu8zi0Psq9Yz5cNz0CPkeFOa8MGA4Yffbpz_630p66qEhXKnMPDvbWygrDzfU0yyYnI21bhIO9mmbpSXJtKdjuJP8IfOtilbI2OaHW50_E7zONROAZRkp9ik8EYuxT-EQiZ94sQiKvoLRSlv4I1Wd4UWK77dm6j759DZGHtMyMDHNB6kxQZicAViy3IvLhOow_4cai-73Co03RJOV0W0l4msnn7lSOMZ2LpURNgueN1EMQb30KWt6Syj9A8qHIpxQq8KRQKCAfK_R1iGjbVgG-wCkuP146SSDvcdhTvaP_36v9lPUusUUrZpvOqiSbvPASA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
😆
😆
گزارشگر اراک: محمد خلیفه ما رو یاد جوانی‌های مانوئل نویر میندازه!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/105749" target="_blank">📅 20:27 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105748">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d287258445.mp4?token=fClqUjKGRTMdnBiDASaTZZJ14w1tQG3OWVUUwBSB80jTIuvrm9CwcrNtfuWl6fdw9valzdANujYyytDI1I5C048src_99LkgFVmgnd4KGq-Rmn3LT7p1o2zaVzJ_6F1ns0BbA6diBu0GP7NhT25ddh5ZKXzHUgJfCyTD9fK_3kjD_aRncSLlsa_dCo5ZSoSTmcG4jiPfekf1G_DVdhWxLRCfKTy2JAmdyHgALutqFXlQLa5tQW796VcXIHd4PQGmLHnz03RoYdXwgYYLU3MGttZM3ysFhrJYPNLOPkhoCqToEGn7BBcifvSozfaglT1zxX5p68WG95Vypr4SO_PbxA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d287258445.mp4?token=fClqUjKGRTMdnBiDASaTZZJ14w1tQG3OWVUUwBSB80jTIuvrm9CwcrNtfuWl6fdw9valzdANujYyytDI1I5C048src_99LkgFVmgnd4KGq-Rmn3LT7p1o2zaVzJ_6F1ns0BbA6diBu0GP7NhT25ddh5ZKXzHUgJfCyTD9fK_3kjD_aRncSLlsa_dCo5ZSoSTmcG4jiPfekf1G_DVdhWxLRCfKTy2JAmdyHgALutqFXlQLa5tQW796VcXIHd4PQGmLHnz03RoYdXwgYYLU3MGttZM3ysFhrJYPNLOPkhoCqToEGn7BBcifvSozfaglT1zxX5p68WG95Vypr4SO_PbxA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
استقلال از کوووووون آورد
😐
😐
😐
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/Futball180TV/105748" target="_blank">📅 20:25 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105747">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">استقلال داشت سوپرگل میخورد
😐
😐
😐</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/105747" target="_blank">📅 20:23 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105746">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">واااااای</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/105746" target="_blank">📅 20:23 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105745">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/da0209e41e.mp4?token=sllSOAdWdGdgIYui2qNcyVSnb2WCPLGyKiG51sJbjkLp0_bmhAPK5Kdc2A77BqYo-_3fKdUghPHA8lFoY4AkOg-iR6pH6RfWCZ8kzvxpYm6CnMNPPr0wl-Wqp_J8vT7N1ggUHo9xK-MVmRmZ4w8cgeX4MDkAuxU_tV_X8JDtgg3KgQxU6LQpZCF07t3zbOcNCwoJUGvTKQP9AgFa1tegRPyybEm7HcGhsHNyle9p1rKBh3gh95cO41bA-fxj5BjssYNIBPqCrlb1fYfBPhsjIJcpFNcMojKNVugOY4AXHDJbmKLyXr5ynK98jx5WtUARa8TT6rh6a0SUlWv5ei01Gg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/da0209e41e.mp4?token=sllSOAdWdGdgIYui2qNcyVSnb2WCPLGyKiG51sJbjkLp0_bmhAPK5Kdc2A77BqYo-_3fKdUghPHA8lFoY4AkOg-iR6pH6RfWCZ8kzvxpYm6CnMNPPr0wl-Wqp_J8vT7N1ggUHo9xK-MVmRmZ4w8cgeX4MDkAuxU_tV_X8JDtgg3KgQxU6LQpZCF07t3zbOcNCwoJUGvTKQP9AgFa1tegRPyybEm7HcGhsHNyle9p1rKBh3gh95cO41bA-fxj5BjssYNIBPqCrlb1fYfBPhsjIJcpFNcMojKNVugOY4AXHDJbmKLyXr5ynK98jx5WtUARa8TT6rh6a0SUlWv5ei01Gg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
گل‌اول سپاهان به استقلال خوزستان توسط لیموچی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/Futball180TV/105745" target="_blank">📅 20:20 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105744">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/cb815a8901.mp4?token=Gy6qlOIsf7pbGqib2KwapZpFleulqt3qyRyjU507V0cF0IZ07a575WaZm4nboRX5IqRuaonOm9l110MbB8Sue4JUXQiA59lsQZdhSZTqoudgNOGxwutB1e8WjSKgBLavJEkjCF4YhQzyZiehXf_IFwQJ7tklFTJBA6G_LUWevBkwigONN604XDlXuwVreYQ0XCdSlrqUHNb0GFlhl7yW-uNOH4qqwJYmIXWpvXVrxVkNXMyDjs9QvaVkKcNVHRxzgRumY_mnmJMYytLcBY7CtSOiyuR-Vvz7NftmUMm4NWmC45RfMphdDrIPDGhPDX1q4fU0CQ4nl1-W0wTIw8kfGQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/cb815a8901.mp4?token=Gy6qlOIsf7pbGqib2KwapZpFleulqt3qyRyjU507V0cF0IZ07a575WaZm4nboRX5IqRuaonOm9l110MbB8Sue4JUXQiA59lsQZdhSZTqoudgNOGxwutB1e8WjSKgBLavJEkjCF4YhQzyZiehXf_IFwQJ7tklFTJBA6G_LUWevBkwigONN604XDlXuwVreYQ0XCdSlrqUHNb0GFlhl7yW-uNOH4qqwJYmIXWpvXVrxVkNXMyDjs9QvaVkKcNVHRxzgRumY_mnmJMYytLcBY7CtSOiyuR-Vvz7NftmUMm4NWmC45RfMphdDrIPDGhPDX1q4fU0CQ4nl1-W0wTIw8kfGQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
گل‌دوم آرسنال به چلسی توسط مارتین اودگارد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/Futball180TV/105744" target="_blank">📅 20:15 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105743">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">اودگارد گل دوم آرسنال رو زدددددد</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/Futball180TV/105743" target="_blank">📅 20:14 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105742">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OQF6NiBxa01yP4FgX97lU0CrTx_ITlTOQlkjkrHhRGteE6nRXYhiBiTK1wX8KrHQVUObaxLds6RlanlMDX9lLTwRNXTk0GTa_HvKP4tl4nUElWiwHXm4UvxxaT7N9-_ZslLb-WhL-TMomoXS4kZpe0gvMw9F27Iy3rp_3fbRkzj39Y6TTbldXPibWJ2imoveALJqkGITd7Cggk_GN6PlkUSWFFGwMmksLfTW3wTne2JvLNHwEmNg0OwKZ5_4xDiEtdA3S_88NC3C51hlTamBrX2VAG_80x6psyUC44XqFjbwHzYRckgzhtycCpoBO2oP19KudN6rkk34hEd7deQisw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
📊
🌟
مربیانی که بیشترین تعداد پیروزی را در بارسلونا کسب کرده‌اند، پس از انجام 80 بازی در لیگ:
🥇
1- فلیک (63)
🥈
2- انریکه (62)
🥉
3- گواردیولا (61)
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/Futball180TV/105742" target="_blank">📅 20:02 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105741">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sAYGKhLVkgXWaK5qySRmn7UApOiBmBEGAcay7kB3En7Shjtm7Q9jxFBM84_aMXIJAs-R0KMR5WAiZSdcoZZpZcIPThV8HjTSqUrMTaayzcev27iFz2p0i2OJSi7QMCQudyJEiXA1lz2me8b8i72y-RLTvdzo2jBq5171XDd6HnJPkdmxFmlAlKiM-ZW4nrjtkoReLyPkx5qizmuZejQHc9TXlrmvn5vQtNx9IilK2XPh-qy8q2oRx8pM_lv3y867FJxbgjWdHXLUcqHBJxnSD_jpSOFl7lmiKQLnEfy_Pv3bigcSM7tPtABCGtnuG2ydZiPHzHDpjC8bpvC-MCYEUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⚽️
هفته‌چهارم
لالیگا| خفاش‌ها اسیر درخشش فرمین و یامال شدند؛ نمایش فوق‌العاده شاگردان فلیک در مستایا
🇪🇸
والنسیا صفر - بارسلونا پنج
🇪🇸
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/Futball180TV/105741" target="_blank">📅 19:48 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105740">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/e47c1a3826.mp4?token=QdmHmIvfUsfmBkfYYTe18_gzr4llyf-e8YtQp2Tx0ALpQVfmVwCFe41jHu5A4zsSn9CfM4UA_EphHVx4w5z91vBfslwnZL9Joax5f9nNG-h3SkKyrbEzHk2tOkEk8PYZ5TGGjZeKVFXc-KUpRhWAt4ZwWJII0IW1n_PLHGv4KTm1pn3jbwyDrDZ1VWiuNuXVs8IhHJn-56ZQYlrGEt3sdDmou_Cz2fLb0xacBRaTV-Ahq2lsm0--w_pd27f1YhiPu-ujuiJTXyn9iQmudWabOfG8iwnNZHpCitLayuSjcIwXjAjk-ZxMqeMlA4AkgKaGnU4WLrvgmHd8if48UkG34QiywPs4lswzChsuh3sFEP68i7OCXbM6anENeY_npyvX8UphwD340ChtMolCxj6yAJJRKnGuHAnJ3EvKrvSFcQEHl2wAbdcUSNnJZJ4SsQUXYmZ_vTJKlpzB5bgoamf02vOp5PWpHrDmLd0iGc6fmb1W5t9hNFpcveD7tKt8-QF2JlgpPPmYjVrNjr_5w_xEOsye3Hie92BZ4Ch0JwADqIvG8D9Lzc0M9ezrgm6itB3S8MmfgbhjWx3BZJ9W04KymLILofsFJnkJnUFkn6-dIedH_OTgzxWW_8Bx5s3uhDKFsUwi1dvgSOXUhCtrI07tAWdtLbJpqkVeUb2k1XGRsiY" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/e47c1a3826.mp4?token=QdmHmIvfUsfmBkfYYTe18_gzr4llyf-e8YtQp2Tx0ALpQVfmVwCFe41jHu5A4zsSn9CfM4UA_EphHVx4w5z91vBfslwnZL9Joax5f9nNG-h3SkKyrbEzHk2tOkEk8PYZ5TGGjZeKVFXc-KUpRhWAt4ZwWJII0IW1n_PLHGv4KTm1pn3jbwyDrDZ1VWiuNuXVs8IhHJn-56ZQYlrGEt3sdDmou_Cz2fLb0xacBRaTV-Ahq2lsm0--w_pd27f1YhiPu-ujuiJTXyn9iQmudWabOfG8iwnNZHpCitLayuSjcIwXjAjk-ZxMqeMlA4AkgKaGnU4WLrvgmHd8if48UkG34QiywPs4lswzChsuh3sFEP68i7OCXbM6anENeY_npyvX8UphwD340ChtMolCxj6yAJJRKnGuHAnJ3EvKrvSFcQEHl2wAbdcUSNnJZJ4SsQUXYmZ_vTJKlpzB5bgoamf02vOp5PWpHrDmLd0iGc6fmb1W5t9hNFpcveD7tKt8-QF2JlgpPPmYjVrNjr_5w_xEOsye3Hie92BZ4Ch0JwADqIvG8D9Lzc0M9ezrgm6itB3S8MmfgbhjWx3BZJ9W04KymLILofsFJnkJnUFkn6-dIedH_OTgzxWW_8Bx5s3uhDKFsUwi1dvgSOXUhCtrI07tAWdtLbJpqkVeUb2k1XGRsiY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گل‌پنجم بارسلونا به والنسیا توسط لامین‌یامال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/Futball180TV/105740" target="_blank">📅 19:39 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105739">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tBaEvmKnOjt8TazL1hm7ydUoZEMC1uAORIMxuEa6Z7Fh1vCBR8pVu3GeWG7h075tAPToPx4vqJDIapjslP1CZ2cR4XMlH_CrlSAtt6NCSr8tYEBTCVq6qu3Scoq6qtFtzS4bAkWf-K4SMH-PI8tfxbMdGRdc4fHd2VeVg_EPYMAmg4SjikO-sq9Yu1sZ33RteUmRPVOAAiqVIS75oBOtusK_G_rtxfCrtflxLFVbJPsWIhyhzffTFoOMvtA0e6jmVCz1UYeoSXP34_jQDipahE23SpLjyzCoVCYTWFNexogWQBPfuhcKaR0SjknmPoPil7bRM2h3mJ-WIM1bGwkWcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
⚽️
لامین یامال به صدمین گل یا پاس گل خود با پیراهن باشگاه بارسلونا رسید.
فقط در 19 سالگی!
🤯
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/Futball180TV/105739" target="_blank">📅 19:37 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105738">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">لامین‌یامال زدددد</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/Futball180TV/105738" target="_blank">📅 19:36 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105737">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">بارساااا ۵۵۵۵۵</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/Futball180TV/105737" target="_blank">📅 19:35 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105736">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">گلگلگگلگلگلگلگگلگل</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/Futball180TV/105736" target="_blank">📅 19:35 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105735">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/db8af8559a.mp4?token=dzltKCYOi7AA-a_Q0RBu2nc5FGAthN59qXCi6d2M_O0bEae-BahtAY7VqZLfDIPxYsV3JL74OH9f1rwebpAas5ExsdExMC2A_jYacOvatrfcI7Y9t0_N8GtMRrNkF0PH9CpTjtd8oK5VSwCxEaeA9LxpfuZM_tVN65YsebJcWJy1bct4SFfyfydRm8rRBtZWxtDSzROhk68Pi9rD09CftMRVRhNENn_BIUyld50YSYt0UCDwEEk-YAoI9MaRv_FEh_5tB14khbciNfRwYcjcIeiQ3tUW048yQF1D5ktaiV3c1mip8-GLJawWgz_qeBoj7SIUTSiCvWyKfOmN0nXIJEQCaU9ZUhO8_COU0W2fAwHCUyJNqmsqVR1d-VX0LvvllCN4gzNVFrQcDGiQGAYEiEgroqmXBE7ZExWc_ypSYz4NOSq1p8Jnu-SrB7iqV4dODe9p9RMRNHcZTLW8E8cp7eQOwrt3lCuxDQeaXjXedXJvwxBx6tjdqmiYkiZu0URPu5OTYrgI0TbPrfhppGlqAAZQ8n_Gy6aoZa9aTJM5NOheaKHn_a9m362qs6a2CBOaVbKEKB6cS7xAgrjXXJpOz0ulNLIqcTCGc-gTtic8VL52OPhEOsjkM6R_EJjlCZ7zFZBSx6kSZxsRYJA0zbJNAgVwJjQ7itgpoyUy_NhlZeY" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/db8af8559a.mp4?token=dzltKCYOi7AA-a_Q0RBu2nc5FGAthN59qXCi6d2M_O0bEae-BahtAY7VqZLfDIPxYsV3JL74OH9f1rwebpAas5ExsdExMC2A_jYacOvatrfcI7Y9t0_N8GtMRrNkF0PH9CpTjtd8oK5VSwCxEaeA9LxpfuZM_tVN65YsebJcWJy1bct4SFfyfydRm8rRBtZWxtDSzROhk68Pi9rD09CftMRVRhNENn_BIUyld50YSYt0UCDwEEk-YAoI9MaRv_FEh_5tB14khbciNfRwYcjcIeiQ3tUW048yQF1D5ktaiV3c1mip8-GLJawWgz_qeBoj7SIUTSiCvWyKfOmN0nXIJEQCaU9ZUhO8_COU0W2fAwHCUyJNqmsqVR1d-VX0LvvllCN4gzNVFrQcDGiQGAYEiEgroqmXBE7ZExWc_ypSYz4NOSq1p8Jnu-SrB7iqV4dODe9p9RMRNHcZTLW8E8cp7eQOwrt3lCuxDQeaXjXedXJvwxBx6tjdqmiYkiZu0URPu5OTYrgI0TbPrfhppGlqAAZQ8n_Gy6aoZa9aTJM5NOheaKHn_a9m362qs6a2CBOaVbKEKB6cS7xAgrjXXJpOz0ulNLIqcTCGc-gTtic8VL52OPhEOsjkM6R_EJjlCZ7zFZBSx6kSZxsRYJA0zbJNAgVwJjQ7itgpoyUy_NhlZeY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🇪🇸
گل‌چهارم بارسلونا توسط پدری
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/Futball180TV/105735" target="_blank">📅 19:35 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105734">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a50ec1141f.mp4?token=agKojHqNLzcluoLmh1pqBvQbugF96GJeQFR_vOecyOmzXy2zsmjrna8jSogQu7LUbEljQ8kK09l3UTpZRlKoKqyTcQmtoapSH0O642McDWWhNewpbbffg-sqx5ibl4gNpKey0vxu3wwCBcQwTIsNBNN0I3ZQf-B_sMauu9Nm3E8rmgz8cSsTHG4JGe5LPGuYCkf_9Lce_oeZLgRIcJpIJu4b1KdNuwk_G5tr9U0RwUFo17Ag3MnHOqUF68m_26cN2cltx6_QNj9av_IeaITkQEBOL9IC00uIPZLFfzEmAzjOJTL96BU8EIao6AJUaJFsoTpTfipxFvS_1LgbVT8ThA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a50ec1141f.mp4?token=agKojHqNLzcluoLmh1pqBvQbugF96GJeQFR_vOecyOmzXy2zsmjrna8jSogQu7LUbEljQ8kK09l3UTpZRlKoKqyTcQmtoapSH0O642McDWWhNewpbbffg-sqx5ibl4gNpKey0vxu3wwCBcQwTIsNBNN0I3ZQf-B_sMauu9Nm3E8rmgz8cSsTHG4JGe5LPGuYCkf_9Lce_oeZLgRIcJpIJu4b1KdNuwk_G5tr9U0RwUFo17Ag3MnHOqUF68m_26cN2cltx6_QNj9av_IeaITkQEBOL9IC00uIPZLFfzEmAzjOJTL96BU8EIao6AJUaJFsoTpTfipxFvS_1LgbVT8ThA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یا حضرت محمد خلیفه
😐
😐
😐
😐
😐
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/Futball180TV/105734" target="_blank">📅 19:33 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105733">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">یا حضرت عباس پشمامممم ریختتتتت
😐
😐
😐
🔥</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/Futball180TV/105733" target="_blank">📅 19:33 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105732">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">محمد خلیفه چه توپی گرفتتتتتت
😐
😐
😐
😐</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/Futball180TV/105732" target="_blank">📅 19:33 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105731">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">پشمامممممممم
😐
😐
😐
😐
😐
😐</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/Futball180TV/105731" target="_blank">📅 19:32 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105730">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/89f570dcbd.mp4?token=U9xmNVFzb3gslgwufpzbjP131UVzQhoTWeCsCWkW2xsjR2gvnVXs-BQ6YQSYox8yI5vcMyfBOXVSCeluvxRcaNhsyDwEAVCuijJA8Vv8Vo-stDvW0lvgdXgSTtoOyR2TA_JI7ZaKqrPsJDvXEcijQCjr8USZJQLDjGaGDrTCswVPyyE-6FUwpxjTloxBQf1IF4_e8_9rRDM1s6V9tw-wXm--sLzrWQ7kv1ObgQXlzd2GfBiWi5wwBwlac9Ey8F1-wjbpq7v84dpxfHe29pSRMwkYdmUztSBP1aLZxHbx9kBvYA89KWscWvShNil8iwyAPu5SxmcX2kjc9-32YfB8XbtOlb_ggSYFaQr3adnqLS5theSn9rAEuX4L1JCRofACVPskM6WkdYXR8_1U7Q65Rf4Xgz8QFkNp2H0qXUADemyAs3obTkXphngSLRH3T7dVdEqT22EU-gFiwoxd04fBlfv5X1MJcS6OCf-XIC5YlC9nxG7KkyYLWRA8i3Lufpy3AfvF4UjzmaaRv0j6DjNvj7hcj4UCSp_ovD6C3durMCKMt7xCt8TPNL1HbaIEavoscqANs6pHj8pPAZgLvWQkui1ZwpsKklJY41L9PkjgsfBN2FIfwmE6wkiyki-ENtKyTAI9RLK62SGfx17FXWXRfLTwRZ8015tOcu7yDdtun-o" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/89f570dcbd.mp4?token=U9xmNVFzb3gslgwufpzbjP131UVzQhoTWeCsCWkW2xsjR2gvnVXs-BQ6YQSYox8yI5vcMyfBOXVSCeluvxRcaNhsyDwEAVCuijJA8Vv8Vo-stDvW0lvgdXgSTtoOyR2TA_JI7ZaKqrPsJDvXEcijQCjr8USZJQLDjGaGDrTCswVPyyE-6FUwpxjTloxBQf1IF4_e8_9rRDM1s6V9tw-wXm--sLzrWQ7kv1ObgQXlzd2GfBiWi5wwBwlac9Ey8F1-wjbpq7v84dpxfHe29pSRMwkYdmUztSBP1aLZxHbx9kBvYA89KWscWvShNil8iwyAPu5SxmcX2kjc9-32YfB8XbtOlb_ggSYFaQr3adnqLS5theSn9rAEuX4L1JCRofACVPskM6WkdYXR8_1U7Q65Rf4Xgz8QFkNp2H0qXUADemyAs3obTkXphngSLRH3T7dVdEqT22EU-gFiwoxd04fBlfv5X1MJcS6OCf-XIC5YlC9nxG7KkyYLWRA8i3Lufpy3AfvF4UjzmaaRv0j6DjNvj7hcj4UCSp_ovD6C3durMCKMt7xCt8TPNL1HbaIEavoscqANs6pHj8pPAZgLvWQkui1ZwpsKklJY41L9PkjgsfBN2FIfwmE6wkiyki-ENtKyTAI9RLK62SGfx17FXWXRfLTwRZ8015tOcu7yDdtun-o" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گل‌تساوی آرسنال به چلسی توسط هاورتز
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/Futball180TV/105730" target="_blank">📅 19:31 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105729">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">گل چهارم بارسلونا توسط پدری</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/Futball180TV/105729" target="_blank">📅 19:30 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105728">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">هاورتز زددددد</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/Futball180TV/105728" target="_blank">📅 19:26 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105727">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">آرسنال مساویووووو زدددددد</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/Futball180TV/105727" target="_blank">📅 19:26 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105726">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/581a696d28.mp4?token=mLWt08NV_92veKaVmnTd_AlcMnlkP5BZMtY_rzdCKNu4UW-dGVqeSbLIVDEMEuKKOxqFFILJ_XtjHCeljaghGo_7Ywi4UYYistuLaQe93QJUPGd2CpMz9p7WJVG8agMsEChTpnxHJBiWv5jJZ1EsesItVnNXz6oVBC9-qMRkAAmt1R0WbDHzmZRspwcPn3Fw0DiipBGmhx0A7yam0BPvxUAaiuBgRsevJo5yAJZs4g1XpI9FhLsjbHPTite87dJEh6pzGHHRr5_lOwXFWdMhOkk1OxCqy1oyoyKSqgz-U6jcp3U73ExkKv0iAma78RFKtaXXvKO-M0qN7ye3mjO2F4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/581a696d28.mp4?token=mLWt08NV_92veKaVmnTd_AlcMnlkP5BZMtY_rzdCKNu4UW-dGVqeSbLIVDEMEuKKOxqFFILJ_XtjHCeljaghGo_7Ywi4UYYistuLaQe93QJUPGd2CpMz9p7WJVG8agMsEChTpnxHJBiWv5jJZ1EsesItVnNXz6oVBC9-qMRkAAmt1R0WbDHzmZRspwcPn3Fw0DiipBGmhx0A7yam0BPvxUAaiuBgRsevJo5yAJZs4g1XpI9FhLsjbHPTite87dJEh6pzGHHRr5_lOwXFWdMhOkk1OxCqy1oyoyKSqgz-U6jcp3U73ExkKv0iAma78RFKtaXXvKO-M0qN7ye3mjO2F4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
گل‌اول چلسی به آرسنال توسط مورگان راجرز
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/Futball180TV/105726" target="_blank">📅 19:07 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105725">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/31943b0e62.mp4?token=vWF4OcVE--X_uHiyZQ2Kr22UMXQymqa-KGEE4a8F3_H_oVEA2ABgg4gAIEb6ucLUAsTj3sL-D-2sPjEFG8ddmoF-hWx2pn2YgDf67RPf235P5QtrG91Ql2sX9mEC_I6JRkIwPutOkVJXNpZwNUTVYT2QmaBfuLz_-tMRhz6NANP8IWZ361g8Z7L-A078xJs7Lclo6Hcq-87WZqWwWmJ_Hw9il49f_iKlqChYgXeJT0nK3MRY8CA2MDsLdizkCc8KloUtqcHzBj9BjIFgloKtYC_JC2kQAc1BohvqF13NYHnfS4QINJHFG3rqAsHfwbM8QursJFESDyOlmw3CjMnSPQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/31943b0e62.mp4?token=vWF4OcVE--X_uHiyZQ2Kr22UMXQymqa-KGEE4a8F3_H_oVEA2ABgg4gAIEb6ucLUAsTj3sL-D-2sPjEFG8ddmoF-hWx2pn2YgDf67RPf235P5QtrG91Ql2sX9mEC_I6JRkIwPutOkVJXNpZwNUTVYT2QmaBfuLz_-tMRhz6NANP8IWZ361g8Z7L-A078xJs7Lclo6Hcq-87WZqWwWmJ_Hw9il49f_iKlqChYgXeJT0nK3MRY8CA2MDsLdizkCc8KloUtqcHzBj9BjIFgloKtYC_JC2kQAc1BohvqF13NYHnfS4QINJHFG3rqAsHfwbM8QursJFESDyOlmw3CjMnSPQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
گل‌سوم بارسلونا به والنسیا توسط رافینیا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/Futball180TV/105725" target="_blank">📅 19:06 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105724">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">بارسا هم سومیو زد رافینیا</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/Futball180TV/105724" target="_blank">📅 19:04 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105723">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">چلسییییی یکی به آرسنال زدددددد</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/Futball180TV/105723" target="_blank">📅 19:04 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105722">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GeGRXkP_lNESEfRiGC4n0Bpe4ggjQEnQN0fpXQssCI8Z7rgX3eqUGJUGRAeDPMxZ9BV1RRX1gowhMMWteCzJZnXsWY5P_qr0cLYLN-NjdBW4b5ymuUMNrhxhQh-60ggbgeRmh028FyZFUMczuuxd4GMay6Vyd8GQJnIwBvosqfOLh4rDsehXqnoXp2_-yr9CjP8acZrGocZBR7yn6dD5YfmTOaniDD9hoTBvHge7YDmQO1jfNPib3eKGJDbDTUnHAiGwIiEsd2ZwCPSDaG7SCYI6KZ9jNS9VdnvvyGpTAMakUhTivuYd-fk73srZ38lZ9AO-HifKs-U04gvFZjyh0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
رد ناخن حسین کنعانی‌زادگان روی گردن و گلوی عارف‌آقاسی؛ لامصب چه جوری چنگ انداخته
😐
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/Futball180TV/105722" target="_blank">📅 18:41 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105721">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MaR-6giyeSEixw78Q2WmenfqReFppO0HQqert961P3Pg_HmPa7oPuX_05qvCO5XKBA7_J523sLOi1OvpEHuB68F3I6N_f55VNC4NtB0OywC5oFfB3izJG_7scnldU1MW5KEkw8GE8EMY0O-Rv7HBqDYDpFfHux78AOu8m5brDWhofk6HPvOmz-xJ0qeY3KgmRVPUN8MO4CuywsS1O7SFQCJzJCHkeYuC-kqgdvsfH0s6CMkgLyMCqXQxwkJIiBaoZfSZoCl52MlWi8hUsUFTYc5nM-GrwIyKVFDNvZ95b4hs4I5LlT_Y1J2pLzzdRm-IcJzo4vgin5XG_rybQw_gBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
اریک‌گارسیا در بازی امروز بارسا بدلیل سر به سر شدن با رودری دچار شکستگی بینی شده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/Futball180TV/105721" target="_blank">📅 18:36 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105720">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LV-uAxUd2uXsrr5Tznu9QjD0UeD6bMkRTTpsEmL-TZxoeeTTCEg2rdnePNGOL2qHWuPQ6zwR8avbHDFJUhCdsuN_8_w2sHg_jKepk_9RHx1XAf7NiuPOVRhdSC8yOp_K571kedhYir8LxJsHbfxzE-sTens3SWWxijdgXQofxL9-YrOufRUMHXI2w76DdoNoKJKbH4tNlUD8UYfVLtkKoFIzTq8Jcd8Ox72SUIP5FQC1DYZ1FKlWVn5ZAcXwWVetwMnJ9LTzfVvvwS7Ua8UCyd-lmsjhbcDXY3BeOeNllj0-YPNqWzVVhHoXYfgBow2GB855W499-ZCSomoDSZNe1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
گل‌اول بارسلونا به والنسیا توسط لامین‌یامال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/Futball180TV/105720" target="_blank">📅 18:33 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105719">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/90fe998947.mp4?token=sbAJ-Dskx7XDXbF-lqBjb6pTPg1zLA119osyGJCD4vHJYky2hFfSuswwZgUaJKmgq4MZ141R6ySjdJCcFS9XBvLpYz7bDc_z0tKJgF2EGPHeUMWLJOOUYqzdpvtInEQ99UuYGDTHxP7sWDSUA6HKuQzt-Mbkwe_M5hCuJ4YFEDId82CZ6_CjBANIoow6mUi41eiuDz58LNV_yvDx1rz6xYmoFnUuuVdTNhCecGPAWIt2LeS4d-1cpIvxnl80TTvtc9eHDdMtoAiV5F99nCf4I2AuF03bhSqvKupC0tA74oeiMmRwRGuj23OtVRiCKQglqgwhQCDPZI_z8lO6rEgnYw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/90fe998947.mp4?token=sbAJ-Dskx7XDXbF-lqBjb6pTPg1zLA119osyGJCD4vHJYky2hFfSuswwZgUaJKmgq4MZ141R6ySjdJCcFS9XBvLpYz7bDc_z0tKJgF2EGPHeUMWLJOOUYqzdpvtInEQ99UuYGDTHxP7sWDSUA6HKuQzt-Mbkwe_M5hCuJ4YFEDId82CZ6_CjBANIoow6mUi41eiuDz58LNV_yvDx1rz6xYmoFnUuuVdTNhCecGPAWIt2LeS4d-1cpIvxnl80TTvtc9eHDdMtoAiV5F99nCf4I2AuF03bhSqvKupC0tA74oeiMmRwRGuj23OtVRiCKQglqgwhQCDPZI_z8lO6rEgnYw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🔥
سوپرگل دیدنی در ثانیه های پایانی؛ گل دوم اورتون به منچستر یونایتد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/Futball180TV/105719" target="_blank">📅 18:29 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105718">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2e19464327.mp4?token=LCYc_igokmkW57aLHwwPFdrmbMFz7bb6M798s5qPaNmZ2ZiHARuj8UzJdRghJFuHnBuf480tjfqlpUaaH2X11v5-YunM3o_j7aJ4aE2qJXXMpFw0e5j4lfjrrsPoSiOM19570DQADxTgIcD8rnr1Y5m2cOVsJ-Z5ZqY9l-Cdr0aIZI5p6zIqL7AimmGh6P2BdYoVuuiQAVcWDjlwCrxuTCGu-luEih8G2d4PAcEHL6amCPJDCLhvP32-bMRMJVf1_b-6YRNkZqKinitYEdn0avgRojxU9PEjMHjszEm5TtMxNTKq5NF_WPIgYXg6J49YKII-d54OkRf54r702vE2Qw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2e19464327.mp4?token=LCYc_igokmkW57aLHwwPFdrmbMFz7bb6M798s5qPaNmZ2ZiHARuj8UzJdRghJFuHnBuf480tjfqlpUaaH2X11v5-YunM3o_j7aJ4aE2qJXXMpFw0e5j4lfjrrsPoSiOM19570DQADxTgIcD8rnr1Y5m2cOVsJ-Z5ZqY9l-Cdr0aIZI5p6zIqL7AimmGh6P2BdYoVuuiQAVcWDjlwCrxuTCGu-luEih8G2d4PAcEHL6amCPJDCLhvP32-bMRMJVf1_b-6YRNkZqKinitYEdn0avgRojxU9PEjMHjszEm5TtMxNTKq5NF_WPIgYXg6J49YKII-d54OkRf54r702vE2Qw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گل دوم منچستر یونایتد به اورتون توسط بنجامین ششکو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/Futball180TV/105718" target="_blank">📅 18:28 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105717">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">گل دوم هم یونایتد زدددد</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/Futball180TV/105717" target="_blank">📅 18:19 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105716">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c4032557f9.mp4?token=PMzAKg0yFlGF2KAl_bCDepZIL2mIUeyaw7suXAAfL3zWrryOeZpURzxCo31VlNGAu-le8oNaidqMa438QwsGKgEtD0-cCSmSv2KPkJGg0nGWGWo2dtBAl1uYNe0Jt2JUyuSGmWW-wjTda7KgRAB9CGGXriSIEaAsUrptKotWBGK2GOY1naJQ0EK8qQZOGr92ac5BCTW3Uopf_JgAm1F_Cb3wmVPiVK6F4rb61Q0LOj9SNCcKxxXOelXyq_KkJ87OYh4orOcr0hZP1nkI8PCPUV8-fV4NgNif75ck6XWnVEIPXtevG4VvF4pdOaBSSRqEFp2PJ0-CBvFu2rgweu1HTg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c4032557f9.mp4?token=PMzAKg0yFlGF2KAl_bCDepZIL2mIUeyaw7suXAAfL3zWrryOeZpURzxCo31VlNGAu-le8oNaidqMa438QwsGKgEtD0-cCSmSv2KPkJGg0nGWGWo2dtBAl1uYNe0Jt2JUyuSGmWW-wjTda7KgRAB9CGGXriSIEaAsUrptKotWBGK2GOY1naJQ0EK8qQZOGr92ac5BCTW3Uopf_JgAm1F_Cb3wmVPiVK6F4rb61Q0LOj9SNCcKxxXOelXyq_KkJ87OYh4orOcr0hZP1nkI8PCPUV8-fV4NgNif75ck6XWnVEIPXtevG4VvF4pdOaBSSRqEFp2PJ0-CBvFu2rgweu1HTg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شلیک به زاویه موافق لامنس؛
گل اول اورتون به منچستر یونایتد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/Futball180TV/105716" target="_blank">📅 18:17 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105715">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">گلگلگلگلگلگلگلگلگلگ</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/Futball180TV/105715" target="_blank">📅 18:12 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105714">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">گلگلگلگلگلگلگلگلگلگ</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/Futball180TV/105714" target="_blank">📅 18:12 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105713">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">پاس گل از آنتونی گوردون
🔥
🔥
🔥
🔥</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/Futball180TV/105713" target="_blank">📅 18:11 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105712">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">بارسااااااا ۲۲۲۲۲۲۲۲۲۲۲</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/Futball180TV/105712" target="_blank">📅 18:10 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105711">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">چه گلییییییی زددددددددددد</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/Futball180TV/105711" target="_blank">📅 18:10 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105710">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">فرمینننننننن لوپززززززززز</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/Futball180TV/105710" target="_blank">📅 18:10 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105709">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">گلگلگلگلگگلگلگلگل</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/Futball180TV/105709" target="_blank">📅 18:10 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105708">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JAV-kjiui53B6cJt3ys8nBCNfoC4rR3M5z-fy93RF7yLXakH842D3vrOv7uBrulAxafqLbAWgUcczYHLkvOqqOaOZziRH9in6hvtAG3JRd4IeNSBbdaBIqruJDNYzpc6LRy01MEc1TzU7Sl2xw_MODAAHggwGEJqRqt7cikb63LGgfB0rJD3NNyEwX_WV3r4U6atPFiXTPQitMkoqBMhfw3zOdD_OsKotyBwCWMRRTsOufj9IrNnw6SHJFOh2jiXS3hTTDsExbOWaR4MIF-RhRasZ_BYyEI7qeEIx6ZcNfNejeTBKiNIrz7QXqZbkUSPkxYNfw7oUoR47IuCWf2p_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
❌
گلگلگلگگللگ یامال آفساید شددددد</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/Futball180TV/105708" target="_blank">📅 18:04 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105707">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ULCCy5odVLu6A5Ja9vkDj2Gcp-69lcvsWXnsAAmP_bBY06p56VDHKOVN7aZMSHqs-kQFyaTkMdIbkJNqSBxjfK0SoyPBqrowd57leHgzjSf9jnxcDw1Unp79fRjvk32Ub_tJZ-Ity3yyRNNB4Ok1M2X4zaQrk05dtMBGwzeFVSsH_3AVf2IVHocu5NgLFFk_6aqKO1DP0Li_vWDk4tZfONQz9GOxS3LqvbMTFE8-nRKzkJON82ZpEMqHYuW_gcrHmFLiX7InSfN-ydJxPs5HPmB9Jr6ZJxADnpGlf3DB2EST7d9pfHfrYzv_e80HbeJi5WKq9itawFrMEqZXPefdQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
ترکیب سپاهان مقابل استقلال خوزستان
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/Futball180TV/105707" target="_blank">📅 18:03 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105706">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/10c1daa423.mp4?token=II69XAs-GdgUjnRmWgr-cMQ11-3otzdwkPqWAhgPOfSo22IzrsSNjMKOSK5q2IoP3FVkjSWP_xqyrj3OwDrRi-UhxicKepsoydE9wwF8svEaRJ1QdMqWyNGeRr594gplj-xvpVTWWWRexkgTuVk2jT4DT5jAaGvRK9c-B_wy_b_Bjg65mp1ghoLLSJfLO6D_7iyYrb6v0pG1GeGI_uJrFXGE69D5NTfJgLClKQVeyIDg_QKI-eywJRR5Co-QJbm3scH3--nkd8AEc_zDXb5G5xQOOtJJcectHwv4iNDqbNolpp0xAkggnlRv1A91R61dVtH7VHloigMmOo-QfC62aLuBga6Snf20RsLPSQYxzTj9zK2Z9fD3oD_RVup-F_P9JRBWKIXXa_k5UumfOxgJOBnG_uIOuUm87z6d_HHCm2nx_Z4wGn1LZy2l4219NXrvploAiONMwJRBoZIiD_SYATLo05Mo0_bmsA6zUaRVshrrJkgKYFTHhddFJNwlIspJbbjLx8jngXFNUiR_1bvF3osaqZtoH6Z0FINBC9HQky-P40nbTSdOIueW2BukxqrMh_xgtaGc7Pet4cIxLPETTle2QFcITwZoblZrQnaETT9d8S9lDSkMjgqU0laHMGiPau5Gs4Qd0vmeAJwloaf28jjkpWd3n6lXpW5bIJvMivk" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/10c1daa423.mp4?token=II69XAs-GdgUjnRmWgr-cMQ11-3otzdwkPqWAhgPOfSo22IzrsSNjMKOSK5q2IoP3FVkjSWP_xqyrj3OwDrRi-UhxicKepsoydE9wwF8svEaRJ1QdMqWyNGeRr594gplj-xvpVTWWWRexkgTuVk2jT4DT5jAaGvRK9c-B_wy_b_Bjg65mp1ghoLLSJfLO6D_7iyYrb6v0pG1GeGI_uJrFXGE69D5NTfJgLClKQVeyIDg_QKI-eywJRR5Co-QJbm3scH3--nkd8AEc_zDXb5G5xQOOtJJcectHwv4iNDqbNolpp0xAkggnlRv1A91R61dVtH7VHloigMmOo-QfC62aLuBga6Snf20RsLPSQYxzTj9zK2Z9fD3oD_RVup-F_P9JRBWKIXXa_k5UumfOxgJOBnG_uIOuUm87z6d_HHCm2nx_Z4wGn1LZy2l4219NXrvploAiONMwJRBoZIiD_SYATLo05Mo0_bmsA6zUaRVshrrJkgKYFTHhddFJNwlIspJbbjLx8jngXFNUiR_1bvF3osaqZtoH6Z0FINBC9HQky-P40nbTSdOIueW2BukxqrMh_xgtaGc7Pet4cIxLPETTle2QFcITwZoblZrQnaETT9d8S9lDSkMjgqU0laHMGiPau5Gs4Qd0vmeAJwloaf28jjkpWd3n6lXpW5bIJvMivk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
گل‌اول بارسلونا به والنسیا توسط لامین‌یامال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/Futball180TV/105706" target="_blank">📅 18:00 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105705">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sA3knATZqS0xwgdbQhfniHWw7CPPcQTQ7N-NYIFYOl9TKwW7XdMK9WWEfIvfCLgMSVPg7IKPJtiMBl2uAdQFs3-faOxbU87_x5BpFuIUJE-WPPv0gVAFlN7TX-cn_QMS5VxUJGQi12zRos8PYqY1aE62_HIQdQKrwAR6javWo1tffGTiHOcpafgRb4MKhs3p9dy-7F62TXWQdjPUjzMF9EsNAza8kNBjHeL0_WDIJyt1axvjMQKVPaJC5jwfJk8ovvKXGknMhdbaG3BoOIlewncBJP4f_c-b-6lVhIXinbYemnexltgp_Wj1Jwo51F87t-9TschXyLy4TPis-KRc7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اووووووف بارسا چه سوپریههههه
😐
😐
😐
🔥</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/Futball180TV/105705" target="_blank">📅 17:59 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105703">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/J-Mpm_Np9VLxKyPhaRAg9DQzCOhrfwot8ZPrcG-mEEGJ6YQQD2cpzLE1I5tFM9612lxoj0jZgzb5XdAtx0IFORX5ZhqKtMgDZTrd-4lbIcikrSM7S6gNF-kQVj4W4ns3JGeuzo1Ne4nsvqC6TDB0fyvMeJsDImmcloYUC2bV6EF9UE2MnA-rk2fUpfszEv-4x4TplXTOQVG7NvN_67nQqJa-gT8IJJEmYzP27jALwnCWL12IeIIhebnVMu-DBWf8SSAthVUoBHS3m5M7hmDVLmF54ZEeqc3mlAiQhZwAoB2Hjb-v6lIOglMt5ILiVU6MnoxEKWG1SSUK340ej0YRPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/B8-fAsSLOFWnLqPSIX1ni2o5Z7jMpmsAPcKr6YTJS13bWbJ7scqbz_qSc3vK7u-kENEiHybFGqxDG7RigS-P_JtY4-kil--M1n1Lh3l4NbxExARy2lpPOCb8Cmn2tDRcfaHDffWWZcW2xlI-fb3blom33N_DUmiXLM29YvUVICJh8x1UyMrZrT2QphPcBJN7m7xLY-SSJB6AJPu1XxeMHeAbwmuO-d3B8kJG64PzauNt9_x2YAYfa_D6IrNuvdP-yecezwPlHY9AlNjNHHyChKpHUM_eF7k5zZLZQ7jbhdMWLdoT7F5dWtvTkwYbJuGY9w5rtzXxK00DDqI9RFaRlQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🏴󠁧󠁢󠁥󠁮󠁧󠁿
ترکییب دو تیم آرسنال x چلسی
ساعت 19:00
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/Futball180TV/105703" target="_blank">📅 17:58 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105702">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">اووووووف بارسا چه سوپریههههه
😐
😐
😐
🔥</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/Futball180TV/105702" target="_blank">📅 17:56 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105701">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">دبلللللللل لامین یاماااااااال
😂
😂
🔥
🔥
🔥
🔥</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/Futball180TV/105701" target="_blank">📅 17:56 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105700">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">گلگلگلگلگگلگلگلگگل</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/Futball180TV/105700" target="_blank">📅 17:56 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105699">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">چه گلی زد ناموسا
😐
😐
😐
😐
🔥</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/Futball180TV/105699" target="_blank">📅 17:54 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105698">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">بارساااااااااا دقیقه ۶ اولیوووووو زدددددددد</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/Futball180TV/105698" target="_blank">📅 17:54 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105697">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">لامین یاماااااااااللللللللل</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/Futball180TV/105697" target="_blank">📅 17:53 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105696">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">گلگلگلگلگلگلگگلگلگلگ</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/Futball180TV/105696" target="_blank">📅 17:53 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105695">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2d3e81743b.mp4?token=sSWWI9_syeHgVtxIeSYQKVSOzMtWN0dTRoRgs7152qOXgqdLNCSzAGfNitEX6VcCIVJGmSc7gWSY_xMl0DbHxmy3AMu-5qyov1cbLI3iOMLEWNnjfQcbD1Vx_tO8Trd9seCgQWc6V36Xc1p2X3nNb-_EsCdkWn8NoZHyXhWaXss6pnAMBi7NVJVl7Zbjq64fCoUOjfeTkaiOW89Ich5m49egI082yegikdwRxoZGC7O_bDNkVJ65Ybg86R-OZwWtxH4hf6rmLIa7fL0eMdvTJWCgE6HIsjOHTWrYnFD0f1sOTo8rF10yt3crBzLcVeJ3GNN8GNWbiEjocdDGsZ-aVQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2d3e81743b.mp4?token=sSWWI9_syeHgVtxIeSYQKVSOzMtWN0dTRoRgs7152qOXgqdLNCSzAGfNitEX6VcCIVJGmSc7gWSY_xMl0DbHxmy3AMu-5qyov1cbLI3iOMLEWNnjfQcbD1Vx_tO8Trd9seCgQWc6V36Xc1p2X3nNb-_EsCdkWn8NoZHyXhWaXss6pnAMBi7NVJVl7Zbjq64fCoUOjfeTkaiOW89Ich5m49egI082yegikdwRxoZGC7O_bDNkVJ65Ybg86R-OZwWtxH4hf6rmLIa7fL0eMdvTJWCgE6HIsjOHTWrYnFD0f1sOTo8rF10yt3crBzLcVeJ3GNN8GNWbiEjocdDGsZ-aVQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
گل اول منچستر یونایتد به اورتون توسط برایان امبومو با گزارش ابوالفضل عامری
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/Futball180TV/105695" target="_blank">📅 17:39 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105694">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C4iSBS9LmDG6VtnYuwb7ws6_SV0FDCsEpedXngmuQF-2acgvjvqzoxnVaeGcsAiDAy6fwtwk1fGsB9xOsDxK7MzV3-tzT15ZjAE40970GTa-C2lfXxnS8SMb_jt68kUDzfwJ0jvVvg2KctWJhWYoES6v8Ytgo0CDhjRhAH95eucY7qjTNlJDfdb55mio65DUyAsYgzi1Ufaz0Rq8mzUUVQmTUHVfFcXnSoJzkLx6eEzwRwo-3M8auef6pQYHbsagpUTZE4llJ2DOaZ0vZmehJnttLnvw1vMEiKyeGGwu8r79vSjuhyfQK7ZAJCzuE5uypdoKd-Q-wBHwpXmtnwMefA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
ترکیب استقلال مقابل آلومینیوم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/Futball180TV/105694" target="_blank">📅 17:37 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105693">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">صداوسیما راحت با ۳ دقیقه تاخیر داره بازیو پخش میکنه
😐
😐
😐
😐
😐</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/Futball180TV/105693" target="_blank">📅 17:37 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105692">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">امبومبووووووووو</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/Futball180TV/105692" target="_blank">📅 17:36 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105691">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">منچستریونایتد یکی به اورتون زدددددد</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/Futball180TV/105691" target="_blank">📅 17:36 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105690">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">گلگلگلگگلگلگلگلگلگ</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/Futball180TV/105690" target="_blank">📅 17:36 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105689">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JjKniWJ_85PfcAuPTgCsBbW22y4st-3j1AL48q4cH2W02_7exGWJVzQrd2_5VXEf2cSDZziNU7DfVB472X1J4zC1qqRKnen8cZMv5gIBohQ-VwgAowmNt1IGSpLaiv_EL_HcsgPKGb1ThLe_joqeS8U_9GR9UCAs_s-S3yAdaO6respmbxemI-y0PJAVjqEbOKqwFN_KNpC1jsmT9rl4ig2AOL8CH_GiTkJsJu9O6tgzOQSSZ4N8I8da3g379ucoL0hCzqk9DeuZFDx9pRvxP62V8C_jLEpWIETjPoZR5ONyR1loMVH8QTDDnCyd4uwWtuqCBhvHj62-3lxTAGZZ8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🟢
ترکیب آلومینیوم برابر استقلال
محمد خلیفه، امیرمحمد هوشمند، امیر نوری، ابوالفضل قنبری، شروین بزرگ، سیدمهدی مهدوی، سیدمهران موسوی، سعید صادقی، ساسان جعفری‌کیا، عباس کهریزی و امیرحسین امانی‌پور
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/Futball180TV/105689" target="_blank">📅 17:31 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105688">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/31aab68480.mp4?token=qseQJT9BwY43ZFuOeo4krI61Tc6ybKNa_SsKAShh_-MojDwnPNo6_njHEBmVKc_QBUZ2X0gRvdFE6nyF3Wl2uhjPX0ZQ5KUKvoVTJkcWHMnU96TqnmZPhMCkDz2WUR6IMoO5M0n-eVxDgiaYeaIkDMteM4x0uHofdBDyTB5R6uxc91yGnRZv86QDV2sWpFN7a3yk6hZLFPcI82C9fispkeZwfgvyxGi6Y9gXR_WtWvOj7waUivy_F4eXDTaOH57R-0wR31StW-MkGXzOYG-OE-oAYY8yfmUKumvVZaqMmFTZhe3LF_uW0aoWYPgnyi0SXNg20inxokKsLORqT4uq9A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/31aab68480.mp4?token=qseQJT9BwY43ZFuOeo4krI61Tc6ybKNa_SsKAShh_-MojDwnPNo6_njHEBmVKc_QBUZ2X0gRvdFE6nyF3Wl2uhjPX0ZQ5KUKvoVTJkcWHMnU96TqnmZPhMCkDz2WUR6IMoO5M0n-eVxDgiaYeaIkDMteM4x0uHofdBDyTB5R6uxc91yGnRZv86QDV2sWpFN7a3yk6hZLFPcI82C9fispkeZwfgvyxGi6Y9gXR_WtWvOj7waUivy_F4eXDTaOH57R-0wR31StW-MkGXzOYG-OE-oAYY8yfmUKumvVZaqMmFTZhe3LF_uW0aoWYPgnyi0SXNg20inxokKsLORqT4uq9A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
⚽️
صحبت‌های هوادار استقلال
:
🔵
سهراب بختیاری‌زاده مثل مدیر مدرسه رفتار می‌کند! کاش صالح حردانی در مسابقه امروز بازی می‌کرد. نظم خوب است اما امروز باید صالح بازی می‌کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/Futball180TV/105688" target="_blank">📅 17:28 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105687">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Hwrdi9BEHhi18dWq9U8beFC9a57CzIOqItnxl8d8cHMelB17Y7yXUw3O97so2THHFd8vU212_lzTSYyj42kZ1ip-i7cbU_fbPBnnn8DFmUPYJJeJ4whBCN9QNdS49K6QUpwwUzum_-KGH21WZIvLFzp9Who5D7SQzF6LFgkfDRTJ1uAto5Ys2jlD_MDwN6_UiQVP8m3RwG6OOGBrqcXYpCtYN0Z0Y8lNqavIeu0uct2zrfyVIgE8A-zqxe0XHAMDKzNgeDxn8MQKXpFE-nFt5PBfz9OIkEZXJLdmeQq8EuS-LGvtDxAdesmaGDfCsJlyrqtzzBzExLVOUh487bpmEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
شماتیک ترکیب بارسلونا مقابل والنسیا؛ ساعت ۱۷:۴۵ شبکه‌ورزش
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/Futball180TV/105687" target="_blank">📅 16:49 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105686">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/Futball180TV/105686" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/Futball180TV/105686" target="_blank">📅 16:49 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105685">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YV9pgqmo3MQBX7pftymnIVFL7ymJsIvxu72DbWiUrewPVVWxqTi7TkfFJ63fEWTvgATDhLNxuFt6jy51nIOxxR9yJnGBe7fDxFoXga9JoP_w_mJKUZX5VE8Q_RJwLFd5hg0_pElapuyqWMCfM4XDRNC3dBpageMTVyXOt90AWz_vfZ0z6ZwEt2QpqCsRHQYPgQPu0Nq6ALdM8HuUnxonprSi67spfwYHjhUOiexpXjYr_EkEooVCiDh_a4pzIhVo7ewtYYjOIyE6sLyPsHQXdqYyYDj1DXb71P-WCI8CQken7jCm2_QVb32yH0KDW3F5DfwkMvkRnJfBUb-xYyGlnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
بازی جذاب
⚽️
چلسی
🆚
آرسنال
⚽️
را در سایت بین‌المللی
TrexBet
پیش‌بینی کنید.
📊
نگاهی به آمار ۲ تیم:
چلسی: ۲ بازی ۲ برد و ۷ گل زده
آرسنال: ۲ بازی ۲ برد و ۴ گل زده
🦖
بونوس اولین واریز تا سقف ۱۰۰ یورو
🦖
بهترین ضرایب بین تمام سایت‌ها
🦖
واریز آسان و امن از طریق کارت به کارت
🦖
🦖
🦖
🦖
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/Futball180TV/105685" target="_blank">📅 16:49 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105684">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9f2bdbbb8d.mp4?token=LN3YPK4HjCVKDta4lcJyLodevrXbB9_JQnSTLZK9UXawILkYFJSRwlQnYRL3SVGMBzHNaF3mH_7Dcm1sTu5khXako930QGeZahT0vmGmtkX82h1x37lbgGlCKVq3Y_UW1y_uOHfkfC77JZ25kdRglB7ei2HOnLOoaeA2HT3hNAKxxTk_DgsEj3UrY7bK2tfFesGK-H-dFkyYC8EaLh_Pvv8SLfswyx6EyXcBJJqLLWek4-wmHc-Of7_UDFI8lByF7ylVPg714KRC3r1TCggVsQmuZkHlGS9tk1h16YkItrdb3TlPgunLlYyCJi7r5cmpkFdWJ0_6k5BDGAx6n3kcgw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9f2bdbbb8d.mp4?token=LN3YPK4HjCVKDta4lcJyLodevrXbB9_JQnSTLZK9UXawILkYFJSRwlQnYRL3SVGMBzHNaF3mH_7Dcm1sTu5khXako930QGeZahT0vmGmtkX82h1x37lbgGlCKVq3Y_UW1y_uOHfkfC77JZ25kdRglB7ei2HOnLOoaeA2HT3hNAKxxTk_DgsEj3UrY7bK2tfFesGK-H-dFkyYC8EaLh_Pvv8SLfswyx6EyXcBJJqLLWek4-wmHc-Of7_UDFI8lByF7ylVPg714KRC3r1TCggVsQmuZkHlGS9tk1h16YkItrdb3TlPgunLlYyCJi7r5cmpkFdWJ0_6k5BDGAx6n3kcgw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🇮🇷
وضعیت دیشب امید عالیشاه هنگام ترک استادیوم یادگار امام تبریز!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/Futball180TV/105684" target="_blank">📅 16:30 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105683">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fd27d50a5b.mp4?token=SuUUJcjTntHCUhxzBd5H653oQ9HxNCzEu5VAAw_gmJ0ubAaeEH5IWiyHFdWbcMqJH2hhnVoOFqfxrAZH8MIdtz5h2_biWGqDZVsRm2Tf-k0nBrQ5mNcYPrZMV4DVZobr7crswXskT2BM13UFs1dqobX-mTpYcHuUCCSrzFldCYH4JKI4EWjbzRn0VEhoHcQet9gIMCtCpjX9t3QNFP63ULfZxi6TCBO1y_c9XIHtSCb2bz59L7jG7U669Gh4FBRF1-H7KDjBc-zwkjhDr292g61MRE9HU5We9xbFAAAXs0YpwTwcH96vrEjESomatcH3D2Au7HTnckXN8hiXO2aHGQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fd27d50a5b.mp4?token=SuUUJcjTntHCUhxzBd5H653oQ9HxNCzEu5VAAw_gmJ0ubAaeEH5IWiyHFdWbcMqJH2hhnVoOFqfxrAZH8MIdtz5h2_biWGqDZVsRm2Tf-k0nBrQ5mNcYPrZMV4DVZobr7crswXskT2BM13UFs1dqobX-mTpYcHuUCCSrzFldCYH4JKI4EWjbzRn0VEhoHcQet9gIMCtCpjX9t3QNFP63ULfZxi6TCBO1y_c9XIHtSCb2bz59L7jG7U669Gh4FBRF1-H7KDjBc-zwkjhDr292g61MRE9HU5We9xbFAAAXs0YpwTwcH96vrEjESomatcH3D2Au7HTnckXN8hiXO2aHGQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
💥
🇮🇹
شادی فوق‌العاده شب‌گذشته لائوتارو‌با هواداران تیم فوتبال‌اینتر از این زاویه خاص
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/Futball180TV/105683" target="_blank">📅 16:05 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105682">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🚨
🇮🇷
مهدی‌تارتار سرمربی پرسپولیس: اینکه پنجره نقل‌وانتقالات تیم استقلال بسته شده به من ربطی نداره و مشکل از مدیریت خودشونه. اگه استقلال بازیکنانش رو به تیم‌ملی امید داد ماهم میدیم. اگر اونا ندادن ما هم نمیدیم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/Futball180TV/105682" target="_blank">📅 15:55 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105681">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0df0581598.mp4?token=t_mONKRyFT157Vl1MUGve7GV3n_OFX8Q7UrokthzVlbQmmhZ5uOGqitC0C_l_7nrbn0S3gEbsrI_GZD2fY2JTxQsrrVO1CsYjuSm-vWIDo23kA2KOqLQj7uB4ghQ76MHF5ihf4Bz7hXDuS8Rs4aVM1zzdl3Ln2lWGQwXBZNeS6SQ6WSNmNNOPOj-zpkSKQdjXc2u-8vbEsALBHht40PGXdMr1PISDNRQJ-2PPom7f6QLpmaGjmwJ4B5Se6tZNUS7qahSpHELrn1pehC_9BULQpDbaaLb-m9VHx67BleziJYNihLZmw7QrRtipVeIBR2-N1jg2grZ3HM3pkELmbOCnw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0df0581598.mp4?token=t_mONKRyFT157Vl1MUGve7GV3n_OFX8Q7UrokthzVlbQmmhZ5uOGqitC0C_l_7nrbn0S3gEbsrI_GZD2fY2JTxQsrrVO1CsYjuSm-vWIDo23kA2KOqLQj7uB4ghQ76MHF5ihf4Bz7hXDuS8Rs4aVM1zzdl3Ln2lWGQwXBZNeS6SQ6WSNmNNOPOj-zpkSKQdjXc2u-8vbEsALBHht40PGXdMr1PISDNRQJ-2PPom7f6QLpmaGjmwJ4B5Se6tZNUS7qahSpHELrn1pehC_9BULQpDbaaLb-m9VHx67BleziJYNihLZmw7QrRtipVeIBR2-N1jg2grZ3HM3pkELmbOCnw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
مهدی تارتار، سرمربی پرسپولیس:
از فیروز کریمی(پدر زنم)من خیلی چیزها یاد گرفتم‌. الان چون ایشان استقلالی است زیاد نمی توانم مشورت بگیرم اما از او چیزهای زیادی یاد گرفته ام
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/Futball180TV/105681" target="_blank">📅 15:52 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105680">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🔞
⭕️
⭕️
⭕️
⭕️
‼️
‼️
‼️
‼️
🇮🇷
🇮🇷
صدای منتسب به فحاشی زشت و زننده و ناموسی خداداد عزیزی بعد از بازی امشب تراکتور و گل‌گهر به امید عالیشاه در کنار رختکن گل‌گهر سیرجان! در صورت تأیید این صدا احتمالا محرومیت چندین ماهه نصیب خداداد میشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/Futball180TV/105680" target="_blank">📅 15:47 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105679">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">❌
واکنش تارتار به گل پیروزی‌بخش تراکتور مقابل گل‌گهر: نتیجه باید در زمین مشخص شود/ مطمئنم که مسئولین بررسی‌های لازم را انجام خواهند داد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/Futball180TV/105679" target="_blank">📅 15:41 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105678">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8127b1da2d.mp4?token=dkXln7eqwtVDUNycK3qs_sSFF4k7Rn1aF4uzbkv1Et-u7L6po6u3Y_rZmdo63kUoBdwwrJsGXi0NdygDhuDfkrTrwiXDNkNphCw09B5N2HsOJBpQUe6oE0XHLq9PRn-axaNrz_lR-Gy-FpJmk2Q7bxsOOi4TcZ4tuzDlwQUY8uMFHedqoWWtxpVo4wFmCbxZMmbDg737fR39d8JwgQ5PwvYqTT682IXgkZgZrNmg-Y_Hum-tG7e-h6yThozY9KcryJyKj15a5fCwkRna9dzRFdDcq3R-ncQbKbZg2r7AXMkxlXsN_fk7cA6JqHhbcCpGasPtHh60uXTnHCuRz-qRVwDAoBiEkKIK3FiS4Le2joc8reXAW5gN9dTgmHtJBqCDrHbkBv39I0M9z38nxCutKzcO8joTSdewpEtEhu2DOgNgcenLO-oRwI4GvlUNThmaoOSRZ75nE3JDVNPGn-be9VLG-TZsOrO3AoyHeaQGIe3j1jaHKPjK4MEthvgYl_W3sZEbnIszhw9gjji9lcjlqfGtgESvJR8-gxBjx-vgzYU7rK_kaEtQur9GJbr8IUV1Ut1H-5PD-uUghNGHUEy_o_5RYhZjqozlUdhILF4vzD27ZhcUp7ih7AfjqH1gVzx9L2kjgFHLTUQa0JwLbqV2CKK1xK0WWAZ5J7t_KRLI-oM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8127b1da2d.mp4?token=dkXln7eqwtVDUNycK3qs_sSFF4k7Rn1aF4uzbkv1Et-u7L6po6u3Y_rZmdo63kUoBdwwrJsGXi0NdygDhuDfkrTrwiXDNkNphCw09B5N2HsOJBpQUe6oE0XHLq9PRn-axaNrz_lR-Gy-FpJmk2Q7bxsOOi4TcZ4tuzDlwQUY8uMFHedqoWWtxpVo4wFmCbxZMmbDg737fR39d8JwgQ5PwvYqTT682IXgkZgZrNmg-Y_Hum-tG7e-h6yThozY9KcryJyKj15a5fCwkRna9dzRFdDcq3R-ncQbKbZg2r7AXMkxlXsN_fk7cA6JqHhbcCpGasPtHh60uXTnHCuRz-qRVwDAoBiEkKIK3FiS4Le2joc8reXAW5gN9dTgmHtJBqCDrHbkBv39I0M9z38nxCutKzcO8joTSdewpEtEhu2DOgNgcenLO-oRwI4GvlUNThmaoOSRZ75nE3JDVNPGn-be9VLG-TZsOrO3AoyHeaQGIe3j1jaHKPjK4MEthvgYl_W3sZEbnIszhw9gjji9lcjlqfGtgESvJR8-gxBjx-vgzYU7rK_kaEtQur9GJbr8IUV1Ut1H-5PD-uUghNGHUEy_o_5RYhZjqozlUdhILF4vzD27ZhcUp7ih7AfjqH1gVzx9L2kjgFHLTUQa0JwLbqV2CKK1xK0WWAZ5J7t_KRLI-oM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
واکنش عبدالله ویسی به اظهارات رکیک خداداد عزیزی: واقعا خجالت می‌کشم در این مورد صحبت کنم/ تویی که فحش می‌دهی! شما خودت ناموس داری
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/Futball180TV/105678" target="_blank">📅 15:37 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105677">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1304ef0ba1.mp4?token=Vt7fF_4QRSN2p_VhfzBVDupHbsRc6F-5DCV248jh28OsubejhVIqzcgHMl-_FEmRM-3vpPuU83RlY7Xsf08Eq_sEpdWEbSNxla2EyKxFNchwmvOI9ltQHgKL5p7VQeM2BS8m5KK8hq6sOt4xlWWIAtyBO8Vln_zdeJLcEYYH6QPIFiZ_5ynd2Mb1k5f3xL7OtR9cYd7D8TlVcwxnktAPASFxNy3KKgzTl-NZr5kOQ2bsm7P6nFr8xANfJilQhRdbYQZv54UBRCebBLPMEYwPMDoOvB58NoEmfMHQ6PmlvClran_pKUTp1syYBFN_jQXsDqd0L-UzW_k3JdDIoVWrLQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1304ef0ba1.mp4?token=Vt7fF_4QRSN2p_VhfzBVDupHbsRc6F-5DCV248jh28OsubejhVIqzcgHMl-_FEmRM-3vpPuU83RlY7Xsf08Eq_sEpdWEbSNxla2EyKxFNchwmvOI9ltQHgKL5p7VQeM2BS8m5KK8hq6sOt4xlWWIAtyBO8Vln_zdeJLcEYYH6QPIFiZ_5ynd2Mb1k5f3xL7OtR9cYd7D8TlVcwxnktAPASFxNy3KKgzTl-NZr5kOQ2bsm7P6nFr8xANfJilQhRdbYQZv54UBRCebBLPMEYwPMDoOvB58NoEmfMHQ6PmlvClran_pKUTp1syYBFN_jQXsDqd0L-UzW_k3JdDIoVWrLQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سلاطینِ پنالتی این فصل در رئال مادرید دور هم جمع شدن.
🤝
🙂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/Futball180TV/105677" target="_blank">📅 15:15 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105676">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/03ae12814c.mp4?token=lR-oFhAQa-p8e6ujMsLuBsiHqIdgUSLPw67kDc3EHwnZLPx1RqgJqp1iiuIj-vrWjD_o4z8CxJ24mYy4i5nagsG8y5ViN0Kh0fT5aMTPqpeIs92qO5DtBLvaThfVsyjot7BbuAKBSO1WQqLeioBlDYiUqTrpsoNUdH5bfZuVPn5OzoRRS5TDs2SP0DUHq8oH6r8PigUYyaCdY86tZwyOs0PgTZG6VDMJgz21qMxTwO8ShpshZeDsGhsgEyA38ne02pJCX8FZS0Dl22HHxkZpEXh_CFHy72vNpqekU2DbjDn3K-DK3bJGQR5N0ez-vi_uBc2Uv-oNCicYUxvkn747YA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/03ae12814c.mp4?token=lR-oFhAQa-p8e6ujMsLuBsiHqIdgUSLPw67kDc3EHwnZLPx1RqgJqp1iiuIj-vrWjD_o4z8CxJ24mYy4i5nagsG8y5ViN0Kh0fT5aMTPqpeIs92qO5DtBLvaThfVsyjot7BbuAKBSO1WQqLeioBlDYiUqTrpsoNUdH5bfZuVPn5OzoRRS5TDs2SP0DUHq8oH6r8PigUYyaCdY86tZwyOs0PgTZG6VDMJgz21qMxTwO8ShpshZeDsGhsgEyA38ne02pJCX8FZS0Dl22HHxkZpEXh_CFHy72vNpqekU2DbjDn3K-DK3bJGQR5N0ez-vi_uBc2Uv-oNCicYUxvkn747YA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎾
👀
واکنش خانم‌ها به تعویض لباس آلکاراز!
کارلوس آلکاراز پس از پیروزی مقابل وو یی‌بینگ در دور سوم US Open، مقابل جایگاه تماشاگران لباسش را عوض کرد؛ صحنه‌ای که با واکنش‌های جالب هواداران، به‌خصوص خانم‌های حاضر در ردیف‌های نزدیک، همراه شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/Futball180TV/105676" target="_blank">📅 14:50 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105675">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c2e7b0fcfb.mp4?token=Ws9PUleMKS2blJVbFENcQdbLv4HfNy3wh9kSUvUvZg2gB0Wl9ZT0xk_PYyLLPI0Og2mWIlXJl5zxbfvuFlOLZwDE6z8tqzk6gJlyMMO01kyy6ttfDB8LK0WRmau2YH55bHomLd_Vc3nhib5FmgIMnOK63y0UaWX3JxDVTSHwYkJtLRSoUOZJi9FC0UUNrfQpCa1FeKcscfR3tiSow3j81m6C2IidaJrosruYEOcwXt6i26Kq7mbNp9d38zJ_st0L3M6daCj9yJtrZJnkC5Cm90ZTjUksISLseSi8euFX5Eyh0VQ_UmtND0UYkqiXmUYLLlYl4dZOVKDW0nG1vmeZig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c2e7b0fcfb.mp4?token=Ws9PUleMKS2blJVbFENcQdbLv4HfNy3wh9kSUvUvZg2gB0Wl9ZT0xk_PYyLLPI0Og2mWIlXJl5zxbfvuFlOLZwDE6z8tqzk6gJlyMMO01kyy6ttfDB8LK0WRmau2YH55bHomLd_Vc3nhib5FmgIMnOK63y0UaWX3JxDVTSHwYkJtLRSoUOZJi9FC0UUNrfQpCa1FeKcscfR3tiSow3j81m6C2IidaJrosruYEOcwXt6i26Kq7mbNp9d38zJ_st0L3M6daCj9yJtrZJnkC5Cm90ZTjUksISLseSi8euFX5Eyh0VQ_UmtND0UYkqiXmUYLLlYl4dZOVKDW0nG1vmeZig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✔️
▶️
بهی جدیدی، بازیگر نقش مهرو سبابه‌چی، نامزد مسعود شصت‌چی در سریال «مرد سه‌هزار چهره» به کارگردانی مهران مدیری است. وی سابقه فعالیت‌در تئاتر را در کارنامه‌اش دارد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/Futball180TV/105675" target="_blank">📅 14:25 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105674">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/051a0fae8d.mp4?token=QqJ6MvqEht4pTwnxz-q2tM5VMgUBKCnfsoPUKhcLUIryjoM84LG0xCvt4YGBXbVDeaqwT1bZUcJ-OzOPg7fGdXynQa52fsvydiSfLyzeXIgmwsGmExPDa6xfFX_IbX2OnsQD-WJpJ_pZmoFtbUsJjy0vSnvB_5m2gpBNb2SWB7U83XAKqt8Sj1Pet4enSFX33EqrS1DTv16-U6ZIXWQhNXyaTfLPvd9jGsOpVsYN2mPcp4MR9P3j6kJbmNaC4F6szm8vgqTAx880LTEhziDaeyQeEGehIL9ekt8kc25Oeseh_rYZba3z8gIoHcUluqZzWtHuxR6WzdJQ-e7CNrDVYhqqRxjzJc8Sq06jnE58dHkA0eL1JCkIN2f4rFbdL83hBDQjdehfZgipSwZdc1osAX6iJpGSj_GXVxUw2ExRnU2wN-HNAm9wcN93b7fiTuUUNuW3t0Pzi7F2dNCA1PuSzUjnbXqdzuMRIGw5KK2qhmyggdRp5FBpgiJHi51T-bac2vXTPlTVw-NnwLPxa-HdkRxa6UVhMlXSjhmOTstLPS_wHuvlb9xjhfk2AqH7rJDGUaBoU5jRizX-72pEgP8uu7Dcz3cgLbC1Qd_qdvSa-HXdofhJmzIk8VplCAK2ReS96IfzXL_8B0_0h7RKBRnX5nvKvy0GfD6C3tifHhfjfxc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/051a0fae8d.mp4?token=QqJ6MvqEht4pTwnxz-q2tM5VMgUBKCnfsoPUKhcLUIryjoM84LG0xCvt4YGBXbVDeaqwT1bZUcJ-OzOPg7fGdXynQa52fsvydiSfLyzeXIgmwsGmExPDa6xfFX_IbX2OnsQD-WJpJ_pZmoFtbUsJjy0vSnvB_5m2gpBNb2SWB7U83XAKqt8Sj1Pet4enSFX33EqrS1DTv16-U6ZIXWQhNXyaTfLPvd9jGsOpVsYN2mPcp4MR9P3j6kJbmNaC4F6szm8vgqTAx880LTEhziDaeyQeEGehIL9ekt8kc25Oeseh_rYZba3z8gIoHcUluqZzWtHuxR6WzdJQ-e7CNrDVYhqqRxjzJc8Sq06jnE58dHkA0eL1JCkIN2f4rFbdL83hBDQjdehfZgipSwZdc1osAX6iJpGSj_GXVxUw2ExRnU2wN-HNAm9wcN93b7fiTuUUNuW3t0Pzi7F2dNCA1PuSzUjnbXqdzuMRIGw5KK2qhmyggdRp5FBpgiJHi51T-bac2vXTPlTVw-NnwLPxa-HdkRxa6UVhMlXSjhmOTstLPS_wHuvlb9xjhfk2AqH7rJDGUaBoU5jRizX-72pEgP8uu7Dcz3cgLbC1Qd_qdvSa-HXdofhJmzIk8VplCAK2ReS96IfzXL_8B0_0h7RKBRnX5nvKvy0GfD6C3tifHhfjfxc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🎙
افشاگری وزیر کار دولت رییسی: برخی کارکنان موسسات نفتی و پتروشیمی بیش از ۲۵۰ میلیون حقوق می‌گرفتند!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/Futball180TV/105674" target="_blank">📅 14:01 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105673">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/37d1369def.mp4?token=Hx_Yg79MCE4nWQArapQPQZdWLLp-duuQamZsvdtbrby-5tBUjX2GvxS05ksZQD0It7Vmzcmvsw4JgWyxl_l1wFtHO0k3REURlkXibiM-m2FkPtn__xO4yytUf0ZjPziSasfoxgwWqyqhiglnyOhw7PyfDm9h6y-CnxEC-4C5elZiRVS7_oY1vvobIwYH1ifOD7wAA69_TnCFxP-LjC9xP2_jCUVBB4bNltWTfF4yEidAfK3LP87e0KL42t0H3lPmMlciPKAC7IcIj_mrWgOfArc-1-esI5jkHfayO3uljgUo94L7RHlukPNpah6Y1aSc6QjYqS4YLZ_MpoTyoZIz0XEXOdEoIIMZ1S3umeEjSFMN6lhYc1TMKMqsQOUvWwCRpCBpaWkdZrdPqPnK4d1mR-30HBlo4PVMn20EFSDVRPcwhMv3ArZ05S93JnpC-frSMyF1ZTrYHRx2eaLvVcSx33Zelyr_3noeehvOMkRn8bv8oNMPBToe0ygUNVBwkV1jwlJ6vPuoK68Bt26FQCISNwMcX1bY-K0qm7KrzKGqyn_TTUiaxELOHXdUir05AqB_UiwG0rb0zjVklKPAEJ0Bex_pcmBVE0bIXYy_O-uodspe9kBXMPN2HsJdgKCwTLV0YXmkHS50kNc5M4Cagx8Xj2PvhircNS5Or6n48_D2x_g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/37d1369def.mp4?token=Hx_Yg79MCE4nWQArapQPQZdWLLp-duuQamZsvdtbrby-5tBUjX2GvxS05ksZQD0It7Vmzcmvsw4JgWyxl_l1wFtHO0k3REURlkXibiM-m2FkPtn__xO4yytUf0ZjPziSasfoxgwWqyqhiglnyOhw7PyfDm9h6y-CnxEC-4C5elZiRVS7_oY1vvobIwYH1ifOD7wAA69_TnCFxP-LjC9xP2_jCUVBB4bNltWTfF4yEidAfK3LP87e0KL42t0H3lPmMlciPKAC7IcIj_mrWgOfArc-1-esI5jkHfayO3uljgUo94L7RHlukPNpah6Y1aSc6QjYqS4YLZ_MpoTyoZIz0XEXOdEoIIMZ1S3umeEjSFMN6lhYc1TMKMqsQOUvWwCRpCBpaWkdZrdPqPnK4d1mR-30HBlo4PVMn20EFSDVRPcwhMv3ArZ05S93JnpC-frSMyF1ZTrYHRx2eaLvVcSx33Zelyr_3noeehvOMkRn8bv8oNMPBToe0ygUNVBwkV1jwlJ6vPuoK68Bt26FQCISNwMcX1bY-K0qm7KrzKGqyn_TTUiaxELOHXdUir05AqB_UiwG0rb0zjVklKPAEJ0Bex_pcmBVE0bIXYy_O-uodspe9kBXMPN2HsJdgKCwTLV0YXmkHS50kNc5M4Cagx8Xj2PvhircNS5Or6n48_D2x_g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
🇮🇷
جمله کنایه‌آمیز نکونام: چون یکسری قانون خوب داریم، تا نیم‌فصل نمی‌توانیم بازیکن بزرگسال بجای مهدی‌ترابی جذب کنیم. خودمان برای حضور در آسیا دست و پای خودمان را می‌بندیم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/Futball180TV/105673" target="_blank">📅 13:28 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105672">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/Futball180TV/105672" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/Futball180TV/105672" target="_blank">📅 13:28 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105671">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rGngy_NR_PYnmbkkvozvaZ0wH7RWU91KWuhlf_ydlTR0YcqV5h7Z5R6jLcuVZ63_CrkiIg1-NzFrVTNnFy7yilaOfu4hB7lbt5MOF7DYbzgNHzO7jGOvhFYGQwwJpJqOLNHjAvHedlZDsc1JHz3VHqVkdfP5NS-fuaARIAG7D6rCLHmpSw8DGiWDz8henauplLjT3Rj20kivQmxIFJjoDsBXhXXIqQZnUmcOZ6JG2KVzh0hZlJigqpLpt3UmRf1ir9Z13DJTlSF7PM2ehs6j1HDpGaYknN94RVmLR4b2KQF09w6gR6p6ywL6G9gk0R8vrkng_ymypf1b3seMIumI_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
مچ‌های مهم امروز در سایت بین‌المللی
TrexBet
پیش‌بینی کنید
.
اورتون
🆚
منچستریونایتد
آرسنال
🆚
چلسی
آلومینیوم
🆚
استقلال
والنسیا
🆚
بارسلونا
یوونتوس
🆚
میلان
🦖
🦖
🦖
🦖
🦖
بونوس اولین واریز تا سقف ۱۰۰ یورو
🦖
بهترین ضرایب بین تمام سایت‌ها
🦖
واریز و برداشت آسان و امن
انتخابت رو انجام بده و آماده‌ی هیجان باش!
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/Futball180TV/105671" target="_blank">📅 13:28 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105670">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JvoyJHP6XywdQV-CH2iKl5AlTIG_LX1U_H6TlMqUZYvlixl2KiHia0AUqs7xjrqfu4uZC_iKwy2FXWas3W4wBrCRIIVK25WaApTmt5auoy9_N1KP__fl4VW9PIDApz5aZASGE6UUSJmezxNRfASOQIhnqyMl8GWFR0cANWF6q99_CzbGRk1xg2ayj1MSs7KE-WfPvw6I6UjKGa12wIkJzo4S2JqU7ZdOxqxFMrysgwQ1WV0RSSiT5btSlecxWm449s9UyGI1_slimZ5-lU6T5UT4Qn4kDfj1z1ZsIW4OmRcSi4jo9lSiSLzMH5ZGelxNII3FH7i1vnF-P5u4RtSFcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇺
🤩
🇮🇹
🇪🇸
مایکل‌اولیور انگلیسی داور بازی روز سه‌شنبه رئال‌مادرید و‌ اینتر شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/Futball180TV/105670" target="_blank">📅 13:21 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105669">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd7107d982.mp4?token=ud3HUOjqakmE-uOKcL2yTEGsTF4ncLTo7us8sJ8-dSV8NrQBg7LdmDHCqR6YfMTL_AQexGQOI3pXCV5xxgZThkBkZl7OUC8qW-LTorDGIYy32Ayd5HG6x6sQFmO9QA_W9WgwpZA9D9nsXTEPsUOYr22QayvX6T98r2wSW0We3IYrPtt1w54Lap-6WUqy-dAkUZvmAuKCeskb6Fks44KLqQ2YsJvottAC0IpRZgg57prm4GEQbqGFtXf1vI5yxt5WEUD0AsCvMyqOwmMhhbF1ZFdMWu5LTRclZh0kUacL_4gfpify64nVLHDIXPUVs3vvM4sjQ7DevHdcm2POROhs9g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd7107d982.mp4?token=ud3HUOjqakmE-uOKcL2yTEGsTF4ncLTo7us8sJ8-dSV8NrQBg7LdmDHCqR6YfMTL_AQexGQOI3pXCV5xxgZThkBkZl7OUC8qW-LTorDGIYy32Ayd5HG6x6sQFmO9QA_W9WgwpZA9D9nsXTEPsUOYr22QayvX6T98r2wSW0We3IYrPtt1w54Lap-6WUqy-dAkUZvmAuKCeskb6Fks44KLqQ2YsJvottAC0IpRZgg57prm4GEQbqGFtXf1vI5yxt5WEUD0AsCvMyqOwmMhhbF1ZFdMWu5LTRclZh0kUacL_4gfpify64nVLHDIXPUVs3vvM4sjQ7DevHdcm2POROhs9g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🏴󠁧󠁢󠁥󠁮󠁧󠁿
مارسکا در مراسم معارفه ایوب بوعدی به بازیکنان سیتی: فقط خودت باش، ما میدونیم تو چقدر خوبی، اینجا لازم نیست چیزی رو به کسی اثبات کنی. کار کن، یاد بگیر، لذت ببر و خودت باش.⁣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/Futball180TV/105669" target="_blank">📅 13:10 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105668">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/63b1b9b41e.mp4?token=n5mKNyLaljNNOei611JHgWWLKXEpNzaAB8pHZtqKNDEvBw4UO5Guqo52BsJSmYs2x4Kfbyb2mSn_NlFs21h3EoyX57e9sK7z9CKyNjhFms-TwnNIKQvc9gJ0DEuskQ-KjhgAj2hcTvPI08uOnjkZDHrsbUqU7N0c1m2L4H1kFQnRPlaT3G_oSaa330nQKOrKalY8wd42f99jXM4o9x0v47WAFbMub0lMkuvI4Br3SGKxnXDwiatPzSYPBuzCtaf8NX31iFYeirFhh9STQZWH3jaQhuXxd__1ljXJ6ZUGIwqY31g4C_A4jkm0k_vJWUL-jfTgC1X5d9VSd_hPqbUJCA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/63b1b9b41e.mp4?token=n5mKNyLaljNNOei611JHgWWLKXEpNzaAB8pHZtqKNDEvBw4UO5Guqo52BsJSmYs2x4Kfbyb2mSn_NlFs21h3EoyX57e9sK7z9CKyNjhFms-TwnNIKQvc9gJ0DEuskQ-KjhgAj2hcTvPI08uOnjkZDHrsbUqU7N0c1m2L4H1kFQnRPlaT3G_oSaa330nQKOrKalY8wd42f99jXM4o9x0v47WAFbMub0lMkuvI4Br3SGKxnXDwiatPzSYPBuzCtaf8NX31iFYeirFhh9STQZWH3jaQhuXxd__1ljXJ6ZUGIwqY31g4C_A4jkm0k_vJWUL-jfTgC1X5d9VSd_hPqbUJCA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
🇮🇷
روایت تاریخی رویانیان از هزینه مراسم وداع با اسطوره مهدی مهدوی‌کیا در‌ پرسپولیس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/105668" target="_blank">📅 12:45 · 15 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
