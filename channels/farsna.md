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
<img src="https://cdn4.telesco.pe/file/U6N0wJ1VquEIA4yffvfDYnDnhgl5N2RiWWE3Yj5P_aqYrRHT-K_R7s_ZJCjmJt3oqBXRvS3uYtWhcaE6FeSNnW1rQf3nNCfIBSaEdodbDPZeweYCLoVTvguLTLQPtyfmu_505yEbjdWV47QrSKNHi5adb1-PP-iBSdlHsSlOJIpymNzAN9R56fj8ru_qZxqVTNxTZeC2lKP_G_US4B-LKc6TTsB8f0dRWC94PiGcRQApShYc13q4Vze5Xirik1zum_Icd01WsrE9cwSDUHZxZoThueuyHLeWVwz-ivlum4oR5EFDYHh3Lvbo80gs-t42npzqjvmL-AQG-ITFemE74A.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرگزاری فارس</h1>
<p>@farsna • 👥 1.83M عضو</p>
<a href="https://t.me/farsna" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 حقیقت روشن می‌شود‌‌تبلیغات@Farsnews_adsارتباط@FarsNewsفارس‌پلاس@Fars_Plus‌ورزش@SportFarsجهان@FarsNewsIntعکس@FarsImagesپیام‌رسان‌ها@Farsnaاینستاگرامinstagram.com/fars_newsتوییترtwitter.com/FarsNews_Agency</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-07 17:50:05</div>
<hr>

<div class="tg-post" id="msg-445328">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e027d9d098.mp4?token=lT0J-K5d_LykZwmdb5t_Sk1Xz782VfN2gFXNOSdeKymli1SrIkCtWZQydwsao2LhWXDku-0_Ix7UFOjRxTnwPwYDXdXt55Tedazv3nNMu_9L05LLFOrB7_eFBU25NuZU_IwdWXAdIptPqCiU5Hshl9McL6fP1B6-WisJy3X72en1OaZ7SiNVSQ1teFJSyLL950QyPPRa3hnGabznmpuDStHjS3y5HdAQhGG7NTLl-a4HPIDeqN2N36bimO9xa2PL-L_S-28B0MX_KHEQ3CFwGqFDY5S-KSAghMhPN8TlmTCFCdlFeRHiTX6wS89gbB0uDMPKgBT4cP-UvpnBmkxOuw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e027d9d098.mp4?token=lT0J-K5d_LykZwmdb5t_Sk1Xz782VfN2gFXNOSdeKymli1SrIkCtWZQydwsao2LhWXDku-0_Ix7UFOjRxTnwPwYDXdXt55Tedazv3nNMu_9L05LLFOrB7_eFBU25NuZU_IwdWXAdIptPqCiU5Hshl9McL6fP1B6-WisJy3X72en1OaZ7SiNVSQ1teFJSyLL950QyPPRa3hnGabznmpuDStHjS3y5HdAQhGG7NTLl-a4HPIDeqN2N36bimO9xa2PL-L_S-28B0MX_KHEQ3CFwGqFDY5S-KSAghMhPN8TlmTCFCdlFeRHiTX6wS89gbB0uDMPKgBT4cP-UvpnBmkxOuw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">والیبال ایران از سد کوبا گذشت
🏐
ایران ۳ - ۱ کوبا
🇨🇺
۲۲| ۲۱| ۲۵|۲۸
🇮🇷
۲۵|۲۵|۲۰|۳۰
@Farsna</div>
<div class="tg-footer">👁️ 3.79K · <a href="https://t.me/farsna/445328" target="_blank">📅 17:24 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445327">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OIP9wtV5IzAGRx08owtqQsSdcwhbRQmYt4QNl4yQC8gBsv3bPcOaMVzvNapQV8I9hULcTBJGUs-2t77tY7ubgAXhXjWgeWnlP8JmkBC1qStOeeu1_c2x3LimYRNKXxfn4zPpM5bhpXvJ4TwCxde1ztqFLnhcLWqifbWhtRvzKcinFRjvkA1Prxd2r1XZCbDmbT7nnwfJD55pfZ8OxTjLyDLUjc0Dyl4-E5FQn58772FS9B9gdUjITrJe6euhW9EtA3hqqo0VY6pjKw3PfU4LhXG7t1ElUvo2eHH-nS3DI5JI8-eIyqV6F-TbvQVD-7-us9guyuhJhuCHaRvZEPFO3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قالیباف: با جدیت پیگیر خاتمۀ جنگ در لبنان هستیم
🔹
رئیس‌مجلس در تماس تلفنی با همتای لبنانی: در گفت‌وگوهای هفتۀ گذشته در سوئیس یکی از مهم‌ترین موضوعات بحث پایان جنگ در لبنان و حاکمیت و تمامیت ارضی این کشور بود.
🔹
این مسئله جزء مهمی از بند اول تفاهم‌نامۀ اسلام‌آباد بین ایران و آمریکاست که در گفت‌وگوهای سوئیس، پس از اشارۀ جدی هیئت مذاکره‌کنندۀ ایران به موارد نقض این ماده، مقرر شد یک واحد کنترل منازعه بین ایران، آمریکا و لبنان تشکیل شود و این واحد روند اجرای این ماده در لبنان را پیگیری کند.
🔹
هدف ما خاتمۀ جنگ در لبنان، بازگشت آوارگان به خانه و کاشانۀ خود و رفع اشغالگری و خروج رژیم صهیونیستی از سرزمین لبنان است و با جدیت پیگیر این موضوع هستیم.
🔹
رئیس‌مجلس لبنان: آنچه شما در سوئیس پیگیری کردید در جهت منافع مردم لبنان است، اما دشمن صهیونیستی تلاش می‌کند موضوع اعادۀ حاکمیت و تمامیت ارضی لبنان در چارچوب تفاهم اسلام‌آباد را از طریق دیگری دور بزند.
🔹
تفاهم واشنگتن بین لبنان و رژیم صهیونیستی یک توطئه و فتنه است و امام علی(ع) می‌فرمایند فتنه بدتر از قتل است.
@Farsna</div>
<div class="tg-footer">👁️ 6.32K · <a href="https://t.me/farsna/445327" target="_blank">📅 17:00 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445325">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ze2O0r52KEJ7-IYv-MDOPVDldUFZOddeEXyMnqT8PrrHBXRwlzQzj7LutRTyfKw-QkkyjUrhyM09BS7VHY2YjtTLsIYr7tGr6SyrN-YmRVVRQ-OODw-3s3IPPXLu7VREL_9k1K4t3ZqjMqmKEth4QT3aAYpvvp6VyxBdhikSQhHu3gGyYJ5u_r6Yd6ARaCz16qfdKgyCT4oF6E1L3aZ16lw0j8DJTzcBwQr3WfgozjymZX_mbzkRXm2xKnA9fLfPuURxy4j8mVrsim70RJ-I134LfDyinle2lmNbvcxKelcqx9t3lFAOfQyElWceab3jHzUQkcH31P_ncdiGTgF8NA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
ولایتی: حزب‌الله ستون خیمه و حافظ حقیقی موجودیت لبنان است
🔹
پس از سالها تجربه دیپلماسی میگویم :«آزادی بدون استقلال سیاسی،قفس طلایی است»؛حزب الله ستون خیمه و حافظ حقیقی موجودیت و استقلال لبنان است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.44K · <a href="https://t.me/farsna/445325" target="_blank">📅 16:48 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445324">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/11900a29b4.mp4?token=cDXebAG_HhvDdeuNKwKRRviRIEpLt93WaiIBZSyi5zHNxd9SrPNE6NwZgzp7N-p8xdL97GfDC0Sz0nVf21sDqMU5mTraWM57PX72ZREP_LeXXHP40WKbulYKZWwIjAXeD8zxsICvKci4LnX1X0lLyhbpw9WpU2O8kODTn5I00NRcrhG8QPVvKomRI2tGBaB_2TyqXt9NefV2PhAM5ACl_a1-rNe7_PknHULuQK1M1T23tMy29TQZ0YHdJsqFSnkZpNiCOeKbfxmQvru2KZ9Xd6oKV_uCCVUoo67wU_wSy9321LPKzidKMEEgG9CEouxVsoq60B_tYNb0DTehPs3OuwUyIGzOCBhJoL_G_LwmxK6SFqAnd-JbogyZi0q2uWUFir9GmIJeTa7BryiUqV0JGq902MTJlHSZGuwKM4fIMOpuOzuJoZaSln9wRsYrqUvv1Fzn8rv_Qk4UXlHHjEtd_nwmUu_kOolEZrq11jisx3Tb3BbfoR_uEL6-w1mElUVZVOymHKOPDllCbRZTvVj03gA46CpjomaAYBfZW7dn54oaGIhuksR8p_77LNme6tQC8EFVNU1rmzJl05VNcRQQXEaGWxo-_MkDnSmy7b46NcL7MYJ3owj49yvT-JKTBzI9qira4K4FtIBraEcLyCI66BRhVyrbE6JoEMdmweIxjz8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/11900a29b4.mp4?token=cDXebAG_HhvDdeuNKwKRRviRIEpLt93WaiIBZSyi5zHNxd9SrPNE6NwZgzp7N-p8xdL97GfDC0Sz0nVf21sDqMU5mTraWM57PX72ZREP_LeXXHP40WKbulYKZWwIjAXeD8zxsICvKci4LnX1X0lLyhbpw9WpU2O8kODTn5I00NRcrhG8QPVvKomRI2tGBaB_2TyqXt9NefV2PhAM5ACl_a1-rNe7_PknHULuQK1M1T23tMy29TQZ0YHdJsqFSnkZpNiCOeKbfxmQvru2KZ9Xd6oKV_uCCVUoo67wU_wSy9321LPKzidKMEEgG9CEouxVsoq60B_tYNb0DTehPs3OuwUyIGzOCBhJoL_G_LwmxK6SFqAnd-JbogyZi0q2uWUFir9GmIJeTa7BryiUqV0JGq902MTJlHSZGuwKM4fIMOpuOzuJoZaSln9wRsYrqUvv1Fzn8rv_Qk4UXlHHjEtd_nwmUu_kOolEZrq11jisx3Tb3BbfoR_uEL6-w1mElUVZVOymHKOPDllCbRZTvVj03gA46CpjomaAYBfZW7dn54oaGIhuksR8p_77LNme6tQC8EFVNU1rmzJl05VNcRQQXEaGWxo-_MkDnSmy7b46NcL7MYJ3owj49yvT-JKTBzI9qira4K4FtIBraEcLyCI66BRhVyrbE6JoEMdmweIxjz8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
کولر را با این چند کار ساده سرویس کنید
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.59K · <a href="https://t.me/farsna/445324" target="_blank">📅 16:41 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445323">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ubMFCGKlK_RcixnEPUEKIrj2Ic1wunT1ooGRnV1UBTmRG1d9jyyfT9bKpJzj52-iftYj5eKwxlyReYC_roKfXWkMmugAsjDcbmQBYG67t5wPigh0ADShBut3VklTdJdvyZrL2WvUrQw0j2L-pxK3iY6SK7BhZLXRyaww4xT8TvVnLLOjHwmugVyfkX0glQcZpp2t4flC4znUyrRmQmMgNyXjvqMKmGlPZTJbNNlm9n6y1d6iK6OWihCzWy8UHvZV8Pl9XJJh_IefPPagq_HinZKXhXXRNehYlkEdA4o-0kxLg0iVg6t24UjnNL20z3F8Bl3jlHX4OgEADe3eCkbQSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیدار پزشکیان با خانوادهٔ شهیدان خطیب و موسوی
🔹
رئیس‌جمهور در ادامهٔ برنامه‌های سفر خود به قم، با حضور در منزل خانواده‌های شهید حجت‌الاسلام خطیب، وزیر شهید اطلاعات دولت چهاردهم و شهید امیر موسوی، رئیس فقید ستادکل نیروهای مسلح، دیدار کرد. @Farsna - Link</div>
<div class="tg-footer">👁️ 7.88K · <a href="https://t.me/farsna/445323" target="_blank">📅 16:20 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445322">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TyzfQ8xMwhb47ATcR4pb8Nklt9cxwJT0yUvZ8F5BijXLDkEmyfP1ePqhWbqUIa7rmOBok0ZC1p1OUH-82SmlKYz_27Kr4_Yu1gmNfDtIqJTpenGVde_H75A_4_WH_dQcLZVqVh0qlMmmL86SLfgZTeiMl5m10AkMauAUlqkGr7wGeAJOcgl5Yac61MIraVQzhkh-JlxWYUWfJYBrHBl559Yhbc7XWC7itTvA8He0npAY51UutVskxXal9Zb_DQtrM8tAD50cOt0zEnQThCVhGBjRDiKlyd4729Cxte7WgvmaT4CKFb-laHsgb4KA5i2nnNlbVlG7KQsR9Z_n2w364Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سقوط بالگرد در عربستان با ۱۴ کشته
🔹
براساس اعلام وزارت انرژی عربستان یک بالگرد متعلق به آرامکو در منطقهٔ رأس تنوره سقوط کرده و تمام ۱۴ سرنشین آن جان خود را از دست داده‌اند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.62K · <a href="https://t.me/farsna/445322" target="_blank">📅 16:00 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445321">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f69df37528.mp4?token=L2SaAsJz2kzNSl6BXEWL78d9dUfcrxAobcvdfqh9hHvSbdNC5IXMPbSNwF-p_4Rvh2M9T2mpaQLwjhG-WqpTGympGl0TurkQkuBHx05BSIXZSQHKLg3MQ6dL0J7BFurtuuH9mJ1jqQcC0x9BkM5UC_5aMBJZrFmMNnV4XM73KCDY3X1K6Juc7wGX68JB0rvKfStg5O7N5_jDQtBxjEIbO6dJa04ZOTgTJplmhNqDxG3QmCdmFabjxDAlj53ATZEpdvJy3EPRD-tOBNLvL7IV3Jguj4EkYQaAmGHZojm0Z6fuUfEYipnCpKBC9pPfWgBT67uPeH7mlfbiezgineAKBg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f69df37528.mp4?token=L2SaAsJz2kzNSl6BXEWL78d9dUfcrxAobcvdfqh9hHvSbdNC5IXMPbSNwF-p_4Rvh2M9T2mpaQLwjhG-WqpTGympGl0TurkQkuBHx05BSIXZSQHKLg3MQ6dL0J7BFurtuuH9mJ1jqQcC0x9BkM5UC_5aMBJZrFmMNnV4XM73KCDY3X1K6Juc7wGX68JB0rvKfStg5O7N5_jDQtBxjEIbO6dJa04ZOTgTJplmhNqDxG3QmCdmFabjxDAlj53ATZEpdvJy3EPRD-tOBNLvL7IV3Jguj4EkYQaAmGHZojm0Z6fuUfEYipnCpKBC9pPfWgBT67uPeH7mlfbiezgineAKBg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
چطور از گرمازدگی در تجمعات جلوگیری کنیم؟
@Farsna</div>
<div class="tg-footer">👁️ 8.35K · <a href="https://t.me/farsna/445321" target="_blank">📅 15:57 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445320">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">انفجار بمب‌های عمل‌نکرده در محدودهٔ فرودگاه شیراز به‌مدت یک هفته
🔹
ارتش فارس: عملیات خنثی‌سازی بمب‌های عمل‌نکرده در محدودهٔ فرودگاه شیراز از امروز به‌مدت یک هفته اجرا می‌شود؛ احتمال شنیدن صدای ناشی از این انفجارها وجود دارد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.54K · <a href="https://t.me/farsna/445320" target="_blank">📅 15:35 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445319">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vrHfFwRQQYrkxN1s5sXRpn9hJBz9e0K6Azw0YjLCZo6zxT0xYqF0-me2P-zphy_E3x3DTwOk_7Eji_jhul-3aeO3fCAqVnza1ko5SZ7j1SWrp-dHVyUOa19mVs0rjIr9ZGlwwDPc8QdMVCvcr_ukMoGhHk9dMqlE3FWnkXopcnnjUgLeFwuHyd1Lc38g4-Be9OQ31oMK7YUj5PeEA_g2RvVTbX53Y0dYKk5-Mga_gtNgMJyRqsCuqbNKsTlTCRKnYEtfvqKKt61mH65xmEFLkF9hg1paMk-jmNIWV-zUSjOVVADnnUFfuQNhsxqsRFyB2CILqjz5UGl_bGtnkrqhZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فروش سامانه‌های دفاعی پیشرفتهٔ اسرائیلی به قطر و عربستان
🔹
بنا بر ادعای رسانه‌های صهیونیستی، شرکت‌های اسرائیلی «البیت سیستمز» و «صنایع هوافضای اسرائیل» (IAI) سامانه‌های دفاع موشکی و قطعات مورد نیاز جنگنده‌های پیشرفته به ارزش صدها میلیون شِکِل را به عربستان سعودی و قطر فروخته‌اند.
🔹
به گفتهٔ روزنامهٔ هاآرتص، اسرائیل با وجود نداشتن روابط دیپلماتیک رسمی با کشورهای قطر و عربستان، روابطی از جمله صادرات سامانه‌های پدافند موشکی و کلاه‌های رزمی برای جنگنده‌های پیشرفتهٔ اف‑۱۵ را در پشت پرده با دوحه و ریاض پیگیری می‌کند.
🔹
این روزنامه مدعی شده که قطر برای حفاظت از جان مقامات ارشد خود نیز به سامانه‌های شرکت‌های اسرائیلی از جمله سامانه‌های شرکت «البیت سیستمز» (Elbit Systems) مجهز شده است.
🔗
شرح کامل این گزارش را
اینجا
بخوانید.
@FarsNewsInt</div>
<div class="tg-footer">👁️ 9.97K · <a href="https://t.me/farsna/445319" target="_blank">📅 15:20 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445318">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b3f04c60bf.mp4?token=ozxIbzCmHw2pxTqNwl8MOVApbagmqInDre1RvUDqlvRB9jifn-y9hLvR6ZrK8fxsw7V4SZ-J-KPWS_UzFxfrl43t48eZvfHrAk7ipoeqqn2-ry-HhiJRT9W8hMmD9uPNFRlYS2dXhFfXzxlSVoOFO7vD-__eXE3vhgxCW-9oGcQF06NKAN0_faHivcopuPTw5AbWC9N1QLDWHlZThhex6rKjqZtUmGCCu65_bkbhJpTOJ74ZV_TpAzTmZezoIDMXOyho2HaHT0m5tNSsanQBXOnbc0NhzCNod1q8HqJV1ljBALHT0AqgoNlJGt0BDONrHCLgDL9A3pQ5KP2Ge9dNSg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b3f04c60bf.mp4?token=ozxIbzCmHw2pxTqNwl8MOVApbagmqInDre1RvUDqlvRB9jifn-y9hLvR6ZrK8fxsw7V4SZ-J-KPWS_UzFxfrl43t48eZvfHrAk7ipoeqqn2-ry-HhiJRT9W8hMmD9uPNFRlYS2dXhFfXzxlSVoOFO7vD-__eXE3vhgxCW-9oGcQF06NKAN0_faHivcopuPTw5AbWC9N1QLDWHlZThhex6rKjqZtUmGCCu65_bkbhJpTOJ74ZV_TpAzTmZezoIDMXOyho2HaHT0m5tNSsanQBXOnbc0NhzCNod1q8HqJV1ljBALHT0AqgoNlJGt0BDONrHCLgDL9A3pQ5KP2Ge9dNSg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
گِل‌فشان‌ بندر تنگ کنارک سیستان‌وبلوچستان فوران کرد
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.52K · <a href="https://t.me/farsna/445318" target="_blank">📅 15:10 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445317">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iXKwjihBdQUmMLcl96Sn1CfLZDjWmGJ_XGXLwbSn-XQjyF-7h82HqrpbITIxxLBuondnXeMpeg_mwuJMRlPpkxhySqvkXzLlIdF-gX1zwe7-3WInJkZUzdQby3D6ttUUTNQMVYz6h0kmpmGDINEJ_77G80F03JemNU5fPpnEh-euH2IwBIkxEeHJJi2Iw9hYyyxYCECLt2faCy1wAJQNdhazIq-CPDqZRUPLNXP9yCtSca3qfvFIUOA-Kvg03HqBRcWnBkTXrtqGWcYxff5nJ6JaY7wqjtqPqgp0fBk1r5WHR8pUMbLfyNL4uetXA61KZcqh1ZGuDgN7Ixf7fiBJPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
میثاقی: اوسمار بعد از بازی دیشب اخراج شد و پرسپولیس با اسکوچیچ بسته است
🔹
مدیرعامل پرسپولیس وعده داده بود که اگر پرسپولیس قهرمان نشود کل حقوق و مزایای ۳ سال گذشته‌اش را پس بدهد. @Farsna</div>
<div class="tg-footer">👁️ 9.77K · <a href="https://t.me/farsna/445317" target="_blank">📅 15:05 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445316">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BYuTNO1Z6GWNanHc79xueWcF6orpEKE9ckADqHGijHOyXoomwtc_fWlTxYWZOVtoRpcq_aiPJn781rt2uGEU5JAZIvn_K5OL3FnJcRo-rtYASM6lts4HBgM_0UYoiOVRHdMDSaOJjKCEAdNtOdIkmD9uorOaDd6W86kSFDuaMI0QSiqrxn1vIj0JjAoORgl-W99DElx035WhrPsliFFx21OrWmuhPCQJWDabz9p8O_BtuDMccMHrbIaBhyr5EJHEaF9BoUfxx6Jwqk1SBIjHjPtWpxXhnpCCEnMNpMx7gQruynivEjt-llZytBTMDzaxX3Li0DDp230A-w7wTm92HA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تردد خودروهای پلاک مناطق آزاد کیش و قشم در هرمزگان به‌صورت رسمی آغاز شد
.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.05K · <a href="https://t.me/farsna/445316" target="_blank">📅 14:59 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445313">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Mk5xRHms8gAncvdlZqHAFWVh_oIQUq_9C0p2EzL0R0w4jgw4ObvZ3sBRXf_8cKSQnv7z5Y7HNzA0svM-E7qfR2uEmIK0O8Z7Jz_pjJde1gbcUbN64vxr6XkAC0LZQek-x1nQyd0HiZutvCq_0-tTjFnOj1EweOWb-CEW69JoIvB86E6UEVziYgIB3eq-K9l5OlpHlWJ4c4jipTmwLPDa02OkFPeNzvYI1TLeizAXV9Kh4VGdhLxHiMLbeTyDy8zfiydkFb6rcyjqvSgEo4Y9IozcJmwzVRNXhZ9y25n9vnb765hKYz78ZM2Ovc7Fc1Fp2LjOcpHhbYgtQ9Y-s7-eHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jD3gJTh0rZfF0O3T3L-icumzQFt1ul11Q8FZr3GL131KvKA3uFfwQi8YYkF9VY354XaZ9ko4-4xV-amFu2poq5oSELbNGQw1mBuDPh4nO1-JTmbZgA42QVQXqd5AC-DnV43yHkRW924fQg_gnvucKzvyewgkgLmZy9Pi1m6u0HESzOV8FkjmncN-z3F39xoSsH6diyiAKvav9pEhB2u2dbvehTvmojx0wXqhaiMub_Aytv-HFAB7y3_cVDMEWwFST9lNYs0vZtonVAJrhVA_j7i4wbnveG5h3ti1UkiTVLgNiVlO8xqo0EWctQthXZG43neeYMBR2BGK7aJ2CUw-qA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/S5HH5nt7dASqYF3v5fGSimBVaOK5I6PwIDM3NlEI9Wtsg_jzV2orNbS_EeAWdCVFfrJYt0mOMw2rGzqm8SlLUYCljOhLEeH9HlciSVHJx79H-ee5fLIF3OlqhM3dWTrSoh3R-kJIbR5kc69KeY2crk9icA1rsL-n7wUN_BXM9S9zifVWvYzH4Vw17Ms0YeyfolkbHn1H9OIjOQVntANHq2XxYS-esGOnqTpMo3zjXj3UPPe8VcjlmgJdOMGW8Z3tOc9SB7R1kSXb2jwGerupKm4v7RhzSa94vNR1Fmit-4RIcCctLiq1u21zq4hxU1IMvMXWUut6J8fNQFOydahc8Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
عراقچی در بغداد با رئیس‌جمهور عراق دیدار و گفت‌وگو کرد  @Farsna</div>
<div class="tg-footer">👁️ 9.43K · <a href="https://t.me/farsna/445313" target="_blank">📅 14:50 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445309">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DQlfKdAO61ndZYkyxkgneVkZ569mXM3I6oRXVy3r9r9iIwxeKqHP4MOLGt33fjWlRFRe0XNTktzdGPbJtvXA98tqROs4Il-mprgeLHFtHZVUNjIaZ42xC7LILKaHoUQnfDuTCJQ2kziB6-5svfMLvHzFfE2yJWdTUhdoDXzHIq8eB4Gqq45ecMw70DoZKzzP0_XoSaLFezpvDPwa-7b8GeS8k-2lwQ4ejXy_TlKaZIr2kDtkRFf6DQgqvn8rJktVBVLT6xsacV6mDtDsxSjaSQ7bvPeKEy1KiLtudpNFnv5MlrvU02rTKOIqtDNsZ8xx5CJhBXS7tV-JcDHvfqd5FA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RBvVA5CXAREeuo_ptXBhNLCsEhp3ypQT6cA7GLAx5e-_K9CRcShnn_5e-DqR7F9r5GkXTfT27pv1C9uu1UzxNiKKUTgBipues_IZfG2g8j5Dlc-oXY-XLCiTVXfnxkareobERqYgAzv0BtRda1i90wvSEOqc8J2QsojludzpCJNubM3RijdHx1xD5pYAV5dyRR_MiqMU3LOi66Ww2IVasOx2OGV-t-2gRjJEjdhzegex2q2gkYS7YcsYfsgcPhUwJ5nCXCKGtJOKr5hR764DLYBFFvv3UlSIeDx4u5o3288piqLjn4Px2Teo9n74ddYLpFpxTlzhiRS-p9xA9fVdDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LbqlZgUM6EZ2nEQjF8mbhToNRjeXhRr1_EFQs76HbtTWcX4HMHBM7BRHgfbl85JwxherCR3hmKppg26tr9I-LlO3gYGGHjKerMZKmMmenRVF2A3yP2ttNKAN5mTwQLheYf7SXx7BHg6n-sH4JhZ1GdhRoMY00jbTh5v-Q1Mcj0wpmPHkuXDryUfWTEYLL1ufm9ZA2ResDS_0PEQpG86XNKqUA0K2icja2-X6penpR3Ha8QjXPzgGGr89L-l1Up3Nh1eXyKWwspdUVLgMCuYKvVJKgDYC3jHSg3Ak7DJRT96ufh6O4KMwvTwGMFpyV_RH6pnukZhLqYgJEHpN32K0wQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lLa9VyCnF8XOwsb_h3UbAKWRQilFvJq-7LxZoXsUhfw4lhw8GhzzcT9w85RYbwgFBVg1z4Re2-r1Ok7p43eyIE0F-BPUtNd4vMniCYPGPJJW3ET2tUwcHCZWxJwVwt03kJ3ly085qabQuoWftc1hKPxVFRMJ4Ma-2_DGCF73phKv2kCKJ1zJdpyfKZZU2isMhSD9_d131OKaHYW2BHJrs_vxtyR5itRgOxL1sMJq9ENNzfgYppLa6ARzCWXklBw-ddoVqxhmqaXJ06jfwfS6mYaBEPu_WbSkyyCEK5ImFT9nPfSjAnTlSgxysJS0RKlHy22QQPXB1OreaMTbLj2i5A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🎥
عراقچی: از پیشنهاد وزیر خارجهٔ عراق برای تشکیل چهارچوب ۲+۶ برای تأمین امنیت خلیج فارس استقبال می‌کنیم
🔹
براساس بند یک تفاهم جنگ در لبنان باید تمام شود؛ مسئولیت حملات رژیم صهیونیستی و عقب‌نشینی از مناطق اشغال‌شدهٔ لبنان با آمریکاست.
🔹
امنیت خلیج فارس باید…</div>
<div class="tg-footer">👁️ 9.36K · <a href="https://t.me/farsna/445309" target="_blank">📅 14:47 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445308">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k7JBQGWhT4XmZVgTztsYf2cCx5oEChJRZbGVulHRDfIjKaafLZe23mUM6npJZZs1O59ucXrMjGcdx6cOe9_F3U7M_M145oThwMXx-PbCfDEu_I6lnKLcDX72nONVc9AZhwQGsEnHaSjcAv5S0-2N-Ufdqxczn-868Ak66trr-yv4yn05nFEHxoe3d_hh95FHIZCy_Nt_1bWKGcMyJAk5oenuoPOr-Pf5TF4HY0gU41zKy6EbGiT9AbA32q652KYofSH6i8wBKegUQokjfmB8nhFRaGRVQ866dNMMsvZRPcB7Jd9YtLT7CjnMrlc6lzJExLWSR9YIYHqZtDKd7R_v2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توقیف تمام اموال ساعدی‌نیا در نوشهر
🔹
دادگستری نوشهر: اموال ساعدی‌نیا در نوشهر به‌دلیل اتهام حمایت از اغتشاشات و ارتباط با جریان‌های معاند، با حکم قضایی توقیف و برخی دارایی‌های او از جمله یک کافه در شهر پلمب شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/farsna/445308" target="_blank">📅 14:36 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445307">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">لیگ برتر ۱۸ تیمی شد
🔹
در جلسۀ امروز هیئت‌رئیسۀ فدراسیون فوتبال تصمیم گرفته شد با نیمه‌تمام اعلام‌کردن لیگ برتر و عدم معرفی قهرمان این فصل، سال آینده مسابقات به‌صورت ۱۸ تیمی برگزار شود.
🔹
دو تیم نخست لیگ دسته اول به‌صورت مستقیم راهی لیگ برتر خواهند شد و تیم…</div>
<div class="tg-footer">👁️ 9.65K · <a href="https://t.me/farsna/445307" target="_blank">📅 14:30 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445306">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AeqIH2PEZDu4znEBhQmtdF5w-vZ6fUmt_x7qHDw_c5VcsBIlvZcDFl4xxdS7HLBGd43Xmb1CQoogElDx62mvHUbVqF5ZyEpej97X9-wDAc1_xfGp5xOxaeO3imYn7LhLNMx2vDYIPhIapMhOShh1LpOmrSs9mbCU9qNEYYdDWsIxvsOOpTQFqJ7Q7GN8HsqunjUJlgj2w0mnEsm78xvsi04QaIDizauwB_fJsZ8UJR_t0EMJadwdLmVPB7oE98Qk26kbT5bW5OoQnn9DO4u9p_eWd1u8yvBUxrGGphJ4amh6K43rlqFnUioAuS9NHt9CTA6mSWSXR5F95oaVkHi9Ww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آیت‌الله مکارم‌شیرازی در دیدار پزشکیان: نزدیکی بیشتر دولت و رهبری باعث آرامش مردم می‌شود
🔹
هرگونه سستی موجب جسورترشدن دشمن می‌شود و هر اندازه اقتدار بیشتری از سوی مسئولان نشان داده شود، دشمنان ضعیف‌تر خواهند شد.
🔹
مردم با وجود دشواری‌های فراوان، ایستادگی کم‌نظیری…</div>
<div class="tg-footer">👁️ 9.18K · <a href="https://t.me/farsna/445306" target="_blank">📅 14:30 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445305">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">‌
🔴
رهبر انقلاب: در قوّه‌ٔقضائیه باید اجرای عدالت به پایه‌ای برسد که هر مظلومی آن را مأمن خود بداند و به‌خصوص کسانی که به‌نوعی از قدرتی برخوردارند، جرأت تعدّی به حقوق دیگران را نداشته باشند و باب سفارش و توصیه در آن به‌طور کلّی مسدود شود و داشتن آشنا در بخش‌هایی…</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/farsna/445305" target="_blank">📅 14:11 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445304">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">‌
🔴
رهبر انقلاب: قوه‌قضائیه جایگاهی کم‌نظیر و بلکه بی‌بدیل برای اصلاح روند امور و به حرکت درآوردن سایر بخش‌های نظام دارد که این مستلزم پیگیری روند اصلاح و بازسازی در داخل خود این قوّه نیز می‌باشد. @Farsna</div>
<div class="tg-footer">👁️ 9.61K · <a href="https://t.me/farsna/445304" target="_blank">📅 14:10 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445303">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">‌
🔴
رهبر انقلاب: قوه‌قضائیه جایگاهی کم‌نظیر و بلکه بی‌بدیل برای اصلاح روند امور و به حرکت درآوردن سایر بخش‌های نظام دارد که این مستلزم پیگیری روند اصلاح و بازسازی در داخل خود این قوّه نیز می‌باشد. @Farsna</div>
<div class="tg-footer">👁️ 9.25K · <a href="https://t.me/farsna/445303" target="_blank">📅 14:10 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445302">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">‌ متن کامل پیام رهبر انقلاب به‌مناسبت هفته قوّه قضائیه و سالگرد شهادت آیت‌الله بهشتی و یارانش  بسم‌الله الرّحمن الرّحیم
🔹
ایّام مصیبت آلُ‌الله و شهادت حضرت ثارالله صلوات‌الله‌وسلامه‌علیه‌وعلیهم‌اجمعین و یاران باوفایشان را به همه‌‌ی ملّت ایران و امّت اسلامی…</div>
<div class="tg-footer">👁️ 9.02K · <a href="https://t.me/farsna/445302" target="_blank">📅 14:08 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445301">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🔴
تا دقایقی دیگر پیام رهبر انقلاب به‌مناسبت هفتهٔ قوه‌قضائیه و سالگرد شهادت آیت‌الله بهشتی و یارانش منتشر خواهد شد.  @Farsna</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/farsna/445301" target="_blank">📅 14:02 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445300">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">مرکز مدیریت حوزه‌های علمیه: در صورت نقض تفاهم باید به دشمن جواب دندان‌شکن دهیم
🔹
مرکز مدیریت حوزه‌های علمیه در بیانیه‌ای با اشاره به پیام رهبر معظم انقلاب دربارۀ یادداشت تفاهم رئیس‌جمهوران ایران و آمریکا، بر لزوم صیانت از حقوق ملت ایران، هوشیاری در برابر بدعهدی طرف مقابل و حمایت از تیم دیپلماسی در چارچوب تحقق کامل مفاد تفاهم تأکید کرد.
در بخشی از این بیانیه آمده است:
🔸
بر رئیس‌جمهور، اعضای شورای‌عالی امنیت ملی و مسئولان دیپلماسی کشور شرعاً، عقلاً و قانوناً لازم است در صورت هرگونه نقض عهد دشمن و عدم پایبندی به بندهای یادداشت تفاهم، به‌سرعت و قاطعانه از مذاکره خارج شده و پاسخ دندان‌شکنی در عرصه نظامی و دیپلماسی بدهند.
🔸
بر همۀ مردم بزرگ و مبعوث و انقلابی ایران لازم است ضمن حمایت از مسئولان در میدان دیپلماسی، تحقق بندهای یادداشت تفاهم را مطالبه و بر رفتار و گفتار مسئولان نظارت کنند.
🔗
متن کامل بیانیه را
اینجا
بخوانید
@Farsna</div>
<div class="tg-footer">👁️ 9.3K · <a href="https://t.me/farsna/445300" target="_blank">📅 14:02 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445299">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🔴
تا دقایقی دیگر پیام رهبر انقلاب به‌مناسبت هفتهٔ قوه‌قضائیه و سالگرد شهادت آیت‌الله بهشتی و یارانش منتشر خواهد شد.
@Farsna</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/farsna/445299" target="_blank">📅 13:42 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445298">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qDR9DfjcKHXMkZ94M6wVSe_ZB5s3OBWy56x2E_xXpkmElo7tW5Lt4JB4V2rb3PQJi5ROYduqNVValsXpfRgGq9OWkY8Rx5AXtcIKtuYO2kYybCWaxlgThGR-Z8rQAq_laSxrHygIUGH-RCUZUkI_N2Dl1VrM3t0OXpi7etm6B7rXi-k9_LLIhP-HqEQWJNia36ktxoF1HPVaMiVoV_jsRx9NsxBi2on9ZYOnACPoNQpKSeMMOW1Zyjdvy8k8CIOlyDJ2Fxa8xnO7Ng-WOL1fBrLSTnjEOn1f2H8-PBgJB4cuJlu4JvZxwcrKzbkbfwyQgo8Z7SsL-JEPwveZBfkCVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آیت‌الله نوری‌همدانی: رابطۀ مسئولان باید با رهبری رابطۀ امام و رهرو باشد
🔹
آیت‌الله نوری‌همدانی در دیدار با رئیس‌جمهور: معتقدم اخلاص و تدین جناب‌عالی می‌تواند در پیشبرد امور و خدمت به مردم نقش مؤثری داشته باشد و این ویژگی‌ها سرمایه ارزشمندی برای مسئولان در…</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/farsna/445298" target="_blank">📅 13:27 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445297">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7979577ff6.mp4?token=Wl1B0bYL-n1TvyzqbDXTkp1HDtDW6I6PrOutdR-MWNzLa616HMRPbRdi2DkgO2aya5ScFnXyQRk6bW8Ud8WUHJob8mP4rSmkxAUP5KaAivtIlK6ieHlFuJrfCvWwXAE24pTWYehe7XP6ff1dZhzTrOkOuBU4zPL4WWAy9DEbUjnXdMysb8zeN-oZMERecX3qT7uw90Y-7U3mrcHzz64pQKepF9XeUhQLdUbxWSrWs1Lq1I-qQBXAuMenakCEiFn2d8RvHx3gvM7JHpl-L9mAgUoowqeLYkxr-_30PBbkgAketzUB3H5-BeTCrf-mgZeWYmD-tZEH0mImgzIidcPEeA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7979577ff6.mp4?token=Wl1B0bYL-n1TvyzqbDXTkp1HDtDW6I6PrOutdR-MWNzLa616HMRPbRdi2DkgO2aya5ScFnXyQRk6bW8Ud8WUHJob8mP4rSmkxAUP5KaAivtIlK6ieHlFuJrfCvWwXAE24pTWYehe7XP6ff1dZhzTrOkOuBU4zPL4WWAy9DEbUjnXdMysb8zeN-oZMERecX3qT7uw90Y-7U3mrcHzz64pQKepF9XeUhQLdUbxWSrWs1Lq1I-qQBXAuMenakCEiFn2d8RvHx3gvM7JHpl-L9mAgUoowqeLYkxr-_30PBbkgAketzUB3H5-BeTCrf-mgZeWYmD-tZEH0mImgzIidcPEeA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
وقوع انفجار در تل آویو
🔹
منابع خبری گزارش دادند یک خودرو در منطقه «حولون» در تل آویو منفجر شده است.
🔹
منابع صهیونیستی اذعان کردند در این انفجار ، یک اسرائیلی به هلاکت رسیده است.
@FarsNewsInt
-
Link</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/farsna/445297" target="_blank">📅 13:10 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445295">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/u7DmUQMcy2cD9gdGLvfbHKvHUkVDDXFkTPOPmvRamqt9hg5XiXJ0Riu4kahEDOzVQ-VeOZ40yiaaDKV-NuN4fTDxtiBsATpBCeAi4C-9Q4TQhtz-f1QlLPUGh6WLO4ZIGhXrjIY2cYKeGyHXIE9X8Log44bcVcQpnV8iuI_pHLxN9D7Tlvg-1zq9fSfg7Qmwe1-NhXK1ZSMHp3JvPxFW5diRUuMMirZ4xGG4FjNfHraO3nbILX4wo7E6eu0Kyc7Mg0BYsgiuAt5OT1pGGQeeg8sfP3J9xkQ3c8ttOTxx0moWHhH3V2baJNX9NzD0xwVQdF6lsOJu1Ez2zjkhnd2pUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Psce35DB2czUDyhy5TIEt87RP1rlFWBRXoQJpJ3jYvLLw73QB9djrscfDLcKxA_80KR3pOYNrdcsNp42xkNrATU06_C4SwgQJdf1nwYc7_6Jm2OpcYU4RXuZihVhxGaMaYl_bNHjaTxjwQMqyrjBuiD1wMuBFe8eq-j1nUn1k9fOI2WqAYHvCNKqQQgbORlZivFp5QWwIMdHAO_OzfgNeekrL1qFLYhqxGVA7aG3AmUYMyF3X7cwWDRq8S-2i0jNQN2pG2f6dGXBaId_fGbWRF7aPO_JaRCzwNaQjgE-oWgDPbKDOnpKx7ZHVssuGLnu9ffmR0MgIt50B-u-Miag2A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
پزشکیان به حرم حضرت معصومه(س) مشرف شد  @Farsna - Link</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/farsna/445295" target="_blank">📅 13:01 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445294">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CFhOWGIlgm_KDFw1faV0PyZa2CTjA5zPhwMAStXhs7gjumay7cdpoe3wkpeUMZcorjhMUMW5Xs5_25AZLlj3bMEFjYaUSre22wEkQBlqKJ33yckMaSgRFTU3ZJZqzbZjw-sDDdB4b0Oj86DMGi2zJlyhuPpma-YqR42B2YdP-ScS5KE1Ue-rFsB_1XnVrz9kzzIzQdfTZDTLpve21L6KJtZfCPmJWMS7ObrsNfrNDjaPhQY50xuw8V3fCx4YXfjImZJNxYB7huOuWztsZkuFGNjOD64L3_gGW4QA21iE5IWL5mmbtxe5vCafk7a0eue26Iv4F9OdREb4aRPca4AeDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پزشکیان: تعامل دولت و قوه قضائیه زمینه‌ساز گشایش در حل مشکلات مردم است
🔹
پیام رئیس‌جمهور به‌مناسبت هفتۀ قوه‌قضائیه: امروز بیش از هر زمان دیگری، جامعۀ ما نیازمند گسترش عدالت، تحکیم اعتماد عمومی و تقویت سرمایه اجتماعی است.
🔹
دادرسی عادلانه، حفظ حقوق شهروندان، مبارزه با فساد، دفاع از حقوق عامه، کاربست رأفت اسلامی و صیانت از آزادی‌های مشروع مردم، از مهم‌ترین پایه‌های حکمرانی مردمی و از مطالبات جدی ملت بزرگ ایران است.
🔹
در شرایطی که کشور برای عبور از چالش‌ها و دستیابی به افق‌های بلند توسعه، نیازمند درک مشترک، انسجام و همراهی در همه ارکان نظام است، تعامل سازنده و هم‌افزایی میان دولت و قوه قضائیه می‌تواند زمینه‌ساز گشایش‌های مؤثر در حل مشکلات مردم، تسهیل فعالیت‌های اقتصادی، حمایت از تولید و سرمایه‌گذاری، ارتقای امنیت حقوقی و بهبود فضای کسب‌‌وکار باشد.
@Farsna</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/farsna/445294" target="_blank">📅 12:51 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445293">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a1b966a1d4.mp4?token=Ci15QksaPFGyl-x9xdBqArPiOwZmbOeWg7Ta53F81-KJNQRD0xjFXSMpiaMBtKzYdqjr52DtWA2SzXqGK2kcK4Jjn9B_FaU-oSd_EVKg8sVl9FQsnpe4HxzPRvpQSHQfYlBNk79PchcLKEcjpvLnPZLALs6KgV8NgQ_0aKX8XEG6-Z7DWii_CnY-tsVP_Sv7w6GRjgZetcqcb4aErxMpRryN5IPmmKY7PvF4BbJyYt-bB2qXN3pMs5qbYN6h96-NCnDHJ2HcKF_x-OBGqopnlSl7nUlYGx3s_gjl0zgGotx2eJyUoxfHHxY5mUqk90cfNDmuQ3fBi_O75VwaueER9Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a1b966a1d4.mp4?token=Ci15QksaPFGyl-x9xdBqArPiOwZmbOeWg7Ta53F81-KJNQRD0xjFXSMpiaMBtKzYdqjr52DtWA2SzXqGK2kcK4Jjn9B_FaU-oSd_EVKg8sVl9FQsnpe4HxzPRvpQSHQfYlBNk79PchcLKEcjpvLnPZLALs6KgV8NgQ_0aKX8XEG6-Z7DWii_CnY-tsVP_Sv7w6GRjgZetcqcb4aErxMpRryN5IPmmKY7PvF4BbJyYt-bB2qXN3pMs5qbYN6h96-NCnDHJ2HcKF_x-OBGqopnlSl7nUlYGx3s_gjl0zgGotx2eJyUoxfHHxY5mUqk90cfNDmuQ3fBi_O75VwaueER9Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
عراقچی: در تنگهٔ هرمز دخالت نکنید و به یادداشت تفاهم پایبند باشید!
🔹
براساس یادداشت تفاهم، تنگهٔ هرمز تحت مدیریت ایران طی ۳۰ روز به ظرفیت قبل‌از جنگ برمی‌گردد؛ هیچ کشور یا نهاد دیگری دراین‌باره مسئولیتی ندارد و هر دخالت یا تلاش دیگری اوضاع را پیچیده می‌کند،…</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/farsna/445293" target="_blank">📅 12:43 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445292">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tbSrso2h2lXvi3zQQ-rCXe8zAtWm1JfgYmOgE_w6rXIakQOVxpTOnizxDC2svN3V7anqYqemJpc9M65vPqdcl8OebKmVYdhYNwuq1hXzlIlo2Frs_Fmjg9sfXXSFB637GJUkRXSlg_yC12MSnmhoJI-OBxzJ5eifndp3ErRdZN0dy1OWKdtYufVYM6VxI6OuhM37CF0k6CRq8a5Z9kCn5H_FxyEe9jj4fsHtSMrf9YymkPAzqtTH4j8lBAT2hfTKthQzpD4HiPwrhvpSQzMO1_Rrs8dJJrFYymAid3RmLfTA1cnTG8WYYB6f3wqIfDWt-Mm5TpGUFXKMCElOtFFvsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ریزش ۲ درصدی بورس
🔹
شاخص کل بورس در پایان معاملات امروز با ریزش ۱۰۱ هزار واحدی به ۵ میلیون و ۷۶ هزار واحد رسید.
@Farsna</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/farsna/445292" target="_blank">📅 12:33 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445291">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3ce21f683d.mp4?token=M7B9ZDZo7Hmfb39-Qg3-wa_3z484WHxB3bSIyED9z0J3SMAFjrynjmf6Y3hnlwn8mKZjFx4SmAtCLfrkusFFmuWc-ruXzpIZz-RF844W6nRVGXoJMyHqFnL-9gZ-muB7fXzylSyE_Ro6Z0VmYl5XS_N-onL4MJbwFrvYJ71DN5lRll4RfsP2MZCbW12ue84RVQp0ihDkVNhD8qIo1_VcP77tLrdVkLjlTKs1fobThwwaEJ8aNzmEeePLWKNhFFxPFLRZav2NH251NXIBne5waL6ysH8G8-iQu-IdiPgGSCU67o9dSIkHSTvPEnmHm7m-voWVsW804DJUIJ6BVBPNpw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3ce21f683d.mp4?token=M7B9ZDZo7Hmfb39-Qg3-wa_3z484WHxB3bSIyED9z0J3SMAFjrynjmf6Y3hnlwn8mKZjFx4SmAtCLfrkusFFmuWc-ruXzpIZz-RF844W6nRVGXoJMyHqFnL-9gZ-muB7fXzylSyE_Ro6Z0VmYl5XS_N-onL4MJbwFrvYJ71DN5lRll4RfsP2MZCbW12ue84RVQp0ihDkVNhD8qIo1_VcP77tLrdVkLjlTKs1fobThwwaEJ8aNzmEeePLWKNhFFxPFLRZav2NH251NXIBne5waL6ysH8G8-iQu-IdiPgGSCU67o9dSIkHSTvPEnmHm7m-voWVsW804DJUIJ6BVBPNpw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
عراقچی: هدف سوم من انجام هماهنگی‌های لازم برای تشییع پیکر رهبر شهید انقلاب در بغداد، کاظمین، کربلا و نجف است
🔹
با تدبیر و همکاری دولت عراق مقرر شد که تشییع پیکر رهبر شهید انقلاب در این کشور صورت بگیرد و نخست‌وزیر عراق ستادی را برای همین هدف تشکیل داد که…</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/farsna/445291" target="_blank">📅 12:30 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445290">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bc39ece711.mp4?token=iBPnBbIqJ_Jidc2mrki4TMGAWJJpHBs5_76awAW55sMPIGZPdaxjgVTnvjUy6nCJ0Lg7LjM_qX9wUiG6LqlFfRh7WwJzLul14ml3i4ByNrvVcVFGuu-0CFasokcMyHFcu33oUyun3twBT_saLuuLEnGwZ9U1GmfpMM6Mv1lOEO9eI120_MxtB9Ku9pv7OjU8jIJq3uc8Doe__VqUrlij6gXqM_O6x5VTws9KbDa7c0QRYHO1hLexAsWtu3UyD3AM1PQzb8qYicBVmDoR0CoyTR8Hh8iRTOIaRH5g4hAC2btaGlK9YGE1xYEGVC1pOf-mKmHwR8LfNFrePcNttZPI2A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bc39ece711.mp4?token=iBPnBbIqJ_Jidc2mrki4TMGAWJJpHBs5_76awAW55sMPIGZPdaxjgVTnvjUy6nCJ0Lg7LjM_qX9wUiG6LqlFfRh7WwJzLul14ml3i4ByNrvVcVFGuu-0CFasokcMyHFcu33oUyun3twBT_saLuuLEnGwZ9U1GmfpMM6Mv1lOEO9eI120_MxtB9Ku9pv7OjU8jIJq3uc8Doe__VqUrlij6gXqM_O6x5VTws9KbDa7c0QRYHO1hLexAsWtu3UyD3AM1PQzb8qYicBVmDoR0CoyTR8Hh8iRTOIaRH5g4hAC2btaGlK9YGE1xYEGVC1pOf-mKmHwR8LfNFrePcNttZPI2A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
عراقچی: هدف اول سفر من تشکر از حمایت‌های دولت و مردم عراق در جنگ تحمیلی علیه ایران است
🔹
دولت عراق مواضع بسیار خوبی در محکومیت تجاوز و حمایت از مردم ایران گرفت. همچنین ما از مردم عراق حمایت‌ها و پشتیبانی‌های بسیار زیاد و دلگرم‌کننده‌ای را دیدیم.
🔹
هدف دوم…</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/farsna/445290" target="_blank">📅 12:23 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445289">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7306e07762.mp4?token=Yos1dfKB73WFg5o4jjutpryHizir4lhlKhinzEh_qcIwpg1JvdW496Ikv864mD6P3su7FIS_mArZ2YPny4O4BeSSzgoG0UcSbHv7DyXMEnkodpbPHm1DOXnwXIVMbl5r6n4g2a_5b4Lks75Ut3L0-NufL0PhJvLUggzt-jdM25Pxvbes1Q0O5o8N7_Q6rt-tEekoWH_cMA2-xXbiI79amqqfXKvRCBOE4n8nZ9e7ZNmgONWEFpG-vjTX5gdjbImDQb9RyDhyRP-cAKV_t5fjJAhoejez5xlcQBYHiKDvJdDYg_XM7m0Sfr0y8HiW5SAZdtjQudMhJiyP0p9wgOA1FQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7306e07762.mp4?token=Yos1dfKB73WFg5o4jjutpryHizir4lhlKhinzEh_qcIwpg1JvdW496Ikv864mD6P3su7FIS_mArZ2YPny4O4BeSSzgoG0UcSbHv7DyXMEnkodpbPHm1DOXnwXIVMbl5r6n4g2a_5b4Lks75Ut3L0-NufL0PhJvLUggzt-jdM25Pxvbes1Q0O5o8N7_Q6rt-tEekoWH_cMA2-xXbiI79amqqfXKvRCBOE4n8nZ9e7ZNmgONWEFpG-vjTX5gdjbImDQb9RyDhyRP-cAKV_t5fjJAhoejez5xlcQBYHiKDvJdDYg_XM7m0Sfr0y8HiW5SAZdtjQudMhJiyP0p9wgOA1FQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📷
عراقچی در بغداد با همتای عراقی دیدار و گفت‌وگو کرد  @Farsna</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/farsna/445289" target="_blank">📅 12:18 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445288">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">ثبت‌نام خادمان مراسم وداع با رهبر شهید
🔹
شهرداری تهران با هدف تسهیل خدمت‌رسانی به شرکت‌کنندگان، راهنمایی و هدایت جمعیت، حفظ نظم عمومی و پشتیبانی از بخش‌های اجرایی مراسم تشییع پیکر رهبر شهید انقلاب، از علاقه‌مندان دعوت کرده تا در این حرکت به‌عنوان «خادمین امام شهید» مشارکت کنند.
🔹
علاقه‌مندان می‌توانند از طریق نرم‌افزار شهرزاد یا شماره‌گیری کد دستوری *۱۳۷*۳۳۳# در این حرکت شرکت کنند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/farsna/445288" target="_blank">📅 12:11 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445287">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rIQ6V00znmqGUtF_J3yNjW_ClxJSKqYaqOu0bLPHg6d5HJ18hu8sGzq8ZWlqNgnCZ8t0l36VExmQa0ahCtCfKWAlMICtXmYp3P5pDK7RmvweDG1AQEW6mmyG_TIz0E9lz7PK7TN6zKsirMOhxTXNDg4TSkES0gpEBLitUdXP42Eg-BLWWzcxu_pi6_CHpuch5VOJjznUYbwcPKIK1X3A3baaruf6Xm60TC_RdQXxxuYWlR34p0sSp6Ndrobaz5V9WFVLipYeWL_bHqSiFfZE5WdOe8g_XxZmrB0Q8maE_kZKwOu0v5OhSZtXP9mnqmicovi9R6_PXPf_2IFx3nD_dA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آمریکا تفاهم را از چند جهت آتش زد؛ تکلیف ایران چیست؟
🔹
اقدامات اخیر آمریکا در حمله به ایران، موضوع لبنان و آزادسازی دارایی‌های مسدود شده، چندین بند از تفاهم اولیه را نقض کرد. تهران نیز در میدان، به اقدامات خصمانه آمریکا پاسخ داد.
🔗
شرح کامل این گزارش را
اینجا
بخوانید.
@FarsNewsInt</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/farsna/445287" target="_blank">📅 12:00 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445286">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">حملهٔ جنگنده‌های اسرائیلی به جنوب لبنان
🔹
منابع خبری گزارش کردند که جنگنده‌های صهیونیستی لحظاتی پیش، شهرک «دیر سریان» را بمباران کردند. یدیعوت آحارونوت دربارهٔ این حملات گزارش کرد: مسئولان صهیونیست این ارزیابی‌ را دارند که آمریکا محدودیتی برای آزادی عمل نظامی اسرائیل در لبنان قائل نیست.
@Farsna</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/farsna/445286" target="_blank">📅 11:49 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445285">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/42bdd99163.mp4?token=XcKK3xdVCjEx-1zqcUN3KmxPJIbEBUTjcjqHtHQoBCaOlw5r87hYv07toPYOhTgUEYBOOBRQ1uFef_65y5TlhtdYPgKYmz_pAnMeYxDSgokqW1nBivOj2E8eUto7rBqzVyIiGaVFMBcyxYf7VMqgKA0hq02NGULIhwZWTKg4TBvHb9NXXUfQHZii6RGMchdJ5pUd_Nz0iKRE9nKxcpZb9t14NXdweTUpV9oKN3PRHVUfhFv6oZoTbJO9omaV87_h-bQ_f4ErUykMsG-oH3-YDv8EeDN75Spaf9Fkskelz9uQvWtJoukNkhcDcZuE0tN8nbAHqam77WRXB9FVrWrgJg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/42bdd99163.mp4?token=XcKK3xdVCjEx-1zqcUN3KmxPJIbEBUTjcjqHtHQoBCaOlw5r87hYv07toPYOhTgUEYBOOBRQ1uFef_65y5TlhtdYPgKYmz_pAnMeYxDSgokqW1nBivOj2E8eUto7rBqzVyIiGaVFMBcyxYf7VMqgKA0hq02NGULIhwZWTKg4TBvHb9NXXUfQHZii6RGMchdJ5pUd_Nz0iKRE9nKxcpZb9t14NXdweTUpV9oKN3PRHVUfhFv6oZoTbJO9omaV87_h-bQ_f4ErUykMsG-oH3-YDv8EeDN75Spaf9Fkskelz9uQvWtJoukNkhcDcZuE0tN8nbAHqam77WRXB9FVrWrgJg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
عملیات قاطع موشکی و پهپادی سپاه در پاسخ به تجاوزهای آمریکا
🔹
سپاه پاسداران: مردم عزیز و شرافتمند ایران اسلامی؛ فرزندان غیرتمند شما در نیروهای دریایی و هوافضای سپاه طی عملیات مشترک موشکی و پهپادی در ساعت ۲ الی ۳ بامداد امروز یکشنبه هفتم تیرماه، با پرتاب موشک‌های…</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/farsna/445285" target="_blank">📅 11:44 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445281">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pDTlXdNhVXMcRNxlt_1v1o-n9DfDsr2dyOLyB-15PRPFUAOAm66oQE4X3F4ShwUECsFGt0cyE0Y9NrBczDHj6UNjvxMCuNsPqGZgrOuUeJCvdgdrO8oT2fmuX0SrhqiJGTFexbO_gn9JckzsD7JQjlC9Dujni3p2djbRU6uYMx6H6ATFpiaCprkYkxQaF0d4-ETEB7wrnahxMwmY9MNnLb7husDKahNulYb54PVBKuwfJeIeqlISICH8HUrmqmdWQDPP9OVcZ_nwP5ZZI4h7775BQL4wQwKrWJS8pRoxbJgPADCPM_lMLJuALRF6tRz5xfRlk_mbdzph69yo9dp16g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bjoV86Y-WNm-0feY2VbjSW_wj82iBiaK1itF2HZFCcGFR4OLPmiPFh6Mlyt5hOAeVsfKUXHSXy6JXyzdUCopQfbR40v8QQZWbSck4YcoNGn7I0wb72gWNTD8wI5OTyLZYOdCVQik1PHDhv3QmTWxr1yeZuB7pba09EbXZg3bPV9COmD9k6LuPHA_jAInH3M_3VlY9oYYPBx72lIIu_Acp3l7Kc0nKuWJciK5iZaGst8AZPOM33LITSC1JyxhzsGqk167GQQubuENDvzDRTBiDaRIBHsxrT91D_jaPyF0xSfPbM9R3GKFrGKNC1bFMSISkV3lZGWZQiwDCvIug1LHaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/m0oyAYgn4wNix8_Vipd9W_A3B-qzaDvHv6QtRy9ODi-tYMO0zu8S7gU4APfrXO827ATLhYOA_DwS9HblwtWgPvPsHs0SHnR8fC0dk3dpLC2VsWVnP31VQDBg6LYZ7dzA95PUXTyH3fHTvdpjUFJJcoDgAHI2voBwBK9OFz1eMEun1eeWQ0CvVq8QvQakiG2ASLTlAtwJh60zUxeGzr3b2WDqWE27PHu6oj6W3ciEjPOvw_32GLq42cyqisjE2rcOf7gGJ2uUWyxzVoCDri7ROAln8-_npXtLsRHmTpukY42uAyjZnAANfxLFJFpGIt60rfaD3_IsI5cOB_MX8PFMWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Vw8vEzo1to-Y64XFB8U3p8hLb4aiEdVzvOq70-uls0Fly8TIBHZetqJMa_dco29Zv6lacRUJQ-8Sg7KMikvgTtU3eARsGrDKaSJsyEEvlVEyX_CpZcAp1kRe6p9FELrR4ew6j7m4BQh-YS9angczbfh33tB-O66cztHuTFAcZT9O5gUP1XgttxDV3n29XSioP1XeVe_WYtAZVon4Km1cMhGhAu8AAWQPwlSo3DioJ9rswPGqnFcpp8J2mL2yMZjaX0tOdAqYC3JG3dpB-MQlMwu-zeK3g3SGGC0_utW1WeCcXR3yAGaEPmHc4X0-b1fcFHUKYE_MgoWuUYskjW-AEg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">پزشکیان به قم سفر کرد
🔹
رئیس‌جمهور به‌منظور زیارت حرم حضرت معصومه(س) و دیدار با مراجع عظام تقلید وارد شهر مقدس قم شد. @Farsna</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/farsna/445281" target="_blank">📅 11:30 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445280">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ae82fd1339.mp4?token=hdJ7MkXh2l6pMpc54LhjOHssVAUkvPYGPFaVGa7QKKUUPYnov799Oq4RS5ir51MyaqJvByp14X-sULB6zqZj8LrSPtDz_FV-ldOy9uGkjBj_nMRPXfsD3BqO90T8WS-HxIyv0LaisV8hBPrp5nKsNcqr5Q49yHxs6NfnM5lY3H5Of5fup84DBlBre82B-Q_zR59xG43rFiVkXALU5FrPJpbO0N-83Q96_bGrlRHuo4fj7soGTFIIQOiP7XLu2fR1_9SWtyDKB9p5_61VRJgOYB7ZGCiVPY3vEHOb3e1WZVIyZXhUujQE2_JsXiSL5Hj2JyUzBNT1Csbb_84mREVIeXBaMmN_Mxl3gZsm3708tfUVWXaImY1Y0AZDM4hfBREh5fUKzJC6kvIiDerC0ZRKfirbCNZ2g8drb1HoJrmUTrOJxopaRMZxgy_ezgvxT73K-efPsD2Fe9wpyU4KeI7FyUnJXWOHencHMCZD-_0t79pBcBkWXaMnj1RUpQIVXrwsFUg7Tqebkepyi5SEVY2Jg_UHaK9dqro5oHPs5QfA7YxXyddQy1R3mivP27p1PWfuG8-GsjGA34MYnTUXtr1Kv2bY6K8kp1ZMAj88jUeJbnKiqXh2bvRY339SmGVxkBsRH1tT71n_cgBGZnKg5x644tpL4KphLg89xOmcbgUXd0E" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ae82fd1339.mp4?token=hdJ7MkXh2l6pMpc54LhjOHssVAUkvPYGPFaVGa7QKKUUPYnov799Oq4RS5ir51MyaqJvByp14X-sULB6zqZj8LrSPtDz_FV-ldOy9uGkjBj_nMRPXfsD3BqO90T8WS-HxIyv0LaisV8hBPrp5nKsNcqr5Q49yHxs6NfnM5lY3H5Of5fup84DBlBre82B-Q_zR59xG43rFiVkXALU5FrPJpbO0N-83Q96_bGrlRHuo4fj7soGTFIIQOiP7XLu2fR1_9SWtyDKB9p5_61VRJgOYB7ZGCiVPY3vEHOb3e1WZVIyZXhUujQE2_JsXiSL5Hj2JyUzBNT1Csbb_84mREVIeXBaMmN_Mxl3gZsm3708tfUVWXaImY1Y0AZDM4hfBREh5fUKzJC6kvIiDerC0ZRKfirbCNZ2g8drb1HoJrmUTrOJxopaRMZxgy_ezgvxT73K-efPsD2Fe9wpyU4KeI7FyUnJXWOHencHMCZD-_0t79pBcBkWXaMnj1RUpQIVXrwsFUg7Tqebkepyi5SEVY2Jg_UHaK9dqro5oHPs5QfA7YxXyddQy1R3mivP27p1PWfuG8-GsjGA34MYnTUXtr1Kv2bY6K8kp1ZMAj88jUeJbnKiqXh2bvRY339SmGVxkBsRH1tT71n_cgBGZnKg5x644tpL4KphLg89xOmcbgUXd0E" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
این ویدیو را نمی‌توانید تا آخر ببینید
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/farsna/445280" target="_blank">📅 11:17 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445279">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8be510b3fa.mp4?token=eydJuC3wieYwpYDdIxxOZAWd_2PfF5InN_3TIPq3pEFlYmKyOkPFG7oCEqrYl9mPOpDVD68B1wC38I60FBr7t0XYYLQwGCR2wf6_I4OjCNTIz7sScC_QX656jEu_NomB-7qUy0Xfx1l5d9no7Ovp-LmWLnSg_5oEiJFpnsI8RiBF5SDjAxEdIgEoNnw56noKr_-oEa-qLKNqBcOlHKS99q6Gjy6QvtX8as7I8ad2y0gdZEXOiCDHGBtbIcEqy0rp8wpwLFLOaIAqGIurCfFCGh4zK8eoyGILRFrFxw_7MrAg1dy3Q8aVFZ6fgAceGiX9GrHJAmcz7RhbaymTAiQidg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8be510b3fa.mp4?token=eydJuC3wieYwpYDdIxxOZAWd_2PfF5InN_3TIPq3pEFlYmKyOkPFG7oCEqrYl9mPOpDVD68B1wC38I60FBr7t0XYYLQwGCR2wf6_I4OjCNTIz7sScC_QX656jEu_NomB-7qUy0Xfx1l5d9no7Ovp-LmWLnSg_5oEiJFpnsI8RiBF5SDjAxEdIgEoNnw56noKr_-oEa-qLKNqBcOlHKS99q6Gjy6QvtX8as7I8ad2y0gdZEXOiCDHGBtbIcEqy0rp8wpwLFLOaIAqGIurCfFCGh4zK8eoyGILRFrFxw_7MrAg1dy3Q8aVFZ6fgAceGiX9GrHJAmcz7RhbaymTAiQidg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حملات پهپادی روسیه در تلافی حملات اخیر اوکراین
🔹
به‌دنبال حملات پهپادی کی‌یف به تأسیسات انرژی و زیرساخت‌های مسکو، پهپادهای روسی مناطق مختلف اوکراین را هدف قرار دادند. @Farsna - Link</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/farsna/445279" target="_blank">📅 11:03 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445276">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Kj5AZ_z674RabYrb53TwXMZcqG6rCFpYQoLSeEA8M69wOsDMszw4Qea6eXI2dD_-0uTPrGljoTPomucT4UobNSLRYYqk6DYF_Z4jZo0BgAln3H7_plZT_0vQ89tze32AOPWr803khTCmyjlXZO0QqJMKbZo54qxQtnQtxTX6VBxyg6F-ERFBYl2u16UZYpYw-Szth-j_M9MznhVifcE3DCKI78gi2YV2plWDdSmNBzCDjnMLP-4R8uNwxYOQwcF1WaFwW7dNp81UN6P56TZqbTLiVlDCAWp0nskvjiRtO-CINtMhB9fI2GPREFKYYyLWJGrVr2AGgIMbo97EVI_EqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JRFeDLn935Z6CTAxtYH6Z5aeZ1mkOf07UjKbViQL3lOSPcCzZQfqxt-cZ-xQO_6h-41JZq0J3p0V8VMPhA82VIVi-tjoLB3OibG1Rf2kG5eGY5hPewsP3smzgMsQQz9Np9uK42t87oVuzh6M4jY6Cwy2jJP08N1osMHGV_BN6MOpGbXJ9OTp1Tkhd_9hT1Xn47e66O-rMeVA3iwBlyWmzDDfyEwvttKDVj_hUYdeGocwiLHsJMdzC9M6NmWAEmDzEBwRmohIoxZlYvyqWvALnOkMW0WUyq2PcML4azfvbqsJ3VK8NW9VjB-UGUTSChkNJP3wR_cn-4x_SvnVdPiMPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FPp4Bh-0myFtmEkb1_AFuzlHtYtoTe03ErXHDvs8BXFb37_cpHKj20IwA6EdZCDduiv8Dj1Gj8oPccxnkQfwb3jkVKeuDuIFDXlnKHBPXomYTq14J3gWwd0VNuZXRzXoQYllBjiypNv-DKeLlNS5lG-GKL3LYliYZMluqNeQUpr8gklKd1xN4y-nvTd4T30efOcfyZQ4r__1JQsUjuG8YvHZAp6LZNSyyVnrzHcI5ocRB3LeMECy5N4w_pGjaZ6yckc4cYJ-JxyWEOsqxdViOn4tP6iyBDD2c9M8CrWP1yd_bR20D48K7D7pgoKhu7A_FcqJqksglTy3dMCPBW5yfw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🎥
عراقچی در محل شهادت شهید سلیمانی و ابومهدی المهندس به مقام این شهدا ادای احترام کرد  @Farsna - Link</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/farsna/445276" target="_blank">📅 11:01 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445275">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cdc600a860.mp4?token=OTBTO_4MlQ16uky4-G03nefPc2NlZfBHDi5XqjEMX8pA09kqfqDkQX1dx1-6ZNNXy4QSLFnkxx2ou1RIoeyd2--lpDA-PGZ1_d-NUzd4jJgSHryE-5ohUgS5G4AwDyOknCL9qAWjaQhlKVWwDHeoYaHSmSVDC8599fiRsMWQ-lJq0LeMAUEOifgWY5cyh5wCCr8dbvm3e3UbpP0LXL97966PhgN3Cdbn9ySFjiD9P5QKUAU_kKcGz0GuYvI17A1H73uIDUrdFiIe_5N7TlIEGJ0X33GIg8mrTgZycSHoEJ0sSRbOY9_GL0iFYpgEVTcyJmIjkwXnWDHZNtFeYI7T9Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cdc600a860.mp4?token=OTBTO_4MlQ16uky4-G03nefPc2NlZfBHDi5XqjEMX8pA09kqfqDkQX1dx1-6ZNNXy4QSLFnkxx2ou1RIoeyd2--lpDA-PGZ1_d-NUzd4jJgSHryE-5ohUgS5G4AwDyOknCL9qAWjaQhlKVWwDHeoYaHSmSVDC8599fiRsMWQ-lJq0LeMAUEOifgWY5cyh5wCCr8dbvm3e3UbpP0LXL97966PhgN3Cdbn9ySFjiD9P5QKUAU_kKcGz0GuYvI17A1H73uIDUrdFiIe_5N7TlIEGJ0X33GIg8mrTgZycSHoEJ0sSRbOY9_GL0iFYpgEVTcyJmIjkwXnWDHZNtFeYI7T9Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تصاویری از رهبر شهید در ارتش که برای اولین‌بار می‌بینید
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/farsna/445275" target="_blank">📅 10:47 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445274">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/121e2116ec.mp4?token=AGZ4PRVwBYfu2bOEdixwpiAYzjX40jqGsQolevWJS0GN4H6r000ejWMmDQSl1U-a-QRh9rnJo0AAqPXPln_7Plxx7tcfsUnRIWJSeQ79FkqvCReNzWPuiSReY_cf1YR9D-jiB5XgJON6_fYxS5pJ6yvi9a5LXedfOTU7vLBeFIwmnnzWianfaVwI3wDaQKpdDjvariIAYiWYfYz3d-VsEmtzT1uXWQ_lCtsoO3lccJ3DgPs0DIo8kyFfJX7yzS4M31m3cYtl1k7wthER5lgL5ScxmW9hCKh-pvRuBdu8CECmerQyggxozqO0uoeZPll4KK4kFy5Jn3XFhJeq8xHsOg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/121e2116ec.mp4?token=AGZ4PRVwBYfu2bOEdixwpiAYzjX40jqGsQolevWJS0GN4H6r000ejWMmDQSl1U-a-QRh9rnJo0AAqPXPln_7Plxx7tcfsUnRIWJSeQ79FkqvCReNzWPuiSReY_cf1YR9D-jiB5XgJON6_fYxS5pJ6yvi9a5LXedfOTU7vLBeFIwmnnzWianfaVwI3wDaQKpdDjvariIAYiWYfYz3d-VsEmtzT1uXWQ_lCtsoO3lccJ3DgPs0DIo8kyFfJX7yzS4M31m3cYtl1k7wthER5lgL5ScxmW9hCKh-pvRuBdu8CECmerQyggxozqO0uoeZPll4KK4kFy5Jn3XFhJeq8xHsOg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قابِ متفاوتِ احسان یاسین در شب‌های محرم ؛ خواننده ای که خادم عزاداران حضرت اباعبدالله(ع) شد
احسان یاسین تنها
خواننده سبک الهی - عرفانی کشور
با حضور در چایخانه هیئت عبدالله بن الحسن (ع) در قامت
خادمی عزاداران اهل بیت
به سوگواری پرداخت .
@Farsna</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/farsna/445274" target="_blank">📅 10:44 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445273">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kBlCRdA9yJglYro-beWaRGQxMQDGUlicelsavbiVh1ypEcbxvxpjwtk_iItlKWvKx_BRE7KwzXF5_QjreYHknYQ3STdkgvTgNf6Bdp_uw7n6n77Wn3n1ayWUybii9ZL6VCy1qBmMZZiQJg5N5GVJFyGmumElJskoq0SeNLt-K0MqGwLTFILpGag2CDn_ZoYDTcb9wj-6wlpYzoeOfiQoVvRpJclTSJBGHjn1BKuJjd8uYa4_-RG71pklcBPY5Wm2ERpMorL4SPt2nKDRZBPok78_moXM3Zpe9GWgXYsWtkW-f2jN85w-exk0l7M6-mG-L59KVQoXnXSOFDSb7AR_9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
به مسابقه جام جهانی دعوت شدید!
جام دی همزمان با جام جهانی
با جوایز جذاب و متنوع
⏰
هر شب از طریق شبکه ورزش و
ویژه برنامه ۲۰۲۶، همراه بیمه دی باشید.
پیش‌بینی هر دیدار،
جایزه داره تو دی‌دار
ورود به بازی
daycup.dayins.com
#کانال
اطلاع رسانی شرکت بیمه دی
@dayins24
#دریافت
نظرات
@prday24</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/farsna/445273" target="_blank">📅 10:42 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445272">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/farsna/445272" target="_blank">📅 10:42 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445271">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/303480ddde.mp4?token=UQmMBizFTB6-ZZ917OhO7XLx-DaV0mkypAVWmPSMwDmX-oDsqIZUPF9chcHq5zNTYZUm9He-8HEmrEr_t86Ov-vL2-LIxuITkdNXBk-PCdOMYIm-sMcVae5PZxp4N5HIknmPMwSxSIqBqnsO7xs7u_vb5PHy5Z2Du6KEQNYDJKw8qhd7UHlJGeGaJOb4jWZcL9zIwn1JIsl2uIML5MPrnmvyKYO4e49Gkd7H9INqmGlkSLCJKWvW6tNGkjiu_ZSH3OAbv0bGNQZW8uMAJNaVCTabjejnJgThleDkZa7fS1io-E3jxZmu0V9omQTRXpgM1PfOsrGFHpdg0GQSh7psbQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/303480ddde.mp4?token=UQmMBizFTB6-ZZ917OhO7XLx-DaV0mkypAVWmPSMwDmX-oDsqIZUPF9chcHq5zNTYZUm9He-8HEmrEr_t86Ov-vL2-LIxuITkdNXBk-PCdOMYIm-sMcVae5PZxp4N5HIknmPMwSxSIqBqnsO7xs7u_vb5PHy5Z2Du6KEQNYDJKw8qhd7UHlJGeGaJOb4jWZcL9zIwn1JIsl2uIML5MPrnmvyKYO4e49Gkd7H9INqmGlkSLCJKWvW6tNGkjiu_ZSH3OAbv0bGNQZW8uMAJNaVCTabjejnJgThleDkZa7fS1io-E3jxZmu0V9omQTRXpgM1PfOsrGFHpdg0GQSh7psbQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سخنگوی ارتش: در طول جنگ ۴۰ روزه تجهیزات پیشرفته‌تری ساختیم
🔹
برای مثال، در روز‌های پایانی جنگ از پهپاد‌های جدیدی استفاده کردیم که مراحل تحقیقاتی‌شان از گذشته شروع شده بود و توانستیم آنها را در دل جنگ عملیاتی کنیم.
🔹
همچنین موشک‌های بهینه‌شده‌ای در سطح نیرو‌های…</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/farsna/445271" target="_blank">📅 10:24 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445270">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5397b19d2b.mp4?token=XaLXoB1ta9deJzN0d8_2HyMh6GYLoXvLF93lfvD1r9YjPJX_cnm8t_zJT88XlZtuwHKx50fDMbUCHzoun0HACnseSf4GeLFDr1UmHOtJWfyN85ORMqfYnzOOE8ALE9-v3ZJhSlIC6gkYit4dNnoiEBjrUDOamH-rzmmfbiayqfzTiw4YIPEnpLnMGQ1yFCZMyJ5kj0fk5cbyjeWnTWvZMkloj4qUviuEXXbKnnUuyO6GrF7-MvfBbBLaGUh3YCM1ljzCkXmfR6W3Ek9qHxhD_PPjWO0WwWtUpBMYtez8izJWnrnJ2o13FMTaOKbddDKBlkgXxGMezRkUJs0eYjRJP4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5397b19d2b.mp4?token=XaLXoB1ta9deJzN0d8_2HyMh6GYLoXvLF93lfvD1r9YjPJX_cnm8t_zJT88XlZtuwHKx50fDMbUCHzoun0HACnseSf4GeLFDr1UmHOtJWfyN85ORMqfYnzOOE8ALE9-v3ZJhSlIC6gkYit4dNnoiEBjrUDOamH-rzmmfbiayqfzTiw4YIPEnpLnMGQ1yFCZMyJ5kj0fk5cbyjeWnTWvZMkloj4qUviuEXXbKnnUuyO6GrF7-MvfBbBLaGUh3YCM1ljzCkXmfR6W3Ek9qHxhD_PPjWO0WwWtUpBMYtez8izJWnrnJ2o13FMTaOKbddDKBlkgXxGMezRkUJs0eYjRJP4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عراقچی راهی عراق شد
🔹
سیدعباس عراقچی وزیر خارجۀ کشورمان، صبح امروز برای انجام یک دیدار رسمی از عراق، عازم بغداد پایتخت این کشور شد.
🔹
عراقچی در این سفر با مقام‌های ارشد عراق دربارۀ مناسبات دوجانبه و تحولات منطقه‌ای و بین‌المللی رایزنی و تبادل نظر خواهد کرد.…</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/farsna/445270" target="_blank">📅 10:17 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445269">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/899d7b7908.mp4?token=YUPPGUSSenjPq6Lr8Qp_CnH9z8Q0bSf1cunfulnU0Hspklqx2Z_6Z4d7ewgYFP4t7N2x2NLf65btdFaA5PL4NndOScnTUXjX58uY9cpLHSQgrO8Cq2iqRf4P3YXMc7-V6-n3S9WuXqAjeS29sagLbPZHBe0xIuNlQxWn6SXHtZxJe41VklIDpUnyvwtrqeIyiKAFb64hVcYIn_4EJCjnPJwt8KucL8qoUqkyKr4FON9UKbnaWaEaBHMqV2FJJ4v-ibK7G9evvWpWFFHo2AOa3fur7wjJjf7rfMaQTAxz9j_0VzgL8uzqKHy5XEUyCAj4DCDxw-OwlmdfsxnJ27-Q1g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/899d7b7908.mp4?token=YUPPGUSSenjPq6Lr8Qp_CnH9z8Q0bSf1cunfulnU0Hspklqx2Z_6Z4d7ewgYFP4t7N2x2NLf65btdFaA5PL4NndOScnTUXjX58uY9cpLHSQgrO8Cq2iqRf4P3YXMc7-V6-n3S9WuXqAjeS29sagLbPZHBe0xIuNlQxWn6SXHtZxJe41VklIDpUnyvwtrqeIyiKAFb64hVcYIn_4EJCjnPJwt8KucL8qoUqkyKr4FON9UKbnaWaEaBHMqV2FJJ4v-ibK7G9evvWpWFFHo2AOa3fur7wjJjf7rfMaQTAxz9j_0VzgL8uzqKHy5XEUyCAj4DCDxw-OwlmdfsxnJ27-Q1g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سخنگوی ارتش: در طول جنگ ۴۰ روزه تجهیزات پیشرفته‌تری ساختیم
🔹
برای مثال، در روز‌های پایانی جنگ از پهپاد‌های جدیدی استفاده کردیم که مراحل تحقیقاتی‌شان از گذشته شروع شده بود و توانستیم آنها را در دل جنگ عملیاتی کنیم.
🔹
همچنین موشک‌های بهینه‌شده‌ای در سطح نیرو‌های مسلح، هم ارتش و هم سپاه، با کیفیت بالاتر به‌کار گرفته شد.
🔹
این نشان می‌دهد که ما در عین حال که از تجهیزات موجود استفاده می‌کردیم، از حوزۀ تحقیق و توسعه نیز غافل نبودیم.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/farsna/445269" target="_blank">📅 10:10 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445268">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/74179bfa7b.mp4?token=ENfh0PQqb_jMZRBzv5n25293Zu9JpQV4ZgwhtHp9XD1lxKIuydOf6iL3EANMhBVada09cNVssF23a4_iKuNhCMQePD7Acv8uMYuu9qfCWmDxBEtgN6Krp6SoDkpg_HxSDPpm5EBPKPZ-5sy4C6RWbFl6bjWGBqic5mns8InQ0_ibkr4aY12WHGKDd2eSrP_DbEocRCTjUjdVBeAYQ-djlhdeiPfvryVt4ovUDWxk8teYBegQNWIzdp-lF0gzTNuoMVphZEZabKmBcgT8ZsrUq-zJ5BuMnqLq1D17nEilRFrrqecGdyJcuZ-t4JO538wxoT-lsAAUd1ettRylQgQURw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/74179bfa7b.mp4?token=ENfh0PQqb_jMZRBzv5n25293Zu9JpQV4ZgwhtHp9XD1lxKIuydOf6iL3EANMhBVada09cNVssF23a4_iKuNhCMQePD7Acv8uMYuu9qfCWmDxBEtgN6Krp6SoDkpg_HxSDPpm5EBPKPZ-5sy4C6RWbFl6bjWGBqic5mns8InQ0_ibkr4aY12WHGKDd2eSrP_DbEocRCTjUjdVBeAYQ-djlhdeiPfvryVt4ovUDWxk8teYBegQNWIzdp-lF0gzTNuoMVphZEZabKmBcgT8ZsrUq-zJ5BuMnqLq1D17nEilRFrrqecGdyJcuZ-t4JO538wxoT-lsAAUd1ettRylQgQURw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رسانهٔ صهیونیستی کان اعلام کرد به تصاویری دست یافته که لحظهٔ هدف‌قرارگرفتن نیروهای ارتش صهیونیستی در حملات حزب‌الله در «مارون‌الرأس» در تاریخ ۲۵ مارس ۲۰۲۶ را ثبت کرده است.
@Farsna</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/farsna/445268" target="_blank">📅 10:04 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445267">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GL4oeOMTkIzCroHrKRNveoZPT48-FEJi7bSLnSsAb5U-Gt25t-liv8BbLtYYJkR_qpAefgetUVyNqjal7Ifjnxs29MlzMXmz2E40bxJlpreMo0GFKTc8o7jXOrJXVMAL4NR7q9DitRuVrC9dEGDoQgg-1-ZkEzL1Xs-RPOXpmRA1i_pSuWETqIEAbDsB82oh7glq8ov8FTnoMfMWbde54cdh1BCve9NNfIe8h1JSXRiKG-8uUXRQNfcUbsDR3PJbJ9rvrX4CCiVNctXnCHK7MESbVqvn5-cPgkSGGoDOX_BBELqkcPVROnLgZV9i9svxWfEskEeEzEvaEqrDjr3-UQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
نمودار مرحلۀ حذفی جام‌جهانی  @Farsna</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/farsna/445267" target="_blank">📅 09:35 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445266">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WMNjpZqBrL2nzg5SFfcifW08g3fp7ktOIof4AuAtkBdg4i2jE_5ywB155MTSRaKfHLjeO_-MvZn9ZXGOeSQZ_FG29YRCow_DIkOUHemwjmJUejmvoRFEWV58H6rMlYL9FZPgBS23hS118grn8tftL3rqT-bq1hJQh9HMH6-Sfe_uFgjb1Zim_0_UELzqN1ntwRrCMmnO67vcP9PzyNEXvGG1xNw2wkt58zuaPE6Whj19cz54sG1j6TC8tQuMlUwVqIjXVybRuUbsG19qx2a6jSdDxgKuTzG5n4agovFKZgDNAxfdwC0VVRTvS9PqRV_kUHFDaVTjch6WPLaTGaUfZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
عملیات قاطع موشکی و پهپادی سپاه در پاسخ به تجاوزهای آمریکا
🔹
سپاه پاسداران: مردم عزیز و شرافتمند ایران اسلامی؛ فرزندان غیرتمند شما در نیروهای دریایی و هوافضای سپاه طی عملیات مشترک موشکی و پهپادی در ساعت ۲ الی ۳ بامداد امروز یکشنبه هفتم تیرماه، با پرتاب موشک‌های…</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/farsna/445266" target="_blank">📅 08:51 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445264">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lNxJ8TOxyPW1_svytEBpQfxqiz4Pq62S-r4BfKMuTpiJF13NhSlxXNBB8-oRnmF1y9Tt3aLSmrHQ3HpF7eXQodU7ifP7iaF7b4ourseNVEbhVUXD4PqSmpb6R9LpINzd-KtN0O8lU3P4Fn4qZQBql-Gm9HlKpv6VWyjaZj9qrzgiw_aV6LheTfklorNr8Znvq0f-rpruFkkL5qAYlzHrKcZaj4a125QwwFq1yQEtPA8eZdDF57aVjqIdnhwZn5ML0gmT0InyeO1OhNn89PE9VSTYbyqW5X-fR06Kp7MvfqFJMzj8rgpXWJgMECuJ3etq5W-d_fOIMtbUesJ4raMYnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">المیادین: عراقچی یکشنبه به عراق می‌رود
🔸
عراقچی هم‌اکنون همراه قالیباف در عمان حضور دارد. @Farsna - Link</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/farsna/445264" target="_blank">📅 08:03 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445262">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">اسکان و فعالیت‌های تفریحی در حاشیۀ رودخانه‌ها و ارتفاعات مازندران ممنوع شد
🔹
براساس هشدار هواشناسی، با ورود سامانۀ بارشی جدید، از امروز تا صبح فردا دوشنبه وزش‌باد شدید، رعدوبرق و آب‌گرفتگی معابر در مازندران پیش‌بینی می‌شود.
🔹
با اعلام مدیریت بحران مازندران، اسکان و هرگونه فعالیت‌های تفریحی در بستر و حاشیۀ رودخانه‌ها و ارتفاعات این استان در این‌‌بازه ممنوع است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/farsna/445262" target="_blank">📅 07:56 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445261">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس ورزشی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tPV4YAyA0ncMovkyeXOVxbpFoQ9BnK2hYCHEFf2rKDXHd1xCVIyXQN1JZpQ1uldUcdyOuCrhAaMvoC2uH3UL-6-xF3PKF2bU0r6Uw3y-kQQCLp55x6HQwG4IBEf60gzjz0Lnmy9w9cWD1llFbw_w3_yfnjtdTt2xB8l9ul82M3XsIq_1faIKBaBJPLoOEWKgmcH-R6nVqaut9wgDuWwFw5Rzzang1LMSwt_SvuUQqx8dBFswCMmpB6r-r7Gz8wadJD5hxuEuYHLL38UgYfaMKuNZppfAPKIBfAUPK_CiiWvkfo7YfA0QmrjFxmsOA95XTbS5_T_quDG5EbXaXAn9kQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بازی تمرینی آرژانتین
رکورد جدید مسی: گلزنی در ۷ بازی پیاپی جام‌جهانی
⚽️
آرژانتین ۳ - ۱ اردن
@Sportfars</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/farsna/445261" target="_blank">📅 07:46 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445260">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EDKmmsYrRFZpZqRonLiKSisDHIw8_C-EJxH78I42FtNCyw5NhLeCbHrst0NBaPj9tOhEu9oezZXxZlfYywjR3LHaG2amrLv1rysN4cFrNgVZrLADxpbD5-RmNEqOFiFYr-tRdInJ2L3sMgWZt3btr9r1YVM1mip_yd1IdXxWxHdH-34y-Kqd8bCY-HVvA97AewD048cB7_IGqzs2Rn4DHGqDDkLVmnHH4DjTUgt0oa6c5aRxXOoXBRofxFDZTi770oxF8ZJyXVinoDx9UlxE8E1Zrgk2TIWaQNiXCXcA3qBIBq7nadRotNAcFX7co4D5O7fdHQn5QEWtV-Z2xR6VbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
نمودار مرحلۀ حذفی جام‌جهانی
@Farsna</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/farsna/445260" target="_blank">📅 07:40 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445259">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZSLjPDd8AcEMT6tso6MugbF-VRGooPKQN2Yq1hJmym9ZSwVutvIMFcAX5JodRRZ72ug2Anm87ljt0M9b9TytMX7tw1e1tbAcKwgiLefZEKMcE6v-0mnM-2TYlqxD_pPr33FIzBCjXaS3BARBiYWYOezqgrXKC7PgLS-Mu5wd2OQqzcerjQTGTFMJezoQIMR5ofBqaVlxL4u7wYJ5uAh9UMjxKc3gdRLNnqMczhyYrwmZOdQxOnfdY9Ofh3U5tzPBo9lQceKcuvC28ygQDPoq9w5Ld0bfLAgYbCSsknME4n6ZeILnqjFWNBe1dQ1po0vDyRT4z0iPUqHyHS0vt1I35w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
جدول تیم‌های سوم پس از پایان دور گروهی؛ ایران از جام‌جهانی کنار رفت
@Farsna</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/farsna/445259" target="_blank">📅 07:37 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445258">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس ورزشی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gS3Xn-qO3nfMItdEyT3_BBnVgrif63M-JLqnt1u5koXSyOq8H8xa-7xxbA5WtqbMFJBZerdrtk-vhJPaUCBZVpaedrpoWkQDpZT5B9Lpzwr-DdrgJy-ILXwQuIBCjh8VXY0gv0vrtJpIHB4oMJXM1dvvvloEDjmfif0WopBAJgr9-YWqphtKsQ-dPz95xCNq8YHJlxHgwj56dMnW_tyQXTao2_1X_CPfSoYR0YsXPPXfE4aqllQWmQ9BrLjA28DO2Ks-A0TFeDmrMZB7emqBnPHOV1p8BPXBUWYrpDcuWHorEQqOzsrGgTyO5uaINX19Hzq0qpVkQYr4RjaGTuHSIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همه چیز این بازی باورنکردنی و غیرعادی بود
دست‌دردست هم صعود کردند
زودتر از این جام حذف شوید
اتریش ۳ - ۳ الجزایر
@Sportfars</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/farsna/445258" target="_blank">📅 07:31 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445257">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/barcIoMW929g6EydRZ9jYJJ8oNCUCxEk8pDFOY8sckyzWOdjEgf_3tU9togRWGdI4-_RY8Jn2ZiOTIjHfKtDt-XVJpoJGRC9vYEg1YBmN5CWraFqvrT0J7Iz6GIJLQe8EBMX2IPwVoQopOW7SfKyP9Ua99OicGnjTlyPJJcT99wh2Kc8M8NLMmnHMFdv1A664rokLMhNEgMuGpqfx5k354WWt0mKCMOnCYjYOpH2jUS7P6_0t3hUG7_5i29roAbNMdAgouboqilg0B_hVAk7Orq2-nziE0PBMTFRT8PZ_J_VDdJJ5wF0WB09-PsyhWUPeiyEbDZ5xmu4Q1DZPwohyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پزشکیان به قم سفر کرد
🔹
رئیس‌جمهور به‌منظور زیارت حرم حضرت معصومه(س) و دیدار با مراجع عظام تقلید وارد شهر مقدس قم شد.
@Farsna</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/farsna/445257" target="_blank">📅 07:30 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445256">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rTl3QESDnWIeKjZDfc3Jzn_j3jzf_I8YHMkDhVdhA7G2by5_ClJ6XOb4sy1IcsMZXeyvfq1zY3tGBL0MPxKamebakONDcJdElzFjGboU2A1TXqNpPiNc4_Ltei4KbSIpLHz2L6d2Vs8A5ddUZADruQDEvc9iosxs2T_Qdl-fGve-184wzBsCXoOgba5nhJO4whXZq2VHohiANmksZTnc2d9zIu5t9cVTAjTHm4s5GpaPw09jlDtnzcaB9VyltkdixPeEYM2DCyb2o2E9fsWA4rmaAtdStqk3lF4b3seJN5OhHdnlOtp9G9hZBEN_28CNJFGI_wKPJejAVTWO6xK_CA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ثبت‌نام کتب پایه‌های ورودی آغاز شد
🔹
ثبت‌نام کتاب‌های پایه‌های ورودی اول، هفتم و دهم آغاز شد و تا ۱۰ شهریور ادامه دارد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/farsna/445256" target="_blank">📅 07:20 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445255">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🔴
منابع خبری از فعال شدن آژیر هشدار و شنیده‌شدن صدای انفجار طی دقایق گذشته در بحرین خبر می‌دهند.
@Farsna</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/farsna/445255" target="_blank">📅 07:08 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445254">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PdvTcWc_4yaIuvZqm2bgsMlWIIT3UOfCN2eNri2iUbte9lNrD5gwfWGMmbMxI90ltK_A8L0vUm4bK5T_58W4hFpfGGvG2Zny2xM7rQGgQUBBENPa3tlGMGV76Mvf-vpPyCf-Q85Foz6bPbjSrLJ5cMznTU2vWI0k4PcwohOAgVXg0yLL0xPFA4FGAc9IxVeM_kBXn5f2Xx0cFi670OhQ5uInTmqcqrqMqlu-c1EngcqmmQfnAWyC4fOqwDFbazJ5pPcVreEZpOMY5gMGPiD1EUebxxZPfdIYRrLhmeP167nF7wnIZ-8ziIfBv1QKEGxTin5GLZYAY4cv-5bAuGIJGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استعفای سرمربی اسکاتلند پس از حذف از جام‌جهانی
🔹
استیو کلارک، سرمربی تیم ملی اسکاتلند پس از قطعی شدن حذف این تیم از جام‌جهانی ۲۰۲۶ از سمت خود استعفا داد. این در حالی است که او تنها یک‌ماه پیش قراردادش را تا سال ۲۰۳۰ تمدید کرده بود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/farsna/445254" target="_blank">📅 06:28 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445253">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xo_UUgXHCITEBvNQhLriTXY5VIQymYpXrlr3dhM9EmciH-pvKLMgLRJcMXjRMlmxaIENX0pGRebS_dw04ZZvVKJPJm7u6prz3q7FlPTojsG7bugrePATiTa959bieoO0DDZdZZuqsPJ-_EqEVikJ7uPgbDRn1ZquqavpAN39fjw_4S_cbruCNCekSyIS6Qz0JQl_8UCXvwNDS9ULpMt7tauyzEQvHU9hfrH10hCgbJFSYNC9RT3WuCW964ctZQXLm2rzLRUWKGbNFBQt4c2xlv6c6zCDHfkkAt6Op1aCYip2TGErC-mAvFdz5fAIBAn3TKzs09SBCmDZXT_X7gmw2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیش‌کش ۲ منطقۀ غیراشغالی از سوی اسرائیل به دولت لبنان!
🔹
بر اساس توافقی که دولت سازشکار لبنان با اسرائیل امضا کرد، رژیم صهیونیستی اعلام کرده از‌ دو روستای زوطرغربی و فرون در جنوب عقب‌نشینی کرده و اجازۀ ورود ارتش لبنان را به آن خواهد داد؛
روستاهایی که اساساً تحت اشغال نیستند!
🔹
شهرداری فرون در بیانیه‌ای گفته قرار گرفتن شهرک فرون در میان مناطق آزمایشی را رد می‌کنیم و تأکید داریم که این شهرک منطقۀ اشغال‌شده نیست و خارج از خط زرد قرار دارد.
🔗
شرح کامل گزارش را
اینجا
بخوانید.
@Farsna</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/farsna/445253" target="_blank">📅 05:40 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445252">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oqO0BRivGndabwpZur0b7r2oD8MC4SZZ7DBe-H4xutpL5sW0gVNwpr-k29eZ6s-8Bycu-lL11oQQHSzSLliQGSnlWYF16L4c3d7_dj-iYqryfgblRU8-iAV_xXZFQ1hpkUkxEthjeP1hE1nypK4vlrb4ERCYGV_TJXzC-7EAdMJ5IK1KLnAsGk2Y2GW2Cv1AbyZC5nR26gl_9MtAGyM-_IKrNF5g8QToER1DAiibOM7dSybURg_tMC-vlop4GdoDjR60M61JeCLS4I5Ijktk-OsHaXG2P94FBri1B15b0awhCQIyFfdln8zkj0eo9aP4W5VRZn91BmAZdYgoztfgfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کنگو مقابل ازبکستان پیروز نشود.</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/farsna/445252" target="_blank">📅 05:05 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445251">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a5kXJlgiUQijasZ06Q7K6nIO04nRBggNWmR8_1SE2Njs1fl9PfjJPcwOKtJxIqRKv9FKPC-fSFescHUD3wWG8BlZ9MfqW8Y7n9s3glbHhLwbxOP4X-b9H7mKOp3069itbHWvwiRpAXBSVIPZJdce3cauMYkNbUIl9COthLcF0QL3Syo3v-BREU-qgMbACvo-IIDqSR9hJEWX7E7vgWNkEfKnkhHGxA4ifkJIb-dJLHzLYvU9fRJlyHvXwF1xZd-CK6gHsJZq6WN5mTTN4DsntT1StkXxSFlGDZn1PzL8iZOktxFw3OzENYWCsX42iuNso1pgrQt56PpND1KzCkUBng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بازی پرتغال و کلمبیا با تساوی بدون گل به پایان رسید.
@Farsma</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/farsna/445251" target="_blank">📅 05:02 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445250">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">وابستگی دوباره به شیخ‌نشین‌ امارات در کمین تجارت ایران
🔹
در پی ازسرگیری تجارت ایران و امارات از طریق بندر جبل‌علی، وزارت صمت امیدوار است مبادلات به شرایط پیش از جنگ بازگردد.
🔹
با این حال، کارشناسان هشدار می‌دهند که وابستگی دوباره به امارات، ریسک تجارت خارجی ایران را افزایش می‌دهد.
🔹
تجربۀ توقف ترخیص کالا، مسدود شدن حساب‌های تجار و اخراج برخی بازرگانان نشان داد تکیه بر یک مسیر تجاری آسیب‌پذیر است.
🔸
با این حال درحالی‌که امارات به‌دلیل زیرساخت‌های مالی و تجاری جایگاه مهمی دارد، اما کارشناسان و مسئولان سابق اقتصادی بر لزوم تنوع‌بخشی به کانال‌های تجاری، مالی و لجستیکی برای کاهش اثر تحولات سیاسی و ژئوپلیتیکی تأکید می‌کنند.
🔗
شرح کامل گزارش را
اینجا
بخوانید.
@Farsna</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/farsna/445250" target="_blank">📅 04:46 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445249">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dId5YDOmcY_58arnNGkGzUaKrDuIObBCjkentA8hT19rD0beC7wRszOI7h9DV9JFw2zkZdtQYyn84BLN2CLCHRZo19OuqcO2_VPmGr4rlBlug-ACXL-G1sef3_zjMzlVzEvEEMSVpg0I4Pd9y8cIdQM7G7jDKEbTD4RtgAtQn-3WAGxQv4PnOC-Xz7uwcBTdruWHd94XlFwujcyGUuHfsaMJvybOkrp81Duf8zmvhMsH05SaNy8SuhxVVAi5hBCdC4MPbsPTOVTk5HKa0aFfdgmhIjTseqdTA2g9zxfo2aiqzUG_f8n6_h6pxmhLNzMXSy0tpFH_qX6Iz_VNM5yapw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
نیروی دریایی سپاه: آمریکایی‌ها جهنم را در این روزها تجربه خواهند کرد
🔹
فرماندهی نیروی دریایی سپاه: شلیک‌های کور آمریکا به سیریک معمای اشراف ما بر تنگه را حل نمی‌کند. اما شلیک‌های ما به متخلفین، راه روشن عبور را به باقی شناورها یادآوری می‌کند.
🔹
حساب پایگاه‌های آمریکایی منطقه جداست. جهنم را در این روزها تجربه خواهند کرد.
@Farsna</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/farsna/445249" target="_blank">📅 04:25 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445248">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c935e2c032.mp4?token=lRDHRQk-B4b0QCMQ5OFk-IuComfiOFcvOxS8rML7agaX283Er_k6lExIvoqLvdxdAfI4vgnntMjpkM3sep5-sjiVC-FDzhrxz1sZh3gN7Y8J1KaHcYfNHIYzbFrMP-qShxP5yxV0RmuNcmmX3vksjDqhCFTOmTR1cDeEb-Dk_WK2yynVfOJmiz1u43TlcOOWd07BaD8f5s9qb3iPVGP7HkJQSCPSz6d7riOoK8si5nhQup0Khlq5-reM-s7RrHZQeB_0ZTfg4sV2gtm6xlzRpKogEwbapCEG46LUWSQhnuL5yn-njMP8Ppk9wvLZwVNbA5kLZIL42LU6QmSm5MsVag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c935e2c032.mp4?token=lRDHRQk-B4b0QCMQ5OFk-IuComfiOFcvOxS8rML7agaX283Er_k6lExIvoqLvdxdAfI4vgnntMjpkM3sep5-sjiVC-FDzhrxz1sZh3gN7Y8J1KaHcYfNHIYzbFrMP-qShxP5yxV0RmuNcmmX3vksjDqhCFTOmTR1cDeEb-Dk_WK2yynVfOJmiz1u43TlcOOWd07BaD8f5s9qb3iPVGP7HkJQSCPSz6d7riOoK8si5nhQup0Khlq5-reM-s7RrHZQeB_0ZTfg4sV2gtm6xlzRpKogEwbapCEG46LUWSQhnuL5yn-njMP8Ppk9wvLZwVNbA5kLZIL42LU6QmSm5MsVag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">منطقۀ سبز بغداد بسته شد
🔹
برخی گزارش‌های تأییدنشده حاکی است منطقۀ سبز بغداد که میزبان مراکز دولتی و ادارات مهم عراق مانند کاخ ریاست‌جمهوری و کاخ نخست‌وزیری، و سفارتخانه‌های آمریکا و انگلیس است کاملاً بسته شده است.
🔹
برخی منابع خبری با گمانه‌زنی‌هایی دربارۀ دلیل بسته‌شدن این منطقه نوشته‌اند مقامات عراقی، مثنی السامرائی، رهبر ائتلاف سیاسی «عزم» را به اتهام فساد مالی بازداشت کرده‌اند.
🔹
او یکی از برجسته‌ترین سیاستمداران اهل‌سنت در عراق به شمار می‌رود و در پی این بازداشت منطقۀ سبز بغداد بسته شده است.
@Farsna</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/farsna/445248" target="_blank">📅 04:23 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445247">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🔴
عملیات قاطع موشکی و پهپادی سپاه در پاسخ به تجاوزهای آمریکا
🔹
سپاه پاسداران: مردم عزیز و شرافتمند ایران اسلامی؛ فرزندان غیرتمند شما در نیروهای دریایی و هوافضای سپاه طی عملیات مشترک موشکی و پهپادی در ساعت ۲ الی ۳ بامداد امروز یکشنبه هفتم تیرماه، با پرتاب موشک‌های بالستیک و پهپاد به‌سوی هشت زیرساخت مهم ارتش کودک‌کش آمریکا در پایگاه علی‌السالم کویت و ناوگان پنجم دریایی در بندر سلمان بحرین آن‌ها را منهدم کردند و تجاوزهای اخیر آمریکا را با قاطعیت پاسخ دادند.
🔹
دشمن متجاوز که نقض عهد و پیمان شکنی در ذات او است، به بهانۀ مقابله نیروی دریایی سپاه با کشتی متخلف، اوایل بامداد امروز، به پنج پست ساحلی جمهوری اسلامی حمله کرده بود.
🔹
براساس تفاهم‌نامۀ اسلام آباد ترتیبات کنترل عبورومرور در تنگۀ هرمز با جمهوری اسلامی است و من‌بعد با کشتی های متخلف قوی‌تر از گذشته برخورد خواهد شد و برخورد با تجاوز احتمالی دشمن به هر بهانه‌ای که باشد ولو مانند دیشب و امشب تجاوزها به اهداف کم اهمیت باشد، پاسخی خرد کننده خواهد داشت.
🔹
دشمن بداند نقض آتش‌بس خلاف بند یکم تفاهم‌نامۀ اسلام آباد است و توقف کلی روندها را در پی خواهد داشت.
@Farsna</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/farsna/445247" target="_blank">📅 04:03 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445246">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X2zUcDmzFBScggQnqySHtqxQ8rqoyLXfJA2AOMw6Rb94RQyH06VLxqIhgzZe4p4a8gi3rsOqhE_jjqZm7iinvHuF17qaW-_9zjhAJDhQhQnhxCj7m2eUsJrSklgZKc6E48dHf2De3CuGoJLS_t-EN3TgfhwFZK-ewLjVIXi8-ki7zI84BfOuHpA5bTPqxDcuii1J8Vy6CM9Q62aBSg0OcWwUOks282isMZqUkPAYs3IWVhqX2FwQBcT6YjGaUnkBrIqAYLI4KocTItKacYh92jBd_NctYUFHvw5b7Zt6XFTLSXaII6Nb56n3C3U99CFSC9E8hTrb8UIw_flHxSsfig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
وزارت کشور کویت در بیانیه‌ای از شهروندانش خواست از ایستادن در کنار پنجره‌ها و مکان‌های درمعرض‌دید خودداری کرده و در مکان امن بمانند. @Farsna</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/farsna/445246" target="_blank">📅 03:49 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445245">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SOyh5Qas5uBJco5N5bkstzy50Cc-ipelXctuPaK5zgY9KA0O9MWUwZxpJ5KzahVZWuwuxEFbb2n-JXt71jl_vK5cbeXZwSYY6CYWLHjaBL8kDlkppc2oJeP7D0cBjiHTsEnqMmSmNQVYsS6SVfasLH2x9WaFlkWT-QdMFpGJzQroMy6rkMyf6IAdwuUaMijLCoJKEtXYeY_6xcK3eN20HSSqIhLlI_VYJHnlWEz2Vy4p6r7SV2EHMml23jU6f0ipdiJmkEzDQbgV3XJIFVk3VGotJ41BaNKNqo3qMxcHhWDdwxGdgIF8dz1nYSRSV_njjFfNAV-Zm4P8cB4-foK7vA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌
🔴
صدای آژیر هشدار در کویت
🔹
برخی گزارش‌های تاییدنشده از فعال شدن آژیر هشدار در کویت حکایت دارند.  @Farsna</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/farsna/445245" target="_blank">📅 03:45 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445244">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🔴
گزارش‌های تأییدنشده از صدای انفجار در بحرین
🔹
شبکۀ خبری پرس‌تی‌وی نوشته بعد از حملات آمریکا به مناطق جنوبی ایران گزارش‌هایی از شنیده شدن صدای انفجار در بحرین دریافت شده است.
🔹
هنوز منابع رسمی این گزارش‌ها را تأیید نکرده‌اند.  @Farsna</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/farsna/445244" target="_blank">📅 03:40 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445243">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">غول هوش مصنوعی آنتروپیک در آستانۀ بازگشت
🔹
آکسیوس: دولت ترامپ به رفع توقیف قدرتمندترین مدل هوش مصنوعی جهان نزدیک شده است. مدل Fable 5 که ۱۵ روز پیش به دلیل «نگرانی‌های امنیتی شدید دولت آمریکا» ناگهان از دسترس خارج شده بود، احتمالاً همین هفته بازمی‌گردد.  اما…</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/farsna/445243" target="_blank">📅 03:36 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445242">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">🔴
گزارش‌های تأییدنشده از صدای انفجار در بحرین
🔹
شبکۀ خبری پرس‌تی‌وی نوشته بعد از حملات آمریکا به مناطق جنوبی ایران گزارش‌هایی از شنیده شدن صدای انفجار در بحرین دریافت شده است.
🔹
هنوز منابع رسمی این گزارش‌ها را تأیید نکرده‌اند.
@Farsna</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/farsna/445242" target="_blank">📅 03:22 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445241">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PThFxHNPN4hn2cwD-kgh7SiMznU_KuuLWsV77KjkSM513Pl3zYAzpy9Q2_MaAJ3jdq9VojYjGD0-Lf2zWs8nRWUt9xhk_pbE4N1BsdCzHQ_nZzrGIWVWfa7IzIvRz1OQb-456fYJ_JrPOD79TLNcPGlNC1qrnb1MlHyHHd4QM2q8tyPMvZDOGD7t7NW64gOkyGnPpqiDWQNmjmwPp-NC7dviH22lVdFSt_d2Mx5H4ML8tgLu6k01-SKuYhpYVY8Q9TXIfMd7utThIRi1FdEr6VsTlE2fj6AX07U83n0McjR9xNwKBI8kQBY3lU96U1hmzroTbQEAOYDiuU7ERdWGrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ تأیید کرد آتش‌بس با ایران را نقض کرده است
🔹
رئیس‌جمهور آمریکا دونالد ترامپ در پیامی در تروث‌سوشال تایید کرد که ارتش این کشور به اهدافی در داخل ایران حمله کرده است.
🔹
او نوشت: «هواپیماهای ایالات متحده همین چند لحظه پیش، به دلیل نقض دوباره‌ی توافق آتش‌بس، انبار‌های موشکی و پهپادی و همچنین سایت‌های راداری ساحلی ایران را هدف قرار دادند!»
🔹
وی در بخش دیگری از این پیام نوشته است: «ممکن است زمانی فرا برسد که دیگر نتوانیم منطقی رفتار کنیم و مجبور شویم کار بسیار موفقی را که آغاز کرده بودیم، با ابزار نظامی به پایان برسانیم.«
او مدعی شد: اگر چنین اتفاقی بیفتد، جمهوری اسلامی ایران دیگر وجود نخواهد داشت».
@FarsNewsInt</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/farsna/445241" target="_blank">📅 03:05 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445240">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">🎥
روایت تاریخچۀ تأسیس تا حملۀ موشکی دشمن به حسینیۀ اعظم زنجان و بزرگ‌ترین کتابخانۀ تخصصی عاشورا در جهان تشیع، از زبان مهدی رسولی
@Farsna</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/farsna/445240" target="_blank">📅 02:57 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445239">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">🔴
خبرنگار المیادین در غزه: ارتش اشغالگر رژیم صهیونیستی ساختمان‌های مسکونی در شرق شهر غزه را منفجر کرد.
@Farsna</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/farsna/445239" target="_blank">📅 02:44 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445238">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vLdJFhtHZZweJLR9bhaUDUh8fGwuIK6dyqg1THuhm5rNZuxoPcAo0nCQGeg5Fi5qxgSAIp7r4_UkXfcviCbAIz6lFkC2vCBzJaIyHod8IzDyKBiKLmGl491uggIr0jo_-z6VwizDeVqOKTelcQ06p5GXEloInRkmSQ0FaOvmzEThX1KKRw_FOMn-9u4WMXKjjFet-D7X2WznrExDt0oJp3DxYfEbmWvxcfzK255v1NivpZmi8LbSRQDe-KZ33l-AeeRnfZKBeSRaDbmxm8ItlEI1_j_3n9hhN7c6W-Oovn4_G_eDZAiUNahk5o3jWgELrW4Sbez1CZY4yZG1B4wZ7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
تیم‌های صعود کرده به مرحلۀ حذفی جام‌جهانی ۲۰۲۶؛ فقط ۳ جای خالی مانده
@Farsna</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/farsna/445238" target="_blank">📅 02:36 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445237">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T6gJdaP92ikh83Wvcbz85j1DUe1ktRCp0KqJDOk-aT5ICgzBqEUuPqdQgDOJMV_eHSYW8vAleUMzfiGimi9Gbc8r7ieZ17LFb2mhqAVGaBE90olaF56bPECYnJTVlGSBC6IvMm5r2Plw_mrpR56Fdm_ifdlDlg0qaYnTC4HTUrRETpkxtNK82WRnXpOegTeERf7YDRWTNyHcATDjGge6Xk6UKM6jw4wT7-IR-VkJ-MerZ0OLymMiUFtCg1QJUNChByiZH-C0ltv0cFBxDxy4dIb5bqchHqwpDemax1PnGYQd4SP6W8EDfJrcrg7f6b8gqgVTknpxS76ebQapOjLk7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">غنا پیروز بازی با کرواسی باشد.</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/farsna/445237" target="_blank">📅 02:32 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445236">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس ورزشی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZQ0Pabg-UJ6xjjwW26mO5_U3TbBTxFEcI10kiF9ikfzmWHb08INQ3RBDEug-A7H2JcdwssS538191VSj6HWHAL4i5KxKcidbC2RxqFYl7QlY2UoxAIm3i-yBFp5SNvFOVtIhk2A-Jr_tGL9zGOExb4ldu86GUAemAQ2a7c3juXzQVXXM4CLtS3aw7EJrnPpkx5dwHe3CmUdYeRi-1ZAkgjPW-P2zVQFi_NGFsg0GtHXGaO0siCeTSx07PxkWLDoVpl-DLE_E-2-vhQIXSU8k4G8S02PT4Eyp5NlFbWReTCh9GBL47ftBkGPsVFMB8gWhAY4xzvUn4xeXEG9N7CTP8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سه شیر‌ها با صدرنشینی صعود کردند
برد بی‌دردسر شاگردان توخل
پاناما تنها تیم بدون گل‌زده جام
⚽️
جام‌جهانی ۲۰۲۶
انگلیس ۲ - ۰ پاناما
@Sportfars</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/farsna/445236" target="_blank">📅 02:29 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445235">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lVQxl-qKpR8j79H0uLCLO5ZdhRCbiL2a_tK9ZBzcZe8j9GyZ8NIybwrcDUtVQFELq6Yj4blRDCMmWfMeY31aM0rVJz83sPetMo9zhu8rW-Uwd12ph38G2DkKhNfhQU1R9snX0eQ_y4jeqN0AxzJstDripjkGfko6n96Dab3sKW5hJZtOWAEH84nHEjFP1icNskI02dVh6QRD9nkp5yXDGoXM-EDVp3k5q0Obydn8-PPzFX10hsQZ4CzK9qNQIyx4astpbfGbaDz4sQnaPefU_thiWxY9L1aHrh8A21C2uTRblRyu6UQIPPMyQkAW6517s2ThBjTMxhqs0LXR7C1yuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هندی‌ها برای حمل نفت در تنگۀهرمز بی‌کشتی ماندند
🔹
بزرگ‌ترین شرکت پالایشی هند، ایندین اویل می‌گوید، هیچ مالک کشتی‌ای برای حمل نفت‌خام و ال‌پی‌جی در تنگۀ هرمز کشتی اجاره نمی‌دهد.
🔹
یک هفته‌ای است که ترددهای تنگۀهرمز افزایش یافته اما همچنان نهاد مدیریت آب‌راه خلیج‌فارس می‌گوید که مسئولیت عواقب عبور از مسیرهایی غیر مسیر ایرانی بر عهدۀ مالک، بهره‌بردار و فرماندۀ شناور است؛ در دو روز گذشته هم دو کشتی مسیر جنوبی تنگۀ هدف قرار گرفته شده‌اند.
🔹
اسناد مناقصه نشان می‌دهد که محموله‌های قطر، کویت و امارات و عربستان قرار بوده به سواحل غربی هند برسد، اما منابع آگاه بازار می‌گویند، مالکان کشتی‌ها حاضر نیستند ریسک کنند و منتظر روشن شدن وضعیت هستند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/farsna/445235" target="_blank">📅 02:17 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445234">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bWD7-zZXjufcDKLerLs5E0jtVq-A-vvSZzw9kVcYwT7hGDteV2FS-gfxTrwkznHKMh9mhv4GqUiK-qUK86bPx6NOwGZINk3ZUL6fbFXzuiHKI2qT45VXXLnThG8vVgzZdftrbCvkgndygfDLtwj3T8k7sWmxl5LpLxLt9WosbW-J9LRGg1VKDNQhxQdYBpKsejxBRiNwFktXP33EnidIY3IDT8_var5dA_fXEkbduC0TEARmwdy5aA-20DbhC7SUuedtgdXCGW7L-noaaPJ-9Aym39zSrYwjlBrGQbTvYn4oYeoXLr62hVeEf_ms27_0NDc4XzSFHouqVQjHkUMrPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هر نوزاد ماهیانه چند قوطی شیرخشک سهمیه دارد؟
🔹
طبق اعلام سازمان غذا و دارو، جدیدترین سهمیه‌بندی توزیع شیرخشک به کودکان به این‌صورت است:
🔸
کودکان صفر تا ۶ ماه
⤴️
۱۰ قوطی یارانه‌ای و ۴ قوطی غیریارانه‌ای
🔸
کودکان ۶ ماه تا یک‌سال
⤴️
۸ قوطی یارانه‌ای و ۴ قوطی غیریارانه‌ای…</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/farsna/445234" target="_blank">📅 01:51 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445229">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/I7g7lQXqAdkQpHLCJLcgN_EzYdKQ6zdYlDGTLsThRpCCq2UCuKt48DpzJe9x9XzkXlVh0UOmFdYdLJ6k_FgViKQuMKc-elfcPDPiJ0W189oULCPdV3ZgNupSKQJjMpv0BVaVBm5_krSKzpPOGqF7FmKYQpd8uUlOyZF4BBawwA5EBy8nFf3EyuFvCJojWA-FFtuMH1duEAzV_VQsokkmLHdLbFrvPJH5Z-RuW9p-uiCqIHo_h7JUv2lRCUGl6qMaUNvecObqk_jIisg8zlTVIYjPk4BTQf8F3dM74T4MEViGjA0sJH3Cb9_QEEAqu4XtBCVJMCbtjVHpcp_P_qUNoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EACWPyXqxTqyQTrHI3bj5kzsAf5ZiDAfe397Zk1Vv4JXwMBAD5kDermNODTg8FE0-Gy-ypCnp7nwKKCStpQf5rRF9huH1-kF9a4uW5B1tB8Zk5rdoOvUm2AeKYj9VuLvKYEl_CzSJ5mlisfgZfJ0kPZ02UaWpWlg-uy3nzCoS71KwxmHUHfq4X7wDElK9X0LyZp7fLrMZ0C8i7zrxIHpqDowU6WJoQmF4CUwwdvuyq1OVt5twajVTGqHIY7Y2Hr6-P4MCkd0iwpfHuqgc8-y80LLpagbdCYnqr21UnpuUnAHR1xeN0QraZ0XbVMVGMlncVsZ7MB75sU3wyVfqth53w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FM94FpuS57BGqmMKG6LLkk8kASHYhLqIwNXWJbX7Zkz0L4OLqeSRXVzlCyky2Z7cd8vYz72zhn-l_MFDS2wULpneunnXghkkwjnmKBYysac6gKKw9iTthFw4aGR1OkFPsEQhQE30KJ7uVOy8uxp4ZvbvP5BE8BGrpA9Fj4PP2pGsbfkfTEtYvIeY4nwZMhIQCxCPfT1avURw6KVffV4NmSvV7R7u9YTbdSDkkrZZEgD7eukIBLZfT-8CH1Lq6CuatEXT_d9bllflZNGrqqwQ4_e1glkeiVKFB8LS-cskeCAlYMeeQSPM2VrvZMZuCkVxwnhKXE9Ta4jV4MmGovUOlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/F8fPDZCJVyADXEpL_mgDftP1YJ0E2Lf7T4mywHhmAmfXMXTgHfFWOzOp8d6fv0w89ARVbJW0HqjY0UZw_HJDkDU1PGgvS7Nbj-qvspMciuP6y0EsY0ZwMm3wqDRgQwmL7ZGmh_2Hckrzj231oob7HGh2eAa-VH7akBVg01MFm3ydTqsLkTupoZJ9ckyGRR4ABaw4BTgw3HPcFJa9eiVt-8745esi_FUM1P8UGdcVLxGRQSM13DKDJWRx47Wzq8inSXwc5KbxfXSTxzTuriaoxmSW7O57hpN3yDceUXPI6myQBw-JB8tN6biq8Dl_N6kQXjQszmvTmTX4ddZplHw8WQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BifiCfzNcnuSWQ9DQ3bJkNc4nRoG7GEGzo8UXFNXpdxqqugxgF7XQDy7emagF0gWuGO3AoW2cBkFmAjdfbiIgp8dPYWp5ZG2ogRJqfQR_IPz7IA_gb3Mf8RQuoiqiEYdPtabeDsR9yefgpTSjbtPVrKgbBve_fd7iUhI_egSJoGO3SFcVXgNQW6zpcvvyffN71xscbGAV-FsV2KQdnl1KwsTA8US1CmvU6oNqqrPpupx6hfBqvM7Pf9ZhUTasn6ZVPPNsttJie_ZF7fLiVU96AjggmmOl05abIHvh-ggDUGvaVAGaObO8sBtZTnLbq4ewsYEoxX-ek8SwHlJQ_nvgQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📰
دکۀ روزنامه | یک‌شنبه ۷ تیر ۱۴۰۵
@Farsna</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/farsna/445229" target="_blank">📅 01:35 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445219">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KCOC5DBNgUtcZkC38q5WLW8maT7j0Xv7w-S_FdfyCezKjGU13Pl4iMOugJol4fhsFBa-nLH5gU4eHCqgUM5K5OP9dqv1GkcGunZR4Ff7lDabEfoG9tx-eG33LBcXr-wAJsfr3xNqHuYt1tW4b-6dT9ixltBoT79ZEuKe16JrzpkRWzEhEnzCTSwXc8yTzSdyorNSDqh5Nm-1Cu_MpdN285SW19FTrwPjcfpTdnmFfZFRuYK27JLXhP6JxijQE_qsXUgOskQAzg5OFQdz7-V0xH5TL6RlHnq4Wa2LE1vwuWiSzH2_NFF5ZGZ_UXNXIAFL7ELAdSVbUQpcB5p_5RDrpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/p43OcfKJJIgnctXAeHw9zR2F09WYvgHSgpBWE6cF8Je_FPETFNaK960cvP8WTnr7pkU01Jho-ynkWf1ayxo_3A1DzxMrggZR-qIlYTpyPVb3x_T5aOo7aZ1WVrMV4KRzSU7QALwQp833HMCPFmHTCJDio-nLCnzVHgZs-PelMhOtnvCtUqmBJmIOhPcHgNhlc5EOHsRJooLvG4NjL8cUins-exK-d4SNgH4DVfOmQgzz3KwoqvglCVsaiks3FFCAXQTU1IvA5dQnBQwoGmLTznY5ERT2PeihPF8bHwMTrS3lWQvyNZ4SbLVkqX6HbztUFsKFaXDRHMd9waoWEQisPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IwP20np5UVe9weRGkheXnNcG-D_90QmCqWcy2Jy9fN5no1xuFB9QHrAkbZmpfPuDMqQDWCXqkmq60FJoelsFctgz4GZttsJKrwQ0CA1uMz0iKWjW3ye0-1_bt1UIRS9hck2W1pnEWjS5hz4Ob-Y8zzrIkIE8C8EKfx0yn_L39G1IyaSSdSKnM-zNmul8_mhgbLtwcPz4bEfi2s0bZoFgKugn4k0P9Pw_P5Ao0pm2jxhnLI-yAqIYizDZXfiJjXhi14t6QEmzJjj6S7Oi9hwnWbGzYxR0x3xfuA4vt1yQto6RjJB165ynth4Qa3b9UKjUOkWnoVAWzk0ModZGMVCBQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WXthadFNRS1XnDrm0_7hn5uvwjPWqU-6AnMZD4LYIIYhETZBRDH_8fPaeEdtFwovXqsm2lAqKp4R3unay0zCNdG5Hor9Es39izon_5ApgXzzT1J7UL07BH85jtT6fNKuY_yXefcOk2WW2OKvxa3WdciuXtjaHjbf-UHHMYniu7gdBZSkd3LG6uR5ZbBYESq9iyaIcXHqgCDFGWe-9NFcrFhD9EXjGFuFI0VHNHz6Gf3LonFQwm3cAJvCHkC5UpRR1f0VUfvc2L9jqYQ4yoCuY3KBX79yTm2vkh6VnYFZKniNX0XuHpU6kxtHg0vgRyhTUrAtmsTI33k1v04yDsuR9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/shnZn_Vm6sP35UE_oLLx0XRY6zPt5q79ynOVCiKHx3B4YgO4lFqIeM1buroiYNAO4FBr3aFp3qHXI1bXkwNW4mc-jRR7zHY7-_zFLYd-WAf3iIKcmL9xPQL9vDH-PpFLmAichiJphKpGfmXfqYx7ZmzypLjUM3SmEjh7L42uwwFhjecXUPX37R5AbNimZcydsaSrCfLjhC4QQmSR33PwuIA2MNuyKcQ6j0FJ_V8MMEA6N7ZUce3XX8jFITifkfJrSMdoz4R43V_G13BMN3GFx5yOPs0gvzQjr9KpwNWV87W7NuTK3qHxAXiEzEq8eZ8FQPW_SftvTXYYWg_ejKY_pQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OmdQaOH44bXEcRWF2CaLk6SrOeANb0L7Pa2pDMcDt8sf3fcuBuWs91eqNs53IdkCnUWd42cUcmspRuirCpkswC6ZakYBOFMcA21BjNTYKtzt8XIjrcVSpkdOcN8JefDHWuKIkhoxUAgrLXSW39UJ84ae4ZmHPd65-zXD9Yrg3_0KrSbQvVM0UGVpcwOb4oJcrKZcAKjL9qFauRUeXSRU4zg5UP47hFmnnABMYFWAmhk19LYRXSMJvFRuZf05XZYShu69C5ygqdkCCbJviiVHofs6AO-EjbEx56p6LwPRZ0Y81GaITXhEtlQb4uEli-7gV326GMm5kxkSlubyPw9l5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cPTBGX_UnkBRaW-LAwNKqQRQDmwCyYwTECWvMrnsZegHQQtbSC-fd2N12_K8A1QYqEd1U7t2qDwde7dyISQ8DAvBZKehLZPS3AeTce9hLu4aDQpbqAFipAbw5EvHM_kJiP9UnRZO9Un9apzGyy9aIyLSxnFyZIj3G77-sgWPrYTF_CH7pNewFynKyyyy19t6rVIraAibAfHiXTrAm0Iv-XFkeP6ssH-4VgVB02uZRl6bFBjG42UbHi8qUmz32Cwd5B5Cj2NiLy-MTEHWc5taNFbTxU6HumjhpdWVIC_nMXslCuN1N3zBe6uUoDz0XfZWyBv2YvABOhbGTMQNNFAtRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FpJRjLQAzfCkOAAVeYLaf7k30yLdIOvqdJlU-l_jgazaEQquL-n0O5_buPoKkuvpPxYfW6mZzHsy5jqCYatTJpo3AI1Ujtw11YupPNzKQPdjJ9MMHaFIv5VG17owIwly6Q6-R8s0rgQTQxOckgiKygBq_LA7qXAXizOOLdnfRupTPrhXbrcdSdh8f36MD0JpFqOq-kkO8Fqnd6KWaX4uOUDaBHDsWsfD8A3grawREKyKDKfTzfboSSFhOcPUmFh2yKCWXKq90pkUBBlsXFkEGy_Q1PZk7lljarJXVHHORnKmwAHpgxj2WMTydpithcEAF_239hoMkUwnbQC3YPmy2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vfikzOPH4OXxhtlzclVO4oEQxBRukkM4UJ7DqXO75koFaGJY_AtjHQzcRvk-h4JMnPU-VCQDgQqtpyBmST_AFNKnVOW-mVaIdC5BkAppv3thM_Tu29DpqeRtcMnbU1Qiuw5CGTy4Y_CddMjleK8XM28Yf5adsVpcpkMtchXLPyONLMfqOul38FOhNXWQsOft3wH525v-w0PWeAEJAuLrUfxg14terFXrzRKvX7jfjDxGsHLHkSinl1wdoUaxUKVXbV9ym-1rGzHIbq5RDjOFvp86yvS7pS0Uufvcv9UNJHDBq7ZC_p5HHLcUQx-Nif6jDj4kxy12PGSkyMF0GvU95g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eENCkzZjh7eAxdDYUe0uycdXkqRizBy_u7GGuX-ivEC5LljOsED-GfpXYWgGt7fbKC5VyAenk5Wmpj2t6-U5cC4wspCF5U4XxgClqQjhgkUSS3oVkVoxU9M703C14-Fp7JyyIMylmiMxEtjj9vJPgZFnc_WXgeedCGYbe4ZXozBu1BO_y6EUvJMXDLKz7ndGhlq9vi2524uFTguh9bWPXYhDYp8XnmrmCY_3vDs1Aiq8XWF3s8LtVAdTxPq8KqvNPU3Ve_-4nlX5bCqIYS-ShhBho-jDRvKrND7sBdreToaMeaqYJ6c4AmNC5XBe7EF93-Xj_yfFFXLxvRpCl_ZSAA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/farsna/445219" target="_blank">📅 01:35 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445218">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🔴
صدای انفجار در سواحل سیریک و قشم
🔹
دقایقی پیش مردم در سواحل و محدودۀ ساحلی منطقۀ طاهروییه سیریک صدای چند انفجار شنیدند.
🔹
همچنین اهالی مسن در قشم نیز از شنیده‌شدن صدای چند انفجار در این منطقه خبر می‌دهند.
🔹
محل دقیق و منشأ این انفجارها هنوز مشخص نیست.
🔸
جمعه‌شب…</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/farsna/445218" target="_blank">📅 01:21 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445217">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">🔴
صدای انفجار در سواحل سیریک و قشم
🔹
دقایقی پیش مردم در سواحل و محدودۀ ساحلی منطقۀ طاهروییه سیریک صدای چند انفجار شنیدند.
🔹
همچنین اهالی مسن در قشم نیز از شنیده‌شدن صدای چند انفجار در این منطقه خبر می‌دهند.
🔹
محل دقیق و منشأ این انفجارها هنوز مشخص نیست.
🔸
جمعه‌شب پس از شلیک اخطار توسط واحدهای نیروی دریایی سپاه به شناوری که با عدم‌توجه به هشدارها، در صدد عبور از تنگۀ هرمز بود، سنتکام دست به تجاوزات به مناطق ساحلی هرمزگان از جمله در سیریک زد که با پاسخ قدرتمندانۀ نیروهای مسلح کشورمان روبرو شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/farsna/445217" target="_blank">📅 01:06 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445216">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sC0RP7DuUaPvCtoUObHujUuc7wGKzqf8v5SHrs25ZDTAX6iK8P757YoWGYznePO5fqdK7dnqzvAsnez64ZcSCEGxCCbdBCJ2F5D8fC5hru5UhWC-vBfXrvs5l_TKN7gmwhgAChlQ8q99XH93IuYCnfQ-yw9bDBoDNPeRmn4ZV8KQ2v3IcuFvPkrqA4herVuJaWsrjbcGvbPpfHCSCPUza5yw4Sih7B40b8_I-yTJkT7uLD2gnTGlXX670q4CEVX_TxLZquZbTzB3vSC2SyY2GH6GlnKRKYHY4LHSPwbOfyk7_lHpnWRWG98eXQhOvd9iQr97GqqMuztGOG1w9T5c5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رئیس‌جمهور لبنان خواستار خروج اسرائیل از جنوب این کشور شد
🔹
دفتر ریاست‌جمهوری لبنان در بیانیه‌ای از گفت‌وگوی تلفنی میان رئیس‌جمهور این کشور و ترامپ، رئیس‌جمهور آمریکا خبر داد.
🔹
در این بیانیه تصریح شده رئیس‌جمهور لبنان در این تماس ابراز امیدواری کرده که واشنگتن، اسرائیل را برای خروج از اراضی اشغال‌شده در جنوب لبنان تحت فشار قرار دهد.
🔸
با وجود این، در بیانیۀ شب گذشته وزارت خارجۀ آمریکا دربارۀ امضای توافق چارچوبی میان بیروت-تل‌آویو، حکایت از آن است که کاخ‌سفید دست اسرائیل را برای ادامۀ انواع تجاوزات در لبنان باز گذاشته است.
@Farsna</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/farsna/445216" target="_blank">📅 00:53 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445215">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">قطع برق تعدادی از مناطق تهران؛ دلیل مشخص شد
🔹
تعدادی از مناطق تهران از ساعاتی پیش با قطعی برق مواجه شدند.
🔹
پیگیری فارس از توانیر مشخص کرد، مشکل فنی در یکی از پست‌های ۲۳٠ شرق تهران علت قطعی برق است.
🔹
هم‌اکنون تیم‌های عملیاتی و فنی برای رفع مشکل در محل پست…</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/farsna/445215" target="_blank">📅 00:40 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445214">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">کتاب آه</div>
  <div class="tg-doc-extra">قسمت ۱۳</div>
</div>
<a href="https://t.me/farsna/445214" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">قسمت ۱۲ – کتاب آه</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/farsna/445214" target="_blank">📅 00:35 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445213">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">آسیب‌شناسی گفتمان مذاکره در فضای عمومی؛ از اختلاف‌نظر تا شکاف اجتماعی
🔹
در فضای کنونی جامعۀ ایران، دو دیدگاه کلی دربارۀ مذاکره با آمریکا شکل گرفته است.
🔹
وجود این دو نگاه در یک جامعۀ متکثر، نه تنها طبیعی، که به مثابۀ یک فرصت برای پویایی فکری محسوب می‌شود. اما آنچه این وضعیت را از یک اختلاف‌نظر سالم به یک تهدید اجتماعی تبدیل می‌کند، نه خودِ اختلاف، بلکه کیفیت و ادبیات گفتگو در این‌باره است.
🔹
شکاف اجتماعی زمانی شکل می‌گیرد که این اختلافات از چارچوب استدلال و نقد خارج شده و وارد حوزۀ تخریب، طعنه و تسویه‌حساب‌های روانی می‌شود. در این مرحله، دیگر هدف رسیدن به حقیقت نیست، بلکه تحقیر طرف مقابل و «تثبیت برتری خودی» هدف قرار می‌گیرد.
🔹
نکتۀ روانشناختی مهم این است که در چنین فضایی، عقل و استدلال دیگر نقش چراغ راهنما را ندارند. در عوض، احساسات اولیه و پیشداوری‌ها تعیین‌کنندۀ موضع فرد می‌شوند و سپس عقلِ ابزاری، صرفاً برای توجیه و اثبات آن حس به کار گرفته می‌شود؛ که این دقیقا نقطۀ مقابل روش قرآنی و توصیه‌های رهبری است.
🔹
نکتۀ راهبردی این‌جاست که بزرگترین منتفع از شکاف‌های سیاسی، دشمنان خارجی هستند؛ هرگاه گفتمان داخلی از مسیر نقد منصفانه به سمت دشمنی درونی و تهمت پیش رود، عملاً دشمن اصلی از صحنه خارج شده و انرژی جامعه صرف درگیری‌های درونی می‌شود.
🔗
اما برای جلوگیری از تبدیل این اختلافات به شکاف، چه راهکارهای وجود دارد؟ شرح کامل گزارش را
اینجا
بخوانید.
@Farsna</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/farsna/445213" target="_blank">📅 00:27 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445212">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/il_yC0flO-uQCzZXCTkgL-Pm0q6ZZBTiYwKPV7PDZZmdbbml2WINNp9tk7u1YvdXlcBi7cxU_Eo6T90db_SESeZOOusEJ0PMgKdIUEWUrh9NVyBFPXgBXDnIGwfs8DwNgZ-4hX50ZY-ni7Kqvl2e93r94SG8Sc7YKnteaFaQaQ6Y4Fz5Z_1nlgQ3Huh0aozAVbE7izwlBy-JUC4lyZw2_GdwnYfrCA7EZsGjpGLpu5cFAKC0bWdtYuXeyABQaY_72f3TnieXG4vUfxDHItBnQf4RFZOmscUCd4-oPXp5qX6mvGr6uWuFN4QQJ7Il8uvYKvMvmz3qOTs15JCBmQW1nQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سزاوارتر در تحمل سختی
🔹
امام صادق(ع) به همراه گروهی از یاران خود از مدینه به مقصد کوچکی در خارج از شهر حرکت کردند. در میان راه، بند کفش امام(ع) پاره شد. ایشان کفش را به دست گرفتند و با پای برهنه به مسیر خود ادامه دادند.
🔹
یکی از یاران امام به‌نام «عبدالله بن یعفور» با دیدن این صحنه، بلافاصله بند کفش خود را باز کرد و آن را به امام تقدیم کرد تا کفش خود را درست کنند.
🔹
امام صادق(ع) نپذیرفتند و فرمودند: «خیر، اگر سختی و ناراحتی وجود دارد، خودِ صاحب کفش به تحمل آن سزاوارتر است. معنا ندارد که حادثه‌ای برای یک نفر پیش بیاید و دیگری متحمل رنج بشود.»
#حکایت
@Farsna</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/farsna/445212" target="_blank">📅 00:10 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445211">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">بیانیه جمعی از اعضای مجلس خبرگان درباره تحولات اخیر و مذاکرات
🔹
جمعی از اعضای مجلس خبرگان رهبری در بیانیه‌ای با اشاره به پیام اخیر رهبر معظم انقلاب اسلامی و تحولات اخیر، بر لزوم رعایت خطوط قرمز نظام در مذاکرات و هوشیاری در برابر ترفندهای دشمن تأکید کردند.
در بخشی از متن بیانیه آمده:
🔸
ضمن تشکر از مسئولان، به‌ویژه مذاکره‌کنندگان محترم، که بنا بر تعبیر رهبری معظم از سر دلسوزی و حسن‌نظر به دنبال احقاق حقوق ملت ایران و جبهه مقاومت هستند، انتظار داریم که با ملاحظه تجربه‌های مذاکرات خسارت‌بار گذشته، کاملاً مراقب ترفندهای دشمن فریبکار و بدسابقه باشند و توجه داشته باشند که رعایت خطوط قرمز رهبری واجب شرعی است و تخطی از آن‌ها به‌هیچ‌وجه جایز نیست.
🔸
موضوع تعیین متجاوز و معرفی عاملان مهدورالدم جنایت‌های کم‌نظیر جنگ تحمیلی اخیر، به‌ویژه رئیس‌جمهور جنایتکار آمریکا و نخست‌وزیر پلید رژیم صهیونیستی، و مجازات آن‌ها و انتقام خون امام شهید امت، به‌هیچ‌وجه مورد اغماض و بی‌توجهی قرار نگیرد و بر هر مکلفی که به آن‌ها دسترسی پیدا کند، واجب است که این جنایتکاران را به درک واصل کند.
🔸
مطابق تعهد مسئولان محترم به رهبری و مردم، انتظار می‌رود که هرگونه پیمان‌شکنی و نقض بندهای تفاهم‌نامه سریعاً پاسخ داده شود.
🔸
بنابر رهنمود واجب‌الاتباع رهبری معظم (مدظله‌العالی)، حقوق هسته‌ای کشور نباید مورد بحث و مناقشه قرار گیرد و بایستی از دایره گفت‌وگوها خارج شود.
متن کامل بیانیه و اسامی امضاکنندگان را
اینجا
بخوانید
@Farsna</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/farsna/445211" target="_blank">📅 23:56 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445210">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">ویروسی که از آفریقا تا اروپا را درگیر خود کرد
🔹
چند روزی است که نام «ابولا» بار دیگر به صدر خبرهای جهان بازگشته است.
🔹
این‌بار با ثبت نخستین مورد ابتلا در اروپا از زمان آغاز شیوع جدید، دوباره توجه نظام‌های بهداشتی جهان را به خود جلب کرده است.
ویروس ابولا چیست؟
🔹
ابولا بیماری ویروسی شدیدی است که نخستین‌بار در سال ۱۹۷۶ در نزدیکی رودخانه‌ای به همین نام در جمهوری دموکراتیک کنگو شناسایی شد.
🔹
دانشمندان معتقدند خفاش‌های میوه‌خوار مخزن طبیعی این ویروس هستند و بیماری می‌تواند از طریق تماس با حیوانات آلوده یا افراد مبتلا به انسان منتقل شود.
🔗
علائم این بیماری را
اینجا
بخوانید.
@Farsna</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/farsna/445210" target="_blank">📅 23:38 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445209">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c0d9e2eb96.mp4?token=vwrYu-zzVcie4RRsU8SgR-0GauYTsKNo5O8UlliC-F5xGOOrBH1Yi62qhsZ8zwmZJHeNeTwQT0FnEdaDd7G806g49gCpnaNRcx7IPhp3nMlIyFikq8Q4GV5L1X__9MutyxZSm8yUY5GBxL1o1ws7cD1eYUciHFRyzOpXRwTLxQ21PaWUh_imVAnRikBmeiI-_-AGN43t9yrgqlDjF2Lea-CRUEe64Q4FNt5YVyv3f_xARWnrCMjCl5rynWhX4ERNbOMqthPefL4qmAwPey3uh-yUxOlw7MFmP48NLjmur6xi5G6X2Og1OvdcpGom6aiTX4RHKQYMF2tRB1ClASRxNg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c0d9e2eb96.mp4?token=vwrYu-zzVcie4RRsU8SgR-0GauYTsKNo5O8UlliC-F5xGOOrBH1Yi62qhsZ8zwmZJHeNeTwQT0FnEdaDd7G806g49gCpnaNRcx7IPhp3nMlIyFikq8Q4GV5L1X__9MutyxZSm8yUY5GBxL1o1ws7cD1eYUciHFRyzOpXRwTLxQ21PaWUh_imVAnRikBmeiI-_-AGN43t9yrgqlDjF2Lea-CRUEe64Q4FNt5YVyv3f_xARWnrCMjCl5rynWhX4ERNbOMqthPefL4qmAwPey3uh-yUxOlw7MFmP48NLjmur6xi5G6X2Og1OvdcpGom6aiTX4RHKQYMF2tRB1ClASRxNg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
میدان انقلاب تهران در ۱۱۹ روز حماسه
🔸
امروز روز وحدتِ میهن است
🔸
هر اختلاف از جانبِ دشمن است
@Farsna</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/farsna/445209" target="_blank">📅 23:21 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445208">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8645d7b23a.mp4?token=ZAhyyT3s6UKsNg1hf84GADXt21YDCaAmF7wlqFYulzrwu4B7IBYG4q8nltHGFjDVtBsnP1hQNZ9djvpv60E04pe6rR4i4CITbOxA8rQfYnzdjtSufNnO1fkdvqhdRpnFXUSxxpyhqgyAbTve5DRHy2XNpL4DGKTE-40o0EoKwpbewC7whVALcnp5zzc90tTaP7Rp7Ea8MEOyEEP37WXGPeBaosfO6t_pgDIb_dxzv9VZF2pxBkqrjeOpBV01sE_a1uWf9GfPl6sME7HMZ4UFY5MFfkBFCmsSR5NQSK2ZuFos6q9xP7Ym8FLbQCRrhv9lwPUHWVkUV8HlzfB86EIqsA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8645d7b23a.mp4?token=ZAhyyT3s6UKsNg1hf84GADXt21YDCaAmF7wlqFYulzrwu4B7IBYG4q8nltHGFjDVtBsnP1hQNZ9djvpv60E04pe6rR4i4CITbOxA8rQfYnzdjtSufNnO1fkdvqhdRpnFXUSxxpyhqgyAbTve5DRHy2XNpL4DGKTE-40o0EoKwpbewC7whVALcnp5zzc90tTaP7Rp7Ea8MEOyEEP37WXGPeBaosfO6t_pgDIb_dxzv9VZF2pxBkqrjeOpBV01sE_a1uWf9GfPl6sME7HMZ4UFY5MFfkBFCmsSR5NQSK2ZuFos6q9xP7Ym8FLbQCRrhv9lwPUHWVkUV8HlzfB86EIqsA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سردار حسن‌زاده: مسیر اصلی مراسم تشییع رهبر شهید در تهران، خیابان دماوند-خیابان انقلاب-خیابان آزادی-اتوبان شهید لشگری-اتوبان آزادگان است.  @Farsna</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/farsna/445208" target="_blank">📅 23:13 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445207">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🎥
سردار حسن‌زاده: ما نمی‌توانیم در مراسم وداع با رهبر شهید توقف جمعیت داشته باشیم
🔹
برنامه‌ریزی این‌گونه است که مردم از یک نقطه وارد مصلی شوند و پیکر مطهر را ببیند و ظرف ۱۵ دقیقه از آن بخش خارج شوند. @Farsna</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/farsna/445207" target="_blank">📅 23:09 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445206">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1ce2fd43a9.mp4?token=EpJZponimlXfTc3KvWyDeaC6nlxyLjRy6WB_Zf-fb9V7K22_Pwyh_OBy-wgg2n9ggod9EzZeZMpDTHAij-nFR4XDY6CNWs3BPPCmpwcVYrBzLumX-csDzKtRisgF1sOtqnFDnRD0vqXHSo9EZ0OQeVNX40L9n-m-3zUdElTssTfsFrKZLlnWl1OOPeY-BHbcjcr_HfNyq0BSbE4pdJIILrkoIn6UjXnQamYXZDmZlRpMsLtjkvOb6p756ZcALo9-e_PiPwT5btxvrPPWZY7if6XhhAbYxiLYw260v_MhLl6o5pSm0Ik4zOqbLP3kOC3Yxai8E67gSqXto-YazV1I5w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1ce2fd43a9.mp4?token=EpJZponimlXfTc3KvWyDeaC6nlxyLjRy6WB_Zf-fb9V7K22_Pwyh_OBy-wgg2n9ggod9EzZeZMpDTHAij-nFR4XDY6CNWs3BPPCmpwcVYrBzLumX-csDzKtRisgF1sOtqnFDnRD0vqXHSo9EZ0OQeVNX40L9n-m-3zUdElTssTfsFrKZLlnWl1OOPeY-BHbcjcr_HfNyq0BSbE4pdJIILrkoIn6UjXnQamYXZDmZlRpMsLtjkvOb6p756ZcALo9-e_PiPwT5btxvrPPWZY7if6XhhAbYxiLYw260v_MhLl6o5pSm0Ik4zOqbLP3kOC3Yxai8E67gSqXto-YazV1I5w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سردار حسن‌زاده: برای مراسم تشییع رهبر شهید انقلاب در تهران حضور حداقل بین ۱۲ تا ۱۵ میلیون نفر برآورد شده است.  @Farsna</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/farsna/445206" target="_blank">📅 22:59 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445205">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">عارف: تشییع رهبر شهید انقلاب یکی از مهمترین حوادث قرن ۲۱ است
🔹
معاون اول رئیس‌جمهور: باید مستندسازی، روایت‌سازی و پوشش رسانهٔ مناسبی و در ابعاد جهانی از مراسم انجام شود.
🔹
با توجه به گرمای هوا، لازم است تمهیدات مناسبی برای ارائه خدمات مختلف به مردم در نظر گرفته شود و کادر درمان نیز در آمادگی کامل باشند.
@Farsna</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/farsna/445205" target="_blank">📅 22:56 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445204">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7d8d91acc8.mp4?token=WoATxA4DAl4yuK4F-qIiBp4bf-rpdnz0in9BCZnFzHDEsF1iFKhYv91gD5aScWEH9CenbX6Kg65EY5k05Owcg1eQILMVhg3Q5sUdQARfuhrJVGDjylPKDik0apDy7-nbW249s153C8t1rPPBjGdo1OdX8a_iexQTwYqZL1x9ad85kkoiNSw3py7jeLDJiebFvvm6JQhckIJDApofnRNycGaGoe6cVJ6YxKdEJOGKrrIosKqoyH_fPGOXVN7VL3_ORKGsJ1KLFGW_3qWDyItt-dDNVAZurKrVIHeCIXMnUqXj1RGLouV5_8EfUZpmSnTDi37kMyQ_F1iP5ib2ffFOxw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7d8d91acc8.mp4?token=WoATxA4DAl4yuK4F-qIiBp4bf-rpdnz0in9BCZnFzHDEsF1iFKhYv91gD5aScWEH9CenbX6Kg65EY5k05Owcg1eQILMVhg3Q5sUdQARfuhrJVGDjylPKDik0apDy7-nbW249s153C8t1rPPBjGdo1OdX8a_iexQTwYqZL1x9ad85kkoiNSw3py7jeLDJiebFvvm6JQhckIJDApofnRNycGaGoe6cVJ6YxKdEJOGKrrIosKqoyH_fPGOXVN7VL3_ORKGsJ1KLFGW_3qWDyItt-dDNVAZurKrVIHeCIXMnUqXj1RGLouV5_8EfUZpmSnTDi37kMyQ_F1iP5ib2ffFOxw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سردار حسن‌زاده: در مصلای تهران بر پیکر رهبر شهید انقلاب نماز اقامه خواهد شد.  @Farsna</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/farsna/445204" target="_blank">📅 22:51 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445203">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2cb911549f.mp4?token=rneMZhhB4ptpKmMORuDjO7ZFBuEZB3rfYDS2vQ8MSCDYVbuOhIaw6dSixM1JnwPME7GcWkphG61GesLo89t01A3CfAqMkGiVvc1Ful3d67V7YCSZV7NXJkk3M762ixbNvW467fuHtzrcZ7ayctj_ONzgfXtzcJ0iQopbsrQtpxuXN8pqcClcFKOeK2F3t3r4ucdn29YU8Un5TWfQMdC-Z0BHUeND6qbpKImtdV_05BvZHydwv7uRPhCQCbvbrTnEo-0A0vuN7kxtGRJ8WrReUP9QksknwDLpkCeyE6ca_TAqKC_3wkPpKUU0Gw5kWYFJ_8ZPBK_XhPoOkWoGxMLdeQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2cb911549f.mp4?token=rneMZhhB4ptpKmMORuDjO7ZFBuEZB3rfYDS2vQ8MSCDYVbuOhIaw6dSixM1JnwPME7GcWkphG61GesLo89t01A3CfAqMkGiVvc1Ful3d67V7YCSZV7NXJkk3M762ixbNvW467fuHtzrcZ7ayctj_ONzgfXtzcJ0iQopbsrQtpxuXN8pqcClcFKOeK2F3t3r4ucdn29YU8Un5TWfQMdC-Z0BHUeND6qbpKImtdV_05BvZHydwv7uRPhCQCbvbrTnEo-0A0vuN7kxtGRJ8WrReUP9QksknwDLpkCeyE6ca_TAqKC_3wkPpKUU0Gw5kWYFJ_8ZPBK_XhPoOkWoGxMLdeQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سردار حسن‌زاده: در مصلای تهران بر پیکر رهبر شهید انقلاب نماز اقامه خواهد شد.
@Farsna</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/farsna/445203" target="_blank">📅 22:50 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445202">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d8f80eb42d.mp4?token=P8OxWS3H-JUmV-yrVMWecTii1F9DJVEI2lVrjkwz7Wd9wWuk0XkZf1ZODrQIDxVgJr0P30kPsxJhGRN1dpWLAB7uO9b_mODq31-vYSHy_Ft1uPuRP81jLFpfkeuSXN9ECk6tLyATfOu6vzfGfhFeJy4pxkVZr1wYon4pMceDw3Md3Eed56dKYvCS-kRKcwkFQbkdm-UhvAZDp1WgI0G_BdoGUJy-LT6gHb30p5zu_5olq9nokwBkzFUo0d7DAr2PqsaXZ6P6PvtKHTl0PeSE-tj_k2Rccv3sq8Mf4SBm4xbFHuBcdEVJPgFUlbMoiOhuaYKPsRpZckvCLyg66SaoFA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d8f80eb42d.mp4?token=P8OxWS3H-JUmV-yrVMWecTii1F9DJVEI2lVrjkwz7Wd9wWuk0XkZf1ZODrQIDxVgJr0P30kPsxJhGRN1dpWLAB7uO9b_mODq31-vYSHy_Ft1uPuRP81jLFpfkeuSXN9ECk6tLyATfOu6vzfGfhFeJy4pxkVZr1wYon4pMceDw3Md3Eed56dKYvCS-kRKcwkFQbkdm-UhvAZDp1WgI0G_BdoGUJy-LT6gHb30p5zu_5olq9nokwBkzFUo0d7DAr2PqsaXZ6P6PvtKHTl0PeSE-tj_k2Rccv3sq8Mf4SBm4xbFHuBcdEVJPgFUlbMoiOhuaYKPsRpZckvCLyg66SaoFA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مردم گرگان در شب ۱۱۹ نیز پای عهد خود ایستادند
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/farsna/445202" target="_blank">📅 22:42 · 06 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
