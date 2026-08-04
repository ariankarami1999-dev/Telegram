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
<img src="https://cdn5.telesco.pe/file/PR7HEnNfexSLnQAMZvN-2xy4IoABrpSMe3yAJY7tPm6wdlkTDWODgbJBa4-SYabZKT-vqnG1VXcTsYht7YCunyJ5ZOPq-BKGBKqflXqH8LqgbxoXayHnio_JTKaVV_08xBUvl8lyKmNI_5zt8qB510MdyIC2rWIhEwK8D_ftUFBhpUnB7l1-VeGDN369_TnfX4zZRHmbT4ve5gv3fOtLfnBmc4Cpr6OL5_0Dsqb6iuzGychrdCrMibk2Om6E8eE4UTR32BFDqmQ1PMLMA705dluSU37PYNmK8VxNOoO8Waf_WTOir4-82tmoMAGGQ9io_B30UBmqz_zpCa69chAZFQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فوتبال 180</h1>
<p>@Futball180TV • 👥 496K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-13 19:37:34</div>
<hr>

<div class="tg-post" id="msg-102704">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ISxYPZRyLEnyjoegFslWzIXUmbgdmZhyjS0NU54cj-Q3oTVtFW440Ovl9gSQeqCdJvEvc4RmMXKbPTPrqhOJnb-VunjPrEbxKXsjuVsRz_qsIoqYAUoCJZo69aYDE-6d6Em0xYXFKmEpp0jAv5sCaTJu-rh_5qHv72rNzQkRBGo_XXaku7jjEDShBB44ShT8gWGt-t2XjVZ64NDZ_8U8i5UlLSL921f3GiyY2On6YDVv-veRJ9_bSkyOjGbRZ2SCkTwDF5H121p5CGaKNvcn0vAwxApR1h9o_sLHXg375D2RNqWzLDZshWnB8uPquI-4t3Iby_4DJ_eGVXiVrH1KKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📱
👤
پست جدید خاله جورجینا در تعطیلات
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 1.22K · <a href="https://t.me/Futball180TV/102704" target="_blank">📅 19:36 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102702">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rc4YbGMVcNPeLSzeRaspAHQHIsez-55Zylyjl-3fEFmo2-qN_FZRYRVHoLaAgpYxFiodpx291KbBGpfX3gOcKfec0hxFzqU7wLmI7Yywds1F9VPVp7PUVdiu7nG6ATHGZapqTdb5hVn0pafdreId7UIF71nYXjIfSfA_28b_jRI2OQx5r09YCdnl5czAVe1zBYf6BfDvkTHrYhMd1lGjSkhFyHyj0abZCFabO99qOqt8Gxmk_joHBvhStYxARdMPRiVmUY1FAzMnCPd-d2DN5Q6I6dI6nRlQFWclO1TEx_vWfZkidEL0hz9cyGsj9PdX0ujfylSuADQtNidSBd8r6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/K8lxRnwBA5QHIglGFVopTlnKNKI1jZOsaLYYDD9OPK_a7qXGuaEH6i26K-b6LKHtgRackHu3yWqfg9iSoR1tQc8mkuuZQGIBSQXrk6yIHCQW48uE4kyR0hzCxzCbarAdb8RcuUjLANYO5Zut0EHZvAh8KnvhgCW2pQA0mz3hbOB89PFDve3u92_iAXwnd7t0IsayFAm8EwHRKfiliCrvcgU9E3NvgmPwg3o1eOmrJoC9S_1t-OsUPhf2gbTKwK4r3k52yUST7TylzYR2OWK4zQs6YSwZ2OgTk_gtc7x2WOmiAN9_ftPNQdDCx6ZTkMneFhzTcIX4SuVZWt1YR894vw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔴
رونمایی موناکو از کیت سوم فصل‌آینده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 1.83K · <a href="https://t.me/Futball180TV/102702" target="_blank">📅 19:33 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102700">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/94b7db1a6b.mp4?token=h9V90l693rzxXz3iPx2QvHOFDU7_7hbHCwC1dTADCa-ybQROC0JHPbxX7x94Ew9T5v_4gmWjYyJxytH4gnrq67skWzqdllK8oegwJj6bZMXQoxe7oUaIMOM6ptr51_EtgYmpci3FzOWeLnnqWv_cPcUSIIFLJdFCcOm-WiIF6u0kLUYmEUHyTJwG0oBvCDGVXRcTvaZzdynHOrExtFRGLuwL5XV0gOoKLjTaKxP5N_0XFQdPr9IhZ83TwQptxtyv-wzMDHHfhCAsS1iOhAetQEOxFIp4TLJalQ_bq_ohSUFcnUl8sCAigAwvb7TPY50mySoyU5xfcJmCfBUBeNxqwQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/94b7db1a6b.mp4?token=h9V90l693rzxXz3iPx2QvHOFDU7_7hbHCwC1dTADCa-ybQROC0JHPbxX7x94Ew9T5v_4gmWjYyJxytH4gnrq67skWzqdllK8oegwJj6bZMXQoxe7oUaIMOM6ptr51_EtgYmpci3FzOWeLnnqWv_cPcUSIIFLJdFCcOm-WiIF6u0kLUYmEUHyTJwG0oBvCDGVXRcTvaZzdynHOrExtFRGLuwL5XV0gOoKLjTaKxP5N_0XFQdPr9IhZ83TwQptxtyv-wzMDHHfhCAsS1iOhAetQEOxFIp4TLJalQ_bq_ohSUFcnUl8sCAigAwvb7TPY50mySoyU5xfcJmCfBUBeNxqwQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😢
مطمئنم شکیرا ومپایره مگه میشه آخه تو 50 سالگی اینجوری باشی و با 30 سالگیت فرقی نکنی :)
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 2.44K · <a href="https://t.me/Futball180TV/102700" target="_blank">📅 19:31 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102699">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/abd0cef8d4.mp4?token=pyqH_vA2Dacvponh4AHC-E35Cyhn7BlpsgIYxczEN-i70bkalXjar6G2cEF0DG6oWEufq8dDIrDzlnWoeO-aszDDEEJZenjv2XAIZnsh2X8ifdChD42fMGpsqxhl0FWe5l7q8QpH4Y0U7DEdsmRlDSzlUlLa77dPzUPmvJ4Yda8Ji2J7ciZP_Stam0yqSBS5ZM5mWthq7a7bqpL-K5jwKCdGRGqgwAVCMLN2jFgMVRgfLJvePfivTHE_TYer9UVuNeahBgUxTqWWYQx6a-S5hDu7dg3d78qpeYLGjYgRmNAWWvbwZ-BIXJNCUdE-DhkG0ALOUAw66X8iBHEpsifssw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/abd0cef8d4.mp4?token=pyqH_vA2Dacvponh4AHC-E35Cyhn7BlpsgIYxczEN-i70bkalXjar6G2cEF0DG6oWEufq8dDIrDzlnWoeO-aszDDEEJZenjv2XAIZnsh2X8ifdChD42fMGpsqxhl0FWe5l7q8QpH4Y0U7DEdsmRlDSzlUlLa77dPzUPmvJ4Yda8Ji2J7ciZP_Stam0yqSBS5ZM5mWthq7a7bqpL-K5jwKCdGRGqgwAVCMLN2jFgMVRgfLJvePfivTHE_TYer9UVuNeahBgUxTqWWYQx6a-S5hDu7dg3d78qpeYLGjYgRmNAWWvbwZ-BIXJNCUdE-DhkG0ALOUAw66X8iBHEpsifssw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خاطره خنده دار پیمان حسینی از عکس گرفتن با دخترهای بلاروسی
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 2.14K · <a href="https://t.me/Futball180TV/102699" target="_blank">📅 19:31 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102698">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromتبلیغات</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RJNwkAi0zu2F_lxeGtaUozy_FqKZcJhe8t8X8j7w0MK9CteAMvrbNAy0upBcogla085h3gSy_N7HAV6txCtcpSs9_0Co3R-G8FVibJiqTeYGYKCZF9L5PN-V-B3PS4UcuMIOwGaCgSHD-VZMJW0Ya7v75G-oaMc0tObIbbmjseG7cSARlfy3FM6SAQvmTqudlPjq8ZgQ2zet-RTKC5ngo3GlH8WEviax3QjSWOKTGlfr9naFie5GH6rzL3v63Hl3I05CroSWXV1G30AM1etJtQh60_SurSPguLZoEZ1xrgYgKRexAqDGqAikxdpgn2XqMuiMwejZtQGBovXpAbWKiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
این حساب دوستمه تو ۱ ساعت ٣٥ دلار یعنی ۷ میلیون در اورد
🥇
گفت یه روش که با گوشی انجام میشه
💎
۹ دقیقه اموزش میبینی سرمايه اوليه ام نميخواد تا ریسک نکنی
🚨
بعد ۹ دقیقه میتونی روزی ۳ ۴ میلیون با گوشی در بیاری
رو لینک ثبت نام فوری بزن اموزش ببین
⬇️
⬇️
⬇️
🆓
ثبت نام فوری
🆓</div>
<div class="tg-footer">👁️ 2.13K · <a href="https://t.me/Futball180TV/102698" target="_blank">📅 19:30 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102697">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u8Xi0zXGUFmevZ_CjQb0Cx8h9XRYnRoQAcnoRLXK8bThD4f7XV-kM9U6YVZzd8leuKCPUBMKEc3iq4KG_a4bWvb3iu0--ok6ICvYPNRYA-Ouh0HsASGGjOksaSHJSaNBoO-mOLnmdYLZ3twKg56ThBT-aHdTHatznxS2h_FHII7CWjoLkhZaC54YwDMoIy6d8IQ-Bp46OrvRydQyKEbotYxqd55CKypJP_jgIv6D67uUCd7FgI278fe8cHmec3O8Q4LbjLLrr1FDBKouGYm8lkg4tl5lb1_bGnI3jLXx0VKP-6HymrVhr-2n70yPuNmgD9Se4t54ORpP9bURDdYR2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🗞
🇹🇷
#فوووووری
از رومانو: ترابوزان‌اسپور ترکیه اولین پیشنهاد رسمی خود به مدت دو فصل را به محمد صلاح ارائه کرده است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.05K · <a href="https://t.me/Futball180TV/102697" target="_blank">📅 19:26 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102696">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VlKJXyCjAw5gDNEDNhN283lGTQb1yobskak4nj8EgcKbsA3w1pDUn-N802y6MRfEudehSjyHeoqZWxDdHMjs6OnsouYxkasZ7_QbwOWlcEGuQulwz_pSbjI4Fwyl7idTu9cCPuNb3sm60x7PX-RkP4N6w7Tb6UAMH0bc9-I8VARQBK-B_ErDCwwkeBKhMkNx6BPnBlg2T1YFA03QM20ZszXlIF4k-ezPgWOQufC1SHml-r3prpMYWqAwBiYCK-ZbHiR2YclGRDbiWt1edsEopU8w2Tcm9Agfmc0TcDx2K1P3ZLAK1GuNT2wiC2BrcdQ4e8J7M9CFvqSqsNfIajoQtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
#رسمیییییی
؛ علی‌نعمتی با عقد قراردادی به تیم لوسیل قطر پیوست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.28K · <a href="https://t.me/Futball180TV/102696" target="_blank">📅 19:23 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102695">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5b46370582.mp4?token=kBdLpk91-pesx0hC5jPeD3z6VI6sXkpwu_Dv0Pw0JvX7iWBPqRSuq6pq-eGPirTb1xeKIKOOKJntvl2hwirpV4nvOu-yVWm4nSTD6qZReUtg4scx1bcokwrBkXp87TXibmXnK6kT-1JLL-1pEaKmOvkPSy_9qEP9MpIAJLa4qY2Whsq33Xn8MDV8z8sV_uF63QvzFdx3TAutapI4CD380jKn4ZCnY54X-osskn2jTRo4RmssrjD2p0HZceXCt5PH9EC5uPfVOSUCUus0mPOUj8e2nSd6411XazNWvUjAPum3odb8p-2YsixRmMKE-zDfGM72thAwvJDNWYzKmGF1ool8GVvjSfp-eht75bvy7Jyn_XxG112d4NOglppPwQBKftw3OUMB2hCDiklQwDzkQVD9614XmhPMQfHNqdFFJwueh1CZj9KqCyqaJcLtfrsjIRS9NWUSqD-IGvj30Gqm6sJbI9h4kYj9Fm5nqPJ64U67Bca9XjHyxHsb2yLrL229_mdxyWSigrZt7bKwb1EwEgO1oedY0GgTc9UejhyjNKVwILg5DIhPCxIP1LNHctdS7bbKm3pLy0tIGMaON92TA92OVoYyoJTVvtv68pjDoYRArC1D5MDqFzlbT4Z5uTr0AFd2Os9hx2DpTlVULwI1GzG0DeKbHZjiRBmOCPIdnBQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5b46370582.mp4?token=kBdLpk91-pesx0hC5jPeD3z6VI6sXkpwu_Dv0Pw0JvX7iWBPqRSuq6pq-eGPirTb1xeKIKOOKJntvl2hwirpV4nvOu-yVWm4nSTD6qZReUtg4scx1bcokwrBkXp87TXibmXnK6kT-1JLL-1pEaKmOvkPSy_9qEP9MpIAJLa4qY2Whsq33Xn8MDV8z8sV_uF63QvzFdx3TAutapI4CD380jKn4ZCnY54X-osskn2jTRo4RmssrjD2p0HZceXCt5PH9EC5uPfVOSUCUus0mPOUj8e2nSd6411XazNWvUjAPum3odb8p-2YsixRmMKE-zDfGM72thAwvJDNWYzKmGF1ool8GVvjSfp-eht75bvy7Jyn_XxG112d4NOglppPwQBKftw3OUMB2hCDiklQwDzkQVD9614XmhPMQfHNqdFFJwueh1CZj9KqCyqaJcLtfrsjIRS9NWUSqD-IGvj30Gqm6sJbI9h4kYj9Fm5nqPJ64U67Bca9XjHyxHsb2yLrL229_mdxyWSigrZt7bKwb1EwEgO1oedY0GgTc9UejhyjNKVwILg5DIhPCxIP1LNHctdS7bbKm3pLy0tIGMaON92TA92OVoYyoJTVvtv68pjDoYRArC1D5MDqFzlbT4Z5uTr0AFd2Os9hx2DpTlVULwI1GzG0DeKbHZjiRBmOCPIdnBQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
این خانم باتجربه نکات خوبی رو در مورد دفاع شخصی به خانم ها میگه، حتما ببینید :
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.48K · <a href="https://t.me/Futball180TV/102695" target="_blank">📅 19:20 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102694">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Wsfl2lj2JMIgSlmrMCInOqgfkAxdevHeVQAZAUGEq6HZC5hJCTTlozZTxvGgZaNAyerMeVLL3uA0ctvav5EMNIyGYv0hLk1X9mmQjXDg25En-nDUdwUv7d6Jv0R-ddp_oo81a1139sd6F3gMN7XjpVKvNkmAKJs7pfU9FYN_DJp9n9rbjwA-WG9xwil_chHzbXFymUi-LUTmay79LMlBk3MMtnxpZCQmeU-z5NtGIPWZsHSqs_eeAQx6E7wpUWuB8dWXxuhwwwKa-nqWKDPaCwop5tlfuvWw3yfT1Dy7eGSX-YTmV-hm606RPA6dMgiMC-NNdo4s0QTWQhf0y01NaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مسی برای حمایت از بازسازی مناطق آسیب‌ دیده در سیرا اوئیسته مادرید، 80 هزار یورو کمک کرد.
😍
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.65K · <a href="https://t.me/Futball180TV/102694" target="_blank">📅 18:51 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102693">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iD2jUiZh0l6DghX-Ln8C7uA8c8ARl2q6jAz7vx_QaMm3XmUfqu3paDqlaDX_bMl1sGxsQAplXnFxgjvhzUcI4NQew8BC2Pvqg3r7Z2DW2Luxd2O5R_jjfWjaqSdRJcIhx1U5AoydVfABhlWedCct4d0EAaUjYj5kfONmIY4o3cTf6fLZYmMEHl7HurE8QEitKQlfLVD8kaqLe9i9bhPOvJtDz40BQC5c_kdSKupb9AhDN1ANam4Nl-pTceupbLf4IPlT3KCkDgZ2FeoGqFhV8g75Gh4S4LC4VTQsEeWNrYxPMxHFkHkJ5s1taCrGLlYouc1I2JPt09do8xr1gaNKOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇨🇮
هروه‌رنار سرمربی تیم‌ملی ساحل‌عاج شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.95K · <a href="https://t.me/Futball180TV/102693" target="_blank">📅 18:26 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102692">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e9f0d298b0.mp4?token=urZhn5loDbJ3_szNlt9pE6JbmrprSkCWSkV_H3JxZRuz7Mi_fy8EyRUrIYbfAY_YlrRu9G6MiJd8ZwssF9DVdvuMlOhF4Eh13CWaDMOMLPBwshcqP7Gw7X8CjxP9AAIWqof3IXHtUL6iO__7chkTzkM25MD1rRkyv8JMgeLZ8aE9NdWmO92Lr8thtloy_iQfZudZWG08oWAsNytB2-oiADyXmMzMoSOHllDF0hwbmep-ia5CxnZx8_ygecU4AXr7SrTpHEP9aaNTfGlzYTbuCqNpESh4fJUS42qSQtY5QjKYU5z8b9w6suG4Hjo7S62UOXFtsyR47Peh3TumQsjhAxkeCmsJm_g5zh8Lvvt0NIb58_YA7SnRhTWRVaN9XY74WKyqLi3uPXL089_FpY2ahKvvISI8vNObRro4s_R_Njn58UnEMxqHNUmI6Iy7Qb3XgNZZp2GhJKOHRB63uYfoJTqDE9aHXIcyIprK9NhxTOj9tL34sLXaSrC9AGAscCJQBko_owV5rON-5kFJBqq0El96ZhCO0rJ5Z8fkETvM9Ni9XL1EOsLzfWDpeIpQoY-2y0y1c7patXXCm68AnCil7Jj1rxxauUYtR4Y50MZyHMT6LgXPWm4Cid652cC8DeWsYY2ofqNZVl6f1TXY0C7uWLLtW8wIDyB6LLoadIFHa-Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e9f0d298b0.mp4?token=urZhn5loDbJ3_szNlt9pE6JbmrprSkCWSkV_H3JxZRuz7Mi_fy8EyRUrIYbfAY_YlrRu9G6MiJd8ZwssF9DVdvuMlOhF4Eh13CWaDMOMLPBwshcqP7Gw7X8CjxP9AAIWqof3IXHtUL6iO__7chkTzkM25MD1rRkyv8JMgeLZ8aE9NdWmO92Lr8thtloy_iQfZudZWG08oWAsNytB2-oiADyXmMzMoSOHllDF0hwbmep-ia5CxnZx8_ygecU4AXr7SrTpHEP9aaNTfGlzYTbuCqNpESh4fJUS42qSQtY5QjKYU5z8b9w6suG4Hjo7S62UOXFtsyR47Peh3TumQsjhAxkeCmsJm_g5zh8Lvvt0NIb58_YA7SnRhTWRVaN9XY74WKyqLi3uPXL089_FpY2ahKvvISI8vNObRro4s_R_Njn58UnEMxqHNUmI6Iy7Qb3XgNZZp2GhJKOHRB63uYfoJTqDE9aHXIcyIprK9NhxTOj9tL34sLXaSrC9AGAscCJQBko_owV5rON-5kFJBqq0El96ZhCO0rJ5Z8fkETvM9Ni9XL1EOsLzfWDpeIpQoY-2y0y1c7patXXCm68AnCil7Jj1rxxauUYtR4Y50MZyHMT6LgXPWm4Cid652cC8DeWsYY2ofqNZVl6f1TXY0C7uWLLtW8wIDyB6LLoadIFHa-Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📅
شش سال پیش در همچین روزی ایکر کاسیاس از فوتبال حرفه‌ای خداحافظی کرد.
"عده ای برای پر کردن زمین می‌آیند٬ عده ای برای تاریخ"
⚪️
🔺
ایکر کاسیاس از دسته ی دومی هاست٬ خیابان ها هرگز ایکر مقدس٬ یکی از بهترین گلر های تمام دوران رو فراموش نخواهند کرد :
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.64K · <a href="https://t.me/Futball180TV/102692" target="_blank">📅 18:25 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102691">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8f5e14ddfd.mp4?token=vk7eTBLQgkUS2mhzR1LGgbvOHLFipo0gvjGzLi3luDCQkZcbYVCl9EYroS2C1TpQd1jKAaEGgM58JGLUrzG8Mm5cpUrCEYbBttM9m6JloNqIsuLrblwjmbbbuqZXk5ZdO7iGup_MS56x24Wovre-MafwfpO5SVqrYDBJCz_uubE2P1mXAwVoawPyb2nhpJWVo2-0UyDxW7RDuBeWwvsJIOOjVjaEj65kOGF_6MMKiYUt9SUSTq8x5qIjLUJLQxBZ3UurMUaPznXMWSOLGf4Fl0dUTQ0w7-Ft-JrE9z2rj3Y4LZYO4t0F05YImAfqyOX_NxxP3HJdlHObFPKRSzP5EQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8f5e14ddfd.mp4?token=vk7eTBLQgkUS2mhzR1LGgbvOHLFipo0gvjGzLi3luDCQkZcbYVCl9EYroS2C1TpQd1jKAaEGgM58JGLUrzG8Mm5cpUrCEYbBttM9m6JloNqIsuLrblwjmbbbuqZXk5ZdO7iGup_MS56x24Wovre-MafwfpO5SVqrYDBJCz_uubE2P1mXAwVoawPyb2nhpJWVo2-0UyDxW7RDuBeWwvsJIOOjVjaEj65kOGF_6MMKiYUt9SUSTq8x5qIjLUJLQxBZ3UurMUaPznXMWSOLGf4Fl0dUTQ0w7-Ft-JrE9z2rj3Y4LZYO4t0F05YImAfqyOX_NxxP3HJdlHObFPKRSzP5EQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
👍
#نوستالژی
؛ دیدار فرزند رونالدو با مسی فوق ستاره فوتبال جهان در حاشیه مراسم توپ‌طلا سال ۲۰۱۴
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.86K · <a href="https://t.me/Futball180TV/102691" target="_blank">📅 18:05 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102690">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fxylJGOYH8HFsHwOwwLSx1vKSsnZDZ9bxckDkNc7ewtGjlwV22D1Jfjqk6IitF1BhK_6G1yIH80Llr7bO-FsqoD6NPu19zIP6prUy7XBuupm8CIEZP6-gyggDzPX7_MlWPyrHY-Lq1hZKsNaomTwhAhPdqGvQyIwu-8xTTBTRfrBupbFPQChIEnjUopDHIcH_itVNtu8q3Cmw644-0wUNAGapNbNsSaBaQJRqAtt2nZcaEt8MTPXrhtQuukgonFCY7XQpHU9ok4igYOGZFHb7HMkwfo-OZXd25U8qqErGwGiVzrAVLQ7jnWkfkdR8CzDgNxERs4mIpl68lYJNNPy8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟢
بازیکن سال 2003 آفریقا: ساموئل اتوئو
🟢
بازیکن سال 2004 آفریقا: ساموئل اتوئو
🟢
بازیکن سال 2005 آفریقا: ساموئلاتوئو
🟠
بازیکن سال 2006 آفریقا: دیدیه دروگبا
🟠
بازیکن سال 2009 آفریقا: دیدیه دروگبا
🟢
بازیکن سال 2010 آفریقا: ساموئل اتوئو
🟢
بهترین گلزن ساحل عاج: دیدیه دروگبا.
🟠
بهترین گلزن کامرون: ساموئل اتوئو.
✨
بزرگترین مهاجمان تاریخ آفریقا.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.79K · <a href="https://t.me/Futball180TV/102690" target="_blank">📅 17:40 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102689">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🚨
⭕️
🇺🇸
روبیو وزیر خارجه آمریکا: مذاکرات بسیار خوبی برای بازگشایی تنگه هرمز در جریان است و احتمالا امشب یا فردا یک بیانیه مشترک صادر خواهد شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.93K · <a href="https://t.me/Futball180TV/102689" target="_blank">📅 17:35 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102688">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CEcQH_1kIMaWcXts35wp1Nonx1l4RF_QnTn_AK23G9V7-E45vEebyMm0QvaJkZCZ9f_7ZfFODJ2gMLS7Z_X4Ivb19QeVYZhHgChYiOKWYlcSOpRxcfDfJc0YzzbERX48mrtTELsVhIZiNVmm_O542OQznhSApkE6p0dJkVe3crKJi2MzIxXy5XM_R6WSjCCYYikDMtiMSqY0_bog8dKJUc0_4v1kWwQijBJTLYzYl9z-HS6BTz-59SvUZBUMHh0bK2kEDmAHyNKuHRmt_Zi2x4AOxPTHARSqDq3sHdn0ENLQ0x8AWaPuvTah2X94hs4g1Pk4wxXA2jEJZ8g3Clz9cQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔵
چلسی صدر جدول تیم های با بیشترین خریدهای بالای 100 میلیون یورو در تاریخ!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/Futball180TV/102688" target="_blank">📅 17:19 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102686">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lAIedibtgAfqpuFnhbmI40DgrjsSPYU2XdI3QiUTYVDtZyc_IjUscdTXDh4HFVJhcWC8y5zCG49FZTRRvOAZ4kYwCP1HC8fsl0zv8d6vT1G5wvKqL84-bP7z8yeCYogrH7wsULPWAYVDfL12SjJhBjGpG46K2ndT0FN2GMj-7NuQEy0YhvmizHMOV50dUNFiqp7V39s6NCvkBNbW6z6nmuVjtbYe-q15KcS4YUq0Zvx2UrhYN8-3kF_Ol-t94sZ4q7zkh_zqakePlhLlV_Ntzl4FVRSRY-vJFNKX7N02Z2K86KSE723gzuEx2Oa1gMeKFQcb-yksofvyBuz0WcppwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/h7APQ9i1SCYeoLwn5uFJofVylrKUHAhDFKlcZ-9m00DDwljJiEVMkUmHUq0Rv8Nt8t_ej6YzHg4C9h5yJJSRfsJvoW-RldWOvgbpLo5Gesya_uN4UyR_ZFNJjAQ6IjlkXD3tAJpPsFVs2nlHaHSLeOWZaXqwb7gc2QntRA0JiIfZqHfRnvvaTgq6S02nKp973Wpszz1zRP2sSyAOmfHRMMVlLZPoPQ9MG8tbBlpss88puZVhcQkveAiZc_k4GDHhqnrFGTXAb_SfHNstOnmWRoOASvvz8znRt7gXA442x9tbOwSvJ9C5HsKzUVSsx8788oPTXsmx1485JrOfmlTnhw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👀
تغییرات رودریگو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/Futball180TV/102686" target="_blank">📅 17:17 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102685">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AceDAJz9KevIt_jqG7J5qMyC4bkHzsrPhPJp5-zBLv-DhbPLY8PwL2pUs04bD_1G0mTm40w26hsrBHdo6_1eN72_rplBaoK1dPhFs_x4Vsv8kqamQ3P06RM5DImNQZ_W8weli0fCw5SA7P1pDioxA35Bd9PsCIJiUX8MWu5DeJxyqatQ-VIpBUVsOREHzGCDBNxCwd6uhfEC25BgBT55NiOGMzLYEARBQBAXypCRcuFr4MZk1ATFJAAitTyKuz75IS2_y36M7UXgaqvRax5xfaFu6JSm0qO2xlPhHEQhOnrpu8dTmasBD6tGMSgH5pbVdJlHXhPpBJKzlth6SWyaZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇹
14 سال پیش همچین روزی؛ باشگاه یوونتوس پل پوگبا رو به صورت رایگان به خدمت گرفت.
🟣
پیرلو: روز اولی که پل پوگبا با ما تمرین کرد، همه خندیدیم چطور منچستریونایتد می‌تونست اجازه بده بازیکنی مثل پوگبا رایگان به تیم ما ملحق بشه؟
🟣
بوفون با خنده به سمتم اومد گفت: واقعاً پوگبا الان مجانی به اینجا اومده و منچستر اجازه داده؟
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/Futball180TV/102685" target="_blank">📅 17:15 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102684">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c78b336809.mp4?token=D_dBb6o-tWyYaIP-PySxBC2tcXLcCm93yFh7TjCIpXxelhdThwM2RoH3nArvX_zWxHZiIVKMltTPIZRe2LQaM7V67T0auLDx6f5xht8BgxaUiyLIdzmzQVdD1tm9FLfqzOAmx8wiIChMxgDIdv1AiqE_PuB5uHvZLJ8A-vTnvMYmd_5R2yfxV_NnEHUzrOnINNbzoU586Q5DqnKcFjIjDaUo8HxEslZgY6Rz_-PJh3zLekMofxDkvZavJW6ggQKxAERaxnQT6EIVsx2rKXavUDIiTdeCjNR7mFFbNCnEkZVA7zyVKBdNvdOJr6NVOexZDKYxxrzgSGQUhWKvH3Y62Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c78b336809.mp4?token=D_dBb6o-tWyYaIP-PySxBC2tcXLcCm93yFh7TjCIpXxelhdThwM2RoH3nArvX_zWxHZiIVKMltTPIZRe2LQaM7V67T0auLDx6f5xht8BgxaUiyLIdzmzQVdD1tm9FLfqzOAmx8wiIChMxgDIdv1AiqE_PuB5uHvZLJ8A-vTnvMYmd_5R2yfxV_NnEHUzrOnINNbzoU586Q5DqnKcFjIjDaUo8HxEslZgY6Rz_-PJh3zLekMofxDkvZavJW6ggQKxAERaxnQT6EIVsx2rKXavUDIiTdeCjNR7mFFbNCnEkZVA7zyVKBdNvdOJr6NVOexZDKYxxrzgSGQUhWKvH3Y62Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔹
امشب، سالروز تولد پهلوان مسعود ذات‌پرور است؛ مردی که از باورهایش عقب‌نشینی نکرد، شرافتش را با هیچ چیز معامله نکرد و در کنار مردمش ایستاد.
🔹
نام او برای بسیاری، یادآور ایستادگی، غیرت و وفاداری به اصولی است که به آن‌ها ایمان داشت.
😭
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/Futball180TV/102684" target="_blank">📅 17:13 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102683">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hTz4h5Y6YdUbIj2XoqCzx5TDNGP9KFWrjy_9uwrN-wAZFCDFOf1T5rnFYhVgfPVfnb84olORucEsboAPjpyqZoRYqLw4rzGXLeU__ov1db_5_QPaGPCx7XYtrLXIV9yRafXhozbN3k9INIDhmFX4PCiqMk7Fqk0SBEo0wpv_c_pfpFl5uGoceBICjiaYyPH52JcGZu4SS_WqtYJYo8FZMDMYv0srkT4DZ19U6KbfWz9nPBqaeNFJsLBeplzYHd1IXGh6AFJZlcEu9NVAFTXT12Qo4bwdO3cOStXNT6z33Za1gSyk3VSufzWZkfEa1cDK6g4enkljd7iSf73OgW1igg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
❌
پست جدید بیژن مرتضوی درباره مصاحبه همسرش با مجید واشقانی و شایعات بازگشت به ایران: تا وقتی جمهوری اسلامی حاکمه به حرمت خون‌های ریخته شده در ۱۸ و ۱۹ دی‌ماه به ایران نمیام
.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/Futball180TV/102683" target="_blank">📅 16:57 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102682">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a3348f33cc.mp4?token=SQmPiVXL73T664RxaMMuSjFod2hKqN6uZq0R8kUDcn2t_phpcT2IghUx1b6AdewgktXSbZ5kP3phgLMj5m42ajcSwrVb1Caf2rADwlJl_xWs3CxotHh0yUQzPjkh1oQz3qT8NDCr1BvgS4OKW0lwRz8juXMioLVCMKK0LybpDwbKt8BlwfEKa9RJ5InIaoGDwO0XgGD5Xpq9sQU30Y2CFHzgb4z7iwwtVbNrPpntcIIs2fFC89cviXUctx40CvI7r_-zSj9j0PqnMAmsVHGB6nYL09sm95cU9V-n7lhvTWEAapG822yGEs_LdPz0a5p1loHRVBrShEm6yFUJb_s11g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a3348f33cc.mp4?token=SQmPiVXL73T664RxaMMuSjFod2hKqN6uZq0R8kUDcn2t_phpcT2IghUx1b6AdewgktXSbZ5kP3phgLMj5m42ajcSwrVb1Caf2rADwlJl_xWs3CxotHh0yUQzPjkh1oQz3qT8NDCr1BvgS4OKW0lwRz8juXMioLVCMKK0LybpDwbKt8BlwfEKa9RJ5InIaoGDwO0XgGD5Xpq9sQU30Y2CFHzgb4z7iwwtVbNrPpntcIIs2fFC89cviXUctx40CvI7r_-zSj9j0PqnMAmsVHGB6nYL09sm95cU9V-n7lhvTWEAapG822yGEs_LdPz0a5p1loHRVBrShEm6yFUJb_s11g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
#نوستالژی
؛ هتریک رویایی علی کریمی جلو کره
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/Futball180TV/102682" target="_blank">📅 16:50 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102681">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/018847c7b0.mp4?token=MkvA7fZmT6vUnUIBA-ghHRQ-2Fs8F6yZxlRT98vJR5STqoLdmtALTLczMUEWPGqPMUNaol7q-XGPCVV-skSJnJM8hooacRlzEOrj-XGH9EQHj1J9wR4sDA2CpskF6y3HfelgdwElXqXOqP1NQhrj6bUswmBNL6WN3dfBjdmz19RGVRd1QwDpsGxekpaho1ZX0E6tqt4hw4RdiquBb9H0SN95uRP0hF8akHRkkenPuyuTfO5tGOb45BQht39EhhNAL4anJ1Sq3GcnbP23LX1vnDhRDZqFqqRfpEoaez3Qh-kfXLtiSR6eDtF0hAM2G-p9Ri2TW0YdgWw3njENiwaQzA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/018847c7b0.mp4?token=MkvA7fZmT6vUnUIBA-ghHRQ-2Fs8F6yZxlRT98vJR5STqoLdmtALTLczMUEWPGqPMUNaol7q-XGPCVV-skSJnJM8hooacRlzEOrj-XGH9EQHj1J9wR4sDA2CpskF6y3HfelgdwElXqXOqP1NQhrj6bUswmBNL6WN3dfBjdmz19RGVRd1QwDpsGxekpaho1ZX0E6tqt4hw4RdiquBb9H0SN95uRP0hF8akHRkkenPuyuTfO5tGOb45BQht39EhhNAL4anJ1Sq3GcnbP23LX1vnDhRDZqFqqRfpEoaez3Qh-kfXLtiSR6eDtF0hAM2G-p9Ri2TW0YdgWw3njENiwaQzA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😃
عشق‌وحال یامال و زیدی همچنان ادامه داره
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/Futball180TV/102681" target="_blank">📅 16:25 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102680">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LrWjXDhj3RmJdWdCrEWdF6dsWSDPdZT1xEapHjz9XJKjQDZvkOEOu3AlZBhoDuSaSGaLtj92oWeE1FcJRH-GIF0_bcyjvqSIyqUZetkpafNPyH8GoZuPEOUEJjABt50rCTkWfoLuk_SKWsEVYQ4sv_jf_dyGp63U6-wtM03AEMWVo3m_tKDpIVWfsv0JRlsTcxn5xUdzlzuY1M7zhQA4FkCPHMAD-ujSAv_T_mjrqm_DviJwc7b06Oq6rR3zv1vYhzhc9fh8b7dXF-qV8-L7Mfw3LH-pvhaqSvaz5f_3X-_K7kvvBNBbbpVlQAjrHULwU2DwIvI4_F0pzk-NdtSySg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
🔥
🇪🇸
آمار جاودانه کریس‌رونالدو با رئال‌مادرید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/Futball180TV/102680" target="_blank">📅 16:02 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102679">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d5903f6c3b.mp4?token=EXJwwX7dvhboKSAWNPMl2IFDk0lW06Q6jbXfn_ojuwU_M5jkZ1nzCGhgp4rxXYTCbjmXjzzQai237ajSY9isj5Rh1muXjJx5NEbczVdqmqVX-Ee0NZut7oDVugiDqepjgf0t9Mwujt2DdvdwDhhFtYQ1DuDVIE2R788TDNZ2XywP9YMPADeE7fkyZ-OyUBaYEaGfwNI9ZJGCumNydJc1QkB2TE5Rc-lmov9PMd_PVwgCDQVJYRj3JoaINCRof_oVlrmGViCQeZ5Hm3YJPfAFhSxZHEEjfqKNCuxz-q0n53wErq18zn3QEo6iiFadNfWu7Apo0Stmmvr5n4XKML9YDXsDMtcFpO4BgzwwQc2GrcOboNT5brjrIQ7KL46JVlW48wfQgHjEWxgjetvHxErKt0__BYoJ-xuvV8IKRV_ZpXPFc6EQXa3xcILzbMQreiF-t8fiDZSfdIUI6rnsvkJvMHqIyFaextqY3BghnpFoVhTPdU0L47vYNNv1wqEO8oE39kv4liFpfF2BTBe825NCiejcJsWCuIpnW4WvPDCnjJyzIMipGrJqLa0ObhcFkP3IXsTLmG0bUdhGc8IuC-IJ7BC1HKQT8VoWhmnQBwPHiay_-wSJkyUxgxWh0-O3ogiXRFPNPar9eAhRYqynFuVhBmWmpd6QwUhHFyqQm2m6_GA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d5903f6c3b.mp4?token=EXJwwX7dvhboKSAWNPMl2IFDk0lW06Q6jbXfn_ojuwU_M5jkZ1nzCGhgp4rxXYTCbjmXjzzQai237ajSY9isj5Rh1muXjJx5NEbczVdqmqVX-Ee0NZut7oDVugiDqepjgf0t9Mwujt2DdvdwDhhFtYQ1DuDVIE2R788TDNZ2XywP9YMPADeE7fkyZ-OyUBaYEaGfwNI9ZJGCumNydJc1QkB2TE5Rc-lmov9PMd_PVwgCDQVJYRj3JoaINCRof_oVlrmGViCQeZ5Hm3YJPfAFhSxZHEEjfqKNCuxz-q0n53wErq18zn3QEo6iiFadNfWu7Apo0Stmmvr5n4XKML9YDXsDMtcFpO4BgzwwQc2GrcOboNT5brjrIQ7KL46JVlW48wfQgHjEWxgjetvHxErKt0__BYoJ-xuvV8IKRV_ZpXPFc6EQXa3xcILzbMQreiF-t8fiDZSfdIUI6rnsvkJvMHqIyFaextqY3BghnpFoVhTPdU0L47vYNNv1wqEO8oE39kv4liFpfF2BTBe825NCiejcJsWCuIpnW4WvPDCnjJyzIMipGrJqLa0ObhcFkP3IXsTLmG0bUdhGc8IuC-IJ7BC1HKQT8VoWhmnQBwPHiay_-wSJkyUxgxWh0-O3ogiXRFPNPar9eAhRYqynFuVhBmWmpd6QwUhHFyqQm2m6_GA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
👀
هفت کارت قرمز عجیب دروازه‌بانان فوتبال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/Futball180TV/102679" target="_blank">📅 15:35 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102678">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fVmDimc6ONs0QyupNy4AbB2BUTAH-OWp1nPYXVtQdqGbydwHth8KbZ0quTteSRXGKpiZV_C2oN5KeOIQeA-OBKZKREGkomlzMDQjUqAmFpDTepdrGNIpjcm50fpa9O9cg4WiIZkA5jzfe_-ODefyA0QUdEA7vwMw4OzoDVxs29nbdqz_PyPWVEm6SnTbFTEgwNzp7mvsO2MQNEfT4-B4M2QHGFV847-dF_RLO2YHknzap5ntY7FhlfKOq23D4zqvgffB34sfOIjzPJNeCk5hJpptJbeCwro4rseOPs1M6ptRjCX5w8nFbkL2UlPpkZrcmHQUxlxo-WpYIXLEmuCmrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
👀
💥
عملکرد ۴ مهاجم برتر دهه‌اخیر اروپا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/Futball180TV/102678" target="_blank">📅 15:10 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102677">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PodPkMOONQRiKN1ZULP-VEZMy2SFnTLRmoH7jjJrGDoW3ga2lDWDpm5TRWl1oIGA66BTyGG--RqIn9FTWMCyw7N1m6aCePdNCNDu6Bpscgf1gOSDbszP5iuZfRUgUH6gfUSNaDWncK7TBcxCy0lDjWeailgHwV50-1lwKIeZ8P7Fdlg4-OTYJp-roPwlPRd7FZ7ekZHyTEoeOE8py2Cg6vwfA9Y7e72AhInL7WN1Du4uMJojOkMAfC3tNAttsM9jNnu_HtJ4aeCnpMVr-PwuCTzfaxwpT3eu4ok4BykD8ejJrXRFvhmuBF02Xv8f-d1qopyva_LKLXwg4XbUmekQlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
پاریس؟
🎙
فران تورس: خیلی خوبه که باشگاه هایی مثل پاریس بهت علاقه داشته باشن! هواداران بارسا باید احترام خودشونو به من نشون بدن تا بمونم، فقط باید بهم ثابت کنن که دوسم دارن و بیان باهام برای تمدید قرارداد مذاکره کنن!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/Futball180TV/102677" target="_blank">📅 14:58 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102676">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1b59000aa4.mp4?token=QXbwQiuvacNU7BdnMOm9EsAl07-d5q2eZYc5S9eByDR_wR9NjC987oc2GKsZ5NJOStI_mJjRCN-ALXDc7pVBqCVt3fgf3ubvfP1Au9FgDvnWjIooQE4A2FIxOmQN-TgBsRGCj7A4yEQU90ODseEAP2gvIg9UfKNk9WAUYRzG7ZOaaeBW56unCHFfqPRsD7H-93vX9RkMxUu2MhrEpGGVYwmLTUUWbhZYIvYXNjmYfwKiKZMSojd8upOAcWdBaIB7JNN82k0ydrrFtcWF6p_ne4RB4aQyrGl0IvgCQcaSIhKjEd6jIDqhLcySrIE2LVRErBFofAaK7C9Ma2yH6eooJA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1b59000aa4.mp4?token=QXbwQiuvacNU7BdnMOm9EsAl07-d5q2eZYc5S9eByDR_wR9NjC987oc2GKsZ5NJOStI_mJjRCN-ALXDc7pVBqCVt3fgf3ubvfP1Au9FgDvnWjIooQE4A2FIxOmQN-TgBsRGCj7A4yEQU90ODseEAP2gvIg9UfKNk9WAUYRzG7ZOaaeBW56unCHFfqPRsD7H-93vX9RkMxUu2MhrEpGGVYwmLTUUWbhZYIvYXNjmYfwKiKZMSojd8upOAcWdBaIB7JNN82k0ydrrFtcWF6p_ne4RB4aQyrGl0IvgCQcaSIhKjEd6jIDqhLcySrIE2LVRErBFofAaK7C9Ma2yH6eooJA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
🙂
برخی از ریدمان‌های اساطیر‌فوتبال :)
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/Futball180TV/102676" target="_blank">📅 14:45 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102675">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AzKC0kCw8M3MLwgJiIDuVtxxEvZlTXtFlN5kyfOONxsUapZuSg7zQ5FXmktbgNKCKs9u3hZJPtZ4-gPJAw7BtkRzcb9eszxtJB5M_cmoKTYNw0y4IGm4zz7PMLlF1aags6Hm1_kJM1xDoEMgNLhtFSOobC3pMtknfQdV6vjkdy0IH5MEK_-WAJ5tsQRuhAUZrbG-CXPhnSQPIOWaIsAsNgCW8OQMoBFU37ReMb55rtpFtXTgucRwXy6Jzu_ls11dNRBaMWBr-B3hAMyluH5CBA7aWqpCUZkhPH-mOKC0Flo9KZEeconFcvrF_xBTEvpxcL53zxK1IziRZwMquagUKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
اولین جلسه تمرینی ژابی آلونسو با تیم اصلی چلسی:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/Futball180TV/102675" target="_blank">📅 14:32 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102674">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eb25fb54e6.mp4?token=ajQoKc_cK5smMuIohkkDcFl74wpN_UfTERjGTr3ngZtNiFOTr0Nb-Om5_bwjJxQ10a8vBjyaNvQ4dDl6m8iHwJ2HqysVvOoee9U7g5zMxncL7El4jx_IQFAeXqvo6EcJ9iFi_GA8T1Cy8AMX6Hwxhj357BSRPAHHbCNzZUNudx1o1_OU5jox5BKqdoU3_Z6VewP5V7dk1_iK1xq-BDIvI8b9HziBHtmFq44sAgbzpD48hxLe_FoVsl6NNfyBx5AHDx-z0EGo0-xCAtZMiMdpmjB0X9mqd06JrXqNHTIJAc4cSx6vIDQD1RoMqg9mZ8mr6ZlZcCzV3Ye5rrwqgSVV4Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eb25fb54e6.mp4?token=ajQoKc_cK5smMuIohkkDcFl74wpN_UfTERjGTr3ngZtNiFOTr0Nb-Om5_bwjJxQ10a8vBjyaNvQ4dDl6m8iHwJ2HqysVvOoee9U7g5zMxncL7El4jx_IQFAeXqvo6EcJ9iFi_GA8T1Cy8AMX6Hwxhj357BSRPAHHbCNzZUNudx1o1_OU5jox5BKqdoU3_Z6VewP5V7dk1_iK1xq-BDIvI8b9HziBHtmFq44sAgbzpD48hxLe_FoVsl6NNfyBx5AHDx-z0EGo0-xCAtZMiMdpmjB0X9mqd06JrXqNHTIJAc4cSx6vIDQD1RoMqg9mZ8mr6ZlZcCzV3Ye5rrwqgSVV4Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🇪🇸
مثلث آلبا، سوارز و مسی که بارسلونا رویایی فصل ۲۰۱۸/۲۰۱۹ رو رهبری می‌کردن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/Futball180TV/102674" target="_blank">📅 14:20 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102673">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jLxrj9DLn6b53SYXriQ_wpMCA8tfbUhoZV2xq2XK7kHAYiZbR1b2U6Vv0mbEZOHNupT31pLXhNzv8T5A5w8ZE7f6Nk9Wj4KzvHZ7UDb8mNTZUImLW8R4AYbKro7uOHm9NSFQqI2jO3l39inV3bYZZIyqLL6amnygqYBTkTHKbDiugS_5rQ67ET3lVbzQV8VN2eV52KbrXRlHuJuc9C2vYIBV1705Ee1oJQfC2KOCFQ82anKIyCFvnu8mIxaum_QJKPxOm4hmMYPPBpQBd8TGw2fH0tjW0z__4QeXul9wNErmSYE9hGepErQuRRzn3ORxErdpmkqOVzxr4B78wDfNWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیس سنگین ایکاردی به وندا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/Futball180TV/102673" target="_blank">📅 14:09 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102672">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">🚨
شهرک صنعتی شمس آباد انفجار رخ داد که عضو هیات مدیره شهرک اومد مصاحبه کرد و گفت یه مخزن ترکیده و چیز خاصی نیست نگران نباشید.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/Futball180TV/102672" target="_blank">📅 13:50 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102671">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u4x-U81f_lSDeeM9ZoNKq5TIuV-8NXVvPMJun7LUG_jl-LnKX_Xym99-6s2sCHtld-AWdLG5IaeUyWQJhQJ7CLp0nm9rBOGlvHbtuYmql_dTqshK7kg1v878y4tO6lYuE_d_UJNO8doR_gmilkja4uWjc471ceLU7U65bkCrHba1qtDu7Zqd3EkGMq70LUHMFQ1ZpVHG0_PE8I0wsDyPrvqjA8l3RvLzsJESjYPjHE5_VMAQIy5U3CWGuJ9XHdsucdfgRrEvs_f5jrKrpjBu2yBwozDxcM7Qx9IHjKxlq-uFjNscGBp6Og7tFcoW5TnzG64gbbN8uym4TDJxo33eyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
تو سبزوار یه مرد بخاطر اینکه زنش پیراهن امضا شده پرسپولیس رو به اشتباه شسته و امضای بازیکنان پرسپولیس پاک شده، درخواست طلاق داده و به زنش گفته که کل مهریه‌ت رو یکجا میدم
😐
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/Futball180TV/102671" target="_blank">📅 13:42 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102670">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/627a83e0e2.mp4?token=nGeXavpoYdw5PaU6D2ipuRptnLly4gJmeq4Y73A1nH3uXJjf5Nobm3E4xlzinvcUg4Za-RR6EmRy36ywlmDRVjOfLBABllpLW_1Oa0N7DnjOegHJ-JysNJ5v98b6Ge5w8GXe5DQqouOIoqKQclj42PbCruHyHZZhdJbqPaaCBkVgVdrrCX7NtgrFwHS0Way2aFlNgwxItZsnvfrfqfnqRXWNEHnaIAyZLNEWmAznca1fQieKOpF3VOsHAxHjgiJwpSRjkN-cvhvMXFFDbqnEgpQZluNxI5iF3zKAhctv9T3HlEaYgRbYHcvr_I_yzd5vxMEJOl-Qxv87H_sZbGxbvA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/627a83e0e2.mp4?token=nGeXavpoYdw5PaU6D2ipuRptnLly4gJmeq4Y73A1nH3uXJjf5Nobm3E4xlzinvcUg4Za-RR6EmRy36ywlmDRVjOfLBABllpLW_1Oa0N7DnjOegHJ-JysNJ5v98b6Ge5w8GXe5DQqouOIoqKQclj42PbCruHyHZZhdJbqPaaCBkVgVdrrCX7NtgrFwHS0Way2aFlNgwxItZsnvfrfqfnqRXWNEHnaIAyZLNEWmAznca1fQieKOpF3VOsHAxHjgiJwpSRjkN-cvhvMXFFDbqnEgpQZluNxI5iF3zKAhctv9T3HlEaYgRbYHcvr_I_yzd5vxMEJOl-Qxv87H_sZbGxbvA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
روایت‌ایووبی بازیکن سابق آرسنال از تقابل با مسی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/102670" target="_blank">📅 13:33 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102669">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gv-_oqse4mW7qxnzQvS-9fkcuQfe5XJ5rRyJfOSqg9Kqi-q5xYH2JF543WQ6MgB4IFh1004yTgY4ZKa07GaqqRDXBXa5Oq10kRKmMtmWQpNvFrDEAz5lW3KG-_rsY0M6yZ2eqxKRPcXl74YxKQ0PLZoN46yJxPgooyg-snYTe7sBIWJpVz-CjlUTbuuaQ4p2KBHVr17abpaZGdaq8n2t59maT06Y-PEJYT7oaqkRwbnKqBpCQonwsZ857y0lBRDKUyHFk_l-bQ0lSdLviyctylfTpBei_b2SMQa88sOoJsnJ44lXfrHacZQ8BVzFrzIqIRGi9Sh1aifxbDjF_ZwXKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🇪🇸
متئو مورتو: باشگاه استون‌ویلا درحال مذاکره فشرده با اتلتیکومادرید برای جذب متئو روجری است و احتمالا تا ساعات‌آتی این معامله نهایی می‌شود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/Futball180TV/102669" target="_blank">📅 13:14 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102668">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3e611ac196.mp4?token=nI0knLKhFDc1vsMBkQBZB88lA8uz9QVSxQVtlUNfUh_sjo_beGQR1BEABEIuHm7XaxBhJ86MXsYa_LFD3DUukmMRkthNQoEgo3Bd2lJhSQEcnRn72YpQMgB7L30x8Jkcu4Zyv7JKRQ4uxLWLkK9aT_A2dzDp43XKTgObBaRgp_u2lkhs5jMc09L_QC8eqhTFmrzthY3r-sQKIugLKJC8oZVohfR7A47eaNK85VMPKaQLAaGe4FgMVN_HYoGgQ5V80jstY9Im51NzzJ9f4aNq_IgO0WB3SmeWLGAiIsCN3a_aTvO8jA2K-f-mITDe85uuwlpSiA17hpiWJ9h4aO3S5w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3e611ac196.mp4?token=nI0knLKhFDc1vsMBkQBZB88lA8uz9QVSxQVtlUNfUh_sjo_beGQR1BEABEIuHm7XaxBhJ86MXsYa_LFD3DUukmMRkthNQoEgo3Bd2lJhSQEcnRn72YpQMgB7L30x8Jkcu4Zyv7JKRQ4uxLWLkK9aT_A2dzDp43XKTgObBaRgp_u2lkhs5jMc09L_QC8eqhTFmrzthY3r-sQKIugLKJC8oZVohfR7A47eaNK85VMPKaQLAaGe4FgMVN_HYoGgQ5V80jstY9Im51NzzJ9f4aNq_IgO0WB3SmeWLGAiIsCN3a_aTvO8jA2K-f-mITDe85uuwlpSiA17hpiWJ9h4aO3S5w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⚠️
اوکراین دیروز کسخل شده و با پهپاد یه ساحل تو روسیه رو هدف گرفته که چنتا مردم عادی کشته و خیلیا مجروح شدن!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/Futball180TV/102668" target="_blank">📅 13:05 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102667">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/937fee7ba7.mp4?token=A2f-YeZmwIIYIzRlhjpuxeHyGCoeXjKZCzohmRumNoYbps420g4Osl1H7ZLZyrDZOkzGYoAIHL50J0ScSLwWj6Q0erjCMOsag1CPTnZiab_z2fxIb4rb-r0TIPWaeV8jmth7bAnAyovPQMQWwAh-dNmn7pFE-v2FWzjp7f5fYMy5FOdgFBjgz2p0lsoSjtNhXhLLBC3qCHqD8qb8XFRNdSR_jM3u51EJe2aVxZxzKhHQmakZbH8g04XvgFNbdmAjPSJ8VIp71HNhrQ1vqOyQ31OXTnPyB3HvjASCM37NoVMVMWPmN_sDj8TFN5Nk6i3-6oiOISjcy4ZeTdTRupgkdA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/937fee7ba7.mp4?token=A2f-YeZmwIIYIzRlhjpuxeHyGCoeXjKZCzohmRumNoYbps420g4Osl1H7ZLZyrDZOkzGYoAIHL50J0ScSLwWj6Q0erjCMOsag1CPTnZiab_z2fxIb4rb-r0TIPWaeV8jmth7bAnAyovPQMQWwAh-dNmn7pFE-v2FWzjp7f5fYMy5FOdgFBjgz2p0lsoSjtNhXhLLBC3qCHqD8qb8XFRNdSR_jM3u51EJe2aVxZxzKhHQmakZbH8g04XvgFNbdmAjPSJ8VIp71HNhrQ1vqOyQ31OXTnPyB3HvjASCM37NoVMVMWPmN_sDj8TFN5Nk6i3-6oiOISjcy4ZeTdTRupgkdA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
❗️
دلیل اینکه چرا کورتوا یک‌دهه جزو برترین دروازه‌بان فوتبال اروپا قرار داره:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/Futball180TV/102667" target="_blank">📅 12:40 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102666">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/222ef9e7d6.mp4?token=uQyf5Lmm3Sbg320is1xfasuJKjNGsy-i1mNCZfq0vTscJe9SMDeMMnMVBU5SRYAq7U1My4XyUcNzpiCvlb8q8dMT0mbQ2d2Kw93iyUtju_JXg6rKzOtgcEPrrcoWu6EepvffGtt9J1F33AfHhDSYMzlI-ja8xvxbUKRa-wdr6troi3VTBESLm2MiHq517YMvNihoTD4R2OKsOXqUuWcD7wFJCUOKA3_tT-LAHj2crNvPukK14Y2CWxKZdfhUUi4byjHYtn_0Nk1zaSoEc7bbfHOMF2scpC0R6amBuC6GyXURsAql-WyBgetk3JDCZFu037WpbcdNx6aajz4DeCFc6Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/222ef9e7d6.mp4?token=uQyf5Lmm3Sbg320is1xfasuJKjNGsy-i1mNCZfq0vTscJe9SMDeMMnMVBU5SRYAq7U1My4XyUcNzpiCvlb8q8dMT0mbQ2d2Kw93iyUtju_JXg6rKzOtgcEPrrcoWu6EepvffGtt9J1F33AfHhDSYMzlI-ja8xvxbUKRa-wdr6troi3VTBESLm2MiHq517YMvNihoTD4R2OKsOXqUuWcD7wFJCUOKA3_tT-LAHj2crNvPukK14Y2CWxKZdfhUUi4byjHYtn_0Nk1zaSoEc7bbfHOMF2scpC0R6amBuC6GyXURsAql-WyBgetk3JDCZFu037WpbcdNx6aajz4DeCFc6Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇰🇷
هونگ میونگ-بو، سرمربی کره جنوبی در جام جهانی ۲۰۲۶ مجبور شد در برابر مجلس ملی کره حاضر شود!
‼️
او توسط نمایندگان مجلس درباره تک‌تک تصمیمات تاکتیکی‌اش بازخواست شد. از تعویض‌ها و دعوت بازیکنان گرفته تا ترکیب اصلی تیم و سایر تصمیمات فنی، همه‌چیز زیر ذره‌بین پارلمان قرار گرفت.
هونگ در ابتدای جلسه از مردم کره عذرخواهی کرد و مسئولیت نتایج را برعهده گرفت.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/Futball180TV/102666" target="_blank">📅 12:15 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102665">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/be9e48b7ed.mp4?token=P4yWSJxVBBbwagXbFCi_OzsSCPJUjCc0gfgHkI64nkhHFLYOnqdHhMDxNdkuzJfuBJOi2sGIGWHGLM7dzffjimuwd0seD4cwHSWW8VncT_m47K0obTtmmLZ7JbiS1yImaJurT_UNg2u96MNheh6RJKcubxs91mZyhuqdi6M7vgYzvFP6FsksyUo1RDNNqgRVwW_J088am6uhTZjmfWe3TWu6xnbgyth5KBmZ-YZLjgkOxoPKDTkkw3Ez0UA1sl9XAF7omkvdDv6R7Z6AxgMILznPKGa_aXWlU3jKm9wQZ_YF2pUwG2IILLlUI3UD7SYppwN0dO_RUK21nHX15bAxFQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/be9e48b7ed.mp4?token=P4yWSJxVBBbwagXbFCi_OzsSCPJUjCc0gfgHkI64nkhHFLYOnqdHhMDxNdkuzJfuBJOi2sGIGWHGLM7dzffjimuwd0seD4cwHSWW8VncT_m47K0obTtmmLZ7JbiS1yImaJurT_UNg2u96MNheh6RJKcubxs91mZyhuqdi6M7vgYzvFP6FsksyUo1RDNNqgRVwW_J088am6uhTZjmfWe3TWu6xnbgyth5KBmZ-YZLjgkOxoPKDTkkw3Ez0UA1sl9XAF7omkvdDv6R7Z6AxgMILznPKGa_aXWlU3jKm9wQZ_YF2pUwG2IILLlUI3UD7SYppwN0dO_RUK21nHX15bAxFQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
گشت‌وگذار امباپه و اکسپوزیتو کف بارسلونا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/Futball180TV/102665" target="_blank">📅 12:02 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102664">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bOfEYMUW9kYYpgEIuA5FWmqnYV-4dHJT7WB92ssAmQZg1njsJpi4Z7fwbmve796miXcN7HlY6-2-lbzF7rujeBGkUBxOqV11rb9fVK85yIL1tIt61J7IQZIV5O2BE8cjp2jHYQdQ5rMoTzVzt-Ls9W38UgiCDjUZ3hXP0hyi6V-VFcfSY-CRvSRwP0aQrER9iO9G5Xr3uJMhMaF3JpKg6WAINodyZ8J3duwsiQrjwDcA7yh8xiqerCajGN0tLKoWK0vRKbNsFsnTWnvmzwAYgssIcJq8ZkpnTvZuRNnuL3AY0WFj_I8lgidrHrBnRsjOnlyOBLeUuxfyTevx63MYdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇩🇪
🟡
فلوریان‌پلتنبرگ: بایرلورکوزن درحال مذاکره با الاتحاد برای جذب موسی‌دیابی است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/Futball180TV/102664" target="_blank">📅 12:02 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102663">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KnFlWr6Cxgbwu6L06W8J5PaLzEFuKb-mDaI3Dhpu824y0GHoFSk_aBWA1PUMhy8PFqYzm5Q4NQJaM8jybwy9FFBCxpdnDMiL9F3PDrhNFgdjifMXbrP6mZITv8-S9Vld5LB7fIAtxS5dCJD2h6fw29VAtmXwkfCk6ljhJkGD4Vpb3yElZbumZpguiK4E7-N8BMBxIajBgJ-ZVFgb7UHnHn64hPktZ10GRDMzECjETzoYMKbkAdwFp2JJrpbzfM1dKEirs1cuGVnyB-ztwy5GXZE2Ic6p0v3uzQ9A5Jbz4qD_bOutIQ7HMeJKvqwh9o8h2tUvXBbDr7cNHdDErf8Dzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
❌
⚽️
فیفا با انتشار بیانیه‌ای خبر حمایت دونالد ترامپ از اینفانتینو را تکذیب کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/Futball180TV/102663" target="_blank">📅 11:49 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102662">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UITp43Tu7Z3xq3KL78biQer--Ck-bMO4HJyZCtGZdRQslMKnQryuV_zwUXGRUHWfg2r7CCaN2gP22E-DCuENVDHOS3ShtTNABntWMJ2JGQkoBQj21BagPf1rv56x8v49f2yuBLicM6AXJNxZLOsPg-LscPqljpIqFQpYFGKThrmIt6JVkJUptkf8imJB3L0Co8bSIQsGBRZ1fVoxQEHpnEsiQ6-CoSSQRi8t_PMC8HDjsZOjrHAk3Ub5SZop0OaIIEVBXZ3wMGwdM7wxS53cIUkjOHT7yTlxASwYW7lNREJzZjYAx-OZkJfipWyVL1ZLaBe7aq1UqyosM1e3wKg6Ag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇪🇸
⚽️
#فوووووری
از مارکا: رودری دست رد به سینه سایر باشگاه‌ها زده و گفته که فقط به رئال‌مادرید میرم. قراره بزودی این معامله تکمیل بشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/Futball180TV/102662" target="_blank">📅 11:36 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102661">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/uQbn6QAtRi62l8XWh8BE1MgwsMQwrnirNBM0uGYYXhPJvtmfN_6RCgv2kqo43bhWUOwRkV4NLevuP8UdJ0gmXPE4p_LI4weOWkvKmorfPEQp7yaps_VL3-0B0O1eTQRcqLWTV83gTXPUxSiDQvcll1tfiD7q4raktdq7bzpGGQ-vzbjPjNRuyeyR1J0T4Vvn160MKPKNAtQ6MqPJ5ILh0h3ms8AemO-35fw7fn80EUNeyuna6K0Hytrdvb9oWg1f3nq6jWsaMqLxOviSkyV50vtHLuxqcl5S6Qu22lhd9q7l3S6qygqp1wBOP6a0_Zg2636rVAOsKB9El3gwcvUAsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇩🇪
#رسمیییییی
؛ نی‌لاند دروازه‌بان تیم‌ملی نروژ با عقد قراردادی به لایپزیگ آلمان پیوست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/Futball180TV/102661" target="_blank">📅 11:32 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102660">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🚨
‼️
😆
😆
🎙
ساکت الهامی: 55 میلیون تومان دادم کت شلوار آنچلوتی را خریدم تهش ۶ تا از استقلال خوردیم و باختم!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/Futball180TV/102660" target="_blank">📅 11:25 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102659">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Yao6cydMPDDf_6O5SveyjH3qjr_zvpZG21uLpWBQmWS1VYqyoW1zt_J3MuoEkXq6lidt7eOsuHuQOgo4D3q7dzYpfBpGv-SMZ9z2ZyYeV3lm4E2jbdOyy2uZXPfwYF0Oqq7E2eGqR4hHZ3XBVRhzqAPjW-MMvdrn6H71JAUOkAmeivDHto_dmNpEAn7jxx97jlkHxu7WRdzGhk_HHkhphNeEwyGLcWyY9ySCRKp-lCacK8RK_dFHzQAXHcl46Dr7tLyC62wR9cbDv86934V30tuvtwe0e7EDzry8YMTqKBYJP1WOsENpABI-PecFjemNRYg4UoneIi7roT0PFgJBAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
آژاکس آمستردام از جذب مارک آندره تراشتگن به صورت قرضی تا پایان فصل از بارسلونا خبر داد.‌‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/Futball180TV/102659" target="_blank">📅 11:02 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102658">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bbf1a57969.mp4?token=MmK2CnVJFUHfICvOtUyd8E8brqLznec6Dka4K_VoGYX_nNL0KpelVE0nPymbjSveuaGlwqkvTAN5r93Eah5aIsO5fnVTmidnjAMkIvEdQgk--NGjlEZuj9RFfY4WWScjPpb3dEOQiM3go_NKq0ZnHSNWthCVLGu_lID4fhejdMWBxb6SStDZK8v_ayV6pOlNPRR7PmGP1cYq10SwyaI71Gke5eMrISAtVfih1AuVIttdgQyo5xrCbbaOO1OrJNIOEi9nxCEQAwN4AGaRYqQgBZWyYGxioZTJNkQGGRsjHvz72EuXGyriG6s7y3Mr187EoscFD8Q4SlayZNTS-p8H5w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bbf1a57969.mp4?token=MmK2CnVJFUHfICvOtUyd8E8brqLznec6Dka4K_VoGYX_nNL0KpelVE0nPymbjSveuaGlwqkvTAN5r93Eah5aIsO5fnVTmidnjAMkIvEdQgk--NGjlEZuj9RFfY4WWScjPpb3dEOQiM3go_NKq0ZnHSNWthCVLGu_lID4fhejdMWBxb6SStDZK8v_ayV6pOlNPRR7PmGP1cYq10SwyaI71Gke5eMrISAtVfih1AuVIttdgQyo5xrCbbaOO1OrJNIOEi9nxCEQAwN4AGaRYqQgBZWyYGxioZTJNkQGGRsjHvz72EuXGyriG6s7y3Mr187EoscFD8Q4SlayZNTS-p8H5w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
پدر تشریفات ایران آداب استفاده از آسانسور و پله برقی رو بهمون یاد میده که بنظر هیچوقت نمیتونیم رعایت کنیم
😂
🤣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/102658" target="_blank">📅 11:02 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102657">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6a0e4679b6.mp4?token=EI_6HTaKTj012GwVCeMwVP0Eh0ojgqsiat9sT1CxRvyCwiy6va_h-7Ssu4W7hKddRIU8sTwQNufDvIdCSa8ZvhFmiWpgPrm5epcejSqcHUIfIAicJn_5YlwXcEj37w0tvusXVW48ReQZ8UjEiAalmFfV1wrieOhnlV6wVshrWitxkiSjmKoPN9MEIArCzITmEVywIpQQoSq47yHJ6PhK5tOLh5VbmYGqbhCLBQATV3XqReOmTQb-UVVPvND-0tbL_Evhp56i9U1fRMDhMjl4MZLycKesr9I40zM9pjbnYIotnWZnPkGx3Lyaay74x_gotu1diJZjcDt6muQxyP6MBzyfhZhytttqU8ZfdJLEBSLTEQdi_GgKs_Uw6zTzAWjeOaMyVKBpZbwBwHWkE4QJSg_f8cgIYAzkSE8fZTCNz5iSFFgZeDGFyl-NunYIAtGY50me_C1qyv09Jc8vZ-zi4Jjx2BMHFx-bBYCdtL1Y0Ao83IxPMH7QeE8Toiy0cOzCO_HppND_3llX3Tz6m5aITUfoe8RtT0MCsJUvmchgXqEwHH32eAjP3UHmo--RT8EchIjwJN5koWvEvKCOYcGsMNeUYZGTJ8_m60BTodFbp2KRgdGnKyozgJbD06SL3pmYM2BFX2orYfVIYl6AuHzARpXx0Mz0-c-LmCjQzZHcn10" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6a0e4679b6.mp4?token=EI_6HTaKTj012GwVCeMwVP0Eh0ojgqsiat9sT1CxRvyCwiy6va_h-7Ssu4W7hKddRIU8sTwQNufDvIdCSa8ZvhFmiWpgPrm5epcejSqcHUIfIAicJn_5YlwXcEj37w0tvusXVW48ReQZ8UjEiAalmFfV1wrieOhnlV6wVshrWitxkiSjmKoPN9MEIArCzITmEVywIpQQoSq47yHJ6PhK5tOLh5VbmYGqbhCLBQATV3XqReOmTQb-UVVPvND-0tbL_Evhp56i9U1fRMDhMjl4MZLycKesr9I40zM9pjbnYIotnWZnPkGx3Lyaay74x_gotu1diJZjcDt6muQxyP6MBzyfhZhytttqU8ZfdJLEBSLTEQdi_GgKs_Uw6zTzAWjeOaMyVKBpZbwBwHWkE4QJSg_f8cgIYAzkSE8fZTCNz5iSFFgZeDGFyl-NunYIAtGY50me_C1qyv09Jc8vZ-zi4Jjx2BMHFx-bBYCdtL1Y0Ao83IxPMH7QeE8Toiy0cOzCO_HppND_3llX3Tz6m5aITUfoe8RtT0MCsJUvmchgXqEwHH32eAjP3UHmo--RT8EchIjwJN5koWvEvKCOYcGsMNeUYZGTJ8_m60BTodFbp2KRgdGnKyozgJbD06SL3pmYM2BFX2orYfVIYl6AuHzARpXx0Mz0-c-LmCjQzZHcn10" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
▶️
آخرین فصل‌ لیونل‌مسی در بارسلونا
❤️‍🩹
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/Futball180TV/102657" target="_blank">📅 10:35 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102656">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">▶️
🏴󠁧󠁢󠁥󠁮󠁧󠁿
برترین گل‌های محمد صلاح در تاریخ لیورپول
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/102656" target="_blank">📅 10:19 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102655">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VzEIEP1EFY1we2j6I9Z9GxlL2t-mpIVEC9PoM7z3zwmG9sBxXHsyddIWPkVxzqSiZdNMWrZIVOVKYk-ujJ93sYHu-_5LYROHMA0zmcfr8P_l5OeSHlsY5cq9Fh-A0jcLp36Hy8lzGQrfywqyPgubZPWl6eosgIiIkcGvqzlRVHs5ySUsYaAR0PGbGJ0075RxBI6xmIRJwM0HNZPcUoa2-ePrZXgGAi4j4k9BKyeT_jUCqKz-rp0BKM8UjItra5-dA6AWk5d55oHaysqRHqId76FCiB67u5QCkHP2Sh_eudSjHZcXqxsJZBzM1QTtysVj8saDdodjK1Rfk-FrdxJi6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇩🇪
مدیرورزشی لایپزیگ: دیومانده به محض بهبود بیماری خود به اردوی تیم در اتریش ملحق میشه. دیومانده بازیکن تیم ماست و به قراردادش پایبنده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/102655" target="_blank">📅 10:13 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102654">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">👀
🇪🇸
🇪🇸
یادی‌کنیم از بازی دو سال قبل و پیش‌فصل الکلاسیکو که حسابی جنجالی شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/102654" target="_blank">📅 09:50 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102653">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🚨
‼️
😔
🇮🇷
پرزیدنت مسعود پزشکیان در واکنش به جنجال‌های ۲۴ ساعت اخیر: استعفا نخواهم داد و خواهم ایستاد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/Futball180TV/102653" target="_blank">📅 09:40 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102652">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4f47080196.mp4?token=bk-kFDh_fbuRyO6bxHl7N1lSJv3tjIXBkq1VYO-JVf8aTOFyuRsJX8-DV3pDBLSmqz7H56uBpER3k1V5L7KHqctVZUj8UjQt6ZtgV9Jq58wZHBa6M6uJqssp7Nz1ovOstSyG6YluLPSB1RvgL3RQ_mToBuUpLMeyvNWrvh0gXcw7e930GI7D1yBJme1tUabFFMfeF_dv2_xjPGorllaRUTHdO3Ilj8f-ICWhMf8BOLGgyk7kVCyIxUAejBE6vxN-ysWKbwip719RI3wOc8WBwfQe-a1MNRLqHKjplwa7m7bExBwj3gxVHRFomPcSdHu3S9TqgzQNE24KKeycTlmPag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4f47080196.mp4?token=bk-kFDh_fbuRyO6bxHl7N1lSJv3tjIXBkq1VYO-JVf8aTOFyuRsJX8-DV3pDBLSmqz7H56uBpER3k1V5L7KHqctVZUj8UjQt6ZtgV9Jq58wZHBa6M6uJqssp7Nz1ovOstSyG6YluLPSB1RvgL3RQ_mToBuUpLMeyvNWrvh0gXcw7e930GI7D1yBJme1tUabFFMfeF_dv2_xjPGorllaRUTHdO3Ilj8f-ICWhMf8BOLGgyk7kVCyIxUAejBE6vxN-ysWKbwip719RI3wOc8WBwfQe-a1MNRLqHKjplwa7m7bExBwj3gxVHRFomPcSdHu3S9TqgzQNE24KKeycTlmPag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
روایت دیوید بکهام از میراث فرگوسن در یونایتد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/Futball180TV/102652" target="_blank">📅 09:25 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102651">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TttQfYtL06AB0GWuzd7LypBbWOM76yhCzoKJNK_wcF4OlK1Tev6AphSysA0P-U7SwDGlU7Qf7aOv8vQ_9G1NPdVkaamB1R3PNnZgwgCwuS9Mp26dIKYgWmU9VoQGCA86nistSelRr4n2MQiNqYKlp8iW3kzs6ghlNfKxqOZR5rc8bj74a3J0gNqGCUadh3pd1F_Ut50KOmfI3VwtODDZuHHqrS2Qb69Fiucbp5nbGe30VkCUUxAIi6ss3RlR0nYHBp31NxLZ--QAuvHCIkvePPLShTTixazyANAMt2lywvo0NGEVjVH4JgGnTpNabexmcfqmdV5gzzuZz_hirvMJ0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇸🇦
کشور عربستان سعودی در حال ساخت بزرگترین شهر ورزشی جهان با بودجه ۱۰ میلیارد دلار است.
🤯
این پول معادل هزینه خرید ۸ بمب افکن B2 یا ساخت ۱۰ تا برج خلیفه ست.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/Futball180TV/102651" target="_blank">📅 09:07 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102650">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SeIecWXv7za6JA807m-ERhRffFF8KUbFcTfk0D7Osmmv-4rhuSLT71Da6R7r_6H41SDPhsDaRbQbs8xpkkZzckFx-i76xNe_ss0GhVNHEMAvgwXdPPLN4fizxtmUxCxLfHrFhFAx9rxDezpPfm8jXRXYLggLClO-bJobxX5whbfvCvMzzS4U-dZeQcAWiPoM6uiVH5WFJWn-Zpe3Ovh4fwz871Wn-dW9JBd24b1XWe2iCabpAbHYeF85RbSrSxGOoM2Y7f3nr457fglDvJ3mK4tCFhof50BCDbEXaFskrcwFMLZWd7d0W8JdaStqcuos_8wvKGVZU7ziAFRG6W3qAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#فوووووری
از نشریه سان‌انگلیس: باشگاه استون‌ویلا بدنبال جذب مارک‌برنال ستاره بارسلونا است و قصد دارد رقم ۳۰ میلیون یورو برای جذب این ستاره جوان پرداخت کند. هرچند که بارسایی‌ها این بازیکن را غیرقابل‌فروش اعلام کرده‌اند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/Futball180TV/102650" target="_blank">📅 02:58 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102649">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f5d8f16631.mp4?token=ZgpLizEHSb1VRZXL13OK-JhPE3guoLxL50T2rSkjT8VdmQXrrfZIVD3j32JEuzXYJocqLLVWKnmuVH4ZYwOLA0e6ABaAomPDFOXXi9Nl7M_-JjTTzIbmL-74mRJGwCGCek-aFzOF-0CL89SHK6xY6luUN3ZsdtWq8MammAtiHJW8KzBanjTs00ldyLV3T1HuyTw09ZQKzSzhrU_NDyoojN28-xfaoKT-gH4Dole0hQmbHghIhSmsFLeZHunxyJoBvLbhYVzF0xwisXoRnwXpo2QRBTgyEvGV02vUtqSxicU6eNxttC9r5gUhCP6I2iUXqOrEJ30izKZHC1Ni1cymzg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f5d8f16631.mp4?token=ZgpLizEHSb1VRZXL13OK-JhPE3guoLxL50T2rSkjT8VdmQXrrfZIVD3j32JEuzXYJocqLLVWKnmuVH4ZYwOLA0e6ABaAomPDFOXXi9Nl7M_-JjTTzIbmL-74mRJGwCGCek-aFzOF-0CL89SHK6xY6luUN3ZsdtWq8MammAtiHJW8KzBanjTs00ldyLV3T1HuyTw09ZQKzSzhrU_NDyoojN28-xfaoKT-gH4Dole0hQmbHghIhSmsFLeZHunxyJoBvLbhYVzF0xwisXoRnwXpo2QRBTgyEvGV02vUtqSxicU6eNxttC9r5gUhCP6I2iUXqOrEJ30izKZHC1Ni1cymzg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🚨
⭕️
گویا سپاه به پایگاه آمریکا در کویت حمله کرده و آتش‌سوزی رخ داده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/Futball180TV/102649" target="_blank">📅 02:36 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102648">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🚨
🇪🇸
#فوووووری از ESPN: رئال‌مادرید پیشنهاد دستمزد ۲۲ میلیون یورویی در سال به وینیسیوس ارائه کرده و قصد افزایش این رقم را ندارد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/Futball180TV/102648" target="_blank">📅 02:25 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102647">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uuOH_Yp4V5-jDDnDcA8btBUP2sY6-5V0sQ_TGmKFAUAb4iOuf73-9hjO5AZhqNDQvjwxQDBAGOVoVtF7Vt-3cal-zZi0qwNNie3jyoOf9JDfu5E6babyOISpcTimWNWvhnWAZt0gphhPAcbGNDQepwiM5BT-JavpTAreyDhfqmihzP2Q18TblSn6cTmSkU8bNrBp4tVQKbkEcnUBfpVDo6-FsWbJYLezJVLqQyHnEEChvlzThfsf_iJtO-1AuiMTTBs8SksGI0LbhYTU6DpI5B7KCAkHm0SodArywt11LTT47Wafb1-1vNq6BwUuZTBTUjEwg5eU8G_5i0JTabpiAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
#فوووووری
از ESPN: رئال‌مادرید پیشنهاد دستمزد ۲۲ میلیون یورویی در سال به وینیسیوس ارائه کرده و قصد افزایش این رقم را ندارد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/Futball180TV/102647" target="_blank">📅 02:08 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102646">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/obcSzdhUA0nGrDOwQ9N6RDb0Aq1scTLFANmXh-W2ytRDZICMHzV5yhNQOkTGbaaVwtCxVidsICqA9tq1vZtBU2tDd-GyOueIg536VV2ORtUcLsWSPBkzaHOxEfxMtr8MErcxHo92Cgh7_T9QooSNt3IXEPLCoSDSYsgS2FE1ygVR3OC7_XV7zuNNcv6ciUQAWHUq45dwyY6ISM6QZmT5SK8ri0B_YwGPCFm6z86Q3RrDch4dDOgTrD_-Xd8sXGUdkyokU5sHVZyL0ZMamzxfP2dLkqAlYD-YhYpK7ZU_YRNOsCket_KA3ieK3BveHOegLgj2rxPYUbAW0rzbyVwf7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
بن جیکوبز:
چفرین و ناصر الخلیفی در سالزبورگ دیدار میکنن تا درباره تحریم جام باشگاه‌های جهان در صورتی که اینفانتینو همچنان رئیس فیفا بمونه تصمیم بگیرن.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/Futball180TV/102646" target="_blank">📅 00:46 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102645">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YDyZ2VMnL_sKkGYfSa1ovh9Qlb86MC6V-T9N17LjIVkEd6NjWvgPqBJUAIHdJ8cpMBH-_TzwEClEme6dCcePO2ONW7HCD0Kb2qdjxFoCJvRCz6QM5WCCOQ1uf_2Z2KSHtyPBIt3HIl1NvDYeNWyIVFCO2TNAbkzbWmdgZ7RTHTDWUDnXIvKdKTYxBE9i7bdK1XdDDCCCPlIzP2EuqNbzNG6lNB5dUoj_pVDS4hVrJvZ2QrvVoppniep1b3XXnBPBCzneNGUPewkXqQ516hSgxLupsLVCkJ5UwFdrOVbI-kPc5NZuBfCKfM4OuKOrbF-czElViuBHTeCJUhxgZrPTpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
پاریس؟
🎙
فران تورس:
خیلی خوبه که باشگاه هایی مثل پاریس بهت علاقه داشته باشن! هواداران بارسا باید احترام خودشونو به من نشون بدن تا بمونم، فقط باید بهم ثابت کنن که دوسم دارن و بیان باهام برای تمدید قرارداد مذاکره کنن!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/Futball180TV/102645" target="_blank">📅 00:45 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102644">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">🚨
🚨
🚨
#اختصاصی #فووووووری
❌
با تایید تار تار و اعلام رسمی ایجنت بازیکن قرارداد نهایی شد
‼️
‼️
‼️
https://t.me/+W21WaISjE0U4M2Nh</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/Futball180TV/102644" target="_blank">📅 00:45 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102643">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/kZlxLj-srXeOdjonwpmkp9dL65bqFME80BHcihJ0I68kGfcaX2L2Zfj4jVeBYyi2Pj0ZgUc8DlCOKKAd1WjggOUUdYWBIt1R0YclF2kj3lTb_IGKn8vXBWBmI5tK9FXbLAn54sqgprjzBCi1QHto4cuv7cJWy04HNhxMVMBm2nxRMI6s3gqx3irko0tuoZJyZ-zy4OsoLzQPC36tYJqEpSm6kjWQD1rkKs8poPS_Pib51mOEi88JMam3XwMKupqsDo9rAkcERc2vCKyDD9g_mTfmYssXA68SLYySWnhGkshIJp58VouAVzQi_VSjGL_msHAXw90uQdsIY74Oy0PvpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#فوری
🔴
تارتار تایید داد؛ پرسپولیس بار دیگر خواهان جذب</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/Futball180TV/102643" target="_blank">📅 00:45 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102642">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t-HdpzVlCQ6A1k4ckeIS2JT8H2Y1DDGvBLH-veY2bdCiO68Wo1CKcuWhgECDNdMO1ev3vzD8rMPMc32272zMFh7GVZzW2TwW26JBl0E_KupmjBrGZYLbFV07OoszqwPdbDGGHNj-TuoOZT8Lv-eoBfE2Ymm3rbDBP9mQU9SKluaQE3Fypcyju2mS5hNIiLVE-RHAJPBWT0kIRDR4tBGzd1zSuv5Qlx619GiiaTrSthsUl2xg6dm1EUeJNB-4623hwOV57iHD3dIqIFXbIzde7tLTOYsJipRKQoBoqDX2QouXjQmKz-BX1Wu1QsAV4LE-6qRnsVSi0a98N-s0-U6kvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
⚪️
برناردو سیلوا:
بی صبرانه منتظر کار کردن با مورینیو هستم، اون کسیه که برای فوتبال پرتغال خیلی مهمه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/Futball180TV/102642" target="_blank">📅 00:36 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102641">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4b215f0831.mp4?token=i2pKnuFEYWbzylQEMKhSLNd5Kd1uspyZD5LB58rxkQ9Xwb4lbANjhVag7p7wfojCqxIg_xn78tcyatLswYH6knPpmzHcqwgsODIZhLM0EePVZlNXBcRfmUGENUarp__XiFGeGI38Y8Q1upCqmiH-1_nNPY7Ee_gA495pqHwLZzS_ljBCemghkqluw-SkRw_zfA_1Ug2rZtG2OWj7OOfF_gJkHpzEvWsLOJNrHb9X8fBmRlhzJbZZGVVT_B4mCAqE2WDrbKEWd_D0AMEK2LqD-rXd8mvd3O8PgVjgDpM1KyDwvLy21D2ThDmdLRmNjMkD5Dm_ihN-5llVjkiThUubAh_8Hpeb0X3yw_gb_2LxmbD7tM0XndE5Wh3VW57Mf3C6ihWEjwH09OheRRaYgSo3-ZQiI6iv48p9Yppq-Ze2KrKc_FGe-w6_bmHDeuw-VIcRenAaDrR795kl2ZpD8wnZK-K4PVUHOX1FqKZQdiD_XDZLkQ0Cyv92haMqquTdEP9TcD3wPw7KJIgQFv1MP0QtzgdMrCpT13vzKTgiqZ6sTXbED9yJeu3-NaABBiV-edHUfNy2ZfhfOYXUk2J7-YYL8GOS3nlRliGhArjrQ9zgx7Vme0HLEu1783IDPB1DJNEuwx2BQ4DhuzxUs6aLF_92x4uNw19wbrd2zX_Jz7aahiw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4b215f0831.mp4?token=i2pKnuFEYWbzylQEMKhSLNd5Kd1uspyZD5LB58rxkQ9Xwb4lbANjhVag7p7wfojCqxIg_xn78tcyatLswYH6knPpmzHcqwgsODIZhLM0EePVZlNXBcRfmUGENUarp__XiFGeGI38Y8Q1upCqmiH-1_nNPY7Ee_gA495pqHwLZzS_ljBCemghkqluw-SkRw_zfA_1Ug2rZtG2OWj7OOfF_gJkHpzEvWsLOJNrHb9X8fBmRlhzJbZZGVVT_B4mCAqE2WDrbKEWd_D0AMEK2LqD-rXd8mvd3O8PgVjgDpM1KyDwvLy21D2ThDmdLRmNjMkD5Dm_ihN-5llVjkiThUubAh_8Hpeb0X3yw_gb_2LxmbD7tM0XndE5Wh3VW57Mf3C6ihWEjwH09OheRRaYgSo3-ZQiI6iv48p9Yppq-Ze2KrKc_FGe-w6_bmHDeuw-VIcRenAaDrR795kl2ZpD8wnZK-K4PVUHOX1FqKZQdiD_XDZLkQ0Cyv92haMqquTdEP9TcD3wPw7KJIgQFv1MP0QtzgdMrCpT13vzKTgiqZ6sTXbED9yJeu3-NaABBiV-edHUfNy2ZfhfOYXUk2J7-YYL8GOS3nlRliGhArjrQ9zgx7Vme0HLEu1783IDPB1DJNEuwx2BQ4DhuzxUs6aLF_92x4uNw19wbrd2zX_Jz7aahiw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
برخی از بهترین گل‌های کاشته تاریخ جام‌جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/Futball180TV/102641" target="_blank">📅 23:55 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102640">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/290de4f011.mp4?token=RcpGfHRmeQ02nc4HshxFIG92GjANJNMK-rID186IWpkGm9gzneU9nriGomQ73KMJRKgG3f8X0vI7gOOjYZknb8vBcEZmR00fuwpA2vNvsHINhRmkFUttoIn3z5vU8zxvgDRlY7ovkHyf-Dz1zpf336criFlAr-l-W53NQLmBdCNDjHc_xO8bpj5-6K5yYEJeG7aMrTnyE8dIhRu1bcRD7IpDYvRncGc-bXqErLuhL3Fi793udkZCEluAhC1D47THnK8t-aEI8i-vXpdiy3J4NI3kEdEFpydjojFC4WZaY5mMFkfxh8mAZbDwDg-gKfAvAv9E9Nf3kfPweW55BauFhA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/290de4f011.mp4?token=RcpGfHRmeQ02nc4HshxFIG92GjANJNMK-rID186IWpkGm9gzneU9nriGomQ73KMJRKgG3f8X0vI7gOOjYZknb8vBcEZmR00fuwpA2vNvsHINhRmkFUttoIn3z5vU8zxvgDRlY7ovkHyf-Dz1zpf336criFlAr-l-W53NQLmBdCNDjHc_xO8bpj5-6K5yYEJeG7aMrTnyE8dIhRu1bcRD7IpDYvRncGc-bXqErLuhL3Fi793udkZCEluAhC1D47THnK8t-aEI8i-vXpdiy3J4NI3kEdEFpydjojFC4WZaY5mMFkfxh8mAZbDwDg-gKfAvAv9E9Nf3kfPweW55BauFhA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😮‍💨
چرا بزرگ شدیم؟
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/Futball180TV/102640" target="_blank">📅 23:02 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102639">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MTIZAy9ZTRakw1YxTvOYD3GSfikl64AOyC9XrWeMinDws7OVhHEiCyKgxoOj3GezBlyouUc9_Pe3wnwj6kfJSFLYOxo4-ja6sluA-T-ogmvIv4agNEvxdgwpzmDMizoSDHgVIbqbCmcCzt12vhQqOJxhgb48N_le3mG_gAdgZ2WbIKESqEUSwqJBi96a0NKLZMy5JJbJKiFm6IlTblyDDju0dvFOoNmup7SUdaxzH7snlAm1j-4Iw-Wk8mp0Rc4DVjgNGBhJNVy3Oq9qNHUlCvfzjujYGWOaO_qlPelt18nC-qyX6NWM-SwYAqmIKi3dfna7UlX8OUjgmgW0GR-jBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برناردو سیلوا : رئال مادرید بهترین باشگاه تاریخ فوتباله، نه گفتن به پیشنهاد این تیم غیرممکن بود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/Futball180TV/102639" target="_blank">📅 22:59 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102638">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromدنیاکالا- کفش ویتنام و اروپا در بانه</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IC4pYrDWA4Ifo-DAdwlVvQRgcQiorzAHrgh3DyA0LQktav4yrooy_LKRCsctSPdCU5NlJxyPmOaDjO-7wRV0aOflfeJgOPtzKsFDDAylgtj95rBxvx3O6RVr2X8c3Fo1KLQ0kDwfwG72miHYoB9gy9uSCIQ7m5blWkz5UTDP_Kl5HkBAwj0jqngea-p97GaarsuaKoueWbnAVjbQfEuAY6gvb5f-hCUK3_LwoYUQ09bZTgdFjKW-I4z9UQf2qQUu0E4Nn2pRNEtt9PtclKXcmEX1_u4qRAhhaUW2A56RzkEBJsGcDFlRcjUr5BPiZ8jFRxp1IiledudYoVFe_vqjWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کتونی
ویتنامی و اروپا
رو از شهر مرزی
بانــه قسطی
💳
بدون ضـامن
بخر
👇
👩‍💻
https://t.me/doniakalacom
کانال تلگرام مجموعـــه بزرگ دنیاکالا
📱
https://tlgrm.in/doniakala
بزرگترین
واردکننده
🚚
کتونی در ایران با
سـ۳ـه شعبه فعال
💊
کاملاٰ
طبــی
ضـد زانودرد
🦵
کمردرد
🩻
اینستــاگرام
مجموعـــه دنیاکالا
📱
instagram.com/doniakala
✅
ضمانت
کیفیت
💸
قیمت
مناسب</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/Futball180TV/102638" target="_blank">📅 22:59 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102637">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eac45ed94d.mp4?token=i4c9krYUGlryEiQlz8WBm2PNnl-rh0ZnwmJspHdiSge3jjfPGiMAc8W9AsIOopvi86CKDQAZ6fuIDbFzXtuyxkPUcFexvt3XhmB4q6zaC7fre-VCf8Q1DODIcNyRhOEy9bTLG7osloD-CWLTnl4RpIOCVifHPOfEn4e_yiwKhYE4gP2gQcMHionbgmZZffYUgX3X-AcJsCkb8tPVky94x6Qyzsbh0wlcvLv_u-kEK1WGZ9pS1PahIynA_GNLJRaxxTFLuWY_yXOCPGwL83ic1fnJhtomTJieWzQDuQ58n8nTTkBemPGK_iGz7vbPcPDZjfk9ClaDmwMyOEc2R_AX432RxXVjXYx9UA3i3mJseiU9xNKX46ReIYbWCMuMYtBWm2DikoWFIn73VEc6BbH8ObXhQ4TceZeBudUQNk0yRxkLV9NPJyqLOkultPIu7zWYliBOjubo85p49yTEH9NvF0PJJzzQvVHBCs045LNTk1SELDDmlZLda_lL4-ON5EnDYfZgGYdIuXjey6pWHtArsHWL_gxvnCByziDA4CRCO59vJsKobuqnIzVrt2ucNDtuzulSS_bcxCexKUhihXk_IIVP4HfLUsHNxxj5-x4d22FKnBk7h1j0rainFfxEgNE8SL2d53wiHyRsJghrx7eYUAduFi0HT1DubPNG56LRoW4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eac45ed94d.mp4?token=i4c9krYUGlryEiQlz8WBm2PNnl-rh0ZnwmJspHdiSge3jjfPGiMAc8W9AsIOopvi86CKDQAZ6fuIDbFzXtuyxkPUcFexvt3XhmB4q6zaC7fre-VCf8Q1DODIcNyRhOEy9bTLG7osloD-CWLTnl4RpIOCVifHPOfEn4e_yiwKhYE4gP2gQcMHionbgmZZffYUgX3X-AcJsCkb8tPVky94x6Qyzsbh0wlcvLv_u-kEK1WGZ9pS1PahIynA_GNLJRaxxTFLuWY_yXOCPGwL83ic1fnJhtomTJieWzQDuQ58n8nTTkBemPGK_iGz7vbPcPDZjfk9ClaDmwMyOEc2R_AX432RxXVjXYx9UA3i3mJseiU9xNKX46ReIYbWCMuMYtBWm2DikoWFIn73VEc6BbH8ObXhQ4TceZeBudUQNk0yRxkLV9NPJyqLOkultPIu7zWYliBOjubo85p49yTEH9NvF0PJJzzQvVHBCs045LNTk1SELDDmlZLda_lL4-ON5EnDYfZgGYdIuXjey6pWHtArsHWL_gxvnCByziDA4CRCO59vJsKobuqnIzVrt2ucNDtuzulSS_bcxCexKUhihXk_IIVP4HfLUsHNxxj5-x4d22FKnBk7h1j0rainFfxEgNE8SL2d53wiHyRsJghrx7eYUAduFi0HT1DubPNG56LRoW4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
دوران پرایم‌اسطوره مانوئل نویر در بایرن‌مونیخ
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/Futball180TV/102637" target="_blank">📅 22:30 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102635">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/P47N3pcoQi3JL2smPMryCfz3gq6FFhI2Nogf00nZnojyomk4Jdc8TUmrRnCy5kj91qhAZrCvFmDOcqLZULQBj1buX8pwlVJyx32dR0T2i4cIun5loXScoyvD3Dn3XZWu6BiqSSShEYu7j1QtvaWr6gF0IaH1RrzfIV5xezwGCGtYGov8PJKkuQ7ClVx9Gm6wOFyJp6lLGu4vE4bWM1NKbtlDr9282K_V0CMiIIuEnrYHE1bRkXX3Cvj0Hf9etljldIGqlmEKdOrIq8DKObRudvFIPDqKZ3j4TJJ5P7OMo1Yog6YTD1kwANjhuWdObJ33rRuRep-NDZ1LFQHb1e5OAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UCzkR67UHqgrSmXWZHTz7rBTmLrtIcQS7EJZa5Z2RxLfpku5FwzC_oguXv6r60nwdeHFJBnTiwDMnsSmGKosorrV620FxYD7VefDdEsOK2uFFl5jhBinWbUIg98RrvhkwazWUB7b-mUOTI9tIHcUTm6nGQ7_LpzYLMACVTzcK9iMuGe-lPukuUZbhHsuOIGWGAOpb6OSaTeL9-44XuvGFqbtGz2NojEodRc4SOEvoNy7_LhENNpW-kCVhGmqEd-tOjVUJZiX0N7efKKBrErCEuAvGZ2NViAyiyc7Behx59qbkCauKzb6_121Vy84-cz076NfM3hUsbUl8VHROmNitg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">وندا چقدر چاق شده
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/Futball180TV/102635" target="_blank">📅 21:48 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102634">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0cbde7fbeb.mp4?token=LkzpuNqKiSEPnPy8WjyZsO3RPBYfRr74GMZWwHBS-vFAEWrtjATkgctxuldnPDFNMq8pBQwc3Z6BuasmnmOv_rVV4P_uMdrgF7RUBOPKiXdP_gJwU2aaD1ic6SrQAHCy9DSBd8ysOjxj-hSUnyJMf5Hcj1q6fnq1rHnB4VOPmj_-RdlKRO29DLkyirObDkOpSKDPLvYv2vuZSAeXJtarf0DNvo2wX3tr_fKPxSlvkkzEt17LqWfKL0s-eNMH64lsqNRTYsN-8f7OX90mDAOsub5Ed8fVCZ9eFG9LyXXL6NHvzjyyFEccMZcTIQ2HaJC0xQfbQGBf4XtiPM_dWi0rkg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0cbde7fbeb.mp4?token=LkzpuNqKiSEPnPy8WjyZsO3RPBYfRr74GMZWwHBS-vFAEWrtjATkgctxuldnPDFNMq8pBQwc3Z6BuasmnmOv_rVV4P_uMdrgF7RUBOPKiXdP_gJwU2aaD1ic6SrQAHCy9DSBd8ysOjxj-hSUnyJMf5Hcj1q6fnq1rHnB4VOPmj_-RdlKRO29DLkyirObDkOpSKDPLvYv2vuZSAeXJtarf0DNvo2wX3tr_fKPxSlvkkzEt17LqWfKL0s-eNMH64lsqNRTYsN-8f7OX90mDAOsub5Ed8fVCZ9eFG9LyXXL6NHvzjyyFEccMZcTIQ2HaJC0xQfbQGBf4XtiPM_dWi0rkg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قوانین به ظاهر ساده فوتبال که نکات کوچک ولی مهمی دارد و در لیگ برتر گاها داستان ایجاد می کتد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/Futball180TV/102634" target="_blank">📅 21:25 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102633">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9b862859bc.mp4?token=M0z19UtfoK4vK2IF58vGP-JainG2iN6jFGWZRaxqD3Vz3r3TdpkNZZXizGyHk4evqofnZsxVO7CzyUziuAbxMHJF9kt8fP6rFc4dHy9S0Jc6p45MxxBlQ_YsO52aUxPZHJ57X4RaAr3bNRKr4DysLUNJuAEp3S-xr_4Lljb6sUPHfgNGihw16YRbKlEJd7OzvsqA26ImDXOQqCH22MF62Uj599Bln9CYvbrAm8S37jJY_k4HH2jIh5RSZwHpgSbwJxIa8JjHUqR8yWKGndIFgs4uaYBs1OLSRydbXedDTAkSCvwm0IObvPImL8uOneNl0d_xRPSzxZqh_D-tzf-5NgWxmn0e4T4Fc5ArLRTTVD9e7tW2SKsvhL0e_9x2sjRiKwHQd3M4veo6rcVK3BTAl_ALkPZyP-04FfS-PKkT8gM9Az3dR6mmSPAwgDbveBpnqkCpn5gipXTk7a_w_9z7UWoaIM-j5lbQoRd9XTMEgOKbcrqsFs32fCE85sWr43T2f25vb8sn0f9A6R_wpRVbZ2mxuLAQOYy9XX5LsHlKkYqIIKaike07Kkix3Z1t27_RuWJFdWyaXS80F3QJlrgCv7T3Gp3Zk7kt6AT08zMn9P9AwvfzTZNZjhr-qs_kO2-EzLUG3MUItUk3u8S118MleHenem7pP82HQqgFg840edQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9b862859bc.mp4?token=M0z19UtfoK4vK2IF58vGP-JainG2iN6jFGWZRaxqD3Vz3r3TdpkNZZXizGyHk4evqofnZsxVO7CzyUziuAbxMHJF9kt8fP6rFc4dHy9S0Jc6p45MxxBlQ_YsO52aUxPZHJ57X4RaAr3bNRKr4DysLUNJuAEp3S-xr_4Lljb6sUPHfgNGihw16YRbKlEJd7OzvsqA26ImDXOQqCH22MF62Uj599Bln9CYvbrAm8S37jJY_k4HH2jIh5RSZwHpgSbwJxIa8JjHUqR8yWKGndIFgs4uaYBs1OLSRydbXedDTAkSCvwm0IObvPImL8uOneNl0d_xRPSzxZqh_D-tzf-5NgWxmn0e4T4Fc5ArLRTTVD9e7tW2SKsvhL0e_9x2sjRiKwHQd3M4veo6rcVK3BTAl_ALkPZyP-04FfS-PKkT8gM9Az3dR6mmSPAwgDbveBpnqkCpn5gipXTk7a_w_9z7UWoaIM-j5lbQoRd9XTMEgOKbcrqsFs32fCE85sWr43T2f25vb8sn0f9A6R_wpRVbZ2mxuLAQOYy9XX5LsHlKkYqIIKaike07Kkix3Z1t27_RuWJFdWyaXS80F3QJlrgCv7T3Gp3Zk7kt6AT08zMn9P9AwvfzTZNZjhr-qs_kO2-EzLUG3MUItUk3u8S118MleHenem7pP82HQqgFg840edQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پاس‌گل‌هایی که ارزشش اندازه یک‌گل بوده
👀
💥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/Futball180TV/102633" target="_blank">📅 21:03 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102632">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c26f6b0dfb.mp4?token=vRU554IqIuraZ3s6R1ZghHL4i0mR9PIM017-e3Z2bfrWnFq9gRp9RFBZOWtUt_5IJaP94oljIYYGp-zGFkDnhMWdBISMVNJoau3c8yleqZfHQSaaWbROpzvs9pLJeafbiOnh3pOkVo6qqjgIT8oLUUYQZoPmPzXJM_0ADNtd0ps6XzUTeDyaqPibxBn3zuL-AIXVLjTDix8JGH1dp-SkRkWje7zEX_l71oniJcBFQqFfSuj7qTafvxdno4Y-6okFXo9ucnnpabl6Z7WyDoua84bQs3eMcUXwpRWCwSm1SVItsGeTFAc2ptDyR0L2ktpGwBWBFbjUn4jO6-s27r2sIw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c26f6b0dfb.mp4?token=vRU554IqIuraZ3s6R1ZghHL4i0mR9PIM017-e3Z2bfrWnFq9gRp9RFBZOWtUt_5IJaP94oljIYYGp-zGFkDnhMWdBISMVNJoau3c8yleqZfHQSaaWbROpzvs9pLJeafbiOnh3pOkVo6qqjgIT8oLUUYQZoPmPzXJM_0ADNtd0ps6XzUTeDyaqPibxBn3zuL-AIXVLjTDix8JGH1dp-SkRkWje7zEX_l71oniJcBFQqFfSuj7qTafvxdno4Y-6okFXo9ucnnpabl6Z7WyDoua84bQs3eMcUXwpRWCwSm1SVItsGeTFAc2ptDyR0L2ktpGwBWBFbjUn4jO6-s27r2sIw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
فران تورس درباره آینده و باشگاه رویاییش: "میخوام خوشحال باشم..."
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/Futball180TV/102632" target="_blank">📅 20:49 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102631">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gQEZ9oGzj9SgRDHZW69Yojh58thRudhku91fX_Z3_Dq9s4pbG2_Wb6BiMYioHS4WjKJfRVGFyWjnzoj9yOstBIFPDUUH5ILxboqWdVw8ACT2OpOHp13mm-xToNvx9hwqC2IDxmb4WsbjBboem2tMAyWCh8VOD3W-WtYEkhuslcQHCqvSGkeCyeOqlAYY7p1RKGvlffVrT7r4UnE5ZEMGeX72k6T5afbtZfJVQDhcu5MuhD3qFSLj7Kj2rbv20EHA_YjXP4QmVN5RwEI4BighHf7AXkdvGIEDr6SAkvK-_lRN9lGyqUEgVunJPVMY5LDeOy-J9PvIslMNc72fva1obQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🇺🇸
تلگراف|ترامپ تمام تلاشش رو میکنه تا جیانی اینفانتینو همچنان به عنوان رئیس فیفا به کارش ادامه بده.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/Futball180TV/102631" target="_blank">📅 20:29 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102629">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bL_uU4L-oyP1mwwQY0YDMe_421f18p19Rc4-JhmvYrFJ7b29z-HyjSAbncvWnXDVAoJOxbrVcYPuYueC2A9E6wA7bN2YWiKmjugunE6m2S3gIhC3PDnWKAfLm78bk0YU2MCyHOARToN4bf0yBa26Tcz8WeYN8CFCmx1WD5etOqggk-mdhaN2BkNd2QFXYO9hF9eHku5qr7BPNgEnsqFsbmDfDYulNcbjCaTD6E3eS4-q4o0HpAaxHApf6RcACM2pDpCS4Dg6gRK_OeRjxAVp88k2bY2hXNYwiOfxyVJx8H8YrpxLkGZVTVMTt33CNoLjJsVuHh3DQB0wWz-x2xHVRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dBp_h78_PFRVju_be553NeIhTCVsdIC9cIsqlSUQh6vcUeVJRHPHPafXyZOJoeO7qV7Z2bx0mTPDhMXS7X6QCkXI8Z-Aayfql3-A7PniWentmkw6SUR52el6KOcdfHr1I_IKiRFYVT9HKOBOnbPd5-sN-SJpv007zO-jpyGER8zjOgUkxBO7BmOYkECr8X8hmpt4huNkWZS-TbzUFEMDCISEedQSn5eJ45FKAWTQUvldRedICZ4993JLYiITdHMYnSaodSKLDvP42I1kZYwH1d0w0GI7b3e-PnRhOP5q7YnIts1dEg8KpxhkQSW8oPWUXtggIl1cuDsWSMCbzgX6lw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔵
حضور مودریک در تمرینات چلسی بعد از ۲۰ ماه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/Futball180TV/102629" target="_blank">📅 20:21 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102628">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rIQ7AwFedl3hkSuEd01Zl88pk8aMka2r8vRBh4UO9AcKa8kRCoFToLrXRNG6ZY3HX-woErSjXE0j4R7PRbobNUHvrhhel6s3rDSbOkNF2jCl9Z7C1mQLbvfstlV_wxxlvpaIHpn2D3li1qq95Ik4a5I0159itZNUKH4eZpCqVR3eGyuohiS7Uyki5nAfbDfRZFHrV_irNym0cNvyQrGFVcMMkMkYBzOgQHIKoiOVJHvvulRaY2Rcop-xRmCNsxB3DNnL3sCQUTf49e5rPm6rZmzZ8h2HAyjbVK7FVbanvk_s1BW10lLe4yPdJUn3ZCye7kgEJsO_9AwdF0YtHgMmtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
فران تورس:
در حال حاضر با بارسا قرارداد دارم ولی تو دنیای فوتبال شما هیچوقت نمیدونید چه اتفاقی قراره رخ بده!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/Futball180TV/102628" target="_blank">📅 19:46 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102627">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/590393501c.mp4?token=t7VESgrDFUVcqmEFtaFdqTCgBiRFmw5qfkQLJZv3Y3CqoAptRRi8kzszNZ99wQgUlSyJdJXdwTcoNBTXWXl2wgB_c8DT9-_8D7GXWpbpFBjGgzuF8nAk185XW13ymXGCho3W4FeKscSgtaCID2UwEkx3I6jXk_XecZec-4nP0v8HHZF4wc9ggGPPS1q6TKNPRA_n3O22RGRD2lXHmRl3NGkOjfj2rUiOY8FDsf-hsWPTNBkQ0uNxNoH6gyME-rxx87QN3yfc7Z3vHp-h9BFVkIPYRxw_JwuynpBRgoFIngsTfhExGACPEcuIugYei_zkOldLWl3K7uwNy8D1ClXYhQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/590393501c.mp4?token=t7VESgrDFUVcqmEFtaFdqTCgBiRFmw5qfkQLJZv3Y3CqoAptRRi8kzszNZ99wQgUlSyJdJXdwTcoNBTXWXl2wgB_c8DT9-_8D7GXWpbpFBjGgzuF8nAk185XW13ymXGCho3W4FeKscSgtaCID2UwEkx3I6jXk_XecZec-4nP0v8HHZF4wc9ggGPPS1q6TKNPRA_n3O22RGRD2lXHmRl3NGkOjfj2rUiOY8FDsf-hsWPTNBkQ0uNxNoH6gyME-rxx87QN3yfc7Z3vHp-h9BFVkIPYRxw_JwuynpBRgoFIngsTfhExGACPEcuIugYei_zkOldLWl3K7uwNy8D1ClXYhQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
قلیچ: علی دایی مردمی هست، من مردمی نیستم؟!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/Futball180TV/102627" target="_blank">📅 19:33 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102626">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/Ida6lu67h6SJv95t005ro_WmLXdGx9JbBeBk_Qo88jQcCLTXkOCZPTYKqOfVNTM6siSjbySEB0bJmnj_NMsT6YAz-FC3AikAZLhK817OkK388mGZ_tI8aTuPIAEZFapHatQx_vGVEOctycekW7Fl3xrDlncNPMwkxB2GaOdXo0bflngUmkAWOVU8Ekb2XCubq5yscyi82tUxHkjKZ9pHYa-XaglSrvSb0ElMNpfHiRiBqbHvfAyTfz7iBJYv6mywmiSepLWzDHjvS5zR1wutENwtcV5HkcLVEWCGmyMRQc_YObRbK7RCTWKoGYJwfNb7i7KcvwUltjEOlecFl7Mvww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇪🇸
باشگاه لایپزیگ اعلام کرد که پیتر گولاشی، یکی از اسطوره‌های این تیم، به ویارئال پیوست.
این دروازه‌بان در 11 فصل با لایپزیگ حضور داشت:
- 362 بازی
- 117 مسابقه کلین‌شیت
• در سال 2016 با این تیم به بوندسلیگا صعود کرد.
• 2 بار قهرمان جام حذفی آلمان شد.
• 1 بار قهرمان سوپرجام آلمان شد.
• 3 بار بهترین دروازه‌بان بوندسلیگا شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/Futball180TV/102626" target="_blank">📅 19:32 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102625">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QY7GJt4kPxIsLtJXPBeOXnEIzkkGIeiNePoBCHrxSpA1RETabLc5gQoUVG4fDjSv-rLvA36BTzNy0XV1kbw8okZoZGt4SKf1qGphpKZElUSPZlFto0Gb4IoDX-ozcFxlC8ainzLF3HFq7IaBQYgJcVWvBdC3apxFmReGSkPmIb5F4gPH-uZ39uvOPFPUtKWPV4zCMOnv_gofM6gz3sh8Upc5VyqftsYQ-HwB5cbOS56cWNH-5wAMgIctQh3bi0V7OJIIS2KHUtb0rGoQ9wpZxGBqSh3GtZ0W4W-zrFiYR6wzy6XpV_6ixMAYH2eGACAQPo8vlPKhJo2OFXlyTP-_ig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
رونمایی رسمی چلسی از جردن هندرسون.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/Futball180TV/102625" target="_blank">📅 19:19 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102624">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Tv4zUHj7fEcYKzoHXS2R3Pv9t2JzRQy_pmSxo2rhDr1kGU83NJKIFNwLbQWgscPoAVS9Ld8kbjKYGQHGwkbfYMvPeKAr0fu4zK48acWPXC91FQ1TT4TTpYXr_ZpO7CVg8un1RMTd16z4_lqjZoSQrPHaS8fiyW-Kjqla7FGRmcTAoFr66tfwW7qdCaWKP4gIVdlLcVJYEbsOiL-D3LWmznRV9RJP-7RtykFvt3DVt6g_waDsY87Y8c3igUjIi-Krqg_MviqBWQnMVzpuin3eoF08daH1iVdFXSe6f6Y2_z-qlN-BhwAJmFjg9dnzjg2OX0j39nJiMchzXgb2Ey399w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚫️
ماتیاس یایسله به کمپ نیوکاسل رسید.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/Futball180TV/102624" target="_blank">📅 18:51 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102623">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/16357a3407.mp4?token=jbbPiACl6784LqXwAm9BgbiQ3YHdQSLYYzI4MlATX4cc-VGxCSZOy1n9CtbVver1ccpn6_1n83RDBYeVST4j3HqbhIMVz-ZIcqsUeJcmWP4iODhGB6nxWHZlbTh7PgUqiqG1H85uw2vtdb6dMMepWRQ_xs-UqlBCKMcucVaQVgVjv_l3k_AACmlmc-xXJmmYUiXUJv8kbVm0xeseWyK71YbEKm4pHGnny7H5HNe2czAlZc3e7MedW6SLvY-hOgnrGz4ij_sh1nHoWHD5QPmGHrrlT00CIOjRjl79XlrDEgB1_SLMLq0DduJ3K4cyA89e5-i4EpfBqdTOj68EYCS_nQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/16357a3407.mp4?token=jbbPiACl6784LqXwAm9BgbiQ3YHdQSLYYzI4MlATX4cc-VGxCSZOy1n9CtbVver1ccpn6_1n83RDBYeVST4j3HqbhIMVz-ZIcqsUeJcmWP4iODhGB6nxWHZlbTh7PgUqiqG1H85uw2vtdb6dMMepWRQ_xs-UqlBCKMcucVaQVgVjv_l3k_AACmlmc-xXJmmYUiXUJv8kbVm0xeseWyK71YbEKm4pHGnny7H5HNe2czAlZc3e7MedW6SLvY-hOgnrGz4ij_sh1nHoWHD5QPmGHrrlT00CIOjRjl79XlrDEgB1_SLMLq0DduJ3K4cyA89e5-i4EpfBqdTOj68EYCS_nQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">واقعا فوتبال ایران بهمون یه ممد مایلی دیگه بدهکاره.
😂
یادش بخیر...
واقعا فاز عجیبی داشت
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/Futball180TV/102623" target="_blank">📅 18:25 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102622">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">ویدیویی از شعرخوانی یک جوان بلوچ در باب جنگ که حسابی در ایران ترکونده
❤️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/Futball180TV/102622" target="_blank">📅 18:00 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102621">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OmjGgLRU8R8gelBT1OmhHvQb93g0fNuHiySK0uHo5XKS211l6TUMBAvnaRPr6_cVt7HKZsQNXZCPiC9l6jFdn3UH4u1pHV2R36WtJqrMvctdkjEhA1y9qE0_hMjTaw4Bz2aX4ZBsEmr8Uf36YRs16Dd08rVsXgBF9rWhE24R8iyn20aXEbc2bnEXP6--6nUTi75yEDxnZLU0zVqTH3nlZDkIsd_TjI7ntG0AYAEmI5-oIqOe24ua3RX0AqCJdISDvPkhRrfjYq3VJsgyOBNUZ-yf9pC5eb2Km2lwakNoZCNhACeqnKHvU3XgD09qb_d0V-q4kHDYPGObRksVtZ_vvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
مسابقات سوپر جام در ماه آگوست، پیش از آغاز فصل جدید لیگ‌های اروپایی:
🔥
🏆
• سوپر جام اروپا:
• [
⚽️
] پاریس‌سن ژرمن
🆚
استون ویلا [
⚽️
]
🏆
• جام خیریه انگلیس:
• [
⚽️
] آرسنال
🆚
منچستر سیتی [
⚽️
]
🏆
• سوپر جام فرانسه:
• [
⚽️
] پاریس‌سن ژرمن
🆚
لانس [
⚽️
]
🏆
• سوپر جام آلمان:
[
⚽️
] بایرن مونیخ
🆚
دورتموند [
⚽️
]
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/Futball180TV/102621" target="_blank">📅 17:48 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102620">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RVJc3T7-K_z_-FNADpcWFO5bLO82bR4REeyPDw2RbmaKikD10mrUlel5xJOp4753he1NpTDMJRuM5KVIIm64vkvUt-VYMVLjv7h2WAQ5LHtPKvPCBQgjWDSrXk24t9q8_y4GH8FHf8CH07uCYmyaI4yuiRzJXqRSReC66-PeqVkroOtzv1BCFtS0YrjBM79wid_rQyniKQL-eYtz0eoRT5te5kE7um5YdLk-pIVAPwgZGSGw0M6ce2zj6hEN3DvANNNJ8NkTOFBiZjiyJg107HfOmIGyxHAffE0fF8YHNRFMAcnyiFHdjrJfTLPCEHPLnv_z2zq_mawNBlSl24Xefg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇮🇹
🗞
#فوووووری
از رومانو: چالوباه از چلسی به کومو با مبلغ ۳۰ میلیون یورو
HERE WE GO
🔥
🔥
🔥
🔥
🔥
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/Futball180TV/102620" target="_blank">📅 17:32 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102619">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A9XHvEExMXUm7zs505oG1fdlGiGWPjJejiiY2R4uX1yiElHUMpp1XC9GaEY3-R1uwEeh172oFRIVMgclkcm3Qv_YlB3GeOOhBISuXFc5D5XWGiro69N_mkHdjOywio1xxTh5zCs2GDVNjhRfuEuFbmqZgWfyTkrwTs_baqYpSD6T_qjZVnVpuikwowEYHR50DwIIxYjDUeAVhgJPSkJbf80yoUB3eW282tbbYcTPTbq7jnOSySjIXICuCLKICcc7FFbKgO8qgmqSv3siFz7hvfFBR8N_v2F8qVpyFUx_8MPUIMMJjT1DV5Oydg4lMn-YscA1a_0CIbcyquMQargeRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇺🇸
پوچتینو تا پایان سال 2030 با تیم ملی آمریکا تمدید کرد و به کار خودش ادامه میده.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/Futball180TV/102619" target="_blank">📅 16:53 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102618">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">سیوهای تاریخی گلر‌ها در دهه اخیر؛ پشماممم حقیقتا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/Futball180TV/102618" target="_blank">📅 16:34 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102617">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O8RLU_PwKJm5ZfPjrO8cMkx_sBECCVWc59KJpAsZsc5fMk31CePD2lxIumlU8pfPRzQbvB3ADZvxxQvMJAiMvmtfLch76yr-mBz0XQxzm607h25jUIDWxLs_gr14IBRCzdz0luFNmdPTPHmnd6CvQHT_c9LF5OTYq9HXfh4A7CMIXieCtNJ475GL3VxnauqpxUH0T7YW0rSULUzVfYEByN5ztM3dxcuk6CnFeHdVjV9mxck5JXuRM-G8MPx70GYRue0a2Vfl_hBlKl14CWKOVrmHrpxV8E7YmVIjWqwz9nAnoz3N-SX6vIDzXQUXirnPUuffbY4TfelT6Hpf4Mf5Rg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
دیماریا:
بنظرم مسی تا هر وقت بخواد میتونه فوتبال بازی کنه، اون تو 39 سالگی نشون داد یکی از بهترین هاست و هیچ محدودیتی براش وجود نداره.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/Futball180TV/102617" target="_blank">📅 16:26 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102616">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1714deeba5.mp4?token=dafRDqzX1Pde4TT5We3h_FcnybPiI3dMGbx02vFqLyCf93Mv6MxmrZsH8ea4TodxTQFaoulLxgbCBxgjw2uyQeyfUQcCw3CqnIqsEOPg7PegCCrjJ6BAiFsE0WkKNK0ocqw_L6tia_Gm_millWZwJ2JR3ST1MZAc6na80zfEzDwY-bdE2GwrplmiSn4RmiZ3xfXJrDtnTuM51IVXiWd-h1oq-wcVwA2NmM84TZigXTHWni_w2rLt8pSXVNaFpcvhmKsmFH9HP9f3sVRML3wrFWWwSJKCbFz9nietbqLKepoQoe74nMUL-9kxLcifDIpwqwc7ICPwDza4mn8ANXRptDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1714deeba5.mp4?token=dafRDqzX1Pde4TT5We3h_FcnybPiI3dMGbx02vFqLyCf93Mv6MxmrZsH8ea4TodxTQFaoulLxgbCBxgjw2uyQeyfUQcCw3CqnIqsEOPg7PegCCrjJ6BAiFsE0WkKNK0ocqw_L6tia_Gm_millWZwJ2JR3ST1MZAc6na80zfEzDwY-bdE2GwrplmiSn4RmiZ3xfXJrDtnTuM51IVXiWd-h1oq-wcVwA2NmM84TZigXTHWni_w2rLt8pSXVNaFpcvhmKsmFH9HP9f3sVRML3wrFWWwSJKCbFz9nietbqLKepoQoe74nMUL-9kxLcifDIpwqwc7ICPwDza4mn8ANXRptDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⚠️
🙂
بعد اینکه رونالدو و جورجینا با هم ازدواج کردن، ملت شروع کردن به ساخت مراسم عروسی با هوش مصنوعی ؛ از حق نگذریم این یکی خوب درومده
😁
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/Futball180TV/102616" target="_blank">📅 15:45 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102615">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2c41942b27.mp4?token=YB9o5Sf4d9RVVLVUxfiVg3SA8feAlJA0lg6f4Oq6u4nbJim0Jyx7FdSNltlJWxz99Fzbd5LTLGO1c-yCD9wb6hRl2YjYfvhvWD3Gaur4C38Tb-3eQGGS0mqUuhN1Re8cVjOODYtUCtZHd0Hu5AjaXdvbUTPr0RVAPsN9lJh3GDDqyVfffb1pZMH19_PFNJfUNutPiZuGGN9j6N-P7KOt_A-giKq8_n-Pf9GE0PgVQt6v8RgwKpIW_6E8MD7CazslUHsCJigVBWlDJlNdMaYZ8lsUHF1-xRWL1WUwh4scFK3JzFpVthIaXfLw4rNX0ezmhZOzVDyYtpT3n8KP3Mlp1A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2c41942b27.mp4?token=YB9o5Sf4d9RVVLVUxfiVg3SA8feAlJA0lg6f4Oq6u4nbJim0Jyx7FdSNltlJWxz99Fzbd5LTLGO1c-yCD9wb6hRl2YjYfvhvWD3Gaur4C38Tb-3eQGGS0mqUuhN1Re8cVjOODYtUCtZHd0Hu5AjaXdvbUTPr0RVAPsN9lJh3GDDqyVfffb1pZMH19_PFNJfUNutPiZuGGN9j6N-P7KOt_A-giKq8_n-Pf9GE0PgVQt6v8RgwKpIW_6E8MD7CazslUHsCJigVBWlDJlNdMaYZ8lsUHF1-xRWL1WUwh4scFK3JzFpVthIaXfLw4rNX0ezmhZOzVDyYtpT3n8KP3Mlp1A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
یه قانون خیلی جالب فیزیکی تو فوتبال هست به اسم «اثر مگنوس»!
وقتی بازیکن به توپ چرخشی میزنه (مثلاً یه ضربه کات‌دار)، توپ تو هوا یه مسیر منحنی رو طی می‌کنه.
ماجرا از این قراره که چرخش توپ باعث می‌شه هوا دورش نامتقارن حرکت کنه. یه طرف توپ، هوا سریع‌تر می‌ره و فشار کمتر می‌شه، سمت دیگه هوا کندتره و فشار بیشتره. نتیجه؟ توپ به سمت فشار کمتر منحرف می‌شه و اون حرکت پیچ‌دار قشنگ رو می‌بینیم!
برای همینه که تو ضربات آزاد خوش‌گل (مثل شوتای دیوید بکام یا روبرتو کارلوس) توپ یه دفعه زاویه می‌گیره و دروازه‌بان رو غافلگیر می‌کنه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/Futball180TV/102615" target="_blank">📅 15:25 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102614">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4b784bfd43.mp4?token=XtIZQyirZ3Jx1WB0xrL0BZlPeVzSa_X0CFg6TkFBTwz6RZR6nDYexBLWLCH6BfrBSYaXQ8Xwq47_xGq-j55mu6RzaZv89IOlfIgXWjeJZulDYPHlUbktHvKz7eZE5m9Yl3C0Wd1JxAmcSlb2kmcn_jn-aim0bwfgzwfa5-Rxjk66DYfFUvA5l1a66P40CY4x2Z5h-useyMKtmGD-P2S273QdEN8DZwa9gooHZcW9BBL1MudI5Sz9vajhhGPUVUWHbAhSWDGZ08Ixdua7NA2cjShSjOUwgrDOKVW5p2BFc6Q3RTcxvTu8theZK4YSVULb4cld6BMJAj2uTWjZ5gYxVQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4b784bfd43.mp4?token=XtIZQyirZ3Jx1WB0xrL0BZlPeVzSa_X0CFg6TkFBTwz6RZR6nDYexBLWLCH6BfrBSYaXQ8Xwq47_xGq-j55mu6RzaZv89IOlfIgXWjeJZulDYPHlUbktHvKz7eZE5m9Yl3C0Wd1JxAmcSlb2kmcn_jn-aim0bwfgzwfa5-Rxjk66DYfFUvA5l1a66P40CY4x2Z5h-useyMKtmGD-P2S273QdEN8DZwa9gooHZcW9BBL1MudI5Sz9vajhhGPUVUWHbAhSWDGZ08Ixdua7NA2cjShSjOUwgrDOKVW5p2BFc6Q3RTcxvTu8theZK4YSVULb4cld6BMJAj2uTWjZ5gYxVQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
‼️
خولیان آلوارز همچنان در رویای بارسا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/Futball180TV/102614" target="_blank">📅 15:01 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102613">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qmvN5l1oujrwx1ConkGRW9hanOkw7qbDxEAXhO3WCVbQ0nbYAUMRCSQKGm8Yz6tGFzCnu25F1z9jyzSOLL3CT7-3Ha32MGIn5svNg9O2Di_6lV_dO5tHxIrxX7rYT5FuqnOyNNs9viTTi-0XeGabCGeInhiJPiQYupNoqdBpBmiYAyLRxougBLeKdFA8G8NeXzZHRMNatq7PTyb4ARoJUnPfZGI98VN8rhO-XqmxnvlPJyp4hxpTWw1dba5xmbOouK5RYFGL_WXXVHEahBwV30NyaocZFwuywlUY8n_oAee587qqtefF_cb2Dhxb1gYKhQaZR4e7yf7O7luswtz2xw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
استقبال هوادارای کولو کولو از ووزینیا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/Futball180TV/102613" target="_blank">📅 14:55 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102612">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uMtEBnWAfo6MQuL4zJZefG-PkHHZuNDMN6lAvTUN25iGAZbSKnkL23CBwADjelm8HxEgoO3nGHK2bWV8YMc9A6uw4s2xFQ8aPigSeL77OU65JLS60GfI-Y44kAjpTcyCgMFvTB4y_O3O5DtBDvzaTW8PFxU5pfA1JtXaXsDMCEz1UFrt_65k4ecWyW6UVgrXHctwZ-C1mmLz5fuR21s1HlfO2Injg5sEmOL5Mmm8tddMK-2wCpCz6AsVQL50bXXF0hQGctzQzBd3f5NdSqPIlNvTfng7Ia70tbtCcUfthA70IdjLIP1B4-hqssw9UmHoZEjlaejuP7WLNBj6STqdew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
🔵
مودریک رسید به هنگ کنگ تا تو تمرینات چلسی برای فصل جدید شرکت کنه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/Futball180TV/102612" target="_blank">📅 14:07 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102610">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HiNt9YrMDtSIBgsCICF9r3lC-71dsy0raKB3OlYRLOo-qucAJcd_2DXCJJidCrBsJEFhFs1_A6YY1eWxwK7ALPHOorqnZ2eA60yk9cc2sPsOz1SXRcyGo-aGavArMA4MXFj96R2uQvagsF35G_DtG590yaEDbSIzX3hVDihW9EcHOjBtlWQuegpLPSRIphHtjdTHMmNYXgFuUb8UVc5PzZLjncGyUoqtLLXg7mXUHH5XAIoqVoUvEP6jxRPyU3JTvTwGhuDQctuA95s4ke0ECjrgIkcIoiU8zx2rQ8MzlyYi4NiBQYOpvxwwehNOINGh-Et_O-5gmnaf3uLAVhuBWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MyQE3GzmvD9-ZrYFMDyadpR3tX076kMI4ZTONVcznzuKfgzdVW-Y3-gd1ms2c_SVf1A1Kn025nYXzCNi5F3FgIoEOk_N3Mf4EubUtrjOfB49Z0TZCtPUujEuJfYqTYG98hIhKl_-8qz2T40Kt0Ess3mhhPZWo4eSMZmS4vBmuhNRONx2jRUCkWQLmSJ9fNh7kDYui3OhOggqaEX6jCbU6RK2GyymnWSIZrT1qNOvodKIg6B9BUI1rQmCvZaNOoqFYOrfOuLqhYlJNO3P5z3j-fbY8Lr28Ys2CPBSrrNSOnDQqWLaQODfvZYxWR4KQvnh79fRdBMrZXjvQf2V_3qHvQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">اینا کامنتای زیر پست بنز و پورشه نیست؛ کامنتا برای خرید پلی استیشنه‌
😞
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/Futball180TV/102610" target="_blank">📅 13:40 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102609">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/25e039d9b9.mp4?token=SbKCaQJPS-BRc9rCJhCxFRzG9rafSOBhNTe2aKWKyGIfPcTVkTG_5YWdxg5Pz-TmPAqh6EulrqSTCglIO5nK7Mugz6CaUVjPVNHIltM9BbsJ0c78Ppf8Eq_ubGkgNTrcuHuklcoY67y7qbwrMxVeROnGyFk8aAqlV2ieaZ8QGQ2MfyjO_lLhaNm71QWacdbKflPykV5W5TVS_s1ij_sVQO77AFPfiFukp3IjebIDWj7JgmDRnJriNWu35swhsIM2Ef76v3MLhMe4Jsqv7fN3uiE0brPHIj7BZq0AKYWsbBGUiDuBFyNQ7Wvyc8vrfO0Tp36xnl7ZiToXiT34SuB47Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/25e039d9b9.mp4?token=SbKCaQJPS-BRc9rCJhCxFRzG9rafSOBhNTe2aKWKyGIfPcTVkTG_5YWdxg5Pz-TmPAqh6EulrqSTCglIO5nK7Mugz6CaUVjPVNHIltM9BbsJ0c78Ppf8Eq_ubGkgNTrcuHuklcoY67y7qbwrMxVeROnGyFk8aAqlV2ieaZ8QGQ2MfyjO_lLhaNm71QWacdbKflPykV5W5TVS_s1ij_sVQO77AFPfiFukp3IjebIDWj7JgmDRnJriNWu35swhsIM2Ef76v3MLhMe4Jsqv7fN3uiE0brPHIj7BZq0AKYWsbBGUiDuBFyNQ7Wvyc8vrfO0Tp36xnl7ZiToXiT34SuB47Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
عملکرد ریدمان دومفریس در بازی اول با رئال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/Futball180TV/102609" target="_blank">📅 13:30 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102608">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ls8lmOWNqy1PKpE9tajnKbf4M6sWe5MgGugTYUdhc43tpvhkzO6wALA3fkhzZzSfuI8lPKGPbJ8tPL2AKfg3WEDYpuLCAwCRygNFa3TtlG7QgWlfMIApMKGN_XFt7LUPoR5EMz8f-TEb4BQq3GKX9HYKQA8QnLEuia7_zR475fy1mNWn4yxRW8sDZ4i8s3IYmOchJEKGyY9NuJOSbMI3BnOhL70QKSPMSxH35dEXk8MyaQdEv9saUVECzWixBm_eJxM9fNVRu-3hT7fp67ngIVzfkxLmpAPZ9RfpPBxYz0hb7tJD48OCC90op3mGx_Azn9vKAEfsCvbrGBsuwHWDdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وینیسیوس بعد از کلی خوشگذرونی تو تستهای پزشکی رئال شرکت کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/Futball180TV/102608" target="_blank">📅 12:53 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102607">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9d0946d726.mp4?token=KLQyelrchksA6W1PfzJ-UJM2zuaNu59npEyjN9rdmTgn7FV6noRgUyhOwepxXI1d4Nw0ZgQAwj5-Hrhasvwvqg4-C5aGP8ViukZbxzV6CjV05VHO6VfYsWl2241GhrfIGIjcaaUtguqkssG1j_fbQ9DqWnY-JYRnvWNBJ1zrJLnz4oBHsKyt7Ct4aBcMovEtAozpDytbpV6TQfGZM4fYi8Gbwq2hVF_9tH5ex_Em-LZKW-85W7p-AV3vykkD1sR3uc2xvrrZfrfnj0VFUqgA27i-R0rSeXh3xnfDytce4BGtXFI6sYjMSEEPV-k0qsmF-uCTmNtwrMymcjXP49aW4w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9d0946d726.mp4?token=KLQyelrchksA6W1PfzJ-UJM2zuaNu59npEyjN9rdmTgn7FV6noRgUyhOwepxXI1d4Nw0ZgQAwj5-Hrhasvwvqg4-C5aGP8ViukZbxzV6CjV05VHO6VfYsWl2241GhrfIGIjcaaUtguqkssG1j_fbQ9DqWnY-JYRnvWNBJ1zrJLnz4oBHsKyt7Ct4aBcMovEtAozpDytbpV6TQfGZM4fYi8Gbwq2hVF_9tH5ex_Em-LZKW-85W7p-AV3vykkD1sR3uc2xvrrZfrfnj0VFUqgA27i-R0rSeXh3xnfDytce4BGtXFI6sYjMSEEPV-k0qsmF-uCTmNtwrMymcjXP49aW4w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🔴
انتقادات شدید و عجیب وحید قلیچ: چرا تارتار منو دستیار خودش نکرد؟
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/Futball180TV/102607" target="_blank">📅 12:45 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102606">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J7xA6185J5kcsmaKTy7Y0tGFhng-n0TcCsXycdTQwjR9lz6-KmGoqzMyDps1_4Xjf1zggn_ntgRR0Sl7SDTSQqFVQcj-eJGR6ejp2PDDaevg_9ClB3farzpzitbTnYZEPcnV3No6CbkBnJbFabsplJbkfptUBp97kqwWh8l3mQXTSInNvm8ezMamtWwO1P7SEagohxc5swznOZAnpsoOu1LWgYgtBqg1nRqmzamGd7ldPjSTgtBlOle6S-bDrQWumavLLSXkFTuhnKhiv-w0pYNIQMWMIIm6eb1U3xLkwsZDkOBfzNoXjMZqNjZVwy6GmUk5oePQoGHJWIgOSeISGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
⭕️
باشگاه‌استقلال اعلام کرد که فیفا در نامه‌ای تاکید کرده که یاسر‌آسانی فسخ قرارداد خود را در پرتال فیفا ثبت‌نکرده و این بازیکن مشکلی برای همراهی استقلال در فصل‌جدید ندارد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/Futball180TV/102606" target="_blank">📅 12:27 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102605">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/19edf655f0.mp4?token=kvimT8cYo51ULN2cFUQK8Fkji9I2tUqNtt9aBIoP9G-e_ao6x8cVZFlVSeD5udrCgJ8CMQ85xzi0Zv63SEtnD0QGKCLYZ0igsECPFHLRd17uEfdFmGB3eP0nysNk0HbTJwAaq4ByO2BR5Cd-xp6H0ukhdKL_lCQuuvrXOVIZHLwtz5Q-poiNeY0NKlcCH5O9cYeOynNGxCHVC4_dS6bGyZFSa6NjJZ5GGMsM26lKh6oOU_V1lHtjPa2JquMoMtkaLRIasOwCAKfwnWfkEstdT23nT79zJOcEKItiXcUIn3VgwWx0etc24Thr6X5pVU6kfXZnTb2bLTF99mXwnAjGvA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/19edf655f0.mp4?token=kvimT8cYo51ULN2cFUQK8Fkji9I2tUqNtt9aBIoP9G-e_ao6x8cVZFlVSeD5udrCgJ8CMQ85xzi0Zv63SEtnD0QGKCLYZ0igsECPFHLRd17uEfdFmGB3eP0nysNk0HbTJwAaq4ByO2BR5Cd-xp6H0ukhdKL_lCQuuvrXOVIZHLwtz5Q-poiNeY0NKlcCH5O9cYeOynNGxCHVC4_dS6bGyZFSa6NjJZ5GGMsM26lKh6oOU_V1lHtjPa2JquMoMtkaLRIasOwCAKfwnWfkEstdT23nT79zJOcEKItiXcUIn3VgwWx0etc24Thr6X5pVU6kfXZnTb2bLTF99mXwnAjGvA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
این عالیه از دستش ندید
😂
❤️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/Futball180TV/102605" target="_blank">📅 12:25 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102604">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/743e4b909e.mp4?token=RORP-5mYUTRfv-RO2QRrRP3zXM9PrdZzfD7AT7Z2ve3E2PryP79GmJ-fQDcBLXxFKsn_r-MDk-t3j4VZBIG6RQlDF5S4fjbUDQWSyzRGXvDxeJjQkR_fgX_I4wPt7UUZhFpHv_4rh2OvKlpimOTJcSPp1TJ0CXSEukgPSQOuDJybTyFMGg6Xz1dQWc-cyVSJME5FVT0x4GaJyOXOB2moudMmFcAwJ7jHvvgkC1dHyOsD8WeZ83V_dJJWqicZD9lGDKtXKqKH5_t1ngJ4J4WE7bqimrGh_g2MWsqzeW4hqUbsgqJPmgSsiXZc623c7SRgaiAYk2Dy3whS2Waao1bCUg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/743e4b909e.mp4?token=RORP-5mYUTRfv-RO2QRrRP3zXM9PrdZzfD7AT7Z2ve3E2PryP79GmJ-fQDcBLXxFKsn_r-MDk-t3j4VZBIG6RQlDF5S4fjbUDQWSyzRGXvDxeJjQkR_fgX_I4wPt7UUZhFpHv_4rh2OvKlpimOTJcSPp1TJ0CXSEukgPSQOuDJybTyFMGg6Xz1dQWc-cyVSJME5FVT0x4GaJyOXOB2moudMmFcAwJ7jHvvgkC1dHyOsD8WeZ83V_dJJWqicZD9lGDKtXKqKH5_t1ngJ4J4WE7bqimrGh_g2MWsqzeW4hqUbsgqJPmgSsiXZc623c7SRgaiAYk2Dy3whS2Waao1bCUg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
🇪🇸
مورینیو رئال امسال رو نجات خواهد داد؟
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/Futball180TV/102604" target="_blank">📅 12:02 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102603">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aCqJ4e3DUnDGH_TbmOACYPtB9cTUWFJ7_1daWwjglzfnC_6jSt43tzejKQEGcGWq2b02SBIckkSZy6vXCh9ZcF6sDS8sx5rKuSHjbQ2ppNCu_WVBvBbbqmE0c5_tNBYrD-KuDn27FAJJ33KIeJJD4KN95tSuJDBVxO_nwiQeNRfl8DEBLio1eN4Yw7XempouvagVcDgTKB1dETj9KM0VTaRGAm_eZMAGCY0V3OU-ozNUSqeMHfgS3YCz1YAAjqxFR9VqMIipERApTC0c5PwIP8igBgwrK6FxHaD5hl4A2-8S8KCwIEsYHeKIWXFlz-r0k11DnD4FRc_CDTx_-ud28A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">معجزه فوتبال:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/Futball180TV/102603" target="_blank">📅 11:39 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102600">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PUUlkqYc53x_DD1JmOEtAsxPIB008TQa7hbnaiz0ddSHZK2AxKrxysnIL0VZE95-KSSQeFuVO5uTEPsuY7cWCa9BGT2f2eefyD_dlta70y-beQvOWSRWaB9WAiZx_HhDjCoLgaHp2PUviI_o1pAhhTqWsd6-qvKlMPV3X05hGB7jOJ_NYWSG1adlAUAUuZ9nAXIFh3hHeIS_NevXKiwmvvd2XwitcFfz2aE20MeZhykfA2A02-S-Xo4qTyudSw8s8GkYR9w9vnVBHMseKRejmZE6hOj21Jl4q1JVa-dDRaskGjK2sis8zCuhKSH3DIdPdHjidGhbPBA0N3RPZ7GQbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BOOB8Vs-G8kdRzq0vm2vg78EqkNAth2qFry7_pwqo59Q6xVr-im30XVLBRa4rhAhQTGznM-UngRtiHyobEEboSICs7wydhfc1ZapMREe0vEWRs6xq62rO35lv-F_ePTYqbct2tc_Af8IyYIWG75nFa1LlOI9QoEoqpAcr4546HycV-RuXqiPKs5KXAwi35VM-XFBJa6LnyXTOyEZUN-0rTSr0s4QVWh5vInBxLjbGZIX7pFrvuzdhUsMGZu8sJ1J7nERUc8kWsz3walmRLki2B2L3iWfOqVtdZXU_aWH2_TonziQf8xw9Urh0oaLN8h7tX8z3Nq2odWx8BHdb5JOXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dCJE6aZX5Iv9JXkAizQ88JSfQFvQye2ZsnSeyzVMkvupQirDr8ArwB2WEA0glncPY5CBYKjFpIaB816MhzFU6JVResEHFxN-sW4cPxXHOik9NlBV8GQW-m-WkJi8VvEcqnbKSAj4aykW8UFBlsEELNQJgsEnI95csuhydOVcVQ0U58IMCwM7ARncnk52E3W26nDtWNhCt5mZjEI7J2l3FpAHvLng8wEZy_5GrkHrOAGARQZ2v3bIyLZmfEWD-rioYJJrXsqW3VUSapj50PVVwAyQYxwy8tD7XRfr-JQTnZ-B-1jhEQnXYl4VwxoYSK6Gi3O7YIJkfO5FQEhbHUNm3Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🚨
⚽️
کیت
‌سوم فصل‌آینده آرسنال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/Futball180TV/102600" target="_blank">📅 11:13 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102599">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uANTXyMonMMbZ9kY3j_ZnoPuQI2SNO8eR_R1J8zhaZ4xL69ugZ0G8WtJXhqPcQQjTSJXpLBjpGmw_4WD1PmS1yzfWVu21QI6T9ZrkiTBKACu6APxBddl3xVe9b-7KKdEYq86VlItQlDK2G_y2WjBLKZTM6Y1XWQsaUFD-K2KPgRbDYtcfnHoc4UxEMbnRg6FqlLEuZNftEyCrPsnwKKKqHTOtqGVAtgvujDRNPP9X4DVqoFRcvN11qxyuvQBoUyVtFTRYg1hkbNDVthLqeB6-wSIzJEMnbhZH1jX5XbgxnkHpHrVrln-OMfvVmYu8drcg3dZcvqttzQZls8Wr_x-Yw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
رونمایی منچسترسیتی از کیت سوم فصل‌آینده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/Futball180TV/102599" target="_blank">📅 11:13 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102598">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FEC5yyrW88uctGFtq9Bvixju-G-3ahDkXg7Q1bfOO9rSnsArMS_9pZRaGn9mHKN_vxWj35BXltKWz3DAu8gJM-orVsPb0bgLeenQv5AI1O21oFtZUpuPa_vfGOmottn0Yr7yHNfKeb1DK0gQXlub-NekGPCQy4ATF4FgsMtSBxqsQjSkRdCDN-Tw-QdX1Ht2-l-rvFsOMppmIgQxgchDfJVUa6EkNlNGFBni8c6kbKFGrBz2fxH0A3SYeIyppGQnJmOJi06jry0ODuz0AtZnDQz4gKdUfNAt_ATyIM6rbMmsT6BG9xxoW3l2DhFvJjyl2mrTNHxakqDOVsNSABn3Aw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
اسپورت:
لاپورتا از جذب گوردون و آدیمی کاملا راضیه و اگه آلوارزو جذب نکنن، عجله ای برای خرید نداره و ممکنه بازیکنی نخره!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/Futball180TV/102598" target="_blank">📅 11:11 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102597">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/17336a98ad.mp4?token=flacpTi0wjrLhvmOhBPdZc1bBuBKs3FJKKP-UXYkO1EbNRbZFizH0FY-aON-OgCPediCnD12uCWjjuo--J_9UQBidrxreDKXeqdnjuBQ1-ET-wMUWccTrDITGP_1MNProj-z8LrFSFLuGQBLYjeeLAKaTyCbefUgChv1i9ijbwkoq2gIJoyKUc-7c24cd7PTloHuwuDQTX8TZZsWah5cS_xb1jJe-LKdvV8P7Cgl0T0odKqtO2khptfQsqIzVwSIPyX26u01yP1xYRqhHmjE1v8_t5XMyXq9xmpscTQ26mvywSMRrEVZtPLK1P4Y_6TR5oNOpu16eT_bPQj5uiGZqw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/17336a98ad.mp4?token=flacpTi0wjrLhvmOhBPdZc1bBuBKs3FJKKP-UXYkO1EbNRbZFizH0FY-aON-OgCPediCnD12uCWjjuo--J_9UQBidrxreDKXeqdnjuBQ1-ET-wMUWccTrDITGP_1MNProj-z8LrFSFLuGQBLYjeeLAKaTyCbefUgChv1i9ijbwkoq2gIJoyKUc-7c24cd7PTloHuwuDQTX8TZZsWah5cS_xb1jJe-LKdvV8P7Cgl0T0odKqtO2khptfQsqIzVwSIPyX26u01yP1xYRqhHmjE1v8_t5XMyXq9xmpscTQ26mvywSMRrEVZtPLK1P4Y_6TR5oNOpu16eT_bPQj5uiGZqw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یکی از رالی‌های جذاب و تاریخی در مسابقات امسال لیگ‌ملت‌های والیبال ببینیم
😐
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/Futball180TV/102597" target="_blank">📅 10:31 · 12 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
