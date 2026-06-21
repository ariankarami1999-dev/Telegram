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
<img src="https://cdn4.telesco.pe/file/O1ufRcbpQuYmcEa_PWk8cWFAOxOdfa-dHNLw0QOpTEz4L00tD9Sy-ssiK_KdfWVQ5PzVQH8AUO8nM-umZ5h1Qdgrukb9a2Tb5gJnGMtZftCqRhnDQ4g8b1MeUJwI7OGuHnk4bM7dRPgcjZCxIQjo1PIQFuLj9fJxs7cYRFGzR_3iMW3Ng3oea7bPVYI24lzsKEeEJSNoUj5JZ3Lb4oHDMtJIr2ijSNp85Puu_nqL2lBQ3kUbSwHGK44UBDMH8SLiiku1oBFkXmnPNNiZq8zLeYZjF117xWQMiTmZ87YLTpG4FYjGj7ZjK3VpCfAsl0jTWtXt_-WJYeSJt2UlshduJA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 309K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@ads_Persianaaپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-31 10:56:56</div>
<hr>

<div class="tg-post" id="msg-23963">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eH2evKFOr7ZBP3hw4hiPFK2qLj-1IfqUOYj_PXATFhVi7Sru8CpQ1d5uO5vPGsVgDSJqN9Onha3f9DWOTHanjFJTR222wwPVq16mY82Frt6qRDgDCuvC00mZBKREcIiOuAZDRIudDnjyfPKZf1h1cFobXBnZpa81adbfxLEMj7nswHbiRb4KYikGskQ8G1U0-x-6stU0E3iu0YA_MOm91QWU-RJ0wYlNBMrOFD0Jd9U58F4ihnWN_4ikkNkC0YDquCPABAwNYirPo1q_Kqvtj0O-YFU3DmDF4voAFcpySZ9PRxkJo5m93OZdhx1Zzb87yfeWq3Xjt7ci28rhLH15gw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
طبق‌شنیده‌های‌رسانه‌پرشیانا؛باشگاه استقلال امروز با وکیل‌ایتالیایی‌خود تماس گرفته که این وکیل به باشگاه اعلام‌کرده‌است که نهایتا تا پایان هفته اینده فیفا پنجره نقل و انتقالاتی آبی‌ها رو باز خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 5.15K · <a href="https://t.me/persiana_Soccer/23963" target="_blank">📅 10:44 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23962">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/caZWsBnquqJn_FUz7etX4ekibKsWeDSGxUIbE6i8IBzIYobUUfLLLBIxBKC8h3x6k65CImhafh5aJhxV86ttu2z1N70hZP48UTC0AC60SGYeN-a9-u9bg8vVlDlfEXufYrT5IWJvt1YHZIVPoHtRUm_QPdNB5YnlmkkCBS5aO39W7CCxXWJD2m6JR2hmLnKfizycMiGZfexWw1Wixwa1n64fzfwvN_7YNS2wOtX6ztOaWF44q-9xzqSvkAquzT8B370OnyxnjWi-F4S22y-mX63Lb_NMlESDNbZqNLsuFW_Cz8fve9zXMQ_nPxwAq0mE9wn6G_y9-Ug7N5ofb_rZ8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
پرچم‌باشگاه استقلال تهران درحاشیه بازی امشب دو تیم آلمان
🆚
ساحل عاج در جام جهانی 2026
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 7.28K · <a href="https://t.me/persiana_Soccer/23962" target="_blank">📅 10:37 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23961">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r8CEwgFv1ZFp0ZvJ2ahEFuSfLeJLX-OSBC8GpFZUevp1dCs_lSYT62YFbG0RgQDx5Dyy-kP1l1H2r-c6ztKKHG0FsSoZklv0lvpSytK2OwLwV-WskA1A7bcFXzCAS33GTvPMnsmJhVjPQdXraiTVkZL1blPyiTsYVKn--_m1UnXpT6RX1yqLm7-HYwD9Nfj6C0YvTAtdb8WcdAA1oURROjXy-D6xqvF6uBSgKrq5WDp_Grjlnu5dqG3Rq9rOM5Q5Z4Myclc-h8tGK_DVPCHrLK7Bgwh-y8Ae86YnPuIFBujpGN5sihiwwuQ9gbI2g0IKExcDK-TVDRCzh_uJwmoV5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
آمار پیروزی تیم‌های‌ملی‌آسیایی درادوار مختلف رقابت های جام جهانی؛ کره جنوبی فعلا در صدر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/persiana_Soccer/23961" target="_blank">📅 10:19 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23959">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/550fbf8a8f.mp4?token=lHXTQUm_1KN7jPMrm9-Jh0HhC7jBrce8hc5aB4B8YOHbnUok6QQniohiCkvIj73mZ-7lBQxKEDF2lv0JtU1aqwbNM9DPJfCAehf0Fl-lATQ0JTGfFB3FIRgfi-8BcBEMnNhvN-zZXl53JBl9jTph8mBfbK8aDu---nPA4LTzIpNqVVsDdjMB3xXEXqAOS9CJ-vKi-V6bpIfP3QeZJQ9dGYQCACUb_T60tXBGHfYh0FMV9wXY-REYwA4UOTgY_LZ9o8PbMaVhlzHeU0TJxldhF-nuC730bli-U9xRmglFT69XiAhdrg47LlRQo9F8I_ecSyZngigXGdfWiU9zRYq5Pw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/550fbf8a8f.mp4?token=lHXTQUm_1KN7jPMrm9-Jh0HhC7jBrce8hc5aB4B8YOHbnUok6QQniohiCkvIj73mZ-7lBQxKEDF2lv0JtU1aqwbNM9DPJfCAehf0Fl-lATQ0JTGfFB3FIRgfi-8BcBEMnNhvN-zZXl53JBl9jTph8mBfbK8aDu---nPA4LTzIpNqVVsDdjMB3xXEXqAOS9CJ-vKi-V6bpIfP3QeZJQ9dGYQCACUb_T60tXBGHfYh0FMV9wXY-REYwA4UOTgY_LZ9o8PbMaVhlzHeU0TJxldhF-nuC730bli-U9xRmglFT69XiAhdrg47LlRQo9F8I_ecSyZngigXGdfWiU9zRYq5Pw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
سرهنگ علیفر:
از اونجااصلا نمیشه گل‌زد؛ واکنش صادقانه آیاسه یوئدا بازیکن ژاپن به علیفر
😂
😂
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/persiana_Soccer/23959" target="_blank">📅 10:02 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23957">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BSoNIK1tD9Mk3Xf4EuYPcXDALo4J2q_p0BpoplJ2uR9uJHu5QoTHl-A6DFeLupW638wAMxbkndKeyoBMQXKeGVar1y4fZgO3V-evo-azMyNbgV0JjECHGDafA0beGQtI7JLe9SAQwTzvWdP_Y3JyzIX2h4rxnw47QbV7wuRlpMRaHgFGeGVMCblB7uqn836cFWW6pHSTUvigiB72Hrs6DefL6UpHObJEHJbGSUMNpk_24S2c3iHBDqsBT_nFTR9Zu_RsCDstUGXBloibs56hyKDnyr2gKMwSaXF3ryCx1SSC_lAG7O7c7JyN46rKGc2hgTWcHvwHxjO_-Q4ulavyiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/f2roYN7wN957X6ZfdcfQ7cMl6tLRHsnHvU-15DybnLY2RkeEc0AVR1wjyOiCrBxV_uS4N82TLJoNQl6am96HIeW7n851KmuIRj-iutsGi96wNUrVjF699f5rSY9H7vAcWZT4PO57svSme1HrpH8wqxtP5qPeE0ztJMpFbLxe_Pk_1uD-8oHfW0NQxw8b8N3CI1SBt60MhMn2xnDQ6irIFm1qFopF9vCYWZ9xxNqa8QT9lOHUZ0H0amat6bs4gg-4H9_SgPHM-yDB1tVzYFcxWIfWXsm5LKM7TrOHF9xmvCpa0kOFgP68QCaisp3Qugth-Vkf-c3SECc4MK8zDpYIwA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
برنامه‌دیدارهای‌امروز؛ از جدال ماتادورها مقابل عربستان تا مصاف بلژیک با شاگردان امیر قلعه‌نویی
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/persiana_Soccer/23957" target="_blank">📅 09:52 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23956">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q1ZDqF6BZUFmtP0N0-IfpndXIpzFCOMveKf1K-UuJALqyWW6ovcJKvsIOEEY00m2-L9omwcp0XZ52-yObxm2FZ23Hy6Km4hS7O3ta35FO7fbIF4c5hG1j2_6rsT1DpZv5ifOwTBQvfpXiC-JVezi26TabXF1zLUzkvP5qbVC9xG2iM8iEHyZePAQ-f4L_sJT8tYyWqNmhye7DaCnkSemOB_6tKiZST_TBmMy0VGXoDzG-9A4xwNLThw2zRNbHJdp2EyppeqMsn2WYaWXWSE2o412OCAqzlVzho_IyhAXwmjV7Pmkb1HlEBr3N_qVQtMIWOSYCGzm6mM2VCubqZAFhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇪
رودی گارسیا سرمربی‌تیم‌بلژیک:
مهدی طارمی، سامان قدوس و رامین رضاییان بهترین بازیکنان تیم ایرانند. رضاییان اگه 25 سالش میبود الان در یکی از بهترین‌های تیم‌های اروپایی میتونست بازی کنه‌‌. چند تااز بازی‌های او رو دیدم فوق العاده بازی میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/persiana_Soccer/23956" target="_blank">📅 09:01 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23955">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EOljrrBvmZTpmkwhG3iczplb_cuXFmIvr18YS4dTCHD_9kh7yCAVmOwU8GzWxQQtaVwzJM0OAoC7FEUHVMP5ZQfsKwNMW-i8DyLqQvfY2p7tUZBrISP9lRnFtEZ86qJbEFDleB2G005pbZVF9XlrgHyhDF0zjbHfkqg71w5bHYxsFvnAP6aC4r69hwegyfATWjWB4lma0M577VN6DPxuzi18yZcf9b2Pi4F1V90Sy3b4oa_8UvXA27iKJNl5MX5dRBFkD0R6a0N_udMtjLkxbtIE9ChcRJhmBLMdmuy_aN3RaMiFN9UBRFcxJqwTz2EYV5FvpUKMmGjGE4L9q_vtfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته دوم جام جهانی 2026؛ یه پسر کُرد سه امتیاز ارزشمند روتقدیم ژرمن‌هاکرد؛ کامبک  دیدنی شاگردان‌ناگلزمن‌درشب‌درخشش‌دنیز اونداف ستاره کُرد زبان آلمانی‌ها در فاصله تنها 20 دقیقه.
🇮🇪
ساحل عاج
1️⃣
-
2️⃣
آلمان
🇩🇪
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/persiana_Soccer/23955" target="_blank">📅 02:56 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23954">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TkNigWgx5bUzDNT58cOpJcFBHlDV_8c2gLTFYw6V3D6QcZff6inbLPyagNAIzwo1ZDAjo2QthxHNvLMKBgfeQVE3MxUN7X-H556XRbnQ3yAZB0VHKbAAa16qAAMOD8UIMCMhqdDI5kA4ZkCNyVcHwrs21VOHEGgGpSkmZ7wVer05lToWloo3T7rQRCkHCUyZnH2dbMeScWkfTd5w338kUlLyBjgstjCYh0rrSvQS0wfJVTm4XG1QYo6tx-wFEVr7eG1qDdC7011q2WsCNP4QUhHPYMzPq7dUi0fNgxNqoh6qznW6ov2K8FIUmhqN1pH7Zf8WjvbD55GPj3OlT8GUIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇩🇪
دنیز اونداف ستاره اشتوتگارت همیشه در شادی های بعدگل خود کُردی رقصیده تا اصالت زیبای خود راهمیشه به همگان نشان بدهد. امشبم کلا 30 دیقه بازی کرد دو گل زد و نمره خارق العاده 8.7 گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.5K · <a href="https://t.me/persiana_Soccer/23954" target="_blank">📅 02:35 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23953">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XcsVHwqXOGw6_nmq-KVVJsO_-aOrK44jW-x5LpRh1L9zUUWw6ZRMuQNd_kekWcaiyyFGwy0t__KrpHu-kxsyM7Uvky1yrUmB9hIDVWchKNaqLogtY3bpQPoz3flHNOsvWvdsXu3YcduFAr_bsvODHqO0XXkOdftG6BNaF0Zt1yOOeT26jJRi-tXmowLxd8J2zAzbb6pNHiEEWPjoPK49jIJUG6aT1FU9bnCPUK-87fXDmGezU-bUQ5Qp5TSB0IzlRwdfSqhgpvgcngreMxgAjCmP7tlX18xZWihi2pZWyR8Irx0uoskSSRitEA5pxrAJiOHpduv-YqiYA2Cebr448Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌دیدارهای‌امروز؛
از جدال ماتادورها مقابل عربستان تا مصاف بلژیک با شاگردان امیر قلعه‌نویی
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/persiana_Soccer/23953" target="_blank">📅 02:05 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23952">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MtJeI3XgFGnU1OilhRUQ4bvjnfTADbz_lGyZqTElJ9RZ7AjyoHGb3J80sn4pdPSP9aS5blYUPMA5hTAhZ38V87fqQcPKfpbFX743ISU36GN5AzW3MEutNeDB2tY0VQXT_6E95dWVUVKz8qDGCnIEQdR3PqC2VmT6Ub_aW_LoAOb03bn981qF_fSM01ToU-LRlhHPBiKW2MAWllqsZt1fEjwCk7V_ryHTFo2uFSFKTG5AuWY7i966FPH5sAiMYNpyqItFnaWBOfN1JJ5Ipkt4tG_jPYzr1DJ76uImugCi_QH-s7wovw9EQImypHwdKjNc3UcisgRsfajUR9GLYw3YxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌‌‌دیدارهای‌‌‌‌دیروز؛
ازبرتری‌برزیل و هلند مقابل رقبا تا راهیابی مانشافت به دور حذفی جام جهانی
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.4K · <a href="https://t.me/persiana_Soccer/23952" target="_blank">📅 02:05 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23951">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2bf800e040.mp4?token=IS_Zse6flpGQ9Q141qiix92L2jHbLX_dpU1xM5Use6tekal_lDW8NAfwk1QgV4ODbPyB1mCNryed97VyaBMppSS_5AVWzVDg_X5W9VDF6eRM7VSOF_M4VD3i9Jp3kBPPJgQKR4isLCqY-cHqihQoCtmTdefs9TI1Jorm-GB9YwCoWg897TtICNDf34xIxcL8aAADEsCmA1UPG0Yu6sWwZmj1xoTN_bH5XiGumOydt-VWqwrdnmEu0_rb8hmKv4YPa_ZPcTkdSJ4gUqAi-ZVZ1KrRNmK1MaaPnGrGlf9MDGepxBzkI-X35q5qbRwbXeJ3AOVgm4y0J1jk5MvHkCc9bg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2bf800e040.mp4?token=IS_Zse6flpGQ9Q141qiix92L2jHbLX_dpU1xM5Use6tekal_lDW8NAfwk1QgV4ODbPyB1mCNryed97VyaBMppSS_5AVWzVDg_X5W9VDF6eRM7VSOF_M4VD3i9Jp3kBPPJgQKR4isLCqY-cHqihQoCtmTdefs9TI1Jorm-GB9YwCoWg897TtICNDf34xIxcL8aAADEsCmA1UPG0Yu6sWwZmj1xoTN_bH5XiGumOydt-VWqwrdnmEu0_rb8hmKv4YPa_ZPcTkdSJ4gUqAi-ZVZ1KrRNmK1MaaPnGrGlf9MDGepxBzkI-X35q5qbRwbXeJ3AOVgm4y0J1jk5MvHkCc9bg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇩🇪
دنیز اونداف ستاره اشتوتگارت همیشه در شادی های بعدگل خود کُردی رقصیده تا اصالت زیبای خود راهمیشه به همگان نشان بدهد. امشبم کلا 30 دیقه بازی کرد دو گل زد و نمره خارق العاده 8.7 گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.4K · <a href="https://t.me/persiana_Soccer/23951" target="_blank">📅 01:55 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23950">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LqQx38eEbbhB9sBtuLIj16CKpzmZs62LEAN65wLG6GJdhtb4y0G4LEKHeQ_kvVkqn2dU33F7XA85iywL-2RC7nzfCFont0zedx0END8zcCXaqpOhL2KohsBNOGm_0MGRxOH8jWkLXUmwYgwGRJmNJhnd5IwPh_IaOy66vG0BRsTy4HnQS6rTcTUgeo4aLkT9-ECGzE_Se1YDl8uZvXHZGkzRLGd_5DK1g8ixE3ez8yJe5X00BAuWaHDmR3IzPyR1icll6_ICA4z31-oHA7rKbjBREa3rhtZer7iGnhCipko9_qnHUtmtPHSMLlYXi2gLRd2LNwAq2K2Wu0VFuBTgEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
باشگاه‌ گل‌گهر به مدیران استقلال اعلام کرده با دریافت20میلیاردتومان‌رضایت‌نامه پوریا شهر آبادی مهاجم جوان این تیم رو آبی‌ها صادر خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/persiana_Soccer/23950" target="_blank">📅 01:55 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23949">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YSWTzWZb7A7hRD5BVdiUYMPad1_jSG-URzQJh59bhpk_d08dUA4gzID_GoCjQAdH_v6YtoUFh8ece0h3eYBteMikyS2CQsN2zP6FrqS3FOjWtfxzgSVu7MMaIKccUoSsVpK_QMBGp2umWCjArXEb13tRoV7lKKHrtx_A4BZoR5dJmdtCwdDioHgAIOSklD4GWmEjraFFIt1eG-wYY1S61oyaGRccA6TFz1EaQJtqbpLpP1gGECcMAgAuOD_G4KXr2U6MdcmRM34zBWa86EbrXd-OuI_zGt0PVzTZ3iwmFPayDBINvipBbAJwom7F-HwLfB_zmC2TbPCD6pOG-xWB2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📣
آیسان اسلامی به تلگرام پیوست.
⭐
اگر توم از طرفدارا ایسان اسلامی هستی بیا توی کانال تلگرامش فعالیتش شرو کرده کنارش باش
🙂
ادرس عضویت کانالش
👇
e30
👇
https://t.me/+QMjHLL65ocsxYzRk
https://t.me/+QMjHLL65ocsxYzRk</div>
<div class="tg-footer">👁️ 32.2K · <a href="https://t.me/persiana_Soccer/23949" target="_blank">📅 01:55 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23948">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/40b51e8a93.mp4?token=CWbHytZg529X5lz7t1e0y3y3IcaOLAEisNzhCn7PYgo3jQPQWRVM7tuRyc76eyVjESrkBQDmXi9Ztk56JmNq8OoNHEh8TRIyTXf-eN43ay1C3iFNa2GDTjO4tBCTS8jdq-PUT5y9nAgrgWe5CIW-sRPpndHNHSTXnrqLMVp2No2MZ8q7iqs3CYO6zIj_fVZlNz8363MMf7JfiNYHfcVvLmNxKW2HC7Ef1gTxWnyQvTgfuYh4ECjx0IRNOy4AQmgwIjRut2HzyJCg65MCYFr-Di9p2E4T4QAtYJrqCM88SCgVyuyxMKSq4ARbOcl7uChLdmboqRPhJPPuiVtV4bHK5THLnn31TLhxr4zCNH_hnJyEBXLPVsK8szZPBkb961hD6v2oNaEQCQtcAZSvbKKXi0cvMYvlZkdyT9C9uh7q_5fJIvThG8C7cznacPT7G-KcYL48HrETSGI1USN4QWZ7jX7h3eRPNp-qXmIcuSFLrIGAwaem_c8riKGov6azHtWQ2d5WNSwWejB2Y6iUNt0vrqYaeX14XMyXPXPicM3fHtSB57GN07K7HQTDAZ5vt56augeTNrcY0-4LbHtVjC2XX9aypV37CE2_PPKdjZM_0VitevC0ktURFg_0g1BbbyuNwQP3yRsCI1ASKbDkj7QV20G-FQSMbSWKfYvTzifVUOs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/40b51e8a93.mp4?token=CWbHytZg529X5lz7t1e0y3y3IcaOLAEisNzhCn7PYgo3jQPQWRVM7tuRyc76eyVjESrkBQDmXi9Ztk56JmNq8OoNHEh8TRIyTXf-eN43ay1C3iFNa2GDTjO4tBCTS8jdq-PUT5y9nAgrgWe5CIW-sRPpndHNHSTXnrqLMVp2No2MZ8q7iqs3CYO6zIj_fVZlNz8363MMf7JfiNYHfcVvLmNxKW2HC7Ef1gTxWnyQvTgfuYh4ECjx0IRNOy4AQmgwIjRut2HzyJCg65MCYFr-Di9p2E4T4QAtYJrqCM88SCgVyuyxMKSq4ARbOcl7uChLdmboqRPhJPPuiVtV4bHK5THLnn31TLhxr4zCNH_hnJyEBXLPVsK8szZPBkb961hD6v2oNaEQCQtcAZSvbKKXi0cvMYvlZkdyT9C9uh7q_5fJIvThG8C7cznacPT7G-KcYL48HrETSGI1USN4QWZ7jX7h3eRPNp-qXmIcuSFLrIGAwaem_c8riKGov6azHtWQ2d5WNSwWejB2Y6iUNt0vrqYaeX14XMyXPXPicM3fHtSB57GN07K7HQTDAZ5vt56augeTNrcY0-4LbHtVjC2XX9aypV37CE2_PPKdjZM_0VitevC0ktURFg_0g1BbbyuNwQP3yRsCI1ASKbDkj7QV20G-FQSMbSWKfYvTzifVUOs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
هفته دوم جام جهانی 2026؛ یه پسر کُرد سه امتیاز ارزشمند روتقدیم ژرمن‌هاکرد؛ کامبک  دیدنی شاگردان‌ناگلزمن‌درشب‌درخشش‌دنیز اونداف ستاره کُرد زبان آلمانی‌ها در فاصله تنها 20 دقیقه.
🇮🇪
ساحل عاج
1️⃣
-
2️⃣
آلمان
🇩🇪
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/persiana_Soccer/23948" target="_blank">📅 01:36 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23947">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jf-S3-5CiQzS1KpT4TcxBUAnDK2-3SXB78-vzCR6xVEfWQ8ahBmm5fJoWXZPXn7yI9f1bprMsGgHl65Zmu4RlXAqYuEuiMljlmQogH4dq1nd0QY-H3YMItDqzrXALH4wptLRJbUg1IwSRPBTVxSJWV7jztz62j27wZrwpEJeHwbSnd3d6HBNdPn_vfNa43ydza5FXMBC7ZKV0wUejQPbg46mvtNaQMU-vjsAMEEvTSWZUXH0XOjzpNFU45n77WhmXFKCNkHpcmWnSSTbZZ9TPpvujTu2_ZEhxIig3z6KBMD7gVO7KvoioHK7zwLQsaME5gMIaGQ6U9UQTVTrnb_SsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇩🇪
گل امشب تیم آلمان به ساحل عاج: ندیم امیری بازیکن اصالتا افغان پاس‌گل داد. دنیز اونداف بازیکن اصالتا کُردگل‌زد. اونداف در دقیقه 60 به زمین اومد و8دیقه بعدش گل مساوی رو به ساحل‌عاجی‌ ها زد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.3K · <a href="https://t.me/persiana_Soccer/23947" target="_blank">📅 01:31 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23946">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mJ1qbZvrJps4z8f-2iieSzmk8KB6jAi5eh_kuScrPGpIqWj4T40EjWrTYyMT0De0bHn5M3pjnTkVxxoJkWPxauI4FP6-7p9oT7xMAGXh_hUzI3P1pXaPDqzEZJ3YLLGLqtMgnnLm8yEC03P97VFy3FhgMMkRa5w0gucummRCV9FtOzx1y7IL55SlAzO1sW0ZUXzqHIIYMYXzSNP7a56kNjL7DeHIhcQNkJ6M4RThw8Q7KCaT_CuBGJbQ-chPjOrq1_bug_qP9tKX4T0d1DMYl0vjKMe09ceUQFv9PdTWg_4StkoQTtY8Kz8I2ROChs1kN5qP-HDApYPVeG_GdPokng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته دوم جام جهانی 2026؛ شماتیک ترکیب دو تیم آلمان
🆚
ساحل عاج؛ ساعت 23:30 از شبکه پرشیانا اسپورت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/persiana_Soccer/23946" target="_blank">📅 01:21 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23945">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F7r2-mxfGyr9EriJRxD23EDs2XRvmJE0R9jFUTna2YFifA012meheBDc3mzRkoQ3Q1lGJwIJpCtjhKdQImj8djrxKxNGVtmXViiu2DfbPuYJRWhK0Tgzpn4fTcLTPTGPof45cwfsw75oRxeYdg8FiabFkI_abDt2tGkmn4566cbMiSCfqBZj14t-Pl31wNoD2vHt9O7wtOX5oVTlXRYdnRAXc94I8tdHYykrl2mSBo86I_ezly__NxOd1bgoZb5Opo4RzxX3rBtgea23VML70c_pxbiqk2ddxHvKVyueOTLGjeSIL05pYDNsBewDGyWedKineDzRA_5m55fv2O833w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
👤
امیرقلعه‌نویی سرمربی‌تیم ایران به این شکل نشون داده که ساعت رولکسش رو پیدا کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/persiana_Soccer/23945" target="_blank">📅 01:12 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23944">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eb124e2149.mp4?token=bLoMVog3rrZDsmiMQXrGu3NI8apkdN_qHpuT7b3XIxiSjZ4uRVUSaf9wFoau9F3AbsbhtE_oLbslgPntGjU_W1JyHEZfSPZCAmmD7clxgv8odQ655TV1IS67jtZorqCZtYp2hU9VKOjKUIGA_D98uV7E5UBmYYjqYmvdnubbly3pflIEaRKx-3sG6z05gP_k-13MWuiLBmvKvFvkG4X20RgzYhscdxyuiTnq3o-AbyQ-El6whm3aLNRiGX5i0px9B9G9uSGbb_Pz5zcRKvRrI74eXUpdZc95k8HoYvf_DlrTy-jT6Qslwq-oU1A-hu9QQ4aVPjTKx65lUlbDT_c66w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eb124e2149.mp4?token=bLoMVog3rrZDsmiMQXrGu3NI8apkdN_qHpuT7b3XIxiSjZ4uRVUSaf9wFoau9F3AbsbhtE_oLbslgPntGjU_W1JyHEZfSPZCAmmD7clxgv8odQ655TV1IS67jtZorqCZtYp2hU9VKOjKUIGA_D98uV7E5UBmYYjqYmvdnubbly3pflIEaRKx-3sG6z05gP_k-13MWuiLBmvKvFvkG4X20RgzYhscdxyuiTnq3o-AbyQ-El6whm3aLNRiGX5i0px9B9G9uSGbb_Pz5zcRKvRrI74eXUpdZc95k8HoYvf_DlrTy-jT6Qslwq-oU1A-hu9QQ4aVPjTKx65lUlbDT_c66w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
روزهای اخیر شایعه شده بود ساعت ژنرال فوتبال ایران دزیده شده که عکسای رسیدن تیم به لس‌آنجلس نشون میده‌که‌خداروشکر این خبر کذبه.ساعت‌امیرخان
🟰
خط قرمز مردم ایران
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 35.4K · <a href="https://t.me/persiana_Soccer/23944" target="_blank">📅 01:07 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23943">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/keLyCK134Bud5qquNrHyHr1kAtkb82QLzROxX2kX9FRL4H1NQv7iO8IQwL6WPRWLNdq-Cb-vOFxBvfYMjbMOE3_WGPCC03_MuTjBMXe5jYCGzfnA-5Hpvt_h7VzphM1Tq0D9y26WrVHiI6be6kyp-uEVM3h6uPtHSDWV5DE5Sg3Qw-Hk88ta8IWOtCYt5AC96pxnP0skFKziGAE_4WTsxV2-9BBmxtm-I0dIEHnbAG4DlPFqZ2G5TlqQ8EWbPwQl_7tM0oFen7YMpVOQ5olLxf-tzXP_RZYOxZQUXbL-Kzfz_MVxU_df4cO2HtUY0eaMknOZ8SIQVWoOIcXtR9dKVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته دوم جام جهانی 2026؛ شماتیک ترکیب دو تیم آلمان
🆚
ساحل عاج؛ ساعت 23:30 از شبکه پرشیانا اسپورت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.6K · <a href="https://t.me/persiana_Soccer/23943" target="_blank">📅 00:39 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23942">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TLuvqiTYH0DeDxvae5u28OhjqE87m8XlY2sRpl2WlfmgpSPQoAe2Fj8KuKdkkoNAAIsKlcqrm663_NGMxxmSVeI_AxcVjif9QnqoJvAenLHabSu8J5l18PVLvGDMEAMXA46vS1UpKOfXafAmVcr3PflmziY2bO6Mg8I-OlppRcBZzuaHmXpnWdtXaNuBWq_o_kXHO9r4aEHGe8eondv3bzFZaLxpNaQeo1vIeKQDGse666hS4LNuj8lpt96DppoDjunek7sAmma8kEd6HzCaNCeDhhN7whsPwmP7hEytDCKqd42uIFOAGaZtIQtjbHXdNSuGO3zTkhDXACckppljSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#تکمیلی؛ مهدی‌ گودرزی ستاره‌ جوان تیم خیبر امروز از طریق نماینده اش آمادگی خود را برای پیوستن به تیم پرسپولیس در نیم فصل اعلام کرده و درصورت‌توافق دوباشگاه‌این‌انتقال انجام خواهد شد. احتمال اینکه فخریان راهی خیبر شود نیز زیاد است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.6K · <a href="https://t.me/persiana_Soccer/23942" target="_blank">📅 00:25 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23941">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1a6c4ff321.mp4?token=UNDi_GBMplV9dyBr-p_bt6sCgtkZlJjFvfIAHDxBvQYcho3oKwmtCWSCzWqKtX0saCYh2QjhmYqG7whDASPewjsKApMIRTilGvWi02791kHJX37dgh66wx6Kby8bWu7X-zhX1xDvlft2tcwYaUGWWLq_2RC7oKgnYlq6qa7oBdJpLcGRbnFQGsAkpwedZP_ZFluzci-p0LZmHA93Hcmp9tHxlrRWqnhpmmiUWAUS2EW2jfsDxWge_H8VHUXRAgMRloiFMdXvnzGXapwh_5d2Nt4D1RWjE4NmUEaIx6M1e3ghNSBNgo6mWGbIBn3vtCe47QH98kL7RR1DNEF2yLIMAA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1a6c4ff321.mp4?token=UNDi_GBMplV9dyBr-p_bt6sCgtkZlJjFvfIAHDxBvQYcho3oKwmtCWSCzWqKtX0saCYh2QjhmYqG7whDASPewjsKApMIRTilGvWi02791kHJX37dgh66wx6Kby8bWu7X-zhX1xDvlft2tcwYaUGWWLq_2RC7oKgnYlq6qa7oBdJpLcGRbnFQGsAkpwedZP_ZFluzci-p0LZmHA93Hcmp9tHxlrRWqnhpmmiUWAUS2EW2jfsDxWge_H8VHUXRAgMRloiFMdXvnzGXapwh_5d2Nt4D1RWjE4NmUEaIx6M1e3ghNSBNgo6mWGbIBn3vtCe47QH98kL7RR1DNEF2yLIMAA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
خداداد عزیزی از دست‌کارای‌ جواد خیابانی فشار افتاده میگه حضرت عباسی این کارها چیه میکنی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.7K · <a href="https://t.me/persiana_Soccer/23941" target="_blank">📅 23:53 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23940">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ri6vFnpNu4_Ei3KqePUHrInt8QXboAaUqaCcv37LuBXCXpCqkRWw1U2xYKiabLwIx-M_vUOCknMznBB6UXMS5KkdIsv8tQS1di3qwr0zEirazZWZL16ZXmMZJMROG6xIJ9ZYLLLlcb7hnZhekk3G6chmx-Q_rNjadugqLZquOVVbfAimA059w52E2rnjYSy07ppAIwmBFFIXkCIeGi3fO4K6fAmL2_NlRJZ-Pd_vPuk2M36cPg74079kSyYg8DkrJ082CLUOTosziC2B-3pJdTcXx71I-WERfx7lbyjbe_xHmQ_4RynxIENmU2CAsCnzFEfb8T1i4K_6QrECuAgL-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
بازیکنانی‌که در جام جهانی ۲۰۲۶ امتیاز کامل ۱۰.۰ را کسب کرده‌اند: لیونل مسی مقابل الجزایر؛ جاناتان دیوید مقابل قطر؛ کودی جاکپو مقابل سوئد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/persiana_Soccer/23940" target="_blank">📅 23:43 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23939">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/elYpDGijupc-8COT4yf8BMzeC_LULD6dJuKSVV21mFUt3_vOC5yz1qZdymI1LK1Z9kU2QNSB3hl7vbq1kLk0WaxLyBxQ5qINGJR_ulqffILUDyVISHQk34JNDnWIe9HRHKOjJGePhwiwY7DZgyVKVdCLr8fqtrE7n7W7xer3gUalzGpH-k1iqVmewcsiHU3JbgKj1fe2bIj2vQiKjGyrb7Ga9QER0dxS_oYs9ffY_9ky5boNgf-S0vJ1LslvqZg0_YPPd2OfZJ0vQ_qGmneDts5BorJDWKPl2KV-7uzEWx-av6CYSiE_4a7ToTwISR2dKoGN7tnAssx2f7OOg4dVmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌دوم جام‌جهانی 2026؛ پیروزی ارزشمند و پرگل لاله‌های‌نارنجی مقابل یاران گیوکرش در سوئد.
🇳🇱
هلند
5️⃣
-
1️⃣
سوئد
🇸🇪
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.6K · <a href="https://t.me/persiana_Soccer/23939" target="_blank">📅 23:28 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23938">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T4tRzUYeTUdDBCvcJ0CbvReN1axuMGOc52xbx-zo8qrn1tafIbuDu-eTAV7Cis-F8v2lG_7d8e5gFtjgBUDOcjJuG1GcMdQAUklpxUOPTF1f6aMzbnSDEGtTH-3CzixUYvkmrwPxs0CpyPR-jqfQogD-KwJ-B_ohAH95bfYfMcSCuNfYLtv0J_r0GmtUWAtfjo-_41f45Mv5PJ4lRSVQDs6Dfbm3Wv0ilclDG6sGi_YjYvYqU8TzZpVP7bhvge1v6l9HB5dJgzrxCxiOJQtsrJ77uTZH3s7jlFCywUUnCoqUKYJ5BzpGcEnYdx1xgmaPAXo2Pdddpnmh3MGXDkSG8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
رسانه‌های بلژیکی مدعی شدند که جرمی دوکو ستاره تیم ملی این کشور دیدار فرداشب مقابل تیم ایران در هفته دوم جام جهانی رو از دست داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.4K · <a href="https://t.me/persiana_Soccer/23938" target="_blank">📅 23:04 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23937">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W04Jj6WpUScXU3IfrdrKtv5pUiy5nT_IJ1yr3nEWLUBWRUG1Rns4QYuV4QLS1NvKpanTDmJjjwBgZ8z6_4IYj3xu0fuyyahKWkWTpnxtKmWo3osMiwx_nu9a0hKOImMTyFVi58dcpYSg6fTmL-RaKHEiyhtYds74KIrBpJznBOHoW2aKoR3WFDak2oAetT_I33QUIecKDo3gek7Iyc_N0t42tF-q0Q1kQE8smSr_7OIIJviy3_3sxbGQVc_cSfPhIB1Aj25SQcZhG_UEShB5utZDPmry3C04C6YuS3_eqnfO3Lp-iCXL0IsvKyb1i_KTCS3_qqKZjBnE6qFbR1Wd3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛ پیمان حدادی مدیرعامل باشگاه پرسپولیس برای انجام مذاکرات نهایی و عقد قرارداد با دراگان اسکوچیچ  راهی ترکیه شده. به احتمال 99 درصد اسکوچیچ سرمربی فصل پیش‌رو سرخ‌هاست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/persiana_Soccer/23937" target="_blank">📅 23:00 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23936">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e541eb115f.mp4?token=kNl8VyPU7FVjGngmcW-wtA40dSCAiVhLdUg9uzJyN6W7KPeDMqwyK4zX7rrep1ITz1gYFcuf22bkZLFcp2Y94-ZHwAfyRs35O2_bEQjadUNjRaSUWyMdni9_fCbfVK7-GkLkQJHvvDaR318rDyJYE_gRoFwUSdO-oMMWB7BDWrmcYUN7OhZpRDMhleHt49KLX3fN_8ghx0_q3YWseViDyorN6DTydx2pUwJWF2KIlcsleOYwoV80K5ivJrHvEtVoNdUsYrKNjN1SasFVfpt7a3GFgQnDSO0aJXGzjoZtuApsWkybCpLxHCs8rvH__ZTmvA2b8Nchoopr06m40jqd65LfOGvTs2p7QwMfTdrt3UYE0q4bK3ALtIa5BZT_nvBZF7v8wrs6CFv4gv1cDZqPeRP7XJedwKgLJdMjGDMaq6MXxi6z_bbw1QJ-V9nVy_DuLgIK3rTdJbRkRvi8GK79EGFwbSXmRPV7beYeB6BrpeVvBxW6NZS8PfS_cNoGnTz4Qswb7PPYpFhFHVhusFl2rvW_A6DVb22hNKnmIxINb2YIjdL_En38kOD_pegNqTvImobkeuN4kPn2rOUy31kba8RlGI8fuA-q2GK55aMl4wq7YNg5JJDZhQsdX-1qIGPl266-_hEbho1E4DC9sIfXwZQpdwOpYqX02ha-Ev9YVis" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e541eb115f.mp4?token=kNl8VyPU7FVjGngmcW-wtA40dSCAiVhLdUg9uzJyN6W7KPeDMqwyK4zX7rrep1ITz1gYFcuf22bkZLFcp2Y94-ZHwAfyRs35O2_bEQjadUNjRaSUWyMdni9_fCbfVK7-GkLkQJHvvDaR318rDyJYE_gRoFwUSdO-oMMWB7BDWrmcYUN7OhZpRDMhleHt49KLX3fN_8ghx0_q3YWseViDyorN6DTydx2pUwJWF2KIlcsleOYwoV80K5ivJrHvEtVoNdUsYrKNjN1SasFVfpt7a3GFgQnDSO0aJXGzjoZtuApsWkybCpLxHCs8rvH__ZTmvA2b8Nchoopr06m40jqd65LfOGvTs2p7QwMfTdrt3UYE0q4bK3ALtIa5BZT_nvBZF7v8wrs6CFv4gv1cDZqPeRP7XJedwKgLJdMjGDMaq6MXxi6z_bbw1QJ-V9nVy_DuLgIK3rTdJbRkRvi8GK79EGFwbSXmRPV7beYeB6BrpeVvBxW6NZS8PfS_cNoGnTz4Qswb7PPYpFhFHVhusFl2rvW_A6DVb22hNKnmIxINb2YIjdL_En38kOD_pegNqTvImobkeuN4kPn2rOUy31kba8RlGI8fuA-q2GK55aMl4wq7YNg5JJDZhQsdX-1qIGPl266-_hEbho1E4DC9sIfXwZQpdwOpYqX02ha-Ev9YVis" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
صحبت های فیروز کریمی سرمربی سابق پاس و آبی‌ها درباره‌ اون‌ویدیو معروفی‌که ازش بیرون اومد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/persiana_Soccer/23936" target="_blank">📅 23:00 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23935">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBetegram</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hXir4Tdg84lYWO-8hVC528Q3DoVrOTNo3_tIHFgHLDCP0UkOBft6VklnuqzflM5BrTjvjNGImd9E1S5sQL7vz1aLYbxh3_ouo2NtXG2X1UZOKkH4hHhmSVMhO9HgAGkHcqfx_ik2J-uQzrcBcrddN5QSdxGBmSGdP2eDkTTcKvovDYyfRjC9Pj_viNEFO3fc7PiCRvZXsmOFM1Ym4-WicJDSr7WFKpgNF93ZTp2vMjEQzexMpZl8KIZK788elAs76vMPMrZP_8ipONI_N5OBlJJq7MW_W4801pzfHhS51n_-X44oGO0Tx00Eh9SAO4mSdkBG9Sx02M_wiBsP0lnAvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
بزرگ‌ترین تورنمنت فوتبال جهان آغاز شده…
📺
پخش آنلاین و بدون سانسور مسابقات منتخب جام جهانی
در کانال تلگرام Betegram
🎁
شرط رایگان ورزشی
🚀
100% بونوس
🪪
داراي لايسنس بين المللي
🌐
فعال در بيش از ٤٩ كشور
⚽
هر گل، هر لحظه و هر شگفتی را از دست ندهید.
امشب میلیون‌ها نفر مسابقه را تماشا می‌کنند…
تو هم به جمع آن‌ها بپیوند.
🌍
http://betegram.com/affiliates?btag=3_l7</div>
<div class="tg-footer">👁️ 38.5K · <a href="https://t.me/persiana_Soccer/23935" target="_blank">📅 23:00 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23934">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">✅
هفته‌دوم جام‌جهانی 2026؛ پیروزی ارزشمند و پرگل لاله‌های‌نارنجی مقابل یاران گیوکرش در سوئد.
🇳🇱
هلند
5️⃣
-
1️⃣
سوئد
🇸🇪
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.2K · <a href="https://t.me/persiana_Soccer/23934" target="_blank">📅 22:34 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23933">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mJAftfsek8qyM61wD4YEVG_0traQYCQ46Qo_1A3qZfV7Q6W1vNoxtjUmeMt60Cz5G1zouR5RE5vh1NDv4Y5oi5ht8aPGY4mIaQpAh-QWpS_LIY79qYztvm1xAOfi0_hvYuDqhvAsZcrbljbXLQRknfUdWKItaBehmUQIwsjjyvSrASBIlCFC0dWDseEnX5KTtP0FMkUT1iQIEKM6OxbncQXOZNuLB9CNjS1PZtkZ2Q-i56YcGt3D22TGPVshLErauHA68kURCHGyiyMVq1Ur9U98veCWK92XUEgfyaRa7TdA1dsIp1MCLzucvxGpjUCz4AG3I1iCH2ytcRJnt3tDpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
هفته‌دوم‌جام‌جهانی 2026؛ شماتیک ترکیب دو تیم سوئد
🆚
هلند؛ ساعت 20:30 از پرشیانا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/persiana_Soccer/23933" target="_blank">📅 22:29 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23931">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ad4RxPTvFipaYEvPZrQBkbnFQIwJxPyB9SRipN1iJz_T4iuroQCxW0xhEh6SjcKfoc0l9FCTGLEracaaoce9rAfaCn3pYk6SRoPQwIYSCtZswfDO_C8KOIfd10xh8szGLivCM1uPmLc5fF00-RTc0JWbz69dGUZ-GR8W_OIh7gY3QM5dh9ff7hywnYfCU5FMEt37ZEQdKjWawhfnTpzT4hkb7GiLsEzvZp1sXItKwk7pc-NnrFZ49lvdQO4ShkAowtxHnJ5YuZOR4TXSGazS_EAOKbFpDFK-OzYSKGKDktLxnLjulapXp6orzw_NiYwKJ9gJzdF4g1nrrj6N3ehAjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fR1cHDxyRN5vojxhZxQ4HKSha4k3A5OJMZ6lbj9X0nvClup96LAZYz9sDc4rkf-EWwXiAnRhttbeyljNMIHHb-3fg152wP5WAw0HAls9vEKZ-hX0hUFg9Ke600bKzUkaQPPJ1O1KV8MpVmct_WbOhkj5FBvWLfoFQ50cWJh97tr-kYzcGf70D2_3b06s4aEZOE72513R04Bq_gpiwBbNk8MNGKb27PNBReS4TwOOHKOMd0NjlIVhckOlY7iwM93cBVzJu7rBLg_zg-iYGUQ9dS_bdYy9GFrlnAS2lmCkp5HGt0NDObyUcBHm0kSnN4OFZ5fJexRHOcvNrbS3hPtlIQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
هفته دوم جام جهانی 2026
؛ شماتیک ترکیب دو تیم آلمان
🆚
ساحل عاج؛ ساعت 23:30 از شبکه پرشیانا اسپورت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.1K · <a href="https://t.me/persiana_Soccer/23931" target="_blank">📅 22:19 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23930">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lKWJGzB8F_Llkta3fIVYsEMWG5iodbDW7gnn4-dqN6su_CkqG0TZNpYn6pyzbC8Tm4ktcwJD4Y3B88qcs-N-Xv7a-KOdB6iU6F2QzLSa-D-bjkfqYMubk-zOCA-o-NZn6ASGnz_NfZL7gfq9l0MsktZERyTVZkOWp7g2aaT5pXTHsi_63EBN2So97ud4DYihbr8dAhMv_3EhL2K611_Y3SJXa8pZIorQ7ZrMXR-IiGcsQUDzgjZumLzQhFuDbuDWEW9NZoqSzUHZygVtXf4JvXw3P34Nw08bC4TE_8zAqa2J_3Zt1RiT7TXYFBxXc0sTfWXqzuRk-zl3wf_ogCGotg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
جرمی دوکو ستاره بلژیک بخاطر زایمان همسرش و متولد شدن فرزندش اردوی تیم ملی بلژیک رو ترک کرده و ممکنه به بازی فرداشب با تیم ایران نرسه.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 40.6K · <a href="https://t.me/persiana_Soccer/23930" target="_blank">📅 22:11 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23929">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3537466720.mp4?token=RwMlJW529uUSV29n_UE3rtfKE9xvstd_bCDQw2js3Iu15TlJhPB5Ut98hl9FIugkTU6iZt6k9T-XEfoSomKku1nozq2gbFxx8cCbcGLhTjPtThE_iE6wI020Gu_VqHMSnH-sgq5RIfRqL2z7nI3T06lyqzQgbNOY_dTMDfYMKC2cT0pfNiOnX64VIBxfrh0nTveEwpotfknzVyEeE5bDjeiS42py2Fok0yXZlLutS20Vaf73Sda_oBpVPCc5vHJoYSeLXzjnkMxFaOrORdl_PVw07DrC-qDv3unQrfhgHXApaxnpdADJx8w1x3v4KiNE1Z7PG4urn7RQhWXB_ZrvSQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3537466720.mp4?token=RwMlJW529uUSV29n_UE3rtfKE9xvstd_bCDQw2js3Iu15TlJhPB5Ut98hl9FIugkTU6iZt6k9T-XEfoSomKku1nozq2gbFxx8cCbcGLhTjPtThE_iE6wI020Gu_VqHMSnH-sgq5RIfRqL2z7nI3T06lyqzQgbNOY_dTMDfYMKC2cT0pfNiOnX64VIBxfrh0nTveEwpotfknzVyEeE5bDjeiS42py2Fok0yXZlLutS20Vaf73Sda_oBpVPCc5vHJoYSeLXzjnkMxFaOrORdl_PVw07DrC-qDv3unQrfhgHXApaxnpdADJx8w1x3v4KiNE1Z7PG4urn7RQhWXB_ZrvSQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
سعید دقیقی امشب‌ مهمون‌برنامه عادل بود بنده خدا داشت‌راجب‌برادراش‌میگفت‌عادل برگشته میگه خودتم سفید مفیدی؛ عالی بود ببینید
😂
😂
😂
😂
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.4K · <a href="https://t.me/persiana_Soccer/23929" target="_blank">📅 22:08 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23928">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/463a3196cd.mp4?token=KlLnSxhFuI0nXmmUCnlF2jdGcBmG99UthOkaGQ6GcK6SZA7vcEOMmHas0lUxDNMp1-C9xUa3d5196oBZthJQ26JOsKAiD3V0WVHL5j0Sw3gqAjpq0VGwK69EIXhi1MqHirPEvyXDs74fHT7aLCz9qUmEWGXGPDgqjrdwyQIP343Sa14YQfuZBLMGyDmLeZhbBRfe9ZiPQWOLxjo9Zz1eMXs9jrEGVFec-IAodUONJYlzyhJyuD22V_9wLMsbh-ZJXWrS_4O6nZPlbOI8UALhhyh1ZcO2Z93MPq4xELCu-WRdI7PMa9Vy2xhjP7WVtjbh-N2H9ekK3DJTSWLPDrLf_w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/463a3196cd.mp4?token=KlLnSxhFuI0nXmmUCnlF2jdGcBmG99UthOkaGQ6GcK6SZA7vcEOMmHas0lUxDNMp1-C9xUa3d5196oBZthJQ26JOsKAiD3V0WVHL5j0Sw3gqAjpq0VGwK69EIXhi1MqHirPEvyXDs74fHT7aLCz9qUmEWGXGPDgqjrdwyQIP343Sa14YQfuZBLMGyDmLeZhbBRfe9ZiPQWOLxjo9Zz1eMXs9jrEGVFec-IAodUONJYlzyhJyuD22V_9wLMsbh-ZJXWrS_4O6nZPlbOI8UALhhyh1ZcO2Z93MPq4xELCu-WRdI7PMa9Vy2xhjP7WVtjbh-N2H9ekK3DJTSWLPDrLf_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
این بخش از گفتگو دیشب عادل و اوسمار ویرا تامل برانگیزه؛ زندگی‌سخت و تلخ اوسمار در بچگی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.6K · <a href="https://t.me/persiana_Soccer/23928" target="_blank">📅 21:57 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23927">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🇳🇴
هوادارای‌نروژ وتشویق‌وایکینگی‌شون‌کف آمریکا؛ چه عشق و حالی‌میکنن، چه تابستونی رو میگذرونن.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.4K · <a href="https://t.me/persiana_Soccer/23927" target="_blank">📅 21:48 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23926">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Hh5qfau8cfehzgHe2oaFZo--wdq2UZZsH2nGUYHd8jetvCyjgh8QR5L7iQ9znCnqVi7CyTliwO2DHMR1grYzon3tP85fUaa7rLe-cdLUhkdmVOMUdkURr8gUQkeNHu8D40mT7cYzywHZknAyfCC_bNmjflz6Z7_yzHjBG4Xd3W5nhNQDeINXpYxpGG-839mfcFlGJrdthFYtfG3DhWTLCJcyQ4u0yxhMT3T7j7mhscCslgtM8rrvpYer4o036Dqvq9Lo5a3-DlkgaaDJjs1TKjRaZuMpl__l6J31ucZpreZHIJjdQHv8q4oH3wsc7hDny0S84a2AAkfaMgMxupnJoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
طبق‌اخباردریافتی‌پرشیانا؛دقایقی‌قبل با یکی ازمسئولان‌باشگاه‌پرسپولیس ارتباط گرفتیم که ایشان اعلام‌ کرد بزودی قرارداد اوسمار ویرا با باشگاه فسخ خواهد شد و او فصل بعد درپرسپولیس نخواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.2K · <a href="https://t.me/persiana_Soccer/23926" target="_blank">📅 21:36 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23925">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EwavZm3Xtqk8Rn37bM7I5G-6Zi5fESNHB8k1dDUYKoh0PRU2btbserOeojxLff59mG95pPV-N00jPUeGZW9zX10Gqmlp791w-7wSjD3t6Vpc80ojHfDpJX2VdRGc9bOPchrQ3APybJlrQ59uRKuzsg1b_sS5Blh3vn2up797M11pBpn0FdRucYhYwkCxXszHG67ZGNylkZS65CAEPDW-sqL0CMzYFVSQot31KxZCVWyBuJIae_2X6vtkt8FJ2KjTcbI5ui48IvxoeqeKuz1utxYRyn11yIxp1THKEU2YjnCW9c4EkVo_prlPUFvg5qJSgF60zJ9R0f5dxLETyjRITQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
🇹🇷
تیم‌ملی فوتبال ترکیه با ترکیب 300 میلیون یورویی و لژیونرای مطرح بادوباخت بدون گل مقابل استرالیا و پاراگوئه از جام جهانی 2026 حذف شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/persiana_Soccer/23925" target="_blank">📅 21:05 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23924">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">✅
محمدجواد حسین‌نژاد ستاره سابق سپاهان: من خیلی میتونستم به‌تیم‌ملی کمک کنم و خیلی ناراحتم که در جام جهانی حضور ندارم.از لیگ ایران پیشنهاد دارم و احتمالا برای فصل پیش رو برگردم ایران.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.2K · <a href="https://t.me/persiana_Soccer/23924" target="_blank">📅 20:28 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23923">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q1Qq5b2cAIlS3Fm3xsoUxrK-FLlJnr17ns5J7csDipGP3boV3Pfy8vSqoG29E2jKy8gY0xHTV3GAH2C06Pw7F5k8ZE_0KrkzUB-guQBoQHI52isrQf8XmAaUaZhKeNs-fMkENFE-4cyKvUaodAOJm8ba_cwJi_esfBjDZk2VzxK2QjkmzgS02ghXNVIJmzNHJUyrO6voM9nJ58Ip5FJKcw3Hcd459r06jhzTy1JQ2chfeLvrp7cA_28d6c-zdZzPwUjuR2psy5UXsuDYZ8EnJ7ouldD8rRpj0fFvxfFuTB73HtIzleCuPFTU7wuy1lBRdILd3hApuFSpvJsN5D6Dxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#اختصاصی_پرشیانا #فوری؛ علی نظری جویباری مسئول‌نقل‌وانتقالات استقلال با مدیربرنامه های محمد جواد حسین نژاد مذاکرات خود را شروع کرده تا بعد از باز شدن پنجره این انتقال رو بالاخره بعددوسال نهایی کنه و حسین نژاد آبی‌پوش بشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.5K · <a href="https://t.me/persiana_Soccer/23923" target="_blank">📅 20:15 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23922">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c65b32d4ba.mp4?token=mRwcrJU0bYkMjU-Ty8A_Tbg680m4NzHBWU7dDdm6HYDBcW4busBHD5yJUor9-bLfJldbV4EpOt_rh95paM8g4WgvKG8JrvtpJ2KIf_DSdskkxYHYZxJeghO3W4Yb8VjgBCPMrKXcrb3OrABxw-QI2Gs3Ht9BSaNB9oz_SVURrE-E8gI5D7wl3_hFbsZfnScOiuwe3UtThyLyJieZwaq18SWSz7ZAhUYDdz23QIASNm7K2Vc6JAv0pAX9swbBcg0nbg4rh2tVMdy1HOQPjdh9-CiWf8q-kST8l_sD6XB9GRtv-7qFOhzCvry5JBkTyT393Lffpa-6S9kVGx3NN003gWd3k0tUM43N06Gd5W9XWl-z3xjSac1tOu4ZdnGYUxAZDRSv5OZF7LkgjnO4j2DoWUjyyHNPMlzo37KY2idJ12LTjOFDaXfY1_dwt_mgjOkV7Mqscg3xmdhVOq8fcZU2TsHazWk8RwnCvrF4iGhUc21wYrdMn3Hr2EpKSJjky2zFx66k5trCN683MMkaMpZtxZouHGE3qyLueKPHRiE_vTKs7qYbUrp35XzE67kQQ_J6FqJxVr2aPFw3r86DHThS1X56URcNRKkjvNBzXz9pxpidF95zv_bM_IiCT81R-Nvufu8aDeqea-6InIiqhr_dbSsqjQyl3Yj2BfROitOJEVc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c65b32d4ba.mp4?token=mRwcrJU0bYkMjU-Ty8A_Tbg680m4NzHBWU7dDdm6HYDBcW4busBHD5yJUor9-bLfJldbV4EpOt_rh95paM8g4WgvKG8JrvtpJ2KIf_DSdskkxYHYZxJeghO3W4Yb8VjgBCPMrKXcrb3OrABxw-QI2Gs3Ht9BSaNB9oz_SVURrE-E8gI5D7wl3_hFbsZfnScOiuwe3UtThyLyJieZwaq18SWSz7ZAhUYDdz23QIASNm7K2Vc6JAv0pAX9swbBcg0nbg4rh2tVMdy1HOQPjdh9-CiWf8q-kST8l_sD6XB9GRtv-7qFOhzCvry5JBkTyT393Lffpa-6S9kVGx3NN003gWd3k0tUM43N06Gd5W9XWl-z3xjSac1tOu4ZdnGYUxAZDRSv5OZF7LkgjnO4j2DoWUjyyHNPMlzo37KY2idJ12LTjOFDaXfY1_dwt_mgjOkV7Mqscg3xmdhVOq8fcZU2TsHazWk8RwnCvrF4iGhUc21wYrdMn3Hr2EpKSJjky2zFx66k5trCN683MMkaMpZtxZouHGE3qyLueKPHRiE_vTKs7qYbUrp35XzE67kQQ_J6FqJxVr2aPFw3r86DHThS1X56URcNRKkjvNBzXz9pxpidF95zv_bM_IiCT81R-Nvufu8aDeqea-6InIiqhr_dbSsqjQyl3Yj2BfROitOJEVc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
‏یسری‌از آمریکایی‌هاازهمچین‌جایی‌شاهد گل دوم تیمشون مقابل استرالیا درهفته‌دوم‌جام جهانی بودن.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/persiana_Soccer/23922" target="_blank">📅 19:42 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23921">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uDZna6Qz9O_0N3Jzv_kKnArvZ1dw6lhEKZCq6JT0qmJp6HXNAEX-XZ3V7qPrSg007R01gJJ6464i53T9WHV9vqUGA_0KAiSc_ft95rsTydyxeikBey7_BnaQfcy5HUwrJ5Qg_9o3N75eiR6JG7cq95QzqCIwgDHieCp-p7hfkWR5wIhLFbMqk9hfsBFmVG4Xdfou7pPg6hGH6TIqfNh8Q-dRbtUBeo0oMo4lcXLDm8xiPDxT2PGEpoRVh-IscXRM4zZQy-LFnys2TlUnFdwOShvPIfhr3JoQM5rHqh5Xw49WmYar5OzGQcovvqEmoM-HoxsfhOTTrduk6aY0tiv2xg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟢
🟢
طبق شنیده‌های رسانه پرشیانا؛
سید مهدی رحمتی در روزهای اخیر مذاکراتی با مدیران باشگاه پیکان و ذوب آهن داشته و احتمال اینکه با یکی از این‌دو باشگاه قرارداد امضا کنه بسیار زیاد است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.1K · <a href="https://t.me/persiana_Soccer/23921" target="_blank">📅 19:26 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23919">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EutOeEFsSX45r2V7kvs0fMHxWxOCIX6XDP68mQTPjXfRgTAs0ssxk4YBhcqdqTBiyCFXeLNkLZPiJ-SpLNyoFSMku1SNNS99fHjSUxJ_zTRdYSsZdoVH9J0fx-9zIN5T4rnVUpspBfJanQ0BSv3bGm0gEUq0aEoB2P_1dRm6hZ9hbN7RUeE4WjNDSZnCybuQNCx6_LtPFhGrwfBy_c8Spcj-9izfgLfHMULuVTleML2y4S2K5tU-a2YwcqR8vJRabI6jm2ZaXGMmSuPILjudtVU21orUlffZBK65EW7UjyvnEWIlayHaQ5CFKrc-YyefZl0F2HpryZF0PcedeqFNKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WaChM3oE0oC3-vD-ZHV-yBGZMrOlDbXpm8aGhq64Ikfkk5PMRksxeiQHVdgURdvIPTWio4_bfYlBGtrR9OlxzdpA_LqajUtCHL2UJUWV8gLa2OUxRtf6mrNBNezbZyOXUHsGAIuoq6nT7TI7zRaFjI5hK1zX7WbY6PEQy6PlX35r70taL8bL-i3DtuVUrtsxKoDRRgKDlCxPoOmweZzmLjp11ibNn9crOM69sGfkDEmDEJhLWEIYd2iEfNN51-BWkMouys7hHRhOjH0CKtPXmLjbSLBdH8VI9ha8AV87RU9Ozg-fLySGz8LPHR9dWotWDHCuJDVIYm_dxbkxpT8T0Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">⚽️
هفته‌دوم‌جام‌جهانی 2026
؛ شماتیک ترکیب دو تیم سوئد
🆚
هلند؛ ساعت 20:30 از پرشیانا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/persiana_Soccer/23919" target="_blank">📅 19:22 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23918">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/413165ef88.mp4?token=IILgRH-O_VAalXvxpyzqeMG6vVHf2_wrcHaCTi2jpx4g7PFjwyZdDFqnmpDs10U_KRfhdvk2Z4lWbb9WzMs-_bESg7WMJ-soM5FiYyzFWYedFmXZk7kO07Z4PPPk-WF3y8dRoDSlmCN3yXJLccz9Y6EJcewZXI92UH51AUl8EJsjAlfqV-hDCwNRYXDeMcOUifvTTlk7Z7HHtriJfxPv8XdicOOmwkZ6EARyyVf5l4gC-oPVzmdddRGB9sliVGOfzwWvDTh6mOav3-WrDBnyeIlADNu2hzA4NJqD412PNsEnwnhllYqBb71LyXzDwnt2JveO6FJcfP07M-omHSytzB3IDm61SiG0dx5-WDeBavrADv8RYACvLE8IddQEhktW_7YbaoqdL0BT9Uurr1H6GzibTxlpOXTYxy0mwAgAyO69pFFO_-70vTrBLKl_sTnoQFcZUp0xQlaF3awZZuFlORLRvW6bor43ainLL2MdBYIJhuxOyBZZjusZdUIrQjAWfH-l0_8CmnrhpvAI4JbhHfVA40y8EKv3Je7nsCPeP52Egm4Wey0PqWlyl1dQ2zrJAhHO73kcbV8yiNC2fpCbj-RIXDt7GeYTYBA9Eidc6BTm6RfrPEtsMhQTHZhoSvlPvuDtYxCijIuER_2rxqrhzEsssyMJ_bTiveM-ygK6xK8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/413165ef88.mp4?token=IILgRH-O_VAalXvxpyzqeMG6vVHf2_wrcHaCTi2jpx4g7PFjwyZdDFqnmpDs10U_KRfhdvk2Z4lWbb9WzMs-_bESg7WMJ-soM5FiYyzFWYedFmXZk7kO07Z4PPPk-WF3y8dRoDSlmCN3yXJLccz9Y6EJcewZXI92UH51AUl8EJsjAlfqV-hDCwNRYXDeMcOUifvTTlk7Z7HHtriJfxPv8XdicOOmwkZ6EARyyVf5l4gC-oPVzmdddRGB9sliVGOfzwWvDTh6mOav3-WrDBnyeIlADNu2hzA4NJqD412PNsEnwnhllYqBb71LyXzDwnt2JveO6FJcfP07M-omHSytzB3IDm61SiG0dx5-WDeBavrADv8RYACvLE8IddQEhktW_7YbaoqdL0BT9Uurr1H6GzibTxlpOXTYxy0mwAgAyO69pFFO_-70vTrBLKl_sTnoQFcZUp0xQlaF3awZZuFlORLRvW6bor43ainLL2MdBYIJhuxOyBZZjusZdUIrQjAWfH-l0_8CmnrhpvAI4JbhHfVA40y8EKv3Je7nsCPeP52Egm4Wey0PqWlyl1dQ2zrJAhHO73kcbV8yiNC2fpCbj-RIXDt7GeYTYBA9Eidc6BTm6RfrPEtsMhQTHZhoSvlPvuDtYxCijIuER_2rxqrhzEsssyMJ_bTiveM-ygK6xK8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
👤
یادی کنیم از این صحبت‌های علی دایی عزیز اسطوره مردم ایران درباره رونالدو اسطوره جهان.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.1K · <a href="https://t.me/persiana_Soccer/23918" target="_blank">📅 19:22 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23916">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EmWqOBZFroneIVmhEdif7Kteu5VsNNa7v4JXFtOtMREokRAf0u8ACqUFjlkWmmlTMRdqr7eiRNlWXRi1k7qypW0d5cIffZUkotHI5hITGgBxr3WERomYXS4Fdi5vKcD3w-4ulXmN-gUcqI-y--BwWzo3iwxSlcOAxf31d2ZW6V7NceRkNXawMPW4fTn67xY7j-O15bLjBw_KZndYe0-7S8PM2wIPTdndM0fbW4CZT6sctvi2v2BKFDUDdJx3ompXfdEjvUCirI9ZDJUnVgtJGpSzZToTEKXOyaVGiN9oXh5uo4ZGa08fPDmT7kAZV2PijOZlzPl6cjcsHxwN656vtw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇪
👤
تیبو کورتوا دروازه‌بان تیم ملی بلژیک: تیم ایران یک مدافع راست‌خطرناک و گلزن به نام رامین رضاییان دارند که زیاد در حملات تیم شرکت می‌کند و ارسال‌های‌دقیقی‌انجام میده بایدمراقبش‌باشیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/persiana_Soccer/23916" target="_blank">📅 19:03 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23915">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HVK23VkdbDXlt3GmeZ2w3dFn_f2Vb8-DKyW7_j0udA7b_LSVjEBeYmBGAcHMVAB45yCJ3cpct7IcCq3GGBtqTog6EYGECkdCDQljR8UVKzLo5TljqcHWkmi1nCi_Om9NFdi4cpeT0oE16apBHjoHnw80kKo5VfM5PUtxbmht1WxUqnmY9gvx1oLs8x3BoYzArqVohcxiGaUxmKqQhfuRbkWhxte421RgktyYMG6e4NH093OjmhKlAyino2ewGVIhOqvSWvnbkoLtdX-nIRufcjv5TQ96HM2G0XHbMLayTMftamfDdGghZYLoeXIwEkKb3gG1zWfE5ESwBRHe1r62Dw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
پیش‌بینی اپتا از نتیجه بازی ایران و بلژیک
‼️
سایت‌اپتابراساس۱۰۰۰۰شبیه‌سازی‌نتیجه‌بازی ایران - بلژیک را پیش‌بینی‌کرده که درآن شانس برد شاگردان قلعه نویی ۱۵.۱ درصد است.  در این پیش‌بینی شانس برد بلژیک ۶۶ درصد و تساوی ۱۸.۹ درصد است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.2K · <a href="https://t.me/persiana_Soccer/23915" target="_blank">📅 18:55 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23913">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/602d7756fa.mp4?token=KAWVgktd1oTmYKsntbRsAxsqOaMS9UsQs_S7bMq9I9pLtE_OD4cOqYRWlAWC9L-Y4E2bq5-W7-Seo7uUbscPx4RtPdEh8jVfJvToEKoot3kODUXgm3W5AiFwya3xGE8asDQY76ga_VRqZkWj_Rx_QSypHdAQxAJzGoPeZoiURVhPtBGLtIlJ8am42uFWah2tLQy8_jWk2LRCy2rKamPJcNgmP_VGzaztA2Yr7Q8B-W_nYR8G27IavX-MWLQAp9fkql1i5A1XhVoY1vRvmTZ2FM1MruczFO4jMqm33hzmWRnDh_SDF-4ir1uffTmA3LzOdopleZ2yQi3QtdA4gX0yxg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/602d7756fa.mp4?token=KAWVgktd1oTmYKsntbRsAxsqOaMS9UsQs_S7bMq9I9pLtE_OD4cOqYRWlAWC9L-Y4E2bq5-W7-Seo7uUbscPx4RtPdEh8jVfJvToEKoot3kODUXgm3W5AiFwya3xGE8asDQY76ga_VRqZkWj_Rx_QSypHdAQxAJzGoPeZoiURVhPtBGLtIlJ8am42uFWah2tLQy8_jWk2LRCy2rKamPJcNgmP_VGzaztA2Yr7Q8B-W_nYR8G27IavX-MWLQAp9fkql1i5A1XhVoY1vRvmTZ2FM1MruczFO4jMqm33hzmWRnDh_SDF-4ir1uffTmA3LzOdopleZ2yQi3QtdA4gX0yxg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
اخراج‌المیرون‌ بخاطرتوهین به ترک‌ها:
آلمیرون بازیکن پاراگوئه به‌دلیل توهین‌قومی به بازیکن ترکیه اخراج شد! تو قانون‌ جدید اگر دست‌جلوی‌دهان بیاد و مشکل پیش‌بیاد بازیکن اخراج خواهد شد!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.6K · <a href="https://t.me/persiana_Soccer/23913" target="_blank">📅 16:36 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23912">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/94a793ad17.mp4?token=gDBQ7pEM9sf__dEVc5p8QW6n0BVEKL0zS3uLP2i4fRNemhMe09syPu_LgXCcKmilBYVa36L133zYcYAtn9WuOEJGk4BvzH4JyYBO-4GSQb7oKTVNpMAYclQoJ08TldrjFjZesRqn6SpATXM39Be9j6HD_BJcAoOuxAOraHp7MebupNlH8aj9yj5AqWg6MOjuIjXMuxT1fjd_221XH3MwKG26wlmEmZCUCA882xprBLwewDaSqK86T-SvIOgZdOVqvrG7ByX7ELmVVU1in8yQTeuR4VAERYj-_-VQCG_eH590vtTjvwoRCCCupHQIUPaxsHFPm_mmnT3FkS9phnt2Sw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/94a793ad17.mp4?token=gDBQ7pEM9sf__dEVc5p8QW6n0BVEKL0zS3uLP2i4fRNemhMe09syPu_LgXCcKmilBYVa36L133zYcYAtn9WuOEJGk4BvzH4JyYBO-4GSQb7oKTVNpMAYclQoJ08TldrjFjZesRqn6SpATXM39Be9j6HD_BJcAoOuxAOraHp7MebupNlH8aj9yj5AqWg6MOjuIjXMuxT1fjd_221XH3MwKG26wlmEmZCUCA882xprBLwewDaSqK86T-SvIOgZdOVqvrG7ByX7ELmVVU1in8yQTeuR4VAERYj-_-VQCG_eH590vtTjvwoRCCCupHQIUPaxsHFPm_mmnT3FkS9phnt2Sw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📹
گرفتگی یهویی عضلات پای عادل در ویژه برنامه پریشب جام جهانی؛ سه تایی غش کردند از خنده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/persiana_Soccer/23912" target="_blank">📅 16:17 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23911">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UmRtqriPVIfcI8CWQMZqHsCAZAOJH1rbdBtkt7bL3BK2B3KMU8_C6ZVGpaG9Hm6iMElNsIB5896GsC3JQrX4GFENzVhhRABN2f7Pm4saKeX5HtZvbMsVWWfbZchfYHKovfNrZ7kPZsTsgvY81Bi2lWwwOVCxwBQVjOn4KIWJKaheyzc3SFQrlL083-qjAGOSdJXsq4YTYJIfTZvRSSz5KxMOfXbWZ_Xx9vuiCH5XeRGOvX53rBMi5WuLkgM0jLeYmkUvI6FsjhmbNlYOd1lcPHr_caaBZoUCiIZU6ZODDYcyZ8bVoXlXhDBuh0LY3W6krnMw7ZbF5NkxTzfMh8BQFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
هوادارای خارجی رونالدو بخاطر مصاحبه ژائو نوس که گفته بود کریس‌رونالدو برای‌ما فرقی با بقیه بازیکنانداره‌وبهترین‌بازیکن‌فصل پیش لیگ عربستان هم فلیکس بوده ریختن تو پیج دوست دخترش:)
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.2K · <a href="https://t.me/persiana_Soccer/23911" target="_blank">📅 15:54 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23910">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NLxa4iEGD08MZPvyIW98AKsA7bAO9NScgtjuTb6WK4XWV6I42vrCzw9hpmb8b35Upy8OWCoCfUv23fLj2oRboLtq6NdgRWi1YB5AxWrEU2mGTcgYp6WVtKlLLaqXKUnXOtVjKdBQ2EfG3TqT1ryMt1JtMV48IyUJtiIQhvyuMLsBFz6lWHUe_AHwtI3OmnYIIo4XVJyQGoNDD41a0ocz0kKQ38qpJDJe60leLKjHuOEJREXVjAOdDVTmiZgnRijO1bMmLYI5_SvVV45rwo1g05KIw5BxVuX6vswsetcrlTlzpWQv_rHtrKEFQK5CeF8U1vkGv2-zELPzD93qW_stIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛ طبق شنیده‌های رسانه پرشیانا؛ علاوه بر امید عالیشاه و مرتضی پور علی گنجی، سروش رفیعی دیگر بازیکنی است که در پایان فصل قطعا از جمع سرخ پوشان پایتخت جدا خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.4K · <a href="https://t.me/persiana_Soccer/23910" target="_blank">📅 15:49 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23908">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d95ab0dfbb.mp4?token=TBehl6D5s-YvAwHHcDYdabWOOf953q3L7lol39MqlbBz-FhikY5UKqU9zGEGSCLT_v-uVNE0bo93gEnQpo28D4ziZjmVgZPWmA8sLsMJ1a93k5cdDJ9vwNmeeYtnQLLZb4Hf9zNq6snQo_-9ZBvbgA_pCTkz_W0ItyylNByE1ft8812sGVZFz0dmdNSYSI0bwTOiAz5m64xbKoJgJdyq7VILfFKvBRrNsvTYtPJgrEgrFvAVrBUpwkwjWRj4BE62fzG8_7AGb2a-F4KSb30W4wZTcVeaxJHtL_JtTRIKVzrUew0mcJ1AgLCvW-AP34D_wG-AZqXWqlCYcTLJnO56Gw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d95ab0dfbb.mp4?token=TBehl6D5s-YvAwHHcDYdabWOOf953q3L7lol39MqlbBz-FhikY5UKqU9zGEGSCLT_v-uVNE0bo93gEnQpo28D4ziZjmVgZPWmA8sLsMJ1a93k5cdDJ9vwNmeeYtnQLLZb4Hf9zNq6snQo_-9ZBvbgA_pCTkz_W0ItyylNByE1ft8812sGVZFz0dmdNSYSI0bwTOiAz5m64xbKoJgJdyq7VILfFKvBRrNsvTYtPJgrEgrFvAVrBUpwkwjWRj4BE62fzG8_7AGb2a-F4KSb30W4wZTcVeaxJHtL_JtTRIKVzrUew0mcJ1AgLCvW-AP34D_wG-AZqXWqlCYcTLJnO56Gw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
#تکمیلی؛ لحظه ماچ کردن خبرنگار کره‌ای توسط یه‌خبرنگارمکزیکی؛ حالا خبرنگاره اگه ایرانی میبود تا از خانومه لب نمیگرفت ول نمیکرد! این خجالتی بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/persiana_Soccer/23908" target="_blank">📅 15:38 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23907">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DwCc5EmZIGFCh30lP4TlSZeGo-b-byuzwsQh_ajRE9HCm2XVFaTEuIgbhNtYykqdxiZtPfTRQGURs8SXTc90n9Tu5cH-qv9c7PzHCb2NTc0Z-0HMW38AqmnMClW-hQG_xuL4tLXucIehMJ-Pitp59LqKCjBEs18MAUGm1pY2ooiTTJMxaiPF3NU07OH7lZvq5UYE9e9UI54EnjXUhC7ta_hsXc5KulJgvksLC_hDHjFDTOocfDhxwMl-xiLZfT0QUKwxsV9E61bvYflbcHtx6ByDt4dHH8i2zVzxw-RhiVN78FT8yQa46ttEFwcLQHTtToS3BgC0QYkJHzIQ1MefkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
جرمی دوکو ستاره بلژیک بخاطر زایمان همسرش و متولد شدن فرزندش اردوی تیم ملی بلژیک رو ترک کرده و ممکنه به بازی فرداشب با تیم ایران نرسه.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/persiana_Soccer/23907" target="_blank">📅 15:23 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23906">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b6M-DSMZ4ixtVDL2CsuIFwL_QXuNLdGE4lOscCwHK9Br-KNDj87kV1MOxunHaJk7DqQLqAw09yZSJK9YYhauS_vvSTyBT7S3MbHCTQCgSJ9Cyh57Ktk9FpXh1owFwY1ztf7tHmNCiwPVrLTZjs_r2HcYy9W_fM1cju_x9TvCxLIrPFYNOPkwKlMV0sRQQyEEaiqJmLby-tqb3whWO_52Z6qQKlpFA2ZWFJTpNqqFK4nyzsl78o3BDEBRSGpvdkRkrrEhs4dETwlypIuJz8i-H9SO-9QnsvNV8jYtEBzZfjvyyTBjYF1kAYdLAMTooyXNqa3Z6QCI9jOEoBdF3xtZ4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
#تکمیلی؛ طبق اخبار دریافتی پرشیانا؛ محمد دانشگر مدافع 32ساله سپاهان بعد از جدایی از این تیم از طریق یک‌مدیربرنامه که رابطه نزدیکی با علی تاجرنیا داره خودش رو به استقلال پیشنهاد داده و گفته حاضره به جمه آبی پوشان پایتخت برگرده.
‼️
محمد دانشگر تابستون سال‌قبلم…</div>
<div class="tg-footer">👁️ 44.6K · <a href="https://t.me/persiana_Soccer/23906" target="_blank">📅 15:16 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23905">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Asp3g4mPvnmabbaxEs2YEvgZbnsK1Y1ODa91-KLrEoCZIr6_7Nztk0kNi1KJ7QHNYubiqUk7r-2w1LtVwpHealwk_w8ES_7T9-KSNHgqWw4vnx0JKFsGl2Aty8Hb1HQfCTGyXxQ9yzFCtEycsdXXUSefflFT1aVqiaSG1-qDNXOlqGHz4YYkZkbtHqmkQLYq89bkQqqXSX2gRyOdp6lrfRpf_C2bXh6NXhMGUMydx6Q6lOcvPESCNPCy51Qpp-o0BpVeTQMHmgpXYQEDY4LMjmLgCsbODwBO1VPEIu6ej46Uu7fFlIWX48m6bzTLAJXXvA9pbds3UtRHqVw4_i3JdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
کاسمیرو ستاره‌خط‌هافبک تیم‌ملی برزیل و سابق رئال‌مادرید و منچستریونایتد برای‌عقد قرار دادی دو ساله با باشگاه اینترمیامی به توافق نهایی رسید.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/persiana_Soccer/23905" target="_blank">📅 15:08 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23904">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VBGWzeW4WbSybnQMqzmofyiI66K4xF8mrZ058qCnhCLkBOscwt2qXgYYkHkcXz-oJeLK1Hols5ZcUQeYSKPvZkYY0cK2KDM-82yIDzPstqkKWjWE7uPFUvqAKF8qv3DRqOJJJjfj8KZQJTwFWa4utPKcc_uHzdxeaRbM6yHFhYB2hvsHvxOstlmzE6IOCaOqfZqse6cYTUqUOQXo56YoAv3sViiogRyAYpfP9Pza5ryVxeavyQx6LBqnUM02-kpY_34U0phco-46w5lefs2DN377DVKbpiga7KVM9w6_EZGHZim69TPag_rY5W9jcu_WRXa-ZoKOrkBalYwkyAvoIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
ویژه برنامه پیمان یوسفی برای جام جهانی بدلیل این که علی فتح الله زاده به میثاقی مجری سبکه سه تیکه انداخت متوقف شد و به او اعلام شده که دیگر حق ادامه تولید این برنامه رو نداره.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 44.5K · <a href="https://t.me/persiana_Soccer/23904" target="_blank">📅 14:42 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23903">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/50f475cbb4.mp4?token=YdpQufRV6waWeQTj7zIJFkGbgV0LlhvRLw0x6w1O5jXKoiDqkNUHiw_LZDMj270TCd76nEW_EpYqd3oL0ohxqhOtgr3gKaYTD5gURbK2zhAKlVdqfPqJ-olMxWJ24DxbW9Vl9GjJWJJTYqYmbDmZprB-wvKpOspXJgouWKPL-xHYNhR--JTquLtAYLQcFei0xpskjrwUYVLFEof3CD_W5yb1blD3tmemQ8XD_0Pfc7B_jDcdEf0QWbXEfAp-MnlL--Hn-V5I6C-rTHl-272JR0ujurhBlYJWIMdfdsbPBQNnBnzuIe_eF5YVeSk8ymIZqEUY_pSBUrI6aZjdPGI3Lw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/50f475cbb4.mp4?token=YdpQufRV6waWeQTj7zIJFkGbgV0LlhvRLw0x6w1O5jXKoiDqkNUHiw_LZDMj270TCd76nEW_EpYqd3oL0ohxqhOtgr3gKaYTD5gURbK2zhAKlVdqfPqJ-olMxWJ24DxbW9Vl9GjJWJJTYqYmbDmZprB-wvKpOspXJgouWKPL-xHYNhR--JTquLtAYLQcFei0xpskjrwUYVLFEof3CD_W5yb1blD3tmemQ8XD_0Pfc7B_jDcdEf0QWbXEfAp-MnlL--Hn-V5I6C-rTHl-272JR0ujurhBlYJWIMdfdsbPBQNnBnzuIe_eF5YVeSk8ymIZqEUY_pSBUrI6aZjdPGI3Lw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
عادل فردوسی پور:
یه زمانی من و محرم خیلی بدمون ازهم میومد ولی الان من خیلی دوسش دارم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/persiana_Soccer/23903" target="_blank">📅 14:40 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23902">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AY6ErMtU6-C0NzdaKYve6LFlmxT9DGP10J0LyLOxabXDjhWil3tZAbr8YdSM1vvP11dI4QKNbYq5z0Tr0196XWLxsXdq7p8zlW6Glvtfpx2g-dK41pnOknn8JxDgB47euUCzvHuUkruUZ3qOKWgBSGvnUYEYYf0-dtlpCE4Ijc_8bULIofv2pkmr1oSffhsZa61VR9wMW0nT939zrV-D1PBml2v_OS6iIhXmTiW6R9C8wOUBSOVMOCe8XenFKdl_A5xAn-YbMBwGxpjI2ldgktJoht1x9MQYJFjjO5xghgI3-sL_4ACGDRe1NsOhoJ5UxnzzNNwhHCY3kfG_zkZGJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
#تکمیلی؛ طبق اخبار دریافتی پرشیانا؛ محمد دانشگر مدافع 32ساله سپاهان بعد از جدایی از این تیم از طریق یک‌مدیربرنامه که رابطه نزدیکی با علی تاجرنیا داره خودش رو به استقلال پیشنهاد داده و گفته حاضره به جمه آبی پوشان پایتخت برگرده.
‼️
محمد دانشگر تابستون سال‌قبلم…</div>
<div class="tg-footer">👁️ 44.7K · <a href="https://t.me/persiana_Soccer/23902" target="_blank">📅 14:27 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23901">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lFq5u3m80iLQM_73bO4eRbJZ3xXaJbVixqYU4G2BqrpqGwoz8BFv6zls5X_-9_AnHl1hUkX0IHVqUmQX5tSnntSnzCEyto_vBAWAiu27Y68XCrtZpYybb0BTdrVvGQcaRXlKAxpXX01U0gfi38yEH04gbehm4J5asYLI2YvyBTsNqjZrz0APnO8XgiB7aOyMOjfuB0H7DDkPBHdkGGgQQ-OeUGqOJGixeK076Fi5HLirSYzStIP9jsPeJPp5t8jvV7YDcvzzWCc29wEEkGRm0f_qL0V1_9V5h9uKS49Dy0eNogwPIFv7rx1hKz3-EhgsXNbxgMnLDmA8OL-28TCiQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇳🇴
عملکردشاهکار ارلینگ‌هالند در لیگ‌ها و تورنمنت‌ هایی که تا امروز بازی کرده: 279 بازی و 260 گل!
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.2K · <a href="https://t.me/persiana_Soccer/23901" target="_blank">📅 14:20 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23900">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NJPLDV1JdQJHZhfogcFaf2poSGYglFcpkj4SdoQBsGYZOCw17Qh16vTPwbFV4p2wRitULCINt5cEZcD91DwC5xJiQGBb1aKAdA79tJA84WoXObVtRqXhjGcI1SpXsvx_MSWFO0TyC8UKjxyQVNyrnloX8dHMdkCbRV094sV_MWdRIYKiHLfbzV_I0WNnLocVLZN-UJ0w3qXa7eHiV2_FKibDDJ8pEUwkrj36p80R60pTlW3yrbM9aKwbhZ_zOOR639mk9EOoaxxPy0tMaTMxXRG7XvrqbVWtr92kqEIxHuMKjR5qon3hZ3q0IiOjp2URcvq81WEOPQfxS7YYLQ_ZCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بااعلام‌فدراسیون‌فوتبال؛ سهمیه خارجی باشگاه‌ های لیگ برتر درفصل جدید چهار عدد خواهد بود که یکیشون حتما باید آسیایی باشه. به این شکل 3+1.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/persiana_Soccer/23900" target="_blank">📅 13:56 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23899">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UzQJFfWnZ9IpT6Gi42KC-p6qEkgGNMMtrEUuSvfeUsKlrMfl0ZlT_iJebGYEGigo9Gdt9C9T8se4IWR2Mn5yYvim4zk6K0JL7OYaH_9kPSyscH7xQSp9toP_FAVPfqnjeGETUKVWiGkLR2Rwu1UtQ5ScwJzr93cEoonCQlVCotnVW7cx1VYH4XfSYouTZ9HOdrHI42ckQc1rcqjuR1DHfRHyPNL1kcdmXhQ1qk9A2l92BywhjSbEGpPnrE3bfiD5BI2ILC60nsBuSqjmwOWwvszX6zXsc4nKFgQSXMFA83nuy9Xpu_okilDLeZaarplwekP578RQGBD2Hk6L0kcZ7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مهدی تاج رئیس فدراسیون در اردیبهشت قصد داشت استقلال رو بعنوان قهرمان این فصل رقابت‌ها انتخاب کنه و حتی‌به‌مدیران این باشگاه این موضوع اطلاع داد اما بعدِ تماس مدیران باشگاه پرسپولیس با مسعود پزشکیان و بادستوررئیس‌جمهور تاج از انتشار این خبر خودداری‌کرد.…</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/persiana_Soccer/23899" target="_blank">📅 13:46 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23898">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d55cf4416c.mp4?token=CrJcMzUq-hUykXz6jRz7wj62EJtx4oJ2jyTNIdhXfFM4dBipaHF0HvmxI4VguSqWFuJBiIv0bsKxQcAUeBVIlhTWb_uqxqjzu-kvLWk8mwtGMPC9EfgArVRa--8LjvkbRV2JWIQAewMgThbQm6KoGgZea0kTEvGcAcBV5t09kp_LSgy1c1-WL9hJ8Vf8aMPE2FQQht951ouZu9z4prwV_muSBX07QLcpUG8tFOZFXiI0kXmzlTcKjkGYCYaX7qnlrbZq4UZhAVodr7BETtkh6dyBypTzZGXC61XOquz8Or-L5_4KrdLUtlsfqB-hkYPCAC0buVsVOMk26vmY0ay0zA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d55cf4416c.mp4?token=CrJcMzUq-hUykXz6jRz7wj62EJtx4oJ2jyTNIdhXfFM4dBipaHF0HvmxI4VguSqWFuJBiIv0bsKxQcAUeBVIlhTWb_uqxqjzu-kvLWk8mwtGMPC9EfgArVRa--8LjvkbRV2JWIQAewMgThbQm6KoGgZea0kTEvGcAcBV5t09kp_LSgy1c1-WL9hJ8Vf8aMPE2FQQht951ouZu9z4prwV_muSBX07QLcpUG8tFOZFXiI0kXmzlTcKjkGYCYaX7qnlrbZq4UZhAVodr7BETtkh6dyBypTzZGXC61XOquz8Or-L5_4KrdLUtlsfqB-hkYPCAC0buVsVOMk26vmY0ay0zA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🏴󠁧󠁢󠁥󠁮󠁧󠁿
لوکاس برگوال ستاره تاتنهام به سرعت داره به یکی از مطرح‌ترین ستاره‌های فوتبال تبدیل میشه. این هافبک سوئدی‌که ۲۰ سال سن داره نه تنها بخاطر ورزش حرفه‌ای تو جام جهانی ۲۰۲۶ آمریکا معروف شده بلکه به خاطر صورت زیباش هم وایرال شده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/persiana_Soccer/23898" target="_blank">📅 13:41 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23897">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a8cf4e4f15.mp4?token=ub63aHCT54WLSkieYf6P5i9QUwQ5zyL0hgl0U_L9DQqWabgULpLBU7Cefa04EIAaBRXmLNTKzl0UyO9EE_AtaqTV-GmMdurWmMmuxQOJvOaQTKch_sweF_F-0TMqixZEH2-1UPG8io-SFLb-9INbOnQDvRjJKRgWl-PqTsovBo66MmknNCPNYGGuxLDoHKeFjR-5-DEiejg750ogcSch3qLnDg3swz354m0ewodjlkvYdcqk-_GnuM_CFo4p4oq4iZVuKC0CJNJ4rPn8q9tC7Wx4Li7T6LSf-RjlhG5cgCZKRFG8SMipyQWsVFiRlu8XoUvypWRYNvbv5SkNt2JsIg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a8cf4e4f15.mp4?token=ub63aHCT54WLSkieYf6P5i9QUwQ5zyL0hgl0U_L9DQqWabgULpLBU7Cefa04EIAaBRXmLNTKzl0UyO9EE_AtaqTV-GmMdurWmMmuxQOJvOaQTKch_sweF_F-0TMqixZEH2-1UPG8io-SFLb-9INbOnQDvRjJKRgWl-PqTsovBo66MmknNCPNYGGuxLDoHKeFjR-5-DEiejg750ogcSch3qLnDg3swz354m0ewodjlkvYdcqk-_GnuM_CFo4p4oq4iZVuKC0CJNJ4rPn8q9tC7Wx4Li7T6LSf-RjlhG5cgCZKRFG8SMipyQWsVFiRlu8XoUvypWRYNvbv5SkNt2JsIg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
خداداد عزیزی مهمون ویژه برنامه جام جهانی یه لحظه از دست جواد خیابانی عصبی شد پا شد زد تو سر خودش و نشست گفت من استعفا میدم.
😂
😂
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.4K · <a href="https://t.me/persiana_Soccer/23897" target="_blank">📅 13:26 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23896">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vt3caMHrTm12zXpLvFKkVWPbW33Hlc3jNfJQgEYyuilb0te4UCeorGEKF6k2CKQX9rP4o3195LlfULnsOWvj-hyErdnBtuQjc5cndSZbq8D1amH_PbvqvWUEiqZfay4qtQxyCLqoWEMIkm7xi4cNQkPghfdIA2hCTW6xprMPQSM5DSui6dUI2a7-YnSu6VXsGmKNoJ1wNFhlWH-ZRyIDRVaaKmYtA_wgwQ60tZzl0V1hCK7yMXK2cLl_GhNE1xxbPGPlhDNRLe3Y8hnyZfN41fo9dj5x9i-kfv_I_fNR7x4_dUnRJhJqVjnSLFgJikSf7vQON4IP61H1vISrqQHqcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
جدول گروه C رقابت های جام جهانی در پایان هفته دوم؛ برزیل سه هیچ هائیتی رو برد و مراکش هم‌با یک گل از سد اسکاتلند گذشت. بازی های هفته اخر بسیار جذاب، مهیج و تماشایی خواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.3K · <a href="https://t.me/persiana_Soccer/23896" target="_blank">📅 12:59 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23895">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dBOS3XzFpqb6JogWW1y_fN6_xPmJjYQtTMBGR7YJqSj-MITtavdIc80e_BphOFjDVFxqJ49Jjgn52CdiZM4oUvsR0pAbRqGzabZuvvrh9nKCCegfMH1RydyDBbtAaH8IjHGpEKN2UctFkxICMfdecRkOQ8MqlVDiEOA287wyeMil1PeoeLdwRQMO7od7QLs6QX_ThSMTcOkvWnXXENbxcPp7PYZmskLvFtBYrLAMVbZOkCzZBzXtfTewktHDmp-84R2xNEOfFXHwouU6FT5BXXsGsdEy5X_u3TcqBy-4Ijo3Dir8zrzvmnIcMD1dEFHHpgklXaRSYIgDp8Ib3GcnUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
دقیقا 19 روزپیش؛ صبح 21 اردیبهشت؛ مهدی تاج با تاجرنیا رئیس‌هیات‌مدیره‌استقلال تماس گرفت و به او گفته بود که فدراسیون به این نتیجه رسیده که امکان برگزاری لیگ وجود نداره و بزودی استقلال رو بعنوان قهرمان لیگ معرفی میکنیم اما تماس‌های اخیر حدادی مدیرعامل باشگاه…</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/persiana_Soccer/23895" target="_blank">📅 12:40 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23894">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b18c6a9792.mp4?token=DHlFd_PVuOwMmOkRKyk5ObGhzugtOvdp7lGXo4bamkwZdXxXXFReErR3RtTD2EXtKAyvlV48tMBy7lngMLNK8XOtv37ZXN_lF9DX-nE62TdbiWVWv6Dte3ifdLtV9BBxkBMGKrKnTinqmQtiEEqGQieFEVgFioclQ7yfEMaZ6w71n4lztN8sbUQVcePwOJmhu3-EO7RYZwtWjqwiL6MqVPNBwelI6pIlX2mGYvpXFtcBeqINQDT6nBYjEHEjMNXZ7W3Y5EbWxcXdNGrIJLiX_xCRiLFx_cWJSMrtH7gcCWBj8bGeIfWcpEmGIFlU6R5vPcIce2dWsuj8RHpjz63td1kmekeuaDEA4BKRTYldC2V-1Z8yapvYFc9Iq9IVKj_-CEbJImMTrk5QcvlX6WX1CiWFahOpaEtcqzoNh5nzZQspuhY9QrcbVglQYNe6eibdigEcXVCUvyrmGrfIqvqHRk_w882HzbxUTWJxROhXUTFhU1DWt25nko6cAPEpm97Jvzu1wXJZmph1E8OgZKrHovcTJsq78G0DcJPc07YbH5NE7zq0EIVNjuYIhqW4DZn2V9UxAYVYixLHIPdfPfnXLl5kj9rffIFT-ENUZc9Ss_F2TRdpGA_c-g6dpSnqs6XRvYAdY0crgwa0H6OWedZrzabiF4pTjVAEQOCquBD9vJM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b18c6a9792.mp4?token=DHlFd_PVuOwMmOkRKyk5ObGhzugtOvdp7lGXo4bamkwZdXxXXFReErR3RtTD2EXtKAyvlV48tMBy7lngMLNK8XOtv37ZXN_lF9DX-nE62TdbiWVWv6Dte3ifdLtV9BBxkBMGKrKnTinqmQtiEEqGQieFEVgFioclQ7yfEMaZ6w71n4lztN8sbUQVcePwOJmhu3-EO7RYZwtWjqwiL6MqVPNBwelI6pIlX2mGYvpXFtcBeqINQDT6nBYjEHEjMNXZ7W3Y5EbWxcXdNGrIJLiX_xCRiLFx_cWJSMrtH7gcCWBj8bGeIfWcpEmGIFlU6R5vPcIce2dWsuj8RHpjz63td1kmekeuaDEA4BKRTYldC2V-1Z8yapvYFc9Iq9IVKj_-CEbJImMTrk5QcvlX6WX1CiWFahOpaEtcqzoNh5nzZQspuhY9QrcbVglQYNe6eibdigEcXVCUvyrmGrfIqvqHRk_w882HzbxUTWJxROhXUTFhU1DWt25nko6cAPEpm97Jvzu1wXJZmph1E8OgZKrHovcTJsq78G0DcJPc07YbH5NE7zq0EIVNjuYIhqW4DZn2V9UxAYVYixLHIPdfPfnXLl5kj9rffIFT-ENUZc9Ss_F2TRdpGA_c-g6dpSnqs6XRvYAdY0crgwa0H6OWedZrzabiF4pTjVAEQOCquBD9vJM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
گلچینی از صحبت‌های جواد خیابانی در گفتگو با امیر حسین قیاسی؛ مجری برنامه هنگ کرد قشنگ.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/persiana_Soccer/23894" target="_blank">📅 12:27 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23893">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BSsYQ5LxdlQa60eEwPJ6BXo8VRJ09qY1viSHp1QxL-_TdAnwgDHToRXWY1Zgn4FCzLMUIjMoeIJN7k0xWG9QRbMcGx6Q_Iv-5UPdnJ4pFJ8rGIevWx2J4_JBk8CIaFNYjq5K09HVpx4dJuJRFAvZi65dlFKrB0Lz-ki-U8AjEFaD4ksTTJwnwcmBacq0XOkU4JhDD-zrP9DySoncPg2WzMXEsqo1cwnZE211F32NQGcNofDlcW7RHAjP-O3aG-n-abcIUF0iMvPMLykhIjXJ4WSSTFGGbq1x1QvDK6aH5RnhFh5EmSEVzKmMl6-LTx0qhxAw2FZKz_9ad7bMfzvk8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
طبق شنیده‌های رسانه پرشیانا؛ به احتمال فراوان فصل اینده رقابت‌های لیگ برتر 18 تیمی خواهد شد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.5K · <a href="https://t.me/persiana_Soccer/23893" target="_blank">📅 12:08 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23892">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zi861ojd1Szct9rgHM_ZKldWC9OAh_LeSiaEpJnaGDxBRvZ7_FIHw2YopUcnFdUwDKU_ggHriiTSgCLek9rPbZBG79cgJ0apzUFaSGSrJaonNi-03WVwJiHBf9juxxdAnw3F8eRbP5FHWBFavmIz546IHdGLEWfbLLk6ga4z0jsf9d9x_pepnfLQu3Xmuc-ZkePsElP_4VA_CNkls816pS0NtNUIvQAg07LmjSHOSELjMdb3jNy6aF0cnY3OBB-_lD2xCo84SuQbsIaoTxjTbcqD_dsJtwnPE4bL_Q-nWDS5MnTSpFapUrMzGANgvLrHrbdpvmj7USo5Gbrt1ihjhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
طبق آخرین اخبار دریافتی پرشیانا؛ دراگان اسکوچیچ ظرف 72 ساااعت آینده به تهران خواهد آمد تا مذاکرات نهایی رو حضوری با مدیران باشگاه پرسپولیس داشته باشد. هیچ چیزی قطعی نشده. اوسمار 50 درصدشانس داره. اسکوم 50 درصد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.4K · <a href="https://t.me/persiana_Soccer/23892" target="_blank">📅 11:50 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23891">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a0ae405613.mp4?token=mDxj2f3Ta4n1aMaOhh8fpyVu9SR2ON_Y7wOdi9u0YAL07Z8kEPhL82TKAu-HOz9rgtN_BacI4UqMnZgmwAgyGUPub3S5W0vTBRydEi2NcRqTYVorgbuhwG-3yb24wfRV5lyx0nkn5YA5JVcFPTyYJa-if24pF7Uztcww4CsMez3RU-6qvhCUhilDQw93BbE_5oMK58DCB6T_pTWYcCTCkAAtkJ1bqDVMIQkvYH3e1osjtyQXl4424ZTZX-cNAQ-smanMhTgml4iHZrZkJulD8aL-AgOycZ957BNzW7rEUX5h8KebNcEx7YvteO5JqkidWDOaVC07KbKDB3CyXIL_gw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a0ae405613.mp4?token=mDxj2f3Ta4n1aMaOhh8fpyVu9SR2ON_Y7wOdi9u0YAL07Z8kEPhL82TKAu-HOz9rgtN_BacI4UqMnZgmwAgyGUPub3S5W0vTBRydEi2NcRqTYVorgbuhwG-3yb24wfRV5lyx0nkn5YA5JVcFPTyYJa-if24pF7Uztcww4CsMez3RU-6qvhCUhilDQw93BbE_5oMK58DCB6T_pTWYcCTCkAAtkJ1bqDVMIQkvYH3e1osjtyQXl4424ZTZX-cNAQ-smanMhTgml4iHZrZkJulD8aL-AgOycZ957BNzW7rEUX5h8KebNcEx7YvteO5JqkidWDOaVC07KbKDB3CyXIL_gw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇫🇷
👤
واکنش‌طرفداران تیم‌ملی فرانسه وقتی بعد چک کردن وار فکر کردن علیرضا فغانی براشون تو بازی مقابل تیم ملی سنگال پنالتی گرفته ولی...
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.4K · <a href="https://t.me/persiana_Soccer/23891" target="_blank">📅 11:45 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23890">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jylqh1WwZJFS9GybcCz41xdzoVAfNxGLGIk5OZUZRF7N5qJAR9HjRSQLeighG2SVp5obYDb8lw3zvhd01zlLg4XmjTi7Z4kvWxc1t18yk5oFURPVFkotJ7qi8idhdf5Il8YCod-4iIG1sHRTa37OlGQTRpoVTy7uBStqP0OWBznjhHthLn1PT3VDvzzt_bhfTVWeCSw8i9Qxy8pYjbLvGq_qrpWhyQrT8IAF6mJeDq4b8ykdpM5gSaR3BcmNoZ_XY4xDb9v0sPzenQ8_0I3R9T0fAP_bmkZx1zmPrAQmBd-zKa4Qh9qs-Ax9Ilcf3ichVY5Ed6wNJfUBWJshpA-U9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇷
👤
بااعلام‌فابریزیورومانو؛نیمارجونیور ستاره برزیل که به دلیل مصدومیت دیدار با مراکش رو از دست داده بود حالا در حال ریکاوریه اما ‌کادر فنی نخواسته روش ریسک کنه و او رو برای دیدار مقابل تیم ملی هائیتی خط زده که به آمادگی کامل برسه.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.8K · <a href="https://t.me/persiana_Soccer/23890" target="_blank">📅 11:31 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23889">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1f8eb0d50c.mp4?token=tyKWYnk3plTIhZSoGT8T0A-ctDwiF29ZU0mvzliPmWByRLXsllrpmc0okPV7GlubxGXhyUTXSTKQ1tqRqSoQhNeiGbiTZhzTiAwAeimvg4l-gGpIWEBY9XOmJCv_ep17en2DVl0qpE-RPyV86srcXh-0bM2klUybfjFNL4kKVtTfbwDdqMh3mQqxIkj0SbKsiqg19k7gDw5oWz5BUsa16O1Sm7M1R6A0NNotfvlF76Ue2Se3zl75d_8_NKm0S-CyjaPLgQD1V88izoajrzd2BG27lZgy_zKlTvRP-tgZXI4XrLDTa1q64zWvsErU1ULMIfQDhfnUdYIcKfINnGqRfYrhoxU8BiMjT6qlm0j56_vqLdDMq-ISBcuOZrihZHa1dTBh6wgDb5Q5IWxo5GylSwmZZbGMYOAEhdgG0YeLR2VtD2UMmoki4xuBF8NqCdQRjqD9etxfMs2XBkR2aHciyesuL99rnOHIbBpp2EIB50fGrbqYypyEnplz0YjexlnapFq4kQqkZTketXnzx8d8DUgDfhE7sXcvdtGiBZMDXmyjWAfPjuLjw1ofhJ7vKKxGGRdgc03PLn3fL2PXMmp_7TOPBsIW_X-BBhmrvzXvdD6_eLp0Y3B7lDWKMybnIJpEVl6u8bTpJ8QhZzBDNFYOwoqAr0oaAH4dJblJrLHCAoI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1f8eb0d50c.mp4?token=tyKWYnk3plTIhZSoGT8T0A-ctDwiF29ZU0mvzliPmWByRLXsllrpmc0okPV7GlubxGXhyUTXSTKQ1tqRqSoQhNeiGbiTZhzTiAwAeimvg4l-gGpIWEBY9XOmJCv_ep17en2DVl0qpE-RPyV86srcXh-0bM2klUybfjFNL4kKVtTfbwDdqMh3mQqxIkj0SbKsiqg19k7gDw5oWz5BUsa16O1Sm7M1R6A0NNotfvlF76Ue2Se3zl75d_8_NKm0S-CyjaPLgQD1V88izoajrzd2BG27lZgy_zKlTvRP-tgZXI4XrLDTa1q64zWvsErU1ULMIfQDhfnUdYIcKfINnGqRfYrhoxU8BiMjT6qlm0j56_vqLdDMq-ISBcuOZrihZHa1dTBh6wgDb5Q5IWxo5GylSwmZZbGMYOAEhdgG0YeLR2VtD2UMmoki4xuBF8NqCdQRjqD9etxfMs2XBkR2aHciyesuL99rnOHIbBpp2EIB50fGrbqYypyEnplz0YjexlnapFq4kQqkZTketXnzx8d8DUgDfhE7sXcvdtGiBZMDXmyjWAfPjuLjw1ofhJ7vKKxGGRdgc03PLn3fL2PXMmp_7TOPBsIW_X-BBhmrvzXvdD6_eLp0Y3B7lDWKMybnIJpEVl6u8bTpJ8QhZzBDNFYOwoqAr0oaAH4dJblJrLHCAoI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
تماس‌تلفنی امیرحسین‌قیاسی با «سردار آزمون» وسط برنامه بفرماییدجام: من ایـرانی الاصل هستم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.6K · <a href="https://t.me/persiana_Soccer/23889" target="_blank">📅 11:05 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23888">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LE8u8rgwRSBIcuG-gCjWpxufLqrAdrIcWDUhq6A2yBQwUxkxV0VIGOrR76FmmbsKU2hi-6Fn54bS9bYg_v4OwZFYcvE_wDmoRwuXYnVENe0Zyj-Luc_Z-ff-eeFG-ygmJbR8ntxvJv1oCZTTgg261eHVk9VnTp2MIQgYxEcPvrk_35ejRxBWj_HWjxsY2fFXr92fIkV0zzFmu5Ed60zqMqyoZDiiLJutf_4k-qdaodGfDYhBVtiUUZ85xeDsHQXJMBtT953ficpX6F3vGZFkF_P-SLnGCcikpRbirNqpDPeubDBbfEP1Xnlwm-xnFq6xkF5-hwNcnvkf9RyCauKzvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇪
👤
تیبو کورتوا دروازه‌بان تیم ملی بلژیک:
تیم ایران یک مدافع راست‌خطرناک و گلزن به نام رامین رضاییان دارند که زیاد در حملات تیم شرکت می‌کند و ارسال‌های‌دقیقی‌انجام میده بایدمراقبش‌باشیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.8K · <a href="https://t.me/persiana_Soccer/23888" target="_blank">📅 10:38 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23887">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/55029334cb.mp4?token=d6T-6rYv_zk9dM-YZ8BifZ6D3YdG5OWqlGRR5O7ZWh69-uJrJS3p-TRal2TJ_MKYn4blXLbzi3PESzWs0Ip5BphJPP5ICZmvpVnvNTmbiEcHIO7n7auxfffOm0VAXASURNL8LJz4WZrWHRq6XkvVAiHuLKyncqcc_39bar_Xan4_D8cmXxTc4wQeObEA0_LifYi059QBYA7hmN6seeipngfhwQofo6Jfn1lGWA5mSyjV590IGe5AfhioTtdi5uisr172FGPSLF1tWjXHTar3MUYeNmb0Y6XOHH3jmP8f-6aDYQBXfYUWp4mWXDp85jCQ7yJD6bXvppmUfRae-nkrOg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/55029334cb.mp4?token=d6T-6rYv_zk9dM-YZ8BifZ6D3YdG5OWqlGRR5O7ZWh69-uJrJS3p-TRal2TJ_MKYn4blXLbzi3PESzWs0Ip5BphJPP5ICZmvpVnvNTmbiEcHIO7n7auxfffOm0VAXASURNL8LJz4WZrWHRq6XkvVAiHuLKyncqcc_39bar_Xan4_D8cmXxTc4wQeObEA0_LifYi059QBYA7hmN6seeipngfhwQofo6Jfn1lGWA5mSyjV590IGe5AfhioTtdi5uisr172FGPSLF1tWjXHTar3MUYeNmb0Y6XOHH3jmP8f-6aDYQBXfYUWp4mWXDp85jCQ7yJD6bXvppmUfRae-nkrOg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚽️
#فکت
؛گل‌اول‌تیم‌قهرمان‌درجام‌جهانی در 3 دوره اخیر این رقابت از روی نقطه پنالتی به ثمر رسیده.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.3K · <a href="https://t.me/persiana_Soccer/23887" target="_blank">📅 10:38 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23885">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dHM7uZ0aDSRVyvQ_6uy1tC_1PxDCSO9ssdG9qU0tIE0xYDtQunlVct0Z8i95HzYKzXT7eawRKeLqKNDtI4dCDjbf2q8I3fBXgzOxk496JNSewx8y1Fwc6NUcIU87quPRtEQvEXXGcbpAhZ_ZdvaXbh88gKrXTNBR8I8MVY6hYL6a3RgjNiyEUkzg7nhD02TmSj2wwNNgFNGNJLe9nToMP-TuXM7Eq0txmVDQbC9_CBtNojLrHss7sgfGEnr-Uf7CkWQET1aIYMMeqp30vI13LGYgjzl1-aXT0DeDNzgVtAiUxNt2AArrty-lb18rz0KZClmtAg6lC2YHkErJZ6Mrdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛باشگاه‌پرسپولیس بلافاصله بعد از پرداخت مبلغ  توافق شده به باشگاه روبین کازان از کسری طاهری خرید‌جدیدخود رونمایی خواهد کرد.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.6K · <a href="https://t.me/persiana_Soccer/23885" target="_blank">📅 10:03 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23884">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2831c060e3.mp4?token=oUReHOXVz-emPjq61IHNUUq7hBHndyHhNg71m1ozcU7CR5-urd_FRvJGFaJfQojaernOu3CGyw5PFHd9CVg_gUWB1nPMKoYX8AX1cGcnkY1_tRJHRK-dbjZI39nemaZxLKkDdZZk1Gvf2tZBeBzS8hmnC_lwhfbAbMZO3oupcUs3_AcIMU7Hh069JJnK5cq8EA6X87a3UINZ9fp3qIdFkoaG4ijlAfFHQvanawh3MdseXTkFwPCQCj66mAHoR3OM_kAN2oFXbArmtgJY_tcu84-xHhEPKe8435fTEojVoP3CG23NkDJ3Q7iHvxw231B3VxzBTdP86c2Il5gwBgIPpw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2831c060e3.mp4?token=oUReHOXVz-emPjq61IHNUUq7hBHndyHhNg71m1ozcU7CR5-urd_FRvJGFaJfQojaernOu3CGyw5PFHd9CVg_gUWB1nPMKoYX8AX1cGcnkY1_tRJHRK-dbjZI39nemaZxLKkDdZZk1Gvf2tZBeBzS8hmnC_lwhfbAbMZO3oupcUs3_AcIMU7Hh069JJnK5cq8EA6X87a3UINZ9fp3qIdFkoaG4ijlAfFHQvanawh3MdseXTkFwPCQCj66mAHoR3OM_kAN2oFXbArmtgJY_tcu84-xHhEPKe8435fTEojVoP3CG23NkDJ3Q7iHvxw231B3VxzBTdP86c2Il5gwBgIPpw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📹
بعضی حرفاوجملات هستن که ارزش داره روزی چند بار بشنوی؛ جمله‌ای که این داداشمون تو برنامه دیشب ابوطالب گفت واقعا باید با آب طلا نوشتش.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/persiana_Soccer/23884" target="_blank">📅 09:46 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23883">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bOMQzrtPOSibP9xsfD3UBQ4AyDYfHmtgnjVOUEUVhgopu6TFDvVZxeSU5y98hjsDQBYBjloSW6f1K-cfVrKlUpGEI4OETTA26YwXltYvPR6XN6WbkqGnzQpwmdVFk05TBZQEcVPkr4X4De0cMZyucLH2YNocu74TdT55oAyd-o4b0BgtqMGm7ScBcqrRYnsILVWTLitHkreZ_P7nMa7vigD5f5spYS8DR4joBcbek4F9ErZCBwDiR5icT46D9GHZVDxw1CQkFzdlCH5qhudQfPPG4TvsvW2pYBDEuQjU7dlFXJEc4zHDFe-PnJq6YVXCUe9jISyb98_rkYmwYllECg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
یادی‌کنیم‌از واکنش‌کریس‌رونالدو وقتی مسی بعد از کوپا آمریکا 2016 از فوتبال‌ملی خدا حافظی کرد: دیدن مسی درحال‌گریه کردن واقعاً ناراحتم میکنه و امیدوارم به‌تیم‌ملی برگرده چون‌اونا بهش نیاز دارند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/persiana_Soccer/23883" target="_blank">📅 09:22 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23882">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ll-BAvM0O3dIXhASUtrb86AVO6H3nGOESf7BbO7ENUmTlSTZCosrF8g1YuJyG9DOenZIPAGm5xsopH-4WOQ-0yKh4zWLFCkC1EFzyayWa7kTBuj4awwp12WtaD9toQoVLBRI5AyIuDppuGymxpzU6XKjyg7gwUPLCwGZ4lwKWfsR2ZErtB_bZ3swxbHGGty5ILZJ71HuXbTrH_jRHgWUhgSUlyya-D18bPSgECKAAj1joQntWxkYgsm12XoS_NKOK3jUhaxt-bf7B89KZHuJTNjlT_FPjn2NI19xXSGfzJNRX1MOFXnvv7zVqfM2EfcFYSlvPdW_0wd3HJlWx4WmVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
جدول گروه C رقابت های جام جهانی در پایان هفته دوم؛ برزیل سه هیچ هائیتی رو برد و مراکش هم‌با یک گل از سد اسکاتلند گذشت. بازی های هفته اخر بسیار جذاب، مهیج و تماشایی خواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.6K · <a href="https://t.me/persiana_Soccer/23882" target="_blank">📅 09:05 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23880">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l-0DEIeOuiUAuid1lALYWFfkDxhQht4CbPhXx0NQhD13cYQ2qivSqX1UvsA7PrXmj8CYiRU7xj2VbC6BZomFYxVwjHbcdOc8TZdIpd-Xl7yZ5ho3eG4CAtBTORDy_0wfRVwiyJzgEhfJBeNakdtwWbpC_mm4Xe_NTXHOp4qW43eBCXRxRq4Lsj71jMiE1MVdwzTHRHCY9D82xKkB1bYHt-BPQR__NamnqoAo4YUhGK-CdElqp1fots_2x9pFQizZwFtVKCHoL59fPG2fKeKkf-qlf9nIcNyZ3BTjPaQ73OKLxuiYTsBTPPxe3XK9va_YigMappsri38I_TDLfKBK9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج دیدارهای دوم ایران در ادوار مختلف جام جهانی؛ پبروزی دو بد صفر شاگردان کی روش مقابل ولز بهترین نتیجه در هفته های دوم جام جهانی.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.5K · <a href="https://t.me/persiana_Soccer/23880" target="_blank">📅 08:33 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23879">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">📊
جدول گروه C رقابت های جام جهانی در پایان هفته دوم؛ برزیل سه هیچ هائیتی رو برد و مراکش هم‌با یک گل از سد اسکاتلند گذشت. بازی های هفته اخر بسیار جذاب، مهیج و تماشایی خواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.7K · <a href="https://t.me/persiana_Soccer/23879" target="_blank">📅 08:11 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23878">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bL_fCYwYAPv-K45WtJ_8jHrns9CX7uKiyVfLgFL8l9OG8UiK_2lNygPYoVnXJpH-kPxVGF7AVksRJ6bSQApR8Qo8L2HP-oGIk24Xv28VXZVcsKL8G8qMxDaGcOxH01VNUjLsmYWoNPyo-NwsrMTmW3HwAYF238vqPJ2tEwitTEqk2gU4wk-oFz9kTbAZXkc3AEX_55vX_aBzXcyfBYqq3qfDuNu4aiKOaBJH9PKiM1tiqNtsuHPHIWX9yJ89p6o32WMIK6bMmYHegrsHpF6LM5PjFy1UdkyqCpl870_onk-S7x1FFjAv8qbZuwoiBWWnQxQt86ibvromRILrQvWPJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌دیدارهای‌امروز؛ مصاف برزیلی‌ها برابر تیم هائیتی و دوئل تماشایی یاران فن‌دایک vs گیوکرش
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.7K · <a href="https://t.me/persiana_Soccer/23878" target="_blank">📅 07:55 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23875">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZhoKkK4egepkAotYkyotpL1-5_lUVsTb3NNNvTOgrqial2ibSJYALxytgiTE_tIX07GWtJNY9S5JpFY6PBbt5pKsYoEWPkD7CcIsSphD9atqxTvrlp8BvgciT4-rV6CQ8rZFrb8Zsy5ntNX1f3Fb49TCEokmSHx-ucvOJuf-QMa4C7N6sW41OFG9lZnNhA0OkXr58wSpoN3QhQ_LTQ4TYb5owF1YTeGlf4vYNmV3qxUrxtNIIXnU_xmyofYxqUw4rONh8Ua-XjF6K51wSdeuYttzAJMEPx6T5LBvyGFqNibrrGMQIVmnVxIjViaAChfb1ZbXasf_nWj-xqVntk-48Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
قیمت خانه در محله‌های مختلف تهران در سال ۱۳۴۶ چقدر بوده است؟
جالب اینجاست که در متن آگهی ذکر شده مردم قدرت خرید مسکن ندارند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.6K · <a href="https://t.me/persiana_Soccer/23875" target="_blank">📅 01:54 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23874">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MR4e1qVdmps6vucl5kwzhnvMa20Wz1IsCRU_oFG3RZg4kU7aY7b1SdoZ33DJacalabzoj_7rIuRbBSWUlSS4GrQXyD2TPrHJQnsfIhM6lWe1SgcMdfVTtmvu7_9rPUJBaj3jCOlzO3mPd-F7tJkz3LlmVrM-CKJS6WC7ly5c5m2OIVQ6P1oxBO5FGd65xYEisDhpkXA6AaGiVyChBFyKFpE5TLhzxBe5___F7pIvbeDvc0Ac29iSeKsHEKbOUzg40nXi3sBriLfNzuvGTSktR27AA3QaDZvotQP5ECCNEJBuvjHQCLF73QTn4UoGqkfaDTjKJI-t5Wg1UzJVg8IjGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
بانک‌شهر برای دوفصل‌حضور در پرسپولیس آفر 2.2میلیون‌یورویی‌به‌‌دراگان‌ اسکوچیچ داده که مورد قبول سرمربی سابق تیم ملی و باشگاه تراکتور قرار گرفته. حالا تنها مانع راضی کردن اوسمار ویرا برای فسخ قراردادش با سرخپوشان پایتخت است.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 48.6K · <a href="https://t.me/persiana_Soccer/23874" target="_blank">📅 01:48 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23873">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">▶️
قسمت‌‌‌ نهم‌ ویژه‌برنامه‌‌فان‌‌جدید ابوطالب حسینی برای رقابت‌های جام جهانی 2026؛ عالیه حتما ببینید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.3K · <a href="https://t.me/persiana_Soccer/23873" target="_blank">📅 01:28 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23872">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dp5dVUD_Y4wQs2fzNe1XcrqcBv8A_zo5owpoCa-fW5Bps7f1ByTtaJf88bmcoFg-piqu5qYrR-Mu4I5cs8QZz-6L-I8FIPQv6pHgixU3RNbOIR9vjirvc-g53LrxJE7qzVV5NFQ-g1K0N-06goQjnk3FVZgSM7dGneGPnqhdCcbEZxYoDxVQmrbTpbFOj1ODGk412wKA8VSLg5uUbgyor_g23ljHX-wUtFKo2JMF_8hccIDCBrN-AXAmJEOfZBUH7_cgkMRwtyyTv0zzyfGBDyw7mRbpqh9rA9J0Wiu02ufJJ7p0u-YUZzjiYSxRYckxFRV1Dsjj_uGRxBVHPQVNZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
خوزه فلیکس دیاز: رئال مادرید با درخواست نیکو پاز برای‌ حضور در کومو به مدت یک فصل دیگر و بازگشت به رئال درتابستان‌سال‌بعد موافقت کرده.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/persiana_Soccer/23872" target="_blank">📅 01:08 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23871">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vn3stuTXJK4yUFTPD6l7bQlDyXYyN5XySK3RRqJX7zGV6uw8_DVPEwdghRymNNKp8nO7St9fmfc2SDylDbcXCdX6RQqU-xotx846_WQS8LWKpbWKT03XGWnlFio6uTKEhbfGRIiBrcQBevIk2PjGStg_Fp_FWc6oeNaSOqlGu4UdewGse0K19c7vacdwyEZHrBI7lWI8x0SHzAulmt1GDXOUGoqwupGrCupG5_zxKuzHePvYD-zUiQtnvUoCROKJPV-Oz8ic_wCTxmDCWW74xVpchmTT3utXlpZTucbjK8OWqUTF8NmZ_pw57lBNfvxc7ERX5tnFk16SybCDC4bYeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌دیدارهای‌امروز؛
مصاف برزیلی‌ها برابر تیم هائیتی و دوئل تماشایی یاران فن‌دایک vs گیوکرش
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.5K · <a href="https://t.me/persiana_Soccer/23871" target="_blank">📅 01:04 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23870">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UOp1kSNdrRU8TkxJuFjwIdnk1fg3CHQLV25R8f6Ib6KwPmDbAqYbrrWAfxqeAxiKcdmInaXE6c4MqKVyhd0QIVJMIcBzNEmYDFAZnmiua3RSHc5eGG_T0HfVR2zoyedLM9lCuZp2XHe_h0PJ2WMXqGMeJMYJSNK0VUKTQRheUsKPuonm6mRrrjtplZ1jIkhCtPbNBVil8Z68yejaN2XiuwTQrDDE9-p_cj7Z5f56sWl81JeXXfx-RMPoPyDmrr1M0NaE8fJ68tvjEq8-B4zBatC8bkT70G7vGB5ZPfj4PTFzOzydqBmMXmSgnq85Os560nw9X4KXmWC7eyW50aVeSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌‌ دیدارهای‌‌‌ دیروز؛
از باخت سنگین قطری‌ها برابر کانادا تا صعود مکزیک و آمریکا به دور حذفی.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.6K · <a href="https://t.me/persiana_Soccer/23870" target="_blank">📅 01:04 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23868">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">⚽️
ویدیوکامل‌ویژه‌برنامه‌امشب‌عادل‌برای جام جهانی 2026 با حضور اوسمار ویرا سرمربی پرسپولیس.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/persiana_Soccer/23868" target="_blank">📅 00:49 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23867">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EG0nH48TBOU8vahURo25-TQNgDDLS9MA7po4mybQdhCZQDCLleiCcKCZCMkaMZ0Ivy_urgvy_TJr6f-fk_Ih2eIuCJsegxAhaVouifI1uY9ky0txjlLqdzPLVWw1iJXMqeGDE8LzUoteA3NcxJA-egmCi6KggN6aAi8-_NA8raYeM0CML0s6-fEwbTazHly2e5EyyYIRyG6efynUpfjiK6fk_gbvZD-Js-Kwqr-rLBdccbj8U6vSkf_tE9mA26oZ08RDLKEbT9DfnD7nSRrMExoAtVkllNf8DC6-g1OxOPswCz0ePqqLHRrf1cTmhe8-txv3sc5B6HSIk6yFrym7tQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#تکمیلی؛پیروخبر اخیررسانه پرشیانا؛ حالا خبر رسیده که‌مدیریت‌باشگاه‌استقلال برای عقد قرار دادی‌ چهارساله‌با پوریا شهرآبادی مهاجم 20 ساله گل گهر به توافق‌کامل و نهایی رسیده و درصورت توافق بامدیران تیم گل گهر این انتقال انجام خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.3K · <a href="https://t.me/persiana_Soccer/23867" target="_blank">📅 00:45 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23866">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">✅
هفته‌دوم‌جام‌جهانی 2026؛ بعدِ مکزیک، آمریکا دیگر میزبان جام‌جهانی‌دومین پیروزی پیاپی اش رو بدست اورد و قاطعانه راهی مرحله حذفی شد.
😀
استرالیا
0️⃣
-
2️⃣
آمریکا
🇺🇸
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.4K · <a href="https://t.me/persiana_Soccer/23866" target="_blank">📅 00:41 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23865">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C-chB8d70sUo-KtlXQa2_BKAj18yHyW4RT7KYHCSjb_vI7Anp0dxDkI-GlfFhYsUKOWhsh-8L-JA6qEXgmizGDWI8HOLCI8bum91woY6Fe4Ni4-lmTws8kKHvs8MXDB3fNIEiifcdiGMiZpFoytMoleNz_WVDeepMigKf8rg6NApYF0CgSN4ppGqVvA09d53c2lmc2LFfmw9lYHz9wYuUmH4cTNMBwGObK8v7EXX81Obs6C8aqPF45ySCM_r6_Yt091ILrdonMd1jzCXZmenhwlrn7SCrwIV9IKmo6yzj6yMWCXGnv8Hd6Njaz5VHRIWR0qBZP5y-n3I77ftmHHE0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌دوم‌جام‌جهانی 2026
؛ بعدِ مکزیک، آمریکا دیگر میزبان جام‌جهانی‌دومین پیروزی پیاپی اش رو بدست اورد و قاطعانه راهی مرحله حذفی شد.
😀
استرالیا
0️⃣
-
2️⃣
آمریکا
🇺🇸
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.8K · <a href="https://t.me/persiana_Soccer/23865" target="_blank">📅 00:37 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23864">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IhCOWGEtGifP5ZxA4syM23KuHa6Jg9MqGeohxsaKLYHJNiA3aa4jxC76jsebm375z-_5CACA-K20BWH7_8KVbKNYhmWbjR_KXXQx7jZRlqFK5OB2XCuauNIN5E2mxZ3utkNbZdGqCRXsHRl4kgylEJ-AogVVPZLHkImS7lz1jGaTmdgO3JV1y1dO1h3iL3UZ8Fk3m9XpYeuhYL55GV8e88YBgxyNHMwaf-rhu0DmVrlTL-Dhe8Y80QdieQAjBDFpcjb55beA6zAQU5N6UFgGpiVt3QigEgCfFirE_X7xgOFNCxKTHRfzz_iX6UGTxAOXqiq_9IpworhyX8yMcK3ecQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#تکمیلی؛طبق‌شنیده‌های‌رسانه پرشیانا؛ مدیران باشگاه اتحادکلبا امارات اعلام کرده که اماده است که رضایت نامه محمد مهدی محبی وینگر 26 ساله خود را با دریافت 1.2 میلیون یورو صادر کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.8K · <a href="https://t.me/persiana_Soccer/23864" target="_blank">📅 00:10 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23863">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/asqQkqgNHgQxczYaNtNHdS-LPuIM3FMVSF7W9CQ5XaJmFpC4wZVRlNytf9t2jrIzzqmaqsPmR-RRVJf7v05b1RzdmfqujQdjzdYq3OqpXhUpyF-nRleI4bPn3yLBuQCqk6iQfa2J8nwLsB1lSZCZS0-8XcpBpHz32f7UiFU88neeEUn5Vgn2c4BU27I2Nj2bRzf6aALGJiN8Wf_-XnqfTxlRJD7KiNq3sbJGhcI6QYvbO0T_CJHabS2W1x0IGHE91oarpTzn3JNGVVkHJiAVvlv9KYM3AuuvGqoqLDrHNiERjTn1-4RnIcNJsOvIDDTYzTd10l4MyFvHIMBltuKl0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
با اعلام رضایت پرسپولیس، چادرملو و گل‌گهر؛ برگزاری تورنمنت 3 جانبه برای سهمیه آسیایی قطعی شد! و جزییات آن از سوی فدراسیون اعلام میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.8K · <a href="https://t.me/persiana_Soccer/23863" target="_blank">📅 23:27 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23862">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a0mddJCiec_hwoWNL96FEy-MAlLn3gwf0wDaPDmfi4fTQVjMYkYiSGyei4ERW7i5Y8yTkytqMs6wh4sosiO5Qkaxnp52FZ98Rb7u4wYf01dnGZivWbL5oCMoXNU0vnlFM6qvlZVYUmU71BZiFd1rNUVYSiaiG3hi13tBRCGQjnojwHtEPHOEwxvjwTKlVncZLDP-yRUp5OCpyjDp77D__0-8Bwe2R5E62o1-OOblNEc2AHpJUVtAdTVlBgXK8DtX9Sg6V7OhS_8Y6BOdeB86f6SpY6lbOaB1dfDK51U57x_DcZHd0RJFt6BGhqVh-9NQ1lNF7FlhOrO7cBdeGUSSRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مدیران‌دوباشگاه‌چادرملو و گل‌گهر سیرجان امروز به فدراسیون فوتبال اعلام کرده که در هییچ تورنمنت سه گانه‌ای برای تعیین‌تیم راه یافته به سطح دوم لیگ قهرمانان آسیا شرکت نخواهیم‌کرد. مدیرعامل گل‌گهر گفته حق مسلم باشگاه ماست که راهی آسیا شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.7K · <a href="https://t.me/persiana_Soccer/23862" target="_blank">📅 23:10 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23861">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NyLqj1pPsY2HkSk9fsxbSAq0QVOWt_PnnK1TQaPWSaaorolzPsW_IPMVMwoo3zNp8qPvJNMKWzG_fBM5G4znZNO5r7OUvcww5HIUrvl0uSsxs00M-iye6pEvNw7QLeGYcxeW5LZQJYh1YWcrUX4f5yKoh6-E-X2P-yAPE0918Jt9LVYAHYRWeENJX2x4Rsq1VddcThaxH7o2encwuaMsfEz5J3FjgHrbF3bQ6U3AOSV9zZNEQx7tnTVgXEDuosf40V-3fNbOClNVwyRUq5OWsc7HEtYqRbXwUSJa61iGUAiCmg-VDlxnXdtkaIGW9ouwjZ0TEIUu-Q1wEeQRvAgoLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
پرونده‌نقل‌وانتقالات‌تابستانی رئال مادرید با این دوخرید بسته میشه: 220 میلیون یورو برای جذب مایکل اولیسه + 120میلیون‌یورو برای‌جذب انزو.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.6K · <a href="https://t.me/persiana_Soccer/23861" target="_blank">📅 23:10 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23859">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZcDDzAjz8KCeHpEhknkk9w0cFHf9GYqfYp6Zedq8z1l9eqBi9mJ9pectCpAXwVgWr7eWuZY-dRaS4zx7wBAWgZ89IUrm8YmoQqLsIhVhdg_8CXqIEcSrfpQrq3bTbBjak6eDAcqQbfuSyPxZ-mJsEtxEUbGKTo9gilf5JYFC_X1KvoSqxIoU-s7QqsxX8QnPMbR5bFUBrXDMy_hI4kkOqDILOWslTR06Ls3IQjohdoYm1S4eUqoYWfG_lD8zXLvTzqj5IN6sJyJoyum0IhuU9p1FBXxROOAerdNMYuHxF_iuT6890ooeuS9XQdfJ0Rh6LJbdynwIKtDLTKUnhuk4LA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
👤
#تکمیلی؛ طبق اخبار دریافتی پرشیانا؛ مدیریت‌باشگاه استقلال از علیرضا کوشکی وینگر 26 ساله آبی‌هاخواسته‌که هفته‌آتی به همراه محمدحسین اسلامی برای تمدیدقراردادش‌به‌ساختمان‌باشگاه برود. همانطور هم که در روزهای اخیر گفتیم تموم توافقات لازم با مدیر برنامه این…</div>
<div class="tg-footer">👁️ 47.3K · <a href="https://t.me/persiana_Soccer/23859" target="_blank">📅 22:42 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23858">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gC9ZAHTEm34DkXKYhcM_QcSchN_vSwJBcoiW3M7BsvP5p54XrE_qarRj4wOrX3oMqspU_S33rHRwRBuVNlat0wrIfvcHRILOF5KL1IB05c1MOwA2dxxJBIwe27jUZ-DcE32wAVknjRms8zCc8oWxkRUz39G_b8EilYw70z7FMk0DYBF3Q4pchlnO0niuzlGW7GcvshiP7q9m9rvuaWYLPbAod_EdH7Io5mTUBUgbcNV9jp4VzKCfJNkIqj95sDBbujCkc9a8VwdJut1HK9YfbvRM-iX9CGI03ggluhTNDRCs5wPTBZyNEKvrT5xujQiBEscvynM4-5gSk2T1KOhJrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
💣
🔴
#اختصاصی_پرشیانا #فوری؛ رونمایی رسمی از لیست بازیکنان مدنظر اوسمار ویرا برای فصل‌آینده‌پرسپولیس؛ لازم به گفتن است برای هر پست نام دو بازیکن رو به مدیریت باشگاه داده تا اقدام لازگ برای جذب یکیشون انجام شود.
🔴
محمد امین حزباوی و دانیال ایری؛ دفاع وسط.
🔴
آریایوسفی…</div>
<div class="tg-footer">👁️ 47.8K · <a href="https://t.me/persiana_Soccer/23858" target="_blank">📅 22:10 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23857">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v4fRMJqkndEiRnweBONHAPY1DsxhFI-7ZK-7vkG9uVLWOlNhBQOlX6LG35GHACInuhQOn_Nuvo0OLAHaDdrJh8iFQJR1l_Ip6HgIBGSyt60TQwSkgJs4eR1HowdUbqpq63HOSoEPHRCo6KhVLZAXo8AhPDixQZSx-bVs46i78cSdUcqpKxUVNkE1QKbAq8jefFQfwspazBeuWfhR_9h2qa2cmXhMW_3Tufdp1aW3RzJyyUIQszwJGHixS3g6qvCgsbzHod1lBYr2IZ_ejemIqpbSgh3UGVyBUxrcD9N1yf7SI3E7Ruis5c3EL1awkryqVETPmysRCU-BC4UeBJ9iIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مدیران بانک‌شهر معتقدن که پرسپولیس در فصل جدید باتاکتیک‌های‌اوسمار ویرا بجایی نمیرسه و قصد داره توافقی باویرا فسخ‌کنن و سرمربی سابق تراکتور رو به جمع سرخپوشان پایتخت بیاورند. باشگاه بخواد قرارداد اوسمار رو یک‌طرفه‌فسخ‌کنه باید 1.5 میلیون دلار به او پرداخت…</div>
<div class="tg-footer">👁️ 47.9K · <a href="https://t.me/persiana_Soccer/23857" target="_blank">📅 22:03 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23856">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fA9xc3ys0IR1kqBM-Nh1kUO-eBOt7Wk45wpQLpesmq5jLs9KptFF_wgfRkAyRc8ZZ_4c9TYAJyUTmYOs8QrxAUo724dz7oZjwQSwnbtkAMbxzaIK2UcgBQofO-Zd_Rl19EORrAms67vQrAoQhtJo9Vf4diL2eIn8EOGz66ufAVObik3wMMvyxBcJXGYxKE_37KFyyb_rB5cJw18pOeQnFLxBzpwNXVwmghG9_pdfN19RU8tY1RGk1xZVShMMiwKyO1olVcEwf2jA8KbVECVZhNHi_nne9STl-6P0gy8eSQM-ze9eXnFgKNi5zBUQbcKGrk2F9YzCarv2bOyFS0hnGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#فوری؛ نماینده اوسمارویرا در گفتگویی کوتاه با رسانه پرشیانا اعلام‌کردکه اوسمار علاقمند به ادامه‌حضور درباشگاه پرسپولیس است و حتی لیست بازیکنان مدنظر خود رانیز به‌مدیریت داده و اگر اتفاق خاصی از طرف‌مالکان باشگاه رخ ندهد او فصل اینده روی نیمکت سرخپوشان پایتخت…</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/persiana_Soccer/23856" target="_blank">📅 21:56 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23854">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EwwWzkJ4oQjrffu9ASqZH20Ms19bGEgvoV-xtoDiwrIDyTr0H6gsanHOntW5H_wIdYrCM9ls55ZzlQNp6w7pYyPwUMASdex-JMNIiUllN2jVX9z1HomjdhGiYf66O8a9aCeCzhGpYhWyiCbZcLirZ-guiKPAVT5njrAFT9beWt3nPGJKAO3V0OZPXOG4V1FCGHqKu_WpotPBXp93l45l-qjJtJo9HG31sH_XdE2iolL10JAVnhmnCENr6BttlK1qIbN4_Hj01l7Tggf--AeymQ0Cmoo0eaj9VZWOeIeaFFWZqV73n4KLD8BhXs1SOVx8P3tavJVQwoWGgVeBMMIpFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/X3uHD0IzdM9NrS8w42KT50r02Gf5befG56Uh33sjsZ114TvD0m2RgRsU4sxdgvLu0PgNejQTX5EmTzvT46fvdFTtwXn-BQcPdtmBqXAbgadkulFnO5QObgVAg6bvl8ugkk1JyZAz6xqtNqGSDvOIQiXejaAQl_lex7eJogDG4ye9lDJRFwPHUkJUBvR7bbtREG46KwEgPTjbBwAkUpX-Q8Iz5eAqxgxPEP6PIaFl4whNGKGUQxkL2eEuAmu3yrn7PgPkZKZ4mvGj5ZV5m7ch2_Ms2sLprBjUvluSFZa31sQHbhUJdCzfh6jjO4yjswOgkEfVM67xGK78jm3sNaavig.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">⚽️
هفته‌دوم‌جام‌جهانی2026
؛ شماتیک ترکیب دو تیم آمریکا استرالیا؛ ساعت 22:30 از پرشیانا اسپورت؛ هردوتیم‌بازی اولشون رو قاطعانه بردن این مسابقه امشب دیدن داره از دست ندید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/persiana_Soccer/23854" target="_blank">📅 21:21 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23853">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oie1hjYWQMFbFSaY2CMXGleeSuWdB3AKZGQaHgmMnMs_CQRpyqCMNb2jfcrT5eOJgeQe0BoI-Rp8Vo4OYBkaAHDScFCuJfXge6iV_vWc_ArJGp1y9UNsOLqM9wO1-z0FN_gdJYfUEEK3SWCiBZw-l4Q_23IKIcplDWmSKDm1SlJ6Jp58wvYlZgF6rQuC9ksCG902Qde-lWf4Uiqsaci2O-4uoMMApDgzFut-q-U9Mt5cu8-FfJy6b5VA0shsUGpCklVD6-eWfcTzYzLFwbxpIvtCVO3asiKUkiUrE8wbgvibxl0lZxfOfJEbbcWFwMCPMw_0NViQ7txM5iqQ_0g2yw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇦🇷
مارسلو ستاره‌برزیلی‌سابق تیم رئال مادرید: برای هواداران لیونل مسی احترام زیادی قائل هستم اماهرجور حساب میکنم این صحنه واقعا کارت قرمز داشت ولی چون لئو مسی بود چشم پوشی کردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.5K · <a href="https://t.me/persiana_Soccer/23853" target="_blank">📅 21:12 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23852">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WbKAN7hH_y8B0g67BVOMTwpSQ904y_7oiT74hbLJdGfXZTBGiawjsvFE0CzRB4TVAT68D8uKXhCikVGMvzJ4VZVt0h-2-o6MB9Al_Q44HPF4wWHwOd94hjqugZM0DYLziAPdmcdLic3zaDL4jF-_NiC1ZPrw4wFDzIEk-ILD3XANPT7xyU8wJI9gNIqYkGjzDX9M81QLlPy9gOAS8rFKNS4nIRaCChsU7-a3khVQWX3KVcEx8rEBQNb_G-5Gx-Kh5EbzmdfY02cnMWDOBsmryosoWnxeZEmwhRFSZl4Q2kGpoZbpFeNHS6tPaG1DodcnM-JbPaDY7Gy_rbGclM0gpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
سعیدعزت‌اللهی‌بازیکن‌ایران‌باثبت‌حداکثر سرعت ۲۶.۴، پنجمین بازیکن کند هفته اول جام جهانی شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.9K · <a href="https://t.me/persiana_Soccer/23852" target="_blank">📅 20:57 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23851">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7648c46620.mp4?token=v2yQWOfiv1uRYWjZHaJCYZ2UuKQ6iPBNXwC9Uh6J8mFdC9pjYO3c2nvYXla4pBiDFLkVjeYOekJ2vIan5HWPEdxStb5CWO_9b1bAyZquEqfAItqvBhestODyOiPxo4hmY-mQy8brjzJlytRoEkeT6ys2yCA97ciT77kRLLD99gpePnL_SWsBLEVv3CvOrjBXqZRQ9y6VQqulsd1ZcBVjhF0_8SZhe9lG78ZsKemYkpTS6RdTNTvEtuc-PmbNiOAIXuZAFBBUa1L7gI1y4fBKeIfjbFk3rK7ALbcVB7bRm_kx2uk3e-Z40XSvOKQfr45geGSctYSByVpegbF5IW_H4g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7648c46620.mp4?token=v2yQWOfiv1uRYWjZHaJCYZ2UuKQ6iPBNXwC9Uh6J8mFdC9pjYO3c2nvYXla4pBiDFLkVjeYOekJ2vIan5HWPEdxStb5CWO_9b1bAyZquEqfAItqvBhestODyOiPxo4hmY-mQy8brjzJlytRoEkeT6ys2yCA97ciT77kRLLD99gpePnL_SWsBLEVv3CvOrjBXqZRQ9y6VQqulsd1ZcBVjhF0_8SZhe9lG78ZsKemYkpTS6RdTNTvEtuc-PmbNiOAIXuZAFBBUa1L7gI1y4fBKeIfjbFk3rK7ALbcVB7bRm_kx2uk3e-Z40XSvOKQfr45geGSctYSByVpegbF5IW_H4g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
👤
خبر مذاکرات‌ نهایی‌ باشگاه‌استقلال و توافق با محمدجواد حسین نژاد که امروز اکثر رسانه‌ها اون رو کار میکنند. 10 روز پیش اعلام کردیم که باشگاه استقلال اوکی قطعی‌رو از حسین نژاد گرفته و فقط بازشدن‌پنجره و پرداخت‌رضایت‌نامه او باقی مونده.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.2K · <a href="https://t.me/persiana_Soccer/23851" target="_blank">📅 20:28 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23850">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/agdhwKGr9d_z9DrpwRerDPdF1xFalGT1Q334vIQhEHU-Z_ZCqWdY-63rwb7qzpdfIMJeOds-4aJpgbLO-Vs_c8bCwgWlXcWbov1aPCtwSgoVzeKfAmnxcCMFfjC9uzLI02TRIX8i7CHQBYMXkuGahcl3Qv8AKgYq1-P2_Tr66vDFt02LbrcprNnHg7FGK6ZVJghtDJcsrVavAUc7Aq5NBk2-R5SSqcZdHz1B_2i_xsZIIlvcxcuUHhnhK4ut9XWxvmcQ6nyBCQ1yp1cSJww7ywDbB_glyXQ_FbyQEOyc3S9EWo9V7CpRm5h0rn4O1lc2LrvHxRtmisbOzCqRECeFOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇫🇷
🇫🇷
خوزه فلیکس دیاز: بعداز توافق شخصی فلورنتینو پرز با انزو فرناندز؛ کاماوینگا و شوامنی دو گزینه پرز برای جدایی‌از رئال مادریده. شانس جدایی کاماوینگا بیشتراز شوامنی است. درباره فده والورده پرز گفته او فروشی نیس بهش هم فکر کنید.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.2K · <a href="https://t.me/persiana_Soccer/23850" target="_blank">📅 19:54 · 29 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
