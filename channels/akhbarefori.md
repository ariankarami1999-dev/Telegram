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
<img src="https://cdn4.telesco.pe/file/DWOw1fVnu9-oT9hLaH8nzZ9yw8HjzLKd6S9ZDBVuc5cynjVP4qvMj2MRaHeEMwV811ml-4HIRDBYYKwGm8WdrgMyCisOx58zpBYIAMS-vlGiCBJU-iN1p4sERNTFHWS5wQ539VZdGeMkdQftGm8ZpLchFewXzBMxx7eI7aIo_1RUCw9jOCDxKuZkxXB0-KQOsvgi8QwKT5j1KVznupxhii0mMXoZEq9YrwPeXNOCc5X3u6OYGC5KIji2plJ6j89q0OMcgUfzwTHHLx0wg8H62oQUzh3hCLrV5BCfX98CUnXEA9Tn64kPYu53iD7UEac-0J-cgECpCi3xuTqMeOZx9w.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.2M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforiiتبلیغ در ۳۰۰کانال تلگرام@Maino_marketer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-20 22:19:07</div>
<hr>

<div class="tg-post" id="msg-680406">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">♦️
ایران فقط نیم ثانیه به خلبان جنگنده اف ۱۵ سرنگون شده  آمریکا فرصت هشدار داد
نیویورک تایمز:
🔹
در آوریل ۲۰۲۶، ایران یک فروند اف ۱۵ ایی آمریکایی را بر فراز جنوب ایران با یک موشک زمین به هوای دوش‌پرتاب سرنگون کرد.
🔹
به نظر می‌رسد ایران از با استفاده از پهپادها برای ارائه موقعیت مکانی، سرعت و جی پی اس  به فرماندهان ایرانی در هدف قرار دادن آن  جت کمک گرفت.
🔹
خدمه هواپیما قبل از اصابت به هواپیمای ۶۰ میلیون دلاری، تنها حدود نیم ثانیه فرصت هشدار داشتند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 1 · <a href="https://t.me/akhbarefori/680406" target="_blank">📅 22:19 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680405">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k2wKvtFLLupv-aR8EVHitUPpRWpGiPiuu9JFZdyuNGVkhAgmA10lU7l91v4_YSiv1JxRNKekaqIGugnEAJlTOVVL5XNzBoW-tC1ql6M6XcpZfoMJkvbdf2ua41cc8EMBwM9YTq0KECLbCEVrqNBFolhYuXxZkkw1ESeMm33ReI6mplN327X4CXYB1tzCK6f9CM5Um618gqKaNnycmKe3MRHOn2rpx0jIOLiGB_MRUTWaEYo3RKLfkNujUAVuh1iludOQ-Sr-OHboc6ERPxCQWNtLLJwSFQDhROH5lPvc_sweKIXpQ_OriXSsSQmNmnB-kjcvFYzKMe3UeySY9GSQyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تصویری از انفجار در منطقه بنی‌حیان در جنوب لبنان منتشر شده که تحت کنترل ارتش اسرائیل (IDF) قرار دارد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 1.32K · <a href="https://t.me/akhbarefori/680405" target="_blank">📅 22:17 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680404">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bd1944e2df.mp4?token=HMglYr3pTIUGR6iumiBLPGQGTVOHg5bGlDRU5gxBnpBfW_OhJoNehAGGtzosVj2R8Bh89CNNrMlbsvfFKKqOSiUwv4015w4_TFdeVaZsPmj82_YLxdYLl3viR1wQ7OxYm3We8-as9aN5UCkSwVcys5XdZKqCEadrLth2sy-vcBbXqceESqqlHp7m-xtBHlkBgpcab9VJwUOW4iWRSkxHS4k0o8Hx9Z00HMs8kEVd6kgFeAbPjlImIwFfFBTzg3ecqt6iN8oF9yOa0Kb12iYiv6qeUMMd_rQoSdNcrKSA_prWsfjTVGhj65JmgNNXsaW1FV0Tzhbvj9K7NlE_nseNWg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bd1944e2df.mp4?token=HMglYr3pTIUGR6iumiBLPGQGTVOHg5bGlDRU5gxBnpBfW_OhJoNehAGGtzosVj2R8Bh89CNNrMlbsvfFKKqOSiUwv4015w4_TFdeVaZsPmj82_YLxdYLl3viR1wQ7OxYm3We8-as9aN5UCkSwVcys5XdZKqCEadrLth2sy-vcBbXqceESqqlHp7m-xtBHlkBgpcab9VJwUOW4iWRSkxHS4k0o8Hx9Z00HMs8kEVd6kgFeAbPjlImIwFfFBTzg3ecqt6iN8oF9yOa0Kb12iYiv6qeUMMd_rQoSdNcrKSA_prWsfjTVGhj65JmgNNXsaW1FV0Tzhbvj9K7NlE_nseNWg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
در سالروز شهادت پیامبر(ص) مدینه سیاه‌پوش نمی‌شود
🔹
هم‌زمان با سالروز شهادت پیامبر اکرم(ص)، مسجدالنبی مملو از زائرانی از سراسر جهان است؛ اما در مدینه خبری از مراسم عمومی سوگواری، نوحه‌خوانی و سیاه‌پوش‌شدن اماکن نیست.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 3.65K · <a href="https://t.me/akhbarefori/680404" target="_blank">📅 22:12 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680403">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">♦️
زلنسکی: برای خاتمه جنگ با روسیه طرحی ارائه کرده‌ایم
رئیس‌جمهور اوکراین:
🔹
پیشنهادهایی را برای طرحی با هدف پایان دادن به جنگ با روسیه به مذاکره کنندگان آمریکایی ارائه داده‌ایم.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 4.37K · <a href="https://t.me/akhbarefori/680403" target="_blank">📅 22:10 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680402">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jklkQvmSAzAJ4JRY32MPL1ZojZr1T6E-yi-3ruD21nr5IDlOM87QL6pkN8GRbeYc19jwet4or9T9AaX73JnhWI68jVMGl5ykvPs_y5bRRzsHCCl0lZpzKYgkJjTCR4JoaT1uNXsmM2Ff91dLXemUw50Pd6cGUEbuscQZt6qqakeYBgFfBSZR88dU9pzdful3Bj8NUi2qJFdyK7BZmPpLsHXjILl_kNXmSknzuvniFpJGBFHr8MFtsmQGplU-0riO88R4JZrc08UwIaKPMKzoHq5zqubOgefTuJl0qmrfP4mlsimZIVnwUUtab7GE_CgdTP_lNl4X4LOMRRHFukSrUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
صبر فقط تحمل سختی نیست؛ گاهی یعنی ایستادگی در برابر چیزی که دوستش داری
🔹
امام علی(ع) در حکمت ۵۵ نهج‌البلاغه، صبر را دو گونه معرفی می‌کند: صبر بر آنچه انسان از آن ناخشنود است و صبر در برابر چیزی که به آن میل دارد. گاهی دشوارترین صبر، نه تحمل رنج، بلکه کنترل…</div>
<div class="tg-footer">👁️ 6.7K · <a href="https://t.me/akhbarefori/680402" target="_blank">📅 22:04 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680401">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">♦️
شرط سنگین رامین برای پیوستن به فولاد
🔹
طی ساعات اخیر شایعاتی درباره پیوستن رامین رضاییان به فولاد خوزستان مطرح شده اما پیگیری‌ها نشان می‌دهد که این بازیکن هنوز قراردادی با باشگاه خوزستانی به امضا نرسانده است.
🔹
رضاییان در مذاکراتی که با مسئولان باشگاه فولاد خوزستان داشته، خواستار قراردادی به ارزش ۲۰۰ میلیارد تومان شده. رقمی که مورد موافقت باشگاه فولاد قرار نگرفته است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.71K · <a href="https://t.me/akhbarefori/680401" target="_blank">📅 22:01 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680400">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/badcdc31e6.mp4?token=G-stGWTJlHvxCRU7gvqFj6NHBWSwPZdcx7eMGleI1ptQNcqKLRGTNVZLndy4JreWIux2g_s_teDleJl8G4HcWrC76lC2veex63hIBIh5s-8sB5sv0TtbFmrUrhfJggQcXdw7F1hRm5zYikP1iFD8LVL5lmCM6TtvWXfgweCPUacazh2OL6uwpiBPDNs4AaeD-p9W7H6sXzefQTOUYa_1lPDJV4ez_r0u0Idnfz1laomKKW1GZCwHYOMYPtMelM6dMPHacm_WdzyBdGSf0LU-nbDLN7muZ3FOT1LYU2qoglCM_cEBVCHQnSgKA_tq0R-HgBz6KG7HcWb3cg4R3nUazA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/badcdc31e6.mp4?token=G-stGWTJlHvxCRU7gvqFj6NHBWSwPZdcx7eMGleI1ptQNcqKLRGTNVZLndy4JreWIux2g_s_teDleJl8G4HcWrC76lC2veex63hIBIh5s-8sB5sv0TtbFmrUrhfJggQcXdw7F1hRm5zYikP1iFD8LVL5lmCM6TtvWXfgweCPUacazh2OL6uwpiBPDNs4AaeD-p9W7H6sXzefQTOUYa_1lPDJV4ez_r0u0Idnfz1laomKKW1GZCwHYOMYPtMelM6dMPHacm_WdzyBdGSf0LU-nbDLN7muZ3FOT1LYU2qoglCM_cEBVCHQnSgKA_tq0R-HgBz6KG7HcWb3cg4R3nUazA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
طوفان و سیل شدید در استان ژجیانگ در شرق چین
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 8.72K · <a href="https://t.me/akhbarefori/680400" target="_blank">📅 21:56 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680399">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e120af53ce.mp4?token=BVgtLO_4lObQteagdJ1vQBv99JzL9n0W0NhaLTPWdhYI-9JdSFExeFhB88Lj8Vz9vuKYdwvVA1m7pGOA2bKySkvrxeBHIoaDk-TmQBC6jrWE_CYRu9COkJsdIXyfVnJ0YNxfhsd-S-aWVnJX_gcVd5xdF7UN7AQdJ_5p5U9C2YbyADiLLOzgc7ah9quX-igPYRkkvZ3_HcAXn_eg1SdLA5SyIGWkeVbAZzZlfgQzEdn2UUdY5z59oP7zjDThIaiwAQ41OUHmZoFc8nxSR6AEk76TBv4s0WAYMhWJFXfEXzWJvIK45-g4p-BEdid9he3n8iJHn03llfFWr7cELmIVvQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e120af53ce.mp4?token=BVgtLO_4lObQteagdJ1vQBv99JzL9n0W0NhaLTPWdhYI-9JdSFExeFhB88Lj8Vz9vuKYdwvVA1m7pGOA2bKySkvrxeBHIoaDk-TmQBC6jrWE_CYRu9COkJsdIXyfVnJ0YNxfhsd-S-aWVnJX_gcVd5xdF7UN7AQdJ_5p5U9C2YbyADiLLOzgc7ah9quX-igPYRkkvZ3_HcAXn_eg1SdLA5SyIGWkeVbAZzZlfgQzEdn2UUdY5z59oP7zjDThIaiwAQ41OUHmZoFc8nxSR6AEk76TBv4s0WAYMhWJFXfEXzWJvIK45-g4p-BEdid9he3n8iJHn03llfFWr7cELmIVvQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خبر تکمیلی گروگانگیری
🔹
در ادامه این عملیات، پس از رهایی فرد گروگان، مذاکرات با گروگانگیر در دستور کار تیم تخصصی رهایی گروگان قرار گرفت. نیروهای تخصصی نزدیک به دو ساعت با این فرد مذاکره کردند و تلاش شد وی بدون درگیری خود را تسلیم کند.
🔹
در ادامه، زمانی که…</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/akhbarefori/680399" target="_blank">📅 21:44 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680398">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tlO0kYrZdBudTzU2pZ1iBDoejnO0vAVt75vSywgl0WLzVOhQ-MC6EIq93RgWOa8K7O0d5qPkRNslnNJZMC3s7_9q1gvgmbOU-zn4fO20hv0jHAS3LTaxHGcdlZVQ16EklLEy9TY1IbSrNbwgmsJDrG9-nosyRIS3uPH2RMselt_KBe0uCnYTIH8yMoGHVredvxpMe815jHrTyOcJQ7Ma46K7cUiyviroVM6M771T1qj5ea104DWMSB944zHBrLpvxWzish_ILGCxYrIe0Paah56LGn4wq5r8Ags_j5c2j5DkvpzsYBykYKMS9mMp1QlvZwoCQOPOCrDbcfS0blr2bA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
آموزش آنلاین، رکورد قبولی تیزهوشان را زد
🔹
آمار قبولی‌های مدارس استعدادهای درخشان نشان می‌دهد دانش‌آموزان تام‌لند در آزمون‌های ورودی پایه‌های ششم و نهم، بیشترین تعداد قبولی را به خود اختصاص داده‌اند؛ آماری که از حضور پررنگ دانش‌آموزان این پلتفرم در میان پذیرفته‌شدگان مدارس تیزهوشان حکایت دارد.
🔹
تام‌لند به‌عنوان یک پلتفرم آموزش آنلاین، امکان دسترسی دانش‌آموزان به آموزش‌های تخصصی را از طریق اینترنت فراهم کرده است و نتایج آزمون‌های امسال، از موفقیت گسترده دانش‌آموزان این مجموعه در مسیر ورود به مدارس استعدادهای درخشان خبر می‌دهد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/akhbarefori/680398" target="_blank">📅 21:43 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680397">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/08b561de50.mp4?token=GqEfnug59RcdMPiwHlmzorblcnHnllIGtHs440pajJsTDCqxFpYrCdBJA8-2wmm6dJTaF6yClvonV3Zt4lipmuhPp3FwyJHnpD6ToQ-1DlassJX_J53ITVdPVmD9T863DKtU47bE3F20awWDaVrkDLnDR8FpFB3WQOltfjiUmwoEShtmA45p-z9NBOI2ToFQnP4S5N9SkMXn34-IgZ9esRoGR3rukj1bp3e_ZQYpOVQ56GOyOuzC7jqWwSYqNUt3tCW8a6MhJ559DZ0qaiB_yyXAL2P5_cfe7-ymVU_Szw_PiA-W96lcbu25ezirv5vvbnL82pPypJz6bPUgT6j-_g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/08b561de50.mp4?token=GqEfnug59RcdMPiwHlmzorblcnHnllIGtHs440pajJsTDCqxFpYrCdBJA8-2wmm6dJTaF6yClvonV3Zt4lipmuhPp3FwyJHnpD6ToQ-1DlassJX_J53ITVdPVmD9T863DKtU47bE3F20awWDaVrkDLnDR8FpFB3WQOltfjiUmwoEShtmA45p-z9NBOI2ToFQnP4S5N9SkMXn34-IgZ9esRoGR3rukj1bp3e_ZQYpOVQ56GOyOuzC7jqWwSYqNUt3tCW8a6MhJ559DZ0qaiB_yyXAL2P5_cfe7-ymVU_Szw_PiA-W96lcbu25ezirv5vvbnL82pPypJz6bPUgT6j-_g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پزشکیان: بر تعمیق روابط با پاکستان در همه زمینه‌ها تاکید داریم   رئیس‌جمهوری در دیدار وزیر کشور پاکستان:
🔹
اهتمام مقامات پاکستان برای همبستگی و تقویت روابط و مناسبات با ایران ارزشمند است
🔹
بر تعمیق روابط با پاکستان در همه زمینه‌ها تاکید داریم
🔹
وزیر کشور پاکستان:…</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/akhbarefori/680397" target="_blank">📅 21:37 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680396">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">♦️
یمن خطاب به سعودی: به‌جای گریه و زاری، محاصره ظالمانه علیه مردم یمن را متوقف کنید
عمر البخیتی، سخنگوی دولت تغییر و سازندگی یمن:
🔹
ارتش یمن در اعمال ممنوعیت تردد بر کشتیرانی سعودی کاملاً جدی است و این موضع غیرقابل بازگشت است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/akhbarefori/680396" target="_blank">📅 21:34 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680395">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">♦️
آتش‌سوزی گسترده در پالایشگاه نفت الزاویه در پی حمله پهپادی ناشناس
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/akhbarefori/680395" target="_blank">📅 21:30 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680394">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">♦️
حمله یمن به کشتی حامل تجهیزات نظامی در باب المندب
🔹
منابع یمنی خبر دادند این کشتی تجهیزات نظامی متعلق به عربستان سعودی بوده که هدف حمله قرار گرفته است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/akhbarefori/680394" target="_blank">📅 21:28 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680393">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KRPVpJchX7_-ndHYyNFnMNDaeiDFfJ9SL0iSIJSWRhvZgPnqeKUIprQ-MXc0Qt1p1Ek1V6W5L6RRYohRo7zdNTEpaVtYq4QurT1HbvxCMdCaPAtwhJnHvzJfYL0cAc1MWEwhUbVfUs2HEyKM_XgJgiCuJpyqjDEeVrMZXuZZMUD2widiJjCtbiygigtfy0G7icT4mkrW68t6FqU60E0a5TKEC1SQ1jKeWHPph8OMdajxZQEZKQ45Wc0yVNIwFaXboSIVEgDDgBw-9tixG3RR-9n3J5MqAPbWAC4isrJQG7qLMxS7yZObEbCdDVse-aKBIGyy7Uf27ZwEIfygBCTuEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
لحظه فرار ترامپ با کامیون آشغال
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/akhbarefori/680393" target="_blank">📅 21:26 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680392">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bf53473d10.mp4?token=XSzVfKjWuSZDrupirnmg0Z5PlExXlbFHQ5GTTYFG0RVdB5hd0JQ529KDEvpuaxzWSudcIKIDSvmxvJ92riyDOTz0zZcZaKAfRTZlT0Jg0lN81QPdnaQgs1bihPLQ1pC-EG5IP07U68oTujIat_eHXmpWbTWPQmVLjcrIA9ot9o0oxT5lHsriYOiNxnqTq39B_OcJSg_azYh8r-3X-gDWqBhVHEX-7fiW1rz1phYDjudiCMO_NQQTJlhMfWE39ciOJfdJs0dQU8fi-5VHf2xrIqc-eyoLweqYldawHqF1u_CjLV1CKNrk9Sq7NHdvzNDOU1_kvCEMB1T-FNBntac3Qg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bf53473d10.mp4?token=XSzVfKjWuSZDrupirnmg0Z5PlExXlbFHQ5GTTYFG0RVdB5hd0JQ529KDEvpuaxzWSudcIKIDSvmxvJ92riyDOTz0zZcZaKAfRTZlT0Jg0lN81QPdnaQgs1bihPLQ1pC-EG5IP07U68oTujIat_eHXmpWbTWPQmVLjcrIA9ot9o0oxT5lHsriYOiNxnqTq39B_OcJSg_azYh8r-3X-gDWqBhVHEX-7fiW1rz1phYDjudiCMO_NQQTJlhMfWE39ciOJfdJs0dQU8fi-5VHf2xrIqc-eyoLweqYldawHqF1u_CjLV1CKNrk9Sq7NHdvzNDOU1_kvCEMB1T-FNBntac3Qg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
وقتی سلامی گوشی را دست معاون رئیس‌جمهور داد و مشکل یک چوپان را پیگیری کرد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/akhbarefori/680392" target="_blank">📅 21:24 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680391">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">♦️
روایت نیویورک‌تایمز از نحوه انطباق حملات ایران با تاکتیک‌های جنگی آمریکا
🔹
نیویورک‌تایمز نوشته حملات ایران که منجر به کشته‌شدن سه سرباز آمریکایی در اردن شد، نشان می‌دهد که هم‌زمان با رو به اتمام رفتن موشک‌های رهگیر پنتاگون، مهارت‌های جنگی ایران با چه سرعتی ارتقا یافته است.
🔹
این روزنامه نوشته ایران با ادامه جنگ علیه ایالات متحده به دشمنی ماهرتر تبدیل شده و یاد گرفته است که چگونه هم‌زمان با گسترش میدان نبرد به اکثر نقاط خاورمیانه، از پدافند هوایی آمریکا بگریزد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/akhbarefori/680391" target="_blank">📅 21:21 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680390">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">♦️
برخی منابع از وقوع ۲ انفجار مجدد در مواضع مزدوران سعودی در مأرب یمن خبر می‌دهند
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/akhbarefori/680390" target="_blank">📅 21:16 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680389">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DMWi65xW8nDPG3LVWACd_hicXnl0pSk7cTQYSxznTm7WfUbWuRRmia1DFl_lCb3fThqYHoYqMfEAixEf2y2P2gh7hws18D3QDR7TJpfYZP1r9jFaemeUGyslHUDnlyuWrYXvE_yTLZj-V2Vz_XAKumGnjqmbpZfQOQrx2yqD8EbYsRzxqiXABoZruiPDGOC3e7O3_3rwMQH0oxRaQ2VfkyU0bK5QSTD1lEvruexGrwSwq3zME5WYgn_EBpYwM8-5rHVhEnnmv2KN1QwT__ky7pGXeXBjG7q2c4Z-v-uJAS2MLafNmKSiAYnlNXWYQo6bhpgJ0PcV5wND5hU6IZgQ9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
توئیتی از ادعای مبنی بر اینکه
جت سلطنتی امارات امروز صبح به تهران سر زد و بعد از ۱ ساعت ماندن، برگشت
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/akhbarefori/680389" target="_blank">📅 21:10 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680388">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">♦️
تعداد کشته‌های زلزلهٔ کلمبیا به ۲۲۴ نفر رسید
🔹
تعداد کشته‌شدگان زلزلهٔ ۷.۴ ریشتری دیروز در کلمبیا به ۲۲۴ نفر رسیده است. کلمبیا این زمین‌لرزه را «فاجعهٔ ملی» اعلام کرد.
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/akhbarefori/680388" target="_blank">📅 21:09 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680384">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gIedKX-VQZRPcfwnAhw0MLAkDQdvSdriS712corFRh6tEk_vlXOYbjxHua1VH-7M28Z3XnRj9g3S4ZsVhU6hJe4s0oIKbSppNa_5ZR2BgQAXi1EkUWgGq_15tM5VCZN9-sv-EY1bXVZsg20hgcJLjxwTfoYx6VtxKFbn3oSnpjxP516SA4CznPE4UrTT2G08vhEFt-zurKbTNhU5hcM5pw8ze5EiO21Av3RaZzyczhMitdhT9FHL-Bb7Iz032Frbixpd_v0-BxCw7xx5a-rdEGe4Namp2-i6VA2zri4lXuVpoq3IMcVH38TJYPCUYOKngx3RYJ4h-npjuUJNc1RgwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rpGNOYrUI3TV-Cs_jmm7deYprTIm-aw3qULm5d_0cdEBLxASe4sqo37OFaZah8jDk2s8Q9oR0lKmK7wwbLTQE140xz7k4PmC9knCOsJoU1bW5ptfrg4Dy-f74b2sL1G7pRyxkMcthFbVjzKwflFsZA52gF9zRjfJOpAIQUU8uLxlRQRGTofvYNq0zSaNaVAyKi092f-bZjxqH72ZfyeEIghxc9gXEPzkNIr0EYhHUZoOrx-jSPD3T5aPTN2k5U414ZsZSrC5M87OupQlQi_uQD7DT4OFDHX-2mBmD3TF1-ZiK_10zOz2C2pFMWj3Dpf0g-1YEg-ZOYr-VbHIh5Xqtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tFY0tMYaJj8WgxJvD1ILFXtxaYUumpLvMaE56jWQ3gORy6wlgzlnogByascjhNf-zMf29ICPZ1MigGWuFw7C88S2RyDs3SEd2XHBfaEYV2yPdlwQ34TqddzZ6d0cvMbAAUjXCBaaRnRMNXb49LQouFTDg2yHBbNcsAJZt_zG0JsrW5kF4k-thdPzVObketezmunWPN4Yf_q3Nr4VwpnGeDujx0DQEfcg8gWG0meEXXGsykFQjaX1Vaw6ky8_mwCz0P48qJ2spON9fB8-zYQC651hPxShpRw3wngek81_Pemj3EGnzJEqMYSgyvEaNq08wlN0x-Fo2snRzN6xQBW2Nw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vM01Djdtu3AI1sFDCezcG3GD6VeOz8nK29oy-tnFcumwQZ0amlfXlO3ywhUlxv9ab7QMXsdglSVlnxCUv_jpVilq4xyqJfsn8PTNhg3lo-pVQWiWwBO04o4g8hdXZBVG-8-ZXis431fntx5MYbTPfoIe8fiOsHaAfHdutWJXaedNHaE0QxoocBD9HJNhblG6tmbPl4jZp5gdw1s77ed8jHm4ZKlNS9JYPpbSihTBlgybkZ7z4qyOTloI63rAhNtguAcvZaIHwFK9VbTtn_MRdfcOkq4lsv-eZhQzvVeR37vRsAHXBY4LzxxBGmcp-7VCP1jO3dvX07L2DLClxoW9aA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
لحظه فرار ترامپ با کامیون آشغال
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/akhbarefori/680384" target="_blank">📅 21:09 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680379">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LksJWJORMcrPZm7p_DNMYEExqw_zytqqT3IIc1G6-BD6-6gBpQJMQNlGeTwlDlveP9rKKOvZ7y0CuPEd2coLIai7T_mdJylFA0b-0ixrfhONq-YJRL7PNOYq4vzOY-GFBoPCGYnp4wMIFEQ5dqfmhPd3JANuMyJxNlAQd-A307lj2sWwDft87Xx9IuRnZNUIxj35Z2oHQO-1DnF3eJzNkBDe3tXjtMOMJXUVzEah9QcSRXTDV57T_kmvbiDri6I1UedQJlAOxBFrm7QJPRA4BXq9P4zgyD0-SYYqNEkGe5-qYuPV804tpKBtkg56rc9BwNyuRiNkxo1omGtM25QZOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
شبی که ماه کامل شد
🔹
کارگردان: نرگس آبیار
🔹
ژانر: درام، عاشقانه، جنایی، مهیج
🔹
بازیگران: الناز شاکردوست، هوتن شکیبا، شبنم مقدمی، پدرام شریفی و…
🔹
خلاصه داستان: فائزه، دختری جوان از جنوب تهران، عاشق عبدالحمید می‌شود؛ عشقی که در ابتدا آرام و ساده به نظر می‌رسد،…</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/akhbarefori/680379" target="_blank">📅 21:02 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680378">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBimebazar</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rnt53cst-Twci7IzE0fRx0CJD-0Vax-8wipklbz4XibrHNAm9ifE5aqErvjySCHhDHTTkseIAGDt-ofaroALwkItkCxvfHwW2zsq56xuzjvXYOJoVlZUAsaL1DukvLSJIuHpw185HdtG0AtYEe2DCa2QvSiVAL1y0i6L35Ih77LjqM-pdG7_-NohLvh5nDSsJOO3GzxOzpdx74sHmvt59EDsCpkUNwNwrU_d5Ng7s-L-JtQMXCl8lcW6JHi016rAgrAv5snEmf_g92Vpny2l15VV1eET4NmFMgYK-dHzvXZyW5Qox3B3wgS3kBchOPrKEhNd0OMQoDTLfzYDjdKWlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
با بیمه‌بازار، هر جا باشی بیمه‌ای!
فرقی نمی‌کنه
کجای شهری
؛ پشت میز کاری، توی خونه‌ای یا حتی در حال سفری.
✅
با
بیمه‌بازار
برای خرید بیمه
لازم نیست جایی بری
...
کافیه وارد
سایت بشی
، بیمه‌ها رو
مقایسه کنی
و فقط در
چند دقیقه
بیمه‌ات رو بخری.
👈
برای مقایسه بیمه ها وارد شو
#بیمه_بازار
🟡
@bimebazarco</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/akhbarefori/680378" target="_blank">📅 21:00 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680377">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">♦️
پالایشگاه نفت لیبی بار دیگر هدف حمله پهپادی قرار گرفت
🔹
عصر امروز انبارهای پالایشگاه نفت منطقه الزاویه در شمال غربی لیبی، بار دیگر هدف حمله پهپادی قرار گرفت.
🔹
به گزارش الجزیره، اتاق عملیات پالایشگاه مذکور اعلام کرد این انفجار در اثر حمله پهپادی رخ داده است.…</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/akhbarefori/680377" target="_blank">📅 20:57 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680376">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/84874eea4a.mp4?token=hMDHc6rOYIMpDMb3NDqB_Ju6P8J9CuG72z-N9bldVIiDwO7jcXzEfMqTQlDgMkv-exm719F3Xe0j7h7wXmIjx8raBFp81heKaO68NrSrGudQQ32Joj21zaWVkEHrQfqJ1UIj_o6hNA7CUKvX-qgYRwP1WjNqfp_eTvbcDvlpeds0IQRhgLvFH6FWRv2D8uXWf3sRYpSSdVOFKGvBymG3Mexc9U0obwm9gQpsrqyDIa8fjNJnvOCiWgKl1G7os5WhpO3CYIbZI0PT5QQPjTkkoRkHKwzOorKp_IfY_6Xp3ByJ9QZ_H7sPH_yq6MSCKk8SUWUPiu4qLZoQQFkSsbbv4A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/84874eea4a.mp4?token=hMDHc6rOYIMpDMb3NDqB_Ju6P8J9CuG72z-N9bldVIiDwO7jcXzEfMqTQlDgMkv-exm719F3Xe0j7h7wXmIjx8raBFp81heKaO68NrSrGudQQ32Joj21zaWVkEHrQfqJ1UIj_o6hNA7CUKvX-qgYRwP1WjNqfp_eTvbcDvlpeds0IQRhgLvFH6FWRv2D8uXWf3sRYpSSdVOFKGvBymG3Mexc9U0obwm9gQpsrqyDIa8fjNJnvOCiWgKl1G7os5WhpO3CYIbZI0PT5QQPjTkkoRkHKwzOorKp_IfY_6Xp3ByJ9QZ_H7sPH_yq6MSCKk8SUWUPiu4qLZoQQFkSsbbv4A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آتش‌سوزی گسترده در پالایشگاه نفت الزاویه در پی حمله پهپادی ناشناس
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/akhbarefori/680376" target="_blank">📅 20:50 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680375">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
رییس کمیسیون عمران مجلس: عملکرد بانک‌ها برای تسهیلات مسکن، زیر ۲۰ درصد است
محمدرضا رضایی کوچی، رئیس کمیسیون عمران مجلس در
#گفتگو
با خبرفوری:
🔹
درحال حاضر حداقل باید ۶ میلیون تولید مسکن داشته باشیم تا تعادلی در عرضه و تقاضای مسکن داشته باشیم. بخاطر عملکرد ضعیف برخی از دستگاه‌ها از جمله بانک‌ها به سمت تولید مسکن نرفتیم طوری که عملکرد بانک‌ها مجموعا کمتر از ۲۰ درصد بوده است.
🔹
هرکس برای مسکن ثبت‌نام کند و خودش رأسا به بانک مراجعه کند، بانک مکلف است که به او تسهیلات بدهد اما بانک‌ها می‌گویند ما صرفا به کسانی تسهیلات می‌دهیم که از مسیر راه و شهرسازی به ما معرفی شده باشند.
#فوکوس
@Tv_Fori</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/akhbarefori/680375" target="_blank">📅 20:48 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680374">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I4v5Mc0QNjPXqF-O7FGrbOf3TZcXsqqG1eVkIfdrpztzhQVeRuJSiUtuWqSV6zHr5kg3hnLMC129k9iGXEznXNZfNtC80bSLpzyodds-zvsYFXvxNhoFKkuMA02y0UVCpubEThDGYhO9EnRNE1KQMQ4p798VNxiteeuDzgFmMRl3JAremSJImvdEQap6fLFLCc9QWTzEswf9Zcgp4KNO_tLRMeOKd9rXCSXP4j058Xo9eoT4POtfmJZ52NgHBeJIh5FmRLb2kZHy7JQsOi7Qw2rzMXleUFsG1DNV3wKG0mKmLtexGDdmKhtaUpv1ae6W4VbpHrpQTge8Uun3C5M6nA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پزشکیان: بر تعمیق روابط با پاکستان در همه زمینه‌ها تاکید داریم
رئیس‌جمهوری در دیدار وزیر کشور پاکستان:
🔹
اهتمام مقامات پاکستان برای همبستگی و تقویت روابط و مناسبات با ایران ارزشمند است
🔹
بر تعمیق روابط با پاکستان در همه زمینه‌ها تاکید داریم
🔹
وزیر کشور پاکستان: روابط ایران و پاکستان مستحکم و ناگسستنی است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/akhbarefori/680374" target="_blank">📅 20:47 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680373">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">♦️
شنیده شدن صدای انفجارهایی در شهر مأرب یمن
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/akhbarefori/680373" target="_blank">📅 20:45 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680372">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">♦️
اکانت متخصصان سلامت روان آمریکا در واکنش به پنهان شدن ترامپ در کامیون حمل اشغال: چطور ممکن است کسی تقریباً در تمام کارهایی که در طول زندگی‌اش انجام داده شکست خورده باشد
🔹
اما در نابود کردن اعتبار قدرتمندترین کشور تاریخ بشر موفق عمل کند؟
📲
🇮🇷
✊
@AkhbareFori…</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/akhbarefori/680372" target="_blank">📅 20:41 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680371">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">♦️
روایت سفری شگفت‌انگیز از طبقه اول تا هفتم آسمان؛ هر رفتار دنیوی در آنجا دیده می‌شود
🔹
00:11:40 عذاب دیدن برای جملات به ظاهر ساده‌ای که باعث رنجش مادرم شده بود
🔹
00:16:25 نورانیت عجیب و جایگاه برزخی والای پدر، بخاطر حرف‌های مردم در مورد او
🔹
00:30:40 دریافت پاداش چند برابری از خداوند در ازای بخشش اطرافیانم
🔹
00:34:25 بازخواست شدن در برابر اعضای بدن از جمله قلبم، بخاطر غصه‌های بیهوده‌ دنیایی
🔹
00:52:30 شکایت سنگ و درک آثار آزار یا خیررسانی به حیوانات
🔹
00:59:00 پاسخگویی و مسئولیت انسان‌ها در برابر دین منتخب
🔹
01:08:20 تردد همه موجودات از آسمان هفتم به کربلا
🔹
01:12:50 تعظیم و سجده تمام ملائک با نوایی دلنشین بر حضرت زهرا (ص)
🔹
01:22:10 تلاش روح فرد خودکشی‌کننده برای ورود و تصرف جسم من
🔹
قسمت بیست‌وهشتم (فراز و فرود (۱))، فصل پنجم
🔹
#تجربه‌گر
: سید محمد موسوی
🔹
قسمت قبلی
#زندگی_پس_از_زندگی
#فصل_پنجم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/akhbarefori/680371" target="_blank">📅 20:33 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680370">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">♦️
ترامپ از فروش جنگنده‌ها به اروپا برای انتقال احتمالی به اوکراین خبر داد
🔹
رئیس‌جمهور آمریکا گفت ایالات متحده تسلیحاتی از جمله جنگنده‌های نظامی را به اتحادیه اروپا می‌فروشد و سپس این اتحادیه می‌تواند به‌طور مستقل درباره نحوه استفاده از این تسلیحات تصمیم بگیرد و آن‌ها را به اوکراین منتقل کند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/akhbarefori/680370" target="_blank">📅 20:31 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680369">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/028d009122.mp4?token=XwSsyIba3fwJ2A_iyODURltQ-_SomVMJ5O9XXpIbe5InoXLKfjWBUnC4c0JYD9atLHvR0-hXyWZkrrzmb5W_nOROmhmBhR3MvfkhSA9yX3wQmzVYUar4zu7KIuZHZfElwhNSFzDCcc6IvJMXckVyNSH79jrQ97P3cWVQ89ZhXh4rZGPkFNsDZrDHBt3MN7CB3w6SsWAsnhS8xM4xq10sTylxCTk2X4k8kpCj0OYCgaRA8dNMLajreyR6pyV3_aRbaNlmcZKlIfE7Nwoqk2vQKIGj_dwi_NKmF7opfwaPmUhe0f2zesheLbEarKKcBY1pZj9sbzLMvwyW2iE7lhlkeQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/028d009122.mp4?token=XwSsyIba3fwJ2A_iyODURltQ-_SomVMJ5O9XXpIbe5InoXLKfjWBUnC4c0JYD9atLHvR0-hXyWZkrrzmb5W_nOROmhmBhR3MvfkhSA9yX3wQmzVYUar4zu7KIuZHZfElwhNSFzDCcc6IvJMXckVyNSH79jrQ97P3cWVQ89ZhXh4rZGPkFNsDZrDHBt3MN7CB3w6SsWAsnhS8xM4xq10sTylxCTk2X4k8kpCj0OYCgaRA8dNMLajreyR6pyV3_aRbaNlmcZKlIfE7Nwoqk2vQKIGj_dwi_NKmF7opfwaPmUhe0f2zesheLbEarKKcBY1pZj9sbzLMvwyW2iE7lhlkeQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آتش‌سوزی گسترده در پالایشگاه نفت الزاویه در پی حمله پهپادی ناشناس
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/akhbarefori/680369" target="_blank">📅 20:27 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680368">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eVAkJ75_swGngrFKzHl-HHg5cD8ZOc5bseT0B4J6p_Z3cW040FcUqtOwSrCzquR4ZrO6aDEMgripTvajwqpqEke0grImjq0d_fg26Ki_epmHCE067WSlEJ60unEX2TzHlOHJ9WpjrWosLko0xaks1T8Rx_sGi-XAuOf_lE9wldkF06IUpzPQVjDrrv1vXWNvnoW0IiuM-pBd8FAOaKbCaMatuXbMfFuXCv6wyNF8sLUHUtamJFx7ivgN7GyzGceiL4qRyo-pVdBH8DdkhxYWX4KJz9B3pvtsp_ybccy0LkYR4zn48Xxro6bjixFfmwdsHqkDuMYGhEZSGgz7F79KSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
این جنایتکاران که فهرستی از صدر تا ذیل‌شان موجود است، آرزوی مرگی آرام و در بستر را با خود به گور خواهند برد
🔹
بخشی از پیام رهبر معظّم انقلاب به‌مناسبت تشییع و تدفین آقای شهید ایران
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/akhbarefori/680368" target="_blank">📅 20:22 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680367">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromوحید یامین پور</strong></div>
<div class="tg-text">احکام استشهادی سربازان آخرالزمانی امام زمان(عج) صادر شد‌. آنها که پیش از این بر این مناصب بودند به شهادت رسیدند و اینک گروهی از دیگر مجاهدان وارسته از ناز و نعمت دنیا، آگاهانه و شهادت‌طلبانه جانشین می‌شوند. نظام جمهوری اسلامی حالا از همیشه "مقدس"تر‌ است. نظامی که مناصبش تهی از بهره‌های نفسانی و جاه‌طلبی و اعلام آمادگی برای ترک راحت دنیا و فداکاری برای دین و وطن و انسانیت است.
کاش ما کمترین باشندگان این سرزمین هم امکان خدمتی اینچنین مقدس و مجاهدانه را داشتیم.
➕️
@yaminpour</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/akhbarefori/680367" target="_blank">📅 20:21 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680366">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/22e92e2968.mp4?token=CIy6i2JME4RfSrlTGLdB3OhtlyXsDeEtx5gdBdmakQ4Hgn92w-FDCLEyPpHNs7PYTtLaXQ9PmRGZjRPctUU83Dg7N_veC50jsnf8jQeWrvn3mv9JpVyHbFtPtiSTMIIjnW5EoibR-3ipbHuP5kE1YScDI-i7OAV9PK77H9w30IofeFxff7QybuFX_qNISjehi7dsmMNKfSzUD0s0bDpVfjOxyTgT4fBZQqLLY1eaRc8F1YG7bfZbG19qjUM2FJ5ko_LVqMWTowuUs2ywMop3oJRiVGyUsu2FtjdhbtQ5tni3RzpQCnu7mYIDROPfMu8xqrFw8Eg0HdmnnlTPWCGcVQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/22e92e2968.mp4?token=CIy6i2JME4RfSrlTGLdB3OhtlyXsDeEtx5gdBdmakQ4Hgn92w-FDCLEyPpHNs7PYTtLaXQ9PmRGZjRPctUU83Dg7N_veC50jsnf8jQeWrvn3mv9JpVyHbFtPtiSTMIIjnW5EoibR-3ipbHuP5kE1YScDI-i7OAV9PK77H9w30IofeFxff7QybuFX_qNISjehi7dsmMNKfSzUD0s0bDpVfjOxyTgT4fBZQqLLY1eaRc8F1YG7bfZbG19qjUM2FJ5ko_LVqMWTowuUs2ywMop3oJRiVGyUsu2FtjdhbtQ5tni3RzpQCnu7mYIDROPfMu8xqrFw8Eg0HdmnnlTPWCGcVQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ترامپ در آستانه کارتر شدن است
فرماندار سابق ایالت نیوجرسی:
🔹
ترامپ دارد به چیزی تبدیل می‌شود که فک نمیکرد انقدر به آن شبیه باشد؛ جیمی کارتر. او گروگان ایران شده و تمام این ماجرا هم کاملاً داوطلبانه بوده است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/akhbarefori/680366" target="_blank">📅 20:15 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680365">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/18975e3ffd.mp4?token=B4ubq6oddMVeMz3Crkc15TCMQqFTnOsW7SolX31ZMpx6vXpb9Mus9n_u9CkLlMbxdLoVclbYn8-SET-YrLG85NxvfqRHqZgJ5V59hXABfp9DtM-8SFsE80Y3V4ygGTQ-QiDGuxWBdTcY_Ftn3bO6iUe-1g4Mt5OaSl7cjDk7H4hWizY7SJJUHc-O5SHe2P3aXMzLcSC5EWRSvlY0t1tNYlYtrqOIDUXV0HEr2UTSsQ0d3hs9AatBRzqS2q-NMgtD8V7xWw-lk15MdaEg0NgAAiJuqpXQa4_Ffst7tIqkuE_EXb2S2seRkHB-r19juvc1mmNG2HJVRTlfSJPmaDIdEA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/18975e3ffd.mp4?token=B4ubq6oddMVeMz3Crkc15TCMQqFTnOsW7SolX31ZMpx6vXpb9Mus9n_u9CkLlMbxdLoVclbYn8-SET-YrLG85NxvfqRHqZgJ5V59hXABfp9DtM-8SFsE80Y3V4ygGTQ-QiDGuxWBdTcY_Ftn3bO6iUe-1g4Mt5OaSl7cjDk7H4hWizY7SJJUHc-O5SHe2P3aXMzLcSC5EWRSvlY0t1tNYlYtrqOIDUXV0HEr2UTSsQ0d3hs9AatBRzqS2q-NMgtD8V7xWw-lk15MdaEg0NgAAiJuqpXQa4_Ffst7tIqkuE_EXb2S2seRkHB-r19juvc1mmNG2HJVRTlfSJPmaDIdEA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اولین تصاویر از ۶ متهم پروندۀ قتل حمیدرضا رجب‌زاده
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/akhbarefori/680365" target="_blank">📅 20:09 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680364">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0b9f62ee96.mp4?token=smOVcMkum5zYcYEO7fXzj2k0LasPZd4AW_TufW7hhKccP2gSBJ-Dol4tnihBQHUjG9HcIM3_fpSsa2BBshMtHPRxsJKY-ErzaVXgcmHkIi7AEgOdYTv06IA5BJyvB_0PL4fR1bGvirB4bHBOSoswTrDOXt1QACKlZN8dsw-NIe-jf1hIE42jUMHt3VT7qSxEC-QcgFta6n-XnK5dxEuqyI80IhNtNsOQog6GmHnOX6MQuPY9v79fBlBUcnHuvY0D3jK4FfB3nOMew1nzB5bplNcCDVVWVns7RkPlF_rRCB8ODJSbH7lGfc5h-TLPgYNEWusBFBGs0GKxyY8BIUGWvg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0b9f62ee96.mp4?token=smOVcMkum5zYcYEO7fXzj2k0LasPZd4AW_TufW7hhKccP2gSBJ-Dol4tnihBQHUjG9HcIM3_fpSsa2BBshMtHPRxsJKY-ErzaVXgcmHkIi7AEgOdYTv06IA5BJyvB_0PL4fR1bGvirB4bHBOSoswTrDOXt1QACKlZN8dsw-NIe-jf1hIE42jUMHt3VT7qSxEC-QcgFta6n-XnK5dxEuqyI80IhNtNsOQog6GmHnOX6MQuPY9v79fBlBUcnHuvY0D3jK4FfB3nOMew1nzB5bplNcCDVVWVns7RkPlF_rRCB8ODJSbH7lGfc5h-TLPgYNEWusBFBGs0GKxyY8BIUGWvg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
با این روش میوه و سبزیجات شما همیشه تازه میمونه
🔹
هوای داخل کیسه خارج میشه ماندگاری میوه و سبزیجات چندین برابر میشه! #ترفند_فوری
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/akhbarefori/680364" target="_blank">📅 20:05 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680363">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/STNvYknyAKyvHdeUoOq74mG5wbcametLKyIt_iR_AAPhDRtorISW0B9_KIL4eP8E5-DwAD--aE89zFKKtn5f2HXRCs5BCE1X-ugSG6Fm0ZBX07cNB0HzT0gIg6pQArrdSbqbyzyGQPYKZnD-FKCaJauEMf3BnzpC-hztQrqRKmArb3i7Zaoj_IXu4NWwRa-d3Q1yokcdkuR5vKT2DjUyIQAsdhrVyWb_eYGX_fOZCU7l6oDfNczxXJRch_huXWhZmnxQ9RJrBOVF0_WPJVciVx0dZURjHHOkm3tSrvfc_FW_8KX2GOlsooILujfw-LpS2qMQI08s6uaCO5KBUTBddA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👠
UPGRADE YOUR STYLE!
‼️
تا ۷۰٪ تخفیف بر روی کیف، صندل، کفش، اکسسوری و البسه زنانه و مردانه چرم mono
💳
پرداخت اقساطی با اسنپ پی در خرید آنلاین
💳
پرداخت اقساطی با اسنپ پی، دیجی پی و زرین پلاس در خرید حضوری(مشهد، اصفهان، شیراز، اردبیل، بابل، بابلسر، کلارآباد، زاهدان)
🆔
@monofashion_co
🌐
www.mono-fashion.com</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/akhbarefori/680363" target="_blank">📅 20:03 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680362">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4f75305259.mp4?token=WuwohweVYYNf8t6KX3BRr0raOO9Hwk7fGSQsZ_QYW5CttoeKY7XXiKOoG7huFIMGit_Xm5fsJOJTlNGmJFR1qnGPeFP3im8TRffEIj7g8z6MJvIPEw70MXuE2DrcicwZD2_AKLipgx2-D0ibXXf2qlhvG7KxkKvr9fjsf9UB90q50KRDF4qTQIhfTdTtqGpZUWhChtW2bq3FfpfN2LXDd3UdUrM6vhI35KpfHQQuaUOG_-u2ART3HKT34CVZO-wsM0-fPdZm5pc_Lw8zAIe6V82EEywjPZyMkNOdWZWBKS6H08RQjYdeiFm4G5EdR3CvKSHePnAg23SwUkzXB9uMBw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4f75305259.mp4?token=WuwohweVYYNf8t6KX3BRr0raOO9Hwk7fGSQsZ_QYW5CttoeKY7XXiKOoG7huFIMGit_Xm5fsJOJTlNGmJFR1qnGPeFP3im8TRffEIj7g8z6MJvIPEw70MXuE2DrcicwZD2_AKLipgx2-D0ibXXf2qlhvG7KxkKvr9fjsf9UB90q50KRDF4qTQIhfTdTtqGpZUWhChtW2bq3FfpfN2LXDd3UdUrM6vhI35KpfHQQuaUOG_-u2ART3HKT34CVZO-wsM0-fPdZm5pc_Lw8zAIe6V82EEywjPZyMkNOdWZWBKS6H08RQjYdeiFm4G5EdR3CvKSHePnAg23SwUkzXB9uMBw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚗
هر آقایی یکی از این جاروها توی ماشینش نیاز داره
👨‍🔧
🎥
برای دیدن کاراییش ویدیو رو حتما ببین
❗️
✅
سه روز ضمانت بازگشت
🏠
پرداخت درب منزل
تعداد محدود! همین الان کلیک کن روی لینک زیر،
تخفیف ویژه
رو دریافت کن
👇
https://khabarfouritel.affdn.com/lead/44273
➖
➖
➖
➖
➖
➖
➖
➖
➖
5000 محصول تخفیفی دیگر
👇
khabarfouritel.affdn.com</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/akhbarefori/680362" target="_blank">📅 20:03 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680361">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">‏
♦️
سخنگوی وزارت امور خارجه آمریکا ادعا کرد که این وزارتخانه با همکاری وزارت خزانه‌داری، در حال اتخاذ تدابیری برای تداوم کارزار فشار حداکثری علیه ایران است
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/akhbarefori/680361" target="_blank">📅 20:03 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680360">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e3f4ba4b2b.mp4?token=rh1siz3OOrJm5mbo7ntdo1ZhGU2cFkLmw6aPQ7zenWuJPnzYSBAv3BboXi2n9vColN-B4rwaAJfjht18UeZ4Gu6Nhh7xJH_Z-HaZowLBwX3CwbyXL8e03jrzfxyBKYeL-xVL9RgohKTvoFUaylPHLZuXI-cQZvVjFqzasCyjG_KC5DaqFL_Feg9Off7LFvaFgexKxK3zjyV8yOhOLEfTh-fVqVdfmIN7oXdjYVdaF5itcYvO7H-FqikIIhPLlWI_xocPgcjTbZGC00jbm5V62K1VtolLkk5i1nwPkBqODBS-wTzcFeBjXcomYgp5Cry6KH9hjmCLBBA4WPTsiVsBXQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e3f4ba4b2b.mp4?token=rh1siz3OOrJm5mbo7ntdo1ZhGU2cFkLmw6aPQ7zenWuJPnzYSBAv3BboXi2n9vColN-B4rwaAJfjht18UeZ4Gu6Nhh7xJH_Z-HaZowLBwX3CwbyXL8e03jrzfxyBKYeL-xVL9RgohKTvoFUaylPHLZuXI-cQZvVjFqzasCyjG_KC5DaqFL_Feg9Off7LFvaFgexKxK3zjyV8yOhOLEfTh-fVqVdfmIN7oXdjYVdaF5itcYvO7H-FqikIIhPLlWI_xocPgcjTbZGC00jbm5V62K1VtolLkk5i1nwPkBqODBS-wTzcFeBjXcomYgp5Cry6KH9hjmCLBBA4WPTsiVsBXQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بی بهره از فروغ ولای تو یا حسن
مشمول این حدیث پیمبر نمی شود
فرمود دیده­ ای که کند گریه بر حسن
آن دیده کور وارد محشر نمی‌شود
🔹
رحلت پیامبر(ص) و شهادت امام حسن مجتبی(ع) تسلیت باد
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/akhbarefori/680360" target="_blank">📅 19:56 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680359">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/prWya7MzE3ur421siNmyVidjFpXNOIKKXUD64UL_3xsizqgMZ21oohBKW3vc5bC_sHeOLiqdcLYsbaQTgSJGmaiNSP-ivW64_Aq-zgGHY5PviQHZ4HUhHkGwJtpvKXqpv6uGIEnGAREhIpMslIoHAMX3iasfJYDMECcf2Yk-mgnCrC17hnzwQVYmf2Yi0_3Je2_QmtT-UtcYM-JIfplQ2g82vHgvfC-nd-EKIb7ypWmkdHeLSWP0fFdUBzdBWX8z3CRRLJLd3v2Kpw5z0KWT6nc8FJDBoLfH8oJfodfmZX03ir744_6beafu_btUfMFFZzm6WS5zFxSeXil0cXSD3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کشورهایی که هرگز مستعمره اروپایی‌ها نشدند
🔹
در طول تاریخ استعمار، اکثر کشورهای جهان تحت سلطه امپراتوری‌های اروپایی قرار گرفتند؛ اما کشورهایی مانند ایران، چین، ژاپن و کره همواره توانسته‌اند استقلال خود را حفظ کنند و هرگز مستعمره قدرت‌های اروپایی نشوند.
@amarfact</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/akhbarefori/680359" target="_blank">📅 19:54 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680358">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d0739cab6c.mp4?token=kYifKQvbMSAtAUMOkXpRdOmhlo8s212HDVkw6sssbuqrMhrD_Vi3o1v6djjxRlNBaEk6H9P4nZJBOJTJhA9ZmL1arE8eNAuVLgz7pkiopPmNA2zUNK7AY7QXTL037MpcNhzxE5VCpSKXYfapwiiHFcARvZa-RjO6DvH-AjUVgB2HozTajQdCAtL7uI8Z7SQ38D0m4TOgKCrjTzBdPvALNpbYCsOG4UrKIadq4fQbRo-JgXvwKZHDk4PhBEGwaWydkSxDlnaALpqpdJkuNmi3-jtz6xrxsVDwBBFHAUJEKC2VEhgKzqq-VD1M5MZdNG71DniihPWB1pFnSCeo-CHQJEalk1sv1e4R16IQ8nnV_sXBCcp5K4bqld2Zi1LvHmrrOkRXBxx788rG0BHEtH2PIIRE1mJezDo3rRc-TAZ21RL7INOhFnTEky5pNVVOZXoC3aehBOyCCiCVOEree-y7UmeuaS0T8w6DlMEKU-WTLz4sXouL59Gut6iKnAlk7hX1AyApdAdp92wfJl3n_Kl5G-8E2OXIhPLWmOq35Qwug2d9-ab-qDDPh8OZKEhz8YfIbOeCNQvoq59H1BvsxC1v2RsInOKZsZQKpxlqO9iDeC-BIuMwq5Cwtdvgz2Xlgb6cPf7_qd12U1AU7Jax1p_hGz7JCAnE6YDwtYH-KhxhSf4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d0739cab6c.mp4?token=kYifKQvbMSAtAUMOkXpRdOmhlo8s212HDVkw6sssbuqrMhrD_Vi3o1v6djjxRlNBaEk6H9P4nZJBOJTJhA9ZmL1arE8eNAuVLgz7pkiopPmNA2zUNK7AY7QXTL037MpcNhzxE5VCpSKXYfapwiiHFcARvZa-RjO6DvH-AjUVgB2HozTajQdCAtL7uI8Z7SQ38D0m4TOgKCrjTzBdPvALNpbYCsOG4UrKIadq4fQbRo-JgXvwKZHDk4PhBEGwaWydkSxDlnaALpqpdJkuNmi3-jtz6xrxsVDwBBFHAUJEKC2VEhgKzqq-VD1M5MZdNG71DniihPWB1pFnSCeo-CHQJEalk1sv1e4R16IQ8nnV_sXBCcp5K4bqld2Zi1LvHmrrOkRXBxx788rG0BHEtH2PIIRE1mJezDo3rRc-TAZ21RL7INOhFnTEky5pNVVOZXoC3aehBOyCCiCVOEree-y7UmeuaS0T8w6DlMEKU-WTLz4sXouL59Gut6iKnAlk7hX1AyApdAdp92wfJl3n_Kl5G-8E2OXIhPLWmOq35Qwug2d9-ab-qDDPh8OZKEhz8YfIbOeCNQvoq59H1BvsxC1v2RsInOKZsZQKpxlqO9iDeC-BIuMwq5Cwtdvgz2Xlgb6cPf7_qd12U1AU7Jax1p_hGz7JCAnE6YDwtYH-KhxhSf4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سردار محبی: سرعت افول آمریکا بسیار زیاد است
سخنگوی سپاه پاسداران:
🔹
خبرنگاران در جنگ تحمیلی دوم و سوم، قوت‌های نظام را به تصویر کشیدند.
🔹
سرعت آمریکا در افولش بسیار زیاد بود.
🔹
آمریکا در ایران، با کمتر از ۲۰ روز جنگیدن به استیصال رسید و شروع به واسطه تراشی برای مذاکره کرد.
🔹
آمریکا در همه اهداف خود - از جابجایی نظام تا چپاول ثروت‌ها - شکست خورد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/akhbarefori/680358" target="_blank">📅 19:51 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680357">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e2ddef2586.mp4?token=WlBpep2fJJCInpoPgm3pgw1EoAJtK-YSMY6S6-NQViJkOJJ8ZCdS7KtPOi2eevVCVxYpej9bwLw4XpPff7dMP9MffgniF0kI4iXwP5hW7r7UO8-wecWBopqr34tSNtgtmK4lpgJOMd1xhnFWUYyTjtF4EFEPBGNxzo3yfYuE9yyIQuTY_zmkz9mJJGbukaQW58s4yq7jXfHqIS-NDfKEMcxfK0JBMZCZmhPaqBk3SKaw2oQjL7BJ0f9RSqh67OkOitLFlNfFZWoH2eXgExTbHa_qNXDfK8_ebTZDyGrAlCD8yzx4_1tzaLmJUWHI4V2sccfaJ36ChtrqlElvjxwD7KO9bXoN-yRTpw66pdcQLGLZ4CKj8c2eCLhTObMv6xNoQCjYrYNC_uRoPPhGouwWoJKSaR8lONb7y5TwKHuOyrDgXT4640BxP3jT85fl5yvrdXG_PDJ0uFrCHqyfSsQg288YIdrpZ8DSEhnhsEiwcT4QX5NpADApHUghBNAb-Fcu57BU8zFGox8AcOonDtH1oLFBlt37hDQZdYOOIU0XyxrV9eeLNO4SbujrcaIgLKVVzHSd8PCAjq0_MCkuznXhBwOl67jVLsWDfaRdrs5gKBWzag7dh5Dik532ktKPN4W7CN9T10xzmNVs1AOnCbIJu3WyJGd6cUPgL-kDefQRuwE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e2ddef2586.mp4?token=WlBpep2fJJCInpoPgm3pgw1EoAJtK-YSMY6S6-NQViJkOJJ8ZCdS7KtPOi2eevVCVxYpej9bwLw4XpPff7dMP9MffgniF0kI4iXwP5hW7r7UO8-wecWBopqr34tSNtgtmK4lpgJOMd1xhnFWUYyTjtF4EFEPBGNxzo3yfYuE9yyIQuTY_zmkz9mJJGbukaQW58s4yq7jXfHqIS-NDfKEMcxfK0JBMZCZmhPaqBk3SKaw2oQjL7BJ0f9RSqh67OkOitLFlNfFZWoH2eXgExTbHa_qNXDfK8_ebTZDyGrAlCD8yzx4_1tzaLmJUWHI4V2sccfaJ36ChtrqlElvjxwD7KO9bXoN-yRTpw66pdcQLGLZ4CKj8c2eCLhTObMv6xNoQCjYrYNC_uRoPPhGouwWoJKSaR8lONb7y5TwKHuOyrDgXT4640BxP3jT85fl5yvrdXG_PDJ0uFrCHqyfSsQg288YIdrpZ8DSEhnhsEiwcT4QX5NpADApHUghBNAb-Fcu57BU8zFGox8AcOonDtH1oLFBlt37hDQZdYOOIU0XyxrV9eeLNO4SbujrcaIgLKVVzHSd8PCAjq0_MCkuznXhBwOl67jVLsWDfaRdrs5gKBWzag7dh5Dik532ktKPN4W7CN9T10xzmNVs1AOnCbIJu3WyJGd6cUPgL-kDefQRuwE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سخنگوی سپاه: انتصابات جدید رهبر انقلاب نقطه‌قوت نیروهای مسلح خواهد بود
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/akhbarefori/680357" target="_blank">📅 19:48 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680356">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">♦️
وال استریت‌ژورنال: کشورهای خلیج فارس به کنترل ایران بر تنگه هرمز تن داده‌اند
🔹
روزنامه وال‌استریت‌ژورنال گزارش داده تولیدکنندگان انرژی در خلیج فارس به این نتیجه رسیده‌اند که کنترل ایران بر تنگه هرمز ممکن است دائمی شود و این می‌تواند صادرات نفت و گاز آنها و عرضه انرژی در جهان را برای مدت نامعلومی مختل کند.
🔹
به نوشته این روزنامه کشورهای عربی حاشیه خلیج فارس نگران هستند گزینه جایگزین یعنی بازگشت به جنگ، پیامدهای بسیار بدتری داشته باشد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/akhbarefori/680356" target="_blank">📅 19:46 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680355">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">♦️
سی‌ان‌ان: کاهش ذخایر موشک‌های رهگیر آمریکا، نگرانی تازه کشورهای عربی خلیج فارس شده است؛ آنها نگران‌اند در صورت تشدید جنگ با ایران، توان پدافندی آمریکا برای مقابله با حملات احتمالی کاهش یابد
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/akhbarefori/680355" target="_blank">📅 19:42 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680354">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2e210c6ba5.mp4?token=rFEScVU-d7DJ_wbkU3-Y-QOZ-5fjO80WBIYn-rkNT3b-NKm8qRIdaQNTYG7N89q7iP61tM1BKEyXHownKdkQkw5jH9wYfWupdK0fx_PdnRv7CNLR00ZF3QsKnpcXmRMDY6wwemQDWalKjfcn6MbhoadbnVvfDIogdGnMV6lPwOCDafi5csY57ocveaqvtY3AlY7MwVT4uN6Dkp0CknemeoGTy1yey7s9dTrkAqcSCtGDo-5cKIIqXE8DiHJjQOBrkVnuBqiPPqXuzzEHmAX0vy0yLM-ledQfwaBdIQSWSZrpz5BvgpQndGQNjFdiH6TdV0jKJNGxkBsPk6Q6u4ep86ektu9nPYSoKcE8nd6hyv_O0gZ8wFqTkNqMnK-pv63wxSWIJ9ABzPGilbW6L_MjW-t_W8gmKXa9cpCx3xSG4_hUdqm_MXCsOLEtM09P4lm9cQtzgp3GWgiMw7NVu9ZWVK0Vpmj_M3CO2sbejOG0QY3x1x9aC7jy_oz6tAjFmC-CBnV-6EIKK4X1WFYfLIZfk2cPomEVjeJw2hPoIhegsPcSf1D2Ro7t30irWHsxFeVIjabpl9D-AK9NILCFdbIzG3M8makyXZxLqWFzXeWMlaKObmRvhLJRd2MhRu6x-LVMpD6PQihjEiOM_dXEtrYAAacxX3vitwrnqTy9xAOQEwQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2e210c6ba5.mp4?token=rFEScVU-d7DJ_wbkU3-Y-QOZ-5fjO80WBIYn-rkNT3b-NKm8qRIdaQNTYG7N89q7iP61tM1BKEyXHownKdkQkw5jH9wYfWupdK0fx_PdnRv7CNLR00ZF3QsKnpcXmRMDY6wwemQDWalKjfcn6MbhoadbnVvfDIogdGnMV6lPwOCDafi5csY57ocveaqvtY3AlY7MwVT4uN6Dkp0CknemeoGTy1yey7s9dTrkAqcSCtGDo-5cKIIqXE8DiHJjQOBrkVnuBqiPPqXuzzEHmAX0vy0yLM-ledQfwaBdIQSWSZrpz5BvgpQndGQNjFdiH6TdV0jKJNGxkBsPk6Q6u4ep86ektu9nPYSoKcE8nd6hyv_O0gZ8wFqTkNqMnK-pv63wxSWIJ9ABzPGilbW6L_MjW-t_W8gmKXa9cpCx3xSG4_hUdqm_MXCsOLEtM09P4lm9cQtzgp3GWgiMw7NVu9ZWVK0Vpmj_M3CO2sbejOG0QY3x1x9aC7jy_oz6tAjFmC-CBnV-6EIKK4X1WFYfLIZfk2cPomEVjeJw2hPoIhegsPcSf1D2Ro7t30irWHsxFeVIjabpl9D-AK9NILCFdbIzG3M8makyXZxLqWFzXeWMlaKObmRvhLJRd2MhRu6x-LVMpD6PQihjEiOM_dXEtrYAAacxX3vitwrnqTy9xAOQEwQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
رییس کمیسیون عمران مجلس: مالک ۳۰ تا ۳۵ درصد خانه‌های خالی در کشور، بانک‌ها هستند
محمدرضا رضایی کوچی، رییس کمیسیون عمران مجلس در
#گفتگو
با خبرفوری:
🔹
نزدیک به دو میلیون مسکن مهر ساختیم که ۱۰ تا ۱۵ درصد آن، جانمایی‌ها اشتباه بوده است.
🔹
۱۰۰ هزار واحد مسکن مهر هنوز مانده و ساخته نشده است. پول از مردم گرفته‌ایم اما نرفتیم که تکمیل کنیم.
#فوکوس
@Tv_Fori</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/akhbarefori/680354" target="_blank">📅 19:33 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680353">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">♦️
سخنگوی سپاه: خلیج فارس خالی از شناورهای جنگی آمریکا است
🔹
سردار محبی با اعلام خروج کامل شناورهای جنگی آمریکا از خلیج فارس، هشدار داد در صورت تهدید دوباره علیه ایران، تمامی زیرساخت‌های آمریکا، خطوط انتقال انرژی و سیستم‌های جهانی متصل به اینترنت هدف قرار خواهند گرفت.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/akhbarefori/680353" target="_blank">📅 19:29 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680352">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MTtI6B607ew9_HokvEoAbTGszpjEtGmA4lEdA2ih2L8cUBusphPCsE3HocrkFkPpA1e7uA04v2ihgmp87q29uLxsL2uyH25hEIYFjju1P2jSjCC_Pl5DZ89i_3Fyi4FrLlymxVPsYVfLVYhjbC7YBcnxKKi2ZQhDl9ATs9HeEO66ZVWt6iMhcIh3X1OORJIFJ2lRMIuo38UwaU9FfH3n_KZiuqbxgpG20sL-Jv038OCpeSxm-JwpW1yktqa42sq2pPoH8gtftjdo2fMUIyyW8gLNRYv-x7oJD8qUuFONhhKHGiXSvvMW_x2mxu6ztPyWViu6sMywm-SzTS_Wob57YA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
لحظه فرار ترامپ با کامیون آشغال
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/akhbarefori/680352" target="_blank">📅 19:23 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680351">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SxZh0cngvFLgHVlD_bUYjxD7mu8NT6Csgk_H_dqRMan72t7c2G5V-cv9Axr_Jk99Z4zoEneRj54o6qwbyds8v7bFoDSB0u1SG3Tj7UI6EDOOibXIHVO6jfQP8nvjhpP4yhwlKCE15o0a1xeGHkbgaWGG5GGvjN3sboOKvPGYDbLrlUECRvMptVew9txWx7XpquoL-BT8b5MAXY5bLCu5czm1WIRF1eM2NGc3klB4qoaxz1tPddZfOSjOI4MlNLzJgamToP2-DFQ2GNXcF8OG0rZSHatt5Mz98iXiW4bbNCTDPnl_oK5nN7Z0BGQ2aLkLQJ34gfuTw7otkg3ymWi0qA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سالى سرشار از ركوردشكنى در گروه فولاد مبارکه
🔹
تداوم مسير رشد، بهره‌وری و تعالى توليد در گروه فولاد مبارکه با ثبت ۹۲ رکورد در حلقه های مختلف زنجیره تولید
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/akhbarefori/680351" target="_blank">📅 19:22 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680350">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">♦️
وقوع انفجار در یک پالایشگاه در شمال غرب لیبی
الجزیره:
🔹
این انفجار مهیب در داخل انبارهای پالایشگاه «الزاویه» صورت گرفته است و هنوز علت انفجار مشخص نیست.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/akhbarefori/680350" target="_blank">📅 19:21 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680349">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1d4c76a182.mp4?token=G1a7Y9R82T1hSqTXXfIrR17lGS_zX0ckPBrzYGKsrOzH1xNHx5SaeSs8UnGyzwyJkno3Cu-A-KFQte7fAdjdTlE7nDwL-7urr0szNQ_jb6ftA0k1cM08ublc2EXXGYOnN59vVohq__oKl32spyEKw8qGMfHThXEso9qXbGSqnbAHc4BXn4K14_ReoXasI2rg7aCraWal_WJ8iB4IT1viYSxHZVhy2yTzd8zdVRklr3V_lrW3ybDAwyzKOWFa3L0mirWhjtGQ91fSp1p8vtzKwSp-FTUL0bjCsmUGj9vwXiG6Rfa67ceBKRllHeD01DnLn_7F9yRwGrxs6xgCq7Nggg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1d4c76a182.mp4?token=G1a7Y9R82T1hSqTXXfIrR17lGS_zX0ckPBrzYGKsrOzH1xNHx5SaeSs8UnGyzwyJkno3Cu-A-KFQte7fAdjdTlE7nDwL-7urr0szNQ_jb6ftA0k1cM08ublc2EXXGYOnN59vVohq__oKl32spyEKw8qGMfHThXEso9qXbGSqnbAHc4BXn4K14_ReoXasI2rg7aCraWal_WJ8iB4IT1viYSxHZVhy2yTzd8zdVRklr3V_lrW3ybDAwyzKOWFa3L0mirWhjtGQ91fSp1p8vtzKwSp-FTUL0bjCsmUGj9vwXiG6Rfa67ceBKRllHeD01DnLn_7F9yRwGrxs6xgCq7Nggg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
رکوردشکنی تاریخی بیرانوند با ۹ مدال طلا
🔹
محمدجواد بیرانوند در مسابقات وزنه‌برداری آسیا و آسیای میانه با کسب ۹ مدال طلا، ضمن شکستن رکورد نوجوانان آسیا، رکورد جهانی دسته ۷۵ کیلوگرم را نیز ارتقا داد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/akhbarefori/680349" target="_blank">📅 19:20 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680348">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">♦️
محسن رضایی: شرط بازگشایی تنگه هرمز، پایان جنگ و آزادسازی پول‌های ایران است
🔹
محسن رضایی، دبیر شورای عالی امنیت ملی در دیدار با سفیر چین، ضمن تقدیر از مواضع پکن در شورای امنیت، آمریکا را عامل اصلی ناامنی در منطقه دانست.
🔹
وی تأکید کرد تا زمانی که آمریکا شروط ایران از جمله پایان جنگ (در غزه، لبنان و ایران) و آزادسازی پول‌های مسدود شده را نپذیرد، تنگه هرمز همچنان بسته خواهد ماند.
🔹
او همچنین افزود که توافق احتمالی با عمان برای عبور و مرور، موضوعی جدا از انسداد کلی تنگه است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/akhbarefori/680348" target="_blank">📅 19:10 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680347">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T-NfpXPaJnIA9EmJhdU3kMJQC4It6sBUd4gaw9bUxsKiq-b65wkB7v3hXi72gQ8bjLa7knWWbsw8KF_jJiaTNLr5UDHnMwHcvMoujb3O6StV5Xp4zDnCeRGUXN1D-BUw2aZDsnch5gGOgkBxwHMiusL2S3ZNVdKEa-0iTlIzwB8KTlE6ZuP8AVB08aVyySC3_b3HvTW2gsZ0bAZGwZhUUflpG9MchlIK2Bbae_g1m_0Z6G8tECzhkDuRw4TAYE46GAvmShXwGW0-F5DIwOqCZHt9dCBHKVU8BrZ36L5q3uIBMw-ubPdiBGfSunB8btEz6m9gX-OiIUp7zhu6lgZpTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
لحظه فرار ترامپ با کامیون آشغال
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/akhbarefori/680347" target="_blank">📅 19:10 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680346">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromروزنامه دیجیتال خبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Erl25SZBltbKvgpqhBfxzoTLqRFL92ZNy0lMOljTfBOcRbgnfGfim8FKiJ95HBlSkCyZb6t90Rgjr1_REi2UwMgIBiWX4VgBjMjtqO--jQ6XBg8S94nRIDcTBjp_LzG1YbGjb52zkv7_FYCzpKcWSdMV1Z4Sr-mGFZs2GEIxAWpcFbUgrG-YdJP0zWOezOdbUop-fQkXetRgRSSs8WDuHYYxAcOU5zbo-pxAWM9YXbkQ7oiSXbXSHWlzePVhyeiql6nKGZjV1CgbpWz_mWp7WaSILHmp7SDwlaSnNxBiqvlqWglTrChpbtpU9o5QKyFK9vYy9aGbgY7gycXd6EN1jg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
کالا بی‌برگ
🔹
اجرای طرح کالابرگ در برخی فروشگاه‌های بزرگ، به دلیل تأخیر و بدهی دولت به فروشندگان با اختلال مواجه شده است؛ مسئله‌ای که علاوه بر ایجاد نارضایتی در میان فروشندگان، دسترسی مردم به این طرح حمایتی را نیز تحت تأثیر قرار داده است. در شرایط اقتصادی کنونی، استمرار و نظم در اجرای کالابرگ اهمیت ویژه‌ای دارد و هرگونه وقفه می‌تواند اعتماد عمومی و همراهی شبکه توزیع را کاهش دهد.
🔹
هشتصدوسی‌‌وسومین شماره جلد یک خبرفوری
#تیتر_یک
@rozname_fori</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/akhbarefori/680346" target="_blank">📅 19:03 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680345">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g4nXPTqjr3ZTs8mo9aBGdWFQ1NpVOuGYzH-vajUfp8NKvWxhnMdAb2ge6k-YQ2iYcyhw-ZyMcXoshXWFGX1doke3Jwqn14DNaLMVpEPYDqt5JH74OB8MJtGGMZoCVo4RX5ltxC9I2jnTK9Rnipw92CrKrLD9inXBbCSLD5MvzRNcrcmM6IxuFseBIpFvDOWQVjdxg6K4o_4Tgtd2DFYdKfzVY8R_pKz5XceWaT2gevqgURTDQ9QnW_g_IPSe5hW_7ug6mBosxurzDHxbmGIq6-LZRx6_-346CPRPBTLel9KcKXUVlppxZiHFrW4sQjYfjP-9XOOWjEN5UbCUZAPjyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
مخبر، مشاور رهبر انقلاب:  تنگه هرمز باز نخواهد شد تا شرایط ایران محقق شود
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/akhbarefori/680345" target="_blank">📅 18:52 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680344">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">♦️
نتانیاهو کودک‌کش: جولان، سرزمین ماست و همیشه متعلق به اسرائیل خواهد بود
#Demon
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/akhbarefori/680344" target="_blank">📅 18:51 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680343">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MeS61uvL6VBTCuyw2InE-oF12oQDZXLw4N8ykdLk-PAt4JbcF96gAQm_c6WJqZpaH56T5lqPrc3JBMO4yxP4wPqEW-eX_3lx6hmyT9rXOCfPqHZB6Wxrsc7qEOAwmH0a84Qb3LabAeIMZTZpqPJqssN-yyUw0tQrd7aD-pY-tH-CuChENUwrXEQbIIdOLRdqul6CqSfXIz66gaqhOshC0M-4HEydaWr1b9W3WexvXjqb4dKzMJV8hAY2lDOhVRJlHuFn0n8PTtzAM56i0J4LP_4HD8GoPTpQo4tuW1cNk8n1Foheon7WYqerJ5hwb--5nG960YbMQJoJ5wl0Omv0Cg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تامی ویتور، مفسر سیاسی و سخنگوی سابق شورای امنیت ملی آمریکا: تصویری که در ذهن از ترامپ در حال پنهان شدن از ایران داخل یک چرخ‌دستی حمل غذا شکل می‌گیرد، ویرانگر است
🔹
پیرمردی ضعیف و احمق که از پیامدهای تصمیم خودش پنهان شده.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/akhbarefori/680343" target="_blank">📅 18:37 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680342">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AEiKQnEu3hAd1Upk7UOvmRbGcHDqfZdZLBnMVCTNAlLpIlJp8QBlsbUEbUe4PVn6ZE0TiXpG0ZWAINKqEcu8NEuJeVMEx3f2rDy4Sdeu78hbMP_p1LoFG15a6bkriGbZrRYzjgCtOlakhQkV1d1k0AlFcLM6tUtyVXwuBGbTy9Qu0_JfKu8sYl57CBd3eTJuKHuyI3CgvPLRSot3tLdWaik2hezGJNv-1CNhRij83VbcNOa8USlDNP8kfSIPmOikxCLLMFZNupgdvYqUAUmUCg1JKPOOD_x8ddwYXSqgERKm1BgUU0RmzqUrPe3YyRbiIjrcyOTdxsJsR2WmKtMymw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صندل مردانه نسکافه ای مدل Arman
جنس رویه : کوبا
جنس زیره : PU
کفی پرسی و دوردوزی شده
رنگبندی : نسکافه ای
سایز :41 الی 44
🔴
قیمت 1,358,000 تومان
✅
پرداخت درب منزل
ضمانت تعویض سه روزه کالا
خرید از سایت
👇
https://memarket24.ir/product/brief/46479/180124/</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/akhbarefori/680342" target="_blank">📅 18:36 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680341">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/122bee6636.mp4?token=r8PhJydjEmwKFn_YltZbrNvbv0RVxjUf_BMQJGqhJBUMVUAYT9BB7H6sCyr3CUUhMyCPuIytQVamJa1I_KFAN0Cn-PxyG9NIJ135-el7oXvQMfJVkkVcixfkYzhj5Q8LliT_bwolCe_TVXLoJb5RLPjRCuBjktYeoKhyGHOAkfrt--G6i0NB4dGa76TtkmoXZmINYWStPWaL13b56VG61KybJ63rKNv3TPU7MyNEyh37eubsd_KbZkgwZc6YyCjeVsDOjC-u_nFuph91eBkKk4regPsApukkV8EPgp3guyqWLjFtfO0mv5Pm0up8rXi4Xxs9W8j7lE_SETQyPtYaNg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/122bee6636.mp4?token=r8PhJydjEmwKFn_YltZbrNvbv0RVxjUf_BMQJGqhJBUMVUAYT9BB7H6sCyr3CUUhMyCPuIytQVamJa1I_KFAN0Cn-PxyG9NIJ135-el7oXvQMfJVkkVcixfkYzhj5Q8LliT_bwolCe_TVXLoJb5RLPjRCuBjktYeoKhyGHOAkfrt--G6i0NB4dGa76TtkmoXZmINYWStPWaL13b56VG61KybJ63rKNv3TPU7MyNEyh37eubsd_KbZkgwZc6YyCjeVsDOjC-u_nFuph91eBkKk4regPsApukkV8EPgp3guyqWLjFtfO0mv5Pm0up8rXi4Xxs9W8j7lE_SETQyPtYaNg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حمله موشکی به گروهک تروریستی کومله در اربیل
گروهک تروریستی کومله:
🔹
مقرهایش در درهٔ «آلانه» در اطراف استان اربیل هدف حمله سه موشک قرار گرفته است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/akhbarefori/680341" target="_blank">📅 18:31 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680340">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gUq-Pib6gmX_f7D8hxa8evDPopUsrnfqXRGzLz4AqHUDR1azTqomkeBwJMKVG6e_yVwEsdAJoWI6pu3luLsr2aX_Hw0JC9M12_GNtgVVEXnMT-bu7MCDPeDIT7EDtzERaRH2qro05rVxxEDJFtsWdlPzVwq1zxOrenvEedcMRMXvI2IH57md6m5HwArnTUPJayPTsgaoYopMv-8Wi0zmf6rjRbWb8Wt9IrzCm0ssgGgnvnmxyC9rnrgluPrZDX4A8EUtDLxJdOgYO4bsH8urUgIcwyvylItb-mbXlar5E5GLCsnmB2vtfgc34V-FWiOC7bxrnWehNlDdfbtwxIvSCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
رسانه DD Geopolitics: دست از آزمایش نیروهای مسلح یمن بردارید، آن‌ها قبلاً نیروی دریایی ایالات متحده را شکست داده‌اند
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/akhbarefori/680340" target="_blank">📅 18:23 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680339">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">♦️
ترامپ کمبود مهمات آمریکا را گردن بایدن انداخت ترامپ شیاد: بایدن با ارسال مهمات به اوکراین، ذخایر آمریکا را کاهش داد #Devil
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/akhbarefori/680339" target="_blank">📅 18:18 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680337">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mBRz_QHzJuepHc-Wd0EVLQkp2fHp9L3y0-QB_8yzn0XvhMpM-SqqJMdnNiiRyQYX8OBJ-Ykt1gtUV0aJuM2JQFxMFFpBNp_qhmoHp0y59qvCnrL3iD0zQXdACPHQOPeqxf_eG1ZkHS8TT_kHJEmppWfAKURzHqV17j8M2Tw8n1sjFvJeV4l-4lxG1ZE6uHWWWnFCihnpPOCWtfgm4V_SMJFu76Vl7lukcZ3HO6oBupcBGrsqS35LjT2XEynEl31MHQvmdPzBVBBXxG1oNUvsUN4rWnOZs42gZbs2MRw193tc1_3SC31HPqJx77MeriVwtZButChqlve-z6iH438MyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
مرکز تحلیل اجتماعی (متا) در یک نظرسنجی ملی، از ایرانیان درباره قیمت واقعی بنزین ارائه شده توسط دولت، پرسیده است
🔹
طبق نتایج این نظرسنجی،
۴۲٪ از مردم معتقدند دولت بنزین را ارزان‌تر از قیمت تمام شده برای خودش به مردم می‌فروشد
و به نحوی از این طریق
به مردم یارانه می‌دهد.
🔹
همچنین،
۳۴
٪ از مردم بر این باورند ایرانیان
بیشتر از نیازشان
بنزین مصرف می‌کنند.
@metaacenter</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/akhbarefori/680337" target="_blank">📅 18:13 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680336">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">♦️
درگیری و شورش در ناو هواپیمابر «آبراهام لینکلن»
🔹
در پی اعتراض خدمه ناو هواپیمابر «آبراهام لینکلن» به وضعیت معیشتی و شرایط دشوار پس از ۳۵۹ روز مأموریت، درگیری شدیدی میان نیروهای این ناو رخ داد. بر اساس این گزارش، در این درگیری با سلاح سرد، ۷ نفر کشته و تعدادی مجروح شده‌اند.
🔹
خدمه ناو به مواردی همچون کمبود شدید مواد غذایی، وضعیت بهداشتی نامناسب و عدم پاسخگویی فرماندهی «سنتکام» معترض بودند. این گزارش همچنین به حادثه مشابهی در ناو «جرالد فورد» در اسفندماه ۱۴۰۴ اشاره می‌کند که منجر به عقب‌نشینی آن ناو برای تعمیرات شده بود./ تسنیم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/akhbarefori/680336" target="_blank">📅 18:10 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680335">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qbJ6S8kfjHTRKtfVJguEtc2V4TnAGZL6PiIuNuYWUfOYQQD_sDG3_xGcJySRCBQTcoTK054P7VzjbdiUDVvIbMf2oSncsDPqnGwYFlRLfY6IMyO1IIIEwdE9s02c615ZcY6KQhDtWmUCw-77DKvAm3hKEkNtoTUlsEviNvu__FlNDPbUxN9H0powePb85iyWTwn_0mITGbA0mv3h3r1dpUtFRpYdos7nSL103xasmx0xYFPXWQ3yF11cp8ZuVv-XMka9QdtC5WmTxL5KSoww4wF2CMhKHUCyB58hLMBLoYlSMJQSfP_KjevnkSIVE7XobfCPICDjoMKmpHbvXWWt9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
شاعری که زبان شعر معاصر ایران را دگرگون کرد؛ احمد شاملو
🔹
احمد شاملو، شاعر، نویسنده، مترجم و پژوهشگر برجسته ایرانی، از مهم‌ترین چهره‌های شعر معاصر فارسی بود. او با زبانی تازه، آزاد و انسانی، شعر را از قالب‌های سنتی دور کرد و آثاری ماندگار درباره عشق، آزادی،…</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/akhbarefori/680335" target="_blank">📅 18:00 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680334">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bIZcdbRfenGvI9exHMG9D84i0lwFv2ipKxzN6gUIau9Cy2z3VB8MWlYpTgn1bYJenaE-OgF2kfO1xjYJyiI1XlRVZiws63X5ybSwVF75-oZVBr1OO-zyrT77Hf9edDAQJYL9OYzjKeiIjnG5U_Mfik1VP9t_XeoKaqO6n9I7aCfRDHa45pyrRZOIUO0h6kLr2DHD73Z6nw5gdIS-pyeA2-EEAjnceCrmiPLvLQZx7NP1pgQ7saR3ceEQkZnogn-Pz0i0CYU6tJ5QVKGmtCBam5w13qI3VAEDWQYISUz_PhJ2O-JlpqfwgsfH6K9y0VJFKNL3WuwXjHDc1qtC3foy-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سرانه مصرف چای در کشورهای مختلف جهان
🔸
بر اساس آمارهای جهانی، سریلانکا با مصرف چشمگیر ۵۰.۱۷ کیلوگرم چای به ازای هر نفر در سال، در صدر جدول کشورهای جهان قرار دارد.
🔸
این در حالی است که بزرگ‌ترین تولیدکنندگان چای دنیا، یعنی چین و هند، به ترتیب با ۱۰.۱۹ و ۴.۲۱ کیلوگرم سرانه مصرف در رتبه‌های بعدی جای گرفته‌اند.
🔸
ایران نیز با سرانه مصرف ۱.۶۹ کیلوگرم برای هر نفر در سال، در رتبه ۳۰ جهان قرار دارد. ایران با تولید سالانه ۸۳ هزار تن چای، هفدهمین تولیدکننده بزرگ چای نیز در جهان محسوب می‌شود.
📊
آمارفکت | مرجع تخصصی آمار کشور
@amarfact</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/akhbarefori/680334" target="_blank">📅 17:57 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680333">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">♦️
دیدار وزیر کشور پاکستان با وزیر امور خارجه
🔹
سید محسن نقوی وزیر کشور پاکستان عصر امروز سه شنبه با سید عباس عراقچی وزیر امور خارجه دیدار و گفتگو کرد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/akhbarefori/680333" target="_blank">📅 17:52 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680331">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">♦️
حمله بالگرد آمریکایی به یک کشتی با پرچم پاناما در تنگه هرمز  روزنامه وال استریت ژورنال:
🔹
نیروهای آمریکایی با استفاده از یک بالگرد به سمت کشتی «ویلا نوا» با پرچم پاناما در تنگه هرمز حمله کردند.
🔹
گزارش شده است که همه ۱۷ نفر از خدمه کشتی سالم هستند.
📲
🇮🇷
✊
…</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/akhbarefori/680331" target="_blank">📅 17:41 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680330">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
رییس کمیسیون عمران مجلس: شهید لاریجانی می‌گفت این قدر به حضرت آقا ارادت دارم که اگر حتی حس کنم حضرت آقا موضوعی را دوست ندارند انجام نمی‌دهم
محمدرضا رضایی کوچی، رییس کمیسیون عمران مجلس در
#گفتگو
با خبرفوری:
🔹
شهید لاریجانی باهوش بود و به مسائل کشور مسلط بود. آقای لاریجانی مظلومانه شهید شد. در شرایط جنگ باید به طبل اختلاف نزنید و روی اشتراکات متمرکز شویم.
🔹
شاید برخی آقایان به آقای قالیباف نقد و ایراد وارد کنند، در عین حال حتما در خیلی موضوعات با ایشان هم نظر هستند. روی اهدافی که در جهت نابودی دشمن است، متمرکز شویم در غیر این صورت یعنی دشمن را تقویت می‌کنیم.
#فوکوس
@Tv_Fori</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/akhbarefori/680330" target="_blank">📅 17:35 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680329">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BMbNW2pGGDx2iU-RUR3VT1LfTdv7Hxzr5w0ztBDiegdZBJ5ulkdA51zNPFzLQ_OWXZKEiSNGMyI8NmjSdfvItbOXQhC8RtCUgg9sjJBx_0ZfoqL1yBs9CILcbxBS-o1hKFNODdb0SWTS2MR5V-_bHKOFtskqSrbPtBpaIC54APwrLqOTo6DJvwi4z6KPS4-4_dYNeLU8rbQNEwvqlYwKqZ4mfr--Pw0Id_vQiSWykcIVuHpe4Q05TCXYjrZep7eH3v9fo0qzfWfxeb8KwOBXNLBNCAi9GW0s894kuA42o7lKKayvwppE9ie-0JUAXUNgwfL4_ToEDMpplXOcV5RXgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">"
⭐️
جاباما تور رسماً شروع به کار کرد
تازه ترین سرویس جاباما با هدف ارائه تورهای گروهی  و تجربه محور راه اندازی شد.
مزایای ویژه جاباما تور برای مسافران:
🔸
پرداخت اقساطی
: بدون نیاز به تسویه یک‌جا، هزینه‌های سفر خود را در چهار قسط بپردازید.
🔸
تضمین امنیت و کیفیت سفر
: همکاری با مجریان معتبر و دارای مجوز رسمی و همراهی تورلیدرهای مجرب.
🔸
کشف مقاصد خاص و بکر
: سفر به مناطق کمتر شناخته‌شده و شگفت‌انگیزی که تجربه آن‌ها تنها با تورهای تخصصی ممکن است.
🔸
شفافیت کامل قبل از خرید
: بررسی دقیق برنامه‌های سفر، جزئیات خدمات، قیمت‌ها و نظرات مسافران قبلی.
🔸
حمایت از جامعه محلی
: کمک مستقیم به رونق اقتصادی مردم بومی و کسب‌وکارهای محلی.
🏕
اطلاعات بیشتر و مشاهده تورها:
https://jabama.me/koP2PQV
📞
شماره تماس و پشتیبانی رزرو:
۰۲۱۴۹۲۷۵۱۱۱</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/akhbarefori/680329" target="_blank">📅 17:33 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680328">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LBKK5DRwa3RTE0R3H1FJNPcnu5-_vL0cxYnOLKfWSZaMeeSc1f-XeK3o7FIz_BP2BjqUxFkoQvrGEXHnDBVuXqXsSoT0snKc_AuH2YoL8HOD795SkcLYQTuZRvD8_7QaVSmbdhasMvpYzl7Gco4hQXO0KLClzXM__pG220ORoCXezHJyFAGihcuhHFFytb3m6QTwaMNrNo7cWMZIg_3rfEnexCN0y6pDowsFW25SfNdR3BNg_SvsMlgql-bS5N7L5j552Msk79lD4p_A7wtfxlf1RLuwkkbH_eJpcWznmY4_AZPymBD3m-xmY8gBxQXpDiIl1W-104CnJE7DWMJ_9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بازطراحی زیرساخت ارتباطی بزرگ‌ترین فولادساز کشور با فناوری 5G رایتل
🔹
#فولاد_مبارکه
و شرکت خدمات ارتباطی
#رایتل
با امضای تفاهم‌نامه همکاری فیمابین سعید زرندی و مهدی فقیهی مدیران عامل دو شرکت، مسیر تازه‌ای برای توسعه زیرساخت‌های ارتباطی، شتاب‌بخشی به تحول دیجیتال و حرکت به سمت
#صنعت_هوشمند
ترسیم کردند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/akhbarefori/680328" target="_blank">📅 17:31 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680327">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8d17e9789e.mp4?token=YEnnRRN23OsSdSvSEOpiiH_fllsgw2JcF6rfbUFA8gIlxJ2XRmaLIL5VGiE-5qyhZFbhJn7wGRWVkWvDdOxe8gRHp8yJB8ki-bDsqHxq2SOVn1HWi7PNw0HUftTfZkMPYMM5lR-oZxg6SDskLFVg19KqqfZxkZtkDtYy065ZDwpu00pvquXVnkP4qm8RrAdO8r1wAAvwnk2kct6dGjxyMQiCVi1qiZBPGCQIr2ZrbSCG-s8fcvo6LlNuPO9a3RVlcUPAQzMasrD3fm7PLZZRimsCYFVR9AAdUMrBDAeGeRxQbfA3C0JsZhjH6yrJbniB_nmM4xQhCUorlfWOu2MrRA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8d17e9789e.mp4?token=YEnnRRN23OsSdSvSEOpiiH_fllsgw2JcF6rfbUFA8gIlxJ2XRmaLIL5VGiE-5qyhZFbhJn7wGRWVkWvDdOxe8gRHp8yJB8ki-bDsqHxq2SOVn1HWi7PNw0HUftTfZkMPYMM5lR-oZxg6SDskLFVg19KqqfZxkZtkDtYy065ZDwpu00pvquXVnkP4qm8RrAdO8r1wAAvwnk2kct6dGjxyMQiCVi1qiZBPGCQIr2ZrbSCG-s8fcvo6LlNuPO9a3RVlcUPAQzMasrD3fm7PLZZRimsCYFVR9AAdUMrBDAeGeRxQbfA3C0JsZhjH6yrJbniB_nmM4xQhCUorlfWOu2MrRA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پرواز بمب‌افکن راهبردی چین با موشک اتمی
🔹
چین برای نخستین بار تصاویری از بمب‌افکن استراتژیک H-6N را که موشک بالستیک پرتاب‌شونده از هوا JL-1 با قابلیت اتمی را حمل می‌کند، منتشر کرده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/akhbarefori/680327" target="_blank">📅 17:30 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680326">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/13991f0b53.mp4?token=aHoQSXfMHRkSJ6CWlkhyAvcfajhTBMCikvdJZlU8XwBK0a8rhEwunTRucdowcHDixcj-AVH0-AMebRYeWLo22xcKUUK_wY11Fz-i9WgGCQ3mNwKvMPMlGr6wGNsFqXYmEfOxSUfI5sCZL0ISpP81BvYdG0D5Bo54dFI-Xj1pc93OfnfAMh29Pw0768S7SVvzSBfTcXNKm_JUYqoGOc_vVJsW_G2NgLc-lruBnPuV7fo1fODMenu4kydznACCgFk7NDh7R-qDYVFTo2RW-OOVAIKqxOvTStQ0aeJqwig-5xgW4yU6rStrsaz6qgQZLXPvXz9ZtzoeL6x-uYGiU8hNOQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/13991f0b53.mp4?token=aHoQSXfMHRkSJ6CWlkhyAvcfajhTBMCikvdJZlU8XwBK0a8rhEwunTRucdowcHDixcj-AVH0-AMebRYeWLo22xcKUUK_wY11Fz-i9WgGCQ3mNwKvMPMlGr6wGNsFqXYmEfOxSUfI5sCZL0ISpP81BvYdG0D5Bo54dFI-Xj1pc93OfnfAMh29Pw0768S7SVvzSBfTcXNKm_JUYqoGOc_vVJsW_G2NgLc-lruBnPuV7fo1fODMenu4kydznACCgFk7NDh7R-qDYVFTo2RW-OOVAIKqxOvTStQ0aeJqwig-5xgW4yU6rStrsaz6qgQZLXPvXz9ZtzoeL6x-uYGiU8hNOQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
صبح امروز |بارش برف قسمت‌هایی از آفریقای جنوبی را سفیدپوش کرد
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/akhbarefori/680326" target="_blank">📅 17:20 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680325">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c4ef73cdd3.mp4?token=AeSs7t-VwsFQMG9lVwe-VaC7AcGw11Xit-ZtQB10AmWpszhFz4F9h2OOouXvdPbfha-S0F6soHFxaj9KTfzz5aPUaNqrP0RH8oeHsA7Y6zdEoh5QEx0N4MQN6zbFc6PKH_rsqXNVKbvmUu9ssMlP6TqO-4LJFsojXdOXr8Huz9a3IJ-pp4YDUz5XWrce0gwTgaKjaNpkP89YjFP0uD6cjsHTV_8PMCxK4LqYfq6lu1g4Lz3COAQbRcxQW1hoVWzlXgQ5hO5NWzTWjJrunWhhqXegllrlWf15q3p3FOVUYkVuklBKbbVjLvxWGrfb_saPCBjlKuR0SmQBAqMnMfH8lA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c4ef73cdd3.mp4?token=AeSs7t-VwsFQMG9lVwe-VaC7AcGw11Xit-ZtQB10AmWpszhFz4F9h2OOouXvdPbfha-S0F6soHFxaj9KTfzz5aPUaNqrP0RH8oeHsA7Y6zdEoh5QEx0N4MQN6zbFc6PKH_rsqXNVKbvmUu9ssMlP6TqO-4LJFsojXdOXr8Huz9a3IJ-pp4YDUz5XWrce0gwTgaKjaNpkP89YjFP0uD6cjsHTV_8PMCxK4LqYfq6lu1g4Lz3COAQbRcxQW1hoVWzlXgQ5hO5NWzTWjJrunWhhqXegllrlWf15q3p3FOVUYkVuklBKbbVjLvxWGrfb_saPCBjlKuR0SmQBAqMnMfH8lA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ادعای جوادی حصار: دولت فیلترینگ را برداشته
رییس ستاد پزشکیان و فعال اصلاح طلب:
🔹
فیلترینگ رفع شده و تنها شبکه اینستاگرام فیلتر است!
🔹
من خط سفید ندارم ولی درخواست دارم به من بدهند، نیاز دارم. یک عده در این مملکت پزشکیان را هم سیاه کرده‌اند/ تلویزیون اینترنتی مدار
گفتگوی کامل را اینجا تماشا کنید
👇
https://www.aparat.com/v/inm2imu
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/akhbarefori/680325" target="_blank">📅 17:12 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680324">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6ff8b5055e.mp4?token=Duc277iTz2Dct9nW3vKbB_VK3LwLdt6fsvJ7CpmJfZoR0gcQuzGEjh8KgK9lHWepT3vtOelbcj6h_mgVll1kTMRe9zMOzJDpTf7d1cx85p4RRMrXWnT3-1pLW86zJoYjNDFGvHApZ-S1nwN1_xEalfuD-cZJhIfuv0iRjuI3J3PpTPTRjc6v202moVncTpi-hDYff749d_Z6WjJb4iwFqj1t__tC4uNuBgT9xY8DI5F9bWGWRGJlVXhv57qJ8K0KSI9hBarbWrkrel5fCpXDVVfshZkYPi6zSv9J2OWPY70jttfVxkgLOZ7jTdJaJPPlRQaeXsTTV59IG9SjFUsa-A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6ff8b5055e.mp4?token=Duc277iTz2Dct9nW3vKbB_VK3LwLdt6fsvJ7CpmJfZoR0gcQuzGEjh8KgK9lHWepT3vtOelbcj6h_mgVll1kTMRe9zMOzJDpTf7d1cx85p4RRMrXWnT3-1pLW86zJoYjNDFGvHApZ-S1nwN1_xEalfuD-cZJhIfuv0iRjuI3J3PpTPTRjc6v202moVncTpi-hDYff749d_Z6WjJb4iwFqj1t__tC4uNuBgT9xY8DI5F9bWGWRGJlVXhv57qJ8K0KSI9hBarbWrkrel5fCpXDVVfshZkYPi6zSv9J2OWPY70jttfVxkgLOZ7jTdJaJPPlRQaeXsTTV59IG9SjFUsa-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
زلزله ۷.۴ ریشتری در غرب کلمبیا تاکنون دست‌کم ۱۳۲ کشته و ۵۷۰ زخمی برجا گذاشته است
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/akhbarefori/680324" target="_blank">📅 17:08 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680323">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">♦️
حمله بالگرد آمریکایی به یک کشتی با پرچم پاناما در تنگه هرمز
روزنامه وال استریت ژورنال:
🔹
نیروهای آمریکایی با استفاده از یک بالگرد به سمت کشتی «ویلا نوا» با پرچم پاناما در تنگه هرمز حمله کردند.
🔹
گزارش شده است که همه ۱۷ نفر از خدمه کشتی سالم هستند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/akhbarefori/680323" target="_blank">📅 17:04 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680322">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromكانال اطلاع رساني بانك كشاورزي</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sD94v1CZ_m0sqBY3MkaosYQRQ0V9K79HGxJM2hnfWkNXPuV_PfR1oNStfr_6BSSKCsr0ndgcOQ-7as2LP0ZACpvKEONtdW7jBzEkg3h1e_rfjkhXHUtmgaLxeVJyzW0zMN4yJxw6zs9GoYVvsI1QO06aUF5vaG4ASeUviC3EGiiaViIKc4Vj3A7MuUU9-JPZwdfpm4YRI57FkQsiNKUA-8OmaKhYzHgnltxmXDd0Ngjv3ECA16gMZ1gS0XxbcIXQnaStC075EKH5MqQNClkMjNE1kTKUmwsFA3fI4gRWUHP1cWkGdzv26qMonN0Jsdap5f6Zcu6Z8JMlhh29QAeexg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
پای کار «خاک ایران»/۶
🔹
ثبت رکورد جدید در جذب منابع ارزان‌قیمت توسط بانک کشاورزی
🔻
همزمان با افزایش منابع بانک کشاورزی تا مرز هزار همت، سهم سپرده‌های ارزان‌قیمت در ترکیب سپرده‌های مردمی این بانک، با روندی صعودی از ۶۰.۵ درصد در تیر ۱۴۰۰ به ۷۰ درصد در تیر ۱۴۰۵ افزایش یافته که بیانگر ارتقای کیفیت منابع و تقویت ظرفیت تأمین مالی بخش‌های مولد است.
🔻
بهبود ترکیب منابع می‌تواند ظرفیت بانک کشاورزی را برای تأمین سرمایه در گردش فعالان بخش کشاورزی، دامپروری، طیور، شیلات و صنایع غذایی تقویت کند و این دستاورد در کنار افزایش منابع  تا مرز هزار همت، نشان می‌دهد این بانک همزمان با توسعه حجم منابع، به اصلاح ساختار و افزایش کیفیت آن‌ها نیز توجه داشته است.
🔗
مشروح خبر
🔶
🔶
🔶
@bank_keshavarzi</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/akhbarefori/680322" target="_blank">📅 17:04 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680320">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
محمد مخبر و محمد فروزنده جایگزین شهیدان لاریجانی و موسوی در هیأت عالی نظارت مجمع تشخیص شدند
.
🔹
مهلت ثبت‌نام آزمون‌های خارج از کشور علوم پزشکی تا ۲۴ مردادماه تمدید شد.
🔹
رئیس‌کل بانک مرکزی برای شرکت در اجلاس بریکس عازم هند شد.
🔹
پارلمان لبنان پیش‌نویس قانون مربوط به لغو مجازات اعدام را پس از اصلاحات تصویب کرد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.2K · <a href="https://t.me/akhbarefori/680320" target="_blank">📅 16:53 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680317">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">♦️
افزایش سقف وام برای زنان دهک‌های یک تا ۵
معاون امور زنان و خانواده ریاست جمهوری:
🔹
پیش از این با تلاشی که در دولت قبل انجام شده بود، برای زنانی که در دهک‌های یک تا پنج قرار داشتند، در صورتی که برای دریافت وام نیاز به ضامن داشتند اما توانایی پیدا کردن ضامن را نداشتند، ضمانت انجام می‌شد.
🔹
در هیئت دولت به تصویب رسید که سقف وام تا میزان سقفی که شورای عالی اشتغال هر سال تصویب می‌کند، افزایش پیدا کند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/akhbarefori/680317" target="_blank">📅 16:36 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680316">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e2bded3e4b.mp4?token=f3WQVLV5J1_wc4GT4dSsLMBjgDnjklOfTcayBCXSPAZt5RqihHGmcrrApxoiJfE4_3ylx8azW6NWLaqac5K6OhHLi8hAqB05K3BYol4zyIPfN8CPuo-FkQNihqpppE5n58WbUUGMeFpqmBHwQcymX2mo86rixfTKyN_kIj-GYIwy43TlSU_mKIflZt2yLRWsVDlqm-XynQVtf6YPCIe4lTVC2nxJC5tLdvOEOfbsL3GbrS7omu0q9z0rR-59WDLvlLYtKc2s39HsMbz23MWcFLuV4wioXS-Zv3BC-CNcT-pYjjWj-cyaNByl55VUGUzSnjl968rFzD2gxGprgYGKMg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e2bded3e4b.mp4?token=f3WQVLV5J1_wc4GT4dSsLMBjgDnjklOfTcayBCXSPAZt5RqihHGmcrrApxoiJfE4_3ylx8azW6NWLaqac5K6OhHLi8hAqB05K3BYol4zyIPfN8CPuo-FkQNihqpppE5n58WbUUGMeFpqmBHwQcymX2mo86rixfTKyN_kIj-GYIwy43TlSU_mKIflZt2yLRWsVDlqm-XynQVtf6YPCIe4lTVC2nxJC5tLdvOEOfbsL3GbrS7omu0q9z0rR-59WDLvlLYtKc2s39HsMbz23MWcFLuV4wioXS-Zv3BC-CNcT-pYjjWj-cyaNByl55VUGUzSnjl968rFzD2gxGprgYGKMg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
با گوش دادن به صدای ماشینت بدون مشکل از کجاست
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.2K · <a href="https://t.me/akhbarefori/680316" target="_blank">📅 16:34 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680315">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/35e04feca1.mp4?token=aRaGd_87BhtAN1xXb0mcW7jH6v5C5x241hmyQjryAiTMOKQzI7oBLiaGoHm2PrJ4W_4PbxxOlFOcBu5mIm8pb0xrk_zpBf4ddciF5WlcP_PaonJfmhVhawghm0NFQ7nAVYsDtwqS04wklC3oAz2rknjokqevTUXO9GlgVRPu19Sc6rpvFIj6OZgchIfKP6yrQ3B2Ieo_Vg21AF6FHo-SL3rWZ_qtmk5NwDGYQ95m2f_3dr3DEBXlz-KU6d2eqyxdgOIA9SZmq1z7q2zeBLxNxHAaNqTSSJ2wAkVI2biDtKXde7OC0kAGjXKkVAiCgW5H5xk7WKISi0XdLzJpGzKu5A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/35e04feca1.mp4?token=aRaGd_87BhtAN1xXb0mcW7jH6v5C5x241hmyQjryAiTMOKQzI7oBLiaGoHm2PrJ4W_4PbxxOlFOcBu5mIm8pb0xrk_zpBf4ddciF5WlcP_PaonJfmhVhawghm0NFQ7nAVYsDtwqS04wklC3oAz2rknjokqevTUXO9GlgVRPu19Sc6rpvFIj6OZgchIfKP6yrQ3B2Ieo_Vg21AF6FHo-SL3rWZ_qtmk5NwDGYQ95m2f_3dr3DEBXlz-KU6d2eqyxdgOIA9SZmq1z7q2zeBLxNxHAaNqTSSJ2wAkVI2biDtKXde7OC0kAGjXKkVAiCgW5H5xk7WKISi0XdLzJpGzKu5A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
کاروان موتوری خیبری‌ها در شب‌های جنگ دوازده روزه چگونه شکل گرفتند؟/ در یک شب ۶ موتور، به ۷۰۰ موتور که تبدیل شد
🔹
برنامه تلویزیونی «دچار» هر روز ساعت ۱۸:۴۵ از شبکه نسیم پخش می‌شود.</div>
<div class="tg-footer">👁️ 33.3K · <a href="https://t.me/akhbarefori/680315" target="_blank">📅 16:32 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680314">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mVUhsUp2UId7R_8cVz-udXay3mpiSiUnzL5KbXWP-z84XXpCNpoR7t95rN05c5TX6m_WeP919X2UY4bnIW18nA4oG9mreWk0xLSXY58eV8HF4maqnWvFhVmCDQCZpv6TzJRbsgKynwqf2I5E6_eI7lWvxiBY7Qk7y2UvIWBlyU-wbaq0qQIbcPM9xZR0ri8q1wsnq9ejtJMwxOqtDbPz5OIvp8UdRIvDgEYbv298MyBsD9lCjjGd02CqaoIyA30dhXOKsF5XjM-I9aa6fD9oVmjlkf34R7GpIg2f2SMa1WcF9k9GAg1P66-Psxc1cIGVNIoFKD-asAn40s1SG1TgPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
معاون وزیر کار: نقص اطلاعات فراجا، کالابرگ برخی افراد را قطع کرد
🔹
پیگیری‌ها از وزارت رفاه نشان می‌دهد کالابرگ برخی افراد حاضر در کشور به‌‌دلیل ثبت‌نشدن اطلاعات ورود در سامانه فراجا متوقف شده و وزارت رفاه پیگیر اصلاح این اطلاعات است.
🔹
افرادی که صرفاً به عراق سفر کرده‌اند و پس‌از آن به کشور بازگشته‌اند و به کشور دیگری سفر نکرده‌اند، اطلاعات لازم از سوی فراجا ارائه می‌شود تا از فهرست افراد مشکوک به اقامت خارج از کشور خارج شوند و کالابرگ آنها مجدداً برقرار شود./ فارس
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 34K · <a href="https://t.me/akhbarefori/680314" target="_blank">📅 16:27 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680312">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e4fc4927ea.mp4?token=tcW2i2gbyGTd-hW2udDuO8Cc6HKuhhyXUqFEnsACH07Ru80ZChsWuOhQ1hlcLORlBbtZpc27yOOkH05xcZlLl9WFfY5Y7i-j8IZJN-Kd1CKWhMyZ1giGRvcvrt6qUyc-4ENqaJBB3OcXFMPcIwtNqrL8qUyI_k8gJLcceoxfqY9mXvkR4VtGDajfp9Gv4qcVnqXOUae09q7ESwLhT286SSkExVKQkZczf8atgztqGspxaZfJWgYmv4Skl2Vv_3AEo5muDMKYSUBnKy-ghgi_n6uKHs8L5d5Ksg4Ajan-1bJ1hgJ9J2-7nB0Npi12GG19g654ygJcGBvOVYA4DVatvhORZfLrakb0LDkI2x6pXzAS8vIpGkyirHRNNNa_iSiJmTHTL9X33yFKYMmEON9xOn49qybQrbr-31U8BBUEnHyKrm4lo_NOCGJL6UPy5PP4oaoO1TNzwZkPNWd7jgXUcyXbifiraROuqnZ5EPQ-NcpiUM1ieTs_lpzywnWmfEPkoR6ewKqEHKFQDCb3IS5U6dKO5Mox3aOLKanM1ZWGRG4XcUsFJEGMOxSHu_KaCmPA6UCpEJgnlZpHcEPopDnh5BFv6MOWDSnokr-YyZkae9x_cjOlQK0u2atCCOGVs4qRgOJRWoRCSnjdEj0X0eu4JQAEgGkL-y5SJxKH2A3xBpM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e4fc4927ea.mp4?token=tcW2i2gbyGTd-hW2udDuO8Cc6HKuhhyXUqFEnsACH07Ru80ZChsWuOhQ1hlcLORlBbtZpc27yOOkH05xcZlLl9WFfY5Y7i-j8IZJN-Kd1CKWhMyZ1giGRvcvrt6qUyc-4ENqaJBB3OcXFMPcIwtNqrL8qUyI_k8gJLcceoxfqY9mXvkR4VtGDajfp9Gv4qcVnqXOUae09q7ESwLhT286SSkExVKQkZczf8atgztqGspxaZfJWgYmv4Skl2Vv_3AEo5muDMKYSUBnKy-ghgi_n6uKHs8L5d5Ksg4Ajan-1bJ1hgJ9J2-7nB0Npi12GG19g654ygJcGBvOVYA4DVatvhORZfLrakb0LDkI2x6pXzAS8vIpGkyirHRNNNa_iSiJmTHTL9X33yFKYMmEON9xOn49qybQrbr-31U8BBUEnHyKrm4lo_NOCGJL6UPy5PP4oaoO1TNzwZkPNWd7jgXUcyXbifiraROuqnZ5EPQ-NcpiUM1ieTs_lpzywnWmfEPkoR6ewKqEHKFQDCb3IS5U6dKO5Mox3aOLKanM1ZWGRG4XcUsFJEGMOxSHu_KaCmPA6UCpEJgnlZpHcEPopDnh5BFv6MOWDSnokr-YyZkae9x_cjOlQK0u2atCCOGVs4qRgOJRWoRCSnjdEj0X0eu4JQAEgGkL-y5SJxKH2A3xBpM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
رییس کمیسیون عمران مجلس: مسئول بی‌کفایتی داریم که در زمان جنگ به وظایف خودش عمل نکرد و در زمان مناسب خودش رسیدگی می‌کنیم
محمدرضا رضایی کوچی، رییس کمیسیون عمران مجلس در
#گفتگو
با خبرفوری:
🔹
در کشور فرهنگ استعفا نداریم. همچنین ندیدم کسی عذرخواهی کند. خیلی ها وابسته به میز و صندلی هستند و طرف با اینکه می‌داند مقصر است، اما حاضر نیست از مردم عذرخواهی کند.
🔹
در کشور مسئولانی داریم که همه شب‌ها در یکجا نخوابیده‌‌اند؛ نه از روی ترس بلکه برای اینکه باشند تا به ملت خدمت کنند.
#فوکوس
@Tv_Fori</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/akhbarefori/680312" target="_blank">📅 16:15 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680311">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dF3pFLSVdDBRPHCZwiJxsmoQoFPpt-sL0vxKlqlfyro4Zv7fdX-18U6sMiRArliNb_vAP43wZEMRTzmIQhX2WFP3zQr6BGD07fRRR6YlWr0IVpUd7nF__NSwwAWUNKRLHesfJrhFBh7rJNIatkpdIDi4We8xEUaoqFzxgyExQlsiC_JNdBABmgNpr_RVpmk8QRIyg5M9aZJfX1U9vL_SDtK1RliN_1XDT8iZp9ak0SXba8Gypy3mWLQr3DKap48rPrOzl4FhSwRFEwtlZZsu78o0MKRcIzOHZhm4zMy-6k0fpgFh5fsJSqnYcPDzALd1IjsNod7Go8w4logWUcrmIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
محسن رضایی: ایران در برابر هیچ تهدیدی از حقوق خود عقب نشینی نمی‌کند
دبیر شورای عالی امنیت ملی ایران:
🔹
جمهوری اسلامی ایران در برابر هیچ تهدیدی از حقوق و منافع ملت خود عقب‌نشینی نخواهد کرد.
🔹
در همین راستا تصمیمات در این حوزه باید قوی‌تر از گذشته با شناخت دقیق صحنه و با تدبیر و شجاعت اتخاذ شود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/akhbarefori/680311" target="_blank">📅 16:08 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680309">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ef4b3e15c2.mp4?token=MdxKuXuIkgPugAcWpb-7zSsbBaUOZZpbAFvOTVTGCJGrHFQdekav7CAr1AvG93lirGhnZX45U_5U_dnixERHK9vyOLdrjxXVtcjCFHdcYviR_4X7T2vQRdr0YD2uNRhcHsHw96FTx51rQhb5HN4mCUU22Q48XmaPCPAkMQSwjeQRHOJ92sJ0drgVYK7EuWe6UX0J10YQC1BK--0cDHzSSDFbyMmsljQi1iyHyXR5SLu_bBs6oOEFCtFlVAzh7LSYeemIdUZbLV2yiMGH-i_lD6ZKLB7rsfRgEXO1kjbhWe2WxGNaBijGYfsE-yrgY5Tll1wVAFnH3Z9OYqgr5qSB8g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ef4b3e15c2.mp4?token=MdxKuXuIkgPugAcWpb-7zSsbBaUOZZpbAFvOTVTGCJGrHFQdekav7CAr1AvG93lirGhnZX45U_5U_dnixERHK9vyOLdrjxXVtcjCFHdcYviR_4X7T2vQRdr0YD2uNRhcHsHw96FTx51rQhb5HN4mCUU22Q48XmaPCPAkMQSwjeQRHOJ92sJ0drgVYK7EuWe6UX0J10YQC1BK--0cDHzSSDFbyMmsljQi1iyHyXR5SLu_bBs6oOEFCtFlVAzh7LSYeemIdUZbLV2yiMGH-i_lD6ZKLB7rsfRgEXO1kjbhWe2WxGNaBijGYfsE-yrgY5Tll1wVAFnH3Z9OYqgr5qSB8g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
با این فرمول زمان خرید سکه و طلای آبشده رو بدست بیار #دارایی_هوشمند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/akhbarefori/680309" target="_blank">📅 16:00 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680308">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b43b28bb1f.mp4?token=dPFSfWy7nqtpzYRCAfpqgTQgf2j5tBxOT3n-zZ3MAYwoZ1xIuLsNMjlB3twZWc1TU7xNQMIE7uh0wvTf4u7jpxJSckcT6OkLmSirX-hvwOKsWSyupCfSq-0XZ3rJNTaaLAUKXMXm2KHhz4AJMXIuay7pxExzMWczdhfYfnN8UCR85-6MlXbWdNAtOqBZ3_pg4KIpH3IQmfolRsgtNTP6qEgTrcwwP7kdalZsLp5b4sGceLY2_trWXtvDUGjIZFApUsyNHSaO00ziYs0U4ANWG03a58d9NzyH9_1Wxttp5pNEteU4fLQXVJvfiyd5ffaJlx11jB1UPLzmpv3v8kgrsQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b43b28bb1f.mp4?token=dPFSfWy7nqtpzYRCAfpqgTQgf2j5tBxOT3n-zZ3MAYwoZ1xIuLsNMjlB3twZWc1TU7xNQMIE7uh0wvTf4u7jpxJSckcT6OkLmSirX-hvwOKsWSyupCfSq-0XZ3rJNTaaLAUKXMXm2KHhz4AJMXIuay7pxExzMWczdhfYfnN8UCR85-6MlXbWdNAtOqBZ3_pg4KIpH3IQmfolRsgtNTP6qEgTrcwwP7kdalZsLp5b4sGceLY2_trWXtvDUGjIZFApUsyNHSaO00ziYs0U4ANWG03a58d9NzyH9_1Wxttp5pNEteU4fLQXVJvfiyd5ffaJlx11jB1UPLzmpv3v8kgrsQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اگه فکر می‌کنی وظیفه ‌ات رو انجام دادی، این ویدیو برای توئه
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/akhbarefori/680308" target="_blank">📅 15:51 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680306">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">♦️
حجت‌الاسلام رفیعی در سمت خدا: هر غم‌دیده‌ای به زیارت امام رضا(ع) برود، غم دلش برطرف می‌شود/غم و گرفتاری راه دارد و در روایات برای عبور از این روزهای سخت توصیه‌هایی آمده است/ توجه به خدا، استغفار و زیارت اهل‌بیت(ع) از راهکارهایی است که برای آرامش دل و گشایش در زندگی بیان شده/ در این میان، زیارت امام رضا(ع) برای غمدیدگان جایگاه ویژه‌ای دارد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.1K · <a href="https://t.me/akhbarefori/680306" target="_blank">📅 15:47 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680305">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-poll">
<h4>📊 به نظر شما مهم‌ترین مهارتی که در سیستم آموزشی به آن کمتر توجه شده چیست؟</h4>
<ul>
<li>✓ تفکر انتقادی و حل مسئله</li>
<li>✓ مهارت‌های ارتباطی و کار تیمی</li>
<li>✓ سواد مالی و مدیریت پول</li>
<li>✓ خلاقیت و نوآوری</li>
<li>✓ خودشناسی و تصمیم‌گیری</li>
<li>✓ سواد رسانه‌ای و فضای مجازی</li>
<li>✓ مهارت‌های ورود به بازار کار</li>
<li>✓ سایر موارد</li>
</ul>
</div>
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/akhbarefori/680305" target="_blank">📅 15:43 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680300">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Id1GZtywrNFttz7n4jlskBldK-mwyR6LOuM46NBBVnsQqH09MM4O85fJR8IgjJQyNep_Kr8sBoVfeOXHPSr2feDmCQ8JEHuqtidC99zGhQ39Xoxs4C-TFxP3WDnpR7WIJg_Kp9-btG8kpPszxlQHAorhuYLxBSZvef64Nt5_vOy-5t9FJ9tE7MxNHfuYZSvzP-mHEUKVQT3pOxIOzLssMM4NY7loew-L6PteoH6NchI73LJBPG-pdG03wO7tZgUFenHKkULALMUy1T4xlDG5-VJsqsp4izc7sq_NLwqqgx_Y3OoU1lSXgoJS9fMR2nURJHqk4rf1u4faG41iQ_TkOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سازمان سنجش: کارت ورود به جلسهٔ کنکور از دوشنبه قابل دریافت است
سازمان سنجش:
🔹
کارت‌های شرکت در آزمون متقاضیان کنکور سراسری به‌همراه راهنمای شرکت در آزمون از دوشنبه ۲۶ مرداد تا چهارشنبه ۲۸ مرداد در سامانهٔ سنجش مشاهده و پرینت فعال خواهد شد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.1K · <a href="https://t.me/akhbarefori/680300" target="_blank">📅 15:32 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680299">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Etzh8Q5aEUCKoRgfK96lNzXCP7ynl6oEkzQ3if2FsStQfvWaUkITB_8pfLiU8yon4Sf1o5cYKkeD03hoBk-_Lk3sfH4Nodpjut7w7nFvA68d6Ffadsc4IfbLQ8Gxz2aQ3gnvL4BEGhKqayFYO1BJdoCO4Xa-Pw0-3uMxG-Q_fdIjmjbVFjwMmDBniZUJaaTK2LrjiFTVEUEaJTr5-MfhhsHB7p5LkXK7u6CBLvKt8CWdhp1n5y3d28Pe1Fp2ShyzROBdVUmI-4OGZKhfOMasjSlIekDq3-PtoRbEfAXOj74CvZdAfj5HWxoneUUMswLkoblezeHU0RWC_Tes-0TZNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
علت مشکلات مو رو بدونیم تا بهتر مراقبت کنیم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34K · <a href="https://t.me/akhbarefori/680299" target="_blank">📅 15:30 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680298">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/53ba1afedb.mp4?token=i8WnEM7Gnygw4LfLwaGziDGbht14_ru1cACQ4-h45E_YnyPm_ssKEpA8dOV8alEc2Ag0CC4hfnkRK8GNE3uF7FLzlQjjyc9iybaW4-DrNJkJasjeKHsiWQpom7rAbz6wQP-W5AXkbx-sx7erXWnbn0p0M1t22Pqod7bC9PlPubHYXFnbU8HFyvgNabZ3GaqyTgN9zRuwqySnlz7Ri214mnzG0ZquI_-vvUNlMJfaMyMt8yyWLtfx3yv2-QZcOqLHkppSixmL6XtxhFJ6Ve2nIGcIiRmH5NcpBo-v41Ri_e-bkIwEFzAIIQ8WqdP26umTBEPPo4LDWS5wcRSkb64Q8w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/53ba1afedb.mp4?token=i8WnEM7Gnygw4LfLwaGziDGbht14_ru1cACQ4-h45E_YnyPm_ssKEpA8dOV8alEc2Ag0CC4hfnkRK8GNE3uF7FLzlQjjyc9iybaW4-DrNJkJasjeKHsiWQpom7rAbz6wQP-W5AXkbx-sx7erXWnbn0p0M1t22Pqod7bC9PlPubHYXFnbU8HFyvgNabZ3GaqyTgN9zRuwqySnlz7Ri214mnzG0ZquI_-vvUNlMJfaMyMt8yyWLtfx3yv2-QZcOqLHkppSixmL6XtxhFJ6Ve2nIGcIiRmH5NcpBo-v41Ri_e-bkIwEFzAIIQ8WqdP26umTBEPPo4LDWS5wcRSkb64Q8w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
فروشگاه‌هایی که قیمت‌های قدیمی را از روی اجناس پاک می‌کنند و با قیمت جدید به مردم می‌فروشند
رئیس تعزیرات تهران:
🔹
با فروشگاه‌های زنجیره‌ای که اجناس را با قیمتی بالاتر از قیمت درج‌شده بفروشند به‌شدت برخورد می‌شود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.4K · <a href="https://t.me/akhbarefori/680298" target="_blank">📅 15:20 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680293">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/19111ad870.mp4?token=WiePHUR8RH-HReJFhLojqCLgCftP8duEU6LW3XJbU2F8WAkaxoDQ3oRI9mlolGUgqfX38_UCbKij1KDG1A2rEPKx0ILfNSwGkZgJ3_RVKKQgW1kub_QGD-QUFPgT6mDgUJXKzLQXw-YLcq6YT6fj7Ra7u7AtDyv5x_UcrhloRQO4x5m6VbLg57PqPfczbOXygZYxgK4GEN9A5fqlyNINcIGDhyqescM9XenLNZ5EtyTETVxzSTgESIA5_Mn8BqtCVjDCytF5BX5qq3xp3IsF3lHdjj7Zq5pXG5vNmdfzW0zSWkXOGjnLu_f7pp89rSjrtjn1m3NUAo_a7n-9pXJ91Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/19111ad870.mp4?token=WiePHUR8RH-HReJFhLojqCLgCftP8duEU6LW3XJbU2F8WAkaxoDQ3oRI9mlolGUgqfX38_UCbKij1KDG1A2rEPKx0ILfNSwGkZgJ3_RVKKQgW1kub_QGD-QUFPgT6mDgUJXKzLQXw-YLcq6YT6fj7Ra7u7AtDyv5x_UcrhloRQO4x5m6VbLg57PqPfczbOXygZYxgK4GEN9A5fqlyNINcIGDhyqescM9XenLNZ5EtyTETVxzSTgESIA5_Mn8BqtCVjDCytF5BX5qq3xp3IsF3lHdjj7Zq5pXG5vNmdfzW0zSWkXOGjnLu_f7pp89rSjrtjn1m3NUAo_a7n-9pXJ91Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
چین‌وچروک‌‌های لاله گوش اصلاً بی‌دلیل نیستند!
👂
🔹
مکانیسمِ این فرورفتگی‌ها مثل یک ردیاب ۳ بعدی عمل می‌کند؛ موج‌های صدا را طوری تغییر می‌دهد که مغز ما می‌تواند دقیقاً تشخیص بدهد صدا از بالا، پایین، جلو یا پشت سر می‌آید!
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.6K · <a href="https://t.me/akhbarefori/680293" target="_blank">📅 15:03 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680292">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromمشاور سرمایه‌گذاری ترنج</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H5LrCOvLAhT3ExABjQ4PXZfFV03wTSgArLsFvar_tHZM3-HTaje35FkXgGnAsJqi_PhPk2aLIkkeIqTpQyTh5Fxu5lVbiP1ysXzLVZQyTvy90bMMM1g4-M4EkJ9yLi4tIlZdAgO_UGrWXoiUsXcbtaM1fZVDcF24FgKwlvf0gDtQ_hMdidfZCrAqR_ienfGuHlWWZOzEO5cJB0HNFDC9psl-HMZiOvPWUdpRBrQwowedAWkOPYW_xg7Z8e2EuLvbHSbFT56VTlkHQYKRaosYkesdojvAEsofSWJ9b_kk503i5w3KAlmFG5l8vO7SbHLbNC89hhWAZBpkpRaqEKkMWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رز ترنج؛ روایت فصل اول یک مسیر بزرگ
نقد‌شوندگی واقعی با ۳۹ همت ارزش معاملات
🟢
صندوق طلای «رز ترنج» در اولین سال فعالیت خود، ارزش معاملاتی بالغ بر ۳۹ هزار میلیارد تومان داشت.
🟢
هم‌زمان، بازارگردانی فعال و حرفه‌ای، در کنار حجم بالای معاملات، نقدشوندگی واقعی و بدون حباب قیمتی را برای سرمایه‌گذاران فراهم کرد.
▫️
@ToranjCapital</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/akhbarefori/680292" target="_blank">📅 15:00 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680291">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/65e3869a5d.mp4?token=YRJ9piOK3J-cT_uE7-cY6kTgMZr6CUR4SPuExp9ZNhfGyq7_vcW15UH9pJiKrEHV36UlCmCjfHieLB3DXIzWbwjMEvO_gcOKyXBjzKNa_pmJZvC9J25_VoMt16AjDLQE2_lRBTP0rvTCq-G2UaQR7pdALfaiNkZeWN1ozuhRC9GtwVtN19Dh0-AsCbFP1Y7GDLryrCGkDDP66hTT8LDKXe_GsfhPNaNQGWJ3EC2xRw90dcS6Pzw4IGDHcDUmjjFQ6YCO5ihK_EKB4sNsDIUKye0vkdiwtDuUssdeT2kA0knylMqYATAKcpdIHrSCuwxpLL0QGwJx4M5tr_hxdGa-_w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/65e3869a5d.mp4?token=YRJ9piOK3J-cT_uE7-cY6kTgMZr6CUR4SPuExp9ZNhfGyq7_vcW15UH9pJiKrEHV36UlCmCjfHieLB3DXIzWbwjMEvO_gcOKyXBjzKNa_pmJZvC9J25_VoMt16AjDLQE2_lRBTP0rvTCq-G2UaQR7pdALfaiNkZeWN1ozuhRC9GtwVtN19Dh0-AsCbFP1Y7GDLryrCGkDDP66hTT8LDKXe_GsfhPNaNQGWJ3EC2xRw90dcS6Pzw4IGDHcDUmjjFQ6YCO5ihK_EKB4sNsDIUKye0vkdiwtDuUssdeT2kA0knylMqYATAKcpdIHrSCuwxpLL0QGwJx4M5tr_hxdGa-_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اژه‌ای: تا جایی که ممکن است اموال، مدارک و وسایل مردم را کمتر نگهداری کنید
رئیس دستگاه قضا:
🔹
نگهداری طولانی مدت اموال و مدارک ضبط شده از طرفین پرونده ها در شعب قضایی، ممکن است موجب فساد یا تضییع حقوق افراد شود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.4K · <a href="https://t.me/akhbarefori/680291" target="_blank">📅 14:50 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680290">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/100da9ed3a.mp4?token=XiCs8Dga1sRMpknomGwlfn-Em6fkyCIZZSZ4BAii4F_7bFzOKfhqLiF69Sj1s3Eu6pJC6nL5koNIhprUH0yF0ozU1NKann3yx30jk-NsTVBINOW3pmC-GYqBorElCnAx7DyPw1C0wubY-DjLc5x68BMhbp-kAmdTGH-PveuOVwvFMlmTgGKmA2rGMrwT-0R5cuHWmogBH3yQPQ_7o-71dE6sfq1IgRDaa4JXo9hmE3y57uIkvIEvZk9UTwWWzkWD8VgUrGHr49Izf9Wwkq4-cyvyyvJXxLkdK1lsp6QVbQPHHtT7Z1_oJVpHDzGLLROmBR7k71ILk2mAfuJ2YNEtCQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/100da9ed3a.mp4?token=XiCs8Dga1sRMpknomGwlfn-Em6fkyCIZZSZ4BAii4F_7bFzOKfhqLiF69Sj1s3Eu6pJC6nL5koNIhprUH0yF0ozU1NKann3yx30jk-NsTVBINOW3pmC-GYqBorElCnAx7DyPw1C0wubY-DjLc5x68BMhbp-kAmdTGH-PveuOVwvFMlmTgGKmA2rGMrwT-0R5cuHWmogBH3yQPQ_7o-71dE6sfq1IgRDaa4JXo9hmE3y57uIkvIEvZk9UTwWWzkWD8VgUrGHr49Izf9Wwkq4-cyvyyvJXxLkdK1lsp6QVbQPHHtT7Z1_oJVpHDzGLLROmBR7k71ILk2mAfuJ2YNEtCQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بزرگ‌ترین پالایشگاه روسیه که در ۶۵۰۰ کیلومتری مرز اوکراین قرار دارد، در آتش سوخت
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/akhbarefori/680290" target="_blank">📅 14:49 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680289">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3dd3c187fd.mp4?token=FGWaaUc34igQMUKP0pbpenx4WBgqooNot1r3WOuEGfceFQgMlK56RsEugNebku6looEpRSHqOoVUEcF5bqDUOqntVhmNircir5RzjZO-8sQCtBVPC8R44fk5BzNNZbfYJmNCNs3LONh12oUHE_er4UbgbE_b7_s_aTrykqyr4O1pmI7vgM1GNsAsA2hb5slkpeon0WBfvp-VkOEl6xL885ZtKOE3g6BBwXtJndfFWFclnpIlHxJAP340wYpTFiSGjRtU9nLiXV82iob_ygQGKNFqDXi5uUugj0opOniaWzWuVvzHc16XXiUGzNKxmgNifdgUdPmpveHV-SJxQJVLgA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3dd3c187fd.mp4?token=FGWaaUc34igQMUKP0pbpenx4WBgqooNot1r3WOuEGfceFQgMlK56RsEugNebku6looEpRSHqOoVUEcF5bqDUOqntVhmNircir5RzjZO-8sQCtBVPC8R44fk5BzNNZbfYJmNCNs3LONh12oUHE_er4UbgbE_b7_s_aTrykqyr4O1pmI7vgM1GNsAsA2hb5slkpeon0WBfvp-VkOEl6xL885ZtKOE3g6BBwXtJndfFWFclnpIlHxJAP340wYpTFiSGjRtU9nLiXV82iob_ygQGKNFqDXi5uUugj0opOniaWzWuVvzHc16XXiUGzNKxmgNifdgUdPmpveHV-SJxQJVLgA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
واکنش رسانه‌های مختلف جهان به انتصابات جدید رهبر معظم انقلاب
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.5K · <a href="https://t.me/akhbarefori/680289" target="_blank">📅 14:48 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680288">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">♦️
رسانه قطری: توافق مکه بی‌معناست؛ چرا ائتلافی ضداسرائیل شکل نمی‌گیرد؟
عربی۲۱:
🔹
توافق مکه مشخص نکرده در برابر تهدیدهای منطقه‌ای، از جمله اسرائیل، چه موضعی خواهد داشت و هیچ‌یک از این ائتلاف‌ها اسرائیل را به‌عنوان دشمن معرفی نکرده‌اند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.3K · <a href="https://t.me/akhbarefori/680288" target="_blank">📅 14:41 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680287">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">♦️
تنها جمله‌ای که پدر مینابی بعد از شهادت دخترش گفت
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.2K · <a href="https://t.me/akhbarefori/680287" target="_blank">📅 14:39 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680286">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f8715daf57.mp4?token=E8Ze7hLVgKQURM20n9Qg6U7vp8hcatdi5xk7anoE3CfY9YWo7jroZB9sK7LmobzbCdbpd7dqX4KDm4dtgo8ybk-LVXkBMU3Ta0eaOIX89FQE1ssCPX7aWg0Ka01QXiik3Unn7-SaF4ocPP2K4jLsriZxsn_5OXu0Ol9bW9AfvXpzqnYxyFOeqmt6Jlzj5kSKkOr8Qb6K2ceMi-aAwyoL4OaimpMQMZ6o623jwq57sbDXF_9HQNh-sXs2JiM7lxDhCe6z6noVAFGvye-nGDK85pSD2f5yW8plVyHKUMEU1iIbLqOQmSLxj7JnDmYcQ_nKHCdDzoonuwfKrAQzUuyMRA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f8715daf57.mp4?token=E8Ze7hLVgKQURM20n9Qg6U7vp8hcatdi5xk7anoE3CfY9YWo7jroZB9sK7LmobzbCdbpd7dqX4KDm4dtgo8ybk-LVXkBMU3Ta0eaOIX89FQE1ssCPX7aWg0Ka01QXiik3Unn7-SaF4ocPP2K4jLsriZxsn_5OXu0Ol9bW9AfvXpzqnYxyFOeqmt6Jlzj5kSKkOr8Qb6K2ceMi-aAwyoL4OaimpMQMZ6o623jwq57sbDXF_9HQNh-sXs2JiM7lxDhCe6z6noVAFGvye-nGDK85pSD2f5yW8plVyHKUMEU1iIbLqOQmSLxj7JnDmYcQ_nKHCdDzoonuwfKrAQzUuyMRA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
براساس علم عصب‌شناسی کتاب خواندن برای نوزاد، قوی‌ترین محرک رشد مغز است
🔹
در سال‌های اول، مغز کودک در هر ثانیه بیش از ۱ میلیون اتصال عصبی جدید می‌سازد!
🔹
شنیدن آهنگِ صدای والدین و دیدن تصاویر کتاب، دقیقاً همان چیزی است که این شبکه عصبی را فعال و قوی می‌کند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.2K · <a href="https://t.me/akhbarefori/680286" target="_blank">📅 14:33 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680284">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
شهردار بوشهر برکنار شد
.
🔹
انصارالله: عربستان به دنبال وارد کردن یمن به جنگ‌های بی‌پایان است.
🔹
وزیر خارجه آلمان: ایران وارد مذاکرات با همسایگان منطقه‌ای و آمریکا شود.
🔹
براثر وقوع سیل و طوفان در فیلیپین ۱۹ نفر جان باختند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.4K · <a href="https://t.me/akhbarefori/680284" target="_blank">📅 14:25 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680283">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">♦️
رئیس پلیس‌راه خراسان شمالی از اعمال محدودیت تردد انواع کامیون و تریلر در محور فاروج–جنگل گلستان و بالعکس از ۲۰ مرداد تا پایان هفته خبر داد
🔹
ممنوعیت تردد شامل انواع ناوگان باری است و وسایل نقلیه حامل مواد سوختی، مواد بهداشتی، کودهای شیمیایی و کالاهای اساسی از جمله گندم، جو، برنج، ذرت، سویا و دانه‌های روغنی از این محدودیت مستثنی هستند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.4K · <a href="https://t.me/akhbarefori/680283" target="_blank">📅 14:22 · 20 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
