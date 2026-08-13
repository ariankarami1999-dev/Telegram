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
<img src="https://cdn5.telesco.pe/file/NBrOOuWkUUUk1wHBGGzNwImsqoquiBao4Qjxm1qo2Kqcm0Tcp2gJtd1d3lcGdPNCK6HOO7echGmbJFZzLXqwhY3rxtBF7rgMjl2oOTHIHwo44D-8R4FAmk0bd6ybJskfp44QBZf4bx1dN9o73hqFg6jNk4i1cl5k7xNS7a9GMAVauxc7_ToA4DcqjrzNKMRVOnv5-A9jMB_mPoKrsydvzOE5DhgEduH6R9ZJ20C9zSEXti8Q1ytnFyjpQnC5EYEgBL7FgxK88vqx21jYbCRq6lukm56Vz7vh_c-zin39C20P2hCcKRX84NfsZYzDMbhEzAc0jfGXY2kq7zNI2prDmA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فوتبال 180</h1>
<p>@Futball180TV • 👥 471K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-22 17:46:37</div>
<hr>

<div class="tg-post" id="msg-103582">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f5eb10d932.mp4?token=IEkPHaQBby0d9CT03V5bnRdRvcngTGkllvP1hfMJYWTVmo-uPmeb0NymIpCo56lxgQSpOuOZZ8MJFlnskaD1oT5U_iiguTR3_Of2pkADywreR-5Aeh0_PMruyVpFA6bcfJM5AndIkqVcMP8DVBXgHTOUNhBi_HG1feTON4PvJij6c8bcBiQzuUI5L1AuVaSjm5ASIYbqBOVs2FnEkaFoGARyH_Pt5Fianp34TUZZXWDwxyijRw3OHvQNU6CQcD46W8ToLBLrLpJxCqKtQTyWTblew_8NnzeXLL2rgr28RqAEI7519Dpv_C8-KbGzaQGnSuvOyvoYO9qT2ONSIYJMhg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f5eb10d932.mp4?token=IEkPHaQBby0d9CT03V5bnRdRvcngTGkllvP1hfMJYWTVmo-uPmeb0NymIpCo56lxgQSpOuOZZ8MJFlnskaD1oT5U_iiguTR3_Of2pkADywreR-5Aeh0_PMruyVpFA6bcfJM5AndIkqVcMP8DVBXgHTOUNhBi_HG1feTON4PvJij6c8bcBiQzuUI5L1AuVaSjm5ASIYbqBOVs2FnEkaFoGARyH_Pt5Fianp34TUZZXWDwxyijRw3OHvQNU6CQcD46W8ToLBLrLpJxCqKtQTyWTblew_8NnzeXLL2rgr28RqAEI7519Dpv_C8-KbGzaQGnSuvOyvoYO9qT2ONSIYJMhg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
🔵
کنایه تراکتوری‌ها به استقلال با جام قهرمانی: اولین بازی آخرین قهرمان لیگ
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 308 · <a href="https://t.me/Futball180TV/103582" target="_blank">📅 17:47 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103581">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t8Ln_vB6sE6R6VnW7nQdIA8BKAYyFssbV5rQ4VtaqqK2uKcJ9f5I-A7C8musqLgegmQvqFdj6cKDCz3Fzu5OWj7IbULiLHsc1ZiJ-C2aHwVLFAZ1wp7GZ30LHZZRZrQ2gnzRxZr3RWi7e-Y5a905b7GvKEaLDiYdLVUv2Ny0UxsNjLgPhlkMj5xeyP286YAQlSoUT_IF37Jw-Rvzmwx-3_ztjqT1x_6f97gyE8pa2D0i873DVw2Pm0WDOBKDQNe5oJYYiOoZJSlsc-k72q05aTsLTq_qILFt_Wsm_OtqB53Me56try0EWnblfCT-0kjL1RDptWCFKWM8xOCHDHhoGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
پاری سن ژرمن پس از جدایی امباپه، 10 جام از 12 جام ممکن رو کسب کرده در حالیکه 4 تاش جام اروپایی بوده. ولی شرایط برای رئال مادرید کاملا متفاوت بوده؛ اونا پس از پیوستن امباپه، فقط 2 جام از 11 جام ممکن رو کسب کردن.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 1.52K · <a href="https://t.me/Futball180TV/103581" target="_blank">📅 17:40 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103580">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AegEbis7EeU-CW6-5gIQ_FMCqEwL9LAZ-9ow5vKoxctxAgSbSc-2dTXQfkgILGEyT01_WV0mwuzEEpTPx-z4anD3zBRUTkqV1egCcf1EfJpNOY0Xu9Yi9BhHqguVbiCx2Kfus9VLN15k14hznSkeKdNmTZMv1toGenMpMZSAouxBjwOZY6QBYjGEJ3boZCBYy0Tkdv-a_ZBJcF5axzi932GWXSXwzk5O7oZMdv3VedXw68medEmNTh7tu100lnCkI3aCJdQm6I6sGcq65KNIVTJHyIBjnWYAEmXpQnTmz2-LRDfm7Dtf3zsqPQV5c6z0f1JsP3XlLDy19rVnplinPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
✅
دریا بنگر، دختر محسن بنگر کاپیتان سابق پرسپولیس و سپاهان هستن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 2.13K · <a href="https://t.me/Futball180TV/103580" target="_blank">📅 17:37 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103579">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🚨
🚨
🚨
جرارد رومرو:
خولیان آلوارز همچنان با خشم و عصبانیت شدید به تمریناتش ادامه میده.
باید منتظر بمونیم و ببینیم بعد از بازگشت خیل مارین به مادرید چه اتفاقی می‌افته.
اما حس و حال کلی در مورد سانجام معامله خولیان اصلاً خوب نیست و کاملاً منفیه
❌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.65K · <a href="https://t.me/Futball180TV/103579" target="_blank">📅 17:30 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103578">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ee6c2af722.mp4?token=Cepi1RtLUhaA5G1kJKmqFJIFCflVOK5XvGAqZ-dIgnWar_vCfIkH1JGzFYgU4F3hyIiXNY8_e8_GmTzzoJvzo4Ufth6ktq4j7QadFq8r7O4YVerr-m8kLkvjQ_TutZX_P5wmU-IT_tmNnL9tEnZrIdWUQuUzManSGh4U7ekhf1e_rNxxJZ5L32oswjXsRLclzelBfjw2uSDUikyMpuz6ZJERsggIwi3weazs2791GzMsF9dAtf6vMsqpO7d-l7U3A1BweFckRP0xIYmLUPPpf4Lpoo8a5kOMd0QUrqX6q3VWtQOcZgnW2JD6gcmwlMsrXd2jtXMCLc0mtC1C-cSwTQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ee6c2af722.mp4?token=Cepi1RtLUhaA5G1kJKmqFJIFCflVOK5XvGAqZ-dIgnWar_vCfIkH1JGzFYgU4F3hyIiXNY8_e8_GmTzzoJvzo4Ufth6ktq4j7QadFq8r7O4YVerr-m8kLkvjQ_TutZX_P5wmU-IT_tmNnL9tEnZrIdWUQuUzManSGh4U7ekhf1e_rNxxJZ5L32oswjXsRLclzelBfjw2uSDUikyMpuz6ZJERsggIwi3weazs2791GzMsF9dAtf6vMsqpO7d-l7U3A1BweFckRP0xIYmLUPPpf4Lpoo8a5kOMd0QUrqX6q3VWtQOcZgnW2JD6gcmwlMsrXd2jtXMCLc0mtC1C-cSwTQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">از عجایب سوپرلیگ کشور ونزوئلا
😂
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.56K · <a href="https://t.me/Futball180TV/103578" target="_blank">📅 17:20 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103577">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">🚨
📊
🎙
🇮🇷
جواد
نکونام: یکی از تاکتیک‌هایم امسال هواداران تراکتور هستند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.22K · <a href="https://t.me/Futball180TV/103577" target="_blank">📅 17:05 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103576">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7cdfdeee34.mp4?token=O6eTBMyCTcNn5fiTAOZ9Zrs5t9z4_SgswcfxVqNsTRAtSmFZApUG1pDf8OM0VfuSFqQD3v4Up4s1g5RZQcWw5OFSkUHCN2qwEq3ZpvwywdgzGvz8vzmuzbVqjkyZIcShsMyotpwlz_jibkX7FKCR_etupZPRBUAmyiLqErQ2eh-ZkUFIi9qLN-7J9qiPE9OEh6W5_ed3wCUfZj1oMeJfm62rZts5Byi4aIoxlQbSVeyFC2nlZmWEiq4--lmKqJqxgZjkdG6adDly5PArl21jlHGCQ1_GFgLMKSPy5YNT4CxTpUGmV15_ctrlIlhpy1LnxjcefRyXiKCkiGV3iu2h0A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7cdfdeee34.mp4?token=O6eTBMyCTcNn5fiTAOZ9Zrs5t9z4_SgswcfxVqNsTRAtSmFZApUG1pDf8OM0VfuSFqQD3v4Up4s1g5RZQcWw5OFSkUHCN2qwEq3ZpvwywdgzGvz8vzmuzbVqjkyZIcShsMyotpwlz_jibkX7FKCR_etupZPRBUAmyiLqErQ2eh-ZkUFIi9qLN-7J9qiPE9OEh6W5_ed3wCUfZj1oMeJfm62rZts5Byi4aIoxlQbSVeyFC2nlZmWEiq4--lmKqJqxgZjkdG6adDly5PArl21jlHGCQ1_GFgLMKSPy5YNT4CxTpUGmV15_ctrlIlhpy1LnxjcefRyXiKCkiGV3iu2h0A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
⚠️
زلنسکی رئیس جمهور اوکراین بالاخره دست به کار فیزیکی زد. ابتدا تمرین پرس سینه انجام داد و بعد تیراندازی با کمان را امتحان کرد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.19K · <a href="https://t.me/Futball180TV/103576" target="_blank">📅 16:34 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103575">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e5uLVnn1mPRL_1lFXtDXF9Is6I8Fsxxl0nXBb6Qo6zUk4SQ8dkTr7tLx22myLyfFcYT4ZnUe5SYG_70IlX_ChbfguxpvdVJXQ_MPTNpWUii_YjV4ZrSsOr42bV8JSg4_AD3LrVKku1NNSfj4ocDhgHwlzE4SjW7LXSm4mT4baoqsA-EYyGlnw7nrNpLhwOfVJcEwhOiHs-GjvhOdSpfnSTsrxXaDPPOokuvkf8XxKnR12eNHaK8mEGTrBXK34GOjNd9fY_kXR8KJ9fbISBOvrR3J5V0qNOKEpkW6MRgpRtIwkJgssGX9IRFNWpN4rQUmyHqpVdFLOl6DTanayUH5wg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇪🇸
پائو
کوبارسی ستاره بارسلونا برنده جایزه پسر طلایی فصل 2025/26 شد
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.01K · <a href="https://t.me/Futball180TV/103575" target="_blank">📅 16:28 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103574">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7ef89e7942.mp4?token=ei1f_rKOnNEnoUApj6UweY5Ry9FMGbPDEoPQ4CwwE_AkM0s4BOaXdx85JXXm5Qr2KWjJdCWR1lDLV1p4l_cAs_RBqZjjm9vD87RFhfQ4gY7shkfRZn1KCW4Cahd1CnFHjBg3dUqWCviGeOS1bDufsUo_z6RANMxSEzWq3qtNccgS4E201rQdfJKFfw9e_OjZvpfknw0mE1k5eoDmBIcKHAmKAEg97rpU34WbNm1b9mtmhnzWu85qq0Ryevs3BKv7yQNLyRXXvbkaijkXg6kq2wZbkQtJSewusfGJ0NsyaN7FZBKLbXcKNnhhBh7m5CQMPJBcJJoRmWS3gC31qj6CqVdBrtO5WScCXTNFniJoMmCqbmh0neUBz7NfYopE8FNkbC_LXb3yp4eIGA9hm8CcvE2ndwjV3mcfETWekoEWZeqTfciJLtwTYY4PTAYBUR5MiF2auS00NCxJV9D41VTFASs-SlnIsKwKaatiB8ScM5jweV4TBMLOzm7sCU4gNLVXXWvT7SMR1zKEVePe2lyhoVtol5F5I1QjEDxtIMgceW-za3zHNvzT3j3DvuxUuLRNSvzW4KvToFxNYVrU3YokIBYQM63fIHspCrz6sEgjbjJcXfhoEgah93znYSjyuEOmcVXxpJIKi1PKHTxb1glIGLk86Z01wPJ3lx9onLP78SI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7ef89e7942.mp4?token=ei1f_rKOnNEnoUApj6UweY5Ry9FMGbPDEoPQ4CwwE_AkM0s4BOaXdx85JXXm5Qr2KWjJdCWR1lDLV1p4l_cAs_RBqZjjm9vD87RFhfQ4gY7shkfRZn1KCW4Cahd1CnFHjBg3dUqWCviGeOS1bDufsUo_z6RANMxSEzWq3qtNccgS4E201rQdfJKFfw9e_OjZvpfknw0mE1k5eoDmBIcKHAmKAEg97rpU34WbNm1b9mtmhnzWu85qq0Ryevs3BKv7yQNLyRXXvbkaijkXg6kq2wZbkQtJSewusfGJ0NsyaN7FZBKLbXcKNnhhBh7m5CQMPJBcJJoRmWS3gC31qj6CqVdBrtO5WScCXTNFniJoMmCqbmh0neUBz7NfYopE8FNkbC_LXb3yp4eIGA9hm8CcvE2ndwjV3mcfETWekoEWZeqTfciJLtwTYY4PTAYBUR5MiF2auS00NCxJV9D41VTFASs-SlnIsKwKaatiB8ScM5jweV4TBMLOzm7sCU4gNLVXXWvT7SMR1zKEVePe2lyhoVtol5F5I1QjEDxtIMgceW-za3zHNvzT3j3DvuxUuLRNSvzW4KvToFxNYVrU3YokIBYQM63fIHspCrz6sEgjbjJcXfhoEgah93znYSjyuEOmcVXxpJIKi1PKHTxb1glIGLk86Z01wPJ3lx9onLP78SI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🪄
آخرین حضور اسطوره اوسین‌بولت در‌ المپیک
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.56K · <a href="https://t.me/Futball180TV/103574" target="_blank">📅 16:26 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103573">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-text">📌
فقط ۲۴ ساعت عضویت رایگان باز شده از همین امشب چک کن ببین چجوری میشه پول دراورد
💵
💸
🛒
این فرصت محدود رو از دست ندید
https://t.me/+MT03hkV78q9kMTc0</div>
<div class="tg-footer">👁️ 7.33K · <a href="https://t.me/Futball180TV/103573" target="_blank">📅 16:26 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103572">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0106cebdea.mp4?token=qeDyZ9t4OPAP0PUQ3HwAnvjnqix8vnj5SFNfDSYA2ul88EuTeNM86g40dGI64nQ1XlJUnP4Zjnw8NlVGxaO1ReA3GbK7ikCe_Q-G5kH8jRNw2J8sm7czBb-goV35pTaEMtgr7-h8qCQCSzkc472iFOzoR0FOYViqguRW-gznO182o4iBRQTEkaJHdF_VyM0_DxJJXLrBADCGQRdXmRcFbuhyw82KZJ1i7oDaBZbik2it26Gnqd6v_FRvaxGNyYlVTZLbfZWc_o6Bzpqp2cmC6gTrLDqMJUMlrclSZRH2AQx-XT1bTAg3ToQhLqqanZugA10KPQr-jKeMH7wtprUHZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0106cebdea.mp4?token=qeDyZ9t4OPAP0PUQ3HwAnvjnqix8vnj5SFNfDSYA2ul88EuTeNM86g40dGI64nQ1XlJUnP4Zjnw8NlVGxaO1ReA3GbK7ikCe_Q-G5kH8jRNw2J8sm7czBb-goV35pTaEMtgr7-h8qCQCSzkc472iFOzoR0FOYViqguRW-gznO182o4iBRQTEkaJHdF_VyM0_DxJJXLrBADCGQRdXmRcFbuhyw82KZJ1i7oDaBZbik2it26Gnqd6v_FRvaxGNyYlVTZLbfZWc_o6Bzpqp2cmC6gTrLDqMJUMlrclSZRH2AQx-XT1bTAg3ToQhLqqanZugA10KPQr-jKeMH7wtprUHZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💯
تنها کانالی که حتما باید توش عضو باشی
✅
چون راه پول
درآوردن رو بهت نشون میده
📝
حتما آمار کانالشو ببینید فعلا به مدت محدود عضویت رایگان باز شده فقط تا پایان فردا شب
🚫
⚠️
نمونه آموزش بازی Apple of Furtuneکه سودش تضمینیه رو براتون گذاشتیم پیش بینی های معتبر فوتبالی هم دارن
z22
:
📶
https://t.me/+MT03hkV78q9kMTc0
📶
https://t.me/+MT03hkV78q9kMTc0</div>
<div class="tg-footer">👁️ 7.31K · <a href="https://t.me/Futball180TV/103572" target="_blank">📅 16:26 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103571">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/48e9ffe2f3.mp4?token=Jupv-col1BH-NdEvcn-CyMawg44onJLn2g1nGjadwOHSum4JKEJIRXC9mB8pzYn3XQEAoJgcNHxP3CAWOf1YMonYM7tInrdkp1PSbTL8DyN8BTwqsJaxuxCDDLF_td_kuJxVTp3bHYTjGDZJ0ZqdWr36hN9dT_OgGTlzjg1WN-93KNZHVhAahk35FmdmXDf5TbnmuSY889-7dys3n8eaurHunKsDUiIT68BJ1ahbirNXn9zSdgVScA3SYLAeE8H-LYHNj2g-Cmen-MoLYsnoVpZRP0r4uHCJyAlPfk4MVulFlg_RVfNX-HKnYBLuqdvKj-A-Eb_VByF3zy5f68NzvwPWp3rk_q7bLzUPylAuQL3bl33tkivTPOkypjjUd8JgF2oWUrM3Km-BGxT5UuYTQFPrsSxXA6QhF02GVLPouXUrv-0ntVOeYdNaWwp2f1EEy_GEDAI4jwU5svL9PqEoGKAcINY_Eynw4sN-cZcZ6zJJN7w6Eo-GvuvoG1qhO1ZTkrUOBms6yI9r6nXGJCdD1AgjhH5wXyZvhPkepLwQjkHL_KnBY4r3bArvsfPz3xTFZzbRZ4yGo6ONJOJL1x18S_INv1QFN8Vbhj7SLendMF_ETm8J7G_FZKnvS_qw96JxeceMkIcj9wEKi1fQB8eXzToTiJ1R3B-29Wdp8kCzw00" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/48e9ffe2f3.mp4?token=Jupv-col1BH-NdEvcn-CyMawg44onJLn2g1nGjadwOHSum4JKEJIRXC9mB8pzYn3XQEAoJgcNHxP3CAWOf1YMonYM7tInrdkp1PSbTL8DyN8BTwqsJaxuxCDDLF_td_kuJxVTp3bHYTjGDZJ0ZqdWr36hN9dT_OgGTlzjg1WN-93KNZHVhAahk35FmdmXDf5TbnmuSY889-7dys3n8eaurHunKsDUiIT68BJ1ahbirNXn9zSdgVScA3SYLAeE8H-LYHNj2g-Cmen-MoLYsnoVpZRP0r4uHCJyAlPfk4MVulFlg_RVfNX-HKnYBLuqdvKj-A-Eb_VByF3zy5f68NzvwPWp3rk_q7bLzUPylAuQL3bl33tkivTPOkypjjUd8JgF2oWUrM3Km-BGxT5UuYTQFPrsSxXA6QhF02GVLPouXUrv-0ntVOeYdNaWwp2f1EEy_GEDAI4jwU5svL9PqEoGKAcINY_Eynw4sN-cZcZ6zJJN7w6Eo-GvuvoG1qhO1ZTkrUOBms6yI9r6nXGJCdD1AgjhH5wXyZvhPkepLwQjkHL_KnBY4r3bArvsfPz3xTFZzbRZ4yGo6ONJOJL1x18S_INv1QFN8Vbhj7SLendMF_ETm8J7G_FZKnvS_qw96JxeceMkIcj9wEKi1fQB8eXzToTiJ1R3B-29Wdp8kCzw00" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
👀
بیاید باهم چنتا رقص دوربین تاریخی ببینیم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.92K · <a href="https://t.me/Futball180TV/103571" target="_blank">📅 16:05 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103570">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/acb4aa9e2a.mp4?token=jgkI20kUZQDynCfnWXlE_3cHicgwQeo0v5UF1EdN_T0VIlSWVXLYwIXbHTelspwI8wS6sL7l3LVYFWBSjaVx-kdXaGhX0K8sa8kdhX1MKUkuEp-V5Oz2Vj6VghhiAn6q72DqzsWRhkSK97Bobe_zG200RBiiR8g53pkblUas8y7A06RFWOo8bmZSz13gZQOj23AaFzrnuXYqGOse_aFJM9QboRv1TFu_COqTTCck0gtzByws3YLSuvqVs7BuKiKRt6RjMa-s37dEYyRgMbRLPo3NUGp9W-3HZnwzCe-w8eheS2K_UJN3WqhBZlr_Ad5_-v_goiGEvaYUvp1hqIvULA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/acb4aa9e2a.mp4?token=jgkI20kUZQDynCfnWXlE_3cHicgwQeo0v5UF1EdN_T0VIlSWVXLYwIXbHTelspwI8wS6sL7l3LVYFWBSjaVx-kdXaGhX0K8sa8kdhX1MKUkuEp-V5Oz2Vj6VghhiAn6q72DqzsWRhkSK97Bobe_zG200RBiiR8g53pkblUas8y7A06RFWOo8bmZSz13gZQOj23AaFzrnuXYqGOse_aFJM9QboRv1TFu_COqTTCck0gtzByws3YLSuvqVs7BuKiKRt6RjMa-s37dEYyRgMbRLPo3NUGp9W-3HZnwzCe-w8eheS2K_UJN3WqhBZlr_Ad5_-v_goiGEvaYUvp1hqIvULA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هوادار ترابوزان‌اسپور خوشحال از جذب صلاح
😍
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.06K · <a href="https://t.me/Futball180TV/103570" target="_blank">📅 15:40 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103568">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u1t_9g_Ed_a_YgH56petum2vQ16K-Ht0nNMcW0z_BUDB9iOb4UBmjJowwDdqWu3ql6HaWKV7va87DtQNVECkDvHRWcSJtUD9qudVva-6BdnlowJupUlxGGR-pa5T8EOXRFxe7sX4voP1pjLGeaiNXG-IopaD79qhjwNz1R4GPS4TqUMvdXey_QvXGdsN4EuIvcK-6-NF6PtnbvbT5FHUN7YZ1c0eTleV3cbffSZiSIWzwQL9umJVy511aEdJacLhjprH1rZDguV0OM5bDw9MBLoTHKU2T2I5034_-EBmn_xnS0Llk-2eh1xTADQkFs6aXDKg_EObXM18RXk6NZjudA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/20dcaf140f.mp4?token=HPKL80StI7yCQ75IyBN4f2gZgaWrfZWc8r95gHGi2sjYVj9tTNKzhGrleq9EyZnVtD79ZlKRrhD9G8453hjtxr35wb7qpXjbImM8DxU2Fq9Z7kU2NcVsshXrE_fM5DJ4_DYIndy3lqltua3yenieYvGgHMal29XEMCf6L9O77sUCYJZXsYSrl1GtbV6ew2iJZWbm5oKInc25fVP6Go1dC9Z1N-fk0l3y90RIKki1k9fmZdDB_um3o6XbQGvxxjWQ6h_akkmdaBhdmQbZD5nVTjVYJguXvQBMrOtJx1Q4K9yJrrQXitLyAhboOORHYoWirVkzdUFV7FCcTK0euSWhew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/20dcaf140f.mp4?token=HPKL80StI7yCQ75IyBN4f2gZgaWrfZWc8r95gHGi2sjYVj9tTNKzhGrleq9EyZnVtD79ZlKRrhD9G8453hjtxr35wb7qpXjbImM8DxU2Fq9Z7kU2NcVsshXrE_fM5DJ4_DYIndy3lqltua3yenieYvGgHMal29XEMCf6L9O77sUCYJZXsYSrl1GtbV6ew2iJZWbm5oKInc25fVP6Go1dC9Z1N-fk0l3y90RIKki1k9fmZdDB_um3o6XbQGvxxjWQ6h_akkmdaBhdmQbZD5nVTjVYJguXvQBMrOtJx1Q4K9yJrrQXitLyAhboOORHYoWirVkzdUFV7FCcTK0euSWhew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یه زمانی رئال یه مهاجمی داشت به اسم ماریانو دیاز فقید که از لیون به رئال مادرید اومد. جالبه بدونید 12 گل برای رئال مادرید زده ولی 13 تا جام تو کریرش با رئال مادرید ثبت شده
‼️
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.78K · <a href="https://t.me/Futball180TV/103568" target="_blank">📅 15:21 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103567">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f385b11729.mp4?token=PIVKoJVxOiVdVf8td5Cwx3XhxxSxUzb3ptbp6vKdFRas9RKvp18-nG7JqJdI4y2j8Ij-JQS2GhqcmPr2vsmz4IW3tBeP9vgBeWGgZv4BvArffy829YgMGwRToAaFKr_PcuGEEXxVP-8ABls7_T_Y1gKArzjNU8plrd89n9AaZqCxrz3beHqlPJoj30soCSIdec4mNKs84l7Z7iM80O7ljsa9Qz6fgi9mbo7VzYWSzypuSSYLAcEbgbwD53vsAR47K9BUden3AVhsLM8Wy6RuHU33vhAVgqHtT2l0qLsr8oHP7zBwXmJhAU2LT4aWoE2m2n05fNSXhFn5XBHIfxg1vw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f385b11729.mp4?token=PIVKoJVxOiVdVf8td5Cwx3XhxxSxUzb3ptbp6vKdFRas9RKvp18-nG7JqJdI4y2j8Ij-JQS2GhqcmPr2vsmz4IW3tBeP9vgBeWGgZv4BvArffy829YgMGwRToAaFKr_PcuGEEXxVP-8ABls7_T_Y1gKArzjNU8plrd89n9AaZqCxrz3beHqlPJoj30soCSIdec4mNKs84l7Z7iM80O7ljsa9Qz6fgi9mbo7VzYWSzypuSSYLAcEbgbwD53vsAR47K9BUden3AVhsLM8Wy6RuHU33vhAVgqHtT2l0qLsr8oHP7zBwXmJhAU2LT4aWoE2m2n05fNSXhFn5XBHIfxg1vw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
‼️
کنایه‌های تند مجری تلویزیون به مشکلات کمبود دارو و اختصاص ارز ترجیحی برای ورود ماشین‌های خارجی!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/Futball180TV/103567" target="_blank">📅 15:15 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103566">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dbe161733b.mp4?token=gPJd3V7rkNHgy7HBFBrPyvWbgjicTG4UPHsWqOT0xz2BA-EL3lfWfxE7_wGc1jtG6bxQuzd5JATLab7ENZzI1-OGPdelRbo_ZYNYu-3tIrs-2G4w3w9DpHlQV5mBjl73a2pO-rYjAlW7UIaonbW8qurFui3sdr7O2aw0pBdzmsQwVe_p2HzIjzAfNnfloDn9cgC88Gv1ceMsOHQiSuoTBF58KXwX0EjmLiUiljVH6wSl6eV38QMeIS3al4LVpcxJIrgMf4uHcajtwzjG8jjqUqUbzbFRSTB-WJVvdvGv_KzLZO1gBpogUTCTDiI0ihdLEgUbeUYbVXftkap5ZdfbiIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dbe161733b.mp4?token=gPJd3V7rkNHgy7HBFBrPyvWbgjicTG4UPHsWqOT0xz2BA-EL3lfWfxE7_wGc1jtG6bxQuzd5JATLab7ENZzI1-OGPdelRbo_ZYNYu-3tIrs-2G4w3w9DpHlQV5mBjl73a2pO-rYjAlW7UIaonbW8qurFui3sdr7O2aw0pBdzmsQwVe_p2HzIjzAfNnfloDn9cgC88Gv1ceMsOHQiSuoTBF58KXwX0EjmLiUiljVH6wSl6eV38QMeIS3al4LVpcxJIrgMf4uHcajtwzjG8jjqUqUbzbFRSTB-WJVvdvGv_KzLZO1gBpogUTCTDiI0ihdLEgUbeUYbVXftkap5ZdfbiIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
ویدویی که بارسایی‌ها میتونن هزار بار پلی کنن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/Futball180TV/103566" target="_blank">📅 14:50 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103565">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5263acb67c.mp4?token=TTzo_n7O67WTW4HSct3iB_Ktk8OE9mkG2Sdb6o57U62npMJ0BGM7UeOlNZVOz4mnz9GVulOUIKJSiVPuOp8f9_lO-j0ts7c7T0D81onw4VENc9cgnrfLjlYNZoZxCZxZj6CBBvvQoHgMSTLmmLA11iF763YABcrNxHlgZCzDLw90Ap1KxATKYGxCn0eGt_24usnYKTHvpTqt3IY41pKM1eAjDXqKopPkI1P0ELLuTBlY2F3Be23KjHOPjlDyE8stOsYRRC4Mo39SXWZq8yc8CR3Hq2CggwNhzn5EHN36TCqD7D_W1tp0JWkPNrKM1Om_L4raWUWivH-kpocZDcrOdg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5263acb67c.mp4?token=TTzo_n7O67WTW4HSct3iB_Ktk8OE9mkG2Sdb6o57U62npMJ0BGM7UeOlNZVOz4mnz9GVulOUIKJSiVPuOp8f9_lO-j0ts7c7T0D81onw4VENc9cgnrfLjlYNZoZxCZxZj6CBBvvQoHgMSTLmmLA11iF763YABcrNxHlgZCzDLw90Ap1KxATKYGxCn0eGt_24usnYKTHvpTqt3IY41pKM1eAjDXqKopPkI1P0ELLuTBlY2F3Be23KjHOPjlDyE8stOsYRRC4Mo39SXWZq8yc8CR3Hq2CggwNhzn5EHN36TCqD7D_W1tp0JWkPNrKM1Om_L4raWUWivH-kpocZDcrOdg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
لحظاتی با مهارت‌های تماشایی کیلور ناواس ستاره سابق پاری‌سن‌ژرمن و رئال‌مادرید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/Futball180TV/103565" target="_blank">📅 14:25 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103564">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Lw4Jbwy2vX6yIMMUKNT-tmRzoz7eVOCwc_9Ljd_QTxvIqyQC07PYKWNmGRkETKGeyEqpeacBCUPoJlKSmzNdqZkF5tNdSVz5ZdQVCGdxTsgb_WbkUopT4yo2dTUs4AQzEfn73wnx_7hQHrwTUUNStVvVqsKR_YB6DY0mYLLTIUMxtinH_a71WWOR2t0yF29IXJBLJKVGOQqA_WHW8OGVtgqhed2ZcUN9XFm-TeFVwWZ1xM_5cfYn6SP7nrLj1LH2xeSZMPZ000HLFI5eZdZyb9R-k8RKoywhgpTAiCOZX8g2D8wt8G4hK7zTRvALWl6TeYc6I0kc-dseBgbwr9AS1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇹
🇮🇹
🗞
رومانو: دو باشگاه اینتر و لاتزیو درحال مذاکره نهایی برای جابه‌جایی داوید فراتسی هستند. رقم پیشنهادی لاتزیو ۱۵ میلیون یورو است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/Futball180TV/103564" target="_blank">📅 14:21 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103563">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZhsAAkGjvBIRyVRLSOrXqaZxsC-mMVY9zclVE2ua6KepMy4zc9jcocCnMkFfOqXg8WWuW4iJIwo4q8h00IMWYIZxyskwjEgmVRuiNzKBn7LQgQeyQr23ZLfhzRcmOXUe8mNdsufy_lKUREP_Ojz2lwMYvmdfdaQwRjyL_siqpkROElwQuTk0fUPd1ajUE3CJjHczp5rjQop3rJsaMVIT36v6HPY97pPP6b7NfmlxZOFVgs5rG1LmzbjbgyUa9JPJ-IjLI3LPIL5DsDQ3wBleJRW08OMxQYsM_u3DmGNwJzcmTLugyBKtRBVipDSy3umZBRmzWnbKsN-NGiHOkv7Ucw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
سوپرجام اسپانیا در استانبول برگزار میشود.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/Futball180TV/103563" target="_blank">📅 14:14 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103562">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/734a158141.mp4?token=jD7RJDqZ8dbfDt6gDnh-gETzr5EC0BmcXN84kARkq5r6WWI0WfLI7RXooW5PNAiR6LTR0eNpbUX7bp0_W2FegYBkWEfKrH0K8C9RaQytxymB35UP7dqL2pVh1I5tomtF8WadXPg8enPHR9LZwCWB17g4yIbhWqE7oeV57ScwDzGJvw20unU3zNt-Be1a1YAEg6MSjE6bRa7XunU7O7NiYbpbTmkze_uxC_Xe-Ih_uZxBQ_ubq-o7ayDHAobA_nAG_X4i-cKPVM1SbGV0Ikh9jSGUdocGZrykUbEsc99s42BoOZVI8FP3rgk6bFeswaUcE6p55awnofYmxGYraYOITQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/734a158141.mp4?token=jD7RJDqZ8dbfDt6gDnh-gETzr5EC0BmcXN84kARkq5r6WWI0WfLI7RXooW5PNAiR6LTR0eNpbUX7bp0_W2FegYBkWEfKrH0K8C9RaQytxymB35UP7dqL2pVh1I5tomtF8WadXPg8enPHR9LZwCWB17g4yIbhWqE7oeV57ScwDzGJvw20unU3zNt-Be1a1YAEg6MSjE6bRa7XunU7O7NiYbpbTmkze_uxC_Xe-Ih_uZxBQ_ubq-o7ayDHAobA_nAG_X4i-cKPVM1SbGV0Ikh9jSGUdocGZrykUbEsc99s42BoOZVI8FP3rgk6bFeswaUcE6p55awnofYmxGYraYOITQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">داستان رامبد وسط برنامه ۹۰ رفته دستشویی
🤣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/Futball180TV/103562" target="_blank">📅 14:02 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103561">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uPVGjUu4vYNb5dSlerfER5vp1-UPEKNJ0o68LPZZ1k4hKMTmc283d95kPGNAgxRRj47ZGAyn5F7OTizBPsxU3qZ1qeaU_yBPhG2bk-Ux05BmUO__6QTxy7mQdPRKakZsJA0v4ijL_jyTxsnTNSTvcYB1pc3MKy50ABEk8rL7Xl1i7A63DkyG8W4rBxbL-BcJvEaHTADY0fcquN_uBYH8AN0Ub7yZFT8FXQyrxLnWlFdfvF2cA1gQg_S_AF752c_jjCM9IuFjPTrMunCHf3hwa-4aMmSEFJbAh484-sDWHQLEjSpNDV9rCErLQreUP3zL5HL7QpJOu3ERIKwYOG10FQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#رسمیییییی
؛ جرمی دوکو تا 2031 با منچسترسیتی تمدید کرد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/Futball180TV/103561" target="_blank">📅 13:45 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103560">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/372ecd711b.mp4?token=iyLp-L0VL8tCH46AXhXFp4DvJbkvMEInO6XgzKTWnV-46-tHg1yDMXCmC0p3dtWrBeyqqvuxE9CgQu4FcMYhzEPZx--gsNE3gxa5VQaHJp7nzemMeRbK7ZgHu9WuHPXxR-cFFLl9JX_UW8M6QExaunQAO2_xpvRtfoe2bsWanTZ8TlKc1akmNylx-nn-a4tU5UkK8xjfj_pvkY6qp2Cm6AXBTtJkV-v6_tHOxKtnMNgD8Z65GAhQB2VIUVAHsXVWF3aFzDP5vRwZyjMiTYp0CS-fVHDaZIr45Hwa6ebFanIHyJVeY-wbygU9O7PEhUwVkcar2MqaIzKbWMKZp_Rl0Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/372ecd711b.mp4?token=iyLp-L0VL8tCH46AXhXFp4DvJbkvMEInO6XgzKTWnV-46-tHg1yDMXCmC0p3dtWrBeyqqvuxE9CgQu4FcMYhzEPZx--gsNE3gxa5VQaHJp7nzemMeRbK7ZgHu9WuHPXxR-cFFLl9JX_UW8M6QExaunQAO2_xpvRtfoe2bsWanTZ8TlKc1akmNylx-nn-a4tU5UkK8xjfj_pvkY6qp2Cm6AXBTtJkV-v6_tHOxKtnMNgD8Z65GAhQB2VIUVAHsXVWF3aFzDP5vRwZyjMiTYp0CS-fVHDaZIr45Hwa6ebFanIHyJVeY-wbygU9O7PEhUwVkcar2MqaIzKbWMKZp_Rl0Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رونالدو: یک آغوش بزرگ برای تو و خانواده‌ات در این لحظات بسیار سخت، لئو. قوی بمون.
❤️‍🩹
🫂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/Futball180TV/103560" target="_blank">📅 13:40 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103558">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hzEaY5IU827KnCrUO3kH2NHVOxNisXkY0BDMl2EK064HJSLC6TfBaz7K5UyIfMknIOXVLPa03HI9owhMCzvK4rqi-jyYTnJQG3gEmPhQbgZaUyA12yqWEDwh3EwSpEf5_ekONKULXE_KfWTDQaVy5k43wVuB2l5jjlGWoz1F70caPULrEHY_T6zk4g1mUgwmsS2FE5mUclZjM20ZxgtNfuZtHMysHcpNG7HJUZRQQOBJesWqkNLgaOKu-VvcIoeDNFhh1ipUv4xxLFj3eKSXb2fm7T3kJMF9X9L1voiVWFwfWU5sZVnaivqPq7e64PCKXhCpmG-yRbbSOqOFC2DMqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ku0C_2qW2awoLsavkDlmFZaqYN2jpIZHsBNLdW8-hcFEiaNfJvZAD-Kq6SZuqNbL57nrKlsjlqqnUtGb86CIl9m4hlMWEcG5BOjpfsH_2LhGrbrDTTc3mXMg1u1f-lAPpd5vhKjDjnAtZ3hgkXp7nCAfuqYN6EplRnmOAdUV5M4ZQNauguixtJv6jlggpdfE-URJ0j3vDRDv37jwGXx13eWvDGOyK-AV4Qlyht1mm1xprFPo-Cno1F-J85zjyTdWMu3ppG3RuMyu670vaMUfQARQGXxnHMFJLIj45HsioNyC4rGJCNblXL1a5taPbcJiW8a71_Ll2cgskipHet1gyw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📱
کامنت‌های سمی ایرانی‌ها برای پست رونالدو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/Futball180TV/103558" target="_blank">📅 13:31 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103557">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f44077de54.mp4?token=CFjLG5VhMZogap-mOUI9vVNGxA6hNECP5tmOyeZ6JdySyqlwOTU_A0sP-XZJmm2eyynr7oZxKLZf3Rela2TWSMs7RjKhEmLy0Q6y8nuklwwOUPNTzZTiFPYGfkn-QeZK9rGy-aj9djUiVQSd-qC_R49CsUjiw1E3XVkPNPUKqWO5UeRTzJwcXqvAGCS98KEraYw45hcKrmoEZXQJmikad6uVITzW1hq2fG1kZYafYEgUXNt-cvKWc5JIctK78Cok8_mYL1xso8po-a08cyt5PmSWZYtpSwLqEMV2HRvyjx646oW1Yi3GW4ySF6j95JUIxWXgL_Ds42UHag8dlbkB8w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f44077de54.mp4?token=CFjLG5VhMZogap-mOUI9vVNGxA6hNECP5tmOyeZ6JdySyqlwOTU_A0sP-XZJmm2eyynr7oZxKLZf3Rela2TWSMs7RjKhEmLy0Q6y8nuklwwOUPNTzZTiFPYGfkn-QeZK9rGy-aj9djUiVQSd-qC_R49CsUjiw1E3XVkPNPUKqWO5UeRTzJwcXqvAGCS98KEraYw45hcKrmoEZXQJmikad6uVITzW1hq2fG1kZYafYEgUXNt-cvKWc5JIctK78Cok8_mYL1xso8po-a08cyt5PmSWZYtpSwLqEMV2HRvyjx646oW1Yi3GW4ySF6j95JUIxWXgL_Ds42UHag8dlbkB8w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
🇮🇷
ماندگاری، مدیر رسانه‌ای استقلال: درخواست سپاهان و تراکتور برای برگزاری تورنمنت 3جانبه غیر استاندارد و عیر قابل بررسی است. جام قهرمانی حق ماست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/Futball180TV/103557" target="_blank">📅 13:16 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103556">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/26d7de5b02.mp4?token=Ukt4OwxpyG3cqNTm4OIotZfaI8s9CCE3QByZpX4PIwJ2PMQGhX7tx8nvHpJRZ05ru5RDzS_mqHclqBGakmbufRbrsagIiBrwKGgsvG4bfXx6JBX11sogIA5Q7W0WLwTRuajyhTc-Stt9cqTls4FwlwbUXGkmyCKhT0eAhZvRCt939GweUdN6oghSDvFVH_BjnbaE2GDxPzhtMFIgXw4a4Y4hrOfhbO5c-YBU-Ela86Txlcb7RyO-V60SILsLQv82jlJMqkP0Ml29UvT_sGKfJZBEu4FgLKTxPLrMdZ6iXKCsCTr5B9EaBao7t5MSvEVrowFVvnDN5pgZWYMdNSHXZw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/26d7de5b02.mp4?token=Ukt4OwxpyG3cqNTm4OIotZfaI8s9CCE3QByZpX4PIwJ2PMQGhX7tx8nvHpJRZ05ru5RDzS_mqHclqBGakmbufRbrsagIiBrwKGgsvG4bfXx6JBX11sogIA5Q7W0WLwTRuajyhTc-Stt9cqTls4FwlwbUXGkmyCKhT0eAhZvRCt939GweUdN6oghSDvFVH_BjnbaE2GDxPzhtMFIgXw4a4Y4hrOfhbO5c-YBU-Ela86Txlcb7RyO-V60SILsLQv82jlJMqkP0Ml29UvT_sGKfJZBEu4FgLKTxPLrMdZ6iXKCsCTr5B9EaBao7t5MSvEVrowFVvnDN5pgZWYMdNSHXZw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
‼️
روایت ژوزه‌مورینیو از ترس‌همیشگی‌اش مقابل اسطوره تاریخ فوتبال لیونل‌مسی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/Futball180TV/103556" target="_blank">📅 13:10 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103555">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f85bd08121.mp4?token=cdZZA-lXliZFcRcaPZtZXwUeZBZoG3mFpeLQ89spJz-VmljLCZlqYqXuYknLnsIsq9mk1HE8jR8_lgC9mNG4thE_vLLApV_OBo_HiMaPZdRBxjZmgl1AgIeounDmHo82Zgvu3TfmLMQiov4abWpEBNXhWWovOi3RiM6LkYUFcn5oukVQrgChZ_ptG9aBmCL-LSgU4dEwMUWuxkMbiL7EO66aHOqwDuXTbBE_A_xtFVa6btDNmKz4TfzTUSBaI4xWcKqxswaPl7v06ak6Fo8jyASBCge3zmxuOqH6kSOw05JBRL7jqtCQiRWGxP87bcuw52xvxNgOlS6XS1ekyZ8mcg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f85bd08121.mp4?token=cdZZA-lXliZFcRcaPZtZXwUeZBZoG3mFpeLQ89spJz-VmljLCZlqYqXuYknLnsIsq9mk1HE8jR8_lgC9mNG4thE_vLLApV_OBo_HiMaPZdRBxjZmgl1AgIeounDmHo82Zgvu3TfmLMQiov4abWpEBNXhWWovOi3RiM6LkYUFcn5oukVQrgChZ_ptG9aBmCL-LSgU4dEwMUWuxkMbiL7EO66aHOqwDuXTbBE_A_xtFVa6btDNmKz4TfzTUSBaI4xWcKqxswaPl7v06ak6Fo8jyASBCge3zmxuOqH6kSOw05JBRL7jqtCQiRWGxP87bcuw52xvxNgOlS6XS1ekyZ8mcg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🎙
🇮🇷
سهراب بختیاری‌زاده: شرایط‌مان عادی و خوب است. نمی‌خواهم مداوم از شرایط باشگاه انتقاد کنم و گریه کنیم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/Futball180TV/103555" target="_blank">📅 12:48 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103554">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/84923651a5.mp4?token=Y6joPDAKJc-WRkWRleyyHg-cxgVpNEZGINKNJv9irzroi-UW2vKh5hJIEYFVo20mOSYnC-KwiqR06eS9jII7FQuVrC3X-sxrj_MKaDeB_pjnGCHDpKpd0A-SuL2Fzug3ZZTm93AHCYAu6kU8bHx_w4IOyppj71viQJJ-BkbXtf2beNJClcoev_RqIOS2qc7K4L7SbXryNCjYVqYLYPDjdca3EKFE8dEY9iiCu_OBG3OqzQDF11uXVhhMhBwhmhWkPUAtXaPLv9211y0p6dD4ZOs4hNkQM0DQbsiGh5OeCYA-Jn_X5_LqYPLyxChDwu3fJFHuLPu1RLz0GtMeCUPGNQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/84923651a5.mp4?token=Y6joPDAKJc-WRkWRleyyHg-cxgVpNEZGINKNJv9irzroi-UW2vKh5hJIEYFVo20mOSYnC-KwiqR06eS9jII7FQuVrC3X-sxrj_MKaDeB_pjnGCHDpKpd0A-SuL2Fzug3ZZTm93AHCYAu6kU8bHx_w4IOyppj71viQJJ-BkbXtf2beNJClcoev_RqIOS2qc7K4L7SbXryNCjYVqYLYPDjdca3EKFE8dEY9iiCu_OBG3OqzQDF11uXVhhMhBwhmhWkPUAtXaPLv9211y0p6dD4ZOs4hNkQM0DQbsiGh5OeCYA-Jn_X5_LqYPLyxChDwu3fJFHuLPu1RLz0GtMeCUPGNQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🎙
🇮🇷
اولین کنفرانس‌خبری فصل سرمربی استقلال با کنایه به رامین‌رضاییان
🔻
سهراب بختیاری‌زاده: بازی دادن به بازیکنان پایه در استقلال سخت است ولی در فصل پیش رو حتما این کار را می‌کنیم/ باید به جوان‌ها بیشتر بها بدهیم تا اسیر بازیکنانی که تحت تأثیر فضای مجازی هستند نشویم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/Futball180TV/103554" target="_blank">📅 12:44 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103553">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TyDBQXye4HozU8HIACddjQU_-8buOFtRRJePdBNcOMI1jPyKSuI7Ow1Q0gg0oZXwHOZ80p5zqZNn-UoKKEHx_C11_VIojmXOZ7g4VMOalqs60GPlzy3DC4e_Z6R8y1ZHyUH-BLhAO5U9KuDLsd_uNPyXCJTtTERcIoGYkk5yBR47G_959LJZXovzGkGsN75QRbRtDbzpX1qxnFwbf5E61iEm0GCJ4RKxO7Xt3rL4YUvbp0CiyEV_xqpmk-0tQfOac71ie-gmeNKupAfMQq0mJlxi5YPxjhEdgitWxojFOl81vs5c78Bl8Th4Li_jZTBLePe4trK_t2DfP29jHManHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇪🇸
🇮🇹
رومانو: بارسا هیچ پیشنهادی برای جذب لائوتارو ارائه نداده و اینتر هم از طرفی مطمئنه که کاپیتان خودش فصل‌آینده در تیم موندگاره
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/Futball180TV/103553" target="_blank">📅 12:41 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103551">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/985e98ad84.mp4?token=WdDHufqQfAOcnNBqerlPLMMArw0UzIF5sSVxwc3eKxBtuUM50E9sFLBG9beawnWwr7SjEabYcow0liu_Gi5mNYL8V69hvC0H8fND4c8qPlDtP2OxF-Ji7pCqDdTniJOrOaItdmHuNTCxB-QfQuaat6op4QCYgUXjJWy28gxuK_jufaNdm3IGGfgNV4VLsCZQSm8kjfoo45j4O0PWKvSg8bqf109ROvTpdn_wTscJyYQku9OjGXl2Vl3fPmSXkosSlCKMigZ8lpjDB_Ke2QmmvgY7V1KhiTsYkFvZyHSk2gt3bx8J7nVdUO_iqY8M1ZmsPj-pCO9s3IodJ_YVckkMyg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/985e98ad84.mp4?token=WdDHufqQfAOcnNBqerlPLMMArw0UzIF5sSVxwc3eKxBtuUM50E9sFLBG9beawnWwr7SjEabYcow0liu_Gi5mNYL8V69hvC0H8fND4c8qPlDtP2OxF-Ji7pCqDdTniJOrOaItdmHuNTCxB-QfQuaat6op4QCYgUXjJWy28gxuK_jufaNdm3IGGfgNV4VLsCZQSm8kjfoo45j4O0PWKvSg8bqf109ROvTpdn_wTscJyYQku9OjGXl2Vl3fPmSXkosSlCKMigZ8lpjDB_Ke2QmmvgY7V1KhiTsYkFvZyHSk2gt3bx8J7nVdUO_iqY8M1ZmsPj-pCO9s3IodJ_YVckkMyg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🤯
تصاویری متفاوت از خورشیدگرفتگی از داخل یک جنگنده و یک ایرباس!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/Futball180TV/103551" target="_blank">📅 12:34 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103550">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oCIuovaqFnVjjsN6JtMcbMX7cjCnj6gndwn_tpgis5LpGcKaBWKLAmC6pFskpnyubvM86dHP6bCq__d9WSMo9eP4AqmaKm0iDEea19fPx_e32S4i2eP36TgWbOeOAH2F12t61XMLJOdZM5lS8jKA7ur0b56gQ6JRKUoQK_6uyi3evUER9K-j0tzs0GMf6jMmp4qiyi5wGogHElv0ZJQXqtWUdgVKxFtkyMSaFaPwhdopWV3VlQNUCgxbGQ_c1LJYGuFEIOSVNDlmb86mxlAkvpyIl9gcLc8QSDVQC5BlPI9GEwb15Yr_a5dJxYovjjlMi56qxWeCPmGzgw0iuIAN3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
🏆
برنامه‌هفته‌اول‌لیگ‌حرفه‌ای‌عربستان که از امروز آغاز میشه؛ رونالدو بدلیل مراسم عقد و عروسی خودش دو بازی اول النصر غایبه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/Futball180TV/103550" target="_blank">📅 12:24 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103549">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/954fdc44b4.mp4?token=nvkn_p35SHcvVbeX_E-peDvqRSxeiX0p-dL8SjBsUtUBAFD1IMeRdqX49fDKJqU4NAM08OOo15Eanpo10nYwd364c8BUFbD711FuvbaRy0IKoCoCBD-uh6Xs16100e4UQv-6D6EO2-dEVmCODoe200orCwWMkv8m9ephIrTrVMPYrIG36PnX7lAYg-curX9NZElf3etHp3jDUb4XR25Ju-zf2IEPt-tRpR5tr1u7dOpGyO_1S4NcZp3-3HGFFe4vCyjUFuYR5oXSiNF8rw93yS1J_QKvi6R6hjKSbpyMAJf_CFYjaOmGrl-Jb2PG7lE9d-Uy8ndkTc_3QuCavBCrHA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/954fdc44b4.mp4?token=nvkn_p35SHcvVbeX_E-peDvqRSxeiX0p-dL8SjBsUtUBAFD1IMeRdqX49fDKJqU4NAM08OOo15Eanpo10nYwd364c8BUFbD711FuvbaRy0IKoCoCBD-uh6Xs16100e4UQv-6D6EO2-dEVmCODoe200orCwWMkv8m9ephIrTrVMPYrIG36PnX7lAYg-curX9NZElf3etHp3jDUb4XR25Ju-zf2IEPt-tRpR5tr1u7dOpGyO_1S4NcZp3-3HGFFe4vCyjUFuYR5oXSiNF8rw93yS1J_QKvi6R6hjKSbpyMAJf_CFYjaOmGrl-Jb2PG7lE9d-Uy8ndkTc_3QuCavBCrHA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
🎬
ویدیو بسیار کاربردی برای‌دوستان باشگاهی که تمرین پا قراره انجام بدن؛ سیو کنید و برای دوستانتون بفرستید
❤️
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/Futball180TV/103549" target="_blank">📅 12:20 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103548">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M-97XaHZ-AOTc-F5M08fWPs_xu9ESQ-aBawVOJuw-l-xoUSjRbDkXJUQbTttk0YiYnu_5WaB_dgYiIr-_WdoXXqfrDR-cf6hTAwi6E5ryDd8OSzKILrelqqtDuEgZ14IPhLPQQOOo0SYBdSprDWUMfTBMNJfbXbnbo12D8kMf6BwCNBu8PDv7bEHREylO26q21_9FYVWYBf_prbZ_3lrfFcpFA92-19szz8-5aMQFApmJlEtvs2AVijhQdodOaKrT081qIReSl7SNl-H9DqfGx3DhIzBWeEmLvv9c20nBZ1_R9KYbVAPYOOdjX6YweIxpTEA0cadYzW6WLMLd_Eekg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚜
باشگاه تراکتور از کیت اول، دوم و سوم خود در این فصل رونمایی کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/Futball180TV/103548" target="_blank">📅 12:18 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103547">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gme7wtmMPosTeUa_2KPwzuYq0NxB6Q63lm9UDg5QVZtEKIRVU1HqjF8I7fNn6MrUD2a2nLiSvw2wDCJeJiLy8Y-hUschEcji3pS2RsCGlXnu2HdndlM1XJzz6OjWXsdCvVceyt4_3DsdUC1cE6WC6SR6hYbKgcnUd30rjXQqvFaJScQjcN6rUyJTaAuRY1GlynI1Oa1vftAn1EPWLujE9zDQTsujvLBg6NRvDRtXLlA_PoywUHt4WN_sPD5j5WJkWs1fmGNgAhIfo2ddM5jpmj_pHmtF4UAhPPWauJIPuHSty3edivFLYRN94yWMj8rX6aRFqsNdNEPgsKShSqax6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
بن جیکوبز هم تایید کرد:
منچسترسیتی پیشنهاد دوم بارسلونا برای جذب رودری را که حدود ۶۵ میلیون یورو بوده، رد کرده. مذاکرات بین دو باشگاه همچنان ادامه دارد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/Futball180TV/103547" target="_blank">📅 12:17 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103546">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UllOQ7iCclfjjBXgmZxfrorw5ZqY9K7U_H0ZPTkdeRScCl6TFJW7IGEsKq2ey8IO_JxXOZLcUnWrQasFrLf7j5lFnulXGnfba1fDGVTtITOa1jo90fhkCxPdeeMJQq1xkIjLxobfMHZjvPpBi9kNOELlbgHekzH00yn9xOcZcZOtBrPVxmK9OoTXywpSwrGaRnNufZishmyLP2VcOEe9Jt83R6zFGsboldS7JsztckgNK2BWG8OV6siawcDaJnNV9uPUY4gjCzIq6y112KOOAcGC-I-IVBYUdWF1lRha7qjRBeUha9uddnHtZ9jhdKXE9If9TxmMvCDuigZMtHhrJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
🇹🇷
ستارگان سوخته منچستریونایتد؛ بازیکنان بزرگ فصل‌آینده تیم فنرباغچه ترکیه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/Futball180TV/103546" target="_blank">📅 11:55 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103544">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vk_LkYXGJ9aqn_tdOXHvUATMihK_TC4oATOHCIcW9xMK7vmxvp9E8TxYg0iv8IUWqNgDhBJROuKMcrVpBLoSE2Lia-LExVIJlBDREKZpFons_GMtpwhP7LwKBBsNBc1I8uvd32f-Ii1Tf6Lb9atDnlwT8T67QJuEo0LN2gbbItr4ZejQNRQQR79fHDvUPfVj0yET6dTtFbRIKeja33mG6h9cTmjwdCpYrWS5cfyRa6HcNiwl0nVMQeqUgmOvHMgseXHqOseg6QtoP6kE4vJUUIJZRgnS1ZLFEHKiSTBUpwLHmh9Rrxzsce_2pzpbChN8RF4Jq7JFqbz3qNkHG9LfxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6e13d26513.mp4?token=DBgZac1MBsX7zsXt5f02QzhoYUgqIm0TMcn4Q7MM0j6g4LEySDLpvF5h7p8-5pVU-7e1ivTGIqLTsxRVO5smm8O0Ki97ZcMlCkOCO_uW3FmJ0EfTh1A-TtCCYYmXBpy_ydvMA5BL2LEgHhCKVu5px0o5EO4txPROeWs5hEJBBXAR2hGHi45TKsKJbG8h7wbFY3JUPahqwyRZ99aIvsj4DKzF3mSEYUi0YT8K2g9I70-tiQN5pXr2ktX7u-3YEVc4mQrU7XXRKuTbyF-Zm8wmL-pFD0MzsNnC-qotyKXfDinf7XigJRX1rMKMuSna9UtEkoVnEKpDm7U0j4OxErRftA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6e13d26513.mp4?token=DBgZac1MBsX7zsXt5f02QzhoYUgqIm0TMcn4Q7MM0j6g4LEySDLpvF5h7p8-5pVU-7e1ivTGIqLTsxRVO5smm8O0Ki97ZcMlCkOCO_uW3FmJ0EfTh1A-TtCCYYmXBpy_ydvMA5BL2LEgHhCKVu5px0o5EO4txPROeWs5hEJBBXAR2hGHi45TKsKJbG8h7wbFY3JUPahqwyRZ99aIvsj4DKzF3mSEYUi0YT8K2g9I70-tiQN5pXr2ktX7u-3YEVc4mQrU7XXRKuTbyF-Zm8wmL-pFD0MzsNnC-qotyKXfDinf7XigJRX1rMKMuSna9UtEkoVnEKpDm7U0j4OxErRftA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">9 سال از این سوپرگل تماشایی کریس رونالدو به بارسا در سوپرکاپ اسپانیا گذشت...!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/Futball180TV/103544" target="_blank">📅 11:47 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103543">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e210c19682.mp4?token=J96iAcNENZxlw0yaiaFnx9mzU12xZu6cZt0Th2ukey_ZmEUKS5nI7g37iTxg_lRrTuAX9D6AZltoG4CatxEnNjkETdqZ-pweTKj1-USvGpz8AAefUz2sfOFhnh7124Sb5u-qmjGQfY0UMqP4wL2iAvuk0dlcZGkDk3Es8WQij5n9pWx3AkavkpGvgG9oH2_UUFyPbaMG4i8GT0FT3_A794cYUDpkHxP1Pc65_pE93AAT8fbSPayt0oi5hCCgCYMqHcbKW5b1f1bug626Nrth2MwoWYK5lgdXoI2rk7BBp3XgnXNB1ctFs6Q8lC5jwLaDNTPl4T8T0765FopDA_uKIHk_-U8gsb_gef4a-HPE7VQ4tx2tTjBntPzuQLE7n_Qf9LbbG3_uayeORT-K33g4himPFzRgx3QJ-InksPUUElzsECPrZ_k4NIvREDsCqexFZ0N1aCtReBf4SLV6P29TVPa2XmAhuOkp6yCGIF91ZgX7eOVP2sOW7ch0XBks84hvOD07mZf2dEFEfbyUxTpVNH0TavQ1iYr8zRb4SDTolL7V86YUO3M_3bzhiPrDWkZ0U9DbO8feul5FasoXu9dNOQdI7jSQfkww6EVFPmfXSOOPsSgGBxdC6sdjIFH8nrWAaZ8kH5kGsdryoKUaWe4mo169sRdpB9Qgf7lJApuR9LM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e210c19682.mp4?token=J96iAcNENZxlw0yaiaFnx9mzU12xZu6cZt0Th2ukey_ZmEUKS5nI7g37iTxg_lRrTuAX9D6AZltoG4CatxEnNjkETdqZ-pweTKj1-USvGpz8AAefUz2sfOFhnh7124Sb5u-qmjGQfY0UMqP4wL2iAvuk0dlcZGkDk3Es8WQij5n9pWx3AkavkpGvgG9oH2_UUFyPbaMG4i8GT0FT3_A794cYUDpkHxP1Pc65_pE93AAT8fbSPayt0oi5hCCgCYMqHcbKW5b1f1bug626Nrth2MwoWYK5lgdXoI2rk7BBp3XgnXNB1ctFs6Q8lC5jwLaDNTPl4T8T0765FopDA_uKIHk_-U8gsb_gef4a-HPE7VQ4tx2tTjBntPzuQLE7n_Qf9LbbG3_uayeORT-K33g4himPFzRgx3QJ-InksPUUElzsECPrZ_k4NIvREDsCqexFZ0N1aCtReBf4SLV6P29TVPa2XmAhuOkp6yCGIF91ZgX7eOVP2sOW7ch0XBks84hvOD07mZf2dEFEfbyUxTpVNH0TavQ1iYr8zRb4SDTolL7V86YUO3M_3bzhiPrDWkZ0U9DbO8feul5FasoXu9dNOQdI7jSQfkww6EVFPmfXSOOPsSgGBxdC6sdjIFH8nrWAaZ8kH5kGsdryoKUaWe4mo169sRdpB9Qgf7lJApuR9LM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎮
این داور فکر کنم اصلا کارت با خودش نمیاورد:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/Futball180TV/103543" target="_blank">📅 11:41 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103542">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">derbybet.apk</div>
  <div class="tg-doc-extra">53.7 MB</div>
</div>
<a href="https://t.me/Futball180TV/103542" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">✅
اپلیکیشن حرفه ای اندروید سایت بین المللی دربی بت
✅
اسپانسر لیگ انگلستان
👑
امکان شارژ و برداشت با کارت بانکی
⚠️
برای ورود فیلترشکن روشن کرده روی کانادا یا سنگاپور یا آلمان و ....
📢
😀
Telegram Channel
👇
https://t.me/+c5jwC3lt9z45NTE0</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/Futball180TV/103542" target="_blank">📅 11:41 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103541">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZhgUIh4MOjMTuwSVsgFI090b6wmX0IZzN0W2-alDVHnf1Z8rjWzdy9e4OI73uBKSTFkfopmlSfI2vx-lTENqWRRRdi7Y_7LbCd-Xz_dfOhCauvVGN3EhOMkZ1nEjoLAHWFUpiStJ9GDA2RNSwXibUDy3fTfZ9_FA3bJdpcAeF5Il_iQyDwElktdUxRGpvD4PkGD9zTPnZa9V_f4CZLaymZDKW925DoGPSjg3Rczwa395-IL5zm73_g2zovDx19n60VrOP1VXfdnlK2hoi09dwEH4YOCitAGXWSuVpI5nquYyshI26pX3kDjVpY_d-MQzLfPMGSgpthwrkRXCNkzMzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😤
میخوای مسابقات فوتبال پیش بینی کنی؟!
🥇
پس نیاز داری به یه سایت بین المللی و معتبر
🥇
⛔
دربی بت
همون انتخاب  100%
💎
ویژگی های سایت جهانی Derby Bet:
⬅️
امکان شارژ امن با
کارت بانکی
⬅️
واریز اول دوبل شارژ می شوید(بونوس۱۰۰٪)
⬅️
پر اپشن ترین سایت فعال در ایران
⬅️
تسویه حساب کمتر از 5 دقیقه
⬅️
برگشت بخشی از باخت به صورت هفتگی
⭐
دارای لایسنس و مجوز anjuan
🚨
کد هدیه ثبت نام:
GG007
⚠
️برای دانلود اپلکیشن کلیک کنید
👉
r22
🔔
کانال دربی بت :
👇
✅
https://t.me/+c5jwC3lt9z45NTE0</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/Futball180TV/103541" target="_blank">📅 11:41 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103540">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R_OnI88bVNS0V-j6toOHvk2HgDrpt5DRYvE93L4xfY0erRwj4iX0Q_tztVdACGRoamguGOOaQN8uBYQTV6fmOOzDJsCGN4j8cJhCfS3ctc4P3VJehBmSnZhmyTiLKYltNt4rDxLPPgQswfPpKdMIdW3bRVy0sWcQ1MO_b40a5EggZ40TWseW-zjKvdJ5w43RncmJrtNpywYH3AO80eU9njyeVtAunNx-hbBSPHDFm_NdbrmxNp-revoDPG9EsYUNC_d0o3sew6xv8Cj0uXbjd6nhuJqrUgn5XR7yXB4JLgOIdTn9DlrdZw3HPvLNyBcxEzPoQZIggZ6CXs-ResoUwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
🔻
بازی‌های موردنیاز اساطیر برای زدن ۴۰۰ گل
🇧🇷
نیمار: 653 بازی برای ۴۰۰ گل
🇫🇷
امباپه: 537 بازی برای ۴۰۰ گل
🏴󠁧󠁢󠁥󠁮󠁧󠁿
کین: 631 بازی برای ۴۰۰ گل
🇵🇹
رونالدو: 653 بازی برای ۴۰۰گل
🇵🇱
لواندوفسکی: 632 بازی برای ۴۰۰گل
🇦🇷
لیونل‌مسی: 525 بازی برای ۴۰۰ گل
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/Futball180TV/103540" target="_blank">📅 11:33 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103539">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">🎙
تقلید صدا شنیدنی با استاد علیرضا جماعتی گزارشگر قدیمی شبکه‌استانی اصفهان
😂
😂
😍
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/Futball180TV/103539" target="_blank">📅 11:00 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103538">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C03MgwXO2R4bUSWX-OTjzw4xcGQA-nb31R3UJwxQDTtcpS24nvFFbyBecNVyvHXC6yspw3OtbHrLHotq_RTAOvODMvulPqhukaCjvhyti_qKAFDhfuPS2_NoA36SJrhN4jQwVHPp7Hl3Uv-MASGymsm8dRYQtfobXIa-sUjKhW5yYzi_P6Nyfbbpx_M1lbiI7BKInuQzXUkrhFfysZv_HxY8xQrLpo64_wieiveo4Zn5iYPeeVeUOKX4t4f7MzChhZiSBuprxaPGrTzGQHn5srLGxQTQRYkolH0BwR3GlwQdZNYIJft2krlZMAXV82eNvTEe3GE1q0GzWVIbzkNVHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🗞
رومانو: باشگاه القادسیه عربستان که در لیگ‌نخبگان آسیا حضور داره، با ارائه پیشنهادی نجومی به منچسترسیتی خواهان جذب تیجانی‌ریندرز شده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/Futball180TV/103538" target="_blank">📅 10:35 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103537">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">▶️
🇮🇷
ویدیوی دیدنی و جذاب باشگاه ملوان برای رونمایی از پیراهن خانگی فصل جدید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/Futball180TV/103537" target="_blank">📅 10:32 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103536">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qvF2ImCdnmSvXbjPFYqb-QsLrBBDInYrEVRMrk5ATXTsdS3Nn-gJPFryk0jhRWy9u_LvG6LNtDwT4m08ZHMraCyCtrosgpUlaJZLXsCydkg-Cb9wd8xFUxPAAkqCn7powe45DkARSJ_efFVJt32B1BIamMp-LjDJsBeVSwp22xmFRfPt6WCBkNJRQ7_GSS9b7jI10fCE_-eOIl1SHujDQbIK0xsvywUdQcpLKgQX0FvQHPgGjib_5S1u35TTLWATiHyHxjDuD43sk5QTfiUEf6ax0QU-GVTInqRDOPubFdiZ9Rj_48pVLBr-pjXje_Vb8Ni0XFCH8niHadJKWctsIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💫
تصویر روز ناسا
پنجشنبه ۲۲ مرداد ۱۴۰۵
🔸
عنوان: خورشیدگرفتگی کامل در اسپانیا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/Futball180TV/103536" target="_blank">📅 10:31 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103535">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/69a4112b9b.mp4?token=Hqm-hpQTQs2ZxRjDgCrnoTIep088xQKLlX21Aw5KGbpE9maOwuIhhD-t8T-foh0umi7xACIz-sabTd7MK9EZ_feSP9zVUn--lhtBYtwPTR_w76mnJqOGSiH9b-OoY9xXRe2dBIwoLY-mbsI5Rc7qYCg2VIqB0QGnkgBYbxm23TVZbghN-8GWG4Smk_WNiH-dR5740sCgwu_2zAmRsDpSxymHT0iB3Vx3O7Gzca_piytcUJB0DUFgMvj_oQED_z-xbSBQTNLv_aa0kZcIxs0b22RTDR8y9JZjQPrrHtpD4jOfIM5qmKVoa3v0mRehSrSJg6rtq0YtStUe445ePPzm3w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/69a4112b9b.mp4?token=Hqm-hpQTQs2ZxRjDgCrnoTIep088xQKLlX21Aw5KGbpE9maOwuIhhD-t8T-foh0umi7xACIz-sabTd7MK9EZ_feSP9zVUn--lhtBYtwPTR_w76mnJqOGSiH9b-OoY9xXRe2dBIwoLY-mbsI5Rc7qYCg2VIqB0QGnkgBYbxm23TVZbghN-8GWG4Smk_WNiH-dR5740sCgwu_2zAmRsDpSxymHT0iB3Vx3O7Gzca_piytcUJB0DUFgMvj_oQED_z-xbSBQTNLv_aa0kZcIxs0b22RTDR8y9JZjQPrrHtpD4jOfIM5qmKVoa3v0mRehSrSJg6rtq0YtStUe445ePPzm3w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❗️
⚠️
تاکتیکی که قراره برای بنزین اجرا بشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/Futball180TV/103535" target="_blank">📅 10:10 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103534">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/srVZCzJ82dE9R6lVRUpg1pSMT8HhkcCeCsTHEMHlSTzkLmD0hGTCREFPVDW__CjqriB7wn4QE_cWz0cHMazQay-g4gOjj-nl2td4ZsxBktP0RIwixhS77WXOPxemOu1twSsXGGfFzzHsWfy6E7v2AhofNiGSHUoLyNi1Odyq73mcX063ZSHWfrT7OB21RZpy2n9gtZ_LzHqHZakM7Yb94uz6hAr9ZDvVa55HnwIDpSZrXTmpbwLzUHB6NwsdghkgrVe7Lj7LQVWwobeNmCXSQGvcezkDi2KD9VaHBx1y8doK7gYLQJkvDrLLhZt32E14VLqwt0F6DJvbP4RujbCFIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
‼️
علی شیخ الاسلامی، دستیار فصل قبل ریکاردو ساپینتو در استقلال به کادرفنی این فصل مهدی‌تارتار در پرسپولیس اضافه شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/Futball180TV/103534" target="_blank">📅 09:46 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103533">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ddc4d6fef6.mp4?token=mnSM_apb_p1YIrJXysW-9qroID9Ygw7_bl2-HYYDOo1M2wRQp1gjqkCPwaRP7HR-p0hmW4ArVqxYpIYNtXPwhZi_bpy5bat5DohEzhvSf-eXCkid6ov_RBBQEdQPynolJ5thBJ3N6ZqqAPale5ZtJUPyQSmSepO-DkoptI5QY0bVkBUMRGqsPRDTdZJuQ65ga_L0EjFLfRttrQ23QBvz00AjTkP1rGA_8YT-4PQruM7v_l4641VRKdF6jvULNIgZ4m_HQ_0X4z9wd6V8Nv669D6TtUrAzliNN6kLvIK0iL9_zCB8RnAUHDlh9qJnUnKrOg_DC2F0kwigLca__jOtQl0ixU-TmJq9iCXrMytMH_nT7mwrRFcdzwZyKtieABgNcPWN4e4yuxBEBascxOD6kO4Su52o95wRX14JsSmEL-SdiQ3jncZQqXHaKvtww-3j53-q8hcNQdOPoSUgzqXEytbfEHiJEgIWtKIIVxzd2PeL0nmGBMpHSKtw0apT_Cdjqe1qW6f1AmSJYCRr_1EOrHujYgjniZ1YQaf98XdBWt78f3v9hgm8O8rdun3ICUbK_a_k7kMcHTJwl8gelFUWnuwmgktodOvGedLBDcBoKNsawvUhRPweIBYolaF2DQr_d3y8tvXtdZe4K23dyyOaoUmsfFtmtHKMJh6KtmaWn9A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ddc4d6fef6.mp4?token=mnSM_apb_p1YIrJXysW-9qroID9Ygw7_bl2-HYYDOo1M2wRQp1gjqkCPwaRP7HR-p0hmW4ArVqxYpIYNtXPwhZi_bpy5bat5DohEzhvSf-eXCkid6ov_RBBQEdQPynolJ5thBJ3N6ZqqAPale5ZtJUPyQSmSepO-DkoptI5QY0bVkBUMRGqsPRDTdZJuQ65ga_L0EjFLfRttrQ23QBvz00AjTkP1rGA_8YT-4PQruM7v_l4641VRKdF6jvULNIgZ4m_HQ_0X4z9wd6V8Nv669D6TtUrAzliNN6kLvIK0iL9_zCB8RnAUHDlh9qJnUnKrOg_DC2F0kwigLca__jOtQl0ixU-TmJq9iCXrMytMH_nT7mwrRFcdzwZyKtieABgNcPWN4e4yuxBEBascxOD6kO4Su52o95wRX14JsSmEL-SdiQ3jncZQqXHaKvtww-3j53-q8hcNQdOPoSUgzqXEytbfEHiJEgIWtKIIVxzd2PeL0nmGBMpHSKtw0apT_Cdjqe1qW6f1AmSJYCRr_1EOrHujYgjniZ1YQaf98XdBWt78f3v9hgm8O8rdun3ICUbK_a_k7kMcHTJwl8gelFUWnuwmgktodOvGedLBDcBoKNsawvUhRPweIBYolaF2DQr_d3y8tvXtdZe4K23dyyOaoUmsfFtmtHKMJh6KtmaWn9A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
اشک های غم انگیز پدر طالب ریکانی بعد از پنالتی معروف از دست رفته پسرش
🇮🇷
💛
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/Futball180TV/103533" target="_blank">📅 09:25 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103532">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7815ca585d.mp4?token=Xe86elQ3E8MvzGHbBXt2zxEd9KnncZ8KmC0rdlEXItM28xr6zEQnKO-BZdYS5iFfhTXZRdz-bqVMbk3skvDFqyah6I7mHHLZuOOD9jyptHOUpRqrQu5xeHBpBOuuZi5xzzMc520N-PW8Ud3TKxW_YQxAn1Gq0XMf3WuMJuSqZOdBFBEubj0XVB990icfG_MFv7XxHjnEmaSa5OBikvounzOyeaOICyqRlgOj0UIS4vli2T043l4COGzWeZc5p9q5HVyWDteaWs33xwWf5OUK8878PrDrpCLlAVCRTz8GHJebD9OPBIT4JOSNgrSZMe6xed2VjgyByBIgEUrCZDpcQg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7815ca585d.mp4?token=Xe86elQ3E8MvzGHbBXt2zxEd9KnncZ8KmC0rdlEXItM28xr6zEQnKO-BZdYS5iFfhTXZRdz-bqVMbk3skvDFqyah6I7mHHLZuOOD9jyptHOUpRqrQu5xeHBpBOuuZi5xzzMc520N-PW8Ud3TKxW_YQxAn1Gq0XMf3WuMJuSqZOdBFBEubj0XVB990icfG_MFv7XxHjnEmaSa5OBikvounzOyeaOICyqRlgOj0UIS4vli2T043l4COGzWeZc5p9q5HVyWDteaWs33xwWf5OUK8878PrDrpCLlAVCRTz8GHJebD9OPBIT4JOSNgrSZMe6xed2VjgyByBIgEUrCZDpcQg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👍
🐐
حرکت فوق‌العاده زیبای بازیکن تیم‌لئون پس از تک‌به‌تک شدن با اسطوره لیونل‌مسی در بازی امروز
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/Futball180TV/103532" target="_blank">📅 09:01 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103531">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9df00ddf89.mp4?token=tzgmryxDBH5c6F_6Yx1FxRipcrhXRbU9xPjkKRKywSzPrM8a1EsY8MyOkJ_wSUE-I23Z1Wq4jvniuwPbLv-Ia4ReWDWPklKO92Q8abdOg55Zc2XrR6ziYSb6qJwpzeKcLRxpIBUEDEK7c7BGINblG-uzd0cYe_Mz8cfsc8DMR_ldXFe_ItoMryKxdccidA9BILvJZ4hQEmpdKrGAAgVF3dNVPKD777jOyLjt0C55ATfuUNO6XyedQ4UHjYjTLE1wWErPFsXn_OR9Xso3hswykbPICsp1nY85YuB-5-fwIlC7hlAFe3jv6weoXoEx6ltIywY8O9_75mDMFApCqJUhvA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9df00ddf89.mp4?token=tzgmryxDBH5c6F_6Yx1FxRipcrhXRbU9xPjkKRKywSzPrM8a1EsY8MyOkJ_wSUE-I23Z1Wq4jvniuwPbLv-Ia4ReWDWPklKO92Q8abdOg55Zc2XrR6ziYSb6qJwpzeKcLRxpIBUEDEK7c7BGINblG-uzd0cYe_Mz8cfsc8DMR_ldXFe_ItoMryKxdccidA9BILvJZ4hQEmpdKrGAAgVF3dNVPKD777jOyLjt0C55ATfuUNO6XyedQ4UHjYjTLE1wWErPFsXn_OR9Xso3hswykbPICsp1nY85YuB-5-fwIlC7hlAFe3jv6weoXoEx6ltIywY8O9_75mDMFApCqJUhvA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🐐
مسی تنها ۴ روز پس از درگذشت پدرش، در لیگزکاپ برابر لئون برای اینترمیامی به میدان رفت و به‌شدت تشویق شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/Futball180TV/103531" target="_blank">📅 08:10 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103530">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m-mFa4kirmXQY7bHnlONoAwS4TQDMPBz3PHhRFlafVfnOBxTUUUDVo6XvLL3trMCA-DubXzsXoHIXqOm348zX5eU36cX9u1iQGPNG4kA6tnHpHTZbEum7Ci1cl7j7Oc84CLI0PLJ5MvvoCCA6BK25HlVBHcbXYZMFsrd_q2FykDoDnfKgOeNSgLtR6KxHmRJ_3ieksDoZxDLlASB5Oc2C3SO1jT-aNE6SmGpa-ok9WL7cdez2P8N-vLPiWXHCO4RpqvLjGKX66Wy8XM7I_iKntnHgoI8uCD8gwEDjEpe4gTgOp2sQKzaNp0sGPZOY1R8NdaZi8vCaI4eOPn-ju7zqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
😳
سم آلتمن مدیرعامل OpenAi:
احتمالا تا 6 ماه آینده، Chat gpt بتونه صفحه نمایش موبایل شمارو ببینه و بخونه!
به این صورته که کارایی که در طول روز با موبایل انجام میدین رو میتونه تحلیل کنه، مثلا وسط چت با پارتنر یا رفیقتون، کمک میکنه چی جواب بدین.
یا اینکه سر کلاس آنلاین، جواب معلم رو چی بدین؟ حتی می‌تونه تماساتونم ضبط کنه و وسط مکالمه کمک‌تون کنه!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/Futball180TV/103530" target="_blank">📅 02:28 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103529">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/05ad3b95df.mp4?token=HFdvF3sgheTmFDuMiFdHrvh0MfhI10QnwNbzfVBKQOxOokt3gS3JScIaD7rYsHmjd-zIRip1xXVdsL9yba_Z6BiwYF0yHTZh-K2mK8Hx6uOVx_Eb3ruk6OXBb71i-WXyre7l7OxsLbRc0QdJ1nI5U1gKW8rqA3h24AbqLlnnrArNARgi2-BCjmzrzUQqLS2K67E4J_nKKHtovBMVaR2y_eAwg5_3Epn-7B_c6FtTae66a7QW1gYSE4oRIPAFQemPvt2Aky9psXzihi2NTUiatZ2SneaBLQEpJ_Vscg79E8wYeSx4RBgVB3B3KQPO9fR0_JOoKS3FVRvUOB2JG9HyYw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/05ad3b95df.mp4?token=HFdvF3sgheTmFDuMiFdHrvh0MfhI10QnwNbzfVBKQOxOokt3gS3JScIaD7rYsHmjd-zIRip1xXVdsL9yba_Z6BiwYF0yHTZh-K2mK8Hx6uOVx_Eb3ruk6OXBb71i-WXyre7l7OxsLbRc0QdJ1nI5U1gKW8rqA3h24AbqLlnnrArNARgi2-BCjmzrzUQqLS2K67E4J_nKKHtovBMVaR2y_eAwg5_3Epn-7B_c6FtTae66a7QW1gYSE4oRIPAFQemPvt2Aky9psXzihi2NTUiatZ2SneaBLQEpJ_Vscg79E8wYeSx4RBgVB3B3KQPO9fR0_JOoKS3FVRvUOB2JG9HyYw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
با قهرمانی پاریس در سوپرکاپ اروپا، حالا رقابت بر سر توپ طلا هم جذاب تر میشه.
👀
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/Futball180TV/103529" target="_blank">📅 02:04 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103528">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/281d339227.mp4?token=t4bSf2a6XCyubxIUq-ghnDqUBhYrhjXKlpNBvhwcABc_38xiEkOJshvdzEoCTvfjNO0pbPyvB3v9tGeBz7ljCQtfanpl2MJ8p8Gzdr-oa5Ew1dT36mTJa8X6oY4C7bZ3T1n7wVrIWjbFbR8A56yXehtGkoveSCtHEJRLG51Etes3pZj8jm9hkzakbdWNqc6Hknw9oLRu2T15M1tV5rPyYxoWJjK3D8uZ83KkN2pRN8qTpLVX_QEEfDDC8rtgev9UBqreGVk-nHWnBoGtmituyd5Tqb9XfjD-4t_axWF6Os-bQOe42mG6lqDKPgkyZmfvZml9Z1BbSU85aC-VcPZZQw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/281d339227.mp4?token=t4bSf2a6XCyubxIUq-ghnDqUBhYrhjXKlpNBvhwcABc_38xiEkOJshvdzEoCTvfjNO0pbPyvB3v9tGeBz7ljCQtfanpl2MJ8p8Gzdr-oa5Ew1dT36mTJa8X6oY4C7bZ3T1n7wVrIWjbFbR8A56yXehtGkoveSCtHEJRLG51Etes3pZj8jm9hkzakbdWNqc6Hknw9oLRu2T15M1tV5rPyYxoWJjK3D8uZ83KkN2pRN8qTpLVX_QEEfDDC8rtgev9UBqreGVk-nHWnBoGtmituyd5Tqb9XfjD-4t_axWF6Os-bQOe42mG6lqDKPgkyZmfvZml9Z1BbSU85aC-VcPZZQw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
⚠️
جزئیات طرح احمقانه و پشم‌ریزون بنزین 87200 تومانی که قرار بود از امشب در کرمان اجرا بشه ولی ظاهرا فعلا متوقف شده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/Futball180TV/103528" target="_blank">📅 01:39 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103523">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HeBsnIGh5HE9YZvQ4GoU0RbdqkTy0MNWsrktXrvriuMGi-Is-torBHnX17QgFtxZTiGA31Gt-BLCJ46l5ime7pQJaFtCDpuOWpRQ-TRf7MWj_R9uVU0O8DPVqhW2EEX9Q4LG2laDdh3dvk1RrfYxRwGgWG3AGlO3XcscndFY9j3oHEoKUtV0i2tJeeiXs2DHyTV56AdAuYfBwGGwY2HFIKLweEZi-UwWXM_9NTesfxfKW-65Idui3DVNciaH_X3d8dBjquIUJQN7F4wJ5-CyxPdavTEstFL6kFPKloiT1fHDPYiAI1ubRoRFMZYv1ZA3eM9x7R-icXcDmVGx9Mc6bQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZjhY0VMfGmP7Gv8aDqQcFcyX_zVzzJWjjzXN8i8Bx_zOLOnvUyYs-5Kmvsl-6skD0RP6df-AvCYL3lXb4bGHCqvJg85Vd7qHnO9dEFsYQZdGqc5pYkXsA6qtpmIE4BQ66IXbxQZWMJ38OjIoNv_YGVORaB2GjDvAF0-mXknVYwvSOu4gzFZZ6GJAydNYggDL2J713GCRjo6_AghjbDmaJVPrIg8_GHllbK_zEpAERSay-unDnf7uuyqLy8lHv84DZpdtwpFcwKAlH_wEb4pTwD-tqOcYbV3z24cM7Zrt2XZ5vCUE5-SsO3Hh4tEPOxvzdMSLKow1m5j_16TlDfRTsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pdHDORDhl_-6M7eJb5vSwTskFLw08CcCOtV0mJAzhk_dB4oA4crcksJ2bRmxTP2C3e2SgidwlsWbej1u4qL7adozo_Z4_uJ6mj6FznODnyLU3irE_j3s9pRCR4ooGhYZyzIdtTQKRY1q4HIUYBIjg2_CqEjz8WE00-UYq3PCeAhn1341BzKRkSXW02nGl8ktItjvhFONVApkg38eGHWki-sdpSHHmSjGzOts8Ih_CG0IkutG3c8jgkFLsLe634rbJuja7sF--2YobidpppvyUJ9b4R0Lwq_dAghxWpSUxCz3RBQ_EPP0ijLApVulwXxgVJUMv1oE5Pifbm7UVZ2Sqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CunFtsv607R7aB8iJBzsP_qbjG4Oc6CIMcVr0Cm2nb4eIXcPRebpRmUJz1MSklm9CV0FfMaHdn0K_g35OPdJYn8jwNyLKwdSRrBhubWiRPfoqRIxKYmvxZDhan3S88_JMLERYzhZIz4sgsxXorg0EBt0514hJhEFwiqIkvmhF7ZlJOdMwEhmXfMi85yLgvvWoExkV_IzQ2DHMe3G65kRmNj8nyrRmb6CyIW3ZTau8vnXSgq3dT91Q5CFBtQKela5HnfeG_jU8GB7VdokmTaDABaD45G4_aD-DsDNQqIOKsWMI3Db7fnDlChR8spgMOM-c-ykU-daMx8-R9g2yF2YHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Dp8iaSWJSGTDkbSA7bGnd5CoAIhRNKcpRf1HEqWV7e-iO8jz8is_4KP8CifUUCG0mztXire8JsBnsHp4eSFYgzavXna8TFI-oX3cw-8DDghVmZhll_mKK3gKs0e04HWxbLwlkhJLQtADHMU-A4gylEd3jzD2_S0ZPUBYdQIcop83lUGynVZ3sh1JHRgIpO-KmCUy3rp-uI5Vpdq5ikDYHhxJRbr-4hTE2JXBxOrBXNtZbWrYHENg9FqgexaBAcpXVA4pc4o8Q54AA_9m7PfVQwe6XDt64ZiX8sS-L4BUI1xG8kZ9rkVlAQwna78EsaRHrgXorD7ON-G-08C8DTvdDw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇫🇷
🏆
🔥
✅
تصاویری از جشن‌قهرمانی psg
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/Futball180TV/103523" target="_blank">📅 01:27 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103522">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🚨
📊
🤯
افتخارات پرتعداد مارکینیوش کاپیتان برزیلی و مدافع پاری‌سن‌ژرمن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/Futball180TV/103522" target="_blank">📅 01:13 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103521">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">✅
🎬
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🇫🇷
هایلایت بازی امشب PSG
😀
-
😃
استون ویلا با گزارش آرش اسدی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/Futball180TV/103521" target="_blank">📅 01:11 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103520">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D85UmFnbP5qPRVT318VqtaAeMq1B8Y56mFJhVaRN-eC8RLonLz1HqfYLDQSn3eOI21VttCyEksBNNZ8kNpHlADtoYMl4T-fV27Z79Fl85Jkf-YgI6zrUc67MthKyx96tgDaA5pk5V1vRtqp_IFg3xd0LiYfd-Yfl0os_s4bKSrmSn66Dc-L36zwyWyQT-qDiiomTchlxkqJnjebW14Mf0YSbcVcwDYlbCDpwjW072koQrj4LQ08s1sAHYXNrTrZD0rSvFJC6yTOCF8fqJ_2UQQa_xJVHg3asjAtNWqr8A47dukpHjfrvGVE-ymOmvRUVpmpiE7_KUlYWn2e-LJ4BSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🗞
#فوووووری
از اسکای اسپورت :
⚽️
منچسترسیتی بیش از ۷۰ میلیون یورو برای رودری می‌خواد. سیتی ترجیح میده رودری را برای آخرین سال قراردادش حفظ کنه.
❌
هیچ‌کدام از طرفین در تلاش نیستند این انتقال را مهندسی، تحریک یا به اجبار انجام دهند. سیتی راضی و آسوده است و رودری هم راضی و آسوده است.
✅
در نهایت همه‌چیز به این بستگی دارد که آیا بارسلونا می‌تواند رقمی را که سیتی حاضر به پذیرش آن است تامین کند یا نه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/Futball180TV/103520" target="_blank">📅 01:02 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103519">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NrPkNKOjQTYlbjP1lRk493Ecp5Kw7Tan6Vq11VpECsMZZUHc74aoao2CCq3PKl_SWiSmDpnPcrEOJbf5S0aPPYwMKXhqkfLniYfkAmKBaXfHmQKJf4wNYu-busMgiRl9QJ-TodllZlg9QBr_jrZCNbEWunoTL9L5sgM2o5FhlTUtJ6ywRLcezoUjCR6T7ina1xVQ9gzZ_umgWts8jvOL5qfd-oH_DP7S2_cbeumiakCJ4WMfiiH5Q2LgS7zq4AeatT6WpX7Wvad-D0KTRhiv0qspof5JdtRJXL5gWdpQ5Dtdcgw7itqH3HJ36J3vyAg7OC7clZOrtS_MYNwIc39usA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
✅
رئال‌مادرید امشب در بازی مقابل لاکرونیا با تک‌گل براهیم‌دیاز به برتری دست یافت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/Futball180TV/103519" target="_blank">📅 01:00 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103518">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-text">👑
فقط کافیه مرغ از خیابون رد کنی و‌ پولت چند برابر کنی راحت
💵
👌</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/Futball180TV/103518" target="_blank">📅 01:00 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103517">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/17cffccbc4.mp4?token=AUSejolOxY8fzRaC6pBlBjZdKBAa9_hcMgSAarHJ7nwjlp3NP4y5udgQHNDPPuXPEcJBy6aCRgb7dqbQjmZS2OtJ7i3uftGV39Osc2dewSqPARKCClisExbDhAVSUNpmFFJ51FquxXVpsFFYpbpgwfTsp7EBU410ECxGhRL44j-F0ZNtB4HiuC5zUT5HGrHyX60WXg5AJt4LphFM6f33FqDKdE65i3J6KX8HS6Ar1NDJqs0HLu9TadtfCl9QtaXxVWxZ3DXV6PGkX4nqJ9h1QfVn2IdnUZAghZ5I0cSd_hvjuIvAeK0bdfFUNZNBRAb9B8-w6H7IM3ZPW1plheeoEw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/17cffccbc4.mp4?token=AUSejolOxY8fzRaC6pBlBjZdKBAa9_hcMgSAarHJ7nwjlp3NP4y5udgQHNDPPuXPEcJBy6aCRgb7dqbQjmZS2OtJ7i3uftGV39Osc2dewSqPARKCClisExbDhAVSUNpmFFJ51FquxXVpsFFYpbpgwfTsp7EBU410ECxGhRL44j-F0ZNtB4HiuC5zUT5HGrHyX60WXg5AJt4LphFM6f33FqDKdE65i3J6KX8HS6Ar1NDJqs0HLu9TadtfCl9QtaXxVWxZ3DXV6PGkX4nqJ9h1QfVn2IdnUZAghZ5I0cSd_hvjuIvAeK0bdfFUNZNBRAb9B8-w6H7IM3ZPW1plheeoEw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
a21
🎯
همین حالا عضو شو و شروع کن
👇
https://t.me/+FaoDjhEVG34wMWFk
https://t.me/+FaoDjhEVG34wMWFk</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/Futball180TV/103517" target="_blank">📅 01:00 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103516">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🚨
🚨
🚨
#فوووووری
از استانداری کرمان:
با تماس‌های برقرار شده با مسئولان مرتبط،
فعلا
عرضه بنزین با قیمت لیتری ۸۸ هزار تومان متوقف شده و مثل روال قبل بدون تغییر عرضه بنزین در استان انجام خواهد شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/Futball180TV/103516" target="_blank">📅 00:50 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103515">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/idmBWvV7EXmlfAV_Bu_5iq0zC8ubEU_FEPS6Kb0uFBekib_NhpSp0sLTPtprf0Hc8VnwUyoWL-_XsCfKJFcO2nYyAdtL14-1M5Jsc5IPKOPW6IUZcRDIsY3ajGJx8CVtAMKLmSC-KtQv7ASV_HzZCjxslMl1msuhKMGw5WlIniH-Uh4LWQa_ckRYOObr31PAnApwp25Nx9Q1fnN32DZ8V3a9IWKbzbOfiw3fzILuuNylsu1Ku1twg-zVMvrDifbvwh9YQ9SvKSDp-RsgWfS3b35je7dDERwxXwQtgfp3prI9c2McOMt8yohE9c_KBZ_j2VcoA06liUhbjkBOF6S_kg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🗞
#فوووووری
از اسکای اسپورت :
🇪🇸
بارسلونا به منچسترسیتی اطلاع داده که آماده است پیشنهاد خود برای جذب رودری را به ۷۰ میلیون یورو افزایش دهد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/Futball180TV/103515" target="_blank">📅 00:44 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103514">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eU9NYoVIxKMFuCiUfbNi38YXGAfpMFq0Ojric5th7tau-i9jomc-1s5gcKpPC7oEJQ-iProcrzmkNYo8SM945upURhw0kPFSSz6Xok2eK49RDqlCFIjWzEqILEj044CtRHVN2mF4Y9_QZWtexGV4AEyBfHh3DS58jkRsQwuVbNrzGt17smWABUN31BbWXjXP7PwNhBESFwhpc8X7g1H-etCsyJuNSZxhTmZ3gb7xROFQIOb6vbN3fI0EfXaHTp1z4zRSJqXz65DoQCqgvz-UJ117CyS4nWkOcgkzb3vlKOGXmiLU1tlv1kvH9Foyo5ei4MWF3hBBHjj90feJZMK7Hg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🥶
🥶
🤕
یکی واقعا تو بخت اونای‌امری ریده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/103514" target="_blank">📅 00:43 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103513">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m7mct6y0-L23Nbnhs8RlIS3Bzq480CvvXQQg-7is7UJKgXA64GCFDKcTZNcEkNvZqRXJcRdbchEAwNm2LqVFshxIsYQf_RfKTF8Jhv6x_-CRC9nGrSF07x70dh3JYhrSDt9Fw-8ayLIgom1YNyPAAPQW0YBnkBZN-veyD74xPM2yXHhJ43lJ2O02Ywb-BkP3B7_A6oaXw-B0pNVh9eWBSIY5sP46xTybyh_0dpHoTbz2AdEyUps5g-o7Ncvvb8yvaeYFS1r6aeBc9Ons1Gcc3F-LU9QbkUGyECY_fmjwl2uRz2Nt18ynQosZI5LzS8F-i7EFyarJHWPHc3NOk-I28g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
📊
🏆
فقط چهار بازیکن در فینال لیگ قهرمانان اروپا و فینال سوپرجام اروپا گلزنی کرده‌اند، در حالی که سنشان کمتر از بیست و دو سال بوده است:
‏
🇳🇱
1973: جانی‌رپ، باشگاه آژاکس
‏
🇳🇱
1996: پاتریک کلایورت، باشگاه آژاکس
‏
🇪🇸
2017: مارکو آسنسیو، باشگاه رئال مادرید
‏
🇫🇷
2026: دزیره دوئه، باشگاه پاری‌سن‌ژرمن.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/Futball180TV/103513" target="_blank">📅 00:41 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103512">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bWlSoebSctCP1qIDhz7Vw1pFmFo-CM2XkBUOJ3rtaPAl3un1sIzuQ61li9PIzi6UuKcQGSYuRuhxLXg84ia9U4DbxkaLTamH2OSmFxPpmjQmslsJtQRLQY7pGzVCd4ExCSAHSBY7pKvd2bJ9La9uIXYWzW4EjU-AbVjuUUtqLBhhnLuCnsesxcqmTSoqMkyoPAS7VbOU4zJ4Ctdo_NhlflrT5uCj65FUREOWhFKT9P-Kzbow9NBrRDzHMcKWvkRpjqKm0BOp1iplt5k_Co3A45ii-PkHY5MhHpH8D3nAmLNM9uesDrhY84S64JwdC33V_PoXoqJ3q9eX4xmm76VLRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📊
🔥
🔥
🔥
🏆
فقط سه تیم در تاریخ، عنوان قهرمانی سوپرجام اروپا را در دو دوره متوالی به دست آورده‌اند:
🇮🇹
میلان.
🇪🇸
رئال مادرید
🇫🇷
پاری‌سن‌ژرمن.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/Futball180TV/103512" target="_blank">📅 00:34 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103511">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XgZoNhEWYpux227-M2ZHeIBxQMjtnXIFI8q5wO8XFGAJIGDelkmkYcC7v1GlF-KS1s0H-cPHeaI7xWljvt1XpESuhLREj9zEOYSKxFFBETbpuX02jUbq97sRfWuwL7kWxUDc6Zo9V3XqoFZsdFq__Zz0cGcu5cMPh-cjhq4YSc0rfgAFb9bZluygE8AsUptzAf4QwOJ_eQ2Zu1rtMY2VcI5e8tJpiliwmqMLUt9FHrzoFhiZmJmRBT8iUZnnA7neBpxg-KL1PpxEq40CCyjbLz9t7GpMjb5yGKWB0-8kWH7rPFNiwkm66AUkxJiFsXAtEZiJptwSNYCXOS7ilZbFnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📊
🤯
افتخارات پرتعداد مارکینیوش کاپیتان برزیلی و مدافع پاری‌سن‌ژرمن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/Futball180TV/103511" target="_blank">📅 00:33 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103510">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AzlOjt7iciSCcdJpOBVesPsOzpTPn2wLvoc9O0LpbiNZvEy9PCdQaJ6BS0muGg_M77Xp9dZ7TcyIzw7IOh6lW6_Iy6zjautB_ixkbf5CIpsOi9iGaQ-uc8Bma40V2FsZJ38S8g80tzDjGagvVz-wcof4jAGBQH6Xt-wS7VRvZ0aCzURWz1UpCz39_ElqQ8tfP8n7L6AypWEzoA9YikzFguaZ2RXs_uBdjtc9RiVEnbJVe22sNLKmUzvCfLoFtlBMSb8ndibpaMK_kt48JJwPi1rFZdW-W22RMfaC3zo1w3UXPy0-n9dPZNZ7Pa2rHmZd3zJTdgPGxu_1ZqEyqcGUPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📊
🇫🇷
پرافتخارترین سرمربیان تاریخ پاری‌سن‌ژرمن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/Futball180TV/103510" target="_blank">📅 00:30 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103509">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KPXLq9zSqkpfxq-a0dv0igAOJfG3RXi5-913fYAnKuDTUp-NMj1gI4RoAmhV3Sp-UW5XBirpjq7-Mfj022w4PtA0_IkTcESI0xxpiN7_BgxEqTeGuqJvoxI4kKFUh7DWSQG-aeykf91uXQi2QOvqk4Vn64mglJFCYhlFgNT4nMl6EoLZctIGQSZk1aLZ0-em2nuEUkEwqIsc-PyldukDS0jb9ojvIzsxv1UfBGUmzzGLEwkRmoZqsAFVz4BkpdDmW9n-N18iyL766XkQ_69E9pmRLGJ7fxJsHIyfvBNg4HwGh9asQHOYTC0wLvNJGHqARdhtM25VSOJUKLw4gw3SNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
✅
پایان‌بازی سوپرکاپ فوتبال اروپا؛ پاری‌سن‌ژرمن درحال یکه‌تازی در اروپا؛ انریکه با کمک خط حمله وحشی خود موفق به دبل در سوپرجام شد؛ دستان امری بازهم به کاپ‌قهرمانی نرسید
🇫🇷
پاری‌سن‌ژرمن
😀
-
😃
استون‌ویلا
🏴󠁧󠁢󠁥󠁮󠁧󠁿
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/Futball180TV/103509" target="_blank">📅 00:26 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103508">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hvis4rh8Hlt4GflwsfCmYqhgyXNv3YHfOyx-QkSGbXUcvgEN-DJitWuKYmb7FExK1ZQRssdRJ4Wfy2K0dl8OHeChxRXLRGn-J3OdWLyqVU6d80dfTLtVewNrC5E8I51TuMgwYP0sax0qbGfgBFAVscDNIPmiOdChaQtQ4sNgm98yL_L8_7ul3EY3C81R_4pvPTytOpLIMv7uryqkdD26-OzwMJj4__7QCMNvFs3Y5dKrk87B1hYfpI1aQEYug9pL5bpCgvrF5eSaJCwAsBrwSPPGfJmY7G5gf5OA9lu3tvGus857-oFqQwqi0njS8u0CHYvALiiqWGN3AZ5xOepdyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
✅
پایان‌بازی سوپرکاپ فوتبال اروپا؛
پاری‌سن‌ژرمن درحال یکه‌تازی در اروپا؛ انریکه با کمک خط حمله وحشی خود موفق به دبل در سوپرجام شد؛ دستان امری بازهم به کاپ‌قهرمانی نرسید
🇫🇷
پاری‌سن‌ژرمن
😀
-
😃
استون‌ویلا
🏴󠁧󠁢󠁥󠁮󠁧󠁿
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/Futball180TV/103508" target="_blank">📅 00:25 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103507">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5497970611.mp4?token=Xe_a8ZtdcevWfXNPG_VLQBKvGn3zS_8uqc0XpN68uHPog0eTdbedxRRdtWD7NOkbEn5f0-MSQIIOs7bOt_5GCeRZZSI_VUozyGVvqryMBXP68hxak27TMPPMyJxwZ1jDY6YB9dqDMACTKvJ_junp_xH46xT0gaUQhnrRIm-kRhhRg9h7LIeit6QopcgOfq_s6VeUctXJCV72QDApx3Mor66FPwYM0SiXUS9zi8BDiJrBImN3LA1i_rfqFjwLPsoMkgFiuC-ZKk4_RUv2sUsl3KRyhem9SrTd4bKuZfRJxCRymDr7aUiGemdQXunplEv8nZb4_afbHh9CUlDPNrh4wQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5497970611.mp4?token=Xe_a8ZtdcevWfXNPG_VLQBKvGn3zS_8uqc0XpN68uHPog0eTdbedxRRdtWD7NOkbEn5f0-MSQIIOs7bOt_5GCeRZZSI_VUozyGVvqryMBXP68hxak27TMPPMyJxwZ1jDY6YB9dqDMACTKvJ_junp_xH46xT0gaUQhnrRIm-kRhhRg9h7LIeit6QopcgOfq_s6VeUctXJCV72QDApx3Mor66FPwYM0SiXUS9zi8BDiJrBImN3LA1i_rfqFjwLPsoMkgFiuC-ZKk4_RUv2sUsl3KRyhem9SrTd4bKuZfRJxCRymDr7aUiGemdQXunplEv8nZb4_afbHh9CUlDPNrh4wQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇪🇸
✅
رئال‌مادرید امشب در بازی مقابل لاکرونیا با تک‌گل براهیم‌دیاز به برتری دست یافت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/Futball180TV/103507" target="_blank">📅 00:23 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103506">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#فوووووری از رومانو و اورنشیتن:
🔺
چلسی تا روز جمعه ساعت ۱۷ به وقت لندن به تیم‌های خواهان انزو فرناندز فرصت داده که پیشنهاد خودشون رو برای خرید این بازیکن ارائه بدن و حداقل رقم ۱۲۰ میلیون پوندی میخوان. پس از این تاریخ دیگه این بازیکن برای فروش نیست…</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/Futball180TV/103506" target="_blank">📅 00:11 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103505">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FBwSz2-zBmzDqU6hMWmFbEsEwi6akt2nOe53DEpVGBn8IgzE7UcrW4q20ujboV5HVU6xXc2iy7Q5vxbfZIkOMwAZ6IvnlTkyHlWf6VKropEkNmwNeo6rDw4R1e71mMJEcsQTUBipv7lZ7jA27oFb-buQRZ3PsbdbVsewXejgE2diDWw167dpowX8sE-ICPK60eVjST6wdtp53oUXq_lESBDxVeDIMNBa46NwdbIQ07g_TQ5cqiLujId-4BAi99vox0WNOO4pJnhKLRYAKQBx-1cdSZ-OudvV9BuiWGKZw1tgFdM_HtA_GLWP-jOAr0YZBmYifegcFG3rhaSIY5ZEEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#فوووووری
از رومانو و اورنشیتن:
🔺
چلسی تا روز جمعه ساعت ۱۷ به وقت لندن به تیم‌های خواهان انزو فرناندز فرصت داده که پیشنهاد خودشون رو برای خرید این بازیکن ارائه بدن و حداقل رقم ۱۲۰ میلیون پوندی میخوان. پس از این تاریخ دیگه این بازیکن برای فروش نیست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/Futball180TV/103505" target="_blank">📅 00:03 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103504">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/38009c3d9d.mp4?token=PlrYBAglnBn5vTaRjEdhXtoKDQ-4UhWCGvuM3B8lHzG5g07ghLMmOkbmbVaEG1Z9-aBdiByE9aBG5hMPANbkQAL6hPpqA9kMH1sCv3PbPD3HlVt4EMMQyOx7C2nW1Z37zVlyRE_4bBHQjpAukcp0R3Q4ELG2HSe4lcabZmwh3neJ18v_3LMXGiO-EQUR7JydFCvrqA7k8uBoJjSl94tesubYei0IDFbNIz2HITgjicFOFmDBvJB2sB3ZRgFhiXs6g0GBbawsnZRAZyIe2Ao8KdvTiWTwJ2ZWRRqgZRPzFNtakjSx3scR7X4MqPtTwwZd82Kd9MBuoC5mY8Mr3iAkqg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/38009c3d9d.mp4?token=PlrYBAglnBn5vTaRjEdhXtoKDQ-4UhWCGvuM3B8lHzG5g07ghLMmOkbmbVaEG1Z9-aBdiByE9aBG5hMPANbkQAL6hPpqA9kMH1sCv3PbPD3HlVt4EMMQyOx7C2nW1Z37zVlyRE_4bBHQjpAukcp0R3Q4ELG2HSe4lcabZmwh3neJ18v_3LMXGiO-EQUR7JydFCvrqA7k8uBoJjSl94tesubYei0IDFbNIz2HITgjicFOFmDBvJB2sB3ZRgFhiXs6g0GBbawsnZRAZyIe2Ao8KdvTiWTwJ2ZWRRqgZRPzFNtakjSx3scR7X4MqPtTwwZd82Kd9MBuoC5mY8Mr3iAkqg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
❌
😱
لکه‌های نفتی بزرگ در سواحل قشم تنگه هرمز
🔻
با تداوم محاصره دریایی، مخازن ذخیره‌سازی نفت ایران به‌طور کامل پر شده و ایران دیگر امکان ذخیره‌سازی نفت ندارد و به ناچار نفت مازاد خود را به دریا می ریزد. این خبر تایید شده و مقامات جزایر ایران درحال اجرای طرح پاکسازی سواحل از لکه‌های نفتی هستند!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/Futball180TV/103504" target="_blank">📅 00:01 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103503">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/29b02952ec.mp4?token=UCokJcvDS1yKu9wvdbSiv0YxRGKqK3KrQ_qQjWRQ_FJJvWVfe0qjjbbexlwW9A3dVnvTMa7Y_WVuXj56r0XXCeo19cMi56oQE1FRvCea-DC0R930ZeGXsZhAg7lWHJb9o_rMz9D8ruPy4tUgU3vSioJeH7lx9CtkGLHDuHsIuU2FGuCPcL0JLpT1-mBvwPMvqhFkDZFKTH6Dgcb6Zgx0DF8wjUJtSQppDDUGAdiOqUuLkC-2nubiTEdsm_6MLtTcORhtzQB6ZakLJyAchL4QDZxEJFUkf1OGVTH596pwjkSv2v5APlb6Q6RD6rxTaKU68AAQ0Kx7-gTk4kBqjgr-27E9V8-PftNVso9bBMEvwqHr05TfjlyiWOi8iV7trNUxcJqRpYiD4PgSSjsMRnEHOjLrffLviq2qo1d3vI7K9vMJqNw1CBE5HrJwQ94gQdMV3VqFz1Lx-9wyBPNZq9MNRTqjjSS9jnHKzE9youALcIKyvIXdb9ay0ClfSSX_sDh3rF7-bUoHMAAFAOSHSyASnZg8Bdd7lGOeDNsln1R-Steag21QIIbEqL2PJ8VQi3QPRlFfYMrarCqfsdS0YduarRdGTrKgz6M6pH1vrjoOhdSF8LvXDfcTfKSFRQp5KPb4vVSdIHnd-3CB28dAhgCdNKczB9h3NpJ3CN042z8orqc" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/29b02952ec.mp4?token=UCokJcvDS1yKu9wvdbSiv0YxRGKqK3KrQ_qQjWRQ_FJJvWVfe0qjjbbexlwW9A3dVnvTMa7Y_WVuXj56r0XXCeo19cMi56oQE1FRvCea-DC0R930ZeGXsZhAg7lWHJb9o_rMz9D8ruPy4tUgU3vSioJeH7lx9CtkGLHDuHsIuU2FGuCPcL0JLpT1-mBvwPMvqhFkDZFKTH6Dgcb6Zgx0DF8wjUJtSQppDDUGAdiOqUuLkC-2nubiTEdsm_6MLtTcORhtzQB6ZakLJyAchL4QDZxEJFUkf1OGVTH596pwjkSv2v5APlb6Q6RD6rxTaKU68AAQ0Kx7-gTk4kBqjgr-27E9V8-PftNVso9bBMEvwqHr05TfjlyiWOi8iV7trNUxcJqRpYiD4PgSSjsMRnEHOjLrffLviq2qo1d3vI7K9vMJqNw1CBE5HrJwQ94gQdMV3VqFz1Lx-9wyBPNZq9MNRTqjjSS9jnHKzE9youALcIKyvIXdb9ay0ClfSSX_sDh3rF7-bUoHMAAFAOSHSyASnZg8Bdd7lGOeDNsln1R-Steag21QIIbEqL2PJ8VQi3QPRlFfYMrarCqfsdS0YduarRdGTrKgz6M6pH1vrjoOhdSF8LvXDfcTfKSFRQp5KPb4vVSdIHnd-3CB28dAhgCdNKczB9h3NpJ3CN042z8orqc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇫🇷
گل‌دوم پاری‌سن‌ژرمن توسط دزیره‌دوئه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/Futball180TV/103503" target="_blank">📅 23:54 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103502">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vrM4KMy-pNE3e2ATqm105WhBsmgGXZ6hrlfOQ8uOV_f-5yDPkxXhBF4xtJ4AyRSQ_Xl-rJqGvvYbRnMMn9GFYUX4vTtR6ZDZvtf8k_abzbPL1sxI1qzJXp3G41IImeU7cCsoK4kTGqNq_A82I_TmxfWyPEu46tyD2xdHUV3Jy9o3QphU9rjzNFigZufpaPZB4dmF64IyftTH74EbsUoJlBVXiAV13f7NiTr07XZODbHpe78rQeWKbmblEKTd1rGzG40KLcU0ABQdcxfK_cEZM95lkuNTfZQUTsD5Xe2ZELygY0Mj6WhLdUEErXpJ-t3zor3NOPt3aLoJ99lfZtuvbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🇪🇸
🗞
فابریزیو رومانو: کریستین رومرو به اتلتیکومادرید مبلغ 40 میلیون یورو
HERE WE GO
🔥
🔥
🔥
🔥
✅
✅
✅
✅
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/Futball180TV/103502" target="_blank">📅 23:41 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103501">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uVQC3X2qTQlHKi00LKgeqDntaXUZOBv4JXspn8OUFqDPIQqwhvmbw1p_E9yfto9VpX9_lMf38mV794_1zEFZyTvpDAUAPA30i5XpiABK1kFyHlJD5Qct_6KhpBjrg5TyHYEw571KbPqQt8R8maYc-mCfebs6Df6-5md-vnJg6HEL6hQC1nVMCZDxqYl79ulVtw-Q9uaMSLEj17nL8p7LeCgv6-69aP_USsphph6ryrdu4MVkyI-dwOx4kb9dmIt9QNlkb_oKrv86IelU81fSgQ5t1MRGxLWVa9aAgEfFIlQSNWlaPgWbWi9CmgXuFCEgcz1NGjMkQWDy5rbKZEIUYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
⚠️
🇦🇪
امارات متحده عربی ساعاتی‌ پیش ۱.۵ تن طلا از دارایی‌های ایران به مبلغ حدود ۲۱۰ میلیون دلار رو در تهران تحویل مقامات مربوطه داد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/Futball180TV/103501" target="_blank">📅 23:39 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103500">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ojDJUQ7CBgjIjK4Birr0nXWlrNEcijUJN4roIJvltS4iQwyfGms_agB35mfJt01d-BMMJu0FNpkj2ajciJ7hKDsbonzmU9nzMOTrqVoyyf7ZSVIXlT7dhvi-lc3oqJPto7P0wOywB8dvxEXzWBZ4ErizZYD_MdXkNoLWS9uI6QfKJXKootD8VZEAzr4Z43z9lgBTxlxh-XMQTe4jK68cLIlJZIKBoP4P5uQjGPevZ1q5-h59Vnz67bWUwkq4G_LMBUZ6iFNZUzwzjZpig7LYXbm-ZS9xX2huu76U2ip2ELxCCYJDGLVG8Gh6hd21W51bdqUUrlwX8uuQh41IgF-0ZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
✅
تصویر دیدنی و فوق‌العاده از خورشید گرفتگی کامل ساعاتی‌پیش در ایسلند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/Futball180TV/103500" target="_blank">📅 23:35 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103499">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d_j2H3tlxX5NNq7Toz5kUFj23rRYaaIej-lmNAZxuLE2F67Tu1uICHUwEaNGXdpW3pgSGmZXtjRQsttkyUvalVw-oaxEnJzeP_X50HpEfeFIIEZ4ne9qOkvUtprNXwL5-NAdVYB7pE065DgJ0SM6h1YE_7P8pksGT2FiL7kEJ9kEKyU204Dm0zTDWZECe8AIshrXrKJS-Fh1k-nRfgkOJmFaee0R8xTqNdymhx5sDquWHoKXx3OFYEW6c_mTPoe3NVekvY26W9NHykkmW6_tGIoyn2ALouV762nNLJyZrX0KHMaxa9ujVwHVm5Y2KdGIypYxbmYeSM6YbxlqIqTRzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇫🇷
🇬🇪
📊
کوارتسخلیا اولین بازیکنی در تاریخ است که هم در فینال لیگ قهرمانان اروپا، هم در فینال جام‌جهانی باشگاه‌ها و هم در فینال سوپرجام اروپا گل‌زده است.
🥶
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/Futball180TV/103499" target="_blank">📅 23:28 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103498">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AZJwlNi7Ke6kI4dQoO5xJHeVp5T23u1MgPMM1njmKWZd-9QQEKzoZo_JYI4aA8SUuYonauf5INkKImQ2dX4fODeWHpmz_wm3UjJMiB-bwm_RKYGVknp81EMr3s1ICfKc8sTcjgfq2lUMWzJpSrd2avIfQOsi5YjZ0UzX_LdqVZbXl7933cKDGQ-vzv2IjfoNCaUubh4JTKOwI6KQ97ahr5JY9ZVCJKpCZeFlrvcvzSW6mY1ZzDS4tEapW0WdvHfrFUniQmvQKHnD2WVB-8b3TlK_TRvtCS64B-tLGGn5Iilp7htixF_8DTCeh6LTmdPPyOw-SFmrgrbgzv5d5nkvCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
📊
🤯
🏆
#رسمیییییی
؛ ماجو با گلزنی در بازی امشب، با ۱۷ سال و ۲۱۲ روز تا جوان‌ترین بازیکن گلزن تاریخ رقابت سوپرجام فوتبال اروپا تبدیل شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/Futball180TV/103498" target="_blank">📅 23:24 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103497">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f8d89b14cf.mp4?token=s0pvLqaUjG4Fil9TLvJorl-nQthOIK3KdeHsym2Hh-rtc9kGjVmFPEA0mMuCmja8ROfVuqiWclriDSNRnPl67XzCgVKhsCQ7hz_uDncCb_0PLarWdR5XGwpEESVl7pSj0V7Hbhkv9uorRj_9gHi1RRAD3cAB0TXMuVz4b2DrOQ7GpJDVzpVdj8BWYANxLRmeMdJzs37NylAaYJIK6ZbUShA1eK56onAyxNgxBQGbbjGxrX2QjYO-oi1hyOx-KItYg7MVlu6-W57TAp24ZflVrU3kfALmmWPVKiT5JJnp5qyHoho8x_LFjnKYEV9U7rG5gUJwpDMiJkHkMPcRys5fDA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f8d89b14cf.mp4?token=s0pvLqaUjG4Fil9TLvJorl-nQthOIK3KdeHsym2Hh-rtc9kGjVmFPEA0mMuCmja8ROfVuqiWclriDSNRnPl67XzCgVKhsCQ7hz_uDncCb_0PLarWdR5XGwpEESVl7pSj0V7Hbhkv9uorRj_9gHi1RRAD3cAB0TXMuVz4b2DrOQ7GpJDVzpVdj8BWYANxLRmeMdJzs37NylAaYJIK6ZbUShA1eK56onAyxNgxBQGbbjGxrX2QjYO-oi1hyOx-KItYg7MVlu6-W57TAp24ZflVrU3kfALmmWPVKiT5JJnp5qyHoho8x_LFjnKYEV9U7rG5gUJwpDMiJkHkMPcRys5fDA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
گل اول استون ویلا به پاریس توسط ماجو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/103497" target="_blank">📅 23:18 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103496">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">گلگگلگلگلگلگل مساوی استون‌ویلا</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/Futball180TV/103496" target="_blank">📅 23:16 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103495">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0fba6f1f51.mp4?token=GU5aMuSYoMn8NEAZIzBgVlH_PWZPpYN7sbsYfQCKnTC6QDWrDPHN3Z_OpZTE33gxmi0LTHKoCNtY8yVty2G-Cfr4Ty8MbdAxDJb5iyFxmFtZt3MqvkvGaJ53HOXQEHhzXjvVzme01nWMcpE81GpHXCB6h_WMUGyOBJgoZwqERu5DqmbfZC8Xw7U-HKX9gRpZhKUC7hCJS-taOcKNHxaKX1lprIOKy3DTS3_24KewljQzGJcpkcCsfYos97rckyyxBD7KSET-uZSmXuleGWPVNvcfnOUFKn0TTO4qNeVscPN-NSQ6ag2bVWBqCrkIVpGIfTeGGoNKg1Qy3xJmO2SR6A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0fba6f1f51.mp4?token=GU5aMuSYoMn8NEAZIzBgVlH_PWZPpYN7sbsYfQCKnTC6QDWrDPHN3Z_OpZTE33gxmi0LTHKoCNtY8yVty2G-Cfr4Ty8MbdAxDJb5iyFxmFtZt3MqvkvGaJ53HOXQEHhzXjvVzme01nWMcpE81GpHXCB6h_WMUGyOBJgoZwqERu5DqmbfZC8Xw7U-HKX9gRpZhKUC7hCJS-taOcKNHxaKX1lprIOKy3DTS3_24KewljQzGJcpkcCsfYos97rckyyxBD7KSET-uZSmXuleGWPVNvcfnOUFKn0TTO4qNeVscPN-NSQ6ag2bVWBqCrkIVpGIfTeGGoNKg1Qy3xJmO2SR6A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇫🇷
گل اول و دیدنی پاری سن ژرمن به استون ویلا توسط خویچا کواراتسخلیا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/Futball180TV/103495" target="_blank">📅 22:58 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103494">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/di73kRqaVMY_J038MqV9Bx7amyfCKQ99FAE0Vz2Xjjc5nKMr4-2o_TZQE9kzN-38jbnduEPlQkAKG2V8M0sHnRzlGQSZlSr1sdwi2wPzQZV9KOr2WiXzIPNk-ff6_l_VS1SYdlr4xYFD1BilPEYcjsD4Pp8lndSrVhhg9doXSvonHmP3QHSNmiw5Ri7zZWrSXNYDYc97HSFjV8dq-Pu86ReEuBCy5CSVLhFuzLN4w2erYw-h37FWi0MzOkqLjOfy48vK3IPTIz_EVCYXtoH_4djI61TNmrI4W0_EqfRlkjVMDqJMHv5tVb-j44yvq6wnqPWDHKFZOs2VGPlAYy8xuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇳🇱
رسمی: ژاوی هرناندز به عنوان سرمربی جدید تیم ملی هلند تا سال 2030 انتخاب شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/Futball180TV/103494" target="_blank">📅 22:42 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103493">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JRlR_smRIMq0R4fQPQMrdNOartngoIfYk4V1ydRXjVSycUuwth5DzlzKyJNolrUS_k2ZNjoPr5CPw9T54bDHADbP_uOiOEFhlvlzQp0FQhaTZrJhEIMURov1WxcQ36vUgNVjzNkKkze_gthvRfZihgLMpuw6Y_OFuK-3B1M8ajBiibCFMN6_V0i6-NzFcsPB7XCO5s-vgWZGpIcf2GESdQUXIcGgc7qQwrt6EjQ65Z_JBJN26rT3ka4nB6LotvA7mUQC4Zpra0Z_yQNDe3NaDglyb_x6ULbP7Y7ASBF1aarlxkYUF7kLyb6RFotXyrgCZp74ZudTk5tPrc4UrkRJGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
اسکواد پشم‌ریزون فنرباغچه تحت هدایت کارتال!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/Futball180TV/103493" target="_blank">📅 22:15 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103492">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d270719e48.mp4?token=nita-tqoSyUyPWVUKj10Q4qimLgIwxfhyR2sv6b-e9kbDNamPufItZP_H-i-u-sedWDWU2gfFwZfMKGEUcidxy--MkY0pJrSQaf4Hje5UrfzaZvnn6F0KfGhxP4RplwLLkl1UMn1J1PXFL_TWNvPSc19meTUwRLZ13SBdl1e9v1vcxWo7DNDcGOjITgHokUcFmYSgCgYnrB0rWAaZPIXTMlOpz2aORPUT8bI_4d1Hon4n-uQg1qslSFq8SulZXzfy84DeTBkBA_fgC_sZfZRPakSNKTsIcM7xB2HhmRqWstGqdC7QGygdz9nBHJhl_ungcjgZtro0q_SBZr1latVIg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d270719e48.mp4?token=nita-tqoSyUyPWVUKj10Q4qimLgIwxfhyR2sv6b-e9kbDNamPufItZP_H-i-u-sedWDWU2gfFwZfMKGEUcidxy--MkY0pJrSQaf4Hje5UrfzaZvnn6F0KfGhxP4RplwLLkl1UMn1J1PXFL_TWNvPSc19meTUwRLZ13SBdl1e9v1vcxWo7DNDcGOjITgHokUcFmYSgCgYnrB0rWAaZPIXTMlOpz2aORPUT8bI_4d1Hon4n-uQg1qslSFq8SulZXzfy84DeTBkBA_fgC_sZfZRPakSNKTsIcM7xB2HhmRqWstGqdC7QGygdz9nBHJhl_ungcjgZtro0q_SBZr1latVIg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
🤩
عمر آرتان داور سومالی که توسط ترامپ از قضاوت در جام‌جهانی محروم شده بود، داور بازی امشب سوپرکاپ اروپا هست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/Futball180TV/103492" target="_blank">📅 21:29 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103491">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vkyNdLbsZMojVbY4qpS0DGnRTuC1K2rrSrnKaPUsRj4T6aPoHnZnfzsJLoS0k--Do5_tMo20IArWZpb6WemGZn6p9QWQqSFxOMeDh3rzm6PZ5LOjIUlq6BcgDiKHPuuU-7miXPXfbeqFBxHfCKA9E3ZFb6O5MSVIS9IAbPUFc_H9Kn1kDAEyJq9C6uotaRLjY2tAuzl3-RX57oiCdI3YQgXJifprrngE0MzFQVo1G-frdsB95FsPJKAYrUVKYbAqk_ml54kKKJqTWreT2jMViLWvb3IsPpexh4JZndRuKEpEIOZ1fghOzxj-6lw_TcN5pjsd_hAW3jZqqdDfPXvW1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🇫🇷
سوپرکاپ فوتبال اروپا؛ ترکیب دو تیم پاری‌سن‌ژرمن و استون‌ویلا؛ 22:30
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/Futball180TV/103491" target="_blank">📅 21:24 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103490">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TZWaXOqdOre8XCDjCFKxnvyczISPPvF4beelRsVx5ajbRxT3FjFH5jEabJ-IkJl7YhgmXQdJCB0U5dcXwcjhFTJexrVVV6C5hpfsN8neYXjDJ5GBvi-rXbQ8qBRe1VJ0ZBWhdP-2dYomrmcSwEvYNgz6YwAn2T17ssoHdmB55ETUDDs7fatnzO1xJT5tKX7aV_-3kFOM63MTNQPKUKLGr7d1VeOtfRwuhkSwJDPq7nZfdt3joxhw54wN89sb-PJEoruQfILa6FyfUhL8mbX3LNFX3JT9jWRKdZf8z0_n8VEdqqrDQZ47T4S-AKGjNhkJLacCz_dgB4Pryb4JNKE20A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
ترکیب رئال‌مادرید مقابل لاکرونیا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/Futball180TV/103490" target="_blank">📅 21:23 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103488">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/de3G9hmyrXYGNvJJTH5muCX35ZKz4t7OKd9JS316Yl-XJylSLqoZ4DLV7fqIXpddLL82-Fb-jUMId7Q0y4R_p5tC9t4YGUrQe6Z-BIY2vb74iiUd5IgOzyEDBOAa8r2spITrs6BARA7KRn8ZaJwT6jimoo1dgQ4CmIOvd-skHrKIWVkuPGmlfvoHl0ui_KZgIBfzxjrm8dG3BkNQ-6Ud2eQc-0dFctiOZRhJX3ngkZ8Mkd6PtY5CZdlVYAT3vBl-X4aWrr3WAOVeVRaDDuy1LmA28fVX0a65Rm9BzlIxnc1KrYHu70VmmQHKsCjmWYOM1Fwm3WwZTO9MEAgooNINsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/N0YwaYnxEGpS6tYe251g4hSVaVKcIb5cYeh_RDD8jHHatd4GaR7_d1WFaOrRPqKzcGbe8D8ILa1Fuw2-Z7X17JTCN-qdu71HcEErYCiZENNZRVoDRKDb9Rwa9NGz7U4MptdjuFW6SS18Sg3TQsJzBl6rWyPujSNOLuaBc4dJLSgpOEoIuliHxKSJnPWaCIrkz6Gq_ABUcpiIT_q1j4ohKJ3qDJ6wDUs8sd_w5lY45vW2NUFfJHr_agBmf_AeO0cSB7HdWdTuMrrq0wuPU-83bZibvBzpDJTXR_FY2N6QFyaOdljsY58MjukQK0XBR1ZF3jraIAzzogwRfQOoseSlJg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">هواداران پاری‌سن‌ژرمن در محل برگزاری بازی امشب
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/Futball180TV/103488" target="_blank">📅 21:13 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103487">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XVwRKhKrAB8OTXsHeVHj8fuJYT77pJtmUHqNV2EPUh5NYhBOFmQyFy5iO4GV9hLDcaOa0Tm9xBDzBj8ed6oLivqQmAiCKixrh2MOjOi4RhflBdtljafjaFOoWsmm7SAMGSBtsjOzI71n59EHYoTm1OQdJ6tc_av5wHp8tDM46lUX4mpT_3Vfl7LfuU8CByAFQs7aYdNAm7DoBhUHWNoryTSH9lNHIsZE4H3oyMD178FwxOnuZGuXt5Hc8QCfwqdBbaEVtH7zOKj6lKkjw9-57nD5wQmljL9kRku2AnY8CVkaB51E7dd0iKnp1niVbRi65-tzifmzL3Exad9rp6syYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
آمریکای جنوبی Core: تو اتوبوس تیم سائوپائولو نزدیک 90 کیلو ماری جوانا پیدا کردن، اتوبوس توقیف شده و یه چند نفری رو هم دستگیر شدن تا نتیجه نهایی تحقیقات مشخص بشه.
🤣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/Futball180TV/103487" target="_blank">📅 20:29 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103486">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hgQixB-nQGhm7gzRB9xtjs2JB7UQqvUXCyKQ1QBZAYcBCSDRDXMUP0dfM268wcTGUsqax2y_RlO2drfDLcRGll2nc6lPIjHraPBzJ3b3ecdOXfRsxMWgnvu714em4q_Wf8pmWfWUtPxG7hezzvL_Oomy8fxCAlHdhOTFNouo2oOZu6J4wSX9015orhL0ySJD7-SqGroXKhgeLgkc8YUK7ekN_ZdII7LULOULAz7d2RCYCXNQ9YKcZlZgcUIZkXsJl4flrfd7_ZR5I0rhT0ylDoylVoCzywHKKJtkLkh0NQYa_txlBeMCvreJrg20MW8BYGKcVNLiTQl79vF3TM3JYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
تو چنین روزی در سال 2023 هری کین به بایرن مونیخ پیوست.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/Futball180TV/103486" target="_blank">📅 20:21 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103484">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/azWfM-GZRu60J3n6xRbVZ1N2aAdW03cPxQP2PC4nSovxbWNrVipvmnondb9coG6G_oeUYClcXlUinwDVgD4uLOzGWHwY1dQQtFzQ-cE_S_tyNBxPhnJ1ThAQ1aRHoTY9xhcJCGOfGIS6MoWqc_Q84d2QmAI5IDjrq1bfZ_4Webi4irB1db8Em4RA4fozhP7x3xoUzbyfXWGIKXb9QBJ4KPV2NAFwc6JT3d8dxK4NebKxb24whrrSIO_JHke2x3e4WV_D1tGBmXhww-07oLNPy1zcD5RTnvDqK9fXXBkhY8WlZv8Y457BFFd9hHTNF8m6dQkB5eeSITOCZz6lruxMoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/s20V_TeVvby7vlMxWVHjw14cn6EPTHT5q5w58Rdt7CFihJ6pSazlaUl81JeMbBduSiUYm7Aj7k5a0FKx6qml0QnwXb5QxlYdJvcCvqqAU6ItpG69TFvCc6V2xKahS3u7zM1kzXADk5sNBwaudmzN_tjxVqAy5FJKEbCspNR87eCzioD654qfSuKikXOlL6mB1FuC31Zu2203BcZvRcsjdVvPKeUUxCT3ci6L6RYzJe0z9dP7-5MP6YyXD6aSQnOviXrC0WktzciDn9rAI9XHxIdgtxxgxG9jyKFMVzqJQeaJkw49khO6R_d_vB3Pc8DbHSf_zaMSCUZNem-uwRBeiQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🎙
مارسلو درباره اینکه آیا حاضر است ۵ قهرمانی لیگ قهرمانان اروپا را با یک قهرمانی جام جهانی برای برزیل عوض کند، گفت:
سؤال خیلی خوبیه و کاملا صادقانه میگم؛ بله، این کار رو می‌کنم. قهرمانی در ۵ لیگ قهرمانان با رئال مادرید دستاورد فوق‌العاده‌ایه، اما قهرمانی در جام جهانی با پیراهن برزیل برای هر بازیکن برزیلی یه حس کاملا متفاوت داره. اگه مجبور باشم یکی رو انتخاب کنم، بدون شک ۵ قهرمانی لیگ قهرمانان رو با یک جام جهانی برای برزیل عوض میکنم.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/Futball180TV/103484" target="_blank">📅 20:20 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103483">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBetegram</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M54ulZyCE20_9ZTUfFyoxvRgUcg7dCp55hoNXnewvBtj7iDlaO1AZSOUUKBtyrK-B4zRC9RpAzccjLDrvYK7QHqQBUKakUUnNQBnQkb7yrcApfsemjmeHDPW5-CMINLZ5U8KKcce07kI6ELVJiwZtAOTDHPnakBn_NxVJGqjLfHA5RAeZ4jgaqii-uhMOraNTkeKWB0MY1dc9tmPDQBcvlP3_Xgw0Y3LHYMbP8H27oxBK1xVrieBaIH66GcWR_l8B6SpOlxo35kaplG6Eg9YgHgU8c-j5hBXsF0una4L2hbngk7hd-j1dZSQNQI264B8r7RmDiRs7v9en0vwEtvM1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیدار دوستانه پیش فصل
🔵
دپورتیوو لاکرونیا
🆚
رئال مادرید
⚪️
فکر می‌کنی مورینیو ترکیب اصلی رو می‌فرسته یا بازیکنای جوان‌تر رو امتحان می‌کنه؟
⏰
ساعت ۲۲:۳۰
🎁
هدیه اولین واریز، ۱۰۰٪ بونوس رایگان
همین حالا پیش‌بینی خود را ثبت کنید و از بونوس‌های ویژهٔ
Betegram
بهره‌مند شوید.
http://betegram.com/affiliates?btag=3_l7</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/Futball180TV/103483" target="_blank">📅 20:19 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103482">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qJmmGPncBXEU7pSHgSRL0VtCfelQAyCoQjI5o78vo2wVeNOZ-at5-a2HrUdsVsrYO2XIZvC7TK1blYwSOnmgV9zEp52uDpeK-AaW2Jmay9sC-WSyu96GwnCj5mCodteKukvfZB4vFaDYw12WGLdAwwIFT4oJeF1bKxUTYx6mPv4VOeK0suH8lXezZRFzovBIPnPktlRf6kCCqB97taqFl8uR3Mg5m8w17CZB6jhdS9TMUqWWZ_aCKIshxVk3WwQGXWw4o2OvUUAKbk2jLCONln80rM3c__2Ol5T2feKDQuAQBkrY_R7suFRlSc4zuTcFXYHCcH7OZV4BU_GJLlMs7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
🔵
خریدهای این تابستون چلسی در یک نگاه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/Futball180TV/103482" target="_blank">📅 20:02 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103481">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FnkYWnnKRoRdAqgff4f3jyKha8184a-wCavca7VcN_TwjLvyMwnXxuAKTqnE_-V6UeD4kfJDFHXwZs_sYQAwJymHFcEvAl6LdTw3wxBv1lIPnrmV4VXaZkZ9wapCiwRm2Lsms5S-pVUpm_z1aT9Dmm--Fx-LnRUXq86QNXF9Vgf2GOOmMGsH2otlWWiQqjbJwUYkMXk62BjKh1jB2LSIQBmwIGWsM8H25YKWRg99ZPw4dH8cX4qCeRkNTL525LG1jPAdYskcRu_I8uczp0rAMWzEqoLFdY4wiJp0qBpb7xO736-MX4LqbCaWhahx_vWJWNVfDqfEJ1fiPxc_EnK1aw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📊
🏆
🔻
عملکرد امری و انریکه در تاریخ مسابقه سوپر جام اروپا
⚽️
امری: ۳ فینال سوپر جام اروپا = ۰ جام.
⚽️
انریکه: ۲ فینال سوپر جام اروپا = ۲ جام.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/Futball180TV/103481" target="_blank">📅 19:54 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103479">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oXlukmN3izdJxGq48tZhYCjlopuoQcgXeCmHZNeuy-hFvcvgI3HXDoXByHc4I5k5tSNjnp1HZ8Jsn0salIIRUtc91o3G8wQqorFcdd6qhwERnPz_rhbGARYCXVRa72NtldOoYocgyOXw77wckGxvD6vojcZGFHO495fFPc8okwxTUcDSH5NlYoKZBOy7EvgPsOF2A5_JXzDoK-JqxoN_T9nMVQ9fyctzdjT7erexxAOoga5auczTQHumhsM507lSVUv5c4HXD7SWucSEdckh0189v1-7gs0i7HHkZuZENzzsCCLSOsju6IZJ_qcg-dUY9D9RHl95vuNdriXzpf-clQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UbzJFaGVWTB3QAWnyw8919D8x3gEuEfsbuPvWtmWjprJ7MdVuV5xDUzkOboWINz1lkn70BRZ2tTwCi8gGnHy5a3QoGgFn8mkgqKzsr3rthR61IPPbGZM0M34ZQt7eH4UU85g8Q2Hs5gngll8qziGmBHwXjStusbjGFq6vt3wkTwt2msy7iBXVf8wlWdgVJCxt-n6Y3Bjj1rUPtSL6v9oGiVR01s2QRrLSfLI_Ar20ehv_Rf_aZjjHiUVIk0Arrh4Iy_wUyvP_VgrvVgDbSR0jUcp-VGTFpuGaer3tWiVFW-i8n9gQ16dvMbCQ1FufBfkG3s3SFYqFbW4eE0yX4cg1w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🎙
اوله گونار سولشر درباره از دست رفتن فرصت جذب ارلینگ هالند توسط منچستریونایتد:
تابستون قبل از اینکه سرمربی یونایتد بشم، به باشگاه زنگ زدم و گفتم: این پسر رو حتما بگیرید؛ فوق‌العاده‌ست. ولی قبول نکردن. بعدش که هالند به سالزبورگ رفت، دوباره همون موقع بهشون گفتم: بخریدش. اون موقع سه چهار ماه بود بازی نکرده بود و هیچ باشگاهی حاضر نبود اون مبلغ رو براش بده.
قیمت؟ فقط ۲۰ میلیون یورو!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/Futball180TV/103479" target="_blank">📅 19:40 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103478">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h-Gi6zOd_Djdc1-uHVMp2LKz9Jpw_fnAP2DPrSt5ay5ygmRGMspGF4CjVxpOwPO17YVm7JDyIMWe8Ldf-uhH8cQM1CMi9D_QgwlXWegPeq0KHUIq8JozSZpi_Wazb-7CSAP0KKQDwHStJDAfonvlnIj2l2Y8PZtcgxrvcFW_5Yz1muqtK3D-EWomGjBRZ8NS7TOmPI4yrn-yRiKa5grVNibLMsfkgczUb30JEzEzBnjTmMQA-VGSpMkxSyXlLTmcY_4bqyycr5C8JyM1fWm43TJ2M88G_iuY9WkhxYINv77pZSgoOkVX6LV7yc5zv1FZzsJl3wPSwylQPxaemBLl1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
✅
🇮🇷
اعلام شماره پیراهن بازیکنان استقلال در فصل‌آینده؛ شماره ۱۰ به ماشاریپوف رسید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/Futball180TV/103478" target="_blank">📅 19:31 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103477">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nXKaUuw6IqyAqDc858BcA4_fuypf0rNbnHBcmrenfXGXD-zXdr8VjqUqivEOHxSQV9YBwhByopJCmRWyt4scNwHUhAyD2kDXz66-ew_aChoR-K3ZcAJBoZHZFxwmF0oQuI4INeluMWtF-W8uc3js_SaadU2Tbp8XoC42BK8uclwtZf3kyRMHjCcMaAavGc3ipp1VFCFFRvtvFedpcDsZlWxbcPedezeFplsNDRKN0aoYVRBzSiD6XKI_qXdzBOUR-shcq6zC2KxdECc2jLuiE9G4Q5933AqLBZvtXK8PZjALZLLLVrYPap_AnlI_I8mCm2YiHuLyEHIGxREV2WfLlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
‼️
باشگاه‌های لیگ ترکیه همچنان دارن به خرید بازیکنای بزرگ ادامه میدن:
🔵
روملو لوکالو به فنرباغچه پیوست.
⚫️
دوشان ولاهوویچ به بشیکتاش پیوست.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/Futball180TV/103477" target="_blank">📅 19:28 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103474">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/S48sGLOR1O5Q7LjCA1TEeBziw_MpreCIOHAZ4X36AYIE3-KxI1_zjSRCKmGNmsyS6-mwMcpol9AWV8Ukw2TV9lOx7IYerY9NxvoMx2V9CSJ8w60JZeDpGT5u2lBq3zngNg-8f1mJQtDNbryCL_Yz3Iz2b2d0MxnwyXaVvsiUvxuiVG-7x5LreEbQhB6EQ3j6oCDbYv2AEnPvo6r_xuc9xjY7ZirqRNxcL_C1b0AJ-m8g7YUx3tDTmuadt3v4mYHKkZHPS_FOwTpeIemovpitfTpRvGb3lezmU64xzwuGmk601ir7xsqSlc94y21hMFb6mQ7ZV8oUa-6hmz3EoZ7ZcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ol0FxKDTdTiV-y2cHJRDT-EGXFyZLGdfIUmTvK3X7SLNZZWNEzZu-1OcWsGeXvdobfUGlOyppoqXk9GWoemuN3DI2TDTsCEFvf6UJsHG2wogq3aF0hUKbq5zlqrZ67T2UqU4IkYqtBzITqh1M--pjApZbgPQnwiPOgL6UHBSZg1fnj5K7dDh3a_m13gw8Fk8q4BHRxWA1tMrMluGkUX49FYbaPqlj3Ukm_wPdh_FkuWITj4n3GwvgsDqj_XXM2nf0Blt3gxMBzpfk7-rqYFqqygNu7zgG1r3V2xCCWY2gpyrpcPCu0AcdGAUasggSE2P3eBNPbOZonEzA2BNEZS3hQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👀
‼️
باشگاه‌های لیگ ترکیه همچنان دارن به خرید بازیکنای بزرگ ادامه میدن:
🔵
روملو لوکالو به فنرباغچه پیوست.
⚫️
دوشان ولاهوویچ به بشیکتاش پیوست.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/Futball180TV/103474" target="_blank">📅 19:26 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103473">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/30210b96aa.mp4?token=S5vqdcezv_pxdFq4Neu3aQKxpUSPu_A8LLR_jYCHhV7_nmb2dQcQn8685te9opNsQho_An5i99NUpnOL6W1mf6gV6jkvtWHgJ8yKO4MlbV2tp2l3VBWCBGQbf2ZcoIAtlD5SY2f7WsJPPdbATE23L-jYXor-U5vwwT2q8o8bUzY4qp4jmpf2-o4Wx080kzx1v9c3gmcSPxJb9YlY7sNFgrL7S3UJWsb4-_mJpVRxUuSZk5HLV_UIAuKt4fhpWd8FprTUF78xZMJditLoKVcwklWrOJn8atoyZi65OcoSWbU6PJrLuMGvyUhORnl-hkSxiGNTSFaOQ-WcqlbIa2QPkg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/30210b96aa.mp4?token=S5vqdcezv_pxdFq4Neu3aQKxpUSPu_A8LLR_jYCHhV7_nmb2dQcQn8685te9opNsQho_An5i99NUpnOL6W1mf6gV6jkvtWHgJ8yKO4MlbV2tp2l3VBWCBGQbf2ZcoIAtlD5SY2f7WsJPPdbATE23L-jYXor-U5vwwT2q8o8bUzY4qp4jmpf2-o4Wx080kzx1v9c3gmcSPxJb9YlY7sNFgrL7S3UJWsb4-_mJpVRxUuSZk5HLV_UIAuKt4fhpWd8FprTUF78xZMJditLoKVcwklWrOJn8atoyZi65OcoSWbU6PJrLuMGvyUhORnl-hkSxiGNTSFaOQ-WcqlbIa2QPkg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کمی هنرنمایی از رونالدینیو تو پاریس ببینیم.
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/Futball180TV/103473" target="_blank">📅 19:20 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103472">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7767f0d57a.mp4?token=o_UQUvDXTieCBOGubfFDnd9aivbtLIbO3ZsKIGO4aYfWhdnUgi0e-sITqsDQxjUKGPRmmFAAe7ZRvVmDypibwkFdjdYenPO5uairnWLHIIGvOOYNbL6SJgIxGcD9vXEF1LJ7ac7q1AgKx0YHF23nFJqf6UEy5pYTd0qHCQhxmwLLBD42mZBLcokYQARsHEH1Jc3e-FqcBrsD7PBohncZEiSmJLRZyRldC0nmSEOJXu-o1a41FY3mK05xDHC3kllr050nANnAn0GnEtLcuYCUTr70yJoLyv7XqqfJbQmeZ3G2SGMwWWd1PSPZbGL3UfTQgbthOctwYGpAy7imIeQUyg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7767f0d57a.mp4?token=o_UQUvDXTieCBOGubfFDnd9aivbtLIbO3ZsKIGO4aYfWhdnUgi0e-sITqsDQxjUKGPRmmFAAe7ZRvVmDypibwkFdjdYenPO5uairnWLHIIGvOOYNbL6SJgIxGcD9vXEF1LJ7ac7q1AgKx0YHF23nFJqf6UEy5pYTd0qHCQhxmwLLBD42mZBLcokYQARsHEH1Jc3e-FqcBrsD7PBohncZEiSmJLRZyRldC0nmSEOJXu-o1a41FY3mK05xDHC3kllr050nANnAn0GnEtLcuYCUTr70yJoLyv7XqqfJbQmeZ3G2SGMwWWd1PSPZbGL3UfTQgbthOctwYGpAy7imIeQUyg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🤯
🚑
⚠️
پشمامممم از مصدومیت فوق‌کیری و عجیب در یک بازی‌ دیشب از لیگ لیبرتادورس آرژانتین
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/Futball180TV/103472" target="_blank">📅 19:18 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103471">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/438b0dc101.mp4?token=rC9m6kGHIh0d_gJY3ph0zHZQiFNhU0K8lVxuupE9tDyhW1POOomXCQFtQHUarilOgY3lsfkAkrxmQ9VQDr6kPFbi3L25ahEvCpBTwzXmCsZB296C-VrzyGnSKfgLxYPhYzuTgbohvnfY0_3VOwAYjaSoIziJmuosfZDNId94nGR4C5lsVbeZ-M8ND8fbsDXk_5jjwi5KxC2UpPYzIPT0WAS8FdER1iGstrcNGDFIgt_is7b93bL3zGLeBJcBGwsWcSSz5Dj-9dg24fKsfBkJ0uUsawI4xIJtKBw1UcepHBIBysiZYqOzOoUIFAwL-wHF56_W445H9S-D6FqUa0MBUQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/438b0dc101.mp4?token=rC9m6kGHIh0d_gJY3ph0zHZQiFNhU0K8lVxuupE9tDyhW1POOomXCQFtQHUarilOgY3lsfkAkrxmQ9VQDr6kPFbi3L25ahEvCpBTwzXmCsZB296C-VrzyGnSKfgLxYPhYzuTgbohvnfY0_3VOwAYjaSoIziJmuosfZDNId94nGR4C5lsVbeZ-M8ND8fbsDXk_5jjwi5KxC2UpPYzIPT0WAS8FdER1iGstrcNGDFIgt_is7b93bL3zGLeBJcBGwsWcSSz5Dj-9dg24fKsfBkJ0uUsawI4xIJtKBw1UcepHBIBysiZYqOzOoUIFAwL-wHF56_W445H9S-D6FqUa0MBUQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
سوپرگل محمدصلاح در تمرینات ترابوزان‌اسپور
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/Futball180TV/103471" target="_blank">📅 19:04 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103470">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LPX-JF19TqihrOR8MsyIbrYGJ6UgWD6KyVasiBxzA-H9HBd1oxshMDdA0JNcHL2Oygf-MCuOlMkWXKrB-MBTyG2P-r4LIUOicuJNqO-eH5X14QPNUR62cEfU_G6dMx_yQYVEV5_eBiAaMRCqNkarkehOOvGMKmZV7mbohVeSPpAXc6LqDLJ-x3Bk19Y7j7fRF9VGdRANCLrAbgf0AYKuSRGbTe2wRh0jbQYfv_dURxCI2CAk3KOpqLa_Y6PTg2nWLwpizUQ3RjyR3Z_6dlk-lRZgIrJv7t9gEvb39YcpqKMi2WOK7LsrdRztB796eqQxsZa8KDcKdWIrLZiiufbhBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇪🇸
⁉️
ایجنت کونده امروز تو شهرک ورزشی بارسلونا بوده؛ پریمیرلیگ در کمین است؟
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/Futball180TV/103470" target="_blank">📅 18:41 · 21 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
