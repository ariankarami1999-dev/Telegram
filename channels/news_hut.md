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
<img src="https://cdn4.telesco.pe/file/HGOOaRlDJPCY6p5k643vQKlilVrsrjoLxO2fN_0RLKOsP5pD_2mbYMVZe35mrj4aF-SEPYZUV2-rZZvhsoHd19UD6q8UIEYk7-hs8UGM9K0kKi126v1P8GcvsOMT2lnlew21SheMdT8U9uEc-3_HImNUD2np3LU7cbHyAkKLlvRghVm5vK-4-BqdGl93f3NjGYkqsMCEcASFxakNdH1DeVCXpzu46qK0EBE8g00CC9a_GuUrqyBkTpjXaBSDlRu3Fo24Wc4VqsAETFaW9YwKigF0_WTKd40dqEpm2Dv7p71jIKFqlXWtnx22i6UyR5pQtBuG7gOt9XNMqApTMKbc0w.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 116K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-07 07:44:06</div>
<hr>

<div class="tg-post" id="msg-70738">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/70738" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 6.12K · <a href="https://t.me/news_hut/70738" target="_blank">📅 02:01 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70737">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uL6bikRQU5sagSvJ7gkzTMIaEcpmeK6Jg7TIfCG9ThA5lhO3o8KCDz-P2UMVEFUUegA13FBDk7ZvcbtG24H09krURJaZU8Szid_HqlWPxRVaM9nmfgZLderR-3sKv8I9fOnbzkNWaQ3FSJxSMyxKb1-HOFK_1DCRbSefM2hM8FRMYvPSeBt3xK0IeAkqBMHObl0X47wqq6ZAqDpQ6a08kl-Inm3KEz7_tCyfVm7b0tpVtMwE1BSdaj9YakcRBwBCjMl7ayxFf5FRIKmprGgrL1S6SdsipL5mjdb5MHyMx0p1yfENCIazMdySG1CYUgyCGOBDsT4tgllgi5VccieRxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
فقط یک بازی از میکس‌ت لوز شده؟
پولت برمی‌گرده!
میکس می‌بندی، هیجان بالا میره، اما یکی از انتخاب‌هات خراب می‌شه؟
با پیشنهاد ویژه
TrexBet
، در صورت رعایت شرایط، می‌تونی
۱۰۰٪ مبلغ شرطت رو پس بگیری
.
همین الان وارد سایت شو و شرایط آسان‌ش رو مطالعه کن!
💰
🦖
🦖
🦖
🦖
🦖
بونوس صدرصدی اولین واریز
🦖
واریز آسان، برداشت سریع
🦖
سرعت بالا، طراحی حرفه ای و تجربه ای متفاوت
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 6.19K · <a href="https://t.me/news_hut/70737" target="_blank">📅 02:01 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70736">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🚨
ادعای العربیه:
شبه‌نظامیان عراقی قصد دارند در ساعات آینده به عربستان سعودی حمله کنند.
@News_Hut</div>
<div class="tg-footer">👁️ 6.35K · <a href="https://t.me/news_hut/70736" target="_blank">📅 01:59 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70735">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qRMTPorfJBPYx1kvegtNYB8U6QILwbcO8tsd50exh-jTI5YxcR-5W-YlCdLvtIVwQBYEAvLQv1WdIUiIZGwC3tRviyfO6s8lEHnAmWZcbHUEfNhuxHxE4FcF893ldhTzAUYHFIibJ-KydqZN-66erkpCFUPoSfPF_qSMM3feihFCotMB4JirlS1X-z4H-R8plhh3xW-JuEBk3u9GHd_2LblYxNLVnLLvP7A8SYiRn_oSMOum32Bm6EWpbuXvAcQOyy6z6u26pDDLqudidTLT1_SUiSLPzN0pbxMSfd_Dm6QGc48IBlBETysaa_DURcJaWH0nXaWjVTRlqc0duAX6Qg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
مجری:
غیر از قرآن و نهج‌البلاغه، کتاب دیگری هم مطالعه می‌کنید؟
🇮🇷
پزشکیان
تا دلتان بخواهد. فکر می‌کنید همه حرف‌هایی که می‌زنم، فقط از همین منابع است؟
🎙
مجری:
آخرین کتابی که مطالعه کردید، چه بود؟
🇮🇷
پزشکیان:
آخرین کتابی که خواندم «فراجامعه» نویسنده آمریکایی بود.مگر می‌شود کتاب نخواند؟
@News_Hut</div>
<div class="tg-footer">👁️ 8.44K · <a href="https://t.me/news_hut/70735" target="_blank">📅 01:25 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70734">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dcb6ce22e5.mp4?token=PDindH9ekVsmIwCk810ORmkp3R7zIKKLuR_YziCC4PBnE3j3KBOeQtR0dp_z0Oo7xbFNp8AC5j3kny4V1aq_DczSGMDKDPUYVdTuw_8uE6f_ovvTqTVqe2glj4hw3NQUNt_zRV0wZxUVKekENpZj_IneddNzW7hda157gKmdZpszl48BQLvvmoiOsD-KznYrfwsrgAMSoyOLaqRsGVocb4mGdgbzL0K7pZHV-CpGUCSz27-n2M-4eHruaLS2uGkUfIoPOVfs05cIsQfCEKNGjSixSOhu4c7oaZhyZXwYxNKHNTw0iam4C1W2ET8hsdkziAQxEeieJNiSySmoyA0Weg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dcb6ce22e5.mp4?token=PDindH9ekVsmIwCk810ORmkp3R7zIKKLuR_YziCC4PBnE3j3KBOeQtR0dp_z0Oo7xbFNp8AC5j3kny4V1aq_DczSGMDKDPUYVdTuw_8uE6f_ovvTqTVqe2glj4hw3NQUNt_zRV0wZxUVKekENpZj_IneddNzW7hda157gKmdZpszl48BQLvvmoiOsD-KznYrfwsrgAMSoyOLaqRsGVocb4mGdgbzL0K7pZHV-CpGUCSz27-n2M-4eHruaLS2uGkUfIoPOVfs05cIsQfCEKNGjSixSOhu4c7oaZhyZXwYxNKHNTw0iam4C1W2ET8hsdkziAQxEeieJNiSySmoyA0Weg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇷
مسعود پزشکیان:
«زمانی که حتی پیش از وقوع هرگونه درگیری، با کسری بودجه ۱۵۰۰ هزار میلیارد ریالی مواجه بودیم... آیا این صرفاً ناشی از سوءمدیریت است؟ آیا این بدان معناست که مردم تورم را احساس نمی‌کنند؟»
«بدیهی است که ما در زمینه معیشت مردم مشکلاتی داریم. روشن است که... باید تا کنون میزان طرح کالابرگ الکترونیک را افزایش می‌دادیم. ما در برابر مردم شرمنده‌ایم.»
🇮🇷
پزشکیان:
«در این شرایط جنگ‌گونه و در این وضعیت اقتصادی
بگذارید بگویند
:
"من می‌توانم با همین شرایط و محدودیت‌ها مشکل را حل کنم"؛ آنگاه من دستشان را می‌بوسم.»
«نه اینکه به من بگویند "پول و منابع در اختیارم بگذار تا مشکل را حل کنم"
خب، اگر من پول داشتم که خودم حل میکردم
😐
@News_Hut</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/news_hut/70734" target="_blank">📅 00:45 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70733">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/MYbNatPLoAw2Iv4xQJmPmUDBqJEAy_cPfGKUBzJmjzUotckwRb5MsivU9TUbVp2d0KVR_0PBin9Zk2EeQtWjfOvmHJZF7JjA-WTxxWIXqnAtnZn7JkN0cwr8mxnyadXeNXAfi6qkZD5ihgD8cPDNJHqUjttrB9SXNiIACiFFcm_9zKPxNTxo253g1-HCM1Ue9qQBu5F_Lqk5FSZ16jq2qi5BRMg_ABP6WVjydBqByj1Nlq6Nk6y3vcZ1yLpgDFuzMBW5iIXw0SDO0Jm9c7b-TkWYBgyW-XQcFDD8O1dtmpPd-35cSBw5NnBl9vDp4MkLSZbW8wrryENfKJHySutrjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇦🇫
برای اولین بار تور افغانستان گردی برای مردم ایران موجود شد.
قیمت تور ۷ روزه‌، ناقابل ۵۰ میلیونه.
@News_Hut</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/news_hut/70733" target="_blank">📅 00:34 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70732">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2cae7f25ce.mp4?token=cXlkLvVlvWteOiEP-U_morUSEseQWifDYw_W9u9HXBU2Id59_aExhxU2XJk8l9GRHFvvriJk0Kg4aa44avCdA31kiO3R8-LSwaGRfkuAc96k9HSADjZ8eGmca89tR7pkyYIBWHMWlvDCqAeI3bjXeXugH7gLydMeINBkJw62x7QbimJy-J8y8pCG2FaXvOABmpSQsXvhB9MzsJJysxXdkkp8RUNggmuFtRpljmEelN9r2aZ6sF54WU1YHNoowxz9T4pKHDZHYLtrWKgN_ncaFQ4kCG_LgQijWzHNRSpq9DryTeY4DBZdxiHjuRzSDLsVKf8DmNMhKSw6bcYJ5yS8zg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2cae7f25ce.mp4?token=cXlkLvVlvWteOiEP-U_morUSEseQWifDYw_W9u9HXBU2Id59_aExhxU2XJk8l9GRHFvvriJk0Kg4aa44avCdA31kiO3R8-LSwaGRfkuAc96k9HSADjZ8eGmca89tR7pkyYIBWHMWlvDCqAeI3bjXeXugH7gLydMeINBkJw62x7QbimJy-J8y8pCG2FaXvOABmpSQsXvhB9MzsJJysxXdkkp8RUNggmuFtRpljmEelN9r2aZ6sF54WU1YHNoowxz9T4pKHDZHYLtrWKgN_ncaFQ4kCG_LgQijWzHNRSpq9DryTeY4DBZdxiHjuRzSDLsVKf8DmNMhKSw6bcYJ5yS8zg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
⭕️
🇮🇷
بنزین لیتری ۱۰ هزار تومان !
پزشکیان: فقط نرخ سوم قیمت بنزین پس از هماهنگی با همه نهادها و ارگان‌ها از ۵ هزار تومان به ۱۰ هزار تومان خواهد رسید.
@News_Hut</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/news_hut/70732" target="_blank">📅 23:35 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70730">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b620b727bb.mp4?token=qqPZ8iKGt8rs8Yt6k9uz5taoGrj0KfPO532t5ARrsDo57K8RR_EGa6yw7b3kqgL1dwFzMUYR-zTBwsAtYtG0Zd_i2gZ4SwMgSFzNHh1UAZkg-duQ76L6Rfs2VfE9b8LrV7HR9bnXC97B3a9qJerj-nX74PsL7YnkgPMMjH4tvXvs8nmOwI65TqlMKWyN4bGLv5NT4zEgFGcr3OcFlhVnRZyiRzN34HN6g5pKl_YlvGCNyvCpwgjpOtSL8hGTpGIpvFRsbbAll6Z3jhzadflPzJZR9XRSlxt_yFOyTGpA_IvnaJhCDWcPpL6BraAHfGqZKSNh9zvNDCUNyOD4nEUKDA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b620b727bb.mp4?token=qqPZ8iKGt8rs8Yt6k9uz5taoGrj0KfPO532t5ARrsDo57K8RR_EGa6yw7b3kqgL1dwFzMUYR-zTBwsAtYtG0Zd_i2gZ4SwMgSFzNHh1UAZkg-duQ76L6Rfs2VfE9b8LrV7HR9bnXC97B3a9qJerj-nX74PsL7YnkgPMMjH4tvXvs8nmOwI65TqlMKWyN4bGLv5NT4zEgFGcr3OcFlhVnRZyiRzN34HN6g5pKl_YlvGCNyvCpwgjpOtSL8hGTpGIpvFRsbbAll6Z3jhzadflPzJZR9XRSlxt_yFOyTGpA_IvnaJhCDWcPpL6BraAHfGqZKSNh9zvNDCUNyOD4nEUKDA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇦
❌
🇷🇺
پهپادهای انتحاری اوکراینی از نوع «شاهد» به پایگاه هوایی «انگلس-۲» در روسیه حمله کردند؛ پایگاهی که میزبان بمب‌افکن‌های راهبردی نیروی هوافضای روسیه (VKS) است.
@News_Hut</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/news_hut/70730" target="_blank">📅 23:12 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70729">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/54b3be23a9.mp4?token=ZDg1Y3w4U-bWbofZnhMbI4y9hZ3Azy3brQZclrJtBvdcMoPpbzsk01M4pV22xhHDoGMpFxVU4M9hVq78c39bD-qsnK51pUMJsXF8G6jA_zrQdKsVjqu-VZJeVhdzzzVgWhzj7ug1BolbPOOZxfGOukmWr3TbI1-ULjasSt-PEbl3ii5FfTlmmKbVvw9dBrBrkGUtCHxTBGQ_k_ua3MCGeZJdnM_b4k5PJvR8R_uFMqhEeCSCYjJHMtnsMyduq0gQVh_os9zN3MzjEgRenmevcjtyHAxQ9FlI3dvFQmyoQRZ5JPDnl5aD9JOL9BtQGt51OPD6A1337lN3muhxvND7sA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/54b3be23a9.mp4?token=ZDg1Y3w4U-bWbofZnhMbI4y9hZ3Azy3brQZclrJtBvdcMoPpbzsk01M4pV22xhHDoGMpFxVU4M9hVq78c39bD-qsnK51pUMJsXF8G6jA_zrQdKsVjqu-VZJeVhdzzzVgWhzj7ug1BolbPOOZxfGOukmWr3TbI1-ULjasSt-PEbl3ii5FfTlmmKbVvw9dBrBrkGUtCHxTBGQ_k_ua3MCGeZJdnM_b4k5PJvR8R_uFMqhEeCSCYjJHMtnsMyduq0gQVh_os9zN3MzjEgRenmevcjtyHAxQ9FlI3dvFQmyoQRZ5JPDnl5aD9JOL9BtQGt51OPD6A1337lN3muhxvND7sA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
صحبتای یه مداح؛
روزی بود یه میلیون حسابم داشتم رفتم ده میلیون چیز میز خریدم تازه پونصد هم حسابم موند
خاک تو سر مسئولی که چوب میندازه لای چرخ اداره این مملکت
اصلا دلار بشه یه میلیارد رزق ما دست خداس نه دلار
دلار ۲۰۰ تومنی هزار تومنی ۱۰۰ تومنی همش یه عدده مهم نیست
@News_Hut</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/news_hut/70729" target="_blank">📅 22:35 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70728">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">🚨
🇮🇷
چندین موشک ضد کشتی از سیریک به طرف تنگه هرمز شلیک شد.
@News_Hut</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/news_hut/70728" target="_blank">📅 22:18 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70727">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5ff34e4aca.mp4?token=DhtMJtRt_NOO9LH2bQfHeyxC_gm5phl4b7Zf6RP2Jkq78zfcNiqALeHM-SfJVLYQVhQzlS_hE6fTe8Z0BZSBZN2C547QpbNIeD0W-dtjRTrODcwrGM88VyZkdIL3ZNBELDXV2V1aZXmMYfueH_75KJ9iq2isaOKRllPYgtTmuZj9LBpcZATaQN-hmsxW7uBemZu3rcZ6YUclAh-bdj8PB6W9UNFlDmZIi2i2ILfR2iSjMmWfK5hH74-h9FTggENj-QDGnjyfBfke19BpXSGP5W0euAzXTpyKzNE4BKWom-YPq4nLXyxeHoYiJyPUTndNpn3viHoOeEcwXXgob6upNA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5ff34e4aca.mp4?token=DhtMJtRt_NOO9LH2bQfHeyxC_gm5phl4b7Zf6RP2Jkq78zfcNiqALeHM-SfJVLYQVhQzlS_hE6fTe8Z0BZSBZN2C547QpbNIeD0W-dtjRTrODcwrGM88VyZkdIL3ZNBELDXV2V1aZXmMYfueH_75KJ9iq2isaOKRllPYgtTmuZj9LBpcZATaQN-hmsxW7uBemZu3rcZ6YUclAh-bdj8PB6W9UNFlDmZIi2i2ILfR2iSjMmWfK5hH74-h9FTggENj-QDGnjyfBfke19BpXSGP5W0euAzXTpyKzNE4BKWom-YPq4nLXyxeHoYiJyPUTndNpn3viHoOeEcwXXgob6upNA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
مجید شریفی:
جایگاه کره‌شمالی با جایگاه ایران اصلاً قابل مقایسه نیست
اگر ایران سمت سلاح اتمی برود، همین چین هم شما را تحریم خواهد کرد
مطمئن باشید به اندازه‌ای که روس ها مخالف اتمی شدن ایران هستند، آمریکایی ها مخالف نیستند؛ این را مطمئن باشید
بازی مناسبات قدرت است، بحث دوستی و اینجور چیزها نیست
به محض اینکه اعلام کنید سلاح هسته‌ای داشته باشیم، مطمئن باشید با تمام قوا حمله خواهند کرد، هیچ حد و مرز اخلاقی را رعایت نخواهند کرد
@News_Hut</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/news_hut/70727" target="_blank">📅 21:57 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70726">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/209278afcc.mp4?token=Vu7yMg-1ROVrkAXJZa8iXf4AYDHS9D7TILbpYW5QpcQovg3nqfP5NDMIPCkKWEfek76Ui2lcL0n37_iRSh0MkSIIy4HcWPR4_QmLNLoeUyFVLr_O1i_PFfCNeCjVIq5RntUvlmd2HH7xGJ6XgI0TXYzUHwZFmJHHQMTXEWq5DKwHiwgLxP-aFHUXzHnVhZ39kXBmKPBf72rnRrf1UgyYA97JDypjbZmGtBhEURlZvm10YxcaZpoZMqL2Dubopqiwe5Jc_YAcaz2UNQIrAhNMZefRMy7eGlRaDHJlgvid4GHZ3KESi4kURHiP0K5KWmchtsSEk7uRuY55ZSg1xfF2ag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/209278afcc.mp4?token=Vu7yMg-1ROVrkAXJZa8iXf4AYDHS9D7TILbpYW5QpcQovg3nqfP5NDMIPCkKWEfek76Ui2lcL0n37_iRSh0MkSIIy4HcWPR4_QmLNLoeUyFVLr_O1i_PFfCNeCjVIq5RntUvlmd2HH7xGJ6XgI0TXYzUHwZFmJHHQMTXEWq5DKwHiwgLxP-aFHUXzHnVhZ39kXBmKPBf72rnRrf1UgyYA97JDypjbZmGtBhEURlZvm10YxcaZpoZMqL2Dubopqiwe5Jc_YAcaz2UNQIrAhNMZefRMy7eGlRaDHJlgvid4GHZ3KESi4kURHiP0K5KWmchtsSEk7uRuY55ZSg1xfF2ag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇸🇾
بعد از حذف شدن سوریه از کشورهای حامیِ تروریسم؛
احمد الشرع، رئیس‌جمهور سوریه، به یکی از فروشگاه‌های دمشق رفت و اولین تراکنش پرداخت با ویزاکارت(کارت بین‌المللی )رو انجام‌ داد...
@News_Hut</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/news_hut/70726" target="_blank">📅 21:15 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70725">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/944309cb4f.mp4?token=LunrzEWYzRy_dBi7wv6GV9NBHC4nW8JA06uQSTVsGhe3xO4VstlHaCcA1vuZYBwp8v2bG86CfLlu7mwDdQSC6F_P7FCDPsJ6euRM4wUMEQiGDAxMxnJwh3Z3CMejdUrudQRpxt5IHXawuZElMf73WGBMldlWdT8ulSMo56n7UnXf0vkJdNQhWNxQnFEdd4VP8vJizKdADc69EoHG7DWnIUsL6juSvhqayx46SttxzgrDuKGtLipcWqLWS0HV6-BvdDzfXcOsFWXdhj3xLqZmcj3RYI4OG7OIz3bVg8RRozNMpn9MupX0Qvjf_4V7hL4xiGpc4aon1W1DthI_5I_4jQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/944309cb4f.mp4?token=LunrzEWYzRy_dBi7wv6GV9NBHC4nW8JA06uQSTVsGhe3xO4VstlHaCcA1vuZYBwp8v2bG86CfLlu7mwDdQSC6F_P7FCDPsJ6euRM4wUMEQiGDAxMxnJwh3Z3CMejdUrudQRpxt5IHXawuZElMf73WGBMldlWdT8ulSMo56n7UnXf0vkJdNQhWNxQnFEdd4VP8vJizKdADc69EoHG7DWnIUsL6juSvhqayx46SttxzgrDuKGtLipcWqLWS0HV6-BvdDzfXcOsFWXdhj3xLqZmcj3RYI4OG7OIz3bVg8RRozNMpn9MupX0Qvjf_4V7hL4xiGpc4aon1W1DthI_5I_4jQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇳🇵
ویدیویی دیگر از آنچه در نپال رخ داد:
@News_Hut</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/news_hut/70725" target="_blank">📅 20:39 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70724">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Pxip_QGJyyBiE7YwT-6XISecUnItXKNnhvs83pcq1lymo5Zq0MxSAwif-nKRfgrTGTZsWpsr_dFmLslHtjaKOb97e7IGeDBJTRG3849eNyu6RABMi2zwKw3UTlKJkd1PfmtXXg_d-NiCqjmxzdnypuxj9mEJEjdYkn7xgjgj8AjM05ZpCe_J_YHsbNeIaUAhQijiR51PFDcE2LoCRRqZeiuB0IGtkByGfr6yAygwVzMUv2nhssWWT9I4KYrPxRY-uF-qxQoanEW5_kBhoDtGVS_xLKzQPk4Bo9M0VxBT0BUy0H8Ru2FKvsprJLUUDJGqOZSBZD1QWpvKxtWiuNbY8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇺🇸
اسکات بسنت وزیر خزانه‌داری آمریکا:
وزارت خزانه‌داری وعده داد که تمامی شریان‌های حیاتی اقتصادی باقی‌مانده برای تهران را قطع کند و سرانجام به تهدید ناشی از رژیم ایران پایان دهد.
ما همچنین هشدار دادیم که حامیان و تسهیل‌کنندگان فعالیت‌های ایران نمی‌توانند همچنان از دسترسی به دلار آمریکا و نظام مالی جهانی بهره‌مند باشند.
بانک «مصر» (Banque Misr) در امارات تصمیم گرفت این واقعیت را به بهایی گزاف و از طریق تجربه‌ای دشوار دریابد؛ و امروز، ما نخستین گام را برای پاسخگو کردن این بانک در قبال حمایت‌های مستمر و فاحش آن از رژیم ایران برمی‌داریم.
امروز، در چارچوب «عملیات طرد اقتصادی» (Operation Economic Outcast)، شبکه اجرای جرایم مالی وزارت خزانه‌داری آمریکا (FinCEN) مقرراتی را پیشنهاد کرد که دسترسی «بانک مصر» (شعبه امارات) به خدمات بانکداری کارگزاری با مؤسسات مالی ایالات متحده را لغو می‌کند.
علاوه بر این، دفتر کنترل دارایی‌های خارجی وزارت خزانه‌داری، «رضا محمد تأیدی» — مدیر شعبه دبی بانک ملی — و همچنین یک شرکت پوششی مستقر در هنگ‌کنگ را که در پولشویی وجوه برای یک صرافی ایرانیِ تحت تحریم نقش داشته است، تحریم کرد.
🔴
«عملیات طرد اقتصادی» در حال قطع آخرین شریان‌های حیاتی مالی است که رژیم ایران را سرپا نگه داشته‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/news_hut/70724" target="_blank">📅 19:50 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70723">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q4qw7bb4BfkOuGmtJ43nhVJkXnukuJiPaqlsvFksCc5iXfZtwuhcDmwZK8fdmCDMjEZDfG2YzoZdMQ4dowOJuCOu1zivLb8ar3sLFrYROHVKN8bh496Wjxiw8jqj-9tX3rJPItksAoVxwhc33xwOmt_v289FssDtWtw0ywOreUb8E3qxO71WT81qCJeKS7WrOrSBPWJMbOQCMbQojYfR43bRJidkMYDahFQBuUoLb9OpJzMF59lyLjIYLT2N-vQvjFwQpjis-wm2QWaO0ARGZVZWYftWadmtAeru9sQR1Lg2x24uKks80nfAIOH_US-DCZ-skEIX4tJgC4bHgcx7NA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
🇺🇸
ترامپ: دیگر خبری از آن آدمِ مهربان نیست!
@News_Hut</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/news_hut/70723" target="_blank">📅 19:08 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70722">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eea13a9b78.mp4?token=A0E6zcSjMfiDUpVhZtXD9s2BYxqNWl-c2wqPW1Zu8F_RVlQ10nkHenG-ioQ87jNG1t0yCNTxCtnWgh7HUNVnCI5j2vBq1oOuiPXMTeXwxWRahK2hq1GhqC3SKmt5kKAY19HZpPI1M1dJ_1lai7lHQsPL0nl-vo-N9vqEWcS0pTf_x9qpd9v5ITdNEWlXpT1VUl3ndlQWPlybSfnQD95fi6QeuzsrqYIjNGhbHxnv6C-kEcj280AyFOMLs_0QGlqcT1Fjm7gqMbc8KImmvN-dolflhCQcWYdy-uvpY7YmCfWfFJ68XKbse9PVty2xEjt7iLKti8SPs6_ScmaKxu6AIw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eea13a9b78.mp4?token=A0E6zcSjMfiDUpVhZtXD9s2BYxqNWl-c2wqPW1Zu8F_RVlQ10nkHenG-ioQ87jNG1t0yCNTxCtnWgh7HUNVnCI5j2vBq1oOuiPXMTeXwxWRahK2hq1GhqC3SKmt5kKAY19HZpPI1M1dJ_1lai7lHQsPL0nl-vo-N9vqEWcS0pTf_x9qpd9v5ITdNEWlXpT1VUl3ndlQWPlybSfnQD95fi6QeuzsrqYIjNGhbHxnv6C-kEcj280AyFOMLs_0QGlqcT1Fjm7gqMbc8KImmvN-dolflhCQcWYdy-uvpY7YmCfWfFJ68XKbse9PVty2xEjt7iLKti8SPs6_ScmaKxu6AIw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یه دوربین مخفی ضبط میکنن از رفتار جامعه با دخترها و پسرها؛
وقتی دختره بنزین میخاد صدنفر برا کمک بهش می ایستن
ولی وقتی پسره درخواست بنزین میکنه حتی یه نفرم حاضر به کمک نمیشه
🙁
@News_Hut</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/news_hut/70722" target="_blank">📅 19:05 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70721">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/70721" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/news_hut/70721" target="_blank">📅 19:05 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70720">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AnegxZ1H_JDBSpzE_jJdwEAMVv06ftMlaNljfu3susokIDw3rG2KRFax8TwrKHBUqGfMChIeyM45C5CkniiMzIpoGJwceliRi8qmy4UYzSeL3pKrgxOhUXPN9uBhGYKLyfeI7Y9DaVAZZoLplyKA-8fdzSzKHxKBEyT3005rmMuT2l9Tc3xoQMnXs_IlovtzUHzNr69jGCUOpqOZtQGP2adsMpZiqJc2jSpyJiTwOzUdA4XOFzsYLjsBFSHiOxmNIKHxI_bve4VGzny27pdMIRLJd7jVvYzZ_U-EItdQqPc5dyIU9vIsyD3SGD5CFeTmtW0OZN5GbQllWCWQtI9qmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
مچ‌های مهم امروز در سایت بین المللی
TrexBet
منچسترسیتی
🆚
کریستال پالاس
ویارئال
🆚
آلاوز
ونیز
🆚
میلان
اشتوتگارت
🆚
بایرن‌مونیخ
پاریسن‌ژرمن
🆚
لیل
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
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/news_hut/70720" target="_blank">📅 19:05 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70718">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e98c21e852.mp4?token=FFksDvsk9FQuVwi2NCtSToFwPcabo1TuVIv9m0nsiqZiYZSK7BKo8Kq-yENTUlivG8yagHvCIYNV1DnFMHC56QHHWF2URgv-PvVMmjps8UdlrbR1VndmwB4t4YUUtC-0RT0Ebrde6cMvpMMawFkO01TzLnLiKxgGT3yCoBXci2gE0bzyEL2yhHS7qtVNCO6ysaVjGTWq9-PpwNkXjfFUjcC-YJ5BbSkPJdG3B0z5shLSeFCqNzykqH5wWj4Hx_7qsBAn_2q1J91-N1Em7Y1kOexIwxRnnVckE6gQFUO_o11Gk3EBkb_jGsMZD9V3fY1A6600S_HwEKzVBkhhqQyTuQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e98c21e852.mp4?token=FFksDvsk9FQuVwi2NCtSToFwPcabo1TuVIv9m0nsiqZiYZSK7BKo8Kq-yENTUlivG8yagHvCIYNV1DnFMHC56QHHWF2URgv-PvVMmjps8UdlrbR1VndmwB4t4YUUtC-0RT0Ebrde6cMvpMMawFkO01TzLnLiKxgGT3yCoBXci2gE0bzyEL2yhHS7qtVNCO6ysaVjGTWq9-PpwNkXjfFUjcC-YJ5BbSkPJdG3B0z5shLSeFCqNzykqH5wWj4Hx_7qsBAn_2q1J91-N1Em7Y1kOexIwxRnnVckE6gQFUO_o11Gk3EBkb_jGsMZD9V3fY1A6600S_HwEKzVBkhhqQyTuQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
مجری خطاب به آخوند:
یه چیزی بگم باورتون میشه؟وقت تموم شد.
🙁
واکنش آخوند:
خوووبه؛اگه اینجوریه که من دیگه اصلا نمیام اینجا.
@News_Hut</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/news_hut/70718" target="_blank">📅 18:32 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70717">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/55129dd199.mp4?token=pfnI5cDAe3q3GPDPvGIVESJey84sex7LpJTHSjlxAbOFOsmxo9tQz5Uh01gQ9XpEhCcgtdRz0E6L41Q3qIR8ngfX5X2J6UQBJTEDPsDyJEvjiaES35GbiSXKVx5rSgPycDWAITz9kd9IOmoc-pNw8FmpWyBnsTLT0YNAHXzwSpaDJbQKd_WTrbxV4gfsIebK5fxOdVZxPopa6aw8w7WuCLwQd_QhIQqtEjENwIpsPsngubW7E11hhuiQbq_DCUiuo327vmNBz1eoZIZoZCldzd7U9LZZ__YpAnc7M1VJjPQyhJk-f2eetDkcrqPWbvuzlp7yGsRWwgNMU_pAWlp0ag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/55129dd199.mp4?token=pfnI5cDAe3q3GPDPvGIVESJey84sex7LpJTHSjlxAbOFOsmxo9tQz5Uh01gQ9XpEhCcgtdRz0E6L41Q3qIR8ngfX5X2J6UQBJTEDPsDyJEvjiaES35GbiSXKVx5rSgPycDWAITz9kd9IOmoc-pNw8FmpWyBnsTLT0YNAHXzwSpaDJbQKd_WTrbxV4gfsIebK5fxOdVZxPopa6aw8w7WuCLwQd_QhIQqtEjENwIpsPsngubW7E11hhuiQbq_DCUiuo327vmNBz1eoZIZoZCldzd7U9LZZ__YpAnc7M1VJjPQyhJk-f2eetDkcrqPWbvuzlp7yGsRWwgNMU_pAWlp0ag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
چرا یهودیان بهترین بی‌سیم‌ها و شرکت های اینتل و راکال رو دارن؟
⏺
مهدی طائب؛ کارشناس مذهبی: چون حضرت موسی یادشون داد.
@News_Hut</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/news_hut/70717" target="_blank">📅 18:00 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70716">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/508daa856a.mp4?token=g16Sp71EWYgVOPky13zKBylBhN4bpHQ2W_8wMzZyF1H-Us5ubp7dEg2jMorXvC6s-yNQdZTErV4w-Nnz3lOraYQy10lX_h7tX-J1HGO-5Z2yFIotVFfw5lFnT7LAYSpig3PwQ5ZJWyEAHoYZ9ltVd4ErE70VfJponfm8_oziA5MmgiEA8TQu3UW4Hgqy8TbWIdB5LBTIMWQX-qDz8oYgThonzKidY6LXcWR1MqX60cFMq43BoGrgmqMH4ENH3aEOUfV0X_G5GxXCI-oz0dwaT-UPrsmJgk5DrSyEWOCaezrusl4OQeZuf_9LgxGvywJoAp3W1MGowjtOGdzHT0n-fQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/508daa856a.mp4?token=g16Sp71EWYgVOPky13zKBylBhN4bpHQ2W_8wMzZyF1H-Us5ubp7dEg2jMorXvC6s-yNQdZTErV4w-Nnz3lOraYQy10lX_h7tX-J1HGO-5Z2yFIotVFfw5lFnT7LAYSpig3PwQ5ZJWyEAHoYZ9ltVd4ErE70VfJponfm8_oziA5MmgiEA8TQu3UW4Hgqy8TbWIdB5LBTIMWQX-qDz8oYgThonzKidY6LXcWR1MqX60cFMq43BoGrgmqMH4ENH3aEOUfV0X_G5GxXCI-oz0dwaT-UPrsmJgk5DrSyEWOCaezrusl4OQeZuf_9LgxGvywJoAp3W1MGowjtOGdzHT0n-fQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
پشماتون بریزه؛ یه پسری داشت توی خیابون قدم میزد که یه پیرزن رندوم برگشت بهش گفت: تا حالا کون کردی؟ دوس دارم منو از کون دار بزنی، حشرم بدجوری زده بالا
😐
@News_Hut</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/news_hut/70716" target="_blank">📅 17:33 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70715">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/65902c1b90.mp4?token=IetUKvSxhICU4qrZc5DoSXQI3DF3fQoqiy3_hBUGjrNnoN0zq-4eqnkJLPXbwZ5AbzSKaFWn5zZi767FzsfsXoTL6_EY92yUiRMpaHkUMLC7KpxVF2fN4gA2yuFWlIpl0SOuZo3YieHvhTu9fEb4ODRAHZjfzA4PxX3cHqHMe-Ribl48B_Ev97b15l1btYuGKkm33rlUzEgCuE1lphgIRxnXBtABGhtKXUNBcPKWijANaWgD4F-UfXl-P0FT2L2t6XOG16nV0E6YPiNBJqAK6zia3OHE7AoO5T9oCQL1xVw-sYAQ3gVJiWyCKQW0VvX3ilP9OcdwDZFejsm993TIxw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/65902c1b90.mp4?token=IetUKvSxhICU4qrZc5DoSXQI3DF3fQoqiy3_hBUGjrNnoN0zq-4eqnkJLPXbwZ5AbzSKaFWn5zZi767FzsfsXoTL6_EY92yUiRMpaHkUMLC7KpxVF2fN4gA2yuFWlIpl0SOuZo3YieHvhTu9fEb4ODRAHZjfzA4PxX3cHqHMe-Ribl48B_Ev97b15l1btYuGKkm33rlUzEgCuE1lphgIRxnXBtABGhtKXUNBcPKWijANaWgD4F-UfXl-P0FT2L2t6XOG16nV0E6YPiNBJqAK6zia3OHE7AoO5T9oCQL1xVw-sYAQ3gVJiWyCKQW0VvX3ilP9OcdwDZFejsm993TIxw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
ویدیو وایرال شده از پسری که ماکت آیفون رو میگیره دستش و زیر ۵ دقیقه ازش میزنن!
@News_Hut</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/news_hut/70715" target="_blank">📅 17:00 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70714">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/50851d2a93.mp4?token=NKSnPLojMLwcameanZdBf2kCJuc0ZVFEtWkccUFFnBYFc8ZsMMRvP_6PviItSu8Fi47uahUOHplTegKaQw_LnBT7B8kEhnVaVxxGSMPkYlrRdHP_hlA4lTlccI1oKJAFDXLAdeK9EaySfxc1aViUeBhY6nTOv76g4Z56LFrBOVMMt2bFexOmJ069kJEWHHGmhpI5evyRQE02V6naog4LjDJU3cKsOgrRzCGlqHqr2XoTvdC2X4BBFJh0NDV9DO1jWytkqzBK3P5hGK-VMzABj2eD91dEyjo9ZuOsSLanp7JYcNrrVSZP94CuFlgekOUPN1d3k77aaTOnOVCtl5-f0A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/50851d2a93.mp4?token=NKSnPLojMLwcameanZdBf2kCJuc0ZVFEtWkccUFFnBYFc8ZsMMRvP_6PviItSu8Fi47uahUOHplTegKaQw_LnBT7B8kEhnVaVxxGSMPkYlrRdHP_hlA4lTlccI1oKJAFDXLAdeK9EaySfxc1aViUeBhY6nTOv76g4Z56LFrBOVMMt2bFexOmJ069kJEWHHGmhpI5evyRQE02V6naog4LjDJU3cKsOgrRzCGlqHqr2XoTvdC2X4BBFJh0NDV9DO1jWytkqzBK3P5hGK-VMzABj2eD91dEyjo9ZuOsSLanp7JYcNrrVSZP94CuFlgekOUPN1d3k77aaTOnOVCtl5-f0A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یه نفر با زنش دعواش شده و رفته جدا خوابیده، و اما آخر شب برگشت تو اتاق پیش زنش و این شاهکار رو خلق کرد:
@News_Hut</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/news_hut/70714" target="_blank">📅 16:34 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70713">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0c52147d4b.mp4?token=YmX74AC2Hlq9IUMd3ntxaeJRQMyoyzsV0iSeGvNLw21JTcnT3_Pt95Zq1yWTr8nxX1uhrIDP-rOp1VJCqy2yJlI2tpjywQywIfD3IQH_IsnCMTAX7npC9fZGMOKiw5KakqdSqtgn02rbXTcZy5TrGJKNEbJhfi_HqV4u-ifEMF_1fRifAKtWeUkkmBj-THDRZhDdWmKcA-1QtiiJduAZ8KzfVvBw2RW1DZ5CKM0KcseMjrkazGn4XF_4bs8r02AvYCOIabJZq2RnC8TbNeOdLP0ylX09IgC1wxOujQgMfFXkiUQe3vajEzKy5N0LYhrvgfvPWW3bi9xVtJIfg53O1E7ZhDcc3tixenpmtAKY6iAX_sxxj0uxnbQ0CUvoLeuHqzWDO2YfmaR273c826admjLwxnvPWoz6xeItu4A6CK3_AWQNUTNgdME5Ei-z7FJQXVeZsRDDNycVCiy3BWJAmCXVqALumsDLWnVyRltqOXI52fN5et5cGeEgbrA526iktaQG5rB2NPMZmDT8PoB0FZt6knReGCud53XElneDoPJ7qmi-smhqZ55U7GWk3jgeWFlg51w4PUSjGZVvfBI2oQmmMX9GLqOpno5K_bJV9k5h6gdG9NygUycBlv65fYGCYvXmvPoR6aUnDBKwWV-yMpO0lDJVMFbq76j9wOwdJd0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0c52147d4b.mp4?token=YmX74AC2Hlq9IUMd3ntxaeJRQMyoyzsV0iSeGvNLw21JTcnT3_Pt95Zq1yWTr8nxX1uhrIDP-rOp1VJCqy2yJlI2tpjywQywIfD3IQH_IsnCMTAX7npC9fZGMOKiw5KakqdSqtgn02rbXTcZy5TrGJKNEbJhfi_HqV4u-ifEMF_1fRifAKtWeUkkmBj-THDRZhDdWmKcA-1QtiiJduAZ8KzfVvBw2RW1DZ5CKM0KcseMjrkazGn4XF_4bs8r02AvYCOIabJZq2RnC8TbNeOdLP0ylX09IgC1wxOujQgMfFXkiUQe3vajEzKy5N0LYhrvgfvPWW3bi9xVtJIfg53O1E7ZhDcc3tixenpmtAKY6iAX_sxxj0uxnbQ0CUvoLeuHqzWDO2YfmaR273c826admjLwxnvPWoz6xeItu4A6CK3_AWQNUTNgdME5Ei-z7FJQXVeZsRDDNycVCiy3BWJAmCXVqALumsDLWnVyRltqOXI52fN5et5cGeEgbrA526iktaQG5rB2NPMZmDT8PoB0FZt6knReGCud53XElneDoPJ7qmi-smhqZ55U7GWk3jgeWFlg51w4PUSjGZVvfBI2oQmmMX9GLqOpno5K_bJV9k5h6gdG9NygUycBlv65fYGCYvXmvPoR6aUnDBKwWV-yMpO0lDJVMFbq76j9wOwdJd0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
سخنان ویرال شده از یک آخوند اردبیلی که درحال وایرال شدنه؛
تو دنیایی که جوان نمیتونه ازدواج بکنه ولی میگن عیبی نداره تلاش می‌کنیم درست بشه
تا متخصص های شما وضعیت رو کنترل کنن جوان مملکت از گرونی استرس اضطراب سکته میکنه میمیره
جوان ۲۵ ساله شب میخوابه صبح بیدار نمیشه این خیلی حرفه
میگن بچه بیارین آخه بابا پوشاک شده ۷۰۰ هزار تومن شیر خشک شده ۳۰۰ هزار تومن لعنت به قبرتون بباره از کجا بیاره آخه بیچاره
میگن آخوند میره میخره بابا بیا منم عمامه رو گذاشتم زمین
اینا همش شده شعار به ولله نیازی به مذاکره و کشور های دیگه هم نداریم مسئولین ما بی عرضه ان
ایران‌خودرو شده مافیا برا خودش چرا جلوشو نمیتونین بگیرین؟؟ ولی واس یه تار مو میکشین واس یه قسط عقب افتاده میندازین زندان
جلو اینایی که زیر سایه نظام گردن کلفت کردن رو بگیرید ننگ بر شما و حیف این ملت که دست شماس
@News_Hut</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/news_hut/70713" target="_blank">📅 16:02 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70712">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/80bc2fd38e.mp4?token=t3F0Pv1hfNZMDRH_zhAHWx_CWt6n5YT7dhPtdA_59B281DuO4f27vH8Tx0h7ORrnj4S21f-B_807zbf--b76p6pVcgUSsmyf31HEoth5VciO4O9VF970vOvgzX2XicGFNwhn_MW6JLqupzbXP9CqXmy2K4Am3_rdMO3KVtr4hjORORWXjkClVB8BWPf4TQhH5TZmv6zRh2a-jbTfeekLqlVYMHKCCEbnC_cAv5I1KkJ0UsDhkKMVrC2VgkLCHzWm8yibDscyTJHDKEBLMA2WzHx4LcAd7Q9WkbFko7nDgzUtOQ8yOI26cPpJAFsNWwPyeiaAn3Ik1hCnoE6WXUe58A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/80bc2fd38e.mp4?token=t3F0Pv1hfNZMDRH_zhAHWx_CWt6n5YT7dhPtdA_59B281DuO4f27vH8Tx0h7ORrnj4S21f-B_807zbf--b76p6pVcgUSsmyf31HEoth5VciO4O9VF970vOvgzX2XicGFNwhn_MW6JLqupzbXP9CqXmy2K4Am3_rdMO3KVtr4hjORORWXjkClVB8BWPf4TQhH5TZmv6zRh2a-jbTfeekLqlVYMHKCCEbnC_cAv5I1KkJ0UsDhkKMVrC2VgkLCHzWm8yibDscyTJHDKEBLMA2WzHx4LcAd7Q9WkbFko7nDgzUtOQ8yOI26cPpJAFsNWwPyeiaAn3Ik1hCnoE6WXUe58A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇷
سخنگوی دولت:‌ مردم منتظر بهتر شدن وضع اقتصاد در سال آینده نباشند
@News_Hut</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/news_hut/70712" target="_blank">📅 15:32 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70711">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">⏺
🇺🇸
پروفسور جان مرشایمر استاد علوم سیاسی دانشگاه شیکاگو درباره اینکه چگونه تحریم‌های آمریکا می‌تواند منجر به اقدام تلافی‌جویانه ایران شود:
در سال ۱۹۴۱، ما یک محاصره نفتی شدید علیه ژاپن اعمال کردیم و دارایی‌های این کشور را مسدود ساختیم. ژاپنی‌ها در وضعیتی بسیار وخیم و درمانده قرار گرفته بودند.
آن‌ها تصور می‌کردند که ما با آن محاصره اقتصادی، بقایشان را تهدید می‌کنیم؛ و در نهایت، دست به حمله علیه ما در «پرل هاربر» زدند.
به گمان من، شما نخواهید توانست ایرانی‌ها را به زانو درآورید.
اما اگر بقای آن‌ها را تهدید کنید، آن‌ها دست روی دست نمی‌گذارند تا صرفاً محو یا تسلیم شوند؛ بلکه واکنش متقابل و سختی نشان خواهند داد.
@News_Hut</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/news_hut/70711" target="_blank">📅 15:06 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70710">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🚨
📚
#فوری
؛نتایج امتحانات نهایی تیر و مردادماه پایه های یازدهم و دوازدهم در سامانه بینا منتشر شد.
🔴
آموزش دریافت کارنامه :
۱. ابتدا از طریق پنل سنجش وارد بخش ثبت نام در آزمون شوید
۲. ورود به سایت آموزش و پرورش
۳. مشاهده سابقه تحصیلی و ثبت نام ایجاد و ترمیم سوابق تحصیلی
۴. ثبت نام ایجاد و ترمیم سوابق تحصیلی
۵. بعد از ورود به این بخش از سایت وارد لینک سایت بینا شوید.
@News_Hut</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/news_hut/70710" target="_blank">📅 14:37 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70709">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cc088cfcb6.mp4?token=r45d25BQpTa_qfAvFHTmOysRmak3CsMPO7ESJ2Ojeyyip-XWExSKf-p7nPiqj1XR-Jx-1N2S_aCWXEc81gwly6-MYE9qCOs6fUvAYgjKOqfxdpCay1LE1PfGRx4X4FjUQ8dIpvvM2sIISLY3EVD_xVK8WUcu6jYiJT6ustEQ45lmObKV4pEJD8SyvsHDAGmr5uu9Qj8tE2qcPer_Nb-Lu1Bk5qSls0vjJ9MO7JXL5z1k6jtGWWhyOs_nO02mR0xju6GZItPcWHeVIVjuCjAGBOArBiMXoDWGHDEdyfkda2mejjfy_NsCxsR957oAk3YgHTj1j9nHRwcTN3oVJfewTQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cc088cfcb6.mp4?token=r45d25BQpTa_qfAvFHTmOysRmak3CsMPO7ESJ2Ojeyyip-XWExSKf-p7nPiqj1XR-Jx-1N2S_aCWXEc81gwly6-MYE9qCOs6fUvAYgjKOqfxdpCay1LE1PfGRx4X4FjUQ8dIpvvM2sIISLY3EVD_xVK8WUcu6jYiJT6ustEQ45lmObKV4pEJD8SyvsHDAGmr5uu9Qj8tE2qcPer_Nb-Lu1Bk5qSls0vjJ9MO7JXL5z1k6jtGWWhyOs_nO02mR0xju6GZItPcWHeVIVjuCjAGBOArBiMXoDWGHDEdyfkda2mejjfy_NsCxsR957oAk3YgHTj1j9nHRwcTN3oVJfewTQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇷
ویدیویی که بین طرفداران حکومت در حال وایرال شدنه و دارن میگن به زودی این صحنه از صداوسیما پخش می‌شه؛
@News_Hut</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/news_hut/70709" target="_blank">📅 14:31 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70708">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🇹🇷
شرکت‌ترکیه‌ای«روکت‌سان» (ROKETSAN) با موفقیت موشک کروز جدید خود، «چاکیر» (ÇAKIR)، را از یک پرتابگر زمینی آزمایش کرد.
این موشک با بهره‌گیری از جستجوگر فروسرخ تصویریِ نسل جدید، اهداف زمینی و دریایی را با دقت کامل (اصابت مستقیم) هدف قرار داد.
این آزمایش‌ها همچنین قابلیت افزایش برد موشک را به واسطه سیستم سوخت جدید، تأیید کردند.
موشک چاکیر که پیش‌تر از سکوهای پهپادی پرتاب شده بود، اکنون توانایی شلیک از خودروهای زمینی را نیز به اثبات رسانده و قابلیت یکپارچه‌سازی با پلتفرم‌های گوناگون را نشان داده است.
@News_Hut</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/news_hut/70708" target="_blank">📅 14:30 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70707">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/70707" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/news_hut/70707" target="_blank">📅 14:29 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70706">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KK9nc7DBqWQcKQI8BaUNnIAr8Tj0fblGDn1Pz-GjlQfSJbeh9O9Z--MXYZJ-uIs2GHfrd_jB5M_3U5qVQsqiN21bH71Er75MBty_rFvNjEwak-m016jXi84JmWv3lXC6-ZsuA8gvi6Gs1TgdB4W1nAOMala6qwKVERqIPLyYb0RXolzGcHqxurUpuZIBI-DVZ-x4PqM7nWEn0cd_tn05tG_2OK-nBFwnfepIN5za-gUWDbmkK1dSG17QIo7TJMIO25QRhZ8OG4I6NFFDj_GVAr86oS99Sa2LhBott1tiMW2Es4Lau1se5z98ILEw4UKB6891oPEQMy_fKLIBhWSpfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
نبرد جذاب فوتبال ایران را در
TrexBet
پیش بینی کنید!
🦖
استقلال
Vs
فولاد
🦖
جمعه | ساعت ۲۱:۰۰
🦖
ورزشگاه شهدای فولاد خوزستان
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
🦖
هیجان بازی، وقتی بیشتره که انتخابت حساب‌شده باشه!
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/news_hut/70706" target="_blank">📅 14:29 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70705">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9e90df5a6e.mp4?token=t_IlkXV-hU3TDONRcbVed-PbWZbAR_Dy0O2d0DzpkI-loxheABJeqIK0ebdNrULGEkV4n9qfgewPT1qZaHA6N9xWB6MrLU_3KsU-Xg2ayL5blxP65C8mmvPG9_YBZIpcvcQySSAkFgSLrqT7BXdDycrVKMjyIgXQzc-AGQQ_YEi-nFoy75Uxb0TQRmmSNPayR45tGE5-WBTLfTrcTaSQluNWNSSxp00PeqR59_GKw2NrRLZA0nHaZ07E0eJLzU0X45PuMQaUnoPdZlwoaoMPLzON6ao970cgk2YtIYwWQGMxXV-e8Gc1fmIAqUp7IoTZrtFsPriHGyktm7S3qtWZ_Yi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9e90df5a6e.mp4?token=t_IlkXV-hU3TDONRcbVed-PbWZbAR_Dy0O2d0DzpkI-loxheABJeqIK0ebdNrULGEkV4n9qfgewPT1qZaHA6N9xWB6MrLU_3KsU-Xg2ayL5blxP65C8mmvPG9_YBZIpcvcQySSAkFgSLrqT7BXdDycrVKMjyIgXQzc-AGQQ_YEi-nFoy75Uxb0TQRmmSNPayR45tGE5-WBTLfTrcTaSQluNWNSSxp00PeqR59_GKw2NrRLZA0nHaZ07E0eJLzU0X45PuMQaUnoPdZlwoaoMPLzON6ao970cgk2YtIYwWQGMxXV-e8Gc1fmIAqUp7IoTZrtFsPriHGyktm7S3qtWZ_Yi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تیزر سریال مرد هزار چهره هم اومد و مسعود شصتچی یه جایی عضو تیم مذاکره کننده هم هست:
@News_Hut</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/news_hut/70705" target="_blank">📅 13:54 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70703">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/N0qxKDzS_OnbJ7HtA1gQZudIkdlH3PmBthMRn_J4Htc_-PHnsFakVbR7UVqN5cDTl2biPD1WZ1QYrJdv6D3Mn0yrVZaJo2RqrN1GEs6rBzZMIbm2CG46CckILM6jb_Z-HzRh8wlreWfsEyqo1xZmlm4tIJ8td8lMQ9h3rqZfwXq5FLXHTODs0jR3EsAehHwdi2s8RR4r-yep-MvDCgCIdaQeArDXKx6Begsg8vJHUitoOoT2IGmllKIuIzkCTdiYAt9QhOejMJlMznoADzqHtrDlruSEQKVfNL89JvP_7NKwj54eMnjeQNV02ACmb2fTPCU9KSKkhnyrf1HhLeah1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PZDqcdSmDdMullMQha2hVrr-XNRl9OPNAjKND188FlPeZdUDEPg7EL2yl4y1z_Zdez8CB-wLyeKKh7f_ckGrgxYJnoRKLmYY4xtz13bWveZpuxu4-OL5df1Ppe5WIdE6cUW5genitg1C-C8alKw8ZrRKZyek091lwnwZ6fgcALevTSHfMbpbRx3AOd7stiRN_bDfhGVOQO3BYPMDQsD2OpC3i0Bq1brbSjeISp1WYz2oQX8fO_RT3VLUcpFuwQ-dNCvVt5tweVqC8lt9x4PU53Rbu5P4i5_Ndz0-UDL4uK1a2nt9svNHiMq20liAdPZppS0s7s_karlX_-DH9c1eoA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇮🇷
بیانیه وزارت امور خارجه جمهوری اسلامی در رابطه با تحریم ها:
تمام کشورها موظف هستند از اجرای تحریم‌های یک‌جانبه آمریکا خودداری کنند، و تحریم‌های اقتصادی آمریکا علیه ایران غیرقانونی و کاملاً غیرموجه است.
استفاده از دلار توسط ایالات متحده به عنوان ابزاری برای ایجاد ترس و فشار بر سایر کشورها به منظور وادار کردن آن‌ها به پیروی از سیاست‌هایشان در قبال ایران، نقض حاکمیت ملی کشورها و حق آن‌ها در تعیین سرنوشت خود است.
همچنین، تحریم‌های آمریکا به عنوان نقضی آشکار از منشور سازمان ملل متحد و اصول عدم مداخله در امور داخلی کشورها و همکاری بین آن‌ها تلقی می‌شود.
@News_Hut</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/news_hut/70703" target="_blank">📅 13:32 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70700">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/X4NGgZQXOF2sLp0KclqvGOKbLO1MY6WsOfe-2yhA2CketCKD2o3ADRbkXC_S3CaC8yvEpfkDcdsFmDvv0uGiZThUkw30WdoCOGbausGUVZMZqlJdPffCc2ZyOefAWOFJH3YcgL-HFnUErQS1aUYlLnNaQWiopFaFcDnSxHaNag9xYIiGn-rYOgQPg5tuylx3S_aMWDm4WlA-H3QeHBH3V-6EXfpc3td9F2RjhZnsoQy4ZCgg5RjMjiHpwvKpso75NT0OsJv-DWtNNLloQMYz-5wrA_lBGgCzqdClNGAPWHNNvb4eXAdJUuidXF0BNELO64xCSOwSYr5z5iMpdn4LPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/AgO6fojeTarjbZbJQl51WnmdGsdrMbZuGBxcyRJcs6rGpSzaHRyL78h5oRZktthaHFE3Rv-mdOcklWZzzUILksXyEWWudBRuomoKxZ113m-4z4Fipn9GmsF1xKGAXrtoR1VGHMELOh3xx5acgQl1ew1xJTLLEV1eyI8vJgLM-EVvcDKxqm3t28hS-x7NeNIPVc5dPC7ILbF1ttqf7Y4P3jmpEfDEda8441wNhy6RrwIO8kionOw7NM1hfHJJqML7HXyR6hMuWrtm7I8T9TgC-0xn8lcCgTp4R-QeNfwtRRrZFjX7emPCl5fvJqeQCEgz18gvHbV7zRzs2I_Vpvsj8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/rlLU7O24PnSyWbNVLwD6pCgezTIKQun4GvkzqmV3ZL1i466hBj-ZJ8BCsXSagHTwd_-lHjkP_drIDqd11rSRc8X8G-zXFVBkpjZJeWtt69pjjfYR98Rzqhi8YCTOsZQgjQX6aH9IiEHPb2vyBSp0GEVSu_OfD4YU_ZUbHcARb2gHFNhagcAOZc2L-CrsW69z9en0osQeLvBzKjP8_VbeqMV-SnIkgx-HE3_PM4YUnlKpUkgkxiFqmzhlpW3HuSF2LPshhT6OS7G7dtNoDFxWg2R9uOl1zRYqljYCVLdMRUKcEL5_7gUJmatCg9M4SOMV9i-xuE8LRGU79UTN1ROmuw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
نسخه پرمیوم ایران این شکلیه؛
عکسی که چند تا جوون از دورهمی‌شون توی تهران منتشر کردن:
@News_Hut</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/news_hut/70700" target="_blank">📅 13:15 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70699">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DJ_sByVU_hnq4pRCRPUbJGsx3qebw9PaDjcO0ZwC2GW_OttrhcbrdfSDMJ4zzAwrbS2EZ_wBZsBkkyG0xoemqdqaPNtUUtIDTnb6ecw_QzqzWDMTdqtwFmHnnjDv8cxCFG315t-tupS1_QX4fwCQnJtJebrQb8MIUqODw_YEy9Mg9D_an1Ursd84SwUY4DRnJNlpMWl04i1H_SrRuu1aHkSpkHDYsLExZngs65RfHgLPSbzY6fbnI3viPnaWq24FjcbK3ScsdxuG4-ibbtquD6FM4_W7CX__QeHajFgOLRGnSYMHFdxns9Hg-wlMd83tpcijbMdpPMW_ioMrLcIAhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
کافه بابک زنجانی که هفته گذشته افتتاح شده بود؛ به علت بی حجابی پلمپ شد.
@News_Hut</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/news_hut/70699" target="_blank">📅 12:33 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70698">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1291af3432.mp4?token=Wla0jbcWitrmBeG_xkMuBijwdScFfgDRVqxDSOVjwFJXTKr5HOOo4caky8Ije-DaFisI1FtRsB0SmvZGjo9naZiUi2VCUd3PSl7CWGAxI9Ag7IzjX0jGuKFx6WXoBWuy79C2syJRofP5T_9KWMV9S2EZrEYNhYLHUOTvT_URJWASQSwI5w1JhzDLrHUlvtSAbz70rPXUk2BNUnaCQDmUwnjkfffXZ9hSjKriiendl4L0bXLEV0NmHMNv5-6dOLc9JZVVO36vdeGzmEmaM36a3CMyRJDHzzpNJ7a19ht5inupk7fS2hxZN49fjDzCyi8kxN42YM4DeGDQRWD-CvBSRzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1291af3432.mp4?token=Wla0jbcWitrmBeG_xkMuBijwdScFfgDRVqxDSOVjwFJXTKr5HOOo4caky8Ije-DaFisI1FtRsB0SmvZGjo9naZiUi2VCUd3PSl7CWGAxI9Ag7IzjX0jGuKFx6WXoBWuy79C2syJRofP5T_9KWMV9S2EZrEYNhYLHUOTvT_URJWASQSwI5w1JhzDLrHUlvtSAbz70rPXUk2BNUnaCQDmUwnjkfffXZ9hSjKriiendl4L0bXLEV0NmHMNv5-6dOLc9JZVVO36vdeGzmEmaM36a3CMyRJDHzzpNJ7a19ht5inupk7fS2hxZN49fjDzCyi8kxN42YM4DeGDQRWD-CvBSRzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
〰️
فرماندهی مرکزی ایالات متحده:
🖥
من دریاسالار برد کوپر، فرمانده فرماندهی مرکزی ایالات متحده هستم و گزارشی عملیاتی درباره مأموریت‌هایمان در خاورمیانه ارائه می‌دهم.
۵۰ هزار نیروی ما در سراسر منطقه، ضمن حفظ جریان تردد تجاری در تنگه هرمز، با موفقیت در حال اجرای محاصره دریایی علیه ایران هستند. ما با بهره‌گیری از غواصان نیروی دریایی، نیروهای ویژه (SEALs) و توان هوایی مشترک، به دستاورد مهمی نائل شده‌ایم: پاکسازی کامل مسیرهای کشتیرانی بین‌المللی از مین‌های دریایی که پیش‌تر توسط سپاه پاسداران انقلاب اسلامی ایران کار گذاشته شده بودند.
طرح‌های بین‌المللی تفکیک تردد (TSS) — که حکم شبکه بزرگراهی حیاتی برای کشتی‌ها در اقیانوس را دارند — اکنون کاملاً عاری از مین‌های دریایی ایران و برای عبور و مرور کاملاً باز هستند. طی چند ماه گذشته، ما به عبور ایمن نزدیک به ۱۵۰۰ کشتی تجاری حامل حدود ۷۵۰ میلیون بشکه نفت خام از این تنگه کمک کرده‌ایم. در همین حال، به دلیل اجرای قاطعانه محاصره دریایی که از اواسط ماه ژوئیه از سر گرفته شد، ایران حتی یک بشکه نفت هم از سواحل خود صادر نکرده است. هیچ کشتی غیرمجازی وارد بنادر ایران نشده یا از آن‌ها خارج نشده است و ما تنها به دلایل بشردوستانه اجازه عبور داده‌ایم.
نیروهای ما با به‌کارگیری بیش از ۲۰ ناو جنگی و صدها فروند هواپیما، با موفقیت مسیر ۷۵ کشتی را که قصد دور زدن محاصره داشتند تغییر داده و سه کشتی متخلف را از کار انداخته‌اند. در جریان بازدید اخیرم از منطقه، شخصاً شاهد فداکاری، حرفه‌ای‌گری و آمادگی فوق‌العاده ملوانان، تفنگداران دریایی، سربازان و نیروهای هوایی‌مان بودم. آن‌ها همچنان با تمرکز کامل، توان رزمی بالا و عزمی راسخ به وظایف خود ادامه می‌دهند و من به موفقیت تاریخی آن‌ها بسیار افتخار می‌کنم.
@News_Hut</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/news_hut/70698" target="_blank">📅 11:47 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70697">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/c1e3e3b651.mp4?token=TQiiLRxhdFC4rbHWYIu7mRax2NPn0kJbB7J6BAl6Myo-BUUofNjlzxT4OvL77VmVESY-rT_HQhwoOOzMVJXEumY7XK3f0p3e6aBAUypagJAFgVGJWjWR1opCJn5RHlROi1k3RGAbyVU_7JSugr9qi3ye6kXNIqPo78BH3GS97vW3Cw_Mf1UFGvCwwgw6euUZFDhd2OaIz4QMgSUxLdpRD4jDUC92KyPlnc6wCOzDFhywOOO-IvvVTl_8lMkgv-Z6408qEbD7ZJClEoY4FaCT2h359fxQnVDBJdY3PZTyKL5dy06bQIa5oXuWzWANk6nODIkYogVPjYbmzgzsVZjLuw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/c1e3e3b651.mp4?token=TQiiLRxhdFC4rbHWYIu7mRax2NPn0kJbB7J6BAl6Myo-BUUofNjlzxT4OvL77VmVESY-rT_HQhwoOOzMVJXEumY7XK3f0p3e6aBAUypagJAFgVGJWjWR1opCJn5RHlROi1k3RGAbyVU_7JSugr9qi3ye6kXNIqPo78BH3GS97vW3Cw_Mf1UFGvCwwgw6euUZFDhd2OaIz4QMgSUxLdpRD4jDUC92KyPlnc6wCOzDFhywOOO-IvvVTl_8lMkgv-Z6408qEbD7ZJClEoY4FaCT2h359fxQnVDBJdY3PZTyKL5dy06bQIa5oXuWzWANk6nODIkYogVPjYbmzgzsVZjLuw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
سخنگوی دولت:
از من خواسته شد که پوششم را تغییر بدهم و چادر بپوشم، گفتم که حاضر نیستم و چادر سر نمی کنم!
از زمان دبیرستان روشنگر بودم و چادر اجباری بود و سر می‌کردم.
@News_Hut</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/news_hut/70697" target="_blank">📅 11:34 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70695">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BMetmc87nbCc5ysb58-Sh7DoPZdmMPg2Dlh2eCWVqcrfCj7dMYFYtTPQbDPVKXbt6jacFSTcdT42V0myWlTcDnaEC6oQbYmR0a0AwaPEEIIOsyRU5Z_E8ywohE1BIjZMyWzbLbzy_6NVi0qFYNmSueH3C4Z0hqQSlO18IO5elKyfHxmxrqiugJbXy5fDq8Lbiioao8zPUwc7oN1C0xmERu_dPJuJ6mBPFKCe_BFYgioGxtWSRUyD24o-XxtviL9wCxzyPyvmfPWf7C52FsZuIq5JYu04FeourKPm5hVZ3vmLvPuanrVQm97oGdW1qByNB9FwjQCgEWz4efK_BoHWOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6029290388.mp4?token=BVneXzvpbsLy0Z_eU3URf8RSPg0MevUtTRPpR_LqIjXI2XD5cEE1rH8Ub_jlCPTNGlHh7h6hoLJENghzUgEJVQ-RTzyC4wWTfXNKGnCSj2rdL9fa5QRlqLSMdQRE_E-jDLlzBAJfM7J-4WJHVbwbcK-K2P_-EaBzcaVVFYwMOOQR-J90aGoA0JFpjQE2mQXWrpzPxm9-PAmI_EdJo5OQmZ8XaASb8ydXZiVZ7YLMK2z2aw9QeDy0BR_Ng-I3fJPfe17bkoP-hEF0BFQAENBQEX1RkufZV48mBhn9d7-5aryjfhTHP1GWRTKG2uTiapiTPjzCNdU0KjPJxckbOdUQXg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6029290388.mp4?token=BVneXzvpbsLy0Z_eU3URf8RSPg0MevUtTRPpR_LqIjXI2XD5cEE1rH8Ub_jlCPTNGlHh7h6hoLJENghzUgEJVQ-RTzyC4wWTfXNKGnCSj2rdL9fa5QRlqLSMdQRE_E-jDLlzBAJfM7J-4WJHVbwbcK-K2P_-EaBzcaVVFYwMOOQR-J90aGoA0JFpjQE2mQXWrpzPxm9-PAmI_EdJo5OQmZ8XaASb8ydXZiVZ7YLMK2z2aw9QeDy0BR_Ng-I3fJPfe17bkoP-hEF0BFQAENBQEX1RkufZV48mBhn9d7-5aryjfhTHP1GWRTKG2uTiapiTPjzCNdU0KjPJxckbOdUQXg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
📚
آرش عمید دبیر هندسه و گسسته کنکور، وقتی یکی از دانش آموزان بهش گفت ما پول دادیم، اما نصف کلاس یا داری حرف بی‌ربط میزنی یا کلا صدا قطعه، به این شکل توهین آمیز جوابشو داد!
🗣️
بعد این قضیه آرش عمید اومد و از شخصی که بهش توهین کرده بود عذرخواهی کرد؛
ماه‌های گذشته با اتفاقات سختی روبرو بودم، پدرمو از دست دادم و شرایط روحی خوبی ندارم.
اما بازم این کار منو توجیه نمی کنه، بخاطر حرفام که باعث رنج اون دانش آموز شده معذرت می‌خوام.
در ادامه هم گفته که هزینه که این شخص برای شرکت در کلاس داده رو بهش برگردونن
.
@News_Hut</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/news_hut/70695" target="_blank">📅 11:04 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70694">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">💢
‼️
تریلر کاملGT6 که راکستار رسما منتشر کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/news_hut/70694" target="_blank">📅 10:32 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70693">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">🇮🇷
فیلد مارشال محسن رضایی:
ادعای ترور پسر ترامپ؟؟ توهمات نتانیاهو هستش و اگر ما چیزی بخوایم بکنیم کسی نمیتونه جلوشو بگیره
ضاحیه و بیروت خط قرمز ماست کسی نمیتونه به اونا صدمه بزنه
باز شدن تنگه هرمز منوط به اجرایی شدن شروط ایران توسط آمریکاست
محاصره ادامه پیدا بکنه بشدت اهداف اقتصادی آمریکا رو میزنیم
آتش بس در لبنان و غزه جز شروط اصلی تفاهم با آمریکا هستش
نتانیاهو رو خواهیم کشت
@News_Hut</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/news_hut/70693" target="_blank">📅 10:03 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70692">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/51590b7113.mp4?token=P1dhhLQcgSXqczMcle_1jjsjCu8Cpbf9Gk6CL6kSLSNH09JIiSK3t1JIj2tl6aybTw4Rs1tKTpE6mAwqrzCqgSwmQHUQoBQlXTxMT2MwxSnbhSoI6yH9jPHIJj7kupjznEecTTf-WiLZ3v6fVHXaGI42wSgz02pFbR83cN60wJqN--2zz-8Ixva5S3QjT4Vn-petrvXqIAi1umh0E_7Unl1FNQ9ML_Iibd9dAbxrG6tcGe0s0NVjrBnpqnPKoDpuPut0_CYq1nipvTXUUHFfEXqJ3kdiAGcrCrIql3NEo1MLlaeB6eEaqzre-iAc7Mvt3XHtl3eaXg8PLFix4lBavQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/51590b7113.mp4?token=P1dhhLQcgSXqczMcle_1jjsjCu8Cpbf9Gk6CL6kSLSNH09JIiSK3t1JIj2tl6aybTw4Rs1tKTpE6mAwqrzCqgSwmQHUQoBQlXTxMT2MwxSnbhSoI6yH9jPHIJj7kupjznEecTTf-WiLZ3v6fVHXaGI42wSgz02pFbR83cN60wJqN--2zz-8Ixva5S3QjT4Vn-petrvXqIAi1umh0E_7Unl1FNQ9ML_Iibd9dAbxrG6tcGe0s0NVjrBnpqnPKoDpuPut0_CYq1nipvTXUUHFfEXqJ3kdiAGcrCrIql3NEo1MLlaeB6eEaqzre-iAc7Mvt3XHtl3eaXg8PLFix4lBavQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
ویدیویی از وضعیت اسکله شهید رجایی بندرعباس
@News_Hut</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/news_hut/70692" target="_blank">📅 09:34 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70691">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VEnjNW1HPfQgpe68gBot9Zp9Ng7aOnbdDpRSkRicaPJ5W56ePGtMU5F0gRSMMZgOqhGv1fwoW03naez6bOMCQp5zj-W34fzkTRce4uvgGHDJ38Iw_YjZ_pqhSGUxwj3ljP3h1tnjATALHrWuCc11uZM1i0oCdHy9OH3umqHRtIitBhybdxDDsQE3IvA7xsNQEVG5OTTLmPk9dBpL6J63zvEI80dOe_-erxo5M6RdK_5YdiY5xbghIN3FJWZy7lNFOk-EwZBe4LjK7okSjPpNNAmPanlhPCGAa1OkFGHVjbbEkkdwCDeo2nG_HXDHKTyell2NozLoF1efPxeiTlj6ag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📰
🇺🇸
🇮🇷
وال استریت ژورنال:
ترامپ بازگشت به توافق اولیه ماه ژوئن میان آمریکا و ایران را رد می‌کند و در عوض بر این باور است که تشدید فشارهای اقتصادی، تهران را به دادن امتیاز واداشت خواهد کرد.
ایران تأکید دارد که هرگونه بازگشایی تنگه هرمز باید بر اساس چارچوب ماه ژوئن — شامل رفع تحریم‌ها و محدود کردن فشارهای آمریکا — صورت گیرد.
پاکستان، عمان و قطر برای میانجیگری تلاش کرده‌اند، اما این گفتگوها پیشرفت چندانی نداشته است.
@News_Hut</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/news_hut/70691" target="_blank">📅 09:01 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70690">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WBCB7mpfL1UHHxM7I0Pay1ljrGYToySooG95OfaRA3R4tjIX5fnFGMqqDRlVGZ2KHhE38A4G9aTkvXlTfbrCohAY6rpQ5UZPYiz3kSmugZJKlukCXdGciXFVKBLoKpg9wzlKHtrzZJGiYfBq--cD1X_LRfCp2i7pXL7YD7GqZIjNm_EJYfiGUWBHV00AiISFvASi8d8q4BN8kRBYtHLlD9uavmvOBo7ggi5vtGJSVSSOdIcGgJblppuIux9xXxWqF3JVI3WMG66u-KOM1JRJ0SEJCxXuCpmK9piINIhy9OUdZutEAW1NAJx5PUYaWYblHF6T71fZJj9o-xoGTnF5uQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇺🇸
پرزیدنت ترامپ:
ایران کشوری رو به فروپاشی است.
@News_Hut</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/70690" target="_blank">📅 02:15 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70689">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qydw3ZJngelftcpbPQcp7wVzWFa5hF4UIIQCxyPbut-Wki4UL6NZ-ShEnDRVuA5HWIpIfDVP4yXqLuigGmoLKC3Ohb-77VqCZSWUJhxQYsIOds6QCC70OL_LWMGWVbl8PI75-jT-KbVU4P5JECUiTOz2AcLB82WtdSZzQcKn3pD8voyV8ZXSq6B0INfBrl2rk5IRAzxm0ZwyHL1Kunm8NWjc--OZQMjuWpmrtCSbGWV7-r1ZT1kME6SxKICVhin0I1ve25Ss_kxCvoFw-hxrT--po5VoGd1fU8d5HHFIjO8fkwomhD0LcwSsBw2wGUWDnV876-ufhXBzLWege5a6cQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
محسن نامجو بعد از ۲۰ سال به ایران بازگشت! می‌خواهم در این مقطع از زندگی، در وطن، در کنار خانواده و دوستانم باشم و این موضوع برایم از فعالیت موسیقی مهم‌تر است.  @News_Hut</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/70689" target="_blank">📅 02:01 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70688">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XSAhbVOpAdOXeE8db6mNv4rAJjRcWFKg9yJj-aFByQfx698WcSMfmYkpucVmpFYmG9aU2VHk0f-5p107dYhSebKynqmVXxucJU_mLyqTWXYLGbolYf0KuzkX1ahBhO2e08M9o_ksTjADARF_CmD-VbWrmDaTBhODphb_MZOE1xAm9JecYxtiaUD85jUXfEcKeMnQWSnsOOMKD3PwEpy1CLhULzagAfATusL98Ms9RBP4rQKKiJ0V5cOQdR1n6f5NpdwGqrDO0j98dKz-wQFHwOse0cgkMD05NX2OaLFr-QS4QG76MJg_dgf9_PhguwlbUHFNswcjVhvxP2BX_euyKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇺🇸
ترامپ رده‌بندی رؤسای جمهور رو منتشر کرد و خودش رو به‌تنهایی در رده «بزرگ‌ترین» قرار داد.
🗣️
جیمی کارتر و اوباما و بایدن در پایین‌ترین ردیف«بازنده‌ها»قرار گرفتند.
@News_Hut</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/70688" target="_blank">📅 01:13 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70687">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">⭕️
تریلری که راکستار به صورت رسمی از GTA 6 منتشر کرد
💢
@News_Hut</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/70687" target="_blank">📅 00:46 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70686">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H_7tcpWYPFSDKpUciX_lvhd0T8vArIa85RutaNNhvWK-Ja6c1ToW0xkmv9fPT5iV-ygQFnJ06jMZolfPn58lvdd6TGoW7YZrMmn7y5X5pw0AX47bfU3lCQHrCQbNVp5z0QvcmFhv4VCOd8pTJvnwnrplYuSUZ__6JrsUzDBJsSSP_EjuAc6eJ6rX_0OgyA7Bja9K7QIjcX3_L-2Ec5mTfrgzxVqIpv_PYsY0Eiup3ZTXRNvDWkkkhqog9xbVsjQxXiI5CVfpyE-re3WpWzLcrzU0Zds9tMfKxISlBFqbNBGsGoFcOex0GujiEdl3GAoQz2wGzASuyXYnwemQZyMUgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇮🇷
🇮🇷
درحالی که دلار به تازگی از مرز 200 هزار تومن هم عبور کرده؛
دیروز پزشکیان به مناسبت گرامیداشت روز کارمند، از تیم اقتصادیِ خودش به خاطر عملکردشون تقدیر کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/70686" target="_blank">📅 00:34 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70685">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f13108aa49.mp4?token=MSgwZaw-U279Rz2XYAgj8gDFwTtTyuNaNgDmEQ8kHijJguLPY6e1HN_8pFY_ePFXseHR1sqWxHF-dTag8FX4zBHCCkycfsEDjjMu9Zc33R4wbyz4HRzq9AFrbiiy3c860nPMO_e_i8NTNuQJtmYY0T6wQjtFGhoPX6PLZx7EIn8DrELFZzND18Fnyr4t34rJBv3pSGPyvZRzsk-n6YUqVr-FN-SAstCUqwptz3L31EmKiSSs8oGIIVCEA_W7JUeSQXyOvlBsXozFD_nCDYrgjfBtPAI2W2m90nLjDtkgb-9fPqj-4_kAxCBmF6LZvHwflMT2f1zU8tDNVp4nr3FdDA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f13108aa49.mp4?token=MSgwZaw-U279Rz2XYAgj8gDFwTtTyuNaNgDmEQ8kHijJguLPY6e1HN_8pFY_ePFXseHR1sqWxHF-dTag8FX4zBHCCkycfsEDjjMu9Zc33R4wbyz4HRzq9AFrbiiy3c860nPMO_e_i8NTNuQJtmYY0T6wQjtFGhoPX6PLZx7EIn8DrELFZzND18Fnyr4t34rJBv3pSGPyvZRzsk-n6YUqVr-FN-SAstCUqwptz3L31EmKiSSs8oGIIVCEA_W7JUeSQXyOvlBsXozFD_nCDYrgjfBtPAI2W2m90nLjDtkgb-9fPqj-4_kAxCBmF6LZvHwflMT2f1zU8tDNVp4nr3FdDA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
بخشی از یک موشک ضدکشتی جمهوری اسلامی در نزدیکی سواحل ایران
@News_Hut</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/70685" target="_blank">📅 23:51 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70684">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fc3febd1d3.mp4?token=F3n_j2TFon7sXFSTBn3H7EjPc_UTNoCrFPlZor4UI-76IVv2LD3O41HJNtP2_RtjklhLcQXuseVBw4CAZdFtqmFCb-HcAtv5QIVss21_QlH-6Uqs_thbty8nHOMdkvSW49sXzDTB1Sl8bKSfNOKlcnRVIuLBpCjd7Z8lGTJ62qS7XIqpbZAp7yf1Pci2fdhQn54CxO-rJ2D30fZ8ov7WQnkV9InVKeDKqDtzSXO1hi4vsbTlUcW1Z2PxMMQ0GJTfXK4EUqtck5zQZpPkFbyHJJFFQaleFZL8tgWA-vDMjShtfN1BFh05nszjTvqRRuWKriijcfjq-EIjv8RhJh3y7g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fc3febd1d3.mp4?token=F3n_j2TFon7sXFSTBn3H7EjPc_UTNoCrFPlZor4UI-76IVv2LD3O41HJNtP2_RtjklhLcQXuseVBw4CAZdFtqmFCb-HcAtv5QIVss21_QlH-6Uqs_thbty8nHOMdkvSW49sXzDTB1Sl8bKSfNOKlcnRVIuLBpCjd7Z8lGTJ62qS7XIqpbZAp7yf1Pci2fdhQn54CxO-rJ2D30fZ8ov7WQnkV9InVKeDKqDtzSXO1hi4vsbTlUcW1Z2PxMMQ0GJTfXK4EUqtck5zQZpPkFbyHJJFFQaleFZL8tgWA-vDMjShtfN1BFh05nszjTvqRRuWKriijcfjq-EIjv8RhJh3y7g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
کارولین لیویت در آستانه آخرین روز کاری‌اش به عنوان سخنگوی مطبوعاتی کاخ سفید، سخن می‌گوید؛
«احساسی آمیخته از تلخی و شیرینی دارم. تلخ است چون شغلی را ترک می‌کنم که بسیار دوستش دارم؛ کار کردن برای این رئیس‌جمهور، یعنی رئیس‌جمهور ترامپ، افتخار و موهبتی بزرگ در زندگی‌ام بوده است. هرگز کسی مانند او نخواهد آمد.»
لیویت پس از ۲۰ ماه فعالیت در این سمت، کناره‌گیری می‌کند. دلیل این تصمیم، تمایل او به گذراندن وقت بیشتر با خانواده و دختر نوزادش است، هرچند او همچنان به عنوان مشاور ارشدِ خارج از دولت به همکاری با این مجموعه ادامه خواهد داد.
«آن‌ها در مقطع حساسی از زندگی‌شان هستند و بیش از پیش به حضور مادرشان در خانه نیاز دارند؛ بنابراین مشتاقم که وقت بیشتری را با آن‌ها بگذرانم و در عین حال، همچنان به عنوان مشاور ارشدِ خارج از دولت در خدمت رئیس‌جمهور باشم.»
@News_Hut</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/70684" target="_blank">📅 23:15 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70683">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c174815597.mp4?token=MhlPtFn3m1pQu2FUeglLIZTZe8QUbc7-zH6woa39NTzsB5MDLvBwFaV2t9s8tVisSlfDr61owyaV8pNex2IlT5sTFAeFj0VhLOjjt54ZzhbD1DSPr6mwbHLBQDIcYfr-x0pIrERQaAUyp7ueqO8c0HNiMOGHYJaYmbN6a1NuTn3XQUK8Q46D3cxtxauvYmQPZwcudFyfiPdtT26UT1n89DEbjgNUvSLpUIunouj6HPZArsl3ShJP7ueoUfsJ7ObAlE8CTZR-oCYKD6sqbU2C4fHPNbemWtK7eqcTvD-CH2FJyhSsO1rTkCW6UI5g86OZyxBOMLJlwNG5qYMqU08vPA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c174815597.mp4?token=MhlPtFn3m1pQu2FUeglLIZTZe8QUbc7-zH6woa39NTzsB5MDLvBwFaV2t9s8tVisSlfDr61owyaV8pNex2IlT5sTFAeFj0VhLOjjt54ZzhbD1DSPr6mwbHLBQDIcYfr-x0pIrERQaAUyp7ueqO8c0HNiMOGHYJaYmbN6a1NuTn3XQUK8Q46D3cxtxauvYmQPZwcudFyfiPdtT26UT1n89DEbjgNUvSLpUIunouj6HPZArsl3ShJP7ueoUfsJ7ObAlE8CTZR-oCYKD6sqbU2C4fHPNbemWtK7eqcTvD-CH2FJyhSsO1rTkCW6UI5g86OZyxBOMLJlwNG5qYMqU08vPA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
صحبتای این فرد که در حال وایرال شدنه:
الان که رهبر رو زدن، مسئولیت این کار زدن رو گردن نمی‌گیریم، جرأت نداریم رهبر بعدی‌مون رو نشون بدیم. به هزار تا داستان دیگه داریم. ته جنگ‌مون معلوم نیست. نمیدونیم خونه هامون میمونه، خانواده هامون میمونه، ناموس هامون در خطر هست یا نیست.
بعد بگیم که آقا ما دست‌مون رو تنگه و هرمز گذاشتیم. خب حرکت بعدیت چیه؟ بعدش میخوای چی کار بکنی؟ خب من... شما پنجاه سال این کشور دست‌تون بوده، نمی‌تونید یه تورم ساده رو کنترل کنید. ادعای حکومت امام زمان رو دارید که میخواید دنیا رو برای ما بسازید. خب خیلی خب.
بحث ساده فرهنگی‌تون، آمار طلاق‌تون، آمار احتکار‌تون، آمار دزدی‌هاتون. یکی یکی آمار، یکی یکی دارم میگم. میدونم تمام کل و هزینه سرمایه این کشور رو برداشتید. همین آقایان استفاده کردند به هر قیمتی هم باشه.
من یه حرف رو میزنم. همین آقایان سپاه رفتن میلیاردها دلار هزینه کردند، عجیب و غریب و زندگی من و شما و بچه هامون و نسل های آینده رو به فنا دادن.
@News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/70683" target="_blank">📅 22:32 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70682">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c8a6f01648.mp4?token=nOQPi7yFJ1rAayaTXeDo3hAVMDyDpJaNJoRWtYhg_aP9841TSwcSMpIyrJZpWHG8YPVpb2Nd57sKRIUoJNkDKFU8Pw540TusLeYuVQWOwZMdkh4PnrUqPWlP4ZxBxdWy12CoIfyMa_Bjolp8BqcRJ5VL9B9De9UiEegCyQ08B2HkhUv-eFGweJKCkK6P-jTTu044xf1y5dwXnLW1Jb_EF5pDPcyMnLz6IGA-xgLCJRLX1B43oasEF0lS2lxCh3_UhU3uj5sPz3k3jjaz9M7AfamgPbAC9LXULdJdo9r6Mp3g8Jp10ux1GSzqeHIWTxejGcK8kzfChtCh3AG4Nj0Z9A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c8a6f01648.mp4?token=nOQPi7yFJ1rAayaTXeDo3hAVMDyDpJaNJoRWtYhg_aP9841TSwcSMpIyrJZpWHG8YPVpb2Nd57sKRIUoJNkDKFU8Pw540TusLeYuVQWOwZMdkh4PnrUqPWlP4ZxBxdWy12CoIfyMa_Bjolp8BqcRJ5VL9B9De9UiEegCyQ08B2HkhUv-eFGweJKCkK6P-jTTu044xf1y5dwXnLW1Jb_EF5pDPcyMnLz6IGA-xgLCJRLX1B43oasEF0lS2lxCh3_UhU3uj5sPz3k3jjaz9M7AfamgPbAC9LXULdJdo9r6Mp3g8Jp10ux1GSzqeHIWTxejGcK8kzfChtCh3AG4Nj0Z9A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇷
سر دادن شعار «مرگ بر آمریکا و مرگ بر اسرائیل» در نشست علنی مجلس
@News_Hut</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/70682" target="_blank">📅 21:53 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70681">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6cc74b5c0f.mp4?token=hyLQ3HVYQbwIbDwcZY6h-Uu7Tj4TktsYETv5DmhGnkqxW_IyXGWtot8KM9800JJCj998qEzt3Wo2fUb_O497aoxaudh2mZ4KrlCzqCWBkfk2XgxOVBJ8ntea-p0J2pP2sjh5gacePPHAoAnhg5zspr2baoBiVV72v2AymPXbgToHNZHFBayu7hjBLtcMSV1FTDsFiUb_ZQsRz6pkJpKGKb90TJ6BJtGV1J3a07Pwu62EwRrc78zagAXzza5JlNWrFTouHy1OEg346Cwgmb3A5pD3sKm4d_di_lkNQfBmp-S7_Sw6yms7HsgBfQaItAto35iPa5B3rncYQ_fPfjXiRA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6cc74b5c0f.mp4?token=hyLQ3HVYQbwIbDwcZY6h-Uu7Tj4TktsYETv5DmhGnkqxW_IyXGWtot8KM9800JJCj998qEzt3Wo2fUb_O497aoxaudh2mZ4KrlCzqCWBkfk2XgxOVBJ8ntea-p0J2pP2sjh5gacePPHAoAnhg5zspr2baoBiVV72v2AymPXbgToHNZHFBayu7hjBLtcMSV1FTDsFiUb_ZQsRz6pkJpKGKb90TJ6BJtGV1J3a07Pwu62EwRrc78zagAXzza5JlNWrFTouHy1OEg346Cwgmb3A5pD3sKm4d_di_lkNQfBmp-S7_Sw6yms7HsgBfQaItAto35iPa5B3rncYQ_fPfjXiRA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
ترامپ:
ما یک خلیج داریم. یک دریاچه هم داریم. حالا چیزی که نیاز داریم، یک اقیانوس است.
بنابراین شاید مجبور شویم نام اقیانوس اطلس یا آرام را تغییر دهیم
😠
@News_Hut</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/70681" target="_blank">📅 21:25 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70680">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/70d624c250.mp4?token=XHenOO5bI3ZHcaE12tzGdMGTGoutgua5U378TGVly2Jh4l6u0Rd5tGgmkVuBaS8-p1OjikHrEua8m8udvw3YoF-UPOpMDnbnYj7SfZ7tSi4l_Cgt2RdEGsGJCI02J4GvjQFvsaBbqtc8Zb50aj6kxmG1dcz922f3igeCTwEoyX8sPdvHsNDidydic7GNoysI60uWiZehpUSAiLZ6n6Q9eC-pJ0YOEeAeF6_cadm1CFIKgq2JiadSpPJqM8OTtJpJb0i-ZOy0WurZxLfG71B4UmH_MyllTSrXkfwRTUZHU-_v0bfixzy9LbyHj4xecNKWGTNnVbIK6_Dv4U2u4-bPToLuwCHrrWCgwxd_zjQ7xoWWk0MrjnRSZBy1CytLrK0dtM6d3gqqOKl1c9hLVbrNPDauRehOy5-yKtu32UbeKJ6UM2oLaC7SD68GIa8Xa6YmiX9w8-fI8stnaEsXvTzFr3gf6umayG747vY8u7eqh4t55bDSa__gU3JIr5ziyDU4e0oHx8dKFpTFYDenv1S5gicwYaWHhvg1Qp1nfM0wqG3KwQDC4vqpU-ssTieZujbklEbKdI0XlTcZ8JNCWZWabQQHpgfhMGc6D8vT-LadSGIcdm1g9soi3UMOFK0Uex-A5iBBIUXmzCGH_m7fUCwywUxRrEfItwsyFUtHZ7Xv538" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/70d624c250.mp4?token=XHenOO5bI3ZHcaE12tzGdMGTGoutgua5U378TGVly2Jh4l6u0Rd5tGgmkVuBaS8-p1OjikHrEua8m8udvw3YoF-UPOpMDnbnYj7SfZ7tSi4l_Cgt2RdEGsGJCI02J4GvjQFvsaBbqtc8Zb50aj6kxmG1dcz922f3igeCTwEoyX8sPdvHsNDidydic7GNoysI60uWiZehpUSAiLZ6n6Q9eC-pJ0YOEeAeF6_cadm1CFIKgq2JiadSpPJqM8OTtJpJb0i-ZOy0WurZxLfG71B4UmH_MyllTSrXkfwRTUZHU-_v0bfixzy9LbyHj4xecNKWGTNnVbIK6_Dv4U2u4-bPToLuwCHrrWCgwxd_zjQ7xoWWk0MrjnRSZBy1CytLrK0dtM6d3gqqOKl1c9hLVbrNPDauRehOy5-yKtu32UbeKJ6UM2oLaC7SD68GIa8Xa6YmiX9w8-fI8stnaEsXvTzFr3gf6umayG747vY8u7eqh4t55bDSa__gU3JIr5ziyDU4e0oHx8dKFpTFYDenv1S5gicwYaWHhvg1Qp1nfM0wqG3KwQDC4vqpU-ssTieZujbklEbKdI0XlTcZ8JNCWZWabQQHpgfhMGc6D8vT-LadSGIcdm1g9soi3UMOFK0Uex-A5iBBIUXmzCGH_m7fUCwywUxRrEfItwsyFUtHZ7Xv538" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
🇺🇸
🇨🇦
ترامپ فرمان اجرایی «تغییر» نام دریاچه انتاریو به دریاچه آمریکا را امضا می‌کند.
🎙
خبرنگار:
با تغییر نام دریاچه انتاریو، چه پیامی برای کانادا می‌فرستید؟
🇺🇸
ترامپ:
هیچ پیامی.
@News_Hut</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/news_hut/70680" target="_blank">📅 21:23 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70679">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/609cc5c89b.mp4?token=l8NFuYDIPFzoxfkb08Ijpd5_yjItRcLu_noX1V3dkNViVFbiuqNRBbuyUjXaQz1s69dVX_q8poIgx4xdp0OJMSPYJzNwVVCCztNZl_pr39l-qpOI1myEWit69dZPHhdaUWPH0xXn61eQNpLhWviGiVrs1mN2fBsS2Bg5ArIiESfKub_YWV9bUFFgoPomLnZgmUzEomFg-knlkp-v3zg-5oGODwC_S_sgALmLVYFwpiU8e1Vi7z3bEOZN0aPY-iHqRXw_qRDkXPHrnhi0S91d_rLG3FPrDNpN2VDAGKle6IrY1pZiGQDHP0RWAzhzXh4LKyK8Cmfw9zBlacSma3Bxmw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/609cc5c89b.mp4?token=l8NFuYDIPFzoxfkb08Ijpd5_yjItRcLu_noX1V3dkNViVFbiuqNRBbuyUjXaQz1s69dVX_q8poIgx4xdp0OJMSPYJzNwVVCCztNZl_pr39l-qpOI1myEWit69dZPHhdaUWPH0xXn61eQNpLhWviGiVrs1mN2fBsS2Bg5ArIiESfKub_YWV9bUFFgoPomLnZgmUzEomFg-knlkp-v3zg-5oGODwC_S_sgALmLVYFwpiU8e1Vi7z3bEOZN0aPY-iHqRXw_qRDkXPHrnhi0S91d_rLG3FPrDNpN2VDAGKle6IrY1pZiGQDHP0RWAzhzXh4LKyK8Cmfw9zBlacSma3Bxmw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
خبرنگار:
چرا بانک‌های چینی را که با ایران مراوده دارند، تحریم نمی‌کنید؟
🇺🇸
ترامپ:
چه کسی گفته که این کار را نمی‌کنم؟ شما نمی‌دانید که آیا مشغول انجام آن هستم یا نه. لازم نیست همه چیز را اعلام کنم.
🎙
خبرنگار:
با کدام‌یک از رهبران درباره قطع روابط با ایران صحبت کرده‌اید؟
🇺🇸
ترامپ:
صحبت خاصی در کار نیست. ما نمی‌خواهیم با آن‌ها صحبت کنیم. تنگه باز است.
اقداماتی که در قبال ایران انجام میدهیم به معنای منتفی شدن گزینه نظامی نیست.
گزینه نظامی همچنان روی میز است.
@News_Hut</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/news_hut/70679" target="_blank">📅 21:19 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70678">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rzaDIoXrFgZSREjcj43eoDMKD0o1WDfu7AmIO5cXIpmjubmnZHNNeSf6bG76XNcN7JUYKGwR2mPnmZMusoHMvfjZpJ2eJ0S_iGw3ln_0I8gvywAYBnKXz81-B3Ot_W6GX4wHYkPtBokHqLrqQkp9ihLy4EjXYORu6iTHEqrHLdJmNqADYCr4Ulaazf3JRwXyaaKz_h7jC04py3zmn34D4ePTV2XITIoMBBCIacK7udYX6zfFC3xhCtMTRYrt14XkR-Om3-unSJVgxLI-lyOubvVLATlrWphAW3RddV5yaVVe9n9wQgBUlVPugh5j6o3fsfQJsuYlDEMXK8_DmZWj9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇰🇼
🇵🇰
کویت و پاکستان یک توافقنامه مشترک دفاعی و همکاری نظامی را در اسلام‌آباد امضا کردند.
@News_Hut</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/news_hut/70678" target="_blank">📅 20:45 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70677">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bb0fgZ_ytxLNjEPnGrFeSz5FYcr2E7RJ-FH8byZtssB-uZ-ujZd1id6KEpD3fWfHxNFdG6YwJS_J_UNyQkomcL5RW98cA0-EwaE4yawVIKIFXSCBalRF2pBvtVFd6lvSIiYxDt_KPANoQex40iSbL6VM-J6z8vTVRSkgwy7VsiJXAta9AljoEB7EgawJJIcoK47G40VH7SBofOmayR8lgU5zdTI88sBG3xtYcO3VXWbsMrUIso140VZCx4g9LDWblv3PqV6kGAA9Sb_TsnCQqkxTDwkmlc1KS1Kq4zRkACnrq2jC0xzC6pg5xrHo-wk0Wl4xCvN4cQuFvEGBDgWvWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
🇮🇷
قالیبافِ در جواب بسنت:
این امپراتوریِ رو به زوال، به‌جای سرازیر کردن میلیاردها دلار به سوی اسرائیل — آن عامل نیابتیِ تروریستش — و صرفِ هزینه برای ۷۵۰ پایگاه نظامی، می‌توانست آن پول را خرجِ مردمِ خودش کند؛ اما نه، چنین کاری برای این رژیم بیش از حد منطقی به نظر می‌رسد.
اسکاتی، رفیق، اعتبار تو در خطر است. کاری بکن.
@News_Hut</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/news_hut/70677" target="_blank">📅 20:31 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70676">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/df6a4150d1.mp4?token=eoXhLNmQ00Exb6uMddhbGfdrgI2oSQQgrByLDfFuNjuuWpuPTj7c4PjHf9rcl3f3KqB4WRk_v-qbNMHSCJ6SKEoGV1z_jVBvvkEdLAHbLeuIwjhg6HsLj9B0cOfgewn2RO4zg7xFlhjYB_VYX_e1NWDTuNlETafKr90e7OoshXASbWB4q9cgEPjuoIYLgzW81bDy2bUejrk55EGToByKckG_G9r2VPOmX1wTR7rkDAEAdq5Wi0NTlN757ncx5EoaWRbt4S6EqJXpr_2kY8ItbAWbJ8ue81w92KMHeuQ9Tteo7nrw7YefKxTMfUD1DCDGnnQx31WqvE6GERjimLjD_Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/df6a4150d1.mp4?token=eoXhLNmQ00Exb6uMddhbGfdrgI2oSQQgrByLDfFuNjuuWpuPTj7c4PjHf9rcl3f3KqB4WRk_v-qbNMHSCJ6SKEoGV1z_jVBvvkEdLAHbLeuIwjhg6HsLj9B0cOfgewn2RO4zg7xFlhjYB_VYX_e1NWDTuNlETafKr90e7OoshXASbWB4q9cgEPjuoIYLgzW81bDy2bUejrk55EGToByKckG_G9r2VPOmX1wTR7rkDAEAdq5Wi0NTlN757ncx5EoaWRbt4S6EqJXpr_2kY8ItbAWbJ8ue81w92KMHeuQ9Tteo7nrw7YefKxTMfUD1DCDGnnQx31WqvE6GERjimLjD_Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
صف عجیب پمپ بنزین در کرج دیشب
.
@News_Hut</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/news_hut/70676" target="_blank">📅 20:15 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70675">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BFTYbxFumfbMPG4IWsyBf669rdKHdvW7wpXMLiH4wxtLYF_3yY78hxmUHZg7mpM4uIJIIljf1-AKyOsEfGpZkhxvjH1OpBowONVI7VLdpat_mYwVY7BHQaQukTW8IcZY4Wk_Exag5TKbfQwVo0R2TQ1HIMJjXemCYRbZFCH-MWf43i3C0RdMSihbdHOBd078CF83ZKq-jFxjDCxPqh8DBWgPBJBMqlMVXIkyt2ess5c04_nAgSFMK9N_8X4qmFRH52TpE8hwETXGbRgKq3Wh5zwxpx4u6WLiNJmkuoofzvu_JD3ytVDod80MMWQvFDvvVTSOeGcnJc9WmE6Tc-_i1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">〰️
سنتکام:
هم‌زمان با تداوم اجرای محاصره علیه ایران توسط ایالات متحده، هواپیماهای جنگ الکترونیک E/A-18G نیروی دریایی آمریکا بر فراز آسمان خاورمیانه گشت‌زنی می‌کنند.
تا تاریخ ۲۷ اوت، نیروهای «سنتکام» (فرماندهی مرکزی ایالات متحده) برای اطمینان از رعایت مقررات، مسیر ۷۵ کشتی تجاری را تغییر داده، ۳ کشتی را از کار انداخته و برای بازرسی وارد ۲ کشتی شده‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/news_hut/70675" target="_blank">📅 19:29 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70674">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0833865a38.mp4?token=fNvFvvzGYUraCWHZWAGsB5cT0tACmym-2jFYxZ-8uERIt8ZHeaw5HgAX5Qw9jR9SWnthOR01GfZTvLMMVZ_XoFwJS7pggIaZXQDfCKr_B1V7TPLdIAjtiZ-VoBK8938MFYSD54JGqeiSstG_QzoQSvVOHU-0mAgYOyf02-s7G-GtG-_UaxsdKWF5y51n9xwLqjJ4trTVi0oNxk972E-LSLlfqoXMh6uBwGzu8HlGDbO-GowWbK_uL0qTg1cv1uz0oY8-zVNMk7BRcjO5lZflRVCWowfRMiwMZlg_-x4gE5218lQuuboARxOgpC54x0mej4EFMw1-bWcqQ7KbFH4anQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0833865a38.mp4?token=fNvFvvzGYUraCWHZWAGsB5cT0tACmym-2jFYxZ-8uERIt8ZHeaw5HgAX5Qw9jR9SWnthOR01GfZTvLMMVZ_XoFwJS7pggIaZXQDfCKr_B1V7TPLdIAjtiZ-VoBK8938MFYSD54JGqeiSstG_QzoQSvVOHU-0mAgYOyf02-s7G-GtG-_UaxsdKWF5y51n9xwLqjJ4trTVi0oNxk972E-LSLlfqoXMh6uBwGzu8HlGDbO-GowWbK_uL0qTg1cv1uz0oY8-zVNMk7BRcjO5lZflRVCWowfRMiwMZlg_-x4gE5218lQuuboARxOgpC54x0mej4EFMw1-bWcqQ7KbFH4anQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🟥
فاکس نیوز:
🇶🇦
نخست‌وزیر قطر در حالی وارد تهران می‌شود که تلاش‌ها برای کاهش تنش‌ها در این مناقشه، با هشداری صریح از سوی رئیس‌جمهور ترامپ روبرو شده است:
ایالات متحده تا هر زمان که لازم باشد، به مبارزه ادامه خواهد داد.
تنش‌ها در تنگه هرمز همچنان بالاست؛ جایی که ایران اعلام کرده این آبراه حیاتی تا زمانی که واشنگتن خواسته‌هایش را نپذیرد، بسته خواهد ماند.
در همین حال، ایالات متحده با اعمال تحریم‌های بیشتر، فشار اقتصادی را تشدید می‌کند.
در داخل ایران، فشارها رو به افزایش است. صف‌های طولانی بنزین، تورم فزاینده و تضعیف ارزش پول ملی، مشکلات اقتصادی را تشدید کرده و نگرانی‌هایی را درباره احتمال شعله‌ور شدن دوباره اعتراضات برانگیخته است.
@News_Hut</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/news_hut/70674" target="_blank">📅 19:16 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70673">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/50aa1684a3.mp4?token=St7R1k-D81x1Itd67deOM0f0iSJWzxv8anS98TVvma9s2rCiVNgfT1n5trMAprrIfEIWWpPHWKRA5h5f9Mfwyli3L_alpTWymI4p9WPTqXgtrUH_y_npKuQrN9vY1CV_ySx94sEkP3Jh0-wMCJxOfAetEMTL0QfCT3z5CPhYC3-yFKY2GO30pYkCDLpkRgTnvcGLe9dAMWHBPM5PEG9VHVP-TrX4KRI7GjWCKcr-kuurRfzJ7d56ZiM4aGWOkpvrd8NcVDX7AojlXPwGaKiUUO_OugljCaClXO_h_ydtLYW2f65zsnHhmIRomyo6AJ0ykJfWW-8uJP5CL2vGfjU-YA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/50aa1684a3.mp4?token=St7R1k-D81x1Itd67deOM0f0iSJWzxv8anS98TVvma9s2rCiVNgfT1n5trMAprrIfEIWWpPHWKRA5h5f9Mfwyli3L_alpTWymI4p9WPTqXgtrUH_y_npKuQrN9vY1CV_ySx94sEkP3Jh0-wMCJxOfAetEMTL0QfCT3z5CPhYC3-yFKY2GO30pYkCDLpkRgTnvcGLe9dAMWHBPM5PEG9VHVP-TrX4KRI7GjWCKcr-kuurRfzJ7d56ZiM4aGWOkpvrd8NcVDX7AojlXPwGaKiUUO_OugljCaClXO_h_ydtLYW2f65zsnHhmIRomyo6AJ0ykJfWW-8uJP5CL2vGfjU-YA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
🇮🇱
فیلم از منطقه صنعتی بین کفر رمان و نبطیه الفوقا در جنوب لبنان پس از یک بمباران هوایی اسرائیلی.
@News_Hut</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/news_hut/70673" target="_blank">📅 19:02 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70672">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/shYJCBrNPNWnkhEeM4LqNmglaDScxM8vSB2xPC-q_Dc5YAiPOIhHRooIY0ftX-82nIuW7vIds56WPwp8EK8kesuuMqUdfI6vmZgTCQFrUcTVi4I-03EV9jCEU9-7dovyG1tqVDnpZoQPW_u8ocNmQshZ4M5HE9HmHd0SqjSE5idAxNoqm8zixZ6oQvIv6gG1l3UBr187JOD4nKSf93RXVDNpjVpPqRYQeDYjq_XriMYHZUs8v021-Ct9c8jkltya8xMu-Gjf1uKUrpWld5EUSyT02tq0cepaT1_TZVQM096WJVDPtZo3Doef4mw1tojcoI4b2sFinSNzfhKO8JTvxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
〰️
بِسِنت وزیر خزانه‌داری آمریکا:
در حالی که مردم ایران برای تأمین نیازهای اولیه خود با دشواری دست‌به‌گریبان‌اند، رژیم فاسد همچنان مبالغ هنگفتی را در خارج از کشور هدر می‌دهد.
این رژیم باید به‌جای سرازیر کردن میلیاردها دلار به سوی نیروهای نیابتی تروریست خود، آن پول را صرف مردم خویش کند.
@News_Hut</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/news_hut/70672" target="_blank">📅 18:14 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70671">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f2ea391dbe.mp4?token=CD18_4sJxxeFka4jXQGNffGoxYGwhKzVX95HAOym5Gs3-jqst6h8qZUfucO3Wzz1DMJ2M_8oy3xOmxHzn7ljcGaoWA-LT2gjinmF3bSF4Zc9nSNE843_oEipbJ6tls103rdRKX9ti0UHVqRiV86rXgB-bvh8zs-3lw1zh7g97hXx0h-6Thsu7QrdUV06AEw8M2XwTySjJNQ7kUitnH919O8mVb93ZtrOdgzdAhcKImJVRPvDvmEUV3Gw4k2tD3dpjzaBVeF3FH7OJ1Mteei1eIf6_sjHiJyWN9JV2hhx1wrST_Y_0pMQGphpfTYozmTJnp_CkfTKaZvPlerDFTMjhw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f2ea391dbe.mp4?token=CD18_4sJxxeFka4jXQGNffGoxYGwhKzVX95HAOym5Gs3-jqst6h8qZUfucO3Wzz1DMJ2M_8oy3xOmxHzn7ljcGaoWA-LT2gjinmF3bSF4Zc9nSNE843_oEipbJ6tls103rdRKX9ti0UHVqRiV86rXgB-bvh8zs-3lw1zh7g97hXx0h-6Thsu7QrdUV06AEw8M2XwTySjJNQ7kUitnH919O8mVb93ZtrOdgzdAhcKImJVRPvDvmEUV3Gw4k2tD3dpjzaBVeF3FH7OJ1Mteei1eIf6_sjHiJyWN9JV2hhx1wrST_Y_0pMQGphpfTYozmTJnp_CkfTKaZvPlerDFTMjhw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
🇺🇸
کارولین لیویت سخنگوی کاخ سفید:
در حال حاضر هیچ‌گونه مذاکره‌ای با ایران در جریان نیست.
این وضعیت تا زمانی ادامه خواهد یافت که ترامپ احساس کند آن‌ها ممکن است به شیوه‌ای معنادار پای میز مذاکره بیایند.
ما هنوز چنین چیزی را مشاهده نکرده‌ایم.
@News_Hut</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/news_hut/70671" target="_blank">📅 17:30 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70670">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/14b224b2a9.mp4?token=VrU4FHJdlsIWRgbhrmR0aNYErbl-FQjy4VoNP--YaRAWWd6Cf3hEppsJSkA0EefT5BRUNQDR1CBZWl4-Iz6gsAwdSP2shr5wJSxPWP2FPzHUKY7DaCegHNL0nxXMDTRoY1UDcjeZsp5eAs39mn2SnHm4IKccAe7Xbk5UMNMeoYSiHnu3HZcuQn4yq7My1SCRdfJIsb7Yg8oEDan49CuzmPLVx5FUUn08QTl4RNm8e0YHySUcAta9VHC7dVGKXjuTf3enXNWvGfbqRHkSW-PrZKeVsSxV4MjBwZR99PZPK90FLjGAOtYKvdmoYsqB6UCizQzB_JmZQwWwTOsv-s2arQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/14b224b2a9.mp4?token=VrU4FHJdlsIWRgbhrmR0aNYErbl-FQjy4VoNP--YaRAWWd6Cf3hEppsJSkA0EefT5BRUNQDR1CBZWl4-Iz6gsAwdSP2shr5wJSxPWP2FPzHUKY7DaCegHNL0nxXMDTRoY1UDcjeZsp5eAs39mn2SnHm4IKccAe7Xbk5UMNMeoYSiHnu3HZcuQn4yq7My1SCRdfJIsb7Yg8oEDan49CuzmPLVx5FUUn08QTl4RNm8e0YHySUcAta9VHC7dVGKXjuTf3enXNWvGfbqRHkSW-PrZKeVsSxV4MjBwZR99PZPK90FLjGAOtYKvdmoYsqB6UCizQzB_JmZQwWwTOsv-s2arQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
محسن نامجو بعد از ۲۰ سال به ایران بازگشت!
می‌خواهم در این مقطع از زندگی، در وطن، در کنار خانواده و دوستانم باشم و این موضوع برایم از فعالیت موسیقی مهم‌تر است.
@News_Hut</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/news_hut/70670" target="_blank">📅 17:29 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70669">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded frommydiplom.ir</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o_5CjUyPBCrs97zmZ6H2cKHZbJOOoaZVAoHVwjr6Ajlk6oX1FgjWZwCCpyqz-nKiaqkSXNlt_fdV_sjXE96QyrZ4pisVi2C9LiGE8KPhs7u3U8zA8wuFQuh97oAOUeh1eQtDlBULVZ-pBpYTaGsvR1sWp6EQiD1wx52s_RvQZdKXVv31F3pi-1iiesk1maXJ2bVMmCJ9MkOR4l8F-DE0Wee0J0Wz3_CyFm6ACnND_8N7KV7Xwfw3l0Gt0kO90my-QEGl-pcQvPt2jlUROcCYrkCzl0-5HFXoAoKVL13Hz_8UfHLWPxB4N1qACD37PJUn8djG8tG3j54y72Ds3j9CaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👮‍♂️
مد
ا
رک رسمی تحصیلی «مقاطع متوسطه و عالی»!
✔️
از دیپلم تا دکتری | کاملاً غیرحضوری
✔️
قابل استعلام قانونی
+
قابل ترجمه رسمی
✔️
مناسب برای
:
مهاجرت
|
استخدام
|
ادامه‌ی تحصیل
ارتباط با مشاور
:
https://t.me/mydiplom_support
ورود به کانال :
https://t.me/+lHweVa-y92IyZDA0</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/news_hut/70669" target="_blank">📅 17:29 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70668">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8bacd124f0.mp4?token=iXjLt6QqB6L1-U7HFSaJX85isbvkGDpP29I7obieTNx4MV23uXK_NW8RXMcmLhRtxiiwUYNhgGms9cw1LfgzfYs4SYpdqe10qANWIEqYrwKgQzEgtfMKA4jYW5bq7mhCtnI_yMDHnCVBSfasnlribOTWRaAqEmhDLGzp2ScuoFyeZ-e7lH79rxW89YEa99e2AnqA4XPaoKoOr7jSk6_dkzF2OVji8fYFnhyhAjMO6IbjqSbpmS9LjlexNaHD5YqdOlcmsxH9bPQRZ-RiMO0_wYStXnDwaE47tuXL1EcsC0bI1amg6DJzOvq8pWWROgLvCWF6sOU4Vc2VIg9UwoQcvQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8bacd124f0.mp4?token=iXjLt6QqB6L1-U7HFSaJX85isbvkGDpP29I7obieTNx4MV23uXK_NW8RXMcmLhRtxiiwUYNhgGms9cw1LfgzfYs4SYpdqe10qANWIEqYrwKgQzEgtfMKA4jYW5bq7mhCtnI_yMDHnCVBSfasnlribOTWRaAqEmhDLGzp2ScuoFyeZ-e7lH79rxW89YEa99e2AnqA4XPaoKoOr7jSk6_dkzF2OVji8fYFnhyhAjMO6IbjqSbpmS9LjlexNaHD5YqdOlcmsxH9bPQRZ-RiMO0_wYStXnDwaE47tuXL1EcsC0bI1amg6DJzOvq8pWWROgLvCWF6sOU4Vc2VIg9UwoQcvQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇾🇪
بازرسی امنیتی در مراسمی که تحت کنترل حوثی‌ها در یمن برگزار می‌شود.
آن‌ها به دنبال کمربندهای انتحاری و مواد منفجره هستند.
همراه داشتن سلاح‌های شخصی مانند تفنگ‌های تهاجمی و خنجر برای مردان یمنی امری عادی‌ست
😳
@News_Hut</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/news_hut/70668" target="_blank">📅 17:04 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70667">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/afe281d624.mp4?token=PmT7Ch0al9ybxY5C21Ndr5Aqt6vPZwQ7zfuuR9oZVlcgy0283gGn1cUd2ByartsuB6klSwYks1Bw6pPb4QSI99nYJI_Qjw8dJbdqCt3Pc4IDZv1GaKfgely-8t--FgdLUflUMXi_-IDnxsgGaKv708zZaLm_px2rvUFO1qF3nqQW3N29mkCY0D7p_Ntj71VgazlTL3vPcHEAdvlI8T2ES-JTeJFfI3TfRpjz-UZhFGdROp7jLODSq8QJBRc47LQZqDr0sur03_5kLO28v93Ar-Vwu11jKV1_9rfOWh62HWD2mNG1mGNUom3iDy6C2tP4K9vhWNIJgKwPYkD8u2683A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/afe281d624.mp4?token=PmT7Ch0al9ybxY5C21Ndr5Aqt6vPZwQ7zfuuR9oZVlcgy0283gGn1cUd2ByartsuB6klSwYks1Bw6pPb4QSI99nYJI_Qjw8dJbdqCt3Pc4IDZv1GaKfgely-8t--FgdLUflUMXi_-IDnxsgGaKv708zZaLm_px2rvUFO1qF3nqQW3N29mkCY0D7p_Ntj71VgazlTL3vPcHEAdvlI8T2ES-JTeJFfI3TfRpjz-UZhFGdROp7jLODSq8QJBRc47LQZqDr0sur03_5kLO28v93Ar-Vwu11jKV1_9rfOWh62HWD2mNG1mGNUom3iDy6C2tP4K9vhWNIJgKwPYkD8u2683A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
خنده‌‌های علی مدنی‌زاده، وزیر اقتصاد در واکنش به فشار گرانی‌ها بر مردم
@News_Hut</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/news_hut/70667" target="_blank">📅 16:32 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70666">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dc123970b7.mp4?token=gFIKwbcoCwT_oSqM2kZz3-00eElx-Ez6UvoaGjZ-L4dNSCywL1DVZnjwnAnAEJ0Xo3m6b90IFjvCqDQAc6lJJFgCNXvgtorXUZzDjGH0pUbv3FgeRzKwhMctf3iOBHkFFoA9MZo2Uz9ppU9n3yLFH9DZQ5xQngRU3-0X_hi2q8EumkSEdCC953HdXm80cMDhKhTkHwTFJprxiNtUp1Jo_LvODrsiDyoZloGE3gKK3HrE2UQ3LRDxsW6sb_Glq7KwjmmxAZZsc-yNjJrjJc3rhFszhbW9QmmiSYe-2XcM4UTAkrre_94EcHiEOquWEHl7r_aoWsr67h-23ib88pxRnw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dc123970b7.mp4?token=gFIKwbcoCwT_oSqM2kZz3-00eElx-Ez6UvoaGjZ-L4dNSCywL1DVZnjwnAnAEJ0Xo3m6b90IFjvCqDQAc6lJJFgCNXvgtorXUZzDjGH0pUbv3FgeRzKwhMctf3iOBHkFFoA9MZo2Uz9ppU9n3yLFH9DZQ5xQngRU3-0X_hi2q8EumkSEdCC953HdXm80cMDhKhTkHwTFJprxiNtUp1Jo_LvODrsiDyoZloGE3gKK3HrE2UQ3LRDxsW6sb_Glq7KwjmmxAZZsc-yNjJrjJc3rhFszhbW9QmmiSYe-2XcM4UTAkrre_94EcHiEOquWEHl7r_aoWsr67h-23ib88pxRnw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
ویدیو وایرال شده از یک طرفدار حکومت :
قیمت دلار همینطوری میره بالا و ارزش پول ما همینطوری میاد پایین
ولی این میتونه به نفع ما باشه چون برای اون خارجی محصولات ما میتونه ارزون تر حساب بشه و بیشتر تحریک بشه تا کالای ایرانی خرید کنه
این یعنی فروش بیشتر بیکاری کمتر و چه بسا درنهایت مهار تورم و توسعه اقتصادی!!
@News_Hut</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/news_hut/70666" target="_blank">📅 16:00 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70665">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GSpmjFBJJAADvz6egvHkWd7nV9V4qc__o465Bd6i57C27KsSEwmwSr4ihFZcq4k5BXPbtqzSHXeukbwIWKtxLGpOPLA5V0E36twBr-dMbmNrjObtQDN8SuIHIhPHAIqD7GW8nyZfnQLexnYhz6uxyuLTHuielK_8jK-5QPMHOkGBetMoj5448v0O0GRhk7kmCDbkjx1ZShS9CGRw5EaAPzO1JXV-IfqP9803ewg-7sjDcr4Y5w8ZsIZIPdW3sMfY0YGSQagffuc3MCJW_-9XMuQ_kz8rbsvaNt1VCQb1ezANvEiPzSyctRz9aoGxY6uhiqXpBGa8nSgGm5Mrx91cxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
〰️
📰
سی‌ان‌ان:ناو هواپیمابر USS Theodore Roosevelt همراه با حدود ۵۰۰۰ نفر قرار است در هفته‌های آینده به خاورمیانه اعزام شود.
این استقرار حداقل ۷ ماه پیش‌بینی شده است.
جان پریمن، Master Chief Petty Officer نیروی دریایی آمریکا، گفته خدمه می‌دانند مأموریت بیشتر از هفت ماه خواهد بود و فرماندهی به آنها گفته برای ۸ ماه برنامه‌ریزی کنند.
این اعزام را در ارتباط با فشار عملیاتی ناشی از استقرار طولانی USS Abraham Lincoln قرار داده؛
لینکلن بیش از ۲۵۰ روز در دریا بوده است
.
@News_Hut</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/news_hut/70665" target="_blank">📅 15:35 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70664">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/efaaeae9eb.mp4?token=VzrCtx6v-cl26xqOW_LWlwWIWP1v7lZwD4mxktCDG1qXg3zMzjKGuBwVguLrh8vyLTTH8g3SXJF4Hevoi4wIYBuLh2nsx2o6QSY4KK6svyNP53UzsaC0eTRUm0Z1hVa7F241cdpC1ej32K7ER5FMUG6vpH6wjlyZqW8ZHfnj2BhpwwkAkdO2VbD_pMyHAtwVNaMamZcn7WYijq9bcJCxKCpv-tHBwAYbhRUEzXbaF5RpSjFjj-UYq3ZTMsMuC8-lIlkRylWaMt7Km6H0eIsE1mkQTrQwjcT1yxbhaX0Zi32tGGO0Me_1tvqUG4Snxga8IAWFHZYOQ_6dTp9D8uZ9qQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/efaaeae9eb.mp4?token=VzrCtx6v-cl26xqOW_LWlwWIWP1v7lZwD4mxktCDG1qXg3zMzjKGuBwVguLrh8vyLTTH8g3SXJF4Hevoi4wIYBuLh2nsx2o6QSY4KK6svyNP53UzsaC0eTRUm0Z1hVa7F241cdpC1ej32K7ER5FMUG6vpH6wjlyZqW8ZHfnj2BhpwwkAkdO2VbD_pMyHAtwVNaMamZcn7WYijq9bcJCxKCpv-tHBwAYbhRUEzXbaF5RpSjFjj-UYq3ZTMsMuC8-lIlkRylWaMt7Km6H0eIsE1mkQTrQwjcT1yxbhaX0Zi32tGGO0Me_1tvqUG4Snxga8IAWFHZYOQ_6dTp9D8uZ9qQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
سیزدهمین فرزند مادر ۳۳ ساله بدنیا اومد
؛
از مرده میپرسن چرا این همه بچه حالا جوابش:
اساسا بچه ها رو دوس دارم من ، هزینه هاش؟؟ هزینه هاش با خدا
😳
@News_Hut</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/news_hut/70664" target="_blank">📅 15:01 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70663">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/25e2d9d80b.mp4?token=UHVRLkjnAg2tcR-uhM3TeYhL7y8edGiNk2rJUc8C_vwwYmz-uFDdsdNEP67raXBmtYRzNpvR1l9uDl4fauSSqmh36S3_SyINwiVJN7V2_ZCAaxh_Pgu6HfCNC1zmjHDHvxoCOhoPrg2cKawbR0LW6CUTy1kaTVxjq7L1PJSz750FukwvUFTY6rU_JZo8keLAllu7hs-FHnfwSCds0NNv_yFlQPLYRP4uX8NinovIkQ-9thShCaleIKaLAIeKcWs0vYQJdix2Ne57HDzpDLYVFAKUwwQ5Q5sg4F2Q9CFMtudrZyQQ1IjoyxQPgnmuEPQgLllahwbK2tFPJJcWsKmKng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/25e2d9d80b.mp4?token=UHVRLkjnAg2tcR-uhM3TeYhL7y8edGiNk2rJUc8C_vwwYmz-uFDdsdNEP67raXBmtYRzNpvR1l9uDl4fauSSqmh36S3_SyINwiVJN7V2_ZCAaxh_Pgu6HfCNC1zmjHDHvxoCOhoPrg2cKawbR0LW6CUTy1kaTVxjq7L1PJSz750FukwvUFTY6rU_JZo8keLAllu7hs-FHnfwSCds0NNv_yFlQPLYRP4uX8NinovIkQ-9thShCaleIKaLAIeKcWs0vYQJdix2Ne57HDzpDLYVFAKUwwQ5Q5sg4F2Q9CFMtudrZyQQ1IjoyxQPgnmuEPQgLllahwbK2tFPJJcWsKmKng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
چند شب پیش یه دختره اومد از خودش ویدیو تولد بگیره تنهایی که یهو یه 207 اومد کنارش و سه تا پسر اومدن وسط رقصیدن و تولدش براش جشن گرفتن
@News_Hut</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/news_hut/70663" target="_blank">📅 14:35 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70659">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZzonO9XnVDpu2AYPNPNxXtwEtoCrut1-lyK096PwXnR5dYHypwN7EqY9Iz-jVawjICcEIHhAEm_XNBWeRrGrj9mbWLQyRq_y6QqVVJoefGIXbkYnyQ_Mr2Y4u35qw0oAGX8c71ZYsq4OluNgYchF5Ze--UQhGcoOq4t-gTK6tOZdZd8MfxhWx5V1rmFxXyXylaPxIDHQ72MqvLHTS1K54_f0bQbc9qOdV2_2xGybIi0YKaBSDqBdGZtBYERMr2P0ts_94_fG9NgbbXRj2ofbKd4LdvvvyFM7oxw9KTEwGw0a_hoFta_vw3H6bKCFI4X44OBh7Fch5ZV5Ag3_bC1aQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HM1g7t1kNPdiHRbLK6CFlwTRpNdb9RPSMRXYdDWgPBJ1wQMGRVhflqpeO0DR5dmy0cdqRMTKaZR_fBlAuDecujLbTfX4P2La1fAK88sMHoS1QVgMUwNICSWGKONqVQ7zkFiNwqSLLZ8MIS7G0ruYsFh_n8z6bJuX7MfV7na36srTee73XdRQOpidfM7dCjveZICTHkwzaX0Ydrekix7g5yVATtzbxpS4HAdAeDpprsdtFM3WKqijCLfiv6iN2sjxvXHwlUJ0-7SN_oEFKkHNIojYffA-wSC0oF-2X89ImGvCIuXQKvuAxPth3HWH_OS2GnuZNmMq6UpLWRc7HV8cHQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bbaeab0414.mp4?token=SW1HJos2n3ytxiZQHdtn9LwdnMA8pgE60fipq-bB0kKgj84eTfWy34ldGtVxS3vlsVUyJu-lywlJCDN5xavIAXf5_yjaH2Uv_R9KacIxi-U8gOaBxStb9XbX5krHW2eaTD05QpTLum9TOsexu1JavfR9-Arjq90y2ttt9weXVJWzKDar2XZILoyhtzO6KCnZJA6zAySD4862BkEqKDFO0CLYyY0w1Li6XmlxEsfrQLnS3SK0-zEAxpLLetIPkExpVnfFnHZFivwlcbmr9gi2XFaKj-eCxEsrVKS0J2o4CpleIYieMZjYNM9hiL6RlZESqW71u5Tt9VB6rMAxny8niQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bbaeab0414.mp4?token=SW1HJos2n3ytxiZQHdtn9LwdnMA8pgE60fipq-bB0kKgj84eTfWy34ldGtVxS3vlsVUyJu-lywlJCDN5xavIAXf5_yjaH2Uv_R9KacIxi-U8gOaBxStb9XbX5krHW2eaTD05QpTLum9TOsexu1JavfR9-Arjq90y2ttt9weXVJWzKDar2XZILoyhtzO6KCnZJA6zAySD4862BkEqKDFO0CLYyY0w1Li6XmlxEsfrQLnS3SK0-zEAxpLLetIPkExpVnfFnHZFivwlcbmr9gi2XFaKj-eCxEsrVKS0J2o4CpleIYieMZjYNM9hiL6RlZESqW71u5Tt9VB6rMAxny8niQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
ایرج مصداقی از نزدیکان شاهزاده رضا پهلوی در یک مصاحبه درباره علی کریمی صحبت کرد؛
صفحه اینستاگرام کریمی در اختیار شخصی به نام امید دانا است.
بعد از انتشار این صحبت‌ها، کریمی در چند استوری به‌شدت واکنش نشان داد، از مصداقی خواست ادعایش را ثابت کند و شاهزاده رضا پهلوی رو مخاطب قرار داد و برای اظهارنظر درباره این موضوع ۲۴ ساعت مهلت تعیین کرد.
⏺
مجدد مصداقی در ویدئویی جداگانه به واکنش‌های کریمی پاسخ داد و اونو مخاطب قرار داد؛
علی کریمی یک آدم ابله بی شعوره که سوابق ننگینی داره و توی فوتبالم هر تیمی رفت اون تیم رو بهم ریخت. هیچ سابقه مبارزاتی هم نداره
حالا اومده ما رو تهدید میکنه. آخه مردک تو عددی هستی شاهزاده رو تهدید میکنی؟! چه غلطی میکنی مثلا؟! داریوش که میبینی که بلایی سرش اومده تو انگشت کوچیکه اونم نیستی.
بهش گفتن جهان پهلوان باورش شده. اخه مردک کسی که دوتا لگد به توپ زده پهلوونه؟! همین مونده بود تو برای ما شاخ بشی. فکر میکنه چون فوتبالش خوب بوده سیاستم میفهمه. ما اصلا تو رو حساب نمیکنیم ابله.
اینا رو ارزش دادنی فکر میکنن خیلی بالا هستن آقای کریمی با تو یا بی تو فرقی نمیکنه زیاد حرف بزنی صداتو میبرن
⏺
علی کریمی هم در ادامه اومده گفته؛
از اين لحظه به بعد؛
از هيچ شخص يا حزب سياسى حمايت نميكنم.
در حد توانم به مبارزه‌ام عليه رژيم اشغالگر شيعه ادامه خواهم داد.
این تصمیم من به منزله سنگ اندازی در راه مبارزه دیگر افراد با رژیم اشغالگر آخوندی نیست.
به اميد آزادى ايران و مردم نازنينش
@News_Hut</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/news_hut/70659" target="_blank">📅 13:47 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70658">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rWR5rWcdhcihzCSBNKvKo2WvQuMI8jIWt8r6vxMyXyHH6gwecuSeI4CWgANEjpyuO_68qSVmti7pChSLWSr4cs3p_7f87UWigsk6NO5LJQ6V2S89dtOw_D_-Kg6F-lalw593lkWT2v1hZ4-YWaAJ6WF-vVjuZ0PjEOgvmhNsifwc9gsqef7RUUZaxCNb-RGQnFGgV2lCKK-F0H-FumxTQyg-tnKhiedaWDkjeHcEUEI2myphzQ-JpevgZZgU8Z9bc8oXj17sZgOB3AK8xi2OHiAvXQVv2T4aqGe2KS8Td8qFOVBLYyY6-DClgF2tXNMx1108P9hSjV_inu3vfWvKYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💢
📰
وال استریت ژورنال:جان رتکلیف، رئیس سیا، این هفته در سفری غیرمنتظره به مسکو رفت تا به روسیه هشدار دهد که به کشورهای عضو ناتو حمله نکند.
این سفر در پی ارزیابی‌های اطلاعاتی جدید آمریکا انجام شد؛ ارزیابی‌هایی که حاکی از آن است که پوتین ممکن است در سال‌های پیش‌رو، با انجام حمله‌ای محدود به یکی از کشورهای متحد، عزم و اراده ناتو را محک بزند.
مقامات آمریکایی نگران سناریوهای مختلفی هستند؛ از حملات سایبری گرفته تا تهاجم زمینی در مقیاس کوچک که به احتمال زیاد یکی از کشورهای حوزه بالتیک را هدف قرار خواهد داد.
آن‌ها همچنین نگران آن هستند که کاهش ذخایر تسلیحاتی غرب — که ناشی از سال‌ها حمایت از اوکراین و درگیری‌های اخیر مرتبط با ایران است — بتواند بر محاسبات مسکو تأثیر بگذارد.
@News_Hut</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/news_hut/70658" target="_blank">📅 13:15 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70657">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/c5ef938e2e.mp4?token=mjdXinjzxuSuVXzb1hZ3HPJf3zjvej91THnfDiW1N55CXkLPLiSM-wJoSovdjg2WG1QJG0I9bhBcBFsB2FdJiR_u9EiWWHF3uoZev5h4Kd1N0dEpWbahAoZomRjuijWdBszuRNvScmynR2BhbW4IIJ3f_6bd35R3XsgZP4ciNjytxetPGO_nkyP-3PpDd_jE4fnMnrhIboIg5dnIOVbu1bRb_1bx2-5YRj0HZTld9gTBcDDq0xEvIsorJ94D239zzd3K0--8aX5WapREB_s69AsQ-W5D3QeeSjM_OgZ_9ilaMP643N_RhtRAZUonpKrNXPIsb5bIRZIDuZKiDvYYOw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/c5ef938e2e.mp4?token=mjdXinjzxuSuVXzb1hZ3HPJf3zjvej91THnfDiW1N55CXkLPLiSM-wJoSovdjg2WG1QJG0I9bhBcBFsB2FdJiR_u9EiWWHF3uoZev5h4Kd1N0dEpWbahAoZomRjuijWdBszuRNvScmynR2BhbW4IIJ3f_6bd35R3XsgZP4ciNjytxetPGO_nkyP-3PpDd_jE4fnMnrhIboIg5dnIOVbu1bRb_1bx2-5YRj0HZTld9gTBcDDq0xEvIsorJ94D239zzd3K0--8aX5WapREB_s69AsQ-W5D3QeeSjM_OgZ_9ilaMP643N_RhtRAZUonpKrNXPIsb5bIRZIDuZKiDvYYOw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
از خونواده‌ها میپرسن چقدر خرج کنکور کردین برای بچه‌تون؟ رقما به شدت عجیب غریبه.
@News_Hut</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/news_hut/70657" target="_blank">📅 12:32 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70656">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Cx7ffo1nDVb_NOQSMWvaX6X868ItRJrnPr3FMhhcqSP_1yV-ZFOB4Y2LFYQRnsdqxsQyk5Sg0WT34ba_cVUpIpNyn3yxWiyaLaVzlqXv9m8e4ITy82yZIldeNdqJS5MvgQj0YwFgsgjXgIl4KBbKFtpj_QMxZzcvULnT48474SH-WaVi1o2Jhl1vhuqTd2MMhxvAXjGXwdVwXddJRxQtbyqRdB0Kg61nf4r-atgtOOBLfYooKBjltVjioHSDz0FN7vTsCzKZrd1-TicOJ53APz8nEtKTr_O_6_UDMEu6w9Dbn3xNC1fiOhy2QG2Zo7E_veccgh8ul3BxXnarNgkFGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
سازمان عملیات تجارت دریایی بریتانیا:
گزارشی دریافت کردیم مبنی بر اینکه یک نفتکش در تنگه هرمز هدف اصابت یک پرتابه قرار گرفته و در پی آن دچار آتش‌سوزی شده است.
آتش‌سوزی در نفتکش در تنگه هرمز مهار شده و تمامی اعضای خدمه در سلامت هستند.
@News_Hut</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/news_hut/70656" target="_blank">📅 11:59 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70655">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0fee8faf9e.mp4?token=WDppUiqZLd88k3zFrJ80gmzXnd3ir2jGkoWLwmQlvJPIR5D-a7XJYhMxE5zy2pJMzUeslGKrhv6xhM9aBsaGr3DNXXnyP3m2fxEo9bqmaBQiMpwJCKO2WtxLD14P3f2kxs7zI-xvQpsZQZBNIel9O5eeHJWsyV2cUq784UblkSLNeKuy6ssiGcSpsBHTR0aXawyNQiSXTITEGCJ3d9XxBaHy7gt1BRs7V8YXCE0vxqWg8f-nermebrZUvzYhWjMs6-OMnD-YqeyxBI475LrzJuZ_4IbwQzAzezJgye1r3vvqE_OMHcAaURJoSS4coa_8nGtdZ152kb4RgpG1KozHcA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0fee8faf9e.mp4?token=WDppUiqZLd88k3zFrJ80gmzXnd3ir2jGkoWLwmQlvJPIR5D-a7XJYhMxE5zy2pJMzUeslGKrhv6xhM9aBsaGr3DNXXnyP3m2fxEo9bqmaBQiMpwJCKO2WtxLD14P3f2kxs7zI-xvQpsZQZBNIel9O5eeHJWsyV2cUq784UblkSLNeKuy6ssiGcSpsBHTR0aXawyNQiSXTITEGCJ3d9XxBaHy7gt1BRs7V8YXCE0vxqWg8f-nermebrZUvzYhWjMs6-OMnD-YqeyxBI475LrzJuZ_4IbwQzAzezJgye1r3vvqE_OMHcAaURJoSS4coa_8nGtdZ152kb4RgpG1KozHcA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
🇴🇲
🇺🇸
کاظم غریب‌آبادی، معاون وزیر امور خارجه جمهوری اسلامی، درباره دلیل و نتیجه نهایی مذاکرات عمانی-ایرانی:
ما گفت‌وگوها را با عمانی‌ها آغاز کردیم تا بتوانیم به آن‌ها بگوییم که حداقل در روحیه همسایگی، این اقدام برای باز کردن مسیر جنوبی می‌تواند یک‌بار دیگر تنش‌ها را ایجاد کند، فرآیند اجرای توافقنامه‌های اسلام‌آباد را مختل کند و حتی منجر به شعله‌ور شدن درگیری‌های نظامی در منطقه شود.
​
انتظار ما این بود که با کمک دوستان عمانی‌مان، شاید بتوانیم این مسیر را ببندیم. با این حال، فشار آمریکایی آنقدر شدید بود که متأسفانه این مسیر جنوبی بسته نشد.
​
سپس آنچه رخ داد را دیدیم: جمهوری اسلامی ایران تصمیم به بستن تنگه هرمز گرفت و در ادامه، شاهد درگیری‌های نظامی بودیم.
@News_Hut</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/news_hut/70655" target="_blank">📅 11:33 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70654">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e7b3da01db.mp4?token=BQ8h0d8NtseAKYCUUhfHfJ0abMFpc5JHiphhuYi3FqyoKGHtQyefRnB5tx141TLhKYgWEBvWgeW4LoRwrVTFjA-6nXKuiHu8EUv3lLe2WtJdz57tlTfaJJPkpToQ31NUpBGAtuyeo2iQuRRNbuSALmthyfPEoZ_dUhlEN6JdsUCerkNYlsferglPFVbK247eTAl64SAm8tNEg3BzMOPu-riyWSQ2KzsJo1XVVrLFjYNT6p2NAKt9xWqCzpOcf6blVXpbnLoKHzNiKZXznmBo1UPKxbrq_vKDoyL2cxRzFqz0asePm_UienMGzI0j6vZw14w77bToqL3I3B3jETv8Pg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e7b3da01db.mp4?token=BQ8h0d8NtseAKYCUUhfHfJ0abMFpc5JHiphhuYi3FqyoKGHtQyefRnB5tx141TLhKYgWEBvWgeW4LoRwrVTFjA-6nXKuiHu8EUv3lLe2WtJdz57tlTfaJJPkpToQ31NUpBGAtuyeo2iQuRRNbuSALmthyfPEoZ_dUhlEN6JdsUCerkNYlsferglPFVbK247eTAl64SAm8tNEg3BzMOPu-riyWSQ2KzsJo1XVVrLFjYNT6p2NAKt9xWqCzpOcf6blVXpbnLoKHzNiKZXznmBo1UPKxbrq_vKDoyL2cxRzFqz0asePm_UienMGzI0j6vZw14w77bToqL3I3B3jETv8Pg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
شعارهای عجیب حامیان حکومت در تجمعات شبانه:
دلار شده 200 تومن همتی
یه کاری کن میگن تو بیغیرتی
حیف که نمیشه بکنیم به تو بی احترامی
ریاست محترم جمهوری اسلامی
@News_Hut</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/news_hut/70654" target="_blank">📅 11:04 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70653">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/45450621ea.mp4?token=DPHH8_dP5ud6nKbtZDIThMdl83VSXFAx6gPTYFDF-PqsE7UQq-OAarGtAXYPKWWC0eoxl4nbHWr4ZrLVDwvWN074eElnhfLLmQLjAMIw2JvTIPT3C1od3vKiXUtnOXbi2B_24H3c4mdki6VxQEzyxILn6kRqlozleb2pCni5YwJ9dEuKUkx_WLAhv8vZ0m0rrNDFreXEGmLYzOiZx2QdVKQBWqcCmBM3AAT1siMUV4_Q4MxKEtc0Qz4TWia9KoEC3dcB4PnxDw2FjuMwhI8Wh1l_xVTiIPrGOWlxhey11phRPihft3jVZzDLdusWwa16nKov9kFEvJvMq2x58CAJBjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/45450621ea.mp4?token=DPHH8_dP5ud6nKbtZDIThMdl83VSXFAx6gPTYFDF-PqsE7UQq-OAarGtAXYPKWWC0eoxl4nbHWr4ZrLVDwvWN074eElnhfLLmQLjAMIw2JvTIPT3C1od3vKiXUtnOXbi2B_24H3c4mdki6VxQEzyxILn6kRqlozleb2pCni5YwJ9dEuKUkx_WLAhv8vZ0m0rrNDFreXEGmLYzOiZx2QdVKQBWqcCmBM3AAT1siMUV4_Q4MxKEtc0Qz4TWia9KoEC3dcB4PnxDw2FjuMwhI8Wh1l_xVTiIPrGOWlxhey11phRPihft3jVZzDLdusWwa16nKov9kFEvJvMq2x58CAJBjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👑
سخنان جالب امیرعباس هویدا و آمار ارائه شده توسط وی درباره وضعیت ایران در آن زمان .
@News_Hut</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/news_hut/70653" target="_blank">📅 10:34 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70652">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">‼️
اعترافات اندرو تیت (بوگاتیت چه رنگیه) و داداشش تریسان تیت :
اون زندگی فوق‌لاکچری که از ما تو فضای مجازی می‌دیدید، قرار نبوده واقعیت کامل زندگی‌مون باشه؛
ما داشتیم یه نقش بازی می‌کردیم، مدل کارمون اینه که هرچی محتوامون عجیب‌تر و اغراق‌آمیزتر باشه، بازدید و لایک بیشتری می‌گیره و در نهایت پول بیشتری درمیاریم.
اون بوگاتی‌ها و استون‌مارتین‌های چند میلیون دلاری که تو ویدیوها می‌دیدید اجاره‌ای بودن و اون سوپرقایق تفریحی 50 میلیون دلاری هم مال ما نبود؛ برای تبلیغش پول گرفته بودیم.
حتی خیلی از حرف‌هایی که درباره ثروت عجیب‌وغریب یا داشتن چندین پاسپورت می‌زدیم، بخشی از همون شو و شخصیت اینترنتی‌مون بوده.
@News_Hut</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/news_hut/70652" target="_blank">📅 10:04 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70651">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/630909b4ac.mp4?token=r5FOoMyU0ib02M6b9GI9Ix3VTMqCOJ6xNoXNd4jOFoVFwtqzGk6486QvtUIh0p6iAOuogfioCG37EUQCw5yQ3TXJZjXYiPwBWuR_h5c8yKHBmDk0B3ZPOm0B1q_pA5770cFHXn8GiUriYQcATaZlemBummrtOYyXzSRSyOMZkBs9I-Zx7Lqnl-naK4yhZtMl1UdZrsZF8DSTkJjNg85IxDIA6-WvhjZjOU3r_3Rx7sQ1oauHiecc17erwprzTEwgZMZedbzDr6J6nSfaUA3i1lVJ4R2w5UydWuaQgl3yqhZQ0_zTBsJcHm9CmjUh3LCJu9-EBArdsgVcztN_iF6SzQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/630909b4ac.mp4?token=r5FOoMyU0ib02M6b9GI9Ix3VTMqCOJ6xNoXNd4jOFoVFwtqzGk6486QvtUIh0p6iAOuogfioCG37EUQCw5yQ3TXJZjXYiPwBWuR_h5c8yKHBmDk0B3ZPOm0B1q_pA5770cFHXn8GiUriYQcATaZlemBummrtOYyXzSRSyOMZkBs9I-Zx7Lqnl-naK4yhZtMl1UdZrsZF8DSTkJjNg85IxDIA6-WvhjZjOU3r_3Rx7sQ1oauHiecc17erwprzTEwgZMZedbzDr6J6nSfaUA3i1lVJ4R2w5UydWuaQgl3yqhZQ0_zTBsJcHm9CmjUh3LCJu9-EBArdsgVcztN_iF6SzQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
رکنا گزارش داده یک فرد که بلاگر اینستاگرام هم بوده، عاشق ماشین‌های مدل بالا بوده و توی دیوار دنبال آگهی ماشین‌های گرون می‌گشته.
با صاحب ماشین قرار می‌ذاشته، می‌گفته یه دور تستش کنم و بعد با ماشین می‌رفته!
نکته عجیب ماجرا اینه که بعدش زنگ می‌زده و می‌گفته من دزد نیستم؛ چند روز با ماشینت دور دور می‌کنم و بعد سالم پسش میارم!
ظاهراً هدفش فقط لذت بردن از ماشین‌های مدل بالا بوده و بعد از چند روز هم ماشین رو سالم برمی‌گردونده!
@News_Hut</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/news_hut/70651" target="_blank">📅 09:33 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70650">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/29a5f45322.mp4?token=foC_qk4qEAT1oBFPJnLzgF2GC80a504qF8O6yZkbQlDcw6LoRY9VJL-NT_0xN92-Hrmv9IPVYgtil5SRj5Z5wLaiEnQB3t3fFBPKmbrv4ZdE83y_gRS3miGkoBeq19m0EL8rVKk-0iBVZ_1sZwozu3GIsvuJIqulrd2IZNIhjg_u3Tg_oXVbRHYH8RwbOJwONz4LZRPMl4wvjXTuxVqceAV8VXt7CkX1YcYgfvSCaFQLJDde04k2lNBCuwFZ0k1cpqfrZvXwmNd5L2UR_ypIUADraYUM5u7bHGBwfUOw5pGF5nihnGeT46IB8uxQuQcI1_xWBxjgXdphQ76rjKX8hg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/29a5f45322.mp4?token=foC_qk4qEAT1oBFPJnLzgF2GC80a504qF8O6yZkbQlDcw6LoRY9VJL-NT_0xN92-Hrmv9IPVYgtil5SRj5Z5wLaiEnQB3t3fFBPKmbrv4ZdE83y_gRS3miGkoBeq19m0EL8rVKk-0iBVZ_1sZwozu3GIsvuJIqulrd2IZNIhjg_u3Tg_oXVbRHYH8RwbOJwONz4LZRPMl4wvjXTuxVqceAV8VXt7CkX1YcYgfvSCaFQLJDde04k2lNBCuwFZ0k1cpqfrZvXwmNd5L2UR_ypIUADraYUM5u7bHGBwfUOw5pGF5nihnGeT46IB8uxQuQcI1_xWBxjgXdphQ76rjKX8hg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❤️
یکی از زیباترین سخنرانی‌های محمدرضا شاه:
هیچوقت به زندگی فعلی خود قانع نباشیم و دنبال بهتر کردنش باشیم.
برای بهتر کردن شرایط زندگی، اولین شرط خونه و سقف بالاسر هست و بعدش قدرت خرید مردم.
محیطی که در آن زندگی میکنید باید شاد باشه، غذایی که میخورید لذیذ باشه و لباسی که می‌پوشید تمیز و لطیف باشه‌.
@News_Hut</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/news_hut/70650" target="_blank">📅 09:02 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70649">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">👑
فقط کافیه مرغ از خیابون رد کنی و‌ پولت چند برابر کنی راحت
💵
👌</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/news_hut/70649" target="_blank">📅 02:23 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70648">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/17cffccbc4.mp4?token=fk79cZd8TzovwyI-xw-qWFbSctB0Lv3r1ThKU_mBWNfYZLyxJMhNbUe1UeyOGn-EMeDUHGwjKZKuNRYNivM1neIskC1a-Y2-TyJo-PweaBgmvErtr0cN_Abv6f4xX-rfUFPARbKTXfAhbTxSdwh8FUvSfGfaWC9wNzcLH8ueZPnXwDGgNOxiggqeAYmw7SN0qXGevuwq2WsEX_ovWX4QeCgO4JMY9aC_FKeXmtWkW4DFxAMjyQm9LWqY224EzZxqe0RtTM_R4ABv-h49fd6tITIPmRjB_TNxUB-snzdKKQLI3upcdz2Z40N-EUBDELwUBv3YZz8Eq9zH87HucQNoHQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/17cffccbc4.mp4?token=fk79cZd8TzovwyI-xw-qWFbSctB0Lv3r1ThKU_mBWNfYZLyxJMhNbUe1UeyOGn-EMeDUHGwjKZKuNRYNivM1neIskC1a-Y2-TyJo-PweaBgmvErtr0cN_Abv6f4xX-rfUFPARbKTXfAhbTxSdwh8FUvSfGfaWC9wNzcLH8ueZPnXwDGgNOxiggqeAYmw7SN0qXGevuwq2WsEX_ovWX4QeCgO4JMY9aC_FKeXmtWkW4DFxAMjyQm9LWqY224EzZxqe0RtTM_R4ABv-h49fd6tITIPmRjB_TNxUB-snzdKKQLI3upcdz2Z40N-EUBDELwUBv3YZz8Eq9zH87HucQNoHQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
بچه ها اسم این بازی عبور مرغ از خیابون  هست ویدئو نگاه کنید خیلی راحت 8 میلیون ازش سود گرفتیم
😍
😤
اگ توم دوس داری خیلی راحت از بازی های انلاین پول در بیاری حتما عضو کازینو شبانه شو
✅
توی کازینو شبانه بهت اموزش میدیم از بازی های انلاین پول دربیاری
👌
🔔
کانال کازینو شبانه راهی برای چند برابر کردن سرمایت
🤷‍♂
➕
کسب درامد انلاین با یه ادم حرفه ای یاد بگیر و‌ پول دربیار
💵
a4
🎯
همین حالا عضو شو و شروع کن
👇
https://t.me/+FaoDjhEVG34wMWFk
https://t.me/+FaoDjhEVG34wMWFk</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/70648" target="_blank">📅 02:23 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70645">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aff574e553.mp4?token=GFAs0eHds8RQPX5JUA-LpLQ1zC4sFqexpgJAOwOzBRUFd45-HaGZlxPG25hWt4yj3z2YjQdCalbtff6m-Cwy3_ZyyYsRcJ7oLjBocZliv8q-lxY5_wuj9mpYxCoEYVYuJQHB9REZMpxunaUzd3Tejnpy6U4uZ4_0Lz6r140SToUDDcuKHo4Zsqsz0P18XWAITkkltEhcRw0ui-0mxVNRE5EjdJQpGAn61oW8MKE6yGlJwmagsGgG__rmkRwCSlBeBYrYe-Hjg3YnnOxPzUZNlzVKwNuhS9tO8euKblAhkjGduDsnXqDRjVNb-uyBCxtVrgQ7yD6Ux0EHOJqhrTbgaw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aff574e553.mp4?token=GFAs0eHds8RQPX5JUA-LpLQ1zC4sFqexpgJAOwOzBRUFd45-HaGZlxPG25hWt4yj3z2YjQdCalbtff6m-Cwy3_ZyyYsRcJ7oLjBocZliv8q-lxY5_wuj9mpYxCoEYVYuJQHB9REZMpxunaUzd3Tejnpy6U4uZ4_0Lz6r140SToUDDcuKHo4Zsqsz0P18XWAITkkltEhcRw0ui-0mxVNRE5EjdJQpGAn61oW8MKE6yGlJwmagsGgG__rmkRwCSlBeBYrYe-Hjg3YnnOxPzUZNlzVKwNuhS9tO8euKblAhkjGduDsnXqDRjVNb-uyBCxtVrgQ7yD6Ux0EHOJqhrTbgaw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
شهروندان اسپانیایی ساکن منطقه "سئوتا" به ساحل "ترامپولین" حمله کردند تا مهاجران را بیرون کنند و اقامتگاه‌های موقت آن‌ها را تخریب کنند.
@News_Hut</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/news_hut/70645" target="_blank">📅 01:44 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70644">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RAHMfThr0NvBLryZYRR7t5pJ-vpWexNkMQyilZhugBMxMgCj_Zw2XeSou-FF5H2c_BhDWroGfEoF4Qzvid8qom1muz2G9dMuGwK-t3BYWRivTB_eRD9QwUOwCpOkytFeCMV1-Jpojr3a05WqXIblUlHpVet8pHehRzpG4UZNtrvh9UEvwmM9o87AmgYncZm1UkYPwvcUCdP83FQDXZtJxwXKUD6ZHCGIdb5nH1UYzFuoGQxRDt6c2X0cyXmPh_buSvxyxVa0sYis-gRHTyUX59_OKATlTVYOW-_KirPCQoiFN2YMftX-W9FHLofUnsdn4zFqUgDc-WcGZd3e8chFmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
🇮🇷
اسماعیل بقایی سخنگوی وزارت خارجه:
آمریکا ناو «یو‌اس‌اس آبراهام لینکلن» را برای نمایش قدرت به منطقه اعزام کرد.
پس از ماه‌ها جنگ — و بیش از ۲۰۰ روز بدون حتی یک بار پهلو گرفتن در بندر — این ناو اکنون برای استراحت و تجدید قوای خدمه، راهی تایلند است.
مأموریت: نمایش قدرت.
مأموریت فعلی: نمایش تعطیلات.
«خسته‌ام، رئیس.»
@News_Hut</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/70644" target="_blank">📅 01:25 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70643">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3143921715.mp4?token=prXK97uCOB4EqR7ZQiD96JvHtycTrSkkFsLsOtbxeYFbiniHm8riviL5F0NeFvO2RUfqQLRL3eIFFUYLtsePFKYL6XmutqxdN0fN9QY6E3N7RzUOtuTppTqOHPNb_3JYB34gTphjHR7ldrTWDLqYOIy6PzQvFUzj-qf5XUktK_Tku_mCezafmhUpGm9Jt0eyaJOYYBcc-tf4HSIlhNCeTolyz3-2C3e_LP02nV5VvbTKzTBxYuiJ935LyEsgYbyMBU6BkKGpivI5lI_ZsTZf711f2vQgkRXTBS9r_cRaoez7SADgNrbiBRipWg6kREzU-CUs2Y1kpWRdI-fxboon1g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3143921715.mp4?token=prXK97uCOB4EqR7ZQiD96JvHtycTrSkkFsLsOtbxeYFbiniHm8riviL5F0NeFvO2RUfqQLRL3eIFFUYLtsePFKYL6XmutqxdN0fN9QY6E3N7RzUOtuTppTqOHPNb_3JYB34gTphjHR7ldrTWDLqYOIy6PzQvFUzj-qf5XUktK_Tku_mCezafmhUpGm9Jt0eyaJOYYBcc-tf4HSIlhNCeTolyz3-2C3e_LP02nV5VvbTKzTBxYuiJ935LyEsgYbyMBU6BkKGpivI5lI_ZsTZf711f2vQgkRXTBS9r_cRaoez7SADgNrbiBRipWg6kREzU-CUs2Y1kpWRdI-fxboon1g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
شکار شکارچی
اپراتور پهپادی روسیه توسط یک پهپاد FPV اوکراینی کشته شد.
@News_Hut</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/70643" target="_blank">📅 00:40 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70640">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EOIaPw7I0ApA7FqQCkU7hcg9s0r4oqZNdNZj7AEdF0PsBbuxLbi3p4VDJsWi0y6RJ09m_1seagfgF9d4MC2AxrDxL1TO4Q7zOphK3jOy7G9XVSHOEqTgXwsss2KsP_CMVM1eE1wdaP9UElhfmbbyZV3xo1J9Pu_pJu8DjFaYVeOjJoSe3RLHgV1CAaOZjFiPJ9D0eX0aF2wAxSYAlZYCwn0sMnBCriBBaO_rASHyqvkaRg8dlvr12p3xndzHATODuq3AFWUcTgYy0J0FkiaVyEb6de6JmGGLO_4dqB-4bg39nT8JiUsNla6aXK8tjicqSNRE77CDZs7Kri94GXNeZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9d4cb4aa2f.mp4?token=HezOrZ4bqNz87NfH_UTcNeZF30p2OVFspU64bvSchCTwKLYH_ElINsb5P6IrlWeGASXspW7FeZsUpeFgz-ViNxXs5t9VuxBfFSeWUJdSdWeaZxPJ1-HbOnes7Rigd9DO68GnBXbhPtZo7tnUwh7Pu4fEKjpoxgU8D96YRPMYctNMnvpIwNiD-_FpjVEIK1475AFp2bX8qwPsxkPAZ7qxoZD11Z9J06wGcXau7yEw1J-yv6J1Qjk9_gXI683gfv547xsVk9PvHC4XFXptHKZrUk_7aotl_Wjx8NQOVVr2CTGjDOwkCsEgYBkT1Vovyb83I25hSVueQce-R4T95d2aVg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9d4cb4aa2f.mp4?token=HezOrZ4bqNz87NfH_UTcNeZF30p2OVFspU64bvSchCTwKLYH_ElINsb5P6IrlWeGASXspW7FeZsUpeFgz-ViNxXs5t9VuxBfFSeWUJdSdWeaZxPJ1-HbOnes7Rigd9DO68GnBXbhPtZo7tnUwh7Pu4fEKjpoxgU8D96YRPMYctNMnvpIwNiD-_FpjVEIK1475AFp2bX8qwPsxkPAZ7qxoZD11Z9J06wGcXau7yEw1J-yv6J1Qjk9_gXI683gfv547xsVk9PvHC4XFXptHKZrUk_7aotl_Wjx8NQOVVr2CTGjDOwkCsEgYBkT1Vovyb83I25hSVueQce-R4T95d2aVg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇨🇳
🇳🇵
ویدیو هایی از سیل آخرالزمانی و وحشتناک امروز نپال که باعث شد صدها نفر کشته و ناپدید بشن!
ویدیوها عمق فاجعه رو به خوبی نشون میدن!
@News_Hut</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/70640" target="_blank">📅 23:55 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70639">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eee2e6eb68.mp4?token=EGwvdi0hwRzHJPciKN0HV7Eit-C42akiawL7no6v2etwPewBnqL37FdTFF4JArLNabytQZOWHwGk59Ods91dcaum9gQuN8Jme8rHXwwfdOAxkZPuWj8dKajSVwzprjBAALBghcHSkGUUJ3Ep23OyeLck0gm8Vb6xoJmNmNHLl8muyyb3J6vd-bGaEQg0BuEfNvZL9djWvyeyIYPIjb-RSV-KrXzl_Ff6Yq28yGaHtS_X1zaAzhUzWUF_zng6CZbHPhe7Yqm-0fCDKE-TN59TY0V33gKxNH9F0kpg7As9kmgmt6vcUwjqySq2yCUdzYafqbrZshNqI03GQRnYznj70w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eee2e6eb68.mp4?token=EGwvdi0hwRzHJPciKN0HV7Eit-C42akiawL7no6v2etwPewBnqL37FdTFF4JArLNabytQZOWHwGk59Ods91dcaum9gQuN8Jme8rHXwwfdOAxkZPuWj8dKajSVwzprjBAALBghcHSkGUUJ3Ep23OyeLck0gm8Vb6xoJmNmNHLl8muyyb3J6vd-bGaEQg0BuEfNvZL9djWvyeyIYPIjb-RSV-KrXzl_Ff6Yq28yGaHtS_X1zaAzhUzWUF_zng6CZbHPhe7Yqm-0fCDKE-TN59TY0V33gKxNH9F0kpg7As9kmgmt6vcUwjqySq2yCUdzYafqbrZshNqI03GQRnYznj70w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
عبدالملکی، وزیر سابق کار:
دولت دروغ می‌گوید که پول ندارد و نتوانسته نفت بفروشد. در طول جنگ ۴۰روزه، فروش نفت ایران افزایش قابل‌توجهی داشت و درآمدهای نفتی کشور حدود سه برابر شد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/70639" target="_blank">📅 23:15 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70636">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e07429c6dd.mp4?token=syP4kzOM5OE5lwF_AEehHdth2ffYF1I3wfZR3ut-99cjCzfOxeWETxVOXqTwNuGOfDKtpecMl6F2aBuO6wC0sL5B9Ct-Kta6GRnz7AEADPkZwMHjX42tmN01UmM64zPXzB4n-ny_w9aw6h9BUBqPcjnuyV6GUmCFNoepcQi1ttt19r2Lp4tD-4Cgf2ulYGsVdcchMCnVQ2oMT8wihgPd4gcJLPDx3yYxCPyMijQOyTaJojWp19m8NhcvaXl_ShcqZcPAHfZL9LM0xdNsP_SQJtchNbV_SHEpBaeuRa4myPc_ugZCt_A8iVfu9q4KLcLM6BV3ALs9VVNAMetltvlaBw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e07429c6dd.mp4?token=syP4kzOM5OE5lwF_AEehHdth2ffYF1I3wfZR3ut-99cjCzfOxeWETxVOXqTwNuGOfDKtpecMl6F2aBuO6wC0sL5B9Ct-Kta6GRnz7AEADPkZwMHjX42tmN01UmM64zPXzB4n-ny_w9aw6h9BUBqPcjnuyV6GUmCFNoepcQi1ttt19r2Lp4tD-4Cgf2ulYGsVdcchMCnVQ2oMT8wihgPd4gcJLPDx3yYxCPyMijQOyTaJojWp19m8NhcvaXl_ShcqZcPAHfZL9LM0xdNsP_SQJtchNbV_SHEpBaeuRa4myPc_ugZCt_A8iVfu9q4KLcLM6BV3ALs9VVNAMetltvlaBw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
دادگاه محاکمه اندروتیت اعلام کرد ماشین های بوگاتی و استون مارتین اندروتیت اجاره ای هستن(یعنی مال خودش نبودن)
اندروتیت یه مدت بخاطر ویدیوهای انگیزشی و سیگما طور که میداد بیرون؛ حسابی معروف شده بود.
@News_Hut</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/70636" target="_blank">📅 22:31 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70635">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DAQviSqGnQ-NNeqKsoJ3LnOP4lc7K91NboCe_8qmTd3ddM7if1Ya48SzI03tNfZZE2Pj7qI7t2fzvxcE2bIU0du38UM8pajsFJ7VPKucRVTBtERTHpQiGiGXA7ZwkAjUCyzVbrTUWv40IxjVt_Xa2Y5TutZGt3R_8WIixVpzIIOYxzfCG99SKSxys1WafRG2Z2PlOESsGPrzHymknpjus3JFD6w0a8Unjof1z1II09QznYgqClkKl6Kjh4RmG0kJuiEI0-4SuLzgVxII3VAD3ec9aaSp-tfSdEcaGgsXqMbX_iVPj_YsiMzFzvUhyxbZXflGtMlW9FNRLtj1gRn7Xw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
قالیباف:
ما از بیانیه اولیه چین حمایت می‌کنیم که تحریم های غیرقانونی علیه ما رو رد کردن
مشارکت استراتژیک ایران و چین بر پایه احترامه و سازندگی و یک دیدگاه چند قطبی استوار وجود داره
این رابطه نیاز به تایید هیچکس نداره
@News_Hut</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/70635" target="_blank">📅 22:09 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70634">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/66110614c2.mp4?token=Z8cV6Rzzfu1iNbWylALE8GdCqN9gKEMsyX9mKpm-ALFOXHyIG9d5c8xNKkBG7Q-8FiouXQXxj5Ho7byLJseIHehp7JRyx6aLh7-yRJLEYnsl5hlmytFKFmL9Z8XTW59C4lAGlHXd2kAm8h5J2AkngC6MV698r3T9wkCFsPDORnFy2w4KTlyrMOZbqxvJ17buMHI_XrK0UmdaEIs9tGhcr9tTqJz_7xNRC3lqRiwvvR6cJwDCtIk2A715BIjLdQpFHJvR7wsUg_RRvJTVhJP2paNgUxWSpoyMGt1x91h1bgnKDBdK0MI8Z8fdRENF5_PntoXHm4O2DcfvzoOawb0b6g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/66110614c2.mp4?token=Z8cV6Rzzfu1iNbWylALE8GdCqN9gKEMsyX9mKpm-ALFOXHyIG9d5c8xNKkBG7Q-8FiouXQXxj5Ho7byLJseIHehp7JRyx6aLh7-yRJLEYnsl5hlmytFKFmL9Z8XTW59C4lAGlHXd2kAm8h5J2AkngC6MV698r3T9wkCFsPDORnFy2w4KTlyrMOZbqxvJ17buMHI_XrK0UmdaEIs9tGhcr9tTqJz_7xNRC3lqRiwvvR6cJwDCtIk2A715BIjLdQpFHJvR7wsUg_RRvJTVhJP2paNgUxWSpoyMGt1x91h1bgnKDBdK0MI8Z8fdRENF5_PntoXHm4O2DcfvzoOawb0b6g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تو‌ ارومیه یه پسره واسه دوست دخترش یه لندکوروز سری 300 که قیمتش بیش از 70 میلیارد تومن هست رو خرید تا سوپرایزش کنه.
تازه، زیرش میدونین چی نوشت؟
ایشون نوشتن، تقدیم به زیباترین دختر ارومیه...
@News_Hut</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/70634" target="_blank">📅 21:30 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70633">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bBCacIYB0CSJSNSPNNUsw8P727RUDMTurqVMRBmRbHOel0O-8gWn5HXLzXZ-6q0HmVQhNjkoi3uX_0n7A2P-5fEyMHg26NcPiJKM1s1mox6y33912GKq1BjppU_XjT55kX-KI4ORLHxFhzs96J_pmiD_yKWccjb5tAGYNiVcothL_cu7HgGTmWD9woNYJV4kxwg-ZuUySXwV2zTrKj3co5pzfkCP5lpYbVWbCKuA5IeFM3O6VbxsEXMiQpDqJOqOZ3p-bsOu194ChMKtDbN9GWSD2VZ_FtpUttSJnN-lRXgkykY_Ji4y1EdU5fbYy8c3PHJ1hzY_1y8IexQdeZn8Hw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
فارس:ایست بزرگ مقابل کشتی هندی در تنگهٔ هرمز
یک نفتکش هندی به نام «HAANA» لحظاتی پیش قصد داشت تا از مسیر جنوبی تنگهٔ هرمز موسوم به کریدور عمان عبور کند اما با هشدار داده شده از این کار منصرف شد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/70633" target="_blank">📅 20:54 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70632">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tt0ah793Hv00tELiIyE58vK35b5UoCkrzIBco5ezyAzHgwEo685Hvk9EPcIa9ujfqAxkVnxemNwQsK_j4z38GeKuYEFH33PqK7d_29OEWxAX0azLRwWVOOm_wQcF-rh_1ZYsXuek3tehwg2Wb44rsWUCZjqr4KblcH2POD4PB9rgUcu4zgklClArpqTN1qHzHllvaEm8ud6u_ucSMMAthJo3ie8emwGVWqMNb8bId9v5Vr3w61y4j0MOBmxwjTo1xIOcCKuOGPTJQFP-xjLO6qdv68oXhDjPI9qft_Nby1CvA2p-G2K0QNVk0oScIZZJ8atnPlmXcodLAWZaQOr_bg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
پست ترامپ در تروث سوشال
@News_Hut</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/70632" target="_blank">📅 20:12 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70631">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">ℹ️
صحبتای امیرمحمدزند بازیگر صداوسیما:
حرفم با مسئولین اون وره چون این ور اگه حرف بزنیم احضار میکنن و تعهد میگیرن اخرشم‌ممنوع الکار میشی
قبلا حدقل زنگ میزدن میگفتن ممنوع الکار شدی ولی الان زنگ هم نمیزنن خودت باید بفهمی جلوی نون تورو گرفتن
ما ایرانیا با دلار ۲۰۰ تومنی و طلای بیست چند میلیونی و مرغ و گوشت و .... خیلی مردم شاکری بودیم
هرچقدر هم اقتصاد بد باشه گرونی باشه جنگ باشه میگن باز شکر کن سالمی حدقل
بعد که مریض میشی میری بیمارستان با هزینه هنگفت میگن شکر کن حداقل زنده ای
طرف میمیره بهش میگیم خدارو شکر بابا مرد و راحت شد
ما ملت ایران انقدر شاکریم خدایا یه امتیاز ویژه برامون قائل شو
@News_Hut</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/70631" target="_blank">📅 19:31 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70630">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🇮🇷
مهاجرانی سخنگوی دولت: در میدان ولی‌عصر یک خانمی به من گفت الهی بمیری!
رسایی سرباز نظام نیست؛ ظریف سرباز نظام است
رسایی منافع ملی کشور را نمی‌فهمد!
جریان پایداری خلاف منافع ملی حرکت می‌کند.
@News_Hut</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/news_hut/70630" target="_blank">📅 19:01 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70629">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/90d9d9f6e5.mp4?token=Yclf_Be53fjwZh5hl8MsFzKP-UERnTwPgQQhNb7l7BMPVZndzfBqdgSnxHPuAGu06L58zzcJ-fqAaHOT8ZIW_IreX-uJS2CY-upexXxmUvbWXVMOcdCsglmbvKY3h8BF6SH-94sN4q8bmcCBhVZC2rt_vt1t9_4jGQISYG5ZTLpYzm-w6Oucv-Zf2dDU0UPKL73wKjtk06r629CA1d_AtPRflNgEI6TBHt_Lmx9fibGm2paXP1ESpRAWoB8q3Q6aJx3jIgzctVeoUZ7tQntHeBez8MqUkm7DAVbSjgZL2KmLN_HFgd2iRzZgONt17e5xC3TTZqb_m_wGEIlw5htqpQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/90d9d9f6e5.mp4?token=Yclf_Be53fjwZh5hl8MsFzKP-UERnTwPgQQhNb7l7BMPVZndzfBqdgSnxHPuAGu06L58zzcJ-fqAaHOT8ZIW_IreX-uJS2CY-upexXxmUvbWXVMOcdCsglmbvKY3h8BF6SH-94sN4q8bmcCBhVZC2rt_vt1t9_4jGQISYG5ZTLpYzm-w6Oucv-Zf2dDU0UPKL73wKjtk06r629CA1d_AtPRflNgEI6TBHt_Lmx9fibGm2paXP1ESpRAWoB8q3Q6aJx3jIgzctVeoUZ7tQntHeBez8MqUkm7DAVbSjgZL2KmLN_HFgd2iRzZgONt17e5xC3TTZqb_m_wGEIlw5htqpQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
صحبتای این دختر در مورد اینکه تو این جامعه، سخت‌ترین کار پسر بودنه، به سرعت در حال وایرال شدنه.
@News_Hut</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/news_hut/70629" target="_blank">📅 19:00 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70628">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">بازی شکار مرغ این روزا خیلی پرطرفدار
😍
توم میتونی بازی کنی و پولت چند برابر کنی
👌
از دستش نده
✅
https://t.me/+x83BW_KQnT01ZGE0</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/news_hut/70628" target="_blank">📅 18:59 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70627">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7abc39cb8f.mp4?token=DfckMzLFX1XLoGa6vsJzCbG0_mTnPkCkpuXKsV2MncqdRp4u2qIltTuXVBDNnnXsLHjq92Gtif8XfVfO8PXkZTSKF6o1iQ-d5YYofopv5vtf3pRNGFaUM3XoAskJv_C8eGzyzSDD0WsFOknGUgeKTLiih0jNgVihGWKm4V4U8UVyxKi3NoX9ojA0CGYuimQL2MtroF9JhyN6F4Qrl3D0Zsbs3dAwdT-PgaJRbFYn7AmkXVaXLewMHbwvi3zZUjbn_3GPFNMH8KqCPbTyW0qLOl8-CyeIoRbAIwPwlw67tneZkZfEOrU3BZbu7HmDnPoM6jQebRr4cQUhs7a-V5pSj0mtszEQbydscH62gjpkOjzGREkXK39RYfJ9U8uiTn-DKCPZbVY7OZR03qq4XbLYocERqmm_0W1TPnYymXhRVsH-ZMP7xf8CA4eqGmQ7Oua_oL-hJvAiDQcZi7TE-eKtoQZQwfGX4y300kacDMC1p4tlQ6ZV0nxTCRCoirumLGt5NjL1_-vgqHnAqr0VgewD1t7u7yUm1XVfgjd2BYn8xFT-vNcl1H1pHqG2ElxiOjdiIX7kpLRZvMS1hyN7-R3WMstDgTwsbcJl8b1l4qfmPh84YZy4fjJMSt5JWZVSVtjLR3XIbfVN_-hF8SJN6Lozq306aerXZFIh1A1T30zE6lw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7abc39cb8f.mp4?token=DfckMzLFX1XLoGa6vsJzCbG0_mTnPkCkpuXKsV2MncqdRp4u2qIltTuXVBDNnnXsLHjq92Gtif8XfVfO8PXkZTSKF6o1iQ-d5YYofopv5vtf3pRNGFaUM3XoAskJv_C8eGzyzSDD0WsFOknGUgeKTLiih0jNgVihGWKm4V4U8UVyxKi3NoX9ojA0CGYuimQL2MtroF9JhyN6F4Qrl3D0Zsbs3dAwdT-PgaJRbFYn7AmkXVaXLewMHbwvi3zZUjbn_3GPFNMH8KqCPbTyW0qLOl8-CyeIoRbAIwPwlw67tneZkZfEOrU3BZbu7HmDnPoM6jQebRr4cQUhs7a-V5pSj0mtszEQbydscH62gjpkOjzGREkXK39RYfJ9U8uiTn-DKCPZbVY7OZR03qq4XbLYocERqmm_0W1TPnYymXhRVsH-ZMP7xf8CA4eqGmQ7Oua_oL-hJvAiDQcZi7TE-eKtoQZQwfGX4y300kacDMC1p4tlQ6ZV0nxTCRCoirumLGt5NjL1_-vgqHnAqr0VgewD1t7u7yUm1XVfgjd2BYn8xFT-vNcl1H1pHqG2ElxiOjdiIX7kpLRZvMS1hyN7-R3WMstDgTwsbcJl8b1l4qfmPh84YZy4fjJMSt5JWZVSVtjLR3XIbfVN_-hF8SJN6Lozq306aerXZFIh1A1T30zE6lw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙋
ویدئو بازی پرطرفدار Chicken shot
🙋
فقط کافیه شکارچی خوبی باشی و مرغ هارو شکار کنی و پولت چند برابر کنی
😍
💵
💖
توی سایت بت اینجا بازی کن و پیش بینی کن و پول در بیار
😍
⬅️
امکان شارژ با کارت بانکی راحت و امن
⬅️
تسویه حساب سریع بدون احراز
🎁
هربار شارژ کنی 12% بیشتر شارژ میشی
✅
🎁
اگ باختی هم 10% باختت سایت بهت برگشت میده
✅
🚨
ادرس ورود به سایت:
💠
http://betinja.bet/affiliates/?btag=2760677
💖
فیلترشکن خود را روشن کنید و روی کشور مناسب قرار دهید مانند المان،کانادا،امریکا،ترکیه،سنگاپور،فنلاند و...
g4
⭐
کانال اطلاع رسانی سایت:
👇
💠
https://t.me/+x83BW_KQnT01ZGE0</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/news_hut/70627" target="_blank">📅 18:59 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70622">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c1a8b5c63c.mp4?token=GrSjJj0E1gDB9YDJKAD8Mo7xEQsOnQkbIrjKGe16E2BX1xSQzb69-31asohfg0jfpsb4h83ILbyWD4gnBy51TAjIggbYvBdgINyGAjYlyUIYY1hjrwYfJx6Jpu6b8rqdoopy3Xincm0jUoCeYAe4VElXBTjkHz6TVqefLKuOfQ10Aeki2-no4WfU3btMVwDn-YPqkL5UvFQ7tOgqzfXN-fSdxxKhuULfd3X8eylELdcc0hy0wNTEMvWC7F-d0Rhq6EdA4tHq_2QNkE8BwnYA6snRDJfwyvWjlT5lArVrEMvx2ykJFnBIF5dIsVi_ciVsY5n8WrQgpdF2ppQ-sAUIuaVeoveCiECJjJVU-qXDQgnIdu50zxQYAR-NSUd_VUI1wQOlUMCnNZiWAo3FZndpsCF55VHkp2itzRLaUgjaKLQ-wmacBTtwAWSlu_wSPfNkpkv9U7DGngSMJs1l-8tnF5dItBS1ZYhhORJNZ-EC8tidKDZE_GRY30FwUqr9fvBa8l8fqJbF45azzPT8FLKL3Vp38BVQjRWtH5JEpRsKnmLuzhwkx5M5ObFOpE9EoJH8coQNhzZb2sTHm54pKCtbydthrrmbT7k6Qc0t_iV2ZecUkx9o-u1IuPtZg0STzsp3cqI5D4LAfhxh7t7u-7iJ4siY7ksYI53dK7RT-Cca6s0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c1a8b5c63c.mp4?token=GrSjJj0E1gDB9YDJKAD8Mo7xEQsOnQkbIrjKGe16E2BX1xSQzb69-31asohfg0jfpsb4h83ILbyWD4gnBy51TAjIggbYvBdgINyGAjYlyUIYY1hjrwYfJx6Jpu6b8rqdoopy3Xincm0jUoCeYAe4VElXBTjkHz6TVqefLKuOfQ10Aeki2-no4WfU3btMVwDn-YPqkL5UvFQ7tOgqzfXN-fSdxxKhuULfd3X8eylELdcc0hy0wNTEMvWC7F-d0Rhq6EdA4tHq_2QNkE8BwnYA6snRDJfwyvWjlT5lArVrEMvx2ykJFnBIF5dIsVi_ciVsY5n8WrQgpdF2ppQ-sAUIuaVeoveCiECJjJVU-qXDQgnIdu50zxQYAR-NSUd_VUI1wQOlUMCnNZiWAo3FZndpsCF55VHkp2itzRLaUgjaKLQ-wmacBTtwAWSlu_wSPfNkpkv9U7DGngSMJs1l-8tnF5dItBS1ZYhhORJNZ-EC8tidKDZE_GRY30FwUqr9fvBa8l8fqJbF45azzPT8FLKL3Vp38BVQjRWtH5JEpRsKnmLuzhwkx5M5ObFOpE9EoJH8coQNhzZb2sTHm54pKCtbydthrrmbT7k6Qc0t_iV2ZecUkx9o-u1IuPtZg0STzsp3cqI5D4LAfhxh7t7u-7iJ4siY7ksYI53dK7RT-Cca6s0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇳🇵
🇨🇳
وقوع یک سیل ناگهانی و شدید در منطقه مرزی میان نپال و منطقه تبتِ چین، خسارات سنگینی به بار آورد.
گزارش‌ها حاکی از آن است که در پی این فاجعه، تاکنون صدها نفر از غیرنظامیان و نیروهای نظامی و پلیس مفقود شده‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/news_hut/70622" target="_blank">📅 18:14 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70621">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🚨
🇺🇸
ترامپ:
فکر می‌کنم ۳۰۰ [درصد] باشد. شنیده بودم ۹۰ درصد؛ اما به نظرم تورم ۳۰۰ درصد است.
@News_Hut</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/news_hut/70621" target="_blank">📅 17:16 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70620">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/07afc966eb.mp4?token=BEiIrI49cTZSz2vLzmbZU7psBtltXzB1_oUJ1vHux5YQUTy3aRRC09tX8cx9N2FheIsJo4Ir67fI7b3bv_Eb9O1fghaLJxDlP34qXmk6tQdVe0cT2n4DUWXjq_LARfcKGOqEiTRPZZcBmRm8AKrR0vSFxMjgqUOIv3GocJ6dBugBF7m3Bz91BcdgVDTcXI6Bds3DAySLZwGl_kXuVOCJQQhQsCOGNY-CEDtqltSP-M2NX5wHq6nizfZrQAYYJS1qRFsLiA_zYRT4Q_uv2Bu2yeQPvkN2431LL2LvdqmCIC3L_Oq2V9v2VQAiaSI8zyQnAArIE7N9fASYAchIzGCutQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/07afc966eb.mp4?token=BEiIrI49cTZSz2vLzmbZU7psBtltXzB1_oUJ1vHux5YQUTy3aRRC09tX8cx9N2FheIsJo4Ir67fI7b3bv_Eb9O1fghaLJxDlP34qXmk6tQdVe0cT2n4DUWXjq_LARfcKGOqEiTRPZZcBmRm8AKrR0vSFxMjgqUOIv3GocJ6dBugBF7m3Bz91BcdgVDTcXI6Bds3DAySLZwGl_kXuVOCJQQhQsCOGNY-CEDtqltSP-M2NX5wHq6nizfZrQAYYJS1qRFsLiA_zYRT4Q_uv2Bu2yeQPvkN2431LL2LvdqmCIC3L_Oq2V9v2VQAiaSI8zyQnAArIE7N9fASYAchIzGCutQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
ترامپ درباره ایران:
وقتی کسانی هستند که حاضرند شما را بکشند، اعتراض کردن در ایران بسیار دشوار است؛ به همین دلیل است که آن‌ها اعتراض نمی‌کنند.
و البته احتمالی هم وجود دارد، چرا که آن‌ها بسیار تضعیف شده‌اند... به بسیاری از سربازانشان حقوق پرداخت نمی‌شود.
@News_Hut</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/news_hut/70620" target="_blank">📅 17:14 · 04 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
