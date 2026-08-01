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
<img src="https://cdn4.telesco.pe/file/uHaQaZ6FegJ4UqJdkTCjuG93Fw4Y4pcxErLMJ6NeWfY8UJ-ad9ZyyDitgsnfLpyepw4ZnlslBdrWLlFvCyLy7AuCHo2oGPV6rxTHL6dOy4Jsxr2f82FNVxpMxvGwZTLX0s31Ie68ZRzYeoQguSCCkv891MFUBaQ_H854a71S4zjO4nr589hs_QPsXg_EIyp3gZiL3XBSbWQ-yh7fW3V3FRkrd6GfqVESksoL8_v-whFqgQWzMHlm5sMGA-g6PPdW2xQdtB_NjSge9ypsYcgCXOYbSl3ktuzj4aOQg3A0q88ksblakYm75H0DZZFXHqCz02ny0Wf5-PC8qkcvpKlFGA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 [ Fun HipHop ]</h1>
<p>@funhiphop • 👥 225K عضو</p>
<a href="https://t.me/funhiphop" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 «قدیمی ترین اجتماع فانِ هیپ هاپی»🟡صاحب سبک🟡Tb :@FunHipHopAdsContact :@Chaman_Dar_KhakFollowing Copyright Laws©</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-10 19:05:43</div>
<hr>

<div class="tg-post" id="msg-81631">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gjbc1r7n4hw_wVCEr-ebN5J0VnOIhdf3brjgRs18AGERD9vl-APt9s9GYCDns4Hbctlp4r5i8pB2Vp6-ktQvXq1BorD6B47vEv_A7wZCEOCrLjLejWAnMOnlgRymBflzuBSfeDpOo6KL3Uopk-1TfZaLBYlzlHvUOwnIMdBlYgpSe3aE7l2VA_FGXvQwwGDR1lncqjnaLXS8eljIJCZqq0RzBon4xweXsUU6o4KpHHk_63nzd8mcfKwbcySK626Tf4aXC8eYT2Z9ozWN2z-9EKPlROaYnxmNbdkmYvXMRTvy7Kz6QD1czosRB3zjWkW12OOnhEyeQ3hTX_WpPK3yWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این مرده که توی سریال کلید اسرار که قبلا از شبکه سه پخش میشد میومد پند میداد و همه میگفتن چه انسان شریفیه رو یادتونه؟ الان رفته پورن استار شده و بعدشم عضو یه گروه تروریستی به اسم FETO شده و تحت تعقیب پلیس ترکیه هم هست و برای بازداشتش ۵۰۰ هزار دلار جایزه گذاشتن‌.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 1.47K · <a href="https://t.me/funhiphop/81631" target="_blank">📅 19:00 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81630">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">رسانه های نزدیک به سپاه: اگه زیرساخت های ما رو بزنن؛ کابل های فیبر نوری در تنگه هرمز رو قطع میکنیم تا اینترنت کل جهان قطع شه.
پ‌ن: مشکلشون با اینترنت فقط داخلی نیست انگار، جهانیه.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 5.49K · <a href="https://t.me/funhiphop/81630" target="_blank">📅 17:59 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81628">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jzH7mWXGopTIACOBGmb4qU5jr23xVh_AZ6NbdTAjYaJy3UT-TPYsfwKPSWs7RcPIkeyBacCODssdPqtOLp9076r7DUUUjQnZQeQWo8qXaPyo3ct4r9-kZu_Xpgu1yUsHumBw490V0KmqA0fHOXtpL_IodNbUOV5_eotrbYMwH_UQg7m7P88npgLUtvyK1FE7jeC3M8ZyK12bcNOacw7c-A_KGsi4RPGdykbLV33l8d3OomF3JnCGtmhPBgZvX9xObkuyFAIhdmV8P-Hy6vgZUtRk-iIZ5kdRpHy3XKXwSZo8SRSKR6NTUDAxzzc-LzbOw1goCK_LdHChxaABfBeJlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f0bf99c7d1.mp4?token=n-V4tKjShRWT8XoiaRDIZQEkNwTCKc7xB98Rda4E1of4KIV4DdE_5p_263RRiMVRIOPptH-9HIhsaz4HrIFsITXMklwze3lCDkhO4tEbSmW1MusQ9zwIjxOHNB1gXwHUHwRxwx6EsDc3eImTSVzJKZFq2pV1X1iTjuEjylKwj21-e7LR8hmpHJXnBrKcWI-PBn7kQ8BbyCzU_exQGjl9O08eIAr7CJqVmQNAvcy4wEYgq-yNAQ7pDbwX9uNeJEmUbBhMn0Wv-NQeUpLTvncqwycYHYXeyqRj9h78PL0Y0x-7smHUhdSfpXVCaqBWCovM8fCXETrfy1R8A_f5pXQC2w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f0bf99c7d1.mp4?token=n-V4tKjShRWT8XoiaRDIZQEkNwTCKc7xB98Rda4E1of4KIV4DdE_5p_263RRiMVRIOPptH-9HIhsaz4HrIFsITXMklwze3lCDkhO4tEbSmW1MusQ9zwIjxOHNB1gXwHUHwRxwx6EsDc3eImTSVzJKZFq2pV1X1iTjuEjylKwj21-e7LR8hmpHJXnBrKcWI-PBn7kQ8BbyCzU_exQGjl9O08eIAr7CJqVmQNAvcy4wEYgq-yNAQ7pDbwX9uNeJEmUbBhMn0Wv-NQeUpLTvncqwycYHYXeyqRj9h78PL0Y0x-7smHUhdSfpXVCaqBWCovM8fCXETrfy1R8A_f5pXQC2w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیو جدید سیدنی سوئینی برای برند لباس زیر خودش
.
پ‌ن: برا آخرین بار ببینید که نت قطع شه دیگه تا چندماه خبری ازش نیست.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 7.1K · <a href="https://t.me/funhiphop/81628" target="_blank">📅 17:48 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81627">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fanzkOde3zOTJF4X04M3g64p6ldwHSMlNN6QRSblWGmd0EuH8BJR9eluTfqbl_eGNTTOh1Ow0Co9iyIc_injfF3OQJalgvPLHnx2qzDXPWCrK8Ng2t4pD_zueVrCd_uXjoBy1iPivjvdE50boXgg0ZXLulyX0U0M-Ct_jqb6NXMZdG5NSy-v7k5Q_VK4Cv8uTJZ656qkiyYb30RYlnuF9DSh9oT4qPGa0QJOk4117WsNJI-3JLsVlo7PwpNoBjqs-iMBindRnusrJYMW6RCuNjZhmzmd90EEfx8cm-zxPTxVMjJcLwnY_Kb5x_HVNfQIddQWO_T4DXNutHJct2DCUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎮
آموزش حرفه‌ای بازی‌های کازینویی در یوتیوب بت‌فوروارد
🎲
⏩
اگر به یادگیری بازی‌های کازینویی علاقه‌مند هستید، آموزش‌های اختصاصی و حرفه‌ای بت‌فوروارد را از دست ندهید. در کانال رسمی یوتیوب بت‌فوروارد، نحوه انجام بازی‌های محبوبی مانند انفجار، پوکر تگزاس هولدم، سیک‌بو، دراگون تایگر، پاسور و چندین بازی جذاب دیگر را به‌صورت ساده و کاربردی یاد می‌گیرید.
👍
در این آموزش‌ها با قوانین، روند بازی، نکات مهم و روش‌های مدیریت سرمایه بهتر بازی آشنا خواهید شد تا با شناخت بیشتری وارد هر رقابت شوید.
📲
همین حالا به یوتیوب بت‌فوروارد سر بزنید و آموزش بازی موردعلاقه‌تان را تماشا کنید.
👍
ورود به یوتیوب بت‌فوروارد
کلیک کنید
BetForward_Official
کلیک کنید
BetForward_Official
🅰
g10
💻
@BetForward</div>
<div class="tg-footer">👁️ 6.51K · <a href="https://t.me/funhiphop/81627" target="_blank">📅 17:48 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81626">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">انتقال لجستیکی آمریکا به خاورمیانه تقریبا تکمیل شده، الان دیگه همچیز به ترامپ بستگی داره که دستور حمله رو بده یا نه.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 6.73K · <a href="https://t.me/funhiphop/81626" target="_blank">📅 17:42 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81625">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Drumiq-NW0PMBq0eqmzcDLRV1AvfRo_LDid24RL0psQTqi28E1bLVkNjfBSSnHJ8CD15g-VaA1nPt-fcpj3MtvcS-_bn3nwWPVrm20dmQOxPWVVkwpndoHQcrs2u6CI54_CgLKGhUZnMC_09fVXmcI0FnhVLVIshH15rh6qSTPedg1A8tNR7iHUxRwxuuHjtMsMpTG4qF3etxIB2JrxaiHfDE_ZpmeV8ebSywcmGo--fh-szWxz1KU9guqXfQP1c1ZQjGVBas9u3Kqndr4YTMlvW7TZeQDHATiGXzW9K9Lao2TbYCHmKSQmUAn7SOskAw-Ee3CnOcHn6nXLn-m3WIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تصویری از تانک‌های T-72 لشکر زرهی ۹۲ ارتش جمهوری اسلامی در حال حرکت به سمت آبادان و مرز خوزستان با عراق
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 8.14K · <a href="https://t.me/funhiphop/81625" target="_blank">📅 17:25 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81624">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">امروز صبح آروین خیرخواه یک زندانی دیگر اعدام شد
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 8.62K · <a href="https://t.me/funhiphop/81624" target="_blank">📅 17:14 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81623">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">اول جنگ ارتش یه سوخو 24 فرستاد العدید قطر رو بزنه که منهدمش کردن و تازگیا جسد یکی از خلبانا پیدا شد و برگردوندن کشور.
ارتش گفته این ماموریت 4 نفره بوده و همچنان اون 3 خلبان دیگه مفقودن و دنبالشونیم
منبعشم نمیدونم کپی پیست کردم
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 9.46K · <a href="https://t.me/funhiphop/81623" target="_blank">📅 17:00 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81622">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bR7ee0QGrtfiqfqOEhdqaIrJ0Gh3oDAbeeUHPaPBX1RZBNk1d22SPmXgyQdm24XH7WQunWy00sL4VVCXe_Jojm5ti7ksvp929PC4RRIUVDg6M6X-ueFG5dQmyzKvGHc6KtSL49-AyLaoJMxQoKcaLrEojjH8mA51FgTEyuhJnotFXd3bZ0GcZewu-NdG0FEZgEJPz7xYqp5K0-8jZ3wooxzQt53Iv7pvvKxUwhNFLzh9grkaNWQ6QfDA8zZffiXkobP1xN0PdoqKFdfEvK1FUAz_UYJs3uCDi5CgS_xgX-LbwvZfnymyku5UFWejF5YmvwQI1TFDQICXHskzCwWVqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بابا کمتر پورن نگاه کنید، مغزتون گاییده شده
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/funhiphop/81622" target="_blank">📅 16:41 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81621">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">سی‌بی‌اس :
ایالات متحده در حال برنامه‌ریزی برای قطع کامل برق در سراسر تهران است
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/funhiphop/81621" target="_blank">📅 16:32 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81620">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bfo9DboGhFeE8P_TfRyOP7u1V29xwlRW_LpbDFn47ztlpdo8D5pCmhrwgtPIdaGl0JahWbzxmbPAjrRCSJPzNm7N4pAXIznBrvonkedVIjSnTVwenTdUlK9PA7pE4lmyB8qpT5il3JplkkCO7eKQj70uh8LArQ60fvOB9WHajNU060J0Ji5vSJKS6N5dDH_ZaJnKXW7HvabsMI9BmBFYVkLthKvCB04DaB6fFZRn3wOfU59GwvAF5fZ1kwW6yK6nzbIy_1MjG8O-hGFM0MUNBQd6G7H31KRDRlBkMUPuzb0I1BSKzASTybRuhftrkblTFf43jfWpeCaIWqxlI8pfvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">داش چارتا چیز که ندیدیم پیشنهاد بده
اینو بابابزرگ خدابیامرز منم تمومش کرده</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/funhiphop/81620" target="_blank">📅 16:23 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81619">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RHH8RPavMNqVdcuc-dg0BCv8XwSLcalNoJFewXZT4O9tA0JOFD2BWKbyoFLJ_pqIlUZw_-WPooCOeaRwcpVfpnrHvBHYMlRx68AvzRBGHHdDhmN7X3inrDcQM-_Ea6uxJiKoku-_emapOiBzs7BD_m3JQ50ekokh2S9w0S9Yp58yNvfR7Ea4ATTdctTMIuQ9PhdSWnlXbmPKm2aY2qufpKVFf3N-enSWusy4Jn8nYT0iSyDQjx2dAeooOmeAXn3kcUkOA_Vva4BBvapByTBBqWcxq8MGGz5wYU8SGP5oMONdugWOmedKrQltLN15XUpRcdO-iXszDCZr5c-s1cU2yg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آب دستتونه بزارید زمین برید این سریالو ببینید.  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/funhiphop/81619" target="_blank">📅 16:18 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81618">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iJ4FleRgfsyQqS8l7r5_A4aruR6c8IrBAx1RK-ro90Uc_SbPriyavH2BXTePTN6LencOlkDRDXRyIey9TSL97dLJ8iDkEiQkTtiSO2XxXVZJuO5RNWGj68cIrwmRTZJD59rD2MJxiWUHUGAumaKaU5UtcpIfCWSMdWiuj8EiBzYYbVJv3-LDkwbvBYT3dnMptzDmOk9gtowRejCF7BnhvAxNGBNaPZg0_hS9bmGwXqi-GUSxAaiWKNoNIbvF0YQoQlx7R7ALgortt78tssFOHfu8GyATOGUdV-qZkfKIcY6n4HqVs3QmOdRnTJwLgb7yuT_6b1MT9N7gRREICUXEew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نگار جواهریان جدی معتاد شد فک کنم
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/funhiphop/81618" target="_blank">📅 15:43 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81617">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/07811532ee.mp4?token=aQPlplFxOaupdpbG0qLeePUhrfxx-fhNeN5CDr7TAebZ46YjLRaWJ56lojH8xQoWut4xOHnOZzuUfJcJEw8aQrzGh6wIcTrnon1YdcyDA_DjjKkf4UhWiyarffo_tO8EyMCG85CKWq--tXtvsS2uwUZGEA151wQ57sxE5LX5hJ3iD1mH4ITUOrm1ckb8Lqe0B5MJZTj-juWBEsGXJPqbv1qN5lOxJrrGB9qc6g3EVk-s3S7G-M42hM-vkVeAp2DIU0hKp2BDRRhm7c-Zt3FxMUh2JkOSQG3eZnbxYoj1mcXp_MB0DCNeMTka4ESKUxVkR2TUS48ITR1UpS8RvzxOWg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/07811532ee.mp4?token=aQPlplFxOaupdpbG0qLeePUhrfxx-fhNeN5CDr7TAebZ46YjLRaWJ56lojH8xQoWut4xOHnOZzuUfJcJEw8aQrzGh6wIcTrnon1YdcyDA_DjjKkf4UhWiyarffo_tO8EyMCG85CKWq--tXtvsS2uwUZGEA151wQ57sxE5LX5hJ3iD1mH4ITUOrm1ckb8Lqe0B5MJZTj-juWBEsGXJPqbv1qN5lOxJrrGB9qc6g3EVk-s3S7G-M42hM-vkVeAp2DIU0hKp2BDRRhm7c-Zt3FxMUh2JkOSQG3eZnbxYoj1mcXp_MB0DCNeMTka4ESKUxVkR2TUS48ITR1UpS8RvzxOWg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اسپید به مناسبت ۶۰ میلیونی‌شدن یوتوبش داشت با بادکنک پرواز می‌کرد تا انیمیشن محبوبش یعنی Up 2009 رو بازسازی کنه ولی یهو بادکنکا ترکیدن و با کون سقوط کرد
.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/funhiphop/81617" target="_blank">📅 14:27 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81616">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">غرب کرمانشاه یجارو زدن انگار صدای انفجار شنیده شده  @FunHipHop | چمن در خاک</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/funhiphop/81616" target="_blank">📅 14:18 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81615">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">غرب کرمانشاه یجارو زدن انگار صدای انفجار شنیده شده
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/funhiphop/81615" target="_blank">📅 13:51 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81614">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e859712cf3.mp4?token=oPru8FfpUloefN5NinRrSvypeulBtxjJFWGfplZSTxFb_6N9T8MB3p2vQJnFONeuq4oRciXUj9M00B94edyDM9OJc46rOw1Rr95ZfPwjlMT5KhXcVhTXEkh1pDCfrRwlw6CCwPBo8-k3xjUTLcGHPrtI0RzdNltzJvqwDYke6i2q_wA3rh2CX0r_fkwm_0J5t1U6vMk9Dvvw7gW50F_LvfVpiI8TjeNsbzsV5KH_ofpqQSj-VW-W4oWRrfSDvbYvu4LHvj0WkEIIzsask_i3ateHvANqk_avgR41YmfvgCabxfk5CzGJiKwBbhJF8Th7k08NeZZg6rK6Wt-a78IUtw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e859712cf3.mp4?token=oPru8FfpUloefN5NinRrSvypeulBtxjJFWGfplZSTxFb_6N9T8MB3p2vQJnFONeuq4oRciXUj9M00B94edyDM9OJc46rOw1Rr95ZfPwjlMT5KhXcVhTXEkh1pDCfrRwlw6CCwPBo8-k3xjUTLcGHPrtI0RzdNltzJvqwDYke6i2q_wA3rh2CX0r_fkwm_0J5t1U6vMk9Dvvw7gW50F_LvfVpiI8TjeNsbzsV5KH_ofpqQSj-VW-W4oWRrfSDvbYvu4LHvj0WkEIIzsask_i3ateHvANqk_avgR41YmfvgCabxfk5CzGJiKwBbhJF8Th7k08NeZZg6rK6Wt-a78IUtw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چرا همه با ورس شاهین نجفی دابسمش میرن، پس عرفان بدبخت چی
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/funhiphop/81614" target="_blank">📅 13:47 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81613">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gnY_If6rQoYGnlUOkStwjAh4pwtO6W2zBAKiY-cVl75M8QzfuPQlCha5L0_9UU67_OQ_R5VKhFeGBOT352_Z5MPfk2ppba_12A5tzIfbazENgX-kXK-VkvLoxdDCgai5YTTc5B_R7yxgyndcotS6TzPwhj55mM62O9u43fs3-8XVqUXZ7a_abOgbj3TQ3JlArmq-Wri03cvF38OwMqHDCv3RgrroZa_sH-aPw1vgBF8venDIB9V8lwq0ZnfLECQK4yK-h-90SwP0bV_bmoWLKC5Uwtg001tuGJltsI0_xRQNsoJgzOJl_q-h1NmQHXNdeTfwitjWTVfLieSDjNLvWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎮
آموزش حرفه‌ای بازی‌های کازینویی در یوتیوب بت‌فوروارد
🎲
⏩
اگر به یادگیری بازی‌های کازینویی علاقه‌مند هستید، آموزش‌های اختصاصی و حرفه‌ای بت‌فوروارد را از دست ندهید. در کانال رسمی یوتیوب بت‌فوروارد، نحوه انجام بازی‌های محبوبی مانند انفجار، پوکر تگزاس هولدم، سیک‌بو، دراگون تایگر، پاسور و چندین بازی جذاب دیگر را به‌صورت ساده و کاربردی یاد می‌گیرید.
👍
در این آموزش‌ها با قوانین، روند بازی، نکات مهم و روش‌های مدیریت سرمایه بهتر بازی آشنا خواهید شد تا با شناخت بیشتری وارد هر رقابت شوید.
📲
همین حالا به یوتیوب بت‌فوروارد سر بزنید و آموزش بازی موردعلاقه‌تان را تماشا کنید.
👍
ورود به یوتیوب بت‌فوروارد
کلیک کنید
BetForward_Official
کلیک کنید
BetForward_Official
🅰
r10
💻
@BetForward</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/funhiphop/81613" target="_blank">📅 13:47 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81612">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">پدرو سانچز، نخست وزیر اسپانیا رسما به گوه خوردن افتاده و خواستار یک جلسه اضطراری با کشور های اتحادیه اروپا در خصوص بحران به وجود اومده توسط مسلمون های غیر قانونی شده
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/funhiphop/81612" target="_blank">📅 12:00 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81611">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VRtMW0RTg7t6M0TlB1xYT1Rp9WZ7779xbaww18GBuO1rm_89LUl8uUIsI6pQ3H2GFDiw2nclJt21ntLlHUmVo7Z8hNR0uSJ6dZFZeVmKVFrgSWwKXzEYFKYWpIzvg-zEuJpOziqICV7tXiSTL6oC8lybx70bel8vtrXbom5en5p0kW5Fpnk1EkG5fpRemZP-IC9WuNPlzT2eVUUBfhSn245mbooshkouOU2UdeWzbjWhoSafk0o0SxA7XQV9u40LTfoduOfuCyQynQN5hzR_lrwJkpgFE0gaqdMyTgfDhLSbkxuionRgjtKnk6nV3HHkPBBNGUqda2VyR-xSYek81Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تورو خدا به این بی ظرفیت چیزی نگید از این به بعد
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/funhiphop/81611" target="_blank">📅 11:52 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81610">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">امتحاناتون بالاخره تموم شد، چطور بود؟
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/funhiphop/81610" target="_blank">📅 11:35 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81609">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">مثکه به دیتاسنترا اماده باش دادن وقتی جنگ شروع شد سریع نتو ببندن
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/funhiphop/81609" target="_blank">📅 01:54 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81608">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">راستی وارد شنبه که شدیم بازار های جهانی هم بسته شد
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/funhiphop/81608" target="_blank">📅 01:50 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81607">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4ac286f3dd.mp4?token=kdCj19u4DD79ECu_Iemr-IUgJHvodh9vD28YmU97eFeeyFNqUIXwnxifjy4RGS11S-K8xQQVGFtRgN5mneTEF5kG9yEDks3RqlIKOaO5H-bOZ9CyMTKL0nnobZ96pTN4QW17LuEot-Vtb0KFg2UXLJDLijb14T-JVI4ZmN-v1Fc2TvMd9sn_qsj06R8rL3U_4jrTRmDRZ9X2s2doSCdQ15e7CwbHu6FZ4AoUpDAM1W2sjL6Kx-FL6W8vKDdrNOukAZGYK8bDko68AVnf5ek2d2MTf3keqAdZMgGXo7cuISQnFd3l7pyI24ZAvId27DZqmZJMcKrmLDQVqiylgb_MkQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4ac286f3dd.mp4?token=kdCj19u4DD79ECu_Iemr-IUgJHvodh9vD28YmU97eFeeyFNqUIXwnxifjy4RGS11S-K8xQQVGFtRgN5mneTEF5kG9yEDks3RqlIKOaO5H-bOZ9CyMTKL0nnobZ96pTN4QW17LuEot-Vtb0KFg2UXLJDLijb14T-JVI4ZmN-v1Fc2TvMd9sn_qsj06R8rL3U_4jrTRmDRZ9X2s2doSCdQ15e7CwbHu6FZ4AoUpDAM1W2sjL6Kx-FL6W8vKDdrNOukAZGYK8bDko68AVnf5ek2d2MTf3keqAdZMgGXo7cuISQnFd3l7pyI24ZAvId27DZqmZJMcKrmLDQVqiylgb_MkQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جنگنده های اسرائیلی و امریکایی دارن کسچرخ میزنن
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/funhiphop/81607" target="_blank">📅 01:46 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81606">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oMHv5krfdYIpVoGFrF3bOWOMgcWLtJJl6Dqxxl9rPope6XvGVF_W2To2tpKMRhSXNE2xFKHPdkm35z6xnbOD-iwib2AH4sVSTFGTOUxHx87w5_AKasdjQP48qAjjOOZFkzgFCl5cZ9pVZdT7QOjGaeRFL9sSJG3ASS1yTukBTx3Y9-2RxBaZaq0K_-DH6aOn0VhTXCVCCi5ymckyrWU3xnovyPBGbjATtIPGDdRnlwFcmibtcW5MWgwNdnwkuqiu2ioABzq1dFRSkaW7fgRQDlvq8GhV6QERpHcS572TU1TM3oMnAh4KwLw_ehtVitEBooR28GP6ZTTAXJ8bQ6KoHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شیما کاتوزیان جزو ۱۰۰ فرد تأثیرگذار دنیا در فهرست TIME100 سال ۲۰۲۶ قرار گرفت.
@FunHipHop
| artin</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/funhiphop/81606" target="_blank">📅 00:41 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81605">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromɪᴍᴀɴ</strong></div>
<div class="tg-text">گویا دلار تا ۲۰۰ قراره بره بالا
سال دیگه که قراره بره بالای ۲۶۰ اصلا
همین امسال فرار کنیم</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/funhiphop/81605" target="_blank">📅 00:05 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81604">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LaqIf7Dyj30arAerAvyGs6m5Z_CTccr-UPYJEaRw9_GuaMi4hnnIIOjqLZtyqjdKeTtSOmFr8jrGwaIOonaIAGdpbWDWTW_qKr0pCNQ26Y8zQHv1fVNTS1IALmOgoETDb78ZCOOZm3_wqPbW_KubWw1Amng0y1n5tBnwa8TyQjIrH7oWxbgnsQCh6laY_eoIvfrSn9rg9PvznJIUZvyqityT5QaUjZ8eJTMmArLudXCcWmPV3NFYJBw3AWhag99PfxLjMZRgnMF1KcxD6yJWxym8Ao-IU50EWAiDb77y8WCsB2xYDj3GXEBNn3gvUlhINeUnJvtzZl-6m-XMyGRQsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/funhiphop/81604" target="_blank">📅 00:02 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81603">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/83c227c270.mp4?token=TlzAxa7-hRI6Q6Xfy9kgu3uwdU63BCIvovuLBp_emNBWqpJMZwt-FfYZvbgvxmgVmwJyfQ8CtMV-9EeeYXTQ1aMwuUEvWLNgUwiuLDqoCDmCmcLK5T0iC7T6bw0zFfQKUJnTHSy6dUPJjINMbuAKA2-XYnzwK_X0x8lhYB0y4vBPS9RlixQCeaV5PV_QJszy9ZTUp07SasqJyFQdXZStde6OcXx7B21UC9Gx-W9cZNtr1YCVE09D-hAaYpLe_PTEdOBuCNXggq-XfWVHeAgrzaPPle5_0NhO-i0U5RoIIS9HP7g59MKwONnadrh5y6db3EIiYbQBgdwnqWAVnaleqQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/83c227c270.mp4?token=TlzAxa7-hRI6Q6Xfy9kgu3uwdU63BCIvovuLBp_emNBWqpJMZwt-FfYZvbgvxmgVmwJyfQ8CtMV-9EeeYXTQ1aMwuUEvWLNgUwiuLDqoCDmCmcLK5T0iC7T6bw0zFfQKUJnTHSy6dUPJjINMbuAKA2-XYnzwK_X0x8lhYB0y4vBPS9RlixQCeaV5PV_QJszy9ZTUp07SasqJyFQdXZStde6OcXx7B21UC9Gx-W9cZNtr1YCVE09D-hAaYpLe_PTEdOBuCNXggq-XfWVHeAgrzaPPle5_0NhO-i0U5RoIIS9HP7g59MKwONnadrh5y6db3EIiYbQBgdwnqWAVnaleqQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترام:
من قبل از شروع جنگ ایران یه نقشه و ایده میلیون دلاری داشتم که خب ما میریم توانایی نظامی و هسته‌ای‌شون رو نابود می‌کنیم بعد سریع خارج میشیم همون‌جوری که به شما گفته بودم؛
ولی اون وسطای جنگ چیزهایی در من جرقه زد که خب عقب مونده، تو هر چی خراب کنی اونا دوباره می‌تونن بسازن که، برا همین الان دارم یه ایده میلیارد دلاری رو می‌برم جلو که بتونم کنترل و نظارت هم داشته باشم رو همه چی، خواهیم دید چه خواهد شد.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/funhiphop/81603" target="_blank">📅 23:57 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81602">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">نیویورک پست:
برد کوپر، فرمانده سنتکام طرحی رو برای یک عملیات بمباران گسترده و طولانی‌مدت (به مدت دو هفته) علیه ایران تدوین کرده که این حملات به صورت نامحدود هستن.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/funhiphop/81602" target="_blank">📅 23:42 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81598">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gYDeG2BzxZhVwn1CUMv0CoxF6G8CISXngKoBSBts0u-OPpljzai0svxUMstADkzQJoa4vApcJTqINyHWAqm4kSRR7NJII7dEEP6zLJlqAdK3b3W8FZZOS5d7YprIEJqcf0dC5exOji2p8YUuv0yRAAb5xtKIAclxxUcVhBQ0Pkm4Si_A5DBQDdmnCJVK3zNKxZEM7A1D8yBgdoDgphFC01z1wSkbJA4brITbhEQ8_nfTOl9IcickVPk92YknP3so7vfTGfASjSC6iLUHygdo9w4K9BBwAMPy8A_r1IPBA_vDw0Fr-pkypZ2aiRE_fhHNcccroX5Wz4oUyA7_CgZkbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jqLIBSXWqPFZfEpAMHwclqhDCU4OElymf2dKZb5fn9T1015CmqWOl5M8pnYdXvuDWHZu7jKUdoeJlGmfgqWCuSZmDzMK2km-OtfZIguQDOk_IWiM7ihpZZoe4-mh1FVl9WRJROBPEmwQUjmYtIZTo807yqADt0TU90rL47a1UyUCEveKi68FMnvRD6bedEjGnVWBv4eZiPtqT1nxEZIuoeGyWWYEWgAF2H25BQCleIW8HiYlA3jYw89xeN73srGjXrp3AgPu3_cyftkNRNB8EA7t1KpBWkFJ761a7qtJZK7DoYTYMFm1LWeSsa9vO_-oPREwvLkQPs9cLmjEzzBfAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fJbQHDCyBkHQA0zhWijrzP4B9eb63uns86j2QwRZP-OyqvsHejaUTuFfGIxW8WjQiJWlxoe6e0FuYb1rqLW2YDmz1OLaUXDfTbJx1pttEv1SXvPB6iEHvNPBsU0XHVTusM-TSKT01mZA1aCqb5Zky2_ws0DGn8XaVWH7OHW3EC84kCONGg8f4RMAUCxMbFkzW8xSg9pQQ7sNRAARMmwoZpPa41PMNbffUVsD59jlWIiasmfkDsCQ78bW7xOLrfTfoH0MqpHvNDf-ckVyDEX8zRvnTcI04VqJ_WxzoB9VxmFXOW8ln7DMg-E1sXZ9dM371n5N-9o_lO-NN_moubkf9g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/10712ee047.mp4?token=lXvRSvjJWFHGqfmW3T1oG0aiW39MBFs5UWYlWzK8pvQqr7RHCa3cjMLJbtcewiTLDkYIkESG7ancF-phPWdvrJ_J7pS5c-anqNthtt-BWiVd5X_PBsfzftMf1LXbx1M2SetEfaQ_yEV00pCkGGk50oqNqIpBvwopSj6j0KxkFRcwsTSWBd74Wsg9IK08z13wWDzNp-dTLsYmuT6bOiYjzSJ4JbehWjvwxurl0wXLwT2laR1odDZ1Qb_WBljNAaB68oOCATk2vCN3uyvMHhYmQc2KwWmHFOSHjH92FKmZmzduNUg3tR-tTTSl9WN2lH069TrnpNgv5y7nYSSkIoXL5Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/10712ee047.mp4?token=lXvRSvjJWFHGqfmW3T1oG0aiW39MBFs5UWYlWzK8pvQqr7RHCa3cjMLJbtcewiTLDkYIkESG7ancF-phPWdvrJ_J7pS5c-anqNthtt-BWiVd5X_PBsfzftMf1LXbx1M2SetEfaQ_yEV00pCkGGk50oqNqIpBvwopSj6j0KxkFRcwsTSWBd74Wsg9IK08z13wWDzNp-dTLsYmuT6bOiYjzSJ4JbehWjvwxurl0wXLwT2laR1odDZ1Qb_WBljNAaB68oOCATk2vCN3uyvMHhYmQc2KwWmHFOSHjH92FKmZmzduNUg3tR-tTTSl9WN2lH069TrnpNgv5y7nYSSkIoXL5Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پیشرو و آرتا دارن موزیک میبندن.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/funhiphop/81598" target="_blank">📅 23:25 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81597">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">🔞
فیلم های بیتربیتی با  زیرنویس فارسی
🇮🇷
تاحالا دیدی؟ با ربات زیر میتونی کلی فیلم آموزشی با زیرنویس فارسی دانلود کنی
💀
⚫️
@EzzyPhBot
⚫️
@EzzyPhBot
تازه میتونی از
💎
Porn هم هرچی خواستی دانلود کنی ببینی و برای دوستات بفرستی :)))</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/funhiphop/81597" target="_blank">📅 23:00 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81596">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rDo3UZij0scf1HImCEKsLwImV-AkiS5Ec2UWWD3EIlRPdzZM3-ncqsXRuNejtO5Q8kCDI4bLNX9pKb5XQgpKy45lB-_ni-67fVBXrgfb0xV3JDEV-jdwkp-zWQfOSlb1AL0Y6xgxyHwWFpAfSpZdL90Tx5rzhsWoBAMEpdlk9eaduRMuKL5YCaryyeN8Sg97PY-Tzt5UEmbf5_UmnUBm0Nct40hSlKnsLQTTz97M_5Xnfr3JXFiXK2ag5TlNSWUneYq2Yb87hJfTT-bd_SYaJuuVimSq5g2AmMqOKjyt-ym3DPid7JIriR_fEb2yxdii4b-uEB5KfdOHX7uwC5D--w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">@FuunHipHop | Jenayi</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/funhiphop/81596" target="_blank">📅 22:38 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81595">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j_tlIsRGZa8v_xcqeydZ8ThmXgPDW-t7ROB7goWNsoHBNFjbvZaUeIGBFFi_eZ8pBe5jvyCREsQgx1cfFjnp-q2prKZA9mskKyg1n65KRv_LliJxqYTw08hmgkHh1xs6m9YB3jEbOIZWWCVfjh47ifjgdi5IMC7q5Za13mSzwhYO6zpvKaKuchagrV5YFrmQDmU55FVrA5hXVR0thmj1IOx_UPK495TPsuC0jGNJ-MMvxZVR1l1ygK7j_ZgL24JkVeCujkev_IznCOdAb1EeO4cVCjr5INO9-5KFNAGoAqRATU7udF10_w00sfpmKFNCq9WCF5BqBd2hw5aOBwex9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برای عمو هایی که میگفتن ما عزت و احتراممون رو با برنج و ذرت عوض نمیکنیم او عه او رو بخونید
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/funhiphop/81595" target="_blank">📅 22:30 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81594">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TrJ6QlXFpbXvGHEJ4IaDOsPbsPdTytcfA81VVCqivhOekrpFeora7MXW2xbl2SCPf2SJIwQ9GBvm-CaLVREfrzwcNFq_6JgerQxB_1gZia-LhJ-jTYfpJ9IoJrkL9ji5y2OWt-dXaIwlTbTPGjzTiL6EDnSta4TnGqedgq1Vod5eUcCkGcZy8jo9_b7zcwjVQV8X2wu9VJlxUMtkLmd8T-lrHDdGLzv4QNh_Tlk1TzCNCUuuhw2pKp_j9Kv_59KWaFWBhiINnu8nMm3pX0mwU6B4ILWj1BzMJOGHW1FLp2Pb6d1ZgNwXNoWfrX0dNbUuBq6MI2LsRlVtXqQ34sjGkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وول استریت جرنال:
ترامپ از دیپلماسی ناراضی است و وعده داده که ایران را با قدرت مورد حمله قرار خواهد داد.
ترامپ روز جمعه گفت که قصد دارد حملات نظامی سنگین علیه ایران را از سر بگیرد تا رژیم را مجبور به آمدن به پای میز مذاکره کند و قول داد که به این کشور «بسیار سخت» ضربه بزند و پیش‌بینی کرد که رژیم تندرو در نهایت «از صحنه خارج خواهد شد».
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/funhiphop/81594" target="_blank">📅 22:06 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81593">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">#شرمنده_بابت_پست_رپی ترک جدید سوگند و سجیل به نام وقتی رفت ریلیز شد.
🎵
SoandClaud
🎵
Spatifay  @FuunHipHop | Nima</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/funhiphop/81593" target="_blank">📅 21:05 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81592">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q2I9Y9PomhAVnMgc3nI5eJnddaTU6gizVanxzBufNtNOAe6_9lDQuncloUxkI7NSOwVmTIch_y2XHlh-BzZcfOnWXY7iZ-xFgtZWyfMLPslUqRVzdL5RYq_n2Ff8OGTu9ZEEMPq2XK_Ai5sW96INa6QJwKe-u1LA9YGb1wF0ONNms4DcpCyTANVkRKW3R2BCLzYsPQqKADesIksrO2-EcW3ndY_P0adSxD2SWXYP_TBP130m1cIOFSfVfcFc-LR6sAn_QfjNZasrQ7J1CLYEN6awY1oXMffeMTnmuvkjpVYHU16fwN1kfuyKIxOlu7AZtJfJOi0zcBatv8pjWHUhZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#شرمنده_بابت_پست_رپی
ترک جدید سوگند و سجیل به نام وقتی رفت ریلیز شد.
🎵
SoandClaud
🎵
Spatifay
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/funhiphop/81592" target="_blank">📅 20:51 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81590">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VU3QACddeGYwy8YKH8XtO9slbk7cExLcWBgpmLFQQqydhDmYKaYXrtQX0vnvEnWqLfEvbU7Vdvbltws5tkcWaB50w48U8hcxW-2jUJ4XP4vovYbu9Atqn3s2UFZK74B-sn0KMZU49mHfWSK_GQ7QFAE_DKrRO4B3mGmXqvfQR4N3SxnWbj1BXQ81_N-eAiXheSfUYnDdBWNWI8YWICbzDYSBAjiTMtqgaNUCrG8Vi5uRN1YqNoqz37h3MCernJcgb6GVHZacPVPVvP5DtExxrwtit8mcfaQq-wF3-5CsJBs9xZkTPPFFXND6D9qJ32Bg_4dP7uMl132brHA4KYSsUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دست خدا عیان شد
آقا تو کربلا رویت شد
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/funhiphop/81590" target="_blank">📅 19:20 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81589">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YU5IkPSs4it6eFvDdLBX0AFfAqYymb2HWSuMFFwopXziPeqU03cB9Sd-442njgDl5myQNmp3bk0hIRgytLCq7k9nYadV-tcOTys1gIksPfIhisuuSGa6y4churHAKOMPt03i4JHkH-zy-yWtwhQcyHkywD2A2NiQ5b0ob8OTqOBQirzMq-mTGStP21zg4fAhfb2S7GImNB98jEp80jCTmhwGgCH75Bw_kLb-Jq8K-D042lNVJ3okIXQu89EG2vi28oUi1PSzVH9G4CKS75RSCVynVqCM3xcfM_TRJKtnW-5idYHAjMd8lYxi45GeL4AJhaeJkZo_-tUdBcJ1LkHfKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هیپهاپولوژیست هم لایک کرده بود
@FuunHipHop
| Jenayi</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/funhiphop/81589" target="_blank">📅 18:37 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81588">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HJOALC-9oQJj38Z2Z1Ai2cTMc5ASWlIejKSsFiRjZSxDmtaoFfTmX9Z4NcYZYJ3dFJN11SIP6VLCK4QjetW6jPEjOZ6xPTJgoeRib-80sFdYybEd8G60BaRXRI_c2Bhw5-dWYgzXko7-mZWdtMASs2rc-SAokKGGCxJyivvlZffpi0s51xjXkg5BFvqvh6isO-STR4XRKUn190g4d8SNXhHFgLeUgUvbRtrSawn2v6kt22gL4qe2H6ZTsC4yVhU619IokJ_YZL1VpUvY-yaKFtjeej1OJVw6b8od7VAXfZASsMfcj_I_3NlNjQGORedPTsm1X1Aey7vuBUtpYzvVYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">@FuunHipHop
| Jenayi</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/funhiphop/81588" target="_blank">📅 18:16 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81587">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J9IDSjEtvIWh6hOUU7rQcrhUxfkebYgYmJGcbI1tlXBHBJ_g3MkiJCOoN95Fd9-XKdYrDPaoMVv3CiXpiEODsMIo5XiwovcTMkRo9dfFf2ylewzJWb4JgG0ot8GNkMQ_M_iZZL5hne8_q2_wXqOdTmBBAb7sKlDOs8PNvRdrcNN0Kstv8Dq7Sd9S4nei05MwAPao735wi-DacwtV3AH0W5PqrSzIXi9XhOJ0qeH4hNc3g0yZUTa64j2nppOuNnUPbar8X6EBtnyrtG2lgBKHvocEBnvKyIshNhDliwbACAqtKU-hKkSds2IXBSjcxjHwpKdB3W3j3HrjfBmZ-PB1oA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽
بیرمنگام سیتی
🏴󠁧󠁢󠁥󠁮󠁧󠁿
-
🇪🇸
بارسلونا
🏆
رقابت‌های دوستانه باشگاهی‌
🌍
🕔
جمعه ساعت ۲۲:۱۵
🏟
ورزشگاه سنت اندروز
🎲
با بیش از ۲۵۰ نوع آپشن پیش‌بینی
👆
ضرایب شگفت‌انگیز
📊
نگاهی به آمار دو تیم:
✅
بیرمنگام در ۹ بازی اخیر خود شکست نخورده است.
✅
بارسلونا در ۱۵ بازی اخیر خود مساوی نکرده است.
📈
میانگین گل در ۱۰ دیدار اخیر بارسلونا ۳ گل در هر بازی بوده است.
🧠
مسیر حرفه‌ای از نظم شروع می‌شود، نه از شانس.
👍
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
🟢
دریافت سرورفیلترشکن رایگان
🅰
r9
💻
@BetForward</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/funhiphop/81587" target="_blank">📅 18:16 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81586">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from𝗥𝗮𝗽𝗶𝗪𝗮𝗿</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5f78835d85.mp4?token=oSXt36_Mns26xUAfyALArOqOhpAr3R6VLVsOA4dTPuzB-DUFZP3Loo7HrftHB-HQx6zkFE4bEdzQzh4Hp1-h1zT3N51GQCtFJR59g7BGiSKjezx2Ke8C2Rjw-EfBMCdVhG_vNV0BKppFMTH8uRduguD6di0HI-tUihX2aSHK5h3lUKP4jSw-bEHvw8QbCIQ0AqnO2aRDsjrScokFGzYzNvo2gnfnJdIe4dgVNIqabfEgnkgpA4SiuxkwRvJfy5whWlGDuC35JJXJJPA9QJVWqhgTwyi_5AfIyy8YhSv6KqfVsnodTaELKmvcDJka8w2pje8-ar_jIPtAhZ3jzCn5Yg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5f78835d85.mp4?token=oSXt36_Mns26xUAfyALArOqOhpAr3R6VLVsOA4dTPuzB-DUFZP3Loo7HrftHB-HQx6zkFE4bEdzQzh4Hp1-h1zT3N51GQCtFJR59g7BGiSKjezx2Ke8C2Rjw-EfBMCdVhG_vNV0BKppFMTH8uRduguD6di0HI-tUihX2aSHK5h3lUKP4jSw-bEHvw8QbCIQ0AqnO2aRDsjrScokFGzYzNvo2gnfnJdIe4dgVNIqabfEgnkgpA4SiuxkwRvJfy5whWlGDuC35JJXJJPA9QJVWqhgTwyi_5AfIyy8YhSv6KqfVsnodTaELKmvcDJka8w2pje8-ar_jIPtAhZ3jzCn5Yg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اینجام جلوی خود خلسه دست میزنه به اندام خصوصی جی جی
@RapiWar</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/funhiphop/81586" target="_blank">📅 17:22 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81585">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2a90b7fcb9.mp4?token=rrkrzXnM16W357fdasn4bAlvxeiC09aaTlomhwcWrOKrRimE1dzj1lkq0tHYU6zxJiT_R-P6uei0ZN8Ax0m4Iml7I-P0PeMPIq2cQ_e6f2E_d2Po1u54Jvod44QtF-4lct4QotNaNXY96-SfV2B5Esd-H5b5u6VVDZHLOJPOrXM8VO1fzqTC7s7n02iy0bd3PPinbE01OAlll02nYYadC9NACwawKCK_K8LjYu8mULcsN5kTLF4tOtgD4syWWK9FzmMAIeyPK7BjcIBZAoeMMn090XkEqijtVGPvW9nVffeaBWDiB0UXJ2-2nnvw6x2xntIRdngSHCw1QrcAXT56DA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2a90b7fcb9.mp4?token=rrkrzXnM16W357fdasn4bAlvxeiC09aaTlomhwcWrOKrRimE1dzj1lkq0tHYU6zxJiT_R-P6uei0ZN8Ax0m4Iml7I-P0PeMPIq2cQ_e6f2E_d2Po1u54Jvod44QtF-4lct4QotNaNXY96-SfV2B5Esd-H5b5u6VVDZHLOJPOrXM8VO1fzqTC7s7n02iy0bd3PPinbE01OAlll02nYYadC9NACwawKCK_K8LjYu8mULcsN5kTLF4tOtgD4syWWK9FzmMAIeyPK7BjcIBZAoeMMn090XkEqijtVGPvW9nVffeaBWDiB0UXJ2-2nnvw6x2xntIRdngSHCw1QrcAXT56DA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حمله دسته جمعی مسلمانان به خانه های مردم در اسپانیا
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/funhiphop/81585" target="_blank">📅 16:47 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81584">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NjiqgZEcQ9IjfL_JvoATboLYi6Co1zHmbuAdAt6RBFbonBeYENv-ZoGazPzdcLGElTkNTpxbivXcdCG06Un2TMG-a93LqNCXZJhhTcHaaau5PY7343yuMXUvHqLhkJ8s5I611WVLwD4bomdKhNwbU2xOj2QMHiXr41v7SRahFNGBPRJO89UUP_Yyh57oTCUZVFgAeUd7C2h0qrh1RticIrFEyS0vbhWN5sTr3cPMnmyVC2P0BW-W9IqAoSx6t0Bl_n7BaN1F0mljAoHbXcl30NVfyyZiLAkRhCEs2cpSpd1vBMjV6nNr1tHD-SD5zI89zuRJxgP2tbc1uaSfFkw4Uw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینترنت استارلینک از دیروز در کشور عراق فعال شده.
۹ میلیون برای سرعت ۱۰۰ مگابیتی و دانلود نامحدود.
۱۵ میلیون برای سرعت ۴۰۰ مگابیتی و دانلود نامحدود.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/funhiphop/81584" target="_blank">📅 16:19 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81582">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nfW6NCps7AjlNBvdHOOgY8P2DLICpdjCU7ynFaG4mFV-Os4MHRAfeKlmnzzcwx9uzY_FVqpBkye7ReNFA4qsnQpNQNdEQRoaCtCotZzQ5Q8iFs4nYxmnt8rr4r8gffSHhXwXEgp0KcYDOZqeLo-A6-OMc9cJzRima_Io0HJCaAah0tpA7QnNE8glPG4XHaQTWw8hI7Bn79FOm_y5itsZfb2Py14XsgLUFddIbjDle6oYju5IO-Gr1AjHCtjAqbAvtC2K03tYDo6dFmzdf7c0vTI5uJKPRW07iZGKWT-ApBLRYxci_jgDC0ik9_x_jJSvxI7q_8awkpLghRI4YayRVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZSBbXrgHjlurxiFRmqaLXhDy5zSSLiMG7oezHusQeQEV4tGsdljnVYfk61vzcglTH-OC9kDnoXisGbFK8TR3YHlIkDaotN3V9Q6pNvnxaUMDeuIqQPVdQ0OqhkPCeG0M5xBYNzBjRBJmanDDjnphF8gmjUmDNwC-HHM0k7mUP5JfclJDDllTgrIgTk7-19FtfgqYP8Epyv_49ZvEQtoPHkdL49NLG3Jtv_rzzoAGx2M6Rn-FZQq44VcYRLZP7yR6PmHWWjEh9rnrybJqJRqqHQU1Dsj65b5yPx3cO1coWWJWogLwv9BusVgEX4vVBHKhHdB-i6Dhut5YE4CJAbh-ww.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">اصلا حواستون هست داریم چه بلایی سر اسطوره‌های ایرانمون میاریم یا نه؟؟؟
🥲
💔
#free_toomj
#تتلو
# اکسپلور
#پرامپت
پروکسی
پروکسی
پروکسی
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/funhiphop/81582" target="_blank">📅 15:33 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81580">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fe5jfXl2vuh5p1QZtAAkDMrrcwMZR7q4eaN4c83lVpVSeoAY--Ptl3RDZ-AUcGgfgEKad3cTXnUDWuFjC9EYgXJlaLJa87VfgRyMcBnKVF-g9c_n5DhSMbchi_lCTqR5FCtSsOmz1oZCZ0qq3tqD7_FfySa5zwj-jYU7G_CuMX1hx1O-Mz5-fAA-sC9t4UBvU-c-ufhxup5hqKbTiXaOh1skFNHqndqCcttg1h_CstGDsfYE8aAYsNglvSRFf2-BVN7hmuDEJfFUD5VzuV_LfXymJCUIit4OYADOHpDse_GzW5UQdse4Xd6_VtcRMH51kBBgirc13iPAF9mR4k0ZbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/k0gf0vbAxSD7pVj1q6MAdi_hXuolFvumqX52JQUCvIw37b0Ve_noFH5Az_38pEEmNngm6baIMpy9c97nXenlh2XI_ynMFqDjeHkn8tO38mqswfQB_hooSnBfLsZCDafuVcIK4MZUvYjed1CjQhA5HLowHVaD5g1TxHjD0jfaV83JIG3lGBSgo5HcNPeP8REb9fVoIiq_hKryB-0l3ht8jmTvnVFnh_s8LauX4NynOdCC2BVF_LPPe7NIZTZNjPfe_bOGZdDrb0W961J06kwiwYVhMmLhRHOhuo7tZ9TPc_SIOOzb08IHp9OJIjHmfAtQBejozKmcRXmYQdYxggVcGQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">عاقبت استروئید
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/funhiphop/81580" target="_blank">📅 15:08 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81579">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hNVp0qorQ5jsEufVY4ztME9HL6A0r1tLXNrPIrr8N03zOYZM--j5xFfh_gnE8-a0c3djpH4ZXisJTWtUrwqUNQt91LKv4cloJKI3iPjyegtxoAmbOnz-YvPwX811lVhGUjJE1pAVw7xtlaylF2hanH9nYdTZVuS_iXFrA6Ks8xxIEO4PRsYM4cQnovH7vTCotV2kizvam1rTQCPwOu8OnlJOU0qJiYPNFzuqUBG6V8kn9kaNudC_qPNUU0Z41I6K6UYwqCHLzIMn02ysYRi94HipnGNpopDdmBCIPibCKosIs1IcaPqVMAOyqvG4zokS2cNPrg1yRWWmvwubv74Zjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">منم میگم تایماز چرا انلاین نمیشه  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/funhiphop/81579" target="_blank">📅 14:49 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81578">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">ترامپ امروز با کابینه امنیتی خود در مورد ایران جلسه می‌گذارد.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/funhiphop/81578" target="_blank">📅 14:30 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81576">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">دوتا کشتی تو تنگه هرمز زدیم، امشب آتیش بازی داریم
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/funhiphop/81576" target="_blank">📅 14:00 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81575">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">آقا تبریک</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/funhiphop/81575" target="_blank">📅 14:00 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81573">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k4ocuGOyiJA2BvwPLLLXWPgJekTdBYa7bxkr3lhUj5H7pMRVJ_WDYGbibU5wZT25fAz7ny3XseC54_XXAJ-jmPqoAvTG9Ai_1PAjQbszvYtXRcT9poYSVXRznWKD003gFszoJN5bgUpiFoHC9ISRmfiRTUkzWoMPiyYunArgA_-E9DotPlNJmk-ltETgumm4GerZIAdCPpNyudSTiAMoNSODfRM5Guuj_KSynip14k8wu6AkC6cJ1F5TtX5cUbYrvo_tk-pCtp5sX8glKXMNS7NoDIacBJlDKHmqt4hR7bqpSXmpcuaX7VGeKxbcFBruW2-XoZyiJCCDdpnXH0nacA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">منم میگم تایماز چرا انلاین نمیشه
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/funhiphop/81573" target="_blank">📅 13:54 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81572">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gKTBi5RMn62LvGDKeY6ZhK3XVvS_9H9rQXaZubyf7KtNU9XjBAn3cOy2WRDVqxxybgxNKBt4vSiNrt0TBPz3ovX9PsPg5efZIrOY3uHsglZi82M6vHGYduEWb3SeOcT60sqPhF6YOOcuFxJEDZXtOQA9zQs__Vrd7lNj-ljJGzR81KUdSegiiPz0QqndugM7bmJ74V5OPSt1TS2mxdLGMKa6BA1CCrCZne2XW7c1skNRCmdCWmwQqlY7DGYBb5g4WDT_CMpYYxHICgKOtqpDgj5Os1xii8BAyX64VYaSb2yQDbIYfoLNxi8NMVEjZ_kLp67Eyn5-ygsyPEP1OI8dIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پسر وینی چقدر شبیهشه
(پسر دوست دخترشه، پسر خودش نیست)
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/funhiphop/81572" target="_blank">📅 13:38 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81571">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DWZDFOZV7Ao2jKbiIzKFDZUTYCfAFGb2-Awi6qbP53cNXb_1h__DC4QG3H331-1gYA9M64kzO4x-ZujGQ6xqrThSmN6cuxcpysCJDP79aiXasJqQA-7NoQrv41VCk_Gc6PKMAj1mFRLLnYmcuzKZtDV_X7ADW51eT3uBbXVIwsApCVnLBMQBxVKY-vrW8tVbM_SNl90uVX70NqhXMmixhtQce3PItQjASmEhx5cIrPZNzYU7-ABge5WxDrjKiMnMmeFsxIl_064HTh0LQC8B70fWYjKS6eoOXL0zm6gtosKDoyCIK0iBbJhH83sexjtpTOG6rvNXYzVJu93pqX0mag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آب دستتونه بزارید زمین برید این سریالو ببینید.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/funhiphop/81571" target="_blank">📅 13:12 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81570">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Uj4VYHo1A6Bs9-VPbW2uOi-nc4jz1u0u7p5Si7swZdzbrdfxSKWhN3rd5MklMNIZRKmSMTflRnmxMiJHN6GhVI4KdSiYK9paoRHSoP6vntGH62tnOvjFaMuKSmo_y2vEnlxZ8tCMdlOQhslArShiHKGosAx_P7UzBASziWSwqU9uaRER_RPn_lgwdDbhzkbT-e5bwWkwcflmwvx37HINIyQEpdRuvkV_dmEX37BRHYGh6gFiCOfKOyzxdclfUsmEunoOzoLryggjFxiSqcMMzqUwgHEwonxv9aJBhCmkRJTks9jiysBZW6Z73t3e20iB807tKMV59Yta9vlZDEQzpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زیبایی ببینید.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/funhiphop/81570" target="_blank">📅 12:43 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81569">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FejKB5hRDEpqPQb3hwy3Yy4Ol0Qz_B9wqmeeGwlAwZoK0HQ72EkrYsryg0o3MLOVehC7glEPnV6j4iKcbgvlFoYiFjKVXsukaC37Cqpi-uIBXhEbZE0c2oPxEf0L816bvWzGwGN5H9LdZzg-IjVZVpHKgTDqx1mOGZeJAYYP_z9wnf4Zkd1O2HhORz7MJGce50lAlpl0In_X6YFhFvAwPWSuY_l0D3NQNaNd39BRdzhoPwSdOr7b6Vfjmi8OWcYpXqiaT9dknISi-pUEQtTAvuGRDCptiIluuj_S_qxwFrDkkCub9vXguU8hwMJccuLgzisovR3B0fgMnPppDhT0KQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽
بیرمنگام سیتی
🏴󠁧󠁢󠁥󠁮󠁧󠁿
-
🇪🇸
بارسلونا
🏆
رقابت‌های دوستانه باشگاهی‌
🌍
🕔
جمعه ساعت ۲۲:۱۵
🏟
ورزشگاه سنت اندروز
🎲
با بیش از ۲۵۰ نوع آپشن پیش‌بینی
👆
ضرایب شگفت‌انگیز
📊
نگاهی به آمار دو تیم:
✅
بیرمنگام در ۹ بازی اخیر خود شکست نخورده است.
✅
بارسلونا در ۱۵ بازی اخیر خود مساوی نکرده است.
📈
میانگین گل در ۱۰ دیدار اخیر بارسلونا ۳ گل در هر بازی بوده است.
🧠
مسیر حرفه‌ای از نظم شروع می‌شود، نه از شانس.
👍
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
🟢
دریافت سرورفیلترشکن رایگان
🅰
r9
💻
@BetForward</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/funhiphop/81569" target="_blank">📅 12:43 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81568">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RbEGlqyCSK-eBefgqKXsXt4h4RF4jKjv52updaXCSEagSYYEmycynmSykoY4xPh6Hm9J-zKImZaC1kn8iGe4T2FaPb5QJiQ8iVpHQolINajsnUNn30QTgpjybg1nl2xkUYXPSoGBb-Nw3F1DzEtJgQklOZWWSM3eaYVG8uLAxeuGlUA7rAQiURKW6MG0myxQa1TSzKsZog_oES-zTwwUSCEn8MHkvTgMuqrvdF1B35D7pzpdScojxxx9ZGxJQWnFBQ6XujBBltiXgpzN2fMgkAwuAGWK3a0JhhaKeVfozpNJir61qY-s_ozumz_mcAUSbuNFB14uzQ6yOqYqM6qY5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/funhiphop/81568" target="_blank">📅 11:31 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81567">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">یتیم گیر اوردن کصکشا  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/funhiphop/81567" target="_blank">📅 11:20 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81566">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bf580585ef.mp4?token=GQDtq2ufkMyHO_xUI6pHjL090P7EyvulaM-u8UJ6q_L6R1fpOm0HiM6-BDIvg7hqlMt6XvgNYaYPKYjCDc58n4aNV75EiCxBcuZzrYpq7lri16oWtvaW1MmpJR1UiH_w8oZdUmfiPlmv76fLdpiurERnzlR-9s7WQptCx7_IFW0KiJQFIZxP0bMIKSyURBRbfXW1cbH27kBg4GtOkmqvjKBm6yRi_xQmQs8SvhCRExqoMbEuzuaucsfnwJf1AUECtnJmeORqJ6l2YIJjrCWFfLseQ6vRhUvsWycWzXsYHXeyOhdPszEr7s-vPDwX0nFuR7VPHrAzJPwl2AeHdt2gsA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bf580585ef.mp4?token=GQDtq2ufkMyHO_xUI6pHjL090P7EyvulaM-u8UJ6q_L6R1fpOm0HiM6-BDIvg7hqlMt6XvgNYaYPKYjCDc58n4aNV75EiCxBcuZzrYpq7lri16oWtvaW1MmpJR1UiH_w8oZdUmfiPlmv76fLdpiurERnzlR-9s7WQptCx7_IFW0KiJQFIZxP0bMIKSyURBRbfXW1cbH27kBg4GtOkmqvjKBm6yRi_xQmQs8SvhCRExqoMbEuzuaucsfnwJf1AUECtnJmeORqJ6l2YIJjrCWFfLseQ6vRhUvsWycWzXsYHXeyOhdPszEr7s-vPDwX0nFuR7VPHrAzJPwl2AeHdt2gsA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شعار مسلمانان مراکشی بعد از نفوذ غیرقانونی و حمله به اسپانیا: الله و اکبر، ما اروپا را اشغال خواهیم کرد، زنان و کودکانتان مال ما خواهد شد.  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/funhiphop/81566" target="_blank">📅 10:23 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81565">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FvTuze2-1YFuxDrlyUWy1BpaX2MYSJeUbRWnn4ZHq_T5fDZKjdbKw-jpmSjloU0IrMKQphhQS_dKcjCBFOsZsm8al9SKHr9KFbhdjTVU0lz9of8JijB6kLV60c4Z_HmsAcQGLeT5rGaJIkalxpCdasddygFx_zTGgMvPw_-ChCeIEAhkHUo9dhQaiL8g9X8ZBiNVtOEcfVnSQvK5Xr2ADet0b4SX_7SEWAbcKSe_auOUvajKj8mQWlqm_4clGCYl7E7XN8u62vtnoswpXEJNYVWNzMQzD9RUf-qgb99gqlFN1IAEV2cd3avzCgxeMcpEG0NU1GRv7xik2bI0uRQ1Hw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بعد از این تحلیل کارشناسی شده‌ی رائفی‌پور، خبر اومده که عربستان داره برای حمله زمینی به یمن آماده میشه
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/funhiphop/81565" target="_blank">📅 09:47 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81564">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/76336c1936.mp4?token=nGu6Ns0sB62yE0mrbdk_oPZDxzxClOXAyhJ4-LeTkUDa0QvyRk4cqulKZZrtFKfRHqgIVhNj3sguKf8Wbph_LycJtMbr9aC66NxutbsluiZMISApFrxch1b9gFi5hr8qXJHtalO60qs11oOgMgzaDPmBolHthbe65jxggcMrmahSu8kG6meJNGtFJRLrLUnjEtgP10Tr0fXXf5V9v6eoxxrun4q97-YBdoPdxd6Bs2KChL6ki9rvZtdFKVCdkUkuA-0DkFxw98Q0eseSS79zuHjYKLqymm3L6xjx9_dFGvyDvn3f9MZ8P_ka2zM0SwG1sSw2hDkZInaoOn_cJ7t2BQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/76336c1936.mp4?token=nGu6Ns0sB62yE0mrbdk_oPZDxzxClOXAyhJ4-LeTkUDa0QvyRk4cqulKZZrtFKfRHqgIVhNj3sguKf8Wbph_LycJtMbr9aC66NxutbsluiZMISApFrxch1b9gFi5hr8qXJHtalO60qs11oOgMgzaDPmBolHthbe65jxggcMrmahSu8kG6meJNGtFJRLrLUnjEtgP10Tr0fXXf5V9v6eoxxrun4q97-YBdoPdxd6Bs2KChL6ki9rvZtdFKVCdkUkuA-0DkFxw98Q0eseSS79zuHjYKLqymm3L6xjx9_dFGvyDvn3f9MZ8P_ka2zM0SwG1sSw2hDkZInaoOn_cJ7t2BQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خودشون سر شوخیو باز می‌کنن بعد تا ما چیزی می‌گیم میان می‌برنمون.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/funhiphop/81564" target="_blank">📅 06:02 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81563">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">اسپانیا داره شبیه سوریه میشه.  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/funhiphop/81563" target="_blank">📅 03:29 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81562">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">اسپانیا داره شبیه سوریه میشه.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/funhiphop/81562" target="_blank">📅 03:15 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81561">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">حماس خلع سلاح می شود   ترامپ: شورای صلح امروز به توافقی تاریخی برای خلع سلاح کامل حماس و سایر گروه‌های مسلح در غزه دست یافت. این گامی عظیم به سوی صلح و امنیت پایدار است.  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/funhiphop/81561" target="_blank">📅 02:19 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81560">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">حماس خلع سلاح می شود
ترامپ: شورای صلح امروز به توافقی تاریخی برای خلع سلاح کامل حماس و سایر گروه‌های مسلح در غزه دست یافت. این گامی عظیم به سوی صلح و امنیت پایدار است.
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/funhiphop/81560" target="_blank">📅 01:59 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81559">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">شب جمعه خود را چگونه گذراندید؟  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/funhiphop/81559" target="_blank">📅 01:39 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81558">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/06fc3e48dc.mp4?token=hYSmHAh4CHTjZ4oS_bvw3AKBpZVYGnXysp80qvi33n5Pj8NZwfVUrN_UWppfL3poxrUoNZbS0UVbYK21Vrg-Ls_hl9d_vJTzCTokwITusdXA-9ry9BoVujFkMbgMZ9wKoneXvZGGa7isJxZgQYT6w-fNEHdOm_A9pHZOCoUG1YXbdURkonwsbVmLiAsOMWOWqNB-nx1m3x2z4Mz0DUztMWlAFN7PTw1k3-297GjB37tMaKRr4c6EeZzW_uEjWZ805RI81poG-MvU5FC-Ij5lC6hnY9sq7U9R5DGsDSvIgMUu2d0-vmzFoEoFYrnEzZ5gVpYBPPA9ZdPi6-TpPbRn9YWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/06fc3e48dc.mp4?token=hYSmHAh4CHTjZ4oS_bvw3AKBpZVYGnXysp80qvi33n5Pj8NZwfVUrN_UWppfL3poxrUoNZbS0UVbYK21Vrg-Ls_hl9d_vJTzCTokwITusdXA-9ry9BoVujFkMbgMZ9wKoneXvZGGa7isJxZgQYT6w-fNEHdOm_A9pHZOCoUG1YXbdURkonwsbVmLiAsOMWOWqNB-nx1m3x2z4Mz0DUztMWlAFN7PTw1k3-297GjB37tMaKRr4c6EeZzW_uEjWZ805RI81poG-MvU5FC-Ij5lC6hnY9sq7U9R5DGsDSvIgMUu2d0-vmzFoEoFYrnEzZ5gVpYBPPA9ZdPi6-TpPbRn9YWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صحبت‌های جالب پژمان جمشیدی درمورد شایعه‌ی جنجالی
بوسیدن دست وزیر ارشاد توسط ایشان:
آقا حالا ما نشسته بودیم یهو رندوم خیلی اتفاقی وزیر ارشاد اومد کنار ما نشست منم یکم چیز شده بودم با هم گرم گرفتیم و داشتیم می‌خندیدیم درحالی که دستم تو دست ایشون بود یه ذره خسته هم بودم یهو سرم خم شد ایشونم تیک عصبی داشتن دستشون یه ذره تکون خورد یهو دیدم رسانه‌ها دارن تیتر می‌زنن من دست این بزرگوار رو بوسیدم.
😐
این تیترای زرد و سخیف و مشمئز کننده چیه می‌زنید.
😐
چجوری می‌تونید نبینید من همیشه در کنار مردم بودم و برا همینه یک هفته‌ست باید با فیلترشکن وارد سایتم بشید دیگه مشکلتون چیه؟
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/funhiphop/81558" target="_blank">📅 01:14 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81557">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">این پست مربوط به رپ فارسی است  @FunHipHop | Taymaz</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/funhiphop/81557" target="_blank">📅 00:57 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81556">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sctq85JXrOhfCaa7vyLUl61GhGcgz4yVSmj420XeGkUyb9XrkIY7_oox6iVZdDnXDjCsAPNv6FfavBz_eaBbdD31Qt-9NMOVbbqw8QtmvTEezAP08tTQap7jZh7WjltRcB6I-JbUWkqkdxSobY90e9eD_2qfJDe78pXOWN9hIECru9jWeGvsRipI7raX7AQDlttnym9zhbpxoddhMoNRwv19EvtY4JJQ9T_irL9KXix1qwt9ceXdRUeTe54dexOpcU7U0_ax_DPTcBA33PB50BuRUep5aLmRuPEmurLhB2UCDS7eNaMpyVHpMGLmBFZLCWcPiiuEmaTm8RRc7QTiJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این پست مربوط به رپ فارسی است
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/funhiphop/81556" target="_blank">📅 00:06 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81555">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">دادستانی تهران علیه افراد حامی محکومین اعدام دی‌ ۱۴۰۴ اعلام جرم کرد.
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/funhiphop/81555" target="_blank">📅 23:34 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81554">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LYxRhAAti3mq7P7rImpr1gkhHtRlswNz95V5wvc9S-l3Yp5p2UHm-Gqy6UMtEMknS1U5x_a1_xVRyHlCMeJieNad55bbWS3PCF237OaUa7XRFuLK18TlaQXDyyI1Jyut1brC38A_jPFIyHUKPI9aRfowow37S2xE4clJFrJlzOzVwzT5ZqZ7E8T72DSX5v5uMhon8ljRuQbTIJ6qJRyyoC15w1XusEp0KoMBi_j50al0Ni02oIh906xxolwn4_ATFgptBzvztvDXbvdP8LcJuod7sQG_R25Rpnb9okTYnsuBfihrg8kEvZtRx_VuVqAfcFvNk5RbBQjb0nME1hTlpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بچه ها ده سال تحمل کنید تمومه.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/funhiphop/81554" target="_blank">📅 23:14 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81553">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/37370edf56.mp4?token=eNzNQlQu7q8FoRzu9ltN6A8AA6i3kaIeOqNd2fh6tnV122335sqWg8xe5T7bDrq9OQMyv06FgJd8Xb1ktLz3UEjCCPljOeaAjwhtQ1YVv-Dxb2EitGAHCiCPztSVpAzFA4XQMg5OaTYX3LkNRBBMnEDpaIEjttNmYdZQ-payZ6h53SLGNgqDrIs__nh7JxfGPPWFTzvqqS9XgXZDm2GN-f9kJ-wzHikwztbHimaMjngbEJv99JYhkfkwkLnfLR1HE-EmmAYC28NbT-_632DeZnRNxt-0RDEcmHpWAN-S5k6yUl4Vi5kJH2CgWZYlK4xkXqRxb4WGPrfAr2isCD-q1TAk82rzbK8n9ZuJNqEgd-MAp_v1M2Sk6A48Orp45kaNbi8Nym9zxuLcQ8Ao5ar7b6IU8GAOnfPzBsAazvDjoB39jQdLTmaQ_Zgr82fLC-v70FUmD6lo28QGcIu31sNnUcPnjwhU5xGHnWWOLIDNkGXONi4AhAxtclxhktPe1UHA7xByI0c3a-N5Ia5VhgQHdBtm9GONwMpRH-qavdSeRFpnJQuSEyrYUTRFqvuu1GNkQkhLZ_XVdDfjDppRlS8IthcJX1MF4po0TFzaaddoDiJzEpvcBspfIQVmcGTYNtnADPO6AKmZB6AICPIFyA4PX4bGkx3I4xekOXIrT1Smgg8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/37370edf56.mp4?token=eNzNQlQu7q8FoRzu9ltN6A8AA6i3kaIeOqNd2fh6tnV122335sqWg8xe5T7bDrq9OQMyv06FgJd8Xb1ktLz3UEjCCPljOeaAjwhtQ1YVv-Dxb2EitGAHCiCPztSVpAzFA4XQMg5OaTYX3LkNRBBMnEDpaIEjttNmYdZQ-payZ6h53SLGNgqDrIs__nh7JxfGPPWFTzvqqS9XgXZDm2GN-f9kJ-wzHikwztbHimaMjngbEJv99JYhkfkwkLnfLR1HE-EmmAYC28NbT-_632DeZnRNxt-0RDEcmHpWAN-S5k6yUl4Vi5kJH2CgWZYlK4xkXqRxb4WGPrfAr2isCD-q1TAk82rzbK8n9ZuJNqEgd-MAp_v1M2Sk6A48Orp45kaNbi8Nym9zxuLcQ8Ao5ar7b6IU8GAOnfPzBsAazvDjoB39jQdLTmaQ_Zgr82fLC-v70FUmD6lo28QGcIu31sNnUcPnjwhU5xGHnWWOLIDNkGXONi4AhAxtclxhktPe1UHA7xByI0c3a-N5Ia5VhgQHdBtm9GONwMpRH-qavdSeRFpnJQuSEyrYUTRFqvuu1GNkQkhLZ_XVdDfjDppRlS8IthcJX1MF4po0TFzaaddoDiJzEpvcBspfIQVmcGTYNtnADPO6AKmZB6AICPIFyA4PX4bGkx3I4xekOXIrT1Smgg8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شعار مسلمانان مراکشی بعد از نفوذ غیرقانونی و حمله به اسپانیا: الله و اکبر، ما اروپا را اشغال خواهیم کرد، زنان و کودکانتان مال ما خواهد شد.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/funhiphop/81553" target="_blank">📅 22:37 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81552">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/mFXImB_YaSRdUIGqy1cwU5cks8J7fjY6ZnpOWOUT54LIhVgG75yyqNhyNwfUerhjNXZO9InYC1fRrvt1jE2ptng1z5SoNbckTDnW1oOUfLZF4c3Ho7LTxJh3K1D7cctY2fOP-PgbMjRuCSSBPU3qaNIEAu8Gyi-xyui42Ht9zuKwNdzxilF2NkFRFifzloqmMYfXeYOnicCCXWxgikqLnjpD6vxBUv0m-yxlY3LjuJVjHrt0EtoJB9fYAcBmrPA9b1-VmoxzsLjHbB261af_e0Pq0FSpD9dMVaWZfN9Se_zrwq6rqYCSCABb514oS6u3WezR9KnZW44ISCNV6LPAfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
😐
پشمامممممممممممم
نیکی نیکول دوست دختر سابق لامین یامال پورن استار بوده ، فک کنم یامال وقتی فهمیده ازش جدا شده 4 تا از فیلم هاشو پیدا کردم براتون گذاشتم ربات چه
کصی
هم میده لامصب
چه ناز و خوشگلهههه این دختر
😍
مشاهده فیلم:
https://t.me/Footballi_Dark_bot?start=get_tbcbmlqhfqdjyaew</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/funhiphop/81552" target="_blank">📅 22:27 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81551">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">ترک جدید مهیاد به اسم چشات میگاد ۲  ریلیز شد    SoundCloud  @FuunHipHop | Mmd</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/funhiphop/81551" target="_blank">📅 22:14 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81550">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dyu-duWTUsxpTasm9apEXJYf7Apa15OL9Zz2nkuxxZTod-HoqW7igsAyTMPDNEWzd6wCXsBIeHWAqzcl6d6vGIq0uSR67ZYx6GSiztCgBochkCwhKhmaMA7IHwwiolZEEU1cozbw3lu0ZQq_5wJpdhplXf-cDYD9PYDuLh2o1ESsQfLLwIncC8-67oRWZTAkdUAkHqFfoBzaQN80l5TuBgHigelrBJwwj8NDC8cVpH8iLjikelw74JniIlIbHjQ-CrqmzadZ_AKC_A8VHq5qNAlRwCxMP03u4Gj_xAVi9Vmtd17gxgdmg1UOIKOj7BsWn29uTU791uEdEEVQaoxI4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترک جدید
مهیاد
به اسم
چشات میگاد ۲
ریلیز شد
SoundCloud
@FuunHipHop
| Mmd</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/funhiphop/81550" target="_blank">📅 22:13 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81549">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c2Zogy1ZDPJIEIfxGyHoY1zfxZxhwzZ_v_DOYB0hY6wXAzeKk9c8UDNfKKtdyRUF0xnr8fNyI7BYAj6J7l9ybSk8LyqkxR9QrhMFmfDSaxvtVR8Jy0xqXGpxo47t7Kiv-juyRl2PVilT8FYtsdVhrEQcROVpD43Em8aCvGyxSTT3TT9IdMH-1HnoIc8r_cBPxG8FkZuBTbUg8-I3CFbUFS3zSzdn32h_7m_Xma3yb50NsgH3iyzmEB1tsrntnJvT0Hg8sdOq-QuLZu5ffSatcG8MIaznKZmIHWE09fjso4r-WoMhydrRvpu1iH_yNJfkJjPzlC1GwrZ_VnebxGKQGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یتیم گیر اوردن کصکشا  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/funhiphop/81549" target="_blank">📅 20:59 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81548">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">پیج اصلی سروش ولی زاده برگشت
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/funhiphop/81548" target="_blank">📅 20:14 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81547">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FqMdocKZ_Gz8WGViOr5cRoByrhgNvmLjfzPXgXSc5gjpNT1-R-omGjkkcCvO4mWbIMgRPGQh8_C8CgYzOYr_6_CKLA1GBFn_M2UGS9XwpVVUPecY1iU5wK1_iyCWc40XwAEvcL2Ysr14LPIaZGAKIco95V2A3IYKfEqdoOsOHRl2u6yrfbVco1GdWvpJUzyN0N0p1rAR2FG7DCvbcYtbOYAFktv2_4OqsRiliTZnAHrpdNKkj1Ckm4mji8jlaTREfbvmKow33uOrvT8PYuFqli2YKT6zGffsy8H3YrDm1njzug2E0uffxTOEuaAPbiNiM4B3pOO144qfZyYITf3rdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پروفایل پاول تو تلگرام:  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/funhiphop/81547" target="_blank">📅 19:57 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81546">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JC8v9MSmzGyge0eXJuDTWyw_jIBxchqzQQP15Fil9ldlvwuF1khy2BWudhPD2FEQ4c9oD61E__5PNbShCHmjUgJWmTpMSk-9QlrlLUvbwal3jqY7M1XuW42sswmZXv352K5bu4n9USUQs9yEr4ouDlFwkQ0ZaRd7j2x1dW9VjhKR0-N9cYWnOAFK_ZR-M87d4iJeYt-bSQaAcL9wVxUj8IjWNxJK6DLMykKTLMcBz1JKVcIpbgOfbipzz0Tmn-ZZIPAagKGUwYPAuKkKkGH1aOrGeq1JGerOD_oiXEMmE66gyi6rMq22ZF1dF2VXyp2-TkgA1yUC7V3wgXd8niFd7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این بازی شاهکار رو از دست ندید‌  @FunHipHop | Jenayi</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/funhiphop/81546" target="_blank">📅 19:52 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81545">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ALzyRVKtqGDhIUVHnw3ErmDXfvXC0Ic5VztTc16fiYwJErCB8zUWM-5wsInPOWjIWfAOtVZVUxIcs0BHsd50EdkeNJk9OBD09rHnv5IOWapbreQjcVONeuM3SdtAxnLXPLnNKrgnx6rTeDM6Ruachye7HIWvu3xdqk3TGfUfQNi9eTcDIbZwhwBYICOhPgjIBdJ80qHnd8fJosinTwUYaZwwDuIuaNUZy557qLykpLWGsERsjC6J4uJ91WP_lu21_huGgPuNN6cH12RxEX4HFYoVrIKzslbHy-kl4ZOB9v2LUPA3PHdjo90sSN3pxlahjpJvsKUEX615L59gdieN9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این بازی شاهکار رو از دست ندید‌
@FunHipHop
| Jenayi</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/funhiphop/81545" target="_blank">📅 19:45 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81543">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qBnAhY_21kdThY4qaex5aCmEQyhmE4J5A0pgVjpT4RMe4_ITE2oGbAB21MSQ2gGdmp0rpPQ8wnclsnpmKXrFdPn5jVsIsAZBsVzJpBf4KpNoqp4C7D2zdnFK2yBdrbw4K9xZBuyrZW11l4r2vb7zKw0FOiQY70_3u_Q7Fua5kt0CdCP-sGZOHyLR69Dr4J9r3hqIWZjuGAP5Mv_cqPdJgAlzsIg6d6b9wj8WFN_EYkcEu2AtEZEiVu3MhCZ-A4JXPvdK2haa1zUgMDpxl9Ol915DbMCopM3El6NSoi_XMNCveYWjA30sdR8RJIvRPV3Cdpg_TWx-Zgj0P4T9SUIRpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ایران:
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/funhiphop/81543" target="_blank">📅 19:06 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81542">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QePd_mkfftwUsvw9R5PnKMUCUOmbax2HN2FzFVFn8G3CMU2SyTLCHt4TQ9eoWQ5Beyaq7fjevQrEjcP2tPzqukejnvbnu4gYdY1_pxnQCBn3TvfZ_kFKq93wLkzpRkO6MxnbQqhpyNKZmhs-FSqEU7Q0TmhGK4Hm_9ctNMWioo911987ASH1M8HjBeErVxLPZFONlHot4h2TYtQukw2ByFYg-vR6DMLpANCg71Nfx44RiI3pdeu19b8m8PKHcDOPWtacooSkrVXLD2uE9Jes-KVx0EdeVBWPjMwOneQfkNChT0Fy7q9YBr-gi4-Px-stGWabw7ODgJOqNaHYZX-FcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گلشیفته چقد ترسناک شده
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/funhiphop/81542" target="_blank">📅 18:01 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81541">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bi2lxh2guiqhsjNYzlyYH9p5sOMsyVejH8EShVPc9zUNlsYzdtiowW5s7C17mRWuI3DUmY-uVyVbnAKw-VQt9qOKYQWd96JOPQPiERghBNZKKR4sOOXZ8E3c71x9TZrnA3QEddRbE3o3XNKJ-iJyMLBC94kBviLMF4i2jkYl7G9ml1LRWM2LIJvzKcC6QXnAMuI0u5LvgE5AbcLNG_UpxYAdzz0ay3uF1oMy63tZCZIa7Za_E1NMAsjSgSusCvqGEYfuuNxo4_20D_x3ko7cAC8ehcYuvVUV5gS6hYDavD9SQ1eAWmg9Vj8WF2rfM1xsaX8dZn-PX6rzedTOeD7CSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حکم اعدام بنیامین نقدی، جوون 26 ساله و از معترضین دی ماه صادر شد.‌
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/funhiphop/81541" target="_blank">📅 16:56 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81540">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Asj3siKb6gN3wbU6Dcl-eNamLzVOdEcw8PchJ4hqAL3qEe5cDHxWdFybNSfzNsgOabZmoLDNaOBCArhk6uqhJlgGQzFWNFmBYWoUMWS_5bCaWNC_C1r3Zc3kdF4njniWcUmFd5NE7AUULoEKUBsQjL3BRUItoHgf2zbbBFeN6DXXYa2Z-h9h0HO9I1TXxgSz2rCKUlZFH_U4Tx011k7TEE4_eR-Gc52MACMM1XPG77lAEWjHlpvlipz249uZpaOBGCKykqk_4M-sup04j3S3NVGhcGyb9SJO3my-kzsXqD24ivd4hvgfuNyqswq1Slm0XjKbuxkloQojWKkBYK0A_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیج افشین فدا بلاگر مازنی بخاطر استوری که برای سه جاوید نام اعدام شده تو اصفهان گذاشته بود بسته شد.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/funhiphop/81540" target="_blank">📅 16:44 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81539">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">از نیرو های مسلح درخواست دارم کره‌ی زمین رو منهدم کنن دیگه زندگی کافیه
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/funhiphop/81539" target="_blank">📅 16:30 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81537">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S8-PDVLuB68Cug_svpgNBWEi0aCdP1l3o3XpSVWwsFhCii8Q7BskT0XuYeB1nmQHbxeGKCtLVHkJMHqE3b1KvFlEKqgqq9IVL-uof87plIu3Rb_JmQMiyax3EVQBRI79L1zncYz547DN6eEfyGUMmLCJtPfvWiTy6nW1_l2TvCKsiD3P8Seo2GNKHF_mVAWJO4mRC35hL5Fscw2vGMQHiX8ePzaTJ489uodFgD6uLC9rtYQ3l2Cw_nZiULWPkcYclIU3VS7kXPl895rcGYt_iaUyeFR4pA_sxebJMhHTZjEPCVqGb_cWt3JDdnm7fcK0soopX1N21G-kaKTG9v_YPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آفرود سواری در کشور ممنوع شد
تصویرم از وضعیت یه پیج آفرود که این تصمیم دولت رو به تمسخر گرفته بود
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/funhiphop/81537" target="_blank">📅 16:00 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81536">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">اشکال نداره چین میاد بهترشو میسازه
🔴
چین گزارش‌های منتشرشده درباره برنامه‌ پکن برای تجهیز ایران به سامانه‌های پدافند هوایی را رد کرد و نادرست دانست.
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/funhiphop/81536" target="_blank">📅 15:47 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81535">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OmxPbSN93aOY3xcaGhc2OhOIjIHabMWbkMf6yrmJARHh3SreEqTizSOaoEe34GQ32xTyc7conPUoBC1gG4gaOLcFYjRdkWZx7mqshih8QOwZ_Ce59Y0i7KWCsLfhWOSU4i2U-GBe7JTEg9XW_NJCikAjV8JHqkGDqyIbiylUwpU_JPQuL6ZX351H4sVB5Wpjkzf83kfd7Tc0SEQjGqldSygDabcfLabNbNe657kpAqdZsqlL3NjYpoNrwZJTW6_U1LC2EieHjxZmarVAIA6-8xBLo8fCY64NT1CkQZJufa5DTP026ZAVgYebYGczFvMXodnXL_zlJ216qTv8Xs2DaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آماده اید؟
صداوسیما: امروز صبح در پاسخ به حملات آمریکا به ایران، 6 تا جنگنده F-35 رو زدیم 3 تاشون کامل منهدم شدن، 3 تاشون هم خسارت دیدن چند تا از خلبانان جنگنده هم کشته شده.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/funhiphop/81535" target="_blank">📅 14:42 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81534">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HZnNT2oWYg-WLv7huvxh7Gd4XDgKCUSrI-kbA3EjsF061Rh3k8AT8dSJHsX0jhf-KEJy59UeVzn1QXKQi_NLptPc_bbG5yO2hQDNS2i2TUNPOqwmSH5r8W-NSDNUBOMPT-b3Sn9IP2xeOCAhpLM59nodsJ6Jgj944u-614002eyybk6wwhzVX7N_spvOyuMc57USOvenwo1c4M0z5ZXFsVHXRrFTGHnwWURenNF5Dkp7sbSlmjmymwXOYtgB0h1rTjUEPU_Sb2H83YZKJltYRopTJtRlvi8XPTLyts4vbNAWOGrYWDaCWFTjKQZrCqL535hBTeA1QIIt0w-2wudfXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دایرکت یه وکیل دادگستری.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/funhiphop/81534" target="_blank">📅 14:05 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81533">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/533f3ca2cf.mp4?token=BYuJ7RLrz_zTJum5tVZh9nXByhsmsUvEQWRYREbwwt0n6klr3r0mzaZqxt0nQl11q-TQuZ47h7eFEtwpPlSeXOwSXgbXg3ZdiXWW1aQzlDrLQeJQg94aojcida9EbhelOGWsMzyb0EzWleFSY692u5P2193OQYOKfx3fnUA9nO5h0KfztCslcIHzOacNAeCjTEGFr660vjTTkG-rLr9S6MKEQxNk_dk29zp8wHesTFOhkTJ6OuTBUvGpTPyVzZOmpI0MbUxLH-3leoI-XB-7G07OFCObt8S7urEGEE7OBWTXTGGT2kVOtfxJRIl4N65IX-YkU-WBDqQWAnpa1DDQUVQ0sma7rr5DTmBagSpQTGl3iC60-hPRCTuNS-LiVjcnMc4oiKDs71t8CBrWsRUgmYI6cQ2zp4u28XIHQYEUcLUULoM5Q_oF9UDWW5b_DygIKkTSKxlA7vgcymKVF4gCZVNZ6vsxLdjn0rLkdE9Tybfqwekb5nodUHkbjRr59UVFCtwC8sqDhO7bNFSZPMCvr0cIZn3hVy6TaOov4D4wUlGu0iKvIMr9xMSx2WIzmVyEOAJjpYWWxYjJjsNvpMkwtV0Nz39uazRu838lNdW6K__GEZmyHo5bgO66OvU30Wz8NG4OU9frUf7zDPoQZKgf1wQgj8Kmq9oSF0VMQG0YRYw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/533f3ca2cf.mp4?token=BYuJ7RLrz_zTJum5tVZh9nXByhsmsUvEQWRYREbwwt0n6klr3r0mzaZqxt0nQl11q-TQuZ47h7eFEtwpPlSeXOwSXgbXg3ZdiXWW1aQzlDrLQeJQg94aojcida9EbhelOGWsMzyb0EzWleFSY692u5P2193OQYOKfx3fnUA9nO5h0KfztCslcIHzOacNAeCjTEGFr660vjTTkG-rLr9S6MKEQxNk_dk29zp8wHesTFOhkTJ6OuTBUvGpTPyVzZOmpI0MbUxLH-3leoI-XB-7G07OFCObt8S7urEGEE7OBWTXTGGT2kVOtfxJRIl4N65IX-YkU-WBDqQWAnpa1DDQUVQ0sma7rr5DTmBagSpQTGl3iC60-hPRCTuNS-LiVjcnMc4oiKDs71t8CBrWsRUgmYI6cQ2zp4u28XIHQYEUcLUULoM5Q_oF9UDWW5b_DygIKkTSKxlA7vgcymKVF4gCZVNZ6vsxLdjn0rLkdE9Tybfqwekb5nodUHkbjRr59UVFCtwC8sqDhO7bNFSZPMCvr0cIZn3hVy6TaOov4D4wUlGu0iKvIMr9xMSx2WIzmVyEOAJjpYWWxYjJjsNvpMkwtV0Nz39uazRu838lNdW6K__GEZmyHo5bgO66OvU30Wz8NG4OU9frUf7zDPoQZKgf1wQgj8Kmq9oSF0VMQG0YRYw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
دیشب مامورها ردِ نوید زیادخان، همون فردی که خانم‌ها رو‌ تو لایو کتک میزد رو تو خیابون خرمشهرِ تهران زدن؛ بعد که رفتن دستگیرش کنن، این مادرقحبه با قمه به سمت پلیس‌ها هم حمله کرده! مامورها هم اول شلیک هوایی کردن ولی دیدن تاثیری نداره؛ به پای چپ ، پای راست و…</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/funhiphop/81533" target="_blank">📅 12:55 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81532">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nW2kTTqrWuTQRhGjTW_wnDFNakh4suWX8iMpLfJhFvcAfyGF4gCe6PktMx6k8yjoVNoGV2dXO0qaRv-ok8GhdR-CnJ7Ij5Agxyez5vn36tbWexnPd1aCGwiSPpLNlqtFXSY8JwTHSuCtDIxwEYqWvakH_I7QzPUEaB5iYGOGA7_S55BAz0vbvI7vYPKHcUw-a7zuUXVUarAv8MtyHy5RaIISYpMd8Ar5n5JpYnXB4SmR9hIanN0MlxglTnkEzNFjelMSGcofUfAva8CvxL6t-A8mcnyTQDt2hvIogQ21wfTan-ydvhkxN_o0l3oUs4mO1swFuJHN5gx3X5np-fEuLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
دیشب مامورها ردِ نوید زیادخان، همون فردی که خانم‌ها رو‌ تو لایو کتک میزد رو تو خیابون خرمشهرِ تهران زدن؛
بعد که رفتن دستگیرش کنن، این مادرقحبه با قمه به سمت پلیس‌ها هم حمله کرده!
مامورها هم اول شلیک هوایی کردن ولی دیدن تاثیری نداره؛ به پای چپ ، پای راست و دست چپ نوید زیادخان شلیک کردن و این گراز بالاخره زمین‌گیر شد.
این مادرقحبهِ 36 ساله، قبلا به اتهامِ "ایجاد مزاحمت، دعوا و درگیری، سرقت، ضرب و جرح، مزاحمت از طریق فضای مجازی و تهدید به قتل" زندانی شده بود.
@FunHipHop
| Jenayi</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/funhiphop/81532" target="_blank">📅 12:53 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81529">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">یک منبع آمریکایی به شبکه "i24NEWS" گفت:
حمله شب گذشته گسترده بود و تأثیر قابل توجهی داشت. این حمله تقریباً دو برابر قوی‌تر و گسترده‌تر از عملیات‌های قبلی بود.
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/funhiphop/81529" target="_blank">📅 10:27 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81528">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">خلسه از زنش نیلو جدا شد   @FunHipHop | چمن در خاک</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/funhiphop/81528" target="_blank">📅 10:20 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81527">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">خلسه از زنش نیلو جدا شد   @FunHipHop | چمن در خاک</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/funhiphop/81527" target="_blank">📅 10:16 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81526">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">خلسه از زنش نیلو جدا شد
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/funhiphop/81526" target="_blank">📅 10:15 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81525">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GNVxa7e2Df-f7FVTan-3T0aqb6mbhBjBOzViYAK_9msrrWJl2cqeRLfFbud1Lbx57ZntyOacQlk-fz7rwt1zrijeGOPhGhd1OwYgjMbbEexk3GZL8mmkStoe7-aWnwOX0wJenthmJDIITHjz0BQky8c5Uxbev-k7tzzEpL42o7ZORQ8pBrNCb1eWbg3PgFdrPjed3Rco5U4wSJylypqQZJcmOkS5oZeqwI4RGSnpPDeWgBbLqZj7Iv4_TraZQ4kcb23SNAQ_WTCbDjLfnkbSmyq-qZq3cWaACpDNV3C7aVPj5BzyX8anfQPLtRSFS-7uFh8pOzBFQ042A2uNek5f1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ای کیرم تو این اکسپلورم
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/funhiphop/81525" target="_blank">📅 08:46 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81524">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">اینکه شب گذشته آمریکا مسکونی زده احتمال داره یه پیامی باشه برای ایران واسه جنگ های بعدی که احتمال داره رخ بده، که امیدوارم کصشر باشه و این برداشت صحت نداشته باشه. (اگرم انقدر اورانگوتانید که فکر میکنید آمریکا کصدسته و مختصات اشتباه به بمب و موشک داده و صرفا اسرائیل نقطه زنه نظر ندید کلا)
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/funhiphop/81524" target="_blank">📅 08:17 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81523">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1b757b219d.mp4?token=ZIEgbcnyXqWqpi6wzu4ofr7xfUuwz8_wkogU5XplxHlAu3m5kCB465X_ZhjqVeG8LDWQ3rFPtBxyQE9TwNSkV8XwGsT1LPhGEik6-yPy4USOdLJ4Q5TJwwdBfU6j4BURwcl_KTBWSiyZJKMzEUhSv_mehSB4Q_3CZpWfIPU5oCkhQ0DMCkjaL-m2NhxbLnaEr0O0iMHZwoasWyhtdEMbv89n_G38j-q0bw2xde9PzRzzzeMN8WO7qGYKWZBzWQbt_-bwE4faxdLk9ZwujeK-bVlE8_opAIEsVG3E1BEOaDs_ocmcpG8QIPFLzZJZMm0rp_D19hPgMVldIfm_L2Lcbg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1b757b219d.mp4?token=ZIEgbcnyXqWqpi6wzu4ofr7xfUuwz8_wkogU5XplxHlAu3m5kCB465X_ZhjqVeG8LDWQ3rFPtBxyQE9TwNSkV8XwGsT1LPhGEik6-yPy4USOdLJ4Q5TJwwdBfU6j4BURwcl_KTBWSiyZJKMzEUhSv_mehSB4Q_3CZpWfIPU5oCkhQ0DMCkjaL-m2NhxbLnaEr0O0iMHZwoasWyhtdEMbv89n_G38j-q0bw2xde9PzRzzzeMN8WO7qGYKWZBzWQbt_-bwE4faxdLk9ZwujeK-bVlE8_opAIEsVG3E1BEOaDs_ocmcpG8QIPFLzZJZMm0rp_D19hPgMVldIfm_L2Lcbg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">متاسفانه شب گذشته هم:
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/funhiphop/81523" target="_blank">📅 06:51 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81522">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">نتانیاهو:
نمیدونم دیپلماسی چقدر ممکنه اتفاق بیفته، اما نسبت به شیوه رفتار ایران بدبین هستم.
اونا همیشه دروغ میگن، همیشه تقلب میکنن و همیشه برای خریدن زمان بازی میکنن.
آیا ممکنه این رفتار با اعمال فشار کافی، از جمله فشار دیپلماتیک و اقتصادی، تغییر کنه؟ باید این رو امتحان کرد.
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/funhiphop/81522" target="_blank">📅 06:41 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81521">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">تسنیم:
برق برخی نقاط اهواز قطع شده.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/funhiphop/81521" target="_blank">📅 05:05 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81519">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">انفجار های پی در پی قشم و بوشهر و بندرعباس
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/funhiphop/81519" target="_blank">📅 03:57 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81518">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">بوشهر آبادان کیش
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/funhiphop/81518" target="_blank">📅 03:42 · 08 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
