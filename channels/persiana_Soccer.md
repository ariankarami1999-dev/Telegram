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
<img src="https://cdn4.telesco.pe/file/h8btISsDn1lLBnJInvFEzvG-MizRLxLn-DJYNzR6lCIq1SJ_Gogt9hoksvToT_jpF10XBgH6ZcekQph0q0T6hq5bHDDC_PupLi2N8DlxkBd5gIkBdPgARpBejZJVTFlSgUcib0MEnvPfCNfs1H_qOgKtoxcIckseYIJ6n_H6X8bMLBe-WWeVmbFH9v-8qqmxnOAphMKBMUKvO10JA8x2k9GwJ4u5TYQV8NEe-QiWKY8tK77yusrURvSeh7e-ASoCaIENI4CcP01f9s5NB_A3MpyBwsfyfRcMh3WvuWaCUyb_hxSmpWomh6JqEmlHTVAmTtpLAXvK8GqNPLTRDBvmgw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 310K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@ads_Persianaaپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-29 13:44:06</div>
<hr>

<div class="tg-post" id="msg-23825">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9fc0b5e928.mp4?token=EK62__OlJVmwmKBSSHAqYIObv84gBI5crrsShyaW69nNU0Iu5FFtiwrecIJzz4CMJOTMHRCAKCihl4F07Qxanz8hV3NbRNJYYlZsmUKq4j2ioPXA90S0kSxEMVSvZqk0sZyzOXspm9dNMKsYPt-OGnkqUYPYoeOQmgwOqtau3JloT7QA5_7hsIvv1ctaZD9FL5pM3l6dOJiIrLInvKvLR3o3xl-9OpZjO4jN9R614KUhDEcGk4PJ9uxVrS8yCTCGFBhpxxPhmX-s_Ob6dPJu8IJrmyFyN8fkwdoE3g0zT_t5kaLJr17Upz0yDoj6XC2OlqrI4SoWCkJPkjuxWdtwqQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9fc0b5e928.mp4?token=EK62__OlJVmwmKBSSHAqYIObv84gBI5crrsShyaW69nNU0Iu5FFtiwrecIJzz4CMJOTMHRCAKCihl4F07Qxanz8hV3NbRNJYYlZsmUKq4j2ioPXA90S0kSxEMVSvZqk0sZyzOXspm9dNMKsYPt-OGnkqUYPYoeOQmgwOqtau3JloT7QA5_7hsIvv1ctaZD9FL5pM3l6dOJiIrLInvKvLR3o3xl-9OpZjO4jN9R614KUhDEcGk4PJ9uxVrS8yCTCGFBhpxxPhmX-s_Ob6dPJu8IJrmyFyN8fkwdoE3g0zT_t5kaLJr17Upz0yDoj6XC2OlqrI4SoWCkJPkjuxWdtwqQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
صحنه‌دلخراش‌ازبازی‌دیشب‌قطر
🆚
کانادا؛
خطا مادیبو بازیکن‌قطری‌ها روی‌کونه‌بازیکن تیم ملی کانادا که موجب شکستگی استخوان پای این بازیکن شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/persiana_Soccer/23825" target="_blank">📅 13:09 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23824">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TdkhJMwShptY53miIWd9sUyQLnzcB6CDPedLQKrIlL84trrtYqh4ckrJjm6Y73oXB6W6Aa9_WN-xKcKFwWXqn_pisOMr5-LIGsyAON5UqnTyARCFKmVjUZtIfNBkH5Xj1KJC07LrI-AOpoygXd0digvxaVfF8_eryV4_UnUskgfnA0kGSiMOlZS6NNq6C1VpAIcz-S8AR-0-9JZGQgegpDTUq7ZLpqDktOFPlCfnko468AwzVmnta9GZq_TM_aGrVLIxiQuO7txwieFRlJbgblPnnpCpxOO1T1ogf9PrB-q3SEl7msLWcE2qtZJcngtRT-HZpD8CFU9XgFhkowktRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
عملکرد کامل لیونل مسی
🆚
کریس رونالدو در کل دوران فوتبالی‌شون در مستطیل سبز ببینید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/persiana_Soccer/23824" target="_blank">📅 12:46 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23823">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/15564d6447.mp4?token=TMzqROF2F9MJFXil5FDoksHBKG7bdhilLt5NXnGS7ptINEu68X4VU_bwyKqhJhTw5znNMrCX6sQpsfvrbkZRsLBTTYaFpLqQtZNfSJmz9ue4nGjs6FYs2gopxP4dz8AUpbiLAj89GXAUxsINdkZraBX4FGAZYiVk8JxOjsZKUqh5idZHkf_Nuc7Fe1drKEAUdQ60-f6n7ESqrCrrM2cjQwO-yBA0HRzpuglWwh8069uElE5AouNBR3H3Tc1o7oW61sa-xhE-Cyl4vjFEkbPACOvzu4F9sgw1M7w1qe2xwQcdeAjjBzOZLFyAMtKiT7i0EdX8vntVYmXUikhKL8Tcog" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/15564d6447.mp4?token=TMzqROF2F9MJFXil5FDoksHBKG7bdhilLt5NXnGS7ptINEu68X4VU_bwyKqhJhTw5znNMrCX6sQpsfvrbkZRsLBTTYaFpLqQtZNfSJmz9ue4nGjs6FYs2gopxP4dz8AUpbiLAj89GXAUxsINdkZraBX4FGAZYiVk8JxOjsZKUqh5idZHkf_Nuc7Fe1drKEAUdQ60-f6n7ESqrCrrM2cjQwO-yBA0HRzpuglWwh8069uElE5AouNBR3H3Tc1o7oW61sa-xhE-Cyl4vjFEkbPACOvzu4F9sgw1M7w1qe2xwQcdeAjjBzOZLFyAMtKiT7i0EdX8vntVYmXUikhKL8Tcog" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
پدر رامین رضاییان:
خیلی‌ها بخاطر طرز تمرین کردن رامین او رو مورد تمسخر قرار میدادند و حتی ویدیوهاش رو برای من میفرستادند اما او برای جام جهانی برنامه در سر داشت و مزدش رو هم گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/persiana_Soccer/23823" target="_blank">📅 12:29 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23822">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kOygqNojSISExG2shF5RvF0DspZ0XiJjf2NURHV-U_m_UOeDhsi7lSrke814gwRXL1i6ID3tqb4y8JEDKjjWfRHspxaXC1x_tpqTwMsv8ydEIYl6yKXVW-ZZOa9L5v4Ik6BWed7FwfKAQabf7sN6--EDq2IkRpGhitzZsO_s_P0VtB_hmeEIJGXd18dk_ICSFwbT7NHdfUGLaE3BqCBi3LwmjD7sgJSBfwgsxE34gBs2nQ85Bk1S05u5X2We3frAJ2vD_aJ_bRbLGdr2UocPsf1GEZE55B9cTOABw2eIFA1FaW4mdURshjHtdhTMweuBO7ylZcFaRDKufFuiGrDVcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🟡
👤
قرارداد محمد محبی با باشگاه روستوف روسیه به پایان رسیده و با توجه به اینکه برای تمدید قراردادش‌اقدام‌نشد او بازیکن آزاد بشمار خواهد امد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/persiana_Soccer/23822" target="_blank">📅 12:18 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23821">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rnT4st_ywiQZy5JwnVJhahl1LS9ReMjz3mHg70TJuZLq-cgT0izYYFnclKBsOF9VxtepIkaCtTdEQ4NOvl78prchUZNiFFqp1w6RrpR4cSbB6osAa287aTPVHaonl0m0nLI1PPHiMvOzSpKU9bzk76Y8-dp69HrkYef8G60vniRkKyPMoApSaCBuh8sDk0kdmez1BO6PCLcSc-EI04t-zbY-1Y2ldNIgquOBhn687fJX5STqaBkbjMQX1odp5umCbUzmUnz3HwXi0ZUpMxTO5W9xzuhjtiQF3N7dTLQBvfC7CvIOj2EVLWPMb-DCtmG4RSfEt7QWkESwEJag6oc87Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#فوری؛ طبق اخبار دریافتی رسانه پرشیانا؛ مدیریت باشگاه تراکتور منتظر فسخ قرارداد اوسمار ویرا باتیم پرسپولیس‌ است تا با این سرمربی برزیلی برای‌پذیرفتن‌سکان‌هدایت پرشورهاواردمذاکره شود. اسکو در پرسپولیس، اوسمار در تراکتور؟ باید صبر کرد و دید اوسمار ویرا برزیلی…</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/persiana_Soccer/23821" target="_blank">📅 12:08 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23820">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b4aaa4b5d3.mp4?token=tq4RZBFQY6X5pK-Tx06NzKVQJPNil1H-aoEdiLNb86XL-EN1gH-eSOjdUfgOvSrlmTMqEPHO48bRcHsKlb2FIyQ1Vm7UXfUuv5ZhZ9SOcy58uGG7PFKRfVqeuDfaMfw5O4tjDoIKoJBx-sSlf6VD7fcLxXTpdrDOphRFWYfccLGWY6PwLZTDuKlZNWKpvqw4SgtD22BB-mSpUMtSImQ_QKB50T38gTU0Ri460nV9UMU8HWoznuLW67rN0NrR5kfdupLW-kHF_EgPbHSbIiC5arhLAZOAaiDN_QXR4ZpR0xdZskqNwTvm1AoheaCrT7QTt4pjylIuB-OY9fjvTVyu2w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b4aaa4b5d3.mp4?token=tq4RZBFQY6X5pK-Tx06NzKVQJPNil1H-aoEdiLNb86XL-EN1gH-eSOjdUfgOvSrlmTMqEPHO48bRcHsKlb2FIyQ1Vm7UXfUuv5ZhZ9SOcy58uGG7PFKRfVqeuDfaMfw5O4tjDoIKoJBx-sSlf6VD7fcLxXTpdrDOphRFWYfccLGWY6PwLZTDuKlZNWKpvqw4SgtD22BB-mSpUMtSImQ_QKB50T38gTU0Ri460nV9UMU8HWoznuLW67rN0NrR5kfdupLW-kHF_EgPbHSbIiC5arhLAZOAaiDN_QXR4ZpR0xdZskqNwTvm1AoheaCrT7QTt4pjylIuB-OY9fjvTVyu2w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
روایت‌حنیف‌عمران‌زاده از نحو خداحافظی اش از دنیای فوتبال:
یه‌شب بابرادر خانومم تو باغ بودیم تصمیم گرفتم از فوتبال خداحافظی کنم به‌خانوم هم گفتم یه‌متن‌بنویس‌بذارم تو پیجم، صبح که از خواب بلند شدم از خداحافظی پشیمون شدم ولی دیگه دیر شده بود همه زیرش نوشته بودن تو ادامه مسیرت موفق باشی منم مجبور شدم خداحافظی کنم!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/persiana_Soccer/23820" target="_blank">📅 11:28 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23819">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bda6868e35.mp4?token=O7-i8vTu9ifTMQ6-1Qkm-XWmKYD8-BnadgsY-QTLjcHAG29yCnpoRtnkEoeEWU_xQUN7leFyALOpEKFryQoo9gaX4IwlbzTpkMwKxqqs5fgU5R3tmixEhlfHDh-M3A1WHRW-WzVR_lWSQXXuH4LAiLvN7JRaTMLO-Fe_aMz6gYCmjAGRvEMPLJ5Du_9UYtXwe8V0DJJR4M1FGcitaTqVdJJkIrZln0L7GII81DlUXF2LtRmM_Iq0pkeeM592HEYFH10OPf6eAmI8k5eyxsMdCRCShXnw8dT_Oa07lMAC7LpIGibQGwu1N5e1GIYyrmWpKPp9q8_wsqBlX92v9hrVWw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bda6868e35.mp4?token=O7-i8vTu9ifTMQ6-1Qkm-XWmKYD8-BnadgsY-QTLjcHAG29yCnpoRtnkEoeEWU_xQUN7leFyALOpEKFryQoo9gaX4IwlbzTpkMwKxqqs5fgU5R3tmixEhlfHDh-M3A1WHRW-WzVR_lWSQXXuH4LAiLvN7JRaTMLO-Fe_aMz6gYCmjAGRvEMPLJ5Du_9UYtXwe8V0DJJR4M1FGcitaTqVdJJkIrZln0L7GII81DlUXF2LtRmM_Iq0pkeeM592HEYFH10OPf6eAmI8k5eyxsMdCRCShXnw8dT_Oa07lMAC7LpIGibQGwu1N5e1GIYyrmWpKPp9q8_wsqBlX92v9hrVWw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
پرونده‌نقل‌وانتقالات‌تابستانی رئال مادرید با این دوخرید بسته میشه: 220 میلیون یورو برای جذب مایکل اولیسه + 120میلیون‌یورو برای‌جذب انزو.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/persiana_Soccer/23819" target="_blank">📅 11:28 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23818">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">چرا این روزها همه سایت جهانی
MelBet
رو انتخاب میکنن
⁉️
🎁
شارژ هدیه 130 دلاری اولین واریز
🎁
شارژ هدیه 100 دلاری در روز های یکشنبه و چهارشنبه
🎁
و ده ها بانس ارزنده دیگر...
🥇
متنوع ترین آپشن های ورزشی
🖥
پخش زنده مسابقات
🎮
بیش از 80 نوع ورزش مجازی با پخش زنده
⭐
کاملترین کازینو آنلاین
🛡
امنیت فوق العاده بالا
🌐
اسپانسر رسمی جام جهانی
💵
واریز آنی جوایز با بیش از 30 روش شارژ و برداشت،
از جمله کارت بکارت
🎁
کد هدیه 100 دلاری: Sport100
✅
معرفی سایت و اپلیکیشن مل‌بت
💯
ورود به سایت مل‌بت (فیلترشکن خاموش)</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/persiana_Soccer/23818" target="_blank">📅 11:28 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23817">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J4dEk4K7U4-PmBowuFlLbq4KFQspdbHtDl69rF5e3eGJ6lyvYKzgwn7W21CY84iHJN55Ofbco_Tea3DKyQNEDXcC1qEoliPJMoBlSY3k54caWLPtl90BN5z9Tf77DvhUccREUOkWvRGkMKjB7_ZJg_LxQ83GXYrNVEwXdoMCTxob-Np6nssKzPDcYuIMOPQOp2rmgOhiWKg6k_u1CvYMJ4V-eHd3IPfM62imbxj_F90EloxbptajRVplGR6evYv1OOFBXniJPh_gaWGU877CNOgxhtl1Wq2UZZirjJ1WN4UFbrOT5zyeBNbXQDFAzqXBzVKcpZVWYU4RNAlcAQjZVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتیجه دوبازی هفته‌دوم‌جام‌جهانی؛ تساوی چک و آفریقای جنوبی در گروه یک و اولین برد تیم سوئیس با آتش بازی مقابل یاران ژکو!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/persiana_Soccer/23817" target="_blank">📅 11:05 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23816">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4ee7c7274d.mp4?token=uz6_FiwkjnUX-QnUsI7vNpZnSdLkKHi6nS5BjJxT8ij3chl0fkdlQu2fZZbWHGk7cKu_9GA2YkPPsUPDzkbj3N0nzFNawHHO4eYD6BrbBYjYAEIlSKK6mZbZxdLuXoC3gDkyaeeXRIqnIa8-ilhp2Xvf8Lb0XkH1jIRFFib1R5WlKNedIIyQJ8BHUGQhpe9Ba6xWxUtFSkIdpavtfzwyuIffd-yEvCtrcEcrZtjT2dvwEXtC9vmOaPKexFe-uH3bG_Ono-BQNpmb-7Hgsr6EUNvLFPWZOyL6si921JfSLP96zkBqVDPl5xbk9G-qz660yhH06nmDG8Syh-1x229TNA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4ee7c7274d.mp4?token=uz6_FiwkjnUX-QnUsI7vNpZnSdLkKHi6nS5BjJxT8ij3chl0fkdlQu2fZZbWHGk7cKu_9GA2YkPPsUPDzkbj3N0nzFNawHHO4eYD6BrbBYjYAEIlSKK6mZbZxdLuXoC3gDkyaeeXRIqnIa8-ilhp2Xvf8Lb0XkH1jIRFFib1R5WlKNedIIyQJ8BHUGQhpe9Ba6xWxUtFSkIdpavtfzwyuIffd-yEvCtrcEcrZtjT2dvwEXtC9vmOaPKexFe-uH3bG_Ono-BQNpmb-7Hgsr6EUNvLFPWZOyL6si921JfSLP96zkBqVDPl5xbk9G-qz660yhH06nmDG8Syh-1x229TNA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
رونالدو نازاریو اسطوره برزیلی فوتبال جهان:
"به نظرم اگه یه نفر باشه که لیاقت اینو داشته باشه که جلو بزنه و عنوان بهترین گلزن تاریخ جام جهانی رومال خود کند، اون آدم کسی نیست جز لئو مسی؛ مسی بهترین گزینه برای داشتن این جایگاهه."
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/persiana_Soccer/23816" target="_blank">📅 10:49 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23815">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8463cba5a3.mp4?token=ZU6wqcM77CQI3bjT6tRkRBBhKsQCIDfC__ZjdtYkry1qkKA8GPOz0rxEKxhx_uR1c6BO5MSdZk4bimF4HCvj2ZFl_Lv3RxL-3Bnnb_xPoGNXh_zV-DfZEL3i7zzF551VvkITLke_TZP2Lj4RDjCRz_6cAXKzEGUskKc7-RBe5YpgvNQHV0SDThaTCF_6x8f8O_e3T4e4LadB0bZR9PrUxxli9xMN2Uqvlu3JYD8ZbPKzCiLsC3WinQ7jFnOLfi3MRb6LwLuLJlrTiICyqP9vHVLJ-gyPR66JQ7s--nqAMSdVpNBWGXb7dl0dOldaQY1SwMwQXsxL8r_RB9t60UiV6A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8463cba5a3.mp4?token=ZU6wqcM77CQI3bjT6tRkRBBhKsQCIDfC__ZjdtYkry1qkKA8GPOz0rxEKxhx_uR1c6BO5MSdZk4bimF4HCvj2ZFl_Lv3RxL-3Bnnb_xPoGNXh_zV-DfZEL3i7zzF551VvkITLke_TZP2Lj4RDjCRz_6cAXKzEGUskKc7-RBe5YpgvNQHV0SDThaTCF_6x8f8O_e3T4e4LadB0bZR9PrUxxli9xMN2Uqvlu3JYD8ZbPKzCiLsC3WinQ7jFnOLfi3MRb6LwLuLJlrTiICyqP9vHVLJ-gyPR66JQ7s--nqAMSdVpNBWGXb7dl0dOldaQY1SwMwQXsxL8r_RB9t60UiV6A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
مزدتموم‌تلاش‌های یک‌سال اخیرش رو گرفت؛ با اعلام از فیفا: رامین رضاییان بازیکن تیم ملی ایران با نمره ۸.۲۳ بعنوان‌خلاق‌ترین بازیکنِ دور نخست مرحله گروهی رقابت های جام جهانی 2026 انتخاب شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/persiana_Soccer/23815" target="_blank">📅 10:33 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23814">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rh6JXTrQf7owuJFzwdNa0Fm3grMdgOUAKFe0WEDvI6_m8VqgyWX9gvyajwyP5pwOjMoDe9729tqcDy_ar2V9R1BN0VJMO3YcZhVmAW9qArinqdYKeraIbuGqjaDTH73WRmgTx9cqlBARX7IjFTzxmclbML-NdeQoFLh5NGbTUEIjoGy4750A7sNnCyF4a3hu40uQxWIdENeH6j__fA7EsuSHUzRj9ksl3kH5qOkezA_BPIhmLXLZLTznZ32JpH2ZjYLw52ku81cxeh17FDEUW8EkVpnnqBMHBZbOkV_0Bs4Ioldna87lLKc2Kiv-uUhUAWR4vY0Ock0BfE8LFvnabA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📱
تعداد فالورهای وزینیا دروازه‌بان تیم کیپ ورد از 50 هزار به 3 میلیون رسید اونم تنها در 5 ساعت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/persiana_Soccer/23814" target="_blank">📅 10:26 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23813">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i1xZu4_YLdI6Wm07Iwe4hFAYrGTJj9VyYAP95yEg4iG9imUA0l2MIUmqAqJHrA3eXd6KhhXRn6_WacKiJlbnndihlfGQ5PzMU4_b08dGm4LXfzIwtAyay8WZX5D3rAn1-1sqk8aaG8VFgSbywvNkfV3IxsgTb2MhPGmKBif_rneFxAmo5jE1uPwJdaO2-BPK7FZrS4H4tn9XzIvC4TEguQ6zyuYIt9EkAdPcEb8RLdIYvj3l2MpaqQhBYermKa6WfvZmOeQxXlcFRKLqKIOc3dokhumSog_rWsq6kH1s21jk4YGaM8VJmZDJdSSZSvupyL8yCPzFj4Nk7GaG0lVLRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛ باتوجه به تعداد سوالات زیادی که پرسیدین؛ لازم‌بودبه‌احترام هواداران پرسپولیس بگم که‌اوسمار ویرا لیست بازیکنان مدنظرش رو داده و از بین اسامی 9 بازیکن که به مدیرعامل باشگاه داده 5 تاش رو قطعی میخواد حالا اگه مدیریت علاقه‌ای به همکاری با اوسمار نداشته…</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/persiana_Soccer/23813" target="_blank">📅 09:51 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23812">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">📊
نتیجه دو دیدار بامداد امروز جام جهانی؛ تحقیر سنگین قطری‌ها مقابل کانادا و پیروزی مکزیک مقابل چشم بادامی‌ها در گام دوم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/persiana_Soccer/23812" target="_blank">📅 09:40 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23811">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7641de3fc6.mp4?token=WrJ5XPXP-auXKST--nlFaaxnE_6PiTOBhZBjJ8P2aPNoSQP3BPKW5QfUFaOWPOqnQ2s45DNyxvNeEy5dNlheH9jqQbYXExyh3DL_uuT-b8xqY72I-bxnLQLhPQ6lbNFZb2k49WkJgt3QgJa1X7_bmmx5I78GmVCAhiuzpDhSwbBTxGqs5FBB8pvLkYJgNHDqRTsUuj0FiFuIL_mxmfCMyQrG6HCGqr7LCrSMH68hcGPfAxHQHNaxIa5JpX-iIWBAbWEKdCHV6LZfzwsR2-IGfm90TR6XuB_gQaILyN1zG0KJd2fuFYJHGDO2Z2CNfdaIzYwf2FmG-rdowX5jwucipA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7641de3fc6.mp4?token=WrJ5XPXP-auXKST--nlFaaxnE_6PiTOBhZBjJ8P2aPNoSQP3BPKW5QfUFaOWPOqnQ2s45DNyxvNeEy5dNlheH9jqQbYXExyh3DL_uuT-b8xqY72I-bxnLQLhPQ6lbNFZb2k49WkJgt3QgJa1X7_bmmx5I78GmVCAhiuzpDhSwbBTxGqs5FBB8pvLkYJgNHDqRTsUuj0FiFuIL_mxmfCMyQrG6HCGqr7LCrSMH68hcGPfAxHQHNaxIa5JpX-iIWBAbWEKdCHV6LZfzwsR2-IGfm90TR6XuB_gQaILyN1zG0KJd2fuFYJHGDO2Z2CNfdaIzYwf2FmG-rdowX5jwucipA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تاکتیک‌امیر رولکس برای‌بازی درهفته‌سوم مقابل مصر؛ صلاح و مرموش روز سختی در انتظارشونه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/persiana_Soccer/23811" target="_blank">📅 09:36 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23809">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bGhs8-xgsjU-M3LJ69oq-tFeA5dWJbyJuPIB8MhazIOdbMPir0l64Cyb5YNGuUANz-uqxKwllRsjDeXSZ-NV1xZxToEkr6zJQ7Pofu2awktb2C6ie-cptwdpSIH0UintewTM2BHHZtAMPSUf8O_BscHaPmNpikOEuFvgCSoiqcNj07gQ_LWRBp2o2C7R8ftc1ZA2yB55I9_QDn4rSFMn497RfHLeFcNlmgb7_010C1XjseNMa5ST1ikIuv7Si9uCa3gjJQR8HoINpAOm_Gn7-VEVwjotJk4To28SV9u9_sy7l95kYo0Wm0XIpH9DPrwRT-WfDOvW05JIerSb38wVsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lUX0Yg3dawl2JFf_U0DRIS93U0zf6LzFsUyYiHo-pwWuu2kuGp5AyaUBJgLGRhHBrCXWeoXkREBHk2lo2nY0Mrr8rI_EwfYlzWCixRlkboi04csBcS-V2oCzfNd2LcBE68YCwMCz03ekBEUcOyenvkgvXT-vafwPh9Opqxh9quBz2xpVQ6lpTMdzj2DoxQIH2stbgqWdt8uNB-Tm8Vt_E6Te5gGQMjcKnzrBR3DXAsvSLP00V4W12rcCodbMljRFK35BvMGjdOj3xKcnaX4i5Xqrox1PE2EEZMCURSAhm3zHa6KIrEgZL5xsyxIT6hDEyd0Kbf1LTH0CeaZ2IeGGog.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
برنامه‌دیدارهای‌امروز؛ از رویارویی کانادایی‌ها با شاگردان لوپتگی تا نبرد آمریکا و استرالیا در سیاتل
🔵
‌ @Persiana_Soccer</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/persiana_Soccer/23809" target="_blank">📅 09:30 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23808">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EYZfE7YINPIsx8Yq4pwCm2fsHBBUXlprobv8g3pg5BAxmCmAUnlzZaV8n2M4LFkJ_AqYZIja6DVvqPcuYmdBKm7Gl_KNnIDGqYcmfWczkStwzUuP5u8smkXO5s-_P1aX3NsLScKVBtDsTctxbi7vbM-EQT_C0ebFqr-IJXlccz7uTdkOdNMtk7SyO_S0AyL1pLvPLgVMUZh2CSNVhTm96vM6IicOlxxHVvsZvNiqDJD5d2w-X5FXWnmrHMjLnZcWBc41KU5BxVxlbn-v_ihArTj1yn-GM_59aCK-vqNzmBxO_oftYFhkzogQoQTbJBK3nXZVp4vnmNkF87rRHG1AEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مارکا درخبری‌فوری: باشگاه رئال‌مادرید میخواد بزودی پیشنهاد220میلیون‌یورویی برای جذب مایکل اولیسه برای بایرن مونیخ بفرسته. با جذب اولیسه و انزو فرناندز پرونده کهکشانی‌ها بسته میشه.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.4K · <a href="https://t.me/persiana_Soccer/23808" target="_blank">📅 02:38 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23807">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7ab6b2cc1e.mp4?token=E_bHzO09SHDJEgqhgJqFFQsxKx1Hm28-D0ssWX6fWAgd5JL01itUhMwn6MYUWpCwTpv3--aLtcJLyzuF1tK3ZE4tcHq8vpanwM_lD-2zK6LgFci-YkVIfv2-lB1sd844DsCE9JzODVtMbKFp_kgjkZdDF4-SKFYCgIG583PRv0XdjwJbAUnrHYHB4v_zTkmDB7hdljGE9FCOvBT_j74x_AUfSC4rT9SmAPl7doOz0b2DMQs0l2NGh5LRg7pr0gW7G3QFuyHGHl8pK5GRmqp_0Yb64Yp64OrnJwwyOWGX9DstJq1gyYZ5euSSqcLZlX1o_jAfo1mvTGwiOPueOrV-Zxy36Ki4YCu_3iz00L25Y_V_Cj3rpSvNbqExgydq6UbwwoKY5YRY6y-wH4XjVVJyiPDMu8J2PLr16PN335AhcKcI8JPqW6lRAzNXIjIsjiLOkTqICwzEOfhlwhFqKW1SwgdNGrfmb5Le2-UOzox4UOhOQ7-y64QSVOFTl0gXZllyC3f8iFr8QmvTkz1pupuaHRSgjhatreAq1XN4zBjtgx2WKpTurdHVXYw8NICRmYP2itPPZ06pO1Ue6QJWyTyz6xH8A6k8JwNflTE_xB6kzeP5COpPFk-G61I_zyhEAz-ZHB7WytJAAHGqaeAVX5iQOIMejDLm3rmjaBzKrLdx22U" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7ab6b2cc1e.mp4?token=E_bHzO09SHDJEgqhgJqFFQsxKx1Hm28-D0ssWX6fWAgd5JL01itUhMwn6MYUWpCwTpv3--aLtcJLyzuF1tK3ZE4tcHq8vpanwM_lD-2zK6LgFci-YkVIfv2-lB1sd844DsCE9JzODVtMbKFp_kgjkZdDF4-SKFYCgIG583PRv0XdjwJbAUnrHYHB4v_zTkmDB7hdljGE9FCOvBT_j74x_AUfSC4rT9SmAPl7doOz0b2DMQs0l2NGh5LRg7pr0gW7G3QFuyHGHl8pK5GRmqp_0Yb64Yp64OrnJwwyOWGX9DstJq1gyYZ5euSSqcLZlX1o_jAfo1mvTGwiOPueOrV-Zxy36Ki4YCu_3iz00L25Y_V_Cj3rpSvNbqExgydq6UbwwoKY5YRY6y-wH4XjVVJyiPDMu8J2PLr16PN335AhcKcI8JPqW6lRAzNXIjIsjiLOkTqICwzEOfhlwhFqKW1SwgdNGrfmb5Le2-UOzox4UOhOQ7-y64QSVOFTl0gXZllyC3f8iFr8QmvTkz1pupuaHRSgjhatreAq1XN4zBjtgx2WKpTurdHVXYw8NICRmYP2itPPZ06pO1Ue6QJWyTyz6xH8A6k8JwNflTE_xB6kzeP5COpPFk-G61I_zyhEAz-ZHB7WytJAAHGqaeAVX5iQOIMejDLm3rmjaBzKrLdx22U" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تیکه‌های‌سنگین حنیف عمران زاده به قیاسی که سانسور شد: امیرحسین پا میشم میام پارت میکنم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/persiana_Soccer/23807" target="_blank">📅 01:50 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23805">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mr93pZ93BxNI0WPtUhfrzpKxs3_iegEwlCbmFmx9CJ4yI_KYIQkXb2lXdta6lYEMHh2zIm982g5QCkeTEn9jA6G87W87FOC-vcJFYzwsUWTw3qO17Sq4wt20gxZ5mgugwCyuAVGHIWsTN28N0CXuvOrkTc8-pTQwa9X-2HFfl87Gq58KjENkpxLa5YWROn5jir-ouOTHvxR-IoAJtgZOg7tojpcGdOstmJCRQkW0Qo44uSR0cPcVFS6M1SeMrVEARZOr2OISA7m92FgM1FA6Zdf9pfXa36XsD7I9Jr7Hd6jZP_Pmuv7e-m1boZCpaCEmUT4AZJW_tBvaVJ9YMQLScg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌دیدارهای‌امروز؛
از رویارویی کانادایی‌ها با شاگردان لوپتگی تا نبرد آمریکا و استرالیا در سیاتل
🔵
‌
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.1K · <a href="https://t.me/persiana_Soccer/23805" target="_blank">📅 01:19 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23804">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lGv_j1T_iXNnisShCviaVYqKNW1AgHN5WQbdyKfcYrgTmOipc5TjQVJ6kbcZM_igyH54K9oHiIQwUvhPWCAoYrC2zeAt0F9BorNIm5CNUpw7LD4sQ4P62U62-1GR7-1hX4eKmDEN6RT48TXQp-EQhDXi7l21vDahuToqtp0G63QAPDlDHEtTg7gG99cP5ziJioy6h2unaCdOTJhOlzNViIz-m2roTwIobhGcZyYBHeIk3jf4SpnKH6SoTvM9IthBjJtA_VWu2E_XFeaPSVFb3FtApqBdZvE1cQs9Xnj40jrwAzfL_D1FEjLkpoplH2aXpfC54Hz0gQ8QBomX21VKiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌‌ دیدارهای‌‌‌ دیروز؛
برتری کلمبیا با درخشش لوئیز دیاز و پیروزی‌قاطع‌یاران‌ژاکا درجدال با بوسنی
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.3K · <a href="https://t.me/persiana_Soccer/23804" target="_blank">📅 01:19 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23802">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7bad87a3f4.mp4?token=m5WskaPzanSm_PeZ5HTZ2CMgivt4jwR3qe_9JDfYddO1khaXdFKHrr63gvUbGEOCraIKkRXd_X6EGOzmPCMh7xG27dB8g_xLLzohC26F3pSLw2YdQLPp1hmqV9_GUOnImHnL8arJdXyqHHPRmpgkSwseRfdbSYBdESZbQyF2hCRNw82D0ifFxqSwfWhd_mFswRC2ZiaU3x5iUHd0AhFmXJ90Hc9-Zfl_3x_z_ExjeZFDppXesxZ8nRHOY0rK5KSlfFEb_Jl-Xn_l2rYxxsTFocCgKLO6XypEXYcxqbWqCzXaja4MjYE9Vs65xuXjGAY2e-8pRSvZnXBkrpV-T4DL6A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7bad87a3f4.mp4?token=m5WskaPzanSm_PeZ5HTZ2CMgivt4jwR3qe_9JDfYddO1khaXdFKHrr63gvUbGEOCraIKkRXd_X6EGOzmPCMh7xG27dB8g_xLLzohC26F3pSLw2YdQLPp1hmqV9_GUOnImHnL8arJdXyqHHPRmpgkSwseRfdbSYBdESZbQyF2hCRNw82D0ifFxqSwfWhd_mFswRC2ZiaU3x5iUHd0AhFmXJ90Hc9-Zfl_3x_z_ExjeZFDppXesxZ8nRHOY0rK5KSlfFEb_Jl-Xn_l2rYxxsTFocCgKLO6XypEXYcxqbWqCzXaja4MjYE9Vs65xuXjGAY2e-8pRSvZnXBkrpV-T4DL6A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚽️
آرزوی‌جالب‌خانمی ۱۰۴ ساله که‌تک‌تک جام جهانی‌ ها را دیده؛ برای تماشای لئو مسی، چهره‌ای که خیلی جوان‌پسند نیست! همه را دیدم و مسی بهترین بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/persiana_Soccer/23802" target="_blank">📅 01:06 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23801">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">📊
نتیجه دوبازی هفته‌دوم‌جام‌جهانی؛ تساوی چک و آفریقای جنوبی در گروه یک و اولین برد تیم سوئیس با آتش بازی مقابل یاران ژکو!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.4K · <a href="https://t.me/persiana_Soccer/23801" target="_blank">📅 00:52 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23799">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PesvnlNFfCpRVsZyVaJjVATP-CvR9dAca3u2qPcPQiV2d4VTcpUpTMIRAZO-FSnDR0RXfd7z9sXL9q9-NXXIzrQ2Oq94DW26VRuOd9vUXnw17iKpcANNHkKlJP7hgsBr_XvEt7GQxV1Y5KpHDTb1plwsof9qWfxkOAhGSYc8ZnOy68EUMiDJZs3IUhC9dVAcZ19_yZLVQ465xmAk3OobusXZ9iajGlImm6BQwXJLqDbm_1y4JR2ZdN9fLhEEWpex2mk1sDX0H1szjue5aq8UP_3MEuXgogFWmu7NpfIW9cO0_fw6J7Amyx-lgs669E4UtRU_BpaHD5bOBGczIO45Yg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/S3rwiXBtF6Ek42FtDB1V5kk_o2FgkT4yyBxIM7HLHIVCfGVALzxuX7fRSMn_NnZyawoFksGtu3e3bpbj9arSKjl7eO52aSjzQly2Z9KDrE380nBPjLGQ2g0TYIaQ0a44GK7pTwi4nGTG340V3VQXSvtcihem_vr1EE1RiElAhdecghNqbEx5ZmFsi06K1-p08CV-BWK-L6zNryuMMqT4UhS3V3daqY5-VJ_3Ea9BVtHZOdeGO3KaCb-rHddGLni9ihb8XS6vZeEHgHR482ygzXQeMsjolZIDNxjX8lD5SA6X5u2R06MnlIV3fN5Xqbvr6Msa8ZuDZHRKTJ1JM949rA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📊
نتیجه دوبازی هفته‌دوم‌جام‌جهانی
؛ تساوی چک و آفریقای جنوبی در گروه یک و اولین برد تیم سوئیس با آتش بازی مقابل یاران ژکو!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.1K · <a href="https://t.me/persiana_Soccer/23799" target="_blank">📅 00:33 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23798">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qlcelT-g190CRsxqAS_XLFuyRMORZA8_YCQtw6BMbHxnucZ3xf4VQglX5VZGnM8P-BQUs5EcHaQjp3TMCAN8eUYwIOTfY-_sibf_p1YHaUTi6rhnocn-mXBbDA8fSkvY8HyP1jrGbtLynuFTVhhcAFu8avbevOMCQRdHZpwCSigkQor64PdmK957XcWzTrcQBCJE9t-UbS2IXm2FTZ7veYfIIBHFVKE2tz4erSxMh1qAxSf9PSJxBNN9595Pgid8o50NZEp0dgBBtNntOJMLTeQsS19EL5uYL38DgA_2OuwX0I4cm8a_7BaRQdmIfW3r1NpNGRO_L6ax5Qjt43iYZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">▶️
یادی‌کنیم‌از شبی که ایرانِ مدل کارلوس کی‌روش به این شکل تیم ملی مراکش رو شکست داد. شبی که تموم مردم ایران دوست داشتن ایران در جام جهانی 2018 روسیه موفق شه و از گروهش صعود کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.1K · <a href="https://t.me/persiana_Soccer/23798" target="_blank">📅 00:25 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23797">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/my_uwEai0cpmW_MxZ7-D6N2SB4nvYQrf7YL-yPt_A8xjylFJGm5x6AlCRyVbfHO8XRGZ6aUz69IP44AgnRefi9-d87WgM0JypgQ-arJOlVpL3SfOurhYz-AC0XvDH279d4DeaTuicK9JEUpyIL8I0JS1qXdfR1KLHBjapEHbd4p6LnYqceHSxBKVu3QF0fC8KpLJboEcTW7znWf2ATPVJPdCgZqQpSlXz8sgsiwMWQK5IGjGsYFQsXqQj0wi2FyyT-7OF9taoV3Axqw2iRUfSZcYijQGzWF3qkHRnh5BW9o010Nd2kCT6HwI0H27ojzOgxnjp6TCS1VQzly8VHyhYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
#تکمیلی؛سیدحسین حسینی دروازه‌بان 33 ساله سپاهان که پارسال قراردادی دوساله امضا کرد باشگاه به مدیربرنامه‌ هایش اعلام کرده درصورتیکه باشگاهی او رو بخواهد با دریافت 10 میلیارد تومان رضایت‌نامه‌اش رو صادرخواهدکرد. قرارداد حسینی با سپاهان برای فصل جدید 140 میلیارد…</div>
<div class="tg-footer">👁️ 41.2K · <a href="https://t.me/persiana_Soccer/23797" target="_blank">📅 00:15 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23796">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VQi4fzsQjBWSUbQasUl0BADV9lXlqqCC6pVraB4FbmHNF3F1OR7mccT3lFge11UCY_eIOEVPRdpL0AHPM3TRIVWx3gT0jwqodqhj9ojk_u8r0HhF27WvtmkZLZYFVnwf5w_8qIPRQswMgzFZiAEaVQHOGJFM2qHwOBVEkWP3-IVBfshQGIBMoHMfSf-fNLXqWPqN9OQeBrZhSHjOzF4k7DfuITFmDVZBu24TtE-C4BEQswePszg5AxsUFvpvFtCsN0bRIxJRTeK3HlIDcVJ6cFurV86cr8t0gHdPwXPFQgiXtD3Br8BaMrYNCgvQFmn_U9Hh6bA9kargVUdT8G5QJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇫🇷
🇫🇷
خوزه فلیکس دیاز: بعداز توافق شخصی فلورنتینو پرز با انزو فرناندز؛ کاماوینگا و شوامنی دو گزینه پرز برای جدایی‌از رئال مادریده. شانس جدایی کاماوینگا بیشتراز شوامنی است. درباره فده والورده پرز گفته او فروشی نیس بهش هم فکر کنید.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.4K · <a href="https://t.me/persiana_Soccer/23796" target="_blank">📅 23:46 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23794">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RRvl_94ZC_XerG7pDEN09BUoUiMQcqJGdM1zjhXL2pSUJ7KJMYyJI5MusZaHLX3HFoxBOFKpdrlxysHj-7Ys_3RHSBXcBSgmrsRrYjlFri1SyEgqCnB3fmBfF-a3Kw29GDisMSiGi3r70PAVUPU3VVc66FBGvU5-uuXnFLI53p3yRWjxP5gTpik6lUyasOgEJsafV1Fg2l00L5L_25AOTyM1ZFxiu1dg9W6_T_lqCIrxiWc3TWRso1I6KbTHLTADexBy9bRKwzOzR-yfAqoNG_mEBJ8-lr-s6ovPdcoIgi_8QKNVkqy5-XsBgUl8Y9YZOhW9TPXY7qrRRhXbFVbXmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bLdYRZAP7XKXw8goTCQUkMDdH53N6aLmheaHoGPTjpne3JspJ6Jkq212-WewpvWmkKtjxsMESNJeKuWIyANUAhkhoBpvdW9_wyuHCzAm0X-e__8FQHyVEwwWPQbsKF3pUl5qjWckNJC63cI1tN4UlaN6Pbym8DeLFpB8hDdgD2f6aa7gEFJUtFT9eyuDiPm7NJdLz2Zb70tlCxi8jRKY1BPEUs_J1QWItEFbmOcluJ11YZqlq_-2ST5VqjlAR7KpjIc-tlPegKG8WCal89JIw780cusPaGRkx5_Ne--FYZUhwe8_2jd6nN4EdhpzeIUQEXmZMNmMw389e0XkWJG2nQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">⚽️
👤
ویدیویی زیبا از شاهکار فوق العاده علیرضا فغانی دربازی‌ شب‌گذشته فرانسه مقابل سنگالی‌ها؛ همین‌عملکرد درخشانش‌دربازی دیشب که دو تصمیم فوق العاده گرفته ممکنه باعث بشه که از همین حالا بعنوان داور فینال جام جهانی انتخاب شده باشه.
‼️
دو تصمیم مهم فغانی این بود:…</div>
<div class="tg-footer">👁️ 42.5K · <a href="https://t.me/persiana_Soccer/23794" target="_blank">📅 23:38 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23793">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IspuNaJmplozTQw_S-0BNOoiHSiXXeM6QcTlxb4sXI-p2uMdW8MhAI406UiDuO9jzgip_--oXeLGgZhIQXv4djgK7aqwa6NYs0H1OOdtGF_H88LJOsWhZ9qmeHxaiwMcWPwpwiH9OnaGPj8RWOLFrHSE92oYuO3AEBkZcBaW28OdL5VhoNjFn3hAPEjW311O2MjT6p4e0kRTFzfja9P_LvrlHsU_KGsh3sv6zQOpHr2u3OToTOoQLfYzFPzXiu4VPq6_OQ8lmsxr9tF0UAkDJMueSbq9ueByOysNeOJykKxjzDmuyER1u66x7r0Y8Kjmi1y8O7Y07Y7uPQqL8Qu0jw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
با جدایی ریکاردو ساپینتو از تیم استقلال؛ رامین رضاییان کاپیتان دوم آبی‌ ها در پایان فصل به جمع بازیکنان‌این‌تیم بازخواهد گشت. رامین رضاییان پیش از رفتن به فولاد قرار داد خود را با استقلال به مدت 1+1 فصل تمدیدکرده‌بود. همچنین وریا غفوری نیز بزودی زود از کادر…</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/persiana_Soccer/23793" target="_blank">📅 23:21 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23792">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a4f7a0d943.mp4?token=bpxlf0FV3wXr1t44nCPTEc2VQKxY7I1DUECIvcAWZ3ac9jQdEye4_tTuVMYVeOJdxDTgF-EWjLvdSkDZQpmyaBjSFe1jhAuPZskY-3RrDgGF-TVPtbuGn_WRqLoUH9puujoIvqucSc8WcZhHESa9MFlBhQxQqAVSxfMMR8nRwEbRqePcfdM3WI-VzzYvX5HtJAiSsSI-ycU-3LIZBxvNpSvFFqAvJXv0qDU05hmMLN7VaWYs_8F9q_9A4PmquckT1n56A3gkXhyki5UEinpqLxfpecLWUSgdnrsnWlpM5JgebSXZGlF4G8u_em15sbn-X82l7gX8YDgY00A_Fe3XghhwfbXMnXoxIHbq-txuXflM9vrkDVK4TorSb5GRIZ3x6-7hUNdmOg4FtrBn-v7HfG1qyaQVZ0XindwNi47QjyvN_wcxsMq0IpUY0cGfId5hhlH6Qu88tZtLeNITlPGHiGb07SZDm9gZJV6C-TUH2YLD8y6Iza4K0FTc4ux1PcqWqIar3auGtNsS1urqFhCUO5NKLupc-tiZgRjkTqbmIsc3OsDEryz53BMX_Nu8v9Hh2uRyVJBApLAHd-_sK-OaCBP9TIyrGuyJDZFfH7X8vKkV_CmH_pRgwsyc74K9LEDIC-0Ogo60wKvTAIe0_kZm5_PP3MtZzr9gmpR1uhdALk8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a4f7a0d943.mp4?token=bpxlf0FV3wXr1t44nCPTEc2VQKxY7I1DUECIvcAWZ3ac9jQdEye4_tTuVMYVeOJdxDTgF-EWjLvdSkDZQpmyaBjSFe1jhAuPZskY-3RrDgGF-TVPtbuGn_WRqLoUH9puujoIvqucSc8WcZhHESa9MFlBhQxQqAVSxfMMR8nRwEbRqePcfdM3WI-VzzYvX5HtJAiSsSI-ycU-3LIZBxvNpSvFFqAvJXv0qDU05hmMLN7VaWYs_8F9q_9A4PmquckT1n56A3gkXhyki5UEinpqLxfpecLWUSgdnrsnWlpM5JgebSXZGlF4G8u_em15sbn-X82l7gX8YDgY00A_Fe3XghhwfbXMnXoxIHbq-txuXflM9vrkDVK4TorSb5GRIZ3x6-7hUNdmOg4FtrBn-v7HfG1qyaQVZ0XindwNi47QjyvN_wcxsMq0IpUY0cGfId5hhlH6Qu88tZtLeNITlPGHiGb07SZDm9gZJV6C-TUH2YLD8y6Iza4K0FTc4ux1PcqWqIar3auGtNsS1urqFhCUO5NKLupc-tiZgRjkTqbmIsc3OsDEryz53BMX_Nu8v9Hh2uRyVJBApLAHd-_sK-OaCBP9TIyrGuyJDZFfH7X8vKkV_CmH_pRgwsyc74K9LEDIC-0Ogo60wKvTAIe0_kZm5_PP3MtZzr9gmpR1uhdALk8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
خاطره‌بامزه‌حنیف‌عمران‌زاده‌مدافع‌سابق استقلال از کتک خوردن مقابل بی‌آزار تهرانی؛ حتما ببینید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.1K · <a href="https://t.me/persiana_Soccer/23792" target="_blank">📅 23:11 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23791">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/euKV-9L6vDL4pEJodRNadTaNZgwPwFkUeq574tukLkIGOrJ9KfB-aiGwRut8V4MRsdLPfRn2JhdOwJ9byiMZIQioL0IIdDX-6ftkXiCJmQ6EoYLjgZHJqKJTK0WPEKt96rljmZrFrRqBzAiEoKbtpvlqbdOw_1BcXIMzguIVnrG5LVMueBJuFFXGbvDtL5FC-lLxeQ1dEIBFM8v8KUN5CwZ3kVwMHhkNTwJQ2uFhufIk4sduR4B76hh7EsceHhdufmA4EqwA36hiJhsrlrDUZEgcocZMoYJUjXNQutgIn8myVEdhAUzSkVUD81FSiJmxMeL0uk59HGhDdPHJLqJeBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛طبق‌اخباردریافتی‌رسانه پرشیانا؛ مهدی لیموچی از طریق مدیر برنامه خود به باشگاه پرسپولیس اعلام کرده درصورتیکه رضایت نامه این بازیکن رو از طلایی‌پوشان‌زاینده‌رود بگیرند مشکلی برای عقد قرارداد با سرخپوشان نخواهد داشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/persiana_Soccer/23791" target="_blank">📅 23:11 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23790">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBetegram</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/js5yFKBokVW1_48X-6p-WynXxqwhPiaz6qa66hPr2LobLzuci197qMWlAY8h7bbHrY_vCoX241ar8eJKoT-e_ybSjmYgkhFxlnTqYUci7YkizzB0pwoRwRPooIcq8HquCU-iXBSoBxNo4N1GKI46HEpYASZVX1SG80KLgJl1N3Ob_n6MJ3Orw9pOnYTJyjyC5RFneWSKeBO7qn0C7bMXJznIdoIBXsNj0-D164IUaDEsJB9UMWoieDbpcRn4VTVkhaXqLgVfwfj848twxROdxGslJ84OZ45QwKFGYiZYdUQ5BAq3ehatU32_AVoN1zmgdxylLq1PbCZ5P5cT2gHlxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
بزرگ‌ترین تورنمنت فوتبال جهان آغاز شده…
📺
پخش آنلاین و بدون سانسور مسابقات منتخب جام جهانی
در کانال تلگرام Betegram
🎁
شرط رایگان ورزشی
🚀
100% بونوس
⚽
هر گل، هر لحظه و هر شگفتی را از دست ندهید.
امشب میلیون‌ها نفر مسابقه را تماشا می‌کنند…
تو هم به جمع آن‌ها بپیوند.
🌍
http://betegram.com/affiliates?btag=3_l7</div>
<div class="tg-footer">👁️ 41.2K · <a href="https://t.me/persiana_Soccer/23790" target="_blank">📅 23:11 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23789">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mW4YEbzRQalcalJc5cVe8Hgeydd-OLlf1qCri3PDnBpTlz4SbUvqEabZKZ-0nPp4cWodohG27DRmarVvalnvAvvEtuKA-fQaVRvVRpNXaGux23MGEBEAcwoPdwnXeztSDae36zdZMWmNkMUYN1OMdiqWs-aEU4F0v7OXIYByJR1EzuXd9L01oxPHpGLVm6xTupBqPk1eUkdq8z9f17VEWvFdzWbGkzE57FsZ1rtL3d-417E4Pq-2l4FzZ4FscEqXg-81p7xN6yb9-rhuIIyhJ0hd1iNTzTgKQ3MqljWCMeeL_OX0Oxe0LH6sJXVzP2wRrU96_97lN-t4UizbPv8Wdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
همانطور که حدود سه هفته پیش خبر از علاقه اوسمارویرا به‌محمدامین حزباوی مدافع میانی سپاهان دادیم ظهرامروز باشگاه پرسپولیس با ارسال نامه‌ای رسما خواستار جذب این مدافع تیم امید شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.5K · <a href="https://t.me/persiana_Soccer/23789" target="_blank">📅 22:45 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23788">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M7vZZSIffoAbWhsE-ZngLr9BBEjjogLGv_EGauJxFAGiXikNAdeZkVOd7TELqcJxtuc02SFnXky7Y35LzH0rLfTLpQ6eF6kYYKyvifTYF3TyYyH45HmzvwbBLXVuFywXEjJ2kXUOr2Vc890QrB33-uDEHMOsrxthxbI2DK8C1E88d5QMOmaF3x6AS5hfyul12awyralnBsi5-7_uTZ-Vlwd8RXZQernZas731PbLdpOvDBfnPx5Ny04olKPKYBNLIRpFwwcDSs8YZqmBfLSSAts3FV2N_DgqvtwUdTjw9llEnaHfeh1Oivd3fIv7Rnt1_2_a9X4gqvhqmgePWUkIEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
مزدتموم‌تلاش‌های یک‌سال اخیرش رو گرفت؛ با اعلام از فیفا: رامین رضاییان بازیکن تیم ملی ایران با نمره ۸.۲۳ بعنوان‌خلاق‌ترین بازیکنِ دور نخست مرحله گروهی رقابت های جام جهانی 2026 انتخاب شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.8K · <a href="https://t.me/persiana_Soccer/23788" target="_blank">📅 22:33 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23787">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cGjYzWlyATvvZZs4ABvu0SA375pelRYoLjsOiQPiv8s76Z5AVuDeChfHIfERQbPlEAX7X_rt0pzLsFZ3qRUrHRvzivb2zMw2LDInFXSFIKwP16kyQcmrJKMz7twfjNOGU-8qU_hJNIZNM5hR9cPTapbC4wAF2Fyl8yQFZQdJ7UtjQM56Qlrb2VoGokhvwrsgX_VB7lqmcgNHANNYhcenrtrmtgKqdbqqfmdSqc2zzBGPpkUC4xZ9Rfr86AYLO1BmG372bUY-ASc3bKDOCgUKVdwJGdqPD_B4D_GK-XHXAYjcgVI2IASvxJnMAxKFalRhuFT2NKv2fg4fqV17m4dhqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
سانتر خط‌ کشی‌ شده رامین رضاییان ستاره استقلال در بازی بامداد امروز ایران مقابل نیوزیلند؛ خیلی باید روحیه‌جنگندگی داشته باشی که با وجود یک‌فصل‌درخشان دراستقلال به تیم‌ملی دعوت نشی و سکوت کنی و فصل‌بعد با اومدن ریکاردو ساپینتو نیمکت نشین بشی و بازم سکوت کنی…</div>
<div class="tg-footer">👁️ 42.3K · <a href="https://t.me/persiana_Soccer/23787" target="_blank">📅 22:31 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23786">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ef4d39f268.mp4?token=ciYDMSiv2zR1tVCvyGSg9bkEHNiQWmyu3mRUJ4Aam_XnwaJP_6au0TWPTWxTWMvWQ7PJVpd8Xoi4T_VCIFGEzGGF7po_I2z07JoRz_bUfDh7cFlWAt25efwrDvphLRbr5OEAOhM-jyssyOcGqUC2bj77wZV8D3nTzpZv5DVqxgG5rBJXyxmYTboaGG0H5Z9ihssZ1aFxCWrwf3d6SxuTs6Kqi0CyRLHKR433SSRi2wHQcr6QkaPirbJ-I3kXOCb14WCFw-PWjy_Cs8ndq_exVBMnV9lsFELxsQ8y_zNVOxjNip_lRl_rzr-rAyuYuApJQlkS9ofaA9sZUFzSkB_WNg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ef4d39f268.mp4?token=ciYDMSiv2zR1tVCvyGSg9bkEHNiQWmyu3mRUJ4Aam_XnwaJP_6au0TWPTWxTWMvWQ7PJVpd8Xoi4T_VCIFGEzGGF7po_I2z07JoRz_bUfDh7cFlWAt25efwrDvphLRbr5OEAOhM-jyssyOcGqUC2bj77wZV8D3nTzpZv5DVqxgG5rBJXyxmYTboaGG0H5Z9ihssZ1aFxCWrwf3d6SxuTs6Kqi0CyRLHKR433SSRi2wHQcr6QkaPirbJ-I3kXOCb14WCFw-PWjy_Cs8ndq_exVBMnV9lsFELxsQ8y_zNVOxjNip_lRl_rzr-rAyuYuApJQlkS9ofaA9sZUFzSkB_WNg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
روایت‌جالب‌ابوطالب از گلر40ساله کیپ‌ورد؛
به تموم دخترایی‌که‌پیجش‌روفالو کردند درجا بک داده!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/persiana_Soccer/23786" target="_blank">📅 21:55 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23785">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UiMtZ7miuCWm3mhS_28Hv66xLKEGBg7ckTw8CHxAGrhgbA04pTfrYK78wOSUN2bjsegi1RH5Zv5RPIq0NsmPisDD_HAwpvVFBmEUIjlFba78IGj9oStC_Yoc3lWK7UxxBemykaHaKqhwE1xS8iQd5y_CRS6X_baWfx-PuqvW0iDll9QqsOtaRyjLmPGAj7SGmZEPX6Fzb0XHzITzGHbz7WMAFzj9mfIXMXgfJevPSUFd-271KbZ7MuxjKk6r05iJQFJtDMK5PZZPRY1Hd_zeGlinY_gGCdvO_kUWMysMSCk4xz9q6bggr7pShLAh349lnEwRP1zXYSb49rx1__0qnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
بااعلام باشگاه لخ‌ پوزنان؛ اللهیار صیادمنش در تست‌های پزشکی این تیم حاضر شده و در آستانه امضای قرارداد است.  او پس از علی قلی‌زاده دومین ایرانی باشگاه لهستانی لخ‌پوزنان خواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/persiana_Soccer/23785" target="_blank">📅 21:48 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23784">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eSCKQA-QCXMTPbHeHSkyM3etwJ_Ma7AXRRIGvRQSZWtm2eN68UJhdjtgX64YUPchFcBW6_UiV9AMxnmv9IqRjuvnrSJ489PGKTW3V9V0JjBQuNhRn-jAY3PuhraKhmTQB0nM9oZSvwMfP68lrf3pArgF9SObEIO2yC7a3GSd_sUKc7QTLevYClx5czrHYMQSrkVmn_NwTz5jenMt2PrDJnOELOCR-EladxL-153qh2p_3uN62f5S35Kb6-OV1gmTrGpKMHXKgdV9rE1YOIgb9If1G7MTApimy7yHfMEP3Vd2U3SCJVIvUHDOlln1hhggLrHKZTIOFeo36SBJ_zWkBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#لژیونرها؛ پیروزی ارزشمند 2 بر 1 لخ پوزنان مقابل کرونا کیلچه در لیگ لهستانی با گلزنی قلی زاده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/persiana_Soccer/23784" target="_blank">📅 21:36 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23783">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dJgTwuqFhM3B6XbNy2jicZGqQONP6wK9CKJqsCsj8mtJ1FlJmm4JeD0apgORyVEIjLC26zSbAumJR2rGzgkGPQ_Z7D5nnv_A43pECHy40j7w44_aeBwCjwQ3qUockNGwgCG51hdj6jeQUMbERaShmPYGFmh5Ej-n6CUICjxhunQAaXGGSLPJF7XS_iA_k6wyJ2N1TjQdoZZfUoLYNIo45JFjGCJy8cpEcrK9O8cFEh9G0qMtXMTrv-bo1NUHWCU8Ex3J-yKkroR-3o37viezh_FIvqT0u8S8P834a_-K7q7tm-h1LGBH2xnCNulyB7NYnQsIMFmJAtAYkYXNDUcRAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
ارزش‌طلای‌موجود درکاپ‌قهرمانی جام جهانی از سال ١٩٧۴ تاکنون‌تقریبا ٢٩ برابر شده. البته این ارزش دلاریش‌بوده.ارزش‌ریالی‌بیش از ۶٧٠ هزار برابر شده!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.8K · <a href="https://t.me/persiana_Soccer/23783" target="_blank">📅 21:25 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23782">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fSeoEXCOW4DMF_CgfbIVSt7Ihd3ts0LJ2NYdPFnhvHi1mFlFkwV4YCVefYwWVwjcoHsjQQANIM6qJZjxpwsUA2F6mjzwls7w-Vk9aelVuT5gbURHbZN3iRUsGsqnRnel0XZB9WYE7P36bcNkn10xcOhCHAXOyNTqQaVRnnvTaIDvwAVeWMoQJRgFL-d3S1OWbXifZLTlZ-rLT9c68Pz2aVknhPOa_IxItQSXgDfz9gWWsdsnh6sGfrc1o8Nuet_6po-adwyjMM0AqB5grqPlD7tFxl8YTK3MYVXs_FRLI8gXHchF15mXIm0eWELM2z1mrOlAdaQUqI0SRKttEYLFMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
طبق اخبار دریافتی رسانه پرشیانا؛ جلسه مهم امروز پیمان‌حدادی‌مدیرعامل‌باشگاه پرسپولیس و اوسمار ویرا دقایقی‌قبل به پایان رسید و باتوجه به اینکه مالکان این‌باشگاه با درگان اسکوچیچ به توافق رسیده‌اند به احتمال بسیار زیاد با اوسمار ویرا قطع همکاری خواهند کرد…</div>
<div class="tg-footer">👁️ 44.6K · <a href="https://t.me/persiana_Soccer/23782" target="_blank">📅 21:05 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23781">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">⚽️
👤
ویدیوکامل‌ویژه برنامه امشب عادل فردوسی پور برای رقابت های جام جهانی با حضور مازیار زارع سرمربی جوان و موفق باشگاه ملوان انزلی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/persiana_Soccer/23781" target="_blank">📅 20:58 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23780">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mqzL8JPZ7NQtR4j99eS7Ue_amb59vRYgwYO-dpznjwQZciOtAqnUVn0sQJTkzYcokrd4NdYYnR3txAeXQFkSWQrETmczInFYlgBFWy83xI-qLtg44Kub4rH6C_uLubwxthz0s3k7gBzP-FhQTFzhuq0iKTkmXr5ltqfjwGDVBMw9ss5ACN8i5I9F4DKo1bSDl1w-0uykKsYoBd5GXbcymf6Ko1JNwsfcXIl_qXpS3gkVMHVRBn7nLuXeklQZUxd0nNAvY21XP0n8JVzDfgCEhajQ8LoCmZ4P72ji28WASrCpG92DZRYuAlUEY9djCNZAGqr4bQYUqA9daevAPFIqYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
#فوری #اختصاصی_پرشیانا؛پیرو اخبار روزهای اخیر پرشیانا؛ فیفا روزهای‌آینده پنجره نقل و انتقالات تابستانی‌باشگاه‌استقلال بزودی باز خواهدکرد و آبی‌ها قادر خواهندبود تا بازیکنان مدنظر خود را جذب کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.4K · <a href="https://t.me/persiana_Soccer/23780" target="_blank">📅 20:44 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23779">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/okL6IhEzKQqqtfstl4C30zrXq3MezdvldRuKyl3Pl_hNxSm8BjmhnlpK6Bet_4DrABWXiUdCtFB_bqg-PleaXibaW1jAXmlCyc4dLbUZQF4EP45fSAf5JiWlNRbiwnD4dzvgrl0B-sM-LQshVIefY2PJTnRvBx9qrqxptTbH7aLFLiCVRLTty1h28rCCRaRs3gVrapEp3g60caRbuCEU5vJhL218SGQTTqrmaAu3dsEQ5n_fbtqBqWJiVhKh7nKn_RG7jp9N6ePEc9BdyHB5cYqKcBEBnKQFptReFMPmdweKJlm1_7b5NCXzHTI9kkMsZV2CO0aBTVUODvB_Y1B9CQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
هفته‌اول جام جهانی 2026؛ پیروزی ارزشمند و شیرین‌شاگردان توخل مقابل کروات‌ها درگام نخست.
🏴󠁧󠁢󠁥󠁮󠁧󠁿
انگلیس
4️⃣
-
2️⃣
کرواسی
🇭🇷
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.6K · <a href="https://t.me/persiana_Soccer/23779" target="_blank">📅 20:38 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23778">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Kf3tx9pktCU5EvKLDUNhVPeNhnWxQKgLfkZs_jkdJK_n5-321Ix4WSk1x5kWFiq8SWshfAqvBdml3WNW5CZMKwjxjrg68yU3OclvhDJAsguQrok98NfZiBICJQ0pix0sNY5gWtUnXH1zUKOhZf7zH3LpM-h-aeYte57Wy9Q7xBeLVVUfaN1m4eCopYwqrorP0uw3e911ByBZSc0Jp38mbrnrFXjR8LSM7loBdXRT9bwOWVK6nwM6Lq76dyE4O7_JXiaxQYfKrhLFWbsO9r6Q1U71x6H6AlkdP9P2lHKb6s-bHYl0llpBrOqGv8g_E-sdVzKLO0R2_QT8-M1WQoQ6Zg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
#تکمیلی؛ ژوزه مورینیو برای‌فصل‌آینده رقابت‌ها مندی و فران گارسیا رو در لیست مازاد رئال مادرید قرار داده و قصد داره که در فصل اینده از ریکاردو کالافیوری ایتالیایی و آلوارو کارراس استفاده کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.3K · <a href="https://t.me/persiana_Soccer/23778" target="_blank">📅 20:38 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23776">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R4nrKQXTQnS3pPwHGyddFG1ZUi4CH_XLCVON7X0P2FZJtTTtNAS9xiFNnFPhP-hxF9nBMffLwi6wQdx4Ehw9KgZDzMdl8HT8TPAjClibCPpR_Nn8WlEczTudwl4uDCnFGLwvvx_MSfWlsVdEG8jRAgR3grSF7fidax6HkzuM4pGVsVTH5c33yehRuC-HFtVWGEby6A85NZRKi_uBJ6ZWjR9VbRgCnMThjZo3mZHIj3q9N7A5BCWrTN8Lg7hLjFKFXw4WIvXbJd-vcaCXuDhAiMxoZaNsFdfWwb3wMmnpLD3kqRgubr5RsiANBOkwRPpP63CLEnKIJTDuEv3BTJ9cug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
باشگاه پرسپولیس برای‌فسخ قرارداد توافقی با اوسمار ویرا برزیلی به توافق‌برسند سریعا با دراگان اسکوچیچ قراردادی دو ساله امضا خواهند کرد.
‼️
مدیریت تیم استقلال در ابتدا مذاکراتی با دراگان اسکوچیچ داشت اما عزم‌ علی‌تاجرنیا برای اوردن این سرمربی کروات صدرصدی…</div>
<div class="tg-footer">👁️ 43.7K · <a href="https://t.me/persiana_Soccer/23776" target="_blank">📅 20:23 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23775">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ceb72d8ebf.mp4?token=IB6CERunkw1XVi4y2E6TW2XH5DeCRpdjRV950Rmkfj7LypAaDSTBgQfDJ-B0GtDX0aoEo9x6qTl8FiN8QflboeMeuNRVP9NEw_9f68iUUJHbrYDNBDPCBMXBep7IUxsBDBWNnDijU0vIn5YjZVYWnPTjA-KErp9aBpWUU6eDH5djH5s_qUbNCZ5CGUeKgfMhuJ3VPMh4KHAU6vb6FCFpVhWfhVZ4-Sv_sa-FLw5tBpgdFPl0ccGL3DgTZUfNTlWR7S19CjCSzjLDY_W_SKxwku0QWKev0s8ge65OzEhj54zF-yBnJo1_u_Hz55bEEIAMSc-ChhxM6SxvOYt8bDzEJQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ceb72d8ebf.mp4?token=IB6CERunkw1XVi4y2E6TW2XH5DeCRpdjRV950Rmkfj7LypAaDSTBgQfDJ-B0GtDX0aoEo9x6qTl8FiN8QflboeMeuNRVP9NEw_9f68iUUJHbrYDNBDPCBMXBep7IUxsBDBWNnDijU0vIn5YjZVYWnPTjA-KErp9aBpWUU6eDH5djH5s_qUbNCZ5CGUeKgfMhuJ3VPMh4KHAU6vb6FCFpVhWfhVZ4-Sv_sa-FLw5tBpgdFPl0ccGL3DgTZUfNTlWR7S19CjCSzjLDY_W_SKxwku0QWKev0s8ge65OzEhj54zF-yBnJo1_u_Hz55bEEIAMSc-ChhxM6SxvOYt8bDzEJQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
هنگ‌کردن‌خداداد‌عزیزی‌از رفتار جواد خیابانی؛ از خداداد سوال میپرسه بعد میگه تو نگو تا خودم بگم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.6K · <a href="https://t.me/persiana_Soccer/23775" target="_blank">📅 19:45 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23774">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dVbvmUk4BuZBUO2lE7wIKJXJ7jw4cE9wZKf0RTs1A-ic2idWufRDDi5BYsGf6lrZ_UYDG4T55MD9c1s-gN7qk5XERNyqbk_8I3kTiYa0TaZGIL7xoci-wfEibFMBXDJLo9dNBEbuJYqqUxYImCSh1eWFsk-7-NKW_f4bdbUthK35-DvMYy2HBwwTg_6of_BSRX9eeUEIvUqCrOq4Vm1rxMX1ZvwaimRtzMLvccpnPTNgneqwqrhIENTPdOa-bbtFhGI0Ar1bqevOL9NxpblUMNscW8HqECSx_33Fi4_HnAGgTJNh46FFZStFUcIl28L_IejY2-KEXFuL82wlfEv-Rw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مارکا درخبری‌فوری: باشگاه رئال‌مادرید میخواد بزودی پیشنهاد220میلیون‌یورویی برای جذب مایکل اولیسه برای بایرن مونیخ بفرسته. با جذب اولیسه و انزو فرناندز پرونده کهکشانی‌ها بسته میشه.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.8K · <a href="https://t.me/persiana_Soccer/23774" target="_blank">📅 19:19 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23773">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n15l-U_3vSKH-RWfyJTvoCWJkE54EqsJV2YC-gkeDpGVgPqH9-6NZr0IZHw5a0TKtLpwRHQM3ih_DX9HUobbmKx1ZqwfYPWC5cZhfSiwusOJlBPYyO-bzzxULwBoJIPwyd8GAulN55Pku8-ocUOAxAMmClbWQxRHDG1jXW5MocKkRCavfH15utwztWiskhNWipyW-SWXUcgwIMf37RESW1XWTdmCb5OZmQYf8XelNgkv0EYRaAb8loPwlKmDnWtSyqFrvloANREUWqEFuOiFRyKWCR5RPzCXj015IUi1YrG8hhS0ahnJMtWB8xFJUwrr9d0kcVsj2_oD3YmqGh0h_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🟡
با‌اعلام‌باشگاه‌سپاهان‌اصفهان؛ آرش رضاوند و میلاد ذکی پور قراردادشون رو با این باشگاه تمدید کردند اما محمد دانشگر حاضر نشد به باشگاه تخفیف بده و جدا شد. رقم قرارداد دانشگر برای فصل جدید 170 میلیارد تومان ناقابل بود که کم نکرد ازش.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.5K · <a href="https://t.me/persiana_Soccer/23773" target="_blank">📅 19:06 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23772">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SKJmvnNTHNQBZsghNbKDWgKpnfit4upOnteVo4CymOVicCPlWCp0rQN_yTMSpVoPXCOxNbNKJO--7YvWpYECQzYf7_GzGRZhcvNPmgoCSqIimcuLMFtOL9jZ-jUO9VgamxfvYFcdkr4PApOu2KU7hhDpdX0ERaynoqUI2DtLr3Phjj6IfXpm3xN-9kB-XviuoQ6TXBO_E_3gRcLCcBhHguzoflfip1st8TLuC3Tg3rHkwPZOHeqYGuuQx1zNivVR9FgM34eKh03GCp-C4SeXHQaBxptfSfaV3IW5ZtRJQU7J83_48bDUNRwJhLlLF3O33RYgDat49GF7Hbczy2L5Hw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇧🇷
👤
برخلاف‌ صحبت‌های کادرپزشکی تیم ملی برزیل؛بااعلام‌‌کارلو آنجلوتی؛ نیمار جونیور فوق ستاره سلسائو دیدار حساس برابر مراکش رو از دست داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.1K · <a href="https://t.me/persiana_Soccer/23772" target="_blank">📅 18:52 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23771">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CHf4Aoy3nZYKkLjz6NiT7FNiUU7xAEf8mUHj3j-Lw0N0jxLEZ2hxNco0nZYeXtgzzSvFlpG6UvSl8Ql7g55hEMDGmSVXfzEJfDm4epeICBjvgzoGDc0BQrBpkVPzEPNU-4Z9_wRgi7TyM4AyhHLY6NoDOWeAJ-cV2GJy8bGsEFJnUKGNCKA3hnWICU0vLENzS5oWqK-zuGPWzfc1b1oQdOlFArJvk1YMHo5j2Fdoc_qxhSaOD107SSAxaGS9yBYulQbvVWvumw9jL5eu4tdmJAOVMxkEA1gVwSg4xAp-aaWoae--tK1layTPCucVrkpu_dvfe6yJAH9F1oqiSVTzPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
فابریزیو رومانو: ماتئوس فرناندز ستاره پرتغالی وستهم؛ منچستریونایتد رو به رئال ترجیج داده و به ژوزه مورینیو اعلام کرده که نمیتونه بیاد اسپانیا.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.6K · <a href="https://t.me/persiana_Soccer/23771" target="_blank">📅 18:47 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23770">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Wl4zdCuI-Lb-g2YSuvSQ8GtWWtfuSEAAt84kmlPLESnyONhoZWwLf1TSxsO7WT1r2xhTDFKlgvw5PPla7S569f5lVrhdigkPmL1ab5F0bKybvmKalHCmh5eqapveCVay8Fj5J-a4MJuH0RUAWA2rqbWTHsAEOPuww0gHq2E5EcDjWaiJOgBkFjJNV-zCHe-4pM24HuB_lyvhzDSqzjr4y9mvAIxiORU8tMXEiSTdAvay6Nl6Lo1vLS7Rx0YqNub76zdmz15oqzSZeMoyGw2nKAqE7y_38uiU6XabSPcWxCSYUS9vMTYsKH-racNwJjp2xWpKxtx6vfuha00L8dhmAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مارکا درخبری‌فوری: باشگاه رئال‌مادرید میخواد بزودی پیشنهاد220میلیون‌یورویی برای جذب مایکل اولیسه برای بایرن مونیخ بفرسته. با جذب اولیسه و انزو فرناندز پرونده کهکشانی‌ها بسته میشه.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.2K · <a href="https://t.me/persiana_Soccer/23770" target="_blank">📅 18:15 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23769">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o03nm1bKaTDPED9m_B6IlmXg8AngadIBaNV9ot-kx3tWnbXIvjsiUUqXYTJkI5rQFY9u-GPuPCaVourUabo3B9Y9Tqu4WnMUGMhMTCH81NN-KxzXS63HQHzM8poMcFp7Mo2-uN7kbICmL0-cPV13SMktmbp7u8msoBL9S2qW_H5Xk5zZBZ_1EjguOxTn2TmNy70qILFIKm6qa2Z-rx18v7TBLAV7IEvlXlqR8LeoRVE_CxQqJ8qaA-zXrg57LXKqfhk3V5KdFxPEuPgiywjOURF83Eigts22mFfKhqBjMMUA63nsTgXk74QXBHaEO-qZdwxc0HPJ_lSv2edcTME_Iw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
#اصلاحیه؛ برنامه هفته‌دوم‌جام‌جهانی 2026؛ بازی ایران
🆚
بلژیک ساعت 22:30 برگزار میشود.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/persiana_Soccer/23769" target="_blank">📅 18:00 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23768">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/629abdf2a4.mp4?token=rWuxy_q2UsauDRd_Ah0PIIuXL0vTOMrQ0hVHAvjY-EIvwf-Al8Z2MEZaFBOsWksArqU77EtdWilLF3wlBpl3ZNFGQY_MlBb16UFpYcBcTgycgy-oB0KvmUzvfabOygwwT-vxgMHD2aE4-pHIilXhygFLVkDQDsYeeXdoBT2MvEzREX53U-ghyfFKS4xKzFwZR_HGjahDy8mZkxLywqWS-t86srOZYyo1MpnYNiw30L8ZGiXLmTN9Tth25pfCtiPFZtloqKa_b_un95yRLA1doHxJhALQEjTbijwNDCVNH7oFAssoy_vCxpFAmAger6BUTTrUkc1etAVF6kjgKgHu5g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/629abdf2a4.mp4?token=rWuxy_q2UsauDRd_Ah0PIIuXL0vTOMrQ0hVHAvjY-EIvwf-Al8Z2MEZaFBOsWksArqU77EtdWilLF3wlBpl3ZNFGQY_MlBb16UFpYcBcTgycgy-oB0KvmUzvfabOygwwT-vxgMHD2aE4-pHIilXhygFLVkDQDsYeeXdoBT2MvEzREX53U-ghyfFKS4xKzFwZR_HGjahDy8mZkxLywqWS-t86srOZYyo1MpnYNiw30L8ZGiXLmTN9Tth25pfCtiPFZtloqKa_b_un95yRLA1doHxJhALQEjTbijwNDCVNH7oFAssoy_vCxpFAmAger6BUTTrUkc1etAVF6kjgKgHu5g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تیکه‌فتح‌الله‌زاده‌مدیرعامل‌سابق آبی‌ها به میثاقی در گفتگو باپیمان‌یوسفی: مواظب باش بعضیا صندلی نداشتن اومدن صندلی رییس رو صاحب شدند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.5K · <a href="https://t.me/persiana_Soccer/23768" target="_blank">📅 17:40 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23767">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p4riYTDC4yDFUPNAUHZqDyCgPV48GTD3j3XutjSKPy56QAoPWBG5jA5JKsdfI6aKthUJc3hG62wMcYlqj_IgvFfV-90upLv0LTpo9RNfznXaDYFn1IAFuJav70E637rPDT5xZlZTJZPMoOEjGhL0unDEP6R68iyEHVFbwG6CFuNQdMbAtqq8cN_E3wO3GX9bVuZtW5HQB_yYaIX9QtY8-Rh9KS9K-OMVqlq9Tv2-SSeZ5sswP4NcvQepzh37AfZ2hurl8fmGXpbrprrAD6RhW489PPy9G0z1KYJ-8IojoJHHM2fewmtSO5gZ1-zc5HJ6XXdoEwrHzo5jpJFBOiPrUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
خوزه‌فلیکس‌دیاز: فلورنتینو پرز رئیس رئال مادرید به مورینیو قول داده بعد از اتمام رقابت های جام‌جهانی 2026 تموم‌تلاشش رو برای جذب مایکل اولیسه فرانسوی از بایرن مونیخ بکار خواهد برد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.5K · <a href="https://t.me/persiana_Soccer/23767" target="_blank">📅 17:33 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23766">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SjMRSj8ipE-wa39gfsDCn-5LJ5vgyaBP-XlmIIc8SdYQfhqTKQDT4DXlqwVeVgWXgKq6SsJ1uYIMlnEDR4h-fnfvUMlPCBDJLhf9RPbx8nVc6FFpUAYhZnFc7Gl3nPcZi5qE8qSlYR79wUwDYaG2vdyj7ph20kcdl7dDJO33ULnCgEyEe-D3yX-0_14NtIU4R_rjSKzJyQwkTkgDyAwv4I13aXvzBuOg0yn9qHbQhNlZRKqEKxZOTnSGITtDVqPRAw9FO-YTPwbB4Y90KX3n4nVyb9PCorAX5nQHJWBew9Rl57rUiqv_mSPTuDnu5i9K15CZ9sUKIduD9Drz6zC1Nw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
مقایسه عملکرد چهار بازیکن بارسا و چهار بازیکن رئال در هفته اول رقابت های جام جهانی 2026
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.1K · <a href="https://t.me/persiana_Soccer/23766" target="_blank">📅 17:18 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23765">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GpEv5D3IbhY1YqAhf5rkqNJq6aOmpzC_gtwJFY9Ih9s9QWud1B1y-JMWAr7vvO1fKMt38HMvUBqK4yPXlnkRYVf45KDIUTK_o8ZJb9LMigDDseptVeA7Z6uneRKb54kJi7wXJZtRUtQbnocZhsF7OBr8kE1gKzALiYoOldfy9tP505rjCe5HPp-InQFFHdFA8SufoXlZtxYPX_XY_-h6Mq9u8UEwsc_E6-I0vuGqISQGzMMyJLfrlabLWrET7n0EVnHGVySfvYV96J2lBagSifdP-1t9_4Ua0dXDvknyAXQoBWO2o61Fmb5TpSUbpd1XRMjzzH_-pTtf-XwfcnLUzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
بهترین‌های‌دوره اول جام‌جهانی ۲۰۲۶ در یک قاب؛ از ارلینگ هالند و لئو مسی تا رامین رضاییان و علوان
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/persiana_Soccer/23765" target="_blank">📅 17:13 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23764">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JZLuS0aMaX9D0FwnEqpnpfcRqkRx6BSMlaDBfLqVdcz5-ZJL08gJEs0o3-Mj7GM043klZv71DtSgAkRrELp3mV2ObLyGGWsSlaov8dUSjrvFnwZ7lolA21iZa-6wykAIb7sUuU3-pqv8UkYa4zeK4IC4573YSEJs_t5NY1j3xMVbaxSpQB4kAM-c95rxS4FH71iQabo3-W2E49ZaGxdkiYSF5Az7Y-QV8hc9NyAciOBBWeV6AN87Szu8zPr1XFzSz2Boc9fdVsGK4sX0Oo3YWyoruXj9E-VqK46-ppQYb8-1DKULyzkjXpfQ0pb39h9IQCvHyf1SOF59_8yTmEF--g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
خورخه ژسوس سرمربی‌سابق‌الهلال و النصر بعد از جام جهانی هدایت تیم پرتغال رو بر عهده میگیره. روبرتو مارتینز هم هدایت النصر رو بر عهده میگیره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.3K · <a href="https://t.me/persiana_Soccer/23764" target="_blank">📅 16:47 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23763">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jxt8bgsHVlpeXxqZWVOGu3oTH0GMGaVJf0oxL0s6aui1k0vfjeiVwKGQZ8M25Te9kn6zUJZ_4RWB_IH8HH7srngK4cKpq8ZSrNKFBluAA8N_AjZvUqIOuZGeGPSAPiogTE6Mra26hc1ZiBUH8-FMrLZdcn1VElV71Lbq0qqs3ggSbxl5TguPHnUNMf0J0XJKTbS1uiiomB61s3c2rXGc1JWDEYkMdV1IX8sVZPqpn2yAo1N3B3T_N-rXKCBnHdiOhzf_11mQH_Bn2bok05YExyBz72VOeGrWHStIAaebC-91rCsYFciFrnVuWhMCde2fkVWTY8R_lQla_w5X7DM16w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#اختصاصی_پرشیانا #فوری؛ علی نظری جویباری مسئول‌نقل‌وانتقالات استقلال با مدیربرنامه های محمد جواد حسین نژاد مذاکرات خود را شروع کرده تا بعد از باز شدن پنجره این انتقال رو بالاخره بعددوسال نهایی کنه و حسین نژاد آبی‌پوش بشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.2K · <a href="https://t.me/persiana_Soccer/23763" target="_blank">📅 16:27 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23762">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ln7o2w7rLaz_XO1Rdtvk4plyUDCiHOj_a94HcsXOG4U8BsHS8Rh5wGLl_DbQWcutZX2hfVEStptWPvI0zcHupC3PVlcw-uZehGTD9oSveNwXPQBZ12nfB3qWbUWZOGcrO2YLZCwyNSB5HWcVVyJXuhuguJ4YcRXo3z0IokUFbZjvFu272q8RCB_DMy7mcj9lllkpRDb5h-SItsvJXadkGcKO2-4zJYoUOJbhdIS0w83cCYvpjx9XDKbbLoqis-GWqnzXUVfA-JOHq0BkYDaqs5GhvB8BuyDvSeinUZbBpsFo8u-nZ3MzrdMcYEWGYBE4pjrZarzK3_WzD_Vj8FyJtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
طبق اطلاعات به دست آمده پرشیانا؛ باشگاه روبین‌کازان‌روسیه به ایجنت ایرانی که ارتباط خوبی با او دارند اعلام‌کرده برای‌صدور رضایت نامه نظمی گریپشی ستاره آلبانیایی 2 میلیون یورو میخواهد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.8K · <a href="https://t.me/persiana_Soccer/23762" target="_blank">📅 16:16 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23761">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pxD6R5gxEQr8Q8pwHgyDGsI3u2tkofu1OgiI4bR-CQQEdzum5qo2LtkEIKFhCo-ar70clXy-WSpD1PUCA-skb3SoMbue7qw022WplWwlD6tBQVMELcuT7QImWx4bqYdcppgtlGj2ampW9FQxHzgRo04cycRKcOq6mRcAYRtPBBcMxoc02oS8AC2b6VEaJQHFEY0KuXCIV14ThypXRoeOBwaGb6BAf9w2STtcpok8BC8EhlZGAnFa4RfrqNjo72iZHG5CljJTe5_XOgzRpbaz5RKv75tAdmqlEV0xRGO-Sd2bLV65ICHIOXJrsfHRJZRd8_jHco_GrfbNIfzYCPx_SA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
برنامه‌کامل دیدارهای هفته دوم رقابت‌های جام جهانی؛ این پست رو فعلا یه جایی سیو کن و بفرس برای رفقات که تایم دقیق مسابقات رو بدونند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.4K · <a href="https://t.me/persiana_Soccer/23761" target="_blank">📅 16:10 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23760">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gvc1Btqo_VdvCaCVDJQYYluCt_jC9X6EEPWLzEuAKHR8dDRa6aIX51Ey8y7zWq4qGiF2-FDL8i1B56X-oR60PW7jnUWi6bAZLT6GGf-AXxJXj-QOawxVMvMfpX5OwbqlfInd3Tp5lMylDOBmn1u5mOHisOGYMtsSk4I986oAeBwcLiMR4EKMSHBTT5gnlua7mbpFJWItfQ2rzKw386ZuxgrwvW7abP-MBov7qTCrBKsV1-2JNCYIKWHNXBxD4zUdYyfSGU2QyayvS5Bt7HOaWz3x7g47LTCsqHC6Paq3h85nOA47E4tGS9yU8JV8Cgjg08gXIJTw0uFnxQD72_UUhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
نشریه ESPN به نقل از مارک کوکوریا مدافع جدید رئال‌مادرید: انزو فرناندز به شدت علاقمند به پیوستن به رئال مادریده و فکر کنم در این تابستون این‌انتقال رسمی میشه و انزو به رئال خواهد آمد.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/persiana_Soccer/23760" target="_blank">📅 15:24 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23759">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X_c6RO8c1BVdbAgYgppd6KlSYCF3n6RA-4HbdeWucNEnDPPmWu37GFudXKb16SJYJDXs14XoFwCRepQPr7nvafZRxmJkFz-Dtbx270SyHALYHF9mCUDjrZOtkyU3TNiMBEZIjgBrRmoN5MQv1F9gTa4kyG7rkKUn5RYmoXP6K75DSOJ0pz1gI2Q32pEG9VVMyBAI7ctUzF6UxjS3aRB32g_ULZVt8o-wftycwgsGRGDy9R9frALMJ3l4_sjXC060KvEBz07kSB6U1cR96vbVZHVp3kxVHvD8g9KUA_X1EenqznygfXiox2L3s4iPVx1VKEO7lr985MV8-v7N_fUCZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
⚪️
🇦🇷
#فوری؛ باشگاه‌رئال‌مادرید برای عقد قرار دادی شش ساله با انزو فرناندز ستاره 25 ساله چلسی به توافق کامل رسید و حالا تنها توافق بین دو باشگاه باقی مانده است که این انتقال رسما انجام شود.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.8K · <a href="https://t.me/persiana_Soccer/23759" target="_blank">📅 15:07 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23758">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c2e3fa7271.mp4?token=h_HpH_KIMAzxW233cr5gGZC3WS1KctNEGrk-s5G0yaUB3EIEocg9dJsKylWRAQ_twAYgjwdwmaQOKb8TnZQtOFmH2ze2iibR-sDqml1Oc7KllQ5PFQzW5zgDQkt8iFw-VUukPpRBeGUbyyUT609rR9AZHyYo3z7gC-w0awzpUQzLhuyG9TKSX1S3koGYiGjGySeDbMfwVNoNq02giAI6AK4T3_lavVn5qsE0BPqB5mfS8tbSKYC_Y_f0pLbMZP8qINK4n662PkuQ9RshHsbtexSxUD89P713avkAsiibahzBmEdhQSz1_o6euU0aQeEDRTWJJNo6vr1AAyQ7Z2neIA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c2e3fa7271.mp4?token=h_HpH_KIMAzxW233cr5gGZC3WS1KctNEGrk-s5G0yaUB3EIEocg9dJsKylWRAQ_twAYgjwdwmaQOKb8TnZQtOFmH2ze2iibR-sDqml1Oc7KllQ5PFQzW5zgDQkt8iFw-VUukPpRBeGUbyyUT609rR9AZHyYo3z7gC-w0awzpUQzLhuyG9TKSX1S3koGYiGjGySeDbMfwVNoNq02giAI6AK4T3_lavVn5qsE0BPqB5mfS8tbSKYC_Y_f0pLbMZP8qINK4n662PkuQ9RshHsbtexSxUD89P713avkAsiibahzBmEdhQSz1_o6euU0aQeEDRTWJJNo6vr1AAyQ7Z2neIA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
آندره آ استراماچونی سرمربی سابق اینتر میلان و استقلال درگفتگوبا DAZN ایتالیا از محمد محبی حمایت کرد و اعلام کرد شادی بعد گل او رو پیش‌تر از بسیاری از بازیکنان حرفه‌ای فوتبال دیده‌ و معنی خاصی نداشته و فقط یک شادی بعد گل ساده بود.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/persiana_Soccer/23758" target="_blank">📅 14:44 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23757">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ih-yHyJmoDOea14ntkQSI2eIIf3lkuAcUciclxv2M-_vMANGDo-U5F6ZANFO6gT1J6SLlaXPl_co52r8bxNftgO9pO4hJGbzspAaeMkzw7MXCaNdMHxwxZcSzFADYHM5bQa6NrcotdLc1K0lwwDyTmEPgeGOsrcscviLbaeYBKRbbep7sCfAcS6PYWmuJgtXrkEzS1VC8SONpKf-B2rl6x3HvOiqiso0jc9XaMH82SpQcwVDCw0GMkAR4sTVau311kHIXb-qmeZlRcgrzad5SW5uiIcwbSeTgd5D3G6fJsOPmLqx37bKUjgRumAm8A1ebaj7-4X6YjaVYVVdJEhe7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#فوری؛ باشگاه چلسی آمادگی خود را با فروش انزو فرناندز به باشگاه‌رئال‌مادرید درپایان جام جهانی اعلام کرده: 120 میلیون یورو بدهید انزو رو ببرید.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.7K · <a href="https://t.me/persiana_Soccer/23757" target="_blank">📅 14:21 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23756">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SWocxv_EkSbDy5dOVkZPeeDQF0kSBo6w4FC4PTJfsZau3TKWHfTNFeIFZ2b22oWTr34C4h4w2la-mMVYVjkJb98lh3V6ORtfV-TaVaNC97I61ckNKJLvSiC3WUC3uL0OWeq_uYwwwD33gdpchz5nB5HQVtRaa7O2c_kZ8GwXMAPfeNR3gqRmPegKbYSnLV9lNd1j9v8TblLSSDMpWSYkvWsGtvpdUHzbgqyJmN3RTbv9BS9sfk4rQ_hXpWEouApouYc6T0FSYo065mU3ja60KFyfilVHPcnj4i-phgUpJ8gs9DMmW_VRJdZ2KyvwDeVOlafYGWjahs6qmC4LtULNSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسماعیل کارتال در گفتگو با TRT SPORT: آماده پذیرفتن هدایت فنرباغچه هستم. مذاکراتی با باشگاه داشته‌ام باید صبر کنیم ببینیم چه پیش خواهد آمد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.4K · <a href="https://t.me/persiana_Soccer/23756" target="_blank">📅 14:13 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23755">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nxXko_NuTGhcdwlWu4HpE5I5orQkXYWkCv1IZ_OhZWkX4zEVIYNFDiZFcu7RjS4ZLQj1VQ14iyuyaWQxEXj7gF-iMtyy5Qo2B7xwB9-hTuPyxTQHlgw0p3BKxm59OBE2ynNo2bzLbZuQbhD8q9nSYAHZYaA9EyO0S-k7TL5VYAXe8K7rM_RE1h5GBw3Brjgwcoi62zR5kC_U35f__UUiSPMp73G_ZBHWP08tkqmX0F8LXPMNkHcTWxPz_dRguJDDs37b5_aGtHdUc6O5d0PnaOn40p57mT8gpHScuCESoJ3OlB3gF5cincJFwx3IToo4pnAZCKl_Kb7Kjad_hm6-8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
باشگاه پرسپولیس برای‌فسخ قرارداد توافقی با اوسمار ویرا برزیلی به توافق‌برسند سریعا با دراگان اسکوچیچ قراردادی دو ساله امضا خواهند کرد.
‼️
مدیریت تیم استقلال در ابتدا مذاکراتی با دراگان اسکوچیچ داشت اما عزم‌ علی‌تاجرنیا برای اوردن این سرمربی کروات صدرصدی…</div>
<div class="tg-footer">👁️ 44.2K · <a href="https://t.me/persiana_Soccer/23755" target="_blank">📅 14:09 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23754">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j-x51S5GyzF4V0sI_aPsYNqnxHvFWtH4Jeg2CyBDPF7al5Ne4visN5kXtjruMG1sMTqAUeMnYqAs0dXOTdexlUqs7CNVzzgS4586vYCK_kRN1jABx4IDbqz91uTnd1CFmHUUngkP0w0I4SY8Sl88H1AMMLUCZ7yzkqukXMFIM7nRljrpD34zrVB5QfYdCere32ACezLqSF75fGRRWegngojdtohfPQ_OtNqBOeSAnyeNrEhBgf8VlIfSfj94qBC1u2SIf_I5vIOAMYjEpbsoCxxOweyYwPavMEYlnkxh6x9CLE31vhF-TtQkPJY-JZaKigWW8Hn6t8zO0OdWCy-xbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
جالبه بدونید مثلث خط حمله بایرن مونیخ در فصل گذشته؛ هر سه تاشون عنوان بهترین بازیکن زمین هفته اول رقابت‌ها رو از آن خود کردند.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/persiana_Soccer/23754" target="_blank">📅 13:55 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23753">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iwX7xi7KMmkn_X9fLvKst3tBrvIPiiBU2QxchBWdjayq83wKgAiyffdohx4igvO_AeQqBksDKnSrg83wmDoALA9_o7Cu2IUDFPTyBV4CkyzfSCiJI3O9L5tqQjBVmNc03PQBZZhg6_k8cWIgs3QeJt-ILCE1wyYmuoGpe2jtYh1zruSetUhzNks9mGaQvERm67b_TnvbfKJs4k9n_vWiBnX4x2xYm7gLqgM61tCvrnuVM7S9tJk7DzUea5yxb2XcNT_dUsIKInvZs0hjwKDcvCizpLviqTizTU_9UKKkU3uUd2xgkQQFy69sFjFvOqA8J1n2Pai-dRloNZ1naMvpkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
بانک‌شهر برای دوفصل‌حضور در پرسپولیس آفر 2.2میلیون‌یورویی‌به‌‌دراگان‌ اسکوچیچ داده که مورد قبول سرمربی سابق تیم ملی و باشگاه تراکتور قرار گرفته. حالا تنها مانع راضی کردن اوسمار ویرا برای فسخ قراردادش با سرخپوشان پایتخت است.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 45.7K · <a href="https://t.me/persiana_Soccer/23753" target="_blank">📅 13:27 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23752">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FnyyMVd_0rVWnZoWrUo3iD4iblMxgr4h0n74u3lO9Alw2ZhGJvn1E-1NIhccS6lSz54Db2ceeCJKjrm0__R-xPATGa0VIuAH_Q8-V1sLxv4yoPwcclwMua89Oq8l4vfn_yHoobzyBp0C6_SudFuxLM3NZYmf7anIRs84RXi3fRHgiG2viq3A-stSiN-r58-iv_EuNwtJlZiHdzf38YKYF9Oi4vySK9r7Fi6uHrlWZtuX9WlnguXL2fkjAkdA7f5h3ESEX9_Nv6c5TerHwlKM8ml91RIHvU4O6qQ8NRizaZIbHZIqyJ81LmZbYNPvhQTm-g2ZS9HsWbMOXzbmLLQRIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
وضعیت عارف آیمن در جدیدترین آپدیت سایت ترانسفر مارکت؛ اعتبار قرار داد فعلی آیمن با باشگاه مالزیایی تاخردادماه سال‌آینده هست. بنظرم می‌ارزه این پنجره جذب‌بشه از فصل بعد ازش استفاده بشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.2K · <a href="https://t.me/persiana_Soccer/23752" target="_blank">📅 13:19 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23751">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/10541c5fb4.mp4?token=GdPKD0WAvs9ss1iJQMW9NZexkoNXFaoB5N9czLEtaJTq5fgYuonhjXoVce93UJd-PQhHb-fjACd4lnBhzkybxENC_xStNAqcpyn22mKdZu5oO_AQYlrT-geUCGAD7CXRQrdnsRrF1GJeIQYBiGs10XYrwUSVPTvG1WkTdBTRHQoVHlhMwTIm0BtJ1oSYH5GklnDccmqGYEnG8AEyCuR_Pazcw4F_cT_mKhzTut3w_PxkHC29_EzjBGC98mkcI3n-_YYaCqa0ZrhmaLIzQbJdF5NnmVXOfb8-uLkMy52Xu79rmatZcDy796LxYWhk5WICJn3lEybH44EgShzVL65wTw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/10541c5fb4.mp4?token=GdPKD0WAvs9ss1iJQMW9NZexkoNXFaoB5N9czLEtaJTq5fgYuonhjXoVce93UJd-PQhHb-fjACd4lnBhzkybxENC_xStNAqcpyn22mKdZu5oO_AQYlrT-geUCGAD7CXRQrdnsRrF1GJeIQYBiGs10XYrwUSVPTvG1WkTdBTRHQoVHlhMwTIm0BtJ1oSYH5GklnDccmqGYEnG8AEyCuR_Pazcw4F_cT_mKhzTut3w_PxkHC29_EzjBGC98mkcI3n-_YYaCqa0ZrhmaLIzQbJdF5NnmVXOfb8-uLkMy52Xu79rmatZcDy796LxYWhk5WICJn3lEybH44EgShzVL65wTw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
جذاب‌ترین‌بخش‌های‌گفتگواخیرامیرحسین قیاسی با مرتضی‌پورعلی‌گنجی‌وپیروزقربانی دو مدافع میانی فعلی و سابق پرسپولیس و استقلال؛ عالیه ببینید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.6K · <a href="https://t.me/persiana_Soccer/23751" target="_blank">📅 12:58 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23749">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/C3-bvNsT9eQlXfcdOWxr62xWJRU-vMu7IrH_MrNF-3QjZxtuPiTrx8LaPnahPxpPaQN6TSY5gtXH-xVySYuGiVVvXmc4TwlPY2slB58AQpg3hLjwyomXVw1pYGIz9yYy5NoB279aGut8KLrd6hGZb_Jo-EOcswYf6-Obh7dIEReCEdx5pmF5SJW2gS6WRCp4uYhKVcEdSFuOf2ZeWt8H5CiwXNzcnKp1GlAKUidKeBi_kMY4mKrk7LAXsxmTo0QLrXTIzbHGkNYqLl0bGTNgQYo4znaJzQ7GyP3b-AZWpRfN6tyxAJr_Yw-5TsDEZUqWEYEU_92AAvXGUy-C8RewRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/o9I9ORZ219QwtTDSBmTIb__hSttAnYjJr0JGR9jTI-CRpCDWkZi6uWBDKjvNHeJ7CV-f3OZW4bR6zkTtOD7WJWuJvYBF2LH30WbT5y0Mi5wCInqADhQr3qvtB_ZTf56wVhjFdjH09K16QhPJHQmCtqUl3nJ8G_1Jrf7u84XQoU7GhPUR2JQuH2zPnff4uqjodBPGDlqWYYZS1g1xdixNB5cYqb7fc8vOQFgRVxTKcYn4-9o2Y1i11ENIAIExpsXYE5y5A_PfOnWSd0KMQqACS0Khv9YJSZ0S7VqPj9xoJdnmlpXCxZDZqi9OHrFV7Z6mztO8sQvwki6XAAFZn8fIRw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇪🇸
📊
مقایسه عملکرد آنتونیو گوردون
🆚
مارکوس رشفورد درفصل‌گذشته رقابت‌ها؛ باشگاه بارسا بالایی رو جذب کرد اما پایینی رو پس داد به منچستر!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.6K · <a href="https://t.me/persiana_Soccer/23749" target="_blank">📅 12:51 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23748">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/orMbO10E1CZnfw3FjuKkZniFPZpp8iQAFgK8eSGr_vZmO_Ug0_0yhUugKezwEyPZqvW3PxS7qocCE2isEVqBlaSjMwXefyObFQkELi6hkcnMOeDKkAsez18SGi57WawM0eR_l0XR2ix05B3tBg_N9cM9A1dmc0eSxTfFQHDAAZwOzdDZEWPvGlI32Owt9bvlmBZrMNkH15dRyaU_mGdtXfDUKuTnTSxPtZGTAZxZ0XEm9pwajo707RfEGLzBPpgr5RfX0VObWE1iHL8BkYXw4znEyXLtuaH5vDQ8XbzGrYJcfZ69RjcIGBS86nFE8jptI-2TejNWVNPp1XrXrQfdag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
رومانو: ابراهیم کوناته و دنزل دامفریس با عقد قرار دادی 4 ساله رسما به رئال مادرید پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/persiana_Soccer/23748" target="_blank">📅 12:37 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23747">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0e75ce8522.mp4?token=vzYPv3uG97Wyic_3LfpFkEofMMhiFbcwbZI_-UbIkKzEfoLLTsbs-hq4iRK-zDZJ-DT0oWZrSA_8-n2miROyTAvfTI1WJSW0N7utKeKRIgnLx1c1JLKNmY398y-dM1I3BnGw_hGKWlxfzEgMqNSHIMay3tuvdyrawtLjliry0jwOJfY1nibUI_QU_ox-XWEbZpRslYe2haXEQvWHOMkW5Hz2QHCsZ1WG4qbwV4K0-7bVTa86Er4cXiYUVpvVEwUhMmB5niH9WyX2F3yalES4xqvly1Z9XmrEQDvb6-lSwDZrQzWBVMgqh05vx4ni_yq0LvU4L2wMMT8c-yi-eD-gkw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0e75ce8522.mp4?token=vzYPv3uG97Wyic_3LfpFkEofMMhiFbcwbZI_-UbIkKzEfoLLTsbs-hq4iRK-zDZJ-DT0oWZrSA_8-n2miROyTAvfTI1WJSW0N7utKeKRIgnLx1c1JLKNmY398y-dM1I3BnGw_hGKWlxfzEgMqNSHIMay3tuvdyrawtLjliry0jwOJfY1nibUI_QU_ox-XWEbZpRslYe2haXEQvWHOMkW5Hz2QHCsZ1WG4qbwV4K0-7bVTa86Er4cXiYUVpvVEwUhMmB5niH9WyX2F3yalES4xqvly1Z9XmrEQDvb6-lSwDZrQzWBVMgqh05vx4ni_yq0LvU4L2wMMT8c-yi-eD-gkw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
رونمایی از تنها سرمربی حال حاضر فوتبال جهان که در چند ساله اخیر تونسته ژاپن رو شکست بده.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 44.4K · <a href="https://t.me/persiana_Soccer/23747" target="_blank">📅 12:33 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23746">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ft9wbxY0pKS510Lw1Z2JwuIiqm1CPXdScRnv-HqefpZMep7hF2sZ7MIaU_Eae6Dm2yBkUAz4jk5bz2Ni2z2zkGZWo0FwhxjbXxqKRIkscr8WihRUp6epBh9pUseuZT9C7HyZ4gWk1LP5GCl7pKWgWJ8Oy32CXeM1QJxlThWA5D7TnmKeYylLH9Z76k9OaH6QT1C7MBcIz4qWvNdzZ5IWcUTV47Sv4wxArJttopUZr_nsmGvfA209DxFP-f5n7U5nEyHXS4Os1he_vVZItqT3ib504xbtP2JcZEtqAtc5PUQzaakHUsLZ0deCR-ZN2fPiygQM9kPaqd-dW6GHtVa7mA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ مسعود پزشکیان رئیس جمهور بعد از امضای توافق‌نامه با آمریکا: به مردم ایران قول میدهم بزودی وضعیت اقتصادی کشور بهتر شود و قیمت‌طلا،خونه و ماشین روز به روز خواهش یابد.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 44.2K · <a href="https://t.me/persiana_Soccer/23746" target="_blank">📅 12:18 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23745">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tt0n4Dg6F99X0d81ahNdRa0pdW2fuj98jj5Yo4i9aikyRlE1CptejgYl8-KG9Cd0ycBstqBwko8UMf62JrRv9IloHM-nNsfvPkAU4qCKSSpliff_yTYOJ-N0iC3lGE8lr-xGVGQiVLj-dGIJv1XJbGexCaXIRxSWt4jL61M3HONFnlcetF_eW64ILsfSDrbGEYxuIPUs9fYGSpsJ7Zdkxy1mrilIvWhBpF2rG3oH23k7zkQbrrMJ0j8blYUGUbi4IRd3S_gD1Qs3w59sLBjPfqw3h5C2GDbJf4JkVPs94AhE7teChIoUX5ftmfQ35TjQRNe5RvQGymH7YybsJp-aaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
جدول‌رده‌بندی12گروه رقابت‌های جام جهانی در پایان هفته نخست؛ از امشب هفته دوم شروع میشه.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.2K · <a href="https://t.me/persiana_Soccer/23745" target="_blank">📅 11:51 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23744">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HBc_cdMnrBEndH2bEvfrNbvnS9lUpR_Xaz0MsmQdjtKZi9-BVxmQcsJD0apjy_PoVypeYlesj4v3w-ADtjEdzIQWo6Wd0b2MgpHmazQzb6YObTywVVrmQ6yX3OB9rnMAjLCuD0HVflWbLXQOvdhoY2bgj56UMd20CK8dvMM0Gxa_chhvGq1srmnyifP75SisoKKONHlVaNbSvSBaNI_-ApctABj6qGOCTIEHjzKIf7bke26vXZOz-JPnj9l54supgPXFxFRTJe1cLaIs_uqFs7Uo6In5tW6pfMxJlDbCF_S3awJRAHSftMU90EwNPAJnzImm_hp6R_uuvkBaOh0png.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
باشگاه استقلال با نیما اندرز مدافع راست 20 ساله لگانس واردمذاکره‌شده تا درصورت توافق نهایی قراردادی پنج ساله با این بازیکن آینده دار امضا کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.3K · <a href="https://t.me/persiana_Soccer/23744" target="_blank">📅 11:37 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23743">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">▶️
قسمت‌‌‌هفتم‌ویژه‌برنامه‌‌فان‌‌جدید ابوطالب حسینی برای رقابت‌های جام جهانی 2026؛ عالیه حتما ببینید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.8K · <a href="https://t.me/persiana_Soccer/23743" target="_blank">📅 11:12 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23742">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b9f495fa66.mp4?token=hgvkJGp-xV-NcWwatqT833ybaVrewECjQgDl00TQ1EBGyTuuk1lth-cUOusW7ZdoeGR85HOMBkKxnj9AqO1leVSY5ZJGlAL-ezdYySK1z9gpQxCU5uMFCPS9oIkZL4tc5SfoHIgOHcs8osfYX1guvpMdHdqJKnN1eei8rjdDx7pp-PBURDycpmti5-L509HlrTsEWieEw9yCNmAI1uRzyv7E6QTJGl32DpEh9_jEKOJGHbaYcEz3S6P1bl2gRrZE0pY16N0BNIH6edgOmXPU09oQ_Uds1Y3YdugetDmqQZYkDAp6XUYiXS4FandsAStg-UIPuqDST-6xeBz58Bzjjg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b9f495fa66.mp4?token=hgvkJGp-xV-NcWwatqT833ybaVrewECjQgDl00TQ1EBGyTuuk1lth-cUOusW7ZdoeGR85HOMBkKxnj9AqO1leVSY5ZJGlAL-ezdYySK1z9gpQxCU5uMFCPS9oIkZL4tc5SfoHIgOHcs8osfYX1guvpMdHdqJKnN1eei8rjdDx7pp-PBURDycpmti5-L509HlrTsEWieEw9yCNmAI1uRzyv7E6QTJGl32DpEh9_jEKOJGHbaYcEz3S6P1bl2gRrZE0pY16N0BNIH6edgOmXPU09oQ_Uds1Y3YdugetDmqQZYkDAp6XUYiXS4FandsAStg-UIPuqDST-6xeBz58Bzjjg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇦🇷
واکنش‌لیونل‌اسکالونی سرمربی تیم‌ملی آرژانتین به‌سوپرگل لیونل مسی در بازی مقابل الجزایری‌ها!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.8K · <a href="https://t.me/persiana_Soccer/23742" target="_blank">📅 10:39 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23741">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TVZNb5BWjhPfi68WlEa381DXDKxd8hPI7D3JauBd_J5VQHpveCu4oKPeky1SgW7qBOXR3xCXZDN0Y-P1yWB-jl77mOnogrpYnyXc_OAnfG5hiSz8FfcWEhA8Trpa9xZVnUWMCd-ByQoiDXOvUA-Jh2-mTX7QKk2xlexNeiGPh1DQVTIs0D868jyaWgm5wziBFFXdSf5S9YZDJWZdTJ0QQToxeo8Z3ZmZc7BzwAuFSfWaYUaFaZtI8mHDzh6VaivRf_0xrK6rp8WUXucEe4XL01KRLstrK4kIKqOAFk2kDhpgJW8qGLz56ZgtTJealGwWxKbq_3SSCMfcQeyJ2v6RiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
طبق‌اخباردریافتی رسانه‌پرشیانا؛ فرهاد مجیدی سرمربی سابق استقلال پیشنهادی دو ساله از الغرافه قطر دریافت کرده و در حال برسی این آفره. احتمال اینکه گابریل پین به کادرش اضافه شود نیز زیاده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.6K · <a href="https://t.me/persiana_Soccer/23741" target="_blank">📅 10:20 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23740">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gA5Zq70Tz73w-loCfU5uGydgeB57Q_BZsaISvfIrJspEYy8TNiqQ2o6nio4BYyviPXkmOn7NhmiHhKwOtWnt6zxzRcB4LqB2oQJd7ZA7FVNFEa1gklQ5rd2zWuNgLBuL1hzAZ3SBszHUWdTecQzRx16thNwhjNusCkuNO8QcneJX3gIFgEgbYwo-XojnYgVcpXaJ322_Vn8WaLA2LFzseVcr8hPT3MDODlVX_Rfu9FA4azAX46blwcf_yOPQnt-Ch1kfEqiZLF1F6LS5qw8OVgE11NSAtDVa1sA-DhOmKryTpkqEujvYXg3DMGOFxwa6J34LW-c2EAwOuhF_q5YgDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
لئو مسی در پنج بازی آخر خود در جام جهانی
🇦🇺
استرالیا؛ گل + جایزه بهترین بازیکن بازی.
🇱🇺
هلند؛ گل و پاس گل+جایزه بهترین بازیکن بازی.
🇭🇷
کرواسی؛ گل و پاس گل + جایزه بهترین بازیکن.
🇫🇷
فرانسه؛دوگل+قهرمانی+جایزه‌بهترین بازیکن‌جام
🇩🇿
الجزایر؛ هتتریک + جایزه بهترین…</div>
<div class="tg-footer">👁️ 42.1K · <a href="https://t.me/persiana_Soccer/23740" target="_blank">📅 10:20 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23738">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l5FzlNJcJuYeyirVGvVIlZfIpeGo-sbxtfkYMSQ16mX2d5J3R-kQgTESjgHXDBq7-I1pJvaOOOx1E1hNMafx7VhCv2MywE9lA-PwR5fMYEiAG7BV0B9iKPcic0AanK1SK_lijb-NPp9J8e34GEobWc2Qj0z4N5sceqGf9EZE5QdE_2qXtfoBV50SynjV_mUayKKIuuluIXWv3WjP01tpoMCSVMtQCLstEjdDCmmHRl1UbVov4y7dZRUB8UCD68yTTlYA8ZuXAbHj74sLq6QSxc009f_u7fO0D1DclvcLH3XgOvd3hzAhwg-wLqdPIEY0Ot40qhvq3J8j922nJbbdWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛مدیران‌بانک‌شهربرای‌عقدقرارداد دو ساله باایجنت‌اسکوچیچ‌به‌توافق‌اولیه‌رسیده‌اند و درصورتی که هرچه زودتر با اوسمار ویرا فسخ کنند اسکوچیچ برای انجام مذاکرات نهایی به ایران خواهد امد.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 42.3K · <a href="https://t.me/persiana_Soccer/23738" target="_blank">📅 09:59 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23737">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/75cc17874c.mp4?token=tjSUVXLpcVdPFRjb1kBTGYfULrvRh7vrSrKwaGeTi04OiRuhT-AXst8S7IgVeQk5HIVTvOtdSppjp-4IXTaCWLg_SNKkHCx920eHimi_PoXdr8g37H9SrClrndiG1FVbx0KiH2jc85uMX2U7NVegplBc91exNKD9F7wKlnueZnAwKuPduJK-83jgH6vs8v6OJsmwhvHdEHEPBUnF21uFgynfWSyQZX_np3bDbzXTEXeWTgUIWnBfhQEzdbNsIrnWxatYrGp_6jktFIDElV5QRqZbk9itevqY628R-vMrwE1dmJB4ytsvvm9LP46dRlaUmwxMd1qZ5_yq4B6ZF8oPdA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/75cc17874c.mp4?token=tjSUVXLpcVdPFRjb1kBTGYfULrvRh7vrSrKwaGeTi04OiRuhT-AXst8S7IgVeQk5HIVTvOtdSppjp-4IXTaCWLg_SNKkHCx920eHimi_PoXdr8g37H9SrClrndiG1FVbx0KiH2jc85uMX2U7NVegplBc91exNKD9F7wKlnueZnAwKuPduJK-83jgH6vs8v6OJsmwhvHdEHEPBUnF21uFgynfWSyQZX_np3bDbzXTEXeWTgUIWnBfhQEzdbNsIrnWxatYrGp_6jktFIDElV5QRqZbk9itevqY628R-vMrwE1dmJB4ytsvvm9LP46dRlaUmwxMd1qZ5_yq4B6ZF8oPdA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تیکه‌های‌داغ‌وسنگین پیروز قربانی سرمربی فجر سپاسی خطاب به حسین میثاقی مجری صداسیما.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.5K · <a href="https://t.me/persiana_Soccer/23737" target="_blank">📅 09:40 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23736">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a6e6215526.mp4?token=Mr2-zdrRqBJqnqw7dTpvfnAmKujp534KNARROXGIpP6v6szDTowI22gM69ah4PGRK46Q7ZARcpmdP57s8yonSFcmMl1J2OjvaEtbbm4fX7EGldHs79vIj9Rmf7x-EB59Bhxslr3qR2KDhj10qYG0oOXL7l5Y4jWMrWENywe-7KGLzXOlWUIq6KX1hR6HQv858ceZ2J6lfMk9KunNbAxDt9qlJs37dTRv21SxaIa5I0uVA-_Pc6CH7YPuTbdATL8AkVTpluJ7eojjBpIqoXXtGupSi16bv69VFGDIdAgZNL-Obeua0B9_ymERj7sQirvqCOaUvar0J78ncwqiZAiNpQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a6e6215526.mp4?token=Mr2-zdrRqBJqnqw7dTpvfnAmKujp534KNARROXGIpP6v6szDTowI22gM69ah4PGRK46Q7ZARcpmdP57s8yonSFcmMl1J2OjvaEtbbm4fX7EGldHs79vIj9Rmf7x-EB59Bhxslr3qR2KDhj10qYG0oOXL7l5Y4jWMrWENywe-7KGLzXOlWUIq6KX1hR6HQv858ceZ2J6lfMk9KunNbAxDt9qlJs37dTRv21SxaIa5I0uVA-_Pc6CH7YPuTbdATL8AkVTpluJ7eojjBpIqoXXtGupSi16bv69VFGDIdAgZNL-Obeua0B9_ymERj7sQirvqCOaUvar0J78ncwqiZAiNpQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
دکتر انوشه باتریلی‌از روی ابوطالب رد شد؛
تو عمرش اینقدرسنگین‌دیس‌نشده‌بود. عالی بود ببینید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.2K · <a href="https://t.me/persiana_Soccer/23736" target="_blank">📅 09:25 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23735">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7467784054.mp4?token=Cg9jlPoNe0Fjw_LAVd01GRJ9hQoV0btQRWxtpsdSbUhVJXb76YG3BmZse3O-RQSkLnwNhlTAo4uy9Gxs4tfWa6XcCZLLdEuSS9rorx-s3zT8_e-Kinn1sgv6lLJ_2EYzMYTYDC_Hx64J4pdYXVeUDH5ZUGSGRxV9hvPJ76TZsm99U5g4Ynzjao27JbGN2wcqnf-MZ0l1karylmFtGCB9V6xm0bL8M84ij6hJBZDRRvgwjtTjiqyCrhvHhmOVoWTFzmlZJ7bHB61jKillXSruIb4490gqtP0c_CEUWHBdsBhoBxQqZB9dqWxkFwJxEXSrjEf3fOAkvLhmL8ywamLrfDHXKPeDfMXox1UeqlPCr8Yz5JL8CV7h5pAH3SLZLlYeQSIKEhpOzMCmS-qMv9sNUGak5Xnh2uiWTC1jUxyP_qaq1igLSI_pD1A1Rt2ZS3KE9y8tC8-11f91H6IrIVJBa2J6zXwu9KjM1VXIE-T-ST0riuNjb-IhLQDA9b-Sqm5mRnTDptE8rvzanUjwP-R8vHBtFeHXnNmpC79N4fbRkS2jr896tL83swCfIeOirqFA_SdLMu8n3bIm8uKeL7BBMm3aVptppjlxxsuIJ42OVMzBFdOyYSSmHVFMM8tBMxaxugtmzfTk7JJJPyc-p6NP54VhXXEaqcJzDKgkVKUzOTM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7467784054.mp4?token=Cg9jlPoNe0Fjw_LAVd01GRJ9hQoV0btQRWxtpsdSbUhVJXb76YG3BmZse3O-RQSkLnwNhlTAo4uy9Gxs4tfWa6XcCZLLdEuSS9rorx-s3zT8_e-Kinn1sgv6lLJ_2EYzMYTYDC_Hx64J4pdYXVeUDH5ZUGSGRxV9hvPJ76TZsm99U5g4Ynzjao27JbGN2wcqnf-MZ0l1karylmFtGCB9V6xm0bL8M84ij6hJBZDRRvgwjtTjiqyCrhvHhmOVoWTFzmlZJ7bHB61jKillXSruIb4490gqtP0c_CEUWHBdsBhoBxQqZB9dqWxkFwJxEXSrjEf3fOAkvLhmL8ywamLrfDHXKPeDfMXox1UeqlPCr8Yz5JL8CV7h5pAH3SLZLlYeQSIKEhpOzMCmS-qMv9sNUGak5Xnh2uiWTC1jUxyP_qaq1igLSI_pD1A1Rt2ZS3KE9y8tC8-11f91H6IrIVJBa2J6zXwu9KjM1VXIE-T-ST0riuNjb-IhLQDA9b-Sqm5mRnTDptE8rvzanUjwP-R8vHBtFeHXnNmpC79N4fbRkS2jr896tL83swCfIeOirqFA_SdLMu8n3bIm8uKeL7BBMm3aVptppjlxxsuIJ42OVMzBFdOyYSSmHVFMM8tBMxaxugtmzfTk7JJJPyc-p6NP54VhXXEaqcJzDKgkVKUzOTM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚽️
10 گل‌برتر هفته‌اول‌رقابت‌های‌جام‌جهانی 2026
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/persiana_Soccer/23735" target="_blank">📅 09:17 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23734">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">📊
نتیجه دو دیدار بامداد امروز جام چهانی؛ پیروزی لحظه آخری شاگردان کارلوس کی روش با طعم کلین شیت و شکست شاگردان کاناوارو مقابل یاران خامس رودیگر و رفقا در کلمبیا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.6K · <a href="https://t.me/persiana_Soccer/23734" target="_blank">📅 09:12 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23733">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Wrv1adyKLG4yVjbON8Gn7BYoGxQ8mYFOGTZ0jXIzb4ISqVAOj8QP7vq_LA5YMyT7qraj4bN2LQA_CzrqIpKYCuHruYEOjwF8lyc13ttLttRzhOKCeufAr9_ATCs9UZm_9cR5lpNEnS5fM7_wWiK_rb5g4hRe8vGx9YcfDkaAJKsPfcvtelEULlqmYaeq30RVczLhLFSKcl7Vuv19IbGOIyQ0FpZuHFAUJAopiPcitoEINXKgDdEwvfZiZpqQ3o7dGVwKtNjRIeYQEA2JRtBsyHDEJgLGRk2Wqg8PuH8J1ZlWyl-P7nGvdPzjiJy-s7g1x6mtJ9Fz74d8TGpIh0bIww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتیجه دو دیدار بامداد امروز جام چهانی؛ پیروزی لحظه آخری شاگردان کارلوس کی روش با طعم کلین شیت و شکست شاگردان کاناوارو مقابل یاران خامس رودیگر و رفقا در کلمبیا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/persiana_Soccer/23733" target="_blank">📅 08:52 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23732">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V4UXjGg4qHj2NPTdM5-PDVa6lr9ATlUG8_DDPG0aD7Mxgf7mIprMFljc6WZj69fCieEPrzWkyK3GASZKHUTwfDZwgQ2TOOKbKwxED8ZS5eS_E8K9BP3ehHJhzH_Tv2xrMUd4v-15IBuzqNh-liNhVCGq3AeV4IEexZqYUMfgLGJu8V3v_XPe5kDUjNUDhCus5r2gKm8uMQHgw3L40zu7xzUgGxmewrpNqhPH2bqkPOPR4sLyE1oFuJ2y1yABq98LJoPzCCGdKYrxJ4gWpuV8SliEdP4dhgPOuJJVY3ttiKiyfQ5mIytcOzvNmaDjy5q133j607MIuDFDTUghaPCTGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتیجه دو دیدار بامداد امروز جام چهانی؛ پیروزی لحظه آخری شاگردان کارلوس کی روش با طعم کلین شیت و شکست شاگردان کاناوارو مقابل یاران خامس رودیگر و رفقا در کلمبیا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/persiana_Soccer/23732" target="_blank">📅 08:36 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23730">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CCttairQttmRblCbeV6MmWDkMmCf7KxABUd_7kYxACf5gKNjragSzQIcWz-C8SbtW6OM2QkwmBNBIwXaUDPpi5QqOweZDJcNMQvCbLrlWXiS0RACkn_0VLQ9W5SejMbY5DJyTQBidYiL5NLHH4-NQONR0JWKAHkhp4aKQjuaQXmUXCJV9GDOrPtEOZLVwclczLc2H2yqhqJio7ZuVCM0eeWIe1RhoieOPuthG5BXyXjiudUDvBKD3L0eaiWsI46zi5rDowQFk4t64aqd-xfL1AK4cJyEC1AwiWVtYtR3M3pU9bD7ys0Bk_Z2K1bjdBNR2m9Y1LmQaHW9qN02-1NVsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EPMzm-WbzHi-jYmrkIdgT0idUhuqQWZopfuIp3Ty3V431jRCqImW3w8h8vZQMX-uG_8Rzo5yr38x39cVISNpuB9QJtLD5i-11iGAfYQ9CaltiVUl2HimG7JNieKo682Ywy041ghym47IYuKSj0XQVCInexg7oOTMxkninGNTIuFnIpf9px0k6c3qtSD4xL6w8whBkycY2PxkPCulCEJYAh2551XNCht2UUonApshSdFEJverdmheDKoHnHTjuB7Mpy1tzkyHoX1SLP-ryy7bMZ69iEq5O9x3uxMDhg3_Rcux54ua8UW791CtKKS4vrkMeTUghJQVnoC6EddNt1EthQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
برنامه‌دیدارهای‌امروز؛ ازمصاف شاگردان کارلوس کی‌روش با پاناما تاجدال یاران خامس برابر ازبکستان
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.5K · <a href="https://t.me/persiana_Soccer/23730" target="_blank">📅 08:28 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23727">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qY3kVGA1ZU41DvmgyJC32iN3sqLm0nYcDtelBUjrB7mGK2Glvu-S4NVfJ9iNXGD7koATz2sbPGXQd4h9BCsLG1fQtBxWg5XuKEe8Bn7aLHf8e_pXrs-h7UXWkXj9vY-LKe9wFRtF_V54u5x0ff5D2Kj9W9IlEr90VHZToI59pWKiUP42ZNwo9iKYw7x058rtY2QuzsWKQdV3JFbeXslSYG1ZTB5L3568199bjYtLOdR9m5rArWdBTw-TDTuGlMWZeEbOFYsRg8pVxi5KARD-_CWzx5iKBhgMv_knpMS6-bJnZNjjEXQgyLENp7Pgem_PanjAHj69CrQmgo6ViaS_WQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇦🇷
#تکمیلی؛ نشریه مارکا: باشگاه رئال مادرید بزودی برای جذب انرو فرناندز به باشگاه چلسی آفر میفرسته. مورینیو برای پست هافبک اولویت اصلی‌ اش رو گذاشته برای ستاره آرژانتینی چلسی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.3K · <a href="https://t.me/persiana_Soccer/23727" target="_blank">📅 02:52 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23726">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/feUbUliWMKsco_UkZ8TJUzIrnAVGNpxvXx_LPbD2ec4IPGmCyuB21gtvp7ypjycGXFFeNXn2zHeVKeCN5BSn8LXjUd1vR5usliyk8fdN-LfGWt4SAnIW_iqxvdUlpgJJCM5-kmNbLD0EvIj7hOsnOk9jcNYTZ8HyHo0M1KZU4hY52B7nrs3rcSSg-TSavP_1iJFpuOcq8Pu4IRakzYJjEF19MsnXGQotMJGvUHAyKhtyWwFAltv0iMuOupntaN2BiClsxQDrTPZdFCqZRL5I16D7OJtQf_bwJCIz8RBti2QjlVJ47o3EdBRT7FBYq77Zc64rH_v3_eEGmpSb0Lv0fQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
#تکمیلی؛ محمد دانشگر به مدیریت باشگاه استقلال قول داده بزودی 18 میلیارد رو به حساب باشگاه واریزکنه و کار به‌شکایت و دادگاه نمیکشه.  قضیه از این‌قراره‌ویلایی‌که دانشگر خواسته بخره یه مبلغی روکم داشته که‌تکمیل‌بشه به مدیریت استقلال میگه کمکم کنید این رو بخرم…</div>
<div class="tg-footer">👁️ 45.4K · <a href="https://t.me/persiana_Soccer/23726" target="_blank">📅 02:15 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23724">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PzI0_TzxUzgepEFGuuLdKvCEjChktTDG4PqPkdXrhb6z00zY2T0U0jhbiARcsGDnwxeecnP1vmBYz7K9ubUra9m4Y-hHRHTqQuaq4Nsjm6q6e9_oVl5RBslmGXNt8yoLuqsKQILbhvUYcaEAQu4X_arQIr_0iWOy7fbE_SvjddWYkw_NTDO9J6W6C3pf9Y25_FAR_iiPMkj8DGo-AYgP6X-I6ofPXtT3rtJW5jiagzkDZ-9On-5rNqLBsJquj14TtKUfNnFU_pQyC-RSfL5HIhly6qcPHtuwdmyR21CNWVRtbKi8Lm_GLdErSIP-Ie7gtI4cGy37dlgb0ZflFiHwAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌دیدارهای‌امروز؛
ازمصاف شاگردان کارلوس کی‌روش با پاناما تاجدال یاران خامس برابر ازبکستان
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.5K · <a href="https://t.me/persiana_Soccer/23724" target="_blank">📅 02:09 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23723">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j2unjttuczK-oS0B7nGwnktb5wE5pwUPLhPYt-NofVmldETsqojGPrQKtf7k5HA3AQZWmQXM4JhcXnAhWIpR3au5vvkAybLYA_8i_WFpCRiBMgmKQw60UJivWhgl4M3YdxTe_kscplPXooEa_6CRSWhz_JNcXO7Q8Vh2Z0nYeTbiN6Zohf-rbHlc1A5ePLdoPjGW2YKK2gnEtXIca5EArFMXRA1EqqX62K6Zc9mVHT6qv1DMt6vnGoIBEjhGgqw2C_xrtgzsUFOzsZ7t30P-lq011qElPK2RWZpSGWnGoLXnJbCRuqZTJJSfxj5yVNnMp2y0cjTQp7d5SRPvzgt6Kw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌‌دیدارهای‌‌‌دیروز؛
از هتریک فوق‌العاده مسی درگام اول تانمایش‌درخشان‌سه‌شیرها مقابل کرواسی
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.6K · <a href="https://t.me/persiana_Soccer/23723" target="_blank">📅 02:08 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23722">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b735dd21e2.mp4?token=pHBU8yYeJZCa9bP8Vnv5_lqhjS6vgf8MUQa8nVHZA63oYOuW04hkioWSistQO-bJkl4WZ511Mi4BKfCoZptaW2i8_BpC_GM2t-jqlEWSxxn552Qbr6B8_EgHEwGs_w-31ojbDPlFPbtVJ_zXudtbpA600BsCqXdB8bQLG3y52uyBMVJ-zTg0MXckej5pW5TjElq6rxPqqa1P5tzhfOlkP9yb-DYts000gu1NdeyjiDno6kH9adlpu1TnehLAoHAUX9upCP5eqpdelACEmmPnjiU4XglwusO04xpDUxZPKbJHgwKayXs1-sfeBcT6wTQ4pZYzkg5Qc6Vajri8wdv6ag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b735dd21e2.mp4?token=pHBU8yYeJZCa9bP8Vnv5_lqhjS6vgf8MUQa8nVHZA63oYOuW04hkioWSistQO-bJkl4WZ511Mi4BKfCoZptaW2i8_BpC_GM2t-jqlEWSxxn552Qbr6B8_EgHEwGs_w-31ojbDPlFPbtVJ_zXudtbpA600BsCqXdB8bQLG3y52uyBMVJ-zTg0MXckej5pW5TjElq6rxPqqa1P5tzhfOlkP9yb-DYts000gu1NdeyjiDno6kH9adlpu1TnehLAoHAUX9upCP5eqpdelACEmmPnjiU4XglwusO04xpDUxZPKbJHgwKayXs1-sfeBcT6wTQ4pZYzkg5Qc6Vajri8wdv6ag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
فیروزکریمی‌پیشکسوت‌فوتبال:
بیرانوند درتاریخ بی‌نظیر است ولی لطف کند کمی تنگ تر از این باشد. این چیزی که ما دیدیم خیلی هم تنگ نبود واقعا.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/persiana_Soccer/23722" target="_blank">📅 01:58 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23721">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1e924ecdff.mp4?token=aApTWb_J8h9yd1uQCL_JoFsjizThP3tPMgU10kdpEveEYTl9wk_ZbUNmPsdD3Pm_kuOnPnnD0UCLBopyyhlKaT8IadvEUmnMKizBKOSB8G-bL-94hP9vJVXtbAQLVgRnTGyrv3UweJO3QDnNX2vWg1LsvVp1hlSeG1hcc9BHG1uQah9saZ1sxCcCfOFoaTXmIfli5vlQaH0YOLf1U-pH_JrhKzu1SXCLZVOWGE1bxK3rlhTKsgDUiu4OkTHl162AWTiA_OfzfAUfc3ua5bnk7zC3bkK_LoXXEWR16cxu0HuqTrisBKWdY6DbcJAXQtcpTXMWRsLRh5XNbWPZUJvwCQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1e924ecdff.mp4?token=aApTWb_J8h9yd1uQCL_JoFsjizThP3tPMgU10kdpEveEYTl9wk_ZbUNmPsdD3Pm_kuOnPnnD0UCLBopyyhlKaT8IadvEUmnMKizBKOSB8G-bL-94hP9vJVXtbAQLVgRnTGyrv3UweJO3QDnNX2vWg1LsvVp1hlSeG1hcc9BHG1uQah9saZ1sxCcCfOFoaTXmIfli5vlQaH0YOLf1U-pH_JrhKzu1SXCLZVOWGE1bxK3rlhTKsgDUiu4OkTHl162AWTiA_OfzfAUfc3ua5bnk7zC3bkK_LoXXEWR16cxu0HuqTrisBKWdY6DbcJAXQtcpTXMWRsLRh5XNbWPZUJvwCQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
ابوطالب‌حسینی‌درگفتگو بادکتر انوشه در برنامه امشب: باورتون نمیشه ولی من دوست دختر ندارم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.4K · <a href="https://t.me/persiana_Soccer/23721" target="_blank">📅 01:58 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23719">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/210b9e3441.mp4?token=aqxfTdfmgGU28uFeJwQiRv5b42pEzxZdTZ77NeO05NHPyvrJZsP2U_ADEmSO2G86RIeOisLfAW05hWj9rjuYiJKv54-oVWr0ozubLwNrNhU-gJfHSNWc7TYVOY4140qPDawTKToC2UWgsLRriL5C4Poqq_8y5HOxuIKjhiz20bGuZFiAphF4VYkbxlUrgabV_1L3kp-49vNyLBUyZAlpUPk4DPwRC8nOj31COmqE2OzfXlmuaA3tPeFE_XE0H3DZiNWfL_FLB2M_0xpagvgvONJfbWDmZkPN-74WuM7L6hw_ttX7HP2nTKm3CBdevq3LMWaB1N3msoN8Q5Txtd0JOg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/210b9e3441.mp4?token=aqxfTdfmgGU28uFeJwQiRv5b42pEzxZdTZ77NeO05NHPyvrJZsP2U_ADEmSO2G86RIeOisLfAW05hWj9rjuYiJKv54-oVWr0ozubLwNrNhU-gJfHSNWc7TYVOY4140qPDawTKToC2UWgsLRriL5C4Poqq_8y5HOxuIKjhiz20bGuZFiAphF4VYkbxlUrgabV_1L3kp-49vNyLBUyZAlpUPk4DPwRC8nOj31COmqE2OzfXlmuaA3tPeFE_XE0H3DZiNWfL_FLB2M_0xpagvgvONJfbWDmZkPN-74WuM7L6hw_ttX7HP2nTKm3CBdevq3LMWaB1N3msoN8Q5Txtd0JOg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
علی فتح‌الله‌زاده یا تام کروز در نقش ایتن هانت؟ وقتی علی فتح الله زاده در زمان سربازی فرمان آتش به جنگنده میگ 21 صادر کرد؛ فقط نگاه های پیمان!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.7K · <a href="https://t.me/persiana_Soccer/23719" target="_blank">📅 01:48 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23718">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">⚽️
هفته‌اول جام جهانی 2026؛ پیروزی ارزشمند و شیرین‌شاگردان توخل مقابل کروات‌ها درگام نخست.
🏴󠁧󠁢󠁥󠁮󠁧󠁿
انگلیس
4️⃣
-
2️⃣
کرواسی
🇭🇷
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.5K · <a href="https://t.me/persiana_Soccer/23718" target="_blank">📅 01:43 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23717">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X72e4RSy4xbRLM7THZHo1EJ3kJ5OqRxkhUfwTWYs4U1h1itFayAMB7bZwe31qFIOAGzQxucq-cezYxADMPyhh89e5CirHjUfF9Qxr_hR1G7lOVAcvwBdoOV4rjZf9PYerlD1BuHyHDgWQFhJ2MAZh-HQMJN6q5HmP5Gq_dkExfv_knybURDh9oGHx385KpRYBXqQjq-CV-2svlllynb4wjLs6hT5jSqKotBRS4CivhiJuBtcSW1rkhl5flxE4vExDIiCeoD31b54atNzW_9J6x6XyIgdp1ToVUUgro5l8YfnDkfQcvKCPrduW3zoliasiixktX8igYMaMIKG1gwitA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
هواداران‌تیم‌انگلیس پیش از شروع بازی امشب؛ برای ترامپ شعر ساختن، فیفا هم اعلام کرده هرکی شعرو بخونه از استادیوم میندازیمش بیرون.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.8K · <a href="https://t.me/persiana_Soccer/23717" target="_blank">📅 01:35 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23716">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5d2128a8f9.mp4?token=oJwtXHrq7c6XVeFAMdA3aMiLJO82OA4F7_wqH37WennKf8YLwR-2RHImlDXDFsA-5CA61DnCltDPa5xLMHbRCeYDLPuDNiZCLHYbXxVCUmbpns6N4t0mbqPccLulT0d9PLQRYqpmnVViMAPpDPv6YTxABWhjT7rsXGBQZxZNv9aIJH6tWyJw9_Rye0M2ZZXv8kNG--o95qH9Zq9eA7OE2vaZDAudDsnwPxBWi2Y8GjJfREHpoi460VuqZMAs33A2_qJ6udp6W_n2_PUxxLSxc8cTMqCTc-7E4Bxg_HrPt9wMfxxWc3vgD-9RHllUBGLXCVNYYDN9kyWBy2dlB2wvaA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5d2128a8f9.mp4?token=oJwtXHrq7c6XVeFAMdA3aMiLJO82OA4F7_wqH37WennKf8YLwR-2RHImlDXDFsA-5CA61DnCltDPa5xLMHbRCeYDLPuDNiZCLHYbXxVCUmbpns6N4t0mbqPccLulT0d9PLQRYqpmnVViMAPpDPv6YTxABWhjT7rsXGBQZxZNv9aIJH6tWyJw9_Rye0M2ZZXv8kNG--o95qH9Zq9eA7OE2vaZDAudDsnwPxBWi2Y8GjJfREHpoi460VuqZMAs33A2_qJ6udp6W_n2_PUxxLSxc8cTMqCTc-7E4Bxg_HrPt9wMfxxWc3vgD-9RHllUBGLXCVNYYDN9kyWBy2dlB2wvaA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
چه‌غمی‌داشت؛ یه‌روزی به‌خودت میایی می‌بینی دیگه پلی استیشن رو گذاشتی کنار و بازی نمی‌کنی
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/persiana_Soccer/23716" target="_blank">📅 00:37 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23715">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IY-mvxy-HqeVJ3eJZWnojIEvOnoTv4CFv94d8m_Ldd1dDb20sUdsvLAe4eUH-MsKqILoyxOp-RrlQuasbWSebfqlTsNGVGun3q4NbtqbBFaRcF6cEs7xWJdcNZbp6ZWQBIZcHNtnHAd0mD1RhAYGLncq9eFIO9NWPaLXGXueU-JyJB-WafoSMgfW09M8dEoBF2NIwuqPHIL7_M_K26_Q9BIUfN012XQ7sWP-Jyvu7nSh0HZd_Q21_jgknIRGyDiE_6LKEsuebTRr4CBP9ifI0VFsr72dXSiZsP2S2ZtlN6uGQAhyGcuKN_OJ597DwvvrSqa3pHxDVONcZXqtJuxNLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
هفته‌اول‌جام‌جهانی؛ شماتیک‌ترکیب دو تیم انگلیس - کرواسی برای دیدار فوق‌ العاده جذاب امشب؛ ساعت 23:30 ازشبکه پرشیانا اسپورت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.2K · <a href="https://t.me/persiana_Soccer/23715" target="_blank">📅 23:27 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23714">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K4u3XFT2oS2fMDh7wHCB7eMdBavQPzC9LmmuoSlo1ugeK5BGXeqNV9dv4qyI9BlIqRvisarYPxO8UVAZ50m6poIdFGofl5OnFYiPIc8-fIV5ZGG1BHwSj47J1bLBX2UlaAiFTF0WvTNQ_tRwOZWf2aWTovFRx9vI5UGqCmSYLMxdHj_CGsIwvUQk_hP-DUqNuS_OMa-x7xAUbukVj7-MkiUg0BVhaJSlUOhu7ikzqCXOpEWUmjPP01JqiXZdlmjsync2P-OICfiBuIjiqqG_NvWmromlvdZjRVlmgPmI8rZ5Lh_HNVdo7WN88CC9hYUQRxGnyPhKwbFFkFBihXTObQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🟡
با‌اعلام‌باشگاه‌سپاهان‌اصفهان
؛ آرش رضاوند و میلاد ذکی پور قراردادشون رو با این باشگاه تمدید کردند اما محمد دانشگر حاضر نشد به باشگاه تخفیف بده و جدا شد. رقم قرارداد دانشگر برای فصل جدید 170 میلیارد تومان ناقابل بود که کم نکرد ازش.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/persiana_Soccer/23714" target="_blank">📅 22:59 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23713">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/79c30d0c69.mp4?token=cLUtNF8rHTEuq_ks3Wdi-XD3_Ty4zKWgtXDX5TScdVps7THHRQmwKgZzn8eloGBIo0PaWnqTzFcr78hL5yi9jL0JVwOTUXD4J8dfah8Dp9F4nfPSPyLFZBs5fn7zOb49vU8QbdWam-s8FmRdyv1YoWL7GJunaScU2j3fa8tpD2njIClQlCpbmOOzD7A9kpwNfM8XtbzDFtB981Ljei5-FOcHnecCt08b_nvkfXsmBCsxnHUp91IrIKcJtwcUhU9kh4drTiRVzR-swt1amxXJ6b8ZGJPUs3UjCj8Soc5MSjm-1HClbdEvIxcSTa2vv5VoNK5Te493CRnClu80mfxNE2ADjetykGZG1PR2JXEMjZRqwXHjMFpPa-OlNE7AmhpD_cs3Ed0RBT9uQU3SVkxh_D6-Vwp8fItFZiSC36mTEv3t2p7OLCJegHXadJvSR6_KocvAHrq_gZdNkW2_NdunluhimrBo5YeyPCzETNfIFPGpwNyk5uMolZX1xIejKGNB-Vl0pr8qwHOfm0eMUBWH1PvbA_RgW2EY3YpBXuWU797P-jt9DgTZvSojTxbNUFyAj8EJqNG4qtRe7v8N0pkZWSTLwFhjtDlv9u-LPXX0J3kCLLCf9adtsLRRmLlq9MBr3BlMoflnfdvDpHNl2HrrosIL3O3a517N9f3MJgVzsak" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/79c30d0c69.mp4?token=cLUtNF8rHTEuq_ks3Wdi-XD3_Ty4zKWgtXDX5TScdVps7THHRQmwKgZzn8eloGBIo0PaWnqTzFcr78hL5yi9jL0JVwOTUXD4J8dfah8Dp9F4nfPSPyLFZBs5fn7zOb49vU8QbdWam-s8FmRdyv1YoWL7GJunaScU2j3fa8tpD2njIClQlCpbmOOzD7A9kpwNfM8XtbzDFtB981Ljei5-FOcHnecCt08b_nvkfXsmBCsxnHUp91IrIKcJtwcUhU9kh4drTiRVzR-swt1amxXJ6b8ZGJPUs3UjCj8Soc5MSjm-1HClbdEvIxcSTa2vv5VoNK5Te493CRnClu80mfxNE2ADjetykGZG1PR2JXEMjZRqwXHjMFpPa-OlNE7AmhpD_cs3Ed0RBT9uQU3SVkxh_D6-Vwp8fItFZiSC36mTEv3t2p7OLCJegHXadJvSR6_KocvAHrq_gZdNkW2_NdunluhimrBo5YeyPCzETNfIFPGpwNyk5uMolZX1xIejKGNB-Vl0pr8qwHOfm0eMUBWH1PvbA_RgW2EY3YpBXuWU797P-jt9DgTZvSojTxbNUFyAj8EJqNG4qtRe7v8N0pkZWSTLwFhjtDlv9u-LPXX0J3kCLLCf9adtsLRRmLlq9MBr3BlMoflnfdvDpHNl2HrrosIL3O3a517N9f3MJgVzsak" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚽️
هفته اول جام جهانی؛ توقف نا امید کننده یاران کریس رونالدو درگام‌نخست مقابل یاران گائل کاکوتا.
🇨🇩
کنگو
1️⃣
-
1️⃣
پرتغال
🇵🇹
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.5K · <a href="https://t.me/persiana_Soccer/23713" target="_blank">📅 22:37 · 27 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
