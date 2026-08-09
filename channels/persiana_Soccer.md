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
<img src="https://cdn4.telesco.pe/file/nBja_PaAtjfv17as3K8SYSnY5bRISapIadX28JUkSu7jtoQOufucreL1E8v5YeULgp7wSkBPExmNtx4qb_dACZAZFjgQbZ8TTHS_JeEkRBPGuAoDYWyDYVUXpzodAxFRlKYKsx2cjbpHlCSb-NPaZgS_TlLFiJOx62IeTYSMLd0hNXWBUIgtYvix8L7gieag2NA9UekktRMAk8C5zOxxYmNgcVcl1mPKjtAz3IVD661kKWiuIKZWFeIZgaJVzQXk-L5gMfadYIGWuRSc9Goa84Ezlo_QiSV92hLEssvujdbEEsBuKL5sM4xbe0i48BFUMt-BNHaatT49rPiIbyhBHA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 635K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@adspersianaکانال دوم رسانه مردمی پرشیانا:@Persiana_Plussپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-18 14:29:34</div>
<hr>

<div class="tg-post" id="msg-27391">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t4ZX825WWsT6oQkjn04eT7A2U0iwwWSPz708AUsaciKsIYe8TJ5qu98lgc-D8-BshNenG3-ueCafjahdXV3dn6JkYM5BbGNPy5rv_1rVsNVGpmifSAehPOitPJOpFe-TSpryL9qmFe-3JlOj-gMIRmAsN3K5BJ07LrbSwxQ2emeapf9wnCHeIVccvFnpsP-4xcf190o-6IUFu1kzziNCvVQV-Y1HUTtX6pjrjUUgw7gQoFjC9ci25TeW4bwPLiQB12WbtZqTxWmtT9KoQ5AQYpCKyM0ZabJ_H1aARSAUiigsZHMU7o3wiVYuoSFm2rWqhTRT4j55D5vLRTCgeGod3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ احتمال داره جواد نکونام از بین صادق محرمی و مهدی‌شیری‌یکی‌رو درلیست خروج تراکتور قرار بدهد و درخواست جذب رامین رضاییان بدهد. محرمی رو مهدی تارتار برای پرسپولیس میخواد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/persiana_Soccer/27391" target="_blank">📅 14:15 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27390">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j3mC6JNE7nNbk8fUCYXUZdN-TcVCm1_rR6U9sSNBxDoIs7TvYLJ1SC7-UDvZbBo43jeDR2hZ2u_hPgWuNjDisJ-bSMAlKN1OaZ3lEzlAJKXqJiqZ7cdqNstJ0A0A7xXSK6ky-RHUOUD4nzz7EJ70kBZRo_prY6n8Ik1hkvVeXFNvuw-DTJwOpFeWQ3Stg21Da_JJfJYOvuQt81JbupiJ5w4WzHadxSHDWslOWLO7KgGALc9pkE_HOl48K51mlMVwnrrHTy89FbLfcRmydfRkjxOijpgr_0-vFl4zM0WGUmZ-xtebJV9TcPMj2IgTxdrG-eyoL_MgxtqWJjTo8rtXvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🔴
👤
طبق‌اخباردریافتی‌رسانه‌پرشیانا؛ باشگاه تراکتور رقم‌رضایت‌نامه‌صادق‌محرمی مدافع‌راست30 ساله این‌تیم روبرای رفتن به پرسپولیس 100 میلیارد اعلام کرده و از طریق مدیر برنامه های محرمی این موضوع رو به مدیریت سرخ ها اعلام کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/persiana_Soccer/27390" target="_blank">📅 13:36 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27389">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VpQdV3vvTm5h-fu987fA-5_kVOWo2rTLzeTkYXT9os8qGRcXvjcF9tz3ICcqz4GKsms8HP_UYnYb6fYaBO8URQxQUJQSIhM2mZKkvQiFS_ZUE986W4Na2BsfUz6bjrOEXgeaBkUPFCQQbSrWhunFmvKeBhTtmEAUX59fLHNw7TtfCVolXgwhY_iM-KF1aUDwnQ2a2wbqqI_W7L-zNjEGLMemqnXmlozmdBC8FdVc6PXyrtBpu2VKn0VY3Dxzo3jD79qQI8mNM3PXoT7vY91hksshgj4Ayz8qwfgeMjukjJDVVSWoawFhYuM9MkzhkeiOrmgVblkx_JA5sreKsLXFbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇪🇸
🤩
با اعلام جرارد رومرو؛ دکو مدیرورزشی بارسلونا هم‌اکنون‌درمادرید بسر میبره و قصد داره که فردا بامدیربرنامه‌های‌ خولیان‌آلوارز جلسه مهمی بزاره تاراهی‌برای پیوستن‌این‌بازیکن به بارسا پیدا کنند. چند روز پیش مدیران باشگاه اتلتیکو گفتن آلوارز خودش رو هم بکشه…</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/persiana_Soccer/27389" target="_blank">📅 13:27 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27388">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o0gKfpW59HnbdY3EKzBQZS102mfRJHX6QQLuJ17kjPOamGyp_EgPebRvy9XPUVF9wwD7Ve1Yb7GTY96o3reSSMcF68BmvErIADNtjDbHIwnYTrrzcEuRKjmKZY1B5zvOywJssLHHWAI9RGr2LiGsOd9sgipDWYQMkSEhDkE2tz7fL6ktKg2Od4JP3Sq8x3yV9jW8anIX7vVXkRkeJhyxu02CXqa8xlRfwjalHvRBkw648caUiuK6-lXFFPeVsVcaet43wVDSn4KcfAXX0EK5VEZayQWygTWtyYTQ45GC-XjdUwKjoRezuY-bNiGpYkYms1dLYVBmy8ttQ853DkcKCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تایید خبر اختصاصی 28 روز پیش پرشیانا
🔴
شهریار مغانلو مهاجم سابق‌تیم اتحادکلبا با عقد قرار دادی به مدت 2+2 سال به تراکتور پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.3K · <a href="https://t.me/persiana_Soccer/27388" target="_blank">📅 12:52 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27387">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/222f7c35af.mp4?token=mAQ7DUWws6fLFJHKiPGj-SO5SWY9naiRCRRWzQkaWUzSCD6v-K0GKCW459umL6UC2P5IWMnR9g3-Cjr0y9b2VvH-B-KGhCNJq_zGRBNaRY6Xw0izovGjKoX9h15FJQon1ldN7QdMPXdBFAGhsbrR1slbZhUPU8uZGfl0vPtmINem2ERHWRvi1UC5uRLj4EX5I-CGUAJtKucSL5rFNdEMXv5wMEysYATRZU21acFoGC2HcT2Kw6MC1y5Q3AHVvK1SkdnJZ0It-KHyptP0Vg5igCQljmiZQbxzvc6A5DsYhvV3LECLddoFV-ECdRy2U9NTYyMqghnSPpWLuHhlM53O_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/222f7c35af.mp4?token=mAQ7DUWws6fLFJHKiPGj-SO5SWY9naiRCRRWzQkaWUzSCD6v-K0GKCW459umL6UC2P5IWMnR9g3-Cjr0y9b2VvH-B-KGhCNJq_zGRBNaRY6Xw0izovGjKoX9h15FJQon1ldN7QdMPXdBFAGhsbrR1slbZhUPU8uZGfl0vPtmINem2ERHWRvi1UC5uRLj4EX5I-CGUAJtKucSL5rFNdEMXv5wMEysYATRZU21acFoGC2HcT2Kw6MC1y5Q3AHVvK1SkdnJZ0It-KHyptP0Vg5igCQljmiZQbxzvc6A5DsYhvV3LECLddoFV-ECdRy2U9NTYyMqghnSPpWLuHhlM53O_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">برگ‌های‌ریخته‌شده گزارشگر بازی امشب سپاهان و ذوب‌آهن‌ازپرتاب‌های‌بلند نادر محمدی؛ واقعا قابلیت خوبیه بشرطیکه‌درست ازش استفاده بشه نه اینکه از هرکجای‌زمین توپ رو بهش بدن بی هدف پرتاب کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.5K · <a href="https://t.me/persiana_Soccer/27387" target="_blank">📅 12:23 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27386">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sH9lJnnE546qOYtBupFPqz1-jgKLrjRYO5O6wz-wp5uwM1vnXpkbDJ6MOpLE51vE6vYxY2J7nAdp2HP7_y2keeEVyPb7ctryOC6q3n2l72zNHWXifZPollWtdxMytIdxn3ldc-IHNdNkzN0nZoduTEUIMWUfduHZfoZHXyfoP6QBbrqjzXY6CvmPhUl6o5So4ZuZlfFm1Gjl7C4W70YzHoLSZGrTaYQ71g79-n7_iIlJ5SRUmkxn5mXwHmkXfKh-AdKnLzNuxvVbWPDZDxQ5RHzp786ozrEEEMdteYz9YQda55hIUpZ3vbp_0hwmLkWFNnZCE9vi_dHYU2Eji7SN6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🟡
👤
طبق‌‌اخباردریافتی‌ پرشیانا از اصفهان؛ مدیریت‌ تیم سپاهان‌ با‌ حسین ابرقویی مدافع میانی 29 ساله باشگاه پرسپولیس مذاکرات مثبتی داشته و درصورتیکه حسین‌ابرقویی بتونه رضایت‌نامه اش رو از سرخپوشان بگیره راهی اصفهان خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.6K · <a href="https://t.me/persiana_Soccer/27386" target="_blank">📅 12:02 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27385">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tuIwxSD7EkRn8SBRG6vqu10OhGdCD1c86QiJbIIdtQKLOEqf9W8DVOIr5JSWqq2UMdEIh9GxWCrrrFPHi2YQcmhbb_QhFAKFuL2eMj6zeGsEP9Vc3uO471n9UQU34l8vqTNPRqlqKe8IdVFaAf0YRTKqRnSCDI6eGbOn7Ps2FhfDGBA6wrQ4gJv-rK20Y66h2Kq6qlnk_i_M_Y947OpJJ8XyjWLWP47VTXInTCiRCgnQ6J8elwRemJbBfTzQGZOzfgVPH6PiL_N87lh_6a3-aFxjZ1yb1dydUoIZo96AFl8lpDPK2xXYcvmGdLnTW-Kr3M9jNCTyfan_ten_BqfsuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
#تکمیلی؛ بزودی فابریزیو رومانو خبر پیوستن قطعی رودری به‌بارسلونا رومنتشر خواهد کرد. تمام توافقات شخصی صورت گرفته و توافقات بین دو باشگاه نیز در مراحل پایانی خود قرار داره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.2K · <a href="https://t.me/persiana_Soccer/27385" target="_blank">📅 11:52 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27384">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hSib_VRNfGGXXvefXrrNqCkPasMz8oGcxbGK3y3Y2pwdpyzRTof56N78P6oSZV2EH9uyUa1Cg9U1AQYdcPPV7X4FOTYDZfZX42zUkliThd3Z7oPhmLJ2pa_GEEHxp8vyvWmSxP-dYqJETY_FhlWZYFfmRtN2U547e33LJq_lrMkWZTyfEkwirsli82BKjZdNSnqmTJ_6M9_miXmnmW8EDpQIv0CqceVNpFJXochUv5pTRujjHkVVNpALIP_9kfyeCxek3TNgQCNt4Kj3yQj3YjN3BtvklIG71MYvHRLpJk-TzadH63BH48Go_7O1UXmrHrGz28IRZCdzoyx_f8B34A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ عجیب‌اما واقعی؛ رامین رضاییان تنها باپرداخت 100 میلیون‌تومان قراردادش رو با باشگاه استقلال فسخ کرده است. در واقعا زمانیکه نیم فصل باشگاه استقلال قرارداد رضاییان رو تمدید میکنه بند فسخ 100 میلیون‌تومانی‌درقرارداد رضاییان میزاره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/persiana_Soccer/27384" target="_blank">📅 11:41 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27383">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oLQPcxRwTbL-NA2GJMdJRpMk-LIMw2GSDueaJe0pqpKqfKD5_QNjtnDBwW8mYboD5DAF1nWVWG8S9yZcBF1BGtfS16CGUif8kJeECQUUDQ_CrMOlLgrcWw9JoupB9mzAfeKdKOHQOEYsQ7qLxHDnRBrMLm03VUZEYqtnu97YYdyXDTLJl7hvilDaLCqzDb67ptaiOAHk4Tt2fTUrM8VebtWFlftn3RECxAeDB7bEJw4jbeh1JLx8XevsZBNlZCxaTNE8QOw8sTEGKiWBQFcAhc0w1vIdF_3dN3HrRsW9HEmsYc_OQfMRBiQl8pMQhmt3R8avf3JVyRhA1-AxLUZLqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
بااعلام‌رسمی‌باشگاه‌تراکتور؛ جواد نکونام با قراردادی سه ساله بعنوان سرمربی جدید این باشگاه انتخاب شد و جانشین محمد ربیعی شد. محمودرضا بابایی چندروزپیش گفته بود اگه بزارم جواد نکونام در لیگ برتر فعالیت کنه بی ناموس عالم هستم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.2K · <a href="https://t.me/persiana_Soccer/27383" target="_blank">📅 11:41 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27382">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jr8Bmt7Vn169m395jP-Ui4CsQ4GGSG3R5VLzN4obGEve8LQpHfI7OKzByu7-IEduflFHx8_PmoMTy_4RDJUUBrg0nAqOR_43Z3YSj5BpaCczBH7jNNfmFVj8G61ohdLjGYue9sjY4S4suR5JNAQnaJkpFSFAREAdNhKmlWB6lpZmONCGHB5R7IxA7_vu2s3Jb7am4vfRkfdeSNU_-1bjCBQZenFLGODj54nzgRzDPvULFuM_L_jGKNKO_Z_0KSgmikYn4E11NPtXUjjvAPzmTsed1VRiegMdquFJvmbCMrpCb8YPZ_XHs6H5drslj-pItIg2U15DExjsk3afrlhycA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
سایت جهانی WePari
🔥
😃
😃
😃
😃
😃
😃
😃
😃
🔥
بازگشت باخت به صورت هفتگی
🔥
پرداخت جوایز سریع و امن
🎰
شارژ حساب از طریق ارز دیجیتال و انواع ووچر
┅━━━━━━━━━━━
🎁
کد هدیه ثبت نام: Wepari2
👽
ثبت نام کنید.
👇
📱
نصب اپلیکیشن اندروید کلیک کنید
💳
آموزش شارژ با کارت بانکی
💸
آموزش شارژ با یو ووچر
💰
آموزش شارژ با ارز دیجیتال
🌐
آدرس سایت
👇
til.ac/0L4vyJf
til.ac/0L4vyJf
📲
کانال تلگرامی
#وی_پاری
:
✅
@Wepari2</div>
<div class="tg-footer">👁️ 39.3K · <a href="https://t.me/persiana_Soccer/27382" target="_blank">📅 11:41 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27381">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TtPz8lTzq6Q2tFdJTqYdqbKKnIS38Wkoym-y8jBRX4jTVBUkGh6VnBivh3r5sQpX7YqPejN9loefFZY5ENnPUXjzke1tnuUxcHXUmfKsahDrRktvb0wOP323R3GUj7IMljC3rDLORmtRjhU3FawuOILUYOXsVX0d5vQsfempd2hGZP7XEsK9_CqjB-dfPoY1ch_NqHd_VtmGzK8egbGOs9G3_kbnb6X_IlioZz0mi_iNNqv8pYMpZ7WaGbfgkFY337hLCihAhdiKXOqTPEItdaVwygglUnK-FTlxjo9zcgN3bkcF-Ws081rPXCI5flbbJO0X_KQD4j6fQ8nUXzceXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
بااعلام‌رسمی‌باشگاه‌تراکتور؛ جواد نکونام با قراردادی سه ساله بعنوان سرمربی جدید این باشگاه انتخاب شد و جانشین محمد ربیعی شد. محمودرضا بابایی چندروزپیش گفته بود اگه بزارم جواد نکونام در لیگ برتر فعالیت کنه بی ناموس عالم هستم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.1K · <a href="https://t.me/persiana_Soccer/27381" target="_blank">📅 11:15 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27380">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L40STQrru7Oe8WUnHo7NHTuDg1ifueeRTKlyZaye2a5P-7OkdkdRb-_019D5khUa4UtLDwFdoSEkWWEYVHZL2chM0f26M1GpEfJBIwy9RLxDtHbQs0T_sM21SagSwA1gQdbHv1pWGR7gPprEt5Y6v33XTealleAMwsitOtJxitOLwU6P991tSp-kBH7MTXPYIvWvDWadjkSVfuWujTx4g-i2U9krI-rJueVs3_9LtaRMVjjEJeKg6GNqlN47BICV9HTAUxXKelcAdO7NvbpWvq6OnwXkHzccTW7o3kLn65BLbFxdVO0dSArpQelHEpOhepjvI7kJCiILPaXM23KEuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#فوری؛ در آستانه شروع فصل جدید لیگ برتر؛ حجت کریمی مدیرعامل باشگاه تراکتور بعد از توافق‌کامل با جواد نکونام برای هدایت تراکتوری ها محمد ربیعی رو از سرمربیگری پرشورها برکنار کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.3K · <a href="https://t.me/persiana_Soccer/27380" target="_blank">📅 11:07 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27379">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qvWWUFD2JWPwOIJhVzP-3xyNRGzRLYQDjRUgUtskHQ2kV-Zhmia2zFZrj2_ySXE6rzbo1-Ooy-iX6OIHEFdz8MO_mpqlF1bNct_QoL5hzOolCx6RI8CrHiZ_jIlmY5ImDdoq3_ManlF6n1zbL4uivF3oDkmC3JXuOv1_1vRgRe8OfvwpQCPACN4knLli0kWWTncWoBenXF8U5x20gXE0Y_98g41IMkZ9ERQYVQ6yIQIwbF4FBZXqnSkK0Nks7tffyShs4gAOkxORj8DCJOx9Xgg77lF2K46XduZbVW5OlGCqyLhjIS55GWyez2BmpJ2g_W0ePagwk__OS7wqswyN9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تاییدشد؛ امیرحسین‌طاهری‌مدافع 22 ساله نیرو زمینی باقراردادی پنج ساله به پرسپولیس پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.5K · <a href="https://t.me/persiana_Soccer/27379" target="_blank">📅 10:50 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27378">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dkmgmYf1ry8DuDRMUCsBD7jgOAR-TTDynqSEyme9J1otYu1GlXDFS0rOctrcJbJaWMjOlvGyCLHkxluVQT3Dyq7Hb3C1bpcHz5vh0k43gZacMaC-qaCk9ImcJ_qHCi_J75_oj8MPlntbUMplYUj-39JFdS9C9EyaN_ENEt2UQ2oyKip3P658GVrHxAM22MrwD9x0Yo14pAEkUT6e5fgdqZPtUqG6zqXZVuAhX_KCVZh-VamHpkECNhkb_Oc1aJnsLxmh1XdsF0GId0OBmeFACETDBlSBS5ukisITGndbnedM5EIsraTX6Upr2lGLGFDgCoXerrYHUt-u6x6ahK9taQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
طبق اطلاعات ما؛ علی کریمی از تراکتور نیز آفر بالایی دریافت‌کرده</div>
<div class="tg-footer">👁️ 45.7K · <a href="https://t.me/persiana_Soccer/27378" target="_blank">📅 10:29 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27377">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kkN5FfQ2ZAn0kCo3xpkuFkqn3uGjp3CIRHAr0c10MuKZwq6BKBKKmPeVX13YDPoohaA_wN1D2ETRkPnY6JIJ_YQW1gwDowzOE1Bwvb0U8OhQe4Ew-xdsDdg4WN1MH4r_uijhlaHGOlYE21bNisRmtzJLCFrd1TphjLDJlDm01dEnmKZm2Sa1SeBS25uqbeaZCEtv8g2Mgkla2Kb7BymIA7ijTgb7_e-M_kO8xy2oAS8CDtEeujWev-ArAddSfjCbKRhmUfVQ-a0jN0YipjRSrLUtCIGasgt510AienvOBfRwH46o7BfgIX-1q619k6iQnR0h2i0zxHbph_SjFvp6jw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#فوری؛ در آستانه شروع فصل جدید لیگ برتر؛ حجت کریمی مدیرعامل باشگاه تراکتور بعد از توافق‌کامل با جواد نکونام برای هدایت تراکتوری ها محمد ربیعی رو از سرمربیگری پرشورها برکنار کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.3K · <a href="https://t.me/persiana_Soccer/27377" target="_blank">📅 10:08 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27376">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vejud2YuWx2bk3QFHwO5GbgBUhi-MxwHyUmRMrWd8jR8Zpt9OcgXWkvgefsqB02-JNDA9RbnhPaM4zFoWavAEcyZn3STCEjvh1pBvdyyv0OooBS7dYLbUQBqhRI92K-nTeSlXF6cYsimJ3-ojfIVKydS45Ob9R_HKaLNCc9DHVH4DVIJcJEPRvNBk1aR1jMYtjlPt8MzicuE29xZrBv-QKQgGYoAjM9AmMjgBrNfM_VGh8I_m9qR3RmfbidHdPNFzWpmojXTNPNHAgBgtYuhziSSbVS6nD9zWxCNho8QROun1RLsw9pAnyLeGSTnKq7T6-jfj7ISZbGv2KWI9mFV3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#فوری؛ در آستانه شروع فصل جدید لیگ برتر؛ حجت کریمی مدیرعامل باشگاه تراکتور بعد از توافق‌کامل با جواد نکونام برای هدایت تراکتوری ها محمد ربیعی رو از سرمربیگری پرشورها برکنار کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.6K · <a href="https://t.me/persiana_Soccer/27376" target="_blank">📅 09:56 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27375">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V4RmvV4GRihLa_OKyn24zxZQ5Zb7eatQ1-D_ohwtu8lR5oCWuBULk5FxlO7P7WiNa5CNbza5joW8TJverIYmmCXTLQOiuQHs7NcLHRJJ92s8rwRF-sYNkDbKH9SOGlw6XRcbulN2rSRb8vIS38kwvs37_Z1IEGUG2IzsGiZ9AKT8Of6btFQNcKbouEj6N9QGscFeGIPqEMp9i8eIfFBGux5TILsb_yaujHYR05KlagnfbwnrRDNamuiHbv6Oj-nOVptDQMSw_VWz8sNzdwhscyzUdA13HdbHt3TawoA7iujtXZzHVyzbdTVUvUtI7k9_89SjYgDXfZ4h4P4D6yvVBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#فوری
؛ در آستانه شروع فصل جدید لیگ برتر؛
حجت کریمی مدیرعامل باشگاه تراکتور بعد از توافق‌کامل با جواد نکونام برای هدایت تراکتوری ها محمد ربیعی رو از سرمربیگری پرشورها برکنار کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/persiana_Soccer/27375" target="_blank">📅 09:52 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27374">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rga2m_hiRxR6JjJPieiqymKSD-7f8pny8Ua8dbyx_Tohuo-6uOpa9woP-dNBIw1sZiV5K_aqWeiARS-xzQEGjhQJz-9z6BWsPEL2uDx1WsUuryUYsO3vCKbJYnQDrbSWoIQGSo8OfWjNCOvw10KvcrjKEpeCZk8LsKzSxFKnggvLWmPIMXxN-iiT8h6zOzIVHnWFoec-7ugdky1yYSS_pboR30Olf4dpXLMlLIEHzbHpTQd4TZ_SgsYe5xw1p-TU8Z5h-v_RnOlDcb6CAohtPWpU3YUWo0aK1HtyTR3RBpi28U7OljJlDhCpO5Vkb4sZhQw4PiV_PbOM64iQVJ65hQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
به‌مناسبت‌شروع فصل جدید لیگ‌برتر؛ 10 رکورد تاریخی باشگاه‌ها در تاریخ لیگ برتر خلیج فارس.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.3K · <a href="https://t.me/persiana_Soccer/27374" target="_blank">📅 09:47 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27373">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S-Q1medUUtwYp_bGuAMTdoron1uVmx7kPVI4FdANjAkW2HS8i2R0lcFtgFy-CCl6981nc_JKw4wzVzSScEsG06qsdJJK7jy2JWVfufWEVdb7tde65nMK1kjEbEzlriO7V2hBVUMRQ_BwBwX8PE_yZ-0MgMpG4cD-GYvaIesKGtQwuFN9wwqrXKbEGYT5mPFMzn-05kL6Ms_09ih9N47OKnc3C0uqUrbVGJ_lhit0rG2bGdcFwYISEP5GE53-6OUfJNpO0o2-zUmNGuk8HbDgu88UyXyrRGdMCSTbsAZspRFqrlG8ayNUIpimg4io7IRctvPpHwTL0bks92yOJewdrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
خورخه‌فقط پدرمسی‌نبود؛ ایجنت، مشاور، رهبر خانواده و... هم بود. موقعی‌که مسی تو رده‌های پایه "نیوولز اولد بویز" بازی می‌کرد، دکترها متوجه شدن این بچه مشکل هورمونی داره و باید درمان بشه. خورخه‌که‌از پس هزینه‌هاش برنمیومد، این هزینه رو از نیوولز و ریور پلاته…</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/persiana_Soccer/27373" target="_blank">📅 01:17 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27371">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NQfJMxwzxus9X0hnzgENBIy6nwF2t-HJL5GlYrziVj3WA90X0NaPRch53VqvGpUgHTy88ltiFWffzEYXmv-wrYZLLudemVv4DcVxIyQXr752_AIU9J8crMdIr-0rSBattpuejk0mebcvVpkm6ED3Za_5_h0dKMuW5eSx7YWgnSREc5pKrQbYXhu-HlDd9EauElAaLv4O5e17zBj2pGDpHMZoYez4ZEw5GLIJnr9aV8FHVxnEdlKucln-HJETFvFm445QsnNPoCUC7WQZ0MnHe675ZWIdxbdoDFlxs9e-u4_byNHyH25M9qUoTmDx8UNVexSMrVLloTyJB0F3e7QJ3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌دیدارهای‌‌امروز؛
از دوئل شاگردان مارسکا و سیمئونه تاتقابل توپچی‌ها با دورتموند در امارات‌کاپ
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.7K · <a href="https://t.me/persiana_Soccer/27371" target="_blank">📅 01:01 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27370">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZEjV4YOIOAZOhTgaSSe2GbvJlDAV54bueRp0s58qw1JwhYJJeMUWwlWuJIFf6UCqGyehKqba_bnb1pLSYHqPS37HHQXzZwtr2iWSiTSMRPqNBxlqMQGv16jNDACxXoZDTjWgH3CpiilmDlrHD9ymsjcp1XAsUOyv0fgoagakskEwffrWy_isvoPzATc0oVzTZFequBm0uuY76QtuSzaOJxecs3jHvtU2Qf3jebrudfqhZfqeYXPw_XLcpPVn0rlhRz-lriEHD4cs0ZSQscRrE4MIkkWXo5zA1QCsmPhz66JPnnbIzabxEbyuaOAskyyOV-4B7pE8u0olRuMk6p6L8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج دیدارهای‌ دیروز؛
شکست شاگردان آموریم مقابل چلسی و تساوی در دوئل پاریس و یونایتد
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.7K · <a href="https://t.me/persiana_Soccer/27370" target="_blank">📅 01:01 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27368">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sWZJ__ooERljQtUc0qjbiV6yGsDLGxl4IlPOfOo3amYGQR_7E0e0n8ZxVzB4jzUl-TDtNBej7xWMcm6ICslhqWymJ_goYGg4h_er5xCxuR47rrmrMiBfHTRypDrzFjtthHLgXa8NQmvFDf-lJmpvNjQqsyuCT6fpeGl7tYgdvn-NYsN7uAUS9iGDFqa-n8qhJoaYc8ZXzvM40J1Qkc_u4qhGj_S1KD05Lh2-Nh3TdSsAuJzGIuJQe0biXOMl60Op9AdAI9199BQsaxvOQ9lpTjYFyyfckcj_xBFBekqe3G4nISoz6z5WvgrZexc8HqI7jKdbDP7l_D4eK3sGhImIRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📱
استوری جدید خدابیامرز دیگو مارادونا افسانه‌ای برای درگذشت پدر لیونل مسی که آمادگی‌اش رو برای پذیرش مهمون جدید تو اون دنیا اعلام کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.8K · <a href="https://t.me/persiana_Soccer/27368" target="_blank">📅 00:50 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27367">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bCjNB_mJ-sYFAqt_ALeEmzVa4E7XqsF8nU2uZL8UI3MZsk42lFr1ZmV72CIPYmGMfRPIj5qkDYZmpmfBRvrIBe00BRM7EXU9pfws5oKHxxb4jzIB9JGmTsUR4O0-aHJAt69B6oh9OtjCwGNkcwNCTnYmOgziJr80RUppTdnM9REWvumoDIQzUNjFWWTApjttzGASSYVBvcgZN94EhqfWW2HiaB3MDOgxNe7S5dzzSKk-mLQETJFR_yPhENtJNWKiV0LL3b3RWQRMmMYd7PT0FlXTnKqYotto0NXv2Ctqxp5ecWxN2nunOFg2MYLmpFI63fd8eUdH_QW9HKT9_AZKxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
🇪🇸
از پنج قولی که پنج ستاره تیم ملی اسپانیا درجام‌جهانی 2026 دادند؛ دو تاش فعلا عملی شده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.8K · <a href="https://t.me/persiana_Soccer/27367" target="_blank">📅 00:40 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27366">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rV0uafUj4FmdgZzFJgvVOOAOZlEHKpq1IHv-_mwVJDM3AN62yr_ggsHg5VBirMqnyEIdiJ6h9URu5axKkkAHlMTfp0ckCuDC9TRRrvwP43cp0y24nYAZYqnpsd585ged8uB2tU9xr4OZUPe6iLHJilLK3_znn7RqBRBVJM6o5Cuti421A5qWS1LBaYaueqlh_iJ8OPnhVX7Khsw9CsH8pLNpalAxEEKFn65HZo99eB4DOYb-ktNB6CC3nuwAd2mSq4gFq5UKwLdyx-9SrqSTvZbIV8y4qOhJrfFS3grnelsOM4ietTmRNHwxbfqEh-zKGR_FnhqO9FevflVzw5UpFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
#اختصاصی_پرشیانا #فوری؛ درصورتی که محمدرضا آزادی مهاجم‌استقلال قراردادش رو با تیم استقلال فسخ کنه احتمال این که راهی سپاهان بشه وجود‌داره‌. ایجنتش با مدیریت‌سپاهان مذاکره کرده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.5K · <a href="https://t.me/persiana_Soccer/27366" target="_blank">📅 00:26 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27365">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J-cfVUAcfrdwzNDEKXodHcjCkpTLTZzyLq616rw_cwA3euM5zy0tsujsskurHLylFhSsSvLn0Tbm4ELtXXHxgbv7M46wKr5Es7cE6585NlIWVi5_UNHL-HNxp10WJ3A-Xs22kb_SdllurY1il4w4oN9v5DABVKGdt0pX-hOiRT6V3eA4ndDftFe09nfvO-Pmuwc85WTQ5B0v8NthoRyrv42QjNYJgH63IvwuY0sgTIWVPhg5UkMG-oga--yci6YFEhBZcFStURWxsCtwHpDM1ZolGgW86HKOOzXcdlH0ewEe-rt8V0hbtyYPNsh8QrQOYhxy8pQV36hocTcnszqy6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
🟡
طبق شنیده‌ های رسانه پرشیانا؛ یاسین جرجانی مدافع‌میانی22ساله‌سابق آلومینیوم اراک که فصل‌درخشانی دراین‌تیم داشت با نساجی مازندران و سپاهان اصفهان مذاکراتی داشته و بزودی راهی یکی از این دو تیم خواهد شد. شانس نساجی بیشتره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/persiana_Soccer/27365" target="_blank">📅 00:18 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27364">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VhiIFW-scrXNUTZVpNYs3OU7vCdRX3k9TztDvFJDv6vdahmUF_dxx2tGiwnExBiNQA1Nk8SVzJa-uPgD5FhSZzMqNZR9wculDNTTXQec2CS1-htMfFRU4KOBHCtGqad4mp1HbZpMitjfe_aUXzb26Q5ar9Y_EaugQ2NDTC0pOkdt_ne6gS_SxJ7TM-Ge9jsnKS4lFRmCG8XoDdnN5CFGSmg09MOMBSpYeIPWLw6j9FFJPYOuCIFegxIDKjHFyZ8c6wrHKxKbqbiJL1jkeLG90apmbNw_UwVbAWz1Gd03ztXbIwha0mMmWzghgXbsO_5kOxsLsi980z1l4E-Uy8dZpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🔵
مسابقه بین دوتیم استقلال
🆚
پرسپولیس در هفته پنجم رقابت‌های لیگ برتر برگزار خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.8K · <a href="https://t.me/persiana_Soccer/27364" target="_blank">📅 00:13 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27363">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ap6rONI6qB2E1DorMampU_2EpJ0Lo6xNkmCBjJa-SRX9HagD_Iu50x8xUnNBIAn89JFuBfmJ1dk9sZF5ADAAUhS9Ue7-VPi2ujcWRsvrGEpwrrDuyMkoGg0s_aIBJ-3uIEAXZJLg2F1k8DT0QFXsBnwpTTS6_Jbi3RMPovjB2ncUUYK3FLTmqIre1r7KGjSt3SD8_G6mPmkhkOeWRus_PtA3bXJgHGmFxydg7zIk3S63W7khnMyXEpMKDC88i9CNqnIuzOLKELrwFansw6obnJhzZWPMaxuxn3JRkNkRbjP509XP8f2T5i_YM8RCb4koR0YNldk_qAcjYGBfyTVtPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
خورخه‌فقط پدرمسی‌نبود؛ ایجنت، مشاور، رهبر خانواده و... هم بود. موقعی‌که مسی تو رده‌های پایه "نیوولز اولد بویز" بازی می‌کرد، دکترها متوجه شدن این بچه مشکل هورمونی داره و باید درمان بشه. خورخه‌که‌از پس هزینه‌هاش برنمیومد، این هزینه رو از نیوولز و ریور پلاته…</div>
<div class="tg-footer">👁️ 56.7K · <a href="https://t.me/persiana_Soccer/27363" target="_blank">📅 23:47 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27362">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f50f562360.mp4?token=EcD5FHmnB6uO9g7PEPP08DTRuGAOmnKeu3KhbeqWvZ4BIaeh2wb1T-ozp5WcjiYCll1MncTH-k-enpa4U_FeC5BbfnKnO8zKnLtEOqPWwmAZlR-MVdhhASdIgaOH_xZ9mdwrMzh5NDtbzbvQaBpOq_7ItHVvPQ_NdFsFmxcrCbL_2IpPLuihl25v2FI4wY2yhWTb1VBQ819XiU6zWU6aD9YlKGzSDySKcQyBXZVEx8MsHWCpeCYbMhCtKp3GVKPGIJ5kLtpAU8nYNGIq_r6RD9uCrRWG8EvcPl_0JU8aZB_Pa9HeegLvHuFmOYvRJTdBc3TsSWniX0XWZu49ARUiXQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f50f562360.mp4?token=EcD5FHmnB6uO9g7PEPP08DTRuGAOmnKeu3KhbeqWvZ4BIaeh2wb1T-ozp5WcjiYCll1MncTH-k-enpa4U_FeC5BbfnKnO8zKnLtEOqPWwmAZlR-MVdhhASdIgaOH_xZ9mdwrMzh5NDtbzbvQaBpOq_7ItHVvPQ_NdFsFmxcrCbL_2IpPLuihl25v2FI4wY2yhWTb1VBQ819XiU6zWU6aD9YlKGzSDySKcQyBXZVEx8MsHWCpeCYbMhCtKp3GVKPGIJ5kLtpAU8nYNGIq_r6RD9uCrRWG8EvcPl_0JU8aZB_Pa9HeegLvHuFmOYvRJTdBc3TsSWniX0XWZu49ARUiXQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🗓
هایلایتی کوتاه و خاطره انگیز از عملکرد خییره کننده الکسیس‌سانچزستاره‌شیلیایی در دوران حضور در آرسنال؛ یکی از بهترین وینگر های تاریخ و یکی از دست‌کم گرفته شده‌ترین بازیکن‌تاریخ فوتبال جهان.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.4K · <a href="https://t.me/persiana_Soccer/27362" target="_blank">📅 23:40 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27361">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rOgazvf0QhUJqsSTjtmQwr1PXogn-Vjpkc1sTb6oTCd7aQkbwxhBCkUHCHcPaqeV54Zjhm6ffuE_74GEOY30tOdA_fltv87lWw2h6fEfpiKSiuHvuAJGo-2xKvkVH7o8iY1YlX6wQmuQV9bK1csPrG43hlsJH7cF5k-AY8sbFnUsyXghQ7YHqtUU24Zb1p5ePXjWOSwLD4bq3FIho0m-4rJGtaqfhvEzYWdBZnBWJjKWEWkGcUcbjsEui6oOsLMyFkLEoBiRE2Zw7dwbvZFmjiQXOrUoiTTpMDKHDrEWoN6mQYdleoeHM_HceoFcBDbrve8peIJed8HlSf8ltDVGCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
رسانه «عراق اکسترا» مدعی شده انتقال مرتضی پورعلی‌ گنجی، مدافع‌ ایرانی‌به‌باشگاه الطلبه عراق در آستانه منتفی‌شدن‌قرارگرفته است. این رسانه نوشت: دلیل اصلی این اتفاق مخالفت شدید خانواده مرتضی پورعلی‌ گنجی با اقامت و زندگی در عراق است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.3K · <a href="https://t.me/persiana_Soccer/27361" target="_blank">📅 23:32 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27359">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jg-inFxZ_zcXO3KzaXDtTebP9s028tzfmPJi1MFmJJWCaWfAYr9YmIY4ffv8SthJx_ziY64F83Rv8dlMRNuoAMJ2kBP-4HWgHDoIyPf2eNHP8TUnhxSFXA6XfeI4ciP34_sptVm3jj-QTkAHVVtluSiLCzPrTO7WzlmZCdkSKyGV3WxRuSlT6K483oOkBxaZQ8MbivSqPWJtczS3mxeswsrDKYufTnfC9kuRkNjkrE1bCQo_dQkG2OZdftfL0u2FCLh2uKm45zCJO8qDG70tuQlzAWCb_y2ejWmeeM4qsBXiBXk_Wg5_U4YxINbi3ZwPAvakeAgmNtQR6WsiYOE0KQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛ مهدی تارتار امشب‌باردیگر به پیمان حدادی اعلام کرده اولویت اصلی او برای پست دفاع میانی دانیال ایریه. باشگاه‌نساجی هم اعلام‌کردیم که منتظر است‌که‌باشگاه پرسپولیس 120 میلیارد تومان بابت رضایت‌نامه‌دانیال‌ایری پرداخت‌کند تا این انتقال نهایی شود. فردا…</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/persiana_Soccer/27359" target="_blank">📅 23:13 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27358">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EgRHoQFxQNqc8Pgzzwf0GjzkPuiLbC098yleLDUN07apMXAbLqOs4VfDINtUK7UJWJdY9A_4hN6rlkw09M6oRrJ6qvpxbJqgz2xvuaRzzSFJMVjV9Z7V1UFWlmfBxNo3CZ_sdF3X1dyr-fcZMkNAqPInUZT0DG7335i9KOLgAM0GDaByPhAcIDaVu0WB9ZV4O0PN3tIvVPxe1ZOaI3FK4gj7XXnt-HGoTS9X71sZYjhrnAm_4wJEfvokHbpFECRffV4Q7qKmMWtYTVDVA5RCuU_ZZwSM3lE2e1u8UInTNJdz4CUFDIu8eaJ-gA0xaYGsyE1whcxFfZZ9weCtIxAibg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🔵
🇪🇸
#تکمیلی؛ پیغام فران تورس به باشگاه بارسلونا: دنبال‌جانشین باشید. من با PSG به توافق رسیدم و فصل آینده در این باشگاه خواهم بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.6K · <a href="https://t.me/persiana_Soccer/27358" target="_blank">📅 22:46 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27357">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PN_C5D_-cB0dU_qpKYhwig5a8fVK-VaQQIazYxw7KUHZzrl7L2DPASB0seskHT7do-QDh1t42s2URTWtQtEh0vkVqRssySsCWBtttU6o8UrL-UuX-Atkzhu_b9Ny_C7Vx-QW4tupQrI7TEW9nSoaBIvyyTgyxOVrakFdNBMk0Sam5coMoGM-S67rfIOd6goX6vh48srxr_DhkYz3HIpriZLjssxYf7aZiD3uPO2_WRva9c4dvys4PZlVDWGPQQ6tWsinin-mA-1wwkG3JKgn0BWiVHIsogvdsNKznMn5o7rJBX5lPhP5fTypKCximPPHSoLGPrR8HYaa9jrYKhQnQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتیجه دو دیدار دوستانه امشب؛
توفف شیاطین سرخ مقابل شاگردان‌لوئیزانریکه و برتری رئال مادرید در شب گلزنی ستاره جوان و تازه وارد کهکشانی‌ها.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.9K · <a href="https://t.me/persiana_Soccer/27357" target="_blank">📅 22:32 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27355">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cDs3KWFFNg8sbDXX1YUqg7cdlG8drVhort7bqdJYZrLlfwwUcXji2h8oPeyP76rkV45mpRwBmK-_zJNnF3k7mxqvtoPYOY_xkNTXoFbMY1Q-IC0bHNYoAEaSImc57j8vdWnus-sv1XAmI5SWSqaIe288lPwW8J0z9vRHzRstyyKGGRWA1d0OYQP8y-5AJp_qKffVOuemJW_ObkJu-r5NyM32TF8LIHHur5wiMjtyYOaiULu-HxEgUKBCQBiW72dEFnZM3956SewXKg_os9riEL_SMvOKW6UStpQ68zuWa1-_rX26monn7U3NXrA2-1vcpelisUCbkNQoEDCIxgX9_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Yme9hAfcvD6AErKe0cmIECjSwC4SEJLZQfaCKsRQda2j6r_1S4Z1faNnX2KK524zry_IO_UZby-1pmud7qfoihbscBaaqO8gNivfM_NC-KasHnHXuo2ha_ak_OTGF_-3igYz-0fzKYSiZcL-y6VbFGZBy3q36Q8HeYYJs6xLfUEDtvipNDo--AOJpmM9GVAkd6Qce1-byO-nUCES2MuNNR8-LhNoW4RYrbx0DRg-AtGNgP-X0uDXXGVeCREs6poHmJVVDmazgwkiSm0T2flYtqk-cr98Jrzp2mgBmg2hq_ClvxswjBloDu8cj5xuhIHQh0_-DJWITMs1YKbz9pE-kQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇹🇷
دو ویدیو زیبا از فوق ستاره‌های تیم ملی والیبال بانوان ترکیه با کاپیتانی و رهبری زهرا گونش که اخیر قهرمان لیگ ملت‌ها هم شدند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/persiana_Soccer/27355" target="_blank">📅 22:21 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27354">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bTBvQdyp2iqPvq6Do912eIlygcOP11jwwIocWqFXRIQqAG5stW78GujLPV4kYVfPLKLzDh0ImFJNt04H1OO-8Gc-OrR94qf0C28NSzyMA6eWWKMjyDF5PxspD1cLZPL9g4U0zEu9Ss2-Ti6qvnllcq5VjKIDyXwumzTNLoFTNonL-dTKAMA7sjfVxyXZne2AZIFbjMNMbcoFuKXKp837KDP-gqSOojum1Xm3GZngprseUDLEgZXA0-WDNoAAMrSLQO8jNPsFGJmAXXXzkYh6VYY1mdKSZlutr0S5IxM0r0QoQ-tGtXsZKdyDkhKuZjahNoHZSl5jTb_bWfFSH33OSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
🔵
بعدِ توافق با مدیریت برای تمدید قراردادش؛ جلال‌ الدین‌ ماشاریپوف‌ از امروز به تمرینات‌ آبی‌‌ها اضافه شد. ماشاریپوف به باشگاه گفته تا تکلیف رضاییان مشخص نشود شماره 10 نمیپوشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.4K · <a href="https://t.me/persiana_Soccer/27354" target="_blank">📅 21:49 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27353">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/24f51b1028.mp4?token=V3SqbWeOJJuOilzjHQ8NAyQOLMVAtpfZDzRCOBTyRLmGrW4hU0tP9a1HoJ1rylBx5920-anY3KOTuELrPxYQfywLv6d6sDaplZ5ZRNyshksNq5UnkfWrDBjOa-D7TM4JVsfnBnkM3f4Vwl__P8p03mcEYqhMQaToGges1kQvn-bFccHCf5zJI3PZ-GUCmUIsNRzcT6-wXRfXuuCDagLYPj60qIUfeWuNlMv7N2I1FGlff1dhqbrbMpTlnWBD09NSeKajTbC-W0ybVSqoJi_ZQl-E1AkaAvvJQaB2Zp9cMRgqJj4TS7u1Gvi917ZbA_ouVWi6gfwCp4mA3mGVx31YkQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/24f51b1028.mp4?token=V3SqbWeOJJuOilzjHQ8NAyQOLMVAtpfZDzRCOBTyRLmGrW4hU0tP9a1HoJ1rylBx5920-anY3KOTuELrPxYQfywLv6d6sDaplZ5ZRNyshksNq5UnkfWrDBjOa-D7TM4JVsfnBnkM3f4Vwl__P8p03mcEYqhMQaToGges1kQvn-bFccHCf5zJI3PZ-GUCmUIsNRzcT6-wXRfXuuCDagLYPj60qIUfeWuNlMv7N2I1FGlff1dhqbrbMpTlnWBD09NSeKajTbC-W0ybVSqoJi_ZQl-E1AkaAvvJQaB2Zp9cMRgqJj4TS7u1Gvi917ZbA_ouVWi6gfwCp4mA3mGVx31YkQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
گلزنی دنیس درگاهی دربازی‌امشب استاندارد لیژ مقابل  سرکل‌بروخه درسوپرلیگ بلژیک؛ قلعه نویی تو جام جهانی 2026 میخ کوبش کرده بود رو نیمکت!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.9K · <a href="https://t.me/persiana_Soccer/27353" target="_blank">📅 21:24 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27352">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dvGmGlj5NsF1FXTApei_f90EQBJRAYkkAI6NoxQuwHJH4G50nhNRh_e_xlAYaRn7rmxkByfO8-oY_ONoWUpUDwF8j74nAkPLwgqC2s4gv6qS_QIJ17ef-dWYQmDFmjM1n5U771_EeJ65A6lhTef7bPWeeQfIBg5-4rewdWiH3RyBXMCOh_MtSz2St1AP0qqlPrZhWTQ8IRtIbXJfU8dkHmTt8fA0oJvQYFZMeuYmjEbiA0epi5sLdDXfIvu27fB_vaahywT7whKJQklXB8JKw0oCDwdB7QjL-oomX5mfm1vhVJOcGIiGYgL37mkF2-QrgdliOhhvbJAvYWnp8o3oQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
تراکتوری‌ها با پیروزی 2 بر 1 مقابل شمس آذر در دیداری دوستانه به استقبال لیگ برتر رفتند. شاگردان ربیعی در هفته اول به مصاف پیکان خواهند رفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.1K · <a href="https://t.me/persiana_Soccer/27352" target="_blank">📅 21:20 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27351">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AyVSLbt8xy6rzaZAYhvB3N6qjru6rvyycQ74wlNTvG-irw795snrcUSpIvgx3EBhBMdg1foB2pgZLACTKngPBJvjPANU2_zfND_m1JQseV2QdUOMpJiBDfL-Vg6GG38lMhH1btNnKRr8d6o4gaGioMoP4w8BjGH83uGKQtYw5EKcjexGrGacPdLVMxgydjNd4OFJVSh3BKSvlAZn4uNPZzg9rR-VFcnqopjMyAVueDPkPxdhVuYyYYp8Cv8sxWkkRDJyth8zojTxhK6Zj_Xue_7mA1vqxN1c29S6RKUaNR0cWnjme3wpBbhxoJaxeBBe4d-_ro5hRYOEtOkDD38tkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
بعد از جذب کوروش اژدهاکش؛ امیرحسین طاهری مدافع‌ میانی22ساله فصل قبل نیرو زمینی که عملکرد درخشانی داشت در لیگ یک برای قراردادی 4 ساله بامدیریت تیم پرسپولیس به توافق نهایی رسید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.3K · <a href="https://t.me/persiana_Soccer/27351" target="_blank">📅 21:15 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27350">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/24945e30c7.mp4?token=pJ6NhD5__HOlq5ksTIpoj7Hlv6GfCEmFRs1v2ww6R70cvvcPd4yFTpTJfzhHy77D0HPtBKVHspvrMEhCJ5f833TRqiF8UwfeJ9UA0njbwEhKVYwLElEg4_HlsmXVtjZBOOpfUud5eUIlWICKqOn-8_Dm4MkK3CyG0q0mhkvZehprzWaX1aL8qHPBZd3oUYlhuUueYXSYzwl6Rxkg3xEn0Ui3KZad2zHTzikMS71A3E5kNY1wydaL_125cbuqvXQUOsJN5BXAKIW0CRijCfE094M07o7NZdZH0zdlq713M9tsm8frWxGMQN_jLHbU5Gm-8FU4PIDJNBueYuO2_44KKA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/24945e30c7.mp4?token=pJ6NhD5__HOlq5ksTIpoj7Hlv6GfCEmFRs1v2ww6R70cvvcPd4yFTpTJfzhHy77D0HPtBKVHspvrMEhCJ5f833TRqiF8UwfeJ9UA0njbwEhKVYwLElEg4_HlsmXVtjZBOOpfUud5eUIlWICKqOn-8_Dm4MkK3CyG0q0mhkvZehprzWaX1aL8qHPBZd3oUYlhuUueYXSYzwl6Rxkg3xEn0Ui3KZad2zHTzikMS71A3E5kNY1wydaL_125cbuqvXQUOsJN5BXAKIW0CRijCfE094M07o7NZdZH0zdlq713M9tsm8frWxGMQN_jLHbU5Gm-8FU4PIDJNBueYuO2_44KKA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📱
🇪🇸
🇦🇷
ویدیویی‌زیبا که فن پیج‌های باشگاه رئال مادرید به مناسبت فوت پدر لیونل مسی ساخته‌اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.9K · <a href="https://t.me/persiana_Soccer/27350" target="_blank">📅 21:10 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27349">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cbe423c6dd.mp4?token=pPlNQX-h71p2oZoIuELX1XQnRKT67H-o-wohF0Y5jNVGBLGvtDD96fejQ2oZ2AFbmvgBQ8ubVEcLoSev6i61NRT7UzLhGUAFR7Ni7sfzTkhGaYRhYV6RjaipvVzrzKeAlx1-6a6A3b9HzVooxfMk2qdaUOOjbEwqz3JS7NY6_LCbyk2ytGdFQCTtye_x-bmRw2f6CId7b6XfgYjIG250Edq_whIT19UxEZ187zS7mbt8Rw9-L3UcEwDjaVRXSHiWHXWSE7pRyByjrjRomdapRE89vkniviQelVu7O22x_zwz_cz-IXCyKKvnm0Bp0CADzpT9UEf3SVCvGwloXi2aFw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cbe423c6dd.mp4?token=pPlNQX-h71p2oZoIuELX1XQnRKT67H-o-wohF0Y5jNVGBLGvtDD96fejQ2oZ2AFbmvgBQ8ubVEcLoSev6i61NRT7UzLhGUAFR7Ni7sfzTkhGaYRhYV6RjaipvVzrzKeAlx1-6a6A3b9HzVooxfMk2qdaUOOjbEwqz3JS7NY6_LCbyk2ytGdFQCTtye_x-bmRw2f6CId7b6XfgYjIG250Edq_whIT19UxEZ187zS7mbt8Rw9-L3UcEwDjaVRXSHiWHXWSE7pRyByjrjRomdapRE89vkniviQelVu7O22x_zwz_cz-IXCyKKvnm0Bp0CADzpT9UEf3SVCvGwloXi2aFw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
واکنس ابوطالب به صحبت‌های اخیر مجری‌ های صداوسیما درباره آناهیتا درگاهی عمه دنیس اکرت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/persiana_Soccer/27349" target="_blank">📅 21:01 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27348">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bq6QzTIzLGTifDQWMg8awFVJyPHGCKTF125I2eNY9id9ajak6a9u74He-zJcYHWcl74U2QPz58gcFzoi9Tkf9JKJkqBPxXLmiNWIPIAAzQWgdnZy9qoiY0MsmAY7o_mDlfl0xao2x7ZJMLGX6J7lfE8em54tvis1VPs9CDbEexMv_dvf83gjmgae5V_G53rp3VTGTDMZj8NWMrNkfCaQKOfrbD1lgcmL-WXRxX71oJwYTTymVU2IsSRaJJAxgpNLpNAucqLIhe3Mh4Vxia2Itfir_973QmC7gCVQzHPJvzxsN827fX8dcP74c7GrB6A7WkevbSw0GySNUndmGhz-lg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
با اعلام باشگاه الطلبه؛ مرتضی پورعلی گنجی مدافع 34 ساله‌سابق‌پرسپولیس با عقدقراردادی یک ساله به این باشگاه پیوست و شاگرد علیمنصور شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.8K · <a href="https://t.me/persiana_Soccer/27348" target="_blank">📅 20:49 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27347">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C7Sic5D_BL9ZCZSwpID-_lJJpYeARYduoSL4rM8ZorWrFGaKhg22nNSaa0x1q2EfKln-i-pWG1-V8w4OT93xPKHSDf5NoERZY_TO_Jjt0vkKr0GIoZmaeNcvlJqH6FEDAmT1z0cA6u24kpIo8w-Ap7OPV8lPKp4EEge0Sn6DX_r2y7-r-aTXFpX7hVQqs5FHvht9mlJ6oIKfbi3szo6C1-fSuDFJUO6Rj4jbPQ9wGhRp48AAKXV6YLnmxSFLLNKMzL7uG16qZblUGCHSQ0P6j4_doJymhTtzDGq55Od1FgfLW7UkC2lGcLwxqbyLgMDh57HeXRWNbLgON-_zTZtlHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ باشگاه‌پرسپولیس برای‌ جذب کوروش اژدهاکش مهاجم 18 ساله آلومینیوم اراک 150 هزار دلار بابت رضایت نامه او پرداخت کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.1K · <a href="https://t.me/persiana_Soccer/27347" target="_blank">📅 20:22 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27346">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E8cuZ4bTB85IGiT3pKYrFxKcAy-uy5G6FJ262tpDN1ezeFYTrHkS-4YLZOrNdmDgXQ6fJnvboRxzMZWTRwZ2n_GAP2sYs3mp_Ndb8JvYguL_Lfq5j3C_3AIz4L9Sl6E2MJc3dTuyUejL54e2Mjm0bKLhnP85xxSz6gIPNy7C7OaCkVXte-XA3hXHZpPzeFB1gxjYJWoGYaWq4jevpdnlay_-IsxQhHn0i7aROyyC5_3HnH2UjqElpHqyJCE136c1emviyQJTfLn34CWbsHAtve_9GytQjzExEiGrrohp7pZaZdytqCUZl_sKTR9eZMd4qpFRd4n1IXE9nesHxHlJSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
در فاصله دوازدهم روز تا آغاز لیگ برتر؛ تراکتور امروز در دیداری‌دوستانه بمصاف مسی‌های شهر بابک رفت و به زحمت دو بر یک این تیم تازه لیگ برتری رو شکست داد. شهریار مغانلو و هادی حبیبی نژاد دو گل پر شور هارو به ثمر رسوندند. هیچ تیمی در این فصل بردنش راحت نیست…</div>
<div class="tg-footer">👁️ 59.6K · <a href="https://t.me/persiana_Soccer/27346" target="_blank">📅 20:11 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27345">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s_n7pl1LHkV5XB3QWs5Ly9gDyOkDN_T0m07spdiY_RYbg2wJ0DVeW--8zz6dnqPw3oBRWWipf-BDMQTLZGOXk_QLFoQOfyxslyrhZRTHpJrO91iirDjFw5__xFtPH9-PR2oDjVQPjVzW8lrXICF4IXtHZfCM-VI_apDK8pdfWt1Q2DXrm4EA9quNzihvX02pgkJZFJihBVkDfYjbP-I7lQCub0WIRVRiTCGGoPX51GBvbOArNAXTzIb1FUzlFdJL8SnZ8ILo5JTvd9HseRcS2Lp_Nh1wCRo8qj6wkZEHOJpzTuXvY1kfzBw1eiJ4_5UW14PScwreq9JVP05aU2-j6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">◼️
#تکمیلی؛ خورخه مسی پدر لئو مسی که همچین اسطوره‌ای رو بزرگ کرد مدت‌زیادی‌بود که با بیماری دست و پنجه نرم میکرد و دربیمارستان بستری بود. دلیل اشک‌های لئو بعد از گلزنی به الجزایر تو اولین بازی آرژانتین در جام جهانیم همین بود. در نهایت، خورخه صبح امروز تو یه…</div>
<div class="tg-footer">👁️ 59.6K · <a href="https://t.me/persiana_Soccer/27345" target="_blank">📅 20:03 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27344">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OI5_psRbP-ZwLqRbAK-j1f1IrU84aclsaWbsTbynJDCgM4VeDTcaAlyIgQfzGY6bMLpVkqo94FYCrLa_8hKO_yh9T6jxPi3tREyYosPodkJ2kIeMdQluxXq7_daZuAXnsdWPzRwjVPdqMREfcvRNG-y1TTrJBjezvkrgzXGB2jZx-J7C-yHvu_V_RH1psrPUFrLeIZwN6v18hRz6kWnotuiwHX4WtdyP_OlfhhbfCh3NkkKXZuei1D36pLoTZzrsCGIWRTx5ivyJunBWtM04vyu2f4xiwugfFgT6olqkOZ5TH4zUyz9A55A7a-ms1aqPWTnek6NxVIUCa9oi8o6_sQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟢
👤
رضاشکاری مهاجم‌سابق‌سپاهان و پرسپولیس برای‌ عقد قراردادی یک‌ساله با باشگاه پیکان به توافق رسیده و به احتمال فراوان راهی این‌تیم خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.9K · <a href="https://t.me/persiana_Soccer/27344" target="_blank">📅 19:42 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27343">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vw4KRKUSkl70YCE9fKMNChRZIeJJhRzXVxGMhHgzWncPzAXda9ZltwYiI_AXAvSInO9RMdE0kKPaBCqOf5ci8J0KlD6n2KMIXz7DkkkuiD6FKRNlumWmEmzPErWttQrFrVu3sC_8L1FdnOYTSXxPjaxdgoFDR3quQ2wCgLKO-eg4ps0-AbMjG8LQCYKdxyqsvnWkmqwc-YSJkwNIGk22LQZqTt-EzOJ2tDKSdq1dHupmNOnVT7NUwQuu8PuDE08bRNtBkeSKXFG4hP7ZBHd6RTkDIemz8WF_5R_g6fZLQ9OsnK70F_vSaqOw7KNkXSFU0OT8v6xdQgRnUuyRwbfHlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
طبق اخبار دریافتی پرشیانا؛ محمد جواد حسین نژاد ستاره 22 ساله ماخاچ قلعه علاوه بر آفر از سوی سرخابی‌های پایتخت؛ از دو لیگ پرتغال و لهستان نیز آفررسمی دریافت‌کرده. یکی‌ازشروط مهم حسین نژاد برای پاسخ‌دادن به آفرباشگاه‌های‌خارجی اینه که رقم رضایت نامه او بیشتر…</div>
<div class="tg-footer">👁️ 59.6K · <a href="https://t.me/persiana_Soccer/27343" target="_blank">📅 19:27 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27342">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YeRwm6z26V0ejg5BBXSQw3ND54LUUh2J7K8RwuQd5Eh1-PAAVSQpvR8RA8_3RfprAWby9SSlHXAX5MYA3W1taJDHyg7ikR4HtwEs3P4EFL_YCOuGUGK9PKnfg6j80WnpgP9jYd6LUa9RsdqNhk0EB977kyASNqshO_GlxeVbPfQADnUkidi_kQdLqgJ5N_Z1yA_7MugFLwYcWXTbWs3Mg3mAbzW_e1_gIUAIP8E8_Ng0u9qNtjaZH7xLM3sAlGJqXoxt-L6UZuBmZ26jINJmqpP4PIQkP-8h4vBy2N6mHe5T7xsKsyBv5Qk4BUiYU0JRC3KVPklkhIqPJa0OGG4lgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بااعلام‌سازمان‌لیگ؛ دوتیم استقلال و پرسپولیس فصل جدید رو هم در قلعه حسن خان شروع خواهند کرد و فعلا تا هفته ششم هیچ خبری از آزادی نیست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.3K · <a href="https://t.me/persiana_Soccer/27342" target="_blank">📅 19:07 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27341">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sWJTDNzfRbDTbhbHug7zuI-J2aydDsibL0bInuJZCpJPVvUaxDQXB4MDCDUHeR3Rb-1aFzXTnDLtql1jikXBYnwAwShY55MJPsN1wveP14SEBmeW3b0L_UqMcwalTAEy-ukSiwprg3BbMGXJikp2YpSyLW0eHwkYHj_TckkbAnC1-RqNrOUwxFnUUEJ9M6zwJdri1113iM8nMiGfTnkog1Ohl-WJlKKzAEgqNEZ9aWjJj_86OUtJpAyRYVg4W75A2mTzMS9DROnx59W_V3oGVcfnOYVyj3KhMZ-g7yjvga6spvhNB31GMSHmq9aCyhQbkziw8PEzZdpUvT3ZCxEgBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇦🇷
باشگاه رئال مادرید دربیانیه‌ای درگذشت پدر لیونل مسی فوق ستاره آرژانتینی رو تسلیت گفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.6K · <a href="https://t.me/persiana_Soccer/27341" target="_blank">📅 19:03 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27340">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tZcbGf4E9UB1PDPr1QoYUbjwO3KlNcMejCqKK3S4gYw1hsV-JMLCMITbi48UFRXzot0PmKO8i1PQDTY_iosgB-sD_z1W7tXkljeVgZdgrNh3DDv4OKAyJh6oklqaNDuILfx0ft2_nCs94Ocboisg5DnySxog5SenM9HlHQkdz1mf8V92NTFwjog9BDaqZdT0DAG68aVvU7lwX38eEu4XeHLD2Elwp8pdeUmUIRbCCcF13RssetHMdTzJyqbwt_vCuzfgMzKhdkmhsm2KnWu0dafACG2QeqOEQXbHQ7mejaSrMxqPpNMKp3k_Y4UstBLIf3rcjS56Pjzpw0ZYN2TmFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">◼️
#تکمیلی؛ خورخه مسی پدر لئو مسی که همچین اسطوره‌ای رو بزرگ کرد مدت‌زیادی‌بود که با بیماری دست و پنجه نرم میکرد و دربیمارستان بستری بود. دلیل اشک‌های لئو بعد از گلزنی به الجزایر تو اولین بازی آرژانتین در جام جهانیم همین بود. در نهایت، خورخه صبح امروز تو یه…</div>
<div class="tg-footer">👁️ 56.8K · <a href="https://t.me/persiana_Soccer/27340" target="_blank">📅 18:54 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27338">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SXpB7giuULmrB3yWLat1NBU28CYIfAKSWB6GJ6OdyUpEHyJxLCsZ1Q3RagvAc-IvCE2G_95_QmBtd11pEhSrzGmV9SxNFJeowavK_Li5YV5caynFst-WQdNiO2hVVvmSl9Cal_XSx8SxWdry7yJuQaGTEq24IrI6pmavR3tWd1GzDSKzLYsymSuULzwYrnYZ4UtcArAowCe9MS0j7z2cvDihnmXPuK_MX6qmDeRVu5CVVYd--W4BiBBXVfaLQi2gw8Ylvg_sHIEoUXNgfOHUMNnyp6aVzhr4ZWpzvMy9G4aujgwKXRVGqBeuYIKc465xJegdYNEQihg7MeY3qzUl9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
وزینیا دروازه‌بان‌کیپ‌ورد درباره‌پیشنهادات متعدد باشگاهی بعداز عملکردش در جام جهانی: من میخوام جایی برم که منو واقعا برای ترکیب تیم و مسائل فنی بخوان. نه فقط برای مسائل رسانه‌ای و تبلیغاتی چون الان یه پیج دارم که 30 میلیون فالور واقعی داره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.4K · <a href="https://t.me/persiana_Soccer/27338" target="_blank">📅 18:54 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27336">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5ca7c42226.mp4?token=jmYRR1B0V05uuWIXP6-yWlxWybpJB3LdTAoBoeouyVSSkw6ZDl5oDU6o644x06mXW0RCXQc-ofZ5iUitIVklGka849sRWZ4gutZ7uEnjGRyXjqwuvzn3tH2QL1vacIaPqcK2JRkuvkwoWSNQOyhBUollIBlw934SuMLPSXVzIIW6fZ0LbhQ2MtiJaMHNZl7trOP1rIIwKNwYtE01_wWQrtld3F_U2_GkP1UtYVSWe3mQnuMKu8XtK25ES8z06yDwxDYF9XlDBJccMnmWhM13K1HBE1FgZMQWl4nUQxPXt9Z4WyLUr829RGLLVdKhanbuebjxE3aCp75Jq27hD2eQiA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5ca7c42226.mp4?token=jmYRR1B0V05uuWIXP6-yWlxWybpJB3LdTAoBoeouyVSSkw6ZDl5oDU6o644x06mXW0RCXQc-ofZ5iUitIVklGka849sRWZ4gutZ7uEnjGRyXjqwuvzn3tH2QL1vacIaPqcK2JRkuvkwoWSNQOyhBUollIBlw934SuMLPSXVzIIW6fZ0LbhQ2MtiJaMHNZl7trOP1rIIwKNwYtE01_wWQrtld3F_U2_GkP1UtYVSWe3mQnuMKu8XtK25ES8z06yDwxDYF9XlDBJccMnmWhM13K1HBE1FgZMQWl4nUQxPXt9Z4WyLUr829RGLLVdKhanbuebjxE3aCp75Jq27hD2eQiA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
مرگ درپخش‌زنده‌ی تیک‌تاک؛
یک تیک تاکر وقتی داشت لایو برگزار میکرد داخل‌مخزن آب پرید و چون فضای‌کافی‌برای‌چرخیدن‌وجود نداشت تو پخش زنده غرق شد و خیلی مفت جونش رو از دست داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59K · <a href="https://t.me/persiana_Soccer/27336" target="_blank">📅 18:37 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27335">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/twtPRKTBAuIrS_YDuLyathkxuj4aIIkmbIdMH788a2sKDgic-VUah3Oz25ymVL5lPvSiSqQ1IAOO1u5GL6wW8HieFkf_4R6M1-jd7aikad74zyvGrDrJ502wSTTDQaQbHatR8XANP_uqCfHmO8SfLLZpYE8KvTnbslX7vKHeVrnsv2x77IoCXax5Ic7BHVl6y2U4LLXsl_zoxsj9xSdMt8QfrspNk8qk_iqLqJCWF9WhIFtYY_cUVEjfzmbl-9c_dXChMptWXXxuHKgdtUrYU8Dsn4c63uYjPzvZqRTk9Q77uHxbd84Gk8zNMUh0SVmqOZiiwWaH5-qhki_BchBR-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
فدراسیون‌فوتبال آفریقای‌جنوبی در روزهای اخیر با پیتسو موسیمانه سرمربی‌سابق‌تیم استقلال در حال مذاکره است تادرصورت توافق قراردادی چهارساله تا پایان جام جهانی 2030 با این سرمربی امضا کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/persiana_Soccer/27335" target="_blank">📅 18:28 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27334">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DbjPyt5G3qnF2C0-UWSzDHPvMUTlu-Niu3nPSeLO-miQfM0SJhsR_qvisdQWQUilRFSYuRU_iR57Qa7HiQ8WkUIzBzE4cYl_Omt8QgUtkoq7PULkAQNecsp1A9HiMY30k4CM4ZYS88tKFw44b7j0x1aCViW-t9xgJYmom9uSf9SjhSOyvVqAIlUS6R5D8V1-GB9BE2imjoge-d-jRKLCsai1OxBxvdP8ymB4Yliz6XedoZXySCyufippf72WYUGUKpS3PWiWqncmoK7TrWKfyzPiXMtp_Eo_jePWNyA-D60mNGEgKLwtmbORBgfUKD4zzJggwwaoZUCdKt4dw3TEAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🔴
🇺🇾
با اعلام رومانو؛ لیورپول خیلی شیک و بی سروصدا رونالد آرائوخو مدافع 27 ساله بارسا رو باعقدقراردادی‌قرضی‌تاپایان فصل به خدمت گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.9K · <a href="https://t.me/persiana_Soccer/27334" target="_blank">📅 18:02 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27333">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E8UGRtbbsIQExB5oPI0_Ga_oCVf8f0NZm3Icg8cscws-CW3ontPhvpqm8j2iddZLjwfIbmBSFeTAdvJzZk9xlKDXR6KxK9t9dl-2U2ZMJaicUEFGgZiMsUb-6ccz9TdnkGSJ7vHck5FxVqF5cvPjPv9KV03r7WDCeAlzSIl8DmNfS2IIoHnaWH2of5Towk-m4-6SGatmZ0smpcRERXlVZjEgYUa8p7n8sDW0Ajo1vYHB2tMUQhayaTjNw2PHosTyR77lAnwyo4eQKZ9KQ9W9FFLee_2DAXXhzT6cj7IUZ6w99J2QsQ_wNS-r8cg9OkUxXtO9OfRo5GQ05VCnG4VaUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌دیدارهای‌ امروز؛ از مصاف روسونری با آبی‌ های لندن دراندونزی تاتقابل دوستانه یونایتد و PSG
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.7K · <a href="https://t.me/persiana_Soccer/27333" target="_blank">📅 17:54 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27332">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uIfWUoNBH1yQCMIp9LibNAdKjuxGmXfMu_gqgibXXt8RhJZuWKBYQqMW4K3jRtclcdcCDI7LTOZNVJQYJ1qMIBMOHNvQAXbrSB-hWjj7kvL1DDMlun2788we5VXk-_kP1qt-At-Yekln63hGAv133L6QsZr78UppxmgYxOabyQwSCJb7VWFZbNS1cA92yGCSJV7o88Z3v0wQRUScM4m10zllWlkyCQjR5Ina35Ge1h3e-OmvmM2g1vkdmm8v7PBKY6KQAlZ95YFtTR9pNoSfjArrv0ONmHnxnPrfcyKOedXB_EJYez4vQ5AcqO7H-VB6gFKWCx21QYuDctMIOediQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">◼️
#تکمیلی؛ خورخه مسی پدر لئو مسی که همچین اسطوره‌ای رو بزرگ کرد مدت‌زیادی‌بود که با بیماری دست و پنجه نرم میکرد و دربیمارستان بستری بود. دلیل اشک‌های لئو بعد از گلزنی به الجزایر تو اولین بازی آرژانتین در جام جهانیم همین بود. در نهایت، خورخه صبح امروز تو یه…</div>
<div class="tg-footer">👁️ 58.4K · <a href="https://t.me/persiana_Soccer/27332" target="_blank">📅 17:30 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27331">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m1-ZF4GE6Vu5o91UIDpoJWkhOxMmUZuXfMQMIh41lyDQE-jZhvggVqwyZfWTjTvM7UuFKs1QslnwHaxLKeHz-0PhJK-KEJOwsw83Pu9e8yItPBFLMI63na6XcXfhowV93W5s25OK5fEndfN6yzL29AOQSSzlDCT6le6W-7WnrrpLwTqAcrgJ5MLxr108390dE2DN1mbPL_5h94-D0WwPrZ5DpXEG2_Izs1IywEbiTmzzgiTBiLIHvlBPL-lsi6YkxELGgWCwl836H4GlZq-y6hAwN6j6wZY0-jwNa8Tc-nl98W6DwtuIvuMGaPrN99P-znZww21m42y3JO7jIb1aHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
دوباشگاه‌استقلال و آلومینیوم برای‌حضور قرضی شش ماهه محمد خلیفه در آلومینیوم اراک با توجه به بسته‌ بودن‌ پنجره‌ آبی‌ها به‌توافق‌ رسیدند. درصورتیکه تا روز سه‌ شنبه پیش‌رو پنجره باز نشود خلیفه تا نیم فصل راهی ایرالکو میشود. سه شنبه آخرین فرصت باشگاه استقلال…</div>
<div class="tg-footer">👁️ 58.6K · <a href="https://t.me/persiana_Soccer/27331" target="_blank">📅 17:16 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27330">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KhF-699Grv3JyijoXBjunJf_NphCXFGbTavJpPKRgyOMxLS_vUFN0NJ1vHO5UZ2Begm2snLfkNdYQtj_ePJQn8R8ynETBD74TqDsE8JMkN28Xihq6gcdVfES5izujSR6JEo29PY1-kCN17GANld9_xAOw9bDAZ_oMKd471mDSxknLpOzOT_haosmopPP6I7UU2SocT3UFZ7IYHCPwAwYxguoDIXC-O8fjiBvuDWRBfVvMT7q4mfnFw1fsvBodu7HxtOMVCMlBy1DmXz4ij3hcEri0NX3X1FqUsrOapUEAFFskPBkVIBm81lWEkPH2PGYCWiCh0C2vn5Wz8SwXz_lyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
ویدیورونمایی‌تیم‌پانایتولیکوس یونان از موسی جنپو وینگر جدید خود؛ طبق گفته رسانه‌های یونانی قرارداد جنپو دو ساله و به ارزش 800 هزار دلاره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.6K · <a href="https://t.me/persiana_Soccer/27330" target="_blank">📅 16:46 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27329">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GgOL2Iuc9501dvRa_z2cmuBf2SklB7E_v_dHGknWQRI7mLhEgl3_58qXJ4mDPmd9k7vpLDxv6CHyIj2t8sqoVgcmRNDMftOfGvblJZxECjsi_I9O1fjKPdEHbyIaFdT1KaG0lSQuWeFoJR3pirK37QCNboSaBtRIB0vyEYYApM6QGfYD4XUzard8T8KKtrejCeL8T_GGGHP8EJ6LwsJX9xxBaDv5xcifjTh27xR1OrWvQ9Q8rZA3hjXaJjdyxYBnuxFSfuxaLZNKK-CJnnISrnYBjOtDmpmfraxpqfv350cL70ADqZKxJDknej6SrWcZISV7ggg-_5gDKrzeTXL0Ow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
🔥
فقط و فقط ۱۱ روز تا شروع بهترین لیگ دنیا و رقابت‌جذاب تارتتا و سهرابیولا مونده؛ برنامه دیدارهای هفته اول رقابتای لیگ برتر خلیج فارس!
⚪️
Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.9K · <a href="https://t.me/persiana_Soccer/27329" target="_blank">📅 15:40 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27328">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LICKAVT01DG3aCk9yxj51vrSp1rsVq1NSHGWieXuzzM59Tsd6IONlqNYfZ_7wSSbY-zvsy42qiAGJhH2Z2zSZo0ozGgsutIK_V9vCNOg3Uw_2B20pP4Q5Do0EclsIqVCFCui9GJkWzmH04idP6KcLn-bdz8X7rFIgXZH2BJXr3tDKOi25k0tLntpUs8kvbwXF6QGKSwIxGCb24CnD4wYhA7NKhb4g5A0g_g5skCxLrRIPT7v-no-DRyE5BvKRWmGQGVla22-cgGyyHNWC_9h2K03pO05f45iw0rr-73JXa1ggUhz_Ezw9ZZpN4D4wy-g0bCfYFEs4vCfLPhamqTb9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
پیغام باشگاه بارسلونا به سران پاری‌سن ژرمن: فران تورس رومیخواید؟حله 55 میلیون یورو بدید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/persiana_Soccer/27328" target="_blank">📅 15:31 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27327">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YsJjbyD46bhRGS1jsvPvmQMoCyJqiP_NdceO-U0edQ5phMnMU6ZJH6NfrT4cSnyQ4iLvPic0hhcZW1oIxL5xDR793nFqcyJx7DONTv8UsocWHjqh42YdRGawqDNexxGeeoRcQK3-ConS0DIMED8YX_XHyGZNfkAmg3kls03MLv2NFiJMmXbNq_MtKI-5Pu4vGlrF3Qmb0ObA2BkvXXJ29RaU9tddlV2NGrnO9mOXYgjnRcs19bgm0SnN8Te4AG5yifr4i2b-WFm_Mu40_12FYJnqgJ8UhOd-aUndCTqzA9Ef_iULWlqYmWSbX6tseYkunMW83AhVFllWmifH90sbEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🤩
#تکمیلی؛ سران‌بارسا قصد دارند بعداز نهایی کردن‌قرارداد رودری برای‌جذب‌کریستین‌رومرو مدافع میانی 28 ساله تاتنهام و تیم‌ملی آرژانتین اقدام کنند. رومرو برای پیوستن به بارسا چراغ سبز نشون داده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.8K · <a href="https://t.me/persiana_Soccer/27327" target="_blank">📅 15:20 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27326">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B95ozO62Wx--TFWA13PYl7BqDjBZXkU8dM2JkvaEEmdJKhvmQrdTRMTy-3j1oYu0zWApejlwjle9JBmd3AXMdMNOtJRUQ4HHE3ivo-F9SGNRtu3tg-Gxux2OFciMZMF-GiiojlMBWkQY0h7aQqquC0NeEiPCGKBN7Jz3L8JtrxhETQlo4hSZIx8sF65uLVw_csEJo_gDM8qXmgXfjOX78i8TOt6q3RcewyrHrn-_ml1GKAujywp8CziFNuCkZZFTx9UqofvkDV1JY00AcuIzNNiHWMp-HHaI2C07SBbNvWPsezHtgXoa-pcXXHs3HaX_jCWsK7IiChxK2o4ciZ005A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔵
باشگاه‌استقلال‌اخیرابدون‌مجوزو مدرکی 80 هزار دلار دستمزد به اوزجان بیزاتی مربی ترکیه این تیم داده‌ و بیزاتی چند روز مرخصی گرفته بود و به ترکیه برگشته بود که بابت به همراه داشتن این پول بازداشت شده و باشگاه درتلاشه‌ مشکل رو حل کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.4K · <a href="https://t.me/persiana_Soccer/27326" target="_blank">📅 15:17 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27325">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hVQajxavKZYDZWkf55QiDEz5fm1ur0aYd46sVtUbd2kMCTlEe8MLg4Iq56nkGfD79bGEOgr7hlqBx-mblWEldaZixIHaJ-a198ZOd2A1DNSld1DEAexEd3F3c6ElVBt3CDgjuoax_GvW7BSDtd154sC49Knq3nARmwJI-P9kfgYVS8ZSmdhYdv4JQ3MSDjHIlXPBK42nzfjmXRK_47qFQphRiU587HvikadcUCckXzXmoG5XVrZ-D7X1IjpvzpdShkAvR3U04nZ95TbsPLihzDF4DNj9lg78pWWjgaorNtGvxzLoYgo3492yN1YvnVpZl8duZrLmyaVJfhWL8HbgmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
👤
#تکمیلی؛ هفته آینده مراسم عروسی کریس رونالدوعه که اتفاقا لیونل مسی هم دعوت شده بود. حالا با توجه به این ضایعه بسیار تلخ باید ببینیم لئو مسی دراین مراسم حاضرمیشود یاخیر. البته ممکنه که کریس رونالدو مراسم عروسی رو عقب بندازه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.5K · <a href="https://t.me/persiana_Soccer/27325" target="_blank">📅 14:45 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27323">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/U6yjVBwDas9Yl5s8c-tgCMyilHVqB64dgEUSWVvPiugGPolVuk2A-oLJV0GgCAwdoR3YWSnEiD5oaKPkXrSRuWLqgmjxYyezDpQeJHgefdnJwZjGeNsCREJU_BvKvolLK370e_1tpLOSq_BhsPvRtZu_MVTQ7ab1HExM6KZm_hhRTIV4DUhMfCxoxduuh5YoKv0pOxv2Dr8mzoxKQFOQEdiy00PURyYROuRJXS0wZIyJJMAzQ6qIKascmhTSxz9sfVs9ZkYhf0gQP-I45rn3zj-iu4teuP2ivH_EbD3I_JyfLkvWy4C0Ya4Dz200e68Hs7-ezfHex-Q-dwSFEfbrrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NRqhOsYA_uvYlH6eXQKCiXStBQqMSM_G0osWr9vcAOus8IZe7LoLyErc3qpWDWCilnIsnXzPUhdrANBplDqkE0coiOKxXTE5r2q7oDLh6D_aY7PMBNzCa72Y99uCVBwvrBSz5NPTbssqlklyK78gRJqfuhY1UcXkod_VV6HlGjCVlTvZlV3F246Ng1-P1zS3gP0T5aWzaF7aS0xsXT0oqfIXBzOKIHRFTWdvMVzHNO4GuyM4rTfX-WynWTkLanizO30hmE8rOq5tYRiCQhI_ObiFcGBhl7dJuNiAMLu2dRiV-y3P7EOAX5l74tABWe7di8YS6b1OgLPCUvKlsWpAmw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">⚫️
🔴
🇧🇷
رومانو هم تایید کرد؛ باشگاه آرسنال 75 میلیون پوند به باشگاه‌نیوکاسل پرداخت کرد و برونو گیمارش ستاره برزیلی کلاغ ها رو به خدمت گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.8K · <a href="https://t.me/persiana_Soccer/27323" target="_blank">📅 14:35 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27322">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qI9ENzlPE2OvLBoM42FDEhgmcKF_GFHLHbm8I5D0pNDCLCYg5OrlPZtR6UZ8JrfmovNX7EItigj9LTcOaF7msdp7AUw2gd40b3EpmRw0eA-fJMH29x0KGh7F50PqBfm7Uehyj-smKQ0TjVBLAALs0kSVEFRgJpepoDzAyGkWXgRMggNBbGkQN9vl2y0jlhQqt4oDkJP6L72WJIloP_H1hvbQN0848F8pP3VdfIFIbf5xFAyfhburkZq2Y3LnAq0-EK92Owvlm2xILYDOCJJbUdkxg6fNWNTIUDq4JCZFCANXBtEidtBJs1BcXg0FIPGCPjv-WnzMrs5cMEkU_dDJtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
پدر لئو مسی فوق ستاره آرژانتینی فوتبال جهان ساعتی پیش در بیمارستانی در آرژانتین درگذشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/persiana_Soccer/27322" target="_blank">📅 14:28 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27321">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gX_0WqaLeeC1wZvt462Qg5PacMsEjoRI1t6K1UVCGFsdCvtC1EkENjSCFcFRNTkIh7hb9h7wKqplDsDnXUAOhmwm-zqh79UB9LWPMlcmXwb82cBnXazP2qGhoFASzgNHeOl_tOao1xQCqLO8oRMWwA8UQAbp9sP0oP1OdEA7bYlI7z7liiLHMzbNSyT_I4uafPoqRy9Yr8QAgYXWyP-O9SHvOlrJ4xW0s0fLcGBTzszIDL9xBZGV07zz6BeWMU98_W68prNM1kxla5LaVeZ2bfI9a0Gkhr4SyKYZtyfTxVyvBvbNsufPgCs1mlS7dE7fL0BEUiKaN0lvqr3oGMoeSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
پدر لئو مسی فوق ستاره آرژانتینی فوتبال جهان ساعتی پیش در بیمارستانی در آرژانتین درگذشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.7K · <a href="https://t.me/persiana_Soccer/27321" target="_blank">📅 14:22 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27320">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/euzZT1mSvXBd5WUdy_NJZ_z4vP5kcQwd84jUblF7O5Yg4AUMoNfcJGNcAM6jvn-a2RmNLS8y2AfZSjoUQunV1nlQp0XI315E_lAVFeQvGPyR_FVkpj47glPZgkdMzEB2NNOB8GkGI0e6Rr2tdJTxLc4elWO8sOiNvBTaHObwk8jeDcbuVfAuTwkUmzy7qTqNwnX-adJtINrDlBO4yPpLyqw71inyurAB6aYaRGNKYdepSE7nhS2jrED4YwGGYJHkD20etiUlPmjzbhQNiecrmcY4x2k3XXBTyfDktN-16IR-M5iHUSVYrrA9eJCnuXC2Y0bYbjoGRYaou9-mJYW7sQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
#تکمیلی؛ بزودی فابریزیو رومانو خبر پیوستن قطعی رودری به‌بارسلونا رومنتشر خواهد کرد. تمام توافقات شخصی صورت گرفته و توافقات بین دو باشگاه نیز در مراحل پایانی خود قرار داره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61K · <a href="https://t.me/persiana_Soccer/27320" target="_blank">📅 13:50 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27319">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0fa190d851.mp4?token=Fajo63S97JBS7aICF7I5DvK9ik8lF3rBk-mH6NorEczMuN80czHQMddwSy5lxe5QsJ814FlYcJgxOUbW-7mtFYz13cbQ8lUUO8GNPJDCnwDycpUborr2j3xYi5Nrj6Wp1cuK5Y5X2a623Fco91KlqjnfEKW6Mbdo1TORTKcQxkcX8w1NNT3GDuykNWw1zTYsBSHPtL6vvGp0ZH2Gur8vO-m0ZxDJ2c0Qq5mkwdIUR7SjVhKfXmGTOiZzFajHr7he4tIMsXgvTLHEdkydtFSu63EBsrlVcsc1piNid0R5EaqditLT2vqt4vW1gDnm32lb_UZ6JVAh7SGgCcw2gy1rOA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0fa190d851.mp4?token=Fajo63S97JBS7aICF7I5DvK9ik8lF3rBk-mH6NorEczMuN80czHQMddwSy5lxe5QsJ814FlYcJgxOUbW-7mtFYz13cbQ8lUUO8GNPJDCnwDycpUborr2j3xYi5Nrj6Wp1cuK5Y5X2a623Fco91KlqjnfEKW6Mbdo1TORTKcQxkcX8w1NNT3GDuykNWw1zTYsBSHPtL6vvGp0ZH2Gur8vO-m0ZxDJ2c0Qq5mkwdIUR7SjVhKfXmGTOiZzFajHr7he4tIMsXgvTLHEdkydtFSu63EBsrlVcsc1piNid0R5EaqditLT2vqt4vW1gDnm32lb_UZ6JVAh7SGgCcw2gy1rOA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟣
ویدیویی‌ از خداحافظی چندفوق‌ستاره از رقابت های لیگ‌جزیره؛از محمدصلاح رودری‌هم رفتنی شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.6K · <a href="https://t.me/persiana_Soccer/27319" target="_blank">📅 13:24 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27318">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rWP-E252L1ORQHGxO1AyyIW_jb62jIcfQvFng33rhFZ-F_Hak8h835UBt2RfAbj3jfd5qdnTXl-5ZWZPlQEnR7vt1-UaWYId05bbI2Lv3v_78HgG_abWimr6-3U9k8RaNeaP7DIgEvRdUE1kQaQ0oXiIfiwwvKoJDjlagd-0_lIHMBsTWt_xmZw8kSWUGR1712M9OCj345_cb-fGRZ3IZUTCLZdpzwf8xfqwbM8jtiO4f6zrt3WprlHCbS1oJMkZY9T5Mk0HPaeO7qCqWw9hMM-msvyPoyKyTFWQHbgc1l7Tfz5vq1exxMUnF4ZvlfxaRB6sW5XWmSqaVxB0hrvphw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#فوری؛ محمد جواد حسین نژاد دقایقی قبل ضمن تشکر از باشگاه پرسپولیس آفر این تیم رو ردکرد و به‌پیمان‌حدادی مدیرعامل‌سرخپوشان اعلام کرده که فعلا قصد نداره به لیگ برتر ایران برگرده!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.4K · <a href="https://t.me/persiana_Soccer/27318" target="_blank">📅 13:04 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27317">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🎙
زلاتان ابراهیموویچ: وقتی 20 سالم بود با یکی رفتم توی رابطه، الان دوتاپسر ازش‌دارم، توی این 25 سال حاضر نشدم باهاش ازدواج کنم چون میترسیدم اگه بعدا طلاق بگیریم نصف دارایی و اموالم رو ببره. بعدازحدود25 سال یه شب کلی تدارک دیدم و فضای رومانتیک درست کردم و از…</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/persiana_Soccer/27317" target="_blank">📅 12:47 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27316">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dUXoXklC8P_5LemnqTBXlwxvHMHOgs6YKVS9yXjaUlZkv440KpUVJVhE6NztctiEf0MTmPyBjhWlDLyO-7YkCQK1D45mGLA4jeUMEF3-QBHXaB0SGIx6FZKBS0uBaG1ALCtxaOBJQ3kVWAzQ8e-CJuZ0XHHYXOaZb8w_CETvICVAKDSGzscrQ82_VsZpV3tqwGW7b6AFy-j6mvJIJwm_ltj2NFA6tvIPRlUACIiYNj5Mf3fNdEIrKucQoo8HfOOtFmc1ox08uuouUvK0O-8EBp9M-KI1zQ0CKJRY1UiHPgcsSeOp_DQWIYLgyfMJOxTwHT8dVXLt2oFwT5iahdJYkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
نشریه‌مارکا:
رئال مادرید و بارسا به احتمال زیاد در الکلاسیکو رفت‌لالیگا که روزیکشنبه سوم آبان ماه برگزار خواهد شد با این ترکیب بازی خواهند کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/persiana_Soccer/27316" target="_blank">📅 12:08 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27315">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fGBvwfK_OO1zNNBT-xbXopcvHHXMrMv46MZZ5JbNoBD3rE5SXSTSQF6zCY5iRTR8o0RXG6-WQozgjO7y8CUAJ3Tlq-e0fr2wCvS-aHxWdV_Si3Xb2UWCGcyXV6IB75xaqtiOiD91Qqc185XS8bkjWUPYPPRUWjYDrIJ6sPZs0gCqv7uPPvQFY6wBYxUEPczLqgoAvtQMKbPGu0ISV-opSRloh27RGxCTaAjOIzeTMw7Py2xp9UqtYh-Kc191ihnNrMavYDN1mN3nVkELBCCsBNW6P1N5dDdrNT54yXIzj7S7XqxOJYLoisrJT8ORM-jhk8BqmRy_GY00fgUR-xS6gA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔴
⚪️
#افشاگری؛محسن خلیلی بدون هماهنگی با مهدی‌تارتار با امیرضا افسرده مدافع میانی 25 ساله ملوان‌مذاکراتی‌داشته و قصد داره تارتار رو راضی کنه که بجای ایری این مدافع رو جذب کنند. مدیر برنامه افسرده همون ایجنتیه که با مستر خلیلی داداشیه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.4K · <a href="https://t.me/persiana_Soccer/27315" target="_blank">📅 11:42 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27314">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MQmv06BttAITpkv0zxPoihktEYdGOB14uGQbHpRo-hunUOkWnPiauCAluX8CFTFhWQMTbxSjqrLU9VV7DcFYE6wCmEabDHJWQNsH7bQUQ4n3ojyFJpeQgxhuuMZB9lMcqKUG8mWnNZTFYC4ZU-2SOq2wD8sklFB2bFoDyrwVPHQnGieE2aQxwlX2eaVJTVGp2s1L8jCMwtbI1oFSuVs-kcYuynFDEuActjz2kjE9f95ZnykLAdlZTzWnWFk9l7mdWNlZG2A59Usbh7Se3slU_T1hrD-zR0KAP6ZOBKmjuP8DC0rwR6tElcgAIW0TWUbdEjaIIkmeuWEBVCPJRdntRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
جایگاه‌جهانی تیم‌های ایرانی در رتبه بندی قدرت اپتا؛ تراکتور تبریز درصدرتیم‌های ایرانی قرار گرفت!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.3K · <a href="https://t.me/persiana_Soccer/27314" target="_blank">📅 11:42 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27312">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FX8OAzXYopWWMbcLBLAlVeJCzJdbZhi3kSaqmd_Qhf1qm0buBSh2mwGDxziTCilWgT_QQ8aBIBWcLthTI0xgac1jsJjE3ZBa7VTsBw5VPprgWkGG8PxynM7aVa8y8acqGU1Sam48DDUNLbzHnh3efvy7MV7WmY_2x1lNbUOeELKYNzJoaTpdUDtLnFgQlEdjRDc-KJS7iT0CyHQkNLa2J5w3tCl-6WJ-hQtRGjvQqeJ7AmCimCpSX4E_5l_G5KuzEVvEjfuhK8I6T-1sAGmGBJSe4-sAwuZ1Ucc_tko4WRx9VnYjoqBoHDSzsYo1NCx3ergADUJjZUgM9FBs1WdZOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
طبق اخبار دریافتی پرشیانا؛ احسان پهلوان هافبک تهاجمی33ساله‌سابق پرسپولیس، ذوب آهن و فولادخوزستان‌مذاکراتی‌باباشگاه فجرسپاسی داشته تا درصورت توافق نهایی شاگرد رسول خطیبی شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59K · <a href="https://t.me/persiana_Soccer/27312" target="_blank">📅 11:13 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27311">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RoL4JKMqc8ZLJIMC_BzPYrFxXLwidXO3gGX6VVPgKwZ-am899wlaGUYmGCIWHGK-04llZGu7aUSqwjW8ZXTlsKtKA__VxYdfeqUHk0VD8YckmHgJeBQ6u3biwAKLj9IzcPvHuhRxAN9ei0sXRyEkDQ05Mtb7AIeiXySKjkjBaqRz67fc8cBG97LqyxJ6cwG8ONYFkWt_PusU735gkYt0xiQxTPTDLE_Rouo8tchA7U3jCpbMvdDqtBilW92MVCgqD_0lU-yboysL70DrVEy00NiDf6QUvcbA6Cvg1naspblqDgnMLiOWKAFFX4U959hl57SCQcxOBj2VV6PWCep4ug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🔴
🇺🇾
با اعلام رومانو؛ لیورپول خیلی شیک و بی سروصدا رونالد آرائوخو مدافع 27 ساله بارسا رو باعقدقراردادی‌قرضی‌تاپایان فصل به خدمت گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.6K · <a href="https://t.me/persiana_Soccer/27311" target="_blank">📅 11:10 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27310">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4a095528f2.mp4?token=MJHsEH31ii73Mprg_JqNPa0jA3hzMtouYVOR1whAHN1XBvcXxuS5H3o0wO3fU_C0svFd3aAYSon9sEVvMz8bYxmQTCHtA4cW2EbbQDF84oEX0YI12XBhf_JnjlfSI3gLuutMWBXm1LN_LmeR7SL7S47eXqMuZb4tpkfg10EnBXPaQwL7UaG7yq9ENEavWppGpdD8a_sSG7EeDSD2sy5ZeCq8QnlkU5f_iaZGirp9A5mjYojxyi2bMhIOgUKtDoiBHE76wRpc4pNPSQ9AIdzyrAv9dhnX3LFBG9wdpawdhW6dyNzw0AeXn7YW0oJ15nj4wjpgBko2QkH43W7jKk56Drfht8vAX-KU_27KL84_9f2nC2gkD5SGgxy3GVlE8SyGZ2I8Pe19OEZ7v4qG0-_Mysb4KFi4hVJr9sm1cRUVZyLWbezJPZ0w0tNTxOazrlOKM66CMCobTdzkYL5vwqk4wcDu_rHWn8VzKem3ccRhPSw23xIb4Evc7kz2LNqIZhRob-qFKreC7ibuOwGLuHpBYV-42t8_qNxQwxtcJC4okWj1oZFWZlRhL2CBV2-TdpqSXo51xOc8TZB-5voS6SKN9V-xs_abL6P3OFnPGCWKCEMsPkkZtYtCA_B3l4D74xrRa6HV_gIoe6oEcfCnSRdiuQTNooQdejw1a8uSB6M8te8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4a095528f2.mp4?token=MJHsEH31ii73Mprg_JqNPa0jA3hzMtouYVOR1whAHN1XBvcXxuS5H3o0wO3fU_C0svFd3aAYSon9sEVvMz8bYxmQTCHtA4cW2EbbQDF84oEX0YI12XBhf_JnjlfSI3gLuutMWBXm1LN_LmeR7SL7S47eXqMuZb4tpkfg10EnBXPaQwL7UaG7yq9ENEavWppGpdD8a_sSG7EeDSD2sy5ZeCq8QnlkU5f_iaZGirp9A5mjYojxyi2bMhIOgUKtDoiBHE76wRpc4pNPSQ9AIdzyrAv9dhnX3LFBG9wdpawdhW6dyNzw0AeXn7YW0oJ15nj4wjpgBko2QkH43W7jKk56Drfht8vAX-KU_27KL84_9f2nC2gkD5SGgxy3GVlE8SyGZ2I8Pe19OEZ7v4qG0-_Mysb4KFi4hVJr9sm1cRUVZyLWbezJPZ0w0tNTxOazrlOKM66CMCobTdzkYL5vwqk4wcDu_rHWn8VzKem3ccRhPSw23xIb4Evc7kz2LNqIZhRob-qFKreC7ibuOwGLuHpBYV-42t8_qNxQwxtcJC4okWj1oZFWZlRhL2CBV2-TdpqSXo51xOc8TZB-5voS6SKN9V-xs_abL6P3OFnPGCWKCEMsPkkZtYtCA_B3l4D74xrRa6HV_gIoe6oEcfCnSRdiuQTNooQdejw1a8uSB6M8te8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
ویدیویی از عملکرد خیره کننده و تماشایی زوج لیونل مسی
🆚
کیلیان امباپه درپاری سن ژرمن؛ تیمی همه چیش تکمیل بود بجز داشتن یه کادر فنی خوب.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.8K · <a href="https://t.me/persiana_Soccer/27310" target="_blank">📅 10:52 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27309">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">🚨
🔴
بعد از جذب کوروش اژدهاکش؛ امیرحسین طاهری مدافع‌ میانی22ساله فصل قبل نیرو زمینی که عملکرد درخشانی داشت در لیگ یک برای قراردادی 4 ساله بامدیریت تیم پرسپولیس به توافق نهایی رسید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/persiana_Soccer/27309" target="_blank">📅 10:18 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27308">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LqkVpg4vH1j2su9pWRL3uIGLtJgbqn3-hovpWglycmpLWWnPnW6B3dVw9bzrmWrTm6KFVMmI5xpW1HEQNH3c-FrSLSCBRRfCgOArfNJm4fsG4cv77MwJLBENqpk_IQGOSW6nOaHLjsbR01IRBsOqcjs2LrEaJ44YtM5tAIYXM87PpbRUFmNXUiduFMEUOZsEyYCnPQ0kvxRuP013uuScrxLi2LccmymlferKWnsfcM7aUO96_yx5f3uTNaddpnoqF690gxqdXMAsmYudflD2Km0qlJ8pEr6GJZG00a5LjIjgbe8xYc68q3TIRlC2uE9RgEYro4qAF0MnpvLH9z8cLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🟢
🔴
کوروش اژدهاکش ستاره 18 ساله فصل گذشته آلومینیوم اراک برای‌ عقدقراردادی پنج ساله با باشگاه‌پرسپولیس‌به‌توافق‌نهایی رسیده و سرخپوشان بزودی از پدیده فصل قبل رونمایی خواهند کرد.
⚪️
Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.7K · <a href="https://t.me/persiana_Soccer/27308" target="_blank">📅 10:12 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27307">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E49ym7q23kLfsed5oOQayN1IGNsdGFZ4SM2Y_AaCCm-YKJnX4dN31xeBp12qHT6zbD1EPPzbNhy9uGT_BwUGcDliNLZ7_JypnDrYoQAHpS00yIjoaUbTlFf9JcRk6w_XtLLIOWiH7dllZyFXBbd-g57t4UuiyzeyutBYHLjFBIroLpTGYjJOaVy46iIRATMG1dCRS0wxkJ4Sr7wypw2He6N-YQ-psqCN-PTeDiGKJrH_6is19luJpxfj6UPONrVq33KE2anq5MCuhrwL2vX4s3l8HPfRIZKLCyszhHPClU-OhZUMjmDAyCnblQaJrgOcQLeOlGfXFxIDmC9eA6P2Ew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🔴
🇺🇾
با اعلام رومانو؛ لیورپول خیلی شیک و بی سروصدا رونالد آرائوخو مدافع 27 ساله بارسا رو باعقدقراردادی‌قرضی‌تاپایان فصل به خدمت گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.9K · <a href="https://t.me/persiana_Soccer/27307" target="_blank">📅 10:00 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27305">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DM7yCK3RYRObcxYftTJAk6cd79i9pN-Y_QfqOrtPuyp3cz9IJ2iBztiK66pL-L4KExzEUlvaQIqpC29d45cdllzpc2PlLUIa4wNW-VpZOEA3PhDusiBGgIHCwdhlqlg6xCTQDtn0yN1ivAg7I_bAkcCvj_WklMVxpv5xxPi9iDVv8nYRfW6-ctPpUlpkKTy4hzWurFYt_79RWVNzXBF_-k3drB9Av4xv3XJfstdBGcuVs2U9_nyx1W_lwy3S3Vt9SDS5lVQjMAGZhLJoIekbrrsd1dF3KsY9ox6aL5VfKXnmA78IxKsIRfiDQCJJSKye11oSvh80SHvhFF_OEUwP_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇹🇷
با اعلام باشگاه فنرباغچه؛ اسماعیل کارتال با عقد قرار دادی دو ساله رسما سرمربی این باشگاه شد. ارزش قرار داد دوساله کارتال پنج میلیون یوروعه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/persiana_Soccer/27305" target="_blank">📅 01:31 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27304">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I7GEys4qE5aYjRsxw7_wm9qOPnSpOBZ6yCduUA7dV-z_ZzFR6heFnbXLSIjdcDUMfRLvpiE6-SoU_5LDZGOmg4W39dizsbtl9jan541wt-sVrv-eTGHm_pQBEetKgreZIyEuYcwkNb-Of3_ydh3aJvzDKHgE8lI1k8qGqfc-QXRfXqAc9002EmDLbEV7NknNtOSpeolX05z8ZPWfKCbCvE9HyGkDTLUnBy4qCcb5QUMuntDPRaORR8le-0NSh66WBbR_F-Idw6fYvjmfDgj5Qa4seFg-oJWEFfuZQ8YLy7yA0HEQQGqI5HMviFF2HA2pJ7r9lUc-qdkoxPEgxRxz1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🟢
🔴
کوروش اژدهاکش ستاره 18 ساله فصل گذشته آلومینیوم اراک برای‌ عقدقراردادی پنج ساله با باشگاه‌پرسپولیس‌به‌توافق‌نهایی رسیده و سرخپوشان بزودی از پدیده فصل قبل رونمایی خواهند کرد.
⚪️
Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.4K · <a href="https://t.me/persiana_Soccer/27304" target="_blank">📅 01:29 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27303">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cc07f33275.mp4?token=U6geduRT6KcWvu659qrgDWiU6dogQJpUvKwPX3Un2eXf7Eun5uQ4XDI7y4h3tEIpRDXBOUhpKqedYOAPv4WCKcJ66haiCMYZ1ZwRzGq3hWlZkiq0sKB0QZdpD-zCmrAFu0qfUxBe2nksox8Rw2rFukmhbnfmqdZjrHI_EyQoUPKMRGGKtG6GU51y-4WMsO_EQbkHanP_59xfiab49JZFE7E3OnjazKxw8etByKtNpfdy4BXVXoxdpEE6Ygq4bV3gW5r748wsXTaD6mn8OHCLfm2NUas-JioudYLx0WRD_TxHhcW4SiT3vt0Aad1ogJlp58diFrK83DoSvtUY8dwupDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cc07f33275.mp4?token=U6geduRT6KcWvu659qrgDWiU6dogQJpUvKwPX3Un2eXf7Eun5uQ4XDI7y4h3tEIpRDXBOUhpKqedYOAPv4WCKcJ66haiCMYZ1ZwRzGq3hWlZkiq0sKB0QZdpD-zCmrAFu0qfUxBe2nksox8Rw2rFukmhbnfmqdZjrHI_EyQoUPKMRGGKtG6GU51y-4WMsO_EQbkHanP_59xfiab49JZFE7E3OnjazKxw8etByKtNpfdy4BXVXoxdpEE6Ygq4bV3gW5r748wsXTaD6mn8OHCLfm2NUas-JioudYLx0WRD_TxHhcW4SiT3vt0Aad1ogJlp58diFrK83DoSvtUY8dwupDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
ویدیویی‌خاطره‌انگیز از تکنیک‌ومهارت‌های خارق العاده لوئیز نانی ستاره‌پرتغالی‌سابق منچستریونایتد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.2K · <a href="https://t.me/persiana_Soccer/27303" target="_blank">📅 01:28 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27301">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U3IP_Kue9RnuXtwDEXZR3sv-BLHwAXfC4IoVm14S1WAerfa7MdGYhk9KytZWqxP2eGWFIRwsG1m_hrMzgKR7ASm5QKNDaqGLwB0xKRFc56ofzwBjF2iKZzZVCgOXIlbMEBY-nw1CKHY1RmhUgT7wGWgMm2NkFkM2kyMqYKQcNG7kra3zxnPeBrIXfhriTkDt46hUMiCPdigm_-efbRaJ-L3urOMzuJyq0GVKlFLW5YZjZiMmvNZIHIW1euq_CD7kQcwY67bRQPYCYfdZDcVQ3SRaRl3ZE2twy_mh9ORQh_hW58E4ipHBHzg-_kWqyLQ-wR1zQvkQNoH0hw2LWjhEyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🔴
🇺🇾
با اعلام رومانو؛
لیورپول خیلی شیک و بی سروصدا رونالد آرائوخو مدافع 27 ساله بارسا رو باعقدقراردادی‌قرضی‌تاپایان فصل به خدمت گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.1K · <a href="https://t.me/persiana_Soccer/27301" target="_blank">📅 01:07 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27300">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ezt4lEElefiG4T44KWi6FKCM1V92SZ09B2HsONlLDKSUvGwN5U-myy8fKNyhrvKRY6dQegnT6TuOJv1qRKL057n1lkOTVMjuuIA-AClRyuDloyqzVU9JC5MbKn2v8km-0ymhhqex6pMhisdkns4MEqbBbXzg9qYsVKDiMJsGnYuRo5vj3EhZ_7k6mOY38iADLgS-bR11MZ7GYu6DzWJJd7LWS_aGWcsJcZTvCAsPeS7BwyKXDyk9_WXnKmnxcPKK7O6x8-2qmCnYzWt7NcimC4mJIqmMWezyHyVBwqBFqXqWPzEw7xItzbI1H4a8zaniJQd81XlEqn8Ca0mGgrVIkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛ مهدی تارتار امشب‌باردیگر به پیمان حدادی اعلام کرده اولویت اصلی او برای پست دفاع میانی دانیال ایریه. باشگاه‌نساجی هم اعلام‌کردیم که منتظر است‌که‌باشگاه پرسپولیس 120 میلیارد تومان بابت رضایت‌نامه‌دانیال‌ایری پرداخت‌کند تا این انتقال نهایی شود. فردا…</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/persiana_Soccer/27300" target="_blank">📅 01:01 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27299">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SK6A1f14bcEyd9G9tQxSFlViAzXaVpuVM8CBRmj9qTmXE7QJ3E0arNxFnpKgjgDhvx6sVX-0uEr09aEOlDIZ43ttN8hq0JxKaBXMmyKss_qvJlLkm2B4669qqhViOQgrCnPwPsL_JPLQIOnPo859fRprcC34JPe8lhu4BtcbncFy9Jgcd3Dj1JGe5PBK4i4T1qLgqrS0NiaSD-GHOcP8tPBHrB0y5vdvQPI9KltaaAobADvlqc7FOtprgPARiKMQsdjbrWPMmMjfN-3P_-GNlawTaasAWUWySv8SN8FVIS3G2p5MBq04xG-EwlIa3q9SYBPvoxPaGIw2qj3menaJfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔴
⚪️
#افشاگری؛محسن خلیلی بدون هماهنگی با مهدی‌تارتار با امیرضا افسرده مدافع میانی 25 ساله ملوان‌مذاکراتی‌داشته و قصد داره تارتار رو راضی کنه که بجای ایری این مدافع رو جذب کنند. مدیر برنامه افسرده همون ایجنتیه که با مستر خلیلی داداشیه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.1K · <a href="https://t.me/persiana_Soccer/27299" target="_blank">📅 00:46 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27298">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rKofRFMT91L26al3_kRn947d4wF_2OmVPFzfSaQ5N3uqNPcu8pFZpTO1q0ejDEGmA6w0thoTAUxw_YmGpv3YJMw0odOa7MWXFFOkJ1c0kShgh4qoFzggboXr836R9IeMq18Y4LxeFoblHzCy2CQonbPALbJGhbI8cfzap6aQdtA4LlrTuT6qoA9b76SHPAaKihVrj7M5q34Fiu_hpB_ujU7bsGEkStIFqqQMhaPsmjxdClqfRZuq08s2Ft4IMMy_WaW7iewv6zTB8EirIvIGfZsmBlGzy-otPGb6RWy9v91LslPPNtgyhwtnqmRZQXUavlO_KvYgZDouVCeixLrv3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌دیدارهای‌ امروز؛
از مصاف روسونری با آبی‌ های لندن دراندونزی تاتقابل دوستانه یونایتد و PSG
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.8K · <a href="https://t.me/persiana_Soccer/27298" target="_blank">📅 00:30 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27297">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/soDt56qSbGvyujfb7v4E5vGzK5EBZL6l-R9Zl5U9XwdRnD6NrfdIUh0FnSxOFTY4I4_O60LRQS9vE0HIMrgmb5O6NhsyopFDr3priFwV9SOXei1liUw_KGx9cqfhKFdbfHCfT3AOeKkIduuEKt50cKgU518GSmB8TzxyxF0t-lQD23i2EeEtS30HPXiRi92Vu9DcKkttlkXS-gGil0EqBXjk48y37oDmSah8mrDKMj6WRnczeF-Tnv8nWfjxgraR64MWthoCSf9PHk5m-groZCAZUicSsYOpaTX_1NhCXRPkqOYMhiTQd2sv8wfqQXzr_gAcP55LDcnQrm_5Q9uLaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتیجه تنها دیدار مهم‌ دیروز؛
برد شاگردان کمپانی مقابل استون ویلا در اردوی پیش فصل باشگاهی
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.4K · <a href="https://t.me/persiana_Soccer/27297" target="_blank">📅 00:30 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27296">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/12d08bf5d5.mp4?token=KR1kJqUcAgU4rbuqGFTlq00z_BVIolVERXXoxLnFDGDvA5ehzALrK3bVcrfdfFGI8ahTQC9UHHMzycTT_K8ni263bvKAx86YOUKgG96kTeqQudndwLVDPWap00S4McXa5w51M9mQ0IXhdXRWPAAEaPFr_iA98y6Cw953YDtRAv1EVP7VHkcq8rPETF8B-Wrvaqx5psJ9qmUVuQv37SfGqC36yEp1cnunUkHYpLgcHX29vjt61PTZJtbrG_dNeaf9Hq3ICqdZOaxKL4lpgwk0Q6q7YOe1VHqSaolh7Eu7khB1iomYDduRmc2H4VBVXMNEa3C2XYbIbMerkf8G4e_BfA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/12d08bf5d5.mp4?token=KR1kJqUcAgU4rbuqGFTlq00z_BVIolVERXXoxLnFDGDvA5ehzALrK3bVcrfdfFGI8ahTQC9UHHMzycTT_K8ni263bvKAx86YOUKgG96kTeqQudndwLVDPWap00S4McXa5w51M9mQ0IXhdXRWPAAEaPFr_iA98y6Cw953YDtRAv1EVP7VHkcq8rPETF8B-Wrvaqx5psJ9qmUVuQv37SfGqC36yEp1cnunUkHYpLgcHX29vjt61PTZJtbrG_dNeaf9Hq3ICqdZOaxKL4lpgwk0Q6q7YOe1VHqSaolh7Eu7khB1iomYDduRmc2H4VBVXMNEa3C2XYbIbMerkf8G4e_BfA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🟢
🔴
کوروش اژدهاکش ستاره 18 ساله فصل گذشته آلومینیوم اراک برای‌ عقدقراردادی پنج ساله با باشگاه‌پرسپولیس‌به‌توافق‌نهایی رسیده و سرخپوشان بزودی از پدیده فصل قبل رونمایی خواهند کرد.
⚪️
Persiana_Soccer</div>
<div class="tg-footer">👁️ 65K · <a href="https://t.me/persiana_Soccer/27296" target="_blank">📅 00:20 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27295">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/198183711e.mp4?token=T5-OkZ_Blpga7RuIZZaLX4hSVCcNbnWjZ2VZKXiv6QRu56kU03s24pY8jnwBfZmLVd6AdldeBPWP_BVGGDZcd7617-Bkx9xyXxFZmiZAwf0HJ8YxfwKWbXjuXkAwcdVtMsmPjzDAhFINZcLDii3M6xDyekcwf20k2sHppJi4cY9zE3zPnTa2IwcvX8Ik7D-bIUZem8PiyRNap1zcb_J2aKcPj-w_B7VGvsY8feL6SLiISv1NVr97Ukq18VuCd01iIESfCk4xHXm0McQaov59pWOiULr9miB6TZL0ax8bMH2128R6mm_de04Hcjx2BByJ4KXP-ZeWhxd2hrLnv4rx6w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/198183711e.mp4?token=T5-OkZ_Blpga7RuIZZaLX4hSVCcNbnWjZ2VZKXiv6QRu56kU03s24pY8jnwBfZmLVd6AdldeBPWP_BVGGDZcd7617-Bkx9xyXxFZmiZAwf0HJ8YxfwKWbXjuXkAwcdVtMsmPjzDAhFINZcLDii3M6xDyekcwf20k2sHppJi4cY9zE3zPnTa2IwcvX8Ik7D-bIUZem8PiyRNap1zcb_J2aKcPj-w_B7VGvsY8feL6SLiISv1NVr97Ukq18VuCd01iIESfCk4xHXm0McQaov59pWOiULr9miB6TZL0ax8bMH2128R6mm_de04Hcjx2BByJ4KXP-ZeWhxd2hrLnv4rx6w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
برسی ثروت و دارایی برگ ریزون مایکل جردن فوق‌ستاره سابق تیم ملی بستکبال آمریکا و NBM
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.2K · <a href="https://t.me/persiana_Soccer/27295" target="_blank">📅 23:53 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27294">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pX5zFeapqkFZpifXK2bDaj6blQ-JkJMXVtrU4Mey4-igT3hRYfhkZ5QlrOMeBZGOKfLZvM4LE6dEaADqQ2ogH2qD1uZHCTLM0C8Gyj-gCvOiFGzhYYtbpdq-b78SR8vd1Ow1qAAU_zKAUfZcbmDN_E86RIkXUpyVM-zuEKPz1YfglNZLj9rF665QaOTZlCHVnA6pgnoSklXqjzhpoTJSc6a8A4opRR1ZFYJWXSi9tWRv68YgfAKPTVYUXGx1hk2KukXH3YpXaRPebrYMYpag44FdnCjlS3zkOy3we245-Bruq8kfY1KlbrVdhe9TLhrUK6EuBSyyZrKnok7OrtIvmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
👤
#فکت؛ هانسی‌فلیک ظرف‌دوسال حضور در باشگاه بارسلونا 55 میلیون یورو کمتر از مورینیویی که فقط دو ماه است به تیم رئال آمده هزینه کرده!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65K · <a href="https://t.me/persiana_Soccer/27294" target="_blank">📅 23:32 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27293">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W13PZoscMqnpzNsooZkNf-NZhyNUZBmrzsgAugZ_X0JZB1sEJJJ9xeRGahMm5TSoSgFNwiy7O4XJPd2nQdf0vwfcVYrZFvUWFae3GNUDclK-Pfm6DrOE1wDiZ6mw0CmWeUZOcx03IdaxrEtB-OUFLS6rpjLaHoWdWLckI1dwyCBckput1OTsxcaaNf6G4E-9ffq3ECMvBvzpFHO9imTjGTRuyqYTDOx40nbKFVTXKAAm7_ua7Ji1M7j-yMwRz2BQ8YF4erZy5Ct7f8YCjXDL2bLqXtcD6MAS-SKvpeeyifsIuv1DrKnuX03l2aC8oS8KhQGdKwxwmXe1GogBB1lIiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
زلاتان ابراهیموویچ اسطوره‌میلان در مصاحبه‌ای جدید از دوران مدرسه گفت؛ زمانی که یکی از معلم‌ هایش آینده‌ ای برای او متصور نبود و تصور می‌کرد این شاگرد پرجنب‌وجوش به‌جایی نمیرسد. اما زلاتان مسیر خودش را ساخت، در بزرگ‌ترین تیم‌های ایتالیا درخشید و ثابت کرد…</div>
<div class="tg-footer">👁️ 66.7K · <a href="https://t.me/persiana_Soccer/27293" target="_blank">📅 23:07 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27292">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o_xFGzxKfC9MHj7MVNGKm4ic9Lnjcv2qytMZ46Bo9haJJnh99aKRXo5PvdsqY8lLJ5dcPstDk7W5YEW7cm98by3DMcIUPUu9j3fpPEgJpkhLQxxXSpA5-rp2TS2aT8Pet0OLgWDAIdyxBKVObvRyNbqAQOttJQvRAd-gmTUS8ihuIcdNtHoY4P8oPCjsxAlDWmusok0j05khQc5wSdqkRUNFjfR4fTt_R0FJPP2KyMwXWmLaHH4ofqPOcdYi6cQiiCwi3aiaNGsQrCnoDgKqwewoxZdlK6otnIAe1V4bEWyqrsRPQpxu3yQAO7FxVXxMuej9wFfof4fQUN2xR6L1WQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
طبق اخبار دریافتی پرشیانا؛
احسان پهلوان هافبک تهاجمی33ساله‌سابق پرسپولیس، ذوب آهن و فولادخوزستان‌مذاکراتی‌باباشگاه فجرسپاسی داشته تا درصورت توافق نهایی شاگرد رسول خطیبی شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.1K · <a href="https://t.me/persiana_Soccer/27292" target="_blank">📅 22:50 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27291">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CGiwBpMAk5-aG7b0SXpEINzdCV-o0CzseoOf9mc7sPIbzLenMPlGX3bHbABSHuaoT4jrUdirUgCbaMLBXwiTuluC1Ga50pUDM466oH0gGvJccY4_8e2KHzBLpx3wCqd-21ws0MR5j0Ddi09XxclcJz5FfiBhcl8Rh0KlGSCOvhEg0ycJHnlsfyqbxLUiHxTm-NVtM6d14yrfQ5XArk_TmDvldJ_dBWPzRTUpuXayyl8ZdFqdXVbr1KT8ehJjlH-oBhoM072bgRq-KdWn-rrOdepTXz_MJwYClsClAOvHr_g6Zv2kkvtIz-RbABmrS_RPAhpMpJKJ6tlLf8pvD91TpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇨🇮
پوسترباشگاه رئال‌مادرید برای یان دیومانده ستاره جدید خود؛ قرارداد تا سال 2033 امضا شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.8K · <a href="https://t.me/persiana_Soccer/27291" target="_blank">📅 22:33 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27290">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F8SCy4dwousgcXbs24VF9ubkszg0h2TtnNzMl65SjqKP1U5Evmj71uQksdb-QMBgRcO7hcOR8z3VT0RzijkkvR-JeV6t8TMxUyaN87BzSmsWwZwpFcXnl7WIchKtm3rVfY2eO8Bh4qhhigBk34hpjexJzrjDL9HuPvCtnksdWtgGzwA3D8oCXkEIxRCC4DuyvfwCDt_GzCiMFAY7kpXGXeFk91utanQnSSgVcLblAwVNJHfQ4xhXN-0KKft4QuLRRRUcNXElbhRUQ9ZuSx3FVxbCf-LoBTyeC_pWHNkadcf7y5sJBvHntCh-dMk-8_lnZSaQCVFkqslydsMONrwPxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
آنتونیو آدان زمانی که تازه به استقلال اومده بود با الحدادی زیاد حرف‌زد تااو رو راضی به پیوستن به استقلال کنه حالا مدیریت به آدان گفته‌‌ اند بار دیگر تلاشش رو بکار ببره و با منیر و همسرش صحبت کنه تا شاید آن‌ها برای بازگشت به استقلال راضی شوند.
⚪️
Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.2K · <a href="https://t.me/persiana_Soccer/27290" target="_blank">📅 22:10 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27289">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BZXZd4yjYrSu80A3YoVpyplyezTLZyIT2tfX82ZkxxViUIIf4fMfZqpTOAhfs2gOxIid-UTjaWmPd9NDIhqGzVloM-WhbQgiivonueFwYya_SJwsiIatCmcXu_-Ztsgd69m55m1nvz5T-g2p74dcZO-ASnGwBWngUbGpb654PXIGDV_tdHe8kSelgovS52kqY-M82BAdOv0uJk2kY2at72yjlvYSb4iI_QmRxS4G-lkG_m7b7zhFMxwlO_Hzs4A2XGUjr_hF_2GI1G_qMU8T0s_kcJsvYL-9UXe-fEPbL9cnuyN6UPM1Hf7yi_r-7Nfh06C-lQvRIXvmHX6LO11Ibg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔴
به صلاح دید کادر فنی سرخپوشان؛ مجتبی فخریان و محمد حسین صادقی از لیست پرسپولیس برای دیدارفردامقابل آلومینیوم اراک خط خوردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.3K · <a href="https://t.me/persiana_Soccer/27289" target="_blank">📅 21:53 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27288">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Sj5Bzv7kwOBz162tyfqsH9mgJxurZB808LNmjYgWpXl_vs2FRQJ6KnlsleLOqyxAQQBVDhdtinaog7K_HbhehjBtR76fS917pZCeatj55gdmnd70MDa7PPETW3agxoDAxMsXo9lloBiEDUlwDzm1Gbh6oWGtEGH4QVKwnlrTTg3l9m057qAijzesfHtSkXTxAGsnj0JyN1LbojcBKiObpdki8ho3I5YkMhmSZeCNKCQA_Vf1M9vKsUP9EsYSZWvIOPIL5J7noacujTdx70LGhUQtdxLRYQG40V17kz7KQJ1s1l8lQST1NdkhzAQKZSA-bp9EU4bdERuhESIOPJbQSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
نشریه کوپه: انتقال رودی به بارسلونا نهایی شده. او دستمزد بسیار بالایی در بارسا دریافت خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67.5K · <a href="https://t.me/persiana_Soccer/27288" target="_blank">📅 21:26 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27287">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sinCuyK5vy5xNNzjjDXhXD-1_H3XJEsMcoq_xMYtuNYG8cmHDFmY7O7-n4zlUYa5j9SBNvi12GAdYxK0DH19VX9_VLrdThqs73b06PoS8x2DxpoyDdc92zcstPsmp2vLnRKyba96EI1QboFY8XVUCeMFsAm5V5IZpKIBBeSA18mH1fnNp5MyyrKjmxQkqyom_lbLqm7T-wmjeoDiB4YNKnlw8rfP4vL-3bYtCjCogz4nAeuvSDKu14-qmtgGFlg6glX3GGsiSTgpW0FYvpgEZXcNw3VUFNUV2wUuHonbIwVNmiPhh5k1B6V3qdVCScnqFlRxfoDkrTiw9is-HTgkVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مدیریت تیم‌استقلال باایجنت‌های دیدیه اندونگ، موسی‌چنپو،داکنزنازون و آنتونیوآدان تماس‌‌های خود را آغازکرده و اعلام‌کرده‌هرچهار بازیکن‌رو برای فصل جدید میخواهد. اندونگ، آدان و نازون آمادگی خود را برای بازگشت به تهران اعلام کرده اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.6K · <a href="https://t.me/persiana_Soccer/27287" target="_blank">📅 21:13 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27286">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tKb3q6Ogkw2zbpW4CqlbnLa_2tZO2hQQaWKFUH-hNR_fNXeIGTQwJeGpB46ZM0zD3QPRyq67O7WFED9BSuISue7ewsN9_oSbwI6MDsUzMtAemeiWMYC9NZScemOyWcCruIfyaumFjSUvlcva2eDC76YmBsv43np4210tDXZUkPKolRXuph7PAQ6QiQcNEuy8f2G-qVs9Bnffekuib_6Il4esXBkq6KHksHXOdhfHR9zTjlSBpF2TttKD3pHi_p4k1j_aprpHoMdQc7uo7F3v4Rxu6gzmqk_NO7scAhUkShbF8kWxK1_ytfAWB1fr_Me1RRIHd_m4VZp4Ii3Tj6fgYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔴
⚪️
#افشاگری؛محسن خلیلی بدون هماهنگی با مهدی‌تارتار با امیرضا افسرده مدافع میانی 25 ساله ملوان‌مذاکراتی‌داشته و قصد داره تارتار رو راضی کنه که بجای ایری این مدافع رو جذب کنند. مدیر برنامه افسرده همون ایجنتیه که با مستر خلیلی داداشیه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.3K · <a href="https://t.me/persiana_Soccer/27286" target="_blank">📅 20:52 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27285">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bLSHb1Mi85YRfAsZSzM3fecG7or2ZYsFIHSJ5rNKrdliGro9T-HMrCxByahysk83cpIdKoIMZ1A4UVEpz0NVgyJ7ZF3IMAUf9Aw7JQ2gUQR2bZusiuFUnYxcFHvirHgq53xLda8efrzoKItev1zot8CDjGO_xl-WTHmuIDcahVavaLvTxbWgM2ST_fj2OQUhy-v3UeKAPVDBBpXjz0m3FllnHEf1H3RjpXmkKa3GpAVEy98dNwZkg8zychuxdXJeajl-KAQYza2HyboXcSMk8Rn4xRfhiIrdpcwgupdTnwCG1JUggECrRKpBdE1X_Bkam04jeFflJOv0LioVRE0mDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
زلاتان ابراهیموویچ اسطوره‌میلان در مصاحبه‌ای جدید از دوران مدرسه گفت؛ زمانی که یکی از معلم‌ هایش آینده‌ ای برای او متصور نبود و تصور می‌کرد این شاگرد پرجنب‌وجوش به‌جایی نمیرسد. اما زلاتان مسیر خودش را ساخت، در بزرگ‌ترین تیم‌های ایتالیا درخشید و ثابت کرد…</div>
<div class="tg-footer">👁️ 66.5K · <a href="https://t.me/persiana_Soccer/27285" target="_blank">📅 20:19 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27284">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vj6IU1IM1a3_Dkg0g7mezK7hNwea5ONaSmuOyfEpwRXv8RQ51xncaa_0pttr5wSckHqMxLGpnM6jhrXB19fq302KT8IPm42PneuPtp92SyZt5GBNgR27dl9ixdcrxiJzHVxz69BZGiGUB-y_Ol5WRV9Hwn79LAcYEnGQNdBt1xVR1phepnQlRP5EdnuFST8G17f6PRVUL13qwwUALdb0Q_xvCEnRkAv096zZG8Gf1heDEHtkFqVekjFAtxGWZT7IaUsEGfUHRH-_qyhCK7eNB8yWQJ3BMV0fDhiMSiO6CnBucZUYYRbUJhnlIFeFZZVBmiO9yiNAheXtk3N2n3VyTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#تکمیلی؛ آنتونیو آدان موافقت خود را برای بازگشت به استقلال به‌مدیریت‌آبی‌هااعلام کرده و این گلر اسپانیایی بزودی به جمع آبی‌ها باز خواهد گشت. باشگاه در تلاشه تا نازون و جنپو رو نیز برگردونده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.4K · <a href="https://t.me/persiana_Soccer/27284" target="_blank">📅 20:07 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27283">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5be754a68a.mp4?token=huPf0YYMhyH0ifI0ushsRyVDdihpOhY0wnd2WqY1Lj5cjU4DlKOHP-l5Pv-U2B8ytuFJLD4SWHKqVSsQswp36vo9aa4JT2Gy1060ZdWTesSVdhhDACpYAgjUQy_mpP42m1su2LTa5eln88gcsvwf7BJmSSl2IaFfX_I-RibdPYBHwN1lQJKl1HJ8U-_5yaIRPF4aQZKTpH8RKTaWFhOwqQMRbofuaWeP2nLC89jA7JhYkbAkGWfCEb0AekEaxDR9BS4uNcHtPe7-yMgbOWS979mImTPxB33d52Ryg3_nbXYhtMMUq2f-YvZtnI-mk7SGs9Q9QBuvWw3MAvw-cg2YHowJgkYTBYKzErcR23QuPWX0lAKpZv0nXHdg3Ql3ir1mnzDu4wXgSov06EfVlLOJzA_TZ7H5aphGgtga4fYiq_M3XRdm3aGMv0dgHRn8nW93brQI4MwHv0Bsz2OkQG6mjIMzs6ouRx1-d4StIYvCnPoUSzxFkFfbwg4tBKs3T1wN-ndhr7bMh-HnmmHlpfvMVL0xgSTXXIouDyeYPHNHj0-Ciw4p2L_7CHEASJZV9-BX8B_o-OmFRp9fZBQEktppTvO0GdOziwMt0l0TXFAu2eUF0EghTwquzAoSDL1OW5KPODpuL7UlRVE89wVucgN_jryPdSethyNVM7Qc4deemts" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5be754a68a.mp4?token=huPf0YYMhyH0ifI0ushsRyVDdihpOhY0wnd2WqY1Lj5cjU4DlKOHP-l5Pv-U2B8ytuFJLD4SWHKqVSsQswp36vo9aa4JT2Gy1060ZdWTesSVdhhDACpYAgjUQy_mpP42m1su2LTa5eln88gcsvwf7BJmSSl2IaFfX_I-RibdPYBHwN1lQJKl1HJ8U-_5yaIRPF4aQZKTpH8RKTaWFhOwqQMRbofuaWeP2nLC89jA7JhYkbAkGWfCEb0AekEaxDR9BS4uNcHtPe7-yMgbOWS979mImTPxB33d52Ryg3_nbXYhtMMUq2f-YvZtnI-mk7SGs9Q9QBuvWw3MAvw-cg2YHowJgkYTBYKzErcR23QuPWX0lAKpZv0nXHdg3Ql3ir1mnzDu4wXgSov06EfVlLOJzA_TZ7H5aphGgtga4fYiq_M3XRdm3aGMv0dgHRn8nW93brQI4MwHv0Bsz2OkQG6mjIMzs6ouRx1-d4StIYvCnPoUSzxFkFfbwg4tBKs3T1wN-ndhr7bMh-HnmmHlpfvMVL0xgSTXXIouDyeYPHNHj0-Ciw4p2L_7CHEASJZV9-BX8B_o-OmFRp9fZBQEktppTvO0GdOziwMt0l0TXFAu2eUF0EghTwquzAoSDL1OW5KPODpuL7UlRVE89wVucgN_jryPdSethyNVM7Qc4deemts" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
حمیدمعصومی‌نژاد خبرنگارسابق صداوسیما هم فهمیده که نون تو فضای مجازی و ویو گرفتنه؛ حالا ببینید چه ویدیویی گرفته از مردم شهر رمِ ایتالیا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67.3K · <a href="https://t.me/persiana_Soccer/27283" target="_blank">📅 19:42 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27282">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/97a5e9dd3a.mp4?token=pZF0olDcDpe5a9uyaT80L1HBW5bjpE9y5jXmw1_KUnKGhCGu7mSyoNwfVCDQXqmKBPFpIaI2vSF76PyRxuF7ntunlsoH8FWNpqpvzZMFzjDl2EyHJ6xjhvZ8Gle6Qv7ocaPwUWoopEpfe35Yg48-iwjXjdgScPgMG3EpBq9ty9rUgXCfPe30SIas_5vkCth3pnhO0R4CpmK4e3z--Ckhh2dBthE9QTiBsWUacXhOVio9kmI9e2pC3Fuf1LEUk-1bZ6Y6QR0cdPivc3y5EQhyuVN_dFVRWIht5abdNaBa0gKaBvCiXPjOo0OElCyIJDnWz8oOT8gVbHfxhV2a3E6X9QE3TKvTn-_obbfXVzoE2fNGQgyrFclijzm8easNVECrcTY7zS6b6lzaShLk8OMuKWrJFHg1wUGWZOW-EQITkLZmtXCrLENLTegyH_jQXm6zn8Ymt4u2akoFFoXDeR9-5H1Ss7fZaRhu_THSpB5C-nKgisDautQsnbY61I68wcixhgcU6SlrLY3ZxZMpDaa2QdsY0eGoDfXZxKBKo28lGmJEAOs5uRnbIGxMXzrSKXPftvnBTv9eqN5KFkN-_VC4iisEgNrefzvRdcQTocKauECYBhOhiZE8aMHW5PNwjRxNkhIg0jGJkdELIMVEfraC_kT-68N70sOWz4zBPDt5K-8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/97a5e9dd3a.mp4?token=pZF0olDcDpe5a9uyaT80L1HBW5bjpE9y5jXmw1_KUnKGhCGu7mSyoNwfVCDQXqmKBPFpIaI2vSF76PyRxuF7ntunlsoH8FWNpqpvzZMFzjDl2EyHJ6xjhvZ8Gle6Qv7ocaPwUWoopEpfe35Yg48-iwjXjdgScPgMG3EpBq9ty9rUgXCfPe30SIas_5vkCth3pnhO0R4CpmK4e3z--Ckhh2dBthE9QTiBsWUacXhOVio9kmI9e2pC3Fuf1LEUk-1bZ6Y6QR0cdPivc3y5EQhyuVN_dFVRWIht5abdNaBa0gKaBvCiXPjOo0OElCyIJDnWz8oOT8gVbHfxhV2a3E6X9QE3TKvTn-_obbfXVzoE2fNGQgyrFclijzm8easNVECrcTY7zS6b6lzaShLk8OMuKWrJFHg1wUGWZOW-EQITkLZmtXCrLENLTegyH_jQXm6zn8Ymt4u2akoFFoXDeR9-5H1Ss7fZaRhu_THSpB5C-nKgisDautQsnbY61I68wcixhgcU6SlrLY3ZxZMpDaa2QdsY0eGoDfXZxKBKo28lGmJEAOs5uRnbIGxMXzrSKXPftvnBTv9eqN5KFkN-_VC4iisEgNrefzvRdcQTocKauECYBhOhiZE8aMHW5PNwjRxNkhIg0jGJkdELIMVEfraC_kT-68N70sOWz4zBPDt5K-8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
خون ‌دماغ شدن شرکت‌کننده زیر فشار؛
اتفاق غیرمنتظره در جریان یکی از آیتم‌های فینال «مردان آهنین» درجریان‌یکی‌ازآیتم‌های برنامه مردان آهنین، یکی از شرکت‌کنندگان در اجرای حرکت دچار خون‌ دماغ شد؛ اتفاقی که برای لحظاتی روند مسابقه را تحت‌تأثیرقرارداد بطوریکه از ادامه رقابت بازماند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65K · <a href="https://t.me/persiana_Soccer/27282" target="_blank">📅 19:22 · 16 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
