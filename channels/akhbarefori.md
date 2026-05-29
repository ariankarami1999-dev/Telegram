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
<img src="https://cdn4.telesco.pe/file/ibArnC4A7L1VTOkvFXxWu1Oj-0qth_PHX5DaSVZSeG35dnpi6WcXxs8SFDdLiw8GqK9wP4cKJVn0B2Bs_Q3EqOMz_vUvcsPMrotljWlHkSRL8I0x7Y6KBzqG7AYQ1sicIOI6cJEUbRv_NMCRnjUaZi7kgHtYmibVi0N705nl2XhmqBZJXDJr5hYWh5PiZD3IGR7Doj5C3lsybl2Voi2hDmWtFTbRbSVv09Wf3pvIyGBFDyTSAIq7TBTsY6wxmmQfm5Gv5oe8ktyEtA6R_92siaipxJ7tbptPkiBRvNt7qZn-uqinR5MDkKW5OfJcax0R_FIkLUPkq5So1e3U3G0HXA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 3.97M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforii</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-08 14:09:23</div>
<hr>

<div class="tg-post" id="msg-654621">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/17fea825c6.mp4?token=cZwKuQHCdFm3E7LHAo4WuZx02SYNbr_T2IcovI-pgWuS2e2l9vhZWXZqNjYubmrTjXB4eI8ZWf6Cx5bo5-dYHWH6LnYdilNwqkx14sf2HaXjjXGryIv90trqizN_ckjAHNET__kHoRo9bY1UPnLLJ20FT3bU0av5zrafwaErg8c4ID7cFFeTG9sKHAu-tYJJFd7HXfUV8dqzcAKVBaLY2EmXum2B1NBJfVwTXOVBTbm4C4ZVNqt-tPSaYGEgRvSgKsXupHTBlYgWFA49FlEptcDYwptlvsqeZ8LUp296G9bcTPCA-6wgAZ4-P8XjG-bhEhYY7zddVsJUm2n23iwOaw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/17fea825c6.mp4?token=cZwKuQHCdFm3E7LHAo4WuZx02SYNbr_T2IcovI-pgWuS2e2l9vhZWXZqNjYubmrTjXB4eI8ZWf6Cx5bo5-dYHWH6LnYdilNwqkx14sf2HaXjjXGryIv90trqizN_ckjAHNET__kHoRo9bY1UPnLLJ20FT3bU0av5zrafwaErg8c4ID7cFFeTG9sKHAu-tYJJFd7HXfUV8dqzcAKVBaLY2EmXum2B1NBJfVwTXOVBTbm4C4ZVNqt-tPSaYGEgRvSgKsXupHTBlYgWFA49FlEptcDYwptlvsqeZ8LUp296G9bcTPCA-6wgAZ4-P8XjG-bhEhYY7zddVsJUm2n23iwOaw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
وزیر خارجه پاکستان به آمریکا می‌رود
🔹
طبق اعلام منابع پاکستانی، اسحاق دار، وزیرخارجه پاکستان، در تاریخ ۲۹ مه (۸ خرداد) در واشنگتن با روبیو دیدار خواهد کرد./ انتخاب
🇮🇷
✊
@AkhbareFori | khabarfoori.com</div>
<div class="tg-footer">👁️ 3.24K · <a href="https://t.me/akhbarefori/654621" target="_blank">📅 14:01 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654620">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G6sH5c8bez38EsMuD5-AI1x5rZQ405viOFPwE6e_MdjXrBxxaqTCXcAi5FBaCV4nMrSdSzBKK_agUQ6OplJ-XA3XFX7IT6oFRhUA1sEgJ_IcxGDdAH9AlVR5SvqqHUE6aV8d4e-aME7ehJH47TbStI5ZDsihwhzy1iBsfFpFIl83yGxnejCpJSDKDYvUUhgB3U2tHAA32v03Tc6vXWaJ32CHPCwNzo9tsjXLADdOzzJhe8Rob7M_m97odJaSXG4aF-kkqeqXr3ouhWXtbxDKFDlZ_zT1ZwsKo_xj5EZyXjDKslffiQ-VykN2X7NrCsO-Kgu9qDJLTOhivrdNMJqOOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
محمد معتمدی: چند رادارشان منهدم شد و حاصل شد برگشت آب به دریاچهٔ ارومیه
🔹
حالا فکر کنید اگر کلا شرشان از منطقهٔ ما کم می‌شد همه‌چیز چقدر پربرکت‌تر بود.
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 5.93K · <a href="https://t.me/akhbarefori/654620" target="_blank">📅 13:54 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654619">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tHh1TVL-eVe0IPuFsr-gQ5UGOeXr4Do9lCzCnILN5QzAJ8GEGuNxxcrWbhh9n-1cKbox8NZEbJIuyc8lDfOTsNAWZElwe0op76e_GQSFx5D3827GATxHF7xtoPBGuksnSgKdnKYZDe3BZCIktsaPYnm5rwugU1kiLbMCnCbuOqy9-4f3I5umuKCzuXCaJOQv-IgA8cV6Zc8gm8VXuAtCQCEG9hzIJ8eR0gxRk4HEuKGvmRFdMkw2Uc_Jtm6EN3sDE8kwW_GblbXWFyE8V2CfcqgrXFKx2W_cw45cS-X1HjwGneYB3M-c-_BKw99QBKK9zJWdXOsnI3er-TOlglAt6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
نیویورک‌تایمز : پیشنهاد صندوق سرمایه‌گذاری ۳۰۰ میلیارد دلاری برای ایران در چارچوب توافق صلح
نیویورک‌تایمز:
🔹
یکی از عناصر جدید و غافلگیرکننده در توافق پروژه صلح ایران، پیشنهاد ایجاد صندوق سرمایه‌گذاری برای ایران با حجم ۳۰۰ میلیارد دلار است. ایران ابتدا این مبلغ را غرامت خسارات جنگ (برآورد ۳۰۰ میلیارد تا ۱ تریلیون دلار) مطرح کرده بود اما طرف آمریکایی آن را به‌عنوان یک صندوق سرمایه‌گذاری بین‌المللی بازتعریف کرده تا از به‌کار بردن واژه «غرامت» اجتناب شود.
🔹
این ایده به استیو ویتکاف و جرد کوشنر نسبت داده شده و شامل پیشنهادهایی مانند تقویت پروژه‌های املاک و مستغلات در تهران و سازوکار سرمایه‌گذاری گسترده‌تر به‌عنوان مشوق توافق است./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 6.06K · <a href="https://t.me/akhbarefori/654619" target="_blank">📅 13:52 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654617">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a550993e97.mp4?token=cBTE4eUByS6HQUgv8GfUsmTNRNSzDDWTySaZO3MiP8qYq20ScRfpQZGqWxgvAtYpzNrGzF7dvLyNLl-DrKWSpKJBQzgMvu7SthB8aVi54DeE-FIM75LZnef37AYL-TLf9Wvv_zRB2UL1PXd5Firvw7mTgXURKkCUUVrssMVXwg8Ml8acqni1-TKIy27Cd3u_sMbsCBPUDtMk-b11nNZby-bOrfZRa8m8mRApvjDkLV6FTQN-NMcD9w5bVklQccd5py23rZfnvIqBkFxD5BygQFRs3yS6mMD0_o5A8gxCIPDGNnL4AClv9oK6q4LlPvdJ53uaePUvNHjUuqq3l7zG0Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a550993e97.mp4?token=cBTE4eUByS6HQUgv8GfUsmTNRNSzDDWTySaZO3MiP8qYq20ScRfpQZGqWxgvAtYpzNrGzF7dvLyNLl-DrKWSpKJBQzgMvu7SthB8aVi54DeE-FIM75LZnef37AYL-TLf9Wvv_zRB2UL1PXd5Firvw7mTgXURKkCUUVrssMVXwg8Ml8acqni1-TKIy27Cd3u_sMbsCBPUDtMk-b11nNZby-bOrfZRa8m8mRApvjDkLV6FTQN-NMcD9w5bVklQccd5py23rZfnvIqBkFxD5BygQFRs3yS6mMD0_o5A8gxCIPDGNnL4AClv9oK6q4LlPvdJ53uaePUvNHjUuqq3l7zG0Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سیل در رودخانه فرات، در شمال شرقی سوریه
🔹
به دلیل سیل گسترده، وضعیت بحرانی در استان‌های دیرالزور و رقه اعلام شده است.
📲
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 7.43K · <a href="https://t.me/akhbarefori/654617" target="_blank">📅 13:43 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654616">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oDyYH6gAG1uF--1iPQC0BP69X_N6M2Wu8phb1MgCLRJMrNv833LYMHMt48h3XwSY8ingQrtSp09IOLA1DIV5ofOhwrh9RU_coP5Q5wEPcq3yIoRttCc5_nUrbzU_5wFAUzFxXNJa9U1ipc0yjm2wbEuvG_epySQXmNUp6HdfogeskYDN1aC6YBUn0duvpD3AuIw_mo984-gTupYCNuQIuJIbeVJx3QHkIej0JOhrWQQDykc6oFPSE4VGOqGWUPJSWFuEdao5CGPKK0QiVxuftGUg7RVj55eAO3KZa-pUR4LvEbGj6lE91oo8Pv8Vc4HAEjIgsAdJBuXlgRt8XK_SjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سخنگوی کمیسیون امنیت ملی: به قدرت ایرانی‌ها تعظیم کنید
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 9.83K · <a href="https://t.me/akhbarefori/654616" target="_blank">📅 13:34 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654615">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
شایعه‌سازی برای یک گنج در ایران
🔹
رسانه‌های غربی دوباره شایعه‌سازی کردند؛ آن هم درباره یک گنج بزرگ که احتمالا از نفت هم با ارزش‌تر می‌شود.
🔹
جزئیات را در این ویدئو ببینید.
@Tv_Fori</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/akhbarefori/654615" target="_blank">📅 13:27 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654614">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">♦️
خلاصه اخبار سیاسی هفته/ از ۲ تا ۷ خرداد ۱۴۰۵
تحولات مذاکرات ایران و آمریکا
🔹
ادامه مذاکرات ایران و آمریکا و انتشار خبرهایی درباره نزدیک شدن دو طرف به توافق و نقش‌آفرینی قطر و عمان. همچنین انتشار سند غیررسمی اولیه تفاهم» توسط صداوسیما
افزایش تنش‌ها در خلیج فارس
🔹
انتشار گزارش‌هایی از تحرکات نظامی و درگیری‌های محدود دریایی و فعالیت پدافند هوایی و حمله به شناورها و پاسخ متقابل ایران
اظهارات جدید ترامپ درباره ایران
🔹
آمریکا «به توافق بسیار نزدیک شده» اما همچنان اختلاف‌هایی باقی مانده است. مذاکرات با ایران را به تحولات منطقه و توافق‌های عربی مرتبط است.
🔹
گسترش رایزنی‌های دیپلماتیک ایران با کشورهای منطقه از جمله قطر و پاکستان/ همچنین ایران و قزاقستان ۱۴ سند همکاری مشترک امضا کردند
واکنش رسانه‌ها و فضای سیاسی داخلی به اخبار مذاکرات
🔹
برخی جریان‌ها خواستار انتشار جزئیات توافق احتمالی شدند و فضای رسانه‌ای کشور تحت تاثیر اخبار مذاکرات قرار گرفت.
مهم‌ترین اخبار جهان
🔹
ادامه تنش‌ها در خاورمیانه
🔹
نگرانی درباره امنیت تنگه هرمز
🔹
افزایش فشارها بر رژیم صهیونیستی
🔹
ادامه بحران انرژی و اقتصاد جهانی
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/akhbarefori/654614" target="_blank">📅 13:22 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654613">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kzDqQ6NVADSZH9exEXblwIEKIMwF9Tacjgmpx8jD_7u-uoo5JxIqpf4aDXS7G3-rGrIE0l8HQnji03l7y5MjUrb9I_Uf_TlU8nUxbYXfZueYiOCwJ1L3Hd4DdTxMkKylBZ3z-jHSaiKOGSa4cjkrBrAoC85OPYyzKJQ-UhfprcCe-M2R1XUTQmH6aY-7VDYYHB6hH6FmSBAL0jVJnoHKd_eKGn31vV32EY6FMCA-9Xcv0PacKVUa3L_b-ZCq_CUlYBvqYDdCR_yAV4L-N_5NVjVwUozr_8KqaKyCceebybfroXYOSiiYxsqLKPkz-CEQ_xjmONpmBbpbrYLwYLYV7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
راهی برای معامله نیست | چرا ترامپ نمی‌تواند ایران را وادار به عقب‌نشینی کند؟
🔹
یادداشت تازه آتلانتیک درباره بن‌بست و سردرگمی دولت دونالد ترامپ در مذاکرات با ایران است. نویسنده توضیح می‌دهد که ترامپ پس از ماه‌ها تهدید، فشار نظامی و تحریم، اکنون با واقعیتی روبه‌رو شده که برخلاف انتظارش، ایران حاضر نیست تحت فشار کامل تسلیم شود.
در خبرفوری بخوانید
👇
khabarfoori.com/fa/tiny/news-3218537</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/akhbarefori/654613" target="_blank">📅 13:04 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654612">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromمن°(منتظر شهادت)</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2738688f66.mp4?token=iS8e0d7B3AOTfm2wuMh0GamTPKscBJjaFiofPXpFS4IEdJwuiOBTn06ZWQn8WkhioHUfU34x1AudMsx0csOXsHe1oW9DQEhupe8eR1XQFEfE_BayXqzYstv6R6HPnuxEGBwFivvSbJHph3wke7P8J6pPma4Hx_p6OgksMqb1of8kmCwN4-s_ftqoXGLe2ZbiBvs5c8QON1tbBX2PDzWLh30fl-JupEmq29Sh6oVoHkmn0qz7VCFpac6GXZkV8i39ZrfdFw6sINdb5orkeELE-TxbYIGVMB4beVHrc_0mmpGkIdzBUb1XYqeuNuugfCkhyTa512u_nGGYitFUhca2eQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2738688f66.mp4?token=iS8e0d7B3AOTfm2wuMh0GamTPKscBJjaFiofPXpFS4IEdJwuiOBTn06ZWQn8WkhioHUfU34x1AudMsx0csOXsHe1oW9DQEhupe8eR1XQFEfE_BayXqzYstv6R6HPnuxEGBwFivvSbJHph3wke7P8J6pPma4Hx_p6OgksMqb1of8kmCwN4-s_ftqoXGLe2ZbiBvs5c8QON1tbBX2PDzWLh30fl-JupEmq29Sh6oVoHkmn0qz7VCFpac6GXZkV8i39ZrfdFw6sINdb5orkeELE-TxbYIGVMB4beVHrc_0mmpGkIdzBUb1XYqeuNuugfCkhyTa512u_nGGYitFUhca2eQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مأموریت امام زمان الان چیه؟</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/akhbarefori/654612" target="_blank">📅 13:02 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654611">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YjVlH1isgW14Wq_Ri3kbtXy8hTAoOVeZ7aT_v8MngWeQxz2edd1HurMwklCZw8nL5etIuf7pQU6SfSvFzM4wJUa7AzvD9_o5-dVSyUhqxDG6-93JkvQbdVRwSM7Gp5Tv6KzerI94n-5t4jbyrXgLgoRL7zASKJ4QFp5enFHIkK8pDf1yp92XfMQmO48-CRnEyPQHGwKFBbJq7JXiSHMCKCL9SrPlsg93ZeVE0UfCM7kNiG74yu5htdEKO2nJyeA8_28LD3x2aS2hlMYHS93FZPO1XCaxMD9pg_KpqqE2mtr1liDpUI4929gdhiNftw7K0lol-OjeiXkusbufGLz_YQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
هلاکت ۲ عامل اصلی آشوب‌های دی‌ماه دره‌دراز کرمانشاه
🔹
۲ نفر از عناصر اصلی آشوب‌های دی‌ماه سال گذشته در منطقهٔ دره‌دراز کرمانشاه به نام‌های مجتبی ویسی و میثم ویسی، روز گذشته در درگیری با نیروهای حافظ امنیت به هلاکت رسیدند.
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/akhbarefori/654611" target="_blank">📅 12:56 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654610">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Cy2Q8SN-P1pU8w0TEH1N-3AYqptRRqN5KjzscXq-_XSSirbr2HNhvvpl-QF6z7R3Ipd5SrpD44uTnRSVDCfh3l-MxWrVq6yvJSa65HL0CWGy8XrhsS8252x-IVzsvaMuWLj1fWR5Hs24IExdrUOMIfPhhKjxe88pe5ANefz5hqlKbOAsPcIZHpj-a1zrLR3heDI94oBE_vNgY8qcg58n3WPtvtOzKbrlbBDrXUme15NuE6VjlY-t1x5ktAPzhCfkVC2IYYGZm42mi9B1-sMRoP87vsTPmfVwhFnKN7HzC5cwM7P2ybCtgqNHisoDO8tk1DSagW5sAMRv9_8TTMF14w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
حقیقی‌ها ۱۶ همت پول به بورس تزریق کردند
🔹
در هفته اول خرداد، سهامداران حقیقی بیش از ۱۶ هزار میلیارد تومان نقدینگی تازه وارد بورس کردند که باعث شد شاخص کل ۸.۳ درصد رشد کند و به کانال ۴ میلیون برگردد؛ شاخص در پایان هفته روی ۴ میلیون و ۷۳ هزار واحد ایستاد.
🔹
بیشترین مقصد پول حقیقی‌ها صندوق‌های سهامی، گروه بانکی و فلزات اساسی بود. میانگین ارزش معاملات خرد هم از ۱۳ همت عبور کرد. صنعت لبنیات با حدود ۲۱ درصد، داغ‌ترین صنعت هفته لقب گرفت./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/akhbarefori/654610" target="_blank">📅 12:37 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654609">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1567d3d1f9.mp4?token=uY9G_5PIiu3GXwQ-3pOrYVAhr33erW5sYRtFlLWlXD1b6N-ucfRM6nKL_tjUTzbk3e5Kxe6xgl2TtYBAwwBt-viIf-bmy3NxorapaB3VDyycvg_jYmboBjiBLcfUvKXcp0wRopSNGJkQ3V-geOKs2c0Rn09AWT5KB67OtDtj2QHzjM8qKHwAWuwLYllZ_okZdbUZr8rPSlQG1LHopJUyxa4LlXqYKn8pwlUnaoCaIpXOuWJxwOAX0E0ZY4dTQ7WWb9zs6U1SNT4YcyqPUy5cBNJciCUOQjSBFHM35MS3tILUlLeorEOljFAf4Reb3Wp9E-LT4T_R3is_szOewinARQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1567d3d1f9.mp4?token=uY9G_5PIiu3GXwQ-3pOrYVAhr33erW5sYRtFlLWlXD1b6N-ucfRM6nKL_tjUTzbk3e5Kxe6xgl2TtYBAwwBt-viIf-bmy3NxorapaB3VDyycvg_jYmboBjiBLcfUvKXcp0wRopSNGJkQ3V-geOKs2c0Rn09AWT5KB67OtDtj2QHzjM8qKHwAWuwLYllZ_okZdbUZr8rPSlQG1LHopJUyxa4LlXqYKn8pwlUnaoCaIpXOuWJxwOAX0E0ZY4dTQ7WWb9zs6U1SNT4YcyqPUy5cBNJciCUOQjSBFHM35MS3tILUlLeorEOljFAf4Reb3Wp9E-LT4T_R3is_szOewinARQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
وزیر جنگ آمریکا: ایران یا توافق می‌کند یا با نیروی نظامی مواجه می‌شود
پیت هگزث در جمع سربازان آمریکایی:
🔹
همانطور که رئیس جمهور در جلسه کابینه گفت... ایران یا می‌تواند با یک توافق از طریق مذاکره، کار را به روش درست انجام دهد - یا می‌تواند با شخص من در سمت چپ معامله کند. که اتفاقاً من بودم - اما این من نیستم. شماها هستید.
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/akhbarefori/654609" target="_blank">📅 12:29 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654608">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bd34f8637c.mp4?token=cXZlWlNUflm6L9jc7g4Y7jnaRNRlng4S7n4_vEJxdhi81MQ_HQF4UgPdYxsV8cpzxo4pHZLGIQz4X-cifIRAuo0z_M3R3ybU9DLCiRMS28G8NoV9fq_aNcu7LSha0QTTbORQb8PvNhs5yIrYVA-eFJ1PVWp0bydUntJcplOYO_2v2Thwij0KDzQ0Z0A5GZea6ZHFDplUqiEfUSnHcSqLGgFBEEteG9rfwsHPkvw5EnSVQ9l4c7hT6MAtMWsbEYT6CkU2osBsa7Z-CjwsNipdxIJ_zbHIZJmBovw-YrrLJ2_-DJvRfshTvDqKa1zSsFPriYsKvFDbMLnzp-dHU6_BiIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bd34f8637c.mp4?token=cXZlWlNUflm6L9jc7g4Y7jnaRNRlng4S7n4_vEJxdhi81MQ_HQF4UgPdYxsV8cpzxo4pHZLGIQz4X-cifIRAuo0z_M3R3ybU9DLCiRMS28G8NoV9fq_aNcu7LSha0QTTbORQb8PvNhs5yIrYVA-eFJ1PVWp0bydUntJcplOYO_2v2Thwij0KDzQ0Z0A5GZea6ZHFDplUqiEfUSnHcSqLGgFBEEteG9rfwsHPkvw5EnSVQ9l4c7hT6MAtMWsbEYT6CkU2osBsa7Z-CjwsNipdxIJ_zbHIZJmBovw-YrrLJ2_-DJvRfshTvDqKa1zSsFPriYsKvFDbMLnzp-dHU6_BiIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویری دیدنی از حرکت فلامینگوها در میان کانال های آب دریاچه مهارلو
#اخبار_فارس
در فضای مجازی
👇
@akhbarfars</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/akhbarefori/654608" target="_blank">📅 12:20 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654607">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
لوازم آرایشی تا ۸۰ درصد گران‌تر شد
مسعود گل‌کار تهرانی، نایب رییس اتحادیه آرایشی‌ و بهداشتی و عطریات تهران در
#گفتگو
با خبرفوری:
🔹
واردات لوازم آرایش درحال حاضر تقریبا به صورت کوله‌بری و ته‌‌لنجی وارد می‌شود. قیمت لوازم آرایشی به طور میانگین بین ۵۰ تا ۸۰ درصد افزایش داشته است.
🔹
۸۰ درصد کالاهای آرایشی و بهداشتی تا الان تقلبی وارد می‌شده است که بیشترین آن از کشور چین می‌باشد و پس از آن هند، پاکستان، و کشورهای سمت غرب ایران هستند. این کالاها از اروپا وارد نمی‌شود چون تولید چنین کالایی آنجا صورت نمی‌گیرد.
@Tv_Fori</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/akhbarefori/654607" target="_blank">📅 12:20 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654606">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/85b5942bb5.mp4?token=j_yWz5mHEM6pBwFyi0esu--H8C3FO-7XP14dM-IdNcQ-jxApVcs3x66gmYKjdVcuHJQ82b_MBbIrH82oZwy49ecNmYZLn7DrZcG_jH8T2b7vSBxwF8k-ixM8VvKv98nxR1MK1sietI26p5ZO6iGTQmaRee6dtlBvS0Pq24Cywa2qR-eU-N1zbAYyeBFshZtkHdsRSB3Klng71Wvhu5MjVB3hgCVebNPTr3zO8ZMA_7eMyamKvmQDfp81cneT8LIv3C48qpBOfAf6Etj_d_t-hutR4u-8YNgZXMJZg5EjGr0p_RDl_mz6KMAX4cL2d28GvgMLgVBrolkl32BAO7m5Nw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/85b5942bb5.mp4?token=j_yWz5mHEM6pBwFyi0esu--H8C3FO-7XP14dM-IdNcQ-jxApVcs3x66gmYKjdVcuHJQ82b_MBbIrH82oZwy49ecNmYZLn7DrZcG_jH8T2b7vSBxwF8k-ixM8VvKv98nxR1MK1sietI26p5ZO6iGTQmaRee6dtlBvS0Pq24Cywa2qR-eU-N1zbAYyeBFshZtkHdsRSB3Klng71Wvhu5MjVB3hgCVebNPTr3zO8ZMA_7eMyamKvmQDfp81cneT8LIv3C48qpBOfAf6Etj_d_t-hutR4u-8YNgZXMJZg5EjGr0p_RDl_mz6KMAX4cL2d28GvgMLgVBrolkl32BAO7m5Nw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
معجون اوتمیل یک صبحانه مقوی و خوشمزه برای بچه‌ها و بزرگترها #آشپزی
🇮🇷
✊
@AkhbareFori | khabarfoori.com</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/akhbarefori/654606" target="_blank">📅 12:05 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654605">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5e8d7516f6.mp4?token=WVdcCrpVoyGIYMmgfZ_qJnM_cLrSHFCW8jUL-KM4r0LqWsZ0XXUO2iiep_v1GDjEi_nsBPEpyi05rVVdCni4GfnFCe4sdL9Fobw1dPdvybQLB6Vy2KQHzaBGj-o6f9augzt3FIhQFUHKM-FnF3ViCg5APWGfS0hOZMZINTX7ag_jjuBBGIgnzVcxIdp23qPezuxf_e3XbdBKTUQdsMZltdlNKpNLNX1wXiTm_E9V-iEpnoNH9-4FerXZFiTrc4TBo5CmctvweZmj_9r6iPvL32ZISKrYIt0wQ7GhN0osIvDFwiwVOc_Mkx7FqdrgqSQ3Bif6kgYhZyR6aQy2zFMa8g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5e8d7516f6.mp4?token=WVdcCrpVoyGIYMmgfZ_qJnM_cLrSHFCW8jUL-KM4r0LqWsZ0XXUO2iiep_v1GDjEi_nsBPEpyi05rVVdCni4GfnFCe4sdL9Fobw1dPdvybQLB6Vy2KQHzaBGj-o6f9augzt3FIhQFUHKM-FnF3ViCg5APWGfS0hOZMZINTX7ag_jjuBBGIgnzVcxIdp23qPezuxf_e3XbdBKTUQdsMZltdlNKpNLNX1wXiTm_E9V-iEpnoNH9-4FerXZFiTrc4TBo5CmctvweZmj_9r6iPvL32ZISKrYIt0wQ7GhN0osIvDFwiwVOc_Mkx7FqdrgqSQ3Bif6kgYhZyR6aQy2zFMa8g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
وضعیت کنونی در مریخ از دید مریخ‌نورد Curiosity
🔹
این ویدئو در روز ۱۳۵۳‌امِ حضور مریخ‌نورد روی سیاره تهیه شده است.
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/akhbarefori/654605" target="_blank">📅 11:57 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654604">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">♦️
ترامپ به بیمارستان رفت اما از مجروحان جنگ ایران عیادت نکرد!
سی‌بی‌اس‌نیوز:
🔹
وقتی ترامپ روز سه‌شنبه برای معاینه شش ماهه خود به مرکز پزشکی والتر رید رفت، با اعضای سرویس آمریکایی نیز دیدار کرد اما به گفته یک مقام نظامی، او هیچ یک از ۱۴ سرباز مجروح در جنگ با ایران را ندید./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/akhbarefori/654604" target="_blank">📅 11:44 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654603">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفوری گرافی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ktv_RSMChjLUbhh8FaCJiGeoTsyVFQi5aGqZx0O4xgR10cSQ25qavMaoRDzr4qamhcfn8C8GpjkpYyvQYF-r4YYKodMSn41XxBKdCAqYbA0v91Llontxe1YvmxbuGoAncBksklBK4ay_bzRzuDXXL2TN6rrMJ70vmBX-bIo0HpgkTVW9T4MMJNyx8NRgg0yOklc9EghDfkBou8HgaCrfTztVVRPiaJXIzftRFWK0z-O-u6p694H5EBUKmjMibB4OmL-BfPzK3--V-xvc1jlAtAQa8qsJxSuVt9pmwWaWMqmIF7_mq9iHIjZ4Ku5J80xluLK4Iu0vKhfORemEAIM__w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
نسبت قیمت یک متر مسکن به یک گرم طلا در ۱۰ سال اخیر
#اینفوگرافی
@Fori_Graphi</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/akhbarefori/654603" target="_blank">📅 11:39 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654601">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/npoaDmYL7auMAVJ1L6GDghB-0osxNSnKHdjeUzjFTW4KCrJW-s8MXrFUBVmdpM1an2oZDGUD6s_L-oYdIQyxhJ9Lh3M-0ml5RzxoJl_GSBiCqKDw4svYjDpEuWggQZ9qVj7IjCyWhYS89Ae06c9cOxgqFmP5X5nDqCzvYPOsZ_nG-U81_Cjpjnc4bxC1vgtgCn-dP35ZOuE1UkVqV7ahB2l77aBiNaRwh29KTPXDz-kx3XU8Djqbdt8RJ-5SkTmQO3p8tF_ZmjhmB_l5ThGeEiSD9vs0g0qHNBsTiNtuttqNGSs5qL6-tqoxe3qO3Fewjhj8BukAFtPnWzfH5fI5Pg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
چه گروه‌های خونی بیشتر در معرض سکته مغزی هستند؟
#سلامتی
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/akhbarefori/654601" target="_blank">📅 11:33 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654599">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3811cf74e2.mp4?token=P7BNvKqrJ_pP_iSsMhaUPoLJD4lb1PhmU3UZaCeMtVH-lqeFQCE-cnSRTv8de5ZW-RVOAUeQViJPLK383dIrdr6oC-gRstoeIqDmLHGwfUJpDKNavQ_tCq8cHZC9PxsDOy0TwtT1zOUxEDS7iKoJMViI4Z85ITeHH_DxdVgiD3cShviX8qWcqJ7Hu-K1HFYm7AINbsHtQpagPe79vTtdpupe1pdDzOT6lZwOCeSZuu1-73UF-NauMETdpJWzVbzPkd8X5plRJ71r31Omt066wAFqsJR0DwjSWa2FFV9GMTpEeCT4xqR6r-rMGfKzLRuOwCyLCF12xpGu-Qk53WiDZA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3811cf74e2.mp4?token=P7BNvKqrJ_pP_iSsMhaUPoLJD4lb1PhmU3UZaCeMtVH-lqeFQCE-cnSRTv8de5ZW-RVOAUeQViJPLK383dIrdr6oC-gRstoeIqDmLHGwfUJpDKNavQ_tCq8cHZC9PxsDOy0TwtT1zOUxEDS7iKoJMViI4Z85ITeHH_DxdVgiD3cShviX8qWcqJ7Hu-K1HFYm7AINbsHtQpagPe79vTtdpupe1pdDzOT6lZwOCeSZuu1-73UF-NauMETdpJWzVbzPkd8X5plRJ71r31Omt066wAFqsJR0DwjSWa2FFV9GMTpEeCT4xqR6r-rMGfKzLRuOwCyLCF12xpGu-Qk53WiDZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
معاون ترامپ: آتش‌بس با ایران همچنان برقرار است
ونس:
🔹
اگر وضعیت فعلی جنگ با ایران را با ۵-۶ هفته پیش مقایسه کنید، به نظرم کاملاً مشهود است که آتش‌بس تا حد زیادی برقرار است.
🔹
در زمان برقراری آتش‌بس گاهی تنش‌های جزئی و پراکنده رخ می‌دهد.
🔹
این نوع آتش‌بس‌ها همیشه تا حدی پیچیده و بی‌نظم هستند؛ گاهی اوقات نیروهای رده‌پایین با مقامات سطوح بالا هماهنگ نیستند و ارتباط درستی ندارند. بعضی وقت‌ها هم افراد مرتکب اشتباه می‌شوند.
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/akhbarefori/654599" target="_blank">📅 11:06 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654598">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3a3a90562c.mp4?token=KI2O3IDk_n36a_0EtI3rkyEkIk_G_s12zOcOra4wD68MY2qzt7cDjUBw4bpNeerXBFsQ72-E_FgX3YdglcD4zj5tWcvCl7PN0Vg_uEgqhksTXKwR1M3zjfdOU1Kl0wk0zHuNn1bVqNNMsrTg_vpkNYGKKnuxQOnXn5bDNy2oyE55LQk5p1jAWnZTPNMnJ9fFr42KnTeUh_TG8bPiNL-VU8RyENx0088dSzZfgqzXMXxG0VuQ28XLmLXHbj9sT3mVNtBAsk1X1iWyhlBWeaDeVYICgT1_qBFyygarM76NZY2kEmuxnmp9SkBS9gB5lTYNsWVEzKxJPPenSOBCUW6fAg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3a3a90562c.mp4?token=KI2O3IDk_n36a_0EtI3rkyEkIk_G_s12zOcOra4wD68MY2qzt7cDjUBw4bpNeerXBFsQ72-E_FgX3YdglcD4zj5tWcvCl7PN0Vg_uEgqhksTXKwR1M3zjfdOU1Kl0wk0zHuNn1bVqNNMsrTg_vpkNYGKKnuxQOnXn5bDNy2oyE55LQk5p1jAWnZTPNMnJ9fFr42KnTeUh_TG8bPiNL-VU8RyENx0088dSzZfgqzXMXxG0VuQ28XLmLXHbj9sT3mVNtBAsk1X1iWyhlBWeaDeVYICgT1_qBFyygarM76NZY2kEmuxnmp9SkBS9gB5lTYNsWVEzKxJPPenSOBCUW6fAg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
دریاچه ارومیه دوباره پرآب شد
🔹
تصاویر جدید از وضعیت فعلی دریاچه ارومیه
#اخبار_آذربایجان_غربی
در فضای مجازی
👇
@azarbaijan_gharbi</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/akhbarefori/654598" target="_blank">📅 11:00 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654597">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YGciVeHvKM4KspQWKd3EYGNQJVWwDDcV4iF2CKFxxrt4bI5tb97pq3EWm6zyGSi66GMBaxgpiqP12EXP4dCXpgMm_pwqtyf-frVB3cFBVlhSb2OL8qUrlKBsVCf8kuwCaZlHlTTW9t-2nBS8Sj4NJmdsGXhbtQ6Cm-u3nYBDpcQKqV5jkezxS7z4qf7zE13rCm02eyMxuQ9Pdk3jDuQEApjTpYCMKLWyfLmYRqlSJfhdtUQS5TwRYaFSu8P_woboA-pbnIAwGycS-HFq2QYhxyoWZOZJmkKpGcAdhZ9t51XOdRlQVhh-BGNZCuwjpVM2HddaX3xq0kUNdPImBEdLiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
صحنه عجیب، زیبا و تاریخی از غروب زمین در پشت ماه، از زاویه دید فضانوردان ماموریت آرتمیس ۲ ناسا
🇮🇷
✊
@AkhbareFori | khabarfoori.com</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/akhbarefori/654597" target="_blank">📅 10:50 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654596">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/db822NoSg8Sk59QQJUGyvQ7udphyMF0nZIDuyJ1twA2wWylRxQJbxN9jYOGbllsUetFOTVyYdf54xJEItu24rzZGcSWShWX4SGYHu4m6zK-aqBOamTeceoB6UeRl2xp7a-BqUxaPcX-UHt7OSSJV2m4NeF3BBdf0b4df8bfPfAEQ_c0gAp7cstAUyfh19ELqWDujzrsdoNZ8nQTOUA59oI3aRlJk8V3OF9iXj3E8APYIyxuma2tqQBm6nmjre-zGEACAhWq_xn5C3z2AKoUoMWlUvOk3GFXOAVAWYYLWvNv_-aOmE0evt9hh2LUOhi8YrN8_U8j6H5iR-zNivkqvrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
فرماندار جم: یک هواگرد متخاصم منهدم شد/ هم‌اینک وضعیت شهر عادی است
🇮🇷
✊
@AkhbareFori | khabarfoori.com</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/akhbarefori/654596" target="_blank">📅 10:46 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654595">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">♦️
آموزش‌وپرورش: در همه پیام‌رسان‌های ایرانی می‌توان آزمون برگزار کرد
آموزش‌وپرورش:
🔹
مدارس برای اخذ آزمون‌های غیرحضوری می‌توانند از انواع پیام‌رسان‌های ایرانی با اولویت شاد استفاده کنند.
🔹
خبر "مجاز بودن برگزاری آزمون صرفا در سامانه شاد" تکذیب می‌شود.
🔹
فرآیند ارزشیابی پایانی نوبت دوم مدارس از روز شنبه نهم خرداد آغاز می‌شود.
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/akhbarefori/654595" target="_blank">📅 10:31 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654594">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MsWaFTCz_-7X2crblswjs-qdQ2ysqBT4sbzUWPL0PC6M5PG0sqyRAN7QLe9DFcxTZrN7A7p6WBwJjXZuM6Zp7n9sd1bjQJaF4WlYvjZR6OE1tEH8jPNKO7lAKCbWeU6VNnz0X0Dcgd-1pVxBF7Lz64Ywi_MAGkGDmvN_LXkFuaLT6vwPfPnw0qU5m7uXArQxWgeJcWcLsiIQp6tJ590ZCwpSmgzlxqV9udPfnLnMs0xSUi5uiIp1eL20F4-uyhti0KgD0N8ZJj6xwqtXmKbCTK8AlwxlRNFkA_0dsa1UsZ4Q8Hcy1BbrfBzIL6DNmLLRUK3Wl04dIjQOIqNiV2q_vA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
استاديوم‌های میزبان جام جهانی ۲۰۲۶
#جام_جهانی_۲٠۲۶
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/akhbarefori/654594" target="_blank">📅 10:25 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654593">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/23b2f826a9.mp4?token=JlJLXpxBj5FbW-whlz4Xzz_PwzPr507kbAV30kiXGIMG_IQXSA9OR_IQrvUIv-Ssed33C0Ll7X_GZcDomGFALln0fFEKdkJEIJZaFB-lBjHeC97XZwJEXVcRgazcDz9tCoyGzZcq5Nyb_Musw-0-TiHEbijYMQx7M6UghxiBYYjKz11f-fo9TGWpx4w3CorIUs25iVln7gg4BJ1hD6jpeExByuIa8lr-eH1GH2TD4OOqlYsD-yij3oKGXuJ6VNnaN6sYK2ut_eZFd7JSRBEkHh_uIYl9fKWssacDHTRcri7CpU3RAlgCMgdCZuOzJ47dD2Rg34mNAZZNlT0hZlH6-w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/23b2f826a9.mp4?token=JlJLXpxBj5FbW-whlz4Xzz_PwzPr507kbAV30kiXGIMG_IQXSA9OR_IQrvUIv-Ssed33C0Ll7X_GZcDomGFALln0fFEKdkJEIJZaFB-lBjHeC97XZwJEXVcRgazcDz9tCoyGzZcq5Nyb_Musw-0-TiHEbijYMQx7M6UghxiBYYjKz11f-fo9TGWpx4w3CorIUs25iVln7gg4BJ1hD6jpeExByuIa8lr-eH1GH2TD4OOqlYsD-yij3oKGXuJ6VNnaN6sYK2ut_eZFd7JSRBEkHh_uIYl9fKWssacDHTRcri7CpU3RAlgCMgdCZuOzJ47dD2Rg34mNAZZNlT0hZlH6-w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حادثه ترسناک در شهربازی تگزاس
🔹
۸ نفر پس از توقف ناگهانی ترن هوایی، در بالاترین نقطه مسیر معلق ماندند و عملیات نجات آن‌ها با حضور آتش‌نشانی و تجهیزات ویژه انجام شد.
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/akhbarefori/654593" target="_blank">📅 10:05 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654591">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vccwU-OTCumepWd7VrPy0eSGMrLh-THqHbAUcb6KcA3wCCWP5dgyNEcnOPUGd0ri597Y_ncybor0-j4sS1kK7mRSeck00YkxUJOPESXZ8JhB7-s5h5b-ar3dIz0U9J2GOi_3cslLrrqmJD-jJFmo8VnBwJ8X7PCDQ4Y4maeNzr03go5wa7rj43Re8LItCNcXhDOIphF7xY26pucHxwCeWIYGXojXTLwcNGotn2v0kU4DS2AYhMGE8mXNiwAaWn74m6p8lTvBeYevO6En4S8qDiZuynCWSyjLUjke_WUQYkJScfk2xOnETO-lgqxxTgPHxeL3k_wiUezQWcssaAFEwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gtL570j_O5GD_mWwK5my1rgEyHT11UVSy2IJgZ4QJvQ1lyNvAKf2nreJGjKHtKuj44-JqsN6ZloyYkogyY--mL5brlRyJhxe8JZYLURlKkGZaj-3dvptnbfrH0CyHh6KxSCNMutZunrQrf69cygqblnIHkSerHbwAR6e63zKefEdO6nmOYazFHwak0f5EGKDwD6rT98sGYg-AK8O0H54IEw3igV7P1PP4KBO4b_9JN9UZcxbg3O2c3Z7cotfyY_pknFMk6Vx200GvyADajiBhNUf3kUFFcC_LTqWC54b3r8NRhlhQu9JD5gsv5Zm1jpsVHNIK-PiOfB8AKDp-oY5aw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
ناشناخته‌ترین بازیکن جام جهانی ۲۰۲۶ حالا دیگر ناشناخته نیست!
🔹
تیم پِین، مدافع نیوزیلند و یکی از حریفان ایران در جام جهانی ۲۰۲۶، تا چند روز پیش فقط ۴ هزار فالوور در اینستاگرام داشت.
🔹
یک اینفلوئنسر آرژانتینی او را به عنوان «ناشناخته‌ترین بازیکن جام جهانی» معرفی کرد و از کاربران خواست صفحه‌اش را دنبال کنند.
🔹
همین ویدیو کافی بود تا تعداد فالوورهای این بازیکن باشگاه ولینگتون فینیکس به ۱.۴ میلیون نفر برسد!
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/akhbarefori/654591" target="_blank">📅 09:55 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654590">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d5859f60eb.mp4?token=dApMdQfV6leIaCkRGRNA0YIQhtZpL-aGi2d8nbPw-_LrIeRyA2dREhBD5Ho2SqCZXQs1XW-vDTFgXGdOOhNbUreiHuuW-PbXUsmEubniIza7bMC8ThCzYSZ01l-ICkBiiWUYWtRqRxrcr4ifYdsr5l9YKUUZomE5uuzdEHXaSCa4h15sL4EmKxTzH6gnGh_zB3ka4nZ0mwQFrinI4uiZeHJD8I7tyUenGusvLpXn6aJa8WO2rVmy6Efyu9waHcS3WVTwKzWULK-Ss6FDKe2QGXGVbuRxIsVCSGri2bJ4XYT2hchHXY4jNAswC1pqS_GS-0NVNi4v7rWKsNA5mWO4zA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d5859f60eb.mp4?token=dApMdQfV6leIaCkRGRNA0YIQhtZpL-aGi2d8nbPw-_LrIeRyA2dREhBD5Ho2SqCZXQs1XW-vDTFgXGdOOhNbUreiHuuW-PbXUsmEubniIza7bMC8ThCzYSZ01l-ICkBiiWUYWtRqRxrcr4ifYdsr5l9YKUUZomE5uuzdEHXaSCa4h15sL4EmKxTzH6gnGh_zB3ka4nZ0mwQFrinI4uiZeHJD8I7tyUenGusvLpXn6aJa8WO2rVmy6Efyu9waHcS3WVTwKzWULK-Ss6FDKe2QGXGVbuRxIsVCSGri2bJ4XYT2hchHXY4jNAswC1pqS_GS-0NVNi4v7rWKsNA5mWO4zA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
صحنه عجیب، زیبا و تاریخی از غروب زمین در پشت ماه، از زاویه دید فضانوردان ماموریت آرتمیس ۲ ناسا
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/akhbarefori/654590" target="_blank">📅 09:50 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654589">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/82564870e9.mp4?token=tAlpahvCJoGIaShpQbuAKEnV6MzBAq-sxSeDoi4D76LchUEHjAYLV9flZ-e7HzjbJq93TTeICCRYE-1ANFTGWAJbArkc6ZZxr5nX9V74N5JSl_nc_lDgB-dctTYke0HKyaOtMQNscJwEuch4dnmmgrNA7bLLxtvv45KPtqkn2A1IVpd1Du1SDZzTm4OTHy7loIj4qLMqw3HJ_I-x-KkCKSXivw6SNSbMzqayp88t1r6ZpEtvkH26z-v2dndTx5r_y4yfK6jlihWXRQMlfy2WgDU7xsfGLwDqknz7PEpovy5bb0kz0kq4EfrZHlB71hHRNKg9YZc4QfQs1xs2eso10w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/82564870e9.mp4?token=tAlpahvCJoGIaShpQbuAKEnV6MzBAq-sxSeDoi4D76LchUEHjAYLV9flZ-e7HzjbJq93TTeICCRYE-1ANFTGWAJbArkc6ZZxr5nX9V74N5JSl_nc_lDgB-dctTYke0HKyaOtMQNscJwEuch4dnmmgrNA7bLLxtvv45KPtqkn2A1IVpd1Du1SDZzTm4OTHy7loIj4qLMqw3HJ_I-x-KkCKSXivw6SNSbMzqayp88t1r6ZpEtvkH26z-v2dndTx5r_y4yfK6jlihWXRQMlfy2WgDU7xsfGLwDqknz7PEpovy5bb0kz0kq4EfrZHlB71hHRNKg9YZc4QfQs1xs2eso10w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
رونمایی از مجسمه‌های بادی غول‌پیکر یامال، مسی و پولیسیچ در فاصله ۱۳ روز تا جام جهانی در اسکله «سانتا مونیکا»
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/akhbarefori/654589" target="_blank">📅 09:44 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654587">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/92e24de456.mp4?token=DyODWx5WLB5SfarDZXESpk2xzMKwO8uT27eVqbxdGqAHF_vFtLPPsfjOoWvlo0K6ycqy8g5JQEIE6C9lQewPt9XuJbAc8Wq8sPAYgoiiaGbnMrwJVPz_QZibxFDm1MV0ULokZphfSewGWmBP-yfdqenjwoL6pyMkRVKiDhUjmlqlNSu1jMz1WQUTh1k2pvVfLF6z_48-s8EEtdv8VQuF9WJHFb7dCF1DKYcfgtWdhov6ggxpb5inGiMWnxG2-LR6skll32r1shPRZK34qKSSkbn-mmfT2cQaFKJPGUQO-PbQxu_APmYbQbi2OiaCXppfCLBHQNhDzUHT2incty1prw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/92e24de456.mp4?token=DyODWx5WLB5SfarDZXESpk2xzMKwO8uT27eVqbxdGqAHF_vFtLPPsfjOoWvlo0K6ycqy8g5JQEIE6C9lQewPt9XuJbAc8Wq8sPAYgoiiaGbnMrwJVPz_QZibxFDm1MV0ULokZphfSewGWmBP-yfdqenjwoL6pyMkRVKiDhUjmlqlNSu1jMz1WQUTh1k2pvVfLF6z_48-s8EEtdv8VQuF9WJHFb7dCF1DKYcfgtWdhov6ggxpb5inGiMWnxG2-LR6skll32r1shPRZK34qKSSkbn-mmfT2cQaFKJPGUQO-PbQxu_APmYbQbi2OiaCXppfCLBHQNhDzUHT2incty1prw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
الکس یانگر رئیس سابق MI6: ایران در جنگ دست بالا را دارد
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/akhbarefori/654587" target="_blank">📅 09:17 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654586">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">♦️
سازمان سنجش: مهلت ثبت‌نام آزمون سراسری امشب (۸ خرداد) به پایان می‌رسد و تمدید نخواهد شد.
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/akhbarefori/654586" target="_blank">📅 09:07 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654585">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5df31a1411.mp4?token=k3SvlBsfsBVlhi1oCtvuD3zqVCyDIb6caxpQa7Vob-RHnfvTqWRm9HeFcTVavKgf2XFe3vsE-uD-qOlW4bPG2KUVXZ8qPTxY0Tb3AEzSZNpX8m8zpizhz4b-Wsf_6C5i7AT1OetIOtDXN_iRHNXOysbARMvObm5pr9chuHM4FIwcFqe9CvYb90wHWGXEXxOmKDE2o1FlJjJq4r9O-FOcm3a6ggdhvDvcrTW58819SxjhwaWVEVMPXqrFQUDZzgVBEdixOF0EGaTccv6I5XddaBIZlynIIjMXYFcRaRW0TSjk1iyBqG5EWOCvXaF4zZm0X8FhcTz46I014hUtGphnEQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5df31a1411.mp4?token=k3SvlBsfsBVlhi1oCtvuD3zqVCyDIb6caxpQa7Vob-RHnfvTqWRm9HeFcTVavKgf2XFe3vsE-uD-qOlW4bPG2KUVXZ8qPTxY0Tb3AEzSZNpX8m8zpizhz4b-Wsf_6C5i7AT1OetIOtDXN_iRHNXOysbARMvObm5pr9chuHM4FIwcFqe9CvYb90wHWGXEXxOmKDE2o1FlJjJq4r9O-FOcm3a6ggdhvDvcrTW58819SxjhwaWVEVMPXqrFQUDZzgVBEdixOF0EGaTccv6I5XddaBIZlynIIjMXYFcRaRW0TSjk1iyBqG5EWOCvXaF4zZm0X8FhcTz46I014hUtGphnEQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خودداری شهردار نیویورک از حضور در رژه روز اسرائیل
🔹
این اقدام ممدانی او را به نخستین شهردار نیویورک تبدیل می‌کند که در بیش از ۶۰ سال گذشته این رویداد را نادیده گرفته و در آن حضور نیافته است.
🔹
برخی رسانه‌ها اقدام شهردار نیویورک را پاسخ یک مقام مسلمان به جنایات رژیم صهیونیستی در غزه عنوان کرده‌اند.
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/akhbarefori/654585" target="_blank">📅 08:56 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654584">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eFf0aBRlK47q-vlgXp95R95Sw3xlEUctmW3kp6BCs6PjbRaxKPVyOClQFkmCio18e-fwgshIX_04is1rEjSpdzgzTfVX34ajMsAzCEQbPPo9Wd18e8WCaFYqHSvIWwrrttKyBInoOx9R7V_nJ8kLLXVizswGMOw9XM8MlewvnE7rDH3ANp0jlCij13SjNXt_tUsVwtFkH3vpmS0rpze3I_0NrY1LvdkOoHqOwLjfY3GEwk2QmVMf5nDdzczIwA5UHr8X9nAoGz1GdNXM5PojjOS9HulAF8po4GS-tl5hqTUL5wlLfeLxndyC-OI589fxOczdhj62sa6ZgnDCgOsMiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ایران ۱۵ پله بالاتر از عربستان در جام جهانی
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/akhbarefori/654584" target="_blank">📅 08:49 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654582">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qo3es8sYo5830FAc0EKO7ZWrt374EYE5Y0fY2-xvrTRkhDMCjA3I76hBEL9UNyKpHRtMK9LSj5ujRodh8kIwgJ0t5UM8qXyPfznW38Tni5bkppYynMQcw4TjSWsXasmlfy--M6Fiqrk-mj005cmETnfbR73B_4u2SHDEkYqAV9KduFS0TrzfxlWS4ieyRNZ9OwxZ06sVOdcX_a3PD29DSpo2UR9LnfEN1kuu5Ty4I_FZWu1ZqU1Z2u9C2rsW0lJ6oTbFyWTpkB_9jGOsB4Thl7mJDM4RPoquyrAJnOxWdLEwtzhs1waVbEDPp6OXX_agMibOiHtd9jk8h7U8ynQ9bA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
زمین با النینو وارد منطقه خطر شد
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/akhbarefori/654582" target="_blank">📅 08:40 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654581">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">♦️
جی‌دی ونس: تعیین تاریخ دقیقی برای امضای یادداشت تفاهم با ایران دشوار است
جی‌دی ونس:
🔹
در مذاکرات با ایران پیشرفت‌هایی حاصل شده، اما اختلاف بر سر غنی‌سازی و ذخایر اورانیوم همچنان باقی است.
🔹
رسیدن به توافق نهایی زمان‌بر و نیازمند حل جزئیات فنی است، اما دو طرف به مرحله حل مسائل باقی‌مانده نزدیک شده‌اند.
🔹
توافق احتمالی می‌تواند به بازگشایی تنگه هرمز برای کشتیرانی منجر شود.
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/akhbarefori/654581" target="_blank">📅 08:37 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654580">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b61dc42e1c.mp4?token=vnAbQQYh7q8zbRB6rAFmdh0gyzsSR-f3kXAVO0Dtw6XGs3pQvXa4XrxfTT2cQAPhMITqV6IcMLR6E9GANQOvCj5CJxsEMkCuU9Ge4buqwkw5BfoFRds4CEn42yapVanHR7kCt0Zt4n_jYZCjBnovtvam6ZksR7vQ_LmxYYduWhm1Y9IdcWJ6SzZt_30wUZMvQti8bHtIuyXgS3TXCzDUS3-DqE2jsS6ETCFZuVrXw5AE5GO6OpMJhofPkP3FD4JIp2GVxuN3IEwHG2X9HDpddkCgDC_kD0Jm9xPi5INZtIje5YVRjyRGRGIESHV1iO0rW54Kte0ikkEBfHwnausbeA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b61dc42e1c.mp4?token=vnAbQQYh7q8zbRB6rAFmdh0gyzsSR-f3kXAVO0Dtw6XGs3pQvXa4XrxfTT2cQAPhMITqV6IcMLR6E9GANQOvCj5CJxsEMkCuU9Ge4buqwkw5BfoFRds4CEn42yapVanHR7kCt0Zt4n_jYZCjBnovtvam6ZksR7vQ_LmxYYduWhm1Y9IdcWJ6SzZt_30wUZMvQti8bHtIuyXgS3TXCzDUS3-DqE2jsS6ETCFZuVrXw5AE5GO6OpMJhofPkP3FD4JIp2GVxuN3IEwHG2X9HDpddkCgDC_kD0Jm9xPi5INZtIje5YVRjyRGRGIESHV1iO0rW54Kte0ikkEBfHwnausbeA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
شکست آزمایش راکت شرکت آمازون با انفجار شدید
🔹
راکت «نیو گلن» متعلق به شرکت Blue Origin، بامداد پنجشنبه در جریان یک آزمایش زمینی موتور در سکوی پرتاب «ال‌سی-۳۶» واقع در کیپ کاناورال ایالت فلوریدا دچار انفجار شد
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/akhbarefori/654580" target="_blank">📅 08:31 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654579">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jOsKXP0svVSt5HuKNl95zWJhCLAk3aOWHgeXj7euuAhxztfxa0LvjQLBrwgj2a1q8rj14mgH3PwjtrmQmi0kKXXTWrVTVMQf8VasU9Mr-DmPm1k6jSCHNqEBZQAKDMKu_l6zj5KEksmtWn3vHbeck1GdvSutcv2C1tRSwrxdlFEYufenQ1qNoUBZKklrcO2SVOLHL-XSUFiMpe7KxsaAeb7Qc3oHF1y8gJ4RfHw20D5BWu2n0H7Yh6gav-NbtXi14SI5Sku9ql9rAqrz_rffTCKHg103Dfu32IhAtIGYDB8X8VfqZdXXxPRjwqRWIhkoMXXhbHJiGumwudv0FU-Btw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پزشکیان: سیاست ایران گسترش همکاری با کشورهای مسلمان و همسایه در همهٔ زمینه‌هاست
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/akhbarefori/654579" target="_blank">📅 08:24 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654578">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1d77c76ec4.mp4?token=A1yg65irEINtSihP_yRKA-06vndMJ4psffqm0cWLRclTWjkzEmUK9KWCCn8nYfTIbFNbz0VlU8Py4Ok289_pkTIsvKecWIb6f8xdcIZ9K8gzUGldu6tLlVrcfSni4imnO2Ppd7bSReTu9pcmSx7Z2iwCJOeM5tYP3_7quT0qMTPuhnsNZk4iCplh-eY1pee8iHGbSfPWcN6JnFuLNm7EAJ860H_ORqVksQPtRu-8qHRzTcgSukBmpwG2Pas9BAppyucqtmnUVtYI7S2kGSccd66p5vQaQ4hI3N0jpruCeWl_1pIJVT0i1QuwM4FvdtLMOItht52w53gsLSsGW1OU4A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1d77c76ec4.mp4?token=A1yg65irEINtSihP_yRKA-06vndMJ4psffqm0cWLRclTWjkzEmUK9KWCCn8nYfTIbFNbz0VlU8Py4Ok289_pkTIsvKecWIb6f8xdcIZ9K8gzUGldu6tLlVrcfSni4imnO2Ppd7bSReTu9pcmSx7Z2iwCJOeM5tYP3_7quT0qMTPuhnsNZk4iCplh-eY1pee8iHGbSfPWcN6JnFuLNm7EAJ860H_ORqVksQPtRu-8qHRzTcgSukBmpwG2Pas9BAppyucqtmnUVtYI7S2kGSccd66p5vQaQ4hI3N0jpruCeWl_1pIJVT0i1QuwM4FvdtLMOItht52w53gsLSsGW1OU4A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
موتورسیکلت برقی خودران در خیابان‌های چین
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/akhbarefori/654578" target="_blank">📅 08:21 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654577">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g_xIl3ku6pOq3ILNrEwXP0xVcDs7LjN-vB1OVa5vyMUaynM6x6ETjjs_il_1wwfFE9uQR0M0we6lUDb3uzJcqiwBDyf-4H_zKb2PqSJZ3-Ky9pKo8vFI-tMaxCIe_7udXWP-9gQSa1G3VsXON2ZtN1dqsOmUOszhW9UWpdlryivy0UWOfVp304pSFZoqC8QcNII3ij-Nx9tj1iILXgLU2MtOmD_Ka_ST60oBAMjlmqb5iJa0ccQv9KpukJ1y5WeVuNxayGAoSjQe8Af8E90ijTRKT21_d67aDisSnTZs6_fL-O4Y-Rb1G825HXyU5eQ7dBzwDwBWKxijMzx3YNbrQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
خبرنگار مطرح آمریکایی: ما توسط احمق‌های شرور اداره می‌شویم
آرون روپار، خبرنگار مطرح آمریکایی:
🔹
قابل توجه است که وزارت امور خارجه تهدید دیوانه‌وار ترامپ مبنی بر منفجر کردن [عمان] یکی از وفادارترین متحدان ما در خاورمیانه را بزرگنمایی می‌کند. ما توسط احمق‌های شرور اداره می‌شویم.
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/akhbarefori/654577" target="_blank">📅 08:11 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654575">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EmQu9gY1jEmH2G_RRajAgNRJs_K8bJ7QAD7iv4dPwWRNbN0Uar8w5ZIOqPYI0-8IIs73VW857wjD28fxBD7z99-0YruGt56qr5sI7k0RV5YtHl-QIPzEKsdfXs0-Z_2Idtm-UZT9dT4I3DZiR3gkTJQBep3nzvNW_OIty5V3S4wLqw8HtojJfgk8BvGSSTlEIeS16Bk7MSexjuv9ZrPoVuopsXp9wSQQRlkenBGD-5801LDzLAh_MHmJG34qTPKUoTJm3oU6aPy__G85LPZJ3YrT6TqMb6pPQ9Gs_MfluLYQ3E5QzHRg0H1ZWi5Jx-hZSWQZ8tB8c7xV5wJyvrd9gQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هر روز خود را آغاز کنید با:
بِسْمِ اللَّـهِ الرَّحْمَـٰنِ الرَّحِيمِ
🔹
با خواندن دعای عهد و چند دقیقه گفتگو روزانه با امام زمان (عج)، پیمان همراهی و خدمتگزاری‌مان را تازه کنیم.
#صبح_نو
امروز جمعه
۸ خرداد ماه
۱۲ ذی‌الحجه ۱۴۴۷
۲۹ می ۲۰۲۶
جمعه‌ها
#دعای_ندبه
بخوانیم
⬅️
متن و صوت دعای ندبه
@AkhbareFori</div>
<div class="tg-footer">👁️ 32.2K · <a href="https://t.me/akhbarefori/654575" target="_blank">📅 08:00 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654574">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fad9145928.mp4?token=GN7basp_dPLh6FVKjlm9YpDwGlqH9z26YdPkkx8Cn2u12XbAGFGXwBL7TzLDqm71htjwpLx3uor_D9KrCLZKHOZj0kIEPKXls9kKZMYEakpNHLB3JnvYBllaQnQAqdFa4Hbw48uTZ54vDmUJMTce33hJICqAf3vrS541CEy_uqTKLQRMYBrxjFKQtuAgTD07oILSCeep7DIjoZQV9D8SuzaxbaLieiquhuNALXFQJEEAX4KZpKOH4-oWLQqIFifk4Plpl8vEjz6vcroWAuggn5bZKlkJJqI3EMIAT7sxuJ1z2PeRYG4MFNY5Tf23FVfKWrXEUo-ALaphCISva1oLZw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fad9145928.mp4?token=GN7basp_dPLh6FVKjlm9YpDwGlqH9z26YdPkkx8Cn2u12XbAGFGXwBL7TzLDqm71htjwpLx3uor_D9KrCLZKHOZj0kIEPKXls9kKZMYEakpNHLB3JnvYBllaQnQAqdFa4Hbw48uTZ54vDmUJMTce33hJICqAf3vrS541CEy_uqTKLQRMYBrxjFKQtuAgTD07oILSCeep7DIjoZQV9D8SuzaxbaLieiquhuNALXFQJEEAX4KZpKOH4-oWLQqIFifk4Plpl8vEjz6vcroWAuggn5bZKlkJJqI3EMIAT7sxuJ1z2PeRYG4MFNY5Tf23FVfKWrXEUo-ALaphCISva1oLZw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فروش فوری ویلا مدرن در شمال
- اطلاعات بیشتر و ارتباط با ما وارد لینک زیر شوید :
https://ble.ir/vila_aghsat
🏕️
ویلا مدرن نوساز
،داخل شهرک
🔥
✅
متراژ زمین ۵۰۰
✅
متراژ بنا ۳۵۰
✅
۳ خوابه (مستر)
✅
روف گاردن با ویوی ابدی جنگل و استخر چهار فصل
✅
معاوضه با خودرو ،طلا،دلار و...
✅️
دارای سند تکبرگ
✅️
⭐
اقساط بدون بهره
⭐
قیمت ۱۵میلیارد کلید تحویل
-برای اطلاعات بیشتر و ارتباط با ما وارد لینک زیر شوید :
https://ble.ir/vila_aghsat</div>
<div class="tg-footer">👁️ 45.2K · <a href="https://t.me/akhbarefori/654574" target="_blank">📅 01:28 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654573">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">آفــرتــورهــای ارزان و لحظـه آخری
جهان گستر پرواز شرق
🚀
🔻
ویـژه بـهـار 1405
🌱
🇮🇷
تــورهای داخلی:
🏝️
🚂
قشم : 5.700.000
🕌
🚆
مشهد ریلی: 3.800.000
🕌
✈️
مشهد هوایی: 13.500.000
🏛️
🚞
شیراز ریلی: 5.500.000
🏛️
🛫
شیراز هوایی: 15.700.000
🌎
تـورهای خـارجی:
⛪️
🇦🇲
ارمنستان:19.500.000
🏔️
🇬🇪
گرجستان: 34.370.000
🏙️
🇦🇿
باکو: 59.400.000
🕌
🇴🇲
عمان: 39.900.000
🇹🇷
تــورهای ترکـیه:
🛍️
وان: 7.900.000
🌉
استانبول: 44.200.000
🏖️
آنتالیا: 67.990.000
🏕️
مارماریس: 290$+ 34.500.000
🏝️
کوشی داسی: 118$ + 40.000.000
🚤
ازمیر: 147$ + 40.000.000
🚢
بدروم: 171$ + 40.000.000
🖼️
فتحیه: 104.890.000
🏞️
ترابزون: 38.000.000
🌌
آنکارا: 49.900.000
💥
آفـــرهای ویـژه:
🌴
🇹🇭
تایلند: 100.000.000
❄️
🇷🇺
روسیه: 265$ +49.000.000
🏙️
🇲🇾
مالزی:114$ + 140.000.000
🌊
🇹🇳
تونس: 890$ + 99.000.000
🗺️
🇻🇳
ویتنام: 1.590$ + 149.000.000
💰
امکان رزرو به صورت نقد و اقساط
📞
جـهـت رزرو و دریـافــت اطـلاعــات بـیـشـتـر:
🌍
جـهـت آشـنـایـی بـا خــدمـات مـا:
05131714
☎️
https://t.me/fullticket
🌐
https://fullticket.ir
☑️
لینک کـانـال بـلـه:
https://ble.ir/fulltikitir</div>
<div class="tg-footer">👁️ 42.6K · <a href="https://t.me/akhbarefori/654573" target="_blank">📅 01:28 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654572">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromخبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JtuAAVbahY5XSNi8OIgbWwoqrtq-5a6vx5pujKiUMQagJb0zdNkOD6cCTQqrJfCNX0n8lnzZvx0AQy3InBdmzME449TmY8NGhOoF8s7dDU7xLUPplKd7aJT-0UP6zt-w3YwigoJApjgG1xQjyd-G6E1p1N-Cg4owW0gx6_WgQNqpJKH4IlN2aemmDIWjr6BwwMSnrCJX-f9m-0SYHp-UK0TiJXsQfycJ3s27jJEqzwkeOlG2u7XSOLtJa_XfESazxVvB-uk_ajUUPIGUtNmuDAFGucyTuOMPeDt9oMdvP2ClSC3Qt0INEBHInjPzn-cZ4SnJXaHQRHWlVIHkTKbGCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
با هم دعای فرج را برای سلامتی و فرج آقا امام زمان(عج) می‌خوانیم
🔹
با قرائت دعای فرج به این جمع میلیونی بپیوندیم
@AkhbareFori</div>
<div class="tg-footer">👁️ 39.3K · <a href="https://t.me/akhbarefori/654572" target="_blank">📅 01:27 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654571">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">♦️
نورالدین الدغیر خبرنگار الجزیره در تهران: یادداشت تفاهم، حاصل جمع بندی مذاکرات در سطح دیپلماتیک است
🔹
برای اجرایی شدن، نیاز به امضای مقامات عالی در تهران و واشنگتن دارد
🔹
نیت توافق وجود دارد و انتظار می‌رود که از مرحله نیت به مرحله عمل منتقل شود./ انتخاب
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 43.6K · <a href="https://t.me/akhbarefori/654571" target="_blank">📅 01:02 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654570">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">♦️
افشای
فایننشال‌تایمز: کمک ۸۲۵ میلیون دلاری به «اینترنشنال» قبل از شورش‌های دی‌ماه
فایننشال‌تایمز:
🔹
شرکت مالک شبکه تروریستی «ایران اینترنشنال» اندکی قبل از شورش‌های دی‌ماه در ایران مبلغ کلان ۶۵۰ میلیون پوند معادل حدود ۸۲۵ میلیون دلار «بخشش و تسویه بدهی» از سوی سهام‌داران خود دریافت کرده است.
📲
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/akhbarefori/654570" target="_blank">📅 01:00 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654569">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/60702f5550.mp4?token=DURrOivJFDMBOABUd_vzdbhM40wv3e9Xr7NvNsKEZFQ51z4lkTwh7Z4Ed3lJz6oIdLpasetsh6kqJrUkfLzdGHVsePfBvF8xfVwRFV7Y82_wklbfIgonHhme3kElo4M_wNuq5p0aLt67NYAZppZaLc7jR1ZQG35QiH1eeOILdYpTxNQqZcySvXVBz9IGQXka1k0OBJkAI6zS4IjHDJsTlKm-BWEXWd-OfkHCs7oZalJfMIDsvsqMG1hG-0Cj2QTNr3VITryJY12d3ojyg1-fUQw5jaQvUUF_1fJfUNjoKHuS7m_Y5t6lax4SBSrcy0jq8HK0X0RduK5FY1xshybCJnOywmayKD3SIrmt5Skani7mweK0fIXaTFWO5bF43v1IleBkmkbt5ROCMmi0uuICTfuX7tnNEoNPYPQQDtoMTJdTZAfh91u0ZpZIRT4DH6igTvnR2Kq6W8AcQrfdYiZjuOBwbdJ8Dw5mWhIhbcqVFwXARvjtfJ6eQDA156iySzMHw_8aqEETV35U8eSKjdYswkMUo6hlw-Nl77KCFpyJALs5ELBF6zD3QFMCbYfTm7O_CA752k_QuCuWv58MW_0_5dS9R7RtqhjHT-VPV5WQnAeLDCXDkW0sLThYWNXCfb_tqcP688MzOIBRiGpEWITSJfpNmbgWt_zbam7oyW7_FL0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/60702f5550.mp4?token=DURrOivJFDMBOABUd_vzdbhM40wv3e9Xr7NvNsKEZFQ51z4lkTwh7Z4Ed3lJz6oIdLpasetsh6kqJrUkfLzdGHVsePfBvF8xfVwRFV7Y82_wklbfIgonHhme3kElo4M_wNuq5p0aLt67NYAZppZaLc7jR1ZQG35QiH1eeOILdYpTxNQqZcySvXVBz9IGQXka1k0OBJkAI6zS4IjHDJsTlKm-BWEXWd-OfkHCs7oZalJfMIDsvsqMG1hG-0Cj2QTNr3VITryJY12d3ojyg1-fUQw5jaQvUUF_1fJfUNjoKHuS7m_Y5t6lax4SBSrcy0jq8HK0X0RduK5FY1xshybCJnOywmayKD3SIrmt5Skani7mweK0fIXaTFWO5bF43v1IleBkmkbt5ROCMmi0uuICTfuX7tnNEoNPYPQQDtoMTJdTZAfh91u0ZpZIRT4DH6igTvnR2Kq6W8AcQrfdYiZjuOBwbdJ8Dw5mWhIhbcqVFwXARvjtfJ6eQDA156iySzMHw_8aqEETV35U8eSKjdYswkMUo6hlw-Nl77KCFpyJALs5ELBF6zD3QFMCbYfTm7O_CA752k_QuCuWv58MW_0_5dS9R7RtqhjHT-VPV5WQnAeLDCXDkW0sLThYWNXCfb_tqcP688MzOIBRiGpEWITSJfpNmbgWt_zbam7oyW7_FL0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
انتشار برای اولین بار
🔹
خاطره حامد شاکرنژاد، داور برنامه محفل از اولین دیدار خصوصی با رهبر شهید انقلاب
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 47.8K · <a href="https://t.me/akhbarefori/654569" target="_blank">📅 00:39 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654566">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UMc_ShXIbrVy71Ok0YY7ZVW5v2m21Vtl619z1UOXPFYHZ0EciOaechs5w5Q9WwHuks5VAUz84ZjWC7S068FQk0IlF-FU02nYa-DHvfgS7B4GstWZiD-dgL9G9i0g6WhvYBBFM0l32RiCZvQ15MJPx4Yj0Hnabhaq4nZA0iMGSIZe0maMjHz8KLWcv71FEb49iNVPvJw_hTQ-TzW7H1YEtxVh1H64Oy_xEYyuU58qBhMT676Fx_rfd4DYOSy0Ng2YnWiSY_mTns8M7d_k3F4Sj_fuKvjArEdsX6QPPI0aMk9mdTQYKh_eLDp-HwiIn7YEQauT1k9LH-b7s9mkLdjfEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b8b16ea4bd.mp4?token=D5OaOVbk0LHJUHcCXqQbSaj0wQ-sjFa0KwYHZ8jyOfK78DZKPjvSJiZA8SAmllKkvH6-pTCOZbl7LTxf4Y08mtGQ37VFM4yoD3tKy1lPeyR3yEmjSyhOVoJ4l1kr6fUjqtALf9Njn4sQ6VQlXZwpXTFZ8E19j1iHioOOoOvgelrJqlXEyiBOxB7mMDP-O9E-WdcoMtnu4xX45tgt2SxEy44HhpAtH3NZ3QNMfxI9V4S5iu0GNVu62F5QfR-_VWVNxtVK9z-ZbA4JOJtP10PewhQtBXszZaPAhIZUd3kM1Oxi1K98MCZUPdHwnmLKDEUxdc1AVeoDN472mfAycavG2Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b8b16ea4bd.mp4?token=D5OaOVbk0LHJUHcCXqQbSaj0wQ-sjFa0KwYHZ8jyOfK78DZKPjvSJiZA8SAmllKkvH6-pTCOZbl7LTxf4Y08mtGQ37VFM4yoD3tKy1lPeyR3yEmjSyhOVoJ4l1kr6fUjqtALf9Njn4sQ6VQlXZwpXTFZ8E19j1iHioOOoOvgelrJqlXEyiBOxB7mMDP-O9E-WdcoMtnu4xX45tgt2SxEy44HhpAtH3NZ3QNMfxI9V4S5iu0GNVu62F5QfR-_VWVNxtVK9z-ZbA4JOJtP10PewhQtBXszZaPAhIZUd3kM1Oxi1K98MCZUPdHwnmLKDEUxdc1AVeoDN472mfAycavG2Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تریتا پارسی با انتشار ویدیویی از حمله به پل B1 کرج در جریان جنگ تحمیلی سوم:
با بازگشایی اینترنت در ایران، تصاویر بیشتری از آنچه واقعا در طول جنگ رخ داده، منتشر می‌شود
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 47.5K · <a href="https://t.me/akhbarefori/654566" target="_blank">📅 00:32 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654565">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromروزنامه دیجیتال خبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vbhpASOPNzFaX_p49U_QRTtUv5QJ4L7UhxR-zTyHwTgk3p94ZlYF4tR2B8t8_kiIGNkTn1NABB4hH9eR_IzDbslNMlP7cg9CzgUXB46gAHQqNiS_Qfmwi_opM7an1ibJGUTQWj-U1tRc7sRdjgjCs5uML4fwdO0mYLPLy6nnudBd6-xu2dj_QTEYhHBlHjGSmbN9qgL_NquMpnrMIj2Ckjhb59uk5qIDh62-MsLfuH8RSedSChtN598GCOChMmCIOA7JLcE1z7UUmJ7hBXOITuqyrUeFOTvuCqZMDrkB2MPMldNQq4eoUK6T3Jvh3dWYwe8xA2x4aTVqmACE309JlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پرهیز از اختلافات پوچ
رهبر معظم انقلاب به مناسبت سالروز افتتاح اولین دوره مجلس فرمودند:
🔹
از جمله مصادیق تقوا، رعایت نعمت عظیم وحدت ملّی و انسجام بی‌بدیلی است که حول پرچم ایران اسلامی به ملّت بعثت یافته ارزانی شده و در زمره‌ی مهمترین عوامل ظفر در مقابل شیطان بزرگ می‌باشد. شکر این موهبت، اهتمام آحاد ملّت خصوصاً نخبگان فکری و سیاسی از جمله نمایندگان مجلس به صیانت از این وحدت و پرهیز از اختلافات پوچ سیاسی و برجسته کردن تفاوت‌های اجتماعی است. ایشان بیان کردند: از این پس، بیش از پیش برای پاسداری از وحدت صفوف منسجم و به‌هم‌پیوسته ملّت اهتمام ورزند و اختلافات غیرموجّه و حتی موجّه را به تنازع و تفرقه تبدیل نکنند.
🔹
هفتصدوشصت‌ویکمین شماره جلد یک خبرفوری
#تیتر_یک
@rozname_fori</div>
<div class="tg-footer">👁️ 45.6K · <a href="https://t.me/akhbarefori/654565" target="_blank">📅 00:24 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654564">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">♦️
هاآرتص: ارتش اسرائیل برای احتمال از سرگیری جنگ با ایران بدون هشدار قبلی آماده می‌شود
روزنامه صهیونیستی هاآرتص:
🔹
ارتش اسرائیل برای تشدید ناگهانی تنش امنیتی با ایران آماده می‌شود. ارتش به نهادهای دولتی یا سیستم مراقبت‌های بهداشتی هشدار می‌دهد که این امر بدون اطلاع قبلی انجام خواهد شد.
🔹
مقامات ارتش اسرائیل همچنین اذعان می‌کنند که در طول جنگ، شکاف‌هایی در اعتماد عمومی به تصمیم‌گیری در مورد دستورالعمل‌های دفاع از جبهه داخلی ایجاد شده است./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 43.3K · <a href="https://t.me/akhbarefori/654564" target="_blank">📅 00:24 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654563">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">♦️
صداوسیما: دلیل صدای انفجار در شهر جم مقابله پدافند با هواگردهای متخاصم بوده است
🔹
ساعتی پیش صدایی در منطقه ۷ چاه شهرستان جم استان بوشهر صدای انفجاری شنیده شد که گفته می‌شود ناشی از مقابله پدافند با هواگردها بوده است.
🇮🇷
✊
@AkhbareFori | khabarfoori.com</div>
<div class="tg-footer">👁️ 44.7K · <a href="https://t.me/akhbarefori/654563" target="_blank">📅 00:14 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654562">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">♦️
یک منبع نظامی رهگیری یک پهپاد متجاوز آمریکایی را در اطراف بوشهر تایید کرد
🔹
به گفته این منبع نظامی، این رهگیری از طریق شلیک موشک پدافندی به سمت این پهپاد انجام شد./ تسنیم
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 47.3K · <a href="https://t.me/akhbarefori/654562" target="_blank">📅 00:03 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654561">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">♦️
صداوسیما: دلیل صدای انفجار در شهر جم مقابله پدافند با هواگردهای متخاصم بوده است
🔹
ساعتی پیش صدایی در منطقه ۷ چاه شهرستان جم استان بوشهر صدای انفجاری شنیده شد که گفته می‌شود ناشی از مقابله پدافند با هواگردها بوده است.
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/akhbarefori/654561" target="_blank">📅 23:58 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654560">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🔹
خبرهای داغ امروز و امشب را از دست ندهید
🔹
🔹
تبادل آتش دوباره میان ایران و آمریکا در کمتر از یک روز | شلیک ۴ موشک به‌سوی شناورهای آمریکایی | شنیده شدن صدای انفجار در هرمزگان و بوشهر
👇
khabarfoori.com/fa/tiny/news-3218570
🔹
این سند خبر از جنگ سوم ایران و آمریکا می‌دهد | پاشنه آشیل توافق یک صفحه‌ای چیست؟
👇
khabarfoori.com/fa/tiny/news-3218518
🔹
اخبار لحظه‌ای مذاکرات ایران و آمریکا | توافق نوقت سه روز پیش نهایی شد، فقط مانده اعلام نهایی!
👇
khabarfoori.com/fa/tiny/news-3218401
🔹
رئیس تازه ارتش آمریکا؛ یک ژنرال چهار ستاره تندرو که دوست صمیمی هگست است | کریستوفر لانو کیست؟
👇
khabarfoori.com/fa/tiny/news-3218501
🔹
راهی برای معامله نیست | چرا ترامپ نمی‌تواند ایران را وادار به عقب‌نشینی کند؟
👇
khabarfoori.com/fa/tiny/news-3218537
🔹
ویدئو‌های جذاب را در آپارات ما ببینید
🔹
http://aparat.com/Akhbar.Fori</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/akhbarefori/654560" target="_blank">📅 23:58 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654559">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">♦️
ترامپ قمارباز: ایرانی‌ها مذاکره‌کننده‌های خیلی خوبی هستند
ترامپ:
🔹
«آن‌ها مذاکره‌کنندگان بسیار خوبی هستند — خیلی حیله‌گر و زیرک‌اند — اما همه برگ‌های برنده دست ماست، چون ما آن‌ها را از نظر نظامی شکست داده‌ایم
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 46.5K · <a href="https://t.me/akhbarefori/654559" target="_blank">📅 23:49 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654557">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">♦️
منشا صدای انفجارها از سمت دریا و مربوط به تبادل آتش است
مرکز کنترل فرماندهی پدافند هوایی ارتش:
🔹
تا این لحظه انفجاری در منطقه بندرعباس رخ نداده و گزارشی در این زمینه نداشته‌ایم.
🔹
براساس گزارش پدافند ارتش، منشأ انفجارها از سمت دریا و مربوط به تبادل آتش در اخطار به کشتی‌های متخلف در تنگه هرمز بوده است.
اخبار لحظه‌ای حملات امشب را اینجا دنبال کنید
👇
khabarfoori.com/fa/tiny/news-3218570</div>
<div class="tg-footer">👁️ 48.6K · <a href="https://t.me/akhbarefori/654557" target="_blank">📅 23:38 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654556">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">♦️
غیررسمی: پدافند هوایی ایران یک پهپاد آمریکایی از نوع MQ9 را سرنگون کرد
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 48.7K · <a href="https://t.me/akhbarefori/654556" target="_blank">📅 23:36 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654555">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">♦️
تسنیم: گزارش منابع محلی حاکیست که منشا صداهایی که شنیده شده به درگیری‌های نظامی در دریا برمی‌گردد
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 49.8K · <a href="https://t.me/akhbarefori/654555" target="_blank">📅 23:34 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654554">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">♦️
گزارشات غیر رسمی از شلیک موشک هشدار به ناو آمریکایی
🔹
نیروی دریایی در نزدیکی تنگه هرمز به ۴ فروند شناور خاطی شلیک اخطار انجام داد. این شناورها قصد عبور بدون هماهنگی از تنگه هرمز را داشتند.
🇮🇷
✊
@AkhbareFori | khabarfoori.com</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/akhbarefori/654554" target="_blank">📅 23:26 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654553">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">♦️
آمریکا شخصیت‌های حقیقی و حقوقی مرتبط با ایران را تحریم کرد
🔹
دفتر کنترل دارایی‌های خارجی وزارت خزانه‌داری آمریکا، نام یک فرد، ۱۶ شرکت و ۸ کشتی را در فهرست تحریم‌های مرتبط با ایران قرار داده است.
🔹
فرد تحریم‌شده تبعه هند است و شرکت‌ها نیز در کشورهای چین، سنگاپور، قطر، جزایر مارشال و امارات مستقر هستند.
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 48.5K · <a href="https://t.me/akhbarefori/654553" target="_blank">📅 23:24 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654552">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">♦️
وزیر ورزش و جوانان: وام ازدواج حداقل ۱۰۰ میلیون تومان بیشتر می‌شود
🔹
تلاش می‌کنیم صف وام ازدواج به حداقل برسد.
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 47.7K · <a href="https://t.me/akhbarefori/654552" target="_blank">📅 23:20 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654551">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">♦️
گزارش‌های تایید نشده از صدای انفجار در هرمزگان @AkhbareFori</div>
<div class="tg-footer">👁️ 50.3K · <a href="https://t.me/akhbarefori/654551" target="_blank">📅 23:13 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654549">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">♦️
گزارش‌های تایید نشده از صدای انفجار در هرمزگان
@AkhbareFori</div>
<div class="tg-footer">👁️ 48.3K · <a href="https://t.me/akhbarefori/654549" target="_blank">📅 23:08 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654547">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">♦️
ادعای وزیر خزانه داری آمریکا: توافق با ایران به ترامپ بستگی دارد
اسکات بسنت:
🔹
توافق میان آمریکا و ایران به «آنچه رئیس جمهور ترامپ می‌خواهد انجام دهد» بستگی دارد.
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 47.3K · <a href="https://t.me/akhbarefori/654547" target="_blank">📅 22:54 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654546">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d9af1d091b.mp4?token=H89Y4CY2fmxz5q0dgr1ICx-48mdlU4gB0d_l5WZHafcr8jlYeO7sY2aXtL3MLO2FYxvL7qF7tALq49o-BTq7tC_e_wvvR1Cb_oZ5XIsO_IDGP8TPXTYxnPzLdWzsi5wtJ3e8Fmnyru6F2ZjPb7LcdFLvI7iSkls9KB2Rz31qtujiICVJFXfokPmRHB013WzBZ5x0o1TYk54OMxBYoCM3oNlQVeUx2B8TrH50L6kWtS_aR_U1qJPXGQ6oMhBHkhvFG5xRorN9OJEZZBq7pLw8E7MMDECJjNO4BBCsR3I8e4lSMzaPw86N8FIeWCNkz7DJ2JXsIZ-GrFLMy1lQcMRpSg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d9af1d091b.mp4?token=H89Y4CY2fmxz5q0dgr1ICx-48mdlU4gB0d_l5WZHafcr8jlYeO7sY2aXtL3MLO2FYxvL7qF7tALq49o-BTq7tC_e_wvvR1Cb_oZ5XIsO_IDGP8TPXTYxnPzLdWzsi5wtJ3e8Fmnyru6F2ZjPb7LcdFLvI7iSkls9KB2Rz31qtujiICVJFXfokPmRHB013WzBZ5x0o1TYk54OMxBYoCM3oNlQVeUx2B8TrH50L6kWtS_aR_U1qJPXGQ6oMhBHkhvFG5xRorN9OJEZZBq7pLw8E7MMDECJjNO4BBCsR3I8e4lSMzaPw86N8FIeWCNkz7DJ2JXsIZ-GrFLMy1lQcMRpSg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
وزیر ترامپ مدعی شد ایران برای اولین بار حاضر به گفت‌وگو شده است
!
🔹
اسکات بسنت، وزیر خزانه‌داری آمریکا، در شرایطی که ارتش کشورش در تحقق اهداف جنگی‌اش در ایران ناکام مانده روز پنجشنبه مدعی شد که ایران در دوره دونالد ترامپ برای نخستین بار حاضر به گفت‌وگو بر سر برنامه هسته‌ای خودش شده است.
🔹
ترامپ کاری انجام داده که هیچ دولت دیگری قادر به انجام آن نبوده است. ما ایرانی‌ها را به گفت‌وگو بر سر برنامه هسته‌ایشان و دادن تعهد برای نداشتن [سلاح اتمی] واداشته‌ایم.»
🔹
بسنت مدعی شد این اتفاق هیچ‌گاه تا کنون رخ نداده است.
🔹
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 48.3K · <a href="https://t.me/akhbarefori/654546" target="_blank">📅 22:43 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654545">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">♦️
برخلاف ادعای منابع غربی، متن تفاهم‌نامه احتمالی تا این لحظه نهایی و قطعی نشده است ‌ یک منبع نزدیک به تیم مذاکره‌کننده:
🔹
بر خلاف ادعای برخی منابع غربی مبنی بر اینکه متن اصطلاحاً «یادداشت تفاهم» میان ایران و آمریکا نهایی شده و فقط منتظر اعلام دو طرف است،…</div>
<div class="tg-footer">👁️ 42.8K · <a href="https://t.me/akhbarefori/654545" target="_blank">📅 22:36 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654544">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">♦️
یک سایت نظامی صهیونیست‌ها هدف حمله پهپادی حزب الله قرار گرفت
🔹
تجمع نظامیان صهیونیستی در مرکز تازه تاسیس در شهرک «العدیسه» در جنوب لبنان هدف حمله پهپاد تهاجمی حزب الله قرار گرفت
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 42.7K · <a href="https://t.me/akhbarefori/654544" target="_blank">📅 22:36 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654543">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bad37beb71.mp4?token=HMDEC8-2kLBegJRlFqZWGON4muSPcku8qJdjRGqnRrvcBLmbJZeIRT0SFBhEFZgN0yAZC4AGOrokVl5VrEiqDum3eD9FzJEnpbxog48toI-tlgsC3ex1E5E-mutnAkELQejKEV1SXMiTcaW4vKpSVPKzmCzQRY8QyMndnD68d0UppPJf0D-eUuygeyJE8jdRx8FAT9QkJ_0dTaqdMKLwHmNu2x-mg194XUT09lNasnsh2F8vFJMc4MaUHzbqI-jUTCLVQ_13JguHLx2RuCeEL2sAk3b7a6803NzmxBC3rjAe3_w7813eYtBoUaoSAx2JHfoIax3bsdJAN29e4QvlUQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bad37beb71.mp4?token=HMDEC8-2kLBegJRlFqZWGON4muSPcku8qJdjRGqnRrvcBLmbJZeIRT0SFBhEFZgN0yAZC4AGOrokVl5VrEiqDum3eD9FzJEnpbxog48toI-tlgsC3ex1E5E-mutnAkELQejKEV1SXMiTcaW4vKpSVPKzmCzQRY8QyMndnD68d0UppPJf0D-eUuygeyJE8jdRx8FAT9QkJ_0dTaqdMKLwHmNu2x-mg194XUT09lNasnsh2F8vFJMc4MaUHzbqI-jUTCLVQ_13JguHLx2RuCeEL2sAk3b7a6803NzmxBC3rjAe3_w7813eYtBoUaoSAx2JHfoIax3bsdJAN29e4QvlUQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
کودکی که با آرزویش در برنامه محفل همه را بهت زده کرد!
🔹
مردمی که امروز در خیابان و میدان دشمنان قسم خورده ی ایران را شکست دادند سربازان در گهواره امام خمینی بودند، با بچه های در گهواره ی شهید خامنه ای چه میکنید؟
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/akhbarefori/654543" target="_blank">📅 22:35 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654542">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HbtX39jnFer5gxv8IBoIgG_N5M2e8SJR21Sos_y_MrM7WNbc7cR4RQnwsprG6mBNoYRMvMI9jMewEA18Dz0OJ6FOqQp8qVVmuHj_B2d2vo4t7VqWgYr5gUbOG5onNMh7_jgx0zJQISdZFRaDC4JqBh20bNEDec_ocJINJObkf0D0_oEhOeNixgNcleTzgAorN5nn6Ec3Wm4yoA3ScJBKNT-5VgCW1f7uIk_9pkfleomyzTSYhvLE6_auo0ZyMn1ji1N-PSiICo7qnHtzBwURm2d4pVQ3pVHLfB5k1scR1xoZq63tcY0oeYwZj3I2qId_zDIWprEfxW5eB3qBTOaanw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بانوان ایرانی آگاه‌تر از همیشه!
🔹
آمار ۱۰۰ هزار کاربر فعال روزانه و هزاران مشاوره ماهانه در یک پلتفرم سلامت زنان یعنی «خودمراقبتی» برای زنان ایرانی به یک دغدغه جدی تبدیل شده است.
🔹
با توجه به سبک زندگی شهری و مدرن پلتفرم‌های سلامت زنان به یکی از بخش‌های اصلی زندگی روزمره زنانی تبدیل شده که می‌خواهند آگاهانه‌تر درباره سلامت جسم و روح خود تصمیم بگیرند.
🔹
همزمان با روز جهانی بهداشت قاعدگی، آمارهای ایمپو نشان می‌دهد نسل جدید زنان ایرانی بیش از گذشته به سلامت زنانه، آموزش و پیگیری مستمر وضعیت بدن خود اهمیت می‌دهند؛ تغییری که می‌تواند آغاز یک فرهنگ تازه در حوزه خودمراقبتی باشد.
مشروح خبر در
👇
khabarfoori.com/fa/tiny/news-3218552
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 41.4K · <a href="https://t.me/akhbarefori/654542" target="_blank">📅 22:30 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654541">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">♦️
خبرنگار: آیا کاهش تحریم‌ها از ایران روی میز است؟   وزیر خزانه‌داری آمریکا:
🔹
هیچ چیزی روی میز نخواهد بود مگر اینکه تنگه هرمز باز شود و ایرانی‌ها توافق کنند که باید اورانیوم با غنای بالا را تحویل دهند و نمی‌توانند برنامه هسته‌ای داشته باشند.
🔹
سفیر عمان به…</div>
<div class="tg-footer">👁️ 39.6K · <a href="https://t.me/akhbarefori/654541" target="_blank">📅 22:20 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654540">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/047748234e.mp4?token=MnHB3eRDKqVsUug1rWCRXD-cpxGDDWSvHo5ubNlfSZCYgqtatGF2FiGC-C_GKuf2xw4bqGIHtm3lTxHNCs2jkGrlZb8NsZYWYyBp9XJiWjysEDm-rNorO2oU0nCQ10tfccsjFjtMNy-8M8GiyJmlLfD9L9TAwWsAIp5mhb53FjCRe9anVdK7YobUlIMKELkqz3X_f6_DTMqNuq2Xb1M0AcC8OHMr8bGiTxAUFagJwVIAAWYH-gIeMOzmWGK77KSk7HtwhLlISmxK3GirvhixvBIRntFzD56IKPCD-99NoasCLaUjkU3p3tY5rftJT-U0HGMPI8IQasgoNYyp0sBAPw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/047748234e.mp4?token=MnHB3eRDKqVsUug1rWCRXD-cpxGDDWSvHo5ubNlfSZCYgqtatGF2FiGC-C_GKuf2xw4bqGIHtm3lTxHNCs2jkGrlZb8NsZYWYyBp9XJiWjysEDm-rNorO2oU0nCQ10tfccsjFjtMNy-8M8GiyJmlLfD9L9TAwWsAIp5mhb53FjCRe9anVdK7YobUlIMKELkqz3X_f6_DTMqNuq2Xb1M0AcC8OHMr8bGiTxAUFagJwVIAAWYH-gIeMOzmWGK77KSk7HtwhLlISmxK3GirvhixvBIRntFzD56IKPCD-99NoasCLaUjkU3p3tY5rftJT-U0HGMPI8IQasgoNYyp0sBAPw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خبرنگار: آیا کاهش تحریم‌ها از ایران روی میز است؟
وزیر خزانه‌داری آمریکا:
🔹
هیچ چیزی روی میز نخواهد بود مگر اینکه تنگه هرمز باز شود و ایرانی‌ها توافق کنند که باید اورانیوم با غنای بالا را تحویل دهند و نمی‌توانند برنامه هسته‌ای داشته باشند.
🔹
سفیر عمان به من اطمینان داده که هیچ برنامه‌ای برای عوارض‌گیری از تنگه وجود ندارد.
📲
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/akhbarefori/654540" target="_blank">📅 22:16 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654539">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a4aeb2fe51.mp4?token=bocJP1ABP5WLjkoQNJEqoS-xFJTKVyJ8aFRRIR44XZkpkMbHg2UWg-kj85QaLhLhMlkWAI8mpt1xXkDtttpIwoaiaG-u_jhyz5UVtt7QJX8IhXonKjRoo7cHUsi6M5S4Uwu_Q19tBzrW3-_x5dRappM31-B8YwIrBT2Icd8ECkdUjQxYa05qNzrzqc6W0cq38g-fFnmww0fbLN6O8tNUchkk6EN_Jvt6m4kLRSGHl-fNMMYDODKLEIDwyETxWPM02Ofr-II6dNRzRH6XRJcufC6MtYV3P49-0gXUbIIgawmbfYNjuymFVDMBgzljkZFwlEGx1tretc_4Bopy7Zy70Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a4aeb2fe51.mp4?token=bocJP1ABP5WLjkoQNJEqoS-xFJTKVyJ8aFRRIR44XZkpkMbHg2UWg-kj85QaLhLhMlkWAI8mpt1xXkDtttpIwoaiaG-u_jhyz5UVtt7QJX8IhXonKjRoo7cHUsi6M5S4Uwu_Q19tBzrW3-_x5dRappM31-B8YwIrBT2Icd8ECkdUjQxYa05qNzrzqc6W0cq38g-fFnmww0fbLN6O8tNUchkk6EN_Jvt6m4kLRSGHl-fNMMYDODKLEIDwyETxWPM02Ofr-II6dNRzRH6XRJcufC6MtYV3P49-0gXUbIIgawmbfYNjuymFVDMBgzljkZFwlEGx1tretc_4Bopy7Zy70Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
رئیس کمیسیون امنیت ملی مجلس: تبادل پیام با آمریکا در جریان است
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 39K · <a href="https://t.me/akhbarefori/654539" target="_blank">📅 22:10 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654538">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">♦️
ادعای خبرگزاری CNN: ترامپ قبل از امضای تفاهم‌نامه با بنیامین نتانیاهو مشورت خواهد کرد
📲
🇮🇷
✊
@AkhbareFori | khabarfoori.com</div>
<div class="tg-footer">👁️ 42.2K · <a href="https://t.me/akhbarefori/654538" target="_blank">📅 21:53 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654537">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Iz-nlMD2LeSYJ21401eZF7-n6OsGJRCyZ4G8azriTx2XuiqSc6AHenAInEeKofZuBK25ZpG2hLTntH3ybFkdqhgDVjzSbWd2jf2Okfnb7w6s7BlVYBbPrMoByjIabUREonOdguBTNCowenEutUp5OA9ftAtDKtykoAlzUD1fTjmxo5e5T-jCpdMI23ndJaQfQcWLkN5KgXeLBlwZRAFk-coRmGbU0xq9i-q4mvmhvMBsJTTOFLvs3Gj0bdmXujlQqA_np5FWWdSGmBA9MRaYicqiNtLpC0l_B2BS5IKF6JJhX_zzAnD9YtbI0inHSHZqoIKtfXcevrXQUec0MtmLWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
این سند خبر از جنگ سوم ایران و آمریکا می‌دهد/ پاشنه آشیل توافق یک صفحه‌ای چیست؟
🔹
پس از توافق محدود و موقت، مذاکراتی طولانی، پیچیده و احتمالاً کم‌نتیجه میان دو طرف آغاز خواهد شد و این بدین معنی است که جنگ سرد میان ایران و آمریکا دوباره ادامه پیدا خواهد کرد و هر دو طرف منتظر دور بعدی درگیری در آینده خواهند ماند.
گزارش تحلیلی خبرفوری را بخوانید و نظر بدهید
👇
khabarfoori.com/fa/tiny/news-3218518</div>
<div class="tg-footer">👁️ 40.3K · <a href="https://t.me/akhbarefori/654537" target="_blank">📅 21:47 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654536">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PscdwQxiNWuK78Z2ZJiYwX_F6Okqe5pN36yt0Tz11FLU5XmrVwX7nOn4EZgTvj_wnAjs4wkUnzY9OlBTD6cfwsn37Tu4tYLXNK2-f2dE4wujrPKd5kIdev1NLiFq4URfSGQQxvl6ippEyLVuarfy0kIRwDdjCRUweyT2eflT96lXAiNdNscO2BdxCYj8sokLGazsjbWHf_jFkFhxCjtwWHOP3cuEtSbp3XTdS-wm9Ru4XS7bFlESc3KK-HjUYRa63wCLHjyqNeyQvl9GwwdvRvhtARmRAT0G6JX2B4jgjMfwPeJ3kfUkhDVmZ1CD6UbZkZxfMcEyNByfxivo2XUExA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
الحدث: هگست نخست‌وزیر قطر را تهدید به ترور کرد
🔹
الحدث مدعی شده وزیر جنگ آمریکا در تماس مستقیم با نخست‌وزیر قطر، در گفت‌وگویی درباره حماس و ایران، با لحنی تند او را تهدید کرده است. طبق این ادعا، پس از بالا گرفتن تنش در مکالمه، دوحه نارضایتی و شکایت خود را از طریق استیو ویتکاف به ترامپ منتقل کرده است.
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 37.3K · <a href="https://t.me/akhbarefori/654536" target="_blank">📅 21:45 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654535">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">♦️
ادعای ان‌بی‌سی: ایران و آمریکا سه روز پیش در دوحه به توافق رسیدند، اما در اعلام نهایی آن تأخیر می‌کنند
📲
🇮🇷
✊
@AkhbareFori | khabarfoori.com</div>
<div class="tg-footer">👁️ 36.3K · <a href="https://t.me/akhbarefori/654535" target="_blank">📅 21:38 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654525">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromاقدامات هیئت قرار</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/stRWTWmQb_t5gZdTk_Yd0Wz3BfJVSxic2ViOLNgnCp6BW7Y9q-sDxfHMWot5pJrPa1qCrFmTHRqasnRW4bEbNOT9988pTwUeZYMkj7Il9oNFoVnIkVl4nWBGwViRPbACRNuHH4fKK6ftCJAZNIayvG3YRNf5NNG024nuvSoxt7N1OTYxcTYBoh8ixybWDSDbackEONXhT9rltCr_ANUFBWxvulkJ4OUDNoFWwFOPi4-o4I0mS2LPl2ELdtnXnylfTVv9UklcOEHDU3GfyDJ67OEP2ZWlIK55B5yVYWbr0au2n-Gj5KFPkS5qgTKWQQzQonjnekoV7jLt73-j0eYhrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bSd_gV07-5DQ3yG8-JOgiCQvoRGhZSHPHal2dy7ATFfejt49mL8j0yQbweVbjhaZd-b5DlI7OSDcFW6mZAY9Ojn4IwZy1PlHrqP85bwIOdshG6elpUugR4VcZCsHDIfTbNRjbxN6nG6jmTIK5HQ9btnUDiNUVskYa_19hqOue5XWow229X0kCOkmppBbBrs9DhEYl5DLa1q7j8MUiTzH2VIUcCFqNA6nFQUhLK9f6eeJmNx0CE-Ka3dnA7g4Q3nkw030KizlMnkqx3czFElAGeYjDoDyl3inowgmUNWB2EuzVQlTTCDm42M-lV6zr5-Dn3Tfjq1zuHlWGnIzvL7HYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Szbn3sGo0yLvqbJ232XcMhS8vTPa_J1a-mepV2TcTvZdS6VtKpinlymx2pj7Z5fizs5i49PrS2_IdzvDU5Uqv8Yn4BdVfGj5C4ZZFlnI3Smp3tUV5tcN7a5UbJT_MsQ6awQXpVnviHQ9w66S4NNPXdhepNFcyDy2pL8aNGl-JewTm1yUo6fOqiAxBo_S0LQbh4b_KF2epCCyWc3qC67GWLWpr_JAWcCok78nU6okPv_Y75cJxmXyVp5XN3Sq2ZzzPX66Ql2qFunDB2LyVyWSpH1NsWkIml3TFx-8q2ftSODS3_rhP8zJaYXPPQSeMFq0OOUIhFeLv2gquTwxK4USCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qHCAwz06T_T7dLbVaAnOTD_boSGJiNHUj9xEHvJq9OISj3I3qtTZvgyVzrdKonol43gPqoPJGb8-stUcsDFFIr19vKi5VLckEaT-BpV9qEEzjyqfIvlvs49hbPUasT4vRfEhoCUyF-LYcx22gJIj-kn0grNIzocQnK9byjCZadH_fvvq0RTPeV-n--BbNGFlxULaqn4gDt0z1bCdhyyfx9-WEFVU18JsQ7MNsDxCxkafhNJ3WoYxPRo9bQwEB8EkaWNtv4k3Gis7740Q83JGrQyyqygQJOW3hD7OU1wYhKqvmAoVX341fuwUk8ARHtUJqPAh0Hqcdbj3GdvPNaU4hQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UlYpFYkI2Uc33ltS_RRSoCVMciQJGSslUAqbVwOBrs_wZqM2C4BLf9LolcukTCSoJ9W3dnMmOMphtMWZzjeb70PpgByiZOw6t40JC5FU-QnjkUnVQWrsxfQtQtfIyERM6svajnYyy6mlAVb1R2qps_W7G6RWmqKVpbuOWw-WPUul78S7UgKIKLGdMXTI5tnQQB6toGTFx9dKOgaM4IofqL8Pza_jRGb4Q2Tak7d4MVg_-i44b9vPcbfxvLe_Qq3vvsL4EDst1ptyJljDTc-juEu4P0FXDkFCWYWeL5MkBU_MBekX4jJAweA9de_Jbv7WFbHdUTFEnzyDf9j9kUVMWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OPymfWoGUs5pIzwF8ezytRd3EENY0L9mxH5zfblQcoc-6u-vomee3Qfuu2GNpddOGReESDfYbmvC7Jomx--XEMKE6aGpjJw3o7ZfQ5oX_bSyirCAFH1u6l00ur4LMHiMkoZ00XS8mbnN1uiwEMoNOFt0pHsvAufrbnnxzB4OAjABTWO1XysLQxXrLhMWKkxwU0kbXElmS3mPaesAByqWOjBWA2_2Ix84x31oHx2IKGjRnAl3AwH7ReG2VcmoQ9LIVtZ_3z2arpjT56r-9227jmGl3URHQguL1tg_rncn5i7de58faW8zYmmoKEiY1uzrHLR2n3Ov_ODHdVq8SidAHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/j280-lb9VLiPcVKL5wkwS3HtYCJJDnZhNz4Ve3FgIEkgOIfQWN86R9rAExoELAWI-JxT5SIRVz3oP8gxFLDKOfbrUjnXZdjjqZue4E0eqFX7wwA_mm7wC52XR9EQNguFwmLNsxr9q1BGMWqrUtJkrhgeMCM_hUvjXNFQlmAyofCCjOF_53XE3_lC4qGvfwukIGAbrBYUmtp3B7u6QoXRpBQiq3mcsTsQ2Uzhoh0Y8JzqdaQJnudsMIaAsBQ8zMp1CAOu3J0qP0do3lDK16-Ms_UnQyAtjT2tIKTz_moEFCSOF7QfeSHOMkGgz3LNkyU-9jrVNlpnw4NK6tKNG4P1lg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oGReYhTswG-xRcyyddPZI_JHsV2R-C2jGoWueFoJsbzgu1QCJrlg0-OO3fifT6LN4LUs1k5u83ePvxt2GGs85ZtY1DZa_2ei0hb9np-ZYdmBVv6ORU49x7BpRF7gsa-9cWQ08JPq3NFwMUQgQTK93cC9Juxx_xckd2jB9Vc6rwmYq3ttyMnPBnXecUY1XwX1KO-FvOljq-k40PN9IrXjoh3s2lSGt2dGyChRtNFT7V1LuOBpaXcyuDdkZvK1IINVmq2f682zrfHxOZoAkiFgqojxtZOOXakxNIP_S4xKWlout6RyaKTSdFpqZZswohG9JUvFniwM7IFg_zfhRC8qkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rd6fqg13eQMsdD5TBA6N5eSeB0aVI---h7Qmh2473-Gg8SWJ5mlLXmijniDMT9sBV9Xh6oeepYDiM1ugVA_W04-jg5s1rInu3tNMkZN6bHCQBzvv24LFr_3VwQDAkPgqaHZKFWy6mGM13bRy6rwp-OZcH2S4v16Lo30iBHLw8_vumUrtmkQ0cOS-05QS1Yaqo_rpBPC3ZI3cBHxOD4ZTCso5yPXy7F70m8w6bucVb-8Vu279j3b7o7bOULfapiX6dbONEKuMdGjecjkrwai2xVvQYoa4AHz-fiKXggQxufT39JQYApiiAe70iRzXEnQDLEYOVE3soBJ6sHnv9GbtCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vkf23kKvWd_ElY4RMfd2QqUptT6rTaGow5518DkHf6f9BKJdXMg4tg2lSVzklRWlt6Iaaa0PN44qw-4TBlBgyT5r-T8JW0gQjW3ixEYCoOQwGwNF3ul8YVByl2l14ncf9qKwTMJzAX_xkGc-RrOaziWjFsXU6r_4YBw3HBA8WGf-ylpfxB-1592JaV420sgBxlqgK40LZU9suGAJ3NJDKmOoGDEqITmZAWzWEU7ovMKdLcZ6xY6dAMNaCASMstkClvFoZYjsOZDptEdYf5j3BOWTWlb8xHZ67FiBnnKHhZz_wO6XeGbmWdwNPlazEzPVhl_LOl7hIdhL44lMx3Cxag.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">💫
روایت
#همدلی
امروز
💫
امروز هم سهمی از مهربانی در این مسیر جاری شد…
#هیات_قرار
با مشارکت شما مردم نیکوکار، ۳ رأس گوسفند را قربانی و گوشت آن را در راستای حمایت از خانواده‌های ایرانی میان خانواده‌های حائز صلاحیت توزیع می‌کند.
💳
گزارش اقدامات هیئت قرار را در کانال زیر ببینید
👇
@Heyate_gharar
شما نیز میتوانید در این کار خیر سهیم باشید
👇
5029087002135690</div>
<div class="tg-footer">👁️ 39.1K · <a href="https://t.me/akhbarefori/654525" target="_blank">📅 21:37 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654524">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">♦️
یک منبع دیپلماتیک به العربیه: توافق بین واشنگتن و تهران در دو مرحله انجام خواهد شد/ انتخاب
🇮🇷
✊
@AkhbareFori | khabarfoori.com</div>
<div class="tg-footer">👁️ 37.2K · <a href="https://t.me/akhbarefori/654524" target="_blank">📅 21:25 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654522">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VgQte6K4YYEJ_Cecca27tabVFU8LIpkTSTwfm9aJE2Ig8b7Yi2I3UZovHTl3A86fkp_ZwN4F2kfngDfMa899qWEEdzQTT0OAaHlHi90ZNbx1v4lio0U74bdT6B3O16IKmszfxaXevWcxQ0aoWPSZQy7SFhEIX7WFGGiboQfDCm3oIIaRq-EUnTLL7jemNQFi94k-H9NleBzFefwmIFyqveYOGXyLzFHNSkIdhHWjVIaafLD3gvOFfckYPSEe1FtMBrDVSdDqZ9xPopcDkKnBTG3ZGCzPtIvvRIZ5w2TRHZXNgSgBsMoCpSiMFznMGfCoDqMWvSkPDVephh-VfhQrzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8bccfbe369.mp4?token=Zl24OdHV9Tic4oTQTtTvmpq7WmAhmal9dHOlTm4-FI4Tloa9WsIm6ynBL9D8NrxlxtZ176KzQxhy3XftppqFps_5DFzfrenAATCXx2n_LSND8NTSqmaLVTkSPqqFqp2Y2kJ-aBZhR-A_4y1tsjRpW3kYiPEwTvlcp-aK4izN71Jb4Vt_0sxbZEQwhMAwzwqZu5jqtbaQ0mLDUNiRXdOqETTcSbWVgDeTEx8PeLwwWrMturBAXeXlsnralA4PlnOrzi-1Cp6lgGffBpr-3WawiBMSETOGgUZfr-hD-fC6_vziwI4P00nlGF7NsiUiwS34ZcVlCjiqHrLwAZTnOdyMqw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8bccfbe369.mp4?token=Zl24OdHV9Tic4oTQTtTvmpq7WmAhmal9dHOlTm4-FI4Tloa9WsIm6ynBL9D8NrxlxtZ176KzQxhy3XftppqFps_5DFzfrenAATCXx2n_LSND8NTSqmaLVTkSPqqFqp2Y2kJ-aBZhR-A_4y1tsjRpW3kYiPEwTvlcp-aK4izN71Jb4Vt_0sxbZEQwhMAwzwqZu5jqtbaQ0mLDUNiRXdOqETTcSbWVgDeTEx8PeLwwWrMturBAXeXlsnralA4PlnOrzi-1Cp6lgGffBpr-3WawiBMSETOGgUZfr-hD-fC6_vziwI4P00nlGF7NsiUiwS34ZcVlCjiqHrLwAZTnOdyMqw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
واکنش سفارت ایران در غنا به عکس روبیو و همسرش در تاج محل هند: بعضی مهمان‌ها آنقدر ناخوشایندند که خانه خودش بلند می‌شود و می‌رود. به‌خصوص وقتی آن خانه از روی عشق ساخته شده باشد؛ برای یک ایرانی
📲
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 38.5K · <a href="https://t.me/akhbarefori/654522" target="_blank">📅 21:17 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654521">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gnuHQJnFUSa7xciixbB1lpmayLnwCc9k71beVqJuuDx5kTqQYEUhBAmaQPTXrZuWWhW_u36kFSLgiExvGJdZu5lqjBrXS14GTItVWS4ERrEhIImGlJVa5nyz4zC-dMThzvypJqS4BK25odiUXIeZUyUVqM1yuBT-BTXCbAipcooB38zpky8zzQBj-Fytu2RpRKarDtv10bew9CEF2Wf7PB3QxQy9gFkoUOjEBijSlHgqdiA5bYAudeOU8G0G3nh6KzreVFTCTuVm2mq8C32zrcDztTCP8f-BlfilWPElEXs0nNYozeARIUhsS6DtPDZUMBgGTfof3Jtg-ch81rUhMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
شبکه CNN: ایران به سرعت در حال بیرون کشیدن زرادخانه موشکی عظیم خود از زیرِ زمین است
🔹
روندی که ادعای ترامپ درباره نابودی این توان را زیر سؤال می‌برد. به‌گفته این شبکه، ایران با بلدوزر و کامیون‌های کمپرسی در حال بازگشایی ورودی تأسیسات زیرزمینی و خنثی‌سازی راهبرد پرهزینه آمریکا و اسرائیل است.
📲
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 39.1K · <a href="https://t.me/akhbarefori/654521" target="_blank">📅 21:16 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654520">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">♦️
ادعای یک منبع دیپلماتیک به «الحدث»: پاکستان به عنوان «شاهد» در مراسم امضای توافق آمریکا و ایران حضور خواهد داشت
🇮🇷
✊
@AkhbareFori | khabarfoori.com</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/akhbarefori/654520" target="_blank">📅 21:11 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654519">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nQkOs4BqXjkrtqxCpldAYh3lRan2idhtXsCw_5rOlZJ2F0_RS0xvLyvwSsxK7K1sVZ9iGP30IajJ4yVxHPA9EyFDsO8Mp4aJcxIo8EWxNcTj_CejZ9OTzzOMKRXiF3-znNfvNByaQ6VxIIjgk_W1bNGWCGrxrpTO-oVIORkkUvK6BcyPKmq5ri-BRZJz6d9EOs7-_eAsOQ7Ygr04JLsSttTEhQ8V2dGwkbUs82xg7uSjhq1EPazahPvbftGWPAsjxE8rpLX63NJ8DzshpZ9NBgD5gHkrWt5kWKY5IHxOieAE3yHZINYsn-JT-unDxDCWgMImrmydE8pObEnn8NRjEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
آمریکا عمان را به اعمال تحریم تهدید کرد  وزیر خزانه‌داری آمریکا:
🔹
دولت ایالات متحده هرگونه تلاش برای اعمال سیستم عوارض در تنگه هرمز را تحمل نخواهد کرد؛ به‌ویژه عمان باید بداند که وزارت خزانه‌داری آمریکا به‌ طور تهاجمی هر بازیگری را که در تسهیل عوارض برای…</div>
<div class="tg-footer">👁️ 37.6K · <a href="https://t.me/akhbarefori/654519" target="_blank">📅 21:08 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654517">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/emnLN1_R7hl_lb1rRDCbBSMTSRE4athNFBOm8pVr-q2hVSVLcVD3eibS0nhwTH5kZelGoi3fg9d3WW7N-bGaESah7jDTYLRpFsqvi1tueIn1h1-pOo2DXfnTCcZxnqzJ08_d2wbMxwZMfFj3UdlpjohxXEV6PFmcLlPWp23pM-OYKCUrK20rVBPs-7XBmUYZjMn-dCQyUsLGTijnTMNCqjx4LKRq2_S9W-8eJfqbEyeHvoCJlO9kSFPcMDfE5fwRMhXdgmHuGVM4Uhe8lI3UVEu_Yo6q8lA4cCWqCe_D-Rc8weIYvFXmJbI-PDeUocTU3WsWUs-04HBszJNsS5XDmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
مجله آتلانتیک: چرا ترامپ باخت؟
🔹
ترامپ که با وعده «تسلیم بی‌قید و شرط» ایران هیاهو به پا کرده بود، حالا اسیر همان جنگی است که نه بر اساس استراتژی، بلکه با انگیزه‌های شخصی آغاز کرد. او که پیشینیان خود را به بی‌کفایتی متهم می‌کرد، امروز در وضعیتی است که ناچار به مذاکره برای توافقی شده؛ توافقی که کفه ترازوی آن بیش از آمریکا، به نفع ایران سنگینی می‌کند.
📲
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 38.6K · <a href="https://t.me/akhbarefori/654517" target="_blank">📅 20:55 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654516">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/445ef439c4.mp4?token=FFcYR9A06yvEVgZOYVeudG0_XW4OI_OOzGmaSKxNWhFxCkUKCD7a0d48AzFSqDqzzX_8vXy_wy4ZpTqUPGRC1KpwxB71LrETHz6QM7oJMwQnMnGi_t3UzzsQAFaCUrEwV59gOWnURTLGrQLsZ9rUktGScFqkbqyzMLpZNOuypkhaCUThULF6XQn6xVe4xF4xEfP4xqQBjfEkscvyvbwy1Q9JcIHds-JzxmdWdbNGqIhB8xOivMpeISBs9ryop95nent5JuLOoeF4O45LsUYK4354FOEvFtSpynRz7-hk37xKs0wO-TuYfJDUrjP_4KJl03bf_xvfptNm51sn0iCKrA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/445ef439c4.mp4?token=FFcYR9A06yvEVgZOYVeudG0_XW4OI_OOzGmaSKxNWhFxCkUKCD7a0d48AzFSqDqzzX_8vXy_wy4ZpTqUPGRC1KpwxB71LrETHz6QM7oJMwQnMnGi_t3UzzsQAFaCUrEwV59gOWnURTLGrQLsZ9rUktGScFqkbqyzMLpZNOuypkhaCUThULF6XQn6xVe4xF4xEfP4xqQBjfEkscvyvbwy1Q9JcIHds-JzxmdWdbNGqIhB8xOivMpeISBs9ryop95nent5JuLOoeF4O45LsUYK4354FOEvFtSpynRz7-hk37xKs0wO-TuYfJDUrjP_4KJl03bf_xvfptNm51sn0iCKrA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حسین پاک، خبرنگار ایرانی حاضر در لبنان: دولت لبنان و اسرائیل همین الان در حال مذاکره هستند تا ارتش لبنان به زور حزب‌الله را خلع سلاح کند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 37.1K · <a href="https://t.me/akhbarefori/654516" target="_blank">📅 20:50 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654515">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">♦️
اتحادیه اروپا خواستار مذاکرات با ایران بر سر مسائل منطقه‌ای شد
🔹
کایا کالاس، مسئول سیاست خارجی اتحادیه اروپا امروز پنجشنبه گفت هر گونه توافق میان ایران و آمریکا بایستی با «گفت‌وگوهای عمیق‌تر» بر سر امنیت منطقه همراه شود.
📲
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 39.6K · <a href="https://t.me/akhbarefori/654515" target="_blank">📅 20:39 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654514">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">♦️
پزشکیان: به دنبال سلاح هسته‌ای نیستیم، ناآرامی منطقه به خاطر اسرائیل است
🔹
با ذلت، دیپلماسی نمی‌کنیم، اینکه مردم بیش از ۸۰ روز همچنان در صحنه هستند دنیا را متعجب کرده، درحالیکه فکر می‌کردند با دو بمب و موشک امکان دارد یک عده وطن فروش مملکت را با آشوب روبرو کنند‌.
🔹
اگر ما درمقابل قوی‌ترین قدرت دنیا ایستادیم باید سختی‌ها را بپذیریم، نمی‌شود بجنگیم و انتظار داشته باشیم روند طبق روال عادی قبل باشد.
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 40.2K · <a href="https://t.me/akhbarefori/654514" target="_blank">📅 20:24 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654513">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">♦️
ادعای یک منبع دیپلماتیک به «الحدث»: پاکستان به عنوان «شاهد» در مراسم امضای توافق آمریکا و ایران حضور خواهد داشت
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 39.5K · <a href="https://t.me/akhbarefori/654513" target="_blank">📅 20:15 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654512">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">♦️
حسین پاک، خبرنگار ایرانی حاضر در لبنان: جبهه مقاومت باید با فشار نظامی، اسرائیل را مجبور کند که از لبنان عقب‌نشینی کند/ اسرائیل بدون اقدام نظامی دست از تجاوزگری برنمی‌دارد
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 39.5K · <a href="https://t.me/akhbarefori/654512" target="_blank">📅 20:15 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654511">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">♦️
ادعای منابع آمریکایی: یادداشت تفاهم با ایران در انتظار تأیید رئیس جمهور ترامپ است
ادعای منابع آمریکایی در گفت‌وگو با الجزیره:
🔹
ما تأیید می‌کنیم که ایالات متحده و ایران در مورد تنگه هرمز و مذاکرات هسته‌ای به تفاهم‌نامه‌ای دست یافته‌اند.
📲
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 40.5K · <a href="https://t.me/akhbarefori/654511" target="_blank">📅 20:01 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654509">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">♦️
رادیو ارتش رژیم صهیونیستی به نقل از یک منبع نظامی عالی‌رتبه: بعید نمی‌دانیم که لبنان بخشی از توافق آینده آمریکا با ایران باشد
📲
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 39.2K · <a href="https://t.me/akhbarefori/654509" target="_blank">📅 19:50 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654508">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">♦️
معاون وزیر ارتباطات: بهبود کیفیت سرویس‌ها و بازگشت ترافیک بین‌الملل چند روز زمان‌ می‌برد
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 39.4K · <a href="https://t.me/akhbarefori/654508" target="_blank">📅 19:49 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654507">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">♦️
عزیزی، رئیس کمیسیون امنیت ملی مجلس: تنها مشکل سردرگمی آمریکا است
🔹
ایران پیشنهاد‌های خودش را در قالب متن ۱۴ بندی ارسال کرده
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 39.4K · <a href="https://t.me/akhbarefori/654507" target="_blank">📅 19:47 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654505">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">♦️
حسین پاک، خبرنگار ایرانی حاضر در لبنان: دشمن در جنوب لبنان بزرگ‌ترین ریسک تاریخ خودش انجام داده است/ ۶ لشکر بزرگ دشمن از ۵ محور به شهر نبطیه حمله کرده‌اند
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 39.6K · <a href="https://t.me/akhbarefori/654505" target="_blank">📅 19:42 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654504">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9c81dd164f.mp4?token=Ev6wi-rfvMmUbo7DxtNrs3G_ZZGdUO9Xkj0XJX_aRwksLRLHu4D0tpX2zFslq92mkH2CoOUM5EM88e2Pw95-lgkIgy7MJ1Eh3PREQLXb8p0QIhhmIOEnxKf2zFfMRDpWgeQ4WOZ1SyQAdFCexn1IJIVOXmPaniGLBFnokPCZVQiVKIG3LiHBxd2UIkFclPurLbYf87jvPT1vuLXE6E7q4f0Uar9gbybGZw4RnM8CPIvhtpdkeGR0RfbznPAg01RBzBgDvdUknVHI3YwI8OmIAu7g5o90kIIwxBkocVs9CnaU7Mv93ZZVrvjYA9XRzMVRyP56kFD-XphAIwDtN3FvuQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9c81dd164f.mp4?token=Ev6wi-rfvMmUbo7DxtNrs3G_ZZGdUO9Xkj0XJX_aRwksLRLHu4D0tpX2zFslq92mkH2CoOUM5EM88e2Pw95-lgkIgy7MJ1Eh3PREQLXb8p0QIhhmIOEnxKf2zFfMRDpWgeQ4WOZ1SyQAdFCexn1IJIVOXmPaniGLBFnokPCZVQiVKIG3LiHBxd2UIkFclPurLbYf87jvPT1vuLXE6E7q4f0Uar9gbybGZw4RnM8CPIvhtpdkeGR0RfbznPAg01RBzBgDvdUknVHI3YwI8OmIAu7g5o90kIIwxBkocVs9CnaU7Mv93ZZVrvjYA9XRzMVRyP56kFD-XphAIwDtN3FvuQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
غریب‌آبادی، معاون وزیر خارجه: به هرگونه نقض آتش‌بس، پاسخ قاطعانه می‌دهیم
🔹
تا زمانی که تفاهمی در راستای منافع ملی نباشد، ایران آن را امضا نخواهد کرد.
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/akhbarefori/654504" target="_blank">📅 19:40 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654502">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">♦️
نماینده ایران در سازمان ملل: اقدامات ایران در تنگه هرمز، قانونی و منطبق با حقوق بین‌الملل است
🔹
هیچ کشوری نباید تصور کند که در آینده از سیاست‌های مداخله‌جویانه آمریکا مصون خواهد ماند
🔹
برخی ریشه‌های اصلی وضعیت فعلی را نادیده گرفته‌اند و به دنبال انداختن تقصیر به گردن ایران هستند
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 36.6K · <a href="https://t.me/akhbarefori/654502" target="_blank">📅 19:32 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654501">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/424fdf2b4e.mp4?token=pNbsQ4heAPk4V6CPqnqVisVZl8npQEtSFDs49gPTVv3QT2UBOzpaf2fCjE1RZQzhMTC6jqyFJwohFw0Z2BjUu2h0ObJaXxNSfqiTylGwBRCmYLIHdh1Yb52bTarnvibjqd9vy7aC1sLZw87opJ7QMixIEzI7pegXptWv6H4PBvqWGxQE7KxLTVT4dRN8sGJ9p7XnhoZAKHaBnQhS5AzvD5gMNtmdRrbrK70aa74cZq4a9F_hvn5-wW9vKko5OcUl5G5cU3V3H_dbT5NUVnTWKc3NpaExuPyVrZD04DchhVRPX6LVlTG24DOPynvZvTECiJO4H3D3MQNJ_JHzgqaGyQiQ5dhZNcuAHvZu33woLx4D9A4ggYqUWwFSDGdxGD0CGVOH09aXryf9G2uAe_HPhNmAKNqEtCIDuerR39KF8R6F6zWqIqURgCvYOtX7ghVXEjtd1ZVtIX1R_Dpqa_kaopYsjSeK94jerOv8lEysJKwkiTBc5P9d2VEEn8051jy3fgLJvHxZDq8UqiRuaUxpQKrsbhRQNdzdcOr2xpZTcrU2dT03pLPcybtZurSzY9lq1Q0o_h8s5cZZP5THFGZ6AY8NJYXw-G15c9KqI9qphHqLYj_9q-ZIl_fKGm0wtgQFj_qUoFFiPxNlGBKndFuhpDpAL3D_OMHTFci3oukZZd8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/424fdf2b4e.mp4?token=pNbsQ4heAPk4V6CPqnqVisVZl8npQEtSFDs49gPTVv3QT2UBOzpaf2fCjE1RZQzhMTC6jqyFJwohFw0Z2BjUu2h0ObJaXxNSfqiTylGwBRCmYLIHdh1Yb52bTarnvibjqd9vy7aC1sLZw87opJ7QMixIEzI7pegXptWv6H4PBvqWGxQE7KxLTVT4dRN8sGJ9p7XnhoZAKHaBnQhS5AzvD5gMNtmdRrbrK70aa74cZq4a9F_hvn5-wW9vKko5OcUl5G5cU3V3H_dbT5NUVnTWKc3NpaExuPyVrZD04DchhVRPX6LVlTG24DOPynvZvTECiJO4H3D3MQNJ_JHzgqaGyQiQ5dhZNcuAHvZu33woLx4D9A4ggYqUWwFSDGdxGD0CGVOH09aXryf9G2uAe_HPhNmAKNqEtCIDuerR39KF8R6F6zWqIqURgCvYOtX7ghVXEjtd1ZVtIX1R_Dpqa_kaopYsjSeK94jerOv8lEysJKwkiTBc5P9d2VEEn8051jy3fgLJvHxZDq8UqiRuaUxpQKrsbhRQNdzdcOr2xpZTcrU2dT03pLPcybtZurSzY9lq1Q0o_h8s5cZZP5THFGZ6AY8NJYXw-G15c9KqI9qphHqLYj_9q-ZIl_fKGm0wtgQFj_qUoFFiPxNlGBKndFuhpDpAL3D_OMHTFci3oukZZd8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حسین پاک، خبرنگار ایرانی حاضر در لبنان: جنگنده‌های اسرائیلی حمله بزرگی به بیروت کردند و خط قرمز را شکستند/ یکی از رسانه‌های اصلی دشمن می‌گوید هدف حمله یک فرمانده ایرانی بوده است ولی ما اعتنایی به بیانات دشمن نداریم و منتظر بیانیه مقاومت هستیم
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 37.3K · <a href="https://t.me/akhbarefori/654501" target="_blank">📅 19:29 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654500">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">♦️
الجزیره: اتفاقات اخیر تاثیری بر مذاکرات ندارد
ادعای الجزیره به نقل از یک مقام آمریکایی:
🔹
رویدادهای اخیر در تنگه هرمز تهدیدی برای مذاکرات با ایران نیست.
🔹
مذاکرات در جهت دستیابی به توافق ادامه دارد؛ اقدامات نیروهای آمریکایی در تنگه هرمز و حومۀ آن «جنبۀ دفاعی دارد».
📲
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 35.4K · <a href="https://t.me/akhbarefori/654500" target="_blank">📅 19:28 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654498">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D0CzWVXF7nixPlxS6aO4VO5OzuzxkIrzDhaWB8H6yeO65ZTdBTXM5XZkO28_U0gvNXsF4D-5TQ2dLAbliaEYMJj9HkCCkl7PY87E_sWOsAXS5Mqd59zHzvxCsMGViu6JnhVIG3Hjvwx9ekTemVlEWSC2eQDHHfWNQssoGNffCYnVAhS1hevNi-om1rQES4R84HQ8EkoJO8TRhKe7MKXDTDjTQxVlCtqifcxYZDRUqBjUKUT7RjjiKIXfAZSuev-1vZHPNFlTN60TiekTimiCfm43hqVYekjcp5CbW9MMX5xAPvYYnfNQqm5oGPep_XED9UYi4mL_mlrX9Oy0LGgkxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تفاوت‌های تیروئید کم‌کار و پرکار در چیست؟
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 37.1K · <a href="https://t.me/akhbarefori/654498" target="_blank">📅 19:00 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654497">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a9gwkPP6zSG-QSTZgP3hO4y7G5pE9zBRl6Ge5rezUHo200KzJVmH9mVABtffCrgQ4PiJKu1X8A-QAiSh1DP4csiw_rkeSX_UPaJ-VvlWbi6_yGFOFx9GvmD-tuGsbjQUf7GODi7Me9Z6SD9D4bRqK6ZOSLdp_h6uf4Db3UBYq_nTWrXRcqCbaGHGv6EYquYUMWIn-K0H7gI5q87wpBJWYpkk9k-AkLiYGVtAGTRwXJmMOi75SVDYZfgx7ziAxuB1p_a1Jq0vAl1rcEQ0fB2v216kmmVUbbYxP_8RdUkfK6lrI1RlhYFfQU-_yWVggu3DgHqP8MB1cBIlpJ_MTDq-VQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
شبکه NBC: از سرگیری جنگ برای ترامپ سخت و پیچیده است؛ زیرا اهداف نظامی باقی‌مانده در ایران یا زیر زمینِ مخفی شده‌اند یا متحرک و دائماً در حال جابه‌جایی هستند
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 39.7K · <a href="https://t.me/akhbarefori/654497" target="_blank">📅 18:26 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654496">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
نگران نباشید؛ ابولا در ایران نیست!
قباد مرادی، رئیس مرکز بیماری‌های واگیر وزارت بهداشت در
#گفتگو
با خبرفوری:
🔹
سازمان جهانی بهداشت شیوع ابولا در جمهوری دموکراتیک کنگو و اوگاندا را به‌عنوان وضعیت اضطراری بهداشت عمومی با نگرانی بین‌المللی اعلام کرده است.
🔹
با وجود محدود بودن کانون اصلی شیوع به چند کشور آفریقایی، همه کشورها باید آمادگی لازم برای شناسایی و کنترل موارد احتمالی را داشته باشند.
🔹
تاکنون مورد قطعی از این بیماری در ایران گزارش نشده است؛ نظام سلامت ایران آمادگی کامل برای شناسایی، نمونه‌گیری و پاسخ سریع به موارد مشکوک را حفظ می کند.
@Tv_Fori</div>
<div class="tg-footer">👁️ 36.5K · <a href="https://t.me/akhbarefori/654496" target="_blank">📅 18:22 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654495">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">♦️
آمریکا عمان را به اعمال تحریم تهدید کرد
وزیر خزانه‌داری آمریکا:
🔹
دولت ایالات متحده هرگونه تلاش برای اعمال سیستم عوارض در تنگه هرمز را تحمل نخواهد کرد؛ به‌ویژه عمان باید بداند که وزارت خزانه‌داری آمریکا به‌ طور تهاجمی هر بازیگری را که در تسهیل عوارض برای این تنگه نقش داشته باشد، هدف قرار خواهد داد و هر شریکی که تمایل به آن داشته باشد، مشمول جریمه خواهد شد.
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 36.3K · <a href="https://t.me/akhbarefori/654495" target="_blank">📅 18:15 · 07 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
