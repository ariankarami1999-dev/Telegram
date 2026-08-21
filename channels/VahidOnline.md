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
<img src="https://cdn1.telesco.pe/file/Yciq1n9apje3vp5r2Rd9BOBlmlha7oFDi_TQYtR_wcfjgb5diJ9gpJIJwT6EifdvQ53k_wznUWeVbLuuhRkyIvqhnnwG6-xAj8vDubdwwB-hBzkV_wO7bxM8jzyH0tGqM1Co_GCkKyZP2_Mh-LYELysxw6rPRigdl4DbkItOhbKe3KeNZBzaZOlXXFrs4G0l8NMPs1yhFIXx30qRjSY840YP_6Q8lwoWvntUmVjZUpOIh2rb8YtC3Mlli34oy8a7-xHKzIt5IaIkaNVy-IFX32H4MElW2teXEU9ATsLe9E2Ez5K18AnsiqfoG3vMNoVyu-BlWwhHb0d4CBsz5X7ayA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Vahid Online وحید آنلاین</h1>
<p>@VahidOnline • 👥 1.41M عضو</p>
<a href="https://t.me/VahidOnline" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پیام مهم:@Vahid_Onlineinstagram.com/vahidonlineتلاش می‌کنم بدونم چه خبره و چی میگن.اینجا بعضی از چیزهایی که می‌خواستم ببینم رو همون‌جورکه می‌خواستم به خودم نشون داده بشن می‌گذارم.به لطف حمایت‌های ماهانهvhdo.nl/patreonو گاهانهvhdo.nl/paypalممنونم</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-30 14:27:49</div>
<hr>

<div class="tg-post" id="msg-77976">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/KUDd0xV5x7m15V4npLjyHXnKsc9xnv0wCghrJO2F5iyidFV25Clz-fzuQeheIdS0f5TM7Y7DzGU3h4N5cjYO99vJpBYBmTF6BalpZnepyGd6zuA17no2OK5N5DxzfH4Yywr5CtsuPB9N9wJO0nSV0fIQ6kbsS1Mx34Rk-2xtfs0HzD215MFh5DYeMz9FfWFWsgJLwEFKOtYciGy5ECA_5E88zcZmaAkhIGuULsR6Z-_7ohbRSH0ydKm-OyDH3jM3IEt45V65CvSFrH9nTFU0IfSp8LyuiJ88q6mRX0o0Qq_g0100TWrIgNDWkVVc40qzjbaNYVZZpHZKPQ0YMfXeow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پس از «دونالد ترامپ» رییس‌جمهور ایالات متحده و «اسکات بسنت» وزیر خرانه‌داری آمریکا، «جی‌دی ونس» معاون اول ریس‌جمهور آمریکا از آغاز «مرحله جدیدی» از جنگ ایالات متحده و ایران خبر داد و گفت: «موثرترین ابزاری که برای اعمال بر حکومت ایران داریم، فشار اقتصادی است.»
جی‌دی ونس که در پادکست  «کلی تراویس اند باک سکستون» صحبت می‌کرد به «تعامل ظریف» بین دو کشور اشاره کرد و گفت: «ما به آنها فشار اقتصادی وارد می‌کنیم، آنها نیز سعی می‌کنند به ما فشار اقتصادی وارد کنند. اما آنچه در چند هفته گذشته واقعیت داشته این است که آنها فشار بسیار بیشتری نسبت به ما متحمل شده‌اند.»
به گفته معاون دونالد ترامپ آمریکا این روند را ادامه خواهد داد چرا که بر این باور است «این بهترین راه برای دستیابی نهایی به هدف نهایی» این کشور است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 231K · <a href="https://t.me/VahidOnline/77976" target="_blank">📅 01:47 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77974">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/e6E94iSOU6NkDUh7mwSXJ92EJcc2m6PC93wmHGtF_IFJspBvQWKmQZrBMDs8bTmgb3Qg1tFpmQQl4QCZqPUyZWB2m6gOQyXBv07_ufnCs7k4UTa_v7O0OLPVQXP1nK_w2fEVrq6dgYA1RVje0rd49Axsx9BN_mNZGLjw-aC-4uJZYHFeYM9swANEOSjxsqkz69CpoxEs6S3RxkDy7RpxbiMuqnmegWD6iEoNfDj5aSj4v2V6HZ4Th_1TSR5kbQlBLMHsJwFbhq8Wg5zmcVI4OnBfMd8gxISdSDlHWoOsosxJpUmh069ckUouKgvpIJ0ArwHGFAk1rhm2BeDbCihMwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/avo74U5X6XdXsho_kw9n8W2_r7sOBMrHGKX1AUIJIKTU6pvERucXocrvvmmMKRMTRqp7VKSV_J9oEozd8KeqlpLloIOmVuO2QAm7MP9gVRNpMBThATIEEyHeLWGac_R9PVm2IxSXg-TfQqyzMZ3ktGVeI882IWZ8FEajRONlQApGkQkspQjpDSZ7M18c64yHbWMquW3X_QPrXRAFFeUEPxfH3H48wwJCWucz6HyDwZa4wkalUVdAoGh89OsVo-esTnmi3xunbe2O1EGzPkkb05fZ1pUCMmU1ud9VhLmAmGRLx1dLxZ_ZFgYeT-SwOtka0hYFA86p6s0WiObIrF9DyA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">انتشار تصویری از محمدباقر قالیباف، رئیس مجلس ایران، در جریان سفرش به عراق که در پس‌زمینه آن عبارت «خلیج فارس» دیده می‌شد، واکنش همتای عراقی او را در پی داشته است. هیبت حلبوسی چند ساعت بعد تصویری مشابه از خود منتشر کرد که در پس‌زمینه آن عبارت دیگری دیده می‌شد.
@
VahidOnLive
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 220K · <a href="https://t.me/VahidOnline/77974" target="_blank">📅 01:46 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77973">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Nbtl60wvOcwfBLy82o7jFAF8wNmGG2HejHSEJapvaeJVRzKGulQY6vC39v-mwxepBHIUzHMLLgrfL4W-Zx_gGsTY5fUwP2L4DiNz97jLwKkGnywwisZcnWgr9hPXIXoXze98dL8VBFeu9wMvgfTCZsXTx9N-XU2SbMplko3wCpkr_JfEDAHdik7SCzK9a0LG9acv8mmUB3Pqs23EJgtMLSaqyf0Q0nieVU8pOJCkDhA-ajuZ9c2Tzqh0SBC9z7v-MpaOXa5StuQHC3rWEjoD07pHGzAZVO8V8KOc7BQFIRbwwTW7QgVCmWB1SSirLRTFUTNwheaQy0imNZl3HRCJbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسکات بسنت، وزیر خزانه‌داری آمریکا، روز پنجشنبه ۲۹ مرداد گفت طرح واشینگتن برای افزایش شدید تحریم‌های اقتصادی علیه ایران با هدف «سرنگونی» حکومت جمهوری اسلامی دنبال می‌شود.
بسنت در گفت‌وگو با شبکه سی‌ان‌بی‌سی گفت: «این طرح در ایران جواب خواهد داد و ما این رژیم را سرنگون خواهیم کرد.»
او افزود: «این بزرگ‌ترین انزوای اقتصادی هماهنگ‌شده در تاریخ جهان خواهد بود.»
وزیر خزانه‌داری آمریکا روز ۲۳ مرداد نیز خبر داده بود دولت دونالد ترامپ قصد دارد اقداماتی در مقابل ایران انجام دهد که به گفته او «در تاریخ انزوای اقتصادی یک کشور بی‌سابقه بوده است».
او گفت: «اگر ما حداکثر فشار اقتصادی را اعمال کنیم، به احتمال زیاد دیگر شاهد ازسرگیری یک عملیات نظامی گسترده نخواهیم بود؛ اما تأکید می‌کنم که این وضعیت مربوط به حالا است.»
اسکات بسنت همچنین خبر داد که روز دوشنبه هفته آینده یک نشست خبری برگزار خواهد کرد تا «دقیقاً درباره اقداماتی که قرار است انجام دهیم» در قبال ایران توضیح دهد.
هشدار به متحدان آمریکا
وزیر خزانه‌داری آمریکا همچنین در پی اعلام طرح جدید دونالد ترامپ، رئیس‌جمهور آمریکا، برای تشدید فشار اقتصادی بر ایران، به متحدان واشینگتن هشدار داد که در موضوع انزوای اقتصادی ایران باید میان «همراهی با آمریکا یا قرار گرفتن در برابر آن» یکی را انتخاب کنند.
او دربارهٔ پیام خود به متحدان آمریکا گفت: «این بزرگ‌ترین انزوای اقتصادی هماهنگ‌شده در تاریخ جهان خواهد بود. ما به آنها می‌گوییم که یا با ما هستید یا علیه ما.»
وزیر خزانه‌داری آمریکا در پاسخ به پرسشی دربارهٔ احتمال اعمال فشار واشینگتن بر چین نیز گفت: «بسیاری از گفت‌وگوها بهتر است در خفا انجام شوند»، اما همزمان از پکن خواست «با این برنامه همراه شود.»
او گفت: «ما اطمینان داریم که همه خواهان بازگشایی تنگه هرمز و کاهش دوباره قیمت انرژی هستند.»
بسنت در ادامه با اشاره به وابستگی چین به نفت خلیج فارس افزود: «در نظر داشته باشید که ۵۰ درصد انرژی چین از داخل خلیج فارس تأمین می‌شود. بنابراین، همراه شدن با این برنامه می‌تواند خدمت بزرگی به خود آنها باشد.»
این اعلام موضع وزیر خزانه‌داری آمریکا یک روز پس از آن است که رئیس‌جمهور ایالات متحده اعلام کرد که کارزار جدید و بزرگی را برای هدف قرار دادن اقتصاد ایران به راه انداخته است.
دونالد ترامپ شامگاه چهارشنبه در شبکه اجتماعی خود، تروث سوشال، نوشت: «امروز، من کوبنده‌ترین عملیات اقتصادی‌ را که تاکنون علیه کشوری انجام شده است، اعلام می‌کنم! این یک جنگ و انزوای اقتصادی در مقیاسی بی‌سابقه خواهد بود».
او افزود: «همچنین اعلام می‌کنم که هر کشوری که به نهادهای مالی، کسب‌وکارها، فرودگاه‌ها یا ارگان‌های دولتی خود اجازه دهد هرگونه راه نجاتی برای ایران فراهم کنند، خود با عواقب اقتصادی بسیار سنگینی روبه‌رو خواهد شد».
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 271K · <a href="https://t.me/VahidOnline/77973" target="_blank">📅 20:18 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77968">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/dNcZeb1sMSQg67y4oFH67NEA9TN83svjFUI7C4CbjC4OcXMTdnLW-DHjSN-0eoyEw7sZdo71Q2aH3J8SXzweaRgNZHoV_-99GPWgnCz3v77TAYmh80QR5r4LhlN75aHSbeWQrZdWNASr6PhZJwjv_CU4BKTnxOxFtxfAWlfOQY_VR0PRKiwy8TE8aTKlcXGQ5XWeHox5ECAaDcw3O9fUJdI57EYnhJERw-lgcnl7VOd0ByH7BPEpNsqskS1m35Ex3TfyrViU7u03SoKC6oGzaw-Nb_9HvgS0nc15oTPWkz6MXroW1H-a_4utlJr7NxFZj_XiYKoC2hnuoSbf-P_jJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/GM0jp2dSzrryA8mKO5FpEELqy_ZtOyDQqq3xE89d7MRoLeJshQLJrGy2ENdZkMp8TR0L-JXHkX5eInXiTc8duyDnxWZa6qIUEEXsgzGHKvfWTRGwnFESrqbHBTfuyhS8yEbG0TnGUMeIqlRd2bA8byIoByF04fq3K7-YkDO1m3TIZX8neK3MMbD4iwAXZtBGvqZc_Wv68Qt8B8HESIC0H12NzFg8m4cPyDbliu2_jsj3ffJ0RVvnb64rzKp22mgdUlhtPTnTdJx8suyhZ35LQNyv6cCnxX06AgnHPlIKSNw5ifPfG63DT02kVV75SsHz9031xtT3yAwBpR3iERGqRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/as5q7hD6B0jv62rZWLdRR5aQk9eRsAev_92ra9evFTAZiAS6oww9cjlCBfOYaDgPcmtJxiey_qP-l472ts-r6VPJRr0YLLAgieaSULsf89cTjyZEiMiESNrPr1yogNIKHS8pCyaWRXc7JPBjWKT7HZWYci3sr_xbWxaGdJ23MN_C6KE5KLbNZFzuYVRC-9IGDRcVjUb17eDT237Byd_umEFYJcJwx81jy2XQ2Jz827-RHWVitz9IQTiazfzTZqTSRgE9MUnQ5fYYG-P7z9O_H9wQivrz3jyQ_e49yw5uF8FiXCZ8o46K8g-MxrGzcgnCWeg_3J5wpyxVPAl5FvIReA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/5e50a342f2.mp4?token=uczdPQaoArVNPjohga7-9iD5BjgGfFqTQPxoxYHoZ7tLOjfP9z9S135vH9h7weSRyY1VCKUAviy08fqIoFu2x9KsjDIFQVVsvQcBp8w-5GXupNGXEWDGWngTuYsWTujvFdTLV-ZPWkph2IiAuJnbAwohO-nGFoNiQCHNqe4S43X3u8OvJ9vC7A_ldJAEw4ioMGHocvlrYYyNwfvn0SWhQiuPS1gYhiNtbw80vsEYrqzTMZBN9j_fVOPyAxKC1c0DIxmSYPilAhzU_1p7wmt5I4fRKITLLJRUmPnwkVZb0gV78pVloGyp_ZQCHCrXGnw9oWNCOfiJuroR8rW42GbeEnP225LPaIzRPt8CQ15AJtb3skKv8_Wsu-PMypqPF16tWHloC3y8B6ICc9yy93j3k2738yG0kJ6QawwbqLN7FBtA8BxoXAOKbLeHtQWpB0df8MElzKJuyRKldjCcvc5ijlL1Yz02FIifcZzkDVjqpa1sYhQMJZck3YH8muZ8LsT-8d-uQ2j0mn3Br5EGO3YSGGulIDxZlK5RovAwLobaYYFuPX8k6ag6v5F2QFMIWdN3FF1H774xYhdWWRUiF8mGilHuhDMKAJfgXTynS8f5CKCA7_ovaRHD-NU9rXrzwd_S_-vm6q1wxSi6qeQU4h5o6RwDiGhbQdbiSa81-XmsJ0A" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/5e50a342f2.mp4?token=uczdPQaoArVNPjohga7-9iD5BjgGfFqTQPxoxYHoZ7tLOjfP9z9S135vH9h7weSRyY1VCKUAviy08fqIoFu2x9KsjDIFQVVsvQcBp8w-5GXupNGXEWDGWngTuYsWTujvFdTLV-ZPWkph2IiAuJnbAwohO-nGFoNiQCHNqe4S43X3u8OvJ9vC7A_ldJAEw4ioMGHocvlrYYyNwfvn0SWhQiuPS1gYhiNtbw80vsEYrqzTMZBN9j_fVOPyAxKC1c0DIxmSYPilAhzU_1p7wmt5I4fRKITLLJRUmPnwkVZb0gV78pVloGyp_ZQCHCrXGnw9oWNCOfiJuroR8rW42GbeEnP225LPaIzRPt8CQ15AJtb3skKv8_Wsu-PMypqPF16tWHloC3y8B6ICc9yy93j3k2738yG0kJ6QawwbqLN7FBtA8BxoXAOKbLeHtQWpB0df8MElzKJuyRKldjCcvc5ijlL1Yz02FIifcZzkDVjqpa1sYhQMJZck3YH8muZ8LsT-8d-uQ2j0mn3Br5EGO3YSGGulIDxZlK5RovAwLobaYYFuPX8k6ag6v5F2QFMIWdN3FF1H774xYhdWWRUiF8mGilHuhDMKAJfgXTynS8f5CKCA7_ovaRHD-NU9rXrzwd_S_-vm6q1wxSi6qeQU4h5o6RwDiGhbQdbiSa81-XmsJ0A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مادر پرنیان دبیری با انتشار ویدیویی گفت دختر ۱۶ ساله‌اش پس از اصابت گلوله به کهریزک منتقل شد و پیکرش در محوطه این مرکز روی سطح آسفالت قرار داشت.
او همچنین گفت هنگام پیگیری تحویل پیکر دخترش، یکی از ماموران با قنداق تفنگ به او ضربه زد و تهدید شد که در صورت ادامه اعتراض، پیکر پرنیان تحویل داده نخواهد شد.
او خواستار پاسخگویی عاملان کشته‌شدن دخترش شد.
این جاویدنام ۱۹ دی ۱۴۰۴ همراه پدر و مادرش در خیابان بود و از پشت سر با گلوله جنگی سرکوبگران هدف گرفته شد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 274K · <a href="https://t.me/VahidOnline/77968" target="_blank">📅 16:07 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77966">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/HESvSMcfb2dGxCqjZ00tT8u_kJnY3RCDp1F1h78P2hmPJZ5aNASbRkiLK3XSneQjaeOwVLU5XeaVSDF2_QkFSwmtb2qLmYGzPiPFl8WRXfc_xs0t6f8P_m6W943Qz4BElLhbzJTMAy4rjuKS7ZvSfQu5g999UZi4c-dLsJ7AdcqoGRoERLQaSxkaTgf7qMgfZkg1lmuuok6APFG43Vu3gYl7adrI-NrjrTYZXrdMepjmbFilPWcDc95kY411QDhH9OwDOsHgtOzAj54HWBjUW_h6X3IaQ7N-XYOq3nNdmJClIbe1EY3B12EICJVFayBhDWIf4_d2Z-t1eifgzKyTeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/lIOEI878p7YTW0jvg83HKqEaIgc__VA85XxITbfTJzz8bPujLQvg-CSBksKtXVPVTM21kOEiwM8FwMwXM37n64xlhJd9cg2gQWWlb0bLsYF9h8q8kEvuZ-7UpV0uIPydBVYxDenNE8c_yBj4LaM9LvGwet_cJWZ6X5dAOUvDvlfRUr-OddbJNgISsi_PTjzwxm0gHmeTVzfCIP9wsiMVB5qlw6Mz4pXxm2InJDinAdArPQIDsGfbxo5NEbsBZyta4FMlopFIYcyxL_9PbOs63LZWJH_psD71PExo3w0cbf4Q56DImQLYX9xSTEmCHmhVNLOEMWjjiOyAUmv3jg_SGQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">عباس عراقچی، تهدید دونالد ترامپ مبنی بر آغاز کارزار اقتصادی گسترده موسوم به «روز دی اقتصادی» علیه ایران را تلاش برای سرپوش گذاشتن بر «بحران‌های داخلی آمریکاست» توصیف کرد و از «بدهی‌های بی‌سابقه و هزینه‌های فزاینده نرخ بهره» به عنوان نمونه‌هایی از این بحران‌ها نام برد.
@
VahidOOnLine
معاون وزیر امور خارجه جمهوری اسلامی ایران سخنان ترامپ در مورد کارزار «روز دی اقتصادی» علیه ایران را تلاش «محاسبات غلطی» خواند که برای پوشاندن «شکست‌ بزرگتری» ساخته شده است.
کاظم غریب‌آبادی نوشت: «ادعا می‌کنند ایران در آستانه شکست است و به یک نخ بند است، اما به همه متحدانشان التماس می‌کنند که کمکشان کنند.»
معاون وزیر امور خارجه ایران در ادامه افزود: «جنگ نظامی نتیجه نداد، حالا اسم شکست بعدی را جنگ اقتصادی گذاشته‌اند.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 259K · <a href="https://t.me/VahidOnline/77966" target="_blank">📅 15:32 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77963">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/2ab9ff1cf5.mp4?token=SfU7OVUwfQsXqm9VLBArrVKkeyqkRJRoB7ZzfoArdRVPPXU0YiHra7mdqNYfimZe-exRryJK1sJcfsnrQjaI95Jq6pSwum8PzjgqkHL2tAFc4JLwrEY3KjH7PkhiJoD6S3A6EyoKiZE5GQN8ywKqgIEiQxMNadxO5wbbGzboppgqM5prUj_wmRfYSid2B_xNY_AhtVJAN23BTDHmjPVbl5l6SVxQiefeoX5VKfgIHmQxgk2vhOO2xCKUwPEMhKr_PhZ7YUcJRcK3omCilCEZl78oSw68FGFvhV6U8IE9bYZb47MegJ4o2DrKtXniR2vcCw5mPz483zCw_EcHgES-cQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/2ab9ff1cf5.mp4?token=SfU7OVUwfQsXqm9VLBArrVKkeyqkRJRoB7ZzfoArdRVPPXU0YiHra7mdqNYfimZe-exRryJK1sJcfsnrQjaI95Jq6pSwum8PzjgqkHL2tAFc4JLwrEY3KjH7PkhiJoD6S3A6EyoKiZE5GQN8ywKqgIEiQxMNadxO5wbbGzboppgqM5prUj_wmRfYSid2B_xNY_AhtVJAN23BTDHmjPVbl5l6SVxQiefeoX5VKfgIHmQxgk2vhOO2xCKUwPEMhKr_PhZ7YUcJRcK3omCilCEZl78oSw68FGFvhV6U8IE9bYZb47MegJ4o2DrKtXniR2vcCw5mPz483zCw_EcHgES-cQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عبدالناصر همتی، رئیس بانک مرکزی ایران، در یک گفت‌وگوی تلویزیونی تأیید کرد که صادرات نفت ایران در حال حاضر متوقف شده است.
او شامگاه چهارشنبه ۲۸ مرداد اظهار امیدواری کرد که تفاهم‌نامهٔ ایران و آمریکا احیا و مذاکرات از سر گرفته شود.
این نخستین بار است که یک مقام رسمی جمهوری اسلامی به شکل رسمی از «توقف» صادرات نفت ایران خبر می‌دهد.
در هفته‌های اخیر برخی مقام‌های جمهوری اسلامی با اشاره به تشدید بحران اقتصادی و معیشتی، نسبت به دور تازه اعتراض‌ها هشدار داده و از آمادگی برای برخورد با آن خبر داده‌اند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 244K · <a href="https://t.me/VahidOnline/77963" target="_blank">📅 15:28 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77962">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/r6tvSEBz49r2tUAZnhjl30qbEE1_rooAVK8HKD1PJL4nozSYuZFMQbpP7_M8To_VzT8MCJWoUomIu46Viu3E8u_DueFsyxAnPJS-cjKwaZe5lWeq-5zeqk3c27jef_hKkEWtaeM7oQxR8agmOqYk3P1jAUPbV9YmZScjHKSoPcqd4vPjM59otJC77mZpTYm6TRLSZeUbfzAkwk4MFHKBhEClS5trMu2zxR4Yagn3wCxz9llGIE9UafhKDGaEtJc84WI-ouqC1jD1hAtSyFLVQi2y1MeeowwG319M3TvCrdb4NJKvDWgdNHBFy_Ehtlu7_rK0XtqJa42tyDvR9LBmGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قوه قضاییه جمهوری اسلامی صبح پنج‌شنبه ۲۹ مرداد ۱۴۰۵ «قائم حسینی»، معروف به «آرین»، را در ارتباط با اعتراضات دی‌ماه اصفهان اعدام کرد. او پنجمین فردی است که در پرونده موسوم به «میدان علیخانی» اعدام می‌شود.
خبرگزاری میزان، ارگان رسانه‌ای قوه قضاییه، حسینی را «تبعه خارجی» معرفی کرده، اما تابعیت او را اعلام نکرده است. در این گزارش همچنین اطلاعاتی درباره زمان بازداشت و محل نگهداری منتشر نشده است.
قوه قضاییه حسینی را به «دخالت در وقایع میدان علیخانی اصفهان»، کشیدن سلاح، ایجاد رعب‌ووحشت و ناامنی گسترده و اقدام علیه امنیت ملی متهم کرده بود. براساس گزارش رسانه‌های حکومتی، حکم اعدام او پس از بررسی فرجام‌خواهی در دیوان عالی کشور عینا تایید و اجرا شده است.
قوه قضاییه پیش‌تر «ابوالفضل سپاهی»، «امیرحسین صفری»، «عرفان اسفندیاری» و «گل‌محمد محمدی» [پسرعمه قائم حسینی] را در ارتباط با همین پرونده اعدام کرده بود. همچنین میزان اعلام کرده بود که برای ۱۶ نفر در این پرونده کیفرخواست صادر شده است.
شروین باقریان، امیرحسین ملکی و علیرضا سپاهی، سه محکوم دیگر این پرونده‌اند که درباره احکام نهایی و وضعیت کنونی آن‌ها اطلاعات شفافی منتشر نشده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 258K · <a href="https://t.me/VahidOnline/77962" target="_blank">📅 15:19 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77961">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/MQ-oiJnyCD-6o0yvOR-qyvHb-_Wm5G-faHWh0wSqJl1_fEkfhKDnCxh7SUpFSVupP6SN9Ug-J83WnonqR-NqC7mhbDvr2afIFqYuTD3zvplDGFIFXDOXCl5WgGn-9BNUTy_Dhkf1Jicnb8uSVcYA3EytR-EM-Upi2TRreL6oRPvUq5nBOglS6qi6KsAkf3PCFiy_r7fZouW5TNNiabiXp2tRzN3DWy7W9K7huXyflo5yjJ8pNo3xST0msNLVPrxNstKI9R_gIAFbdZtnEwRidGR-f82BzAvEdkf28gqB5lMwFlkd3rKB4Nk9ORtsZlW5rl3Wvz052dMWQEI4AIUwsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">☄️
ترامپ:
هیچ‌کس بیش از من به جمهوری اسلامی ایران فرصت بزرگی برای رسیدن به یک توافق نداده است. به‌طرزی فاجعه‌بار برای خودشان، نتوانستند از آن استفاده کنند.
بنابراین، امروز اعلام می‌کنم که
کوبنده‌ترین عملیات اقتصادی‌ای که تاکنون علیه هر کشوری انجام شده است، آغاز خواهد شد!
این، جنگ اقتصادی و انزوا در مقیاسی بی‌سابقه خواهد بود.
نیروی دریایی‌شان از بین رفته، نیروی هوایی‌شان نابود شده، کارخانه‌های نظامی‌شان اکنون به تلی از آوار تبدیل شده، پولشان بی‌ارزش است و کشورشان به مویی بند است.
امروز همچنین اعلام می‌کنم که
هر کشوری
که به مؤسسات مالی، کسب‌وکارها، فرودگاه‌ها یا نهادهای دولتی خود اجازه دهد هر نوع راه نجاتی برای ایران فراهم کنند، خود با
پیامدهای اقتصادی عظیمی
روبه‌رو خواهد شد.
قاچاق نفت، خطوط سوآپ، انتقال پول نقد، صرافی‌ها، ثبت کشتی‌ها، شرکت‌های پوششی — همه این‌ها باید
همین حالا
متوقف شوند. خودتان می‌دانید چه کسانی هستید.
این یک
D-Day  اقتصادی (ECONOMIC D-DAY)
خواهد بود و ما به همه متحدانمان نیاز داریم که در کنار ایالات متحده آمریکا بایستند تا تهدید ایران را منزوی و شکست دهند.
این دیوانه‌ها به آخر خط رسیده‌اند و این اقدامات تاریخی آنها و توانایی‌شان برای گسترش ترور در سراسر جهان را فلج خواهد کرد.
ایران هرگز سلاح هسته‌ای نخواهد داشت.
از توجه شما به این موضوع سپاسگزارم.
رئیس‌جمهور
دونالد جی. ترامپ
realDonaldTrump
توضیح چت‌جی‌پی‌تی: D-Day در اصل اصطلاح نظامی برای «روز آغاز یک عملیات بزرگ» است، اما در کاربرد عمومی تقریباً بلافاصله عملیات نرماندی در ۶ ژوئن ۱۹۴۴ و آغاز تهاجم گسترده متفقین در اروپا را تداعی می‌کند. بنابراین ترامپ با گفتن ECONOMIC D-DAY می‌خواهد بگوید این اقدامات اقتصادی قرار است چیزی شبیه یک حمله بزرگ، تعیین‌کننده و همه‌جانبه در جنگ اقتصادی باشد.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 330K · <a href="https://t.me/VahidOnline/77961" target="_blank">📅 02:33 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77960">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">Vahid Online وحید آنلاین
pinned «
⚠️
تبلیغات خطرناک فیلترشکن
⚠️
من  فیلترشکن و VPN تبلیغ نمی‌کنم. کلا هیچ تبلیغاتی انجام نمی‌دم. تبلیغاتی که اینجا دیده میشن به خود تلگرام سفارش داده میشن و من ازشون بی‌خبر هستم.  به نظر میاد همه تبلیغات هم کلاهبرداری باشند به ویژه اگر درباره فیلترشکن و فعالیت…
»</div>
<div class="tg-footer"><a href="https://t.me/VahidOnline/77960" target="_blank">📅 01:15 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77959">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/XF40wNhaVcHsIByLUznulme6K5RW7CcETys0d1UI6AQlW92jB1prI68RiZ6S10sfLwM6aLE1CbZl4fWtSmgWT2XoaSQBscy-D60S-5kTMhl5U0PYd89LHmvJByOlYugApR9s9W0eFT-GoKnt8N1y0dD8chhFh9YXUFjNTFkvL4ytk9z_Em5nmWYH0AQqChMURPdYo5IEakibNhcESABYE6c7TSyzMrNJ8xfmV99NrMFhBzSmS51IO1hrAzPBywNLPCCq7qKZ9YSaxr7SISMd6U8x5hS_2dTUobG9esGtZKRQUEezUNwoG3_4LPyEJi2pFd9-6lSxaYq5xEQhU0Q81A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وبسایت اکسیوس، روز چهارشنبه ۲۸مرداد ۱۴۰۵، گزارش داد، ارتش آمریکا طی هفته‌های گذشته یک مسیر کشتیرانی تحت کنترل خود در بخش جنوبی تنگه هرمز ایجاد کرده که امکان انتقال روزانه میلیون‌ها بشکه نفت به بازار جهانی را فراهم کرده است؛ اقدامی که به گفته دو مقام آمریکایی، بخشی از اختلال ایجاد شده در صادرات نفت در جریان جنگ را کاهش داده است.
این دو مقام آمریکایی به اکسیوس گفتند در چارچوب این عملیات، هر شب حدود ۱۵ تا ۲۰ نفتکش از مسیر جنوبی تنگه هرمز و در امتداد ساحل عمان وارد یا خارج می‌شوند. به گفته آنها، اکنون حدود ۱۰ میلیون بشکه نفت در روز از طریق این مسیر از تنگه خارج و وارد بازار جهانی می‌شود؛ رقمی که تقریبا نیمی از حجم انتقال نفت پیش از جنگ است.
به نوشته اکسیوس، عملیات آمریکا تنها به اسکورت نفتکش‌های حامل نفت محدود نمی‌شود. نیروهای آمریکایی نفتکش‌های خالی را نیز از دریای عرب از مسیر تنگه هرمز وارد خلیج می‌کنند تا این نفتکش‌ها پس از بارگیری نفت در بنادر کشورهای منطقه، دوباره از مسیر جنوبی تنگه خارج شوند.
یکی از مقام‌های آمریکایی که از نزدیک در جریان این عملیات قرار دارد، گفت آمریکا حدود دو ماه است مسیر جنوبی تنگه هرمز را تحت کنترل دارد. او افزود سپاه پاسداران ممکن است برای کشتی‌ها «مزاحمت» ایجاد کند، اما کنترل تنگه را در اختیار ندارد.
بر اساس این گزارش، عملیات انتقال نفت از سوی یک گروه ویژه مستقر در مقر ارتش آمریکا در فورت براگ در ایالت کارولینای شمالی هماهنگ می‌شود. این گروه با کشورهای عرب منطقه همکاری دارد و هر روز فهرستی از کشتی‌هایی که قرار است از خلیج فارس وارد دریای عرب شوند و همچنین نفتکش‌های خالی که برای بارگیری نفت وارد خلیج می‌شوند، تهیه می‌کند.
کشتی‌ها هر شب در دو بازه زمانی مشخص، در قالب دو کاروان جداگانه برای ورود و خروج از تنگه حرکت می‌کنند و با هدایت نیروهای آمریکایی از مسیر جنوبی عبور می‌کنند. جنگنده‌های نیروی هوایی آمریکا نیز برای مقابله با موشک‌های کروز و پهپادهای ایران از این عملیات محافظت می‌کنند.
به گفته مقام‌های آمریکایی، ایجاد این مسیر پس از یک عملیات دو هفته‌ای فرماندهی مرکزی آمریکا، سنتکام، علیه سامانه‌های راداری و نظارت دریایی ایران امکان‌پذیر شد. در نتیجه این عملیات، توان ایران برای رصد تردد کشتی‌ها در مسیر جنوبی تنگه هرمز کاهش یافته است.
مقام‌های آمریکایی می‌گویند ایران اکنون برای نظارت بر این مسیر عمدتا به چند رادار بازسازی‌شده و نیروهای مستقر در قایق‌های تندروی سپاه متکی است. به گفته آنها، کاهش توان رصد باعث شده است حملات پهپادی و موشک‌های کروز ایران بیشتر به سمت مناطقی انجام شود که احتمال می‌رود کشتی‌ها در آن تردد داشته باشند.
اکسیوس گزارش داده است که شماری از کشتی‌ها در حملات ایران آسیب دیده‌اند، اما نیروهای آمریکایی نیز تعدادی از حملات را رهگیری کرده‌اند. به گفته یکی از مقام‌های آمریکایی، نیروهای این کشور در اوایل هفته جاری هشت پهپاد و دو موشک کروز ایرانی را سرنگون کردند.
بر اساس این گزارش، طی دو هفته گذشته هر شب ۱۵ تا ۲۰ نفتکش از مسیر جنوبی تنگه هرمز عبور کرده‌اند و میانگین انتقال روزانه نفت اکنون به نزدیک ۱۰ میلیون بشکه رسیده است. مقام‌های آمریکایی می‌گویند در برخی شب‌های هفته‌های اخیر، حجم نفت خارج‌شده از خلیج فارس به ۱۵ تا ۲۰ میلیون بشکه نیز رسیده است.
به گفته یکی از این مقام‌ها، در یکی از شب‌های این هفته بیش از ۲۰ کشتی برای عبور از مسیر جنوبی تنگه برنامه‌ریزی شده بود و در صورت اجرای کامل برنامه، حدود ۱۵ میلیون بشکه نفت از خلیج خارج می‌شد.
دونالد ترامپ، رییس‌جمهوری آمریکا، نیز در گفت‌وگو با اکسیوس گفت «حجم بسیار زیادی نفت» از تنگه هرمز خارج می‌شود. او در عین حال گفت آمریکا در حال حاضر با ایران مذاکره نمی‌کند و افزود جمهوری اسلامی در مذاکرات «وقت تلف می‌کند».
ترامپ همچنین گفت ایران هنوز توان مقاومت دارد، اما در مجموع «بسیار ضعیف‌تر از گذشته» شده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 296K · <a href="https://t.me/VahidOnline/77959" target="_blank">📅 01:12 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77958">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/1a65b09283.mp4?token=BzSSIXlZ3WtWdwUL_HXKh7BEwUiCc2e_87gxNFPwbpssIPNp-4dI3MXYv6s4Z7y5E4ZMCd3Uvvunh5WOes_Yo5u20yn218YJXV3buQnVgCwPQW2nflYfdfZKWUvmj_bb_fr6p_KKn-HFA6xzT0Z1B9s9LHsQe6BTzoQgBAdgVXSYvE4c7ACpded1y3AqupWosA36USj1GqbJy71vJT8sfhNp6vYO1wmEPNMNH-rc2bIRMPofEYACJt6_sA7uPm7yFJH4GwabWhmuIBKQOf2-nsg9_p8BMt7hISZoqh-j7bs2G_bUXN8AUX1KsQNerp79tj-nvfCXajstLTVJZF-BeQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/1a65b09283.mp4?token=BzSSIXlZ3WtWdwUL_HXKh7BEwUiCc2e_87gxNFPwbpssIPNp-4dI3MXYv6s4Z7y5E4ZMCd3Uvvunh5WOes_Yo5u20yn218YJXV3buQnVgCwPQW2nflYfdfZKWUvmj_bb_fr6p_KKn-HFA6xzT0Z1B9s9LHsQe6BTzoQgBAdgVXSYvE4c7ACpded1y3AqupWosA36USj1GqbJy71vJT8sfhNp6vYO1wmEPNMNH-rc2bIRMPofEYACJt6_sA7uPm7yFJH4GwabWhmuIBKQOf2-nsg9_p8BMt7hISZoqh-j7bs2G_bUXN8AUX1KsQNerp79tj-nvfCXajstLTVJZF-BeQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔺
خبرنگار: وزیر خزانه‌داری می‌گوید ممکن است همین هفته شاهد اثرگذارترین تحریم‌ها علیه ایران باشیم. این تحریم‌ها چه زمانی اعمال می‌شوند و چه چیز دیگری ممکن است در ایران تحریم شود؟
🔻
ترامپ:
خب، چیزهایی داریم که می‌توانیم تحریم کنیم. ما تحریم‌های بسیار سختگیرانه‌ای داریم و خواهیم دید چه می‌شود.
در حال حاضر، تنگه باز است. کشتی‌های زیادی در حال عبورند. این را گزارش نمی‌کنند و ممکن است در مقطعی کمی کند شود، اما همین حالا تعداد زیادی از کشتی‌ها در حال عبورند.
محاصره دریایی بسیار مؤثر بوده است. صفر. یعنی واقعاً، تا وقتی برقرار بوده — و مدت زیادی هم هست که برقرار است — به‌جز یکی دو وقفه کوتاه که عمداً آن را بر اساس یک توافق باز کردیم. اما آن توافق به نتیجه نرسید. می‌دانید، توافق آن‌طور که آنها گفته بودند از آب درنیامد؛ وقتی یک چیز به ما می‌گویند و کار دیگری می‌کنند.
اما محاصره ۱۰۰ درصد موفق بوده است. هیچ کشتی‌ای وارد ایران نشده، اما کشتی‌ها برای جاهای دیگر وارد می‌شوند. خواهیم دید. خواهیم دید چه می‌شود.
یا اوضاع بسیار خوب خواهد شد و قیمت نفت مثل سنگ سقوط خواهد کرد، یا دقیقاً همان کاری را که داریم می‌کنیم ادامه می‌دهیم. می‌دانید، از ۳۵۰ دلار برای هر بشکه حرف می‌زدند و امروز ۸۴، ۸۵ دلار است و ما داریم نفت زیادی استخراج می‌کنیم.
اما اتفاق دیگری که افتاده این است که مردم گزینه‌های جایگزین دیگری پیدا کرده‌اند که هرگز به آنها فکر نمی‌کردند: تگزاس، آلاسکا، لوئیزیانا و جاهای دیگر. علاوه بر این، تعداد بی‌سابقه‌ای خط لوله در حال ساخت است. بنابراین فکر می‌کنم تنگه هرمز دیگر به آن اندازه که در گذشته اهمیت داشت، مهم نخواهد بود.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 267K · <a href="https://t.me/VahidOnline/77958" target="_blank">📅 01:10 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77957">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/v_jgPdp3wxoAmgfq2Bpl7EX7TvBrZfsc9dURQMzPpdorM-qVnxP0NPYmoP9oUc7EOxodYh4FpSirIUjOO5jlyErIhSPu9mPT_l73jODAEq1CCTT4U6VcwWjh2MNQsq3_Xz8C5oM55ZcYTLZaf2rUKr-GZG9YDHyIeFr902U6BDsX_Gt_jOCNcYyL4BSmz43rq4OaHZwpC2rDb-QNta30iG_9NAont3qSXIn6GCB2N1dIYaBaM4rIjgSOh31y8ehtHaECSpqidZqG_E6IbHhfjpjH_Vx3va9VAy3wx4DdT3VkzZ-3IOgYBvfG8da9zvInz4zNVP4fZLNGudyWKRepNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دولت فرانسه روز چهارشنبه نیلوفر شادمهری، رایزن فرهنگی سفارت ایران، در این کشور را اخراج کرد.
ساعاتی پیشتر وزیر امور خارجه فرانسه رسما خبر داده بود که به عنوان اقدام متقابل دو وابسته سفارت ایران را از فرانسه اخراج خواهد کرد.
هنوز نام و سمت فرد دوم که از فرانسه اخراج خواهد شد اعلام نشده است.
پس از آن که وزارت خارجۀ ایران در بیانیه‌ای دو تن از کارکنان پیشین سفارت فرانسه در تهران را عنصر نامطلوب اعلام کرد، فرانسه نیز از اقدام متقابل درباره دو دیپلمات ایرانی خبر داد.
در بیانیه وزارت خارجه ایران آمده بود که با توجه به «فعالیت‌های خلاف حقوق بین‌الملل، به‌ویژه کنوانسیون روابط دیپلماتیک ۱۹۶۱» از سوی دو مامور شاغل در سفارت فرانسه، این دو فرد عنصر نامطلوب شناخته شده و حق بازگشت به ایران را نخواهند داشت.
طی روزهای اخیر مشخص شده که این دو فرد، از کارکنان بخش فرهنگی سفارت فرانسه بوده‌اند و ظاهراً در ارتباط با پروژه‌ای فرهنگی، با دو گرافیست ایرانی دیدار کرده بودند.
این دو گرافیست هم از همان زمان در بازداشت هستند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 279K · <a href="https://t.me/VahidOnline/77957" target="_blank">📅 23:01 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77956">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/168f12d8a1.mp4?token=AqYTe0g7SmSBoqyQzDfGxTiQI1vO5OmyQkXv_2BRcM9PK8gEsr6wsoR43xkhIjjXBSJUmgE6u-5Mr2hHeF3FpqD_3GTdMEMWM1SFwrrtylTIFkLUDF7i2TzdH_imJLvvA68NIbslst_YRpaL_gT74Av2gSqRRR1zJ_MJl_ClgK4Xy6q5FMREp1T9-ei3i4IFgehNAgoHFNeFoyoPMzZv0RkjjG90H7BA5x_5zJ_5PGoEdy9GI0SDfPOsxDQQk0Cm7rHDFtGc0vmYhFx4wAbl37sN7wNgXLUVYatGitYYhBe99AGVKk4HFXYqeCXQ4EFreBW9C0FiWPHRj879hzE-6w" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/168f12d8a1.mp4?token=AqYTe0g7SmSBoqyQzDfGxTiQI1vO5OmyQkXv_2BRcM9PK8gEsr6wsoR43xkhIjjXBSJUmgE6u-5Mr2hHeF3FpqD_3GTdMEMWM1SFwrrtylTIFkLUDF7i2TzdH_imJLvvA68NIbslst_YRpaL_gT74Av2gSqRRR1zJ_MJl_ClgK4Xy6q5FMREp1T9-ei3i4IFgehNAgoHFNeFoyoPMzZv0RkjjG90H7BA5x_5zJ_5PGoEdy9GI0SDfPOsxDQQk0Cm7rHDFtGc0vmYhFx4wAbl37sN7wNgXLUVYatGitYYhBe99AGVKk4HFXYqeCXQ4EFreBW9C0FiWPHRj879hzE-6w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دونالد ترامپ هنگام بازدید از محل احداث بالگردگاه جدید در کاخ سفید، در پاسخ به پرسش خبرنگاران درباره احتمال گفتگو با تهران اعلام کرد که در حال حاضر شرایط مطلوب است، اما امکان مذاکره در آینده وجود دارد.
ترامپ با تاکید بر موضع واشنگتن در قبال برنامه هسته‌ای ایران گفت: «موضوع بسیار ساده است؛ آن‌ها باید به‌طور کامل سلاح هسته‌ای را کنار بگذارند. ایران نمی‌تواند سلاح هسته‌ای داشته باشد، چرا که از آن استفاده خواهد کرد و ما اجازه چنین کاری را نخواهیم داد.»
رئیس‌جمهوری آمریکا در نهایت تصریح کرد که ایران نباید به سلاح هسته‌ای دست یابد و دست نخواهد یافت.
@
VahidOOnLine
ترامپ افزایش عبور کشتی‌ها از تنگه هرمز خبر داد و گفت آمریکا کنترل کامل این آبراه را در اختیار دارد. به گفته او، شب گذشته تعداد زیادی کشتی از تنگه هرمز عبور کردند و اقدامات ایران، از جمله شلیک گاه‌به‌گاه به پهپادها را «مزاحمت» توصیف کرد.
رئیس‌جمهوری آمریکا همچنین گفت قرار نیست همه کشتی‌ها از تنگه هرمز عبور کنند، اما تردد در این آبراه ادامه دارد. ترامپ پیشتر نیز از کنترل کامل آمریکا بر تنگه هرمز سخن گفته بود و مقام‌های ایران این اظهارات را رد کرده‌اند.
@
VahidOOnLine
ترامپ می‌گوید مردم در حال یافتن جایگزین‌هایی برای تامین نفت به‌جای تنگه هرمز هستند و تگزاس، آلاسکا و لوئیزیانا را از جمله این گزینه‌ها معرفی کرد. او گفت خریداران برای تامین نفت به ایالات متحده روی آورده‌اند.
او گفت یکی از دلایلی که قیمت نفت به ۳۰۰ یا ۳۵۰ دلار در هر بشکه نرسیده، افزایش عرضه و روی آوردن خریداران به منابع جایگزین است. او افزود قیمت نفت اکنون حدود ۸۳ تا ۸۵ دلار است و پس از پایان شرایط کنونی، بسیار پایین‌تر خواهد آمد.
رئیس‌جمهوری آمریکا با تاکید بر اینکه این کشور نفت کافی در اختیار دارد، گفت: «مردم دارند جایگزین‌هایی پیدا می‌کنند. یکی از این جایگزین‌ها تگزاس است. یکی دیگر آلاسکا و دیگری لوئیزیانا است. آن‌ها برای تهیه نفت به ایالات متحده می‌آیند.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 284K · <a href="https://t.me/VahidOnline/77956" target="_blank">📅 20:07 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77954">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/pOFMrJOFc1XKvmDVjIs6DH9Z5e3PLo7kMxfZYtwph8X6zyIjjt_Lfdn1iXCKWLIiVo6xQU5WFl6UTvyUgUY8HRnmqnNK10CihtYmRrMGIj-R-COE8xu0j2DaarbLQ-oLJAile3a9LERDLyKMcj840bN6KecoXHGA2j8192eZUPfR-X3Iruc2ThsUZU3uCORphy-ytTiHJwIkg-XNCqCMjg0a678MrBMhV2XaaJjiGMfhbjGBimBgS2F1sjfjltcX15u0rkMd48-TeiRaF_OTdU_cZ7uS6USVFAt0OasCeOB_WVDamnNAOuGcxGB6Q58231Go_xmICrPQU_kLK0O9Dw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/ZFfvYwQltLwXMcx6WAcrU53Y_zLYPGIfmVnRIZeiBkk1jkCh9JRrsutPo2CyXl1pDe1ggoCaGKCF64l5JxGXraztNr8rHSSoiKdRBwoPtT3uqf8X2d-7qIDMUZ6rKr3SpqUXEGZxpngK85euA3ycGeG7ae5C8ibN7yjMthWfzmDwsccU-4QPrHoBmD6lW6h0Fqh3mo6eGfSCBXr_O8jbZxBw0ntZYtXQW4l7B1Iu2ZRdHgI2UQf22_IbyyLjdT81QBXUX72fQzSHdxXIYA-d_aOsgh3U6Nx_nyBJBhPWEoCExjevI20bJ_llLySJguCV4czHBcBsPC-NUJe5I74mgQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">فاینشنال تایمز روز چهارشنبه ۲۸ مردادماه با انتشار گزارشی به نقل از دو مقام ارشد جمهوری اسلامی گزارش کرد که اگر دونالد ترامپ تصمیم به گسترش جنگ بگیرد، هدف قرار دادن پایگاه‌های نظامی در جنوب شرقی اروپا را بررسی خواهد کرد.
براساس این گزارش، یک پایگاه نظامی در بلغارستان و یک پایگاه نظامی ناتو در قبرس از جمله اهداف احتمالی جدید ایران در صورت تشدید درگیری‌ها خواهند بود.
مجلس بلغارستان ماه گذشته با استفاده آمریکا از یکی از پایگاه‌های نظامی این کشور موافقت کرد.
همین دو مقام که نام آن‌ها اعلام نشده می‌گویند نیروهای مسلح جمهوری اسلامی به‌طور جداگانه حمله به کابل‌های فیبر نوری زیر دریایی در تنگه هرمز را در صورت تشدید تنش‌ها، بررسی کرده‌اند.
@
VahidOOnLine
یک مقام سازمان پیمان آتلانتیک شمالی، ناتو، به خبرگزاری آنادولو گفت: «ناتو برای مقابله با هر تهدیدی آماده است و همواره هر کاری را که برای دفاع از همه متحدان لازم باشد، انجام خواهد داد.» این اظهارات پس از انتشار گزارش‌هایی مطرح شد که بر اساس آن‌ها، ایران در صورت تشدید بیشتر جنگ از سوی دونالد ترامپ، حمله به اهداف نظامی آمریکا در اروپا را بررسی کرده است.
این مقام ناتو همچنین به رهگیری موشک‌های بالستیک ایران در اوایل سال جاری اشاره کرد و گفت پدافند هوایی ناتو در چهار مورد جداگانه، موشک‌هایی را که به سمت ترکیه در حرکت بودند، رهگیری کرده است. او این اقدام را نشانه قدرت و موثر بودن وضعیت بازدارندگی و دفاعی ناتو دانست.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 276K · <a href="https://t.me/VahidOnline/77954" target="_blank">📅 16:51 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77952">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/XYAHxpgFfGvHWqZIWhfyU0fw1Y0YXmdZv52Q-4r-L3-XMEOoudQ2sfYEfP_iC3yPZCvYHwUTAzNDDLJScCWjU7HGd1HmvMZRXtP-8MRq5ZI3ITtEi9dM5uM6dkK0cTuwGQe_c0_c3TTl01_-Tt8lDP8zzLsbiYkGcrqZxCPz__l3lGo0tiVarF7LVSu8eCx4Id65EKc69zD1SDYYufAs6VlXLczldyb4I8544UHv24WsmqIdnCRyGlmMMDhNXx3nYAE8Z4vja894kySpM7lCyCfylUOi-L8BIg_dCLPfxg0k2FO4n6I-9d6HLdEh_y-ZKshi5t_NL4JKwGAhgFIE-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/WS9srzSk7EB1LZISTCh1u3sV6BqYafGUj6_cKLNN2jzasOZeLJDRrPFXhmr98w-vfE-7YRUTyKdiTK1kPPr8s4aJ_hXGHaKW7Ffisp1-FEv306i6qFbDFsWEM5nkEL_9gxmtmhbvrKSBHc9AO1aTWicK5_12WJVO2ziOSiiQcSRXtdzFJnTbMpxDWxsxXUkWh5DVo-RG_hJB_Rb9IaTL3oMAqrW67bL2d3UYKeMdAS4TminCtjUbkWDp5sbfOMo5TEr9OIZD8erAjMYc_d8RwSPUVZE7O_XGP2EKFOBgs70KPbbXbyuhHfkcAiapI-A9seUsOCpHG2z1dK-DuaXYFA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">روند افزایشی قیمت جهانی نفت، همزمان با مبهم‌تر شدن سرنوشت مذاکرات مربوط به بازگشایی تنگه هرمز، ادامه یافت و قیمت هر بشکه نفت خام برنت روز چهارشنبه ۲۸ مرداد با یک درصد افزایش نسبت به روز قبل به ۹۲ دلار رسید.
روز سه‌شنبه دونالد ترامپ گفت «هیچ مذاکره یا گفت‌وگویی با جمهوری اسلامی ایران در جریان نیست و هیچ مذاکره یا گفت‌وگویی نیز برنامه‌ریزی نشده است».
@
VahidHeadline
قیمت ارزهای خارجی در بازار آزاد ایران روز چهارشنبه ۲۸ مرداد بار دیگر افزایش قابل‌توجهی پیدا کرد و قیمت دلار آمریکا به ۱۹۱ هزار تومان رسید.
این بالاترین میزان برابری دلار آمریکا با ریال ایران در سه هفتهٔ اخیر محسوب می‌شود.
گزارش وب‌سایت‌های اعلام نرخ ارز و طلا نشان می‌دهد که قیمت یورو نیز بار دیگر از ۲۲۰ هزار تومان فراتر رفته و هر قیمت درهم امارات نیز از ۵۲ هزار تومان عبور کرده است.
روز چهارشنبه هر سکه طلا هم ۱۹۴ میلیون تومان معامله شد.
افزایش قیمت ارزهای خارجی و طلا به دنبال اعلام امارات متحده عربی در توقف هرگونه مبادله تجاری و مالی با ایران رخ می‌دهد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 252K · <a href="https://t.me/VahidOnline/77952" target="_blank">📅 16:43 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77951">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Xzc8OSxIelf6cr54TJ6a_zmEGcOwxiEcE_aDg4mj1JdWTIhfwBFoyrGgzl7JGH9453h0Az7NmzQbHNrhFHITvfYB2ScE3_PKnUXaNvg5G_YttIeDraJreMCnZfRol4siIk2ITFPKRL_BPC5D0uyEVqb9y0ynXZ3MD574p0wj6D4c8ursCAJP22RwG7ERRMVvQIpn2l8RpGapEOThEzH4ttg6NkaMSCBroFMnWI8pqiE7_g5YIs_mdVNuF3pKi4Geiawk7DTaFcBiBBv1wTQdditD4OAlGxKGeWw4RaoSVA9srP4oNxcEjyx3CeWUcYCWU9MNvZ1C4nzA8nycTVxxXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به گزارش وای‌نت، نفتالی بنت، نخست‌وزیر پیشین اسرائیل، گفت که در صورت بازگشت به قدرت، معادله بازدارندگی را تغییر خواهد داد و هر حمله حزب‌الله باعث خواهد شد ما ایران را هدف قرار دهیم.
نفتالی بنت همچنین وعده داد قطر را «کشور دشمن» اعلام کند.
نخست‌وزیر پیشین اسرائیل ادامه داد: «ترکیه و قطر را از غزه خارج خواهیم کرد و به جای آن‌ها مصر را وارد می‌کنیم و در عین حال آزادی عمل اسرائیل در غزه را حفظ خواهیم کرد.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 236K · <a href="https://t.me/VahidOnline/77951" target="_blank">📅 16:41 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77950">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/QWutb6NxJMsTHk_Yj1sWkAJAyGtx3lDeeY5ErzW37h1uNjVlUhRbcCgPpSZ546vLx3YsSlEpt4YBKD6IeHEbBZQQyceGQC7n_A1z5VgrPTdtlHaBN13ozi26NY1O6OWfs9RbV3e_9VMbqAAaRK6ZaVumg1SEg0RYnJPHo9YlzYXzQTY_zQ1MbZyh3N9gv-QUrwi5DcJKuE7wROwIU-_Buk-RupE40y0kboU29dVEd80KCjL4lPDXcewx53MrvRCT_rsy17bRxHxlEY6aym68J9WMZs9XXCD8ZYNkWafiCrP0b04cPvEmis_lzz91bmn7fpzqNuF0R1_iqa3w0yGLgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رئیس ستاد کل نیروهای مسلح جمهوری اسلامی ایران بار دیگر به کشورهای حاشیه جنوبی خلیج فارس نسبت به «هرگونه کمک» به ارتش آمریکا هشدار داد.
در پیامی که روز چهارشنبه ۲۸ مرداد به‌نقل از علی عبداللهی در رسانه‌های ایران منتشر شد، رئیس ستاد کل نیروهای مسلح ایران به کشورهای حاشیه جنوبی خلیج فارس گفته است که «چیزی از چشم ما پنهان نمی‌ماند» و افزوده «این میزان هواپیمای نظامی، به‌ویژه هواپیمای سوخت‌رسان، در پایگاه‌های منطقه‌ای بدون اطلاع کشورهای میزبان بعید به نظر می‌رسد.»
فرمانده قرارگاه خاتم‌الانبیاء در هشدار خود توضیح بیشتری در این باره نداد. شب گذشته امارات متحده عربی اعلام کرد تمام مبادلات مالی و تجاری با ایران را تا اطلاع ثانوی متوقف کرده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 240K · <a href="https://t.me/VahidOnline/77950" target="_blank">📅 16:40 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77949">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/OpfAH48m_rsi9Th1iCDeW3ATuSvsizuW8foeDpdFRcoGmKsHsDd2CBN5Jml0Ad914AHyclhiNFwWDn9fwlWc6KcYO1C6MwxGlqQu-eI67C4bJtMNtO4hj8Qd_8nt5KB_mR3hkPkV5_rf4eO3GV2bTpa1eukemgtn2hT1BOALafmBJ-2pUF2a-MKVdh8XDo3PGK-JY2hT9nRAK_mTTP7SpUCgvtmO_GPHOzYd2gEYbLFKumObY6w-sAlsoJ0CDkM_xUUXQ1GzCRPfXgiZTLHnbfQs2Frzrl1wrxVz913ZUDlYRHX0TLXvbjTp2-8zo5_oah2wJBZ1oEN7C8GbB-grBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری فارس، وابسته به سپاه پاسداران، صبح چهارشنبه گزارش داد نفتکش اماراتی که در کریدور شمالی تنگه هرمز توقیف شده بود، مسیر خود را تغییر داده و به‌سمت بندرعباس در حرکت است. بر اساس این گزارش، مقصد اولیه این نفتکش بندر جبل‌علی در امارات بود، اما پس از توقیف، مسیر آن به‌سمت آب‌های ایران تغییر کرده است.
فارس نام این نفتکش، شرکت مالک، پرچم کشتی، محموله و دلیل رسمی توقیف را اعلام نکرده است؛ موضوعی که ابهام‌ها درباره ماهیت این اقدام را افزایش می‌دهد. گزارش‌های بازنشرشده از خبرگزاری فارس نیز می‌گویند این نفتکش هنگام عبور از تنگه هرمز و در محدوده کریدور تعیین‌شده از سوی ایران متوقف شده بود.
این خبر یک روز پس از آن منتشر می‌شود که امارات متحده عربی، ایران را به شلیک دو موشک به این کشور متهم کرد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 219K · <a href="https://t.me/VahidOnline/77949" target="_blank">📅 16:39 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77948">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/DoacuTib19MX04jy14IJuQ6Nxvw8u0sFhfSjO-6g-LcoDmunNUFjm82xoOl70avZ1dmwbNzqoHL5_raW1-_K9hJHv-xA9S-H3vTHBEOJojWWIZV9CQsfVIpAcnVCuPGwMdMgSq-cjcIYERx_gIT-kSeNfbq497TgVv_LwfM63bTh47bL8GZd1nmCAQz_of-3patwWDopUNvCwvaiKIX_Ow78a7fOUCr3Ka4mlW8X9ywSPGasT9mfZREeSGpgwQ9o0c_d0bzAc0CIjvvj0l0fBRgQXbAgaNbhrmBMZlhjtc5s_Lucz5AqjMiySP8h0aDP19mKrWXTd_301fabNpsxKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حزب مشروطه ایران (لیبرال دموکرات) اعلام کرد فؤاد پاشایی، دبیرکل این حزب، هدف «سوءقصد» قرار گرفته و در بخش مراقبت‌های ویژه بستری شده است.
بر اساس بیانیه این حزب، این حادثه ساعت ۷:۴۵ عصر ۱۷ اوت (۲۶ مرداد) به وقت لس‌آنجلس رخ داده است.
حزب مشروطه ایران همچنین می‌گوید پلیس لس‌آنجلس در حال تحقیق دربارهٔ این حادثه است و اطلاعات تکمیلی و «تأییدشده» دربارهٔ این حادثه بعداً از سوی حزب منتشر خواهد شد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 206K · <a href="https://t.me/VahidOnline/77948" target="_blank">📅 16:37 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77947">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/edef31ced2.mp4?token=MPGHOTSIS9XUOQrqKO75FjBKXpultrj-Lq7V8EYrBuiPBRtE-_BGWqkZvI7vj9LqIL6kEowdofpDjMUGAq5U2MY1Mc2gyz4ZYk32cStFrK2IR7bhrk1Jz_ngdpnl0TTxP_oWYCKXc8tZmmCnX5WJSXcvxB5n9OdOJD2gXfWxL5EPIweL9Od2EB8NcITtpeMvHrzC46xAO0jXQeRf_1VCd714YLBMmb7BWhPw25XuDthZTAdVdLl68E3nTKS_NiGIyRq-U39q3XP7q9lp6ZRTdiXkRlCVn3PWRKHdPyTOypVyBVtM2d2ut7pWmot9becGxUhUzOR6ChWK-w1QafiOMw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/edef31ced2.mp4?token=MPGHOTSIS9XUOQrqKO75FjBKXpultrj-Lq7V8EYrBuiPBRtE-_BGWqkZvI7vj9LqIL6kEowdofpDjMUGAq5U2MY1Mc2gyz4ZYk32cStFrK2IR7bhrk1Jz_ngdpnl0TTxP_oWYCKXc8tZmmCnX5WJSXcvxB5n9OdOJD2gXfWxL5EPIweL9Od2EB8NcITtpeMvHrzC46xAO0jXQeRf_1VCd714YLBMmb7BWhPw25XuDthZTAdVdLl68E3nTKS_NiGIyRq-U39q3XP7q9lp6ZRTdiXkRlCVn3PWRKHdPyTOypVyBVtM2d2ut7pWmot9becGxUhUzOR6ChWK-w1QafiOMw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هیوا سیفی‌زاده، خواننده ایرانی که در جریان تک‌خوانی در «عمارت روبرو» در اسفند ۱۴۰۳ بازداشت شد، روز چهارشنبه ۲۸ مرداد با انتشار ویدئویی اعلام کرد که دادگاه او را به اتهام «تشویق به فساد و فحشا» به چهار سال حبس تعزیری محکوم کرده است.
خانم سیفی‌زاده در این ویدئو به رای بدوی دادگاه اعتراض کرده و می‌گوید: خواندن شعر سعدی و آواز ایرانی چطور می‌تواند مصداق «تشویق به فساد و فحشا» باشد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 215K · <a href="https://t.me/VahidOnline/77947" target="_blank">📅 16:35 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77946">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/M8MdWgRXHrtJh51Vd1i-ZYPWbJC7p7REmnF4nsVgmsg_gmq2wBM2ZgqMkZkEfOJJ0JP_Tni6jHvMymst50pmZAv1zL7Wm78alrKeug3c2WvnqA00qQrp02zSp2qtINz5ve-QNzEYPJC3vHfPYFMQ_dH0ohjjwtbECB0ovh2KXLvQs7QnrOZqzrHQ3cWKZVKiIVI25dFowQTNdtRXHZ-9SQnJCEfuR7vq-tp6Zl_F6S4jwqq0TzjnGZ2mhhadUvEj5Cq8O4EEds2oRrf3y1Vzw9B2CNzpcRzGLRbIjpY5l1gIzY5SpSCZcd7ePNS7KvGypGCcu_cIPDEh-h8HW7NPDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هرانا: آرمین نورانی، خواننده موسیقی سبک رپ که با نام «خجسته» شناخته می‌شود، بازداشت و پس از مدتی با اخذ تعهد آزاد شد.
در پی بازداشت این خواننده، ویدئویی از اعترافات اجباری وی منتشر شده است.
در این ویدئو که مشخص نیست تحت چه شرایطی ضبط شده، آقای نورانی نسبت به شماری از اظهارات و مواضع پیشین خود در ارتباط با اعتراضات و حمایت از معترضان ابراز پشیمانی می‌کند.
لازم به یادآوری است علاوه بر نقض کرامت انسانی که در سایه ضبط و پخش اعترافات اجباری صورت می گیرد، اساسا تا زمانی که فردی در محکمه محکومیت نهایی دریافت نکند، از منظر قانون بی‌گناه محسوب می شود و هرگونه اعمال مجازاتی پیش از محکومیت نقض حقوق شهروندی و انسانی او محسوب می شود.
hra_news
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 287K · <a href="https://t.me/VahidOnline/77946" target="_blank">📅 16:35 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77945">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/FM2DgbaaQXLqPorFjBU5sCkuBFKZruRyxMVK0f_PhsAB25B5aedKen8cYmuNiHJ55hyimXgofFv-4J9rI3CDUDQfaoLTWD8LDZF2u6gkaoDIuPLihKvGj1D8ko5RPpL8fT8V6ejXuVkGLap3fC9VdmYvN9ivIVybHsCRe7U9GyfGLs7g9EQKqhx35DpIMIuQ9pDOn7pyeSMdwat3sF4tuxk8cJnkPoeV4qBpHnVdGq6rIhZzLFC1K0Ge1bqMdUBvNUkxQmhkhR3XNqoSSCgQ2agCUq31fA60ZPM0OZRH4nPyQAmwvXEJMesOIN0LsvXlmihs6gW_7Fp6J9txR2itfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امارات:  تمام مبادلات تجاری و تراکنش‌های مالی با ایران تا اطلاع ثانوی متوقف شد
مدیر اداره ارتباطات راهبردی وزارت امور خارجه:
افرا الحاملی، مدیر اداره ارتباطات راهبردی وزارت امور خارجه، همه ادعاها درباره وضعیت روابط اقتصادی میان امارات متحده عربی و جمهوری اسلامی ایران را رد کرد.
الحاملی بار دیگر بر تعهد راسخ امارات به گفت‌وگو، همکاری و همگرایی منطقه‌ای به‌عنوان ابزارهای اساسی برای پیشبرد صلح، ثبات و رفاه در منطقه تأکید کرد.
الحاملی تصریح کرد که با توجه به تشدید تنش‌های منطقه‌ای که صلح و امنیت منطقه‌ای و بین‌المللی را تضعیف می‌کند، تمام تجارت، مبادلات تجاری و تراکنش‌های مالی با ایران تا اطلاع ثانوی متوقف شده است.
الحاملی تأکید کرد که امارات همچنان قویاً به حفظ سلامت نظام مالی بین‌المللی، مطابق با حقوق بین‌الملل و بالاترین استانداردهای جهانی، متعهد است.
mofauae
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 337K · <a href="https://t.me/VahidOnline/77945" target="_blank">📅 23:53 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77944">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Mm_7hbVt16zgQfv--aWBaDwxYzX3y0Ln-KqWtAOqHVda7k_5Q06EDEpEvRWY6rVtILXS6vO_IEKPe1GE1NmcBj08OJ9htYzLBCc9PkAFrhQIBsNI-OzcqvWyWdApt1l5p9Gluj-JZ9CjRn-HVmAJMNFzwRQk-5oxQEBa08f29BEnJ_ENbeeRDqfzLTZzP9AnscxVjou2AYbuPxXPU2PO1DWFNNN1W5-V_4j2BZ51zumYHrT5L5kwpXOd95vaGWojmdnzuR05Azl73HB_U2d86W8RDe8LAnZv-1QR0ib1YiI5T-eObyMNox2Iy0y-g2HOT9R-0AjhPodzcvNfUg4pqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر خارجه فرانسه: دو دپیلمات ایرانی اخراج می‌شوند
ژان نوئل بارو:
مردم ایران، مردمی بزرگ، قربانی اصلی این دوره از تنش شدید در خاورمیانه‌اند؛ مردمی که میان سرکوب خونین اعتراضات ژانویه ۲۰۲۶ و بمباران‌ها در تنگنا گرفتار شده‌اند.
دقیقاً به این دلیل که فرانسه در کنار مردم ایران ایستاده و از هنرمندان، دانشمندان و پژوهشگران آن حمایت می‌کند، دو دیپلمات فرانسوی در ۱۹ ژوئیه گذشته به‌طرزی رسوایی‌آمیز و عامدانه مورد حمله قرار گرفتند.
من اعلام کرده بودم که این اقدام غیرقابل‌تحمل پیامدهایی خواهد داشت. این کار انجام شده است. دو دیپلمات ایرانی در فرانسه در همین چند روز آینده اخراج خواهند شد.
jnbarrot
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 329K · <a href="https://t.me/VahidOnline/77944" target="_blank">📅 22:19 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77943">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/COf_3Y3a62Fcrt0PaDSRNziS9rqOGOjpVlxt1Fxp-tu-Qwy8AxGSd9BpwDvnMde6kTpThyLLWDoG_188Dr8Jxiczh_rDjVPtlmRrEPLtXw_PoX4nkd7WnHKSPVwb_hb_4Vvx_4xzAmG-HuLvDxy7BT1wvM44OtVtQkTs2gmRTBFyXG46vSLqouX0B__GYge71X0X24rmAGYyvhZ79X1Htv26phhrH1WmOp9SffVjPBJU81lp9cMFbSt2f7MmPMBIYJfJzs2bgGxx4h4bDvXgcyej840MOcLe-9gl_tNu0hqIvE4F9LJozg0tqhbdeQUg0Qz-hEObMtxOwiDpLfz8Rg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قالیباف:
آمریکایی‌ها فکر می‌کنند اگر فشار بیشتری بر ایران وارد کنند، می‌توانند امتیازهایی بگیرند که اصلاً جزو توافق نبود. بسنت و هگست واقعاً در حد و اندازه این کار نیستند. دیگر منتظر نباشید این دارودسته دلقک‌ها از کلاهشان خرگوش بیرون بیاورند؛ خودتان افتضاحی را که به بار آورده‌اید جمع کنید.
mb_ghalibaf
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 320K · <a href="https://t.me/VahidOnline/77943" target="_blank">📅 21:03 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77942">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromVahid OnLive وحید آن‌لایو</strong></div>
<div class="tg-footer">👁️ 315K · <a href="https://t.me/VahidOnline/77942" target="_blank">📅 20:50 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77941">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/WA7huVQ5xY98mmXTozAnBfepGq92OCYQZs0ZrZq7EuisnTFRrl8JMTAzqzB7yic6yRvrow2YFM8RdFiUmpX0TL_XIcCnRSCmId8D-aAhBOMe7-CWoqKAh8cIgACa0mSR9NrBN4OcIVDR_qOsgAZKPCDg2cWQVQP2cupf-VzmEv4PEJPCPWaX4LEVdwY5KnhGXt8tA8IrOh03mqnMz0rGiEmiTWJMoZ88TyPDsCAN8C4qHWyXqJC4EY9xU_C5E-RaiUxvEiePS6y-dTja7x_cud8YLw-jXG5qyBSwA-P4LmStN8ZirBPy9rfZR6drYSvECrtIMpYdPI5Lmh28DDBqGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سازمان ملی مدیریت شرایط اضطراری، بحران‌ها و بلایای امارات:
سامانه‌های پدافند هوایی امارات متحده عربی یک تهدید موشکی را که این کشور را هدف قرار داده بود، شناسایی کردند. لطفاً در مکانی امن بمانید و هشدارها و به‌روزرسانی‌های منتشرشده از طریق کانال‌های رسمی را دنبال کنید.
NCEMAUAE
آپدیت:
پایان وضعیت اضطراری
پیامک جدیدی که برای شهروندان در دبی ارسال شده:
از همکاری شما سپاسگزاریم. به شما اطمینان می‌دهیم که وضعیت در حال حاضر امن است. می‌توانید فعالیت‌های عادی خود را از سر بگیرید، اما همچنان احتیاط کنید، اقدامات پیشگیرانه لازم را رعایت کنید و دستورالعمل‌های رسمی را دنبال کنید.
-وزارت کشور [امارات]
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 306K · <a href="https://t.me/VahidOnline/77941" target="_blank">📅 18:30 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77940">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/S23nUd-LvGMte5m8w_g0jd8NrnaTYBM9E7aui2Po9M8itANSPwiAcebza_LaeGHUApIM5ieAWy4A0qxzSLj52Tp_TfKJiX_EvUfX1NHwaOvdZ-yDLX5K8_6iFGkTkiXwtPAAV-KlIV7v2-p8rZdEpgkORP9pucDYWZasXjDm2Prgla9twopTgDAZNrxeKqwGwy11qra-42I8dmJmOIxljZmP51TUH6VKqA7p8udLvouqrnSczTG_kbq43_EOnvzdF7vK-BrvIt7JCXLMNPpg7N2jyUUyy1NZ5Kem-R7DnQLAngR34jC4dMATpxpaB9kZflSrO5wwAx6NKJ1IZB4A9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وحید همین الان دبی آلرت موشک ۱۸:۵۲ وقت محلی
پیام و تصویر از دو شهروند مختلف
آپدیت: پیام‌ها و تصویرهای مشابه دیگری هم دریافت کردم.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 288K · <a href="https://t.me/VahidOnline/77940" target="_blank">📅 18:25 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77939">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/g22Up9sR8mHHh6ASQfRuifxlPLRwFT0Ck5EqNAQY1xt_DqnULNWeucto-AdFlZRKpiusktzDdm_peDdA84pXi3OBDomiU7_sy7xGuNsHJwmsiJKBPamhpupZ4NbbF4y4F_vd7PxpJLltxvRo1V51_4qWBGtriLvGEpn8Np2umeRqus-eEh7xA_R45BYn4SwwM2u-cb6gogc_e-6232FTg8D5p63VpU3gdfQJlky_vt5oCNCf59LaAI4PS7jOW9fl8t-MF-fiLJ_ALdnTYIs2Q-o66Pd6qJoTYopwmxeUHEKaM9imN4Rjzb0PQ8CffSTaUOZCPzb2bdvmXNfWSGhTcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">UKMTO:
مرکز عملیات تجارت دریایی بریتانیا با تأخیر گزارشی از وقوع یک حادثه در تنگه هرمز دریافت کرده است.
یک طرف ثالث گزارش داده که یک کشتی فله‌بر هنگام عبور از تنگه هرمز با یک پرتابه ناشناس مورد اصابت قرار گرفته است.
این اصابت به سمت راست کشتی آسیب وارد کرده و موجب آسیب‌دیدگی یکی از خدمه شده است.
گزارشی از پیامد زیست‌محیطی این حادثه وجود ندارد.
مقام‌ها در حال تحقیق هستند.
UK_MTO
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 278K · <a href="https://t.me/VahidOnline/77939" target="_blank">📅 18:05 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77937">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/KBrRlZUQ52sqoAIbyLeg3BbPrW99Qw4BSEClNVoohwZua2f5ksw255LUs1dffsZlrU8AM2kQVsGKrubR57YvnWdTwjFpLG-C9e8l4FsX6PrRsXOfeg4Tubgf65LXbTctE9WA7WOVj4tercmwx7R-v2SyTKuPZwIDskjjmW9A43QqU5vWvWkWoY8T17EGW1-8CvE0wXck_mUHozco8VinO8_f8QlBLZ6CAJLXiBgM1ACfWOcyDipunGSZcU8Qqi1TrJv68zn-yEXy8lMLmf_aYCdIMNCAxGY_moBADVJo0uV0qwmi9m1cRJLyMNT28f_dX79milnUE2tiF_6JNArO_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ:
هیچ مذاکره یا گفت‌وگویی با جمهوری اسلامی ایران در جریان نیست و هیچ مذاکره یا گفت‌وگویی نیز برنامه‌ریزی نشده است.
محاصره دریایی همچنان با تمام قدرت برقرار است.
تنگه هرمز باز و فعال است.
همه مین‌های دریایی جمع‌آوری یا منفجر شده‌اند.
از توجه شما به این موضوع متشکرم!
رئیس‌جمهور دونالد جی. ترامپ
realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 278K · <a href="https://t.me/VahidOnline/77937" target="_blank">📅 17:03 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77936">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/J6K6QR6B1P_2l7P2rO3kxe9hiYPftxvvYGEo3wOcG0qrzdS0jrmmoGLhVypgaJA_TYoED2mGZS6I8r63GkApuGW3bjnGM8bhEFmz4VK3h7n_dKbWrdnEE34xqVF5VB5G1E5Y17_sW4HYCK5eKcXcdetRlmYKA3vi1XNlygMfjbDeM-tXJigWyaRUmUsYUGh5KByfseVWSClo-Mhji0Gd8yzNrCYOhLW4yfzl73Vo-RMmq0XPEHy5YNtvtq_Zrv5JyXxkYhBQfo4gMdyTv1PqokNg8RjrpD-Mye2ROAmUrljxeGCC5VfQ-N_jJN0f0u3CHtOyHFZFvm-ECSptuW6Yug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رئیس‌جمهور ایالات متحده روز سه‌شنبه ۲۷ مرداد در پستی در شبکه اجتماعی خود، تروث سوشال، بار دیگر تنگۀ هرمز را «قلمرو ایالات متحده» خواند.
دونالد ترامپ با انتشار پست تازه‌ای در «تروث سوشال»، یک تصویر گرافیکی را به نمایش گذاشته که در آن، تنگۀ هرمز، به‌عنوان «قلمروی تازۀ» ایالات متحده نشانه‌گذاری شده‌است.
او پیشتر هم در یک سخنرانی با لحنی نیمه‌شوخی و نیمه‌جدی، این آبراه را به‌عنوان بخشی از قلمروی ایالات متحده معرفی کرده بود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 265K · <a href="https://t.me/VahidOnline/77936" target="_blank">📅 16:28 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77935">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/VchonTpyIdEb4wq4QV1AyQMgsklzghNC7gVWuqo5CejcSoKltPosbGgrsInYZM2N_0PLUcLGJ6ieI_BUm-1UE3NRJOvTK4V6yOpk-VD8scJ_1mGrutT73jMJzcbFuHZG77i4pfZ8XacGMvG6jbVScG_uIUiIJcQDr5RQDaGBGkIoyxcKSY4a-t4x5V769PpMiV9tdMcLt0hkA1P5Xtpb2m1qE265v18MO8hf1_XpYBEfaieyoTgxwAr-eFrwlhGKveSyb4Lldd6ZxXvikvSWiOj0QRdC28ITcI4TOLsY610_l4hHKVFxMR5ABUYhCKc-lzbHaXSBE8SsUOEQ0I-F_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سخنگوی وزارت خارجه قطر درخواست جمهوری اسلامی ایران برای ورود کمیته بین‌المللی صلیب سرخ به موضوع خلبانان ایرانی را «ترفند رسانه‌ای» خواند و گفت ایران هنوز به دعوت این کشور برای بررسی موضوع پاسخ نداده است.
ماجد الانصاری روز سه‌شنبه ۲۷ مرداد گفت «دعوت دوحه از هیئت ایرانی برای سفر به قطر و بررسی این پرونده همچنان پابرجاست، اما تهران هنوز به دعوت دوحه برای اعزام هیئتی به قطر پاسخ نداده است».
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 248K · <a href="https://t.me/VahidOnline/77935" target="_blank">📅 16:26 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77934">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/7722d713c1.mp4?token=NQRMI1fYBScU_yrs3pybydFCbMrL94Bx7ud-umVsB2GjboQJ0SeidgM1h6QpVCPadrriNyaMk_6AaVN7LepBd4ab59gKG6fsbGekBF_EuEMJkBpz-ApwTeQMLq9Fqz221RdgY1c93xSrWkylY-bnY4crvKnCoQny-_TqhdSxuvxTBMbhdf7_O6Z8tOjc3LuCWA5etXAOTj2txd3e2CxlUAj_UZcoy5fHD6OkXQOKuMN_hDcW0KwNynzPWJG0uheVj1Z4sbKZOqmRvZ3QSUOH0TaPLqCCalUFLqZh3g43xn4J_FBDn8G82v2inhLmXsXw7I_HgH9ZdmtDRTfiv5x0gQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/7722d713c1.mp4?token=NQRMI1fYBScU_yrs3pybydFCbMrL94Bx7ud-umVsB2GjboQJ0SeidgM1h6QpVCPadrriNyaMk_6AaVN7LepBd4ab59gKG6fsbGekBF_EuEMJkBpz-ApwTeQMLq9Fqz221RdgY1c93xSrWkylY-bnY4crvKnCoQny-_TqhdSxuvxTBMbhdf7_O6Z8tOjc3LuCWA5etXAOTj2txd3e2CxlUAj_UZcoy5fHD6OkXQOKuMN_hDcW0KwNynzPWJG0uheVj1Z4sbKZOqmRvZ3QSUOH0TaPLqCCalUFLqZh3g43xn4J_FBDn8G82v2inhLmXsXw7I_HgH9ZdmtDRTfiv5x0gQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رئیس مجلس شورای اسلامی و مذاکره‌کننده اصلی با ایالات متحده می‌گوید تهران تا قبل از رفع محاصرهٔ بنادر ایران توسط آمریکا و انجام برخی شروط دیگر، تنگهٔ هرمز را بازگشایی نخواهد کرد.
محمدباقر قالیباف روز سه‌شنبه ۲۶ مرداد در نطق پیش از دستور مجلس، دیگر شروط ایران برای بازگشایی تنگهٔ هرمز را «آزادی اموال بلوکه‌شده، رفع تحریم نفت و پایان تهدید و عملیات نظامی در همه جبهه‌ها و دیگر شروط» تفاهم‌نامهٔ اسلام‌آباد دانست.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 232K · <a href="https://t.me/VahidOnline/77934" target="_blank">📅 16:24 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77933">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/IaIddYX-6EIzM3PnMXP3cj6h4d0DvwEvhYCQ35qE0G-JSuNO519iM8Iy5XVEg0IHDrtws8K4fKwwOHmqYIJzTxT_KDsaODJEV5MMdHTrHZHhdCqtmgTyclpS3D7Rpr-YBItocKeiQVgbDeUYux0erXbTwB5TfJDmwqeGpky6XINE00aRqWPS7PPE2M7TEw_FSi1mIgHIY-nvUCy6BbTmIB57wqC3t-RARhB3gV8ZEaYYToM7KT3tTgk-Pj2Gdc88fM80V0hVOgAReMtRuTQ_HOUuS7P_jBqHJq-blq4IjIl6tMBq9tGHhs2g-1aJkXVRZ1tqdiHfbFo5kQuij6WsWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پس از آنکه دونالد ترامپ کانال ارتباط پشت پرده آمریکا و سپاه پاسداران را تایید و دولت ایران و سپاه آن را تکذیب کردند، شبکه العربیه به نقل از منابع آگاه جزئیات جدیدی را از تلاش‌های نچیروان بارزانی، رئیس‌ اقلیم کردستان عراق، برای برقراری تماس بین آمریکا و سپاه گزارش کرده است.
العربیه به نقل از منابع نزدیک به ریاست اقلیم کردستان عراق گزارش کرده است که آقای بارزانی در تلاش برای کاهش تنش میان تهران و واشنگتن، دیدارهایی با مقام‌های باندپایه ایران و آمریکا داشته است، از جمله دو دیدار در بغداد با اسماعیل قاآنی، فرمانده نیروی قدس سپاه پاسداران.
به گفته منابع العربیه، آقای بارزانی میانجی‌گری میان ایران و آمریکا را از اوایل ماه مارس، یعنی چند روز پس از شروع حملات آمریکا و اسرائیل به ایران شروع کرده بود.
دلشاد شهاب، سخنگوی ریاست اقلیم کردستان عراق، دیروز در پاسخ به پرسش بی‌بی‌سی‌ فارسی، تماس‌ بین آمریکا و سپاه از طریق آقای بارزانی را تایید کرد:
«این خبر از یک جای قابل اعتماد منتشر شده و نام برخی افراد به عنوان منبع در این گزارش مطرح شده، ما هم همین اطلاعات و جزئیات را داریم، همه آنها صحت دارد و ما هم تایید می‌کنیم. من فعلا اطلاعات بیشتری جز آنچه منتشر شده نمی‌توانم بدهم.»
خبر این تماس‌ها نخست در وبسایت اکسیوس گزارش شده بود.
سایت خبری اکسیوس به نقل از منابع آگاه گزارش داده بود که آمریکا حدود یک ماه پیش از امضای تفاهم‌نامه با ایران، با میانجی‌گری نچیروان بارزانی، رئیس‌ اقلیم کردستان عراق، با سپاه پاسداران تماس برقرار کرده است.
اسماعیل بقایی، سخنگوی وزارت خارجه ایران دیرور به خبرنگاران گفت: «خبر برگزاری نشست محرمانه میان ایران و آمریکا در اربیل کاملاً ساختگی است.»
حسین محبی، سخنگوی سپاه، هم در واکنش به اظهارات دونالد ترامپ که وجود کانال ارتباطی پشت پرده میان آمریکا و سپاه پاسداران را تایید کرده بود گفت: «این دروغ ترامپ، صرفاً فانتزی‌هایی است که به خاطر توهمات و کابوس‌های ناشی از شکست و استیصال درجنگ به او دچار شده است.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 243K · <a href="https://t.me/VahidOnline/77933" target="_blank">📅 16:19 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77932">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/ff868c2485.mp4?token=vs8S5aEjYbX2ZMEk7S7DtWg05u5OnaKlpje9snMMYi1AA-ifeN--kNMKesBCtxcJGCIiA1XR_e2kyvSXgl04ZTimHjfepY_grcQTc935PBW7h2mnpWPLUsN4f5gfDpM8wjP74wLIis87yqHrFDgH3Ikx5xftV8B51pJTliHE1aX6gI2TV7w1fxrsbJsrbV8oFhKdqLyun59S3Fna4txbzwOPjZOcIaqSH9vxrigtbOUTehWBQsC6Z62YBke6mfK2Sd96knGYSypJRUmUAo18GJBHEuNFJMQGG1p8-Gbdl6b4jUJRaXVRZiAPeB0JVv7BNRHE3eUH_LzUQUeuIM2bfw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/ff868c2485.mp4?token=vs8S5aEjYbX2ZMEk7S7DtWg05u5OnaKlpje9snMMYi1AA-ifeN--kNMKesBCtxcJGCIiA1XR_e2kyvSXgl04ZTimHjfepY_grcQTc935PBW7h2mnpWPLUsN4f5gfDpM8wjP74wLIis87yqHrFDgH3Ikx5xftV8B51pJTliHE1aX6gI2TV7w1fxrsbJsrbV8oFhKdqLyun59S3Fna4txbzwOPjZOcIaqSH9vxrigtbOUTehWBQsC6Z62YBke6mfK2Sd96knGYSypJRUmUAo18GJBHEuNFJMQGG1p8-Gbdl6b4jUJRaXVRZiAPeB0JVv7BNRHE3eUH_LzUQUeuIM2bfw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رئیس مجلس شورای اسلامی می‌گوید که افزایش قیمت بنزین توسط دولت مسعود پزشکیان «تدبیری حساب‌شده نیست»، چرا که به ادعای او، «دشمن» برای این مسئله «برنامه‌ریزی کرده است».
محمدباقر قالیباف روز سه‌شنبه ۲۶ مرداد در نطق پیش از دستور مجلس ادعا کرد که «بر اساس اطلاعات پیدا و پنهان، دشمن مترصد ایجاد آشوب و ترکیب آن با عملیات‌های نظامی مانند ترور و اقدامات تجزیه‌طلبانه است».
او بدون ارائه راه‌حلی تأکید کرد که مشکل کمبود بنزین باید با برنامه‌ریزی جامع و بسیار هوشمند حل شود، به‌گونه‌ای که «بیشترین عدالت وکمترین نارضایتی را در مردم ایجاد کند».
مسعود پزشکیان، رئیس‌جمهور ایران، روز ۲۵ مرداد با اذعان به تأثیر محاصره دریایی آمریکا علیه بنادر ایران گفته بود که راه ورود کالا به ایران بسته شده و دولت منابع لازم برای واردات بنزین را در اختیار ندارد.
بر اساس آخرین آماری که دولت ایران منتشر کرده، تولید روزانه سوخت در کشور بالغ بر ۱۱۵ میلیون لیتر است، در حالی که مصرف آن به ۱۲۹ میلیون لیتر رسیده است که نشان‌دهندۀ ۱۴ میلیون لیتر کسری است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 232K · <a href="https://t.me/VahidOnline/77932" target="_blank">📅 16:17 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77931">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/MXElllHrimAkVULjklZLfIzGChIdk9PKdiS84qja7iI3h_CwgszURyI0Dc3ii5S96SAqtM0xtcKHCcnvTylBZiIDS7UQDma-WAfsTzZicWifZDFQ9yyZdW-uCbjGqrp6FZEN7W8XmT2nylo2U1RcaB_WgrSXAFEtr_gH4Gy4sfUSYA6dzhipeUcjpYssU7J8UkBeHAm9NPPIuosmRkiSs6dfFWsOCWJHEz-zByxCmdycxpob98yCgCNXAvZL3XMV3tGlEIJ_Ko8C8NIw5SMLv9-NqWDHhWH6CgNZ_ZkkI2RCqhGOvhYVYD-mfweiN1NrDWU2PKnlGCz6XJ_jzY6gTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک منبع مطلع به ایران اینترنشنال گفت که محسن (مهرداد) تکش، شهروند ۳۳ ساله در اصفهان در رابطه با اعتراض‌های دی‌ماه سال گذشته با اتهام محاربه به دو بار اعدام محکوم شده است.
تکش، ساکن دیزیچه اصفهان، در جریان سرکوب اعتراض‌ها در هفته آخر دی‌ماه بازداشت شد.
منبع مطلع گفت که او در دوران بازداشت به‌شدت شکنجه شده و دستش بر اثر شکنجه شکسته است.
به گفته این منبع، تکش تحت فشار و شکنجه ناچار شده اتهاماتی را که بازجویان به او نسبت داده‌اند بپذیرد و همین اعترافات اجباری، مبنای تشکیل پرونده و صدور حکم علیه او قرار گرفته است.
خانواده تکش تا حدود چهار ماه پس از بازداشت، از محل نگهداری و وضعیت او اطلاع دقیقی نداشتند. او پس از چهار ماه بی‌خبری، از بند الف‌ط زندان دستگرد اصفهان با خانواده‌اش تماس گرفت.
منبع مطلع به ایران اینترنشنال گفت به‌جز اعترافاتی که تحت فشار و شکنجه از تکش گرفته شده، هیچ سند یا مدرک دیگری برای اثبات اتهامات مطرح‌شده علیه او در پرونده وجود ندارد.
محسن تکش پیش از بازداشت، در دیزیچه یک تعمیرگاه مکانیکی موتورسیکلت داشت و از این راه امرار معاش می‌کرد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 267K · <a href="https://t.me/VahidOnline/77931" target="_blank">📅 16:06 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77930">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/STEPlx4qadXpZz_kT6mlqimVY2q670zjwVdLkMn5b2L_YwRIGay_X7UR2K-YWSUuIlgqNrk1lAjyzScaYOAfQzZbRt77kKR6Fs6s71vsVgLygTU1kDQJWg_HTiC5OW58BJFrdeDnko4wbLcKTfJOa3L43fz4qYWMyEDTWfkiGY8YrOMqBOO4VraRtfZkEZXzQiVOrr6jNv0NItwlxM12UpLby40JJymIKThFRJVaMvgtsr1oP76iWZEV0beDNoEHBzyozXvrUDgKOjRSsEbLWjK0K7qttOIGjOQ6H2liCwUL3k6cyOVhbQFbUeAr0Pgw-CGPlZSDLCuvXBTl8xeSWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">UKMTO:
مرکز عملیات تجارت دریایی بریتانیا گزارشی از وقوع یک حادثه در تنگه هرمز دریافت کرده است.
افسر امنیتی شرکت گزارش داده که یک شناور هنگام عبور به سمت خارج از تنگه هرمز، با پرتابه‌ای ناشناس مورد اصابت قرار گرفته است.
این برخورد به موتورخانه آسیب وارد کرده و باعث مصدومیت یکی از خدمه شده است.
در حال حاضر، گارد ساحلی عمان در حال کمک‌رسانی به سایر خدمه است.
تاکنون هیچ پیامد زیست‌محیطی گزارش نشده است.
مقام‌ها در حال بررسی این حادثه هستند.
UK_MTO
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 306K · <a href="https://t.me/VahidOnline/77930" target="_blank">📅 07:31 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77929">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/gp_ZPezl5Tb3dGct90Ot7s7I_KwvUxbit-eBkRwsySOnnqR2-rCP4KleXGVmii667tC8IlpSZ5c7gyV42bFxk3fnc9_6J4A0fWOJqTqoAzTL8EuBrSvErsWSKDgt56BSgqGVqgB6htce_pewfCbF_ArNkhL8p7wzaHZjifVW9gwKhUZFd_NoLoT-5czp5jeqGxUCrIlTLpLlkmHEuYg2-cEsW202Nhn8N4IrUbdeDRqRVkj39I3QnGu9DI4NZ3q7SHVwwp3d7-rizI6_riGiFjZfIhnzeitglxx_ABXhFojaPIPh-4XGz6bxJ_qoqYE5zu-LBNTVvwNRTvBt53AVoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دادگاه فدرال کانادا در حکم نهایی خود درخواست سلمان سامانی، معاون و سخنگوی پیشین وزارت کشور جمهوری اسلامی در زمان سرکوب اعتراضات سراسری آبان ۱۳۹۸، برای توقف روند اخراجش از این کشور را رد کرد. بر این اساس، اداره مرزبانی کانادا موظف است حکم اخراج او را اجرا کند.
سامانی پس از استعفا از سمت خود با ویزای توریستی وارد کانادا شده بود. این در حالی است که بر اساس قوانین کانادا، مقام‌های ارشد حکومت‌های ناقض حقوق بشر حق حضور در این کشور را ندارند.
سامانی در درخواست خود مدعی شده بود در صورت بازگشت به ایران با «خطر شکنجه، اعدام یا خودکشی» روبه‌رو خواهد شد.
بر اساس حکم دادگاه، قاضی این ادعا را رد و اعلام کرد سامانی در مصاحبه‌های خود از عملکرد وزارت کشور در آبان ۱۳۹۸ دفاع کرده و هیچ مدرکی وجود ندارد که نشان دهد حکومت ایران او را «خائن» می‌داند.
قاضی همچنین تاکید کرد منافع عمومی کانادا در جلوگیری از تبدیل شدن این کشور به «پناهگاه امن سرکوبگران»، بر ادعاهای سامانی ارجحیت دارد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 285K · <a href="https://t.me/VahidOnline/77929" target="_blank">📅 07:29 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77928">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/mVxxBiLigoSAPytvkwG3-O2udB7CP7JmxayfzYQPwIYAV-RjRYjrC_eTlTDM8EVc4MO7jko_C-8LOk1GvOLOfHa3SlVIGsr-aJdjjMvfVWY4ci0PuBmuQcjV65L0b13zLRqZvdw-Nh3nGCc7phFg7M9XMwWXfFlIeH1FMncrkUqGSfByDqU3Z-NfS87yY4LMDLGFII2Dj1xWesywnzILZG-gxy_GXa-_j_caAqbMhZDqmqAhdzawOwyLY6E_d1w2jlYLGO95Rqpfoe183aa9-oyZ1eO7H1Q5bvlSZfvwHSF0uyclvBDt239FkK_BemzBbu5mrRpNQ69pgsJ2LmzP9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رجب طیب اردوغان، رئیس‌جمهور ترکیه، در گفتگو با دونالد ترامپ، رئیس‌جمهوری آمریکا گفت که ادامه گفتگوها با ایران برای بهره‌گیری از دیپلماسی حائز اهمیت است و ترکیه آماده مشارکت در این زمینه است.
دفتر ریاست‌جمهوری ترکیه اعلام کرد که در این گفتگوی تلفنی رجب طیب اردوغان، آمادگی آنکارا را برای حمایت از تلاش‌های صلح ابراز کرد.
پیش از این جرد کوشنر، فرستاده دونالد ترامپ، رئیس جمهور آمریکا، گفته بود که گفت‌وگوهای ایران و آمریکا جدی و فشرده است، اما دو طرف هنوز به تفاهم نرسیده‌اند.
آقای کوشنر که داماد دونالد ترامپ هم هست، به فاکس نیوز گفت که مذاکرات آمریکا و نهادهای مختلف حکومت ایران احتمالاً قوی‌تر از همیشه است، اما دو طرف هنوز به نتیجه نهایی نرسیده‌اند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 281K · <a href="https://t.me/VahidOnline/77928" target="_blank">📅 07:28 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77927">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/e635bc1048.mp4?token=qgNdzU6ekvbuJ-jMwp20pAOt-04_JEthchnII0E8vfm-G8gQbgT8oY6MJHopBW76SLv0DxORcqjmtAgtTclr0KGde2Euu-VuDSes7TemguT8eeIOyxEhUugxz_h29s2uj60j73_PV12LJqEfh1W70_9r5ae1F1GT7NUDiE-KQFqdCX2QTuQ7UMBM_-jQTMBC9isnB7aXlZ-L4PcyQUprlh7XpUpoWfQ7ELlpDjwKjLMSKjCtIAo_k11nlsi7GibxMvKLpZksPxZIw6B7MialsJm7i0cuvtikSBrxzX5bXILryXdezNzkgxT5S9EXcSdwxDIrVEMHhVUMCDH8j7mxhYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/e635bc1048.mp4?token=qgNdzU6ekvbuJ-jMwp20pAOt-04_JEthchnII0E8vfm-G8gQbgT8oY6MJHopBW76SLv0DxORcqjmtAgtTclr0KGde2Euu-VuDSes7TemguT8eeIOyxEhUugxz_h29s2uj60j73_PV12LJqEfh1W70_9r5ae1F1GT7NUDiE-KQFqdCX2QTuQ7UMBM_-jQTMBC9isnB7aXlZ-L4PcyQUprlh7XpUpoWfQ7ELlpDjwKjLMSKjCtIAo_k11nlsi7GibxMvKLpZksPxZIw6B7MialsJm7i0cuvtikSBrxzX5bXILryXdezNzkgxT5S9EXcSdwxDIrVEMHhVUMCDH8j7mxhYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سخنان ترامپ، بخش‌هایی مرتبط با ایران،
ترجمه ماشین:
🔻
خبرنگار:
درباره ایران، امروز صبح گفتید اگر عمان مانع بازگشایی تنگه هرمز شود، حسابی عمان را بمباران خواهید کرد. آیا می‌شود گفت صبرتان در برابر عمان، این شریک راهبردی، تمام شده؟
🔺
ترامپ:
نه، فکر نمی‌کنم خیلی خوب رفتار کرده باشند، اما خیلی راحت با آن‌ها برخورد می‌کنیم، مثل کارهای دیگر.
🔺
ترامپ:
وقتی اخیراً با رئیس‌جمهور کره جنوبی تماس گرفتم، که از او خوشم می‌آید و واقعاً فکر می‌کنم آدم خیلی خوبی است، به او گفتم: «مایلید کمی به ما کمک کنید؟ ما برای ایران به کمک نیاز نداریم، اما اگر مایلید، درباره ایران دستی به ما برسانید.»
گفت: «نه، ممنون.»
من گفتم: «یک لحظه؛ ما ۳۹ هزار سرباز آنجا داریم که از شما در برابر کیم جونگ‌اون، همسایه کناری‌تان، محافظت می‌کنند و شما نمی‌خواهید در یک عملیات نظامی خیلی آسان در ایران به ما کمک کنید؟ این عجیب است.»
گفتند: «نه، نه، ترجیح می‌دهیم درگیر نشویم.»
من می‌گویم خب، پس چرا ما درگیر کمک به شما هستیم؟ من می‌خواهم به آن‌ها کمک کنم، اما وقتی از کسی می‌پرسید «مایلید کمی به ما کمک کنید؟» و می‌گوید «نه، ممنون»، بعد ما داریم در برابر یک کشور از آن‌ها حفاظت می‌کنیم و خودمان میلیاردها دلار می‌پردازیم؛ این کار برای ما میلیاردها و میلیاردها دلار هزینه دارد.
نه فقط برای آن‌ها، بلکه برای کشورهای دیگر.
به ناتو نگاه کنید. ما صدها میلیارد دلار هزینه می‌کنیم تا از اروپا در برابر روسیه محافظت کنیم؛ صدها میلیارد، عمدتاً در برابر روسیه، اما در برابر چیزهای دیگر هم.
بعد می‌گویند نمی‌خواهند وارد موضوع حفاظت از تنگه شوند؛ همان‌جایی که بیشتر نفتشان را از آن می‌گیرند. آن‌ها ۵۰ درصد نفتشان را از آنجا می‌گیرند و نمی‌خواهند درگیر شوند. پس چرا ما این کار را می‌کنیم؟
تمام چیزی که می‌خواهم انصاف است.
🔻
خبرنگار:
با منقضی شدن تفاهم‌نامه، آیا امروز به رسیدن به یک توافق نهایی برای پایان دادن به برنامه هسته‌ای ایران نزدیک‌تر شده‌اید؟
🔺
ترامپ:
خب، آن‌ها می‌خواهند توافق کنند، اما قرار نیست آن نوع توافقی را که من ضروری می‌دانم انجام دهند.
ببینید، ما فقط به یک دلیل آنجا هستیم: ایران نمی‌تواند سلاح هسته‌ای داشته باشد. متوجه هستید؟ ایران نمی‌تواند سلاح هسته‌ای داشته باشد و سلاح هسته‌ای هم نخواهد داشت.
و همین حالا، اینکه آن‌ها بعد از کاری که قبلاً با بمب‌افکن‌های B-2 انجام دادیم یکی بسازند، قرار است... قرار است خیلی طول بکشد [نامفهوم].
اما ایران نمی‌تواند داشته باشد؛ خیلی ساده است. آن‌ها نمی‌توانند سلاح هسته‌ای داشته باشند.
🔻
خبرنگار:
هفته گذشته گفتید که به‌زودی تنگه هرمز را قلمرو ایالات متحده اعلام خواهید کرد. می‌توانید بیشتر توضیح دهید؟
🔺
ترامپ:
خب، به نظرم ایده خیلی خوبی است. بله، منظورم این است که ما آن را کنترل می‌کنیم. با محاصره آن را کنترل می‌کنیم. ما محاصره داریم. با محاصره آن را کنترل می‌کنیم و ایده اعلام کردنش به‌عنوان یک قلمرو را می‌پسندم.
ما کنترل کامل تنگه را در اختیار داریم. حالا آن‌ها می‌توانند دردسر درست کنند. می‌توانند در آب مین بگذارند و مردم خوششان نمی‌آید کشتی‌های میلیارددلاری‌شان به مین بخورد و از این قبیل.
اما محاصره بسیار مؤثر بوده و می‌دانید، داریم خارج می‌کنیم؛ حالا شاید این متوقف شود یا شاید حتی بیشتر باز شود، اما ما هر هفته میلیون‌ها بشکه نفت خارج می‌کنیم. اگر به اعدادی که ثبت می‌کنیم نگاه کنید، داریم این کار را می‌کنیم.
تنگه باز است و قیمت نفت در حال پایین آمدن است و به پایین آمدن ادامه خواهد داد، مگر اینکه تصمیم بگیریم کاری بسیار شدیدتر از کاری که الان می‌کنیم انجام دهیم.
ایران در دردسر بزرگی است.
آن‌ها تورم ۳۰۰ درصدی دارند.
کشور به‌هم‌ریخته است و ارتش کاملاً شکست خورده است.
خیلی ممنون از همه.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 316K · <a href="https://t.me/VahidOnline/77927" target="_blank">📅 23:24 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77922">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/gpron7fxl8ahVfLA1EHCxRUYKBPQAWcz83tAsDR2tHSVxMo3SN18yEK5mkiw4P5VtZkoAez9F7qxlf0gMv3TPQxcUgJidj2LzgcJ5rdRPIKU0DRsEvv1O9URgENUgYEMe638cu6_LUHN9hHM5H93FtF_-TPlztPiX6rG5ty7OB_4YAC0RkqDH1xiFvXY-PVVcZH_JvNtVzMYc3lJmMPXWZs2bK_6851SgE0l9skTSxHNReriTxWQoY2ESOfSkvp3ZjZJOU-l182LP14S470OQMQWCT_5ImxvCZZJ49L6ZYnur-xR59KpHQD-ryjxsa3a0UKyjw8D_N6vUVWWU1TtTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/d4485798f8.mp4?token=PTvWY66cIeeMR_s4MzANnkMOnisF35ZMy4azPkc77cRxf0N3W9RZZfOrDeQ4J3al179vetF4faKF9ystGetUBYpJsIdJM-eXDj_wt75czsc0qQhi22xvdi69556SWB81iNc2i1aEymg3NzbeWfl3E80i_97IBYeYtbqq7TgxkVwTNyapshMcJsTQJZZqfRvSoMXlfyW3pr2NmMNukRgtTnG80fY1juzl5eMtTe8muvzCRz7M2gvZTduy-xI9ew7m9gWWO9jAv-qP7qdCHhEdLznCnkMrudSCUY04RB0ytnhpjCr1_Wv4YSxjXzEpTf4M8IN-_Pud5MQC-ZMcMswUSQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/d4485798f8.mp4?token=PTvWY66cIeeMR_s4MzANnkMOnisF35ZMy4azPkc77cRxf0N3W9RZZfOrDeQ4J3al179vetF4faKF9ystGetUBYpJsIdJM-eXDj_wt75czsc0qQhi22xvdi69556SWB81iNc2i1aEymg3NzbeWfl3E80i_97IBYeYtbqq7TgxkVwTNyapshMcJsTQJZZqfRvSoMXlfyW3pr2NmMNukRgtTnG80fY1juzl5eMtTe8muvzCRz7M2gvZTduy-xI9ew7m9gWWO9jAv-qP7qdCHhEdLznCnkMrudSCUY04RB0ytnhpjCr1_Wv4YSxjXzEpTf4M8IN-_Pud5MQC-ZMcMswUSQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تصاویر دریافتی: آتش‌سوزی بزرگ در میدان شهرداری گرگان
Vahid
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 338K · <a href="https://t.me/VahidOnline/77922" target="_blank">📅 21:13 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77920">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/pC20KoWlwZ8tPFf3B29QnjgDkQxGMKlDTJIF57JhDtLE5XPEsvhEfmdhPaNAJt08xjsmxUeq1wYQMwdDRIenujWlcNMhw1gTmu5rf5kWJBMWD4q58cti-nh3Wuj6WSYIVOHpL6FMMOvzbN_Vm8uZiTTkhVqcR5NOmMZqzFJaUPG37UgOWdAN_f3LRPiLLtBNWVNxGO3DXVmB_s6jKtZTyHGWI-sxcRnct0dS-ZuKlhHY7XkTVObSDO4gClusZe7pzGGSbjiMGSHseKr1FjlKjrnDtdOlQ6w7lIG7qgGDTbORUFziaV_JDrTSV_8Cz_wuEh7fLe8N2sD9eRi1w1iFTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/43c261d593.mp4?token=Vrikm49AvkWui-fcqUOBeJwueHwnHFcOT3eEi3_mfgNxgxB0L7pgWHy4C0c_C1omU5r-jvAjq6bBNjaTwsxJJg4H3iLVkXRd2onYM2AaO6A2j8XGu3jzM3LhwXEmbhaSj_gUXcntd0_q--A5XISHps472GVkXgrFSg_uNut0ayDo05_cDaDtxBZZUCAZnEQYFADHO8GhIxJTwNTdLmY5tY1Qp1d0ZK7TMoofSxjFIvKW_j0UURtQqdOQJZTHsFlSvGvH93-RKCPxByAwT6iewRw1lDgFesZlubzTPiBf-ngfz056OHqyf4GP1gCaNZkuT199EyVDFexBdqPs_tWM6Q" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/43c261d593.mp4?token=Vrikm49AvkWui-fcqUOBeJwueHwnHFcOT3eEi3_mfgNxgxB0L7pgWHy4C0c_C1omU5r-jvAjq6bBNjaTwsxJJg4H3iLVkXRd2onYM2AaO6A2j8XGu3jzM3LhwXEmbhaSj_gUXcntd0_q--A5XISHps472GVkXgrFSg_uNut0ayDo05_cDaDtxBZZUCAZnEQYFADHO8GhIxJTwNTdLmY5tY1Qp1d0ZK7TMoofSxjFIvKW_j0UURtQqdOQJZTHsFlSvGvH93-RKCPxByAwT6iewRw1lDgFesZlubzTPiBf-ngfz056OHqyf4GP1gCaNZkuT199EyVDFexBdqPs_tWM6Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آتش‌سوزی بزرگ در مغازه‌های دور میدان شهرداری گرگان
تصاویر دریافتی: 'ساعت ۱۹:۳۰ دوشنبه ۲۶ مرداد'
Vahid
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 314K · <a href="https://t.me/VahidOnline/77920" target="_blank">📅 20:40 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77918">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/tQpIExAuWI_U6HnhCH6H4T5vaa1xE03OG1HXtWjxK_BIRV6r2M-_uMG6MsCjd39HTmVFR__7w6y_YgKch5NaseRGkrm86h4gbRtn5JoYgEXQng3vjGnchclMFc_S3bbonSiFFiWCGtgZsu46HqOc7j-NFJ1LdSFz9bBHwMTamWk8CuzBmJSfnx0AoTni883z4ImM_1-F9zdbIkzSFCzHcHFhD9wI0Wahm5w9fekR74J5UwpQ6HuYde_b0h2E32G7ECVpiNCse4mYmTXZcMhUIRwGr_PHxMECo6vSoe6Lxm1uk-VhPXuq5CrD4U5Zr2fdWu4Raklwyu6rImtF3cG4Ow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/NtHZ7RURKs7SRzdafgi58cB1yDBGvGCsFJV4aCVx2g_sNqOGJdxhmD2gQn1caAv9jp5-oisWjZbaLeQXlPRvptglOpcVu7z8MWALOX_4a7Ryv9ovf1Cqdg5dRcFMEwWZLaKwJR9IIE3bckzxQFjVnhGF1XVG29tCdr6Cr_kmgK_8eDJzTamVgqn51LhQElV5vk3BYVXoZ1nchdtKlMJf2i1ueHHMpQ8HG7RiFaQMDSoaJS0r2vwZQzbRu9JkhWWFTKiYNZmr4wpioPsoMlS8n0B2YGtdUfNTe4FMjVegv_a2K754YQiIKCQbSsxhTjU6r7pkmC7uMRAx_g0diTDqrw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">دونالد ترامپ، رئیس جمهور آمریکا، روز دوشنبه گفت که در مورد پرونده ایران عجله‌ای ندارد و به «کانال‌های ارتباطی پنهانی با سپاه پاسداران ایران» اشاره کرد. او افزود: «ما به صورت مستقیم با مقامات سپاه پاسداران ایران صحبت می‌کنیم».
او به فاکس نیوز گفت که «ایران باید پرچم سفید تسلیم را بالا ببرد» و خاطرنشان کرد که «محاصره دریایی آمریکا همچنان فشار اقتصادی جدیدی را بر رژیم ایران اعمال می‌کند».
او افزود: «آنها در پوکر فوق‌العاده‌اند... اما دارند می‌میرند.»
پیش از این، رئیس جمهور آمریکا تاکید کرده بود که «ایران تحت هیچ شرایطی نمی‌تواند سلاح هسته‌ای داشته باشد.» این اظهارات در آخرین روز از مهلت ۶۰ روزه تفاهم‌نامه اسلام‌آباد برای دستیابی به توافق صلح دائم و فقدان پیشرفت در تلاش‌های دیپلماتیک برای پایان دادن به مناقشه بین واشنگتن و تهران مطرح می‌شود.
@
VahidOOnLine
سخنگوی سپاه پاسداران، ادعای «دونالد ترامپ»، رییس‌جمهوری آمریکا، درباره وجود کانال ارتباطی مستقیم و پشت‌پرده میان دولت ایالات متحده و مقام‌های سپاه را تکذیب کرد.
براساس گزارش خبرگزاری «تسنیم»، حسین محبی گفت: «هیچ گفت‌وگویی میان مقامات سپاه با آمریکایی‌ها در جریان نیست.»
او اظهارات ترامپ را «فانتزی‌هایی» ناشی از «توهمات و کابوس‌های ناشی از شکست و استیصال در جنگ» توصیف کرد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 318K · <a href="https://t.me/VahidOnline/77918" target="_blank">📅 17:44 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77917">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/h3yDRAVP8qOgbJv5eZnkgEQMCc1mhcdVP1ZQJIANnewXPVKgYZ3pboz1L9bkWFK_jZWLRmsqzf5plg2blywU5fFUIHTomFuT91x6oCR58xTH1QLf77PLUtC46dLj6Y_BL2pE7QKziuIWx5FP_Nbwcnkv2dAHceFpW8eed408YaMnL2Uhkt-U3UDOBvw2u7TI0DY5R0Uo9J6gVjdWx0OoM7k29T5s-nxnL6PNb2x6xu71FPrPIo_R8VTfbXCGUYyHP49jFVmO4bhlbcsoN4FAmqUlXjQU-Q8kW5-rs6j-FXDAqUFWYKnqZ8CbbdsiJOTg3XZpnh0bT4NyU3-uubKSgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اداره مبارزه با تروریسم اقلیم کردستان عراق اعلام کرد دو پهپاد که شامگاه یکشنبه ۲۵ مرداد از داخل خاک ایران پرتاب شده بودند، دفتر مسرور بارزانی، نخست‌وزیر کردستان عراق، و همچنین منزل رئیس اطلاعات این منطقه خودمختار را هدف قرار دادند.
بر اساس اطلاعیه روز دوشنبه این اداره، «دو پهپادِ حامل مواد منفجره از نوع حدید-۱۱۰، از آن‌سوی مرزهای ایران به سمت دفتر خصوصی نخست‌وزیر اقلیم کردستان و اقامتگاه مدیر آژانس پاراستین (سازمان اطلاعات اقلیم) شلیک شدند. خوشبختانه، هیچ‌گونه تلفاتی گزارش نشده است».
مسرور بارزانی در پستی در شبکه ایکس، به شدت «این تجاوزات گستاخانه و غیرقابل‌قبول» را محکوم کرد و نوشت که «این اقدامات به منزله تشدید خطرناک تنش‌ها و تهدیدی مستقیم علیه امنیت و ثبات منطقه است و چنین حملاتی ما را از ادامه انجام وظایف و محافظت از شهروندانمان باز نخواهد داشت».
انتشار خبر این حمله یک روز پس از آن صورت می‌گیرد که وبسایت اکسیوس گزارش داده بود دولت دونالد ترامپ در دور قبلی مذاکرات با تهران، از رئیس اقلیم کردستان عراق برای برقراری ارتباط مستقیم با فرماندهان ارشد سپاه پاسداران کمک گرفته بود.
@
VahidHeadline
اسماعیل بقائی، سخنگوی وزارت خارجهٔ جمهوری اسلامی، این رویداد را «بسیار مشکوک» توصیف کرد و خواستار «هوشیاری بیش از پیش همهٔ طرف‌ها» شد.
عباس عراقچی، وزیر خارجه جمهوری اسلامی، نیز در گفت‌وگوی تلفنی با فؤاد حسین، همتای عراقی خود، گفت «هیچ اطلاعاتی مبنی بر آغاز این حملات از داخل خاک ایران» ندارد.
@
VahidHeadline
📡
@VahidOnline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 299K · <a href="https://t.me/VahidOnline/77917" target="_blank">📅 17:41 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77916">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/0d5ca5b6b3.mp4?token=vEfO7dTCm8lf0rMFN7WR1pNh8aEKszsjJsymMtlHVcap_i2oldAwCAxBYokbxp9JPcYDBgA5yU9J4yIpsWnn66ysi9pjrcefZjQI94nIVSt110g9vZy6N_V3Ht6OvEwyWNJMa-x5ST5QB2jWXVwWuktL8ZvEz-A89Crd87rqSz8UE-HWLSBmKx6tS9gocryVnJR3_kezKvE3FoVbM-PgvVuJo9oA7aUVYf0yALD8u-VGl53p1-TLsdFSG3zZJ4UNGD5qZPwSAblePPtQ8WVJk27-BQ4eM6RHzYaxhlIv6kqsERAhKH0X-1TAshsfoXv1ubihV_6N7DIXyKfhgXbf3w" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/0d5ca5b6b3.mp4?token=vEfO7dTCm8lf0rMFN7WR1pNh8aEKszsjJsymMtlHVcap_i2oldAwCAxBYokbxp9JPcYDBgA5yU9J4yIpsWnn66ysi9pjrcefZjQI94nIVSt110g9vZy6N_V3Ht6OvEwyWNJMa-x5ST5QB2jWXVwWuktL8ZvEz-A89Crd87rqSz8UE-HWLSBmKx6tS9gocryVnJR3_kezKvE3FoVbM-PgvVuJo9oA7aUVYf0yALD8u-VGl53p1-TLsdFSG3zZJ4UNGD5qZPwSAblePPtQ8WVJk27-BQ4eM6RHzYaxhlIv6kqsERAhKH0X-1TAshsfoXv1ubihV_6N7DIXyKfhgXbf3w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بخشی از صحبت‌های یکی از مجریان صداوسیمای جمهوری اسلامی که می‌گوید «جنوب ایران، فدای جنوب لبنان»، در ۲۴ ساعت گذشته در شبکه‌های اجتماعی فراگیر شده است که با واکنش تند کاربران همراه بوده است.
خبرگزاری صداوسیما روز دوشنبه ۲۶ مرداد با بیان این‌که این صحبت‌ها «تقطیع» شده است، ویدئوی طولانی‌تری از گفته‌های ریحانه قاسمی‌زاده را منتشر کرده است.
با این حال، آنچه در ویدئوی منتشر شده از سوی خبرگزاری صداوسیما هم دیده می‌شود، همان صحبت‌های پیشین است.
در این ویدئو، مجری صداوسیما در واکنش به انتقادها درباره حملات هوایی به جنوب ایران، حرف‌های منتقدین را «دلسوزی دروغین معاندین برای ایران» دانسته و تاکید می‌کند: «جنوب ایران، فدای جنوب لبنان».
در زمان حملات هوایی به جنوب ایران در ماه گذشته، بسیاری از ایرانیان در سراسر جهان با مردم جنوب ایران به ویژه مردم بندرعباس ابراز همدردی کرده بودند.
@
VahidHeadline
با توجه به چرندیاتی که قبل و بعدش میگه به نظر می‌رسه منظورش این بوده که مخالفان جمهوری اسلامی درباره جمهوری اسلامی این رو می‌گن که جنوب ایران رو فدای جنوب لبنان کردند.
اگرنه وقیح‌ترین‌هاشون هم درباره مسائل ملی مردم‌فریبی می‌کنند و این طور صریح نظراتشون درباره «ملت فدای امت» رو جار نمی‌زنند.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 271K · <a href="https://t.me/VahidOnline/77916" target="_blank">📅 17:28 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77915">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Np7_i470gkBmugSBZCzgKL1EmoTglhOyYdKhYg8HeTeq-cUV_tS0_Bm3BEnVOnA8ehvOQvRAiDmhuI9ONOq7yn5aMmgBswAtxYpgm9F_eCvqTSYkHuFx_z24-RLOBPyUslA4PVmnfBcJlaPLNGf7Uwu22iflPVr-8__XLivkZ0vqfJgZt8ohzYhC0_gXS8s1rb5qPEWK4iESuSXBdDXJZyCu2I7rn9HfWxFLqyEk1aJ0nI8ckzyPYDWQNVWKHPX7kjFX0rIOj0WhOXRaGWPfxdrA-3yYh0627STX6Z-YmoMtRGEmCeSU8hymoVQEyuc6XGJaJE0wUZo6r7XV9UTGCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بنیامین نتانیاهو، نخست‌وزیر اسرائیل، با انتشار تصویری از تبلیغات حزب لیکود در شبکه ایکس نوشت: «نگذارید آنها برنده شوند.»
در بنر منتشرشده، تصاویر زهران ممدانی، شهردار نیویورک، نعیم قاسم، دبیرکل حزب‌الله لبنان، مجتبی خامنه‌ای، رهبر جمهوری اسلامی، و رجب طیب اردوغان، رییس‌جمهوری ترکیه، دیده می‌شود.
روی این بنر نوشته شده است: «این بار نتانیاهو نجات نخواهد یافت و ما به او اجازه پیروزی نمی‌دهیم.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 251K · <a href="https://t.me/VahidOnline/77915" target="_blank">📅 17:23 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77914">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/h-Ss0KiCZkZ5x1UikAwt7Faf6R1CqQzP9NBi-zG8uU3u5Avqx9ezb03eSh0gr-99zLwCTtLuS8uwvvSSz0fCo6EJbNOTfVuKSr80IWSou-GbfpntBtDuZXS3JYwVgvxeQ-AXMCh_4Yu_YV5sJ_y6tX-f2VV2p-CcljtWWvpNCxDNwGs6Lmb9OqNG0kGjaXbARHKtjcVlmhrdRzFr6cDg875pLa3KTMwsJFvfLqP8jBz2MG1s-8JfJz-eu1zoncMNklr9WI40xtoZvfoEyZk7erS8c7NB3p9upHHNsUYwDQuL9ThRNXx8hSSvitu-9YHoC6Ckk-TaAX9zB5wyh1wnNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«ملیکا همت‌زاده»، دختر ۱۳ ساله اهل روستای دسک شهرستان نیکشهر، پس از عقرب‌گزیدگی و در شرایطی که به گفته پدرش امکانات و داروی مورد نیاز برای درمان او در دسترس نبود، در بیمارستان نیکشهر  استان سیستان و بلوچستان جان باخت.
پدر ملیکا روایت کرده است: «فقط یک خانم دکتر آمد و گفت سرم می‌زنم و پس از تمام شدن سرم، او را به بیمارستان نیکشهر که مجهزتر است ببرید.»
با وجود وضعیت او، مرکز درمانی بنت آمبولانس نداشت و خانواده با خودروی شخصی مسیر ۷۵ کیلومتری تا نیکشهر را طی کردند و ساعت ۳:۳۰ عصر به بیمارستان رسیدند.
سعید همت‌زاده درباره ساعات بعدی گفته است بیمارستان نیکشهر نیز به دخترش سرم وصل کرد، اما پلاکت خون در اختیار نداشت.
بیمارستان چابهار نیز پلاکت نداشت و قرار شد آن را از ایرانشهر تهیه کنند: گفتند یکی دو ساعت طول می‌کشد. یکی دو ساعت شد پنج ساعت اما پلاکت به دست ما نرسید. تا ساعت ۱۰ شب منتظر ماندیم، اما به جز همان سرم، هیچ خدمات درمانی دیگری ارائه نشد.
ملیکا همت‌زاده سرانجام در اواسط شب بر اثر تاثیر سم عقرب دچار تشنج شد و جان باخت.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 255K · <a href="https://t.me/VahidOnline/77914" target="_blank">📅 17:22 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77912">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/37ca2442dd.mp4?token=KoAkKVxZqqN80tRamagFM5hb-0axPHz6tkT5XWEFua_5rlSU7-RRRMp6wbnl4h1SFYJ8ky60elwWI6ox0F4jSOUHHg5mnjQ2QpL_0JRvS-f23zQ63oW9NaSI8ZKa4xSGrIZp6pGLZbeINLQnUdDihnzasLfyxBLTaFXw008xjfsPSrLe1g6g5S8zGiP3EUfPcw6m6daF7KJuIo_6Pdb1VG7d-3MeTnCwDEhErkgQwvh6MBTOzt9IdUfpq7ecTY9t86lneG5UrW1yKrcg6_mCUOIo5XluU4KjHhv-HjZxFIWBM443Mfb6pqGgTkQ-R3ypSlIIZl6_Ca42voXJijIjSA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/37ca2442dd.mp4?token=KoAkKVxZqqN80tRamagFM5hb-0axPHz6tkT5XWEFua_5rlSU7-RRRMp6wbnl4h1SFYJ8ky60elwWI6ox0F4jSOUHHg5mnjQ2QpL_0JRvS-f23zQ63oW9NaSI8ZKa4xSGrIZp6pGLZbeINLQnUdDihnzasLfyxBLTaFXw008xjfsPSrLe1g6g5S8zGiP3EUfPcw6m6daF7KJuIo_6Pdb1VG7d-3MeTnCwDEhErkgQwvh6MBTOzt9IdUfpq7ecTY9t86lneG5UrW1yKrcg6_mCUOIo5XluU4KjHhv-HjZxFIWBM443Mfb6pqGgTkQ-R3ypSlIIZl6_Ca42voXJijIjSA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ، ترجمه ماشین:
پولشان بی‌ارزش است. نیروهای نظامی‌شان شکست خورده‌اند. کل نیروی دریایی‌شان غرق شده؛ ۱۵۹ کشتی. آنها ۱۵۹ کشتی داشتند. تک‌تک کشتی‌ها همین حالا زیر آب‌اند؛ در کف دریا آرمیده‌اند.
همه هواپیماهایشان را نابود کرده‌ایم. آنها ۲۰۹ هواپیما داشتند. دیگر هیچ هواپیمایی ندارند. ندارند. و می‌دانید، شگفت‌آور است، چون این داستان‌ها را می‌شنوید. رادارشان از بین رفته. تمام فناوری‌شان از بین رفته. تورمشان ۳۵۰ است.
پول نقدشان بی‌ارزش است. پول ملی‌شان کاملاً بی‌ارزش است. بعد نیویورک‌تایمز را می‌خوانید و می‌گوید ایران وضعیت فوق‌العاده خوبی دارد. می‌دانید، واقعاً باورنکردنی است. تنها چیزی که دارند اخبار جعلی است. همین؛ تمام چیزی که دارند همین است.
اما خیلی زود اتفاقات خوبی خواهد افتاد. در واقع، همین حالا هم اتفاق افتاده‌اند، چون یک چیز هست که نمی‌توانیم اجازه بدهیم: نمی‌توانیم اجازه بدهیم ایران به سلاح هسته‌ای دست پیدا کند.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 232K · <a href="https://t.me/VahidOnline/77912" target="_blank">📅 17:13 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77911">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/c9e563043f.mp4?token=gCIVXO_lv1cL9CFITfNMvb3r0x65WGbsjmY2ffpqAKQdwkYusDr1dxd_Kb0NYeswyMILeh3sgFp2zPdEJapWH5KW6JPPiadfYjv7fdcr0NZH2P2E2wLlr3YZ5dkZ-e4dTyhvm87Nc8P9j3kJ3aykmNEVqT_wjYM8KzAMPnTK5LcO9ngPhmH-lwVIFEMQ781vrb-jslESgu60B3Oqwu_DEOoFK9xOR82r6jT1tarFthVBbebq4DmLzLnRKPUwIDCosrtfm9MesxB7p81_sFwcTDIj8O3iHQM4Ta1UTCXqe9dCqknq3TU1ZGKhu6CKiHQ1zxkgN9OxzHgHfJOrulxVHQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/c9e563043f.mp4?token=gCIVXO_lv1cL9CFITfNMvb3r0x65WGbsjmY2ffpqAKQdwkYusDr1dxd_Kb0NYeswyMILeh3sgFp2zPdEJapWH5KW6JPPiadfYjv7fdcr0NZH2P2E2wLlr3YZ5dkZ-e4dTyhvm87Nc8P9j3kJ3aykmNEVqT_wjYM8KzAMPnTK5LcO9ngPhmH-lwVIFEMQ781vrb-jslESgu60B3Oqwu_DEOoFK9xOR82r6jT1tarFthVBbebq4DmLzLnRKPUwIDCosrtfm9MesxB7p81_sFwcTDIj8O3iHQM4Ta1UTCXqe9dCqknq3TU1ZGKhu6CKiHQ1zxkgN9OxzHgHfJOrulxVHQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محمد باقر قالیباف تفاهم‌نامه میان ایران و آمریکا را «سند افتخار و پیروزی در عرصه دیپلماسی» توصیف کرد و تاکید کرد که ایالات متحده و اسرائیل در جنگ اخیر «به هیچ یک از اهداف خود دست نیافته‌اند» و تهران پیروز شده است.
قالیباف که در جلسه‌ای به مناسبت روز خبرنگار [در تقویم جمهوری اسلامی] صحبت می‌کرد گفت: «با تمام وجود اعلام می‌کنم که ما در این جنگ پیروز شدیم.»
او افزود: «در جنگی ناعادلانه به رهبری ایالات متحده و اسرائیل، ملت ما با قلبی باز و بدون انتظار هیچ چیز در ازای آن، شجاعانه ایستاد و جنگید.»
اظهارات قالیباف در حالی مطرح می‌شود که او جزئیاتی در مورد اهدافی که معتقد است واشنگتن و اورشلیم در دستیابی به آنها شکست خورده‌اند، ارائه نکرد.
@
VahidHeadline
قالیباف: ما نتوانستیم آن‌طور که باید این پیروزی بزرگ را روایت کنیم تا حس افتخار در ذهن و وجود همه مردم، جبهه مقاومت و آزادی‌خواهان دنیا شکل بگیرد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 247K · <a href="https://t.me/VahidOnline/77911" target="_blank">📅 17:00 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77910">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/557e36e83b.mp4?token=lJE1zd0xpFRonLtHJD2akSHCOSa8tmNyY2LKAwI_zSI4760NRsskmHaiU9zZjRwRYh-s8ugHol6OI4JFv4O7vrKNsSJWGly1NHaONwOlWnFAyXWC4ZtC6cDopEDVURjekru9f5VID1otntgCUeJXiSrWxR5n6prxOfX8P7w5i8SsdqtZvHptDgCHMG5D5k74-Rx6IrasGGxUCq-58Vzx8NsHIJBCfzC4i3WRtOhV-cRl5NxQtHDWC5T3xFGMg3lKZMqhSMBSfHhR41wB-QV-NKzQNAfvth0DVrNtjyRpzRctHm8kpNP6bzNTzDNIlOmuFN1p5iu79Dno8Feo53MeMg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/557e36e83b.mp4?token=lJE1zd0xpFRonLtHJD2akSHCOSa8tmNyY2LKAwI_zSI4760NRsskmHaiU9zZjRwRYh-s8ugHol6OI4JFv4O7vrKNsSJWGly1NHaONwOlWnFAyXWC4ZtC6cDopEDVURjekru9f5VID1otntgCUeJXiSrWxR5n6prxOfX8P7w5i8SsdqtZvHptDgCHMG5D5k74-Rx6IrasGGxUCq-58Vzx8NsHIJBCfzC4i3WRtOhV-cRl5NxQtHDWC5T3xFGMg3lKZMqhSMBSfHhR41wB-QV-NKzQNAfvth0DVrNtjyRpzRctHm8kpNP6bzNTzDNIlOmuFN1p5iu79Dno8Feo53MeMg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">احمد آریایی‌نژاد، نماینده ملایر در مجلس ایران، در یک مناظره تلویزیونی، کشته‌شدن مهسا (ژینا) امینی را با عبارتی توهین‌آمیز توصیف کرد و اعتراضات پس از مرگ او را «هشت ماه اغتشاش» خواند.  این اظهارات در رسانه شهرداری تهران (همشهری) مطرح شده است.  پدر و مادر مهسا…</div>
<div class="tg-footer">👁️ 236K · <a href="https://t.me/VahidOnline/77910" target="_blank">📅 16:53 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77902">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromVahidOOnline وحید اون‌لاین</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qibO3R3uQypcxfmxpUvWxA-ANY76rytBe9yqBM8fVsJcXM9LGSw4UHDzUj72uk6JRqq2CZS6fySoW_lQdPIyIDBdaw2Z8Ycdg1wdQySbtrv1EXSIxmuGwlS1PJT1sBungSxgcbTwilWVgtJtkEme6IJaaA_Nv-e9KRvnCbDnDXsVMk3Mh-IFoaF4rumEz_660Wsp9zoXuCHZpbMlY-sc18xzVSnVQPVY-dEvAAszNQpvyeV3tfUs0K4NF7rDRr9IJLJGs8lfOXWH_3RcUuas3FjETLbKRxZ3lpqwn8hhtWIWq8BAftAZ--hCuQc1BgE9GTpzAcDTJqmiXiGKZmHO7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Cal4sAojT4k4vZ75ZoAPEmWZ0qW_ByFHJHrmHOZWYsQLpK9LBR3w--Vlw2qHavdMVSoGJlAgeYN7m922AIGcWRGdHTHzcQJTwJUKJpqIqr5wyA1uKAIL-yf5dvQQqSTLB_F6MQ57KL1N6kL8I7LSyPGT2BLTmAg3Pm_1K057iH26IZj9jlTH1GqQq2mUA3_WwYgxT7z6n5Zfucie25C_Ik00hcSeNytZJ2tg3ed4vk7GogJ411KhLZy-2BE1UfLnIPADv8ELE7BOjjq1r_vz1PfIFEKhFOBlUx8ll5ZGFG9LqvImkP1m_Y1_3VtaX2aUlgm6IHoscEcm4RT-4yjz7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GAZ33QXtY-LbbG0YCMA4tp_FDx-cXs_-QCrRrrC8O4IEP_0ZmKIXL9GOzMuFuMO4WqUYyCp3lnYZDVPHnGTNGW00PR9nzAYiPIfhk1M9Itv2wM4edw0sPC2dDXiJX-_BKQVKOQ6EGjDaCWvL5cCkMsCwECAaxSuVopM4TGO17GzSqchpRo-XghB0R6GFMPyY20TjcwozegsEgRna5quS1YTGm8deLksx4q_V96JwTgDkaHhc9X7SA-sxVkpLikdg0pvbC95ypu3Q80EARLyhmO2qFztspUsCoGIxkzlnWUYM6YpVbBiZy-PziGqYf8EvJULHIs_S3Pf5nZ73SISE7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ex9FClY2ItcZMwjDw68234UuOltq6uO767sYxr8d8-nHrHbzp-aPvn1Si_5AHGWcltVLXZG62i9bWXucpztHYGttP8eJOFQtRRZNKvVUNC6QR2FyzCn9wYphHPnXXzYxGLVYdGFRjYsp6C9KFoeJ7CRzg7G2nCOD70Pc6XbgXNLVFl6RNR27XJsVf_Ju2ktREjvxP4pJLK1FVP6vxRxTc6zE1NETj2X25bvpCJ6HiFsbmecLawbHYuX_rj5tcCtZEB6NwPJmFyqvVSXX3ExTRziaM2Pb42ZjE1wKoQFoWu-bQJQmAccfKCBhFxhXhVO30FiYYsp5TZcRhBx4enxpFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ld4prHfH5iNbDXWD1Seq2xuXDkSXPdEU2Ca1BDzYSnCWU-9ob1Kh70yPjJZMBTI-WCLlq6b6_yKii7NZMWVOIOZkcxMb9ckB397v4Twcdeg9qwVnjUiNBWyaFzoV9g4o844XoxnzicNNcCk67G2ROJyxULyfWPxmUXZsCjPFBR6KbZCQdpkJBSZRfiATeGOYbyj8RCjsxErtawcu-RHsSmbwNszcdWzP8lk62tzHeqGwWvKU0gPeDS7ZlkeHoBoiouZusuLJqydCq9Oazh-0YmkSnQaBBkyR2c9OgtiX2y281Od1mVBIn6KHzSQsD714ycNRlUjxLY1HJ8tT3D675w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/o5kmW2T0oAR2roCglpwvmTCM-pCDnJ3MrxE7GAySK5Uh8Vl5aic2LCGzafsWRoRJQCUQKYD3ITwU6cQZiadCf_wfLte2b-N8T4V9ec6UUrzAJObOs9uNZctMBq54P-Q2Jt3-O0GYU5bCDnFsymZAUC52hV8FLSk4pm19CXdUYdoak9fezG0jrvd-qkPjPmzOL8B5HQIeCRFfoUFh5XguEfGtcNnw_YMknriIMGgU8ivfcfaGSJ47zyL2jjQl7LsLNhB8wwCGERoFAo9rjPyZefMBF7lemOvpeXGAKaXN_xAV91jav3WdtnSPtLh-9C_U8zrMFX951StkbGRlVsyEAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/j0mMlqswlfgsc9hJksMORAN2U9fpvI1UM0HCYIDVRznzTAbJBgaxaKPS_ztlI1s6wZW_Ai-LUWiIhBw98hAZ3V5I9jBvu1-qVNyrEGWHb4ajdYiiid-2ITQr3vURTkFUVakSSQrje2JkGLk4WfoHnLv7GTBbGvb-52YzF3a6nYxHqWXD1DJ8h_tI4fubsXqVLdgJWuMNTtsaAyovpYSNnIRLEhCT9sOnncQzt1ApNFwWHrIX5CQ4gRAD5QdSWP0rRPeyvCklEC61K68Z3ic8JE2GOThIGdrhBk89sFtDbR62SLUISDsKfMwmXDoZejPC5DL1uGajw5h2GWR8cFbSvg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d1adb18b17.mp4?token=VwYwtmDwoH5SoFbNuoX_MA84k7_75Ejfw1dzQIeBZCOIiK8fXF7eNYbkPJTCA87JBf7vfVe6DXX12urQpCV3iTxieSAkMaCyV5P71k7tppe-oWfQsw5JvbGqSIqCkzOL_MbAyHdrppxm9Y88Xdt0AuxZ6pcLBMAAqZJeBegP50xp2Q97sLpurxUhAXT0xObyk1zTGqEhanyozYy6Gog5mKB4Z6vSJ1QXn7fVgJlKqsPZjygmMDqjLefUMIOo7BbrJ7m1kZKfisKcnOLwyZUbVXDd-tg6HFVtLEm-YqXu0Hmv6Fk1vWp6gbDOjL-0df08M8HxYkzN8gbyyFIG6CuvdQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d1adb18b17.mp4?token=VwYwtmDwoH5SoFbNuoX_MA84k7_75Ejfw1dzQIeBZCOIiK8fXF7eNYbkPJTCA87JBf7vfVe6DXX12urQpCV3iTxieSAkMaCyV5P71k7tppe-oWfQsw5JvbGqSIqCkzOL_MbAyHdrppxm9Y88Xdt0AuxZ6pcLBMAAqZJeBegP50xp2Q97sLpurxUhAXT0xObyk1zTGqEhanyozYy6Gog5mKB4Z6vSJ1QXn7fVgJlKqsPZjygmMDqjLefUMIOo7BbrJ7m1kZKfisKcnOLwyZUbVXDd-tg6HFVtLEm-YqXu0Hmv6Fk1vWp6gbDOjL-0df08M8HxYkzN8gbyyFIG6CuvdQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ایران از نگاه جهان: مهم‌ترین اخبار و تحلیل‌های دوشنبه ۲۶ مرداد ۱۴۰۵
ManotoTV
🤖
@VahidOOnLine</div>
<div class="tg-footer">👁️ 234K · <a href="https://t.me/VahidOnline/77902" target="_blank">📅 16:51 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77899">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromبنیاد عبدالرحمن برومند برای حقوق بشر در ایران</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ofOs06-JHN3120ZPBtIBGtevuiPIdx_MNNJ-iAiv_a1OgAWC649bHWocN-Fu8WJ9PInkNmhVWhih5zuwU7D1diwamtDkiapzHW5gbjLPUg7Lfi1QmDsniSXMdrYI-8j4a8vPzBuRzENcAAlp1hKtSQxa1F0gmk-P505HPHp1WJI1IWr1KTTUletccUo27xKae0BJgaBIkwCHobMUXmZ9SIq1OCi4aihdBO2FWYMBP2hhE1zkiTR76L8HTykspDpVLMGEXY_zg1mfpdO0RhbctcUEBqwdUnNEC2b989IyRJozAQJ3brMi-9oWmoSa4N6TSCgBVoheF1zwr2DlTuCbsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hgqNo0rwZjqfqGnBakzzj4VIk1-oSCsQ7Exun6gFDPHlaquklr6SQkhtdKv1Ej1IGfdR7OtlCCkjvD07ZyGX6XVLWiJP63rE6FhQiGrR3X0OLnEXpkN50YgQvtR7gujZmKOrc-5mDyZpI4qdAvkaHJkflZScmqbuBXp7K38jMaiJ2VjqdYbIpbCmSuoDmEoiQUbHkDeDrN6KbDozf7ZfG7M6OWKBdVXA7eaMvCRTujK-C-Vrwbg0nUh2WG7NZTxhj6v9xhtM_dQtgL2_cuyxzwuG3gQe31QtKisbFn0RPke49bcKLYaVSd2wRx0678weImNd1Wxvbho0PB39e8XXFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YVy8ka8W1A4HBbfdZn4Qtcz2tGglLgjAlhWJaLv3QNH-fVHS647gyUu8wpXeGETF1pQePbqkFI0IMK7nvqyYfGvBCQvGGYC_ha9EOSlJOBRxT7zwn3P7l0BvmcL7ukUtuB5Y3YUmj3YBNXVWLhbZKGuCObDBsY3KMe_sGGx1TGqn1eyxat_8BwOUWof2bWgAwz0pGAHhgt6iLci4LMLXyFWA3Re3nJsl9QkLUo278tbwKlrYCPkSi1uMKdrPYJExe2BHKdMb8dmPmpmKsMWp607MQwI5VYkWuUFZeBkLJV1ilpx4WHGRdqM2RXnSk61FrEf6r0GeRuTbpm6vasaa0w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔴
شاید کمتر کسی بداند در سال ۱۳۸۳، در چنین روزی یک دختر ۱۶ ساله به دلیل «رابطه جنسی خارج از ازدواج» در ملاعام اعدام شد.
عاطفه سهاله با استشهاد محلی و شکایت پدربزرگش دستگیر شده بود. او قبل از آن هم به همین اتهام در مجموع بیش از ۳۰۰ ضربه شلاق خورده بود.
‏
🔸
نگاهی کوتاه به این واقعه:
https://www.iranrights.org/fa/memorial/story/-3134/atefeh-sahaleh-rajabi
@IranRights</div>
<div class="tg-footer">👁️ 282K · <a href="https://t.me/VahidOnline/77899" target="_blank">📅 16:50 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77898">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/5da532981c.mp4?token=cLtkleH9ANCeo0Z0w90rBFrr2HhGcVYejI44YGgljImiqKLpaxLddbArF3O12NOxFQJYVpv_E7G8KZNc3iC04o4ziFjRA1ZyBCh81SUrer-36jHv2tGK2P7TFtsOadPfkXuPs3bcYMKkEEjFruUuzjWs9ugRtmAGPi_X_lmkokJCCg8CY4PmRDDsyta1j5QYmk5YPvJ_nX8_nPbxb9wjZWG0ZXu0rQxNg0oRMtkIZbiuldsFe3Isyb3I5BV_27AF3H522DPPtBCBmREzN8jolkGi09o2HZ9pO91Z3S4LumZMiUpVYnZNP0o4Rp-lolJyYgM5tz2HIB7QXw-QvhN5uw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/5da532981c.mp4?token=cLtkleH9ANCeo0Z0w90rBFrr2HhGcVYejI44YGgljImiqKLpaxLddbArF3O12NOxFQJYVpv_E7G8KZNc3iC04o4ziFjRA1ZyBCh81SUrer-36jHv2tGK2P7TFtsOadPfkXuPs3bcYMKkEEjFruUuzjWs9ugRtmAGPi_X_lmkokJCCg8CY4PmRDDsyta1j5QYmk5YPvJ_nX8_nPbxb9wjZWG0ZXu0rQxNg0oRMtkIZbiuldsFe3Isyb3I5BV_27AF3H522DPPtBCBmREzN8jolkGi09o2HZ9pO91Z3S4LumZMiUpVYnZNP0o4Rp-lolJyYgM5tz2HIB7QXw-QvhN5uw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">امیر حاتمی، فرمانده کل ارتش جمهوری اسلامی، روز یکشنبه ۲۵ مرداد در مراسم گرامیداشت روز خبرنگار [در تقویم جمهوری اسلامی] گفت: هر کسی، هر رزمنده‌ای، که یک  آمریکایی را بکشد یا دستگیر کند و تحویل یگان‌های ارتش دهد، هدیه‌ای معادل ۳۰ هزار دلار (حدود ۵ میلیارد تومان) دریافت خواهد کرد.
بر اساس  گزارش صدا و سیما حاتمی همچنین اعلام کرد زنانی که موفق به این اقدام شوند، دو برابر این مبلغ جایزه دریافت خواهند کرد.
@
VahidOOnLine
او در ادامه گفت: سلاح هر فردی که موفق شده نیروی متجاوز آمریکایی را به هلاکت برساند، به دو برابر قیمت خریداری شده و سلاح جدیدی دریافت خواهد کرد. سلاح فرد نیز در موزه‌ای که پیش‌بینی شده، نگهداری خواهد شد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 380K · <a href="https://t.me/VahidOnline/77898" target="_blank">📅 20:13 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77896">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/ORJAOXhDNB3XHH5FkTREFhAJoFMb8StjngNDh90tbv549dpbOnEsB797pMOlbVp1A3-9dIR58q29gUoj7GXHF8V2Xj-UNjIYmneT2AuPsX8rHgiYrbpT1MbfYjEmu8VA6bh-kzcAIt6v1FqEFbUPUVtw93bYSsJHrZ2Y-qFU6ti5lQZR5PT3LKWN504o4ihtVsZqSFUciNlN8uPYahJQargrpAzl0dd9ejV14pupcqgsMtp6e6g8F6mx3M5KxFU3FaNV2PcBDBFfLHhRA1wrmWn02OK3rTa--ke53WeprErhcVQ5psU3W2rRiZ17vcA-2N573lmUBzmPrrJoK10FUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/ZALF9XH_TAyb4dwXQaY5OjB5RuLp8wx6ZxB13E6s4Oiupw23kgG_A9j08HaYmi9Y1zeACVdDpAjwfoRD67z5PAXoFcZN9nkUNhzvBtZTBCe15vHBdS1VhxzFCInZ2VB9zHqTq6LhmZbjtdOxJYIobiXRH6gjLQmWE-KuNCKkiOpJWyH8GyaARt9Yo9zcaxkBogUxD8zbfKZwBYtEdBhBIxbfkxpS4dnd85HA3UlCBlEzVMHlJJ-iyCd4GQ2tJsJwssFJn-ojo77j9QsOrsgol6TZpkkdpZnzqW_iymVv6QbafxywgMnUhhdu5yP-0xpk2fFwWXBx5F6Vv7C6UXK1hw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">وبسایت اکسیوس در گزارشی نوشت، دولت دونالد ترامپ در جریان مذاکرات محرمانه با ایران برای پایان جنگ، به‌دلیل تردید درباره اختیار مذاکره‌کنندگان ایرانی، از نیچروان بارزانی، رییس اقلیم کردستان عراق، برای برقراری یک کانال مستقیم با فرماندهی سپاه پاسداران استفاده کرده است.
بر اساس این گزارش، مقام‌های آمریکایی در میانه ماه مه نگران بودند که محمدباقر قالیباف، رییس مجلس، و عباس عراقچی، وزیر امور خارجه ایران، اختیار لازم برای رسیدن به توافق را نداشته باشند و مواضع آنها از سوی سپاه پاسداران تغییر کند یا وتو شود. به همین دلیل، دولت ترامپ تلاش کرد مستقیما از موضع فرماندهی سپاه درباره مذاکرات مطلع شود.
تولسی گابارد، مدیر وقت اطلاعات ملی آمریکا، در همین چارچوب با نیچروان بارزانی تماس گرفت و از او خواست برای برقراری ارتباط با احمد وحیدی، فرمانده سپاه پاسداران، کمک کند. بارزانی به‌دلیل سابقه زندگی و تحصیل در ایران، تسلط به زبان فارسی و روابط نزدیک با مقام‌های جمهوری اسلامی، از جمله فرماندهان سپاه، به‌عنوان واسطه مورد اعتماد واشینگتن انتخاب شد.
بارزانی پس از تماس با طرف ایرانی، خواستار گفت‌وگوی مستقیم با وحیدی شد. چند روز بعد، یک مقام سپاه با یک تلفن رمزگذاری‌شده به دفتر بارزانی در اربیل رفت و تماس امنی میان دو طرف برقرار شد.
به نوشته آکسیوس، وحیدی در این تماس به بارزانی گفته است که از مذاکره‌کنندگان ایرانی حمایت می‌کند و موضع سپاه نیز حل بحران از مسیر مذاکره است. بارزانی پس از این گفت‌وگو، نتیجه تماس را به گابارد و او نیز آن را به کاخ سفید منتقل کرد.
پس از این تماس، آمریکا پیشنهاد کرد مذاکرات محرمانه میان مقام‌های ارشد دو کشور در اربیل برگزار شود و بارزانی میزبان این نشست باشد. طرف ایرانی این پیشنهاد را رد نکرد، اما درباره امنیت مذاکره‌کنندگان ابراز نگرانی کرد. بر اساس گزارش آکسیوس، مقام‌های ایرانی نگران بودند که نیروهای اطلاعاتی اسراییل در اقلیم کردستان حضور داشته باشند و احتمال حمله به آنها در اربیل یا در مسیر رفت‌وبرگشت وجود داشته باشد. در نهایت این نشست برگزار نشد.
آکسیوس این تلاش محرمانه را نشانه‌ای از دشواری واشینگتن برای تشخیص مرکز واقعی تصمیم‌گیری در جمهوری اسلامی دانسته است. این رسانه می‌گوید جنگ و کشته‌شدن علی خامنه‌ای و شماری از مقام‌های ارشد جمهوری اسلامی، همراه با ادامه درگیری‌ها، نفوذ سپاه بر تصمیم‌های مرتبط با امنیت ملی و سیاست خارجی را افزایش داده است.
به نوشته آکسیوس، بارزانی اخیرا نیز پیام‌هایی برای کاخ سفید فرستاده و آمادگی خود را برای کمک به ازسرگیری مذاکرات ایران و آمریکا اعلام کرده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 342K · <a href="https://t.me/VahidOnline/77896" target="_blank">📅 19:12 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77893">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/QZHJxmx0UVKa0cziB93uGyJW5Xqf6rL8JLvDvAA1uB-TOmFSO4zS-wJuxI8by6qOtqybHhUjk3MuFNsjD0UY6XvHvcVw5YcmERhkx8jEsKkVM7KFTJDr2wkKs7hm0DvLC_APNogGQnHX7zfCsW437HC-YfHk3mOiW5CX08ZTQMm-M79XlR3Qk0Y4bRA7K_RrnPeLxlV8ompvm4wbsWnaB-9_bbyUif7EEVRhYHPwUCeXf9kkQMOH027fjdyYAyv4yKuIBmzZopTFAGspNSSdAtmg9NOPCi5kCHS2grM7kdodR3anMKyLhlZNoWq4exPamP_EN_rGViW3doa3E2CE2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/dGNjEBij-Kw2AA9KCvZr3MeVLbJgG24WPIoqMrLMsIrAlVQNqcRXWiTg04SLNIIOsZwzO0KSlJNypyEL3LkyoA4g6WMze6JPwt8pYAEsQ3GwV9_q1dU_ptrJyf5a3mMQaA150ruVJovYvVHYkEi5xRO5qG0afZURu8o2KAMauKHk5-jwkUHacNrALD9sIS44pwPSX9bwlE5-LuSLMHbRZ8VXSvwcRzgD6Z8iAYACpnMJXepEwpFyZ0lgovenZRVfA7u7e-BR1KlrWS8mHLYk4uEXulJ5RFBKvXVVGRf22_K1XWxalbjXhyuz0nZ-EleHDAXp4DWkAb588gzVREgfXw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/1630a6bff7.mp4?token=BMx_am8vZye4RocTd3FA6Qg8b1zVthwsZVZCDwwxUAwQwbLDuL7X91dP4bR3yTEScbx7HPBhqxEccBw9dNwCK5yQdKcu_j9WQjj3Oa-XenA4xsryyt2TwNP-CSJHnuwOHzdkX0UBeX2yrlZ_bEG5B8c4nK6h43S5oWtGpQXwYKz-DKKqjUS-w1qpsNGU6kN3r4Y75978j3Yo8oqFT3m0olaFZ5KrGBdlX97SdVHlivKPL3NUwOaucojlmfUHhxpMLHDleTbIH3Kue6rhAmnzFN2boeRA8l9mBOvRxnBttyZH2crwsfrx0YRgGV-m2IAeqVKDRCqGoc4-oPokCGeOUA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/1630a6bff7.mp4?token=BMx_am8vZye4RocTd3FA6Qg8b1zVthwsZVZCDwwxUAwQwbLDuL7X91dP4bR3yTEScbx7HPBhqxEccBw9dNwCK5yQdKcu_j9WQjj3Oa-XenA4xsryyt2TwNP-CSJHnuwOHzdkX0UBeX2yrlZ_bEG5B8c4nK6h43S5oWtGpQXwYKz-DKKqjUS-w1qpsNGU6kN3r4Y75978j3Yo8oqFT3m0olaFZ5KrGBdlX97SdVHlivKPL3NUwOaucojlmfUHhxpMLHDleTbIH3Kue6rhAmnzFN2boeRA8l9mBOvRxnBttyZH2crwsfrx0YRgGV-m2IAeqVKDRCqGoc4-oPokCGeOUA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پس از آن که قالیباف اعلام کرد درباره مسائل مرتبط با سرنوشت مردم ایران از روی حزب‌الله لبنان تصمیم گرفته میشه و اطمینان داد که مذاکرات به خاطر حمله اسرائیل به اون‌ها متوقف شده بود و مدعی شد که تهدید کرده بودیم اگر ادامه پیدا کنه "
این‌طوری، این‌طوری، این‌طوری، شما را خواهیم زد
":
شنبه:
‌وزارت بهداشت لبنان می‌گوید که حملات روز گذشته اسرائیل به روستاهای جنوب لبنان ۱۱ کشته به جای گذاشته است.
ارتش اسرائیل گفت که این حملات در پاسخ به حمله حزب‌الله به نیروهای اسرائیلی انجام شده است؛ حمله‌ای که به گفته اسرائیل سه سرباز را به‌شدت زخمی کرد. اسرائیل همچنین می‌گوید که یکی از فرماندهان نیروی رضوان حزب‌الله در حمله به انصار کشته شده است.
این حملات از مرگبارترین حملات از زمان آغاز آتش‌بس میان اسرائیل و حزب‌الله در ماه ژوئن به شمار می‌رود.
با این حال، نواف سلام، نخست‌وزیر لبنان، با تاکید بر غیرنظامی بودن قربانیان، این اقدام را تنش‌آفرینی بسیار خطرناک برای ثبات منطقه خواند و خواستار توقف فوری آن شد.
@
VahidHeadline
و دوباره امروز یکشنبه:
ارتش اسرائیل بامداد یکشنبه نبطیه در جنوب لبنان را هدف قرار داد.
این حمله تنها چند ساعت پس از مرگبارترین روز حملات اسرائیل در لبنان از زمان آتش‌بس با میانجی‌گری آمریکا بود که دست‌کم ۱۱ کشته بر جای گذاشت.
بر پایه گزارش الجزیره، آن حملات صدها خانواده را به فرار واداشت و جاده‌های منتهی به شمال را مسدود کرد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 310K · <a href="https://t.me/VahidOnline/77893" target="_blank">📅 19:04 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77886">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/FH82cYYh-Jxm98gsN6yxIIUF20KiBLsq9akPBjW5eOOAlSrNdAo2rOv44ZzNK0wrv2pv3_0nyhh0ts-JCuJlIcrLxiDZ0EJnPxPCoRVYer0dJE5UUDGhoW8yE86vJDtcgRjs9sDktuGVdn56AUKQG0AaPHVCmBPuBQa90FHUGvf1AOvj3zRYzqlYt1f_VMH7Mgeg0kNCEKyNdMZGXtY704nWLIT_L0TxQAizAvyZLL42ePD6A8tstmOHNyZZNheM1-qTEyHtCBOA5zkyj_lc38xubMIlCvWFDcHCRuhgMvlMY-SbT0vVTu7m-SRuZVmuyfgbn8oa7s7zjC-pF6kbeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/bXIm-bp16xgaNpEu6PxxA434MGdx7al4UK2NDeVkpNuLpgxeuWMglWql55znXUonBc4pLdS1OIChulPev8XwHhHqv_UvpUdy8UdlzFIsz2C4rwReJ6Ivvj238D5M1XBOx0iH5GibmaT0tIGu-6h4JyZNX7Pi156yZyMAZkC8qwF_6uf1oeoq_LR1f1g4ao5hbiqyAn9UgdYpAGo6KaaNlbT4sdxfvgd699uvUtAxSWNNT6Bz_EHWD6K1oNi7M8bHUW33kVY-pr3M18W6rq0ok3SkMB_e7BtDKiyxZr0BHgg4tJXg87GqK1bBr0KDQSGwGJylJiV_hR1BRB84qs4Qkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/kZP-Tgo8lFikgUvtqr9GrvxsOnO_LG1fQq3FTbkmMbWqsqayvslWSraAqyQBl-IBz6LNi97zSxmzV2bI4sFO3zhJAEqbbd6YSWa4La5eh284Fh0VNezpYyPE-XoSm7JbCSSDT_axMkIC-evzkTN5Z8QnWXQ6qZMb2AWifiiPSJfcGFOHfiU-Yvnv8FU5D3Y5M4ZcHBsZx8-fcWMHrRJYDhZacVclDJjrDjaRYm3F69ceAna2gSFL8WY-R6O4jMKGz_67SFaKIRIhRA4ir44OM16CtWTbmkYzo19K5l8loer9QJq-iivljTHL500e2zAHtNOs0QlXGxG-wHDjh_ctTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/h0TRytLEHy0HRVeoWnLjY3C_CFXntW28cIvPdgG1AYAnxoylGWRxmKny3PK6kqUvJHTGC807z6Chq6Pnz8pxNEA_Wc3oEfMHCDyZmXbQsSuQWn7miw1UsV1v6ZS-FB181nqDDpMKOsikCirISYADnaZb_DYhx12W4wZzhCxA0jg7xbruXAibiPLtHi4S863_YZot927magRAhyvzgpBveaL26VNA6VmRtnFxDrJHLq8Thf1bx2TUPqjAuMa-hpUwe9eUJk4-lMtzrc2Tx1ROMiAueENes2vYiyWFwlziNYs6Ky8oLWBpNihipyr3kRVYeeKr3YriVN-uLf_uHV-puA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/InwzuOj_-6XlqxNQDW-jWmARafv_6qvkkB-gEr8r45jX6vYRZiyUbHdHC6v9rTQNET-BOrvLnkKwF609Ha2Bp0VofcnoWniS04M4p4oaEgxUhcGuIxGV8eUbhCAE2bpZUrV-QpvClPEVwLsS9fbn8mLm-yqy1trltUylEfQzLDSQeAIr-DlVgP7Pbz__WGVtptOTBATbayG8dZ3Qvti8XzixHl0satkoy3zrWnBAlzHe1_bIlxs8Qk0QSKRBKPBATihaFxDIo3xTphsvUdf8-JBXTQcbkWcuM8RURCUwcFRr_xTcGByMKb88UTyHimEeaQVi-QRIt7KP9-a-hRs46A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/LDDYs6c6lQFPNuMJKopit9fennjrBlILGB9ay8Y5O0l-JulfbYN7pnuu-eE2rZJT-CVM3pX9Hm5UJnKfRwHzE77DymIXovOQEf4U7UicJTh_MKB_2NM2Mzf6IGivrioENLBZNmUCfGRegTo2jxAStWNTn9XONBe4A3AfPlSol755lGilCKMC181F1gV8J2Il8IvmMneZh9EmSoQGYzl-q75i5iqs2mSbkCRzU7PVhPCngeSTp9oP_ErpqEcFU0vMfOFAXWGv17_ZFJ8QgTMuOiif3yssHfzlP1Dq53wf790pj9ZP0Vyrn-rofRq6WPh5shHJumpDbxvqhJtadu7HCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/EUbsi5Hfj0w4KxYNj2qdN6NsIeU2eEPZXVrAu4gsXFxZzA2G7bVmO5_e_KWvlewigsdnVlD8H5m_5JQqRchtVa2xNTW7N7OMJq4P1kfRC86DeAc0sivHwrbAzYZ0s4M1ffj9YrtUOx9CygxEI2UKXxjFfBem-Dktl-6zZ9oqONCBpJr1PdLDn5BccNEn8dWQjw3rHJMoZVZPjUUCmWFpy8fsk6_j8vbxKYdiLWDnRcRF_fCApYpDltSmaQaedp0V_OFFg7oOucojV-Qo18gN9CmeFqj8673_0RR7b1ssPBcMAm8ygws2YxMndHUGZSzFBFhumSAvGuhEVE56nDe3Cg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">اعلام کردند که کلیات این طرح تصویب شده و جزئیات منتشرشده [
به نقل از "پایگاه اطلاع‌رسانی وزارت کشور"
] هنوز بررسی و تایید نشده‌اند:
مجلس شورای اسلامی طرحی را تصویب کرده است که در صورت تبدیل‌شدن به قانون، مصاحبه و ارتباط با رسانه‌های خارجی، ارسال فیلم و عکس، همکاری علمی با برخی دانشگاه‌های خارج از کشور و شماری از فعالیت‌های فرهنگی و آموزشی را جرم‌انگاری می‌کند.
طرح «مقابله با نفوذ سرویس‌های اطلاعاتی و دولت‌ها یا نهادهای بیگانه در کشور» روز یکشنبه ۲۵ مرداد با ۱۸۳ رای موافق در مجلس تصویب شد.
براساس متن منتشر شده از مصوبه، مصاحبه، شرکت در گفت‌وگو یا هرگونه ارتباط با رسانه‌هایی که حکومت آن‌ها را «معاند» می‌نامد، مجازات حبس درجه شش، معادل بیش از شش ماه تا دو سال زندان، خواهد داشت.
رسانه‌های آمریکایی، اسرائیلی یا رسانه‌هایی که از سوی این دو کشور تامین مالی می‌شوند، در این طرح از مصادیق رسانه «معاند» معرفی شده‌اند. دبیرخانه شورای عالی امنیت ملی نیز موظف خواهد بود فهرست این رسانه‌ها را هر سال منتشر کند.
گفت‌وگو با دیگر رسانه‌های خارجی نیز به اطلاع‌رسانی در سامانه‌ای وابسته به وزارت اطلاعات مشروط شده است. مصاحبه بدون ثبت قبلی در این سامانه، می‌تواند به شش ماه تا دو سال زندان منجر شود.
ارسال فیلم، عکس، صدا و هرگونه داده برای رسانه‌های غیرایرانی یا افرادی که در خارج از کشور فعالیت رسانه‌ای دارند نیز با همین مجازات روبه‌رو خواهد شد.
اگر ارسال اطلاعات در قالب همکاری، با آنچه «قصد مقابله با امنیت کشور» خوانده شده یا هنگام «بحران، اغتشاش یا آشوب» انجام شود، مجازات به حبس درجه پنج، معادل دو تا پنج سال زندان، افزایش خواهد یافت.
در متن طرح تعریف مشخصی از «ارتباط»، «رسانه معاند»، «شرایط بحرانی» و «فعالیت رسانه‌ای خارج از کشور» ارائه نشده است. گستردگی این عبارات می‌تواند ارتباط شهروندان با خبرنگاران و ارسال تصاویر رویدادهای روزمره را نیز مشمول پیگرد قرار دهد.
وزارت اطلاعات و سازمان اطلاعات سپاه ضابطان جرایم این مصوبه تعیین شده‌اند و رسیدگی به پرونده‌های آن در دادگاه انقلاب انجام خواهد شد.
محدودیت همکاری‌های علمی و آموزشی
مصوبه مجلس، همکاری با دانشگاه‌ها، موسسه‌ها و سازمان‌های خارجی را نیز محدود می‌کند. وزارت اطلاعات موظف خواهد بود هر سال فهرست مراکز خارجی مجاز برای دریافت بورسیه، کمک‌هزینه تحصیلی، انعقاد قرارداد و شرکت در همایش‌های علمی را منتشر کند.
همکاری با مراکزی که نام آن‌ها در این فهرست نباشد و همچنین ارسال نمونه‌های پزشکی، تحقیقاتی و باستان‌شناسی برای آن‌ها، مجازات شش ماه تا دو سال زندان خواهد داشت.
برگزارکنندگان دوره‌ها، کلاس‌ها و کارگاه‌های حضوری یا مجازی که به تشخیص حکومت با «فرهنگ ایرانی ناسازگار» باشند یا تحت هدایت نهادهای خارجی برگزار شوند، ممکن است به حبس درجه پنج، معادل دو تا پنج سال زندان، محکوم شوند.
در برخی گزارش‌ها مجازات برگزارکنندگان این دوره‌ها پنج تا ۱۰ سال اعلام شده است، اما متن منتشرشده از مصوبه، حبس درجه پنج را تعیین کرده که براساس قانون مجازات اسلامی بین دو تا پنج سال است.
افرادی که با اطلاع از هدف برگزارکنندگان در این دوره‌ها شرکت کنند نیز ممکن است به جزای نقدی یا شش ماه تا دو سال زندان محکوم شوند.
محدودیت‌های تازه برای هنرمندان
فعالیت‌هایی مانند تولید یا کارگردانی فیلم، سریال، مستند و تئاتر و همچنین تولید موسیقی و کتاب، در صورت ارتباط با نهادهای خارجی و با تشخیص نهادهای امنیتی، می‌تواند مشمول مجازات شود.
در متن مصوبه از آثاری نام برده شده است که «احکام دینی را زیر سوال ببرند»، «چهره سیاهی از ایران نشان دهند»، «مروج فرهنگ ضد اسلامی» باشند یا با هدف مقابله با جمهوری اسلامی تولید شوند.
تهیه‌کنندگان، نویسندگان و کارگردانان این آثار ممکن است با جریمه نقدی، محرومیت دائمی از خدمات حکومتی یا ممنوعیت همیشگی از تولید آثار فرهنگی و هنری روبه‌رو شوند.
عباراتی مانند «چهره سیاه از ایران» و «ناسازگاری با فرهنگ ایرانی» نیز در این طرح تعریف نشده‌اند و تشخیص آن‌ها برعهده نهادهای امنیتی و قضایی گذاشته شده است.
@
VahidHeadline
کانال  مجتبی خامنه‌ای، بدون اشاره مستقیم به ماجرا این پست رو گذاشت:
🗒
لازم است مصوّبات مجلس با مسائل اصلی کشور و نیازهای مردم نسبتی مستقیم و مشهود داشته باشد و معطوف به امیدآفرینی و آینده‌سازی کشور باشد. جامعه پیش از هر چیز نیازمند مشاهده‌ی نشانه‌های واقعی امید، مسیر باثبات و چشم‌انداز روشن از آینده است تا بتواند بر اساس آن برنامه‌ریزی و حرکت کند و نمایندگان مجلس با مواضع، مصوّبات و نطق‌های خود میتوانند مجلس شورای اسلامی را نهاد پیشران امیدآفرینی نمایند.
✍️
بخشی از پیام به‌مناسبت سالروز افتتاح اولین دوره مجلس شورای اسلامی و آغاز سومین سال فعالیت مجلس دوازدهم | ۷/خرداد/۱۴۰۵"
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 296K · <a href="https://t.me/VahidOnline/77886" target="_blank">📅 18:43 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77881">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/UMoTwjzrLTK_KdNLcMvMLx5wR7rvzFQyzW0Yq1dyHcYRirl0xABWDouBQ4kKEd0zEkGVjJ9K8vAOf5RKv5HW9VYKxRee-0q8l5_MceqKOb4bkM4Ldc8P4tt4Sn0mJF640bMBNF-Y64dIDCA2l1fTD0VVIpxF9hJVOzb1XAyDD_j1f5YD74dzXOgijZUYIATNHmvn-tqN0GEnZx2bH2oAXk1O4Va36mMNjS0PbI73PQSArVLRkwVuptRTpuhmd59dyytej7EFcejXo0h5uKjfR4RqlAZmnUlYlCvrEoQs-YJk3_B4e4sXX0psjwvk82ZPglyEffXMcN9XRAcQMFdWRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/fd7jyoVkQvzF1hTxmbgXHqjMq0UOfJSNsHXmB80umy6ZfMYB5kPF2l6x8skTR1Z-LIcwFMXuOl57ztFy0cGe0fA7kT253XR-J0DREk6TWxeAZH21F342w4XsFTHOyLezfcjzcULf_sFndYvPo2Sowb9VUE2sN182zD8oib4mGrDHaDwDyxpmItZKzdVtcRDv1jjxH56BDqgiWwCM6JPXjlr15kfGvn0L32nKSWmpQa0gWGzDaSHts_o1Ojcnb_6xrWakiCQJvfSxXajcLPyFWKlnU8apV3KhoFIDaurfZnpul9BRSwI5UtXdIrGt4Q8n4CtVNRu6kwZ_Cepv0HdpKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/hD9Sf-TxRHzaKKYpc3x_qrKQCwaEfHS75Xf5j44SZUJ5PGL_cDTgAbCWgxgQYM6_-Lljm1FJ7q27bHf98xguCGgp1ueXI8qCs6_abjRBUfDsFfzYgZb6eNOl0NcPk82dEO9Ix0mCQyEJrHEK1XGIc15uy4883X_b8aR_n5DkBcnLUCBCVQDGeHc-RoAE2mbZqZD_GDb2cCex9XZUETvrcZVcPNC3i7ZWyi8-fJl-dalEi5r3al3X5ZtW1jrQnX72jQE2RVVApN6t_vdxKQFv65L5PNs-qokVFdvh2tv0fzicT8w2nU4SYH1uzkWhqT5mxQTcuBCOI6N8yGTC6nh9Mg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/QcYCT3-fI1mF2BGkY7y3SzxAuut_HfQ8jjO7ORDEVSql3Py75mvX0MF6jkxElUCHeAOMNt3jY7UQBcdsjLDPYKlIFAqlddsVJZSPggyeeA4NhozICS5p5woGS7ri0yWWNatKhbhAP1zLRpdD0GyCFu-9A0Ezw1xTye-YjAqaUXqm0Bximjai0pB65R9HYX7SxfAniFAsMI8fqP0jgl_2QI_z-pLSMhYmIClyQP6GWbYWmj4i2VomgJs781GTf6wtuKMqD7FlCD4RnOpBe4FuvSL7Xv9kPURnN56RJagswL63MVvl1wJvM_Xqi0nVyeL8psrTutN_Gu5s7fekI_E-Tw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/f0bf656d54.mp4?token=V62NAkX--wQPmVc0ZQuzw3wsrc-LSlKI0JBznPk0j8SDal3JZSAji_YlZDEr5blK0zEl7hk0l_pYb6nkSK1YLQOv_B1bap6zEntyT1jcv82f3KVASiS5JZP85DApNW4LMHOVj4vFMqQlRH5ZttIkGlWkJvez2iiwTtI3Kip5Zb0e2eCZ-_Zz8-X4-4okweKmBvCQY9oaqu4N0xBede46nkcB6q0N_3LvWvFWCtwNjQaPiPG5uo9xl7OB7031INpxbv4bREMyE-rIzY9BSen_UpiwAkX-H6Ailr0_b9jWNFPTTlQ3Go26vRiz_1y4RyoyvFdASPYGwc32w3vBhPFY1A" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/f0bf656d54.mp4?token=V62NAkX--wQPmVc0ZQuzw3wsrc-LSlKI0JBznPk0j8SDal3JZSAji_YlZDEr5blK0zEl7hk0l_pYb6nkSK1YLQOv_B1bap6zEntyT1jcv82f3KVASiS5JZP85DApNW4LMHOVj4vFMqQlRH5ZttIkGlWkJvez2iiwTtI3Kip5Zb0e2eCZ-_Zz8-X4-4okweKmBvCQY9oaqu4N0xBede46nkcB6q0N_3LvWvFWCtwNjQaPiPG5uo9xl7OB7031INpxbv4bREMyE-rIzY9BSen_UpiwAkX-H6Ailr0_b9jWNFPTTlQ3Go26vRiz_1y4RyoyvFdASPYGwc32w3vBhPFY1A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">احمد آریایی‌نژاد، نماینده ملایر در مجلس ایران، در یک مناظره تلویزیونی، کشته‌شدن مهسا (ژینا) امینی را با عبارتی توهین‌آمیز توصیف کرد و اعتراضات پس از مرگ او را «هشت ماه اغتشاش» خواند.
این اظهارات در رسانه شهرداری تهران (همشهری) مطرح شده است.
پدر و مادر مهسا امینی در استوری‌های مشترکی در شبکه‌های اجتماعی،سخنان این نماینده مجلس را «توهین‌آمیز» خواندند و گفتند چنین اظهاراتی از ارزش و جایگاه دخترشان نمی‌کاهد.
@
VahidHeadline
امجد امینی نوشته: «مطلع شدم احمد آریایی‌نژاد، نماینده ملایر در مجلس، با لفظی چنان‌که سزاوار و شایسته خود و اسلاف ایشان است و با کلماتی که در هیچ آیین، مرام و معرفتی جای ندارد، به دختر ما، خانواده ما و تمام مردم کردستان و ایران توهین کرده است.»
پدر ژینا امینی همچنین با اشاره به وضعیت اقتصادی و اجتماعی ایران، خطاب به این نماینده مجلس نوشته است: «عجیب است در شرایطی که مردم این مملکت به‌خاطر تصمیمات امثال آقای نماینده در اوج فقر و فلاکت هستند و هزاران دختر و پسر هم‌سن‌وسال ژینا در افسوس آینده‌ای که ایشان به آتش کشیده‌اند می‌سوزند، باز هم سراغ دختر ما رفته‌اند.»
او در بخش دیگری از نوشته خود آورده است: «می‌گویید فرشته نازنین ما به درک واصل شد؛ بریده باد زبان شما که یک مملکت را به درک واصل کردید و نه‌تنها از عقل و خرد، بلکه از سر سوزنی شرم نصیبی نبرده‌اید.»
پدر مهسا امینی در پایان نوشته است: «نام دخترمان در کنار هزاران انسان بی‌گناه دیگر تا ابد در تاریخ این کشور جاودان است.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 322K · <a href="https://t.me/VahidOnline/77881" target="_blank">📅 18:31 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77880">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/OTjEMpsvG5T0R9KTBIU9H_jl53xUePwI_K_kyAayzgbnm79ulS_pv-C56vUAJ4vXPtYTZEkxCSGiNxI0ZPQG7z1ARULkQLVyJQ-oE_2_u7_Hv_gN1Jg7aFrckdytYyd4k4pTiS4ax1eDFxXrl-0zl8Ggx6iTYzIVY_JXcoeSQJNdwz87dhY0i588R_6htJJ9edEqBludjey6cUOLjFGwtO76JXan-XZetgMmwO9swLH6E0lEhxzYmYsE_BBznvMFG5e6hqE1EIQEq_dq-Y0xdN-DGiPeIl43UVj3gF1UEthO2jibGsEBCewxj_lFaCluSmtcAXRJ0H66vL6n89ZzmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری میزان، وابسته به قوه قضاییه جمهوری اسلامی، گزارش داد حکم اعدام شهرام صادقی، از معترضان خیزش دی‌ماه، بامداد یک‌شنبه ۲۵ مرداد به اجرا درآمد.
به گزارش این رسانه حکومتی، دادگاه انقلاب کرج صادقی را به اتهام «اقدام عملیاتی به نفع اسرائیل، آمریکا و گروه‌های متخاصم» به اعدام محکوم کرده بود.
خبرگزاری قوه قضاییه این زندانی سیاسی را متهم کرد که شامگاه ۱۸ دی ۱۴۰۴ در جریان «کودتای آمریکایی-صهیونی»، با یک دستگاه خودروی پراید شماری از ماموران یگان ویژه استان البرز مستقر در چهارراه گلزار کرج را «عمدا» زیر گرفت.
میزان نوشت در این رویداد، هفت مامور یگان ویژه مصدوم شدند.
مقام‌ها و رسانه‌های جمهوری اسلامی در تلاش برای بی‌اعتبار کردن صدای انتقاد شهروندان، بارها اعتراضات ضدحکومتی را «اغتشاشات»، «آشوب» و «کودتا» نامیده و آن‌ها را به بازیگران خارجی، از جمله آمریکا و اسرائیل، نسبت داده‌اند.
شدند.
میزان در ادامه گزارش داد صادقی پس از «حمله» به ماموران یگان ویژه در کرج، با «همکاری اغتشاشگران» خودروی خود را به آتش کشید و از محل گریخت.
در این گزارش آمده است: «او با جعل هویت و در حالی که اعتیاد نداشته، در یک کمپ ترک اعتیاد مخفی شده بود که بلافاصله شناسایی و بازداشت شد.»
خبرگزاری قوه قضاییه نوشت صادقی در جریان بازجویی‌ها دست داشتن در این رویداد را رد کرده و گفته بود شامگاه ۱۸ دی از اسلامشهر راهی خانه خود در کردان ساوجبلاغ بوده، اما برای صرف غذا وارد کرج شده و در آنجا خودرویش به سرقت رفته است.
به گزارش میزان، این زندانی سیاسی سرانجام پس از مواجهه با «مستندات و دلایل متقن ارائه‌شده»، اتهام خود را پذیرفت و «اذعان کرد» خودرو را به سوی ماموران رانده و سپس آن را آتش زده است.
خبرگزاری قوه قضاییه افزود حکم اعدام صادقی پس از رسیدگی به فرجام‌خواهی و تایید در دیوان عالی کشور بامداد ۲۵ مرداد اجرا شد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 369K · <a href="https://t.me/VahidOnline/77880" target="_blank">📅 08:57 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77879">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ZMLIBN-tj_gDmiug6tUqkABDYHyAwjss-yZtxVik9F0BN8EDqqVD5wpGfgJfwRsC88wHgB41y1zsX8inos4IZxW5h7k3MeV21FVn3Zn5d9IOhuvLTdzoOtNcoGERsM02bfpZOnJUDeQ7qB7csfZtubfralFabcyRG09WRQ_iuztlckyZlxYwDijjXhjI3mf21qU1nekvoEm92vr7aypvJWCzVJ0iwxl3ado83IYCrC5gLsKwtVAxa8kdccR0YcWRTgjPAUYnl2GBVQvfWRllX4X0YlxXI6pWwnpHrfin86OuQpzzDnxvVy2U1pzig8qUXX3yUumI--yJIsCvX1eerA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ماجد محمد الانصاری، سخنگوی وزارت خارجه قطر، ادعای جمهوری اسلامی درباره بازداشت سه خلبان ایرانی را رد کرد و گفت نیروهای قطری پس از جست‌وجوی محل سقوط جنگنده‌ها، پیکر یکی از خلبانان را پیدا کرده‌اند.
الانصاری روز شنبه ۲۴ مرداد در شبکه ایکس نوشت ادعاهای مطرح‌شده درباره بازداشت خلبانان ایرانی «به‌طور قاطع» نادرست است و از انتشار این اظهارات، به‌ویژه در شرایطی که تلاش‌های دیپلماتیک برای کاهش تنش در منطقه ادامه دارد، ابراز تعجب کرد.
سخنگوی وزارت خارجه قطر گفت پس از ورود خلبانان مورد اشاره به حریم هوایی قطر، با آنها تماس گرفته شد و مسیر هدف‌گیری نیز بررسی و تایید شد. او افزود پس از رعایت قواعد درگیری و برقراری تماس با خلبانان بدون دریافت پاسخ، قطر اقدامات لازم را برای دفاع از خاک خود و مطابق با الزامات قوانین بین‌المللی انجام داد.
الانصاری همچنین گفت تیم‌های جست‌وجو و نجات قطر به‌طور کامل عملیات یافتن پیکر خلبانان را انجام دادند. به گفته او، دولت قطر پس از پیدا شدن پیکر یکی از خلبانان، برای هماهنگی تحویل آن مطابق مقررات حقوق بین‌الملل بشردوستانه با طرف ایرانی تماس گرفت.
او افزود قطر در ماه آوریل از یک تیم برای بازدید و دریافت اطلاعات درباره جزییات عملیات جست‌وجو و نجات دعوت کرده است، اما طرف ایرانی تاکنون به این دعوت پاسخی نداده است.
پیش‌تر فرمانده کمیته جست‌وجوی مفقودین ستاد کل نیروهای مسلح جمهوری اسلامی مدعی شده بود سه خلبان ارتش که جنگنده‌های سوخو-۲۴ آنها در جریان حملات اسفندماه سقوط کرده بود، به اسارت نیروهای قطری درآمده‌اند.
مقام‌های قطری با رد این ادعا، روایت متفاوتی از سرنوشت خلبانان و عملیات جست‌وجو و نجات پس از سقوط جنگنده‌ها ارائه کرده‌اند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 373K · <a href="https://t.me/VahidOnline/77879" target="_blank">📅 23:28 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77878">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/eJckIsBHRpWkHg8uPUmPHPU-lP1RXP6Yq-N6eoQ_rWb9B4nctXFL2VISmZzMqyQp54YYOHu0yMHL2SR7T978hsujStxmfBY82xin1XVQ3J99ko466vCz8GgyeYrz1MwEnuUcUdR-z_mwWdzJHZ97xhDJCDPwUBrirdnW2THmQUqg4HSfVmu2vboy6aO-dnvrCNn8qPFDb-EHT3YW5Vttkq5zYNzXF_RgQ5-P11e65iCO_OsKP21WQBRplFrPe-oaDGJLYU3SQvupW7y06rYF44YkQgK_zvNFu9Dv5aiP2AEZIn84L7lc-yXqA4wFdgbv4etW5b94IrNyl2CMSMrupg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محمد باقرزاده، فرمانده کمیته جست‌وجوی مفقودین ستاد کل نیروهای مسلح جمهوری اسلامی، در نامه‌ای اعلام کرد سه خلبان ارتش جمهوری اسلامی که جنگنده‌های سوخو-۲۴ آنها در جریان حملات اسفندماه سقوط کرده بود، زنده به اسارت نیروهای قطری درآمده‌اند.
خبرگزاری فارس، وابسته به سپاه پاسداران، این نامه را که خطاب به رییس کمیته بین‌المللی صلیب سرخ نوشته شده، منتشر کرده است.
بر اساس این نامه، جواد صالحی، عبدالمجید دشتیان و عمران به‌روشیان حدود شش ماه است در بازداشت نیروهای قطری به سر می‌برند. باقرزاده گفت دولت قطر تاکنون اجازه دیدار، مصاحبه یا تماس این سه خلبان با خانواده‌هایشان و مسئولان پیگیری‌کننده را نداده است.
پیش‌تر مقام‌های جمهوری اسلامی گفته بودند به جز مجید کاظمی که پیکرش پس از حمله به قطر به ایران بازگردانده شد، وضعیت سه خلبان دیگر این عملیات به‌طور دقیق مشخص نیست و اطلاعات موجود درباره سرنوشت آنها ناقص است.
@
VahidOnLive
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 372K · <a href="https://t.me/VahidOnline/77878" target="_blank">📅 18:44 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77877">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/5168e558df.mp4?token=lrSpk5TVqaT3nXa3LK1O5z-DotBzfRk2Of9LcNDM0cNLrmx6h99Jv70Jtm8XLDWy-OdRUiCes3uLed9oldevLt5yoJWwGUgkcdCAjXuxFgBLKQWRL4vXwPir2bdOU23ncjcgTZiV3k9ghJNkXGeIztVvEugOsBj_mzTwC28M3DCNWD8lFZOhffBupmcpWEioSxeCn5u84E0ZR8C9TYQi18o2uTAQemffoyQUpXm22WnWKx2QNGL-H155JBtrH2UXETxoOGfcfnZWHY69rcnUCFpnl9UyvR5Dz5O8wlv7H0uo4VhmUuw_3S11MEulY65H92rS1wNnSFVcuzBQy6hBWw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/5168e558df.mp4?token=lrSpk5TVqaT3nXa3LK1O5z-DotBzfRk2Of9LcNDM0cNLrmx6h99Jv70Jtm8XLDWy-OdRUiCes3uLed9oldevLt5yoJWwGUgkcdCAjXuxFgBLKQWRL4vXwPir2bdOU23ncjcgTZiV3k9ghJNkXGeIztVvEugOsBj_mzTwC28M3DCNWD8lFZOhffBupmcpWEioSxeCn5u84E0ZR8C9TYQi18o2uTAQemffoyQUpXm22WnWKx2QNGL-H155JBtrH2UXETxoOGfcfnZWHY69rcnUCFpnl9UyvR5Dz5O8wlv7H0uo4VhmUuw_3S11MEulY65H92rS1wNnSFVcuzBQy6hBWw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رئیس دولت در ایران روز شنبه ۲۴ مرداد گرانی‌های اخیر و تأثیر آن بر معیشت شهروندان را «طبیعی» خواند و محاصره اقتصادی و تحریم‌های نفتی آمریکا را از دلایل آن اعلام کرد.
مسعود پزشکیان در نشست با دبیران کل احزاب و فعالان سیاسی گفت: «قبلا محصولات وارداتی با کشتی وارد می‌شد؛ اکنون کلی مسیر عبور می‌کند تا وارد کشور ‌شود و قیمت تمام‌شده کالا بالا می‌رود.»
او در ادامه افزود: «درآمد ما هم کم شده، قبلا نفت می‌فروختم، الان نمی‌توانیم بفروشیم.»
مسدود ماندن تنگه هرمز علاوه بر افزایش قیمت انرژی در جهان، موجب فشار بر اقتصاد ایران و تشدید تورم شده است.
گزارش‌ها حاکی است که با اجرای محاصرهٔ دریایی صادرات نفت ایران از طریق جزیره خارک به‌شدت کاهش یافته است. حدود ۹۰ درصد صادرات نفت ایران از طریق این جزیره صورت می‌گیرد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 344K · <a href="https://t.me/VahidOnline/77877" target="_blank">📅 18:39 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77876">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/4a1eed77d1.mp4?token=fTiokQQlg2A-l1y0NeVVvgdj43ngX2ydUE_UgKiAKG3iA0sj0JBUeU6nknjPYlzdZrQaJDrlqMqqdGoOp_CUYL3nV8OQSLXYO5Rj8QwGm6wQuDMy_H42KGkRER0KDTWb0yexwFmsytvWueapLEDasY1z17PanDsJ8cgD3X8r89ZlHZA7TdRFcX1xD_yi9btJlR_L5k_e4L89duq80b0Fn9jdlZN8zJrJX1MDJa-nJH-BfCbho-anJ2uatDm-cbcD8n2j-GazTk_h1icxRRRdsij2A4q6TLLFiHGsamXY72IuRIPsHkF9qrtwPY49tCNqNFHJPRVhj0ZyaSz5WBsLGA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/4a1eed77d1.mp4?token=fTiokQQlg2A-l1y0NeVVvgdj43ngX2ydUE_UgKiAKG3iA0sj0JBUeU6nknjPYlzdZrQaJDrlqMqqdGoOp_CUYL3nV8OQSLXYO5Rj8QwGm6wQuDMy_H42KGkRER0KDTWb0yexwFmsytvWueapLEDasY1z17PanDsJ8cgD3X8r89ZlHZA7TdRFcX1xD_yi9btJlR_L5k_e4L89duq80b0Fn9jdlZN8zJrJX1MDJa-nJH-BfCbho-anJ2uatDm-cbcD8n2j-GazTk_h1icxRRRdsij2A4q6TLLFiHGsamXY72IuRIPsHkF9qrtwPY49tCNqNFHJPRVhj0ZyaSz5WBsLGA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محمدباقر قالیباف، رئیس مجلس و مذاکره کننده ارشد با آمریکا، می‌گوید پس از کشته شدن یک فرمانده ارشد حزب‌الله در حمله اسرائیل به جنوب بیروت، گفت‌وگو با آمریکا متوقف شد.
به گزارش رسانه‌های ایران، آقای قالیباف گفت: «در آخرین حمله‌ای که به ضاحیه انجام دادند و مسئول اطلاعات حزب‌الله به همراه خانواده‌اش شهید شد، همان‌جا همه چیز را متوقف کردیم. گفتیم که امشب این‌طور و آن‌طور شما را خواهیم زد و اگر رژیم صهیونیستی هم پاسخ بدهد، همه منطقه را می‌زنیم.»
به گفته مذاکره کننده ارشد ایران، «همان شب محاصره را برداشتند، نه ۳۰ روز بعد از تفاهمنامه، همان شب. توییتی ترامپ زد و گفت ما امشب برمی‌داریم. زیرش هم نوشت البته ایرانی‌ها هم تنگه هرمز را باز خواهند کرد. وقتی این را دیدم، جلویش را گرفتم و گفتم ما چنین توافقی نداریم.»
«به میانجی‌ها گفتم که این توییت اگر الان برداشته نشود، می‌زنیم به همان شدتی که من گفتم می‌زنیم. ۵۸ دقیقه بعد ترامپ بخش دوم را برداشت و نوشت تنگه در چارچوب تفاهمنامه از روز شنبه باز می‌شود.»
«این مذاکره یعنی مبارزه.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 314K · <a href="https://t.me/VahidOnline/77876" target="_blank">📅 18:37 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77875">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromبنیاد عبدالرحمن برومند برای حقوق بشر در ایران</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MKPWbN-Lyy_aMj-LWsXQRnGCSTyA0-xGrNmXLWPgZmtlS6MKpDdjT1DwNkO1dHHXhVw5OWccJIvK0OLFWIFC9TrUrUxg-WicfXbE25LNQZOaA25cqaKcCuO3YdtkKoXRLoB-FC2MIQwH4rVQCSLMQxyTzhOBYr3yxtjEj-Hnohheox5S5RsI_nFyk2m3Y2L5d-hdrqMKCG60RUf-FrD5-GUn67Gteg4C0cxE17j_m7e8ELZOD-_e9m0M58o16zhBxKbevoXHS5rRSYh5Jva6UkHnKxqxz4tDs7NFgtHQuboExNq5wAirpqx1nEAMJ0opr3P7ppW-58TnKVMmyVmE1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
سپهر امیرزاده، از بازداشت‌شدگان اعتراضات سراسری دی‌ماه ۱۴۰۴ در اصفهان، از سوی دادگاه انقلاب به اتهام «محاربه» به اعدام محکوم شده است. پرونده او هم‌اکنون برای بررسی در دیوان عالی کشور قرار دارد.
🔸
بنا به گزارش خبرگزاری هرانا، آقای سپهر امیرزاده در ۲۳ دی ۱۴۰۴ در منزل خود در اصفهان توسط نیروهای امنیتی بازداشت شد و پس از طی مراحل بازجویی به زندان دستگرد اصفهان منتقل شد؛ جایی که همچنان در آن محبوس است.
🔸
جزئیات بیشتری درباره مصداق اتهام «محاربه»، مستندات پرونده، روند بازجویی و نحوه برگزاری جلسات دادگاه منتشر نشده است. آقای سپهر امیرزاده، متولد ۱۳۸۲ و اهل رامهرمز خوزستان، مدرس و نوازنده موسیقی و ساکن اصفهان است.
#نه_به_اعدام
@IranRights</div>
<div class="tg-footer">👁️ 321K · <a href="https://t.me/VahidOnline/77875" target="_blank">📅 18:30 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77874">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/FLvsMnqSI_3FuoN7Muyl8gHklh2cml7bg2HeySoIEdS7D1uHuSsxTzrp52N774VaN9N-8-Zc35timqH1pazm9UjDAQcS3g3-3O0hFRnH-25dvaSfqZ550f67X_V7TfUfXIln-7A6qdoz7f3P11eh1qDkwEvf9jxZMX68iChTx088rxp-QtlEcTIrfV2ZrYdXN0DK4FkECfWOB6t-DdILMuQxKllhhEsM7JO89G5cAaTiPHzheLIqXPCTSBoDYXeJreiPitlJjZhsH7K_Yw4biCjipobP2JCSFgaDqh3wQ7aS50h3npzeCz9wDENMNIatk9Zakt3VZp-iapxHuelXag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ روز جمعه در نیویورک با اشاره به حملات آمریکا و اسرائیل به ایران گفت: «آن‌ها دیگر رهبری ندارند. رده اول آن‌ها از بین رفته، رده دوم از بین رفته و نیمی از رده سوم هم از بین رفته است.»
او افزود که این وضعیت، مذاکره با جمهوری اسلامی را نیز دشوار کرده است: «یکی از مشکلات من این است که کسی برای مذاکره وجود ندارد.»
ترامپ سپس با لحنی تمسخرآمیز گفت ایران «تنها کشور جهان است که هیچ‌کس نمی‌خواهد رییس‌جمهوری آن باشد.»
رییس‌جمهوری آمریکا همچنین مدعی شد سامانه‌های راداری و تجهیزات پیشرفته اطلاعاتی جمهوری اسلامی از بین رفته و توان تولید موشک ایران ۸۲ درصد کاهش یافته است.
به گفته او، جمهوری اسلامی همچنان تعدادی موشک و پهپاد در اختیار دارد، اما این تجهیزات تنها بخش کوچکی از توان پیشین ایران را تشکیل می‌دهند و ظرفیت تولید آن‌ها نیز به‌شدت آسیب دیده است.
ترامپ در بخش دیگری از سخنانش، گزارش‌های رسانه‌ای درباره وضعیت ایران را هدف حمله قرار داد و با اشاره به تورم و کاهش ارزش ریال گفت ادعای عملکرد موفق جمهوری اسلامی در جنگ با واقعیت‌های اقتصادی این کشور هم‌خوانی ندارد.
وزیر خارجه جمهوری اسلامی روز شنبه ۲۴ مرداد در گفت‌وگو با «شهرآرانیوز» گفت هیچ مذاکره‌ای میان ایران و آمریکا در جریان نیست و تهران هنوز درباره از سرگیری مذاکرات تصمیم نگرفته است.
عباس عراقچی گفت قطر و پاکستان با تهران و واشنگتن در تماس‌اند و میان دو طرف پیام‌هایی ردوبدل می‌کنند، اما این ارتباطات به معنای آغاز مذاکره نیست.
وزیر خارجه جمهوری اسلامی همچنین گزارش‌ها درباره وجود یک «آتش‌بس ۶۰ روزه» را رد کرد.
به گفته او، در تفاهم‌نامه اسلام‌آباد از «پایان جنگ» و تعیین یک مهلت ۶۰ روزه برای گفت‌وگو درباره توافق نهایی سخن گفته شده بود، نه آتش‌بسی که اکنون نیازمند تمدید باشد.
عراقچی مذاکرات تهران و مسقط را نیز «فنی و تخصصی» خواند و گفت ایران و عمان در حال تعیین مسیرهای دریایی تازه‌ای برای عبور کشتی‌ها از تنگه هرمز هستند.
نیروهای مسلح دو کشور نیز در این گفت‌وگوها مشارکت دارند.
به گفته او، ابتدا یک مسیر موقت برای رفت‌وآمد کشتی‌ها تعیین خواهد شد که ممکن است مبنای مسیر نهایی قرار گیرد.
عراقچی در عین حال تأکید کرد تعیین مسیر کشتیرانی و بازگشایی تنگه هرمز دو موضوع جداگانه‌اند.
او بازگشایی این آبراه را به تحقق شروط جمهوری اسلامی از سوی آمریکا مشروط کرد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 364K · <a href="https://t.me/VahidOnline/77874" target="_blank">📅 11:37 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77873">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/3500bcce36.mp4?token=M8bGeOh1tCep6BpEJYXn-QaDmhHUoSPSI8Avx-xW2_jtbLzTihz-jTDl8FVoWIah3GGN7xez5y_DcWQdy0MeWrIIQNqZcXnCNwpV1f2-dtOTk0QANM9kArIKupl0dJS1AuwXbtPIc6IzQcCkVbKsrbVaFRDY-jppjOaTPisWQRhbHUcL99CE6E5LMsNxmoF-q_1EF_mPYSy0JR1yzTO-bI1wwGGEYH81ckhFgw5zCdxsFcIT20QhWT2MVQ14O-kZMRdEblZpdPxBNxgdmiR9-L3BHSRWR2fSzqf16GpdaZP7o0Xj1FuGeyEg1K7mCZQI06in-hFNvhSJbooHyH5k1Q" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/3500bcce36.mp4?token=M8bGeOh1tCep6BpEJYXn-QaDmhHUoSPSI8Avx-xW2_jtbLzTihz-jTDl8FVoWIah3GGN7xez5y_DcWQdy0MeWrIIQNqZcXnCNwpV1f2-dtOTk0QANM9kArIKupl0dJS1AuwXbtPIc6IzQcCkVbKsrbVaFRDY-jppjOaTPisWQRhbHUcL99CE6E5LMsNxmoF-q_1EF_mPYSy0JR1yzTO-bI1wwGGEYH81ckhFgw5zCdxsFcIT20QhWT2MVQ14O-kZMRdEblZpdPxBNxgdmiR9-L3BHSRWR2fSzqf16GpdaZP7o0Xj1FuGeyEg1K7mCZQI06in-hFNvhSJbooHyH5k1Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ: تنگه هرمز را قلمروی آمریکا اعلام خواهم کرد
دونالد ترامپ، رئیس‌جمهوری ایالات متحده، طی یک سخنرانی در جمع نیروهای مجری قانون در «لانگ‌آیلند» در ایالت نیویورک گفت: پس از آنکه شکست دادن ایران را تمام کنیم، که هم‌اکنون نیز به سختی در حال شکست خوردن است، خیلی زود تنگه هرمز را قلمرو ایالات متحده اعلام خواهم کرد.
در اصل هم ماجرا همین است، ما محاصره را در دست داریم و هیچ کشتی‌ای از آن عبور نخواهد کرد مگر اینکه ما بخواهیم.
@
VahidOOnLine
برایان شوراتز، خبرنگار وال‌استریت ژورنال می‌نویسد که به گفته یک مقام ارشد کاخ سفید دونالد ترامپ، رئیس‌جمهوری آمریکا، با مشاوران خود درباره اعلام تنگه هرمز به‌عنوان قلمروی ایالات متحده دیداری نداشته و هنگام مطرح کردن این موضوع در سخنرانی روز جمعه خود در ایالت نیویورک، در حال شوخی بوده است.
آقای ترامپ پس از بیان سخنانش درباره تنگه هرمز خنده‌ای کرد. او پیشتر نیز درباره برداشت رسانه‌ها از شوخی‌هایش، صحبت کرده است.
رئيس‌جمهوری آمریکا در سخنرانی روز جمعه خود اشاره کرد که آمریکا عملا تنگه هرمز را تحت کنترل دارد چون هیچ شناوری بدون اجازه آمریکا نمی‌تواند از آن عبور کند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 402K · <a href="https://t.me/VahidOnline/77873" target="_blank">📅 00:18 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77871">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/d41b4db679.mp4?token=fZB0Ckox7i85p1Z7eAQXcnfpi_Pc_R4JJTWO0lfd_4jKrPziWZxkVRsnXV4Ts2zm2bxqmf2LoMN6DTfJw3SMjYJgpP8H6EhWMxCXP8ADyq9JphsCMpm7smT1i64XgC243qs4JjS2ktL87-IViH7zmMl6IBFpWK3HrbVIvDUqPtYGhIlI87nU224xN05hgBqkrQZaYB5VFov9_X4k2gnqfw4kxnwn-qcoZUhBqveXSJDxrukGJK_gBZ69ZOZIcg7np6con5n73WmlmPSd7qJU3JEcyYMvrII3U1P-d8l66m8hOaSFGT3wTe7y1xc7q32qj1cjPcZ3AJuQCrjknYXSOw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/d41b4db679.mp4?token=fZB0Ckox7i85p1Z7eAQXcnfpi_Pc_R4JJTWO0lfd_4jKrPziWZxkVRsnXV4Ts2zm2bxqmf2LoMN6DTfJw3SMjYJgpP8H6EhWMxCXP8ADyq9JphsCMpm7smT1i64XgC243qs4JjS2ktL87-IViH7zmMl6IBFpWK3HrbVIvDUqPtYGhIlI87nU224xN05hgBqkrQZaYB5VFov9_X4k2gnqfw4kxnwn-qcoZUhBqveXSJDxrukGJK_gBZ69ZOZIcg7np6con5n73WmlmPSd7qJU3JEcyYMvrII3U1P-d8l66m8hOaSFGT3wTe7y1xc7q32qj1cjPcZ3AJuQCrjknYXSOw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">«بریم نجف» از نوحه حکومتی تا ترند شبکه‌های اجتماعی علیه سفر اربعین
همزمان با راهپیمایی اربعین، انتشار ویدئوهای بلاگرهای حامی حکومت با نوحه «بریم نجف، پس می‌ریم نجف» به سوژه کاربران شبکه‌های اجتماعی تبدیل شد.
کاربران با استفاده از همین صدا، ویدئوهایی متفاوت ساختند؛ از سفر و تفریح به جای رفتن به نجف تا کمک به نیازمندان و غذارسانی به حیوانات بدون سرپرست.
اما ظاهراً همه این ویدئوها بی‌هزینه نبودند؛ زنی که ویدئویی از غذارسانی به حیوانات با همین نوحه منتشر کرده بود [ویدویی دوم بالا]، به پلیس فتا احضار شد. [همه پست‌های قبلی‌اش حذف شد و پستی از طرف حکومت در صفحه‌اش درج شد]
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 404K · <a href="https://t.me/VahidOnline/77871" target="_blank">📅 18:26 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77870">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/c594f01e2b.mp4?token=brxtCfagaGE6ks3dsptIPUH66cr4sIILe5kRMtcF63OAFSV4fIDtaF5Fjmm4dLR9guPsJf8s7RXZBMjsUS8tX4nD-UUIGE0dMFGbensDOB_nvIu8qu03yOHm33z7ZesaAcaFhLZkeo5RdRRA1FoT3dWPa2knJMzA0bk4O-uYZePGhecqY9K5Eac8tFbQWD9Cjn1b-Rqtc0HyyN441cswlR7n4ZlKcdBj9AHkvSOE_JVMMY9aApdeeriuCILstN9gTaT2AqkoceoThdoevANWJwAxpj1EGmMoJa48vVoZ-ZTjUp7zT1JM5yj4B1AtNZtYViwqEzTlmEnvadx0D9HDloi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/c594f01e2b.mp4?token=brxtCfagaGE6ks3dsptIPUH66cr4sIILe5kRMtcF63OAFSV4fIDtaF5Fjmm4dLR9guPsJf8s7RXZBMjsUS8tX4nD-UUIGE0dMFGbensDOB_nvIu8qu03yOHm33z7ZesaAcaFhLZkeo5RdRRA1FoT3dWPa2knJMzA0bk4O-uYZePGhecqY9K5Eac8tFbQWD9Cjn1b-Rqtc0HyyN441cswlR7n4ZlKcdBj9AHkvSOE_JVMMY9aApdeeriuCILstN9gTaT2AqkoceoThdoevANWJwAxpj1EGmMoJa48vVoZ-ZTjUp7zT1JM5yj4B1AtNZtYViwqEzTlmEnvadx0D9HDloi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پدر عباس قنبری، در سالروز تولد فرزندش، با حضور بر سر مزار او در گویم شیراز سوگوارانه می‌رقصد و یادش را گرامی می‌دارد.
عباس قنبری، مهندس و ورزشکار اهل گویم شیراز، روز ۱۸ دی‌ماه ۱۴۰۴ در جریان اعتراضات در مقابل کلانتری گویم، بر اثر اصابت گلوله جنگی جان باخت. از این معترض جان‌باخته، یک دختر خردسال به یادگار مانده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 370K · <a href="https://t.me/VahidOnline/77870" target="_blank">📅 17:15 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77869">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ugvhvYj7WScrgzVCk-4H7pzNun43r5qj2IScMA837j8Zn4VbupN3sK0Ummgt3gmFXFmZyiOdFCz8B6LnfI84_0vKlII3dD3G3HWaivLgqoTsjtfbWWN1CzRzWa3Unw-ZUfFHKF0ZqpPEvGtso2Qggq4JabWAHlxD2hnOg4HbktkHGvVzJpdh--5ku3-4EnaRa4KgyTDiK-fJ2YEDnxl_aoKTh_5uKlK4VHPwNFUwF3t_cCNBbgYcLq61wMsVuwJ6yggtYHb2A1kIcqwuVtw707Tx1oD0aOXKu-1qGXaVmLwHfg4ttNdCHd1MFM7PkDonVMu2gomlxtlODG2r1y0fFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مریم طهماسبی، عروس معصومه ابتکار، از گروگانگیران سفارت آمریکا در تهران، که به همراه همسر و فرزندش بازداشت و هم اکنون در مرکز پردازش اداره مهاجرت آمریکا در تگزاس نگهداری و منتظر اخراج از آمریکا هستند، نامه‌ای خطاب به مردم آمریکا در نشریه «نیشن» به همراه عکس بی حجاب خود منتشر کرده و از عمق علاقه خود به آمریکا صحبت کرده است.
وی در این نامه گفته است که او و همسرش عیسی هاشمی، «معلم و استاد دانشگاه از طبقه کارگر هستند» و پسرشان، فقط انگلیسی صحبت می‌کند و از دوران پیش‌دبستانی در نظام آموزشی کالیفرنیا پرورش یافته است.
پسر و عروس معصومه ابتکار با ویزاهایی که در دولت اوباما صادر شده بود، در سال ۲۰۱۴ وارد آمریکا شدند و چندی بعد اقامت دائم دریافت کردند.
دفتر سخنگوی وزارت خارجه آمریکا ۲۲ فروردین‌ماه اعلام کرد که کارت سبز (گرین کارت) مریم طهماسبی و عیسی‌ هاشمی را لغو کرده و آنها به همراه پسرشان در تاسیسات تحت نظارت اداره مهاجرت آمریکا نگهداری می‌شوند. در این بیانیه به نقش محوری معصومه ابتکار در ماجرای گروگانگیری اعضای سفارت آمریکا در تهران اشاره شده است که اندکی بعد از انقلاب ۵۷ اتفاق افتاد.
مریم طهماسبی در حالی در نامه خود مدعی شده که مادرشوهرش «فقط برای گروگان‌گیران مترجمی می‌کرد» و «ماجرا مربوط به ۵۰ سال پیش است» که معصومه ابتکار در پاسخ به یک خبرنگار خارجی که از او پرسید «آیا حاضری اسلحه به دست بگیری و گروگان‌های آمریکایی را بکشی؟»، پاسخ داد: «بله».
معصومه ابتکار در دهه‌های بعد نیز اعلام کرد که از شرکت در گروگانگیری اعضای سفارت آمریکا در تهران پشیمان نیست. گروگان‌های سابق از جمله بری روزن نیز معصومه ابتکار را یک بازجوی عصبانی و خشن توصیف کرده‌اند.
کارزار درخواست اخراج فرزندان و وابستگان مقامات جمهوری اسلامی که در آمریکا اقامت دارند، با کشتار معترضان در دی‌ماه ۱۴۰۴، شدت گرفت و همزمان خبرهای اخراج برخی از آنها از جمله فاطمه لاریجانی، دختر علی لاریجانی، دبیر کشته شده شورای عالی امنیت ملی منتشر شد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 354K · <a href="https://t.me/VahidOnline/77869" target="_blank">📅 17:14 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77867">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/RjKytsNmzsaYsJvLXHdci8-TbcmsSgk7acA2kkMJlEpjC89IPu_FqQ2YNuxkJGpewjekKSQDVPSeM_FduExjQpdlNVMpw1PYqIgE1jmRvHi8Jv0YDHZdbYf0XNN5jX4zSMMaCrQWju3-jXMe0R-BEDgkBr-AglHFV0xAPmFYaxo5JkGSpCJHBj7aBYRVELCgaCAQoIJINI7BUWSgzPlNmflt8iXjJ_8ynr14bR8inAoCnCRWGr7sSuPMfvsCXQrsISt-U5goJN0N_prkRH-JgSRXZ2Ggz_VhI2LYoKCzaTsqYjsyjhI0ZU8VuNdaSQKfxqvttlCqr7sacvP7xUtjGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/193ca661cb.mp4?token=AWPXSiaELphQzGfqMRPKBm5IRDFGCxMg26tWT7yIwsrqIfaesfdDtPXoVSmpjn-jNhr4TtmuyMewK1ndbI38d3-WLfKqjtuj5Kav3Zi9r4dOvFCKkOocavzGy--j4NW8qFmShwLHFVUrbTz4AyM8j6UFirBXvDWOrzuau1MBspgV--vAcVr6Z2QO6WnPc-vCgYJl8LQOCe4ximwYcRFM4fBEI3MuqEV8zymsp79hfwwLAyLsZ_xoGDkTZPXHHsdiPgpqzmQovDTPfIpPx5KcCRwYcf9eeyBNnB5-BCDUJkrzsRiGvnSlh1mq83RNK6VRFngj_z1kAzRIS5oedBPNXQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/193ca661cb.mp4?token=AWPXSiaELphQzGfqMRPKBm5IRDFGCxMg26tWT7yIwsrqIfaesfdDtPXoVSmpjn-jNhr4TtmuyMewK1ndbI38d3-WLfKqjtuj5Kav3Zi9r4dOvFCKkOocavzGy--j4NW8qFmShwLHFVUrbTz4AyM8j6UFirBXvDWOrzuau1MBspgV--vAcVr6Z2QO6WnPc-vCgYJl8LQOCe4ximwYcRFM4fBEI3MuqEV8zymsp79hfwwLAyLsZ_xoGDkTZPXHHsdiPgpqzmQovDTPfIpPx5KcCRwYcf9eeyBNnB5-BCDUJkrzsRiGvnSlh1mq83RNK6VRFngj_z1kAzRIS5oedBPNXQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در جریان یک درگیری میان عزاداران در صحن حرم امام هشتم شیعیان در مشهد، دست‌کم دو نفر زخمی شدند.
به گزارش تسنیم، این درگیری پنجشنبه ۲۲ مرداد حدود ۱۰ و ۳۰ دقیقه شب رخ داده است.
رسانه‌های ایران می‌گویند هیئت‌های مختلف با چوب‌های مخصوص عزاداری مشغول اجرای مراسم بودند که ناگهان میان دو هیئت درگیری شکل گرفت و عزاداران چوب‌های خود را به سمت یکدیگر پرتاب کردند.
تسنیم به نقل از امیرالله شمقدری، دبیر شورای تامین خراسان رضوی نوشت که دو نفر زخمی به بیمارستان منتقل شده‌اند و حال آنان مساعد است.
@
VahidHeadline
خبرگزاری فارس، وابسته به سپاه پاسداران، با اشاره به درگیری با چوب میان شماری از حاضران در صحن «امام هشتم شیعیان» و هیات‌های مذهبی در مشهد در شامگاه پنج‌شنبه، نوشت که بروز اختلافات سلیقه‌ای در نحوه ورود و خروج یا خستگی ناشی از گرما، امری طبیعی و قابل مدیریت است و نباید به دعوا ختم شود.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 340K · <a href="https://t.me/VahidOnline/77867" target="_blank">📅 17:11 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77865">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/HFQ4kt56exev5Rl25zuWjpMqjbv3MUAGHEIUs1kt26VG0oiBk2htB3kxmS4zFmzAP7pFRzSaM4ZdNMznHgCuJgUaqxHpp1PKWzIoErq7UFPGeaxWSYR8bbOfV4xPfkJE61_TtRzquUoTIJoloh7vJPdIDOSS2btHr1g2TubTpXqW_ID7OqA_UAelLKQkEi0cEfx-dRRucqmMFDtG7pScahRnH6UST1YIt9xJ3dTrUlSoiUZuvWgmZv1N6DGDc2AdgUVHpLMwFN_hRcGvWq-m19rVLQfgoJsGCAFx7hF0pnYS-dZQbLuWzOiK-mUphGmqEaJUJyL1uTKEgpU0QoMKgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/e-JmvIOkgqJ4uxGQA2OQpPOuDpQtmluD5d9IiYSQjWjD7Fota-Vcdspl34tOoUPMI8whC9Xxv8elfxPmfvV0H8egP6i9qVcK01nXT63fOHRbTQR4Il6znYEepFUmA577zdGVTwtF7ZFnZYkO3pNhAnPf--dbpAWIrAbl9PCErs0ad1UJ_AgM08EKkmc8afnhuaKYSoTeSqsmsK_YzhF9NXFn_inrQwpjk1fQ4G7ryDorAPSGMnXuFK79Jt5GsU-YBwh9GMCd7spH6jpSzTLHH1S9PA5t3lYgJVwiPlEJnn48RlAKf0WUMriiNZSGD7w4dOGsN71wqpoMVtG_7H3I-w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">دونالد ترامپ، رییس‌جمهوری آمریکا، با بازنشر گفت‌وگوی اسکات بسنت، وزیر خزانه‌داری آمریکا، با شبکه نیوزمکس در تروت سوشال، بر برنامه دولتش برای تشدید فشار اقتصادی بر جمهوری اسلامی و رساندن «انزوای اقتصادی ایران به سطحی بی‌سابقه» تاکید کرد.
بسنت در این مصاحبه از اعلام اقدامات جدید علیه جمهوری اسلامی در هفته آینده خبر داد. او افزود واشینگتن قصد دارد سیاستی شامل انزوای شدید اقتصادی جمهوری اسلامی و ادامه محاصره در تنگه هرمز اجرا کند.
به گفته اسکات بسنت، این محاصره مانع ورود هرگونه کالا به بنادر ایران یا خروج کالا از این بنادر می‌شود.
@
VahidOOnLine
وزیر خزانه‌داری آمریکا نیز روز پنجشنبه ۲۳ مرداد با هشدار به تهران در مورد اعمال مجازات‌های اقتصادی بیشتر، تهدید کرد که ایران را در معرض انزوای اقتصادی قرار خواهد داد، «به گونه‌ای که جهان تاکنون به خود ندیده است».
اسکات بسنت به شبکه تلویزیونی محافظه‌کار «نیوزمکس» گفت: «ادامه محاصره در تنگهٔ هرمز... مانع از ورود یا خروج هر چیزی به بنادر ایران خواهد شد».
او افزود: «منتظر اخبار و اطلاعیه‌های بیشتری در این زمینه در هفته آینده باشید».
بسنت رویکردی دوگانه را توصیف کرد که شامل فشار مالی و محاصره فیزیکی بنادر می‌شود.
ترامپ اخیراً گفته بود تنها در صورتی از حمله مجدد به ایران خودداری می‌کند که توافقی برای بازگشایی سریع تنگهٔ هرمز حاصل شود.
ایران فهرستی از شرایط را برای بازگشایی این گذرگاه تعیین کرده که بعید است دولت ترامپ آن‌ها را بپذیرد: پایان جنگ در همه جبهه‌ها، لغو محاصره بنادر ایران توسط آمریکا، پایان تحریم‌ها، آزادسازی دارایی‌های مسدود شده و جبران خسارات زمان جنگ.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 279K · <a href="https://t.me/VahidOnline/77865" target="_blank">📅 17:03 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77864">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/RRq_zAv7DgQgmHEVdRx96i5np45TdDeFWteJjSDYN5n2alPggWe5mjoG8scKDBj6Blj68QpZMTyMD_tqtZjajXMgXdFJ-wzsJyx9e8MvuprhdI1RhFwe3Mc2o7hR9LGYeLlV7iD7yXwc8hnz0hQsSEF1s47pZziz4MN11TZ6UhER_UGyIXItXwB4Cb4PPZqU5EQJ8G0kV3X_dJEyhuJVxbGix60n8WkUHS47Ztocab2JNAhvmD3POUF7TzWn7m9ceNqb5W3cbP7ynIVVsblLMhB_4QojyEIS-_Oc0FofH-g0qjrDKFebhJe5vjsAkadaLRXdoOwr_IxNytCcPIdRHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بنیامین نتانیاهو، نخست‌وزیر اسرائیل، در یک پادکست رادیو ارتش اسرائیل، با انتقاد از مواضع اخیر بریتانیا در قبال اسرائیل، با لحنی کنایه‌آمیز گفت اولین «جمهوری اسلامی» مجهز به سلاح هسته‌ای، «جمهوری اسلامی بریتانیا» خواهد بود.
نتانیاهو روز پنجشنبه ۲۲ مرداد، در این گفت‌وگو با اشاره به تغییر رویکرد دولت بریتانیا در قبال اسرائیل گفت: چیزی شبیه به جمهوری اسلامی را امروز می‌توان در بریتانیا دید. چیزی که من به آن می گویم جمهوری اسلامی بریتانیا.
نخست‌وزیر اسرائیل در این پادکست همچنین از مواضع بریتانیا درباره جنگ غزه و سیاست این کشور در قبال اسرائیل انتقاد کرد و گفت اسرائیل در شرایطی قرار دارد که باید در برابر تهدیدهای منطقه‌ای از خود دفاع کند.
اظهارات نتانیاهو در شرایطی مطرح شده که روابط اسرائیل و بریتانیا طی ماه‌های اخیر بر سر جنگ غزه، وضعیت انسانی در این منطقه و سیاست دولت بریتانیا در قبال اسرائیل پرتنش‌تر شده است. دولت بریتانیا در ماه‌های گذشته فشارهای بیشتری بر اسرائیل وارد کرده و درباره وضعیت غیرنظامیان فلسطینی و ادامه عملیات نظامی اسرائیل در غزه ابراز نگرانی کرده است.
نتانیاهو در حالی از بریتانیا با عنوان «جمهوری اسلامی» یاد کرده که این کشور متحد دیرینه اسرائیل و یکی از قدرت‌های اصلی غربی است. استفاده از چنین تعبیری از سوی نخست‌وزیر اسرائیل، واکنشی به تغییر موضع لندن در قبال دولت اسرائیل و جنگ غزه محسوب می‌شود.
این اظهارات همچنین در شرایطی بیان شده که دولت اسرائیل همچنان جمهوری اسلامی ایران را یکی از اصلی‌ترین تهدیدهای امنیتی علیه خود می‌داند. نتانیاهو در این گفت‌وگو بار دیگر بر تلاش اسرائیل برای جلوگیری از دستیابی جمهوری اسلامی به سلاح هسته‌ای تأکید کرد.
اظهارات نخست‌وزیر اسرائیل با واکنش‌هایی در بریتانیا روبه‌رو شده و برخی منتقدان آن را توهین‌آمیز و بی‌سابقه توصیف کرده‌اند. این اظهارات بار دیگر شکاف میان دولت اسرائیل و دولت بریتانیا درباره نحوه برخورد با جنگ غزه و آینده روابط دو کشور را برجسته کرده است.
@
VahidHeadline
سخنگوی نخست‌وزیر اسرائیل از اظهارات بنیامین نتانیاهو درباره بریتانیا و توصیف این کشور به عنوان یک «جمهوری اسلامی» دفاع کرده است.
روابط بریتانیا و اسرائیل که متحدین دیرینه هستند، از زمان جنگ غزه به شکل محسوسی پرتنش‌تر شده است.
دولت بریتانیا تاکنون واکنشی به این اظهارات نشان نداده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 269K · <a href="https://t.me/VahidOnline/77864" target="_blank">📅 16:57 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77863">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ICpHJhdfzbi_x8v4Uz7J9udP7R3v_NgBr7owxKeNCZuZm1WIo32Xjryw0D-5SkXal5Jj4gRHZLI0vfDZwlhTXC7vm7XWvV6G5euUK4q_YoA4440dAheoNdWgXUzgXQ4XuFNU-1aDIGRAg5q-3MoSisJtV2-sjmikP9IwfIIjgqHuHDfYsuKWe-LZQyugzx_qusF2TRcSEMBwN01-eAEzI-Qd1Y7mnZzaAed_RYnQNLOUfGfMSCpUWNARwgOsUkBnur85RhJzWHqcESI97OsSUX2mLgW5wgl-K9CtSchgkZn88aNsCtht4OHy4WmOYPak_4pv48Mq4ORrEAYG0QpZlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزارت امور خارجه امارات متحده عربی بامداد جمعه ۲۳ مردادماه با انتشار بیانیه‌ای، حمله به دو نفتکش وابسته به شرکت ملی نفت ابوظبی (ADNOC) هنگام عبور از تنگه هرمز را به‌شدت محکوم کرد.
در این بیانیه آمده است که این حمله بدون بر جای گذاشتن تلفات یا مصدوم، دو نفتکش وابسته به «ادنوک» را هدف قرار داده است.
وزارت امور خارجه امارات این اقدام را نقض آشکار قطعنامه ۲۸۱۷ شورای امنیت سازمان ملل دانست و تاکید کرد که هدف قرار دادن کشتی‌های تجاری یا مختل کردن مسیرهای بین‌المللی دریانوردی، مغایر با اصل آزادی کشتیرانی است.
در این بیانیه همچنین آمده است که هدف قرار دادن کشتی‌های تجاری و استفاده از تنگه هرمز به‌عنوان ابزار فشار یا اخاذی اقتصادی، از سوی امارات اقدامی «دزدی دریایی» از جانب سپاه پاسداران ایران تلقی می‌شود و تهدیدی مستقیم برای ثبات منطقه، امنیت کشتیرانی و امنیت انرژی جهان به شمار می‌رود.
وزارت امور خارجه امارات از ایران خواست این حملات را متوقف کند، تمامی اقدامات خصمانه را پایان دهد و امکان بازگشایی کامل و بدون قید و شرط تنگه هرمز را فراهم کند تا امنیت منطقه و ثبات تجارت و اقتصاد جهانی حفظ شود.
@
VahidOOnLine
عربستان سعودی نیز با انتشار بیانیه‌ای هدف قرار گرفتن این دو نفتکش ناوگان انرژی امارات را «با شدیدترین عبارات» محکوم کرد.
به گزارش العربیه، ریاض در این بیانیه با تاکید بر مخالفتش با حملات ایران به «کشتی‌ها و نفتکش‌های تجاری» در خلیج فارس، تهران را مسئول پیامدهای ادامه این حملات دانست.
پادشاهی سعودی در ادامه با اقداماتی که امارات «برای حفظ حاکمیت، امنیت و منابع خود»  اتخاذ می‌کند، اعلام همبستگی کرد.
@
VahidOOnLine
وزارت امور خارجه بحرین هدف قرار دادن دو نفتکش شرکت ملی نفت ابوظبی (ادنوک) در تنگه هرمز را به شدت محکوم و آن را «باج‌گیری اقتصادی» جمهوری اسلامی ایران از کشورهای منطقه توصیف کرد.
بحرین در این بیانیه در حمایت از امارات متحده عربی افزود، امنیت در تنگه هرمز را برای «حفظ امنیت انرژی، ثبات عرضه مواد غذایی و دارویی و تضمین جریان تجارت جهانی» ضروری دانست و خواستار آن شد ایران از آن برای «اعمال فشار یا باج‌گیری اقتصادی» استفاده نکند.
@
VahidOOnLine
وزارت خارجه مصر نیز در بیانیه‌ای خواستار توقف همه اقداماتی شد که امنیت کشتیرانی بین‌المللی را تهدید می‌کند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 268K · <a href="https://t.me/VahidOnline/77863" target="_blank">📅 16:56 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77862">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/bVjgWAvzRPTmaMG9a1bWc5fj2iPrgg2-9n-LXWAxcfvxJy4kWbc0uAUvGZASBvY2OVy-T-DMHkpzVDJHKWCrwa58N-ctdZtmbcWySQMVfWEOjUe7IklK0whLIij7ve4Vj2tuRtKuVcLwZTDez1qeifbQJVLrhfMYPSMEbWLUIeYq9-ZpF0-2Bi9NcpT0XQ9geOStarWqh18Fna4r7wE9S8V4fxUsreBo5unDokwWNBX0YRzU1PIxI65rH5M-Maeyxr9FxyhkUrJJ25CrJ7NJcBvFqZDxzWCpd3dIhjGJLy0qu6YXywJak7jdtwp1NjEE41lTxkwW49-yGFl97Fqpbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صداوسیمای جمهوری اسلامی به نقل از شبکه العربیه گزارش داد که مواضع نیروهای آمریکایی در نزدیکی فرودگاه اربیل، مرکز اقلیم کردستان عراق، هدف حمله پهپادی قرار گرفته است.
بر اساس این گزارش، چندین پهپاد به سمت مواضع نیروهای آمریکایی شلیک شده‌اند و به گفته منابع محلی، یکی از آن‌ها به‌طور مستقیم به یکی از این مواضع اصابت کرده است.
العربیه همچنین گزارش داد که در جریان این حمله، سامانه‌های پدافندی آمریکا فعال نشده‌اند و تنها جنگنده‌های آمریکایی برای رهگیری پهپادها وارد عمل شده‌اند.
در پی این حمله، فرودگاه اربیل به‌طور موقت بسته شده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 270K · <a href="https://t.me/VahidOnline/77862" target="_blank">📅 16:47 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77861">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/YaiwJXaHnF1n2TSDUaoSAUvGZrI4-uFMYp2xUhxISdAzlsKGd5mBU8IjL0KnQDxMU2ntV0Evb3JcKR99Fs9RAyvYhUx0fiFmdOINQoImzGJ3CJJ3UBDwI2nPfG0i7CT9-JA__wd-tIiocO_gYoP6oSV98xsbrVy5Feer19RSNOLBw94QZiMhAA6ENg8C8vnntmKMvj_1v-KPlr-NnNY1IKaBATRGm_nHk--mziiifC_CtbOSTuZYeNVej21dkD2Tbl8CpdASzovRLjAllyJM2WlduuF-FNaJLS8RK6_c1xbWsHXYfcwbJSaXnWMlugCsGxHI38NhtLEDG-INIinqhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مرکز عملیات تجارت دریایی بریتانیا (UKMTO) اعلام کرد یک نفتکش هنگام خروج از تنگه هرمز هدف حمله پهپادی قرار گرفته و در این حادثه خسارات جزئی به کشتی وارد شده است.
بر اساس اطلاعیه این مرکز که روز جمعه ۲۳ مرداد منتشر شد، در این حمله همه اعضای خدمه نفتکش در سلامت هستند و گزارشی از آلودگی یا خسارت زیست‌محیطی در پی این حادثه منتشر نشده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 280K · <a href="https://t.me/VahidOnline/77861" target="_blank">📅 16:46 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77860">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/KEO7WpWkQfaTQlvAfxY7rWIaxTOJPo7nvjMA5AKfOj9NH_Y_ukqVr763b2oIrR2E_8m9VN3p8up3B-A54L4ywaxFAngjbdy18k-erRWDa2AOpyezLp9E6Mo3gPxfcrwbMXFCrOQR76tzIYRUqZwCbIzz7CPOdfM4nZsBVmuNUkKFjSVXBJn8rrDBc5PDz2MYz3tJitxrG7189wAcCYI87L9rZmZzP8JWERMDM8gnON8Xt9_xHs4fAi-F6uYXHRmd7oriDcy2I49MOxWVHyPLvTvt99epa8dLpWmvXFmKm76kC8BDqesPRfJ-uVOsqXyAgd3f7c8pY_m2nW9sgNxxvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سایت هرانا گزارش داد تکتم رمضانی، زندانی ۳۷ ساله که بابت اتهامات مرتبط با مواد مخدر بازداشت شده بود و دوران محکومیت خود را در بند دو زندان وکیل‌آباد مشهد سپری می‌کرد، سه‌شنبه ۲۰ مرداد در پی پارگی کیسه صفرا و تعلل در رسیدگی پزشکی و اعزام به بیمارستان جان باخت.
بر اساس این گزارش، رمضانی در چهار روز پیش از مرگ از درد شدید در ناحیه کیسه صفرا رنج می‌برد و با وجود پیگیری‌های مکرر برای دریافت خدمات درمانی، به بیمارستان اعزام نشد و از رسیدگی پزشکی مناسب محروم ماند. او در زندان به‌عنوان کارگر در بخش جمع‌آوری زباله فعالیت داشت.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 285K · <a href="https://t.me/VahidOnline/77860" target="_blank">📅 16:41 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77858">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/tDR1UXhwBlIrPUJbBnig-qap-SvMuctQZkvHUTUw4CT5ymZcum9pF02BYFYRYr2uyeupmE4ZJ-crDAI8NL_FjVCz_2vvMoB-Sze98p4zLJnno0zSlp-gw-oCBEdHrT8ziRYcu9Bskw7P9Xa-TjBC6Sg0ICG7ebHCrLJhNMRCRnmuQP31OnOHaTEakTUk6RQnYxwnNqWzcKxwvTEflamx0eq8dDdlD0Ecpg37Lh9QrPyzDVyr4745TZIsJuh8DxJGQ1sDE3mqs83HENTxiL-_363iRD53d65ZQ6HNtSygPpAtcCTi2zVJyuvgpY2x1RNnEKWuD4rPvQ7GSOPu-5ns1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/gfUCy0-tH2EbwP2fQ2DZpTCkf6p9dDiYEprtyYbGEslxlnLv4Bil-Om8Q5zraU2mncsgX2ReNLCwfZ8oGMlbLEzpy0whtk2Pj5yx0NJheZtLl_j60aAPE1dYgOT9n-OhSwwbSgHX31MO4_hPDogVRdsoWpHY11j-31kuOWqrLsenffsixQY2Gir43FHdrDJHbpE3UzqTQIio2P4bvj15-k4e0WstrC5NY5UZhrlGN7K-iTSiXHXtLabL_xc2SL8ul8U3aYuCwHGZhwJHzso0kXEQCV6-rg0rKJaRAnavGIQE55ZN0NnOQFlayOPRxf7qenHFCsGJTF2wojlkykGFJg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">واشینگتن‌پست در سرمقاله‌ای نوشت توافق با جمهوری اسلامی و تزریق منابع مالی بیشتر به تهران، به رفتارهای «مخرب» این حکومت پاداش می‌دهد و زمینه‌ساز دور تازه‌ای از بی‌ثباتی خواهد شد. این روزنامه از دونالد ترامپ خواست مذاکرات را متوقف کرده و سیاست مهار جمهوری اسلامی را ادامه دهد.
هیات تحریریه واشینگتن‌پست جنگ آمریکا علیه جمهوری اسلامی را از نظر راهبردی ناموفق توصیف کرد و نوشت این درگیری نه به تغییر حکومت انجامید و نه توان موشکی و فعالیت نیروهای نیابتی تهران را متوقف کرد. به نوشته این روزنامه، هرچند حملات برنامه هسته‌ای ایران را به عقب انداخت، اما انگیزه تهران برای دستیابی به سلاح هسته‌ای را نیز افزایش داد.
واشینگتن‌پست همچنین نوشت تفاهم پیشین میان واشینگتن و تهران نتوانست اختلاف بر سر کنترل تنگه هرمز را حل کند و ازسرگیری حملات نیز تغییری در واقعیت‌های میدانی ایجاد نکرد. این روزنامه با تاکید بر تاثیر تحریم‌ها و محاصره دریایی بر اقتصاد ایران، پیشنهاد کرد آمریکا به‌جای توافق، فشار اقتصادی، محدودیت صادرات نفت، مقابله با نیروهای نیابتی و سیاست مهار جمهوری اسلامی را ادامه دهد.
@
VahidOOnLine
شورای سردبیری واشنگتن‌پست در مقاله‌ای با اشاره به موثر بودن سیاست مهار حکومت ایران و اعمال فشار اقتصادی و محاصره دریایی و در مقابل کاهش کارایی کارت تنگه هرمز در دست ایران، استفاده تهران از این اهرم را به گروگانی تشبیه کرد که از پیش گلوله خورده است.
در این یادداشت آمده است: «تصرف تنگه هرمز از سوی ایران را می‌توان نوعی گروگان‌گیری دانست، اما گروگان از پیش هدف گلوله قرار گرفته است. بازارها عملا بسته شدن تنگه را در قیمت‌ها لحاظ کرده‌اند. قیمت نفت، هرچند بالاست، اما فاجعه‌بار نیست.
علاوه بر این، تأمین‌کنندگان نفت در حال دور زدن این مشکل هستند. دولت ترامپ مدعی است که اکنون روزانه ۵ تا ۷ میلیون بشکه نفت از طریق خطوط لوله ارتقایافته و پایانه‌های جدید صادراتی از منطقه خارج می‌شود. عربستان سعودی نیز در حال تشکیل ائتلافی چندملیتی برای حفاظت از کشتیرانی در دریای سرخ در برابر نیروهای نیابتی ایران است؛ اقدامی که واشینگتن باید با ارائه پشتیبانی اطلاعاتی و فرماندهی از آن حمایت کند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 343K · <a href="https://t.me/VahidOnline/77858" target="_blank">📅 05:24 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77857">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/CYO8gkLVJ_jv7tPcUiRRGTCeRHjVOd8YISFarVpugpD-lFbKdHGBS5jMh0JYJoUN_Ch3iqXJonuIvrhc2fOJsn498B-tcZYMlyKBOaoACQHUmrV9CyHRvRXTSTL7Ds_IlwnOeWsNGUzI3iysCu5Fl2j0YpGawRzqDb62vxc2G1d-4HIaF8j9DNsOI6wdiTcvQPfh6I73KFgMKwGHjvFdD-npA8s0dR2nlXDROpZjajW0jljsGjASA5l2GZtRCMrQ_nHUIAVFs-KZ8PccrC2DZETQK3xH2Bhfux5BzJYklncezIxz47HYzS0Ayp_3W-Z9ViWaiA1zaP5hA_4q-MHfGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری رسمی عربستان سعودی (واس) گزارش داد شاهزاده محمد بن سلمان، ولیعهد و نخست‌وزیر این کشور، جمعه ۲۳ مرداد با دریاسالار برد کوپر، فرمانده ستاد فرماندهی مرکزی ایالات متحده، سنتکام، در جده دیدار کرد.
بر اساس گزارش واس،  شاهزاده محمد بن سلمان و برد کوپر در این دیدار درباره همکاری‌های دفاعی عربستان سعودی و ایالات متحده گفتگو کردند و آخرین تحولات منطقه را مورد بررسی قرار دادند. دو طرف همچنین درباره تلاش‌ها برای کاهش تنش‌های منطقه‌ای و تقویت امنیت و ثبات گفتگو کردند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 304K · <a href="https://t.me/VahidOnline/77857" target="_blank">📅 05:21 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77856">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/c1726204da.mp4?token=Uy1gMZ_m6H8Y-8Q8Xb821Fdiw3aL9w7plhXskObqkWYJemFBhVBHTrxlobeSSRkBQqyzH-T4ztLRmfGqS1FRP2PD0SOkzCBgZsYf8RFHYqF0RlXisIxh-tQ-N9XPNE_7DUbUC3sxatlUQEulcP1jE5GFzXWz-MGQD2GX7wn4Pi4LyN4_EKhx_ox5Ew_Nckx7xftsptMexQEIv8ER6_g655bxHqhyw9G-mWwWlJQuKwaQ2b6izowvyQG2V0iLVLOrVQ94_uMTcr9DhISjFa2UzCYyXERSyoSilWP4zueGgJcl8pFdKm1CK_9dU87QfHSToeJzzQsP1mKhsP6D1zRhkA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/c1726204da.mp4?token=Uy1gMZ_m6H8Y-8Q8Xb821Fdiw3aL9w7plhXskObqkWYJemFBhVBHTrxlobeSSRkBQqyzH-T4ztLRmfGqS1FRP2PD0SOkzCBgZsYf8RFHYqF0RlXisIxh-tQ-N9XPNE_7DUbUC3sxatlUQEulcP1jE5GFzXWz-MGQD2GX7wn4Pi4LyN4_EKhx_ox5Ew_Nckx7xftsptMexQEIv8ER6_g655bxHqhyw9G-mWwWlJQuKwaQ2b6izowvyQG2V0iLVLOrVQ94_uMTcr9DhISjFa2UzCYyXERSyoSilWP4zueGgJcl8pFdKm1CK_9dU87QfHSToeJzzQsP1mKhsP6D1zRhkA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">معاون رئیس‌جمهور آمریکا گفت که اولویت اصلی ایالات متحده در جنگ با ایران دیگر برنامه هسته‌ای این کشور نیست، بلکه کاهش قیمت بنزین برای مصرف‌کنندگان آمریکایی است.
جی‌دی ونس به شبکه فاکس نیوز گفت که جلوگیری از دستیابی ایران به سلاح هسته‌ای اکنون در مقایسه با برقراری مجدد جریان آزاد نفت از طریق این تنگه، در اولویت دوم قرار گرفته است.
معاون رئیس‌جمهور آمریکا افزود: «می‌دانم که قیمت نفت امروز کاهش یافته و نسبت به اوج قیمت‌ها در روزهای اولیه درگیری بسیار پایین‌تر آمده است. این هدف شماره یک است؛ ارزان نگه داشتن نفت و گاز برای آمریکایی‌ها در سراسر کشورمان».
او تصریح کرد: «و البته هدف شماره دو این است که اطمینان حاصل کنیم ایران هرگز به سلاح هسته‌ای دست پیدا نمی‌کند».
این اظهارات در حالی است که دونالد ترامپ، رئیس‌جمهور آمریکا، همواره برنامه هسته‌ای ایران را به عنوان دلیل اصلی خود برای جنگ مطرح کرده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 327K · <a href="https://t.me/VahidOnline/77856" target="_blank">📅 05:20 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77855">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/qxD4z_Elm-7veN00iljNTXnd3aYWh7E2yu-Nc3QnlsaekdDAb6x7vGWKN-PB6BSe09Kmieqi7TXTULW2nqxsv2hqj8ol4exxbieNlhjIm8gq2Tu9n9SzjDQPXOCen-oVObi62_7nqZ2KrgavweAupim_XGwC1tJHG5NucBRl2FojxVE_c_EPPO7Vp1HpPRicBzsWY4fNsc4E_EGz_WXRnl9NFcmzHRGEOYw3sG9yZeR8s4yXBBbfjR9Kj93n4Zo7DjCZlx7JC7mON4Bto8sTPP57y5Lfz9tLprrAzyhoEWsUdotLiZFA5YP2Vm3mIWcNkEbiRSdEKqF8YoIIhKsETQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در پیام‌ها از زمین‌لرزه حوالی اندیمشک و دزفول در شمال استان خوزستان خبر می‌دن.
آپدیت:
تصویر و پیام دریافتی:
بزرگی زلزله: ۴.۵
حسينيه، خوزستان
عمق: ۸ کیلومتر
زمان زلزله: ۱۴۰۵/۰۵/۲۳ ۰۰:۵۳:۴۷.۹
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 341K · <a href="https://t.me/VahidOnline/77855" target="_blank">📅 00:56 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77854">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/R4H5bcsGSJ3NNNZgVxwT2asV2j-S-d0hY6M-BEmf-o-VhAUcTwujk5zL1PpI5OhRbf8dEAtgUlOfXFwy_EMurCGIDpgvuY_gMEs6jA9l94uapSfZcVdaTlaNxua4L9Sv9Cnk4m37Y5ZeO_ysCPXZtiP0c77yTYyGTO9ld2hFH3hvpjRaSwH8Zwk6cyt2Wwkoeh5B-7WUcV7r-_Ctu5xmYX2kd-Qu6p3Nb17P8wPz5_3ANQfpQ8Hm1nq1LMbyA5-CSPFQmHp8t_3LzazZ4OPbcDCiZKomBwD_UEoHhP0Ibw49sR3ueQToGole81X0JZJTFeqLjEJb92Mnl23iuoqjKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فرماندهی مرکزی ایالات متحده، سنتکام، روز پنج‌شنبه ۲۲ مرداد از آغاز روند تشکیل نخستین یگان چندملیتی و چندحوزه‌ای پهپادهای تهاجمی خبر داد.
این یگان با نام «نیروی ویژه فالکون استرایک» از پهپادهای یک‌طرفه تهاجمی و سامانه‌های بدون سرنشین هوایی، سطحی و زیرسطحی دریایی استفاده خواهد کرد و نیروهایی از آمریکا و شرکای منطقه‌ای در آن مشارکت خواهند داشت.
سنتکام اعلام کرد رایزنی و دعوت رسمی از کشورهای شریک در منطقه برای پیوستن به این یگان آغاز شده است و با پیوستن آن‌ها، «فالکون استرایک» توانایی‌های پهپادی تهاجمی در خاورمیانه را در قالب یک ساختار چندملیتی و چندحوزه‌ای ادغام خواهد کرد.
«فالکون استرایک» ۹ ماه پس از تشکیل «اسکورپیون استرایک» راه‌اندازی می‌شود. به گفته سنتکام، این یگان پیش‌تر از پهپادهای یک‌طرفه تهاجمی در عملیات نظامی علیه ایران و همچنین از شناورهای بدون سرنشین تهاجمی در حملات ماه ژوئیه به تأسیسات بندری ایران استفاده کرده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 353K · <a href="https://t.me/VahidOnline/77854" target="_blank">📅 21:44 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77853">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/NH1lnAwFk9iEtivliovqlPV0TH7Zz-a3llgmtDKkYeNDjPncgJYfsblmsI84FT4-ZSPUccpen6idKOhvXnv4ywD-l54fRJXL7WlwBps-RcFHQSeof01BcJfZpni1_jhFZzGpbe-hUg2oDV0eD7pIRO5hS_TklDwklkGoUsJUppdziG7wyZ2Tp6eJkV9MW1VzxGfTvcnnyvMhVC8aX8tnHFz0XnGkOTWzBDf1MKOtrUhEncHePNvMyaX_Y7sEzHOy74kECOR8fUwP1uX_5j7jLDa9TDPg6bR7dYR-mlmPx21ETh_V915kpLugGp4-yuIPU0D_hkx_yFXdbMgAKuTfeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تنها چهار روز پس از یک حمله پهپادی به بندر جیزان در عربستان سعودی، خبرگزاری وابسته به حوثی‌های شیعه یمن روز پنج‌شنبه از حمله‌ای دیگر به پالایشگاه آرامکوی مستقر در این بندر خبر داد.
در حالی که هنوز منابع خبری سعودی در این باره اطلاع‌رسانی نکرده‌اند، خبرگزاری سبای یمن نوشته است که این پالایشگاه «با دو پهپاد» هدف گرفته شده است.
روز یک‌شنبه هفته جاری هم این پالایشگاه در پی حمله پهپادی حوثی‌ها دچار حریق شده بود.
جیزان در ساحل دریای سرخ و در نزدیکی مرز یمن و در تیررس حوثی‌های شیعه یمن قرار دارد که از حمایت جمهوری اسلامی برخوردارند.
آرامکو روز پنجم مرداد پس از حمله حوثی‌های یمن که به مجتمع سیکل ترکیبی یکپارچه گازسازی (IGCC) و بخش مخازن پالایشگاه آسیب رساند، فعالیت این تأسیسات را متوقف کرد.
حوثی‌ها در آن زمان اعلام کردند که تأسیسات آرامکو در جیزان و ینبُع را هدف قرار داده‌اند.
پالایشگاه جیزان ظرفیت فرآوری روزانه ۴۰۰ هزار بشکه نفت خام را دارد و فرآورده‌های پالایشی از جمله بنزین و گازوئیل با گوگرد بسیار پایین تولید می‌کند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 323K · <a href="https://t.me/VahidOnline/77853" target="_blank">📅 21:43 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77851">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Y_eBWyoH-XLtcB-sEIK8ZrrTGWoG4rPzJa9V-YshUHHvSAnWPxcisH0Th2genmgAeQaPPp8JlcTcerGbGiOdBxhVMypPhF1J9yI-iVulJpl_xWS_mEdxQ72ox1vwxiXzPVRHOBi6tcdBx9A29LZ2e3l9HY2KWHXfP4MzAwveOLLtF_YJRzHsGtdn95MaySkehBczpbUV3A7UlUxdr813xirFfGMuPXRTaasovprvb90KzE0J28cSNwtsfyXpiPYErBYtgILZbdrQCqu4NhL6DLJL58QBMGZv6W5r3VbdAqPT6ka6OC5awCDA6hlchu-3dLO5CrxE8ALJQd70jDjzFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/JJf2HldKHhrcly7GnDrCk_rAE3G8bg-D_KjYZQxP0A8UisGsTFJz775TtQ5BMcKyh-7XN5_ihx83jyuwqSocHYCMKBd7v_6s12MbUjvCizB1GcQjhCgNhCJ0Bzso8oFTwjRVRHtMVurUxY6qcoRivOfeqcjR5SSXs1zS-Il5iYeCq_cqGLsBEyNCPmquAk4mA_XcKyIFsC16bfzg2O--hnrebwW1Peeqo4xyWmYQiDXfrqRetNdDHCsPfLUZ09HQIBo9Lw1e-7AlpQs0de1ZiWZqz3PwnJmrXuHcMib_N0RHmQFZ2clMWy4cAeVH-vxDVELzTkIwx_AFHToZ0G8DVA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">پیت هگست، وزیر دفاع آمریکا،‌ روز پنج‌شنبه در گفت‌وگو با خبرنگاران تأکید کرد که ارتش این کشور قادر است «تا زمانی نامحدود» به محاصره دریایی بنادر ایران ادامه دهد.
هگست گفت: «نیروی دریایی آمریکا قادر است به طور نامحدود به محاصره دریایی ایران ادامه دهد، چون همان طور که تا الان کرده‌ایم، می‌توانیم کشتی‌ها را [عوض کرده و] وارد و خارج کنیم، و به این کار ادامه خواهیم داد.»
مجیدرضا حریری، رئیس اتاق بازرگانی ایران و چین، در هفته جاری ضمن هشدار درباره این‌که «زندگی در محاصرهٔ دریایی به سطح نازلی سقوط خواهد کرد»، گفت انتقال بار از چین به ایران از راه زمینی «حدود ۱۸ میلیارد دلار هزینهٔ اضافی به اقتصاد ایران تحمیل می‌کند».
@
VahidHeadline
روزنامه وال‌استریت ژورنال به نقل از مقام‌های آمریکایی آگاه گزارش داد که ایالات متحده در چارچوب یک برنامه از پیش تعیین‌شده، ناو هواپیمابر «یواس‌اس جورج واشنگتن» را برای جایگزینی ناو «یواس‌اس آبراهام لینکلن» به خاورمیانه اعزام می‌کند.
ناو آبراهام لینکلن بیش از ۲۵۰ روز در ماموریت بوده و طولانی شدن استقرار آن و محدود بودن توقف‌های بندری، نگرانی‌هایی را در میان شماری از قانون‌گذاران درباره شرایط زندگی خدمه ایجاد کرده است.
در همین حال پیت هگست، وزیر دفاع آمریکا نیز گزارش‌ها در مورد شرایط بد در ناو هواپیمابر آبراهام لینکلن را «کاملاً تحریف شده» خواند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 321K · <a href="https://t.me/VahidOnline/77851" target="_blank">📅 19:26 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77850">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/LcBmZ_P9DF9FYH2JDDoXh-o12bxUTAjc_B6ED0fVBwiiDbJ_Y-khwOcKojBUZV1n_Ha8-gNAIs6tneo4p9eUJ6RM5DkCAfLSd51M6s39IitEeNsAYWeXYwPJlleO_YEHgaau6Zir1NScWA1ClGOKChdP5d377mXDGpmRktifxfgDtrCSA1XSlvNzcu81hO_eGQjrmvQF-N8BuzlqU4NraMH5lM167FVofrTIIJ6tEaaKx4ME66Qe79r8RGQlpF-VIwQ_TF7Fz07ZfDXYsKzdOJcQ1Dsg0TH-GkLcVSPTRouGo5i_jz_4Bfmi0Y47JTkUAZjRaZiZPAZW85TZRyz14Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محمد مخبر، مشاور مجتبی خامنه‌ای، روز پنجشنبه ۲۲ مردادماه در شبکه اجتماعی ایکس نوشت که «راهبرد قطعی رهبری» در صورت تحقق نیافتن شرایط ایران، تهاجمی شدن جنگ است و این راهبرد «معادلات قدرت را در جهان دگرگون می‌کند».
مشاور رهبر جمهوری اسلامی در ادامه ادعا کرد آمریکا در محافظت از متحدانش در خلیج فارس ناتوان بوده است. او اجرای «سازوکار اقتصادی-امنیتی هرمز» مستقل از تضمین نظامی واشینگتن را پایدارترین راه برای ایجاد نظم جدید در منطقه دانست.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 323K · <a href="https://t.me/VahidOnline/77850" target="_blank">📅 18:23 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77842">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromبنیاد عبدالرحمن برومند برای حقوق بشر در ایران</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/k_j43FIlmk6McD7GPdWhg4Q5fIeQEqdfePtjsta0dUwztje-3TfAuo7nluJlC48VXqivg3-xoNVSiTkd53mTbN_oLOimbcdb7XjY_W5356GBDoR3YjI1Y0T7fxCZSP_zBIbi8pyw-LTbjpfufMkOL_o93pxbpKA3xDaKDkc_fNWL6kslt93Kq3JG4eIddr7ObXEZEE6CJAkfyPwAH02k3xPjlBCw6-guJG05veibPl8TBU4-EiNuNM43ByN5FkQE9-0iFiPFjOBZyMrYzC7zQXxhuw8K_SJjiZdRSJ_xRDGAQogTOw-m4TH_dW4omrYlUp0HbgpXrL5tpg9FSYWZEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uhb09o4s3RWY4ecjQyYHed9WrUdE-mKDroBVVx78XJJGHNhDnw7Z29g2ePAmZ3GvUDyFQvJo4IPDtz7vuUTJoovowjto39y_dYWbHV7nLnjAY7fbYu-YJDfRhpmgWsEqRTkE_TguHZr23XYhGVmFtHxuh5KBrybf2kJxc1jGcgOLeve3nWHjMxWQKIWrk5m079bI-1H7_wK0GR8nHNyYR2hg8uGJHSuGpPB71Qg4LeIGPpFKfYsdJCBEjiGUn6yVFWKUq3HpJFw4foWLS2kz8k3MYqAKOTmvmKXJA-DRXTG04i5rE8aRX1tYyNTnKVRtMB1ptRNHxl4nDB2VocsjKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NsD0lgnTtVV8j8PP_Pdex12kAUPmFV7c2TyoNvNrumLVQiJFqTI02Hkuttm1J08VeYO61vUWb0olk6feE61efZYjsv19t0Q7J0wfPBIDMPVPzr4vbSofqbjP20FrsCGnEWpE9c_z3zRY2wBQNp5DoxsU3BK3TIC0q4hvTeNF2Ha7p4pEibCO0nDb037fhJpSC_JeYQTKVCxzmDHmGfAxNqeO4_KhUF3jPpnZ4Ld0je_hza8-esSwab1A5hhtT99XiOGphU3lJaLMvGo7QYnWVTXJaqR2sMgTfjq3nrVbb3STBREBNEg_btgaoxlG2brrEEzlOrVi8r8N7V-G86U5Og.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BcmtHOLqd7-cRo30RvQ-GL-QjjEqu09HJ5RLiPs_VEq-NmthDzPTFA-CesB9Gm4KVNxi2GnrkOCBoK9n5wYGiKcZ2t-zQlvjVpscgRKIk6HJU6C4fXDFQ9Xdeh9STKcLSC_wZDpQh3tod5_B2gXUBYTwjHuMr6hAqFfSSX73tRZ_ooaNPKaLNu8IOd_jOwe0wAbCms6FbEyUjtrIgO6AQJhsJgC12s1oepstynCMljd-zwVtJ5e9eDdO8PZZHhmTfd84910WsQtvB4YEjjlPPa7U4L5PKxxtJHRxmKbHPC0LthkUyleJzzXppGatXg1YQzkyWpRO_NK-tFqsMSldSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Mco9Q7AdWAYMKyAdDPjxA-L10OmWdnS-9kGJj4iP-gR3r-wwK3FrpZw1_Idedvayxeu7C3mug-KC9zjaJwweyrE9G3DnTbF0Cd0UCOo7EsIIJbVBqJVfcD353TlLPL2KSS9yOfcxnvPKGUD-zHthhwcoetoUl2q7Ggbne90L7BMbmeU4vSCsxBtrKwcmMWYk_OaYj5diVU5bkrp2A8ShQBos-rQYBIteFacAew0-226TreL_7G9Nkdjq_qa9hUUr_KkCEY5vpNrzWX4TfJNuNCRji017e3HD3eqNy5eN5VDaluqy6IWLvMyWKsP3Q2O2Uo_CupUymdI9mJsxz93TIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/V72EqF89PMwdPBUUXy6fzfokry3_HJ21DISoLk_igCSGyOGnF6oDCqGCxVuu9RrqUbMr7RxytYVtiLqQCAFpwlty1fMYWkHEpUViyU-bW9KDQXm9PaG-vcLzDpfsY_6BLUKvG_5b5Q_q9G_CZXZCSC6YUj5srwGnGgf6bS58BkgQxLKUawI1JvnsJGQlrdT8stfF-fo8N8e1VmzlqFXltVh4yeFCsCj7KaS_D6Gy1Vd1jtL1QDYShe5QEovAWoTR5awZSJWuMenhmDkS4LiMFctkYqAVFjGFBNau7GlKwonvBNZ4z-6kipifQbO3G4eMTAbz9ra6tbsJv-kDhH_Ovg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ErQMCY1j_6fC-PWpYIIJNme0ckNfkfQZhg0jD8RE_9XJiCRkvJkOrhcnTwDr64UlJWcwwEQ5bbTKPm9WWBzspvEyyrAtlaxH8A4ls3YNxqLoLmI9gAlnELq2IdmixqT75zQVNQNVnqnQUlDJOxjrbZwE7f3mdlRuL9jYcP4e81cQu0MX_tIFv9JC3-Eaw0Whkex4UgnLKIkjlg-82ahfPixEsLi44ZYYwBggFz9lI1LDCvAQOx2UAPM6xGdZuo5iPOL1KFJK2mD4SsGJlTgofMmNH7U5r8rl-CLVONY7uyzgi27lccsbnh4j-AjjXCK50X0wHUhdlJqS6FOeCqbyGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sJo47BEc_gdfhhXNe92dq4wJAJWUEPMrZR_nVIWGwz8nTUlRvfsU3udXE4aq2KtM8789iSpeJfxx_CZPk-2dln593jClukv2tDnnQyHTvvGGpUipAbqtaDli_PPyrTOewc1_z5slnlyV3TlZpTCzYywZJBAsTFnVj_zLfIRJ4mF-jtbAyqx8G9JzeE3BbnyvK1n_v_2hQxL8f7DnqGRoeR4SbCe5ic4himou3NNkTuoCpZ1rIIX64cZDZ9d3b788oPNaWfmqvb7xj8R817UkMJa0nTC0UqAKwOqR452PhmXiaXK_3RECVE3mamHZl2JKxET_y_uHS4-AYDp_LxETvQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔴
شلاق مجازاتی بی‌رحمانه، غیرانسانی و تحقیرآمیز است که طبق قوانین بین‌المللی به‌طور قاطع ممنوع شده است. با این حال، جمهوری اسلامی سال‌هاست از شلاق استفاده می‌کند؛ نه‌تنها برای جرایم عادی، بلکه به‌عنوان ابزاری قضایی برای سرکوب معترضان، زندانیان سیاسی، زنان، هنرمندان و مدافعان حقوق بشر؛ ابزاری که هدف آن نه‌فقط وارد کردن درد جسمانی، بلکه تحقیر، ساکت کردن و بازداشتن افراد از مخالفت و اعتراض در آینده است.
🔸
بنیاد برومند پس از اعتراضات «زن، زندگی، آزادی» دست‌کم ۱۷۳ مورد مجازات شلاق مرتبط با اعتراضات را ثبت کرده است و در پی اعتراضات دی ماه ۱۴۰۴ نیز در حال مستندسازی همین الگوست.
🔸
از آنجا که روند رسیدگی قضایی شفاف نیست و بسیاری از قربانیان و بازماندگان تمایلی به گزارش چنین مجازات عمیقاً تحقیرآمیزی ندارند، مستندسازی ابعاد واقعی استفاده دستگاه قضایی از شلاق همچنان دشوار است. با این حال، این کار برای آشکار کردن الگوهای سرکوب حکومت، حفظ شواهد برای پاسخ‌گو کردن عاملان و به چالش کشیدن استفاده جمهوری اسلامی از شکنجه، اهمیت حیاتی دارد.
@IranRights</div>
<div class="tg-footer">👁️ 366K · <a href="https://t.me/VahidOnline/77842" target="_blank">📅 18:23 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77841">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/PkGVnXWzzQcyRfyIlfV5FHFNfkxEBFWwa7Vimv7rQPMJ5AGOdfDbllFMN4kR9cf3lFULhjEaKxWeOOJMjGrriHiZ7CePDOeFEW07gokUgpgs9MLLvKqpmQhcPPa4o5Qo7RudtgL8UItQtEKuukIt2ZJkdQyspxWD0Gqt_LwFlWOMS4iYkAEtlvxJhHH3PgQpeWVN4d344D7-PQcYnJqzfQt4PbAsdM9xwH_ZSJfdWCc1y09_uQ5w7AaJMB-M7SVGXtDLxCZ7Q493U5Dti8VZtkfr1D7jZJwUxTM0lPP8Kur_vFbCo4oGhQjy0yR4TBNHL0ROeovFhqg7q1RPUjysjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری صدا و سیما:
«توقف اجرای طرح عرضه بنزین با نرخ پالایشگاهی در کرمان»
مدیر شرکت پخش فراورده های نفتی کرمان:
🔹
پیرو مذاکرات امشب استاندار کرمان با مقامات کشوری و نیاز به بررسی بیشتر در خصوص طرح مدیریت مصرف سوخت و مقابله با قاچاق، عرضه بنزین با نرخ آزاد پالایشگاهی در استان کرمان متوقف شد.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 426K · <a href="https://t.me/VahidOnline/77841" target="_blank">📅 00:56 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77840">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ax9g22K2mV5Uuoq-AWN0DBqFeuKhy3lc7e8MRuZQ032PN8KrV3N4x4d10NORA14-a_XcQYGBshcajeiMzD9qiDpEel0t1ivvPKbmDAjcFsHRr8YCdjaHKpLsJZPUrPdB4f359NCEhYYkvnGXOv80k0x6BP7MbFv7SLiO7NPk7EX2Pz2jQC1nylcRKTQwPTUmv3ZJvAsI097bnyL10TREPFcb9u2t7zMeUMy9d1MMmZKgbcjBZLLboUKNA5mu2-W-akAnpEby7IzO9Wo-KMM00ivaMX5m-yfx83Cof3ERGMTLCmoFqnlSRVJulgrlkPgkeac3a742Mqti84Aze8T-zw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">معاون هماهنگی امور عمرانی استاندار کرمان از آغاز عرضه بنزین با نرخ تمام‌شده پالایشگاهی، هر لیتر ۸۷ هزار و ۲۰۰ تومان، در ۲۰۴ جایگاه سوخت این استان خبر داد.
به گزارش ایسنا، علی‌اصغر ذاکری‌هرندی اعلام کرد که عرضه بنزین بدون یارانه از ساعت ۲۴ چهارشنبه ۲۱ مرداد، بامداد پنجشنبه، در جایگاه‌های سوخت استان کرمان آغاز می‌شود.
@
VahidHeadline
🔄
آپدیت:
متوقف شد
.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 403K · <a href="https://t.me/VahidOnline/77840" target="_blank">📅 23:53 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77838">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/sYZnx26VF7Uyry7XvXbXzwod1r92s8XlURskh5eSjQlKrfjF0P1DHXIIKqrEHjloURAqrJ1H6r8PcQyeOtKyrH0086LvdmtLLZnnopnvZVgeaQi4HEf12nFvJJtHpASrRk-iZA5huenHpf9oFr5UqjUgiwQX7GiyTLVIJeOeF1wowxMm4tt8QiX0CuxXcqPRHR_l2VAYskVWj9W8YhK0R3Cyv20Qf_mZiH6J5bNC4p8bI2G80O0gY13qChbUSFQHDvDuRMN7CM3usSBakQnWYMmZqq_IfX6nDLsKmzJUH8CF3UeEKJXKkBprU3cXsNBudzAmV3JZmiIZGAYe-CFtoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/RMsL7c_85nokDIeiCPXH83CwxxjqDINoYP-aQ6UVLXUeOubfoA_1qLapMAXrnsNjfG8K6tUFVANf25TJ8AG92JW4HFy3ysldZsjKi20HPGis1Bvrdai7r5aAdTz-DKL1GSgghpN9WOkuDXeyJdYEDa45vNf8KLLhPIfmsLLYH9er7eWGrN6Wuq1sQFdIzuuzlUuVIuSGssro7CVs-JMxcZdQyv--aj1CoTJ5hrG8_nEpuGMBl7Xrf1nnDQhdczjny9VntaEnVCCB6Xm_hHXh3LbocO7Lcw0Ku6uJBTiQ8VP_tk1sfx3uQHBtQ9lfGUNzEOf26xHCr6t7oRllCV9NDQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">اتحادیه اروپا و شماری از کشورها، از جمله کانادا، بریتانیا و استرالیا در بیانیه‌ای مشترک، با شدیدترین لحن ادامه اعدام معترضان در ایران و سرکوب افرادی را که برای عدالت و کرامت انسانی اعتراض کرده‌اند، محکوم کرده و خواستار توقف فوری اعدام‌ها و آزادی تمامی بازداشت‌شدگان اعتراضات شدند.
در این بیانیه که روز چهارشنبه ۲۱ مرداد منتشر شد، آمده است که استفاده از مجازات اعدام برای خاموش کردن مخالفان، ایجاد ترس در جوامع و مجازات افرادی که از حقوق بنیادین خود استفاده می‌کنند، به هیچ‌وجه قابل توجیه نیست.
کشورهای امضا کننده تاکید کردند مردم ایران باید بتوانند بدون ترس از آزادی بیان و آزادی تجمع مسالمت‌آمیز خود استفاده کنند و از جمهوری اسلامی خواستند فورا به استفاده از مجازات اعدام پایان دهد و تمامی افرادی را که به‌صورت خودسرانه بازداشت شده‌اند آزاد کند.
فرانسه، کانادا، آلبانی، آلمان، استرالیا، اتریش، بلژیک، قبرس، دانمارک، اسپانیا، استونی، فنلاند، ایسلند، لتونی، لیتوانی، مقدونیه شمالی، مونته‌نگرو، نیوزیلند، هلند، پرتغال، جمهوری چک، رومانی، اسلواکی، اسلوونی، سوید و بریتانیا از جمله امضاکنندگان این بیانیه هستند. نماینده عالی اتحادیه اروپا نیز به این بیانیه پیوسته است.
در ادامه بیانیه آمده است: «مردم ایران باید آزاد باشند تا حقوق خود برای آزادی بیان و آزادی تجمع مسالمت‌آمیز را بدون ترس اعمال کنند.»
کشورهای امضاکننده همچنین از جمهوری اسلامی خواستند صدای مردم ایران را که خواهان تغییر هستند بشنود و برای تضمین رعایت حقوق بشر، اقدامات عملی انجام دهد.
ژان نوئل بارو، وزیر خارجه فرانسه، نیز با انتشار این بیانیه در شبکه اجتماعی ایکس نوشت که هفت ماه پس از «جنایت‌های گسترده» علیه مردم ایران که برای عدالت و کرامت انسانی به خیابان‌ها آمده بودند، حکومت ایران با افزایش اعدام‌ها به «ریختن خون» مردم ادامه می‌دهد.
بارو این سرکوب را «غیرقابل‌تحمل و غیرانسانی» خواند و خواستار پاسخگو شدن عاملان آن و آزادی زندانیان سیاسی شد. او همچنین تاکید کرد مردم ایران باید بتوانند آزادانه آینده خود را تعیین کنند و حقوق بنیادین آنان محترم شمرده شود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 404K · <a href="https://t.me/VahidOnline/77838" target="_blank">📅 20:20 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77837">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/vexpmGWbjreWS13HTSL0LWfP4fVYY_R7IE29hkJH-MbvBiQxCzVLvsT451wEx8bhwhfabk-ZaC61qoXmupTPJvfwUrPlBqh6uvPFKHcazyWsacl8IF784km-4wkTrEJu9RIIbXifMGp5987WdjFaMTy8jJajupnM8aJutNYlH3QOPD0oGxzIwSx3Jj9hHlcG8scsK5JQIi8Muy4OE6BE5pwGXx3YTT_CQxEWcovEZeV9AQJ0ah_Wt8LRXp4h2g_xurULVnLNWtWUEzF4J3B7uXmCBfPCeOMZkpPP1hexLC4xsXR-4VndCn16UElD6rYCnYvY3JIyod4lY2x-11iSqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست ترامپ، ترجمه ماشین:
ایالات متحده آمریکا کنترل کامل تنگه هرمز را در دست دارد. فکر می‌کنم آن را حفظ خواهیم کرد!
محاصره دریایی ما را همه «دیوار فولادین» می‌نامند و ایران هیچ کاری نمی‌تواند در برابر آن انجام دهد. آنها نیروی دریایی ندارند، نیروی هوایی ندارند، سربازان باقی‌مانده‌شان حقوق نگرفته‌اند، سپاه پاسداران به‌شدت تضعیف شده و در حال فرار است، و «رهبری» آنها، در بهترین حالت، نامطمئن است!
آنها هیچ پولی ندارند — کشورشان «از پا درآمده» است. تنها چیزی که دارند اخبار جعلی و تورم ۳۰۰ درصدی است، که دارد بدتر هم می‌شود!
ایران فقط حرف می‌زند و هیچ اقدامی نمی‌کند؛ دیگر قلدر خاورمیانه نیست. الحمدالله!
رئیس‌جمهور دونالد جی. ترامپ
The U.S.A. has total control over the Strait of Hormuz. I THINK WE WILL KEEP IT! Our Naval Blockade is being called, by everyone, “A WALL OF STEEL,” and there is nothing Iran can do about it. They have no Navy, they have no Air Force, their remaining soldiers are unpaid, the IRGC is decimated and fleeing, and their “Leadership” is uncertain, at best! They have No Money - Their country is “shot.” All they have is FAKE NEWS and 300% INFLATION, and getting worse! Iran is all talk and no action, the Bully of the Middle East No Longer. Praise be to Allah! President DONALD J. TRUMP
realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 364K · <a href="https://t.me/VahidOnline/77837" target="_blank">📅 18:25 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77836">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/56807a2a8f.mp4?token=e5_3nlJ9hPP4zLboOqIj0wVKu9smN21f5FXWUCHu1REzi10r3G0FAPxlaXuz8l67_jF-Mk4QCABr0lSiT4gwd4eRQU3Fmpfwwt_4XCvXllXWkSMyz1NlAtBfXnmRZVBz2grHUNcradU6YsQb9tFeHMOiFcdNvmaQ3IQIX98cplFJnoBr8XScjt7AtR_wdTa02Azh_FKOG2rgS53eRhyxcZjcRyFttQZ08pk25C2kl8kx1mDJYOkgXfppgC5lg-O0UCpaBBFDuS4yLgy_8KeWjLMMdj8Nf-v_CoF0QFHhbUC2gek8dj9ssy4Xoq8QkH91YzAyz5dRwd_S4uAB6Djos1atzC0lfHnijaZaIF-FEa_Yr0ffbvnywIyIOQvm-DdUaTVGUwDlOzdexeb3XeAYe0rqjf-j7gp8N7BNasRNQuDGQgpj29PAQlatcMFUIdDOlg0UxWV0POv3qPGdAK4oseCxHcYrfC6kWlLKpDXklIN_AoUO3MfbjQGy_URfJ8v3mPFE1N26J8TFL7vQT0VhIRzn4FCZTwAeJP7ncVgBHO-2w3PFStmYUkwzzXqKO8GLu8u1kq1ArUUQpBY3hsK_AtSNiUPhjHngS16OrCDd_9bYdmtMCXb4-9_P59XEXj9nwn57SfLqBqqlclEtPFpUyv93qDLFdvH2KDUaCuxN_Nw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/56807a2a8f.mp4?token=e5_3nlJ9hPP4zLboOqIj0wVKu9smN21f5FXWUCHu1REzi10r3G0FAPxlaXuz8l67_jF-Mk4QCABr0lSiT4gwd4eRQU3Fmpfwwt_4XCvXllXWkSMyz1NlAtBfXnmRZVBz2grHUNcradU6YsQb9tFeHMOiFcdNvmaQ3IQIX98cplFJnoBr8XScjt7AtR_wdTa02Azh_FKOG2rgS53eRhyxcZjcRyFttQZ08pk25C2kl8kx1mDJYOkgXfppgC5lg-O0UCpaBBFDuS4yLgy_8KeWjLMMdj8Nf-v_CoF0QFHhbUC2gek8dj9ssy4Xoq8QkH91YzAyz5dRwd_S4uAB6Djos1atzC0lfHnijaZaIF-FEa_Yr0ffbvnywIyIOQvm-DdUaTVGUwDlOzdexeb3XeAYe0rqjf-j7gp8N7BNasRNQuDGQgpj29PAQlatcMFUIdDOlg0UxWV0POv3qPGdAK4oseCxHcYrfC6kWlLKpDXklIN_AoUO3MfbjQGy_URfJ8v3mPFE1N26J8TFL7vQT0VhIRzn4FCZTwAeJP7ncVgBHO-2w3PFStmYUkwzzXqKO8GLu8u1kq1ArUUQpBY3hsK_AtSNiUPhjHngS16OrCDd_9bYdmtMCXb4-9_P59XEXj9nwn57SfLqBqqlclEtPFpUyv93qDLFdvH2KDUaCuxN_Nw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ایرج درگذشت؛‌ جناب سرهنگی که «پهلوان آواز» ایران بود
حسین خواجه‌امیری، خواننده نامدار موسیقی ایرانی که با نام هنری ایرج شناخته می‌شد، امروز چهارشنبه ۲۱ مرداد ماه در ۹۴ سالگی درگذشت.
درگذشت او موجی از خاطرات دوران طلایی موسیقی و سینمای قبل از انقلاب اسلامی ۱۳۵۷ را زنده کرده است، به ویژه در نزد شنوندگان برنامه‌های رادیویی و یا انبوه تماشاگرانی که آواز برخاسته از سینه ایرج را از لبان ستارگان فیلم‌های آن موقع می‌دیدند و می‌شنیدند.
افسرآوازخوانی که حسن کسایی، اسطوره نی را واداشت «پهلوان آواز» خطابش کند و صدایش برای محمدرضا شجریان، خسرو آواز ایران، «متر و معیار سنجش کیفیت صدا در تاریخ آوازخوانی ما» باشد.
ادامه مطلب
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 365K · <a href="https://t.me/VahidOnline/77836" target="_blank">📅 16:50 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77835">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ggNMHzsv6gExGNui99USZ4sJRGDUu_PFg3MHPEqD6Zyx0T86KKcoSONMvbOQVnFGEfsQd6a7QjeFko3DzNpl9exyx7E0-W3CJP9obGL7fmXv3CY9oqqhG_3UAIbMiPlAq-G3sw99ALUmFAKwFCcKwFU9ifKjG4bCMXn2D-qu3bwmML3SDLoQaF3k69wjnlX24G0m8YgXKQUw8Oq0pFFamU3E1iXgWUUFEpHPQv8enE0T9mxnoa6D1HrYM5ZLFTqtkIw9pFWv4wUa2hGei8Kx-UdBjSxSu4_oObT3ymmlF8BMnfR0cVFo1Pp8x-Oq9A4WNe_ZtjCO_FUwfZNmQjimWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر بهداشت جمهوری اسلامی می‌گوید هند در واکنش به انسداد تنگه هرمز توسط جمهوری اسلامی، حتی در طول جنگ یک کشتی مواد اولیه تولید دارو نیز به ایران ارسال نکرد.
محمدرضا ظفرقندی در ادامه تصریح کرد هند ارسال مواد دارویی به ایران را مشروط به عبور کشتی‌های مرتبط با هند از تنگه هرمز کرده بود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 314K · <a href="https://t.me/VahidOnline/77835" target="_blank">📅 16:41 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77834">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Cq18nXFlGTnGuzJ2EQyrWQ9V4UlJGBNsWpSvTRqPcF6jCYKog13nojrhgaoX_9M5jp5RukGQX11Am6bCJisSUyAOEp1fu63wgPFPTl6WqlwtKb3cA6Cb-ySjFA2TEflWZjdV1nlv1ixm5wobqkijGW-0aUUhCrisz0BBxftKoPkISaC_PURSWMHGtX61O7U5rOMaiszk6d0LHbrIcl_2XuNTfg1d9kG-kKQ2vmrhxBREN0D1a66wMXt9YGkoYtrfFU2xfl9cymMX5erXyc6nAhKqlTrru1img-x30z8St8FAboq5pgwKsa9x88UCl35cXsiN9LK_qafY6iv8gA5nJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک هواپیمای مسافربری پهن‌پیکر چینی، قرار است روز چهارشنبه ۲۱ مرداد اولین پرواز تجاری بین‌المللی خود را انجام دهد.
این جت جدید که به عنوان پاسخ چین به هواپیماهای مسافربری بزرگ بوئینگ یا ایرباس معرفی شده است، کوماک سی‌ - ۹۱۹ نام دارد.
این هواپیما اولین تلاش چین برای ورود به این صنعت پرسود است که تاکنون تحت سلطه غول‌های هوانوردی غرب بوده است.
پرواز هواپیمایی چین، ایر چاینا، صبح چهارشنبه پکن را به مقصد اولان‌باتور، پایتخت مغولستان، ترک خواهد کرد.
این پرواز رفت و برگشت به صورت روزانه انجام خواهد شد.
برخی تحلیلگران معتقدند که ممکن است سال‌ها طول بکشد تا جت‌های چینی به رقیب جدی شرکت‌های شناخته‌شده‌ای نظیر ایرباس و بوئینگ تبدیل شوند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 298K · <a href="https://t.me/VahidOnline/77834" target="_blank">📅 16:39 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77828">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/o0LBK9u4PDou9foL-HteXQ_GHvZqy6cAr4OOfOUm_nBV3FzCS3_3OT24-yoIfby0BJwpx0Ion30EyTgwh667RqWax5yKQOQpYxjr7MpJF4cAFtDeU-C6xwaX3TtZySGEfriQ1t0uT3m05Zez_Oejvs5veY47CfEPVoK9Q3BLiUSwihPyM4_sTF-IXdMePMzU4G1i342yqOJ4Gf8FayQECkovrQduJi0S9Lu1tO2bPPl1Ep5TZ2TXzcwScO3gGDPedRRIZxZb11v3GwO8uQl-XEHDdQYJzPnR6cIirm9UWXiPBFIeme-JNKEIeJAIQbIHEytz5ZUvAqPYZnmPNKpRDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Jfq5MyqrBDgmmRj4Ay15sdJsFlfzVuyvZFGM0AG7dNI_80Rs-VREBa0V0O8uB4CEKPKOgfHm8F3P_3ZMqBYV7jXDwd01j2OHhYqAuDJWi7Wu5wqI6gUXDwu3NlkC5v2XO-fa1NWJaTv6aLanGb1GxCUHcCVEipieP10uYDk8J3sgmFIiW__9urjX2ZArcf4aDIaEx6xTX6Ny4VvL0QfL8q94BrKK0KN98Mu4UKrLetY3PH0vKXCg_1dwSg9JjwlBg9_AMKQtFMlGVPD4PIEoAm2dYm3wx89yjcfYTanktQ9NX2UBPwIMWsh9m6ql0F2M5oOCXgdKmW5-PycL7EVdrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/QlubsDeQO7bu7MUHzNN4iCgIDfr8cl7DK_96N8u68TPET9g1B8jOsn2e_fH6Edeoaq91a_4HrUXvCKW0y3khR4x4eYt68KCLI2imPBOQmaETxGXfSsdzjI_3H9Lg06NSW_OurWbihjlhqQGFpkDPHZ97BeB1CGpDp69hq9Ow-9N876Z6KRPwZx_VCT17aboqJ9XnxAb2bE7itwD9Bf3YXcbO-Rta6dSsYFYtCUZpeO6_p5ixcMTSGdoBowifsQoCPopz5SG5OCKl6bh3Cm9x-IJKOZwu3GNF8JjK0UV2IhA8xc3QkmIs7VSnOVmiM9sdQeo1hntR5RgHx2nqCy2t9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/MT9XrZoXMI3bJrn6h5EkJkZmg7A-COBiF9UDWAyHm0EZk0UUF9KxNA1XqJeNulUDqxgU3BDI4rSkKQrW7_1DVgbArbBoY4T2uZyjt_duwXXpHtEfqjmTDUo_siwKNFsPCaApKabCnmb07MYYlxk06y3-qjwdkf85DxARJY7VSWFrxiuQnw5uZkqhgxDDN8Wu-gui-nNbZN1pgVdOiQALoE4TIWLmgj_L-0OsS5UNKBfXPOK04QMggo4H4LuCps40ny8un8ZBMDVd2ldzLuAQqkPJAcPGWc9TCKJaPVPmPfodjqf-yFXaQ5J73qEnjZ11dH_tbW7ZZG67PMWIOcoBag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/NyutHFdRAXrj_C5QMZE2SMlvS2Fw-8O1c7Dulwlz6p6qjy4MgmqJw6r_sMI4DKk3Nnh_wfDDQbCFWth53Z1NS_U4FUUHa2BCOTGsGrU-wR5TF3PwHy-9i1Pep7Ase6KhimfUwZx4dro5u7u_QBAsgEP2ie4oaPHB-onT1dINQUHpGKDCFcAkLwRhFPSus15l-l-oJiyvAcNl85qXbRitUFvf3IoGLGhBaqfyXLHzsO1YCFSjQLvfNkZW6c-u3TOIK-yz3A4jb8N1AP9dn7rWs7SsVqhxpDyZsYZlfMv55gd-6gBlsCOuLC_jrW_7Q35_wszUYA4Gg3eIf_qsoenDxg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/8a19a9b2a0.mp4?token=YDL5jU8DBWdM_TgZ-o_hfh8fKNn4LNFDG15Fj1UQmjJtKEZxAa0gFunNLCe5oJPKr6vGslVve1j15BP31NL77G_Xmb0A4oRakUJVv9ZjsaKt-4C5mMe2I79XqenRhMQWnEB5xTJ4WGce6cGJptaeI-3RCSSmsqEJRa4Q3HkHMq0UjYyktRpYPNPZAQkPZAFFJJheW2Aq0zsmNo0PPUUnIi23mVDEmCrypD7hrXtAm6VTQZLiX0sJpAbyjqM8HV7IjIkvkvalQ_qsiSx0HVZJ0GJk6lBcyHh6kXrmlVDuDSsISgD2JoB58ESIT83_PSgQGrSApJuoHTTY702dnM9oTg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/8a19a9b2a0.mp4?token=YDL5jU8DBWdM_TgZ-o_hfh8fKNn4LNFDG15Fj1UQmjJtKEZxAa0gFunNLCe5oJPKr6vGslVve1j15BP31NL77G_Xmb0A4oRakUJVv9ZjsaKt-4C5mMe2I79XqenRhMQWnEB5xTJ4WGce6cGJptaeI-3RCSSmsqEJRa4Q3HkHMq0UjYyktRpYPNPZAQkPZAFFJJheW2Aq0zsmNo0PPUUnIi23mVDEmCrypD7hrXtAm6VTQZLiX0sJpAbyjqM8HV7IjIkvkvalQ_qsiSx0HVZJ0GJk6lBcyHh6kXrmlVDuDSsISgD2JoB58ESIT83_PSgQGrSApJuoHTTY702dnM9oTg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آلودگی نفتی مشاهده‌شده در سواحل جنوبی جزیره قشم به محدوده جنگل‌های حرای روستای «نقاشه» گسترش یافته است.
خبرگزاری ایرنا روز چهارشنبه ۲۱ مرداد گزارش داد بخشی از لکه‌های نفتی وارد محدوده این جنگل‌ها شده و عملیات پایش و پاک‌سازی با هدف جلوگیری از گسترش بیشتر آلودگی آغاز شده است.
به‌رغم گذشت دو روز از گزارش شدن این آلودگی، رئیس اداره منابع طبیعی و آبخیزداری جزیره قشم اعلام منشأ دقیق ورود لکه‌های نفتی را به «بررسی‌های کارشناسی و جمع‌بندی گزارش دستگاه‌های مسئول» موکول کرد.
جنگل‌های حرا از زیست‌بوم‌های حساس ساحلی قشم به شمار می‌روند و نقش مهمی در حفظ تنوع زیستی، پایداری سواحل و زیست و تکثیر گونه‌های مختلف آبزی و پرندگان دارند.
سواحل هرمزگان در بهار امسال نیز با آلودگی گستردهٔ نفتی روبه‌رو شده بود. مدیرکل حفاظت محیط زیست هرمزگان در ۱۲ اردیبهشت اعلام کرده بود آلودگی آن زمان در پی حمله به پالایشگاه نفت لاوان ایجاد شده و مواد نفتی به نقاط مختلف سواحل استان، از جمله قشم، لارک، هنگام و هرمز رسیده بود.
@
VahidHeadline
در عملیات پاکسازی نفت از سواحل قشم، از پدهای جاذب برای جمع‌آوری لکه‌های نفتی استفاده می‌شود.
این پدها معمولاً از الیاف مصنوعی مانند پلی‌پروپیلن ساخته می‌شوند و نفت و روغن را جذب می‌کنند، در حالی که آب کمتری به خود می‌گیرند.
پدهای جاذب می‌توانند با جمع‌آوری سریع نفت، از گسترش لکه روی آب و رسیدن آلودگی به ماهی‌ها، لاک‌پشت‌ها، پرندگان دریایی و مرجان‌ها جلوگیری کنند و آسیب به سواحل و اسکله‌ها را کاهش دهند.
با این حال، پدهای جاذب به‌تنهایی برای مقابله با نشت‌های گسترده نفت کافی نیستند و معمولاً در کنار بوم‌های مهار نفت، اسکیمرها، تجهیزات مکش و دیگر روش‌های تخصصی پاکسازی به کار می‌روند.
پدهای اشباع‌شده نیز باید به شکل مناسب جمع‌آوری و دفع شوند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 276K · <a href="https://t.me/VahidOnline/77828" target="_blank">📅 16:38 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77827">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromبنیاد عبدالرحمن برومند برای حقوق بشر در ایران</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tEM41freFUr8LvP_iNOFJV6xSKYEApQu33ANsufOZomfd9gB4ppi9woagyJBMSsWSiVvjrrg2jRUqIQGIBUy3G5zPKNILtbTWa8RAXAxLXdbCAFBkC3niErakpmuAjVZiHFvkwKHAQvTxJ032guSDCkF1VDTqMWx1HC-xjBYaleuuR4CBKp5-PfIov6TNi5cft_67GihipTmkFBFf-ko7uHQbyrj828AuBIamzZd2mu49PfgxI_4wuhUbfFKopei-PnXgumU1MWU8u3LV80UabdPlV5c9M4erGZxGvCRv7kLn_Tn2vo4I_i6EOh8LL8dEiXvgufSiQcchd2myAR-XQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
جمهوری اسلامی ایران از ابتدای سال ۲۰۲۶ تاکنون دست‌کم ۹۱۶ حکم اعدام را به اجرا درآورده که از این تعداد، ۱۵ مورد در ماه اوت رخ داده است. شمار واقعی اعدام‌ها احتمالاً به‌مراتب بیشتر است؛ چرا که حکومت ایران برای جلوگیری از افشاگری، نظارت بین‌المللی و واکنش افکار عمومی، آمار واقعی اجرای اعدام‌ها را پنهان می‌کند.
🔸
هم‌اکنون شمار زیادی از معترضان با اتهامات سنگین و خطر جدی اجرای حکم اعدام مواجه هستند. روند صدور این احکام بسیار شتاب‌زده، ناعادلانه و بدون رعایت آیین دادرسی منصفانه بوده است.
🔸
جمهوری اسلامی از صدور و اجرای احکام اعدام به‌عنوان ابزاری برای ارعاب جامعه و پیشگیری از شکل‌گیری اعتراضات جدید استفاده می‌کند.
#نه_به_اعدام
@IranRights</div>
<div class="tg-footer">👁️ 305K · <a href="https://t.me/VahidOnline/77827" target="_blank">📅 16:38 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77825">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/jssImyU6LwG_USpzopmlgGmNYCl4H5b1N_JoeElgIQFGQ-GN_OeyMVP8mGx5TJ1_koZDIEh_V_XKS-4Uq8tO7RBjHTVeV8MpdkVUn8snITjGWJXBBamV3LjL6InsWk4tOH89Gcy_v-EngmG380-NRA9gNz9L6jQTSyWuPmg-X1cL0K5GrovleSTWl-JWkLu7Ns5wfQjf3jTnD1mtXyAWGI9Bc2p2w9Ejq8CtptT_jJORrqqlDMRAjkoX-y5UziJxo4jmhJOZ0vp0Rl-jMYSghbeYEdJLNd_-4ATfdZtIRHaQ_703JYfXNWubmiuQSFuQIfbCka0LaIeB4fqvUe1kQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/HZFWeQmU07Mo4d0_LE1VqFZHKYIykp9-NxrPmo5Hijlnvvtfhe4xW5Ze--3xaWyBcBLR3iuieqBbeWSqEC6LJcVnsQVuftSY95S8rrBh20plzhNnFATdK8dw0-ZbWRlnuHEJF4fRao0K4GZhgLlRD7VrZdw227bIUODsnfM7opZbrCiLknG0qQ840x-ZjqmdXq0hizluEKcgh7kvQ-126mWEIjiCRlW5Z-VF24Tdi4RGo6TnUwp8EY3uViY8KXGrBWWKz5QLVBn5ji6nCyvMgd8Pb1YVIABoGnIih4yJ-9eOVpsu8_r1svLWr7retbgngiZpC3upSwp2j-knnisTWg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">اظهارات علنی متناقض؛ ترامپ در پی تهدید ایران، مخفیانه با پروازی دیگر از ترکیه خارج شد  ترجمه ماشین: واشنگتن‌پست دریافته است که تهدید ایران به ترور دونالد ترامپ، رئیس‌جمهور آمریکا، ماه گذشته باعث اجرای عملیاتی فوق‌العاده شد که طی آن ترامپ به‌طور مخفیانه با…</div>
<div class="tg-footer">👁️ 360K · <a href="https://t.me/VahidOnline/77825" target="_blank">📅 08:02 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77824">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/49def3f074.mp4?token=rGAEPGdmQSJjjyt-04vP_YeTZgO5NLtWDo7L0zeJhdkfsUWnV-BeenbgSq8feEI6aj3O7yZKBeYquayKSvuqcZVTVV44vDxulsSdpkbj2YZvhEhgkF09ImGbu_C5hYW3HWd3on3vRD_cz3OODx4WtETM_bq4IGpbiixdzqEafoSa04W4Lu18uodlu2BejkV02cqS6rbBdX9KN36oyUcsA-ub2pvXQAJ07MQLaQ798Akaa6F3Zkc6VO7zXVjGrQyw6hJcUCV--JsYqwzJPY3rNIGF9_WoKnWMVgF8_zMhlBFcGm9jkVT1H-DhQpcAGYlVZ64STF0-unydzoegQko0zg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/49def3f074.mp4?token=rGAEPGdmQSJjjyt-04vP_YeTZgO5NLtWDo7L0zeJhdkfsUWnV-BeenbgSq8feEI6aj3O7yZKBeYquayKSvuqcZVTVV44vDxulsSdpkbj2YZvhEhgkF09ImGbu_C5hYW3HWd3on3vRD_cz3OODx4WtETM_bq4IGpbiixdzqEafoSa04W4Lu18uodlu2BejkV02cqS6rbBdX9KN36oyUcsA-ub2pvXQAJ07MQLaQ798Akaa6F3Zkc6VO7zXVjGrQyw6hJcUCV--JsYqwzJPY3rNIGF9_WoKnWMVgF8_zMhlBFcGm9jkVT1H-DhQpcAGYlVZ64STF0-unydzoegQko0zg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دونالد ترامپ، رئیس‌جمهوری ایالات متحده، در گفتگو با خبرنگاران گفت به ایران اعتماد ندارد و افزود: «من آخرین کسی هستم که به ایران اعتماد می‌کند. آنها پیوسته به من دروغ گفته‌اند.»
ترامپ همچنین گفت ایالات متحده در حال حاضر «کنترل کامل» تنگه هرمز را در اختیار دارد و افزود: «آنها کنترلی ندارند. ما کنترل کامل داریم. اختیار آن دست ماست.» رئیس‌جمهوری آمریکا در ادامه گفت ایران دیگر «قلدر خاورمیانه» نیست
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 357K · <a href="https://t.me/VahidOnline/77824" target="_blank">📅 07:57 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77823">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/3e9b0ac932.mp4?token=ENG_LPfOSPoKQ9BGqVgLnrOnjFFep8VferenjZf7wZbMN1S9pEDbmH89oi_Npf75N6I48dc1wZJwW1l0_qAbm56gjd0oydEWQWT6iMSYCdl4KndDZj-PqPnK3VAf_bHy2T1Gx9bbDaXaBXIa77jXH_yx31o-O2OOaWJE9SFRw0h2a8Wz0p4eWX_wxIdQ0EAf7wFeHHxtDt2Zaa-zfwVLVZstEd5PO4nqYGwWm9Z3Nip9HH2opyCKuNQO-oHE9acyhHChkt_TNqkf7Nee1QCclKIptge12aV0RKpX3gL0HAKrjB1b8iZH_ocAgZhHdm0I_0Yrg4OKw-rTm2dNpYqA-w" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/3e9b0ac932.mp4?token=ENG_LPfOSPoKQ9BGqVgLnrOnjFFep8VferenjZf7wZbMN1S9pEDbmH89oi_Npf75N6I48dc1wZJwW1l0_qAbm56gjd0oydEWQWT6iMSYCdl4KndDZj-PqPnK3VAf_bHy2T1Gx9bbDaXaBXIa77jXH_yx31o-O2OOaWJE9SFRw0h2a8Wz0p4eWX_wxIdQ0EAf7wFeHHxtDt2Zaa-zfwVLVZstEd5PO4nqYGwWm9Z3Nip9HH2opyCKuNQO-oHE9acyhHChkt_TNqkf7Nee1QCclKIptge12aV0RKpX3gL0HAKrjB1b8iZH_ocAgZhHdm0I_0Yrg4OKw-rTm2dNpYqA-w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرگزاری‌های ایران تصاویری از «آلودگی نفتی» در بخش‌هایی از سواحل قشم منتشر کرده‌اند.
به گزارش این منابع دادستان قشم دستور شناسایی منشا آلودگی، مهار، جمع‌آوری و پاکسازی نوار ساحلی را صادر کرده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 380K · <a href="https://t.me/VahidOnline/77823" target="_blank">📅 21:15 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77822">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SoI7VN0u5BMoFhphdphVPZt9YtXXhwqhHTGIDYdLoweCYVN3IMiqeENef3DvuYsK5ZQojE0G_GcjQgHWE2dtQbGPqZWL3VnF6jODnlmzht8bHvaHQefrzY8WVk6CaI4yQnhZEs9eF2M5jbnbeRNi2iGY35_pULx7jR0tZEBFyoS5DZDpWGa7xRnICJda_G_FfbLCozx8iuPlDLFaTRN-Oq4J1xPaoCsQ8sMg8n1z1l1M9n0EtWqhXDGunOQJTyQBvYZLEkVL3OTA9o0HyXT9xbGmKraH7ePAGaSfR8opKyGEU_ax9TL1GSz4hFI2swQ-GKGFMNbY-883XagU1_SSMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محسن رضایی، دبیر جدید شورای عالی امنیت ملی جمهوری اسلامی، در نخستین موضع‌گیری پس از انتصاب به این سمت اعلام کرد برای باز شدن تنگه هرمز، آمریکا باید جنگ را پایان دهد و پول‌های مسدود شده ایران را بپردازد.
به گزارش رسانه‌های ایران، او در دیدار با سفیر چین در تهران گفت تا زمانی که آمریکا «رفتار خود را تغییر ندهد و شروط ایران را نپذیرد» ایران اقدام به باز کردن تنگه هرمز نخواهد کرد. او پایان جنگ و آزاد کردن پول‌های مسدود شده ایران را دو عنوان از شرط‌های ایران برشمرد.
این در حالی است که دونالد ترامپ، رئیس‌جمهور آمریکا، روز دوشنبه در کاخ سفید به خبرنگاران گفت ایالات متحده کل تنگه هرمز را «مین‌روبی» کرده و کنترل کامل آن را در دست دارد.
محمدباقر ذوالقدر، دبیر سابق شورای عالی امنیت ملی، که رضایی جایگزین او شده است، هفته گذشته شروط مشابهی مطرح کرده بود.
محسن رضایی درباره مذاکرات جمهوری اسلامی با سلطنت عمان درباره عبور و مرور در تنگه هرمز که طی هفته‌های اخیر در جریان است، نیز گفت اگر بین دو کشور توافقی در این زمینه حاصل شود، «این توافق موضوعی جدا از انسداد تنگه هرمز خواهد بود».
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 353K · <a href="https://t.me/VahidOnline/77822" target="_blank">📅 20:14 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77821">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/GOhkf6hZNK6isfgKUAQqKlLeor5FrXtWUp32g4eIOJ35RuVQYdOi2l9vj0jF6acSe9b-ghGwHBQFGrOxQPjsboIX7TRhetAGDBH32JZPAD81ITwdfaVmI6jr9qoVRCZJROkPPGA9gmr5b55PYAu3GrCBznIwFkF1cYXjaOepgBYdGkgd3OcwsDoBW0fGP413Id6bu2RcR0x3GRBPqrx_OyZE_0jImIveiqMAh2YG7ttBrXQzPjPVnUTwi688NPfnaxC0tsGKCBtqaP6A6uVKMPXVWD7OpoyHnmeWtGHX5EjHYdg35UHK5QxoTHQyUs_sU0sKSTNWBuESM1KmHo3YYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ: اگر مانع دستیابی آن‌ها به سلاح هسته‌ای نشده بودم دیگران ناچار بودند رهبران جمهوری اسلامی را «آقا» خطاب کنند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 314K · <a href="https://t.me/VahidOnline/77821" target="_blank">📅 20:14 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77820">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/poQxBHIbsF5vFYomAmgH9YIXj5gt5hSo8iausngzV6rjsXsaGossYn4vEUgsUFbPNy_sjjqEYA1sX3HX9-y0UF59apEN6pzq04AgFAAQ6NYlfR7SpVGCkmx4WZ3hEXaNKYtEfIZBBdz7gEj0LpwoliYRSS51_o1lQ671WHLxSXifoqin3V88Ls6h0kia2AU7Uw77HE5rwzUuYya96owgi7TIZefqwC2kTgj9qtyvJD_it9nkl8qL-wczdbcbhNlJQ3Z9QdCWxSFf_2YUENYPaKtE6LePpxyw-NLdBlUa91ptbZHFlLIzccRgwNu9D_mDFXi4rcrJBiRt_dkYiuniUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یوسی کوهن، مدیر پیشین موساد، گفت ماموران این سازمان در گذشته چندین بار از تاسیسات غنی‌سازی اورانیوم فردو بازدید کرده بودند تا اطلاعات بیشتری درباره این مرکز هسته‌ای به‌دست آورند.
به گزارش تایمز اسراییل، کوهن، روز سه‌شنبه ۲۰مرداد ۱۴۰۵، در نشست «مجمع جلیل» در شهر صفد، گفت: «ما بارها از سایت هسته‌ای فردو بازدید کردیم تا این سایت را درک کنیم.» او درباره زمان این بازدیدها و این‌که چه افرادی از سوی موساد در این بازدیدها حضور داشتند، توضیح بیشتری نداد.
او همچنین درباره حمله آمریکا به فردو گفت: «بمباران آن توسط آمریکایی‌ها تحقق همه رویاهای من بود.»
تاسیسات فردو، همراه با مراکز هسته‌ای اصفهان و نطنز، در جریان جنگ ۱۲روزه اسراییل و ایران در ژوئن ۲۰۲۵ به‌شدت آسیب دید.
گزارش‌های پیشین حاکی از آن بود که حدود ۴۴۰ کیلوگرم اورانیوم با غنای بالا که در این تاسیسات نگهداری می‌شد، زیر آوار مدفون شده است. با این حال، اسراییل بر این باور است که ایران پس از جنگ بخشی از این ذخیره اورانیوم را به سایت «کوه پیک‌اکس» منتقل کرده است.
کوهن همچنین گفت اورانیوم غنی‌شده تا سطح ۶۰ درصد همچنان فاصله زیادی با ساخت بمب دارد. این سخنان با ارزیابی برخی کارشناسان هسته‌ای تفاوت دارد. دیوید آلبرایت، کارشناس حوزه هسته‌ای، پیش‌تر گفته است اورانیوم ۶۰درصدی ایران می‌تواند در صورت تصمیم تهران برای ساخت سلاح، ظرف چند هفته یا حتی چند روز تا سطح مورد نیاز برای تولید جنگ‌افزار هسته‌ای غنی شود.
کوهن پیش از این نیز به‌طور علنی درباره فعالیت‌های موساد علیه برنامه هسته‌ای ایران صحبت کرده بود. او چند روز پس از پایان دوره ریاستش بر موساد در سال ۲۰۲۱، در مصاحبه‌ای کم‌سابقه با تلویزیون اسراییل، جزئیاتی از عملیات این سازمان علیه ایران را بیان کرد.
او در آن مصاحبه از انفجار در تاسیسات زیرزمینی سانتریفیوژهای نطنز سخن گفت و توضیحاتی درباره عملیات سال ۲۰۱۸ موساد برای سرقت آرشیو هسته‌ای ایران از یک انبار در تهران ارایه کرد. کوهن همچنین گفت محسن فخری‌زاده، دانشمند ارشد هسته‌ای ایران که بعدتر ترور شد، سال‌ها در فهرست اهداف موساد قرار داشته است.
کوهن در برنامه مستند «اوودا» با اجرای ایلانا دایان در شبکه ۱۲ اسراییل نیز گفت که با تاسیسات مختلف هسته‌ای ایران آشنایی نزدیکی دارد. او در این برنامه گفت اگر فرصت پیدا کند، دایان را به بخش زیرزمینی نطنز خواهد برد؛ جایی که به گفته او سانتریفیوژهای ایران در آن فعالیت می‌کردند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 329K · <a href="https://t.me/VahidOnline/77820" target="_blank">📅 20:04 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77819">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Mf-UK94yZu-92FCUpatnKoq_7xJDt6jVgHdUnF5_4gTF9dH5LKAWC8k8FwYAHPgjTdPgoz35hjV7R8SCalmSP9cUj_GKtqRSCfRMHOpBxZ7cfZJM-LUkPmyZjxUAqCyi0MQZKP-wOfRwt-YqHYimtKbGeGJRhdJa66h24byRoBQUvKG7yF4D_pDIZpTVcCid5sy-51yL-yTDc2QdPrhLXXlxiuIuLZKeUI3fii_nTKM506_2G9AD4Goozm4CS7nf2O4iGnO9G1UJ2sMTtD47wsDtw5J9_jaor99Wp9Y8G7L5nuUhrAMNRtuGPhBySSkGEThmJ9Xua9F6oFIYfynJdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرنگار شبکه‌های تلویزیونی العربیه و الحدث عربستان سعودی روز سه‌شنبه، ۲۰ مردادماه، گزارش داد که در پی اصابت یک موشک بالستیک  حوثی‌ها به یک کشتی تجاری در تنگه باب‌المندب، سه نفر از اعضای خدمه این کشتی کشته شدند.
بر اساس این گزارش، قربانیان دو پاکستانی و یک تبعه اندونزی بودند. الحدث گزارش کرد این موشک از شرق استان تعز شلیک شده و کشتی تجاری را هنگام عبور از باب‌المندب هدف قرار داده است.
این حمله در شرایطی رخ داده که تهدید علیه کشتی‌های تجاری و مسیرهای کشتیرانی در دریای سرخ و تنگه باب‌المندب همچنان ادامه دارد. باب‌المندب یکی از مهم‌ترین گذرگاه‌های دریایی جهان برای تجارت و انتقال انرژی میان دریای سرخ و اقیانوس هند است.
همزمان، درگیری‌ها در چند جبهه یمن نیز ادامه داشته است. بر اساس گزارش «العربیه» و «الحدث»، نیروهای دولتی یمن مواضع و تجهیزات حوثی‌ها را در چندین جبهه هدف قرار داده‌اند.
@
VahidOOnLine
شمار کشته‌شدگان حمله حوثی‌ها به کشتی تجاری در باب‌المندب به ۴ نفر افزایش یافت
@
VahidOnLive
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 297K · <a href="https://t.me/VahidOnline/77819" target="_blank">📅 18:24 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77818">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/U6geAXRymy4s9IhrupnfFts4EdCksxZ8OTDk7H4eiLwlt5C_lcnLtLUlvNFn1KT6CxTwJKQIJSUbdWa9KJdzYVcPibDoAEspM6qNatjCK5Aff0mvvjNy9rTW2N06rCtYjK7D0WX2CSKGZCk8oBUbyawn5tVjTXBPDuvp8fS37Md5jF4Rp6j7ZMXxk1g4DJf4Ky1ml7fNoxv-hGn-ZwHlk-3PAub-SuXSbS0S-ZGc7XP8gm5WNj-a9_5VQubl9UctC3BaRnuu-aTF1cFIstg5oj2Qddi1JmYEifB0jRoM4CoJa52m6pv-ElpC48-O5_dWEUtJ8dH2Y709RWLbuVsyyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک مقام آمریکایی و منابع امنیت دریایی از هدف قرار گرفتن یک کشتی کانتینربر با پرچم پاناما در دریای عمان خبر داده‌اند؛ یک مقام آمریکایی می‌گوید این کشتی به هشدارها برای توقف توجه نکرده و در تلاش برای شکستن محاصره دریایی بنادر ایران بوده است.
همزمان، روزنامه وال‌استریت جورنال به نقل از یک مقام آمریکایی گزارش داد که یک بالگرد نظامی ایالات متحده پس از آن‌که خدمه کشتی هشدار نیروهای مأمور اجرای محاصره بنادر ایران را نادیده گرفتند، به سکان این کشتی شلیک کرد.
@
VahidHeadline
آپدیت:
پست سنتکام ترجمه ماشین:
اوایل امروز، نیروهای سنتکام تجهیزات هدایت کشتی
M/V Vela Nova
با پرچم پاناما را از کار انداختند؛ این کشتی باری در حالی که می‌کوشید از خلیج عمان عبور کند و با حرکت به‌سوی یکی از بنادر ایران، محاصره آمریکا علیه ایران را نقض کند.
پس از آنکه خدمه غیرنظامی کشتی هشدارهای مکرر نیروهای آمریکایی را نادیده گرفتند، یک بالگرد
MH-60
نیروی دریایی آمریکا دو موشک هلفایر به موتورخانه
Vela Nova
شلیک کرد. این کشتی دیگر برخلاف محاصره آمریکا در حال حرکت به‌سوی ایران نیست؛ محاصره‌ای که همچنان به‌طور کامل برقرار است.
تا ۱۱ اوت، سنتکام مسیر
۵۵ کشتی تجاری
را که می‌کوشیدند محاصره را بشکنند تغییر داده،
۳ کشتی
را که از دستورات تبعیت نکرده بودند از کار انداخته و وارد
۲ کشتی
شده است.
نیروهای آمریکا که در خاورمیانه فعالیت می‌کنند، به‌شدت هوشیار، مرگبار و آماده‌اند.
CENTCOM
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 273K · <a href="https://t.me/VahidOnline/77818" target="_blank">📅 18:22 · 20 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
