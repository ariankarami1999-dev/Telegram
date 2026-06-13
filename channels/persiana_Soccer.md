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
<img src="https://cdn4.telesco.pe/file/ssDHd6s_djXWaajl1LAI4_MlYBwQRQj0VEKv7ISYDGdPUG6qgk9Lgai81jzGsn_Pb1R9Y5V1l9dcjbxKBOVkHd5XNfBA2vDtGD-hlYylTk42MVg529VS-JocyhaLU9j_0EHoIrYF1FIwJwuZC0JEKAeKI6G6UZ0zHGsK5532HrenFI8lvDgjR1sX8nYuRjvRjQU7BnpP5YY6uzNFcqY0oldsiJm1uSQp2X4ZGnCp3-nk7EVeHpRMkleqKvbr6p2S1xFTthq0X7pUeBQmNy5fnzlUpn2Ez5_ak_9SBPQLAndK0AcDOVYRD1p9XpIjLtwcvP-Yaz2uITSF4YrFftZlYQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 247K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@adspersianaپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-23 18:04:58</div>
<hr>

<div class="tg-post" id="msg-23363">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z8WJGM_qQLG0ZpqGHTOF4DruZtgUT0V2SMYERdulOrEVHcxiZQDrUcYLKHURpPJnB_4WaCu3kDdduFGcvDU56K4N1zWO-54BrBzplmRdnUeAxGVkPgjyEDnjVXARxAt7h7Ci4klwCi1EzKGM7QqIuqyIU40TobvMY4USysgr0CGY5kmX-yWZdAVN_yf3qGtnQ3u5i2N-SW-Bw_JyDfxENXw0ndT4lH5em1Yys--nPUfX2uBb7h9sGx2aJKHRCViZkDg6SLfCtZVTjPb0J-3pBlW32OJzknd3WI8vtbDDhUSCJqNKFa8w6xCB5SG7Ez6f-LcsdGzRPxYloqupAiilAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇸🇪
سوفی‌رین‌مدل OnlyFans میگه که ویکتور گیوکرش بزرگترین طرفدارش‌بوده‌که ۴.۵ میلیون‌دلار در OnlyFans برای عکس و ویدیو‌هاش خرج کرده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 3.03K · <a href="https://t.me/persiana_Soccer/23363" target="_blank">📅 17:59 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23361">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ObcLwAgIxaM_ltiVkRX7bPplsen5rj2W_yrL25pWjp-S14vTaXqVeWq6UGDrOtdlEX-eoeOpcOLmThAisRz7vRtGKNZhvQmdwVZBLocklJPkt7xoYe3FuGgmmdAhij0b7YyjQAX-DmkpxuoGquaMA1OssJ9sNZUnvQ2RdXU94orG1xEJZcgugm969y4bi2Z0u9DyLb-cnTuxXmDkjux5vPUdt8iSOZ9tx6QIq3aU1Ju6acyY7xIbeS9qrq5Vg0JhhOS_DJfPD0DpU6j_3rHwUJ6aaRTe0-JsgrdSMd5b2oD9zjgAdk017en9oHrGnM2ZTezsqKmiiYvYR351_D4PBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
👤
علی رضا فغانی اسطوره داوری فوتبال ایران بعنوان‌داور دیدارحساس‌دوتیم‌فرانسه
🆚
ساحل عاج انتخاب شد. این دیدار رور سه شنبه برگزار میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/persiana_Soccer/23361" target="_blank">📅 17:21 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23360">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IO4We_L4ZPYaYcF4-jR-w0QQo9SPfW_FaKUXwdymXFPPfnVuI4nsu8edrM9zsh1EdvqJgJ9mvTYmmVQcRiJSf2M94WbUgiXmYIb1fBRX7Gv7w3wI8fTsvTYfBbawVpJMYFqLfb4KX-jcamULhcCmJO_3YUsLFwW0J18IAcQEvAdYGzQdzqMUWsbVoHQYGsDX71SkZx5koVvMpzvaT-vrcVZ0ilpETTtSnDwmm0ERbD9I6LvbJcVHrSaTlC-8c98MUVfrh7s8xiDCQ20iQ-5Xsx6plX_7Y2YrhCn24Ls9D8TsigrGS706SbFQTAlraVGGrxRTyedFG2aYH5flWUHLfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔴
#تکمیلی؛طبق‌پیگیری‌های‌پرشیانا؛ رقمی که استقلال برای‌عقدقرارداد چهار ساله با کسری طاهری مهاجم 19 ساله روبین‌کازان پیشنهاد داده. فصل اول 55 میلیارد تومانه و در فصول بعد سالانه 35 درصد این مبلغ افزایش پیدا میکنه. رقم پرسپولیسی ها یه مقدار کمتر از این رقم باشگاه…</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/persiana_Soccer/23360" target="_blank">📅 16:50 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23358">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Dsxnr-LdtlIGsoR6HioC3hYY_MHBIIxwxycV_GE045hxvvAOjOpOW2prMRFzIUrakHsoD17m-Ki_l9474lFjWlvBLH2xXvfr2VTPrtklEqWS1R9K4favAtZWouYjCvlRRDvqV_KEre9UO09AcAOY7PGKEyHcAVmimjX3tKDoczxtvIjwZvBC90GE4RSm6u-CcSkYNewG7ePti1CFBCQ-vwrO0FUo_HgPCWX4rpCrYWInjktUIB3g8eu-4vgzZNb3UykAqYiWBD4pP430slGyZd16ASmC9isqOikHBrujpbpmQyLAnMwjvkoD0xHvQD2XL3s96AE3Ds6zwhl5laLGdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WobKySs5564p0N6vwzBOT-dC4tSlzI9DQkgn_sbAyw_1GIyaYw6ulhBXDQoCZzOlAfZ5xq1kJdHPP3PnE3dDwTTxejtZTgIgw-lM4V7vvHjKi17LsXXBjkDe4d9BYLhwS7V3DnUCwzw1_qMZzfLxQTav5-UU_k99iUh3Mewvae3F4N9ICKg9SoZTOCLYezKK5uLTwyv-lgyfJv4QpJX9T05nGg4X5gcZpaQW-WAv6UdaxF4YyI6pCQBABVl-jEetZg1jkkeWIVw7k3vwjKshtLzubyxm13xfgBgWiDKObbQxH9BYO_waF6oLMEfioMmrewHzUl-Y_riyDQOn9xHW5Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🎙
دوست دختر پسر 15 ساله کریس رونالدو: من رابطه‌ ام با کریستیانو جونیور عالی است و شایعاتی که منتشر شده کذب محض است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/persiana_Soccer/23358" target="_blank">📅 16:20 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23357">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BRfDWALqvLCmuVK7hlVJRHTVZ9MKXnpepi0xrIRKl044iB2rUuyjAsRa9woPrYAfTmTSHSm9LgJ3y3L3ynlerFkADveff2LNSJh9k9mVxzCeeFrhbr9VZ7wK8qzI7Sy9pQk9KT3K-9kMh0cnBFP2ryZdEO4BK1KQ3-9U7RhLujItvTOQdfOPOhbyCZomrldDPNV_fe3S-LsTtxU9-FfU4fKdGkHxXZFe0asdNhXB3jZ8LN0ZpphCqOVheDxW8aAgGZErp1atJpqPrqBioujsEwRk4uNPcD5drSoJqC03vIJ90UrUKB8RAZhBNQr5wg8VAw29uRmUkiP6R4uvQ10BRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
👤
#تکمیلی؛قرارداد یحیی‌گلمحمدی با دهوک دو ساله توافق شده که سالانه 60 میلیارد تومان دستمزد سر مربی سابق پرسپولیس در این تیم عراقی خواهد بود. دهوک بزودی از سرمربی خود رونمایی میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/persiana_Soccer/23357" target="_blank">📅 15:59 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23356">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AKsFFG_XZw0SocvmcsV32r7Hi_wBEKKRu9VbADV1RXJRX8mwhg9zHHlm2Q7mmklUfPKtzTheRaeEWKwJhi9guJr4396iXcYdEZcNhi_X_sMelitxSBOPU-OoBUfJAvo3Jr0nFHtqhMnbR1KGo49mCozBgd8iT-s82H3m1gOEOT_r6WxxALr_lhZdwmnht-LLZ-G7xub0noCqRnNVkDl8Q4renfnJEzKx-BAnkZDUpxFxcM4moKxUlS40zgI3t9BOhbV8Q0R09pQpSr6QK1P_vgL8DI42dF147MBfUlgQoFCPy8HBVdXxHFCAKbVvS07jvmgWUbzRwwXxsNqgBCEzBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇸🇪
سوفی‌رین‌مدل OnlyFans میگه که ویکتور گیوکرش بزرگترین طرفدارش‌بوده‌که ۴.۵ میلیون‌دلار در OnlyFans برای عکس و ویدیو‌هاش خرج کرده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/persiana_Soccer/23356" target="_blank">📅 15:45 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23355">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XBsll-nDpWZtPUPdZjc6KqPez7oo1lMRqzvIMUuuGCeaMvSs4Pn65CVe3A35hQiDH9GnpELr_sD3_QkUbGNsZRQDjIOiddQJLJzX40lRpDWdVDLCQ6mfhc84B1up8mtcAP2kcHoBg64dwdgJPFicmkigSuhAJsiobbBuX3XuZSC7G_KdTwNbUGlL9RYs_t3NrOkAvMM4ULrdcz3uwSe8-qzFPcSoGLZ8bzukL3w61qRrl3XQdpeGNy583QYBZXTkNgnyDRcaa8xY_1Z--RHrjMk_JE4VsJ0cLzo6sqj_YaUhyW26oXE_d_WZs0qkGaTJM0VtF035GRYayKt1sMptFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
رسانه‌عراقی‌اکسترا از انتخاب یحیی گل‌محمدی به عنوان سرمربی جدید دهوک خبر داد. دهوک تیمی درکردستان‌عراق است که در فصل قبل لیگ عراق که شب گذشته به پایان رسید در رده دهم ایستاد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/persiana_Soccer/23355" target="_blank">📅 15:31 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23353">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JWkPvNqSPd9MVgh1WjySjMFyaxLGqbO2iZARcw5yJN-arLK3Rm9kwCzLNCUCjU_B0lXySI4l4jEZAQnJHmsq4sjXIzYiGPjw1TC-z6EhvGYo_ll85cgeaZRhfANz6rLeCvt5xoOBZJ3eKWWd_mDjXe_5lwVVZBNjBDSp10tMe4mkbjFpexAE7PC3pcAHz7yMokanFMQ78d946XeFJzfaXPqRIt_ZKvggZewL09u2-dNdvWGqwmPa2WIyToTr4cGdevNcxj0Q9N63kBAjjusnZcz7cNuQqXr9wWw1FORytORlbOTMbhuzxO5rSUCeJo1_zmJCtaduisKuzZa7REatng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/n85_65G2cEEPR30dQi1ZwrU4K4hO3DzBh6o77oUUTsFrLWeKpH4Wmi71uew4OVDX-9ZDQW4tf9_rNm5KNCmUph23BqI9w0fbknqFW7TcC07W1kFYaX-C27yRr8ejcGpRx7rIUkYau-SWRvNzCS-9GUIic6hZAw8Lm7ppJ2i7uEnKBaNme4c98n31QgjS5NYnTT0QM86ENjlGChGP_G1tcbUDjQbl4OEpsysv-1AsnIVzld5r8rDCglxX-Tp70Y2pkDWPZd7YrqYFO3pvrLlkT57PACMoD68Yx0am0fHK-hr5RifNxi04bjYm94vrv_JmTUXxInEOKkhtobAEVA9XOA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📊
نگاهی به کارنامه کریستیانو رونالدو و لیونل مسی در ادوار مختلف رقابت‌های جام جهانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/persiana_Soccer/23353" target="_blank">📅 15:11 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23352">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dvFH58eIvFKZ0k4t0VPV4hSzIdfqCFYf49BpXCmKeNNQD-zOxgwfzN9NMNfcd_TQlskRmveUKeSbICFzdBg0M_OmOdqlgjoZb6H9yv9kyO6NDFgK5Db_20cNQRAL-Va89SRYpvboOu4SZ1cQRgWalomiD0Xzpri8xkfEZsr5v49awD76GuAHirWCHrT8A52L1wNSJG_H1g5pdagco37Tm3o6pO2tEdKYTtorgK_veYYjmxQ_ENn9t-VMlC8C-38ScoAhbLwj_cS5j0OBqPy1vDwqUD-UUnzZoQxjViJJTaBp2oUinarl7dSHowxkZp2RtF1MOmmRl7DJI4rpighyZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
لیگ‌ملت‌های‌والیبال؛ جلسه‌‌مهم پیاتزا با بازیکنان جواب داد؛ اولین پیروزی سروقامتان مقتدرانه بود.
🏐
ایران
3️⃣
-
0️⃣
آرژانتین
🇮🇷
25|25|25
🇦🇷
23|19|23  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/persiana_Soccer/23352" target="_blank">📅 14:52 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23350">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/C4_mcdDrRPkjwF3_QFksSwABBqKYyPgMsLAArSH2GZTT7Tllmufun0-0q35jTaGhcEK0e4J2jVsUPiOEpOUoLb_bD_6vc52B8dGfxu8g8MVO2X2QNSDjSXMBeTcgKDijGMqj4svll0Pbh26fL9yEZctnJZsS5bKY3b-6eiqVvL3o7l_YVuh2NZbdEDM4rtgJ4qliRPkCxP-pxGWjvhrsDwFbodnHv5KOlC9rMv_rhRV96sFtlxiOi8m4UC0ps2RG0mWf8WJ76ICefwd6nFuydHwOd8Lrd0kKCV_Sr3WsjyuIxX_GMbgr4oxRfolsBblF2XaKJnfJ_Lh1oWAIi6qRWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OPUpgCE8Ahe-ftOb2ePETZHC9Aj2F5R2FHOOSbXP-n8bAOh_gghyZOO1JdeO3Mmex4d8WfrDvkQbxyAijgFYDVyLwxb70j-L-lFXEV6r3i44iJLizT8dJpFwnKVYs505vE6fxyYrgVcf3Wl9NNYjw287-AEdqvlI3i9rvPqk_t2Sk5YJG71WtGvdn7vX8t4lFewnc8aBypmvABG6LRrI7mZrGF38c9ivKgnFyIHd6EVdMkqHQAnvSBIHCpt8aqVKbqTWWJHRKJaZPqvJGvaw42qSJd3NuxPpGXYMwAmzOhIfpSa8PQkFDLJ_cgAYbYIkf0q4HgrrPi5Nx5ZDMyUhrA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇪🇬
گزارشگر اختصاصی بازی‌های تیم ملی مصر در رقابت های‌جام‌جهانی 2026 ایشون هستند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/persiana_Soccer/23350" target="_blank">📅 14:34 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23349">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z7vciWc7ddL9g-43hQ3JSqMa9LBNof2JpaVGpgvlT7ZhZJl8u3OPnBvDTxWRovm9JIPjymOwFxkHsEYzUHvm57E-YXfR83SoJ88C6K4tjjCkopMZESQJCeYhLo-rvRnmoNOkDqNsxn-nxuHmXomn2KgeFxmaFMWUWvT5DIN9pCc0JW4W1Rz5VAitR8CRg8V9ypDBq_eG2FXmqh2n6IO_oRnxGAHh1S64zxceRI08nVwjBnosLhowf7BMYkSA904pgdNUZuPYsu3Y1S5SP-oxcRXsgk3bqtxJFkrgS1ZTNXF8e2H6DkI19NS7vmB6Em-SaR-t0NRH7R-cpowUfRXr8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌دیدارهای‌امروز؛ ازمراسم‌سوم افتتاحیه در کشور آمریکا تا‌اولین‌تقابل‌جذاب تورنمنت بادوئل فوق العاده حساس برزیل و مراکش در بامداد فردا
🔥
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/persiana_Soccer/23349" target="_blank">📅 14:24 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23348">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3ad2f53b38.mp4?token=oWSFqFkBloU3fAINN4hXm-WgcvxEke3vEL-PJVIcvVQFXhy0I1nfWFflFqV86LfCr5oHyYTvvp7qedjCVuZBytS_1KMSmtJi_e6AzmKi-FrQlzmlWlWfBBMF28Vupm-CEIvDDHz5WYj6FXV-vnM7XkJVu73XPBcDtLVoE90ARDgHT9Usoxa1ggfo8Bw1nOTmQ3W1PUyXNJx5Vq5I0oT3oFXNjYYs0fp2CxBHXU-BOpvqHjscTb-XkxgC1xRfTBaq1OKIy1Kmt8-1uWEM2Olmn6q0Yoif7C04iNgwxvZ-zSeSsict9nBG-XPHyaF9OSTqOQa2t6JXREk43jlt8ySBvw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3ad2f53b38.mp4?token=oWSFqFkBloU3fAINN4hXm-WgcvxEke3vEL-PJVIcvVQFXhy0I1nfWFflFqV86LfCr5oHyYTvvp7qedjCVuZBytS_1KMSmtJi_e6AzmKi-FrQlzmlWlWfBBMF28Vupm-CEIvDDHz5WYj6FXV-vnM7XkJVu73XPBcDtLVoE90ARDgHT9Usoxa1ggfo8Bw1nOTmQ3W1PUyXNJx5Vq5I0oT3oFXNjYYs0fp2CxBHXU-BOpvqHjscTb-XkxgC1xRfTBaq1OKIy1Kmt8-1uWEM2Olmn6q0Yoif7C04iNgwxvZ-zSeSsict9nBG-XPHyaF9OSTqOQa2t6JXREk43jlt8ySBvw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇹
👤
اسپید یوتیوبر معروف در حاشیه بازی بامداد امروز آمریکا میگه‌ رونالدووپرتغال قهرمان‌جام جهانی میشن؛ زلاتان هم این‌مدلی بدون هیچ‌حرفی بلافاصله میکروفون رو از دستش‌میگیره‌ومیگه برو بیرون بابا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/persiana_Soccer/23348" target="_blank">📅 13:45 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23347">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O0oCLsr490IHnAczI2whDHnSmeTaAbLz3I8uDaEA2mMK2XKYLcpFX_c-9joc9aoMZCefmttcWMPMXaDMPyZErDkwav9WMZB-SXlk2SsFQbT1KCioSkBZwm6z2dRCS6CzceCl_Rf6MLqHKfHIklaBZTX_CNC6swsApGMM7xUC5KhQp7_HLSXMHeIZMOBNDHc0YFCBM2tqkCUfrIjhwWOYtIRmWU6WjKDTJzsCNnNTrHA7UDXpYeIk2NwPR8maXZPa1mJRiwoi8mgQnTrzh0gcf_w1FrZ7SFszZXjWCCtVaDSzSBofzZOCLWFOKW01iTnslC-aYd4tjVG6h56YQqUK9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
دقیقا 19 روزپیش؛ صبح 21 اردیبهشت؛ مهدی تاج با تاجرنیا رئیس‌هیات‌مدیره‌استقلال تماس گرفت و به او گفته بود که فدراسیون به این نتیجه رسیده که امکان برگزاری لیگ وجود نداره و بزودی استقلال رو بعنوان قهرمان لیگ معرفی میکنیم اما تماس‌های اخیر حدادی مدیرعامل باشگاه…</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/persiana_Soccer/23347" target="_blank">📅 13:20 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23345">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MlV6dv2c6iFFzRdxEQi2af_qlftHKsVV6uPei9uoh9RrK8bZSFaRthDLeVhpVJKKB2PUd-vj-TDDk8e9H8CIixtj-9E8JwNA2UdjAVCl4Og5VRsU3QBDEt68r9n2Enr-ZPJnUxGkFkqoyH5VOvChRc07uDKvlpIhUui0KTYt70xPYl_c63-lCGaZZIek5FVfXAFvg_27d924YL5bELc42ygr0y85EShG3RTxpM1Ayys3OFHLMVbDa1wQYfnunyZP4rCEoywLuceSp1SvxShL6KviVPhZ3vVfuRmaOlebkNzzmCcj-XS246CK9TvKWKJRwM7iypHOso3tKhexZzo82A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LHygT6oii8WQ5tE_2TFB5TGIUfMn9HKd-5xIRw_4yTHbOm-sW1Wt7XPppyUyAgNfxSYJognZMb3wLDvdUqi479QWySQ_JciMdrkSr7esRFB8IxclpPLiz9sP0GwO5wO0l3B66psL6nkCk7oIi0bZ0Y4YHq8wIhJwi9GPgjBwgfTDO9sPczNSzP7o-O5GKB-GAKnIq1tcbWrm74Qp9e3QItMpkRSi1zVkCcTdbymMcUWxcvId_dJ1I04zlTR_QVKCjceCjhGunPHj-PljvpaqvGyCd39To-DJIi4dloK75Oj9EZFlCkDK07CXon_KmTflVlMVyW7QFEWtV1q-UY06nA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">خبرنگار معروف باشگاه شاختار: بازی دیشب بارسا و پاری‌سن ژرمن فوق العاده بود. انریکه یکی از بهترین سرمربیان حال حاضر دنیاست. همچنان معتقدم که باشگاه‌رئال‌مادرید قهرمان این فصل لیگ قهرمانان اروپا خواهد شد...!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/persiana_Soccer/23345" target="_blank">📅 13:09 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23343">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CarchW2PrKf2bElyduVr4Gvwygy1w0R6hI0bk_Oq9qwqlbbWLCy3C-NpHGBPFM8mGCQ39Dvf13GrSB3VaZ-cJB4IB7XY9GwKvm2wUbHgBlp_aNEgGG05UmGbdyIeHtJNi4Bl0MyHXrAoMi1R7dpPCyWIIjlIv1CEUUP4izFmxo1W2BK2x8eJSb9_9KASm4dMNmev758qdBUzRMsVMMz3ssC8j08mF0jlyNhN4Kw6f9iQic27Yy3fdC1w1AxUSAZ8dSY1_0wTzutVVq5_wAOwMQ09F2elc1HYwCRVgC3cEj8SzynES1iRKk-gWkSSZb3hSfs0ly5yhk-pg8-if1iiqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#فوری؛ رافائل لیائو ستاره‌پرتغالی سابق آث میلان در آستانه عقدقرارداد چهار با باشگاه منچستر یونایتد قرار داره و توافقات درحال نهایی شدنست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/persiana_Soccer/23343" target="_blank">📅 12:44 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23342">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZAHk8dOS3otVj1FJEQTPUOf0UDLtP5GNBIC6OHfa6aT-gV6j9riUb54uXi1zwktDh4CODSL_GFEREu4pJmvLrqB5qAoWHUvkEJxWyM6rkXblEVKnI2ApUmntswZXV3jpPxBvT-ybuwqGFC48mSXdvGs4r3uUhsibzSpFGJ0vRmOh5UheAH2ICE8RuxliMTL1WvPR5nLEmE5-HycNf677RUuZsRtD0khHn7cxfzTlqo7YPjH_Fw3esLk4cbq2eX1At7-I_alDFenGWNW2R4fMRjUdSr270r7sIUdet2KDfh1ear5QxRTKqVeOgG-caAnRR6jCXcKZxeJpIyHvewIQEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
کیف‌وتجهیزات تمرینی تیم ملی انگلیس در حین انتقال از فلوریدا به کانزاس سیتی دزدیده شد. بنظر میرسه که هری کین یکی از قربانیان این اتفاقه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.5K · <a href="https://t.me/persiana_Soccer/23342" target="_blank">📅 12:21 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23341">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QDPs8G2Yq7HRDTeNSdYLy4scQRUwWLWgpfMDlcZaeTkNqyOI5ZmovhashKfPh912SaPTN5Tt4ITK8JJvXpmvsQ73k-aYySkGEyM6VKHqY3rlNYOUkekU9HQ4cgqet92V-ceBIG1CQqFCA0Eh-MBK2bJRidO_Z-MRMhhXsJ0UHMaQPDOPyXQIJ6aOnjoSrMbOY0JJI8Y0VXOWPMFQE6Ws6tU5YxJR5wOmQDnBOnjpeHzfxImpH6Z8jK1kk8xjGNlfO15IfQ1C_VayY1KAMgFMtkXoIwTwriLukFBjNCWhGvYow69v4owWqbTNAd5LyvUzP9ObYKMtUBNF_sDRH98Z-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🟡
طبق‌شنیده‌های‌رسانه‌پرشیانا؛ باشگاه سپاهان برای فروش محمد امین حزباوی، آریا یوسفی و مهدی لیموچی روی هم مبلغ 220 میلیارد تومان میخواهد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/persiana_Soccer/23341" target="_blank">📅 11:40 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23340">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gltS5vDvv3q26xpnaIgcg4vx7_2JMquWe50zlwzIm_vVm45rdAbMPeXqJSyQ-FPg19tj_yGV-cvXra45dLxfDs8CVBmoTlKSbtcCC2oCkKOz0PhDOvaL0xFalS4zay8ohzg_ZZ4j_F1WxTVl7EY3Aa4HoTDHHr_UdZhTpPJHYyV-t5eA91Lf7LCopOHj_ZNs1yNDF9_HcSnFoxPCCvZPJbcemeOSAdIFTlMAMAMhlzVcQwNk_PmuIrKhY8qaJcTe0x8VWXG_0dLGJthf_Ov3-0uk9FGn-xs9BK4TBv0jheKEmBAMJ43UgB8_KdtBb4jVEtmv4nAOHqWE9ivo8Te73g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">▶️
گل‌های‌دیداربامداد امروز دوتیم‌ملی جمهوری چک
🆚
کره جنوبی در هفته اول رقابت های جام جهانی
‼️
هوانگ این‌بئوم با ثبت یک گل و پاس گل و آمار بیشترین تعداد لمس توپ در زمین به عنوان بهترین بازیکن دیدار کره
🆚
جمهوری چک انتخاب شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/persiana_Soccer/23340" target="_blank">📅 11:29 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23339">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C1HXfOkByOcUg64VeMR37jNqUk9A9Re-C3rrApKm7556fjsQz89KqngLTGDE_M7AeSnGkNyoGLI3srgticfcoOuo7IlsglTPZ-wsRLYt7OfmapUp5cEYPbD2mMG0f5qMDOo_SfKwCdA9iUde9JzK7-j5ynV0ohQKStFrY2p6Dyro6qLooaxdQFSptHRi8yw5eAVddlTasWd9sSFD0C6PuORcqDYuvDnMuZdZPgbgLOE_Wv-DluJZcf7xRpMdJFqqc6S2Q3J8vVr-1j1ZMBwvNUoGTCzXCzBDytXZPILpzJYKVyFkWSKiPNvvzBWYx7pEdpT3e1iydFDctuT0f8mFuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📱
10 صفحه برتر در اینستاگرام با بیشترین تعداد فالور؛ کریس رونالدو بعد از اینستا در صدر جدول.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.1K · <a href="https://t.me/persiana_Soccer/23339" target="_blank">📅 11:15 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23338">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fof4uumosMmMXccuy-NNkDWdZ4HjPGqP7vq5wgqfoT_YUXqz_ngWD0CgmPn_EzFonbyMYZ6GljOiLDnpGnTYalbae5PXaa-9184fE6-jMOr2dy8XZE4XcW0HjJ_W9Jk-IP6zWlFojCt_GjAUkPv9FTy6nom0gsD8RpABOBQdghtbfdhDpiUo_L04fE3LR3mgDcdeNAJYmkROOsH06kfJ2kvtBYa7oN2lYmIgIKPGs_ZL0HAm3_cPsa4yDdMPtUjybdawppxwQluhGorSxlSiXVlWLbc-QQEizZjlm_sVyFIALVLrwYgodYFV_4amFlgKFbxskIZJT8s7RQ2LTnz8YA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
محسن خلیلی معاون ورزشی پرسپولیس؛ بعنوان سرپرست مدیر فنی سرخپوشان انتخاب شد. نهادهای ذیربط مجوز افشین پیروانی رو صادر نکردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.4K · <a href="https://t.me/persiana_Soccer/23338" target="_blank">📅 10:56 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23337">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kostp4X6rAbaSAtG2KEHTc53A39O0NTdvhE-x_fjcu9RJTeC8P93uxxMGRoCZ_bW4wnvi7GUwLP-h1w9Gzt_KAhalw7JXUpc9yPW_k7bTBzKu5V5tB-zC_r-kFvrdQ7pSqeLH714vLlHQDKehsf9MOuX9tbnQo_2fEqZB7M62IXwntugPXrNAuMl7U2dWMGr4i0KNL3coUbSxUbD5PLvM_wqDvmsdMyFcEfakivEx0LlqC4j4pK6tXNNN_Z2YZnLIKQkAaoHjqEUVpQJfazmJ-LBEt034CDaKzIvaOs2Vlb54xrhVhQn-X0jhVG8XHG9zTpZMcN4CbhawjDG5NJVSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
👤
#اختصاصی_پرشیانا #فوری؛ ارگان‌های امنینی و نهادهای‌ذیربطه به علی تاجرنیا رئیس هیات مدیره تیم استقلال اعلام کرده اند درصورتیکه فرهاد مجیدی تعهدکتبی بدهد و در مصاحبه‌ای عذر خواهی کند مجوز فعالیتش در لیگ برتر صادر خواهیم کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.1K · <a href="https://t.me/persiana_Soccer/23337" target="_blank">📅 10:46 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23335">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/29987e4127.mp4?token=X7O1QNKpaikdjVsvolIoeSBCNxOWQA1ASRZY0b76jyHyebQZUf6sIHqGcWrMPXFdmnjhuMecoAVItK96ou-hYt6Evyx1TN-UfCYYAbrp8qtedcBrdhwTcGPjttw6SSDJvQf9TRRxsTXIAfe-wuqjfQyHQj3qXdcmaUFhSkDHZzzcsS1Amg5gIdEiM3pHTJaB_J6i0tAqlC9uNM_-enICIzfnWf2Alj40L9inyBH5oIm7QyB3-Q4xEA97ZbQ0Q_ZwgRHWmcfIKIs3_HPwH3fj_ePgv9wBwUQGC3q35jNuOHHcUNTOUVB-MxRUfdyzoN4tJJIHj9mCS24eIe62QW6PLKQRhc-9h3adD9IyYYdMYID7fO6HujMVQ3PEvn6GU8VO6DTz3CbAbt3Em5Gkc-9_oUknKZaNte_H98r3OQ-qMF2gjETphc_i9lPdTXKJgAhFbkQEC-P8rmdsPsiVy6Znr5GQXZnrM77Gqf86lGzbCUFu7dsIqHtV__j0Pj2u5VPAC8Gt1-_8JmC6XGuIHPZ5VUlGqcPNM7ySaPWhPQ58bWgCrIobwx9s-ceDy82ha76aJ0VWSxBzrN3MAo1SZNBLrC6wxuM_WiVsY9j4ZdX2AXjENEk-8h3aJ6d0szzzn4obDUGbwnFh0vwyzTg-0fbEWBhwafQ51LcgCwBBKwN_2Co" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/29987e4127.mp4?token=X7O1QNKpaikdjVsvolIoeSBCNxOWQA1ASRZY0b76jyHyebQZUf6sIHqGcWrMPXFdmnjhuMecoAVItK96ou-hYt6Evyx1TN-UfCYYAbrp8qtedcBrdhwTcGPjttw6SSDJvQf9TRRxsTXIAfe-wuqjfQyHQj3qXdcmaUFhSkDHZzzcsS1Amg5gIdEiM3pHTJaB_J6i0tAqlC9uNM_-enICIzfnWf2Alj40L9inyBH5oIm7QyB3-Q4xEA97ZbQ0Q_ZwgRHWmcfIKIs3_HPwH3fj_ePgv9wBwUQGC3q35jNuOHHcUNTOUVB-MxRUfdyzoN4tJJIHj9mCS24eIe62QW6PLKQRhc-9h3adD9IyYYdMYID7fO6HujMVQ3PEvn6GU8VO6DTz3CbAbt3Em5Gkc-9_oUknKZaNte_H98r3OQ-qMF2gjETphc_i9lPdTXKJgAhFbkQEC-P8rmdsPsiVy6Znr5GQXZnrM77Gqf86lGzbCUFu7dsIqHtV__j0Pj2u5VPAC8Gt1-_8JmC6XGuIHPZ5VUlGqcPNM7ySaPWhPQ58bWgCrIobwx9s-ceDy82ha76aJ0VWSxBzrN3MAo1SZNBLrC6wxuM_WiVsY9j4ZdX2AXjENEk-8h3aJ6d0szzzn4obDUGbwnFh0vwyzTg-0fbEWBhwafQ51LcgCwBBKwN_2Co" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
چالش جذاب هوادار ایرانی با کیت های تیم های حاضر در رقابت های جام جهانی 2026
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.4K · <a href="https://t.me/persiana_Soccer/23335" target="_blank">📅 10:42 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23334">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c684a93218.mp4?token=XZwRbBaNv0n7_9wdrCaVUXTQ3zKdSHNvdMwTUWqvKFu_kCn65zTTTUOsZ2X0SasCUVv67s3ExwS4S9_BqECBkldsGp_nXN62OhQRqMATa09yVLkDr5M_FRYtUuWqrssLQPKCtdLxJuYlxoQ9b4odeRibosWh3OkXjxaIdZOlSHAfPiKtbQFEUBcHSlGSCSpZkQXLQ82mg57r66eQqSS1Qpnz8ZOL-qcA9dzEHK4JO-jVuUWFURbgfFx17kHE6GcWnkOWJr1UWYgWXyI4iPx2XoLxdoIw5anu6cygfLsgT_HxEoRyqLaSpmJ91eG34bCe19QGlsMKGF13G6DjtxzfkQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c684a93218.mp4?token=XZwRbBaNv0n7_9wdrCaVUXTQ3zKdSHNvdMwTUWqvKFu_kCn65zTTTUOsZ2X0SasCUVv67s3ExwS4S9_BqECBkldsGp_nXN62OhQRqMATa09yVLkDr5M_FRYtUuWqrssLQPKCtdLxJuYlxoQ9b4odeRibosWh3OkXjxaIdZOlSHAfPiKtbQFEUBcHSlGSCSpZkQXLQ82mg57r66eQqSS1Qpnz8ZOL-qcA9dzEHK4JO-jVuUWFURbgfFx17kHE6GcWnkOWJr1UWYgWXyI4iPx2XoLxdoIw5anu6cygfLsgT_HxEoRyqLaSpmJ91eG34bCe19QGlsMKGF13G6DjtxzfkQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇩🇪
🇩🇪
بازیکنان‌بایرن‌مونیخ چندسالشون بود وقتی نویر اولین بازی‌شو انجام داد؛ منتظر کارل بمونید:)
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.5K · <a href="https://t.me/persiana_Soccer/23334" target="_blank">📅 10:42 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23333">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">💛
هنوز توی MelBet با این همه آپشن خفن و ضرایب فوق العاده ثبتنام نکردی
⁉️
بعد میاید سوال میکنید کدوم سایت معتبره
❗️
👀
اگه میخواید توی شرطبندی موفق باشید و درآمد کسب کنید در اولین قدم باید سایتی با آپشن های بی نظیر و ضرایب استاندارد و امنیت مالی بالا داشته باشید
✔️
🎚️
همین حالا از طریق لینک زیر ثبتنام کنید و وارد دنیای جدیدی از شرطبندی بشید
🆕
🎁
کد هدیه 100 دلاری: Sport100
✅
معرفی سایت و اپلیکیشن مل‌بت
💛
ورود به سایت مل‌بت (فیلترشکن خاموش)</div>
<div class="tg-footer">👁️ 34.6K · <a href="https://t.me/persiana_Soccer/23333" target="_blank">📅 10:42 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23332">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XRSSeLDV_NlxODcFu-GrQke-f6Uxy5mdShrVO4va64TxWMXRCVQKfVgqa278TRJs4GQ9l7wG1cWkzt_3v7wp7g6D7sH9CSjRh5Ppxndit_puiXYr5xq8cwgHsZAkHIp1WnNNoax4nx9oCp-GY7J8QgH_kgxeE6R7IaddQNh1TipKUf_5h-loVG5c3KQKkYaqoJhLGteYayBJN_cO9Hw2XHYgGcSk8Uh4EYhNlZv-ucBlBQfKgGKif2tktkxtQR04llmRDTJZzrZ00O-B9T_Z4b7ZaBhjSquSSLAM5zP8_G8ZVAWjbrqn5iC1StTrq69WOzKBzNyFo66EqfrH6PCm4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#تکمیلی؛ طبق شنیده‌های پرشیانا؛ باشگاه استقلال طی‌ساعات‌آینده مطالبات یاسر اسانی ستاره آلبانیایی آبی‌پوشان پایتخت رو پرداخت خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.1K · <a href="https://t.me/persiana_Soccer/23332" target="_blank">📅 10:21 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23331">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">✅
هفته اول جام جهانی 2026|آتش بازی یاران پوچتینو در گام نخست‌ رقابت‌ها مقابل پاراگوئه
🇺🇸
آمریکا
4️⃣
-
1️⃣
پاراگوئه
🇵🇾
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/persiana_Soccer/23331" target="_blank">📅 10:11 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23330">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ADEEQ6c3ba7xVz5IuWPj_R1dyYcnVP19uwI-v2sGT9Fo_Qv5UN81wTBAmsrs-rsRzsUzllZSGloCAnr1O7zD4-vrvdvCyzVtNTqEjfJQJ8YaisxzS2ln7-uGrwi-bXfK0anPJgtSXEA_EXy2fJu4WhJxuU4ySGIKaBmgkmge7MTseNqVFtkdv7g1kH3G52gp8lpjnn9QMDfDsEhfc7VBWBUknpLvAoHhq_GLHjC3ppHGTXzWT06v3iH6t7G80byG6zauFixO9nxtZqOJXnpM3UTu-im3VwZh6mKgKreciGmpJchsFyoEIWo5rEnYxI-x1gz1NUPR-pUeI1xF1UtcDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
هفته اول جام جهانی 2026|توقف یاران ادین ژکو مقابل یکی از سه میزبان جام در ایستگاه اول.
🇨🇦
کانادا
1️⃣
-
1️⃣
بوسنی و هرزگوین
🇧🇦
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37K · <a href="https://t.me/persiana_Soccer/23330" target="_blank">📅 09:52 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23329">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5291a03c3c.mp4?token=kol1gJTsyzmeSzfjw6-soU6_EBYrJVpMdDzhUyh1azzwRI6ZSACJPv28ySjM8u--qcRpu_u8RZN0YwVIIRFIPZWVEFkJOYaKXab3ecM5JRLDyX-5hH7m9cxcGwLtdJh21YMGCuywTT9oYsl1FIG-sSD3honwQJcdOsGAkD4NDplQ6BjFzxN6QeYwcPbnJbq4jKE1ILFCTvcyzJhJyqeAJmSuOI4_QA92JXpWxILY4Ke1l8XLMtVczsIm8012NrZ-Wy9kQCq0OxVyYddB7s4Mf3UaFIg-m4E-vOpxQOi2Y-GZpb7dvMxizVh1kacVKN1PW63_8Xw-Nz0pbtVahyfASw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5291a03c3c.mp4?token=kol1gJTsyzmeSzfjw6-soU6_EBYrJVpMdDzhUyh1azzwRI6ZSACJPv28ySjM8u--qcRpu_u8RZN0YwVIIRFIPZWVEFkJOYaKXab3ecM5JRLDyX-5hH7m9cxcGwLtdJh21YMGCuywTT9oYsl1FIG-sSD3honwQJcdOsGAkD4NDplQ6BjFzxN6QeYwcPbnJbq4jKE1ILFCTvcyzJhJyqeAJmSuOI4_QA92JXpWxILY4Ke1l8XLMtVczsIm8012NrZ-Wy9kQCq0OxVyYddB7s4Mf3UaFIg-m4E-vOpxQOi2Y-GZpb7dvMxizVh1kacVKN1PW63_8Xw-Nz0pbtVahyfASw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
تیکه‌سنگین عادل‌فردوسی‌پور به امیر قلعه نویی بابت ساعت دستش در مراسم پیش از شروع جام.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/persiana_Soccer/23329" target="_blank">📅 09:40 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23328">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d5d11f7375.mp4?token=B9NDDfvbGYzhh9UUudZKzXs5gAUynPkGoLoxcFxsJ5uZPIbeFXJv3SpmnpD53VYMa3KCBERVrusnMCVsVZ3QcE-U3v9uWh9PEqPtyoQSofasQE68PCXX317-a3eZvCFDqpMd8wRepZ2LDXrL5GFRLoYDJ3blH8gChS1E4hbsZ5GrWkYaUJJyRt9gg_k9OUAG-PvAhm5xuODhZzI-XK2kgg0PKDUrM-WtDpg6ILQZolF_PPSt-CskAKVS5hfwl54IaoIp--F-GsYrBZ41YJJlGnRckwD-XrVIxObTQNz230vRyOGvBFVhoJlT724zgoz_CPpADonrpna7oBwUzvfZeI-c9C7rPayOKICqRphd_vm9iLtql_dW-eOQWC75gbhfzmnJum-mh1A4dQtx9wnDkRnB_bH4UR5_s3Pgustf4R_O-fEj685OkHmoanDWLyf86IAlcXsjNvr354YoWlhxBoJXJg-O5ARw9hG_6lLytVAY9ZJM-389cu8157cbRjA7csPqiC1W40tIgDAOs1BE2XWvZajjRs43H9AA0hL8rwnSjmS_s-zwsfXJoDT0XmU_Vf-8Goevp5QPoReuPGGYxZdR__RBoJcvX-W_aPeb_DwxuHTBZZO6_Y8AdAZjIYfgtQQfWyPLQpRKjjXbb9KHisOqBhFupmH9TYxSmKR2zlA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d5d11f7375.mp4?token=B9NDDfvbGYzhh9UUudZKzXs5gAUynPkGoLoxcFxsJ5uZPIbeFXJv3SpmnpD53VYMa3KCBERVrusnMCVsVZ3QcE-U3v9uWh9PEqPtyoQSofasQE68PCXX317-a3eZvCFDqpMd8wRepZ2LDXrL5GFRLoYDJ3blH8gChS1E4hbsZ5GrWkYaUJJyRt9gg_k9OUAG-PvAhm5xuODhZzI-XK2kgg0PKDUrM-WtDpg6ILQZolF_PPSt-CskAKVS5hfwl54IaoIp--F-GsYrBZ41YJJlGnRckwD-XrVIxObTQNz230vRyOGvBFVhoJlT724zgoz_CPpADonrpna7oBwUzvfZeI-c9C7rPayOKICqRphd_vm9iLtql_dW-eOQWC75gbhfzmnJum-mh1A4dQtx9wnDkRnB_bH4UR5_s3Pgustf4R_O-fEj685OkHmoanDWLyf86IAlcXsjNvr354YoWlhxBoJXJg-O5ARw9hG_6lLytVAY9ZJM-389cu8157cbRjA7csPqiC1W40tIgDAOs1BE2XWvZajjRs43H9AA0hL8rwnSjmS_s-zwsfXJoDT0XmU_Vf-8Goevp5QPoReuPGGYxZdR__RBoJcvX-W_aPeb_DwxuHTBZZO6_Y8AdAZjIYfgtQQfWyPLQpRKjjXbb9KHisOqBhFupmH9TYxSmKR2zlA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚽️
طرفداران‌کشور‌های‌مختلف حاضر در جام‌جهانی؛ از سری جذابیت‌های بزرگترین رقابت فوتبال جهان.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/persiana_Soccer/23328" target="_blank">📅 09:20 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23327">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">⚽️
ویدیویی‌بسیارجذاب‌ومختصر و مفید از مراسم افتتاحیه رقابت های جام جهانی 2026 آمریکا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/persiana_Soccer/23327" target="_blank">📅 09:05 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23326">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sdwWoXHDkym3LLD5UwIwsLubQmA4Ua8jEP-3yMkzIY8bOBQhPc-c2Nc_Qz6aaA6jcfE98ULcLBTDp9avVcFgozp4vc50MueQpp7Y4fUsR3hGX2mfyldw7Ekc03PHV7ws4o3iz3IKG_wsCodBPuvZZfs2-Xq5Lltxza-uKRMS7ozDoucVMy3xmjL4HwyDKmDdEQLskwMA_jsa3LRn1e9kXQUopp4qnSqF26D2PQy6ITkkMA0U9gO9btVQw5na2GbwPkd_hSsVZE44HfNjFB8yg5IsTAfurULZq1VOnPZGp1vjKD0q7f4PwUVhsa2DgqPmHJ-UDDb7iKgZ3H2FsaUfaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
حال بازیکنان تیم‌ملی والیبال تو بازی امشب اصلا خوب نبود. این صحنه دو ببینید. باهم تعارف میکنند!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.3K · <a href="https://t.me/persiana_Soccer/23326" target="_blank">📅 04:13 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23323">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Lz6Lvksjl5JCLwWpd6JBCvZkbLbdOXlkmqNnodw9qxNZMi4udFmgB106iOb6QMdBLTBeIF2OsjKz3-pk6chC2aM0vwTXSlDs8Q5r1rp_jbaN2wS8RwNxKlKlgHx2KqLN7dRA1jCzMbYJvrwKcQP2l8RRrVct_JG7UEaSrojqBX9rJxgZDQBZbhH-jY0bBhpHMyX2rA-0IwOXy0WefZ_stGVV-DSAoJoDfuhdQTSgM-hf8o8bRAaaXdua2W7yKmF3BGIPx6167sd2jGhn8OzrpDKdbs9OJJwkNxudMS-mnasffdECuTY-1jBREyxr-839mwty5l4AokH3Ihp6dmWEYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/StdMVAWGXP1cA1xJdIdXC55Nz6soXd8j-L8koLLiLkMoAu5dJqssEXkPktVXzC88SBgeowS-Uhnk9WrlPRo3nEB1ZSUR_OsvMZLhqRvUPEJQjjPMAy6AtdfsFbYU1uK46MPwFtQl7HzbR-5Y1EJrxVI382KRpM0ahMQU5IH-46maDbv-MyYnfILy6irFbO0pyUL1Sbbm-g68ejaQGGEsZMVKxtfDPfL-aLX6AJJRnqhSd0-aghQ_O046kJhO9y0_HdHPy6Wzv9hChv8QbcMj7dmPA9NumWgEGOy5tdODMy4UjWOj2_qubwvNhGlfS2lxZwbUCBMJFOhR1U_OkEsTkA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
امنتیت بالای شهر تیخوانا؛
در ساعات قبل رو به روی محل کمپ‌تمرینی شاگردان امیر قلعه نویی یه جسد توی صندوق عقب یه ماشین پیدا شده که در حال تجزیه بوده. این ماشین هم توی پارکینگ محل اقامت شاگردان قلعه نویی بوده که دقیقا رو به روی کمپ تیم هست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.5K · <a href="https://t.me/persiana_Soccer/23323" target="_blank">📅 03:07 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23322">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Erp3GwTL-ivj12_3JnQTp7wC6I7ILVINiJrZNFPETAJaRAsxoBjJw7pWUGRMKCtkIM1DFqQpSsp_A5PyL1_edzU5KOuvKlzSsJsSamu80WHnfwgK2ipNhJfW-CydfbXR-gLsMMCq5lDvTOlrWx0EMSEe-fBsfiF-44LqrRdBZ6M7-mdvGyvmR8B9C1tjC8CLJuBwqEBQkHIki3MNK8YP1C_sKwtP5iYKCx0TCb2_wIj1PtXirBvBvXRuVWcUzweBeWSxKlrSgdFDywJ609VfBTjhhWlg-Kmvt9fH7YjG8wlEnraEcFvY6qMvBio4xj1-0TduXrScbgSUi-Zw1_4XVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇷
👤
بااعلام‌کادرپزشکی‌برزیل؛ مصدومیت نیمار جونیور رو به بهبود است و این بازیکن از هفته اول جام جهانی دراختیار کادرفنی سلسائو خواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/persiana_Soccer/23322" target="_blank">📅 01:59 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23321">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OhdXb8hxqpL9pkETLTT2d0NA7m6zj23zjdO6YnuFUWJrJeHcCSQ1by19sSaH_JgAZU8E9oVAhcd9lV92I5C2_T6eOM6of-lKKnHrjnP5urMrvJ-GNHapIEqArdB-KAxdnmwRjyqQyccd1MpnUEwi4eftcmHHy0WbQyitCll7nb_UML4tIUXUxdoDYi8H5p6DplcIa3jJhkN7nENVVBa8n9mUQXbfOxQTPM6lvMOv3VEWqZbzgmqLrXODjc6A8CxU1BgytHgB_-esnqzD__NSfECA_KQxd-UDjllE-3n-QPgd1_Sub4mMpgMbvg-Z2nxN--Mxl8yrK1RrdPUBBBecXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
#نقل‌وانتقالات|نشریه‌موندو:دکو مدیر ورزشی بارسا بزودی با ایجنت بارکولا ستاره فرانسوی PSG جلساتی برگزار میکنه و پیشنهاد 50 میلیون یورویی به PSG برای‌جذبش ارائه کنه که ممکنه قبول کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.5K · <a href="https://t.me/persiana_Soccer/23321" target="_blank">📅 01:34 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23320">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">▶️
قسمت‌‌ دوم‌ برنامه‌فان‌جدید ابوطالب حسینی برای رقابت های جام جهانی 2026؛ عالیه حتما ببینید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/persiana_Soccer/23320" target="_blank">📅 01:23 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23318">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fRSC8X5hT31wnTQ2qpvg9wwETR0Uxo6o2YC2UpEvvbY7jvf2-mVqDW_YoKCgPX-nh3bV1Q8JE99eBsw80jdxFq6M9Zi7n3cwbc9mnFiJz4IkWR67AhFqHf9AdTi2kURg-uwNIoUYPCP9Wn6lhbxWBcRuxCoqUrNhtb2okOrCHm2aEcK0DRFyRUkSJU6sb3BWYbvU9pbDSPPw-3kXwTH-k-k1BUewMyfKJtlWEBCBcCnU5PFL3hFVQ4JA2ef8-dQUixwkg9AhSu8fYYYqpNnmDdSC9wycn5bPoPtL02Hx8m61Z-T-Gq8w0hnW7xqdP2_won2js9ctvTdLeVLXSZJFCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌دیدارهای‌امروز؛
ازمراسم‌سوم افتتاحیه در کشور آمریکا تا‌اولین‌تقابل‌جذاب تورنمنت بادوئل فوق العاده حساس برزیل و مراکش در بامداد فردا
🔥
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.4K · <a href="https://t.me/persiana_Soccer/23318" target="_blank">📅 01:16 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23317">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c9wugEvCqPEos720gAbMfTS8YoAdpXxHT6kSt7q4LURqrTaDELCOmSqKjEc3GjeCInn65_gloQLVf9fRdRiFS8SfnsO9vxCvn3_iethm0KdkB0lgDWqbvsN6oXi4PGRxRnCXbdKT7v-qIJfj7arLkj16UBezssriyxGktn-S8jNlBlL9KTlNXU-fUpQtUismhUPjsdHDD7Q2_nyAw5Pko7T1WhDm6VIZNhSa8bk9DtrEmU9geizgwXc6ZRwTx57tGt0fkIA1661D6e-iA9JfDe18L2rVHkpB_CW97DtEBMH8JzfXhga3CHrSbiaVIhcBRNBStTc77ozvB6s6XCYPZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌دیدارهای‌‌دیروز؛
برتری بزرگ کره‌ای‌ها مقابل چک و توقف کانادایِ میزبان در مصاف برابر بوسنی
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.7K · <a href="https://t.me/persiana_Soccer/23317" target="_blank">📅 01:16 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23315">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/f81I74RgRK_HL71n1qKuKwKaMaWKwzKBC67hN_HWpS6thL6VNRrS3hPbqIpIOamxvRWBhGoWkRGKApQDvL45gVo5JWM5e6CFrinTRXyWHLvUJxOQxn_xKYMozvcw4CpnyuRdEokhVVCKdw24XAgvvrnDLMtSE2-9j1EuLALxR6N1TT_hO6ScyxmNQUjInOLt3C-poBG-CMkphCgt_JIgvdjrbTXRUUCwaRBy8xG2z87HxLL1KIFfQAugBjFe8yN_8Zitm2nXzhkdZ4lHoIrhfEv2PrmXYy5NAm7BahT_AnKNve3uwcJ9dtLIDkcNEtsmkWwBP8VUPeW-wXp4O6Rb2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DGHaOK4ftb__ALZj33rshLXD_Tsa_OUNKPI_vbUjk03njN8jJkvLfzcDzDmMhBHWbmLx5ULiJmUYZvs7keOdXSoLRzTMpmLEz0Jd2cIAVc6Dw6bjOA0sTvPERF5gGlDUJfOxsEnboN56mUv3R3gIo6G7zH5Gj7SMiIdiBBCyo4wjV_wchHShwjw3rQHjYMnBY6AKZUTp80DmpHqJNUhLV2eUTzX3YtLRMxLEL9vRx0SwIgrNrZYPLpjZoh2WLqRiS6918rLuXnvF-9lSPJvbzyTxyw2IAQl1iIB7_MYTuGtikSLkTQBy8Jr9xDxAvyivMXioDdaeFTyAD4MSXjh3NA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📹
شات‌های‌جدید نادیا خمز دختر پاکو سرمربی سابق تراکتور؛ ایشونم بعداز اینکه اینترنت مردم ایران کامل وصل شد پست هاش رو شروع کرد به انتشار. حدود 70 درصد فالوهاش ایرانین که اون سه ماه نت نبود اونم پست نداشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/persiana_Soccer/23315" target="_blank">📅 01:12 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23314">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EUQn4dBF35W1rrLDNI9AUiMqKN0o-ALdVix8L7P2kbOSDCwVwfTi485DOAZ-EHybwgtJKJUf1Qs2UO-acih-4m0Mj0p3YXrAXmRNVjp2nkbavYbk0iPdI16H8t5-MTTPNKtTD4XOotSMpg_ZpGcb_I2Ski00GpHauRlSCyW0Wy2KTuDM7BuX2urhOXLCLhIud1edozt3JFaEL7yRvoiOsBM1DbjKovkPzfVAqsKIFH1YdZccrYIl_zCjEOCDn46TnHrHTWo8pzP13Wkz2Yg93o_Q8A8RIB-OzECOtH8CMk-4IalleMJYowbv6tVcPPdIxZDBe1Qdm6BvQt-aFms-Lw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ رونمایی از استایل جذاب و گرانقیمت قلعه نویی دربازی اول ایران مقابل نیوزیلند در WC  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.7K · <a href="https://t.me/persiana_Soccer/23314" target="_blank">📅 01:12 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23312">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l-q1dT4qpgbtaY5VlJchqnrLDE-JSQ13wRPcmrEd7zqg_wuCLRcpHH46HUbCkeeYnGsjuJrhl2mt00ZjWqUwzvU_XlengHPS4KIjPY3hVUPD1YMsFp5h4FOFKxM8tslaiAqv_AapN6jBCumx4EzQv_QhJaYmOic9vjW7BW1nGuaSZdyXGVkWYgVqTeW_VlkY8KwiGZbdnlTzKXEt_HNMKeruC05iAO9Rg-Y7zKUEPpcahrBz6f-790DvEZOzl3_z0-5nLy6NVeEzuy_U1jMVEA-JDOXxvtK_r7h1jtVGIJG3rN4EhIUHpTXp19_EhE22JzKl07Rsryq8eyetHx--Fw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
میثاقی‌به‌منتقدای‌تیم‌ملی‌روی‌آنتن زنده:آدم مفت بر از جا خالیی ......تره! همون شعر شایعه رو میگه.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 40.3K · <a href="https://t.me/persiana_Soccer/23312" target="_blank">📅 00:51 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23311">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d8e109d357.mp4?token=q_Jlju0PKUQAGL2RyoltSK6RILEPKMcV7N94-3F2kJCs5rKLvqKcklauQY7onBqTyIJcKq84mA2ezi3bEvstDJVOqf8_MCZFyUInhaeZGOlW0uR141fWM_3dd3RLRUlh1pba1okK759-imZ8GWIDtRpWbrBOF7AuLfJ9C0PmgCSZinplOM_aYZOz9SLzhl0ccfHU0gXjbe28Hd7fzAkN00oinHoC__VfXDCGOf75dwljhAKJZvh2O-1lrFZb8bfLAV-i-pfm77xIZ5raGeNSbWl5TZhuFe7GbEU67geEDLq3jBlZ__kValcTmD0j7csKY4V23Sm5M4txSmwN0sJtcnAnXoAJ0885HmhQC_A-hlyEsnQ3c1MqOvxpz-PKosVlWrUUR9B06UK2U8LwhjLTuZBRh1gy3qK7zBXtUX25kZfaE7FPoP6UlbUTvFrmUuLRFES57oFa2V421QYqIXD1J5ckjqJkU_G5Me1U-j0vSnFHyr9CFZTF5UslckmfdmBHe1dLBSgnWl-P9C0RcydTj1tOugepOk76NiP9SxyBlMDzflvrICvhUinzoO22yLfxx8bGEI0dsA-W-jCSjI7FiMzJt_PiLL7KqTJ39WJIdCHHqr56vQ6echrfu7aGU3-bzCSoY49dosT1uFmPGEPNzjFvsnSA0who0me6kC01LcM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d8e109d357.mp4?token=q_Jlju0PKUQAGL2RyoltSK6RILEPKMcV7N94-3F2kJCs5rKLvqKcklauQY7onBqTyIJcKq84mA2ezi3bEvstDJVOqf8_MCZFyUInhaeZGOlW0uR141fWM_3dd3RLRUlh1pba1okK759-imZ8GWIDtRpWbrBOF7AuLfJ9C0PmgCSZinplOM_aYZOz9SLzhl0ccfHU0gXjbe28Hd7fzAkN00oinHoC__VfXDCGOf75dwljhAKJZvh2O-1lrFZb8bfLAV-i-pfm77xIZ5raGeNSbWl5TZhuFe7GbEU67geEDLq3jBlZ__kValcTmD0j7csKY4V23Sm5M4txSmwN0sJtcnAnXoAJ0885HmhQC_A-hlyEsnQ3c1MqOvxpz-PKosVlWrUUR9B06UK2U8LwhjLTuZBRh1gy3qK7zBXtUX25kZfaE7FPoP6UlbUTvFrmUuLRFES57oFa2V421QYqIXD1J5ckjqJkU_G5Me1U-j0vSnFHyr9CFZTF5UslckmfdmBHe1dLBSgnWl-P9C0RcydTj1tOugepOk76NiP9SxyBlMDzflvrICvhUinzoO22yLfxx8bGEI0dsA-W-jCSjI7FiMzJt_PiLL7KqTJ39WJIdCHHqr56vQ6echrfu7aGU3-bzCSoY49dosT1uFmPGEPNzjFvsnSA0who0me6kC01LcM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚽️
هفته اول جام جهانی 2026|توقف یاران ادین ژکو مقابل یکی از سه میزبان جام در ایستگاه اول.
🇨🇦
کانادا
1️⃣
-
1️⃣
بوسنی و هرزگوین
🇧🇦
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.4K · <a href="https://t.me/persiana_Soccer/23311" target="_blank">📅 00:40 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23310">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vbz3TH7qw5T1bK3hdaMl2VeRS169syFLk3kMrp39O4Lpf3tCx-cxGvBPRoTBYeB3k2e_bjM-2OQX1Hs4dP9k4st1fhTs9_yQ1uXpDz6qub3Yb0e_oSR-luIcWchEhxfJEU8TG_9Jgq_o1-X63S85BS3i4K2UGG85SMe_dFrLPrZLtowaBVCeye76xRLd98NjzSQLnoBm3iOhHQHOQy-TduaOco8R4M8Sq_G0OV_CUYGYe69-1-h2hAvXu0PjegHa9Zd8xnDEfldFBl4nMpstYHWkQr10vq8FIsBF1jwDlO1K8RzLIkThje5zQeRBqlLavwJSViLZwU04jBhMEJvUOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌اول جام‌جهانی گروه B؛ شماتیک ترکیب دو تیم ملی کانادا بوسنی
🆚
هرزگوین؛ ساعت 22:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.5K · <a href="https://t.me/persiana_Soccer/23310" target="_blank">📅 00:34 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23309">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vi-YUe5GVCz23xjTrb_ow-FsQLDXa_9wspnoWUTfKgz-FcxJgMZNEFwTZPSApd6B-p_tfD2Pt3bpxo5o-l-z06raW4jB_7Kc_ggGUmziXTye5g_RSeOVQIsMiYpMb0aYBvT2HA559gwP_H9Bh_JeR25PVlm4N1-srqcOTB7QbilMxVxhWvoXSHHpO-BZ7Zw_JSQx5_o9iw_8wy4KgOLukoIAqENqc2x6bhUgKIfjOoNH70_dAwjoeC4mOErqJP9DpR3SSg-jm1buG6JA5ndfdHeWDHLNQzQiOK5dmKKPvu-RffyzpRn0nE0FXkzoaPkV5vw1uOS4FQjLseH-09cZPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#فوری؛ نماینده اوسمارویرا در گفتگویی کوتاه با رسانه پرشیانا اعلام‌کردکه اوسمار علاقمند به ادامه‌حضور درباشگاه پرسپولیس است و حتی لیست بازیکنان مدنظر خود رانیز به‌مدیریت داده و اگر اتفاق خاصی از طرف‌مالکان باشگاه رخ ندهد او فصل اینده روی نیمکت سرخپوشان پایتخت…</div>
<div class="tg-footer">👁️ 40.3K · <a href="https://t.me/persiana_Soccer/23309" target="_blank">📅 00:30 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23308">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CxS9NfC9OYEAH8Y7_t6sb-oWSsEWF20ukfPAF_MFfO4e3vQXNOhZ03Fk_-bogRIkNrMreEsATJXIwj4kN8ADckStw5ASRyjEj8833FzDEDTErq5KUwn96KVuwttH3mRdjHXvTAoJHylSz9FbLQvT2ecuRHQoadK5uV1vRmA99Q8thqFeCdciKB5A2So5kh7vbXaBimduAsSiAjEGVb_k0jmrke3eucs5tBd3nD0sM_oyaw3nvGihPtR3is4xhrCTqXUViI-Gh6vzOdMVbCQY0fs-kSgJ9kcd8_eJcRiWEuXFpeiJG3dGsZ-orhQBvb-zfDJqnla01cMwmcqh1jTWYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
طبق اخبار دریافتی رسانه پرشیانا؛ اوسمار ویرا امروز صبح‌درتماس‌بامدیران باشگاه پرسپولیس اعلام کرده که به قراردادش با سرخپوشان پایبنده و به‌زودی برای پیگیری تمرینات تیم وارد تهران خواهد شد اما توقع داره که در نقل‌ و انتقالات تمام بازیکنان مدنطرش توسط مدیریت…</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/persiana_Soccer/23308" target="_blank">📅 00:22 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23307">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lj5vPaqIxfn0A9Bqe7VfN3gL022SL52v4Znlhx0ThF5a-uzzAmPJsityIQWl1RTs-zKWAOrzaPEltLgvfBDozHIhLgInM7VFTgQVPyJ3cxbPwCrIs2RtXnT4tmhUjqOeYBvkFAwqqyHM-0Ffw9xDPY_a64WTwS6K07S3uA7ONuUpeWnJElCGdRBjOSpwiWjSPPgxChLWounOB7VpCid0U2xwfCopeoWj9pIgXM19d2g5jvOvf4B1VlDApa4MLhu-EystwbXVkQWOMhB42FKSAudWB1mvWSCYHl2sc7T1jWj4cFTmlce1xNzLCh2WwU1p23d2Wv74PudQvyf7WSnHCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇹
🇮🇹
#تکمیلی؛ رومانو: نیکو پاز به مدیریت باشگاه رئال‌مادرید خواسته که اجازه‌بدهند یک فصل دیگر در کومو بازی کنه و تابستان 2027 با قراردادی پنج ساله به باشگاه رئال مادرید برگرده. نیکو پاز 21 سالشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/persiana_Soccer/23307" target="_blank">📅 23:49 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23306">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vCAzfd01iskjIJ30uU97vO33A9NRvauvftZTrECYtVPvyXV34JlyltC55jzJzSqs2vctZaYcekOFcmZWYQyk7Rh3TvsisKLWH0yHw-TDy_X52UiTlfjWkCTdjKWHkOXDpIBz6VB1UFkLIoGt1HEqNIkXmPUjnAEejKEBzqG-DeMMvjgAT8bCeMG5giKNqPiuCCc4q-NsjRfdpdEQ4h0fRyC5n0D-PXqjfRQ9Qb8_becxcE_az5OKVlDee3klDvxSrJV4ptuSMoWKEf9YsmkgdS8_ii8196rrAMde4M6kN9QeeKw6y8PFfx6k5e3vbXNoiALSfCeMLvMDJIyvjc1wLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇹🇷
🇵🇱
#نقل‌انتقالات|باشگاه‌فنرباغچه مذاکرات‌خود را با رابرت لواندوفسکی ستاره سابق‌دورتموند، بایرن مونیخ و بارسا آغاز کرده تا او رو به خدمت بگیره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.1K · <a href="https://t.me/persiana_Soccer/23306" target="_blank">📅 23:44 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23305">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3f8afd5643.mp4?token=AXJIkg3ILCWpxUkm2b0BTZPHtpLXg0XRvZTVEYLuQt27r0FGZVV7e_j3q3ZzPPAj4wyzCkkE4H678e7CJ4oDBHy-ZACEY0H9KKnl12WphKShBgGkAgJC2VeCJgx2nWSXucvuyt9J9YqkrWOS7pMpT2BbhW0rgmj8u1f0PvgkYoSZTlvm5BGsd5bJ8xE0CWpj_V53J1xGQy8rWdZ_F05T-sJx9sKjS9G37LyG-DJpB_fo56w-GK1cZW1CNRjgszfkUPE22SXfANZRg2PCDhA7xNE1r4M7p6l_I8i24Qo7vKaMHGS2YrC09yGt8sPOfHGfHKUBnu5OsH8TIb89FWHXGlXPdheHvhVc8Aq2S2exWHw9ZgK1LdP7M2aNEosjKDHW6hXt_aH64qLOrU5LY-BDukhsdRoCABPTR8oFpNT8R0XyB16tG37aTQiG6nNh3Y-matpOQwPVvCWCOrwa9MAifIxnf908Q52_5-DVmkU2xyTMsgtCq599dDRswmOhmsAwGZ09bVrQitS8GwguZVgh_AAWIOG98tDoAkKvolbB5AB4igV2P8DgmqPY1SfBV-eHaItY8ZzIjKHHSZX-Fnm9uGsW9kXjRmI8n6BFsWR-oAMTi1200HkLhW-MDS9yk0BZZ4IVpz7C0ZF4LJcNfhx3jwe9oIO9bK0DhIb6KrZdud0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3f8afd5643.mp4?token=AXJIkg3ILCWpxUkm2b0BTZPHtpLXg0XRvZTVEYLuQt27r0FGZVV7e_j3q3ZzPPAj4wyzCkkE4H678e7CJ4oDBHy-ZACEY0H9KKnl12WphKShBgGkAgJC2VeCJgx2nWSXucvuyt9J9YqkrWOS7pMpT2BbhW0rgmj8u1f0PvgkYoSZTlvm5BGsd5bJ8xE0CWpj_V53J1xGQy8rWdZ_F05T-sJx9sKjS9G37LyG-DJpB_fo56w-GK1cZW1CNRjgszfkUPE22SXfANZRg2PCDhA7xNE1r4M7p6l_I8i24Qo7vKaMHGS2YrC09yGt8sPOfHGfHKUBnu5OsH8TIb89FWHXGlXPdheHvhVc8Aq2S2exWHw9ZgK1LdP7M2aNEosjKDHW6hXt_aH64qLOrU5LY-BDukhsdRoCABPTR8oFpNT8R0XyB16tG37aTQiG6nNh3Y-matpOQwPVvCWCOrwa9MAifIxnf908Q52_5-DVmkU2xyTMsgtCq599dDRswmOhmsAwGZ09bVrQitS8GwguZVgh_AAWIOG98tDoAkKvolbB5AB4igV2P8DgmqPY1SfBV-eHaItY8ZzIjKHHSZX-Fnm9uGsW9kXjRmI8n6BFsWR-oAMTi1200HkLhW-MDS9yk0BZZ4IVpz7C0ZF4LJcNfhx3jwe9oIO9bK0DhIb6KrZdud0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
طبق‌شنیده‌های‌رسانه پرشیانا؛ مدیران دو باشگاه مس رفسنجان و نساجی مازندران در روز های گذشته مذاکراتی‌باسهراب بختیاری زاده سرمربی فعلی آبی‌ها داشته‌اند و درصورتی که بختیاری‌زاده با تیم استقلال قطع همکاری کند با یکی‌از این دو تیم قرار داد رسمی خود را امضا خواهد…</div>
<div class="tg-footer">👁️ 42.7K · <a href="https://t.me/persiana_Soccer/23305" target="_blank">📅 23:18 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23304">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">✅
طبق‌شنیده‌های‌رسانه پرشیانا؛ مدیران دو باشگاه مس رفسنجان و نساجی مازندران در روز های گذشته مذاکراتی‌باسهراب بختیاری زاده سرمربی فعلی آبی‌ها داشته‌اند و درصورتی که بختیاری‌زاده با تیم استقلال قطع همکاری کند با یکی‌از این دو تیم قرار داد رسمی خود را امضا خواهد…</div>
<div class="tg-footer">👁️ 43.2K · <a href="https://t.me/persiana_Soccer/23304" target="_blank">📅 22:53 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23303">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DRltrN7J5MeqhAzCjFPRsPB2Ry7HlKdSncweevnoCziLBygooPeOw-PSjdy2AG6rJnkbKgAG1ZtOCRskcWcjceBJWn4cyYxcNArScEqiF16mZcZ08pMhuoHlOcToNB-57Hjp4xVIgrk8WFRfr5fWEBp11Cvgm5AUr8qtWQS5PRxIM6BcLxTjs1fdljYO40O6tpofDC2M0oFrTvx1rK86sGN4FNGqNGFEDW7VgHtKo6RnHvugDeSqH1qnMSR2PrHyJU13hCaw_mJWB4kUo5LT2MvYHzgHIzKURZiEkytzHEazYRsmeVsjBBTBGuTjGkGn6mP9kY0axbnTa_KeCtj7qg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛‌طبق‌پیگیری‌های‌پرشیانا از مسئولان باشگاه گل گهر؛ روز شنبه هفته گذشته 9 خرداد ماه؛ پیمان حدادی جلسه ای 3 ساعته با مهدی تاتار برگزار کرده و به اوقول‌داده‌که درصورتیکه باشگاه با اوسمار ویرا ادامه ندهد اصلی‌ترین گزینه هدایت سرخپوشان شخص او خواهد بود.…</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/persiana_Soccer/23303" target="_blank">📅 22:43 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23302">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HVQW-6a8XI7WKCfiAYt1hNeFVSI5GdG7YRu69ZDGSgTC_J-IYAA3wyrJjTtgAWg7YfOkWFHruWWubY7a9Xddf6Wb_sgTQw7oD9Q87RtSSSxPQO-nn-ji661I8wt6Y7PT0uocDgqFllR1nTPVvkhsj7V1aOkMuhh8I83KtSlxAxGmgjnoCxCrFCKaPSXd0suYBysOdxSuV19txsjFWjmQ2OIwPcgq84hG24GeTlAS29OyJYrgLvlavqD4hOHiYIqUSyv1CyrgSW-xxVDOTtGip7JCbfgBTPYKpQHSfrw2KoAXo1qsGQHbURVq09tq9QwIgYcityjx-FEMk574kg2L_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
معاون‌‌اول‌ مسعود پزشکیان شب گذشته با سردار آزمون تماس گرفته و از اوخواسته‌ضمن عذرخواهی بابت استوری که دردوران‌جنگ‌از سران‌دولت امارات گذاشته بود به‌جمع‌شاگردان امیر قلعه‌نویی بازگردد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.7K · <a href="https://t.me/persiana_Soccer/23302" target="_blank">📅 22:26 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23301">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tzB0Oe_brdEFQAht_ghScxDEKV1Khp30jyvAXYiQo0BPaHyOlyV83W75Sryl3Nsu0NQpexfvVUt0Riv0xOEZSuc3ijulV3Py8BGRuCU_CdO3ju6OV6kerI4GX4xgQy75TgEpcbVPVCG8IsFY9GSQ-sT_eH0k1v0YxQabbBGxf_FVMP-WN-Mseuec2pqc_SKtcGB9AqsqTnsA7pABea8NPmNUn4t8tHV18iqPhz-phS6a8opIDs78Gb-eso9iqdPMGeA0pcXK8J7-87CAwEq3yhgotstjK-0hiLnxVvmqi6OIogDEVSg6w9a_DI5QbnAYBda5PuYeMLp6uk3rK6X6dg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
#نقل‌وانتقالات
|نشریه‌موندو:
دکو مدیر ورزشی بارسا بزودی با ایجنت بارکولا ستاره فرانسوی PSG جلساتی برگزار میکنه و پیشنهاد 50 میلیون یورویی به PSG برای‌جذبش ارائه کنه که ممکنه قبول کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.7K · <a href="https://t.me/persiana_Soccer/23301" target="_blank">📅 22:20 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23300">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OcH_rf-sFeBPWEKSnwzhx_XrrTmKZS66f79ZP0l7Z1QhVAn9jwu0O7rfgoWT_5pBtlosMurakOn9U4uqn2EBJt0jKJ96GF3l5wMwrhiDLk6tRKMcasjBCIcT3zi8d4vMskX1R-sxHTBxVaql5Xw7j_K_nGpThd6d0gi8xcr5hHErxJDhPDQeQGIyBhDkp3drfw7CxPAiU4b53Y3v0hZDUyh9HPYgk4dVI8LgSpFY4gdHCjOU4d-7ZnpWZHNMozYaBGK2uusUXKCdKv_Hp3XOf1cyQJ7Yl-BawulNvoKLdL2I6317gLWFUqGC58AgWqOzQ9IgFtb-5p_rKMZko3u7aQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#اختصاصی_پرشیانا؛ مدیربرنامه کسری طاهری هم‌بامدیریت‌باشگاه پرسپولیس هم با باشگاه استقلال مذاکراتی داشته. رقم پیشنهادی باشگاه استقلال برای دستمزدخودِبازیکن‌بیشتر از رقم‌پیشنهادی پرسپولیس است و الان‌همه چی به‌خودِ بازیکن مربوط میشود که کدوم یکی از این دو باشگاه…</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/persiana_Soccer/23300" target="_blank">📅 22:05 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23299">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3ed2c6f597.mp4?token=BcVRgdGOpOeCwXC5YXjj5sehooJq4urHwNi47wPc7duEM83xfilth79SEYWSipGC-OLls-K_rGmtZwWN9XVMfIEO7S1LUVzJSOyT-xpRtmymloeJEfbVkioLSSavS-6TNa5B25_mg8hASm7kXeCbETehucHVHox4PQ0lTk5LbYQqVdk8i-xTt_GcO7NeoKJVAgXCOxjV_n4I-QGUPFZpwBo-aOQ84z6pztzbSj0KnymFMGPj8guxNr8tYQbAV00hB1jSnJoaVd1X5whb8J9zpuvi141dXlAoPN458Yd9cNTcHLWkB56CS-ws1PrjL4zLErfWjfbgTX5fwnM3BTKLBTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3ed2c6f597.mp4?token=BcVRgdGOpOeCwXC5YXjj5sehooJq4urHwNi47wPc7duEM83xfilth79SEYWSipGC-OLls-K_rGmtZwWN9XVMfIEO7S1LUVzJSOyT-xpRtmymloeJEfbVkioLSSavS-6TNa5B25_mg8hASm7kXeCbETehucHVHox4PQ0lTk5LbYQqVdk8i-xTt_GcO7NeoKJVAgXCOxjV_n4I-QGUPFZpwBo-aOQ84z6pztzbSj0KnymFMGPj8guxNr8tYQbAV00hB1jSnJoaVd1X5whb8J9zpuvi141dXlAoPN458Yd9cNTcHLWkB56CS-ws1PrjL4zLErfWjfbgTX5fwnM3BTKLBTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇹
👤
دیدار کریستیانو رونالدو بایک اینفلوئنسر که بشدت طرفدارشه؛ دختره زده زیر گریه رونالدو بهش میگه اشکات رو پاک کن عزیزم. تو خیلی خوشگلی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/persiana_Soccer/23299" target="_blank">📅 21:46 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23298">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uM8DcrSBYlH5uqNvFIlAT4PlXGxNLwsAY7DfAR5SD0b8NAMgjwvWrlSvt75K_M8ityRk_eHAimZIg-8F7gtwaQw5El3WspmnraZGoU2HrORhTKRtY-LEtPZXlmoZywF6HkK8s4n1RuXwvMc4yERPDMhB6yM1UKRGnvurqoL3HJkITQsSN_Ar5TCXmoErA2r4g_wNWJYDA6EW8tsxW3l1W1s7FjrF3CtFqyqcNen59Nk8XmhV8Vd_q3c_074zu6uIQnfVYyxas6WSHS3eJte9_uIyl3qSym_AzHc88UPQE5aBCpeyzB0U4PL_6LoPKwjoeSWLhrKi591x_mhzp1KwUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛‌طبق‌پیگیری‌های‌پرشیانا از مسئولان باشگاه گل گهر؛ روز شنبه هفته گذشته 9 خرداد ماه؛ پیمان حدادی جلسه ای 3 ساعته با مهدی تاتار برگزار کرده و به اوقول‌داده‌که درصورتیکه باشگاه با اوسمار ویرا ادامه ندهد اصلی‌ترین گزینه هدایت سرخپوشان شخص او خواهد بود.…</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/persiana_Soccer/23298" target="_blank">📅 21:38 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23296">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GmZQS2_3My58-CRyQH1KaHJCRlGVJ2VCAhxlMu-BUstgn9AS4TqMCjWIr8ElgDCCUzSOYuNHa5dnMlzMMm_-7BefUxkETaUutOaZzMacGQu_fQ1j3ZWu0Pu3sRrWYqxxT8bTgiur7VaalSqdidLOOl6nlEAh83VerHnPrPq31JBUMqdViyENMKyklvLuKEBsaqWY6opvjpX53x9nNDClxYDlCwMkX271YM8X4wKV2fJORFjegTsGveZ53UYfT2g7fp1c4wqAqg7EYF7ttV99doIN__Cy23cS7L-DLDZ5dCcdzvHd3ACdatD64ugcio-D1zHEfP0sCvE6EB9f1UcN6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DFE4hwheDgHpxrWdpeHiVmqcA5eUkMJB3gUWNyNbVUAhaXLmRp0DcqKLBu-KvXrWl9l9M57C-gRPJRmzYVA-K0rPJBOT3Q_Qhwwq1sRYo6kpumbKin09kIMl8HSIbCdbqS0HmaOAsB9_tRm6PvdEfYvWbsi80Lh3B7q9v_dGh-0fw11L-QbuaCKw-O5elfekXTHRT9opZ6jCYOA26n9bmz1ldDEd_88ncbBs97n5JyeOO2WrW9NAJsfX6yN6ULO0EHqxak5_OogqX70wkZupeKTIJLVEW_fGRUcY5EERWY1h0c2xULWLyfJMYDsANHjle23nsrbdFWXWueGL2mCsGA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇵🇹
این‌مدل‌پرتغالی و فن کریس‌رونالدو روی قهرمانی پرتغال در جام جهانی یک میلیون دلار شرط بسته.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.2K · <a href="https://t.me/persiana_Soccer/23296" target="_blank">📅 21:27 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23295">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">‼️
آکسیوس: دونالد ترامپ به نتانیاهو اطلاع داده که زمان پایان دادن به جنگ با ایران، فرا رسیده.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 43.3K · <a href="https://t.me/persiana_Soccer/23295" target="_blank">📅 21:24 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23294">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GvjmSl7ImDeM3M232IqIp-0ulnE5lUGwTHjShfCbY7NN8EqW4nyxx8W8o3hPN3d0FooH5ZhOq_q1fcHqvySy5yLv1qFTqXkjmjAKnpmAAFzpa8SkCGmkHqz7Lc2RW8Rkg_3jiYtZZTW6jMQwc_MhZe5Fiv_D_4WwJW7tYcePIEUukNqQD27DdhRuhdxJFFh4QAC1sIFXXVsPd-EjBc04wmIk1dy42BPYfE9Kc2ZUfbqYwK6eZqv3XmChPakCKOGK1g96PYrk0lq2bHK_sSwyjL7gkaLmLGyuP-WkrrnEiTQMyY-7uOUaw3kvCcubcJJAwV58TcjBbsrC0rbKwhH6fw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌دیدارهای‌امروز؛روزدوم‌تورنمنت با برگزاری ادامه مراسم‌افتتاحیه‌جام در دوکشور کانادا و آمریکا
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.8K · <a href="https://t.me/persiana_Soccer/23294" target="_blank">📅 21:16 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23293">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3b49d10c6a.mp4?token=YRbaDABBEtPrANkJ7zu4kOgqF9JYAO8ylLc8SEh7bK2wcdvEOIBuFxSBP24SPcuHrktIEWQIzc9gZJIF6u1pzbEhQD8EM0ctuwrBmGcNNkuGLpP0uJ1IJ61YGLvmYXmV6S5fQlVzu52IaT54hnRBPAF3iYf01Nv5vtMiAZ_nvavZ5R_TwiUiGJH0B26Ol2cWtS-pKIEwAW_DnKBHXS4yVsHlJGxkwBeyvj8r4LBc6zCjcxe0JdH6rDqe6hc2JOcoVK3hE4t4wdrPWi3r78jIeRa5EkWjdEFtwbNsKQkUc15oWZ_daXcHmkfEaSyFYj8AciaTSitqeadzVzL4lrktsw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3b49d10c6a.mp4?token=YRbaDABBEtPrANkJ7zu4kOgqF9JYAO8ylLc8SEh7bK2wcdvEOIBuFxSBP24SPcuHrktIEWQIzc9gZJIF6u1pzbEhQD8EM0ctuwrBmGcNNkuGLpP0uJ1IJ61YGLvmYXmV6S5fQlVzu52IaT54hnRBPAF3iYf01Nv5vtMiAZ_nvavZ5R_TwiUiGJH0B26Ol2cWtS-pKIEwAW_DnKBHXS4yVsHlJGxkwBeyvj8r4LBc6zCjcxe0JdH6rDqe6hc2JOcoVK3hE4t4wdrPWi3r78jIeRa5EkWjdEFtwbNsKQkUc15oWZ_daXcHmkfEaSyFYj8AciaTSitqeadzVzL4lrktsw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
اسپانیایی‌صحبت‌کردن‌جوادنکونام کاپیتان سابق تیم ملی با پائولو دیبالا ستاره تیم ملی آرژانتین.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.6K · <a href="https://t.me/persiana_Soccer/23293" target="_blank">📅 21:07 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23292">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nUEg7yGsjK8W6T7NO4-jdiGaIofwvkE_gThC5HXblCZp6vzQl7yQ511WEkUYtFXu6PEe6qUMy89ODvKfXYwAL5XUYQgSwPPT4Xy6cbc2w7F6pFOIpFxXtWBJFjFJZUF5OMGqy-0sCcLrGivPh1dj0HNI8SK-BYFUD52h0GMpoydeZS5DWAnV4VuZcUuqBCwBHOX9G-RjdVGojDhm6AUsiqC1Z68ftPOnBpTH0NoTfyjZbapU6EolI8Z4JmSn_ukEHGsUZEHiWoZFKWoHDeon0iIsjycO2LOuLpbML3ni-HdZqje7-8hN_pBXQjsfnQUJ0WvWkccDXXe-yVbNruCGhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
گویا برنان جانسون هافبک کریستال‌پالاس؛ با لیلی فیلیپسِ پورن‌استار که‌رکوردسکس با 101 مرد در 24 ساعت رو تو گینس ثبت کرده بود، وارد رابطه شده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.6K · <a href="https://t.me/persiana_Soccer/23292" target="_blank">📅 20:50 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23291">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fCQ5Niy_XQb6vYI5JaIG8_gtq88KiJcVKMM1EqwG33c1fZUNx_MU0E4KAbHa8hSfuqmgTC4rcoD2qhztmqEJRq4bTY5753N1ZThP-DzOlzYeJKws3UG6jSlUBOIASf8CH8wdbbuA40jEu23-LPPplppaW3KMXnHdoDcC0-6LmHbF_RekDu-RtOR1wkxjKi2Qwq9wHaeiZJHA_YmzYSwD99jNUmKhmXJNLmaEYmmNPibpaVlDxYC0hKfoZlG5zpONc2NFMtRNOzPz6Bxfhe7oABPxPQ2t0MmXMnrBlhyS0hnIvyXfU9Vg-rI3DEaXi9uKNKfe9KKSiZMFv2XgY95W5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به‌‌ بهونه اتهامات جدید توماس پارتی یادی‌ کنیم از‌ زمانی‌که اگردوربین‌‌لپتاپ‌نیمار روشن‌نبود، اون الان بخاطر پاپوش مدل‌برزیلی پشت‌میله‌های زندان بود.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.7K · <a href="https://t.me/persiana_Soccer/23291" target="_blank">📅 20:47 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23290">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RaD1dWMaJdMzaehhuyBM_5Wps-dEFYlEdW0RMmRdxjGThQI7rGxSLp5FGIaEPRl_oKBD9xc53BVoq7Cn_-hHYh9VfDKXHq7ghuGVKWnuylelkgQlZ-eBeqi8BcHwbFY_-tS3jgy7DdpRDgupME2CO519Ml-bEeQtSPmXG5gEGnHxJkGvVnZ7F9Hj_f0RQIfp_04OFJdCBerIXM4x1Sty_lifeseHakOI37L56s5LE-UMQEtH49VC6zffOlFP700ZPSv-0ARF_JJGMsd9Qs22CQdhMH56AKQ3asXj7ichleN53hcGyg52PQnE-8bc-uZZc4hXENNqZ0TLYlruFvFu-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌دیدارهای‌امروز؛روزدوم‌تورنمنت با برگزاری ادامه مراسم‌افتتاحیه‌جام در دوکشور کانادا و آمریکا
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.7K · <a href="https://t.me/persiana_Soccer/23290" target="_blank">📅 20:37 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23289">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VWOxf2_nUve83r_oQq6543SS89fORbCGShkgzAk57qiNX9GGnduwz8HvvaO_dobVXawSI0IVsvPrpm48fF_-_OzT8Nt1afFzmz9gAaxmcfJXXJT8QuQwdLfMdnP1Ql--TJKF3KDoYYIrTACd7C7EtJl5mVdrbMnAKlRWInRiIpzOvjj3ku3jo3hQxktMptL693aT2p0YOG6vj9r6_-eYNbfEB5PuRRBOFnBAm4ER7GMk5I3n8ikB6fV2g3yc8MSActydZCURMntsa1O5nsKlazbCZCuHVqPD8Q4EzORQ-vDleSYBpnwy0j3pinHCDwV3D23YdwHjZ9s8lymqSXP40w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
#تکمیلی؛شهریارمغانلو مهاجم‌ملی‌پوش اتحاد کلبا با اتمام قراردادش از این‌باشگاه جدا شد و بازیکن آزاد شد. شهریار فصل آینده به لیگ برتر برمیگرده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/persiana_Soccer/23289" target="_blank">📅 20:17 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23288">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/omQ4YeG0n5rFzofNIU15z6XVtjk3vMk3wuLrM0KtuDdJUNUeGVK0IBuD1gHi17Yg-kYbyJJEzZS0AEyTLgOp_waarc4YcZGglWjSENm5s0YMWHj3pPvgXj-aSdWJEA2znlaAIl4G66phhORPpeJnT0EwNaIAvXcYEzGaKY1enadRX3n5Z1pZqLrcSt7LZcSqR4cTWI-ygfAn--ZcmrXXaueblWNdg1KfDCyrVb5yv-kKNOpkov8cZhydAA-rww_TXyKhw9u2d6Ixm8FfHxKNERV5Iye1jZ46ajP-56UYiVZPOoJwNJDzZJWYpxI59G_Hh_pYNdktqqozumYQK3HEdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
مدیرعامل‌تیم‌آلومینیوم‌اراک:طبق‌ صحبت‌هایی که انجام شده باشگاه استقلال ظرف یک هفته اینده مبلغ توافق‌شده رو به حساب‌ باشگاه ما واریز خواهد کرد و ما رضایت‌ نامه قطعی بهرام گودرزی و محمد خلیفه رو برای این باشگاه صادر خواهیم کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.3K · <a href="https://t.me/persiana_Soccer/23288" target="_blank">📅 20:00 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23287">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/av2AZM_UoiCcFNjSZRQ3L3zX67NcUlVYt57-wmyG2ybCNMiVCpsU9wxrxsYGqGcKoT2EiKbAbOj1KYaWYklVoGtskvcpIhNtiEHXsRL-SJWBVI0BHi4eFp6oCcIO6_8f9iCuCDcgOFBs5l7kY81jkgruMQg6vvb1I1Sh2uxiQbCiMJQ1t4VZCIKzYwon1naXlEL0Z530oRIRctdMfwKTaJzwc90HZaTCe5iiV8RM0KZqpvKTPHYT89rHj6NzL9rCYOMgdpqr2Rz0C6rHjz2t18eHsCkn0P6WbAOgNLzWW3WGjbXLv01FJo3P5xkoRL8MLhY9Y-8LcN4X3Q4jtkMwLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔴
#تکمیلی؛دوباشگاه استقلال و پرسپولیس با ارسال نامه‌ای رسمی به باشگاه روبین‌کازان خواستار جذب کسری طاهری مهاجم 20 ساله این باشگاه شد. حالا دیگه بستگی بخود طاهری داره که کدوم یک از این دو باشگاه رو برای فصل اینده انتخاب کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.2K · <a href="https://t.me/persiana_Soccer/23287" target="_blank">📅 19:57 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23286">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p71AdYA1uMcDeXm6q65NBnV1KAOmosC4XKZWicFoZ0VczYBCPCRWbmY1Ti4RhQud_LW4_zwSGqaAY1SlB9NvsctNBY22nKtf8QUMTp-kk83J4s9jEjOXZ2rFbv1KtPPHCYn99mxK3zy_FV62wXzcduZqmR2_mEr1fxdBUHO43BNDl48nGsxtg74qF4TjnZ6EgtDV2nlKGojKEZsEa0dE5vkyrHLbrga1369ULPYfhqe7TnGx1bS54R-zfAt9t6rZ2Z7UDN6_kKP4Jdrqh7wZz3b9I4yX6qPs-tUOcSGUYppZeY8-TCGFxTXFEBWfTYTVof2tMb5-gKmrbXFVAEyj2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
👤
#تکمیلی؛ طبق اخبار دریافتی پرشیانا؛ مدیریت‌باشگاه استقلال از علیرضا کوشکی وینگر 26 ساله آبی‌هاخواسته‌که هفته‌آتی به همراه محمدحسین اسلامی برای تمدیدقراردادش‌به‌ساختمان‌باشگاه برود. همانطور هم که در روزهای اخیر گفتیم تموم توافقات لازم با مدیر برنامه این…</div>
<div class="tg-footer">👁️ 46.6K · <a href="https://t.me/persiana_Soccer/23286" target="_blank">📅 19:55 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23285">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🚨
🔵
طبق شنیده‌ های پرشیانا؛ سیاست باشگاه استقلال در این پنجره نقل و انتقالات جذب بازیکنان جوان ایرانیه تا درصورت وقوع جنگ در وسط فصل اسکواد این تیم خالی نشود. در بین بازیکنان خارجی رستم آشورماتف، جلال ماشاریپوف، مونیر الحدادی، اندونگ و یاسر آسانی در تیم ماندنی…</div>
<div class="tg-footer">👁️ 47.8K · <a href="https://t.me/persiana_Soccer/23285" target="_blank">📅 19:49 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23284">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/46ef7ef7d1.mp4?token=ZrK2mEWa3GBwSz71SovQ5kDadJyQ3aS1plj8h7RhjiZXbXfAZuAebAlqRurAqdkAjFSBqwQltdpxG-48d4Fh7hxfnGdgcYgFf0-4OejYjNhj2NtdCwjvoATC6sSde_HBVfWMnbL_RQ2ojKh5MkeE4zaFmvzvJdpYLwE_7vvOPq4TpQlUuarScKJhEax_g6scRHsyJU1q_hAn9l2MUEVeFqyhRIyyNi5JW3qhsK0RxzGJbdR5622It6KhVbC9-bMmzLjU3i70HnlyxENMY44DJ_Il66e8oFB1PGM0F7UGXUdcUtNF1r5x4ckGUE7dRt2cl4qFUqf2YiMdJjS573_rhg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/46ef7ef7d1.mp4?token=ZrK2mEWa3GBwSz71SovQ5kDadJyQ3aS1plj8h7RhjiZXbXfAZuAebAlqRurAqdkAjFSBqwQltdpxG-48d4Fh7hxfnGdgcYgFf0-4OejYjNhj2NtdCwjvoATC6sSde_HBVfWMnbL_RQ2ojKh5MkeE4zaFmvzvJdpYLwE_7vvOPq4TpQlUuarScKJhEax_g6scRHsyJU1q_hAn9l2MUEVeFqyhRIyyNi5JW3qhsK0RxzGJbdR5622It6KhVbC9-bMmzLjU3i70HnlyxENMY44DJ_Il66e8oFB1PGM0F7UGXUdcUtNF1r5x4ckGUE7dRt2cl4qFUqf2YiMdJjS573_rhg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇹
👤
صحبت‌های‌جالب کریستیانو رونالدو اسطوره پرتعالی تاریخ فوتبال درخصوص جام جهانی 2026
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/persiana_Soccer/23284" target="_blank">📅 19:30 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23283">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gW3ZEH7-HC8KOExZZnW-nU07dMro7Q4jr7ARl9xeiUsfRpPf3Oj-Tfh42dd7tkLOYAKXksK1tHkDIoEgK5kBk0eYstTjK9N879gY28BmyEbhx-f9fZ6wjY8y-Jd_8o8676NEbOkxwxLS6gv6WhFwkPy_YmmTbT0QDNCmvQoEOlgMB8cQJNrMt9ofYCkU7OwOZzCim6rUFHyCy0__vJpZkE9pj48sAKOiHEpvix-JG5KSqdXb4Fyf9x00ndbxlwRdIsw_bFbdrVuushlzWO4Xuuv6ihTljU26evCEAV0DZ0RefCrBhEXLBtnhqVp9g_xVkQrXT8D3X6w1r3Z83HUJKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
ارزش ساعت جدیدی که امیر قلعه نویی خریده و در تمام شات‌هاش نشونش داد 136 میلیون تومنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.2K · <a href="https://t.me/persiana_Soccer/23283" target="_blank">📅 19:04 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23282">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/64a2fd248d.mp4?token=Umji-lijMvbZGXOlhHo_LjYlWyVhzxHFsF1m9wMn5C3RE9pvpLkCOpM1Mz6lCfISAEKxcvaRc_KabwMoUXoshfWHsQFJD1nsrmYxMCqG_hXdsb5UheOxTycq4iC5LkC8uLawLj43k2p6PcCpaXkOoiXVL_qBhdR59Z8m28ZQXr9E9l3OV7ke-C54t0m4Yzt8mqT3QFJ_nlGmX4pcgwI883rM9-plfclT3jjKrUGIUTSLNRQD0_IbA4lkTXC_KREz2SSfDKr9hpm93f0bl38okkdSo89Q3WMqyEjBK0mue6AtcibAINKCGGWMS_eQME5d7l2ux-0xu5OahLyQMn_Wrw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/64a2fd248d.mp4?token=Umji-lijMvbZGXOlhHo_LjYlWyVhzxHFsF1m9wMn5C3RE9pvpLkCOpM1Mz6lCfISAEKxcvaRc_KabwMoUXoshfWHsQFJD1nsrmYxMCqG_hXdsb5UheOxTycq4iC5LkC8uLawLj43k2p6PcCpaXkOoiXVL_qBhdR59Z8m28ZQXr9E9l3OV7ke-C54t0m4Yzt8mqT3QFJ_nlGmX4pcgwI883rM9-plfclT3jjKrUGIUTSLNRQD0_IbA4lkTXC_KREz2SSfDKr9hpm93f0bl38okkdSo89Q3WMqyEjBK0mue6AtcibAINKCGGWMS_eQME5d7l2ux-0xu5OahLyQMn_Wrw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ترامپ
: آتش‌بسی نقض نشده داریم به یه توافق فوق‌العاده دست‌پیدامیکنیم؛همون لحظه خاورمیانه. یکی‌از دلایل‌مهمی که اخبار جنگ رو پوشش نمیدیم همون صحبت‌های لحظه‌ایه. مغزمون به اندازه کافی سرویس شده دیگه لازم نیس صحبت های لحظه‌ ای ترامپ و جنگ رو پوشش‌بدیم. همینکه بتونیم اخبار مفید فوتبالی رو در اختیارتون بزاریم برای ما کافیه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.8K · <a href="https://t.me/persiana_Soccer/23282" target="_blank">📅 18:58 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23281">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oB2KcX6jv1dQIVbaaJiNehrLjaOAYC3Igm9976VO8BL5ZNT6jh_FYfsbmPxYO0Str6pBT_7Hbjj4JVUqxG589sb1gnzmYwLilXp68pWF0CHO7cqayDrkhlI6_0RMukpdVZt47rcTV_H2JmkRSm4Ia0G7glvzZ1QAEDugB2oh3mgUdx4ARqVZF69XgBWJtVh5ENrkQ5MyfrJZyNZg-EIqU5aUDXmYKL3YNy3w-8htyR1zRIJdPNhIQ6bNl4XXBWc4FVm3KyzJeYnGfOKi4U5HiM34ck0Ipa2jzb7n747Z8b2GpARj2isvz4qoCROn5vSuFPK8c0qBRfBFMYdYYtj7Eg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">▶️
اینجابودکه‌عادل مثل خیلیای دیگه شدیدا کراش زده بود رو دیبالا دیگه شروع کرد به تعریف و تمجید ازش؛ خنده های کاوه رضایی هم داشته باشید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.1K · <a href="https://t.me/persiana_Soccer/23281" target="_blank">📅 18:33 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23279">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/20d475f3d8.mp4?token=EL4Lg5vZysZMXMi2klCrZTBJoTLNyDux3JTaSGicexAU42zbdMchgaHAYVRgw0dQY3vQqZc3IX9oRtAZLDko6k-LuLIFrJpYyK89ZqBac0441txj8C5ZXA2i5noLVExgvfpUPoYnr_tOUpM_OQDI5moY-HC3K60iTAbdaKrCLdWW055dgJbTmn_WFhLlSdwdDPb5olLpMaPlcP7KYGgYO_ZiMfsBeNt3oMubXKk98Cj6zkDcfyFaBPJim4YeVZxYJ7LgYAz8DhTynRazE67Hz5-NnrGnVGOf24EgrGYo3Zfy2QGNhAEvTCmtKIfwagO_uizca4oDwyhnfBV6XPut5A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/20d475f3d8.mp4?token=EL4Lg5vZysZMXMi2klCrZTBJoTLNyDux3JTaSGicexAU42zbdMchgaHAYVRgw0dQY3vQqZc3IX9oRtAZLDko6k-LuLIFrJpYyK89ZqBac0441txj8C5ZXA2i5noLVExgvfpUPoYnr_tOUpM_OQDI5moY-HC3K60iTAbdaKrCLdWW055dgJbTmn_WFhLlSdwdDPb5olLpMaPlcP7KYGgYO_ZiMfsBeNt3oMubXKk98Cj6zkDcfyFaBPJim4YeVZxYJ7LgYAz8DhTynRazE67Hz5-NnrGnVGOf24EgrGYo3Zfy2QGNhAEvTCmtKIfwagO_uizca4oDwyhnfBV6XPut5A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇲🇽
هواداران‌تیم‌ملی‌مکزیک دربازی‌افتتاحیه روز گذشته رقابت‌های جام‌ جهانی با افریقای جنوبی
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/persiana_Soccer/23279" target="_blank">📅 18:25 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23278">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d34dfb18b5.mp4?token=qEM5R3lZTsDpAGWHHJzDM02726FtIm_0gT6c7oVBwvU5L3pVp7ykKEArAe2tolylyWwtLKzX0PJp1vVyG4leVVCvDmPs5GvvAB1bC-AYqlcl7jGGBpefmRaK8d_eD09UY5habr8MuqtrI1IrGNBsQiuZmOswEgIhD3IBtkk3yM0mqjBn5Is-DXkwE4NTy9yWa0xgeANMrbMWlvQIIa4-tzx80yZIIvBdvOxP2A6zL7xpPscfsniu7F7Zp8penGi7lBNW5Omz9K-Y_0kYnVskTsfZmHj-a0yUlRsdCN4IPOc8kUnCmL4XRIvHgM_2nZ_7vVQeDgMlZ4n_FR0mRwi5IA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d34dfb18b5.mp4?token=qEM5R3lZTsDpAGWHHJzDM02726FtIm_0gT6c7oVBwvU5L3pVp7ykKEArAe2tolylyWwtLKzX0PJp1vVyG4leVVCvDmPs5GvvAB1bC-AYqlcl7jGGBpefmRaK8d_eD09UY5habr8MuqtrI1IrGNBsQiuZmOswEgIhD3IBtkk3yM0mqjBn5Is-DXkwE4NTy9yWa0xgeANMrbMWlvQIIa4-tzx80yZIIvBdvOxP2A6zL7xpPscfsniu7F7Zp8penGi7lBNW5Omz9K-Y_0kYnVskTsfZmHj-a0yUlRsdCN4IPOc8kUnCmL4XRIvHgM_2nZ_7vVQeDgMlZ4n_FR0mRwi5IA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
اثر پروانه‌ای چیست؟
یک تغییر کوچک، جزیی و بظاهر بی‌اهمیت درشروع یک‌جریان، میتونه در طول زمان زنجیره‌ای از اتفاقات را رقم بزند که در نهایت به یک نتیجه‌ی غول‌ آسا، کاملاً متفاوت و غیر قابل‌ پیش‌ بینی ختم شود؛ درست مثل این ویدیو. ببینید حتما.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/persiana_Soccer/23278" target="_blank">📅 18:25 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23276">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TEFlKzxLzHG88ZL4oOnaLKu_Qpi_sdwmw3NJIDFqB13rrS9Ar9lM9eynvNoypkio3hV9XsZayWv5DioYHlTjJGnC--ezWWVuf7rv9Evr1U5k5ZErgo0PblOII6OrG9Sc_MtYoVdgHTiIcD10PphP8BpXy1u-OtnKKl63yKEeXlYhP95dyeS4pOp5NcvxdYwlcMPPS_H-sZiNvlxhbEjO0MufBhNoQTM0PiAew2-Mavm0hd7d-YMeH89MxvQr5RHdxTDDQh-yLWKmveIV6omjRIrU_cKjxndKKRf4IxCQskzQFV1ebBwe2LFyzKvo8bUsRJHXXMGn_xgWAqwc_HhGFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
#تکمیلی؛ طبق اطلاعات موثق به دست اومده پرشیانا؛ باشگاه استقلال افر سه‌ساله سالانه به ارزش 1.2 میلیون‌دلار به دراگان اسکوچیچ سرمربی کروات سابق‌تراکتور داده است. همانطور که در روزهای اخیر خبر دادیم تنها شرط اسکوچیچ امنیت منطقه است. گفته جنگ کامل تموم بشه دوباره…</div>
<div class="tg-footer">👁️ 41.6K · <a href="https://t.me/persiana_Soccer/23276" target="_blank">📅 17:45 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23275">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9833527b4e.mp4?token=LFmfA0coWKsy4uWsTA4NSQZLd6iNpgPSzugaba3tiqebo2ocnQuO0rhztB4xJiJXDzE5fSCpOfrwaAYQdmgB9u34iQ1aIs_XDvk3xs6D6BB1ioAubthEFFwQSF1vT5kWumME3_Z0aELOSJXXTwhL47ZySEf34YopYWDN0s6HWrUE8SDKUid_NvJdEZUAOapi7JpG6cXaEgmYYI1kfmvbi-M37896i9gNqdTPQQoUvw2HDUOrWgEX3yn2BsdD7fDB2of544rmL_cSdGnml2D7KVz_itjl7RTY0sIB5UZnNIFeLr6ynf4dZTEEsFa1NzhgmhWnz69YdKipe6z9eHozcg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9833527b4e.mp4?token=LFmfA0coWKsy4uWsTA4NSQZLd6iNpgPSzugaba3tiqebo2ocnQuO0rhztB4xJiJXDzE5fSCpOfrwaAYQdmgB9u34iQ1aIs_XDvk3xs6D6BB1ioAubthEFFwQSF1vT5kWumME3_Z0aELOSJXXTwhL47ZySEf34YopYWDN0s6HWrUE8SDKUid_NvJdEZUAOapi7JpG6cXaEgmYYI1kfmvbi-M37896i9gNqdTPQQoUvw2HDUOrWgEX3yn2BsdD7fDB2of544rmL_cSdGnml2D7KVz_itjl7RTY0sIB5UZnNIFeLr6ynf4dZTEEsFa1NzhgmhWnz69YdKipe6z9eHozcg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
شاگردان قلعه‌نویی شب‌بازی با تیم‌ملی نیوزیلند؛ ژنرال ایران از تاکتیک‌های خاصی استفاده میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.7K · <a href="https://t.me/persiana_Soccer/23275" target="_blank">📅 17:32 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23274">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/awOPOGgeKw3DjeM0AGBU96Io4V5Xs9RjdO3DzyEoKb2MPhkTZ1aqOW3mkkV9v-6SYKZ1wTmHtfavDaV5T4PB7oWSJcqmDu7-i7Gtjx-FyOGZ--9JN48DTaNSaXEMUDtUB-TPg56ClPcMmctnORt6UcCdmhJqwFSwPRE-oxIRR5U9evDIwd_v0q-X2tPLmvEXk2WuyNd41sP-OUQe1rglyuNloOxxGhaGlIkuIiebRmS2yanPsxJc1Tlf_4130Imna3qC6cpnuII9NvvVwz7u7hIyrMdV319T1Ixz83lLflq3hkDQxuZmrOe_egLjVwMUz2-KTYqKLIRBAPmSuSpR6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
این‌مدل‌پرتغالی و فن کریس‌رونالدو روی قهرمانی پرتغال در جام جهانی یک میلیون دلار شرط بسته.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.4K · <a href="https://t.me/persiana_Soccer/23274" target="_blank">📅 17:16 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23273">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e0ea01c2e9.mp4?token=b6-v3V1bVDxWL7qsqYgL9eSYmsqNLmttPFyNtUPNUzO2gUz5nbLMOL104UBxlSOOyPhok83GuQ26D74izuNxUbjOz6JWr2fyH_lNGiTt0a0WEHCsWQSXXw2841Labih-kNmIavROaU0zFhRKTd6UZ8OU8A_F8oGK0Q192rmUjX9zS8ifneSxGqp5YlfKX9t-3mHIN_V8cCqUGGB-u6qUcN1p9ea5P1DNmUl68i_iK6tCp5DZ7ZilY_fxjZzPM1pcII0FQWgubacHcQbmaO2ITRE5Q48QEd1s6cOdlpDlaZk-YFKOaLPwRKbomT77eXbZDJiq3YvTOENRZoc_9I6Cgg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e0ea01c2e9.mp4?token=b6-v3V1bVDxWL7qsqYgL9eSYmsqNLmttPFyNtUPNUzO2gUz5nbLMOL104UBxlSOOyPhok83GuQ26D74izuNxUbjOz6JWr2fyH_lNGiTt0a0WEHCsWQSXXw2841Labih-kNmIavROaU0zFhRKTd6UZ8OU8A_F8oGK0Q192rmUjX9zS8ifneSxGqp5YlfKX9t-3mHIN_V8cCqUGGB-u6qUcN1p9ea5P1DNmUl68i_iK6tCp5DZ7ZilY_fxjZzPM1pcII0FQWgubacHcQbmaO2ITRE5Q48QEd1s6cOdlpDlaZk-YFKOaLPwRKbomT77eXbZDJiq3YvTOENRZoc_9I6Cgg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
قسمت‌اول‌برنامه‌فان‌جدید ابوطالب حسینی برای رقابت های جام جهانی 2026؛ عالیه حتما ببینید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.2K · <a href="https://t.me/persiana_Soccer/23273" target="_blank">📅 17:09 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23272">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eVdFmnu0jT0pgqQe5yNjAmDoMzOYP9l6CUDMzlqAWnFG7GBAasNwNrwbepm5O0yUSiFVTDuE09_RGvI1EHqry6z4GbSYErNkid5XMjI63yQOSoXoaWWV_2k-wf_iwO2ggcRTnQ9oU_0RhkzRicSER5IcHTWwiX4-DNAo2LzszXkW1fz2kZqgW15AezzPGWI1FzyhGvCLsCc0MaZrSimcB5qO-8m2rK0IJh16KWTW7vyFRpej-gcNExnOpxWHlNhF4icQYFfXO9Ej-7iaswEBf3m2Ws53sGB1LatIDwGAZrFrqz6TmuYnYeo0lY6E9_0lDW9zc2qwGXEyIASvK3usjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
همتون‌فهمیدین ژنرال ساعت جدید خریده یا بگم بیشتر عکس بگیره ازش؛ 7 تا شات ازش گرفتن تو هر 7 شات ساعتش رو انداخته بیرون که مشخص بشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.5K · <a href="https://t.me/persiana_Soccer/23272" target="_blank">📅 16:43 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23270">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sEX-gP-L1R1yGMpCWM0YFJpe4ZHAm3H3Bh-9Hkq29yiMHZreQ70Ct6gBpsM89VctdTIPdbB3v23MQVa80jwmfyyB_iyF9m5vh1uUsqbRqm5j34nn8ZdBz8fTUwMWZZq-Vry11VWgZ879-Pxmj9bVuY_8V167FaG3CE3ZfIIpDCWa5m0GnA-QUlHmV0hOFxuP9Y2MIl8H201fni0BO6_tBfk3cMbMyb8vfqQ-FpAtFdfEpIrxvxMf88JLc5Eimzr4leqHgWNkgkk37TmIbvCvzm6iM83VqeknAjuOJ2GIAfY-G9bxix6mbbD60nA2s0RW2z4sfetMQI0laqH33uWaDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eInTwia93N2mmF30bHjG04N2y97uCLMTNrfeN8G2tPONhTfYKWbKBsrXzTVTTCCx4OCK7CtxfD5vLIORnuclNH9q8A03HjZ5LEZ-8Oyy6vZdg1hDQyDnp69umujEcFLdRQ0mbv8XcfB2to3d4RMYgHCwAJ97OGBRivHIQGw5gWy1d5darHlaS9DpD7JOHG-Vz6Rkj_RSrvZYILpMrS1XeC8-Yp3uSNzpgfQXkIA4ZbsojE4qAJazNG6-a9MjzDrtH_RZ1GxMKQEL2rpDzjLj6D-YxadrTRjNWfwN6GQC-ms-uNKMa2h_g1Kizp8BIAbDQrpig87Vp7_m_qahOCg8uw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇲🇽
هواداران‌تیم‌ملی‌مکزیک دربازی‌افتتاحیه روز گذشته رقابت‌های جام‌ جهانی با افریقای جنوبی
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.8K · <a href="https://t.me/persiana_Soccer/23270" target="_blank">📅 16:29 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23269">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cf1b43a439.mp4?token=ExoFS5P4V7lJRy0dIOLa6qLVN5V5KzSwEnG6QIJsAah-ueh8O73aJgDwDuM4eUQL9rYpxgcS7bSBS_2FMkpA93whAC0h5_r2eKtMpEo5o9TmRKa3SSb7VzmJ673mjDsUo9JQ4jQMW7Q95jZydrXojW67TxdHJUBg21umpV0BgWU1vdGXkCMxt8WSabsagknTPqdRTtsICM57SMYGOV39qMtVYijGJzNfa_g7akc-x7C2lLXeBHlAJ3-r8_Zw6KEWn8tN6_L_uviaprZTcYTecLsuQFky9PWYO5x5Numbll8Q3Lu-MGTKjGzwG_2ZVhoy3IAp4IArMY-RK2k2TGO8xQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cf1b43a439.mp4?token=ExoFS5P4V7lJRy0dIOLa6qLVN5V5KzSwEnG6QIJsAah-ueh8O73aJgDwDuM4eUQL9rYpxgcS7bSBS_2FMkpA93whAC0h5_r2eKtMpEo5o9TmRKa3SSb7VzmJ673mjDsUo9JQ4jQMW7Q95jZydrXojW67TxdHJUBg21umpV0BgWU1vdGXkCMxt8WSabsagknTPqdRTtsICM57SMYGOV39qMtVYijGJzNfa_g7akc-x7C2lLXeBHlAJ3-r8_Zw6KEWn8tN6_L_uviaprZTcYTecLsuQFky9PWYO5x5Numbll8Q3Lu-MGTKjGzwG_2ZVhoy3IAp4IArMY-RK2k2TGO8xQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
بنظرم بهتره برادر بعد از این حرکتی که زد کلا از فوتبال خداحافظی کنه و پشت سرشم نگاه نکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/persiana_Soccer/23269" target="_blank">📅 16:14 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23268">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uU30wzACWgelNMqqo-_q6Dxk_UrkBzDwon9BXKEAfHt-BAwrlMDznwUSAFLjI5EYEQeX7Rm9n8imeFg7nFi8e8yIQuNMfjyIAzT50GMnGbkpiQlvQZUc_cfiUxPKxwTB0Z5C_3_xrNMd1U0F3cAg-AkVrDAZllb4X83wFcd0t9v15Q_yM-Gz13KrTmOA8hYHuHcpSaG7s5f9dzUhLmUkmao1HoSLUho7n4-Ekg_PCSot6ZqNosZqLHi83WcfpMpXHTYM8V8-u2srOASksQAUVlhBZH6vxqZactzQb9BLA0qbWB3qyq0x9yczx5UJoxb4UMBXh2V39DDFwoqs6FqP0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
همتون‌فهمیدین ژنرال ساعت جدید خریده یا بگم بیشتر عکس بگیره ازش؛ 7 تا شات ازش گرفتن تو هر 7 شات ساعتش رو انداخته بیرون که مشخص بشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/persiana_Soccer/23268" target="_blank">📅 15:46 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23267">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UDHEH38etqBYZ4hHjXVELxHJjopVM_yfPncSO8j5Luenl0zh9BtfNf66ZWubezExZkdkhePULJR_qYnX0QxQZwC6uiddAjJ9YxRSHKyGgO5K1bfBakEL4uOvtl6apQ2DrJBjLgifyU3DXgvtwlTwLA1fgfp3k4rJOodpbqo3Id0gnphLChfR7-wpK_xH_-x6iEc491L4xj6xNUl5cagUy9T3dsnhyZgIIpqyRbbnVeStzdXTWZrh9a_1eC-UCpBaBOhtPQNUOZjI7eFA-HeZDLrYpN39ix2cbjlf7eWURbrPud7eO60ZYBpVOK7adfWACCwNUBkWlX_w3R1eg-9NfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛براساس‌رسانه‌های‌نزدیک‌به‌دولت ترتیب رفع فیلترشدن پلتفرم‌های‌ فضای‌مجازی به اینصورت: واتساپ، یوتیوب، توییتر، تلگرام و اینستاگرام.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/persiana_Soccer/23267" target="_blank">📅 15:39 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23266">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/060b4ac464.mp4?token=tWAOo-8l-UujkGqQZVkIZseOl77nm14s30wugED_3oW4vI8MEZI7wi0kvpE1kfS2sveybP3rV7osP_d_1XcP9bajYSfl32QNopDa9e7ZAVDf__K5OR2Prt-tVNfQWvJQDukV8w6AAtFfx77PNJV6idxoFM1MExBjnA4IlSUOwXVkmBZe-xD7ZH_ddn5rebnPQdQFLO_1rNv4OqYJVY_1y3TydDCgpPdFv-bADJmXpd0GJvkAAIKBiHtWyWll8pDAk6hx28TliYvop8GzVDXyvpsBQjJWk_9eYD6-nJCybqxougjJrnHnEyEIPZSmLZTIKvJ5cPfBiU7Xla_9b2F-gw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/060b4ac464.mp4?token=tWAOo-8l-UujkGqQZVkIZseOl77nm14s30wugED_3oW4vI8MEZI7wi0kvpE1kfS2sveybP3rV7osP_d_1XcP9bajYSfl32QNopDa9e7ZAVDf__K5OR2Prt-tVNfQWvJQDukV8w6AAtFfx77PNJV6idxoFM1MExBjnA4IlSUOwXVkmBZe-xD7ZH_ddn5rebnPQdQFLO_1rNv4OqYJVY_1y3TydDCgpPdFv-bADJmXpd0GJvkAAIKBiHtWyWll8pDAk6hx28TliYvop8GzVDXyvpsBQjJWk_9eYD6-nJCybqxougjJrnHnEyEIPZSmLZTIKvJ5cPfBiU7Xla_9b2F-gw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
درسال‌های‌اخیر؛
گولر، اندریک، دانز دامفریس و حالا هم برناردو سیلوا تا آستانه عقد قرارداد با بارسا پیش رفتند اما در نهایت سر از باشگاه رئال مادرید دراوردند و راهی سانتیاگو برنابئو شدند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.4K · <a href="https://t.me/persiana_Soccer/23266" target="_blank">📅 15:25 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23265">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KAUTsdLu5oQRGkDTtr1QEa5Nv7AJT4q_hIgUmfyTIgDwd2lpfmJQUub17vuhFjjRohi5oxqvm6dctrj3jBCdKZUeQUgfeb5iydU2j53GpVlNGpWDdtS2V4K-Uf0u-KIBw-wGZ7C_9fQ973980TlzRgj3UfouFCze_fn5IUnQA2rr_ihlN7birB5b9PieRBeCddU1tdPszTsBeRV65w5ULzP-NgXRcz8xI-0crG77Phc-ETuafXW_Hxvh3wsQNo65Wmv2V77x32WoPAC2nfC13LuHtLZEEdHTGMk6deWA2Y-e7-iLfYKAEJcuwCfeyyCYSxC0SV25uM9ySD8B2kSiog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
اینم‌یه‌لیست‌دیگه ازشبکه‌های رایگان ماهواره که قراره جام جهانی رو به بهترین شکل پوشش بدهند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.4K · <a href="https://t.me/persiana_Soccer/23265" target="_blank">📅 15:14 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23264">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/287a3c4809.mp4?token=hZZKiDkX2U48z9tcLcrhjAshFgVHx4X8sO_GotFNSMSWsp5VqIb_KSCbzdgo-VUC_k-AokOwvyq09WK22P39LUJIY_yL7BV_DOrPiqF4Sa9GPcs0i1h_E8cLCa8vBQcZld6OxTAlSPgR-YOfRZN9xiZTDt6yCDY9AY3mmJLh3MnE9Jt5Aii8jH8nJotmauE6Me27Tx6NedADZSw06JAIZN52_1XXMaG9mEDF-0kBu1S_5gmVYpZK402_ZqMzsr_WuB-VrmCz6lI4MlJwJ7nPWl94PM_I2xlPABJyGDMvXE05nVYMEJ8pASKP4RFJ8Wm0nGZDSVxQKJj6loVkqUYq-zzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/287a3c4809.mp4?token=hZZKiDkX2U48z9tcLcrhjAshFgVHx4X8sO_GotFNSMSWsp5VqIb_KSCbzdgo-VUC_k-AokOwvyq09WK22P39LUJIY_yL7BV_DOrPiqF4Sa9GPcs0i1h_E8cLCa8vBQcZld6OxTAlSPgR-YOfRZN9xiZTDt6yCDY9AY3mmJLh3MnE9Jt5Aii8jH8nJotmauE6Me27Tx6NedADZSw06JAIZN52_1XXMaG9mEDF-0kBu1S_5gmVYpZK402_ZqMzsr_WuB-VrmCz6lI4MlJwJ7nPWl94PM_I2xlPABJyGDMvXE05nVYMEJ8pASKP4RFJ8Wm0nGZDSVxQKJj6loVkqUYq-zzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
🇦🇷
ویدیویی‌باحال‌از مسی‌ودریبل خاصش؛ همه میدونن‌میخواد چیکارکنه ولی بازم دریبل میخورند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.2K · <a href="https://t.me/persiana_Soccer/23264" target="_blank">📅 14:53 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23262">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gXvqZMtpmFn7asBx1r7pZn0w1biC4OZxZ5Sm3HzNd8wGu18UcyxBEFdbdmSmvHheD7R61OMlXdKuXqwp67eQwsfkbV28xmWKIQT9-PqGc29yoi0c9MXdsOT1ESSdqga1NkVPUisFb8xQf6y5bDUu7f5EsIdhO59eysZv_UkrdnAeUrzNjswho0BEHPTZwFnIyCPyRKM__1TiNTyd0396hNU_Kc0iMGlqsOvQ965XsRI3huxxVmVvBjAC-drezL10aL4c9H8u6Oh_CblqM-VgSq1gU9VFpp5c2IRbossflva55XE4lLFv7RSWqT7iGtqvH0CjPbABU0DPRLsN-GdkIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
۳۲ باشگاه با بیشترین بازیکن دعوت‌شده به جام جهانی؛ بایرن‌مونیخ با ۱۶ بازیکن‌درصدر این فهرست قرار دارد. تیم های پاریسن‌ژرمن، آرسنال و منچستر سیتی نیز با پانزده نماینده در تعقیب صدر هستند.
‼️
نکته‌جالب‌این فهرست، حضور دو باشگاه ایرانیه:
🔵
استقلال با 8 بازیکن…</div>
<div class="tg-footer">👁️ 42.4K · <a href="https://t.me/persiana_Soccer/23262" target="_blank">📅 14:36 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23261">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5eeffe144b.mp4?token=arQ00kZtSEmuvviWqycM0ZHiW-NZ_JmZHqGvmn6VcjorfxzZjV7k6pCLpiivtQHkInLTpqcOfOKnsAjpb1PjhcXq9ILeHtw5u7LbjBwlwOWv0XVQyO6Jx0vrjqwCDQh0jG3U9dFK4OCm1yGbbwIZVoe5AiLsLQi8xhtdeUGAbBKDwvxRrTGlLkkYK_2Nfw_mOwbTZ2DGJ_BaaAqnZYZOdIRnbzUl0zZOTWNUW8DBygLMvN2cN7FnYjUOyyb7-V9ktpK_2EOvuEJVZgPUcFWw838nw4lCtNjrACAa-A4y3yQw0Hsh-5Vokor5Fbli2FiD_bzg3DaBo24_11JqJXX6sA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5eeffe144b.mp4?token=arQ00kZtSEmuvviWqycM0ZHiW-NZ_JmZHqGvmn6VcjorfxzZjV7k6pCLpiivtQHkInLTpqcOfOKnsAjpb1PjhcXq9ILeHtw5u7LbjBwlwOWv0XVQyO6Jx0vrjqwCDQh0jG3U9dFK4OCm1yGbbwIZVoe5AiLsLQi8xhtdeUGAbBKDwvxRrTGlLkkYK_2Nfw_mOwbTZ2DGJ_BaaAqnZYZOdIRnbzUl0zZOTWNUW8DBygLMvN2cN7FnYjUOyyb7-V9ktpK_2EOvuEJVZgPUcFWw838nw4lCtNjrACAa-A4y3yQw0Hsh-5Vokor5Fbli2FiD_bzg3DaBo24_11JqJXX6sA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚽️
هفته اول جام جهانی 2026؛ پیروزی راحت و ارزش مند مکزیکی‌ ها در دیدار افتتاحیه جام جهانی و گرفتن انتقام مسابقه جام 2010
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/persiana_Soccer/23261" target="_blank">📅 14:26 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23260">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F3gCryY4k--Pax675bsH0lvsTDYL5eYt9cJFbaPFkVeWpZ-wAMZIfpoW7Tk2Zg5J7Ddx5xraj0AF5bb_DbDHXD-utyv9gg8LKKvqYbBWmWqALkyZ9SCfL6B_J3vXjxtKGdv9OuhpuzzghuHTmC5KJ59BKf0_T__RMYDyJ2cjxBH-aNMt91azIZ0CXmTK42-w6cc_nYQcfciR4N6Ch2C7d7fkTeWWtVDH4PwILt71IWSN6IvQ6LclfKjMnfIK68vTUGnLe1GtOzz_O_2VvMdMXs7vg85DzjsUvG2O_0uAFe_Rye2PgvOzwXJgrYD25p3vVYHAwLAUoh2Eb11-1ZWnDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#تکمیلی؛دوستان‌عزیز لیست نقل و انتقالاتی باشگاه استقلال کاملاآماده‌کرده‌ایم و قرار شد امشب بزاریم که‌به‌احترام‌مدیربرنامه نزدیک به این باشگاه و طبق‌درخواستی‌که از ما داشتن فرداشب لیست کامل روبا جزئیات میزاریم. امشب باسه‌بازیکن مدنظر تیم جلسه داشتن که فردا…</div>
<div class="tg-footer">👁️ 43.1K · <a href="https://t.me/persiana_Soccer/23260" target="_blank">📅 14:11 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23259">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7927d57219.mp4?token=FinXovGy_hsrqCDxT8XdIXksEYRebOpRXc4DscSmETZWrTJi9w45Nudv5QuyWGRbQSuPJkNBHKWKjNSOJNwCe59AsJmXlkAUL-QyadD1I03fkwNHeMuj487TErgDr7cjXEcrJ3ns6PRaune1lVa1FDUVJQo-N12DtbZml33nrTEgCp5VtAgJinhkgUX3dkv1IFXSAZlAG01V1paVOs2ZTu2o2KyVM5XgHaIIgn8SO7aPE82s9v0CGDV06FeUD9P2Un4xBbNBUNSEv_eVQzmPoDurbbROqzi6yWzRlJVVr5M_s2MNt4ftzRacshQuV0Lkr6qSrp8u7subYnN50mGprw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7927d57219.mp4?token=FinXovGy_hsrqCDxT8XdIXksEYRebOpRXc4DscSmETZWrTJi9w45Nudv5QuyWGRbQSuPJkNBHKWKjNSOJNwCe59AsJmXlkAUL-QyadD1I03fkwNHeMuj487TErgDr7cjXEcrJ3ns6PRaune1lVa1FDUVJQo-N12DtbZml33nrTEgCp5VtAgJinhkgUX3dkv1IFXSAZlAG01V1paVOs2ZTu2o2KyVM5XgHaIIgn8SO7aPE82s9v0CGDV06FeUD9P2Un4xBbNBUNSEv_eVQzmPoDurbbROqzi6yWzRlJVVr5M_s2MNt4ftzRacshQuV0Lkr6qSrp8u7subYnN50mGprw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚽️
خبرنگار کره ای پیش از بازی تیم ملی کشورش با چک درحال‌ضبط برنامه بود که یه خانم مکزیکی اینطوری خیلی رندوم اومد ماچش کرد و رفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.2K · <a href="https://t.me/persiana_Soccer/23259" target="_blank">📅 13:51 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23257">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eBWLxvbQpdVuwn6ytI5OXAXiSiHPVU3tLIluOJYHkjziB4ECGPNq4-v0VdlyY8JkzwZRRkTMPKed_PfBqGZjFNLnpGicdC717Z-qr0vmHSuT9GwLoXMAnEvBNkc_8r5kQNlP2sBKYd91pN96sVS9TsKqFHDb0qZSrryLVdfJPlUUf28Rr15KNnkoUcWuiFH47A_JmW0jWftxxkIsx_Eiyt6y1u2943MU3pVnSKBmGdPdhsV9vsqw5Wme1EVFW3jTWXoTtKJoP0DmlHSg0i-8t32yCGrZDESwbjeV4B-IpSdTDe9B4SGARs-hxXU0BU2PVNKVUid-Ie8UI7uCL5LK3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AV0aSUi12x4NAuhu8-U1Fgg7HOuS6FEDu_vp3f5Axs6wX1CMbWXoK9VnQ6UJJxXC51UKv86OAK5B9lV0WfrfFQoWca1uNv9vn2SGi5jUfoFJQoJjMHvLNO8f8bgtCUIKcvhaiVzVGfa-p0LDcvIGSgctbuzAOs2DCwvCD-chrkfjyXb1k8XM7UNrJGK8PNuX0uzz5mEcMm5629o5189kAUt691gQC14sYTYuA20vAhxb086_QN8__QKiHJNY07FYOxDYQ_6qCGuBNgW-WyD8S_u1tT2Uf_wcz2FmYLJMn51WDlvNOstjp-Mkn-EOt0weSD4Bdi01Tzer9ms_i4uRfA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
به احتمال فراوان طی روز های آینده؛
پائولو مالدینی، لوئیز فیگو و رونالدو نازاریو نیزمهمون ویژه برنامه عادل خواهند بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/persiana_Soccer/23257" target="_blank">📅 13:35 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23256">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🎙
استعداد ناب گزارشگری روببینید فقط؛
با این سنش چه صدااای خوبی داره چه قدرت بیانی داره. رفقامون تو شبکه پرشیانا اسپورت تو کانالن باهاش تماس بگیرند که گزارش بازیارو بهش بسپارند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.5K · <a href="https://t.me/persiana_Soccer/23256" target="_blank">📅 13:17 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23255">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jf4BjCjU1gGSyDdcJrLjIPVy_q10dczHpfY1FTTbl62UHV0uBopqKHNb2lgooy23Ywo5Chs9QrlYffmmiQBIvgZhVhB74wecXJTWvyk-PFS2DWmrPc0w2-DOpICrmcipPnVuvXQaCwhstYakAmJVGBxIDv7Rjx8L34O-2TEQiP7ULX3iuJt4NRHdAslEP2LlaTpK4tSuNtuw_Sxnr4FHHsMf7skRyF3rYa68l3ID_c_5Z7c3X_tX_selA4n-xKqshRa-dOx34WYcr3CYI1jmdl2R9thXpIq6JNnTkUfN6UlpnWbVzBeQg5PHgijwbTB1Uq8w6TASHlOwwwm4iZrNjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
خبرنگار کره ای پیش از بازی تیم ملی کشورش با چک درحال‌ضبط برنامه بود که یه خانم مکزیکی اینطوری خیلی رندوم اومد ماچش کرد و رفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.6K · <a href="https://t.me/persiana_Soccer/23255" target="_blank">📅 13:08 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23254">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mFfotLvQgKem8rFklq-XDXB1Zr7S0aMhuJdvbmnWB9x21QxJH7O-G8GNmipTrz46OkqoqWz4JSWwXuboD0Ade01rV92z_9rDhxAkwlPaMcRFG8ufBQn-L6t4WgpvGgSrBLTdmgHQdh6O0Y5_0sof3FWeBGubrlZF7TEc3Yyj9OKWn7p-AD78LVrxB2w1cqKHdkYwgJn2J_gDS3kKDSEWVgybBswULztL8QpZqTsSv-kSYSGPmMDehfVhIEAsmtl9766X-bdNpq4LWATHNHNWh_gPuDPwMvDn2U4yxzTI0HxCTihfgFz_eXuQsIUN5J5fa52uP45whq0FCcH1bB-bfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#تکمیلی؛ در صورت تاییدیه مایکل کریک؛ مارکوس رشفورد قراردادش رو با منچستر یونایتد تا سال2032 رسماتمدید خواهد کرد و درجمع شیاطین سرخ برای فصل آینده رقابت‌ها باقی خواهد ماند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/persiana_Soccer/23254" target="_blank">📅 13:00 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23253">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RXtsjDME3LhfKlS3anXD60QVVsQuc0qxoYC3ZEt5hD7MCbVoftgw1sWr1ODpVBsOVEmp7prGzaj44t5X_ZecInhI2hz1fJ6waESeK_548a9JbJI4q_0COfVxYWT1YAmOj_k0cHrnaYzG6ywle8TSHEXutczkQKm8N5hJ_SMKpRL049US-DaGYomLD_VfBkHzygmlkpiAjv0Jkm_CfEF4I_JwAMfKydbAAuodIQK3Pefe9tPDeSsJBIm8bCU4Y95zEaSgV3kr2a5Z6YYEjjsWbF1GsOaieoqK3v31pXwlFazPFipbgzNkwTdod2q_AFooSJZskINs3SUUMlXaNIvXYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛ باشگاه تراکتور در روزهای گذشته علاوه بر تمدید قرار داد دانیال اسماعیلی‌ فر؛ قرارداد خلیل زاده به مدت یک‌ فصل و قرار داد محمد نادری رو به مدت دو فصل با پرشورها تمدید کرده‌است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.1K · <a href="https://t.me/persiana_Soccer/23253" target="_blank">📅 12:45 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23252">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7d91e6763c.mp4?token=f8oDmWmSFK9XANbPajt-FBfttFiOvTSLPIvMtD0ByLFN4F8_skyYaKoyWMRCafpGXND7DQafS3u5nSy7Bnq6vKTKU55DXKZH89lxCBNdM8id6WeHaSmSgUsBDcbT5qhoGsIk8tvoZ2MI_yyp33ZDGIuZ7vALbq9qMv00WT_RMoUYtIYecM9ne9oB-Zh0BWQ7DAFFR_LxKTg_k1sprx-iVaHKMcuCKrtOk6Rd5HXH9ld7LQxZy7ufewWhJ061XH9xTM0OFhhvdrVQ9lLAnQVzaSbdvvz63MM_3fcwIhOaLGndmqHeM0cibfRMvqnZ9kiSTEQ26sptVN-4PQfLOvhB-oWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7d91e6763c.mp4?token=f8oDmWmSFK9XANbPajt-FBfttFiOvTSLPIvMtD0ByLFN4F8_skyYaKoyWMRCafpGXND7DQafS3u5nSy7Bnq6vKTKU55DXKZH89lxCBNdM8id6WeHaSmSgUsBDcbT5qhoGsIk8tvoZ2MI_yyp33ZDGIuZ7vALbq9qMv00WT_RMoUYtIYecM9ne9oB-Zh0BWQ7DAFFR_LxKTg_k1sprx-iVaHKMcuCKrtOk6Rd5HXH9ld7LQxZy7ufewWhJ061XH9xTM0OFhhvdrVQ9lLAnQVzaSbdvvz63MM_3fcwIhOaLGndmqHeM0cibfRMvqnZ9kiSTEQ26sptVN-4PQfLOvhB-oWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#نقل‌وانتقالات
|
هایلایتی‌کوتاه از عملکرد درخشان الیوت‌اندرسون هافبک 23 ساله انگلیسی که به زودی قراره به باشگاه منچسترسیتی بپیونده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.5K · <a href="https://t.me/persiana_Soccer/23252" target="_blank">📅 12:34 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23251">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J3ZqcdHR06xB6xUthx7PYf3as32k6fp89z-9ynHlkEiom0cuZU_jCPi-yS9ygl9-kg_TnSp8QqJGLtWGXzadCvHhbOElKH8RXvwB248JouLfGNNRX60D_DMFq_t8NoEZBO7-rwt3RXKYLxTGElaQMFh8P4mqe4Ye1WDHxgsS4JppSJHIHyESO3DoK7Lxf4Zd-v9WUVBq_-Vb6IXAOxTTBnym_bYAOwI0Ov-XUHJ42jYujXCkLDV6zBfv7FqXC0rwyhgGaZXhlQkG7I1HuYiohFqX07URkWH_KD_7s0SoykuAvcBjsjQXq7x0yDqtFUE4SWypMqv4UXrFNrZAqrL2qg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
🇪🇸
خوزه‌فلیکس‌دیاز: یوشکو گواردیول امروز در تماس بامدیران‌منچسترسیتی اعلام کرده که از باشگاه رئال مادرید آفر دریافت کرده و قصد داره بعد از جام جهانی به جمع شاگردان خوزه مورینیو اضافه شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.7K · <a href="https://t.me/persiana_Soccer/23251" target="_blank">📅 12:17 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23250">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NPxc8ThZj6JRF9OUong0PV27L4m4OyhNXWAWlf5Qp3oezOOeKA6qnlkWn0bU7E6s-ko9kd3aqFHqwDeFwr1BlQPYMQTbTk7ox5qQgfWsrQVARF9eMRFRh4RPNSS11wMAHrLXHqTudjDw-zcsBevPOwY0Qd-K3ZpzkWBSBmF053pBKI1GzbKI0THXYJp2acK5Bn5mgxwGpKRwgxFwQArFif5KcLzND6_nPogwG7UfRDifme8U6Lh6pKgAHD22FjfYghztoewlJPB3RnS73retIG02wuycId7crtVgMzcrVPbcEuAQg4eqCyeSZPzw0jjH7vCWzGTO1TE7rL8DwUgLHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
#فوری #اختصاصی_پرشیانا؛پیرو اخبار روزهای اخیر پرشیانا؛ فیفا روزهای‌آینده پنجره نقل و انتقالات تابستانی‌باشگاه‌استقلال بزودی باز خواهدکرد و آبی‌ها قادر خواهندبود تا بازیکنان مدنظر خود را جذب کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.4K · <a href="https://t.me/persiana_Soccer/23250" target="_blank">📅 11:58 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23249">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/npd4ZAYbIaY490a2OJ9AceZAoMrGc2hylYx4cOyB5a-ynbDelTypm5PSNMpMMz2py0YOP2qj3Yjc0ZqAk3SY6zZ3H3YU9wEivKBs8mVDicyp6S8D0PAW28RXFUEosDy7lghbd08LIEuq6j5GgTl230NWTe8cTo_ilh79gfiVyUqQG49B__dYQYyQ0vWeNyC50ES-4MPpP9CQ2fg2VHzFtWjYgJLZ9devpKkiJqyjWFp4_s31lULxuV6RI5BSPQeU3DNHfUkZtZ5IujxRhv5OmcJrDKaIXua-jERpK4bSeXgAY2GTo45y1ygVJRG55I6xvCbFZvGniUipRYoY-3clqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
کنفدراسیون فوتبال آسیا AFC نمایندگان ایران در رقابت‌ های آسیایی را اعلام کرد که استقلال و تراکتور در لیگ نخبگان آسیا و گل‌ گهر در لیگ قهرمانان آسیا 2 شرکت می‌کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.5K · <a href="https://t.me/persiana_Soccer/23249" target="_blank">📅 11:23 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23248">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/733942b449.mp4?token=EdiMb9tqyQ7uGikippFwHwSYgTYVpMtmUSvGnn_ORwaQyCwOdj7efV0xx7PbxVu2WXMI5lIEr3ysqgh5JAgDR5BRGZ99wOSPb-WOOFZxPPTvo5vrePBH3g6j5K2-UPkQ9P9dB5DL0w70z1-IbOKIzcMHQT7gdKveXkKmxLUd_tnueWTNiRGWpDd4LPWS-WSYsoWOm1Ao_YVETyy8l0jtiTOYSOdj7Nk8PTWj774LQ7IPCCOQbWlB4F45Oxfq7dhumFQNv-WsEf3HHq3VWNTYti2uE1DwndAgswIyEIOcXPf0PASeyqmlAmP-_5fXlCwJgQsQt-cgIMK1ZuSkdkBmbQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/733942b449.mp4?token=EdiMb9tqyQ7uGikippFwHwSYgTYVpMtmUSvGnn_ORwaQyCwOdj7efV0xx7PbxVu2WXMI5lIEr3ysqgh5JAgDR5BRGZ99wOSPb-WOOFZxPPTvo5vrePBH3g6j5K2-UPkQ9P9dB5DL0w70z1-IbOKIzcMHQT7gdKveXkKmxLUd_tnueWTNiRGWpDd4LPWS-WSYsoWOm1Ao_YVETyy8l0jtiTOYSOdj7Nk8PTWj774LQ7IPCCOQbWlB4F45Oxfq7dhumFQNv-WsEf3HHq3VWNTYti2uE1DwndAgswIyEIOcXPf0PASeyqmlAmP-_5fXlCwJgQsQt-cgIMK1ZuSkdkBmbQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚽️
هفته اول جام جهانی 2026؛ پیروزی راحت و ارزش مند مکزیکی‌ ها در دیدار افتتاحیه جام جهانی و گرفتن انتقام مسابقه جام 2010
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.2K · <a href="https://t.me/persiana_Soccer/23248" target="_blank">📅 11:08 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23247">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b63a3e61cf.mp4?token=YY1QVXGogaUTWLNM9zQyEyTMfpOtM8xL3wZC6ZlrRTFVh0KJid4N3rZDJBXSDnO44tTbwWelpnTNPoENoEDBcl-Z5wNWyDpwCUyNnbj7sSWh-CrhfhxeIVkdptGvY8JU3sGELsrXbA5hkakFWWSgsJgX63NxFZrDApcq_kmE-qla_XcQfiNqKwBtFFup64H4GFFv7L30lH7ub2lfHrojjk_kkxLIdsdsmA1qCmWuo8-JqbOGAxKLGYSQStCOgKvCFe39i_DNJKLpfEHwGdDwSc_GTtwErLmfEcQjTNAnIblxnuMlHSSMC-LMbXLVCzr2VFIDB7E2kwhWtyQKRrdIvg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b63a3e61cf.mp4?token=YY1QVXGogaUTWLNM9zQyEyTMfpOtM8xL3wZC6ZlrRTFVh0KJid4N3rZDJBXSDnO44tTbwWelpnTNPoENoEDBcl-Z5wNWyDpwCUyNnbj7sSWh-CrhfhxeIVkdptGvY8JU3sGELsrXbA5hkakFWWSgsJgX63NxFZrDApcq_kmE-qla_XcQfiNqKwBtFFup64H4GFFv7L30lH7ub2lfHrojjk_kkxLIdsdsmA1qCmWuo8-JqbOGAxKLGYSQStCOgKvCFe39i_DNJKLpfEHwGdDwSc_GTtwErLmfEcQjTNAnIblxnuMlHSSMC-LMbXLVCzr2VFIDB7E2kwhWtyQKRrdIvg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
گل‌های‌دیداربامداد امروز دوتیم‌ملی جمهوری چک
🆚
کره جنوبی در هفته اول رقابت های جام جهانی
‼️
هوانگ این‌بئوم با ثبت یک گل و پاس گل و آمار بیشترین تعداد لمس توپ در زمین به عنوان بهترین بازیکن دیدار کره
🆚
جمهوری چک انتخاب شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.6K · <a href="https://t.me/persiana_Soccer/23247" target="_blank">📅 10:54 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23246">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7eeacd442c.mp4?token=DZXAucCxjB745UTrZorH2fMPY3Fe8KQMdI362H6O6Ppmocytua85pXI-qwNnA2a9KVIplXvtxUcSOc6u3xOrXyqe93FGuc4BAp2r0GxuMTlmx6iWkNHaWx-7EcaElYWSQqvhJ3r8jHEfwIGQq6L6Io-Ut3hFW3vBRVF_DmlTYFU6ww_m5vqI2spYxH8AzZnImjTMwqZPCwUv2C444gApDoJyR1I-qvLgrGlkwgMqEHVj95zNF4a9NAXg7DTQzJeajYMJAM6tUkpXvi0NR5IyOdKWrIbiMDt6gLcPpaSGFJACy8sUCzOOQl8KeqY6fZIsKOcxfWHEYvn_t4JrsmGvrbxbY5U5eaL-Nofc4haLnaLibm797s0MafpMdfnzCRQ_i78kdfqO1HWE6xQ-wdkKSOFnVdyQz1_pnyrerCbMw1dfc0jzINIoPrYvBglRfPaqs4jvh7fBJo1QbddRCuPGCFAd4kXVALB9YBW-kj5k9KDmAZGUCd4jDRHcLTeyYdqA0_VHBRfvlY7GJofIDAeXnReCAQrqOQiJ9VgUFu7SyBQgwNjLW1dcIT-LSalUZDms-GYXSuzjVyrG58NokBCV6HzuQCyZkKVJfDGHawSVfAJbMjyJq-kumMPwfHWxyeXaqsH5rZcrqP9qI6bAAEH0jTEwAxq2Cjetkht0hAPB-a4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7eeacd442c.mp4?token=DZXAucCxjB745UTrZorH2fMPY3Fe8KQMdI362H6O6Ppmocytua85pXI-qwNnA2a9KVIplXvtxUcSOc6u3xOrXyqe93FGuc4BAp2r0GxuMTlmx6iWkNHaWx-7EcaElYWSQqvhJ3r8jHEfwIGQq6L6Io-Ut3hFW3vBRVF_DmlTYFU6ww_m5vqI2spYxH8AzZnImjTMwqZPCwUv2C444gApDoJyR1I-qvLgrGlkwgMqEHVj95zNF4a9NAXg7DTQzJeajYMJAM6tUkpXvi0NR5IyOdKWrIbiMDt6gLcPpaSGFJACy8sUCzOOQl8KeqY6fZIsKOcxfWHEYvn_t4JrsmGvrbxbY5U5eaL-Nofc4haLnaLibm797s0MafpMdfnzCRQ_i78kdfqO1HWE6xQ-wdkKSOFnVdyQz1_pnyrerCbMw1dfc0jzINIoPrYvBglRfPaqs4jvh7fBJo1QbddRCuPGCFAd4kXVALB9YBW-kj5k9KDmAZGUCd4jDRHcLTeyYdqA0_VHBRfvlY7GJofIDAeXnReCAQrqOQiJ9VgUFu7SyBQgwNjLW1dcIT-LSalUZDms-GYXSuzjVyrG58NokBCV6HzuQCyZkKVJfDGHawSVfAJbMjyJq-kumMPwfHWxyeXaqsH5rZcrqP9qI6bAAEH0jTEwAxq2Cjetkht0hAPB-a4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
مصاحبه‌جالب‌ابوطالب‌حسینی‌باهوادار معروف و روشن دل باشگاه پرسپولیس که اون جمله معروف و تاریخی رو خطاب به علی پروین به زبان آورد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/persiana_Soccer/23246" target="_blank">📅 10:42 · 22 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
