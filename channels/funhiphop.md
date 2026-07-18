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
<img src="https://cdn4.telesco.pe/file/ZUsz_fEF3Tt2LFt_LgOT9qr953nSkdOW5C5aytZwkl8HnqGj9QIbC8goSd_UIm7nqvjpgjqwj8ZwoywpH9h7OCDSe9-EatIAU72Qa722XJcm-p-6tvQPB_lbFKh5sxcRWVPoogtFj8kehQ58eKkBO1FJTIKFBdB3mm2R3aUD4SeHFWSO_cIBOMBgn8lnnMP5dYYgSZr4_dIgH-5D9sjT7RBLO-sClFLH8JNNZQem5tSCvCRzlwq4gtB18QbN2gimMv07UKFWEMXUJCPBy_6Wo02vSBxX5JYUB6c9qQPxULzVfe-yjW64KAsRHedz5xlT_Uw4uk5oXJSMkOPiWs_EyQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 [ Fun HipHop ]</h1>
<p>@funhiphop • 👥 193K عضو</p>
<a href="https://t.me/funhiphop" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 «قدیمی ترین اجتماع فانِ هیپ هاپی»🟡صاحب سبک🟡Tb :@FunHipHopAdsContact :@Chaman_Dar_KhakFollowing Copyright Laws©</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-27 13:40:51</div>
<hr>

<div class="tg-post" id="msg-80627">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">ولی خیلی حرفه بعنوان کسی که دوسال نتونسته تو لیگ کصشر بلژیک دووم بیاره به کسی که تو فینال لیگ قهرمانان اروپا بازی کرده و قهرمان آلمان شده بگی رانت خوار
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 1.86K · <a href="https://t.me/funhiphop/80627" target="_blank">📅 13:33 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80626">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">خوش اومدی به بلاد پاری
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 3.32K · <a href="https://t.me/funhiphop/80626" target="_blank">📅 13:20 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80624">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/31fa509f3a.mp4?token=NHq8r-kXNHaGbPfnEfObcIduaAqrAbS9A-nFKCGw79nyli1blbHZegAcTaTBqSYwMllIWVUfNL1d2dYk9lRi79fjujko88W1PbbJepjRqzUNDsgptyuBfdWF9S2vAqGM44HvEFlSPpwmvfCIWwafTuC7fgFDkcqo_c-Qz5RkDviBanj0DxOFjjkSIPYU3p_1_gQOWetOzfIbw-2t0MHiZMiS4PbE9CzTmv9UI5SGRBzfoPZG2VqzWFTjaqpoguVgf7nLA_S6nT-UjwSlrhSxMdDqbR2lrpNwiiiurglaeuXVQTFCuLwXgUpPYhs3OXMCOFgmll7mO984eMF-OjQzSzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/31fa509f3a.mp4?token=NHq8r-kXNHaGbPfnEfObcIduaAqrAbS9A-nFKCGw79nyli1blbHZegAcTaTBqSYwMllIWVUfNL1d2dYk9lRi79fjujko88W1PbbJepjRqzUNDsgptyuBfdWF9S2vAqGM44HvEFlSPpwmvfCIWwafTuC7fgFDkcqo_c-Qz5RkDviBanj0DxOFjjkSIPYU3p_1_gQOWetOzfIbw-2t0MHiZMiS4PbE9CzTmv9UI5SGRBzfoPZG2VqzWFTjaqpoguVgf7nLA_S6nT-UjwSlrhSxMdDqbR2lrpNwiiiurglaeuXVQTFCuLwXgUpPYhs3OXMCOFgmll7mO984eMF-OjQzSzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قبلا مسئول شستن ماشین علی دایی بودی بعد الان خودتو در جایگاهی میبینی که به اسطوره فوتبال ایران حمله کنی؟
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 5.09K · <a href="https://t.me/funhiphop/80624" target="_blank">📅 13:05 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80623">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NR-m5vvEbH_OVLH25WQHyDp8rBXGnMJIKdyR-dmLwOb9OhjbmIUwemsY4Y1mPDuBe3hZNnre4P9bl3z-WPo_SejDSCZ9lyYmvbgMYoD-cNaJJW91yxDPoDA8XoxvY7rz0D6nZ9n9D7LcfPWxUED3u8n7lZbQEofMlqIx6zm7EspjMojJhbqtlgtajooRq38Mq4tfpSlLMHXl_zIJmbkdEnzZhgFaBfIw8Ui9KJxKVGs0RWugKmhsLefpDtDwx4ToN9xGwBYzuGo2rPG8kkfiGxfxlbQ2wMJqCZCqK4G5w2XcSFBzaVzCCCR81dxy4VnwJboxcVFthenIZ6GMpobgmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">باخت آرژانتین قطعی شد، دریک رو برد آرژانتین بسته.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 6.5K · <a href="https://t.me/funhiphop/80623" target="_blank">📅 12:49 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80622">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">سخنگوی قوه قضاییه: برای ترامپ و نتانیاهو پرونده قضایی تشکیل دادیم و کیفرخواست اونا صادر شده.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 7.83K · <a href="https://t.me/funhiphop/80622" target="_blank">📅 12:16 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80621">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fbfbfbbd0e.mp4?token=JGpNp-d4oPnVwm9zWTfQO197T2drDkcTJndkp2djekqizxXuGwk7gzFZ1LR8TF5a1YBmqVQkyqjtqK2gDh94PdRrHtsP8NmPwyIdk8u-cudNZtRt0e_wXtPqEpRiD0SeFEPuUXqUm5wNH7nI6YulzrAioWrULIKA7nZ8QX47gjuhinnqo36oeah18M94l3PZEatAuYngXIVXzq_sMFkyAzHa7gmZPLyMyVmk6ZJgSlSmK7DdsWJGOzGQt7_OPN67-DlH5zps12dGPjO1qZN_lEf-jT5LXxuF3pI9xVpliXhAdjMLuORvfiBjiR7ZTUcfL7Ky0JlTl6bWEFVi_3pJ4A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fbfbfbbd0e.mp4?token=JGpNp-d4oPnVwm9zWTfQO197T2drDkcTJndkp2djekqizxXuGwk7gzFZ1LR8TF5a1YBmqVQkyqjtqK2gDh94PdRrHtsP8NmPwyIdk8u-cudNZtRt0e_wXtPqEpRiD0SeFEPuUXqUm5wNH7nI6YulzrAioWrULIKA7nZ8QX47gjuhinnqo36oeah18M94l3PZEatAuYngXIVXzq_sMFkyAzHa7gmZPLyMyVmk6ZJgSlSmK7DdsWJGOzGQt7_OPN67-DlH5zps12dGPjO1qZN_lEf-jT5LXxuF3pI9xVpliXhAdjMLuORvfiBjiR7ZTUcfL7Ky0JlTl6bWEFVi_3pJ4A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تشکر پرسپولیسیا از علی بیرانوند برای استوری های دیروزش.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/funhiphop/80621" target="_blank">📅 11:35 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80620">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oSG_bvbZ6BqwyAMPvELeG5K3VWmo-yD6wAH5sHm8dw-FEKOfqB5RpFuq5j211xorOgDmfcoDOc9gNFis2-Bks_Iufuc7WeltDoS6-OiV_qFj5wmV7WhEXB0iTWBi6VjVTpJnSroHOIHAi5WPcMQckHeuSXJ5fdjIQnNC-B1MIz7M_LuIoCAip-lfdcmtgVCheBXNWnVmf8EyiDX3uVMgzgPgile8_nSst2Y4euvY0q7KEVbXGuzN9a3Nrps88ce3ltrQBFd1I2y2OL4clJmdotykFjWUmo67grSRijsKwjV2wYUTIOUy5MQ8FImsI64uLM-ogzpVKh1ejeeZvkLCLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگه تو یه کشور نرمال امیرمحمدو میکرد میفتاد زندان.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/funhiphop/80620" target="_blank">📅 11:14 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80619">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Nue1yjE0e97TnNMSWKY3hEw6uf1MFOgXrLNm7hoUpYT-Hku4iv0kvIzaufT0mDVuGrHH3Q7w7tntE4fGLQ4MryjXdpKTqkxZJyDG8uB4OgVBftn6E41ixIxy290hZRLhaT1t07-zwQzx9v35O71LygW3xH7XVbJ3xVzCX0XoWvbNKNkpyPslD3V0j3TtP13m4slJSff3t6y5vsE1m2Cjint_wBKm3v3keFF4eqJ3pBI0rbNLzOXf5ZHcBiMbMGGfy-COjG8iAKyB3vFYEJQSngSSdD-yvvyd1r-dn3OZE92KmByghpBRFk5LCz5UqS1CKly9KT9aEnS8on81bP6GOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
فرانسه
🇫🇷
-
🏴
انگلیس
🏆
رده‌بندی جام جهانی ۲۰۲۶
🏆
🕔
بامداد یکشنبه ساعت ۰۰:۳۰
📍
ورزشگاه میامی (هارد راک)
🎲
با بیش از ۸۵۰ نوع آپشن پیش‌بینی
⚡
با بالاترین ضرایب پیش‌بینی
✍️
اطلاعات و شرایط بازی:
- فرانسه در مرحله نیمه‌نهایی با یک نمایش ضعیف، با نتیجه دو بر صفر از اسپانیا شکست خورد.
- انگلیس نیز در مرحله نیمه‌نهایی در یک دیدار دراماتیک، بازی را با نتیجه دو بر یک به آرژانتین واگذار کرد.
- برنده این دیدار، مقام سوم جام جهانی را کسب خواهد کرد.
- با توجه به قدرت هجومی هر دو تیم و عملکرد دفاعی ضعیف در نیمه‌نهایی، گلزنی هر دو تیم گزینه مناسبی برای پیش‌بینی است.
🧠
وقتی از بازی لذت نمی‌برید، متوقف شوید.
👍
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
🟢
دریافت سرورفیلترشکن رایگان
🅰
27
💻
@BetForward</div>
<div class="tg-footer">👁️ 9.65K · <a href="https://t.me/funhiphop/80619" target="_blank">📅 11:14 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80617">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H1XXXusMSgb1BFu91oABhtS3CqTaLcXtT97EspLbk5NgjWZLlOTXbpyXp0KBcDL7dvOgjR0TxHuw-U7m5FLYAoG1OTjwKgNVH3vusPUl_KxLEMMGAEeGhNsVyC7qvYLOr8Ec2sRgCwPZPZeEoTAWPcdZsvjKbQxyD8shyjPAssZT7sv61WMGW-gGqJi5wCMYPHEepdqyTKHz4GS4Ahw42Nx7SRw-Z7jGxswtisAFG0Z98H0lb88H19sbJwB767uf8oNLvLslxyaxD2Vuu3GWJ8oofvg7YASEijaWcyGi9oFufRUoJCZ_EwqiUYRpdlZ2F0GD9IcnjkrLW3GS_icCOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تیشرت ایمان صفا تو ختم مادر عمو پورنگ.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/funhiphop/80617" target="_blank">📅 10:30 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80613">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XOlSa64LfnS1neMlpi7l4hVrl3EoGZX6r8IXvlWfFnVtaC10aYGEV3J0UEkakA9y9FQH9w_-w3hhAnBR84B-Cqw7MhQrDAPzBwFmNPjLnj2I9lQL9bZNE0BfSGWhd2vscklDnEXuFPtg_cWvqEuJjzjQDj0FkrmNwvhsxVCr1f3ea-HdTsWadmVYsopdPdG53yYEa4seyOec3gXYZq7rzCA6Iru_YAeDlIY9IOHvXUAeBnV9XU4AHD2lmR3rQsMaT51KTPCgpZxceViq97W0TusVvMQQAFYto7ZFAUGoj9pHVA123O1GiKv2gSaUMAdtR3WE_z3YBt2TpNqWs1TiBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بیژن مرتضوی قراره تو فینال جام جهانی بین دو نیمه اجرا بکنه
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/funhiphop/80613" target="_blank">📅 04:10 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80612">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">از الان شدت حملات کیری میره بالا گفته بودن بعد تعطیل شدن مارکت جهانی (3:30) شدیدتر میزنیم
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/funhiphop/80612" target="_blank">📅 03:36 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80611">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">پایگاه الخرج عربستانو زدن، محل نگهداری سوخترسان‌های آمریکا</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/funhiphop/80611" target="_blank">📅 02:30 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80610">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">روزتون چطور گذشت؟
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/funhiphop/80610" target="_blank">📅 02:08 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80609">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">نخندید
ترامپ
: امیدوارم یه روزی برسه میزبان مشترک جام‌جهانی آمریکا و چین باشه
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/funhiphop/80609" target="_blank">📅 01:38 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80608">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">حاجی این قرارگاه خاتم الانبیا که هی میگفت اگه اسرائیل حمله به جنوب لبنانو تموم نکنه میزنیمش چرا تا الان نظری راجب جنوب خودمون نداده؟
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/funhiphop/80608" target="_blank">📅 01:35 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80607">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/278e4b296b.mp4?token=Pet_CoJPV2iXWd0gTL_5S0yeK5FymoyOPIOiBHSU_SC1hq4qPRnd5U8ohnwVzdIJtrpwcmF-7uDAesUgFq54IacphgzL2kNfEOi3-0gy9g6vRc4nE0kLmplZZq-SJwg15ofMOh-RUeY09CzR48RnsxMoAm2996Jtprs2e97e-b_Nz6sL8Vckl8w6Oo0JyCkEzCtiCzsWcC8Uuz_qHzc1zuQzyuLXdvJ1GHj6MI7ilepgD7iJQI9LXRj232KWiJKYZfVa_K5-LDzvXPKAQw1kyNjGeCCtdCGzmTRnwdTi7Qy_v222gLbSBDzgsFGC2cNyRCy1-YmbAOLwTyb4iCcPbQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/278e4b296b.mp4?token=Pet_CoJPV2iXWd0gTL_5S0yeK5FymoyOPIOiBHSU_SC1hq4qPRnd5U8ohnwVzdIJtrpwcmF-7uDAesUgFq54IacphgzL2kNfEOi3-0gy9g6vRc4nE0kLmplZZq-SJwg15ofMOh-RUeY09CzR48RnsxMoAm2996Jtprs2e97e-b_Nz6sL8Vckl8w6Oo0JyCkEzCtiCzsWcC8Uuz_qHzc1zuQzyuLXdvJ1GHj6MI7ilepgD7iJQI9LXRj232KWiJKYZfVa_K5-LDzvXPKAQw1kyNjGeCCtdCGzmTRnwdTi7Qy_v222gLbSBDzgsFGC2cNyRCy1-YmbAOLwTyb4iCcPbQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">استانداری هرمزگان: تا الان اصابت و برخورد پرتابه به بندرعباس گزارش نشده و صداهای شنیده شده احتمالا از منشاء دیگه‌ای بوده
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/funhiphop/80607" target="_blank">📅 00:59 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80606">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">حداقل نهایی دانش آموزارو کنسل کنید این همه عذاب و استرس نکشن.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/funhiphop/80606" target="_blank">📅 00:47 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80605">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">انفجارا داره نزدیک تهران میشه، دقایقی پیش صدای چهار انفجار تو یزد شنیده شد.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/funhiphop/80605" target="_blank">📅 00:40 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80604">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">گروه BTS تو کنسرت جدیدشون به این شکل یاد جاویدنام های عزیز رو زنده نگه داشتن.  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/funhiphop/80604" target="_blank">📅 00:33 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80603">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PSuc0HdYcmBBHYxWGyk-jAl1Jke4WcgGdOjeNRoOXnZytZ3g6RsaUwV332u5mmmdy0QVRH6ixRDIO4_8I4HEsn0OWY-3KrjmoEOHLqyxFLDg_cC-UMEAtq4G9s-4brMBedoNuDse7lA6qkdRdTT1oJ6SA4uUotlaNh0bZL-yYQ40bTMb4jYFNu7q_7AnSgHBnZGC--bc0_nVFjCinW6ghLWHyjkRIaaKow7uF0Ihqj2aSSgAWbXGYKLoA-StV6aGSy78iqpZqVpYIZf_kOTWK70pCnP9DhTZ9zeACY5Y-rKNupeA2F1hDzA7I-T_NgCRDGOElBdbbOiz0ZQyrUmYXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گروه BTS تو کنسرت جدیدشون به این شکل یاد جاویدنام های عزیز رو زنده نگه داشتن.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/funhiphop/80603" target="_blank">📅 00:23 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80602">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j4zuxoXwDs7RdXfF4oMya0vyZQGzFA58e0lPKxuIzcGh3P7b1rx7WA_ARaSFPLacCCJqRMMKYLM9PnFj7FNGl1tG0veSOtRxXuXf48WNcwCfDIYQ3loHBOo3qqDNRc-NP242c1CjLQTfnXHx0CUT1CQxo0IQak_EX1IUMalHcXD4ZF3m3uxAyD0MQd6uMvCEnYZOcKQX8B4azbhXCMkicVZ2DxucNDt2llFEEHPQiGMhTEAnJ0bNfSn5D3IG_3xDhDjzYQBwZWCeH6lBqfwz_vpwmQ0i_4Ynqe2eCtc13wIPOdpCoNLxOKEnFMD38Q7w6D14k6wDdbkM7M1YbBqiGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">علی بیرانوند شرمنده زنت گرمش شده بود مجبور شدم.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/funhiphop/80602" target="_blank">📅 00:02 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80601">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">امتحانات تا الان چطور بوده؟
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/funhiphop/80601" target="_blank">📅 23:51 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80600">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">موج جدید حملات آمریکا شروع شد.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/funhiphop/80600" target="_blank">📅 23:34 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80598">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rmVqpYEXs9oUta-ru_VeXfsKhyi6YIQKYRz4CHTLwUqoTdFb2JW-SdhhyQ7f7_HMqXWrlX5g-QtiCHfQpLUEnyCSKurmkCI705rC73txFaLZrOuqpK_tEb7NJtcKxkQta9ChIcdhvv_I43stc_kXbmpn3zzSBg66E5jB6zO8dbV0WtTr4h-m1cQChyAYJnHDUjMvkQ6lSEa5ojeaYF6WMaSEgIOJQohbB61gIPwzHzS8jgTcOJrf4xhxqE5HnhM_7uUq4uukyTezuPSwKYVxwIlJaH9bGabdqpe_ro-98uMn-B7ipKCw0xBzq-gRBX02tTTxqViRoJJsRCHVH_j6ww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/k2aBSmSOQcPXQLAF5N8VyCmkjS0k9v5kDiyRuLC5VGUTFWY4GXUb2mvrTP3hAL8z0sXXUhOEeITktb2QvAQe0O4vMK7OkpW7xyMIQJBr25ox-HDC9rSUR9GPeUI2mKEAKqjAJeWrMTYPJ9CCRTmYIBVMG0ixarHICQMB45CW-viTFO2lxApwuf-CGxZA5FtQghnAjGT6wPr03XlEiTqbQ_Idx-XtKVE9ow3Tw4iYOc1E_B8JC-IIly4gmEpfYL_ewHfIZkGpshawTGTNplxHIF5OYDgd9GRcaiB5X8Y6tQnl-X5_twcJYzdyBuXF3j3qiNCbiFrWuy1VcqDT-IhqEA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">کیر علی دایی تو کصمادر همتون
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/funhiphop/80598" target="_blank">📅 23:12 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80597">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">یه روز ادمینای فان هیپ هاپ پست رپی میذارن یهو میوفتن میمیرن
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/funhiphop/80597" target="_blank">📅 23:07 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80596">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">رسانه عبری  از جنوب حمله زمینی اغاز میشود ناتو و نیروهای کرد و اسراییل و کشورهای عربی و پاکستان نیز وارد میشوند  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/funhiphop/80596" target="_blank">📅 22:44 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80595">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q5_8TILePR-0_aCnazZOjHs4l4j8yzwoI7uD1V8z-ZoNnqSdoE8ihXYn2jLDGkfQF6_7VcW0j1oLoUhqgT744WU7IFvK1Gw9P5a5ih-_pFLU6fpO-pQ4U8oP8uS-nR4sKnOxfsQkU_zZewH0UxTaSrFLwNlQVzGUaynkSkH6IAYFKY6pA4z_sztxvKpsS8DxuBRupjQOnvZsnLhqrrOiD081I9D42qtVHCPe9VvQ4WGbkimBV3ez_93IxKRvB2OzngkqpheaCYIJ9WYBQzte6nYR9gstibmXq1O3CThfaOO7dYaCr41XqQxcjBQQI79YE8eYR03VRnMHPJPVO0CUPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رسانه عبری
از جنوب حمله زمینی اغاز میشود
ناتو و نیروهای کرد و اسراییل و کشورهای عربی و پاکستان نیز وارد میشوند
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/funhiphop/80595" target="_blank">📅 22:43 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80594">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">توماج شیر دل، پسرِ اکثر مناطق ایران به جز نصف جهان.   @FunHipHop | Nima</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/funhiphop/80594" target="_blank">📅 22:40 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80593">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/280efc03ab.mp4?token=krJlWSR6C2n_ahwqmh_aHbBV8KylYUuH30Ra5QZo3xMgbghVlHvNs0CAcUYV5LteW44d43W09ji3LFzHu7XZnsbhmq-PSXGzlCzx4LwzcvFzh2upLabdfQT5oL2_KMn8jP8VxgRGNMJFENyTmdO56SxBNCnOvIX2DiB2hJiyLQ3etAqxDRqpcnnPDukqSf8BBXWPMbs5q7FiFD9DfBkpMLO9eX2Ll_lqonfnfbhLZt0nUytzFsP-BO25I4xtr9VNCMP4MwRJuYpeZHiH7WAc-3TSGdGk80CWepLaKCmgLyeSMEq9MiQPzxoXjxHMHS49w6_X29a2PR5KEqFGK8IQGg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/280efc03ab.mp4?token=krJlWSR6C2n_ahwqmh_aHbBV8KylYUuH30Ra5QZo3xMgbghVlHvNs0CAcUYV5LteW44d43W09ji3LFzHu7XZnsbhmq-PSXGzlCzx4LwzcvFzh2upLabdfQT5oL2_KMn8jP8VxgRGNMJFENyTmdO56SxBNCnOvIX2DiB2hJiyLQ3etAqxDRqpcnnPDukqSf8BBXWPMbs5q7FiFD9DfBkpMLO9eX2Ll_lqonfnfbhLZt0nUytzFsP-BO25I4xtr9VNCMP4MwRJuYpeZHiH7WAc-3TSGdGk80CWepLaKCmgLyeSMEq9MiQPzxoXjxHMHS49w6_X29a2PR5KEqFGK8IQGg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">توماج شیر دل، پسرِ اکثر مناطق ایران به جز نصف جهان.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/funhiphop/80593" target="_blank">📅 22:31 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80591">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">اگه خدایی نکرده زبونم لال یک درصد اتفاقی افتاد خواستم از همین الان تاکید و یادآوری کنم که این جزایر ما خواهند بود که سربازان آمریکایی رو محکم درون خودشون جا می‌دن و به عبارتی به اسارت می‌گیرن.  @Funhiphop | Nima</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/funhiphop/80591" target="_blank">📅 22:04 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80590">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">اگه خدایی نکرده زبونم لال یک درصد اتفاقی افتاد خواستم از همین الان تاکید و یادآوری کنم که این جزایر ما خواهند بود که سربازان آمریکایی رو محکم درون خودشون جا می‌دن و به عبارتی به اسارت می‌گیرن.
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/funhiphop/80590" target="_blank">📅 21:54 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80589">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tCOI-6mh5NjwFoAy0c6dGx8TU8ZkKvnmwwLKzLValIilSmLgHDBdyukcJMEf7R5RuQ3nrmL-hzgr24yYAfl1pKK0SVF7OzlvnfR7Lfa8PorebW-WlqVJNysc1F4kyd2I0Zrne6B1DCg-ceQwA8uG-J1fvPgS23ZV14MLdYsNHE4oRllz0nM--DZBlfCKsG-0M1O6jwqqmySK7Y6q0XyhnzUqxrXtyIE51sPNGy8V6I5FkvlRlFaIYQ9NzDZCipIX3cBLSub1vRjCdorGDn-wZRMZGoWYCZcyKCsRsfTk9GFfygn7h-rfPHoHs_VfB2ga07LNM7CIXJutup5c_0gynA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آقا رامین هم رفته بوده اسپانیا ساشا سبحانی رو ببینه.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/funhiphop/80589" target="_blank">📅 21:44 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80588">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OVy12dwy5xUangYBqZ4y4ZDTlSNxCJAamcm5kGqGKxkHCeMgppLtjSNZFBHaP0g9UWFpcfJw2Xt3S6iHeqGeGU77xjGRKJPB950QO0rGB2BQ9eGaSf1zi4uAjxkzWvIKmeAwCPQDDYpYPJIm-9eUQTqCW9NeHSaFRfg1bjHhxI2yQRrSmgbNInZmEmlwRLbXy8rb-JFqV1L934ftgWuqNY8YiRM1BAPrS38FCtfrAcI8dhZKmVwo944HkkRbOqNVC0swCm1QA7QJs6ODwb8XjMiz2Yu_gPQWb701IgkBlhqqbi5KdbUBjzBHnStrvdcfDfxD-gBlbrTc-j63eLEjyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آمار برنده توپ طلا ۲۰۲۶ رو یه مرور کنیم.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/funhiphop/80588" target="_blank">📅 21:24 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80587">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromHappy Smile VPN</strong></div>
<div class="tg-text">🔻
HappySmile VPN
🚀
🔺
فوق سریع
🔹
فوق پایدار
🔻
بدون لحظه ای قطعی
✅
متصل با تمامی اپراتورها و نت‌های خانگی
🔺
تمامی سرویس‌ها آیپی ثابت هستند.
🐱
مولتی لوکیشن واقعی در 7 کشور
🇩🇪
🇳🇱
🇦🇹
🇫🇷
🇸🇪
🇬🇧
🇺🇸
🚀
10 گیگ --->
❗
فقط
40 تومن
🚀
20 گیگ --->
❗
فقط
79 تومن
🚀
30 گیگ --->
❗
فقط
118 تومن
🚀
50 گیگ --->
❗
فقط
198 تومن
🚀
100 گیگ --->
❗
فقط
388 تومن
🚀
150 گیگ --->
❗
فقط
578 تومن
🚀
200 گیگ  --->
❗
فقط
768 تومن
🟩
تست رایگان
♻️
ضمانت بازگشت وجه
✅
خرید فوری از طریق بات
👇🏻
✅
@HappySmileVPNBot</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/funhiphop/80587" target="_blank">📅 21:13 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80586">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">از دستاوردهای آخوند اینه که بندرعباس و جزایرش از جایی که همه آرزوشون بود توش زندگی کنن تبدیل شده به جایی که همه ازش فرار میکنن.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/funhiphop/80586" target="_blank">📅 20:53 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80585">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GXjdlwnONUWFRcRkJBd3YtvGY-C3j3Juj9IX5tkJDK7Gvhuyte_UqcCeJZ7pnYEKT4Sp3ki0wl36zq-f_3Z1rFcBW6lAInx7WRfEc0MgnUVaNNKPku7K9q4fRKJf9y0RT4TwFrpXkldhJC2PW_VUcB7sgclrxEjij7Xg99mfbgbD3uS6gHVkQN_ptXvURaag2opBpRoWZYSa3-gv9KBC7tj74HuixEcIsZhD3qQZ6t2JpypOYDDncBnYoY7_PlrY2sNFUv_pFztDCawJPLpTN7sdAnkHSaYs33i-wJwk5SXa27Ivgo9SS2wcbHoZHIP7LVK3N7_cZBllwEwAhz6KPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حالا که بحث حمله زمینی هست برید فیلم warfare رو ببینید که بر اساس واقعیت هست که تو عراق محاصره شدن   @FunHipHop | Taymaz</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/funhiphop/80585" target="_blank">📅 20:25 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80584">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iI3RfsWHgLymxSgdgqCn4J6z1a-PnBI1llwa-Ej7sS2hg8SvSMB5G6swVtvuNxCMFgm3ZzWf0rU6CglYT_xHr0dxo3G1EGadfA0LFuDFI1OGuyNeXX_qMUgpKewW_sNqDK36Si-E-fUxMGf_EQnzChrQC_0vzsI6KOWtaSwqEMx-KILR57vOoNwInyrcidDsKiDpD3RfcUbeG0faMqSlTE9jCHsY0cknThhcQH9wr39XkTziDg_NH1HHYskchJpWW0tqd-1gYjQt2pg-lwNPUUwzU9AwA95GPA7Gv45L82ttF3nenGu9QVfll-jPrIEyGF0LQZxtrGfGVZ89FxkLYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حالا که بحث حمله زمینی هست برید فیلم warfare رو ببینید که بر اساس واقعیت هست که تو عراق محاصره شدن
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/funhiphop/80584" target="_blank">📅 19:57 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80583">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">رویترز: پاکستان به جمهوری اسلامی هشدار داده که اگر به عربستان سعودی حمله کنه، اون رو حمله به خودش تلقی میکنه و وارد جنگ میشه.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/funhiphop/80583" target="_blank">📅 19:38 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80582">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">علیرضا جی‌جی چرا دست از سر رپفارسی برنمیداره، بمیر دیگه کصکش
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/funhiphop/80582" target="_blank">📅 19:27 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80580">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XW_9riKSnKUvK13WvtyFAihjTQwqnj1uwTzvxgbKUk3_uV7R7MqWHz92V08uo8BHDRrJowJ3-6LdTmsE854pCVus14-9yQvBKfS5z4FsiIy9DispWyGtHm73eLbZrBPRbno5QlSsJGPzJhv7wp5f2t1698vEKwuiaJi4bUoOmySmbR2nya6LocaHQZA2ZXFQSGAPJLN8mDDJoVdcWlpfCo4DpWo_pT9WkB5vCuJNLK1XxCPqgJFp5perSQ0E4rR8vXmTA8JU4Xa_nphjrRtiOWCP12KL1o69KaRum2XHzjjW0VzugMx_CcpH8x0F0nxpqKdW9rr0SFGiur5FsL7siw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/3d51fa3abb.mp4?token=GmxfHqEEhMcUZsv6qGl4DRZO-6X9Br17TsVYHpPugHf_PS3Zo_W6yXaEoh07aiAA4yeE4FHlBLKb-jx1mDvCow8RnGu-8eiMprM9h3zGOZ0HHoKYfCO8iif0kECQUzVYRByE2UvJn4UeCv_RiFsk1wTY6bj_JH2zmh5mBTlZGFPDI4zAAQE2gRvXjan3BAmzMJYZa7nZQ3ZuSd6pdqDj9qiS0peJ4QnLWHr1wrkliYBr-4_Jh-1K2cKhxp8tgAOtd1gdyofMzWsyAhtDPObebPd5_u0bylTqSmpsebfKoh6UnDgVnm4fEtW69iEaAvH_bulBFNIVMYTIFzsAhdOcCg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/3d51fa3abb.mp4?token=GmxfHqEEhMcUZsv6qGl4DRZO-6X9Br17TsVYHpPugHf_PS3Zo_W6yXaEoh07aiAA4yeE4FHlBLKb-jx1mDvCow8RnGu-8eiMprM9h3zGOZ0HHoKYfCO8iif0kECQUzVYRByE2UvJn4UeCv_RiFsk1wTY6bj_JH2zmh5mBTlZGFPDI4zAAQE2gRvXjan3BAmzMJYZa7nZQ3ZuSd6pdqDj9qiS0peJ4QnLWHr1wrkliYBr-4_Jh-1K2cKhxp8tgAOtd1gdyofMzWsyAhtDPObebPd5_u0bylTqSmpsebfKoh6UnDgVnm4fEtW69iEaAvH_bulBFNIVMYTIFzsAhdOcCg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">توی تبریز یه نفر بخاطر اینکه کل پولشو رو برد انگلیس شرط بندی کرده بود و باخت، خودشو از طبقه ششم انداخت پایین و خودکشی کرد
.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/funhiphop/80580" target="_blank">📅 18:08 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80579">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V_VuomEpJXl_PzaJjNwzY0eMv3pG1UZHynylcdLfoKN7VUgvahRso1lCGLUiIHKcvPQ0AffgTiGGkGFokcYuseMnZp-3hUG_AWUt7CmD-h21BPCoVm8Iz-BAsakntD4ifAw54zNLFqJZjO0BAQnWNkN334ibq7fzHQPuQW0oq6WHQmK44fbyryaIEIdWgDbVW3hvhI3mdhzbHYzYUsP4XkAcnQXSY29IzVFbzBZlKeMKyKf09XZbi95LgB5aYKhBRAannYLYAH-e-2uGXrZAnPc3sjieB1_ch1nymwdVH-Y4mo_7njNZeml21VqKVLPibo3XeOujNvh-4IyoIlq4ag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دسخوش
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/funhiphop/80579" target="_blank">📅 17:37 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80578">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f1d29960e9.mp4?token=n4rJF3zP6Gmwk-wLeEfEMAuMZLUB2J9Oh5I9_60QffF1tTheDq9hufP8rZWZ7UGt9r7a-9ZXYWVKSIZ86w0KZiZ2J-vmQPNO71-sdGvRREiFOyc1mYImNUwRLaXFtlzNDdHCIIO5qLHzLhDw8RtbZ-o7DDVsXLs9bVPYsrotoDTN6JDhtT_0jA4KsvjJMDdiQSTiUfKz3Ulg-YeckEXLL8ZKmLymCOIfxMIujnkUMmbmqLIdDQGc-bcfyiMTZNXDFhhctBDygOXRDJoYJM08H_U_1dTsPKpIvRHz_W9S_1wFKDXARkZY58wRFC10QVuVkdRKZARNEPQ6fT6GACRoMA04YrQwDmqMOFPPPZ-RyeRKumOXNlhZfUJDo9oTNLbVqTp3ALLdMFATYbfRMEzRWLUm-cyEU7P8K-Ia7IEyAMDndJxKJ7hAKloBsgv2uHOVfaOhPd9cAGwEJWO5yQ0ostG2iOO05Fl8NLDSm68mSqDx9E5XLmd6TI6q5N5YVULUkMrNYPsJAu89cabnCwfVokR740EhT6wzKKViAT0zxrXLyP9vSgkDlS8Ak97sgFdNgG_8hEZPQHzN3-ysKqCMs-0AR3xTygcax8zKCQZUwdl2G2_iHNmcbKRtpk5rUcHBDlEbSn1ARsaoj_PC7v1FdrYrA8omHpMOUegMkVq4n7I" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f1d29960e9.mp4?token=n4rJF3zP6Gmwk-wLeEfEMAuMZLUB2J9Oh5I9_60QffF1tTheDq9hufP8rZWZ7UGt9r7a-9ZXYWVKSIZ86w0KZiZ2J-vmQPNO71-sdGvRREiFOyc1mYImNUwRLaXFtlzNDdHCIIO5qLHzLhDw8RtbZ-o7DDVsXLs9bVPYsrotoDTN6JDhtT_0jA4KsvjJMDdiQSTiUfKz3Ulg-YeckEXLL8ZKmLymCOIfxMIujnkUMmbmqLIdDQGc-bcfyiMTZNXDFhhctBDygOXRDJoYJM08H_U_1dTsPKpIvRHz_W9S_1wFKDXARkZY58wRFC10QVuVkdRKZARNEPQ6fT6GACRoMA04YrQwDmqMOFPPPZ-RyeRKumOXNlhZfUJDo9oTNLbVqTp3ALLdMFATYbfRMEzRWLUm-cyEU7P8K-Ia7IEyAMDndJxKJ7hAKloBsgv2uHOVfaOhPd9cAGwEJWO5yQ0ostG2iOO05Fl8NLDSm68mSqDx9E5XLmd6TI6q5N5YVULUkMrNYPsJAu89cabnCwfVokR740EhT6wzKKViAT0zxrXLyP9vSgkDlS8Ak97sgFdNgG_8hEZPQHzN3-ysKqCMs-0AR3xTygcax8zKCQZUwdl2G2_iHNmcbKRtpk5rUcHBDlEbSn1ARsaoj_PC7v1FdrYrA8omHpMOUegMkVq4n7I" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏩
کانفیگ فیلترشکن و پروکسی رایگان در ربات بت‌فوروارد
🎲
🤖
با ربات رسمی بت‌فوروارد در تلگرام، تنها با چند کلیک فیلترشکن پرسرعت (V2ray) و پروکسی تلگرام رایگان و امن دریافت کنید و بدون محدودیت به اینترنت آزاد دسترسی داشته باشید.
🚀
سرعت بالا و اتصال پایدار
🎯
کاملاً رایگان
🔓
دسترسی سریع
👍
برای دسترسی به اینترنت آزاد و بدون محدودیت، به ربات تلگرام بت‌فوروارد مراجعه کرده و سرویس مورد نظر خود را فعال نمایید.
کلیک کنید
@betforward_bot
کلیک کنید
@betforward_bot
🅰
r27
💻
@betforward_bot</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/funhiphop/80578" target="_blank">📅 17:37 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80577">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">توافق اونقدر خوب پیش رفته که بزودی هزاران شهروند آمریکایی مهاجرت میکنن به ایران، فقط لباس نظامی تنشونه.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/funhiphop/80577" target="_blank">📅 17:22 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80574">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">لاپورتا چی گفته باشه خوبه؟ گفته اگه داور خود فروخته نباشه اسپانیا قهرمان میشه.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/funhiphop/80574" target="_blank">📅 17:08 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80573">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">ولی بارسا جدی بین اینهمه کون بچه به دوتا بازیکن با تجربه مثل رودری و لاپورت نیاز داره</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/funhiphop/80573" target="_blank">📅 16:40 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80572">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">نقش من تو قهرمانی یورو و فینال جام جهانی اسپانیا با پدری تقریبا یه اندازه بوده
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/funhiphop/80572" target="_blank">📅 16:25 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80571">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r5He9t0ToTrtgOXyZN7mm1Hu7eaOuVr8pf6fcJf6fGh7uBv_m3NqIsWxqfb8fytdyH20-IRmpdAD2e_YOXpNSnNH6odMIOYfAG-Jxxxozl8gx_1OosJWnIfIxKXej_jw3IpDq0ySNfconXi44pXjL9mPKXGQRaFChJtwSiYF68qrb0c2cqHN71ab52ReBH3gMSK_OSJP3h1MpzV9FM-jC1rBlDjaSnhYnBlChqZ27clYnJUO2kqprmYGsthoaZNPC_5hlzQo78w76Cb6AS9dpam5r16RiDBfui9n-hT0Akqwh4MMWKon23QgPtX6mFNvQVuFyO0q9xBXv-vGPqyhoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عکسای مسی با بازیکنا کنونی بارسا یجور عجیبه انگار واقعا خودش پدرشونه
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/funhiphop/80571" target="_blank">📅 16:04 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80570">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">باز خدارشکر این اتفاقات جنوب پیش اومد، وگرنه این وسط بازا لال میمردن
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/funhiphop/80570" target="_blank">📅 14:54 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80569">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">کل زندگیتونو ببندید رو حمله زمینی آمریکا.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/funhiphop/80569" target="_blank">📅 14:24 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80567">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">قیمت دلار هم شده 190، صدشو بزار تو جیبت ی نود بده بهمون تا آخر ماه پست میدم.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/funhiphop/80567" target="_blank">📅 13:32 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80566">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">لغو عضویت جانفدا جز بیشترین سرچ های گوگله در حال حاضر.  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/funhiphop/80566" target="_blank">📅 13:18 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80565">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">پخش جومونگ شروع شده؟
اگه شروع شده لطفا ساعتش رو بگید
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/funhiphop/80565" target="_blank">📅 13:08 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80564">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oQLYU-jgAV80IxRyuJP-RQrb1RWdn6Vcle7k6hAQSVEFWC4m7osJSbywTmdwYtb_mlWchpYnnk-3snOdrse6AqDZv44rNO_NsjxhwC69zPcg8UwXBhkyMmLfdQQ_mxol6psTxvAiP52vV0OPiE9AIEemeUQO7m9eeuZs4spYnyE6ziv_ep7EVTOLq9gOEAHVC00tSxpFyXmfvxteNEAkF1hN4hYEspslaum7P8WZAtMx08DNtr7uQ7J5DuCFK6A14zJ2mgTNVkAwgMgoIhQxJKPc5TL7TUXxHdE1gXvBsGRfIL9QhsmolnUmooQn_LOxEecEyn4xAeazZlI4R8l1cA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">@Funhiphop
| Jenayi</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/funhiphop/80564" target="_blank">📅 12:19 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80563">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KHDASrdZqB6yt70M9w3n5E8SUEyAJffTQvY2BN4ipTd8TDPHTGoSAEOSQqTvNM7Lh8bSoPwOpf3uLbaRWDEXOsqHjRUVj1WEqbrvjgM-DAE6wTKredU-dbAQzmo09pNKP0ZYp4eu8XwDd9NmRoC6fLzi8-I3nh7gwsr61d2Q_cRNa5p5oNGBVYsnoeZwUVQyIZCBsAk6FPUh6nZpbX9kMMfiDDZ4PCyVPGy2IS8BKZa-ge_X8MaFMC74ozs7j4FydlUOIWw155i5m_VRlCXRtzvK6Sf6v2RJelXV8dDd5VVR3ecDrlti69gfMWXfnk2kqI9HVtRowt3l02AXU0KGKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تنها راه شکست آرژانتین در فینال جام‌جهانی :
@Funhiphop
| Jenayi</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/funhiphop/80563" target="_blank">📅 12:16 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80562">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f1d29960e9.mp4?token=n4rJF3zP6Gmwk-wLeEfEMAuMZLUB2J9Oh5I9_60QffF1tTheDq9hufP8rZWZ7UGt9r7a-9ZXYWVKSIZ86w0KZiZ2J-vmQPNO71-sdGvRREiFOyc1mYImNUwRLaXFtlzNDdHCIIO5qLHzLhDw8RtbZ-o7DDVsXLs9bVPYsrotoDTN6JDhtT_0jA4KsvjJMDdiQSTiUfKz3Ulg-YeckEXLL8ZKmLymCOIfxMIujnkUMmbmqLIdDQGc-bcfyiMTZNXDFhhctBDygOXRDJoYJM08H_U_1dTsPKpIvRHz_W9S_1wFKDXARkZY58wRFC10QVuVkdRKZARNEPQ6fT6GACRoMC_Q2H7Ams3m2s7eynwMvoiSBqnvLtJzlzvpDztjhvGRmWajpGfpP-bjm8ZAFW2JksPI4vbTQW0kPl_Qxr0SNm9-JSuzHVw2VQWKmqyARC6lrqa6rCaOKcbVsDRMxSVIBwQBhhW9V27RnV_ohrkIowHZt4XyCQI6zOHL0-ypvGMngvg7ePuRd46_mkwxSPB0kSFP8ma3EuisOSfLqb3WI-dodcRgCYdrV6yvH_FZWpKYgUrr0rPH7mmbRJqZqtCdgl4y9Nw8FQWEeS3S12VANxZ_YeLMOnTKuPap0i9dtIGPvfIsG0UMalFgACQW4I4NsrNoe2YBS9itYEWNvkx2uKU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f1d29960e9.mp4?token=n4rJF3zP6Gmwk-wLeEfEMAuMZLUB2J9Oh5I9_60QffF1tTheDq9hufP8rZWZ7UGt9r7a-9ZXYWVKSIZ86w0KZiZ2J-vmQPNO71-sdGvRREiFOyc1mYImNUwRLaXFtlzNDdHCIIO5qLHzLhDw8RtbZ-o7DDVsXLs9bVPYsrotoDTN6JDhtT_0jA4KsvjJMDdiQSTiUfKz3Ulg-YeckEXLL8ZKmLymCOIfxMIujnkUMmbmqLIdDQGc-bcfyiMTZNXDFhhctBDygOXRDJoYJM08H_U_1dTsPKpIvRHz_W9S_1wFKDXARkZY58wRFC10QVuVkdRKZARNEPQ6fT6GACRoMC_Q2H7Ams3m2s7eynwMvoiSBqnvLtJzlzvpDztjhvGRmWajpGfpP-bjm8ZAFW2JksPI4vbTQW0kPl_Qxr0SNm9-JSuzHVw2VQWKmqyARC6lrqa6rCaOKcbVsDRMxSVIBwQBhhW9V27RnV_ohrkIowHZt4XyCQI6zOHL0-ypvGMngvg7ePuRd46_mkwxSPB0kSFP8ma3EuisOSfLqb3WI-dodcRgCYdrV6yvH_FZWpKYgUrr0rPH7mmbRJqZqtCdgl4y9Nw8FQWEeS3S12VANxZ_YeLMOnTKuPap0i9dtIGPvfIsG0UMalFgACQW4I4NsrNoe2YBS9itYEWNvkx2uKU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏩
کانفیگ فیلترشکن و پروکسی رایگان در ربات بت‌فوروارد
🎲
🤖
با ربات رسمی بت‌فوروارد در تلگرام، تنها با چند کلیک فیلترشکن پرسرعت (V2ray) و پروکسی تلگرام رایگان و امن دریافت کنید و بدون محدودیت به اینترنت آزاد دسترسی داشته باشید.
🚀
سرعت بالا و اتصال پایدار
🎯
کاملاً رایگان
🔓
دسترسی سریع
👍
برای دسترسی به اینترنت آزاد و بدون محدودیت، به ربات تلگرام بت‌فوروارد مراجعه کرده و سرویس مورد نظر خود را فعال نمایید.
کلیک کنید
@betforward_bot
کلیک کنید
@betforward_bot
🅰
r26
💻
@betforward_bot</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/funhiphop/80562" target="_blank">📅 12:16 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80561">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">الان این کصخل با همین توضیحات میزنه انتخابات میان دوره ای رو لغو میکنه</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/funhiphop/80561" target="_blank">📅 04:57 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80560">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">اون وسط گفت ایرانم تلاش میکنه انتخابات آمریکا رو دستکاری کنه که همین که اسم ایرانو شنیدم پاره شدم</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/funhiphop/80560" target="_blank">📅 04:53 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80559">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">یسری مدارکم منتشر کرد که انتخابات ۲۰۲۰ و انتخابات ونزوئلا دستکاری شده به وسیله چین و تکنولوژی هاش
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/funhiphop/80559" target="_blank">📅 04:52 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80558">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">سخنرانی امشب ترامپ ربطی به ایران نداره، میخواد راجب تقلب انتخابات ۲۰۲۰ حرف بزنه  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/funhiphop/80558" target="_blank">📅 04:50 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80556">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/auh7rDPao7qRyGrFlH8Rdpxg83C3k9aSTpNSOVhczd7iT63MMVqOfgsA104mHCl98r9KCicdoHbF2lBDFg__Ers4Bs_LLU10DnXe1HSk2X4dz42-RDnYA3kJs2BFe_aCRhiJLUf1oIskw5AY_t4Yx5HPJkyJv8vk_8qnnSgiyV0MdCXrfzldAOOmETA2Uu4r5ZUO30y4Ba11eqsTpHRpJEvKS3H6k2ANGr5eqsgG3gHHRs2BMU_6Ng9p0CGzFDNtAeAXmuZJE7xQiCo_WbYM4YslvobktWjOPhBIxs4dmxWSCwpsmQW2qRueQgqdTfmE9mpLvQuUmfoq_uwXp4khlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DjGXYvnOU44Vu7r4BcLSKOe2PhAW1zaiZtr4J-__40YmK0d2WhS-3dpcLKYIAgYwtMrWt1K1EX0zULY3wuZWZLHB1MTnqlbh0mb_oEN7qglzeFM33gYEOPxCBImPJlPIY30eOebNG288749hiUg0sCN07TqfNoJZi-MH86iLdrG_p4iCWmx0rGYKM6WK0y-nc32QR8PzSkOGR2VlhGSKnPr5GFJOb3t6Qu9xJpkVWaentukkieAFXyj7tchXt7wveqEkyXFdfrn6lEbVDPuL2-4yUf-UA41ElAOxWn9vpkzhl7Fp6KPvIqwaC_mM1OIPyUL4Jq6l_GNTASqffuwb4g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">متاسفانه فینال و رده‌بندی رسید به این دوتا کون بچه، فغانی هم کلا به دنیای داوری گودبای داد قراره کارشناسیو ادامه بده
@FuunHipHop
| Mmd</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/funhiphop/80556" target="_blank">📅 03:44 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80555">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">لغو عضویت جانفدا جز بیشترین سرچ های گوگله در حال حاضر.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/funhiphop/80555" target="_blank">📅 02:58 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80554">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">تنگه رو وا نکرده پس فرستاد</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/funhiphop/80554" target="_blank">📅 02:57 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80553">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">عراقچی رفت مذاکره</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/funhiphop/80553" target="_blank">📅 02:55 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80552">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">شب جمعه خود را چگونه گذراندید؟  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/funhiphop/80552" target="_blank">📅 02:24 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80551">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">پیت هگست وزیر جنگ آمریکا: ایران کنترل تنگه هرمز رو در اختیار نداره.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/funhiphop/80551" target="_blank">📅 02:14 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80550">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/186980592e.mp4?token=HrtqNrjBakYmaXCvGGBBqrUJxTqVSjlda7EK6GGCYzRZHk9H-Siwe0kkgWy42vMPG5zSDrJRNgZjAhnMSa7_p-6sLr-3Lltcl16Yz8vwN1Zs5q3DVuUQ4dHgFMdEidlWRhtBkOr2ZpQ9WVmESuyGPV6UvX6wkh8S5c_J6S8y90JaZaJUwQrYWXGledJUoQd66s_nSNEPv_ADCY6GprRYjrHXybTU5206prapzM27VLqnfUX_2fHwBgvuUuOIWHzORzx4eOAaSvANESRxk1hK8WcEehvHnm73KoXLq0K84b0NiBGUpkUyRYeume8lAdRA3JPSK4K6sFfS2UYvUfdljg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/186980592e.mp4?token=HrtqNrjBakYmaXCvGGBBqrUJxTqVSjlda7EK6GGCYzRZHk9H-Siwe0kkgWy42vMPG5zSDrJRNgZjAhnMSa7_p-6sLr-3Lltcl16Yz8vwN1Zs5q3DVuUQ4dHgFMdEidlWRhtBkOr2ZpQ9WVmESuyGPV6UvX6wkh8S5c_J6S8y90JaZaJUwQrYWXGledJUoQd66s_nSNEPv_ADCY6GprRYjrHXybTU5206prapzM27VLqnfUX_2fHwBgvuUuOIWHzORzx4eOAaSvANESRxk1hK8WcEehvHnm73KoXLq0K84b0NiBGUpkUyRYeume8lAdRA3JPSK4K6sFfS2UYvUfdljg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حملات سپاه به کویت.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/funhiphop/80550" target="_blank">📅 02:07 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80549">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">اگه نتتون ضعیف شده وی پی ان عوض کنید توهمیا، فعلا خبری از قطعی نیست
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/funhiphop/80549" target="_blank">📅 01:58 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80548">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">نتتون ضعیف شده؟
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/funhiphop/80548" target="_blank">📅 01:52 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80547">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">سخنرانی امشب ترامپ ربطی به ایران نداره، میخواد راجب تقلب انتخابات ۲۰۲۰ حرف بزنه
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/funhiphop/80547" target="_blank">📅 01:46 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80546">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">به لرستان هم حمله شده
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/funhiphop/80546" target="_blank">📅 01:40 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80544">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">آقای جلیلی یالا پل بساز</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/funhiphop/80544" target="_blank">📅 01:29 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80543">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">آقای جلیلی یالا پل بساز</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/funhiphop/80543" target="_blank">📅 01:27 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80542">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">سازمان ملل بخاطر اتفاقات عادی خاورمیانه ناراحت شد و گفت تا اطلاع ثانوی قهرم بای.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/funhiphop/80542" target="_blank">📅 01:23 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80541">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">راستی تا وصلیم بگم کیرم تو نت بلاکس، از این اسم دیگه متنفرم.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/funhiphop/80541" target="_blank">📅 01:15 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80540">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">حقیقتا میترسوم</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/funhiphop/80540" target="_blank">📅 01:12 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80539">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">آمریکا یکی از نفتکش های ایرانو با هلی برن توقیف کرده.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/funhiphop/80539" target="_blank">📅 01:10 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80538">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">انفجار ها توی جنوب همچنان ادامه داره، ساکنین جنوب مراقب خودتون باشید.  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/funhiphop/80538" target="_blank">📅 01:04 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80537">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">انفجار ها توی جنوب همچنان ادامه داره، ساکنین جنوب مراقب خودتون باشید.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/funhiphop/80537" target="_blank">📅 01:01 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80536">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">سجاد پسر تا نتارو قطع نکردن پول ویناکو بزن.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/funhiphop/80536" target="_blank">📅 00:54 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80535">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">خطرناک تر از ناو آن جنگیست که اینترنت ها را قطع نمیکنند.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/funhiphop/80535" target="_blank">📅 00:50 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80534">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">بابک زنجانی میخواد بمب اتمایی که از پاکستان خریده رو کنه.
بابک زنجانی: تا غافلگیری دشمنان چیزی مونده، صبر کنید.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/funhiphop/80534" target="_blank">📅 00:45 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80533">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">هدف حملات امشب جدا کردن ارتباط هرمزگان از بقیه ایران بوده، هرچی پل و خط ریلی ارتباطی بوده زدن   @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/funhiphop/80533" target="_blank">📅 00:39 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80532">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">هدف حملات امشب جدا کردن ارتباط هرمزگان از بقیه ایران بوده، هرچی پل و خط ریلی ارتباطی بوده زدن
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/funhiphop/80532" target="_blank">📅 00:37 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80531">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">قرار بود زمستان سخت اروپا شروع بشه ولی تابستان کیری خاورمیانه شروع شد.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/funhiphop/80531" target="_blank">📅 00:33 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80529">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">یادش بخیر ی زمان چند نفر بودن میخواستن با ی سطل آب آمریکا و اسرائیلو نابود کنن.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/funhiphop/80529" target="_blank">📅 00:27 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80528">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">خط راه آهن بندر عباس مورد اصابت سنگین قرار گرفت
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/funhiphop/80528" target="_blank">📅 00:23 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80527">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">یه پل تو بندر عباس زدن که یکی از مسیرهای مهم ترانزیتی و لجستیکی جنوب کشور بود.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/funhiphop/80527" target="_blank">📅 00:19 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80526">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">این عاقبت 47 سال مرگ بر آمریکا گفتن و ایدئولوژی خودتونه، بیخود گردن ما نندازید.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/funhiphop/80526" target="_blank">📅 00:15 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80525">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">آمریکا هیچ غلطی نمیتونه بکنه ولی همه غلطارم اون داره میکنه.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/funhiphop/80525" target="_blank">📅 00:03 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80524">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">خب سی میلیون جانفدا، الان وقتشه، برید جنوب از کشور دفاع کنید.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/funhiphop/80524" target="_blank">📅 23:58 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80523">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">تسنیم: آمریکا شروع به زدن زیرساخت ها و پل ها کرده.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/funhiphop/80523" target="_blank">📅 23:55 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80522">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">فرودگاه ایرانشهر بلوچستان هم زدن.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/funhiphop/80522" target="_blank">📅 23:34 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80521">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">جنوب رو بازم دارن میزنن.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/funhiphop/80521" target="_blank">📅 23:15 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80520">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">از اونجایی که دیشب تهرانو زدن، الان تو جنگیم یا آتش بسه همچنان؟
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/funhiphop/80520" target="_blank">📅 23:00 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80519">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AlANE7Z_jgDtaCiiQ8WOiuPtmoCYMfRTaqnS2ognsNCfY7hVjJQlR_1s-f3lkL1wTWruzxeqfVRt-qx79_dZ5uUlrb-yN_7yWwnFsiYotmNyU6YE3FXcLrg43u99Ph63jl9OhRBtZjKeRjxKD7jtXrWmHz-i0wJlvj__7UnIHqXFlmM9BaRLt91HYsP8LeJfvT4c3WCLLo9AYs4r3_MmuS0XKPSEDio9s7HtpNuiuVDDsEmrbDsU4smNH8fyoQruQzcyHzlUulcD7I1S7fq8-kZHFtpPo5zAwh20OrY2VGYgZl6BeDcJkdmtjkT-jZvI6NoGbZBajn9amTI3KTc29g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😂
😂
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/funhiphop/80519" target="_blank">📅 22:43 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80518">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">اهواز
@FunHipHop
| Rea</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/funhiphop/80518" target="_blank">📅 22:35 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80517">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">با اعلام سنتکام دور جدید حملات علیه ایران شروع شد</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/funhiphop/80517" target="_blank">📅 22:04 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80516">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mw0PJOwPGa7M8eYtHgof85RBxiEAPUCUtP5VeDwceTNcPSZJwM4GqsO6oQ0pDoI0UPspdNgBoUywu2LOZHdcx2GYgjWHdcx14j6Xky4LGNGtgRWQaAZ1hydu60IwKyOK6TYxFz6F8QrLyH_VA-ZBZgWxtBsL6LqOI-UeshOZJ3GJMJ4MItsINg15Syg_SFXJtbXgU1WZCrZrX6m1RRwKnfZHeiMvx883XrxHxiiO9STcg-y2kE49AdJc_FgdNUgZP0SpB7U70ZMWzUHXxl15tRLUV9edqj_WlZbHGzO9-I4HY7gR66snxNTKuQY3TCQp52_nZ-Mhe7c92EQlIN11kg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترک جدید ویناک به نام کارام هیته منتشر شد
YouTube
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/funhiphop/80516" target="_blank">📅 21:00 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80514">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">همان همیشگی (انفجار در بندرعباس)
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/funhiphop/80514" target="_blank">📅 19:31 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80513">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2f999836d6.mp4?token=OVy_PO6Ghm1JBwNg3MwsRLyQSdtMKRcxeRotyM4Qi-2U5-GJp8jkag6Km9FKta2xBe9WgoAjnX1hpXdeOtzM5c5gN6Cp7Rt9R9Tap7zEhh_qvwPSLzsEV0WUldZs7tHArRZvNEjlbb3Sk-W45MclPP_4-JZ39ZLd1gwy5FrRBPPqEGWYrsxGaoARiv0FIL21BgI7mt5HyRC0R93tKRql3sWThsplJQfcSqbMjZRFz9-hkGqMsIPE9--LVdmx7GMP6YgslJgl0LUFWg8MwmphWAyzsBnBYEACXr9SawkisSdEOssAae6zDFD4NC9n0O9ZJkl9QUDoB3rjIfrV6eNTxQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2f999836d6.mp4?token=OVy_PO6Ghm1JBwNg3MwsRLyQSdtMKRcxeRotyM4Qi-2U5-GJp8jkag6Km9FKta2xBe9WgoAjnX1hpXdeOtzM5c5gN6Cp7Rt9R9Tap7zEhh_qvwPSLzsEV0WUldZs7tHArRZvNEjlbb3Sk-W45MclPP_4-JZ39ZLd1gwy5FrRBPPqEGWYrsxGaoARiv0FIL21BgI7mt5HyRC0R93tKRql3sWThsplJQfcSqbMjZRFz9-hkGqMsIPE9--LVdmx7GMP6YgslJgl0LUFWg8MwmphWAyzsBnBYEACXr9SawkisSdEOssAae6zDFD4NC9n0O9ZJkl9QUDoB3rjIfrV6eNTxQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محسن رضایی: مسیری که در ذهن آقامجتبی هست، بهتر از مسیری بود که شورای‌عالی امنیت‌ملی رفت.
مجری: چه مسیری بود؟
محسن رضایی: نمی‌دونم.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/funhiphop/80513" target="_blank">📅 19:19 · 25 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
