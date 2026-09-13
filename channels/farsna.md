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
<img src="https://cdn4.telesco.pe/file/tYkMKLnoeTD2sPHGSgQ6IzpU7WrzTjRsZouFsViv-qLAO_q4Yd3MWP3mX4WBY2S-u1PYwIBHtuIs57s4vpttsRQ_p55LLkcXXJEh2LXuQFwKJxLgd4D2YFpZSwOyezPAz7ZLvIC-Ug7_KqlowaGCYQ0cXLCbwaM8Jo_4yMBYGNY-htPE0raHtx4U3U6MjpryskmfFcfDnBZVjehMoGYJtZ7S2jvocnj-oU9PqT2iVYq9OpKR8ncVee9kcqa7J1WUWO0hKPKiODRdL_XP7rb4xiXEexytWUzMlBnzDMn-CNhmreCyJbsx5yzD5yMN158ChXBIE7_0t6OK7MerRGsznQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرگزاری فارس</h1>
<p>@farsna • 👥 1.84M عضو</p>
<a href="https://t.me/farsna" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 حقیقت روشن می‌شود‌‌تبلیغات@Farsnews_adsارتباط@FarsNewsفارس‌پلاس@Fars_Plus‌ورزش@SportFarsجهان@FarsNewsIntعکس@FarsImagesپیام‌رسان‌ها@Farsnaاینستاگرامinstagram.com/farsnews.agencyتوییترtwitter.com/FarsNews_Agency</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-22 20:20:35</div>
<hr>

<div class="tg-post" id="msg-461853">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e0be10a4e8.mp4?token=W2UbXMdFrsaXCeABAmsUYgoL_6eqeqVvr4ThkrmdDPxf2VT5OUW9k3d9dyrO0yiqcKZ9NCadMxjBywD8FcPX1VT_xWsA1Zbcba7W2EhubwttvRBiyzAuNR2YBI2SA0gbu4jpwHhQSCUGeC3XWPO6eUEabJxFvEpzhxbh6ZTziOoT2ru60I5FX-ECldF-S2t_e9hN4Si0YxL6eVBRgn2Lg8VTIz6HtVea2TldNZYNvMpoLUGvu19l-vjz3IeoJ0K0GFLObzoqgD8oZ-k17ikMQAQqIQBG5qL0uzNuaHRNkJE-pTqCH0dz_kP28A7bP6hizBy47qT9IWr-Loe50JxnjA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e0be10a4e8.mp4?token=W2UbXMdFrsaXCeABAmsUYgoL_6eqeqVvr4ThkrmdDPxf2VT5OUW9k3d9dyrO0yiqcKZ9NCadMxjBywD8FcPX1VT_xWsA1Zbcba7W2EhubwttvRBiyzAuNR2YBI2SA0gbu4jpwHhQSCUGeC3XWPO6eUEabJxFvEpzhxbh6ZTziOoT2ru60I5FX-ECldF-S2t_e9hN4Si0YxL6eVBRgn2Lg8VTIz6HtVea2TldNZYNvMpoLUGvu19l-vjz3IeoJ0K0GFLObzoqgD8oZ-k17ikMQAQqIQBG5qL0uzNuaHRNkJE-pTqCH0dz_kP28A7bP6hizBy47qT9IWr-Loe50JxnjA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پاکستان هم فقط حملات یمن به خاک عربستان را محکوم کرد
🔹
درحالیکه حملات نیروهای انصارالله به خاک عربستان پرسشهایی را درباره فعال شدن بند دفاع متقابل پیمان مکه ایجاد کرده، نخست وزیر پاکستان در تماس با ولیعهد سعودی تنها به محکوم کردن این حملات بسنده کرد.
🔹
این…</div>
<div class="tg-footer">👁️ 1.73K · <a href="https://t.me/farsna/461853" target="_blank">📅 20:06 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461852">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jriHspiG7yxJzFH4bSjDqD655PnYomhHuD_7gcBf1w6gGK5XDsBO6J3nUi746jpUui2qwZbApvR82atLrEeV-LPkPopEVuUSuPolK3zAudDjmOXhXQ8nnK_Wsax_fv3vw76HrjyhxXtEXYo8bir2COLMvSjAnhC4jFj3jA_wvFl6pIim38eTfENluQj0N8gtnm5mCG02_O065_yafkq7Kn_ZT3cJsnTk9XbPGZHAG34OL4QE2cfH2ShMHC7L9p93DPrumsY-ZAkNUnyvP1y0gitrHyJ2ovNpEJmWE5jLDb20eXA6bdJb79-colzrk7uNQrAmb_D3QZd7FWBciDAopg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
خاطرۀ سردار علی فضلی از حضور رهبر معظم انقلاب در جبهۀ دفاع مقدس ۸ ساله  @Farsna</div>
<div class="tg-footer">👁️ 2.24K · <a href="https://t.me/farsna/461852" target="_blank">📅 20:03 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461851">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e7d7804b6d.mp4?token=lnQkzObKHv-UBfxrMgyumNQIQOgaeKizt469RAIr7Q3q7EHtI1mfKZA0cCXHyR2Mu-Ui0pN4S2y3F1iTHh_LJBfQmreG5J0Ex3ClM3Wa1dnbTn7hlZdH5PxgDSSRidnSoI-YdE504bZ3zA5Oe4K5v0hiSJXRpAw_0lrDowuAz41ffPXhN-PiE13Gak4BqpTPdRkW4rQxgU-rHHjyIghAtKW4q7P_GiVSzUhbAzhTg3Ep11U3Q-15W1fycO5T4IMouxAgoyO2S5a6Oo5x5epY7NDwJA1TZ_OPlsSrPpz1RnyLm7EotFibRY1gatDj6QLDwxXiwjIYXWvF4T17jDA34Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e7d7804b6d.mp4?token=lnQkzObKHv-UBfxrMgyumNQIQOgaeKizt469RAIr7Q3q7EHtI1mfKZA0cCXHyR2Mu-Ui0pN4S2y3F1iTHh_LJBfQmreG5J0Ex3ClM3Wa1dnbTn7hlZdH5PxgDSSRidnSoI-YdE504bZ3zA5Oe4K5v0hiSJXRpAw_0lrDowuAz41ffPXhN-PiE13Gak4BqpTPdRkW4rQxgU-rHHjyIghAtKW4q7P_GiVSzUhbAzhTg3Ep11U3Q-15W1fycO5T4IMouxAgoyO2S5a6Oo5x5epY7NDwJA1TZ_OPlsSrPpz1RnyLm7EotFibRY1gatDj6QLDwxXiwjIYXWvF4T17jDA34Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
بارش شدید باران در مکه مکرمه
@Farsna</div>
<div class="tg-footer">👁️ 2.44K · <a href="https://t.me/farsna/461851" target="_blank">📅 20:00 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461850">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fa2d1e303a.mp4?token=ov8fHvj9WLDhYhn-dJd20gL5wQ7q_AL97azrpCblzyOQp8-24bCASY8FLsSyPj9pjdb0lj1UM7ietfDjWJPvem1g4-JXV5a7J07LjQmNme560OYr7IFSElP_UaVhmEpDPdI3qK1SGI2WHV-zhpIWV3IUUTyqMgl5-yPXRVxio2eSEbV1cTimqQmj3y73Bowcgyz_wPOfkpGE6h6WpYeLzvmWa0TIRGovKG0QitbBBHlgX5Kn9ZjbWLPnrpoE8CIwLfADIiTEgmUT6jMWs_DSJmrvOxiGM16JAFI4Ze_5bUW6SdF-3KJiJOlNMzWgMW9BoENYSuSrtlOnFVgzMkthag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fa2d1e303a.mp4?token=ov8fHvj9WLDhYhn-dJd20gL5wQ7q_AL97azrpCblzyOQp8-24bCASY8FLsSyPj9pjdb0lj1UM7ietfDjWJPvem1g4-JXV5a7J07LjQmNme560OYr7IFSElP_UaVhmEpDPdI3qK1SGI2WHV-zhpIWV3IUUTyqMgl5-yPXRVxio2eSEbV1cTimqQmj3y73Bowcgyz_wPOfkpGE6h6WpYeLzvmWa0TIRGovKG0QitbBBHlgX5Kn9ZjbWLPnrpoE8CIwLfADIiTEgmUT6jMWs_DSJmrvOxiGM16JAFI4Ze_5bUW6SdF-3KJiJOlNMzWgMW9BoENYSuSrtlOnFVgzMkthag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
آمریکا در روزهای اول تفاهم‌نامه چندبار آن را نقض کرد؟
@Farsna</div>
<div class="tg-footer">👁️ 2.99K · <a href="https://t.me/farsna/461850" target="_blank">📅 19:56 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461849">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a_HiEkHjm7G7K8Qcw7wKU3AwFGW0uGHBMVWTt-byaX6lrmQC5M_nbc-9zTlhnGNzBCt4sf3l7K2Al7jMyQcyxzFNKt3EdVFVsm-Gh-2CkgSWAV0xQYbz-tFWNukoIH0nBCRnoE1e1bcxD78Njjgw-N4upAe0AtCW2z5Iu_Ckv4YLnMv9IiMEvlpa3a2DMW4Zt9ZL5XkVMSFArfLaVaHbqz7xyOS4kXHeVpUYsp4fxy6vLhh-H2zqU_N5qy1S5kaIiF8R4j3iLNuOycgqX7Vfog8QZHxjBE2tQORhKVrIaJfg3_G8nn_A90r-NIDn_nwvGF-nslTz2eNHAExgvJa_aA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تلهٔ طلایی پکن برای دلار
🔹
چین درحالی ریاست دورهٔ آیندهٔ گروه بریکس را برعهده می‌گیرد که هم‌زمان روند افزایش ذخایر طلای این کشور ادامه دارد.
🔹
اقدامی که در کنار تلاش پکن برای گسترش استفاده بین‌المللی از یوان و توسعهٔ سازوکارهای پرداخت مستقل از نظام مالی غرب، بار دیگر بحث کاهش وابستگی اقتصادهای نوظهور به دلار را مطرح کرده است.
🔹
اهمیت این روند زمانی بیشتر می‌شود که چین در کنار انباشت طلا، سیاست بین‌المللی‌سازی یوآن و استفاده بیشتر از ارزهای ملی در تجارت خارجی را دنبال می‌کند.
🔹
آنچه در حال شکل‌گیری است بیشتر شبیه ایجاد یک شبکهٔ موازی مالی است؛ شبکه‌ای که در آن اعضای بریکس تلاش می‌کنند وابستگی خود به زیرساخت‌های مالی تحت سلطه آمریکا را کاهش دهند و سهم ارزهای ملی را در تجارت و سرمایه‌گذاری افزایش دهند.
🔹
اگرچه نمی‌توان با قطعیت گفت چین به‌دنبال راه‌اندازی «یوان با پشتوانه طلا» یا حذف دلار از مبادلات جهانی است، اما اقدامات پکن نشان می‌دهد چین می‌خواهد نقش طلا، یوان و سیستم‌های پرداخت مستقل را در اقتصاد جهانی بیشتر کند.
🔹
این مسیر در صورت تداوم می‌تواند به کاهش تدریجی انحصار دلار در تجارت جهانی منجر شود و یکی از ابزارهای هژمونی آمریکا را از دستش دربیاورد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 3.6K · <a href="https://t.me/farsna/461849" target="_blank">📅 19:51 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461848">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CJYtguJVR7y2Boj0baCTMc4cj5Y6VtaCnh3rHLLlJvd5OOR7zbwJDTZkWUskSBDhxmSVr11MNdi3T_5YuGPYxdWABrIUdR90Z7zUAf61sa26eviNDgP6hi54b28ux8xzsm2X9u_58-ANVkHObPBG6XuLLRXTA3KhzoF2Ta8_VgT-Pa_sSnm4WkN0QPL8f9ubw5ZpI9zjRve9R2gLFqdN6gK4Q0A9wpgQ6wtpUv854HeBmGsjr9cSoVzrS3uoyXjychppIAnMOzdM5DluL1IkB2-PNhjjOqgttKWVzBnrHh0X1WH0kD_-vQgUkqYKbVc5PNtbHkuKtQPQ3CuOm2gnkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روایت سرباز صهیونیست از قتل خبرنگاران در بیمارستان غزه
🔹
رژیم صهیونیستی سال ۲۰۲۵ در یک حملهٔ دو مرحله‌ای به بیمارستان ناصر در غزه ۵ روزنامه‌نگار از جمله حسام المصری، فیلمبردار رویترز را به قتل رساند.
🔹
مقام‌های اسرائیلی پس از حمله اعلام کردند هدف، یک دوربین…</div>
<div class="tg-footer">👁️ 3.2K · <a href="https://t.me/farsna/461848" target="_blank">📅 19:44 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461847">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">بسته خط ۱۳۳.pdf</div>
  <div class="tg-doc-extra">3 MB</div>
</div>
<a href="https://t.me/farsna/461847" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">بسته خط ۱۳۲.pdf</div>
<div class="tg-footer">👁️ 3.51K · <a href="https://t.me/farsna/461847" target="_blank">📅 19:39 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461846">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r2PrJT_WLea068eRw7Lbygy1rC4FuMEKJlx0CjwoQSBkFREw5_4Mve3ht0OLrzBi7m6vR77ZoWGaeNzcUctasS5qG8a-PRIgsi6IkWFe_w3Zvh8_yLhPcYgcAL9nQ4BBiVzNovWkc71Tea3lctlSkz56VdrmeVfWSJVrNUQ5acNiZkqyiy1-wCgmJRlE0yzPdBI6YNQ5MSCpXzxkiCV1I5A9bfWBKPGLEGJL8g_VEIfrUzIpIgnB3HlHAAUdf-sCXNjXixe6A_nRR4Acq679peUrHAnKdwjSNWQgWYuyUZr9ijh0_ALZst32wHDfbiQXR5ZCNpsWhxlDNZsIRK7VLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
سردار رادان: بیرانوند از اول مهر سرباز است و شامل سرباز قهرمان نمی‌شود، باید بین ۲ تیم ملوان یا فجرسپاسی انتخاب کند.  @Farsna</div>
<div class="tg-footer">👁️ 4.44K · <a href="https://t.me/farsna/461846" target="_blank">📅 19:29 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461845">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qTKsren-PZSpNBXCoOSkYtP83yL3kXafg2w3Hq0SjrnFPLlKCHkpgQRNaWvIpID1jfZGQ6oyNN1iRaL5e3-xdYkBi1D8oQEHmUwBYC8Fla6kC5TT_egh93T0AwLH5oMcg7iHG8qcxnmjsjGK9Cd8PAnu9TvVlvQaYGpaeuR0bXHYDskTjNuNxf7aViH5zYY3dsPmAnPty0PimhWdA8HoIsjdJ5egyHU-E8El_VpaVfbOjLQ9XIdcuc8PtAhap2tUylGtn67cALLbxDkiOiMsct8h5mCLLxYewy6M6TYEX5SDwPwvmg7haJwoHRfKv_3oc69AclxaP_ovUkJauDxfaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تخلیۀ قطار نخست‌وزیر اسبق انگلیس پس‌ از حمله پهپادی در اوکراین
🔹
مجله اشپیگل گزارش می‌دهد که چند سیاستمدار اروپایی از جمله «یکی از نزدیک‌ترین مشاوران» صدراعظم آلمان گونتر زاوتر حین بازگشت از اوکراین، یک حمله پهپادی را تجربه کردند.
🔹
علاوه بر زاوتر، مشاوران امنیتی از کشورهای مختلف اروپایی، اعضای بوندستاگ آلمان، دیپلمات‌ها و همچنین نخست‌وزیر اسبق انگلیس بوریس جانسون نیز در قطار حضور داشتند.
@FarsNewsInt
-
Link</div>
<div class="tg-footer">👁️ 4.12K · <a href="https://t.me/farsna/461845" target="_blank">📅 19:25 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461844">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ewq10XHReVBnVtT9B5ZnL9UZVyuTl0A3ERHdfx7WwoTxVXM9L98195GIFsbYNJ9DG1cHeHeUlMqJCvpZ2OkJzRrnFgT8yizddKLzVkwWBvB67-d_p4E0StVvkAqytVIpSRIagCJKNJFQZ9QGioZqhfP8L6v4jzL2mTScayYi1aXl75nd-NS2z_UWgZOCMVsLyPwhQRRsiP3AYCILSjkXwNQiAST9JSoLf4FRruxSodmC93d3uWK_XpIhxgE1uk_FXLrhSf8pLaDUAArfWZYnAeFWWVeAVjPltdPA4hx7t-XdnV8ZCP_fyhcS2xIVX2g_qX-QYYoTpJ-AHJ6LKICX8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
رونمایی از لباس استقلال و السد برای دیدار فردا
🔸
این دیدار در چارچوب هفتۀ اول لیگ نخبگان آسیا،  فردا از ساعت ۲۱:۴۵ در بصرۀ عراق برگزار می‌شود.
@Farsna</div>
<div class="tg-footer">👁️ 4.8K · <a href="https://t.me/farsna/461844" target="_blank">📅 19:17 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461843">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">یمن اتهام سعودی دربارۀ حمله به یک مسجد را تکذیب کرد
🔹
خبرگزاری سبأ یمن: یک منبع نظامی ادعای رسانه‌های دشمن سعودی دربارۀ اصابت موشک‌های یمن به یک مسجد را بی‌اساس دانست و گفت: تأثیر موشک‌های یمنی بسیار زیاد و مشخص است.
🔹
به گفته این منبع نظامی، علت این حادثه سقوط موشک‌های رهگیر پدافند عربستان در مناطق مسکونی است.
@Farsna</div>
<div class="tg-footer">👁️ 4.76K · <a href="https://t.me/farsna/461843" target="_blank">📅 19:12 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461842">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ALO87-p8WHNfK68R2xE4SnH2-lFsEKx8PtJL2g1mUF8WcWUawGJLd2XJgBChB03E3OgeG46Ix5dPFlWuLrjHhYv7G7iV9YxlAxgX_uTQLUa6DGJVYjNnWIxKSbfeztPBNKmgesu6anvsYeSZASHyoaffX57P4EJ3QXet5mpn-_Em4GAbu6Eg2YXfJFCaGuwrDA_JWyqcOrL_FqsazWNJacAtAXuBggUOxA7BzGUsm2Rq9_Gh4mOHgVsRXOBPDVtK0Zm4F_PuMdU1Es78b5paBjDL929QFJd6htWoQ1jPwe_8Sc8VLOv5gxcLoaFv9PzM3aHXsb-TaXp3IWmT-MD_1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک شیر دریایی بر اثر آنفلوآنزای مرغی جان باخت
🔹
ادارۀ محیط‌زیست استرالیا اعلام کرده که آنفلو‌آنزای مرغی باعث مرگ یک شیر دریایی استرالیایی که گونه‌ای درحال انقراض است شده.
🔹
کارشناسان می‌گویند گسترش آنفلوآنزای مرغی H5 می‌تواند باعث مرگ‌ومیر گسترده در حیات‌وحش شود.
🔸
مؤسسه پاستور فرانسه پیش‌از این گزارش داده بود که آنفلوانزای مرغی درصورت جهش می‌تواند قابلیت انتقال به انسان را پیدا کند و یک «همه‌گیری شدیدتر از کرونا» ایجاد کند.
@Farsna</div>
<div class="tg-footer">👁️ 5.11K · <a href="https://t.me/farsna/461842" target="_blank">📅 19:07 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461841">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f11d60c2a5.mp4?token=EMsTAtShmPHka-3oO47VEN2mQrx2zSMStUvEpWnd9ydImVyD43NyeQcOdozjsyFZfg3DgET_DThOnpe8GbWo8-ID8NQYKcLYTz_NH2o6rv3ytAJQgb9kE0RrH9QqXaW6fIlzSAJ3E4SJAB8GtGa77gsuvZBKKa7PLxZKCo1QGaUFnVM5ZjYn4venUrcdzYfqFoVJTPuvulRZoOozXgyL5gJWbW1wqiaNWafbZbGDxpdGFTo81W6NIl-kfcv6s9mGy5ZjuIC8IwGaddm3w28_FH4jMn-gc7pPYFJPSgVfDsCfYm5mc7I6Sga6aNv3FZvnR1V9vqF5KzOur8OXSWwgzA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f11d60c2a5.mp4?token=EMsTAtShmPHka-3oO47VEN2mQrx2zSMStUvEpWnd9ydImVyD43NyeQcOdozjsyFZfg3DgET_DThOnpe8GbWo8-ID8NQYKcLYTz_NH2o6rv3ytAJQgb9kE0RrH9QqXaW6fIlzSAJ3E4SJAB8GtGa77gsuvZBKKa7PLxZKCo1QGaUFnVM5ZjYn4venUrcdzYfqFoVJTPuvulRZoOozXgyL5gJWbW1wqiaNWafbZbGDxpdGFTo81W6NIl-kfcv6s9mGy5ZjuIC8IwGaddm3w28_FH4jMn-gc7pPYFJPSgVfDsCfYm5mc7I6Sga6aNv3FZvnR1V9vqF5KzOur8OXSWwgzA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حملۀ توپخانه‌ای رژیم صهیونیستی به حومۀ بنت جبیل در جنوب لبنان
@Farsna</div>
<div class="tg-footer">👁️ 4.79K · <a href="https://t.me/farsna/461841" target="_blank">📅 19:03 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461834">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KOCct3OCXb-2jIKMnHVqtiDB16-DxC9IegwBTWkcmu2HoC40UPvRbNrIGlSw2xB8bx8UbHPNcI02HsGV9HiuRZhkbQYaq-poY1iHw9DNBBWErO9IjT_oM63LSyljMnT0axoinmvhlBtQx00n0SKKkfH83mei2vvawBFFMjBmoi4D4at9oOVEdL439lTwVcZdjMsu38P6_nwJIASR7UxdoE6ckAvZ71MeqadnY5NcKFIz944VA7Wqux94aksKhhnBQIRUUt-mms7eGRj_PI1kLYs87HLqxg6wZKXuxuMuE47UJIKd6fHqxkxNli5ng_PQzqKzQXqwS5sv8qezWufFIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CmJaObnqm_XTEWnTr9HXTNPIy-a8kgrHI-Qkz9uuPOGZfIHHWMwj5MdbVSGSZIig0gWLijhHQRUlIhCL--bcMVCQL4ZI5kDDEi9cvuStuWlPCp1cV36lnoe82tPSX2DHcoPvVP9HW1e7XkYHl3162FkCeO9oaSDNCkRvZXYoIBaRVU50GC_mJ5Pv0Bo9gY6jYLL9JNixDKgHJSLFma1bK246UWgyfVNTssT6BSVqQHQ_o2joMSM-J0qOQSF_8j4VGHDtN7iPjYfAUDXfSAlhXENB8QciWP_-rd4zMjZYTRDosv63QJhTjuvTDPmVTbTSyahgIqET5QzT1OMfgPaxwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AT_YcRyOv5BPXBrNBMHF1g_bPgnVLSlBvHHQQZK_HVjiznRjAGVJaacL3ZkcSUN343D2wa1uvJIv9ObMzGiO_wYzqVmdboKilC_ac7t4kXHw4zfd7mlFAbJHm2v1JZf8HeEHVVDNVEU41uIkZ-Q5xRP5MiF3Ccw9eDf1D9aYHo8JVd3fAINgWMm6c-7scCGMbHKf40teqefQqfS1fG0xd7RYfMYju3kjNxL8Uy9Lload0ZBrDcd8IdvdBeTQK_abBwHbunSx8TLi2wyZWZFWi9SssQaVP231DMeL1YqL3Ha_5s4QS6IWzi-SltC54r-FLGqRW6h7UcIe3dcIBhLAFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/k0EmwEPnzLKadNS7-tEiIPU5ATi2uaHDkpOTomxH6rNtx4agHKFmCUdUl-5DgEuYBHFs2Dv0xos2Gu8c3Y5wafQurou2vKYeMpz1-cKNX1ijCktGvCgV8oFfo1Cn9Rg6OHIEAUdJTQgxNYfNZLKxYY9k9DEB17TGl8fNl6HXTR2GzsUvhBopuhKngBg702KIwQvElgniizoVSdInL7x2VIcOCrhMYg1Y2x7KuzYXvkwozX6feftFykvVZoHq1OcnFSXzEoNr47Fig63XO8eMyp7usmfn8Hn1uEFSZe_Xo3nTNzGCytFd6cC3Ncn6QboZWMuwnhjC-wshrP-9J_7vhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rjJhmDh38o9BhWdjb3QIOPBYOktL38FDJhfVk6MdzsAeg4yL7CW8GcyEFV50aaYtZcRw2MXOoG9ujiT0OL5X-VvtcgyRwmn5eeUz4zysxR7rk3gev2_hgfzzEnAqsbduyqnE_0A4ftCefvEjHnB-YI1bmSyOWiYbwY9FLdditO1ZcJfgLRcUh5aP03i34TTZVBfoAFMZ99_IDq_f1ET9ZFMo3cZaYvxK79gSjL-Wt5_8t9VIYW01-U3Wj4BS5_N8lqsRJaUnWBM4V5tnNCAvitHhDNGAdLLqPAD5GLPiGcbBrV-Ji8G0MQueGcE9bzp-BsW6gtMFWzlRVQNQqg315A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YapOX94v7vH4XOQhlwfwoIS2PhsroRJ66MsvRWMwWN3nyd6Kz_FWW0Z1JUXnIH0IaTY6UyYhIBpo4VZNL-ZwqxqDTbgG0ezIhm6P9VAcJCnV8X-hFvDYWwut9JcTtxJ4ChYLHX9b28qCIWS98EsT7OTlmB8mCmxNIbnoXpLrojXSPWtCvnqy7Gus_mYUvu_INOxhSMBlV7YFSf0J2xYDnLdfGhRLwUdRMNohjY6cQENBFUQ4v3sDOO89MI9Rax2piJ19Elgz-tHf9rKwSCpfEDWBBlg8i1qJydKocieGgCvhBWcuA-hx8T_aan9-PquplUrhcFvB4EG2uuMB3A9s1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iEHBKQpoqnH9TsX58rg842JyP_o_uSlRLCgqbe-IZqaxJicVF0XjUUaJmwJsZpYqGJbT_X2dlW9rYVfdf2GKPkhzme8e7y9a_TXXEeWOrab1E6tXcUn8FKhtaSp3syBtgJMZu54alw70P2hVYHNXSLL2YMYLS988seghSVg-4k6iYbUBiBPwKMoc2zcPLbV85lrRYJ5El87UNpK_bzM9AccIEX0CWUdJnl9phRNML2ybaD7SVat0x2bUUB1UPEHF4N-3zEDp9KrXCJuY36PBbMq8DYMKJkImlHso1E_pshD_7HhQ8_y5bDDGmygDzCEWGJOqmsnYEw8mjNPOrPJ_bA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
اعطای گواهی درجه یک هنری به علیرضا داودنژاد با حضور خانواده او
عکس:
زینب حمزه‌لویی
@Farsna</div>
<div class="tg-footer">👁️ 4.84K · <a href="https://t.me/farsna/461834" target="_blank">📅 18:59 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461833">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">بانک مرکزی سراغ ۱۱ رئیس شعبهٔ متخلف رفت
🔹
بانک مرکزی: در ادامهٔ بازرسی‌ها و  رصد تراکنش‌های مشکوک به پولشویی که منجر به اخلال در بازارهای پول ارز و فلزات گران‌بها می‌شوند ۱۱ بانک متخلف نیز جریمهٔ نقدی شدند.
🔹
با هدف ایجاد بستر لازم برای فعالیت‌های اقتصادی قانونی از همهٔ ابزارها برای انتظام‌بخشی به تراکنش‌های بانکی استفاده می‌شود.
@Farsna</div>
<div class="tg-footer">👁️ 4.83K · <a href="https://t.me/farsna/461833" target="_blank">📅 18:58 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461832">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">🔴
منابع عربی از شنیده‌شدن صدای انفجار از تأسیسات عربستان سعودی در شهرهای خمیس مشیط و ابها خبر می‌دهند. @Farsna</div>
<div class="tg-footer">👁️ 5.13K · <a href="https://t.me/farsna/461832" target="_blank">📅 18:55 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461831">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b857003bf3.mp4?token=AhwDRi5nDuKqFJyy-4yGgkdxfO1Wh84L-KNedHaYuvZq0mIosoicrIemw4SHjleIUvbUYhdrwYjnvWW8b7o7O4dC9ABWlP8PW8Q97N3bb_WHR7ciiK0WJLMF0QA5cOhmnXHCR0kBVbhZUmUc237NzzhSLFaHRcHHBxr0XIXJncgbzXsXSmzXEPTNbSQF9wzHEHTUA1nMGzau-xTIz-EEA601mm6KDqZO25GwwECStj9v4IW9e5j28yIJACpRGnm6RoLkYsM0waXFcD5pls9znqYsHI2Izn3U3523eM4HoRCkAe_-kcxao6JnRTs_Bp23MueAcnAmblbx-ekfVstjkQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b857003bf3.mp4?token=AhwDRi5nDuKqFJyy-4yGgkdxfO1Wh84L-KNedHaYuvZq0mIosoicrIemw4SHjleIUvbUYhdrwYjnvWW8b7o7O4dC9ABWlP8PW8Q97N3bb_WHR7ciiK0WJLMF0QA5cOhmnXHCR0kBVbhZUmUc237NzzhSLFaHRcHHBxr0XIXJncgbzXsXSmzXEPTNbSQF9wzHEHTUA1nMGzau-xTIz-EEA601mm6KDqZO25GwwECStj9v4IW9e5j28yIJACpRGnm6RoLkYsM0waXFcD5pls9znqYsHI2Izn3U3523eM4HoRCkAe_-kcxao6JnRTs_Bp23MueAcnAmblbx-ekfVstjkQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
گزارش شبکهٔ ۳ از پیام مجاهدین یمنی از تنگۀ باب‌المندب به ملت ایران
@Farsna</div>
<div class="tg-footer">👁️ 6.12K · <a href="https://t.me/farsna/461831" target="_blank">📅 18:44 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461830">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🔴
منابع عربی از شنیده‌شدن صدای انفجار از تأسیسات عربستان سعودی در شهرهای خمیس مشیط و ابها خبر می‌دهند.
@Farsna</div>
<div class="tg-footer">👁️ 5.81K · <a href="https://t.me/farsna/461830" target="_blank">📅 18:44 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461829">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f0dcc3c402.mp4?token=hbQOUBnUr-OHQfmWIsLp4aQjbHiDbxMQ8jnwNSunv9MaEvcTPlzYTdQPzgRxtqhmAkfrNeQyMA4ek3WJ9QLVyiBf5lzRRaFSbzAEapb8rlBAFUSk-Zav7ru2vgo3WaeSF8JXrJmLchAevMryQM0roxEHU_5_QACTPMyX7U7b1_3cKBEXqeSuOW7agNlBoRizSaIXUCauNum0Dc2GKhfbfPS7CC_3PX64p6EKZMS82UplF4b4O6sSenIED_Z6svyJuAgWZpSy4ShryoIOrL9-_t7CFmwG67UpeOVT2l6tUzdAgZbUCv6DIS2-XdvTWuHLWkvEIC69aIPtAhlJzfeZhw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f0dcc3c402.mp4?token=hbQOUBnUr-OHQfmWIsLp4aQjbHiDbxMQ8jnwNSunv9MaEvcTPlzYTdQPzgRxtqhmAkfrNeQyMA4ek3WJ9QLVyiBf5lzRRaFSbzAEapb8rlBAFUSk-Zav7ru2vgo3WaeSF8JXrJmLchAevMryQM0roxEHU_5_QACTPMyX7U7b1_3cKBEXqeSuOW7agNlBoRizSaIXUCauNum0Dc2GKhfbfPS7CC_3PX64p6EKZMS82UplF4b4O6sSenIED_Z6svyJuAgWZpSy4ShryoIOrL9-_t7CFmwG67UpeOVT2l6tUzdAgZbUCv6DIS2-XdvTWuHLWkvEIC69aIPtAhlJzfeZhw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
راهکارهای پلیس فتا برای جلوگیری از کپی شدن کارت بانکی توسط کلاهبرداران  @Farsna</div>
<div class="tg-footer">👁️ 5.84K · <a href="https://t.me/farsna/461829" target="_blank">📅 18:41 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461828">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LwfQEStntHf75IRGHzURrz-WzeJRhP_Iyqyv5oI4n6u4ZuWf6gmT74SUiH72yfeKIjH5AHaQPKtj_CHKd_VN59_HzKaGRvEacMj920YraDyd3L51It4cxtdD8Hm8Uki4hK6mDOf-BEGKi3pr1gdYKRMcdW5EJ9BptYIkCtk9pt_hcyUDCndifY-MZCiEx6voiKFTK7q2aIMt1W-XgVaaLOQ02mlgKs4v_V2ycebn8b5eWixAjoT_Bg_H6dj3Fri3B098G7dz6yjgJVrc8dO2ciC3LiJcalhqX8o1IkD6YSEy6q6ORkRshkJZxW4yUVWkTZBmFbhhmw-KnWa8rAva6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اتمام تابستان در وزارت نیرو؛ مردم همچنان اسیر خاموشی
🔹
سخنگوی دولت دیروز در مراسمی کنار وزیر نیرو اعلام کرد: «با همدلی تابستان را پشت سر گذاشتیم».
🔹
این درحالی است که اسناد رسیده به‌دست خبرنگار فارس، خاموشی گستردهٔ برق خانگی در روز گذشته، یعنی هم‌زمان با برگزاری این مراسم را تایید می‌کند.
🔹
عباس علی‌آبادی از یک ماه پیش ۴ بار وعدهٔ پایان خاموشی‌ها را داده اما برق خانگی همچنان قطع می‌شود و صنایع از تشدید خاموشی‌ها خبر می‌دهند.
🔹
میزان خاموشی روز گذشته ۲.۵ برابر متوسط خاموشی در یک ماه گذشته بوده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.79K · <a href="https://t.me/farsna/461828" target="_blank">📅 18:35 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461827">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gGLNXow5lVFogruawinjfQ2Sc0cApiy-i40DgEWEFoBtrwE0LuLWz1ZGh39rHvtOu4tTCkpuQ0MMVTy1U4dPlvdBPvIQJM2ETapWUlnBOrXhfz7UGUfspMSnv3UlLcgbaQzly2DfReb1dt6WbvHhwVCd34t8PdgTyU3YOk8lvtfoe3peEEwsmJqxBAzlBHR0bQfagRFDyHondDYvu8v9eP70pbT_DUUOff1OaWwo5eVuKo_kAKpdYRZSsNkv9sySL4tJCZJ4vMrQ0LiQlRYVGCUot1jjgvjUTGTQ4aWWM_xt9aqX_oPG1A2_92O9e-IlOPEab-Sp7HMvkAlyZVnaEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آلرژی پاییزی را اینگونه مهار کنید
🔹
اگر با شروع پاییز دچار عطسه‌های مکرر، خارش بینی و چشم، گلودرد یا سرفه خشک شده‌اید و احساس خستگی مزمن یا کاهش تمرکز دارید، احتمالاً به حساسیت پاییزی مبتلا شده‌اید.
🔹
این علائم که اغلب با سرماخوردگی اشتباه گرفته می‌شوند، نیازمند مدیریت دقیق و پیشگیری هوشمندانه هستند؛ برای اینکه پاییز امسال را بدون دردسر سپری کنید، ۴ راهکار ساده زیر را جدی بگیرید.
🔹
مدیریت محیط:
محیط خانه خود را از گرد و غبار پاک‌سازی کنید و در روزهای آلوده، پنجره‌ها را بسته نگه دارید.
🔹
حفاظت فردی:
هنگام خروج از منزل، حتماً از ماسک استفاده کنید تا تماس مستقیم با گرده‌ها و ذرات معلق کاهش یابد.
🔹
بهداشت فردی:
بلافاصله پس از بازگشت به خانه، دوش بگیرید و لباس‌های خود را تعویض کنید تا ذرات آلاینده به محیط زندگی‌تان منتقل نشود.
🔹
تغذیه:
مصرف مداوم آب و مایعات کافی را در برنامه روزانه خود بگنجانید تا مجاری تنفسی مرطوب بمانند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.6K · <a href="https://t.me/farsna/461827" target="_blank">📅 18:31 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461826">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fuzB74gtOzc7cEnjB0O_O3gkoh7DZ4Aaeit4qiz6NQ58D9PIANGD0jzM-NW4XOTJQjG58MBvRNt9Eg617UGMIkC3wgsJUcRNY6xfGVFk0Xhva3wFGLLS2nwFj4JGT-EFS0lRjEU_qpez0AiQAvWaKb9Fgo1OFMO6NGMP6zAQcsW_d24kI3pmSqv9fa5Dbe5nVOCeMoDrkZrMSLyqwOHXcSzI5go_tFriEfQ4mGy_jazNxpEyFg0rIqRWUbLRL89nLWnqJSyHx8JunMT3UN1hqvZfcwiLqe5GTGCfrQ5HGPU3mo7JdMkJnWNOXLE7C-8OaZG4Av3gyEVi8EYVKG8U-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پروژۀ جدید پرسپولیس برای «پرسپولیس ب» کلید خورد
🔹
یکی از گزینه‌های مدنظر مدیران پرسپولیس برای راه‌اندازی تیم «پرسپولیس ب»، خرید سهام فولاد ب بود؛ تیمی که به تازگی جواز حضور در لیگ دستۀ اول را به دست آورده است. اما مذاکرات در نهایت به نتیجه نرسید و مدیرعامل…</div>
<div class="tg-footer">👁️ 6.04K · <a href="https://t.me/farsna/461826" target="_blank">📅 18:19 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461824">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفالس نیوز</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/03d22c8476.mp4?token=b4kCn7er0QYQHk8aINZc-8Qc6flMdqvGYXK-vlXoHv20vAbCgHwc8aw1CVw1GOlIAzR-7zQyeHvI3IyskFqYBWwytQEB7nXBdZ9enCwG8vbLcf_ogS6c2n8ZSNbhSg9MokXG9P-9zbqJ5RihahzE59XpbY_NeS8g6D5nfgpLYGyx1L2lloEvVw2L99i0m9wScfFZIQp6OmRL0VDE_u6by_3MEXB6bVSeZiAkisSTpxa6Jx1-hClWLG_Q51tLEX5j7I5oGTxauEX91Wwfa-OcDU3fTdifSZUOY24uhMvZPB4vmtCRUSg_uKYjhcZGuzw29voWJMiakfBWzM64SbDmNQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/03d22c8476.mp4?token=b4kCn7er0QYQHk8aINZc-8Qc6flMdqvGYXK-vlXoHv20vAbCgHwc8aw1CVw1GOlIAzR-7zQyeHvI3IyskFqYBWwytQEB7nXBdZ9enCwG8vbLcf_ogS6c2n8ZSNbhSg9MokXG9P-9zbqJ5RihahzE59XpbY_NeS8g6D5nfgpLYGyx1L2lloEvVw2L99i0m9wScfFZIQp6OmRL0VDE_u6by_3MEXB6bVSeZiAkisSTpxa6Jx1-hClWLG_Q51tLEX5j7I5oGTxauEX91Wwfa-OcDU3fTdifSZUOY24uhMvZPB4vmtCRUSg_uKYjhcZGuzw29voWJMiakfBWzM64SbDmNQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">از شایعه تا واقعیت پابوسی پزشکیان از راهب هندی!
❌
به‌تارگی فیلمی به‌سرعت در رسانه‌های هند با عنوان «پابوسی رئیس‌جمهور ایران از راهب هندی» دست‌به‌دست شد.
✅
اما واقعیت این است که در جریان دیدار پزشکیان با برخی از مقامات و چهره‌های هند، رئیس‌جمهور کشورمان با یکی از رهبران معنوی هندو در حال گفت‌وگوکردن است که نامه‌ای از دست پزشکیان به زمین می‌افتد و او برای برداشتن نامه خم می‌شود.
🔎
برخی رسانه‌های هند با انتشار این فیلم از زاویه‌ای خاص مدعی شدند رئیس‌جمهور برای احترام به این راهب هندو خم شده تا پای او را ببوسد.
⚠️
منابع سفارت ایران نیز در واکنش به این شایعه گفتند که فیلم منتشر شده، از متن اصلی خود خارج شده و به شیوه‌ای گمراه‌کننده ارائه شده است.
@Fals_News
-
Link</div>
<div class="tg-footer">👁️ 6.25K · <a href="https://t.me/farsna/461824" target="_blank">📅 18:10 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461823">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ffbed1e0a3.mp4?token=WfYD7-CJIQSvNCXOLquK83PkRzs9x1gbMNQDixYPMkeYMefsZZ6S0zV1BoO_WXhlQvs493Y8bzOAmQJiGUXKFCOlUcIibPpoA44XF6D-Zvnqgum7SR1tyoBF0IIxYJmneBbfHG7FADRKkeUdYtzX3So3-gJIQI_L7yTwP_oknwBqmtps7MN3VOD2F2B2hiymsoaamCGhBiwI0hf7rJZmiBaVLRUCTuxexEbp5AWvF41J4U4GbLTUXglF-EXOVJrEuebMviMg45ueSeumTCKpR8yt5KNkThJwsGBDLeK_DwphnqbPAoL6RdWNSpbp0zgQt9u-dv2-8spgH3qTrijUxQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ffbed1e0a3.mp4?token=WfYD7-CJIQSvNCXOLquK83PkRzs9x1gbMNQDixYPMkeYMefsZZ6S0zV1BoO_WXhlQvs493Y8bzOAmQJiGUXKFCOlUcIibPpoA44XF6D-Zvnqgum7SR1tyoBF0IIxYJmneBbfHG7FADRKkeUdYtzX3So3-gJIQI_L7yTwP_oknwBqmtps7MN3VOD2F2B2hiymsoaamCGhBiwI0hf7rJZmiBaVLRUCTuxexEbp5AWvF41J4U4GbLTUXglF-EXOVJrEuebMviMg45ueSeumTCKpR8yt5KNkThJwsGBDLeK_DwphnqbPAoL6RdWNSpbp0zgQt9u-dv2-8spgH3qTrijUxQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مدیر سامانۀ هوشمند سوخت: هر راننده فقط می‌توانند ۱۸۰ لیتر بنزین در کارت سوخت خود ذخیره کند.  @Farsna</div>
<div class="tg-footer">👁️ 7.25K · <a href="https://t.me/farsna/461823" target="_blank">📅 17:58 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461822">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i825F6Azq4BmoQy8AhAmYK4FDWMURl6EINUDpCxEzguWY_ksC6FLSnLAtvo4i-hbTYTAc9pnFsUo3NF1UhXRlmMGK97G1QkHTmZNq0pcOyxZBRmkXM6uTS-fFcBkosr7EnLuVrtoXGPPi68CZJJEerALdSgxCmqo3yMtqYNjVTQP-1B122lFEj1Z7b82v0ms6OzRDuCgzMIx_2gmramKAFzZkiblw0ZHcvbB5XDe-t4vX2WRVt-oqEMeuvqxjomLeyNgutVRdglZlbNP5kbgCBAk4tbaqFBSeKfFU_ywmKjK4zJX-o5LlZzR8OqBcj236x2kB6Y1kb3kuzsb36LoyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترکیه به محکوم‌کردن حمله به خط لوله عربستان اکتفا کرد
🔹
آنکارا که یکی از اعضای پیمان دفاعی مشترک مکه میان ترکیه، عربستان و پاکستان است، در واکنش به حملۀ پهپادی به خط لولۀ راهبردی شرق-غرب عربستان، به محکومیت دیپلماتیک این حمله بسنده و بر حمایت از حاکمیت و تمامیت…</div>
<div class="tg-footer">👁️ 7.33K · <a href="https://t.me/farsna/461822" target="_blank">📅 17:54 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461819">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PeWWs-6D-S7KneubYxZtgkLQ6MOB8z3WMDjknSwSQ3eIAENk-CIl3ghjMcLqsGr70HNxy9J3rhpKYN8Jlcc4mReZ_eXgL6hCgR_J4_8FimBMaEZldplIUXriHDxgCMCpo7yDHHA1DOMOZv75qqiphs7M4z8Nu8RJJs7wL2vzo7Li9UuHf9bDTCiIgUfjIAK6wy-wr00Wf_1iNlZQvJix2Nm5ELsYWOjTZi81-FV5SOgYZ_h1ZJ3QCmGES-fPSWbEcejHdgjm8u9ciISDsDCjA5s6IrzMzJ_C_n1JtN7k3ee2kIT1tfWEcGc7uUE5_K6iUWgXFy8176eXdBxxADZMmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۵۱۷ تن طلای عربستان در آتش پهپادهای ناشناس سوخت
🔹
رویترز: در صورت از سرگرفته نشدن فعالیت خط لولهٔ انتقال نفت از شرق به غرب عربستان در روزهای آینده، ذخایر صادراتی عربستان در بندر ینبع تنها برای ۵ تا ۷ روز کافی خواهد بود و این وضعیت می‌تواند به از دست رفتن حدود ۴ درصد از عرضهٔ جهانی نفت منجر شود.
🔹
خط لولهٔ شرق به غرب که روزانه حدود ۴ میلیون بشکهٔ نفت را به ینبع منتقل می‌کند، طی ۶ ماه گذشته به عربستان کمک کرده بود تا از پیامدهای اختلال در تنگهٔ هرمز تا حدی در امان بماند.
🔹
قطع کامل صادرات و ضرر روزانه ۷۰۰ تا ۹۰۰ میلیون دلار (میانگین ۸۰۰ میلیون دلار)، عربستان در ۶ هفته (۴۲ روز) بین ۲۹.۴ تا ۳۷.۸ میلیارد دلار و به طور میانگین حدود ۳۳.۶ میلیارد دلار خسارت می‌بیند.
🔹
این مبلغ معادل ارزش دلاری ۵۱۷ تن طلا است؛ یعنی پهپاد ناشناس با توقف این خط لوله، به اندازهٔ ۵۱۷ تن طلا از جیب عربستان بیرون کشیده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.44K · <a href="https://t.me/farsna/461819" target="_blank">📅 17:46 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461818">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/674a05064a.mp4?token=EO3I_CfQ7Y8eHQZU2tNTLu8pV4mn-rAhfmGgx3mmESThTq0aCnlciqJCaTnS07chg0LGTfsTvFjZ1cf_lEY0ghI7lY2HqohCtDDjxQ-PzK_Qy8YNSASuaxzh_SQge6lHIQ6jxJ0TF5s_y8hJLbSJTnL1yjzeKq1ioJ3olX5GQt5QThYve5oqJT6MZV9gM173KcSbKfMMmK9RYW1h24I9mfVNd0SVKGNSxFjBS98MfPvJXLYxuPvm67O3hbQ9ivk4z6XHEiEZs-Op_cST-Aolz7gHpr_54r0XK4gZ7qG1sva50RKZCIGCZJ8XMG1FpTdO8Q3LyacHBq3tOjBmsSYpKIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/674a05064a.mp4?token=EO3I_CfQ7Y8eHQZU2tNTLu8pV4mn-rAhfmGgx3mmESThTq0aCnlciqJCaTnS07chg0LGTfsTvFjZ1cf_lEY0ghI7lY2HqohCtDDjxQ-PzK_Qy8YNSASuaxzh_SQge6lHIQ6jxJ0TF5s_y8hJLbSJTnL1yjzeKq1ioJ3olX5GQt5QThYve5oqJT6MZV9gM173KcSbKfMMmK9RYW1h24I9mfVNd0SVKGNSxFjBS98MfPvJXLYxuPvm67O3hbQ9ivk4z6XHEiEZs-Op_cST-Aolz7gHpr_54r0XK4gZ7qG1sva50RKZCIGCZJ8XMG1FpTdO8Q3LyacHBq3tOjBmsSYpKIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ساعات سرنوشت‌ساز برای بیرانوند در لیگ برتر
🔹
ساعت ۲۴ امشب پنجره نقل‌وانتقالات لیگ برتر کشورمان بسته می‌شود و تنها ابهام باقی‌مانده وضعیت علیرضا بیرانوند است که طبق قوانین از اول مهرماه سرباز می‌شود.
🔹
بااین‌حال کنکاش فارس نشان می‌دهد که بعید است بیرانوند از…</div>
<div class="tg-footer">👁️ 7.81K · <a href="https://t.me/farsna/461818" target="_blank">📅 17:42 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461817">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/050035a39d.mp4?token=TPSlw8kZDY1rEkWCoUTk4ptmvS4rq4enZBJpjPuAi2tp_1GQiD4mVlCb4soPEuOsUq6Sds3rX-tNay2_Fr_a3HX63t06vUImzCtCw0_Yr9vZauCTPxwGWdA21kG0nQWyfc5dxtAUmIZaRbFwF3UFow9OrWM-QNABnH7jf5Aoz7BflLMCaOjbFDHluDTTss5oGE9BYZ9NKnOoJ0JLEs_zmCjEKaQu3kWwkEoVO5_GbD6A-StQEzzYK2HUeCNOiGjZlVtma7JYcLWoMXu11JR_wpi_0Pyy1ETApaR_s7I1a608y9fTXaEDdqHEuaYRIFc5XFGdIyMjiDb4ccfYKnyCsA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/050035a39d.mp4?token=TPSlw8kZDY1rEkWCoUTk4ptmvS4rq4enZBJpjPuAi2tp_1GQiD4mVlCb4soPEuOsUq6Sds3rX-tNay2_Fr_a3HX63t06vUImzCtCw0_Yr9vZauCTPxwGWdA21kG0nQWyfc5dxtAUmIZaRbFwF3UFow9OrWM-QNABnH7jf5Aoz7BflLMCaOjbFDHluDTTss5oGE9BYZ9NKnOoJ0JLEs_zmCjEKaQu3kWwkEoVO5_GbD6A-StQEzzYK2HUeCNOiGjZlVtma7JYcLWoMXu11JR_wpi_0Pyy1ETApaR_s7I1a608y9fTXaEDdqHEuaYRIFc5XFGdIyMjiDb4ccfYKnyCsA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">روش پرداخت کالابرگ ۱۴ سال به صورت یک‍جا به مردم
🔹
با مسکونی کردن فقط یک درصد از مساحت ایران، به هر ایرانی ۲۰۰ مترمربع زمین می‌رسد. با توجه به متوسط قیمت زمین در کشور، ارزش این زمین می‌تواند برای هر نفر به بیش از ۲ میلیارد تومان برسد. این رقم به اندازه ارزش…</div>
<div class="tg-footer">👁️ 7.65K · <a href="https://t.me/farsna/461817" target="_blank">📅 17:38 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461816">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">حملۀ عناصر داعش به ارتش عراق در کرکوک
🔹
برخی منابع خبری گزارش دادند تروریست‌های داعش به یک مقر ارتش عراق در استان کرکوک حمله کردند.
🔸
هنوز ارتش عراق به صورت رسمی این حمله را تأیید نکرده است. @Farsna</div>
<div class="tg-footer">👁️ 8.49K · <a href="https://t.me/farsna/461816" target="_blank">📅 17:08 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461814">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BKCh3HO_Ax4HAFzVNrmzQnAUQU73ZkljjYw4lqe_S7vx0LcOCVyczokDXYypOCCBSZ8RZE6nijdc-WAhlGisilTnSYYckvTojqT67YhD78HT2VF3tk5SNOAeJUWqSf6PSIclIrk6ESH-28jBUtkMgu8ZSqzMlmPJRwtT2yq2OC4o29_YATnLppZ6VRd_Pmo-FnGc-2z_eAi3xLuABsyjFxmAxGbd0OKjjypR-pLqY4Qfb4w1jX_0wlds9hs-GJff-GerFu6tFj3vsgTnhGHZCBab30PZFFxUCGP6lzWKV54EZaKeGqc069DxLjlUHkpaPW-Zt0YLLNJUEII3Vqxy4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عراقچی و عبدالعاطی وزیر خارجۀ مصر در حاشیۀ اجلاس سران بریکس در دهلی‌نو گفت‌وگو کردند.  @Farsna</div>
<div class="tg-footer">👁️ 8.9K · <a href="https://t.me/farsna/461814" target="_blank">📅 17:05 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461813">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/566cf6be2d.mp4?token=ucV0eYxVmT7EvASNVJ2rn2PBXhjDwmTTmK36UA39dZb2YJ9MSh9DsafHPsnodHmCJ9z_nEWGluJ7yjSRTBN_XdmwCbJ10G8czDhgxSGwhSluUlh2Rpob99-Vm7js-K9wQCSCXiVTXPVtBarOakoYFnKVBqsZ_bgKMdrd0Auh_mUs4aR-j1wYljJWEWRbb2EcYN3CMfWEw9QLsuOz31Mn1eH522MPwpY09sGN7ZiB0lwFha8H2vGT3g1VmiyYoKjp_uia-8Yh-gGhN7IRCGPL5i5-2zPB1Z_DhMvDDObOtHkF0LpSFGIx-ukRGsOQ48nry3drPutMCHcTjZxE7DX6dA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/566cf6be2d.mp4?token=ucV0eYxVmT7EvASNVJ2rn2PBXhjDwmTTmK36UA39dZb2YJ9MSh9DsafHPsnodHmCJ9z_nEWGluJ7yjSRTBN_XdmwCbJ10G8czDhgxSGwhSluUlh2Rpob99-Vm7js-K9wQCSCXiVTXPVtBarOakoYFnKVBqsZ_bgKMdrd0Auh_mUs4aR-j1wYljJWEWRbb2EcYN3CMfWEw9QLsuOz31Mn1eH522MPwpY09sGN7ZiB0lwFha8H2vGT3g1VmiyYoKjp_uia-8Yh-gGhN7IRCGPL5i5-2zPB1Z_DhMvDDObOtHkF0LpSFGIx-ukRGsOQ48nry3drPutMCHcTjZxE7DX6dA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
زمین یک خودرو را در نیشابور بلعید
🔹
درپی فرونشست زمین در خیابان فردوسی شمالی نیشابور، یک خودرو در زمین فرو رفت.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.96K · <a href="https://t.me/farsna/461813" target="_blank">📅 16:53 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461812">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a141234c8f.mp4?token=D5dIkQorr4OxHNLYnDAmQyCetRcRbyipB56NCHwslWoY2kKqSx2N01qxHwYV2ic2ChcUvk_rYXy_zmUzV4_whuJ09xeUef8QZsskIcoKMrwpKR-VrWowH62AKJGAn54c7VnClqKbSfOmB28eimIaVu3e5nRpSE4V4pnR0pl-yMkir5xCuIY0k0dHJdhmf37auCSWwJkuhMbUCXWaSLnXxZ9OGq90qzistWmzD-305QGvF5_Eurkf873E2B0z_3i7OyrGgvdxyd246fLQqnM7-oCzej2XjD8BJh7eixcHhKQObVTGdTSmKLi91oDmrhqmgkK1ErBqfje3zSo0AjYQSA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a141234c8f.mp4?token=D5dIkQorr4OxHNLYnDAmQyCetRcRbyipB56NCHwslWoY2kKqSx2N01qxHwYV2ic2ChcUvk_rYXy_zmUzV4_whuJ09xeUef8QZsskIcoKMrwpKR-VrWowH62AKJGAn54c7VnClqKbSfOmB28eimIaVu3e5nRpSE4V4pnR0pl-yMkir5xCuIY0k0dHJdhmf37auCSWwJkuhMbUCXWaSLnXxZ9OGq90qzistWmzD-305QGvF5_Eurkf873E2B0z_3i7OyrGgvdxyd246fLQqnM7-oCzej2XjD8BJh7eixcHhKQObVTGdTSmKLi91oDmrhqmgkK1ErBqfje3zSo0AjYQSA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
دمنوش واقعا سردرد را درمان می‌کند؟
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.56K · <a href="https://t.me/farsna/461812" target="_blank">📅 16:38 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461811">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1769cb0441.mp4?token=PSG0064ZLgj2CTNdQsbgtGbqM6ynyOb8bnWcsi01jgAJMFFcotFMcwldGVztMYnGalw8dGdMesb3AiPij4S3OMru3hP8iqaRdSsx6yCrK6CsG4UY9wnu4vPk7MradwFBfUy0hk4RKlZejAAz2MZNwETLT4FngTZBtwH3Ipu0peM3573LfJ8G-b4ogKmZ6mRQfctIOPzWfsd3p3nFRBndE_7eqwNuYJbU8JeTrxLgl7yiqFH-dZswKwx455hZsRcxcVirA0G-HnoVsV-nl3QfCLGykBfeJV-fsxXQTvN2BThsPc9wwTWwXE2JDiyJcskuwy4EGKZ5JnnkGtUdCLlpKCfmgSVSsIY6Wci2fUBSnkSDEAZfEtWkXkvAZyxVOZ3j-Xe3KWCpkvADfjFLrc46T2IFXnRTa3XZqZgJlx2RykCVMKYuT8d4vj4f8Df0MOvo9-A7roSsh67toHJq9e1d-4B1Yqhluz4to_CT3p0Nx5rGxwu7Hl1TIa4S9N9SqGyy4duBgNrzfTwSmQ6DVIK3ljTSqOZMHnjrvAIb0yvx9cWTYiRN_6H5YTyWsxmTj-NeaOfVb_zjvAK28_MO1TnACaitPtzafG14bUYPovrWzKIBd74xy9bbfHz9lM1lqz4Ftj9XeWIb-mT7SHBM7R4FVRivHYJsZ1EYFwO8459GN3k" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1769cb0441.mp4?token=PSG0064ZLgj2CTNdQsbgtGbqM6ynyOb8bnWcsi01jgAJMFFcotFMcwldGVztMYnGalw8dGdMesb3AiPij4S3OMru3hP8iqaRdSsx6yCrK6CsG4UY9wnu4vPk7MradwFBfUy0hk4RKlZejAAz2MZNwETLT4FngTZBtwH3Ipu0peM3573LfJ8G-b4ogKmZ6mRQfctIOPzWfsd3p3nFRBndE_7eqwNuYJbU8JeTrxLgl7yiqFH-dZswKwx455hZsRcxcVirA0G-HnoVsV-nl3QfCLGykBfeJV-fsxXQTvN2BThsPc9wwTWwXE2JDiyJcskuwy4EGKZ5JnnkGtUdCLlpKCfmgSVSsIY6Wci2fUBSnkSDEAZfEtWkXkvAZyxVOZ3j-Xe3KWCpkvADfjFLrc46T2IFXnRTa3XZqZgJlx2RykCVMKYuT8d4vj4f8Df0MOvo9-A7roSsh67toHJq9e1d-4B1Yqhluz4to_CT3p0Nx5rGxwu7Hl1TIa4S9N9SqGyy4duBgNrzfTwSmQ6DVIK3ljTSqOZMHnjrvAIb0yvx9cWTYiRN_6H5YTyWsxmTj-NeaOfVb_zjvAK28_MO1TnACaitPtzafG14bUYPovrWzKIBd74xy9bbfHz9lM1lqz4Ftj9XeWIb-mT7SHBM7R4FVRivHYJsZ1EYFwO8459GN3k" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔸
رکورد افزایش تولید هلدینگ خلیج‌فارس در سال وقوع دو جنگ تحمیلی
🔹
شرکت صنایع پتروشیمی خلیج فارس در سال وقوع ۲ جنگ تحمیلی توانست با وجود ۲ ماه توقف تولید به علت شرایط جنگی، تولید محصولات خود را نسبت به سال ۱۴۰۳ افزایش دهد و به ۲۷ میلیون و ۳۰۰ هزار تن برساند.</div>
<div class="tg-footer">👁️ 8.04K · <a href="https://t.me/farsna/461811" target="_blank">📅 16:37 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461810">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">گزارش ویدئویی از نشست خبری خانه سینما برای گرامیداشت هفته و روز سینما با حمایت شرکت بیمه دی
این نشست دیروز شنبه ۲۱ شهریور ماه در آمفی تئاتر خانه سینما با حضور اصحاب رسانه برگزار شد.</div>
<div class="tg-footer">👁️ 7.45K · <a href="https://t.me/farsna/461810" target="_blank">📅 16:36 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461809">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-footer">👁️ 7.31K · <a href="https://t.me/farsna/461809" target="_blank">📅 16:35 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461808">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9d3652bab1.mp4?token=l9_iy6fWTZyqepzhUcpMEM6HXMlIehZkLqbX23WhXBJoY6K5dzPO-zgZydrXEzyoujRLbetby-qkJhBM3Hz6OJOzXJn19s3McRSd2yGeTTjnKhUfCq2Eof6ljbQngVoiw9sgGuTKM1oBdmCVI5UQwWl6iek2v0ZOuWqeHj4JB63jkZuCJvtY_4Jx_LlMzvZfLwCiT8nf7bsEVDgC4RZS-L7CLjKd2QnqCRAIkE7f5vl352M72mDYlST0BOxuH7oPp_mBsr0a4wpisPYKYQph4_-dbx4E3stu3Wy4tCgjt2n4uuObdbH_x3q_APXegqWx9noqlXzMs3f0ZGZ-1D_xKluZcCMBIPtUfF7sWdriKpd2GreLUTPWvIKbRPJexaxJszUoS4wsPIGiaKvOf59mYovC4UXPS398439M-OJJvHlfaycjriWB1rRTBU45M2zFmNO9oKJKhrQb7lQlnWjqt06zlEaw3TdXZbnaED_gX98JOx9Bd1pkoT8wpx2wijh8xpIlMQfkZpTkRdn-ixOfodTbQGQY5cUQFU8VLA8CnwVnwFiBeE7yUpArJe4GZPW4IX_rfMJi3ixrKAwx7oT9itF99SgsbytZHli478l6lQte19O4WMMkn6BLFfWIWpBxhELMA7tyooC5K9i2QBs8LnO7X0IaIV5wgRHCYFr183o" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9d3652bab1.mp4?token=l9_iy6fWTZyqepzhUcpMEM6HXMlIehZkLqbX23WhXBJoY6K5dzPO-zgZydrXEzyoujRLbetby-qkJhBM3Hz6OJOzXJn19s3McRSd2yGeTTjnKhUfCq2Eof6ljbQngVoiw9sgGuTKM1oBdmCVI5UQwWl6iek2v0ZOuWqeHj4JB63jkZuCJvtY_4Jx_LlMzvZfLwCiT8nf7bsEVDgC4RZS-L7CLjKd2QnqCRAIkE7f5vl352M72mDYlST0BOxuH7oPp_mBsr0a4wpisPYKYQph4_-dbx4E3stu3Wy4tCgjt2n4uuObdbH_x3q_APXegqWx9noqlXzMs3f0ZGZ-1D_xKluZcCMBIPtUfF7sWdriKpd2GreLUTPWvIKbRPJexaxJszUoS4wsPIGiaKvOf59mYovC4UXPS398439M-OJJvHlfaycjriWB1rRTBU45M2zFmNO9oKJKhrQb7lQlnWjqt06zlEaw3TdXZbnaED_gX98JOx9Bd1pkoT8wpx2wijh8xpIlMQfkZpTkRdn-ixOfodTbQGQY5cUQFU8VLA8CnwVnwFiBeE7yUpArJe4GZPW4IX_rfMJi3ixrKAwx7oT9itF99SgsbytZHli478l6lQte19O4WMMkn6BLFfWIWpBxhELMA7tyooC5K9i2QBs8LnO7X0IaIV5wgRHCYFr183o" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حجت‌الاسلام پناهیان: وقتی کسی را می‌بینم که با افتخار پرچم ایران را دست گرفته، آدم از شدت محبت دوست دارد گریه کند
🔹
این تجمعات شبانه فضای اجتماعی دیگری ساخته؛ آدم خوبی‌های مردم و محبت به دین، انقلاب و ایران را می‌بیند.
@Farsna</div>
<div class="tg-footer">👁️ 7.63K · <a href="https://t.me/farsna/461808" target="_blank">📅 16:32 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461807">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ca59819cb8.mp4?token=INwqJjOUonq6NKV6eYbg2lGLPjNeD6HfXjAtOjY4BKF7mJmeX3T3FfCzHV_ICAXKt-SIHOsN1Mj-_T9fmXTigjPFhtd7efuU2i6TtbHJ2UTQuPOIjKAjYOxXJm6Vtgz-4hCC1ae7ki4WwyCVvGnAU-681i-J2Kc2r7YG_9mfAorjQEwDOqdEjKNHa9p_FvuttW6rliAAvytYiieLicw-sOL9mH32hoiOyzpzKlJzTIvuK4kOfytrDMa0ZoyTCfhoA7SwaAbBDVgD5WNUo5ikeLdCezI_AP2MgV08jr8ssfSemwWPME33to9THzINoyzqJ0IlEIsQTIMzX2ltLdXTUw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ca59819cb8.mp4?token=INwqJjOUonq6NKV6eYbg2lGLPjNeD6HfXjAtOjY4BKF7mJmeX3T3FfCzHV_ICAXKt-SIHOsN1Mj-_T9fmXTigjPFhtd7efuU2i6TtbHJ2UTQuPOIjKAjYOxXJm6Vtgz-4hCC1ae7ki4WwyCVvGnAU-681i-J2Kc2r7YG_9mfAorjQEwDOqdEjKNHa9p_FvuttW6rliAAvytYiieLicw-sOL9mH32hoiOyzpzKlJzTIvuK4kOfytrDMa0ZoyTCfhoA7SwaAbBDVgD5WNUo5ikeLdCezI_AP2MgV08jr8ssfSemwWPME33to9THzINoyzqJ0IlEIsQTIMzX2ltLdXTUw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
وام بانک‌ها کجا رفته؟
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.12K · <a href="https://t.me/farsna/461807" target="_blank">📅 16:29 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461806">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromسیاسی خبرگزاری فارس</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0268d7e623.mp4?token=qu1zEalR8v74cuKjWHI5IKHNjXHIh1E5MegdMt8OWLDmXRkCYeW1CBPzZ32x2VGcp4gL7WjPDrSIYGuSE23Q6y4pqnZk6JX0EELIgmoKVMoFrfugIbpaZTwajKA7oHTVrF-33z-q7atNbMDPj9Y3naH5N8BBWMX5twAQ5ctAfo0Xhti_Xxg8du5qdakjs89Tfeudi6YYGrt6tMa5Mm7NFcxeyTD3dk9TpIDY2GNRwzEWVHkYMmsTbSzQiYkLnvRLeWdEVCFRTy9i_Fx3NnQm9Bmpla3RnUvsbFLG0o1IVvmTcJUh9HZPN9GLFlk3aPJ-sM7SOtbKseAYV7nIHbXK4UuHl2dh8aT-7ERRH3fn4LA-ld5_aL31uASVH0GfUZZ-lcWPlVwY1vGuFwubs5DFEKZ2z-XIOKebLtTIZS0vcnWep3vxn9cicxarPpFEhcMxQX9Y-U7bNCq-OXihUzFnTq5ACHjwhouhuO8uA0gEGJJy8KC4PhcVKucYGOaclOCOWMFlXnu4qY785x3WfbNBJ3AhQ2JLtU-sMMBy4BSEWbc9pW2YxONmcNKjcoL9UaG2TYgg5SSoENzhUzZp59DPbuhEhZsVn12qFuEVkdPAQBvr7qfwUDDaXN2Jnhu1h3oD_e7Xcn759PxkzG6ZFGSkN0DSjH3uBDqtoJ6Mg-pzCR4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0268d7e623.mp4?token=qu1zEalR8v74cuKjWHI5IKHNjXHIh1E5MegdMt8OWLDmXRkCYeW1CBPzZ32x2VGcp4gL7WjPDrSIYGuSE23Q6y4pqnZk6JX0EELIgmoKVMoFrfugIbpaZTwajKA7oHTVrF-33z-q7atNbMDPj9Y3naH5N8BBWMX5twAQ5ctAfo0Xhti_Xxg8du5qdakjs89Tfeudi6YYGrt6tMa5Mm7NFcxeyTD3dk9TpIDY2GNRwzEWVHkYMmsTbSzQiYkLnvRLeWdEVCFRTy9i_Fx3NnQm9Bmpla3RnUvsbFLG0o1IVvmTcJUh9HZPN9GLFlk3aPJ-sM7SOtbKseAYV7nIHbXK4UuHl2dh8aT-7ERRH3fn4LA-ld5_aL31uASVH0GfUZZ-lcWPlVwY1vGuFwubs5DFEKZ2z-XIOKebLtTIZS0vcnWep3vxn9cicxarPpFEhcMxQX9Y-U7bNCq-OXihUzFnTq5ACHjwhouhuO8uA0gEGJJy8KC4PhcVKucYGOaclOCOWMFlXnu4qY785x3WfbNBJ3AhQ2JLtU-sMMBy4BSEWbc9pW2YxONmcNKjcoL9UaG2TYgg5SSoENzhUzZp59DPbuhEhZsVn12qFuEVkdPAQBvr7qfwUDDaXN2Jnhu1h3oD_e7Xcn759PxkzG6ZFGSkN0DSjH3uBDqtoJ6Mg-pzCR4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
راهکار سفیر سابق ایران در مالزی برای دور زدن محاصرۀ اقتصادی
🔹
زاهدی، سفیر سابق ایران در مالزی: محاصرۀ اقتصادی ایران در غرب،  «پروپاگاندا و هیاهویی بزرگ» است و اجرای چنین طرحی عملاً امکان‌پذیر نیست؛ چراکه کشورهایی مانند چین و روسیه با آن همراهی نمی‌کنند.
🔹
دولت باید با استفاده از مسیرهای جایگزین، به‌ویژه فعال‌کردن ظرفیت سفارتخانه‌ها، تأمین کالاهای اساسی و دورزدن تحریم‌ها را دنبال کند؛ حتی اگر این مسیر هزینه بیشتری داشته باشد.
@Farspolitics
-
Link</div>
<div class="tg-footer">👁️ 7.03K · <a href="https://t.me/farsna/461806" target="_blank">📅 16:26 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461805">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">آموزش و سازماندهی ۱۰۰۰ گردان جان‌فدا آغاز می‌شود
🔹
اطلاعیهٔ شماره یک قرارگاه مردمی جان فدای ایران: پس‌از شکل‌گیری ظرفیت عظیم پویش جان‌فدا که تحسین دوست و تحیر دشمن را رقم زد و با توجه به استقبال بی نظیر و پیگیری مدام مردم برای قرارگرفتن در کنار نیروهای مسلح برای دفاع از دین و میهن هماهنگی‌های لازم با نیروهای مسلح کشور انجام شد و مقدمات مورد نیاز برای آموزش و سازماندهی ۱۰۰۰ گردان مقاومت ملی جان‌فدا فراهم گردید.
🔹
در همین راستا از همهٔ علاقه‌مندان دعوت می‌شود در روز سه‌شنبه ۲۴ شهریور از ساعت ۱۷ با مراجعه به سامانهٔ
janfadaa.ir
یا ارسال عدد ۱ به سرشمارهٔ ۳۰۰۰۱۱۵۵ در دوره‌های آموزش نظامی و امدادی جان‌فدا ثبت‌نام کنند و در قالب گردان‌های مردمی جان‌فدا سازماندهی شوند.
🔹
فعالیت‌ها و اقدامات جان‌فدایان برای ایران آینده به‌زودی در سایر حوزه‌های مورد نیاز دفاع از کشور اعلام می گردد.
@Farsna</div>
<div class="tg-footer">👁️ 7.47K · <a href="https://t.me/farsna/461805" target="_blank">📅 16:20 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461804">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3c6383cf15.mp4?token=fIsZANHuaOSXiX2L1z6lvXXF-HxR7xUQ33pmr6dt3eI6lbet7vk4VEX3TBdZ4OTjIlyqH-0uSztLPDYRUiXOKs2yl7E94y2FMGKd2In1RMJOwGmyOAUK3vY1mUoZZXPcQDIz-55bUbjfQsUFD1v-tn7NREoyjaBzDwyTXwobHbNZjPGAkc-Y5nSNXo1wrHC8HDw1w54BYXFSXJ1VIirz4zh5rQtc9M8vA6dO7Z0J1piTx5o5BvZrPhRffWn0VxQ0xFVy9cF2y-e3Rs_3UdXF4voD3ElPq-P892_cpW3aqR96ZLhFnjIX3n67OkIbn5JFqJLmdWy9_5MN8oljvq0O3w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3c6383cf15.mp4?token=fIsZANHuaOSXiX2L1z6lvXXF-HxR7xUQ33pmr6dt3eI6lbet7vk4VEX3TBdZ4OTjIlyqH-0uSztLPDYRUiXOKs2yl7E94y2FMGKd2In1RMJOwGmyOAUK3vY1mUoZZXPcQDIz-55bUbjfQsUFD1v-tn7NREoyjaBzDwyTXwobHbNZjPGAkc-Y5nSNXo1wrHC8HDw1w54BYXFSXJ1VIirz4zh5rQtc9M8vA6dO7Z0J1piTx5o5BvZrPhRffWn0VxQ0xFVy9cF2y-e3Rs_3UdXF4voD3ElPq-P892_cpW3aqR96ZLhFnjIX3n67OkIbn5JFqJLmdWy9_5MN8oljvq0O3w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
یمن چه بلایی بر سر پیمان مکه آورد؟
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.53K · <a href="https://t.me/farsna/461804" target="_blank">📅 16:15 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461803">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dfd4f2aa47.mp4?token=Yrh3cvlQnPsSNq4owO81ObQiOESr_4whTV-L08HgIuReI-MnPUWTYlZnFrNT6YGhUQ2orYSAbAG2_TB_hQcuDl63IWrFEKRDGMs6oKTJpp0N5t4yKSYZAOFCEhf1n3TNb8Ds8fLFvHGF8Ba3NWwaCXxoP_jjX0IkUK3kT1i649Iqp2r-ERRgW8w9o-nkl3Fcj28xbNeXGK18SAjqRi-pfGjzWyF7r28hAXSiWS_RiRDkK7MlULhu3uDyn0rzRcBdDK8LjpWTK3g3jL3JQZqgmOdL6QMFGFYLR7Hf9R5PlU7WuOUdJzai5_oUrgTn_AqTIizT_jZhPRp8IQpEKdZMhw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dfd4f2aa47.mp4?token=Yrh3cvlQnPsSNq4owO81ObQiOESr_4whTV-L08HgIuReI-MnPUWTYlZnFrNT6YGhUQ2orYSAbAG2_TB_hQcuDl63IWrFEKRDGMs6oKTJpp0N5t4yKSYZAOFCEhf1n3TNb8Ds8fLFvHGF8Ba3NWwaCXxoP_jjX0IkUK3kT1i649Iqp2r-ERRgW8w9o-nkl3Fcj28xbNeXGK18SAjqRi-pfGjzWyF7r28hAXSiWS_RiRDkK7MlULhu3uDyn0rzRcBdDK8LjpWTK3g3jL3JQZqgmOdL6QMFGFYLR7Hf9R5PlU7WuOUdJzai5_oUrgTn_AqTIizT_jZhPRp8IQpEKdZMhw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پزشکیان: گفت‌وگوهای سازنده با بانک توسعۀ بریکس داشتیم
🔹
چشم‌انداز بسیار خوبی جهت سرمایه‌گذاری، تبادلات مالی و ارتباطات اقتصادی شکل می‌گیرد.  @Farsna</div>
<div class="tg-footer">👁️ 6.86K · <a href="https://t.me/farsna/461803" target="_blank">📅 16:13 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461802">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">سرپرست وزارت دفاع: اگر جنگ دیگری شکل بگیرد ایران از نظر فناورانه بسیار قدرتمندتر و  پیشرفته‌تر عمل خواهد کرد
🔹
سردار ابن‌الرضا: با اطمینان بسیار بالایی می‌گویم اگر امروز جنگ دیگری شکل بگیرد، جمهوری اسلامی ایران از نظر فناورانه بسیار قدرتمند تر و  پیشرفته‌تر…</div>
<div class="tg-footer">👁️ 6.9K · <a href="https://t.me/farsna/461802" target="_blank">📅 16:11 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461801">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a2e69e07ee.mp4?token=FnMiFW1oAN4YCFGjtaYg59K4jR3N6c6L9aTZJFi5aeqEfUVmK54uu-N_heGPonGR4opcyjW7jtnD0lD7laBv68OkcTovpE5z0_9UR7piHnCDAcH7wSEQURXneh0uRqLzU46sxWDCOfGtWHT3svicdC1NcE1bFq8w-iBPbyf96Bg4H0-fqp72yASQFvLaeHZtx-rtyQfUkXwNoquBWH1t0F6qQ7nF9R2YVPOGiCNMOvO-ze3wh3t0dPCpcCs2pPrNBj_VjIdJr9WLkg51v4cEmgHEpfvo7dMQvdIVibqGPGFuiuKWdVoGF_xbOHZ0WXgidUNQez992rPlbC_Dmc4ynQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a2e69e07ee.mp4?token=FnMiFW1oAN4YCFGjtaYg59K4jR3N6c6L9aTZJFi5aeqEfUVmK54uu-N_heGPonGR4opcyjW7jtnD0lD7laBv68OkcTovpE5z0_9UR7piHnCDAcH7wSEQURXneh0uRqLzU46sxWDCOfGtWHT3svicdC1NcE1bFq8w-iBPbyf96Bg4H0-fqp72yASQFvLaeHZtx-rtyQfUkXwNoquBWH1t0F6qQ7nF9R2YVPOGiCNMOvO-ze3wh3t0dPCpcCs2pPrNBj_VjIdJr9WLkg51v4cEmgHEpfvo7dMQvdIVibqGPGFuiuKWdVoGF_xbOHZ0WXgidUNQez992rPlbC_Dmc4ynQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پزشکیان: حمله به تاسیسات هسته‌ای و زیرساخت‌های ایران در بیانیۀ نشست بریکس محکوم شد
🔹
در بیانیۀ بریکس تجارت با ارزهای ملی یکی از عناوینی بود که تاکید شد.  @Farsna</div>
<div class="tg-footer">👁️ 6.75K · <a href="https://t.me/farsna/461801" target="_blank">📅 16:08 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461800">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3e9b2c37b8.mp4?token=twgAb1tb71_-gcYiHGusE6M7ssQ-Z-3GG5bCDPtrfd6EepNAHvBwhCk74SAHBVtagl6H52WEW1hzjSUBAJUw13GvIzQ4egj233FJedmS3TUCW0M9JO9JEXLrppejX8xZDFXgljouno0FrTAb4mEWWIO4aFSMxFfJlujyG_ilWe_VzsMeVmshTu74JdxQ2YVTFL52apfUePMrGOUGVBz0Y_p9aUx7PNj4zvvoh5IY4FDEp9E0sxSpzNNgNwi6UNs13RZ5piRlRLwCalw9OLQ5JaPi2RfKyFyHWqVlc5NPaY9kUJVm4A-R8frr2B52n30soNnLPR5OMFjpbHjn0fbtvA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3e9b2c37b8.mp4?token=twgAb1tb71_-gcYiHGusE6M7ssQ-Z-3GG5bCDPtrfd6EepNAHvBwhCk74SAHBVtagl6H52WEW1hzjSUBAJUw13GvIzQ4egj233FJedmS3TUCW0M9JO9JEXLrppejX8xZDFXgljouno0FrTAb4mEWWIO4aFSMxFfJlujyG_ilWe_VzsMeVmshTu74JdxQ2YVTFL52apfUePMrGOUGVBz0Y_p9aUx7PNj4zvvoh5IY4FDEp9E0sxSpzNNgNwi6UNs13RZ5piRlRLwCalw9OLQ5JaPi2RfKyFyHWqVlc5NPaY9kUJVm4A-R8frr2B52n30soNnLPR5OMFjpbHjn0fbtvA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مدیر سامانۀ هوشمند سوخت: هر راننده فقط می‌توانند ۱۸۰ لیتر بنزین در کارت سوخت خود ذخیره کند.  @Farsna</div>
<div class="tg-footer">👁️ 6.89K · <a href="https://t.me/farsna/461800" target="_blank">📅 16:07 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461799">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hnDqYl9a4Vw6XS2QTSo7Biwv2-WvRsUrFqbDbSA8hrA-26MRVE6Afmx9UTD69GynukLz9qEfNtRa1NbjyvNeR0UJXYroklINDAdDU-XtZv2RhRCycia8z7hOpaGMnsAmB2tqUmJmjItsK6I46u_wNQaApF99SZgPf7kVmZOdgV12dAXZPWdEOFCILto3rU_q-r5ZPrCZ5iH4vvKYV9IpmlHtEW017PwkG8ac40cXZihNHpiA3GVbYFYIGX97jZFfZK-JKhS01A9AguGlDeZFwvrkF5Uazxp385GfjFwzbPWcouyWYkTUtL5FvIirEKAtufBBAUi3ipFpb2pshVRc9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سرپرست وزارت دفاع: اگر جنگ دیگری شکل بگیرد ایران از نظر فناورانه بسیار قدرتمندتر و  پیشرفته‌تر عمل خواهد کرد
🔹
سردار ابن‌الرضا: با اطمینان بسیار بالایی می‌گویم اگر امروز جنگ دیگری شکل بگیرد، جمهوری اسلامی ایران از نظر فناورانه بسیار قدرتمند تر و  پیشرفته‌تر از جنگ‌های قبلی عمل خواهد کرد.
🔹
کسانی که تلاش می‌کنند استمرار فعالیت های فناورانه و خطوط تولید و کارخانه‌های تسلیحاتی کشور را صرفاً یک روایت یا تیتر  رسانه‌ای جلوه دهند در میدان به خوبی توان نیروهای مسلح ما را  دیدند انچه بعضا به نمایش گذاشته می شود بخش کوچک از توانمندی واقعی و ظرفیت‌های موجود در صنعت دفاعی کشور است و این مسیر همچنان با قدرت ادامه دارد.
🔹
امروز ایران قوی‌تر ، متحد تر و بیدارتر از هر دورۀ تاریخی خودش است؛ توانمندی‌های دفاعی و فناورانه کشورهای نیز متناسب با تجربه‌ها و آموخته‌های حاصل از میدان، مسیر پیشرفت و ارتقا را طی کرده است.
🔹
آمادگی کامل برای مقابله با تهدیدات وجود دارد و این آمادگی کاملاً از جنس توانمندی‌ها و راهبردهای مستقل خودمان است؛ جمهوری اسلامی ایران برای تأمین امنیت و دفاع از منافع خود، متکی به اراده، توانمندی و ظرفیت‌های بومی خود است.
@Farsna</div>
<div class="tg-footer">👁️ 7.4K · <a href="https://t.me/farsna/461799" target="_blank">📅 16:04 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461792">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ga8Y51pBwrA9WQNNYraGLXwmmgPM35VIOx1LzP1tmcj9Oxnl--s7U_nSV-Mbauf3VvqFCYUVe7M1svJOjBB_zolTT93DXZGzUvg9C0-dCHMv7ROLZk2P-JKyoWHvdcN2JAGeoC3fzgaLlH6VKBQJPgHOV7VRSGzzBJwlkypPMilfj19v6HU8ulfvmveScLxTzBWD0cbUIbwb9wwOsMBDXb_lklvme9jGu9RgQT9aDsHQGJ6TQphPKKj8STrl9S9ks6AQIsAy8ekieKPOZhq-W9QtVDpybR1V69CW0oXmzvC-vI-WM78ahIwHR3qA8qEXIrAAoH5s2-5LPNKn_3xduw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vhW9a-3wjttNOUf92d57hs5s86FypwQOgLIn1Z46G0TcPGry3KViWncmR6gsBleVeIW99X_Bxy1xKd4hy4k3wpymiqL_Q3W_Q3sv_tgS8IlibaRymT_HWCQ7uVbebieZNN9F3uWsjX6OHrCl1NytSpG5l2ViLlwAundswWevhPzOVn6yhNr9XRe6WHPQtYWxepvsTjCzfUpPXL40HvRa6_oylWIc9vYbOhzWeREj1I5bdkzJpT0AhTSSTKyW2punY9S5WfVLyHjffFZT9ZW9njHsISgXIpCtyj3FI84tmBsthmlx0N4v9VMotwlz6VahV060RXATN0ecDHHq9VCfuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eQdbi7i55gkiOyoC6am4ekwNm6AY7IYMN-dnshO9qwtVe5JtHq5x9PosOK-I2BoF9EQGhAf6qSxworYfHTB2GKlIOosjNjD5vIJXW1DnpwR_OkREYN_kPCwyXPz1QvIFUexJYcAHfn0NoTQ6LAEjK6lwqE5a1HSBqJlI6BI_D6MK-mholjP7aZwsiXcdMRSgvi2oZeUZmZMghP7iyKb21hRwe8gqZSmYmfvMOb-AzuHmcGMgKWhnw-4aPT9ZMpxROkvEj-rVkVBdZD3qEwn0Kzq6WdD0hEB0xg8-55Veq-YCDg58Y3Z_r9GYVKk5G-xmRdaTmgiBhlp3jVPqzP5opQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/g3gLoTD0LazPlS4dWxEqp4NpyVxHCXaElVP4oW7dtr1ZKf80XRGRnH7M56Ngls9HGVILa-d7s8rR31-MygofJKlLph_e_lUyeSi8dfXPs5bbRI2H28bq63UAFt_vhbN8Ko_bxeI1Et6WAruZQY71sw30a6kp1peP8IAaONm9tGgJo4x8UKnlRZ-3HAfJBkcjBG-yY4J7gdQFXOFPrGqa_Ix80lmEe90qvWYsURb846oAnU8R2GQ_J5IVfN0A1GuMi3iSNQDKhEj557GFgzX04d652OKQtKLWA7JtUMNuFNqJYkrZIhNwmFCnglB5fd8f8E4vtAzQvVeTbKcooYUDSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JRN56udsJy265w78BNZiZOuJavHdCz8Jg5gTyf3vVLesuCaHtmF0m6q3R7kYKL7rxnPdFa79jZvXIxKuoBTTXLIsTR1MB__3CeYnJoiuOCB1BQy1dTVipQax1eLWMpJaOTTXm4bhyA5KSEx8sr2xeCaS7BaLRvooFFHG7Hj57j0YW2sVVuCLcbgdQXHiCQnfPrWv3SXYh7B3aQT7MlVbnwDjclz4xkWwUzYeaYtsasLUehp_WL6GcKWxjMnQI4irhk_x9rujJLPjCHbYrj6Gy7I81u6tNi_21tYnhTJ8tlrPoSdeNSQEguny3iJ2Zt_J0N4-cdvPlMxWTxdpeGXz_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kWcBlNEckcxliRgYszOLNvm94xMHwV5oTnZwTRrYazrKLuxqp27C-YB-d2FP9fM3GfDTz9qd3Sgv-f22jc25SOC9iTroS7morTLEqIaiAsXqt-OG5Z4w-LkUICTaZjyxYqX6ByneUwS-qFBcibHtc5lLE6bUSdj0ESTmTUHQEzVU6cbzgE-7WzD8sdRvO4PlzOg0pJrhJLhug_JWDuf5TGin1tYOitUy8MSdBuQw4uGBEu3GMvADvIqGPjXCfnR7RXHuJ99ey7KezJ-NxFp15lGxFn_vPY7L2XmYvNgS5xYL57BrE-D2bHHMaU9tPwFHItCKm51VH9Jjorys_k96jg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/L-gToslejSu8fG0RLX4wXJoafUSisDqOIPc6FKOVmElrO-bNrYtHCuYtxZtMd_-rbiNE8EliXRdsIIFhopjEfRw4FMPHFbNA9FcGOE51YFannTiJZy-e9Lm9YyNgliqf4WyAA0RHf5ZWSviwFdSjgzz_T0xe6B6r9f2eYFExue5ujpK90pGok9aPL3C3UP1OX4M_gWo-DIawqk8-HdAqkvVWmRae330_rJuWAgXkEsH-Du1d88MuY3EOoxB_XjisK7y5CryF-Y_qaDODutaTUR_vB5W0vX02Hwv4ljXvEiUSdJxZhhKqbYgWY6BRgjFw96RImK8dEPrIeAqh5iJ4kQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
ضربۀ پلیس البرز به سوداگران شیشه‌ای
🔹
پلیس مبارزه با مواد مخدر استان البرز ۳۹۰ کیلوگرم شیشه را کشف کرد؛ در این عملیات ۳ قاچاقچی دستگیر و ۲ خودرو توقیف شد.
عکس:
نسترن کرمانی
@Farsna</div>
<div class="tg-footer">👁️ 6.86K · <a href="https://t.me/farsna/461792" target="_blank">📅 16:00 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461791">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a934d86157.mp4?token=Q0Dv2_DjMDrQdOYHHcqEn4V8z9OcTUaq6QGTwh4w3WoZj3jTUxSfSeegwzGSUnL7jhZfNi79_-PXP-P4Vpq095YTSVES55_ZP1laWyAITvH1iTJr9d_m9LNhWxqD44taLwRm0A7uVKD6uZksALW90NvcHVogye3cJvf9k3pNDi9XrC-WROA9GHob1Ipg9VFAhOeNMJc8CHs1Nwe_azDykLz8nOF4gdcxgS_LUIxvyxUTHDfb8pp1dOeWmBB4vQDdOCIeKSbC0Mki5xiEZ_fCFISnzxJNbGn-trzWlmCBs5q2rie8MBtxOMJFldXeETjtIIFJ416a8UWZHsuPevR1tw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a934d86157.mp4?token=Q0Dv2_DjMDrQdOYHHcqEn4V8z9OcTUaq6QGTwh4w3WoZj3jTUxSfSeegwzGSUnL7jhZfNi79_-PXP-P4Vpq095YTSVES55_ZP1laWyAITvH1iTJr9d_m9LNhWxqD44taLwRm0A7uVKD6uZksALW90NvcHVogye3cJvf9k3pNDi9XrC-WROA9GHob1Ipg9VFAhOeNMJc8CHs1Nwe_azDykLz8nOF4gdcxgS_LUIxvyxUTHDfb8pp1dOeWmBB4vQDdOCIeKSbC0Mki5xiEZ_fCFISnzxJNbGn-trzWlmCBs5q2rie8MBtxOMJFldXeETjtIIFJ416a8UWZHsuPevR1tw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پزشکیان: زیرساخت‌هایی که طی دهه‌ها برای توسعۀ ایران ساخته شده بود، در جنگ اخیر آسیب دید
🔹
این وقایع یادآور مسئولیت سنگین جامعۀ بین‌المللی در قبال حمایت از غیرنظامیان و جلوگیری از عادی‌سازی حمله به اهداف غیرنظامی است.
🔹
بریکس باید اطمینان دهد که هوش مصنوعی…</div>
<div class="tg-footer">👁️ 6.68K · <a href="https://t.me/farsna/461791" target="_blank">📅 15:58 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461790">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/91359b9ec1.mp4?token=fTM-WiGo1DliWP3gKC2RXcdECPpglu1p8AKvmAYKeGpSmy8_32AuiqxgqU12AkirChI8qOfPMrhSSLJWtSx-px2D_S2zddFslRLAVhq79DzgW4aNb25Kt-mgBL9ss1R_AzblxlCGoFTxElCuDX6xvXvp6RkPIhon4LWilNoX6kyoefBZwHA-42GhA-UZZNZdTHzst8qba2_YBdTTDjk-j_DKfVs8cKS6y6Q19deRIs6TEUG6p-5uev2hmAUvxS4XgJBCQCtAvHhgCVxRXwskGA73vlPSsq1qwi01Bw-dSiFX75R7Xng6SO_Aw2mYTQXQPsbhm3CuOvedBRAUQOynQQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/91359b9ec1.mp4?token=fTM-WiGo1DliWP3gKC2RXcdECPpglu1p8AKvmAYKeGpSmy8_32AuiqxgqU12AkirChI8qOfPMrhSSLJWtSx-px2D_S2zddFslRLAVhq79DzgW4aNb25Kt-mgBL9ss1R_AzblxlCGoFTxElCuDX6xvXvp6RkPIhon4LWilNoX6kyoefBZwHA-42GhA-UZZNZdTHzst8qba2_YBdTTDjk-j_DKfVs8cKS6y6Q19deRIs6TEUG6p-5uev2hmAUvxS4XgJBCQCtAvHhgCVxRXwskGA73vlPSsq1qwi01Bw-dSiFX75R7Xng6SO_Aw2mYTQXQPsbhm3CuOvedBRAUQOynQQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مدیر سامانۀ هوشمند سوخت: خودروهای نوشمارۀ بالای یک میلیارد تومان سهمیۀ ۱۵۰۰ و ۳۰۰۰ تومانی بنزین نمی‌گیرند!
🔸
این خودروها ماهانه ۱۱۰ لیتر بنزین ۱۰ هزار تومانی می‌گیرند. @Farsna</div>
<div class="tg-footer">👁️ 7.74K · <a href="https://t.me/farsna/461790" target="_blank">📅 15:57 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461789">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/643027f01a.mp4?token=j5y-alVxQa9O3rA7ey-C8xW9cF5SUwTuzQBzDb5HK-wpm7S9wj4sgYimL2TP6ZpjOtzFak3OdfZm1_Pa0HyZOJXV2Dg5qQ2mHlfjKEvr8aeejeKIkfDeapsdhTRlKAMGVS1f6AbBs_AzxwMXPF3NgvVKxgNAsVu2r2zRHib_2SdKC4DH6xbR8wDwiO9x5hztJIkldb1NnbFkeL4aAljy4IKTvnRMN4rIGiJhk3OavFnGFptgl12tG4PbYHvKpr4vxeFZzciTyLI2vax3MeTNak1aYuqh004JyYgj3Yzyd-EQGILpe7zSaVa5OGwqmzH_Ibd6I_J6pB0wzGTRufpSeQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/643027f01a.mp4?token=j5y-alVxQa9O3rA7ey-C8xW9cF5SUwTuzQBzDb5HK-wpm7S9wj4sgYimL2TP6ZpjOtzFak3OdfZm1_Pa0HyZOJXV2Dg5qQ2mHlfjKEvr8aeejeKIkfDeapsdhTRlKAMGVS1f6AbBs_AzxwMXPF3NgvVKxgNAsVu2r2zRHib_2SdKC4DH6xbR8wDwiO9x5hztJIkldb1NnbFkeL4aAljy4IKTvnRMN4rIGiJhk3OavFnGFptgl12tG4PbYHvKpr4vxeFZzciTyLI2vax3MeTNak1aYuqh004JyYgj3Yzyd-EQGILpe7zSaVa5OGwqmzH_Ibd6I_J6pB0wzGTRufpSeQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مدیر سامانۀ هوشمند سوخت: خودروهای نوشمارۀ بالای یک میلیارد تومان سهمیۀ ۱۵۰۰ و ۳۰۰۰ تومانی بنزین نمی‌گیرند!
🔸
این خودروها ماهانه ۱۱۰ لیتر بنزین ۱۰ هزار تومانی می‌گیرند.
@Farsna</div>
<div class="tg-footer">👁️ 8.98K · <a href="https://t.me/farsna/461789" target="_blank">📅 15:52 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461788">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/trzBB7mC8YCYA7cSSPeNnjKv4LvNjeQt65Isziuq6K4UXzyGUgjhTrEiJj6_tv__i0EklBBnEDuW4To31Vh_tunf4Zpg57Qt6i-GqXJarIAbLtc_Z1EcZIgxcA6AXMhMXO6pJ8cU1LI631hLdXt55R_Yy1j9SDxPasrUM-SfzD_4aPEB5qmvD7TFMAb6fec2YBjFzVxzv_IBMUXlQIOVuk2Z9q3-xE917L8JnSMi2Z0Z5g0QyjEQ2EK1FvqiashVTlMC1ZecKKdZnNdxHeyZO02jasCd_qLaHRiMpGpYn5Q8P50XexcAe7Ci1CP866vFzKCLT1iS2ZaC-DfAs-zx-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امارات از تکذیب هشدارش به نتانیاهو خودداری کرد
🔹
روزنامه عبری یدیعوت آحارونوت گزارش داد که از امارات خواسته شده بود اطلاعات مربوط به هشدار محمد بن زاید، رئیس امارات به بنیامین نتانیاهو، نخست‌وزیر رژیم اشغالگر درباره عملیاتی که شهید یحیی السنوار، رئیس جنبش حماس در نوار غزه برای پیش از ۷ اکتبر ۲۰۲۳ طراحی کرده بود را تکذیب کند؛ اما ابوظبی از این تکذیبیه خودداری کرد.
🔹
این روزنامه عنوان داشت که امارات تنها به پاسخ‌های دیپلماتیک بسنده کرد تا در اختلافات داخلی اسرائیل درگیر نشود و تأکید کرد که «اگر امارات واقعاً به نتانیاهو هشدار نداده بود، قطعاً این موضوع را تکذیب می‌کرد.»
@FarsNewsInt
-
Link</div>
<div class="tg-footer">👁️ 8.97K · <a href="https://t.me/farsna/461788" target="_blank">📅 15:39 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461787">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/23cc25a7ce.mp4?token=VRR4_q0ffnQPWPjGBBeG4eHgEaWKTgvJXzaopt-_lTJSxzZUzvh1-4rMYdhewu6RrR4Lbs41nkMPwRggZTqCjtOBG3loDatnUAwg8VMtKhjUJS-j3JFq3kisDyW86ojcFIRUdnRm3wv938Ko8R0G_-ZuxVvPaFFOZDLFVtFP6Lc7ToO85P2oX-7HfVme4f0McDlGQfIVYwNhea_3Cf_m-qxYhCv9cbcjFmsdw_F124kY4qN9R9nQwWzfYu56JVlNziZZjpZCqXBrKTt5x_qY-kkXIWjmyhJXkIOahtMY0tHM34xSkl07H-dyGKKusBBdU22jlQVo42vVgfulejeeqw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/23cc25a7ce.mp4?token=VRR4_q0ffnQPWPjGBBeG4eHgEaWKTgvJXzaopt-_lTJSxzZUzvh1-4rMYdhewu6RrR4Lbs41nkMPwRggZTqCjtOBG3loDatnUAwg8VMtKhjUJS-j3JFq3kisDyW86ojcFIRUdnRm3wv938Ko8R0G_-ZuxVvPaFFOZDLFVtFP6Lc7ToO85P2oX-7HfVme4f0McDlGQfIVYwNhea_3Cf_m-qxYhCv9cbcjFmsdw_F124kY4qN9R9nQwWzfYu56JVlNziZZjpZCqXBrKTt5x_qY-kkXIWjmyhJXkIOahtMY0tHM34xSkl07H-dyGKKusBBdU22jlQVo42vVgfulejeeqw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ژاپن دست دوم را هم از ایران برد
🇮🇷
۲۱ | ۲۴
🇯🇵
۲۵ | ۲۶  @Farsna</div>
<div class="tg-footer">👁️ 8.73K · <a href="https://t.me/farsna/461787" target="_blank">📅 15:35 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461786">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/809653adc8.mp4?token=hi82Ghm8AfsA5tmdXiTeVNbNdPkVd-09LW3Cev7VSJnE_Vr3lEgEq7XvH9wPCiAnioySNfK2K8xxnQUvQh0PRQyL_Wov5cEPB4Psc8GbzUlE-vFuED-VeO8v9qhK05vJlk4crNmfjNncgZzYH5k7qip0rNGrpufawP-aKFMpRbPhulNAuitThV-6RDDsH5TdINGc73C9Ro3RWuTQ_vl_ejcn7_bPFjHzkhnJ51cxwYJeoHNaHeL5KneqA2wOphUxQh5cqVc3atFgRyaGKI29O7LJUEWYixQZfyJhoaPnTvf53oj7vZgezc9ewluTofCk9FEmemz24mBshCDYheC5fw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/809653adc8.mp4?token=hi82Ghm8AfsA5tmdXiTeVNbNdPkVd-09LW3Cev7VSJnE_Vr3lEgEq7XvH9wPCiAnioySNfK2K8xxnQUvQh0PRQyL_Wov5cEPB4Psc8GbzUlE-vFuED-VeO8v9qhK05vJlk4crNmfjNncgZzYH5k7qip0rNGrpufawP-aKFMpRbPhulNAuitThV-6RDDsH5TdINGc73C9Ro3RWuTQ_vl_ejcn7_bPFjHzkhnJ51cxwYJeoHNaHeL5KneqA2wOphUxQh5cqVc3atFgRyaGKI29O7LJUEWYixQZfyJhoaPnTvf53oj7vZgezc9ewluTofCk9FEmemz24mBshCDYheC5fw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اصابت پرتابه به کشتی ایرانی در تنگهٔ هرمز
🔹
فرماندار قشم: یک کشتی تجاری ایرانی ساعت ۵ امروز در حوالی جزیرهٔ هنگام و در محدودهٔ تنگهٔ هرمز هدف اصابت یک پرتابهٔ ناشناس قرار گرفت که تاکنون یک شهید و ۳ مجروح برجای گذاشته است.
🔹
هنوز نوع پرتابه‌ای که به این کشتی…</div>
<div class="tg-footer">👁️ 9.71K · <a href="https://t.me/farsna/461786" target="_blank">📅 15:26 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461785">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d825e7a2dc.mp4?token=rqp20yZBwemS2LUGZqEK-p8cD-Dnq6_g4_svCTLGkmRksOQ-fyEJxP5IQa7C-S6w6K-gJhf9gOXUk8gr-RAwDzrfZeRwnMA23nxIU3LixAZEKQlF8X5m09AOSej9T1Z4jBNI7ISVJwyhPTfFF6wCd42-fkh5PSmkWjWiUAAlmWedqHAl7omSgqnBd4Xtxyc2Y-xg0crgacG8om6KEN1xWYt8VTWoyQqk_TDvtA5AnAVIoZNSrF_rLPK0feFsrE9O7eW9-nr0SaX7duFHeI3RFMjCPbOd-6PTJMJ8a6Ajdlxb29ZUBSepVnAN5jcThi--zvUHGHX6uPYGtGaFd630uqKBo1Fi-aIBA2XzhaIe5IGvZMBQJ3V31ln7aQ7wDwGXQB6yRyWbMwAazcUCnW9Cp9hsVrgH8bmqpMmeoV2m0ngUn-CjR-GCEG4bSf91zOk-jwKf8O2KJtIt5_wZewZjVx2-msvBAjGmG7u5OoutcYYSffyym_A5Hh4n_H3u_c_u2RgkiG15ifjWQLB7hnsVMcHNWNkEQ_3VM0P9D_v06FM9SqRuwOkRXonh39mOYudBplNhV2g1AWqnvG7n1ENVfiLWyPJElGycFHIGOoVxulZ9x1y6oPuEtu_InmVG5fCfzasQJlqdAHJMN4p_LDXScbAz4Gt0Ov_ghTKVxDsCkkg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d825e7a2dc.mp4?token=rqp20yZBwemS2LUGZqEK-p8cD-Dnq6_g4_svCTLGkmRksOQ-fyEJxP5IQa7C-S6w6K-gJhf9gOXUk8gr-RAwDzrfZeRwnMA23nxIU3LixAZEKQlF8X5m09AOSej9T1Z4jBNI7ISVJwyhPTfFF6wCd42-fkh5PSmkWjWiUAAlmWedqHAl7omSgqnBd4Xtxyc2Y-xg0crgacG8om6KEN1xWYt8VTWoyQqk_TDvtA5AnAVIoZNSrF_rLPK0feFsrE9O7eW9-nr0SaX7duFHeI3RFMjCPbOd-6PTJMJ8a6Ajdlxb29ZUBSepVnAN5jcThi--zvUHGHX6uPYGtGaFd630uqKBo1Fi-aIBA2XzhaIe5IGvZMBQJ3V31ln7aQ7wDwGXQB6yRyWbMwAazcUCnW9Cp9hsVrgH8bmqpMmeoV2m0ngUn-CjR-GCEG4bSf91zOk-jwKf8O2KJtIt5_wZewZjVx2-msvBAjGmG7u5OoutcYYSffyym_A5Hh4n_H3u_c_u2RgkiG15ifjWQLB7hnsVMcHNWNkEQ_3VM0P9D_v06FM9SqRuwOkRXonh39mOYudBplNhV2g1AWqnvG7n1ENVfiLWyPJElGycFHIGOoVxulZ9x1y6oPuEtu_InmVG5fCfzasQJlqdAHJMN4p_LDXScbAz4Gt0Ov_ghTKVxDsCkkg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
لحظاتی زیبا از بازگشت صیادان مفقودشدهٔ بندرلنگه‌ای به آغوش خانواده‌هایشان  @Farsna - Link</div>
<div class="tg-footer">👁️ 9.56K · <a href="https://t.me/farsna/461785" target="_blank">📅 15:17 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461784">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/69ea1595f8.mp4?token=YSsVPWZJ2n2q3MKM7IU7UfWzlMxhaynzdc4TozcgMGxqnog8g6P-W0JCS05qbI82oWc-C8UDCjDZm-6seGzBjxfSyM2VGuGXu3rII_0C2p33HQkBnLDRnPY0yDKBukCX6YD6qP3_dRr0OSszUGk7Txbg4Gy7feewhkyVvwuJaed29tzhGQ9HoHQE3KReT-7AUO_A5P0Bw9_90zfMnS_CxO_sds9CznK2eLT9aqW4VZXmZLaC6zLOxBHb2d0V2PFAp2PRFawsd02Vpi8zO4vqEXnkNMDxdHxEgVkjcR-43fzdzwQO9pLg7CTtRm-TIhM3lP4QDBwVuz4f5gS-iTWECg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/69ea1595f8.mp4?token=YSsVPWZJ2n2q3MKM7IU7UfWzlMxhaynzdc4TozcgMGxqnog8g6P-W0JCS05qbI82oWc-C8UDCjDZm-6seGzBjxfSyM2VGuGXu3rII_0C2p33HQkBnLDRnPY0yDKBukCX6YD6qP3_dRr0OSszUGk7Txbg4Gy7feewhkyVvwuJaed29tzhGQ9HoHQE3KReT-7AUO_A5P0Bw9_90zfMnS_CxO_sds9CznK2eLT9aqW4VZXmZLaC6zLOxBHb2d0V2PFAp2PRFawsd02Vpi8zO4vqEXnkNMDxdHxEgVkjcR-43fzdzwQO9pLg7CTtRm-TIhM3lP4QDBwVuz4f5gS-iTWECg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اولین جلسهٔ رسیدگی به دادخواهی مردم برای جنایات جنگ ۱۲ روزه
برگزار شد
@Farsna</div>
<div class="tg-footer">👁️ 8.83K · <a href="https://t.me/farsna/461784" target="_blank">📅 15:14 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461783">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3a3d048989.mp4?token=q3sE4SpU_ZPfxesnbglyh4b4Rb3_x6AfK7-qawbQPCsuet6J0PwgA77q1LGuYhJPtQGm2CGe5-En8DlCs23qXFNSao3b1j_RhEWijKbzBf5wY7QpcS3WylLMrFFFdc3Fs2CnOXkh848faPQegNDtCo9tFslAXSpupJ-MshJMEnxkzOYwsDbKgnU62Ysv2RFGaTBwFKqCCXDMMlJbsYdB7QWz-G8A6slCJ95ZPkks1ApFjtJFnc3afj3XaoTUtM2TnoX8wB3TEHLkYybRPXGwsi66XYKbZnYNPfnNWxm6AFjeUfaaJdBcxvddcya3twhNGUNl7X0fM7I4KA5O-coRNQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3a3d048989.mp4?token=q3sE4SpU_ZPfxesnbglyh4b4Rb3_x6AfK7-qawbQPCsuet6J0PwgA77q1LGuYhJPtQGm2CGe5-En8DlCs23qXFNSao3b1j_RhEWijKbzBf5wY7QpcS3WylLMrFFFdc3Fs2CnOXkh848faPQegNDtCo9tFslAXSpupJ-MshJMEnxkzOYwsDbKgnU62Ysv2RFGaTBwFKqCCXDMMlJbsYdB7QWz-G8A6slCJ95ZPkks1ApFjtJFnc3afj3XaoTUtM2TnoX8wB3TEHLkYybRPXGwsi66XYKbZnYNPfnNWxm6AFjeUfaaJdBcxvddcya3twhNGUNl7X0fM7I4KA5O-coRNQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ربات‌های پست‌چی مشغول کار هستند
🔹
با جایگزینی ربات‌های هوشمند در پست به‌جای روش‌های سنتی، سرعت پردازش و تفکیک محصولات پستی ۵۷ درصد افزایش داشته است.
@Farsna</div>
<div class="tg-footer">👁️ 8.61K · <a href="https://t.me/farsna/461783" target="_blank">📅 15:11 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461782">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XPoK9-lIz8CUfkN1vu1Qu-LCrkTi-M5lmeQKeYynwvyRzQmfvE-TojXu5-4BtFQsDzmVAM5WGzuf-4bT0zxptoKvu8GOarEuto1zE0fbw5O4gzbY_oJUos7EEA240TdPMiv8fKktMDw9fRW_S1uI_fOiJSDKnfQ5OyK86GAEevT4RyJvjlWXLJp_9b6zIynRkrkDeB-vsN7RlmD4XUIkpnBTz7ufO1uNWnj110tpSIbCMOxTz8pzODUltG_j2daHisx8cSIz9-r-Zhy9al2JFkqZ9POfaG57_YtKIXB7gXOQs8ziS0OMp7aqJ2MIFqqzp5oY1kaFA1_EYaQ8gGblyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کاهش ۹۷ درصدی تردد در تنگۀ هرمز
🔹
برخلاف ادعای ترامپ که مدعی است «تنگه در کنترل است» آمارها کاهش ۹۷ درصدی تردد نفتکش‌ها در تنگه هرمز را نشان می‌دهد.
🔹
آمارها نشان می‌دهد که روز جمعه ۱۱ سپتامبر تنها یک نفتکش از تنگۀ هرمز عبور کرده درحالی‌که سال گذشته در همین زمان ۳۱ نفتکش از این آبراه عبور کرده‌اند.
🔹
حالا اقتصاددان آمریکایی استیو هانکه می‌گوید «به لطف رئیس‌جمهور ترامپ، تنگۀ هرمز عملا و از هر نظر بسته شده است».
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.9K · <a href="https://t.me/farsna/461782" target="_blank">📅 15:06 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461781">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5e242469d8.mp4?token=W5IhgdkbmZ-QxuQUH8NxubjJo2ykqfvsrabUiyjN-BNRnoHx84NfKkjyMj5XzIq9dXlYmdvPg3xi3DfaO8THDCpQn0Meq1Jo9jP51cZKI2qKMm-BBaqVHJBMBdtQE74FGQWE9aAeCmT9vcAqZgExa3yDdYcJS5xVQTCeLwaVWcd5IuyosbZbiowEdzMvAyp-g2oIbVIiT_tTciabJViti25MqnImUTNfmIK02IvpLEwxJ35pTw-KFJRJ7CPwMe80ruOD0Hy9aESJZxSr0TAjHZgB2qpCIw2rwH8DlX4oWUH4ZU5nL-Jq5tWUcxbuILlS5TBWnxMw7_chmoIHcLxnLIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5e242469d8.mp4?token=W5IhgdkbmZ-QxuQUH8NxubjJo2ykqfvsrabUiyjN-BNRnoHx84NfKkjyMj5XzIq9dXlYmdvPg3xi3DfaO8THDCpQn0Meq1Jo9jP51cZKI2qKMm-BBaqVHJBMBdtQE74FGQWE9aAeCmT9vcAqZgExa3yDdYcJS5xVQTCeLwaVWcd5IuyosbZbiowEdzMvAyp-g2oIbVIiT_tTciabJViti25MqnImUTNfmIK02IvpLEwxJ35pTw-KFJRJ7CPwMe80ruOD0Hy9aESJZxSr0TAjHZgB2qpCIw2rwH8DlX4oWUH4ZU5nL-Jq5tWUcxbuILlS5TBWnxMw7_chmoIHcLxnLIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
۳ امتیاز پیاپی پوریا حسین‌خانزاده مقابل ژاپن  @Farsna</div>
<div class="tg-footer">👁️ 7.78K · <a href="https://t.me/farsna/461781" target="_blank">📅 15:02 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461780">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/793dbe983d.mp4?token=pQMix4KK-PLNpJYk2H7fvcrl8m8kuoyX9blDiAu7JZpLwmftqtZeNGHFlYHPcrvYWq2AFuaH8cHp4XYqqvfYSpuRcJtvLiWp2if-O6tSOSfDoysYJSnE_2-eXP7htnzaCMcBAUFgvZbZ_CpW8bfn48lCTNpcgJoFXmyV_K87RDn293_KpYm2cTeE8YXsi11FZA_W7VmGy-_hO1ANtP-kI-0ttZuILVIW1YFTe9r4rfI4lVYUj9YnUxz80OakZ-X5HNx5NxaVti62tw1CRWOXiyfqkFTCdLdCkkfa8iBYiPkW2tn_izLBckbyOJfG61HcpifJXE910ONPTJRgyvZ13A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/793dbe983d.mp4?token=pQMix4KK-PLNpJYk2H7fvcrl8m8kuoyX9blDiAu7JZpLwmftqtZeNGHFlYHPcrvYWq2AFuaH8cHp4XYqqvfYSpuRcJtvLiWp2if-O6tSOSfDoysYJSnE_2-eXP7htnzaCMcBAUFgvZbZ_CpW8bfn48lCTNpcgJoFXmyV_K87RDn293_KpYm2cTeE8YXsi11FZA_W7VmGy-_hO1ANtP-kI-0ttZuILVIW1YFTe9r4rfI4lVYUj9YnUxz80OakZ-X5HNx5NxaVti62tw1CRWOXiyfqkFTCdLdCkkfa8iBYiPkW2tn_izLBckbyOJfG61HcpifJXE910ONPTJRgyvZ13A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
بازسازی پل‌های آسیب‌دیده در جنگ ۷۰ درصد پیشرفت داشته است
🔹
مدیرکل مدیریت بحران سازمان راهداری: در مجموع حدود ۶ همت به‌ پل‌ها در جنگ خسارت وارد شده که تاکنون ۲ همت اعتبار برای بازسازی‌ آن‌ها اختصاص داده شده است.
@Farsna</div>
<div class="tg-footer">👁️ 8.2K · <a href="https://t.me/farsna/461780" target="_blank">📅 14:54 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461779">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cf247b98d2.mp4?token=NaIs4efcx80DlxavSccbY8tOW8qINj_8Czg8og8SL7lQfuEJ1pyzViT4tn6nFyx6adNPAyJHxphnXH0jS1zm_1uRBIbDmlT7P1GMaFeykv6ZirAgrABfvCRE2YQNmrQiIu5mxmdq4F5vKRzH8MN8NgZ0V-evQPtDP1WSAS6RJ8Jdy842x3upvWXr--lmP_2vJlQTove3zEwhxoVS-vhS4xfBSGiXJeUEXjvcA39eT45329gHqVs7iycYFifPY0VtBpFoeGtaX8tfyShx5tcQ3Eltre6niNnnFv0Chpgnj-vTUGWQTOXd0YVdTNINaYx-4AMSJ9upgL7wL2sGkRtVJA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cf247b98d2.mp4?token=NaIs4efcx80DlxavSccbY8tOW8qINj_8Czg8og8SL7lQfuEJ1pyzViT4tn6nFyx6adNPAyJHxphnXH0jS1zm_1uRBIbDmlT7P1GMaFeykv6ZirAgrABfvCRE2YQNmrQiIu5mxmdq4F5vKRzH8MN8NgZ0V-evQPtDP1WSAS6RJ8Jdy842x3upvWXr--lmP_2vJlQTove3zEwhxoVS-vhS4xfBSGiXJeUEXjvcA39eT45329gHqVs7iycYFifPY0VtBpFoeGtaX8tfyShx5tcQ3Eltre6niNnnFv0Chpgnj-vTUGWQTOXd0YVdTNINaYx-4AMSJ9upgL7wL2sGkRtVJA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ژاپن دست اول را از ایران برد
🇮🇷
۲۱
🇯🇵
۲۵   @Farsna</div>
<div class="tg-footer">👁️ 8.31K · <a href="https://t.me/farsna/461779" target="_blank">📅 14:50 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461778">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/116b60a2d8.mp4?token=GxoNl-Uz_9RALk3tJ39DuqXA6onUNsXu2FQn1eS6B5QO6edITAuSAThFAlHNfByA4cF8MUVV3pF_4DUArxPnqD8l-89pJ7pflvUP0q4ju9Ksz5QVMnqy6YbEGc4Fl8XHaTWbRjrNab9uYI9afe6604v1NcAIyBTFE9lADWi8UkYj42bCFgey9wjHD5R1w2fUN1OeEzj1dI6KjmyCfuS0ceIRs2F90EoO0KNOaJiN0p0V1498ErAzffdvA9mTWMYPOqAOXXqJjAzsg1ZK5DSFVu8k-Y8HbhHO0O31n8x4Fnv3X92h67dYUsc7QePox5aZSDW8BtSaVrQPnKzlbqjz1A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/116b60a2d8.mp4?token=GxoNl-Uz_9RALk3tJ39DuqXA6onUNsXu2FQn1eS6B5QO6edITAuSAThFAlHNfByA4cF8MUVV3pF_4DUArxPnqD8l-89pJ7pflvUP0q4ju9Ksz5QVMnqy6YbEGc4Fl8XHaTWbRjrNab9uYI9afe6604v1NcAIyBTFE9lADWi8UkYj42bCFgey9wjHD5R1w2fUN1OeEzj1dI6KjmyCfuS0ceIRs2F90EoO0KNOaJiN0p0V1498ErAzffdvA9mTWMYPOqAOXXqJjAzsg1ZK5DSFVu8k-Y8HbhHO0O31n8x4Fnv3X92h67dYUsc7QePox5aZSDW8BtSaVrQPnKzlbqjz1A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پیشنهاد روزنامهٔ عبری به جوانان آمریکایی: با ایران بجنگید تا بدهی‌هایتان بخشوده شود.
@Farsna</div>
<div class="tg-footer">👁️ 8.53K · <a href="https://t.me/farsna/461778" target="_blank">📅 14:45 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461777">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RiRCH395-P4-C5_kr09IkuLml_YyckQNopJjYHzPuJewWOBN0V3ik8C0PY9iibNNfHQcfn25_342ZtKlWE52xF0CRCoDAWA1CZhrSC-hhfIoi_j1KFb2P8u-LbLUIMqTtQcrU_moyE4b4aubyAO6zt4s95o15W4jYcnhh9UhlEFKSEElei179GsjRcZ9dLmq2m8rQPdOlvyndAC2Vaaa9NCIxaED6C3cryTN_TLXnCgCTTi0Gqq9nhNjwC2KP7ZyTi9Km67eDKjD2E9HCXOIW8vk0yh40c0QJ-F0rL2rwgJtXCIZec3x3xhE2ERDwyyQBSTnnOni1emAWrwc8_Fk9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دفتر سقاب: ادعای بلاگر اقتصادی دربارهٔ شهید رئیسی کذب است
🔹
مدیر حوزهٔ ریاست در ستاد تحول دولت شهید رئیسی، در واکنش به اظهارات یک بلاگر اقتصادی گفت: او را نمی‌شناسم و اسمش را هم نشنیده بودم و تمامی اظهارات وی دربارهٔ دعوت به ستاد راهبری تحول دولت و یا تهیه…</div>
<div class="tg-footer">👁️ 9.58K · <a href="https://t.me/farsna/461777" target="_blank">📅 14:39 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461776">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a1a0932c80.mp4?token=WaxVZ1SH7LGF5k8Wdk21PwksHJ7g1vq5hDITfC_om7CDJYo32pXUBDWgu97Avn1InwHdeHbRPvRafiWaPTKOmf0wwlTZ6lJrE9C6wWeNJXdyOdw164qsIQGNUTYAsyBV5mGqF6miAsbuAps8s3-IUvgNc_97Pu-xhyt17l_GKlHM4bTMyZrSuRH2QRvIpRS0XVx1-jfgmRy7TV4cuemkfiJ4tt7HnZCeaciJHLK5C8MLYCSuXo93ga4dt6fAysQucTaO3-6r_dhPMdYR0XARp-vDIgokeVKwfpbx-0HHAdXh3WgjUZZAeXTov2tMFR7HRBRvD8IxqULFnqwlYyo6HA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a1a0932c80.mp4?token=WaxVZ1SH7LGF5k8Wdk21PwksHJ7g1vq5hDITfC_om7CDJYo32pXUBDWgu97Avn1InwHdeHbRPvRafiWaPTKOmf0wwlTZ6lJrE9C6wWeNJXdyOdw164qsIQGNUTYAsyBV5mGqF6miAsbuAps8s3-IUvgNc_97Pu-xhyt17l_GKlHM4bTMyZrSuRH2QRvIpRS0XVx1-jfgmRy7TV4cuemkfiJ4tt7HnZCeaciJHLK5C8MLYCSuXo93ga4dt6fAysQucTaO3-6r_dhPMdYR0XARp-vDIgokeVKwfpbx-0HHAdXh3WgjUZZAeXTov2tMFR7HRBRvD8IxqULFnqwlYyo6HA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
یمنی‌ها معادلهٔ جدیدی در سواحل غربی رقم زده‌اند
🔹
رادارهای پیشرفتهٔ آمریکایی را که عربستان به مزدورانش در یمن داده بود، تحت کنترل ارتش یمن در آمده است.
@Farsna</div>
<div class="tg-footer">👁️ 8.69K · <a href="https://t.me/farsna/461776" target="_blank">📅 14:33 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461775">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/72852729b1.mp4?token=bq-Df72EKb8gGNIkvCP1BvJNt3s9IFNIeb_loKrrwhx0zHq-x3FRcnYpyaGBSFAjSqOJiqFJYMJGKviltucHIdA4R_HNR3rwjAa2vZCJLWnM4va-hJ7JhYS1i8gDdnmvRF4I1-w4ZgCEERrzlz_Jd0VBbJu_2KNUQsFPaMx4hu8cHW3U8fSZv0TmsmXspDgRTM8-tHk2N8cGin3UgaImivCBhgFU9GZer7BbJze1PKvrKPusYcfhMDAAIb34sQIbuScfCP2Fnc5vBJ8-uSes_S5ttrqXjK4it1nFdInJNPOmT9woZGUKa5wfDt_WVOCS0aeGdbNZ3AgmC3cY3bDtzw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/72852729b1.mp4?token=bq-Df72EKb8gGNIkvCP1BvJNt3s9IFNIeb_loKrrwhx0zHq-x3FRcnYpyaGBSFAjSqOJiqFJYMJGKviltucHIdA4R_HNR3rwjAa2vZCJLWnM4va-hJ7JhYS1i8gDdnmvRF4I1-w4ZgCEERrzlz_Jd0VBbJu_2KNUQsFPaMx4hu8cHW3U8fSZv0TmsmXspDgRTM8-tHk2N8cGin3UgaImivCBhgFU9GZer7BbJze1PKvrKPusYcfhMDAAIb34sQIbuScfCP2Fnc5vBJ8-uSes_S5ttrqXjK4it1nFdInJNPOmT9woZGUKa5wfDt_WVOCS0aeGdbNZ3AgmC3cY3bDtzw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترکیب تیم ملی والیبال ایران مقابل ژاپن
🏐
فینال قهرمانی آسیا
⏰
ساعت ۱۴:۰۰  @Sportfars</div>
<div class="tg-footer">👁️ 9.11K · <a href="https://t.me/farsna/461775" target="_blank">📅 14:29 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461774">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a75af81f13.mp4?token=KB-5pgjOws0INSwIfxPEFfvj6_grxlC7K0ZZ9pnhzIrQXcxDHJMnsEWR1w_8C4tNRUKdqPbsBA0Xh7HhoT0CcmB5efB-ij8Nr8E5wUMuSHwsLavJ53EAGhV76oxrJQGI6euVmPTDZqPLVVQT5XzTIATiFPEbRGUzb2eyVmgjvDIat7ErmfNLtRrjtQIT8g9gr68jVTwhYJI9phOXLKml_n_w1SbGAIoaL_dIbNp0UnVWvSjU7zWTJ6d1fISYOSHh9x5ypttwwCWDi8XcXOIRg4M4HoMtNZ6BVvMGYzE6qzRWdOxj_wAhfTvw0Df_Ikce-6KHjt3SIGZOGyI7NNal852jWQyNh2uTiWh2M93eUb8ZSgn-7kF6caUfSWyNWZhBXJEq4Q_a_MDNjMH-oPrgPm5d71R8ijgKpzBBK11_kjfvoZazLuHrq7zQju1_otXkmXcjwWLPBYUqxejMdfVBHIgmWccXP0X8J6D-gP3vAvkELBLHmBSsSbUvPEiVHUi83VgUFMhNFIGXPOolYTOmZGwKJd_8NVI6o-KOynKBdimy36N_Cm4_lVZOUrM4CHppb8lrZ0cgGIvqiBMEG_YQux4FQvk9-ou6AtYyFlEpMoTy1klUFr_wP7M4zrd_pUFuTfTGhXM9ceP0FdtVycN26HWvqf41cARC7EwW1S2t2Z4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a75af81f13.mp4?token=KB-5pgjOws0INSwIfxPEFfvj6_grxlC7K0ZZ9pnhzIrQXcxDHJMnsEWR1w_8C4tNRUKdqPbsBA0Xh7HhoT0CcmB5efB-ij8Nr8E5wUMuSHwsLavJ53EAGhV76oxrJQGI6euVmPTDZqPLVVQT5XzTIATiFPEbRGUzb2eyVmgjvDIat7ErmfNLtRrjtQIT8g9gr68jVTwhYJI9phOXLKml_n_w1SbGAIoaL_dIbNp0UnVWvSjU7zWTJ6d1fISYOSHh9x5ypttwwCWDi8XcXOIRg4M4HoMtNZ6BVvMGYzE6qzRWdOxj_wAhfTvw0Df_Ikce-6KHjt3SIGZOGyI7NNal852jWQyNh2uTiWh2M93eUb8ZSgn-7kF6caUfSWyNWZhBXJEq4Q_a_MDNjMH-oPrgPm5d71R8ijgKpzBBK11_kjfvoZazLuHrq7zQju1_otXkmXcjwWLPBYUqxejMdfVBHIgmWccXP0X8J6D-gP3vAvkELBLHmBSsSbUvPEiVHUi83VgUFMhNFIGXPOolYTOmZGwKJd_8NVI6o-KOynKBdimy36N_Cm4_lVZOUrM4CHppb8lrZ0cgGIvqiBMEG_YQux4FQvk9-ou6AtYyFlEpMoTy1klUFr_wP7M4zrd_pUFuTfTGhXM9ceP0FdtVycN26HWvqf41cARC7EwW1S2t2Z4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تنها ۴ شب تا ۲۰۰ تایی شدن میدان‌داری ملت ایران مانده است
@Farsna</div>
<div class="tg-footer">👁️ 9.26K · <a href="https://t.me/farsna/461774" target="_blank">📅 14:24 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461773">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9aa721fc17.mp4?token=hSa3uknicgx4Y9t2wrT1aR8CO0NoGjKojRQYUH7BNwpn8E4w3Y1UhYkDug3INEQvgcbFWHZLzYRbO9wfuyiIX3m1nqNPeNGGypwbNTGRHpiy3_lm61Eo6exQhC7beFt24BWjUtWsoA5BuJdp5AwlUKCi4uE5RCvtaDspINyLoXF760c_ZBLCDfVr_TiHGjaolrtQu8_Aw_QYv1wwV1MvgMqA4aueBQXDeTNv0nxIyGxkfHhSCEu8GGhPNf63RpA4Wn8k9Sz_fOQKATZ5QyVreZdiheRdpmD-5JGCMFdw_axKTIO6VCtcvahU19Vdzghrem7nE5XiWzHHo1TvN9iJfw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9aa721fc17.mp4?token=hSa3uknicgx4Y9t2wrT1aR8CO0NoGjKojRQYUH7BNwpn8E4w3Y1UhYkDug3INEQvgcbFWHZLzYRbO9wfuyiIX3m1nqNPeNGGypwbNTGRHpiy3_lm61Eo6exQhC7beFt24BWjUtWsoA5BuJdp5AwlUKCi4uE5RCvtaDspINyLoXF760c_ZBLCDfVr_TiHGjaolrtQu8_Aw_QYv1wwV1MvgMqA4aueBQXDeTNv0nxIyGxkfHhSCEu8GGhPNf63RpA4Wn8k9Sz_fOQKATZ5QyVreZdiheRdpmD-5JGCMFdw_axKTIO6VCtcvahU19Vdzghrem7nE5XiWzHHo1TvN9iJfw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
همچنان تنگهٔ هرمز با اقتدار نیروهای مسلح ایران کنترل می‌شود
🔹
تصاویر ماهواره‌ای نشان می‌دهد تردد شناورها از تنگهٔ هرمز بسیار کم شده است؛ طوری که روز گذشته تنها یک نفتکش چینی از تنگهٔ هرمز عبور کرد.
🔸
این درحالی است که آمریکا بار دیگر مدعی شده که کنترل این آبراه در اختیار آن‌ها است.
@Farsna</div>
<div class="tg-footer">👁️ 9.65K · <a href="https://t.me/farsna/461773" target="_blank">📅 14:16 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461772">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b79704f060.mp4?token=Wy8ZQzX8zA8I_hSpHdlwWxESHPBeobavnzcFpq_sUwx6HN76HHXAVHuBmDDfbz56SQpqJjNUyPlxOT0BwWCmqqHZ4MuyWWUxN_hR28KuDeJubZ-Sj4MoRrO6NtN_B_nswA93qMngeWlHBU68TXc-EtyfY0TNdy2cg4wIX3hgaYEMV9Ua6k7FFbKtU4ywC2SMho5ZXckn01vB6sYG5Px3kG9IjgQEYDzaIgNIdf6VnKeKVWDT58MxWL4EjJ2-ZpxEZcW6X-SFCX_1uLe9ubaZQDqyifWRNAab0RcYa-sZHngugEmAneDiUjP3LPdtp8uZAFo0TdwKrb5NV3JACLhDVQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b79704f060.mp4?token=Wy8ZQzX8zA8I_hSpHdlwWxESHPBeobavnzcFpq_sUwx6HN76HHXAVHuBmDDfbz56SQpqJjNUyPlxOT0BwWCmqqHZ4MuyWWUxN_hR28KuDeJubZ-Sj4MoRrO6NtN_B_nswA93qMngeWlHBU68TXc-EtyfY0TNdy2cg4wIX3hgaYEMV9Ua6k7FFbKtU4ywC2SMho5ZXckn01vB6sYG5Px3kG9IjgQEYDzaIgNIdf6VnKeKVWDT58MxWL4EjJ2-ZpxEZcW6X-SFCX_1uLe9ubaZQDqyifWRNAab0RcYa-sZHngugEmAneDiUjP3LPdtp8uZAFo0TdwKrb5NV3JACLhDVQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تصاویر ماهواره‌ای از انهدام ۶ مخزن نفتی آرامکو در ابهای عربستان  @Farsna - Link</div>
<div class="tg-footer">👁️ 9.31K · <a href="https://t.me/farsna/461772" target="_blank">📅 14:06 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461771">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس ورزشی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/POtwToMm-nM5I_Om5fxUhZz9_Xjzza0r5nSAcHyj5xqhFsdV-uDRNyKKEiyiVh42IMG3Wbqx0Xj5SsFJXdllWDEiL-8sj7e6c5ixrjpANZklTTGMZhMY8gf9ted2hx7es7mnlPBt1tcajJKEG9EfhyZET8KqOPMUpsd5UE39XKdGV0WcWnmboo2hjs8ST_YGwR2S8SF-bjBMDsFJH0FfnZVEuUlp6CQfXqmaXpfkI915Rb4oRAtyy4TAd-q8cFvYeAAt_D3WDo3p0YUGl7UgP9hPRJ9PZT7eBCiW-Y44NlNo2wMgBK8LhIcgetbdjO7DlCv1ow7rHfkBR8G7ZDPuQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترکیب تیم ملی والیبال ایران مقابل ژاپن
🏐
فینال قهرمانی آسیا
⏰
ساعت ۱۴:۰۰
@Sportfars</div>
<div class="tg-footer">👁️ 9.54K · <a href="https://t.me/farsna/461771" target="_blank">📅 13:40 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461770">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZVnurcCvJZQpJjtdoPrm_szc45cgScP4K_ojSenkyqPTsp5sbQK8ye5U-15PKAjgUOm3woyqwUtuAor3mcRiQ_NopICD3QD5BQo7K9p-Gg-vf5XR82vopZ5UqLkmkQ606QM_L3ONPfavRolVKPEJxflKderGpulPjVeJfiRj3japkXTijqq_q9u0yZ6aHnWn0yTTR4-WSzjm4A-sXA5UFf2vvNPGKpVvakrvIN_hsnvLGCeQxBudjzrwv8Ye_ranVmTtEl252QalsJCtUqls4ySYlpRF2lFYqHFo_c0hBLR-dlJYf4zyVhFxpU3k9n9Pg-UZnFunvevxs-4hluc6xg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کشف
۱۶ سلاح و ۵۲۲ فشنگ جنگی در یاسوج
🔹
فرمانده انتظامی کهگیلویه‌وبویراحمد: در بازرسی از یک مخفیگاه در یاسوج، ۱۶ سلاح، ۵۲۲ فشنگ جنگی، ۲ بی‌سیم و ۵ دوربین کشف و ۳ قاچاقچی دستگیر شدند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.3K · <a href="https://t.me/farsna/461770" target="_blank">📅 13:39 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461769">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/20f7a2729e.mp4?token=mFzOHBEwrrkiqwqApCdFj5M0VQThbBgL1E7zNZD0bgDtl5de2YaaDkVYP3YhurO5pUBOucU0YLMwqQwnV_hYMC_x76ue_L0ldt3iqh4449b7gmKa3Ylsnj4YCNT2OLEqM2PhmNkKFAEHguNscapaX_N2QMsMQhGnV2IV6xjH-k6dtzqkzyiheqfadtgnMefjHcz_pZfFaE3w6l62rHgzOoUHr-TEuBB33kns451H05KDqLPYzq8xf2x_s8F0Mokm1sCVfmm_lv8y-0z1nDTdDBaPZOXt9mPpFgeohQ7JAtF8n5iqpBVF5WKqp7fKMqc4AEAe9s8C8bnFtiWQZuAtBg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/20f7a2729e.mp4?token=mFzOHBEwrrkiqwqApCdFj5M0VQThbBgL1E7zNZD0bgDtl5de2YaaDkVYP3YhurO5pUBOucU0YLMwqQwnV_hYMC_x76ue_L0ldt3iqh4449b7gmKa3Ylsnj4YCNT2OLEqM2PhmNkKFAEHguNscapaX_N2QMsMQhGnV2IV6xjH-k6dtzqkzyiheqfadtgnMefjHcz_pZfFaE3w6l62rHgzOoUHr-TEuBB33kns451H05KDqLPYzq8xf2x_s8F0Mokm1sCVfmm_lv8y-0z1nDTdDBaPZOXt9mPpFgeohQ7JAtF8n5iqpBVF5WKqp7fKMqc4AEAe9s8C8bnFtiWQZuAtBg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اداره‌کل بنادر هرمزگان: ۴۴ هزار و ۸۴۴ تُن کالای اساسی از ابتدای امسال تاکنون در بندر شهید رجایی ترخیص شده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/farsna/461769" target="_blank">📅 13:27 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461768">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GwgqA_eV8LSRe37MRkZjTqVbOYvcllZDsssHMRheP7TEpqpHvVx9P-GFdKhE_b9B29Z3C21y-z-eM079kCzVkfjEvKavpucJiMrdAava7oVo-z-4goTJzYdSKqn2u2R_-mky2TpAa7MMwsw4P3lMF1etWi_gRhv2T32LXTA9DL-c_p9OCvBHcXKdIcozHNRrwSbKoK_CRzbvJLr2TWsW52X3W0KCnHqqob81y9TJS88uI-YENfSQQjtypSYHjgu6dX2nWyvB7jy4PBlAXt1BPa2lxq-9i91422LNucYLtIrWVJeL-Zcgiz0sWfwazBnFIeQI0MrIt1HcqLUw9yYrlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شهردار ساری برکنار شد
🔹
حسین احمدی در جلسهٔ استیضاح شهردار ساری با کسب آرای تمام اعضای حاضر در جلسه، از سکانداری شهرداری ساری کنار رفت.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/farsna/461768" target="_blank">📅 13:23 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461767">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/03c3b99d9a.mp4?token=IvOTW6ckYHgrlwx4NLkLdhmMRakyg4bapdI5jR4VUYDW7tfQuR8OCgDyusJEgJkm4eTO0r51-M_JfWrXnnuvcE4UEoRVQR26c9mqRjPuozPpGxftMEeph7abHfuXeK_ffMjKM-iADkvS6BvKzsWhejYQCQuq0ur9XIkDlLnJg__AF4zp0HYvX8UsTn9aNk9JgQjjXQrWzel402FRIpQflNFdtJIat16iyIBvwq7BWeE6neJnIrvcWX2sZlK-jSvuG_Q-SJ9R4rAJnBmryHEdO9-8HW3lp0DkBNKByd5fHxkx5sXwX04U9MbeuFjBkw8SV7PH_HawOM3eF5UHUg9pAQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/03c3b99d9a.mp4?token=IvOTW6ckYHgrlwx4NLkLdhmMRakyg4bapdI5jR4VUYDW7tfQuR8OCgDyusJEgJkm4eTO0r51-M_JfWrXnnuvcE4UEoRVQR26c9mqRjPuozPpGxftMEeph7abHfuXeK_ffMjKM-iADkvS6BvKzsWhejYQCQuq0ur9XIkDlLnJg__AF4zp0HYvX8UsTn9aNk9JgQjjXQrWzel402FRIpQflNFdtJIat16iyIBvwq7BWeE6neJnIrvcWX2sZlK-jSvuG_Q-SJ9R4rAJnBmryHEdO9-8HW3lp0DkBNKByd5fHxkx5sXwX04U9MbeuFjBkw8SV7PH_HawOM3eF5UHUg9pAQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حملهٔ روسیه به ۸۰۰ متری مرز ناتو!
🔹
همزمان با تشدید درگیری‌های روسیه و اوکراین، پهپاد روسی به یک کامیون در فاصلهٔ کمتر از یک کیلومتری مرز لهستان اصابت کرد.
🔹
این تأیید رسمی پس‌از آن صورت گرفت که انتشار تصاویری در فضای مجازی دربارهٔ سوختن یک کامیون، منجر به انتشار گزارش‌هایی مبنی بر احتمال ورود پهپاد به حریم هوایی لهستان شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/farsna/461767" target="_blank">📅 13:07 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461766">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IK5nJ0hcCJsJ4BOiBkVYntDHY4aQ8B0SR5RkiWSeiTxfn_JzakumNw11XhRsFfqxAEOQTW-sZV0z1_3GsBdhYzNEsdL_hCGBGRh43HeXzGKI_Ig21B8J3ZdyiAyar1eXdod98BBLlJ5jr5yFZ-1aOunWI4Aa24o_qkwDs66FVJ0XeknSBPLPPAridOz9-OuxzUm56KrBzqq9ZxxlSF6f0iFEjZx7tpoR0vaJ6WDHIot6gBH_lm3-lhNP3hRYSaRwFSxRv-agjEoTfJKJcZP_HVJrAFx1lETvvgLW6AzFTToWBbcu_1Fru-uvM6cDkp2ooShfxCrlfxj_9ohIEkL_4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بورس به یک‌قدمی ۷.۵ میلیون رسید
🔹
شاخص کل بورس در پایان معاملات امروز با جهش ۱۵۳ هزار واحدی به ۷ میلیون ۴۳۱ هزار واحد رسید.
@Farsna</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/farsna/461766" target="_blank">📅 12:37 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461765">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Rs2AM2MTYVWJ7kTwIfL3JZ5aQmWqTs_YQQc4a6TP9Es5lSVTRO3WUpuzSXHFoGGL9H7ReCtbbazmrglMilYOVkg9gqeasWc0ko63pF0nBD42-gj9LhfVA-8EGvv4AnOMn0d5wKQJg6197nMojUjXBApUQxUfFYU5GXNtyGdG_dhZgJajGoUPB4ATAyi7kszNUSLZKcdlCTO8Dg9LWeSBSoyaMJuqLG0XXCQxrPh2XSHvqURJndTmM-Oi3cGhNa_YgxmYSPC6D1niMuWVNK2ztH0yYdhOUD9j28yyIZvq2TaIE1e1vfUEdDV2d8nE3XLnmZ3NLN-IKDs3J6p6b_VgYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
معاون برنامه‌ریزی شهرداری تهران: در بودجه‌ای که پیش‌از جنگ ارائه کردیم، قرار شد ۸۵ درصد هزینه‌های مترو از بودجهٔ عمومی شهرداری تأمین بشود
🔹
کل درآمد پیش‌بینی‌شدهٔ بلیت‌فروشی مترو در سال ۳ همت بوده که فقط حقوق کارکنان مترو در ماه ۱.۲ همت است. امسال برای پرداخت…</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/farsna/461765" target="_blank">📅 12:10 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461764">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromاخبار چهارمحال و بختیاری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c52ec2e915.mp4?token=KFESwG7FGBUy9X5Xr06Vdym-8wU8QMZhkblFSSvV5lBl-4QS9NMZ8A9gWzX64Mzrpn0WHdcGbErQmHPHYR9mYesbduvBCHguWW6ZhbQATJISpMxGPWHclsbOa3OofXI1A5omlLeBeap0JMeYqUXPLPRN-eontaxM9NDDkw62qnTbrP6m1GDdacj64p8z59uuaeeL5cXQ-eigV4Q2wqFHsO3JUpmkWLamRYLYSVvMSpZKROUidtMS-uiJtgdNLbVJ0dgoTtUoiPKJJwyMN5VeU1UWfpWlAAZ1gt4tzOwKHvBxGyjuTWjqWYgpJhAE0NfRbEzPSa1xqXRU8TGkjcDBLJ19xeOA31KV65dAoeQG_xYOpZ_660HmBzqJep1dCWk7-yrO6w3UQJF0xwSuC4Ub3dEIANdDK4QzN7FmueKgcbw0NFmcgdk3sW9JneT62UP91WnhOOFXxXsUZnvwSoJ6I3KpfZXH7XdtzxjbTfBX4LtQ9bMx-Me9oDGASRgZ0u8RlofAvzH4pJ6SglQbSV0l253ZfzvCrkpIu7Vl4_mkO7d0cIRXBT6-CUy3j8lYHuad6ZOyAJBBdcjrDgZKzC-1BzLKMXJ4ylFHBdDR54sZwrgcy0kJsCdbWXNWVDO1cKNXbj6mXORTc34NJRzdKwfymJt43t_0uORFFIusfRr6BiI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c52ec2e915.mp4?token=KFESwG7FGBUy9X5Xr06Vdym-8wU8QMZhkblFSSvV5lBl-4QS9NMZ8A9gWzX64Mzrpn0WHdcGbErQmHPHYR9mYesbduvBCHguWW6ZhbQATJISpMxGPWHclsbOa3OofXI1A5omlLeBeap0JMeYqUXPLPRN-eontaxM9NDDkw62qnTbrP6m1GDdacj64p8z59uuaeeL5cXQ-eigV4Q2wqFHsO3JUpmkWLamRYLYSVvMSpZKROUidtMS-uiJtgdNLbVJ0dgoTtUoiPKJJwyMN5VeU1UWfpWlAAZ1gt4tzOwKHvBxGyjuTWjqWYgpJhAE0NfRbEzPSa1xqXRU8TGkjcDBLJ19xeOA31KV65dAoeQG_xYOpZ_660HmBzqJep1dCWk7-yrO6w3UQJF0xwSuC4Ub3dEIANdDK4QzN7FmueKgcbw0NFmcgdk3sW9JneT62UP91WnhOOFXxXsUZnvwSoJ6I3KpfZXH7XdtzxjbTfBX4LtQ9bMx-Me9oDGASRgZ0u8RlofAvzH4pJ6SglQbSV0l253ZfzvCrkpIu7Vl4_mkO7d0cIRXBT6-CUy3j8lYHuad6ZOyAJBBdcjrDgZKzC-1BzLKMXJ4ylFHBdDR54sZwrgcy0kJsCdbWXNWVDO1cKNXbj6mXORTc34NJRzdKwfymJt43t_0uORFFIusfRr6BiI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
لحظۀ تماشایی بازشدن دریچه‌های سد کارون ۴
@Fars_Chb
-
Link</div>
<div class="tg-footer">👁️ 9.86K · <a href="https://t.me/farsna/461764" target="_blank">📅 12:10 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461763">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">🔴
حملات عربستان به استان‌های تعز و صعده یمن
🔹
خبرنگار المیادین گزارش داد که حملات هوایی عربستان منطقه الربیعی در شمال‌غرب استان تعز و شهرستان مرزی باقم در استان صعده را هدف قرار داد.‌
@Farsna</div>
<div class="tg-footer">👁️ 9.98K · <a href="https://t.me/farsna/461763" target="_blank">📅 12:04 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461762">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PokXQAFjukwpekKUKJwWkWgdgB2MCPH48FR7JN5l8-90RGxWDFpmGJzOA5EwiBIiDo2JmvtWzSidJltzZ0HTzGUfOi1gniU09Rww84wFUyJFvQUmnmoRWp7vPowKMMvMCcy8FXCpW8bxAXRRdjI6tZbVfjheoo6FgDFMTIEFXy-VerLm4sxEl3eZwGLDScQGAprlw_50HRp3_DmEe2dWa0Z8WDAXcXGVtXYyV0CXHZUA5fzgVcx8UeQGQsCVVM_-jghz0N3ao1Bj3gBEBHxlHs-DJ-61T3ycr2OnYml3XrIcytpmQUCatLYY9Vin5IumzHh22rXb0lT80N5aIoYAfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اعتراف ژنرال آمریکایی به آسیب‌پذیری ارتش مقابل ایران
🔹
«جیمز پی. آیزنهاور» فرمانده فرماندهی تسلیحات ترکیبی ارتش آمریکا در اعترافی کم‌سابقه، حملات ایران را عامل تغییر شیوه عملیات ارتش آمریکا دانست و گفت واشنگتن باید پس از سال‌ها اتکا به پایگاه‌های امن و متمرکز، دوباره «پنهان شدن» از دید دشمن را یاد بگیرد.
🔗
شرح کامل این گزارش را
اینجا
بخوانید.
@FarsNewsInt</div>
<div class="tg-footer">👁️ 9.97K · <a href="https://t.me/farsna/461762" target="_blank">📅 11:55 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461761">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f1cefead0b.mp4?token=klkkwLBtYV1airDIJ5DW2MVOjqNDIpCkkQvV1UMGmvO-TAS4vbF8A8dLAG-8rIQHD2nogub5SFyYMJMGI6GT9rx8vT9ffL6b0T25GOCFJxammia6aCqlnWB9cwW8t1PROPfuqylvcIdJ-qrjZMMcUKCukiAYogBFnhZ97wjFrt1jjikvXWL7jVI4kAhG4rsfqdV-xXdCjPdnIxYB1_p7AD5DAutUDOCbX1dHVw08ctjTbbbytrdhCzgB0WafpUOms_2yj84uGKf_lrMlCi5u3P-mnlhTQpz4Xa1tn3KdC94PWtkXZasAFpHxVcD_ZhGKEEVYLbZ7p0zdypz9uTIVnQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f1cefead0b.mp4?token=klkkwLBtYV1airDIJ5DW2MVOjqNDIpCkkQvV1UMGmvO-TAS4vbF8A8dLAG-8rIQHD2nogub5SFyYMJMGI6GT9rx8vT9ffL6b0T25GOCFJxammia6aCqlnWB9cwW8t1PROPfuqylvcIdJ-qrjZMMcUKCukiAYogBFnhZ97wjFrt1jjikvXWL7jVI4kAhG4rsfqdV-xXdCjPdnIxYB1_p7AD5DAutUDOCbX1dHVw08ctjTbbbytrdhCzgB0WafpUOms_2yj84uGKf_lrMlCi5u3P-mnlhTQpz4Xa1tn3KdC94PWtkXZasAFpHxVcD_ZhGKEEVYLbZ7p0zdypz9uTIVnQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
عضو کمیسیون برنامه و بودجه شورای شهر تهران: رایگان‌بودن حمل‌ونقل عمومی هیچ آسیبی به نوسازی نمی‌زند
🔹
هزینهٔ بلیت مترو در بودجه صرفاً برای هزینه‌های جاری مثل نظافت استفاده می‌شد که این هزینه امسال پرداخت شده و مشکلی برای تأمین آن وجود ندارد. @Farsna</div>
<div class="tg-footer">👁️ 9.3K · <a href="https://t.me/farsna/461761" target="_blank">📅 11:49 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461759">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fWOhtoRwpG1boWLJizTzOwKM1dHfagTFsNasZKSwMJOMZ6qvqOiYclUnZpHYm2fEsKt8fpJUkc9zKD5PgJZo8sM-xtZNv7cb_Z9ZOeXAAZiY4zIvQkveeFfv6r8bIM1a8W5qekuuThDwV8iu1L8U_v9YvioopSbny-jtdEvixVN_2pl5_1RUxN8H020-qoFMyx0rx6h24QIYBzzh7C3mileKvwkFzEsajS8K00r9IWdvpo7AF2Uf5zFYHp9f3wSeYqBIHrI-fOJTiKiDp6DemIBoMoECODAUNw1pLX4hw2XjSdEYfXbNVI-oDrKIvh8MCe_4L2TU7o51BbEkCXUgCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مهمان‌پرست: هرمز و باب‌المندب آمریکا را به عقب‌نشینی وادار می‌کند
🔹
سخنگوی پیشین وزارت خارجه در گفت‌وگو با فارس: پیشروی انصارالله و تسلط بر بخش‌هایی از نوار ساحلی و جزایر مشرف بر باب‌المندب، معادلات منطقه را تغییر داده است.
🔹
جبهۀ مقاومت اکنون از طریق هرمز و باب‌المندب بر دو شریان حیاتی انتقال انرژی جهان اثرگذاری جدی دارد.
🔹
فشار هم‌زمان در این دو گلوگاه، هزینه‌های اقتصادی آمریکا و اروپا را افزایش می‌دهد و می‌تواند به رشد بیشتر قیمت جهانی انرژی منجر شود.
🔹
آمریکا به‌دلیل شرایط داخلی و افزایش قیمت سوخت، آمادگی تشدید درگیری را ندارد و در صورت تداوم این وضعیت، ناچار به عقب‌نشینی و بازگشت به میز مذاکره خواهد شد.
🔹
اگر دولت هم‌زمان با اقدامات نیروهای مسلح و جبهه مقاومت، مشکلات اقتصادی و معیشتی مردم را مدیریت کند، گذشت زمان در جنگ تاب‌آوری به سود ایران خواهد بود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.39K · <a href="https://t.me/farsna/461759" target="_blank">📅 11:42 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461758">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FIhGsmxIKZwO_h6lWp-1SDhXhxXsJpMjibsvM0XikrAje4W8R5U-p38dztECbwtOWDBRp_oJzR5KGNDfZnGdcQgjh75BlQCaGI8XKVLOhGjT3PZ5CTs1Yw0Os6_CdjcSMLP5x5hs1ejXc3IPKNkRO_nObmXxNQBgpJCBOqq4WtKSpFvnXyjJdx7YW8dbziy0hIIj5uoaN3wwuFDUmmHbmayJN0qOlaoB1I3Jqs_OjhpuHWsbHyx32z0rCUE7EkzSWUlrZIHOCpiHDkEHITSfpYyKFRZPOwekrDXmfWd_K_0LmQ8fE7SBdz1qEhFX2e97rgF99uMCQz6UfP5QNZe3ZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پزشکیان: اگر دنبال سلاح هسته‌ای بودیم عضو «ان‌پی‌تی» نمی‌شدیم
🔹
رئیس‌جمهور در گفت‌گو با شبکۀ خبری ایندیا تودی هند: روابط ایران با همسایگان از جمله امارات، عربستان، پاکستان، قطر، روسیه و چین دوستانه است؛ مشکل اصلی پایگاه‌های آمریکا در منطقه است.
🔹
ایران آغازگر…</div>
<div class="tg-footer">👁️ 9.33K · <a href="https://t.me/farsna/461758" target="_blank">📅 11:19 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461757">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/82090b4fd0.mp4?token=TqwtvXsUBVbaKZGXrIwcAvo6fdfkPbTggr1NElOWmV8zK17jhL_V-fREhj6GR41xIX-NC66nHQT3CY3gWOPSV3dloUB68rlxgVU5or5YVY4RXoTiWuAFNJN-Zli5iL0fQg71nNtfjxIjSJGRjfGw-1EHOUqCnz-y3mZIAbIHPyKpbsvINPKz8SC0hn6sFcWan0i0ns6dIDrN1bahvuxbLeCqoZ1aKDuzReNupdFYyNvuomsVCZrEy9H4fQoSPnqI68w0xjtfOYGDt4e3Y8z9xEX9I-CdZesMFXeCZvDESc6pHUgBLSzGDnbLusKSA3wGTuDrvg9rX4XDxlN6dBs_2g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/82090b4fd0.mp4?token=TqwtvXsUBVbaKZGXrIwcAvo6fdfkPbTggr1NElOWmV8zK17jhL_V-fREhj6GR41xIX-NC66nHQT3CY3gWOPSV3dloUB68rlxgVU5or5YVY4RXoTiWuAFNJN-Zli5iL0fQg71nNtfjxIjSJGRjfGw-1EHOUqCnz-y3mZIAbIHPyKpbsvINPKz8SC0hn6sFcWan0i0ns6dIDrN1bahvuxbLeCqoZ1aKDuzReNupdFYyNvuomsVCZrEy9H4fQoSPnqI68w0xjtfOYGDt4e3Y8z9xEX9I-CdZesMFXeCZvDESc6pHUgBLSzGDnbLusKSA3wGTuDrvg9rX4XDxlN6dBs_2g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چمران: مترو و بی‌آرتی تا بررسی مصوبهٔ جدید رایگان است
🔹
رئیس شورای شهر تهران: لایحهٔ جدید حمل‌ونقل عمومی رایگان در جلسهٔ آیندهٔ شورا بررسی خواهد شد و تا زمانی که مصوبهٔ جدیدی در این زمینه تصویب شود، روند حمل‌ونقل رایگان ادامه خواهد داشت. @Farsna - Link</div>
<div class="tg-footer">👁️ 9.23K · <a href="https://t.me/farsna/461757" target="_blank">📅 11:16 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461756">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">انهدام مهمات عمل‌نکرده در دماوند
🔹
سپاه استان تهران: انهدام مهمات عمل‌نکردهٔ دشمن تا ساعت ۱۶ امروز در دماوند انجام می‌شود؛ احتمال شنیدن صدای انفجار ناشی‌از این عملیات وجود دارد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.86K · <a href="https://t.me/farsna/461756" target="_blank">📅 11:14 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461755">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d5c4de85f3.mp4?token=ZXoHC7oOUrvhWBMu63mues5kbnGGQBxKniw_U_cf5cgFkgXcx2-fI8RWCsmHLU_TBZD50DSQYFX8oVSojXznvS6_Kpu7jGaIPg62MF6LAcNOpLwYllaWzI7eJIvmU5zt5yvG0uBjlzNrZ3zXB0qXDwf5HocmpXwMxFWWUfGRwFHcWhV14WkON-S5H9ey55N1h3dpe2sowg80JGMCC9NVDyxajb6db4XEb5PwTrwskekVqqJmvN284SwEaPoAK7Abshcq6JlWvPerPEriyh-U9vDnJXlOcyxPg6QNYoCDgrhGirBoDNxu1GVxzVwpzkZiZM-rXQ9-mF9K3tGlJyDllw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d5c4de85f3.mp4?token=ZXoHC7oOUrvhWBMu63mues5kbnGGQBxKniw_U_cf5cgFkgXcx2-fI8RWCsmHLU_TBZD50DSQYFX8oVSojXznvS6_Kpu7jGaIPg62MF6LAcNOpLwYllaWzI7eJIvmU5zt5yvG0uBjlzNrZ3zXB0qXDwf5HocmpXwMxFWWUfGRwFHcWhV14WkON-S5H9ey55N1h3dpe2sowg80JGMCC9NVDyxajb6db4XEb5PwTrwskekVqqJmvN284SwEaPoAK7Abshcq6JlWvPerPEriyh-U9vDnJXlOcyxPg6QNYoCDgrhGirBoDNxu1GVxzVwpzkZiZM-rXQ9-mF9K3tGlJyDllw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سردار حسن‌زاده: مهم‌ترین پیام رزمایش ۳۱۳ هزارنفری، مقاومت، ایستادگی، پایداری و خونخواهی است.  @Farsna</div>
<div class="tg-footer">👁️ 9.18K · <a href="https://t.me/farsna/461755" target="_blank">📅 11:13 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461754">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Dvx8lNVR_6gO79xPeVf85Vq8XbQr5vubots-7PQrllyrWqVuX_WETqSGx79eEeAUjWPiTvYGGFUQ0XukbBOgrThMNCaJ7riZQnR-AJGPS9hunAdM34SfZWh4uK_iAspUBJVIhGDdB3R3_zkUxLC7JEGpOhXlkU_rKUre2nP5A2lJOylQk97p1sm_OYdvd9AJG1rlDuA3wtrRYdOBH4VMJKYX392OnGqWbKbfS2XeBMbGSFQDmKn_tqeTeMoiMN45UZpa1OIz2vIzTzH9AztwcFFamfe0ocCmxpmNTLaVZcnbDkaBBscv6WxywNuekKXjrGj1Gc-j94-HbhPWynneww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رئیس بانک مرکزی برای شرکت در اجلاس روسای بانک‌های مرکزی کشورهای اسلامی، راهی استانبول ترکیه شد.
@Farsna</div>
<div class="tg-footer">👁️ 9.32K · <a href="https://t.me/farsna/461754" target="_blank">📅 11:08 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461753">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4dc8b45019.mp4?token=tPXAmHQuBVcbQaF0TxwVpz90qFUVsBsVdBcnulUZC8dgdch2xG_nvoPR_A4T7J3IHxbpfNzvS_8eFQSnXWowj_EwZZULJCNIBD35pLisJ-fE5Itr4tBuis6E3JsH6OYK0IXFPPRdjL7bV71--HSnhIVDdZSZTTYgJXjsYw_Y9wm7769_R8gpVlRo1DACcswzSW9NiLKtFfepyxqBbXVAhMJNjFZJn5aMb8-tXrMuwVv7msf1DIssNozIs0pNlZX8QeG0anW90hPwRHRoKFNTOD0_M15LYv89osPBX3rr7b4SwJSe0JnOG4OP8hXIRJDOiBsCBi_CO7kGkMuzKVOxoA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4dc8b45019.mp4?token=tPXAmHQuBVcbQaF0TxwVpz90qFUVsBsVdBcnulUZC8dgdch2xG_nvoPR_A4T7J3IHxbpfNzvS_8eFQSnXWowj_EwZZULJCNIBD35pLisJ-fE5Itr4tBuis6E3JsH6OYK0IXFPPRdjL7bV71--HSnhIVDdZSZTTYgJXjsYw_Y9wm7769_R8gpVlRo1DACcswzSW9NiLKtFfepyxqBbXVAhMJNjFZJn5aMb8-tXrMuwVv7msf1DIssNozIs0pNlZX8QeG0anW90hPwRHRoKFNTOD0_M15LYv89osPBX3rr7b4SwJSe0JnOG4OP8hXIRJDOiBsCBi_CO7kGkMuzKVOxoA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سردار حسن‌زاده: ملت ما دست از انتقام برنمی‌دارد تا دشمن را از اقدام خودش پشیمان کند.  @Farsna</div>
<div class="tg-footer">👁️ 8.16K · <a href="https://t.me/farsna/461753" target="_blank">📅 11:07 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461752">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b94e0f447a.mp4?token=eF8oAYWEYX1WcP24FYrlB6H9f05Esut41yTdC_MhCL2T0S4wDRfn3mY_RYzHXjTgKor-ckvvlW4O_TDRcd_Ff7QfYxnT5SFa-RFBqcNmkJLYxHW7BTUdmCiI9HHP7EhE4XbjswzUbdRKVKCHz6oK5l3ZmbcdiISX4jZ-W-u8E9PIlRjPqIEk7_0QUZQEhVJ5lA_dReca45Rg0rqQHMow8x0sS0FGbOse_xTAcN33R68na-mqbRV4OecoRUD42JcXoaNFWpJUj6qaVX4nzSJVDuGTKvBeUffheR3A5igMmpK1x515faVAIQbHLvcuLAhoExhzsRoUW8mFdqKMVsy_zw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b94e0f447a.mp4?token=eF8oAYWEYX1WcP24FYrlB6H9f05Esut41yTdC_MhCL2T0S4wDRfn3mY_RYzHXjTgKor-ckvvlW4O_TDRcd_Ff7QfYxnT5SFa-RFBqcNmkJLYxHW7BTUdmCiI9HHP7EhE4XbjswzUbdRKVKCHz6oK5l3ZmbcdiISX4jZ-W-u8E9PIlRjPqIEk7_0QUZQEhVJ5lA_dReca45Rg0rqQHMow8x0sS0FGbOse_xTAcN33R68na-mqbRV4OecoRUD42JcXoaNFWpJUj6qaVX4nzSJVDuGTKvBeUffheR3A5igMmpK1x515faVAIQbHLvcuLAhoExhzsRoUW8mFdqKMVsy_zw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پزشکیان: زیرساخت‌هایی که طی دهه‌ها برای توسعۀ ایران ساخته شده بود، در جنگ اخیر آسیب دید
🔹
این وقایع یادآور مسئولیت سنگین جامعۀ بین‌المللی در قبال حمایت از غیرنظامیان و جلوگیری از عادی‌سازی حمله به اهداف غیرنظامی است.
🔹
بریکس باید اطمینان دهد که هوش مصنوعی…</div>
<div class="tg-footer">👁️ 8.36K · <a href="https://t.me/farsna/461752" target="_blank">📅 11:03 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461751">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tbV7wU7E5cNscHfckWfq7jUsnkveQg2FJPatWsTQCah1gTCe5oRN7EogU1sNodwGtieFqAZBkAVtj1PwPWCZWorcMcVYz6VYdtvHGRGj5C-SE6OrJETKxzvOF1tAmivCyGixwO-fDqHlUFkj-C3f9aMXiQf3ZJ1pqfD5gHH1nn4fDXfjVuTAwFO3LLwDvZbu7KxG_dzJTKjFSfZB0ZUxUOLl_QhvXp2QftlQ_Nyn2vhP9YO-iTtn_rcHIZ_YwqqRG0CTIgu3nHPqEedFM0vTJ0ku6xD0xsVj0xAbMzjggnbJS1eeczW9A9_88FwV624cXbR2TDlFH8W01ilDCtqnLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زلنسکی: حاضرم در آمریکا با پوتین دیدار کنم
🔹
رئیس‌جمهور اوکراین در مصاحبه با دویچه‌وله از دیدار با همتای روس در حاشیه نشست سران گروه ۲۰ که قرار است دسامبر در میامی آمریکا برگزار شود، استقبال کرد و گفت: در صورت حضور پوتین، من هم حتماً شرکت خواهم کرد. باید باهم…</div>
<div class="tg-footer">👁️ 8.52K · <a href="https://t.me/farsna/461751" target="_blank">📅 10:56 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461750">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/610198cd26.mp4?token=l0S7A9a8xF3B3QJi8Wz0ZO4XXxyRFcGLT9EjdS6S3_ibTmRbKuwY_7hizcImtmZCdTw9HBNkOvl4mjp5c9k3H4PRDbWVCEKTgipZ3IGy_Rnc8FoZnnnHgu-mhIzB8FDTJvSqHPCC549HWuUYzCX0AafpB-o22ZDwvGx9PbcgB_benDIVBZrQXCs8ZnyxCG4PgvnNii1Goz6FoEV1s4_NVS1CVCtUdPAkitXz1Zq9eGMCQab1Hrup9PNRgn5CFShY_UrgryTMqqoYZaYFIABTHKvbRiW4evnCsNpzMNH4KELpP2ROwd706ocEEQO_8gXUX8SxTBcXOp8tXmDi_lGehQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/610198cd26.mp4?token=l0S7A9a8xF3B3QJi8Wz0ZO4XXxyRFcGLT9EjdS6S3_ibTmRbKuwY_7hizcImtmZCdTw9HBNkOvl4mjp5c9k3H4PRDbWVCEKTgipZ3IGy_Rnc8FoZnnnHgu-mhIzB8FDTJvSqHPCC549HWuUYzCX0AafpB-o22ZDwvGx9PbcgB_benDIVBZrQXCs8ZnyxCG4PgvnNii1Goz6FoEV1s4_NVS1CVCtUdPAkitXz1Zq9eGMCQab1Hrup9PNRgn5CFShY_UrgryTMqqoYZaYFIABTHKvbRiW4evnCsNpzMNH4KELpP2ROwd706ocEEQO_8gXUX8SxTBcXOp8tXmDi_lGehQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سردار حسن‌زاده: ما گردان‌های سازمان یافتهٔ ۷۲ نفره از باشگاه‌های ورزشی و مجموعه‌های هنری و مذهبی و تمام اصناف داریم که برای شرکت در رزمایش ۳۱۳ هزارنفری ثبت‌نام کرده‌اند.  @Farsna</div>
<div class="tg-footer">👁️ 7.91K · <a href="https://t.me/farsna/461750" target="_blank">📅 10:56 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461749">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0ff583802f.mp4?token=Su3qFieZXKeWy9RDjqBcwmGWGPGBvuOYt8AbJq3yRYL5-1Qc8s0AwMwALrUCNMuWHC0xdKwpPnVfCpvx_TfUhoS_MbnThGAjgD4-0eRc9NfVKA9zrRmNv54d5LN3Sl6-FHICmbNPqAMnfBr21y6-ZKOqr2kWGfVH6GnCGWWFpRFtpbHfL1ZGbPxYA_IWEGzvQ6j6Je1kCPTuGCURtBFeO42JL23hD-kvPI3xCgEpoJj5rPCiR4xBUOUc4fCpHlA_1XfRk3zTjAXHow79Wr7_jFxKZZTdKKBDeDBFiY8wK4kh9Xe9uhO9WPDsLmFx6UFpq5WHHsTY_3t4NdVAyPHPdQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0ff583802f.mp4?token=Su3qFieZXKeWy9RDjqBcwmGWGPGBvuOYt8AbJq3yRYL5-1Qc8s0AwMwALrUCNMuWHC0xdKwpPnVfCpvx_TfUhoS_MbnThGAjgD4-0eRc9NfVKA9zrRmNv54d5LN3Sl6-FHICmbNPqAMnfBr21y6-ZKOqr2kWGfVH6GnCGWWFpRFtpbHfL1ZGbPxYA_IWEGzvQ6j6Je1kCPTuGCURtBFeO42JL23hD-kvPI3xCgEpoJj5rPCiR4xBUOUc4fCpHlA_1XfRk3zTjAXHow79Wr7_jFxKZZTdKKBDeDBFiY8wK4kh9Xe9uhO9WPDsLmFx6UFpq5WHHsTY_3t4NdVAyPHPdQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سردار حسن‌زاده: تا به امروز بیش‌از ۴۰۰ هزار نفر برای رزمایش ۳۱۳ هزارنفری جان‌فدای ایران ثبت‌نام کرده‌اند.
🔹
این رزمایش جمعه از ساعت ۸ صبح از میدان امام‌حسین(ع) و تقاطع نواب تا میدان انقلاب آغاز می‌شود.   @Farsna</div>
<div class="tg-footer">👁️ 8.49K · <a href="https://t.me/farsna/461749" target="_blank">📅 10:55 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461748">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bb0931d250.mp4?token=DYvpt_yaJO0yToOp8N8EPKe2c0_SKyLG1IE8dUFc92YR26vufrJPoJyYRk3Ptjpj5qdzOS3N7ptIIy1wKHd2OoT4Mkv8TGukEpGVON2o02y7h_LBjFs-GJP_7swWaI1zQhcR6Lq-lW7wot43B6tz4tHu8B2MijLWID-6Egb1SRw_ytGkxl6Du2tKUzh81WqTpQzY11kqXDvT8YH1x-KQgyJi0PQceqQlreV3dQHOeHwcD2TWwfi7zCy-iBVhokix1oY9wG6CXKIiROk5Km_wVDA1-Eduv4mEZyLqcesYMV84PKRg67QrfC0Iuc6u0ydWq9A04vytISQtJJevOU22OzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bb0931d250.mp4?token=DYvpt_yaJO0yToOp8N8EPKe2c0_SKyLG1IE8dUFc92YR26vufrJPoJyYRk3Ptjpj5qdzOS3N7ptIIy1wKHd2OoT4Mkv8TGukEpGVON2o02y7h_LBjFs-GJP_7swWaI1zQhcR6Lq-lW7wot43B6tz4tHu8B2MijLWID-6Egb1SRw_ytGkxl6Du2tKUzh81WqTpQzY11kqXDvT8YH1x-KQgyJi0PQceqQlreV3dQHOeHwcD2TWwfi7zCy-iBVhokix1oY9wG6CXKIiROk5Km_wVDA1-Eduv4mEZyLqcesYMV84PKRg67QrfC0Iuc6u0ydWq9A04vytISQtJJevOU22OzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سردار حسن‌زاده: قطعا تا آخرین قطرهٔ خون پاسدار ایران قوی خواهیم بود
🔹
فرمانده سپاه استان تهران در نشست خبری رزمایش بزرگ ۳۱۳هزارنفری مردمی جان فدایان ایران: دشمنان می‌خواستند مردم ما را در مقابل نظام و انقلاب قرار دهند؛ اما امروز شاهدیم که ملت ایران قریب…</div>
<div class="tg-footer">👁️ 8.7K · <a href="https://t.me/farsna/461748" target="_blank">📅 10:50 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461747">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/341c656828.mp4?token=RzcmvcdbFDg1BK_S_sHL1v3na2zrhU1JkLpvLO5LykDkdoCvzoQPMj1Bb_KbW95OwadvjZD32V4NKf01qqIhRNIq1DU93yLGxB-pj7s55Gv6MJ_vGN1fzwBquPO2jrN5Jz8EI4cGhU-XX7BgrzVCcELABGQoZnvAAiCRsafOcxcxqvvlYVC-e8-uYnV_zbkL_l6YBwQaSfm3fY5Du6Qm_SJV08ycgGtau5QyG5PKtT1OCnBAROJ2DuOfvPdiuQG-3dIcvnC1VYGlfHVOt-p5soOjuPD3j4U5wTth8pGJVHSgb0t1TjigQB-BoqJ3c8jYy9GBbc9eCQyp9raKnSpihg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/341c656828.mp4?token=RzcmvcdbFDg1BK_S_sHL1v3na2zrhU1JkLpvLO5LykDkdoCvzoQPMj1Bb_KbW95OwadvjZD32V4NKf01qqIhRNIq1DU93yLGxB-pj7s55Gv6MJ_vGN1fzwBquPO2jrN5Jz8EI4cGhU-XX7BgrzVCcELABGQoZnvAAiCRsafOcxcxqvvlYVC-e8-uYnV_zbkL_l6YBwQaSfm3fY5Du6Qm_SJV08ycgGtau5QyG5PKtT1OCnBAROJ2DuOfvPdiuQG-3dIcvnC1VYGlfHVOt-p5soOjuPD3j4U5wTth8pGJVHSgb0t1TjigQB-BoqJ3c8jYy9GBbc9eCQyp9raKnSpihg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سردار حسن‌زاده: قطعا تا آخرین قطرهٔ خون پاسدار ایران قوی خواهیم بود
🔹
فرمانده سپاه استان تهران در نشست خبری رزمایش بزرگ ۳۱۳هزارنفری مردمی جان فدایان ایران: دشمنان می‌خواستند مردم ما را در مقابل نظام و انقلاب قرار دهند؛ اما امروز شاهدیم که ملت ایران قریب به ۲۰۰ شب در میادین حضور پیدا کرده‌اند و بزرگترین مولفهٔ ملی را رقم زده‌اند.
@Farsna</div>
<div class="tg-footer">👁️ 8.67K · <a href="https://t.me/farsna/461747" target="_blank">📅 10:46 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461746">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eb3c089129.mp4?token=trorhi0MSRD5qESwjpx6yU_q1hx39yDbK6ct5QF5vpTlkcm-UeAsQsj2XBd3j9glMfuxujzr0in-WIQ0U0NlxTOSyMV6P6eS4VnYX6vU7xbAUlbuyLOLQlwPbVbhQ087zhjpl_0z75GzFKvPByXdQBtfGa39HnaubjTSAauZrN2Ww0l1OycKao9MygKElW90ZA8NHE4mMuUyyyzR4YJchZN9ANEdaGD3zrcoL8jB9bruwO008RaE42jNwfpF-8KydpuHEYhl3IIh5h72bUz66i8KGNGWRnonGEhcbys3Bj_GgvX_DjoQDxysBBkD0JGd5RD5OMNMaLk-EIGvHgt-ewPWSWlR3Ei0uQ6APPI9zD9rTdiPnl7OujZn70Ox2XhWh9CGqQUay5Th1CHqmMUYsKIaAFeNThGd7WoMfZhcEu5oNq5wopLMmqKvHoHARCHOTiaXAyRAMjNPpF0feqGEd1XrCgSIiWm1Zs_NnoqGp1iEGNmuEFEKK0gw2lpz3I7smDrjjiVG4-VfgdQSqP9rIAJBaWyCzLWKiWa63r6AW1uTQlXkoJr7Q5-F2vWCDxNrWGAL26_cJQuvNcdrOBtNlZepCN9_qfoFZ1XmrI3rpwUHJlPVObL1Zrba8jNlaCWPo7iKLM6wtahQqqXbNlby-5pcBxcCtYgLGrOI-yxQqQw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eb3c089129.mp4?token=trorhi0MSRD5qESwjpx6yU_q1hx39yDbK6ct5QF5vpTlkcm-UeAsQsj2XBd3j9glMfuxujzr0in-WIQ0U0NlxTOSyMV6P6eS4VnYX6vU7xbAUlbuyLOLQlwPbVbhQ087zhjpl_0z75GzFKvPByXdQBtfGa39HnaubjTSAauZrN2Ww0l1OycKao9MygKElW90ZA8NHE4mMuUyyyzR4YJchZN9ANEdaGD3zrcoL8jB9bruwO008RaE42jNwfpF-8KydpuHEYhl3IIh5h72bUz66i8KGNGWRnonGEhcbys3Bj_GgvX_DjoQDxysBBkD0JGd5RD5OMNMaLk-EIGvHgt-ewPWSWlR3Ei0uQ6APPI9zD9rTdiPnl7OujZn70Ox2XhWh9CGqQUay5Th1CHqmMUYsKIaAFeNThGd7WoMfZhcEu5oNq5wopLMmqKvHoHARCHOTiaXAyRAMjNPpF0feqGEd1XrCgSIiWm1Zs_NnoqGp1iEGNmuEFEKK0gw2lpz3I7smDrjjiVG4-VfgdQSqP9rIAJBaWyCzLWKiWa63r6AW1uTQlXkoJr7Q5-F2vWCDxNrWGAL26_cJQuvNcdrOBtNlZepCN9_qfoFZ1XmrI3rpwUHJlPVObL1Zrba8jNlaCWPo7iKLM6wtahQqqXbNlby-5pcBxcCtYgLGrOI-yxQqQw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
۱۰ صیاد مفقودشدهٔ هرمزگانی به خانه بازگشتند
🔹
مسئول دفتر وزارت خارجه در بندرعباس: ۱۰ صیاد هرمزگانی که در امارات مفقود شده بودند، روز گذشته وارد تهران و امروز از طریق پرواز به هرمزگان بازگشتند.
🔹
این افراد قرار بود ۱۶ شهریور به کشور برگردند؛ اما به‌دلیل اینکه…</div>
<div class="tg-footer">👁️ 8.94K · <a href="https://t.me/farsna/461746" target="_blank">📅 10:41 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461745">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">احتمال شنیدن صدای انفجار در جنوب اصفهان
🔹
سپاه اصفهان: احتمال شنیده‌شدن صدای انفجار کنترل‌شده در صفه، بهارستان و اطراف آن تا ساعت ۱۳:۳۰ امروز وجود دارد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.21K · <a href="https://t.me/farsna/461745" target="_blank">📅 10:41 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461744">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/360cb20b8d.mp4?token=pNKycMK5RhSbW0UKaDXH56EqF8Pr3Od82OuYOuxFmU0WwLo3ogxCL0lH8c4eyzhrpbrp1jzmZyZQY5qKtElstJf7lNpI03DW9FBxzOE5uqlLI2K0jG8YYR5KbMIXBHREcYMaPxq4L47WABptPC5QG2JkY8mmwOClWnfyXR6gYsIv9R2TkjbjQaUn7cuHjk1hgxseLhYv0mzPRofFskqKDP61U9_7udGDpU2neDU08ll2HDFnl7165rdzdDamp2y5z-ANMwBkCBM8uGSv3dAuBLN60qiroA9NFxR0qG8kgTBiHS5vmggBYx15uhvtbO1YHnvOT2OxCb2gRqQZqX3VbA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/360cb20b8d.mp4?token=pNKycMK5RhSbW0UKaDXH56EqF8Pr3Od82OuYOuxFmU0WwLo3ogxCL0lH8c4eyzhrpbrp1jzmZyZQY5qKtElstJf7lNpI03DW9FBxzOE5uqlLI2K0jG8YYR5KbMIXBHREcYMaPxq4L47WABptPC5QG2JkY8mmwOClWnfyXR6gYsIv9R2TkjbjQaUn7cuHjk1hgxseLhYv0mzPRofFskqKDP61U9_7udGDpU2neDU08ll2HDFnl7165rdzdDamp2y5z-ANMwBkCBM8uGSv3dAuBLN60qiroA9NFxR0qG8kgTBiHS5vmggBYx15uhvtbO1YHnvOT2OxCb2gRqQZqX3VbA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
معاون شهردار تهران: قیمت گوشت و برنج ۶ ماه ثابت می‌ماند
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.58K · <a href="https://t.me/farsna/461744" target="_blank">📅 10:32 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461743">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UNORXxGGZC-nQuMrcwEG4wMHsAucHwMFUDsf7mJwNJGxUiSLJynZdawEkLzHt1GlFxtoxC4h47HfN10MUKDNa5bROWBp-0iXZjlfi3tfBy_r56txsbLNldMAc9FLr2GqLlMTJS9C4DzoBKSkpQoQwdelFQmWLXW0EdTRfcBDKF__zqNmqfWLx10i00HHX8rbOgjq5DAkVWHYsphN5gWHgF0EiEIB76D6-Sz9e_u_ZdSrfX1eeBa9RlE3V2DtuK4hTNyZIi3sXi51WDcl9JxYwj5HzlaahyoGrurZfyvdjy6Jyaifw4RVfcegMS79dpp1ZNg0yJl_FJJl9ORahh6iZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📣
بازدید رئیس‌جمهوری از جدیدترین دستاوردها و راهکارهای ارتباطی ایرانسل
🔸
ایرانسل، در جریان آیین «یک ایران متصل»، جدیدترین دستاوردها و راهکارهای ارتباطی و دیجیتال خود را به دکتر مسعود پزشکیان معرفی کرد و همزمان ۹۴۶ پروژه ارتباطی ایرانسل در ۲۱ استان کشور با حضور رئیس‌جمهوری، به بهره‌برداری رسید.
🔸
این مراسم، با حضور رئیس‌جمهوری، وزیر ارتباطات و معاونان وی، مدیرعامل ایرانسل، جمعی از مدیران حوزه ارتباطات و خبرنگاران، در قالب «خانواده ارتباطات»، ۱۶ شهریور، در سالن اجلاس سران برگزار شد.
🔸
در جریان این مراسم، رئیس‌جمهوری از محصولات و راهکارهای فناورانه ایرانسل، از جمله سرویس eSIM، سامانه فوریت‌های اداری «فواد۱۲۸» و سامانه مدیریت هوشمند ناوگان حمل‌ونقل و قفل هوشمند، بازدید کرد و در جریان جزئیات این راهکارها قرار گرفت.
🔸
در این رویداد که با هدف معرفی و بهره‌برداری از مجموعه پروژه‌های توسعه‌ای حوزه ارتباطات برگزار شد، در بخش پروژه‌های ایرانسل، ۹۴۶ پروژه ارتباطی در ۲۱ استان کشور، به نمایندگی از مجموعه اقدامات ارتباطی ایرانسل، به طور رسمی توسط رئیس جمهوری به بهره‌برداری رسید.
👈
جزئیات بیشتر
@irancellnews1</div>
<div class="tg-footer">👁️ 8.56K · <a href="https://t.me/farsna/461743" target="_blank">📅 10:28 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461742">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromكانال اطلاع رساني بانك كشاورزي</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PdYGW3p9n2_rhSG5nfx2kiu3Ki7KfGffIEXflTQktVIOzzHEO15iCWsBjhu5mdEHcLnAstZVrxAV_ToJ_TK87SKusfCtGVnTz7o-pm7FvRhvVz4S0hi_05YAxcIWh6IwZkPbz6haLTOADQ_ry592iJeg8P75pRO1UQRMc5LF-FyJKMT2IRVl7jgVac5fvPWxI-y4Aeq1JrhEsd3CfE4jh4hsUxPGH_3TzQqT0fOGVpi7e2UrQcw99pLheXtQfDU9riT3oC3e_PHz9y0XjwUo8bwDF9re6RChxurh0tgHygcGCqWvfFb0Y9korGf6qKY4uhLTD9da2MNm9QjBuxeowQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
همزمان با ثبت رکورد ۹۹٫۷ درصدی تراکنش‌های موفق
سهم بانک کشاورزی از تراکنش‌های شتاب در سال ۱۴۰۴ به ۸ درصد رسید
🔻
بررسی عملکرد بانک کشاورزی در شبکه پرداخت الکترونیکی کشور طی سال ۱۴۰۴ نشان می‌دهد ۹۹٫۶۸ درصد از تراکنش‌های ثبت‌شده بانک با موفقیت انجام شده است. این امر در شرایطی محقق شده که در همین بازه زمانی، بانک کشاورزی ۷٫۷۸ درصد از مجموع تعداد تراکنش‌های شتاب را به خود اختصاص داده است.
🔻
جایگاه بانک کشاورزی در شاخص تعداد تراکنش‌های شتاب که بیانگر مقیاس فعالیت در شبکه تراکنش‌های بین‌بانکی است، نسبت به سال ۱۴۰۳ یک پله ارتقا یافته تا نشاندهنده روند بهبود موقعیت این بانک در شبکه پرداخت باشد.
🔗
مشروح خبر
🔶
🔶
🔶
@bank_keshavarzi</div>
<div class="tg-footer">👁️ 8K · <a href="https://t.me/farsna/461742" target="_blank">📅 10:27 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461741">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-footer">👁️ 7.73K · <a href="https://t.me/farsna/461741" target="_blank">📅 10:26 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461740">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eNpIspWXy49V79tOGsWJgkj5zZZfCcxRiBkJyB5_9ZoIloVcGG0FiE3BT130z6LFAGAfNuOAdLwIUTmXaaligJSRqXY8Xg5ZNCPTHqzPb59UU5JNXDQE_d3VYFuJelg5T1m3gR0hCtEhim5-QCgsLgnjGL31CDyHvndr1q-Zp1v0arP6VH1x9tXcM2F_4BJn_RFJJbX4joVHlRfSe5aGZouPCkEZHigpuPMT6IvJgwnRivynEuEIjQt6Bf1gxSD81RpcFEc3tJroYsjv8gC_SYSyMXIbq9Q5vhx-xlyK0eqwWPcrFxeZeTNkQizkY4c6rs1E9X9deB9cZ8Geriz4qQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پزشکیان: اگر دنبال سلاح هسته‌ای بودیم عضو «ان‌پی‌تی» نمی‌شدیم
🔹
رئیس‌جمهور در گفت‌گو با شبکۀ خبری ایندیا تودی هند: روابط ایران با همسایگان از جمله امارات، عربستان، پاکستان، قطر، روسیه و چین دوستانه است؛ مشکل اصلی پایگاه‌های آمریکا در منطقه است.
🔹
ایران آغازگر هیچ جنگی نبوده و تنها در برابر تجاوز آمریکا و اسرائیل از خود دفاع کرده است.
🔹
ایران به ان‌پی‌تی پایبند است و دنبال ساخت سلاح هسته‌ای نیست و برای گفت‌وگو در چارچوب قوانین بین‌المللی آماده است.
🔹
ایران به‌دنبال جنگ نیست، اما با تحریم، بستن راه‌های دارو و غذا و فشار بر مردم تسلیم نخواهد شد و تنها راه، توقف تجاوز و یک‌جانبه‌گرایی آمریکاست.
@Farsna</div>
<div class="tg-footer">👁️ 9.74K · <a href="https://t.me/farsna/461740" target="_blank">📅 10:14 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461739">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">اصابت پرتابه به کشتی ایرانی در تنگهٔ هرمز
🔹
فرماندار قشم: یک کشتی تجاری ایرانی ساعت ۵ امروز در حوالی جزیرهٔ هنگام و در محدودهٔ تنگهٔ هرمز هدف اصابت یک پرتابهٔ ناشناس قرار گرفت که تاکنون یک شهید و ۳ مجروح برجای گذاشته است.
🔹
هنوز نوع پرتابه‌ای که به این کشتی اصابت کرده، مشخص نشده است؛ بررسی‌ها دربارهٔ جزئیات این حادثه ادامه دارد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.64K · <a href="https://t.me/farsna/461739" target="_blank">📅 10:12 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461738">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7a0cf732cd.mp4?token=bz4KsSZAzuDytH1tE8MbAnO2RMX96l4lsqWiJw7HLCgEIH4LR4bCHYIlm2XwrMT0I0yYTY7ElPuafbmedT3xLQyEf2cxncdfsn8Uqnw0PlphhOvl-V4Q-83ZEkgv4uSPQ5OYCvUwuW_quLQSwYj7QxgbX9kabRSdTKITw82Je7xGD9J2YI7LcCk-LzoUDsAwIJnR5o1kqHPH4QnM16edEBRJQLG29dWqmiTFThksuFokOKJpyDL4btZNYPlRzOS1kenCEbB-mu36dNRbtC228x3B-ldOoWmZmDjpAKNYzRzGXd8yAgB0Z_gptAWFClJMSXT7xbO92jWPGU9TCCcDaA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7a0cf732cd.mp4?token=bz4KsSZAzuDytH1tE8MbAnO2RMX96l4lsqWiJw7HLCgEIH4LR4bCHYIlm2XwrMT0I0yYTY7ElPuafbmedT3xLQyEf2cxncdfsn8Uqnw0PlphhOvl-V4Q-83ZEkgv4uSPQ5OYCvUwuW_quLQSwYj7QxgbX9kabRSdTKITw82Je7xGD9J2YI7LcCk-LzoUDsAwIJnR5o1kqHPH4QnM16edEBRJQLG29dWqmiTFThksuFokOKJpyDL4btZNYPlRzOS1kenCEbB-mu36dNRbtC228x3B-ldOoWmZmDjpAKNYzRzGXd8yAgB0Z_gptAWFClJMSXT7xbO92jWPGU9TCCcDaA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پزشکیان: چندجانبه‌گرایی زمانی معنا دارد که همه در برابر قانون برابر باشند
🔹
حکمرانی جهانی زمانی مشروعیت خواهد داشت که صدای کشورهای درحال توسعه شنیده شود.
🔹
ما به‌دنبال جهانی هستیم که در آن قدرت جای قانون را نگیرد، تحریم جای همکاری را نگیرد، جنگ جای گفت‌وگو…</div>
<div class="tg-footer">👁️ 9.51K · <a href="https://t.me/farsna/461738" target="_blank">📅 10:00 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461737">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🎥
مرزهای چذابه و شلمچه در چه وضعیتی هستند
🔹
ساعتی پیش مرز چذابه برای اتباع عراقی بازگشایی شده، اما هنوز خبری از بازگشایی پایانهٔ عراق به‌سمت ایران اعلام نشده است.
🔹
با اعلام استانداری خوزستان مردم فعلا برای تردد در بخش تجاری و مسافری به مرزهای چذابه و شلمچه…</div>
<div class="tg-footer">👁️ 9.44K · <a href="https://t.me/farsna/461737" target="_blank">📅 09:56 · 22 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
