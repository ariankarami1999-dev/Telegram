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
<img src="https://cdn5.telesco.pe/file/eweV_Z2jjHsC5rSKawF16m150WJl9x66cOShk79XSUttpKOtgwAutl1ZP_IaHKFvOpIyYCcod0xSeuBGpVWtZeLdQNfD29WfMIVWMF5EHTvbeXQ_t5CowmmJK7GzYcxAdM8AT2MLUHxVnbjYumPkkInto33zw3IqBSzR9Uxjd_sHPOFywqWjTwBL1MBoHBsGFwgIIs01VEqczDD8ZepMI9YUjtJmtZLHrgpjONr5GJsAgajdZy5_AaltA-JTFiCQq33MEMCYMRE9izVN01IkQjksztq-Z0-c1hAwyLcay1pm-vD8x6H_xLrOta6dncYswGfUYhZnchKYKz2PRiwQ_g.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فوتبال 180</h1>
<p>@Futball180TV • 👥 438K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-07 19:12:14</div>
<hr>

<div class="tg-post" id="msg-105024">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RLt9wMOPagSMLkDuRvuZY0s_3deTyCAeIhCyIusxBL-1gp62jJPUa7rmuZXTyWCvcWJoAsD-JPaIp2znQ0ELpOkxxJ4Uf-4q8FGhPhkqxvZB6tBSeZ-ns9sg9IrDAVZkqo084PlhFnkVM0QwOWXkr6vMdmRzJwrc9bE8TcL2A-u_ozlsQz4q6HB5ow1ki6GVmYujGUI8HWwGUeOLsnagh7LyZxZ6VO4t6FPo0WFuMDCx8X2YYBfcJVI5Neod6T9OxC3g6Of0FCCpqtxULUWCmotbJ2LahTXVG9fltRg0Aoh4AmCiU6hiAIl5cBvfi73HP26Z06eC-TSgRLNcZXZd2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🗞
رومانو: فرانک‌کسیه از الاهلی عربستان به آتلانتا ایتالیا؛ HERE WE GO
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 1.17K · <a href="https://t.me/Futball180TV/105024" target="_blank">📅 19:09 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105022">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mwGyr70B2pGygHnWKGaelrbkbSpwHSjqumoCrdueARBPEMrgLT1V4rJUfdVuBSsCcT2sfKIgcannzCkU7xTcqitkBtRYmvxVdf2VwJFeZaF-D3Xi3jm-U3EhZEFHaf9jikw-V7gKogrJ6GdZqVztSFkC7JZotubappyrisjAWaehsc45BmvcrcMfiTlaGdJ7Ehoo3kwM9cXaVwjx1_J1IaVRgASU5IzRSZ96nbT8aK5eF40ZIRo6cOtuWM09-AqAxl19zPLNWT4BCRqMliwPjEj4C9PY4_p1qiiPXvCK6J12wAsJFlIUWHgvoDvaVcPux9nVh11oNeXq2GzlwnmeiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ApTd5PtmPWM-oPlDP9QFoEQa1ejPReCMpkuFRWIjbbe-28UCcGzFaugYemxHVJ7UjkZAeV5n4ml0L8SSRrm7gUh2N73QBBWB-BoVRjrzjd8loN9F1o1IkK7NV6kmE5DTuEbryPwJn5CZRdMKg5dsWrnu04wN2oytq4BrRbMquaOxE5o7nJfqFyU8w-MYQNFghznxDSNwl2KoxlFiVoac8wRa2ZvjNubsjUdNQhuyKfhRCU4fv6T38jUUafsMtlwf4KhAHjBk2TlE7chVr2hEet_JNcheCMBial6ijBFuJp4shqyNj00y95qdxEdJdfHHoPvVSvlp4wBU7fzOdUAfxA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🏟️
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🏴󠁧󠁢󠁥󠁮󠁧󠁿
ترکیب تاتنهام و نیوکاسل
ساعت 20
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 1.78K · <a href="https://t.me/Futball180TV/105022" target="_blank">📅 19:05 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105021">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c974ddb250.mp4?token=TFhy9285heot1sNj8BKxWOSOW4KZDKBxmWrHNqcH57I9wCKQY4-eXXZB2BQQtXtwsJfLuib1Kt3v-UxN3dyVnTwp2dyaeEFKcM9ANaOB-D8D427xrh6e_l2NV3Ktq33-zbbdTa9Th7IdrOv_ZGCQ5Zt7nMaUywL9EHQMGTQlG-4z6rMgDsGqQwyGvMzjDhf1HRID0k0We0uxIejgpjQmyGHsodiId-n0YZ_eGJa2Hfvt6RwiVViDdy24NpBH-f4C0M4XgnlEsvnpLsrOlIyqlwlCnHCNkhGzbrQoWCHOqJ4819RJxmMBXN8QkfRwBJkEYhdpG5IV52Jig0-n10-0wTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c974ddb250.mp4?token=TFhy9285heot1sNj8BKxWOSOW4KZDKBxmWrHNqcH57I9wCKQY4-eXXZB2BQQtXtwsJfLuib1Kt3v-UxN3dyVnTwp2dyaeEFKcM9ANaOB-D8D427xrh6e_l2NV3Ktq33-zbbdTa9Th7IdrOv_ZGCQ5Zt7nMaUywL9EHQMGTQlG-4z6rMgDsGqQwyGvMzjDhf1HRID0k0We0uxIejgpjQmyGHsodiId-n0YZ_eGJa2Hfvt6RwiVViDdy24NpBH-f4C0M4XgnlEsvnpLsrOlIyqlwlCnHCNkhGzbrQoWCHOqJ4819RJxmMBXN8QkfRwBJkEYhdpG5IV52Jig0-n10-0wTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هیجان فوتبال رو با لیگ ایرانسل چند برابر کن و با پیش‌بینی نتایج، امتیازت رو ببر بالا!
✨
🎁
هرچی پیش‌بینیت دقیق‌تر باشه، شانست برای بردن جوایز جذاب مثل موتور، اسکوتر، پلی‌استیشن ۵ و... بیشتر میشه.
همین الان به سوپراپلیکیشن ایرانسل‌من سر بزن و اولین پیش‌بینیت رو ثبت کن:
ثبت پیش‌بینی</div>
<div class="tg-footer">👁️ 1.66K · <a href="https://t.me/Futball180TV/105021" target="_blank">📅 19:05 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105020">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/Futball180TV/105020" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 1.5K · <a href="https://t.me/Futball180TV/105020" target="_blank">📅 19:05 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105019">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VkGSo10JRsbraAPNxh8x6wF0IWG_WzuwpdOvxW0IVIeyxy17-VaSAcLgVyz07nOFlIbyTktn8KH9TpI7dqqclGlwXPtRc7GOJsPPFHumVFk1QNBdS5tEUQ2Fcn7R1Ez4hlc_D0ynSU8vM5UM0g89daWY3mQfMsJXgg3EsgC8u9wBL28yw_z8SIwoztfTKBz8qQ7-Z28flXMIW5A9m8D0SNAzUohvYoXvRVKaMgMWfIuommx_IhinCdMl7867Vj5DbVg6r5c1hSGqevqPR_hhvCWtbxk6oyGtSgzzqWUF2YnMK_ZPgJkJOKpYvIkyq_FqgB-UOHhU9DSehitDHG-JVA.jpg" alt="photo" loading="lazy"/></div>
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
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 1.56K · <a href="https://t.me/Futball180TV/105019" target="_blank">📅 19:05 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105018">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Foizx_uz21xjiEbpFvqJCm5mO8J1IVpvFkJ9NE4JkUAqxWAuONzUnztkrQ9SOCK87KRCXQchlHVxAw4mqLz4DDD1CHP5dcTJokv7y03b5bWlIpvi6BsavCMeQkR5CAfUfyfRfIISMvhoPzLwobzW77lyRxrh3pmVXTB9foI5ZJmw-c23lpv3MTBr1Itezzx4i85nSl-PmLG_OWidgPfv4QcyFXeaEPIsCskgpzXEmjLyUjyiLqM7oXclYyYmgIgT6fauHZ6NL563GP0jCeNdX4asaSw9HvES0krJnoodePco3gCIOMbxfgE7aHAUcJbfpMWRuEuahOiMEQURS3CVsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇮🇷
ترکیب پرسپولیس مقابل ملوان
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.75K · <a href="https://t.me/Futball180TV/105018" target="_blank">📅 18:19 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105017">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DoiKPn3e9CJhMzdsewLwQOtPtFGYU2P25nStfrN4cvKGb8-QPMiFmEkEfzxe_nfuw5uVpd2DRmt3gAALTU80mDqtmLBbItP6TBfIF1zchzBfhPvidBqH0lrntITnkmgShuCs_z8AocrPMbmeykUymhUlsb7fy81b9MO_YK440ABuOdZKfS3pKcLk2rZzuJvMumEPvyBJF_x5dUGzxEsorV7dFvk3RNwTOYM-Dk_13MZNxaOn7MrO75XGhJP3gtnik6uc3v2CRqNigLdYcglCvI7Lrzhrhbfzdyp5ADIjoa9C9J-z6_INhL6qCH-2QIynB2FSoxLhXu-qc1d2EdtutA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇮🇷
ترکیب پرسپولیس مقابل ملوان
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.04K · <a href="https://t.me/Futball180TV/105017" target="_blank">📅 18:17 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105016">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🚨
🚨
🚨
‼️
🇮🇷
هوادار پرسپولیس: یک مربی مثل گل محمدی می خواهیم، نه تارتار ترسو!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.58K · <a href="https://t.me/Futball180TV/105016" target="_blank">📅 18:06 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105015">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c6f2734cd0.mp4?token=iIzRzzXuCgRKXM5gDm15n8i6LJlUut-YngDs5dTs09vUKjIk-WxtHGcOhFtZdc7RI6JzgA8bNlP8W4ShenoSCfh327-_S01IJXNTzsujjtA4OY_seq9HwWmLxYRuc5czOJDIqRRRgufeZhPNFXWHhaltAXlQ0paSB_wXcIXk2tCinROJvblMLsMWcP0S0jUr1wwjKQRF6I8Xotx7E3j6WxrIHEg3pY_wDBuTDnW0SMGVsaiqfNwwxXDTYGiVeihaXc07UKXkXRwiDwVRqblNg-Du-76QCmy1DyZ97aL-7UgCPpkKplZsMexjFDCcR7SaQ3viui-3MU-_5gGPjBJROA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c6f2734cd0.mp4?token=iIzRzzXuCgRKXM5gDm15n8i6LJlUut-YngDs5dTs09vUKjIk-WxtHGcOhFtZdc7RI6JzgA8bNlP8W4ShenoSCfh327-_S01IJXNTzsujjtA4OY_seq9HwWmLxYRuc5czOJDIqRRRgufeZhPNFXWHhaltAXlQ0paSB_wXcIXk2tCinROJvblMLsMWcP0S0jUr1wwjKQRF6I8Xotx7E3j6WxrIHEg3pY_wDBuTDnW0SMGVsaiqfNwwxXDTYGiVeihaXc07UKXkXRwiDwVRqblNg-Du-76QCmy1DyZ97aL-7UgCPpkKplZsMexjFDCcR7SaQ3viui-3MU-_5gGPjBJROA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
‼️
🇮🇷
تهدید مهدی‌تارتار توسط گروهی از هواداران پرسپولیس: دربی آخرین فرصت شماست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.49K · <a href="https://t.me/Futball180TV/105015" target="_blank">📅 17:53 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105014">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f68436a0cf.mp4?token=W8nczKUPta0AeauYQc-MLsNmLbR2w-3NNEE0cMe_HYvfCsv1QWIM7ZZngbHtEeqtC2IGd--Vz1zLfydOesu1-ShokFPSxJIGZPTDPGbuSWPw495gZutVoebU9v5d49LTUDV0HPKk9E4yyk-Ut-xV1wsqiu9ga0yTPGAO2VZP3T5C_WwTPgaW0_f02sJJwNflokhBykeNG2svYB-KCtumOi3HycreP6XObqODxlo56KfB9l7EKNhhCVTItuxAAaCvI7TiboPhMeEyFWw8wPSx5JvhmM-F87ab6y6CKi7PqDs_lc6y1XvMpjjZWchcihvDGONmxfjaY1DICGMb6jtgwg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f68436a0cf.mp4?token=W8nczKUPta0AeauYQc-MLsNmLbR2w-3NNEE0cMe_HYvfCsv1QWIM7ZZngbHtEeqtC2IGd--Vz1zLfydOesu1-ShokFPSxJIGZPTDPGbuSWPw495gZutVoebU9v5d49LTUDV0HPKk9E4yyk-Ut-xV1wsqiu9ga0yTPGAO2VZP3T5C_WwTPgaW0_f02sJJwNflokhBykeNG2svYB-KCtumOi3HycreP6XObqODxlo56KfB9l7EKNhhCVTItuxAAaCvI7TiboPhMeEyFWw8wPSx5JvhmM-F87ab6y6CKi7PqDs_lc6y1XvMpjjZWchcihvDGONmxfjaY1DICGMb6jtgwg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
‼️
ریدممممم حاجی اینجارو
😆
😆
😆
🇮🇷
نحوه ورود هوادار پرسپولیس به ورزشگاه!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.83K · <a href="https://t.me/Futball180TV/105014" target="_blank">📅 17:50 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105013">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/beb84b277b.mp4?token=C9dWpxYuThz2weth7FyX5CJXYdYrCgorv7lmwO6R8dqwzc_8xGjkyMmXHX2VwSOlgb9WJ40OmsZp8hLsJov6L73thRtD43ZQoi6iBo8xAPmJv8UXbDJ4aBvruPzIXynhEivs54aali-Ch_wHwxNg-GGHu3yAlThYAhqSSt85m7IHqPEHlPrV81vW_F--OEirI31-DJJvLaSdYPXEa5ByO2ZXhTv13PEp4XSvAuSqeXBwuECOvs7lNIExJ-IQiQR-dK9r7o_ow9mwcPxzR9MqAzddIt8Ndm41Worv_5OBe6ENr-t0947km78vIqcOpG3egVNwDxdWc0O6g5w1psFjsA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/beb84b277b.mp4?token=C9dWpxYuThz2weth7FyX5CJXYdYrCgorv7lmwO6R8dqwzc_8xGjkyMmXHX2VwSOlgb9WJ40OmsZp8hLsJov6L73thRtD43ZQoi6iBo8xAPmJv8UXbDJ4aBvruPzIXynhEivs54aali-Ch_wHwxNg-GGHu3yAlThYAhqSSt85m7IHqPEHlPrV81vW_F--OEirI31-DJJvLaSdYPXEa5ByO2ZXhTv13PEp4XSvAuSqeXBwuECOvs7lNIExJ-IQiQR-dK9r7o_ow9mwcPxzR9MqAzddIt8Ndm41Worv_5OBe6ENr-t0947km78vIqcOpG3egVNwDxdWc0O6g5w1psFjsA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
‼️
ریدممممم حاجی اینجارو
😆
😆
😆
🇮🇷
نحوه ورود هوادار پرسپولیس به ورزشگاه!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/Futball180TV/105013" target="_blank">📅 17:41 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105012">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c0d80d5d54.mp4?token=Fm9sbtaPRjWX0SkxJTyccq-PAxDFg2zFk1PlbePxo6s6e1drgt7YaZamZ0pAOSMyrqG9uBefcA1uiQr9jLLj3miXUhcPgt9IiOkn6tzqM9JvHwCaoKcqPYAw3OdMttosvOvGyraZNLiMsrMBrErnJgJwtPxaieexhwsDqBQ4ICYe-aLlFRYAIX7Lyxh2OaZxvXyMRiph3Nslm4yrkLibexWh47YnLkZsYwoZrZx7rNTMK_joJOtqVOY50t14F7znEJGRp3AujOaUR2u_LKGewUL98lM8gUsPvm00L43DafbVZbO4J3EyxVQerOD-82WU7FpySIf7XQrZ4bmftjXsQA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c0d80d5d54.mp4?token=Fm9sbtaPRjWX0SkxJTyccq-PAxDFg2zFk1PlbePxo6s6e1drgt7YaZamZ0pAOSMyrqG9uBefcA1uiQr9jLLj3miXUhcPgt9IiOkn6tzqM9JvHwCaoKcqPYAw3OdMttosvOvGyraZNLiMsrMBrErnJgJwtPxaieexhwsDqBQ4ICYe-aLlFRYAIX7Lyxh2OaZxvXyMRiph3Nslm4yrkLibexWh47YnLkZsYwoZrZx7rNTMK_joJOtqVOY50t14F7znEJGRp3AujOaUR2u_LKGewUL98lM8gUsPvm00L43DafbVZbO4J3EyxVQerOD-82WU7FpySIf7XQrZ4bmftjXsQA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😐
🔥
👀
پشماتون از ایونت تنیس تهران بریزه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/Futball180TV/105012" target="_blank">📅 17:20 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105011">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZY6KiJli8roiA_izAZPOhr7Xgjl7SC7GTfX2S0HZRHzIwo7bHfLbQcdtrWJmvHaKB9pxOP4Qf3dpLoQyV79REIPaF7VW16Q0H34TTZolEObE6cuZ69z9Pdqwq_Pn7SfqkPbC0keA7p-eIv2TH3luE1bcdkSybegWimxyDNm80kojiQtK4O0j8UNVebs4msb7x7E-8KqVroz-BA_OIiPLvRhKoZGZi-4KdeRVw3-7SvDuYWuBnlO4s4xOO59QRBNF71Yw7phfioFzGWItXf7qsB-Bp60W8wpWxhfnyrXU3popN_KvwS5f_tNQKSozY5ye4zU5mj9fPucIMy1e1rbw5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🗞
🇪🇸
رومانو: سرخیو مارتینز هافبک ۱۹ ساله از رسینگ سانتاندر به رئال‌مادرید؛ HERE WE GO
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/Futball180TV/105011" target="_blank">📅 17:09 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105010">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n03e6oHP-vXGyidJV-Ikk70AfsOzE7apB7c0iR9We2JEcjpk8FhIabi65aIvJqM6x-wWKLskVcgG3YBd1nAWbhGO--uxUAOoA7d0iPLK9beyGN8yE9a0QQXwfxbMFj-3nj7MsYo-l2QEAfjLkxFHK7clzJDVE3HRFlTA5CBSjcpjWCSbnKNvAh2m9n-P6xt0U1N61LC-eeWxhwkti00eRm-kmWNnC-zuHoOwafNNgZPt4ImplHg6smm_N2EoFWB17gOl73iZwqrqYvOOkQ325MITBu-9IoB7AEDAcbQWmzpssJr6xfuxWgvW3ZR9GwatdC1usN_8bQBPnS_ntDKbqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
هفته‌دوم لیگ‌برتر انگلیس؛ لک‌لک‌ها در قواره یک مدعی نشان نمی‌دهند! شاگردان ایرائولا به دومین تساوی خود دست یافتند!
🏴󠁧󠁢󠁥󠁮󠁧󠁿
لیورپول
😀
-
😀
ناتینگهام فارست
🏴󠁧󠁢󠁥󠁮󠁧󠁿
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/Futball180TV/105010" target="_blank">📅 17:07 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105009">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZqdsfDXmmfJQcWVHRaQBgbFc4YzZ6MYqBM1wae8ZzKcFmI24PPooKhfmMIcpvxfp4sar_nSpa0KuMzoMxIFhZ6DsRFJJmZdKKnMtr0lDuvPX6rGbhLW55xkwGhcqLK9nZNgn8D12Q7CORv30DdM2A8PL7NHzy2NFVFPe387GGdjjunD_NEzzXuLZQYBkSfyjAB7ZXpA-nqC8JmGVColN7inc6xfVUnHLejJ0PWAgg7zUhOon5q5boZHRz_k21BlJDn3oyl3KUFz6J3kytoASluMKr4i4vGvKSkfgRdYjWpscIqPF_8mp_bN-zoq3KoPUvxECmLFSFzoULn3lVE6tZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🏴󠁧󠁢󠁥󠁮󠁧󠁿
هفته‌دوم پریمیرلیگ؛ ترکیب لیورپول مقابل ناتینگهام؛ ساعت ۱۵ شبکه‌ورزش
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.64K · <a href="https://t.me/Futball180TV/105009" target="_blank">📅 16:58 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105007">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/C6l4vEbXLx0o-ThELuOoz8SPakjXCIc8pLgyd5UBX5YkILKoNrpFBP4Rvj-6Uk88A_eq8xMdBOw8-2G1Cq0l3U19MEFe0O3WVIBbMjnf7jrA9AbYNua64vO5l_1o_IfIMmExfGrtZhhCyebeN4kGyyFxqyAPGLrRk3C1EpRWMjJsXa4CJFh59Xhv-w2_j7YAA1oswS_JE-gFD3vq-kN6mx5TUWeNWI4FOSZTridyIb_ao-RMPydywu67P_xqG2VAzx1llg8Hb0f15hWXNya6uLgYYxrLjfoL_M1mzP1VyUqaBEPTp0ssVFqbAt7ku8D-WvjuT_i3DSuEoWDIXzvJ5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/A-0CZZVh7VAeJ4uFJzDEo6o2o9_c6JvgXG5RbX1md3SeMHf0ZTV5eCQ1FQjbWmR2J83FUsBT9uuzYsykdaHNlRSm0fq4o732Yp4LmDUGd1Lz8YIHl9MkfzsOPZPeVNuA5ENNRCo87tiVtBhnJZ-mdeXs7oPaAOELW7m9bmKnDo5FYk7FPk1RGaq7Wa44Xx1MBdVduOGL6huXPG4Bn9oYhcTIhKxvXJQAlUnZ9TSjc6CYmT9X72EBY7EC1xP8RacNDzFIJz-dqtF6cpiK3FjSNWQLzp39g_Q4fyrs_bnJdo76qzgkoTo_5zlfW0ASpi5NbUzRRpRr6UO2Mz7dx9e4eA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🇪🇺
برنامه گروهی بازی‌های لیگ قهرمانان اروپا 2026/27 مشخص شد.
18:45 اروپا = 20:15 ایران
21:00 اروپا = 22:30 ایران
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.17K · <a href="https://t.me/Futball180TV/105007" target="_blank">📅 16:56 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105006">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1e0ed52814.mp4?token=YgAcGSTNbvOvEPIrsgmRZmptxm1SseVUgtTmygvuzHhrYszxPBENhtA7f6tFmvbDd22N03c73x-ddVogmYVySCcgcbKQOc-g4R0lq_K6rAqEj9INvFyqKhAVwu-FCRjvE-PBuqsok8XhP8iyHZa6oWje9TSr1HaOzO3-EU4ozWmoXr56gsT39EEmDwXC4PrQVMGcUuXqhjh_IqcXZInQ_-b7fdmP-A0d63htWb8Qi5kGbslQhB5XRy4_z_6boNPv1J5bV1gj7rqRsjPtTYckxbJY8soHXGFsdWjFJAGPDiS2ZC1jBPZP2kRKfkOZ4x9XBD5eyfAS_mD1sU4sTp0VPA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1e0ed52814.mp4?token=YgAcGSTNbvOvEPIrsgmRZmptxm1SseVUgtTmygvuzHhrYszxPBENhtA7f6tFmvbDd22N03c73x-ddVogmYVySCcgcbKQOc-g4R0lq_K6rAqEj9INvFyqKhAVwu-FCRjvE-PBuqsok8XhP8iyHZa6oWje9TSr1HaOzO3-EU4ozWmoXr56gsT39EEmDwXC4PrQVMGcUuXqhjh_IqcXZInQ_-b7fdmP-A0d63htWb8Qi5kGbslQhB5XRy4_z_6boNPv1J5bV1gj7rqRsjPtTYckxbJY8soHXGFsdWjFJAGPDiS2ZC1jBPZP2kRKfkOZ4x9XBD5eyfAS_mD1sU4sTp0VPA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هانسی فلیک: ژاوی اسپارت شگفت‌زده‌ام کرده و برام سخته که بگم کی قراره توی دفاع چپ بازی کنه!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.26K · <a href="https://t.me/Futball180TV/105006" target="_blank">📅 16:55 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105005">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QL0MEPlHfWsvkJ0QZOIMrNORQynzLtTNpVzwuWakSHkCAiy9yFfBpoozYoIvHwWJwx6u0FapkHkJoJNetbgzADDeeSj7i9cIr46yYpGSKXiE3ZKRVihFgAcwfR1KGnWm97Qd-Wc5CGziNNEwK3g9w9fqQE9_H9jw4O-7a5IArYynRPdyvtP5qozNQDSkz7nC7ZT5wvXtK0FejwRmwdq8mZhkHFtb6puDn0RoO2cK1_A2OejyIgN6IBmlXfesYTyGmNeAUr9mNMMky7ucadaJ1IkvpNIX9MQPSaKgJWTOtY3ID4t5PRstkjQefzSv1MHztc0c50uRBq9-o4AjCq3qTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇪🇸
مقایسه بازی‌های بارسلونا و‌ رئال در اروپا؛ با ریکشن نشون بدید کدوم سخت‌تره!
🔥
بارسلونا             رئال‌مادرید
👍
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.75K · <a href="https://t.me/Futball180TV/105005" target="_blank">📅 16:33 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105004">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/609a9de2f6.mp4?token=GswB24B5-1aG4GjuEQE3DORalWJD0oB5GkEBd_Al2g9aO2Qx_e-1_K6pJJ-pJRlqr-q-0UMvZELDMCY_nNJnoHjcDhujRaS4HJBysRuDcbDh9H46fyXYbub78bxRmJz9zEHv9GAgtzs3syveglvSPFJ-wWzsbtKzBiOo854bm6rCuVRXrGZN_6nN2FnhQFPrgTWaaUwS9hTYqj14q2MGcBNGJpNjmL_1uWzOsm2gPdSb5CsBz3Hc8veaFlfNgM3bmdrsMnGZfnIvZHDESGWFu5qmLFY5chxoNRcjDzdENN9NTFyLtR-8Q2zMoRIcqAtU5JUJYb26eBiLzFNx5JZCBw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/609a9de2f6.mp4?token=GswB24B5-1aG4GjuEQE3DORalWJD0oB5GkEBd_Al2g9aO2Qx_e-1_K6pJJ-pJRlqr-q-0UMvZELDMCY_nNJnoHjcDhujRaS4HJBysRuDcbDh9H46fyXYbub78bxRmJz9zEHv9GAgtzs3syveglvSPFJ-wWzsbtKzBiOo854bm6rCuVRXrGZN_6nN2FnhQFPrgTWaaUwS9hTYqj14q2MGcBNGJpNjmL_1uWzOsm2gPdSb5CsBz3Hc8veaFlfNgM3bmdrsMnGZfnIvZHDESGWFu5qmLFY5chxoNRcjDzdENN9NTFyLtR-8Q2zMoRIcqAtU5JUJYb26eBiLzFNx5JZCBw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🥶
برخی از نجات دروازه‌های فوق‌العاده بازیکنان
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/Futball180TV/105004" target="_blank">📅 16:05 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105003">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5be1dc5a15.mp4?token=kr_CESkS2poO6tqgDsrpc7E3ZbYOL5_vK_vMDhCmNwjjHu742i9WPndcoman_dWsloWpo8pU2hq_dsFQ-gM9CdoRcJvfwtpS5tnTJR1fk96k0Ij6GPmup95lsXcjEQINYycsCPAztpn03DcWMUNrHiq3wygHvKnPztiJYMDTb2GE1ZjEG21zGntAFgXCZQwFqXcagMCpr5BjJtn6g9ZB-ea3oel-OpNnbInGu4SIkgIomiK9eaUjxppp4Ni2Ycp5ndpEmjUqhn71022PzBIZlKlqHMUoqCUDGwdrNHyvuhHHozw53qAQKhziK9CN0sp8-CTGdPTgIzpnP1jcwngeGQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5be1dc5a15.mp4?token=kr_CESkS2poO6tqgDsrpc7E3ZbYOL5_vK_vMDhCmNwjjHu742i9WPndcoman_dWsloWpo8pU2hq_dsFQ-gM9CdoRcJvfwtpS5tnTJR1fk96k0Ij6GPmup95lsXcjEQINYycsCPAztpn03DcWMUNrHiq3wygHvKnPztiJYMDTb2GE1ZjEG21zGntAFgXCZQwFqXcagMCpr5BjJtn6g9ZB-ea3oel-OpNnbInGu4SIkgIomiK9eaUjxppp4Ni2Ycp5ndpEmjUqhn71022PzBIZlKlqHMUoqCUDGwdrNHyvuhHHozw53qAQKhziK9CN0sp8-CTGdPTgIzpnP1jcwngeGQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
🎙
پشت پرده خداحافظی خیابانی با صداوسیما
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/Futball180TV/105003" target="_blank">📅 15:40 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105002">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/96846109dc.mp4?token=sL1DbcVZKRHVpR6hfCDlrmeTgM4qbUGRyaAxN1J2Fst9Iq-bpL-HBEd0x1iRiQg8izX-x7_FDV8ptEn8lzeuzuBaCypE5LFQvOGBMIfbwc1CjVeKDvE899w-DK3_k8eMJhfqBLyPAgkgYpBZDK8618ThNcYwXKDXn67bZU9JHDay1lmIr8LiqCQsOO70GGKrNKoecAMpL8kETLj0xz1KUr91QQWpf3ZClsHapfzgRSpOCElKDIE5okAvkimzlHw61l8KZZlUd1wuMd5vYnfA2pk9eNPNnG_X3kF7paIlslWpriq07kue8bzAJ_zHe5BHH5qe-UOi9GvE4I2XZ4t85g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/96846109dc.mp4?token=sL1DbcVZKRHVpR6hfCDlrmeTgM4qbUGRyaAxN1J2Fst9Iq-bpL-HBEd0x1iRiQg8izX-x7_FDV8ptEn8lzeuzuBaCypE5LFQvOGBMIfbwc1CjVeKDvE899w-DK3_k8eMJhfqBLyPAgkgYpBZDK8618ThNcYwXKDXn67bZU9JHDay1lmIr8LiqCQsOO70GGKrNKoecAMpL8kETLj0xz1KUr91QQWpf3ZClsHapfzgRSpOCElKDIE5okAvkimzlHw61l8KZZlUd1wuMd5vYnfA2pk9eNPNnG_X3kF7paIlslWpriq07kue8bzAJ_zHe5BHH5qe-UOi9GvE4I2XZ4t85g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
✅
مرد سه‌هزار چهره با حضور مهران مدیری از روز جمعه ۱۳ شهریور هر هفته پخش میشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/Futball180TV/105002" target="_blank">📅 15:15 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105001">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/568c088f46.mp4?token=C2fgmR8PvLfT9WCLECDxG4yLWkGMVr5whvHwgvRACjX3VWhvGxX2hKwVt7RnDKojKxcroyZIOBNpGakxd9oR1xgYgD0wGIRLgjRqGReWgtdacNbU2JrBJtNF3ds0eCj3RnUf1K0dEzGAxuUSzqwq8TUeRIIOdxWGCFbV6hna7Cz51NP5Y6410EICthorEW1IEUyo2wluDnPrEInjGK2hkGBdXO6Q7wAuCuns_dyOmcdeJC1LwPVIvw3ofoh7rr-34WTuCWLsCzgxYzHBqj_lYVFM-cpO9dvDfon2iOznZWunPdOyTVSfg-JJUkF6SITd3potChOkLWJ6rup_SE3hNg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/568c088f46.mp4?token=C2fgmR8PvLfT9WCLECDxG4yLWkGMVr5whvHwgvRACjX3VWhvGxX2hKwVt7RnDKojKxcroyZIOBNpGakxd9oR1xgYgD0wGIRLgjRqGReWgtdacNbU2JrBJtNF3ds0eCj3RnUf1K0dEzGAxuUSzqwq8TUeRIIOdxWGCFbV6hna7Cz51NP5Y6410EICthorEW1IEUyo2wluDnPrEInjGK2hkGBdXO6Q7wAuCuns_dyOmcdeJC1LwPVIvw3ofoh7rr-34WTuCWLsCzgxYzHBqj_lYVFM-cpO9dvDfon2iOznZWunPdOyTVSfg-JJUkF6SITd3potChOkLWJ6rup_SE3hNg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😢
وضعیت شیاطین‌سرخ بعد قرعه‌کشی لیگ‌قهرمانان
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/Futball180TV/105001" target="_blank">📅 14:50 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105000">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f5e4faa301.mp4?token=AnP0r_Ty4UwxrLmWt71Hido_btCaLzNxIPsTEjcuYugx-KB3vOkeFKhrlnhKMGjWiGc6My4Hy2xXtL7Af2axlF9eLfbICurvjgsINQVIINVqV65viKjA8JD6wwGjguPAYw_4ufAKNFERI9V9QMGADpFLRQE8oEyM0NqaO1InqeMQF4Q2FAIl2-i29D876Gn3VninseFkoqVKd8thx5ZoX4D3M-7eFsvpoQKY_Yd_vYyWJiWbUaqCcSxM_bvj5F2JGoIS5dvfoT6stRL64Cmr01KIoJ3Ay_994pdk-xq5OiqYdKhJjtz0rGt6TGLMhScIqc12aQxzowhwHJunmg1WTQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f5e4faa301.mp4?token=AnP0r_Ty4UwxrLmWt71Hido_btCaLzNxIPsTEjcuYugx-KB3vOkeFKhrlnhKMGjWiGc6My4Hy2xXtL7Af2axlF9eLfbICurvjgsINQVIINVqV65viKjA8JD6wwGjguPAYw_4ufAKNFERI9V9QMGADpFLRQE8oEyM0NqaO1InqeMQF4Q2FAIl2-i29D876Gn3VninseFkoqVKd8thx5ZoX4D3M-7eFsvpoQKY_Yd_vYyWJiWbUaqCcSxM_bvj5F2JGoIS5dvfoT6stRL64Cmr01KIoJ3Ay_994pdk-xq5OiqYdKhJjtz0rGt6TGLMhScIqc12aQxzowhwHJunmg1WTQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🤯
🤯
🤯
یه‌سوپرگل در محلات برزیل
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/Futball180TV/105000" target="_blank">📅 14:25 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104999">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JcHc7-d5qkFcukGflfSPaF52eYSd4HgiAM8jjB0ZU15yETxew_U67TmU18tJecDjR6dnAg3BaySW4FbkO7pHXvPZs9k2ITv_e_zcf38UxE13MSP9dn9FbUpsZZ8zsfnrSkCVxT9DQPhOVyxhrfPLajKXN8KPfQ8knhgyXacm4W9N6Bo-Vh2QAMGly9gt5dJrrV8xw7yVCQSO9H9SWRHOkw6SsgkXUSvmal7IPjmMGbPLaY-usTY6s5Sg-geRoJmeCnnYCfGh9dDNY-E2xX5gV1JOE6dP6eUu42tlIEWJqpoP2JjM3Y5XKlfhuXrHT3thF7KM9gkPie0TZ1-BgziZNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
🇪🇸
پردرآمدترین بازیکنان لالیگا در فصل 2026/27
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/Futball180TV/104999" target="_blank">📅 14:00 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104998">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n3cUxEWbLrM6lgUejQU6UH3wA3UNOi_TVUWKXE4ldfwk5iWWK1OsALw1uAfcMYE3TYRbvMd5oB0X9XvJMX7DUzTXT7VEn0v0OSzBe312OajiD3ZAhEC3TPUZLEc-6m93RLsfFwkU10G_79r0_SXRW8zv7m0Ls-DI9AbMFB0r8R2BLYn8DFnQZldHzzDNB6_DjGHHteSoMzRNBhqcmj8yEJ3aA0_NnNJEr9E5HB_OqtcpNEvLDIz2ii4AtTGTaL5qxEeroJ_ne887Xcq6T6rcRkOx5WhJa2SZGZuYd3FhwR0upvZPZYMP04hEmipCLURadxEUwrsUqdY1zscgomZGbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🏴󠁧󠁢󠁥󠁮󠁧󠁿
هفته‌دوم پریمیرلیگ؛ ترکیب لیورپول مقابل ناتینگهام؛ ساعت ۱۵ شبکه‌ورزش
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/Futball180TV/104998" target="_blank">📅 13:50 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104997">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rgFg8V4TQZ-3SNfinZKCNtG12CwrTtG5En5s4_xmeqEsxCvAtNFkuwF7PEmy2kJjnMu9LRy_WKJbrbsRKjOJPHbxOoY_TQa8qLzIMfSb6rE5vCbZiULwZu9hFhUQxpVR_qufJls6OGr8f0kE9UfxlcEtO1-ZoKCdUxWJyIyefNLxsZbXZx8KzmQA58SxK3Fh_An4iMf7cRCjjmbTTrbnboZg8-0xQc6Q5p06Nji6EEFzgNHzh60_DvPtGLhkxOyNgsh5mq4vuNDq1c3A1Gep8oeehG8Sf8rPNvutow8gXNlp72jXtwkw8m3jD67W3JWzYOTKvudg5_H20H5iVb4YUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
رشد قدی لامین‌یامال طی ۳ سال در بارسلونا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/Futball180TV/104997" target="_blank">📅 13:35 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104996">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g83L3ohmpRGIR0xItIr9KJKtLwdUIeqhsQGTQphzH0_Z2GVbR9JpPZE5JRFbxGnkibT7Iv7vv7B40Hfnu9U3hyFCZ-izHnanN0haCEQK4Y4pG2edePArZ1yvHyTyLkWlDn_r1C93-6YNaL3FSla7WSAqJPRVmKWcboN1OGUV_HLZpBOnjixrLdkvAJDuIM_RtoNsiuiA0A7vuA-YI_Z6HNM4O6KT3bEtb6pf8xvygEbl72up7ZH9BcN9y-qGuUQRSdZ8aJMRPqdlK_r_rgZO900Vk_Asag1fQTtY6q0ocxpjYmH1_sqFa2pb8FzXE-68WJlj8B7tB4lKWNHio6YUdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇮🇷
🇮🇷
ابوالفضل رزاق‌پور مدافع چپ‌فولاد:
🔻
پرسپولیس میخواست برای جذب من رقم ۱۲۰ میلیارد به فولاد پرداخت کنه اما در نهایت این اتفاق رخ نداد و خوشحالم که در اهواز موندگار شدم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/Futball180TV/104996" target="_blank">📅 13:10 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104995">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a1d94427ed.mp4?token=TBmBhQ1WwKGtBLXQLcRbKUIC9uz-KHfxRZb08691Jpq9ELnnw5KnxVgm2TUOeuzrfnUVQkbYXif77YtJIcn6sQq-dnM1dAjTZq77Pz_yaH1F1d9ulRTJOa0QTueX07LeOTLRSh0Or6zAEmU9qwyNrdek9OoYJyp2hO6OB3QibQsSQAfHw3ck14lGaTZCSVT3MxVnGrzdl-qD0dduiukk-3iMKtLSZkVCQBufJNxkjzSOYl3IRCNnUXgmwSXxzAKRT5Fki7JijZu4Ix8yB4gGkBBOcHbnXAr24bSBQ_BRKr3hcvSy9-xQPk3R0EkIlinFnTDNUJUtP-J4KrHE67ZnMg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a1d94427ed.mp4?token=TBmBhQ1WwKGtBLXQLcRbKUIC9uz-KHfxRZb08691Jpq9ELnnw5KnxVgm2TUOeuzrfnUVQkbYXif77YtJIcn6sQq-dnM1dAjTZq77Pz_yaH1F1d9ulRTJOa0QTueX07LeOTLRSh0Or6zAEmU9qwyNrdek9OoYJyp2hO6OB3QibQsSQAfHw3ck14lGaTZCSVT3MxVnGrzdl-qD0dduiukk-3iMKtLSZkVCQBufJNxkjzSOYl3IRCNnUXgmwSXxzAKRT5Fki7JijZu4Ix8yB4gGkBBOcHbnXAr24bSBQ_BRKr3hcvSy9-xQPk3R0EkIlinFnTDNUJUtP-J4KrHE67ZnMg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شاهکار آلوارو موراتا در مراسم معارفه به عنوان بازیکن جدید تیم‌فوتبال لگانس
😂
😂
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/Futball180TV/104995" target="_blank">📅 12:51 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104994">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a2hjdtF_YIMIlK9YQ6S85RQoRYvyMozDoqts7OGWRrjX-mAjs4_NulC2avSjtQUv6cOPYJ6RUGVFQN3ACvLxh3ws9mQoe8PiLeOHh4E0UGNzQvpB97uekws1sSoQbFhN8pu9oMJ9r6l2qMUt6H5c1AQKd9XHoyVi_mv6AJcg5fwwfG6GOxMiQ37hzd5PU0G7chXtMLbhh3-VkauDl2MfsV7WMk5HMu7gioIj41dOXEZhoykD7kx-MxoNlG7WG9dZj7NR8MSdb7elYj0Hdo2h3wP7uHf7LvGJ81uXPAMrLhysxaP43ou8kzSXgs_X1WL5VT8cR3iLOSib1m2nYVZUqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
🇪🇸
🇪🇸
خولیان آلوارز از لیست اتلتیکومادرید برای بازی امشب مقابل سویا خط خورد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/Futball180TV/104994" target="_blank">📅 12:45 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104993">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/694fb72f97.mp4?token=VL6u0qsJbmGgTpzqwqnTsQt8LY3IDorY8kcg7sK1CoGhT-p4-esgzaH1wlIZn1Mrzu-P0lr8yIiqp0OCqnB83jlY8hbV_29h7XB5qMRFvXM97U7fIXmsARTVL_Ev9USOq19Vbth_oePg-HOsF_tOwRIBWoJcCLIENEM62PRkeRGq5smXRlhdZjWOeGYR573RDFSdLl7UkvdYKRrRlxn6GQBPzpLPYAutrb4G5UJqFdYF_N1o8cqilZVqTfglrnZNOfIN9y2Y7cK284Lkd0pquflt0alMDT9M5wzbmFBRDD66XEUXzeURMg9k8X6T1JEKS4WnJqqjpR77XQ3pWMq0OnnBFs8jzSKEK9s_hNer4WhM0HplE_l1Ci_0x1kDn4jZhC5U4BPJGC6jFvw3PVRrt-dXyKL6-D2GulHNrtIGLVFI2Iv9hdBVOClHakPvSHBWer_W_hiHO-sFGRjY-Vz61Nv8jTPKg1J7Np_O-tqiC2EMdMCQq0QPOaIommBSxcHwHMulqpaqTS74XZ7twYc52NTO89fnhQtTKIylJIJfvq3Rm4Drd7v0nnq72FNqxt67kl73CtVxTGq6Bpa7P1hgLyvtfQleeqkw5RRidiVoiYqIAOMAcBrt36TFxAin5x7cT6isXsPcBwSMOVG5-J_jPLfIDSi2p-_IJ4KVsoRZnbo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/694fb72f97.mp4?token=VL6u0qsJbmGgTpzqwqnTsQt8LY3IDorY8kcg7sK1CoGhT-p4-esgzaH1wlIZn1Mrzu-P0lr8yIiqp0OCqnB83jlY8hbV_29h7XB5qMRFvXM97U7fIXmsARTVL_Ev9USOq19Vbth_oePg-HOsF_tOwRIBWoJcCLIENEM62PRkeRGq5smXRlhdZjWOeGYR573RDFSdLl7UkvdYKRrRlxn6GQBPzpLPYAutrb4G5UJqFdYF_N1o8cqilZVqTfglrnZNOfIN9y2Y7cK284Lkd0pquflt0alMDT9M5wzbmFBRDD66XEUXzeURMg9k8X6T1JEKS4WnJqqjpR77XQ3pWMq0OnnBFs8jzSKEK9s_hNer4WhM0HplE_l1Ci_0x1kDn4jZhC5U4BPJGC6jFvw3PVRrt-dXyKL6-D2GulHNrtIGLVFI2Iv9hdBVOClHakPvSHBWer_W_hiHO-sFGRjY-Vz61Nv8jTPKg1J7Np_O-tqiC2EMdMCQq0QPOaIommBSxcHwHMulqpaqTS74XZ7twYc52NTO89fnhQtTKIylJIJfvq3Rm4Drd7v0nnq72FNqxt67kl73CtVxTGq6Bpa7P1hgLyvtfQleeqkw5RRidiVoiYqIAOMAcBrt36TFxAin5x7cT6isXsPcBwSMOVG5-J_jPLfIDSi2p-_IJ4KVsoRZnbo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
رامین‌رضاییان دیشب قصدی برای خوش‌وبش با نیمکت‌استقلال نداشت اما با توصیه ساسان‌انصاری به سمت نیمکت‌آبی‌ها رفت!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/Futball180TV/104993" target="_blank">📅 12:20 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104990">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mHvFXNJP6do5y3-Eb6xjW7x-09JQfO201mArO9781Tly1Oh-sA8Of6jdXtktRz4-z50mCllnTqLJKMF9kgj9G5rdkqx03Yz_r4MQDMUqNI0yCcDastl-2sIL4DlYCl7XXdkb7IGxoVA3MCOabJ2ylsctJb1edVJcWBLaDb_xhPLo5GZ9ygZPH2ADSJSfGxI7VXzfYKwbgz57fSorDzg8yIWQDGC3QwE9dzK8ztlaCGTXLo7_HSXp651cfzjfvEx4K7bUcHhXcm3LIwbEVosbU7oqBTSe3GJKFkS3YDHBrlafP4OA2CwjvwL9QF22zOHcK5W7qgDZDPpRkEO632L5dA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Wco_HfPqpCUyLl3tVLjhutkyaKj0mwG9UE1Yd0kjkOdb9HuaCF0wOEGMj26LJoLQrPk20QfRyCG0-5FllbPKCPwIhAyZCF0QSpNx4sVpXh6lQwaZB64RmsZXmDxDc7H02vxIbmcIjXFUP4SGAN5RruwYaQ7yVL7zLFQXsegXEIF-KGcKqyEsYtZECd4p_1apUw9kLcXJb2Kz5cdQhaZ6MkQnDL-7pw-CLS1xBYkvugtZMk4n9EpOW-AEPFbge8zQEXjj0O2mVAAez9n-uPHLxS-wKnI7JyAx7tv-6qW5oxmApvvK9-o7MCIltrOoy6Bqz907otzg2FXX7Sal1Bdg6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VOY9Ohr-bmuaO6xf86Vv8uofBPjEZWLeq0csZyN0OuyPsPmUOmvzsHu8BSu6skAoU_w5q9xClLgLlWqaf2KLAYQXlSFLo2b2iUbJGVv7C8PUDjlYwF2G-OXaFA34ExOOYGRrCEOCGNUkfCTggliM6WpWXAHOdzOk75Z7NbmKB8pv__J3lU8w7S6I8nrvrVxTNy84tHANLRfJvigOf3QrzQVrkmNdvw_1POiZ75HJKev12UKJh08nwpXOZHi6TeHkCSqpalChC42mHK6UB6fH3Qhm5CPEpsCVPGpFkSl3pGf16GRFXfbblp34vpio3gcHbARa4sfJYoAePqidLAKJAg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👀
گابریل آرتتا، پسر بزرگ میکل آرتتا، دارای یک ویژگی نادر به نام "هتروکرومیا" است، به این معنی که چشمان او دو رنگ متفاوت دارند.
❤️
💎
🤯
فقط حدود 0.1 تا 0.2 درصد از جمعیت جهان این عارضه نادر را دارند. یک گوهره‌ی واقعاً کمیاب!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/Futball180TV/104990" target="_blank">📅 12:05 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104989">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/Futball180TV/104989" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/Futball180TV/104989" target="_blank">📅 12:05 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104988">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m6zXQHN8cS37EEzi5bwBSYLmle7xqTsPo2EWJgslgr-2bdl5Gr575202Ec42TxYEPcCJD_JtQ6pRXrLwsQY_aqqiCIqJgx2FgjjbekIqlZPBz-L-wmfa2_Rw97OzJF4FXt-MI06Dm3yx8wZfxfh9NE7leDM0SWwaLMsqwHlcX68opQngJS667jg46HbAcw2ee0FfSEJ1CmSVudPX-TlGjZqtDYvS2xRG1KP9BUt54TfNRa3GTFeAJZS3uSQCpZYFvbUbdXaKeWc_ur5hKFkgz0NsVfyvl2uFZrlNFCazKxqazWCtQHTvIOv8in7Vdtzfx3vxIVZavw1FByQo4ipqtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
بازی جذاب
پرسپولیس
🆚
ملوان
را در سایت بین المللی
TrexBet
پیش‌بینی کنید.
🦖
دوشنبه ساعت ۱۹:۱۵
🦖
استادیوم شهر قدس
📊
نگاهی به آمار دو تیم در ۵ بازی اخیر:
ملوان: ۱ برد، ۲ تساوی، ۲ شکست در ۵ بازی
پرسپولیس: ۲ برد، ۳ شکست در ۵ بازی
🦖
بونوس اولین واریز تا سقف ۱۰۰ یورو
🦖
بهترین ضرایب بین تمام سایت‌ها
🦖
واریز آسان و امن از طریق کارت به کارت
🦖
🦖
🦖
🦖
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/Futball180TV/104988" target="_blank">📅 12:05 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104984">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bb4df35536.mp4?token=asJUN6KF22MyGo9ARNiHrKtL_dtNiX1HGiR9poZTr65-BB8oWJsr_TkeQYG0IJcUogjc5znRsW4B5BY7e6KJ82KbO1xB4eb0wtRfrHmIUTCjul_A6TU0GBgvYPOeR-vNGZYSQk3cm03ttUA_RLth0GeF6R4yWcwIv6Eh1osuBiHz7IH3n-Je8DnXtnyk9BBOgaxHUoQeulLq6B7ZXGfiXK4od1frDo-X6oEctmJ2sfr4AZltujF59uQUegvSpZJrMq_Vq2_F_TROJtKxsmV2sIStN1a1rqAQJuoiUsWzZUVK0uu-y8kjW5b4EAi80j-01Qu0sa-9lbt3D8_JEqGuVA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bb4df35536.mp4?token=asJUN6KF22MyGo9ARNiHrKtL_dtNiX1HGiR9poZTr65-BB8oWJsr_TkeQYG0IJcUogjc5znRsW4B5BY7e6KJ82KbO1xB4eb0wtRfrHmIUTCjul_A6TU0GBgvYPOeR-vNGZYSQk3cm03ttUA_RLth0GeF6R4yWcwIv6Eh1osuBiHz7IH3n-Je8DnXtnyk9BBOgaxHUoQeulLq6B7ZXGfiXK4od1frDo-X6oEctmJ2sfr4AZltujF59uQUegvSpZJrMq_Vq2_F_TROJtKxsmV2sIStN1a1rqAQJuoiUsWzZUVK0uu-y8kjW5b4EAi80j-01Qu0sa-9lbt3D8_JEqGuVA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
🇮🇷
تعریف و تمجید حمید مطهری سرمربی فولاد: بازی هجومی استقلال باعث شد تیمم مجبور به دفاع کردن بشه چون تیمشون در حمله خیلی فعاله
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/Futball180TV/104984" target="_blank">📅 11:53 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104983">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">📹
✔️
⏸
تحلیل داوری سه بازی مهم هفته چهارم لیگ‌برتر فوتبال با مارک کلاتنبرگ
🔸
چادرملو - تراکتور
🔸
(امیرحسین حسین‌زاده باید با کارت قرمز اخراج میشد. همچنین یک بازیکن دیگر گل‌گهر هم در ابتدای بازی باید کارت قرمز میگرفت)
🔸
سپاهان - گل‌گهر
🔸
🔸
فولاد - استقلال
🔸
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/Futball180TV/104983" target="_blank">📅 11:45 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104982">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s0aBx_EIFgiJlZZXU6h-qLMGmm5BFQ-I_Ky14uuEh_CghvdRPCJHBCqP8mXG7TPI14WQm16ykURQDSo7nHiOPtWkPuTddtDpuBbiz3MvyGkX5mLZ40qtpysQdHdPESOe_uwpTQXswh5XrNp-z109BNWfk0k3tqemJBhAxxi2qB-9BxJyua1j7LeXLVd18WN-ZDbpcYqc0gTI6Hi3s5K8adDEwZmPbSKxdJ7uTKrkx8nDXTbY-bmRKfnJGeu6oxFya2VAY_fRpXCpp4R-hg5xwNvrTxMmBhEUubTWxvYYd3cO4T34kavhpKmcOdDHRc-aPpJgSoh8MXMjFb4yw_8xfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
✅
صالح‌حردانی و رستم آشورماتوف مشکلی برای همراهی استقلال برای دربی ندارند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/Futball180TV/104982" target="_blank">📅 11:10 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104981">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f929791585.mp4?token=M7zHG-y4k2YKa8nnPrSaKlHE9qlUtHw59vo8oAnR6Fl6BsbkYhrT-1E1zNijGWOsyBl1ukvGD1gqvUOneyz4Aql-DoA7m74kzADbXclJUSnvb57-L4V_itUjNZzYXtOZhErmTz9jw9MzfCZAcZjqdWa-4WKPB7s1C0pvJTgfcQp7rXDVyO4LUcxOLcUD47-KP1JrpT0VaVeZJXZv1aqp_TeJj4RbkNnUoI-4RjcfjO6mFav8XDGUuFwlWz0OfFlj3meN7aty8o4sPtUoZGaQ8QpDAfYkRKDqkYwrUNqFMj0jHaG2Wt7F6qijzRBJmHhbY7TaODHFhwGE7BAWF_O2vQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f929791585.mp4?token=M7zHG-y4k2YKa8nnPrSaKlHE9qlUtHw59vo8oAnR6Fl6BsbkYhrT-1E1zNijGWOsyBl1ukvGD1gqvUOneyz4Aql-DoA7m74kzADbXclJUSnvb57-L4V_itUjNZzYXtOZhErmTz9jw9MzfCZAcZjqdWa-4WKPB7s1C0pvJTgfcQp7rXDVyO4LUcxOLcUD47-KP1JrpT0VaVeZJXZv1aqp_TeJj4RbkNnUoI-4RjcfjO6mFav8XDGUuFwlWz0OfFlj3meN7aty8o4sPtUoZGaQ8QpDAfYkRKDqkYwrUNqFMj0jHaG2Wt7F6qijzRBJmHhbY7TaODHFhwGE7BAWF_O2vQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این شاید تمیزترین و بی‌نقص‌ترین اجرای کل مسابقات جهانی ربات‌های انسان‌نمای چین در بخش هنرهای رزمی باشه، آنها آمده اند که بمانند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/Futball180TV/104981" target="_blank">📅 11:05 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104980">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f8294617ce.mp4?token=gGfKcoY4SLjoSfnXkaqrN5OY-5HaaLro0d1MkjIAVRqM6UJ-mAhpE3q2Wa1A0QO_DFQunQck-S8Wl-56dZeXANs927zMB9NP3sOW262qVK8dkCp77OK95WiJKbSUHZesxUFOYBI6lxydr4s5fkvqq4bG4R_GfXWL_siklWF-0R6ilAGtnNUWPCyugiLxmTz7YDeqLP2Fe3YB3aFZMpqVN_fqFLUAsaQB_Qo2Q9HbllMy7ZQ3kCf24wNgyFL6ZO1JAzUm0GazBFRXXnoQpKbFvK_LiDbUFVEvZSv0b4t6GFbOVl9uvmJ8bLbrGiYBezHY8hq2KDHxqZfiarmJLZSt2Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f8294617ce.mp4?token=gGfKcoY4SLjoSfnXkaqrN5OY-5HaaLro0d1MkjIAVRqM6UJ-mAhpE3q2Wa1A0QO_DFQunQck-S8Wl-56dZeXANs927zMB9NP3sOW262qVK8dkCp77OK95WiJKbSUHZesxUFOYBI6lxydr4s5fkvqq4bG4R_GfXWL_siklWF-0R6ilAGtnNUWPCyugiLxmTz7YDeqLP2Fe3YB3aFZMpqVN_fqFLUAsaQB_Qo2Q9HbllMy7ZQ3kCf24wNgyFL6ZO1JAzUm0GazBFRXXnoQpKbFvK_LiDbUFVEvZSv0b4t6GFbOVl9uvmJ8bLbrGiYBezHY8hq2KDHxqZfiarmJLZSt2Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⁉️
👀
چرا در آلمان از کلمه قیصر برای پادشاهان‌شان استفاده می‌کنند و به فرانتس بکن‌بائر می‌گویند قیصر فوتبال آلمان.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/Futball180TV/104980" target="_blank">📅 10:40 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104979">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/31c7fdcd83.mp4?token=FEfyphmbT932BRXFqO-mtVMu_amJseKgrIodmK4002SesnuY_j3d2CR94v4JNMN2dEjv1HlbZ-C3d8SOjmZ_bp9xXHyNM9NiKmw6FUnbPj1MziQJcjJRZOXJEmq3JU-0D-XdvA3jh7pDL1cW-w20PtiiwUnuu5P7Spysd-oEl1b8jwRwMZZ3zqtbEEl5xM64j0O-5l6GDLkrrvBQbj1GG6tTBYemtPYvpX-7qc21E0xB854Oaw7LA-gcXelqsCV1O0c_-apE7p3PtL2GeOJ8y8WFvXL-cttij3rgxAMoFOLKmWYgH9DRMP_w7IhiKIN5VqFpWw6Muz2vQr_nsqORAZc4e8YIOnCWK1uXhlJKDVDjiqGuzQ_gjzl0hJG3WGDmiD94yiisjJK42Bb8fOS3fZYk9j8y2lEj-xiL3DANpVC0uuBrQieoOLSxouHvntrTXnGP37rh2O0PRWO28T4WQjs9wsUgFYvlrQ6GIWmQ8Rcx8eKTmJ3QsdSuXGpzwP_xNYG-lN-3eZJAgfT5C7w4HInE4x5o_ABG78ZE4ovY9ryfRm1eiVeSCILtcP6xctTrlBJ_FIcHmCRBLctUCxzRQSyc85TPcGc0YT_k3oXl-DBUXhEqogrJFfmktze67DfytNz2UgJf7vsQT7PkZjI2RtO1Y4BczoVSaoko_fO848U" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/31c7fdcd83.mp4?token=FEfyphmbT932BRXFqO-mtVMu_amJseKgrIodmK4002SesnuY_j3d2CR94v4JNMN2dEjv1HlbZ-C3d8SOjmZ_bp9xXHyNM9NiKmw6FUnbPj1MziQJcjJRZOXJEmq3JU-0D-XdvA3jh7pDL1cW-w20PtiiwUnuu5P7Spysd-oEl1b8jwRwMZZ3zqtbEEl5xM64j0O-5l6GDLkrrvBQbj1GG6tTBYemtPYvpX-7qc21E0xB854Oaw7LA-gcXelqsCV1O0c_-apE7p3PtL2GeOJ8y8WFvXL-cttij3rgxAMoFOLKmWYgH9DRMP_w7IhiKIN5VqFpWw6Muz2vQr_nsqORAZc4e8YIOnCWK1uXhlJKDVDjiqGuzQ_gjzl0hJG3WGDmiD94yiisjJK42Bb8fOS3fZYk9j8y2lEj-xiL3DANpVC0uuBrQieoOLSxouHvntrTXnGP37rh2O0PRWO28T4WQjs9wsUgFYvlrQ6GIWmQ8Rcx8eKTmJ3QsdSuXGpzwP_xNYG-lN-3eZJAgfT5C7w4HInE4x5o_ABG78ZE4ovY9ryfRm1eiVeSCILtcP6xctTrlBJ_FIcHmCRBLctUCxzRQSyc85TPcGc0YT_k3oXl-DBUXhEqogrJFfmktze67DfytNz2UgJf7vsQT7PkZjI2RtO1Y4BczoVSaoko_fO848U" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چرا پرز بعد از هر قهرمانی رئال در اروپا به مورینیو زنگ می‌زد؟
چرا رئال دوباره مورینیو رو برگردوند؟
و چرا پرز فکر میکنه مربی شر ضروریه؟
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/Futball180TV/104979" target="_blank">📅 10:15 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104978">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/181464f819.mp4?token=uPVqtin4IgTil75rNtDX5y3h0YlXiQReybco_48pypFT_VUTmy2fy30-PvcvBzabM-yYgIY6UcWfQvoGbHepudDkg5TfdszPueQCEnueTjioYHsjCo43EM7NSHLbQXhN6B8BcIQMrQV7IhXtkkj0746gWsB2A-l4FmU_mzwYwB1y4k50ZhZIIJlJT7FjgGZFEssValWy6lA98EvKULAxMw6m2GP0oAdMqw8Xh96t_H-DKDSLgdsH5o3aiO_N3ePyTEN2fRLOUUni1Kyz2nMblk_UL0mN1vXw3Fh0JTWUhNQyApBaLZFig3XgE3vQszrE120CMGBpTZ40WU6WKKkoVA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/181464f819.mp4?token=uPVqtin4IgTil75rNtDX5y3h0YlXiQReybco_48pypFT_VUTmy2fy30-PvcvBzabM-yYgIY6UcWfQvoGbHepudDkg5TfdszPueQCEnueTjioYHsjCo43EM7NSHLbQXhN6B8BcIQMrQV7IhXtkkj0746gWsB2A-l4FmU_mzwYwB1y4k50ZhZIIJlJT7FjgGZFEssValWy6lA98EvKULAxMw6m2GP0oAdMqw8Xh96t_H-DKDSLgdsH5o3aiO_N3ePyTEN2fRLOUUni1Kyz2nMblk_UL0mN1vXw3Fh0JTWUhNQyApBaLZFig3XgE3vQszrE120CMGBpTZ40WU6WKKkoVA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
⚠️
درخواست ۳۰میلیارد تومانی مربی لیگ برتر برای حضور در تلویزیون
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/Futball180TV/104978" target="_blank">📅 09:50 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104977">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f84e6b721d.mp4?token=GWvFsC6niVkGQYbEeXJP_pgx-Ol46TAbqWPEKVfSfDcMZ-8zaIkkdaBhF8u7CoSL9ldTAjRjk9t30PEdCgUq9y8T5fDdYYqT7rkZv7HyCnVksmymRD0tPqoHllR4hEvAwJblHxQz-igQ6H3tCnqSU3ZfTEA1o3ScHB3huU84gZcQ3IDyDcVfTccvLffHzy48-kx7orZjesLGEzCEGu1U9-xA6q-4KydxA7C2U2jQEpvmMcDT8fhOKfmSFvkceWZrVmGyeM_z4O6C3QpTJwWKx29dhdLULZ0HV4ZJKT8fF_3ccBAbvgIghmTaq4GrDIUzqkJDHv2HiYInZePpfMCdEA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f84e6b721d.mp4?token=GWvFsC6niVkGQYbEeXJP_pgx-Ol46TAbqWPEKVfSfDcMZ-8zaIkkdaBhF8u7CoSL9ldTAjRjk9t30PEdCgUq9y8T5fDdYYqT7rkZv7HyCnVksmymRD0tPqoHllR4hEvAwJblHxQz-igQ6H3tCnqSU3ZfTEA1o3ScHB3huU84gZcQ3IDyDcVfTccvLffHzy48-kx7orZjesLGEzCEGu1U9-xA6q-4KydxA7C2U2jQEpvmMcDT8fhOKfmSFvkceWZrVmGyeM_z4O6C3QpTJwWKx29dhdLULZ0HV4ZJKT8fF_3ccBAbvgIghmTaq4GrDIUzqkJDHv2HiYInZePpfMCdEA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇷
🇮🇷
سنگ‌بازی دیشب هوادارای استقلال و فولاد حین خروج از ورزشگاه
😐
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/Futball180TV/104977" target="_blank">📅 09:20 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104976">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/75514852e3.mp4?token=KShZSmEF12VpyoWpzl2C8Cm9eO2Huof0GD2CY0Xoptd4GEqR-pD7VqxImo1j5KzRfxyKZZMfkKIhyYNzJMA9t1zzTU3-Ev1SbFaAHXFtcGwb30aX3zg5NVXl2zICyqGosmPHjEYdg5RhckD0RyYqkVWMBW2qbQlzW-ExUFCXJyn1UYHliw7l5LW_AJXqQ3ojbqwPIG-V1T-IG-9UNLAieLjtwOxF5SC1UFEVrzSyEc23n6nqyRDpKjLD6kQw4DVqnTzCWtwB_cjVANGDG5h9I8JgAHz7uZ1lnYrI4co6X0vd6o9Rw0c8wrINnK7C-cwbmqfg6Z9GV14D7K4QjLT4kQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/75514852e3.mp4?token=KShZSmEF12VpyoWpzl2C8Cm9eO2Huof0GD2CY0Xoptd4GEqR-pD7VqxImo1j5KzRfxyKZZMfkKIhyYNzJMA9t1zzTU3-Ev1SbFaAHXFtcGwb30aX3zg5NVXl2zICyqGosmPHjEYdg5RhckD0RyYqkVWMBW2qbQlzW-ExUFCXJyn1UYHliw7l5LW_AJXqQ3ojbqwPIG-V1T-IG-9UNLAieLjtwOxF5SC1UFEVrzSyEc23n6nqyRDpKjLD6kQw4DVqnTzCWtwB_cjVANGDG5h9I8JgAHz7uZ1lnYrI4co6X0vd6o9Rw0c8wrINnK7C-cwbmqfg6Z9GV14D7K4QjLT4kQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👍
🇮🇷
🇮🇷
تشویق دیشب اسطوره علی‌دایی در یزد توسط تماشاگران چادرملو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/Futball180TV/104976" target="_blank">📅 09:00 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104975">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">‼️
سوتی فوق‌سمی یاسین‌بونو و کولیبالی در بازی امشب الهلال که منجر به پنالتی برای حریف شد!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/Futball180TV/104975" target="_blank">📅 02:02 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104974">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4aac6582ca.mp4?token=R7J6cwfpg16Zn0vVazuPxjl5kglClGWl7b3KvjxLQXXNH5idK8f5DwIIvbBEoj0pTPJg0Dlwc_AH5fqHuYjy8MlAhrss0GVPiSVJ8sWbikNc9weB7HBO4vRYxmKtVbqZhmWmkre6XLE7NZVfqEqXMnLcxoOPn2m64Xrwa6nejV7Doyqcs-MM9uo-kBoWkOkR2mmtoh7BgB50FH03kgSL-N1HlLYpp4RhwaHW-K_vwt9GMsBPEEiurI7ylYstjI_Y1H84WIzf_FiS-_pOu4yhEtQSXnRCJTQg9q_-WHXdOmd7jiZlyUtV53m-9dF8GCGxcnZqRxyOTmw37XnP8fDgLQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4aac6582ca.mp4?token=R7J6cwfpg16Zn0vVazuPxjl5kglClGWl7b3KvjxLQXXNH5idK8f5DwIIvbBEoj0pTPJg0Dlwc_AH5fqHuYjy8MlAhrss0GVPiSVJ8sWbikNc9weB7HBO4vRYxmKtVbqZhmWmkre6XLE7NZVfqEqXMnLcxoOPn2m64Xrwa6nejV7Doyqcs-MM9uo-kBoWkOkR2mmtoh7BgB50FH03kgSL-N1HlLYpp4RhwaHW-K_vwt9GMsBPEEiurI7ylYstjI_Y1H84WIzf_FiS-_pOu4yhEtQSXnRCJTQg9q_-WHXdOmd7jiZlyUtV53m-9dF8GCGxcnZqRxyOTmw37XnP8fDgLQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
🙂
🇮🇷
مصاحبه با خواهر صالح‌حردانی ستاره استقلال بعد بازی
: کل خاندانمون استقلالی هستیم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/Futball180TV/104974" target="_blank">📅 01:10 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104973">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/241731bcb2.mp4?token=qmPsaYKMYhZ8jDHIkHfP-AWQYqM4vBBCZnnveEWOwmjfa0XSvSqK1OGy8p4ntxZOPJ9BFG9-ZzMi3zs4bGdUwvuMv2tj7tBaaombnivPJYZ01aaJYeAoBv8zkLwq4N-2VX2FdH3bjSOvgsl6alTe6mYRtmxtDuc3PZgWhOSZaba_Bo8DGutRhqydSRydGdYyrMvpwRktC25Z16cKJxPWwKIC-ZHmvhBKrEvrWVX4OJ3wXRLO3c4qckAt-zjpPmJHLLm3E4oZwjuEse16EEplwfk3gluq-XbbO4sNzbaRKfZnb0Rl7HvsTV23xWmNFjv7pPIfeuXNM7b-YW7LAAHnQB7JuSl4nVQUpAYBMNYRjgRp1a14W11AD1IJZ20JzVjDBEopNzKW9FPaT02vic1r9_Z98LEijPzcuQ9dtwv-0IJMbF_IEfwVz7Yxgn8DiYsjJwdHlSdljvwTo2Iec_sEaa9mnXaFpWs5iMwnE45tqNhDqzdEmg-Jon9aZ3Di28drKFr4YOwpyjDCRiTWkKB7Kl9e6fkEp-8YfKWvB_BUsJKkd4k8lxu94KeEnv6a1S_1AbgakD0sQ-Wv4kYCU13EkcVQyZHHHQArcQYWMw1qVjvRDTy3zl_UVMRUAo3zeYWuWVaR6c3dzNdrlcPWU4bOJpQFKmvBRjPgNkw3mWmygns" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/241731bcb2.mp4?token=qmPsaYKMYhZ8jDHIkHfP-AWQYqM4vBBCZnnveEWOwmjfa0XSvSqK1OGy8p4ntxZOPJ9BFG9-ZzMi3zs4bGdUwvuMv2tj7tBaaombnivPJYZ01aaJYeAoBv8zkLwq4N-2VX2FdH3bjSOvgsl6alTe6mYRtmxtDuc3PZgWhOSZaba_Bo8DGutRhqydSRydGdYyrMvpwRktC25Z16cKJxPWwKIC-ZHmvhBKrEvrWVX4OJ3wXRLO3c4qckAt-zjpPmJHLLm3E4oZwjuEse16EEplwfk3gluq-XbbO4sNzbaRKfZnb0Rl7HvsTV23xWmNFjv7pPIfeuXNM7b-YW7LAAHnQB7JuSl4nVQUpAYBMNYRjgRp1a14W11AD1IJZ20JzVjDBEopNzKW9FPaT02vic1r9_Z98LEijPzcuQ9dtwv-0IJMbF_IEfwVz7Yxgn8DiYsjJwdHlSdljvwTo2Iec_sEaa9mnXaFpWs5iMwnE45tqNhDqzdEmg-Jon9aZ3Di28drKFr4YOwpyjDCRiTWkKB7Kl9e6fkEp-8YfKWvB_BUsJKkd4k8lxu94KeEnv6a1S_1AbgakD0sQ-Wv4kYCU13EkcVQyZHHHQArcQYWMw1qVjvRDTy3zl_UVMRUAo3zeYWuWVaR6c3dzNdrlcPWU4bOJpQFKmvBRjPgNkw3mWmygns" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🇮🇷
فراز فاطمی سرپرست چادرملو:
🔺
آقای پیام حیدری فکر کرده ما خریم. قشنگ بگید میخواید یه تیم ببازه دیگه اینجور قضاوت کردن بخاطر چیه. امیرحسین حسین‌زاده با تکلی که زد دوبار باید اخراج میشد ولی حتی صحنه به وار نرفت!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/Futball180TV/104973" target="_blank">📅 01:02 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104972">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7aa1d6121e.mp4?token=Gfe2-K38q24Q6CpZ6ijR1D-hdz4j9gJ-uiAmbgMu2-ycEeowIucJI7MNL09pRbTm0OAA2FjKfG59hszMQVm1Kkmc4TkzIoGwz0ilPrgExSBPQ0TNwkFo3lZRvlX-bmOupc9zQGxrV1eiexvx1xiDWXymvSNRG46o5HS0r2OUjpmSGuIk0O2ukQRjQxn_LdMx0BnrYA8-CVs_ECn5IqvaPtrvspla85xvV0MT5tXE3vJ_31Lfl3S0hz9gMNzzgL0Ak1NZ-FeUfmzNZ7UkacSmN2B7RNs-w2JYIWHhd_YlQNkh5pkE0PKYC6u-4eLwfBxVvL679Xkbd13_MtR1vCA0ZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7aa1d6121e.mp4?token=Gfe2-K38q24Q6CpZ6ijR1D-hdz4j9gJ-uiAmbgMu2-ycEeowIucJI7MNL09pRbTm0OAA2FjKfG59hszMQVm1Kkmc4TkzIoGwz0ilPrgExSBPQ0TNwkFo3lZRvlX-bmOupc9zQGxrV1eiexvx1xiDWXymvSNRG46o5HS0r2OUjpmSGuIk0O2ukQRjQxn_LdMx0BnrYA8-CVs_ECn5IqvaPtrvspla85xvV0MT5tXE3vJ_31Lfl3S0hz9gMNzzgL0Ak1NZ-FeUfmzNZ7UkacSmN2B7RNs-w2JYIWHhd_YlQNkh5pkE0PKYC6u-4eLwfBxVvL679Xkbd13_MtR1vCA0ZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
🚨
معاون اجرایی پزشکیان: شخصا اگر میدونستم آمریکا قراره رهبر نظام رو ترور کنه، دست از ایدئولوژی‌های خطرناک برمی‌داشتم و غنی‌سازی رو حذف میکردم چون عقلانیت حکم می‌کرد!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/Futball180TV/104972" target="_blank">📅 00:37 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104971">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ujP37uQHlUQ0R_LgJ28kwkMcgMjtJcchzRVbDG0Phf8SwRqS9o-XgW6adNTFmVffSPqiVv9f_EMMkk8SNmKEyXPLs022eLkzi6CtEDZBZkFbcB4pgTIc8EKYDkHp_iEvZifGv442BkLeGFDrfzbZdNf-VC2soD3lmPDqrxSxoazKcBopGYtPR2Ah9efwM6Bxh04hc_7zceWXtX_YChTZq-VbsJROcnPBT71I7DsLp7jjCw7CtIDradG3fm-rG3BIrsPnsvj3hCWfmVWsDG0B98b3ZYJffZQR71XDe9yLG28VMCWI6zHdCa2l0sCi9anpk0sFgu_2Aeh05aJfrfbKew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇫🇷
هفته‌دوم لوشامپیونه؛ انریکه همچنان در حسرت برد؛ لیل موفق به کسب امتیاز از قهرمان اروپا شد!
🇫🇷
پاری‌سن‌ژرمن
😀
-
😀
لیل
🇫🇷
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/Futball180TV/104971" target="_blank">📅 00:27 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104970">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z31EaWKbgw73gnxuLb4kxUq3_K3Yq9-aw8O3HXO__S_eHycgYHn4dfzeskjbqU6ch15ZqUlfNGW9wzXVq7Vd3VuBUuRSGVfBHD7Cz0M-TB47V2A0GLbZLYAbwZhlHLvw0_fYxjuhYvoz9esYq92GmzSmw7DU423TfyTh7-33DHl-DeYBTmrHpZz4e-2wC8MkN3VT8fPZLPypIh7lKjCdGivZHVwcpUFqp08KoOAh7r8fXgw7kWIWPOoJ5ei8cDwRuJ0XmpVXCCwPC_-FP3SP_HJ0MywhNjAPrxDlRcbCKYA_Ov-dQ8S5twOgVriT5UfPMxFTiskyWqJ9CPUY6YqSzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
هفته‌دوم پریمیرلیگ؛ پیروزی پرگل در خارج از خانه؛ موتور گلزنی هالند به موقع روشن شد
🏴󠁧󠁢󠁥󠁮󠁧󠁿
منچسترسیتی
😀
-
😃
کریستال‌پالاس
🏴󠁧󠁢󠁥󠁮󠁧󠁿
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/Futball180TV/104970" target="_blank">📅 00:25 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104969">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qdEw1S4enbZ3TZ1-s6SsVuz3QCrqJfSe5ki7iDn_m2nJRkffH8FSHxsvfJEXPyy1z7TL9SxQzU3enZEGy5MEbzMqyXS3CLRbClQ0Lnz8p9b2RpulrTIBSlbhemD33SYq1HPaNQP5-YrvMeVq-XteookHUTItw2cf95z9ejFLyYCgHZFr-mZYe5LcJHUi43rI1JWhugtmVKGYJx9jFs435VacKdf78eky7beLSTfIjg8N6Zjbh8n6Qjk_9QBWbvoaprwIWNO8ahIi_HbPQcLEwsZXhfxSzFhqx2jrumYdeoCtpYgnWa-zzQ48YRqXt0tB-mnYRatMhz6VxXAW52NstQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇹
هفته‌دوم سری‌آ؛ پیروزی راحت در خانه؛ روسونری با مهاجم جدیدش دلبری می‌کند
🇮🇹
میلان
😀
-
😏
ونتزیا
🇮🇹
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/Futball180TV/104969" target="_blank">📅 00:19 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104968">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/32fe7cb793.mp4?token=aN4q7m30gUYdERjYvY1qTZ1MKw04J6te_31aNQhesLeBpMaE2nDknFLJARfdme2LmpHoyCtxErbrcGMBveRQCDP88aFNAuKCZpebevAWbt_WpPlbigU3b8dAITDyi8g4RneQca6TjQfWW-B-sXVWFQwnTeI6YXYojBm5Ta0FJ_pvRm9LWaddHV1Akh6wauhv9MhBALp5WsM9RCBQB6LuvweBZ-8Kms3Naml4rm07LRiNYDhRoK__b2qtvVmZJQmJF_bkEzrebusrD26lfWftIuVZidrtG01OKdq1Vph__vKvpVids9Blkm3s6yFs-A1CuJZtnDmA-vbIUBwvJIERHg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/32fe7cb793.mp4?token=aN4q7m30gUYdERjYvY1qTZ1MKw04J6te_31aNQhesLeBpMaE2nDknFLJARfdme2LmpHoyCtxErbrcGMBveRQCDP88aFNAuKCZpebevAWbt_WpPlbigU3b8dAITDyi8g4RneQca6TjQfWW-B-sXVWFQwnTeI6YXYojBm5Ta0FJ_pvRm9LWaddHV1Akh6wauhv9MhBALp5WsM9RCBQB6LuvweBZ-8Kms3Naml4rm07LRiNYDhRoK__b2qtvVmZJQmJF_bkEzrebusrD26lfWftIuVZidrtG01OKdq1Vph__vKvpVids9Blkm3s6yFs-A1CuJZtnDmA-vbIUBwvJIERHg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
‼️
🇮🇷
کشاله‌درد دوباره شجاع خلیل‌زاده در بازی امشب مقابل هواداران یزدی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/Futball180TV/104968" target="_blank">📅 00:09 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104967">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Yj6_kjt4wQk4meYU9iFdKoQmUuYM6tmiCoSRNb_19gNgyUyB19J7V-vXXyZgsxnfnWYKFd4PGY4zJ-6vpcpjnWOT2TivjLjZTOMyb7tCfpA2cUiaZxaX0WU981FLzHO41iPmzmBqPZRLrPO_Rex88Avs3H_XDwsaHhAxN7WNaCu4NaVK8XH50qggM6g5SIE4pB9SxN1yKzaXsfljoilYuG37JVlgvRkbfQNlTf3pMi4ZFGNTh9dkfmWmLwXOvyDX32eha6Eyglsd-6KsgF3rR-mBUA-mj0U8w_3SCRIatJuDHkoKEF0OEnykdPZv1aoz0zfpHF7UxEyrE8bCDUpZWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
🇩🇪
هفته‌اول بوندسلیگا؛ موتور گلزنی خشن تیم‌کمپانی با قدرت لیگ‌را آغاز کرد!
🇩🇪
بایرن‌مونیخ
😄
-
😃
اشتوتگارت
🇩🇪
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/Futball180TV/104967" target="_blank">📅 23:57 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104966">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3e92dec0fb.mp4?token=d1GiOyR-_vuFFtI0h3P3TG3AtUa-1fJ_tTamOhNHU8oovRxYP1VLRioo_3qrunoTAHUPgUHVGJj8eaQjt7HIsVxDArYB5h7gBOK0dzrGhRpDOmxWsXi1LNw8CAV0ZGFgea9K1bnaSkALUN-K2nq9RLi1SmYbf-viuqvWoBAHTJ3jdiLAIIr99ifbbeOT5I6ZQSTZFnAhCcjDVGyumnYoqHAjFt8HV6UEwRIta-LWiCUmpgQTnhhdzDu4dfArZ3AQ47WLlS6VOb07vg-Z3B3gY_ntH_hQr7iFs2BaJ5w18pnRUKq-pTuZy1c5Vwj0SpowCX11nXFVewsYpFlRqzzBFA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3e92dec0fb.mp4?token=d1GiOyR-_vuFFtI0h3P3TG3AtUa-1fJ_tTamOhNHU8oovRxYP1VLRioo_3qrunoTAHUPgUHVGJj8eaQjt7HIsVxDArYB5h7gBOK0dzrGhRpDOmxWsXi1LNw8CAV0ZGFgea9K1bnaSkALUN-K2nq9RLi1SmYbf-viuqvWoBAHTJ3jdiLAIIr99ifbbeOT5I6ZQSTZFnAhCcjDVGyumnYoqHAjFt8HV6UEwRIta-LWiCUmpgQTnhhdzDu4dfArZ3AQ47WLlS6VOb07vg-Z3B3gY_ntH_hQr7iFs2BaJ5w18pnRUKq-pTuZy1c5Vwj0SpowCX11nXFVewsYpFlRqzzBFA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
‼️
🇮🇷
🇮🇷
محمد تقوی، ایران‌اینترنشنال در برنامه هت‌تریک درباره تساوی استقلال برابر فولاد گفت:
«غیبت آشورماتوف در ترکیب استقلال باعث شد تا عارف آقاسی کمی با مشکل روبرو شود و نزدیک بود با اخراجش شرایط استقلال را در بازی عوض کند. همچنین بازیکنان دو تیم در ضربات آخر بی‌دقت بودند.»
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/Futball180TV/104966" target="_blank">📅 23:55 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104965">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/Futball180TV/104965" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/Futball180TV/104965" target="_blank">📅 23:55 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104964">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Spa9MByUMNf_dr9OIEqJIrgBxA4rOEmXRPSVdA0zzhJNIbbXqeW3bBm7Ruv5y9ZAIcppdYBGXDOZ50kAq5tCpLk83rIDPgy7QMqfbRbTIjLmSUrUKLYQwnqbg3rB-SDmOgX9cx3lvIE0HYXZv3lXkV85SHK04607F80vOztIHZIkcSKQ8OIojxZ7xk-hc-VrrBmvrNv7p2WgDSLzDsfxm5DE1YoUptNZ1m9QFXCMSLvyBvCCr4Fk82-GpOzYSbcsgKs7hV292leoVegr9yHa_Q2Cs5sNLN3vA0MRAUZo8mIz-egjhSPLOD3X-7ErsImKi4wgTtEvx2fj7wkrKEybow.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/Futball180TV/104964" target="_blank">📅 23:55 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104963">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c196e7e0a8.mp4?token=PrHEVkPmNZsLqekTya7Gl-E3gRE0r2tFwHxzvN98RHW3NKvEpR0B4UfPJhk5lTUL5UNJ7CkKXMeYj1Ue7-41FncfxnZqPvCrH7x5HinICdMrVyVXhnynDyu2nJw5VgI-NneY0dVZsDXglN8ExqHp64UAjLyi8_b1IBlkF16r_aEHn0LEgAsTsqgcrWa5KohEhB-u2vp65ECkiAe6-4ZpKctGJchBVV4kowmS2TtSSm0vI2M6cQVD85tyw-iCvvcRwrKDIUJp_s_lj8LJL1g-jtRBTPZimPJu9pc2uq5pouBfXifs1qRwlFOla_wo_wURh-tXVFQr1BK_BGSw9byfng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c196e7e0a8.mp4?token=PrHEVkPmNZsLqekTya7Gl-E3gRE0r2tFwHxzvN98RHW3NKvEpR0B4UfPJhk5lTUL5UNJ7CkKXMeYj1Ue7-41FncfxnZqPvCrH7x5HinICdMrVyVXhnynDyu2nJw5VgI-NneY0dVZsDXglN8ExqHp64UAjLyi8_b1IBlkF16r_aEHn0LEgAsTsqgcrWa5KohEhB-u2vp65ECkiAe6-4ZpKctGJchBVV4kowmS2TtSSm0vI2M6cQVD85tyw-iCvvcRwrKDIUJp_s_lj8LJL1g-jtRBTPZimPJu9pc2uq5pouBfXifs1qRwlFOla_wo_wURh-tXVFQr1BK_BGSw9byfng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
مسعود پزشکیان خطاب به کسایی که میگن تحریم مهم نیست و آمریکا هیچ غلطی نمیتونه بکنه: نمیدونم چی بهشون بگم. فقط میتونم بگم عقل هم خوب چیزیه!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/Futball180TV/104963" target="_blank">📅 23:43 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104962">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dc25ebba85.mp4?token=GJnOYYKSR8NEUFvAvjbpnuuy7mb36t1gN56_ooiDEWPAd-PrBUuWmfzY1AgNq6acQPTVOZT0otoGY3hJI_cziG3SKgMGiimCqJlqDqLrjX_t9XOI7oTw2NCAW3BgG8eaF3japqkayDx0x4XnxrhiJ59MijwM43GA5oDLf0lvLBRyAagrKuH_bFsioGMMND49gMBo8lBxgyLsS8DzGL-WoLm4jx6XySEjBfosXzKuypiRcvZ5yB6nJOQkPU0VLIqIM1KS2EXA6gmH16SB_cuuP4i9GlQde3bsQKPeC4vbj94uYEiZfLga8fKznBpp1-t5yE7gwPsvZdtfQMP4dOzo-Bu9VUXOumDyoT_dJ8rxL_SIXZyCgyWnCKqaY6XYnzQxWtDitYZfzMTFl6KAyOZKwrMrvH_qQdNZWQRtgRFqm1shR58uEdhRz1UyEkH4l9HDcrzx_j75Oz_gsZ2nyyk3BB_-EkRhso540Buoenn8Qz7MK6ZPjSmXqiugBnw4ItZlHzEldU9FypIS1XTuwJ2VgV4yvmizfFVd15iI9nQlx-SUMyE3goZLEp0SZ4TULAheOVxZHGr-PekLDDNtMVCIqUzt2pP08mhKeQ6qGvFfU_1vCj1kYeC3205curOFcF6mZjl3UWQl0lqDA23oNyedX7rdUhEDke_N7bh1bPZvWuM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dc25ebba85.mp4?token=GJnOYYKSR8NEUFvAvjbpnuuy7mb36t1gN56_ooiDEWPAd-PrBUuWmfzY1AgNq6acQPTVOZT0otoGY3hJI_cziG3SKgMGiimCqJlqDqLrjX_t9XOI7oTw2NCAW3BgG8eaF3japqkayDx0x4XnxrhiJ59MijwM43GA5oDLf0lvLBRyAagrKuH_bFsioGMMND49gMBo8lBxgyLsS8DzGL-WoLm4jx6XySEjBfosXzKuypiRcvZ5yB6nJOQkPU0VLIqIM1KS2EXA6gmH16SB_cuuP4i9GlQde3bsQKPeC4vbj94uYEiZfLga8fKznBpp1-t5yE7gwPsvZdtfQMP4dOzo-Bu9VUXOumDyoT_dJ8rxL_SIXZyCgyWnCKqaY6XYnzQxWtDitYZfzMTFl6KAyOZKwrMrvH_qQdNZWQRtgRFqm1shR58uEdhRz1UyEkH4l9HDcrzx_j75Oz_gsZ2nyyk3BB_-EkRhso540Buoenn8Qz7MK6ZPjSmXqiugBnw4ItZlHzEldU9FypIS1XTuwJ2VgV4yvmizfFVd15iI9nQlx-SUMyE3goZLEp0SZ4TULAheOVxZHGr-PekLDDNtMVCIqUzt2pP08mhKeQ6qGvFfU_1vCj1kYeC3205curOFcF6mZjl3UWQl0lqDA23oNyedX7rdUhEDke_N7bh1bPZvWuM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🚨
‼️
🇮🇷
🇮🇷
درگیری شدید خداداد عزیزی با خبرنگاران یزدی پس از بازی با چادرملو اردکان
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/Futball180TV/104962" target="_blank">📅 23:05 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104961">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ssz1Nc5_JkCTLHBsZ-8XCwuGtzDuvHCsVq9yErH6aqzsX7ztOCjkquiv9MPzhy7oriWCazBSWzmTlcocRDeNbF6Yf6ZoP2F--YEdlSlV1J1GAHCiURKmzHPklfg0GMo1PoOV67rV0hv3lfLIzV0WJ5_RhmKtR2p9Un63aAGhEi_SP5TjXAodE865CjuARLrgfQRpENXrDo3_-i0fAIzewXHiyl-FY0RpbNJoqCNkXOqXhLRhbn9wMsRLfP7ZanfDqPfaYjD2nXq_Rygz2P8eF34tP0Y1I-6IwgFXwI1ZqyWXRgerzmAabxBEsGkQXgS1hWdc0ztIFH9bemFRZNE5Cw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
🇮🇷
هفته‌چهارم لیگ‌برتر فوتبال؛ پایان نوار برد آبی‌ها؛ شاگردان سهراب بختیاری‌زاده با تساوی به استقبال دربی رفتند
🇮🇷
استقلال
😏
-
😏
فولاد خوزستان
🇮🇷
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/Futball180TV/104961" target="_blank">📅 23:03 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104960">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KwB9Z3VmDwQB_6TTOTIE-KiFmLkuvdxtPUO7Cf2fjd7H1jqTQmgGzWXQYkIWcRDVR-96RRiBgvUq5_2ZyR-PhLfp8Sugaqz071xhi1NOZ_MHVYmZZE-Hj5qy4f2UsSXTZWC5ZFex0En7r7quUd18hnoXKAM1F7TDKn4uBYkAOJv8eR8e2z8Tzpbj0j-6wG_vEs-u1frwi7smfGT9Hmpl3aaKA1xXU_pztA01rgo8rWTXXFLZDPxyWTCjSE8kLz9-F_bhsneSFX265EI_9rzcr_BHt-VnoVc7yslPEYMGMfTK17WSZ-B5kLDMTu3LtAtFFU1HHuAJmFitovuH59inFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
🇮🇷
هفته‌چهارم لیگ‌برتر فوتبال؛ پایان نوار برد آبی‌ها؛ شاگردان سهراب بختیاری‌زاده با تساوی به استقبال دربی رفتند
🇮🇷
استقلال
😏
-
😏
فولاد خوزستان
🇮🇷
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/Futball180TV/104960" target="_blank">📅 22:59 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104959">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🚨
🇮🇷
🚑
صالح‌حردانی در آستانه دربی بدلیل مصدومیت از زمین مسابقه خارج شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/Futball180TV/104959" target="_blank">📅 22:55 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104956">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/ed2d489407.mp4?token=fTC7QN4IJZWcrvBCn1Ij6PgWhxLbtr7NffqMkpD2m1dJWtQeKBUjFmkk4NObpdX90jhm_KVa2BRjTBEyv68a5XGYnQ8sC-2MzXRgb3sjg1fKOiSAIofqiJ7H65FgprMGD0p2fNJTWh3NsC5ZtM_JpvSCAB2PFewJlLFkXLx57T5CEt4H-y65gd7FV1W_GpxsKFDxUPT59YWy-ueSUVzkhvXHNzoZwjZmz7hQUHdpnxcGo9Eby-cvA3WnZcCE5EXMgqL7JA7d2opvhTythWMo4bPNjzwFajgKnFLXGQ3i__TBKZamingcjew7mZ65WPre9YCAsAq1UsTIdRyl_CFzyWi_xmsHWfBap-YJ_CLPkX_RgJ97iNTS_LRm5n83s1V_3z2J_Qz1LB0UmrEw6WcPIbrC1twiSCuwm53795TZHYd0g46Y7Vrefvsoubqw72KgbCMREPzcrDKuSIRlt43ZCXndLkBRKMgb4wSAaApwobKgmYZAIKf033LpR7eDl5DlJHjA-axE9MvHEIiR1HzzzBJXiyU27uQfOCyaFyW_5YcDO4hSZ5RYQ-OC_gK7DDV03mZSoID8l0qohWWhVB2QLgRhU8puDOWcioLsRf65tnnG4DCi-TiWgr-BgnDEK1-NJtslkAA-vzdqzjRnfqFRrOOaALlIezDaIGqw-JwtuFQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/ed2d489407.mp4?token=fTC7QN4IJZWcrvBCn1Ij6PgWhxLbtr7NffqMkpD2m1dJWtQeKBUjFmkk4NObpdX90jhm_KVa2BRjTBEyv68a5XGYnQ8sC-2MzXRgb3sjg1fKOiSAIofqiJ7H65FgprMGD0p2fNJTWh3NsC5ZtM_JpvSCAB2PFewJlLFkXLx57T5CEt4H-y65gd7FV1W_GpxsKFDxUPT59YWy-ueSUVzkhvXHNzoZwjZmz7hQUHdpnxcGo9Eby-cvA3WnZcCE5EXMgqL7JA7d2opvhTythWMo4bPNjzwFajgKnFLXGQ3i__TBKZamingcjew7mZ65WPre9YCAsAq1UsTIdRyl_CFzyWi_xmsHWfBap-YJ_CLPkX_RgJ97iNTS_LRm5n83s1V_3z2J_Qz1LB0UmrEw6WcPIbrC1twiSCuwm53795TZHYd0g46Y7Vrefvsoubqw72KgbCMREPzcrDKuSIRlt43ZCXndLkBRKMgb4wSAaApwobKgmYZAIKf033LpR7eDl5DlJHjA-axE9MvHEIiR1HzzzBJXiyU27uQfOCyaFyW_5YcDO4hSZ5RYQ-OC_gK7DDV03mZSoID8l0qohWWhVB2QLgRhU8puDOWcioLsRf65tnnG4DCi-TiWgr-BgnDEK1-NJtslkAA-vzdqzjRnfqFRrOOaALlIezDaIGqw-JwtuFQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🔥
گلزنی رونالدوووووووووو برای النصر
گل شماره 978
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/Futball180TV/104956" target="_blank">📅 22:46 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104955">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9ccdc8cb72.mp4?token=rcRDKkd-fkVzoD-dfIKZ2FJzvFQGrSfHTzWnV0WHfOqOKZf7msRzt5sct6uPbX6jCvSF_k0hPi5sZYr2zuFh3HVaTsTD4mJpAn-SarOt0-j0CDAX5OAwn52DEJBRg6LOifTLVkvsSW6CWaBZfpf-Jf9HnKjOxC8PpZYM0iA6kY8zJYXHiBI5IlEdgJX5pVdKXHllZRZ61oQCcTZ96jdxLLqt59Quxab4fKZipqOw3JxuBlNJBQQaqj7Myc16okCC2G5w8BlZrloDl0ffmOaBQD2rxpkA2Ww4MuRKX4zxG8cr0S1PNtGDxeV3sKkeNfnlHK1yFswKrFm4L44DqpI6vQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9ccdc8cb72.mp4?token=rcRDKkd-fkVzoD-dfIKZ2FJzvFQGrSfHTzWnV0WHfOqOKZf7msRzt5sct6uPbX6jCvSF_k0hPi5sZYr2zuFh3HVaTsTD4mJpAn-SarOt0-j0CDAX5OAwn52DEJBRg6LOifTLVkvsSW6CWaBZfpf-Jf9HnKjOxC8PpZYM0iA6kY8zJYXHiBI5IlEdgJX5pVdKXHllZRZ61oQCcTZ96jdxLLqt59Quxab4fKZipqOw3JxuBlNJBQQaqj7Myc16okCC2G5w8BlZrloDl0ffmOaBQD2rxpkA2Ww4MuRKX4zxG8cr0S1PNtGDxeV3sKkeNfnlHK1yFswKrFm4L44DqpI6vQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
💙
لک بازهم مانع از گلزنی یاسر آسانی شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/Futball180TV/104955" target="_blank">📅 22:44 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104954">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/77ed0196bb.mp4?token=Vp0FSNm8-Odwbtw9Rh-_5xDvyVZ5F4pWg-4S9l3j1ONBZYPWz4eVXrpV4nslyZM8yPGHvCaRIyolcuFC6iUxCsvXmD71L3N6MzHJzAG8i97LdnwJyNYlmc0nSalI04x0QTG3SDLwn7uisq-dtQX3s8xrGieqscqeCYNbkMud5npSQ896yncPxETiSxXaBE44hkUHqNO1x-jtV3D5LloOEPFfxuGw0chNRXGHCx7BxKIrwJHkhwIqq-Z-4fj7-DTaxOZMttrbWx3xgwm3celUbq3XmTI-PGVAjec_5hMDgMMO_AHQIcxCFbq_d3lu5zvQ5Vb_Hg9JoZZ4aLkew6VpOg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/77ed0196bb.mp4?token=Vp0FSNm8-Odwbtw9Rh-_5xDvyVZ5F4pWg-4S9l3j1ONBZYPWz4eVXrpV4nslyZM8yPGHvCaRIyolcuFC6iUxCsvXmD71L3N6MzHJzAG8i97LdnwJyNYlmc0nSalI04x0QTG3SDLwn7uisq-dtQX3s8xrGieqscqeCYNbkMud5npSQ896yncPxETiSxXaBE44hkUHqNO1x-jtV3D5LloOEPFfxuGw0chNRXGHCx7BxKIrwJHkhwIqq-Z-4fj7-DTaxOZMttrbWx3xgwm3celUbq3XmTI-PGVAjec_5hMDgMMO_AHQIcxCFbq_d3lu5zvQ5Vb_Hg9JoZZ4aLkew6VpOg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
#رسمیییییی
؛ با اعلام پزشکیان نرخ سوم بنزین از ۵ هزار به ۱۰ هزار تومان افزایش پیدا خواهد کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/Futball180TV/104954" target="_blank">📅 22:32 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104952">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SvGZttdOXTj-5Du4kXVWrGRZ6lZxBGpE66_sq77wm9Yl_nQPhBTfbtAcyvaJ9KYJUBFrZBwEi1ByDIjEsc71ZgYTVTPIOUgo1PuMZtGJnaRYJHY8SJxBhlRnyvQp_El5xuDTBcZefCGpkuuPNRaGlEjLyKkW4B_0_5T0bK99YraiQUwFrLWD-uTOagEVTQ9zHvvFpuHCxXOP8KjigNGQIlIiUs7M_UaH7OAA_1BSC0pdmpqfM7ejeh_mWC6ESYHNLDGsPfS-oz4JzD9uyERaZmbymOR9lSktiBvNXcCOl-M3q5FBkh4AQWsEUE53s7yHPT_2KJYaMhulZsH0h155sw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📰
🚨
🚨
🚨
🚨
مارکا:
🏴󠁧󠁢󠁥󠁮󠁧󠁿
طی چند ساعت گذشته، منچستر سیتی نیز به کورس رقابت برای جذب خولیان آلوارز پیوسته. آنها در تلاشن با یک قرارداد قرضی او را به بازگشت به منچسترسیتی راضی کنن
❌
🇪🇸
آلوارز هیچ تمایلی برای برگشتن به انگلیس نداره و همچنان روی خواسته خودش ( بارسلونا ) پافشاری میکنه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/Futball180TV/104952" target="_blank">📅 22:06 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104951">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🚨
❌
🇮🇷
اتاق VAR اعلام به آفساید ساسان انصاری کرد و اخراج عارف آقاسی منتفی شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/Futball180TV/104951" target="_blank">📅 21:54 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104950">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🚨
🚨
🚨
🚨
⭕️
عارف‌آقاسی مدافع استقلال بدلیل دریافت کارت قرمز از دربی محروم شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/Futball180TV/104950" target="_blank">📅 21:52 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104949">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🚨
🚨
🚨
🚨
⭕️
عارف‌آقاسی مدافع استقلال بدلیل دریافت کارت قرمز از دربی محروم شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/Futball180TV/104949" target="_blank">📅 21:51 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104948">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/chEg8sLVLbNaHQtcWWgd_1Ghzry__vcN0I1xPeBH5c4cEb-3eP8EBK2cwzeAltD_mqAunHxV_OxIfoxP4eQeHgZTwzNgOSNxxi2M4F01U9c0COTvjzwiBhvMKqRjRrssLb8BVrwZPmpnyvtvfs0FjJxTFo3tHantfUS4CxjR9te9LAT2e8rL-dU6ukcxV2HZQR-qMam5OPFaLQsTXnaeLHsjNj1kq46kFWmWJNTcNoMMdcTuSZ09g5r4hl4HkgL5-zz_LQaOMWJAsYgMDl4Wi6AlnxbDrro21wDFhTeNIW8P-GbYUq6w2wpttEozFNi-JX3ZZAe0ovA6e0li-PPodg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#رسمیییییی
؛ نیکولاس جکسون با عقد قراردادی تا سال ۲۰۲۹ به ارزش ۶۵ میلیون پوند از چلسی به استون‌ویلا پیوست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/Futball180TV/104948" target="_blank">📅 21:31 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104947">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WYT5DN4fi53MR4CIYlaP_K6iJzPaTuOpNcrkK1vX7WGF1w8ImLFlSzj9tImAbWRfO139VzvS3kqkC2AFnsinpLvwxy3EsQ3ODzz09MMLUc84jpC60qaKEb4KuzzK5AHYrjgE85XqB-sAn6ak2-g3MMer32EOxM7uzE2IZVPGupZfyU_5T8SCzRHPmVj_7kSMZ2k7ixq9r9tFNuvDQBDP0TJmxrDrTYeKXlvZrfTzuGOD09IO_3XcM-e_IbCkp2giEyNVbMsW8I56T1By7bCtx0dYTKqFbUJ_vNEXcfeWSbvIN-Lh356GEl2ps-qj23CV94wC7NwwqShFNOeT-35soA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
هفته‌دوم لیگ‌برتر انگلیس؛ ترکیب منچسترسیتی مقابل کریستال‌پالاس؛ ساعت ۲۲:۳۰
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/Futball180TV/104947" target="_blank">📅 21:16 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104946">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f1abe2b073.mp4?token=TDE8TnbdOWNP4aOKWqHZOVkST6q5A2mmQpIGT0_c4cxGf9OfRdyTo-lC2YbeJ9--IQU7PrmfeFUYAC4yIkx43T5-gyf6VOn3oh-DWU87NhJQ22Q9ts484qS5eTJKcZmnxTsA1qBQq0n9HndHHeni0E_r1BPPNwdm_RMyqcJhbxEhWY6HR-24s53rax5bpdB6PNTzrLHbJQBbM8AcV4O9KdCn3wcGx2TpQXpJluflAljEi48F01JAeF-iFmS_TWme2uYO49KIlQ21qYCSl8Ioclf3TXQ7Ii0t0HDDy2lhaXDU8xXCznusJl96ElC3MsIYKr2X9qMOtFZzwhcoCAS0Zw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f1abe2b073.mp4?token=TDE8TnbdOWNP4aOKWqHZOVkST6q5A2mmQpIGT0_c4cxGf9OfRdyTo-lC2YbeJ9--IQU7PrmfeFUYAC4yIkx43T5-gyf6VOn3oh-DWU87NhJQ22Q9ts484qS5eTJKcZmnxTsA1qBQq0n9HndHHeni0E_r1BPPNwdm_RMyqcJhbxEhWY6HR-24s53rax5bpdB6PNTzrLHbJQBbM8AcV4O9KdCn3wcGx2TpQXpJluflAljEi48F01JAeF-iFmS_TWme2uYO49KIlQ21qYCSl8Ioclf3TXQ7Ii0t0HDDy2lhaXDU8xXCznusJl96ElC3MsIYKr2X9qMOtFZzwhcoCAS0Zw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❤️
گل دوم تراکتور به چادرملو توسط اشتراکالی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/Futball180TV/104946" target="_blank">📅 21:06 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104945">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g_xHDmA71xJAUm9FuGIFYinDvTHDpvBcDZ71GhVSLVTSNG_tOINxTfEF6iwOlh5Mj0swund9PtyV-EeXs785V3Bc0EOg9mieuYvsZjDFfkf_zdJZYH9yNIQZc7KsbzpFffEe2Px0n00Z_ehtLYayG7Mz9wDgrEzR33VboT2NJhyy3rvec8M5h25MIhSVhz86J5JVYckfDra18EqIQSatn7Vk5m6tqZdS7KGJ_58CivZD56POjY8W7prTmC9-3kz7S2FfHqTcjG-ng96q4v8LSzfynD8Yd4vvqWM7NU_ageA2dqBwVdXRiq2oUpjq1NqKWIrEi0jgf-hOJ6Ty8jW2rg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇩🇪
🇩🇪
افتتاحیه بوندسلیگا؛ ترکیب تیم فوتبال بایرن‌مونیخ مقابل اشتوتگارت؛ ساعت ۲۲
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/Futball180TV/104945" target="_blank">📅 20:58 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104944">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c2abb732ba.mp4?token=d_w0NXcBtRiDOdTJOr95ravgUyuxAR_MWxc2cY861egnWI3cCiDfzYJyoDdRDiipBtsGp745THzWxAeAIBi_mA3dD0xW0wqRalTsgWhO4ffn9k6Cewnya2jlxHAfeGXOThpT-Syj8fvaOS_ZC80YM7snGMKLGL3PO7AUwS8ei66ckq688UhOcb7sZGGXmTartRnk_Ww-jhmsdxFhPS4EMHHMqQrVNrmE-J6Ek5xkMYXafrh3nWq19cjlSyZkflspk739Pv1jl1lNOH3fOWWvP0oGnHVUtvzptnzasXPeodrfj8mPoAtOFZgmRvUe39C6vryOCku6NtZpPd9mkGzw3Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c2abb732ba.mp4?token=d_w0NXcBtRiDOdTJOr95ravgUyuxAR_MWxc2cY861egnWI3cCiDfzYJyoDdRDiipBtsGp745THzWxAeAIBi_mA3dD0xW0wqRalTsgWhO4ffn9k6Cewnya2jlxHAfeGXOThpT-Syj8fvaOS_ZC80YM7snGMKLGL3PO7AUwS8ei66ckq688UhOcb7sZGGXmTartRnk_Ww-jhmsdxFhPS4EMHHMqQrVNrmE-J6Ek5xkMYXafrh3nWq19cjlSyZkflspk739Pv1jl1lNOH3fOWWvP0oGnHVUtvzptnzasXPeodrfj8mPoAtOFZgmRvUe39C6vryOCku6NtZpPd9mkGzw3Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🇮🇷
پرتاب بطری به سمت پیام حیدری و بازیکنان تراکتور از سوی هواداران چادرملو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/Futball180TV/104944" target="_blank">📅 20:52 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104943">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/210b801553.mp4?token=I4n7XttU1KFDIUfNrNm71uUVzNHU8K4xKZbrzmis9fZaStdgS2Tq3mPy4d6cWROtZlWUkExRyzurODbgUEpzbQ81pQzvARqXmaVOmBTe0DvN2IheDDI-wMdMTivwn0VAlRYyR_ZwuLJt44sSoeD4WRpKrxHz_mi5oAbjvp3ogH8DPpsmuPwetQcVxdEsvOrTgWTEuMbXJ8_Gc3e6NI7GqxXzKQ2VhbCg3LRXq3FdbxD4QaqoG4tPKVls1YaFCxFvR3WmJe2sha3WNWuWDK6AOooVeKytgKvC4sSfeXf__XcOw-s5a_RL79CKmsbICxBSAucjmADdz5I90QbCnALkrA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/210b801553.mp4?token=I4n7XttU1KFDIUfNrNm71uUVzNHU8K4xKZbrzmis9fZaStdgS2Tq3mPy4d6cWROtZlWUkExRyzurODbgUEpzbQ81pQzvARqXmaVOmBTe0DvN2IheDDI-wMdMTivwn0VAlRYyR_ZwuLJt44sSoeD4WRpKrxHz_mi5oAbjvp3ogH8DPpsmuPwetQcVxdEsvOrTgWTEuMbXJ8_Gc3e6NI7GqxXzKQ2VhbCg3LRXq3FdbxD4QaqoG4tPKVls1YaFCxFvR3WmJe2sha3WNWuWDK6AOooVeKytgKvC4sSfeXf__XcOw-s5a_RL79CKmsbICxBSAucjmADdz5I90QbCnALkrA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
🟥
62' اخراج کلباسی بازیکن چادرملو به دلیل خطای خشن
روی بازیکن تراکتور
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/Futball180TV/104943" target="_blank">📅 20:34 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104942">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4a01cc820b.mp4?token=LkX-DFPj9gM2k4jrwlIm6dggrNTAFxJ8LGmaoKC-EjBG0x2q6fglUOepiZP7Xj2jKPfZa7Zw8TS5N7pE_QAkOPxfzq_8SNEAHRFEBGl0jhAvdlf4Z9l-NTQDvwaqncM8_mo1_oq1ow3vmNqpuB6kEa2Mbf657kmvkEOursSIJEVElhztlKIOkDJUjpxd0CMSk8W9_1t1K2OFibcX0vOFAGIdPoyGsHsnLeBB-W2dC1ek4Uzf7gjREs3MYxZgpbyHl7B40PhcN9bAP9su0G7csExoANt3nPVyKwLXzlHEYGu0TihMK8Xn_uM7u5Mb4_QuP2ooCdPaeUVVJ3rsH_lq4LMLw2HXbZEds2gLrT_w_bCqVApB2qhemz6T5vhiC3S-afAEBnBeJR92f7eTiSwoLM7oxn2KCtMgvBClawubF5NiZdiKmz5NaLlAIqsGBwMYK-Ta0cHuGoPxj7m_I1y1BcswdPJSj5nmxcOl1-8fvTILevauohc2wHcJMzuGxKKIxa6GgHklaQwCWhHEcHhlrhx6Fu2Vf411e3gMuooFi4LJWN6fmoUKxdcu4I6T_kWkmln6nXHwPAOkV-jYs3a8vONZfV2eZrpEGnP1VC0GggOUXNZGXjQdoEB3gOhMjdgJw7NjJRSEXSrjlIOy0k2ltSOU4QwyGwf_2VMdZiHJs0A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4a01cc820b.mp4?token=LkX-DFPj9gM2k4jrwlIm6dggrNTAFxJ8LGmaoKC-EjBG0x2q6fglUOepiZP7Xj2jKPfZa7Zw8TS5N7pE_QAkOPxfzq_8SNEAHRFEBGl0jhAvdlf4Z9l-NTQDvwaqncM8_mo1_oq1ow3vmNqpuB6kEa2Mbf657kmvkEOursSIJEVElhztlKIOkDJUjpxd0CMSk8W9_1t1K2OFibcX0vOFAGIdPoyGsHsnLeBB-W2dC1ek4Uzf7gjREs3MYxZgpbyHl7B40PhcN9bAP9su0G7csExoANt3nPVyKwLXzlHEYGu0TihMK8Xn_uM7u5Mb4_QuP2ooCdPaeUVVJ3rsH_lq4LMLw2HXbZEds2gLrT_w_bCqVApB2qhemz6T5vhiC3S-afAEBnBeJR92f7eTiSwoLM7oxn2KCtMgvBClawubF5NiZdiKmz5NaLlAIqsGBwMYK-Ta0cHuGoPxj7m_I1y1BcswdPJSj5nmxcOl1-8fvTILevauohc2wHcJMzuGxKKIxa6GgHklaQwCWhHEcHhlrhx6Fu2Vf411e3gMuooFi4LJWN6fmoUKxdcu4I6T_kWkmln6nXHwPAOkV-jYs3a8vONZfV2eZrpEGnP1VC0GggOUXNZGXjQdoEB3gOhMjdgJw7NjJRSEXSrjlIOy0k2ltSOU4QwyGwf_2VMdZiHJs0A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
صحبت‌های هواداران استقلال در ورزشگاه
❌
ما رامین را نمی‌شناسیم. این جام را به ما بدهید. پرسپولیس با تیم‌های ششم امارات و قطر مسابقه بدهد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/Futball180TV/104942" target="_blank">📅 20:24 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104941">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9a93dbbe2f.mp4?token=N_IAAFUSX5cwibASQ-hV-gXkK6nIaUaOJh4Jpeup7VZGUKKAvNXKno_pC-n3whYm9VwxwAuzSzZAWnUO3dRvLCB-XjmJD6qYR-AGG4MY4Ki5wvJLrva0IO6EYc2AMqgqACoajQOpj_4FA5HPLtxv_i-WYmCsR59EGL2aeQetEpM6FYJa-h4xuf03aRMYfm0OxFltQoSzLNX9VGXcDO5T_gtj5ekRmwggmPvhT_G-sZGi2wz6IFdWKP13nxMMsiSYMqQ1KyxSl2zqSkNYQ8CUU9DBAcYdJxAR_ufAUkDLxpqyD3UYyrkMrLESoDKbASndWv-AwnW2xHCqribsBqj0hQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9a93dbbe2f.mp4?token=N_IAAFUSX5cwibASQ-hV-gXkK6nIaUaOJh4Jpeup7VZGUKKAvNXKno_pC-n3whYm9VwxwAuzSzZAWnUO3dRvLCB-XjmJD6qYR-AGG4MY4Ki5wvJLrva0IO6EYc2AMqgqACoajQOpj_4FA5HPLtxv_i-WYmCsR59EGL2aeQetEpM6FYJa-h4xuf03aRMYfm0OxFltQoSzLNX9VGXcDO5T_gtj5ekRmwggmPvhT_G-sZGi2wz6IFdWKP13nxMMsiSYMqQ1KyxSl2zqSkNYQ8CUU9DBAcYdJxAR_ufAUkDLxpqyD3UYyrkMrLESoDKbASndWv-AwnW2xHCqribsBqj0hQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇷
گل‌اول تراکتور به چادرملو توسط حسین‌زاده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/Futball180TV/104941" target="_blank">📅 20:17 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104940">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RGWKMaTiz04oqy9jI74lFppwTZtqSe9IsGEFeecSMwORf_Oam6UKOPhb6SIrUnqzpF7zPEuXZxarELhQyBnwFLum8CLigrqVbVFRQRc5KDk81hySuGU1Q0hVzk3TWB_B68nR7ghZMx2n55rEuHGeZwCpLINSgxr2g-w1ld7-PEJUA1lET_eSkpeNiZnZ2fUEbWUygMxMh0CjJwWrnC0T9BuRVx0dv327tsgXVzjeBt_kFhvBONB2oDiVlzWczbTtWK7O8nhM-ag1FIiTd8wfow6YtiuQvxTElzPOinpxUm-B3C-zqiO70PoNZtI6uD9LsEacPb_xVq-_Y5nWzeZJDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
رونالدو در ترکیب فیکس‌النصر مقابل التعاون
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/Futball180TV/104940" target="_blank">📅 20:17 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104939">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f2cdd650bf.mp4?token=nXxpYXuu-fr9q3NkbiZvc7LSE-p6p-_4eW--IqCKw6STvH7TSBq4pBDFASjI4hT8paxLhFxar2nvaQ4b-Tnoe8udEuyxfasP-NGNU0PhAdEAPkyF33cvL_SsrlsQ6K5C7mVWG5leuijGw-CD7WlAptrYwOk2luLSDFbk2V8e70J8ED7t2HvrU2RQ5F9NxohWgyytoIOsiOz6xS-JZ06uYkwa-3C1iVvb9Cx0zLWacOYjHzIm0yQY8din6A0AMITuJWZB6BQz4MvkDgln7BXAKs-73_703MIpoRUXAlUjk8hvUFjxrkYscz9rYBaUz9v7yn0CyePqp-KfWxLLS6RuyA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f2cdd650bf.mp4?token=nXxpYXuu-fr9q3NkbiZvc7LSE-p6p-_4eW--IqCKw6STvH7TSBq4pBDFASjI4hT8paxLhFxar2nvaQ4b-Tnoe8udEuyxfasP-NGNU0PhAdEAPkyF33cvL_SsrlsQ6K5C7mVWG5leuijGw-CD7WlAptrYwOk2luLSDFbk2V8e70J8ED7t2HvrU2RQ5F9NxohWgyytoIOsiOz6xS-JZ06uYkwa-3C1iVvb9Cx0zLWacOYjHzIm0yQY8din6A0AMITuJWZB6BQz4MvkDgln7BXAKs-73_703MIpoRUXAlUjk8hvUFjxrkYscz9rYBaUz9v7yn0CyePqp-KfWxLLS6RuyA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇷
دبل‌کسری طاهری در بازی امشب سپاهان
سپاهان ۲ - ۰ گل‌گهر سیرجان
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/104939" target="_blank">📅 20:12 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104938">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c6ca3971a9.mp4?token=nfpcESJPcPD9nfxfD5POCCav-roEucYT1JAg_hn2kg6cLWS1cHcDHhwY4J3eHeX87o55rs2bNHBizm67wwRUB3Gxzgd2jmcrEprS4FMc1A7NO5k_C08SUhvRiKz60Jo2dDi68XdHgeJl8H1LLe5vidwbPLEzerKDlS2IvgtJxjymjGUYtZdM7tAjFYikwiCzhA1H7VCJBQrGA72ASveCorwXv7Q2NLwGnHuXxDUMEGK_vUqV56lHZuLfdgOtUClKWKN_AIPvyVz7-tk5WTX6HruCRH16dAiP4e9gW4Tw6n3YCT5W3mBmstgAu-dQH4RIbgF0ddFbj2P8H8wBUto4rg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c6ca3971a9.mp4?token=nfpcESJPcPD9nfxfD5POCCav-roEucYT1JAg_hn2kg6cLWS1cHcDHhwY4J3eHeX87o55rs2bNHBizm67wwRUB3Gxzgd2jmcrEprS4FMc1A7NO5k_C08SUhvRiKz60Jo2dDi68XdHgeJl8H1LLe5vidwbPLEzerKDlS2IvgtJxjymjGUYtZdM7tAjFYikwiCzhA1H7VCJBQrGA72ASveCorwXv7Q2NLwGnHuXxDUMEGK_vUqV56lHZuLfdgOtUClKWKN_AIPvyVz7-tk5WTX6HruCRH16dAiP4e9gW4Tw6n3YCT5W3mBmstgAu-dQH4RIbgF0ddFbj2P8H8wBUto4rg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
🇮🇷
هم‌اکنون نمایی از استادیوم فولاد آره‌نا اهواز
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/Futball180TV/104938" target="_blank">📅 20:11 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104937">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pdb74PCuzQMlOmJ9zrIEZT2zr_VYQCU4g2PY00LwJhMzB0bg4BhLB0ttyoKn8K_DVZOHbMH9C7B-_POVOicQzx4IWTLR8NpNbRWfabAFWJB1CFBT77IAfB-WVzQbYOttk7mTYaL3r1LjTNpdG0C59zL2Ut6TI0Xjuov6Q9Jao7jp_TkChx8MBBwApenEqmoXzfiC0tsRFbC-WTEIm3AC-orrMteokSwhZcMRn7sPW8tZKbqX1Wvc32mAYDxqCyAiXKvJpGp4daGuoLfb3V8pKB7t_1m2MznUm0Dv-Q9LaOM5jLM_9Yh93t9CwB7V_5JUjQUYU5LkPFSygX1pBPa_Yw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇮🇷
ترکیب استقلال مقابل فولاد؛ رستم آشورماتوف نیمکت‌نشین شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/Futball180TV/104937" target="_blank">📅 20:03 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104936">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XQNn0m15NgnBQzidE5OFkjLJNXE4UDJmGNfhVUsB80tU35elIuoC32DElpMz_bruRNsnnNodSQdQw6Lw4HI9Q3OfPshXOwZSFkt26lnxr7jfwjD4JmrivvE5Omi52mNQ5D4IGj4Tk8jo7M8UOyvpbMQsoa67dJ0TpCKHJ-dIpdMVt1pkpL9MyexOpmhBNG_7ygE0kzzTQYngADCnTkQTf-zWB-rYKkMszXybqoT2sZVJNdmFNCeWS5x5rEoOiCcTWRLpTl3TZPP5VIxp3a7Na1eoJbfl0SOWssL_c3X-lQhZixMWHsttzngvQVsUSK7HimDq0D5bOwwaQNxTXEr10A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇮🇷
ترکیب استقلال مقابل فولاد؛ رستم آشورماتوف نیمکت‌نشین شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/Futball180TV/104936" target="_blank">📅 20:01 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104935">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2b2f021f29.mp4?token=boeYZw5lVIdOmnXQlKZXMagOWWGnKz6QOZCzHtPAapF1AIQ2gZ5Htr5ggwOgfaxkbO5jJlzBbgfFNFrXE3IiQlBPF1-oYqj9CKp7j_LaUaUiUoYcbA2Vc8WKOpPxBTyX-xbRiRJsNwzA6fRQnoWMjRuSq6soZ88gSOXL9fiLoh-LN98VNsBgnNs2qcoUbVgmpbvslsm1KtU-QugSt2ePqRY9URxsWRV6DInqNThwum5xRIgl9uSVDmc18D0_4EGbjrpP2OH3ts5pnthoY9jZtx3rBe8qRxFv6c7n17dN7h5LrjoU7Oe51eyD58YcXqIMblih7_aeba5_zwsIMuI52Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2b2f021f29.mp4?token=boeYZw5lVIdOmnXQlKZXMagOWWGnKz6QOZCzHtPAapF1AIQ2gZ5Htr5ggwOgfaxkbO5jJlzBbgfFNFrXE3IiQlBPF1-oYqj9CKp7j_LaUaUiUoYcbA2Vc8WKOpPxBTyX-xbRiRJsNwzA6fRQnoWMjRuSq6soZ88gSOXL9fiLoh-LN98VNsBgnNs2qcoUbVgmpbvslsm1KtU-QugSt2ePqRY9URxsWRV6DInqNThwum5xRIgl9uSVDmc18D0_4EGbjrpP2OH3ts5pnthoY9jZtx3rBe8qRxFv6c7n17dN7h5LrjoU7Oe51eyD58YcXqIMblih7_aeba5_zwsIMuI52Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏
✅
👍
تیم ملی والیبال زنان ایران با پیروزی ۳ بر یک مقابل اندونزی برای نخستین‌بار در تاریخ به جمع ۴ تیم برتر آسیا و مرحله نیمه‌نهایی قهرمانی آسیا ۲۰۲۶ صعود کرد.
تبریک میگیم به دخترای عزیز کشورمون
❤️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/Futball180TV/104935" target="_blank">📅 19:56 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104934">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kuRqChO2zYdO5VLpc7LbbhXjrrZ2XMvMlfZyIIYS-x1ljDLrEBvh_ui-jMrSgTu-GyM48ya-YSTYa1rIfKnC4ykUrolOs5A3FFp2HhwVKlApvL29aChgj7Sa0NQ-_vtp4Eeig2R3cutcLonaDC6C-WJoBqraep-qciqjPe2qW11C730RLKaqby1IQG1CLJfVk4PEChoOlGGFKJ9iUbramb71EEhvdXOrtgAj0f228_6ivOLDOOnRx5VzGmoA32o-zzoSG67WIxXBosVVkcT7wpEw6-qmf7oDrmB6Qzj5AcMwo6KIgE3TK_qLipSX3oxtMWWr9SavpUcRVzsMwP8WyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
ترکیب فولاد خوزستان مقابل استقلال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/Futball180TV/104934" target="_blank">📅 19:51 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104933">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ded8751287.mp4?token=SxSt4VOoNjjUZ-MY703i7TWCk6OM_3yGS3wBqXK9tkRH2FUmggf9w5FjyOSY9ifGJ_hqFiEObc8UFbpM8L0RfUZv76Z7oInO6R8MrEP1XCP35NNLO98tUsVSTKVOodtw73gCBGAcF_NKvQoIYuIjP5cCLKdJHLGm687YVUnjaIfihk_z-5iQ3DQVjuajKC7Ld4-nfKDtX7Sf9QbD4DEcO2XR3v7uv02cOd1pqqLtcOXItHuXogp2S2xPIkgev7OpUbz9JtQnIIffjVCi5DCTufyBJY6NVZHT_zgRKaD1RYmd3met81tNI6zHiVfph7bG7Va74Vu-htOQEzZdtYk-Lw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ded8751287.mp4?token=SxSt4VOoNjjUZ-MY703i7TWCk6OM_3yGS3wBqXK9tkRH2FUmggf9w5FjyOSY9ifGJ_hqFiEObc8UFbpM8L0RfUZv76Z7oInO6R8MrEP1XCP35NNLO98tUsVSTKVOodtw73gCBGAcF_NKvQoIYuIjP5cCLKdJHLGm687YVUnjaIfihk_z-5iQ3DQVjuajKC7Ld4-nfKDtX7Sf9QbD4DEcO2XR3v7uv02cOd1pqqLtcOXItHuXogp2S2xPIkgev7OpUbz9JtQnIIffjVCi5DCTufyBJY6NVZHT_zgRKaD1RYmd3met81tNI6zHiVfph7bG7Va74Vu-htOQEzZdtYk-Lw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
گل‌تماشایی خیبر خرم‌آباد مقابل آلومینیوم اراک
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/Futball180TV/104933" target="_blank">📅 19:44 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104932">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6fddb9c4e6.mp4?token=VUa_9muXNkKRH8o0CbXgOV2MYuWiLD8YppEIoFMqS-_cLL7nEwLhHJK3VrDKhquhYnxQ5jd9SjqoD09VhflnkvovGGEQTB8anQTVF1g-ho8pVkdmes1oBbUvI6wv3SGGcq5BtvAqYRKLZkZkKfUCX-pRstLVoqkm7SIMPlm1PxidHqgpYWysAeVrathpBA3ES798iuxCrY8PmKfspipw7pmhg7qUXhBCrdKAEzIC4KTYSwDFRHZaNA06SPfXEnuDqRvsMQnnuigjp6cGJGWrydaCO8hQssOtoJy-yt77_hR3MCa4t17gxQXbCqFk98K6gRORaK9s8Iy99vXh6ciKkA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6fddb9c4e6.mp4?token=VUa_9muXNkKRH8o0CbXgOV2MYuWiLD8YppEIoFMqS-_cLL7nEwLhHJK3VrDKhquhYnxQ5jd9SjqoD09VhflnkvovGGEQTB8anQTVF1g-ho8pVkdmes1oBbUvI6wv3SGGcq5BtvAqYRKLZkZkKfUCX-pRstLVoqkm7SIMPlm1PxidHqgpYWysAeVrathpBA3ES798iuxCrY8PmKfspipw7pmhg7qUXhBCrdKAEzIC4KTYSwDFRHZaNA06SPfXEnuDqRvsMQnnuigjp6cGJGWrydaCO8hQssOtoJy-yt77_hR3MCa4t17gxQXbCqFk98K6gRORaK9s8Iy99vXh6ciKkA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇷
گل‌اول سپاهان به گل‌گهر توسط کسری‌طاهری
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/Futball180TV/104932" target="_blank">📅 19:41 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104931">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f4b835e745.mp4?token=HDiu5B9f3I9C96PQL-NrD6aubBZZqADwD6CCUEqLjziSwvdXcn74aWsDeLYXCT6Ttxsli5jnJZyjl64AFcCx6rj3BrmAGcH3yV5zqf9UV9mxvp56pk7k1-4C6M8qvG0mXEISK1qI6eTGZyKGQjrIm2Dr6VIb_GLbH_vpmHhRw-Hx7Z1aJxDiPygUpOCwt7oy4nNrdhGcG1ZSQQ1xP29AwXM0aNfJZTYygdKnhBU444v0swAqyuXYQeA0XiwY_9Ip6t5HiF7ZvC8Nzso0H0WDFC6iKhhpo9Csl7fut63nSCieEc1ak_WxJbAwSeXHailTQDhwTB_h_7Z2byduZ7qsyQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f4b835e745.mp4?token=HDiu5B9f3I9C96PQL-NrD6aubBZZqADwD6CCUEqLjziSwvdXcn74aWsDeLYXCT6Ttxsli5jnJZyjl64AFcCx6rj3BrmAGcH3yV5zqf9UV9mxvp56pk7k1-4C6M8qvG0mXEISK1qI6eTGZyKGQjrIm2Dr6VIb_GLbH_vpmHhRw-Hx7Z1aJxDiPygUpOCwt7oy4nNrdhGcG1ZSQQ1xP29AwXM0aNfJZTYygdKnhBU444v0swAqyuXYQeA0XiwY_9Ip6t5HiF7ZvC8Nzso0H0WDFC6iKhhpo9Csl7fut63nSCieEc1ak_WxJbAwSeXHailTQDhwTB_h_7Z2byduZ7qsyQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✔️
دریافت جالب و دیدنی پارسا مقصودی لیبرو تیم ملی والیبال زیر 17 سال ایران در دیدار نیمه نهایی مقابل آرژانتین
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/Futball180TV/104931" target="_blank">📅 19:19 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104930">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d3b2bd316d.mp4?token=qx3ZkGyZwtXI-ps19Oj2L3K3WtCPoi7S20Y-st8z7zQHhODNlYGTUeIzbzD0Aik29Wk2DF-F0eTWHbnrAXw4AjhOE3-ASNcZeVYyfGzJjaS_nPdsSfaZTB2-0DeIV6y9IXZZ1cvl4EZqZs7ZLp9Uw5f3qGjf8EqzYm07knMnbtIzAFjldDRc0F0oQNGrDtA5IKlbRJguPcxgE1RSIxxTnlG-vXvxO5XajQfE5HCYkaaFd1OjjvPxwMfvx6TA6bopJxIxvvfaVwCxI-93xln8EPhVWLmNHBtjwzS2yNw_M-_Y2A_sW46gpT4Hkgi37wWbHXNu0kz58XpXQux8BTHHTQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d3b2bd316d.mp4?token=qx3ZkGyZwtXI-ps19Oj2L3K3WtCPoi7S20Y-st8z7zQHhODNlYGTUeIzbzD0Aik29Wk2DF-F0eTWHbnrAXw4AjhOE3-ASNcZeVYyfGzJjaS_nPdsSfaZTB2-0DeIV6y9IXZZ1cvl4EZqZs7ZLp9Uw5f3qGjf8EqzYm07knMnbtIzAFjldDRc0F0oQNGrDtA5IKlbRJguPcxgE1RSIxxTnlG-vXvxO5XajQfE5HCYkaaFd1OjjvPxwMfvx6TA6bopJxIxvvfaVwCxI-93xln8EPhVWLmNHBtjwzS2yNw_M-_Y2A_sW46gpT4Hkgi37wWbHXNu0kz58XpXQux8BTHHTQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇷
سکوهای استقلال در اهواز تقریبا پر شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/Futball180TV/104930" target="_blank">📅 19:14 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104929">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b980e101bd.mp4?token=IS2A8SlVBACDzzqdC9qJNwTNXCup91jokJYeKAgaHG6Nr7cZbZvaXcFJpPCGRg2ga_dFlqAg22rPYnfPwYGg_4P32FT-apEM3dTOYASoc0Kd-en_lzDAGM31KIm6Fh_qDC8Kv9U9SZ9vQl5C0PIQTvRVle16gPvS3EufJbsw4iNHpHRWSklIrk9mZqPRpACsZxv-FujVx0RnY1YH24NecKFzf8t0Ugf5o7lErZ3NgqKUZD0_lhlqxAOwC6ybgRgpD5WEAlqCQD8ahay0shwPWIWnCPLSf9ARod1Wl6aqIG5zkkWq-zNL9M3-r-IJNLL1ggmJWj1cjwN61Ieaj7tJCg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b980e101bd.mp4?token=IS2A8SlVBACDzzqdC9qJNwTNXCup91jokJYeKAgaHG6Nr7cZbZvaXcFJpPCGRg2ga_dFlqAg22rPYnfPwYGg_4P32FT-apEM3dTOYASoc0Kd-en_lzDAGM31KIm6Fh_qDC8Kv9U9SZ9vQl5C0PIQTvRVle16gPvS3EufJbsw4iNHpHRWSklIrk9mZqPRpACsZxv-FujVx0RnY1YH24NecKFzf8t0Ugf5o7lErZ3NgqKUZD0_lhlqxAOwC6ybgRgpD5WEAlqCQD8ahay0shwPWIWnCPLSf9ARod1Wl6aqIG5zkkWq-zNL9M3-r-IJNLL1ggmJWj1cjwN61Ieaj7tJCg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇷
🇮🇷
آغاز درگیری‌ها روی سکوهای فولاد آره‌نا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/Futball180TV/104929" target="_blank">📅 19:11 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104928">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f5f2a045c7.mp4?token=eCRqQp0ijMWu4vJ-JGPwsdTVbKlzckBv_Mecxli9oJtXjrGkTQNxfGEEyXritipK3kmgK4kqdutrt6O9d9CBZa4yYbMeDRZP9JM-XS1fu8Z-bQbapJOzlpYZeDXxRjvHvbjyES_r5YIfYJs_MimFw2aJcr451V9XizzX9AhaeBqilfS9nS4gdRsJyR7wT8IMWp4YWd2geew0XKtLGOCbnYkXeIfBkSO8QaKvatngFflxX3CaR7CKqcSeh6NQiSi_Ma_h89KnC0SPc07K8WTCHDxbdrcFN2dwtDcV7alnW4oRqR96P8pARdWarDEBzDuhd-8h2X6zDBRoIsrCPyK29w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f5f2a045c7.mp4?token=eCRqQp0ijMWu4vJ-JGPwsdTVbKlzckBv_Mecxli9oJtXjrGkTQNxfGEEyXritipK3kmgK4kqdutrt6O9d9CBZa4yYbMeDRZP9JM-XS1fu8Z-bQbapJOzlpYZeDXxRjvHvbjyES_r5YIfYJs_MimFw2aJcr451V9XizzX9AhaeBqilfS9nS4gdRsJyR7wT8IMWp4YWd2geew0XKtLGOCbnYkXeIfBkSO8QaKvatngFflxX3CaR7CKqcSeh6NQiSi_Ma_h89KnC0SPc07K8WTCHDxbdrcFN2dwtDcV7alnW4oRqR96P8pARdWarDEBzDuhd-8h2X6zDBRoIsrCPyK29w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇷
‼️
شعار هواداران اهوازیِ استقلال: فولاد به شهر ما خوش آمدی!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/Futball180TV/104928" target="_blank">📅 19:08 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104927">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pvg5hWCko1hH12Vdin87Qih__d68-wP5S88XZ1Eeeh5L60KlTsdbhEKwoCP252MPAeLsJ7M60QxsRfYQ2EKSDZ5xxLAKCY5balK0ahrQrJbuWQ_9EDujbcZAeXRMHNaG_pvxeEvzsN-RiPtMN9N77BI5UC-yLDbyawlQQ_XIxrM4PmZOOAc7CYqBHUvhLyx8Y1HrtCRjP3Ekt_JPzS9o8JP4bbO-kX_g724ZTl3TDXASaT4hOvh9VubCBa6UpPdNsIxxM_mydMX7wjvn8wzo9w7pEdRLMh4ca028cjMQKTs9ajqaDRRGBnwJDR3aWpzT2McVj0mbFGz7YsyByDdcgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🗞
#فوووووری
از رومانو: رافائل لیائو با مبلغ ۴۵ میلیون یورو از میلان به گالاتاسرای
HERE WE GO
✅
✅
✅
🔥
🔥
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/Futball180TV/104927" target="_blank">📅 18:51 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104926">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/04a994664d.mp4?token=mwIHJV7HHzdU6vB15i-oTMqNZzWObYRlgrktY6I_JO44eVZE_inLuSwCA0MspMvvFOtUTHh99rUUcJS-6aN95ODadoybsWHgMNParw2KadgwYexXGUs1Qq-M2Hs9tUkKK3dYr0EMAJiNxvW8VjS-wvMpLNKUMGtXJiHIXbju5a5nh3-Lxkei7u3TFWNK5BEzJzG54rm-5ha0K9MhUQXTLpeywYAa3Eovk8OWSdAOyC7GqjYvxV1Z7kVDgkfis7JOJtasO0-7_tUl3TSx1449aD2O8muU0it93MFWubIOrF2Sawc046GI6A0xOIgDCp404Fsl6qFfHrs66braC7O80g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/04a994664d.mp4?token=mwIHJV7HHzdU6vB15i-oTMqNZzWObYRlgrktY6I_JO44eVZE_inLuSwCA0MspMvvFOtUTHh99rUUcJS-6aN95ODadoybsWHgMNParw2KadgwYexXGUs1Qq-M2Hs9tUkKK3dYr0EMAJiNxvW8VjS-wvMpLNKUMGtXJiHIXbju5a5nh3-Lxkei7u3TFWNK5BEzJzG54rm-5ha0K9MhUQXTLpeywYAa3Eovk8OWSdAOyC7GqjYvxV1Z7kVDgkfis7JOJtasO0-7_tUl3TSx1449aD2O8muU0it93MFWubIOrF2Sawc046GI6A0xOIgDCp404Fsl6qFfHrs66braC7O80g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇷
‼️
شعار هواداران اهوازیِ استقلال: فولاد به شهر ما خوش آمدی!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/Futball180TV/104926" target="_blank">📅 18:48 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104925">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NetBhn-3UNb0DAcNe4Sw-VwFzI4xafonK9Yxv2VR_-ll0c-FMcHFLWrcxL5WiCmse-OV2NDubk0tqqym-MN3PM2zjmnc7I02a129quheNrXJsC2uJa1vb7QMy6KR7EvtCVfn1bb8RMP8yY7Xe7m2xgxzdLnJSqwY6pDhmHTjrH8F6essbEUvtBO5GJByWLI1OhkWKf8Zej215IXNElYwpbBO4DDI4zR0i1PjQh_spnh-TbmliPGrcrX72et1M4Jsvql5hDuSg9YDRl87o3mMqWhM86O3e9OjqHO15DkJ3xYlwrxtj6MGpEwV5_PyAupNHPveRlcKy_EwaTiQGKDRkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
رومانو: ابراهیم امبایه از پاری‌سن‌ژرمن به استون‌ویلا پیوست. مبلغ ۵۵ میلیون یورو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/Futball180TV/104925" target="_blank">📅 18:47 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104924">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c31b21a19d.mp4?token=aJEhvQaRaHnQZfM4NM4TLl7axrCLlzZkfp5VXxJIqKqB8dyPB2DjxmSSV8jLBjAVzWG4CxoHUjqnN1VhAeLBy5yEsLolq6E8ZKzvaN1hkvbcZsJ4_Y44yKAVlUPDRTy-MLi55sfe4Fm-LX_3BhlzKP1vQffK3-5Wi1iipgiD8Gfm6SUUObrVaTSiUZ4qn-nKrMTXRgsrB9C9gE335lHYUYILhanfH4Us6ITUJ6Bu1jMSQ6AgntTja2cTCuNRnui4a6pgtEJSNyWieD52GvXn_hv28BSOxb_Zq8fIQ3laTCL2gpcQYnw0uJ2yLUBtEIxOjEiwmu-8KEGFMBfWC5f_Tg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c31b21a19d.mp4?token=aJEhvQaRaHnQZfM4NM4TLl7axrCLlzZkfp5VXxJIqKqB8dyPB2DjxmSSV8jLBjAVzWG4CxoHUjqnN1VhAeLBy5yEsLolq6E8ZKzvaN1hkvbcZsJ4_Y44yKAVlUPDRTy-MLi55sfe4Fm-LX_3BhlzKP1vQffK3-5Wi1iipgiD8Gfm6SUUObrVaTSiUZ4qn-nKrMTXRgsrB9C9gE335lHYUYILhanfH4Us6ITUJ6Bu1jMSQ6AgntTja2cTCuNRnui4a6pgtEJSNyWieD52GvXn_hv28BSOxb_Zq8fIQ3laTCL2gpcQYnw0uJ2yLUBtEIxOjEiwmu-8KEGFMBfWC5f_Tg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😆
😆
😆
امان از دست هوش‌مصنوعی :)
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/Futball180TV/104924" target="_blank">📅 18:35 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104923">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a984f5caff.mp4?token=oCqtRFUGriTOIn32a2zJMsgVmvUVMqbTrkc3AZZaNt48Nrhva6crgZOpiSbTSs8Ji7taGUrPUJKBASqsd2JTVORcB3vNnli5afjrQlUZ6uRuem5KEGmo_Zt5BYtIPhSbjnk34szI9dLUj9MV1vFQpEIg-LdHBi7kqkrAUAebnVEg_VN6vats4A7RiD4lbr6ysKkFcRhZu3nSi3NDlF0pkyP1mTq_RKXN-XxYv98Y0yM6y3GGVPZXzWu9R8F_-Yf-841TJPUx25fIfp_ypbh43r3UV18TQc08HFcn7f895F8lBGTooPwBjNQfyBHbz8Vy8HjmHC_PIg_O87v4VxCgoQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a984f5caff.mp4?token=oCqtRFUGriTOIn32a2zJMsgVmvUVMqbTrkc3AZZaNt48Nrhva6crgZOpiSbTSs8Ji7taGUrPUJKBASqsd2JTVORcB3vNnli5afjrQlUZ6uRuem5KEGmo_Zt5BYtIPhSbjnk34szI9dLUj9MV1vFQpEIg-LdHBi7kqkrAUAebnVEg_VN6vats4A7RiD4lbr6ysKkFcRhZu3nSi3NDlF0pkyP1mTq_RKXN-XxYv98Y0yM6y3GGVPZXzWu9R8F_-Yf-841TJPUx25fIfp_ypbh43r3UV18TQc08HFcn7f895F8lBGTooPwBjNQfyBHbz8Vy8HjmHC_PIg_O87v4VxCgoQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⚽️
امیرحسین صادقی: مطالبه هواداران و پیشکسوتان استقلال، اهدای جام است
🔺
یک تورنمنت شاهکار را به فشار باشگاه پرسپولیس برای سهمیه آسیایی برگزار کردند ولی وقتی به استقلال می‌رسند همه تغییر می‌کنند/ هواداران از من خواستند پیگیری جام قهرمانی باشم/ احکام وقتی درباره استقلال باشد زیر و رو می‌شود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/Futball180TV/104923" target="_blank">📅 18:18 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104922">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/877443a39e.mp4?token=H2wT-GXuq3banOZ9APoqkVMImu_uOA0f-Rm8xDWc1WcUxB2pcZCjtBu7TnMn58YAZNhGB_i6_eMhalqQi3QxvalMjVLdvkAFJUoOLsmuChNLO0TpEoLTejsdpN2Llvnqg6rKU3uMta6HuVcqFuNvKMhi3e0Z3ZaQKf6G4rvbJcd46CNB-6tK9lw051LYEyRTfVdRAuN52FHRXsZiBXRedUeXOv_7aQ1BLhpXr30-XtqmxsCxeuv0519zWlf1ZM2PmSkegxizRAGlH29LT82JTDw2zoVfkjL97z7_r79uYD43sCo7wxIZ8ShdfLZ2qs2fgyKwDkF3BaRB82vqSj8GlA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/877443a39e.mp4?token=H2wT-GXuq3banOZ9APoqkVMImu_uOA0f-Rm8xDWc1WcUxB2pcZCjtBu7TnMn58YAZNhGB_i6_eMhalqQi3QxvalMjVLdvkAFJUoOLsmuChNLO0TpEoLTejsdpN2Llvnqg6rKU3uMta6HuVcqFuNvKMhi3e0Z3ZaQKf6G4rvbJcd46CNB-6tK9lw051LYEyRTfVdRAuN52FHRXsZiBXRedUeXOv_7aQ1BLhpXr30-XtqmxsCxeuv0519zWlf1ZM2PmSkegxizRAGlH29LT82JTDw2zoVfkjL97z7_r79uYD43sCo7wxIZ8ShdfLZ2qs2fgyKwDkF3BaRB82vqSj8GlA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خریدهای جدید بارسا دارن از حضور در این باشگاه کیف می کنن.
😍
🤩
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/Futball180TV/104922" target="_blank">📅 18:04 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104921">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/Futball180TV/104921" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/Futball180TV/104921" target="_blank">📅 18:04 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104920">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UjaBdnis85u4NyfsECo8mImW7msO4mFpG6Y9PSp4cckAMFpp5QWkOLNkjaasDgGXdWqb6RF5yDE-29KmXTdLrzE-3tz9-oCZiqQKGjem6JJA8u0rkqtuenruf538YnWLcbs-uHbE-x53L6Z8KAaiAHPjElHWg_YJDEMIxmMH2ypATzRh1B5jO9s6j24KNTgrfB2S73P0DuYc3nzefJczhAwTfsWwCj9tirXsoJXJTi__9_Izh_8MDGpzKmL-Z4E5mm8gzbfJpGqVBYIASETBg0OB5Aj2tC31R7yZzmOS8BCmnGAZe1UseviT49Ph3FamYAbDGk-5glfu7Dhcb96PUQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/Futball180TV/104920" target="_blank">📅 18:04 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104919">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pHJe9EcoXKV0HzDaXln-RZbwzinyuFql_AjW0rnQRv26kDQ6TOBXBkwqCQtvMk7oD8SB1zTg9bIBjOvRnc9KrDMsmigWVX71UYlzZB9mNknUAZBGEqxurbEHPdDDrFU4-pvdam_1CP0iPgnlLe9qXdITGd_H4OLkrORsWfJ5cTkTHhXNGsPAhvhpw9W7rBudpwwjDT5WJRBwUzh90gOa7NXFNlNCVR85vEu0DwzZcXVIcry67Q5_L1UoOWFNsUjhfxy90NwVFdky_zjUUnxrU9075IKS-35dq1DlIMB9ssjWLq5SA-46MHN6r-3qyQ4-2SpmRFZ1eP8o7VmhfQEQpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
ترکیب تراکتور مقابل چادرملو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/Futball180TV/104919" target="_blank">📅 17:49 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104918">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/146c8ac859.mp4?token=NZIwDfU5jjq0u5H6mYrrft6ipZB80YqXHlois-XNACPlLXob3mCuzIzY1KKuhTUjdh2MslPYwHJICiGyObYK_eGjDXwuQQvtABNsDlmO8nVebzeLaEiDeK-ubeGRwXwBKKMSxvgIvRGwIeI2mJDRYyOODegtLDYrcDz2WbR9dQ-D6BUmYkxeTX-BsJn3pvLSj7g1ZL_10i6r8r6uovzLgyws4xS95QhhOBi7NoOzWisFQOievs0ShFfdTFScUD_xMNklgXLNymPFEJuY1v7UyDO9UMBwjzkY4dlFDvMHkrcqT5ln3kpGkqTGlrDt-kgESarmt8OjElDjHN-D5FHdwQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/146c8ac859.mp4?token=NZIwDfU5jjq0u5H6mYrrft6ipZB80YqXHlois-XNACPlLXob3mCuzIzY1KKuhTUjdh2MslPYwHJICiGyObYK_eGjDXwuQQvtABNsDlmO8nVebzeLaEiDeK-ubeGRwXwBKKMSxvgIvRGwIeI2mJDRYyOODegtLDYrcDz2WbR9dQ-D6BUmYkxeTX-BsJn3pvLSj7g1ZL_10i6r8r6uovzLgyws4xS95QhhOBi7NoOzWisFQOievs0ShFfdTFScUD_xMNklgXLNymPFEJuY1v7UyDO9UMBwjzkY4dlFDvMHkrcqT5ln3kpGkqTGlrDt-kgESarmt8OjElDjHN-D5FHdwQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
🇪🇺
لیگ قهرمانان 26/27 قرعه کشی شد و تیما رقباشون رو شناختن.
👀
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/Futball180TV/104918" target="_blank">📅 17:45 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104917">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4f229668d9.mp4?token=D8WiKHL37BF18A8BhC794g544PpBG4qn13NUfTEsrAeOPJmFqlvGr7OScqZWycRHYcISNhHILg9C3aYyUctSw_nyfWmdWCSzr2owS3UAJoqoEHOHr_HfaPH_zcXAqKsJta5Kd3ITdXwVj0DYsxV-xYjbkZczzAyV3fMcC7t-JewzQS7K-hAMklpR2zS2QdUwODdQEzzDuWd4HV-ZtVekkdOOyneNZSAkbhewhznddZ83L5XDUod-aXPdtCZVDpRcNPozt3oxFahq3b4zdLVZ-CW_fzjKhugk5P1RxMX06f0CMK_A9ia1aG0-KasuwLGnxEw_j3EnF2MK52AHUv9g2A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4f229668d9.mp4?token=D8WiKHL37BF18A8BhC794g544PpBG4qn13NUfTEsrAeOPJmFqlvGr7OScqZWycRHYcISNhHILg9C3aYyUctSw_nyfWmdWCSzr2owS3UAJoqoEHOHr_HfaPH_zcXAqKsJta5Kd3ITdXwVj0DYsxV-xYjbkZczzAyV3fMcC7t-JewzQS7K-hAMklpR2zS2QdUwODdQEzzDuWd4HV-ZtVekkdOOyneNZSAkbhewhznddZ83L5XDUod-aXPdtCZVDpRcNPozt3oxFahq3b4zdLVZ-CW_fzjKhugk5P1RxMX06f0CMK_A9ia1aG0-KasuwLGnxEw_j3EnF2MK52AHUv9g2A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌐
🇮🇷
صالح‌حردانی کاپیتان خوزستانی استقلال از هواداران تیمش خواست که امشب در بازی مقابل فولاد حتما در ورزشگاه حاضر بشن!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/Futball180TV/104917" target="_blank">📅 17:14 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104916">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vczlpBxcUB0CAJfL10qofNlfE3igHcoIykOfevhr-lmGyjVwJ5LJpVKU1T6sz2yGFtDnepcnq6qUnaREl_bTeQPdqohmHK3Sx_ZLBM4qdJU9C2dHNGKKIchdLFYksW3Jd2ZiStlNGUtgJoFWZ7-PULAfEh08eDC3y7WpprupEmKjixYe6mIw5q2pYuQ28Y9a01BooZIE3euXP7ep0fBHkrW8fbTdFj7p1UdoKV1l6nODvtlgSGFWZgsAhLAmO4xBikfuwptU2U6LZNydFNYrgwCBS3nu04lMiDLtNjarcHolsSxvgEF4dc_l4ZtppTuSaAEaWJbkLPfyTAdnfpWOvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇪🇸
‼️
کادناسر: خولیان تصمیم خودش را گرفت. حتی اگه اجازه خروج نداشته باشه، هرگز به کمپ تمرینی اتلتیکو مادرید برای تمرین کردن برنمیگرده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/Futball180TV/104916" target="_blank">📅 17:07 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104915">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7ef920f58a.mp4?token=VMRijoejTzfgEKCE_BffBNAprh5pmaG1Ov_YWsgxU0V9SAelgA9iy27Mc8y4VgDPmCq_nJY6d3UGf-YvwcW1uu-hOqi4vusuKfiEwZBwPysQQ9OlMu6Mm6VQGanZ0-QQFICFKVUaFenxLeSg5ZUn6VA-NUca84YUMu_CZVpxeLDecW0q7g8WkS9TeaTRkyVDltVzMak7R_kotLnXrlb8okm-Zn8-NeTaQyS2PUZEv23zFJWuWXq2YbZPk1ljjof1xr1CQao_hHc68Q2kuZDVrNcyJaVoZZ6TiRTpjxAw2nE8FYzMMkoXBiTE4AFGF-Q7c0pvsO2PrExf6D8r7o-VNA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7ef920f58a.mp4?token=VMRijoejTzfgEKCE_BffBNAprh5pmaG1Ov_YWsgxU0V9SAelgA9iy27Mc8y4VgDPmCq_nJY6d3UGf-YvwcW1uu-hOqi4vusuKfiEwZBwPysQQ9OlMu6Mm6VQGanZ0-QQFICFKVUaFenxLeSg5ZUn6VA-NUca84YUMu_CZVpxeLDecW0q7g8WkS9TeaTRkyVDltVzMak7R_kotLnXrlb8okm-Zn8-NeTaQyS2PUZEv23zFJWuWXq2YbZPk1ljjof1xr1CQao_hHc68Q2kuZDVrNcyJaVoZZ6TiRTpjxAw2nE8FYzMMkoXBiTE4AFGF-Q7c0pvsO2PrExf6D8r7o-VNA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مجری شبکه ورزش : دوست دارم عادل برگرده !
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/Futball180TV/104915" target="_blank">📅 16:55 · 06 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
