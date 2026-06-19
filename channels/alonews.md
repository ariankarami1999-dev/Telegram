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
<img src="https://cdn4.telesco.pe/file/ZtlW37VfZnXBGn-pDwlfbQ-QbkcxYOJrrZO8qIVSPbMekE_Mkmaz6TFb_Bk7NrtTmQBssp5kAoKY3iTAw1LvbMbtVv74rIk2GpZ7DFJmVKMZiI3hwsFiB5gVG-FThpN67aZZeqQs438s_qm-rtaQRaW9SRJ9Ukrj0VbKclcAzEbYfCJbNEomI-EuV7zduPiSOy1dTFm7_KCzL8kf8pK1Qa3VnMght3UQK58_PiVn63vdcRQ9lM-j_1A1X_BaSQtSQ-td8TUwwNwHfTlCPLQO6aSs42qk81A8vOQCWLWKZqTmB__Mvkd5UYvyn9mBbp48SW6ut3UkPCSKipNMHMd1Dw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 964K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directادمین کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-29 03:39:11</div>
<hr>

<div class="tg-post" id="msg-129021">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/64fe1a0123.mp4?token=t9wVvQi2QaNyUuihhXi1moMtK9DAqZ9p-rjCdzgqsa2_z2DlyM6WDIoapWWULkAf2JOVQudzy_RxyhzAmOfNTy5ReODo9GIyIOQNlkJeGTI5Io_nv5uDEkbcIZ6h6ahH2pWs-KGf_YZs_Mxqn3gPRM0R-FRvtVWhFFGzGten-lgB0nuFYLQEMDl-vB1OAXhpRjzT0WlXgyU0tyrMmxZZ3uwCnT0RjA0hp1zcYwSHa82wsNaZtjNkoczd7xoT9mFsfed5ntv4B8_OXKZbnwO7ZCLwYkOQVpd5AXqnqeMqGhKkM0AvCC-9N2JBz6XL5oC_TdYx4IKNRnHsLeaLHHwfpg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/64fe1a0123.mp4?token=t9wVvQi2QaNyUuihhXi1moMtK9DAqZ9p-rjCdzgqsa2_z2DlyM6WDIoapWWULkAf2JOVQudzy_RxyhzAmOfNTy5ReODo9GIyIOQNlkJeGTI5Io_nv5uDEkbcIZ6h6ahH2pWs-KGf_YZs_Mxqn3gPRM0R-FRvtVWhFFGzGten-lgB0nuFYLQEMDl-vB1OAXhpRjzT0WlXgyU0tyrMmxZZ3uwCnT0RjA0hp1zcYwSHa82wsNaZtjNkoczd7xoT9mFsfed5ntv4B8_OXKZbnwO7ZCLwYkOQVpd5AXqnqeMqGhKkM0AvCC-9N2JBz6XL5oC_TdYx4IKNRnHsLeaLHHwfpg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
جی‌دی وانس در مورد اسرائیل:
گاهی اوقات مردم رابطه را به اشتباه توصیف می‌کنند و می‌گویند که اسرائیل و ایالات متحده اساساً همیشه همسو هستند.
این اصلاً درست نیست. ما کشورهای متفاوتی هستیم. نیازهای متفاوتی داریم. جغرافیاهای متفاوتی داریم.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/alonews/129021" target="_blank">📅 01:58 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129020">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5c34df45c9.mp4?token=jF34ZIFy4xcD2iQW92hZaBm8OmcqkA3FMrMi21aD7buyCYil-IckdWG2jTJ6W0e315SgxkctS4_h63sMJl5evXHDt1JD56b3NzcG1dkdKTsC8hozYFgEk7Jni9vqhHQD6MpaEW9L228nNbg0EODSIyCPVu8diDy8m4VRyW1KkW8qb170gFq_PrSn-WW8dZSxaCG-R04eMxBUI4v95usmLCwcE8xCtOmhDaRgAbiwUj_st1HxUnSVrlAsfJuRpLh44jEDeURV8_-9TRHZK5S8PlFA9mysFzQZpxj6YKJkRcu3dMBAVjAVMaorq8t_yr5rAfNs8FsZGBDtbk78I2KtMA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5c34df45c9.mp4?token=jF34ZIFy4xcD2iQW92hZaBm8OmcqkA3FMrMi21aD7buyCYil-IckdWG2jTJ6W0e315SgxkctS4_h63sMJl5evXHDt1JD56b3NzcG1dkdKTsC8hozYFgEk7Jni9vqhHQD6MpaEW9L228nNbg0EODSIyCPVu8diDy8m4VRyW1KkW8qb170gFq_PrSn-WW8dZSxaCG-R04eMxBUI4v95usmLCwcE8xCtOmhDaRgAbiwUj_st1HxUnSVrlAsfJuRpLh44jEDeURV8_-9TRHZK5S8PlFA9mysFzQZpxj6YKJkRcu3dMBAVjAVMaorq8t_yr5rAfNs8FsZGBDtbk78I2KtMA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
خبرنگار
: آیا به اسرائیلی‌ها اعتماد دارید؟
🔴
جی‌دی وانس
: من به هیچ‌کس اعتماد ندارم.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/alonews/129020" target="_blank">📅 01:43 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129019">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YVJ4vlMmWssMzwZ5D8llSEtkfXW3apjxO2bfok--FbQHTPMSr2ZBbsqaj-i6cMhEbO7bSzJsOUMPINbjOxxpb20o4OU9jF8t-9BuUupkKVid01gPBfII8WbFVEEWwfFTMS09I8jDCtFBAYhyTMH1Tw2HuO-N2wQQfGF5zUImZgyyWtLqnEWDMKWaL0UhB4yjCYbk62F49DEKCTQ6JDsnl-l1ifJPUAjPdIhvrZT2T_LZXWO8Vkc7jaSoXlh3NpybPk5b6-Y4dBijDBUXeZA56lhDdHFdHbRdLYB_uGG9CzH2KybaL8EQgLl66okwYfBxsh5rsD7wTuEFy_YTAtt-aQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ارتش اسرائیل (IDF) در یک قدمی شهر مهم و استراتژیک نبطیه
طبق گزارش MTV، تو محور کفر تبنیت درگیری شدید بین ارتش اسرائیل و حزب‌الله جریان داره با سلاح سبک و سنگین و توپخانه. کفر تبنیت هم حدود ۴ کیلومتر با نبطیه فاصله داره.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/alonews/129019" target="_blank">📅 01:29 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129018">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/44ee1e7683.mp4?token=R-eJqBo-NnB5sNowKpEERrroObUT2wA7_L3LLal3Lvj4es9v605GF6E469WLHTKODXxdzxxrzBmpdDXvZsj3Rd7VMLe5SxXmqpyTmy2HOBO4t8vrBzcKcj879LJmOaF2MlLKHhSIjzp2TrrPpM-HNJCuyC4xUb2jfsDyfZfsWr41JUxJYKMU2XMFAW-4dcS0FlgfQ6V2DqyJTD8j76n8M-eJKbBAF_mtoe4-UPG0KOd9oZtdXkv6HJbL7_83NOxXExrdiHYW5T7vh67OPxNbpYjTH4s11aSW0DI1ZXz-7hZVDwHRmxb4ZEk4Bf3PuhMMlV6vQdgwiaKmH4RS1z8MmA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/44ee1e7683.mp4?token=R-eJqBo-NnB5sNowKpEERrroObUT2wA7_L3LLal3Lvj4es9v605GF6E469WLHTKODXxdzxxrzBmpdDXvZsj3Rd7VMLe5SxXmqpyTmy2HOBO4t8vrBzcKcj879LJmOaF2MlLKHhSIjzp2TrrPpM-HNJCuyC4xUb2jfsDyfZfsWr41JUxJYKMU2XMFAW-4dcS0FlgfQ6V2DqyJTD8j76n8M-eJKbBAF_mtoe4-UPG0KOd9oZtdXkv6HJbL7_83NOxXExrdiHYW5T7vh67OPxNbpYjTH4s11aSW0DI1ZXz-7hZVDwHRmxb4ZEk4Bf3PuhMMlV6vQdgwiaKmH4RS1z8MmA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
در راستای اجرای بند یک توافق، حملات به لبنان ادامه دارد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/alonews/129018" target="_blank">📅 01:14 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129017">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">👈
رئیس‌جمهور فرانسه امانوئل ماکرون درباره ایران:
شما نمی‌توانید از طریق بمباران به تغییر رژیم دست یابید. آنچه من مشاهده می‌کنم این است که افرادی در اطراف رئیس‌جمهور ترامپ، هم در حوزه سیاسی و هم در منطقه، او را به پیشروی بسیار بیشتر و قوی‌تر ترغیب می‌کردند.
🔴
تغییر رژیم در درجه اول هدفی است که توسط خود مردم به دست می‌آید—حداقل این چیزی است که ما باور داریم.
🔴
در غیر این صورت، نیازمند عملیات زمینی گسترده، ماه‌ها یا سال‌ها جنگ است. به آنچه در افغانستان رخ داد نگاه کنید. آیا تغییر رژیم پس از بیش از ده سال موفق شد؟ خیر.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/alonews/129017" target="_blank">📅 01:02 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129016">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iHokiCxGcMGG2EITx20hFBBlEwj0ogzH6X_PWs8KsbEDj3MZyw1dE56eCSd9y175mxGwDaogAky-PMDFHamI1wk1m5u0WULPGeYPHWcwkfhXc25Gm-eLASOsu_la_ZyFnvbCjRNbPZGwrc-D993tEyxXLG9kNTKMeFnCIHjuES2prFf4hNOUhds2jF7igcHu_-wURKj__WJrW1psUNMAFClEyTmOY00ZZiygMkCXUqmRCQJUL9_yge4B0R8JY23jrzDJfJmTwsFdqUuBhocsru9e_6ddNnGI5B7dJBhiLz2PCcF2yD8ltHCjavoVMKK8Y0fIyS3IcmxLiFDCYzXKZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
یکی رفته ویکی‌پدیا و نتیجه جنگ رو پیروزی ایران نوشته
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/alonews/129016" target="_blank">📅 00:50 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129015">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/93f21d642d.mp4?token=mMEGOy0d1RHhRJ1eO4Tlufe5f9iK6wjIiYOLvYf00WE-semNw-mmW7TKbcKsYc7x8Dig5aeCnpppEfunXP7-l-OGlA6Gg2kUUONhCwm8d2CPyqG4f7Am_l6MtkNoR1Hj57l75sfiGZd3Gi2vVWD986h-K4m6DtPUkIGpWS5CrrPN_gfwPWxKVGMXKD2vysmfKLbS7riyZOLKH1_bNtxfNiSTSbCilKHABXW66s_h0gTHV-KgbmjQ5zmnyDTEojlflXciwSfyLCk92Tf1IHB7bEprV7nU-x534Ts80I2cWc07p4LDkF8FuSfJVHXmoI-1wnCXhVEG5SPifIHfDVeIcQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/93f21d642d.mp4?token=mMEGOy0d1RHhRJ1eO4Tlufe5f9iK6wjIiYOLvYf00WE-semNw-mmW7TKbcKsYc7x8Dig5aeCnpppEfunXP7-l-OGlA6Gg2kUUONhCwm8d2CPyqG4f7Am_l6MtkNoR1Hj57l75sfiGZd3Gi2vVWD986h-K4m6DtPUkIGpWS5CrrPN_gfwPWxKVGMXKD2vysmfKLbS7riyZOLKH1_bNtxfNiSTSbCilKHABXW66s_h0gTHV-KgbmjQ5zmnyDTEojlflXciwSfyLCk92Tf1IHB7bEprV7nU-x534Ts80I2cWc07p4LDkF8FuSfJVHXmoI-1wnCXhVEG5SPifIHfDVeIcQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ: من فقط از طرفدارهام خوشم میاد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 38.6K · <a href="https://t.me/alonews/129015" target="_blank">📅 00:47 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129014">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7b055dff63.mp4?token=Q_Zq9Agp-GFyJsl22nQ1Tieivx5k3U36NSTzzIeROOADpzYHh8QZPLM2wQdmiZIDVUuAhi-w8r02nE17BK98_-wTx3vfXZuPYMnT-uGkQhEdDCVJK4SMch6xCFySEvp_5H60tW7_QWsW5F3q9nnNZP_w1azDVPlm3HYsNPowHzvr7N3r0gp3mBxTz22MzhCNNFHou-_FCxM-4cSuOQXp_k8c1a7dA0Aj64EHMTkKn5GBUfXTluJ4BqefB2kiHwhJw9uqmuRDDMO1XRaBHTRam25L3-N6ygIR4gvNDwJvp-NiNOEeibwpfhHAl3Cooyvx5E-QxgWzwZ7_JQXm-RLCdg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7b055dff63.mp4?token=Q_Zq9Agp-GFyJsl22nQ1Tieivx5k3U36NSTzzIeROOADpzYHh8QZPLM2wQdmiZIDVUuAhi-w8r02nE17BK98_-wTx3vfXZuPYMnT-uGkQhEdDCVJK4SMch6xCFySEvp_5H60tW7_QWsW5F3q9nnNZP_w1azDVPlm3HYsNPowHzvr7N3r0gp3mBxTz22MzhCNNFHou-_FCxM-4cSuOQXp_k8c1a7dA0Aj64EHMTkKn5GBUfXTluJ4BqefB2kiHwhJw9uqmuRDDMO1XRaBHTRam25L3-N6ygIR4gvNDwJvp-NiNOEeibwpfhHAl3Cooyvx5E-QxgWzwZ7_JQXm-RLCdg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
رئیس جمهور ترامپ: مدال افتخار کنگره رو میخواستم به خودم بدم، اما بهم گفتن که نمیتونم و چیزی پیدا نکردم که واقعا ارزشش رو داشته باشم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 40.1K · <a href="https://t.me/alonews/129014" target="_blank">📅 00:40 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129013">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f440aeea74.mp4?token=pDWCDGcdsNOnUWB9SlHgO2D2CmpM-Q-LfL6e4bpob0tjdnYTsAfGcJTJihRiU8pjZnYmoy-Bqjmx4N1l0csFbjSMBo39TV1jw3Lu6ZbB1my6t7UgRpYhgaG2UA00yGWi6VstLPFzuo98MG7_lf-gWP2mdGe2XvVYqLBv6Ka9xpshUEDbG-sgzmulcPRsj7np52hGJdA1HtISNAzZh-VfEJTQNx14NeaX4sz-xYe8FY3TXXaNz0IEhjDIeQu-hxexiZsX4_4iUhXMdBPyWc2GThd7DRKYO-wZLhnEQ-Nw9jv3zA2VBy0sZHrf0WnpWc9MQVHwZ5GPQzYzTM4nxKAcfA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f440aeea74.mp4?token=pDWCDGcdsNOnUWB9SlHgO2D2CmpM-Q-LfL6e4bpob0tjdnYTsAfGcJTJihRiU8pjZnYmoy-Bqjmx4N1l0csFbjSMBo39TV1jw3Lu6ZbB1my6t7UgRpYhgaG2UA00yGWi6VstLPFzuo98MG7_lf-gWP2mdGe2XvVYqLBv6Ka9xpshUEDbG-sgzmulcPRsj7np52hGJdA1HtISNAzZh-VfEJTQNx14NeaX4sz-xYe8FY3TXXaNz0IEhjDIeQu-hxexiZsX4_4iUhXMdBPyWc2GThd7DRKYO-wZLhnEQ-Nw9jv3zA2VBy0sZHrf0WnpWc9MQVHwZ5GPQzYzTM4nxKAcfA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
رئیس جمهور ترامپ:
پيت هگست ، اون اخيرا چند تا پيروزي خوب داشته اون قراره خيلي بيشتر از اين داشته باشه‌‌
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/alonews/129013" target="_blank">📅 00:39 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129012">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/618be4eaea.mp4?token=M9MfPikSdzB9BLlDpWLWCd-z3JGflgAz4BDUcjV4nn5X7Gt0ern8lRFwaQRcewH8DgzV--87YN1A4m29o1826Yg9zL1_m5oJbP_qElDu_qEJI99RDMGksKH40kAY3nEtyiNbJG05q-KvH_Cp6mrFLCVqCKEUmKM8Eukoh5UiZc-FdmGweoJf210NQGe-bLT-WhXisF_PIQeGXBToSf5L6iVc_7bMwNlwWbv9z1UJymirJDkoQ1oz6-47p0h91HC8fM1oJl6Yh7wVNOG2h0wB6IbNxDkdhKJZjFQtfJkL2oplX9PfwA4q-xWSJChS_iUIYqHQhcqEHPgF7eFxEgNSw2yrIVTRDON17B4l6sSdojTUXlRnHHGxCvfliH7thkBzifbZ5UKC5i-afQVnaKHOQXZvCeHPrcslqKQJHSbCTdIF7XKOIn3o5PZJLdK46dbfRm7WKA1LprjmdNWg9hynH8EBePe0Z25MwpbXv-EE-FjJlcoXw7wMBFTnouPCTFq8Bo-dkWZEF3aYxpgcynwmISDefl-kUy30GRymbBguYL0OBX7hme3Wt_dDUa2yTznVvliyQOztdU2N7W84rqRIlPasZCv_mTLyseCUYLCsZqrGfk3_mGZ333eZppz-1t5I8Wu7HY-9ooDy0SFwLXIc9dihWT34plZyCE4IqxSNnsQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/618be4eaea.mp4?token=M9MfPikSdzB9BLlDpWLWCd-z3JGflgAz4BDUcjV4nn5X7Gt0ern8lRFwaQRcewH8DgzV--87YN1A4m29o1826Yg9zL1_m5oJbP_qElDu_qEJI99RDMGksKH40kAY3nEtyiNbJG05q-KvH_Cp6mrFLCVqCKEUmKM8Eukoh5UiZc-FdmGweoJf210NQGe-bLT-WhXisF_PIQeGXBToSf5L6iVc_7bMwNlwWbv9z1UJymirJDkoQ1oz6-47p0h91HC8fM1oJl6Yh7wVNOG2h0wB6IbNxDkdhKJZjFQtfJkL2oplX9PfwA4q-xWSJChS_iUIYqHQhcqEHPgF7eFxEgNSw2yrIVTRDON17B4l6sSdojTUXlRnHHGxCvfliH7thkBzifbZ5UKC5i-afQVnaKHOQXZvCeHPrcslqKQJHSbCTdIF7XKOIn3o5PZJLdK46dbfRm7WKA1LprjmdNWg9hynH8EBePe0Z25MwpbXv-EE-FjJlcoXw7wMBFTnouPCTFq8Bo-dkWZEF3aYxpgcynwmISDefl-kUy30GRymbBguYL0OBX7hme3Wt_dDUa2yTznVvliyQOztdU2N7W84rqRIlPasZCv_mTLyseCUYLCsZqrGfk3_mGZ333eZppz-1t5I8Wu7HY-9ooDy0SFwLXIc9dihWT34plZyCE4IqxSNnsQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ: بازار سهام به تازگی به بالاترین حد خود در تمام دوران رسیده است. حساب‌های 401K نیز به بالاترین حد خود رسیده‌اند.
🔴
و قیمت نفت مثل سنگی سقوط می‌کند. به جز این، روز دیگری در بهشت است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/alonews/129012" target="_blank">📅 00:34 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129011">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DHuaad-v4qvSC0BcudNx2KJprLTgiAPFyPioA58MXTD8cjHpieHStnoMXYBQ60q2cG1rNOjkZ4AdUXnxp7e8BC-qE2_pfurOdWX9uFnkvCH6ZWxBx896YEhnhrCFPHRDgj_vl1MmDvZZ6irK2GwSKDjVk3jpCVvAd7ijjd-CAVva9Ig_MbZjp31k7nFf25Ep5izYezSNqmoqQv4Mr7xv6t5puLUgUK1usjdQtgyVcZx6MpXdzb2YddLx4pgzA39W7jd7c4wErba-ths0ndOIBsJJSMq4m6ilLaUQBp1GWS-1b0kmjq_eNi2mMrOYRsY-XMb0Dai9hwBdvw2xHlJStw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پس نتیجه میگیریم با جابجایی کلمات در اسم محصول میشه قیمت رو ۲ برابر کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/alonews/129011" target="_blank">📅 00:32 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129010">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ekmj780GuazYBWdm1BNWF2Jyc4xD1e1EFuu74DpyhkNKSgVQMjzZ8FXHty9gGWMmMc-jIhchngjQJt7iLzCJGgSA7VYZ2krkMqxGlH07drLEm129ESBHTb3hXAc3zhMIZV8PRhqdOybEu-RiuUsIiixlEfnackSxorHw2nEFXU3p334hr-5UeJB3ATqL9U5u3xcFHT84hd4o4HRBQle3PjjZN6R6kaojFlqjbegH2LN0i3gQw8divou0PIqJvPDXokhUVACB5hI0BbJfBHXn9A5BgA7EowwBZwBaHuSZpLU-_6foq__OUcKgiPs30KNeM2vK8W48JCF2A1dYgGDeDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
حمله عظیم پهپادی اوکراین برای دومین بار طی ۲۴ساعت گذشته
🔴
تا کنون در این موج بیش از ۳۰۰ پهپاد شلیک شده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 41.1K · <a href="https://t.me/alonews/129010" target="_blank">📅 00:24 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129009">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">👈
نورالدین الدغیر خبرنگار الجزیره مستقر در تهران: «اطلاعاتی حاکی از آن است که دیدار ایران و آمریکا در سوئیس برای فردا جمعه دیگر برگزار نمی‌شود، اما مذاکرات طبق تفاهمنامه ادامه خواهد یافت، هرچند ممکن است به سطح کارشناسی محدود شود و احتمال دارد بازگشت به پلتفرم قدیمی در مذاکرات صورت گیرد.»
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 41.1K · <a href="https://t.me/alonews/129009" target="_blank">📅 00:21 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129008">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">👈
معاریو : مقامات اسرائیلی از شکاف عمومی بین ترامپ و نتانیاهو که ممکن است فراتر از کلمات به اقدامات عینی از جمله تأخیر در ارسال سلاح‌ها، محدودیت‌های کمک‌های نظامی و حتی اقداماتی شبیه به محاصره تسلیحاتی تبدیل شود، می‌ترسند.
اسرائیل معتقد است فشار آمریکا برای عقب‌نشینی از جنوب لبنان و حریم سوریه تشدید خواهد شد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 42.4K · <a href="https://t.me/alonews/129008" target="_blank">📅 00:16 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129007">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">👈
وزیر جنگ اسرائیل: اسرائیل در هر لحظه برای عملیات مستقل در ایران آماده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/alonews/129007" target="_blank">📅 00:03 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129006">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/10a67b46ae.mp4?token=RaioeafvovgwxYo1F507tSEQhnDxqJhKsiQgwK4gN2wrXQLCZ1ZCxzH2oUnPY0gc_DU4eajBFUMe6ZDIL9UCkXF3JevVVyLtYr9dbGjFwy0lLKOS9WKu7gKdcrCteDw_fs1n_gig7gsMUoFCAUuqIafFo0I2KcngI2EGx1ycqXnSOoPSVIogn_qbyeAOnT1yFaw310GRIF7oA2CbFnJCN3R-YOT82Q5BnXPAeEhYBpNSIXBC5gnuyiw5E6pHfN1zBmL8gDSpRCbBSZsog0eAwRqrq9T8y8PpOOOgmI6mbi95FbeQbzO2ifacda3NuB8IIBT8ihsp8c4eKQQhN3QvqQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/10a67b46ae.mp4?token=RaioeafvovgwxYo1F507tSEQhnDxqJhKsiQgwK4gN2wrXQLCZ1ZCxzH2oUnPY0gc_DU4eajBFUMe6ZDIL9UCkXF3JevVVyLtYr9dbGjFwy0lLKOS9WKu7gKdcrCteDw_fs1n_gig7gsMUoFCAUuqIafFo0I2KcngI2EGx1ycqXnSOoPSVIogn_qbyeAOnT1yFaw310GRIF7oA2CbFnJCN3R-YOT82Q5BnXPAeEhYBpNSIXBC5gnuyiw5E6pHfN1zBmL8gDSpRCbBSZsog0eAwRqrq9T8y8PpOOOgmI6mbi95FbeQbzO2ifacda3NuB8IIBT8ihsp8c4eKQQhN3QvqQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
اوباما
:
همان‌طور که بی‌قراریم، مردم به دنبال خشم و تفرقه همیشگی نیستند. آن‌ها به دنبال انصاف و عقل سلیم و احترام متقابل هستند. در اعماق وجودمان، می‌خواهیم راهی برای بازگشت به سوی یکدیگر پیدا کنیم، نه دور شدن بیشتر.
﻿
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/alonews/129006" target="_blank">📅 23:58 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129005">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">🔴
فوری / ویتکاف: بازرسان آژانس راهی ایران می‌شوند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/alonews/129005" target="_blank">📅 23:57 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129004">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uXnxTh0kvnXfxzKhEWsqVhPezDcHvaOIu_0M-B76MY1xnIC15VvXG1BYbKGbtgdPaMmXO47nEZcD04pFniYOaEhx8EOc6A3333K4E4nkUsBOQoyO1TQdwAfPQUbyxa7QaVv3bKI6ySFxwhJ997pu0W4A-jtnpaIZv_rhI6Sn83VddbfkMgO87XDbCSFOYU2KDFuovo0WCZeKtfKGsD0pWBhYXvBu3JKvUqeoYNsJ1d1FC22IKv721S2HaPtF50tKYEva9ZUnXV_a1YrdsLnMRm7kks1J4j_rDk9Lrh3POswhhyWzeT1QQ-CLM9f4dIMeThqMpubUokM5uxa3IWufVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
اداره دریانوردی بریتانیا: تنگه هرمز اکنون باز است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/alonews/129004" target="_blank">📅 23:53 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129003">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو توئیت | AloTweet</strong></div>
<div class="tg-text">مردی در یک شرکت بود که همیشه پشت صحنه همه تصمیم‌ها را می‌گرفت، اما هیچ‌وقت نامش در میان نبود.
هر پروژه‌ای که شروع می‌شد، یکی از کارمندان را جلو می‌انداخت و می‌گفت: «این ایده خودش بود.»
وقتی کار خوب پیش می‌رفت، آرام‌آرام خودش را صاحب اصلی فکر معرفی می‌کرد.
اما اگر مشکلی پیش می‌آمد، همان فرد را مقصر نشان می‌داد.
همه تصور می‌کردند او فقط یک ناظر بی‌طرف است.
درحالی‌که نخ تمام ماجراها در دست خودش بود.
سال‌ها این بازی را ادامه داد و همیشه چهره‌ای پاک و منطقی از خود ساخت.
تا اینکه یک روز چند نفر از همان قربانی‌ها کنار هم نشستند.
رد همه تصمیم‌ها را دنبال کردند و فهمیدند فرمان از کجا صادر می‌شده است.
حقیقت که آشکار شد، دیگر کسی حاضر نشد سپر بلای او باشد.
آن روز برای اولین بار مجبور شد خودش جلو بایستد.
و تازه فهمید روسفیدیِ واقعی با پنهان شدن پشت دیگران به دست نمی‌آید.
[
@AloTweet
]</div>
<div class="tg-footer">👁️ 44.8K · <a href="https://t.me/alonews/129003" target="_blank">📅 23:46 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129002">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">👈
دبیر کمیته ملی کنترل و پیشگیری سرطان وزارت بهداشت درمان و آموزش پزشکی: ابتلا به سرطان در ایران تا سال ۱۴۴۰، دو برابر میانگین جهانی است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/alonews/129002" target="_blank">📅 23:42 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129001">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">👈
سفیر پیشین روسیه در ایران: یادداشت تفاهم ایران و آمریکا یک پیروزی تاکتیکی برای تهران بود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/alonews/129001" target="_blank">📅 23:34 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129000">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QHoNcmxSyxydfCOnn3JekVxkmcLus8YMbvmjdPK3oLT4D1hWVEWFhnbCmxrE760WXvIWwdwuEstN93pgcTkQslGRqrCrKmRQX2uom3l6bWllCn8DwYGvuZ9qICD_qoOXBfR7iDt8ky3v5OgQAoVbHb6qEeGa1DY1YR2boAm0rVp11scNz4kFmx0A3BlxuDvLNvuqUIZ5BeUVV5MaID0BDPvKE9oFHXdvv3cr110FnjGVx35nNG0gUfZ6iBK6e3mmcyBceHzkPfC3gjrT3R2F9ZIqdaZtRfZ9rQk0d92jzgGo6Wg-OFdOnP8GBmss2aV2pS9kCBXyfGk8a4TNuKr0UQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
شریعتمداری: شهید لاریجانی دنبال این بود که حساب گروسی را برسد؛ اما جنگ شد و کشته شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 48.6K · <a href="https://t.me/alonews/129000" target="_blank">📅 23:28 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128999">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/L8WkO4OeSiWpSS2vts_HpKBP8-9vk5IaxkL6-et5U3WODywxT5W07d7caAJPKpjEgLlAhH1jCRQE4RfqDNYbrD4SB9VglXZjEp2G8vDHhrDL64FRJq2D2wDrcQWLLD2Fw-YSPos8E99isjBf5Ojomb0Dz_D9uV7c8p37RyyTFgCkZkflngRASrMc3stgdebeNO-k2AbG0LpN8HsB8ZZQ0PaATEXfWvxRZc96zlVvlU3p7xFx4AUwwP-mFBv90ExMq-a4J-4BU3b1gnYi1N3sLIz-8Nt9JGyypqYbVa3Gga_LIM96quPbDHZ3nAAMY0a8GNR8qbaFRY32ZnfRfCXGGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارائه مدارک تحصیلی معتبر از «دیپلم تا دکتری»
🎓
مدارک رسمی و معتبر  هستند و قابلیت استعلام  بصورت نامه نگاری و آنلاین از سامانه های مربوطه را دارد
قبل از پیش پرداخت ثبت نام شما انجام میشه و تاییدیه سنجش دریافت میکنید
سپس پیش پرداخت واریز میکنید
✅
مؤسسه راه سبز تنها مؤسسه صدور مدرکی هست که رضایت ویدیؤیی متقاضی هارو داره
صفحه تلگرام :
t.me/+2yeLgZeivDkzNDYx
وب سایت :
Rahe-sabz.com
➖
➖
➖
➖
➖
➖
➖
➖
➖
➖
➖
➖</div>
<div class="tg-footer">👁️ 48.4K · <a href="https://t.me/alonews/128999" target="_blank">📅 23:26 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128998">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">👈
مسئول سیاست خارجی اتحادیه اروپا: ما تحریم‌های مختلفی علیه ایران داریم. اگر توافق هسته‌ای وجود داشته باشد، فکر می‌کنم کشورهای عضو اتحادیه اروپا در مورد این لغو تحریم‌ها بحث خواهند کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/alonews/128998" target="_blank">📅 23:21 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128997">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/08672f5757.mp4?token=a5DKrKGKGdW7VGSrJ1DSK9GAy_LqplnGEJeeQZAJKk9UQ2U_Eb7mDw7R6xk85C48n7DRC8Cjv2zIwOi5SRrmo1K3nxq6jkFmPNvDFZ-WeYcwGkX3TDguKEk1xgNAAu7BUXahvN3est9BHLrZ9y3doql_ITgJT-t8kesg72fGlm60B1h8byJbwAGxWS-SrhrzZ4PhJ5oflKDVN-oFUuWxupizFWicvDwoiUctCE9kQOBdXzkrT1_FBIFbnnLYV2pmVeBlQ54Fs-vaAKEi5-CWHmmj7mX_cioU1QYWcXSCcJSqQbbbLWmMTkMrweAL4hxantl48_KyKyR_l8gfBQJVgw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/08672f5757.mp4?token=a5DKrKGKGdW7VGSrJ1DSK9GAy_LqplnGEJeeQZAJKk9UQ2U_Eb7mDw7R6xk85C48n7DRC8Cjv2zIwOi5SRrmo1K3nxq6jkFmPNvDFZ-WeYcwGkX3TDguKEk1xgNAAu7BUXahvN3est9BHLrZ9y3doql_ITgJT-t8kesg72fGlm60B1h8byJbwAGxWS-SrhrzZ4PhJ5oflKDVN-oFUuWxupizFWicvDwoiUctCE9kQOBdXzkrT1_FBIFbnnLYV2pmVeBlQ54Fs-vaAKEi5-CWHmmj7mX_cioU1QYWcXSCcJSqQbbbLWmMTkMrweAL4hxantl48_KyKyR_l8gfBQJVgw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
در جریان حمله امروز صبح پهپادهای اوکراینی به پالایشگاه مسکو، یکی از موشک های پدافند هوایی عاجز از رهگیری پهپادها دچار سردرگمی می شود و بسیار دقیق یکی از از مخازن سوخت را منهدم می کند !
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 50.2K · <a href="https://t.me/alonews/128997" target="_blank">📅 23:15 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128996">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">👈
شریعتمداری، مدیر مسئول کیهان: با مصادره اموال آمریکایی‌ها و متحدانش از طریق تنگه هرمز باید غرامت بگیریم از آمریکا
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 49.6K · <a href="https://t.me/alonews/128996" target="_blank">📅 23:10 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128995">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">👈
المیادین به نقل از منبع آگاه: هیئت مذاکره کننده ایرانی سفر خود به سوئیس را به دلیل تداوم حملات اسرائیل به جنوب لبنان متوقف می‌کند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 51.4K · <a href="https://t.me/alonews/128995" target="_blank">📅 23:03 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128994">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو توئیت | AloTweet</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0d437a78db.mp4?token=d-Rz6FNGZGj31kzROfCyAF_InXbowIjFX44Yonpvu_jdVgTFkeo5Qeo9DYpn3A-cwn3GEcmqLnenWBgGN0WTLzF2RFn7K9rxRuKnZOyqjVbRvVVNKIpfzCIeJ784zxz6c6M3TKk6-T9RtzlKXhdS7JZf8ltbc3dtnjopGmCB8_Z-GrPYDpz6VzAQoi1TCd0vMu1HF9oiuHb-tefhpX25Apu92FbSIUPzE4CZaRfJQTlodD9KVFZ2CbIWBhFMDaZsMXGdLO3ROu1dCTkarXG8EDch3Z8aGDCDhiQpnzRI_yMr15f2X5r8qrhwdl-or_oDFfiJfLVHvmuaFFpu6mzAjg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0d437a78db.mp4?token=d-Rz6FNGZGj31kzROfCyAF_InXbowIjFX44Yonpvu_jdVgTFkeo5Qeo9DYpn3A-cwn3GEcmqLnenWBgGN0WTLzF2RFn7K9rxRuKnZOyqjVbRvVVNKIpfzCIeJ784zxz6c6M3TKk6-T9RtzlKXhdS7JZf8ltbc3dtnjopGmCB8_Z-GrPYDpz6VzAQoi1TCd0vMu1HF9oiuHb-tefhpX25Apu92FbSIUPzE4CZaRfJQTlodD9KVFZ2CbIWBhFMDaZsMXGdLO3ROu1dCTkarXG8EDch3Z8aGDCDhiQpnzRI_yMr15f2X5r8qrhwdl-or_oDFfiJfLVHvmuaFFpu6mzAjg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اولین پاسخ پزشکیان به بیانیه مجتبی:
[
@AloTweet
]</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/128994" target="_blank">📅 22:42 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128993">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OIFrX3BifHMXFSGLrujkwBm5K7_sM4LywaWdM_WoGL7a2gCCZG9vI3Nz67TTD4eEOJKfekTIhwjJPwpfYu9EakDvQv7uHn6nSF87e-6nwWqT6rOkE-zi4OO7YI7kcaL1W8SVsQXTbvJd4y99EyAL8zRapOc_SSifu_1ZjtyEMYhsLnY27ssGQn0gXh39kyhdWEkHyWpWs0i-g1JzGPhMOahO473t23DLPT1J3iQoEpPMlTkpFpgRw7vJ3CJy67up8UJS4AFpbdJGpG7266e4w3D40oqSifHJuv7HaSJ7QYsl80ffVGPc1MK-I5P-oNwB_4Zb3cL10t_2n1Bf06_Rlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ثابتی: شرافتمندانه نیست
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 54.7K · <a href="https://t.me/alonews/128993" target="_blank">📅 22:39 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128992">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">👈
رسایی :  باید پزشکیان رو اعدام کنیم.
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/alonews/128992" target="_blank">📅 22:37 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128991">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">👈
شریعتمداری، مدیر مسئول کیهان: با مصادره اموال آمریکایی‌ها و متحدانش از طریق تنگه هرمز باید غرامت بگیریم از آمریکا
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 57.9K · <a href="https://t.me/alonews/128991" target="_blank">📅 22:36 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128990">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XTCWpxuHuhWTkB7KTQ9KATzDHb1fID769zp-m9u4LhRQKV2SJkee3C688SUM3s6ijT9q__EeBDyCf7aSDaF8y63N6jsGQVhCAhYQpHeG1AkgB5-5HWkF8uhDLlybqPnAC16hdY-RjK8vWFVNtsM1jtgCOuYkgBJWMnMH3SoYZoEP4n1lIUdFFcL68Wfq76S7O2V_kvzjFe6aUYuuklAQPImOyGg2g8gOEZErz0sg2UO9EoGUy7bwy2qXUHg27u0XSvb6H5frxLE1KlyzD-mXf0ht4JGviqm9b_d7f2nvo3SidpQDMoRMywKi-LVgWs_J_bKfmDM-4XzAit7zEdWynA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
رسایی :
باید پزشکیان رو اعدام کنیم.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 60.5K · <a href="https://t.me/alonews/128990" target="_blank">📅 22:34 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128989">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ReWBxRbdkMtY4k9S7y8iJaW5hecCzxyj4iAGnSF1RMfngB6mCItwbYkW3OuJW1i5g58zdpGjdIF3KG0qQdLll2Yb3ol601ysDemMjCO0ygy1bcC8KO9t9mLgjhN5cdAGxTp6aKN4kTvztoa1B0MWD9xYZNLboO7tV__BNabv-Xk81frHUAhn5zXSL9VAsVEa1NfqeEZYnRNDRgYEnCmjbw1Bzw25xY-a-5yBSazBNwNg03cFMpFbJuNMNTGPJJPYwLqSgv5fHi6V59NBl0xi3WPbVMK4B_a-GtEFKswdjbHAV2xNjkEfV-vyqmKHEh5JVF_Jg8WudgoBV6vhr4X9AA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
صدا و سیما مجتبی‌ خامنه‌ای با تفاهم‌نامه را زیرنویس کرد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/alonews/128989" target="_blank">📅 22:33 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128988">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🔴
فوری/شورای عالی امنیت ملی: بر اساس تفاهم‌نامه منعقد شده، تا ۶۰ روز هیچ‌گونه عوارضی از کشتی‌های عبوری از تنگه هرمز دریافت نخواهد شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 56.6K · <a href="https://t.me/alonews/128988" target="_blank">📅 22:31 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128987">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bW7vZfnGdgIUQlgNBQQlXxesXZShp9XctTFyxqmtLzBYSY1pDtqpNXg74Rii1TCkwfWk41zrOr67jO0_R5D7OkNXpZP8aPBb7lqjb1Zcnv-UWsU_yNdDBGnKYu8qxLtnyfTOVZE_SXEbPQ8coiXQ-bMwD22xg5h3lVOchSX52iB8amv7fEjm8EEWyikY5BksIQXRV_LAHzx3EY86hWyNfgkZANImrdcDakBMUKJlW_E67SmkQl4oIA6cCM3AQURB1wHympHPxDrePT7vwgFdl8hKq9CAND30klPcCq4lW2EL_C9hvKEMcVIYfep3wSNhcnAM6DwlX2b4ZAk7jycMwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
حساب رسمی کاخ سفید در X
:
ما واقعاً آمریکا را قبل از GTA 6 نجات دادیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 58.3K · <a href="https://t.me/alonews/128987" target="_blank">📅 22:24 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128986">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">👈
ترامپ: «ایالات متحده به صلح متعهد است، و ما از همه در منطقه خاورمیانه می‌خواهیم که به تعهد خود برای اجازه دادن به روند مذاکرات ما تا به شکلی عالی پیش برود، پایبند بمانند.
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/alonews/128986" target="_blank">📅 22:13 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128985">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M4qivLTGTyEzpEZG-lnvf1r37IJU9XXWrKTu-fchzVu3BZy_sjBrW43dppnAThjVardtqH6UN8tVRjxGfgGdnMPDE7x5g0a3X8cqf_HDNW9y0d0l6FLJEvoGoIumECduyreQkVVpNgOT6e1IFJPICcgelXiHxedMEFHU63x86ApKB7xA3whYYjJqMRNegmqD19In36fUy7PZC8pF15kZLOZCCK1NUpOgEfkF_Omc0IZCejqQwvSM9Yd1YVkSh_wLNjDl_xkhPKA9rJrO-f9YNUfq75we3QW_KFzPrOderc9gItPZcfGdzViAuQZJJ0d93GqrNkCiGmx2pmTjgJ5uCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
کسی خبر داره ازشون؟
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.3K · <a href="https://t.me/alonews/128985" target="_blank">📅 22:13 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128984">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X9sLAYDfd07OJc26MCDbbirHF2KJUoOIm37WSIch_51L_PLwI9PehrS5vthrTinINW8VAF8KdcH-13wjiHJjxk9TixeKEn4F18Xs3sWQRGSDE9YaTAT_-AZ6bSQQ0nPLLp8fw9fZh-CDzU4H_MXGL4WQvxXfOhHRoxu0AmGzJoyHFU1fvxEY8US8ytaou6qSp5BzGoWt6H9RlhNmUao9xOrjJ6hBjPtTA70YjMOeMgY8Z_NcnRfz54No16waA4rekwW0tqcDaQov7INTqCCGJ8DlPc5kXxj-MjFncKhJ2WNnmZPLk11uaAixb8i-mlkGXwg5_Wu44oXG7rfXB8oj0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ارتش اسرائیل اعلام کرد از منطقه‌ای که در نقشه با نوار قرمز رنگ مشخص شده، عقب‌نشینی نخواهد کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 58.9K · <a href="https://t.me/alonews/128984" target="_blank">📅 22:05 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128983">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">👈
طالبان  به دلایل مختلفی مثل جلوگیری از درز اطلاعات محرمانه، کاهش اتلاف وقت کارمندان و کنترل اخبار اعتراضات مردمی، گوشی‌های هوشمند را برای کارمندان دولت افغانستان ممنوع کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 58K · <a href="https://t.me/alonews/128983" target="_blank">📅 21:58 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128982">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">👈
فارس : تیم مذاکره‌کننده ایران تا حصول اطمینان کامل از توقف حملات به لبنان، هرگونه گفت‌وگوی تکمیلی را به حالت تعلیق درآورد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 58.7K · <a href="https://t.me/alonews/128982" target="_blank">📅 21:53 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128981">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">👈
آسوشیتدپرس: کاخ سفید توافق با ایران را به کنگره ارسال کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 59.4K · <a href="https://t.me/alonews/128981" target="_blank">📅 21:45 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128980">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">👈
ترامپ: «ایالات متحده به صلح متعهد است، و ما از همه در منطقه خاورمیانه می‌خواهیم که به تعهد خود برای اجازه دادن به روند مذاکرات ما تا به شکلی عالی پیش برود، پایبند بمانند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 59.7K · <a href="https://t.me/alonews/128980" target="_blank">📅 21:42 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128979">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">👈
ترامپ: انتظار داریم میان اسرائیل و حزب‌الله هم آتش‌بس کامل برقرار شود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 58.8K · <a href="https://t.me/alonews/128979" target="_blank">📅 21:40 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128978">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">👈
رهبری سیاسی اسرائیل به نیروهای دفاعی اسرائیل اجازه داده است که در داخل «خط زرد» در جنوب لبنان تیراندازی کنند، طبق گزارش کانال ۱۴ اسرائیل.
🔴
انتظار می‌رود مقامات ارشد نظامی در ساعات آینده قوانین درگیری و راهنمایی‌های عملیاتی به فرماندهان میدانی را به‌روزرسانی کنند.
🔴
این تصمیم همچنین شامل برنامه‌هایی برای نابودی هر «زیرساخت مرتبط با حزب‌الله» است که در داخل «خط زرد» شناسایی شود.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 60K · <a href="https://t.me/alonews/128978" target="_blank">📅 21:28 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128977">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🔴
فوری / رویترز: کاخ سفید متن توافق با ایران را به کنگره ارائه کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 59.4K · <a href="https://t.me/alonews/128977" target="_blank">📅 21:19 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128976">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4bec225d06.mp4?token=ngiaG5hvFMbXV3G7T-bjw-kfCwOO22wlO8MQtENDjaX5vBvbZV8JJctVfMIJddzFOcHAQtwnDhoNS5iHaF9tkruGBGu3Kwwe3CiCPqJsTY5p8eDAK_N4j09KumqU25s-Fq-qzK92g03fYkvPhN_wabnXLqlQP1DVJaBuM7jVsCG0ZHr5xv8LK6YQRkiOPa3EkjXRmb4bK4bmS7V1ZaiOn0uO9_qRxjBPjLfw_aTQJN5W3KEm5XbWe5Dbe99TQXU3j_QP38bu5qk1MASnTWoL2kLhpu7WBa7Q0mYLjhNqNc_ckaXRvts8_eHEFCp-1qFeQHSHSosPYnTd46mBjaywZA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4bec225d06.mp4?token=ngiaG5hvFMbXV3G7T-bjw-kfCwOO22wlO8MQtENDjaX5vBvbZV8JJctVfMIJddzFOcHAQtwnDhoNS5iHaF9tkruGBGu3Kwwe3CiCPqJsTY5p8eDAK_N4j09KumqU25s-Fq-qzK92g03fYkvPhN_wabnXLqlQP1DVJaBuM7jVsCG0ZHr5xv8LK6YQRkiOPa3EkjXRmb4bK4bmS7V1ZaiOn0uO9_qRxjBPjLfw_aTQJN5W3KEm5XbWe5Dbe99TQXU3j_QP38bu5qk1MASnTWoL2kLhpu7WBa7Q0mYLjhNqNc_ckaXRvts8_eHEFCp-1qFeQHSHSosPYnTd46mBjaywZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
داده‌های جدید نشان می‌دهد که ترافیک دریایی از طریق تنگه هرمز پس از تفاهم‌نامه ایران و آمریکا از سر گرفته شده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 59.5K · <a href="https://t.me/alonews/128976" target="_blank">📅 21:09 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128975">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f_A0IWcGsQeVC4a0rqSG2aZ4oEPECQAGatgLQedTLerviliybBlfOZspu8KBuFzeDUQ5yLZoQkyPbfk0WA9VzKN7ByMweVxK0OGOl4HCiPloNm-9a4PDxBHlcAUskqaGMXx1Uhn0aoVGE2PNFMNfwhD1yn-JS83a5t_CHfjRu_eUvS01h3csbW3OS8e3lsJ_P4d7OVRnhIFD5NuZomOBkuqeavSS-U2T2Vv58i7Bt6GT8ckY049RLElFuhCLDJlWbCG-RMQTS1f4UD255PjOw3_bvu4j22LTf1UcsQxu7Cz1bC1mEmltn9QYINqBjC-B2Puz2rdwl9KRFkAnQXAN7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
خبرگزاری فارس:  پیام جدید رهبری منتشر شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 59.4K · <a href="https://t.me/alonews/128975" target="_blank">📅 21:07 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128974">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m-51rL8JuYNVdAf3hkPFi3e4pDuSsLoDcdDv3TTxpEu1GkJ7yAJqsmZgb0law4b1bBFnik7MRJLYKBe19-V16Ld2UoYqZ0Yu0loGEfT0Gahlfx48OZCbok8SdVVQ35q7hmIKK7cTQZOJyPd6sLXEeZqbSCydUJWJlHtDI_hsdfN9Hd9AiVnb3kFRJW_t3tjCznaGDTAx-iLMfVDGWSl2OrdF-4x4gJPTFdPfs04iZgYs9UkxVlpYVFSW_C3kzRYxls-WIZ23MhdsniuOZIOkPCdtSAPGC9khHVx4eUpjko9Tzw5yammNee8RCJFryNJNsC7YpgtgxXocp1XuXCweYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
بیت‌کوین به زیر ۶۳,۰۰۰ دلار سقوط کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 54.4K · <a href="https://t.me/alonews/128974" target="_blank">📅 21:02 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128973">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">👈
فایننشال‌تایمز: طبق توافق آمریکا و ایران، ایران به تدریج به ۶ میلیارد دلار از دارایی‌های مسدود شده خود در قطر دسترسی پیدا خواهد کرد
🔴
این پول فقط می‌تواند برای خرید کالاهای بشردوستانه و سایر کالاهای آمریکایی غیرتحریمی استفاده شود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/alonews/128973" target="_blank">📅 20:54 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128972">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">👈
خبرنگار : چه کسی آن صندوق ۳۰۰ میلیارد دلاری برای ایران را تأمین مالی می‌کند؟
🔴
جی.دی ونس : تمایل زیادی از سوی جهان عرب و همچنین از خارج از جهان عرب وجود دارد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 53.6K · <a href="https://t.me/alonews/128972" target="_blank">📅 20:53 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128971">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🔴
فوری / رئیس ستاد ارتش اسرائیل به ارتش اسرائیل دستور داد تا برای سناریوی حمله به ایران و حزب الله آماده شوند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 55.3K · <a href="https://t.me/alonews/128971" target="_blank">📅 20:48 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128970">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">👈
جی دی ونس: نتانیاهو بهتر است بداند بدون ترامپ و آمریکا قدرتی ندارد!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 54.9K · <a href="https://t.me/alonews/128970" target="_blank">📅 20:46 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128969">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">👈
ونس: تعداد نیرو‌های آمریکا در خاورمیانه را به سطح پیش از درگیری باز می‌گردانیم
🔴
برنامه ما این است که به سوئیس برویم؛ دقیقاً نمی‌دانم چه زمانی
🔴
درباره تأمین مالی صندوق ۳۰۰ میلیارد دلاری، تمایل زیادی در جهان عرب و خارج از آن وجود دارد که درگیر سرمایه‌گذاری در ایران شوند
🔴
در سه ماه گذشته، دو سوم تسلیحاتی که از اسرائیل محافظت کرده‌اند، با پول مردم آمریکا تأمین شده‌اند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 53.9K · <a href="https://t.me/alonews/128969" target="_blank">📅 20:39 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128968">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">👈
وزارت خزانه داری آمریکا تحریم های جدیدی را علیه حزب الله اعمال کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/alonews/128968" target="_blank">📅 20:37 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128967">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xw8DOvv5KboeYqXG9q-Q166BDF26lMQ72vaYC-Om7xOEqvoN4ni4WE35qkigFdVhdi1VMj4UhjiYdPxhQ81Gj7Y7tHpX5-_NB_RSyr-1NUcMNLcMxfwPB4qoyrfVVl7jC4-y_KAuxXVPT6qPABx_K98_iZE-dl-suN1A9T0XsmCS-EvaITanIcyu9fS_cbFze9frrYwrp0k5oIAOKLC9AQfnqruMCR8wGVdkvzQ9g43Mi3oxIvSFebIGX450nwv8UMOOfa94Zbz_vX-E0Ff-taEpou9TfbFxqtV-57Jh9FaQPyjAZzKADnHDVZMvrGMtxle1FlZp6fZrEM_Jdif8cw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
فوری / سنتکام : امروز، نیروهای آمریکایی بر اساس دستور رئیس‌جمهور، محاصره دریایی تمام ترددهای دریایی ورودی و خروجی به بنادر و مناطق ساحلی ایران را لغو کردند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 52.7K · <a href="https://t.me/alonews/128967" target="_blank">📅 20:33 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128966">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">👈
نرخ دیه سال ۱۴۰۵ اعلام شد!
🔴
رئیس قوه قضائیه با صدور بخشنامه‌ای، مبلغ دیه کامل در ماه‌های غیرحرام را برای سال ۱۴۰۵ تعیین کرد.
🔴
بر اساس این بخشنامه که در اجرای ماده ۵۴۹ قانون مجازات اسلامی مصوب سال ۱۳۹۲ و پس از انجام بررسی‌های لازم صادر شده است، مبلغ دیه کامل از ابتدای سال ۱۴۰۵ در ماه‌های غیرحرام، ۲۱ میلیارد ریال تعیین شده است.
🔴
این بخشنامه از سوی رئیس قوه قضائیه به مراجع قضایی سراسر کشور ابلاغ شده و از ابتدای سال ۱۴۰۵ ملاک محاسبه دیه خواهد بود.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 50.9K · <a href="https://t.me/alonews/128966" target="_blank">📅 20:31 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128965">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/le5y6NkIsyEHLWJCmPamzajrRTleSud9pGV_Tw1mPryWH9rIvYIituPoNfZLQR7MuG0t2biwAsmQoRv6OkQU3y4rpneK6umO3yamjmNigK8irbqL-Krpvv27-phEmSqGtbVLL4c4kNlWkycmSrHC7BZP0Z-_ZD5MW4tjv7CFjsQIqwE-HWzdVZpcAuGjzsCGWQD2_B_oficPHku_V0cU_gvjB_polmaXCl7Ainn21aEhOOSLT8RF2w9CbPbu65GouBsoDfptNUQabDXhBGfivlOHz_FC4WUMQipKBh-LH6Pqe5NOaEdOLW8qkLlG5A8IeCxftqDcZIpWpM5RmVRsrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ: هیچ پرداخت ۳۰۰ میلیارد دلاری از سوی آمریکا به ایران وجود ندارد. این اخبار جعلی است! همه چیزی که آمریکا دارد، موفقیت، کاهش قیمت نفت و پیروزی است. به بازار بورس نگاه کنید. تبلیغات دموکراتیک در حال اجرا است!!!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 48.7K · <a href="https://t.me/alonews/128965" target="_blank">📅 20:26 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128964">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">👈
ونس : من تنها کسی در کابینه هستم که نمی‌توانم اخراج شوم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 49.9K · <a href="https://t.me/alonews/128964" target="_blank">📅 20:19 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128963">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">👈
جی‌دی ونس درباره ایران:
من معمولاً نسبت به درگیری‌های نظامی بی‌پایان بسیار بدبین هستم.
🔴
فکر می‌کنم این مورد متفاوت بود چون واقعاً هدف مشخص و پایان روشنی داشت
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 48.3K · <a href="https://t.me/alonews/128963" target="_blank">📅 20:18 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128962">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1b7e326eb5.mp4?token=Zget0VgOu4B_4w1ej_qxGHfm8OV98iV5txCb3CpZ6R6DWNAbmo1jsFAcH79Z9pAr3sXu7At9cjgHbmIA3ylUsJQolXpRUwejTBKUhuEjU574COIs63sYseU0VRO0S6_jNgYLe4Y72eH8XxNChhRdhUiip-DeH0bdMUKJg5oLPDYr-5LjBSAflkrV_VB8BDy48UXxQ_07KRP3PXDvRSVePHivBM6MRJAuJTpiVE75i1tYGXuW-fB54ng4m_hUBSnYIrsCzcN9ZkvXliCLx2BineIWmOnyc6ViIA_aiVc5os03ZLOu65mrvDdp9dIrR5WFS1zlOj6CeRSTHeSkmWG9zDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1b7e326eb5.mp4?token=Zget0VgOu4B_4w1ej_qxGHfm8OV98iV5txCb3CpZ6R6DWNAbmo1jsFAcH79Z9pAr3sXu7At9cjgHbmIA3ylUsJQolXpRUwejTBKUhuEjU574COIs63sYseU0VRO0S6_jNgYLe4Y72eH8XxNChhRdhUiip-DeH0bdMUKJg5oLPDYr-5LjBSAflkrV_VB8BDy48UXxQ_07KRP3PXDvRSVePHivBM6MRJAuJTpiVE75i1tYGXuW-fB54ng4m_hUBSnYIrsCzcN9ZkvXliCLx2BineIWmOnyc6ViIA_aiVc5os03ZLOu65mrvDdp9dIrR5WFS1zlOj6CeRSTHeSkmWG9zDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
جی‌دی ونس درباره ایران: ایرانی‌ها پیشنهاداتی ارائه می‌دهند که حتی شش ماه پیش هم در حد رویا بود. پس بیایید این مذاکره را ادامه دهیم.
🔴
ببینیم آیا اقدامات ایرانی‌ها واقعاً با گفته‌هایشان مطابقت دارد و کمی به ایالات متحده آمریکا اعتبار بدهیم، کشوری که به نظر من مدت‌هاست شریک فوق‌العاده‌ای برای دولت اسرائیل بوده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 46.7K · <a href="https://t.me/alonews/128962" target="_blank">📅 20:16 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128961">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">👈
ونس: مقدار دقیق دارایی‌های مسدودشدۀ ایران را نمی‌دانم
🔴
اعدادی بیش از ۱۰۰ میلیارد دلار شنیده‌ام. حتی اعدادی بیش از ۲۰۰ میلیارد دلار.
🔴
بخش عمدۀ این پول در حساب‌های ایالات متحده نیست؛ بیشتر آن یا در کشورهای حاشیه خلیج فارس است، یا در اروپا، یا در جاهای دیگر.
🔴
اما مقدار دقیق این پول را نمی‌دانم؛ فقط می‌دانم که رقم بسیار بزرگی است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/alonews/128961" target="_blank">📅 20:12 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128960">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e65fb14352.mp4?token=QchKiwy9vb176QOdPU6knR5yaXIGzNAVIvCgTMI6DTkH8yvXiIDHJZ8mCa0qvxIBgFcZolpxD3aUTBRSfsM49pw4bun62keu2AvQNYH90IIi0A-eQcC01DyDn442jqN5tkia1NHkfov_Qb-147c7cLLWyGQtqtGaiNp1HRrL7h-LT3tJ_-QhwTULzhClQoznY2gVzSRtoBTJKAucDEl0q9V6hwLCxW4xd05ncMEWb73f-P8Z3nnEmV32-4eTtJsjVm9eIEeM6gy87WOwnvlz55-Fw0cpPkJpu-NVlyCeVJV4hdW5QaapMq-y_5nqiH01Q3I4qUZqUfgQDG6R_w4qzw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e65fb14352.mp4?token=QchKiwy9vb176QOdPU6knR5yaXIGzNAVIvCgTMI6DTkH8yvXiIDHJZ8mCa0qvxIBgFcZolpxD3aUTBRSfsM49pw4bun62keu2AvQNYH90IIi0A-eQcC01DyDn442jqN5tkia1NHkfov_Qb-147c7cLLWyGQtqtGaiNp1HRrL7h-LT3tJ_-QhwTULzhClQoznY2gVzSRtoBTJKAucDEl0q9V6hwLCxW4xd05ncMEWb73f-P8Z3nnEmV32-4eTtJsjVm9eIEeM6gy87WOwnvlz55-Fw0cpPkJpu-NVlyCeVJV4hdW5QaapMq-y_5nqiH01Q3I4qUZqUfgQDG6R_w4qzw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ویدیو پربازدید از یک‌ مخالف توافق بعد امضا
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 43.6K · <a href="https://t.me/alonews/128960" target="_blank">📅 20:12 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128959">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">👈
ونس: امکان تعلیق موقت تحریم‌های ایران بدون مصوبه کنگره وجود دارد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/alonews/128959" target="_blank">📅 20:11 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128958">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">👈
ونس درباره نتانیاهو: من گزارش Axios را دیدم که می‌گوید نتانیاهو عصبانی است.این بازتابی از گفتگوهایی که من با او داشته‌ام نیست. شاید او چیزی به شخص دیگری می‌گوید که به من نمی‌گوید.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 43.2K · <a href="https://t.me/alonews/128958" target="_blank">📅 20:05 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128957">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">👈
اننقاد تند جی. دی. ونس به بن‌گویر و اسموتریچ: شما افرادی را در ساختار سیاسی اسرائیل دیده‌اید، بن‌گویر و اسموتریچ، که به این توافق حمله کرده‌اند.
🔴
و فکر می‌کنم پاسخ من به آن‌ها این خواهد بود: پیشنهاد دقیق شما چیست؟
🔴
شما کشوری با ۹ میلیون نفر جمعیت هستید. نمی‌توانید صرفاً با کشتن، از پسِ حل تک‌تک مشکلات امنیت ملی‌تان برآیید
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/alonews/128957" target="_blank">📅 20:02 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128956">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">👈
فارس: پیام بسیار مهم رهبر انقلاب دربارهٔ تفاهم پایان جنگ، خطاب به مردم ایران، تا ساعتی دیگه منتشر میشه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 43.4K · <a href="https://t.me/alonews/128956" target="_blank">📅 20:01 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128955">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/18aeee1535.mp4?token=DSjyP_LOhnSncgLMKpVqTinMheWY-1PjKYKbWF7BswdBHATGSgU0tu4jgIXbD4wNN_GUcZSzzad5ggAtT2OXCd2weYMOVWbiKD3if3iEATiBLrGDx7ol-2D-XjBWCoyF_v3jh1_QQaDUzwADEk-S5NtrokMuwvkrKJP8NmA5vPddBli6LD4rKXdloorHVg5t-GiYVyp_uoQVtbJLuE0pp2pQk4snuEmBEeWX5TlVclf8Pnm1K0Yw45tObErDAuOaabhW-QNYOm5wUlCRW9s3Jmn3F20IBrtnxaxk6UjoWM2QKJLwhhCICwNBgg0SK0-2rHYuZaeCFGM6Gg3xmopKfhjsFuM-jcDZSRBXSQxbhQ2HGWZGH20HZhFZbPlUbcJbhM8TgXYWgb2n58crZrGdPEPtQnoRiIW60cXmWY_cIfryfpXIKGKrWDMGorrWgJzys6pm1PiDB9n91LnxBApbsbx5MzjPhM3PIG6khv_0qeER3UQZmU6VLoNkdyzwXj7pEjQ8eFtoWVNATL4cUpKUqdBzCr55IwDq1RopzD0ywznve3rBJDwlYMyZF_M-ox4fHoNzuEcEp10-pTdbRM3TZyhh4CTybpc9ZN6f2BTvZY8yFOhxjO5GTfU4Ich0_7ggC8AYCxGXZtEXrf13w1POvfDfPihxVxks6u1G1d-IGAU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/18aeee1535.mp4?token=DSjyP_LOhnSncgLMKpVqTinMheWY-1PjKYKbWF7BswdBHATGSgU0tu4jgIXbD4wNN_GUcZSzzad5ggAtT2OXCd2weYMOVWbiKD3if3iEATiBLrGDx7ol-2D-XjBWCoyF_v3jh1_QQaDUzwADEk-S5NtrokMuwvkrKJP8NmA5vPddBli6LD4rKXdloorHVg5t-GiYVyp_uoQVtbJLuE0pp2pQk4snuEmBEeWX5TlVclf8Pnm1K0Yw45tObErDAuOaabhW-QNYOm5wUlCRW9s3Jmn3F20IBrtnxaxk6UjoWM2QKJLwhhCICwNBgg0SK0-2rHYuZaeCFGM6Gg3xmopKfhjsFuM-jcDZSRBXSQxbhQ2HGWZGH20HZhFZbPlUbcJbhM8TgXYWgb2n58crZrGdPEPtQnoRiIW60cXmWY_cIfryfpXIKGKrWDMGorrWgJzys6pm1PiDB9n91LnxBApbsbx5MzjPhM3PIG6khv_0qeER3UQZmU6VLoNkdyzwXj7pEjQ8eFtoWVNATL4cUpKUqdBzCr55IwDq1RopzD0ywznve3rBJDwlYMyZF_M-ox4fHoNzuEcEp10-pTdbRM3TZyhh4CTybpc9ZN6f2BTvZY8yFOhxjO5GTfU4Ich0_7ggC8AYCxGXZtEXrf13w1POvfDfPihxVxks6u1G1d-IGAU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
انتقاد ونس به اسرائیل
🔴
ونس : در سه ماه گذشته، دو سوم از جنگ‌افزارهای دفاعی که از اسرائیل محافظت کرده، با دستان آمریکایی ساخته شده و با دلارهای مالیات‌دهندگان آمریکایی پرداخت شده است.مشکل اسرائیل دونالد جی. ترامپ نیست، و هر کسی در اسرائیل که فکر می‌کند بزرگترین مشکلشان رئیس‌جمهور ایالات متحده است، باید بیدار شود و واقعیت وضعیتی را که آن کشور در آن قرار دارد، حس کند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 44.3K · <a href="https://t.me/alonews/128955" target="_blank">📅 19:55 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128954">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fb7cd6ba7c.mp4?token=qI48mjk3fBrDwFbZgcEhkkI_OzRmp8sc69bCnEmhg_s5InrNc6OEZ0NNR7Drp7HH3QLloxHuAVUX9OtCCaw-U7xeYv2GaMgrlYAVWq466HZjwLn7fDt2zp_Vj38w6fnFuRaEkb7CEkOEpPZCDpsW8afBC_A-1KyUspyJGQe1C6_EgO7tznM_MtVjJnlE3h61p1bpIB_CcL7cCKw8VEuK_E9qRksIK45XyT7b_zbkjxK3a5imGHlXdEoaEAnXEY8k1eD0PSVD-bM5sw1NZ0zPKUCnjpW4eoyItypPeRrNEEAfkpwICWU3vBm0O9rz3IIrQ-Ymf4dHiruxQ8G-VZLb_Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fb7cd6ba7c.mp4?token=qI48mjk3fBrDwFbZgcEhkkI_OzRmp8sc69bCnEmhg_s5InrNc6OEZ0NNR7Drp7HH3QLloxHuAVUX9OtCCaw-U7xeYv2GaMgrlYAVWq466HZjwLn7fDt2zp_Vj38w6fnFuRaEkb7CEkOEpPZCDpsW8afBC_A-1KyUspyJGQe1C6_EgO7tznM_MtVjJnlE3h61p1bpIB_CcL7cCKw8VEuK_E9qRksIK45XyT7b_zbkjxK3a5imGHlXdEoaEAnXEY8k1eD0PSVD-bM5sw1NZ0zPKUCnjpW4eoyItypPeRrNEEAfkpwICWU3vBm0O9rz3IIrQ-Ymf4dHiruxQ8G-VZLb_Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
خبرنگار: چه کسی آن صندوق 300 میلیارد دلاری برای ایران را تأمین مالی می‌کند؟
🔴
جی‌دی ونس: تمایل زیادی از سوی جهان عرب و فراتر از جهان عرب وجود دارد که اگر ایران به‌درستی رفتار کند، واقعاً در آن کشور مشارکت کنند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 43.3K · <a href="https://t.me/alonews/128954" target="_blank">📅 19:53 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128953">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">👈
جی دی ونس: ما یکشنبه با ایران توافق را امضا کردیم اما نمیدانم به چه علت، ایرانی ها از ما خواستند که تا روز جمعه متن آن منتشر نشود البته شاید به خاطر تهیه یک متن فارسی
🔴
اقتصاد ایران رو به فروپاشی است و تورم آن سر به فلک کشیده است و یک هزار میلیارد از جنگ آسیب دیده بنابراین فروش چند میلیون بشکه نفت نمیتواند تاثیر خاصی داشته باشد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 43.7K · <a href="https://t.me/alonews/128953" target="_blank">📅 19:44 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128952">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e45fd9b924.mp4?token=uphf3r0lACQH5YMYCViLNrGR39b3U76tSmmG78aZDsGHix_qdyP2SrGgKnrohy_rCd0uoi_5ozYqznXJuotUOQeljEhcJsNdVGi2YFwAchB-YRdomjk8gIvFqtAs0lAE271FWyeyJCZuofHK19SPDZQ1vXGyx16IxQg2xwiHk0bXln_gVPRc784-_iA3zHsqf8mF_6-7D94XOiqAU39hOUAixeNY1eldO6WrC64nWF2nBIr0O3uggsGcQbE20oDh2LOUMYgw7dK8P04KXUoAZVJwmztjQis4zi3VfD7yD5hzFpPz7sdeD37R34uQUg1TONhlMdUVOXAiewo5iFP--w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e45fd9b924.mp4?token=uphf3r0lACQH5YMYCViLNrGR39b3U76tSmmG78aZDsGHix_qdyP2SrGgKnrohy_rCd0uoi_5ozYqznXJuotUOQeljEhcJsNdVGi2YFwAchB-YRdomjk8gIvFqtAs0lAE271FWyeyJCZuofHK19SPDZQ1vXGyx16IxQg2xwiHk0bXln_gVPRc784-_iA3zHsqf8mF_6-7D94XOiqAU39hOUAixeNY1eldO6WrC64nWF2nBIr0O3uggsGcQbE20oDh2LOUMYgw7dK8P04KXUoAZVJwmztjQis4zi3VfD7yD5hzFpPz7sdeD37R34uQUg1TONhlMdUVOXAiewo5iFP--w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ چند روز دیگه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 45.2K · <a href="https://t.me/alonews/128952" target="_blank">📅 19:33 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128951">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">👈
جی دی ونس در مورد اسرائیل: به نظر می‌رسد که ما درست در آستانهٔ یک پیشرفت بزرگ در توافق بودیم، و بعد ناگهان یک انفجار بزرگ در یک منطقهٔ غیرنظامی در بیروت رخ می‌دهد، و تعداد زیادی از مردم که هیچ ارتباطی با حزب‌الله ندارند جان خود را از دست می‌دهند. این قابل قبول نیست.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/alonews/128951" target="_blank">📅 19:24 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128950">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/961d1c224f.mp4?token=f0zdeBGEhQZ19iUgTGOzc2Jo8U1JEmxlxMhXZmBM3v3qJQkKjw-kaBlqJ2LJ4o2BbpHH-3eDFmxNcTgTOXxZlt1jNOYfmml0a6nKFPlsI4tpQtA1YZwZs1jBH_xKoKXjXf_ECMpHAyPyoSMM93McuaQbCiID1W38hz7pfxRHYY04c22MxE72FvQbTR2FNh1dwlWMSejb-w91vwjNs087wh9o4ujvDlH_h1KnG05-eycKI4_UyIgQ93bFjK06h2mv8RqIwDIjpOOAtOKXzJDvQ-0rBYSJdYJ9ztn2uFH0Tu0oWHOr5SQnXm2aaAdYtxHNH9xvVAwU-8TFrUbe0PkdK0sHXFAO7wGFnYx_tXNlzdQXKC0GhtfiUXsQCn5XJkEgBn0ILSSBR2mNV5N82F14QgALhu4EVGsfY3p3a-ZIwe8x-CsL-oBfDM1IEB6WHnzNKbQTt23a5uct5_FPWh7AlsPF-Mt-tQcq3vXtmnxjsq2afy-tgMCD7ZKro5--Lp55evrV1YOGGhvDJTJ2fCoCxWLvvsjBNny3VZ0mCn8KipUXiqIFiNp71uo1pNjLThZ-i5vmr6dLndnhCjdCZGIFHammRHW_-EVNqG1f43Kt0OSKDrEc_4hU2QdefG1Bo54p_mx0coQLzr3OuFAfXNtIqBfAyYDlmSDmQNPPs6y6S4E" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/961d1c224f.mp4?token=f0zdeBGEhQZ19iUgTGOzc2Jo8U1JEmxlxMhXZmBM3v3qJQkKjw-kaBlqJ2LJ4o2BbpHH-3eDFmxNcTgTOXxZlt1jNOYfmml0a6nKFPlsI4tpQtA1YZwZs1jBH_xKoKXjXf_ECMpHAyPyoSMM93McuaQbCiID1W38hz7pfxRHYY04c22MxE72FvQbTR2FNh1dwlWMSejb-w91vwjNs087wh9o4ujvDlH_h1KnG05-eycKI4_UyIgQ93bFjK06h2mv8RqIwDIjpOOAtOKXzJDvQ-0rBYSJdYJ9ztn2uFH0Tu0oWHOr5SQnXm2aaAdYtxHNH9xvVAwU-8TFrUbe0PkdK0sHXFAO7wGFnYx_tXNlzdQXKC0GhtfiUXsQCn5XJkEgBn0ILSSBR2mNV5N82F14QgALhu4EVGsfY3p3a-ZIwe8x-CsL-oBfDM1IEB6WHnzNKbQTt23a5uct5_FPWh7AlsPF-Mt-tQcq3vXtmnxjsq2afy-tgMCD7ZKro5--Lp55evrV1YOGGhvDJTJ2fCoCxWLvvsjBNny3VZ0mCn8KipUXiqIFiNp71uo1pNjLThZ-i5vmr6dLndnhCjdCZGIFHammRHW_-EVNqG1f43Kt0OSKDrEc_4hU2QdefG1Bo54p_mx0coQLzr3OuFAfXNtIqBfAyYDlmSDmQNPPs6y6S4E" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
جی.دی. ونس در مورد لغو تحریم‌ها:
«راستش را بخواهید، ما این را یک امتیاز بزرگ به ایرانی‌ها ندیدیم — ایران هم... این را به‌عنوان یک امتیاز برای خودشان تلقی نکرد، چون چیزی که مانع فروش نفت آنها می‌شد، تحریم‌ها نبود.
🔴
آنها بدون هیچ تخفیفی نفت زیادی می‌فروختند، چون تحریم‌ها اساساً ناکارآمد بودند.
🔴
در آن مرحله، کاری که تحریم‌ها کردند این بود که سیستم مالی ایران را به نوعی به سمت سیستم بانکی سایه‌ای (غیررسمی) سوق دادند.
🔴
با لغو تحریم‌ها، در واقع خواهیم توانست کمی ببینیم که سیستم مالی آنها پول را به کجا می‌فرستد و از کجا پول دریافت می‌کند. این یک مزیت واقعی است.»
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 44.4K · <a href="https://t.me/alonews/128950" target="_blank">📅 19:23 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128949">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">👈
جی‌دی ونس درباره لبنان: ما انتظار داریم حزب‌الله راکت‌ها و پهپادهایی به سمت اسرائیلی‌ها شلیک نکند و همچنین انتظار داریم اسرائیلی‌ها در لبنان به شدت عمل نکنند.
🔴
هر دو طرف باید به تعهدات خود پایبند باشند.
🔴
همان‌طور که می‌دانید، گاهی این آتش‌بس‌ها کمی پیچیده هستند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 42.3K · <a href="https://t.me/alonews/128949" target="_blank">📅 19:14 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128948">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/98cffc6fa1.mp4?token=usms1VtWb2C-UJtFIShN1ijAJDQGFogE7aZP-m0lVUuKZ1bA0yaJlSSXGr7HJoh-dSaND1ROHFHYEVqXH2fnxUgZSb1xActYh5VuMzl6z8vhPctF6UIu6Cqu3fWqKrgp0jzyohehd3n7hmvplzY5voHEf-N8WjlSXpPsDKnD8eM3JLCnuxQPmlCiSciM_LUPFxAO3AdoTrWMraRRgAUJ16smJDvbJlR7KxHyBoMW8wDRU0UkHCSl_gXi3zQn4SRGfUqwOpla29gQ4omY4jPRU1qqSKpXxdTQmi81xbF-xzMcro3_8CErOss8QlmyIqTJ8zWszwTZXFrBoJCpd-eQrlI5mu-QBxU66i6wZC0hJgOm9nFj7P7azuZDTF4S1395QWk4XVx_0Tgnj4sQo9u7Cp_zJL4vjFlk3Pz64Zc6gafONoMH2yazZnfx-6LFTa-XNb_Z5DZTnHcx5Ey9LgeV7sONtnY8I2Yv9rtL1Gcqzhto_kk65W6eN-h051i_cxy0ircUq8NoyavSqEw-p_61xfQwPshCJPZFoMTowh67KbfSatswguHJu77yPANiEBDGYmCmScxk8RBCWtNNe9oiS0amJQDqZxjlsflxCgJ8MzmlBhZZD6xud4arfndYfWeg2rJLypwnKjMeAh_wSufOOYdzScHqHKMGZx3W7U3p374" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/98cffc6fa1.mp4?token=usms1VtWb2C-UJtFIShN1ijAJDQGFogE7aZP-m0lVUuKZ1bA0yaJlSSXGr7HJoh-dSaND1ROHFHYEVqXH2fnxUgZSb1xActYh5VuMzl6z8vhPctF6UIu6Cqu3fWqKrgp0jzyohehd3n7hmvplzY5voHEf-N8WjlSXpPsDKnD8eM3JLCnuxQPmlCiSciM_LUPFxAO3AdoTrWMraRRgAUJ16smJDvbJlR7KxHyBoMW8wDRU0UkHCSl_gXi3zQn4SRGfUqwOpla29gQ4omY4jPRU1qqSKpXxdTQmi81xbF-xzMcro3_8CErOss8QlmyIqTJ8zWszwTZXFrBoJCpd-eQrlI5mu-QBxU66i6wZC0hJgOm9nFj7P7azuZDTF4S1395QWk4XVx_0Tgnj4sQo9u7Cp_zJL4vjFlk3Pz64Zc6gafONoMH2yazZnfx-6LFTa-XNb_Z5DZTnHcx5Ey9LgeV7sONtnY8I2Yv9rtL1Gcqzhto_kk65W6eN-h051i_cxy0ircUq8NoyavSqEw-p_61xfQwPshCJPZFoMTowh67KbfSatswguHJu77yPANiEBDGYmCmScxk8RBCWtNNe9oiS0amJQDqZxjlsflxCgJ8MzmlBhZZD6xud4arfndYfWeg2rJLypwnKjMeAh_wSufOOYdzScHqHKMGZx3W7U3p374" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
خبرنگار: رئیس‌جمهور ترامپ دیروز گفت که اگر مذاکرات این دور به مشکل بخورد، شما را مقصر خواهد دانست. آیا نگرانید که او بخواهد شما را قربانی کند؟
🔴
جِی‌دی ونس: نه، اصلاً. منظورم این است که فکر می‌کنم رئیس‌جمهور شوخی می‌کرد، همان‌طور که اغلب اوقات این کار را می‌کند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 41.6K · <a href="https://t.me/alonews/128948" target="_blank">📅 19:13 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128947">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">👈
جی‌دی ونس از "حق دفاع از خود" و حق داشتن موشک‌های بالستیک ایران حمایت می‌کند: «اسرائیل اگر حزب‌الله به سمت اسرائیل موشک یا پهپاد شلیک کند، از حق دفاع از خود دست نمی‌کشد. ایرانی‌ها هم از حق دفاع از خود در کشورشان دست نمی‌کشند.»
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 40.7K · <a href="https://t.me/alonews/128947" target="_blank">📅 19:11 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128946">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">👈
جی‌دی ونس درباره ایران: من می‌گویم دوره ۶۰ روزه رسماً امروز آغاز شده است.
🔴
پس بله، توافق دیروز شروع شد — ما امروز ساعت ۶۰ روزه را شروع خواهیم کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/alonews/128946" target="_blank">📅 19:11 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128945">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">👈
جِی‌دی ونس درباره ایران
:
من کسانی را دیده‌ام که به این توافق شک دارند — افرادی که می‌گویند ایرانی‌ها هرگز رفتار خود را تغییر نخواهند داد.
🔴
خب، شاید این درست باشد، و اگر چنین باشد، آن‌ها هیچ یک از مزایای این معامله را دریافت نمی‌کنند. اما آیا ارزش امتحان کردن ندارد؟
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 39.4K · <a href="https://t.me/alonews/128945" target="_blank">📅 19:10 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128944">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9e0fa45935.mp4?token=bDyjoVCopxkqbl9GaelHyZBfd0N_OgMRcvpm1M-TvBYqF1yIiDwia-gaFDOOUhQT_96Vy_O1UOlhC0XnLuKeBQr7DwHRDyo2aWqGyw4QXKp1fdSvptBL0N7HzAbYy73ddhpTrH4UzE5WX1NYOOfJLnDsdqudOcdTLQtvv5lHQJUOxoRqq4bWuvY_GMj_aCxfMFQQW4m0KZmWG-58XX3OaR5c0RbrpoUHrvBMUHs5M7kCT5SWkqsmW5Bwr2OJTCBtXGSS6WBPwG7HwMELG2IthrD2R2WVLE5ik8gxwFpoeDLhirXEkeGtAICNIbIpIM89hgF8efhLOQTxf14MU0s6b1wN-WQ6In5LVcniJXHD1fQCNshIudeFZcL8YR3Q4KRh27G_mpB5qHed5Gd2E4QNibnfCSp8XA0CL7wMMLiHF77ilpcBXwWDk-OMK7zdKkO38ScFeRpZcbw8lECD_x7HVfsMnti0yPozYNDbFdLrACZ18f3x74_fAla9hfynn8c0vhKHtAD44ncP4eVZ_CmgIdWbMoQBrevwhPkcenKdDWjcs_CUDFUhk0MLcgaA2EZV3jvXzt-PiKeZS2ajWdgmu7UTbp-VxFi36PurAshNUyeSCuOEwHTsLc5-l2oxR1OHSQTBz4vdLXHtnxKJ7n3osaj-KlITp0L7D09WaSuiQfM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9e0fa45935.mp4?token=bDyjoVCopxkqbl9GaelHyZBfd0N_OgMRcvpm1M-TvBYqF1yIiDwia-gaFDOOUhQT_96Vy_O1UOlhC0XnLuKeBQr7DwHRDyo2aWqGyw4QXKp1fdSvptBL0N7HzAbYy73ddhpTrH4UzE5WX1NYOOfJLnDsdqudOcdTLQtvv5lHQJUOxoRqq4bWuvY_GMj_aCxfMFQQW4m0KZmWG-58XX3OaR5c0RbrpoUHrvBMUHs5M7kCT5SWkqsmW5Bwr2OJTCBtXGSS6WBPwG7HwMELG2IthrD2R2WVLE5ik8gxwFpoeDLhirXEkeGtAICNIbIpIM89hgF8efhLOQTxf14MU0s6b1wN-WQ6In5LVcniJXHD1fQCNshIudeFZcL8YR3Q4KRh27G_mpB5qHed5Gd2E4QNibnfCSp8XA0CL7wMMLiHF77ilpcBXwWDk-OMK7zdKkO38ScFeRpZcbw8lECD_x7HVfsMnti0yPozYNDbFdLrACZ18f3x74_fAla9hfynn8c0vhKHtAD44ncP4eVZ_CmgIdWbMoQBrevwhPkcenKdDWjcs_CUDFUhk0MLcgaA2EZV3jvXzt-PiKeZS2ajWdgmu7UTbp-VxFi36PurAshNUyeSCuOEwHTsLc5-l2oxR1OHSQTBz4vdLXHtnxKJ7n3osaj-KlITp0L7D09WaSuiQfM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
جِی‌دی ونس درباره ایران: در ایران تقسیمات واقعی وجود دارد.
🔴
آنچه در چند ماه گذشته دیده‌ایم این است که عمل‌گرایان درون نظام ایران — افرادی که واقعاً می‌خواهند رابطه خود را با خاورمیانه و جهان تغییر دهند — در حال پیروزی در این بحث هستند.
🔴
ایالات متحده می‌خواهد این افراد در این بحث پیروز شوند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 38K · <a href="https://t.me/alonews/128944" target="_blank">📅 19:09 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128943">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🔴
فوری / ونس: ما در حال حاضر یک تحریم اقتصادی فلج‌کننده علیه ایران اعمال می‌کنیم و تا زمانی که این کشور رفتار خود را به‌طور اساسی تغییر ندهد، به آن پایان نخواهیم داد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 37.6K · <a href="https://t.me/alonews/128943" target="_blank">📅 19:08 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128942">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">👈
جی‌دی ونس درباره ایران: برای بخش نظامی، چند نکته وجود دارد که همچنان درست است و چه ایرانی‌ها با بقیه توافق همکاری کنند یا نکنند، این نکات پابرجا خواهند بود.
🔴
برنامه هسته‌ای آن‌ها کاملاً نابود شده است. ظرفیت غنی‌سازی آن‌ها، تأسیساتی که برای توسعه غنی‌سازی و ساخت احتمالی سلاح هسته‌ای استفاده می‌کردند، همچنان نابود شده است.
🔴
نیروی نظامی متعارف آن‌ها همچنان نابود شده است. ظرفیت آن‌ها برای تهدید همسایگانشان عمدتاً از بین رفته است.
🔴
اکنون می‌بینیم که آیا آن‌ها مایل به رعایت گام بعدی طرح صلح رئیس‌جمهور هستند یا خیر
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/alonews/128942" target="_blank">📅 19:07 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128941">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/adf09694b6.mp4?token=oOpZ_yxsT-MPC7cKrwCfy6ND8me87eh87k3yHnCjH6wZ7v8VSMxlngBwiSL-PbYpGRU0-QyiAoDOwII2bR9zaH5dFfSnFM-EEbYN8Au-JaF5Q0GJcgRLQsSZikSWePKurn_er4Vh3Fil6a4zV6byeLgadt28uigaVxpOamWvOQ0Kg5SbSOdbrHD5lCU356q614dI-SX4Y7a0UGOuMViCerl_FlyHVclVecmx3ltyMN4rdqKP-O436onWtw3JQVlZAMyvh8CTPHNTk0qOWCeaVUNWi2Bb0emu27okTzVYBJ5rbkfngS7uwYpisAuY3udg2WJ0EyGTkCDbn7pV_8A1Tw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/adf09694b6.mp4?token=oOpZ_yxsT-MPC7cKrwCfy6ND8me87eh87k3yHnCjH6wZ7v8VSMxlngBwiSL-PbYpGRU0-QyiAoDOwII2bR9zaH5dFfSnFM-EEbYN8Au-JaF5Q0GJcgRLQsSZikSWePKurn_er4Vh3Fil6a4zV6byeLgadt28uigaVxpOamWvOQ0Kg5SbSOdbrHD5lCU356q614dI-SX4Y7a0UGOuMViCerl_FlyHVclVecmx3ltyMN4rdqKP-O436onWtw3JQVlZAMyvh8CTPHNTk0qOWCeaVUNWi2Bb0emu27okTzVYBJ5rbkfngS7uwYpisAuY3udg2WJ0EyGTkCDbn7pV_8A1Tw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
آمریکا حتی یک سنت هم به ایران نمی‌دهد / جی‌دی ونس: "آنچه از همه شما می‌خواهم این است که صادقانه گزارش دهید که ایالات متحده حتی یک سنت هم به ایران نمی‌دهد...حتی مزایای اقتصادی، کاهش تحریم‌ها و غیره که با این معامله همراه است، فقط در صورتی اتفاق می‌افتد که ایرانی‌ها عمل کنند!"
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 38.3K · <a href="https://t.me/alonews/128941" target="_blank">📅 19:06 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128940">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">👈
جِی‌دی ونس درباره ایران: فکر می‌کنم طرح صلح رئیس‌جمهور در ایران در حال حاضر برای مردم آمریکا ثمرات واقعی به همراه دارد.
🔴
دیشب، ۱۲.۵ میلیون بشکه نفت از تنگه هرمز عبور کرد.
🔴
این بالاترین میزان از آغاز درگیری است.
🔴
ایرانی‌ها برای دومین شب متوالی به هیچ کشتی‌ای در تنگه هرمز شلیک نکردند. تا کنون، به تعهد خود پایبند بوده‌اند.
🔴
سنتکام اجازه داده است که دوازده کشتی از محاصره دریایی ما عبور کنند، بنابراین ما نیز به تعهد خود عمل می‌کنیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 39.1K · <a href="https://t.me/alonews/128940" target="_blank">📅 19:01 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128939">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8e783b213a.mp4?token=PciLHajQzu0oxFqwe2r8R7vreMKi8uIcQO5mwbaCkCaC89qwTvtltgqtZUTQBod5F7QvgRQfN_aP-DincmPJmcpYHYBjbGtRFEyfUiTq-QMRHkrTVk6rdFMaRzktoTHXCZkp8-Gm0MAha0o2O_oiLqKyJjeJ-IBmGABJ8leWIk0LUPvnV9UVZFZO8mbROKiRze0ZGsfJObvXz4TaihNwYjIpGZKBXBdGNFIviSGYzhZgFlvkwryudpOq9vzAMkynmARUa8L5HZYkfL8CvNvfqGr3xUS-wN81dlQX4V5Du4gY60062ZqwF-5ByB5vyL6gIa5qnupqwLOKK06ziX0HbA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8e783b213a.mp4?token=PciLHajQzu0oxFqwe2r8R7vreMKi8uIcQO5mwbaCkCaC89qwTvtltgqtZUTQBod5F7QvgRQfN_aP-DincmPJmcpYHYBjbGtRFEyfUiTq-QMRHkrTVk6rdFMaRzktoTHXCZkp8-Gm0MAha0o2O_oiLqKyJjeJ-IBmGABJ8leWIk0LUPvnV9UVZFZO8mbROKiRze0ZGsfJObvXz4TaihNwYjIpGZKBXBdGNFIviSGYzhZgFlvkwryudpOq9vzAMkynmARUa8L5HZYkfL8CvNvfqGr3xUS-wN81dlQX4V5Du4gY60062ZqwF-5ByB5vyL6gIa5qnupqwLOKK06ziX0HbA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
غرفه نقطه آتش اوکراین در یوروساتوری ۲۰۲۶ در پاریس، حملات پهپادی FP-1 و FP-2 امروز به پالایشگاه مسکو روسیه را به نمایش می‌گذارد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 39.3K · <a href="https://t.me/alonews/128939" target="_blank">📅 18:55 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128938">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">👈
پزشکیان: تلاش‌های پاکستان در مسیر دستیابی به توافق پایان جنگ در حافظه ملت ایران ماندگار خواهد شد
🔴
شهباز شریف: صبر، استقامت و رویکرد مبتنی بر عقلانیت و تدبیر مسئولان و ملت ایران ستودنی است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 41.3K · <a href="https://t.me/alonews/128938" target="_blank">📅 18:50 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128937">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">👈
علی‌هاشم، خبرنگار الجزیره: مسعود پزشکیان شاید تنها رئیس‌جمهور ایران باشد که چندین حیات سیاسی مختلف را در یک دوره تجربه کرده است
🔴
به قدرت رسیدن پس از جان باختن رئیس‌جمهور قبلی در سقوط هلیکوپتر
🔴
ترور اسماعیل هنیه در مراسم تحلیف
🔴
حمله مستقیم ایران به اسرائیل
🔴
سقوط سوریه، ترور نصرالله و حمله به ایران
🔴
شعله‌ور شدن اعتراضات
🔴
تغییر رهبری در شرایط جنگی
🔴
امضای توافق صلح با آمریکا
🔴
در دوران پزشکیان، ایران هرگز از حرکت و گذار از یک مرحله به مرحله‌ای دیگر باز نایستاده است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/alonews/128937" target="_blank">📅 18:48 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128936">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🔴
فوری / معاون نخست‌وزیر و وزیر خارجه پاکستان: از آنجا که یادداشت تفاهم میان آمریکا و ایران به‌صورت مجازی امضا شده است، مراسم رسمی امضای آن که قرار بود روز جمعه در سوئیس برگزار شود، لغو شده است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 41.1K · <a href="https://t.me/alonews/128936" target="_blank">📅 18:45 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128935">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">👈
یک منبع: بررسی اصلاحیه قیمت‌های ایران خودرو نشان می‌دهد که نرخ نهایی اکثر محصولات این شرکت بدون تغییر باقی مانده و تنها چند خودرو با «کاهش محدود» قیمت مواجه شده‌اند!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 41.7K · <a href="https://t.me/alonews/128935" target="_blank">📅 18:45 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128934">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ede7a13d15.mp4?token=JayFy97RSjBKiWvNaHVScydfZUgvcZjXXmT27hvf0Yh5dzdUA3dTk1xF-nmv5YlCjnJvDCa0kbbHAwzU84gZ-WTKRNdcHGxI2SQVgenDdDdB2bbQM3g3oB49Afq8ULn4VdInf7RIzCdoSly2csTz2IN8uxBLxz_rM5soZxVrelUns7Kz14W0KsKMkmYzJMYQGbyxf9cRd0Xg9fuc9P-Q_wSsIgkJBROiEaEwGhMSGBo5vI6yQiCG3Q4YeNG0mWWMBGQndcmlzmwb4ALVMaulWEKkToZHsIWxyn6bO0PKa3or5GSlKq2lrmRf4542ludnzGTqYOU8T-fc0fDsA3TEq4iteBM-GFQUz9WWNwxS3HXAe4_gAMaoAbEcppcr8QFuxUJ6gBlI1n3oJytuPSv60RK3fVrkbPQU5bLj7HMqd_Skxjf5gJ0Hn_aoZWMS-Aw06WDOrxIsMqVspHEfO8pV8wtxwdWBYpg8FwI3QhQNyFd-ok3aF238UEJ7bf-7UvS3AoXxjddACIBZBrcDRFKZTtgcOB_iJGnlDdshd5UXcsotThRfMZ6rF5OuJBAmpQe5qVZOLczpzPSecfvAblwWBEHZCwioN8f4XpSn06uiX13MB4RS_KWgN1cYa6c7bZJMZQmmFKbdvmdxAgH2voPxHK690KaZCcAYpZmA9RDPAU0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ede7a13d15.mp4?token=JayFy97RSjBKiWvNaHVScydfZUgvcZjXXmT27hvf0Yh5dzdUA3dTk1xF-nmv5YlCjnJvDCa0kbbHAwzU84gZ-WTKRNdcHGxI2SQVgenDdDdB2bbQM3g3oB49Afq8ULn4VdInf7RIzCdoSly2csTz2IN8uxBLxz_rM5soZxVrelUns7Kz14W0KsKMkmYzJMYQGbyxf9cRd0Xg9fuc9P-Q_wSsIgkJBROiEaEwGhMSGBo5vI6yQiCG3Q4YeNG0mWWMBGQndcmlzmwb4ALVMaulWEKkToZHsIWxyn6bO0PKa3or5GSlKq2lrmRf4542ludnzGTqYOU8T-fc0fDsA3TEq4iteBM-GFQUz9WWNwxS3HXAe4_gAMaoAbEcppcr8QFuxUJ6gBlI1n3oJytuPSv60RK3fVrkbPQU5bLj7HMqd_Skxjf5gJ0Hn_aoZWMS-Aw06WDOrxIsMqVspHEfO8pV8wtxwdWBYpg8FwI3QhQNyFd-ok3aF238UEJ7bf-7UvS3AoXxjddACIBZBrcDRFKZTtgcOB_iJGnlDdshd5UXcsotThRfMZ6rF5OuJBAmpQe5qVZOLczpzPSecfvAblwWBEHZCwioN8f4XpSn06uiX13MB4RS_KWgN1cYa6c7bZJMZQmmFKbdvmdxAgH2voPxHK690KaZCcAYpZmA9RDPAU0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ در ۹ مارس: این موضوع واقعاً روی ما تأثیر نمی‌گذارد؛ ما نفت و گاز فراوانی داریم، خیلی بیشتر از نیازمان.
🔴
ترامپ در ۱ آوریل: ما اکنون کاملاً از خاورمیانه مستقل هستیم. به نفت آن‌ها نیازی نداریم.
🔴
ترامپ در ۱۷ ژوئن: اگر به بمباران شدید ایران ادامه دهیم، ذخایر ما در حدود ۴ هفته تمام خواهد شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/alonews/128934" target="_blank">📅 18:42 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128933">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4b7d1aae69.mp4?token=MTbEkjygVH3H0NusHNfRK6KtA9FuuP-SeGwoFAdSwZf9xt2phAZrl1UgWXfZf3T4tDo-mXacQyuK4dQ0Vk4SJBtlgiYDJPzSC4pnNRQsJ-w_k3H41Z9WJdOvvq_eu0ojz3FiH81EaqhkTxcDnj6UBKZVxLpZ47_IahO7ddmfJMlCG-L7yhub8nxq435Ptb-I7mLIX1qSNiEKnhle9g9apsrBXCHFqfc3df399KaQLQgpo2tWeufYDbWuQVdu3hOqNuD7Ef6NfhCpaflW9nYbrMssUQajtIczzM_q_NLpLeU1IXGlRz8Ou1fb-gTnbEqxZrsAPP1D9fHQ4RJl0fG-ug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4b7d1aae69.mp4?token=MTbEkjygVH3H0NusHNfRK6KtA9FuuP-SeGwoFAdSwZf9xt2phAZrl1UgWXfZf3T4tDo-mXacQyuK4dQ0Vk4SJBtlgiYDJPzSC4pnNRQsJ-w_k3H41Z9WJdOvvq_eu0ojz3FiH81EaqhkTxcDnj6UBKZVxLpZ47_IahO7ddmfJMlCG-L7yhub8nxq435Ptb-I7mLIX1qSNiEKnhle9g9apsrBXCHFqfc3df399KaQLQgpo2tWeufYDbWuQVdu3hOqNuD7Ef6NfhCpaflW9nYbrMssUQajtIczzM_q_NLpLeU1IXGlRz8Ou1fb-gTnbEqxZrsAPP1D9fHQ4RJl0fG-ug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
چرا با اسرائیل دارای سلاح هسته‌ای برخورد نمی‌کنید؟
🔴
گروسی: چون عضو ان پی تی نیست! خواهش میکنم عضو شود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 41.2K · <a href="https://t.me/alonews/128933" target="_blank">📅 18:39 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128932">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/996fa2aee7.mp4?token=H2hVfdoL81nmnAc_Erfux86sCBc-jfPBAlvCkUy1SxQX4aac4J1PoYfO-haLEokgWv1XGb2CrQhCrtbVAChjI8yBmXa22c5JNb1yxO3-KvEOkpPPJhAzPSkLyQMIT-afriEJpfnUIAmdcGEzSiojikiDr3QN7MzCyf_R2P5WXTM0aLySE9KTCodZ5oTR1sE1zvnGpOfRxmlyprmbIMcz96ydx4buH7liKd0dTT04WuabJf9lytAktaKhu4QpESKxwm0QocXupZSSbXeOzmqBOOkoAshZx37ZUuO9Ec6efPuFb7bS68SFAv0_7khDtNRfCSxKitrasV0p0_0oa1OGpg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/996fa2aee7.mp4?token=H2hVfdoL81nmnAc_Erfux86sCBc-jfPBAlvCkUy1SxQX4aac4J1PoYfO-haLEokgWv1XGb2CrQhCrtbVAChjI8yBmXa22c5JNb1yxO3-KvEOkpPPJhAzPSkLyQMIT-afriEJpfnUIAmdcGEzSiojikiDr3QN7MzCyf_R2P5WXTM0aLySE9KTCodZ5oTR1sE1zvnGpOfRxmlyprmbIMcz96ydx4buH7liKd0dTT04WuabJf9lytAktaKhu4QpESKxwm0QocXupZSSbXeOzmqBOOkoAshZx37ZUuO9Ec6efPuFb7bS68SFAv0_7khDtNRfCSxKitrasV0p0_0oa1OGpg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
لبنانی‌ها همچنان به سمت جنوب لبنان هجوم می‌آورند تا به خانه‌های خود بازگردند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 43.1K · <a href="https://t.me/alonews/128932" target="_blank">📅 18:36 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128931">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CEGN_kJmefK3jSDeYYmaTzILEgjtQBHp6pjkAjZ7LJKbuzvMxUF5acAdRS8h895JDlFaoKbhild3yqvE3AFn2b8q-N8fxl-gvNp5In3ayKjaesam_nmX034rBx2dPgVIQZmn7YrHkRMpk0yEd1zzN7uutcmx5UxhvtfI_P6YVwVdp5Oblqn3XPkKapxhxsQFsJ08rApyge7Kz-XmuPB9dKhAd2vXAs2hcnUTrqfHyNi5SxLOk16o87K7LnYtDmcGd-0Y3oXfsZ5F-cIy15bdCrYic-6dKNG_sIasEhQf_REw0s3HvWiKUnQumGNFOXOszz8waCfBDwrryjCueG5n2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پیش‌فروش‌ بازی Grand Theft Auto VI رسماً از ۲۵ ژوئن آغاز خواهد شد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/alonews/128931" target="_blank">📅 18:22 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128930">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">👈
ایهود باراک، نخست‌وزیر سابق اسرائیل:
احتمالا نتانیاهو در آستانه انتخابات، به لبنان حمله خواهد کرد، و در تلاش است یک جنگ ابدی را با ایران و حزب‌الله آغاز کند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/alonews/128930" target="_blank">📅 18:08 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128929">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">👈
الجزیره به نقل از یک منبع در دفتر نخست‌وزیری:
معاون وزارت امور خارجه نماینده پاکستان در نشست سوئیس خواهد بود.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 46.7K · <a href="https://t.me/alonews/128929" target="_blank">📅 17:56 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128928">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">👈
ترامپ به کانال ۱۱ عبری: آماده دیدار با نتانیاهو هستم
🔴
او باید منطقی‌تر باشد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 47.8K · <a href="https://t.me/alonews/128928" target="_blank">📅 17:56 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128927">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DxTcQ9oYsFTZj1up_iWJgkdLSQ_hiQsogJ1T4acjPXk3ilANgbfwWImBkyzaPdxs3sQ1XYMRDpmdnJ6llnZu4bWn7bzn2oxYWXyzL8wpKV4KorDHJu_VmvU4oiChgMlhqA2R-WcuCYbyTR4Ug6OEkAJwTdXhgxGnSekQel6INqAzb1LkIGibWrMzBAueGiD6nV_qnr0upmw7V-UPORFOuJ7Nb3jPYJFxQBspNeApY1Lo2XU13oNFrIn2fBe4DzAT9ZmCQUdP0yE5zUSo9YZ6GsXXDpmCWpAic7Vo-RdIFiGl9OtQuZ7uEwY2sPSxQwnUk1xOnlXqh-AfIeet1XLEnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
رئیس‌جمهور ترامپ به کان نیوز:
من به احتمال زیاد در انتخابات پیش رو از نتانیاهو حمایت خواهم کرد، اما باید ببینم چه کسانی نامزد شده‌اند.
ما رابطه خوبی داریم، اما او باید منطقی‌تر باشد. من آماده‌ام با او دیدار کنم.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 48.8K · <a href="https://t.me/alonews/128927" target="_blank">📅 17:52 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128926">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">👈
ترامپ:
هیچ ملت و فرد عاقلی نمیگه بمبارون رو ادامه بده
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 46.8K · <a href="https://t.me/alonews/128926" target="_blank">📅 17:44 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128925">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aKxtSS8wepKvFKitEUVwTxkmMKSJyZTWFMYXAETWq_2YtT-goB9Ug145Btt_9-NKeVp4ze2XWt5ihW5vNhPYHI1O5dCxaNW_8o7LvoJg2kogwxhFJIvEjcUDaqJBU4RJppLI_btBdVEb6IFjC0Q3bnqQNSIkFQDSgyS6m-hPaMYgsXtuTNx1VxnH4xKmt3Adv1-cr24pHZzWcLMrBezJSm77PHc0RO38GQcqgpvJIhJZfxpNHLTZKW4NTlvJuBGVBZaUOtowD2Rpu4RrAe1vrhcMLXxCOngmxts8a3WPRhJCa4lAF6qVj-tgbMe0G6asetlzv9wGQVHlikg1RxUWUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ: نفت در حال جریان است ، ایران هرگز نمی تواند سلاح هسته ای داشته باشد (جهان در امان خواهد بود!), بازار سهام در حال رشد است ، شغل در رکورد است ، و قیمت ها در حال کاهش است (قیمت مناسب!).
🔴
کشور ما قوی ، امن و محترم است مثل هیچ وقت پیش. خواهش میکنم!‌‌
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/alonews/128925" target="_blank">📅 17:36 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128924">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">👈
ایرنا: ایران به پاکستان اطلاع داده است دیگر نیازی به برگزاری جلسه حضوری در سوئیس نیست.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/alonews/128924" target="_blank">📅 17:35 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128923">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">👈
تلویزیون پاکستان:  سفر برنامه‌ریزی شده نخست وزیر شهباز شریف به سوئیس بدون ذکر دلیل لغو شد.
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 48.6K · <a href="https://t.me/alonews/128923" target="_blank">📅 17:35 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128922">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/70f05f75b6.mp4?token=jlxODeuSLzxdRzhMnsbEoiF_ru4vlkKgvxLwfE0u9nbtbtnpWP2UDpc9yqudlXX2uuSnppqW1rxJbr9NepmrV06x4o1jcprj33xZ7MMpXl0qc2alcOQ7uBfII9ITfYABKgzQXDDvRsM1O3LgBKKGGF2__xP-gQrXCFgmUjfgPCxDYA9hl4i58bQlkasLo7SJ-OCsLHeIL21SnFFUf2IF_IiQLsfOiXuJkleA7wANcwjRldZ91x9UeNJQINvPZoD6BSptYSnmcv8h_udQbPgysmDM9MusFaBnWX_57r3yiF5vSyAnx11jC1RhJRClyG7a9iHzKQsEp69-zVhqaEk3sQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/70f05f75b6.mp4?token=jlxODeuSLzxdRzhMnsbEoiF_ru4vlkKgvxLwfE0u9nbtbtnpWP2UDpc9yqudlXX2uuSnppqW1rxJbr9NepmrV06x4o1jcprj33xZ7MMpXl0qc2alcOQ7uBfII9ITfYABKgzQXDDvRsM1O3LgBKKGGF2__xP-gQrXCFgmUjfgPCxDYA9hl4i58bQlkasLo7SJ-OCsLHeIL21SnFFUf2IF_IiQLsfOiXuJkleA7wANcwjRldZ91x9UeNJQINvPZoD6BSptYSnmcv8h_udQbPgysmDM9MusFaBnWX_57r3yiF5vSyAnx11jC1RhJRClyG7a9iHzKQsEp69-zVhqaEk3sQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
رویترز تأیید کرد که محاصره دریایی ایالات متحده بعد از ۱۰۰ روز لغو شده و کشتی‌ها بدون دردسر از تنگه هرمز عبور کردن.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 48.7K · <a href="https://t.me/alonews/128922" target="_blank">📅 17:31 · 28 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
