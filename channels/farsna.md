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
<img src="https://cdn4.telesco.pe/file/KnTFg2ZFnQ4Ir25b0dyBVvYDai0oY_91N94pbqHkaJgp5Qd2QerA5nflYq94NYsdPPeNIjHyM-o69EUL0bpWpwx02iX-xioMMrUcc3EEloq2kznU9uAqvjQz7uA5bS2_crLWmo2vlPtxCKjVYLmi94cWZS_1tWtP7uNIihLBQyMbuAX6Elf3Wxg4Pb-PoSuXGq9LE5KlgnaP_nGEfm_MfqKogEEEgOincI6Hwjjpn0iVrKc9I14MrJPTyFzI4UIvVIkuWcbgwBa6IIBHv8XwAss70ZsfyRmKsEGolHAjPKkxWeKS_mRNcUHUiX-smxn1cigeWjYZGHXqxdF-DdGsUQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرگزاری فارس</h1>
<p>@farsna • 👥 1.83M عضو</p>
<a href="https://t.me/farsna" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 حقیقت روشن می‌شود‌‌تبلیغات@Farsnews_adsارتباط@FarsNewsفارس‌پلاس@Fars_Plus‌ورزش@SportFarsجهان@FarsNewsIntعکس@FarsImagesپیام‌رسان‌ها@Farsnaاینستاگرامinstagram.com/fars_newsتوییترtwitter.com/FarsNews_Agency</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-04 10:35:22</div>
<hr>

<div class="tg-post" id="msg-437848">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">‌ بیش از ۲۷۰ نماینده در انتخابات هیئت‌رئیسۀ مجلس شرکت کردند
🔸
مجلس در حال حاضر ۲۸۵ نماینده دارد.  @Farsna</div>
<div class="tg-footer">👁️ 820 · <a href="https://t.me/farsna/437848" target="_blank">📅 10:31 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437847">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">قالیباف رئیس‌مجلس ماند
🔹
محمدباقر قالیباف با رأی بالای نمایندگان، برای هفتمین سال متوالی بر صندلی پارلمان تکیه زد و رئیس‌مجلس ماند.  @Farsna - Link</div>
<div class="tg-footer">👁️ 1.38K · <a href="https://t.me/farsna/437847" target="_blank">📅 10:27 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437846">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TeeSlvm9D-oiDH5ror8zW4pbaau7I8ASDsn3bwUepgw2b0k-oGl_mDth-Z-E8ksHVQOdChDcctS-ifkOq9spcuLgs4iWvvwD1gPcHCOt3lTFhdy7RQuE3wRy9uPff_j-8UakHcqDotEdGkb1ciaV23N9GJGk6yWyy86rRCyxaKUQC0bkgLMjncnCjPrppcTzdg5YZkGdNdwsOysdcoCrTnxMTdjzTGMyTzThE1VgiojWfAlzWYYwo48vKAgxJg7ncKBPjE18l_HPpOLadQYpAZtZl8ber_QtQTL4MNypIGRIvDCXA1g9aIG07Jql92PSXqZosSF8n_7du6cSljwQPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌ انتخابات هیئت‌رئیسه مجلس برگزار شد
🔹
انتخابات هیئت‌رئیسه مجلس که از ساعت ۷:۳۰ صبح امروز آغاز شده بود، دقایقی پیش پایان یافت.
🔹
این انتخابات به‌صورت حضوری و با رای مستقیم نمایندگان برای انتخاب ۱۲ عضو هیئت‌رئیسه شامل یک رئیس، ۲ نایب رئیس، ۶ دبیر و ۳ ناظر برگزار…</div>
<div class="tg-footer">👁️ 2.59K · <a href="https://t.me/farsna/437846" target="_blank">📅 10:18 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437845">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ho8Jq-oGy9IxSFS5rkdgMfn_joI4dx5LvGli8sTNZmofGo5cegDrZ1Qbnucf7itVYWx6X_Ha3XOPkWvsCeYYyDRMJYGg4KVDJv7Iy4385_pIt1_p74YCOQ5bfeUQRzKJUL3ItmtjSoMVi4otOLnpCymz77ctweDPAhEDJyiC7PI3_aE3lcKLFPUdjEVeaxVvVluVXfBykU1eSVrLm8O9GdidpdsW8xntrav2IA67dqNqg1QYPth3tIscG9qbA_4Eou9j-xJ5AS2YDFXUA40qDNHukVRVxZzM1IROZ7f4z8oZgnkwXWwgG2mHW-FxFnZOrW6iBjYabyJ2MsfP0SvjdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
احیای بخش جنوبی دریاچۀ ارومیه پس از ۲۰ سال  @Farsna</div>
<div class="tg-footer">👁️ 2.38K · <a href="https://t.me/farsna/437845" target="_blank">📅 10:15 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437844">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OgWbsDx3T-ipORmRcRaWp8_eWsKcuRRzSmF5RNAQo-DSHiCevrst7EDdDUEic78FgWVk1zic8lzQeIuYQ5iviqz_I3JMqvoDUOkmtuYeIYboaDAnFdWkHzvlrbBNNM8ncbACFvQ5j-g_Tcsf22jiWKp7MMZFEQYq7vFJ8DbL1JXlHjOB3lpQB5J8pdao01cdcvVIhTwfjUDFsNNQTRjyIMQfVy4XakTIBhnY5aSg4Z0m5qEln3h5q3R02bRbIHfUPhJeYXY20hS7mGgD0wGsbuyqqjAZ-jwJ2Xmuy-x-q6lTbyY4gJiEzTFfuoKl2C99vxYECs7NGiwPR6R9EMPsug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مناسک حج آغاز شد
🔹
همزمان با فرارسیدن یوم‌الترویه (روز آماده شدن برای آغاز مناسک حج)، فرآیند انتقال زائران حج به عرفات از ساعاتی قبل کلید خورد و مناسک حج تمتع امسال وارد فاز عملیاتی شد.
🔹
۷ هزار زائر اهل سنت کشورمان با اتوبوس‌ها از هتل‌های محل اسکان خود خارج شدند و حدود ۲۳ هزار زائر دیگر هم امروز به مشاعر مقدسه منتقل می‌شوند تا از فردا خود را برای دعای عرفه در صحرای عرفات آماده کنند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 2.8K · <a href="https://t.me/farsna/437844" target="_blank">📅 09:58 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437843">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lpU5X9nqatUDjrgVJyzYVjxf2ocqdCDDN7t2lhRPTDdv20zAn_c2Qwv99O03JaUFauDBnWZMqnw72kG70VrOPcwI9ATDboqm43X76eN_ljAIP2qz7QxUTCqDS3kJRphIigJlxlUmCyG43mBtaDIZZxAZQFKh-taltiCFLXffiuQYFtTgMtHG-AVph-TxngENQZc-v6C_M8D22dLuw4b8kGHlcChDBhWZ015GyxJwuPQhRSyoFvz9R0z_tGJqhFP2j2ws9Tm91NQypdF6G69EnVyfeLc-AtsTZOjw4hnOnDRbxiPu1FJQ7kyarLo1hgOwz6A5VQeZWwnrwn_JB3STvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌
🔴
سخنگوی وزارت خارجه: در مورد مباحث هسته‌ای تکلیف خیلی روشن است؛ ما عضو NPT هستیم و حق داریم از انرژی هسته‌ای برای مقاصد صلح‌آمیز استفاده کنیم. @Farsna</div>
<div class="tg-footer">👁️ 2.54K · <a href="https://t.me/farsna/437843" target="_blank">📅 09:56 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437842">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pCzdWE1_0TeoT9wkEi0ErpnC19YCAxXt7iSVkpfuadKL3NE6BllYFtVXLyY0IMnBDDHbKpMArKlnhhRP8bjK1-yLuM-HdVqswW4IlF5PRg4FGBC3ji6l8DgSOiTI_utH01lmHjtjz1tIjDkcZmq6YJD3i3MM-tZVUYOKZekCkjLYKAHs_H1gUYpxHugVQ3pdU_hzhD3XMYKr0dgPhkZK5z13vKcP2C-xdITBnULn_gVmAMY42yWm8dbRL6-hE1rb6kpisKsnbcOboFClkYtaBu4Bfa5JGBoUMCCzvBGi0TYyJoj71Jy9MrqZyhazCppmJ-I5aV8yL9Y_YMPXQodMlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فرودگاه‌های فعال کشور به عدد ۲۰ رسید
🔹
سخنگوی سازمان هواپیمایی: تاکنون ۲۰ فرودگاه کشور پس از جنگ تحمیلی سوم بازگشایی شده‌اند.
🔹
فرودگاه تبریز نیز تا یک هفتۀ آینده فعالیت خود را از سر می‌گیرد؛ فرودگاهی که به ۹ مقصد خارجی از جمله استانبول، بغداد، دبی، باکو و هامبورگ پرواز دارد.
🔹
فرودگاه‌های مهرآباد، امام خمینی، مشهد، شیراز، اصفهان، اهواز، کرمانشاه، ارومیه و رشت از جمله فرودگاه‌هایی هستند که تاکنون بازگشایی شده‌اند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 2.64K · <a href="https://t.me/farsna/437842" target="_blank">📅 09:50 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437841">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kw4O8JHUKFAibR_TRwWgBgd4y7AYnh1-zUrxgsGbIY-Nf9AdhBoQ1RjJ3iBJIbniseHRVYA4aC5eOGolF-94__9uEtopEeOV3IcmC_SFs11aDV8_ynHwJesC58GOGpuxTRn9a4nfm7Wjhd6iRVUwXNl2bmviMGpWsrnnccXhqCHy9medBEy5tYPP9XoULfx9JO87J7kcbg7ASX2rWRA7BhBbad3xuKppuEs8Uz1bLlx5_oU7l-YezhFVJ-RxGuwymPvWl2ETX_bJSSHxsMQESDXLtcXLs8N40HQjktzlXMP9GK597TXe0EAsltomwSlXlEkAdj02ioCTEo72sTlI8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
سردار قاآنی: مقاومت امروز همچون خرداد سال ۶۱ و ۷۹ زمینه‌ساز آزادی قدس شریف است
.
@Farsna</div>
<div class="tg-footer">👁️ 3.25K · <a href="https://t.me/farsna/437841" target="_blank">📅 09:37 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437840">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">‌ پاپی‌زاده: جلسۀ انتخابات هیئت‌رئیسۀ مجلس فردا حضوری برگزار خواهد شد
🔹
نماینده دزفول در مجلس: نحوۀ رأی‌گیری انتخابات هیئت‌رئیسه به وسیلۀ صندوق‌های رأی‌گیری الکترونیک خواهد بود. نمایندگان احراز هویت می‌شوند و سپس رأی می‌دهند. @Farsna - Link</div>
<div class="tg-footer">👁️ 3.16K · <a href="https://t.me/farsna/437840" target="_blank">📅 09:36 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437839">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WdjGnyCtVnM1gTnZTwBJ8tshM2s8mzxiCXKymo1-bA9Is15pzwehyupVxkU0YATma7SLydaZSQX3dGmp-HeQUxDyAFZuIAQ1O4xVyn_1GJacJXL0ieS6EbMRM44uv3OK7v_3I1eXFZXWJcjfSwKYNQbWKc76gMTTzMppjvHJ2LXSkHDPVj2X815F7Fzka8WdPRLbsU_6CbhWGXS0NpZ-V4SUN6W1_kf1Gfd3yJHEHhSLkjBHd8_Fdxrb_a2z1J6Q3J1X1gGVk8p7DErY2PFAXUIDf5ChMslE1IQwohBw9SWQcflCgROeY_NK6HKadx4QhGdESLpVSU9YXu3HQcCHsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ماجرای نامهٔ شبانهٔ وزیر کار دربارهٔ تأمین اجتماعی چه بود؟
🔹
انتشار نامه‌ای از وزیر کار به وزارت اقتصاد از لایحهٔ «ایجاد نظام جدید تأمین اجتماعی» پرده برداشت که ابعاد آن، نگرانی‌های عمیقی را در جامعهٔ کارگری و بازنشستگان ایجاد کرده؛ به‌ویژه آنکه این لایحه بدون اطلاع قبلی و مشارکت نمایندگان کارگران و کارفرمایان در حال پیگیری است.
🔹
براساس این طرح، ساختار مالی تأمین اجتماعی به‌طور بنیادین تغییر می‌کند. بر این اساس، حق بیمهٔ سهم کارفرما از ۲۳ درصد به ۷ درصد کاهش می‌یابد و مجموع سهم پرداختی بیمه‌شده و کارفرما به ۱۴ درصد می‌رسد.
🔹
۱۶ درصد کسری حاصل از این کاهش، قرار است از محل درآمدهای مالیاتی عمومی کشور تأمین شود. همچنین، تجمیع تمام منابع در خزانه‌داری کل کشور و انتقال دارایی‌ها و تعهدات صندوق‌های تابعه از وزارت کار به دولت، محورهای اصلی این لایحه را تشکیل می‌دهد.
🔹
رئیس کانون عالی شوراهای اسلامی کار با انتقاد از فرایند غیرشفافِ تدوین این نامه گفت: هر موضوع مرتبط با حوزهٔ کار و تأمین اجتماعی باید براساس سه‌جانبه‌گرایی و با مشارکت کارگران، کارفرمایان و دولت بررسی شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.84K · <a href="https://t.me/farsna/437839" target="_blank">📅 08:51 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437838">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p4sI6eYGMEzL2hDUTtc7Tc8gc3qNS46xRGkk6dx3YP0ZUPFa0oHZSkJt3Et-K6C8KAzlTIUEnAavlBYFYGZ_glmHENZwZaBjOMQV5OokhRluP1RLmkgcnlo8MKkqnhS3_7F5KVwZN7DjdzA_xI2GBuORqk9XUsEIqdVk-BimbNp70FxW7mxn1dcELs1VmV3GmfIJOy867bDYAiEmGEj6BpYqd7PBC9fhrBvRrmKf_3AnH-2e47FBiv9QLacIka3dDlXE3N8i9S2kh5B-PJ8djll8PyZus0p0f7vVXeebo_928CZQbmaMdDvsnXZEiSEEeB-GN79-lMtZ4UqAgPYvPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کارشکنی امارات در تجارت با ایران
🔹
براساس کسب اطلاع خبرنگار فارس از اتاق بازرگانی ایران و پاکستان، این اتاق ضمن تأکید نسبت به‌کندی پروژۀ سی‌پک، از کارشکنی امارات برای جلوگیری از تبدیل بندر گوادر به رقیب دبی خبر داد.
🔹
کریدور سی‌پک که به‌صورت رسمی در سال ۲۰۱۵ و هم‌زمان با سفر شی جین‌پینگ به پاکستان استارت خورده بود با اتصال مناطق مختلف پاکستان به بندر گوادر، یکی از مهم‌ترین پروژه‌های ترانزیتی منطقه محسوب می‌شود؛ پروژه‌ای که می‌تواند ایران را به منطقۀ راهبردی تجارت هند، آسیای میانه و قفقاز تبدیل کند.
🔗
شرح کامل گزارش را
اینجا
بخوانید
@Farsna</div>
<div class="tg-footer">👁️ 5.33K · <a href="https://t.me/farsna/437838" target="_blank">📅 08:10 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437837">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A0LnUrPyQVspmdhi-PCjKwsLuMVfBTdLP3m5QVAK7YiRu2A9Ll9uNqgcvMctuG3OyI1UUy1uKbUMtmV8STvjnuW9tY_LDmcl2qQ3oaYHgbNwphGudvx8EYQXnV0GG6HQ5RJ-xfAvI6Y3j47Qv8FMlNNI-X7ecijs8Xqp4c6L8WW1A0F8cazkdcQPO5xTC5IXSE-ScFfTSlGtstcsUWXIUKtC26nMQIEALi3btns6tYtGBvj7rP3OwdjhL1NWf2B6rfNfW-zQg9nomT2VYKZrN9_i-kwh_ETgz8Fc8WhvoffnqfAx9SYhouVZSlzlHSigGu4EQrVG5G62kP3kwSmLDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تلفات جدید اسرائیل از حمله پهپادی حزب‌الله
🔹
ارتش رژیم صهیونیستی از هلاکت گروهبان ۱۹ ساله «ناهورای لازر» و جراحت شدید یک نظامی دیگر اسرائیلی در نتیجه حمله پهپادی حزب‌الله لبنان به شمال فلسطین اشغالی خبر داد.
@FarsNewsInt
-
Link</div>
<div class="tg-footer">👁️ 4.94K · <a href="https://t.me/farsna/437837" target="_blank">📅 07:56 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437835">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1a4c4f1642.mp4?token=R6baeh4OK7nBdf4eAdnl9Gw1nokpjDQYbNixTV9wE6himAP1ygcEinohI9WtTVeT65W7BEfjZlwiC-J-Ttzcu3pA1FtuzByNWne8kz1rHZEOkibcZStx2h0pJFNqH0YHteOuFwT74Ii0VVrs5AuREmyiR6dzFkkqjkSkyRKIsr2qaWb-pkzAYNuhbaa3cNadkvrvkJ2_CF1nn4tWMeBKqnHEIQzZrXVmhXNz0sULGb7hz1VLq5dC56nUxCaXFbIH4maBrUG_ui-ldjx4EkhEChleYAfaijB1ygsHDZc-Nh6ee4Yjkzuj6rv60Z_6TibWOuWQ4yC5vU-ucduFHBfQxg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1a4c4f1642.mp4?token=R6baeh4OK7nBdf4eAdnl9Gw1nokpjDQYbNixTV9wE6himAP1ygcEinohI9WtTVeT65W7BEfjZlwiC-J-Ttzcu3pA1FtuzByNWne8kz1rHZEOkibcZStx2h0pJFNqH0YHteOuFwT74Ii0VVrs5AuREmyiR6dzFkkqjkSkyRKIsr2qaWb-pkzAYNuhbaa3cNadkvrvkJ2_CF1nn4tWMeBKqnHEIQzZrXVmhXNz0sULGb7hz1VLq5dC56nUxCaXFbIH4maBrUG_ui-ldjx4EkhEChleYAfaijB1ygsHDZc-Nh6ee4Yjkzuj6rv60Z_6TibWOuWQ4yC5vU-ucduFHBfQxg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عباس اکبری، از لیدرهای مسلح کودتای دی‌۱۴۰۴ به سزای اعمالش رسید
🔹
عباس اکبری فیض‌آبادی یکی از لیدرهای مسلح اغتشاشات نائین اصفهان بود که نقش مهمی در حمله به فرمانداری، مراکز تأمین امنیت و مراکز خدماتی این شهرستان داشت.
🔹
او با استفاده از سلاح کلت کمری به‌همراه…</div>
<div class="tg-footer">👁️ 5.27K · <a href="https://t.me/farsna/437835" target="_blank">📅 07:42 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437834">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">عباس اکبری، از لیدرهای مسلح کودتای دی‌۱۴۰۴ به سزای اعمالش رسید
🔹
عباس اکبری فیض‌آبادی یکی از لیدرهای مسلح اغتشاشات نائین اصفهان بود که نقش مهمی در حمله به فرمانداری، مراکز تأمین امنیت و مراکز خدماتی این شهرستان داشت.
🔹
او با استفاده از سلاح کلت کمری به‌همراه عدۀ دیگری از اغتشاشگران به فرمانداری نائین حمله و اقدام به شلیک به‌سمت مأموران حافظ امنیت کرده است.
🔹
علاوه برآن براساس اسناد و تصاویر موجود، نامبرده به‌صورت مسلح در خیابان نیز حضور یافته و به‌سمت ماموران تیراندازی کرده است.
🔸
عباس اکبری به اتهام محاربه، تخریب عمدی اموال‌ عمومی به‌قصد مقابله با نظام مقدس جمهوری‌اسلامی ایران و اخلال در نظم و امنیت جامعه، اجتماع و تبانی برای ارتکاب جرم علیه امنیت داخلی کشور محاکمه شد.
🔹
پس از برگزاری جلسات دادگاه و اخذ دفاعیات، با توجه به اعترافات متهم و همچنین فیلم موجود از لحظۀ تیراندازی و گزارش مرجع انتظامی از کشف اسلحه از منزل متهم، بزهکاری عباس اکبری محرز و به اعدام محکوم شد.
🔹
پس از تأیید حکم از سوی دیوان عالی کشور، عباس اکبری فیض‌آبادی فرزند علی صبح امروز به دار مجازات آویخته شد.
@Farsna</div>
<div class="tg-footer">👁️ 5.61K · <a href="https://t.me/farsna/437834" target="_blank">📅 07:23 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437833">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">تغییر ساعت رسمی کشور دوباره اجرایی می‌شود؟
🔹
اخبار رسیده به فارس حاکی آن است، دولت به‌صورت جدی در حال پیگیری بازگشت تغییر ساعت رسمی کشور برای مدیریت مصرف برق است.
🔹
اگرچه درحال حاضر دولت ساعت کاری ادارات را جلو کشیده، اما وزارت نیرو می‌گوید این اقدام به‌تنهایی کافی نیست و در صورت بازگشت تغییر ساعت رسمی، صرفه‌جویی برق می‌تواند به حدود ۲۰۰۰ مگاوات برسد.
🔸
این در حالی است که مجلس در سال ۱۴۰۱ قانون تغییر ساعت رسمی را لغو کرده بود.
🔗
اما کارشناسان دربارۀ مزایا و معایب این طرح چه می‌گویند؟
اینجا بخوانید.
@Farsna</div>
<div class="tg-footer">👁️ 5.36K · <a href="https://t.me/farsna/437833" target="_blank">📅 07:16 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437832">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">🎥
مداحی جدید حسین طاهری در میدان انقلاب
🔸
همه‌جا کربلاست، کربلای حسین
🔸
همه ایران شده، جان‌فدای حسین
🔹
ایران کربلاست، ایران کوفه نیست
@Farsna</div>
<div class="tg-footer">👁️ 5.28K · <a href="https://t.me/farsna/437832" target="_blank">📅 06:59 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437831">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/60b3c44c8c.mp4?token=Y1TlXcwscg0HFLpu3Ef-3x3yRq13Dv-XCSnsdtcSLdfIE1e8Lt6VeU1y6agHYHEjUx7obtvAFO145g0p_AYOkjmJF9hS6RkLD1RLQdVio9mJ5vWj0BI8M96k418gQMEaWT_A7lr70U7dJnnDqxWQNOQwWRoD_KGBgpaxDTFodefgZim5xeyuX8KACXHx_OguOImh_xEr6GKSVVosNkSOX_kEwvqVZnDd7vmo1SLS0425XCmswsnAbqzIWxB2RYq9CCN75hfLGZjLt8ZjOdNfMkEG5q_ZFv5HyhG_DoTvWjuROw6gugELC2bS4oNq9HJJWh1W5sajqpRF1jd1XiRLnQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/60b3c44c8c.mp4?token=Y1TlXcwscg0HFLpu3Ef-3x3yRq13Dv-XCSnsdtcSLdfIE1e8Lt6VeU1y6agHYHEjUx7obtvAFO145g0p_AYOkjmJF9hS6RkLD1RLQdVio9mJ5vWj0BI8M96k418gQMEaWT_A7lr70U7dJnnDqxWQNOQwWRoD_KGBgpaxDTFodefgZim5xeyuX8KACXHx_OguOImh_xEr6GKSVVosNkSOX_kEwvqVZnDd7vmo1SLS0425XCmswsnAbqzIWxB2RYq9CCN75hfLGZjLt8ZjOdNfMkEG5q_ZFv5HyhG_DoTvWjuROw6gugELC2bS4oNq9HJJWh1W5sajqpRF1jd1XiRLnQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دریای مازندران تا فردا مواج، و تعطیل است
🔹
ادارۀ هواشناسی دریایی مازندران: باتوجه به مواج‌شدن دریا، فعالیت‌های قایقرانی، صیادی و گردشگری دریایی تا اواخر فردا سه‌شنبه پنجم خردادماه در دریای مازندران ممنوع است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.28K · <a href="https://t.me/farsna/437831" target="_blank">📅 06:41 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437830">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vuz9Dt82VZ0MsgQ_t0WiGXuWL7TVB5JQJe71-rbVPEemW0p3YMxgjp3C72btVPGMOwIQReMHhZpZW8CeuUKDYgpkw1KA__AnyD8y0JszCFXEOFSYfHWO3SW6n0BjpfsTLBDyFnhA50dVq1Mn6n2AfKN4mRWs_CGSM7GmRNkKi-AeCClIeFWtk8621mxKJHDB55m0VpkBUh8khbUG_z6BAsgQOT55uB4JIsBGKldcwzaJun0DLikgqVn6hURwtbGtxc-2w_paPlVMKbJqGxID7ZgrQP8M-mH4IuksyUQHfv8Hdfw-1kCFhwF4zkTAqWDJ7w_zmK9a-R5QIjrda-xNEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پایان ثبت‌نام‌های مشکوک در قرعه‌کشی خودرو، با ورود دادستانی
🔹
پس از تکرار گلایه‌های مردمی مبنی بر اختلال‌های مکرر و تکمیل‌ظرفیت برق‌آسای سامانۀ ثبت‌نام خودرو، دادستانی تهران ضمن صدور دستور قضایی برای رفع این مشکلات، خودروسازان را مکلف به برقراری عدالت در عرضه و بازگشت به سازوکار قرعه‌کشی در صورت تداوم شرایط نابرابر کرد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.6K · <a href="https://t.me/farsna/437830" target="_blank">📅 06:16 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437828">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OJu8J_nAwdyrwJQg2zwQsc1ICrGrFswU6LWmmpCTcov7mhJ80fhPfVupgb7g2W72MhT4gQQjI-6dA_P0lrWG5qRBDJnSSbjl3aUQeuaZjWyG-DaNKABQ3tzpmrtn-cekU07ratTZ1YDwoqh2vYGOIPK8cClWPktrGRJpKESdTPi2pGjFpeMamRlwhtEmSOMhrOH7V3nSssI6OSpkLd5neMMBMBOWXpWFyhd0SbYvWkwumXKQmgkuHp0PJZx2D9kYvDUgPHEvgBZCMs94kfXDPluESyd2tdkphhJ4n3DeBjvHwmmhiht1CAGT2vVSKhYI2LNaNpJpneyWuNeZY4CX6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دو پست مهم استقلال در حالت انتظار
🔹
قرارداد بیژن طاهری، سرپرست استقلال در پایان لیگ امسال به اتمام می‌رسد. اگرچه مدیران این باشگاه نظر مثبتی روی عملکرد طاهری دارند، اما تصمیم‌گیری دربارۀ ادامۀ همکاری با او به بعد از تعیین‌تکلیف سرنوشت لیگ‌برتر موکول شده است.
🔹
تصمیم دربارۀ آیندۀ نیمکت استقلال نیز در زمان مذکور گرفته می‌شود و باید دید مدیران باشگاه در صورت نیمه‌کاره ماندن مسابقات، با سهراب بختیاری‌زاده به کار خود ادامه می‌دهند یا اینکه شخص دیگری را جایگزین خواهند کرد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.66K · <a href="https://t.me/farsna/437828" target="_blank">📅 04:48 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437827">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4a6e0f39e1.mp4?token=F9YpAC0xMUp1Ntf-nTlHXU3dltn-1fNnx0YvL1mTKlyV-e-gNTH5RvbwSHp7_nU3vwWywBfOSn1_BYzxIWxxZcH4y5Y4fn1ZepqAFHZ1DSc2SYXJor-d0TXQ00_qg9_1fSvPhFuW-xOGrGePGXXFwXRGHfmLrL2MgygqgHxr-LsNfInT4NPreVjWCGXmG-1791RtIC1Q3omHDT7UDWJKVc7imIAWpmEWOVEYeMF7vQb8LnKnUXnJcDiL9wOq3P8_APh5jrAaPt_05ExupVXyaCXu5Qxh5ueUZ0HDp06vKKt_pMyGMlg7sP2X66-qnTq826PWa_JE4Dhfu2hQ99fjpo9zik5NHe8Utio3FxsMfyl6NOPbLV2UmHr32StfZ_Le-HiTYP2XKVF9EFkK3IBpGYpcwke18BoNUBMjGbfv-8e8VFdr-P6trfDMS4gHVKpp6Gt66y9idbpFmOqPzBHEdUOzKOnLOvwULrJsGToPL2NKUrEGrbRjYls6HE0J-HeWq_qeHHDE4BfJjf7Xjpiuk3tJ7VOaH3WxirCAhBtLXgIVmKquRlAD3mHAwNY9Mzv-tYEJYUH9EujDItwYatOEpw6wf_-jOsrCewKQpRDAdDSRtj1Dcnout_zpj321QDrEB7wEhjS7VLdxnYm9NUjrwwRCdCcbNf7-krNh3qqFBak" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4a6e0f39e1.mp4?token=F9YpAC0xMUp1Ntf-nTlHXU3dltn-1fNnx0YvL1mTKlyV-e-gNTH5RvbwSHp7_nU3vwWywBfOSn1_BYzxIWxxZcH4y5Y4fn1ZepqAFHZ1DSc2SYXJor-d0TXQ00_qg9_1fSvPhFuW-xOGrGePGXXFwXRGHfmLrL2MgygqgHxr-LsNfInT4NPreVjWCGXmG-1791RtIC1Q3omHDT7UDWJKVc7imIAWpmEWOVEYeMF7vQb8LnKnUXnJcDiL9wOq3P8_APh5jrAaPt_05ExupVXyaCXu5Qxh5ueUZ0HDp06vKKt_pMyGMlg7sP2X66-qnTq826PWa_JE4Dhfu2hQ99fjpo9zik5NHe8Utio3FxsMfyl6NOPbLV2UmHr32StfZ_Le-HiTYP2XKVF9EFkK3IBpGYpcwke18BoNUBMjGbfv-8e8VFdr-P6trfDMS4gHVKpp6Gt66y9idbpFmOqPzBHEdUOzKOnLOvwULrJsGToPL2NKUrEGrbRjYls6HE0J-HeWq_qeHHDE4BfJjf7Xjpiuk3tJ7VOaH3WxirCAhBtLXgIVmKquRlAD3mHAwNY9Mzv-tYEJYUH9EujDItwYatOEpw6wf_-jOsrCewKQpRDAdDSRtj1Dcnout_zpj321QDrEB7wEhjS7VLdxnYm9NUjrwwRCdCcbNf7-krNh3qqFBak" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اعتراف مجری‌های «منوتو» به وضعیت فلاکت‌‌بارشان
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.72K · <a href="https://t.me/farsna/437827" target="_blank">📅 04:26 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437826">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/35a5c636c7.mp4?token=i_35jKVzmZaMjbBoz8Ge5Y8KzLYQkgDthI5QD_PxHoS9cnneMXhn4A71T9W0Z0WdwxcMT7Jy8r0IOI6rOKja9ftQDWpPBoHDlp7i8o1DnWP13g6yVg_Hecj2Wh_rRafV-DV57a35Lg29hnkkWWCgDG5ZvDih_m999NdW7SHPYk51CJ8-PLiCRg8sRXMkMhOvymy8njdtQ7f9CVJB0dogw0U8b1Uu-XCrn6X-YZ-aA1_yMGjXAvVcJ3AOhD8HGMSFU5BBfo_NWqkvCbe2uqIqk5iT5yi51epJB2yqezpaGXDdXiNSIvZgGlaNQPkIEfxY9dE8bqfVlNg8FQr82146jw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/35a5c636c7.mp4?token=i_35jKVzmZaMjbBoz8Ge5Y8KzLYQkgDthI5QD_PxHoS9cnneMXhn4A71T9W0Z0WdwxcMT7Jy8r0IOI6rOKja9ftQDWpPBoHDlp7i8o1DnWP13g6yVg_Hecj2Wh_rRafV-DV57a35Lg29hnkkWWCgDG5ZvDih_m999NdW7SHPYk51CJ8-PLiCRg8sRXMkMhOvymy8njdtQ7f9CVJB0dogw0U8b1Uu-XCrn6X-YZ-aA1_yMGjXAvVcJ3AOhD8HGMSFU5BBfo_NWqkvCbe2uqIqk5iT5yi51epJB2yqezpaGXDdXiNSIvZgGlaNQPkIEfxY9dE8bqfVlNg8FQr82146jw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
آتش‌سوزی مهیب در یک کارخانۀ صنعتی در کالیفرنیا
🔹
رسانه‌های آمریکایی از وقوع یک آتش‌سوزی مهیب در مرکز صنعتی بازیافت لاستیک در شهر لس‌آنجلس خبر داده‌اند.
🔹
دستور «در پناه بمانید» برای ساکنان اطراف صادر شده؛ پلیس خیابان‌های اطراف را مسدود و از رانندگان خواسته از مسیرهای جایگزین تردد کنند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.03K · <a href="https://t.me/farsna/437826" target="_blank">📅 04:01 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437825">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c069109f3d.mp4?token=M8RMz9XBA6B7_ZmNnHL9fGAwb87egReTPK68rQzkfTiW0IxGD5I8RHhsQeJFPMunX3s8cPDtMTzr38JROFiQxoOvO-nm4LjhK-8IjDoz9R9prBp3Ljgl0MaaXRoMRxgkEyWs5-P0QdQPgGDfhksy4OAlhM4tf-Sl0Mvp541saVmEEMV6O_uBvALjkLwnwdi8lrk7lDsHrf66JR0NHvf_orPgEvZAnvB_ezc_kbB1wY2ueto-b4fIcR7gQud_iO2tx-16qNqffw7d2RmeXax48V-6l-F2ze0qmTLFyFLpfUuu-UtW5yja-LR8T0jQ_Woe24ebN_Mlce0erDK4i5WiLQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c069109f3d.mp4?token=M8RMz9XBA6B7_ZmNnHL9fGAwb87egReTPK68rQzkfTiW0IxGD5I8RHhsQeJFPMunX3s8cPDtMTzr38JROFiQxoOvO-nm4LjhK-8IjDoz9R9prBp3Ljgl0MaaXRoMRxgkEyWs5-P0QdQPgGDfhksy4OAlhM4tf-Sl0Mvp541saVmEEMV6O_uBvALjkLwnwdi8lrk7lDsHrf66JR0NHvf_orPgEvZAnvB_ezc_kbB1wY2ueto-b4fIcR7gQud_iO2tx-16qNqffw7d2RmeXax48V-6l-F2ze0qmTLFyFLpfUuu-UtW5yja-LR8T0jQ_Woe24ebN_Mlce0erDK4i5WiLQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اینترنت کدام کشورها به تنگۀ هرمز وابسته است؟
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.24K · <a href="https://t.me/farsna/437825" target="_blank">📅 03:28 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437823">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z8nJ-YtmGNojH0sASv2sGrTSw6HEm9tpDEItuOkzI5alTYCEIz6cNgp_LbcXsSMSMeveIE_PmUG2PqxP3AZQEwCrH_h0ODhpps54TpMYUktudqCGS-N9KMQS5T8WwMXrMpH6Z5aBLW294sJHUjxinsLTyUdRo6auwKal-LIMBsyVIedyR3OBBGKwwRyS__ltUuc5jIhGc_LU91f2p47bj_8m81OF-HT0mwgPNjEq5xIUOTpAxmZpsZnq_MriEEcTAbnOhNon8p0nvjpvBBG_LRfqFzfuczJs1Jks9khiW33th5Pqad0xmkITmjgj2f1h1XzsMmisEY6dZ3HyaalH3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">درخواست ترامپ برای پیوستن کشورهای عربی به توافق ابراهیم
🔹
آکسیوس گزارش داد، ترامپ در تماس تلفنی اخیر خود با سران منطقه، از آن‌ها خواست به توافق عادی‌سازی با اسرائیل بپیوندند؛ درخواستی که تعجب رهبران عربی حاضر در این تماس‌تلفنی را به دنبال داشته است.
@FarsNewsInt
-
Link</div>
<div class="tg-footer">👁️ 6.24K · <a href="https://t.me/farsna/437823" target="_blank">📅 03:01 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437822">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/83a91471a6.mp4?token=j5Qua-uNCl5BFarHXAQKsXW6q-qVsor1HhV4a4Odrx25XH8MPC9ej5b-go1s-g6yl5l305NkSvh5k2bnAacXuCtkrBi4_q29mebOTx6Cs0GD6MqWrvVkMQeSIVsPZQQm7h6VoYjzCTHC2Y3wd90CUB2BgOAc0q1w7cRkxzf639lKnh16eCu78tNCBAX255hedzkxVE4o-WVQtIaKOCLCT_VVnK6Xk8Zjfbl_jDBkS8UEUTDlZumqgxcNuatcZONS9jC-8TQ00zARjgB-dBgY_qGsTKgoCMItUBNpn9VXLvgfXc8XjEZDi9sRXPPhoyXj7LxTXAhNHER_hmtQwbFXW3aT_bDggmjJfGyjG9C4GoLV5c2jBpIPveRaMPDUlOb-NIvGExElWGxgnN2gvoxYAExlVlH8fTBfzMeVYJD10br025oWNC8lpE8rArPm9FoBseiviwnVfUvwQVxRfhYL1Co-y82OdFVTtrZBozIE6a1Zmgv-QknbL3V6NeD6QcapLAQZGJaG7qyl0IhNdsCkn5s6KETUiUAAjFFCJn4BPWp1IsLY6akjjUqfdBVJ-IwepJm-HJQ8aLmV6-Gvzf8TqpPw3eoPmaT9vWMLsLeOkonEXzDurnODHOgmS3uzNfH5oqNSwyC5MQBpbaVEd0bJa__TVJx_YUjVjeH6brU5qoU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/83a91471a6.mp4?token=j5Qua-uNCl5BFarHXAQKsXW6q-qVsor1HhV4a4Odrx25XH8MPC9ej5b-go1s-g6yl5l305NkSvh5k2bnAacXuCtkrBi4_q29mebOTx6Cs0GD6MqWrvVkMQeSIVsPZQQm7h6VoYjzCTHC2Y3wd90CUB2BgOAc0q1w7cRkxzf639lKnh16eCu78tNCBAX255hedzkxVE4o-WVQtIaKOCLCT_VVnK6Xk8Zjfbl_jDBkS8UEUTDlZumqgxcNuatcZONS9jC-8TQ00zARjgB-dBgY_qGsTKgoCMItUBNpn9VXLvgfXc8XjEZDi9sRXPPhoyXj7LxTXAhNHER_hmtQwbFXW3aT_bDggmjJfGyjG9C4GoLV5c2jBpIPveRaMPDUlOb-NIvGExElWGxgnN2gvoxYAExlVlH8fTBfzMeVYJD10br025oWNC8lpE8rArPm9FoBseiviwnVfUvwQVxRfhYL1Co-y82OdFVTtrZBozIE6a1Zmgv-QknbL3V6NeD6QcapLAQZGJaG7qyl0IhNdsCkn5s6KETUiUAAjFFCJn4BPWp1IsLY6akjjUqfdBVJ-IwepJm-HJQ8aLmV6-Gvzf8TqpPw3eoPmaT9vWMLsLeOkonEXzDurnODHOgmS3uzNfH5oqNSwyC5MQBpbaVEd0bJa__TVJx_YUjVjeH6brU5qoU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
جهرمی‌ها همچنان ایستاده در قلب میدان
@Farsna</div>
<div class="tg-footer">👁️ 6.45K · <a href="https://t.me/farsna/437822" target="_blank">📅 02:39 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437821">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f59jv4US5dCqxKhm2NhUAgnm09k-K0M90mvDeTlH2TdrTe-OCbM8YHFx491ALpmnjBFNOiGR1FZHg7uau5anPiLfwUB3kaQFvKCHa1_ZzYTHPmfHgxxfh0ELXDkbdlF8tehSbmdco6Z2tipStfuOlQeOv6xbru0jL1KSEXfARcZeVVBwez6Ewy2F6wHPCASVAfLvJDN9R-7r2NWkW9o5SDpPFzQCmcBR_6NYFac7UxFZc5QG6LuUQSMJvMU5fTO_n-aFk74o1hflcGvSmaceBTe7q0cv8iqxLt___mAYIRRVd7gBZo5lP1Id7DveeKytdh2Q3HCiJVZDjPjysSRIkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سه‌شنبه آخرین روز فعالیت مدارس ابتدایی تهران است
🔹
معاون آموزش‌وپرورش شهر تهران، زمان پایان آموزش مدارس ابتدایی پایتخت را آخر هفتۀ جاری اعلام کرد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.7K · <a href="https://t.me/farsna/437821" target="_blank">📅 02:18 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437815">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mdqQoP9rt4jK02nMGYbTHutfO310BtVc5X1GC5-Xbhtitnnh370rpU2tvgHv5BFb6W6FRYn8uJHCP0MKQ-YD-4x1ivX612wnaer6lrYes3BLhlDwUardnbCNC7svDscfnckO0CNugTTXkwgqsg9Xfy1YJ9Pk3u0HfIwIKlOYG1nBk7F32iksup7vW82WlRFXwadaabcbSfkAgB5tyFMzzgo5RhgNiSWwVMZ5se7jXoDQsLpD9AsbwBZEY8JeXKFy7oVaxfdt5Y9FLJHYZyRosdvlOihj0vOGycnU8VUQYhkyMeR0gDNTlBwB8X-wDWkEvgE2uWZeQwfFTuZjnJvEGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XjWx4TOwIXInNM3azSlqVRfujKQUBnNMvc1PVcIn229cGqJ7mf71pEeYV36thsr2YeRYozwgUJvUGKKR0goRAa9q7llX1tDMR2sswb-iOTFl_rQN26gDIOJIe0EPcoSRBkqCZ0bLqrhWlRAj-hz7QkV4-GCQ0mbull-BkgW5OcpUoi0rrYqm0io9jqsWkr9KL6dIEkuWCUOCP0fYlqKF2a4XJFKByMIorEH1pT2iDL8mQdmjxktzrCxeLsUsIIhx--pKki0a6i6e7az_r61XHf2WW8P-UOHvsAcx9P-mFTmIWtlnXp9ZQueUorOyDIEiWHWxvtNViRQ_Ewxphg6itg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZL0URyJ7F4rCZRnXOkbvMz8KAsytUIpb_MaUoNRRVTw1__f0-SjUOZ68EysGIi59TpgKrVhaQb_m8SEsicozx_e26VbC0hmG8ncbLvFUeMyd5xFOxJSWKauTYLzzei7-0xYF4_o1xqhjQ6IEOKi91vnXxUJuFkahRoEox2EEvJskWcqykYyJ1df7pppGbF7ch9uvdmoZfK03yFGAQ6wZRq0s4lIApsfbWgKePrhA90cO4SNDCMIyTWAKWAlUINdJ7mVnT-VpT6LDT3Xpnx3D25sbFltprIGkzyjQB3Xug1JNInakbsExz8ce-GBbJam_Jok1OIoXMObMQ4VAwekhQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QDymtlUfIfIf-M0yl253nosdPDOH4uIoHqHiJ9q8ff53rueDkgEPkbQgMAT30AKz6psR2dCjW0t3zwlPUPrhD4UhTxvSSxjMW5MOTU9Qmkrf956yTEnWdmX5wtON5th6xzS0XRbIFk7w4-RwXYWS1tm3JYSimOgm8pDXIFuCEsx_tA-UG6IfGOGHDDnQh5S--9VBuyYpHCR-PihZINhiQf7q2ZKOYja1M3cbzlNKZ1bNz927xr-bS6TdVfnnCJNo6Gk2bINN7idY98_nH45nutRNwI7yBkspLcI_fDveAZLd4WUCvPPhOR8XS9-3iMILmQJ0yHfJjyw3LoOnVuhneg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eOqlLLwe7SPFQXwPz7tchwecdlLpbzrgFRXbeXuWMVEaQHOul6_cmxLLNeovvMLHkZIRbKa16NEvYy-vnL_FjnUUHefXyNiU5FJkyKRhGGl8GWJMzD7RPojawfaTMZftd0UjAo3TLy6yK1DcdXBOxILhV4qPp_HUH9QkQeWx0xTZa3V0Ivy2kgch-1HWcsjxcHF4g_R5JVTNAeNW1kgv2iSOrWYiDd_WhFypXTg2seY1siF4UOH_PT1M4cZBYqlk1eUgqmuoKdIIiVtNfXqSAVbeh1dj8HtwtsIc8GUeJ4P4gfCF4ZUEXRXKlw3geE40ay7PVbtRWt100fSQq1n7Vg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/c7r55g2tzxCbQzl8K-sU3xvnOl3w8DAIsWhZ5249DrWCZPfKLNc1uXTNMWIDY2IRSdSRvW0VuVPglL-fb_0UB_ycAw3sGdvyxapUNFAaz8EvO5VdN93T-oLTxIYupGqOBx8t4d5v3UaALfpVc8Q6Yv8iXh-ad61I6oPEorz6gPSJpi3W7IIM8vkYttDKVIMp2oarHt171FCXaVlhKQjm8iHKOGQBNkXtBwb-CPHvTCn1Pns3qUsrs0lifXIPM8fy44mP6wCXwzqwYERb_1MTWlSuGLAQTxaOR4VBUADrwhmJB7TnLUpe3_Y0ToUC3YaWd612EEzcsU4Hze3sLkTjYw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📰
دکۀ روزنامه | دوشنبه ۴ خرداد ۱۴۰۵
@Farsna</div>
<div class="tg-footer">👁️ 6.12K · <a href="https://t.me/farsna/437815" target="_blank">📅 02:13 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437805">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bLqBsWI-DlAZ_iJLP4To5-7UHJR_yG0LiUoqM4wATWLV5TdJJ42EkNd-wQ5nmJkY0xZ6-Tk4yDvCcYa-QKBFqj6rOV59Pl1o0rf10jzxtLKPI4cQly6WYRVF6KBa15NsrzY_mNp03hMbFIVfhfZJRDomiZYTSdeyV4cpbdFmDx5NW5zdSsq7vHnQXLXELHO1vbommIvSQSCTP4KkvasbqFYBeT1OehG7tOjXjO4eptCogx5aVeRV92AOvZaBE2nRUuaY3XGUzxFWTV550cQSsYgSfB81Gats6O0Ty_WeHUzWUS_S69TBdyP8MCWublJ-38JdqzPsnMZV3U-6anMT2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fRDX8Ke83OqcPpIA6hM1s11xLsz1GcTWk0czo7_qZ8x5-Lx-LqgIon1SRZP5A8PdY0Z5za_Llwi5sUDEAJtFe6wxTgcMVHyAFZJsnMLZ4l4eN840QyKWdwftbGbnn2RQpN-HzrmX2fEl5p8eiyOCLxYwwhjP0qHQ2AYgCHyrR34TR-Leg3kfOOh6GtHdPx6zv_YrBf0Uhbjt-fOBD0-knftbqYr9geMRP2OBX3aZXL_YExTNm5WE1Ax0R6GiFo-fcbi9vuhCxUjBDF0a_kq1DywikFnCnjg92zeRSMxMiQDL_g78uiA7KvopOIy_8Z4gGBY9lOmQtjqf-DhU0xiWXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Z-Od0u8VUqWnEYygTMrvIvf1JXN6V-9MupoDMx9eW-UplerU2jxpm-gWqybkcREB8829s95DDQeenv7FtL8Lx025r0PUmrU1_28KcPAZJBopyllx4yWmrSIHhkHD9x60R9MPXpmR7rrDVxYlrJ1ef1OnKm649qVdODqlBf7ln4KM1lRVv094H0t0giH0ji0FtLyOWy5rgIHdztQeLI100W7OH7sNI6DClbT1TrdOU9W9bnqkynezeA4956I_7pIVf1HT_P2D352fBRRffKAqZ_Nw-zpUf5a-DCZ3jff2YETTy_WsDhHW45XE7iT_hY9_2tqU27T1qszuHIU3qMsqcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PGn0wyygO3KkMdvyaiFHM7Xl1EGX1AkHZKg9v9-sTXcvOX2j4Q1ocQKJcAwNrCqqQ2YZZpsq1EASNJPC2GppfY0YHKZ3cXjc5Q2yEdSs4ktVUbuUl2i712P3RtIu7PMYlwkXZ1QQ1v8zPnkAaUipw_vMY6Oy9EZBsrlXll0h9s4sfcj3P8dbnjiQ1EU6EyqcidMfpKXkTaaIDdlYrEBwNq7JziJo0L_0YQRAPwZ-hjgGX2x0Fkjr9GeGLY__fP3EVo57oUgFlOhsutKVfaef8fRFkNNCnZcZJ21ITVRmW6Ecwlm1g5SEhuwbWguo7mCpYwbw8nq8NRn_q9xMiIH1Dg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bn4O-jEhIhkGV5PdjKwWVMZNJB56Ke0YrBOPc8ov6X0KBQKWG3fNJfMy2M131DyaoACUOlEqKp9SQcAaH_Ee7wsL-_7TFgmJ6py4kLAVkov3pDFIHpwQvirwsngsjmvv_xJl1n34aGvLPA_sXD0qHw02EsBTaM2BsVBMKfDSXt1vxZt3kJJWWqhZKiI6TryRxWXusNplKCDfrmZRVhOiSeaY7TonTmw2_Bbz0LVXMmmpuyReTqCpfgGnZMXhj1JkTLC4X0t0-EKmvUK_vbxNRaxoKqD7YTxCQRCLOhgmv3nu1tQRFx8GBSjezn6s4LzTFBnm-PfdM_GTpA-o9__1bQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZRbB-9UgVgb2Fq7BU1yD4bgiNZs93rDb0XWTU4YJm6erod1Jxhzt3x_3AXe7EzYqwg02Bk-u-ad9xu19G2GUmXTKTQNyVa9uZz3a6E-z-Pilqmd5TnncW6PA5pMygQ5LOTQb76gxrWuXmGMIKfJiJBJgvYdiQhFLJIvq_lHgzJ70un2bYiPFY-2wywd1gmUrQss0_MCgSxTGPm5aLLzCOorc3R1nx47ZX-8bmEB3cIdiHnYaXyTB7To-hKLXPQKgQvO3H6T-ImFWYiR5b_bsDKFUmwUMOxcL9nT4XOLzGe8q8pxNAuVM6wQ25dlpfqMRNB_Wyw8WqWHSo3LX6-ZzFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Pzk4UP4AX5SqsLp7rFSGjrO2aEsiyteZukZt115Svs1sQk5M2XwDWiFcatyYNdYmlDIWOkAhgj-IdunoK6LJm25fIJBlJ2yBDnLokgWGNutjcGpTYHb_gdk6twr6VLz_lQ68QFIZ-Xn4vPql36nreAIY0g8TyUfcXuc2p3w-ocQRCYHeFds50Y7P-J2KZb7twdwgYyRSyDdgi2vFiN7Kqir1kt0GRtmYmYpnoMrO3WhNjcpt85apQzlBtJsq89tCWfCkd0T3L100U5LV90I8s9iofHndYDpBw2UL4D7MxmXrunfuC_7M_Acv_jmaOTU0zRbFhz2WnT64nEKYvp7C2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Suk-fQFQ-t8LsabYvSD9jcdF0L5WLQXnh6NB8ONcY2rjbWGsPY_P-H1RL4CTR4Uw-wlM3BfAO26PhY2spC_oUyzM3CMjBv9aviSLbTlcoDsGMCMXnAd_X_mJdQrSqNFMwHfIztQMBD4xzokWyLz77ANOR1Ag1d-OzVrvbjOuCLGGJ1v6Y0ACpCp9aKWI9I-FFJ6EXt5GHJfuVOl3jGkAMOXWvs9uyh-OAbmiEVsO-MfGMz56hRjAvasprnnN0r1WVhgO9HIFHl3CFATso-btvCb2iVkybdJIaKuX-JrAg5xJYusxHuimD8EEz9u37sZga5iVaGdmt1kDJuEblgou6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TzftQN4vBmUeXM14wn5cIxnwk1YbGMf99A639swSDW-pDt2cxh-9JB6-jbul3OQZJA_UzJpWbDsyXgUYZVVZQIq-0nMvTbDaUsxA4YvLUIGEpWLLoe3E8PHFPnzYS15g96oL-wFXVk9cOIW6qLX56q_TAm2ajKJvwrEmrrbQ_DSPLO3BcaOUI3MT4MlSD8KwgHs9WV9N9h8eda1IAT3IrHsF9nRlLbgJryZLY6QWnWmrBva8PbxaNj8Z-RXnpkpPrcXSCpho1gHVL7YUC3UQLekY2VMjWTdgUXVBAttIQIHlrhm7X6YbmvilqHlaRkhrvhXujGRbGxpHp9EtJ1J0zA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pCMj03nC9T_dKXpzm70GPfxcUcrXED9cg4p4OTVOPf9TUoQ-IuDzUtlhig0f-ShRbaAcvyCI32Lc6b6GvPUrpuuY2b2BbhkD-kLbA6jyFnNmK4Tt_4zB9jZH7KoZA-_vwKhGkhnfOElZMr3yMNlIAwIZ92Rk7qW4pBiSPtdydNSwufvEFZy65IRCz_BXVKncaulLUMiAvCC0ZQCHYv-IK0eTR57e-RkmEr5RW0QSfxmbP8_7YGT1obBDHPYgXj1gf3wyCetqCjuMtMrBe3VPUa4iTHQt0HBdBH-7E32utb7RPmjL9dP2G2v5zzT4PdI9B8M2yU3JDilhE77Hx-vzzA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-footer">👁️ 5.97K · <a href="https://t.me/farsna/437805" target="_blank">📅 02:13 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437788">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z_qVU9IaDnPHJvS7wh_D7Yl03rM072fAaiBPOvDxlOgqF_A5-5BBOpwPsh-F3AAOaC1bycTilkSoO1qYHFDMVyt5DPhGhumI8azEGuZ2t4FaEbp3rBXuGTO2nnff-5veEOdzNyoPIhugEDtoxr4g7f8Cj3UrUU3upamVzmmWo-K6e8LrZS28SHLLruAVCJKOS5geqkY_pNbjSxPR8jj07JRSWKfdTp-IrzNv5Ca1HTdbyLF9dTrglbFEgP-rLWI0BuYs5_LytuMVQuI8464PAk8abdijUd-KfefOgYUc8hA2WC0yw-tD1mmtAV5ofzpOPtzksLvx1EUrvgxKMh9xug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزغ نادان و مار پیر
🔹
در باغی بزرگ، ماری پیر و ضعیف زندگی می‌کرد که به‌دلیل کهولت سن، دیگر توانایی شکار کردن نداشت و روزبه‌روز ضعیف‌تر می‌شد. او می‌دانست که اگر تدبیری نیندیشد، از گرسنگی خواهد مرد. پس نقشه‌ای کشید و به سراغ برکه‌ای رفت که پادشاه وزغ‌ها به همراه مریدانش در آن زندگی می‌کردند.
🔹
مار آهی کشید و گفت: «ای پادشاه بزرگ، سرنوشت من تغییر کرده. دیروز درپیِ شکاری بودم که سر از خانۀ زاهدی درآوردم. فرزند کوچک او را گزیدم و او جان سپرد. زاهد مرا تعقیب کرد و فرجام کارم این شد که نفرینم کند. او مرا جادو کرد و گفت ازاین‌پس روزیِ تو تنها به اراده پادشاه وزغ‌هاست و تو باید مرکب و سواریِ او باشی و هرچه او فرمان دهد، اطاعت کنی. اکنون من به اینجا آمده‌ام تا به فرمان شما باشم.»
🔹
پادشاه وزغ‌ها که از این سخنان بسیار خرسند شده و غرور وجودش را فراگرفته بود، فریب کلام مار را خورد. او با افتخار بر پشت مار سوار شد و مار نیز او را به این‌سو و آن‌سو می‌برد.
🔹
چند روزی به این منوال گذشت. مار روزی با لحنی عاجزانه به پادشاه وزغ‌ها گفت: «ای سرور من، شما سواریِ خود را می‌کنید، اما منِ خدمتگزار بسیار گرسنه و بی‌رمقم و اگر بدین صورت بماند، دیگر توانِ حمل شما را نخواهم داشت.»
🔹
پادشاه وزغ‌ها که کاملاً به مار اعتماد کرده بود، گفت: «برای حفظ سلامتی مرکب خویش، اجازه می‌دهم روزانه چند عدد از وزغ‌های رعیتِ مرا به‌عنوان روزی بخوری.»
🔹
مار با این حماقتِ پادشاه، به مقصود خود رسید. او هرروز به اذن خودِ پادشاه، وزغ‌ها را یکی پس از دیگری بلعید تا اینکه سرانجام نوبت به خود پادشاهِ نادان رسید و او نیز طعمۀ مار پیر شد.
#حکایت
@Farsna</div>
<div class="tg-footer">👁️ 6.96K · <a href="https://t.me/farsna/437788" target="_blank">📅 01:27 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437787">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dee7ab2004.mp4?token=E3m5-vma2xjBdvAnyBPTPQiGh1DU31eMAeRGuPuSGV-AqrphoreQUsqjANhJRQsDBrpAK0H_nGolt3-TAmlPaeWcjSfRdNlY7uOGuNqDNjGY_7UBjxw3z9-01ePUO7nInf9le16IKNs0p8Tn6TQZ3oHn1y2GIfCYQYa1M7XKK9ltPO6hhnI2MaKQC59Y9yLGc737mJ5DG7dnSbTetFZvouc9BGJgeNjIb-kNeiIAk-ZGPFxHeD9b0VkHPIKsoygWBzDZR39VybP4G6YrTl97dzcL0OQfiRJy3VvOAMBy5_J41132f_3HLjyOKXl_XJP85brxG06ti6OqF-4zotiLXw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dee7ab2004.mp4?token=E3m5-vma2xjBdvAnyBPTPQiGh1DU31eMAeRGuPuSGV-AqrphoreQUsqjANhJRQsDBrpAK0H_nGolt3-TAmlPaeWcjSfRdNlY7uOGuNqDNjGY_7UBjxw3z9-01ePUO7nInf9le16IKNs0p8Tn6TQZ3oHn1y2GIfCYQYa1M7XKK9ltPO6hhnI2MaKQC59Y9yLGc737mJ5DG7dnSbTetFZvouc9BGJgeNjIb-kNeiIAk-ZGPFxHeD9b0VkHPIKsoygWBzDZR39VybP4G6YrTl97dzcL0OQfiRJy3VvOAMBy5_J41132f_3HLjyOKXl_XJP85brxG06ti6OqF-4zotiLXw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
خوش‌چشم، تحلیلگر مسائل راهبردی: روبیو، کوشنر و ویتکاف از طریق واسطه به ایران پیام داده‌اند که به توییت‌های ترامپ توجهی نکنید.  @Farsna</div>
<div class="tg-footer">👁️ 7.1K · <a href="https://t.me/farsna/437787" target="_blank">📅 00:59 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437786">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5888c1c9ad.mp4?token=iPJFxqaWtmCLoVtU9xCO3XltlDZU8Mk3oUpaxTlPiMk7Bkc8SLLlB4dTVaZTabbtRCn0fBllmKlVrcb47Pbss9vC94qBT0qbF4i2Rp56XHdHxhlTeEdq3ZGrAp7MDoTD7LiliNealY_PNi53rg2I5rM2ApjtpvUtQpLhReGjTPmiNoYpTn0pC3Xr9r2GC0_dArZ-dIjLUzjoI9yB9F7qfEuY2XI_3dQ7IYNl3cNXLZI_lvZQsjIn_LsXjKgYgfQwMAp1JlN5fgOIgl7rfs2SFcf5hDLitt3KSlT-CUt4a1OE71xXPTHgnSG_f6QKOk4kpakx5ExwV0shOFl-WDfBVw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5888c1c9ad.mp4?token=iPJFxqaWtmCLoVtU9xCO3XltlDZU8Mk3oUpaxTlPiMk7Bkc8SLLlB4dTVaZTabbtRCn0fBllmKlVrcb47Pbss9vC94qBT0qbF4i2Rp56XHdHxhlTeEdq3ZGrAp7MDoTD7LiliNealY_PNi53rg2I5rM2ApjtpvUtQpLhReGjTPmiNoYpTn0pC3Xr9r2GC0_dArZ-dIjLUzjoI9yB9F7qfEuY2XI_3dQ7IYNl3cNXLZI_lvZQsjIn_LsXjKgYgfQwMAp1JlN5fgOIgl7rfs2SFcf5hDLitt3KSlT-CUt4a1OE71xXPTHgnSG_f6QKOk4kpakx5ExwV0shOFl-WDfBVw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
خوش‌چشم، تحلیلگر مسائل راهبردی: تا پول بلوکه‌شدهٔ ایران آزاد نشود، هیچ تفاهم اولیه‌ای با آمریکا در کار نخواهد بود.  @Farsna</div>
<div class="tg-footer">👁️ 7.22K · <a href="https://t.me/farsna/437786" target="_blank">📅 00:55 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437785">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fd88f03fe4.mp4?token=RG1BNarZD5vm_OQGIUZ5D1O3ikVSxf5ABPJb9TLynI0zKiK2K0Q1qPmYBQ2dLeSmGTkL8XvHO-ypFeRoKmWbCR9DvxKXPvjsZFj4PVyZ6GpfSJGzRKQX5vsLykB9SS2QdJYHF5oeqneXfEeTZK4keyUeUFYxD3bkn0h42ZUjHv0vfqap7aq84RaG0UPdD4yy2ktbWYEF512JkCSciWBXm_a2ulrboBaRIKpElrVVEv7zSr7ntpyRQ9mT2rXFdju9mIVLFPzJibWODjgFFHFZRhK-7OLlpRs6O0AC08a9kZRBJiZXAzeLqMmtaceJm6rhAL_cQMPwGYuj50C3tuEuGA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fd88f03fe4.mp4?token=RG1BNarZD5vm_OQGIUZ5D1O3ikVSxf5ABPJb9TLynI0zKiK2K0Q1qPmYBQ2dLeSmGTkL8XvHO-ypFeRoKmWbCR9DvxKXPvjsZFj4PVyZ6GpfSJGzRKQX5vsLykB9SS2QdJYHF5oeqneXfEeTZK4keyUeUFYxD3bkn0h42ZUjHv0vfqap7aq84RaG0UPdD4yy2ktbWYEF512JkCSciWBXm_a2ulrboBaRIKpElrVVEv7zSr7ntpyRQ9mT2rXFdju9mIVLFPzJibWODjgFFHFZRhK-7OLlpRs6O0AC08a9kZRBJiZXAzeLqMmtaceJm6rhAL_cQMPwGYuj50C3tuEuGA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
۴ شرط ایران برای اعتمادسازی از سوی آمریکا چیست؟  @Farsna</div>
<div class="tg-footer">👁️ 7.57K · <a href="https://t.me/farsna/437785" target="_blank">📅 00:47 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437784">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/615bbd2bb2.mp4?token=awQcsSR_pVMQisXVUr3_YolQX-JCRSqsNpAhge4bAbY5A5meZvCsXODLpyIY3E4qTCfSM4YLUB6loBOa0l2NZg03AEBOS8VwCjPYFlFa9wzO4D2AVyDHITyn-G8wghFqpCUyY0on3qfm2R8UEHZRvU6sU88MkDV65MIOJJusgnEWXhTwzvs14EqGr5oFbGGP4JwdvswfHFa2lDgt5I7YNa91E4pPRDxiUnvaUvCePGg-VgBgHG7jM9vwPto_F4gZNsMzaOvVvA9CdMpElzOkhZ3ZsEBGevrnmpqurSF3d2w0tz-DuDoi_CDzQiufHJlxda84dj3hegestFBe3BXQwA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/615bbd2bb2.mp4?token=awQcsSR_pVMQisXVUr3_YolQX-JCRSqsNpAhge4bAbY5A5meZvCsXODLpyIY3E4qTCfSM4YLUB6loBOa0l2NZg03AEBOS8VwCjPYFlFa9wzO4D2AVyDHITyn-G8wghFqpCUyY0on3qfm2R8UEHZRvU6sU88MkDV65MIOJJusgnEWXhTwzvs14EqGr5oFbGGP4JwdvswfHFa2lDgt5I7YNa91E4pPRDxiUnvaUvCePGg-VgBgHG7jM9vwPto_F4gZNsMzaOvVvA9CdMpElzOkhZ3ZsEBGevrnmpqurSF3d2w0tz-DuDoi_CDzQiufHJlxda84dj3hegestFBe3BXQwA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ایران چگونه به آمریکا پاسخ فرامنطقه‌ای خواهد داد؟  @Farsna</div>
<div class="tg-footer">👁️ 7.97K · <a href="https://t.me/farsna/437784" target="_blank">📅 00:27 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437783">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/287f28225e.mp4?token=b4PMbwmT2qrxN2y8BCHctohNr4rIsW901-lYO7AC4TJ2XDyl1-_V3YxErmxN12M_Oshu0F1qLSFIsQJuqquphHIN-_aPsRUWFBGGD-Er6ig6RtwtAha6wi8w5DKWgWaiS8Z4REWSL2M75bPB8LoqVsaZi5w2_xsNG6bKbFwNUdDBEYZJ0ebAvTXwE6uxcjMvdosm_Civrb3MEB_E5Uk1PlC-gNhVu-PKVKA5CtBDGLR5JMtk1C2TNrx_swSwhhi1iFunbS0ixKEUX8S1MkfxSOpuGfk6QwlHvkbQGyphgGa_2JJrVg6AFacudUuL9tFLlAzfTkaN2Lr6gyKgJyGaah0KI-QxxxCqmpoMHwFv5ZN3IarWMN-nNEOF1ee3sBL0_d3rWlfNqm0n-AFuTOcgVGtMCf_pay9wqB_Mc6Q44EN06RECmOqOi-f8Dmg2RtfJnMs0AkB7sR9wcpPwYSTQBse4FJvQ7LSrpKHEu0t8wXYCdKdvoffaUHH819y1A9jOCnG7QyCA0TDpXIMWRPVx-AKE_1oGxl5JHughb8HMbLOXpL-dv2JfcWTHkSFlkjSijej719g9WmekjLlabaG3KulEAkcg6Py17WkAU9dagNfarMEgUpwaGmWnQWwpG5W8MM1fUU0ycD14iX5_sCeoBufmew73kVG6SKJfNatW_sk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/287f28225e.mp4?token=b4PMbwmT2qrxN2y8BCHctohNr4rIsW901-lYO7AC4TJ2XDyl1-_V3YxErmxN12M_Oshu0F1qLSFIsQJuqquphHIN-_aPsRUWFBGGD-Er6ig6RtwtAha6wi8w5DKWgWaiS8Z4REWSL2M75bPB8LoqVsaZi5w2_xsNG6bKbFwNUdDBEYZJ0ebAvTXwE6uxcjMvdosm_Civrb3MEB_E5Uk1PlC-gNhVu-PKVKA5CtBDGLR5JMtk1C2TNrx_swSwhhi1iFunbS0ixKEUX8S1MkfxSOpuGfk6QwlHvkbQGyphgGa_2JJrVg6AFacudUuL9tFLlAzfTkaN2Lr6gyKgJyGaah0KI-QxxxCqmpoMHwFv5ZN3IarWMN-nNEOF1ee3sBL0_d3rWlfNqm0n-AFuTOcgVGtMCf_pay9wqB_Mc6Q44EN06RECmOqOi-f8Dmg2RtfJnMs0AkB7sR9wcpPwYSTQBse4FJvQ7LSrpKHEu0t8wXYCdKdvoffaUHH819y1A9jOCnG7QyCA0TDpXIMWRPVx-AKE_1oGxl5JHughb8HMbLOXpL-dv2JfcWTHkSFlkjSijej719g9WmekjLlabaG3KulEAkcg6Py17WkAU9dagNfarMEgUpwaGmWnQWwpG5W8MM1fUU0ycD14iX5_sCeoBufmew73kVG6SKJfNatW_sk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
خوش‌چشم، تحلیلگر مسائل راهبردی: علت منصرف‌شدن ترامپ از حملهٔ دوباره به ایران، ۲ عملیات پیش‌دستانهٔ منتسب به ایران بود نه درخواست عرب‌ها.  @Farsna</div>
<div class="tg-footer">👁️ 8.01K · <a href="https://t.me/farsna/437783" target="_blank">📅 00:22 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437782">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🎥
هنوز تهدید جنگ وجود دارد؟  @Farsna</div>
<div class="tg-footer">👁️ 8.14K · <a href="https://t.me/farsna/437782" target="_blank">📅 00:14 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437780">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/04ce8ba916.mp4?token=mSw120IFktx2pKsle7__JPV79EatY3ZqoDg7TMeImTLmxeoOdyl38ULHfHY8Zj_NeY9gUXsM9Z12vhpirh3ot0MR8jwH80c9AhhMgomFfG9qfnWEMTq5EPTnMQTL-oT2hwN00Hr3Co0WfRjj7wJkzWOrkk-upptBnpJt9buQZbRQ0Vk5rbL5f9BpCGSyg43wrJHS1bwvP-jcIrUwOhcCOspqOZvCOt_4RIbO6appmGDb_dlieVzE9pw6NR56HPYEmo00a6OlAwB09Ru93P8WtiAgTwb4CTiJiXdFJjzFC-KHhXShX-3tmITb0IDY8lFRIq7SfRWCaiR-G3ze_njA5YWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/04ce8ba916.mp4?token=mSw120IFktx2pKsle7__JPV79EatY3ZqoDg7TMeImTLmxeoOdyl38ULHfHY8Zj_NeY9gUXsM9Z12vhpirh3ot0MR8jwH80c9AhhMgomFfG9qfnWEMTq5EPTnMQTL-oT2hwN00Hr3Co0WfRjj7wJkzWOrkk-upptBnpJt9buQZbRQ0Vk5rbL5f9BpCGSyg43wrJHS1bwvP-jcIrUwOhcCOspqOZvCOt_4RIbO6appmGDb_dlieVzE9pw6NR56HPYEmo00a6OlAwB09Ru93P8WtiAgTwb4CTiJiXdFJjzFC-KHhXShX-3tmITb0IDY8lFRIq7SfRWCaiR-G3ze_njA5YWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
هنوز تهدید جنگ وجود دارد؟
@Farsna</div>
<div class="tg-footer">👁️ 7.9K · <a href="https://t.me/farsna/437780" target="_blank">📅 23:59 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437779">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9f3b48a794.mp4?token=R7xvBLvk09qroAqVDdzGjtUFWWYejywUN_bHCWTG-omwZqtuml13bxUWdenPZ_ixqqCe0WTrRih7ui8y5iLXWNqh7jPh3-Mm7nnBsEndyviv3rCv-g8VbF2B-VbVTqRK3rGPM8TFy6BUdwDamCX02sbBZJ7LxCAA3fQiqxNRoSHviXIL-M_9cVQ1MmnCcGjlTXVl4RRs2-jjuO_dfrUsscoes69i1_OpytR7wn0NVMbIub72-Be2TP88t7nrVbHnYA7fBqwYC5SA2EJmWK3Iw43sr9fG6Gz8iDh1UNYPqQc1d-iMNsWzdMrBJ-jbNdS5MlfRJGCMlGKrtccuJulhUW4FrSZTpp20GEMhddDL7c8-SBBXc0uxfLlCVdLCC3TRPV8-t6BORC_6mX9gOCcMmG2ZE7urj_05rmvdB8NFzLF0ZoJmfr0_TL2DxNZhIBTRjvj3NMk5StqZctjVRS3v4pMaqEKe5w51CfWKxptc415tSnm9RsjlhPjDSNhauf9uRKXHcR8DMB2NANuwErLeBTWi6Svxw2LaPN8h2WkbqplXFvrukNHL1glc06TbVAcBqn9qObZOz-oToaUgoPRHxI8-UgwrDf7WQLutDyo9Sbk-wfiawBLwf2OTMxrsfSjBf2Oc601W-fTQteIdHuGkJz54AJJ39XXC_EoQuzLBR-k" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9f3b48a794.mp4?token=R7xvBLvk09qroAqVDdzGjtUFWWYejywUN_bHCWTG-omwZqtuml13bxUWdenPZ_ixqqCe0WTrRih7ui8y5iLXWNqh7jPh3-Mm7nnBsEndyviv3rCv-g8VbF2B-VbVTqRK3rGPM8TFy6BUdwDamCX02sbBZJ7LxCAA3fQiqxNRoSHviXIL-M_9cVQ1MmnCcGjlTXVl4RRs2-jjuO_dfrUsscoes69i1_OpytR7wn0NVMbIub72-Be2TP88t7nrVbHnYA7fBqwYC5SA2EJmWK3Iw43sr9fG6Gz8iDh1UNYPqQc1d-iMNsWzdMrBJ-jbNdS5MlfRJGCMlGKrtccuJulhUW4FrSZTpp20GEMhddDL7c8-SBBXc0uxfLlCVdLCC3TRPV8-t6BORC_6mX9gOCcMmG2ZE7urj_05rmvdB8NFzLF0ZoJmfr0_TL2DxNZhIBTRjvj3NMk5StqZctjVRS3v4pMaqEKe5w51CfWKxptc415tSnm9RsjlhPjDSNhauf9uRKXHcR8DMB2NANuwErLeBTWi6Svxw2LaPN8h2WkbqplXFvrukNHL1glc06TbVAcBqn9qObZOz-oToaUgoPRHxI8-UgwrDf7WQLutDyo9Sbk-wfiawBLwf2OTMxrsfSjBf2Oc601W-fTQteIdHuGkJz54AJJ39XXC_EoQuzLBR-k" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
دومین شب از مسلمیه در حرم سیدالکریم( ع)
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.96K · <a href="https://t.me/farsna/437779" target="_blank">📅 23:40 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437778">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9644e81c18.mp4?token=NHZ9jTVoNA_FApF3e4uXJBs-FXle3gh0enMuUZZRM_19GqN_vQI1hR8wdIWoJoHw4_tiomSstUF2m3Lxq36iOw04QaZQi81WM9jjxQWBukHlh-w0ID3ZbN-F1vMgV8S8uzwHI3dUuGR0bz3Zxu3NtvMoNFT9fl9oAI7VeTDmQ64VpHm_mlmhaxMwDmTG_vFCbtXAz7T0y08jSpn4vpANtNdtdzF0OEAiTZ76P_zgnSBrfzSkiOkGuu1dpTR5nelue-StLLvucNNeRO2FWH2zWwlfyzJtFXXMDT19Hgw1MgfV-T9_hbsoayrhIs1gz_awbt8fvVIX5AnKslOE0IsksQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9644e81c18.mp4?token=NHZ9jTVoNA_FApF3e4uXJBs-FXle3gh0enMuUZZRM_19GqN_vQI1hR8wdIWoJoHw4_tiomSstUF2m3Lxq36iOw04QaZQi81WM9jjxQWBukHlh-w0ID3ZbN-F1vMgV8S8uzwHI3dUuGR0bz3Zxu3NtvMoNFT9fl9oAI7VeTDmQ64VpHm_mlmhaxMwDmTG_vFCbtXAz7T0y08jSpn4vpANtNdtdzF0OEAiTZ76P_zgnSBrfzSkiOkGuu1dpTR5nelue-StLLvucNNeRO2FWH2zWwlfyzJtFXXMDT19Hgw1MgfV-T9_hbsoayrhIs1gz_awbt8fvVIX5AnKslOE0IsksQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سردار نقدی: دشمن ۲۱۰۰ پرتابه و ۳۰۰ موشک زمین‌به‌زمین به جزیرهٔ بوموسی شلیک کرد اما رزمندگان ما بدون هیچ ضعفی ایستادگی کردند.  @Farsna</div>
<div class="tg-footer">👁️ 7.61K · <a href="https://t.me/farsna/437778" target="_blank">📅 23:39 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437777">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dc855048cc.mp4?token=Xh_VE6SA8SrbVu2qmufhN3EQSFDii7MixWaOp8k5O9Mmkd0gRHlhVNIT9kQCz9NibU7oHvh4nqgaEYKhbev9TQ3Jtw8RA0BdPzvJDeMFvbvXcyK0h5ue3jIr3Gm_O0r2BgBI7LJlb6I9ukijfPRpxC01WF3_dcr3xsyhdHLRFfML18Bvqhjnhylz9-e2AwS9d7Z97-LRvcPttlnkGG6xqappHEw1rgg7Xm-88s3-Fb2tGaIJVn13OmvovxDeaT_LvupFLYAJYpk5z-Oi9zzQwnWbpUfI2d-Tdc6yhLOzz3QfgVDcjjjFdMAlVZ46_3V9-PhE9wR1PxExk4cjZQ1Smw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dc855048cc.mp4?token=Xh_VE6SA8SrbVu2qmufhN3EQSFDii7MixWaOp8k5O9Mmkd0gRHlhVNIT9kQCz9NibU7oHvh4nqgaEYKhbev9TQ3Jtw8RA0BdPzvJDeMFvbvXcyK0h5ue3jIr3Gm_O0r2BgBI7LJlb6I9ukijfPRpxC01WF3_dcr3xsyhdHLRFfML18Bvqhjnhylz9-e2AwS9d7Z97-LRvcPttlnkGG6xqappHEw1rgg7Xm-88s3-Fb2tGaIJVn13OmvovxDeaT_LvupFLYAJYpk5z-Oi9zzQwnWbpUfI2d-Tdc6yhLOzz3QfgVDcjjjFdMAlVZ46_3V9-PhE9wR1PxExk4cjZQ1Smw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سردار نقدی: سربازان آمریکایی در ناو جرالدفورد باهم درگیر شده‌اند و آمریکا موضوع را آتش‌سوزی معرفی کرده است
🔸
علت این موضوع هم فشار روانی ناشی از احتمال حمله ایران به ناو بوده است.  @Farsna</div>
<div class="tg-footer">👁️ 7.44K · <a href="https://t.me/farsna/437777" target="_blank">📅 23:33 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437776">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/444d37dc97.mp4?token=QR-vuOVnvuv72u-YseKjRkD-_rdr0WFS8NvxzGAltFf_xhhAuaMjs_3oVz60PJk1R5i6rFVTvkNB7ujCtLVYVCKkZy31c1P7uEe0saPDGEaX4UBvrbUtNui0mMx63jvgw_3hErO1zqc7so90ejiCuK3oZG5TlFmw6Jn1eL2F7EGQO3RXMs1XSaLk4ThbokBbPRq9aaQgDkVXW9ym_0z_zd38H0yidNhGy4kIiL2r4NKwqYuOUmkRMm32saft1NF_HV5MQO4tpVwSca1WRLnTaOAgA2LEElFdpq82xl1O9vHwSHLyq4PAl-qifSs68td_f7RnOqDhBZyuLQe3-mbgrg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/444d37dc97.mp4?token=QR-vuOVnvuv72u-YseKjRkD-_rdr0WFS8NvxzGAltFf_xhhAuaMjs_3oVz60PJk1R5i6rFVTvkNB7ujCtLVYVCKkZy31c1P7uEe0saPDGEaX4UBvrbUtNui0mMx63jvgw_3hErO1zqc7so90ejiCuK3oZG5TlFmw6Jn1eL2F7EGQO3RXMs1XSaLk4ThbokBbPRq9aaQgDkVXW9ym_0z_zd38H0yidNhGy4kIiL2r4NKwqYuOUmkRMm32saft1NF_HV5MQO4tpVwSca1WRLnTaOAgA2LEElFdpq82xl1O9vHwSHLyq4PAl-qifSs68td_f7RnOqDhBZyuLQe3-mbgrg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سردار نقدی: دشمن با بمباران سنگین تصور کرد که نیروی دریایی ما را نابود کرده اما نیروها با پدافند غیرعامل خیلی از امکانات‌شان را حفظ کردند
🔹
اگر آن‌ها نیروی دریایی را نابود کرده بودند باید ناوشان راه می‌افتاد و از تنگه عبور می‌کرد. @Farsna</div>
<div class="tg-footer">👁️ 7.49K · <a href="https://t.me/farsna/437776" target="_blank">📅 23:26 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437775">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c4061961db.mp4?token=Ja5EsclR9DCu3TMNgNZ6cPvuwWVeIV3pgERC8AyFru2WkUamG8aVBjy3eovFAbkjZLALioHv_4tkkzi52nSspjb9JPR25hltWSKcFjO5niPvkWLogq75vXuSriR-ygY41qlSFBG-lWqFBMCMQeJg9pQAtOzt6rz6qgSw-oBmN8XvEE6abH1fqdhVKkN7Ns0io7LuJOH4eSaFR9qh1zP43ptlnUt6C6m0PBuwNtpj1mKQwhJFvwMmcnXkftmPsL4xnfDwCO69CZbT9A3yfCjekEPe5PuWkoFdpeL-d4nhICWDQbuSAdnJXV-gfGpT5iirUt4Nye9YAsunrRpW6NgToQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c4061961db.mp4?token=Ja5EsclR9DCu3TMNgNZ6cPvuwWVeIV3pgERC8AyFru2WkUamG8aVBjy3eovFAbkjZLALioHv_4tkkzi52nSspjb9JPR25hltWSKcFjO5niPvkWLogq75vXuSriR-ygY41qlSFBG-lWqFBMCMQeJg9pQAtOzt6rz6qgSw-oBmN8XvEE6abH1fqdhVKkN7Ns0io7LuJOH4eSaFR9qh1zP43ptlnUt6C6m0PBuwNtpj1mKQwhJFvwMmcnXkftmPsL4xnfDwCO69CZbT9A3yfCjekEPe5PuWkoFdpeL-d4nhICWDQbuSAdnJXV-gfGpT5iirUt4Nye9YAsunrRpW6NgToQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سردار نقدی: دشمن با بمباران سنگین تصور کرد که نیروی دریایی ما را نابود کرده اما نیروها با پدافند غیرعامل خیلی از امکانات‌شان را حفظ کردند
🔹
اگر آن‌ها نیروی دریایی را نابود کرده بودند باید ناوشان راه می‌افتاد و از تنگه عبور می‌کرد.
@Farsna</div>
<div class="tg-footer">👁️ 7.31K · <a href="https://t.me/farsna/437775" target="_blank">📅 23:21 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437774">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a5abb24be6.mp4?token=Z2p_RTdaWTDlyBLQlFQP5Vm1cu7arxas2Z970b0rqCxnAotGwwqWzk7TZNOPTaLQpuxxUvT05FdrmeC2OwGgTSLBb4wmk_VIM3Rcu_T-zBYdhCaUYfb3Jw4UIDWbjZmnIQJ6U4WmmrLcnrHRXfntPLLdyGz1ax02m1MSO-UoV6Obgiwkyq24l7MpqAoIOwssYUfkQF0DhBA9THtv3vcYWlBXhkHpacM44HsnUriSkBQGNSj3pX1K9a8rvxL104T3yqpHLswSSREHlD02fyelwMZiijZO4TB9v2YPdX4SMH57-G0o3_1-Lqs5ricWBTH2mLWN0pQn18Lu48RGZtKtFkBV6amS_Ur53D58eEHi0Cu7dpPKyKW9caYvsRwDQnigR8ID7hyNoojS2xDSFSR_tnWD8GVM7pZXUQkj8Q9Gxp8AbYl5DqM7aio6lUZdFQ9QYYPoGq8dVbWu8iTsCR12XCk0wOhxQnUhMls9Vv9xU8bczkxNh-jALDz2y3aN-AL_Mp5QG7UJxBndKlDa-sAEeAFdK_Zg8uBHUewLJBtorkKghwW25gNoi3yjdlQGC27g9_0oMhL3c8vJi23us0gry6bILmCnHVdLGJsDwoJT7BJZOtUvntPCRK2ylcsxbjOEyOmg4n41lT225dSg-vfUOrhPYLj9vaOAAYyxX_AvdWE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a5abb24be6.mp4?token=Z2p_RTdaWTDlyBLQlFQP5Vm1cu7arxas2Z970b0rqCxnAotGwwqWzk7TZNOPTaLQpuxxUvT05FdrmeC2OwGgTSLBb4wmk_VIM3Rcu_T-zBYdhCaUYfb3Jw4UIDWbjZmnIQJ6U4WmmrLcnrHRXfntPLLdyGz1ax02m1MSO-UoV6Obgiwkyq24l7MpqAoIOwssYUfkQF0DhBA9THtv3vcYWlBXhkHpacM44HsnUriSkBQGNSj3pX1K9a8rvxL104T3yqpHLswSSREHlD02fyelwMZiijZO4TB9v2YPdX4SMH57-G0o3_1-Lqs5ricWBTH2mLWN0pQn18Lu48RGZtKtFkBV6amS_Ur53D58eEHi0Cu7dpPKyKW9caYvsRwDQnigR8ID7hyNoojS2xDSFSR_tnWD8GVM7pZXUQkj8Q9Gxp8AbYl5DqM7aio6lUZdFQ9QYYPoGq8dVbWu8iTsCR12XCk0wOhxQnUhMls9Vv9xU8bczkxNh-jALDz2y3aN-AL_Mp5QG7UJxBndKlDa-sAEeAFdK_Zg8uBHUewLJBtorkKghwW25gNoi3yjdlQGC27g9_0oMhL3c8vJi23us0gry6bILmCnHVdLGJsDwoJT7BJZOtUvntPCRK2ylcsxbjOEyOmg4n41lT225dSg-vfUOrhPYLj9vaOAAYyxX_AvdWE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
عزاداری شبانهٔ مردم مشهد در شام شهادت امام محمد باقر (ع)
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.96K · <a href="https://t.me/farsna/437774" target="_blank">📅 23:20 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437767">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">‌ رأی محاربه در پروندهٔ شهید آرمان علی‌وردی به‌زودی صادر می‌شود
🔹
صدور رأی دادگاه انقلاب در خصوص اتهام محاربهٔ قاتلان شهید آرمان علی‌وردی نزدیک است. این درحالی است که پیش‌تر شعبهٔ دیگری از دادگاه تجدیدنظر، حکم قصاص صادرشده از دادگاه کیفری را به‌دلیل اثبات‌نشدن…</div>
<div class="tg-footer">👁️ 8.02K · <a href="https://t.me/farsna/437767" target="_blank">📅 23:04 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437760">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mPJIamyiq-dad92Q5ypNyKEkdhzQG-EYkOUgD7q0L5KxXLBia-gyKHoP9uE6eg24vLvhc-e9SgsqDI8mwx4GARYYcuE3LFpUUG0LHbXLyJJveS2nzQ4R3FaEr3NdT_du7RXzZ9Y9vFa19jpvwmsoAXJWaqM1mIyeJEe9Tiivkd-Qnc4fheVLXuzqj6XTAQZOEDH3eLOk8Bo5e6Lr9pZIq9CKpkao0XsaxKH_Yojb8mbvfilojQ2uAakVc8KcuN9B7PcpCLwfJgPxk8sFC94ng-XMTjDIgs52faBygyMqegzN3rYvno9LNPSNlAp8Ix8-BnZoENZ6tgutHXKTWV8eUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TTbzZ17Pq19_rt_6Xn57iD_4_nfN1Gi8AeO4AXvhMAwd1B6XW7l2yDT5-FTno5HZ7yMNSHs2Q5H8T-1MpQc3ofi84pCWr0oYJ1uGcs7ZCMV8ALizfqD89-nI2Z0wBMYvhkWmz9cPZafFnh1kcfVavxN7ztt2joVqxYdqTCci_N23gc5OhBf8zDd69Yct4ZjRNvBc6d9-ol194RNbtp94NHv2FKCQjCegCItydmt_5QSEoWiprDF9frbK4AFHKqdvRQ95Hd1ny94zUKUtaiOfyU1efqvEK_9kdop4P9TWntRfqPiuf4JBwLL5bzdI6y2x6Czm6_dDDhv9b64VaUvOMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AB43i6PBov3Fc8YekKNJSSxnfA1gl3hT9khsHFDvRun2mvCwYrvJd0OafW5Gwuh_ZOrsXaa0l_eYbVbzoIuP-HJuFfLTAYIEYu6KnhnOx5_PYw-pzrOOlUdQ9H1_Q5nnF7NXKyueFaligdoCdHSwlAbY6aj1zEhdVRX5TtE9bqbk5LSieAZRFea6dvzZOlwSxsDbqOWBa2RIdSKCvaSPNDl8m04qZ9YAk0aNAND3appUrcdvSgJmikL_ZZdzcOk7Y-wTQqepAe6yIkRRJB8OaDgPJCCfIdH3pJ_qMx4ppVxwL2xV0tA0iunDvOqkVNJdCT4SZRDfwWkGlOwBLncxcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cqQZ-UKXiJZIzs6Jv9DbPSsa8q-ZKJRIiqSMh4Eree_TJdsgYyV_d24kxGP4412aMKGrx-pa6rZ8Lf20TK_fE_vRww9Ijx5EN_ZLKKcGQC8spqwg4T1-SzIL97kvW_iApOuI_WamsdbAMbaeRftBSAiLyHILVVA2q9099G4FBAR3CAorP2higrqJFmR-TNDIluvM_dnTBvNUtqRikm7sGh0z0yJ2U8t0Y5LP88g61KEeWON-eKS2QZKPSTzee7ueHYwC7BhmT7MM1l4y5Gziz3p9sBSxXmCXtFg_3ab4HC_CEtFGN2-utnQyCLyldfpicZPMqwkDQ8trh_AdxbQhcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/O5vTf5eg0e0HiAuKd6jSyCw7TrRJTgsMaDV9zi7UEZZLYrMFyGKbPj7_lxepKfKxO2wZLJUM8_GoT3UxiArxqyCaLadQgNfY1oQuKeyoUSEjdFHU3W3IXJUEB0RUFYmMAZe_QGYAhAUet-Dh0SPW5XVVkGRdOvhO9dt-1iLl9f54WSe5BAQGnCxfEO5mB_ftjJw5ZGG6oZZMEABUQwRdwbc5dUkHQbhcBlWUlvddS91dU-ZlDRToNLbiDN3VCEcYxBmgApcUik8kIQnAIyIZ0sWhYIc3MgI9_oA70mWu1l_VtasW2zT-7PakGhUzVwmLJLJbsEGdm_jb1lFAhHY2CQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/suXF56NEgsABzNBj98HYE_fzMDqUS57pPYkmNNpuaepfK_JiNB_enHOf1wgaKktJ5kecM3StTIzxvWCx73WFTkyvQ9DfditG3Jep60_-UNSOeS6J2yvlEdYtdJgICQCV2WsaihQsKsnbS1I-KoGqJpwwf6eLeyH7GFgyV8EbCDZKgw1AR7jPC3NzZOT8KxKiXWDNIZDCdLPAjWgq1FUpjP1PXa2LcrULjBbNLWsQKDoiTg6xISrUfz2ljwzbhECjl-Q_rrS1SEZQu3lWgqkRFssTw18gK0CUe95dJw3pp4K1BqdJyGGIYuI0vnN0t-D22xell1DqzqI8ymTyKvRDJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nrz1F3Cpc56e9g-3RNGApqB0vt0G-x_z1fvo88jXcSckUmFI0U1W-pukBYsXeI3BcTn91PuusBza_4t7ojSsB6fE5CW_dP4isO2j4s_yQ8F250u1nWcNOELuUJ6cv1FxkGl3KJSxcXaq293ULfqu8Y4G4Y30zuKGbBJ_gR-05SJk1etqHkPXFAWhE0-HV4zS3Z0ro-Wwhpxsw02XFGyOzgMco9NWRnSvx5BcuxxFuEbee0GdvgTVSUjhRajsS3MSffL8RIHTXNxShtlZv_WdkjbuUygdcFjJ85YNuseD47z5OR-Hb7oBTJnNBLaaAlJe4r8CLh2QJDRuieQccEURPw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
حریر سرخ گل انار بر تن کویر یزد
عکس:
علیرضا رجب‌زادگان
@Farsna</div>
<div class="tg-footer">👁️ 6.8K · <a href="https://t.me/farsna/437760" target="_blank">📅 22:55 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437759">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/32607a3d2b.mp4?token=VP3Y5nX_TfUvVT0Q7dL620zX534Ki2LEX7a0KE4zwJ8OIj4CfbUiy9zwWZslvwziFt8gR3T3AUxu4xJZndQh9g9dvSALwqZO1_ZUuSzvLtmv2qUhCjTExsvXJBPeY7anWUtkh88nYRo9m5vGPywcBgF_xaSSEgbX-GmfpusjbL_8h0pVzA64ueiEIUZ3YHo_4ZNJ89H8GgRFgvr30heoUJWmyXfQZnoW2DP8hSxwe3C8Iy8Ly35REsRH6_2c8CKJ__XQFgFlQXXHnf0nh9VaZw1Gl4ugw34XIhYElXJ2LppXhbKtDyTd2DGNdjANvU-ykQCTuZg5WbmGTEPf87doaQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/32607a3d2b.mp4?token=VP3Y5nX_TfUvVT0Q7dL620zX534Ki2LEX7a0KE4zwJ8OIj4CfbUiy9zwWZslvwziFt8gR3T3AUxu4xJZndQh9g9dvSALwqZO1_ZUuSzvLtmv2qUhCjTExsvXJBPeY7anWUtkh88nYRo9m5vGPywcBgF_xaSSEgbX-GmfpusjbL_8h0pVzA64ueiEIUZ3YHo_4ZNJ89H8GgRFgvr30heoUJWmyXfQZnoW2DP8hSxwe3C8Iy8Ly35REsRH6_2c8CKJ__XQFgFlQXXHnf0nh9VaZw1Gl4ugw34XIhYElXJ2LppXhbKtDyTd2DGNdjANvU-ykQCTuZg5WbmGTEPf87doaQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
توصیف خداوند از صهیونیست‌ها در قرآن کریم
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.27K · <a href="https://t.me/farsna/437759" target="_blank">📅 22:50 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437758">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eff13ad0b3.mp4?token=viq-oZBt1QnIVmevu7ZJgHPFlfrjdt2EejYlJ3fEnFsosSOkmcQj6Wv6ihrKDLrOcPOoLD1BHfu6M0N7eHbqyZNvsvW-vMww8FMP2eOigO1dyJIWkQYrTU4dicAilElt4eF1KybPc5dNh6ivtzbvU1hWR_pYtqSsTVkHl3zzMqLVfQ-rDj86ojfY2FowycdZwcGmWc75nlkqDmn06QmtKBd2uLkgH6Jbbi5lDiWzGSscz2KIn4m7iAeaXO0Exhtewp9PiZNseP2LgrLn7O1LTr6lMsFMDeegj8PxRSTAh62nvnp3egdL_ZyIe8bWprJHaVLlJaaAEYQ2-ktkichYPw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eff13ad0b3.mp4?token=viq-oZBt1QnIVmevu7ZJgHPFlfrjdt2EejYlJ3fEnFsosSOkmcQj6Wv6ihrKDLrOcPOoLD1BHfu6M0N7eHbqyZNvsvW-vMww8FMP2eOigO1dyJIWkQYrTU4dicAilElt4eF1KybPc5dNh6ivtzbvU1hWR_pYtqSsTVkHl3zzMqLVfQ-rDj86ojfY2FowycdZwcGmWc75nlkqDmn06QmtKBd2uLkgH6Jbbi5lDiWzGSscz2KIn4m7iAeaXO0Exhtewp9PiZNseP2LgrLn7O1LTr6lMsFMDeegj8PxRSTAh62nvnp3egdL_ZyIe8bWprJHaVLlJaaAEYQ2-ktkichYPw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
شعار امشب شهرکردی‌ها: ما مرد این نبردیم، بجنگ تا بجنگیم
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.89K · <a href="https://t.me/farsna/437758" target="_blank">📅 22:47 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437757">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V56kk9uaFIWDUf34JQMjy9cdzl-LQNSZfwc5Gpk2JvCIhl4SxXXJfWF5KIxlB7kXvDtBF7v2ann660sYLnpuk4vurajg_93VSVT76eMml633dDDUZyt7uRAkvQNI_M6za_bucgi100yygrOouqAHOUL0iDqwjkGOkEsr1ohedr_2BuN7_Ex24wkw6K7yt-Cy6yO_pVR7Tzm19N6393aS1xQrh4zlsivYi9PxlECbQdF8jR0ihI4BlXc7F2MR9bkmvQVI4Lu16h2IM1XnB3Ddpjmuoy89JxD5S7E9fBj0UC6DAyFZ8BeGkVP46mcDJI12ZDCcKW7UNn48YomK9mgHTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سردار نقدی: دشمن اگر خطایی کند، ضربهٔ جبران‌ناپذیری می‌خورد
🔹
مشاور عالی فرمانده کل سپاه: ما توانستیم یک بازدارندگی در مقابل دشمن بدست بیاوریم آن هم از این جهت که دشمن متوجه شد که نمی‌تواند مقابل ما به نتیجه مطلوب خود برسد.
🔹
یک بعد دیگر بازدارندگی هم این بود که دشمن بداند که اگر بخواهد خطایی کند ضربهٔ جبران‌ناپذیری را خواهد خورد.
🔹
امروز این بازدارندگی برای دشمن مشخص شده بگونه‌ای که ۲۸۲ نقطه نظامی آن‌ها منهدم و نیز صدها کشته به دست دشمن باقی مانده است به نحوی که بسیاری از آن‌ها را مخفی کرده‌اند.
🔹
روزانه یک هواپیمای ۴۰ تخته بیمارستانی از امارات و یک ۱۰ تخته از کویت مجروحان دشمن را برای درمان به بیمارستان‌های آمریکایی در آلمان منتقل می‌کردند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.52K · <a href="https://t.me/farsna/437757" target="_blank">📅 22:33 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437756">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/463146e110.mp4?token=WJt0P7ZlWjT1jhG8eBzK2mxABaAPpan47HGOpqtMpTqO6XC88DVIG4ua1wlHTUYHaGbBy4vRvu3QBnwv7j5kKM1d8qV0xsIqSBXwAmszVb2VG0LRg3bEW1-rBRh85AeSTchCxrUmVP8mEXuDpq-QF9dqUCgx_ur8HHygoCGnFCjjhcX-p0cYu5IY-7wG6a71o30wm7kr4le6Sg2b1mA1tycKRytXBiwyayo2q8La9KONb2khD4eBxyopGFp1V20rGTt7UGtcxk1Rb8B5jBGsyUO7XQ5eBeHK5VwRiJexH39mwdFzQYTWsQOuLgtEHtVWbcZn2_A7ngU7GyGXchDYUDcpT3rOa1ptLtgBzfENXjcIRzCaQKNPsA1AdaEPjO-cDHlrAsJAvzkv7cpAIZtm45T_0lk6zOfVDpNxDQTpWL6x-88t8s2eDmgPi7imj8u93iqhaUOaSfduvqBYBhcAPypqIc2IWYhbanuypdfzZz4Zn3Yw0RnbEXRVR-TYPcH7hi1LNN0_sbHDlxiRw5-PTPBhNtP8_rLQgOH6_Ah-iZg2Ab7RyMCDIdW07hs6Fyc-zhZdd9siW1cxP4LsF2jLJnuYdUKD8hxp_W_IdMcJ18LR3ilVMu-3chCOboTMpMuN6gCQOEGkgQnRPNiOGSNp5MssG4wVeu04T6tbywAFQA0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/463146e110.mp4?token=WJt0P7ZlWjT1jhG8eBzK2mxABaAPpan47HGOpqtMpTqO6XC88DVIG4ua1wlHTUYHaGbBy4vRvu3QBnwv7j5kKM1d8qV0xsIqSBXwAmszVb2VG0LRg3bEW1-rBRh85AeSTchCxrUmVP8mEXuDpq-QF9dqUCgx_ur8HHygoCGnFCjjhcX-p0cYu5IY-7wG6a71o30wm7kr4le6Sg2b1mA1tycKRytXBiwyayo2q8La9KONb2khD4eBxyopGFp1V20rGTt7UGtcxk1Rb8B5jBGsyUO7XQ5eBeHK5VwRiJexH39mwdFzQYTWsQOuLgtEHtVWbcZn2_A7ngU7GyGXchDYUDcpT3rOa1ptLtgBzfENXjcIRzCaQKNPsA1AdaEPjO-cDHlrAsJAvzkv7cpAIZtm45T_0lk6zOfVDpNxDQTpWL6x-88t8s2eDmgPi7imj8u93iqhaUOaSfduvqBYBhcAPypqIc2IWYhbanuypdfzZz4Zn3Yw0RnbEXRVR-TYPcH7hi1LNN0_sbHDlxiRw5-PTPBhNtP8_rLQgOH6_Ah-iZg2Ab7RyMCDIdW07hs6Fyc-zhZdd9siW1cxP4LsF2jLJnuYdUKD8hxp_W_IdMcJ18LR3ilVMu-3chCOboTMpMuN6gCQOEGkgQnRPNiOGSNp5MssG4wVeu04T6tbywAFQA0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
استقبال تماشایی پاکدشتی‌ها از پهپادهای شاهد۱۳۶
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.27K · <a href="https://t.me/farsna/437756" target="_blank">📅 22:22 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437755">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7d5944a623.mp4?token=HhrtY_SVOznvuWVwqfCYwYcDe3WfUtlB6Cam6kvKem5Ltr-vByobwoFG8roNuULM6p0nKutK7YNvFLraRfdL6jXdXsNLc1_ZVyvJa5D26_BRwLHBTOu98wPNO_n9tTZd4OQ6eCW3C0C0ZZxyU-FoIb6Ra5EF3wMifqLHYcmHJtNBG485yHDx8D7-T9lDLrWsK5YKTFNRt8qid_yAvWLIT9B9ra7sHVTriTUhFkc_QgdbHRUyXUKnpcvmuu1e5k3EBm-aPRVRStIDA2o3EGWTSitT6i0TVPP3fvIkRKOoIt_pl_5fj2ZE7DkIoUhCicJwee1xG-VMAiw8MRJSibDnrYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7d5944a623.mp4?token=HhrtY_SVOznvuWVwqfCYwYcDe3WfUtlB6Cam6kvKem5Ltr-vByobwoFG8roNuULM6p0nKutK7YNvFLraRfdL6jXdXsNLc1_ZVyvJa5D26_BRwLHBTOu98wPNO_n9tTZd4OQ6eCW3C0C0ZZxyU-FoIb6Ra5EF3wMifqLHYcmHJtNBG485yHDx8D7-T9lDLrWsK5YKTFNRt8qid_yAvWLIT9B9ra7sHVTriTUhFkc_QgdbHRUyXUKnpcvmuu1e5k3EBm-aPRVRStIDA2o3EGWTSitT6i0TVPP3fvIkRKOoIt_pl_5fj2ZE7DkIoUhCicJwee1xG-VMAiw8MRJSibDnrYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
یاد فتح‌خرمشهر و مقاومت در خیابان‌های گناباد خراسان‌رضوی
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.46K · <a href="https://t.me/farsna/437755" target="_blank">📅 22:11 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437754">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6192c2756c.mp4?token=UxPfnlNE8Men-ooenP18HAp4i_p8sjiXZVTtyg20-C8-_78k3Slv4iz41OahNJ5nNHjlyzB_MILk5CmCcUkuihgMlVxf427wEi2iZWKOEEar5TlGzyweBktbiM8ClEnKvonE44nHAK7CWg72OvPguOCykB8kvMt9PnyywQk6nWKiS-H9pmFoU9aeWyzM9O0pCASXeXX6mPiZZhj_5rILt6fGdoGrEv3dnk6YPfhs0AzhLtvL7lCs5HSwRoY-qPf5H1teoh_ECnMUjbgmftoHJfMyhMYn7FosSqQfIcUg2XFmaMieuec_JzxhTubm8ulLQt_7O0_DQI_fYmQxeJCc7Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6192c2756c.mp4?token=UxPfnlNE8Men-ooenP18HAp4i_p8sjiXZVTtyg20-C8-_78k3Slv4iz41OahNJ5nNHjlyzB_MILk5CmCcUkuihgMlVxf427wEi2iZWKOEEar5TlGzyweBktbiM8ClEnKvonE44nHAK7CWg72OvPguOCykB8kvMt9PnyywQk6nWKiS-H9pmFoU9aeWyzM9O0pCASXeXX6mPiZZhj_5rILt6fGdoGrEv3dnk6YPfhs0AzhLtvL7lCs5HSwRoY-qPf5H1teoh_ECnMUjbgmftoHJfMyhMYn7FosSqQfIcUg2XFmaMieuec_JzxhTubm8ulLQt_7O0_DQI_fYmQxeJCc7Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حضور پرشور خرم‌‌آبادی‌ها در شب ۸۵ تجمعات مردمی
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.49K · <a href="https://t.me/farsna/437754" target="_blank">📅 22:02 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437753">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">🔴
حزب‌الله: یک افسر اسرائیلی که در اتاقی در منطقه اسکندرونۀ جنوب لبنان مستقر بود را به‌وسیله پهپاد هدف قرار دادیم.  @Farsna</div>
<div class="tg-footer">👁️ 6.27K · <a href="https://t.me/farsna/437753" target="_blank">📅 21:54 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437752">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/60fe3e3dbf.mp4?token=UNe_2iJJpMUNtlhMsIdQPRw1YqkeD1N2byum5WLjw_3ix0F-9oGkPbBh8WTkyRxHs9wx3zdh9nZFUNwHUaezaCP-TzZ6ycXEt66ST2MNbbSiA3_m3DPLYyr1VAFt3uGAb5K8ZQXQeI9q-uSyZ9Dt7xp4Wj2vrkPcWvrgviGjl30uU6S2Umad-RhJaoDvVPYUywRVlpw7bzBQS-gAoEIZtsUM7auJChIdtTAEm3HVpBGycODUU9txVUjIFUbcr0_W4uHweTr_JicWAG5t4FX6GHo0B43Na2g5KKcd47PaWmil034izLsO2QDOmS1n8rVOCNup_cgWJpbD6Ms0Lk_aNg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/60fe3e3dbf.mp4?token=UNe_2iJJpMUNtlhMsIdQPRw1YqkeD1N2byum5WLjw_3ix0F-9oGkPbBh8WTkyRxHs9wx3zdh9nZFUNwHUaezaCP-TzZ6ycXEt66ST2MNbbSiA3_m3DPLYyr1VAFt3uGAb5K8ZQXQeI9q-uSyZ9Dt7xp4Wj2vrkPcWvrgviGjl30uU6S2Umad-RhJaoDvVPYUywRVlpw7bzBQS-gAoEIZtsUM7auJChIdtTAEm3HVpBGycODUU9txVUjIFUbcr0_W4uHweTr_JicWAG5t4FX6GHo0B43Na2g5KKcd47PaWmil034izLsO2QDOmS1n8rVOCNup_cgWJpbD6Ms0Lk_aNg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مردم اردبیل امشب زیر باران هم پشت کشور را خالی نکردند
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.28K · <a href="https://t.me/farsna/437752" target="_blank">📅 21:53 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437751">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mjWmlRhVW7scDrbPvjqLD7Kv4SVuW-nSwPJd-Em-fk0RzzNzksu0Bbi-et035B1YkJfMAlQWMWCLHrnisZBKKYKzQCEaukm3hvVtyd-k0uoVdnKYyOEjsUtp8HLt8WRkp4IJACmQWgMy9U2ifScS7x1ZcbzG8JLQZ0SyZPGx_t5A5IxMQ3LmmNZH9936bTL1DIKUQDvnaPvJwvjOKQNzE1HtW2Af_pkCcW7UKLy1l6t_4dA3ZWnsixhwr3Z5QWB0Cnpnug_Ym8RxVzEfJH4ctozRglWI_eqncmSM-Pjm4-7Y6DOT1MDAgt-Yx1gC-qrZhhXrD59aWQeWdHcxV0IndQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">منیر قصد ترک آبی‌ها را ندارد
⚽️
برخلاف انتشار برخی اخبار دربارۀ احتمال جدایی منیرالحدادی، خروج از استقلال در دستور کار این بازیکن نیست و او فعلا به قراردادی که با باشگاه ایرانی دارد پایبند است.
⚽️
مدیران استقلال به الحدادی اعلام کرده‌اند که مطالبات او به زودی پرداخت خواهد شد و گویا این موضوع مورد پذیرش ستاره مراکشی نیز قرار گرفته است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.87K · <a href="https://t.me/farsna/437751" target="_blank">📅 21:41 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437749">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🔴
حزب‌الله: یک افسر اسرائیلی که در اتاقی در منطقه اسکندرونۀ جنوب لبنان مستقر بود را به‌وسیله پهپاد هدف قرار دادیم.
@Farsna</div>
<div class="tg-footer">👁️ 6.65K · <a href="https://t.me/farsna/437749" target="_blank">📅 21:33 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437748">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">توضیحات قوه‌قضائیه دربارۀ حکم قاتلان شهید آرمان علی‌وردی
🔸
رأی اخیر صادرشده در پرونده شهید «آرمان علی‌وردی» مربوط به موضوع قتل در دادگاه کیفری است.
🔹
پروندۀ دادگاه انقلاب مفتوح و در حال رسیدگی است. براساس رای دادگاه کیفری، پزشکی قانونی در مراحل مختلف علت تامۀ…</div>
<div class="tg-footer">👁️ 8.29K · <a href="https://t.me/farsna/437748" target="_blank">📅 21:17 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437747">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DTRSebci-ESASkGK7D08YMG2xshOYMAGfE7dMNTqCaujeezA2FUL6iXdW728wQw0hGQPbznWwfcNsiJTU52huj7YVaVffOAoFPxQVASrMYktgO5skylSP5e9TyHwkuzgzKU4Lv0ca_PR265P36s5wlBeIQH8OJccGZpNNVHdTW9U0uKz63j65vVz3fIU7gENYcBsFBMJpFC0zZZC5CO9qI98NqM0Kfiuh9Ae0VSo3xZ6sWfEewUxw9c8VXvzAAmHhsCpDwir_LIpNnIQojObmkpppTcy5ZBB0aosA850uxZrZsMl-yPE4Cg3IF3z5FjHLWhVyPX8I0ZrZAinamIjmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حنظله: در صورت خطای دشمنان به شبکه‌های دیجیتال و انرژی آنها حمله می‌کنیم
🔹
گروه هکری حنظله: در صورت ارتکاب هرگونه تجاوز یا بی‌مبالاتی از سوی آمریکا و رژیم صهیونیستی، حملات سایبری ویرانگر فراملیتی علیه زیرساخت‌های انرژی و دیجیتال کشورهای خصم اجرا خواهد شد.…</div>
<div class="tg-footer">👁️ 6.8K · <a href="https://t.me/farsna/437747" target="_blank">📅 21:13 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437746">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5431e8e1d7.mp4?token=D8CdcdUe5GxKpn1xsbp8_-ChC73w76e4r2UKHxkodw8DZ6CIiCkrVQCovDPYaUWJKAwk-s0q_cQpzCf4if6-QCKJ_v0he9KbRmzjTbEwudw6ur6kdQz7TUy5Rd1YawFcwqCF4oX4KFQZqWxE--JkLjQKCIN6xDPCnQI1Vxfd1ZFHmySNTJFvgxW6S-Ijb60P89zmyI2VBdsmo2ajrp-cLeb12R9K57Wm0jhqQ3Loc-Z75DZX10Lr6Q-jVtyUr3wMVDamAFG5SW9tOX6v7Ywiymo6iXNialmXJFIRFdcXHzMjD93Lhoth67uXyqOK2g2FXblj6BLIeEa4IoWC4c_k4g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5431e8e1d7.mp4?token=D8CdcdUe5GxKpn1xsbp8_-ChC73w76e4r2UKHxkodw8DZ6CIiCkrVQCovDPYaUWJKAwk-s0q_cQpzCf4if6-QCKJ_v0he9KbRmzjTbEwudw6ur6kdQz7TUy5Rd1YawFcwqCF4oX4KFQZqWxE--JkLjQKCIN6xDPCnQI1Vxfd1ZFHmySNTJFvgxW6S-Ijb60P89zmyI2VBdsmo2ajrp-cLeb12R9K57Wm0jhqQ3Loc-Z75DZX10Lr6Q-jVtyUr3wMVDamAFG5SW9tOX6v7Ywiymo6iXNialmXJFIRFdcXHzMjD93Lhoth67uXyqOK2g2FXblj6BLIeEa4IoWC4c_k4g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پرچم‌داری لامردی‌ها برای ایران
@Farsna</div>
<div class="tg-footer">👁️ 6.5K · <a href="https://t.me/farsna/437746" target="_blank">📅 21:11 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437745">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">الجزیره: ۲ چالش در مذاکرات ایران و آمریکا وجود دارد
🔹
اولین اختلاف دربارۀ لبنان است؛ آمریکا خواستار آن است که نوشته شود اسرائیل می‌تواند «درصورت وجود تهدید» اقدام کند، اما ایرانی‌ها این متن را رد کرده‌اند.
🔹
درباره دارایی‌های مسدود شده، ایران خواستار آن است که در چارچوب همین تفاهم‌نامه، دارایی‌ها آزاد شوند اما آمریکا اصرار دارد که این اتفاق در یک توافق نهایی رخ دهد.
🔸
انتشار روایت رسانه‌های خارجی به منظور اطلاع مخاطبان است و به معنای تایید ادعای آن‌ها نیست.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.44K · <a href="https://t.me/farsna/437745" target="_blank">📅 21:03 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437744">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a6a41256a6.mp4?token=DIJJdZdcH1_D4kOwt5p9mifW8BsPv1dVdhsWWdF9a4VXnDAgjtOsbZoVrXyqBKbWiZ3HbGw4INZ7d52xyN373AuOmL23wQMejM0ChfFPSDkPI3zmIbL24F-HgWPzZHm-BtATCXkSLH0NQTE7YOQfPWnCjiV1-ZqGmM4-VHmUvOc_Wn_byJUH5C8Bz66XlfuZ-HINFfzBQyxMBjhhJHAYjJ432A0bMP_WQbY0cEzEUGzlF2ACo_XDeV-4b4NGt9yx-PHJX0kGMpsKSVjYtefRj6LtIGfO8fB2sXv1MH5U7ALrEEJTyhuDGR4U0dLDLcylk30ZkB9BX2p7RPZT90tsJQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a6a41256a6.mp4?token=DIJJdZdcH1_D4kOwt5p9mifW8BsPv1dVdhsWWdF9a4VXnDAgjtOsbZoVrXyqBKbWiZ3HbGw4INZ7d52xyN373AuOmL23wQMejM0ChfFPSDkPI3zmIbL24F-HgWPzZHm-BtATCXkSLH0NQTE7YOQfPWnCjiV1-ZqGmM4-VHmUvOc_Wn_byJUH5C8Bz66XlfuZ-HINFfzBQyxMBjhhJHAYjJ432A0bMP_WQbY0cEzEUGzlF2ACo_XDeV-4b4NGt9yx-PHJX0kGMpsKSVjYtefRj6LtIGfO8fB2sXv1MH5U7ALrEEJTyhuDGR4U0dLDLcylk30ZkB9BX2p7RPZT90tsJQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عامل ارسال اطلاعات مراکز تولید صنایع دفاعی به دشمن اعدام شد
🔹
مجتبی کیان فرزند محمدقلی، از عناصر همکار دشمن که در طول جنگ رمضان اقدام به ارسال اطلاعات مرتبط با واحدهای صنایع دفاعی کشور به دشمن می‌کرد، پس از تشکیل پرونده و رسیدگی قضایی در دادگستری استان البرز، …</div>
<div class="tg-footer">👁️ 6.79K · <a href="https://t.me/farsna/437744" target="_blank">📅 21:00 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437743">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6d5ccfcc1a.mp4?token=aajQukw9VezSzaQ9_mbEovI5DE28Y2Js0pNFuXQ5-WjPYI_pCh5Iqm8fVpKJ-nuJ4w4jJRakiX2tTbIPcmM7nAPkPQ20L55tMM5-04a_kUKwfj3cKomxrOB7tKd5WvlVgXaGgnuSUD1tObXP-bwETp3ejqI7gZmAMeIeqxaLDqZjY6GP-On9VcZSTtVhcyjYuC2jxZsaqsZ1Gr6wcCZJJhUVxp86Xceury7uuvSMOrSyX_2CtBEdZVkhbHdFm9mzD5YHnb715xpFRkua3pbDuNJfXKyChbNGuUWy29GDkYIZJkH09k_dv1WSjzQn8P_YOICFefYdJmD-YBGPW7QJXQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6d5ccfcc1a.mp4?token=aajQukw9VezSzaQ9_mbEovI5DE28Y2Js0pNFuXQ5-WjPYI_pCh5Iqm8fVpKJ-nuJ4w4jJRakiX2tTbIPcmM7nAPkPQ20L55tMM5-04a_kUKwfj3cKomxrOB7tKd5WvlVgXaGgnuSUD1tObXP-bwETp3ejqI7gZmAMeIeqxaLDqZjY6GP-On9VcZSTtVhcyjYuC2jxZsaqsZ1Gr6wcCZJJhUVxp86Xceury7uuvSMOrSyX_2CtBEdZVkhbHdFm9mzD5YHnb715xpFRkua3pbDuNJfXKyChbNGuUWy29GDkYIZJkH09k_dv1WSjzQn8P_YOICFefYdJmD-YBGPW7QJXQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
وضعیت ترامپ پای میز مذاکره!
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.95K · <a href="https://t.me/farsna/437743" target="_blank">📅 20:56 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437742">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/85428879ae.mp4?token=Wx_zGdLMUHVq3y77vsJ_-NuL88x4iUQKVd36XxxoCRICaT5OIPNrNadf80e06t713qiLcB3GttHfVMusVuKUt-DcxMT6aBYRYBBDY29WXxLSop1nVC70L88oNYjH2mzZ4me0ukUFnaKu-5NJaKFupGWGlDNryORbU7GbhSx9dcT2IcMqDEYgT1IbZKH3pIwfoUTEYijpBH6VeCKwBgk3Y1b1bgmVytM_ivwWf9PDPV8oxusqk-bBCbDVhBl08rcM-sVxzEHGxo8ggOCIk_XZRcB114PIRK2nTS5TcNzHoh2yllqcr9i3KyFoDmuogEFH28EUwb92902lELTouKZzmA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/85428879ae.mp4?token=Wx_zGdLMUHVq3y77vsJ_-NuL88x4iUQKVd36XxxoCRICaT5OIPNrNadf80e06t713qiLcB3GttHfVMusVuKUt-DcxMT6aBYRYBBDY29WXxLSop1nVC70L88oNYjH2mzZ4me0ukUFnaKu-5NJaKFupGWGlDNryORbU7GbhSx9dcT2IcMqDEYgT1IbZKH3pIwfoUTEYijpBH6VeCKwBgk3Y1b1bgmVytM_ivwWf9PDPV8oxusqk-bBCbDVhBl08rcM-sVxzEHGxo8ggOCIk_XZRcB114PIRK2nTS5TcNzHoh2yllqcr9i3KyFoDmuogEFH28EUwb92902lELTouKZzmA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
آنچه ترامپ گفت اما «شی» موافق نبود!
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.69K · <a href="https://t.me/farsna/437742" target="_blank">📅 20:47 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437741">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b367509dc8.mp4?token=TK7nJVSuBW23JJMDkCWbkmpoEIV4_BRwnVY68O3AfC2L133wU-EeDaEZMAmPGq--FCgcbefHDxoEJinDzuUnRGJBWOEIaQoEnyq95rqgUknaXb3CtsMdOXzhaigalGs0snmWrDXssuLesTj90KQQh-ySaHfULkH7OPoUGPk4b5smq5zQNDrakvEAxw-OTrhF99d_wkH2DyYBfhf4D6Xer2jUbSLJWeulMgdKO7bKTx_W-f3hYc92I24Hmb7Nmw_3DXk3V6oXRc8d619eNTRjiGgGSjpnjX58bAj9KF8Z-IowS2WETP-372qj5wHcAW5WObYPxd40UVrB7-frmTgcgR-JWW2PpHOS9yy7cDWz1mPFcvB71tDlFpnlShikIuOkZdeFTtCDJ7D5JxvVGqTDHddLe0rlUh8f8Gn7xMap5S8oUj0e6T7p2CrgBDZWk-gbq8Ffs-JJUFWXpk66i6PtwwHYtMDZltpCDF4IKq9W8JhTL9cLPRjUCiKfdvHnuKKgD0NGoefEzo9ufWKgddMjHMNnRzZ8Fr4BV7A3ftC5-YStr18D5bLFEdALjoEmK2DH1Gnb-jFjUvXSp0HsWyLb9xU3K6ijLW_zX1UpVd_SUHJQh-THvbkN0TJ5UgSYQGlVaPpDqr3Mrvap9z0jBbuykkeWXWop9qtf6qomm8HQPJc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b367509dc8.mp4?token=TK7nJVSuBW23JJMDkCWbkmpoEIV4_BRwnVY68O3AfC2L133wU-EeDaEZMAmPGq--FCgcbefHDxoEJinDzuUnRGJBWOEIaQoEnyq95rqgUknaXb3CtsMdOXzhaigalGs0snmWrDXssuLesTj90KQQh-ySaHfULkH7OPoUGPk4b5smq5zQNDrakvEAxw-OTrhF99d_wkH2DyYBfhf4D6Xer2jUbSLJWeulMgdKO7bKTx_W-f3hYc92I24Hmb7Nmw_3DXk3V6oXRc8d619eNTRjiGgGSjpnjX58bAj9KF8Z-IowS2WETP-372qj5wHcAW5WObYPxd40UVrB7-frmTgcgR-JWW2PpHOS9yy7cDWz1mPFcvB71tDlFpnlShikIuOkZdeFTtCDJ7D5JxvVGqTDHddLe0rlUh8f8Gn7xMap5S8oUj0e6T7p2CrgBDZWk-gbq8Ffs-JJUFWXpk66i6PtwwHYtMDZltpCDF4IKq9W8JhTL9cLPRjUCiKfdvHnuKKgD0NGoefEzo9ufWKgddMjHMNnRzZ8Fr4BV7A3ftC5-YStr18D5bLFEdALjoEmK2DH1Gnb-jFjUvXSp0HsWyLb9xU3K6ijLW_zX1UpVd_SUHJQh-THvbkN0TJ5UgSYQGlVaPpDqr3Mrvap9z0jBbuykkeWXWop9qtf6qomm8HQPJc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حماسۀ خیابان‌ها در بابلسر تعطیلی ندارد
@Farsna</div>
<div class="tg-footer">👁️ 6.22K · <a href="https://t.me/farsna/437741" target="_blank">📅 20:42 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437740">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/da32a150af.mp4?token=qYr1p0zdR5eGO4y-bSRIw2Qf1ywGBq2nn32OgVSdje7VBxHSVXhHlps07HC3kVGzwbyo8duWErur_DLaZrA1HEC61NnucP56hcLoCdAnH3SZzY26ztFkqEHzXth6AlFwGMlsaQswtfzBPr7oD2-bGJlCzpt7RXKkJSSam19RpBFLQssBoh21V2JYDKLguGuau3pY8NBbWHVwmJhY2z3P5Lp6TDY__0Fdyz5yMhfMwyk4zCa_YtkzyrPd0LGXa21wuI8lvpnsuzofS6G9jXcddEvd1FcoJwRRrk1bbXiMGhA2kvYn-BjjVrL-s-nbMR7kHYgYJU-9o01vbe0ehdUmUw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/da32a150af.mp4?token=qYr1p0zdR5eGO4y-bSRIw2Qf1ywGBq2nn32OgVSdje7VBxHSVXhHlps07HC3kVGzwbyo8duWErur_DLaZrA1HEC61NnucP56hcLoCdAnH3SZzY26ztFkqEHzXth6AlFwGMlsaQswtfzBPr7oD2-bGJlCzpt7RXKkJSSam19RpBFLQssBoh21V2JYDKLguGuau3pY8NBbWHVwmJhY2z3P5Lp6TDY__0Fdyz5yMhfMwyk4zCa_YtkzyrPd0LGXa21wuI8lvpnsuzofS6G9jXcddEvd1FcoJwRRrk1bbXiMGhA2kvYn-BjjVrL-s-nbMR7kHYgYJU-9o01vbe0ehdUmUw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
انتظامی: من از تعداد، پراکندگی و تنوع قدرت‌مان [تا قبل از جنگ] اطلاعی نداشتم؛ حجم بازدارندگی توان موشکی ما بسیار بالاست.  @Farsna</div>
<div class="tg-footer">👁️ 6.75K · <a href="https://t.me/farsna/437740" target="_blank">📅 20:23 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437738">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hC6SB8cqBrfsxF6VmOOyUC-mQ8R8ckqSqKCBtj7sp-p9VaVE93zHJ8PKzSEbUeCqWft2N-6f4BpEOD75eSnNMFsINkykBIJpsk16UwQR6YGhV5CVF3gepaFmZqJ-FUN0xi5br0GtMJQtya4cgXHNfLyxTcxwCA7icAUDNGI5T6PCkehTBhLRGUMg2NGPrxCs_8mMsv9S82PMR-PVIKuNXs52hRlXVE9FJ6WpxE_zHMFAWUCafI7zDQemsdTWLGrtv4tgcbMv_lLckYwVL5GIF9E56GpXv3USJhe4-U-3jnlyrfXYL2an37L6nfeBUmuIKLBMpJQ1fP56ChypxziWdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۲ راهکار برای کم‌کردن رقم قبض برق
🔹
معاون وزیر نیرو: مشترکانی که حداقل ۱۰ درصد از سال گذشته کمتر برق مصرف کنند، تا ۳۰ درصد در قبض برق تشویق می‌شوند.
🔹
همچنین مشترکان خانگی که نیروگاه ۵ کیلوواتی خورشیدی احداث کنند ۲۰ درصد از قبض آنها کمتر می‌شود و اگر تجهیزات ذخیره‌سازی هم نصب کنند،  ۳۰ درصد تخفیف می‌گیرند.
@Farsna
_
Link</div>
<div class="tg-footer">👁️ 6.39K · <a href="https://t.me/farsna/437738" target="_blank">📅 20:15 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437737">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/22f4a3d2c7.mp4?token=MV6Yx4_uGBbcQK3LDewA5hsdhhQvYwBLPXeRwVRhAC1Dzc515XxS6dYGsmDIpTGZz2-d8LPfX3ohbWAlpH3FKT_trulNNOjT8bSrmHoWav5nzjXUHSxaR9iW4QXRCvdpOHnDyzzPYi8OgsgikDhm1TFAXD53BoxIIhji3rP3YUiKs6EAM2dJveejc67m4yl0pXQOc0jF5AccEkQJ6k7mInoBcJ9C65T22jPQ2oCZULUGyPT3VcwrQygGWBjw2h-dnsgo3J2YKPH-Yhzk7rSNBiOZhcTv8QHPwSqWNlKUSaOUdRwl6APUFiAABR64OUEjBZK39rKGNrdV2G4-5kMS8Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/22f4a3d2c7.mp4?token=MV6Yx4_uGBbcQK3LDewA5hsdhhQvYwBLPXeRwVRhAC1Dzc515XxS6dYGsmDIpTGZz2-d8LPfX3ohbWAlpH3FKT_trulNNOjT8bSrmHoWav5nzjXUHSxaR9iW4QXRCvdpOHnDyzzPYi8OgsgikDhm1TFAXD53BoxIIhji3rP3YUiKs6EAM2dJveejc67m4yl0pXQOc0jF5AccEkQJ6k7mInoBcJ9C65T22jPQ2oCZULUGyPT3VcwrQygGWBjw2h-dnsgo3J2YKPH-Yhzk7rSNBiOZhcTv8QHPwSqWNlKUSaOUdRwl6APUFiAABR64OUEjBZK39rKGNrdV2G4-5kMS8Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📺
اسپرسو با حسین انتظامی  گفت‌و‌گو با حسین انتظامی، معاون وزیر ارشاد، را هم‌اکنون در سایت، ایتا، روبیکا و تلگرام فارس ببینید. @Farsna</div>
<div class="tg-footer">👁️ 6.13K · <a href="https://t.me/farsna/437737" target="_blank">📅 20:11 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437736">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FAjJ0NMQXVr0G6fd5AXE-MagJ7IniDNBkiRzacCKxnGXcN50S5j7dhx0byWVZGbVmaKlULKmql_dSicAA66PrOocEKxYkdzXHuGIZhSu-K0X3IvclmoH-rfq4T02wsnlSOSCpXZPbhPJdLRgcZqbThhAvTsyKMLv_E862VQzvHGzGXe0t9WLsR45P29ol8OrWWYaZiJnQ0yrhlcCLQVYm4AIbHxUBVNQWRG-sz37k2tdzJOjhWq-n5QCj4Dhi04gALIJ3vDH2dM0zRwu9fEeBFSYvtNB6vu1HWJRIeLIOojSWojptMLIMB9G2Bw1cTjBcqvbBlpBmPzeylzjM6ShIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هلاکت یک فرماندهٔ صهیونیست در حملهٔ پهپادی حزب‌الله
🔹
رسانه‌های صهیونیستی: در جریان حملهٔ پهپادی حزب الله به جنوب لبنان، یک خلبان جنگندهٔ نیروی هوایی اسرائیل که فرماندهٔ سابق در این رژیم بوده کشته شده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.1K · <a href="https://t.me/farsna/437736" target="_blank">📅 20:10 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437735">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bb10eda20a.mp4?token=Rp2hzR0OXsxfMyyYBwwZ3z-q0tl9FqJlkQQLtxDTcGLFPuc_Ce9OdraCh-u5SriBQcYBzItmwYY1qSKvdRcwePFy5c32g_kMUQ1JoqP0zEYd8E7007IjOjZPsG0kokW_8cXebzWk80K5PzF2wGbpruAA06-S1vQjmucxUcPR4BJMvdDVu8s8FdrUEe15S_tqakBdlsS6Crqc-FqOTU0selNKMP5-qIrT19KR4GLt9cGzyCJFOvZyfio56xoeFOmlXGV1oGK_cPYeASM0VwhKYPqELDU9zpNPInytmic4P4nzBhUKd3EzUsQDygLAjmPcw6bAZthPkVNL2Nw4utLLkA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bb10eda20a.mp4?token=Rp2hzR0OXsxfMyyYBwwZ3z-q0tl9FqJlkQQLtxDTcGLFPuc_Ce9OdraCh-u5SriBQcYBzItmwYY1qSKvdRcwePFy5c32g_kMUQ1JoqP0zEYd8E7007IjOjZPsG0kokW_8cXebzWk80K5PzF2wGbpruAA06-S1vQjmucxUcPR4BJMvdDVu8s8FdrUEe15S_tqakBdlsS6Crqc-FqOTU0selNKMP5-qIrT19KR4GLt9cGzyCJFOvZyfio56xoeFOmlXGV1oGK_cPYeASM0VwhKYPqELDU9zpNPInytmic4P4nzBhUKd3EzUsQDygLAjmPcw6bAZthPkVNL2Nw4utLLkA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
کاروان خودرویی اردبیلی‌ها به مناسبت سالروز فتح خرمشهر
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.08K · <a href="https://t.me/farsna/437735" target="_blank">📅 20:06 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437734">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">‌
🔴
دبیرکل حزب‌الله: این حق مردم لبنان است که به خیابان‌ها بیایند و دولت را ساقط کنند
🔹
این حق مسلم ملت است که به نشانهٔ اعتراض به خیابان‌ها بیایند و دولت را در مواجهه با پروژه آمریکایی-اسرائیلی که نهادهای ما را هدف قرار داده است، ساقط کنند.
🔹
ما از بزرگ‌ترین…</div>
<div class="tg-footer">👁️ 5.65K · <a href="https://t.me/farsna/437734" target="_blank">📅 19:58 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437732">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">‌
🔴
دبیرکل حزب‌الله: هدف دشمن از این همه کشتار و ویرانی، به زانودرآوردن ماست؛ اما ما هرگز به زانو در نخواهیم آمد
🔹
ما در میدان نبرد باقی خواهیم ماند و سربلند از این جنگ خارج خواهیم شد.
🔹
خانه‌ها را بازسازی خواهیم کرد، مردم ما به دیار خود بازخواهند گشت، دشمن…</div>
<div class="tg-footer">👁️ 5.82K · <a href="https://t.me/farsna/437732" target="_blank">📅 19:54 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437731">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">‌
🔴
دبیرکل حزب‌الله: در حال حاضر هیچ‌گونه حاکمیت سیاسی در لبنان وجود ندارد و کشور زیر سایهٔ قیمومیت آمریکا قرار گرفته است
🔹
مذاکرات مستقیم با اسرائیل مردود است و این اقدام، یک امتیاز و دستاورد خالص برای «اسرائیل» است.
🔹
مذاکرات مستقیم را رها کنید، آنچه را…</div>
<div class="tg-footer">👁️ 5.52K · <a href="https://t.me/farsna/437731" target="_blank">📅 19:50 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437730">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">‌
🔴
دبیرکل حزب‌الله: پهپادهای مقاومت به تعقیب سربازان صهیونیست ادامه خواهند داد
🔹
اگر تصویربرداری پهپادها نبود، طرف «اسرائیلی» هرگز به این خسارت‌ها اعتراف نمی‌کرد.
🔹
رویدادهای جاری در جنوب لبنان، آغاز زوال و نابودی «اسرائیل» است. @Farsna</div>
<div class="tg-footer">👁️ 5.29K · <a href="https://t.me/farsna/437730" target="_blank">📅 19:47 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437729">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZSRi7PuwkVD3lZmBcedLPVeuiTVKPsF_q5xD3l7L4dB_gtkxJCMLROPEKDSw2hPbuKNfaHybfy-AeJiuyb1RwVtjNvzDrZ1B9ndamGKRt5KxvWyTxNXTAljDrS1vxzEeLwEqtKLaQpIXFDhehPuctfZURkwsIuXU01XZW9feLSmjhY8547YyMlLE4Z0m8fOzxLgUvjEKrlgCQgDE-5lB5OVZCsE09zxLHF769_EN18SE9ePa4lBjqqkkEVctP-7rDmdMKZXg80KTUqKqgR3ku1qKS08ac6-dNJXKh4GYtwEEcJ5waarIeaGiPVXJZ31BTUpro2Uu-gwqFbxqgJ-eyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تابستان داغ در جایگاه‌های سوخت آمریکا
🔹
گزبادی، تارنمای آنلاین قیمت سوخت در آمریکا پیش‌بینی کرده امسال آمریکایی‌ها گران‌ترین قیمت تابستانه بنزین در سال‌های اخیر را تجربه خواهند کرد.
🔹
رئیس این تارنما می‌گوید به‌خاطر بسته‌ماندن تنگه هرمز، میانگین قیمت بنزین به رکورد ۴.۸۰ دلار در هر گالن خواهد رسید.
🔹
متوسط قیمت بنزین امروز در کم‌تر از یک‌ماه‌مانده به تابستان، به ۴.۵۱ دلار در هر گالن رسیده.
🔸
بنزین ارزان، یکی از وعده‌هایذانتخاباتی پرتکرار ترامپ بود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.12K · <a href="https://t.me/farsna/437729" target="_blank">📅 19:45 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437728">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">‌
🔴
دبیرکل حزب‌الله: اگر دولت لبنان از تامین و حفظ حاکمیت کشور عاجز است، پس باید کنار برود. @Farsna</div>
<div class="tg-footer">👁️ 4.71K · <a href="https://t.me/farsna/437728" target="_blank">📅 19:44 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437727">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">‌
🔴
دبیرکل حزب‌الله: سلاح تا زمانی که دولت لبنان بتواند به وظایف و تکالیف خود عمل کند، در دستان ما باقی خواهد ماند
🔹
خلع سلاح مقاومت، به معنای سلب قدرت دفاعی لبنان و زمینه‌سازی برای نابودی آن است و این چیزی است که ما هرگز نمی‌توانیم بپذیریم.
🔹
ما خواهان توقف…</div>
<div class="tg-footer">👁️ 4.86K · <a href="https://t.me/farsna/437727" target="_blank">📅 19:42 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437726">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">‌
🔴
دبیرکل حزب‌الله: دولت لبنان به ما می‌گوید یاری‌مان کنید تا شما را خلع سلاح کنیم، تا پس از آن «اسرائیل» وارد شود، شما را به قتل برساند و ملتتان را آواره کند! @Farsna</div>
<div class="tg-footer">👁️ 4.98K · <a href="https://t.me/farsna/437726" target="_blank">📅 19:40 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437725">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">‌‌
🔴
دبیرکل حزب‌الله: مقاومت از سرزمین و شرف خود دفاع خواهد کرد و با هرکسی که در برابر ما بایستد، همان‌گونه برخورد خواهیم کرد که با «اسرائیل» روبه‌رو می‌شویم. @Farsna</div>
<div class="tg-footer">👁️ 5.01K · <a href="https://t.me/farsna/437725" target="_blank">📅 19:38 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437724">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">‌ ‌
🔴
دبیرکل حزب‌الله: تحریم‌های آمریکا هرگز ما را تضعیف نخواهد کرد؛ اگر آمریکا بیش از این خوی وحشی‌گری به خود بگیرد، دیگر چیزی برایش در لبنان باقی نخواهد ماند. @Farsna</div>
<div class="tg-footer">👁️ 5.11K · <a href="https://t.me/farsna/437724" target="_blank">📅 19:38 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437723">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">🔴
دبیرکل حزب‌الله: از دولت لبنان می‌خواهم که از تصمیم خود مبنی بر انحصار سلاح در دست دولت عقب‌نشینی کند تا بتواند در کنار ملت خود بماند.
🔹
ما از دولت لبنان نمی‌خواهیم که به مقابله با پروژهٔ آمریکایی-اسرائیلی برخیزد، اما دولت نباید در برابر ملت خود بایستد.…</div>
<div class="tg-footer">👁️ 5.22K · <a href="https://t.me/farsna/437723" target="_blank">📅 19:37 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437722">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gm9YDYMf8EEkqfsv9rpZsGlh8Pv2uCCfp6i8mavf_Bxk2ibWQXSRmzorLNI41NCVWS5yieaCZIOGiDsk1zS-3RZYsjheNSm7URAV4cEW-wrHLG3daCR66jRoMXLVWm5GC6v8kjcJW55URKsmtT9T-SDxhQiqMfDTClCHZzwFCtIAJ0vwhBUEboPW9mzZTCfLVDL4Bx1CMwVn-Twjl1sobZk0fXJP_AzDjeJkUa6qK7KEnn0EwE4cnA68v48KvXm2dMwjx_4nE5DR_QcFO6RDV3QpxNMIfLCQTJE98_H1yUhhfb3eWmCAwHnNNsXYYrexIeeZSKSdpNj4G_6hzKWG1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۱۴ کشور اسلامی افتتاح سفارت سومالی‌لند در قدس اشغالی را محکوم کردند
🔹
وزرای خارجه مصر، عربستان، قطر، اردن، ترکیه، پاکستان، اندونزی، جیبوتی، سومالی، عمان، سودان، یمن، لبنان و موریتانی شدیدا اقدام غیرقانونی و مردود منطقه جدایی‌طلب «سومالی‌لند» در افتتاح سفارت در شهر قدس اشغالی را محکوم کردند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.67K · <a href="https://t.me/farsna/437722" target="_blank">📅 19:32 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437721">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🔴
دبیرکل حزب‌الله: از دولت لبنان می‌خواهم که از تصمیم خود مبنی بر انحصار سلاح در دست دولت عقب‌نشینی کند تا بتواند در کنار ملت خود بماند.
🔹
ما از دولت لبنان نمی‌خواهیم که به مقابله با پروژهٔ آمریکایی-اسرائیلی برخیزد، اما دولت نباید در برابر ملت خود بایستد.
@Farsna</div>
<div class="tg-footer">👁️ 5.56K · <a href="https://t.me/farsna/437721" target="_blank">📅 19:26 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437720">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mdtvX03dtC4-ry05l-zN0yvBc_ImF3J8egiN16Mbjq272Og9dYBuv_V5Wt9-RuxVWmJ8hSgl-b9mfcdXYmLyC33WkdVNNrwDxwhC5NXW5Az6ckX3LsO7R2NTsgp2xtrx4TGnuwOrLhH77Fw1mQ0HW_xjd-yubFCk4TkNfD4BplbTWsS5K5mFO0-J5Q5gnXptnLLs2HmyPuo87-wdwEGO0sQGmy8McAMmqK37ot2brUPvfod-R60W3sGC-fwpbYGqkuQEC-a-Wqn0IVf-aUIjlz_D9n-hJ478gg9fohrgrbmou8ulEgdBRdjmhM6P-FRCWt2hQ_3D5NhbbPvJ0aNonA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📺
اسپرسو با حسین انتظامی
گفت‌و‌گو با حسین انتظامی، معاون وزیر ارشاد، را هم‌اکنون در
سایت
،
ایتا،
روبیکا
و
تلگرام
فارس ببینید.
@Farsna</div>
<div class="tg-footer">👁️ 5.9K · <a href="https://t.me/farsna/437720" target="_blank">📅 19:18 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437719">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">پیامک انتخاباتی جنجالی در مجلس؛ وعدۀ خانه در ازای رأی به نایب‌رئیسی
🔹
در آستانه برگزاری انتخابات سال سوم هیأت‌رئیسه مجلس شورای اسلامی، انتشار یک پیامک انتخاباتی از سوی یکی از نامزدهای نایب‌رئیسی مجلس، حاشیه‌ساز شد.
🔹
امیرحسین ثابتی، نماینده مردم تهران در مجلس، با انتشار تصویری از پیامک علیرضا منادی، نماینده تبریز و از نامزدهای نایب‌رئیسی مجلس، به محتوای آن اعتراض کرد.
🔹
براساس متن منتشرشده، منادی در پیامکی خطاب به نمایندگان مجلس وعده داده است که در صورت انتخاب به‌عنوان نایب‌رئیس مجلس، موضوع تأمین مسکن نمایندگان دوره دوازدهم را پیگیری کرده و آنان را صاحب خانه خواهد کرد.
🔹
علیرضا منادی یکی از ۷ نامزد انتخابات نایب‌رئیسی مجلس در انتخابات فرداست؛ انتخاباتی که همزمان با برگزاری رأی‌گیری برای ترکیب جدید هیأت‌رئیسه در سال سوم مجلس دوازدهم برگزار می‌شود.
🔹
انتشار این پیامک واکنش‌هایی را در میان برخی نمایندگان به دنبال داشته است. علاوه بر ثابتی، چند نماینده دیگر نیز در فضای مجازی نسبت به این اقدام انتقاد کرده‌اند.
🔹
همچنین دو نماینده مجلس در گفت‌وگو با خبرنگار پارلمانی فارس اعلام کردند که در گروه‌های مجازی نمایندگان، فضای انتقادی تندی علیه این پیامک شکل گرفته و برخی نمایندگان نسبت به طرح چنین وعده‌هایی در رقابت‌های داخلی مجلس انتقاد کرده‌اند.
@Farsna</div>
<div class="tg-footer">👁️ 6.98K · <a href="https://t.me/farsna/437719" target="_blank">📅 19:07 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437716">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q1Kv88hwi_M-tfV6cy1GNAm-efIXYlzyEK6aeQJNumwLKT9EupU3HCVOQnV-ju2IY4Jq4GXW0U8_5gxuOQ0vHCE5XRZXX7p4R2WGCc5xMMsplFoKLg7vfQstgne8S91z1HUqrdbTw5A7N2BE4pXyD3uto7lHMT6HYumz5OFX7zTP6Z-6eyZfdpHC90Nc6nWy8o7hoJkQDFC9meQi7YD-CEsKqCsrDhxcNOcQYt8JC_Jv4JzlqQig2DT_qNF6hftYn4bFri5ox3plXhdcRPaA-fSjg5bC0fcx27UDduPOCjwCq6-yJ34dAwCKZpoHqY5j-rWZAOJxnzA5OPCqe_125g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نشست ایران و عمان در مورد تنگۀ هرمز
🔹
‏معاون بین‌الملل وزارت خارجه: نشست مبسوطی میان هیئت‌های عمانی و ایرانی برای بررسی مجموعه‌ای از اصول حاکم بر عبور شناورها در تنگه هرمز با رعایت امنیت و حاکمیت ملی دولت‌های ساحلی این‌ تنگه و در پرتو قواعد قابل اعمال حقوق بین‌الملل برگزار شد.
@Farsna
- Link</div>
<div class="tg-footer">👁️ 6.82K · <a href="https://t.me/farsna/437716" target="_blank">📅 18:50 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437715">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cXbZpRRXX9zII7SsnDaRMmpGYtK6kUm66qfmpmQMd6iTRXEGJCuSD80WNVRXgqg--4Deaxw3ygvTJriRZKdjNUkbFeR_T2b1i6gjnGnN9TyUDBEUDwqmNqzTC9MenPPnoHZwFVI9pvwgdViwvMaD-JhJCxmbGTmZ9YhqNeU8qo37MxL7TUkS8rBOEBZAXg7V6cjR9wam5s5ryw4k1SgopxKvsuC8hKhYKlmE7KTCWNv3MYMWIcP3b4tFk8-gYAnpgVqvcSged2PyViLxmVlbJgTsxkFTKN_Qn-giRHVjno1ofcE45xWkyCdnSnYRflxwCy7koZBs_MdLoG6M2egR_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نتانیاهو: با ترامپ به توافق رسیدیم که تهدید هسته‌ای ایران باید از بین برود
🔹
از بین‌بردن تهدید هسته‌ای ایران یعنی از بین‌بردن سایت‌های غنی‌سازی اورانیوم و خارج‌کردن اورانیوم غنی‌شده از ایران.
@Farsna</div>
<div class="tg-footer">👁️ 7.48K · <a href="https://t.me/farsna/437715" target="_blank">📅 18:37 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437714">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i9Wr0LD1kYMGsnhljsYfhED5-yDn7fP_62iyJpjAMhNIRJNkuabnVewaa2KwlN_CTcYiDCIlKeGxRr_CtT3hyuIFXLN4c7wC_KeGbaYCrePAqrsXu5PTGYxZBKqyv1Tnx5ctZElI9W75-R9GHlXw0lzSZATTea2ST6b3wf4RkYn4nH-J69WRaf2raETAp63xAypwqEp5KgI6zIByJuCpi3Rxl6aCZSBd8CYzlZxe40M_dz8twuGttr8hlnXPTkJ0UA84i6VZJviAB2jQ-c19aq_-SdUq5YSsTzcvNo4IEyPi34kez8funEGp9NzxRdXXCmLt9_eqUBrF-DJW57i_Pg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رئیس قوه‌قضائیه: خرمشهر‌های پیش‌رو را فتح خواهیم کرد
🔹
وحدت ملی در همۀ ساحات و عرصه‌ها، یک اصل اساسی و ضرورت گریزناپذیر است.
🔹
رمز پیروزی ما در عملیات بیت‌‎المقدس در خردادماه سال ۱۳۶۱، «استقامت» و «حضور مردم در صحنه» بود؛ امروز هم با همین ۲ شاخصه و مؤلفه، خرمشهر‌های پیش‌رو را فتح خواهیم کرد.
@Farsna</div>
<div class="tg-footer">👁️ 6.47K · <a href="https://t.me/farsna/437714" target="_blank">📅 18:35 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437713">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس اقتصادی</strong></div>
<div class="tg-text">مدیریت تنگه هرمز با یا بدون عمان؟
🔹
محمد امینی‌رعیا، مدیر اندیشکده اقتصاد مقاومتی: وزارت امور خارجه به دنبال مذاکره با عمان برای رسیدن به یک طرح تفکیک دریایی است اما این رویکرد با چالش‌هایی همراه است از جمله اینکه عمان ممکن است با ایران همراهی نکند و منافع ایران محقق نشود.
@Farseconomy</div>
<div class="tg-footer">👁️ 5.88K · <a href="https://t.me/farsna/437713" target="_blank">📅 18:30 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437706">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LTuV5dnpSeb6-tYzB46p18yumE4LiycM0OJ_XXc7jEDclwG8QyVrWIqb7OG9ERKIrSF2phu_8pDVORohJgPOnDMlgzxaAibhBTkLimRGGvuzVVkOi0f96cGchrSKRTliv8UE4aXVTZgXntab5b8CK_kwdz7egjovBTlwN74VZyuOPDmVUpoQdOS1BTx-SpTnpuM4PWGQeB1-PyJG_J3xaM4LaxLs6Jl74vnIpZNItew5G5KV95_GyrdZ_RvHJU9N4TOdg2B4PlVLJpVSui34Xoic_dn-GRxnCGVe-_vNZ7kNaYSqucoovTEsPqhXIRb9FeROmxvMtCaJLsM9bYbHWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hyqwFJmGYcQGQ0YzOapy3IJXuFIEc93ECCnXdhXZEn2F4FZhMM3480ZA23EseWVj4-O2JYO4YOlDmtPn11-6wrfbYX3c4ZMJAr4N9EsLY77kzMf42rGpbu5VDZs5h9CYsQFdFQZc7mg4u8Xq25WI6bxm97FVUw1Sr_5Gwzfl1M7NCm4dvT9Mb0dLUaIvPVXgd45clLuezGoyPJQ57EvytO-pkQCNPQC-K5n8is7sChvm9aGukxLSTfMLWtfiQqPuYmnBkTqx1Q9aZvtt-g1dzhcRdU60EKL4yW52XzirU2kAorrgywh4-Ly_RXZkdJXvcUNqY8qyhLwou_gOi2sc4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NnS59H02sKD1WWONcILZ3xdrTKiNJjMMWj2yHsXH2NPO0wxSKKVvO8hJ183_LsIafb7CYy78xnclSGkzgW6v4uHyqq__tL3TQMB_uzPq8RqjBzui4wYc-PCEb0iaraMJP1kh7WGs4n7iesglm5_unLJxeCYVgeRKSvLOwo_eL4ATiFyZgQIiRWSDqXz2HwH-ji8iGYUjCGHC8kWSUvWhfVA3uLxjGZWzg7MjRxpgLWcwTIUZUevLlqjiCnGvF0JolG3TWV4L0mXig_8f6XH8b2_KoU1gGAt9PXX7s3GwkQPHCESOH6kcNqqtRAblHrLXp6G6qH8No7TanRNzB6eScQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/h1K1k1cUnCLKM1I5zcA9fQOr2I_8I8vstg_bteQx7KV6zM_NiRhQ9ntSIDU3B6eAKYcZZQlXObTV3ORFBZ5rKNmD9pkeY7US1bMq9PswAHbjdOPBSTt0sPpklsL9d91SccrmEJHlq99m5BG99_t_KkFhjtmjvVcbJo7_qQ6KBruZJYGKy0JkUT1QkeFvoC7XD5hi10t1nRWwtsEmNGYVO6MhO5EwzbruHh9AgX-L8LWiR19z559Ocst18rYutGyfsQk7PwTvRhJPF3EJhZsqym01GgJ6hweRZgQCwao-IHXa2Qye_PLB7p3SAkUVqx5YjI5LLk2gYFA8X3q2rbqEJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lRb-N14RmiSXQ2CPnF-8fuk9iufaLwlv2qj9ioPHzsU7WsbYNe98fCunn55UZxvPOUj4Xv8oCA0f5w7eTFkgN4jEhdZszyT9X_V7v1maFRGL4SQllHUtouNt_jD-m9q0fSKVZSJjJj5Yg0XgaQ0t-OAkTaEQPBe0O0zJwwsjmd6q3strCIRjW_ZVXmx9k_yrbav4OFEvCR6XY2yn1gmRk6U2ptqsQavC77YKfJS8vveSM_F1ZjHiqKO65baYm0MwKYYioBKPuyISuZy5FHdvcJ9zhI8ZLPpYQDXR1UXaj4PPiYWE4rsLs4MJI39GMpfw60YAEyxSkAt4vneQLEad4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/slp3aNiT_KONzZyJypx358SEzEJofC6wRNaJJR5iWTVhorTdtNAw9HNr2vXOO77gc8AxlTElxplqnDmj4Tr-cL005awGxw-wRFH0mfak-vheO33_GSUZJ-na1Jcp56T4aS8U-Nz6sx4v1iHzZcZAgDzeZmrK8IrnGAarRe3dbYmEGJ6IH9QpJQSxKOKA3vI2-8FomqvqSk-XiXaNPU4DXa__msy5-EmtT0_SwaDVeOMR-nVPwFeantq3Wk3FAkELqXvhx_-SeeWkwjtVTv58h5ZeweG3dy-jP7jjehvFqTH1vsH_A3AzMcpJh_03WboI3FBXG5FmQf-6vvme18EKLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Eaq6RnvkMytamyKb0zL0PDlp25-PV9o88Rfsgx4BwdnodVAvwHV0UwG3NL_gbdcPt9Lacp_pjXXtGqPXxvfAOhgfg2jO4rYlz3yVepAqz02gBrZVuXfJkSqDkhjl2qsIHx_vlmeIAr6RoaDf8PfDFukXxIb80mxIL0-1HWt6GJ6WhcEw5isx9QJhste8KZ-ak9hr4CbSa6OcFk0Z5U6O_Z3czKPthLLDkMrH4C0athvEXUj9HTmtnfeYqerpTR00P1Vh0X-j2f0nlWLdOeEEA101McCe7800qxAqruMnG3W_CD7t99jSkP4iMzQ_f-WWMsJ0HsLJfWvKOvL9l0f2hQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
بزرگداشت شهدای جنگ تحمیلی رمضان و سالگرد شهدای اقتدار ایران
عکس:
هادی هیربدوش
@Farsna</div>
<div class="tg-footer">👁️ 6.19K · <a href="https://t.me/farsna/437706" target="_blank">📅 18:11 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437705">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PF1uPUAKl388Jp03WRgbnGDUeZc2SQPyAVyK_hHFcsBkDuEX19xpeu8oqs7qD7t-PlpPOEEzr0SEtvoQlLsZSV7yIc2o_9bhLDA6cQlIjSflObE5OcmlMgJ31An5AZvfuZP3bv-uzXq5cegvWRPlbUT0b-khK49EvSIHyYbvJRQm6wBvIp485mW7mFQ_lfBeCkiI8MgFlV-q36hirWu3VMGl09IIPHlEmFQdFxqMck3NgA0ZuXkAbDeNVhQX_1ulNaPPvtL_PnHla2XJHdwYRi-dHcguKeL2zxEDnA2vHxFRXsjSA6Aiw9p9Vz5y3q6efxOSQXMbQC3upNUtYbWT0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گام بلند بانک رفاه کارگران برای حمایت از شرکت‌های دانش‌بنیان
🔹
با هدف حمایت از شرکت‌های دانش‌بنیان و زیست‌بوم فناوری کشور، بانک رفاه کارگران و بنیاد ایران پیشرفته تفاهم‌نامه همکاری امضاء کردند. این تفاهم‌نامه به امضای دکتر مخبر مشاور و دستیار مقام معظم رهبری و دکتر للـه‌گانی مدیرعامل بانک رفاه رسید.
🔹
دکتر مخبر طی سخنانی در این مراسم با قدردانی از وزیر تعاون، کار و رفاه اجتماعی، سازمان تامین اجتماعی و بانک رفاه کارگران، توجه به احیای شرکت‌های دانش‌بنیان را یک تکلیف ملی دانست و گفت: حمایت از این سرمایه‌های علمی و اقتصادی کشور یک ضرورت انکارناپذیر است و باید با تمام توان از این ظرفیت‌ها صیانت کنیم.
🔹
مشاور و دستیار مقام معظم رهبری  در تشریح اهداف این تفاهم‌نامه گفت: نخستین هدف، تسهیل در تأمین نقدینگی شرکت‌های نوپای دانش‌بنیان برای نمونه‌سازی و دستیابی به محصول نهایی است تا ریسک‌های اولیه کسب‌وکار کاهش یابد و این شرکت‌ها از طریق مشاوره‌های مدیریت مالی و آموزشی به بلوغ اقتصادی برسند.
🔹
مدیرعامل بانک رفاه کارگران نیز طی سخنانی در این مراسم هدف از امضای این تفاهم‌نامه را حمایت از شرکت‌های دانش‌بنیان و زیست‌بوم فناوری کشور اعلام کرد و گفت: بانک رفاه از طریق این تفاهم‌نامه انواع خدمات بانکی و بانکداری الکترونیک به ویژه تامین مالی (ارزی و ریالی) را به این شرکت‌ها ارائه می‌کند. تسریع و تسهیل در ارائه این خدمات ازجمله ضرورت‌های اجرایی تفاهم‌نامه است.
🔹
دکتر للـه‌گانی حمایت از اشتغالزایی به‌ویژه اشتغال فناورمحور را ازجمله رویکردهای اصلی فعالیت‌های بانک رفاه کارگران به عنوان بانک زیرمجموعه وزارت تعاون، کار و رفاه اجتماعی و سازمان تامین اجتماعی عنوان کرد و گفت: تمامی خدمات، محصولات و ابزارهای این بانک با محوریت حمایت از تولید ملی و واحدهای تولیدی طراحی و ارائه می‌شوند و بدون شک شرکت‌های دانش‌بنیان در اولویت حمایت‌های بانک قرار دارند. محصولات این شرکت‌ها نقش تعیین‌کننده‌ای در افزایش تاب‌آوری اجتماعی دارند و بانک به سهم خود از توسعه فعالیت‌های آنان پشتیبانی می‌کند.
@bankrefahkargaran
| بانک رفاه کارگران</div>
<div class="tg-footer">👁️ 5.49K · <a href="https://t.me/farsna/437705" target="_blank">📅 18:10 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437704">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rjEZ5XevWnN3FII2q14ccXKLLP3nCIj-5xtBh9dkl7JrBdQoI4dHK-5v3B-KLNkFXVEuZ66R8S6AarJ4IQJyDgEA1nnLd0SrcOvY5zofP6cbWqOO4kP15PWppA74_UP-8quxqjCsJ7QRhszQdT0Hphan0xOVYAw7kjCkX5T2uBKV1WqXf5fLGTdQuhy2ra8NATZpdbh1wFWYBJXKQywFTPZpivzz57WZwvxqq4g1bSXC3xyANMK2R6mx75y3ntxCjNGmuO4Ab4GwYRweZdTSn76mk5vDFzwpMs_6dvKpYuMz5sMOreDf4kmjV2wn7t0q_yUhLIE8oz1uCn3BwvJVOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔸
وزیر راه و شهرسازی: کاهش ۸۰ همت ناترازی بانک مسکن دستمریزاد دارد/ قدردانی ویژه از اقدام جهادی بانک مسکن در حمایت از آسیب‌دیدگان جنگ رمضان/ تأکید بر تسریع در افزایش سرمایه و اجرای طرح مسکن استیجاری
◀️
«دکتر فرزانه صادق» وزیر راه و شهرسازی در همایش مدیران ارشد بانک مسکن از اقدامات جهادی مدیران و کارکنان این بانک در حمایت به موقع و سریع از آسیب‌دیدگان جنگ تحمیلی سوم و پرداخت سه روزه وام ودیعه مسکن قدردانی کرد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.25K · <a href="https://t.me/farsna/437704" target="_blank">📅 18:09 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437703">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-footer">👁️ 5.02K · <a href="https://t.me/farsna/437703" target="_blank">📅 18:09 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437702">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">خط-45.pdf</div>
  <div class="tg-doc-extra">3.1 MB</div>
</div>
<a href="https://t.me/farsna/437702" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">خط-44.pdf</div>
<div class="tg-footer">👁️ 5.45K · <a href="https://t.me/farsna/437702" target="_blank">📅 18:01 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437701">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pxRBHV7ARMb3OVVknogE33lhSptOJO8qB4M4wLiOSP6zzTOMdTsvNyTTiL_9iFXMBBzRmiljkL-BTdq0HT3cRGr3rTdihvkcL8lNFbsaYG1YH51c4krt2cWmZ9apI-49zxU4WvftopQlLsYwTWVU8El4TI6xg_AyGnimeHeFel18ELFIe5GflBnSoVXJTwkLWdFW9nDw-Rvhy-j1cDoohV0Wo2pTwD8KSyw5xUWD1bVPlxPqn_3wRfHmb37kcaLCDUPhLohcILn21tQkmZ_7apkTNBC1NPRosqNWhiss3m43Cy4ei-4FKzM6YsU9EgPpgGa_61mHuqmhGJqeVUqhMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حرکت مردمی جان‌فدا وارد فاز تازه‌ای می‌شود
🔹
جان‌فدا کاروانی‌ست که در تاریخ حرکت کرده و هر نام جدید که به آن می‌پیوندد، قطره‌ای است که به  رود خروشان اراده ملت مسلمان ایران می‌پیوندد تا سد تحقیرها و تهدیدهای تاریخی این خاک را بشکافد و دشمن را در سیل ایمان و توکل خویش، غرق کند.
🔹
برای شرکت در بخش‌های تخصصی جانفدا و فراگیری آموزش‌های جدید همین الان به سایت زیر مراجعه کنید.
form.janfadaa.ir/login
@Farsna</div>
<div class="tg-footer">👁️ 6.44K · <a href="https://t.me/farsna/437701" target="_blank">📅 17:55 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437700">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a14b750f68.mp4?token=joZg-Q7Gx6hKHRN6CBOIFnbrZM-_39Flq54rdo5HOz2Eyiason-UFUcAGksq02oWKLAXdcokwBVsDpPto4QkO4AYXK29fyFKkeb7onYGQZp-PtRS56_-HmmS3pGuPJFSn-oKp6sq7k0ZTLAAKBbmTYFDgVGhG90XeW8XBD-fO2O5Z_kvI2GSG6yZOd8ixPY6ZrwoqglyH31gSYgIByNwFBacH3UBdPxJqB-BBLjzi2mnDmSc9-_VJw4h-yvVsnV7yUcUFv1Ya3pKV4kgLodZBAgwZHMLB9DXX-TDemArWCH5MxVI3i5L9QzNO1mhbZn6rQDi5vHJKPe3ieg7eeQVxA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a14b750f68.mp4?token=joZg-Q7Gx6hKHRN6CBOIFnbrZM-_39Flq54rdo5HOz2Eyiason-UFUcAGksq02oWKLAXdcokwBVsDpPto4QkO4AYXK29fyFKkeb7onYGQZp-PtRS56_-HmmS3pGuPJFSn-oKp6sq7k0ZTLAAKBbmTYFDgVGhG90XeW8XBD-fO2O5Z_kvI2GSG6yZOd8ixPY6ZrwoqglyH31gSYgIByNwFBacH3UBdPxJqB-BBLjzi2mnDmSc9-_VJw4h-yvVsnV7yUcUFv1Ya3pKV4kgLodZBAgwZHMLB9DXX-TDemArWCH5MxVI3i5L9QzNO1mhbZn6rQDi5vHJKPe3ieg7eeQVxA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
شکار یک نظامی صهیونیست توسط پهپاد حزب‌الله
@Farsna</div>
<div class="tg-footer">👁️ 5.57K · <a href="https://t.me/farsna/437700" target="_blank">📅 17:54 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437699">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">سرلشکر رضایی: پشت صبر راهبردی ایران خشم انقلابی ملت است
🔹
امروز ترامپ و ارتش آمریکا در یک بن‌بست کامل قرار دارند و اگر وارد جنگ شوند، در برابر آنها دالانی تاریک و بی‌انتها قرار خواهد گرفت؛ دالانی که از تنگۀ هرمز آغاز می‌شود، به خلیج فارس، دریای عمان، تنگه…</div>
<div class="tg-footer">👁️ 6.86K · <a href="https://t.me/farsna/437699" target="_blank">📅 17:32 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437698">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VB98bEDiZ_vtQ_o3OGhzJPCjZ3hFlTEv71QV-moL5_PceDfRXO0P680ZEwM9f62bOQjgAcwvQXzSR7bSO702yfwUC2Xc6l1-BJLFyoJ4qCmCIR0Q53NC-hdbbahEEnORTIoZvq9BOmJE2e40deza1OugIfostdVGfPLV2XcWFlpl4wAwtlj5th3Ejiq2IpDZNQ4Us5NMjsBcVmDEEHuS8WnQCKSJyutNsCwBgFe0Kjdk4UBq_NbEX33ahExBH1I2Gp8OrKUtfspCfcx_8oRD97VgCphrcu15_-GoulkaIqXpE3AnWNQH06hqKlVv3N1xynQHc3hN2kX7zQ3iejYqJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سرلشکر رضایی: پشت صبر راهبردی ایران خشم انقلابی ملت است
🔹
امروز ترامپ و ارتش آمریکا در یک بن‌بست کامل قرار دارند و اگر وارد جنگ شوند، در برابر آنها دالانی تاریک و بی‌انتها قرار خواهد گرفت؛ دالانی که از تنگۀ هرمز آغاز می‌شود، به خلیج فارس، دریای عمان، تنگه باب‌المندب و اقیانوس هند امتداد می‌یابد و جنگی بسیار گسترده را رقم خواهد زد.
🔹
تنگۀ هرمز برای تجارت آزاد بسته نیست، بلکه برای لشکرکشی و ایجاد جنگ در منطقه بسته است و مدیریت فعلی نیروی دریایی سپاه موجب شده کشتی‌های کشورهای مختلف پس از شناسایی و ثبت، با امنیت از این مسیر عبور کنند.
🔹
در صورت هرگونه اقدام نظامی علیه تنگۀ هرمز و تلاش برای ورود به خلیج فارس، جمهوری اسلامی پاسخی سخت، دردناک و بی‌نظیر خواهد داد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.48K · <a href="https://t.me/farsna/437698" target="_blank">📅 17:30 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437692">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromکانال ورزشی فارس</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IYr-Rdn2dqOHV65cVvvxMr1o1_II_T9uPVcuqJdrz5xLMywY7NGNd9EuSA-WNwrRrtwEG3sFPGdCn5PK03VX9jScnWz7TfkZguubBr3rDghiKEi6SzfefWKnBiFRut26WOtXa2gpuyd_4cAt-O-XEaZ8XG7AedKUzv3JsE8Tq2VIaRySb9iKqLLQrw35VFi1uBU5SyalF5POvf5FHxZ_Kq8FG2gZ7DQnsXujzb2qnsIWpHeBZCKg5n6wlJ-9mF7KLXpTM6bxXRsyH930902a-gFLfpkst7-zAByBbLcNED2O6sKFSVC1fK8WQ-9EdaFu44ABTff05ObW0R2cDC0SIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iYf0rTzK59hh70C0fhMvo0uXz4fpNtD2GDvgId2j7tfUUF4aa3og6EA0urKkRdMPXimfdj17Th61p67gq_UT9aYbpz5k4bwABviL1bXxrxROIrfEVk5Htzymzi8l8mbPta2cgUtqHbP4R5pxQIopwEk0TOm-WmJsPvKfKdvWFG5LCrVmtXhKyrQevzz3aUTcX-ILiiov41BelWUGD8sV6sQWelpWtttDv4klLt6k4VdoejUv3IhgmVWnAot9v5EqkrH17BecB3g4tYxx4CE19zn8Q_KgoHlE3WB09uBGs-lArBR9CxTnZrW8KuN4JL-Nf66VUQJ0IrJhoT1T2HsZNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vUGjNhLd9-aZyQyHgL-0UFnb-9fZsKh6HmDOXkYQLoclKQArbPaoxsDxF_EsbpkWekfe_QZzWB2SPnEvtllvDgSFScZ-78GjoEoga3Nhw-iDVEPrqBrvZEjUJdv8RV0NTRUjXrDdBA_UboqWPDG8oRAKYIzT9ITkkDQcWrJugMGy5LVlC1oV11dva4jtzBSsswUHzlr1LtPHFNZ2fIoc4WmR9swwgi9Q5jqNqS9lBOhN2HSBlrUlGZTaFsXCZBe4fH4itTwGw0AXgCImvA4cWuoo6U8UQluDXuCwgkIycNRdiKOcnMqv99GS3Eh2MeqiCiVKvMTrNFxRIe1qjIvQ7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SFX3bLkZS6lfAK4iHw2Uh4dgEMsysnxm-q63TaHckY89a-93Nf2dsemxXzWPy7JFNThTNu4vd6dzobv-VnI-NdkT9H32i-yZd5zxaRgMkrrf3ozw82LTiyWE21-EJlVxnk4USpv57pg3wpz05gxVjgzcUKJzg7ysZ6hl1VV3U7dB3esWOvLjzXPPvWfj1QEWcqZKi-7ALcI16v0BiUa1_5qTDXqR7X_Nwnrj1glAKa9JQ4o0iTz-blwKllLvpahHMMQ4ezBRawqRrVcND1EoBl24zW0pumoEKiHz1MHX8TZz7YiOS9ze2GLRZ5Z5Vwc6IBkzJ75z-nm55VknZB6xuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nIPUjdSMVnlvpxFIqT2OQAwk6lmc3MtLIVK6ejkr1qE4dtu_xJY3-5qIa4dwiUCu8e6BWVKklJiSxtxLDSlW69UZEq3oheEr9W5dDxM5zrM8k3KRdg0D1px5YkLwrSWhJbRXU3yh5hrOf1b1nkpRYX4u_RSg2v7-wvw81ylhK9XmvwFXUNXqGZJgplKJnlhbNPiKNxCZ1GZ-n8gjRmcZ9UViG3mc9HpBGe1eJxQifvitJLCo0PpxW17dIrG-1vK-7EXP4S7TzDCkujOi0sOMgIwIwaUyCAznsVCrZH2tN-jBunR1XIEusZyjN-j4pS12-icYjon1r3qf4-aTUK-FqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hG159aJowdyLRBm74RbagRiUxHbiuwnJW2eJ1frmRgXUE8Rx1JiN6NxJEHDNhFW4u5GDGnihnmFwFcu6Wljqsncf_V8x3RlFOuOhHLnIfN4vcGd8oPztMW2CT6fmoRBS4XXUGsVXohhpKkUuB5JrmQlcTCXZK-Dkba4qMc3ElAPzyKkOUTyCh0rr0D0ME0LLeD1-AF1Orhb5C9LA9O4-GAFeGoMWlLh6c3_jKMNCeWAHMQdJUbxTWqVfskkcbcGbA7XzkckQLSWb3gAZajbOQbWyr9_9UDwgxks_uJa4mVm0q-xuCAlrtH1mZncFivEup0DKVAD3zPApZKPPJg6MNw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
تصاویری از تمرینات امروز ملی‌پوشان فوتبال ایران
@Sportfars</div>
<div class="tg-footer">👁️ 6.51K · <a href="https://t.me/farsna/437692" target="_blank">📅 17:13 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437690">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">دادستان تهران: ۱۳ نفر در پرونده‌های مربوط به تراستی‌ها و رفع تعهدات ارزی بازداشت شدند.‌
@Farsna</div>
<div class="tg-footer">👁️ 7K · <a href="https://t.me/farsna/437690" target="_blank">📅 17:00 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437689">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/441854eb14.mp4?token=Nxj_5A6ZIKactjbGMtE7qCGzaXh20_gKuPT7LQttQ17an3kMHX19Njr2t_Ct61XAf8sfIUbICt4PdAr-3WGcHXEuNNNQ1XNhNo_oWfoaL0hadN2O5G-N-9vXxpSU06w8kibQLo_9pjJzuKQOB9rKBAtjHHRRXuNiX6--WzOA4xYFzrip-BCfaUknZVQ7xRtoLhFHrCVct6D--f3TTcHJjOrb4ag8p-IZKb11Al35GWDpa9EwkxmVERe565vnl2y1Rb9Bus2Ts7i_1hNUS6M8NhsHYystBHa0jkFPSWQ7OZbS65RepXqiTlsHZM4pcWmNxNhOfJ3xltqEJ6a35N6q_w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/441854eb14.mp4?token=Nxj_5A6ZIKactjbGMtE7qCGzaXh20_gKuPT7LQttQ17an3kMHX19Njr2t_Ct61XAf8sfIUbICt4PdAr-3WGcHXEuNNNQ1XNhNo_oWfoaL0hadN2O5G-N-9vXxpSU06w8kibQLo_9pjJzuKQOB9rKBAtjHHRRXuNiX6--WzOA4xYFzrip-BCfaUknZVQ7xRtoLhFHrCVct6D--f3TTcHJjOrb4ag8p-IZKb11Al35GWDpa9EwkxmVERe565vnl2y1Rb9Bus2Ts7i_1hNUS6M8NhsHYystBHa0jkFPSWQ7OZbS65RepXqiTlsHZM4pcWmNxNhOfJ3xltqEJ6a35N6q_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حضور سرلشکر عبداللهی، فرمانده قرارگاه خاتم‌الانبیاء، در مراسم شهدای جنگ رمضان  @Farsna - Link</div>
<div class="tg-footer">👁️ 7.93K · <a href="https://t.me/farsna/437689" target="_blank">📅 16:44 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437687">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/662d4ee6ff.mp4?token=DGIpfrMvPnIzCQOr6A6DscLqV8Xx6XLDhu2Qxz642RyKu-sCDGRuOK9Y4e0Z3iSblyHygzCRtaK5-TX3ZIJKs1Cz3NYWX_9C35xtbhjbIkifbzJOd9ORkqG9-suO-l1l1K-ZrS9zJPbWiSfUWnc9Sxbejg3aG9u54RMjG66qTd_YxMnOJ8BT6NE4ierbvFt7f7ryu52LkpOUjZrbZDhEVhc0XOXLi0f_NtPBP69MBokRmfuL4wSg53fzGaQCtPyzaMr0DpErU_Mi4Q2p96Sa3mboKotfYw9BLxPPvqzSMIpcBgXSHfrw4_18j0w0xiNag7uHZWQVGyqIffYJPCq3ag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/662d4ee6ff.mp4?token=DGIpfrMvPnIzCQOr6A6DscLqV8Xx6XLDhu2Qxz642RyKu-sCDGRuOK9Y4e0Z3iSblyHygzCRtaK5-TX3ZIJKs1Cz3NYWX_9C35xtbhjbIkifbzJOd9ORkqG9-suO-l1l1K-ZrS9zJPbWiSfUWnc9Sxbejg3aG9u54RMjG66qTd_YxMnOJ8BT6NE4ierbvFt7f7ryu52LkpOUjZrbZDhEVhc0XOXLi0f_NtPBP69MBokRmfuL4wSg53fzGaQCtPyzaMr0DpErU_Mi4Q2p96Sa3mboKotfYw9BLxPPvqzSMIpcBgXSHfrw4_18j0w0xiNag7uHZWQVGyqIffYJPCq3ag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
فعال اصلاح‌طلب: مردم پاسخ غایبان روزهای سخت را خواهند داد
🔹
باقری، دبیرکل حزب اصلاح‌طلب عهد ایران: در این بزنگاه که کشور در معرض خطر و آسیب قرار دارد، پیوستن به دریای زلال ملی شاید کم پیش بیاید.
🔹
فرزندان این کشور نیز نیاز به این معرکه داشتند که دین خود…</div>
<div class="tg-footer">👁️ 7.76K · <a href="https://t.me/farsna/437687" target="_blank">📅 16:28 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437686">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/651ceb7ed5.mp4?token=A7gyhs2eSgXl08cDk4limCdzTVM1-V-xBo1Xd4Ua-ool023EOfbPj2BGFlhK5iIz_MP2PJ8W7vDD3kRIIOMhSdxxqodQeibViP159qHXcC99PMQaJCaUpf_oLmpqlPz6n_O_-f_l9hBMI8IHBl7y6Id2t5ii4TouYFaP1RKBLenFCszmIhCoCz5KOsZpKoNpPOYDnS6iqW1G2LJVUMm4HTWy9A3bX88LcoWYv4YEvK8TZCpLjB08v0eymLMb2qeawPnwu8dexseP8XN1cJy0Y9IEqe54LmrI0Bog1EwOd-K1SfoBSxj7aMulSBRTJNThuzU3e7PD4Fq0Aue7G99uZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/651ceb7ed5.mp4?token=A7gyhs2eSgXl08cDk4limCdzTVM1-V-xBo1Xd4Ua-ool023EOfbPj2BGFlhK5iIz_MP2PJ8W7vDD3kRIIOMhSdxxqodQeibViP159qHXcC99PMQaJCaUpf_oLmpqlPz6n_O_-f_l9hBMI8IHBl7y6Id2t5ii4TouYFaP1RKBLenFCszmIhCoCz5KOsZpKoNpPOYDnS6iqW1G2LJVUMm4HTWy9A3bX88LcoWYv4YEvK8TZCpLjB08v0eymLMb2qeawPnwu8dexseP8XN1cJy0Y9IEqe54LmrI0Bog1EwOd-K1SfoBSxj7aMulSBRTJNThuzU3e7PD4Fq0Aue7G99uZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پیداشدن لاشۀ پهپاد ساقط‌شده در هرمزگان
@Farsna</div>
<div class="tg-footer">👁️ 7.87K · <a href="https://t.me/farsna/437686" target="_blank">📅 16:23 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437685">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/21abf1a966.mp4?token=E1svFiEzwc6wi_iv0xyqm97JgGNE6jZbN2nBbsJ57IFnN86pdObg3L_HEHGXJWw0mPbRuXbC6Ds6H_JKcVjePEJL57JTyrnD2xeP23mrtvbHQeXE08EC9Wo2b7VuO7VIDkeEgXHT_z0jovEXKmNXiP2AmIlJwMPtb0YnstC-KcuzXFRqPDaLywYF1mF9Wf8PwsGKILx83fgLf-vAWLXc_Mhq6Q9TlIQzXuIHdh0_2p1qrm654_S996II8eB4RhPl3SxvM2J693QfeqidofpZcFigsy5OZ5wF3Rth1wBjCI68NAXarZV9jhwKbpCxtcOYNS1PFn4x8A4nACb327qsqQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/21abf1a966.mp4?token=E1svFiEzwc6wi_iv0xyqm97JgGNE6jZbN2nBbsJ57IFnN86pdObg3L_HEHGXJWw0mPbRuXbC6Ds6H_JKcVjePEJL57JTyrnD2xeP23mrtvbHQeXE08EC9Wo2b7VuO7VIDkeEgXHT_z0jovEXKmNXiP2AmIlJwMPtb0YnstC-KcuzXFRqPDaLywYF1mF9Wf8PwsGKILx83fgLf-vAWLXc_Mhq6Q9TlIQzXuIHdh0_2p1qrm654_S996II8eB4RhPl3SxvM2J693QfeqidofpZcFigsy5OZ5wF3Rth1wBjCI68NAXarZV9jhwKbpCxtcOYNS1PFn4x8A4nACb327qsqQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حضور سرلشکر عبداللهی، فرمانده قرارگاه خاتم‌الانبیاء، در مراسم شهدای جنگ رمضان
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.32K · <a href="https://t.me/farsna/437685" target="_blank">📅 16:13 · 03 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
