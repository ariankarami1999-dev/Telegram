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
<img src="https://cdn4.telesco.pe/file/Y0GVVFWNdl89FFHo9uweoVjy62afyaji048Co82SA5r_v5K1oceFpwZNnIbWMZfYk93Mrw9elDWFwmNZnaEH2vRxTC41jIkRO15q9SJxNhi1t3tFhHF2tReBajTCTeq256ZIWhACnnAbJWWZMFuuyV4E7sbpazD82ZeJeJ0cJ9UJ9EwgFKpoRLPFaYecIliP343BryodvU0w5GHZDnb8XjAMvTuy3QMrJTWGlm_0Pqr01NcZBIaIWfIPa-TrdOQ90mqLWF4dvK04b0KAXUWgn821YVhSlPRiUNfNJnu_bUURogb22qy0Rp7AH9g-yVLk1hWSKFbC8tJB_vj0_LMcIQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 [ Fun HipHop ]</h1>
<p>@funhiphop • 👥 171K عضو</p>
<a href="https://t.me/funhiphop" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 «قدیمی ترین اجتماع فانِ هیپ هاپی»🟡صاحب سبک🟡Tb :@FunHipHopAdsContact :@Chaman_Dar_KhakFollowing Copyright Laws©</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-25 00:14:42</div>
<hr>

<div class="tg-post" id="msg-77910">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZQgfKIG65I1-Gcky4oj2Ode12EaFBaj_XIp6_iRc76KVUII_LWFwqseRU0CX2hEWZFMcQGyz00iNoWlJ6tRNU52yMQv4sYY5_MVBvQnK_WG5jzWliMuOf4BAUTVhKj00hf4WZHlGddKEE12klNZDCAiNI8BAMA9o-adaW0rAKVNAkeGOrxwGZVRuRMR-IJ_cjfwfQi4PJD1s-orru_LxRk0sitf-2xp3bRiYsY5nhrZQZ4VUdj-fo6O57uqkbo-PPcZ-IAu5UoyAFERFv9cOeDJj0vBpcd5Li1xFT6mL4R5TBGW5p1NO7ZhP3hiF8e5edIfsRSgtFloI9Rga0UyYrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">از یه جا به بعد جدی جدی داره تمام تلاشش رو می‌کنه شت پست تولید کنه:
ویکتوریا کواتس از بنیاد هریتیج کاملاً فوق‌العاده است! ممنون ویکتوریا. ایران هرگز سلاح هسته‌ای نخواهد داشت و تنگه هرمز به زودی برای کسب‌وکار باز خواهد شد!!!
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 1.54K · <a href="https://t.me/funhiphop/77910" target="_blank">📅 00:11 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77909">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d0800033b0.mp4?token=CuvgElOHeBvW-E8FJXCYvHdWJTL8LIgwrvA9I7VHIJq6CuuHntIOVzbdOW6KV_Vsh5jvDkbIcuZSwUdiNRsv7NOemeX2pCliOKmgWLlOrz4YzP6ddebVDPJew1x5TcHwxgxnWWoZgjTVXROjX9kgrcPWJdr0NaOrqtIZChiHKjq8uuowBpTDOSkwBblJ1gFmkPpm9JWoVWTGcAOce7OIYPzfqWh7UF_HwBcNJv5dQmb0AGkofWwrIiojEuSZKbrpx9zPoVSXnsYg5tCZ81A2HAY_YQEQxUWpgL-gASXx3gPjovHWiD4H4X0qTQisKYmcAlDioHixEH5CHuPuN2-tYw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d0800033b0.mp4?token=CuvgElOHeBvW-E8FJXCYvHdWJTL8LIgwrvA9I7VHIJq6CuuHntIOVzbdOW6KV_Vsh5jvDkbIcuZSwUdiNRsv7NOemeX2pCliOKmgWLlOrz4YzP6ddebVDPJew1x5TcHwxgxnWWoZgjTVXROjX9kgrcPWJdr0NaOrqtIZChiHKjq8uuowBpTDOSkwBblJ1gFmkPpm9JWoVWTGcAOce7OIYPzfqWh7UF_HwBcNJv5dQmb0AGkofWwrIiojEuSZKbrpx9zPoVSXnsYg5tCZ81A2HAY_YQEQxUWpgL-gASXx3gPjovHWiD4H4X0qTQisKYmcAlDioHixEH5CHuPuN2-tYw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">واکنش بسیار تند باقرشاه به بعضی کارشکنی‌های بعضی افراد در مسیر مثبت و سازنده‌ی مذاکرات.
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 3.38K · <a href="https://t.me/funhiphop/77909" target="_blank">📅 23:58 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77908">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">آدم شخصیت و استایل مربی ژاپن رو میبینه عشق میکنه
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 4.91K · <a href="https://t.me/funhiphop/77908" target="_blank">📅 23:38 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77906">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">کی قراره چنلای فوتبالی تلگرام فارسی از گذاشتن عکس ممه های طرفدارا تیما با کپشن "کاش فلان تیم قهرمان شه" یا "من دیگه طرفدار فلان تیمم" دست بکشن
@FunHipHop
| Menot</div>
<div class="tg-footer">👁️ 6.13K · <a href="https://t.me/funhiphop/77906" target="_blank">📅 23:30 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77905">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">ویویویویوی و عجب دنیایی شده پسر کانال ۱۲ اسرائیل: یک مقام ایرانی اعلام کرد که دونالد ترامپ به ایران پیشنهاد پول در ازای سکوت درباره حمله به بیروت داده است. ایران آن را رد کرده و گفت ما خیلی زود پاسخ خواهیم داد.  مقامات ایرانی همچنین تأکید کردند که «ما برعکس…</div>
<div class="tg-footer">👁️ 6.44K · <a href="https://t.me/funhiphop/77905" target="_blank">📅 23:28 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77904">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">مگه قرار نبود امروز توافق امضا کنن؟
چیشد پس؟
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 6.43K · <a href="https://t.me/funhiphop/77904" target="_blank">📅 23:25 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77903">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ItFAo8Z11BvoLRRCQ2Zbbg1AYbc6uqlHEV0k1d1MU61Y3XtA6JT1QjYKebesIR_c_X_mMyZ5B0s6G2nMncDuSkB2yAVIZV-9SpEfX5l9svehHVH2_4HmWyt7t25sG6KG8LtbAKImr0-ZuvGm99VhJdGtxYzMxSosZuHsIjkEm5gmSIRpYs-m6SQkQmYNsvi3TApXDdgYxALYrn3tNa_4VoRfxYu0-N42Y8SoamNwzl6pkuKlMTOcVS0hclw78Jpc0BlrAOCN9aR5qfA3jF9dwJa-kd5NM8FT8zzYB1Y1TyHIz_N4ekR9FRU0_LVzbC9J6DpzglgYpJ4lKeE008btlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خارکسه تابلو
😂
@FunHipHop | Menot</div>
<div class="tg-footer">👁️ 7.06K · <a href="https://t.me/funhiphop/77903" target="_blank">📅 23:17 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77902">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mKAv58k_eZ1eXZKL_CHCORkswvz4-kPt97YRIwgTSxh0RU2eLYJtob5cww5JZZsuoLsGV0jRDxEky1BE4WounRKh4OfOWA9jgUQCBeM92lay0-KxV-zN58N3MnR1lL5d7rqf8-IEwAyjlUHjUDK7p4p0sCNJ-0djqpb29WhM0arNajq1UNuq53j3q2yJiXhEQaZAir49j8PYI10BIJUYTDXEqUnqC2QENFRwigBpX14aRpbMWWRaP6KM0ZiBbpVDySMpYFDiEMbN2_ziZQT1Nnt0IpqaVWy5-q0Qjxz1-wPezG6dMTcbWlcOUKoUjI2gbwqHDj2uTW0gOycarQ6aYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خارکسه تابلو
😂
@FunHipHop
| Menot</div>
<div class="tg-footer">👁️ 7.28K · <a href="https://t.me/funhiphop/77902" target="_blank">📅 23:12 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77901">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">سخنگوی کمیسیون امنیت ملی مجلس در گفتگویی عمیق و تخصصی با شبکه خبر:
هدف اصلی این نظام نابودی رژیم صهیونیستی تا زودتر از 15 سال آینده است.
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 7.73K · <a href="https://t.me/funhiphop/77901" target="_blank">📅 22:43 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77900">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j4D6WeUkOHod2mlQ8zuBhvRUoQDb5FdMPYC_I60bYlTEY-9Ht-iBybiKQ4n6sd-SRwsv7EMqw4PcTLLTqy63CoSIViNvy4uq_z54MNTqUckvzsDOu7xnCw7b2RTcS84ytT9AwfdvVvGVXclPhAcD7q5rqiDfsHqnVknzpxpUi85K29kvxuHqDaQq8ATEmE78yIjStnNNvJbcdLabH4g8Ekrp_M7fKwT559U_tEeFaCK0yLEqITRbUY8i7k0qZrUPVQs8kUZRSG0m3Bc5T7hbpLc9HBAXq-x6pgbh0cFX4j7SKDYUaSM2GNUXprdFP4-FzyshWe_JAuJ5qUcVewJIwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">باقرشاه عصبانیه:
آنها هرگز نمی‌توانند هیچ بخشی از ارکان مقاومت را تک و تنها گیر بیاورند؛
مجاهدت‌های رزمندگان غیور لبنان و
دیپلماسی مقتدرانه جمهوری اسلامی ایران، حاکمیت و تمامیت ارضی لبنان عزیز را تضمین می‌کند
و بساط دیوانه‌بازی و جنگ‌افروزی رژیم اسرائیل را بر هم خواهد زد،
بچرخ تا بچرخیم.
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 8.22K · <a href="https://t.me/funhiphop/77900" target="_blank">📅 22:37 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77899">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">هفتمی هم زدن  فشار بخور برزیل فن  @FuunHipHop | Farid</div>
<div class="tg-footer">👁️ 8.09K · <a href="https://t.me/funhiphop/77899" target="_blank">📅 22:26 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77898">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">همچین تیمای تخمیی اومدن جام جهانی بعد ژنرال معتقده که تورنمت سخت تر شده
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 7.85K · <a href="https://t.me/funhiphop/77898" target="_blank">📅 22:25 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77897">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">هفتمی هم زدن
فشار بخور برزیل فن
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 8.15K · <a href="https://t.me/funhiphop/77897" target="_blank">📅 22:22 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77896">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">گللل پنجم آلمان  کاراسائو پاره شد   @FuunHipHop | Farid</div>
<div class="tg-footer">👁️ 8.31K · <a href="https://t.me/funhiphop/77896" target="_blank">📅 22:14 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77895">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b73WiSrlAYDOVi6eAFIrKQZOtWh1HYf2llZglN-U2AxeFPG4jbmO6twAAHGI5BcRakalqfq23I3P4x-H1wXj16RhrtNfQNS2z9-shrO1LGkAXUZsG0ZsUMs-s1QspaJX_H_wRxiwSdLVCrjlfFtX5kqQziRsMSeOCQZ6kU4KCEHArDDBlswvtpg37Yg_nZBj-t_KRAk8memRtmRrS_6c8KdL0fsrgzsICU35lzjS5FufFT8IziGmOcKsCNFyYg3nXpOxUs0wcZwWftUXL-tvu1ne1SvY2s7Hi-YQg75WlHHZJl5GLIYIs9UsTiVgkTSwqJY8adgk8b8YvDw41OHc8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تقریبا شامپو شد
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 8.65K · <a href="https://t.me/funhiphop/77895" target="_blank">📅 22:11 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77894">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">گللل پنجم آلمان
کاراسائو پاره شد
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 8.21K · <a href="https://t.me/funhiphop/77894" target="_blank">📅 22:03 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77893">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">باب اسفنجی امروز زودتر فست فودی رو بست، فک کنم یه خبراییه
@FunHipHop
| Menot</div>
<div class="tg-footer">👁️ 8.69K · <a href="https://t.me/funhiphop/77893" target="_blank">📅 21:56 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77892">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">این ترامپ کونکش واقعا ریگان پلاسه</div>
<div class="tg-footer">👁️ 9.01K · <a href="https://t.me/funhiphop/77892" target="_blank">📅 21:52 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77891">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">ویویویویوی  کانال ۱۲ اسرائیل: اسرائیل ارزیابی می‌کند که ترامپ به زودی امتیازی به ایران خواهد داد تا در ازای آن ایران به حمله امروز اسرائیل به بیروت پاسخ ندهد. جزئیات نامشخص است، اما مذاکرات پشت‌پرده در جریان است.  @FuunHipHop | Nima</div>
<div class="tg-footer">👁️ 9.7K · <a href="https://t.me/funhiphop/77891" target="_blank">📅 21:43 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77890">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">گللل چهارم برای آلمان
جمال
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 8.78K · <a href="https://t.me/funhiphop/77890" target="_blank">📅 21:40 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77888">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uSJd7cwGrj_6md7yGWclkehkZJ8vKgdBfErIzos9AWvfNCMTfsuNcbBPBoeOKjm64Is6tSBY0C6AiGKLbXnUqawPr0LJxyF-0pyNfLm1HeSq7MgsC6TA0UsnQgQgLQuIIXzsdR7LxvsAxyIOpttmL70mhB3WaXIrJIeXyMM_YBAE92neFyzS49VObbeIjnlYX2kKTLpkz8ZRKN57BtWYKndKWR7iOrl_gsBRIR4fDIv6lmXD62VCmlkYUT3mk_0KVk7NgrFUnnkIC1kObCAbK6Da0kG-TH_nHs-uXQ5oZj5JSyMd2ABEIgsfS8pcAhARrUIx-LrrWVwWR9mz5wcDtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bae38bd6df.mp4?token=mLUPD4bXsEFmyNvztCpEqhJYdf6_Z9ZCJWuj_DVXBEuAu1ELrbGmmqRF9J9gQD61iXS4niK_PKqPJlDXYuM_PZSuIkZcPlD6drQZkTreIcrT-qBZ0Uxaeqnxk_zb-tlK5jGDlFTfgjf87JxtNUNlRaH342XdOg2iSBZw0Y9hpPFq1DewVq755GigynDv9N6ESb2jNi3IBs0RM4j_prv4K7d_pI6dFEl1pctqPzNWaNH6bsSI8UpagSNQPvL-AET8rdYwi3UPR_OD3aFY9Os9x2XEpJCHGLdCqL6vUHFGfd-0qP28iue0ks2toL4ruLd1FQQsFIMs3HAl6XN2WYk62A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bae38bd6df.mp4?token=mLUPD4bXsEFmyNvztCpEqhJYdf6_Z9ZCJWuj_DVXBEuAu1ELrbGmmqRF9J9gQD61iXS4niK_PKqPJlDXYuM_PZSuIkZcPlD6drQZkTreIcrT-qBZ0Uxaeqnxk_zb-tlK5jGDlFTfgjf87JxtNUNlRaH342XdOg2iSBZw0Y9hpPFq1DewVq755GigynDv9N6ESb2jNi3IBs0RM4j_prv4K7d_pI6dFEl1pctqPzNWaNH6bsSI8UpagSNQPvL-AET8rdYwi3UPR_OD3aFY9Os9x2XEpJCHGLdCqL6vUHFGfd-0qP28iue0ks2toL4ruLd1FQQsFIMs3HAl6XN2WYk62A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کسی که به مرد عنکبوتی یمنی میشناختنش رفته وروی صخره حرکت نمایشی اجرا کرد  موقع اجرای نمایش افتاد ته دره و مرد.
@FunHipHop
| Menot</div>
<div class="tg-footer">👁️ 9.69K · <a href="https://t.me/funhiphop/77888" target="_blank">📅 21:37 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77887">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">گل سوم آلمان
هاورتز
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 8.52K · <a href="https://t.me/funhiphop/77887" target="_blank">📅 21:21 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77886">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">گللل دوم آلمان
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 8.82K · <a href="https://t.me/funhiphop/77886" target="_blank">📅 21:10 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77885">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">ویویویویوی
کانال ۱۲ اسرائیل:
اسرائیل ارزیابی می‌کند که ترامپ به زودی امتیازی به ایران خواهد داد تا در ازای آن ایران به حمله امروز اسرائیل به بیروت پاسخ ندهد.
جزئیات نامشخص است، اما مذاکرات پشت‌پرده در جریان است.
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 9.56K · <a href="https://t.me/funhiphop/77885" target="_blank">📅 21:02 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77884">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">آلمان خورد
🤣
🤣
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 9.4K · <a href="https://t.me/funhiphop/77884" target="_blank">📅 20:53 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77883">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">فرمانده قرارگاه مرکزی خاتم‌الانبیا:
ایده مقدس فتح قدس و اسرائیل و انتقام خون امام شهید هرگز فراموش نخواهد شد؛ ما منتظر کوچک‌ترین لغزش از دشمن متجاوز هستیم تا درس نهایی و فراموش‌نشدنی را به آن‌ها بدهیم.
ما با قاطعیت اعلام می‌کنیم که توانمندی‌های رزمی، دفاعی، موشکی، دریایی، پهپادی و پدافند هوایی ما قوی‌تر از قبل شده و تحت فرمان فرمانده کل قوا، آیت‌الله سید مجتبی حسینی خامنه‌ای؛ خدا سایه‌اش را مستدام بدارد، ارتقا یافته است.
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 9.61K · <a href="https://t.me/funhiphop/77883" target="_blank">📅 20:50 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77882">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">آلمان چه تیم خوبی داره احتمال زیاد از گروهی صعود کنن بعد ۱۲ سال
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 9.37K · <a href="https://t.me/funhiphop/77882" target="_blank">📅 20:40 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77881">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">پشمااام چه گلی زد آلمان
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 9.3K · <a href="https://t.me/funhiphop/77881" target="_blank">📅 20:38 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77880">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">این آخرین نبرده، جلیلی برمیگرده</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/funhiphop/77880" target="_blank">📅 20:22 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77879">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/obg4XmWGsrmBZSCTAWB7bfcZjp3LzvwG_D-jZiz5rhrcUOS0jqCWlMoIFvsx7afvgCewMPWL5NZ3qgKzY2onGQzzvCwxlVcpYHJHGSbKtimI9y5mV3T_Iajn7KvQmlXsaW_PVaw-obpN7XZBZTPeRY21qJzgIVGdA6UeFEvlq2vIl4YnNAxWavvrnbcFiZBQoQ0ZHsqvUkdU0M7zTPoqgFCQNZVt9XaXKxUnHdFZLV6hcK_VSlgnAb5zcO_hj5ktqLIIk2pPRg_C54H9vFziJ9jXGQCfiMV3GvtDP4Sk8__QLce_J9_Rsxr-6H85UBu1vQNlhufvxjaILV-w5jDpXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رئیس کمیسیون امنیت ملی و سیاست خارجی مجلس درمورد میانجیگری ترامپ:
جنایت امروز رژیم صهیونیستی در ضاحیه بیروت بار دیگر ثابت کرد که آمریکا بدون اعتبار ضعیف است، زیرا حتی قادر به کنترل این رژیم غیرقانونی نیست.
پاسخ قوی در راه است.
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/funhiphop/77879" target="_blank">📅 20:06 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77878">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">ت‍       :  امضای توافق امروز به صورت الکترونیکی خواهد بود و پس از یک هفته تفاهم نامه به صورت حضوری در اروپا امضا خواهد شد.   @FuunHipHop | Nima</div>
<div class="tg-footer">👁️ 9.93K · <a href="https://t.me/funhiphop/77878" target="_blank">📅 19:59 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77877">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">خ در ادامه: قرار بود امروز صبح توافقنامه را امضا کنیم، اما حمله اسرائیل به بیروت آن را به تأخیر انداخت. به نتانیاهو گفتم که هیچ حمله‌ی بیشتری در لبنان انجام ندهد و هشدار دادم که این حملات ممکن است معامله را به خطر بیندازد. اصلا چرا بیبی باید چنین حمله لعنتی‌ای…</div>
<div class="tg-footer">👁️ 9.58K · <a href="https://t.me/funhiphop/77877" target="_blank">📅 19:57 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77876">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">تران در ادامه: با وجود حمله اسرائیل به بیروت و تهدید ایران به تلافی توافق امروز نهایی می‌شود. از ایران خواهم خواست پس از حمله اسرائیل به بیروت، با حملات موشکی پاسخ ندهد.  @FuunHipHop | Nima</div>
<div class="tg-footer">👁️ 9.85K · <a href="https://t.me/funhiphop/77876" target="_blank">📅 19:49 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77874">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">ترامپ: توافق ظرف دو تا سه ساعت نهایی می‌شود. حزب الله به ناکجا آباد اسرائیل حمله کرده بود و هیچکس آسیب ندید ولی اسرائیل در جواب به بیروت حمله‌ی بزرگی کرد و این مرا به شدت عصبانی کرد. به نتانیاهو زنگ زدم و به او گفتم لعنتی، داری چکار می‌کنی؟  @FuunHipHop |…</div>
<div class="tg-footer">👁️ 9.36K · <a href="https://t.me/funhiphop/77874" target="_blank">📅 19:46 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77873">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">ترامپ:
توافق ظرف دو تا سه ساعت نهایی می‌شود.
حزب الله به ناکجا آباد اسرائیل حمله کرده بود و هیچکس آسیب ندید ولی اسرائیل در جواب به بیروت حمله‌ی بزرگی کرد و این مرا به شدت عصبانی کرد.
به نتانیاهو زنگ زدم و به او گفتم لعنتی، داری چکار می‌کنی؟
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 9.54K · <a href="https://t.me/funhiphop/77873" target="_blank">📅 19:43 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77872">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">رسمی:
توافق نامه بین ایران و آمریکا توسط ترامپ و علی لاریجانی امضا شد!
پایان جنگ ۲۵ ساله
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/funhiphop/77872" target="_blank">📅 18:54 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77871">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BEeQyR3JujvoZ5H-C6Kxck49_ONhrmXcbJu2c85RFaIaKjxK8aEW4Z123VxPnSrCDISLRRDWPG9i-WUG89bGoAibTPm2_lzM1I_PjATPpJSR8IG6uOAjExNXhvcR3667qJcwcrUVpcFYRytE2AaTy5yNRnDXHei1Q0cjT8AA-pNkwLeAEmruwrUc7p8hyVOBpKaf8yod2i2hIUADs_jJVliz0-EBq8pqVFCM1MrKOOiBym_IvOdR4nAG98IhyVf-FHprA8fBexa_UrPRBswQeJ4_w8bpOdx9vxOCwVlWsyjR1PTSptwwWt_LEzKO4ODiq77RyVLRfdVGu_wkpSq5Jg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بهش گفتم 90 درصد زیبایی دنیا مال توئه
خندید شد 100 درصد.
@Funhiphop
| Jenayi</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/funhiphop/77871" target="_blank">📅 18:48 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77869">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dDHa18KWuhb-Cq5HNjBru3gPcvGBCclQB7RuscHkw9R7TNCh1f3dxgaXIiz9CV8InipZAgvQthMpPM6afOlcCIWzPkmRUMsz84LCqMBM4l04drqp4qIs_k2FrnEtiRd0u5GrZd1Ggl-TAl1lkGMH9mEFer0SBYev5UW2EV23Qdw79lIKoBOTFqAq_H6N2Rs3Pi7KjTF4nwOuQtw6r4RisYV9Uzc4NrAWIQP2yYb6RoHoIZH5L5juq-TaAsqUpfg17f64LsD8EI5dy2j6aH0gOfqdmSK7HkLDzt-Z6dSTChNRw9ebh1Cjn_SFfTiSl2ZqMEVXaFCO-55gcT6IXIudVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YSrPLLV0tcH5Cs2K_xQ3zv4TAC85MdoxGN3ZFsx1D6oUNyOvVrlTvYlKPDGAnORnf-LtHRPdY5IV8yvg88ahfJ_vJFpznlVCwyD3oHVOykLrTSzW5uSCeUSRNDwzXBsXVFlL-OE1BAtyNvNl7AbNPC5LeSGtPBAoBo7HdH7m6uQe9u43BRdeym_e4lbSg6vJp0HBX6fd5giHLrNwqS0K9uejZu9EllLW5uyFvCFivmOgXs3ZYyDr0kfZJhBSU0ddEbTpm6f_Ku81QF6U2YM-eDgiVHkr7o3IktEfdAcA7A9NiIgVtK8jThfLwINwcNk4F3pKJglq4Btea44L64HkUg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">هوادار ترکیه تو بازی صبح امروز با استرالیا :
@Funhiphop
| Jenayi</div>
<div class="tg-footer">👁️ 9.98K · <a href="https://t.me/funhiphop/77869" target="_blank">📅 18:35 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77868">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">با ماف بت از جام جهانی پول در بیار چون کلی هدیه هم خود سایت میده
💵</div>
<div class="tg-footer">👁️ 8.88K · <a href="https://t.me/funhiphop/77868" target="_blank">📅 18:35 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77867">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dyKyL1X3mUU48EQnnyxV_IRHpmTmNU4he1TQxEGQp7mSvPOR7Ei8avzx_YRzBBEOO113ddJc6_ETka9lgDx1MNbiosVNIwJFWAaGAJRXWYVvrF6HwIUX3b1G1RIhMKKpDLzdTaUmsP7nfP5mMNs5Jt2o_UkzHRYK7mtMnC684DxHJXf4FiFNODWRa2e4I8H1DFAiolH6onfNEG5r5V3ziLE_65oWL_8NTrlhxJhmmJX61W-iogSYHhkl1-xRbzU6GSeW1hjGlLN4MXz4HMYKQq6AKhwlSTvoY3T2IUM8_rR-iwcEpuRpL_rQGeRmtfAAmPeNy4g022Oh4yJHo21iDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
چرا سایت بین المللی ماف بت بهترین انتخاب برای پیش بینی جام جهانی
❓
1️⃣
شارژ و برداشت اسان و سریع
2️⃣
پر اپشن ترین سایت فعال در ایران
3️⃣
دارای مجوز رسمی curacao
4️⃣
کارت به کارت همیشه فعال
➖
هدایا بی نظیر ماف بت:
👇
🎁
100% بونوس خوشامدگویی
🎁
برگشت باخت هفتگی
🎁
هر روز 100% فری بت هدیه
🎁
هر روز 20% شارژ اضافی
🎁
گردونه شانس با جوایز بی نظیر
👍
با فعالیت در ماف بت طعم واقعی امکانات در سایت جهانی حس میکنید
👍
🎯
ادرس بدون فیلتر سایت:
✅
https://mafclub.online/fa/?btag=260368
✔️
کانال تلگرام سایت: g24
🅰
🔹
https://t.me/+3Zxs6WU7L_UzY2Fk</div>
<div class="tg-footer">👁️ 9.44K · <a href="https://t.me/funhiphop/77867" target="_blank">📅 18:35 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77866">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p3-bmW1WL1_fn8Wvks-oKWOh51abv7PKDzjGIlgOznO46AqecdbX_px91Hw5F00HYLgWbMS5Wb3CM1AYMU9w1QG7UTGPzFNsF88fl7SjaYEYVo7M8XW1FgtXTsj3cejqr8O1YajcPzOuN60AxPZF75u6BN4H1J_sJ6uSVbfI_1kyh9-0SVDeZuOs6y-hFmQFyXSHRBUm0HpWVUR_hm_XYguJWwxtQ-PGzsDnZy-_YhvUJBQ4hLUhwSFxVkqwelj1z8Oxu1-WQQlkn-T2WoMJyDEgoUJICnj5FxbczrzuMSBrjl1R3Eco0wSIrOIL8mwGRllwtKEDrbY2zcmFAfDEVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ:
حمله امروز صبح به بیروت نباید اتفاق می‌افتاد، به‌ویژه در روز خاصی که ما به توافق صلح با ایران بسیار نزدیک هستیم.
اسرائیل حق دفاع از خود را دارد، اما حمله‌ای که به آن پاسخ داده شد بسیار کوچک و بی‌اهمیت بود، هیچ‌کس آسیب ندید، زخمی نشد یا کشته نشد و نباید این روند مهم را مختل کند.
نباید حملات بیشتری از سوی اسرائیل در هیچ نقطه‌ای از لبنان صورت گیرد، اما همچنین نباید حملات بیشتری از سوی هیچ طرف دیگری، از جمله حزب‌الله، علیه اسرائیل انجام شود.
این می‌تواند آغاز یک صلح طولانی و زیبا باشد — بیایید آن را خراب نکنیم!
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 8.81K · <a href="https://t.me/funhiphop/77866" target="_blank">📅 18:21 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77865">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/emldtZlwY7_C83jQAKMx9PksL-nQRlaxRC0Dd1VaIyoOIKi6-Q9ZbHbYeTlj_2l-1tYSOS0ekuVJ0iEXKg5zlLztE_WejwxIapkhgGrbgPRNHFBlEKxN8qN06MJ1p1B4BY3vgwiNoqRbQKmLcXqLjxJfsq3iOOGNFPchDDu8ZMJAist_Usu_IdmH5mMf3TCK2FP9QqlH5FQc8-L_TFgESYo8dNzQcgD3iwfcSPSmRLa1_2fttmhaid0NwcEyF2b1NOZRYtHN5Zgza-PTmvqq31VQJUEz_3NpNv9nBA_xlHYaYFgpc75WirXAGxvinylDNKD_P13Fn6XVYkrAIm9LLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استوری جدید رضا پیشرو
@Funhiphop
| Jenayi</div>
<div class="tg-footer">👁️ 8.87K · <a href="https://t.me/funhiphop/77865" target="_blank">📅 18:09 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77864">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vF2235Jo6Dxd6LsOUCFNcOTwazRu1xKOYT79o4B9pShLeNvJuwxSTEjxXrac0FFn0W5aJTZ33jSZNuP_0fPOpmAYBoFFt-dm-2sIdD-2gFYATJW0zFZskxGH12oEINSx4OMj7lfvTujUsUny9uYn1csSJda3eyQSFjA4ozbOmpLnMECTefE8Y5JQ3tUTNmnqSoDfyxG7pNpTvrQS0EiNQ9nB1ZSz3SN4ZeyuaNBg9X9j_KlLpHCxCOD2PLISrCtptChmG-MHIeqA_taQkliLwJjj7aS24ouRdNJNCwV6Z-6rPHIP0EM1D9pVMAcztEqLQJS0EX5CXiDDXHgy0Dgb5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فروش ویژه | ارزان و با کیفیت
❤️
🔥
200 گیگ فقط گیگی 2/800 تومان
💵
100 گیگ فقط گیگی 2/990 تومان
💵
50 گیگ فقط گیگی 3/600 تومان
💵
20 گیگ فقط گیگی 4/950 تومان
💵
10 گیگ فقط گیگی 6/000 تومان
💵
بدون ضریب، همراه با لینک ساب
🛡
کیفیت مطلوب، قیمت عالی
🛡
پشتیبانی تا پایان سرویس
🛡
⚡️
جهت خرید از ربات اقدام کنید.
🕶
@Hunter_VpnRobot</div>
<div class="tg-footer">👁️ 9.84K · <a href="https://t.me/funhiphop/77864" target="_blank">📅 18:03 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77863">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">طبق تحلیل‌های بسیار پیچیده و عمیق بنده، سپاه به زودی چند تا موشک از ایران به سمت اسرائیل لانچ می‌کنه، ولی احتمال می‌دم شدت زد و خورد اونقدرا بالا نباشه که بخواد آسیب جدی به مذاکرات بزنه و آتش‌بس هم همچنان برقرار می‌مونه.
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/funhiphop/77863" target="_blank">📅 17:24 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77862">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mGVDNuNckDqoXPAU9NoggrKaed-umXdf_tNc-f6lmd3xw1jr7phTbnBu2w2p9xFl7XBU_ELkgAnQTVLsTXkdJxL3-L9sEc61q9QkYdPSQ9FPvAQTuffnUVZwGdgNirvMsFKKX1b5UhZsLalyvbecqCQYPYN8NNdrb6xUYRT9UaaP33X9byz8xCqnXvZB0_MpLTvtOO0mP5thCioFOE4Ad23QQJ_EvQjnv-gMUqqnxXr4xLONvop7Rhgnjzwb4TIs_WCUWyCR0uQr_kYQQ-mWg0JV0J2TdfdDMBGejLQaT1TZboPHPgUs4tMsQyJF9NIgITnMmMmy6rRVp-1i3oKq9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توئیت جدید باقر شاه
با وجود این شرایط جدی میخوان توافق امضا کنن؟
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/funhiphop/77862" target="_blank">📅 16:13 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77861">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">تا این لحظه خبری از ترور نعیم قاسم منتشر نشده
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/funhiphop/77861" target="_blank">📅 16:00 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77860">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/66e866b19a.mp4?token=n1ezL3EHUynIeKVhsRojpJ7Z1hc9yBjduB6oBnm-eBCBlydIJHCxHWLEeCKn6maHH1O8zDIITXJ92BThY7Y8yUBCv5R6st_ZyWp_cgvILhzPoaErDep58I8pVQygSiy3SjhYW5zempt9RQ9wEY9PHeirz_6JXs8gQpqqi1XZGuhd8qPEqFW4DIlZQVOfkI8C96xByVJPi3Rze1fbNp-Ju_9cIArvgsO4TFVSdBKMYl74XYwRsrHw5WxWT8NcC1SkwZFb-PqOWUSnvtJx9AMKK4dyV5717xkYdrXUn5fFlUIgcY0xjy3sMBYHBQc1fLR_dbKkBywdQhlLNSR5LIEiQA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/66e866b19a.mp4?token=n1ezL3EHUynIeKVhsRojpJ7Z1hc9yBjduB6oBnm-eBCBlydIJHCxHWLEeCKn6maHH1O8zDIITXJ92BThY7Y8yUBCv5R6st_ZyWp_cgvILhzPoaErDep58I8pVQygSiy3SjhYW5zempt9RQ9wEY9PHeirz_6JXs8gQpqqi1XZGuhd8qPEqFW4DIlZQVOfkI8C96xByVJPi3Rze1fbNp-Ju_9cIArvgsO4TFVSdBKMYl74XYwRsrHw5WxWT8NcC1SkwZFb-PqOWUSnvtJx9AMKK4dyV5717xkYdrXUn5fFlUIgcY0xjy3sMBYHBQc1fLR_dbKkBywdQhlLNSR5LIEiQA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پزشکیان:
پیامبر رفت تو یه جنگی؛ لت و پار شد و برگشت
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/funhiphop/77860" target="_blank">📅 14:55 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77859">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">کانال ۱۲ اسرائیل: هدف در حمله به ضاحیه جنوبی نعیم قاسم بوده است
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/funhiphop/77859" target="_blank">📅 14:25 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77858">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">اسرائیل دوباره شروع کرد به گاییدن ضاحیه بیروت
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/funhiphop/77858" target="_blank">📅 14:18 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77857">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dZuAlZJAk8CaLVAGXetCtSEdn8z3IFwLIpGT7_Ylh8cptTtrZwKMcSNxw4KxaBz3yzj1soB1IY814nBy_VvPJRhDp_nF4ElvXAqG5lplyair4flKwHH1J8DcJyP_xKo5DTCwPWbJzcKHh6cwzSWVP7Mol48v5CzAsXBpLQm0Zt9iFL-B2-DALPwsFfDAhbRGIrxbk4eKZGgdzBks6A7XyHPzYxynRzXbrqgb-P4TBB5dLDESbifhcjGyque40u46gRbSV7kbv72Yhy5rK3jWDtm5cghIwg6YYfiXOEaByRnmM1evFP2HBZSI1O0qptu3d2FKAz-WFAQCvAP02ZGzBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/funhiphop/77857" target="_blank">📅 14:11 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77856">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">امتحانات نهایی و کنکور ارشد بخاطر مراسم تشییع جنازه علی خامنه ای یک هفته عقب افتاد
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/funhiphop/77856" target="_blank">📅 13:50 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77855">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">امروز ساعت چند قراره توافقو امضا بزنن؟
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/funhiphop/77855" target="_blank">📅 13:06 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77854">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">دادگاه عالی امریکا ممنوعیت ورود پرچم شیر و‌ خورشید رو که از سوی فیفا به درخواست جمهوری اسلامی اعلام شده بود رو لغو کرد
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/funhiphop/77854" target="_blank">📅 13:01 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77853">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PFbMcCRIroRbRc3oCToOF-bJeKg1N688Gr-rUVGi66qdGDDER-7KHFsuwtoK4z1aXepMSr-vv_sMeuv7aASWZEMrXwhvGfnDpyS8kYnifY43G5xpIBTitKtp5I9Yq-eTpiBhxvZVYyLdAiDMK-dKmkXnjgwx8lWBzms-adojn17Zl5fToIZYtVxHx56U1b4IMn0KXT0kAF26_-FuDhz4yyYKtEhTnqOJP-c61U_6jGk16JllbSP4VVldAlZL_PbkWKZV7Z8FAUheG_BV4g4JFQNaIF5aWxsQ3gtwmYW9QwP0W9EG1fv1cd36kEsaZxr05ZrWEFDxjU1Widl5ivp_GQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">میرباقری(رهبر پایداریچی ها) دستی حزبشو کشید.
@FunHipHop
| Menot</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/funhiphop/77853" target="_blank">📅 12:26 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77851">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/smZ80ilXVKhKP-tuhOXgwcz001UatCqULEkMohCyHb7oNrckDtrj2oUzpz918VCf1FhR6aQNrv6qY4UuCH-HTVop3V69yhX6_6H0XhrNNgtkG0hQMKaYq_nOT5EBhFeiGuHxEsKoNY9rguD-BMEksmRMaqSNnmFI1PgMlfOtfGZC8YVNOxhppeBcuhKW0pKJFbsQOnjk6FVRchJmAnE60dKcaQV3Mhu2-SjR5qChoCa0zYaOD__wx7GsFMDP-6BshrmO7PEf0yJ3Q1yZIcQFQdPn3uuMFCU93Pm4LdJMECA8MkYwSmc3BCa99ui7KDHsqdlfN_NrqjPY4E6K5shPtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/e44HNtJjVcfcjbZdEhBMAc_yQX3hvfanp5L2HYglj2lEwVCItFTYzzoEulXE_njPV168Kt-RKsdydVxc63-g03CluG8g4y1ilT6VebVUqLHpyzB28zaW2UVzj6fSqIOS5uIoYiocya3YGDyNTStA3ym4MU9Do8whNKPq56c2NhXz0x8XkwGA-uaqAcaC65MeUhkxSL9QkEd8RQt12Vym8sYYTAGvBQUHoN65IiE70HeX_OGsUoxZu50mDFfJ24AwW1TMEFvfLBkFDXTeLR24AVMAb18cizYCyKQztZbx5-0Mna9HB5phdbi8LSxaTfYM5iwSvbl_phaci3mxzlO31g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">امروز تولد این دو نفره
🥰
@FuunHipHop
| Jenayi</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/funhiphop/77851" target="_blank">📅 11:38 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77850">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z2V3nYYMScYlFbg819ssWndoUusLwoN1DmDr4B50UtH97CGOZ4d8qj026itEyepD17Pu3Oa2DPQS-we_7OLfDp2E8Th1vDVK1bIZBE9ODRRzDirwywptoXrHUUMQ8vlMgaWrrmqLXSE1wBFWpJNFaqNRQlYFvqKOOuC0r1SUb1Ja99niYU4fZDd0HJcpm9Bt3v5u3DzzMv8OTTKNb_vVCJjhaZ8xEUWxGZZXWYHRC-9PFRj08A280Ie9F_TORWQfTuonZDD0f2GvmQ4Lap_z-VpMULwuLGMw4PgTg53DQ7CBEozO_HPkjHGB8OPzJkGiakxQ_FiPzEZgeSNaeP3D5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جام‌جهانی امسال چقد عجیبه.
@FuunHipHop
| Jenayi</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/funhiphop/77850" target="_blank">📅 11:34 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77849">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">derbybet.apk</div>
  <div class="tg-doc-extra">52 MB</div>
</div>
<a href="https://t.me/funhiphop/77849" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">📲
اپلیکشن رسمی سایت دربی بت
🌐
DerbyBet.com
💰
امکان شارژ ریالی ، ووچر ، کریپتو در کمترین زمان ممکن
🔥
🆔
@DerbyBet</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/funhiphop/77849" target="_blank">📅 11:34 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77848">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fHcaPLHZJYbkCjDEuzCK4DjuE9grngB37ma6vqsn6On-EgaVfUEpZgVlP1AExrxK64bEkd6ywiaBdV38EW5rulGCHNld2LHCgg7Zpey2ev_Iae01ovgOIVE1FfJEwjFYKGBAbMI8vTMNig9raMKMNIAObcAqyDUYvEXf0ndLk0Ml9JcskVPubUo3sqo2cbOHFdiITrGOn7V0SgzT-wi-3se9jTb_-sFFoYISaQNUBAsvmBU527U4irYa3zGppO8BgLHTw9LjunzpeYrGdVO9kXlNCEtCXI11-sYPmdDqujw2-B5vyVV-vWqEIsMSPsV37T-Ew8mRVvoe48RNSvN_pw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
دربی‌بت؛ جایی که پیش‌بینی فقط حدس نیست، شروعِ بردهای واقعیه!
✅
با لایسنس بین‌المللی معتبر، وارد زمینی شو که حرفه‌ای‌ها بازی می‌کنن!
✅
آفرهای خفن ثبت‌نام در دربی‌بت؛ فرصت‌هایی که تکرار نمی‌شن:
⬅️
۱۰۰٪ بونوس اولین واریز؛ شروع انفجاری
⬅️
پشتیبانی کامل از همه ارزهای دیجیتال
⬅️
درگاه ریالی و تومنی امن، سریع
⬅️
برداشت‌های آنی و بدون معطلی
⬅️
پشتیبانی حرفه‌ای ۲۴ ساعته
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _
✅
دربی‌بت؛ بازی کن، ببر، لذت ببر!r24
🅰
✅
https://DerbyBet.com
📩
@Derbybet</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/funhiphop/77848" target="_blank">📅 11:34 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77846">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r_NYd5yUyUl-n0bXclN-n8lbfSdTv-KuXLdZxJlYJDC0UIDa0TtPBfWwVFAWegKywF_IVjGPsVS9703axz3ZfPQ-cmKSRcvw4WPSp618NU-0K0mKL59zS53Hc328KZUkmmPv7wHmhGOkbPaVnhOVCyJv998qp1u-B5FO1JvK2EcT3YU39DuqPgmSErt0efMacLGI_2z4cXYIrgoqAg6wYSnfa-56IiF_jIGvT_1ggZw3r4XQzsCSMg-g9E4DRB4O3vlVhgmjmnUuW-RtvgvFV0N3XD133huqR6iJ2mU3WvqRb6OE7byyf0-t6xraj1yfbIoKnhkjltf5IFXrYWGESA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسمو
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/funhiphop/77846" target="_blank">📅 08:00 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77834">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ab24Ss0ddvfaYbAbbQpDHnxbSXlxnRt9qORiitCpORWxJOxbl9yUsWlCWj9alVrqqBJhTUuvzW_fsWhSuqh1qnAGCzfKb04ics02nndDAXJEoJRoezUmOZ2tfmXwuURjCqmSBWPPCWHWGt401QTLQfKLLnj8rQG2iQ5cNOBrWbs-BFKxGfjkrcMTR4gtzgx8Hse455muwa37g6yT-gRWG130ePA9K52Q6vfO4RI12hVAnQCUmxO60Xro7sT0Cj3sttOkBIR4x0C1ouDwve07DWvS7OOqzq6zNpeyyKcs3SHvekJbrwOb-8B4k6cLQS5bkXU60eeZfy_uB9y8WeXBhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این خارکصده هم باز کسشر پست کرد
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/funhiphop/77834" target="_blank">📅 02:53 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77826">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">گل گل گل</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/funhiphop/77826" target="_blank">📅 02:06 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77824">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">اشرف حکیمی چرا فاز روبرتو کارلوس گرفته</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/funhiphop/77824" target="_blank">📅 02:05 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77823">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">آلیسون یلحظه شد سیدحسین حسینی
این چه خروج کسشری بود
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/funhiphop/77823" target="_blank">📅 01:56 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77822">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">مراکش زددددد
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/funhiphop/77822" target="_blank">📅 01:55 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77821">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">گلللللل</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/funhiphop/77821" target="_blank">📅 01:55 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77818">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sdKe0KFtWGXcJp8BUVoME6ft2aPLdiuTdt2iK1W2H-QBfQCDbLmaesCqq3lyd_w1U1K0BEqpWphsp4SnApY_bLL7ty9oA3bKN8cru7fnJgnSt9TzaIaniJ4JKlAhHMAZSTdNiG0egx1HLsUB7gPqAOb7ihH51aRNV404PVaRWbN7KXG7-sF9eg0xOgXDuCKHeCUGdD8yBX18GMp4cwej68zc3xg3cEXMLa4AdxAb2ft9GxpKs2xF2zHMjOuRoI_-XksWtDFGi_FHsu37fke5T39Uvmpa2wsv1tq6ilFHgS-kGwbV0qEsCIp4YLNjzNQm2pj31n0b20_Q-hRzZU6RGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترکیب برزیل واس بازی امشب
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/funhiphop/77818" target="_blank">📅 01:23 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77809">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">قطر دقیقه نود و پنج گل مساوی رو زد به سوییس.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/funhiphop/77809" target="_blank">📅 00:33 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77808">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">یک مقام ارشد اسرائیلی به ynet:
هدف این توافق این است که زمان و فرصت برای تمام رویدادهای مهمی که اکنون در آمریکا در حال وقوع است، خریداری شود.
این توافق واقعاً چیزی نیست که دوام بیاورد.
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/funhiphop/77808" target="_blank">📅 00:16 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77807">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vLp5p5YE-Bs4KssQa6SiDwmRTc2-vyesqUBraJdgeszTHYRH-HY1UDxl8ipTG8csjR3Vuo0JljEEARcx1ttu3NUBoHn0qKU8HwJBtH2jZUM6RKQOPjF8edvY6EhlfuHpmL3a8n6gGHY_v_MbECuFNHVK4UDPuuoKb7KU2awUvQV-LAYuEzxofkhiSfsmcmaeky1tghwjoQncSO2UurWPo770-d3sZhS5LElVKWGJ05-2G3D5BuuE-1ULpKccx-RMDDIKZe4c5FBj2uJ0djJ8IoizCRa0X1CsswHJYRJtszgCBeLknF-7mSTbuF8ddlmL1s8MG7-JOtm4T9cBw9v-iA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بیانیه ی جدید رهبری در رابطه با مقابله با معترضین اغتشاشگر که دوباره ری پوست شد.
@FunHipHop
| Constantine</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/funhiphop/77807" target="_blank">📅 00:06 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77805">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">من خودم خرداد ماه کف خیابون بودم</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/funhiphop/77805" target="_blank">📅 00:03 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77803">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PnN-KRTxW2am-INVEGpVwkSpZ6rOx_rccBPYHYLoNlOooPI0bOAdXQ4YdaXtEKbtzFd1Jb9o2atxGtTOMklT30brH-BCqgraPnUkofhuU-0_lPpTBoTHZkcrvKnpH0W3iA4yaaCSEYtITvhcg4ObGs-g29nGeVm2Z2bmPWPfFSWUPjqGHngXxtpd5VSlf4hTVVqK-CFFb21fouaPrMQ1WWnJ8-MO_26eP3QvC5J2nK-pwPh2VaBeU5LI8TpkcWX3pmjqTbpJsLlDH8rsmBpbgjpRwtm08VxGckzEaeceCtuprZssjD-v_XA33Wqm8MqZQkmSkj2TDnVeEKc8raQamQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زنده یاد تا آخرین نفس پای رهبرش ایستاد
💔
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/funhiphop/77803" target="_blank">📅 23:57 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77802">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">#سوینا_رضایی جوان معترض ۲۱ ساله در خیابان ستاری تهران  کشته شده به دست نیرو های زحمت کش سپاه پاسداران صدای او باشیم</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/funhiphop/77802" target="_blank">📅 23:53 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77801">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/krr_hrjGM_QulvuKWJYs-1R7bpCp1xD_8B-U09qViLvWBTq5bv8sqoOlSCnH6xwDWGaXFjIpK7vMjsG9DamndRKwVbf5Bw8mNRF0pt_ceQKNcOwWRlb4OE9nr_HxeVvrRX8CC6VWDmaIQPWkbv8X02VAtfscBxnEGN_ZCqTMWsfywQ1tUAnJWBA7bva-bSlbcYfjxnPggZOK4hMo2R7zXrFIHNctY82frrQ8-IwePjhAS0lR1QX3XhfEPAzvk3UkpQpPJqmQutSk971NT3HaaxMGlGzemkkg2ocH_9bdcRth1OKqfbqyOVScQFE54Ipn1b5dAE6VmDQa6FLZO4ch0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#سوینا_رضایی
جوان معترض ۲۱ ساله در خیابان ستاری تهران
کشته شده به دست نیرو های زحمت کش سپاه پاسداران
صدای او باشیم</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/funhiphop/77801" target="_blank">📅 23:52 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77799">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">آقا کجا باید عضو نیروی سرکوب بشم</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/funhiphop/77799" target="_blank">📅 23:48 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77798">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">از نیروی زحمت کش سپاه و بسیج و پایگاه های سرکوب خواستار شلیک مستقیم هستیم
@FunHipHop
| Constantine</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/funhiphop/77798" target="_blank">📅 23:47 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77797">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">منم به این اقتصاد اعتراض دارم
ولی به این نوع اغتشاش هم انتقاد دارم</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/funhiphop/77797" target="_blank">📅 23:46 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77796">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">حجت‌السلام نبویان:
طبق متن توافق، ما مستعمره آمریکا میشیم. آقای عراقچی هرچی آمریکا گفته رو گفته چشم، رد نکرده.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/funhiphop/77796" target="_blank">📅 23:42 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77795">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">این آخرین نبرده، جلیلی برمیگرده</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/funhiphop/77795" target="_blank">📅 23:38 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77794">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">هنوز توافق امضا نشده اوضاع اینطوریه، امضا بشه چی میشه
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/funhiphop/77794" target="_blank">📅 23:34 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77792">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">الاناس عوامل موساد به مردم شلیک کنن</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/funhiphop/77792" target="_blank">📅 23:15 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77790">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">نیروی انتظامی، حمایت حمایت</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/funhiphop/77790" target="_blank">📅 23:10 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77789">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">نیرو های سرکوب وارد خیابونا شدن و اونایی که علیه مذاکرات و قالیباف شعار میدونو سرکوب میکنن
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/funhiphop/77789" target="_blank">📅 23:06 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77788">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">اغتژاژگر را باید بر سر جای خود نژاند
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/funhiphop/77788" target="_blank">📅 23:04 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77787">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6bc96beb56.mp4?token=EtFsZe5h02bHghixz0xwf5zp11pmb7M0IvFIFLBwNvi1n0bqJjRSMf5Gyz5M-MNlqxQnjalg9Fak72zQjmAJkKvSWAnSttqdLiQHIs0YiL6Vr4NACMDpe7j3CLG6aME1lXIWJIweHCNcqp9RRcxGagTU3M8tId8RGrs03XKgPpskx8Q_Hm5qdmARQMiNUwWewu8pz2IHdXiRBP9LkJ2ZOdBR1AbvjPf7Uw8y1Os41baWTf_xsvb2eE6Wn0C68o1ltyTFq4m6NMOUh3XNOE9m4WR6xlMhQe2R3kjljbek7GmxHsbyIQkBA4HCpa7jb9WFWDQKI9sUitFUx3SHAHkhGw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6bc96beb56.mp4?token=EtFsZe5h02bHghixz0xwf5zp11pmb7M0IvFIFLBwNvi1n0bqJjRSMf5Gyz5M-MNlqxQnjalg9Fak72zQjmAJkKvSWAnSttqdLiQHIs0YiL6Vr4NACMDpe7j3CLG6aME1lXIWJIweHCNcqp9RRcxGagTU3M8tId8RGrs03XKgPpskx8Q_Hm5qdmARQMiNUwWewu8pz2IHdXiRBP9LkJ2ZOdBR1AbvjPf7Uw8y1Os41baWTf_xsvb2eE6Wn0C68o1ltyTFq4m6NMOUh3XNOE9m4WR6xlMhQe2R3kjljbek7GmxHsbyIQkBA4HCpa7jb9WFWDQKI9sUitFUx3SHAHkhGw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">باقر شاه در اسفند ۱۴۰۳:
صحبت‌های ترامپ از مذاکره با ایران فریب است و هدف او که آن را امضا کرده خلع سلاح و تسلیم ایران است.
مذاکره با ترامپ به رفع تحریم نخواهد انجامید و نتیجه‌ای جز تحقیر ملت ایران ندارد.
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/funhiphop/77787" target="_blank">📅 22:25 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77786">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/63e89cbdbf.mp4?token=kTYXfqNyhJmvlhUoZPr58vP6DNYBJCokArXHx710sAVw7dNp6G_cRmCT086sNGrJwNAKsFFZcoRjqEmlLTipFUZYp5sRJn1KbW9NtvyMMSc4vJfiUqdakLJbM903HozZullmBFNWKOhr577ACTDwR44hBKzf3YVmdv_xfcYFsmO5pfnOv5JZRBlE5ro2FR3pkgK0zNK-Qu2zdydROi7TyypzFsC9HGxz6JjyJeH8HAsDfAEB12ml6gmVtogUabqerWX1pEqWEAcdYCnif0o3IX-sh9nBnAfP-15xKSzROBR9UdLrC3jN9pHDenaMFN9qEj7XsKrEGmsvcLWcYT_hgQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/63e89cbdbf.mp4?token=kTYXfqNyhJmvlhUoZPr58vP6DNYBJCokArXHx710sAVw7dNp6G_cRmCT086sNGrJwNAKsFFZcoRjqEmlLTipFUZYp5sRJn1KbW9NtvyMMSc4vJfiUqdakLJbM903HozZullmBFNWKOhr577ACTDwR44hBKzf3YVmdv_xfcYFsmO5pfnOv5JZRBlE5ro2FR3pkgK0zNK-Qu2zdydROi7TyypzFsC9HGxz6JjyJeH8HAsDfAEB12ml6gmVtogUabqerWX1pEqWEAcdYCnif0o3IX-sh9nBnAfP-15xKSzROBR9UdLrC3jN9pHDenaMFN9qEj7XsKrEGmsvcLWcYT_hgQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ وقتی جام جهانی تموم بشه
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/funhiphop/77786" target="_blank">📅 22:09 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77785">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3780248517.mp4?token=RapZ4-ZGNGGH-_-jMZdWPVqFRL9bxElRmNWWPNJSmLTfuvYod5-sGr-GHSQ8zYSJTifa2FMEQsLQeQXcF5ycrXcLS8aKc-0rKnoBo6-B72L-YxRlw3kKAvG8A4MTAGap4IHWxhmnOMKwXkDFTy_mV7jh4cCeiPnzUXmDkIOjRMOlGwD-EpN8pTVPLjZd_5CLVB9bgHKvXiUMKA5B1p4dNUxrHfTSkmqVmH5ANorqYP8iEX8TcTRvbBf9SfCAsfg_IOIABi1Hwm4ltUCwvl44J210GOOVioWyI17Mblqn25xoxaMkqsWDJXTykoX6Oe8W5WwfXu8wu7mokYaYI_Hk-w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3780248517.mp4?token=RapZ4-ZGNGGH-_-jMZdWPVqFRL9bxElRmNWWPNJSmLTfuvYod5-sGr-GHSQ8zYSJTifa2FMEQsLQeQXcF5ycrXcLS8aKc-0rKnoBo6-B72L-YxRlw3kKAvG8A4MTAGap4IHWxhmnOMKwXkDFTy_mV7jh4cCeiPnzUXmDkIOjRMOlGwD-EpN8pTVPLjZd_5CLVB9bgHKvXiUMKA5B1p4dNUxrHfTSkmqVmH5ANorqYP8iEX8TcTRvbBf9SfCAsfg_IOIABi1Hwm4ltUCwvl44J210GOOVioWyI17Mblqn25xoxaMkqsWDJXTykoX6Oe8W5WwfXu8wu7mokYaYI_Hk-w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شعار طرفداران جمهوری اسلامی:
مرگ بر عراقچی بیشرف نفوذی
😂
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/funhiphop/77785" target="_blank">📅 21:48 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77784">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">تو تجمعات شبانه از یکی میپرسن کارتون مورد علاقت چیه  @FunHipHop | Constantine</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/funhiphop/77784" target="_blank">📅 21:44 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77783">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">تو تجمعات شبانه از یکی میپرسن کارتون مورد علاقت چیه
@FunHipHop
| Constantine</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/funhiphop/77783" target="_blank">📅 21:43 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77782">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">اگه توافق امضا شد من کونیم
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/funhiphop/77782" target="_blank">📅 21:37 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77781">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromDiscography ship(blue)</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MIaCAiW_59dIwi2977IdzYkEWxcRtI6m70078WfvtKwKRfTfWHKY7SMzm7tj-IhMHNk5p0jmqJp5_r9dIgKrMMXoN216xTlLr0_cKzTFBDOt8acns1En_qeMiKpWY3c6T15PTvrr-9zp6y0GocwFQfRFwYWhoha0lnCntPeuwZYZUDXJY2Gni1yd8Jonu9bsbauM5eLOsC8ewq1_UYkgW84esR0b_pYNCQdL-H_k0USrUZi98vhcMw80OVMlrJ__bVMlzlsMy8WK-YfYWCpn6UL1AEViVqtdGrWSw6PrMLlMYbPTFx7gD9M-CIhmLjIhVmxxnYz0hHIIJaNzh5iDcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Complete Albums Of
Joji
📌
Piss In The Wind (Deluxe
)
📌
Piss In The Wind
📌
Smithereens
📌
Nectar
📌
Ballads 1
📌
In Tongues
Enjoy
🩶
@DiscographyTship</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/funhiphop/77781" target="_blank">📅 21:01 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77780">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">یک سری جاها ظاهرا طرفداران جمهوری اسلامی با نیروی انتظامی درگیر شدن
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/funhiphop/77780" target="_blank">📅 21:00 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77779">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">ترام: فردا تفاهم نامه رو باهاشون امضا می‌کنم تنگه هم بلافاصله بعدش باز می‌شه، امیدوارم توافق نامه نهایی به سرعت پیش بره وگرنه خواهیم دید چه خواهد شد، بر خلاف اوباما (ع) هیچ پولی بهشون نمی‌دم، به زودی هم وقتی اوضاع آروم تر شد می‌ریم باقی مونده مواد هسته‌ای…</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/funhiphop/77779" target="_blank">📅 20:36 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77778">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k8EEUAfCaUxKp4OgC90TJCzw4_RL1JyO0A5SlnIrGSERMcXDLWJtnGxSPSAg_sLd52UVuQTsYnkpgxlYncuwO7yYM1v83F7HFiSWYQ1T91PgppE0CeyHyWM6tePbr3sOcvOHg0r22WuekrNzJm6GMH7-1l6gI6Kmt_z4mIGUA8a8R-iquR98Wdro2ulHK83_xbE9ID-RkBoAP0eqSb8ZJbwJu8LmUxmw1Wh1tnkbc1EpRi7Ec3wkyKfq4X33x3AJuJRr02Es93BBL32bscV4y0-wHljo97UWrwD03sQrKiclpfvzfw1Pmko-2GNyVNNb9bipmZ9Gd_cd_NcsRtzPog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترام:
فردا تفاهم نامه رو باهاشون امضا می‌کنم تنگه هم بلافاصله بعدش باز می‌شه، امیدوارم توافق نامه نهایی به سرعت پیش بره وگرنه خواهیم دید چه خواهد شد، بر خلاف اوباما (ع) هیچ پولی بهشون نمی‌دم، به زودی هم وقتی اوضاع آروم تر شد می‌ریم باقی مونده مواد هسته‌ای رو از ایران جمع می‌کنیم میایم مادر گرامی بنده هم جند
توافق باراک حسین اوباما با ایران، برجام، راهی آسان، زیبا و هموار به سمت سلاح هسته‌ای بود که ایران شش سال پیش می‌توانست داشته باشد و خیلی پیش‌تر از حالا از آن استفاده می‌کرد.
توافق من با ایران کاملاً برعکس است، یک دیوار برای نداشتن سلاح هسته‌ای! در واقع، آنها دیگر خواهان سلاح هسته‌ای نیستند و نه از طریق خرید، توسعه یا هر شکل دیگری از تأمین، چنین سلاحی خواهند داشت.
قرار است این توافق فردا امضا شود و بلافاصله پس از امضا، تنگه هرمز برای همه باز خواهد بود.
روابط ما با ایران بسیار متفاوت و بهتر از دولت‌های قبلی است. برخلاف صدها میلیارد دلار پرداختی اوباما به آنها، از جمله ۱.۷ میلیارد دلار پول نقد سبز و سرد، هیچ پولی رد و بدل نخواهد شد.
در زمان مناسب، وقتی همه چیز آرام باشد، وارد عمل خواهیم شد و گرد و غبار هسته‌ای را که عمیقاً زیر کوه‌های گرانیتی غرق شده و قدرتمند دفن شده است، با کمک بمب‌افکن‌های زیبا و خلبانان درخشان B-2 خود، جمع‌آوری و آن را در ایران یا ایالات متحده پایین‌رده‌بندی و نابود خواهیم کرد.
ما مشتاقانه منتظر همکاری با ایران و کل خاورمیانه در آینده‌ای دور هستیم. امیدواریم این روند به سرعت، آسانی و روانی پیش برود. اگر چنین نشد، ما جایگزین نهایی را داریم که امیدواریم هرگز دوباره استفاده نشود! از توجه شما به این موضوع بسیار سپاسگزاریم!!!
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/funhiphop/77778" target="_blank">📅 20:22 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77777">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jBdC3gs5SbDH4t0XzyMP9De4P5meH7TrqH42fCCEPDlKT0Ft-20fNXA0epLTgprL5gLr39xuyZjTAlqVqOMBqEROWaQqmIpyi2hbfB-m_PZp52y9irIClsEB414sYRFceONysl41pPnFVTxm2TROZaMBi_cdTPngnr_YDyzy0dqAb8i378MfuYdxs77r_TiAzH6ZpOOkCHInJvboyBVFHxKWrVhW8HW-lwQUapa9aLtZeLkoPsXh4O6bS-_BQjY4zFltlm7nbtJxRZ56AMUtHSdI13o7jeA8K2SlNgTNOcAJw-tRSzDXHZ1Uc3TgImwgK5IxHomt8Ci9zb4P68qRdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عجب کاستومی پسر
@FunHipHop
| Constantine</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/funhiphop/77777" target="_blank">📅 19:53 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77776">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/l3-T9OwzVk4lon1gM4MrLRuBjUFXTkCtpsNM1KJoMx6Q4L8AfWvhb_7zbQ6waJlMGoA5pP7u5Q1i1_TMWXZkShW36zeYYZkfFS_tmfzGEdTcRP0gY0T1VIvtHZF58ytznMILj6p4KlT2li1TrM-lWWTWIKvhObrhaOq_8i72at0nmSo1GoGjiFD1fDKHsXr01Q9mXgssy3y1oDeeGwXk-hQK8CNetvzCvfSD4Xaht9CCb1kJyBQJSLFE5AngPJmBGYleafQD2vycLlBEmq6hjegR8nqjiR2WycAhHYueVvImTmQSg8zVVxjTsjGyXCZ54W7OMl0-NMm7alkCHlXJ9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تجمع برخی از طرفداران حکومتی تبریز در اعتراض به توافق با قاتل رهبر شهید.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/funhiphop/77776" target="_blank">📅 18:18 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77775">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">آکسیوس : فردا توافق بین ایران و آمریکا امضا میشه.  @Funhiphop | Jenayi</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/funhiphop/77775" target="_blank">📅 18:14 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77774">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">آکسیوس : فردا توافق بین ایران و آمریکا امضا میشه.
@Funhiphop
| Jenayi</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/funhiphop/77774" target="_blank">📅 18:00 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77773">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qjhFeMwL07_stDEL73O7N7mSy2h5C8pQsvWOLXU2x-C9NMV2L-RzIGvCSdFVRN_Zg4-VIbPqa0qAzwfxCWtIY4OXSHu-KGzv2zHlqWERg8J7kFHiL0fzDisdHHCwUiNRX0O3C7q45w3fbKoDgoR--CDidPq1wrp-VFedh5AiZgZSe9uusul08KCY8svklTEVtemuHpr2lBXJw5dpmgHmc3n_r63jB-85lH4xkhWD1ZcexHWy3GnKj_jOibY2Wtqw-J3AsD5tB0cMRje_Apcr4PwlOcrUYJM3rA9tZoyyX7FQ6dsKVBkg6g0wS4AIGKCg5q7IoLhQ_w83yVZ_Vo5L_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بازی آمریکا پاراگوئه عجب بازی خوبی بود پسر.
@Funhiphop
| Jenayi</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/funhiphop/77773" target="_blank">📅 17:56 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77772">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">با ماف بت از جام جهانی پول در بیار چون کلی هدیه هم خود سایت میده
💵</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/funhiphop/77772" target="_blank">📅 17:56 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77771">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AAf8msAZeHWB5QioyY_PjBmnz-_kcJIRHof4tVPYJjVK0SUSTw9_GXPs4OCGxS_OyL2SKrPlNIuKLk-FvHiwbPdd6t8mjtfuDnersaHwl_lM2eQ0YmZvkK6hSj5AMdtp0DKkGO_c33qRBOowtHq28JXhp8YzbVte_D8nfCF3DW_KvQI7vbumIBelK2q78RNhAGokGnPw_l6kgpkpZ6RJ23q3KDEtlYUUe46EuF3XD4beO2TNw6zxtQFpDMUKjDDEq7WHbbb3qOlh0RVCNLywkGjlm_1WsTVWLHFD2rOnGqMBrt_6Lq1-tEsBgeuYK19ZEPt66kKT4oHHAew32SNWMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
چرا سایت بین المللی ماف بت بهترین انتخاب برای پیش بینی جام جهانی
❓
1️⃣
شارژ و برداشت اسان و سریع
2️⃣
پر اپشن ترین سایت فعال در ایران
3️⃣
دارای مجوز رسمی curacao
4️⃣
کارت به کارت همیشه فعال
➖
هدایا بی نظیر ماف بت:
👇
🎁
100% بونوس خوشامدگویی
🎁
برگشت باخت هفتگی
🎁
هر روز 100% فری بت هدیه
🎁
هر روز 20% شارژ اضافی
🎁
گردونه شانس با جوایز بی نظیر
👍
با فعالیت در ماف بت طعم واقعی امکانات در سایت جهانی حس میکنید
👍
🎯
ادرس بدون فیلتر سایت:
✅
https://mafclub.online/fa/?btag=260368
✔️
کانال تلگرام سایت: g23
🅰
🔹
https://t.me/+3Zxs6WU7L_UzY2Fk</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/funhiphop/77771" target="_blank">📅 17:56 · 23 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
