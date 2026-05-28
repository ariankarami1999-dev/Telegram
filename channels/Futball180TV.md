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
<img src="https://cdn4.telesco.pe/file/hQhajDmEeCBbEXLyUHM3soVJujc3Cz53kC_00iEpsN7MCQ5TcLsBfhMnBYHOaTf_dFCC19baWL6__XCy8_DI656WBrfyN5A_5AVMXUkCPAxKsMVivrG-FuQATBKsoQYi-cXRKymO28m76YNKNMWT1mEVR2ra65FNvIT_IFVfZCyXakWWmSK0f8L0quXkBVzoko0FV5dgq7gnlnBmcXKu6Qj1z3glTd7NiLZ67sjM7NbCL7d0T17CSqgou6GPn4TwA8WxRPFLiKvwajUnE_8Qgt0fSzowrkv6R49ksAGJ80IbkBsC_fFU0DsMvvxo8Q-JMwSnZgU9UvNtUMnbT_UF_w.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فوتبال 180</h1>
<p>@Futball180TV • 👥 122K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-07 21:27:45</div>
<hr>

<div class="tg-post" id="msg-90363">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NL9_rRLY35J7bWeadPLvXvrEiKi4ackWMIAWM5TV9K9XGBl78_NZrbphFFQUQPLM5LvjBKIS1bhG5JWyCbwxBpMKeDYTV7Noyg4keX3qHcCjcevLnyrCZzYo3s00GqiV2yrZMwu4CBdlTw0Rh7BEZWgOJk0-t9nklmokRACDsjpscF2tZcYdQ70lXp0xm1evTa2zgtgG4EA7X5InlSoQhBtJA5oN0IPPsdTOVqGL1bCkKVjMRkW7TRwnIk628ymMaIu26nWV3FiBnBdQu_XvT0pJyO67CEhO8txXZGtfa4orGhanWHv3mwe7471XUJ9uqfBdZuCEywCvkkqzb_5q1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
نیکولو شیرا :
قرارداد برناردو سیلوا با بارسلونا تا سال ۲۰۲۸ خواهد بود.
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 642 · <a href="https://t.me/Futball180TV/90363" target="_blank">📅 21:26 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90362">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FbJPBEPUKYp29UxCFicUMeRTfJAtw-y7w5_MJ5IKBxfovzG2xSk5UALTOCuk3sLyQUzBi8aphUNMIQrGmQ3Y4gyNhUYeSpDCCRRbGCdg6zd6GjT8VXo1MhrmRB7VMQEw1OvTJ1FEa9huOiua4ZihXijTWsDZ5lgQ7bUidyE33kmwFBdZmadPxkfLkChxFyDn6NFVrrceSUvG00BRhsymsVu6MDJ_Dk5XlL9WW7DMEku1ncHBmhTQYnY_LtrYm-Qsi-aKR-CFEUYCOc-autNmOlu9nviMlJf94A4ZvRokk-wBgu_ouKRXZz3CEnUAHkL2NG7mv0cT5EWjtspgwdUiHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تیم بسکتبال استقلال در بازی برگشت فینال انتخابی آسیا موفق شد در یک بازی جذاب پالایش نفت رو شکست بده و به عنوان تیم اول این تورنمنت شناخته و راهی آسیا شود.
استقلال 93-78 پالایش نفت
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.02K · <a href="https://t.me/Futball180TV/90362" target="_blank">📅 20:43 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90361">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IhS9LxPYEV4fevASSSwxC03QEpbrzeMsKociWH40OrWs41o6wqsgAdffUTyguFJqZFz0GIoIPK5-Aj16RNJHTgbjwGW6lP6bTBj1ClKXIl8HNVdbu_ug7DbBDuSBr0uu1EGBejm3Oze7cF6iKWZrmvyAo_VZ9Q-DC4e77iQBMfd8YI1ZTjs5iK4nYIwVxuvlg06xBZLevNbxu0c6ZptU2id0VBzx4iBSY178wPJwMO8qTjmYRqu5TPU4u4Qja9Xfo3PBbmYh9N-b4_TKMgvbFL8JeY1PMYIxF7omkD_UJkvXiyCfuNIHZzWV-SX6vxZ8Uf1j4BcQ0ko55Y5GjHepzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
رومانو : آلگری به ناپولی
HERE WE GO
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.15K · <a href="https://t.me/Futball180TV/90361" target="_blank">📅 20:20 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90360">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">معاون وزیر ارتباطات و مدیرعامل شرکت ارتباطات زیرساخت:
بهبود کیفیت سرویس‌ها و بازگشت ترافیک بین‌الملل به دلیل طولانی شدن قطعی‌ها چند روزی زمان‌ می برد، در شکل روند افزایشی ترافیک بین‌الملل قابل مشاهده است، کمی صبور باشید
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.28K · <a href="https://t.me/Futball180TV/90360" target="_blank">📅 19:41 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90359">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B334AJ8VyIjwh7kKYB7jNZ_faX3LICaqPPla2ceN6zFgFDAW9wjE0u1JaKCbchvH3THsHo9EHyLbXK5gfUEcv7oKuLITevqYxsgac7bAmE-5xbTsvf3w0KbHNAUQRdWR1zYAJp4F1EiS_iV4Hs6V-r6nVdHhU-DB6NyVw90LO3NDP9JSMv8tY3Kr8MyOVmeHi3lfnOwAMt5GHbv7NUIW71L_TBg9lpWVzhsLdr27p8VspiMi7eJIYeetoQdcjLxphxEmvGPJm28S5w3jEIVqJV-WMLnNDNv_yDxhFUYb-MtQCpQOua2ZdTciMNQPYPksmKbTOo-Jd0t6Um91nL5YRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فابریتزیو رومانو:
تا این لحظه وضعیت مارکوس رشفورد هنوز مشخص نیست؛ خودش هم دقیق نمی‌دونه تکلیفش چیه و منتظر تصمیم بارسلونا تو روزهای آینده می‌مونه
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.17K · <a href="https://t.me/Futball180TV/90359" target="_blank">📅 19:04 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90358">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">💯
اگر هنوز ۵۰۰ هزارتومان رو  نگرفتی همین الان عضو شو‌ و جایزتو بگیر
نیازی هم به واریز نیست
👍
تنها سایت مورد
#تایید
ما  با بونوس های واقعی
🌐
Winro.io</div>
<div class="tg-footer">👁️ 5.68K · <a href="https://t.me/Futball180TV/90358" target="_blank">📅 19:03 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90357">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rC71Z5LCuR0_Qg9Z5v_v9CsTK8sRUIK-_mmlS7u7lXM5QnY2TIMoVWegiCXaXvQPixz07l8MaRP5GAzSuZ561LNHbAPzfFyfKqVieKupzBbnHlbpl3bPzPWIj4uuulDje-QgwvkU1hO8HwCAYK-uSiInj27qY77dUNbbR32r9BUUU3EOC0iShczrgAvSXuurCltxNtXCY0UIA01XC_20f-_1WSEic-o1Qy1zxU59a1OTWdfebpJ9skYT_Iof2WASIgXzco45Kk116lfnj5lGcHxPbCMIFr1T9-37L6xlsjdcaq5BsHANpLRdtDLrVFgbc4o6rnRfSkhMBPWZcK0IJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
تنها جایی که در لحظه عضویت بهت 500 هزارتومان موجودی میده اینجاس
❌
🎉
کافیه فقط عضو بشی تا
#وینرو
بهت
🤩
🤩
🤩
هزارتومان جایزه بده ، نیازی هم به واریز نیست.
⌛
پشتیبانی 24 ساعته
🍆
تنها سایت مورد اعتماد ما با بونوس های کاملا واقعی و رویایی:
🌐
Winro.io
🌐
Winro.io
کانال بونوس های رایگان
g7
📱
@winro_io</div>
<div class="tg-footer">👁️ 5.65K · <a href="https://t.me/Futball180TV/90357" target="_blank">📅 19:03 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90356">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iOMWH6m-fWBTSaa6B6sMj0XBYZ-wQDFtONyIz3eGjyZvTaj03aV1_Juzv66EYZjPTIe7oNyOCsZZMPwNItfyTFGaAqGSvezfghvXXy-0aJI58TacXnNSTX-9JmSHdwejWcb3uzDV9bozFqnmcfaSub12r6ywZy9zXfq4GBZQhYEvN79MYgbLgW1SvNd8TLBSR3x4pEJy7wKq5Kh2TAyA-4HPf0eo5R90X6jmRTxe-H9Ijh7h4eu_qKaUX_VGVgdrshO1ofTNBgDGKYzvmPsa2NzTGQa5OsCzzx4iuhdLRizIsrDJvaBDPxkTTRXno6FTDRavGCl7G7up7kOIgy_sJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
کیت‌های ایران و هم‌گروه‌هایش در جام‌جهانی 2026
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.53K · <a href="https://t.me/Futball180TV/90356" target="_blank">📅 18:59 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90353">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DBNC18CMZG-ZyfR91EBpG4e3HUFw0tBIAicOl8kZjYMMRwo-J8QiCRXHEGlBb9yIaLdjbBgAIaJEKJh0jXEsoMMp1I9zZI_4PO7NxpPU7isPpNvY5qstey3kz_BA0VYrgUQtQ-YdRvx6hn2NjtGCDgzRI81TQZb_wq-oXNjsw0tmbxgUq9ypfinn9ivqQYa0vpChdC8lYBTVQLQIuPJcTygSPzrii-Nq5ucCe2Zy7-K-8c_nGso0SXmrWyVlw_G1JXtQVmZ9I7G7-R-ReBp5ABPyUeLZCQsQW81I-kf6hVUp29S7vnsY3_CS1qUblPn9roopUUUi9A3I31TirazBHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فابریتزیو رومانو :
تعجب نمی‌کنم اگر بارسلونا بعد از جولیان آلوارز و آنتونی گوردون هم باز در بازار نقل‌وانتقالات فعال باشد!
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.14K · <a href="https://t.me/Futball180TV/90353" target="_blank">📅 18:29 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90352">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">نیمار سه هفته به دلیل مصدویت غایب خواهد بود
!!
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.56K · <a href="https://t.me/Futball180TV/90352" target="_blank">📅 17:59 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90351">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/abw7k5_0fNfeXl1mySAdkaBWAW_bzxx6F1rTK_2RHZt8b3WioATKjrZ0cxOR1-g5h4a_kAl0EOTN8ITpQ8pThZN05t5mx9UL5wCw-T_tihb2fokNW13Hpezo4km-LfKn78KvF0o3KRJ3vpio7-iqfjlg5Yl_F5obGcvPU4NEaEJZUT3s22oJuH78L8ldrEJk_gcvx3KOM4eBrTcgR1WXXWHhCh0gIu_9AyYvMfybxHGc4UF51_HvSMEEAAE66_654r_HEmwRJeoKXgavMhhQbrL59wZ6F4SILvVUaP6U6LhLMewCWF3qnWqNtwCxJSffA9-na4aL8qEyLZrQMUM20A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
اتلتیکومادرید به بارسلونا اعلام کرده که هیچ رقمی کمتر از ۱۵۰ میلیون یورو برای فروش آلوارز قبول نخواهد کرد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.33K · <a href="https://t.me/Futball180TV/90351" target="_blank">📅 17:37 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90350">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DoOzrntmgG5Gllm1wYErK3o7Rw04l5KN1EOI7si4gllSc8Z1e6pC-7i1bVCHFafqsaKsPWn9gXZoWfDKX_1mI-7EWsfLWFcP2anmMgoYzK6tuYlBWHBwonYCCEdKu4Zf04UQ9WNk7HhEhmFjgpxNfsmdhS9NFCo9dYs4hfH30BsBiV0cQfJpphkpOhTXHBnSB1t8m5EwbUMkj-IoiyqO7HaY6pJ9cKEGON7rQq7t6Wh7Ngw4orvociPUNrgINIVdfle9hgxj_J1y8zZaJ2y5namvq7CPLgudVoYpd2_s_JjE6ytfjoQldpxjd741iu9TGyDI-VuGNN23rJ_18hKgwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حضور گوردون ستاره جدید بارسلونا برای عقد قرارداد و انجام تست‌های پزشکی
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.33K · <a href="https://t.me/Futball180TV/90350" target="_blank">📅 17:25 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90349">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o2FF1v2sQdK4dq_N4Hd02LOaclRUowr9HiZDK0XVi5WzRDwOU5zAFeKCgvUCu_21S9wKZjZN4h_6F10OOQBbPObKijrzJA4MTnV3bXhpr7-mYY_EyWCWkPXr9ay5B8Gax-9ihPwH25WbsHjJtnli0I_hsYw8i4_j2sDQuTXtrIlwk95QVqLYdQVyazrTFkhJLX-7y9kDcgTT0BycT7LN0HvxiFXVzN5BJCynnLLUzwEAek5jSJqx3Wp3NDxA78em-HPpVwgtdBFCy5q-qJQ5Lhgeb7zuHDYuUjyiBa8tGpGcbY7uhAg-6mH-X_Y1t6iPa5xSYdmZIvzNGjbh1FICAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
مراسم اهدای توپ‌طلا ۲۰۲۶ روز ۲۶ اکتبر یا به عبارتی ۴ آبان‌ماه در شهر لندن برگزار خواهد شد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.97K · <a href="https://t.me/Futball180TV/90349" target="_blank">📅 16:39 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90348">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ae9wSRQ3C4p61SmL8RvjG7SaAhrUFVv2XX5py6qHjxtEuyLW30NgNSyQY1srxAx52NITMLlz_l2vIRF1YlonEGLPejtP2eLkVLWnyeG3UEj3vih-MoIzPzihkTIEof7C5SfTr9CQd7HBAobYwVvGNYiX9YQB-9lcX-77dEHMnbJZQewUHfPPZJCEt_Etjc1Qwms2U6OzQUgDKt7I93IZw5rVH6rHLAAiIRL3yaG7eSBVSbD9Eosl_idDAAMb2M0IMtKDvn-EJzyqcN_tlI8-exCF4YqpsMKf9iY26UHh9Q6e3no_ZCvL1y3VxeqKuzgA4dvKWwsfC7pDtjAgnxdiSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
مارکا: اتلتیکومادرید می‌خواد خولیان آلوارز را با قیمت ۱۵۰ میلیون یورو به بارسلونا بفروشه
💸
‼️
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.99K · <a href="https://t.me/Futball180TV/90348" target="_blank">📅 16:28 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90347">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IUXcb-o6MalQJpnNpufQCo3-jP81_s6IWPMPwG_9J_DuYGooLkIRCGZjQNDVD_XV0zm9Z7zoquwfYHxmmId5iqw6rmW8G8ncTGULcgxHSI1YuJDs0lEEJI1v-8KSML9knEj3PRpykSEQpjVzDlK8plCb6RT6jTx7hI84zBm4Aj6KMj8MOHqwTK_P1-zkCOKo4wFkC-nlU0Tt_tYLw4lgQfDU27PBcvoF_h-sRPlNCbCYK466drou7As7qC1bIOPkWH8QmpdPsMF0brIp0h7DXYX0HyDwOGTqsVc2G9OiPJ4rTiBiXd8uFfT43zMCz0PfIX5J-gwk9U-NOTSN8RHPjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مقایسه عملکرد دیگو مارادونا و لیونل‌مسی در دو دوره جام‌جهانی که قهرمان رقابت‌ها شدند
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.05K · <a href="https://t.me/Futball180TV/90347" target="_blank">📅 15:48 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90346">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fb77f6f337.mp4?token=p7464886x3NBXcaRx-TRACgDHvZfDA9_AWjiqGbYqNvroM5a3k_VthxzUs5izUwgxxdo-_EOzBfkV9ZiHiiA5GHcgLk9aorkw5hVG0QaVc38iv8LdZ7XwLRJPgPOzmdyTIvrgpipp3IXzHIFYTWpiUdVaqTKR6OpuvQ8yFB5_ktvdJHTVmPUB83WYmAmeCD3FrMyd2IpjUYtqWXopOMMncNf5h5CaspHV1A9taWuYu1dbNVgvCx6iFht6twmECqhzfFZfZgv4Q5DDl2_7DGP4__qk8RNQNskyVoHjkqUugPDyquxBXvD624Q3aaxdQrM__pXemKL0xMhzu8mQipElm0PIi4GaePrgPh_gJoa0rfGZBBI2UFq8nV5rEmmPCL-iNHCwx2k18pzxm3LYXPoD24OitqZSmWdJlcnzuf2qK9R6RYpr_PQxwQuMTRZnevmUxqIXkGjsjnJNceE5WRnqtnJz3yxyu5wkGdQ-lLJjoMAgSrpAmKkU73lKMAh-y-dobS_zXVnbCKuZMUsG3HAFE_g-lu4nQr1t_yHHiJSU_a4j5gzWDDyWcXWFc5XKDseOibREQ2To6kQl07pDiInS3Z93d4QwyVbh3-9Qgw44Cksx-qxQV2t0N_x2f35n8DfiIxqzRRbWngYtiBDu-rRpSKuZu1vuqPZFee7krNEgBQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fb77f6f337.mp4?token=p7464886x3NBXcaRx-TRACgDHvZfDA9_AWjiqGbYqNvroM5a3k_VthxzUs5izUwgxxdo-_EOzBfkV9ZiHiiA5GHcgLk9aorkw5hVG0QaVc38iv8LdZ7XwLRJPgPOzmdyTIvrgpipp3IXzHIFYTWpiUdVaqTKR6OpuvQ8yFB5_ktvdJHTVmPUB83WYmAmeCD3FrMyd2IpjUYtqWXopOMMncNf5h5CaspHV1A9taWuYu1dbNVgvCx6iFht6twmECqhzfFZfZgv4Q5DDl2_7DGP4__qk8RNQNskyVoHjkqUugPDyquxBXvD624Q3aaxdQrM__pXemKL0xMhzu8mQipElm0PIi4GaePrgPh_gJoa0rfGZBBI2UFq8nV5rEmmPCL-iNHCwx2k18pzxm3LYXPoD24OitqZSmWdJlcnzuf2qK9R6RYpr_PQxwQuMTRZnevmUxqIXkGjsjnJNceE5WRnqtnJz3yxyu5wkGdQ-lLJjoMAgSrpAmKkU73lKMAh-y-dobS_zXVnbCKuZMUsG3HAFE_g-lu4nQr1t_yHHiJSU_a4j5gzWDDyWcXWFc5XKDseOibREQ2To6kQl07pDiInS3Z93d4QwyVbh3-9Qgw44Cksx-qxQV2t0N_x2f35n8DfiIxqzRRbWngYtiBDu-rRpSKuZu1vuqPZFee7krNEgBQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هواداران جذاب الجزایر آماده جام‌جهانی فوتبال
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.17K · <a href="https://t.me/Futball180TV/90346" target="_blank">📅 15:19 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90345">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W5SH_2ycOLMiEDQGtv8ehB1IG17boO9YwiCkbR8vuLMvOQoB4BiJfEhfjE6O7hAx9KNKGqr4cEV_S3DVgzNxGn05oCfpulC8nTYQnpUZ2o6jymo4yUs3vrnw39vZXX57ml-KuD8tgwIOYRLHtn16x-S-DO-ml9q1k5B7P0SMJWuBFJXm6vZXroidQmMbDRJ8cfM37_g9BBsNAsR-4MNki2ENIUNEuHSubQIIJcWtLNvCJfh1_gDRIBprCISl_yMDYF11zHEyXRfVp29hpzkDwQLtsLUCAxypURPeDRC2t6geyuA_TJEwFtWyZ8PbbcdBBA3lOBW3HVbz2M93fob7Zg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😍
🎤
امروز دور جدیدی از رأی‌گیری برای عنوان جذاب‌ترین مجری فوتبال را آغاز می‌کنیم.
❤️
عکس‌های جذاب ۸ دختر از دنیای رسانه‌های فوتبالی را تماشا کنید.
1️⃣
و هر چه سریع‌تر در کانال ما به گزینه موردعلاقه‌تان در نخستین تقابل رأی دهید</div>
<div class="tg-footer">👁️ 7.57K · <a href="https://t.me/Futball180TV/90345" target="_blank">📅 15:19 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90344">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pSVPWnnB2ho_J8wH5wyx0KYp1AU2WB6i7gVozrQLph2kvjLFm20DD1tizhyHTCjt5R6o2URI5o5--5pD0spjUcavoFt03A7vQowlHtzOK9C0Z-Pbg9ZJLDQM2-LbmscPjeTl1GVFnrSAzM6lYDTWHxVEu0V2mlLFCLpR8ggLYe-VfqPACN3zsg7nzLKUrVOiPJnN0oKSLTlAWhKEjIt-lhe2Ni8MxtVbN-bCL3EubqU9lG5ZVd2kzuwE4sVkiOdcjTzzUam_prKAMifk3k2ygE_NpvbKgk72GNUs2kxR-wxeh4sTecrG5RMfIhIzqy9Ym3NCsffAX1252AsuLr3Ymg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مقایسه جالب نیمار و لیونل‌مسی در بازی‌های ملی
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.29K · <a href="https://t.me/Futball180TV/90344" target="_blank">📅 15:17 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90342">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dOyHWDlVHlvhh0Uov-uneb5f3A9rnUJ34DFWK_bdx69gBN6oY0Ovwm2Mx0RDYeRZ9HeF5frqafNMCxAf2XA-a8onW_ZLlJiNn28LM97766K00qhkVM_3l4g6fW1RBrnysv14N2cs8OoO0WL46KBf2HVPBAcKLpZf4ASMTbchsEzyWG5LyddMugkmxlCQm1WriV6eGqah_dEwDCLoVmGqYVbjvlG8qVGHEnR-183wn8sRLODvlB7pPMqkj3uCStxZ8h0yJ9wqY8s8jn6V3kTedPRnVtCVEuj9GcEYOAiPuaISFUXDDxyGD6Nzz_hbKs8SVUZHGPEGCf5Ago7ClYbXdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بهترین ترکیب آکادمی تاریخ بارسلونا
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.48K · <a href="https://t.me/Futball180TV/90342" target="_blank">📅 15:10 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90341">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bdadf29b0c.mp4?token=Xy1SPUU2ytJzoBbjeCvjg9c08Z5lQSD1feQiLdyaPJQa664TuA49zjJOf8IcVUHG5GI_aqMf7BC5urijRCdu8mKu9QCdq1Et7f1-sFpQlkfnBGw8lgZwJLDKFWHpnqioXWb688C_uhJHAAQW1XZ9wepFMHWISPAvN0qvfMXQfzkP-PQShB1TRYr6Wte5skkD6sSg65bmR2NAXd1bHpVrQOUPFVHw30bkwXe65XWcqLEar5ubVoPqRiNy3EcdPvJlYUSKDmuslVdvZo7e4hioVCwxnQ2eq6j2P7ZcIoQj33vRdnZ5nLcEx1p12lpsg_uboQ1dbAvxx_sXzYFKCNeL6A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bdadf29b0c.mp4?token=Xy1SPUU2ytJzoBbjeCvjg9c08Z5lQSD1feQiLdyaPJQa664TuA49zjJOf8IcVUHG5GI_aqMf7BC5urijRCdu8mKu9QCdq1Et7f1-sFpQlkfnBGw8lgZwJLDKFWHpnqioXWb688C_uhJHAAQW1XZ9wepFMHWISPAvN0qvfMXQfzkP-PQShB1TRYr6Wte5skkD6sSg65bmR2NAXd1bHpVrQOUPFVHw30bkwXe65XWcqLEar5ubVoPqRiNy3EcdPvJlYUSKDmuslVdvZo7e4hioVCwxnQ2eq6j2P7ZcIoQj33vRdnZ5nLcEx1p12lpsg_uboQ1dbAvxx_sXzYFKCNeL6A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">استقبال گرم‌ و صمیمی از نیمار در اردوی برزیل
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.83K · <a href="https://t.me/Futball180TV/90341" target="_blank">📅 14:45 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90340">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cc9f0d340d.mp4?token=O4r1MeWrNBZQUTHGNyj6OpvRwjJcWCHidmM27M-_nqKWnnnfoTj1a0lSvSHUu-7vBZH4cBZir5fCMF627NaDKYuKMxHc_i7gpip-WMUEfHbNKMffGnj_KZJ6wnwu73UWrSREWAjbmljjP2cNT22UA_K4nGOn5OTzFHATUvdYW0wtqR5-B08WMlr76cHBdBL_jcqQzqdrow7YpABRgmm5eQL7SRCc9vS-_22S0eptdaAcDzsy6enXlTEH-wikE9E--6jmes65Ob_70fz5P7gLJFsCBMO4JXp9KZIBA_D8Wu72innws825ahR3ClbGKjRoZnXToZqxF6cd5DOtvY0Ixg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cc9f0d340d.mp4?token=O4r1MeWrNBZQUTHGNyj6OpvRwjJcWCHidmM27M-_nqKWnnnfoTj1a0lSvSHUu-7vBZH4cBZir5fCMF627NaDKYuKMxHc_i7gpip-WMUEfHbNKMffGnj_KZJ6wnwu73UWrSREWAjbmljjP2cNT22UA_K4nGOn5OTzFHATUvdYW0wtqR5-B08WMlr76cHBdBL_jcqQzqdrow7YpABRgmm5eQL7SRCc9vS-_22S0eptdaAcDzsy6enXlTEH-wikE9E--6jmes65Ob_70fz5P7gLJFsCBMO4JXp9KZIBA_D8Wu72innws825ahR3ClbGKjRoZnXToZqxF6cd5DOtvY0Ixg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انتقاد جالب و شنیدنی هیوا یوسفی از وزیر ورزش و جوانان که هیچ نظری درباره قطعی اینترنت در ایام اخیر نداشت...
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.2K · <a href="https://t.me/Futball180TV/90340" target="_blank">📅 14:20 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90339">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/18e2b0b1c0.mp4?token=TL5aL77GD2dozUAD3Pp-Q_TkUQSKKcZuaDdBbEG11Z_3CZ0RLaG8dlc_kCDOIcF2yNCRuIDUYlqaAWehCTktxi71LAH_jB9CIz88Y4XLpzdzw0vHM36Y7qkT1LQHAM7uYsWN07-wvGwE42V6SKhDJHT3K1EzrgofIbaxVG_sYEKlRZLxyt2OzVxKFV-JFcJnUr3UXKNEAqGlBsALYGR1Y2iqPwxNmihbHEi4-cA16bxIHu5sEMeHrYSeH-mrOoy315SjvnA3tix2pWcWu6Wklcvf5-HAnQsd17Q1MfoBqweTeTdHAXudCx6YYShgR_vrHa8mfAMQ3wr_i4iHSgwzPw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/18e2b0b1c0.mp4?token=TL5aL77GD2dozUAD3Pp-Q_TkUQSKKcZuaDdBbEG11Z_3CZ0RLaG8dlc_kCDOIcF2yNCRuIDUYlqaAWehCTktxi71LAH_jB9CIz88Y4XLpzdzw0vHM36Y7qkT1LQHAM7uYsWN07-wvGwE42V6SKhDJHT3K1EzrgofIbaxVG_sYEKlRZLxyt2OzVxKFV-JFcJnUr3UXKNEAqGlBsALYGR1Y2iqPwxNmihbHEi4-cA16bxIHu5sEMeHrYSeH-mrOoy315SjvnA3tix2pWcWu6Wklcvf5-HAnQsd17Q1MfoBqweTeTdHAXudCx6YYShgR_vrHa8mfAMQ3wr_i4iHSgwzPw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پيش بينى فرزاد آشوبى از عملكرد تيم ملى ايران
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.29K · <a href="https://t.me/Futball180TV/90339" target="_blank">📅 13:55 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90338">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bFyxN4Y3aGoJYAG0ITXVGRjItb97GXNAURJpOX52zI6qXXWiPO-jRQzrKref1IS4HtQ-q4Eyzv8NBF6ABSKbEaxQi-ALHsz8XwtVZfPuDvlVtrDlrD14ODyXzOTHXcLrB5smw6fwFZsjDxLUPXpAhFTpMx_yeS7VWnRxyDGUGnjQIqMBVMYWr582TRiYmu6A_Q_hj-14sWZLsTwouaCp_68p2FJxesIlP7GCG0E8lJ_SlvVkH4B5qZkboO8segrllMtEz6YxVeK1N7ffzdUIe406ZLiKsI4u53YX0PhWuSv-tUp7Bevp9qVrCIvxMD21QF5wsT40ze8LFgyrmkAJww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در ۱۱ ژوئیه، ممکن است شاهد پرتماشاگرترین بازی در تاریخ جهانی باشیم.
🌍
اگر هر دو تیم آرژانتین و پرتغال صدرنشین گروه‌های خود شوند و تا مراحل پایانی ادامه دهند، طرفداران شاهد رویارویی نهایی بین کریستیانو رونالدو و لیونل مسی در مرحله یک‌چهارم نهایی جام جهانی خواهند بود.
🤯
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.65K · <a href="https://t.me/Futball180TV/90338" target="_blank">📅 13:32 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90337">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jkq23cUzjqdR9w6Eir9XLOiCsfZeHQnjFZPmC4KlxqyUIP9Ig8x_ET63QuEVtau4x1P61tFhjIaXbKEmAyQyiG8zqEA9NgY69Uxobvk7jwhP5jMhp0kA6pdg-wH9piugNtKOo1kd3za3Q66l49YfwHukCRMnJWhaQWOihY-f1hppQ7Mg84kNSZTh1uhLVTkXEAR8Y33_xf6i5MN5kOXMYFGYWH5GBMnRuFGKmBAdtp--nQgWdR9w0d0xP9AVjQ89q7kWrVE9cjw9GQgsDni87C5QnKkcm8ZJ5XOacHUhMfP2_zFDBA9JLwrpqRwWV27SpAcp8cmXI4X_KEvrU4nO6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شماره ده‌های تاریخ تیم‌ملی برزیل در جام‌جهانی
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.48K · <a href="https://t.me/Futball180TV/90337" target="_blank">📅 13:31 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90336">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/31f588b63d.mp4?token=gdNwZFMgf8Rg1TRTTMKuHXe-sKnWK-IBahAHZxf1YQ6g318S_bfs31jKskMpls3tuqZtfFRziZeHBphK0VKxfQkkrtafaTZBdUBvLWmrHRcRa5wJn8H_sC2uJlTdK0HPsbtK-EZtLglJk5CxHnEJ7E8nPHLTNEMx4Z2WrPBK8ZuB-UfjJcp55zwYmWyGf52zMYKMEHeXCs6-rsILaUqJZ7eB6lAJ7PnhpNlWf1Ye4DJ6Q3D6Va3w-5bVnsNqmiCJBXA26yRPOVhAUpfvfjo5TRcG32EnfjSuonWjdp-keX56_9bD11BrI4ERlM5H0ciszks3OlTihzgkBNJdzIHa9w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/31f588b63d.mp4?token=gdNwZFMgf8Rg1TRTTMKuHXe-sKnWK-IBahAHZxf1YQ6g318S_bfs31jKskMpls3tuqZtfFRziZeHBphK0VKxfQkkrtafaTZBdUBvLWmrHRcRa5wJn8H_sC2uJlTdK0HPsbtK-EZtLglJk5CxHnEJ7E8nPHLTNEMx4Z2WrPBK8ZuB-UfjJcp55zwYmWyGf52zMYKMEHeXCs6-rsILaUqJZ7eB6lAJ7PnhpNlWf1Ye4DJ6Q3D6Va3w-5bVnsNqmiCJBXA26yRPOVhAUpfvfjo5TRcG32EnfjSuonWjdp-keX56_9bD11BrI4ERlM5H0ciszks3OlTihzgkBNJdzIHa9w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترکیب منتخب سهراب برای حضور در جام جهانی
👀
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.58K · <a href="https://t.me/Futball180TV/90336" target="_blank">📅 13:21 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90334">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">🚨
🚨
🚨
🚨
اولین پیشنهاد بارسلونا برای جذب آلوارز رقم ۹۰ میلیون یورو به علاوه آپشن‌ها خواهد بود. لاپورتا قصد داره قبل جام‌جهانی این بازیکن رو جذب کنه
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.53K · <a href="https://t.me/Futball180TV/90334" target="_blank">📅 13:04 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90333">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
#فوری از فابریزیو رومانو :  بارسلونا در حال آماده‌سازی اولین پیشنهاد رسمی برای خولیان آلوارز است که به زودی ارسال خواهد شد؛ هیچ بازیکنی در آن گنجانده نشده است.  خولیان پس از رد قرارداد جدید ماه‌ها پیش، به اتلتیکو اطلاع داد که تمایل به ترک این تیم دارد.…</div>
<div class="tg-footer">👁️ 9.8K · <a href="https://t.me/Futball180TV/90333" target="_blank">📅 13:00 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90332">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aqrSVKr5CWjynmOFt7cgyKTaPYREaS9XI57grwShCWyeRKiC6cYUQCL8o3P_slgw-n4c5-yCiS1ONi7EPRGFHrQ3fQAgflS-XFDGhm-r0SgLG7qfgrw1eyzkFx9S3XdUYB5uhkzuQbOzqTOcOoKzy8wj0fJdM6MBhntC7D7bVPRyLAeTx76EG_rFf2aTYMgof8aN5wOWWJNfmtIjgmnsI1QOBj5Z-gt2mZIFsX2NvvVBKOrIzOXEyw2XMxE6lW5NAKZGrtNhJ46uUUL3LkvEhH4vxPYzrSyn0y9AQQjMExhsWFX2XzZIL-oUJ2DyK5YWyX12b6DUC6Yu9IWQ2MEm_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
#فوری
از فابریزیو رومانو :
بارسلونا در حال آماده‌سازی اولین پیشنهاد رسمی برای خولیان آلوارز است که به زودی ارسال خواهد شد؛ هیچ بازیکنی در آن گنجانده نشده است.
خولیان پس از رد قرارداد جدید ماه‌ها پیش، به اتلتیکو اطلاع داد که تمایل به ترک این تیم دارد.
پس از ملاقات مستقیم با مدیربرنامه‌ها و واسطه‌ها، بارسا پیشنهادی ارسال خواهد کرد.
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/Futball180TV/90332" target="_blank">📅 12:52 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90331">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/858ae0e82d.mp4?token=pM21OkO-wqPlGyoKl276A-B7A9EOgpoqOM7SCOZ_3ZzO2wexyxm4BzQhITQ0c-cL6Ofw8o2q-qhghvUbdo0CHqtE127pTNCBz6z9ZBkhrtGqe4Ktf-CwMlXGzdmqJT07TtMv5gP76ODgOzulU8yRNVK0XfaNyX3Rspy9UhfYP0i3AX7FXg16uV35uXOULaTJjMGjA9rPzhBRpuGPeJNU7DmTiwNrRiw0zpPm0HTpAnIjIet0aBnNrX1xdBVkKdur3-X56CEtPGnO1_GYHx0I5-VjzDp35BL4xH4Kac3rc5KAp0SK44ZHpVSZv7F63PnNHpP0hkOH8XkUDHxz0vldaA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/858ae0e82d.mp4?token=pM21OkO-wqPlGyoKl276A-B7A9EOgpoqOM7SCOZ_3ZzO2wexyxm4BzQhITQ0c-cL6Ofw8o2q-qhghvUbdo0CHqtE127pTNCBz6z9ZBkhrtGqe4Ktf-CwMlXGzdmqJT07TtMv5gP76ODgOzulU8yRNVK0XfaNyX3Rspy9UhfYP0i3AX7FXg16uV35uXOULaTJjMGjA9rPzhBRpuGPeJNU7DmTiwNrRiw0zpPm0HTpAnIjIet0aBnNrX1xdBVkKdur3-X56CEtPGnO1_GYHx0I5-VjzDp35BL4xH4Kac3rc5KAp0SK44ZHpVSZv7F63PnNHpP0hkOH8XkUDHxz0vldaA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اینترنت بین الملل وصل شد!
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.46K · <a href="https://t.me/Futball180TV/90331" target="_blank">📅 12:35 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90330">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">👍
👍
#اختصاصی #وینرو :
✅
ثبت نام کن
🤩
🤩
🤩
هزارتومان شارژ بی قیدوشرط بگیر!
💵
💬
به مدت محدود
📣
😮
تنها سایتی که با عضویت بدون  واریز 500,000 تومان شارژ بی قیدو شرط میده #وینرو هست
💰
👑
#معتبرترین سایت ایرانی
⬇️
🌐
Winro.io
🌐
Winro.io
📱
کانال اخبار و هدایا r7…</div>
<div class="tg-footer">👁️ 9.18K · <a href="https://t.me/Futball180TV/90330" target="_blank">📅 12:35 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90329">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pdDXXFMpB3twd6F9qcISJUgV2YOkIIh90sy9CyG9vehkL0n4GKYU0VwLCZBuR_EKjEOX9S_1xSgXEDRRudUxfXNuII6WzxQN7tWNSbVaulXf9grVf-05CmJFHCpZCOG5KPx6ajCkr5B6-1hCEkqgVcOfjpPEVz5YuXlR1AGMWEppWQZrvl1FHi76CpQszRnTsLWEaMqUhuMgYBSP9kqvVOlJrj60Kfvnm8A2pBNyfHWnF_n3JWyyc_NvxKl_WJA_AnsvFVFYzMcpA-8CNY9s-Kah26AWqYz89I0UsMZx363YaE5ut2BW5rkOgvt58nWdAqI3pDoM2Hgxz100rflP9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👍
👍
#اختصاصی
#وینرو
:
✅
ثبت نام کن
🤩
🤩
🤩
هزارتومان شارژ بی قیدوشرط بگیر!
💵
💬
به مدت محدود
📣
😮
تنها سایتی که با عضویت بدو
ن
واریز
500,000 تومان شارژ
بی قیدو شرط
میده
#وینرو
هست
💰
👑
#معتبرترین
سایت ایرانی
⬇️
🌐
Winro.io
🌐
Winro.io
📱
کانال اخبار و هدایا r7
🎁
📱
@winro_io</div>
<div class="tg-footer">👁️ 9.47K · <a href="https://t.me/Futball180TV/90329" target="_blank">📅 12:35 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90328">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/97ac0d5890.mp4?token=YTYJrEv7cZNJG5VcnnumcRcbB12Zs1GuK8jbAmLnDSVMMYolpJ49wd0HhhdJTKEbjMEG85ySkHdTJaNIy401ZQP1vkameL5nM1keFFwUZI7zwyN-7p8_cDF4ZyeAXfonb5Mm0PV0G7078s1N4JjPSbMjxSN_jvoffszzR7nUqT4_hp73wHAZ6rqumbbwNiMYI9mmfKmg_DgSPjTkc41FeV2d8P4yXYoFP8uz8FGled8yXiWBySEnYFSlwc9SvbfdLQYWUKFGeN4iuosAHW__KU3bpfENCJMs9QX63jYA1L1LvHAY99Nc2aaVoQku1sEfqrWzk8NmtfOzSBNJh3ft3A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/97ac0d5890.mp4?token=YTYJrEv7cZNJG5VcnnumcRcbB12Zs1GuK8jbAmLnDSVMMYolpJ49wd0HhhdJTKEbjMEG85ySkHdTJaNIy401ZQP1vkameL5nM1keFFwUZI7zwyN-7p8_cDF4ZyeAXfonb5Mm0PV0G7078s1N4JjPSbMjxSN_jvoffszzR7nUqT4_hp73wHAZ6rqumbbwNiMYI9mmfKmg_DgSPjTkc41FeV2d8P4yXYoFP8uz8FGled8yXiWBySEnYFSlwc9SvbfdLQYWUKFGeN4iuosAHW__KU3bpfENCJMs9QX63jYA1L1LvHAY99Nc2aaVoQku1sEfqrWzk8NmtfOzSBNJh3ft3A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بازگشت لامین‌یامال به تمرینات اسپانیا برای حضور در جام‌جهانی فوتبال
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.12K · <a href="https://t.me/Futball180TV/90328" target="_blank">📅 12:15 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90327">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WJhSaAb7ziiEHhfw2_YdMHkHG1bFR56vECrch6UGYrKX2oNeAjmy3MhHVU1_pwPjcjSS583NO3APUpHnWR3D6R5vE3lIDbHKDOt4G468iGkvHvqQZ5cwrLOa9-R5yUZY7a49iqacY76UOP-s7GwNHbItlLdDNT0isZcqN6s61joFemtBWKsdlV0eyM1dEE3Wibq3ExfdDdOUtxKkwnxioomPOlpncU_-wYCGuJhtP0Lp4ns_Vg6502UN19HdwFlcBDKs6AEYe4d_W9TPnb24Q8hJsmKyK-ePbC3U_1kafOWmCJ70nvercz_cUKACV9YGUkI_gPPDIsPixkm3s1AVbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بیشترین حضور توی سطح اول فوتبال انگلیس
آرسنال تنها تیم بدون سقوط
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.78K · <a href="https://t.me/Futball180TV/90327" target="_blank">📅 11:50 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90326">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2e24e703cf.mp4?token=WZ0s0fTzoO7gFKD1eLIlI_XFxN4VyLWs5wpyZEEd3H869l2-dveo_NV5YXMny6J17DiPP_amCKIsxZ-VgnlPZfYSgrvQlx4fQ_4HztsKhZi8nZgy-Q1Joh5YSFCaubHzFJswbsBW6TbefcCjnR6znlUgVluWYkTuVYP0_40VmzjqZChi-kOM6tdB60J8bHK-N7ZrZmdj1HMPyUOBpglpPgPZxvoSGKf6jcawAho4pDJnmGMbwv1sp7UIZmpwEEsTQJCvFN83AvdX9fI-m_xQTDlXNMt76kfgG55Bai1gUyh5wE3MrYMroG_k0oiAV0oP_qn9KBeoZ-KcyB-2NiTMyQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2e24e703cf.mp4?token=WZ0s0fTzoO7gFKD1eLIlI_XFxN4VyLWs5wpyZEEd3H869l2-dveo_NV5YXMny6J17DiPP_amCKIsxZ-VgnlPZfYSgrvQlx4fQ_4HztsKhZi8nZgy-Q1Joh5YSFCaubHzFJswbsBW6TbefcCjnR6znlUgVluWYkTuVYP0_40VmzjqZChi-kOM6tdB60J8bHK-N7ZrZmdj1HMPyUOBpglpPgPZxvoSGKf6jcawAho4pDJnmGMbwv1sp7UIZmpwEEsTQJCvFN83AvdX9fI-m_xQTDlXNMt76kfgG55Bai1gUyh5wE3MrYMroG_k0oiAV0oP_qn9KBeoZ-KcyB-2NiTMyQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">«تازه خارجیش رو بهتر بلده ..»
😂
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.96K · <a href="https://t.me/Futball180TV/90326" target="_blank">📅 11:25 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90325">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">🔷
#اختصاصی_فوتبال‌180
؛ مونیرالحدادی و یاسر‌آسانی دو ستاره خارجی استقلال برای ادامه حضور در آبی‌پوشان خواستار افزایش دستمزد و پرداخت به موقع حقوق خود شده‌اند. سیاست مدیریت فعلی استقلال بر حفظ این دو بازیکن است زیرا پیدا کردن نفرات جایگزین در شرایط بسته‌بودن پنجره نقل‌وانتقالات عملا سخت و غیرممکن است. قرار است پس از جام‌جهانی و مشخص شدن تکلیف لیگ‌برتر، جلسات ویژه‌ای با نمایندگان این دوبازیکن برای ادامه حضور در جمع آبی‌پوشان برگزار شود
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.59K · <a href="https://t.me/Futball180TV/90325" target="_blank">📅 11:24 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90324">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rxaaxEk3p82le40iFMOx9ISLAUyMl5khaYWR5icNZ2adCSOCJDFNwMYF1CF89BDK-eN54cEDNDxc12atVzwuf7eHNxAR2th3ZIM4YEIMHVhSF49sp-op_nDeOOK4XfgfFqgj8DdILMiUM2LamwYsekRYBuyC-AomjAQJr32Ilo6RkL20D1TKszXCPV-kmDJB9nGVRMRoy5g4H9R6eWXoFUI2jcPgxt43XuYh5YRdkV-xl9RgPo5ku-94XWPQbqcYF3tulxN4tso4YeEdgdr9pKLV7Myev9P_dJidd1dcKPxdZhf3hipGAUesA6Lc4JPK7yhrAudleYWwZUQkajMqiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
شب‌گذشته دیدار مهمی بین سران باشگاه بارسلونا و وکلای خولیان آلوارز برگزار شده است. این بازیکن شدیدا خواهان خروج از اتلتیکومادرید و پیوستن به بارسلونا است
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.04K · <a href="https://t.me/Futball180TV/90324" target="_blank">📅 11:20 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90323">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZNnM7zZpL-vXBHwMB8jHMbKgKJUtm7fS-s9S5tCYys95-Q9SAXisnaO-b12mcsxMtJDdTM-f-wzBjBw0NX88s7tIbYPlmbYM0XiVw9elRtyE3APKXLuS0KG3aaQUqNVduWLRujzQ6b5O9Ajj8VxOrfq3DV3rwZ4ljLv34rcSqriy0zlt94AxW4jUwcnZHEb7L7h0G72Sq52RluD5K0Nb1bJXoT_7ZOT_hPg4c5lurowLO4yMplnJlb_mls3MX7tYLZM-s0e7Cxuk1HsH1nXkIp9MZ7cSbzKkljwB1hWg-autxDlN98-3qG3rSc6cBUdRWHe5n4kcC3J20eZXqubRlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بهترین گلزنان تاریخ‌فوتبال برزیل
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.73K · <a href="https://t.me/Futball180TV/90323" target="_blank">📅 11:04 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90322">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/40f4a1291c.mp4?token=t37iWqIwhsBtLPoNznfCpx0n1uu39gqDuQbAilsNzSpO0yCg0Naf-Y31r55629mtd75KqdX5DJjDVB5KVKr3l9aoSfPh3-EoDIRzOWQFLgKa0JUWDAY6VZWFlawjTBja6zy8weN53kF8c9o6NS2ATT750z2Y_0jwhFGCuT_wO3F8FuWjTRK0C-aKNeYS9xqjszWhmODDurYhSbkLkf3aUraSEoYlGgMLM8JGHaJd-wZ9laE0ZhuiKNPp7AvlbnInD6Wq7Jh7Bt6xoprJbW05iUxHoDto1dSHMNlH8R2yi7SPuaOi7H3Q_rN4MWs0-6T3_8qEuxSyEMQ51a2_ERVuRS-NftlkCPQKqs0adIH9-R6nx5D5aT4zkCqnFneKBqJuWcTx9LBbtUEYRBZynIBc5hnvkC_aohF4gmPumZQgQRkPH4sOfVCJ7CF_rt9EUacoSwmDJrr6o6754l5CvhgVhdIAk62eS9JhDqp2_7_uokymxOoATy8I6l5OwrlCdrH218Gd69Ha7k_Yj6ZnoNojbj_YQquBhTUktA3Z7pcqTaeCU5mdPDZJqjPC9XcY2TfjhtzG3Lz5NMwGkW8KmeYPa3KqrW45kyK38m87JKEBG8k-8yfJ9fjaw-WzjBMyD2HgJq3veI5bfFJuqKc-Ocq3AlYBUb4FbVBIsCJRLNLntQQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/40f4a1291c.mp4?token=t37iWqIwhsBtLPoNznfCpx0n1uu39gqDuQbAilsNzSpO0yCg0Naf-Y31r55629mtd75KqdX5DJjDVB5KVKr3l9aoSfPh3-EoDIRzOWQFLgKa0JUWDAY6VZWFlawjTBja6zy8weN53kF8c9o6NS2ATT750z2Y_0jwhFGCuT_wO3F8FuWjTRK0C-aKNeYS9xqjszWhmODDurYhSbkLkf3aUraSEoYlGgMLM8JGHaJd-wZ9laE0ZhuiKNPp7AvlbnInD6Wq7Jh7Bt6xoprJbW05iUxHoDto1dSHMNlH8R2yi7SPuaOi7H3Q_rN4MWs0-6T3_8qEuxSyEMQ51a2_ERVuRS-NftlkCPQKqs0adIH9-R6nx5D5aT4zkCqnFneKBqJuWcTx9LBbtUEYRBZynIBc5hnvkC_aohF4gmPumZQgQRkPH4sOfVCJ7CF_rt9EUacoSwmDJrr6o6754l5CvhgVhdIAk62eS9JhDqp2_7_uokymxOoATy8I6l5OwrlCdrH218Gd69Ha7k_Yj6ZnoNojbj_YQquBhTUktA3Z7pcqTaeCU5mdPDZJqjPC9XcY2TfjhtzG3Lz5NMwGkW8KmeYPa3KqrW45kyK38m87JKEBG8k-8yfJ9fjaw-WzjBMyD2HgJq3veI5bfFJuqKc-Ocq3AlYBUb4FbVBIsCJRLNLntQQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یکی از عجیب‌ترین وقت‌کشی‌های تاریخ
😂
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.76K · <a href="https://t.me/Futball180TV/90322" target="_blank">📅 10:35 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90321">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/txN6JiZEyrhxUdR3jplFCLHxGpwDWsqkWyB4xJrVO1o9RjgFpgDR8KVjJhf_C9WA7jxgyzoh9_cS-j0tFo-jJD21XYyw-ivZa1YsY8FeWwWsvOizWjKo3QyytYt_eyf94tARuFDP0Kc9ENK037VamdXuZKMGJ7xNhSpSIQg0QY02CsRmFg7eY5GMvcsJ4y5ZAWdq4_wTsla3_1A0oPEqwAlykibmAhaqjlMGYOEykocuqyXeew6oqzgKGQesOz47bMhwhewlukIbvLylqaE969RvgAA7bCVZdW6H_xlc1QOqST7AsvWse3LAxoi-WWZcaEtgeeRymYW-z3dUrk-KnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
فیلیپه‌لوئیز سرمربی جوان برزیلی هدایت تیم فوتبال موناکو را برعهده گرفت
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.24K · <a href="https://t.me/Futball180TV/90321" target="_blank">📅 10:21 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90320">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/njm0193h0GBAWTL_w-wMhf8VeXspC7k4EqIxWnAiSlsju-h5mK_0ti8jAy5zFOnR_2ezGbAV0drrit16X-qXc6TrVpUeAKlZmx5hEcke2d0k3xESTm4-BY6VkogffYvxxpMCThQNL6IooYSNZGQNPlya0xmDg_dF28_cr102aqaVzpZYq5MUx7L5PEXHTVd6fxBhS7lHJTmXfSStcVv5aV4GkUMRLvJHyTU7UhQz3POOc6qTghf74BNeWZnejbR5Bu8gLHK4WxPCyuzKD1Jq3FORJDVhLO8jV2B0iHJp1iMMt980TBGdL74VSKmvEhjGcAPw6SiQ1txL3euUapdeOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسپانسرهای پیراهن تیم‌های حاضر در جام‌جهانی
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.01K · <a href="https://t.me/Futball180TV/90320" target="_blank">📅 10:10 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90319">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/49f9845215.mp4?token=Higc6-I9oXt4iG-YOSWS2k777yB9yfoUG3sIZ5w8nQdhqkUZsVrkBuisx1RvMI5XHj68YmzJQw3FoX_7FtFyk5D855A7HLbqYqmuYZx1MrwX8Em2mQ3qAJ17wtNDrFm3JtJGPpFWnMlXmKjg_58KECg36krKmLD6kX5b2xOwzpRBof_N_w78fZld36TlT9n2EYBOV5O8iaiBHAEZoSHbNa9k4Wc0MD7grQOnVsfvmF5_TM8fw_rBoHyjRliU-K1QRqz-Gic1HsPnyG9Ckv7eQlVBXluls0b-p2sTgGXqSquj37c33yHYpf79YHOfXbeaFYpNrXLa76yZzLLkj17MKXlt71BvPbsGPPRsboiCnoHHWcUGsEAxl8VC76wOCeWJdbdy-hVSrhM920QGSbkFrKahw4HSp5SarsFb2y8pAP2-Not0icf4QkSLqp-UBPyOlI0mqguCMoraLCytULpeiShj5OOnbA5QQAZUb_1d3k9Ff1qBJrS9jbL_yp0dFGPTQ8O3XqvBW7wRzh5PVwpN3n0nkjL7qtKmp6JHf3W1CZ2nTs30_1lMIzO7f0Osqu2OaK9erZHGV9m-O2D1Z2FcWTgtl074xFwplaHe_uxiDKAnEk6I7Y6RuPDBkTT7VUOt8aA9EDwYBQ1qoN6yMGFK-n1mAUfeKQQ61jFlGZ8CdZY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/49f9845215.mp4?token=Higc6-I9oXt4iG-YOSWS2k777yB9yfoUG3sIZ5w8nQdhqkUZsVrkBuisx1RvMI5XHj68YmzJQw3FoX_7FtFyk5D855A7HLbqYqmuYZx1MrwX8Em2mQ3qAJ17wtNDrFm3JtJGPpFWnMlXmKjg_58KECg36krKmLD6kX5b2xOwzpRBof_N_w78fZld36TlT9n2EYBOV5O8iaiBHAEZoSHbNa9k4Wc0MD7grQOnVsfvmF5_TM8fw_rBoHyjRliU-K1QRqz-Gic1HsPnyG9Ckv7eQlVBXluls0b-p2sTgGXqSquj37c33yHYpf79YHOfXbeaFYpNrXLa76yZzLLkj17MKXlt71BvPbsGPPRsboiCnoHHWcUGsEAxl8VC76wOCeWJdbdy-hVSrhM920QGSbkFrKahw4HSp5SarsFb2y8pAP2-Not0icf4QkSLqp-UBPyOlI0mqguCMoraLCytULpeiShj5OOnbA5QQAZUb_1d3k9Ff1qBJrS9jbL_yp0dFGPTQ8O3XqvBW7wRzh5PVwpN3n0nkjL7qtKmp6JHf3W1CZ2nTs30_1lMIzO7f0Osqu2OaK9erZHGV9m-O2D1Z2FcWTgtl074xFwplaHe_uxiDKAnEk6I7Y6RuPDBkTT7VUOt8aA9EDwYBQ1qoN6yMGFK-n1mAUfeKQQ61jFlGZ8CdZY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">برزیل و هواداران جذابش در جام‌جهانی
🔥
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.08K · <a href="https://t.me/Futball180TV/90319" target="_blank">📅 09:45 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90318">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T-tzbO_IFHf8u1dVRjHKjudaQuxOU2a-H13RtimPxThje6QPN3XX7Azeg2FeBemdtwutdqDFiqcEBkDTMJd2o2sVQNDWwxLlIxk7lFRztXDsrgmXI_51KlYVR2YsA2YHg4xv3tIw-bIZLekUYC4Z8xjsqSZBU4vbiqa-15KSjl6yBQvmbbwlju8GHYUAjUz-fJedPe9h1bAG7QDWlKkbnEUlqulqjFLj0QF22Hfo9o7-jO5722a_sab-j-z0wJUM17y8ynArmEwQCWFqPJnLnF-OCBv01c4hIoYmFA12TgZyuGaoZuxxxM_Kb-8dWhqf0n1lgya-cimOGHfDmL6SSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پرافتخارترین تیم‌های ملی تاریخ فوتبال جهان
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.18K · <a href="https://t.me/Futball180TV/90318" target="_blank">📅 09:20 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90317">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e84afd40a9.mp4?token=GY0lauXs2WMFWTnrDGtuU1OPEjBhASnx1ibgDVNQbuX2wij32q7B8lpcbqJRmyyKYb0cVAICA7oDO0g1LK6tnl9orAoHevKFk3R1BHCxZPFcCVgc0MY0WVIpbwRuJtMfh8A0MqW6NqRLJfSnvME_Jc_eVesbStEaliQzx7IxYm1LhxuQBJEtKp1CX0Fuz_3ubwD8OFRdqtWGhW4RYYUGiIX3ePjIZ39kl1KVmIBtR0Oen4_WOMS30AhrkZ9x7n4Y-IcSVfFgtXww00Dr621dyM8aadsCVweuMJLATCWHqr50dXeMFL8xDLcMUJ5y3GCjjRGHryeNyPATYjIK-mPDDj7nd05y64eqSQK4_RxY549vRF1dTxN-j_uXyTSMWroRBcH3Aew_qcso4UTIZcRZXIDvcnP_Wzu1KA2NFX3jE43WTBmUHyivzibEQJDX-0-HMY9P5UTbUs51aUJ_tHw9jrENPDwbFT4c3fZJOj01XbhXikNMagUc907F47pHJF0WubuuEYJh_Qbp7wqNB90eAarlyx_ohgiw6dPOAW-NQV8XNGoq4QuJyIiHMY68xoukRKGLnhyxNV5elE_2fOX7j7QoSkRVIteGmHCDkTHbNsGgKc52B5Jj5jX5wEwDz5Yh_U_xWz5XsSrcW-htm86a3Ivh8I3dLJspj9k0ppe9blo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e84afd40a9.mp4?token=GY0lauXs2WMFWTnrDGtuU1OPEjBhASnx1ibgDVNQbuX2wij32q7B8lpcbqJRmyyKYb0cVAICA7oDO0g1LK6tnl9orAoHevKFk3R1BHCxZPFcCVgc0MY0WVIpbwRuJtMfh8A0MqW6NqRLJfSnvME_Jc_eVesbStEaliQzx7IxYm1LhxuQBJEtKp1CX0Fuz_3ubwD8OFRdqtWGhW4RYYUGiIX3ePjIZ39kl1KVmIBtR0Oen4_WOMS30AhrkZ9x7n4Y-IcSVfFgtXww00Dr621dyM8aadsCVweuMJLATCWHqr50dXeMFL8xDLcMUJ5y3GCjjRGHryeNyPATYjIK-mPDDj7nd05y64eqSQK4_RxY549vRF1dTxN-j_uXyTSMWroRBcH3Aew_qcso4UTIZcRZXIDvcnP_Wzu1KA2NFX3jE43WTBmUHyivzibEQJDX-0-HMY9P5UTbUs51aUJ_tHw9jrENPDwbFT4c3fZJOj01XbhXikNMagUc907F47pHJF0WubuuEYJh_Qbp7wqNB90eAarlyx_ohgiw6dPOAW-NQV8XNGoq4QuJyIiHMY68xoukRKGLnhyxNV5elE_2fOX7j7QoSkRVIteGmHCDkTHbNsGgKc52B5Jj5jX5wEwDz5Yh_U_xWz5XsSrcW-htm86a3Ivh8I3dLJspj9k0ppe9blo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">از جذاب‌ترین هواداران کشورهای حاضر در جام‌جهانی بدون شک کلمبیا هستن
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.8K · <a href="https://t.me/Futball180TV/90317" target="_blank">📅 08:55 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90316">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4c6e129bd0.mp4?token=qjEb2kOkszOTTtktXJ_fsv8dbVjrXeI59r8U_eUbkJYIEsHzHwCQ27kA_03bpEkbQcyupBLlw2275oFlZf_uGwxEq3ZGmnkCxiPNpG4hyyl5iSInMFM5IuDg9TRUe2iJN862olIAQN3WTqi2q-lo1HIKsiBMwAeifHC6ddN-K33Mb2Q1JhS8PUd1BhC-4Y8gvJt_KUeBqJ0L8goZCll0JhDolD3ZW4a43vmrsMCIRMK5eoV6wzLcAIr-ex_iS5yiOGkKNi9ySuPFA58654NWHV6GRPCQuHbX8TE7uz0RqpfCYZDp9dKXlLcPnbibqF9ILCU5gQaPpUJkBYLfASdKPgfzDkBDorv0emIKEMFqu_Azgl01XcVj0cyfLNGvjOWauZZLpLsMyP1Z3R14SkMMf3Kd82fjF1tsAxnbuJpLu5Dp5KKroJv2fgfxoNAZXJi6QPOtqQePExWK0yKyH4bW_8nvSfURNIUnmZR1-0c1KXjLBLWaPt1SEZgx5l8AulZMx2vB28p1MbWnyTELH0l7xHzi_RZD43Jwj3h5FTEVfFAusAQJmCCp_roPhzmAiTahkXcfkbeQECFI7QglV4B31JMqhW2WxN9rK-R8j-PwM9SxVw5upsVZpfW3dY-MPMHW7lS04Xx0c2GS1ZVQZyxj1n7PDQgkMCKpMOQt7JhtN2w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4c6e129bd0.mp4?token=qjEb2kOkszOTTtktXJ_fsv8dbVjrXeI59r8U_eUbkJYIEsHzHwCQ27kA_03bpEkbQcyupBLlw2275oFlZf_uGwxEq3ZGmnkCxiPNpG4hyyl5iSInMFM5IuDg9TRUe2iJN862olIAQN3WTqi2q-lo1HIKsiBMwAeifHC6ddN-K33Mb2Q1JhS8PUd1BhC-4Y8gvJt_KUeBqJ0L8goZCll0JhDolD3ZW4a43vmrsMCIRMK5eoV6wzLcAIr-ex_iS5yiOGkKNi9ySuPFA58654NWHV6GRPCQuHbX8TE7uz0RqpfCYZDp9dKXlLcPnbibqF9ILCU5gQaPpUJkBYLfASdKPgfzDkBDorv0emIKEMFqu_Azgl01XcVj0cyfLNGvjOWauZZLpLsMyP1Z3R14SkMMf3Kd82fjF1tsAxnbuJpLu5Dp5KKroJv2fgfxoNAZXJi6QPOtqQePExWK0yKyH4bW_8nvSfURNIUnmZR1-0c1KXjLBLWaPt1SEZgx5l8AulZMx2vB28p1MbWnyTELH0l7xHzi_RZD43Jwj3h5FTEVfFAusAQJmCCp_roPhzmAiTahkXcfkbeQECFI7QglV4B31JMqhW2WxN9rK-R8j-PwM9SxVw5upsVZpfW3dY-MPMHW7lS04Xx0c2GS1ZVQZyxj1n7PDQgkMCKpMOQt7JhtN2w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">علی لطیفی پیشکسوت فوتبال: کی روش شارلاتان بود، پول می گرفت و بازیکن دعوت می کرد!
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.71K · <a href="https://t.me/Futball180TV/90316" target="_blank">📅 08:31 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90315">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🎯
شانستو #رایگان امتحان کن
⚠️
🤔
میدونستی توی #وینرو میتونی  رایگان شرط ببندی؟
👍
تنها کاری که باید بکنی اینه که عضو سایتش بشید و
🤩
🤩
🤩
هزارتومان جایزه بگیرید بدون نیاز به واریز
💖
تنها سایت مورد اعتماد ما با بونوس های کاملا واقعی و رویایی:
🌐
Winro.io
🌐
Winro.io…</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/Futball180TV/90315" target="_blank">📅 01:14 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90313">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QFBGWfbsmH2X--9Tf6XXoZFCJ2ixvTQ_ez9TxGmZV_ifilpwNOwcqD6ULGJsdWZk9-_taUXpPGl5_PcMYyHrYfulQUmlKz8dox8JtCsiND6lCRSX6cDPy5b3ExjwMBuE5y-tnnEdG_DU7-pdQjfHz1t9GE6p_5SGcHcqPSwraEw1BJxS1zEh52LQO_lOkCFF4CEwwqxF-RCa_XNazkx4qABedBQykNZJAdglIuRfbuMv0bE0ggdXZXx4gEvsZiSbbCu-iwtq8H6myq4RPSQKZaaEQzHQGCL70DIidr1ODFeIyBKxclEWbmBUNpduMzlCjukLR_q9ERUAMy3mSz8btQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎯
شانستو
#رایگان
امتحان کن
⚠️
🤔
میدونستی توی
#وینرو
میتونی  رایگان شرط ببندی؟
👍
تنها کاری که باید بکنی اینه که عضو سایتش بشید و
🤩
🤩
🤩
هزارتومان جایزه بگیرید بدون نیاز به واریز
💖
تنها سایت مورد اعتماد ما با بونوس های کاملا واقعی و رویایی:
🌐
Winro.io
🌐
Winro.io
کانال بونوس های رایگان
a6
📱
@winro_io</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/Futball180TV/90313" target="_blank">📅 01:13 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90312">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qRzMJReUmk8hwMRfWCy8xSvYXoZ6KaSGxdiQwN5cRaAKq4Sqvt9jZPk_n1atP-ncz7s_ScO6Xvp8atB14bZ8GgmDkpUCieR5ZEZs_TI0hwqO8JtI1imWZ-Ur3j45Iub9Oj1ypEbrOymUaTvfjoNboNNEOejz38pJqxgvnLe4uJiKwM79kAeyNkmzvDN8t9pWormPb4AQsgTQ2UskFFXii_efGyU5s47gOeeNEyGFJN_bA8AM7T_dddP9V4EdgiXdMRWuEVgaDsrCPrYG5mzUL0il5mE_KO8W63Sva12upOexZ9GZxwrcldJfr8V2Tt-6wYLabqE1L1pB9jBN53XWsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تیم‌فوتبال کریستال‌پالاس قهرمان لیگ‌کنفرانس شد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/Futball180TV/90312" target="_blank">📅 01:12 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90311">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aAc81RRyjuVoidZHMTmEXwJXhRd6SICxPzzINra_MBHHT58BQ-vC6kPoKGdyRtbD97LUSureFU2PGsxdlvjRFA8EggUQThW1JEj26nXRdAxqvDHrcfAVucATn8f9pwSenTZ6dqKBbpRsRrxEPc_1sPRyQXfbl_tB4n_ST_gS8G49GCnObt9vWwUiEtcZHhUFXutq1z7LaIsO9dQZLI8xZpUz-bhEDfEoQx066Vmf3u80qIWIPJMt5i2n6f3SJ7clqxirF4L2RN0il1vs3m5vtnVes62PUUCyFQ5DTeM_PsTHoqU0XkPVMiBussZSTKpD7-Rc2rImjf8iRb6hpjlxnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کافو تنها بازیکن تاریخ فوتبال است که توانسته سه دوره به فینال جام‌جهانی دست‌یابد. حالا لیونل‌مسی و امباپه این فرصت را دارند که در کنار کافو تاریخ‌ساز شوند
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/Futball180TV/90311" target="_blank">📅 23:55 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90310">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🚨
🚨
برخی اخبار کاربران گویا این است که سرویس گوگل‌پلی درحال‌حاضر رفع فیلتر شده است
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/Futball180TV/90310" target="_blank">📅 23:30 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90309">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l4BuwOmX5Q5hXdTzQJWh-J_RJgAf5JTQy7dw4YIepMpum9XXgOQw3HD0o67z5ILG-DzWoPYfrdBGbH0b8k8B9_u8U41zDh3qkTE4p_onJ5LoWlQVsTfqcg0uj8rITQC6oP1_1QWfo7c28dzx5GsHH66_HPyMDPHuQx_FWmmVZQwZd2ci6-IRvsI2M-AU_TmNhx_M1YbSvT9Htt8vBnWSA-xFUaof9Wc5bEhm_3dlctlM5lUuKFYb-vqp6Jw3rna2pO7gBNo2ER_xoE1q_mqCULdccTeIUqPeKxCPYchLAkw9_9mmI7gVzTNFCJsc-ez0Y3pBRCLMS0LXGvxVIQBv-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عملکرد تاریخی اسطوره فوتبال مردان و زنان بارسا
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/Futball180TV/90309" target="_blank">📅 23:25 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90308">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W3evZK2281CBnBTeIzi5ZTiv3wdHSp5MH1pFnlFuLelmBDa1gjJvtt5IoMwpfsT-yp74Zd1ejUvmDG_mE6s_C7Gh_shh02lDwWur0W4vBH7yCcPjojVxqRygOxjBWTATMec8Ouhf78WTWW12yp6EEvPiupHR4Y0TQxnmUj7ohbm06P_zmxkX-JClgVzfkGfX-uGcM2l-ZPody6NGGmpFjfnCa-nyK9QtIq47QlyF8Z7HAeQuJLjb2XFuz4N6gpXRlCVpPadSa-O3UDWR1gFfcaixDR-e-fBRUFSbWUpV5Barnu3bZR3MosHP9LDRAyWgwL4gNfUA4U-6QZPxkTpxtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎁
گردونه شگفت‌انگیز جام جهانی
🏆
⏩
با پیش‌بینی رقابت‌های ورزشی و بازی‌های کازینویی، مراحل هفتگی «گردونه شگفت‌انگیز» ویژه جام جهانی را تکمیل کرده و هر هفته تا دو چرخش دریافت کنید.
اطلاعات بیش‌تر و قوانین:
🔗
bfrd.link/WCW
🌐
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
💻
@BetForward</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/Futball180TV/90308" target="_blank">📅 23:25 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90307">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/84204a485b.mp4?token=FNiHnsJ9tejIJH450uUiGl_vn409uzHytbHYk0qgqTjyX5jIO5QqmNVT5k-nQ2VK7dedbh0skW7xB9bcu2QB73QsRJC9hnb5ZLxgMusDjMsZP3gSKnJsMdvqOnbtGyjgTuoZwZTA53sGOO3DmpATbU98Pg-tkJM4UE4EzJENJN-rg-3TDZ-wvRvYfYuGNFxwErXbStcGTVfBwGbrpvFV3WPdZrfW0AmAyiud-Ma4qpnJHMlBo-wzhuTA2GD0fHUZvEmomT6Uy6D2i2thpyPW1C5o1GSq1w64z0Dvk39CztF4_RpDe8NpnDPb01JVGTh-Ayl2sM7XtZpntjpsz-KdDw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/84204a485b.mp4?token=FNiHnsJ9tejIJH450uUiGl_vn409uzHytbHYk0qgqTjyX5jIO5QqmNVT5k-nQ2VK7dedbh0skW7xB9bcu2QB73QsRJC9hnb5ZLxgMusDjMsZP3gSKnJsMdvqOnbtGyjgTuoZwZTA53sGOO3DmpATbU98Pg-tkJM4UE4EzJENJN-rg-3TDZ-wvRvYfYuGNFxwErXbStcGTVfBwGbrpvFV3WPdZrfW0AmAyiud-Ma4qpnJHMlBo-wzhuTA2GD0fHUZvEmomT6Uy6D2i2thpyPW1C5o1GSq1w64z0Dvk39CztF4_RpDe8NpnDPb01JVGTh-Ayl2sM7XtZpntjpsz-KdDw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">امیر قلعه‌نویی به سبک لوئیز انریکه درحال هدایت شاگردانش برای جام‌جهانی فوتبال!
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/Futball180TV/90307" target="_blank">📅 23:05 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90306">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fa7TUkEfvWd3apo-jfpcfv5fovppJLiM8nRVN8bJW5JGowgQHYCHeAP8JfP4UOWqAFGE-EZa9RB-45SOUGnbTZjI1SA0qWUwhT7VnD9SQ2JovCoc7BBV46N7nFEEVguFx0h_cFet_wh_g2Qmdv605plb6aBnJsVDJKSZH0Q7rz9OAdzuxTxnxpkrues-OwdALcR7gqmnnjEqGB849543FRvUtqsI7zQGmsYm6EUfx2_qnv0qw8au7i_h37ehUIcngLBADc6A3LloJhiPfCPtxcA_n8NG3Po_UmS3PO_TtzxZimocEw8RU8wVMskPyxuZWitCjAuMA87YwwGFi34A3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اندی رابرتسون ستاره خط‌دفاعی لیورپول با عقد قراردادی به عنوان بازیکن آزاد به تاتنهام پیوست
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.97K · <a href="https://t.me/Futball180TV/90306" target="_blank">📅 22:58 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90305">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/80080a6ded.mp4?token=hEuIBkcw_KhUmWPz7qRaLsyXfrT5OEsUdGRu54Yjr0b7rMu2x90GrPHAiIY4TFfdx5ELdsnrrXY_qtXWkOlZN7lhyDVvWPwObVY1mSy-00yMUW3LnZaKZXLYNVFB5g20XtWoTyflqSYcENLO3PuJvyYLSQPMRV1yEOmCLe1FSmkJ9xUqhkoVPG9h5OZo4mN_Kbl1BK6MX9Oxvg5o9K40w4RGc8KjKoLnBeiK-d9rMVJISpGstOf6AXbOoAHpFxR0P8BGaWL7UdnqTYjBwyNGzu0XQ8imHkABBVK_yNBgQ_P3XgS3KetgHyMPpilYdRlwqx9f0xk1hWjUtHMI2Hy3zA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/80080a6ded.mp4?token=hEuIBkcw_KhUmWPz7qRaLsyXfrT5OEsUdGRu54Yjr0b7rMu2x90GrPHAiIY4TFfdx5ELdsnrrXY_qtXWkOlZN7lhyDVvWPwObVY1mSy-00yMUW3LnZaKZXLYNVFB5g20XtWoTyflqSYcENLO3PuJvyYLSQPMRV1yEOmCLe1FSmkJ9xUqhkoVPG9h5OZo4mN_Kbl1BK6MX9Oxvg5o9K40w4RGc8KjKoLnBeiK-d9rMVJISpGstOf6AXbOoAHpFxR0P8BGaWL7UdnqTYjBwyNGzu0XQ8imHkABBVK_yNBgQ_P3XgS3KetgHyMPpilYdRlwqx9f0xk1hWjUtHMI2Hy3zA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جنگ هادی‌چوپان با رقبایش برای عکس گرفتن با آرنولد در رقابت‌های اوهایو!!
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.93K · <a href="https://t.me/Futball180TV/90305" target="_blank">📅 22:40 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90304">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/35b0dae947.mp4?token=uSKvF1pAkWivot-Bq5-2hpjxtpgGnWhnn7FPgmz7-CiMxx6IzpO0Lo3qDBz0IYjmidLZHifeAXq9MHhdUF9hb3eTAIAd7iRnWsrsryWlaj78eszSYJtPAbQeAfMPWRnO5HDXvsFNuUAqz3L-oGiAVoNvrs15SpuvAkIFAOJYYrW6m_kvjdp_MkU9ZQDw0XUE1LEGGPo-RkjLWIrIimgkLVj1ZpL0Qg_kLZqgGzqVwg-ALon2zToeXuXg1GU71jpZCxE3DtqtRrZzm9tC8bJ4_LOM-yvx7jRU96D2fB426E9ZZf5J7F8BvcWtQzl4a5wQBa-4RF_Reie8-XPSN1mJuQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/35b0dae947.mp4?token=uSKvF1pAkWivot-Bq5-2hpjxtpgGnWhnn7FPgmz7-CiMxx6IzpO0Lo3qDBz0IYjmidLZHifeAXq9MHhdUF9hb3eTAIAd7iRnWsrsryWlaj78eszSYJtPAbQeAfMPWRnO5HDXvsFNuUAqz3L-oGiAVoNvrs15SpuvAkIFAOJYYrW6m_kvjdp_MkU9ZQDw0XUE1LEGGPo-RkjLWIrIimgkLVj1ZpL0Qg_kLZqgGzqVwg-ALon2zToeXuXg1GU71jpZCxE3DtqtRrZzm9tC8bJ4_LOM-yvx7jRU96D2fB426E9ZZf5J7F8BvcWtQzl4a5wQBa-4RF_Reie8-XPSN1mJuQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حق‌ترین جمله‌ای که درباره وضعیت فعلی میشه گفت:
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/Futball180TV/90304" target="_blank">📅 22:15 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90303">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/05aa244672.mp4?token=S5Bs8B989P8yOojO8GbbWbghTAEu4aaZzoJD6ra8K01MTocVPRfR5GNriR_skic3uhwocElBE1EqqOYYnz3_GdGpMVz4EdUKmDlSdd-ZM8ydPrBXV4K59ZkG0f-4WGJf6QSEVpAAoTUQaNW31H9VlYQsdQ6Mtm6gwvln6S9SMhyx1zdFjwqYXV9OnQYtIhzDKp5vI6j4WiTY3TiVykxj2JesRO6qvbmD57_AIseQ9cxdpuQs4z0j7OqdSNjXqfonY2viXSdclueiwQVJxHsVp2hJkFi_qnt3IJ2vZzCd1eaIXJ8UTkYtBpMdzzMADcfdsWqDQHyDfeGxDKlSKhGHMA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/05aa244672.mp4?token=S5Bs8B989P8yOojO8GbbWbghTAEu4aaZzoJD6ra8K01MTocVPRfR5GNriR_skic3uhwocElBE1EqqOYYnz3_GdGpMVz4EdUKmDlSdd-ZM8ydPrBXV4K59ZkG0f-4WGJf6QSEVpAAoTUQaNW31H9VlYQsdQ6Mtm6gwvln6S9SMhyx1zdFjwqYXV9OnQYtIhzDKp5vI6j4WiTY3TiVykxj2JesRO6qvbmD57_AIseQ9cxdpuQs4z0j7OqdSNjXqfonY2viXSdclueiwQVJxHsVp2hJkFi_qnt3IJ2vZzCd1eaIXJ8UTkYtBpMdzzMADcfdsWqDQHyDfeGxDKlSKhGHMA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دنیا برای آخرین جام جهانی شما آماده نیست.
💔
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/Futball180TV/90303" target="_blank">📅 21:50 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90302">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q4o8T6ZJ8CxDmgMQcgs8tv8_xMluHB75gpCxIZPDdKkLRWwigyQjpGFgkGf-LbxumZTBPBTYeQwvKUJE4SKW1Jta56NsecSUSvu03am2WCfEQcVeLagSDLufp-OrT9hiCU1nT6gW6X490JyPBEnDMr5HvZbUHyfH7FwWbO5NEt8WE75kOYcg4MA_rq0bqMfN8EpLkrn7NeXh6QE_MJPa-3hO0CrxSKGuYF4PifQY2M1-D8xtWXrHffIHUMVgG6yn2ge1tDs7f8_dU4hjlMiDq5R9H0ehBlMeDj97W-XAkYbEFpqY5DwJI62uJUiZMtgMw2EbyqGkS3_lvNGwsVdMPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
#غیررسمی
؛ آنتونی گوردون با عقد قراردادی به ارزش ۷۰ میلیون یورو از نیوکاسل به بارسلونا پیوست
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/Futball180TV/90302" target="_blank">📅 21:28 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90301">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b45e4bbf26.mp4?token=S99dRgoI3huik69F-WtFQEzJcvsocLnIxNSAHZZs3gltsR1NmwaqHEbvCrDxw17eqF2Kq42t_-m2j6XbUeLM9tW8FxJG_6SFWFXq8MrKZuqnV3TCxPjt_ZspiIqYU14QPo2xpu19y_wCZKZU5Xv4Cp7XcXA4AV3YTEl1vuc3qWCtwiowxnp7t7bdxFHm7NSS6CE-zrebR8AYu22bARQJo4749WnVq5mNqae7CKc1V38IesAXhQpfUOWhq89Pva6vrqKDpWI1XQNYpha3xUS1DBMJJFJKNqIZl_16D_F86idial7hvlITOWtEhH0B3mLN2dyzHLoFpQAjeM0CwN0rHg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b45e4bbf26.mp4?token=S99dRgoI3huik69F-WtFQEzJcvsocLnIxNSAHZZs3gltsR1NmwaqHEbvCrDxw17eqF2Kq42t_-m2j6XbUeLM9tW8FxJG_6SFWFXq8MrKZuqnV3TCxPjt_ZspiIqYU14QPo2xpu19y_wCZKZU5Xv4Cp7XcXA4AV3YTEl1vuc3qWCtwiowxnp7t7bdxFHm7NSS6CE-zrebR8AYu22bARQJo4749WnVq5mNqae7CKc1V38IesAXhQpfUOWhq89Pva6vrqKDpWI1XQNYpha3xUS1DBMJJFJKNqIZl_16D_F86idial7hvlITOWtEhH0B3mLN2dyzHLoFpQAjeM0CwN0rHg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چالش جنجالى و جالب مجری با محمد نوری پيشكسوت باشگاه استقلال
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/Futball180TV/90301" target="_blank">📅 21:25 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90300">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZHqWingGh9C-Bl57gAmoOHEgynPz6yxeJIrxt24uyJApD0NEufQAl7r_GNtxNX2mDLgblbmmjxC8WphURwTJHMDX9OoRlUjy7QVS8nm_7dUTOhTyvR1_AcDzXX5ASMXCKUlcp78JMrqoJ96l6-FmqrZ0ZnCsLlZwiW9w1mKY7fwvZu2B2v_v19fQn189S3nXny5xph0koA5eEXC6vT8Sa8Yx_po0M5T1FAUnIxKh0O6DVboenD5vNbNnwDqS3MardAyCaa_ICyZ0rYSomC4H2LbiOU0tFylHt2cnWoMd2a_qOUx4dGL9IQjnxf2q0fdALSt1T8u3GkrSOB3MMG5bUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شات‌تاریخی از مراسم جدایی الکس‌پوتیاس ستاره تاریخ فوتبال زنان بارسلونا
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/Futball180TV/90300" target="_blank">📅 21:02 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90299">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WP3DORUbVtIrtd4Zv2J3n4khQPCOcl9DdCnMl0yBR317G9ek3FAXk_E5v9y7IfGv_mHym0Eepu5t9_nX7t4jdKHRmAPx2kx4X5xhLx4alnDfnWyU-wtB1V_SiqMwdLwdjWwZXzPkWQSZg5d8LD8CFnNvU43ejpyKAr1J-WcIq8l-GivBLGxU9Q6h80vIoqHb-CDABpaGfvoxSuHMzncnYx3IQX-TcpRrqk53bX-A-beyfin5ACBkHMgw5YdRB1htarHTmQlnF5GlWxdUKyRGcHvdoJVOeAMWBpVaMnqNpTYqLdEadqXXtOojWcg8VSJ9AyhKZ-VstPtC1kc0np3ubQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قهرمانان تاریخ لیگ‌کنفرانس اروپا به مناسبت فینال امشب این‌فصل از رقابت‌ها
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/Futball180TV/90299" target="_blank">📅 20:35 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90298">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/57a28e2aed.mp4?token=sVHnwJYyz9FnirZ9uzFL7jrgvzd_d84i7FmtWrGt2OY4s711iKGyuK22xLnhLEPIXthVSJQqBxGklTTS8OeTR-FRFXN5uEn1IdErQQOqkI13tnMq3-QxiSccEu5ZeRndFYM6X1okAVS0G8X0z5NYq0LKfamFjLWTtlSpeFmdK4S09qQHimOX0jGw9Txdb4tceeDw69YORaQr9n9-l9ox-HuHVRcbVcCFxKAC4qTzurEoir00Pp3Srvxb1iakY4XNEb3JulLBR6aT_ufhrNiTer3Dtk0720iNYZ9UiI23-SET-E4YSz8WLcEw7jeh-M3isk0F7-12aqwh06r3-whWdQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/57a28e2aed.mp4?token=sVHnwJYyz9FnirZ9uzFL7jrgvzd_d84i7FmtWrGt2OY4s711iKGyuK22xLnhLEPIXthVSJQqBxGklTTS8OeTR-FRFXN5uEn1IdErQQOqkI13tnMq3-QxiSccEu5ZeRndFYM6X1okAVS0G8X0z5NYq0LKfamFjLWTtlSpeFmdK4S09qQHimOX0jGw9Txdb4tceeDw69YORaQr9n9-l9ox-HuHVRcbVcCFxKAC4qTzurEoir00Pp3Srvxb1iakY4XNEb3JulLBR6aT_ufhrNiTer3Dtk0720iNYZ9UiI23-SET-E4YSz8WLcEw7jeh-M3isk0F7-12aqwh06r3-whWdQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حمله عجیب مجری پرسپولیس صداوسیما به سروش رفیعی: پرسپولیس باید یقه بازیکنی را بگیرد که حال نداشت بازی کند
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/Futball180TV/90298" target="_blank">📅 20:10 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90297">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8ac28b3311.mp4?token=HUMmamHSt7VZjXwAtHlQhvVy6sKD_whs3fYW9afGrUmWmDlAv-3SFY6P-m9OWPIVwMi76IuGgbra5pyN-Xxw4Sinvqdo_sj_0AUb3aMWWfB_55RjqTMZOyZU8Uep_HO8kdnhZPYL6mSOeuSxxy189W8AgofwxMcECbW_Q70cOi7ivw86Bwmqb7irR-pLAbSfSmpx4g-d5hGtBIysvn-QCFHMgxwkAfkY0f3i3ADNjGtkk0QXp8QjYqclJp6_TZMDfOFZTRkvIGaFzZt8bDEX6NERnEl1bse_AMVXi0Xz3znKGFEmlGKqtkgnqyluWT4JFjo1m7OsVZDXKKdq5XuCTw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8ac28b3311.mp4?token=HUMmamHSt7VZjXwAtHlQhvVy6sKD_whs3fYW9afGrUmWmDlAv-3SFY6P-m9OWPIVwMi76IuGgbra5pyN-Xxw4Sinvqdo_sj_0AUb3aMWWfB_55RjqTMZOyZU8Uep_HO8kdnhZPYL6mSOeuSxxy189W8AgofwxMcECbW_Q70cOi7ivw86Bwmqb7irR-pLAbSfSmpx4g-d5hGtBIysvn-QCFHMgxwkAfkY0f3i3ADNjGtkk0QXp8QjYqclJp6_TZMDfOFZTRkvIGaFzZt8bDEX6NERnEl1bse_AMVXi0Xz3znKGFEmlGKqtkgnqyluWT4JFjo1m7OsVZDXKKdq5XuCTw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">استقبال شیک نمایندگان آمریکا از تیم‌ملی عربستان در بدو ورود به این کشور برای جام‌جهانی
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/Futball180TV/90297" target="_blank">📅 19:35 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90296">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e4496fe5fe.mp4?token=iPvnXp4ibGQvA2nBkIRT0iQyNig3eeRrYwaChYg41FnFOdlfny5-_Z3kCcXkzTlkThaB1t1hd-oOY8logpAcbvItCbOyUATJKGEFktbcUgCuDH2aTmy9NroVFM2XpJY3hS-ae5Tk8caKZMj4jKZpIZie1z-FOKABZyJ-CrRa9tJRp9Gffokf10Y_o4XtKeglKCU8bExw-P2pVofSaWbgfqkGvHx5_MA2QY6YkmH3czPRpea9RrynYLxyIFOoLNhlkhOi-s6ClPyhtLHTtl-U2-viLgDBYvwm_SQVm7gY4K132fcaovoYx9wWFs1X10gOgt-ot3FCNwEkd_fBAOF2EQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e4496fe5fe.mp4?token=iPvnXp4ibGQvA2nBkIRT0iQyNig3eeRrYwaChYg41FnFOdlfny5-_Z3kCcXkzTlkThaB1t1hd-oOY8logpAcbvItCbOyUATJKGEFktbcUgCuDH2aTmy9NroVFM2XpJY3hS-ae5Tk8caKZMj4jKZpIZie1z-FOKABZyJ-CrRa9tJRp9Gffokf10Y_o4XtKeglKCU8bExw-P2pVofSaWbgfqkGvHx5_MA2QY6YkmH3czPRpea9RrynYLxyIFOoLNhlkhOi-s6ClPyhtLHTtl-U2-viLgDBYvwm_SQVm7gY4K132fcaovoYx9wWFs1X10gOgt-ot3FCNwEkd_fBAOF2EQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حضور نیمار در اردوی‌تیم‌ملی برزیل با بالگرد شخصی
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/Futball180TV/90296" target="_blank">📅 19:23 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90295">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Pa5_HqhBvuRJza_rA9moP8ya69udPPft9zQJ1v3ZPpM59wNEsQW563UB3j1lt6RgkyDoalkFh_gzzcM-S-gGwaoLazXXjcHDOki1Z8sQYFPhR84C_M2fWtJqnsjD2vErvp8L8TTUGCol7xMxo51dCi_vAgyLftOF_i5m684kz51Dek5Ko74BLoRQwJe9ZtNIR21BR_qCcU00ClEWz2FhIrRHv8uRrqeAUTU-X6MfEwM_o1AQxMbSj8zMmluCSzJNG34Mbw75SHRjU4A-1QJZO2nk_E3U-SPbxzUX4nnXPxi-T8lfECitLf-bYECi_KPLCZa1Knof8M6hZf5LZXsyqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
جیکوبز خبرنگار مطرح اروپایی: چلسی برای فروش انزو فرناندز درخواست ۱۲۰ میلیون یورو از رئال‌مادرید که جدی‌ترین مشتری وی است، داشته!
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.75K · <a href="https://t.me/Futball180TV/90295" target="_blank">📅 19:15 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90294">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5c0fba26b8.mp4?token=V_4y3vUIg-HxiN_lJHSXxPL0kAfZcaUJGnCo9axUL1vznzrbUkbQO7lbVTFkorLmfOzN8VyFzj3h43nDCOR4aBo0jOZWAj4j-_1GN2AQx8n3-sb4Z6dY-by8gEzf-KdA8tVxAOeRh5umImRO53GuzbMAm7pO05lSGWKU0VYJ0QR9Rq3FT9MASD60ugDckad0vmZb88L7wOrbL278_3xfIP64uN5qSUbaMIOjMGDRSYniGvc6epZoatVCvh46N3HSHj7q48RKL9ZNKK1Q1pBjlp85KOg-j1BwWvL2mflAZ_z-EJnqz80vWxeSkAslZxi6SZ4nlPBqlVEvLjAeJcZuAEkP1YA8hQY0dgW47-Dp0w0HISukDkQjipWxMa1weEsOBIpusJKoMIqzDJ1VjzeemmVTI4_Nolo0LnRMznF1RG1M2Ci2Dzk2TzEM10FYrbxamPsThJ68OuT_dNbKh4cdwjVRNDEMCCNl-hVN0iBxqNlcqN7LSacAkk-AiSoASvpBZ7yVCDwhdyWONi1sqJFwSxHtYUvlpNZlhtpvkx4tPxfMdtfRv7KfbcTIA0E06IFAaXmWBsRgY0tiYORNhKMG-iK45ATIqqoF50Uir_SXmc-A0t15xT40_GaHIfbwl6I4f3oMpj57RAFzqvBbjyBAqbKuRrSg_fGwmeCuTeNW0BQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5c0fba26b8.mp4?token=V_4y3vUIg-HxiN_lJHSXxPL0kAfZcaUJGnCo9axUL1vznzrbUkbQO7lbVTFkorLmfOzN8VyFzj3h43nDCOR4aBo0jOZWAj4j-_1GN2AQx8n3-sb4Z6dY-by8gEzf-KdA8tVxAOeRh5umImRO53GuzbMAm7pO05lSGWKU0VYJ0QR9Rq3FT9MASD60ugDckad0vmZb88L7wOrbL278_3xfIP64uN5qSUbaMIOjMGDRSYniGvc6epZoatVCvh46N3HSHj7q48RKL9ZNKK1Q1pBjlp85KOg-j1BwWvL2mflAZ_z-EJnqz80vWxeSkAslZxi6SZ4nlPBqlVEvLjAeJcZuAEkP1YA8hQY0dgW47-Dp0w0HISukDkQjipWxMa1weEsOBIpusJKoMIqzDJ1VjzeemmVTI4_Nolo0LnRMznF1RG1M2Ci2Dzk2TzEM10FYrbxamPsThJ68OuT_dNbKh4cdwjVRNDEMCCNl-hVN0iBxqNlcqN7LSacAkk-AiSoASvpBZ7yVCDwhdyWONi1sqJFwSxHtYUvlpNZlhtpvkx4tPxfMdtfRv7KfbcTIA0E06IFAaXmWBsRgY0tiYORNhKMG-iK45ATIqqoF50Uir_SXmc-A0t15xT40_GaHIfbwl6I4f3oMpj57RAFzqvBbjyBAqbKuRrSg_fGwmeCuTeNW0BQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ماجرای بازداشت نیکبخت در پارتی شبانه؛ این همه آدم معروف آن‌شب آن‌جا بودند چرا فقط چسبیدید به علی نیکبخت؟ گفتم نفرینت می‌کنم یک روز جای من زندگی کنی ببینی جنبه‌اش را داری!
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.6K · <a href="https://t.me/Futball180TV/90294" target="_blank">📅 18:55 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90293">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jyHih2zFqIa3ZSVT4z-Ou0PPCjH5YYWJrfAuEdg5_ldHbQOhnNui8a0hYo9RkAdW1AaGcMDasn_YjNzXBqo9q4hrDVTWKSoeqleq2I--MWzGUIYF2USU_WoYiBMa1NeHJ5YfCTkzla7h67cLleMjefSQt8VOxe7LOgOWBbWYbQgtMf4whVNtvS2Yc4dWzK6gAasF64DH63o_wcsrcqTNQNUlbrqC6NwBMgppN8hHfftaHx8KVEFb_8HS_MT7ij8mSumR08bYVkPAxgvRnXs7RlrYqP5jpPzg_J_rygSIa0xiIp_fzx7IzNiT5vJp69x9aG3jgFGMUxzGTmlajnXZtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بهترین هتریک‌های تاریخ ستارگان فوتبال
😂
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.45K · <a href="https://t.me/Futball180TV/90293" target="_blank">📅 18:28 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90292">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">⭕️
تا حالا بدون واریزی روی فوتبال ها شرط بستی؟!
🎉
500 هزارتومن بونوس رایگان فقط با ثبت نام بدون هیچگونه واریزی!
💳
شارژ سریع و امن با درگاه ریالی ، تتر یا ترون فقط با یک کلیک!
⌛
پشتیبانی 24 ساعته
💖
تنها سایت مورد اعتماد ما با بونوس های کاملا واقعی و رویایی:…</div>
<div class="tg-footer">👁️ 9.02K · <a href="https://t.me/Futball180TV/90292" target="_blank">📅 18:28 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90291">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IuUMZhztKdnE3uEdxQM1WtaSQe_6wmGIA7I4HKQXwaLQg1tCtuS5QBpKa90T0q1hpc5NuUhQWFI-tabv9P--M__dBmXXwOkWyQZikW337Bqfy685Q7B-_LCHgucfumCyOAdLWYToHl9c7CblnK2ThvFARP8ZlLKDwUhk57fOntMSoDdD3ykEbNmiT3vJk0zA0yPqKk2vPkyfsYyWaW3IJSAtMmi1E9GgUkn468zb1O4kaonjZDiCxjGdRYrf5k0sTvAMZhmQli8eNIbN5XTRd31CRBPVX9WYOHVjiaki0UXbLLjLn80ByNQ1ojdoIkiIBLs5vhgu3rgvhJA-LyELZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
تا حالا بدون واریزی روی فوتبال ها شرط بستی؟!
🎉
500 هزارتومن بونوس رایگان فقط با ثبت نام بدون هیچگونه واریزی!
💳
شارژ سریع و امن با درگاه ریالی ، تتر یا ترون فقط با یک کلیک!
⌛
پشتیبانی 24 ساعته
💖
تنها سایت مورد اعتماد ما با بونوس های کاملا واقعی و رویایی:
🌐
Winro.io
🌐
Winro.io
کانال بونوس های رایگان
g6
📱
@winro_io</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/Futball180TV/90291" target="_blank">📅 18:28 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90290">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bB-okmGSYVNkbZaYoSFKyOT4n9D50NWVIXaCmXsKkSwXCanO6VGBVOGU8vq48PjaEA9gQeXto3JukBpAx9xJEkQT74MNnxS72X07eaU3oUJw5DLaAu7Li9kf9mIX7vW_HDD18KQg_yp2GCIxvhx7lgaROx2zyLcMnfgZbBp5wRWf023BLQJBd-wXazehJr-_R9yz5jCqU430_RySG9V3m3ymiK0n6JZ8KwYHHl3PTjQwfZEulbY4-gwskg859Da_xD3tGIBj-He-FhYis5dhmbL4HeJIWFTd9QsPT8FItK5fY8GQd75cbPV6W6t7Ha0gNN7TjW2e63LwJ-oP3FRWLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تمامی قهرمانان جام‌جهانی در یک نگاه
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.4K · <a href="https://t.me/Futball180TV/90290" target="_blank">📅 18:05 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90289">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D0Aw0GAx_wMVpYjuzUIluLBq-81glVjRqZa7NCy0DdWtdQE1oh9TcXtUUYycC_SGQJH0qJ8-WUjKx9dMDC3Kc36Wc9VZyHQPOIrV7Mh3N7xPoS-Qv43PqAiPBuOmIvPfL9VYUs6zloljBQr6Lf7vNb2hNVCCg0KLIVGSBdHpWhHCyxp2VCcXxonmvjyXye38lPBkKn9ngUjQoqNT7eupz24YdToWeqE53NYCbOOreMilpkoIeBZsKmgG4HAIyyVkKxqqiMapV75pIFcNkM3gUNtRM5vqwvb0VC4N0lp6xCdK3hkuos-unf5S2gW539gy9ftqTDoAccMHgBow_zESUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
به گفته اکثر منابع خبری، قرارداد آنتونی گوردون با بارسلونا تا ساعاتی دیگر نهایی خواهد شد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.9K · <a href="https://t.me/Futball180TV/90289" target="_blank">📅 17:36 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90288">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JJ9ej8U-cFgY3go5WfHI2XYBmb8_qQH57PGQOrDMlYMfpmlWEzdIsZxxCNO1yse0PI6cdQ4wLvIs0EnQxa7JBdAtfXg-yR_jrwqeuz1eX7gVy4CP55a9JFTlmXvTwL2SL9aBb-Ite53Kmu2pviv_8sbbJR7O3nDs8amxBhDWO-UvEqCxqJtdDk4EKn_EfIBV8pW-ui8EAxPIxiFL4ywj1nvza1Mw-2g024YkdtrlOPOqWo3AyweuX7KkMmmLRnTngBNqm1RpSCzLGBL1cWoZ1XkzkLwzOSysp0Yeby-5reGEvtHgg_ElzoykFqbtB-l17gPhOBC0YXa7xStCk3d6kA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مقایسه میزان بازدید پست معروف جام‌جهانی با پست اخیر نیمار در صفحه شخصی‌اش
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.73K · <a href="https://t.me/Futball180TV/90288" target="_blank">📅 17:15 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90287">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E0dGDFmcLx1G__wi9hCmdRX-Meb_Huv2D_VAeoP9slSiUM_9inG-TCJ23VCGATWN10t4fh7UKK4Ynde5P7EK4y9nXahWV4i1h0L_1zH3xFS8CDhlGGmW_Klh4ZBNqLR-PuMP82PRTxsdAsS45yl-a6quS1NvZp7nYnUlbgUNgu3g1IctVi53QuH8d_2KjCK6IsIt3eUHBJIrckXG5CmMWnuvWZQuN3OQZhapW2Mft3GDL4XIxczCM1NRRs-vvkitD-AHa4W7buKxew3jixacI0GghIi2SdN-XOzrBqdfBgqZ-xLrEc6TEzkL9tlbCDrUQOyuRi-MRKPe5O7N0WrJNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
جرارد رومرو: بارسلونا قصد داره قبل از جام‌جهانی قرارداد گوردون رو نهایی کنه و سپس به آرامی در طول تابستان مذاکرات با آلوارز و اتلتیکومادرید رو جلو ببره
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.93K · <a href="https://t.me/Futball180TV/90287" target="_blank">📅 16:54 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90286">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/30945cae67.mp4?token=W3cJZB3DIqE7DJq1lijhwuvQGPdw90UranUaPO-hKf735yYu94jX-i1b6n0YYGPeHd1if7PtsgBBz1QIXHYZEWDhcBtoo6bIY3KCz5FtB_Bp0Vuoq27kq0R3j6kb5Z8a5yUJuUs-GKVQ5Bqdco4NBRDDQXHrkS7z9vprM7R6SowubiotLAHNxr1ztWlAOAq6jgqzzFkMWjnJ22IXNYoVDxMfNkBs2YwnSI00eRVNUAlKkDmp5R5HdxeSpQlVc9X3eFaWjTq_HlsnVXWIvNLvZKQF_bDoFa5Ds3fDl9HMvBJyvGLoUk8jcUQOiA46ajDHjFJQYDFqZ7FULCnsYjX5ag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/30945cae67.mp4?token=W3cJZB3DIqE7DJq1lijhwuvQGPdw90UranUaPO-hKf735yYu94jX-i1b6n0YYGPeHd1if7PtsgBBz1QIXHYZEWDhcBtoo6bIY3KCz5FtB_Bp0Vuoq27kq0R3j6kb5Z8a5yUJuUs-GKVQ5Bqdco4NBRDDQXHrkS7z9vprM7R6SowubiotLAHNxr1ztWlAOAq6jgqzzFkMWjnJ22IXNYoVDxMfNkBs2YwnSI00eRVNUAlKkDmp5R5HdxeSpQlVc9X3eFaWjTq_HlsnVXWIvNLvZKQF_bDoFa5Ds3fDl9HMvBJyvGLoUk8jcUQOiA46ajDHjFJQYDFqZ7FULCnsYjX5ag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">از حواشی بامزه مراسم خداحافظی باشکوه پپ با سیتیزن‌ها
😂
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.85K · <a href="https://t.me/Futball180TV/90286" target="_blank">📅 16:50 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90285">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7c42b3ba26.mp4?token=W69jEUa6Wnf8OWkE-hbAOBZytd3Zpo8T8fj5YkvKSSIsVazJbrXrEFPwpjH0btCmfZNODNN-zEloTOclwhm-S6-6pUwicbiCwHUzHgoUwlQ3zaVH5PsmLJ1UsWWl_h6gEXkokP7w7ACSbbByfXgXAeNnkapLuUMcEzn2YF2EXyNZ_KgwnA3MRRPwYJlaq2YZ2Y2d4R2eUJHkJZdAsOM4671v9xov94RFRIn7X-2pm_uwEQTmz5SAPAX0nHbc1E2Ysc4Syj68wDItcGs9P7zgq8uHjnaQXTg7Ozw1qAXYqShWCHBnXQZhDN9LjAEpfZAWJ9DR47suXHB38z1u553Cjw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7c42b3ba26.mp4?token=W69jEUa6Wnf8OWkE-hbAOBZytd3Zpo8T8fj5YkvKSSIsVazJbrXrEFPwpjH0btCmfZNODNN-zEloTOclwhm-S6-6pUwicbiCwHUzHgoUwlQ3zaVH5PsmLJ1UsWWl_h6gEXkokP7w7ACSbbByfXgXAeNnkapLuUMcEzn2YF2EXyNZ_KgwnA3MRRPwYJlaq2YZ2Y2d4R2eUJHkJZdAsOM4671v9xov94RFRIn7X-2pm_uwEQTmz5SAPAX0nHbc1E2Ysc4Syj68wDItcGs9P7zgq8uHjnaQXTg7Ozw1qAXYqShWCHBnXQZhDN9LjAEpfZAWJ9DR47suXHB38z1u553Cjw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آرتتا و همسرش در جشن قهرمانی آرسنال
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.62K · <a href="https://t.me/Futball180TV/90285" target="_blank">📅 16:25 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90284">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vb7BrmHdCVseP1KfdBW43tf5mjchwJS2YalSLv-zPavHKIWkbUXeFq75Ocuzo2OBuC3-ilnxSv7lFxmJypfLvREVF7f-z-Iu2fvkYx6KHRapDFsNyucSMQivkicGM-erAaFj9pyJr26HJVNggA-uGrKjKeKH7RcZaBfDCcZFGGJwF7J8lMsfwNlb3h7BOCt03M5_oK5TGJFZ1EIsGdhSNbspyrO5gPl2bH7XXaWzB6w9e8HCAR_0V-8SR7z_xDrgJQkJwdd_W3TlrHgxPleQYHF48Se3GxHlLl2HjcaRXs8XrexNfTktW3OiLy9xQFwpp3PFusf6KAI__3FluZpk8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
لیست تیم‌ملی هلند برای جام‌جهانی ۲۰۲۶
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.64K · <a href="https://t.me/Futball180TV/90284" target="_blank">📅 15:42 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90283">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sxzbK-j3McqpROnFZ1Y3rvX3Y2hwWmD5okvNXVVfK0fiGS8amxjstIl3gkAR9zf-m-fH4ZZHho4-bepPg5SS4PD8ouSF0YDB5GDFHWaRRMIdGIrmMC4r7udDlwMZC0giYUlCYBIkRT6CyAY3Aj-Yr9d0bwPzXqtD326uX-uNftyJc78VixlgAIZk4-SdVkkToz7TFHmYVj-VSWSxgO6s2Xj-5mqbmjvmjnz4_cVBYr-ul2cjj7n6dIUjY4dHx6aRBwgFy1_GJ4ncTCo432r46J0oOFjb1pDs2EtsoRkqZI8oNn7Yj0NAH9ti7x07rC27-lJS4kDOGR_XKjEOA8o3Aw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پنج سال گذشته: کریستیانو رونالدو ۵ عنوان کسب کرده است، در حالی که لیونل مسی به طور چشمگیری ۱۳ عنوان به دست آورده است.
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.07K · <a href="https://t.me/Futball180TV/90283" target="_blank">📅 15:37 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90282">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DMLYu9omOtbgpS-CvE2BFngDOL0WHV23QKQkYNaRbF0OAATFQmFz4G0D6itSwVtgs858Fsnldl-SZDyXD0ca-aTwrysyG-6_tREmKaM21dnhDqTyaBPHp0cGgliZ_dmf4UNmm8QWB7b7kb0j6sLk8OPENdWYPa3iMG6zRfMVcZMTniiJoWiXcQO_Nck11CnoyQdt3v1FLp74RulgHKlfX_lcbnQfN9JlbsfoBQX0btl0c6xPF6Pta1j_W33JwFFc47o3Tmz6yD7J47xWqz8bBK6vZBhF2PEJ21OmTwuv2_JYKJi7n7rvE0nS7FvNMfi26Xsr0M0MhPWzJrLQn7jXgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">180TV
🤩
🌐
دوست‌دختر جدید دوگلاس لوییس در عرض چند روز به ستاره اینستاگرام فوتبالی تبدیل شد.
👙
طرفداران نه تنها درباره رابطه عاشقانه این فوتبالیست‌، بلکه درباره عکس‌های نیمه‌برهنه این مدل ۱۹ ساله با مایو بحث می‌کنند.
1️⃣
جذاب‌ترین عکس‌های دوست‌دختر جدید این فوتبالیست در کانال ما قراردارد</div>
<div class="tg-footer">👁️ 8.75K · <a href="https://t.me/Futball180TV/90282" target="_blank">📅 15:37 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90281">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">آخرین وضعیت بازسازی ورزشگاه آزادی؛ 3.2 هزار میلیارد تومان دیگر بودجه نیاز است
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.99K · <a href="https://t.me/Futball180TV/90281" target="_blank">📅 15:35 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90280">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bbe3da6710.mp4?token=PyY4CFc5hOP5Jm2klbwah4LaQnsctRsXZNi5qAvB-QyjgFhcPx1FUFJWUWwq-FZ47CYViU_1U3vz9PxZqxR3JGsSdcjcTOM8u-FsyP20slkobce4b6R3RGuzJHP1ysSQjXPTW1PWnG1qJBCvOzqLbZ6jlUsB5QdW4zbZYDiX5xesbJwO3madtPj7AgN5wVPLWWYoN98flyTwX6OW5ejd9T5rYwOp4tpV4htgunCggjZ7OWEYN0DMNbTSvuGzp3-BG7QTMtce_EyFC8Gpuz1-5v1alHctItZSu1TL5yd3msOSiuoACumqk0HNvf1HuE5XinYyzsLd7JdJv8i17MKiAJlPo5A9vxodXFRx3ejv6j9Xygrdd0mbgD6zsM2M3cZZf04SGSS4CgLka-XfzBbToqjAEg35hq9W9bP_vPidjwREMsL-78Y455RobJNt6AasNUH4d-e4SaFNlLsC9eJj3coEBuDi-_cggFW3Z0djZxGFF54hg_sGwAs3uNjYIDfpev80-57lC3o6neFTbsgbKuJTLKyRe827xSSe03Ucb7r2NCyfD1mcuzRWw_GYbSFy10IzEce21vJ8CUXJhlmvzd7hYhCdnzfYBlfo4Hs7RQiYShIz3g1BQmy_NQwXByRo5M90fir3fegRKvanqSgkTS-AIruxtOUJOwZW9NnSWW8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bbe3da6710.mp4?token=PyY4CFc5hOP5Jm2klbwah4LaQnsctRsXZNi5qAvB-QyjgFhcPx1FUFJWUWwq-FZ47CYViU_1U3vz9PxZqxR3JGsSdcjcTOM8u-FsyP20slkobce4b6R3RGuzJHP1ysSQjXPTW1PWnG1qJBCvOzqLbZ6jlUsB5QdW4zbZYDiX5xesbJwO3madtPj7AgN5wVPLWWYoN98flyTwX6OW5ejd9T5rYwOp4tpV4htgunCggjZ7OWEYN0DMNbTSvuGzp3-BG7QTMtce_EyFC8Gpuz1-5v1alHctItZSu1TL5yd3msOSiuoACumqk0HNvf1HuE5XinYyzsLd7JdJv8i17MKiAJlPo5A9vxodXFRx3ejv6j9Xygrdd0mbgD6zsM2M3cZZf04SGSS4CgLka-XfzBbToqjAEg35hq9W9bP_vPidjwREMsL-78Y455RobJNt6AasNUH4d-e4SaFNlLsC9eJj3coEBuDi-_cggFW3Z0djZxGFF54hg_sGwAs3uNjYIDfpev80-57lC3o6neFTbsgbKuJTLKyRe827xSSe03Ucb7r2NCyfD1mcuzRWw_GYbSFy10IzEce21vJ8CUXJhlmvzd7hYhCdnzfYBlfo4Hs7RQiYShIz3g1BQmy_NQwXByRo5M90fir3fegRKvanqSgkTS-AIruxtOUJOwZW9NnSWW8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رمزگشایی سامان آقازمانی بازیکن سابق پرسپولیس از علت اختلاف با قدیمی‌ترهای باشگاه: جوان بودم و خوب بازی می‌کردم برای همین از من خوششان نمی‌آمد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.97K · <a href="https://t.me/Futball180TV/90280" target="_blank">📅 15:35 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90279">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FCeFsrYLRXgxD-yZPLnoyCnvFpVjRGOw5qWDyZkP0OJTMtJnPHcQ8dd6ZWUzoEyEbvxC6RWPL5iexej1JNqVgOoddzCOMMLwMhQBtmNlcY3AFE34hPtVu3LPZPNpqtuOX89SUV2jRVjwiESdcFUcmmmnshGfeXONUvi87xa9Ra7BhESgflqVWtRy9mpBFUHDIMmgh6FYHSsQIJFcBzOb2u1oh09ZCo6bnfbIR08taS2Cv0maaM4mx7R0HmQs4X6HA2SwPnGHKZkeH3lLcf8Kp5O3tB272GMYg5BE9JF0k1X5NFQXWxQ4GDqLKTF9EKLSh-u3teRC_TvJGl94zBbp7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تیم‌های ملی که توانسته‌اند دو بار پیاپی قهرمان رقابت‌های جام‌جهانی شوند؛ تاریخ برای آرژانتین رقم خواهد خورد؟!
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.05K · <a href="https://t.me/Futball180TV/90279" target="_blank">📅 15:10 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90278">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2cbec1c58c.mp4?token=t5ZVR-yO8HG3D6pDo6E9lyuxi9cldBAFgu9TI_GdZGnWcoEthuDBI2o_3IebA_5QQM08N3I2eGCJyU7D08Eng576bKi6Rm7kxQK7PlTk8Mvr0OPJuqbgFqhTcuejSR0TxDYqNJyHe1UfEMD9uQb7aBzSsSzXVtIs4XuW_U7uSR80PPyDlQKXLnr4-9GkhZKrygGQ1jyxaZI-Ttt4qR0ilQd7tp815jV8SGFaY3WLpWG2OvbonBT_i2PfHovPtSYDk1rf50SRWEtvRkbobZ2-WIr44WEzjsIYXTW6Aqfs5UzEpWz-RAFCW6WW2TsicL_Vu3uckxZWtWMFXHGD3ERWfw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2cbec1c58c.mp4?token=t5ZVR-yO8HG3D6pDo6E9lyuxi9cldBAFgu9TI_GdZGnWcoEthuDBI2o_3IebA_5QQM08N3I2eGCJyU7D08Eng576bKi6Rm7kxQK7PlTk8Mvr0OPJuqbgFqhTcuejSR0TxDYqNJyHe1UfEMD9uQb7aBzSsSzXVtIs4XuW_U7uSR80PPyDlQKXLnr4-9GkhZKrygGQ1jyxaZI-Ttt4qR0ilQd7tp815jV8SGFaY3WLpWG2OvbonBT_i2PfHovPtSYDk1rf50SRWEtvRkbobZ2-WIr44WEzjsIYXTW6Aqfs5UzEpWz-RAFCW6WW2TsicL_Vu3uckxZWtWMFXHGD3ERWfw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انتقاد شدید صداوسیما از دستور پزشکیان برای اتصال اینترنت بین‌الملل!
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.57K · <a href="https://t.me/Futball180TV/90278" target="_blank">📅 14:45 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90277">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/083cb252a0.mp4?token=rUzNCN6sW4nhT0D1gbqtLThi0wJ4O7H03e7iwxRN3cMO5RoPVID-yAbqjHG_RjgWgM_uOdjdlwzj2KImf-9fVf8-OO57KRYJZzQuL8kPPXpWGHBfS7UPW8K0rIBzy1-wkXnFftlie-6lR1S9kwHumwdIe8fdCxZ2YM04xoR5fI6Pf4O88izGF1TmqNgs9BwhBjm4OYz35xcRWM9kiEo2r38VbVhUQp-UJ9qpaX9lqYpfoQm8aCJo6ll7PUwgaP5Coa8bVTMQ-g2sReTad44OrPyNS2eQW1hBDoRfHvw_0EkBdEC7SRwVuptdTtdnVHpvH2MXhd9jnF6K9xtOxdJdRA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/083cb252a0.mp4?token=rUzNCN6sW4nhT0D1gbqtLThi0wJ4O7H03e7iwxRN3cMO5RoPVID-yAbqjHG_RjgWgM_uOdjdlwzj2KImf-9fVf8-OO57KRYJZzQuL8kPPXpWGHBfS7UPW8K0rIBzy1-wkXnFftlie-6lR1S9kwHumwdIe8fdCxZ2YM04xoR5fI6Pf4O88izGF1TmqNgs9BwhBjm4OYz35xcRWM9kiEo2r38VbVhUQp-UJ9qpaX9lqYpfoQm8aCJo6ll7PUwgaP5Coa8bVTMQ-g2sReTad44OrPyNS2eQW1hBDoRfHvw_0EkBdEC7SRwVuptdTtdnVHpvH2MXhd9jnF6K9xtOxdJdRA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محمد نوری پیشکسوت فوتبال: سردار آزمون را ببخشيد. اشتباه كرده و عذرخواهى ميكنه
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.77K · <a href="https://t.me/Futball180TV/90277" target="_blank">📅 14:20 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90276">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lTOtuORCpu6FQSPdYOiOq84fKxM_g90cfbk7moE2Oy9NlIvQyvebZS1byOhWNleofUpi4eFoPpXVQWR1Pw6zQ0CDlUT5yH3xgzzlV21IZiqTLiCW0Hua3Bdfvd3rJUYQcjv7MkBrRvksKTa3nS7fN3egf7JNOCz8qfdZ3kTQhb1oP3GeB2VxWSdOm5ggYGMPIiWDCBr7c04D5Hw4wVjQVVeqz-efWdR76jC7z_rosU50q4lNlwRegbMKBdrKKivibbr1qYROqXUqDeEt7qxXupZWauNCBKC-zi90uaS3B7pRKuTSCS_J4Xjor2q5QcCS13jnaqlVVbaGHVtAkXAt_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آخرین باری که باشگاه بارسلونا ۸ بازیکن در تیم‌ملی اسپانیا داشت، این کشور قهرمان جام‌جهانی شد و حالا پس از گذشت ۱۶ سال بار دیگر ممکن است تاریخ تکرار شود
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.64K · <a href="https://t.me/Futball180TV/90276" target="_blank">📅 13:55 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90275">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/be02e7f18e.mp4?token=B4DCllfXdyOhRYBS9V09IP74VL8EG5Z8Ks5OfVQJWncAqk16LINkKNAD5vBFPw9qwQs6tuZfwZB58GJhC6uGqa5Z8F9glwFQgG4UN6dq3YmR8CG7P39rdc34cX5BX5OtvOGUYX2B1k2wHO-DMJctsDiXs8EPYO85FB5v4KsxjVMJqSeZ6qFFUBxLi1j_SKzBIqJbl1ToC6NvvkFzR6xzHCtZVPbzSZGS6AJFs5Tc1puI79gb5RHTMMYfecM_HQnMDf18uxDcQsBwvWKLaPGrruTk4qe974wvsfvi9xJvc3cobZ9gxiKGO5BanNKdCw8DzXI9Y5MLg-uKDfbADZocdQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/be02e7f18e.mp4?token=B4DCllfXdyOhRYBS9V09IP74VL8EG5Z8Ks5OfVQJWncAqk16LINkKNAD5vBFPw9qwQs6tuZfwZB58GJhC6uGqa5Z8F9glwFQgG4UN6dq3YmR8CG7P39rdc34cX5BX5OtvOGUYX2B1k2wHO-DMJctsDiXs8EPYO85FB5v4KsxjVMJqSeZ6qFFUBxLi1j_SKzBIqJbl1ToC6NvvkFzR6xzHCtZVPbzSZGS6AJFs5Tc1puI79gb5RHTMMYfecM_HQnMDf18uxDcQsBwvWKLaPGrruTk4qe974wvsfvi9xJvc3cobZ9gxiKGO5BanNKdCw8DzXI9Y5MLg-uKDfbADZocdQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">از عجایب فوتبال بانوان در آمریکا؛ بازیکنی باردار درحال انجام بازی🫪
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.77K · <a href="https://t.me/Futball180TV/90275" target="_blank">📅 13:36 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90274">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ikDQ-qAK3Z-1HcOYLZUKzd98pc3IbuHiaD7o-gArI7mGBv6IkFTUl-KkDF9aAeZk_-gjHOQLb1Y0TsOaEFR8cmoQL2u-95HdEw3e76V6SHnAJZOn5Vc8U1S4iYI4JgNgYrcjCDPp325Mh4bNCj5oHeKLBpecKuESF9JW_s6Qja6VezmCqgiCzLM6equs5FqzSgLn17-GZcbuUN0k_zS7eyNv3mTanW9Xd9CwRUTPZZCJ1k8Hu1KLHHf4OEQV3m308Pz3L8CazTZryDVJ8GJzGUUSY8nKwlpezJTWNuRDrUJuvxeRWJ5wGRCVFR7KwdZZf1ficcO9je9B-WOh9m-RgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
متئو مورتو:
مذاکرات بین بارسلونا و نیوکاسل برای جذب آنتونی گوردون در حال انجام است. با وجود علاقه باشگاه‌های لیگ برتری و بایرن مونیخ، گوردون اولویت خود را به بارسا داده است. نیوکاسل برای جدایی او آماده است.
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.49K · <a href="https://t.me/Futball180TV/90274" target="_blank">📅 13:25 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90273">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LfTFg9FXfZnt4ytoDTnHNQ_wTE1Ypnv89pufX-maohxqyrkYUzFdmC0s-NR_lfNawwQsrrJJTDlgycaNB8shDwo7tj8sqYf_S-_Jc0PCpz9GmOWfGzlZI5JYnahSAoTBGwZjVLVTUrcod4LKKqglyv0pa_bRrcY9Lu7MHPWJ213g-5clG4XKUdCv2ngO7sYZXhPWYo66Xa8ya416ilqsWBfvPNLijL6JB9XKwcZAadwxRBvSdkDJZL6RozFYZ9ZVy9zwia4Erl0gRPOF6lsoluXxK3lA4KawxOHQT2N_HQUZKxmvC8CYDHnY4BS7SZ5ygFUgymgBhX0ufBfJqZy5Aw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بهترین گلزنان فصول اخیر لیگ‌قهرمانان اروپا
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.5K · <a href="https://t.me/Futball180TV/90273" target="_blank">📅 12:50 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90272">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">⭕️
تنها جایی که در لحظه عضویت بهت 500 هزارتومان موجودی میده اینجاس
❌
🎉
کافیه فقط عضو بشی تا #وینرو  بهت
🤩
🤩
🤩
هزارتومان جایزه بده ، نیازی هم به واریز نیست.
⌛
پشتیبانی 24 ساعته
🍆
تنها سایت مورد اعتماد ما با بونوس های کاملا واقعی و رویایی:
🌐
Winro.io
🌐
Winro.io…</div>
<div class="tg-footer">👁️ 9.23K · <a href="https://t.me/Futball180TV/90272" target="_blank">📅 12:50 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90269">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KqxH7K5j0Oxx1o5ajT6Cbgq798WXPXlyhhPgpFKRnk8ACfnIjpj88HVMAHyX1IUsskq3teq0JmOatEGTXofnoeEBmErbwhNNtIZlSoJIh0fM8WmZSmsAd-EkKVTfB1rBUb_JqaIjkELxyXzx-wp7fF1NLzvgEz42FDjhenriXrUDS8MuqnBXqbMkDNv0EMRxM0YIdB3qLI0CNykFhDSuqUph-rO0KUgeZnR9ehg-VXUrMxkoJLLWg9AamwwLpjxZmP91N7EwV8QTao-Vitvzr7YLqMaXEc4ju5Q9dztXhcbNTHWbOQ1LEBU0INVNEq_3pfMwBPXIvWdt9Wd3R2c2tA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
تنها جایی که در لحظه عضویت بهت 500 هزارتومان موجودی میده اینجاس
❌
🎉
کافیه فقط عضو بشی تا
#وینرو
بهت
🤩
🤩
🤩
هزارتومان جایزه بده ، نیازی هم به واریز نیست.
⌛
پشتیبانی 24 ساعته
🍆
تنها سایت مورد اعتماد ما با بونوس های کاملا واقعی و رویایی:
🌐
Winro.io
🌐
Winro.io
کانال بونوس های رایگان
r6
📱
@winro_io</div>
<div class="tg-footer">👁️ 9.69K · <a href="https://t.me/Futball180TV/90269" target="_blank">📅 12:49 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90268">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4cf55f690d.mp4?token=uHs-B6Hrak6D0dL02s-_fs4k3M49d-3IqpYoG-LP-Hhm56w9ShMOQx6qSubTFMTTQh1O1pO7oCbUIhOUKn91Q2ZpdXxqBvX6peR-po81EOSP_Q7p1tn2lu5YIGxlMMm7mrEBjWLUO1N1DnvAnDw4rqmIvNhZTY4d8CHvgvF7VMbJdAKHOTvcHZeliHu7eVmKUs_b0fUYbzBmxpDobOrXPr65qpkLZ_WufBqGMs213YSGs6K41-hDVqx_b1zMW4K2ezJ9BP0zQ5bWelzHu1kWkXW3VClM75IlHp6qwCwTZ3j_2Xz7ZfsuMzufSxnmnbefqcFS7XbZaUmmFpy9lyiuQQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4cf55f690d.mp4?token=uHs-B6Hrak6D0dL02s-_fs4k3M49d-3IqpYoG-LP-Hhm56w9ShMOQx6qSubTFMTTQh1O1pO7oCbUIhOUKn91Q2ZpdXxqBvX6peR-po81EOSP_Q7p1tn2lu5YIGxlMMm7mrEBjWLUO1N1DnvAnDw4rqmIvNhZTY4d8CHvgvF7VMbJdAKHOTvcHZeliHu7eVmKUs_b0fUYbzBmxpDobOrXPr65qpkLZ_WufBqGMs213YSGs6K41-hDVqx_b1zMW4K2ezJ9BP0zQ5bWelzHu1kWkXW3VClM75IlHp6qwCwTZ3j_2Xz7ZfsuMzufSxnmnbefqcFS7XbZaUmmFpy9lyiuQQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اظهارات تند نیکبخت واحدی: افشین قطبی کاره‌ای نبود. چرا در تیم ملی نتیجه نگرفت؟ قطبی ذات قشنگی نداشت
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9K · <a href="https://t.me/Futball180TV/90268" target="_blank">📅 12:40 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90267">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/98d2b87299.mp4?token=nOk4CdAwjqa5S_U3aUrilx9ddkiX2PRXyHbNBJhNpRuGcnaxVkn1rYATz8rTgvvIoOO9f72pXVvMlEwRZ2eWVhPzFdcLwtdcendpNHnflVBru3uw5LI_BOIGmvX5uKAhqli0oVG06KYxFWda6Ibp0HboY04aGWYX3xRtDVApnQrFlaF9dGE_667Ov_3AtDBxQVi1EGIeD7-8QP_bSiHGjTin7atzLm3VZWLQlcFleoLMsAVoevhGfjreRySETOOO9pi0TiSlLup9vk9tgpHJrPW7CHnjBNgQY86G-WugxjOtgRuLp_XwbkM1R2wK5cemsxUlXlBuIOrSVQH6UuPFWA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/98d2b87299.mp4?token=nOk4CdAwjqa5S_U3aUrilx9ddkiX2PRXyHbNBJhNpRuGcnaxVkn1rYATz8rTgvvIoOO9f72pXVvMlEwRZ2eWVhPzFdcLwtdcendpNHnflVBru3uw5LI_BOIGmvX5uKAhqli0oVG06KYxFWda6Ibp0HboY04aGWYX3xRtDVApnQrFlaF9dGE_667Ov_3AtDBxQVi1EGIeD7-8QP_bSiHGjTin7atzLm3VZWLQlcFleoLMsAVoevhGfjreRySETOOO9pi0TiSlLup9vk9tgpHJrPW7CHnjBNgQY86G-WugxjOtgRuLp_XwbkM1R2wK5cemsxUlXlBuIOrSVQH6UuPFWA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
اسپویلِ بازی آرسنال و پی اس جی.
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.15K · <a href="https://t.me/Futball180TV/90267" target="_blank">📅 12:15 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90266">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/99be172cd9.mp4?token=fljuJ3XBRb6G8xjF-pmMJwCpT-5I8VSa9AwzBn-AjeXOYscKehH3f175ZcxP9IYJZEzkSu9U8JKpxsBBbj1yDySUrvOdebI1_9aEK9Gs5-Tii6Q5QIqlpj9D8oibjicReCbi63gFO_e4WAVrxq5q0pfOECktGXNH8R7M6vlpx9zvsTrV2rwwSq710Tf4BhLDbPHpke4QdIqmsDYZ12SE3amr136o1qvPr4SZPbPK7iidOtJGMhVQu1xrSVMZwawVSgRE5GdMcfVlqzYkzMDK4JelDsWYqptubHqQ7wduvLjEQTMN_AFhGG2KytBvYpM1WgGRu6v8jYJfAyfw0BnoFVt_tL4K3zMB9UAInlPURVOwIoiDEYiXTm9cNi0zF_C-oOaj-AYmGE3OHL7CrYb8D1MfHCA3Tvsjt_6TuHzTtXERedfkXLUTPT-2QOfFL652W9Ib5t9bYVoIUW8m8yJbGMe4_fo0EszD9Tq-dS8oRoDntsUjOl2yLQFvwNBCmeZ0rpKaDBz8qxI2zvZ5r_nUCqoNSzZufnKYkBTDsX-Cbwi9EI8pzpVAredEQ2MnxOIC6ILmirKKhk1_vIG5YvYatgV7WajCJo56vLRAdZFLCW153m0B9adl58XmuO3-78fMcUmVhwfF7RKZRE2KzkQu4FGMux2lu1qjt0smXQf5iOc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/99be172cd9.mp4?token=fljuJ3XBRb6G8xjF-pmMJwCpT-5I8VSa9AwzBn-AjeXOYscKehH3f175ZcxP9IYJZEzkSu9U8JKpxsBBbj1yDySUrvOdebI1_9aEK9Gs5-Tii6Q5QIqlpj9D8oibjicReCbi63gFO_e4WAVrxq5q0pfOECktGXNH8R7M6vlpx9zvsTrV2rwwSq710Tf4BhLDbPHpke4QdIqmsDYZ12SE3amr136o1qvPr4SZPbPK7iidOtJGMhVQu1xrSVMZwawVSgRE5GdMcfVlqzYkzMDK4JelDsWYqptubHqQ7wduvLjEQTMN_AFhGG2KytBvYpM1WgGRu6v8jYJfAyfw0BnoFVt_tL4K3zMB9UAInlPURVOwIoiDEYiXTm9cNi0zF_C-oOaj-AYmGE3OHL7CrYb8D1MfHCA3Tvsjt_6TuHzTtXERedfkXLUTPT-2QOfFL652W9Ib5t9bYVoIUW8m8yJbGMe4_fo0EszD9Tq-dS8oRoDntsUjOl2yLQFvwNBCmeZ0rpKaDBz8qxI2zvZ5r_nUCqoNSzZufnKYkBTDsX-Cbwi9EI8pzpVAredEQ2MnxOIC6ILmirKKhk1_vIG5YvYatgV7WajCJo56vLRAdZFLCW153m0B9adl58XmuO3-78fMcUmVhwfF7RKZRE2KzkQu4FGMux2lu1qjt0smXQf5iOc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پاسخ شفاف سهراب بختیاری‌زاده سرمربی استقلال به پرسپولیسی‌ها: فاسد نیستم!
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.81K · <a href="https://t.me/Futball180TV/90266" target="_blank">📅 11:50 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90265">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RwF6hUe9wXoeTiqGHHa7iISM54ap2JETuPfdeQ5WCczWJvNd0nL0PqHCJ_h5QQGKmvVN4AicdocOjf6UEn_tKUsW87HAdGUnRExtEL89WTkXavcrBBQPyN4leREuuggVpE0nnYwpCT9tU-My24CS5uTsT3FQ-CnEN7D28TFEJni2m9VgpwbA9PRBncgt-E_apSy0BVtJvZRNQ2EDcOQ-prLS8M3Q3FKx-Ujk96tzQD-W28BTKAztptlH7QjMEDJ2Q8dWqCnR_tqLUWcXqCKeSDZ851XeClRPA7xHpVpm5Q3YB8oDYGwjyJKBVJnUlBexHs1MxsDUPAJN7ptlTDd0Zw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
به گزارش رومانو، باشگاه بارسلونا بدنبال عقد قرارداد با آنتونی گوردون ستاره نیوکاسل است
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.74K · <a href="https://t.me/Futball180TV/90265" target="_blank">📅 11:25 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90264">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/426e74bc07.mp4?token=VMRRPUrIuTn2vlTQFqGzu7ToQqmI3hEu9ZMtlDIHMgdpOlDFXQPmefONJNE9cA7jad2AfZ9sJh-37tp9o5axbn6wz5eQQftr4UhguWqUGyCb8I39CXDIrHW6Lpx8-N7ISDpQYSbnuRK7iU7FO7sDb6dnAf7F_BZFwU_uH8zrh563Kde7ajpH-OFtEX0Rz2RggLHsOJDSIsr8ZBY2WBQj9r1oAYyepEiCUd3wUYgRqp_D3q9ctNFsnHjOVUt9yb4qB1HQGdyzo5b2nJBZvwrAiupxms7A0DJ2zK_bvNisPxeByFqzv1gQdSRGjqfB_7s6wt_xDiZUPtNO5qvgkOIZPbRmXwNQYJMWVM3RZVj1MCfywVhPZ-ZQXjUoQhO_PfmCQpMuJO-tNVRNNJbrppqn4TzyZkLi6dDL-HjxHm9xnuSFzQRVXpl6wiKySfF3RsrtgytwUWSfzZyR7GV38lqZ50kF1H88xCatGe5TeuENccqocJhR32AIy8Tza5Mj5RwVzc3Vo7TOhOOuthfGsMx0QS3ifO0U_w7bGpvEneKP7vvJ_oe1qPC4IyE3pVD2y5svt8VEBItIymHvDE1npkPM6hKV9sS7ND7hn0peU3xqc-Kkx7Vf4bpSdZp14Z08NGMb5e53fNSofBOFM5y1TB4YbVkKcccJHlS5o8774-TCiRI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/426e74bc07.mp4?token=VMRRPUrIuTn2vlTQFqGzu7ToQqmI3hEu9ZMtlDIHMgdpOlDFXQPmefONJNE9cA7jad2AfZ9sJh-37tp9o5axbn6wz5eQQftr4UhguWqUGyCb8I39CXDIrHW6Lpx8-N7ISDpQYSbnuRK7iU7FO7sDb6dnAf7F_BZFwU_uH8zrh563Kde7ajpH-OFtEX0Rz2RggLHsOJDSIsr8ZBY2WBQj9r1oAYyepEiCUd3wUYgRqp_D3q9ctNFsnHjOVUt9yb4qB1HQGdyzo5b2nJBZvwrAiupxms7A0DJ2zK_bvNisPxeByFqzv1gQdSRGjqfB_7s6wt_xDiZUPtNO5qvgkOIZPbRmXwNQYJMWVM3RZVj1MCfywVhPZ-ZQXjUoQhO_PfmCQpMuJO-tNVRNNJbrppqn4TzyZkLi6dDL-HjxHm9xnuSFzQRVXpl6wiKySfF3RsrtgytwUWSfzZyR7GV38lqZ50kF1H88xCatGe5TeuENccqocJhR32AIy8Tza5Mj5RwVzc3Vo7TOhOOuthfGsMx0QS3ifO0U_w7bGpvEneKP7vvJ_oe1qPC4IyE3pVD2y5svt8VEBItIymHvDE1npkPM6hKV9sS7ND7hn0peU3xqc-Kkx7Vf4bpSdZp14Z08NGMb5e53fNSofBOFM5y1TB4YbVkKcccJHlS5o8774-TCiRI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیو وایرال شده از اظهارات عجیب شیدا یوسفی بازیگر گمنام سینمای خانگی: در کارخانه پدرم، روی شمش‌های طلا راه می‌رفتم!
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.69K · <a href="https://t.me/Futball180TV/90264" target="_blank">📅 11:00 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90263">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6b5959b18a.mp4?token=tWwOok-sNEtnKP3XhR3mKyT7WLA0CrIrQKNE4kFG5OBjI7FwOq6IoHc1ZyYW6xlfn4NIiz8SJ7u5OABlFjIPufgVDG1jlc9qzDkoQ9tRtOQvA-o6vIohOQgczkQ_ly_9chD3V8p25EpURieovY3LrHKMuJo2V7JMn2YGn6KUQUbciXxeUiyDwIXpcB5CGpmjBlSruvfo-f729aaRXOSgWySFpBKTvbBxyOCip2oRLmsUZxJXFh1sYIAdOiN00HitRI_dVMdBgQDZFWlsq1mXRXcbma6tBW7_UYwSM9jL4QZddw3rIyqM82uPiy2RbCC_Lrra24X_NxLPJis_2d11Rw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6b5959b18a.mp4?token=tWwOok-sNEtnKP3XhR3mKyT7WLA0CrIrQKNE4kFG5OBjI7FwOq6IoHc1ZyYW6xlfn4NIiz8SJ7u5OABlFjIPufgVDG1jlc9qzDkoQ9tRtOQvA-o6vIohOQgczkQ_ly_9chD3V8p25EpURieovY3LrHKMuJo2V7JMn2YGn6KUQUbciXxeUiyDwIXpcB5CGpmjBlSruvfo-f729aaRXOSgWySFpBKTvbBxyOCip2oRLmsUZxJXFh1sYIAdOiN00HitRI_dVMdBgQDZFWlsq1mXRXcbma6tBW7_UYwSM9jL4QZddw3rIyqM82uPiy2RbCC_Lrra24X_NxLPJis_2d11Rw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وقتی صحبت از مهارت و دقت میشه
🔥
🔥
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.66K · <a href="https://t.me/Futball180TV/90263" target="_blank">📅 10:35 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90262">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SIwnSaPuhbieDZgx7_u4oauXfvSTp7xX3Y4uP3EKi16ShczYg2bZiNZXJY0pjBmi3lJ1Z-nB-_YU6ekxyxTlcsVpbrDa2feWGBBNM1idI2HUdqd_2GSYzWHCLUeCzbX4zBV2JcOo5FTMPUjkgQPYAYwwMJ7XDFLsq1GKVuFoTs0t1R0bp_CtliAqnlS01lbIsaQJWfdoZNdaAGjIJtytE7hb29Ed1fdKQSgZ-LzMt2rtLr0rAL6vsXC0x3EXu6WTxu8gTBUJYyyCbsh_5kih9UBGH2Ci38GyxTU4Yk-F6MXM_yz2DMqzuvNjUMmoJEWHljmNm6zaPmb23Jo73SpvSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در ترکیب اصلی رئال‌مادرید در فصل گذشته هیچ بازیکنی از اسپانیا فیکس نبود و بنظر عدم حضور بازیکنی از این تیم در تیم‌ملی اسپانیا برخلاف بارسلونا طبیعی است
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.77K · <a href="https://t.me/Futball180TV/90262" target="_blank">📅 10:10 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90261">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8d64b58d74.mp4?token=b0Cx7W90fnQwV8jNZloD-NYh8jbTCBdduQp9f7R8qIqLmfJjabF0v41H9pAhH1iQPNUYgaKfdDLSY91rCRvnHXy7Vq1zZInOmkkKj6hdR5wd_qnZms4N2gKbMXVr3AY3vdCo0oP0D5IiqK8StoFyeyFL-RVj2EGhgTRU9wgMbpMgwt1SpeyqX9u7Yx9sup-PdPi_bWIZAzeofGPKFdHsUD9BQu_mBDV6ctjNCLbpoMMNyfwJfBugNEsEVOBP1VH_48aBj512pxFPKlS9n80j9OIcszVpqwV6T1NQo6s0EaR40tq4Mxapl5kv8pOMC647ZKTvcMFCgTJamGrzxAJ87oWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8d64b58d74.mp4?token=b0Cx7W90fnQwV8jNZloD-NYh8jbTCBdduQp9f7R8qIqLmfJjabF0v41H9pAhH1iQPNUYgaKfdDLSY91rCRvnHXy7Vq1zZInOmkkKj6hdR5wd_qnZms4N2gKbMXVr3AY3vdCo0oP0D5IiqK8StoFyeyFL-RVj2EGhgTRU9wgMbpMgwt1SpeyqX9u7Yx9sup-PdPi_bWIZAzeofGPKFdHsUD9BQu_mBDV6ctjNCLbpoMMNyfwJfBugNEsEVOBP1VH_48aBj512pxFPKlS9n80j9OIcszVpqwV6T1NQo6s0EaR40tq4Mxapl5kv8pOMC647ZKTvcMFCgTJamGrzxAJ87oWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بهترین گل‌های فعلی در سال ۲۰۲۶ فوتبال
🔥
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.77K · <a href="https://t.me/Futball180TV/90261" target="_blank">📅 09:45 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90260">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/26b4bc8543.mp4?token=tsfxljYktmexp9CVh29IKS8pAN2j1QXrALKHOldoi_QgLXNpqbA2nO3AhieVJeiZu6ZAHP949HlO5VwyGl2NFFQcUrbwYjlyrFaVgozyq3W9qsKUrm2W35eZOLXM_imgMqGZlydlPXRAOx3dvolTXx_5egIOuTpfliClZhW2deO0mEBKBQzJPUMN7bWPo-EBL3neMw-X6Omw9dnngWQX0mnV3XasHLEuSLHJkBgMoDCMndxgt3BZJej8HoYuAi9fcESP2I44R5lc0_8pBiiVKJkgfIB96b_Q1dkJI56qjD9GBcDM0Vzh2oRHvHHSRzmeh2-ho6sqCCGEwfT7RrRBHw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/26b4bc8543.mp4?token=tsfxljYktmexp9CVh29IKS8pAN2j1QXrALKHOldoi_QgLXNpqbA2nO3AhieVJeiZu6ZAHP949HlO5VwyGl2NFFQcUrbwYjlyrFaVgozyq3W9qsKUrm2W35eZOLXM_imgMqGZlydlPXRAOx3dvolTXx_5egIOuTpfliClZhW2deO0mEBKBQzJPUMN7bWPo-EBL3neMw-X6Omw9dnngWQX0mnV3XasHLEuSLHJkBgMoDCMndxgt3BZJej8HoYuAi9fcESP2I44R5lc0_8pBiiVKJkgfIB96b_Q1dkJI56qjD9GBcDM0Vzh2oRHvHHSRzmeh2-ho6sqCCGEwfT7RrRBHw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وحید قلیچ برا خودش عالمی داره
😂
😂
😐
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.82K · <a href="https://t.me/Futball180TV/90260" target="_blank">📅 09:20 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90259">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c4b0e0df75.mp4?token=PZTmsJ1MurmsqjQXiCjIvpdlMOt7tysF4PCUT6zO__hlzYpKsmTAVz5tvyP9PLdz57jjBsjXNQAdVRzSzNzAqksO0sUKDKIr9Mh2szvsyjRHhil7Etucrn0_4VbSKUdzUhx5VSJ9PtIx58a8-CvJqBvotiZJe8otBlLKzKvazGhuVYld8IX-qrlxeIMekU9xNDCK7hnGiMjZOtOjQLnx5OJ8akKX-rHSiti2qJagBeY1eAH0vgVBEdtJ-PpfEE-R3CLTpS0PPEosLnG2TAPmYUAYZS3f1wd_auwfqu-_NKt_A7arjuIjzFDU5tQgXpHR5vkppl4XPQ8hYa_UsXYJjg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c4b0e0df75.mp4?token=PZTmsJ1MurmsqjQXiCjIvpdlMOt7tysF4PCUT6zO__hlzYpKsmTAVz5tvyP9PLdz57jjBsjXNQAdVRzSzNzAqksO0sUKDKIr9Mh2szvsyjRHhil7Etucrn0_4VbSKUdzUhx5VSJ9PtIx58a8-CvJqBvotiZJe8otBlLKzKvazGhuVYld8IX-qrlxeIMekU9xNDCK7hnGiMjZOtOjQLnx5OJ8akKX-rHSiti2qJagBeY1eAH0vgVBEdtJ-PpfEE-R3CLTpS0PPEosLnG2TAPmYUAYZS3f1wd_auwfqu-_NKt_A7arjuIjzFDU5tQgXpHR5vkppl4XPQ8hYa_UsXYJjg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
همسر ناصر حجازی: به او یک میلیون تومان پیشنهاد دادند تا گل بخورد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/Futball180TV/90259" target="_blank">📅 08:55 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90258">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">روایت قرارداد نجومی فرزاد آشوبی با راه‌آهن در ایام مالکیت بابک زنجانی
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/Futball180TV/90258" target="_blank">📅 08:32 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90257">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">Soren-VPN.apk</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/Futball180TV/90257" target="_blank">📅 01:45 · 06 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
