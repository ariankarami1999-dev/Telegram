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
<img src="https://cdn5.telesco.pe/file/FcIsEUqwHUiJMiI4h-c4KPWeEfQJidd04r6LyLlTyPFUmqCVNeNjl2O2piStDSqQ7s7Clk8rn6EE509w8Kh-LXW8ZZ9N7ezY4wzSN4B6X-kSBf3zKWZl0UsIH63SjdFuhq77asCF-0qhMSlwFrM44cL3QATVLz7hUFdrnvMrxUhjePK2khVGYq7x4jPPAfwGmedZ84uM4YquNKN0jbNuyUVmZg3CkvhjVdtfQRlLuKfa-mp6mL63x9PpEyMss0Eniy2EUhBSnv1SaLNrAR_KKziS_16b5QOXnXhhHaL8JZxSrI2gilfogjPKoEDcaWEz0jQrdkgei4HBlRV2TVk3Ug.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فوتبال 180</h1>
<p>@Futball180TV • 👥 506K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-10 11:35:11</div>
<hr>

<div class="tg-post" id="msg-102498">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/86343d5e54.mp4?token=iSdCK5DgGRK-jRv9EuYDoso7pbqnH8lEZF3zUS-aW-eORfw4AEZQfRhp3D121lXAYv7Lq8nHooNCzKXpfVidsoPpxeCsWJ4x32YJ_dgdXPRSzlSJK5cCuQ4MH2gZIxdBbhEHdYMDf26JKKRzxIPsAre9cs8MzFxXLWx-fPqEYL0BkYJ3S71IYSK8Jbi16XtcXuSaXPLlsR_Ro7Y8coM7wdZRfTpbv0QKszEMluNfBg_2hkZmoPeO88wAK6aO8gtqqJay5EQzzJ4KpbD3ticLMaca-rswEylW1gVVmaHFAvtl3doB40FY2m7ln7464F1TEIm0WBkM9T15A-X9vZYADjYSVS_HD0d4nKGQWItwOWCoYrjCf6lsJVxbpoHfJ58v3TLIOZvlkvM6rLi2AXnWSPKd1JNPXAjFpR-SCYVIsGi5A0Focj_l7SqYuLM2Z6jeeHoZDhK9DygrFxw6sZBV8cDKk2OQa5QCh9a4FDcwL1r9E_0a74oD-1ssieWuhPs837jD-MZJHkBNEtZ_uyV7G9Sf-C-vaKbYOt0MWabXui9uX_gjqPDlUgH3S1M2ZcbY8ER_1vMUJM9qFvMmKEzFFnUQMHBcS0Ry3_9caK5qh40sLyS3_pnJoQv-xgf3inQnRAZ7XHovu2iTO7zLTcgoP4ESBAKFwozNxg-IRKvkUS4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/86343d5e54.mp4?token=iSdCK5DgGRK-jRv9EuYDoso7pbqnH8lEZF3zUS-aW-eORfw4AEZQfRhp3D121lXAYv7Lq8nHooNCzKXpfVidsoPpxeCsWJ4x32YJ_dgdXPRSzlSJK5cCuQ4MH2gZIxdBbhEHdYMDf26JKKRzxIPsAre9cs8MzFxXLWx-fPqEYL0BkYJ3S71IYSK8Jbi16XtcXuSaXPLlsR_Ro7Y8coM7wdZRfTpbv0QKszEMluNfBg_2hkZmoPeO88wAK6aO8gtqqJay5EQzzJ4KpbD3ticLMaca-rswEylW1gVVmaHFAvtl3doB40FY2m7ln7464F1TEIm0WBkM9T15A-X9vZYADjYSVS_HD0d4nKGQWItwOWCoYrjCf6lsJVxbpoHfJ58v3TLIOZvlkvM6rLi2AXnWSPKd1JNPXAjFpR-SCYVIsGi5A0Focj_l7SqYuLM2Z6jeeHoZDhK9DygrFxw6sZBV8cDKk2OQa5QCh9a4FDcwL1r9E_0a74oD-1ssieWuhPs837jD-MZJHkBNEtZ_uyV7G9Sf-C-vaKbYOt0MWabXui9uX_gjqPDlUgH3S1M2ZcbY8ER_1vMUJM9qFvMmKEzFFnUQMHBcS0Ry3_9caK5qh40sLyS3_pnJoQv-xgf3inQnRAZ7XHovu2iTO7zLTcgoP4ESBAKFwozNxg-IRKvkUS4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🏆
پنج گل برتر فصل‌گذشته لیگ‌قهرمانان اروپا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 1.83K · <a href="https://t.me/Futball180TV/102498" target="_blank">📅 11:20 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102497">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vwRvnMfsoc2UOnS7sJYlnX2akiSBMBc0dyqn0aG4vBr4tAfdpH5zs_nYESkqgn23gWdC9cqQrA3q76StUgtE7RU-kdrEYzIP7ebH-UyKCnae8IYOrxnU9oZyb-UglwpFLq7KcuccWIn4PpVBQgc1Y4Za-X4L6s47B0xN84AWaqzCyJDTtsPrmWheJ09Mcxuc9fMh31KqKfayqpPWcvvK9rQZRHMJzjZW74zO8YW7U6ewewxNtx4UqYrUj5NU5GJOVRRoxRYHFR4GqLgidM7lJyiggDTsvTSIDgnMsfvnkyuNZx_2g-oGcPIm4kp1Tj9vzF7ONQTPm0C4wFGjcYjvRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⚽️
اینفانتینو با انتشار بیانیه‌ای اعلام کرد که طرح فروش بخشی از سود جام جهانی به شرکت‌های سرمایه‌گذاری خصوصی، به طور کامل لغو شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.01K · <a href="https://t.me/Futball180TV/102497" target="_blank">📅 11:12 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102496">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e324940235.mp4?token=Bl5voWHdlRCMsZ-ZFpE1PTscJ5x4F9yWPvOCfx1on-oS829a8DktxJlcrOpFwlhvNrstCmVqipJ1HUlxMG35vrI0ulaIl00_GF1kS2lTlLuyF6AVyB-0o1J5rW-V-12L0-GwM-jUecW49JbAIwQVWOYrg9NdzraEtbue6c8C_ptAn5l0KOl3X4gNitRYw5DiVaJrWvIZCgdCH7AhqELVSSXsyLzPl9YpfvCU6XE3Nh1obV8NVd7fWu7s7xUAR5zDwXbAr-K-Naedt_-y3irYBeGRTNWMzRjJ2csrQ5nSFGOcjNb5WELPXNrkPuwWaAi33dy2gyNh9mu0P3JLyw39nw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e324940235.mp4?token=Bl5voWHdlRCMsZ-ZFpE1PTscJ5x4F9yWPvOCfx1on-oS829a8DktxJlcrOpFwlhvNrstCmVqipJ1HUlxMG35vrI0ulaIl00_GF1kS2lTlLuyF6AVyB-0o1J5rW-V-12L0-GwM-jUecW49JbAIwQVWOYrg9NdzraEtbue6c8C_ptAn5l0KOl3X4gNitRYw5DiVaJrWvIZCgdCH7AhqELVSSXsyLzPl9YpfvCU6XE3Nh1obV8NVd7fWu7s7xUAR5zDwXbAr-K-Naedt_-y3irYBeGRTNWMzRjJ2csrQ5nSFGOcjNb5WELPXNrkPuwWaAi33dy2gyNh9mu0P3JLyw39nw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👍
و بالاخره تحقق رویای دوران فوتبالی کاسمیرو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.12K · <a href="https://t.me/Futball180TV/102496" target="_blank">📅 11:01 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102495">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">👀
🔥
هشت سوپرپاس‌گل ثبت‌شده فصول اخیر
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.22K · <a href="https://t.me/Futball180TV/102495" target="_blank">📅 10:40 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102494">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LuDUKzJs5mE5KePnwIeMi_1iQ9AbhKM0KCULlVIXto517-6VTVbIIQ7QUsAJe9EMj5aQXrvlYEePC0PCAU1_GhBElQfz9LrfibsU1vw6y8s19JnUW_5BjUJg2Fy366aKzrkTfVRJ5Fn5rW0RkBpLt8IKGJRurQEF_bhjpxmHbxksR23HjTxhQvb9lQ6o9PBYyuPc2lWnbmbhHONDBxCAl6C3bCwHHAxtNTmPr3aSLQG1GstnubTJwqVy-FloBtnD5En1_N59tbJwAiU-hPBubG5H5cW0rL2kT56CKIB6BxF0Ss-p19ygQSPCyUm8HH98GIYLZRlPxdqf5Jg_KzsQTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
مقایسه آمار مسی و هالند زیر نظر پپ‌گواردیولا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.34K · <a href="https://t.me/Futball180TV/102494" target="_blank">📅 10:20 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102493">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gvfujV1Z40npbDQYKOnmQyKyWhpoGRO_5YZ6ts1LZuQCHpVjwCfDi2YFbhq-HSrVhFhiet9LKjwQo6Qijo19cCBF42ohyO-IRJ54e1qbSeoWyfQf_EKTHU7Logz87Nx7HaM1KA9_s6GWfpmvzYHy_Ga4IsYa1aCY5KoSSjciSvpHLaDnO_s2eUK7KBd_bkc0PwQDSn6r7LieHLPO7zmqs5La6bXPpah40y0-8_yXAkpbwWoOhKKLECW8IXxpBtoyRn4eXtyybgAEpqK_xvzmbdwaaHGb6CGAvbCmFu98pWeaipP1De8y2c1Dk74d_mBR4kv1PJKf38pcfIO0S6tAhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
تمام قهرمانان ادوار مختلف پریمیرلیگ ایران
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.77K · <a href="https://t.me/Futball180TV/102493" target="_blank">📅 10:01 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102492">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AaQLh5h7nU1YDMZpCjMBwCrkhjDrRZItCfP-QHQ6YLfZi9ylXF7Xcs_YcwMnq8NqZ56cnYjvYIqG9fk7LsJkLrzmRUMwE1y3OhY_LWnIsjX4-hhSvpkPwXxzwjFPfIPavFjyNnAZmznq9ApFnINOTfcKCL4OELDe2hzJTb13ZAHQ6U5eddJsX8iIkdabzLkWDLTPiHpU7YuM4bBSGvtdR7dxaAUAOAfOBIagsR-FxnEcuNa0lVFFf-iz9RVbiOkHRXQh89jselOC9sPwrtPVx9Izbz7Lh5IF_IyZqf_lxXjmc8OWIaoTVTvZPsgZrBNyRV6YkVXslu7rMMe2ULDE8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
💥
باورنکردنی است که برخی از زنان چه توانایی‌هایی دارند!
💪
ژوستین وانهائورمات، هافبک بلژیکی تیم زنان کریستال پالاس، در سه‌ماهه سوم بارداری خود همچنان در حال تمرین کردن است
❤️
او ۷ ماهه باردار است و همچنان با تمام توان به تلاش و فعالیت ادامه می‌دهد
👏
😍
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.72K · <a href="https://t.me/Futball180TV/102492" target="_blank">📅 09:40 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102491">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N5RQ4eI3U8Fm-COxxW8lK1aodHNFLoJsLSt-zgbKJ9NA5SVkfnQJKSv0MthjWxovUGeEbjZZqEULNyV6719LQzuVPli2ZhCXyJzChLHuUVeSjhKF0jnippBB0D48ALHSyhJ8QbTl2CiGIHRK5Nib5vG7ZRRQkzKQHyQW96CtHBlBeNZMCcyIk0q_n3pXEbCxBH7r74iZo9b92z0RT_0eDMyTn5zSEw_KCRr9VcC22t2uTNbMC2eKfLMgHKszWErD9xKlKzti6_MF9ZxpL6sUcX_ObiFtI5-5ic-ijmtKfmQdYqXb1kHYOXcpoG0IfadL2vmVbd4KjeYskQUgdbnOXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⚽️
🇫🇷
فوریییییی از فابریزیو رومانو: پاریس بازم وینگر خرید! مگنس آکلیوش، وینگر راست ۲۴ ساله موناکو به پاریسن ژرمن پیوست. مبلغ انتقال ۵۰ میلیون‌یورو و تا سال ۲۰۳۱؛
هیر وی گو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.49K · <a href="https://t.me/Futball180TV/102491" target="_blank">📅 09:39 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102490">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b17b2ecad4.mp4?token=bzBR6DKt9lRKeumx9HAdkUIxhjQg70eXGvLLwmJU6X-5JFMCTlECl9-c1TWTJYbjV5c1GQHOz0D2oD-1l0VTbHsWrKAqt1WqtoIX2kR62kcxFWp1x1S316KOY3Do-DpRBTOzqwIoCrzZ1sD9L3mgww5V4w9h-PtTL3uHDyFeccWSvOl9cy8nC5mepI2XgvDiK8hD2qmO3J8GAd7EGxMVT8j908AGnS0KyV0Mi5pdgBbR8Yo1J_7g4juMjlJqQPB7rv7IOM-SLGPzyLzIAj-rfwiLbWRdsFNKSJSQJs08__VPwTBBngwlbaS1fhx2byuIhYO1uXELzZtFZA63iSJnXpssTbXQOMTAcpziOsyDRr3kNIITDfoRXgLLMob9wK8ZE5fEUHS7M6zAzYTWoR4_0Eot5f37jGyj_rFElGcI4DmdN1Xfae__KFC1Jcwhbm8QOg0yMp7iUkWPpgvXVoaxxCcW2CCQ9y93ZGWBM8vForzuMb-YX1IJ5iKgL_B75mJi6e-frpvoUs614nlZ36DSOowM7zXmueHCvpKnbE4zvKCELYFgoXyLYwmFib-Th-FPR8RR1SfELHgsIl7axPSysI89HJ5YVHL8B_CVrIMQ-Foq25Ejn0Tagu-_VR470Nnn2ehMs5rJk-8VdQiQNAym1E8wvufJok9-vbDkj_50WVA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b17b2ecad4.mp4?token=bzBR6DKt9lRKeumx9HAdkUIxhjQg70eXGvLLwmJU6X-5JFMCTlECl9-c1TWTJYbjV5c1GQHOz0D2oD-1l0VTbHsWrKAqt1WqtoIX2kR62kcxFWp1x1S316KOY3Do-DpRBTOzqwIoCrzZ1sD9L3mgww5V4w9h-PtTL3uHDyFeccWSvOl9cy8nC5mepI2XgvDiK8hD2qmO3J8GAd7EGxMVT8j908AGnS0KyV0Mi5pdgBbR8Yo1J_7g4juMjlJqQPB7rv7IOM-SLGPzyLzIAj-rfwiLbWRdsFNKSJSQJs08__VPwTBBngwlbaS1fhx2byuIhYO1uXELzZtFZA63iSJnXpssTbXQOMTAcpziOsyDRr3kNIITDfoRXgLLMob9wK8ZE5fEUHS7M6zAzYTWoR4_0Eot5f37jGyj_rFElGcI4DmdN1Xfae__KFC1Jcwhbm8QOg0yMp7iUkWPpgvXVoaxxCcW2CCQ9y93ZGWBM8vForzuMb-YX1IJ5iKgL_B75mJi6e-frpvoUs614nlZ36DSOowM7zXmueHCvpKnbE4zvKCELYFgoXyLYwmFib-Th-FPR8RR1SfELHgsIl7axPSysI89HJ5YVHL8B_CVrIMQ-Foq25Ejn0Tagu-_VR470Nnn2ehMs5rJk-8VdQiQNAym1E8wvufJok9-vbDkj_50WVA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
بازی‌خاطره‌انگیزمیلان و یونایتد در UCL 2010
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.98K · <a href="https://t.me/Futball180TV/102490" target="_blank">📅 09:20 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102489">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">هایلایتی‌از بازی‌جذاب الکلاسیکو در فصل ۲۰۱۲/۱۳
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.65K · <a href="https://t.me/Futball180TV/102489" target="_blank">📅 09:03 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102488">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q7q3yDIgOI6aD9ghFxhJoTVh4n0mdf0EeF7cgAIfUN5UaLBoPodJQ7fABvyAn0A2_IgWzidZd3yq5DiHSmahw9bcm1nB38TQqsMUkKNQNcA_0MuuDDfNha7Knt32VAYGrrEZvbmKYsxg6MYEwnMuARJij9-XoaotDAR0ExOgGsUY5Rm6vwpUbbpXfu8NP-tLVuY5MYgB8Ihzi5rs2f4-K4q-49zAwKwT8Bt4a8htqvVmlWMMK2OvNvvPZt6ZuNJsZwb5iMZDPRK7Q1JLYmS4wbrzCgG-d21RNsksDExh0clfkcjk5TlfLY4LJWfazfydvawqu-mfCFJNPie0lGxpuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بازیکنای اون ترکیب لجندری بارسا چی میخوردن؟
مسی عالیه :)))))))))
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/Futball180TV/102488" target="_blank">📅 05:59 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102486">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eF96ltloueL5yidqKhK4m68FdV-Hf77RpL3qW0DjoSWIKRQTDvTivyZmUlrR07YqjffZYq20j3BYGtIYQ8LDLxEXOb_vHcWYmGYtFv5mkywik77SJG4uy7KMpK0f4UpeGAlNnsUNhm30l8vsK1L-Z7WoHxBFfNTHYYTrXDWTQ5jr-oP-hUYLY-VLbBaMaOHkL7L_8cLTbYAc3186RQNUpqdOOBCYSjBGDGBnlfVdUqpSdwCDmr-BQOlK0ffwhemuA9I3UgZgkop8NQR6dvhE8r_w6dNF587G1dRss8f35KzuaMOiLsXTjyjVJ6sRO4xmLZ6Feifn0NBNwZYcjPLHnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇫🇷
گوئدس ستاره باشگاه آژاکس با رقم ۵۰ میلیون یورو بزودی به psg ملحق خواهد شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/Futball180TV/102486" target="_blank">📅 02:00 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102485">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
🇮🇱
کانال ۱۲ اسرائیل: نتانیاهو در دیدار اخیر با ترامپ موفق به راضی کردن رئیس جمهور آمریکا برای بمباران زیرساخت‌های انرژی ایران کرده است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/Futball180TV/102485" target="_blank">📅 01:47 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102484">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tBDbcvg28_Hz6BEMr8Yg2JZMWZmlOCkl1LZl2eaF7rQZbBY_KItzWgN-U6b0Afcs4Sa2614MML0GZ_5Ccw_4blsgTgMC3auPs1bQuZ8QzMh6E5zdKZckeI1h6esVE74t2qF3d4WNxMC8Yc9BwYVuL3G8fwdiKJcsuM58QCn3fvyl_Trb72FeRRosojDwyNjyUoSZ8_M_qO_65AFhoE58J0M36kOL_TP6BSB7pHWAvLw1UaS4E00WPc3fjwkuLw9ce9Mjd1Rvvr08OqNNm_nERHwjzSvzr7uHiK8ufIXGXfWcw8dlZSQQrcRkOyg41m_tMtnb2Zo179uLcOsEVUTgpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امشب بروبچ محله تامی شلبی حسابی واسه جود سنگ تموم گذاشتن.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/Futball180TV/102484" target="_blank">📅 01:26 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102483">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🔝
وال استریت ژورنال در خبری فوری از صدور فرمان ترامپ برای آغاز یک حمله نظامی جدید آمریکا به ایران خبر داده که می‌تواند بزودی در این آخر هفته (شنبه و یکشنبه) آغاز شود و چند روز طول بکشد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/Futball180TV/102483" target="_blank">📅 01:10 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102482">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/edBSh1GaeRuz_SnJxCe5heoOIidGWrOlkBi4pdNa_Ybi_mWeqsTS61lTv2C0PauZ9jUPilccCnod-EgQAlFJ6a63Y-FItjqTHRJTaBGqcl_PQPJ8BMT5vx3n9WJS2XIoRgKL2YpY6R6XYm5qT2q-wXY2osRlAT0jxsdnigDNibr5sVcfp4SINpnH3W4nmZEb7yEVzehx3nWVJ1LwsAcaRLnSv5WskzD0mi3SIRY37VRlYAY8s5QKyYaxwymBJNjeqmUma0HB62tBaTy-NU_if1q2Nin74ynFXTSoM4LnJ8tWZa_93tmBU-J3-dbTdRdvULplIIrpoJRq7y35TJTtKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
🔝
وال استریت ژورنال در خبری فوری از صدور فرمان ترامپ برای آغاز یک حمله نظامی جدید آمریکا به ایران خبر داده که می‌تواند بزودی در این آخر هفته (شنبه و یکشنبه) آغاز شود و چند روز طول بکشد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/Futball180TV/102482" target="_blank">📅 01:05 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102479">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Y1lY4nX_NS_1lGl76WSpFtpCttQvzASce0ln1DlP_oDEJRzHqR35SfCbeLIGQft_dvHjRD78kE2boANSDaMPuUAnytaSs2ajyFz1dUnqgSBYFDQlFdUPmBrIxhNbWkKiNwTydXBXV9nr4y8pm7Eb5fng0BZIFpNzmCLykbYCmPIz_ViVBYbC_j-1Qq6aVOQckY6iwK57oFiWo2Bo4_kUW8XPFFOL__cE1ugKDAQB69KslFTRKYVkrDzLpYnruDPxpqcsSZ9kzod1yjt586HPLm8aCKhSz5LFQ1I-dwacSA8c3qVsSlhTBUSCk8prnu7qHS5JCHdbVQHPxkB2VRhMXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gBoC4qO03lwN-ZQ7eQbFbimIdBUhe5fB7qogfmvdVgHIKfK3cqKoDAXNmFtD3jkUHw0oma7DSwI1kIZVcHkxrwJLVGzs_nhUjmUyOIny2iaVjLt5isJWayHswnfR58JTMlY4E3DMnz68-KY06XQabH1z0m1cPMWaORi-UpbCLlHFFjzmyQb0ylwrGPrPdS69vgHyqm9GJzPK6e6VQwbqomMg5NFbD-9pnk8M-p5zRb5oWFwU4HbtrsBpXvS6qPQbzgvtNYN-fVNS5ypCJJzY85dNTKK_rM67EEwwr2SjYC1zpGyxeue6sGQO27XOIt30d1JDgdEBBfpOFRyxNF95Fg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/j6deKlP5xYjwdAoUOsYZWyb2kHDXxua9_mr4Ds00_R3I7P-MnO48rYPvWKHBQS2XeHUiEt_XhdDbGmlL1o9UVEd-wc2zPXhaSdFxUyw2j1H4kNVJ_IhausjpfkPpfGG_leRxuIzdbcKOtvRlBAto4CigvJphR9QpkBjMNXIW5JoigvLLTn_3JvvyVlk0qDqr-hW47z1ndexKD_KvMb-Qp6nk6RYoD8p6_m4Koq6mxh-CFl7bYEcQAVmkJjdzzmjrkTA9Tusxm_Xh2xNXAbmNsuBZN5AAb7m-T_srYURCjqm3RgOjPWfCV_ZclsioqPyDjaKLccOJhdHXWV6CmBW9Qg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔴
باشگاه فوق العاده محبوب آگزبورگ از کیت خودش رونمایی کرد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/Futball180TV/102479" target="_blank">📅 00:42 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102478">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LG5ad1so2sO4mttE7gPjjNZVl9OVyqAwJEasYSKI2ibVSICOsHCbjh2ylvjdIWWmxYfG5M9zz_q0Ocnz03LD7y5kN4FZXGQRAzXSKGogfbPvtdQr18FML1aunBfra9juTQsVIjK_J50Uw1DO9NPb0-IX9antrnOb5S8r1MFyyZFcjF4ru_NU1w7VJFp0x1xkXJ3jKhANhZe9ZEKqfs97EaLGi_0qSZrlYX5VuT7L4clAy8lySvZGnEP_SxXJUTkOvho5YttB6fKREM3v9CdNghBZ-JuEJs2C1kqz-ybFfgNmWt5bYnppctt_cUN9BS3r7AMReZm0LJLaSh1uUQvv4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
هندآف آرسنال رسانه نزدیک به آرسنال:
وینیسیوس شخصا با آرسنال به توافق رسید.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/Futball180TV/102478" target="_blank">📅 00:32 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102477">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">چقدر روی فوتبال باختی تا حالا؟ وقتش نیست سبک بازی تو عوض کنی؟
💸
دیگه دوران شرط‌بندی روی حس و حال و شانس تموم شده. اگر دنبال تحلیل‌های دقیق بر اساس آمار، فرم تیم‌ها و نرخ مصدومیت‌ها هستی، باید جایی باشی که تخصصش همینه.
🔹
تحلیل اختصاصی بازی‌های روز (جام جهانی،…</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/102477" target="_blank">📅 00:32 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102476">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/316f36114d.mp4?token=sUkYV155FsCCPvHrB6OmDVUTfJAgXl6yboSjkLSiHRUeigKCOCW_jWyDtHJ3BFAwUCHGl723hWDpHKCaSCalvaqijuRRnWTOShZqm2RE_CLR5Go4gmTjUf9czJm8sgb5KR4ZF-16WaUss9AtTO1sFB--aa8E82qfw3_u2ZKTFuFNCfG1DxXHvO86q3j2RSD8Vso5xPw5Fmrc7NabqN8rHixDf_roytPXTMkGfXdRTwZ3fde2edHbhgegT8u4VJjnj3WzBVptYmGCteax7kSlMPyNQtYdirHUdZ77Rshic1lu-3_-slyh0vH6rkzZUL2PUFYz-TEFQIeJtd1ExyiYyg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/316f36114d.mp4?token=sUkYV155FsCCPvHrB6OmDVUTfJAgXl6yboSjkLSiHRUeigKCOCW_jWyDtHJ3BFAwUCHGl723hWDpHKCaSCalvaqijuRRnWTOShZqm2RE_CLR5Go4gmTjUf9czJm8sgb5KR4ZF-16WaUss9AtTO1sFB--aa8E82qfw3_u2ZKTFuFNCfG1DxXHvO86q3j2RSD8Vso5xPw5Fmrc7NabqN8rHixDf_roytPXTMkGfXdRTwZ3fde2edHbhgegT8u4VJjnj3WzBVptYmGCteax7kSlMPyNQtYdirHUdZ77Rshic1lu-3_-slyh0vH6rkzZUL2PUFYz-TEFQIeJtd1ExyiYyg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چقدر روی فوتبال باختی تا حالا؟ وقتش نیست سبک بازی تو عوض کنی؟
💸
دیگه دوران شرط‌بندی روی حس و حال و شانس تموم شده. اگر دنبال تحلیل‌های دقیق بر اساس آمار، فرم تیم‌ها و نرخ مصدومیت‌ها هستی، باید جایی باشی که تخصصش همینه.
🔹
تحلیل اختصاصی بازی‌های روز (جام جهانی، باشگاهی و دوستانه)
🔹
پیشنهادهای دقیق گل بالا/پایین (Over/Under) و گلزنی هر دو تیم (BTTS)
🔹
بدون ادعای واهی ضریب ۱۰۰! فقط سود مستمر با مدیریت سرمایه.
آمار ما در ماه گذشته خودش گویای همه‌چیزه. فرم‌های امروز رو از دست نده
👇
🔗
[
ورود به کانال و دریافت فرم‌های رایگان امروز]</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/102476" target="_blank">📅 00:32 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102475">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GM9WkHhC9DUmoawt2xycjRetnyrf-4yS2j-9667SYNNdO6q6bwsoGRpPyDaCM4Ap321fFOyGLIuK45gPo6lQHZcUw6dlpxkbUQTl-8Wm4mXkA3f0XEaWpYhOULujqjV--WXrS_-rPD2sB2HQyRvhYSedQjRjSbkeyoD1JXeY4ZKBTWD5c1QdqZZaus1UNCGpdzlwtNlMDEpZ_2XM-TRpL4nmbmY3BJ0E7f-72XZiRlBPYYRJLzwe87mb5nTpeRZ9sGZRpg3nit2Eh6tJznQwRNI8qHfFJyw9aWMsJBy7CK3s2B5vknk5-XkiWKW_SQzDOm3IRhiD5JRxjTtdJcpHRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
بارسلونا در یک بازی دوستانه مقابل بیرمینگام شکست خورد. بیرمینگام با نتیجه 3 بر 2 در ضربات پنالتی به پیروزی رسید.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/Futball180TV/102475" target="_blank">📅 00:30 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102474">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g_BkpDi_CrVjcD417jVQEzkBg7vqTa95cJWUbU--fuo4YQ_HMSn2M6q_Imp82UhpxfT4MoApdIY6HAzU2tSGHeAy_GsNi4l2bNNwcu35vOjFBWEDf1RaXR5hoX6_qHTjpvIjMvNbmLzq-E-pERXzzsKkCZi16vFGL8aJCHScW0dtihg4-7qQrly7OCHbBqlvGakBwxzQGV0fLim-LHtjFZIiXPzeTOwavIMiWcxihGcwWNuYqDDEQKskJDJDzEpAfjM2G9aWpA_dr58wS_b-ZdWdVZXCvi4jo-cDwqDOEer4F9Lees3a8P4rQ-3Lqt7gRlxp5dSLCkaoTbKS2e0jTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استوری دوست دختر یامال
😦
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/Futball180TV/102474" target="_blank">📅 00:29 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102473">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fZ8I_VRhIrXhqgmSMqD6cpn2C-fbM8FaBW6gxw3L5DPyuoZlxIUXht_MgJlYd8s2I5Rbu6Xx2rPQXYwPYf6M4_uOz-HReEZRaQGWEtRt08tO0Dare-mykYemrjc4--K6vKm3I5ude4UkXQxEoxnUpxaQNdEI7mCgayf5LpEtkSjXyXMPFIQQB-SxUXkVNpHHEM6tw86wfeaFMoUEZF1PvGwi8WBDDE4hwaFlRVhPj40PgLm2C8qIvYKfuuar9rQ2RhmnNX_syHkgvhay68AzJZ24LpRQhuo7G1NcYYfdp86gCX0y9DNy15zFG6rJvk9xNZJijIkRfzC7KHlruvyZdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🟥
🤩
خداحافظی امید عالیشاه با هواداران پس از 13 سال حضور در پرسپولیس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/Futball180TV/102473" target="_blank">📅 23:50 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102472">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OYMY_npcHC27ZR1mbnaIoDetbNK691Dni1nICiwb4QbGg-moErDachdvtdJV90vFMr3j_XjKRDOuYaZZJg9Strk8XqyY9xO4PWAlQ24BOXox8fAk7KATvL6NeSRmcLt1_iPTK6GNF_dxB8pFOEylCo2-1FEOtREdx4wTUWk5UYpf-dIksvc4PdcWo3fToLGIw9mxqV6RnnhDkUCMgBFbWzIClBMIsM7nO3MLpnu0ZNWkBJWWHiHSh4OpFFW7TWAKNjj_361zT5yVPleZcSueRVInDyz-TQq4ax67rrYdF8qYOFOJyQHFQ8SgONgRIT7fPKPKX-tsi1tpnLswLHiZpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟣
مسی و کاسمیرو تو تمرینات اینترمیامی.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/Futball180TV/102472" target="_blank">📅 23:21 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102471">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/26c665525c.mp4?token=BQsn3z5YJg5qOtHNPHWkpJgr40AlilwKMHnEXX6owxl0Wa4DjP1eKfaJ5VJaTMWDna-EYJ-iujms8cihJcKqZGcsf_XFBTwYBTWy4epDJI_Dbg_Zy6XsJf05IZSZUPZfPy3akvq8e8JXQQdFLzDk4VpjGqwHhaco75IoOHerwTgscxdHHV8siSCmpsZqwv9EihhSgfqGvWYJqIzHK_eJNjedOb_iQ1T2iwBVHIPDTkmjvFQJTwrN1tJ1Mf49z_smwP4vDOyLx5EptTEwDUEzwhoVGMN9TqHeFJY4NCK3V6WfPkUC5rooVoqjuFaqpTmRhNGzRktAVXIL7ohEOG0oQQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/26c665525c.mp4?token=BQsn3z5YJg5qOtHNPHWkpJgr40AlilwKMHnEXX6owxl0Wa4DjP1eKfaJ5VJaTMWDna-EYJ-iujms8cihJcKqZGcsf_XFBTwYBTWy4epDJI_Dbg_Zy6XsJf05IZSZUPZfPy3akvq8e8JXQQdFLzDk4VpjGqwHhaco75IoOHerwTgscxdHHV8siSCmpsZqwv9EihhSgfqGvWYJqIzHK_eJNjedOb_iQ1T2iwBVHIPDTkmjvFQJTwrN1tJ1Mf49z_smwP4vDOyLx5EptTEwDUEzwhoVGMN9TqHeFJY4NCK3V6WfPkUC5rooVoqjuFaqpTmRhNGzRktAVXIL7ohEOG0oQQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">همین ووزینیا که تو جام‌جهانی تک تک تیما رو سرویس کرده بود، جلوی علی علیپور اینجوری فحش خورد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/Futball180TV/102471" target="_blank">📅 22:50 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102470">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vtvBjDgbRoJAy7FsvLzBqKBIRZABnggEdppkgmKFJFnbfNgu1hh0rVj2Bw84y2NGhoH4Lr_lqSi5_h-TaSvCD1eUHFzxZYAJOh3fvYqCkC1-cr9sOXrVukNAycoTNYoex8g38WXHt-F4uacldeB11Y9maNYaIhD53l4hzz1DZHN-PyvgYjEw4OuF41ckPx8-RFKvrG2SgVvwFnbQKfd2lnpJIr5A72hlcLXIgjQZxN_-XeZNY6K9IW254YFQ6K10Z1uvCaNXGYyhKfqldFIsd8fQhJ4CibwV7So11mdd76C6I0_hn_bj5XLnOOEeEDhkoNekVCwpE0cSRW7XjvnSIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ار‌ام‌سی:
مندی تو وضعیت مالی بدی قرار گرفته در حدی‌ که مدال و کاپ جام جهانی خودشو 54 هزار یورو فروخته.
😞
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/Futball180TV/102470" target="_blank">📅 22:38 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102469">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/261dc7eb19.mp4?token=V-1n8XsL_AqY7QcFAa9pgA7wEXxSwsFYA23PrsdvLPucBVKDc7GxJlJaxKqkHoxL73-Dd_K38UZ0p73JFm6m2DL9XNOwOV9jVMaz4qmDe91zd9wDUhtV9maFrYGoCFkrIur-qWSyW7mCvLiCWVqZ6asFnLZ8EOTVu1i_JcuVjFnm4u5lsgD9_g2lAJuCbwo7smS2Por3LhRRwEG-82wk9bHJy_OE_eF_jE2wEh9hCNaYJEvpC7DFdY5ovD9zhpm3mRDaWm24tciRooD8_Nk3dy5kxgFLRQ59JPxJcfWbDME-g2SAGGryZRHaJt_lUqnOGxSRdNFwHUH3uXGXkhOv7A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/261dc7eb19.mp4?token=V-1n8XsL_AqY7QcFAa9pgA7wEXxSwsFYA23PrsdvLPucBVKDc7GxJlJaxKqkHoxL73-Dd_K38UZ0p73JFm6m2DL9XNOwOV9jVMaz4qmDe91zd9wDUhtV9maFrYGoCFkrIur-qWSyW7mCvLiCWVqZ6asFnLZ8EOTVu1i_JcuVjFnm4u5lsgD9_g2lAJuCbwo7smS2Por3LhRRwEG-82wk9bHJy_OE_eF_jE2wEh9hCNaYJEvpC7DFdY5ovD9zhpm3mRDaWm24tciRooD8_Nk3dy5kxgFLRQ59JPxJcfWbDME-g2SAGGryZRHaJt_lUqnOGxSRdNFwHUH3uXGXkhOv7A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
👀
تام هالند یک‌بار به ارلینگ هالند دایرکت داد و از او خواست به تاتنهام بیاید، اما ارلینگ اصلاً متوجه نشد فرستنده، بازیگر اسپایدرمن است. بعد از اینکه ماجرا جنجالی شد، هالند برای تام پیام فرستاد و توضیح داد هیچ قصدی برای بی‌احترامی نداشته و فقط او را نشناخته بود.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/Futball180TV/102469" target="_blank">📅 22:00 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102468">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IjJAhr05LZaBk5oKwHpp0bYN_dHbNaQyz8XmxlLVGX328HrqaglR5RPL-T0Ii1Fe5zDL2ajJmK0qiNbddeqGS1bAbb-2n0pFHhEAXp_8x0G9HnhSV_biaUkHZ_c0xk8NnXngSP8aIw715IEj13cboQhX6uc8F18n_pq6M8XfenGsVVJPOOuSj-Y8Z5prfIfIrGN9-KexbzefKLZ9QEBPq8cTmFr1xYJlSPLW_ecsjakNTe3mZ2smpiSS48QpojggfQ7Ep1niN3ERQuWm3mNXiJHJPFkXNpH7fqUlBe6hdMIhO6bYRdJLaHQGV5DrDOlVaLzPSfmazYDCsGaEkEpLpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
💣
بمب لاپورتا ترکید:
جسی بیسیوو، وینگر بلژیکی کلوب بروژ،
به بارسلونا پیوست.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/Futball180TV/102468" target="_blank">📅 21:55 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102467">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BHDnfLXGtouDvPMFsCjcB483Dh98Iy9YhSyyZLR6KsbFU074sb-2tx_5hKqpcqnCubPnMOQaD_Q7ih2dx_tV_FXSLp7TpC497he3nOFEuvj9foTQMUuu2mxHFo_uj2yHlKF4tPFe5wCzi07qv99ggyyPM-C0f2BG2Tn66gAotAbKmGT2t2J5vKGh9G-nXc3_yRy23wjvdffnLBfAbaYx7js9MSuUDneeIath6sQHSYLpFV18oTP0gizAi16z-sVJgUoZxp6KMm6Y0UHRSPLZmvbWB2SissxoI_n3JetetoyUGRk3E61v8VcmFaIPNnyMkeRBA_ciZt4EQ6q_ZGszzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
ترکیب امشب بارسلونا در بازی دوستانه مقابل بیرمنگام‌سیتی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/Futball180TV/102467" target="_blank">📅 21:54 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102466">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/72f4d6d3d7.mp4?token=NCXpSSyqmadvMi0cW2Q7WIuB3Y3iTUuks60nObNGlneMgUo96J575c8KoT91WBtmsIwk5c3WF6ex8JVXcCyOL40bvRVm0281L4wppOXSdBLAF1UXwsd-04kBvXMTHZds_-lxfDpRvHuGYxCRned5LtLRlHn1tITisQkMs8-8OucIjB-AmSTbuSd9frxSRZbgT2BeEfIGBCW5CVIgp6dkKGqXAfLRYuhyKrVC5-a6wYglNIL2NnlV2EcYC7zB7FsU7Vy3qHkdzkdOtWGfxJNd1kUu_E5bUbTf8OQqMiC7C0HdAJWbToz76GqepeP1Zpq6rCmYnaIzgSZ3L0yvoJ48ZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/72f4d6d3d7.mp4?token=NCXpSSyqmadvMi0cW2Q7WIuB3Y3iTUuks60nObNGlneMgUo96J575c8KoT91WBtmsIwk5c3WF6ex8JVXcCyOL40bvRVm0281L4wppOXSdBLAF1UXwsd-04kBvXMTHZds_-lxfDpRvHuGYxCRned5LtLRlHn1tITisQkMs8-8OucIjB-AmSTbuSd9frxSRZbgT2BeEfIGBCW5CVIgp6dkKGqXAfLRYuhyKrVC5-a6wYglNIL2NnlV2EcYC7zB7FsU7Vy3qHkdzkdOtWGfxJNd1kUu_E5bUbTf8OQqMiC7C0HdAJWbToz76GqepeP1Zpq6rCmYnaIzgSZ3L0yvoJ48ZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
🔹
وقتی منچسترسیتی حریف پیکان نشد! سال ۲۰۰۲ پیکان با سرمربی‌گری ذوالفقارنسب برای آمادگی در رقابت‌های لیگ برتر، یک اردو در انگلیس برگزار کرد که در بازی دوستانه مقابل منچسترسیتی موفق به توقف این تیم شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/Futball180TV/102466" target="_blank">📅 21:40 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102465">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1bcb0e2d66.mp4?token=T32AzjsmXtIgJ8KmTfiibuVTZF756e8N-_zwYdNNsGLRGfZrw2o2xYXVhdZHukx6zEyMHEBFxOcXsdz8ceibqz-nex4ChunDT1pzkrQwafXcC9KAVrcGN7ncNzqJQGUq92tPIlZ9TFQZSvol72PIIsm7a-uS3anMPBraIJf2pxNJhM1V-0DEW2Uftzgr7CI9mQjl80gk6KFoDMgs_vs20BT76OIR74Chj-_7xLKaDSdBMDEeExgH0BkWnAbUH92V7nqmaDPzVYTwGoT-avEbKztHIeI-t1pO7mA34H4D1APtO7oQU_6W4UF0j9hjEyzlUEXEauR82PSXKznL8btHLw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1bcb0e2d66.mp4?token=T32AzjsmXtIgJ8KmTfiibuVTZF756e8N-_zwYdNNsGLRGfZrw2o2xYXVhdZHukx6zEyMHEBFxOcXsdz8ceibqz-nex4ChunDT1pzkrQwafXcC9KAVrcGN7ncNzqJQGUq92tPIlZ9TFQZSvol72PIIsm7a-uS3anMPBraIJf2pxNJhM1V-0DEW2Uftzgr7CI9mQjl80gk6KFoDMgs_vs20BT76OIR74Chj-_7xLKaDSdBMDEeExgH0BkWnAbUH92V7nqmaDPzVYTwGoT-avEbKztHIeI-t1pO7mA34H4D1APtO7oQU_6W4UF0j9hjEyzlUEXEauR82PSXKznL8btHLw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
⚪️
رونالدو چرا رئال رو ترک کرد؟ شرح ماجرای جدایی اسطوره فوتبال از زبان خودش.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/Futball180TV/102465" target="_blank">📅 21:20 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102464">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/00ed94c011.mp4?token=VaPLf3l2kT9NKdhjeu12yI3O5htzcTxua8H-qOCinTNanPl9F8_sDUp6uAo7KuC3-3VMwgUCg7Nr-tpeuIxu8h9IoBTFMyD7qqhjO64ma4I393jm2LHCgsT_VLRu0o6Jdv5bug1VXKCl7EXtfEqTimPRQ08uPXCS3z06c-YP7ZSULeG71eHi6ltJFHDV3IKTjbe_yIHJsAIlB3UUmRjaukJHrATYJpBsi75pdpb0G91qxAQ7gepUhQ9HItroSB5OIWKp9PaVynToL6VfLOxqSSYHDy6aoe83hwBrNZovIXzR0ftLNbKd2Rhc5q-2Ya9nH6uEtqOQgCw-1648Otb-qA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/00ed94c011.mp4?token=VaPLf3l2kT9NKdhjeu12yI3O5htzcTxua8H-qOCinTNanPl9F8_sDUp6uAo7KuC3-3VMwgUCg7Nr-tpeuIxu8h9IoBTFMyD7qqhjO64ma4I393jm2LHCgsT_VLRu0o6Jdv5bug1VXKCl7EXtfEqTimPRQ08uPXCS3z06c-YP7ZSULeG71eHi6ltJFHDV3IKTjbe_yIHJsAIlB3UUmRjaukJHrATYJpBsi75pdpb0G91qxAQ7gepUhQ9HItroSB5OIWKp9PaVynToL6VfLOxqSSYHDy6aoe83hwBrNZovIXzR0ftLNbKd2Rhc5q-2Ya9nH6uEtqOQgCw-1648Otb-qA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
یک تازه داماد پرسپولیس را حذف کرد!
از ماه عسل برگشته بود و چهار ماه حتی توپ به پاهاش نخورده بود!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/Futball180TV/102464" target="_blank">📅 21:02 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102462">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🚨
🔵
🟠
استقلال در نیمه‌اول مقابل فولاد با تک‌گل ابوالفضل رزاق‌پور شکست خورد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/Futball180TV/102462" target="_blank">📅 20:54 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102461">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8f8b6948d3.mp4?token=FJjh-TZXDgnf3E5VYZbRvSXsl63DboUaVzRP6v6Wh75ES1Ff_8N88r7Aw9R8fZwwMUtOmwvwe6onb16eDZdNs70d_6mQQPzq2JXnTE5CX9DSWL1pgMFdTFN4lgZBSySOyetjXvCooZfviB1fSky02mUVV5rUzSTTQyVl02p3EzH_XrIxABhgCzI2uCQNLvf7pVKZdjwmZcpe6LixHIHuWkVIPPHG_wDDnjG3mew_-TGzxtrKEOkrYiYtyvMIYWkBP_vWv5W66GP2FTMVNTMqr_7V4cn9dlcjrNvU5g2sa6mb8Jsm8TsPAStlIroctrcTh8GpFU_HMeTC0bZLrma5GA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8f8b6948d3.mp4?token=FJjh-TZXDgnf3E5VYZbRvSXsl63DboUaVzRP6v6Wh75ES1Ff_8N88r7Aw9R8fZwwMUtOmwvwe6onb16eDZdNs70d_6mQQPzq2JXnTE5CX9DSWL1pgMFdTFN4lgZBSySOyetjXvCooZfviB1fSky02mUVV5rUzSTTQyVl02p3EzH_XrIxABhgCzI2uCQNLvf7pVKZdjwmZcpe6LixHIHuWkVIPPHG_wDDnjG3mew_-TGzxtrKEOkrYiYtyvMIYWkBP_vWv5W66GP2FTMVNTMqr_7V4cn9dlcjrNvU5g2sa6mb8Jsm8TsPAStlIroctrcTh8GpFU_HMeTC0bZLrma5GA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شزنی جنس رسیده بهش و مشغول دلقک‌بازی تو تمرین بارساست.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/Futball180TV/102461" target="_blank">📅 20:50 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102460">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ace3163b65.mp4?token=tgSDTrUn6R3D9BeGCHW1lFzyWUgh-hPKlwxh25tpNDXUho12_a5xhoUFAiFCT3TG4vprB-eNoiJeKsMeC2myToABXPpKS8RjrdiqyCrOgAizW3t7G7OxORK134_4UzCdp_3RE6629A2-jcS6Q3SzY02UEa0Bu3wq-53dAIJJuObhdxOhNZ_E0ffUgmcGIELUn3PRx4E2Gkp3U3l1O9JFF7yYR3TdpxhFtclbHd9K2KoyHxpEr1SfCZz3eqqH2d7z7Q5CbdWetz9-JA3Ho2coxWZb_9mdmK0pCAITgIeWB2PQ8gxRn-Xg69xqu8VFlXjn6FBdhtITDwXk_DOdYIRuYw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ace3163b65.mp4?token=tgSDTrUn6R3D9BeGCHW1lFzyWUgh-hPKlwxh25tpNDXUho12_a5xhoUFAiFCT3TG4vprB-eNoiJeKsMeC2myToABXPpKS8RjrdiqyCrOgAizW3t7G7OxORK134_4UzCdp_3RE6629A2-jcS6Q3SzY02UEa0Bu3wq-53dAIJJuObhdxOhNZ_E0ffUgmcGIELUn3PRx4E2Gkp3U3l1O9JFF7yYR3TdpxhFtclbHd9K2KoyHxpEr1SfCZz3eqqH2d7z7Q5CbdWetz9-JA3Ho2coxWZb_9mdmK0pCAITgIeWB2PQ8gxRn-Xg69xqu8VFlXjn6FBdhtITDwXk_DOdYIRuYw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
کول پالمر:
برای بازی مکزیک - انگلیس بیدار موندم، ولی بین دو نیمه خوابم برد!
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/Futball180TV/102460" target="_blank">📅 20:40 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102459">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VhtgBuSIVtECjWBENH7A2P_QF9ZTv2zzfC_ePoOR3zayZBlpak5o-kPqYxdYgMVp7_veupnruqgUugWyGBoWTXDJzgzIzKYJS6NqxdaSnghR8MTM7hN1vGRnZBgcYHKf5_d4Y8U3eXQWfo4OhilodFvs11p-vsyE3KphQA9zEYkA10hc-0D5kDeZfGFVHwiuFnunDrU-BoYcxaSmVDYir_kOmTESPxbLX2c3kBXqTBbFjruauuEGdtbOUV-F4F_QslPQKI4cSyDzOcnKg7C42iYwSw6LTmxL38RpagxcasSDKH3dWInrY6AmbLVB8nf0vVIv6YviSTVevCW4EU6jig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
⚽️
دیوید گرافسون دبیرکل فیفا تصمیم گرفته که علیه اینفانتینو کودتا کند تا وی از سمتش برکنار شود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/102459" target="_blank">📅 20:32 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102458">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/opCd1VFSW15xEgcBW6YJbJknArSUXy7EfzriyoZgcGHCxAAQyDLN5fmTOWq7XP_eYopItp4D2hBMp6f3CisT8MZXN8p95nY6JwYDdUYovURFgiP1zeuif_pj1lMr4mGlTgEqMhzLZlmZx-Zc8smhmwRcS5rpNgQT9rQJxRh180RD3mAVXATLwtC9wid0TQmRdkinHPIjuD17_o-_8uSCj_nKM_wSYljcYPoG9Tz2FTC-HRs0_T9oBksJuXC6Lw0YQp2t4i3NkNesZ1EswVBo9x9ztUdWZCdTnmp4Xur-0ZagijAVT7bAd2Tx3P-ajz5X83zsez9-fx8pIOw2C7ErOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
📊
فقط سه بازیکن توی ۱۰ فصل اخیر تونستن در ۵ لیگ معتبر اروپا هم بیش از ۲۰۰ گل بزنن و هم حداقل ۵۰ پاس گل ثبت کنن:
😀
محمد صلاح
🇫🇷
کیلیان امباپه
🏴󠁧󠁢󠁥󠁮󠁧󠁿
هری کین
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/Futball180TV/102458" target="_blank">📅 20:20 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102457">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A4HqdcUXfQm1v0M5NiPy9CDp9c4bkVvrYhaKqcrPOcD38jMrt1me9sOF7dBVQp-gVmGhorfVCZeqMkNzgxZ1Nl2-GnecM9lU-EEqe1v1qimldDYj5WUCLpYyxJ3rihSPIcF7lZoU9SLlGw5OYVWBX5i_Jy-7BXXN4Kqnfw7qN39qVGKoOn_SVbtkkDni0z921Enw9ooGrm1Js1Pa6cDyMFcEpAsq4GxhsHt49IsOXSizHgNTWN1Cm8Xh0n-mOzlYirBq6a6RAomLVQn91FBa4jH66VW4BSLqJ8LYt-vneeCrtGbukI0pYfzqZ1XEQHvFYK_EwfLO-QbZTcKej_OG4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
⚽️
دیوید گرافسون دبیرکل فیفا تصمیم گرفته که علیه اینفانتینو کودتا کند تا وی از سمتش برکنار شود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/Futball180TV/102457" target="_blank">📅 20:15 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102456">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🚨
🔵
🟠
استقلال در نیمه‌اول مقابل فولاد با تک‌گل ابوالفضل رزاق‌پور شکست خورد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/Futball180TV/102456" target="_blank">📅 20:01 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102455">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q1OiiTiAzpQE9z4tIIarAGBsZLubtLzpzz_gtv6oPhGkCN4pEZH3PD6MYw4nVFqPiQ3p5VXqWuMJdcYxcqdVeX0hD-mP9FLqrJSHep6qfCIRoIWKtEZfTkusblUSmSiAdQF9om7Pnq61dFKGbkjjL3aQdLPqzlf6P6eAzqIoWqAWlilqGa5c_cETZh0z5EwT4YDPUjSwB_mcrt6Db0WTWncBXqOsKdWy84KqeTxYlwy1EhXzaGBj9ROE4xqgw9S1Fkc4gVuAfPQTrJc_byNajYQoEG633bfSpI58-6crbxvpCIfTEl5liTYoZ7ju5o41J2bROz5kQgTfPP-HNoIFHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
🟠
استقلال در نیمه‌اول مقابل فولاد با تک‌گل ابوالفضل رزاق‌پور شکست خورد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/Futball180TV/102455" target="_blank">📅 19:52 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102454">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fq-0VXPVp2KNEzL2HBUrLP5QK-RWmC5B5AWV67s6rePpeAuMDO3pDexGxT3kXxFJ2WvCMEe9zsZt5UiIh1POgp8I2Pl_fegZW0AecYlS26chqSGCM5x7Qy6YvyOZnc3ZMTX_TeOziMfnQu4rQSv3CJ7KEajbG9Hb6hTfSMOZYtz46tYlPajU4HwEIiiOwBRkHLRtaljtxdFbMqFV7m8w82gDr8qyrPCxMRoVEhsu1T4rCZeYwx75CwdwPvwOVJq4DdWeoIq_nAnEmT5_bXNcwKI_zukk_980cbJ-N9Ww-i5DBqh6ZsfysMB4S9mfj3dQCfONk3jQPti54Z16PrIFUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
🇯🇲
وینی و عشقش تو تعطیلات در جامائیکا.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/Futball180TV/102454" target="_blank">📅 19:52 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102453">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🚨
🚨
🚨
📹
🔵
🟠
پخش زنده بازی دوستانه استقلال و فولاد ساعت 17:30 از لینک زیر
👇
https://t.me/+E5pLb4kNVJZiOGI8</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/Futball180TV/102453" target="_blank">📅 19:50 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102452">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">کاسمیرو به همراه خونواده که دیروز به این شکل بعد از معارفه عکس دست‌جمعی گرفتن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/Futball180TV/102452" target="_blank">📅 19:40 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102451">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PNG5RdvSPi8u1ASpS3YfgBHZFBwKhILKWZ2pD9_iuzFQhTwVY2lsIiXUX2F5HOtr5fUQpz72k2C4LoyYQELL_AT8-3DjxybKxUvMncYkGGmWWj4B0emGgBQ5Lv9Nt65s8xNJKFB-W7HYITVG4hEPD_y2UjFJK74N6wYmwoE0sadFvosPu5IbfNxbja-JPjtEiGFHLlJuoxYr-eYCeekUDwx2arLPR1vW2noP1MSfG0g0yfp69c7SIPlZxXJQz-j-_F2ag3INGxMy0rhFA_ZKnrxypUK7XJpXbA5zCxIuy5tr2xHJt-o_s53XqgiU7Q_oezwGhUlS_xyr66-rsF_Ejg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
❌
🇪🇸
رسانه ESPN برزیل: رئال‌مادرید هیچگونه افزایش مبلغی در پیشنهاد تمدید قرارداد به وینیسیوس ارائه نمی‌دهد و پیشنهاد فعلی همان آخرین پیشنهاد تمدید قرارداد است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/Futball180TV/102451" target="_blank">📅 19:24 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102450">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AEAyZD0fMXqr9TqhztnbA_tpX9MNbRDl4B7a2Rd4cIMazhFVCZZeCM3nqzBykjg1KjfjZXAOVycjuavd0FVe0O1y6LCkYFf-hXsQGUSxiCk4gk8d_1e1-CCwVK9OQAv7ayy_bbGcY-9k08CAeU9RcoLm2Gjh_6e3Y3FFcO243meLaYLkpwMsqcSLEZvqcxpsQZ9zMnHslpf5_zPn2B7yO9KVvqoZNRZr-HEUSS6D7b3jsgjVx5BrsAN4tmo8xQl2cvmT1XHmkcmBQhPEGUDzecao6eBRvIcoqOgvADfATzvA3ixHuXjVOnsE0x9R9lDAq2YJPkMWD371CBANiju8nA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🎙
🏆
اینفانتینو: جام‌جهانی ۲۰۳۰ بهترین دوره از تاریخ این مسابقات خواهد بود چون در کشور زیبای مراکش برگزار می‌شود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/Futball180TV/102450" target="_blank">📅 19:21 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102449">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RBRzI5io77aSJ4atP-ROH80g7vDE7PCdw4DlAsAhThWrDG0kGViyC3GrMl9kEP14G0IWoLg7RSds1spO33gz8ulsihmXyOAaqIbEa1K9yUmSQrlu5G0BeBh5mKmoVt9jQDfbuBWuvzaCXgbXMw-etB0W_nCpUjpDsqzcFXsSkfkTij4mTF6f766FXRoaAfEwT3TqTaOhI7NANr2YOjmjKIFDghXxtTzFGizBXNKR0bW8ZnoCInB8knIV23RzTK868XJaereWYUs9u_PbTp_uDC_4cyHQDHeqi8y5N06EPe_HEsviiNaTL8pvWoRXcbuLlGK6KFba6-nqeg9F2H1woA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نیوفیس تعدادی از بازیکنای فوتبال
👀
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/Futball180TV/102449" target="_blank">📅 19:20 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102448">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b0Qe0UW7ry8ViU6hKg0Y_BUKAkXxPU0dNEJ9l96vyu0ouQe7I8ErWwNh2IVZoXNWqiNRxWThAluM9KCh3FO4YHJszGhOXjFvI116wKFajjYer5rtbGkrXiBDC0Q_SyBI8fNmq6Rq7_xw_rqPrHm64FOej-LD8g-nQnrNpoAT9N_JoB4sYul__B9mcQYTIrOUvykiXt3k9Kf9WXBovdQuDpu6MGkOL5OBJ5ylSbyn0S2oSr3Od4N0ppgk_WhwY0ejVC-ViFlFI77e-q8QhbrZMCN25QinOOmfaPHxCB-rCEhlgL3liYlcsSCucJhRT_SINNorEBWKx0DJwDsL0Hms7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
⚪️
اسپی:
انتقالم به مادرید خیلی یهویی اتفاق افتاد و همه چیز خیلی سریع انجام شد، رویایی بود.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/Futball180TV/102448" target="_blank">📅 19:06 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102444">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/m8qIWCyleJRdKB6tVvTkOa41IbCNeJ7pby18dqoEKVs-esrrPGOrCIuPvzFNnIesC9CZDO6DbM70DzI5rSYmQ5DEA2FhJdakSHDMP2hjwVkYN5JuMdAiGj7_1UJC-KUJ5N9VImplYPjUVga64RzqtMzAisSaqX6kpKX9kXVBJETDfq4wqy_B3U8MQvCB8PaE9z2E9M46JmACF0grULJH-UQ3-Q35tiP3-Ey1OpXo075ecScTkr1SSV6LDit4S55y6bjFy0NMWmdgzZvKDiLfO5lWS1Sf8xulxYFEOgFmpK2lRvuaLsbBxnSWMuWKFgdAilxAsnfmh8MlLx8WZTYIpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DMD8yaGqew2kE9jSfsGhMZM3BuOmACOVKG7L5pOvhvQayhPeh7Bo038gH7qotcWRuWCGfr-2CgJY_3XK0utqYuEQigsYyObwc-Jq-GjvJTej3bBARPLUxSb7HBzYPS0GNM18apZuEkr69siC-QxxRnue5JngnrYgv8op3kzuLPY1K9e-9oexL5hafNcLSmoEFAP5Mzz5doAkuR-VWahJfaIH8ly6zxuZGFpPtHKV_mpVLI4Db7jsj8yfNqxVT7vRCilYe2P9swevcHzXKKhYd5iPIaiU9kzt0SzRIy99LX4lX4JHT5USOdj8aJzl1o0ia91tP-RdooYXJ7_4Sf0l3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KTcvSAD8FEF9bd36t-v2h-jYCEjvqARmEH6fCILiuiyiwepIbrmtB5IxzQPlFTa3ogsaCB4dWOqnQpPepITVZJ8tLFEVtFFW3HBRIUq6W3hctzIWqBtZIJD1xLTnvEFlPegMWHThjZJ9UqS8vgFhGUeoI06f-2GHwqU6KHgVgXaY3JeCc0Xt_gxOHRO-x27oh0B5qEyPKQQ0aawWHRNbo57vtxFkw5ll10J2DrXo9L5SXPMPzJqoAePyrkTbNK57NRcMPQ5gucq_UndZ8M24NpPrTg3az8Bpqiiucfagr7jYCui-hEfakvK3Nz1FtN2ZQFiJX7hT1exN_vSwxW5EVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vFSJi6921B9EfUAfWDcGskbw15JcMCFEVjFKEdMpCd6MYh0RCjUsjB7NmNMe7EsndHg-6SgSqzZqMkfCQv_0ywAcVtTuBz4GOUEoUptz1wc6GRe1514zdvTHkOh4Kk8Q_Kj4mfaJnVx7GMsWux5GrOrYljJUkja1UAoO_Jxznys02S5I8H08LW9lS8G4_0EQfCOZDgPM1EVJQNjMA9r5aeTU_0c6_OvzSWx48JO82VFiU4LMUYYpRfa1gThmmsDNyAfwuRrO4XePkptt6SVR09yPGeDOn_pxXITaZdfK-jRydunkBVllOYG02gbR7jwoy3ImewDD6AJ_HRnn5DRIrw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👀
عشق و حال لامین یامال با دوست دخترش اینس گارسیا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/Futball180TV/102444" target="_blank">📅 19:01 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102443">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fbFwt3Cx86RuRJocw5Fk-gmShKIordBCWxMlID6MoD2qbMOtb25iLJm2A7Wl9zFsK3ZPHTCJRwSyh1it4qpzzR2Z3RslW7rNKmYp4gNTR4i3kOxBzKHSxz36Q7IGLY5tIVGOF3OsCCQu44q29KiXGjR_Y1P_Z4Z7S2kUOMDy-NX1c26IqVaA_uDmnAe2bz7WQQtUfdjqVoToYaRDf5Z9D_NNM9qiMnTFkQQHg_bCRLJRRKohXaPruKoonwRZED0Wuw8E1Uu1Q6V_fuME_XI-sYDmefxjXD7Yj5Dlb6skMjEfS52JAQ6h5UOvY-0exyygncqYFtpGj4qqmCfw_HDSfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بازی دوستانه مقابل فولاد</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/Futball180TV/102443" target="_blank">📅 19:01 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102442">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DCtdyR1eJUsR55mnjVKZ6tu1yuZadyRUkYSr9Pl22TAgDoxR0rtLBMsWneM4_8LjXWV4k928JSBhznZcNfCw0tuPWZTvWGbeJ62_p3lkyRGIukGRiwiFKqn_c02HzJorIiT0XsSaXvUsbgfNvWOlSUfZqErqbX4ETOa9F5IrL0fLT5yD7J_PO_WzTLWtFCVovD13qKfKlU9QxrK0Friaic9JTh1A7CJVi-TgKALP2kJl6Tr8_6RU5qfNHz3pTCwmaSZ229PbqaspvkcThgPaULG4gfNeT0Act1KDv4I5U5v8xYjo21L-OIlxO3J-ZR2Eii2BSO0a-myCD-HXfpEg6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
فوووووری محرومیت دوپینگ میخائیلو مودریک لغو شد و او به زودی به اردوی چلسی در هنگ کنگ ملحق میشه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/Futball180TV/102442" target="_blank">📅 18:58 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102440">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CXy46wjlBCZW5XWbfkfIgxKzYS_A9ZBhdQNQVtEtqc_u5X0YyOVDhtDrVFbMEP93hcs6iJ3QVdOracJDaijEWWGpsPiL7DaJ3I2OpIlVw7C-wNvK-OJTiyxWEzd9IARVtyf-59OzLa-rHmDTOzSIYM3xDN1tjrfXnnUgREF1cPnITRJHcUG_oCCZlOEaVOVOan8imrZmSpboM3pCbF0f1Y-MAoe5i9KcY1zerC84HJAp9J3J0rSY0YBgY1uIjo62wFBBZzw6huqVmBrEtpfjfkn-ip5rPC-0O2m9ynZEPtHm2iz-GT9TYx71OwB92rlt6ZDTE1JTUUCepCvURDDZfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LZOZe9Bj0JJqMMP-dcIZgX90hUcYJnhItivAsXUOG8Q9-aEgomuEA8DNIdekng6XOU4zN4O8jAA83QnJ09V2Fva_RFNHPtfQPQYFu7wyYT2KV5hPBz2f0F-BCUVnMHz2SNacT90rsAVvoTNeGKRUvvsgijEWdO-jBLSZJXO7nSq1o5iMjUI1b8nLcQy3M1mZAGe_f2L6Vw3ltS10B-BmJuA6WNNGZqo7iVx0wwhxNHp6L0qNx2r0KC1ry86f3npzGe1kmewaOfvTCY6UkzZNfP1I-9m-Ynlcm3O1CanYSnq5foJyczi3SFj1v0F4mh9C_tppiwiVSYiQVzstkSu7Uw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">پیر شدیم و خودمون خبر نداریم..
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/102440" target="_blank">📅 18:40 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102439">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c5d65b7222.mp4?token=NL_bosH61kRC2OliQOKGXbnz_xk0GVXwl9yJ9NrbBPlhsmBQmC-hItNhSEYs2tuEbzADxJ1uBF12f0Ou7qJ2yjglFsKD64XkqBRABV6jgaY88yh8F_myjzaj2deIC9SoHp_qqT6eMvXNHXViVA-4pEA4EPaP300M5ypiykZVAkgxAuCkADlmWFRy9sQadwi0hNPIrpGTDCywg1p5YPjl8rdw3WAgauf1u7dj7MpR-tvaw74Zf8MrDrW0plLXtAPEupRDGdCtN1NqBvpGsXT3kakoiywEUKRq-KXFhH6FSxEieuUZhPJqLm8mxfeeXxk7OvzrGn__xn3nVPMLX1wyPh8r4xAJdRv6LmdRz7MPBn-JNX4Kk3r2BrYO3PhXxqXv4iTdtph2OkgmHJ2UUdN4pDGBpOb4VjvmFvhHHMEXjh4xPlEHWZ_O4frcW1ahniYC0nPFaoxWuXo3t6y5ECz-sb5p21AXoX-n4EH-DcAm-ZktPnAVDtBYpZEMw0AvoWPL0HgIzg50fCRZH3dvpigRAXvcC7-HZJoMIBhat4i4or-JBUnLj_dchf-Vl0Esn2Y4FvfhPTaEMNdRiMNsCN5wEopZ0BMVQ83-T-7gYN4wjnNG0UQiE9r1d083xRg4o4sYMmUzWpVUZUSJb_A0JwJphks_uHjaIzxGvH74GMsU1ac" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c5d65b7222.mp4?token=NL_bosH61kRC2OliQOKGXbnz_xk0GVXwl9yJ9NrbBPlhsmBQmC-hItNhSEYs2tuEbzADxJ1uBF12f0Ou7qJ2yjglFsKD64XkqBRABV6jgaY88yh8F_myjzaj2deIC9SoHp_qqT6eMvXNHXViVA-4pEA4EPaP300M5ypiykZVAkgxAuCkADlmWFRy9sQadwi0hNPIrpGTDCywg1p5YPjl8rdw3WAgauf1u7dj7MpR-tvaw74Zf8MrDrW0plLXtAPEupRDGdCtN1NqBvpGsXT3kakoiywEUKRq-KXFhH6FSxEieuUZhPJqLm8mxfeeXxk7OvzrGn__xn3nVPMLX1wyPh8r4xAJdRv6LmdRz7MPBn-JNX4Kk3r2BrYO3PhXxqXv4iTdtph2OkgmHJ2UUdN4pDGBpOb4VjvmFvhHHMEXjh4xPlEHWZ_O4frcW1ahniYC0nPFaoxWuXo3t6y5ECz-sb5p21AXoX-n4EH-DcAm-ZktPnAVDtBYpZEMw0AvoWPL0HgIzg50fCRZH3dvpigRAXvcC7-HZJoMIBhat4i4or-JBUnLj_dchf-Vl0Esn2Y4FvfhPTaEMNdRiMNsCN5wEopZ0BMVQ83-T-7gYN4wjnNG0UQiE9r1d083xRg4o4sYMmUzWpVUZUSJb_A0JwJphks_uHjaIzxGvH74GMsU1ac" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
چند تا از شوت های کارلوس رو ببینید، زمانی که فوتبال تا این حد راجب کسب و کار و پول نبود.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/Futball180TV/102439" target="_blank">📅 18:20 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102438">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1d5590fc67.mp4?token=TRXIgd-08Rzw89z1UHaBUtyqdmlcH4gK8I5FWDKYZCCzgatJ-jTCG_Pt-3Bdw5CyIBGHxLJw5jhz8IT07l72f-VCIMffPxVRWG0w3SdcP5jJftKnAY0iK-Gm2WbzDkcSLCvD7Jw1dEnCnU6mF_rue9V-7sFtRSNEy1zfstVZ_XJydbRRedkkLjFcTxmtHZyj78N_-fsrVU3eB4jGBKyM3nGvK2aEK_L6ghRKDRdoQ4XyB_t2GngZqm22QsxFWqJTQyYjFMyznccV035t00EGfh3Ac-YHaEYjueZrnGeOeSVMHwCCoAa1L_Em1r8FSbal-f8Rqj371BrB66JTzHlKgA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1d5590fc67.mp4?token=TRXIgd-08Rzw89z1UHaBUtyqdmlcH4gK8I5FWDKYZCCzgatJ-jTCG_Pt-3Bdw5CyIBGHxLJw5jhz8IT07l72f-VCIMffPxVRWG0w3SdcP5jJftKnAY0iK-Gm2WbzDkcSLCvD7Jw1dEnCnU6mF_rue9V-7sFtRSNEy1zfstVZ_XJydbRRedkkLjFcTxmtHZyj78N_-fsrVU3eB4jGBKyM3nGvK2aEK_L6ghRKDRdoQ4XyB_t2GngZqm22QsxFWqJTQyYjFMyznccV035t00EGfh3Ac-YHaEYjueZrnGeOeSVMHwCCoAa1L_Em1r8FSbal-f8Rqj371BrB66JTzHlKgA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇧🇷
ویدیویی‌از وینیسیوس‌جونیور در سن ۱۶ سالگی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/102438" target="_blank">📅 18:04 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102436">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iTVk9mQyoroCRd0QEQX_nvgBcszZwOj4hnyww2ujXykk9MMZ-xltc43pjs5ne6jZJAqwHnRp2dUOa3XQoY_wRGi4lTJ9bzsQQlzQ-hqB_c82rZvzceF3UcaKO65-x-ZJ21_rxlrLxYLPQXvaAbxaiDFm8nzlJlmc1Hyk_miXLn8KQhIyx--8nJddbU4KJQbljoTCpshLodfJmiJMa9_skrda2jvgjdjXVh0Wcr7RMPldNPhRcnztrPACc3QFkbrT_yc2hY0y0g4ADyriiyY7Mbp3WCCacpIJh0aX4zI88qPZ4mQzPHNnis18FFukxlZxKMfCG12k--BXPh8ufRrxcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qEdTwkReHncWTm4e80t5maQhTZNRaRurm_0TJBsbLQ1FQ3U0XbA4Y3mf5tqJzrkimBKVW_pHXzCqYq2047erxfahVs8DBXcNAYRDWHE8WAjc0sVFnaHgSgB0xDteHZ4w96mZIum1gfAgtYjog7i_9PNEaO7WkhCcu-9bzf_2o7J7BdlxduvKztjuPMJyoQCZd7aIb69boQnJd5L8QroSvNSFwLELIW6X9CReykhA7k8x9lD2Ap3-1d0iXx2f61jF0md9mddr-knqxUuBcKOhjUnx5P3Anb_MYWjybkRffxxDiB1SUglxtaZZsx1FESXcS1vILv23hVgKykreuNeF5w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🔵
فوری، محرومیت سنگین چلسی:
🗣
باشگاه چلسی به مبلغ 10 میلیون پوند جریمه شد.
🗣
همچنین، به طور تعلیقی از ثبت بازیکن جدید در دو دوره نقل و انتقال محروم خواهد شد. به این معنی که اگر بار دیگر خطایی انجام دهد این بار پنجره قطعی بسته خواهد شد.
🗣
در ابتدا 6 امتیاز از مجموع امتیازات چلسی در فصل آینده کسر شد، اما باشگاه درخواست تجدیدنظر داد و این رأی باطل شد.
🗣
این رای بخاطر تخلفات نقل و انتقالاتی در دوره آبراموویچ مالک قبلی باشگاه صادر شده است. مالکان جدید این باشگاه خود این تخلفات را گزارش دادند که باعث تخفیف در حکم نهایی شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/102436" target="_blank">📅 18:03 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102435">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/68f9e38a71.mp4?token=qBNlFgmio0ILc5uVR_8TqIS1mxGoDVrRIZ63oZTY3ZteTBeEIqg_8PoY3BHtnb4BSCJDY6ojU2LUun6QBdDQgNHnUcww8Ceq5b2M4iniLbFP4pr8sdcG0B_Jb9ujQo7Ed13WzSMBOkRG8s3S0RfyjNfl9ba2zrVEB92RKtRjNrzsaBgJed_LOG1riIpFlCE0DvvveCGkCwOPtTTvPVebuRwoAiLBDlVYl2mZgqMm9NTTA8QJ4GxPz-dVWUv0kzgxKRGjVm3OrDV5ygll4zz4ctYgUxzoRz31UiKZr3ctc32amig7lP-KAz7y8y-c1IhcdR97d-HQjy6voh1Qn_mZuCRuv8yaHdVqXE16xyUUwFjqowOXZqxn9CIPCXlnrEAVGJMhpDrZ1XUmG-L6FlV4t3pejCp7BOgJlBkQoV_0dpi8l4jKn3TddpAugaBKRjwG3pnHvKvYY8_N80AV978C7lBx7VJbuwXlthKvfvUYD_z3eYLijMKID7XExjeHZ-VgMW87UdEDRXO6OWIWs8vGaLUr-VM0WO9D5lC4gToVbe8w52crPhnEkycTNV92gsAwcJKfP6iFHvWsFfk02976ZX6ED7Ei6RWrGZnq2D2UGOPm48Wur7uBKsrKHaZN8u_8YdDIB29n85ZBTf4GbKljfSKv1VHk-3oFJz8oNViI8Vk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/68f9e38a71.mp4?token=qBNlFgmio0ILc5uVR_8TqIS1mxGoDVrRIZ63oZTY3ZteTBeEIqg_8PoY3BHtnb4BSCJDY6ojU2LUun6QBdDQgNHnUcww8Ceq5b2M4iniLbFP4pr8sdcG0B_Jb9ujQo7Ed13WzSMBOkRG8s3S0RfyjNfl9ba2zrVEB92RKtRjNrzsaBgJed_LOG1riIpFlCE0DvvveCGkCwOPtTTvPVebuRwoAiLBDlVYl2mZgqMm9NTTA8QJ4GxPz-dVWUv0kzgxKRGjVm3OrDV5ygll4zz4ctYgUxzoRz31UiKZr3ctc32amig7lP-KAz7y8y-c1IhcdR97d-HQjy6voh1Qn_mZuCRuv8yaHdVqXE16xyUUwFjqowOXZqxn9CIPCXlnrEAVGJMhpDrZ1XUmG-L6FlV4t3pejCp7BOgJlBkQoV_0dpi8l4jKn3TddpAugaBKRjwG3pnHvKvYY8_N80AV978C7lBx7VJbuwXlthKvfvUYD_z3eYLijMKID7XExjeHZ-VgMW87UdEDRXO6OWIWs8vGaLUr-VM0WO9D5lC4gToVbe8w52crPhnEkycTNV92gsAwcJKfP6iFHvWsFfk02976ZX6ED7Ei6RWrGZnq2D2UGOPm48Wur7uBKsrKHaZN8u_8YdDIB29n85ZBTf4GbKljfSKv1VHk-3oFJz8oNViI8Vk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🏴󠁧󠁢󠁥󠁮󠁧󠁿
درگیری کورتیس‌جونز، سیمیکاس و سوبوسلای بر سر بازوبند کاپیتانی لیورپول در بازی دوستانه اخیر!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/Futball180TV/102435" target="_blank">📅 17:40 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102433">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cocbcTsXReUutAxDBJYX7-nJXvHPUkpIrOGKnlF7U3DzuaZh3U0WAG_-LA0jLe0983QZnwzJ3omfVOi50VlohdwwUBMOO4ZGlZWUxpOStTWW6Dpn2SFz0RmYsErIIIcO7jbmTpXbjVslLRYpH-HztsCLz9aL82Vv9cDBs2PQZixvo8m6q3Acgxll4haPwxaDr474hoLHB_Zra5Qbr5cPicIlYocAvfmGbpOnYyAWlGRdaRQN5ViMm7IWiUQw9CfeUgjHxidFiCTCpBB2vul3gwaLzRV88Lf7kzFu_0bpgQRLeY9N39hXFNGm6XPLyD6QQ-NYN6eCUTUdb-L-3GmIIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RN0cl0AK3F78DCu7MMEwnpFJWqqKprTfA2AAfNCM5As8y1i-XS08PPhTDvrMJgkxHgPcW3PhkGGom8Ch0kPOidDq9SojmvN7yWlfzUVx-nvfM6M05ZpZy16FrkWSGO79z8UQ6feSYU8X0226U83uWtuE31zmJqV7BaZTAKUeQWgmmUZhAnUpwu3np5pKV7ixlyPlNs6fHgcPOnWGWvm_CxVwPphtKTxWtyzMkMjHdJydxMV2CrHG-7x-i5gBhnLS1S6uDCMqts0NMPR812z1DukBt1e0vDBbx8T7KxiZQo899gtffKYQ8_reIxSrdiSC25vLYj-3nsQLLrfipOCH6w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
ال اسپانیول:
پرتغال و اسپانیا اعلام کردن اگه اینفانتینو پیشنهاد خصوصی سازی جام جهانی رو پس نگیره از میزبانی جام جهانی 2030 کناره گیری خواهند کرد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/Futball180TV/102433" target="_blank">📅 17:36 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102432">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromچِشم به راهیم</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/96363baca3.mp4?token=kC7oU17iBVPRWIiGmmhj0NjKxyR1RM1xZJdz9EP-3P-Qu5ZMWfwD9882hxm9QLq2ViMl7yOT9BonYfpGP0a-LFIm7ESUFiUe5Z7fKx1HNTrtAEvMJGwVkQwF8hakR2uPxdkg-u3y37mBjwTcq5S22qat90BQsh3ZhYKurlcLaRn45y-v2eVIo_w-c43FxH--d51lgwpLIAsAvIpx6imMKQjih3St4NEBppCLr-P1JS4GE_dF1dKQhJspSIeIs3C8waABkOOs1JhT_jvI40CSLDbAg_bj1zCs1zFec6bunNHR7z4xQXCyxlsBG4Wm9jQAKpnQMG37Mo59uPyTgXbRCA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/96363baca3.mp4?token=kC7oU17iBVPRWIiGmmhj0NjKxyR1RM1xZJdz9EP-3P-Qu5ZMWfwD9882hxm9QLq2ViMl7yOT9BonYfpGP0a-LFIm7ESUFiUe5Z7fKx1HNTrtAEvMJGwVkQwF8hakR2uPxdkg-u3y37mBjwTcq5S22qat90BQsh3ZhYKurlcLaRn45y-v2eVIo_w-c43FxH--d51lgwpLIAsAvIpx6imMKQjih3St4NEBppCLr-P1JS4GE_dF1dKQhJspSIeIs3C8waABkOOs1JhT_jvI40CSLDbAg_bj1zCs1zFec6bunNHR7z4xQXCyxlsBG4Wm9jQAKpnQMG37Mo59uPyTgXbRCA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
مرزها برای میزبانی از زائران اربعین آماده‌تر از همیشه
🔹
در آستانه اربعین حسینی، پروژه‌های عمرانی و زیرساختی در پایانه‌های مرزی کشور با هدف تسهیل تردد زائران اجرا شده است.
🔹
در مهران ظرفیت خدمات و زیرساخت‌های برق، آب و روشنایی تقویت شده، در شلمچه بازسازی و نوسازی بخش‌های مختلف پایانه انجام گرفته، چذابه با توسعه امکانات رفاهی تجهیز شده، باشماق به سامانه‌های هوشمند مدیریت تردد مجهز شده، تمرچین توسعه زیرساخت‌های خدماتی و ساماندهی محوطه را پشت سر گذاشته و در خسروی نیز سالن‌های مسافری، پارکینگ‌ها و فضاهای خدمت‌رسانی توسعه یافته‌اند.
🔹
همه این اقدامات با یک هدف انجام شده است؛ سفری ایمن‌تر، روان‌تر و آرام‌تر برای زائران اربعین
#چشم_به_راهیم
#اربعین_حسینی
#سازمان_راهداری_و_حمل_و_نقل_جاده_ای
🌐
rmto.ir
🌐
141.ir
@Cheshm_Be_Rahim</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/Futball180TV/102432" target="_blank">📅 17:36 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102431">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">💥
🧐
رونالدو، پسرش و جورجینا درحال عشق و حال در گرمای تابستونی اروپا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/Futball180TV/102431" target="_blank">📅 17:20 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102430">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7e703311f9.mp4?token=uDVSG6RL6CshcV63X5hxgFMjQSR5HcZi6iqExVNNDSqph78HlYliMkolBbD7cCSs5LP36MQnD5yVSWAJtqqZ1aEcAagyg2Opdt-p-q51miT1PtrWFujOEMjjoIzfeAbhPjSSrb0yC-Wj1khxgF5zBz74Is1LoU_x_Z1LK51QsD7gopwGj3B6xlxfd73J_Rbi5WoOyJVfI5zEIhxXO8iSHYXh0TG8ISFkACFdDMLS-DazsQdAwMpVN_qLboIAQyMIjjY5FU1SpGQQvF85Jqujojs3Si6xX-70q7TBVmcD5-zQ-K2MYtc7rSV9pRDIq2EcxbgwKSgq5bTXD0MC2XEFeQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7e703311f9.mp4?token=uDVSG6RL6CshcV63X5hxgFMjQSR5HcZi6iqExVNNDSqph78HlYliMkolBbD7cCSs5LP36MQnD5yVSWAJtqqZ1aEcAagyg2Opdt-p-q51miT1PtrWFujOEMjjoIzfeAbhPjSSrb0yC-Wj1khxgF5zBz74Is1LoU_x_Z1LK51QsD7gopwGj3B6xlxfd73J_Rbi5WoOyJVfI5zEIhxXO8iSHYXh0TG8ISFkACFdDMLS-DazsQdAwMpVN_qLboIAQyMIjjY5FU1SpGQQvF85Jqujojs3Si6xX-70q7TBVmcD5-zQ-K2MYtc7rSV9pRDIq2EcxbgwKSgq5bTXD0MC2XEFeQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✔️
👍
🎙
تمجید جالب کاسمیرو از لیونل‌مسی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/Futball180TV/102430" target="_blank">📅 17:00 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102429">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b472a6619e.mp4?token=tsWuUtyacsjB9Iudv02gZ04AtDtkIyhWACctaMKSf0x0mYzbTg3wB21wSJrddZaQP0wuqtQu2d4I8zz1bYZeiSJ2TcdmO5FPhOescypTrPVjEo3x6UvJ8-2Twr2PhOEs6v8medJiSj3rnmc3gjATfyuKMqWn-KB9hsx_MGMlA8ZdXV2FgmFE7uSE6h4h7tIkgGhy664vH7w4oer2IFs0AItN-2gatYzTb-QYIG8q2uzYZ6Vv0VIM2ML6m2seKICuWDq_NtWZFZLBvBfdhuEfET5NCNAVYV7gnshUt4FUNdfrKrlJeS5ArzU2KBXT14cVMSJ8dnJbbkXrDhMTolbz2w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b472a6619e.mp4?token=tsWuUtyacsjB9Iudv02gZ04AtDtkIyhWACctaMKSf0x0mYzbTg3wB21wSJrddZaQP0wuqtQu2d4I8zz1bYZeiSJ2TcdmO5FPhOescypTrPVjEo3x6UvJ8-2Twr2PhOEs6v8medJiSj3rnmc3gjATfyuKMqWn-KB9hsx_MGMlA8ZdXV2FgmFE7uSE6h4h7tIkgGhy664vH7w4oer2IFs0AItN-2gatYzTb-QYIG8q2uzYZ6Vv0VIM2ML6m2seKICuWDq_NtWZFZLBvBfdhuEfET5NCNAVYV7gnshUt4FUNdfrKrlJeS5ArzU2KBXT14cVMSJ8dnJbbkXrDhMTolbz2w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
🇮🇷
یادی‌کنیم از بازی تاریخی ایران و قطر با گزارش جذاب عادل فردوسی‌پور
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/Futball180TV/102429" target="_blank">📅 16:40 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102428">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dfd29d0ef7.mp4?token=L8E4zboRNYl_mtYOnSCh98UdjtQdeTIMkslDBMD7bIeuZPqcr6gIDpaOoijMZvqfZJ-BRlvB7VqMB78y_Z_KTXH9hgLtf1cxC6F47I2Zg0_HGboMDCcxe8stbR9aJPkG5TH9bbQvsbQ84l-i1-Xj3IiInMVcsHSps4YlsOM_9NTTVpLdbzBK7By-tAE4I_9cfVRtVGsK5MJOeJgFm1FYTwde6-ZEUi7eqxt3m9RewKe4_jxuLbXGrQItMrCrOCXmfSgP8k9hMy-ADLcn5ymDucYnBydhXHNA3rzB0ykT9duAxOt_asdwQeZ-wB_ERfXNgBV0psSp41tTof7t6SfZjoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dfd29d0ef7.mp4?token=L8E4zboRNYl_mtYOnSCh98UdjtQdeTIMkslDBMD7bIeuZPqcr6gIDpaOoijMZvqfZJ-BRlvB7VqMB78y_Z_KTXH9hgLtf1cxC6F47I2Zg0_HGboMDCcxe8stbR9aJPkG5TH9bbQvsbQ84l-i1-Xj3IiInMVcsHSps4YlsOM_9NTTVpLdbzBK7By-tAE4I_9cfVRtVGsK5MJOeJgFm1FYTwde6-ZEUi7eqxt3m9RewKe4_jxuLbXGrQItMrCrOCXmfSgP8k9hMy-ADLcn5ymDucYnBydhXHNA3rzB0ykT9duAxOt_asdwQeZ-wB_ERfXNgBV0psSp41tTof7t6SfZjoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نیاز بود یه آیتم جدا برا لحظات تاریخی فیروز خان کریمی
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/102428" target="_blank">📅 16:20 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102427">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d17c8ef3f2.mp4?token=VtYZnlNtyM2ftsPkQo1BhCGdikv8XHTHOp-Pze1HFq9mVR0o0F2TJrO2D7DqWoHqnoe6LHjh_-YoKm4J1TBunH4x0AGESzXLS62ZY-Z5N9v4pDdvK38tuRTtMOe8U4k-g43XX35YJ-pvYV_As2WSh6n1MGVDBfKVvuFyRCmRgLaI-LXkUbSbi1oD0vSoH_WrZAkAScdqvzDAJCVL3dbdQWNlzOUEZuTb0kP3iznHTXGbexoN_yz97iQUdL7yfRXGqdQT2kL3Q8ZNWn9BIhHorVZE7Oe_KINZVW4ydqWTS2opCzBHN9TTokVgzzPl4vE2MMP19ma19iEXzKgGXH8VXQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d17c8ef3f2.mp4?token=VtYZnlNtyM2ftsPkQo1BhCGdikv8XHTHOp-Pze1HFq9mVR0o0F2TJrO2D7DqWoHqnoe6LHjh_-YoKm4J1TBunH4x0AGESzXLS62ZY-Z5N9v4pDdvK38tuRTtMOe8U4k-g43XX35YJ-pvYV_As2WSh6n1MGVDBfKVvuFyRCmRgLaI-LXkUbSbi1oD0vSoH_WrZAkAScdqvzDAJCVL3dbdQWNlzOUEZuTb0kP3iznHTXGbexoN_yz97iQUdL7yfRXGqdQT2kL3Q8ZNWn9BIhHorVZE7Oe_KINZVW4ydqWTS2opCzBHN9TTokVgzzPl4vE2MMP19ma19iEXzKgGXH8VXQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🤯
▶️
رکورد پرش سه گام جاناتان ادواردز (۱۹۹۵) با ۱۸.۲۹ متر ثبت شد و ۳۰ سال پابرجاست. این دستاورد استثنایی در دو و میدانی تحسین شده است. ادواردز در مصاحبه اخیر بر تکنیک منحصر به فرد و هماهنگی قدرت و تکنیک تأکید کرد. او پیشرفت رشته را با شکستن رکورد توسط نسل جدید ورزشکاران مفید می‌داند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/Futball180TV/102427" target="_blank">📅 16:01 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102426">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/543e2ce52d.mp4?token=OUeUijJi6N6DnlGUywOxSO18kxvvc9U0iiT5UzRUMcWzwD26XqhNHYL2Nnx_DHA4DmxlLOmL1p3DvAeS8zXOFZApCP5Lbp2n2FufGS8VFtEH-Xop9hNtWAy347nE3MYR4vAVYYblu-BQkVFYuXH1PuXuVqV2b4oy3fMsc6tY7_WWXuoWG2vuVe9D8n2FWZKqDemnXSIEuyKck1YIxlsshA3XOPg-7N6G53szCRHKdNhdFix7RdywPId_wY75cqJvaEUH85oVeBAp_o18yqpBsiYrnhMR8-M3-5HJjcaapjq9lA2j1vevg6V_tlAf4i9qSZDv3NeeY0D7VFlMEbzgKQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/543e2ce52d.mp4?token=OUeUijJi6N6DnlGUywOxSO18kxvvc9U0iiT5UzRUMcWzwD26XqhNHYL2Nnx_DHA4DmxlLOmL1p3DvAeS8zXOFZApCP5Lbp2n2FufGS8VFtEH-Xop9hNtWAy347nE3MYR4vAVYYblu-BQkVFYuXH1PuXuVqV2b4oy3fMsc6tY7_WWXuoWG2vuVe9D8n2FWZKqDemnXSIEuyKck1YIxlsshA3XOPg-7N6G53szCRHKdNhdFix7RdywPId_wY75cqJvaEUH85oVeBAp_o18yqpBsiYrnhMR8-M3-5HJjcaapjq9lA2j1vevg6V_tlAf4i9qSZDv3NeeY0D7VFlMEbzgKQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدئو کمتر دیده شده از مارادونا و فن‌پرسی
💘
💘
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/Futball180TV/102426" target="_blank">📅 15:40 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102425">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e43f315425.mp4?token=QG9x83nzdlah2TeJ6Meoq4Byc0DhEpa9J7HKOTUU4nYKu1UIHKiORDkuQeADJd_u5nIznD4MBff08vXxbNYyHfwTbFakggdTxB8EpH1pDeSYi-jBo5qIoXbEwWBEnndu_5Q58VAGA33fehmKkqTHcTw0sYZm03Hsvo6nBErSbYVhhPVdxoja_veM3RAo7-G3gHTwEdG-ToyLjQ1Df7MMxl9xY1PtxHuuUWMD8YdsUrSt2Jx95KTdW0CkBhhkzTnsqrZ8fTb2YB4V_nX482l9GSpMSFDSbN8md3BrC6GpFHXA4BH0hZMoZs8CvXIxKYEZRkaLUiPaRPB7e6cxphhJ9g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e43f315425.mp4?token=QG9x83nzdlah2TeJ6Meoq4Byc0DhEpa9J7HKOTUU4nYKu1UIHKiORDkuQeADJd_u5nIznD4MBff08vXxbNYyHfwTbFakggdTxB8EpH1pDeSYi-jBo5qIoXbEwWBEnndu_5Q58VAGA33fehmKkqTHcTw0sYZm03Hsvo6nBErSbYVhhPVdxoja_veM3RAo7-G3gHTwEdG-ToyLjQ1Df7MMxl9xY1PtxHuuUWMD8YdsUrSt2Jx95KTdW0CkBhhkzTnsqrZ8fTb2YB4V_nX482l9GSpMSFDSbN8md3BrC6GpFHXA4BH0hZMoZs8CvXIxKYEZRkaLUiPaRPB7e6cxphhJ9g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
⚠️
تجسمی از المپیک اگر تهران برگذار میشد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/Futball180TV/102425" target="_blank">📅 15:20 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102424">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ea1f4ae5ef.mp4?token=r1IHsPWJFEHraRIBXHOeZhfrpP3wiQOX_Cv8XuzwdO7QAvvAy1jjGBJ7B_-_ttxXlAxSBKz_8j_EL2g7XwctrGNLLfU3xfse6Yyg7NgEPwVPFMFQy1T5wfq9XqT-VA815_QCVlFkstJizasppXNM7D0HmTQ9toWXY0rG6xAd5zRfBmsA3BQwqrZCWKqky8zBvcxRY0YWjRHueNhAckrf3Yq48j68kR9SLD_b5pE0Wjt-QQCeoXLiyzJ69ff9EOsybSDjsTOVZOR_V5V89hfJzEwKXEnAjSw_Y7fTnCVGY3spVq2EIaRo1yH0BUrjSVwjFVv-mDXfhI6-GCOQKpSCGkhwk3wgT7HUkyaC95NswViqK955ELkFrgErHBqW_TcF56QADQNQNskGR_2m4vpiyS0XyOUNuQg4NjfGeNYf0dqt70lNsT7vfluKmpXkvgCnAdkZ11Bgo46fA7BcTvK3QiOUU1nEP5aNXaMv6kekIxPWoDFqhGN7VrC2xVJmcib2LT2r6hSmirktbJVmlWACwUsXnhKsMs2FS0WUMi96o-Ts4_FLl_ha8DRfNRfu_A1SLtOTH8QYDYkR40XwxPGAy_l3zCI6Wa3kShnSIiOhSHry5402wEINbahPSkekdslmK0TouBx910eyWTJMMZb5d0XtsjZ8qc8HkxQaHDxuYCA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ea1f4ae5ef.mp4?token=r1IHsPWJFEHraRIBXHOeZhfrpP3wiQOX_Cv8XuzwdO7QAvvAy1jjGBJ7B_-_ttxXlAxSBKz_8j_EL2g7XwctrGNLLfU3xfse6Yyg7NgEPwVPFMFQy1T5wfq9XqT-VA815_QCVlFkstJizasppXNM7D0HmTQ9toWXY0rG6xAd5zRfBmsA3BQwqrZCWKqky8zBvcxRY0YWjRHueNhAckrf3Yq48j68kR9SLD_b5pE0Wjt-QQCeoXLiyzJ69ff9EOsybSDjsTOVZOR_V5V89hfJzEwKXEnAjSw_Y7fTnCVGY3spVq2EIaRo1yH0BUrjSVwjFVv-mDXfhI6-GCOQKpSCGkhwk3wgT7HUkyaC95NswViqK955ELkFrgErHBqW_TcF56QADQNQNskGR_2m4vpiyS0XyOUNuQg4NjfGeNYf0dqt70lNsT7vfluKmpXkvgCnAdkZ11Bgo46fA7BcTvK3QiOUU1nEP5aNXaMv6kekIxPWoDFqhGN7VrC2xVJmcib2LT2r6hSmirktbJVmlWACwUsXnhKsMs2FS0WUMi96o-Ts4_FLl_ha8DRfNRfu_A1SLtOTH8QYDYkR40XwxPGAy_l3zCI6Wa3kShnSIiOhSHry5402wEINbahPSkekdslmK0TouBx910eyWTJMMZb5d0XtsjZ8qc8HkxQaHDxuYCA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇫🇷
🔥
👀
۵ گل زیبا و برتر اولیویر ژیرو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/Futball180TV/102424" target="_blank">📅 15:05 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102423">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1a3bfea056.mp4?token=FfrDYOaACpDeUB7SAbh1LHj7KHpnErjEvcUmZBK_45TtE7es--43DI-TwdT2FxId3YJko_SptvSv_9jGAn7-M9MNbui_pEx3bcEmtrYliqNi7ren3nu50zeqgdnJfEVnCilKkydF4wLp20jctRMKmPaDhQjJXMEsA6IzaCCkFDcVfCpCxkzguS7IgiOADPyOu2qFKb_1lC1gdxV7d5NAmqlfrjqk9n0UVU-m-8boKW8j7ilp9sptZWj6x7irYEHi_p0ibQLGFRUxtSlI4kLcR1nb8_ihrqsxp3i-FecQUQ6nZccKjyhlqTNcd19HhTdeRbETy-7b7zOwTEpAR2DUog" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1a3bfea056.mp4?token=FfrDYOaACpDeUB7SAbh1LHj7KHpnErjEvcUmZBK_45TtE7es--43DI-TwdT2FxId3YJko_SptvSv_9jGAn7-M9MNbui_pEx3bcEmtrYliqNi7ren3nu50zeqgdnJfEVnCilKkydF4wLp20jctRMKmPaDhQjJXMEsA6IzaCCkFDcVfCpCxkzguS7IgiOADPyOu2qFKb_1lC1gdxV7d5NAmqlfrjqk9n0UVU-m-8boKW8j7ilp9sptZWj6x7irYEHi_p0ibQLGFRUxtSlI4kLcR1nb8_ihrqsxp3i-FecQUQ6nZccKjyhlqTNcd19HhTdeRbETy-7b7zOwTEpAR2DUog" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🇦🇷
سه دقیقه با لیونل مسی ورژن 2014/15
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/Futball180TV/102423" target="_blank">📅 14:40 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102422">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IlCBKYZ-BIMiS4HQ7MygTFxonTkmjnhMCfH1mABqynk6A1FP7_-8uc-lhesvaWJI4DKFMF64AQsXRzDRjBKZlThCtyxDCzutXIzTRiHufFNeHzbEa1dx1ai2wfS1eIMcYxicqOaXqkszZ7xG8gd62ELhAe6hw5BPPSEKW428ED_3k9rLMKFmCvcZLIKSJfK5-X2zu0XwUkwFyR0PyreETbNuXj5ypjCXHXGJTAG2l6-o2WdYWqJf08mMR35iNvN6jAezecPJ9v4DIPTDuew-vcvcuwwlJ2n2WqU38y60LcJ2HzOoTGH4eQrTZT6Nbgw1ulYa1KNksRMheV25ideWPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
لیست رئال‌مادرید برای بازی با فیورنتینا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/Futball180TV/102422" target="_blank">📅 14:36 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102421">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m6BMd2_GSvwA1KKJj7PSRzUJLLfKgb6tVz-grounSbgwVQLa2y7mtoQqYtl9-Q0V5M-rKAv2eFGMNi42LVeRK0L0cMf4Z64rlYT9SPYQ-VPoYLw4rF0WuLQDch7VI_UH5qJN81XGX7OAG-paInwWwvEUJJuJrxXsYbCH9z_5gA33nqfMZzbo1diRnH5GSzw3lo6BKQhXz0AvGB-7usV_EBog5nPE12nv5gGU0ZW-MjpORmxOM8Vn1cPfp3tV-bUwL2gEDGDxI0QIbiXSmLHkdzUiFAMiX6UM60zaZ57HOodjbteFKL-Gidlifj-WWYK-dW_4nb5_lNRFHeSV8dUSMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🗞
#فوووووری
از نشریه اکیپ فرانسه: آرسنال با نیوکاسل بر سر انتقال برونو گیمارش به مبلغ ۹۰ میلیون یورو به توافق‌نهایی دست یافت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/Futball180TV/102421" target="_blank">📅 14:20 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102420">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/529b07ca6f.mp4?token=PHzh8o_vApNtHvIBCy5-tXcN6q1df9JysH5sWMSAN9TxESItHWVTdGgRNWVzaQGAT6vIZCuwTA3FlLuTwY-avUHQnCgOkcwWPrtMUIuICGhuUsmCZm3iSuoWPecCITpN58un4eKgz1aBbouszfsO9mPSV4CrYpf6OInX4whfly9oczXMSWWjh1SR9aEHxBgYQk8XMNJ2oIAVHmWv2eSaYAwMlfjN6djmV320dkng0mtv6cWhcguNj7qmfXbLtCR8tr3n8L9HtcZ_VSdcpxoia_6d__tSREsERKHY57hzt6TR9AqAEAV92tz2A3tt6cUIeGvjjj7YeO7UA0cBNWPaSQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/529b07ca6f.mp4?token=PHzh8o_vApNtHvIBCy5-tXcN6q1df9JysH5sWMSAN9TxESItHWVTdGgRNWVzaQGAT6vIZCuwTA3FlLuTwY-avUHQnCgOkcwWPrtMUIuICGhuUsmCZm3iSuoWPecCITpN58un4eKgz1aBbouszfsO9mPSV4CrYpf6OInX4whfly9oczXMSWWjh1SR9aEHxBgYQk8XMNJ2oIAVHmWv2eSaYAwMlfjN6djmV320dkng0mtv6cWhcguNj7qmfXbLtCR8tr3n8L9HtcZ_VSdcpxoia_6d__tSREsERKHY57hzt6TR9AqAEAV92tz2A3tt6cUIeGvjjj7YeO7UA0cBNWPaSQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
❤️
✅
یوسفی: زمین و تماشاگر که ندارید، لیگ را پلی استیشنی برگزار کنید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/Futball180TV/102420" target="_blank">📅 14:02 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102419">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9889076a09.mp4?token=SQgrxRqrhnn9a1S5z3HsD2hNYvlZ0DoTDv1w5RiVA9e3bCL0CdumF37WGRGKzc1AA7WNB-1cW_nhlzisbrAaqDGBjnQtseNuBqxgftYHGeF0QGvEycxdkjd4RCKMjvLw2UIcGLQYzJigFndDneyVO2bHa35d8s85x8t5tbN9dQ2MEsL8njBNVoI-1o_U_-lMddCdjoR6WMhmkCvBB3clQfGbI2GVcI5OKmooFQhcgGRxxn40ouPKr2Vx2Z1M1xKR-2AWmRDxUMsWenoXVqOnGsdc_iBGCHeOiym_DX7SncrfW5pKHtujjrCoaiAze_GSMR5GzsUWFk2-etgEIe6S0g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9889076a09.mp4?token=SQgrxRqrhnn9a1S5z3HsD2hNYvlZ0DoTDv1w5RiVA9e3bCL0CdumF37WGRGKzc1AA7WNB-1cW_nhlzisbrAaqDGBjnQtseNuBqxgftYHGeF0QGvEycxdkjd4RCKMjvLw2UIcGLQYzJigFndDneyVO2bHa35d8s85x8t5tbN9dQ2MEsL8njBNVoI-1o_U_-lMddCdjoR6WMhmkCvBB3clQfGbI2GVcI5OKmooFQhcgGRxxn40ouPKr2Vx2Z1M1xKR-2AWmRDxUMsWenoXVqOnGsdc_iBGCHeOiym_DX7SncrfW5pKHtujjrCoaiAze_GSMR5GzsUWFk2-etgEIe6S0g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❗️
💥
روزی که پیتر چک آماده ترین گلر آن دوران فوتبال میخکوب شد و این اثر هنری شاعر رو تماشا کرد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/Futball180TV/102419" target="_blank">📅 13:40 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102418">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jomWBA3ejv83No-9H4UF9aD9biwC_2qcILNO6eAoCCw1kLQYJcHGyZcsrkMhzVOps2lNMkAjXeFGourxj5kfoy8XryvKhgUIewZbjM7nk5I34aoXrfsgFlkC-X1LPSBoAXWpN4XvSIRYa2kD_QZHOCY9UpfSagUd1sb9SChhdNsvI2iZXA7UCD_uxPXVOU8OTQFBDrbhvAMT2HJsc_TICXsKiAHS7cwZ6fd8F_TrKgwHVqKbNGKD_oMvmoK9tJ0Tc2F7y2ZP8U48gZXMEZ2MOt5od5pOVAbpU5w3E1idHjg7ecG761vcaKCRKvisUE0m9_p--_ebpxRWWz6wqGATgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚪️
کارلوس اسپی تو تمرینات رئال مادرید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/Futball180TV/102418" target="_blank">📅 13:37 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102417">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vB2BFYcypbiSQV-55RcBmDa5h9GRs3XRRaPRJYxD3VDNXbfTf1WZh-t-YcctUMUiroEmXS4n6No886MWh_PI18z9BNnva84WkhK0X6w3aD2qvJo0sPwItkIBQ_p95gv1oEmkQQb10aV4XEKUY2rDUMZYXFYhRQ_-XABdNuTMyyQYZDLbSWJcZjus6nIKpqlnuT9bZdyG9oLr_W9tgfZKahTQAvlD9KW7qaenWC72vzb7eov2fXYGIItsVWvay2he8IdJs8bZcHht-04u2hmqxHo3bAqsH0mh50KstlDbHXnxtUnsrzgNeYxGn9lhY6osyy2MhoiJ5IM_WZGNPBsR9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🏴󠁧󠁢󠁥󠁮󠁧󠁿
روزنامه اسپورت: دو باشگاه آرسنال و تاتنهام به رقابت برای جذب فران‌تورس پیوستند!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/Futball180TV/102417" target="_blank">📅 13:32 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102416">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a4938ae1d8.mp4?token=hZYQRQGux1xphFZRaCXR3YSmY94x8prOfQ0faiqTAFQb65qzbYpNMquNEc8Wj30lVvngJOSLFffPvfK0iUjPpn_ybbocR13uXlidtxHIroRJov0G_C6Yz7c9BLbPewSKpeHWU8DeLIPXqcFZd5pA29aHs5qiYGL0TOTPg3Rxz7ftCfTKB59o3XyjZeOBljEc928RXNlpgtlRhEsiJZ9YmMgRU7ZIvpzBPx5SpgGdaevF4mRn3IzxPS9QOjei2FN-_5ae8Md4_AjOncYL366_1kKvczBPv984lwAHsPgECvIMGjutGRkZylnMrFadIupcE8hAPlVMMmt10nUycb8_4A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a4938ae1d8.mp4?token=hZYQRQGux1xphFZRaCXR3YSmY94x8prOfQ0faiqTAFQb65qzbYpNMquNEc8Wj30lVvngJOSLFffPvfK0iUjPpn_ybbocR13uXlidtxHIroRJov0G_C6Yz7c9BLbPewSKpeHWU8DeLIPXqcFZd5pA29aHs5qiYGL0TOTPg3Rxz7ftCfTKB59o3XyjZeOBljEc928RXNlpgtlRhEsiJZ9YmMgRU7ZIvpzBPx5SpgGdaevF4mRn3IzxPS9QOjei2FN-_5ae8Md4_AjOncYL366_1kKvczBPv984lwAHsPgECvIMGjutGRkZylnMrFadIupcE8hAPlVMMmt10nUycb8_4A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صحبت‌های بامزه رونالدو از ارتباط صمیمی با پسرش
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/Futball180TV/102416" target="_blank">📅 13:20 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102415">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5029f55db8.mp4?token=OjtMWpHdpPMDeAYAauMDgF4AA8a5fkJSOC6GttKqajWLPQX9UXp_ilJHO8T33LVJuFTXLPyvIVPCCq928IqFiInbO09NxEqCcG02jS-EdFeLCa2295blakmwZs8KGoqo2VQykafuHs9aR-dUjVaXq5-dmfTfSP_7FRTGrXq6e3YeViWzAkoPYTF2Flex6s5lCnQK7S-BBEfU380w5sFQ-TvzqLbPZHzkwJYD_GI89-g80Irj1o2AL0HyGRSPjySS9vxxfRDo1pxXL_iN-dvhFMPno1eFma_LEkhYHzo6WIjS7Zdc8RNBw4HX8i1JFxgGk3LUCNYGpr_q1MIf2SuUHQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5029f55db8.mp4?token=OjtMWpHdpPMDeAYAauMDgF4AA8a5fkJSOC6GttKqajWLPQX9UXp_ilJHO8T33LVJuFTXLPyvIVPCCq928IqFiInbO09NxEqCcG02jS-EdFeLCa2295blakmwZs8KGoqo2VQykafuHs9aR-dUjVaXq5-dmfTfSP_7FRTGrXq6e3YeViWzAkoPYTF2Flex6s5lCnQK7S-BBEfU380w5sFQ-TvzqLbPZHzkwJYD_GI89-g80Irj1o2AL0HyGRSPjySS9vxxfRDo1pxXL_iN-dvhFMPno1eFma_LEkhYHzo6WIjS7Zdc8RNBw4HX8i1JFxgGk3LUCNYGpr_q1MIf2SuUHQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
🔵
درخواست کودکان جنوبی کشور در وضعیت جنگی از رامین‌رضاییان بازیکن استقلال!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/Futball180TV/102415" target="_blank">📅 13:01 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102414">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0ac78119da.mp4?token=cj3HqyGkrEysedPyKTCcwg2tNACJaEaXrslq345X6iJg2PkaC5ryZBOrDUVV92ocWqudD6maQpIH4fyl-hK7U71qMXTPj1lTnILHAbeJbMs-9iNGkCLV40tnIf-9Bc7UBF6zklcPiynkzMANtqLXBNb1zC7mFI3YuBPUENnjaCCTRmd33d0hs27DVBPMmyo8dzpyl5FWu_yLXIN2YnDHnOPRzxJ3eVzjuUGCZRvBufSRWcjQy0zoGEuZPkH0IvKRbeLIiJv19qLKjCTJCIfPDLzMRqAfdFiqOh_FIeWEbRD-EOxr5gHD5v9ZDLSN4OaN63D81M5i7dMUK48RQCwBdA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0ac78119da.mp4?token=cj3HqyGkrEysedPyKTCcwg2tNACJaEaXrslq345X6iJg2PkaC5ryZBOrDUVV92ocWqudD6maQpIH4fyl-hK7U71qMXTPj1lTnILHAbeJbMs-9iNGkCLV40tnIf-9Bc7UBF6zklcPiynkzMANtqLXBNb1zC7mFI3YuBPUENnjaCCTRmd33d0hs27DVBPMmyo8dzpyl5FWu_yLXIN2YnDHnOPRzxJ3eVzjuUGCZRvBufSRWcjQy0zoGEuZPkH0IvKRbeLIiJv19qLKjCTJCIfPDLzMRqAfdFiqOh_FIeWEbRD-EOxr5gHD5v9ZDLSN4OaN63D81M5i7dMUK48RQCwBdA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
⚠️
نصیحت اسطوره‌رونالدو به امباپه
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/Futball180TV/102414" target="_blank">📅 12:40 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102413">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🤩
#فوووووری فابریزیو رومانو: آلن هالیلوویچ استعداد برباد رفته بارسلونا در آستانه امضای قرارداد با پرسپولیس قرار دارد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/Futball180TV/102413" target="_blank">📅 12:34 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102412">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/75b732a95e.mp4?token=Tyy46tv2zNB5eqormJ1pCKeGX6vaFy0pDdrJz0z4UNcbUkInZNfyEqtSho5B1YOABgRvULq9jY3rGvYVX8eBh98tTSLC8ROxQ-9fB-gNcMZIDK4My36Q_UXpE9qIwpAh0jqp3E1ICrBW2rIEjcsDCNO4rpXsBk7w8KWTA1uji2yS_hJp7WHWE_4Z7383BSJwSNvvnMCg50b4jiGxZ1lQuEgajfLxiPXemMGmhkabjaGMFJY__ANiv55pApm_a3ZSf6iHSwQqd89eyTFHxX5Akmzdgm-AYt_I47qxZKnHCQ3uY6pJSsKENLvw7t5moNMXpMIjcKsyjETcrPm8DM5oNA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/75b732a95e.mp4?token=Tyy46tv2zNB5eqormJ1pCKeGX6vaFy0pDdrJz0z4UNcbUkInZNfyEqtSho5B1YOABgRvULq9jY3rGvYVX8eBh98tTSLC8ROxQ-9fB-gNcMZIDK4My36Q_UXpE9qIwpAh0jqp3E1ICrBW2rIEjcsDCNO4rpXsBk7w8KWTA1uji2yS_hJp7WHWE_4Z7383BSJwSNvvnMCg50b4jiGxZ1lQuEgajfLxiPXemMGmhkabjaGMFJY__ANiv55pApm_a3ZSf6iHSwQqd89eyTFHxX5Akmzdgm-AYt_I47qxZKnHCQ3uY6pJSsKENLvw7t5moNMXpMIjcKsyjETcrPm8DM5oNA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
🇧🇷
آنچلوتی: "در هایدریشن بریک نیمه دوم بازی جلو نروژ اشتباه کردم تیم رو تغییر دادم که باعث شد کنترل بازی از دستمون در بره و ببازیم..."
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/Futball180TV/102412" target="_blank">📅 12:24 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102411">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2964e2f72d.mp4?token=m9tV29IAd8dBzXP6JE9-PN4yKQwLMJzyRAiTcJ6CMM-8xtrAL6IE6M3BuayuyWvvPbDC3jN0GgOtRx84loHW83-Izha_tBOMhNviU4KpGg30LxBSNH4S3PcSKA2u7V5HCzSEStc_U0Au6DvxbG6FZ89c1FZDyOsIvum_zX17Yk1DoU30busRVc3VZ-M8MvzqQOsY0xGN_28o6Q1C0RtgGn9-x1um0cC_LlhowyvTcQv3ysu1JYl5MD2ejiGKj4uLSRf1wb2LpAAvtoB1MUwJ5pys8w1hb3Rnjyui1Gy_nQZaFXDEyu96k8RhzCZo2TTK7JIN0Tn48ooc0v_SBPj9qQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2964e2f72d.mp4?token=m9tV29IAd8dBzXP6JE9-PN4yKQwLMJzyRAiTcJ6CMM-8xtrAL6IE6M3BuayuyWvvPbDC3jN0GgOtRx84loHW83-Izha_tBOMhNviU4KpGg30LxBSNH4S3PcSKA2u7V5HCzSEStc_U0Au6DvxbG6FZ89c1FZDyOsIvum_zX17Yk1DoU30busRVc3VZ-M8MvzqQOsY0xGN_28o6Q1C0RtgGn9-x1um0cC_LlhowyvTcQv3ysu1JYl5MD2ejiGKj4uLSRf1wb2LpAAvtoB1MUwJ5pys8w1hb3Rnjyui1Gy_nQZaFXDEyu96k8RhzCZo2TTK7JIN0Tn48ooc0v_SBPj9qQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
‼️
جواد موگویی که اخیرا در گفتگو با عراقچی یه سری اطلاعات حساس تهران رو داده بود، این سری اطلاعات مسکونی مقامات نظامی و ... هم افشا کرد
😳
😳
😳
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/Futball180TV/102411" target="_blank">📅 12:17 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102410">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1b5a4f433a.mp4?token=CaBqSPiCfFrnCeH9H_dSWpaiNXRjyrMofu0febLccE9XuUg2C8z9Tf3vhezDJGACPwNZhopO9rgu5fsnN4fyXoKDtYzb-AkKHWe4D-cEr-jCfPgcR0ExX2UP6gjP4315iOjp4y88zoW_O9AM5Zy1rlmmsmVdRdSjv9_Gj3nQ8EBDWttFlwK7lM0aDo7AtGKOSQh86z3i37j5sVgnG0rQx0Wtz4DVKmm1pTqSKzmfeqriv_2_QEcH0eQNLHgOy6Gnn8mP7bTECs4zGK2oGadeBavshPwd4tP-f1t3ZRIlJ1_6qRq0C2poQa_ty_9CPaKYXBQcKGmm4BwXjKz849kDAA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1b5a4f433a.mp4?token=CaBqSPiCfFrnCeH9H_dSWpaiNXRjyrMofu0febLccE9XuUg2C8z9Tf3vhezDJGACPwNZhopO9rgu5fsnN4fyXoKDtYzb-AkKHWe4D-cEr-jCfPgcR0ExX2UP6gjP4315iOjp4y88zoW_O9AM5Zy1rlmmsmVdRdSjv9_Gj3nQ8EBDWttFlwK7lM0aDo7AtGKOSQh86z3i37j5sVgnG0rQx0Wtz4DVKmm1pTqSKzmfeqriv_2_QEcH0eQNLHgOy6Gnn8mP7bTECs4zGK2oGadeBavshPwd4tP-f1t3ZRIlJ1_6qRq0C2poQa_ty_9CPaKYXBQcKGmm4BwXjKz849kDAA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🔵
🔴
‼️
علیرضا بابایی مدیرعامل چادرملو: تورنمنت سه جانبه به دلیل کمک به پرسپولیس برگزار شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/Futball180TV/102410" target="_blank">📅 12:06 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102409">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c746b16b5a.mp4?token=XKPr8GxENirk5NF29NjjxhOrU4JyoJK8fHH5Xxc5GxS6nKEd3F4hDDtCuosjzi-jKrMk53ZMFqkZzN2zt5yJeayCvkdE9ewdoJ_9CT2MrZWEieRW7krYnRBUyP9oi2N7pdNA2iIO7QRHPeVGpUfwN1BnQI6AiEECRt4YSEXeew1qAHajaLIkx6nHI1R_MBwQtVzpfT0TKKk20Dzm1tyDdP2t03wbHMy3C8vAVUSf-iR7rotp2SviaghUzuE8Ma_uhKd-F6sH-0PlhSZDHEz6B4lAt1ca-1yHpEj7Dp3NCZzlt3Iv7s1hD8ymcYfUtnr5JwGwqq3p8C2B9fbtPmZGEQWKMvumVTBy_OM2b1Gjf3yKhIUC24G_Z47MdrxP3aKhHQgXjviQt_b78uxiT_ikBsNr69cvh7PX0rGXtB-jRT25R2MiOV-jdTUAoPLugwPd59q-aVuKFny6x5ag1f4_pzTh4-TJzz26SdoXDj-fQ9S8p9OTD-bvhBTTvYUG3LIN1z4B_TUiizQIAa77zHMMrlggHOwJK_H0MY5uoQzLwICBlcqu_3qy5xL53wUOzOWVNFBOtGxhOjRoNQGlGwqLvY31Dyty3BTN460XiFB9AWg1-77l_EFDgjHVe0WFvmbXKOU6VD_ybcO4IURaKGAns35Itoq5U7yLePclBysUBhQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c746b16b5a.mp4?token=XKPr8GxENirk5NF29NjjxhOrU4JyoJK8fHH5Xxc5GxS6nKEd3F4hDDtCuosjzi-jKrMk53ZMFqkZzN2zt5yJeayCvkdE9ewdoJ_9CT2MrZWEieRW7krYnRBUyP9oi2N7pdNA2iIO7QRHPeVGpUfwN1BnQI6AiEECRt4YSEXeew1qAHajaLIkx6nHI1R_MBwQtVzpfT0TKKk20Dzm1tyDdP2t03wbHMy3C8vAVUSf-iR7rotp2SviaghUzuE8Ma_uhKd-F6sH-0PlhSZDHEz6B4lAt1ca-1yHpEj7Dp3NCZzlt3Iv7s1hD8ymcYfUtnr5JwGwqq3p8C2B9fbtPmZGEQWKMvumVTBy_OM2b1Gjf3yKhIUC24G_Z47MdrxP3aKhHQgXjviQt_b78uxiT_ikBsNr69cvh7PX0rGXtB-jRT25R2MiOV-jdTUAoPLugwPd59q-aVuKFny6x5ag1f4_pzTh4-TJzz26SdoXDj-fQ9S8p9OTD-bvhBTTvYUG3LIN1z4B_TUiizQIAa77zHMMrlggHOwJK_H0MY5uoQzLwICBlcqu_3qy5xL53wUOzOWVNFBOtGxhOjRoNQGlGwqLvY31Dyty3BTN460XiFB9AWg1-77l_EFDgjHVe0WFvmbXKOU6VD_ybcO4IURaKGAns35Itoq5U7yLePclBysUBhQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🔵
علیرضا بابایی مدیرعامل چادرملو: بازیکنان را از پای دیگ نذری آوردیم و با خواست خدا پرسپولیس را شکست دادیم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/Futball180TV/102409" target="_blank">📅 12:05 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102408">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f1b81246b4.mp4?token=rvMqFiD5rA1_ZODoyY0iQBzXrC0qeu9u8cs1J1WkNl7wzR5KWui04UBHMis9Ns-O0YViaf3G5MIB6AdPxmtB3DOUZ_9YDTln5miHDVCrWeAxt0wGjt3PruoVWAxSTaMzcfxcq_MWMi8YGk53VedWcOPLuouDH-sZtIa_13-LtAMA0roOz0c9ITSL3l8OxSl684NZma2j9hpAv7l16bLqBPh4gPMf7bUcZLCJ3AtWsdWXXWDvN0vedvGslIZwmkEYM6mw3kkTfeiROj19SjdUtFlfXCekRmJ2a1s4Tn_OPM1knMSmS0yp2waVrW6zl1Y-PVYDcnrN9z8VKymjuk_B8Qsa3n3yaApsqK0bNijgeeRqsBNrpjGrx3Di15DCRxj9cCRKMmt5jgmkvT_D4Th9b0u9pdMkmIYCjfCPjVl1LgMSVhba9wvFItInzVFj1zak168Grdd03j_E3XgakMWsgr4aZ4RpBZjwT6wQR8_Pc7onYI33UudTvEIVm0QYm_rUhiOg3b3YAJwZfuUssBpffSrRb0bbbXCUIQ0DUTfbUFWqcDDIFlV2vmp7a5PkfUdGnLOOSdffIHomfRv2S330zXz8L6i20hu1jJ-LlZkQ_k_Bkk2SfWpVOS1Ea7ExYrgIAdESm8Ke8ZJqrOCcYImD2znnq8M7RWUtyDv0YfZjrfk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f1b81246b4.mp4?token=rvMqFiD5rA1_ZODoyY0iQBzXrC0qeu9u8cs1J1WkNl7wzR5KWui04UBHMis9Ns-O0YViaf3G5MIB6AdPxmtB3DOUZ_9YDTln5miHDVCrWeAxt0wGjt3PruoVWAxSTaMzcfxcq_MWMi8YGk53VedWcOPLuouDH-sZtIa_13-LtAMA0roOz0c9ITSL3l8OxSl684NZma2j9hpAv7l16bLqBPh4gPMf7bUcZLCJ3AtWsdWXXWDvN0vedvGslIZwmkEYM6mw3kkTfeiROj19SjdUtFlfXCekRmJ2a1s4Tn_OPM1knMSmS0yp2waVrW6zl1Y-PVYDcnrN9z8VKymjuk_B8Qsa3n3yaApsqK0bNijgeeRqsBNrpjGrx3Di15DCRxj9cCRKMmt5jgmkvT_D4Th9b0u9pdMkmIYCjfCPjVl1LgMSVhba9wvFItInzVFj1zak168Grdd03j_E3XgakMWsgr4aZ4RpBZjwT6wQR8_Pc7onYI33UudTvEIVm0QYm_rUhiOg3b3YAJwZfuUssBpffSrRb0bbbXCUIQ0DUTfbUFWqcDDIFlV2vmp7a5PkfUdGnLOOSdffIHomfRv2S330zXz8L6i20hu1jJ-LlZkQ_k_Bkk2SfWpVOS1Ea7ExYrgIAdESm8Ke8ZJqrOCcYImD2znnq8M7RWUtyDv0YfZjrfk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⚠️
🇪🇸
مشکل ایمنی ورزشگاه‌ها به لالیگا هم رسیده‌ و تیم رایووایه‌کانو نمیتونه از استادیوم خانگی خودش در فصل‌آینده استفاده کنه!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/Futball180TV/102408" target="_blank">📅 12:02 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102407">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/47a01fbf75.mp4?token=bEKHBUy9gU9ItP63X7I5v1z4iIyn7BX1cHRfd4SZvJTxOmUfdXKSDp__LN2e127w_Ida0vpgsUszsyC62ABBR7azWfC5HT1WHLYAjLgIzg7Hr_K-XzZMquHHy3a539H8Ao2vEAGOtx-yMZuRc3Mmp6ZTaSFSOjYo5x_V2y9WjPQw_AEF7KQfw8O-hUvl9qkzuN0tyb26WD4rUj1W-uIdpyhgOICtH6aT8d8L5kzPslP-S-S_uk-E6wmwDB4bNKg8DgxS4Bu8YwQmcvp85E_tZPXOm-OqzgNQJgNgw6ibtxhwM2gIgKsp8iKSypzJPrYhq-3AqxbSjLFtL4gcOtoZRQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/47a01fbf75.mp4?token=bEKHBUy9gU9ItP63X7I5v1z4iIyn7BX1cHRfd4SZvJTxOmUfdXKSDp__LN2e127w_Ida0vpgsUszsyC62ABBR7azWfC5HT1WHLYAjLgIzg7Hr_K-XzZMquHHy3a539H8Ao2vEAGOtx-yMZuRc3Mmp6ZTaSFSOjYo5x_V2y9WjPQw_AEF7KQfw8O-hUvl9qkzuN0tyb26WD4rUj1W-uIdpyhgOICtH6aT8d8L5kzPslP-S-S_uk-E6wmwDB4bNKg8DgxS4Bu8YwQmcvp85E_tZPXOm-OqzgNQJgNgw6ibtxhwM2gIgKsp8iKSypzJPrYhq-3AqxbSjLFtL4gcOtoZRQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
ویدیو وایرال شده از صحبت‌های تلخ و بامزه یک ایرانی حین ورود به‌تونلی در بندرعباس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/Futball180TV/102407" target="_blank">📅 11:40 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102406">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/262957043c.mp4?token=FGWYYvKilvoDvZY6oqPirJUAVrqIyKmRx5U0_s82SH3ka88jpFLpO5GZRpGVKcp5X7fnDCQCSGIokA9z9McmFafC_1LtyJP1Ank9KChCrvzOIVOAfOO1A1unr2_VSrW9rZuLGoErs8bBRbp7h26y-2FWeRO6okb34zRSCYCXNHEh9DUSXg3SG31Ijr8MBUA10cpkDpP47HW3Gay0IgMCdsX5LVswCEh9Hw3iCrHNgy124gUHP-LCrtXvYe-Yas3DSLTxXnZxLAkgTvobFDqPoyfdQPOGZUgqmAsXLRVharwZW-cx938SLxoPY5mWojHppEWrEe6obe0mZYCdfgbtKg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/262957043c.mp4?token=FGWYYvKilvoDvZY6oqPirJUAVrqIyKmRx5U0_s82SH3ka88jpFLpO5GZRpGVKcp5X7fnDCQCSGIokA9z9McmFafC_1LtyJP1Ank9KChCrvzOIVOAfOO1A1unr2_VSrW9rZuLGoErs8bBRbp7h26y-2FWeRO6okb34zRSCYCXNHEh9DUSXg3SG31Ijr8MBUA10cpkDpP47HW3Gay0IgMCdsX5LVswCEh9Hw3iCrHNgy124gUHP-LCrtXvYe-Yas3DSLTxXnZxLAkgTvobFDqPoyfdQPOGZUgqmAsXLRVharwZW-cx938SLxoPY5mWojHppEWrEe6obe0mZYCdfgbtKg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
🏴󠁧󠁢󠁥󠁮󠁧󠁿
سوپرایز خاص‌ ژابی‌آلونسو برای فصل‌آینده؛ رونمایی از ستاره ۱۷ ساله قزاقستانی چلسی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/Futball180TV/102406" target="_blank">📅 11:20 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102405">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ef2180d890.mp4?token=UP5wvEvM26-hB-TDlZkAhQYiBN61Z2Hlq_xGSj81bCyu7_jVNYv5JdkAgrdg0rlSAfa4iFXiSn7FXF1VZRPjs_Sfr-J-EX2UkFh3WzVQSykhp-oJx-KR2v-yL0KwVt735P7gdC77h8RpDH8rHp089qk0ZPyQZUg2PG-QzSKQjid4YdUQcOSMhTeYnjvHmcmz8iMbKlwrgKovWdKGvjfjUScvPgXMi1INaAfmcA-GTv0oyoDmzLBbfSYWyVRT-8FQaNFnb_ObhaH2kbWDRWLsgPVqueHZny-QDYLiY7w4L7zFPPqI-XXKtQjIwN7L-w4B-LNnbCH1-7HlXtGUQGHDKA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ef2180d890.mp4?token=UP5wvEvM26-hB-TDlZkAhQYiBN61Z2Hlq_xGSj81bCyu7_jVNYv5JdkAgrdg0rlSAfa4iFXiSn7FXF1VZRPjs_Sfr-J-EX2UkFh3WzVQSykhp-oJx-KR2v-yL0KwVt735P7gdC77h8RpDH8rHp089qk0ZPyQZUg2PG-QzSKQjid4YdUQcOSMhTeYnjvHmcmz8iMbKlwrgKovWdKGvjfjUScvPgXMi1INaAfmcA-GTv0oyoDmzLBbfSYWyVRT-8FQaNFnb_ObhaH2kbWDRWLsgPVqueHZny-QDYLiY7w4L7zFPPqI-XXKtQjIwN7L-w4B-LNnbCH1-7HlXtGUQGHDKA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
آماده‌سازی استادیوم نیوکمپ برای فصل‌آینده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/Futball180TV/102405" target="_blank">📅 11:04 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102404">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b31c9897d6.mp4?token=Byjo2nCa0hCOYJ-4zrSlFweb2CZSXIJFJxgxzp8_7JKtGuCFjJ7fSYtFu4Ji1hPkIKfauQvvZWItsGV8_hba5FEqmmZgvbpLEqAQxxm8LlrSREcAEfSkr3O3azw0jMjE0iuqOGx2MolC6FsRemqYGEpzDUo-hrKN54qdwdq2hzZj3MF_IlJMVIPcOs83t3PGTPmRxMErpwiD_8JYrkJfShV5YSkuqw0wW6_AZ-Cv9OdXZ_TetHyKh593Ltj7FOVEf_Yj9RUcFzPBHHPkonKUbBjouo5CQoby4oFGqBDQoHqmd1tMoov-oHzsjmomLEfcysY5bWys6S_7VUcPToZqwQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b31c9897d6.mp4?token=Byjo2nCa0hCOYJ-4zrSlFweb2CZSXIJFJxgxzp8_7JKtGuCFjJ7fSYtFu4Ji1hPkIKfauQvvZWItsGV8_hba5FEqmmZgvbpLEqAQxxm8LlrSREcAEfSkr3O3azw0jMjE0iuqOGx2MolC6FsRemqYGEpzDUo-hrKN54qdwdq2hzZj3MF_IlJMVIPcOs83t3PGTPmRxMErpwiD_8JYrkJfShV5YSkuqw0wW6_AZ-Cv9OdXZ_TetHyKh593Ltj7FOVEf_Yj9RUcFzPBHHPkonKUbBjouo5CQoby4oFGqBDQoHqmd1tMoov-oHzsjmomLEfcysY5bWys6S_7VUcPToZqwQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
پاسخ‌تند و کنایه‌آمیز مهدی‌رحمتی به صحبت اخیر معدی‌قایدی: بذارید تو‌ توهم خودش بمونه!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/Futball180TV/102404" target="_blank">📅 10:46 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102403">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
✅
کیت‌دوم فصل‌آینده منچسترسیتی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/Futball180TV/102403" target="_blank">📅 10:37 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102402">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/869e38d1a5.mp4?token=XJHeC1zGmPCgLz7kVJcMWDRz1MV0MT8GtTglOMDaqC8f9A2gzGlodjNQJ61HIgLWpSk-ex-0eJ3_CniJ4yurojAJxjvnQe0BmL_Pjo8mo3yKVvT1b1Ausz9xFDGtWIsDIy9brncxvPup-6vnNZSjGpW0GLFdqSmyJhzlzOJM78AxbZYziZ3AMgNiLGfNQ5xxwlpSCPapL0IVjcLBjEh2hnAStSvmPdkdJhvFJLbZDSplt4YI8M9dOymyc45sbsFhE3rbhsdINbQB4wwNBPww_xzzCCaIMgFWuxD8c4gvQlnGU089sQrcQMvVS8_UwwlQ6T2yUWPbhQJ1_YELxpu0RIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/869e38d1a5.mp4?token=XJHeC1zGmPCgLz7kVJcMWDRz1MV0MT8GtTglOMDaqC8f9A2gzGlodjNQJ61HIgLWpSk-ex-0eJ3_CniJ4yurojAJxjvnQe0BmL_Pjo8mo3yKVvT1b1Ausz9xFDGtWIsDIy9brncxvPup-6vnNZSjGpW0GLFdqSmyJhzlzOJM78AxbZYziZ3AMgNiLGfNQ5xxwlpSCPapL0IVjcLBjEh2hnAStSvmPdkdJhvFJLbZDSplt4YI8M9dOymyc45sbsFhE3rbhsdINbQB4wwNBPww_xzzCCaIMgFWuxD8c4gvQlnGU089sQrcQMvVS8_UwwlQ6T2yUWPbhQJ1_YELxpu0RIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
درگیری شدید فیل‌فودن ستاره سیتی به همراه مادرش با چنتا از مردم در یکی از کلاب‌های شهر منچستر
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/Futball180TV/102402" target="_blank">📅 10:12 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102401">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9f0266060c.mp4?token=gdYFGpOuizG6BBVJl2i7Ede6zT0kETkZURJBZKI3KkOcr-tTYzz5EnrLSb7Kmp2ZIxiZm5qSkJ9CBdx9O0IZK7AF7mXSkK-8MXqEhjOvn5tPngrQkS66z1GXlzgYEzoeWxv8MEndnE67-33IMIC_EXGgyYlNPuJCigQrKQgVTIgH3tQrnXJDY-_5w04KKUU7dxhzDA1FOYAZEhSPYgn1942V3uzznIg2KnzzEwJ65tvJGaAqrR1mO0nPjwxzfD5ADZ7TPfIaWFpmfE_Xz6OI3qNDORqNUcG4vPHDWzkB805Hb96HjgdgyJNNittHSsFR5VEbjKgLmUQJerYTdVv4XDcSkdIePFsybWhd-bl1r5eaqK_Zn16arnmpsnUdcCqSo85udzyXloFI-Sbio8vYgT2zKy_N7qD6GAwx9tU8ztJ6rntsv2WwTEBggIxVpDyMJWybr4giG6XjpchHY-Kk2BlUIgK25QBCPWjUueG79ef-W4tUnK0zEcRSjRN3wJlw0QRWbARFbTX1CA6QcDafX9dhdY1__uMqgVebeGRO_NjOXo9tN4_Lfrk6tLFsUioO028e5LDoCMKEJ1wpQuLIo_uHs8dlkUWR1ML9HhIz3JD91W8isHiikv3YuMzbYxPBQ0YhOstyWlCufDbCYjEvjcGi2C6oRrFubNYv9PpFdYo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9f0266060c.mp4?token=gdYFGpOuizG6BBVJl2i7Ede6zT0kETkZURJBZKI3KkOcr-tTYzz5EnrLSb7Kmp2ZIxiZm5qSkJ9CBdx9O0IZK7AF7mXSkK-8MXqEhjOvn5tPngrQkS66z1GXlzgYEzoeWxv8MEndnE67-33IMIC_EXGgyYlNPuJCigQrKQgVTIgH3tQrnXJDY-_5w04KKUU7dxhzDA1FOYAZEhSPYgn1942V3uzznIg2KnzzEwJ65tvJGaAqrR1mO0nPjwxzfD5ADZ7TPfIaWFpmfE_Xz6OI3qNDORqNUcG4vPHDWzkB805Hb96HjgdgyJNNittHSsFR5VEbjKgLmUQJerYTdVv4XDcSkdIePFsybWhd-bl1r5eaqK_Zn16arnmpsnUdcCqSo85udzyXloFI-Sbio8vYgT2zKy_N7qD6GAwx9tU8ztJ6rntsv2WwTEBggIxVpDyMJWybr4giG6XjpchHY-Kk2BlUIgK25QBCPWjUueG79ef-W4tUnK0zEcRSjRN3wJlw0QRWbARFbTX1CA6QcDafX9dhdY1__uMqgVebeGRO_NjOXo9tN4_Lfrk6tLFsUioO028e5LDoCMKEJ1wpQuLIo_uHs8dlkUWR1ML9HhIz3JD91W8isHiikv3YuMzbYxPBQ0YhOstyWlCufDbCYjEvjcGi2C6oRrFubNYv9PpFdYo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏴󠁧󠁢󠁳󠁣󠁴󠁿
نظر سرالکس فرگوسن درباره‌مثلث جادویی بارسلونا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/Futball180TV/102401" target="_blank">📅 10:00 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102400">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f864b5c9ce.mp4?token=T_SX3YC6VzjZYxcs87guRntlZtfzEwo7XK0qhWc9bzgR7-q6Xh72A1iAR--vq5OGhl0ESSqe9j-D4WFwEaB6xhN8ckbQaw-B0csgf2fEbqJjHzqEMPCLy8zPN_8S-v5tghmL7f3YXM35jhR3pf7XZk15IjEMZ0Z1Xj3BIfoDQ6SUm4Y_46yF8ndEDVNb7S4WUEtI6VySdxbIsVGpSXhqGrBL6k4GL4JuTw499Qq9MaWNcS5PCItXyKmpjggRnqCspxcqvfz-xnC0xWvjJKhUTlZCVctWW3NzReuUnaGoV6dJCYGLsJeWineXH8-kt6FkszWBuMhuToKxlpmPT6374S251ssqw4KqI-ESK5Xgev6QT8iKePXHVskQrKQdCDJSd2rXT0QTD8UvnR-kBsCra5XZNzN86wRmgEbEMVBuXF2L-GWFuNBKO25UQP933CEbgMvtvwtJj1ODF9Lrz9Cxf3N1wvXsLPtaNyEAodruHkXYdie6ZP5XR5yYM8igmcW0Wvbak9qry3Lx9A5fErkSa2TWj__m-lozO5ld4a3VKJC9APlOaaHDG4RoVuLIrfVl7JVIi8Y2e3IKMLLOS2kl3y4zDcut0qoEkSsEUBAm8GBbbpaXcGJjB5Sx-ZfvA3qBtIAcRczxqxkQQ4OEdyT9K6rOeMF-TK36pSDGHGO-_9w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f864b5c9ce.mp4?token=T_SX3YC6VzjZYxcs87guRntlZtfzEwo7XK0qhWc9bzgR7-q6Xh72A1iAR--vq5OGhl0ESSqe9j-D4WFwEaB6xhN8ckbQaw-B0csgf2fEbqJjHzqEMPCLy8zPN_8S-v5tghmL7f3YXM35jhR3pf7XZk15IjEMZ0Z1Xj3BIfoDQ6SUm4Y_46yF8ndEDVNb7S4WUEtI6VySdxbIsVGpSXhqGrBL6k4GL4JuTw499Qq9MaWNcS5PCItXyKmpjggRnqCspxcqvfz-xnC0xWvjJKhUTlZCVctWW3NzReuUnaGoV6dJCYGLsJeWineXH8-kt6FkszWBuMhuToKxlpmPT6374S251ssqw4KqI-ESK5Xgev6QT8iKePXHVskQrKQdCDJSd2rXT0QTD8UvnR-kBsCra5XZNzN86wRmgEbEMVBuXF2L-GWFuNBKO25UQP933CEbgMvtvwtJj1ODF9Lrz9Cxf3N1wvXsLPtaNyEAodruHkXYdie6ZP5XR5yYM8igmcW0Wvbak9qry3Lx9A5fErkSa2TWj__m-lozO5ld4a3VKJC9APlOaaHDG4RoVuLIrfVl7JVIi8Y2e3IKMLLOS2kl3y4zDcut0qoEkSsEUBAm8GBbbpaXcGJjB5Sx-ZfvA3qBtIAcRczxqxkQQ4OEdyT9K6rOeMF-TK36pSDGHGO-_9w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
شباهت حرکت‌های یامال و اولیسه
🔥
😮‍💨
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/Futball180TV/102400" target="_blank">📅 09:40 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102399">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5630cebcb5.mp4?token=BjjyH5byYJu7parSGbVxgEYPG96Rz6B8P2rOojU0bJN4w6BDsfKJbRil-93fHSqfF09fbh5UNJSV-nLDLjP8nS5RhtbM1Gpw-Ss-9JpnmzDZ19wl-XDquTncj2_G0oWLDaJBd-yMEUpFvZTadHMgZPnxDrfRSc6yAOrvy7hI4MZnB4hil_0V4cvKTIwDMsIhLwXDioBaHkWyZacB3pn57A3XhgYYSzKUMxTxOTHCPDdkQ_zoWm9iEO0mrEgHZgv2zXUVMR65SdRurhpG0FqJfnnzXGwhr_k4mdKvbxVn_1MfYdN_QQc0cLEJXetjkXqbj5pd754ge6Jzs2ZiFBicYU4eoSuLwI0ZDfj0fsJWc2ZDV6M7TlFisFidSPCJUE71Ahbiy8CITt8-pjyiGa-5PQplXRXIPkDGzKF3HTSQ9RkdlNJHEr3xfONuKFjrnG9A9E6gc0YfdZ1jR2f1ntJGXhZbqMoxzhVqV-AeESH5f6UT-x2nOtsh5t7rsxdbZK2sys7gsmbHA_gdOjpz3NFQE75Imt4CRbkDqb6VWGMDW3t7yELDoZMMG73ZnygvvI0vhi4GeScwKs8tp9NnxmE_pMzJ_H3i8i3QmwGPHcisY2g4CPCRPNwEjulyDbaXWbha6xqYsPGjQo2O4b_kzdPa_QcjmCnLbhuc8KIsv00K-u4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5630cebcb5.mp4?token=BjjyH5byYJu7parSGbVxgEYPG96Rz6B8P2rOojU0bJN4w6BDsfKJbRil-93fHSqfF09fbh5UNJSV-nLDLjP8nS5RhtbM1Gpw-Ss-9JpnmzDZ19wl-XDquTncj2_G0oWLDaJBd-yMEUpFvZTadHMgZPnxDrfRSc6yAOrvy7hI4MZnB4hil_0V4cvKTIwDMsIhLwXDioBaHkWyZacB3pn57A3XhgYYSzKUMxTxOTHCPDdkQ_zoWm9iEO0mrEgHZgv2zXUVMR65SdRurhpG0FqJfnnzXGwhr_k4mdKvbxVn_1MfYdN_QQc0cLEJXetjkXqbj5pd754ge6Jzs2ZiFBicYU4eoSuLwI0ZDfj0fsJWc2ZDV6M7TlFisFidSPCJUE71Ahbiy8CITt8-pjyiGa-5PQplXRXIPkDGzKF3HTSQ9RkdlNJHEr3xfONuKFjrnG9A9E6gc0YfdZ1jR2f1ntJGXhZbqMoxzhVqV-AeESH5f6UT-x2nOtsh5t7rsxdbZK2sys7gsmbHA_gdOjpz3NFQE75Imt4CRbkDqb6VWGMDW3t7yELDoZMMG73ZnygvvI0vhi4GeScwKs8tp9NnxmE_pMzJ_H3i8i3QmwGPHcisY2g4CPCRPNwEjulyDbaXWbha6xqYsPGjQo2O4b_kzdPa_QcjmCnLbhuc8KIsv00K-u4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
شیرجه زد، گرفتش، زد زمین، شوتش کرد!⁣ جوک خنده‌دار بیلی مک‌کالاک ماساژور سابق چلسی درباره‌ی پتر چک
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/Futball180TV/102399" target="_blank">📅 09:40 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102398">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fnsr5k9fj8UECvjQ-0JebMyjTUdP61wTURXS22rVgdqRoCDJXaMWLCYeRNcd0_qu368tNccDIYuelLiwqT5eK01ObowUATWf6TZNDtGkn4EeDaQt0SOMr6UxXcXO2OEYGvdtA2fsVG5A3SV3fmLc7VwuQV6PQ6IGjFcDViHcU4YVZLm-MpGBKWoi4nRD8EeRzgKTlzJUZmvNLO5ZtSQsizerFhbjhNrSMHb3XkaQ6TpFq75dTB4YtXoJE5IRT2Kg8kAzrpaqMvzeuqU6a3vEyeFZWt4yQPxI2yp_3exRD_cG7fIkJdvsRdUK_sZfg1YCqr8x80kNolN-3Zk9rXSATA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖤
🇮🇹
لحظاتی پیش، فرانکو بارسی، اسطوره فوتبال ایتالیا، در سن ۶۶ سالگی درگذشت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/Futball180TV/102398" target="_blank">📅 09:28 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102397">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d54a6dc02d.mp4?token=SNRIY44UQEejr2Q0fYTOgDfVkXa97Mlc4wR2ZcqNKPKYzioj7JdJgh0lQ3EoZKqpmx8XoGc3VavNJ7HJkI96Khjt4dIVERMu3KGIZ0nZ-SohFYlqipD335vSzdeHVlRmQxoBH-WUJQK9eIiOSG4hs8EGsz-UGZigTq8MdVKXjvOJsANOJpdmntuJtcdLuAPZPxbJ0FU16N14dikItFW8rqLJKhzc9ACk2BGioGcpJwXVaKF63RwB8pvTIsq8hL7q7aKzekEWHWD62uE_NoDSeZHgZzUBwdw_cqiXnODEHJK-UBYa_JX0qzXZ6z1CE7wlkANnBztVND_8S5E8PlcQBQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d54a6dc02d.mp4?token=SNRIY44UQEejr2Q0fYTOgDfVkXa97Mlc4wR2ZcqNKPKYzioj7JdJgh0lQ3EoZKqpmx8XoGc3VavNJ7HJkI96Khjt4dIVERMu3KGIZ0nZ-SohFYlqipD335vSzdeHVlRmQxoBH-WUJQK9eIiOSG4hs8EGsz-UGZigTq8MdVKXjvOJsANOJpdmntuJtcdLuAPZPxbJ0FU16N14dikItFW8rqLJKhzc9ACk2BGioGcpJwXVaKF63RwB8pvTIsq8hL7q7aKzekEWHWD62uE_NoDSeZHgZzUBwdw_cqiXnODEHJK-UBYa_JX0qzXZ6z1CE7wlkANnBztVND_8S5E8PlcQBQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت فوتبالیا اوایل هر فصل
🤧
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/Futball180TV/102397" target="_blank">📅 09:20 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102396">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e396ec62ed.mp4?token=vVP7OAaw77TGI4d_zwSnPTg4KqBaE1JWGGLS7xETHVeZCVOOnyV8qNs940_D_xCIsivspilQnLXcGBkKbV3KmH0TZdIGXOGZjkLdE3E0Wi3EDK4RMOlNZFHPZ587-t6X9IDS8XrBtj2F8iLRGwSe4Ui9bq7g77Ni8Tj8V3Blkik_8DsVdn_UOXyW-FQQ9znaZT8hxj8YONYsIxZaL_HQJuWgfsoUnWGAPJAXEdQAVY24Kezy-0ec0u8RvVtlarUteHfkcLK3pi5LTCGEkwDLB0cQ2YLPHUEWgUH0kiITUbOAIgcanEDdo9vf4V3aSuEF9oaXv5pxI3fH4pevm3nGrQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e396ec62ed.mp4?token=vVP7OAaw77TGI4d_zwSnPTg4KqBaE1JWGGLS7xETHVeZCVOOnyV8qNs940_D_xCIsivspilQnLXcGBkKbV3KmH0TZdIGXOGZjkLdE3E0Wi3EDK4RMOlNZFHPZ587-t6X9IDS8XrBtj2F8iLRGwSe4Ui9bq7g77Ni8Tj8V3Blkik_8DsVdn_UOXyW-FQQ9znaZT8hxj8YONYsIxZaL_HQJuWgfsoUnWGAPJAXEdQAVY24Kezy-0ec0u8RvVtlarUteHfkcLK3pi5LTCGEkwDLB0cQ2YLPHUEWgUH0kiITUbOAIgcanEDdo9vf4V3aSuEF9oaXv5pxI3fH4pevm3nGrQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
🙂
نظر پرز وقتی مورینیو میگه وینیسیوس رو بدیم به تیم‌های دیگه تو این پنجره نقل و انتقالاتی...
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/Futball180TV/102396" target="_blank">📅 09:01 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102395">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/knS32Im_ogyjc0azUxMYUc8HZThrZnEa0zyPlk6QdudgTuJw0AqJnos5G69bj53HJN5uG7WVO_ZqpmHy7tUj9e67KSnVgnvJDUakwgam3fGVNd70aqIbQH-g5zZ7YOWgI5DHsp_aaPSEQLL4J1Ftg-nlq8kERjEFqKMbmDQQsKi-Ep6BU_mrtMJiCWo356y0i7kjs2z5Ne-6oVdEkMZurw6Rw6dOy1iHTy4ymLJcOdBYfxUc7TqKyuB_Y6aXb64AQhh9auo7BKqTfVg8H83s_tTGM797cYfIxFuDJf7lIarPFQDW_Ljhe7RrsH3j1pK0dIx7xI3eYh6GzoAKguesLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇪🇸
🗞
رومانو: حاضرم قسم‌بخورم که دیومانده بازیکن رئال‌مادرید شده و فقط تا وقتی لایپزیگ بازیکن جدیدی نگیره قراره رونمایی رسمی انجام نشه. اگر این اتفاق نیفتاده باشه از حرفه‌ خبرنگاری خودم کنار میرم!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/Futball180TV/102395" target="_blank">📅 03:13 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102394">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u2lNvGCTEgge5HTFnHWZJri78e0TaTBzWMn_5W8WhlMEaakLpAa__oNSUjmmTJMB0WWLNqlUItVrZgLWBuPHVSzh6oqCQ8UHFRPRq9dchcPRGK6QPviWYbh4mbraBlE6NpNWW-4gTYr4lEUrlKyI5JaUj6NVhI_dwe5IQYZLV0YfiKjeF0WDxEZCJSosP4W0z14E31ZRI36Ml8gI41Vko06QG0KpldkI1XYVswx5XcBaJP_t_snbNVwnQg8rGzQrBX8I8E4zOdPVqa2uvbkSzRXw10YZtidC18j86VktII0G6qZG_QqyhrqWSGwKTCZ9PuImpaYozkHAVEKDBFMCQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
کاسمیرو:
خوشحالم که اینجا هستم و به لئو مسی کمک میکنم، او پادشاه فوتبال است.‌‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/Futball180TV/102394" target="_blank">📅 03:11 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102390">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Fk9wHUSVGBSMQzZ_-lo0DFVUOlJJZngxPyxKDVpES7qj2AZpArbE5pG2OnzKaq_BqjEzLVdIoEHgMxmEJUykmNRJTzTjPiRaZVGDLeziwQ6n4dvyGCaVOgu_84GsDpBMhFgz5-imQ07NMHkvfiLBzrEd-6jbcz6rIy1g1gganccFS1m8i7FEiNcOyh8La_xieMK7-FUgL42MZzCIH_xqOB5R8BnEvctVGbQ-KDjYRJZC4AOa3lPnzH-fsFK-exdjQNr811evSVcV3vN1D0iSzP2wu6r-IUaDB-nAu_uG0VlKjL3YTZU4IT2BFji_zgfXE-VrfuSh_AOM-TnmxYCjpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EVlogR4hVIBhBXUKQSIWT96IGvbwuxRoD1cTnaqVp7-Sh1Ss_5oGXCA51Ufip-XpNacLoeg9WkszgaV2Sfsa8AhiL6lDViQUAcTFDeddyyDHmmSF7a190x81VMxPH0mJLE0Q9vmzBbGjiuPKo66Pxkd-d3z0RaoF6JY5YYalJ1cX4Oq4pIvH2naiR2TLjfdEXV6ky51oXlc5D2d4gkmgKhI2eDQp-2aRts7ep6vIQnGhXxtHNG3Z_bSHUI113IAV_o2PpoOURTjMYTNF6BMDfnLqceA07foHY6klRg0DLQj-PYeNUmqeZbAUcQjTJtk182lGBtR7Ccl_46G2_MzFhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/u78C-XsrUtI-mJLP9efDJSxHoBlg2ESJTft-lgU9TWkDmBjAyC4XRQJAapP0jBOo41qYOc0LMrbIQJ2Lfb5DrG6cPZQJRaq1PbMdJPpsvgaKwgyP_EVtcgQSe-fjLAkuRG5Yo1p8IGeNy8dFK5SpiZHQXeBzCifpHjcTEW4lAlqrvE25zpF_IkusFOapvEhYSR1YoZNs3BZvmgTlAT3gY6NaJQzgXsfNlbBJ14-T7EYmz4XnipOdfPBtgrJyhZ2hdClNCpKlKmDaLbM21WxjeuC3EOQ0jEW4Tjh9uGrmytT62SRuccqW5oN7TYChbpla0cQoZmw6ZspioLVt29GFjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oMEGOXkONRLO9UjfbWKiVf3jY702Y9N6pdeIS80wbNj-gS9y7kDORyPFc22Uz5-sL9ZGNrNP_hiyWNauB4R8Gjo1mphzreYSgpaavkH31Tt4PVkre4aZ0Qwnf6PTHJ83wUGeNf9fIyC_NZD_PdxcWGyR0I-UFjR7_THBRnikTPXtNLLIixwCmWWn0r0rQKgx93VF5x_FRhegPbyxw9vILQhiU-91ofnT4IpJYE2TE8ehjW54VV6h4y1ERrrgCx8T0m7ccQVEE4IPisviwvY12tmE_UblrCvsy77YjbySy6gwDNYUpuBjLgTMXT3VSB-2yEwYO18z_SQrq4_Aedwdpw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">کریس و جونیور و جورجینا رفتن عشق و حال.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/Futball180TV/102390" target="_blank">📅 00:47 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102389">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/511459b235.mp4?token=IHEXFEMrdcfu8b8HQ1pm7EBgOmcwxUKFLdOBYhDTmq9nC1O6xbO0a_PS3CT40yXv1dNy95w7bAOCvmQ3psuPbn1HUiKcsWAN9CQ6K14OLwxU5OtbTdj0K4oq1LG64BE1szkoAAIksnjwf7bbyTK1J_XKxp4riDrAwfYjvxmQwk3aXZKQohwvIDtCXgMKL4y_ffFxpO33zFZbcO0VjLwVbvSO_BUmVJFH3ANwmWIUqtg_84R9WenSYReHCZzVLzk58RdY4kVJqRaZhmgH3XzDoddYB7GQR5BQv3nMd7W2-DusHSvRdy9DELeUL7Bny104y4BgDSAi7FCFroDxgKSQNbmY8kIr486DQJ_5j9NU6HnJ4vgqO67EzqZBqYRiT82uWNerV03MK2mR9-4z6usAdeCUi69u7UCOieWb0wCN1H17ExsOWXfOYi0LeI4RtAkqUOPTnV87NHfLqUfn6YfP3uXBn7PyWLz3I6x4JIytGOeVTLxhoGnYQ5ao4keletOs8GDMTd5ODxkLsnTDisO1Oya6SZDR0Nj9MJKutcu9mGcgTafoq1X6E_Im3vPAbq9T4RyYpKbxn6IKgEjAra6-4CN0p74M3NmKNq280GZbRxrMyf_tY6khjAZSXMS-kbOU0P3DC1YzBWvHAD4e46BxeX1zpwZUtZWmbt1I6HzUYqg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/511459b235.mp4?token=IHEXFEMrdcfu8b8HQ1pm7EBgOmcwxUKFLdOBYhDTmq9nC1O6xbO0a_PS3CT40yXv1dNy95w7bAOCvmQ3psuPbn1HUiKcsWAN9CQ6K14OLwxU5OtbTdj0K4oq1LG64BE1szkoAAIksnjwf7bbyTK1J_XKxp4riDrAwfYjvxmQwk3aXZKQohwvIDtCXgMKL4y_ffFxpO33zFZbcO0VjLwVbvSO_BUmVJFH3ANwmWIUqtg_84R9WenSYReHCZzVLzk58RdY4kVJqRaZhmgH3XzDoddYB7GQR5BQv3nMd7W2-DusHSvRdy9DELeUL7Bny104y4BgDSAi7FCFroDxgKSQNbmY8kIr486DQJ_5j9NU6HnJ4vgqO67EzqZBqYRiT82uWNerV03MK2mR9-4z6usAdeCUi69u7UCOieWb0wCN1H17ExsOWXfOYi0LeI4RtAkqUOPTnV87NHfLqUfn6YfP3uXBn7PyWLz3I6x4JIytGOeVTLxhoGnYQ5ao4keletOs8GDMTd5ODxkLsnTDisO1Oya6SZDR0Nj9MJKutcu9mGcgTafoq1X6E_Im3vPAbq9T4RyYpKbxn6IKgEjAra6-4CN0p74M3NmKNq280GZbRxrMyf_tY6khjAZSXMS-kbOU0P3DC1YzBWvHAD4e46BxeX1zpwZUtZWmbt1I6HzUYqg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
عادل فردوسی‌پور بعد از کلیپ دست‌بوسی که ازش منتشر شد یه کلیپ گرفته و میگه ویدیوهایی از گذشته من رو گزینشی منتشر کردن. هجمه عجیبی علیه من اومده! من اگه قرار بود چاپلوسی کنم الان تو صداوسیما کار میکردم و نَود رو داشتم.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/Futball180TV/102389" target="_blank">📅 00:35 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102388">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cgo4P_aDTnwh__O7nAlx1oSlU0pc5LmCUPiAF4IDancDcWkTulxRWupCouoDe0NQviPauT9bri7WiCWX0wQwGDEh3ouzLGgEfSjncMHFvJGZ0xzd0E1qh7SO9SJ3iUG2dKmwTitmV29I8IbWJHCmlAfMPJW88o-cHkRrmcqhPpjfBx6qUzVY9mbswuiHTIPY4cW6VSW1UR8e6pcqFVmNQHmag6tsR_u_hH_79Ta24tRLtmzrvF_l3pVmItciTiD-FkjT82EFEdB6baFRNTruojVuGCTsySAMtz_XAX8oYlC_qvHiLfdDdVM-PQv2O8T6cAH1kjMsX3mpJ-DKJwtNCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⚪️
فوری: کارلوس اسپی شده با بند فسخ به مبلغ 25 میلیون یورو به رئال مادرید پیوست.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/Futball180TV/102388" target="_blank">📅 00:29 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102387">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O-tKYtR7q41sroBaT5js1rGpMrDxPOnypD21y7R8k_s5NKkaGjRaNXEAy27Fo5W5pGnMj-dyCRdJS7bbQYkHHWHFbAp8ObJLp7Dx-VqE-y_SGBtVRHRSSQLzYphgtFUKE464LdZkoWs4lSm1GCI4ucG-YvbWkgGTmOrjCqoxjuhM9NqgSBUBtlNz5Mc9Gs9SQugiJVsWg1PvHj-g7a_XocGj7zeZLIymhwxC1vY2qYUbmn32dpLjHzFNOXmNIzSGtOEs0PjhhxZznsqnPOZ3BafPzntDJLSt62D9BTaYW2wB6Qf1T2tUq9mvLGbxoXGVLAEePwN4RYd_PBSg9nTq6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استوری بلینگهام که رو دستای زیدش خوابش برده.
👀
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/Futball180TV/102387" target="_blank">📅 23:37 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102386">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ae65f1051a.mp4?token=pQKovuJGOMdi4PKqoPcVzbuv4bMd1B8cZCDGpJylwKHv3rJh1BB5qYl65f8YO3Wy1i96E3DmnGesWPVx8EN606mXXVc5zIwscJQu8Gee2l6yF12EX9JudqCbrl60ror2uJ2p6MCRccOw58Y9fFkH3jUboeVKQ-MCSYpL0rUh_6hzBWTpOcV3X7I-0CBC54k_H9wAYZwFQDIYHgX9fTmXJsV-klB91UisfTaMrgQShvjl0X4n_w_-Y92kcsVmH4P56tHseJUUopJoKek4mrxpaHodUDFViBCDqb-FvthGwB4wRzq2m0TpAJ5tyEHZ9C_r3faZevwgbBxft7_Vfuqpaw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ae65f1051a.mp4?token=pQKovuJGOMdi4PKqoPcVzbuv4bMd1B8cZCDGpJylwKHv3rJh1BB5qYl65f8YO3Wy1i96E3DmnGesWPVx8EN606mXXVc5zIwscJQu8Gee2l6yF12EX9JudqCbrl60ror2uJ2p6MCRccOw58Y9fFkH3jUboeVKQ-MCSYpL0rUh_6hzBWTpOcV3X7I-0CBC54k_H9wAYZwFQDIYHgX9fTmXJsV-klB91UisfTaMrgQShvjl0X4n_w_-Y92kcsVmH4P56tHseJUUopJoKek4mrxpaHodUDFViBCDqb-FvthGwB4wRzq2m0TpAJ5tyEHZ9C_r3faZevwgbBxft7_Vfuqpaw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
🎙
روایتی جالب از تمرین‌های پاری‌سن‌ژرمن؛ جایی که حتی امباپه هم از دقت باورنکردنی مسی شگفت‌زده شده بود.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/Futball180TV/102386" target="_blank">📅 23:00 · 08 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
