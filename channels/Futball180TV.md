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
<img src="https://cdn5.telesco.pe/file/HqdC4bgWskGZJxx_xBP6jCuMbb4C5j_9yeTXCiyxqR9SQWXoPx3EyNJHXDGnXu7GmMT6Ew-Aj5ETYAqMyNxQZFWvqtK4nh7MKf0HZ3VveAgHQEPw8qH7ZTKWcUt8gwDxDrDzMYbJsdGFpfYfLu8ikOkN6W0je_4h94uvPHUndzLtg5FPxMYbPl5emUIZ7JV2GJbjILoOONsdSMzzdIDRDEr7oWr7-DhFqBf7twvb9DxvyvSu-bnOWHdxqZ_7TeeVOCKvcyALsiqYfmclFTSLFqizvY8lbUp4ebA85y64LGdK_cctn0T61R35CsO34BehtmHCe6x_KzZC6fb9atTTLQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فوتبال 180</h1>
<p>@Futball180TV • 👥 409K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-27 16:01:22</div>
<hr>

<div class="tg-post" id="msg-106809">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/171fd833db.mp4?token=WNSHRWE2kVwW3wUiEoL359junnK2wEQxNeXwgEU37IpyrtED2A83oyvQMe85UcZaRXHuRuwoIA7R1o3FmMOC6B3KTC9WTH5w9xMcO4fkGJjo_Q_vbrSKjuku5LiB9IOXNCVESl3eUNI2Slj_WZS-fMh33ABDi5xemO-elSMIqcJuWkYckcokFgNnPm5wbrI25ae6sMC1C1ngFvGrK9ygw0PU7-N6djXhI5HdH7OqC_uPDYOCAPeP7bpo3w3o2e0RSG665w0gTDbt7d6YtNQ34e565z7_2UzMJIY0Qj8VnNTZwjoI-AT8c_o5ONcyDfAsWb_EYtRuKl4OvchnEmjg8g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/171fd833db.mp4?token=WNSHRWE2kVwW3wUiEoL359junnK2wEQxNeXwgEU37IpyrtED2A83oyvQMe85UcZaRXHuRuwoIA7R1o3FmMOC6B3KTC9WTH5w9xMcO4fkGJjo_Q_vbrSKjuku5LiB9IOXNCVESl3eUNI2Slj_WZS-fMh33ABDi5xemO-elSMIqcJuWkYckcokFgNnPm5wbrI25ae6sMC1C1ngFvGrK9ygw0PU7-N6djXhI5HdH7OqC_uPDYOCAPeP7bpo3w3o2e0RSG665w0gTDbt7d6YtNQ34e565z7_2UzMJIY0Qj8VnNTZwjoI-AT8c_o5ONcyDfAsWb_EYtRuKl4OvchnEmjg8g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مسی نشون داد پَرش و ضربه سر هم خوب بلده.
😮
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 2.52K · <a href="https://t.me/Futball180TV/106809" target="_blank">📅 15:40 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106808">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eeb5c6a4f7.mp4?token=sYszOFH3iMQ1ErdtbVzJNZ1Rq-3xZcd7PenmBqRPD_X_eQBi31nNiS97snW2cZzH911LITtmgLrk6G-QuPegh9eXAkiSRrcf7lrULklP9m2b3ONgx-DArg1bRIdpvHyPZambWh3JewPF87CddpZ87mz97iffZ2pXNLmOahGjEXRDLXf96gd-swhm26BQbBXT8YhSBvvkAZm_iubJhtNihM9ifdx6Ozjthc-9n9-TpkvLNM0SH7roTYRvDypUJSrJtiYQxKHiAhJv0lYViY-W4QKzm_o_QLQbGJyZhwN5hJ3K_o-WTTOospl4CFkbToY8TGzzUH5aBuDBBIiOPamm4g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eeb5c6a4f7.mp4?token=sYszOFH3iMQ1ErdtbVzJNZ1Rq-3xZcd7PenmBqRPD_X_eQBi31nNiS97snW2cZzH911LITtmgLrk6G-QuPegh9eXAkiSRrcf7lrULklP9m2b3ONgx-DArg1bRIdpvHyPZambWh3JewPF87CddpZ87mz97iffZ2pXNLmOahGjEXRDLXf96gd-swhm26BQbBXT8YhSBvvkAZm_iubJhtNihM9ifdx6Ozjthc-9n9-TpkvLNM0SH7roTYRvDypUJSrJtiYQxKHiAhJv0lYViY-W4QKzm_o_QLQbGJyZhwN5hJ3K_o-WTTOospl4CFkbToY8TGzzUH5aBuDBBIiOPamm4g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🇮🇷
اعتراض تند رسول خطیبی به حمید مطهری و تیمش بعد از باخت لحظه‌آخری فجرسپاسی به فولاد در اهواز
‌
‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.11K · <a href="https://t.me/Futball180TV/106808" target="_blank">📅 15:15 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106807">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N98BjJOfPpix7Gm-5fdFCfiariPegrqnfknBwfFRbeYtJKogsFUpjk-AmOrI_fdSICvaswk6RekAkNnea1gsTDC7sDKTuVjym2Fd7oSs-8aZl14_Q8zKDcXjijN6DWbXKkbre5loGlIstOFZhs96TKMuCsBSwtslvMEfCPr-uvzJzEK3IBAJPKqAolUlTT2_96NMTMZBFX84BBFpj0E5_M-YUgYGGm5nzF72zQNrd89_JfXePo151iVoKq-7Lr0Z3tWUD7tMKjNrmerITVxJ-Hw14YjvqkhDrVNUjCtqEv86q0BCNLF_7JK4Zd-R7MYIcbUAine9jbazG6kmA3gUtw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🌐
گزارش هیئت مستقل حقیقت‌یاب سازمان ملل درباره مدرسه میناب: مدرسه یک مکان غیرنظامی بوده و در عین حال این مدرسه در مجاورت یک مجموعه دریایی وابسته به سپاه پاسداران قرار داشت. اطلاعات مربوط به مدرسه در سامانه‌های هدف‌گیری و بانک اهداف آمریکا آپدیت نشده بود. هیئت این حمله را یک حمله کور/تفکیک‌ناپذیر اعلام کرده که موجب مرگ غیرنظامیان شده. بر همین اساس، هیئت آن را جنایت جنگی تحت حقوق بین‌الملل ارزیابی کرده.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.52K · <a href="https://t.me/Futball180TV/106807" target="_blank">📅 15:11 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106806">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a40dc07061.mp4?token=gF4WgVfkvjl6kASi964BUVmWaz469WX8SOITeXWFkt5zbsbvRJJydn8BamlpetOCDfqLG-EErXBggCbuV6ek3Jfa8eG6lGFfwQLNE4ADw7zED8FJ5wfHRg9mIFcIuslsBvPzo6Uwv_FoDmrm-Z8dMDCLMSEUoOJpUsKciJL34x23Rep9237kD1tEOzxaitsgBY5PxksANpu5bgtci6PSwomHVMWjp3Cfw9YPYHhQssmQqHwpLN6RakJKQCVK1UcXHYdAX-H4BnUMy0kZHasHyBjWtg1RA8cl2-CwDvbNApGutEBxeiG6U3S_VUxaAb6QWBfj4b7W8XcSi5NhdjZp-Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a40dc07061.mp4?token=gF4WgVfkvjl6kASi964BUVmWaz469WX8SOITeXWFkt5zbsbvRJJydn8BamlpetOCDfqLG-EErXBggCbuV6ek3Jfa8eG6lGFfwQLNE4ADw7zED8FJ5wfHRg9mIFcIuslsBvPzo6Uwv_FoDmrm-Z8dMDCLMSEUoOJpUsKciJL34x23Rep9237kD1tEOzxaitsgBY5PxksANpu5bgtci6PSwomHVMWjp3Cfw9YPYHhQssmQqHwpLN6RakJKQCVK1UcXHYdAX-H4BnUMy0kZHasHyBjWtg1RA8cl2-CwDvbNApGutEBxeiG6U3S_VUxaAb6QWBfj4b7W8XcSi5NhdjZp-Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
✔️
▶️
مهمترین اشتباه در محبوب ترین حرکت بالاسینه؛ به توصیه استاد هانی‌رامبد عزیز
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.77K · <a href="https://t.me/Futball180TV/106806" target="_blank">📅 14:50 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106805">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RIe1NQNRWMXm6vHDQgm3PF3jbltSCttLTP0odcoPK0uQCy0reKjEcBVaPZNOGo_uuTkDLNVbH616THsBwg-FZzjTsSYAIzqeLFac6myAWBLPUYl4XBaSharC1I_E0jI84jOmllku7A5ySfoKT5LNNzqUhF5Ig759618I13oPcGPNNqTusKuk4y9ihLCQt4BkNPQ8-l4r7LzQ3mbmyJ1wxE_g6C4pZQiRbPvLB9DTMtetF0S3e9z1HjlTO5ZLj-4HIdF2E2js2E3bqUO9eGyFlNoHWWs_5MGfvEJ5TJuyqEYrFYTBMoMkk34-zyYCQVsZtnJXA96P2FCTQ5AAG0YQOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تیبو کورتوا درباره برنامه‌هاش برای آینده:
کار من بعد از خداحافظی از فوتبال؟ شاید کار توی بخش مربیگری دروازه‌بانان رئال مادرید و ساخت یک آکادمی درجه‌یک تا به جای خریدن یه تیبو کورتوای دیگه، خودمون یکیو پرورش بدیم.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.06K · <a href="https://t.me/Futball180TV/106805" target="_blank">📅 14:25 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106804">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sNx3CYJxLMgnXE0fUuW_hHtZaCA6oEgKW0bjKPk8vaDUfG3UF0b49Cn9E7DPa79uKQNsoasRQDYkcdcGS3c_rjssYL3yFU7C1ABEOusTyzsYDf3j4w53Ha9Nahe4A8a2HtcTwchtB3gDlmtBXLTTPkYSSEq7NujOu7a070Kj4DjMRuUncfEQx9s7_iYELfAAvHAjCfLH5cHWy22EvAyg3BnBkfTQwrIhjRss2mVHEZV5GweuGUEGgmDcHu4Al2zFD4RLhkpNy0MXwCHj7mkejn4vFEeQ0uzcOTkKejYe_BwEkmeg8Y9X7XemteTFNyqW-9dgl6VAtbNIFROlNR4WaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
هری کین درباره توپ طلایی:
"من دوست ندارم درباره خودم صحبت کنم... 73 گل، خودشون حرف‌های زیادی برای گفتن دارند."
"این بهترین فصل زندگی من بود، و این تفاوت بزرگی ایجاد می‌کند."
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.93K · <a href="https://t.me/Futball180TV/106804" target="_blank">📅 14:23 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106803">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/325a2dc7b7.mp4?token=WA5igbSCeWCdfVnw-pONZ3qYD46rxRDoWe_blBc2eT9mxGnnwuj4vjd_3WZJCrjdJB3QsMZFgcW35TwHrXkO5M-pmzPhI_FD7EFIel6cRDbBPlPCNW9Lf3UggAcc809QhigI33XFdxiu3deS3eJXyiH1H2_-Y84BFaYNtRhYZF4DpRICE46nPGhXl43EinmpQ_ix42Z5zCnOiYx7_V4khwB_uRCs8UX-ogBQSf8PVF7BKTFJ17B2nwa7SnbGG6W_nLF7kAPHB4fb9p2SibXYlMdC7V1-Cdjnh4HDhfwyHBzJZUkSy5J_rHH7AxWCXTRF7xA6onN2jwLR9YfR7mGligcjy6Cs7TPu1qo0VH6uNeyCtylN7yndV_LiFoF5DyXz8TGKUwntFZN_XJ94yW8j2_Y9MkjtQOjf3fNMO80i0FZXR6lTIRp8kS0THI1jgwQjtkXcqyMhQraHVArTTJ9plitHLtFS6jlogkutYPZLODZ0MLwMOGEUBukjzY-_o1hq8hTd158ic09oHXyTg4n38kTk1Hh1Fh1H2RxdCm8EQsj4E3JYJuM9Cl2NiUeU7LAep9yy2MTAuA9T8jtvA-FW6A2PpqPPTGHuUwdEDj9wWZ5fQLCRsCZ-zvKJmMpDfRvs90zEX0FQGq3-encjmFXQ9BQf_LCieR43PhZhzxzFLTk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/325a2dc7b7.mp4?token=WA5igbSCeWCdfVnw-pONZ3qYD46rxRDoWe_blBc2eT9mxGnnwuj4vjd_3WZJCrjdJB3QsMZFgcW35TwHrXkO5M-pmzPhI_FD7EFIel6cRDbBPlPCNW9Lf3UggAcc809QhigI33XFdxiu3deS3eJXyiH1H2_-Y84BFaYNtRhYZF4DpRICE46nPGhXl43EinmpQ_ix42Z5zCnOiYx7_V4khwB_uRCs8UX-ogBQSf8PVF7BKTFJ17B2nwa7SnbGG6W_nLF7kAPHB4fb9p2SibXYlMdC7V1-Cdjnh4HDhfwyHBzJZUkSy5J_rHH7AxWCXTRF7xA6onN2jwLR9YfR7mGligcjy6Cs7TPu1qo0VH6uNeyCtylN7yndV_LiFoF5DyXz8TGKUwntFZN_XJ94yW8j2_Y9MkjtQOjf3fNMO80i0FZXR6lTIRp8kS0THI1jgwQjtkXcqyMhQraHVArTTJ9plitHLtFS6jlogkutYPZLODZ0MLwMOGEUBukjzY-_o1hq8hTd158ic09oHXyTg4n38kTk1Hh1Fh1H2RxdCm8EQsj4E3JYJuM9Cl2NiUeU7LAep9yy2MTAuA9T8jtvA-FW6A2PpqPPTGHuUwdEDj9wWZ5fQLCRsCZ-zvKJmMpDfRvs90zEX0FQGq3-encjmFXQ9BQf_LCieR43PhZhzxzFLTk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
تأثیر غیرمستقیم تحصیلات بر فوتبال، از زبان بهترین بازیکن جام جهانی ۲۰۲۶ و برنده توپ طلای ۲۰۲۴
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.68K · <a href="https://t.me/Futball180TV/106803" target="_blank">📅 14:00 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106802">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2929cbe0df.mp4?token=KOlPV3kIk3eeEYLcB_ifvGRfIHk_3FjuCMQXg95DNIqdcHxk7iiwSCJIk6CRifYU0TSwZw-eBsp__I_7K40EN_DgOIh3MZ2VpOY0CsgsBmnt6Zy-IFolGTvj1feMkFz-HqWvxg9fbhWFx5rNdec17rRq0DJl39grnugy489XCDTLETuK9Gxx76aFux0rdjW-ZFesZpHo4AhihmSJHsWPiHq8-Mk-aCpQmsFNf3oyAwPxr-7pmyx_b9lppYcIQSnRIOoLkyWcpOAcJ8J1NF9mXPw73GfwNQklq2whtxQFGp8qTHTkK7gJDCz8Gh-K9f1-WOBGypxDhZofnZArfJ8abg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2929cbe0df.mp4?token=KOlPV3kIk3eeEYLcB_ifvGRfIHk_3FjuCMQXg95DNIqdcHxk7iiwSCJIk6CRifYU0TSwZw-eBsp__I_7K40EN_DgOIh3MZ2VpOY0CsgsBmnt6Zy-IFolGTvj1feMkFz-HqWvxg9fbhWFx5rNdec17rRq0DJl39grnugy489XCDTLETuK9Gxx76aFux0rdjW-ZFesZpHo4AhihmSJHsWPiHq8-Mk-aCpQmsFNf3oyAwPxr-7pmyx_b9lppYcIQSnRIOoLkyWcpOAcJ8J1NF9mXPw73GfwNQklq2whtxQFGp8qTHTkK7gJDCz8Gh-K9f1-WOBGypxDhZofnZArfJ8abg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💥
زیباترین گل‌های کاندید پوشکاش سال ۲۰۲۶
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.46K · <a href="https://t.me/Futball180TV/106802" target="_blank">📅 13:35 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106801">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/37652c08b0.mp4?token=sxq_lTxraCDzlfQn8hJRgjx-X4eI083Kwt_UFZcR9-a3DXU163T3y7hQcCUWrIFbYn9bo63J5hh55RQSqvCAhcWzICzSaIvtV2kamx3LZ1b3pbOxeschqkSYP_AeP8zcv70q7klXByqFLUKRcejmwTYBRHydNQr7hVlFodVDshRy3D_Ha_DC9Cdblh-XtPVwD3HfOIBzEa2ny3rFm5F073yvEnOYlMzznkfIrWwBUHoTUzYqgY94vT-r2SLZHipn2P6lGulhORth33gEFWVTeQO0tDl_zgsKflBF0xLmVWnrXmnvw_MbgRyycJX5weFlFE1a-2pNfMUCdUEKEUtjPoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/37652c08b0.mp4?token=sxq_lTxraCDzlfQn8hJRgjx-X4eI083Kwt_UFZcR9-a3DXU163T3y7hQcCUWrIFbYn9bo63J5hh55RQSqvCAhcWzICzSaIvtV2kamx3LZ1b3pbOxeschqkSYP_AeP8zcv70q7klXByqFLUKRcejmwTYBRHydNQr7hVlFodVDshRy3D_Ha_DC9Cdblh-XtPVwD3HfOIBzEa2ny3rFm5F073yvEnOYlMzznkfIrWwBUHoTUzYqgY94vT-r2SLZHipn2P6lGulhORth33gEFWVTeQO0tDl_zgsKflBF0xLmVWnrXmnvw_MbgRyycJX5weFlFE1a-2pNfMUCdUEKEUtjPoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
✔️
توضیحات مجتبی‌پوربخش مجری اسبق تلویزیون درباره افتخارآفرینی کیمیا علیزاده در اروپا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/Futball180TV/106801" target="_blank">📅 13:10 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106800">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N9960QSC-MFI7AI_I05cpYfuTYElxVdNsny640X54SF8IlwbPyYtS7B1OqN_cSdpTRVX3hzQLpA43EpS_q8U2dpRuVByhT6XiygZ9Eg32sWs1MvJjdquXIiW3TzInMSK9aL67JfRqlfdDMfsoFAC3NX4s36XzgCVm811uDl5m04pxRU_euyo2lnd8yazKrQs6vtUaPU9hgOwZxqbDqLjSnSO_UBpgAq5tMuOEv2q_A33rmAyR6Rp2HHgxQW_K6CIX5g2Z4e6FPClvzL0FDr2mvlMQxeIuyFlWVSegrDXtyitsWOIObjTr4uFtL9qAfxHaZ2C4mNzWR-L2gw6vjonog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
✔️
لیست تیم‌ملی انگلیس برای فیفادی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/Futball180TV/106800" target="_blank">📅 13:01 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106799">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">‼️
🎙
صحبت‌های عجیب و‌ دردناک مهدوی‌کیا از دخالت خانواده‌ها در مسیر رشد استعدادها!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/Futball180TV/106799" target="_blank">📅 12:41 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106798">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/Futball180TV/106798" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/Futball180TV/106798" target="_blank">📅 12:40 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106797">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hVxe_er6hiiOI7h8cstlFEFrvML12c2EOsZSoKd-TXPqQWzerHsUEQYihlk5nTza22R36LgSJMM5eUmRkfFv2ZCKMvNgvbw0LNU-1NGVV3elxB-_q8C8sAyerXTPszcb8eivuGKwTCQb5848pjOle_1XXJeAP9EX5aDsAQfdcegnfWQxxKuV-DxJ0FcO13GG0wuSnaLg2d47CSz_U1tByvZtWFy270l6Qw0mVVijmcbqVYUwpsOFdsHMh5S4T_rUlbPFoxC_yutW0h37JKVnzWvihxZheMjJuG_5ap-DEFBMAUvNjxmeCV-UjhmLcerzl7NVOhT2ekpiQxjQuawdNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
مچ‌های مهم امروز در سایت بین‌المللی
TrexBet
چلسی
🆚
برنتفورد
انیون برلین
🆚
بایرن مونیخ
لنس
🆚
موناکو
🦖
🦖
🦖
🦖
🦖
بونوس اولین واریز تا سقف ۱۰۰ یورو
🦖
بهترین ضرایب بین تمام سایت‌ها
🦖
واریز آسان و امن از طریق کارت به کارت
انتخابت رو انجام بده و آماده‌ی هیجان باش!
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/Futball180TV/106797" target="_blank">📅 12:40 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106796">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sjpbjAdZMgVsgIytVD0puujvDqLgDPNOmMWE2uIw-YUVf8bZrTL32-oCuLFqPbGba2abILYLWiAK-fQpi5gRA3gTjDWMaIPkCAcrviCrlMhiok6EJa9JR4Gbv-q609n3uqXSP3EUp2VDNTzHfzUQv1UlikG7sQNYNq2W271nmju0UuvNlyonIooC9TzGDJ4RxxP6i42V26m2IrHYcECuXEDxCLjwbFM8H2g8YjdsvHKHg3WOlJ3PFE12UuzzBXygmZNHosnpLQ2KiRM5UmrRpksO20BQAT4ClB_YdmJFZw0Oy3FXQba4pymYBPj0kc-73OZPZD33WvanlXtCcVVJuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
🇪🇸
رافینیا، با هت‌تریک خود مقابل راسینگ، در 7 بازی اول فصل 2026/27، به 14 گل و پاس گل رسید و رکورد بهترین شروع فصل لیونل مسی در باشگاه بارسلونا را شکست. مسی در 11 بازی مشابه، 11 گل و پاس گل به ثمر رسانده بود (فصل 2012/13).
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/Futball180TV/106796" target="_blank">📅 12:20 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106795">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f364f9a06a.mp4?token=jgg3WnCpqN1Ul7W_1hrtswiz-xb6xaSYF-4robWniChXqL4Fr9ZrmVCOAJUJVMVYSeOdgus7LUZmeFkYJiGR7L1lcLJmQXQpJwzzBixSUgFJuCUa5YG1Fifj2gHtZ5kxqnEkfz0Spjx3MwUe0inD0_NFf2-XhTyO6RXKbAd1VYeOJc_ijj0uB-CGq3-p7Fmr1deBLHU_MkK5bflM4qyb_dLOXXgCBzBOaVBeGDzleklXgoHmw4T9PuqhH9SIlyF76O6a_q2PELYSTD1qBv8YBlyROZ5oqXo8MQBRhAKjWuJqmyS7fDy8HBWCauxs2uESEpaNyjihFYYqGZZ1vokNHHz21CS5lQAyyChIRXlGz0APsHQNizjykpFx_p2T5lsSGZ59gpjXe4BpRXuGR7n2UTrRXSiwA1aCIZ9qKpYP9aVWdrn4q1nKC7gBBq7sG_jdytTkrA_WughVsu0gkAHAIiRdhiRmMrQvxip_rM9cNnTzJzZTOjtaZXeS7wMId5218Z7CQhWIr2DmQ0Y6HQpbkEi5pmlJmKTeMZ6W11kBu9gHbDuHgOTRCvpSxnVPRBk6-ueCKytGIoDgIxwVlD43pAxVjKlz0wJXulx-7H7ocrxrkEg5hZi1s2AwUbAAbyJu2vyHo3PyWUjix6XKLxbG7JsRM_MmeBlcr90BZ3t0yCs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f364f9a06a.mp4?token=jgg3WnCpqN1Ul7W_1hrtswiz-xb6xaSYF-4robWniChXqL4Fr9ZrmVCOAJUJVMVYSeOdgus7LUZmeFkYJiGR7L1lcLJmQXQpJwzzBixSUgFJuCUa5YG1Fifj2gHtZ5kxqnEkfz0Spjx3MwUe0inD0_NFf2-XhTyO6RXKbAd1VYeOJc_ijj0uB-CGq3-p7Fmr1deBLHU_MkK5bflM4qyb_dLOXXgCBzBOaVBeGDzleklXgoHmw4T9PuqhH9SIlyF76O6a_q2PELYSTD1qBv8YBlyROZ5oqXo8MQBRhAKjWuJqmyS7fDy8HBWCauxs2uESEpaNyjihFYYqGZZ1vokNHHz21CS5lQAyyChIRXlGz0APsHQNizjykpFx_p2T5lsSGZ59gpjXe4BpRXuGR7n2UTrRXSiwA1aCIZ9qKpYP9aVWdrn4q1nKC7gBBq7sG_jdytTkrA_WughVsu0gkAHAIiRdhiRmMrQvxip_rM9cNnTzJzZTOjtaZXeS7wMId5218Z7CQhWIr2DmQ0Y6HQpbkEi5pmlJmKTeMZ6W11kBu9gHbDuHgOTRCvpSxnVPRBk6-ueCKytGIoDgIxwVlD43pAxVjKlz0wJXulx-7H7ocrxrkEg5hZi1s2AwUbAAbyJu2vyHo3PyWUjix6XKLxbG7JsRM_MmeBlcr90BZ3t0yCs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇷
🇮🇷
فرزانه جمامی، سرمربی پیشین بسکتبال زنان استقلال: تمام اعضای خانواده‌ام بجز من طرفدار تیم پرسپولیس بودند و هنگام دربی اذیت میشدم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/Futball180TV/106795" target="_blank">📅 11:55 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106794">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ON2L0FYnSHumseDPo4-7YeWPZu_KWK4X2EpglfJw5N6kIibWY97dUVe1FJ4zuLase8lkVesju1wBmALUznTSCdtX4lHRJ8drrNE0YcAxRDsogKFWYGSTLzq6Kbj1pKnArnpod6hwANFrgfeu6sEOObfTziJ9ZnSVJWEz7YOz9au__l2bf6xYtqn4qjdhtpWgAcXMM1lDSYYypUdAmOUsjSK6XQ9fl8fUgpg0zqS_HKjDsorHpPHaEvGJLqqOn-qC4AkesZXvmydCJyPvQgHGOL-YWKEyR4Jlx1CXOmKNpXUDYmANpsn36PQUjrFzmuIrELVlLIyQpyQcc9HUha1DhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
📊
🏴󠁧󠁢󠁥󠁮󠁧󠁿
مقایسه شروع آموریم و کریک در پریمیرلیگ با منچستریونایتد؛ اخراج بعدی در راهه؟
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/Futball180TV/106794" target="_blank">📅 11:33 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106793">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bd63d44791.mp4?token=d3qDWTILxWVNRVaakxAQJDX1g02l1Coyhe4Jdlj21uQrlwtN5KVVfpyTns3QmMmZjV5MWWuu3ww8er2-BZ3cdKyKdrWpLFWpHIc2luzI7G5SI6FoFx4H6S6Kt197wBqrNKcE3plx-V5AvQY9NV65qnRrY6onRaHPJvGiJ7SlMKKj6PGgsTvywB9vuvm70S6KwkdxMRPSOgRe63SNW1XEtlFZKg6O_HGcv2_DNv3GwSykRIJXVwK4o4nD94AkA1sBqStIyCnb_161AYZxh0AoyJvt0f6w13E2tWY1o45r_XlyaOIH0fALLvajl5TDYLK-fXVAPQfKSzDCcn8j6Tq3AA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bd63d44791.mp4?token=d3qDWTILxWVNRVaakxAQJDX1g02l1Coyhe4Jdlj21uQrlwtN5KVVfpyTns3QmMmZjV5MWWuu3ww8er2-BZ3cdKyKdrWpLFWpHIc2luzI7G5SI6FoFx4H6S6Kt197wBqrNKcE3plx-V5AvQY9NV65qnRrY6onRaHPJvGiJ7SlMKKj6PGgsTvywB9vuvm70S6KwkdxMRPSOgRe63SNW1XEtlFZKg6O_HGcv2_DNv3GwSykRIJXVwK4o4nD94AkA1sBqStIyCnb_161AYZxh0AoyJvt0f6w13E2tWY1o45r_XlyaOIH0fALLvajl5TDYLK-fXVAPQfKSzDCcn8j6Tq3AA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
پاسخ بامزه علی دایی به یک سوال عجیب
طرف انتظار داشت علی دایی چی جواب بده؟ بگه نظرم در مورد خبرنگارهای مثبت، منفیه؟
😃
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/Futball180TV/106793" target="_blank">📅 11:05 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106792">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/71e2af4be6.mp4?token=CL_BLFPttlWZiYsMK_GWW8rZrYsry1EoWo6XsiNnZCAqyBOmiXmCaN3IDCF2NbxtY0u5-2dQgljelC1AyE3GhyY7G-t0hPmvzpWjme4mjy0YP7JIRkpsUdrU35FS6Ag9dELSJjn9wJBLgfSKdDgx9ym3pLB95lqYhhfzwP5ofVA1WEd3ViJDzqTUShgR-q1Cl-Q9W3X1TPYs_EHdkz9RYAfrvEyPuAAvXJFaP5Q-7rxa___O6f2y447gkIPbe4Ayy0pkPfth3Yc26mjOOBr5v4TEwFRdMd3nDCIJRkU1PAZRxN6dpDYL5uQbCNNg2-8MVpZuOmDq79JbkboCDO16bIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/71e2af4be6.mp4?token=CL_BLFPttlWZiYsMK_GWW8rZrYsry1EoWo6XsiNnZCAqyBOmiXmCaN3IDCF2NbxtY0u5-2dQgljelC1AyE3GhyY7G-t0hPmvzpWjme4mjy0YP7JIRkpsUdrU35FS6Ag9dELSJjn9wJBLgfSKdDgx9ym3pLB95lqYhhfzwP5ofVA1WEd3ViJDzqTUShgR-q1Cl-Q9W3X1TPYs_EHdkz9RYAfrvEyPuAAvXJFaP5Q-7rxa___O6f2y447gkIPbe4Ayy0pkPfth3Yc26mjOOBr5v4TEwFRdMd3nDCIJRkU1PAZRxN6dpDYL5uQbCNNg2-8MVpZuOmDq79JbkboCDO16bIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇷
دلایل جدایی اسکوچیچ از تراکتور
زنوزی: اسکوچیچ شخصیت ماجراجویی دارد شاید می خواست با تیم دیگری قهرمان لیگ شود اما...
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/Futball180TV/106792" target="_blank">📅 10:59 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106791">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bebaab7dd8.mp4?token=WmqI2TcZgOEuVW1h4CcIyl52Sg5i4hCFVe6RKLy9b91C6hv0WqmbOtfT2DSwSURC7yPqKzyTwGvnyqLzImpdLJRE3hv8iGgJexYy868DFgdqSjqolavVN0F1Czp2xaGZXVhib-_ma6NEABxs6GsmODNQPFlbMvFQxTQzeusWmJNkPSXuE7eD_dLbB1KSXMo9onqgFeZ9MUwtGCG84uRecQWSjXFxJexxoL5fPXQffdUp4XkVsnCDAHhDm5EI1oDkVsU_Ao7Rdc8S81SiOufzrXe_dFZinodV4rqRHHFNPcZcuLVukDRLYv9tcY18MpUNXRTGYvXtw9994TiFkOj6bg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bebaab7dd8.mp4?token=WmqI2TcZgOEuVW1h4CcIyl52Sg5i4hCFVe6RKLy9b91C6hv0WqmbOtfT2DSwSURC7yPqKzyTwGvnyqLzImpdLJRE3hv8iGgJexYy868DFgdqSjqolavVN0F1Czp2xaGZXVhib-_ma6NEABxs6GsmODNQPFlbMvFQxTQzeusWmJNkPSXuE7eD_dLbB1KSXMo9onqgFeZ9MUwtGCG84uRecQWSjXFxJexxoL5fPXQffdUp4XkVsnCDAHhDm5EI1oDkVsU_Ao7Rdc8S81SiOufzrXe_dFZinodV4rqRHHFNPcZcuLVukDRLYv9tcY18MpUNXRTGYvXtw9994TiFkOj6bg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇷
🇮🇷
روزی‌که استقلال تحت هدایت جواد نکونام قهرمانی و اورونوف رو تقدیم پرسپولیس کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/Futball180TV/106791" target="_blank">📅 10:40 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106790">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0c341c5cc5.mp4?token=ZSxxg0yQa1XyOelCHOV77SaLgrdSMjv8K8YvKvIIDzzq9u3OUZpCOTxHAEA3kJulE47gvNBRQLAh13gQf82papXI5z7oimN6SjbjD-OmZTAkM0h5yIhqZ7GFKpdU1uMA1ihkylQfCzBu_v-bLwQDTUmM-byQGTScMjHmNWb3cutMD_nYvpvfjuPOZ1jlH2fF7g8L90XGLn6Dz1sE-KuegL800UfTQ6-3ZBY4BdZWoz-JBEAFZIzXV6pRN9gUTCGNMP8bFqIBYoEFHfoQwu482Qa2IgpAyIfctdGfRqw03DcsUpmQS3vf_NGoRY2jtmW_v2zLg9GWTLaNU347Tquuv7Mjlq7ywOaYa4qnUpSWwlw8l7Dbl0lA-xckL1bzmhwGDF73v6y07hipnM063UYfLrIEQykb47Pvh87yBnnS1LBafavFIBoBB5ptw7DvV9IJZuT8iYVevcuwJvh5vN7qV0425F3QNCAZ0KVYmZHTeeBjFPPnjfTHgzjZyNSw7_kfMfNRYnwOyyUG2EBssvplWjlX8aAjSvonyyqQXGfa0iQk21001R1DBVNNZk99HugCVwOGCp3_Y-FM-qLeRUiBRURxZFMWXDUmeSVwJ4oSjpxoLH_bx-EA_VfbzzlybkmeBBGqqXV-y988Y8ZeJdrrzC-Royq2HUPghLscCI9KBSE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0c341c5cc5.mp4?token=ZSxxg0yQa1XyOelCHOV77SaLgrdSMjv8K8YvKvIIDzzq9u3OUZpCOTxHAEA3kJulE47gvNBRQLAh13gQf82papXI5z7oimN6SjbjD-OmZTAkM0h5yIhqZ7GFKpdU1uMA1ihkylQfCzBu_v-bLwQDTUmM-byQGTScMjHmNWb3cutMD_nYvpvfjuPOZ1jlH2fF7g8L90XGLn6Dz1sE-KuegL800UfTQ6-3ZBY4BdZWoz-JBEAFZIzXV6pRN9gUTCGNMP8bFqIBYoEFHfoQwu482Qa2IgpAyIfctdGfRqw03DcsUpmQS3vf_NGoRY2jtmW_v2zLg9GWTLaNU347Tquuv7Mjlq7ywOaYa4qnUpSWwlw8l7Dbl0lA-xckL1bzmhwGDF73v6y07hipnM063UYfLrIEQykb47Pvh87yBnnS1LBafavFIBoBB5ptw7DvV9IJZuT8iYVevcuwJvh5vN7qV0425F3QNCAZ0KVYmZHTeeBjFPPnjfTHgzjZyNSw7_kfMfNRYnwOyyUG2EBssvplWjlX8aAjSvonyyqQXGfa0iQk21001R1DBVNNZk99HugCVwOGCp3_Y-FM-qLeRUiBRURxZFMWXDUmeSVwJ4oSjpxoLH_bx-EA_VfbzzlybkmeBBGqqXV-y988Y8ZeJdrrzC-Royq2HUPghLscCI9KBSE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❗️
خداحافظی خامس رودریگز از تیم ملی کلمبیا.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/Futball180TV/106790" target="_blank">📅 10:15 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106789">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0579123b95.mp4?token=TuXTqb-4MfeQsKusYKBliL2Uuw1iYSUXtG1BXHfkrHMG-f2j7hck5dy44uUv5cszZXeyGmQG1J_JOVr9n2SGjouR5EiApBCFP0S9aP9vyiurX_U3qyx8N3q7PUtDwDmWMR0jj4vlFkUdcEpglVpuaLO5ksgsRLju1xanTilGayS1z5rk_I5Kh9m8dn2o8YOsKIe5_MKBx2nGUrLYW5yhxcZMD4n1edQ2gflisasqjcGqsIkeD1FFrp16vaGziQcKxnlR8brc9hLqd7MvkIm3z8nEW6_tMKV8i8_7G0wwHtC3D4bXtcBCJ2LGmnWJzlcaPKg0-N3bjnfA475ajSkU-w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0579123b95.mp4?token=TuXTqb-4MfeQsKusYKBliL2Uuw1iYSUXtG1BXHfkrHMG-f2j7hck5dy44uUv5cszZXeyGmQG1J_JOVr9n2SGjouR5EiApBCFP0S9aP9vyiurX_U3qyx8N3q7PUtDwDmWMR0jj4vlFkUdcEpglVpuaLO5ksgsRLju1xanTilGayS1z5rk_I5Kh9m8dn2o8YOsKIe5_MKBx2nGUrLYW5yhxcZMD4n1edQ2gflisasqjcGqsIkeD1FFrp16vaGziQcKxnlR8brc9hLqd7MvkIm3z8nEW6_tMKV8i8_7G0wwHtC3D4bXtcBCJ2LGmnWJzlcaPKg0-N3bjnfA475ajSkU-w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇷
حمله تند فرشید اسماعیلی به شفر: قبل از فینال جام حذفی گفت یا قراردادم زیاد می‌شود یا روی نیمکت نمی‌نشینم!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/Futball180TV/106789" target="_blank">📅 09:50 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106788">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1063b33e5d.mp4?token=T4NCzdNUhyKGoo6QTpAuLsKotsW_uQGCwhtqIttbOpsTSmpFenk4EM0sHdA3WeROf-nZsL6HwHDaV0vQCxjuwZo8TbYoJRHouhIJQoDefJ27alwdHd43p4BT3MQJHmRKPyhQmXiofG9ANvG6t58Ul9ar-rdg6Bl3feJbDVKDS-t0bA_z9eIbervuRsraMdz7BAySxs9SD1U3G3f_NSMApEBD4KtHTiL9eEPtqscheVxzpd5O3kIxOOllwJkd7M8e-Z698Dulple1VzMrVzhX9XVvo9zXVH_wpAGuFJT3u0PFZceB8Csacn2dtA3-qH7ZFuACJVuLriFXvXQ96RYz7ARU0RvLhFdzS5PAUR-cISSCm5ZxdvwulVg3GgGu7yXMRqWJVwZhcMEnWRLcDWriVfXx7Z65cMxSBmScbD1oHOoqgAmV-6RO1rpmUvJdIViuuxl3hNF7qfs9mShLhyzidl4jofICasuavS_wBQn6JTkXx9SPArdO9iV86Y2QANCqmKq8WtoKULwb01hAoqx1ezYoxHd9hnI8BTnAbPVm2-SoltBbe-4Yb2FlAXY5P6zJPnsytXUb_yIfYzm0xMLeOOO9WOIeG_alqFYyhav4ToAmRZKdtrxq3nmquYQqNKe4fnWDA-WtEv0rcG5rl6HZioj59IrULCVmC2h7TeZXzXs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1063b33e5d.mp4?token=T4NCzdNUhyKGoo6QTpAuLsKotsW_uQGCwhtqIttbOpsTSmpFenk4EM0sHdA3WeROf-nZsL6HwHDaV0vQCxjuwZo8TbYoJRHouhIJQoDefJ27alwdHd43p4BT3MQJHmRKPyhQmXiofG9ANvG6t58Ul9ar-rdg6Bl3feJbDVKDS-t0bA_z9eIbervuRsraMdz7BAySxs9SD1U3G3f_NSMApEBD4KtHTiL9eEPtqscheVxzpd5O3kIxOOllwJkd7M8e-Z698Dulple1VzMrVzhX9XVvo9zXVH_wpAGuFJT3u0PFZceB8Csacn2dtA3-qH7ZFuACJVuLriFXvXQ96RYz7ARU0RvLhFdzS5PAUR-cISSCm5ZxdvwulVg3GgGu7yXMRqWJVwZhcMEnWRLcDWriVfXx7Z65cMxSBmScbD1oHOoqgAmV-6RO1rpmUvJdIViuuxl3hNF7qfs9mShLhyzidl4jofICasuavS_wBQn6JTkXx9SPArdO9iV86Y2QANCqmKq8WtoKULwb01hAoqx1ezYoxHd9hnI8BTnAbPVm2-SoltBbe-4Yb2FlAXY5P6zJPnsytXUb_yIfYzm0xMLeOOO9WOIeG_alqFYyhav4ToAmRZKdtrxq3nmquYQqNKe4fnWDA-WtEv0rcG5rl6HZioj59IrULCVmC2h7TeZXzXs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💥
👑
🇮🇷
ینی بهتر از این خانم بنظرم کسی نمیتونست تمدن کهن ایران رو بیان کنه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/Futball180TV/106788" target="_blank">📅 09:25 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106787">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7912d30312.mp4?token=cewg0HA5JEtjAXWKzzpXxtZAlE-55upWAoobL_IkE0P5ZVPfGsZ1zjzcUxBX6O690h3oHP5t8BstKPOAfPFATrYFTZKXOUuhamV-aACOaYFaWsBojsfQUd3uqyomQG2g9zvkFj3YrxTwtJNIHlR9sY6NFoFQjHxsKb4rjfloKeTi8Vw3yDjLdGv_m93gfAtiMcwbO9kkyE3kf6Zjv6irvPlNUvTxqcmFi3L081dPKefcM7MnoL2-6AXEmBlpH7bn4eWUAksvZKc1bWDlS-UyWvcoh4_UCrFilOYZ7EUPzfswAkmhgVYS1kGUZM95YQZvyJCV-MMDqzoljyR7nr51azH_NykgQr474k3eyxSmvwub3ue8zs7CMc3Q50mj4KYJfbfABizO12NIbi1qjVmTc3zPSazWYHdxf833P0UaCJ-S0BCC_4e6wP-ClxKj9WgFPV_K5yatrn3M-CMu7eSJknm4IEzQVQP4lvcBRUEFP9ByPzwsx-wusYjiyerdBc1dKr2A9R276xmxH4ZX-tQoNw20XTTkdJY667VBa_H9ducpy2AF8n7Fz2T9iAau0qur0q_W4JQkta7ZetmxLvQEBODE6CzJBrD4aAo1gxhAy_KnkostVHBbD-zL5Tb9WOBv0DMNr-taTBuWN7G3CVTqrUWQp4AknUXVEECFWrkBJu4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7912d30312.mp4?token=cewg0HA5JEtjAXWKzzpXxtZAlE-55upWAoobL_IkE0P5ZVPfGsZ1zjzcUxBX6O690h3oHP5t8BstKPOAfPFATrYFTZKXOUuhamV-aACOaYFaWsBojsfQUd3uqyomQG2g9zvkFj3YrxTwtJNIHlR9sY6NFoFQjHxsKb4rjfloKeTi8Vw3yDjLdGv_m93gfAtiMcwbO9kkyE3kf6Zjv6irvPlNUvTxqcmFi3L081dPKefcM7MnoL2-6AXEmBlpH7bn4eWUAksvZKc1bWDlS-UyWvcoh4_UCrFilOYZ7EUPzfswAkmhgVYS1kGUZM95YQZvyJCV-MMDqzoljyR7nr51azH_NykgQr474k3eyxSmvwub3ue8zs7CMc3Q50mj4KYJfbfABizO12NIbi1qjVmTc3zPSazWYHdxf833P0UaCJ-S0BCC_4e6wP-ClxKj9WgFPV_K5yatrn3M-CMu7eSJknm4IEzQVQP4lvcBRUEFP9ByPzwsx-wusYjiyerdBc1dKr2A9R276xmxH4ZX-tQoNw20XTTkdJY667VBa_H9ducpy2AF8n7Fz2T9iAau0qur0q_W4JQkta7ZetmxLvQEBODE6CzJBrD4aAo1gxhAy_KnkostVHBbD-zL5Tb9WOBv0DMNr-taTBuWN7G3CVTqrUWQp4AknUXVEECFWrkBJu4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✔️
👍
صحبت جالب رسول‌مجیدی درباره تواضع رودری ستاره بارسا در دلجویی از والنسیا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/Futball180TV/106787" target="_blank">📅 09:02 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106786">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/Futball180TV/106786" target="_blank">📅 00:53 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106785">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTrexBet IR</strong></div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/Futball180TV/106785" target="_blank">📅 00:53 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106784">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/swkaGpy_cjukz8FudH63bD04XQRytTuYTdn7im74gXA-CYrCxChtUbYHKkioaptCg3rQf9C82gPtbYIlOsjEU4Dq_ISP4y80OHMOWUOWb8fIPGyazjmKhq2aozi1UB7LPvhk3u8zUFuNkapMzPa7n6u-ESh6NvgeRuN0nWjB3kcamax8bbDnA-nTAd86ilGNDS_OxxwvszDaaMUU_gC47MCI15StCfQBjSVn3LrcZ8wzT2B0dscWhjnBtzjxjYw5BIzpIb1_nuKojMQlel-d4hAg1qDgsqv4jyVcx1v7uaEBDpNk_S73pi-6gFWoPsqgGI5v5BrsU-yiy9gh1E0FTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✔️
📊
🇪🇺
نتایج هفته اول لیگ اروپا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/Futball180TV/106784" target="_blank">📅 00:34 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106783">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ea7884a87d.mp4?token=P7BJQsPXqweDZ-EEOojtHxlCELl0H24kAAgTaZfYNZPYjlRdEfs7lnPcSCev0-pOpG_tDdVrZ8P8REgRov2Z510dAFia51l8rtXYkEFsIS2iV6BkvpXRVjuxOevoFLuWf7mz12hpgbHvhlDU4w3BI1lVnlBJh_m4IjZlnRzw1LLlJJnKCubQseCCDm0TkiuIV_cnIcYKyjb0Dt_AjjGYnqMkww9rkerHsWgjAfdcCV2FV4-duxx7xPtoXZwXrtlpIAkYGEI6sIGlb6zR_JyIU76aF43qVtYLxPVaNVeQetbiAUXJtZrcPa00gUXkbBUZu-Nvq7XePWkzz8qs7lMczA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ea7884a87d.mp4?token=P7BJQsPXqweDZ-EEOojtHxlCELl0H24kAAgTaZfYNZPYjlRdEfs7lnPcSCev0-pOpG_tDdVrZ8P8REgRov2Z510dAFia51l8rtXYkEFsIS2iV6BkvpXRVjuxOevoFLuWf7mz12hpgbHvhlDU4w3BI1lVnlBJh_m4IjZlnRzw1LLlJJnKCubQseCCDm0TkiuIV_cnIcYKyjb0Dt_AjjGYnqMkww9rkerHsWgjAfdcCV2FV4-duxx7xPtoXZwXrtlpIAkYGEI6sIGlb6zR_JyIU76aF43qVtYLxPVaNVeQetbiAUXJtZrcPa00gUXkbBUZu-Nvq7XePWkzz8qs7lMczA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇷
🇺🇸
ادعای هومن افاضلی: ایران در آمریکا از ورزشگاه آزادی هم محبوب تر بود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/Futball180TV/106783" target="_blank">📅 00:22 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106782">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OCuKHDYNy5QLHQGh-kI66WLGF8ehnnS6ZTi00HA8yBgsb9qudsUSiLyrlFGkdc3rxQngp8o-mA_tDW-v9ebbJ7yA6pA__BU7K69XNKxdyVnm3Pv-KEngpg5aAy3MTsjfZjhzAcfWQwot0WCigaBJmCjHmfxG_9TodSONU4bBbN7N0UNl_Gy32iRqJsXE79alViLS3JYjasm0FG293gtLdeVfHgECpiHsnnBy_dstXOUzC4mkzWj7LczqIlvqspeYnpiPWoMaC48zieWBo1XXUQL7E4TMrlkOuzgu22jTAHxHSW5aJMPbXwZe7wtzwYeke8zK0q-GQgq3KQvA5uuZJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
جام‌اتحادیه انگلیس؛ سیتیزن‌ها در یک بازی درخشان و با گل‌های بازیکنان ذخیره خود مقابل نوریچ پیروز شدند
منچسترسیتی
😄
-
😏
نوریچ
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/Futball180TV/106782" target="_blank">📅 23:50 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106781">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/beJXAEaA6S5Tv0TTpDQ_THPpG0EZoY-T3TNyXhCNeKa-4Heae8utkduro2EQBxvSA15I33Y3NtIN4_8_y0hQ1EwzNgn_dc48u5_ioX-_OhDL_tbW3knVvHRmAbeuPDyXD4it58ydeTWVpyInuHR4yohNTHyMnJ5Wwxnu99U7KtNr-GKLs2KS0M8B2f1i0vl8jPHatRiAJsDJe0LP34y01ZtTX3kFY2qHKYVwpuS-zlXm1GSZcjjaNXdhi6U3cc5SKdcvThXNij23swBfNOqVJL99YEIvNGAlbAKjj8IJWj2hj4EzQWlkLiXLhz7vB00W5RXsNon5Tqph85dCJbpYfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
وقتی لیونل مسی در سال ۲۰۲۳ به اینتر میامی پیوست، این تیم در قعر کنفرانس شرق MLS قرار داشت و تا اون لحظه هیچ جام رسمی‌ای در تاریخش نگرفته بود.
✅
مسی پس از ۱۱۵ بازی، به ۱۰۰ گل با پیراهن اینتر میامی رسید و این تیم را به چهارمین جام تاریخش از زمان حضور خودش رساند.
🐐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/Futball180TV/106781" target="_blank">📅 23:27 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106780">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0af53c1869.mp4?token=VNORWdtsFkyQlXr-CubgKUYOZrFp_v6UyX_mj_TFLiosd4yvW_b5QN2AM6JBnttyIcQVGuNmiDJPqm5C1vguPdt0_rXH2eKVsrMywwvwUiI-rhCqQuyJMuH-0V8HWUfiXDpeK2LNqdbXeMli_JEDzHTMzqkJz1CYlWvdHJ1ZxiDHJC0OWmqokHR77M8d3fIhT6T6I3fWAK53APytaqyxTB72JyMOzj2Tnxhq6Vt_QSI36fSyaQRrNY92T4gfe0d5OF9Oehcs6SOYtZkYAU8xSjuFx3xxpPx2Xz3giFIvT9A3UBUc0Ko4EtxFFIQ498_--e59_BjoV7U-oKLpXD8q1A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0af53c1869.mp4?token=VNORWdtsFkyQlXr-CubgKUYOZrFp_v6UyX_mj_TFLiosd4yvW_b5QN2AM6JBnttyIcQVGuNmiDJPqm5C1vguPdt0_rXH2eKVsrMywwvwUiI-rhCqQuyJMuH-0V8HWUfiXDpeK2LNqdbXeMli_JEDzHTMzqkJz1CYlWvdHJ1ZxiDHJC0OWmqokHR77M8d3fIhT6T6I3fWAK53APytaqyxTB72JyMOzj2Tnxhq6Vt_QSI36fSyaQRrNY92T4gfe0d5OF9Oehcs6SOYtZkYAU8xSjuFx3xxpPx2Xz3giFIvT9A3UBUc0Ko4EtxFFIQ498_--e59_BjoV7U-oKLpXD8q1A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✔️
🟡
دفاع قاطعانه بیگ‌آنز پوستکوگلو از رونالدو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/Futball180TV/106780" target="_blank">📅 22:45 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106779">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JfVM7sttIlUpbz7_tnv8_lTtLDI9fJK4xWkwqjz7Iei6hymBeGq3mi73vsqKq7q44NFdet7D3NFj7Riss38FJYfb3DveR8fGGfv8v16Rmf7U24ej2MLgBVhiTT66vxiXMyKdbaVh_Hdnr6smxW5wJKObiLxoi-vlhDtypodsZ51yP6dBmWVyFleQWhCuwdwIaoXNdhFXNpWgjKB1JHHD5kNsBMokhhptLZIsRRAGjXxovnEEsBAWyW5DA3FH2XL_4RXqLF5YJ_J9k-NaugpmuyYS-IE6OPqXZZHnw8OZgLn-u_U_PMD3KsHTJ7GGkDzZjL8mHAJgbvoQ_gNBeSKOZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
مقایسه اسطوره مسی و رونالدو در سال ۲۰۲۶
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/Futball180TV/106779" target="_blank">📅 22:15 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106778">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HlnBp8MhxebSL4riv00h7Tx7uqnELWNQUbaDM2jUv89QE73qjvkmyhCvpjasRaTh-mReciqmT4jrVrTSEEf0KkZNl6RTqmh7JUfxWl5lfRbVuReBJkJ1JeORzMRgTzmO-t28LeLHJ97sDAC3uU5a8gnjQ_uEltdw6dgY-UERNa1oY3ESokdXgHbWHLRaYKFSFm5OFyCE1nakEcV1nBeB-FE5gNq218sdKDh7ZvAmTt1sux3ssx4p0uBUKITsK4deEwJ0End9IvjgOjiMHfFRju9nWPGE_ndejxvrQBjYDXK2BCWzc1UwblwBjYMW7TcrQUG0cmNpXGSvrZ_6rwPNng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
✅
⚽️
هفته اول لیگ اروپا؛ ترکیب لخ‌پوزنان مقابل کریستال پالاس با حضور الهیار صیادمنش
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/106778" target="_blank">📅 21:43 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106777">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">✔️
🇮🇷
🎙
صحبت‌های جالب نوید استادرحیمی درباره عملکرد درخشان یاسر‌آسانی در استقلال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/106777" target="_blank">📅 21:15 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106776">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Th1VK9RyB4H3kj6vqFDexxESdBx-CiN4KhjELQy8awm3R7IGPFHL3cMtjT0h30vE68Jvn0oL5r6p0JdLLBI81Lc4grTk9pJaaxHmmgevm2dpErUmKALyMaKN5fPcfp5op817RTywLTrcJFQLlBc0u0CJuylz6EEQhpi2srVZJ8oZf6JU06C2dsAJQk0d2qCfDj4OdHMRJoqJxi58Xd9c-TjjAMFaXTI6IF6jubXckTP315jetIXPtY-l-99xVUXgM5INWik1AgAT8cWnEZqyvUiOeN1DFGAqroHm6R5SEuNijjDwii7X-oejk7TmDENqtLqs7MqTuVd6oWGeuj3ocQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
جام اتحادیه انگلیس؛ ترکیب منچسترسیتی برابر نوریچ؛ ساعت 22:00
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/Futball180TV/106776" target="_blank">📅 20:52 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106775">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/af8c416616.mp4?token=DO6rAmM3S7g_-zOdGMYWeute3XO8wDdRZ7IhXJ4u1vEyBnJAA4izZYOw514S0lbs_H2MI6YYXgIUiCd4kTnqtMPuRhDGMJyp9ZCAtGxSHcVqgkb03IZZGVBXBHLOArdQClruYdIrRbVoYmAfERv7FGeZ9R0Bmi34A93guNOBEhanVe69QVYx5CQoqGrB-HRDNhzt3SvDXppSWushvmOP60fSo6dwQft29WHNFjIrdgiMbTicWdwZYWMR79jHeTcAF66zleURvBJ8QJrN_MSW8WL045ERW7SCFuhOj9FCU_g_L0ROEhb8qZNvefP5rP68uXsCOfOpzGpaIoQjp-w7PVI-mKI-FRh3vZgOESLJPS2pMbFj4znRYdU5eyvP5XAVffdVntrTLQSALOqXG-o3i8pyZ-CbvaJDCy0tlffr8_JyMZACRCpd_fpiHgTca2KSmx7rb5d6plP64GFmD8mTmdGwAoqaMhCMiHG5DGctiPFs5OLjkvEVu9cvLry1Po18FkgQfjrYZ6SM5XltGouVcUCjc5pMg3b9x6lyGV-tWZl-uf5Gq3CvZ_Y31Fp5dybTenZm6WTcknMjtFk3bYBZk0OXhh6XdjsgjEXfW26FEEOxqRfWqdEQjDb_UWDluipb7SyaCotSjpS4pPzX1guwz-QYtjSJoqkc8H_9Pzl8jpY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/af8c416616.mp4?token=DO6rAmM3S7g_-zOdGMYWeute3XO8wDdRZ7IhXJ4u1vEyBnJAA4izZYOw514S0lbs_H2MI6YYXgIUiCd4kTnqtMPuRhDGMJyp9ZCAtGxSHcVqgkb03IZZGVBXBHLOArdQClruYdIrRbVoYmAfERv7FGeZ9R0Bmi34A93guNOBEhanVe69QVYx5CQoqGrB-HRDNhzt3SvDXppSWushvmOP60fSo6dwQft29WHNFjIrdgiMbTicWdwZYWMR79jHeTcAF66zleURvBJ8QJrN_MSW8WL045ERW7SCFuhOj9FCU_g_L0ROEhb8qZNvefP5rP68uXsCOfOpzGpaIoQjp-w7PVI-mKI-FRh3vZgOESLJPS2pMbFj4znRYdU5eyvP5XAVffdVntrTLQSALOqXG-o3i8pyZ-CbvaJDCy0tlffr8_JyMZACRCpd_fpiHgTca2KSmx7rb5d6plP64GFmD8mTmdGwAoqaMhCMiHG5DGctiPFs5OLjkvEVu9cvLry1Po18FkgQfjrYZ6SM5XltGouVcUCjc5pMg3b9x6lyGV-tWZl-uf5Gq3CvZ_Y31Fp5dybTenZm6WTcknMjtFk3bYBZk0OXhh6XdjsgjEXfW26FEEOxqRfWqdEQjDb_UWDluipb7SyaCotSjpS4pPzX1guwz-QYtjSJoqkc8H_9Pzl8jpY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇷
🇮🇷
توضیحات فرشید اسماعیلی درباره چیپ معروف در دربی تهران
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/Futball180TV/106775" target="_blank">📅 20:45 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106774">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3d822ce6be.mp4?token=gr4g88Odo5GPOJqLrwefMxA5JbPQwaLWGn1Oa6jCXUQkkk8k3tPAhJJIWO3x7HFhDpXmoVX6KtPYIT8KQ-mKUZ8Dkg3L6dgXl8Z5v9xl91NUQozA8_0DP71sgk_8AQQPB7sqw3EuwbpcdQXQjt2f93QV7wZH9cJTY_XqAi3qpjFokzC0k5tzS0Jsc6FIMcWBwMqA785wZxZFbEZ7RKRa_h9lUpWzpWS8NhUe3WuBBbvTg0v6FNMkKjeevvJwI8CAy8VaHAbwz7kwkV8N4LKc0e3RGcq2ECmJvW1kzKe9yX6taJ0Wcrv66gLwloLti1xgOhJJuBXuvZ6q452FlShRYw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3d822ce6be.mp4?token=gr4g88Odo5GPOJqLrwefMxA5JbPQwaLWGn1Oa6jCXUQkkk8k3tPAhJJIWO3x7HFhDpXmoVX6KtPYIT8KQ-mKUZ8Dkg3L6dgXl8Z5v9xl91NUQozA8_0DP71sgk_8AQQPB7sqw3EuwbpcdQXQjt2f93QV7wZH9cJTY_XqAi3qpjFokzC0k5tzS0Jsc6FIMcWBwMqA785wZxZFbEZ7RKRa_h9lUpWzpWS8NhUe3WuBBbvTg0v6FNMkKjeevvJwI8CAy8VaHAbwz7kwkV8N4LKc0e3RGcq2ECmJvW1kzKe9yX6taJ0Wcrv66gLwloLti1xgOhJJuBXuvZ6q452FlShRYw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">باز خوبه قبل گفتن یه ببخشید گفت
😆
😆
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/Futball180TV/106774" target="_blank">📅 20:15 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106772">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ae6b91a252.mp4?token=neAcXEKJt92mxIZsBsHD2baIQSkNAUFi6ht7kqEdKp17sGZhbiz_QuspEq3X8utzuaerE9mCLVkpX6gQG75nDKHwBrqwgOc-YOF0nP119f44kPPbp86irZbIC9DMY3V6HbG_wKQQwAXSSonC_bEd0yEMeROCb5QwXarvGBUYO3YAfe21i9BeZoe9K74E75ehphqlQ4xM_rLkRISnKPsjam0g4MTN8ivH0LEFbHjc2KiWvL305MMck4Rrk51O-Tq9GkIF738SuvFHv2Hm8OWQAs6B70xwJvfIpVUcNjS1_uSwlkD40F_z7RdB4ldXP31xND0I4IBv_ATGMKoo_Rwp-g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ae6b91a252.mp4?token=neAcXEKJt92mxIZsBsHD2baIQSkNAUFi6ht7kqEdKp17sGZhbiz_QuspEq3X8utzuaerE9mCLVkpX6gQG75nDKHwBrqwgOc-YOF0nP119f44kPPbp86irZbIC9DMY3V6HbG_wKQQwAXSSonC_bEd0yEMeROCb5QwXarvGBUYO3YAfe21i9BeZoe9K74E75ehphqlQ4xM_rLkRISnKPsjam0g4MTN8ivH0LEFbHjc2KiWvL305MMck4Rrk51O-Tq9GkIF738SuvFHv2Hm8OWQAs6B70xwJvfIpVUcNjS1_uSwlkD40F_z7RdB4ldXP31xND0I4IBv_ATGMKoo_Rwp-g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⚠️
یه خونواده ایرانی عروسی گرفتن، بعد اسنوپ داگ رو به عنوان خواننده آوردن
😐
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/106772" target="_blank">📅 19:45 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106771">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dd7aec7c83.mp4?token=HqFPARvlnMNrugE_yNCo2VGCBr67i_z-rDx94EoGM06QIBiDFBkS_K4nsGmx-ulOFW9Pbmte6yOTVWt__gXTz5JwYKUFjowXZ9Sw0PIrMb_jTTERdiFpcaHVu3uBFL0A0aE4GgM2NVKN-esEeqXxPkFwhyvt5vXYjxrvASGbDo4-Ok6_t8PY-ASsw9CesrHV_sbkKOq2wRrtxECgM748vGWjaWLxNX7HgnfRsbO_xfplS3nYPbtIg9fen5Fdk4t5586TE-d_MSRYAPHU7KWsmJG6uhrL4mx_VXY_gyBevjOJy_y7IhmPEOEpyld2CweQaGIg5CrUYvB9L0klKMyrgyu0pQmzOeuKTMOFSP6fjmB97ekfl9t1hzbAsFT27hB3Q6Ps1HCEwi4HSDhN8RwBgoKpn92SD38RGWmjPTtkTxlS7n5HVqc953xVBxWsogJgl1Ov01wXkK1lNTa6eI03wVI_Cyn_2aVI0J2o1oPxi3zw9XFkGyl2yWtyhGuD-3EXyTk4Lrm4R7VVd5TP07VA9-uZpCvWFFBLNM4j9jrcy7XSl27qfLP30WaXLuGm1z04sfJEgw5_v41teXqZZ0rcYduuNbzixWutun5nzc0W3qoslh_wLbPxTgUpPY4Ssi5yMMRrgOUNA8j1oOLKCPPA34ZCFhncDBLhBSK0tby6SZs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dd7aec7c83.mp4?token=HqFPARvlnMNrugE_yNCo2VGCBr67i_z-rDx94EoGM06QIBiDFBkS_K4nsGmx-ulOFW9Pbmte6yOTVWt__gXTz5JwYKUFjowXZ9Sw0PIrMb_jTTERdiFpcaHVu3uBFL0A0aE4GgM2NVKN-esEeqXxPkFwhyvt5vXYjxrvASGbDo4-Ok6_t8PY-ASsw9CesrHV_sbkKOq2wRrtxECgM748vGWjaWLxNX7HgnfRsbO_xfplS3nYPbtIg9fen5Fdk4t5586TE-d_MSRYAPHU7KWsmJG6uhrL4mx_VXY_gyBevjOJy_y7IhmPEOEpyld2CweQaGIg5CrUYvB9L0klKMyrgyu0pQmzOeuKTMOFSP6fjmB97ekfl9t1hzbAsFT27hB3Q6Ps1HCEwi4HSDhN8RwBgoKpn92SD38RGWmjPTtkTxlS7n5HVqc953xVBxWsogJgl1Ov01wXkK1lNTa6eI03wVI_Cyn_2aVI0J2o1oPxi3zw9XFkGyl2yWtyhGuD-3EXyTk4Lrm4R7VVd5TP07VA9-uZpCvWFFBLNM4j9jrcy7XSl27qfLP30WaXLuGm1z04sfJEgw5_v41teXqZZ0rcYduuNbzixWutun5nzc0W3qoslh_wLbPxTgUpPY4Ssi5yMMRrgOUNA8j1oOLKCPPA34ZCFhncDBLhBSK0tby6SZs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🗓
🇮🇷
۸ سال پیش در چنین روزی، کامبک پرسپولیس مقابل الدحیل. اون دوران الدحیل تو ۵۱ بازی فقط یک باخت داشت که اونم جلو پرسپولیس برانکو بود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/106771" target="_blank">📅 19:15 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106770">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f5345b9e16.mp4?token=gNnBIOYymxAt_TkhmXmj1nGQBlnTPP7MAYQA0VMPZi1kXaD-zGo5v3jIZHa8UchY4mfkLBqmU4FLEjT_BjBu1IwEileHNkSRZ8uUzI1JnAn84nMeomWIzYO6szZbdBeAo-Z5fpeTMJFcygC7ltJh9nA8gfK6vniiPwUUAuiPXqOm21Wiovisu0o_0f3V8JU-UcV84xdnyVSNzcJdoq1CxGdMKZGHA15L6cAspJaTyg4sQ7a3N_J1jRzMmfxO4G6oz5aIJjclp6myaGsggdWT4n1hREpqdPqpH8IRCAKboU_DzYcOA5zP_50if4f8pMt-2GefDomWzW2suooSp3fzIQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f5345b9e16.mp4?token=gNnBIOYymxAt_TkhmXmj1nGQBlnTPP7MAYQA0VMPZi1kXaD-zGo5v3jIZHa8UchY4mfkLBqmU4FLEjT_BjBu1IwEileHNkSRZ8uUzI1JnAn84nMeomWIzYO6szZbdBeAo-Z5fpeTMJFcygC7ltJh9nA8gfK6vniiPwUUAuiPXqOm21Wiovisu0o_0f3V8JU-UcV84xdnyVSNzcJdoq1CxGdMKZGHA15L6cAspJaTyg4sQ7a3N_J1jRzMmfxO4G6oz5aIJjclp6myaGsggdWT4n1hREpqdPqpH8IRCAKboU_DzYcOA5zP_50if4f8pMt-2GefDomWzW2suooSp3fzIQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پایانِ عصر خامس رودریگز در تیم‌ملی کلمبیا.
💔
🇨🇴
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/106770" target="_blank">📅 18:45 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106769">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d9692b0808.mp4?token=t7IG3VWm2oe6fCu06RdKDA5qbhg-Q_sv3zsykeQyNar3FXZr0KJPE51K0HYf8XRiVdjCUl8C7kzGztfG2WZpJHwMSoTd7QCbIdbcpBNj7rWmLMonp28lwbvXg-LhpvXPYhZEuucD4lV27jWMEpNIafG0ZZSdEuG6u4VhC380Em_WEhnMbEM7dSfIaS1BRNrBBaWc_2lUIXAqWZ7sU5lkuhGjQjLpuTjY5FS5uLJhFVpK_4fDSFGouO2TzpEwBUjNpNScbQU94uWRpqNWxKVslR-2S2bYFi3O0QDJX4CPLBzCcBqK2W6UnYsTzLQ9hMxsWcEBFuMALDX8NL8jBXyowQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d9692b0808.mp4?token=t7IG3VWm2oe6fCu06RdKDA5qbhg-Q_sv3zsykeQyNar3FXZr0KJPE51K0HYf8XRiVdjCUl8C7kzGztfG2WZpJHwMSoTd7QCbIdbcpBNj7rWmLMonp28lwbvXg-LhpvXPYhZEuucD4lV27jWMEpNIafG0ZZSdEuG6u4VhC380Em_WEhnMbEM7dSfIaS1BRNrBBaWc_2lUIXAqWZ7sU5lkuhGjQjLpuTjY5FS5uLJhFVpK_4fDSFGouO2TzpEwBUjNpNScbQU94uWRpqNWxKVslR-2S2bYFi3O0QDJX4CPLBzCcBqK2W6UnYsTzLQ9hMxsWcEBFuMALDX8NL8jBXyowQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❗️
🎙
🇮🇷
بابک‌مرادی بازیکن سابق استقلال: ذهن فرهاد مجیدی را خراب کردند؛ خیلی آدم خوبیه اما یه دستیار مرموز و بی‌شرف در استقلال داشت!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/Futball180TV/106769" target="_blank">📅 18:15 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106768">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m_nwAJWRzqLJSrO-5_5hr0ug_9Fli4HOQZwyJBxjKSpnF42pxtWBYdpNYdjrEmoxAbLTMlJ1qKgogweIUWYD9xi7EtgAKreCEUp5YqbcN4JBvD5YIHoqRTmjDRsZM0OT_6NE2FsabG-CBwOR3N7owA3g3WrmphK4q5q0Dz1VQfeTdIEkBfn6T2qps5wLlM8JGNTZtgH-_W1DB7glRDGSXichXDfLhwNutCQ7OSd-Gn4W71-Wrvl4K3Lym5w5J0DPG9rEfKnDst8CEFfJqtTys56GxU1BnGcumlSnUqJhSk6fHM-VBfNXkxsWN1JqMGaq1tkgvH_UPBNx80ISkzDTFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
✔️
برنامه سوپرجام اسپانیا 2027 اعلام شد
نیمه‌نهایی اول
🇪🇸
بارسلونا_ اتلتیکومادرید
🇪🇸
⚽️
13 بهمن 1405
⏰
ساعت 23:30 به وقت ایران
نیمه‌نهایی دوم
🇪🇸
رئال سوسیداد _ رئال مادرید
🇪🇸
⚽️
14 بهمن 1405
⏰
ساعت 23:30 به وقت ایران
🇪🇸
فینال سوپرجام اسپانیا
⚽️
17 بهمن 1405
⏰
ساعت 23:30
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/Futball180TV/106768" target="_blank">📅 17:55 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106767">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4d8b49aaa0.mp4?token=XXum9JZhozBzqZzccbQ7PUs5eHvVJEMVeTZyCvsfxF138nOdgoYEIWlmIOxR4hwtxHekghZqeWHK7fweJb9B3Eh2D_2iMjXRajM00Qfp1fF6RvxgxSCEVm86-YIYOHN6Jyd6Ri5RGy2x5ypGWX8nXUrn4vy90wFi4i94W3XAWN5xt2hAirhv3HzR_nyzi1JwclHbCxQtvbW7x_Ie_uBzl_x3kD_i4kfv8nio8TWYOCTi8ZkrN-hLdOYdbhZBRegnylwzg2_KmFlfGZDE9NdPECVfz1jg9S5LZdkB_AIOx4-F6k3XuNyvMBasfg0tHmgA5YW1NEuKlOkwtmPrTWQKjQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4d8b49aaa0.mp4?token=XXum9JZhozBzqZzccbQ7PUs5eHvVJEMVeTZyCvsfxF138nOdgoYEIWlmIOxR4hwtxHekghZqeWHK7fweJb9B3Eh2D_2iMjXRajM00Qfp1fF6RvxgxSCEVm86-YIYOHN6Jyd6Ri5RGy2x5ypGWX8nXUrn4vy90wFi4i94W3XAWN5xt2hAirhv3HzR_nyzi1JwclHbCxQtvbW7x_Ie_uBzl_x3kD_i4kfv8nio8TWYOCTi8ZkrN-hLdOYdbhZBRegnylwzg2_KmFlfGZDE9NdPECVfz1jg9S5LZdkB_AIOx4-F6k3XuNyvMBasfg0tHmgA5YW1NEuKlOkwtmPrTWQKjQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇷
انتقاد جالب میثاقی به زمان‌بندی ارائه‌شده از سوی سازمان‌لیگ‌برای هفته‌های آتی لیگ‌برتر!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/Futball180TV/106767" target="_blank">📅 17:38 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106766">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/Futball180TV/106766" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/Futball180TV/106766" target="_blank">📅 17:37 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106765">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tGjVf2fFGgURDxOAvFWIgH-bL7cM0TnwBi08D2czO824DKTqYO6AKgozGWglon0MVnLT_qyR6QAT49p3EPsEDQ3cKHNU1WEtvKnz87v9SvulSiKNVyeQiK1fdd7L4fpO9NVIaTISV1tySptIjgfN9nmaLPgH-5jtqyrw0O3F5OfHtgYK4hijeOYPC_Kxej5lBzrjbVUwzhtEvqNZWqwvn4ouznN1EHHK8YgWIR6Izl-76NklpmlF9qOS1MuNmTx4-9wI2TwztA9WOj5ic06_PsZTIkSt97De9aEcEgAraHvEL51a_m2oGqdIF9bAuHxLtTKXu-TACAUNlgWOzut-LQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
وقتشه هیجان رو به اوج برسونی!
🦖
با
TrexBet
مجموعه‌ای متنوع از بازی‌های کازینو‌ی زنده، و اسلات‌های جذاب رو میتونی تجربه کنی
🦖
تجربه‌ای سریع و روان
🦖
دسترسی سریع و راحت
🦖
هیجان در هر اسپین
🦖
🦖
🦖
🦖
🦖
🦖
🦖
🦖
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/106765" target="_blank">📅 17:37 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106764">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/acdc40365b.mp4?token=DMdPTVh7AYzdzZkkoE7oNkFkHoAwcJ43OvANvKMeMnSmAp-_90dcs-5e3bCmtPV4fjmlOVMUDsd0_SuN0Y-zCx6hzZCGNVAu6hPk29Idcq5adcEM_STFd8GS4U45l7tck0EUBbXICxc-xeQWSH0J1gzcmgMm7LETZ6D5VP58fXofEPi-MgUulZNEnY3nv7-X1gjgU-YeEX8QeAemxBxxOl0G1EwfTXc9BJ9l3M6VFTXXo55ZTGyfi-B0dbLHRYkDKA3nM6q7xpNtgQpBmhA9AT-Qpc9xWcylGVw3hJ6hLqomF3bdA-Srs_e-MlF4z02DiL_DJaivNemhHHODvd6lug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/acdc40365b.mp4?token=DMdPTVh7AYzdzZkkoE7oNkFkHoAwcJ43OvANvKMeMnSmAp-_90dcs-5e3bCmtPV4fjmlOVMUDsd0_SuN0Y-zCx6hzZCGNVAu6hPk29Idcq5adcEM_STFd8GS4U45l7tck0EUBbXICxc-xeQWSH0J1gzcmgMm7LETZ6D5VP58fXofEPi-MgUulZNEnY3nv7-X1gjgU-YeEX8QeAemxBxxOl0G1EwfTXc9BJ9l3M6VFTXXo55ZTGyfi-B0dbLHRYkDKA3nM6q7xpNtgQpBmhA9AT-Qpc9xWcylGVw3hJ6hLqomF3bdA-Srs_e-MlF4z02DiL_DJaivNemhHHODvd6lug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❗️
🎙
🇮🇷
واقعا چیشد که به اینجا رسیدیم که یه بازیکن فوتبال برای خودش آرزوی مرگ میکنه!
صحبت‌های تلخ بابک‌مرادی بازیکن سابق استقلال!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/Futball180TV/106764" target="_blank">📅 17:20 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106763">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VmbddO631lmbAHaIdSDRX4I4_IbYF0QfUH8dImh3YzxOR2J_wnkhOsRFsXy77XHzP1ldk2u7WlWv6W-iO--35RkXXjbU8NLqZwlIyIpdV44GE_nlVwYjkIUe_0k5FEfcxWmj71vS9NuIHFOR0qyGSbT-dIbfAS_wiNZO9K5zuVGXGJFoD-56SdiHVWQ9SkNeAuBGjUPGUceThI47QuZRMSTNKTwWJLYoGdaj7bOMYwvxixZn7gWawTh75jDglIHEqUD9emZ9L54xqTrCdQxFx-Bq9HiCrLX9lLolRe0VvGQ4wTQ2ba3Ux3WalddGnkaaGUT8g23BzL6U4J9uWiV3GQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
📊
🥶
کیلیان‌امباپه از زمان حضور در لالیگا به تمامی تیم‌های حاضر در این لیگ گلزنی کرده!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/Futball180TV/106763" target="_blank">📅 16:55 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106762">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/db11bb42ef.mp4?token=EDCfEv5pY9Xlt0tvjtbhbzMk8It3aHkXLE-NOGKEZds8OZ47pMoGdUT72vBj42uV3Acz7BmeoyXdBQdV4cYYw39aTI5bRFpFxcO5V4Y84DQxwfGfr1Iu7lbTKCymm5zp94WwUHNHaO2LXlxpuUdOK0CXFUKwCr4AM_463xXR4AGbic8z4nvgJBAP4DyIDQlEHANL-Gr5kbt6tpXhW2rJahXN-3VJeYmNBlRJixWultaM0SXdFavb0phgK5Zm9ZZNLw_25onheU0cV_jfJa0vqxKIM3Zve0mSbx33uonrccEi9llUWIhOSOUam0Np9dxJHERD-XofoNgIbebB4anMwyTDdz2dGRVs3CYM-ekUvHesxIk92DlzQnJiuT0Cg5q-cfBGGKUWWTKIHXvRdZuwwRdzazB_MO4-ufpImgg-G_XJLHz3aHJQcJdxyE9pjKLM_9SWCwm0hL50SbCXvdIuHheNu8bel1oocISCXvAHKnoamRi3ziuRrgQcbAY0gt1bKZdqdqjE-UeBAT6-i9Oar9GmzKolj2fOvJ6q5kV21nO3y-JBDJwH40dYEbBc8pEaG6tHkvn6d5aB_v_Py1jUAk8fZITfIb5Gjt61Bjqodu-KZdHrlvMJKr96eC_rhahk_bnzOKX6sG9JKk-CJL0DSPCllD8vJAjE0E_ccbhW2to" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/db11bb42ef.mp4?token=EDCfEv5pY9Xlt0tvjtbhbzMk8It3aHkXLE-NOGKEZds8OZ47pMoGdUT72vBj42uV3Acz7BmeoyXdBQdV4cYYw39aTI5bRFpFxcO5V4Y84DQxwfGfr1Iu7lbTKCymm5zp94WwUHNHaO2LXlxpuUdOK0CXFUKwCr4AM_463xXR4AGbic8z4nvgJBAP4DyIDQlEHANL-Gr5kbt6tpXhW2rJahXN-3VJeYmNBlRJixWultaM0SXdFavb0phgK5Zm9ZZNLw_25onheU0cV_jfJa0vqxKIM3Zve0mSbx33uonrccEi9llUWIhOSOUam0Np9dxJHERD-XofoNgIbebB4anMwyTDdz2dGRVs3CYM-ekUvHesxIk92DlzQnJiuT0Cg5q-cfBGGKUWWTKIHXvRdZuwwRdzazB_MO4-ufpImgg-G_XJLHz3aHJQcJdxyE9pjKLM_9SWCwm0hL50SbCXvdIuHheNu8bel1oocISCXvAHKnoamRi3ziuRrgQcbAY0gt1bKZdqdqjE-UeBAT6-i9Oar9GmzKolj2fOvJ6q5kV21nO3y-JBDJwH40dYEbBc8pEaG6tHkvn6d5aB_v_Py1jUAk8fZITfIb5Gjt61Bjqodu-KZdHrlvMJKr96eC_rhahk_bnzOKX6sG9JKk-CJL0DSPCllD8vJAjE0E_ccbhW2to" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
🎙
رست‌دیفنس در فوتبال از زبان رسول‌ مجیدی از معدود مجریان باسواد صداوسیما؛ خیلی جالب و شنیدنی برای عاشقان فوتبال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/Futball180TV/106762" target="_blank">📅 16:35 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106761">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🚨
⭕️
🇮🇷
🇮🇷
با اعلام کمیته انضباطی فدراسیون فوتبال، شکایت پرسپولیس از استقلال بابت یاسر‌آسانی رد شد. سرخپوشان پرونده را در CAS پیگیری خواهند کرد و به تیم‌های عربی نیز کمک حقوقی خواهند داد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/106761" target="_blank">📅 16:15 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106760">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/915324d20d.mp4?token=J9HikILXa3qw4XR43l3PpcpdZ2i99bxffnJHXZ5NIWsRhrPpmTPAoIC7RfRU2r_Png1iC2fUbS82C7VQPqtTHKV9-K-d2CLy6SRrmrBlPL28jwscvA0YqB22xPKy53oxlK8YkJcQXKt4nrsoxodcjGpZwKbso2f1butNHiyG_buq0uoOGyRTIqDRa3x2Vwq8cAH0hzFsU6F8kRaFe4JR8BCWcCuFprxlibCJ6Tda07kxtxevNul4f5jLwugmv55XQOgZfKnyLq4Vz4EX1xlDLeFOvslpMLIpJcb1j-aBQi9VhbC6RVlsD5LQMBKuabPJJOt0JXk3fx670YrhKEG9hbKYj700fPTptbg5PcGoAgnKec7xr3cN47yg8sVB7vWKZZtcRUx9-hNeBy0sxi1hGCtKkJXH0u7OzW-zoENniyQXOmn68TTHCz_s5NksY01e5HsNDIbMTmeW6uX7MpVNze2DQrds2-zJi9sxhbYJWUNDpPQeuj77Q6lbUGTQM_UxXltf-3MGIj-sA-rK-aNKFsw6lU-jpvieL6Sq32y1S-8rQaJITdXgx4p2OhJ6K_7LznS8K6PnLY2a0x_UDL3ipv0cay3qmCX10KhbPR4elhFBP19OZhn7tGvQoV2L9I5LP0Z-Luo3x4LLw_t4EMcO7LINvfsPfDthnjqsreGnoec" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/915324d20d.mp4?token=J9HikILXa3qw4XR43l3PpcpdZ2i99bxffnJHXZ5NIWsRhrPpmTPAoIC7RfRU2r_Png1iC2fUbS82C7VQPqtTHKV9-K-d2CLy6SRrmrBlPL28jwscvA0YqB22xPKy53oxlK8YkJcQXKt4nrsoxodcjGpZwKbso2f1butNHiyG_buq0uoOGyRTIqDRa3x2Vwq8cAH0hzFsU6F8kRaFe4JR8BCWcCuFprxlibCJ6Tda07kxtxevNul4f5jLwugmv55XQOgZfKnyLq4Vz4EX1xlDLeFOvslpMLIpJcb1j-aBQi9VhbC6RVlsD5LQMBKuabPJJOt0JXk3fx670YrhKEG9hbKYj700fPTptbg5PcGoAgnKec7xr3cN47yg8sVB7vWKZZtcRUx9-hNeBy0sxi1hGCtKkJXH0u7OzW-zoENniyQXOmn68TTHCz_s5NksY01e5HsNDIbMTmeW6uX7MpVNze2DQrds2-zJi9sxhbYJWUNDpPQeuj77Q6lbUGTQM_UxXltf-3MGIj-sA-rK-aNKFsw6lU-jpvieL6Sq32y1S-8rQaJITdXgx4p2OhJ6K_7LznS8K6PnLY2a0x_UDL3ipv0cay3qmCX10KhbPR4elhFBP19OZhn7tGvQoV2L9I5LP0Z-Luo3x4LLw_t4EMcO7LINvfsPfDthnjqsreGnoec" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
‼️
🏴󠁧󠁢󠁥󠁮󠁧󠁿
برخی از راکت‌های تماشایی سوبوسلای در لیورپول؛ واقعا عجب گل‌هایی زده!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/Futball180TV/106760" target="_blank">📅 16:05 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106759">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OhbZX5HqNTAWBJJGuh9VIp5Lio6dG2Z0yhfKkvcR9r-cxvOxxU8WakQihJZ5RHz9zGzxkIfd1__EdqtlIEoXTtugqGTpkdXlsq9khMtmxoB6dEH2gU1jpr_3FI4jkEBUtZiNr-0z6GQrjsZl576b_mXXbMnS5PhSEAqQl8Zu7rpRdmX7O0AsKzlsI9DCIZX4yTYhnqwxt_cveH0I7b2n4c_3XBfML9AtdXwK617l52-Ew5qC46dzAaYnpY0tRb4Wf7T9SMXKn5txefGSfJ9jhfGs-GkWcZ5-LtXkheJSDVwUosVVLVzNDnsO5dIQTNGeHd6m80uEcBWTCJ6cTLBCSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
💥
سال 2018 که فرانسه قهرمان جام جهانی شد، کل مردم فرانسه برای امباپه دعای خیر کردن و نتیجه دعاهاشون شد این بانو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/Futball180TV/106759" target="_blank">📅 15:40 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106758">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0ab14c70f7.mp4?token=N6Ej57aYt9P55jzygKTg6166W5dBOyZRGKaQ9H9YFmUpcCYvITyC13WCDG-rOTmGWCyIO_z9TsYZ6w7SRG_QeUkx1Cjq64GzxOCxAasg6t5FrJQ7HzD2jNmZn2rI_1gWCWXIk6zQ4_PX4rrctmn36-oNrahmkLxqUeSIcTC6dlNY-28nZ1UEVhRdjnats-u2jklnnowZ-6Be3yJf7eL-AjKQF2GFDn0DtWpUBPD0mEosRF-g7vautXlnTsoDvVVL-qY8TtkKqNN_0UDLYOB0gIXahlkyPkIPO8sJ_nSvDKXMMU9S6SumDbNG0wW1T6HTpTSE2cVMFUKrXL_mYJpetr6M3jpEKPs7KibKrIjr-ihj-h11yqKIiQc5Iq08IU1hvAo1vG3-eU5pqhz6ySs4oqlZdLv0IJXVT6lHpslT7Fcn43DoCcuwndc2SV55afGob7m-CgUYZHzyKe8qfEr-JgdFUsAhEecAfUKBzbvGRnFxCf1xgIcisfny9FIe65sZES2I2J7aMeMAi8hXH95EdBIXi5Iaq9BF_v0q1FGxUt4zTgs0LmK735UvW-kEKAEOLeN2PVBGBEoULeYUVNYNFEITPDL-EQlI9VLVaVPBV2NTPNiHT2SrJBw9DIgNthCowvv8ikSd5PSw3oy3epofgc3VJKCE7-xmOPt8CyXWti8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0ab14c70f7.mp4?token=N6Ej57aYt9P55jzygKTg6166W5dBOyZRGKaQ9H9YFmUpcCYvITyC13WCDG-rOTmGWCyIO_z9TsYZ6w7SRG_QeUkx1Cjq64GzxOCxAasg6t5FrJQ7HzD2jNmZn2rI_1gWCWXIk6zQ4_PX4rrctmn36-oNrahmkLxqUeSIcTC6dlNY-28nZ1UEVhRdjnats-u2jklnnowZ-6Be3yJf7eL-AjKQF2GFDn0DtWpUBPD0mEosRF-g7vautXlnTsoDvVVL-qY8TtkKqNN_0UDLYOB0gIXahlkyPkIPO8sJ_nSvDKXMMU9S6SumDbNG0wW1T6HTpTSE2cVMFUKrXL_mYJpetr6M3jpEKPs7KibKrIjr-ihj-h11yqKIiQc5Iq08IU1hvAo1vG3-eU5pqhz6ySs4oqlZdLv0IJXVT6lHpslT7Fcn43DoCcuwndc2SV55afGob7m-CgUYZHzyKe8qfEr-JgdFUsAhEecAfUKBzbvGRnFxCf1xgIcisfny9FIe65sZES2I2J7aMeMAi8hXH95EdBIXi5Iaq9BF_v0q1FGxUt4zTgs0LmK735UvW-kEKAEOLeN2PVBGBEoULeYUVNYNFEITPDL-EQlI9VLVaVPBV2NTPNiHT2SrJBw9DIgNthCowvv8ikSd5PSw3oy3epofgc3VJKCE7-xmOPt8CyXWti8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🚀
🏴󠁧󠁢󠁥󠁮󠁧󠁿
سوپر گل پریشب سوبوسلای به تاتنهام رو از این زاویه باشگاه لیورپول ببینید
🤌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/Futball180TV/106758" target="_blank">📅 15:15 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106757">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fDOjOKcifh-44DyRtG8XDn3ZDHFgHXgRLoWil7c_Vmg20VaDwilAqi3hwLL4FyHdL_tkgYfcxlpVqtydrACXQ-7fkumfbk_xAgQoaB0cTJSz0EwoQixPXeY_vVAtVqK7MFbaHbVd5J26dyPPr72XRUNwR6mF1Tklyh4IB-fsNbjg2f6Wjv0LAAd17CMXL40JurnKajh-5VGlnCE1dcS2OLZ_qHE0Oc8GQceTrJ7BUHLd7u276YkCqL4xrPbXtfUIJFONfyJVQtKgSbrrYW7dQLFbQjJ8gBZb4gAtCqyN3kJi6PZm6w4Uj_gdItHdVc-LYj7wlHnThArmBm61AkOdzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
✔️
🎙
کیلیان امباپه: "جایزه توپ طلایی؟
به نظر من، امسال زمان مناسبی برای من است تا این جایزه را ببرم.
بهترین کسی که از من دفاع می‌کند، پای من است.
هر چه که بگویم، مهم‌ترین چیز برای من این است که توپ طلایی دوباره به رئال مادرید برگردد. باید به سانتیاگو برنابئو، به هواداران مادرید، بازگردد تا شادی را به قلب همه آنها بازگرداند.
آنها بیشتر از هر کس دیگری، شایسته این هستند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/106757" target="_blank">📅 14:58 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106756">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/758a2aee2e.mp4?token=RWL_hnpdyUtfaD1sFeJZu6AdXbwXhYpadeVV8yIKi5KFrXdtLWT7sYv-xjsqy1g4kvs-7LH7rz6-fT7KEFHPP_p6BGjAFxm_JQrK7EWff4cKEhTWNud01VaPlkW7F-7z9E3H2bHuYtIyJnJ_2Ga1m6yZpvY3L65-OSazGXKj8of50DzvL-CqNBzUkpQUWbvtZM6VzIrvg8E47XGk0MuH-acWT8heJOILDDUMd01ZaeirVcx9TgHcdD9tSf_B4dUOCVd72jNyvrPgYbgJD7txf9eop81exiz-0wHVHcgr1GTfj2pr97rPlldgiu3jMRbUqAAZmkW2VZB7--QbpRXo_g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/758a2aee2e.mp4?token=RWL_hnpdyUtfaD1sFeJZu6AdXbwXhYpadeVV8yIKi5KFrXdtLWT7sYv-xjsqy1g4kvs-7LH7rz6-fT7KEFHPP_p6BGjAFxm_JQrK7EWff4cKEhTWNud01VaPlkW7F-7z9E3H2bHuYtIyJnJ_2Ga1m6yZpvY3L65-OSazGXKj8of50DzvL-CqNBzUkpQUWbvtZM6VzIrvg8E47XGk0MuH-acWT8heJOILDDUMd01ZaeirVcx9TgHcdD9tSf_B4dUOCVd72jNyvrPgYbgJD7txf9eop81exiz-0wHVHcgr1GTfj2pr97rPlldgiu3jMRbUqAAZmkW2VZB7--QbpRXo_g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📱
🇮🇷
🇮🇷
مقایسه فالوورهای ده ستاره سرخابی‌ها
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/Futball180TV/106756" target="_blank">📅 14:04 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106755">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LXXxMXg_C0Ras8wK8X_hO019N85QDx9vdaDxCC_DWn3mmj7I-dQl7zukcif7fDpVAgd3xlYFLUbqwY8Sy-NeDONl18lRcOlqVh8e4kFY8yx1paw5ku8YUdUtM6581Zea7Tk6eSARUnCSEQk9a_MnlcQ84E_otVcu_Uo8783OXwQfLTj3rIShXyUh1mSz4uXbNTX2hPNLcvoI2BXIH-Hrs0rZj7P1ltOg71WjM3YlNdyGEtJKxbe-SncVNOs_ST4V7R8-MISGsfofBEOhwqpn0Sasg5duRPmwgYaJ_YGqtc19jp_mKWTZS-KRARPG5Eu2RwQ3Eq7ouCeupgOZQsL8nA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
✔️
🇮🇷
شبنم‌علیخانی کاپیتان تیم‌ملی والیبال بانوان ایران به تیم استقلال پیوست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/Futball180TV/106755" target="_blank">📅 13:49 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106754">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/edd80b92b5.mp4?token=da5-3TaTlWRK4hsj5lrjE8c6f1f9-E13xBz-GzSD09UjcnSBt_w-Dm_Tug0I3UTtRFeuXulCFqUmNYW79JcuHrWH-xCZJysVoLHnkO1CvvgqT4c4eNe4J1BZgKGv_3jNeDijEY1avqnxWlXkV-UDNh15vGEWBAR5Hev1-hGKQUljLWDwAmnXDlc2AigQyjHjLomHZF5WTWWSIt34l7bmj3rJ1YuTXxwxL-AF2b1BSb1xZHBHP9CHP8KY4LJcrOPNUvAFqzVFUjk-VA_5NIOFqQI-5ndTOIWmFnG0R_qf_Yfybt2zNU4O0Zoig8Xr7v30yqS7uws9U_fUJDwuwXMoMw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/edd80b92b5.mp4?token=da5-3TaTlWRK4hsj5lrjE8c6f1f9-E13xBz-GzSD09UjcnSBt_w-Dm_Tug0I3UTtRFeuXulCFqUmNYW79JcuHrWH-xCZJysVoLHnkO1CvvgqT4c4eNe4J1BZgKGv_3jNeDijEY1avqnxWlXkV-UDNh15vGEWBAR5Hev1-hGKQUljLWDwAmnXDlc2AigQyjHjLomHZF5WTWWSIt34l7bmj3rJ1YuTXxwxL-AF2b1BSb1xZHBHP9CHP8KY4LJcrOPNUvAFqzVFUjk-VA_5NIOFqQI-5ndTOIWmFnG0R_qf_Yfybt2zNU4O0Zoig8Xr7v30yqS7uws9U_fUJDwuwXMoMw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⚠️
حرکات عجیب مجری شبکه‌سه برای توضیح عملی دفع سنگ‌کلیه در برنامه زنده!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/Futball180TV/106754" target="_blank">📅 13:35 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106753">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2975c02c1e.mp4?token=E2wxbtgzqQeLyFZtoESGC1LsopLVkh0IpXRJqki5nDU__gsSIjZ4QZzRPW7sGZBK9rdeBJWtvCME3BzLzaZ5uvrUi4h2yIVkrQ1qvFNEOhsflZlFqWsvDi7HxqzecK5eor3FtwDMOQobxHJktUM-AnAWKzFI23ed9vz7CqnxPNoAY4kYYseOFDYO8OaordUeHEM08nb4VtM-xfQZA4HsziYWWGDriWM4-qDYMdwydjB65YisKWnQ03HAFGwe7ZIzwvAbczSHjoE8OmZNqdsJY1zZjmSyrEnBebBVCJm32HrVDpVymkm-6AtgiO-PN37QCZIDKz2ev57fEgn5TYLrfw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2975c02c1e.mp4?token=E2wxbtgzqQeLyFZtoESGC1LsopLVkh0IpXRJqki5nDU__gsSIjZ4QZzRPW7sGZBK9rdeBJWtvCME3BzLzaZ5uvrUi4h2yIVkrQ1qvFNEOhsflZlFqWsvDi7HxqzecK5eor3FtwDMOQobxHJktUM-AnAWKzFI23ed9vz7CqnxPNoAY4kYYseOFDYO8OaordUeHEM08nb4VtM-xfQZA4HsziYWWGDriWM4-qDYMdwydjB65YisKWnQ03HAFGwe7ZIzwvAbczSHjoE8OmZNqdsJY1zZjmSyrEnBebBVCJm32HrVDpVymkm-6AtgiO-PN37QCZIDKz2ev57fEgn5TYLrfw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⁉️
▶️
✅
بهترین مکمل برای جایگزین کردن قهوه قبل از تمرین چیه؟ به روایت استاد هانی‌رامبد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/Futball180TV/106753" target="_blank">📅 13:10 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106752">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vXFfdDubEHUVSwPJ8vHQsmwO50OUV6CZviEJLAAVO82qNcLZ-AhpkPvLY_stKaomtR5txulid_0EQ-cX0WRQqRq7s4ruXMv6LAG3G0uvEg9r73hRK3BrprGM_sYviHF2CHOFEC_2HkrtOU9KwBPTjK6N-iZZrjltR2Rwg_tgJ_wYZGU_nrsYg5qEsCJPJydgLy8kiiBu5PjpoUOI2GtJJlkNP9UHjmlrnv9ZjZ224BE00qPKWapCz7wF9gySFE62BxQ9S8IOH7iV_uNq93Wfk5lIproi_prm3wnv25ptYnHQL9DobUTd94nPOXBZkjZ5HXjoKJZt6NDVvgWcBUV9FA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⭕️
🇮🇷
🇮🇷
با اعلام کمیته انضباطی فدراسیون فوتبال، شکایت پرسپولیس از استقلال بابت یاسر‌آسانی رد شد. سرخپوشان پرونده را در CAS پیگیری خواهند کرد و به تیم‌های عربی نیز کمک حقوقی خواهند داد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/Futball180TV/106752" target="_blank">📅 13:04 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106751">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pyKkgXoSj2UbBNgVQSMV-AaaKOqGt9uFlVLqSzmU2s_oois7SWI0GJdxslAjl3rbJ8Qt5agJMnvzTRr_jbLJCx_nrSfykAbh1ULy5M0o-de8kfKIfrp-WBpGCGNK_LMbNycjfAjgwuRNZPcZVQN16EDbGI4SgoccjG1lPkUmqnmHzyET6HS80e-DAVDhU1Y__3Q1tkABDCClBpnr-5_59otNTpOWethbFciTHqMgrEO6FhpvGGWIP2XeiKRIQ_E-QWx9FoE_dWGCwAP46qUa87gs9hzKh6S_vX8vI6jtrtBl6__n7lrWYGt57XcyEaas4KyOaRs72f_FAcswpJHHMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⭕️
🇮🇷
🇮🇷
با اعلام کمیته انضباطی فدراسیون فوتبال، شکایت پرسپولیس از استقلال بابت یاسر‌آسانی رد شد. سرخپوشان پرونده را در CAS پیگیری خواهند کرد و به تیم‌های عربی نیز کمک حقوقی خواهند داد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/Futball180TV/106751" target="_blank">📅 12:52 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106750">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vE9D5j_oJcRVyfa1QzavhUXr3pwbf99EVRYXFF1dubfoRpAqD9LdOH2TnjldVanFeViy3MBG3JNbeKoR-iXUaBgRxlVPZ6L83Uo1Y2eNRcJ97WOwUOvSDYLBCDzocDnZz51uz5FtqnAyPSlnnjCJFqImbrit0NYVuBg1k4GrFjyFLJtIzr-WgobtjB_8GZf6s0p58Tf7HJvOz-McGGoG-RqtX26KO4wRGeHd32seozUhWIpHi_yR_v_kAJLtMGDdRP_yhCaexPBpz7PGhpSF7g393SLwmaDazILKyCfH1P28bYTWeDmUbU4F0JsLEo0xa3nW4ZCz8gCgedW9NG9Jwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
🫣
بالاخره روز پسر شد
😁
👍
‏در تقویم هخامنشی روز ۲۶ شهریور روز تولد کمبوجیه پسر كوروش بزرگ می باشد و این روز را در ایران روز پسر نامیدند. برای پسران عزیز زندگیتون بفرستید که حداقل تو این وضعیت کمی خوشحال بشن.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/Futball180TV/106750" target="_blank">📅 12:45 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106749">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WUM_sZesHwnsNB4AIYIzuiNYP0VM5tfXEU0fYEVKjnSaeJqSsJQ-R3TYj8MPY5zj6IGRMskdiK6i955LUkcXEnDfr-ZHNdTIiy9hRApiSUwSMJ8rQhx-96M1m4PqQls36TKBrzCLThMCx0oO-dhOkZZ1tS3h1qqVIVLcPoGe0f2H3Yj6hPY-HsLSRs03IX0rBEjbZX7wHoXujEUTM3bVQ0yyw1VVPwRALBy-4zTuULJrp8wV1WsQ5ho0LsSV3U0bhnUToWGNT5UdCnYLxKN2khB08YHmGOwh_vLQGdRjNr8Grz-crKEOR2OAnKdQHe1sN1mn-ZcAd332cC6iNgL2KA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
💵
🏴󠁧󠁢󠁥󠁮󠁧󠁿
بهداد اقبالی میلیاردر ایرانی به طور کامل سهام باشگاه چلسی انگلیس رو خرید و الان تیم کامل برای این آدمه!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/Futball180TV/106749" target="_blank">📅 12:37 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106748">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🎙
🐐
🟣
دیوید بکام بعد قهرمانی دیشب تیمش:
🔺
هنوز باورم نمی‌شه مسی اینجاست و برای اینتر میامی بازی می‌کنه؛ برای همین هر وقت بتونم می‌رم سر تمرین تا ببینمش. به نظر من، با وجود بازیکنای بزرگی مثل هری کین، کیلیان امباپه، جود بلینگام و سایر نامزدهای توپ طلا، مسی باید این جایزه رو ببره.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/Futball180TV/106748" target="_blank">📅 12:20 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106747">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bb69509038.mp4?token=e8puQ34Sy_lWLp_RX5gua4Baqpi2_XztYjgdLU-8_cGv-8aPS9myGM44qjLfMKetilv15uKWphPDgUVe2Mb6LwOmax_Y1PFuiLhLQSaQs2KFNkdVcghp_mj-vIIn2IXql6XNpRVvtcKjwxqZj0GFdoX_gMBsOz8ePzZmTAW7_DE_34Ux4P3FqftvtuJtsbU4V-cekrCmhfUFvpaGqexL8luiMVXy7U5kYeghLOyUym1bcJPo8rnRbs60LQ9aL2TolItpN9wTlV8vxmV0UGIlSv9B1k0D_oYdgtKlqD1ogwzIPG6zdvJ6ji9-KwWw-04N8QKSny8kcGV8LHYg9TBMmxuwZ0S0gn31UikiEX2SKQNHUkTF8P2vL4xrRsWp6_B6gLxbBAx4twlD0sSF2Jg_1BrlyMReTXlN4lSCns_1ubmO97CcGh6E4eXDxfYbyXLoA9hdPMjHM96bS2OIVot6tKUj8KG3bxNG2ZzcVyxCEoLr8e1ReQubriJ7TuikqcjkuWdnpQ-V3C6rXdq-_843s8p5iem94Pb8SrDOH3Hn97bUVH55WMpsTD2Oithd9zCnF6THg0-qyhkuHXHVdUWgcbds-ui8ZYvcDfIZN7njhWJ-mFjnfGHAtp_gaH4-eAozi-0_bx71TNLofTi9aGU1NCasOVqVFwXlvVbHelQQDHA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bb69509038.mp4?token=e8puQ34Sy_lWLp_RX5gua4Baqpi2_XztYjgdLU-8_cGv-8aPS9myGM44qjLfMKetilv15uKWphPDgUVe2Mb6LwOmax_Y1PFuiLhLQSaQs2KFNkdVcghp_mj-vIIn2IXql6XNpRVvtcKjwxqZj0GFdoX_gMBsOz8ePzZmTAW7_DE_34Ux4P3FqftvtuJtsbU4V-cekrCmhfUFvpaGqexL8luiMVXy7U5kYeghLOyUym1bcJPo8rnRbs60LQ9aL2TolItpN9wTlV8vxmV0UGIlSv9B1k0D_oYdgtKlqD1ogwzIPG6zdvJ6ji9-KwWw-04N8QKSny8kcGV8LHYg9TBMmxuwZ0S0gn31UikiEX2SKQNHUkTF8P2vL4xrRsWp6_B6gLxbBAx4twlD0sSF2Jg_1BrlyMReTXlN4lSCns_1ubmO97CcGh6E4eXDxfYbyXLoA9hdPMjHM96bS2OIVot6tKUj8KG3bxNG2ZzcVyxCEoLr8e1ReQubriJ7TuikqcjkuWdnpQ-V3C6rXdq-_843s8p5iem94Pb8SrDOH3Hn97bUVH55WMpsTD2Oithd9zCnF6THg0-qyhkuHXHVdUWgcbds-ui8ZYvcDfIZN7njhWJ-mFjnfGHAtp_gaH4-eAozi-0_bx71TNLofTi9aGU1NCasOVqVFwXlvVbHelQQDHA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇪🇸
وضعیت دیشب نیوکمپ که هروقت بارندگی بشه اینجوری استادیوم به گوه‌خوردن میفته
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/Futball180TV/106747" target="_blank">📅 11:55 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106746">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🚨
✔️
اعلام فهرست بازیکنان لیگ برتری تیم ملی
🔵
علیرضا بیرانوند، سیدحسین حسینی، پیام نیازمند، محمد نادری، احسان حاج‌صفی، شجاع خلیل‌زاده، محمد مهدی زارع، عارف آقاسی، سامان فلاح، صالح حردانی، رامین رضاییان، آریا یوسفی، میلاد سورگی، عارف حاجی‌عیدی، امید نورافکن،…</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/Futball180TV/106746" target="_blank">📅 11:29 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106745">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jtRB_b90W_nUqZ6TTjyuMvnXVT_xFlspRmKoNDdcws4B62TqBQu7TocjgC23oOfSw5SwmrN4foaiGHieXetXcK_RdRRPUthbF61JXYvXW-LZ8JoamWHK3Oo0X7WlXnusIPaNCx6vl_qb3L3OlRqZL4IBMC2Rta61NcY4VDB29Wf2HOHCW_y55-_6xrINxGqwrIsFda6kB15D7fLw3qDWrrGnlcMQO-IaS_wXxSwW3YAeitlhhJ01BkCabhJoctbooDQXgOGjbY-zGSwiEOaQdnlT9OuxmJ1z4Br_nQkl8gVwmmQObRTHe6AMtFMlRs5aybXoBHPBuEVUkIEXPUaokg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
✔️
اعلام فهرست بازیکنان لیگ برتری تیم ملی
🔵
علیرضا بیرانوند، سیدحسین حسینی، پیام نیازمند، محمد نادری، احسان حاج‌صفی، شجاع خلیل‌زاده، محمد مهدی زارع، عارف آقاسی، سامان فلاح، صالح حردانی، رامین رضاییان، آریا یوسفی، میلاد سورگی، عارف حاجی‌عیدی، امید نورافکن، مهدی لیموچی، مهدی محبی و امیرحسین محمودی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/106745" target="_blank">📅 11:27 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106744">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5b540a014a.mp4?token=vjru5yLFXBi6T5B65pLPelIrYnn3Qfd9Lsu05wofXl2TsrlfQMDJ2USv6YsVPKeYyzRzuECVRk3opyqedoHyXxz54QP8dCRYf5dKrzuqF28cW9IFg_oKUfxC5B5HAC-6rvAlkcqLAFQ1Plr9Ejyyl2AylrUv4HKzx4FlKnETfeDt572YQ14WxdErxMfCFxzf2ME9SFrtEZzcW0tp92iuGoYIgxCAnzDSeuF25qXC6SHohZCDU_39p0YlKUtbHirpW_UGEEVCBI3nu4309cbZYN0bEUQsSi40Yhkg5gU-rFt1ZK80SDGVJGGpxY_vy9v-BuVGCA8743baXMoE2UPAwK6iB-Pl4liiEU4WqjIPh0VcyOB2TH1tOIifGv107dltPe9Z1abx1nA2j2CH_CIRgfoEg_5E_m2Tf58Ef8hnq9jg_XqXfj-cdBAMpSoMfa66l7nsEc3OZCuQV_BOgn2m0t4dPtNNW2PD2na5HdlpRBdnxP6sFw0FLpTAmI9ruLw1vO0ffDKGR5PtVhDyYRfFr7cR2ut2nIEtDMIrolNyviAXfqgRnus-tYjkdyAiYgbeCP_t6K1O10GzFWoIPz9ajY3HMCk6P9kEjG8tKEh3oCUm3A2RjPiYcJUD9GIROUs00ICRSCaFl_xTNvv-mXEnSA1q7qopMIbihObJZDJwcZM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5b540a014a.mp4?token=vjru5yLFXBi6T5B65pLPelIrYnn3Qfd9Lsu05wofXl2TsrlfQMDJ2USv6YsVPKeYyzRzuECVRk3opyqedoHyXxz54QP8dCRYf5dKrzuqF28cW9IFg_oKUfxC5B5HAC-6rvAlkcqLAFQ1Plr9Ejyyl2AylrUv4HKzx4FlKnETfeDt572YQ14WxdErxMfCFxzf2ME9SFrtEZzcW0tp92iuGoYIgxCAnzDSeuF25qXC6SHohZCDU_39p0YlKUtbHirpW_UGEEVCBI3nu4309cbZYN0bEUQsSi40Yhkg5gU-rFt1ZK80SDGVJGGpxY_vy9v-BuVGCA8743baXMoE2UPAwK6iB-Pl4liiEU4WqjIPh0VcyOB2TH1tOIifGv107dltPe9Z1abx1nA2j2CH_CIRgfoEg_5E_m2Tf58Ef8hnq9jg_XqXfj-cdBAMpSoMfa66l7nsEc3OZCuQV_BOgn2m0t4dPtNNW2PD2na5HdlpRBdnxP6sFw0FLpTAmI9ruLw1vO0ffDKGR5PtVhDyYRfFr7cR2ut2nIEtDMIrolNyviAXfqgRnus-tYjkdyAiYgbeCP_t6K1O10GzFWoIPz9ajY3HMCk6P9kEjG8tKEh3oCUm3A2RjPiYcJUD9GIROUs00ICRSCaFl_xTNvv-mXEnSA1q7qopMIbihObJZDJwcZM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🇪🇸
آنچه در بازی دیشب بارسلونا رخ داد:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/Futball180TV/106744" target="_blank">📅 11:05 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106743">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z60F07XAw1_5LiO8WdyGmS-JZ-ajNtCVphq6ObYotjcmWmjKgV1mjmNLRhu94LMtMuWcWGcnM9R2hvOugA-SwM3V37WsRNQwLD7t-v138ZkkW9PlaqJlwOUk4H1vgiLls9dhBra2jk4HUgJgWIlkVBnSZlmo0pgAIOqIlhEnwHua6TEWENDPCAmI7dqxU3VkM27_ebOqLRdhq9nyeK0Fz0QkxfWRNXvHFl_FY7YJCQ9Z4YGdITi7NgmbCXsTw07UVPUWhnXb699mctfWbNsMSZOrB_4OCMc2ec1XTXWxoNCGgTfMv9KzOVy-hzRnwMTW9byuQB_iRuZFkjKbrBMBnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
📱
علی‌ضیا هم رسما با انتشار این عکس اعلام کرد که زید زده و دیگه سینگل و این‌چیزا نیست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/Futball180TV/106743" target="_blank">📅 11:00 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106742">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/Futball180TV/106742" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/106742" target="_blank">📅 11:00 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106741">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I35UTFdcbjdAJZJp9BCJMczxYuGBku9bLo6vpeQmtXzo4eU1pnIgnC96mIsCDIYJ5019x5ZjdSgO6nFvR-gmBW7OgikyzQjca8Uf5PqubF-sgD47IyF6RCU0_x5SNbz6faOaNUIiXWwEp2J-0xVxUqSJAVoPXMRwSs-o2FCYRfQAk8w-fE1i-5GWjuygmEuAIVeRHRm_144ncmZ-y4dk1wt9hua4NUaJxukKFF25y_VFsCLb4l5Juqrn5Z6OHVi2hMVVniki9LuoMGXctZhDXxOVHQ5LT4MJ4rYI8b6WKeiufzEu157ZyFGgIzzotYvoGXpVh13llYYm-EtZ53DjZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
مچ‌های مهم امروز در سایت بین‌المللی
TrexBet
ان‌ئی‌سی نیمیخن
🆚
یونتوس
نوریچ
🆚
منچستر سیتی
🦖
🦖
🦖
🦖
🦖
بونوس اولین واریز تا سقف ۱۰۰ یورو
🦖
بهترین ضرایب بین تمام سایت‌ها
🦖
واریز آسان و امن از طریق کارت به کارت
انتخابت رو انجام بده و آماده‌ی هیجان باش!
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/Futball180TV/106741" target="_blank">📅 11:00 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106740">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ee3ee373ec.mp4?token=kyeGZ-k70JeG4JfTwRCU27Qh4ifPiC9y5HRtC7SHKJ7dB5U-DjC7c5HEoE9Pg4ciGIa1A10Onq9zFoIfq-7MIE7AaNOIRlMTuszS-9uNd7tkBNeqYIv8rNmPHNh10fPlPYTWEY9PlOaLG6vGJtfJmllkaABqS5d4qdajpYYGtY0Xh43RIDB50yN901NvLaK7Uq8Y7NkllLtD9J8MMDr468wjpC14Nvv7y1YVkCYG7ybyFfaVmEcFPtruQgQr6f13ax6QPOvbAYr8eCRs-uh9tbiy0WCpfUtKZlX-LJbyuxwMeYWIPF7jLD_XzUGMdOqe69XNlb-x-TAvTxqZak8ccw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ee3ee373ec.mp4?token=kyeGZ-k70JeG4JfTwRCU27Qh4ifPiC9y5HRtC7SHKJ7dB5U-DjC7c5HEoE9Pg4ciGIa1A10Onq9zFoIfq-7MIE7AaNOIRlMTuszS-9uNd7tkBNeqYIv8rNmPHNh10fPlPYTWEY9PlOaLG6vGJtfJmllkaABqS5d4qdajpYYGtY0Xh43RIDB50yN901NvLaK7Uq8Y7NkllLtD9J8MMDr468wjpC14Nvv7y1YVkCYG7ybyFfaVmEcFPtruQgQr6f13ax6QPOvbAYr8eCRs-uh9tbiy0WCpfUtKZlX-LJbyuxwMeYWIPF7jLD_XzUGMdOqe69XNlb-x-TAvTxqZak8ccw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
⚠️
از عجایب فوتبال ایران؛ دیروز حین بازی تیم بعثت کرمانشاه و نفت‌وگاز گچساران یه نفر درب اتاق داوران رو شکسته و تمام وسایل قیمتی تیم داوری رو دزدیده
😐
😐
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/Futball180TV/106740" target="_blank">📅 10:40 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106739">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bebaf856a1.mp4?token=b2_2E0TGoFOuu_yXh-BBajVLRV_-xYgPohg5JZTBeBwLonjqNei01-k9OKKqoJJGlZcL42eVhOayY4egmbDggyMgE3C1NfLSzPp2mql0vc4nEPfHGKtpsg6d_bd5lHGCGaK1mpry46r2p4IpY103tMokAkibVCYMti4a5KqDRq76bSqf57TxOTJegwKU2D19SI-tWGBAgCtjnEIIC8hHYelNs7T_Ec-Im8PV9yrlISU5rhbbPYdAtXpJwpCNFG2z3dMY7bPJa8kM-OVkv4MiwcypH5h0seKzNzyg4kPtJnXE2Pb4KAkl-sAoSBhJ8pAWTFH0VDELrjf25xkFCoxcJw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bebaf856a1.mp4?token=b2_2E0TGoFOuu_yXh-BBajVLRV_-xYgPohg5JZTBeBwLonjqNei01-k9OKKqoJJGlZcL42eVhOayY4egmbDggyMgE3C1NfLSzPp2mql0vc4nEPfHGKtpsg6d_bd5lHGCGaK1mpry46r2p4IpY103tMokAkibVCYMti4a5KqDRq76bSqf57TxOTJegwKU2D19SI-tWGBAgCtjnEIIC8hHYelNs7T_Ec-Im8PV9yrlISU5rhbbPYdAtXpJwpCNFG2z3dMY7bPJa8kM-OVkv4MiwcypH5h0seKzNzyg4kPtJnXE2Pb4KAkl-sAoSBhJ8pAWTFH0VDELrjf25xkFCoxcJw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
🇪🇸
🙂
آرزوی هوادارای رئال مادرید:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/106739" target="_blank">📅 10:15 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106738">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">‼️
⚠️
خودکشی سرباز روس با استفاده از نارنجک پس از زخمی شدن توسط کواد اوکراینی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/Futball180TV/106738" target="_blank">📅 09:51 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106737">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/704ad943ef.mp4?token=h8mbvRh4MF-3uE1Jcxzg9AP5Ifr_XtZgcQRkLlIbsLLc3zKg4r25js6npiECSjg4frmpjxYDz0SSHBfJBrUD_4FTCzx4MwH768R-0uR1YFBg58BRkXiuIjrPXFLTbI9ERX2ZcOGYUqdl5SBlRe72cUmxyeMGX9jCYruvo6Ih9ai6yNt0UznSjfa39JdyuA-QLi9DFCSXfVWFXIF4kjWtR1HAGOe5eh6WfYBqRqPUqflwI0jc5GS7RkYfwoG1QYj_yySKjqTDezKFnwJjqjzApz88kVn3UtEO9nL42zG9b8i94y_3-ZvZf4EBHYBgH3DE_kWRT0HHT9U0vM9Aq17SAw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/704ad943ef.mp4?token=h8mbvRh4MF-3uE1Jcxzg9AP5Ifr_XtZgcQRkLlIbsLLc3zKg4r25js6npiECSjg4frmpjxYDz0SSHBfJBrUD_4FTCzx4MwH768R-0uR1YFBg58BRkXiuIjrPXFLTbI9ERX2ZcOGYUqdl5SBlRe72cUmxyeMGX9jCYruvo6Ih9ai6yNt0UznSjfa39JdyuA-QLi9DFCSXfVWFXIF4kjWtR1HAGOe5eh6WfYBqRqPUqflwI0jc5GS7RkYfwoG1QYj_yySKjqTDezKFnwJjqjzApz88kVn3UtEO9nL42zG9b8i94y_3-ZvZf4EBHYBgH3DE_kWRT0HHT9U0vM9Aq17SAw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😆
کادو ولنتاین سمی مسعود شصتچی برا زیدش
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/Futball180TV/106737" target="_blank">📅 09:25 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106736">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/546d8bc40e.mp4?token=C0FZzcnl84RFYTerwC1Y6K7Ceohd_kURRZtkP3_chi4m1zipoD1Sa_mDatK2UfTpRLSjGUVPjbCTflJtI6mRNFjAw2SJZ4i9Z_PReLCOC38SJD7foNuxIt3yWn4cx0Ky-lvSbRerV4EOrnRO8m6fQljsc0SP-HF6P9oXWKSySPt8KLhakybCFr4EhZzASGrroskQuEqgk0NWZNFts1Gg9HvdipsxmZgElcuzyVP5k9dzc3si-nE1dqCnrf-kRoeA0ElpWlJmOYHR_SdslSE_vZymwRkdzv7tA0kXz9DC5i7MW1hH3tCbW0BRfi_0UsFu26XqhezGM1yLnTScau86Xw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/546d8bc40e.mp4?token=C0FZzcnl84RFYTerwC1Y6K7Ceohd_kURRZtkP3_chi4m1zipoD1Sa_mDatK2UfTpRLSjGUVPjbCTflJtI6mRNFjAw2SJZ4i9Z_PReLCOC38SJD7foNuxIt3yWn4cx0Ky-lvSbRerV4EOrnRO8m6fQljsc0SP-HF6P9oXWKSySPt8KLhakybCFr4EhZzASGrroskQuEqgk0NWZNFts1Gg9HvdipsxmZgElcuzyVP5k9dzc3si-nE1dqCnrf-kRoeA0ElpWlJmOYHR_SdslSE_vZymwRkdzv7tA0kXz9DC5i7MW1hH3tCbW0BRfi_0UsFu26XqhezGM1yLnTScau86Xw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
▶️
یه زمانی نوکیا به تمام ایده‌های ممکن ساخت مدل جدید، نه نمی‌ گفت!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/Futball180TV/106736" target="_blank">📅 09:03 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106735">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eYGoQP_4nHcaccFVJ81N-sgrN33l4cs50eUmt9EnKo1HJgfBeGYSU39DtjoKP2poyott5nDduARsgQtJBVA0rF12GL2h1pgmUzn16fZXBYacA7WtZe-bNrHIj3iZPYp6WdcGTid2qcozbUByNvSl25OWH0TdpaMGWKUu59vp8OYCFpNsrhU9oS0ug-UsmKcsFP2ie_CjJHD8JQQ6H1778OkDO0HXdsmbFtSavpGZloLFOG6OPngYXf1TdrkE3g9ZdQsctM2N_Aex5K16Z5dHshckVm4AeWO0gV0BgI_Po46VBz2PHPZaNA0m_24V9D3-ZD1l2TzhuoImAwJULWabKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🟣
🐐
با قهرمانی بامداد امروز‌ در جام قهرمانان آمریکا، لیونل‌مسی به ۴۹‌مین قهرمان تاریخ فوتبال خودش دست‌یافت و رکورد خود را بهبود بخشید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/Futball180TV/106735" target="_blank">📅 08:04 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106734">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">😶
🚨
🚨
این کانال باعث ورشکستگی خیلی از سایتای بت شده و پلیس FBI برای دستگیری ادمینای این چنل جایزه تعیین کرده
🔥
https://t.me/+bDapVmvigDhmYzZk https://t.me/+bDapVmvigDhmYzZk</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/Futball180TV/106734" target="_blank">📅 01:37 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106733">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/DOedqnfpCpVc_aBMl7nA7TcSa-Y5EoOG-0m8AO4ty9qTjCpLUeFaNXGwrGMNHWfUKVhLdDdhEJWRI3_EIhQbRTQoT56wR7VjypnO5GPqBxTE4yYZrc6rLpmgfhv_NfHdGwitwpvT9wYpklmO0q7rHYzWZeOYI82z2mw0c8Y0TlUCYLNHR1c9vXjyBAo7QcoaFNe-j39_mvGtpkQC2F1OWT9TLA4hGD3D6p9ZUmZUscbMTzPTJS0gaZoxFOxGoO-60i3cqQ6Yfx2rgLn8HZqHO-OcV3nK_cWnLAVKaXx7M9x0qurL7fDw1w7NhtOdYb9e26A_YfcPRzjSpFleSRCFEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😶
🚨
🚨
این کانال باعث ورشکستگی خیلی از سایتای بت شده و پلیس FBI برای دستگیری ادمینای این چنل جایزه تعیین کرده
🔥
https://t.me/+bDapVmvigDhmYzZk
https://t.me/+bDapVmvigDhmYzZk</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/Futball180TV/106733" target="_blank">📅 01:37 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106732">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pfmg3ZGIEbbdLT1oNGkouYuCub6zmN_9WI82NdAMsPe9CkPRvaZqdwRirSMFLHHXy0slN9l6ATI6vle2SA7wEaRq11R5M6LcG7sSaN7Bua_XGWdH2rOj1rKYQGrBgz24uVNW0FBp5N6_owGidSTbrq0ZtSzoeYIyTsllWdnfoYWUB9ddH_VR21wm4Lta2wtkU--6qjH_RCQrs5k703nMuc-qjLN7EE6gFK1k6v9k_06bJg986tf3llmabEopRmeJNq7WSizwiaKKASovYWK2Sxd1E4khtjGgFtviN9EVzdD6UkiRdZEIc04WV5oZuZVaBjjG4caau0efJvgvdrPfeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
✔️
🇪🇸
تواضع و فروتنی رافینیا کاپیتان بارسا:
🔻
من میخوام به لامین ، کریم و گوردون کمک کنم تا گل بزنن ، میدونم مهاجم نیاز به گل داره. ما خانواده هستیم ، توی خانواده باید مراقب هم باشیم و به هم کمک کنیم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/Futball180TV/106732" target="_blank">📅 01:28 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106731">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TAP05ZfOQ-4bHaCWp8KpS6a0y--lmBWs0DhaxvMepHIlpaeMXcZyETRLvKur2r3t7lw8FUMKKkmBvQp2qBfI9_BG59kEme4aBhGSb8C4rQY66yvxpvxZDZeATxflK0CnilSHmtw6jKL_ZXuyN0qPfS_GcMxlPnxhXmSd06hpjEmfPmP2O1wWUjILcBQzh7HbCGoliHJlUQOhJpdBXDX-JSTTtk1ldG9nRNF-HlfDgl3iDPsJhcf_4uL4CcQH1e_f4SVZkJcH5KzzyxGRfgEiEsn_tioXwSEfUUK3PcaXxLcUQajF7WgcELq5PWR1A3lCQzuFAdcQxHwuaOyYMK8ACQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
✔️
🇪🇸
تواضع و فروتنی رافینیا کاپیتان بارسا:
🔻
من میخوام به لامین ، کریم و گوردون کمک کنم تا گل بزنن ، میدونم مهاجم نیاز به گل داره. ما خانواده هستیم ، توی خانواده باید مراقب هم باشیم و به هم کمک کنیم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/Futball180TV/106731" target="_blank">📅 01:26 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106730">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sMN9UmmmW3xFU2YUx3Sd8Q3f5QfpeHuGRJYcHmXE72UJcB4NgqOCrr5RIZ3o8kfsVfFWY8XZs3K_KuT8ncyCgcIt9qmFzo87mLcAttBwoo8mGUx9a9uo2Iri5mPgZvdOSisGEp281SwtBrTueFjaK5LDWm1uYjButswfwUj-U9ZFQ118vFGV7hI4oAwU9uCpdGbmWuqw21rnEMhDJsH0vchUUSuzgqKjgX8DMljNeyvePBihsreyVlgljUbZZ9SPRNL-ndSaPh3LVVF1I37iTc5hALu3_bPYjv64X4BWyOOZkfAeVfER8ZGf1GlF1KNn9V7RAYAWTBf3MXLnXaAzpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
👀
شاهکار این‌فصل فوتبال اروپا بدون‌تردید!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/Futball180TV/106730" target="_blank">📅 01:16 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106729">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rp1nfOadGshpF2HrKReDx64ZUgCMeUc2uio1xouYaqwWaJrBr2J9UAleaIoFaNTZ4PyRRarhL-mZQ02tq5YXryDZUFB2JM-VQqFBAvCidgt4HgqlfpijNR8j89RA1f9jYYuOx3-OzqIxwKuC1u8r0vByen7AQ-2US29nzrzGvQk0LBBdsCBAQqQAfNMVZJXql6iAcUAKbJqud-Dh3xrGNNmt2KqYuhjwwGezbEoHmn7hBS_us1ZOolCky_MkmGNC8yx51TFQ_IpylxIlQ_BGONqzRXXLp5LlGL7-Szqp99fL7qNsrekNs4THpOiTJj2ILLrwOF3kJ1IEDQQ1rfUdsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📊
🇪🇸
وضعیت جدول لالیگا در پایان هفته‌ششم
⚔️
برنامه بازی‌های هفته‌هفتم:
🇪🇸
رئال‌مادرید - اتلتیکومادرید
🇪🇸
🇪🇸
بارسلونا - سویا
🇪🇸
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/Futball180TV/106729" target="_blank">📅 01:12 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106728">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bJn2QygIlWX6pgIJn0oDZj5oCX4VojCE2Lav3SXlCGjqg9b5ZuZtt4A5hn0eqXXzxf4l8k_LMYMsYWpJBQlc6H-E13QeN-9v-rSteL2NWaq1o7HTaYzPsizheB7vGl7m-Jzq5zrWW9A7aqvXjOg4WRaKqbtZJuWJU4gCM6CKn7rtyHX8fAq-Vl5dXWMyDPn1FY97BP1y0YCM5WnARXx4kcAco7GVq0iRc54Cnfay-q1HNGoCPZrZS7EfY4K9_EaCkkngLL5rkHCsplKMmUBO0D91qWKR7lvcn4ot4nIiqFRebmZFFq3yp_wWmxP_Ffs8uBYxsFne4xs8-yLCjm8emg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
بارسلونا بهترین شروع فصل تاریخ خودش را رقم زد؛ 7 پیروزی متوالی(لالیگا و UCL)
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/Futball180TV/106728" target="_blank">📅 01:07 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106727">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V322pWa__B4blZb7WVwjKGzRdpUnDK3pUClRAaQPj3YTsn7eGiEieSqVKxm55BkPQYGpXZIhLl_PLY3qdhHH26-ZL2S9y7IScjLZXJdm2iKehOw45qCj2-BSqDtfxXMeSMCNcgKFRZy_OyRPMpkGi-uBHCQCa2b9yUCRFY6eeCYjoG_ElGfBr5csXueverV-OneqOufzRHFeNf3ykyIDhzsw_UIA619g0j6PB62M9e4l5SbEJKnzqvRUm-7teGoCWRarjYSPacEYxgS0U_yoYbh73c9-QINP6LH_Ds1ujoKlzM6UZLNOxsIwuMWvr5a12uPja7zDdD6oUTFfzZqsCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
لالیگا| بارسلونا به لالیگا رحم نمی‌کند؛ همه را گلباران می‌کنند و یک سؤال: بعدی چندتا؟
🇪🇸
بارسلونا هفت - سانتاندر دو
🇪🇸
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/Futball180TV/106727" target="_blank">📅 01:07 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106726">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">لامین‌یامال
🔥
🔥
🔥
🔥
🔥
🔥
🔥
🔥</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/106726" target="_blank">📅 00:57 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106725">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">هفتمیییییییی</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/Futball180TV/106725" target="_blank">📅 00:57 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106724">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">گگگگگگگگگگگگل</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/Futball180TV/106724" target="_blank">📅 00:57 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106723">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/fd0c97753f.mp4?token=U8p5qz6zhvV1gamosXVueXgJcKsjhaWGtDf5QV7QQ6yZkN-alxcCEAnUhjSJNdYIkEzEG0pk3rRedvRX9qM3kh2kuNV90SptegIQzSzrMI2qNeDu8Ljxy1RazWsjSuHCBTf1NzNpHQy09eD8WHRX7frZK3NsTDne7SOBkgHh2AVgV7tgwH8K3hfWsrNwh1aqwWCMkXkNKwOU4ggxk5bp1v59uPc48Z0gI1FVd5MUQfW8sXj-G06I2KiLbRy7UAwuQwXnHZV_I0mx06SzkroA1K9fSZB1Rex4f0PqRJ9pcT80QP_H1uSqDcUHL-xAVSjCVviMzia1dLniNa8lgBRGGA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/fd0c97753f.mp4?token=U8p5qz6zhvV1gamosXVueXgJcKsjhaWGtDf5QV7QQ6yZkN-alxcCEAnUhjSJNdYIkEzEG0pk3rRedvRX9qM3kh2kuNV90SptegIQzSzrMI2qNeDu8Ljxy1RazWsjSuHCBTf1NzNpHQy09eD8WHRX7frZK3NsTDne7SOBkgHh2AVgV7tgwH8K3hfWsrNwh1aqwWCMkXkNKwOU4ggxk5bp1v59uPc48Z0gI1FVd5MUQfW8sXj-G06I2KiLbRy7UAwuQwXnHZV_I0mx06SzkroA1K9fSZB1Rex4f0PqRJ9pcT80QP_H1uSqDcUHL-xAVSjCVviMzia1dLniNa8lgBRGGA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یا حضرت عبااااااس چه گلییییی زد
🔥
🔥
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/Futball180TV/106723" target="_blank">📅 00:49 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106722">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">پاس گل هم لامین‌یامال دااااااد
🔥
🔥
🔥
🔥</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/Futball180TV/106722" target="_blank">📅 00:48 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106721">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">چه شوت محشرررررررری
😳
😳
😳
😳
🔥</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/Futball180TV/106721" target="_blank">📅 00:47 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106720">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">گابریلللللل ژسووووووووووووووس</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/Futball180TV/106720" target="_blank">📅 00:47 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106719">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">چه سوپرگلییییییییییی</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/Futball180TV/106719" target="_blank">📅 00:47 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106718">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">یا مولا</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/Futball180TV/106718" target="_blank">📅 00:47 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106717">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/b622b454a4.mp4?token=fUeQGAvWhqsbJbM7KQ9do4Cdw8QQbUZhFAjdmLRCbeY8wST1B1QzdoFe7bYZvoqI34bEg_TId2Urd5PSHrH2--vzypw2G8urMrxxqEj34AjWYDFMjAtCS6frLntXyVqJVqr4lgOdlJq9iXQ3Gz99Gy_lZAGJoLyGZXi-xITta6jKl4X5vhOCDspga9mUW7pbdebRPWFLv-LvWYNYFzEHqaNTshkp64Rk3hSb4_yDytc6c9h8Z1jI4KLETh-V-JJGPnx_giQU4p-7iJy6YraPjfLdwMO4i-nidGlMZz1CN3OCJOYIhT5VJd5lK4F8rFZs48IhdjpgkrZGSTowcgYQjw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/b622b454a4.mp4?token=fUeQGAvWhqsbJbM7KQ9do4Cdw8QQbUZhFAjdmLRCbeY8wST1B1QzdoFe7bYZvoqI34bEg_TId2Urd5PSHrH2--vzypw2G8urMrxxqEj34AjWYDFMjAtCS6frLntXyVqJVqr4lgOdlJq9iXQ3Gz99Gy_lZAGJoLyGZXi-xITta6jKl4X5vhOCDspga9mUW7pbdebRPWFLv-LvWYNYFzEHqaNTshkp64Rk3hSb4_yDytc6c9h8Z1jI4KLETh-V-JJGPnx_giQU4p-7iJy6YraPjfLdwMO4i-nidGlMZz1CN3OCJOYIhT5VJd5lK4F8rFZs48IhdjpgkrZGSTowcgYQjw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🔥
🇪🇸
گل‌پنجم بارسلونا توسط رافینیا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/Futball180TV/106717" target="_blank">📅 00:40 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106716">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">گلگلگلگلگگلگلگل یامال زددددد</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/Futball180TV/106716" target="_blank">📅 00:40 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106715">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">گلگلگلگلگگلگلگل یامال زددددد</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/Futball180TV/106715" target="_blank">📅 00:40 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106714">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/a4e9698bbc.mp4?token=AjXoKWuR_x7SlqrRjaVG9f8mIqILOoPiZLLEoirRylQtUI-XQvM5vKz_Vl1gjSp1_gZcuKRl4JZNork4zpl4aGgrPntxpNEjocdf5CcV2m81iwMbtWtaMin5USniiGGY-RvDFJcqbcukrUBU_XA3oRRLZSr-CL_zoMCxU61ybdGKViE9laAG3QL7pbaibT_vYQmJsMeusiRTApB7ADkvH1JMPiFSD_2WDVOXWNmkYw6ZY7S-X-_Hf1L5S0loDoNZ6bKwmExzVOcUEDem1tlcoLjxydK_9LI6WpTQ7AO1D_de5M7uR32_JULjNL0CE7x6MiSiJzhp_zt76dKX_0AiY4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/a4e9698bbc.mp4?token=AjXoKWuR_x7SlqrRjaVG9f8mIqILOoPiZLLEoirRylQtUI-XQvM5vKz_Vl1gjSp1_gZcuKRl4JZNork4zpl4aGgrPntxpNEjocdf5CcV2m81iwMbtWtaMin5USniiGGY-RvDFJcqbcukrUBU_XA3oRRLZSr-CL_zoMCxU61ybdGKViE9laAG3QL7pbaibT_vYQmJsMeusiRTApB7ADkvH1JMPiFSD_2WDVOXWNmkYw6ZY7S-X-_Hf1L5S0loDoNZ6bKwmExzVOcUEDem1tlcoLjxydK_9LI6WpTQ7AO1D_de5M7uR32_JULjNL0CE7x6MiSiJzhp_zt76dKX_0AiY4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
ریدمان محشر شزنی معتاد
😂
😂
😂
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/Futball180TV/106714" target="_blank">📅 00:37 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106713">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">رافینیا هتریک کرددددددددد</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/Futball180TV/106713" target="_blank">📅 00:35 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106712">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">گلگلگلگگلگلگلگلگلگللگلگل</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/106712" target="_blank">📅 00:35 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106711">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">رافینیا پشت توپ</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/106711" target="_blank">📅 00:35 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106710">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">سومین پنالتی بارسلونا
😂
😂
😐
😐
😐
😐</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/106710" target="_blank">📅 00:34 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106709">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">پنالتییییی</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/Futball180TV/106709" target="_blank">📅 00:34 · 26 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
