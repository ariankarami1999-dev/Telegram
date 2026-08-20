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
<img src="https://cdn4.telesco.pe/file/GeJG2unAENGvcz9OFwsX0HPiYyaeOUDDtriiKi_zw1Tq0WOEtcKTXmoHmIf_QbF3YNkhTk3YTUnIGtmc-P43N__Vnbr7TGMEYh1xK_sBj-e_x4EWo5mS_9e639Nw0SeFewdKgS9KxplIlGEs5TltdtNmryNB5A-DWbRikEq69ydkl2wiV6FDomKnlllKPUK5dobBiPyhreM2oqqKVNQ1hP6oXnPq5zMP-OUV-yQpOpmJ0bLH5_PmpRA-XjajV3R2bj_-UXBnulEJgA79j17HjMTMBvEiSP8_eL0PhroF_2JzAYDB5jN6iSli4xWMpFpL0gUarWPhMC_L_3C1Koc6iw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.05M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforiiتبلیغ در ۳۰۰کانال تلگرام@Maino_marketer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-29 21:54:56</div>
<hr>

<div class="tg-post" id="msg-682885">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">♦️
تمرکز عجیب بازار ایران؛ ۸۰ درصد سهم بازار در دست فقط ۲ درصد برندهاست
🔹
بررسی بازار ایران نشان می‌دهد بخش عمده سهم بازار در اختیار تعداد بسیار محدودی از برندهاست.
🔹
تنها ۲۲۴ برند، معادل ۲ درصد کل برندها، حدود ۸۰ درصد بازار را در اختیار دارند.  در مقابل، ۹۸ درصد برندها فقط ۲۰ درصد سهم بازار را به خود اختصاص داده‌اند. آماری که از رقابت شدید و تمرکز بالای بازار ایران حکایت دارد./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 1.33K · <a href="https://t.me/akhbarefori/682885" target="_blank">📅 21:52 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682884">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/heheWVyDYwlFWvRUQdhaI9EfBZUvPNST4Ac0CazXOHnKBGDX7_-Ok2G6b0t5_grpU7N9vL2BxowQg6Jqm-bN1n6ES6aQyQfbMn1lrIxx7IBpF7EGeTSGjPZbal1XtWnLgkBRzrGNmozYeliRj1Z8iFiw5-oAtogp5rYz3CSp8rfXeKVlGFHTUe4YkDNNXuE37f1NPGim4FVm0i4eVhYSbYoX_0hbf00dot4lC07OAFIl3crKUDirQ4JKRjGJNN9Kjl4ec5ufGc-qZRQEvhuFGbfTDoN0qqnm0xH0e69typMqK3nfmcuoGZZKVNzBSSf2J-qW2R4nhnGINXis8NKLQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
رویترز: پس از حمله اسرائیل به یک پایگاه هوایی در سوریه، موضوع حضور نظامی ترکیه در سوریه به مسئله‌ای جدید تبدیل شده است
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 3.35K · <a href="https://t.me/akhbarefori/682884" target="_blank">📅 21:49 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682883">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4b1a89278d.mp4?token=Sbyp90P4ZM52FD-Iy8maIiZj-idzBWQa7AHnNY_pN0yE4TIB6d_ZNae1Jng0HZpAEDEoUl4SaiSMwTfDeoCB2lhpdppBwiYyy75ePsdAaq0b4AbdtT9RR0-cfinAzfwnrbp7L49tLnd0gq6mlLG0DKY9rXk2wlSzoB-rdFobm6BGu9_1wv9EPh4JNK2w9pEpHe1ftqowLKBlHJITqKNEjPZe1vPY1YZ9tYZr4KfUb3nY93RtAqJk47L-Ve4AsItcTarRR23aObPutPfB-1tHi9BYaSLIFrTgwt4zw-VNuflyGLKSDLrSAA7p_m2tKxGzddJ1-evt6Ea834FX5KhSlg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4b1a89278d.mp4?token=Sbyp90P4ZM52FD-Iy8maIiZj-idzBWQa7AHnNY_pN0yE4TIB6d_ZNae1Jng0HZpAEDEoUl4SaiSMwTfDeoCB2lhpdppBwiYyy75ePsdAaq0b4AbdtT9RR0-cfinAzfwnrbp7L49tLnd0gq6mlLG0DKY9rXk2wlSzoB-rdFobm6BGu9_1wv9EPh4JNK2w9pEpHe1ftqowLKBlHJITqKNEjPZe1vPY1YZ9tYZr4KfUb3nY93RtAqJk47L-Ve4AsItcTarRR23aObPutPfB-1tHi9BYaSLIFrTgwt4zw-VNuflyGLKSDLrSAA7p_m2tKxGzddJ1-evt6Ea834FX5KhSlg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
انتشار ویدئویی از ترامپ ۸۰ ساله با پوشک بزرگسال!
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 6.68K · <a href="https://t.me/akhbarefori/682883" target="_blank">📅 21:42 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682882">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">♦️
بازداشت زنی به اتهام تلاش برای بمب‌گذاری در ساختمان کنگره ایالتی نیویورک
🔹
پلیس فدرال آمریکا (FBI) از بازداشت زنی خبر داد که قصد داشت با کارگذاری مواد منفجره در ساختمان کنگره ایالتی نیویورک، یک عملیات انفجاری اجرا کند.
🔹
اف‌بی‌آی با تأیید این خبر ادعا کرد که این زن پیش از عملیاتی کردن طرح خود برای بمب‌گذاری در ساختمان کنگره ایالتی، شناسایی و بازداشت شده است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 6.69K · <a href="https://t.me/akhbarefori/682882" target="_blank">📅 21:39 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682881">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">♦️
راه رفتن دوباره پس از ۱۰ سال
🔹
این دختر پس از ۱۰ سال، برای نخستین‌بار با کمک یک اسکلت بیرونی رباتیک توانست راه برود؛ لحظه‌ای که شادی او را به همراه داشت.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8K · <a href="https://t.me/akhbarefori/682881" target="_blank">📅 21:36 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682880">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4df8662988.mp4?token=ZJjyH4YPoEWITbUcF8kwd75ko1Ahe8cdNmfzWlQtCBCCtTw3zsBqo1KaBeubzQeGZNzhtmZyR2xUN1PDWd-tF7Xyb-_V2h_kpHfX9Po8lqD4ZGfoGOBekeFgcTjlBKodSBl4FKBvH-nnQykO9MGhyIdnxOt-z9rtAICNYzMCH-x2xGqO_pKSVB3SLJu0e3kSCrpszXtyExqe8DEWRYhI2lXCFsEADoLLAQmbaqDyQNw0Ne-N67f8Orl8PyuItPZFcGfi0vDjTGDn_5hzBk3w-qLqpqqfXcqwP0PDk3gYnZZVzPALZCzi-uU7EbmMqvLISWurjZyUgT_PFBGpNB-xqg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4df8662988.mp4?token=ZJjyH4YPoEWITbUcF8kwd75ko1Ahe8cdNmfzWlQtCBCCtTw3zsBqo1KaBeubzQeGZNzhtmZyR2xUN1PDWd-tF7Xyb-_V2h_kpHfX9Po8lqD4ZGfoGOBekeFgcTjlBKodSBl4FKBvH-nnQykO9MGhyIdnxOt-z9rtAICNYzMCH-x2xGqO_pKSVB3SLJu0e3kSCrpszXtyExqe8DEWRYhI2lXCFsEADoLLAQmbaqDyQNw0Ne-N67f8Orl8PyuItPZFcGfi0vDjTGDn_5hzBk3w-qLqpqqfXcqwP0PDk3gYnZZVzPALZCzi-uU7EbmMqvLISWurjZyUgT_PFBGpNB-xqg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
موفقیت یعنی فرزندم به آرزوهایش برسد، مسئولین به فکر خودشان هستند/
خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 8.02K · <a href="https://t.me/akhbarefori/682880" target="_blank">📅 21:34 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682879">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OXPyoCyQDnFv_4C7EGMpMwhPYrF0whuVQ4TxgJxTfZS2mpYxZKWK0IqIbqdYS_EQZ-RB4b5KA9G9eQvpzCMh4rDxCR6dkYUB5kB0TRY6_1Id2O8NoD-wfIg277fE-LvJIySLGHyUQ_hLxGwzerNWlGlUc6UE0ofhWQZ095n0LOmu51TfJ3MSmMgRCLyJJ4gAjbcSCJJ6tTtafc1dRg5zyKU_BOcnIaUfHmcvDKtamJNsxsTtqadm5X7EI-fq-YupGSV7JaYhGQO131zbVhLZy1R_wjrqN2cwDpuCZ0ImVgMoft_ntm7LfJz88U7g_eJUvpRNV4fTPhDqoyWp92yaFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
نیمی از مردم آمریکا منتظر یک سال درگیری با ایران هستند
🔹
نتایج تازه نظرسنجی YouGov نشان می‌دهد نیمی از آمریکایی‌ها، معادل ۵۰ درصد، انتظار دارند جنگ با ایران یک سال یا بیشتر ادامه پیدا کند.
🔹
این نگرانی در میان هر سه طیف سیاسی آمریکا افزایش یافته اما بیشترین رشد به مستقل‌ها مربوط می‌شود. اکنون ۶۱ درصد از مستقل‌ها و ۵۸ درصد از دموکرات‌ها معتقدند جنگ ممکن است یک سال یا بیشتر طول بکشد. جمهوری‌خواهان نیز نسبت به ادامه‌دار شدن درگیری بدبین‌تر شده‌اند./ خبرفوری
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/akhbarefori/682879" target="_blank">📅 21:22 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682878">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0b9c1fa384.mp4?token=nDlTzJ6VB1A-g1STRNVeHT5ri5m2nfvFYcIRbV8XznwcLGp3wIaWhiCT0Gl1HosgrX6IJpZdJUvOdKR2j9rz7UvHox5TQrTJw9k5OEb0Hd-2r-T5TKa2cPCBs-0rYz8dW76qL2wc_6MU-0JfMqJblDUGAFwiBpCbNP7O2bzKmaMTZPwdnNzJ3TFJjvQOs8DDP4XZlvFrT9z2BQFC_sq3qxt0z1OKfdM9foTagLpmFTNR4cwmXucjO7JvsacD-tSz8rHmRG4phxn4IeMYiLB95KtU1tFiszmg9ejq6iKRJyzafrmYqcLPAPRC6Np_GG9Nkr-VRnTLhZXeFOz0tlhxLrCRSmi-6O514hFoZLaJd75QBFYSZ9UlxUEn4zQGNRV6ZIAsYyR5YL7D0uJbMUSdc-VLlrB_J5NnbnZ8JCMoGD3GuvGatbAlhxoqfZlYYERGbT5OS6n4G_SYaF2tQXiiXAn3rn0F2BYyW5_YWOV6ITVUszljeIlDSMtiY5NQv4lntOlUxc5_ruKPh0JmvgkBGQDZJLV_aPXm0iRUg9Srkbgw1xAgrp57xsp2TyFw7UMAVdmnhg_pNfeUGc0MJqm_IFvfJrhUJyvZA1C49Iq3_ddrPXsgKvyfs6DVwMw-868HAlj6OMiKqdbqpyYSBCrYOsWDb8Fsvk07Nhw-XvISlao" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0b9c1fa384.mp4?token=nDlTzJ6VB1A-g1STRNVeHT5ri5m2nfvFYcIRbV8XznwcLGp3wIaWhiCT0Gl1HosgrX6IJpZdJUvOdKR2j9rz7UvHox5TQrTJw9k5OEb0Hd-2r-T5TKa2cPCBs-0rYz8dW76qL2wc_6MU-0JfMqJblDUGAFwiBpCbNP7O2bzKmaMTZPwdnNzJ3TFJjvQOs8DDP4XZlvFrT9z2BQFC_sq3qxt0z1OKfdM9foTagLpmFTNR4cwmXucjO7JvsacD-tSz8rHmRG4phxn4IeMYiLB95KtU1tFiszmg9ejq6iKRJyzafrmYqcLPAPRC6Np_GG9Nkr-VRnTLhZXeFOz0tlhxLrCRSmi-6O514hFoZLaJd75QBFYSZ9UlxUEn4zQGNRV6ZIAsYyR5YL7D0uJbMUSdc-VLlrB_J5NnbnZ8JCMoGD3GuvGatbAlhxoqfZlYYERGbT5OS6n4G_SYaF2tQXiiXAn3rn0F2BYyW5_YWOV6ITVUszljeIlDSMtiY5NQv4lntOlUxc5_ruKPh0JmvgkBGQDZJLV_aPXm0iRUg9Srkbgw1xAgrp57xsp2TyFw7UMAVdmnhg_pNfeUGc0MJqm_IFvfJrhUJyvZA1C49Iq3_ddrPXsgKvyfs6DVwMw-868HAlj6OMiKqdbqpyYSBCrYOsWDb8Fsvk07Nhw-XvISlao" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
چرا وقتی سرمایه‌ای می‌خری شروع میکنه به ریختن؟!
🔹
شاید این اتفاق برای شما هم پیش اومده باشه، جوابش در این ویدئوست، راه‌حلش رو هم گفتیم
@Tv_Fori</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/akhbarefori/682878" target="_blank">📅 21:14 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682876">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/32311f490a.mp4?token=IPmlcYmjRof9nS0ETVQk2p7Lu6eF7Kv91-DP1Yo2BidvgM4m3lAOxU5_iLRUUQsx0cuJ4ztZNjzP8vMkGmkERSq-rSy3egPTrdirv7R-UvMUMnYYztHtrFLt6kE1Fc29Zn_BGfIA352FHbqLuND0uTh_j1P0-pM64qZ0xnR_VGWWzWA777sUxuRjrLgxCGL7bOd_iZAKcdZYH93dY-DKL_cKwjMhJHwPvPcnp3kKC4NxstR97xWu8E5A2XvSgY9DICma8CGC6azxC_rhlzdba5RtoijVMaZibeguT6w0Cp-ra9zlXelqo2glftF3NrCxCkjfD9AL9N_dHASisqOsQw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/32311f490a.mp4?token=IPmlcYmjRof9nS0ETVQk2p7Lu6eF7Kv91-DP1Yo2BidvgM4m3lAOxU5_iLRUUQsx0cuJ4ztZNjzP8vMkGmkERSq-rSy3egPTrdirv7R-UvMUMnYYztHtrFLt6kE1Fc29Zn_BGfIA352FHbqLuND0uTh_j1P0-pM64qZ0xnR_VGWWzWA777sUxuRjrLgxCGL7bOd_iZAKcdZYH93dY-DKL_cKwjMhJHwPvPcnp3kKC4NxstR97xWu8E5A2XvSgY9DICma8CGC6azxC_rhlzdba5RtoijVMaZibeguT6w0Cp-ra9zlXelqo2glftF3NrCxCkjfD9AL9N_dHASisqOsQw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
فریاد خونخواهی مردم حاضر در مراسم چهلم «آقای شهید ایران» با پرچم‌های سرخ در حرم مطهر رضوی #خونخواهی #تقاص_خواهید_داد   #WillPayThePrice
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/akhbarefori/682876" target="_blank">📅 21:04 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682875">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/865c03b40e.mp4?token=qeKcfTk3Nqc5o_B7wy50gjSsbzfBuesF5h29DA7_vygXoltWr5ws6aquOY31y4D_dIihUaHE67mM8Wi9B2XqqnqVc2upQZUiyi-gnnAhzehcesaePJ0rqU6x0HdthuGyXOcLaHo9IMoRpde1lfIlrVFgAL5kcMQo-mvvfeYLT1_CdKS4KUI_uXbF7txj3XO2tJfYTJvSO5lK4Tm1wccEG9hQAi2D0fVaoJQPgun6JFJjAydCGZCaSL0GBqWdiDu6c8Wi1021kguM4GnRq-Wq8-a0HFxkjGVj589gf0n3_HWgHMyZwXI_CZIi9Z9GXuIDtJTCgVzHgUbwq0Zq7yo1SQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/865c03b40e.mp4?token=qeKcfTk3Nqc5o_B7wy50gjSsbzfBuesF5h29DA7_vygXoltWr5ws6aquOY31y4D_dIihUaHE67mM8Wi9B2XqqnqVc2upQZUiyi-gnnAhzehcesaePJ0rqU6x0HdthuGyXOcLaHo9IMoRpde1lfIlrVFgAL5kcMQo-mvvfeYLT1_CdKS4KUI_uXbF7txj3XO2tJfYTJvSO5lK4Tm1wccEG9hQAi2D0fVaoJQPgun6JFJjAydCGZCaSL0GBqWdiDu6c8Wi1021kguM4GnRq-Wq8-a0HFxkjGVj589gf0n3_HWgHMyZwXI_CZIi9Z9GXuIDtJTCgVzHgUbwq0Zq7yo1SQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خبرنگار: آیا کارزار اقتصادی علیه ایران شامل چین هم می‌شود؟ چون چین شریک اقتصادی اصلی ایران است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/akhbarefori/682875" target="_blank">📅 20:59 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682874">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CDf2UfP8yCRBMlcBZ4jEbJbeepv6HvPZnan3GNrtZTvldZLetpVCutTGUxf_Pz2a1qD4Y2SW5C5lYrCBbROiBuLPHjW2bbj5axFnW54xRJ1Fl6TFtAyMFdqMJaV4rXJLHXdoax-6vK1R2yKIEr3eZh2NAU43npCN5moqglvKTAA8fTaecNODlrI_rE8Jcdwa4RbWME1In3Af1CTxMVrNFB_LgLGJhuAqdtOOBLqp1k-ard2AtqWpGMRwcGdB112zZONQ_ioQUM26JJadYRYgJeienYtmEkcus7596-ockR-FyThwMAtUADI5yJ_3SdPPKif26qWPgGmJIiRB5AL0mA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
واشنگتن: احتمالاً‌ درگیری گسترده نظامی با ایران از سرگرفته نخواهد شد
وزیر خزانه‌داری آمریکا اسکات بسنت روز پنجشنبه در گفت‌وگو با سی‌ان‌بی‌سی:
🔹
اگر ما (کمپینِ) فشار اقتصادی حداکثری را اعمال کنیم، به این معناست که احتمالاً درگیری نظامی گسترده‌ از سر گرفته نخواهد شد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/akhbarefori/682874" target="_blank">📅 20:58 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682873">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/11037e9cfb.mp4?token=pvPR-GNw7OLFgwBHRVVPF0pRHkyR72nNBG3tuV6RX52I-v9PDogK_psVbdqLIj7zmnIOwKFY2bt5h2MdhcAGsLtjgo0vpykYpmf5auOjZ_sctwxFrBwkJ1vLpSKZ6iX_SMl0agBNx-0a__4OheScHoDa2hE3gArp3_GoU8bSWyU-7FdtX_yAjAsMoIbSRlngMgeoYOl6ki52WMe0PQgD97Q65_h37oT5JmAQ7Dxf7hOwA51xX8Z6evd9aWjYA1Lq5OLFZO_UrTQN_dPYIK5umnIVHshSF6fflDgE72LJ1hzXoCPdPGbptZjnaX9xVtSD-BSH4Gqn0TQFhDXkO_vwkB2_rlHwmECLJM0YEYVqdqNpFyx3AJGaw8sZYSj_Dnn8LvkyYVNKadY8k7obFHcO24roihJ8bw39qhCGTTCEeiojm5jExj2mHGbgSj7q_SdApaa_FJzPkeHnN7o3_kGmlOgQ5U4ig3SKhLSaLsLzWh_fo2hngvRw7sYx9RUc2oIlHmFIszvcVUqhVGNMfwGQvC_vNThGLwvbwvCAHootEjbhhP8sl99qD_Ojv-WQYJuEyZ-UuyE5wsivSe8Ede-Az165aAbQMU4zCatD03V-yjGLPrpu93Sh1HODckCxa9IYrad3l9GXTSGKK0_98b-b1aHpNW5g96fGYMqjuW7nTAM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/11037e9cfb.mp4?token=pvPR-GNw7OLFgwBHRVVPF0pRHkyR72nNBG3tuV6RX52I-v9PDogK_psVbdqLIj7zmnIOwKFY2bt5h2MdhcAGsLtjgo0vpykYpmf5auOjZ_sctwxFrBwkJ1vLpSKZ6iX_SMl0agBNx-0a__4OheScHoDa2hE3gArp3_GoU8bSWyU-7FdtX_yAjAsMoIbSRlngMgeoYOl6ki52WMe0PQgD97Q65_h37oT5JmAQ7Dxf7hOwA51xX8Z6evd9aWjYA1Lq5OLFZO_UrTQN_dPYIK5umnIVHshSF6fflDgE72LJ1hzXoCPdPGbptZjnaX9xVtSD-BSH4Gqn0TQFhDXkO_vwkB2_rlHwmECLJM0YEYVqdqNpFyx3AJGaw8sZYSj_Dnn8LvkyYVNKadY8k7obFHcO24roihJ8bw39qhCGTTCEeiojm5jExj2mHGbgSj7q_SdApaa_FJzPkeHnN7o3_kGmlOgQ5U4ig3SKhLSaLsLzWh_fo2hngvRw7sYx9RUc2oIlHmFIszvcVUqhVGNMfwGQvC_vNThGLwvbwvCAHootEjbhhP8sl99qD_Ojv-WQYJuEyZ-UuyE5wsivSe8Ede-Az165aAbQMU4zCatD03V-yjGLPrpu93Sh1HODckCxa9IYrad3l9GXTSGKK0_98b-b1aHpNW5g96fGYMqjuW7nTAM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
فریاد خونخواهی مردم حاضر در مراسم چهلم «آقای شهید ایران» با پرچم‌های سرخ در حرم مطهر رضوی
#خونخواهی
#تقاص_خواهید_داد
#WillPayThePrice
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/akhbarefori/682873" target="_blank">📅 20:53 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682872">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">♦️
تحریم‌های جدید آمریکا علیه ایران، حزب‌الله، روسیه و کوبا
🔹
وزارت خزانه‌داری آمریکا امروز پنجشنبه تحریم‌های جدیدی علیه افراد و نهادهای مرتبط با ایران، کوبا، حزب‌الله و روسیه اعلام کرد.
🔹
سه نفر از افرادی که در این فهرست قرار گرفته‌اند مرتبط با ایران هستند. همه این افراد ترکیه‌ای هستند. ۷ نفر هم در ارتباط با حزب‌الله در این فهرست قرار گرفته‌اند که تابعیت یک نفر از آنها ایرانی است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/akhbarefori/682872" target="_blank">📅 20:51 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682871">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">♦️
ادعای رویترز: آلمان برای ایرانی‌های مخالف خط تلفن ویژه راه‌اندازی کرد
🔹
خبرگزاری رویترز مدعی شد که دفتر فدرال حفاظت از قانون اساسی آلمان (BfV) برای مهاجران و پناهندگان ایران، روسیه و چین، خط تلفن ویژه‌ای راه‌اندازی کرده است.
🔹
این خط برای مخالفان سیاسی در نظر گرفته شده است. آلمان این اقدام را برای شناسایی عوامل تهدید و جلوگیری از اقدامات احتمالی راه‌اندازی کرده است./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/akhbarefori/682871" target="_blank">📅 20:46 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682868">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">♦️
درستکار: آمریکا به یک نفر ویزا ندهد، تیم را اعزام نمی‌کنیم
سرمربی تیم ملی کشتی آزاد:
🔹
برای حضور تیم ایران در مسابقات امیدهای جهان در لاس‌وگاس، اگر آمریکا حتی به یک کشتی‌گیر ویزا ندهد، تیم را اعزام نمی‌کنیم؛ چون ما یک تیم هستیم.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/akhbarefori/682868" target="_blank">📅 20:34 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682867">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ab8e709b84.mp4?token=QJkLipLToRQ25GCwRB8oz3xeUe61VeoOPEqq1iD_5lboqXDgDMjprunrOLZ1jj6vtBGa_lZ_RoDhUs9g7R7Ua406gIJYtWmWl4qGTZnbwjF3jzPcNHR-hhrCcpzHUlsd9s1zDwTePi9QGuLFUfkkS5PRibUPsraVs87GeaxgZFybRDhL2xOXMFISFftUTsu4cdWqeRmCW6y0osKxs_eCCULwf38hpdOdcug7w9j4nH7uRWOCxoE4WH4YjPZm8rOku8my1LPSAN9vks8xXhNqz3seLwnEkCZ9s09qhKkvnMQGF2nkb-gbxU6JA-ceKzYu_YRDqgIIpVziv90iy-Mwlg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ab8e709b84.mp4?token=QJkLipLToRQ25GCwRB8oz3xeUe61VeoOPEqq1iD_5lboqXDgDMjprunrOLZ1jj6vtBGa_lZ_RoDhUs9g7R7Ua406gIJYtWmWl4qGTZnbwjF3jzPcNHR-hhrCcpzHUlsd9s1zDwTePi9QGuLFUfkkS5PRibUPsraVs87GeaxgZFybRDhL2xOXMFISFftUTsu4cdWqeRmCW6y0osKxs_eCCULwf38hpdOdcug7w9j4nH7uRWOCxoE4WH4YjPZm8rOku8my1LPSAN9vks8xXhNqz3seLwnEkCZ9s09qhKkvnMQGF2nkb-gbxU6JA-ceKzYu_YRDqgIIpVziv90iy-Mwlg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
لفاظی کاخ سفید؛ ادعای وزیر خزانه‌داری ترامپ درباره رویکرد شکست خورده تحریم‌ها
🔹
«اسکات بسنت» وزیر خزانه داری آمریکا درباره  اعلان جنگ اقتصادی از سوی «دونالد ترامپ» در پی شکست واشنگتن در میدان جنگ نظامی علیه ایران، با تکرار لفاظی ها ادعا کرد: سخت‌ترین تحریم‌های…</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/akhbarefori/682867" target="_blank">📅 20:32 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682866">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oTjobGFtyYoKBO4sdSN0IsQ2EUqkBvaxehQFg_EzJwYHaaCNIlLDX8UcRN8cU0R4RUr92ZoFpqcKUlZVUtkepv-Eax7YnBIoapECtmAi4rZjHqHP1S78zJuEZtG2h1IZPQrDFyRKQuxdqCLULuc9XzyBqdOHi680ZoBPByNlwK4qx5LZgpKPsfQSOhfP8ytQQn26Ie6nm9vu-XYSLyYSxyAxQsKsy4fVerswRaSI57enLbCw8dANa2cMFoz9zCuB9OjDl0NiJJgtNMt_ZiS5iiNvOg8O6KCoE7rUYAzDj_Tqz9-9MViVwiw_j51gPQleR5LRyDrFji3U2YQn40xVFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
لفاظی کاخ سفید؛ ادعای وزیر خزانه‌داری ترامپ درباره رویکرد شکست خورده تحریم‌ها
🔹
«اسکات بسنت» وزیر خزانه داری آمریکا درباره  اعلان جنگ اقتصادی از سوی «دونالد ترامپ» در پی شکست واشنگتن در میدان جنگ نظامی علیه ایران، با تکرار لفاظی ها ادعا کرد: سخت‌ترین تحریم‌های تاریخ علیه جمهوری اسلامی ایران اعمال خواهد شد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/akhbarefori/682866" target="_blank">📅 20:22 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682865">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">♦️
واکنش فرانسه، آلمان، ایتالیا و انگلیس در بیانیه مشترک، به شهرک سازی جدید صهیونیست‌ها در کرانه باختری: این کار غیرقابل قبول است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/akhbarefori/682865" target="_blank">📅 20:21 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682864">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">♦️
تجاوز جدید رژیم صهیونیستی به خاک سوریه
🔹
منابع خبری از تجاوز نظامی جدید ارتش رژیم صهیونیستی به مناطق جنوبی سوریه و نقض مجدد حاکمیت این کشور خبر می‌دهند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/akhbarefori/682864" target="_blank">📅 20:17 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682862">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XveDCle2425mbj-LGz-bH5g6Lgu9LonliVxp6ZnSoNkiMgoZfyPJAewY8AU_OKcWbwy8FxRWba_pdQvOaqXc7iLpShoFSyObuJT4k8h9x2glBbizwE6_wM89gGHwJlSP2gnpQYvgoOHO9UJraQqsJwuzO0UsZtRr9w-MGhmivbmLTixKIaBViFZCQ2WkfkBwCXD4o4696XI2WhNv7wQHFgtJHk6MrO-wgYFq5KxBOACYlmD352yZbzQ1xdCqTLKpOrk8BS79kjEyggM5NPRP4Wza8m2tyQTVQs99qJQmRSF53qMazG4WTfTjkIl4uIYxx7kpnbSFEtYOKx_VH0Af6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تصاویری منتشر نشده از سخنرانی رهبر شهید انقلاب در حرم مطهر امام رضا علیه‌السلام
🔹
مراسم بزرگداشت چهلم «آقای شهید ایران» از سوی رهبر معظم انقلاب در حرم مطهر امام رضا علیه‌السلام. ۱۴۰۵/۰۵/۲۹
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/akhbarefori/682862" target="_blank">📅 20:06 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682861">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/235238142c.mp4?token=YC8ZM-Cp8tMo82UMHNHpUdmp9NzzdRHZVGKfvFWFicOCZdRhwRqelc3LUYv-nd7G7kHCwzUuUJWtCclo3ljO72JhxjU-26ZMYXevdXgy5N16FJ9ImhS86AiJNkxHpISziG7ene1KLaqRgObdv84rSKAJl1NXQbCmz8sMWTA2w5yg_s6Z9FfETmtvDv5DnS7jC6YJkyu9b1Q1ORLw_mAhRcn73TCHMC44SzqCKXkrSG47kH-lXHBk3dznuo5K9_Cd9hXIMAlpofvoScSpAMgPKJ2ZFbxE3zY5bpeu1_FHXD1ACRBEXwSqM-adeI55KnmhqzdzmJIphknyJue5GVfLGg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/235238142c.mp4?token=YC8ZM-Cp8tMo82UMHNHpUdmp9NzzdRHZVGKfvFWFicOCZdRhwRqelc3LUYv-nd7G7kHCwzUuUJWtCclo3ljO72JhxjU-26ZMYXevdXgy5N16FJ9ImhS86AiJNkxHpISziG7ene1KLaqRgObdv84rSKAJl1NXQbCmz8sMWTA2w5yg_s6Z9FfETmtvDv5DnS7jC6YJkyu9b1Q1ORLw_mAhRcn73TCHMC44SzqCKXkrSG47kH-lXHBk3dznuo5K9_Cd9hXIMAlpofvoScSpAMgPKJ2ZFbxE3zY5bpeu1_FHXD1ACRBEXwSqM-adeI55KnmhqzdzmJIphknyJue5GVfLGg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
کامل‌ترین راهنمای لکه‌بری در خانه #ترفند_فوری
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/akhbarefori/682861" target="_blank">📅 20:04 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682860">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ba2666f082.mp4?token=ExMCmSun-K5jN9D3-EtcPT95WeEvqS7bfOcS7jOi1liqenTbNIiHG2PJoiBVmkAsjt8XyceJynFihvELEIFeSg73Zm9xVLAfE3-2GttYCVRNyF-IhX9-EX3rMZLxrF6ZKKE64JRqo_niAfMWt4BrMymZdWxV-Mt1TxcRaKF-h1KBrJ5ywcsGZ-W_dJvZVylsY-xJ3CB21eUuhaTEtcP3SKyfJWf0WRI0HsAhtYbEcPOOjyPMtfXXSoVM8XwEM-OayXNkzlG8hD0kzD-553bnuFA2qaZQ3m3GmDgNEXmibEeGcdOPwJsFOb4v6J29tom97AFPURR1PPz2Xfi9U8m_Bg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ba2666f082.mp4?token=ExMCmSun-K5jN9D3-EtcPT95WeEvqS7bfOcS7jOi1liqenTbNIiHG2PJoiBVmkAsjt8XyceJynFihvELEIFeSg73Zm9xVLAfE3-2GttYCVRNyF-IhX9-EX3rMZLxrF6ZKKE64JRqo_niAfMWt4BrMymZdWxV-Mt1TxcRaKF-h1KBrJ5ywcsGZ-W_dJvZVylsY-xJ3CB21eUuhaTEtcP3SKyfJWf0WRI0HsAhtYbEcPOOjyPMtfXXSoVM8XwEM-OayXNkzlG8hD0kzD-553bnuFA2qaZQ3m3GmDgNEXmibEeGcdOPwJsFOb4v6J29tom97AFPURR1PPz2Xfi9U8m_Bg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویری منتشر نشده از سخنرانی رهبر شهید انقلاب در حرم مطهر امام رضا علیه‌السلام
🔹
مراسم بزرگداشت چهلم «آقای شهید ایران» از سوی رهبر معظم انقلاب در حرم مطهر امام رضا علیه‌السلام. ۱۴۰۵/۰۵/۲۹
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/akhbarefori/682860" target="_blank">📅 20:02 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682859">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6ea40a0464.mp4?token=fvnwfeRWXjyRSDJdMmL4u1596JM84ZkpDHy1BT_fWEmb9HslB3zUKXoIupEIuUJUcGsDzZvtSvacXItqv62dLTfjmYO2htvd9D18enAh5LzBWE0TyvHH3JmjyYIpjbt0rM50TtLU-QWAahgz5F3hVVsrYPag506NcuK55s0vEIjZZOSN8QtJ5kLp2ZB3dNl669OH42_aK-PZP6BnHdMvvvsR7fgaUD14vAXKgxqcuepznh1GGrDWL-dJyimAT4Uoub0jo0cM8zJ65bBtMC5MDDSneF-qc2S0YVsQGisYDL1vEHGbeitwLj5AqqLGn17JYyIh0SrvPn1CBm8us8OBPA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6ea40a0464.mp4?token=fvnwfeRWXjyRSDJdMmL4u1596JM84ZkpDHy1BT_fWEmb9HslB3zUKXoIupEIuUJUcGsDzZvtSvacXItqv62dLTfjmYO2htvd9D18enAh5LzBWE0TyvHH3JmjyYIpjbt0rM50TtLU-QWAahgz5F3hVVsrYPag506NcuK55s0vEIjZZOSN8QtJ5kLp2ZB3dNl669OH42_aK-PZP6BnHdMvvvsR7fgaUD14vAXKgxqcuepznh1GGrDWL-dJyimAT4Uoub0jo0cM8zJ65bBtMC5MDDSneF-qc2S0YVsQGisYDL1vEHGbeitwLj5AqqLGn17JYyIh0SrvPn1CBm8us8OBPA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
ساعات پایانی...
جشنواره ۱۰ سالگی "چرم مَنطِـ"
✨
تا %𝟴𝟬 تخفیف
✨
«تمامی محصولات»
➕
𝟮,𝟬𝟬𝟬,𝟬𝟬𝟬 تومان هدیه اسنپ‌پی
با کد: PAYZ63R
حضوری و آنلاین
👇
🌐
manteofficial.com</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/akhbarefori/682859" target="_blank">📅 20:00 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682858">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/999bcdb3b8.mp4?token=s2_0uLp2Z-OQ8Ie-WLDi7z3ZknZDDwEk5d9Erd7U0e1pOYRTmn1l22B_TyV8J8fDMCynnZi1eLklYk5jyiZQmHbkavim7ttOLtwxg7QwV7sVAU31C6MeVJFZha6KNQ9JPorc_8LBCrztp1w3CH20lUza_7NA4DbZhmQD3DdYF_XFA4WSVfXwM170q4vhPF_GagaiwUhoWNw5xGgwKF4iSUcfoTgHDw1xRS8gXNATOBHp9MnOFMFcy0VjrcWr5qfc8auvvLRBf3vAT-3ZIjDCp4PxxShlYKNO-Hk-bjv2nSvOhEX4NBoQFsZIBlwUQ19xlEbBZPY1NbH5S1PkJbDWZw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/999bcdb3b8.mp4?token=s2_0uLp2Z-OQ8Ie-WLDi7z3ZknZDDwEk5d9Erd7U0e1pOYRTmn1l22B_TyV8J8fDMCynnZi1eLklYk5jyiZQmHbkavim7ttOLtwxg7QwV7sVAU31C6MeVJFZha6KNQ9JPorc_8LBCrztp1w3CH20lUza_7NA4DbZhmQD3DdYF_XFA4WSVfXwM170q4vhPF_GagaiwUhoWNw5xGgwKF4iSUcfoTgHDw1xRS8gXNATOBHp9MnOFMFcy0VjrcWr5qfc8auvvLRBf3vAT-3ZIjDCp4PxxShlYKNO-Hk-bjv2nSvOhEX4NBoQFsZIBlwUQ19xlEbBZPY1NbH5S1PkJbDWZw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اهتزاز پرچم‌های خونخواهی در بزرگداشت چهلم تدفین «آقای شهید ایران» در حرم مطهر رضوی
#خونخواهی
#تقاص_خواهید_داد
#WillPayThePrice
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/akhbarefori/682858" target="_blank">📅 19:56 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682857">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">♦️
داوطلبی که فراتر از انتظار خودش پاسخ داد؛ آنهایی که شهید شدند در کنکور مهم‌تری قبول شدند/
خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/akhbarefori/682857" target="_blank">📅 19:48 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682856">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">♦️
چین خواستار راه‌حل دیپلماتیک درباره ایران شد
🔹
سخنگوی وزارت امور خارجه چین در واکنش به مطالب ایران ستیزانه رئیس جمهوری آمریکا گفت که تحریم و فشار به تنش‌های خاورمیانه پایان نمی‌دهد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/akhbarefori/682856" target="_blank">📅 19:42 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682854">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pjY0WhFXSZSBFDdBUu5bJ2zu_imc3rDZz0rdJdtOWaLGsGeLtKQBQKD7sXtGlfq9Enx4ewZRPfqRDzVzb1Wp7OyyHbvVUty9bngjWADpiXH-6ngXJUlaozi2SAkahlU4PAUVHgYh8t3GJuuQWu8T-Lg7qcbFNaHdqOfPjIyxZIyVLOXrsdcP0w4q0MmyABT7UuPuHz0jFQ5RDP9UaqOA2qr6LvSv6GtlBMlpn7UkntROVF-rcj98s0Pro1yMyhn1RB6HVC97OM7WIY09_57X2klntpUo6q_tKEB01JUtPD0TuGVXG8fdfMybKhVeHmY7pX3_rnPbGsSOFsHb1OC27g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
از هر ۴ ایرانی، یک نفر «سرآشپز» را دیده اند؛ پربیننده‌ترین برنامه سرگرمی‌محور ایران در ماه‌های گذشته
🔹
طبق نظرسنجی یکی از مراکز معتبر از هر ۴ ایرانی، یک نفر بیننده برنامه «سرآشپز» است؛ آماری که این برنامه را به یکی از پربیننده‌ترین برنامه‌های شبکه سه تبدیل کرده است.
🔹
«سرآشپز» یک برنامه تلویزیونی در حوزه آشپزی و سرگرمی است که با ترکیب آموزش آشپزی، رقابت و فضای سرگرم‌کننده، توانسته تنها با پخش ۲۰ قسمت به چنین میزان مخاطبی دست پیدا کند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/akhbarefori/682854" target="_blank">📅 19:31 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682853">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">♦️
ناو یواس‌اس جورج واشنگتن وارد خاورمیانه شد
سازمان تروریستی سنتکام در بیانیه‌ای:
🔹
گروه رزمی ناو هواپیمابر جورج واشنگتن پس از ورود به منطقه تحت مسئولیت سنتکام، در چارچوب یک استقرار برنامه‌ریزی‌شده در خاورمیانه در حال فعالیت است./ ایسنا
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/akhbarefori/682853" target="_blank">📅 19:28 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682852">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">♦️
«فروختن گذشته»؛ وقتی آینده از دسترس خارج می‌شود | چرا عکس مهمانی‌های خصوصی ایران مورد توجه قرار گرفت؟ | توجه به گذشته بخاطر حالِ نامعلوم امروز است!
🔹
در سایه جنگ و مذاکرات، اگرچه خیلی کوتاه اما به یکباره فضای مجازی ایران به تسخیر عکس‌هایی از مهمان‌های خصوصی دهه هفتاد و هشتاد درآمد. مهمانی‌هایی که نشان از زیست پنهان طبقه عموما متوسط ایرانی داشت. واکنش‌ به این عکس‌ها هم قابل توجه بود. عده‌ای آن را به علاقه ازلی جامعه ایرانی به گذشته‌گرایی تعبیر می‌کردند و عده‌ای دیگر هم آن را با فضی سیاسی دهه هفتاد با ‌آن مختصات سیاسی مورد نظر متناسب می‌دانستند.
گزارش خبرفوری را اینجا بخوانید
👇
khabarfoori.com/fa/tiny/news-3238977</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/akhbarefori/682852" target="_blank">📅 19:22 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682851">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/320a0c6138.mp4?token=kQKum0FnVw3QzheWy8A4acZrCI4GPMCu6m1tMxwLVhyNzh1V1_gxi-G9zikaUCOaC4dRlWEkLG03P7KrEH9wj8-3HPb_t6r-MHKDm8nYWvgH76EcbHXXN4CiHDk4Dy4xqZc74_WRFxiRWlhmKjHvx5fRIPhZa3fmB5CiHe3h2u9iCIN0nbn7kYrOuHP8BJ5kis1rdL1u36HHR-FSz-oL2q3EtDOeiePCwCE8qOH10-fnWj9AyxinTMK7zwHKu8BM7A8Quqzn8VryiZ4TPQ3gdHeElg2kKQFnZ4RWu426q43EgFpEAm6Xvoj8qjE1w4cve0TQlAS9aO5hdV9d10x0vw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/320a0c6138.mp4?token=kQKum0FnVw3QzheWy8A4acZrCI4GPMCu6m1tMxwLVhyNzh1V1_gxi-G9zikaUCOaC4dRlWEkLG03P7KrEH9wj8-3HPb_t6r-MHKDm8nYWvgH76EcbHXXN4CiHDk4Dy4xqZc74_WRFxiRWlhmKjHvx5fRIPhZa3fmB5CiHe3h2u9iCIN0nbn7kYrOuHP8BJ5kis1rdL1u36HHR-FSz-oL2q3EtDOeiePCwCE8qOH10-fnWj9AyxinTMK7zwHKu8BM7A8Quqzn8VryiZ4TPQ3gdHeElg2kKQFnZ4RWu426q43EgFpEAm6Xvoj8qjE1w4cve0TQlAS9aO5hdV9d10x0vw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
منابع غذایی آهن
🩸
🔹
عدس، اسفناج، گوشت، لوبیا و جگر منابع آهن هستند و ویتامین C به جذب بهتر آهن کمک می‌کند؛ اما کم‌خونی همیشه ناشی از کمبود آهن نیست.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/akhbarefori/682851" target="_blank">📅 19:17 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682850">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lPIhxBQPSofZ5K2NOUHua7Mq3CFccX-BZgee-TlgrqZPJT3Nx8Vo_eAlQ923g4Ub3NuPOS0qvMVQ9Dxwv_yyL1LNXshMvJjw7mfpcwJcc5UuOu9Z8WTPPYMTgT958D_sAY9tZd96_YsOR378ozD5eG3Ai5UA-W9j4MJvDe8Hv5JvsGY2e2F0RALWEbrkq2GBt78bDEVFNzf6AduSphuy-UivX-Cn9-F8m5zis6t6jxtZ7Nn_6tMA2m6O6O6V2Mzj2VFCrGreA4Qi-bSpTPIhi6T9sKEtMk_K8BvmTrDYUKrxYPlJsgDJ7hd-B5fO_TWW96vg7zN3rxTsJ23gI78_KQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ترامپ شیاد مدعی آغاز جنگ اقتصادی علیه ایران شد  رئیس جمهور جنایتکار آمریکا:
🔹
هیچ‌کس به اندازه من فرصت بزرگ‌تری برای دستیابی به یک توافق در اختیار جمهوری اسلامی ایران نگذاشته است.
🔹
متأسفانه برای خودشان، نتوانستند از این فرصت استفاده کنند. بنابراین امروز…</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/akhbarefori/682850" target="_blank">📅 19:14 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682849">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c7dd4f3fdc.mp4?token=MHAwsEO4hzYRtSlS06CUM2n6q9yZuRRjIB1aHmPtTmCiJ_mI-4Fv9nNgGA6UtmsjNJJAlOSWjGKNX51JiFTJU6j7BdA0qzkL3wEF0VH9XEYW5h0Ot31SDG0reZER6IhC_EbaSA59ezXAERE5RMrPhU8UXaVU9Sm8uTxAK4sgx2EtgpORa_zy1Js5oYnzjAp3A05mzBHs0dGsCa3IMLDNC5tudCxT6LWRVKx84u7Poiyb-PHnZWGlVGfJ6s7ZAEpSldEGvgjoaqgmJkDXLgfbWiKecpP3J-H18uhTigr7329W-Efz_Jh-XAb6XaJjO3tAYKqck_POvjAD1qDalghfYQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c7dd4f3fdc.mp4?token=MHAwsEO4hzYRtSlS06CUM2n6q9yZuRRjIB1aHmPtTmCiJ_mI-4Fv9nNgGA6UtmsjNJJAlOSWjGKNX51JiFTJU6j7BdA0qzkL3wEF0VH9XEYW5h0Ot31SDG0reZER6IhC_EbaSA59ezXAERE5RMrPhU8UXaVU9Sm8uTxAK4sgx2EtgpORa_zy1Js5oYnzjAp3A05mzBHs0dGsCa3IMLDNC5tudCxT6LWRVKx84u7Poiyb-PHnZWGlVGfJ6s7ZAEpSldEGvgjoaqgmJkDXLgfbWiKecpP3J-H18uhTigr7329W-Efz_Jh-XAb6XaJjO3tAYKqck_POvjAD1qDalghfYQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
واکنش قالیباف به اقدام مشکوک حلبوسی، همتای عراقی خود: درباره ما خواهند نوشت که ما دو ملتی بودیم که نپذیرفتیم پاورقی روایت‌های دیگران شویم
🔹
رئیس‌مجلس عراق در یک عمل متوهمانه اقدام به استفاده از واژه جعلی خلیج عربی کرده است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/akhbarefori/682849" target="_blank">📅 18:55 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682848">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">♦️
ترامپ شیاد مدعی آغاز جنگ اقتصادی علیه ایران شد  رئیس جمهور جنایتکار آمریکا:
🔹
هیچ‌کس به اندازه من فرصت بزرگ‌تری برای دستیابی به یک توافق در اختیار جمهوری اسلامی ایران نگذاشته است.
🔹
متأسفانه برای خودشان، نتوانستند از این فرصت استفاده کنند. بنابراین امروز…</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/akhbarefori/682848" target="_blank">📅 18:54 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682847">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/90ed43fd93.mp4?token=gCN-I4zi5jGVGu_9mwUEfeNvNZwc4lgMTrdYS1d_rcbdXIJGVfuSuO4pPaU95FDzVTbs2re2qtsUBTVXQELSBP1ePk0p9k2cvXLtEe-OD9477gGrRJfRQbjxXtLrejHHmL1QfIVdTkL50mDBPr-LxfVkxbDjemGEwq27NXDuXAoKRZKpWPFj7k_M-eqGwekBRDyGytbGr8V5sPgFUKqPMue2D-xOFEwsjGfbUZe0aKx0qknYBeBIC7h6Ai12cjg747H66XSkz8rL80TARIXauF3KLjVRVKqrspf20mzPSfg8eSjeVIMkDNR_4VDL0c9L1dke5of8SA9E9ALjYhrvWw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/90ed43fd93.mp4?token=gCN-I4zi5jGVGu_9mwUEfeNvNZwc4lgMTrdYS1d_rcbdXIJGVfuSuO4pPaU95FDzVTbs2re2qtsUBTVXQELSBP1ePk0p9k2cvXLtEe-OD9477gGrRJfRQbjxXtLrejHHmL1QfIVdTkL50mDBPr-LxfVkxbDjemGEwq27NXDuXAoKRZKpWPFj7k_M-eqGwekBRDyGytbGr8V5sPgFUKqPMue2D-xOFEwsjGfbUZe0aKx0qknYBeBIC7h6Ai12cjg747H66XSkz8rL80TARIXauF3KLjVRVKqrspf20mzPSfg8eSjeVIMkDNR_4VDL0c9L1dke5of8SA9E9ALjYhrvWw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
داوطلبی که به اصرار خانواده آمد و سفید داد/ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/akhbarefori/682847" target="_blank">📅 18:51 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682846">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dfb59856f4.mp4?token=BvMOKmRYtNbjNrm6MfhesU329CnTLyNQGujBwje6anMfU-48qvQP5yd3YGA3XwOsXU4czjZlyvEW6AF9AYpFz0G5EJkBHpkOZax7sVOFyAL3FcLV7RFTAeSQpHztnCNrgiNuj6cI3o5ir6QA5qoGHhJSeNjMRlnV5iB1nQzrQqIiEAqn7sfCODmBkypnEbNlWZw4n9umzlvGTBoJ45F3ytE2XY-ontD6smjMUKvKr2rFbF-1FVPdjO2JzMZUy82nggK5kHZfj9u-WdG49ibZhU5T2hrfxf98a6b6ogLXwFNSpugzWe--_bTal0akDQAmUgeUbI0arsM8pHAWlvOxIw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dfb59856f4.mp4?token=BvMOKmRYtNbjNrm6MfhesU329CnTLyNQGujBwje6anMfU-48qvQP5yd3YGA3XwOsXU4czjZlyvEW6AF9AYpFz0G5EJkBHpkOZax7sVOFyAL3FcLV7RFTAeSQpHztnCNrgiNuj6cI3o5ir6QA5qoGHhJSeNjMRlnV5iB1nQzrQqIiEAqn7sfCODmBkypnEbNlWZw4n9umzlvGTBoJ45F3ytE2XY-ontD6smjMUKvKr2rFbF-1FVPdjO2JzMZUy82nggK5kHZfj9u-WdG49ibZhU5T2hrfxf98a6b6ogLXwFNSpugzWe--_bTal0akDQAmUgeUbI0arsM8pHAWlvOxIw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ناگفته‌های بسیار مهم افشین علا از گلایه‌هایش در فتنه ۸۸ و نوع برخورد رهبر شهید
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/akhbarefori/682846" target="_blank">📅 18:39 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682845">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">♦️
نگرانی امارات نسبت به تبعات اقدام ضد ایران
ادعای وال‌استریت‌ژورنال به نقل از منابع:
🔹
آمریکا از امارات خواسته فشارهای اقتصادی علیه ایران را تشدید کند.
🔹
این در حالیست که مقامات اماراتی بیم آن دارند راهبرد آمریکا در قبال ایران به بخش‌های اقتصادی کشورهای حوزه خلیج فارس ضربه وارد کند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/akhbarefori/682845" target="_blank">📅 18:36 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682844">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Nbl3nHZQ32a_xA4d-UQe28eFZ6Weh7tlybZEprBWebOn14bFvGmvSyHVzTOdea26fNCAr__bAngyzzuxUJNsjAIReIQYpKn3wVSmcvi9ClNdP-KY_UPxXiagOO9vbGFNQm4FPriCDTbn5ZYRIDxwuzhqZtdrHgPlOPHEZ5qmkWXJqoAt4j7cv3nsRI3RsFgK9ggP5kh1q2ZNaaJl982h-CQQaS4u7B6w1G2ks7GGXzXENCDS-mbK0cY_1AVsGgXsl0gxUHJ8RYDnqBW-5T_I-_Xn9K5lr1kDtyTTqEGW04iRwJeCLPLwSbgy2-snsOq4wYTMXK6PO-RLeeLAfL4QnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
هواوی Pura X View با نمایشگر عریض معرفی شد
📱
🔹
هواوی گوشی Pura X View را با نمایشگر عریض ۶.۳۹ اینچی معرفی کرد؛ طراحی این گوشی برای تماشای ویدئو، مطالعه و بازی بهینه شده و هواوی آن را نخستین گوشی هوشمند عریضِ غیرتاشو معرفی کرده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/akhbarefori/682844" target="_blank">📅 18:25 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682843">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TdQ-6fpTDMYxsH2sn82HQ5Rl4o-Vk6VK53bJ9npr2APAh-D5S7jVI83otyRWSTQGtyUG8sH8Pnky4jqA1n2rqHX0FXIhSTq9iTE6wcDHToZVa4sXFhBHZGdsLzFYXBUuEpDScs5p1ulf9oclkMMiBMpBO6gQNJREallW6K__5ntIXwXEKQw6h_OqLbR3R7n62FO2-hvZQM-yNVL1S5Ro4qaDaao-gCsjumK6KUA-MG_7tkXQ4GWcT2fHFFT52s2s6AwG8ybwyD1XOgeg8IBUYmhAalcIvNtz5z-CIzhFXGeMkNIgWGNDrRXqbtjeaPVwJzfU5Jau6025KJMhiBmJNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ترامپ شیاد مدعی آغاز جنگ اقتصادی علیه ایران شد  رئیس جمهور جنایتکار آمریکا:
🔹
هیچ‌کس به اندازه من فرصت بزرگ‌تری برای دستیابی به یک توافق در اختیار جمهوری اسلامی ایران نگذاشته است.
🔹
متأسفانه برای خودشان، نتوانستند از این فرصت استفاده کنند. بنابراین امروز…</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/akhbarefori/682843" target="_blank">📅 18:20 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682842">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q90buqZkdQM5GrTY167MmioHfQCQuDmh3kHBucgfcbjZSTP5jAebrCwbYjE9j2EbAsTmIukuiJtCKD58G7Ug0LZp8wfugyQ1_gFr9Ph0xNSxN30WjbEPEgTol4ljQvAy-JRdxJMipCkEt_0YUhvws_23LUOosEJiDD-px94ufbr57ZXVilhfNkggU1Ly--2V6TEk7xNVIDc7p2v9_p8f2Rm-WEk0vBq6Mn57K2c419TzokPF2C7KIpO_ZwDfq-Z3nfOU9_YSrjcHFhx0QpjSVUl9iVbUxvr9W6kfRFfsB-MAqJVgu3f83e3KD3X_zkRj2gF-Nwilb-fytF-OmGkNDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ترامپ شیاد مدعی آغاز جنگ اقتصادی علیه ایران شد  رئیس جمهور جنایتکار آمریکا:
🔹
هیچ‌کس به اندازه من فرصت بزرگ‌تری برای دستیابی به یک توافق در اختیار جمهوری اسلامی ایران نگذاشته است.
🔹
متأسفانه برای خودشان، نتوانستند از این فرصت استفاده کنند. بنابراین امروز…</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/akhbarefori/682842" target="_blank">📅 18:18 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682840">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gwQajq3taj_BrvalAoUgs6Q-MkaI8h5WKC_Klgg2D0rywKAW6cMcfeGTov97q2Tcq7iTdS29EKe2JouIdwbWdnergN6deDJzccXINrjqNXaDOYRIerue-EFItVtWI-x4ly_wTChzcKvi27CYV8DaF1ySOMS_MPwyHY4dvHjqOZdVPJ0WdAceeLxh3kDe9Te4h1xknNYBC4jGuYFMqkPQcHZk90PUUT9lLDmH6-_pnCk5mrssPGlsaa9GbEn4qAQ94i1Sw1wALq__Au-9H20HlKMNRQTfwTmOOMu9yGAjs6Piv0OBCoasqqexINy80pPwNUNE2NkW1yDEeeHXlhnSwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/njOEQgnnRDGNEu7AL-AImFedYucE_oEV4rAHo8aCpFWG-1leYiVzMdSY6WiBvmseTh4fk5ijvotg6nNBXaJV1MF2pPeJC9y5-M4KeYRmQAZmpoI8XtJHYBhdpSGB4gyuSLr9SSoOr23kT-cw_oLJrK0GwULyxo1DKjF_Ma7OnYmJrftIg6uTtNF1Yuzv1GTFBb6qI22e6JOWWwPEZvOhjoXBu338PpXT0VP0i0Yxj2RljaCAyaR8bObgDV_FTGX-DNl7zXFYi_Mel75fKnipGRML2emyo0wRQ3jTVw4e0r1n4hcaMsN0dMRD8MEcZ61L-19Dx1GlgQ4DEMcGjGX4Ag.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
حضور یک ناوهواپیمابر جدید آمریکا در منطقه
🔹
تصاویر ماهواره‌ای Sentinel-2 از دیروز، یک ناو هواپیمابر آمریکایی کلاس نیمیتز را نشان می‌دهد که در خلیج عمان در حال حرکت است.
🔹
این ناو هواپیمابر که مشخص نیست آبراهام لینکلن است یا جورج واشنگتن توسط حداقل یک ناوشکن موشک‌انداز کلاس Arleigh Burke همراهی می‌شود.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/akhbarefori/682840" target="_blank">📅 18:14 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682839">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/761bcaff79.mp4?token=LFkNSXv7adD1QFWFdCFn_vv2F0UU3O9qrlNLLbj6mPcdLEzGPbgjAAwSMvvJbPfDn810q0WuYZg7rUa47CqKTMqnSbDfSZoYpRC1If4scvOqJoQJ1on1CueIpiaB4gz4sXLsJFAOp21vXem0yIATVPEEuAVKpTTU3jgmNcIMWs-BnyY0R8E90GTPOHLyWcl6demAQJ-Wrh-1dGmjckC1UIGcvP8Ar7r0iY-D_IjbX1I3MA5lLXVY2Gm_lIONOv7wegv7Efh1fPUSHcbogBPyrPQMAHUsRdxg0iTtXMa-NEz36B0OZRG_ngtEgegZRtOEoAIAd98gy2poY1MDTyg6Pw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/761bcaff79.mp4?token=LFkNSXv7adD1QFWFdCFn_vv2F0UU3O9qrlNLLbj6mPcdLEzGPbgjAAwSMvvJbPfDn810q0WuYZg7rUa47CqKTMqnSbDfSZoYpRC1If4scvOqJoQJ1on1CueIpiaB4gz4sXLsJFAOp21vXem0yIATVPEEuAVKpTTU3jgmNcIMWs-BnyY0R8E90GTPOHLyWcl6demAQJ-Wrh-1dGmjckC1UIGcvP8Ar7r0iY-D_IjbX1I3MA5lLXVY2Gm_lIONOv7wegv7Efh1fPUSHcbogBPyrPQMAHUsRdxg0iTtXMa-NEz36B0OZRG_ngtEgegZRtOEoAIAd98gy2poY1MDTyg6Pw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خاطره همتی از توصیه رهبر انقلاب
عبدالناصر همتی با اشاره به خاطره‌ای از دیدار خود با رهبر انقلاب در سال ۱۳۹۸ گفت:
🔹
«به آقا عرض کردم من هر جا می‌روم، حساب کردم ۴، ۵ کشور که دلارهای ما آنجا بود و با آنها پول داشتیم، رفتم و دیگر خسته شدم؛ هیچ‌کدامشان همراهی نمی‌کنند.
🔹
آقا فرمودند: پس نتیجه می‌گیریم؛ برو قوی شو اگر راحت جهان طلبی!»
🔹
همتی با نقل این خاطره، به توصیه‌ای اشاره کرد که بر ضرورت قدرتمند شدن کشور برای تأمین منافع و حقوق خود در عرصه بین‌المللی تأکید دارد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/akhbarefori/682839" target="_blank">📅 18:14 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682838">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bd8959805b.mp4?token=l3JMQXfupqOyS90mzIAgibG45OqPkHBdsSiIq2C1J7aLIWWjqwIryqRlf-2yzA2wnctzFVjAr8A7ETiSAuhibad46cJzHz5rmGAbHl9QaTEhF6m_FNry3dg7lkJivR3QL5eLgtPgENg3jxDx9Zb3Qflx6xhLn-FVaU9Q9FJLgQBQpjZUHGjQB2JhOTQEJtIs4mJ_BToAsLCqmzxIiq_jQIHZW_daA2gAXAcspB71w8vn8mgdbhOnBNqrtXInvecGdRIUMBVh7WPzjbA7tmgf-Wb7Vitn9VKHn7is67L6HcH-lYgg0CFfL4DlgrAD7NtLBGclQt199ge8MUrjXw9Ftg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bd8959805b.mp4?token=l3JMQXfupqOyS90mzIAgibG45OqPkHBdsSiIq2C1J7aLIWWjqwIryqRlf-2yzA2wnctzFVjAr8A7ETiSAuhibad46cJzHz5rmGAbHl9QaTEhF6m_FNry3dg7lkJivR3QL5eLgtPgENg3jxDx9Zb3Qflx6xhLn-FVaU9Q9FJLgQBQpjZUHGjQB2JhOTQEJtIs4mJ_BToAsLCqmzxIiq_jQIHZW_daA2gAXAcspB71w8vn8mgdbhOnBNqrtXInvecGdRIUMBVh7WPzjbA7tmgf-Wb7Vitn9VKHn7is67L6HcH-lYgg0CFfL4DlgrAD7NtLBGclQt199ge8MUrjXw9Ftg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پس گردنی لیونل مسی به کوین سالیوان در دیدار صبح امروز اینتر میامی با فیلادلفیا یونیون
😳
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/akhbarefori/682838" target="_blank">📅 18:12 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682837">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromروزنامه دیجیتال خبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PaMAZV7_moS8BYJ29QwyEfzlGTt0vbW6cMt0tKlqwhQzkAOrrp_rjtE4Vaq-vVagYdXe1Ls-UVvGg3sxq5sYdZ-1J271QbvUvQlNOVgzJT5GamyLcV3dD2ZnbrkFMUS1AOuzHJwADFSx-6YHxGJ2pdjZnOnFvZQywHkyaQ0buS4d0bQXh-7DfKFpuPUrnssSxWMIJYObtH2Ca8E_HzThZAeEpgmZsvAKGQECIHVYej2h6wlwSwd5QQ-esyU2ZIgC9I5TxEctO9wDECf0VfbwCAHP9FAgx2YyafecLX6Hcgk3GD1ZPzYHQEYF7vjORfaOrVcA0ZJtD48HE4TUbAT2Jw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
عملیات شکست حصر
🔹
رئیس‌جمهور آمریکا بامداد پنجشنبه ادعا کرد که «خردکننده‌ترین عملیات اقتصادی» در تاریخ را ایران آغاز کرده، ادعایی که در شرایط کنونی، ضرورت شکل‌گیری یک جبهه منسجم و قدرتمند در داخل کشور برای مقابله با فشارهای اقتصادی و شکست این حصر را بیش از پیش آشکار می‌کند. عبور از این شرایط نیازمند تقویت همبستگی ملی، استفاده هوشمندانه از ظرفیت‌های داخلی و اتخاذ تصمیماتی است که دشمن را وادار به عقب نشینی کند.
🔹
هشتصدوسی‌‌وهشتمین شماره جلد یک خبرفوری
#تیتر_یک
@rozname_fori</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/akhbarefori/682837" target="_blank">📅 18:06 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682836">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
ادعای بلومبرگ: چین میلیون‌ها بشکه نفت خام عربستان خریداری کرد.
🔹
سه نامزد مورد حمایت ترامپ در انتخابات مقدماتی جمهوری‌خواهان شکست خوردند.
🔹
۱۴ هزار نفر در آلمان بر اثر گرما جان باختند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/akhbarefori/682836" target="_blank">📅 18:06 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682835">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DM3U_8F8FcflXbEbBgLRGnH2N2fi5_cPbxeTRSYQajcU2f-AtWWe04rKmczpZqo3vTxRAnT4ExbFNDpmOzRIL8jMNtNwb8UH9FgfoD2R9jfW0NTQ38YwT9QOwxdE2FEctnvISWVrZjdng0_SWUnDxcZAKCB6PqepPZSdaZvzhPb-Tyd3gaa54MdV82hvO_4T95_0eFIFsz4z39lrqONvovfl8XkrEtRhm4W_oKAThi1fMUcYLP_Iyq5daVUOHOEo8ftPvtULsjQuie1nQUx379tUd3zcK9ZTZ_sMLHyM0-QyyxBPyklZYgPpn7pMxIonm9AT1lUpzB3dPT6lUAbUKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
عارفی که نامش با عشق، عرفان و عمق اندیشه درآمیخته است؛ عطار نیشابوری
🔹
فریدالدین عطار نیشابوری، از بزرگ‌ترین شاعران و عارفان تاریخ ایران، تنها یک شاعر نبود؛ او با آثار ارزشمندی مانند «منطق‌الطیر» و «تذکرةالاولیا» اندیشه‌های عرفانی و انسانی را به زبان شعر…</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/akhbarefori/682835" target="_blank">📅 18:00 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682834">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/77b03c53ba.mp4?token=Gvsvcw-edSUMzXvc_EH_aTS3E7nOYb-U779EUJ72vAC5PUpQVxnabkiG2H3fopNNPQYxMJvgwKkF-63whFegFA7SdcwUkGRtyKE4zAZAbV3M5gH0EfbL95qROuKSdzY5HY2paR6gn3xwmEmZ2RYHBGNrSboCoT6G_a2G00nyytVjs5h-bMSacrZU8p1240g-EEC9-yk_OG116bUjNxUKCVHfO9BaMLAK3dstbYX6OIFhqZC7F_G8Wj4j0HjzyR1-SjTGJ8w20pI6GMkwaftkpbgWbPESkOa4az8maLCtKhL_AnE4hhG0Nsn_tWvgUyCSuNWKEp3_D6br5OhzZSDefg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/77b03c53ba.mp4?token=Gvsvcw-edSUMzXvc_EH_aTS3E7nOYb-U779EUJ72vAC5PUpQVxnabkiG2H3fopNNPQYxMJvgwKkF-63whFegFA7SdcwUkGRtyKE4zAZAbV3M5gH0EfbL95qROuKSdzY5HY2paR6gn3xwmEmZ2RYHBGNrSboCoT6G_a2G00nyytVjs5h-bMSacrZU8p1240g-EEC9-yk_OG116bUjNxUKCVHfO9BaMLAK3dstbYX6OIFhqZC7F_G8Wj4j0HjzyR1-SjTGJ8w20pI6GMkwaftkpbgWbPESkOa4az8maLCtKhL_AnE4hhG0Nsn_tWvgUyCSuNWKEp3_D6br5OhzZSDefg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویر آخر الزمانی از انبار استراتژیک سوخت در منطقه کی‌یف در حملات شبانه روسیه منهدم شد
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/akhbarefori/682834" target="_blank">📅 17:53 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682827">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/olsakhRjR7Owqhz1YK50aqP1TDEvQMD2tuCoDA1BNdib-xyWU1srC4sdkm_dI3LmqfW2T2NxVN1xqwtrPE_OJI5ro3df2IQyzRkWdvA9bMvaDKOXEDp8xjON0-iKK78ViLtfCZu1x-WQD0N5cIbKx8IbU2GIU58iXnAfRm1mH5tJpB2-2A5Wyp1b-TvdpvSPzSYcVg5iMquV23PVxQ_5VoKpzUgUTVF6o6gUg83m_QNFzyyXL2Hx6xfKFc3fhmPZ36auZHPyUSXghrZEs_t6YtAcgMT7KjNotl-nsvxh8xcR5S2YAgeY4dj4ZfmkIbSRMq66eOiTodgrQTdnXqhqLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YqBgPYNs4I4Q35L2AzQyAsZoSF3YLCcbAC0bfUwBBlYPixZSkviww0ME4MQBqo5h45DJ6gApJKKSfifjSZbsYprRxAmfbdv-kk6Hy6WyP_hzwPKohVo1f31XITR4jXSQ4mG5BP7nRpgMrDru_Fuz-beYeep6FIenT3Qrpek_xIxVx5GgjNX_D4uKAjN3yGmVGti5f77HlkrkPYHab9z-Kv-WDoxtI70aB_gLj6Q0co4N9z0au507kdLlWr_i9Ih8A9RaQosJqD0y-J9K-8zTqUNqOvrR_3jKFsFvSv0km0Z-lDenWsfkDRZ9f6BTWKTYwbva2oTlPFsqi-hvmsLGTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QZsiZMilnN3BUBPbyaPf6p4wYqXVa5gpYTBPf_Pgh3mEDySIngjLWBaFKlB2TQx5v3dXQ9Ygg1zeODxo4WyWiiO3sYJHAkEWRpjCnE9yGQ7IARo-YXNUx7hWHKwtif2D3Ti2XlK6ROELqXpLwWAFbqArOXck9pPfQoYptT9lY9JOvRdLN3t7liIIn8tSzKZ0AU9IdjqMIDYFc7pBPIiDxZtc7mv1gb18NyG7jmYCwvi5agjqNaztjOxsEjTcxerJZPEhmA3smKa4GVvr2R5Sj6lKWgVTe6FemEpTk8ihuwkOcdpxgdXuY_g-LIoOc-5OP9njxkhewsEiPY9D0STLRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RN8thRtYBye1a-IdjqbNVP_DYnlBF1ZdJ0CnYcrXBKN5giahr85vEJXGOCyQhWNU7OMdrrodelfx5a1qP0BrkkDGRAe3dEkuajSTkJS5AZWAlnpf7x6Ukbfyakg_to1zo4x4MoxWuUpcuohnOO5v1qUG6KERJUwEeBoNWGoN46t2zEYAP8K76MMIkqKeX0pS9o4Va-Uww2i3FdwvQZ-UqymsGZcZPXKiM-1tFpQ-H7tO4kNVW06JKDOi3u9adMia8cLR0wdw3KOW3suYixsTV_xYTwtsgSENVrnxLlCOzrMcblBj2LNz74zpwjVy_k_FmfYvWxqjTSz3ss1iT6KDCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/erwkJCSVuwgWSXb4ShwjQ77_eI9hyECB2pJ9CPWe_ZaSowJtoKVie1gw2qASF4D1fNgoYkjSZ1FcC83nvWeiN7D-w-baqK_nlwu8DsP1Nm_KDxtk0X77JNaNDvGxph5Eb2JTpUf2mm-n6jRYk3StHZYuUGX5F4Yr9NgUgjuuuAPc4S8XJEwyu1Frtz4oXenZHpsBaJo0vl411HFvOhSOu37kkLdsRic7xgWE_n5fomVnarLfWUvDD1Z-WlVj9f0hbkvZnGSkf6ImGkQJlUvrCVG2PbHVAwO-DGP78y5Owb-wTDuk3MV0Yapo5tGwcMgqBZ4-KcPm8MrKnN3e8ghrVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PSHcIIhS7Mk0ClwvHCynq75GjJeOZlDyxllZlQVP9qcaIL8VdcbdesrRswbVumsZo11GPl2AA8_gqYgTnwq3f05Dg02WtgMYE--shAo7NlfZ42c70xSP3-OrzEGu_tHveTLqAZd_3UxFtWT_-LLz2cCOwgUJrUarHuwAIlhwQAmDxO6kBwLI3_xMAsv5uWzO24eTPFL3SzF9jooMnaVXGoMLfUbBuOzDl587Aokbu6LUWcybHZ8-qJsByh5SRQY78Ft11JkvMoYZ4ezcmWl8_Z9CvDZgJ26VZb4ocsMmB4E58aExdnNWSM38DL4Glp3zHs4BQtSCmXKPiWi8J320wA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
نوشیدنی‌هایی که باعث خواب راحت می‌شوند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/akhbarefori/682827" target="_blank">📅 17:37 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682825">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromكانال اطلاع رساني بانك كشاورزي</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qDm5F-Sttg2nyXKr17piuhtC8l8C1MwlDpNVlCHuJbnuzjSp7Ct2757l1rKSeEa0wqpTwJddY5OfWwZ6hVSKJiyFc2WprwF8b3k4bjw4vST_JH5oVNjleegflnICC-pbdDlw1GKu4R9SE3Qujdb_5qe0E38fLL3EoGsUTCzEgFyVY2kPaK9vcHHZOtL83yTeeQU_XC79G5tVfQ6xfOz-DavI6l20HbcB8FNqaOJ-QG1NNuvpoZ-X7017bYenkVj8M0Lp7OON27AHvqIHiiEY8OCncbVEYwkKVbGFTcBKBQEVaf-AzwlrRG9IsYQv4PolJnkB0F8ZyjfbVSWhD6G7KQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
بیانیه بانک کشاورزی در پی احقاق ۷/۵ همت بیت‌المال
⚖️
قدردانی از دستگاه قضایی برای اقتدار در صیانت از اموال عمومی
🔻
بانک کشاورزی با صدور بیانیه‌ای، ضمن قدردانی از رأی قاطع و منصفانه دادگاه تجدیدنظر استان تهران در پرونده مطالبه ضرر و زیان ناشی از جرم، از تلاش‌های قضات شریف، پاکدست، شجاع و مستقل دستگاه قضایی در صیانت از حقوق بیت‌المال و اجرای عدالت در پرونده یکی از متهمان کلان اقتصادی و ابر بدهکاران شرکت کارگزاری بانک قدردانی کرد.
🔻
در پی صدور رأی قطعی مبنی بر محکومیت این متهم به پرداخت ۷۵ هزار میلیارد ریال، بانک کشاورزی در بیانیه ای، صدور این حکم را جلوه ای از حاکمیت مطلق قانون، اقتدار و استقلال دستگاه قضایی، دقت در رسیدگی و عزم نظام قضایی برای صیانت از حقوق عمومی و منابع متعلق به مردم دانست.
🔗
مشروح خبر
🔸
🔸
🔸
@bank_keshavarzi</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/akhbarefori/682825" target="_blank">📅 17:36 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682824">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">♦️
حمله پهپادی یمن به نجران و آرامکو
🔹
نیروهای مسلح یمن با استفاده از پهپادهای تهاجمی، فرودگاه نجران و تأسیسات نفتی آرامکو را هدف قرار دادند که بنا بر گزارش‌ها، این عملیات با موفقیت کامل همراه بوده است.
🔹
این حملات در واکنش مستقیم به نقض حریم هوایی یمن (استان صعده) توسط پهپادهای سعودی صورت گرفته است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/akhbarefori/682824" target="_blank">📅 17:33 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682821">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a9920553d6.mp4?token=lm_9fW7JzhO-vEqC6FxzM2da74W9vfW516gXwaXSFgT78tvaZxfeiF3XHcy9psafD9q-EEIKOGM9-6sPdGIlbuBaR-6H3Yma3S3kiiW3ypoKIBkMpXV6ckaDldvmLmoUzYkfpzB-UeUkoJNSXCCZDICXwwrQrB4H622xAScnGet92Rub_BABrFfzUcYtj4NUp0w2Genwju1X-hkijzZxRoZpkTbNcr1fr2A2K1fl1AtmoFMdT9c4fbKYMhMjyOuBGRrdVvwslz7-SdBePHohlcPQQqc0WmNWWV7NL4ValyZ1sLhD7SssyE-QjXRvBG97J55tUoZ36vKOE_31A3WMOQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a9920553d6.mp4?token=lm_9fW7JzhO-vEqC6FxzM2da74W9vfW516gXwaXSFgT78tvaZxfeiF3XHcy9psafD9q-EEIKOGM9-6sPdGIlbuBaR-6H3Yma3S3kiiW3ypoKIBkMpXV6ckaDldvmLmoUzYkfpzB-UeUkoJNSXCCZDICXwwrQrB4H622xAScnGet92Rub_BABrFfzUcYtj4NUp0w2Genwju1X-hkijzZxRoZpkTbNcr1fr2A2K1fl1AtmoFMdT9c4fbKYMhMjyOuBGRrdVvwslz7-SdBePHohlcPQQqc0WmNWWV7NL4ValyZ1sLhD7SssyE-QjXRvBG97J55tUoZ36vKOE_31A3WMOQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حال و هوای خانواده کنکوری‌ها مقابل دانشگاه امیرکبیر
/ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/akhbarefori/682821" target="_blank">📅 17:33 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682820">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f68LWi8YCwe87DKfNiqs8qOdtbN5ihE7GxXTsl5KMPBTfbLUEB3DAmSD0cnnA0PzS8DYhQ_Jqd2UbyAv18ucmwIIIFUCVfc8U-CqkUrr7KVThhI39ka80dFmIlsqaeArCrdDEMWjJFddakRnqATlc3MDt5JfTzL320oE6z0l-dyfbtuWNWYr9AzcNHqtwVuq0a88VgWt-51znjCmPSRoe0oZpGQU7ATRXcSD322jnoGiWrc5-LDuExH8wVL54WhZfnH9ndwkCsHkZuAdZQntjtesT-Byyudo6Y6G7qb-XipHF5XEqjkSUeO7uKze4hXhHu7tEICU6-NppmNsddoHPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مقایسه کلی دو قدرت بزرگ؛ چین و روسیه
🔸
چین با جمعیتی حدود ۱.۴ میلیارد نفر، ۳.۵۹ تریلیون دلار صادرات دارد؛ در مقابل، روسیه با جمعیتی حدود ۱۴۵ میلیون نفر، ۳۷۷ میلیارد دلار صادرات دارد.
🔸
در بخش مالی، بدهی دولت چین معادل ۹۴ درصد تولید ناخالص داخلی GDP است؛ در حالی که این رقم در روسیه به ۱۸ درصد از GDP می‌رسد.
🔸
از نظر بودجه نظامی نیز، چین با بودجه دفاعی ۳۳۶ میلیارد دلاری، فاصله قابل‌توجهی با روسیه دارد که بودجه نظامی آن ۱۹۰ میلیارد دلار است.
📊
آمارفکت | مرجع تخصصی آمار کشور
@amarfact</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/akhbarefori/682820" target="_blank">📅 17:20 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682819">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">♦️
نوری: دولت خسارات ناشی از جنگ به قایق‌های صیادی را جبران می‌کند
وزیر جهاد کشاورزی:
🔹
براساس گزارش‌های دقیق کارشناسی، روند جبران خسارات وارد شده به قایق‌های صیادی در جریان جنگ در هیئت دولت اصلاح شده است و پیگیری‌ها برای پرداخت کامل این خسارت‌ها ادامه دارد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/akhbarefori/682819" target="_blank">📅 17:16 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682817">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from| تهران روشن |</strong></div>
<div class="tg-text">به وقت ایران ...
❤️
گاهی باید از فراز آسمان به ایران نگاه کرد
🔸
آن‌وقت می‌بینی این سرزمین، فقط مجموعه‌ای از شهرها و جاده‌ها نیست؛ قصه‌ی میلیون‌ها قلبی است که برای ساختن فردایی روشن، در کنار هم می‌تپند.
ایران، با همدلی ما روشن می‌ماند.
🇮🇷
#مصرف_بهینه_برق
🆔️
@tehran_roshan</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/akhbarefori/682817" target="_blank">📅 17:06 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682816">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">♦️
میراث فرهنگی
:
فعالیت تمامی معادنی که در ارتفاع بالاتر از ۱۷۰۰ متر، متوقف شده‌اند/ صدور هرگونه مجوز برای ایجاد معدن جدید و حتی احداث راه دسترسی در این ارتفاع ممنوع شده است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/akhbarefori/682816" target="_blank">📅 16:54 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682815">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/07174a3739.mp4?token=dtyRN0YCRpxcuHCRyK65wbzeoRqJI3PI474nur_DH5Kb5Gh_sqvBEm2LrJVtkn3grmrRurAa7gOtQoHvv2WL7Z59yiVnrhQKEF6-2o0VVWH1Ab0JX4BJUvYdppF-f73SIe2mBVDXnr4lkubtMUoAjdpxqMFMOnU7X_tqOPCZaY3ghki66Y5UbmRSzRgxJ79QUdXAEjrf34RTeKICWQbxuIzlrvWwC0HOubmucYB37ZL9KL0MmMCzg68g43JENFndoHxZV1bwJ19XGmH5_cIwlCBdzpOyCI4wo9-FVI4SLpDzZRkZsiXiowRxK38TSuZKbXONP8CAWupuDTXs-wuPNg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/07174a3739.mp4?token=dtyRN0YCRpxcuHCRyK65wbzeoRqJI3PI474nur_DH5Kb5Gh_sqvBEm2LrJVtkn3grmrRurAa7gOtQoHvv2WL7Z59yiVnrhQKEF6-2o0VVWH1Ab0JX4BJUvYdppF-f73SIe2mBVDXnr4lkubtMUoAjdpxqMFMOnU7X_tqOPCZaY3ghki66Y5UbmRSzRgxJ79QUdXAEjrf34RTeKICWQbxuIzlrvWwC0HOubmucYB37ZL9KL0MmMCzg68g43JENFndoHxZV1bwJ19XGmH5_cIwlCBdzpOyCI4wo9-FVI4SLpDzZRkZsiXiowRxK38TSuZKbXONP8CAWupuDTXs-wuPNg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
انهدام یک پهپاد در نزدیکی میدان گازی «نپتون دیپ» رومانی
🔹
جنگنده‌های F-۱۶ رومانی در عملیاتی ضربتی، یک پهپاد انتحاری دریایی (USV) را در فاصله چند صد متری پروژه گازی «نپتون دیپ» در دریای سیاه منهدم کردند تا از بروز یک فاجعه در زیرساخت‌های انرژی جلوگیری کنند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/akhbarefori/682815" target="_blank">📅 16:48 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682814">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">♦️
اسوشیتدپرس: اسلام‌آباد برای ازسرگیری مذاکرات، با ایران و آمریکا در تماس است
🔹
مقام‌های پاکستانی می‌گویند رهبری سیاسی و نظامی این کشور همچنان با ایران و آمریکا در تماس است تا تلاش‌ها برای کاهش تنش و حرکت به سمت ازسرگیری مذاکرات را بررسی کند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/akhbarefori/682814" target="_blank">📅 16:43 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682813">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c1cf80d568.mp4?token=oOyWEwhYE0NwsHP4iZwbwX8BcDaXZlMZS5PzdhlTR_9zJai5em_cdiAS4i00NLAz_EEEZ-pdFBeQXVPDgZVvRdwGTFRxvPAj91UJKyZCj5-aE-aFlyRP8nO8q_XqLmneUrOVwrYymkfZAAler6jARC789HassY2UMl8np6HROe5nZTAdaJiWODyzLYnmp1wR2EX3ndQPws8n4dBcEgw27E19hT1QomHkQfDgCQcIMlYwJ6XQ6vt9eoKXPztj22bQa9Tcu3kkdwov3RlFmINXw2-oLVaEK8fa0NQOrlW2P_V9UvP2pDv4h86cRbLPE5a4hHD21d0BiUBiPyfYCLO9uhg43RaCQsaVELugKuGjH7nvf3X3D-g7GZQkma8mcBM61so4OhgBWv4Z2fRDrB6ipNb1wOTHSnKdOD8bNZOk2DCJFa_vsqDV7wBy8Fak6pmJyJesTPDJxCl1PqiiW7ZaeYDqIf1eaoRclBJz3PtaOXA9PMa6aYuOlngNvVwFHoF4OyUCaBluT1Juh2UMs5zNoj2C7NUWKrcXORBrISf-Vtdff_yeqkJRksWFRT-o-KI644OATaUGd7rjrlHCbN99VuD56bLJZ2vVssw_f31eOWvssnaSIBRP4fA6ae5_mqWRWpD9eCbWvIWJIvR3Sle7y02fvWNrmE9xENpVlZJw2I0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c1cf80d568.mp4?token=oOyWEwhYE0NwsHP4iZwbwX8BcDaXZlMZS5PzdhlTR_9zJai5em_cdiAS4i00NLAz_EEEZ-pdFBeQXVPDgZVvRdwGTFRxvPAj91UJKyZCj5-aE-aFlyRP8nO8q_XqLmneUrOVwrYymkfZAAler6jARC789HassY2UMl8np6HROe5nZTAdaJiWODyzLYnmp1wR2EX3ndQPws8n4dBcEgw27E19hT1QomHkQfDgCQcIMlYwJ6XQ6vt9eoKXPztj22bQa9Tcu3kkdwov3RlFmINXw2-oLVaEK8fa0NQOrlW2P_V9UvP2pDv4h86cRbLPE5a4hHD21d0BiUBiPyfYCLO9uhg43RaCQsaVELugKuGjH7nvf3X3D-g7GZQkma8mcBM61so4OhgBWv4Z2fRDrB6ipNb1wOTHSnKdOD8bNZOk2DCJFa_vsqDV7wBy8Fak6pmJyJesTPDJxCl1PqiiW7ZaeYDqIf1eaoRclBJz3PtaOXA9PMa6aYuOlngNvVwFHoF4OyUCaBluT1Juh2UMs5zNoj2C7NUWKrcXORBrISf-Vtdff_yeqkJRksWFRT-o-KI644OATaUGd7rjrlHCbN99VuD56bLJZ2vVssw_f31eOWvssnaSIBRP4fA6ae5_mqWRWpD9eCbWvIWJIvR3Sle7y02fvWNrmE9xENpVlZJw2I0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دانشکده فارس، مسیر درست ورود به حرفه خبرنگاری
ثبت‌نام بدون کنکور دانشکده رسانه خبرگزاری فارس آغاز شد.
این مسیر شامل:
آموزش‌های تخصصی
کار عملی در تحریریه خبر
رشته های تحصیلی  شامل :
🖊
خبرنگاری |
📸
عکاسی |
🎥
سینما و تدوین |
🎙
گویندگی |
🤝
روابط‌عمومی
📌
روش ثبت‌نام:
📱
ارسال عدد ۱۴ به سامانه ۵۰۰۰۱۰۱۴
🌐
ثبت‌نام از طریق لینک زیر اقدام نمائید
futurix.ir/go/rxDxXO
مهلت ثبت‌نام محدود است.
✅
اولویت با متقاضیانی است که زودتر اقدام نمایند.
🆔
ایتا:
@Farsnewsfaculty
🔹
مرکز آموزش علمی کاربردی خبرگزاری فارس
🔹</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/akhbarefori/682813" target="_blank">📅 16:42 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682811">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو فوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8fb044920a.mp4?token=jQvfajsqGqsqlMuuXqMncM4Gn-7-GsFor3zxkIYSphSFthljMp5X8TVv7PaAuodvsAXe_34g-ZrPpLzJ-1PGFpdweb_cGzgZql3l45xstCGG_MPZVMEGubiTc0K5mHvdJQimu2xDhv6xtdt8JBGzim50AKylmND_JAbTlx7KQLlbIWaoqS4wnzW0pNcp9XueyUXO_GgQLb_r0aR1hkPrdEfsue58rc4aTrLWy_Jel_ns0tiQ9_d4mgs5E5kqbWDhEM6-zfycVk7umh5C02-GohACkMKQppJfNgsnFig-dRbDICC1S6mlXwqDaHEf1hVbhJg4zEZDgNubMVaJW9TL3Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8fb044920a.mp4?token=jQvfajsqGqsqlMuuXqMncM4Gn-7-GsFor3zxkIYSphSFthljMp5X8TVv7PaAuodvsAXe_34g-ZrPpLzJ-1PGFpdweb_cGzgZql3l45xstCGG_MPZVMEGubiTc0K5mHvdJQimu2xDhv6xtdt8JBGzim50AKylmND_JAbTlx7KQLlbIWaoqS4wnzW0pNcp9XueyUXO_GgQLb_r0aR1hkPrdEfsue58rc4aTrLWy_Jel_ns0tiQ9_d4mgs5E5kqbWDhEM6-zfycVk7umh5C02-GohACkMKQppJfNgsnFig-dRbDICC1S6mlXwqDaHEf1hVbhJg4zEZDgNubMVaJW9TL3Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
روایت‌های شما از دلایل تجرد | چرا ازدواج نمی‌کنیم؟
🔹
بازتاب دغدغه‌های واقعی؛ روایت بدون پرده شما از بحران اشتغال، هزینه‌های سنگین و بن‌بست‌های مسیر تاهل.
🔸
پیام های صوتی خود را به آیدی زیر ارسال کنید
👇
@Ertebat_baforii
@Alo_fori</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/akhbarefori/682811" target="_blank">📅 16:35 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682810">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">♦️
جام جهانی ۲۱۱ تیمی به‌خاطر اسرائیل
🔹
نشریۀ اتلتیک از طرح محرمانۀ اینفانتینو برای «جام جهانی زیر ۱۵ سال» با ۲۱۱ کشور یعنی تمام اعضای فیفا پرده برداشت.
🔹
رئیس فیفا در این طرح قصد داشت بازی افتتاحیه را میان دو تیم فلسطین و اسرائیل برگزار کند که مورد قبول بسیاری از اعضای فیفا قرار نگرفت.
🔹
این طرح هرچند در ظاهر منابع مالی خوبی برای ۲۱۱ عضو فیفا داشت اما در پشت‌پرده به‌دنبال عادی‌سازی روابط فلسطین و اسرائیل بود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/akhbarefori/682810" target="_blank">📅 16:20 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682809">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5e8f254d3f.mp4?token=kAp-9G0-kP4t8yQAoInY91hUCf2oZyE5GPVRcYLAQjDKCRP1HP9AwYu66fdcvTNr-H7yLBA1G53zOqIpPavyH6quOi9K-XN23XzOvMJELTOqcnZiILZq8bnx6pnhcEi4N9QQMK6cINGfZQdAk3Zg_JqSAJola3IxGqXBBv6r-PYjSuGgCbTE16LDH_tN7EFC8EyMueGlMjPF8VV4UBe_ioz4oTfxsXWGpUsbhK-QbAWYzYwiUoCnly-W1tmb9sahCCAXE93mQECEQ9sbEk3BR8g-nbmsSUTBicaFcaDT50DXg9fUFc2L_BN7JrnBqBEzoNp1d-U-EyOaUgJaRFpaCQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5e8f254d3f.mp4?token=kAp-9G0-kP4t8yQAoInY91hUCf2oZyE5GPVRcYLAQjDKCRP1HP9AwYu66fdcvTNr-H7yLBA1G53zOqIpPavyH6quOi9K-XN23XzOvMJELTOqcnZiILZq8bnx6pnhcEi4N9QQMK6cINGfZQdAk3Zg_JqSAJola3IxGqXBBv6r-PYjSuGgCbTE16LDH_tN7EFC8EyMueGlMjPF8VV4UBe_ioz4oTfxsXWGpUsbhK-QbAWYzYwiUoCnly-W1tmb9sahCCAXE93mQECEQ9sbEk3BR8g-nbmsSUTBicaFcaDT50DXg9fUFc2L_BN7JrnBqBEzoNp1d-U-EyOaUgJaRFpaCQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصادف عجیب دو دختر نوجوان موتورسوار با تریلی در ابهر
🔹
دو دختر نوجوان موتورسوار روز گذشته در میدان ترمینال ابهر با تریلی پارک‌شده برخورد کردند و مصدوم شدند.
#اخبار_زنجان
در فضای مجازی
👇
@akhbarzanjan</div>
<div class="tg-footer">👁️ 33.2K · <a href="https://t.me/akhbarefori/682809" target="_blank">📅 16:16 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682808">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">♦️
پلتفرم طلایی مسدود شده، مربوط به جنگ ۱۲ روزه بود/ پلتفرم‌های طلا به فعالیت خود ا‌دامه می‌دهند
رضا الفت‌نسب رئیس اتحادیه کسب‌وکارهای مجازی در همایش زرآتی اقتصادآنلاین:
🔹
یک سوبرداشتی در رسانه‌ها شده که نگرانی‌هایی را برای کاربران ایجاد کرده است که می‌خواهم شفاف‌سازی کنم.
🔹
موضوع پلتفرم مسدود شده به جنگ ۱۲ روزه برمی‌گردد که در آن زمان حساب‌ها مسدود شد. مجموع این اختلالات منجر به این شد که فعالیت پلتفرمی دچار مشکل شده، متوقف شود.
🔹
این که در خبرها آمده مبنی بر اینکه ۲۰۰ هزار خالی فروشی صورت گرفته، چنین چیزی را نشان نمی‌داد؛ بلکه ۲۰۰ هزار کاربر داشت و شکایاتی هم که به اتحادیه رسید کمتر از ۱۰۰ فقره بود/ اقتصادآنلاین
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/akhbarefori/682808" target="_blank">📅 16:13 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682807">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/58c0e4ce1c.mp4?token=SNyIQwrH_V8D5twoKlg2Ozy_5gkLOkeAin6SI2VqOQUzzRd_tLH10W6Dk6jqXrZ9gXWA_47xrH_y93jpzJtDZIPernO10FoPtAn21ITJoEPI6HCcTlM7qJH0YJU1v6JUPr9Y_gsOjN465jGgpsta45vM0DZU9HXiUe1DIV8k_Rc6LFl3dqjPILYTzUb5CE6CwMf6h__7JCcZoqjDRTYXOGiAWmWS-ULMccy_QH66IIEoeQ9UPbHNp3DBB83ptw7t9PqScY1nZEQolU8o4twQbuXzdRAWRaramBOdoAzKErxFKFboVX5Ztw6UJeY4M-l7K-c42Pte2unA6ztZld1QRA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/58c0e4ce1c.mp4?token=SNyIQwrH_V8D5twoKlg2Ozy_5gkLOkeAin6SI2VqOQUzzRd_tLH10W6Dk6jqXrZ9gXWA_47xrH_y93jpzJtDZIPernO10FoPtAn21ITJoEPI6HCcTlM7qJH0YJU1v6JUPr9Y_gsOjN465jGgpsta45vM0DZU9HXiUe1DIV8k_Rc6LFl3dqjPILYTzUb5CE6CwMf6h__7JCcZoqjDRTYXOGiAWmWS-ULMccy_QH66IIEoeQ9UPbHNp3DBB83ptw7t9PqScY1nZEQolU8o4twQbuXzdRAWRaramBOdoAzKErxFKFboVX5Ztw6UJeY4M-l7K-c42Pte2unA6ztZld1QRA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مهم‌تر از درس‌های مدرسه، اموزش این پنج قانون مالیه که آینده فرزندتون رو‌ می‌سازه  #دارایی_هوشمند
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/akhbarefori/682807" target="_blank">📅 16:12 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682805">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">♦️
بانک مرکزی: در ادامه اجرای حکم دادسرای جرائم اقتصادی؛ اسناد انتقال دارایی‌های تعاونی اعتبار منحله مولی‌الموحدین و بانک ایران زمین به بانک مرکزی امضا شد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/akhbarefori/682805" target="_blank">📅 16:03 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682804">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/55cbce766c.mp4?token=W24XJ9n8mHl6t9oi5w2tj-t1svqDdmP5y3O2FLZKuG6S376z6QgY70H3mmr2svMkt-wynyRQtCv7ZtYXNyhY5BWM8WNVlUQMGPT9-1xKZHRFCRRdUp0wQQNrZs34ryAbiQoQ22YgyuabtALeCBBcSG2LRYJNg3rU_sPDJGzDCWzsNNaibZ40tADudMLJK7dkQ6mQu1wW-sBXwFNdWWa6fkF9uSOEEgkQy2XGSjSC4YY5twJx_0BqQuEp5GXMete_AwXHYztO8FLTezMkDmZrF4RFNnyA7R4Yp_hs5HHRe2DSXv-2Ptx9VCjk34a1zvCRQxnwWqZxGCOvSBXFYng-gYgCEvcFzKpmn7lin0cGPymVReElVsT9V2qdQKnF_qVKvXjcOociudffZlW_3QG6Xmy0cVWyYOC0v7ugyqZRspfpBft1DTWPhMYlHeHpLlMvAibO8venMjIaRSaaPJ3y9Vx8fCfrwAIC7Zs141RitrZgAlGK9-pRnOYI9N8ZiwAEe4q8w4scMOVYD14dv4MY5NhF-zdtLAQudBQkGROiNTNV5LwiUEOAaEd2LiH-0U7zKVmvV7V-IYCE7XxyOug1lAsh9rcwKz9eErjWQMDvsXJ-SIqluJlVQBSvK13awfgopjQ5M36m09M1x9TWolmoyqTjz35npjyJOYNzRj-R-oA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/55cbce766c.mp4?token=W24XJ9n8mHl6t9oi5w2tj-t1svqDdmP5y3O2FLZKuG6S376z6QgY70H3mmr2svMkt-wynyRQtCv7ZtYXNyhY5BWM8WNVlUQMGPT9-1xKZHRFCRRdUp0wQQNrZs34ryAbiQoQ22YgyuabtALeCBBcSG2LRYJNg3rU_sPDJGzDCWzsNNaibZ40tADudMLJK7dkQ6mQu1wW-sBXwFNdWWa6fkF9uSOEEgkQy2XGSjSC4YY5twJx_0BqQuEp5GXMete_AwXHYztO8FLTezMkDmZrF4RFNnyA7R4Yp_hs5HHRe2DSXv-2Ptx9VCjk34a1zvCRQxnwWqZxGCOvSBXFYng-gYgCEvcFzKpmn7lin0cGPymVReElVsT9V2qdQKnF_qVKvXjcOociudffZlW_3QG6Xmy0cVWyYOC0v7ugyqZRspfpBft1DTWPhMYlHeHpLlMvAibO8venMjIaRSaaPJ3y9Vx8fCfrwAIC7Zs141RitrZgAlGK9-pRnOYI9N8ZiwAEe4q8w4scMOVYD14dv4MY5NhF-zdtLAQudBQkGROiNTNV5LwiUEOAaEd2LiH-0U7zKVmvV7V-IYCE7XxyOug1lAsh9rcwKz9eErjWQMDvsXJ-SIqluJlVQBSvK13awfgopjQ5M36m09M1x9TWolmoyqTjz35npjyJOYNzRj-R-oA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سیر؛ یک خوراکی کوچک با خواص بزرگ!
🧄
🔹
سیر سرشار از ترکیبات مفیدی است که می‌تواند به حمایت از سلامت قلب، تقویت سیستم ایمنی و حفظ سلامت عمومی بدن کمک کند. بهترین نتیجه زمانی به دست می‌آید که در کنار یک رژیم غذایی متعادل و سبک زندگی سالم مصرف شود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/akhbarefori/682804" target="_blank">📅 15:50 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682803">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MzNh3UFM8GZD0WvJnbD0_bZswjZzdj8lg3Ov7u8XAOj020RzncGG9_ChQahCfU2wq5gGuXies2Z-HDDeDfY2LJOPxKOgd6baniPhqmDULbWSVFso9Fizu4rd0dzpdm4-8nsijCQlEhM1_toDwS9_Lo8mb4Vj3wVh6RagV8z-qxBUTBJbPmgj6YRp11AXRT_Z8MkurBEVze_rYBY0yqiNNpPGKz5BoU9jCtLPLPNjgzMr61SF0O8D7aix6hTfuvMpLq4BinYQxeY56UlZbFPWB-DMK2DIwjpVkjqQfrt98Eb3coDugCVwfneX6TxPux4kusPnw6ArIehNu6S8S1CVKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
عکسی از دنسه هتل گیلاریا، فینالیست Architecture Photography Awards 2026 شد
🔹
عکسی از دنسه هتل گیلاریا که توسط امیررضا دهنادی ثبت شده، به مرحله نهایی رقابت‌های Architecture Photography Awards 2026 راه یافته و در میان آثار فینالیست این مسابقات بین‌المللی عکاسی معماری قرار گرفته است.
🔹
راه‌یابی تصویر دنسه هتل گیلاریا به مرحله نهایی این رقابت، در کنار حضور آثار عکاسان بین‌المللی، بازتابی از معماری و فضاهای اقامتی ایران در یک رویداد تخصصی جهانی عکاسی معماری است. این هتل در استان گیلان، بندر کیاشهر واقع شده است.
🔹
برندگان نهایی Architecture Photography Awards 2026 قرار است ۲۲ آگوست ۲۰۲۶ معرفی شوند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.2K · <a href="https://t.me/akhbarefori/682803" target="_blank">📅 15:47 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682802">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
یارانۀ ۳۰۰ هزار تومانی مرداد به حساب سرپرستان خانوار دهک‌های ۴ تا ۹ واریز شد
.
🔹
رئیس مجلس به کربلا رسید.
🔹
روس‌اتم: به ساخت نیروگاه‌های هسته‌ای در ایران ادامه می‌دهیم.
🔹
دفتر زلنسکی درخواست وزیر دفاع سابق برای برگزاری انتخابات را رد کرد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/akhbarefori/682802" target="_blank">📅 15:41 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682801">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">♦️
مزدوران سعودی اینترنت استان مأرب یمن را قطع کردند
🔹
منابع محلی در استان مأرب گزارش دادند که مزدوران وابسته به عربستان سعودی در ادامه اقدامات ضدانسانی خود، دسترسی مردم به اینترنت و خدمات ارتباطی را در این استان قطع کرده‌اند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.4K · <a href="https://t.me/akhbarefori/682801" target="_blank">📅 15:24 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682800">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/07c271daa3.mp4?token=ptlKBkYhyCM9xex3omyhLJmKQNICRqLas7s-0L6CmcZt7j3e_yaguOrDSak_SuboyzCfcmqI7fzXaA3lilTw-w7Az6cCTpGx_5k1ULABsOimDG-UuMEQcPWoBuu6tGQ9USPRw-fkB3UfhvkM3WzJZlKysBopYWkUdb5PizsG-pTIUso6dI7-Vhfgppsk0m-ALpE2LNuE3lNEjTE3umTgSCb9h5oI0zYBFacYMMRWW0j8PsKqDDIzwUfbFVNnuoJow7Iifc52hDmPexhyiB5beOtMITxoc3FCLs2YgOTHYhsIgsYf2aovNkqLLx-wIg-gIFkgpgQ3DwgHhpHpOfXM3w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/07c271daa3.mp4?token=ptlKBkYhyCM9xex3omyhLJmKQNICRqLas7s-0L6CmcZt7j3e_yaguOrDSak_SuboyzCfcmqI7fzXaA3lilTw-w7Az6cCTpGx_5k1ULABsOimDG-UuMEQcPWoBuu6tGQ9USPRw-fkB3UfhvkM3WzJZlKysBopYWkUdb5PizsG-pTIUso6dI7-Vhfgppsk0m-ALpE2LNuE3lNEjTE3umTgSCb9h5oI0zYBFacYMMRWW0j8PsKqDDIzwUfbFVNnuoJow7Iifc52hDmPexhyiB5beOtMITxoc3FCLs2YgOTHYhsIgsYf2aovNkqLLx-wIg-gIFkgpgQ3DwgHhpHpOfXM3w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آتش‌سوزی در شهر نجف
اشرف
🔹
دقایقی پیش گزارش‌ها از وقوع حریق در یکی از ساختمان‌های در حال ساخت واقع در محله «عدن» در شهر نجف اشرف خبر دادند. تیم‌های امدادی و آتش‌نشانی برای مهار شعله‌ها به محل حادثه اعزام شدند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.3K · <a href="https://t.me/akhbarefori/682800" target="_blank">📅 15:22 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682799">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromموسسه نیکوکاری مهرآفرین پناه عصر</strong></div>
<div class="tg-text">📹
حوا و دخترانش سال‌ها خشونت را تحمل کردند و امروز با ترس دیگری روبه‌رو هستند؛
بی‌خانمانی.
🌿
پنجشنبه مهرورزی این هفته ؛ برای تأمین ودیعه مسکن مادران و کودکان در معرض بی‌خانمانی همراه می‌شویم.
💳
6037991199529904
💳
6037991199506100
💳
6037991199500038
🔖
IR710170000000216780692009
📲
*780*35260 #
📌
کمک مستقیم به حوا و دخترانش، واتساپ و تلگرام:
📲
+989101785282
🔻
پرداخت مستقیم
Mehrafarincharity.com
⭐️
مهرآفرین باشیم
|
اینستاگرام
|
وب سایت
|
پرداخت آنلاین
|
❤️
@mehrafarincharity</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/akhbarefori/682799" target="_blank">📅 15:21 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682797">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3df6be216f.mp4?token=AZA2LogkdEq_-svB48mIYI4bysRMevO6VCNRhSqbrcLFXrI_pSMFmJRaH_JkV346blvKAFBpGzgw52_6hYp9ihxs_8xnbfnmd8pzhKEajA-XYgAklwNkUoZsCrJZrTaUkkokcyYxkimCU6mrgds76697Q12fkyMvqGdBclcYy30LdGXQqWM6xMzvC45bnuCaNQ9_BOMXDvfMKEXn45K5nytDNpm65TPVsF_VFF0YfZQkmSWUKrQxKqj7N0AY_RAx00K3jUBQ6sE_xj0S2Ws4I5UfLDYXt-ClTLi9mIrYZSRcuZxuyj2UPLfAbT0o4pFRoM3laraCxd-jUZLd3YAE3AcQhq1gw2irxwJY17VFqVi4hiw5Wkqg7jhH-_aBYE7ojnT4WsUTNFPL7CkqJ3xw6SwFUaaB1onVcBxyinybfWXPjxTwYYLOj7LcZ-AHjX4DeZiarYoomnwygaZSnm5FXcwyZw9s91kNYXCA8w4UxZPyGGw77u8sOUaGXWRV_IP6Xw-JF5AO87FZA7R4JpV1CtlPFf6aqOb8LK09RbC3VQeXrcv0aF0ZA1eJiFR8EYXm6HkvtaijTkHMQWX27RKMHRMcZEDmQH58o3pY7o8WElB0b_VFlCJiQQdr4XqMhqQ_1zoh5n-vDWnX3Z7pCecE3Q4q9D35W3mC5Ie4wJYpA8M" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3df6be216f.mp4?token=AZA2LogkdEq_-svB48mIYI4bysRMevO6VCNRhSqbrcLFXrI_pSMFmJRaH_JkV346blvKAFBpGzgw52_6hYp9ihxs_8xnbfnmd8pzhKEajA-XYgAklwNkUoZsCrJZrTaUkkokcyYxkimCU6mrgds76697Q12fkyMvqGdBclcYy30LdGXQqWM6xMzvC45bnuCaNQ9_BOMXDvfMKEXn45K5nytDNpm65TPVsF_VFF0YfZQkmSWUKrQxKqj7N0AY_RAx00K3jUBQ6sE_xj0S2Ws4I5UfLDYXt-ClTLi9mIrYZSRcuZxuyj2UPLfAbT0o4pFRoM3laraCxd-jUZLd3YAE3AcQhq1gw2irxwJY17VFqVi4hiw5Wkqg7jhH-_aBYE7ojnT4WsUTNFPL7CkqJ3xw6SwFUaaB1onVcBxyinybfWXPjxTwYYLOj7LcZ-AHjX4DeZiarYoomnwygaZSnm5FXcwyZw9s91kNYXCA8w4UxZPyGGw77u8sOUaGXWRV_IP6Xw-JF5AO87FZA7R4JpV1CtlPFf6aqOb8LK09RbC3VQeXrcv0aF0ZA1eJiFR8EYXm6HkvtaijTkHMQWX27RKMHRMcZEDmQH58o3pY7o8WElB0b_VFlCJiQQdr4XqMhqQ_1zoh5n-vDWnX3Z7pCecE3Q4q9D35W3mC5Ie4wJYpA8M" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
عظمت کیهان باور کردنی نیست
!
🌍
🔹
محاسبات علمی نشون داده که عالم ما با این عظمت و بزرگی فقط یکی از بی‌نهایت عالم ممکن است
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/akhbarefori/682797" target="_blank">📅 15:14 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682796">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
مشاور امنیت ملی عراق در دیدار با قالیباف: بغداد بر تقویت روابط راهبردی با ایران مصمم است.
🔹
آنکارا: تهدیدهای نتانیاهو علیه ترکیه و سوریه، نشانه انزوای اوست.
🔹
آلمان و ایتالیا همکاری‌ها برای مهار هجوم پناهجویان را تقویت می‌کنند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 33.5K · <a href="https://t.me/akhbarefori/682796" target="_blank">📅 15:08 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682795">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">♦️
بینی‌مو عمل کنم، خیلی کیوت میشم!
🔹
فقط بینی نیست، وقتی عمل زیبایی از سن کم شروع میشه، خیلی وقت‌ها بعدش یه ایراد جدید پیدا میشه و دوباره نوبت تغییر دادن یه جای دیگه‌ست.
🔹
انگار این روزا بعضیا تا وقتی چند جای صورتشون رو عوض نکنن، باور نمی‌کنن خوشگلن!
🇮🇷
✊
…</div>
<div class="tg-footer">👁️ 35.3K · <a href="https://t.me/akhbarefori/682795" target="_blank">📅 15:00 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682794">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">♦️
نگرانی امارات نسبت به تبعات اقدام ضد ایران
🔹
روزنامه وال استریت ژورنال به نقل از منابع آگاه گزارش داد که آمریکا از امارات خواسته فشارهای اقتصادی علیه ایران را تشدید کند.
🔹
این در حالیست که مقامات اماراتی بیم آن دارند راهبرد آمریکا در قبال ایران به بخش‌های اقتصادی کشورهای حوزه خلیج فارس ضربه وارد کند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35K · <a href="https://t.me/akhbarefori/682794" target="_blank">📅 14:55 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682793">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">♦️
اعتصاب کارکنان، فرودگاه بن‌گوریون تل‌آویو را به تعطیلی کشاند
🔹
منابع خبری از آغاز اعتصاب گسترده کارکنان در فرودگاه «بن‌گوریون» در تل‌آویو و ترک محل کار توسط پرسنل این فرودگاه خبر دادند.
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 36.6K · <a href="https://t.me/akhbarefori/682793" target="_blank">📅 14:49 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682792">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6073d64997.mp4?token=GJg4IIQ-62Os8KoNQbxAoId8hmxmvaHLUwVfAuQ8FjyX0RjX0vLfZSaCIgwdj0sj7qyJ09EuBWuyk_6RXqVoyXRh8C6aNZWRnktoDy-YYUNPFS5WRQb4sFgbGXe9J1q7VN61Sf3t-R9sfalIBuN8vOdAUYxsmHv24_FSALja87OcGCoM4mNTPhjRlc_RIXg1rycHO8oDW31EjS5DqR4e1e7W05mTo-CSp_em0DWnx0Z3KeZUUaOQefDjroXw31FwxUQIUF0FYMger4f2Ja1L1tQsK-DTEE2hvqwUwGUkx7_h7EtxlnRWdhGJxN9J_UE4iFaNqC-bgHql3I0hNsROtA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6073d64997.mp4?token=GJg4IIQ-62Os8KoNQbxAoId8hmxmvaHLUwVfAuQ8FjyX0RjX0vLfZSaCIgwdj0sj7qyJ09EuBWuyk_6RXqVoyXRh8C6aNZWRnktoDy-YYUNPFS5WRQb4sFgbGXe9J1q7VN61Sf3t-R9sfalIBuN8vOdAUYxsmHv24_FSALja87OcGCoM4mNTPhjRlc_RIXg1rycHO8oDW31EjS5DqR4e1e7W05mTo-CSp_em0DWnx0Z3KeZUUaOQefDjroXw31FwxUQIUF0FYMger4f2Ja1L1tQsK-DTEE2hvqwUwGUkx7_h7EtxlnRWdhGJxN9J_UE4iFaNqC-bgHql3I0hNsROtA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
هانتر بایدن پسر رئیس‌جمهور سابق آمریکا: ترامپ اصلا نمی‌داند تنگه هرمز کجاست
🔹
من عمیقا نگرانم که چطور کسی که این‌قدر جاهل و نادان است در دفتر بیضی کاخ سفید نشسته.
🔹
فقط این نیست که رشوه‌خوار، بی‌رحم و فاسد باشد. او یک احمق کامل و تمام‌عیار و جاهل مطلق هم هست.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.3K · <a href="https://t.me/akhbarefori/682792" target="_blank">📅 14:48 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682791">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ad39f16043.mp4?token=GKZKvDImTyJ_bi-X8y-hFtQDE6MThaKRQKBx619X42wHypR4kf8t-x79qQrdtyhTve2IryeF8vDZv7a2alKANRmH0jxesvjs3ur_fCK1GGuaAp7SvWifAt-mqbEAUXLNQlOOTxhBCVhb0Dr0mvRPLRJEVG2_ARLzy3Y2CU1-idOVpJ0fehWIgwFVzwQJg_cjeAvOHLyTLazHGo18SxetVlrDlSoBtRaDy1AnAixfQPc1BoZdZs63rVaCrLnq9Sa7qOTc_vG6Hq2wvjR3TQHvVMsPSbES3hJb0z4m9NOAlEYnbSPUlk87t1Ni4KKJf9mbg7bZVcS4zhuYe_-W9GGceIhmSZFfxKE54XZI1r8eqvPJPLUDnUur61QgIeKJHw_XW4Rci6gfO4hViMoQV1SWT-yrl6db0pLmymG9VRSwp6gGH229xdXBT86euwqDE552ictLa7DXzGp2hutj-zG2vt_dpD4mWpwx1QX2x8vNL-8asY1ByNVSn7DNmCF33lxoXeRzKFKZ3PEblonJi9by-ifhhmGsYaHuJzj5JTDQNtgLfLDGU-wbVEIvGauanJh0nvDZVk75zpaIXb8yzUN9gVqMSs625o-hPmy3ijcmtECXGoq070sQgyp2a-3oiKPhzLUcvZVFTUMcgEHki5yJ80BRSuRcBMPXtD4Tf5fwwQE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ad39f16043.mp4?token=GKZKvDImTyJ_bi-X8y-hFtQDE6MThaKRQKBx619X42wHypR4kf8t-x79qQrdtyhTve2IryeF8vDZv7a2alKANRmH0jxesvjs3ur_fCK1GGuaAp7SvWifAt-mqbEAUXLNQlOOTxhBCVhb0Dr0mvRPLRJEVG2_ARLzy3Y2CU1-idOVpJ0fehWIgwFVzwQJg_cjeAvOHLyTLazHGo18SxetVlrDlSoBtRaDy1AnAixfQPc1BoZdZs63rVaCrLnq9Sa7qOTc_vG6Hq2wvjR3TQHvVMsPSbES3hJb0z4m9NOAlEYnbSPUlk87t1Ni4KKJf9mbg7bZVcS4zhuYe_-W9GGceIhmSZFfxKE54XZI1r8eqvPJPLUDnUur61QgIeKJHw_XW4Rci6gfO4hViMoQV1SWT-yrl6db0pLmymG9VRSwp6gGH229xdXBT86euwqDE552ictLa7DXzGp2hutj-zG2vt_dpD4mWpwx1QX2x8vNL-8asY1ByNVSn7DNmCF33lxoXeRzKFKZ3PEblonJi9by-ifhhmGsYaHuJzj5JTDQNtgLfLDGU-wbVEIvGauanJh0nvDZVk75zpaIXb8yzUN9gVqMSs625o-hPmy3ijcmtECXGoq070sQgyp2a-3oiKPhzLUcvZVFTUMcgEHki5yJ80BRSuRcBMPXtD4Tf5fwwQE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گاهی یک تصویر، بیشتر از هزار کلمه حرف برای گفتن دارد؛ روایتِ آدم‌هایی که برای ایران، از دل و جان ایستاده‌اند
🇮🇷
#همه_باهم_برای_ایران
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 34.4K · <a href="https://t.me/akhbarefori/682791" target="_blank">📅 14:47 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682789">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">🧠
شما چه تیپ سرمایه‌ گذاری هستید؟
تصمیم های مالی ما همیشه فقط بر اساس منطق و محاسبات نیستند. ترس از ضرر، هیجان، اعتماد به ‌نفس و میزان تحمل ریسک هم میتونن روی انتخاب‌ هامون اثر بذارن.
به همین دلیل ممکنه دو نفر با سرمایه و اطلاعات مشابه، تصمیم های کاملا متفاوتی بگیرن چون شخصیت و رفتار سرمایه‌گذاریشون یکی نیست.
یک تست جالب هم برای شناخت همین ویژگی‌ ها طراحی شده که با چند سوال، تیپ سرمایه ‌گذاری شما رو مشخص میکنه.
🔗
https://ifrb.ir/rknt</div>
<div class="tg-footer">👁️ 35.1K · <a href="https://t.me/akhbarefori/682789" target="_blank">📅 14:36 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682788">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5df511ba0d.mp4?token=hPyvqhn7Df--GAGtN3tQkrqvYmTno_FEUcVsMc55ko99V-_XuqoskbYK8dvbV8x9bxYfx00zz6DRIEQejfs-fBUVOTZSKQJ6AlzAAj28Xx8WjtdneJIRLg4H-tVUbMXBfGiWBibcXw6g7yoknuO9NFp81hzJ43zR7yn5LwQOq47NuDTq-Ft77SnhkGCSsUF1G9U9CTa-A9umK14POmMRrUQEpr3xcRqM876SoI2OrQklWGQaJ6XB9qpn4cXFOtLcQ3qLdwcRswJBU7BEY1KIt5h1kSIckJjcyT2qKRWC6IYKRSjX9CMy_abPzvfFI7aXV7rDPdfdTFLnMWoAcfbLVA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5df511ba0d.mp4?token=hPyvqhn7Df--GAGtN3tQkrqvYmTno_FEUcVsMc55ko99V-_XuqoskbYK8dvbV8x9bxYfx00zz6DRIEQejfs-fBUVOTZSKQJ6AlzAAj28Xx8WjtdneJIRLg4H-tVUbMXBfGiWBibcXw6g7yoknuO9NFp81hzJ43zR7yn5LwQOq47NuDTq-Ft77SnhkGCSsUF1G9U9CTa-A9umK14POmMRrUQEpr3xcRqM876SoI2OrQklWGQaJ6XB9qpn4cXFOtLcQ3qLdwcRswJBU7BEY1KIt5h1kSIckJjcyT2qKRWC6IYKRSjX9CMy_abPzvfFI7aXV7rDPdfdTFLnMWoAcfbLVA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اعتصاب کارکنان، فرودگاه بن‌گوریون تل‌آویو را به تعطیلی کشاند
🔹
منابع خبری از آغاز اعتصاب گسترده کارکنان در فرودگاه «بن‌گوریون» در تل‌آویو و ترک محل کار توسط پرسنل این فرودگاه خبر دادند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.5K · <a href="https://t.me/akhbarefori/682788" target="_blank">📅 14:36 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682784">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nzrHyTjHhfWc3pVMASSHf9qSgdVnBgYCcemW19NNRPYFRf24uC47fqtKWViisoIfOREnRcKRSJwyuRdJ6ulLASdVGsRLXyf9GRKIfZI4wKxlZXSKnBqNJjFHin3Bnoelp9czje9txfUZCOgJnUfTLXw580SCjtxfFvV1erWlW5tjjNqRYkhewafuWoP29ng_AoS1XIB-tNOy5Ctnu79yNPpT5v9blhIJFj2-oaENhY1c7KNplWYiP9THqZ2GLWueI2wfD3AEq6y7wW6khPElvkI5ieojN5jKz3UqpFSBNDz35gECPR0GCBGADq13nB7dgYIMDkhHmf93iA0SVW76nA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
طبیعت زیبای ترکمن صحرا، گلستان
#اخبار_گلستان
در فضای مجازی
👇
@AkhbareGolestan</div>
<div class="tg-footer">👁️ 38K · <a href="https://t.me/akhbarefori/682784" target="_blank">📅 14:21 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682783">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b81RmSTUvPe0zjnm_VSviqVzfAOOciazU76QYpqCuYxCEa2H07IZHc9HjdUfc8_6f-cr5q7caak28kn6iOmCUgALUSdY5jXBhiS4FN1TVUT-otJYbJO3OpZCWi9FfDlqwb9Iha6cuzrs0HY8LcgirDEYnUoGe3GN0kiRZeOcFBqEMT3HGtKYgbzj8gRrt3zpKgemGs9td5wBufqUb-e-VvYhnfpkhAjB64otMs-T_7cuMCaBble98l2rY7_1Ko55YJV6bTA8oZ7a5i6A2k4gL3x2u8Bc_2k4OQqa79HcwhoBZG0r23zpHe8sbvU8sLgRrDOz0U6kHjYTYFgaaSf6Hg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
این ست‌های رنگی خاص مخصوص آقایونیه که می‌تونن شهر رو زیباتر کنن
#فوری_استایل
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/akhbarefori/682783" target="_blank">📅 14:02 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682781">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7ec60087df.mp4?token=pLTVaDBMbEj9H_Jq6-V390vRwIcorkkCQ3ddICeCXm2UiOebs2sN3pJXPycbuLuB_b8qyCbBaRk_pbt0hQZ3VTDQaTTJYEuN-F4Vbp4snFZzzTPvgHI84dzQvtRhDfWwgKnq06lVwIikkzlK8zDV3EUFbT4uNUAh6miCNrIyBahvr_Uh2ic452UblQsx3PLBlASpIV3SuyGleqlgO9l6P3I3icxO3XmlLdc_cwtloJrBZCfMsYViiHtky6DHxY3lRJ99TkyFjUaRj0jcP_wM51LmUH13exFuCu8kBvGQ22mMVPulERZxcJb98RdLvEpwZlR9HqD5am71PhXuAPDpOA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7ec60087df.mp4?token=pLTVaDBMbEj9H_Jq6-V390vRwIcorkkCQ3ddICeCXm2UiOebs2sN3pJXPycbuLuB_b8qyCbBaRk_pbt0hQZ3VTDQaTTJYEuN-F4Vbp4snFZzzTPvgHI84dzQvtRhDfWwgKnq06lVwIikkzlK8zDV3EUFbT4uNUAh6miCNrIyBahvr_Uh2ic452UblQsx3PLBlASpIV3SuyGleqlgO9l6P3I3icxO3XmlLdc_cwtloJrBZCfMsYViiHtky6DHxY3lRJ99TkyFjUaRj0jcP_wM51LmUH13exFuCu8kBvGQ22mMVPulERZxcJb98RdLvEpwZlR9HqD5am71PhXuAPDpOA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
رانندگی خودران؛ بهتر از راننده انسانی؟
🔹
راننده یک خودروی مجهز به سیستم خودران می‌گوید این فناوری حتی بهتر از خودش رانندگی می‌کند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.3K · <a href="https://t.me/akhbarefori/682781" target="_blank">📅 13:43 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682779">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kSr4RCAsKqcrR-PaCFtorVwweap7BjgQ1QtMfQgesWGaAahMr_xmXFcBGAjnd8v9Ooel6amQo8O_wCtaAoF_bs0gKo8N3PRzWPw5n4MXegQTX8AuZh-5bxYBdkM8OVAqEBJgg9nWW56dSnS_D3O_S1mhNX7PzIa3hIMeM4cAlFG2dcvqiOzaGMVSQhCxMt2HhGVYrGfVgMmYIC8-cx6fTx5j7OUEttZHLyoORoJIn_8E1O6yP89Ba1igvmJhYf_ae7pLjo3Hf6tunniYxKeiAOrGgOfIIZymR_8AQIKB0SwwTW3_sYU544k7mZ9zgKHAr_hc9jPgwYNaMX994lk0YA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تصویر متفاوت از آزمون سراسری در دانشگاه امام صادق(ع)
#اخبار_تهران
در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 39.2K · <a href="https://t.me/akhbarefori/682779" target="_blank">📅 13:31 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682778">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromتیتر تجارت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t_5pzOIRJfGU_9X4C5yZj2k-A6pSM9rjjUuSHnqBiuQm_nGLosoaR0FsXuIgL5q-L-4rib3EUXTFdvxjohKIOjziqCnaMj-5IFRZliJIYql7mM94sG0_q-Hdox9zBhIFHSc2IAwaxiubF1Kc5PjPXTL0dnrz7cUdkF-7pM23FnScXZvyjX1x9yimQaiyg8JEeECYxseO--TbAv0M6hPpPsVStPUhH_sFGXmKv3aoF9ENVKWhHrXfC_2BXainrHpQb_OtPlRsPl_FA-2mlzymco6FtOs22n38RT-mRRqEeX3A4p9W2Rk9EGqUjumNIPj1fRHrhmGDA4VoKgZFPnpDlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
#نبض_بازار
| قیمت طلا و ارز؛ امروز ۲۹ مرداد ۱۴۰۵؛ ساعت ۱۳:۲۰
🔹
بازار طلا و سکه امروز با روند افزایشی آغاز شد و هر گرم طلای ۱۸ عیار وارد کانال ۱۹ میلیون و ۸۹۲ هزار تومان شد و سکه بهار آزادی نیز به سطح ۱۹۵ میلیون تومان رسید./تیترتجارت
@Titretejarat</div>
<div class="tg-footer">👁️ 39.6K · <a href="https://t.me/akhbarefori/682778" target="_blank">📅 13:28 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682777">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WrzvUl1a4ypqVgDkIoVREgT7fkhNiHwuE3sZj2O0t4N05ReBDmWgU6b0gPeK4esjDaCfjHoygct7Hpq-IllyLfj9y4ZkgUwNY-BHHH6x1xtg99C3G2UIGTQDKY_zLypN0pkGWEc3kBUv863lP0aXRsmo7SFHVH00JoJXmLQ4OFd07UNNVKKFiSQCtRbJn63z0FuXK44TSNHY5rTnBkplFDkfL8oFc3eFqNyxISG6QkjlLhTnjx_g8jpXyLtUq9JQqYfIkvCVejrIAVvAcwIdMOJmI8yNDKHRYgqAeKq5HfCKFJCFcTPC6X0AAlYRP6Sg5z087sSM5a_YBCsxK_aYWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
وقوع حادثه امنیتی در نزدیکی سواحل یمن
🔹
این منابع عنوان کرده‌اند که قایق‌های کوچک به یک نفتکش در شرق مکلا در یمن نزدیک شده‌اند و نفتکش درخواست کمک کرده است.
🔹
سازمان عملیات تجارت دریایی بریتانیا هم اعلام کرد گزارشی از یک حادثه در ۱۳۶ مایلی شرق مکلا در یمن دریافت کرده است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/akhbarefori/682777" target="_blank">📅 13:26 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682776">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c5e038ed65.mp4?token=t9kmUA-g6MkeIAotGRKJZnB2liDGn_Dgog63fp8D29Lpw7Ss9lVnK1qcZzAfvBD1V9OC-nsihW_8vq2Yg0-JPx0Fbm8dQMipVlrFuFNGbXqVHx7X9NGWEMM92vc9aDLm2zN0TnCXAJp_ius9iEg7R9Y_xO1toTbj5j-E4GjGMKQiKArfcBYDCp0cmDwLJyzGlzcV3o0u58aIikLJQeQcGBtQpXw5Ogu3NxEMZTB-w-Jn6htXIAwTQDXm7Ipu7sEuGTIJo90UwZNDoEY8rHkfNlpGELDedstWwBfXvtYLXn1ez6DzGY0CmpQ1RXN-AWbCSVBD1bbzpGOixI53Y7M_8Y6TH4DM9rGXvkSnMsOJPqmg7qG0Y6liqDOKcNcnjRXzmLl2NRh2ep9BkA-RcudnPfUCzsgAK6t5YfiZv_gaMYZahwoyTOH8CaNGgkLQv65WEbtJwfBHjwx1Lt8IFAiB1GLdZTg0M9c5NiBx4z1qflj0jCm6yEbh2nfm03npu_Z_5jKJbHFUb4jEHvf8qbs_VsPdtbW4CrODp61j2oEeZUPlWLw4S1tLzUg7wjsFSaOuxu-xOZCpuShXhCtlkLzvF3Q7vXxXuVm5jdJGbdwQl5cayhXBAFPns_13QIFyd5YcmPeW-v2XOXZuml3yH5ciDhPcnIfWZtzDV18pRqp50sU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c5e038ed65.mp4?token=t9kmUA-g6MkeIAotGRKJZnB2liDGn_Dgog63fp8D29Lpw7Ss9lVnK1qcZzAfvBD1V9OC-nsihW_8vq2Yg0-JPx0Fbm8dQMipVlrFuFNGbXqVHx7X9NGWEMM92vc9aDLm2zN0TnCXAJp_ius9iEg7R9Y_xO1toTbj5j-E4GjGMKQiKArfcBYDCp0cmDwLJyzGlzcV3o0u58aIikLJQeQcGBtQpXw5Ogu3NxEMZTB-w-Jn6htXIAwTQDXm7Ipu7sEuGTIJo90UwZNDoEY8rHkfNlpGELDedstWwBfXvtYLXn1ez6DzGY0CmpQ1RXN-AWbCSVBD1bbzpGOixI53Y7M_8Y6TH4DM9rGXvkSnMsOJPqmg7qG0Y6liqDOKcNcnjRXzmLl2NRh2ep9BkA-RcudnPfUCzsgAK6t5YfiZv_gaMYZahwoyTOH8CaNGgkLQv65WEbtJwfBHjwx1Lt8IFAiB1GLdZTg0M9c5NiBx4z1qflj0jCm6yEbh2nfm03npu_Z_5jKJbHFUb4jEHvf8qbs_VsPdtbW4CrODp61j2oEeZUPlWLw4S1tLzUg7wjsFSaOuxu-xOZCpuShXhCtlkLzvF3Q7vXxXuVm5jdJGbdwQl5cayhXBAFPns_13QIFyd5YcmPeW-v2XOXZuml3yH5ciDhPcnIfWZtzDV18pRqp50sU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ماجرای تکان دهنده ربوده شدن السا فیروز‌آذر
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.3K · <a href="https://t.me/akhbarefori/682776" target="_blank">📅 13:23 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682774">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s2JEFvCiuzbjHU9MNn5ZvT_ZCBqbtyu1l2WKMzRE5RzOHgOhJiVilorHPkfWc6T9OwSG__mU17dfGYHSYdA54WIg4jcePzynYc1aLr9HztSqEBtFMiBBAQoZ9PgsEz6WaMWTtnPOPCne2qNbGZ1bJHnsrvUQEa6zgWhq588uPROPQ7Udk42mPm6RuAs4sbo3nHYSpbAU6qGPfZGRv-Ys_WSMwz4I0DUePHXKlrUHS6kwM1aWWLj1tUK8SjE8OzYu4kWFbhu48YIBdkZeWBg4EQCwPtRfyOH4BcakH_77DhHH1Jwb_WR6KUk47K-r3pzE-2390O4CFuxxlDRt_yDx_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ترامپ شیاد مدعی آغاز جنگ اقتصادی علیه ایران شد  رئیس جمهور جنایتکار آمریکا:
🔹
هیچ‌کس به اندازه من فرصت بزرگ‌تری برای دستیابی به یک توافق در اختیار جمهوری اسلامی ایران نگذاشته است.
🔹
متأسفانه برای خودشان، نتوانستند از این فرصت استفاده کنند. بنابراین امروز…</div>
<div class="tg-footer">👁️ 38.6K · <a href="https://t.me/akhbarefori/682774" target="_blank">📅 13:13 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682772">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0ef0460a09.mp4?token=Zw82hAvY0pFtDFxywAVlT5ZMrRm0WuQnnl9Mg9P5I92OvPVGN57OTsVan_lAlpi2J44CgBXo3BSOKtF2R2FyKn7hZqOylZMddAb5zbRpt_vyXd1ycvlWsFMro_cqNANteqrgkCk6A4BGf_cAElahwpzzXBnE5n7_rfC5qiyXQgOcPszOnMAYKwiOlcE1FLt3U0ACx5Tta3aWPBB_7L3TtDNWl9GiBoTl5rx-lZjA-_cJlTN85yqiqwL0g71mFy7_i3TMxyxHhRF5k1ZqYD6EXavjj8J12AL1qmC76I2yjME4qrSQnJRoVr5u6cl5yoFy5y1lLQ2h8f3Uq1kSU9jUP2Zd4otOhzwrH7xzOYj0SiLa81CVL5z2l-tIe2vSMdjeaTZcagT1qBCxJ50WPr8OMqipHSvZ2cy_hx3NW1W8GiHu9KvUggnOVg4pe_xn7muogQCg1ehhqs-WKorn4RoIpdw7dBsrB_tHgRxQho6Aozkepcq53m6ZVOWMuVOfNDtfE5Yw8-1yNn0uHiChzOUFeSe1UTRb2QwcuKuKtkVltATXC37OoQjkbnP1lEraiTF4_i58kn6kBL2Yx_XWT60Q_J5Y_24FbOqjTR33QA1g0DnrdoPAXhpjFgd_zHBXjlvrX2S227566ef2UnbmAMikYrpJt8s6xW88f6c5VxQtjgc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0ef0460a09.mp4?token=Zw82hAvY0pFtDFxywAVlT5ZMrRm0WuQnnl9Mg9P5I92OvPVGN57OTsVan_lAlpi2J44CgBXo3BSOKtF2R2FyKn7hZqOylZMddAb5zbRpt_vyXd1ycvlWsFMro_cqNANteqrgkCk6A4BGf_cAElahwpzzXBnE5n7_rfC5qiyXQgOcPszOnMAYKwiOlcE1FLt3U0ACx5Tta3aWPBB_7L3TtDNWl9GiBoTl5rx-lZjA-_cJlTN85yqiqwL0g71mFy7_i3TMxyxHhRF5k1ZqYD6EXavjj8J12AL1qmC76I2yjME4qrSQnJRoVr5u6cl5yoFy5y1lLQ2h8f3Uq1kSU9jUP2Zd4otOhzwrH7xzOYj0SiLa81CVL5z2l-tIe2vSMdjeaTZcagT1qBCxJ50WPr8OMqipHSvZ2cy_hx3NW1W8GiHu9KvUggnOVg4pe_xn7muogQCg1ehhqs-WKorn4RoIpdw7dBsrB_tHgRxQho6Aozkepcq53m6ZVOWMuVOfNDtfE5Yw8-1yNn0uHiChzOUFeSe1UTRb2QwcuKuKtkVltATXC37OoQjkbnP1lEraiTF4_i58kn6kBL2Yx_XWT60Q_J5Y_24FbOqjTR33QA1g0DnrdoPAXhpjFgd_zHBXjlvrX2S227566ef2UnbmAMikYrpJt8s6xW88f6c5VxQtjgc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
داستان کنکور محمد بحرانی
🔹
محمد بحرانی از آن چهره‌هایی است که حضور و صدایش برای بسیاری از مخاطبان به‌تنهایی لذت‌بخش است؛ حتی فارغ از کیفیت نهایی کاری که ارائه می‌دهد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41.5K · <a href="https://t.me/akhbarefori/682772" target="_blank">📅 13:01 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682771">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aX6W_cIen2eUMYppAjE43TKqwytQh0XCT1rEhV3wmy6yEPEGMtT3cwwdb46sqrYhBEDim521hBaULtfP-wNXnpWyKx5LMyhtr93snNeDeclQijcR5QSCtwnSbtQoaSQmgrAa-dBBekboOoYpNdkNJv1q8gX063wflEpkKudtfm6rx1JESGVPyYNPdvm7uPw2x-k0SoI8Ek39tCnZifm3BRCKODubynJcTBycqM17tNTtNvdSghZCRHZ5ldBWvd-LJbeXQtIcBzyOx3ajjJ44UGIQZsvtNe674N1akSkfvOBiO3-ayW9tYQldXsK3dmuZDPYlHT2AbsXo0gExVhRkTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
دفینه در صدر صندوق‌های طلای بازار
🔰
صندوق طلای دفینه با ثبت بازدهی ۴.۴۲ درصدی ارزش خالص دارایی‌ها (NAV) در یک ماه، در صدر صندوق‌های طلای بازار قرار گرفت؛
عملکردی که با توجه به سابقه کوتاه فعالیت این صندوق، توجه‌ها را به روند عملکرد آن جلب کرده است.
📎
مشاهده خبر
🔘
روابط عمومی هلدینگ مالی و سرمایه‌گذاری سینا
🔘
🌐
سایت
📲
بله
📲
ایتا
📲
تلگرام</div>
<div class="tg-footer">👁️ 38.5K · <a href="https://t.me/akhbarefori/682771" target="_blank">📅 13:00 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682770">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ccDN0Cu8XxqmcD6nF6NU_gnsofzm_LZk6OifgrKhaSI0GCr-FYhjb3vXC526M3DKScjCekvt1XbjZw-ObQc3RM5eHw6hppuzI9P_DxCyQfsUlTZxrI_PWMg2SIgJU3oCEfCwTwe-SzAicROKJjwzv_8JDnkYY4zXpj24o1bI2lqdVB3rxWnCnCGEhJtgOv3A-ntkqNJA6klHqdoJSDCFAcDTtMw2hfarUaFszBxmtRb06dohCEqdXEpH_i2M00yqrs7oT_EHwaA7BXE636_t6lTb0oLSHa70rBQPvoqMr9impFosMzq-xXHUotKetbIpBC0RWOI-XzZ1w3mwxtChbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
طلا در یک قدمی ۲۰ میلیون تومان
🔹
به‌روزرسانی قیمت طلا و سکه.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.6K · <a href="https://t.me/akhbarefori/682770" target="_blank">📅 12:56 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682769">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UYoiyuFNAakDpw8WZ3hIZI9Z4xaqXbXhhjiZxxGU63DNjzNpIzQggqEaMbX7NsuOuU6gJOB3x_BTWDUk67l9HPX7tnWYKJ7yzSCmd0Jfmt_5loWeVXhkeT_zUkZ5ulC-xUibDHuCiUQQ20W9NYtMBSMgerYVBnvsGbQh-2g9aAoHSAkZuqw9EQVzXARhvyNWH2P8ymS5BQ2c14qj9zLHMEOJRwHVL8CF_gOwnURkwiwsSVpZzb6OZU3Geb9y5w0-IeE7adbw7v9pma0yYng8ggbZxk-yn-ToO82xrT1pYT2hqY_bhhu6WZQY9Cfp4NHTDGJ91aKIyK2UBFASEid1cg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سیدبندی لیگ قهرمانان اروپا ۲۰۲۶/۲۰۲۷ مشخص شد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.2K · <a href="https://t.me/akhbarefori/682769" target="_blank">📅 12:47 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682767">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec88211ffc.mp4?token=tAnzOhjk5jACAx9mKRPI4Vm7ZWw2_4tHR7jrRT7p7OVtFKMGWgjoXLKHeRdL1zonAvr8U-WYGGnrnWheihUZTXSyirQFq2S6IaFL7UvN-15EdPXzOOkkKmctgmo7y3VqeCNRYaeMWjXcqPbLTROPjUK5CaRE2K0UBbvFbygFb_fGvxddfB3hhW11A6vokxZHEZpqy4N4Hmy3qb7bVVcjyZnsLlKB87ZbHr_zgFkVXVqX9c-tk6v89Jqeenn2uSknQoJ_txsNBecTpJ0SLXQvC6VtBNqQqOqF4QRyLTMnkeYuJWr_yX_aQpmK_Ub-QXGB8SfweLRLgtJUAhFVCXVz8A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec88211ffc.mp4?token=tAnzOhjk5jACAx9mKRPI4Vm7ZWw2_4tHR7jrRT7p7OVtFKMGWgjoXLKHeRdL1zonAvr8U-WYGGnrnWheihUZTXSyirQFq2S6IaFL7UvN-15EdPXzOOkkKmctgmo7y3VqeCNRYaeMWjXcqPbLTROPjUK5CaRE2K0UBbvFbygFb_fGvxddfB3hhW11A6vokxZHEZpqy4N4Hmy3qb7bVVcjyZnsLlKB87ZbHr_zgFkVXVqX9c-tk6v89Jqeenn2uSknQoJ_txsNBecTpJ0SLXQvC6VtBNqQqOqF4QRyLTMnkeYuJWr_yX_aQpmK_Ub-QXGB8SfweLRLgtJUAhFVCXVz8A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
موش‌کور؛ نابینایی با یک «رادار لمسی»
🐭
🔹
موش‌کور تقریباً نابیناست، اما گیرنده‌های حسی بسیار حساس روی صورتش به آن کمک می‌کنند محیط و طعمه‌ها را شناسایی کند؛ این حیوان هنگام قرار گرفتن روی زمین نیز به‌سرعت خود را زیر خاک پنهان می‌کند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.5K · <a href="https://t.me/akhbarefori/682767" target="_blank">📅 12:40 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682765">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FJoa2J2W7fPbAjlbWClF32YbgxuzjQxYSFjAdJQovZxPKUDiV5jg2dLcywdrwYUyUg-yxLfsOmGaq6cDhqI5Ma3qVJdk9zsK0qdH9h5mhBciVrmHwf4kBiv4o_4sOq2p8TZFji639-Hat5BYmdiDWF1iGRpUMoiLH3ohkBEcFbVymPexTxqOjyGBw5Y0UY43TSlRi5FYNx7_ug4ZPyxF9_W7M-Q-gPY8dN_E1KYZqM8CApb0Z36AjwDct9Eowiitj255RU4l-_W8AJjbigX3Eoiybq9rLcsVpphNYrA63nZYci7N65iq-kHAepdBixhHn_NnNOfUNpYjPFx8Y278xg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ترامپ شیاد مدعی آغاز جنگ اقتصادی علیه ایران شد  رئیس جمهور جنایتکار آمریکا:
🔹
هیچ‌کس به اندازه من فرصت بزرگ‌تری برای دستیابی به یک توافق در اختیار جمهوری اسلامی ایران نگذاشته است.
🔹
متأسفانه برای خودشان، نتوانستند از این فرصت استفاده کنند. بنابراین امروز…</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/akhbarefori/682765" target="_blank">📅 12:11 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682764">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9e2f7760b8.mp4?token=blGbn9C-GxmGVFeu5HwaDLpehi1ezg2jlBsr_RBnvQPxgaEiztAEYjRa1sy_PJZoJTgvDwGDRJJrxHvSxoI-PcyxvoyeOfhSIpEXwzKvJYGzVkDlgP9aXp56nzMoA8QN-NO1zT_580ueXzKqCTG61o97IVOtOEki5jeaX2wkUnJeNFYmsf5xfpCrfXQi9kGiK-9dGaLPPslIN4BKp-OoRCQPgjfVZO_lc1JFs9IrfKyFF0niiuBF-DGLyxuiblXIV1QWoG9XPhyJwg6O7NxeFzm6jhDyQbOuMgUH_v9pmmaUnJGjF5yrnqyQwImBVBBLpYP0DS0rVme8XcGHNY7iyQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9e2f7760b8.mp4?token=blGbn9C-GxmGVFeu5HwaDLpehi1ezg2jlBsr_RBnvQPxgaEiztAEYjRa1sy_PJZoJTgvDwGDRJJrxHvSxoI-PcyxvoyeOfhSIpEXwzKvJYGzVkDlgP9aXp56nzMoA8QN-NO1zT_580ueXzKqCTG61o97IVOtOEki5jeaX2wkUnJeNFYmsf5xfpCrfXQi9kGiK-9dGaLPPslIN4BKp-OoRCQPgjfVZO_lc1JFs9IrfKyFF0niiuBF-DGLyxuiblXIV1QWoG9XPhyJwg6O7NxeFzm6jhDyQbOuMgUH_v9pmmaUnJGjF5yrnqyQwImBVBBLpYP0DS0rVme8XcGHNY7iyQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
از زبان ‌علم بشنوید چرا بین خانم‌ها و اقایان این‌قدر تفاوت رفتاری وجود داره؟ #سلامت_روان
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 40.2K · <a href="https://t.me/akhbarefori/682764" target="_blank">📅 12:07 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682763">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m3XEaFqI4fhAECdMlUeeiWjozo-sOAfzo-1Q8Tj_DLhk2gT0en6eLYrRQqpqDzMx6wK8YOAz0GWzG3QIZw309RVTBFMqJEw7L_momW0cY-PlKeJDwAHBur2lI71VFVG_Y_MGDPQgKqX9tu7yiVVtiua9MasJ02hyPV5uS_5YXz1j5nqdkdBXi_0qZm41oB7Abt7ITOa8UX3ds0fanmhTAaq3aNh7BHjmqWyhA-GZCzEVQ0wRRcQybKNgVxCNsQUWWtR_m7QqWOQecTiWdL89Ui2CNSFmtWdLwv0P7kHUCqS86uQzgiBOnCzSUB4ASVorhFI7TajiupabLzGILczczw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
۴۰ لغت کاربردی که اگر بلد باشی سطح زبانت B1 هست
✨
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.7K · <a href="https://t.me/akhbarefori/682763" target="_blank">📅 12:02 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682762">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d2XeStgCsV0Wd14EgHqcP5CvmVwtuR6Po12FvBR3TnZ_a6fEn8hcGcyIX9LrO1WD4UBK1Kpt40ZzsS489tkXpGjXkRjFqODUZ2Qkpy8rBVCEFv20wrO_21vF9FUmdwDY7TK0SOLn8QhZ4_8jzdQ9Kl4V5qxAC6jbzmvLoOjzyjVPIyUHb0mJf4jDYeBdDI6crJLL5bQPDX-H5fdOnLuu4vQHoZf6CjgJ_fpXscuVNHcCnRspNj6lc25ArUylz1gC2iaot5epamSFaPEif8Wu3m3s27JHuXzGuBFoc9CJMq3b1f-UiPRnJjX_GLz00K8Ezi0dYH64vr8Q2WhMq1kenA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💥
تا 70% تخفیف در جشنواره mono!
👠
صندل، کفش، کیف، البسه، اکسسوری زنانه و مردانه
‼️
امکان استفاده از تخفیف بیشتر فقط در ۳ روز پایانی مرداد ماه:
💰
1000000 تومان تخفیف بیشتر با اسنپ پی در خرید آنلاین: PAYCVCCK
💰
500000 تومان تخفیف بیشتر با دیجی پی در خرید حضوری: DEAKJM
💳
پرداخت اقساطی با اسنپ پی در خرید آنلاین
💳
پرداخت اقساطی با اسنپ پی، دیجی پی و زرین پلاس در خرید حضوری(مشهد، اصفهان، شیراز، اردبیل، بابل، بابلسر، کلارآباد، زاهدان)
‌
🆔
@monofashion_co
🌐
www.mono-fashion.com</div>
<div class="tg-footer">👁️ 39.6K · <a href="https://t.me/akhbarefori/682762" target="_blank">📅 12:00 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682761">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cf1830b1bd.mp4?token=d9pX6wRe_FLsyS1uBeAqMfiLExiVUV7spSWFi-EurnL_4iz_Cfz2TpZ2b7zZy8jAwo9PxHc7TSu01FIyBcDmaOlGfM25SIBgqgU1LNUvWtq0Ph8r67_YRU_hq_p07Pt2sFwjhc-GO6KnIshopU5CTZTdTtQ_ty6QFohJkXT91uW0lv_xcTS1ml2kaM5wNp5UJd92bE-IO5KMK92jiK2l44YvZRTEJwvn9HUZqOXMIPxYfwf074P3c1Q_UV8UkFwENnQS-eCr4HP_K6SHISdIoiOdOZ2loEbKln5P5L1p2dKDfyKYNSb5ZvtD0SDYPjSZfJF4qO0m9YYQHle9kUNCWA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cf1830b1bd.mp4?token=d9pX6wRe_FLsyS1uBeAqMfiLExiVUV7spSWFi-EurnL_4iz_Cfz2TpZ2b7zZy8jAwo9PxHc7TSu01FIyBcDmaOlGfM25SIBgqgU1LNUvWtq0Ph8r67_YRU_hq_p07Pt2sFwjhc-GO6KnIshopU5CTZTdTtQ_ty6QFohJkXT91uW0lv_xcTS1ml2kaM5wNp5UJd92bE-IO5KMK92jiK2l44YvZRTEJwvn9HUZqOXMIPxYfwf074P3c1Q_UV8UkFwENnQS-eCr4HP_K6SHISdIoiOdOZ2loEbKln5P5L1p2dKDfyKYNSb5ZvtD0SDYPjSZfJF4qO0m9YYQHle9kUNCWA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حسین پاک، کارشناس حوزهٔ مقاومت: اهمیت اصلی علی‌الطاهر لبنان، علاوه‌بر موقعیت جغرافیایی، به تأسیسات استراتژیک آن برمی‌گردد/ در میدان نظامی درگیری‌ها لحظه‌ای ادامه دارد و حزب‌الله همچنان با تمام توان درحال مقابله با دشمن صهیونیستی است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.1K · <a href="https://t.me/akhbarefori/682761" target="_blank">📅 11:58 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682760">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bf4e744901.mp4?token=JH1fOn4fZdcZxBn_6yGWFHiXA4wJpjsQeKnE3NtY_AhJ9589LLFab0NGDlg8W5G-fopgAqelGC_BaYprNsoAbuchPKypwPkKba9c6xVDDNd3OWuNez1OC51Z680BjPEbVokVE3IY12BnqB-UR8uFYTaAkBA8VhoHSiluRi0JZs71Pq50LCa3_539eCSzI5O3_z_dqqgecF_UpVDJ5esyQHuogFPy4hPw9P3WPqreViKoGVo1QQv5c34vhTl0OAwlsdQir39oqmiqQPE9IpxbyDPUHEq42g4229YoKb6ExbWl-xjxww3-TJwDmB11QprlhuEH-wjkaFFvtSPT22EFxxPdP3T0azfpSIVpB4p16JpL7z3F-0iVgmcsinjZIRUXl11Ek7UVPG2IB03vBiHdwPHd7JSXzYI2g0jwEa-xMeeg-9QoS1RR1S7DEZ8j0UTRf3-r86KI88TDUBHBgBQlKLfIxAeNXF1j8i1EPKLcBic0duGHcIOLwn69nBa1B3qtjfKkhfK_uAzyt5pgufzvKnyf8xJ9h_gvfHPzny4Ux2ATTH2ZS0_el6tBt262TfPWyaLhy7vqYKziSyJyuILrr_EFSQ2q_s53ruWpU9DcG3JS3-AM8n8gqgXTucI9Up7-RhPmCc1fjawIwk5acpdGY7MsTVu45uJVg7ImvIl2X7E" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bf4e744901.mp4?token=JH1fOn4fZdcZxBn_6yGWFHiXA4wJpjsQeKnE3NtY_AhJ9589LLFab0NGDlg8W5G-fopgAqelGC_BaYprNsoAbuchPKypwPkKba9c6xVDDNd3OWuNez1OC51Z680BjPEbVokVE3IY12BnqB-UR8uFYTaAkBA8VhoHSiluRi0JZs71Pq50LCa3_539eCSzI5O3_z_dqqgecF_UpVDJ5esyQHuogFPy4hPw9P3WPqreViKoGVo1QQv5c34vhTl0OAwlsdQir39oqmiqQPE9IpxbyDPUHEq42g4229YoKb6ExbWl-xjxww3-TJwDmB11QprlhuEH-wjkaFFvtSPT22EFxxPdP3T0azfpSIVpB4p16JpL7z3F-0iVgmcsinjZIRUXl11Ek7UVPG2IB03vBiHdwPHd7JSXzYI2g0jwEa-xMeeg-9QoS1RR1S7DEZ8j0UTRf3-r86KI88TDUBHBgBQlKLfIxAeNXF1j8i1EPKLcBic0duGHcIOLwn69nBa1B3qtjfKkhfK_uAzyt5pgufzvKnyf8xJ9h_gvfHPzny4Ux2ATTH2ZS0_el6tBt262TfPWyaLhy7vqYKziSyJyuILrr_EFSQ2q_s53ruWpU9DcG3JS3-AM8n8gqgXTucI9Up7-RhPmCc1fjawIwk5acpdGY7MsTVu45uJVg7ImvIl2X7E" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
چین در سال ۱۹۱۷
🔹
فیلمی تاریخی از چین که در سال ۱۹۱۷ میلادی ضبط شده و تصویری از این کشور در بیش از یک قرن پیش ارائه می‌دهد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/akhbarefori/682760" target="_blank">📅 11:54 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682758">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">♦️
ادعای «الحدث» به نقل از منابع آگاه: ترامپ دستور داده است مذاکرات با ایران برای چند هفته متوقف شود و احتمال تمدید این توقف نیز وجود دارد/ انتخاب
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/akhbarefori/682758" target="_blank">📅 11:37 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682756">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fe6b7f22ee.mp4?token=NzgyUQ0nx0hppyltYoDPwBOAvW5Xiw0eDjOcllMAgVG5hz5mHCCRjsQWr6nfhlSVglDNNT2uXmg2LO1_Bv7Z2OY1rtjV7GhaBQWC--Ahx6vy9exPp2S9dvqnP5BKKMemc090KshTj-RJO2eKV0CFFAmWWG_ZfvHNUYTjtGTbW1GX2pqD0M_UKKkkDbmjJ3ScTnTwR45sWKqyMLu4GAnS2Z1KZMgtNlZEDVAY5pkVBaftniQVTnM1HKLcP2ZhRD4K7KwOHl5eoIE46IpWIRuw75gHTT1EyMNEDApbTG2tnGNAQ3U3fRrRTzQs_OfcxxNOccg-_l1uDywKTub88jQEnA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fe6b7f22ee.mp4?token=NzgyUQ0nx0hppyltYoDPwBOAvW5Xiw0eDjOcllMAgVG5hz5mHCCRjsQWr6nfhlSVglDNNT2uXmg2LO1_Bv7Z2OY1rtjV7GhaBQWC--Ahx6vy9exPp2S9dvqnP5BKKMemc090KshTj-RJO2eKV0CFFAmWWG_ZfvHNUYTjtGTbW1GX2pqD0M_UKKkkDbmjJ3ScTnTwR45sWKqyMLu4GAnS2Z1KZMgtNlZEDVAY5pkVBaftniQVTnM1HKLcP2ZhRD4K7KwOHl5eoIE46IpWIRuw75gHTT1EyMNEDApbTG2tnGNAQ3U3fRrRTzQs_OfcxxNOccg-_l1uDywKTub88jQEnA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
هر شیشه عسل، حاصل میلیون‌ها گل
🐝
🌸
🔹
هر زنبور در طول عمرش حدود یک قاشق غذاخوری عسل تولید می‌کند؛ برای تهیه یک شیشه ۲۸۰ گرمی، حدود ۶۸۳ زنبور روی بیش از ۱.۱ میلیون گل می‌نشینند و مجموعاً حدود ۵۲ هزار کیلومتر پرواز می‌کنند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/akhbarefori/682756" target="_blank">📅 11:31 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682755">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/597578ac3e.mp4?token=FTqG4-VOLxihAaXXyDqlMUuesecVKLPOwjZWspXCw71JaYhbI1v8SLP_4uf_XNBOxSfmi4-pGzlSK92alr8IDNyZORrgSG6_KPJJcpC0UVG-JJyzYORAmG_8G1mM8bqCbuGwub3myNYKMDZeg6PGmln8dcfdDBXOaLndx1QMbb7UJLMpiiZQey_iE05PiMbQBOkDs19Zy6skdp_aZN8D8XGuOCD_YCdTU1k-x-XK7gGRAOJPVIyLW5xC86N5xtip9MwYqedjzJxRtMe07QQYsYWxNd8yEgiGAMHDSfZlF-DDCDY8PNSm2vGBsFim9LTx15IE2IXFiUHF6KNH3Gdamw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/597578ac3e.mp4?token=FTqG4-VOLxihAaXXyDqlMUuesecVKLPOwjZWspXCw71JaYhbI1v8SLP_4uf_XNBOxSfmi4-pGzlSK92alr8IDNyZORrgSG6_KPJJcpC0UVG-JJyzYORAmG_8G1mM8bqCbuGwub3myNYKMDZeg6PGmln8dcfdDBXOaLndx1QMbb7UJLMpiiZQey_iE05PiMbQBOkDs19Zy6skdp_aZN8D8XGuOCD_YCdTU1k-x-XK7gGRAOJPVIyLW5xC86N5xtip9MwYqedjzJxRtMe07QQYsYWxNd8yEgiGAMHDSfZlF-DDCDY8PNSm2vGBsFim9LTx15IE2IXFiUHF6KNH3Gdamw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
دود غلیظ جنوب تهران ناشی از آتش‌سوزی ۲ تانکر بود
روابط عمومی پالایشگاه تهران:
🔹
حادثه برای دو تانکر هنگام بارگیری نفت سفید رخ داده و آتش‌سوزی در کوتاه‌ترین زمان مهار شده است؛ این حادثه یک مصدوم سطحی داشت و تلفات جانی نداشت.
#اخبار_تهران
در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/akhbarefori/682755" target="_blank">📅 11:26 · 29 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
