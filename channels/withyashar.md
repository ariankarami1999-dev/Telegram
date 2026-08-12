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
<img src="https://cdn4.telesco.pe/file/WhhBM6f7AkA7Y29iNqYOcm5u7-34VwaAw3uTeaz8iFB6shMOp7MkHoIINx8QghLj1j7sJw3rKpZATo5lFn8bwo7PKXa_eSTJQwf7Ae9-aP09ngCkYAuKfuX8t9LdonEv7EHIUk1jo4ZmOBVFaIQwiWOa5BSjs4IeHdjl3VHMc677p5FV_61ZRk2krC4RkTTzwbHvZ2FhAZSSE9ppHI5qrCSKTXsDefXZdtcEc5BKgRHFb_Q4TpoJY87-a2E1CzvzJ8WRdM0f_axdmeKv4aJBvy-RfEKveve4K5gAWFH77dLQNkU89r3ZyDrsc87cAPw2jE4Cab3FQSWZZAzH4xsDKw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 WarRoom with YASHAR</h1>
<p>@withyashar • 👥 445K عضو</p>
<a href="https://t.me/withyashar" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 چنل رسمی«اتاق جنگ با یاشار»اخبار لحظه ای و فوری از‌ جنگ با تحلیل📸instagram.com/yashar🐦x.com/yasharrapfa📺youtube.com/yasharrapfa⛑️paypal.com/paypalme/yasharrapfa</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-21 04:40:03</div>
<hr>

<div class="tg-post" id="msg-20863">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c87bdfe17b.mp4?token=OHWQRoyQZhScSpFsMez0EwCR3Z32HvRzrhiPx3Z_GVeDjLu6k7SuFhnnRiEmDvLGKlMF6n_kdgfANqZ9xtFGgkry9y0QAPVFpavU9riJq_Rz7EXYb9rd91yxPMhd6UhjSCDnsLDhSuH3L0bzXJiEviqYxxA_tsQ4CrHOQWpJJGHOweonnIBpruq2EYmB1Ycbj7Dlzvo0aUOMMdjIWtW-H-KbpE9f5SbPht-M-RsEPUIq9nvp-3z6UoN1eJnHA8tVyAEXSMh1LRTYQuP1vOQCzc7vGlRc4_Ip2yVsH1Mc_gKeyZEsFcvL46V6arQt1ebDv3hRVwsUzkvnidIuQdzyyw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c87bdfe17b.mp4?token=OHWQRoyQZhScSpFsMez0EwCR3Z32HvRzrhiPx3Z_GVeDjLu6k7SuFhnnRiEmDvLGKlMF6n_kdgfANqZ9xtFGgkry9y0QAPVFpavU9riJq_Rz7EXYb9rd91yxPMhd6UhjSCDnsLDhSuH3L0bzXJiEviqYxxA_tsQ4CrHOQWpJJGHOweonnIBpruq2EYmB1Ycbj7Dlzvo0aUOMMdjIWtW-H-KbpE9f5SbPht-M-RsEPUIq9nvp-3z6UoN1eJnHA8tVyAEXSMh1LRTYQuP1vOQCzc7vGlRc4_Ip2yVsH1Mc_gKeyZEsFcvL46V6arQt1ebDv3hRVwsUzkvnidIuQdzyyw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ در محل بازی‌های میهن‌پرستانه:  به والدین نگاه می‌کنم، آنها به فرزندانشان بسیار افتخار می‌کنند. و من به گروه افراد حاضر در این اتاق بسیار افتخار می‌کنم. عشق به کشورمان را می‌بینید. کشورمان هرگز بهتر از این نبوده است!
@WarRoom</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/withyashar/20863" target="_blank">📅 02:56 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20862">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">چیزی نیست رعدنیاهو بود غرب تهران
😂</div>
<div class="tg-footer">👁️ 42.8K · <a href="https://t.me/withyashar/20862" target="_blank">📅 02:27 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20861">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">گزارش صدای رعد و برق شدید</div>
<div class="tg-footer">👁️ 45.3K · <a href="https://t.me/withyashar/20861" target="_blank">📅 02:24 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20859">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">بلومبرگ
:
دونالد ترامپ موضع خود را در قبال ایران سخت‌تر کرده است و این امر، امیدها را برای دستیابی به توافقی جهت بازگشایی تنگه هرمز کمرنگ‌تر ساخته است.
@WarRoom</div>
<div class="tg-footer">👁️ 57K · <a href="https://t.me/withyashar/20859" target="_blank">📅 01:51 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20858">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">گزارش ها از درگیری تمام عیار زمینی میان حوثی های یمن و نیروهای نظامی وابسته به عربستان در شمال یمن.
@WarRoom</div>
<div class="tg-footer">👁️ 78.7K · <a href="https://t.me/withyashar/20858" target="_blank">📅 01:01 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20857">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">آمریکا 2 هزار گیمر رو به‌خاطر تصمیم‌گیری سریع و عملکرد خوب تو شرایط پراسترس ، برای برج مراقبت فرودگاه‌ها استخدام کرده
@WarRoom</div>
<div class="tg-footer">👁️ 80.2K · <a href="https://t.me/withyashar/20857" target="_blank">📅 01:00 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20856">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f1ab5e54bb.mp4?token=mRzir3BrqEAy9wQJ07jWQxGy6wF1rQbhrc5Bz3Vb-QjIZWT6XVs-5XNlrY5-XVSj2XArh7OYN_Y04-K_py3dXBky_k489_cT_SQeVAOPahqCa_uppux9frsjAwNJVprhcJWfC7JR9Ug4RkYqosU1bzegNBBU8sBDzZ0HBBdqL5aDrmBfG-0I0wLwqFPRqRUgG4LG_2mUpP1tNcK5Qd0SAH6AKB3M0Ia3e4PRVVmIVxhlCQeDx6ivFpicH4zfuMCO0mnkaiWCRoLuAeiEXbvL1HHAMJfX0ucOysYHVCUuZ8ma3ZgRe2eWQZp0h4ypRUrPQ84Gpuw2FUpKSLBk7jyI3nTZiw8F5FjhTDbo0um2rcOgUAdi8YfS7aBC7fidyLAktHKTIH8M9SA8f9HWm4PkjGiyjcXIUU1HmCoLg3Qj0wSdZw3ROKJXXJ1ZoA0spdQUtpShLvuWFv_CxnFmFvzaYAOAptHGhnR-KLvTsXAuhyZGzNlg9rYJeDkV6Or40qmpteEluuguNlTJtG4E-g6I0bt6WLAH3-Jnq3rB9w2qni7fBs9WWVdMJmN2xqbY1TtRK4njcrr7IQUebRs8KWDvrSajILLhg9HSuHJzU5MHdHrCPEkFNuWs9Qs7vCSolsR84I4-rL2hBEBDRssRT20nZ0YJ0W7D8I4QZXO50VaZ3dg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f1ab5e54bb.mp4?token=mRzir3BrqEAy9wQJ07jWQxGy6wF1rQbhrc5Bz3Vb-QjIZWT6XVs-5XNlrY5-XVSj2XArh7OYN_Y04-K_py3dXBky_k489_cT_SQeVAOPahqCa_uppux9frsjAwNJVprhcJWfC7JR9Ug4RkYqosU1bzegNBBU8sBDzZ0HBBdqL5aDrmBfG-0I0wLwqFPRqRUgG4LG_2mUpP1tNcK5Qd0SAH6AKB3M0Ia3e4PRVVmIVxhlCQeDx6ivFpicH4zfuMCO0mnkaiWCRoLuAeiEXbvL1HHAMJfX0ucOysYHVCUuZ8ma3ZgRe2eWQZp0h4ypRUrPQ84Gpuw2FUpKSLBk7jyI3nTZiw8F5FjhTDbo0um2rcOgUAdi8YfS7aBC7fidyLAktHKTIH8M9SA8f9HWm4PkjGiyjcXIUU1HmCoLg3Qj0wSdZw3ROKJXXJ1ZoA0spdQUtpShLvuWFv_CxnFmFvzaYAOAptHGhnR-KLvTsXAuhyZGzNlg9rYJeDkV6Or40qmpteEluuguNlTJtG4E-g6I0bt6WLAH3-Jnq3rB9w2qni7fBs9WWVdMJmN2xqbY1TtRK4njcrr7IQUebRs8KWDvrSajILLhg9HSuHJzU5MHdHrCPEkFNuWs9Qs7vCSolsR84I4-rL2hBEBDRssRT20nZ0YJ0W7D8I4QZXO50VaZ3dg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دونالد ترامپ برای شرکت در رویداد
Freedom 250 Patriot Games
(رقابت‌های میهن‌دوستانه ورزشی ویژه جوانان آمریکایی به مناسبت ۲۵۰مین سالگرد استقلال آمریکا) عازم شهر ژنو در ایالت اوهایو شد و سوار هواپیمای ریاست‌جمهوری
ایرفورس وان
جدید شد
@WarRoom</div>
<div class="tg-footer">👁️ 91.7K · <a href="https://t.me/withyashar/20856" target="_blank">📅 00:24 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20855">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">گزارش ها از هدف قرار گرفتن ایست ‌و بازرسی نیروهای نظامی توسط افراد مسلح ناشناس در شهر مرزی خاش در سیستان و باوچستان ، بر اساس گزارشات داخلی 4 نظامی در این حادثه کشته شدند
@WarRoom</div>
<div class="tg-footer">👁️ 91.7K · <a href="https://t.me/withyashar/20855" target="_blank">📅 00:20 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20854">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">محمدرضا نقدی، مشاور فرمانده سپاه، گفت که «این سازمان باید برای انجام عملیات هوشمند در خاک دشمن آماده شود.»
@WarRoom</div>
<div class="tg-footer">👁️ 96.1K · <a href="https://t.me/withyashar/20854" target="_blank">📅 00:04 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20853">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">پرواز بالگرد آپاچی ۶۴ آمریکایی در نزدیکی قشم  @WarRoom</div>
<div class="tg-footer">👁️ 96.5K · <a href="https://t.me/withyashar/20853" target="_blank">📅 00:01 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20852">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pFM_EigLFctsNOdx18c30WHEIgzCu28WClxW5MT14gHf1SF7c8_yRHGV8WBo34CeFaKNeGH9TrMuQrswC5yCSBIoPMmZUjs9fd3hC-drYmKC2s1FR88k7l2XHr_6oaSDzR0pUyYDo4cTp6Jg52Op8Eb0mFeclLZZ0ZcAFEilcNwr36lrp65wI-R2_Dso5sYnhSjmfxedhfl62U5CnKO1UHYw-ijkjIDijJHR0mpgdG5jf1HUx6uAHCd1Z-AGp2rDHgX14Lv8rk1JJgCPVY6syZ-JpaYIwFeEunfDrBjZK0iIr1COwxa4eUD8B5ZyIj7zZUwxBGydkJkx0Z7dEncU9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کانال ۱۴ اسرائیل: مجتبی شش تندرو جدید را برای رهبری جنگ بعدی ایران منصوب می‌کند
با وجود شایعات فزاینده درباره سلامت مجتبی خامنه‌ای، تهران ادعا می‌کند که او شش تندرو از رژیم را برای رهبری جنگ بعدی ایران منصوب کرده است؛ پیامی نگران‌کننده برای اسرائیل و ایالات متحده مبنی بر اینکه رژیم در حال تشدید تنش‌هاست، نه عقب‌نشینی
@WarRoom</div>
<div class="tg-footer">👁️ 103K · <a href="https://t.me/withyashar/20852" target="_blank">📅 23:40 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20851">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">باراک راوید , آکسیوس : امید به توافق میان جمهوری اسلامی و آمریکا در حال محو شدن است
@WarRoom</div>
<div class="tg-footer">👁️ 108K · <a href="https://t.me/withyashar/20851" target="_blank">📅 22:44 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20850">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IEpKnGPJtpjWvYHo8UBUXeXWAFoCusjhuPSbSE1rTabgwE-HJ5t3J7MGcJmYOQfRDunPmd_uIz4oEznHcUJJAFRpjDqrla9LoBA24ZnJ0FZ5GVGUAb4-SrO7G7oD98_Qh6AN3qr-licKFCuSAELaz8wty8IWc3T0QHECYGdQXYWJ8vCMrOF931i9GZP3-EESPs-bClrC3YcRrzUD-_rrhb3q88TK0kx9SIgIgU1rOxSMcrDYe0Hz-2hqeWB452GK0QkMvNlL9j-wTBIC0V_dka3a4L-xUjmp9SFSMhGWw2JfEA_PT1X0nLw7vWsJqpYDOGV3GyFGUckKwOxwSe6kVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سنتکام اعلام کرد نیروهای آمریکایی امروز کشتی باری «ولا نوا» با پرچم پاناما را هنگام حرکت به سمت یکی از بنادر ایران در خلیج عمان متوقف کردند. پس از بی‌توجهی خدمه به هشدارهای آمریکا، یک بالگرد MH-60 دو موشک هل فایر به اتاق موتور کشتی شلیک کرد و سامانه هدایت آن را از کار انداخت. سنتکام گفت تا ۱۱ اوت، ۵۵ کشتی تجاری را تغییر مسیر داده، ۳ کشتی را از کار انداخته و ۲ کشتی را سوار و بازرسی کرده است.
@WarRoom</div>
<div class="tg-footer">👁️ 107K · <a href="https://t.me/withyashar/20850" target="_blank">📅 22:44 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20849">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromA B</strong></div>
<div class="tg-text">یاشاار
جون هرکی دوست داری زارتان زورتان و حذف نکن از ادبیاتت
من هم توهمی دهنم سرویس شده
از وقتی نمیگی برکت از جنگ رفت
🤣
خداییش جدی میگم</div>
<div class="tg-footer">👁️ 107K · <a href="https://t.me/withyashar/20849" target="_blank">📅 22:26 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20848">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">سازمان دریایی بریتانیا: فعالیت‌های سپاه در تنگه هرمز در طول 48 ساعت گذشته ادامه داشته است.
@WarRoom</div>
<div class="tg-footer">👁️ 108K · <a href="https://t.me/withyashar/20848" target="_blank">📅 22:11 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20847">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">دونالد ترامپ در چارچوب قانون اختیارات جنگ آمریکا (War Powers Resolution)، با ارسال نامه‌ای به کنگره که ۱۹ تیر ۱۴۰۵ امضا و ۲۲ تیر ۱۴۰۵ به‌طور رسمی اعلام شد، از ازسرگیری عملیات نظامی علیه ایران خبر داد. با این اقدام، مهلت قانونی ۶۰ روزه برای ادامه عملیات نظامی بدون مجوز جدید کنگره آغاز شد. این اقدام به معنای صدور مجوز جنگ از سوی کنگره نیست، بلکه صرفاً روند قانونی اطلاع‌رسانی به کنگره و آغاز مهلت ۶۰ روزه را فعال می‌کند.
@WarRoom</div>
<div class="tg-footer">👁️ 113K · <a href="https://t.me/withyashar/20847" target="_blank">📅 21:45 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20846">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-footer">👁️ 109K · <a href="https://t.me/withyashar/20846" target="_blank">📅 21:34 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20845">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">من با دیتا های اپن سورس تحلیل میکنم پیشگو که نیستم ! هیچ تاریخی هم نمیدم فقط احتمالاته اگه انقدر حساسی  پس از الان رو نزدن حساب کن  ! اگه حرفه ای هستی پس ویس هارو گوش کردی کامل روحیات منم میدونی و دیگه سوألی هم نداری که هی داریکت بدی</div>
<div class="tg-footer">👁️ 111K · <a href="https://t.me/withyashar/20845" target="_blank">📅 21:23 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20844">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">به نظرت قطعی شنبه میزنه من میخوام با بچه ها شرط ببندم</div>
<div class="tg-footer">👁️ 109K · <a href="https://t.me/withyashar/20844" target="_blank">📅 21:19 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20843">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromSajad Mousavi</strong></div>
<div class="tg-text">به نظرت قطعی شنبه میزنه من میخوام با بچه ها شرط ببندم</div>
<div class="tg-footer">👁️ 108K · <a href="https://t.me/withyashar/20843" target="_blank">📅 21:13 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20842">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">گزارش ۲ ‌انفجار یا پرتاب موشک/پهپاد از سیریک @WarRoom</div>
<div class="tg-footer">👁️ 109K · <a href="https://t.me/withyashar/20842" target="_blank">📅 21:05 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20841">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">گزارش ۲ ‌انفجار یا پرتاب موشک/پهپاد از سیریک
@WarRoom</div>
<div class="tg-footer">👁️ 110K · <a href="https://t.me/withyashar/20841" target="_blank">📅 20:48 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20840">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">ترامپ اعلام کرد که رابرت گیلمن، سرباز سابق نیروی دریایی ایالات متحده که در سال ۲۰۲۲ در روسیه زندانی شده بود، پس از گفتگوها با ولادیمیر پوتین، آزاد شده و به ایالات متحده بازمی‌گردد.
ترامپ گفت که روسیه موافقت کرده است گیلمن را بر اساس «ملاحظات انسان‌دوستانه» آزاد کند و «هیچ مبادله‌ای انجام نشده است».
ترامپ همچنین گفت که اولین درخواست گیلمن یک «همبرگر عالی» بوده است.
@WarRoom</div>
<div class="tg-footer">👁️ 110K · <a href="https://t.me/withyashar/20840" target="_blank">📅 20:46 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20839">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">ترامپ : ما بر پول ایران کنترل داریم و کنترل کاملی بر آن اعمال می کنیم
ترامپ : سلاح و جنگنده به اروپا می‌فروشیم و آن‌ها در ارسال به اوکراین آزادند
@WarRoom</div>
<div class="tg-footer">👁️ 108K · <a href="https://t.me/withyashar/20839" target="_blank">📅 20:45 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20838">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">اسرائیل و ونزوئلا پس از ۱۷ سال قطع روابط دیپلماتیک، توافق کردند که روابط کنسولی خود را از سر بگیرند و یک کانال هماهنگی رسمی ایجاد کنند.
@WarRoom</div>
<div class="tg-footer">👁️ 107K · <a href="https://t.me/withyashar/20838" target="_blank">📅 20:43 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20837">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/797367122e.mp4?token=BvEpAfeAfl63_KiiVEZtAZ2O4zpjQeifPPwvO7SMHn4BqOSNVtrwwaNpVWSZ_F6IuiutS9mOCgZpYa4Uf69LlUzS_cZ2TtSLUeIF6l1yEvOtULIfF6-vBSsRMb-2PRZq-GNhMBxzRuc0A_Zkq-plmkZ6HZMYq0SZ6LzZ9trneLKal_kfx2P6U7CKATWIV9tiKp_ExU9plHB5dKvdTuN7kAV9om4DOdIC_LFbiywoLszot_Sggh016Zn_8eNJ9HimbT7fQd16WVlZEEPFbflD7FncHiyY2GJWbl_jZw6Gt0-gLmHx2CtU7M9FBqMvn1xOEhy8oCLUEY1GrmrKSNLRHQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/797367122e.mp4?token=BvEpAfeAfl63_KiiVEZtAZ2O4zpjQeifPPwvO7SMHn4BqOSNVtrwwaNpVWSZ_F6IuiutS9mOCgZpYa4Uf69LlUzS_cZ2TtSLUeIF6l1yEvOtULIfF6-vBSsRMb-2PRZq-GNhMBxzRuc0A_Zkq-plmkZ6HZMYq0SZ6LzZ9trneLKal_kfx2P6U7CKATWIV9tiKp_ExU9plHB5dKvdTuN7kAV9om4DOdIC_LFbiywoLszot_Sggh016Zn_8eNJ9HimbT7fQd16WVlZEEPFbflD7FncHiyY2GJWbl_jZw6Gt0-gLmHx2CtU7M9FBqMvn1xOEhy8oCLUEY1GrmrKSNLRHQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پرواز بالگرد آپاچی ۶۴ آمریکایی در نزدیکی قشم
@WarRoom</div>
<div class="tg-footer">👁️ 112K · <a href="https://t.me/withyashar/20837" target="_blank">📅 20:21 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20836">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">رسایی : چونکه نمیدانیم اسرائیل کِی حمله میکند مجبوریم جلسات مجلس را مجازی کنیم
@WarRoom</div>
<div class="tg-footer">👁️ 111K · <a href="https://t.me/withyashar/20836" target="_blank">📅 20:19 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20835">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">پست قبلی بی بی پاک شد این پست کارای اداری رو انجام بدید
https://www.instagram.com/reel/Db6BHf7MYhi/?comment_id=17896725462373851</div>
<div class="tg-footer">👁️ 111K · <a href="https://t.me/withyashar/20835" target="_blank">📅 20:09 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20833">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">نتانیاهو : جولان سرزمین ماست و برای همیشه متعلق به اسرائیل خواهد بود.
@WarRoom</div>
<div class="tg-footer">👁️ 116K · <a href="https://t.me/withyashar/20833" target="_blank">📅 18:52 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20832">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">دونالد ترامپ: ایالات متحده می‌تواند بزودی و با قدرت بسیار زیاد به ایران حمله کند.
@WarRoom</div>
<div class="tg-footer">👁️ 118K · <a href="https://t.me/withyashar/20832" target="_blank">📅 18:25 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20831">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">یوآو کیش، وزیر آموزش اسرائیل:
صرف نظر از اینکه رئیس جمهور آمریکا چه کسی باشد، حتی پس از ترامپ,  اگر لازم باشد به تنهایی اقدام کنیم، به تنهایی اقدام خواهیم کرد.
@WarRoom</div>
<div class="tg-footer">👁️ 120K · <a href="https://t.me/withyashar/20831" target="_blank">📅 17:38 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20830">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iGaJqVfjWXd9j7NivqA6deJ6a3SD16p7C74px9C3jTcycgMuAMB84abPFsYoKA1fZ6yUhaQ_y7fFxDS0OTERiDvOZ2OPvlVfO4WDz-1mSY-scex6p9jB-IITFLJQkTxrdLInQXwtTnzlYktR-B61Gno57U8zM67gpYjS3ddpXm1Hgw2UGJSHzsylrKPjCDvsl3eB1cm8fLnDXV0b3YNl6PUfd09iJP7tc6D-c0y6nSXfTH5zE7O1b0wscuwSJ2WRZpPURDJJb_keLsMtP-Y_SBsZ3laUXDKHQ2fy_D-Pxp5OzeToh7XmExP08IcFpC3OWJAYEBuTashqrbx3Q4ZCVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزارت خارجه اسرائیل : ترکیه این جسارت را دارد که از اسرائیل انتقاد کند؛ اما واقعیت‌های میدانی چیست؟ هزاران سرباز ترکیه و ده‌ها پایگاه و موضع نظامی در سوریه، عراق و قبرس مستقر هستند. در حالی که تجاوز نظامی اردوغان مرزی نمی‌شناسد، ترکیه ۳۶ درصد از خاک قبرس، ۵ درصد از خاک سوریه و ۲ هزار کیلومتر مربع از خاک عراق را در اشغال خود دارد. در مقابل، اسرائیل به‌طور موقت تنها ۰.۱ درصد از خاک سوریه را در اختیار دارد؛ منطقه‌ای حائل که به گفته اسرائیل، برای حفاظت از شهروندانش در برابر تهدیدهای امنیتی اثبات‌شده ایجاد شده است.
@WarRoom</div>
<div class="tg-footer">👁️ 122K · <a href="https://t.me/withyashar/20830" target="_blank">📅 17:35 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20829">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">به گزارش رسانه‌های اسرائیلی،
یوسی کوهن، رئیس پیشین موساد در نشست «مجمع جلیل» در شهر صفد گفت: «ما بارها از سایت هسته‌ای فردو بازدید کردیم تا این سایت را درک و شناسایی کنیم.»
او مشخص نکرد که این بازدیدها چه زمانی انجام شده یا دقیقا چه کسانی از این سایت بازدید کرده‌اند
@WarRoom</div>
<div class="tg-footer">👁️ 114K · <a href="https://t.me/withyashar/20829" target="_blank">📅 17:21 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20823">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">روال هر روز پیج اینستاگرام در ۴ دقیقه ریکاوری شد
😁
عرضشی عر بزن
🤣</div>
<div class="tg-footer">👁️ 117K · <a href="https://t.me/withyashar/20823" target="_blank">📅 16:44 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20822">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s8Y9WeNGQ14Os5rwFgbYG9h2H3S-NjQG_LpDfGbz2wLhrOfx6D4ZL0HhL6IJANFF5A8Oh7SC-ciQdM0Rd4iVzUjL4EVgGSEJD9GK_QjZDaj64N8ytVaMDIvsWnOE8gWew1FSq2pmnXgFEf9Ubm5tKumuZLb45C0wSI1UjZmuwACTei2llTEHFrH18tWULuwy66AcbJev76LXjCk9NpGWJStrRd1uZ6hyUCtj0lB5pg6hwptVtJmrlDqA5ucYhN9Jqf-JzZ5GkNJ1N5WtPGnZYQg5ELBdmEL0rZsOztn5RhGntS6YRZ5vygq1fzm6TYcmXdoXceTmXq9zfnt2hfdpkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بی بی دوزندهیاهو : آتش‌سوزی در کارخانه نخ اطراف بیدگنه،  ملارد
@WarRoom</div>
<div class="tg-footer">👁️ 119K · <a href="https://t.me/withyashar/20822" target="_blank">📅 16:35 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20821">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">دبیر شورای عالی امنیت ملی ج.ا : ما در یکی از حساس‌ترین و سرنوشت‌سازترین مراحل تاریخ معاصر خود قرار داریم , در برابر تهدیدها، از حقوق خود و منافع ملت‌مان عقب‌نشینی نخواهیم کرد.
@WarRoom</div>
<div class="tg-footer">👁️ 111K · <a href="https://t.me/withyashar/20821" target="_blank">📅 16:24 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20820">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">وال استریت ژورنال : نیروهای آمریکایی امروز به سمت یه کشتی که با پرچم پاناما حرکت می‌کرده، شلیک کردن. ظاهراً این کشتی قصد داشته محاصره بنادر ایران توسط آمریکا رو نقض کنه. @WarRoom</div>
<div class="tg-footer">👁️ 113K · <a href="https://t.me/withyashar/20820" target="_blank">📅 16:23 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20819">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">وال استریت ژورنال : نیروهای آمریکایی امروز به سمت یه کشتی که با پرچم پاناما حرکت می‌کرده، شلیک کردن. ظاهراً این کشتی قصد داشته محاصره بنادر ایران توسط آمریکا رو نقض کنه.
@WarRoom</div>
<div class="tg-footer">👁️ 113K · <a href="https://t.me/withyashar/20819" target="_blank">📅 16:05 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20818">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">وزیر دفاع پاکستان به بلومبرگ:
نشانه‌های روزهای گذشته حاکی از آن است که به توافق صلح (یاشار: بمباران) نزدیک می‌شویم
@WarRoom</div>
<div class="tg-footer">👁️ 111K · <a href="https://t.me/withyashar/20818" target="_blank">📅 16:03 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20817">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">روال هر روز پیج اینستاگرام در ۴ دقیقه ریکاوری شد
😁
عرضشی عر بزن
🤣</div>
<div class="tg-footer">👁️ 113K · <a href="https://t.me/withyashar/20817" target="_blank">📅 16:01 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20816">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">آکسیوس
:
به گفته مقام‌های آمریکایی و اسرائیلی، دولت دونالد ترامپ در پشت‌پرده میان سوریه، اسرائیل و آژانس بین‌المللی انرژی اتمی برای خارج کردن مواد هسته‌ای از «سایت ۹۹» سوریه، مرتبط با برنامه هسته‌ای مخفی حکومت بشار اسد، توافق ایجاد کرد. این مواد شامل «کیک زرد» است که برای ساخت سلاح هسته‌ای کافی نیست، اما می‌تواند در بمب‌های رادیولوژیک به کار رود. اسرائیل پس از سقوط اسد با نگرانی از دسترسی به این مواد، ورودی‌های سایت را هدف قرار داده بود. عملیات انتقال هنوز انجام نشده، اما مقام‌های آمریکایی می‌گویند به‌زودی اجرا خواهد شد.
@WarRoom</div>
<div class="tg-footer">👁️ 117K · <a href="https://t.me/withyashar/20816" target="_blank">📅 15:35 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20815">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">وال‌استریت ژورنال : خامنه‌ای با تغییر مقام‌های ارشد امنیتی بر ادامه تقابل با آمریکا تاکید دارد
@WarRoom</div>
<div class="tg-footer">👁️ 114K · <a href="https://t.me/withyashar/20815" target="_blank">📅 15:08 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20814">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">گزارش حمله موشکی به اردوگاه گروه‌های کورد در شمال شرقی اربیل
@WarRoom</div>
<div class="tg-footer">👁️ 112K · <a href="https://t.me/withyashar/20814" target="_blank">📅 15:02 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20813">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UzM0AvsKTBU65iyzCJJpw3MosZqds3LBdNkj0zy83oOlRFXkbz99A0aqjDpwI9-Jo83mcJC0F_jffrpmPEEUOAi01ixbIDYOG_SMkdon0rVzsZWJvleAjvYmLwod8H_M_bb-M0bYlt4R1IlE7ATa8x9N_NinUvm9JMKg2G3kbNcxyaxTq6eZCx4rH-IbG90cwQ8O-Paf2jD50GZiQEdxvtWwGFKjZS1jxeZEIRUrSs71RWXJJwNQnEA8yfVq--4NWnniv24Q6d50RewpjzBxYePegS-YVq3EHCPGBPriIH0__B8jATjOfpkR3p8F7Yqsjcs22w8TFbY5oSZHsfNa8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به گزارش خبرگزاری رویترز، سازمان حمل و نقل دریایی بریتانیا (UKMTO) از حادثه‌ای در سواحل المخا، یمن مطلع شده است. گزارش شده است که یک کشتی باری در دریای سرخ جنوبی مورد اصابت یک موشک/پهپاد ناشناخته قرار گرفته و منجر به تلفات جانی شده است ، این در حالی است که یک کشتی سعودی صبح امروز مورد هدف قرار گرفت.
@WarRoom</div>
<div class="tg-footer">👁️ 119K · <a href="https://t.me/withyashar/20813" target="_blank">📅 14:39 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20812">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">سید محسن رضا نقوی، وزیر کشور پاکستان برای گفتگو با مقامات ایرانی وارد تهران شد.
@WarRoom</div>
<div class="tg-footer">👁️ 108K · <a href="https://t.me/withyashar/20812" target="_blank">📅 14:35 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20811">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">رسانه عبری : مجتبی خامنه‌ای، از احمد وحیدی، فرمانده کل سپاه پاسداران، خواست تا برای «عملیات تهاجمی قدرتمند علیه دشمن» آماده شود.
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 114K · <a href="https://t.me/withyashar/20811" target="_blank">📅 13:57 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20810">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">ترامپ درباره ایران: ما سه راهبرد داریم , همین کاری را که الان انجام می‌دهیم ادامه دهیم؛ فقط به همین شکل پیش برویم و ببینیم اوضاعشان چقدر بد است، چون تورمشان ۳۰۰ درصد است. پولشان تقریباً هیچ ارزشی ندارد. حقوق سربازانشان را نمی‌دهند. سربازانشان در حال ترک خدمت هستند. بنابراین همین روند را ادامه دهیم، چون این وضعیت پایدار نیست.
خیلی، خیلی سخت به آنها ضربه بزنیم؛ یا در واقع، راه سوم این است که از نظر اقتصادی آنها را شکست دهیم. البته همین کار را همین حالا هم انجام می‌دهیم. این تا حدی بخشی از راهبرد اول است.
بنابراین از نظر اقتصادی، آنها در وضعیت بسیار بدی قرار دارند. نمی‌توانند پول قرض بگیرند. ما کنترل پول آنها، یعنی آنچه در اختیار داشتند، را در دست داریم؛ و مقدار آن هم زیاد است. آنها پول زیادی داشتند و ما کنترل کامل آن را در اختیار داریم.
من بانکدار آنها هستم. من بانکدار آنها هستم.
@WarRoom</div>
<div class="tg-footer">👁️ 118K · <a href="https://t.me/withyashar/20810" target="_blank">📅 13:54 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20809">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">ترامپ : می‌خواهید یک گورستان پرندگان را ببینید؟ گاهی اوقات به زیر یک آسیاب بادی بروید و هزاران پرنده مرده خواهید دید.
@WarRoom</div>
<div class="tg-footer">👁️ 109K · <a href="https://t.me/withyashar/20809" target="_blank">📅 13:50 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20808">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">جورسلیم پست : ترامپ از حمله گسترده دیگری به ایران خودداری کرد ، با این امید که فشار اقتصادی بیشتر می‌تواند تهران را مجبور به تسلیم کند، بدون اینکه منجر به یک جنگ منطقه‌ای گسترده‌تر شود.
@WarRoom</div>
<div class="tg-footer">👁️ 112K · <a href="https://t.me/withyashar/20808" target="_blank">📅 13:45 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20807">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TJwa14lNoxMcWUtqA5-jgITPrzf9jSBkyxMqiEdbifXpIr756gcd84WBIrTJF7pRU5-9JuFlxUxNYi3X8m2unWdvVBHazlAxTcarE8RTwei4Bc0QjFQjfSnWyLww0I70K_1A3YrdlscUkUxi6dXzPxq3a-uhoRw1wxjGoRwEtdyOnUBqZqmGse3XoZSnQ-lE5REXZioHLNKlBpmcwy4L8hTga1X0OmNqMCjtYf9YJMl3fewSV_hS8Z-AvuPI3OpOGhNJcCiOAvSJrJDQkckUsdDVbqaBsHGqGnQ_pr6-BRUNLkYrHhSz7U9Ly2eJlYQU7wFQPK1yYP2sS5xKD9Y7BQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مرکز عملیات تجارت دریایی بریتانیا (UKMTO) گزارشی درباره وقوع حادثه‌ای برای یک نفتکش و نیروهای نظامی در خلیج عمان دریافت کرده است. مقام‌های مربوطه در جریان این حادثه هستند و تحقیقات مرتبط همچنان ادامه دارد.
@WarRoom</div>
<div class="tg-footer">👁️ 115K · <a href="https://t.me/withyashar/20807" target="_blank">📅 12:45 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20806">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kKefenrtjK3gcAV2aIMuifdQbaQ2_llbH21VF7I-RM6_93x4mj28mK8XqPKeW6ZRtUXGg7lOhB0ZrPHSArMqTlkGLjnX-lpvN1xZ0P3oekUBjMm690Sxm2sj3yeve-4QMEwa5w3UF9h4jsd4NJnBuedOJorhanRnRiLOrC0qTsJMRY3zdd52mx_TfimxCfpgrQgMnoQM7Z91_vYGvC22V8uKnfKt-Eru2_-NdiSOLVjk1dgshubHxNwkgs8SnltULedXSWYnvDThQJEFSA8g6KwHPdv5sQ6XTfy9UEsv_oZoJ2MxU0FecAaHgzxxBU1XQ7Y_mVn3tfqmywy3J_C2dw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۷ فروند هواپیمای سوخت‌رسان KC-46A پگاسوس نیروی هوایی آمریکا از پایگاه‌های مبدأ خود در غرب ایالات متحده به پایگاه هوایی مک‌دیل در فلوریدا، در شرق آمریکا، منتقل شده‌اند؛ جابه‌جایی‌ای که می‌تواند نشانه‌ای از آماده‌سازی برای اعزام قریب‌الوقوع شماری از هواپیماهای…</div>
<div class="tg-footer">👁️ 115K · <a href="https://t.me/withyashar/20806" target="_blank">📅 12:38 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20805">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">دادگاه جنایی دمشق حکم اعدام برای بشار اسد صادر کرد
@WarRoom</div>
<div class="tg-footer">👁️ 113K · <a href="https://t.me/withyashar/20805" target="_blank">📅 12:19 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20804">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">https://www.instagram.com/reel/Db5HBuLozsg/?igsh=ajBqMW82djZrZW96
استوری که درخواست زیاد داشتید رو به صورت تریال پست کردم</div>
<div class="tg-footer">👁️ 116K · <a href="https://t.me/withyashar/20804" target="_blank">📅 11:34 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20803">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">گزارشهای رسانه های‌عربی حاکی از کشته شدن ۳ نفر در پی حمله حوثی ها به یک کشتی در تنگه باب المندب است
@WarRoom</div>
<div class="tg-footer">👁️ 119K · <a href="https://t.me/withyashar/20803" target="_blank">📅 10:41 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20802">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/If_a-DPCFsPm0Vkd8X_54HfiwueUNoY4bxwP4ojvjZqsS3ZG6ABRSAOWh3KUFPb-kn6FkqXRKi4yygSz_7EsDQFzFlUULGItWFY7U_HND2vtw3HZy3HpbPh7BdRYXbt6LS83r_G-VrDWJ0C9M_KTk-RSHvQnh1SGIhttjQ7lxtgp_s2W-c7KUaa8-ZaZq1MaZHgURyyuxh6OwjsZLB6pWJwc0y0cMPFOjki3z34E12u9z82lggTqSMu_zYkka7-MA5KaL4oFpiPDEkB6PKluL7Le4ASz0-VvntzxPqhTLz9o9chyiQ6ZbAXKV39kF81GHDEkULyGMPX0tS3qMTsbVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نفت برای عبرو از ۹۰$ خیز برداشت
@WarRoom</div>
<div class="tg-footer">👁️ 118K · <a href="https://t.me/withyashar/20802" target="_blank">📅 10:28 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20801">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">ترامپ: ما بر اساس سه سناریو با ایران عمل می‌کنیم: اول، نظارت بر وضعیت نامناسب آن؛ دوم، اعمال فشار اقتصادی؛ و سوم، حمله نظامی قاطع. @WarRoom</div>
<div class="tg-footer">👁️ 117K · <a href="https://t.me/withyashar/20801" target="_blank">📅 10:23 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20800">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">‏تام کاتن در برنامه مارک لوین در فاکس‌نیوز: مردم ایران باید آزادی و سرنوشت خود را پس بگیرند ‏سناتور تام کاتن با تأکید بر حمایت آمریکا از نیروهای آزادی‌خواه گفت مردم ایران نخستین و بزرگ‌ترین قربانیان حاکمان رژیم جمهوری اسلامی هستند و شایسته آینده‌ای بسیار بهترند.…</div>
<div class="tg-footer">👁️ 115K · <a href="https://t.me/withyashar/20800" target="_blank">📅 10:21 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20799">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">‏رییس اتاق بازرگانی ایران و چین با تاکید بر لزوم پایان محاصره دریایی بنادر جنوبی ایران گفت : «چه با مذاکره،
چه با خواهش
، چه با تهدید و چه با جنگ باید این محاصره دریایی خاتمه یابد» و افزود: «تبعات محاصره از جنگ هم بیشتر است.»
@WarRoom
🚨</div>
<div class="tg-footer">👁️ 115K · <a href="https://t.me/withyashar/20799" target="_blank">📅 10:16 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20798">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">رویترز: تعداد کشتی‌هایی که از تنگه هرمز عبور می‌کنند، به ۶ فروند در روز دوشنبه کاهش یافته است، در حالی که میانگین این تعداد در ۱۰ روز گذشته حدود ۱۱ فروند بوده است. این کاهش در حالی رخ می‌دهد که امیدها برای دستیابی به توافقی بین واشنگتن و تهران رو به کاهش است.
@WarRoom</div>
<div class="tg-footer">👁️ 117K · <a href="https://t.me/withyashar/20798" target="_blank">📅 10:06 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20797">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">ترامپ: ما بر اساس سه سناریو با ایران عمل می‌کنیم: اول، نظارت بر وضعیت نامناسب آن؛ دوم، اعمال فشار اقتصادی؛ و سوم، حمله نظامی قاطع.
@WarRoom</div>
<div class="tg-footer">👁️ 119K · <a href="https://t.me/withyashar/20797" target="_blank">📅 10:05 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20796">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/78bdb30a06.mp4?token=l8J-vVmmnRB4NcICMZ8vmhfvHE-ShJLQr1O6TdNTIZUz1O72_ofO7Owlk9z_Pqf3aYZjDNc4hGovhLUctYgfCnA_gTVVnLj4va4gJepT0vqBCgPQn8jpPCtnnomecmMjvHZQ9nPeBwgjB3RQGFjzBycZLx5EV8Qe_K-p_ZDcNUtE6EWVbcPLEK0XQKLYZjdUW9buOLGLIcntHyzRttEzyJPSw3zJ9JyPUJJDrggFsuyuP9fkpN5jN5-5nA9hNBCDuOh_-ojasQLUmAcn4EM0ch3dEoEBxTQsFK7Bvn2o-jZWKTm3DZyo6TKyfDZTC1DTbq3nE83d5gZOUrKjjjbRBjLggHFuqkurukihvSH9xBGby0EZ-G9lfdDR9tg9fD43GsnILUQmIv_4FEmjESWz7PcGWnjoUjoTt4XIYTzupSbDIw988nNr4FgTid5oEweglpYF5AKRRVx_plGoEiPQRPBzmjF5sWksLuRfQ5kBKgRfDHDBDYYXVScpSmi4db-pxU2MJtyF2D7X6gmDUD8mkd3Zx3nAnc-89a3xN_vx5UK4dNGeUNFEMbk2L5e97iABURJ15WLSusRlm1bR6LmovE4YTwXFX5iuQ8Gv1Ygl_fzMPdc78N49XxGE5T0YMUfd34OumXUB41P4rC4jjV7vxsMhhYXwz9h0ubeCaNXXqSQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/78bdb30a06.mp4?token=l8J-vVmmnRB4NcICMZ8vmhfvHE-ShJLQr1O6TdNTIZUz1O72_ofO7Owlk9z_Pqf3aYZjDNc4hGovhLUctYgfCnA_gTVVnLj4va4gJepT0vqBCgPQn8jpPCtnnomecmMjvHZQ9nPeBwgjB3RQGFjzBycZLx5EV8Qe_K-p_ZDcNUtE6EWVbcPLEK0XQKLYZjdUW9buOLGLIcntHyzRttEzyJPSw3zJ9JyPUJJDrggFsuyuP9fkpN5jN5-5nA9hNBCDuOh_-ojasQLUmAcn4EM0ch3dEoEBxTQsFK7Bvn2o-jZWKTm3DZyo6TKyfDZTC1DTbq3nE83d5gZOUrKjjjbRBjLggHFuqkurukihvSH9xBGby0EZ-G9lfdDR9tg9fD43GsnILUQmIv_4FEmjESWz7PcGWnjoUjoTt4XIYTzupSbDIw988nNr4FgTid5oEweglpYF5AKRRVx_plGoEiPQRPBzmjF5sWksLuRfQ5kBKgRfDHDBDYYXVScpSmi4db-pxU2MJtyF2D7X6gmDUD8mkd3Zx3nAnc-89a3xN_vx5UK4dNGeUNFEMbk2L5e97iABURJ15WLSusRlm1bR6LmovE4YTwXFX5iuQ8Gv1Ygl_fzMPdc78N49XxGE5T0YMUfd34OumXUB41P4rC4jjV7vxsMhhYXwz9h0ubeCaNXXqSQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">واشنگتن پست:
در پی تهدید به ترور از سوی ایران، دونالد ترامپ هنگام ترک نشست ناتو در آنکارا، ابتدا مقابل دوربین‌ها سوار هواپیمای قدیمی «ایر فورس وان» (بوئینگ ۷۴۷) شد، اما سپس به‌صورت محرمانه به یک فروند هواپیمای ‌کوچکتر
C-32A
منتقل شد. در همین حال،
هواپیمای قدیمی ۷۴۷
به‌عنوان هواپیمای فریب با شناسه «ایر فورس وان» به پرواز ادامه داد و خبرنگاران و حتی برخی کارکنان کاخ سفید تصور می‌کردند ترامپ داخل آن است.
در ویدئویی که از این عملیات منتشر شده، ادعا می‌شود
انتقال ترامپ با استفاده از یک کامیون خدمات فرودگاهی، احتمالاً کامیون حمل پول آرمور(زره ای) ، انجام شده است. این در حالی است که
هواپیمای
ایر فرس وان
جدید ۷۴۷-۸ اهدایی قطر
، هواپیمای رسمی جدید رئیس‌جمهور آمریکا محسوب می‌شود و با آن به آنکارا آماده بود و در این سفر، نخستین مأموریت خارجی را انجام داده بود.
@WarRoom</div>
<div class="tg-footer">👁️ 125K · <a href="https://t.me/withyashar/20796" target="_blank">📅 09:49 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20795">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/At8mqcfyaXEQoe4XsL7JWs5oO4iRqZ1DhLF7W0Y-OLKNIzcf4OILOKM5A3A7jouEJT3Lxr4g5YAfuYIDl65Cahs9emXadYvmk7qJD70wbTg6-BceMW0ODg-yBLrl8WQGBls5kLa0xqEsNQJC1-_J-XAx6w7PuY-7IDOci04ChTJ0eh9MBbpYO2gXfXoEtFHSvFnqqmzQdwK0PWyAAqWRc7G8N0umryfp93gKQ3Mtlia26K7ZXceacLVuQrbhxByRtD2HdlXNdIBGLNYqDHDs3qkzsP_PKZ8KlklkdUh4XZr9lumUsbIFF52tUv4HtV0C-x79v1u9vsn4H5-v9u16uA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ آخر هفته را در زمین گلف خود در بدمنستر سپری کرد؛ در حالی که یک سامانه پدافند هوایی کوتاه‌برد
AN/TWQ-1 Avenger SHORAD
نیز در محل مستقر بود.
(سامانه AN/TWQ-1 Avenger SHORAD:
یک سامانه پدافند هوایی کوتاه‌برد آمریکایی است که روی خودروی هاموی نصب می‌شود و مأموریت آن حفاظت از افراد و تأسیسات در برابر تهدیدات ارتفاع پایین است. این سامانه معمولاً به ۸ موشک دوش‌پرتاب
استینگر (FIM-92 Stinger)
، یک تیربار ۱۲.۷ میلی‌متری و سامانه‌های دید حرارتی و هدف‌گیری مجهز است و برای مقابله با پهپادها، بالگردها، هواپیماهای ارتفاع پایین و برخی موشک‌های کروز به‌کار می‌رود.
@WarRoom</div>
<div class="tg-footer">👁️ 131K · <a href="https://t.me/withyashar/20795" target="_blank">📅 02:56 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20794">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">ادعای وال استریت جورنال : مسئولان ارشد دولت و کاخ سفید به ترامپ توصیه کرده‌اند که تشدید تحریم‌های فعلی و اعمال تحریم‌های جدید علیه ایران، ممکن است موثرترین راه برای وادار کردن این رژیم به تسلیم باشد.
@WarRoom</div>
<div class="tg-footer">👁️ 128K · <a href="https://t.me/withyashar/20794" target="_blank">📅 02:04 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20793">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1faa6dd22c.mp4?token=jk44kg9rh8CUUTM8qvTkI8yJwj9Rzbk-ugzgVP2e7HneRC8fQl5usD0oLxwbNApqKS0b1vZav7qN6tzIkFcGYb0A_K4yP9xe1TJgF7jzn6nInp4s_0pciyTnngolJxmL5CuAmXTpKspINqKWVt-YK_9vyAKlA2AvihyDBqkacM4rswkMTCOFyu_0XIv_Hqm8dLYwSDvua6FHNaJN-sP_2lYIdDUZolq2W-_oQgdSjhDbM9NRvvThD5haieHpv6178Q_iKZYTMe2QTCQk3ISj5yICxLkGbMMZRl_yxczGnoE4nOQModHS1mAQiPj9cqDvy9U5P4m6NXEThVuzDl8_GWtqLaxP4_A5o8eRtYUV_9d1AfrF77Fx8l0ivSQRiaR-GnReJ1cAWULPhg9Bp9UKDiPYU6xYv0xU_INDYhYt9DBhimu2iA94RbwVgO4WuJNlyXSc5ah4Ki1kjTJxh3-zjD4sBUaXLyjcCzuTryMiFrcnTb2IDBRg6Naki3BuN941sPZTKRMwT-96c6EahffuM4Aoxr2YPE7gkYfJ74eT-gcvF-f8s7GYGnKlC57qGtq7mQ18R3XdL8Q8ZVhkP1umJrYlzxE3xpTlVL9StSdRwTZpj8TxKUYeUsq5I-M5uL4pLGXoo6pJVDCcnHHgIJIERHj3dqgoZ0fLCe254FhU5rg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1faa6dd22c.mp4?token=jk44kg9rh8CUUTM8qvTkI8yJwj9Rzbk-ugzgVP2e7HneRC8fQl5usD0oLxwbNApqKS0b1vZav7qN6tzIkFcGYb0A_K4yP9xe1TJgF7jzn6nInp4s_0pciyTnngolJxmL5CuAmXTpKspINqKWVt-YK_9vyAKlA2AvihyDBqkacM4rswkMTCOFyu_0XIv_Hqm8dLYwSDvua6FHNaJN-sP_2lYIdDUZolq2W-_oQgdSjhDbM9NRvvThD5haieHpv6178Q_iKZYTMe2QTCQk3ISj5yICxLkGbMMZRl_yxczGnoE4nOQModHS1mAQiPj9cqDvy9U5P4m6NXEThVuzDl8_GWtqLaxP4_A5o8eRtYUV_9d1AfrF77Fx8l0ivSQRiaR-GnReJ1cAWULPhg9Bp9UKDiPYU6xYv0xU_INDYhYt9DBhimu2iA94RbwVgO4WuJNlyXSc5ah4Ki1kjTJxh3-zjD4sBUaXLyjcCzuTryMiFrcnTb2IDBRg6Naki3BuN941sPZTKRMwT-96c6EahffuM4Aoxr2YPE7gkYfJ74eT-gcvF-f8s7GYGnKlC57qGtq7mQ18R3XdL8Q8ZVhkP1umJrYlzxE3xpTlVL9StSdRwTZpj8TxKUYeUsq5I-M5uL4pLGXoo6pJVDCcnHHgIJIERHj3dqgoZ0fLCe254FhU5rg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏تام کاتن در برنامه مارک لوین در فاکس‌نیوز: مردم ایران باید آزادی و سرنوشت خود را پس بگیرند
‏سناتور تام کاتن با تأکید بر حمایت آمریکا از نیروهای آزادی‌خواه گفت مردم ایران نخستین و بزرگ‌ترین قربانیان حاکمان رژیم جمهوری اسلامی هستند و شایسته آینده‌ای بسیار بهترند. او گفت: «همان‌طور که رونالد ریگان در قرن گذشته در برابر کمونیسم شوروی ایستاد، ما نیز باید همواره در کنار نیروها و دوستان آزادی بایستیم؛ چه دولتی طرفدار آمریکا در برابر شورشی ضدآمریکایی باشد و چه مبارزان آزادی‌خواهی که برای رهایی از دیکتاتوری‌های کمونیستی یا اسلامی تلاش می‌کنند. همان‌طور که پرزیدنت ترامپ اوایل امسال بارها گفت، کمک در راه بود و مردم ایران باید آزادی و سرنوشت خود را دوباره به دست بگیرند. اگر مردم ایران به آینده‌ای بهتر دست یابند، آمریکا امن‌تر و جهان نیز امن‌تر و صلح‌آمیزتر خواهد شد.»
@WarRoom</div>
<div class="tg-footer">👁️ 135K · <a href="https://t.me/withyashar/20793" target="_blank">📅 01:55 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20792">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GbexqznTVRAyKTv2A_FgkZY_vklvJGIkBjTOF3NojWSTxJIcdcyZf9mCU4Im9E2YP6k4u0ZZdna4s_hpY9NMtjiRc1UVyQCdSaaqMIoUdOzU5qMc5526y0yj35UH9AKO4jeyb6gmEGARd4GyfBlTFetfEpfV8442aMUUFRXP175uD1BUPEg5pKtFtPrXv6UQy1qWHElp34s4UF35z4r1MyT-fZdnEHVzAbh0FzVDlGavM_y9uUzt2VOG3p06RZsBFYi4ngytPsUUT1QvfnmYaVnFnvZRjrv2meLVGsn2yiVpw6OuyyHM0aHZuu_HcWsax9usbk2Ymx2QZU6twVRDjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بیش از ۱۵ نفتکش مرتبط با عربستان، که بیشترشان نفتکش‌های بسیار بزرگ و خالی هستند، در حال حرکت به سمت خلیج فارس هستند.
ترامپ همچنین امشب اعلام کرد که تنگه هرمز کاملاً مین‌روبی شده است. باید ببینیم میتوانند عبور کنند.
@WarRoom</div>
<div class="tg-footer">👁️ 133K · <a href="https://t.me/withyashar/20792" target="_blank">📅 01:35 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20791">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">اتاق جنگ با یاشار : کنگره آمریکا در تعطیلات تابستانی قرار گرفت.
سنا از ۸ اوت ۲۰۲۶ تا ۱۴ سپتامبر ۲۰۲۶
عملاً در تعطیلات است و جلسه عادی بعدی آن
۱۴ سپتامبر (۲۳ شهریور)
خواهد بود. مجلس نمایندگان زودتر برمی‌گردد و
۳۱ اوت (۹ شهریور)
رأی‌گیری‌های عادی را از سر می‌گیرد.
حالا اگر آمریکا در این فاصله به ایران حمله کند، تعطیلی کنگره از یک جهت می‌تواند برای دولت ترامپ یک مزیت سیاسی ایجاد کند:
ترامپ همچنان فرمانده کل است و تعطیلی کنگره به‌خودی‌خود مانع دستور حمله نمی‌شود؛ اما نمایندگان و سناتورها برای تصویب قطعنامه، محدود کردن بودجه یا اعمال فشار فوری علیه عملیات نظامی، امکان بسیار کمتری برای اقدام سریع دارند
@WarRoom</div>
<div class="tg-footer">👁️ 138K · <a href="https://t.me/withyashar/20791" target="_blank">📅 00:54 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20790">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">پرتاب موشک/پهپاد از سیریک
🚨
🚨
@WarRoom</div>
<div class="tg-footer">👁️ 137K · <a href="https://t.me/withyashar/20790" target="_blank">📅 00:45 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20789">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">کامنت جدید برای ترامپ (کارای اداری)
آقای رئیس‌جمهور، فن آخر استاد را اجرا کنید
🎯
https://www.instagram.com/reel/Db30SjjS-Wl/?comment_id=18183518170406206</div>
<div class="tg-footer">👁️ 138K · <a href="https://t.me/withyashar/20789" target="_blank">📅 00:26 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20788">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">‏
رسانه‌های سعودی: اسماعیل قاآنی، فرمانده سپاه قدس، به بغداد سفر کرده است.
@WarRoom</div>
<div class="tg-footer">👁️ 140K · <a href="https://t.me/withyashar/20788" target="_blank">📅 23:49 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20787">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">عراقچی در تماس تلفنی با همتای آلمانی خود: تضمین امنیت تنگه هرمز مستلزم توقف اقدامات تهاجمی آمریکا، به ویژه محاصره است.
@WarRoom</div>
<div class="tg-footer">👁️ 138K · <a href="https://t.me/withyashar/20787" target="_blank">📅 23:46 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20786">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">ترامپ: رئیس‌جمهور بعدی بابت کارهایی که من انجام داده‌ام، اعتبار زیادی دریافت خواهد کرد.
لطفاً یادتان باشد که این من بودم، نه آن‌ها.
@WarRoom</div>
<div class="tg-footer">👁️ 138K · <a href="https://t.me/withyashar/20786" target="_blank">📅 23:42 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20785">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">خبرنگار: آیا پاسخی به نتانیاهو دارید؟
ترامپ: من امروز آن را در تروث منتشر کردم. من یک پاسخ دارم، یک پاسخ خوب. بله، رابطه خیلی خوب است.
@WarRoom</div>
<div class="tg-footer">👁️ 138K · <a href="https://t.me/withyashar/20785" target="_blank">📅 23:15 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20784">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6383d52564.mp4?token=nf5C8_fS1CULSicJupmo0sOedfA7k0B33UPPepd2G0DHvDF33gntpdhdqd9p-7X_S11VTyJW8ToJXui-KhZfQJuUhtA2voOnsKKEY9SXLAzXLtpP0Xp9LjincdVXFvNQbhnAvRn8VLM7ElZRZ8Gh9_Oj5K4wbm4SoQmPdXptg5xKaH8aaOk_TKMQvmKa33e1m0N83U2d7-46E0vBZkGjQhGqYbpW2-ZYCsuShZtq4bI47xMhrMqvUHcxWqykzKaADBGJm6UijDcLhbaa3iWnKup06BZotuznw294pOZhKrF8NZVAcI2GgAfVUxhxpzw4dwI6DPeoH6A1x-bFvLsrtA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6383d52564.mp4?token=nf5C8_fS1CULSicJupmo0sOedfA7k0B33UPPepd2G0DHvDF33gntpdhdqd9p-7X_S11VTyJW8ToJXui-KhZfQJuUhtA2voOnsKKEY9SXLAzXLtpP0Xp9LjincdVXFvNQbhnAvRn8VLM7ElZRZ8Gh9_Oj5K4wbm4SoQmPdXptg5xKaH8aaOk_TKMQvmKa33e1m0N83U2d7-46E0vBZkGjQhGqYbpW2-ZYCsuShZtq4bI47xMhrMqvUHcxWqykzKaADBGJm6UijDcLhbaa3iWnKup06BZotuznw294pOZhKrF8NZVAcI2GgAfVUxhxpzw4dwI6DPeoH6A1x-bFvLsrtA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره ایران:
ایرانی‌ها صدها هزار نفر را کشته‌اند.
حالا دارند تاوانش را می‌دهند.
@WarRoom</div>
<div class="tg-footer">👁️ 138K · <a href="https://t.me/withyashar/20784" target="_blank">📅 23:14 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20783">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">ترامپ در مورد ایران:
آنها می‌توانند دردسر درست کنند، اما ورشکسته هستند. آنها پولی ندارند.
ایران کاملاً ورشکسته است. آنها حقوق سربازان خود را پرداخت نمی‌کنند.
تورم آنها 309 درصد است.
@WarRoom</div>
<div class="tg-footer">👁️ 131K · <a href="https://t.me/withyashar/20783" target="_blank">📅 23:13 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20782">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e43e103fdf.mp4?token=I-qgGHw8HOqxzv8laQhqS9YnuN-OYZttU8QTRPrmW7EOeS51MOzliZ2jE7jmrWf9L18-0aysrvkyqzG8T9U0wNlDglIk9KvqxVo0O1LPB_WGXj6NghmCsrHe4eEWW49w1A6Rptj4oJMCVeQrvmxdqAC2syyJaEXrITgmuXmn_J5s5db2fstfM54JpFGuz598O8usQyJUSR1J7GlTT3fm6cnb1fnT8MT8Iv-m4pxRrM-QYo7vVztQ3A_RjtxFgAVOWPqdzdUsmIvyvMMBWdsdJilQge6JHvIRt1x087vKwFM-SIV9FuxIbodiOm9RqPeOX84DGvZVoQcp31DBfed7Hg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e43e103fdf.mp4?token=I-qgGHw8HOqxzv8laQhqS9YnuN-OYZttU8QTRPrmW7EOeS51MOzliZ2jE7jmrWf9L18-0aysrvkyqzG8T9U0wNlDglIk9KvqxVo0O1LPB_WGXj6NghmCsrHe4eEWW49w1A6Rptj4oJMCVeQrvmxdqAC2syyJaEXrITgmuXmn_J5s5db2fstfM54JpFGuz598O8usQyJUSR1J7GlTT3fm6cnb1fnT8MT8Iv-m4pxRrM-QYo7vVztQ3A_RjtxFgAVOWPqdzdUsmIvyvMMBWdsdJilQge6JHvIRt1x087vKwFM-SIV9FuxIbodiOm9RqPeOX84DGvZVoQcp31DBfed7Hg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرنگار: تنگه هرمز کی باز می‌شود؟
ترامپ: الان باز است.
ترامپ در مورد ایران:
همانطور که احتمالاً شنیده‌اید، ما تمام تنگه را مین‌روب کرده‌ایم. شاید نشنیده باشید.
ما ۱۰۰٪ تنگه را کنترل می‌کنیم.
@WarRoom</div>
<div class="tg-footer">👁️ 131K · <a href="https://t.me/withyashar/20782" target="_blank">📅 23:08 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20781">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">ترامپ: اگر قرار باشد خسارتی پرداخت شود، ایران باید آن را بپردازد
ترامپ: تشدید شدید تنش‌ها همچنان یک گزینه است
@WarRoom</div>
<div class="tg-footer">👁️ 126K · <a href="https://t.me/withyashar/20781" target="_blank">📅 23:06 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20780">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">خبرنگار: شما گفتید این آخرین فرصت ایران است. حالا چی؟
ترامپ: خواهید فهمید.
@WarRoom</div>
<div class="tg-footer">👁️ 127K · <a href="https://t.me/withyashar/20780" target="_blank">📅 23:04 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20779">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">ترامپ درباره ایران:
هیچ اتفاق بدی در نتیجه اقداماتی که ما انجام می‌دهیم، رخ نخواهد داد. هیچ اتفاق بدی رخ نخواهد داد.
@WarRoom</div>
<div class="tg-footer">👁️ 128K · <a href="https://t.me/withyashar/20779" target="_blank">📅 23:02 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20778">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bIw1ekjzukl7nS6df8X7sVqItXofeolu1XY93L-fcF3MXEAUMH5T5xrhKhHJ2bkgSPob6zd-xZlw8mddLfhoNpUWU-8KgBvuUd8rgfWeE96_c5I9Sp0SM_xFlMX_NHQpJcG4zG2zLWPODvS_pPyfpPFOrky7I8lETYQ7-6jeC2KKD-C9a5yjNSE3MTCevitC3bvOHVqkqP8qlv14L7dTgblLN_y8QiBGHNlpTTYl_vHGYZc0yl3wcEjXFWqEZkZtEObZEMaqtzSNe6l6dplfAHvfhfj95xtoUFemVtCrgFI1BhGqd-GEQnwSFpV90W4cn-WW0FiJuoiHbKkcOQiakg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در تروث : می‌بینم که نمایندگان جمهوری اسلامی ایران خواستار دریافت غرامت بابت خسارت‌هایی شده‌اند که در جریان درگیری نظامی پنج ماه گذشته به آن‌ها وارد شده است؛ درگیری‌ای که از آن‌جا آغاز شد که آن‌ها نباید به سلاح هسته‌ای دست پیدا کنند. با این حال، چنین…</div>
<div class="tg-footer">👁️ 131K · <a href="https://t.me/withyashar/20778" target="_blank">📅 22:44 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20777">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">پرتاب موشک/پهپاد از سیریک
🚨
🚨
@WarRoom</div>
<div class="tg-footer">👁️ 127K · <a href="https://t.me/withyashar/20777" target="_blank">📅 22:26 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20776">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eJMuBw7Z1lqQ1UHyizvkJCBUPU-3gldOzwb3A-mMNmQEHLD3AIr78zV31gQXlw_hkZ_hCYYVOF2jSSz3VvfQaL7Di5QCCQP5-QZmwDXs9p-zbgv1zNuY68H_tgmDw7cBfDrNo4S6azUdyJWLT5xfxWK-XEkkW7OmMxUBr0_y-eb56KAnEpAdxttGbOq7C5toFVNBhXBIzNV30IoVirM5lChNy8LTBsC42UdY-8cqfoPP57pYb-vuHynmfWGY-zbENbmfORT82Pyf0EQmbFmDxunONgvypREcz7BoW7VKVgBK_lyEBD1pAKvxgbz9js504Qli2hOsQIpXSv7fkbDI1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۷ فروند هواپیمای سوخت‌رسان KC-46A پگاسوس نیروی هوایی آمریکا از پایگاه‌های مبدأ خود در غرب ایالات متحده به پایگاه هوایی مک‌دیل در فلوریدا، در شرق آمریکا، منتقل شده‌اند؛ جابه‌جایی‌ای که می‌تواند نشانه‌ای از آماده‌سازی برای اعزام قریب‌الوقوع شماری از هواپیماهای پرمصرف (احتمالاً بمب‌افکن‌های بی-۵۲) به انگلستان و سپس خاورمیانه باشد.
@WarRoom</div>
<div class="tg-footer">👁️ 131K · <a href="https://t.me/withyashar/20776" target="_blank">📅 22:21 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20775">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">‏کانال ۱۳ اسرائیل گزارش داد که این کشور به آمریکا اعلام کرده به هدف قرار دادن نیروهای حماس که در حمله هفتم اکتبر مشارکت داشتند، ادامه خواهد داد.
@WarRoom</div>
<div class="tg-footer">👁️ 128K · <a href="https://t.me/withyashar/20775" target="_blank">📅 22:06 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20774">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a7c44f7cd8.mp4?token=vsxeRcYmv-aaD3v61uIXm34Nvp145dY6wzw6W4eCaY5aei260Vzqp4I7kd2-nOO4FwJ--Ftlz-zsyn5lwszGPhQnUuoKf9FdaDw7VPOsm3OcM8UVsv2ezn17J1nxEMFuZXtHhNP60RvXzZ0vNU1j689lV4iq0b_Cx-fXxWnFKN4ScxAldiPZKq7dO_K-2MILr33wKgO5Eb8PAY6YPYxCcaBrIGCsorVuuqJmpIHG8eZTVISV2MQFxPsw20OWtNqx4NwBCvLMiDCAAaAr9-UJgikgJONyTMshGL-QdHITfQTRtPDmEvx1i-BCzSp7PmW06wrDrfnU_JhurZLFM3alaQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a7c44f7cd8.mp4?token=vsxeRcYmv-aaD3v61uIXm34Nvp145dY6wzw6W4eCaY5aei260Vzqp4I7kd2-nOO4FwJ--Ftlz-zsyn5lwszGPhQnUuoKf9FdaDw7VPOsm3OcM8UVsv2ezn17J1nxEMFuZXtHhNP60RvXzZ0vNU1j689lV4iq0b_Cx-fXxWnFKN4ScxAldiPZKq7dO_K-2MILr33wKgO5Eb8PAY6YPYxCcaBrIGCsorVuuqJmpIHG8eZTVISV2MQFxPsw20OWtNqx4NwBCvLMiDCAAaAr9-UJgikgJONyTMshGL-QdHITfQTRtPDmEvx1i-BCzSp7PmW06wrDrfnU_JhurZLFM3alaQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فرمانده ستاد کل نیروهای دفاعی اسرائیل در کنار فرمانده سنتکام: "ماموریت ما این است که بر واقعیت تأثیر بگذاریم، نه اینکه تسلیم آن شویم."
@WarRoom</div>
<div class="tg-footer">👁️ 133K · <a href="https://t.me/withyashar/20774" target="_blank">📅 21:25 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20773">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">پرتاب موشک/پهپاد از سیریک
🚨
🚨
@WarRoom</div>
<div class="tg-footer">👁️ 134K · <a href="https://t.me/withyashar/20773" target="_blank">📅 21:19 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20772">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">جان بولتون : کناره‌گیری از رویارویی‌مان با ایران یک اشتباه است. ایالات متحده ضربات سنگینی به ساختار نظامی رژیم ایران وارد کرده و سال‌ها طول خواهد کشید تا آن را بازسازی کنند. صرفاً به این دلیل که نمی‌دانیم اهداف نهایی‌مان چیست، نباید با دادن یک پیروزی سیاسی به این رژیم، برتری بر تنگه هرمز را به آن ها واگذار کنیم.
@WarRoom</div>
<div class="tg-footer">👁️ 135K · <a href="https://t.me/withyashar/20772" target="_blank">📅 20:44 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20771">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/544e884864.mp4?token=ZLNrXwwOQ5m4dhbfEIMnzumzlu48T6XQdnHXgMMAtcsram160WAUckduLQ2xZ7I1J5VQHX1NcTXeNXXbcXQGJiILET3qSDUKFhDJKwdCemLfNs8dM9CH8NuRMEuZ8ysqT2X1sHpcSneq1NE-fGpKLPdO_XVmXWEwdMHppfdNxyys2km-4jI1qv-VBA4l5xSZyzahMyQJoisCdALq9DcHe6-nLbQIJzy2yyhlMx_VhN4aQHeMsJCzt9z584AjnvnJINQ367eoYKj8vnB7iYbLyAiKkht_W96FbkbtjCoS4LX9a26wyPOCyk50fEQphOT2hUFHWpdOpMYZrUj7-2z4Qw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/544e884864.mp4?token=ZLNrXwwOQ5m4dhbfEIMnzumzlu48T6XQdnHXgMMAtcsram160WAUckduLQ2xZ7I1J5VQHX1NcTXeNXXbcXQGJiILET3qSDUKFhDJKwdCemLfNs8dM9CH8NuRMEuZ8ysqT2X1sHpcSneq1NE-fGpKLPdO_XVmXWEwdMHppfdNxyys2km-4jI1qv-VBA4l5xSZyzahMyQJoisCdALq9DcHe6-nLbQIJzy2yyhlMx_VhN4aQHeMsJCzt9z584AjnvnJINQ367eoYKj8vnB7iYbLyAiKkht_W96FbkbtjCoS4LX9a26wyPOCyk50fEQphOT2hUFHWpdOpMYZrUj7-2z4Qw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پایگاه مشترک چارلستون رسماً به پایگاه مشترک لیندسی گراهام تغییر نام داد.
@WarRoom</div>
<div class="tg-footer">👁️ 132K · <a href="https://t.me/withyashar/20771" target="_blank">📅 20:27 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20770">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Nbp4DEJqCnnz266V5PEkzsJxa_ifbtrs7PovlWYjdb-k-2zDFEK1l1o86Kqr3ITXNORchzZt5B-_u5n24geMf6IUolBV6_98tkqMVth6AIJ81RohG8iz4YX6WJCXmW7sPcEExtGS72hqrZUglGMPblNkw3bo5AcgqRdFOpEB9BuButFn7x-evgYmv53eEbLupoJ7ZA_9cL6L-2E4yQkomtxtsm8060tnkftBB7yUakZ2-ZbkYD0JC3v8UZYicKs-KtVFqYjqEw-K50sEMmr3wc7b_xm7MJhz8htJJZkOYZXq2-vO74N4YIas5Qf9U9cnXjmaW6oWyJpF7C53BGiaIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در تروث : می‌بینم که نمایندگان جمهوری اسلامی ایران خواستار دریافت غرامت بابت خسارت‌هایی شده‌اند که در جریان درگیری نظامی پنج ماه گذشته به آن‌ها وارد شده است؛ درگیری‌ای که از آن‌جا آغاز شد که آن‌ها نباید به سلاح هسته‌ای دست پیدا کنند. با این حال، چنین موضوعی هرگز در هیچ‌یک از مذاکرات یا دیدارهای ما مطرح نشده بود! اما این ایده جالبی است، زیرا حالا من نیز از ایران درخواست غرامت می‌کنم؛ بابت تمام افرادی که با بمب‌های کنار جاده‌ای و درگیری‌های متعدد، که به آن‌ها شهرت دارد، کشته یا به‌شدت مجروح کرده است؛ اقداماتی که در ابتدا تحت هدایت ژنرال سلیمانی انجام می‌شد. این شامل خانواده‌های کشته‌شدگان ناوشکن یو‌اس‌اس کول و هزاران نفر دیگر که در نبردها جان باختند نیز می‌شود. افزون بر این، باید به خانواده‌های صدها هزار معترض بی‌گناهی که ایران طی ۵۰ سال گذشته کشته است نیز غرامت پرداخت شود؛ چه برسد به ۵۲ هزار نفری که در پنج ماه گذشته جان خود را از دست داده‌اند. به نمایندگان خود دستور داده‌ام که این موضوع را با قاطعیت در همه مذاکرات آینده مطرح کنند. از توجه شما به این موضوع سپاسگزارم.
@WarRoom</div>
<div class="tg-footer">👁️ 140K · <a href="https://t.me/withyashar/20770" target="_blank">📅 20:08 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20769">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">مرندی ، مشاور تیم مذاکره کننده : جمهوری اسلامی آگاه است که نیروهای دولت ترامپ در خاورمیانه در حال آماده‌سازی برای یک حمله برق‌آسا هستند؛ حمله‌ای که ممکن است با همراهی نیروهای اسرائیلی انجام شود.
@WarRoom</div>
<div class="tg-footer">👁️ 135K · <a href="https://t.me/withyashar/20769" target="_blank">📅 19:48 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20768">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">با حکم مجتبی خامنه ‌إی آی، علی عبداللهی فرمانده ستاد کل، احمد وحیدی به سرلشکری فرمانده کل سپاه، کیومرث حیدری جانشین رئیس ستاد کل، ایزدی جانشین فرماندهی سپاه، عظمایی فرمانده نیرو دریایی سپاه و طائب رئیس بسیج شد
@WarRoom</div>
<div class="tg-footer">👁️ 142K · <a href="https://t.me/withyashar/20768" target="_blank">📅 19:33 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20767">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o9w7IT5vDDg2wbYqdlAVKfqYUDJ2K5b96lyp1fTCjjDz9aSBBK9XtSXohzA8kYFcMGqulCYBWB8184nyFrHnxeSTnYAhZOyXkuW_PKLvLMJDwH0DD4PWjXxqYVI7XmcZQ1w3_SSKcm8xCZ4i5TBFQ4grjmw_qdqnnzwfxaswZlZylm6nG8LqhslkqYbw1S9MiaerKbChnxlMqE8OCRZuRhsDmUsAc-aYmre4SwHlp1DVwkB-GyM6O-tEGXKtbb6fQ0k1HQ3Nq158PI8nGD24gJYFoE1jCbGODZp5mhgzmKP2t_j5Sig8w2X-yHA9PmL0laFqk25QXZlCKQK7YYsZPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اتاق جنگ با یاشار : جمهوری اسلامی متوجه شده که با بالا نگهداشتن قیمت نفت، حمله قریب الوقوع آمریکا را به تأخیر میاندازد. امشب، ساعتی قبل از باز شدن مارکت، این حمله ها را انجام داد و هم اکنون با باز شدن مارکت، نفت در لحظه نگارش این متنالان حدود سه دلار گران…</div>
<div class="tg-footer">👁️ 143K · <a href="https://t.me/withyashar/20767" target="_blank">📅 19:23 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20766">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E_MJmZc3F_xFFix0sgcR2RbPRM71ot6n5RYCZdQ_Z4Zd8000SsOSv8XsacL2OkonzMtqj1o1XWT939aUSQlnKiRH2QzL2jqp-2Trg4o1GTYmzRJUDM1JMRizsRAKH-X_FXQdE2ZDL6BtnTLtR3i-0_p-WgLDVLy4i7uzPkm9IcSPwH4eHtRTFNi3dMztqLO6hxD_udciER77LQsFNtqq6YqzvOplKkI69KwU_PxBLrak4DWn8C5GnIWHeeo3M77i8_AWwQx0hPa4nhWLQ0dnNFoZ2NqfJ3mnL_1lwvc3dEr2PHMk_BGXiSG-LD7fsY37CpFEZtr4HzsZhHhAugKWRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کانال ۱۴ : عاملان کشتار جمعی اکنون کنترل ساختار نظامی و امنیتی ایران را در دست دارند.
ایران به‌تازگی قدرت را به‌طور کامل در اختیار دو فرد تحت تعقیب اینترپل قرار داده است. محسن رضایی اکنون با اختیاراتی هم‌تراز با رئیس‌جمهور، ریاست شورای عالی امنیت ملی را بر عهده دارد و احمد وحیدی نیز با اختیاراتی در سطح رهبر جمهوری اسلامی، فرماندهی سپاه پاسداران را در دست گرفته است. هر دوی آن‌ها به دلیل نقش ادعایی در طراحی و سازماندهی بمب‌گذاری سال ۱۹۹۴ مرکز یهودیان آمیا در آرژانتین، تحت اعلان قرمز اینترپل قرار دارند
@WarRoom</div>
<div class="tg-footer">👁️ 151K · <a href="https://t.me/withyashar/20766" target="_blank">📅 15:14 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20765">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">وای نت : ‎نتانیاهو قصد دارد انتخابات 27 اکتبر کنست اسرائیل را تحت تأثیر حمله جدید به ایران قرار دهد تا ائتلاف لیکود متلاشی نشود
گزارش ynet می‌گوید نتانیاهو در شرایطی قرار گرفته که
تهدید ایران و بقای سیاسی شخصی‌اش عملاً به هم گره خورده‌اند
؛ زیرا اگر بدون یک دستاورد بزرگ وارد انتخابات شود، فرسایش قدرت نظامی و نبود موفقیت سیاسی می‌تواند برای اردوگاه او هزینه انتخاباتی سنگینی داشته باشد
@WarRoom</div>
<div class="tg-footer">👁️ 152K · <a href="https://t.me/withyashar/20765" target="_blank">📅 12:38 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20764">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QfRLiszATFm_BMvN10bmtZo_VUz0rQU6Cf0QpwNBWqp9FY2HFHKWm6BNJ8YtjbPhoec29wq5giLqAcKKW7bNqfLC-dnNVED_ls8Q0_lJPSfmdO58wDzh_rp0ZfGxhwpqmONJ_1vkxtF0UBdhl_LQiQWCjmVHRnG0xq5Xr8SH7H_v4K2ODMNd7iG7W9fDmXhIMoF0AXtQBzk-kozFVePyFvYs4aLOW2c8GbWwzoY4Fm6konwmXCpGDa-eo9tOd0vrWDaNm3VnFO9a4dj8rHrwrKGTq0CAnnuWF0FdGKsiCjsKptEk_cT88bZIYBSt7sQlHwBb0tvRXsDIGUL2vG1KtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حضور محمود بوتاکس در جلسه دیروز مجمع تشخیص مصلحت نظام
@WarRoom</div>
<div class="tg-footer">👁️ 155K · <a href="https://t.me/withyashar/20764" target="_blank">📅 12:24 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20763">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">مقام ارشد به کانال 14 اسرائیل: بزرگترین ترس دشمنان ما این است که نتانیاهو در قدرت باقی بماند.
خب،این به چه معناست؟
نتیجه بگیرید.
@WarRoom</div>
<div class="tg-footer">👁️ 150K · <a href="https://t.me/withyashar/20763" target="_blank">📅 11:18 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20762">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">مجید شاکری ،مشاور قالیباف :  ترامپ با ما توافق نخواهد کرد.
@WarRoom</div>
<div class="tg-footer">👁️ 148K · <a href="https://t.me/withyashar/20762" target="_blank">📅 11:10 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20761">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">باراک راوید ، آکسیوس : یک مقام ارشد آمریکایی به من گفت که کاخ سفید از اظهارات نتانیاهو درباره طرح غزه «نگران یا ناراحت نیست» و آن را بخشی از فضای رقابت‌های انتخاباتی در اسرائیل می‌داند.
این مقام آمریکایی گفت: ما نیازهای سیاسی بیبی را درک می‌کنیم
@WarRoom</div>
<div class="tg-footer">👁️ 149K · <a href="https://t.me/withyashar/20761" target="_blank">📅 10:39 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20760">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tbe5WKlbEkxDQfpFUMkgsv8eQJq3a-V_bXfiy72P4ZtWGqE3TwF5Scm5jQbhGLXceryRPl0aomktruHDjQI7byzCrrk-3XyMP4T6E0ASyd76ukpqxdULpGVmt5LN9nlqdehql3crHB4ygKvzDT_8ffJZEU0IN_tdR2WgChCGEnnMztoHPBWBu4a2kOcNHF40QGB5xZWdXBEXI1ARc2O9ypajO6s6OvNLCqoziD_xyhwbSihn4gO9_wT4no76T03ptDNsCPhu2i12L0UlhSxrPSOfCyGnf3h7cX_tuUSRLTxrsCTxmwt9Th8xdu0SOtlgozIEjlPyazcKpVrrP19eDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چیز نیست، بی بی داره خنثی سازی و بازکردن ورودی های تونل ها رو براشون انجام میده.
@WarRoom</div>
<div class="tg-footer">👁️ 149K · <a href="https://t.me/withyashar/20760" target="_blank">📅 10:14 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20759">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAlireza</strong></div>
<div class="tg-text">مهم نیست داش یاشار مهمات عمل نکرده دوران هخامنشیان هست</div>
<div class="tg-footer">👁️ 140K · <a href="https://t.me/withyashar/20759" target="_blank">📅 09:53 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20758">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pG1hBv_IA9Rx_zldLfXYLCTCPVBtDZeWAyUe08UZsFs0sixhMdY_jWRKeVwoICyqoQdf_GDRGRJDuZcYFdQZcrMyrAcK80Zf0yLDBSYBdjo26yarzkkWDAafP0tMgWQRp8FIuaEBLjVAuzV96O-1JaU_HVsLa-UsU-w_Ph-0n1rsvmAJ5uy7pP4nQsbn30QHDWvUCG3B7jnLRZ0YDSGSeNNtI-CCbBp7bIiTZsyac0gbVbGr1zIDO2sHOdGNVz9Lc_Q-_bh69Ci-pfpMw-nUvnKZF77AiplP8QGW3Qfm5MzXC-QCkAgL_vcNBnWKJPRTvyH0y1Gbxr5vxoDgqkW5ZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اصفهان سمت پادگان ۱۵ خرداد انفجار جدید
@WarRoom</div>
<div class="tg-footer">👁️ 146K · <a href="https://t.me/withyashar/20758" target="_blank">📅 09:49 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20757">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jJ9Yb9bUddRZeY6cqJpQh4dL46Y6KRB7sD8mZmYWlqJUHCTXCTdF6cCAiJH9fKqQO9_AKxCDrh0ixSME2KNLVvLTjzmXHa_EI-3TRD-Fdgpi1wU7c2663HFJBnROGhgW4R3QTxGVeacR8tpEv7_hdlOEPLt9Tie58VeTSL7aHCJd3jJsdDJ5UCwEEB1oQ8F-H_6hsefg4hHuvJn5KUQsi-jpzPzyly9qeR3hDHUiqbvoFlspzf38-od81YxfqOkyhIHu2WFb0svhHkB4lFE8FuXho7eJmqzgLptm6s93dyKCehKQqFktTO3DTAvFY1IS_ZDDCgeHuWMCQtWWe7N7eQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دو انفجار شدید در اصفهان
@WarRoom</div>
<div class="tg-footer">👁️ 149K · <a href="https://t.me/withyashar/20757" target="_blank">📅 09:42 · 19 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
