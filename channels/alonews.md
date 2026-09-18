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
<img src="https://cdn4.telesco.pe/file/CuxB3qD4xcgHGfh9il3yleb8r4qprPRdstAxFEKMFU6nUIdMaduQ_P0BOXdBsSUbhVjoxD7z28pMcZdibA4r8DkDVDqD_rLxBhk414aooVXjYx5n9ZyPtZnwI8pOwfn1qVmii215wahAXn3W23EExHrEFsxycs4E1fOyllr8u0K9zi-FhTULhZYXm2i9Z5ifN0gFVuPxPUeol_9gJYj9223brwghBx3Pis2a7nkOagIPAiNPlt4bTvB1S-4vG91zQnnSMucfiv6G8072OO7TrLQh7y_nop16VRj-ZzzYAx5hhexaU_5ICgclpHYKvJY1fT1FeVbENIxWd6dojW7GLw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 957K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directمالک کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-27 11:00:35</div>
<hr>

<div class="tg-post" id="msg-147983">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gCUofUUG4n7Nnp71Fl2__RfFROzUwP0L5-0t-4pnfVOT7y3oR29K9BIfOiNF16leR-8FnmdWVNNF--JPL8nP3aO2kK_gJ45Jw2O7zFQAexj4rMx6mcWaX8LlT8Jrz_lDxsea6RnISzWhVtXliS5iV2IXBzTS9hLvwMqkl0-KRTcHEceMhqnPtvEtKDipao-RPzaL9B7JjhKlwrfcGrhcSRvzO-f0cHYo6XZkG6ImNACTWjWoYGhFV2Ylb7OTmIzMq3xSIDNd8WUB0ZjfXKKZtCM8cOrh9bXbLpkpfr14Zj0OPqA4vnsMciVY2stw5Rq9b6mNZD90f4wUkL5WayRJBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
عوستاد خوش‌چشم: مطلع میگم، آقا مجتبی تجمعات شبانه رو میبینه
✅
@AloNews</div>
<div class="tg-footer">👁️ 4.09K · <a href="https://t.me/alonews/147983" target="_blank">📅 10:55 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147982">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">👈
الشرق‌الأوسط: لبنان در حال بررسی گسترش «منطقه آزمایشی» برای دربرگرفتن تپه‌های علی طاهر و شهرک‌های اطراف آن است
🔴
همزمان، قرار است با حمایت آمریکا یک پست دیده‌بانی بین‌المللی ایجاد شود و استقرار ارتش لبنان نیز در این مناطق انجام گیرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 7.17K · <a href="https://t.me/alonews/147982" target="_blank">📅 10:49 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147981">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">👈
ترامپ و صدراعظم آلمان درباره تنگه هرمز و دریای سرخ گفت‌و‌گو کردند / برلین:
🔴
این توافق وجود دارد که این دو آبراه باید سریعا بازگشایی شوند
🔴
فریدریش مرتس صدراعظم آلمان و دونالد ترامپ رئیس جمهور آمریکا در تماسی تلفنی درباره جنگ در اوکراین و تحولات تنگه هرمز و دریای سرخ گفت‌وگو کردند
✅
@AloNews</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/alonews/147981" target="_blank">📅 10:44 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147980">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🔴
تا ماه بعد وضعیت طلا چجوریه؟</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/alonews/147980" target="_blank">📅 10:41 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147979">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZgtWUYrgB27Vtf8RvHbUOBG4K5CK_-lXikOkGfmNjpXF2laEbZY-diY-pMnSimQ7yddoDecOsWe4Z9GoSX96vJ9NUwRxQb0vsbxQlboXBs5906C2k4cFNSqeXzNQIp7b1nP65PqoQg--g7boDY7CN5wbsAV3Y_8IAWg6cJ6c7R1N4jC4R2Jlu3ArbNGqXHpDHNoVX5cUNgvfxLH4NUWwozZCKAkrvhAjfFh33_d2QGUIe2wO-buLoNs51ByvX5bNxrOFfph_t_8XEFoJP13juZJ1USPnvsyoI9LyfrKjiGfxZDxIzbwFLRpc8LoDjHd-qnmDrSMcz6VnNMdwLhBcqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نیروهای یمنی، سلسلة کوه‌های "الأغبرة" را که از نظر استراتژیک اهمیت دارد، در منطقه "المضاربة" واقع در استان "لحج" تصرف کردند
✅
@AloNews</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/alonews/147979" target="_blank">📅 10:39 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147978">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">👈
آمریکا رسماً از شورای حقوق بشر سازمان ملل خارج شد!
🔴
وزارت خارجه آمریکا این شورا را متهم کرده که به ترویج آنچه «ادبیات ضد آمریکایی» خوانده می‌شود، می‌پردازد و در برابر رژیم‌هایی که به سرکوب مردم متهم هستند، رویکردی مماشات‌گرانه دارد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/alonews/147978" target="_blank">📅 10:34 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147977">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">👈
ان‌بی‌سی نیوز به نقل از مقامات رسمی:
پنتاگون در حال بررسی طرحی برای خروج حدود یک سوم نیروهای آمریکایی از اروپا، شامل ۲۵ هزار نیرو، هواپیماها، کشتی‌ها و تسلیحات است
✅
@AloNews</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/alonews/147977" target="_blank">📅 10:31 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147976">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو توئیت | AloTweet</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B2xAo7rRU8XVyCXhqbI4QMTbrIMBFnH1eQPsxyrDPRVjRzfbc3n0dm7K5WjN8a9vLGn1Kp1Q-UHxKWwE6hbSi8rmISdNcTlNbxgFWJWGkJnxhzDefnBo4EhXkI6eESog1567PKf6gq9FpKnVW4VNBj2T99oH11C2cNcdcf7LhQH9VgKzZH8Dps3RWBJQkppLTmId1G95_YVBMuH9-PtxG5QyP2KmrkgWTxDoy1b2S5PjBxKq-ULFOvMYEUGjF2xfgS1UnQQ2vO5E7iZ8EusIo8KTv2uG9SiDnOJmViyEZIlJU-UBTNsHzID94FN2u4owwYT_7cxUodtqJcj6bqA-7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امروز ۱۸ سپتامبر، روز جهانی خایمالاس
این روز رو به دوست خایمالت تبریک بگو
[تصویر تزئینی هست]
[
@AloTweet
]</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/alonews/147976" target="_blank">📅 10:11 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147973">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/E9h-ibu4bO3Q1bTLMGDzA942HbOJdRveZiI7ZYMOUiMMwwl7_dToEzAUjJhlS3v7NzLppfHVkALSsPjEIirp0ALkA9ax0cZxM8JXMLMlNZXXM7WD-oKPocuzjhjuxj04v1ji69zkPpGXZVlmVSeTqujVghJ4qPDMZsUwtEgsdkInU_f6_x8NnoaL44a0ikTzKN_MEm0zIGQQPzst6q5n0UWchMeXplBwI7ShN4UobvYUKze6yvIYJN7q2fJ8Anobhiv-YgQjMUKIIpoRfWHbI1kkQoicFnVQPSwqIWEwwGdVJ4YL89cV-O3MmFGUTB63iZlHa0d7tpWGkA5FwQKTYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/I8sJxwn9hJlQudyItEqQ5qV1Fcb9sVh6gyvcU7hk0kWJjWd9uwmVtLAC94n9r3TPrydkeX3RID1RhytHF2HCv1wulHGk54cDnZvT6O1qykTwQ21WmgDUEmgdg7m0CoH12ZFBiZ0VWHyuLNV2ffMQR0O7urxKrq-d0kjXSg_TAcBoAZt2MUFTHewmIN7wkKjRbh7CCNn27N9HUl0IBnnUAvkrxwGMvwmgXXcLAo4Ye0sT9OlXoKCbsCya6AFa-zE598c8S2MoYzbqua0QQjIJEpe_Os0p_RynipAYER_3wWR0DrzQRnOe_moF94chFZ_74fYC2BikWIj6jGzOrPJlYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZdCMt1YGH1-y0QIA4PZYVAy6YTeVXIainXZwxdAG_iIDsSbfLi1LmtXEeOJ2JSqNJGhDB7cb_pIjsrA97Mh-ObP1d6JZs0Bffty_hIuttutFbWc_OdcT_91rFrhNrN8KoHzEog712FAWCSjE9KiUhHTiqVzAFj8C3Jv50uAb7jY8KUkl938lEqLnGlX988Di7AuZg3PNOjfN3S0wv44sTaFZGP3NW7sVe-Hbvk2v7NcFicxvyoRpi2tzgHR-EUDoxCIqJLUq8Lxwe9xYEwSfhRlOuiIGuGhgTlydJvhYvr9FdzDeZ5DruQAYpNa6wLL8iChNaFN5-IHi-Rudac06tg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
انتقال تجهیزات نظامی آمریکا از عراق به اردن
✅
@AloNews</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/alonews/147973" target="_blank">📅 10:10 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147972">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">👈
مقام سازمان ملل:جنگ آمریکا و ایران در ماه اول، ۱۵۰ میلیارد دلار به اقتصادهای عربی خسارت زد
🔴
این خسارات معادل حدود ۴ درصد از تولید ناخالص داخلی منطقه است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/alonews/147972" target="_blank">📅 10:03 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147971">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/00fa97a9a0.mp4?token=XtdN2LZuASuyjBBBCh9AvAlySQPvdpIPEF1_GjemZKYvfsVHi-iAzyxTyXCW1nHW4Czf2Mhl8kxKLusIp6glxtp1utCV9ed6fsovvkDRsR9NZ0bBaVBSqkiYCsOzkDlqtfFcRY7lp6d2mUbUd8M5k7AJ-S6DDFgpEPNUlBlQrw89DGhiA44QD4nZ3-YwAbtYOhCAU5cAiWGREB6wd0blgS4tiMhmj5EaPD9c0JImWybgSbRn4jsXcKFCSpCV-TK2bLIdCXy3WnvgIXxUAFR-fqSJO5vn01PRCuk2ppoKoJ5qCAgXS2U17M_UXFw9fHrNO2JA8ai4WLxu4ld1gMZVTYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/00fa97a9a0.mp4?token=XtdN2LZuASuyjBBBCh9AvAlySQPvdpIPEF1_GjemZKYvfsVHi-iAzyxTyXCW1nHW4Czf2Mhl8kxKLusIp6glxtp1utCV9ed6fsovvkDRsR9NZ0bBaVBSqkiYCsOzkDlqtfFcRY7lp6d2mUbUd8M5k7AJ-S6DDFgpEPNUlBlQrw89DGhiA44QD4nZ3-YwAbtYOhCAU5cAiWGREB6wd0blgS4tiMhmj5EaPD9c0JImWybgSbRn4jsXcKFCSpCV-TK2bLIdCXy3WnvgIXxUAFR-fqSJO5vn01PRCuk2ppoKoJ5qCAgXS2U17M_UXFw9fHrNO2JA8ai4WLxu4ld1gMZVTYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
سخنگوی ارتش پاکستان: تا هر سطحی از عربستان دفاع می‌کنیم
🔴
ژنرال احمد شریف چودری، سخنگوی ارتش پاکستان، گفت اسلام‌آباد در برابر حملات موشکی و پهپادی حوثی‌ها به عربستان سعودی، از این کشور «تا هر سطحی» دفاع خواهد کرد.
🔴
«پاکستان کاملا در کنار پادشاهی عربستان سعودی ایستاده است؛ هم از نظر دیپلماتیک و هم از نظر عملی. ما تا هر سطحی پیش خواهیم رفت.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/alonews/147971" target="_blank">📅 09:54 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147970">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">👈
رئیس‌جمهور کره جنوبی، لی جائه میونگ، گفته است که سئول تجهیزات نظامی را به خاورمیانه یا تنگه هرمز اعزام نخواهد کرد، مگر اینکه این اقدام خطر وارد شدن کره جنوبی به جنگ با جمهوری اسلامی را به همراه داشته باشد.
🔴
با این حال، دولت او در حال بررسی امکان گسترش نقش کره جنوبی در حفاظت از کشتیرانی در تنگه هرمز است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/alonews/147970" target="_blank">📅 09:48 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147969">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">👈
صداوسیما: هر شب بالای ۶۵ میلیون بیننده داریم
✅
@AloNews</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/alonews/147969" target="_blank">📅 09:43 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147968">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">👈
مشاور ارشد ترامپ درباره تلاش برای پایان دادن به جنگ با ایران
🔴
مسعد بولس مشاور ارشد رئیس جمهور آمریکا در امور کشورهای عربی و خاور میانه مدعی شد که دونالد ترامپ برای پایان دادن به جنگ با ایران تلاش می‌کند.
🔴
برآورد رئیس جمهور آمریکا این است که جنگ شعله ور شده در سراسر خاورمیانه به زودی پایان یابد و وی برای تحقق این موضوع تلاش می‌کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/alonews/147968" target="_blank">📅 09:38 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147967">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">👈
ادامه روند نزولی قیمت نفت برای سومین روز متوالی
🔴
قیمت طلای سیاه همچنان بالای سطح ۱۰۰ دلار باقی ماند
✅
@AloNews</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/alonews/147967" target="_blank">📅 09:34 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147966">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">👈
الجزیره: داده‌های اولیه نشان می‌دهد که تنها ۴ کشتی باری در روز پنجشنبه از تنگه هرمز عبور کرده‌اند که نسبت به ۶ کشتی در روز قبل از آن، کاهش یافته و بسیار کمتر از میانگین ثبت‌شده در ده روز گذشته (حدود ۱۶ کشتی) است
✅
@AloNews</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/alonews/147966" target="_blank">📅 09:16 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147965">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">👈
یک مقام سعودی در قبال تحولات یمن در گفت‌وگو با شبکه ۱۲ تلویزیون اسرائیل: ترکیه و پاکستان هیچ کمکی نکردند، آن‌ها فقط می‌خواهند سلاح بفروشند
🔴
«از سوی پاکستان یا ترکیه چیزی جز اظهارات نرسیده و هیچ همکاری‌ای صورت نگرفته است. آنها فقط می‌خواهند سلاح بفروشند.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 33K · <a href="https://t.me/alonews/147965" target="_blank">📅 09:12 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147964">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">👈
رادیو اروپای آزاد/رادیو آزادی (RFE/RL) گزارش داد دونالد ترامپ ممکن است از فردا قانون «تحریم روسیه و ایران لیندسی گراهام» را امضا کند.
🔴
این لایحه پیش‌تر برای امضای رئیس‌ جمهور به کاخ سفید ارسال شده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 33.3K · <a href="https://t.me/alonews/147964" target="_blank">📅 09:08 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147963">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LWblYq7-nXV5Fdiwq4HPxdZb11qeqZaLTSlzZXNsNnocwddfpaORiR5BnCuiuQgj77OaUmb8TF0rfnhy5U6PmpDGhmRJnAE4u6iJjXMnHpwEsOzB_TKpceh3HD1fE6FOOsUvwpx35BC9bTFFNR0NUjOuWMx9HQnk0hCltvWLFzbadIscJPl2SDPWKdIsjKyEAOlv19ZT26VfLFtgnMnImFtfK5ZDR4lrX7HC2evadcHX0ocULMgxg2MAKtArwb4r3tzUNCyDx4CWLwbnc3wWl5o6Uh--GunUEvYt43BN2q2T8a-363xCP0GTgkSlFS8fnuNvuVP5W7pafyL2h1r5Xw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نوسان قیمت نفت برنت در ساعات اخیر
✅
@AloNews</div>
<div class="tg-footer">👁️ 33.4K · <a href="https://t.me/alonews/147963" target="_blank">📅 09:04 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147962">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">👈
نظرسنجی شبکه فاکس‌نیوز:
اکثریت رای‌دهندگان آمریکایی معتقدند ترامپ استراتژی برای پایان دادن به جنگ با ایران ندارد
🔴
۶۰ درصد نیز اقدام نظامی آمریکا علیه ایران را تصمیمی اشتباه می‌دانند ‌
✅
@AloNews</div>
<div class="tg-footer">👁️ 34.6K · <a href="https://t.me/alonews/147962" target="_blank">📅 08:59 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147961">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0bff9339b7.mp4?token=u_fIZoOjZq5J646TvSAEb89dOqTSGcgP7RENTSxauqxnpMXVp-xuEwduPyc9LrCgOHwQFtismY6x74BE5dvX0Jb8iZtGtrdSR0ySHhXqis-TJwhSPMeg_LKQjFUz2XJwtZYylq7JApAPp77UAnGzw6ZkIv9J6mbY-c5aFopJMTBITEmPqqECaSbMUUXYq6X31VR8FxZ-EPFzF4B6j_OqEEfMyMkv2S7xWK7vDESdppe_ufgzUCdwepDK5zKeQGIEHVIc3amWNP97cxG8gBF3gvujVcF12TJ_oIfCJ6GSFqJsSZyYycPpaFug6QgSLGLx3yo0jFiKHyn4iHnRKnAQBg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0bff9339b7.mp4?token=u_fIZoOjZq5J646TvSAEb89dOqTSGcgP7RENTSxauqxnpMXVp-xuEwduPyc9LrCgOHwQFtismY6x74BE5dvX0Jb8iZtGtrdSR0ySHhXqis-TJwhSPMeg_LKQjFUz2XJwtZYylq7JApAPp77UAnGzw6ZkIv9J6mbY-c5aFopJMTBITEmPqqECaSbMUUXYq6X31VR8FxZ-EPFzF4B6j_OqEEfMyMkv2S7xWK7vDESdppe_ufgzUCdwepDK5zKeQGIEHVIc3amWNP97cxG8gBF3gvujVcF12TJ_oIfCJ6GSFqJsSZyYycPpaFug6QgSLGLx3yo0jFiKHyn4iHnRKnAQBg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پرزیدنت ترامپ درباره جمهوري اسلامي ایران:
هر جا را در جهان نگاه کنید، ایران به عنوان بدترین کشور جهان شناخته می‌شود و مدت طولانی است که این‌گونه بوده است.
ما کار را انجام خواهیم داد. آن‌ها در وضعیت بسیار ضعیفی قرار دارند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 41.2K · <a href="https://t.me/alonews/147961" target="_blank">📅 08:18 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147960">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">👈
دونالد ترامپ، رئیس‌جمهور آمریکا:
«
اگر ایران بخواهد به توافق برسد، از نظر من هنوز آماده نیست. ما یا به توافقی می‌رسیم که توافق خوبی باشد، یا اصلاً توافقی نخواهیم داشت
.
🔴
ما پیشاپیش توانایی آنها برای دستیابی به یک موشک هسته‌ای را از بین برده‌ایم. اگر ما از بمب‌افکن‌های B-2 خود استفاده نکرده بودیم، الان ایرانی داشتیم که سلاح هسته‌ای در اختیار داشت و آنها خیلی راحت از آن استفاده می‌کردند.
🔴
ما به کارمان رسیدگی خواهیم کرد، ما... آنها در وضعیت بسیار ضعیفی قرار دارند.
🔴
ما کنترل تنگه هرمز را در دست داریم؛ به‌طور کامل و قدرتمندانه آن را کنترل می‌کنیم. ما هر شب، معمولاً در طول شب، تعداد زیادی کشتی را هدف قرار می‌دهیم، چون آنها در شب نمی‌توانند چیزی ببینند.
🔴
آنها می‌دانند که ما آنجا هستیم، اما نمی‌توانند چیزی ببینند، چون ما رادارهایشان را نابود کرده‌ایم. آنها هیچ نوع... دیدی در شب ندارند.
🔴
اما ما عملکرد بسیار خوبی داریم و فکر می‌کنم آنها در وضعیت فروپاشی قرار دارند.
🔴
می‌دانید، اقتصاد آنها در حال حاضر در سطحی قرار دارد که هرگز پیش از این ندیده‌اند؛ بدترین وضعیت اقتصادی‌ای است که تا به حال داشته‌اند.
🔴
آنها تورمی بیش از ۳۰۰ درصد دارند. آنها کاملاً به‌هم‌ریخته‌اند. ببینیم چه اتفاقی می‌افتد.
🔴
فکر می‌کنم در نهایت پیروز خواهیم شد. نمی‌دانم از طریق توافق خواهد بود یا نه، اما ما همین حالا هم در حال پیروز شدن هستیم و فکر می‌کنم در نهایت پیروز خواهیم شد.»
﻿
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.4K · <a href="https://t.me/alonews/147960" target="_blank">📅 03:21 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147959">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/411c3a472b.mp4?token=vNzdMidmyt51kdbpqFxTldgkVvJxPBeYi9gtnKpMLYLGfFQJ4y66rMkkP4zP5NyQVhPte3b7nFfSMZA65D5nbwXtQVVdHPUGf_u4s5bRyej4ma08WXBeBi4pqrQIoMdrJ-rzDa-tPOqgmKl0kgBkE9K_sEqlfbNl6QesoFf9sQeWqqGtNe32KN6tFgYbc6sBhTygiU6tWzdbKmwOUa7ro9OPqVMWJqT6nKVcnKAor5zSpzhutObtQQiv5j_ZndUZS9eWKEBwq8z0fznQY5K7_2Lrx2qtbdx3tx_MzXzfXs-b5PAJ4YOZ6EY_0mUJOmAYlsxbM1l7MQvAevFPYVFJ1y38mUV_bXNXT-l4q_76nTKhbmFWk8AYgKwMVmLkqLl6ZRI-2q4AX_j2zSx_fbssk7wNaELAceN687Cp8hQ20S24Z0KDCTEB17iIAs0n_f80WzwOVWvSAR1NUdQQFuc77RQ-gjrp9-yxmUtzoDJWTVSfxULNcKuhhRTu9pzhHkQ_0lu_I3Js-Z5VjohC_tkQJJI-yjOlb1YeP-V6nlwW73HJMCH8cA2ptHe2izDmB4lluHpy33Hux3vhD4iKN_OaveNR-VsBiIb3JX4BaDo7vuWOhXEFxGUfmb3RmV2CcsZ5zSLayXrCbT5mZlu1-wbAJQHcB5K8S8nbaaoV07g7jyM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/411c3a472b.mp4?token=vNzdMidmyt51kdbpqFxTldgkVvJxPBeYi9gtnKpMLYLGfFQJ4y66rMkkP4zP5NyQVhPte3b7nFfSMZA65D5nbwXtQVVdHPUGf_u4s5bRyej4ma08WXBeBi4pqrQIoMdrJ-rzDa-tPOqgmKl0kgBkE9K_sEqlfbNl6QesoFf9sQeWqqGtNe32KN6tFgYbc6sBhTygiU6tWzdbKmwOUa7ro9OPqVMWJqT6nKVcnKAor5zSpzhutObtQQiv5j_ZndUZS9eWKEBwq8z0fznQY5K7_2Lrx2qtbdx3tx_MzXzfXs-b5PAJ4YOZ6EY_0mUJOmAYlsxbM1l7MQvAevFPYVFJ1y38mUV_bXNXT-l4q_76nTKhbmFWk8AYgKwMVmLkqLl6ZRI-2q4AX_j2zSx_fbssk7wNaELAceN687Cp8hQ20S24Z0KDCTEB17iIAs0n_f80WzwOVWvSAR1NUdQQFuc77RQ-gjrp9-yxmUtzoDJWTVSfxULNcKuhhRTu9pzhHkQ_0lu_I3Js-Z5VjohC_tkQJJI-yjOlb1YeP-V6nlwW73HJMCH8cA2ptHe2izDmB4lluHpy33Hux3vhD4iKN_OaveNR-VsBiIb3JX4BaDo7vuWOhXEFxGUfmb3RmV2CcsZ5zSLayXrCbT5mZlu1-wbAJQHcB5K8S8nbaaoV07g7jyM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
امشب تو شب نشینی شهر بابلِ استان مازندران، وسط تجمعات شبانه‌شون دور هم جمع شده بودن و داشتن «
کلاغ‌پر
» بازی می‌کردن
✅
@AloNews</div>
<div class="tg-footer">👁️ 73.2K · <a href="https://t.me/alonews/147959" target="_blank">📅 01:53 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147958">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WYJuBgMirdy-Y5cZRTjs4hxgQNHCozmKNgOXqobGJVRivaO3Hdn4BuSn8eqvvE3GJVr3_GpliaSll4EJ3BZ0Bs_xCPlf__9kNwEqLQE1_jkwUCApe_dXGQCOs1F5WE0046KbT01-JLiTcDQGespEoXXdxcUo3jgMMnpvAK9Rc4AexkSLEu63UQh-7lSOsqWMwOCYYSrbdgxSEPi0NrbS5hBYYQ1_vesKJ-G1FdAEzDsejYlr-IrPDOKb4lzfmpCYbzp7sCil3WtE-HBadTcH8FontmWcpWWN5bH8YONs31CgvfTG2bf-9_ssWXg8H21Tlvc9N9N8Lbw_Jibcuve-lg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
عجیب اما واقعی
‼️
🔴
ایران ایر که یک زمان بزرگترین ایرلاین آسیا بود اکنون فقط ۹فروند هواپیما دارد که اکثرا فرسوده هستند
✅
@AloNews</div>
<div class="tg-footer">👁️ 82.9K · <a href="https://t.me/alonews/147958" target="_blank">📅 01:01 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147957">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MqXDDJHAKfJ3MDAgF1DE0vJJVAA2pD6MXb5SU76U2Pr2p19ko11r_9Vs8Ajxrxov4bBIsx12nz3r0M_YoQ4RSZt9euqtcTIK1v8dQzuIgkxlQ4JAev0zdCJZPj33riCsMxdYh4sDHVKR82lnBMy_f5S_BuCsmf-ViJy79Bl4wnwhtvWj9HBaiKuhA5BuLPMc2BPUTeYk37gLNOzYPTKZplkAalshCpc2ai06sSbmwMLUW0ICYfg2ppzc5GVrDaPF1I6E7noKoJw9tchZod6aXy_mn6odskn5q-mqRG99iy4cSUAadiqYIEda4OmeYIA856GjVod7F_hXxYs4XY-JmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
بمباران شدید جنوب لبنان توسط اسراییل
✅
@AloNews</div>
<div class="tg-footer">👁️ 81.4K · <a href="https://t.me/alonews/147957" target="_blank">📅 00:40 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147955">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MQZvLPFXcA3LKc0AaJyUscLNAd7j0l6UyLrnyDBTACQj4AfvKYgzixUlKeMxI_GyfbqStkY7WXtg2d2Q-cj2pi5aqLuszKONkvH3XXJbEQPPaRGr-M4ulWz86HJ3vZzXTic6mWNNFJ42GoHdlh_xj_-SQCnxVtFdIkGO7bSEQ9C72V7xkp1z3mwtD2H07DnlTrSGVYXxSTtGdbPjpH4LAuo0m0sjodWNYPXsq18Yco8vycEKOAsld_5ju81oe_a54LAWrEvUGUOp7v5Z07iXtBWjCoPKYEd0xxENN6yadoKOa3Vw1W5XJLESoGYwEkOee549PSnsc4xcLrD63Wkkxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bidmfQ7NdrUS8cGuMr9AWJiFo20zt5MOBLZ7TrV2L-qSsLLb2gFPSSy1D2-1oHU48CTKsAsZ1h-r44se8q8Ygee8Zcm5d4TRFVw88Pd4Ggn1fmYRa5ximu3PcFvZlo2Qep2QNj_XeAKPq2qKWaLBcA0f5lRjZsfGISnfenU4LB4rCKLijau1rpoUsyLFeQzIC46vJ0PoH4SJ-b_Q2Ha9ixokOimJYin7A2zgwAxKy8OkOWAmK148YD84DEzuo_bhG93if6YJQhQUDTbH8C72BNZL6Na2CBo9g2j8v78_3IOyQZeJtXFFExGUB-0LCOvEmxa6dtg_q_ONYsr9m09yqg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
گسترش سریع فعالیت‌های ساختمانی در سایت طالقان-۲ تهران
🔴
تصاویر ماهواره‌ای نشان می‌دهند که فعالیت‌های ساختمانی در تأسیسات «طالقان-۲» در تهران به‌سرعت در حال گسترش است.
🔴
طالقان-۲ از تأسیسات مرتبط با برنامه هسته‌ای ایران در چارچوب پروژه «آماد» معرفی شده و گفته می‌شود این مجموعه در اوایل دهه ۲۰۰۰ برای آزمایش مواد منفجره مورد استفاده قرار می‌گرفته است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 81.5K · <a href="https://t.me/alonews/147955" target="_blank">📅 00:27 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147954">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">👈
قوه‌قضاییه: واسه ۱۵۹ آمریکایی اسرائیلی پرونده تشکیل دادیم دادگاهی شن
✅
@AloNews</div>
<div class="tg-footer">👁️ 80.3K · <a href="https://t.me/alonews/147954" target="_blank">📅 00:17 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147953">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">👈
میدل ایست آی: ترامپ «وسلی هانت»، جمهوری‌ خواه ضد اسلام و حامی اسرائیل را به عنوان سفیر بعدی آمریکا در عربستان نامزد کرده
🔴
این انتخاب در لحظه‌ای حساس برای روابط آمریکا و کشورهای خلیج فارس صورت می‌گیرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 80.5K · <a href="https://t.me/alonews/147953" target="_blank">📅 00:08 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147952">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">👈
نتانیاهو: من نه مسیح هستم و نه پادشاه.
یک پادشاه نیازی به انتخاب شدن نداره؛ اما من باید انتخاب بشم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 81.4K · <a href="https://t.me/alonews/147952" target="_blank">📅 23:57 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147951">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">👈
نتانیاهو درباره ایران: اگر به‌موقع برای حمله به ایران اقدام نکرده بودیم، امروز اینجا دور هم جمع نشده بودیم؛ چون ممکن بود اصلاً کشوری به نام اسرائیل وجود نداشته باشه.
✅
@AloNews</div>
<div class="tg-footer">👁️ 82.5K · <a href="https://t.me/alonews/147951" target="_blank">📅 23:39 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147950">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">👈
مکرون خواهان اتش بس فوری در لبنان شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 81.4K · <a href="https://t.me/alonews/147950" target="_blank">📅 23:22 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147949">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">👈
سخنگوی وزارت خارجه آمریکا به الجزیره: هیئت ایران طبق تعهدات کشور میزبان در مجمع عمومی سازمان ملل حضور خواهد یافت
✅
@AloNews</div>
<div class="tg-footer">👁️ 81K · <a href="https://t.me/alonews/147949" target="_blank">📅 23:17 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147948">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🔴
فوری / عملیات تجارت دریایی انگلیس (UKMTO) اعلام کرد گزارشی از یک حادثه امنیتی در تنگه هرمز، در ۱۶ مایل دریایی شمال‌شرقی خصب عمان دریافت کرده
✅
@AloNews</div>
<div class="tg-footer">👁️ 81.2K · <a href="https://t.me/alonews/147948" target="_blank">📅 23:13 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147947">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M10dM4kaNLYgJwIqjVMxCPkWBXxECCTf9PP4MySIKTXFt-k7rLdEZWqJXZRtPl_eDVWATfZPeJqkNJhmitolRzfRWPOxTPLiVGgw3-HMQqAPQvSRbcT5-72sK12bsDZYXwKYa0kfgjGX9J3xyPE0RXP_Wy9i15UeXKWR6qcbDOHoPYbMmf41xknJlQgdDgCi9pmtuUlUjAkrrLbv-mPre6mRqHIq313gMCrI5EueTfEwYCqpPMiXpNCdHUUexWKWsT52GBoyCJQ48sVuv7_IWe5UE93yUqql4Nu6QV5n8kI5Mo_nCNrchXhXvvVMitQN8x07GRzBHb_Noj-_hftovw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
قالیباف: نظم تک‌قطبی که در آن یک طرف با زور و اجبار امتیازگیری می‌کرد، به پایان رسیده است.
🔴
وتوی چین و روسیه سوءاستفاده سیاسی از شورای امنیت را رد کرد و حاکمیت قانون را مجدداً تثبیت نمود.
🔴
ما باید از چندجانبه‌گرایی دفاع کنیم؛ زیرا یک‌جانبه‌گرایی در خدمت منافع هیچ‌کس نیست.
✅
@AloNews</div>
<div class="tg-footer">👁️ 81.3K · <a href="https://t.me/alonews/147947" target="_blank">📅 22:59 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147946">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">دلار و طلا تا کجا بالا میره
⁉️
🚫
پاسخ عجیب هوش مصنوعی
👇
https://t.me/+cs85WnZxgpM1NjRk
https://t.me/+cs85WnZxgpM1NjRk</div>
<div class="tg-footer">👁️ 75.6K · <a href="https://t.me/alonews/147946" target="_blank">📅 22:56 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147945">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">👈
خزانه‌داری آمریک«بیت‌بانک» (BitBank)، یک شرکت ایرانی فعال در حوزه دارایی‌های دیجیتال، را تحریم کرد
🔴
گویا صاحب بیت‌ بانک بابک زنجانی هستش
✅
@AloNews</div>
<div class="tg-footer">👁️ 77.8K · <a href="https://t.me/alonews/147945" target="_blank">📅 22:43 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147944">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">👈
آخرین جزئیات قتل‌عام خانوادگی به خاطر ارثیه از زبان خود قاتل
✅
@AloNews</div>
<div class="tg-footer">👁️ 75.1K · <a href="https://t.me/alonews/147944" target="_blank">📅 22:39 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147941">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EtIgKbKhdjN5qDbNYfR_tLphlQL4NYkqAtAhO5avw8MdGY6hdLzJhXeGS6N3iQUlhbmemzgDZhaWfISwbXDxPGDG9qRRYsVGFljDi-tDku3xTPpwxcfqMkIOoRIljTpk-aBZv0e0pmYTQvAdXqxkQ7b0U-Wujkc1qrClfv7OTyTC8zIEz0yfeck9DMfQQ0InKODm_ZkOsA3ZmzAMzKUC8iYXrRrsk6lRlvBqDaYTB1v_3gEkMZH_NaC7dRg5305SUnLgFHa_fdHo4PtygI37dBqdFprFiyAGyWKdl3sZinxoJ6BLtzhNkB9-A_2HLmZsQc4fbYgA2xgrkoAX6ZvARg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HJmUFB_A255g8PH_dMP5FvlYcG-hx_J741M38Yir78LUxMIjhYT9BiKVw_9DLuXHPYihLLzvKRBIEswsEjU8tCMSv_oWMct2tb1hGSwqjHZDYZxoxqRTipT3KVEx0SukKthaFfK4Kvcaw5KaazvmBYL86-tlxkr5XSwo9NWkNHevcXbf4nVsxlq3aOGQVO0ikvHbJOAXCQNbtt4RTHI8-_xyt8TRdg4uJntAI7BylDFfVgc_ohNUne0Gyro1mKQ8GU36lTdTD7RF8lR8FqsS6dj64sDkT63zLCh4EWUQwkYaj7-Lj2ZpcE8Udvaxle-CcGBkR0AxZ4F_2O3jpqlHFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hCRuNmlRPjptkGTGbm_t3wqIlUBa7-gm3nrXTKZ9xBq-Y9zRYfB9tzwWkGWtelFPTxznw4QZZdMUsX4Ixa5WbMrdUsN75n_RAxd8488tc40xcXkxIDcwMNeV18UTn9QkGmITQMkMkxSU-LdJODSTY7UQ1pu94OHuHrv3OlZkVJfvFc_S4t_IZ10guTPWFRvqQeeRrjpgk0CRZpDt9gQIiTbXDilrSwl5UMrV8a3cBnqcbJgRWfBtIwRjnxMopXz0Db2iReuh_bdgmiKTeXM3vstxRoxlFmRpkHoTkTCn97KynWXmZKd86mGY5t1M8eUXcGqzdNF_TIMzdVRfV2KmLw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
تصاویری از محل سقوط هواپیمای F-16 در شهرستان بلر، ایالت میشیگان، در شرق ایالات متحده.
✅
@AloNews</div>
<div class="tg-footer">👁️ 72.6K · <a href="https://t.me/alonews/147941" target="_blank">📅 22:26 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147940">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">👈
آسوشیتدپرس: واشنگتن با صدور روادید برای مقامات ارشد ایرانی جهت شرکت در مجمع عمومی سازمان ملل موافقت کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 73.7K · <a href="https://t.me/alonews/147940" target="_blank">📅 22:19 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147939">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9263a32ce5.mp4?token=U5fTvQ7o79cpmP5joeVaQQMJa_A4OIxVBWeV0g4dQNHs5PDBXAclmPx3JFKvnMdhEjfTv6Fx9sbWpW0zQE2f0I1g12jh64z_cBzQ1m6T3S0_aS0YsQvMpkaJFfzkUGWzIiPtI_Wb85afNueRqAoAzQQ5-GJg8EaRc2_b-lvxFx3sLFvOzCYOLSdTDXfVRXYfP9iTRy47H0epYw9m_luONkBAXRz9RTvAN6SIn2w7oWIGn7o84myhp2a8I225nRZnOvQAAG0GpRCfU-BXssDnLtxiOHn-TUvyy20vtB5bIh3JVBlXgi5zUUqQLL1Ookd7ybJ6zzkiY08tYbNTVbwmMg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9263a32ce5.mp4?token=U5fTvQ7o79cpmP5joeVaQQMJa_A4OIxVBWeV0g4dQNHs5PDBXAclmPx3JFKvnMdhEjfTv6Fx9sbWpW0zQE2f0I1g12jh64z_cBzQ1m6T3S0_aS0YsQvMpkaJFfzkUGWzIiPtI_Wb85afNueRqAoAzQQ5-GJg8EaRc2_b-lvxFx3sLFvOzCYOLSdTDXfVRXYfP9iTRy47H0epYw9m_luONkBAXRz9RTvAN6SIn2w7oWIGn7o84myhp2a8I225nRZnOvQAAG0GpRCfU-BXssDnLtxiOHn-TUvyy20vtB5bIh3JVBlXgi5zUUqQLL1Ookd7ybJ6zzkiY08tYbNTVbwmMg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
عروسی یک زوج ایرانی ارمنی با حضور اسنوپ داگ خواننده معروف آمریکایی
✅
@AloNews</div>
<div class="tg-footer">👁️ 75.1K · <a href="https://t.me/alonews/147939" target="_blank">📅 22:13 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147938">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">👈
وزارت خزانه‌داری آمریکا: ما به دلیل حمایت از دولت ایران، پلتفرم معاملاتی ارزهای دیجیتال بیت‌بانک را تحریم کرده‌ایم
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.8K · <a href="https://t.me/alonews/147938" target="_blank">📅 21:57 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147937">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">👈
بر اساس گزارش شبکه خبری ای‌بی‌سی، سام آلتمن، مدیرعامل اوپن ‌اِی آی، و جنسن هوانگ، مدیرعامل انویدیا، قصد دارند هفته آینده در یک شام رسمی با اهمیت بالا در کاخ سفید در کنار شی جین‌پینگ، رئیس‌جمهور چین، حضور یابند
✅
@AloNews</div>
<div class="tg-footer">👁️ 72.9K · <a href="https://t.me/alonews/147937" target="_blank">📅 21:46 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147936">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">👈
وزارت خزانه‌داری آمریکا: ما به دلیل حمایت از دولت ایران، پلتفرم معاملاتی ارزهای دیجیتال بیت‌بانک را تحریم کرده‌ایم
✅
@AloNews</div>
<div class="tg-footer">👁️ 73.4K · <a href="https://t.me/alonews/147936" target="_blank">📅 21:35 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147935">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">👈
وزارت امور خارجه ایالات متحده فروش احتمالی ۴۸ فروند جنگنده F-35 لایتنینگ ۲ به ارزش ۲۴.۳ میلیارد دلار به عربستان سعودی را تأیید کرده است که نخستین خرید این هواپیمای پیشرفته توسط این پادشاهی محسوب می‌شود.
🔴
این بسته شامل ۴۸ فروند F-35، ۴۹ موتور پرات اند ویتنی، تجهیزات ارتباطات، قطعات یدکی و حمایت‌های اضافی است.
🔴
وزارت امور خارجه به صورت رسمی کنگره را از پیشنهاد این فروش مطلع کرده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 72.5K · <a href="https://t.me/alonews/147935" target="_blank">📅 21:35 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147934">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">👈
نورالدین الدغیر خبرنگار الجزیره در تهران: «صحبت‌های ترامپ درباره حمله به ایران، به اعتقاد من تلاشی برای زمینه‌سازی جهت مذاکره با ایران است؛ چرا که این موضع‌گیری‌ها بلافاصله پس از سفر عراقچی به پکن مطرح شد. همچنین تماس تلفنی میان وزرای خارجه چین و آمریکا نشان می‌دهد که چین در حال سنجش تمایل ایران و واشینگتن نسبت به هرگونه اقدام چین برای حل‌وفصل اختلافات میان آن‌هاست، و ایران نیز در جستجوی کسی است که تضمین‌های لازم را ارائه دهد.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.2K · <a href="https://t.me/alonews/147934" target="_blank">📅 21:31 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147933">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V0vblWBb9mKSuCVsNJpNVLpOVSoghTc4Ws3twTTvGLFsC0fUL_3HcTP1M5gj6B4IhITh31xlu6XSs8ri1qPKSKoLg48Y52j7A-n3h7VHzm1CseLzQUN5lFp38TTS7uqo1_viJQAHLNPB9CFxJURYWtthqNdhCgdof0TcrVSfWww05yZr4OT3NaisoUHhEBhd3MKl8h2u1iBvWpNfnqAJl9EUGUD3Yj53vS-TiUoJQrM3KaKSBztVWboZ_jzUQPMI3UN-sV62rH06qa6vLmVRal78ucuhH2ie1ZVbK1VAvptmIxE7_FtMSqExmCng-M66WXLrtog6zcwXcDhYjztTIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ درباره لهستان: اخبار عالی! به لیدرهایی جسورانه از سوی دوست من، کارول ناوورکی، رئیس‌جمهور لهستان، پیشرفت‌های چشمگیری در جهت ایجاد پایگاه ارتش ایالات متحده در لهستان حاصل شده است.
🔴
اگر این اتفاق بیفتد، مکان آن به‌زودی اعلام خواهد شد. این یک گام تاریخی برای اتحاد بزرگ ایالات متحده/لهستان ما خواهد بود. از توجه شما به این موضوع سپاسگزارم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.7K · <a href="https://t.me/alonews/147933" target="_blank">📅 21:27 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147932">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2ba25b1275.mp4?token=fh9I2fD2Y337GWuMzfBrWGxkR-JOfUwLufvOMsfqPsefa0dvcF7NhwpfbThz98_ziZhs9Lsv5MWqTWcraqouJSB2KCNzEhqFQLTJE_ffZFTfAVMXuh28pl0dwAxl1wNNzvNq7qY0v1b9daP7jA_z3GcGjRs4VwTZmp-rxG-xr7xfQMVAYq25dvq8kpNGh2Nox6kPKnmnxBuZo5vDSZ183hmNJuHvng7EBedlPoIJCKXx3mjtSYOyigvNfypDVZvNEL5bvLRrReQjo-MqeoChUxco1_LRA04OLktjDVDQUN9_EsJWqk6JLL-Wbdq3zu_oZoCfpTm4NewFoTjTahQF3g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2ba25b1275.mp4?token=fh9I2fD2Y337GWuMzfBrWGxkR-JOfUwLufvOMsfqPsefa0dvcF7NhwpfbThz98_ziZhs9Lsv5MWqTWcraqouJSB2KCNzEhqFQLTJE_ffZFTfAVMXuh28pl0dwAxl1wNNzvNq7qY0v1b9daP7jA_z3GcGjRs4VwTZmp-rxG-xr7xfQMVAYq25dvq8kpNGh2Nox6kPKnmnxBuZo5vDSZ183hmNJuHvng7EBedlPoIJCKXx3mjtSYOyigvNfypDVZvNEL5bvLRrReQjo-MqeoChUxco1_LRA04OLktjDVDQUN9_EsJWqk6JLL-Wbdq3zu_oZoCfpTm4NewFoTjTahQF3g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
فارس: کالابرگ ۳۰۰هزار زیاد شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.2K · <a href="https://t.me/alonews/147932" target="_blank">📅 21:15 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147930">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gMwUfgCjxlsS0SU329S-pPX61Mc198UxXbfmGeVp9DIFrb6J2EOGypbayhItf6XM81jV18ecewraAVduQSvCteYV5xlBSE5tGb_wjLkOHDKxrQiUfBNrlrxHcsvu8FF9LB3laP3-3yQJoznXUfFpkQasdS0m7KUwhIcg0Po_b2M52OZcMi7uCMBPoWbTQzY3Rj7BOLJNnbPyP3C3JfbYd6hiE07tFWe61s3c-xT-Ri7S9X41-YkolfY3XUH2YsJupVAetUgs-E2Ur347kucrjiQve6WSVQLTOlG-oaZbUnkpyyaxkSVA5sEfgjKNK10Uq6XX_pW-X3DIdlz0rNtQ5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ef55f0b0ff.mp4?token=IaKdsoPjdkXgtfOLi1ZFLbht7bDexp7M7pnpmBv2yROe7xTqYUk0OvnkRdM-sDuy897Rm09iRKdA6rKDylfBuLdgLT7fJPN4oaNv2GQ8ltYoCDqvwGMqbkagGdKVNG6tS8s5t0OtBhHGCP0QpOywa2xCm7eN0mX7Ot8Wv2wzAIcaO243z61SK4WLRpdU1p_ndCwkM5Pt-nf6SW__ClxcPDVdiUFfyyLHZ1JOvgmIkzgucTh4QZbpoDNtfzm90RtlRknUex46VhOVvaYe4p3p0FDuVVtKIkLODqALEpYp4VUq3y64ylPNpabAvLYKluHoITGpcyRSsIOvpmL50tNugg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ef55f0b0ff.mp4?token=IaKdsoPjdkXgtfOLi1ZFLbht7bDexp7M7pnpmBv2yROe7xTqYUk0OvnkRdM-sDuy897Rm09iRKdA6rKDylfBuLdgLT7fJPN4oaNv2GQ8ltYoCDqvwGMqbkagGdKVNG6tS8s5t0OtBhHGCP0QpOywa2xCm7eN0mX7Ot8Wv2wzAIcaO243z61SK4WLRpdU1p_ndCwkM5Pt-nf6SW__ClxcPDVdiUFfyyLHZ1JOvgmIkzgucTh4QZbpoDNtfzm90RtlRknUex46VhOVvaYe4p3p0FDuVVtKIkLODqALEpYp4VUq3y64ylPNpabAvLYKluHoITGpcyRSsIOvpmL50tNugg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
حملات سنگین اسرائیل به جنوب لبنان
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.3K · <a href="https://t.me/alonews/147930" target="_blank">📅 21:13 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147929">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🔴
تا ماه بعد وضعیت طلا چجوریه؟</div>
<div class="tg-footer">👁️ 67.2K · <a href="https://t.me/alonews/147929" target="_blank">📅 21:12 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147928">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">👈
آکسیوس: ترامپ دستور داد سطح نیروهای فعلی در خاورمیانه تا پایان سال برای احتمال از سرگیری درگیری‌ها حفظ شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 73.5K · <a href="https://t.me/alonews/147928" target="_blank">📅 21:00 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147927">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">👈
وزیر دفاع پاکستان، خواجه آصف:
حتی اگر هیچ توافق‌نامه‌ای وجود نداشته باشد، اگر عربستان حمله شود — به‌ویژه مکان‌های مقدس ما — ما به موجب یک توافق ابدی موظف به محافظت از آن‌ها هستیم.
🔴
خانه خدا و مدینه منوره — محافظت از آن‌ها وظیفه دینی ماست
✅
@AloNews</div>
<div class="tg-footer">👁️ 72.3K · <a href="https://t.me/alonews/147927" target="_blank">📅 20:54 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147926">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cb984ea71a.mp4?token=d3ykdmfyLoZxrsybuGGB2rE1w-SGZRssnMIf8mJCTqJtp_05v3kExMbh2SUPxMy8A0TCBXJ2rLYYzl7phSxLK2feo2XvzKDLd23Vczy8SAZkl98QA8FBL-4fCrVmxJGnuVHRgYVaZx9HjiJh8bvBCLOVD89bRQQkA8Hmbl6yN6LYRC1eoVonA_h4a6VA_PQlHiiavXkc4WVf7WE4psGdEoeTJKmw_d8kPfEGmEYHP30KIUIoVl8AbravNIUSu8LSLEPZIQ2ijlVkfqNuzqe2sOe7Xu7UGac0gsSLXdufJ9o_8CF-HOazZ7mluT1h2UiHkN-zznAMLhZgifZDp2_EhBQsRAJKreovaRLJ2JpRuuoCjcr8tmySYGIg7eDa8lz1wNI4rvR5UmoZIOp6xNHXFmEG7HrNg8Hb83kDm05VSAj0Zey8mZazOtSaG14havz7qS_Nee25LsIa79GOhsOjo1iMbiC89yQmSNrki7cV3aJTiWyDDN3omcE4MgH0xNy_LhAx1mTnj6EKelkP8W45gL2jogLuWbbFH6tiOiujnNtXxqZZr3-bm3vgBillXH-vD2rTCN6qMlvt66RG3uTn25TfbNuDCniKWLm6vGx8OntRNHtyIIovkaHujJnSERUSHfeC5hjqbggXCK_80HakEKiWvGgbjFiPsLaZKK3GYF8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cb984ea71a.mp4?token=d3ykdmfyLoZxrsybuGGB2rE1w-SGZRssnMIf8mJCTqJtp_05v3kExMbh2SUPxMy8A0TCBXJ2rLYYzl7phSxLK2feo2XvzKDLd23Vczy8SAZkl98QA8FBL-4fCrVmxJGnuVHRgYVaZx9HjiJh8bvBCLOVD89bRQQkA8Hmbl6yN6LYRC1eoVonA_h4a6VA_PQlHiiavXkc4WVf7WE4psGdEoeTJKmw_d8kPfEGmEYHP30KIUIoVl8AbravNIUSu8LSLEPZIQ2ijlVkfqNuzqe2sOe7Xu7UGac0gsSLXdufJ9o_8CF-HOazZ7mluT1h2UiHkN-zznAMLhZgifZDp2_EhBQsRAJKreovaRLJ2JpRuuoCjcr8tmySYGIg7eDa8lz1wNI4rvR5UmoZIOp6xNHXFmEG7HrNg8Hb83kDm05VSAj0Zey8mZazOtSaG14havz7qS_Nee25LsIa79GOhsOjo1iMbiC89yQmSNrki7cV3aJTiWyDDN3omcE4MgH0xNy_LhAx1mTnj6EKelkP8W45gL2jogLuWbbFH6tiOiujnNtXxqZZr3-bm3vgBillXH-vD2rTCN6qMlvt66RG3uTn25TfbNuDCniKWLm6vGx8OntRNHtyIIovkaHujJnSERUSHfeC5hjqbggXCK_80HakEKiWvGgbjFiPsLaZKK3GYF8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
رئیس ستاد مشترک ارتش آمریکا:دشمنان ما در حال یادگیری از جنگ‌های ما و به چالش کشیدن برتری‌های ما هستند
🔴
دشمنان ما ممکن است از نظر جغرافیایی پراکنده و دور از هم باشند، اما به شکلی فزاینده با یکدیگر در ارتباط هستند.
🔴
آن‌ها فناوری، اطلاعات، تسلیحات و حمایت‌ های اقتصادی را با هم به اشتراک می‌گذارند.
🔴
آن‌ها میدان‌های نبرد گذشته و کنونی ما را مطالعه می‌کنند، به سرعت خود را با شرایط تطبیق می‌دهند و در پی یافتن راه‌های جدیدی برای به چالش کشیدن برتری‌های ما هستند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.9K · <a href="https://t.me/alonews/147926" target="_blank">📅 20:49 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147925">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">👈
ترامپ: ایرانی‌ها در تماس مستقیم با ما هستن و همچنان خواهان دستیابی به توافقن
🔴
می‌خواهم از جلسه عمومی سازمان ملل (هفته بعد) استفاده کنم تا مستقیماً از متحدان منطقه‌ای درباره گام‌های بعدی جنگ بشنوم
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.6K · <a href="https://t.me/alonews/147925" target="_blank">📅 20:44 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147924">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🔴
فوری/ ترامپ: به جایی که باید درباره ازسرگیری حملات گسترده به ایران تصمیم بگیرم، نزدیک هستم
🔴
هر اتفاقی ممکن است بیفتد
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.8K · <a href="https://t.me/alonews/147924" target="_blank">📅 20:43 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147923">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🔴
فوری/ ترامپ: به جایی که باید درباره ازسرگیری حملات گسترده به ایران تصمیم بگیرم، نزدیک هستم
🔴
هر اتفاقی ممکن است بیفتد
✅
@AloNews</div>
<div class="tg-footer">👁️ 69K · <a href="https://t.me/alonews/147923" target="_blank">📅 20:43 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147922">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🔴
فوری / دونالد ترامپ: قرار است تصمیم مهمی در مورد ایران بگیرم
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.5K · <a href="https://t.me/alonews/147922" target="_blank">📅 20:31 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147921">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ed64f0a840.mp4?token=QnEMG5eG6ZvR0UZOArOTpoWC89q6KQJgYdwYjHUskW1y9o9eic-D8U__SB372bOxpbff-qtVkakHGaGTuAHITKRN-NDYzbCZeahPXpfvad4K5ftgAtBzwy1-v1P1YpbQTZk8oxJYGeG0gIMzOZPpJrOEJpVUSiNcoB-mpkT9WFgb0e_8bsCqmhM8BEL02doyStatJby-uj0g-aUa10H1wps_ZspvC4-jqRVv74d-HdCoDCT5GtlOMA9qEtfpkQH8Bfv1qW0GI3pttSqIOMriIsYo4N7j7HA0uwfdgXUIwI6mPuOcX_HZtdrdqyQWCxdkpuQ4-AElLEshq_INe3YQ3w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ed64f0a840.mp4?token=QnEMG5eG6ZvR0UZOArOTpoWC89q6KQJgYdwYjHUskW1y9o9eic-D8U__SB372bOxpbff-qtVkakHGaGTuAHITKRN-NDYzbCZeahPXpfvad4K5ftgAtBzwy1-v1P1YpbQTZk8oxJYGeG0gIMzOZPpJrOEJpVUSiNcoB-mpkT9WFgb0e_8bsCqmhM8BEL02doyStatJby-uj0g-aUa10H1wps_ZspvC4-jqRVv74d-HdCoDCT5GtlOMA9qEtfpkQH8Bfv1qW0GI3pttSqIOMriIsYo4N7j7HA0uwfdgXUIwI6mPuOcX_HZtdrdqyQWCxdkpuQ4-AElLEshq_INe3YQ3w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
نمایش بمب‌های سنگرشکن برای تهدید ایران در گزارش خبرنگار فاکس‌نیوز
🔴
خبرنگار فاکس نیوز: آنچه الان می‌بینید، یک بمب سنگرشکن GBU-31 ویکتور ۴ است. ما در یکی از انبارهای مهمات ناو هواپیمابر جورج واشنگتن هستیم و همان‌طور که می‌بینید، انواع مختلفی از تسلیحات در اینجا وجود دارد؛ از جمله موشک‌ها و بمب‌های گوناگون
🔴
در انتهای این بخش هم انواع دیگری از بمب‌ها را می‌بینید. این‌ها بمب‌های ۲٬۰۰۰ پوندی هستند. باز هم تأکید می‌کنم، تمام این تسلیحات در صورتی مورد استفاده قرار خواهند گرفت که رئیس‌جمهور دستور حملات بیشتری علیه حکومت ایران صادر کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 71K · <a href="https://t.me/alonews/147921" target="_blank">📅 20:25 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147920">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9225e42d16.mp4?token=WIY5qzE10K2g7iPWyou9WnFwdhM5qyweRZAZBwxRvfqjXAHifZ4KLtFJSYsCo2hrYRm1s9CyDInKne2RWyCMmIif6zL8MCZdl2Nmx4jT0ophcvDdWckNOaFJDn7h6wXXRgc4p22P0AXs9m1edH7d66gKdImuvITCNJJ_oeOA9Xiw2HVnCHDF0kVcCJtaOJjgcIibZaXLUV5yPx8gkTyHBo5jQg-dPKKlQb2CWd87Ax6UUzGQDREOE7uQ1HRny89KTtEdR0gPVgbX2Ks-XPPnFeDm2tezD0sua95CHs7PD_9spIxiL-yn0l9WaR6YAHk6ywoTVOvNhI7TzRZL1Q51hA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9225e42d16.mp4?token=WIY5qzE10K2g7iPWyou9WnFwdhM5qyweRZAZBwxRvfqjXAHifZ4KLtFJSYsCo2hrYRm1s9CyDInKne2RWyCMmIif6zL8MCZdl2Nmx4jT0ophcvDdWckNOaFJDn7h6wXXRgc4p22P0AXs9m1edH7d66gKdImuvITCNJJ_oeOA9Xiw2HVnCHDF0kVcCJtaOJjgcIibZaXLUV5yPx8gkTyHBo5jQg-dPKKlQb2CWd87Ax6UUzGQDREOE7uQ1HRny89KTtEdR0gPVgbX2Ks-XPPnFeDm2tezD0sua95CHs7PD_9spIxiL-yn0l9WaR6YAHk6ywoTVOvNhI7TzRZL1Q51hA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
اسرائیل و یونان یک مانور دریایی مشترک برگزار کردند که شامل تبادل خدمه و آموزش برای سناریوهای مختلف مانند «موقعیت‌های اضطراری» بود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.9K · <a href="https://t.me/alonews/147920" target="_blank">📅 20:13 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147919">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/16578a4b94.mp4?token=NvwuO87D8TS2_MqQXULfJFpdboEZtVAobK9cJqcggfZVA-EK5HVXZQT-MQIwKKOyAlVpFLf62H_7tBO-VyakYH6195sydauFQeqaVJMQ1chVScPOcJF1SR5waV3LqhmfeAajGjYFABH8aIxB9bmYEQnrz-PIQMQGWfGAmrkCGoCln2BPtRzjqvXjKptV9D1xKWpTNI5XrYs7LM4QF7vfYkgasR6KiYFw95ncrJDaJ4gxCYcTgiD_0SPDwDCW066zHms1h2JgB-QawxZoucCTLB2zEc6upeSk1gRpX7hN4yzeotjBLaNJfv2X0h52B3I1VDx7CKVw_Oufi5DsAa00lA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/16578a4b94.mp4?token=NvwuO87D8TS2_MqQXULfJFpdboEZtVAobK9cJqcggfZVA-EK5HVXZQT-MQIwKKOyAlVpFLf62H_7tBO-VyakYH6195sydauFQeqaVJMQ1chVScPOcJF1SR5waV3LqhmfeAajGjYFABH8aIxB9bmYEQnrz-PIQMQGWfGAmrkCGoCln2BPtRzjqvXjKptV9D1xKWpTNI5XrYs7LM4QF7vfYkgasR6KiYFw95ncrJDaJ4gxCYcTgiD_0SPDwDCW066zHms1h2JgB-QawxZoucCTLB2zEc6upeSk1gRpX7hN4yzeotjBLaNJfv2X0h52B3I1VDx7CKVw_Oufi5DsAa00lA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ: من خیلی باهوشم
🔴
رئیس‌جمهور آمریکا گفت: من آدمی با سطح هوش بسیار بالایی هستم اما در نهایت من فروتن هم هستم
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.9K · <a href="https://t.me/alonews/147919" target="_blank">📅 19:58 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147918">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vy4dhSIJ4xXk6iBthVoFsjGck4TmKZJ2gbXGiQfOZVN_1uABX-1ZAfptDpwosmXykpubEDupKx9CtXoT_AJe6-ubGYUEZdoU-zRue5YSLvO8H9USfu7xSTthsXqr37v1kkBMPamIUn8q5VJKq8xcpJmUktMRTnpubZc-w0YLOg873SR7BIak_Qia7pL-2sJGFjyO9SEI-0FQ5JoNk8KIkwWyVVqGbGeG9-70erCtrBa-vb4OcYW_a6Qn1jnnrLZ3clu7LkRTf_rLTM0GMmJVOdGfM4Mfbq8HupclFz1KrBp5wmqA9P863Cp_pNrapwO0LT2-TM13EYf7kMfh8H9xpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
محبی، سخنگوی سپاه خطاب به آمریکا :
شما روایت هالیوودی می‌سازید اما ما لاشه جنگندتون رو با فرغون جابجا می‌کنیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.4K · <a href="https://t.me/alonews/147918" target="_blank">📅 19:53 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147917">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">👈
سفیر آلمان به وزارت امور خارجه احضار شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/alonews/147917" target="_blank">📅 19:47 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147916">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SPyjcWgtyQMdVW7SyUmpJ165aetIzYb6Y-E97bh6GxQksT5pa2-pAnDJtHEw1aFIoecRD7uI8jGJoM5HbaJhfM56yGNaspZ8RTei8btTxqHHfCKpMFs8G6jryptREnVPUow9RvNaJymQ3pdnUqNtrGYi8YTGiO_uyRotOLq0iRg54FA5i0Zk5Tr9at2IsBe40CkQcMZQNILCy_MMCiv3G8P5q2hzBSL4X5XgVpw5JhslrRVnCmzLKP_HBy6CSmvzzntjww7v3b2J_CJrfUasyMVyO3M2mYRN3XYuMCN9V36NtPH3AAU4RfUwYwIutg8u_ou57OFrH6RY2EGWgvPRrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نیروی دریایی بریتانیا اعلام کرد گزارشی درباره وقوع یک حادثه در فاصله ۷۵ مایل دریایی شرق عدن در یمن دریافت کرده است.
🔴
بر اساس این گزارش، یک قایق اقدام به تعقیب یک نفتکش کرده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.9K · <a href="https://t.me/alonews/147916" target="_blank">📅 19:46 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147915">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/75c065e013.mp4?token=VdKmtRgGvDzq9NE-hUsd21exWToBfayd2FZ0gyhCuaydJHXLK9KXchI3g_wUTU7QtFkalH4b0YbEPAH07p6o7ysXxfWl8udokXH3M_c5I9JybJqKfFcpkmrv2GaUsJn6dLUirna04ORmLQbgf_L5ZkgdWXFxkuiN_DQPVfFg_aSaw1LnOpRLl_NZmuPt7MdPQeuY_WL3yv7tcSpA69eg5NbNPUf3gn4NjXRqRGXX4mlOLtX2XHLbew-KB0wDP9ZJw5j_S6bXqDKPq_KXYYRA3i8ptCyl7pfXsuiptHCu2O0eQhUe4LKCAzr6WGga1c_V3kCzOAXvXAfmKRhcVD_uboWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/75c065e013.mp4?token=VdKmtRgGvDzq9NE-hUsd21exWToBfayd2FZ0gyhCuaydJHXLK9KXchI3g_wUTU7QtFkalH4b0YbEPAH07p6o7ysXxfWl8udokXH3M_c5I9JybJqKfFcpkmrv2GaUsJn6dLUirna04ORmLQbgf_L5ZkgdWXFxkuiN_DQPVfFg_aSaw1LnOpRLl_NZmuPt7MdPQeuY_WL3yv7tcSpA69eg5NbNPUf3gn4NjXRqRGXX4mlOLtX2XHLbew-KB0wDP9ZJw5j_S6bXqDKPq_KXYYRA3i8ptCyl7pfXsuiptHCu2O0eQhUe4LKCAzr6WGga1c_V3kCzOAXvXAfmKRhcVD_uboWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
نماینده روسیه در شورای امنیت: عدم اجازه ورود رییس سازمان انرژی اتمی ایران و معاون اول رییس جمهور ایران به شورای حکام، نقض آشکار  قواعد بین المللی است
🔴
در سال 2025 تمامی قطعنامه های اسنپ‌بک ملغی شدند و دیگر امکان بازگشت به مکانیزم ماشه وجود ندارد.
🔴
از آمریکا و بقیه کشور های حاضر شورا می‌خواهیم دیگر تقابل با ایران را ادامه ندهند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.6K · <a href="https://t.me/alonews/147915" target="_blank">📅 19:39 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147914">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">بیت کوین منفجر میشه
‼️
‼️
‼️
اگه توام نمیدونی بخری یا نه حتما ببین
👇
https://t.me/+4jOgodAq96dmYzY0
https://t.me/+4jOgodAq96dmYzY0</div>
<div class="tg-footer">👁️ 57.7K · <a href="https://t.me/alonews/147914" target="_blank">📅 19:34 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147913">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/igHlqLuvPXGhGVNVD42RUVSW76XHtf0CkDvkWYC5_Ed068ySzmrppDOuNu8paoDV6m1C00xAgWEOYS6XKt9oYwRP_C2W7VWAcHVjOc9FGO5N-iNiQ0I3d70pQEzaagaVk8uR3i5gku6e8xpypVSpwnI0pS5fPDLUKPPlow_1_UsU3MfaRoaT9akKK27FX0AG7FGmITaVkwNpwjfrDc-C6kLSxqR3AZPpPGrfMDOlySYGapdTRiUy-HIKWILrPb49qH2LTdyQWkxhfhsKGzQaTFZl3sL8Cn_qVBGuvdpdhEZGOekHmzRHBesG3xdmbcT0Aeq5RG-j1QHOU_udn8_gpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
۹ جنگنده F-16 دیگر آمریکا دقایقی پیش از اروپا راهی خاورمیانه شدند
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/alonews/147913" target="_blank">📅 19:34 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147912">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b7d68625bb.mp4?token=saMZjFYe4VcskBNDY6qdPAqKn0sLbrxn3O6szvatCwQeGk6Rsj9ko3wRren_ayeK8VFufQXFY9IbJmuNv1fijrmJa8ef-hHhePhDf3BVRimThu1CgIV1kfi0NIY36HWnzJueOZfT7v7ofd99yZaR67cSTtijAZ57xdblhV_nMdX5GtWut4GfYIF9Fjc89bLODr_IpUHIEcq1Dnvs92jREBs5g6NCUk0b8i3e3DaG4x3WolrEXqRlm7m_S2btqjNL04CjJUPSaCEdoJHxzixT0WNBKwwdqwh1E4XZIRqx7lAsMVJMbFSWpTtiVl__Z3ScZugVqFETfha4OpFPtQyW3A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b7d68625bb.mp4?token=saMZjFYe4VcskBNDY6qdPAqKn0sLbrxn3O6szvatCwQeGk6Rsj9ko3wRren_ayeK8VFufQXFY9IbJmuNv1fijrmJa8ef-hHhePhDf3BVRimThu1CgIV1kfi0NIY36HWnzJueOZfT7v7ofd99yZaR67cSTtijAZ57xdblhV_nMdX5GtWut4GfYIF9Fjc89bLODr_IpUHIEcq1Dnvs92jREBs5g6NCUk0b8i3e3DaG4x3WolrEXqRlm7m_S2btqjNL04CjJUPSaCEdoJHxzixT0WNBKwwdqwh1E4XZIRqx7lAsMVJMbFSWpTtiVl__Z3ScZugVqFETfha4OpFPtQyW3A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تصاویر ماهواره ای جدید نشان می دهد انصارالله در حال تقویت مواضع زمینی و سنگربندی در کوه های اطراف تنگه باب المندب  برای دفاع در برابر ضدحمله احتمالی است
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.5K · <a href="https://t.me/alonews/147912" target="_blank">📅 19:27 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147911">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">👈
فرماندهی مرکزی ایالات متحده (سنتکام) روز پنجشنبه ۲۶ شهریور، اعلام کرد که ارتش آمریکا در راستای اجرای محاصره دریایی و تضمین رعایت قوانین، تاکنون در مجموع به ۱۰۴ کشتی که در تلاش برای نقض این محاصره بودند، دستور تغییر مسیر داده است.
🔴
سخنگوی سنتکام روز گذشته با تاکید بر اینکه خطوط کشتیرانی اصلی در تنگه هرمز پس از پایان عملیات مین‌روبی همچنان باز و امن هستند، این محاصره دریایی را «آهنین» و کاملا موثر توصیف کرد.
﻿
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.5K · <a href="https://t.me/alonews/147911" target="_blank">📅 19:23 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147910">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/98b6b9d143.mp4?token=MMmfBQjLdMF9OjVBAHK5hYioTVZlinijYMZXVCfGxykKLrDTIexP88Vqy-wwjuefzC0FJEMy25kP_Ad_b6yBcULxDa3Rq-YYXcddv5KJx0K0wvD-xTh1tdWWZJwz9wYg4wMqMbEpwX3iOsMfqa6sOMqTjTsDuFOYkpjtE224tSDjd3Lpl5nhjn7tzcRvOzlZZ9Epn15e_HIvz8fYhsdeRJFHH0Qpb3wy-Xp8UOk0H3V2bhmtFZ_khh-akMpr_TI9M5OV2bLX1Vr38aKRExx04t6Yax0_NQOaHaLwp3kRVAuH02bE_kWVUOoPoaYUntHMbeT0Eu7ZwCqHl01J7eBY3w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/98b6b9d143.mp4?token=MMmfBQjLdMF9OjVBAHK5hYioTVZlinijYMZXVCfGxykKLrDTIexP88Vqy-wwjuefzC0FJEMy25kP_Ad_b6yBcULxDa3Rq-YYXcddv5KJx0K0wvD-xTh1tdWWZJwz9wYg4wMqMbEpwX3iOsMfqa6sOMqTjTsDuFOYkpjtE224tSDjd3Lpl5nhjn7tzcRvOzlZZ9Epn15e_HIvz8fYhsdeRJFHH0Qpb3wy-Xp8UOk0H3V2bhmtFZ_khh-akMpr_TI9M5OV2bLX1Vr38aKRExx04t6Yax0_NQOaHaLwp3kRVAuH02bE_kWVUOoPoaYUntHMbeT0Eu7ZwCqHl01J7eBY3w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ویدیویی از وقوع بهمن عظیمی که گروهی از کوهنوردان را در ارتفاعات قفقاز مابین روسیه و گرجستان گرفتار کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.3K · <a href="https://t.me/alonews/147910" target="_blank">📅 19:20 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147909">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PoqZmIlcgALiEHr6eveMizyMXOPZnobZqsB8ZTekMt1yrnsf-dbL7rcm0i-Vo9Yan1hnWk4F-XbqVX5m-vS7tQXkoUvi39MKqFLnX15q4ALQj0D3Pn58Heaz2mvAY9q5vYkwBRt43BuWnBZO_4gvFwOZAhPTxJLvw4csTxwRjQjKvNy2Ch6kh161Gevhsz0NbjJ5_jznMF3rBcGLQKSdiD31YMA-KloLRtYwIKmaUMbSD013ia37FQfS-7n3tV9TS7gAW5J1j8jmXkIFIG_u0xylSQVe5vrjbIqL23a6AqUagLhzu_vtH7EyNQdXZ4wtmOg7uWbpGPjshrEvF-GkJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
هیئت حقیقت یاب سازمان ملل:
آمریکا در حمله به میناب و لامرد مرتکب جنایت جنگی شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.3K · <a href="https://t.me/alonews/147909" target="_blank">📅 19:18 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147908">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">👈
هشداری فوری جامعه «باستان‌شناسی» خطاب به رییس‌جمهور: تخت جمشید را فوری نجات دهید!
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.7K · <a href="https://t.me/alonews/147908" target="_blank">📅 19:13 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147907">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/7c82a08a4a.mp4?token=lYn2939tLmPqersVxi2Jx7KDdwQKftniEiuh18mdGvvv6NCGf-sMPDu6BK8I2MOf8TnyIEmOpoY7ACtuiBAT3pxvIvP_7_F7XFfgIPllev46EdzilKyaT1kXjGgiiT_wit8Fgh_vfkVJj_T5_NdB16S3hSOoMtl0zWRpYdqEIA9am-41dT8KPft9NVdo_ET6gJubq-NQg4e9a19ALNrDbJF5l55DBkWnuCUqiTLNbdbz2q4SPsteJYuSzQcm9FxoOmnXIIwYDDAS0NiRKjOYWB6CU9zIxryXhDnuGkcgYuLWL8PT5V0egIw7TXCLUErNYozOE2ugYhWO5QIyCx0ruolUCFRZicbaoUG7xoYub4hjPJAr28cQhXqgHrlySRy8XciU0cW7pmJQmHkmgIF2EfbkiKiomFTbq1IMfB8od5jaCuuoQnhp9O5SXaJuW1WdhAUyMnQ63xRBbwf6THfiUpSODOgNp9hMfIkt1H-eJeW-HurMQgJ4BFO4lGHBEcAFDnr17OcfUX_Lq1Vl-uryZuWxVjaDyjHaF_bBuCwAftW3WWogwk_SINghyZSRST5goPhi47vW1T0a8VE6uiL6NPFWSnm7UoI6FszD3fcngmqWsK5YEL8NBljpJ-B-4Qnwyj5b0aeIb6G_7_Ubc_p6mjP8Ldbx4xydKinn31NydIM" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/7c82a08a4a.mp4?token=lYn2939tLmPqersVxi2Jx7KDdwQKftniEiuh18mdGvvv6NCGf-sMPDu6BK8I2MOf8TnyIEmOpoY7ACtuiBAT3pxvIvP_7_F7XFfgIPllev46EdzilKyaT1kXjGgiiT_wit8Fgh_vfkVJj_T5_NdB16S3hSOoMtl0zWRpYdqEIA9am-41dT8KPft9NVdo_ET6gJubq-NQg4e9a19ALNrDbJF5l55DBkWnuCUqiTLNbdbz2q4SPsteJYuSzQcm9FxoOmnXIIwYDDAS0NiRKjOYWB6CU9zIxryXhDnuGkcgYuLWL8PT5V0egIw7TXCLUErNYozOE2ugYhWO5QIyCx0ruolUCFRZicbaoUG7xoYub4hjPJAr28cQhXqgHrlySRy8XciU0cW7pmJQmHkmgIF2EfbkiKiomFTbq1IMfB8od5jaCuuoQnhp9O5SXaJuW1WdhAUyMnQ63xRBbwf6THfiUpSODOgNp9hMfIkt1H-eJeW-HurMQgJ4BFO4lGHBEcAFDnr17OcfUX_Lq1Vl-uryZuWxVjaDyjHaF_bBuCwAftW3WWogwk_SINghyZSRST5goPhi47vW1T0a8VE6uiL6NPFWSnm7UoI6FszD3fcngmqWsK5YEL8NBljpJ-B-4Qnwyj5b0aeIb6G_7_Ubc_p6mjP8Ldbx4xydKinn31NydIM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
حیف و میل گازوئیل توسط قاچاقچیان در منطقه مرزی سیستان و بلوچستان!
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.7K · <a href="https://t.me/alonews/147907" target="_blank">📅 19:02 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147906">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/53768ce3a2.mp4?token=YMYK5we8EjYCsJ2-UjKneBfdx9E-VvwkBfXLx-SriDI1Y7I5uFkix4m-bkNI7DpQi_bul-1eEoVkDyacJs2Or6N7rQHvLjxgGzXxukxqMA6xW6Fleye_-wvfNkrahpvyrZEhSSjIcqXxHI8TmtuFYdieepJxo9yt589x-M-k3v5kI10XKRfPoDH5EaWY8luEfnhnaenEGSQdJW7UK5S-s4RwLEa6iZ2Lwly5cmm9MV6I5t7y45fZovMzv2A_rbAUySDzb6LRm26qrCzmvw8npjq5Y_HLLdJnClw-TQszZVNQfezhIF4LlazDLLk1-7UFLpeQ-WnEbQcaYpHVWe58vw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/53768ce3a2.mp4?token=YMYK5we8EjYCsJ2-UjKneBfdx9E-VvwkBfXLx-SriDI1Y7I5uFkix4m-bkNI7DpQi_bul-1eEoVkDyacJs2Or6N7rQHvLjxgGzXxukxqMA6xW6Fleye_-wvfNkrahpvyrZEhSSjIcqXxHI8TmtuFYdieepJxo9yt589x-M-k3v5kI10XKRfPoDH5EaWY8luEfnhnaenEGSQdJW7UK5S-s4RwLEa6iZ2Lwly5cmm9MV6I5t7y45fZovMzv2A_rbAUySDzb6LRm26qrCzmvw8npjq5Y_HLLdJnClw-TQszZVNQfezhIF4LlazDLLk1-7UFLpeQ-WnEbQcaYpHVWe58vw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
گروه حوثی‌ها (انصارالله) یک پهپاد سعودی را در آسمان استان دمار در یمن سرنگون کردند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.6K · <a href="https://t.me/alonews/147906" target="_blank">📅 18:54 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147905">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kR28y0fuMS1YjdRNAU0dqR1fmm2qW9xZ9L1t3QfrOP4WIiSjJ1joeFb-4ffArRplxizo1TG23l0_SHGIzTlGILhg2R-uAHoUuNI1uA2c_Tt6iAJTWDkSPPGe9h1FPgZwdhaJ8SQhnFHyg51iKqI0VnE3UG4fo1o7cU6-q8ak722bLyNvc4_4auHEHy9qG6QCcA14kWcjguLjM4o-GkblxTLmvaY5V_cY2v8jIk6xdmj-t29SgFJZmCPbvvmYUaoMdukdESfe9KH1lx8njvWVtxdTlPXuMWfztu2-X3XH43S1mRJuNDSCqZZOQYkHBphVBX_kZB70BrMWaMYkDWXz9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
حرف حق پسر رئیس جمهور:
ملت جانفدا شبیه یمن، یارانه نقدی‌شان قطع بشه و از برق سراسری استفاده نکنند و هزینه زندگی‌شان را نصف کنند و به سفر نروند و از هیچ خودروی استفاده نکنند
🔴
نمی شود از یک طرف به خاطر اقتصاد ناله می‌کنید و از طرف دیگه میگید بزن توی دهان فلانی و فلانی
✅
@AloNews</div>
<div class="tg-footer">👁️ 60K · <a href="https://t.me/alonews/147905" target="_blank">📅 18:34 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147904">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">👈
عراقچی: از ابتکارات رئیس‌جمهور چین استقبال می‌کنیم
🔴
این ابتکارات در مقایسه با دیدگاه‌های غربی، با درک درست‌تری ارائه شده
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.3K · <a href="https://t.me/alonews/147904" target="_blank">📅 18:32 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147903">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">👈
الجزیره: روسیه و چین با استفاده از حق وتو در شورای امنیت، پیش‌نویس قطعنامه پیشنهادی آمریکا برای تمدید مأموریت تیم کمیته تحریم‌های ایران را رد کردند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.8K · <a href="https://t.me/alonews/147903" target="_blank">📅 18:25 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147902">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">👈
شنیده شدن صدای انفجار در محدوده تنگه هرمز
✅
@AloNews</div>
<div class="tg-footer">👁️ 61K · <a href="https://t.me/alonews/147902" target="_blank">📅 18:24 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147901">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">👈
رو دلار و طلا سرمایه گذاری کردید؟
آره
✔️
نه
❌</div>
<div class="tg-footer">👁️ 60.5K · <a href="https://t.me/alonews/147901" target="_blank">📅 18:20 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147900">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">👈
ذوالقدر: تا به زیر کشیدن ترامپ و نتانیاهو، تنگهٔ هرمز رو نخواهیم گشود
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.5K · <a href="https://t.me/alonews/147900" target="_blank">📅 18:18 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147899">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">👈
الجزیره: روسیه و چین با استفاده از حق وتو در شورای امنیت، پیش‌نویس قطعنامه پیشنهادی آمریکا برای تمدید مأموریت تیم کمیته تحریم‌های ایران را رد کردند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.8K · <a href="https://t.me/alonews/147899" target="_blank">📅 18:13 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147898">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0940fba80b.mp4?token=vl9sFMdFc_mA2FdpECrdjeimBfcLVepeXHjMs0qr4k7KX4jXwVuNUmtu2AiBKdkt5hKR4oiNlM8tMO9tZ3PczHLru8LqzlzMeb-d0qsl_VTAJZac_1B705rp9t7JiTKiCfrDaog_xO1XEikolqyIoTo4eIFap0M7eI-JXsYN6B_6x9dT2GBY9V0AugDU4vCP-aro9Tmhk375JrjOd0zqbgNR4MJQ2x0635YzT6ziAFxtxpq81WnQq3VSPeHLQNRdXx2kOYnxLF_YTaN14FdnRMbFkZEGsq8ZvA6nH7MihPpsNMjTWgmTGv17j9v85TeB9xhBBvdC7f2gk5vxhYKCI6uLEitxhF2MmpfIY-xwaDR8q6JDmPefdLM39J-hAnjFDgBMMLJA6aiHBYFqxAq-u7RsT0E2EVHCOyPJPD7epISV38oCHGGFed0hm7KIOvaYQ_a7GXtpBhkKKORIx7s3I8SN2XcBM6vvBdeA9sLaz-q-ZiuCoJrswRFKPd1dJGA8wKRaSFM9Zb2IIzCCr53dYrQLp69D5Wr5RaM5w6oVXmm_hF6NOiBii7m0DoIcagQutp2w_107WvLzvfCPDJnAPk6sWMkmG6meLOfqmh1nGX7Wbtdds_bMK-X3_a_NQhtzenEswyRKFQKZv0aKlkqXBV8L9Q9STjciPs8ss3twrHs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0940fba80b.mp4?token=vl9sFMdFc_mA2FdpECrdjeimBfcLVepeXHjMs0qr4k7KX4jXwVuNUmtu2AiBKdkt5hKR4oiNlM8tMO9tZ3PczHLru8LqzlzMeb-d0qsl_VTAJZac_1B705rp9t7JiTKiCfrDaog_xO1XEikolqyIoTo4eIFap0M7eI-JXsYN6B_6x9dT2GBY9V0AugDU4vCP-aro9Tmhk375JrjOd0zqbgNR4MJQ2x0635YzT6ziAFxtxpq81WnQq3VSPeHLQNRdXx2kOYnxLF_YTaN14FdnRMbFkZEGsq8ZvA6nH7MihPpsNMjTWgmTGv17j9v85TeB9xhBBvdC7f2gk5vxhYKCI6uLEitxhF2MmpfIY-xwaDR8q6JDmPefdLM39J-hAnjFDgBMMLJA6aiHBYFqxAq-u7RsT0E2EVHCOyPJPD7epISV38oCHGGFed0hm7KIOvaYQ_a7GXtpBhkKKORIx7s3I8SN2XcBM6vvBdeA9sLaz-q-ZiuCoJrswRFKPd1dJGA8wKRaSFM9Zb2IIzCCr53dYrQLp69D5Wr5RaM5w6oVXmm_hF6NOiBii7m0DoIcagQutp2w_107WvLzvfCPDJnAPk6sWMkmG6meLOfqmh1nGX7Wbtdds_bMK-X3_a_NQhtzenEswyRKFQKZv0aKlkqXBV8L9Q9STjciPs8ss3twrHs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
سه تن از نیروهای امنیتی سوریه در جریان عملیاتی که علیه منزل فردی مظنون به عضویت در گروه داعش در شهر الصمین، واقع در منطقه درعا در جنوب سوریه، انجام شد، کشته شدند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.7K · <a href="https://t.me/alonews/147898" target="_blank">📅 18:08 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147897">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gs68jJduMNftcWjqLnFJWHQMZBtrKYJxze6ops09R6USswS8j-oiYr618jU5P7JpcxAU5pvtzppPug9ELH7HhrVJ-eE6GT28M6d6GsvEfHROjqSIoFODATtTGedq9OxuekYeGu7EJ2ugul_9yjyV6ki3ZefBkP2XcS5uErRvxZPuy2M1pExNupi0nV6fMBtA9wQUxl_z_AxCZRcpxwKSVHbmse5CovYGZgFGMdxyeyP4AL8EDd6ahlomjujJ0p3I_Ir-Wnbdu0BiTjBLImt2v027wbfqckbP4Nu-9O55BA-kDET4L2O_kBx8iqn0nfy_nMyR75ETlATKSO7WmQKnSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ولایتمدار: روحانی و برجام ما را ذلیل کردند؛ خدا ذلیلشان کند! حالا با اقتدار مذاکره می‌کنیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.9K · <a href="https://t.me/alonews/147897" target="_blank">📅 18:01 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147896">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cGwKi4V2oH8vtd9q5baOtjyjXTL3GlQ6PFWeMEJ9fuDyLeShAq9s8vBp_urfvD7zr4hVs8wj2dOnvWTCTVmCXa4Ss03pEqc5AwnF53AONsJgxtyuVgBLXTZb1JNHIqU5ip861NrUz5JyY4oAMhxxaHOBDGjpwNjfPJnAe24UA70brT3DNE13q0bDwjQG3rBLmfdbcRCNns6YWW0HEes-Qi4Pz_JGG3LgahIru7-MD_6PihsOSY6IOSjdcJ6GIGgdn0_vhPN-xIbsnE3QYaJ6ZW-O2txrthuW2LAGO6cEY3N9r4yVujOCc_QsgwPdefg_q5LAZbDRKdcsD3JWnp9PdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
جذاب ترین رهبران جهان با حضور رئیس‌جمهور پزشکیان تو رتبه ۱۱ام
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.8K · <a href="https://t.me/alonews/147896" target="_blank">📅 17:27 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147895">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GfOZTHX4YDKbZClY5LeSGGZ8W7Rau_6Aai94W__yXuhQXPst3AMb4p-Ioh5V_peIb8TBsAbd2jM4owxuiGcLA31rg00NvcKF7dw84aTEg6DdqwpuU3rMg3z4KQOZJNuWnZmJDpS3oqQk7Mpt8sikXPZd9bQM8r6RzAHIpRqYeEIA-YVaTa2KYxzTouem-Vx8x5baUQRrEPqfevGW1tWQkJGhv5QRQ2rwGAPl2HhJEwIw4PzP0WvEvernjDuZTm4wmUFq05FjF4Itb2B985KFe8OLz5HR1XQk_0g_CzKlkN1YXS3hFa6BJqr_b-GsOgADoDpO-VE4xVEOFgzK-ZquCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
قیمت نفت برنت به ۱۰۲ دلار کاهش یافت
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.7K · <a href="https://t.me/alonews/147895" target="_blank">📅 17:10 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147894">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">👈
گویا کارت‌های سوخت جایگاه‌ها به‌ تدریج جمع‌آوری خواهند شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/alonews/147894" target="_blank">📅 17:04 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147893">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">👈
المیادین به نقل از یک منبع آگاه: ریاض از عمان درخواست کرده است که از انصارالله بخواهد یک آتش‌بس دو هفته‌ای برقرار کنند که طی آن، گفتگو برای بررسی راه‌حل ها صورت گیرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.4K · <a href="https://t.me/alonews/147893" target="_blank">📅 16:44 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147892">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">👈
نتانیاهو:
تمایل ایران و نیروهای نیابتی‌اش برای نابودی دولت اسرائیل از بین نرفته است، تضعیف شده، نظام ایران را سرنگون خواهیم کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.7K · <a href="https://t.me/alonews/147892" target="_blank">📅 16:26 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147891">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">👈
سپاه: پهپاد زدیم
🕺
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.3K · <a href="https://t.me/alonews/147891" target="_blank">📅 16:21 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147890">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/16117ba246.mp4?token=RUUg52eqkVdl81x7qDtjF1zvdctkWdaYDoLorImXaTcqpRUhnDsi6qZ7mNUMhHQsKWURuxkxvfn91SHh9RyPm_vh7RHmzS0I6Ldq3BuL_ZCT50S71SCVAgZQZxyaBrbJ01Fy1k3K5UcjQkvcUcHD4OUhOImPqZ4kJFxScQLeIvLhDKAM9n4wpGhu91QwMUh4p6SYD1ZrzJouo0V4QpTkhr5fkmaJ69qXyJs_7u50zfqZnJW3snM2sgV5tdvTnJWihaB1JVMaIuKXzWpNEUTLCS1uQer4uBRDcM2CvzEV8Y0XRytmxGpWZTnS2u5nldh9zoyowzked0iFwZ8tYI0Jqg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/16117ba246.mp4?token=RUUg52eqkVdl81x7qDtjF1zvdctkWdaYDoLorImXaTcqpRUhnDsi6qZ7mNUMhHQsKWURuxkxvfn91SHh9RyPm_vh7RHmzS0I6Ldq3BuL_ZCT50S71SCVAgZQZxyaBrbJ01Fy1k3K5UcjQkvcUcHD4OUhOImPqZ4kJFxScQLeIvLhDKAM9n4wpGhu91QwMUh4p6SYD1ZrzJouo0V4QpTkhr5fkmaJ69qXyJs_7u50zfqZnJW3snM2sgV5tdvTnJWihaB1JVMaIuKXzWpNEUTLCS1uQer4uBRDcM2CvzEV8Y0XRytmxGpWZTnS2u5nldh9zoyowzked0iFwZ8tYI0Jqg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
نخست‌وزیر کانادا: هیچ‌کس برای ما تعیین تکلیف نمی‌کند
🔴
مارک کارنی، نخست‌وزیر کانادا، با تأکید بر استقلال این کشور گفت: کانادایی‌ها متحد هستند؛ هیچ‌کس قرار نیست به ما بگوید به چه زبانی صحبت کنیم.
🔴
هیچ‌کس نمی‌تواند فرهنگ ما را تعیین کند یا به ما دیکته کند که در عرصه بین‌المللی با چه کشورهایی توافق و همکاری داشته باشیم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.3K · <a href="https://t.me/alonews/147890" target="_blank">📅 16:19 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147889">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OuHL0wz1w2Bm5Rt5o9B8hGxev7f2uSBnNMo-wz608aTOZ3S5GtotLJe3jM7vPNanHW3S2C1H4Q1L1wZJ-kduvSHMPdgkm23cf-qttgk--C54lk33phubIZSk8TiMgatiEItEBY08VveItLcqjEYgizmDw8zwcmikV6Bym7LLia5KNyZAk_BDKiGGVkILQW1Xudc0x0mqhsSeUSfz-b7-UItNyPEXU-u5SbRPoLl2GNMCw73M20vrk9K0quA_R-S0cRpq8vNeWtDzo0i0V6RQHbgV_oPCV_qhNheJuPJuyLP2oTL8Bp-MYvJi0s3zm5vDTiCCkl_mtZT8x9OYlYxrmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پس از به صدا درآمدن آژیر خطر و شلیک موشک‌های دفاعی، آتش‌سوزی بزرگی در یک شهرک نزدیک به مرز لبنان رخ داد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.6K · <a href="https://t.me/alonews/147889" target="_blank">📅 16:12 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147888">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">👈
رویترز: شرکت پهپادسازی آمریکایی «پاوراس» خبر داده یادداشت‌ تفاهمی با ارتش پاکستان امضا کرده که شامل یک سفارش اولیه در حوزه پهپاد می‌شود
🔴
این شرکت قرار است با یک شرکت سهامی عام ادغام شود که تحت حمایت دو تن از پسران ترامپ قرار دارد
🔴
مدیرعامل «پاوراس» می‌گوید بخش دفاعی خصوصی پاکستان «در حال ظهور، اما هنوز نابالغ» است و این باعث می‌شود شرکت‌های آمریکایی سریع‌تر حرکت کنند
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.9K · <a href="https://t.me/alonews/147888" target="_blank">📅 16:06 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147887">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vz2URe8RUgGCJmh6bF4gQrxqu1YsrfF6ywY3_Dca3wZv7aj0AgnGo2SlDwLhoiv6iedfCoQ15NbXEh0X0JTP-cxNPrQc-iShqqFyKhSMSAxZgPt2k9jMzvzLJpodO1ROSNFtiN8udcuWlnSmRFBTyj6-w2-2nTwRhxIPXuMqVKSzVFiKpyQVTeUjOAg-EH4_fiR5AGPXKDl9_bPKL2oUoub52NvNCfWQgEtORFZ4TH0WxYWka6pbN219ly_bSQfLqqG0S39vJbYSLit4xfDM7fArNqXdZQo8-rX_BPZi1JXNnn0zBn-nDqhcPeXq-alP_XmmQehwY0pcL7QBFQcMiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
قیمت آیفون ۱۸ پرو تو کشورهای مختلف چقدر خواهد بود؟
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.4K · <a href="https://t.me/alonews/147887" target="_blank">📅 16:05 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147886">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j8D5BEwkGf0kxP1SNRTs_5Rke5my_gZ6_xqXwiF0DfKm3tHJhQATdrPDSVjhxgf_tMBBgsTrSxog5PHYFMiPRZLAhFhU9gXfYDlQII0eb3DW_QcehcRcus4SLXVnvmZ1u8zVvDT6tvH8tnHsUrKpsPZn0hHj0MdkhfJsOwCVZadtUP5ZyfF3HnH7JhgtYzBdlj1gfVcO-n2YH1e0xCo84DQRx0TSU3Hj5UpqLnxo8Xk6_95MgeAz6pwsMUfvGCicIZflqPLjlTerYSLIynSuTpOlY0i6c2TIwXFNjEE17MLb_YafTfdIvWEoYdKI5-KaCEloShO6x2RreckDqA81BA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ساعتی قبل جسد پنج زن و مرد که گفته می‌شود قربانی یک قتل عام خانوادگی شده بودند، در بلوار سیمون بولیوار تهران کشف شد.
🔴
اجساد این افراد در گور دسته جمعی درون یک چاه عمیق دفن شده بود
🔴
عامل این جنایت دستگیر شده و پرونده برای رسیدگی قضایی در اختیار مراجع مربوط…</div>
<div class="tg-footer">👁️ 59.3K · <a href="https://t.me/alonews/147886" target="_blank">📅 15:59 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147885">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">این تاریخ بیت کوین میاد رو 200هزار دلار
از این تاریخ پرواز میکنه تا 200هزارتا
👇
https://t.me/+4jOgodAq96dmYzY0
https://t.me/+4jOgodAq96dmYzY0</div>
<div class="tg-footer">👁️ 57.7K · <a href="https://t.me/alonews/147885" target="_blank">📅 15:56 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147884">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HOLSt5HSKFpgcugi5PaNDjM5qALeSL3vs4PrLZONRtIVaxxkI92Vht7sJmcZdZvLdtP31q4j0G_hqhBGeKJbGnp7OyU_yQmMuP_nqBWudj4DjKgXux-s5tQPo1eNqh29BeMJKfpooAvBQ9pE_10RtGZfocUIFa0fbGDrfTA-clwZped73K7wPyGOyl-CpBvMPLUhIUGNWqbrfELvrqo2SNQjQhOWTaF31bCIRlSudx_0V0la8AMz0D0Bw7xqeATIBW0yGyYdxiRGoQGW1moc1KFW9pf4gW-dPe2lne9xdzHlRni8O5E0IScC-K4_l562Mnpe9KcgMnGKaa-RLkeTCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
آخرین قیمت نفت: 103 دلار
🔴
امروز نفت برنت 2 درصد کاهش قیمت داشته و به 103 دلار رسیده است.
🔴
قیمت نفت آمریکا هم به 100 دلار کاهش یافته است
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.5K · <a href="https://t.me/alonews/147884" target="_blank">📅 15:49 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147883">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">👈
سپاه: رهگیری و انهدام پنجاه و سومین پهپاد MQ-۹ ارتش امریکا در قشم
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.4K · <a href="https://t.me/alonews/147883" target="_blank">📅 15:48 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147882">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">👈
وزیر دفاع اسرائیل: جنگ با ایران و سایر گروه های شبه نظامی ادامه دارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.3K · <a href="https://t.me/alonews/147882" target="_blank">📅 15:37 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147881">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/96265f0275.mp4?token=RS2j177yAqXfZqWAaGYuIOwQBl4QK4zIzJSEq2Tm0zC22mpxj2PEPhicUUijmMRl8TIYgM5gq1LBxRREZdVVH0Wvz2NoYcQH4VGNIMHY5e-LLj3Y152LeDHLr_0s1x050aROWScqtQPzuA31Rn5DDoj-HdUCAA1x7VkrLXrmXRlGJBrOg76OjXuMyDXnEbz79XgL00aw3vdfH_fTtws84E5tBNBgOiJWsSWf4ZgWt_JzeicnNigOFW2LYgFnhZ4JjyEpCkKM3nymF5Uj_S47vc6j-Fy7i0z7K4ZYPKAAKfJ9Ox6FkncDGGdzRasZY-QZn5Lb1sSj7TQWDZfJeOCwMQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/96265f0275.mp4?token=RS2j177yAqXfZqWAaGYuIOwQBl4QK4zIzJSEq2Tm0zC22mpxj2PEPhicUUijmMRl8TIYgM5gq1LBxRREZdVVH0Wvz2NoYcQH4VGNIMHY5e-LLj3Y152LeDHLr_0s1x050aROWScqtQPzuA31Rn5DDoj-HdUCAA1x7VkrLXrmXRlGJBrOg76OjXuMyDXnEbz79XgL00aw3vdfH_fTtws84E5tBNBgOiJWsSWf4ZgWt_JzeicnNigOFW2LYgFnhZ4JjyEpCkKM3nymF5Uj_S47vc6j-Fy7i0z7K4ZYPKAAKfJ9Ox6FkncDGGdzRasZY-QZn5Lb1sSj7TQWDZfJeOCwMQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
نتانیاهو: تمایل ایران و نیروهای نیابتی‌اش برای نابودی دولت اسرائیل از بین نرفته است؛ فقط تضعیف شده است
🔴
توانایی آن‌ها برای عملی کردن این هدف، اساساً به‌شدت آسیب دیده است. ما وظیفه خود را انجام داده‌ایم، اما هنوز کارهای بیشتری برای تکمیل باقی مانده و آن‌ها را تکمیل خواهیم کرد.
🔴
ما حماس را از بین خواهیم برد. همچنین ابتدا رژیم ایران را شکست خواهیم داد. آن را سرنگون خواهیم کرد؛ سقوط خواهد کرد. با حزب‌الله نیز مقابله خواهیم کرد و آن هم سقوط خواهد کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.1K · <a href="https://t.me/alonews/147881" target="_blank">📅 15:33 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147879">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KfQJfYREYYFRYC6p6P4ceUMlcVOj2e3nlJKCDp0ub6mtiDyJWMoCAad8-xvJHkyWICkaeLrwDtc7aJFDmiSLCtvgGU0pS2jXxtiDZtAvwUclerL2iVXJ3vQ58DejdewCLSgrzLkWXic_ys-ILGBd9cyTehzRiz6R6qCBJ2bLDxaHxi8hk7EgVag7TBtM05fjd0f24y1u0lpZX_XQmdEjfkrWUQLrG8RwXaFv-kJr_b91FiAxtbzalqOjwE070NhrVZiR_Rm6EdXmhcFZHrdypyh70zYyuNf6UQoBlapD_th1P-K6zVyY1r5w69SkXKp5Y2NsnQkTnok3i7MbHkh9oA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Taq7KjPmF8OhlnAJEDmjvckUrbq7cpr_H4O5DDv3eNC26CZsnK1HCi5-UmK8ii1IfKLHUy_ghblYH5zfZPSfsrkcQcYeZ867pGMpFAT2UvnWNX5f43vMRHL6A3rkLfWLJszzqRv2J2yHSODCzZoqkvy52THmcKi62NsojGWY2yYAt6EW8GfBGT3j9bwarKqiCaiys5GM6C1mN5U5Hu2OoPGxnMEkdXcPCoCwguE4ciXx0AnYnvWTP3ysFcahfHYakZmFLU_jhPc-JIlBJHzPGJMZWYPYKXXnYE4piR2q8Mc-qyBUNOozl1AJLFxEqLsdRgSZAAyK2w9XhN1szYM_VA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
فعال شدن پدافند در شمال کرانه باختری
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.7K · <a href="https://t.me/alonews/147879" target="_blank">📅 15:32 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147878">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QhURT3mSz_aqD_OAEiFXxvh9zfUghmSZAxB9rUD1i-kefDbAJ2jDY-CFvmY5CRfkToSCEZQ_3LUfO0Y3SDp1AvV679Idtd1JwG2J7bI3RNeGDvspfvFNXVg3fZ8T4v2R7rIBLwp2OPaF29L1EOYtPU4ty4XAF2_ILmNEyRIBGZgv3eI-Uf5Kp6i4WPFyiiiW_7OVxsE6fXBw1AJjUh4mmL1hue55GR7ESFz5941AS44UsEaJTFmv_aNrIu7h88SqIe21uasmqP4pMmXJLElIrl_fHhLfzJCRyNimhis_GIvFV5mJ5HhOoohjXqiR-NVjXXR7yTztBmGRChK0x49uWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سعید آجورلو، عضو کمیته رسانه‌ای مذاکرات: آمریکا برای کاهش فشار از مذاکره مجدد می‌گوید. سخن ایران مشخص است؛ به هفت شرط مورد نظر تهران عمل کنند تا تفاهم عمان- ایران درباره تنگه اجرایی شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.6K · <a href="https://t.me/alonews/147878" target="_blank">📅 15:26 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147877">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QyEILBrUqo5V4NLzwL9Ie2jsKD2xw4YP5P1g4L_Jq4Y7zEGrXJYsh4X9qYx7JU1cPF1Tuz2G4LD9qCvrFToOBe1ZWYuS_9PKn-4JO4NjB1nGAWJwRroUcZt-TPrB6bbPkzhX24xPWqmpbTT6E3IgdW44laEQyu8PZu8pWp6O9WDcKrNG89Ij0b9q3-NSTG4Zy0BmANgQP9YkE8tfJFxyIRF0arZxBzrC5OUpu65zO-5jkb-u_9Ylk0NFf0Jq6iXFfUV_O5StxPOkrN0KjfblsIDYQtkTyQfeNQMDcMBZKHWAE6eVBPjMwx-SayUJhUvtW_veTlxzXOPR57-JPupkfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
گزارش ها از نفوذ پهپاد و فعالیت پدافند در شمال اسرائیل
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.4K · <a href="https://t.me/alonews/147877" target="_blank">📅 15:16 · 26 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
