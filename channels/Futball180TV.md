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
<img src="https://cdn5.telesco.pe/file/nsTl0sBdmqKtcYk2XxsvZzO3MDGr_0MmKNM2vPW6cUdNGivhTgOpC3D2O9WdMpTfXkxdy_X_3YHCtxsg9MGjBc_AITRIpG0fpJeWJ7mJa80CHfXAosuk4tpgCaSW7YKyE2NIkkcL-37f-ZrqH_ROAk3NZfOmFsd-8ZR9MiVuRYefRGDilIMXPobAyyzMr7v_s4K9Kee1rYPETDpAyThQnwZwL1tr3HwJky8Ha9xBUCaCRkSux18tdJ5eD-sgN8wDLjdy913hrksyJkDjR3PoHvJ-fy1cy65iog5x31JFVW67Udi9RmYhYdAGnOB6Ga3IiNbPV0NyLyF4p0XI5j3AVA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 جام جهانی 2026 | فوتبال 180</h1>
<p>@Futball180TV • 👥 584K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-26 06:23:54</div>
<hr>

<div class="tg-post" id="msg-93547">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sylKtHLY-bB-TFghTSW6pR7tJaAFLDeeC3Jb1R8QpXcigZ4GW0ySV50bbDSVX8-xRVRvC1fkLfPeW6WIRowkw_0azSd5xDMrgaoNAbEN6bdABhofKQIopimeg82Dg5P7puizwJFBKQI-WocRjIlJTu8LajmVUO5U4OGBhJ2Id8glWSSddxN57KIsIp9tvabwOlQC5Tx0A6LoabjKWjZN4PG1kSBOmyBEVENlFYXSigHNuB3K7yqNClvahcteutmWo0zjWL0umh_JrSr0nACsqoDA0v_8FukHe50bpB6aQtP2_XSSI00-0eun_nQeOPPm3Q6CekXj7JVRcP9yQdb_mw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
#
فوریییییی
؛ به دونالد ترامپ اجازه داده خواهد شد تا مانند جام باشگاه‌های جهان، جام جهانی را هم همراه با تیم قهرمان بالا ببرد.
🔺
عجب قابی بشه بالا بردن‌ جام‌ توسط قلعه نویی در کنار ترامپ
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 1 · <a href="https://t.me/Futball180TV/93547" target="_blank">📅 06:25 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93546">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">علیپور هروقت توپ نزدیکش میشه فرار میکنه
مرد حسابی آوردنت بازی کون بدی پس؟</div>
<div class="tg-footer">👁️ 13 · <a href="https://t.me/Futball180TV/93546" target="_blank">📅 06:24 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93545">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ftQNLAfbnk6LE_9WHmWtMFKvvOUXiT5PTBof5zRud6R8fhov1rCsPA0gnOtXVEc7gebEHQfONa2iqkRADV76BA-FvE9pQYAa98NS_U_vvGua3q2ygk6iEAzIaVjNvg_51cUQYC7hQPz1VZhdS-l3R3ABJ8MFCh5LJcVsBVeQPm6_0wIhktcXurDPA4JSvLnsgyoIrkuIasXf-Sp5Te33XJ2VMQuPl3Arv8pI59tA_CEO7vYmDWVOQ-1oXjcP84Z5cdbDlXjZwIYtSRc9gSVkLdh64IVEflshOOougOF_clinFzqZHhpWrp3nfSnkudo6dQAiM39P8wHcs-drMK4sYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به دستور شخص اینفانتینو نمای کلوزآپ یا همون نمای نزدیک از تماشاگرا تصویربرداری نمیشه و به همین دلیل برخلاف بازی تیم‌های دیگه که تا نوک ممه زنا رو هم نشون میدادن این بازی نمای نزدیک هواداران ایرانی حاضر در استادیوم خیلی کم نشون داده شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 2.02K · <a href="https://t.me/Futball180TV/93545" target="_blank">📅 06:23 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93544">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">عزت‌اللهی ریددد</div>
<div class="tg-footer">👁️ 1.02K · <a href="https://t.me/Futball180TV/93544" target="_blank">📅 06:22 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93543">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">الان دقت کردم اونایی که پرچم شیر و خورشید دارن هم بعد گل محبی خوشحالی کردن
😐</div>
<div class="tg-footer">👁️ 2.03K · <a href="https://t.me/Futball180TV/93543" target="_blank">📅 06:21 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93542">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">دو دقیقه پاسکاری کنید چی میشه مگه
😐</div>
<div class="tg-footer">👁️ 3.04K · <a href="https://t.me/Futball180TV/93542" target="_blank">📅 06:19 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93541">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">‏با اختلاف بی کیفیت ترین بازی جام تا اینجا این بازی ایران و نیوزلنده. قشنگ هر دو افتضاحن.
کریس وود پشت محوطه استپ سینه کرد، با سرعت ۰.۵ چرخید، سه بار زد تو سر توپ، ۳ دقیقه فکر کرد بعد توپه گل شد</div>
<div class="tg-footer">👁️ 3.07K · <a href="https://t.me/Futball180TV/93541" target="_blank">📅 06:18 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93540">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">طارمی بازم رید</div>
<div class="tg-footer">👁️ 3.08K · <a href="https://t.me/Futball180TV/93540" target="_blank">📅 06:17 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93539">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">طارمی بازم رید</div>
<div class="tg-footer">👁️ 4.08K · <a href="https://t.me/Futball180TV/93539" target="_blank">📅 06:16 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93538">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ovesz0bc8CjRoI79sMSwZtBKd68nn83ITLWfoeoI0OZqX8G2zpt3SLeG6Utc8sowuuq2pqosUeAEAxbOJofDo1AadJUXR2QF-GVgVg2TGH2JHG5Iwlctt_cqjSBi_Xp8THxFZw8wsoqUQblFMVJ1IedtaKz5eAG9euCCgc7CmFzDuyw7Jt8D--GMKFTT_z5ZHYoIS9zi7dh2p2h_yr_CDMD9dTT_9R4gmwF5WxUkX6Pd0sIOCTYVp8ERaTGaz7anMtfFjs5UEmGCyOXAys-MTDEi4dxDjS2c_jwxSKRNmVwHDE9gzTU2Wes805AUTvcFu6mvEeX3sHjbFcvLjVfitA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سکوت میکنم که این سکوت منطقی تره
😛
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.09K · <a href="https://t.me/Futball180TV/93538" target="_blank">📅 06:15 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93537">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">هافبک وسط نیوزیلند بیشتر بهش میخوره ورزش کبدی بازی کنه تا فوتبال
😔</div>
<div class="tg-footer">👁️ 4.09K · <a href="https://t.me/Futball180TV/93537" target="_blank">📅 06:14 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93536">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YFZM2KQrUw-DEZx0o4S4Zs_3rjB_L0PskDebtFD8VfhN5HlxbrSxQhd9tV_xhvLc1GouMd0DzjxkW7obQg_pZMu9DnFpOpdqky7QAgNgrz7H7p-V5GgGzPJF7TYCYa2a-qcdy4qzFp2AIbzMCB3bEyT1incL1UPFFov7FOCGLfl5FYC2-yTYvoz8o7HCtk-BVgVV3bbVPEVstjohcOijWeRLjavum1FcLQ1kavn8lnbjrlLIM1Lg3KAEujkVs2Q1PXclKDKLKv2ql-TpjmvHv30IuyKcC_Rxv3Sp_4R06Mm6Axeqf_3Q97yeim2Jl7W8w4rcyKa3l0M0_WHYJs-XFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✔️
کوارتسخلیا مناطق جنگ‌زده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.1K · <a href="https://t.me/Futball180TV/93536" target="_blank">📅 06:11 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93535">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">اینقدر اختلاف ساعت کیری زیاده که ایران صبح شده اونجا هنوز شب نشده
😐</div>
<div class="tg-footer">👁️ 7.13K · <a href="https://t.me/Futball180TV/93535" target="_blank">📅 06:07 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93534">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">نیوزیلند تعویض کرد</div>
<div class="tg-footer">👁️ 7.13K · <a href="https://t.me/Futball180TV/93534" target="_blank">📅 06:06 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93533">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">رامین‌رضاییان یه حرکت دیگه بزنه تو تیم منتخب هفته قرار میگیره</div>
<div class="tg-footer">👁️ 7.14K · <a href="https://t.me/Futball180TV/93533" target="_blank">📅 06:04 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93532">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">کرنر برا منتخب ایران</div>
<div class="tg-footer">👁️ 7.13K · <a href="https://t.me/Futball180TV/93532" target="_blank">📅 06:04 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93531">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">حاج صفی بجا قدوس اومد</div>
<div class="tg-footer">👁️ 7.14K · <a href="https://t.me/Futball180TV/93531" target="_blank">📅 06:02 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93530">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/118bebbcf8.mp4?token=OyI7aEgfT0Yw3l-zHsnGgdbUyCuB6KBQfoMJyPJWC0fDWwK-5H2gy3PskywNHwKhTt84gjYToULuFSmCX83dZrWiVUAsois3C30VaNjcjYUW92RIqBkGwxQuqA4x-0w95LyAIoZG9S45MtjrPzOYFpNaailsnGR9-fvk0VF6FJtUutrdoYvYi4b8us_FhYWqTqpKDXE3v3rPWNH2foX4R1ASLN9Q0ghpjjrl3Rv1Z1UftyHneFgv2_Q7fwy7qW_GBvSqfVGtKoy2u57tN9dXRfVmoBAVPehkIS95BUfn8-Y8VaHMJj5ggLt0woVjgTU0d6kFCmfR7B9IloOP-kckpQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/118bebbcf8.mp4?token=OyI7aEgfT0Yw3l-zHsnGgdbUyCuB6KBQfoMJyPJWC0fDWwK-5H2gy3PskywNHwKhTt84gjYToULuFSmCX83dZrWiVUAsois3C30VaNjcjYUW92RIqBkGwxQuqA4x-0w95LyAIoZG9S45MtjrPzOYFpNaailsnGR9-fvk0VF6FJtUutrdoYvYi4b8us_FhYWqTqpKDXE3v3rPWNH2foX4R1ASLN9Q0ghpjjrl3Rv1Z1UftyHneFgv2_Q7fwy7qW_GBvSqfVGtKoy2u57tN9dXRfVmoBAVPehkIS95BUfn8-Y8VaHMJj5ggLt0woVjgTU0d6kFCmfR7B9IloOP-kckpQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
گل‌دوم منتخب ایران به نیوزیلند توسط محبی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.14K · <a href="https://t.me/Futball180TV/93530" target="_blank">📅 06:02 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93529">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">تعویضای بعدی رو بذارید بگم بهتون از الان  حسین‌زاده و دنیس درگاهی میاره بازی این دوتا هم کسخلن کاری ازشون بر نمیاد بازیو میبازیم
😛</div>
<div class="tg-footer">👁️ 7.15K · <a href="https://t.me/Futball180TV/93529" target="_blank">📅 06:01 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93528">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">محمد محبی</div>
<div class="tg-footer">👁️ 7.15K · <a href="https://t.me/Futball180TV/93528" target="_blank">📅 06:01 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93527">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">گل‌دوم برای تیم قلعه‌نویی</div>
<div class="tg-footer">👁️ 7.14K · <a href="https://t.me/Futball180TV/93527" target="_blank">📅 06:01 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93526">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">تعویضای بعدی رو بذارید بگم بهتون از الان
حسین‌زاده و دنیس درگاهی میاره بازی
این دوتا هم کسخلن کاری ازشون بر نمیاد بازیو میبازیم
😛</div>
<div class="tg-footer">👁️ 8.15K · <a href="https://t.me/Futball180TV/93526" target="_blank">📅 06:00 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93525">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">این مهاجم نیوزیلند شجاع رو گذاشته رو کیرش میچرخونه</div>
<div class="tg-footer">👁️ 8.16K · <a href="https://t.me/Futball180TV/93525" target="_blank">📅 05:59 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93524">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">نزدیک بود سومی هم بخوریم</div>
<div class="tg-footer">👁️ 8.15K · <a href="https://t.me/Futball180TV/93524" target="_blank">📅 05:58 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93523">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">واااای</div>
<div class="tg-footer">👁️ 8.15K · <a href="https://t.me/Futball180TV/93523" target="_blank">📅 05:58 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93522">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">امیرخان اگه بازیو نبری واقعا کیرم دهنت
اینقدر بیدار نموندم که باختتو ببینم داداش
😆
😆</div>
<div class="tg-footer">👁️ 8.15K · <a href="https://t.me/Futball180TV/93522" target="_blank">📅 05:57 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93521">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">دفاع نیست که
تنگه هرمزه ماشالا باز بازه</div>
<div class="tg-footer">👁️ 8.16K · <a href="https://t.me/Futball180TV/93521" target="_blank">📅 05:56 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93520">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">اوه اوه</div>
<div class="tg-footer">👁️ 8.15K · <a href="https://t.me/Futball180TV/93520" target="_blank">📅 05:54 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93519">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">اوه اوه</div>
<div class="tg-footer">👁️ 8.15K · <a href="https://t.me/Futball180TV/93519" target="_blank">📅 05:54 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93518">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/5aa3b3040d.mp4?token=nD_jQHo6WSxsjR_IK62t4e5ib0Yfe6j_KVFbunHAHvJeZtN0kxe5p5oGqkMpKd3qm8dIn4wluHMFffeL1vm5o8QyGembULnVPhRPWl-SLPhAR1ezoHwn_97Xn6s7hDhepg8uai9-hp-ydkF6JiESBAz-dJlI_WvBZPYOwGEY47LM0HstngHMAsOwOA0hcE3coWoflvH0N3IHAAXCX3TdHdHMNmoTVUUGWBtTAIS_Fu_iiVvKKxwtFajXKL6izuAgxS90QC2cnNWa-Fdi2br13qRXm0MBKsFsZSmmGhy8RKVYj6ahsq41i23_WmjZ-LsLlkkWdDvHbsw8IUKO6pMveg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/5aa3b3040d.mp4?token=nD_jQHo6WSxsjR_IK62t4e5ib0Yfe6j_KVFbunHAHvJeZtN0kxe5p5oGqkMpKd3qm8dIn4wluHMFffeL1vm5o8QyGembULnVPhRPWl-SLPhAR1ezoHwn_97Xn6s7hDhepg8uai9-hp-ydkF6JiESBAz-dJlI_WvBZPYOwGEY47LM0HstngHMAsOwOA0hcE3coWoflvH0N3IHAAXCX3TdHdHMNmoTVUUGWBtTAIS_Fu_iiVvKKxwtFajXKL6izuAgxS90QC2cnNWa-Fdi2br13qRXm0MBKsFsZSmmGhy8RKVYj6ahsq41i23_WmjZ-LsLlkkWdDvHbsw8IUKO6pMveg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇳🇿
گل‌دوم نیوزیلند به منتخب ایران دقیقه ۵۵
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.15K · <a href="https://t.me/Futball180TV/93518" target="_blank">📅 05:53 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93517">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">دقیقه ۵۵</div>
<div class="tg-footer">👁️ 7.15K · <a href="https://t.me/Futball180TV/93517" target="_blank">📅 05:52 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93516">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">خوردیم
😐</div>
<div class="tg-footer">👁️ 7.15K · <a href="https://t.me/Futball180TV/93516" target="_blank">📅 05:52 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93515">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">گلگلگلگل</div>
<div class="tg-footer">👁️ 7.15K · <a href="https://t.me/Futball180TV/93515" target="_blank">📅 05:52 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93513">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">علیپور بجا مغانلو اومد</div>
<div class="tg-footer">👁️ 7.14K · <a href="https://t.me/Futball180TV/93513" target="_blank">📅 05:50 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93512">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">شما هم حس می‌کنید مساوی تموم می‌شه؟
🐸</div>
<div class="tg-footer">👁️ 8.14K · <a href="https://t.me/Futball180TV/93512" target="_blank">📅 05:50 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93511">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/946a01d6d2.mp4?token=gw1RirLImOL9otPptnNheCqrmBXSqmH_MbEPeGL63uHONHD5ksmUjEI0FZGkR-lLsT1apXnIYI35l1GfoJoMB6oN2l5jgo1FIyj1OrwrRliisl_qMWF5hSS2oWYfIGoaFnb6E-l-WFeYF6Meacxc0DPSz83cOPu-TiDYJxJYbbvph1xA4-jdoGptFJQO8pw8f3ySkw3dSOFwU0TTic-qaDM7W_7gbiintjdXlaUq1Nskm4iWLbE-d0M26yCZ9VDI4e3cjJUzHxSXJ2KUUQy0c8EJidRo7PnsF-Gunl6b4H9w1tH-AfZtI3H1ZN6NPElSjphR4muhDE_x3gKF01egQw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/946a01d6d2.mp4?token=gw1RirLImOL9otPptnNheCqrmBXSqmH_MbEPeGL63uHONHD5ksmUjEI0FZGkR-lLsT1apXnIYI35l1GfoJoMB6oN2l5jgo1FIyj1OrwrRliisl_qMWF5hSS2oWYfIGoaFnb6E-l-WFeYF6Meacxc0DPSz83cOPu-TiDYJxJYbbvph1xA4-jdoGptFJQO8pw8f3ySkw3dSOFwU0TTic-qaDM7W_7gbiintjdXlaUq1Nskm4iWLbE-d0M26yCZ9VDI4e3cjJUzHxSXJ2KUUQy0c8EJidRo7PnsF-Gunl6b4H9w1tH-AfZtI3H1ZN6NPElSjphR4muhDE_x3gKF01egQw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سیس میلاد محمدی در لاین آپ قبل از شروع بازی
🤣
🤣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.14K · <a href="https://t.me/Futball180TV/93511" target="_blank">📅 05:46 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93510">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">ریدددد به معنای واقعی</div>
<div class="tg-footer">👁️ 8.13K · <a href="https://t.me/Futball180TV/93510" target="_blank">📅 05:45 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93509">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">خاک بر سر طارمی</div>
<div class="tg-footer">👁️ 8.13K · <a href="https://t.me/Futball180TV/93509" target="_blank">📅 05:45 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93508">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">قایدی بجا آریا یوسفی اومد</div>
<div class="tg-footer">👁️ 9.16K · <a href="https://t.me/Futball180TV/93508" target="_blank">📅 05:41 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93507">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">بریم سراغ نیمه‌دوم</div>
<div class="tg-footer">👁️ 9.16K · <a href="https://t.me/Futball180TV/93507" target="_blank">📅 05:41 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93506">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🚨
🚨
هو شدن نفرات منتخب ایران در هنگام اعلام اسامی توسط گوینده ورزشگاه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/Futball180TV/93506" target="_blank">📅 05:37 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93505">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ddc1604caa.mp4?token=l7SsfwiRxwsE-d95GlZaG8NU4IxY_axqdZdRporwSCiunVQcPD_k0wCnbBiGncy2Fq9dkJQCsdC2R_GoFMUDh2C-PSjmLnVFrcXyrV78zLacpnoAUqcTqwRgeDXWEebPk24ufsyfS0n8gYCrMbO-BQQV0-xoVlYpQl0ejE6e8sAcMaSeoJcnlNSCBo-B7Wrn9nxdpaVL0IJXOky-jPe7A8fpoVi4YHgSD8Ft3LCVXTwARz1BpAxcQi4-hqiIxNg3xmrO-fRwz5_h7HohNX_bPjQDHixPnaD8xhKG2b-poMf0OMCz2OOXa2GIesGei5Voa9_YRm2v6OaumcEBA024AI0krXE0fGRokvzjq1L7t528wrTzsZJEcC6N2GVG0s0_09yQmwCAj9fXXAzyS8pPWHW16u9VtiC09HnDQOjXtEsR2buN_IBDXzE4nXLeEbfeqVYiDrUGUxQBJ__kH1RQdzsqr3DeFuyqpMgnfSEqMT3fU6VbDeon5KqmOu9wksk8xu0UrUjyBuuznBo0vnhaKw8Td_AwaQzeAJd8C8i2A1O-KFjY91pkzfnBpD9ssu_if2bkHUKfwWrzUpbF_kWi0G1Sy0y4spMcgDtDhAHpPrYStQ_kl7VkOQEa-cWSfi8IN6JbM29VvVVqclUJXjSYtkLpRMzEiGCOxIBgL5-zarM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ddc1604caa.mp4?token=l7SsfwiRxwsE-d95GlZaG8NU4IxY_axqdZdRporwSCiunVQcPD_k0wCnbBiGncy2Fq9dkJQCsdC2R_GoFMUDh2C-PSjmLnVFrcXyrV78zLacpnoAUqcTqwRgeDXWEebPk24ufsyfS0n8gYCrMbO-BQQV0-xoVlYpQl0ejE6e8sAcMaSeoJcnlNSCBo-B7Wrn9nxdpaVL0IJXOky-jPe7A8fpoVi4YHgSD8Ft3LCVXTwARz1BpAxcQi4-hqiIxNg3xmrO-fRwz5_h7HohNX_bPjQDHixPnaD8xhKG2b-poMf0OMCz2OOXa2GIesGei5Voa9_YRm2v6OaumcEBA024AI0krXE0fGRokvzjq1L7t528wrTzsZJEcC6N2GVG0s0_09yQmwCAj9fXXAzyS8pPWHW16u9VtiC09HnDQOjXtEsR2buN_IBDXzE4nXLeEbfeqVYiDrUGUxQBJ__kH1RQdzsqr3DeFuyqpMgnfSEqMT3fU6VbDeon5KqmOu9wksk8xu0UrUjyBuuznBo0vnhaKw8Td_AwaQzeAJd8C8i2A1O-KFjY91pkzfnBpD9ssu_if2bkHUKfwWrzUpbF_kWi0G1Sy0y4spMcgDtDhAHpPrYStQ_kl7VkOQEa-cWSfi8IN6JbM29VvVVqclUJXjSYtkLpRMzEiGCOxIBgL5-zarM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
ورزشگاه یجوری پره که اصن پشماممممممم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/Futball180TV/93505" target="_blank">📅 05:33 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93504">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b25ed16f17.mp4?token=V6SzB_dJJsDMkr5kjWTci3iWkU7-FDMw68_RdC_g-m0BjCEcAv40MMECeAiN0cXlK-izBsJS3dPZjXTYf4CO9dEWadeMtnkZinXihU_g-1EvWRexryn_mMjq_btFYissJJnMdZq5DvH8JGZZDkH3kRkjAgf7Ch41-UDitRryNBRR9hHhYrW7Wc9xiaZocTV-rysMXVxScczY7k8cNK1ifWFHTCcoQMzSnVmj9mAQsMot0zlUmj6B0k6ZTYh7XJJrYIXavK9NNj0bu-644sFq9zJ_GlsaLk1ncfETEVMoOSndLH7qiLen6YqjSixaU1ga-Jp9rKscUrFC7YT52WLYyQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b25ed16f17.mp4?token=V6SzB_dJJsDMkr5kjWTci3iWkU7-FDMw68_RdC_g-m0BjCEcAv40MMECeAiN0cXlK-izBsJS3dPZjXTYf4CO9dEWadeMtnkZinXihU_g-1EvWRexryn_mMjq_btFYissJJnMdZq5DvH8JGZZDkH3kRkjAgf7Ch41-UDitRryNBRR9hHhYrW7Wc9xiaZocTV-rysMXVxScczY7k8cNK1ifWFHTCcoQMzSnVmj9mAQsMot0zlUmj6B0k6ZTYh7XJJrYIXavK9NNj0bu-644sFq9zJ_GlsaLk1ncfETEVMoOSndLH7qiLen6YqjSixaU1ga-Jp9rKscUrFC7YT52WLYyQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
😐
واکنش هواداران ایرانی استادیوم به گل نیوزیلند؛ صدا کم کنید درتون نرهههه سر صبحی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/Futball180TV/93504" target="_blank">📅 05:31 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93503">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vZPq-VzR5oRghKLuM9Fkzb5qhTldPrz4o66BRC9ZsciL9FOdGuv7sfHD2kMCrftuj5LymSrw1B4dusH6rZ1YYreBZOHlkOY8AYn6lzJOTOum9ecLgUOWwsiSr7G1ZXXMu3LqcUkbs19sOopzv4Ei15wp6OKDD7-XTH0v0dInEJwOAfAXYoEASgo3m18G_X9BEB8d7EpB2AmYf45vHYKNidM_3cdyooaGeHNIFohMyYv4bh-MDLOBTG3S6GzgZGmjOWv_NoFgkUsCAg8lG97P7duNMwbxjJTeSi7OaeEQ9RLY7snR68aE3Ji_PTBsHVgw1bH9riGG7jy1ZmNxJRPyqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آفساید میلی متری علی نعمتی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/93503" target="_blank">📅 05:27 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93502">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🚨
پایان نیمه‌اول با تساوی
😃
بر
😃
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/Futball180TV/93502" target="_blank">📅 05:24 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93501">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">واضح بود</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/Futball180TV/93501" target="_blank">📅 05:24 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93500">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">آفساید شدد</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/Futball180TV/93500" target="_blank">📅 05:24 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93499">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">علی نعمتی</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/Futball180TV/93499" target="_blank">📅 05:23 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93498">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">گل‌دوم برای تیم قلعه‌نویی</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/Futball180TV/93498" target="_blank">📅 05:23 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93497">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">مغانلو ریددد</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/Futball180TV/93497" target="_blank">📅 05:22 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93496">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">۶ دقیقه وقت اضافه</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/93496" target="_blank">📅 05:19 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93495">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Nhp3jJ53SiShrA4VLUrg180YeXSB8KkD00u10P5BbvvAFOjiojHt9HLa9ISv-ua-KgSmGags05lDFRkP0Ngx_RGB9UWj4RR8r84A8ICE_w4aHI-K6uREO9iKZ3gGryX0EWpnXYPdSbBsfsJ_sCMqLe023ZjFOsc0XxpKZAxU0g3APDK5hswGlDMo5lDQoKX6ISw22n5Ppmu-M8s6JmpR6oAqBON50zLVAq6ZMzTwcT8zV74mY5wvFTPaKup39Wmjwls3-ZU84ZGhRzfq3Gej-C1DRMjUNxtffyLxR_TXbc8ADqV6FPhC656qEB1Zdupi6QkjNAIq5fGT1qL60YvQqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هوادار نیوزلند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/93495" target="_blank">📅 05:17 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93494">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">خطای خوب برا نیوزیلند</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/Futball180TV/93494" target="_blank">📅 05:17 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93493">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">نیوزیلند فوق‌العاده کیریه حقیقتا با این نوع بازی باید چنتا گل میخورد</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/93493" target="_blank">📅 05:08 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93492">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">بازیکن حریفوو
😂
😐</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/93492" target="_blank">📅 05:08 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93491">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/5e40878478.mp4?token=VJBRAoyQseLQLFcs2jV85jxZ6Z7qCybORIVxjxKL9sRZTWLGpKAdT28RjSzOlFBkSCGhAl32Cj7bTphqCzW9GH2i4Dr1R8jPvK0s_M_3wrfAY-WoUm0H7R0AyTbz19-2tzyIFTpNWbFmFsx-fD_h9EAqUzpcR4PG6xB7llHVx_8KjrACGZLyZz47jj3VDV_i7WK29psKOMDrkqOcLlfoV_LpoqnNVQkIB31md7URZbMp3oewM3iFDzSQkuxy9ssltjY0JSTeHXAtJ05TdAR8d_pdjUGkkj-cV5SU6b7XmP5K_pD3NBHmyFLyFHPWGmqwpicL6ffcGuecNV8yLhQKnoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/5e40878478.mp4?token=VJBRAoyQseLQLFcs2jV85jxZ6Z7qCybORIVxjxKL9sRZTWLGpKAdT28RjSzOlFBkSCGhAl32Cj7bTphqCzW9GH2i4Dr1R8jPvK0s_M_3wrfAY-WoUm0H7R0AyTbz19-2tzyIFTpNWbFmFsx-fD_h9EAqUzpcR4PG6xB7llHVx_8KjrACGZLyZz47jj3VDV_i7WK29psKOMDrkqOcLlfoV_LpoqnNVQkIB31md7URZbMp3oewM3iFDzSQkuxy9ssltjY0JSTeHXAtJ05TdAR8d_pdjUGkkj-cV5SU6b7XmP5K_pD3NBHmyFLyFHPWGmqwpicL6ffcGuecNV8yLhQKnoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🏆
گل‌تساوی توسط رامین‌رضاییان
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/93491" target="_blank">📅 05:07 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93490">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">رامین رضاییان</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/Futball180TV/93490" target="_blank">📅 05:06 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93489">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">ایران</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/Futball180TV/93489" target="_blank">📅 05:06 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93488">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">گل زد</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/Futball180TV/93488" target="_blank">📅 05:06 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93487">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">کسخل خر</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/93487" target="_blank">📅 05:02 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93486">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">گلروو</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/Futball180TV/93486" target="_blank">📅 05:02 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93485">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">قلعه‌نویی داره پاچه طارمیو میگیره
😂
😂</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/93485" target="_blank">📅 04:59 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93484">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">کولینگ بریک</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/93484" target="_blank">📅 04:58 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93483">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">اسمال چرا انقد جلویی
😂</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/93483" target="_blank">📅 04:57 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93482">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">طارمی تیررر زد</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/93482" target="_blank">📅 04:56 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93481">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">طارمی تیررر زد</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/93481" target="_blank">📅 04:56 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93480">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">قلعه نویی: قراره تو جام جهانی کاری کنیم یک هفته کل ایران تعطیل بشه از خوشحالی  + قلعه نویی دقیقه هفت بازی اول:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/93480" target="_blank">📅 04:55 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93479">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LvVn4ePd0XsP8ZDKpMO9_gN76ZwXyFPL--85SWrsg1ZI4jUNs7SmG2623FEjM-P4dIKldv445K7PMxSmGhYeH_RbkU0dHodmxjRir_nW8LYgOeKtk9bJ-YrdAOtsvcnN2GqRMbNNcYSEEScDolIJYUf2_G17BIjjSJJkZYbQh04uzvqhrMqD-jzB9xgGVFlo2z_bJZSxxqQRYxif9iD0qG1GhFmvADhkBk7R-bkAVq_z7krdMpIid0ZpoiLUG-9jfmAVoMekiS3xILJ9s-RTwugtdVEhef-c_rpijlV1A_Z8pu7ovzzERxZuHwK8q8Q55mPpuryVVcSWIx27dnYXFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قلعه نویی: قراره تو جام جهانی کاری کنیم یک هفته کل ایران تعطیل بشه از خوشحالی
+ قلعه نویی دقیقه هفت بازی اول:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/Futball180TV/93479" target="_blank">📅 04:54 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93478">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">مغانلو کسخل خودشو زد زمین</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/Futball180TV/93478" target="_blank">📅 04:51 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93477">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">صحنه مشکوک پنالتی</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/Futball180TV/93477" target="_blank">📅 04:50 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93476">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">قدوس کصغزووو
😐
😐
😂</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/93476" target="_blank">📅 04:49 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93475">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">مهاجم نیوزیلند دروازه خالی نزددددد</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/93475" target="_blank">📅 04:49 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93474">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">یه ذره هم توپو بدین دست این یتیما</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/93474" target="_blank">📅 04:49 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93473">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">پشماممممممم دارن تجاوز میکننننن
😐
😐
😐</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/93473" target="_blank">📅 04:48 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93472">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">مهاجم نیوزیلند دروازه خالی نزددددد</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/93472" target="_blank">📅 04:48 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93471">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">وااااای</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/Futball180TV/93471" target="_blank">📅 04:48 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93470">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OM0J9K77JVG2SvHkrOlxmVSxHwqFhtsASLY3yfg5bqo4aBBIe2252-JyVHoAzEuMRtYA1u2tZdQfFLnPYDJk0xQeDZ53ChlSG9eWibMqv4IwMbdn67Uznwvh4taTKlKYIugS3vFmIGfgKjM9HQzRYZRoQMMqAoRMGNduKj6A4z_FFEbVOHi2t4VcZvtPj0LhZXviPpd-_XRghWjC2Blgt1GcmZLmiKJdf9wrsWj9dVwWCEGeNr1G4dtO1iusEBu3987o0J8YRTDcjQVNLhb7QX23-QxiAdf27leUONWKlIF0bJZMkOIFdZneKL9hlS5ciHDAHRD8Cf5MWk-EyK17hw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇳🇿
گل‌اول نیوزیلند به منتخب قلعه‌نویی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/Futball180TV/93470" target="_blank">📅 04:48 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93469">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">نیوزیلند خیمه زدههههههه</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/Futball180TV/93469" target="_blank">📅 04:46 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93468">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">واااای</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/Futball180TV/93468" target="_blank">📅 04:46 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93467">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">بازم نزدیک بود نیوزیلند بزنههههه</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/Futball180TV/93467" target="_blank">📅 04:45 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93466">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">وااااای</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/Futball180TV/93466" target="_blank">📅 04:45 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93465">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">هم تنگه هرمز باز شد هم تنگه علی بیرو
😃
😃</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/Futball180TV/93465" target="_blank">📅 04:45 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93464">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">پشماممممم اینا تمرین میکردن یا مخ دخترارو میزدن؟</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/Futball180TV/93464" target="_blank">📅 04:44 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93463">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/4297351610.mp4?token=dbjJHpgAbf2iEGTsGl-GGSgMEq7cICRA48kmdcX4pXQ_rox721kCyHztKjbu1zX2DmyEWId5-0XkWevotxJXKf7A1RIMV-mamH2oNemB6xCBXpTJ3zMlW2xt7CwnLZk5Yf5n8kJuSP6CKwJKOsC8zKtI1zRHUM45QeRoqHyvaD7UuC05LYdvXNen1LTTO_Qy0OVyVlM4ciW4h3Ws7wYaP0mcyI-BXKL-FAsczLhPMziGgDSpnnPFDCSeqlTdNGADzsMIlX0dmC47onj7lKxkCQPMhi89RMc1yMdAsXMWKVrnR6fTXkl7PPi4xwQPobNfecQb6aunxI7cYNnE-i2B5Q" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/4297351610.mp4?token=dbjJHpgAbf2iEGTsGl-GGSgMEq7cICRA48kmdcX4pXQ_rox721kCyHztKjbu1zX2DmyEWId5-0XkWevotxJXKf7A1RIMV-mamH2oNemB6xCBXpTJ3zMlW2xt7CwnLZk5Yf5n8kJuSP6CKwJKOsC8zKtI1zRHUM45QeRoqHyvaD7UuC05LYdvXNen1LTTO_Qy0OVyVlM4ciW4h3Ws7wYaP0mcyI-BXKL-FAsczLhPMziGgDSpnnPFDCSeqlTdNGADzsMIlX0dmC47onj7lKxkCQPMhi89RMc1yMdAsXMWKVrnR6fTXkl7PPi4xwQPobNfecQb6aunxI7cYNnE-i2B5Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇳🇿
گل‌اول نیوزیلند به منتخب قلعه‌نویی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/93463" target="_blank">📅 04:42 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93462">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">علی نعمتی
🤣
🤣
🤣
🤣
🤣
🤣</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/Futball180TV/93462" target="_blank">📅 04:41 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93461">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">دفاع کیر خری قلعه‌نویوووو
😐
😐
😐</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/Futball180TV/93461" target="_blank">📅 04:41 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93460">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">پشماممممممم</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/Futball180TV/93460" target="_blank">📅 04:41 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93459">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">نیوزیلنددددددددد</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/Futball180TV/93459" target="_blank">📅 04:40 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93458">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">گگگلگگگل</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/Futball180TV/93458" target="_blank">📅 04:40 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93457">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">صدای هوووو شدن شدیددددد تو استادیوم</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/Futball180TV/93457" target="_blank">📅 04:37 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93456">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EXGea3dYgiDRolCGYcgx7Zy9EgQwOmTL9R1PBXxpiBlxpV5A4MoI5Rse1FdWNN37H-_0S3aECs5QVCf2f6lTd8DI49NmElAXqTeJU81Kc__Rmfiwjk2GCcyZfQ4oU7VcXdf4adAlkDNFONNXiIxbSElGcX65x2EEfjBeGn5Rq8I9DXajUuPsqsOj-yFR5mVJzKRJaLfuMRytzNVtKNqBtyq6Us5JapkSr3RkSaBbyzgkFcbcymlBFFCtQi_Tt6rxkcs81G45OqxT9txTWKVJfzR68CEpgERatftclHJpheeF-0VohAcPK1KFmY41N96FL6duH8OuoTTjS3zSO7iw5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طرف 2.5 میلیون دلار رو باخت ایران بت زده
‼️
‼️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/Futball180TV/93456" target="_blank">📅 04:35 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93455">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">اولین سانتر بازی ثانیه ۳۰ توسط رامین رضاییان</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/Futball180TV/93455" target="_blank">📅 04:34 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93454">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">قیافه قلعه‌نوییووووو
😂
😂
😂</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/Futball180TV/93454" target="_blank">📅 04:33 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93453">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🚨
آغاز بازی منتخب قلعه‌نویی و نیوزیلند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/Futball180TV/93453" target="_blank">📅 04:30 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93452">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">بازیکنان وارد زمین شدن</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/Futball180TV/93452" target="_blank">📅 04:25 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93451">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YPHindtJKH4hD-DpxdHl13eKVkMJy4zLjriH9mbzaMP1dsraJVfp4R5AnuES18mGamCRqZHCStTdF6EvlGmkKsaA8R1hmHv0NV_P8YHauBAcKjFyKfFQS7xKRkazOfKkupGwtud9PGHNTqrAWNwLvvQdDr7pyYtoVgBb79OGI_qw9-0IBzE6ysTvz6qZOnG42ovRZpCgEDiThhKIXMwKioNhPwf-qJ9b0N-fYLtIQ5rYUlCn3ikmUwqSYfOyIlDQMkY7g2wQUMMW__WUzp2Qijmk1MPxlRACXdEFi70Yfd1BfBLVsYkY2QXzz43tKoD6hywjl6cq6vG0Ee0ap_G18Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">از فنای ایران ببینیم.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/Futball180TV/93451" target="_blank">📅 04:25 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93450">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cjqVYolu1ocGuGA8or9ZTpCSNfSjSLt4KxImaKu7j7XEcfXWbcxqY1lfmpjL4t2BkfsSXF96I0LXJXI0aPgoKlE-KGf9NwQZebMKf5ohzAqu1F14furP6STyPaB26gux6GFEqSjU1JIgfXUgcmasBzA2rEQN7RQJx39UOyV69L-XIMz7JUNjyO8_UN7DyDr4j1eIRXZiJrYHgVDhwxzaUfSIRtNwmkGy0f9Iwj3B9Zw1hCh17EDuUKDVzN2eK9DRfyaRr2sDmjC2HdDmQJYTT7OcoEvOQGUPeRCdm7nsRCfrFBp_cLhN1GUydQObVbmkqi1et2PzMdJwW81rKzffpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جو پشم ریزون استادیوم
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/Futball180TV/93450" target="_blank">📅 04:23 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93449">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Suvo2GLIfRpaUfKQjoHunRm0mdGY0KCI2mqjDDOgnZ6M_nfXSRBE_KiKyugl_7ZK5tO1XilJYNYKK7VdcsEuGDoGB7z7TkcjJqoQn_yXqkpopHm8hqvCcVSDe5U6najfwxinlzuCA02yUM7fWaY4ioczbjusioBe6J0K2D6G6yGOqUu_GfuBikdslbthfAXt2pBe47z4xx1Vi9jnMgR5x7bDD4bq29HGf6I0a4B4rEbTTpIv3uPK7OgpcP6q-mYFNl39vofEG36FyQW68uGEZqsx9Orih3eWzmvHHVF_-b_F_6_Yui6R_-PmN9PoUHhkPJPJR5tUuSvH2nB9APTu7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گویا دارن به پرچم شیروخورشید گیر میدن.
‼️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/Futball180TV/93449" target="_blank">📅 04:23 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93448">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lT_8wyBT6lI5n0AY0x9fkdg7SWCPFCzhazyS8_LVxN6Wncmjsj2p1zM9Ue0z1yTv47FnTHlTlpIl5zrkVL-T4KI1nx3jhXYd6-r-rZt33Pe-pnWm4pa3H79Ye3ktAU39pqtmRgYSf7_uLx6v9ubLkNT_0MHCI_XSJGNKWpUO1_KGFZ9Z9C6dB7qShidokF2yqRQcmV-YITuJVENnFB3dhLvgkgACa3gwORugKBOhOUn2Nrb2c-WacPU9KG1azMuPC8NvwjelvAg6pTzwOOUm-TK8oSV8mRpRFiSTFZoS5ZvT8SG3B7HFFDJ7aX1R0oK-hZfYuN7Jtgpv0F2LIZTi7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ظاهرا مردم مظلوم غزه هم تو ورزشگاه نماینده دارن. بیشتر شبیه تقابل جبهه کفر و مقاومته تا بازی فوتبال
😂
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/Futball180TV/93448" target="_blank">📅 04:10 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93447">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">با لایک و دیسلایک بهم بگید عشق کردید با پستای دو سه ساعت اخیر عمو اسی یا تلاشمو بیشتر کنم گلای تو خونه
☹️</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/Futball180TV/93447" target="_blank">📅 04:08 · 26 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
