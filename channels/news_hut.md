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
<img src="https://cdn4.telesco.pe/file/bXca-b8SWx0tTpih1-aWrk_ISuEviuD6adU5B5HPnDPgTUo4dYNkWkX11Ad6rPLAfkUU_12Zs6B6-lRcfvS__Q67sMkXfUw2WAa43yvkzwjKTgHjEOHqoqwAjrukIdM1Il8WHLxkeLWuNHSmsW5ecFXlnQnHtacB5lkhp8CTg0-lWCcKxld0PmpWOOwSZ8Gp0A6fWYrObFqvT7gKpcMgMaWWifcYZeF3M37_mpDtiSdJ3GajspuMv5GUIAHBoNjKs5A9xvRz1axTG4FEaqwqNJsBkWYlNd2FGdmAlVu8l53L0yZKxjjSuQqzSTzTkihcI-2n77rETxU8f6flWfuxsQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 158K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-29 18:55:36</div>
<hr>

<div class="tg-post" id="msg-68649">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lHfasZ7Fer_cFWwKBY3IRepd_ePE3btlGeScFjWCc8Zqh3SVzRVnrZ2p5lsVl6bqsGf4-maSq_kB4MysXe90nvCuv8rjQeJzdXi9p9_LUWIbn9vCkNK6IEbcUP4hCNTlmwwvZ24c9Jiqu5PVbsptyAPtrWAwGDOVLKcw8Eti2A4T4YBHat8UAYfQkd-SPhl4sYWkrPdXqrCHy0VEs7nUntEqbtOng-ELosgSvTrNiFNQQnFX_Cyz4Abg0BhxeSRITB_nvX1skYJ2xvvWg3FmBLzYFTDKAET6gjxXG-OHBm_LroQdoFsbNOv-m-4BTiZpGAirckX-krrXRfpHV2U-0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7e216a5ddb.mp4?token=MQUtxDM6x1LeTcCyCxeubptYwHNX5-i6AQqlsP7zgvE3S6tIbzIyJOzDDwUrEwEwKTjBZ5DN0mCmBiUia7tSZBJSMkOHgjRi2rJyH7hEML5zqeOIKCEt-O24RqclauCj3hZGYD5P7pabGElY2SJxyQgYB_wamXocB3rEjbhajZg2DxXw3FTcq_cPdjQu52B1_eL0XfbvWdG81fWE0bBC5hj0RHcxlaAPsnPKWX2Zub78N1RfCq_sw46RBm9sdct9ZdhucKmwq8IYs05vJm-_FooeT-5rftyWdcb1ohwT3wgso2_1H8JuXpA1lUDYyP7nCziSDw8aZGV87XrW7RrsOg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7e216a5ddb.mp4?token=MQUtxDM6x1LeTcCyCxeubptYwHNX5-i6AQqlsP7zgvE3S6tIbzIyJOzDDwUrEwEwKTjBZ5DN0mCmBiUia7tSZBJSMkOHgjRi2rJyH7hEML5zqeOIKCEt-O24RqclauCj3hZGYD5P7pabGElY2SJxyQgYB_wamXocB3rEjbhajZg2DxXw3FTcq_cPdjQu52B1_eL0XfbvWdG81fWE0bBC5hj0RHcxlaAPsnPKWX2Zub78N1RfCq_sw46RBm9sdct9ZdhucKmwq8IYs05vJm-_FooeT-5rftyWdcb1ohwT3wgso2_1H8JuXpA1lUDYyP7nCziSDw8aZGV87XrW7RrsOg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
آتش‌سوزی در یک تانکر نفتی در تنگه هرمز، پس از هدف قرار گرفتن آن توسط نیروی دریایی سپاه
@News_Hut</div>
<div class="tg-footer">👁️ 616 · <a href="https://t.me/news_hut/68649" target="_blank">📅 18:54 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68646">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HJyqZbUu29x2Jn4cuNsmm7ArHN5R1Mmn78WJiNdkGCCuvYn6mWGKTZbuqvmsUi_2gkQb9dxFj15m1FbjemVHWcsBFx35GhBS899B0QZELSb06UKQzFBBd6WUBkwKElQF3yZUVntbOeodyKAxZ2YS5RhBKmLnt2GbByD0jlxHuA2Vd6SFM5Xsor_7LVzGmJwl4rXS-H17nD7KaZ_sygmdJcDLlVksMiEiToOYbE_-Ciy6F7x3T09a2-6Kiait_sYcSgj6QUIyP9mpznqHuAVQZPN0YyYGjS4mokvnF-SbnsLo6DKQH-eyQ66Z_8TBtj5zchA7-QtK99-QWM0C-1OSow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qkPx2zKWb61ZoCYmPzZDeqkhoUy_ciXF6GuXVDsyofozN6TXv3wgcNAnT2GJMbr84Y76LyzXwhl35Z348pIhHPRCZbInvJSH8mvRllPAPvIzPFTnvbXnyhUgdmtYmE2vfIw8FrTFwcHfzx1keDM6w5lm559E1vCqvFBFWunc-9KLJBzygJlDchybv8qJbDbNS8-35xll07NdPtbCc26afPJAsmMlSDMlmWD41t5KXB0vgzl2qPR5qeglw_fFhZ0dNe-20Lt8jioxAxWnnqx8dUNt4l3x_jhRW7tBo4y6ebFMUeHR9n8zH1LbhoE9ZOQjce-f_E6Ryg1Iuag9QHuuMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/T89IPaLjuyknBnzQLY6fuTpQIT9Gwm-Ni8_rM0VoI55FnuH2D8KRudCIQwYUk0IcGxCGGOmRxjH9MD3AQu3C-1e9iUl3Rt4dTHjGIBVlm5KbjsHxAgAgVvrq64cPhtXBy581mKp6rKYvsMhXhiOk2Yt1frjdqowLo3YlKy4SlVv4XqIbf9t6QKE51rsrO8WWmYkH-90cHAlNLQpvbP6ndaae_obMMZBJjkurM4PSZYiNid6dlnk09Zwe9TZWagrW2Ds8B0Qrd2nWAsbBRHGqZHg45RGqfPrTIakCWq3s1U4WdvMFJO7FF9qtIO_fitzXYQXiCOYtYlU4-lV6n3heLQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
شلیک موشک از شیراز
@News_Hut</div>
<div class="tg-footer">👁️ 1.65K · <a href="https://t.me/news_hut/68646" target="_blank">📅 18:51 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68645">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🅰️
🅰️
🅰️
🅰️
🅰️
🅰️
✔️
آپشن های متنوع پیشبینی
💥
برداشت سریع با کد پریمیوم ووچر
🩸
هدیه 100% برای اولین واریز
🎁
25% فریبت ورزشی برای واریزی‌های ووچر پریمیوم
🔝
با ضرایب بالا، بردهای بزرگ را تجربه‌ کنید
1️⃣
لینک بدون فیلتر
1️⃣
ورود به سایت با فیلترشکن
••••••••••••••••••••••••••••••••••
💠
لینک اخبار و هدایای سایت
👇
👇
🔸
https://t.me/+ioIBrQfqMLtmMmEy</div>
<div class="tg-footer">👁️ 1.8K · <a href="https://t.me/news_hut/68645" target="_blank">📅 18:50 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68644">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gu-CSegMEF6RU30E6v21_fhPtedUJz1i6Zuu_1soCmUwKvBcrR5leXjD1cl-n_zj3MEVGyf_LWu1tqdTv7PRSwxMotbxJIwN1ZE3RvkwSgWmjvcRQQF2bu_pnmdy5TLzkqqWCEem-sWAyI6RVSn1EMM_2Y4d9VfwjNq8DOoMjzZoPRSnfwXTiy_bvPDwzPhxWpyR7zRmcbY2Wx6cXB2kXBEIY4kLSasWSwrMbui6xg7F1B0SL7ScNx8nw9N2gF55J1d6Bqr7f5Vgpr__AijY9VA0JY8mlZe1sOcy-ygu_LfPBpr01JgREj5loAGZHg-JizU41TvdUNJK7466piV95Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💎
سایت پیشبینی
YekBet
💎
📣
یک حدس، یک برد، یک قدم تا برنده‌ی نهایی
💶
تورنومنت
صد هزار یورویی
گل یا پوچ
رقابت های بازی جذاب گل یا پوچ در کازینو
creedroomz
⬅
️
برای ورود به تورنمنت کلیک کنید
1️⃣
لینک بدون فیلتر
1️⃣
ورود به سایت با فیلترشکن
📲
@yekbet</div>
<div class="tg-footer">👁️ 1.78K · <a href="https://t.me/news_hut/68644" target="_blank">📅 18:50 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68643">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">🚨
❌
رویترز به نقل از سازمان عملیات تجارت دریایی بریتانیا:
یک کشتی باری یونانی پس از اصابت یک پرتابه ناشناس در نزدیکی تنگه هرمز، آتش گرفت.
@News_Hut</div>
<div class="tg-footer">👁️ 6.27K · <a href="https://t.me/news_hut/68643" target="_blank">📅 18:19 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68642">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0dc4ef2082.mp4?token=uhMwWfDOTAVgfUNUm5XdbEmL9v6fLSZdUXYgLKCzT0zQm54dKrN_gEvn118qao03caQz3mGz_AfK20k9B-i5uaXcdfm0p2Wl7PwKvWKNCRcb49d72SZWTqjZPmZzVw6cqAVVP6hvNFyTUh2kILKfXJf_ENqzbxkGtaNHC4HddQRMk9XyjDTvDKCi2UjjRtbLqFCRjDQCQK-5gSnqbPhyXrJ9KoDb0wNd1efTlgpsDQRkBNyZRos7sVVqjUsheuDAIsl-FnE_ASb_rYzS7Xv8Uax7u59n0a4vraqLK4t7GBTRSAyybX4bPctKeTUnQ9MfXNU-D_qlzp1IxfrOdu0Piw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0dc4ef2082.mp4?token=uhMwWfDOTAVgfUNUm5XdbEmL9v6fLSZdUXYgLKCzT0zQm54dKrN_gEvn118qao03caQz3mGz_AfK20k9B-i5uaXcdfm0p2Wl7PwKvWKNCRcb49d72SZWTqjZPmZzVw6cqAVVP6hvNFyTUh2kILKfXJf_ENqzbxkGtaNHC4HddQRMk9XyjDTvDKCi2UjjRtbLqFCRjDQCQK-5gSnqbPhyXrJ9KoDb0wNd1efTlgpsDQRkBNyZRos7sVVqjUsheuDAIsl-FnE_ASb_rYzS7Xv8Uax7u59n0a4vraqLK4t7GBTRSAyybX4bPctKeTUnQ9MfXNU-D_qlzp1IxfrOdu0Piw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
ستون دود در شیراز
@News_Hut</div>
<div class="tg-footer">👁️ 8.99K · <a href="https://t.me/news_hut/68642" target="_blank">📅 17:58 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68641">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">🚨
🚨
فارس:
خبرهای اولیه از مورد اصابت قرار گرفتن یک نقطه از شهر شیراز در جریان  حمله هوایی دشمن حکایت دارد.
@News_Hut</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/news_hut/68641" target="_blank">📅 17:50 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68639">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZwjV7wciqsavjsuqUvoFkSZb1N9igDCTGJ4CIwIDOsFIuQA4Hu_wp4jYO43bjzjx2WMyDRhwW8A8NH8giCHlBU5B1YitgsLDQNbsiK0v75MZc15zPIMu16nURndeODUe49hIvX43Hu3WihwKRWsWOnZgzrf2Zevd8TbMLJmW8z_MM6rCZHBgQ2NRcCdo5RuyM0PKjsyv5FIuVqPWgzD0wU5_vCfJpBpcz4eMuV8Yg6VIfFEk4S9umqRVbyGhbbrIdWxBgkw0MTWqYQjvTKomDYoZiAOerdu1wvFSIVZxjHFBF_MFHtkUCdG8f0yVgBo80deGGWpVofrwLoz17-zBxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CyqCM2ZNJNanebq2ck9EtZsArUQJMEWZeFswWV48RO5tmtmwup2Ykl9nVzUjQLRNkHvnl83dvJn9QNR1MrvTl59xlZdGZx9QTlvT7UK3jVDLYYMI9VJirZOjLi72e4nLXCbW7xiMv2w7dYMuxWYYYTcsmZnp4hfS-htcFmjw7-JjFJIHjWozRpX4zRiHlVnlgJmbUX2D4XPMIJhUmHMowVqfUHbo7GQ4wZtwgbJ_mvomYOV4YZV8misoTTlHNvVzGknf0_XoMqA6_BNAJiKgxMmIZEGnST3_NaKtQAM7WYxkPM11yYmpfla4hX-fVDsPHk3fjpwirvICX3z4hmQp8g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🚨
⭕️
گزارش های اولیه از انفجار در شیراز
@News_Hut</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/news_hut/68639" target="_blank">📅 17:41 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68638">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">⏸
حملات نیروهای مقاومت فرانسه به رهبری ژنرال دوگل به زیرساخت‌های فرانسه و منفجر کردن پل‌ها، قطارها و خطوط راه‌ آهن در جریان بمباران‌های متفقین برای آزادسازی فرانسه اشغالی از حکومت نازی‌ها (1944)‎
@News_Hut</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/news_hut/68638" target="_blank">📅 17:31 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68637">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D_EhwJe_VOBGTocIRP7rBZtfWbMLjJfdLDrAxUNEZwisKrs1gDGjUlqk6J_hDB6G-wnvUhBoJ734VL8rXZ7sDe2EiIKqPzmWigGQ3iGjS3RdNEobIxl73TWhCP3CpVmxPbCdwgL0MT4Z_RoybVi7RsQxv15_AxwmstJJdbGiIGIn4l-eGelo9aVtChICXqZimy9DDKO3zk-y96EQ96wzNOro97ReMnOX6crjnFWDx-WYfgzqDu6tFYzuFG52Q_oW0-oXTjpQzvJ89jqMI4-btFr9qawWWYgTQ2i3UrlXjM3-wK5Ui_5vNKGrTf4vDFactDqMNQaZQ6laDyfI7fiRlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
اکسیوس:با تداوم درگیری‌ها در ایران، قیمت بنزین بار دیگر از ۴ دلار در هر گالن فراتر رفت.
با ازسرگیری درگیری‌ها میان ایران و ایالات متحده و اقدام واشنگتن در برقراری مجدد محاصره دریایی که می‌تواند تنش‌ها را به‌شدت تشدید کند، تردد نفت‌کش‌ها در تنگه هرمز بار دیگر مختل شده است.
رانندگان ممکن است دوباره همان شوکِ ناشی از قیمت بالای سوخت را تجربه کنند، چرا که میانگین کشوری قیمت بنزین امروز بار دیگر از مرز ۴ دلار در هر گالن گذشت و به نظر می‌رسد رئیس‌جمهور ترامپ آماده تشدید تنش‌ها با ایران است.
@News_Hut</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/news_hut/68637" target="_blank">📅 17:01 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68636">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">⏸
🏆
👍
ویدیوی کامل مراسم اختتامیه جام‌جهانی ۲۰۲۶.
@News_Hut</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/news_hut/68636" target="_blank">📅 16:15 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68635">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">🚨
حوثی‌های یمن با صدور بیانیه‌ای، از اعمال محاصره دریایی علیه عربستان سعودی خبر دادند.
حوثی ها با صدور بیانیه‌ای رسمی، محاصره کامل دریایی علیه عربستان سعودی را بر اساس معادله «محاصره در برابر محاصره» اعلام کردند و تأکید کردند که این تصمیم از لحظه انتشار بیانیه لازمالاجرا خواهد بود.
@News_Hut</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/news_hut/68635" target="_blank">📅 15:43 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68634">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UoNHQbd-xLkDa3vrRCSATGXr57hikAM_F55jDRa3qyeCxqsrNjO1Y9ah3dlmpL-1JT7_C_UJn4adC_ZiWS6-V2f6zNAIGuQB1aSmHkxdRx-rZNexbWBHV2z7gKWfkNt4LDyKz-k4qTMkU01PclnUM5vuqKREFvxg2OjWQ15BCmyEHiUIhncGFXz4L2asV3zf4_jCHvIggP4b2o86e3-WO2-fjH8S4KDhQVfHD3bRA3Cxqb6qYBUw57XT_lDuBSdfvwc7KLcDzi_HmAlXO_antnnNDSp_IKhXKPoLPi2H6G34TwaReAq9GudakRs6PKWM3FF4m0LvqtffdyKxoM7viw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
رویترز:
میانجی‌ها به ایران و آمریکا پیشنهادِ یه آتش‌بس 10 روزه واسه احیای توافقی که امضا شده بود، دادن.
@News_Hut</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/news_hut/68634" target="_blank">📅 15:35 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68633">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/acwW63iWBpdFN8eiB8yZQF4RVzZw9EQd8-xLTFRNuxAj9LSy6i_zsH8ZE9_peBTAhncP4ur6wMkLINEHDGynW-YegHueYN_hvVPeQD2pUnymnnlVOMzUpgOveXbXrIXeLlH_YYipsRTN47z0_oGa7dLypK3zZwUNTe0o3V8H6zkTn17b9eS4O0rUDR5ib-ztkwihViZwNa1psgAzX7Tnhs6xg1y5aNQtPucgkGJUMGh74ubPFUo1IXRTMJJHfGlwIj71UmNHgOC-WqLAePGhDed-JcmbMBswdRNxFmI0GraQLkXVsSArkfjlznRPmQhcH3gdzJCQgD_sMiIS1nB-tA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
قالیباف:
آمریکایی‌ها مدام تجهیزات نظامی جدید به منطقه می‌آورند و ادعا می‌کنند دنبال توقف جنگند. روی هوش ما اندازهٔ آی کیوی مختصر خودشان حساب کرده‌اند.
ما در شناخت این آمریکایی‌بازی‌ها به مرحلهٔ استاد تمامی رسیده‌ایم و بر این اساس آماده شده‌ایم. اقدامات باید مؤید ادعاها باشد نه ناقض آن‌ها.
@News_Hut</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/news_hut/68633" target="_blank">📅 15:01 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68632">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e891d77eae.mp4?token=HM8GCqix2kQgdOuXvbZQ0584I687b_D2K3Ru0wGWnOdjdLxqjO5B5cVheFQzCHrzLBc4uX9GEvGUv33-0W03B5DFKdq9bCgA1FuhrRzi7F7NGInKm6Uk02G36p34s5qPdx95QBTCJYkZkgKR_tJMeeGzyxFPBaqa_eUvwexc--ANvQpyvcxr6ESfg9jj22peY436k2bOpZ-RAOhzQ8bH62Tzeg-nmgLXHQg0PVNFSjG74PdFww9RW1I9easnGgF7RnOxnlvKp00TSuzFFLwAwVjsy1-EETuBicCJYR7fAu3sEImnlYij-jFMqkK5K587Gf_TK8K6MDEmiwlCWp18SYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e891d77eae.mp4?token=HM8GCqix2kQgdOuXvbZQ0584I687b_D2K3Ru0wGWnOdjdLxqjO5B5cVheFQzCHrzLBc4uX9GEvGUv33-0W03B5DFKdq9bCgA1FuhrRzi7F7NGInKm6Uk02G36p34s5qPdx95QBTCJYkZkgKR_tJMeeGzyxFPBaqa_eUvwexc--ANvQpyvcxr6ESfg9jj22peY436k2bOpZ-RAOhzQ8bH62Tzeg-nmgLXHQg0PVNFSjG74PdFww9RW1I9easnGgF7RnOxnlvKp00TSuzFFLwAwVjsy1-EETuBicCJYR7fAu3sEImnlYij-jFMqkK5K587Gf_TK8K6MDEmiwlCWp18SYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
عادل:قلعه نویی موقع جنگ رفته بود بیرون از کشور تو امارات و ویلای خودش تو آلانیا ترکیه بعد اومده به ما میگه شما تو غار بودید.
@News_Hut</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/news_hut/68632" target="_blank">📅 14:58 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68631">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">🅰️
🅰️
🅰️
🅰️
🅰️
🅰️
🎰
لذت بازی در کازینو و کازینو زنده با 30% کش بک بدون محدودیت سقف
💥
تسویه سریع و آنی جوایز شما
💯
اسلات‌های داغ و جذاب از برترین برندها
📱
اپلیکیشن اختصاصی با سرعت بی‌نظیر
🎊
وقتشه با کازینو یک بت، برنده‌ی بزرگ بعدی باشید!
1️⃣
لینک بدون فیلتر
1️⃣
ورود به سایت با فیلترشکن
••••••••••••••••••••••••••••••••••
💠
لینک اخبار و هدایای سایت
👇
👇
🔸
https://t.me/+ioIBrQfqMLtmMmEy</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/news_hut/68631" target="_blank">📅 14:58 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68630">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lfcKiEJzsmAHRXSER5-zweYnhjzh4Ipvrb1pFXHsWMFYreLpah_Oht4vdVQrjQnFyhS7zLvYZy_eE0YNcwNVpKP82KjxwbMQpuYsScQV6bj4K7G5Pk4JkpomwMrNRvSsfmlVh1_9O-JU6IwtMsa63h5-8fYbBvbOSVe7ceTlqLhnhFST9HOu8LuCJX-6sbpaHJWfAgqcRKePX_aaw6OFuS4oLIsn5JFrLqxLX9_yzByyG6lJm9AAxFCB2EtJElvCPnyqFULSsrluwFru-wiGrYF19wylBBPXWUM02vdWAq5ZxcvxZvRISKJGwEngRm8tUX1tL5dzx2jgJ6sRF99gwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💎
سایت پیشبینی
YekBet
💎
🌟
کازینو آنلاین، دنیای هیجان و برد
🌟
🎁
100% بونوس خوش‌آمدگویی به مناسبت اولین واریز
تا سقف 100 میلیون ریال
1️⃣
لینک بدون فیلتر
1️⃣
ورود به سایت با فیلترشکن
📲
@yekbet</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/news_hut/68630" target="_blank">📅 14:58 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68629">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HBv1k09jaXvFsQEkmNUC2JNkDNzUI9eT9Khrt2JE_7uZE19M4S2W4UDDVRng53XEyjoTBMvxHsPWF8Ujg2mJCxarkD22Z7kpwNxKXnQrXqEiakD2RV9bDGeW7014dX10bTtGmTdQTSTZtLQg1WxVuSdvP5LAJgYwX5AtmrqF7f1E60JJzmq84RpZsaa9cReha30i2OeGvHVKSY-BBkpdN-2hBsCRgkxEA8M9fwKfe6mqF0R5EZfpYai9dYAT7p9DyrouCTN8DYg3Wp8EdPMyDvxoC_UYP3tgst5Mihba_AMQFGsMNGfdGhOgcRdeq93KRn5IedHUh3_NLr0asgYQwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
عبدالله شهبازی :
شطرنج پیچیده این جنگ داره به آخرای خودش میرسه.
به نظر میاد جمهوری اسلامی توی این بازی مثل یه بازیکن مبتدی عمل کرد و ترامپ هم در حد مگنوس کارلسن ظاهر شد.
ترامپ طوری بازی کرد که انگار حسابی گیر افتاده و به توافق نیاز داره. امتیازهای بزرگی داد و با طعنه و کنایه، رسانه‌ها و فضای مجازی رو هم با خودش همراه کرد.
این نقش رو اون‌قدر حرفه‌ای بازی کرد که جمهوری اسلامی باورش کرد، فرصت‌های طلایی رو از دست داد و دنبال امتیازهای بیشتری رفت. در نهایت هم نتونست یه «استراتژی خروج» انتخاب کنه و مسیرش رو متناسب با شرایط تغییر بده.
حالا نشونه‌هایی از اجرای یه طرح غیرمنتظره دیده می‌شه؛ طرحی که اگه عملی بشه، ارتباط مناطق جنوبی از هرمزگان تا بوشهر و شاید خوزستان با مرکز کشور قطع می‌شه و عملاً حاکمیت جمهوری اسلامی بر جنوب ایران از بین میره. به نظر نمی‌رسه اجرای این طرح نیاز به ورود گسترده نیروی زمینی آمریکا داشته باشه.
⏺
اگه این سناریو موفق بشه، می‌تونه شروع فروپاشی حاکمیت جمهوری اسلامی در سراسر ایران، طی چند ماه آینده باشه.
@News_Hut</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/news_hut/68629" target="_blank">📅 14:25 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68628">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/357e3ebc2d.mp4?token=fgFvFkSOaEcZ2PFDqnuuVpKHA3COgFuYsn_9afzlhe1YK7ifNopx3oPhq3Al07O85D_L0RgoFuppZAF_l0r_AVtoSdYyOqijwNiKPvzJeVw_beG6zbX3YHU9_jYDxnwdJ639IJPSBgBSSRVxCoVpWO2c6e8tdtsWtE9KZLbIiXcR7wWo1DcGXBMWdo1xubi891cCYThaRnBtldrVeCBVKV2DQ0da3DhUQsuRqWBu9eH4qqpTkmdixaKOgCIoS-X6qCEkpM56-0RL7eWofi8XRquaT7lVCLkpw8MNRAkfcCRDhuT5oXfm21otXHZ4DeesNr29oXedBPXTXQWZlg7GaA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/357e3ebc2d.mp4?token=fgFvFkSOaEcZ2PFDqnuuVpKHA3COgFuYsn_9afzlhe1YK7ifNopx3oPhq3Al07O85D_L0RgoFuppZAF_l0r_AVtoSdYyOqijwNiKPvzJeVw_beG6zbX3YHU9_jYDxnwdJ639IJPSBgBSSRVxCoVpWO2c6e8tdtsWtE9KZLbIiXcR7wWo1DcGXBMWdo1xubi891cCYThaRnBtldrVeCBVKV2DQ0da3DhUQsuRqWBu9eH4qqpTkmdixaKOgCIoS-X6qCEkpM56-0RL7eWofi8XRquaT7lVCLkpw8MNRAkfcCRDhuT5oXfm21otXHZ4DeesNr29oXedBPXTXQWZlg7GaA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
مارکو روبیو:
«اگه اون دسته از آدم‌هایی که واقعاً می‌خوان برای ایران یه کار مثبتی انجام بدن، قدرت رو به دست بگیرن یا مسئولیت مذاکرات رو بر عهده بگیرن، اتفاق خیلی مثبتی خواهد بود.اما امشب هنوز تو اون نقطه نیستیم.
به نظرم دنیا داره به جایی می‌رسه که مشخص شده حداقل یه عده توی ایران می‌خوان تنگه هرمز رو در اختیار بگیرن و ازش به‌عنوان اهرم فشار علیه دنیا استفاده کنن.
دنیا باید تصمیم بگیره که آیا می‌خواد اجازه بده یه آبراه بین‌المللی دست کشوری مثل ایران باشه یا نه. این کار کاملاً غیرقانونیه و اصلاً قابل قبول نیست.
آمریکا هر کاری لازم باشه برای حفاظت از کشتیرانی جهانی انجام میده، اما وقتشه کشورهای دیگه هم سهم خودشون رو ادا کنن؛ چه با تجهیزات نظامی، چه با حمایت مالی، تا این بار فقط روی دوش آمریکا نباشه.
حافظت از کل دنیا برای همیشه، وظیفه آمریکا نیست.»
@News_Hut</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/news_hut/68628" target="_blank">📅 13:59 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68627">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fb49be0645.mp4?token=fksMqsEzF41YNTDu78fgjx8PSlWeZiVyWk7WHYY51t8Gpvj5lF3jIWHmKeQBxv20Elc6V7TNFSczCs8FkLqCV3zPp2wwA3ozkyRoAI-6bQ7E1BsRn3b-LaRhkb_VgxC5-Lqx34wbNt_p7Y2LlKq3z6EbyjLzd48UQTnZ7gfstS9EoWZJDk6bMxX3Fs46cB5GkZkFyCH-eHyEEVptRJdZxngRb-W1PiPHylogHxxCEPecJRDdj4UbnVFqrEe8pUcZ1x03Un_YA_LAynq8vHGpZgmJMidEfrns3sDGBXN0Gy_Asxf3ZruGwhgmO0PG3oo3_-41wd3xeM2__YhESXj7oA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fb49be0645.mp4?token=fksMqsEzF41YNTDu78fgjx8PSlWeZiVyWk7WHYY51t8Gpvj5lF3jIWHmKeQBxv20Elc6V7TNFSczCs8FkLqCV3zPp2wwA3ozkyRoAI-6bQ7E1BsRn3b-LaRhkb_VgxC5-Lqx34wbNt_p7Y2LlKq3z6EbyjLzd48UQTnZ7gfstS9EoWZJDk6bMxX3Fs46cB5GkZkFyCH-eHyEEVptRJdZxngRb-W1PiPHylogHxxCEPecJRDdj4UbnVFqrEe8pUcZ1x03Un_YA_LAynq8vHGpZgmJMidEfrns3sDGBXN0Gy_Asxf3ZruGwhgmO0PG3oo3_-41wd3xeM2__YhESXj7oA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
مارکو روبیو درباره ایران:
ایران کشوری ثروتمند است. یکی از دلایل وضعیت نابسامان ایران این است که این رژیم هر پولی که به دست می‌آورد — چه از طریق لغو تحریم‌ها و چه از راه فروش نفت — صرف سرمایه‌گذاری در حزب‌الله می‌کند؛ آن‌ها در حماس سرمایه‌گذاری می‌کنند...
آن‌ها باید میلیاردها دلار را صرف سازندگی کشورشان کنند، اما در عوض، این پول را برای حمایت از تروریسم به کار می‌گیرند.
@News_Hut</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/68627" target="_blank">📅 13:20 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68626">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/425aec1f1e.mp4?token=cd-67mLRbYmdC4nQdCPq9YhHNtjgah8Y7xk-TcUSTQEn3yESPFLOwCZv78aIvz8Cc-pxOdVEDyIQ5eYg9wfFmBL1JQQs-mL4C4AY08zJ79vUo9FYlPqbQWSs0lt4ePCdQ2HxLvzfLGC71aZyBFkiYU368eZb1hOoqv0tZ5HzP9fZ-S8PXavY7f4DbA8rNoeoLHf5vEBcQJbA3C4T6UtmMxWEo5vtdQgimhx4W9EVDopBLbjqCVU_7dPwAHPs_jgnSczjaNXSaOyGapwuwJEnmOPrU_UXg52lV9FyX204doVo6avRC7LxkfUjLuC69pe2zGprVt4joH7DhPxP8Kl67w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/425aec1f1e.mp4?token=cd-67mLRbYmdC4nQdCPq9YhHNtjgah8Y7xk-TcUSTQEn3yESPFLOwCZv78aIvz8Cc-pxOdVEDyIQ5eYg9wfFmBL1JQQs-mL4C4AY08zJ79vUo9FYlPqbQWSs0lt4ePCdQ2HxLvzfLGC71aZyBFkiYU368eZb1hOoqv0tZ5HzP9fZ-S8PXavY7f4DbA8rNoeoLHf5vEBcQJbA3C4T6UtmMxWEo5vtdQgimhx4W9EVDopBLbjqCVU_7dPwAHPs_jgnSczjaNXSaOyGapwuwJEnmOPrU_UXg52lV9FyX204doVo6avRC7LxkfUjLuC69pe2zGprVt4joH7DhPxP8Kl67w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
مجری:
آیا احتمال تجزیه ایران وجود داره؟
⏺
مطهرنیا:
امکانش هست ولی احتمالش کمه.
همیشه این امکان واسه کشوری مثل ایران وجود داره ولی تجزیه ایران نه به نفع امریکاست نه اسرائیل.
اونا خودشونم خوب میدونن تجزیه ایران بیشتر به نفع روسیه و چینه.
پس امکانش خیلی کمه بخوان بفکر تجزیه ایران باشن.
@News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/68626" target="_blank">📅 12:59 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68625">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rr9vzrQR-g5iR6_u3iim3Ve9Vr5LzV09-fl8neG05_uKsbhtk--cYDvy4qgBQSBKg9Q0mnP21Tr18GEK3k5tEYGnrIwhwzU23Vh05niWLDmjx0V84St5n10WJ94zbUeTMin3mtpMOP1KVao9VRH-UHX68gM6uCXhZlbZPYp8K-yNJPk7yby-zZspeGALrn_n7UMIHmBw5MDv7mfcNq0QzGhos-JvyorXObBjQ7ZDgK4qsXpTKnWgAlmoDLmINre4FFA-oJmLW3lkvY4s_6A9wo-yaMdkb_9uyROcAy5XkahjixzOKaz6arHMb9do-T2i4KbfZPKj9fKOEiHeQz-jCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
مسعود قهرمانی تیم اسپانیا در جام جهانی رو به دولت و ملت اسپانیا تبریک گفت.
@News_Hut</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/68625" target="_blank">📅 12:17 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68624">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c5ad1a2f2a.mp4?token=bJyerNeJsP27ZSYsOjiF8qK4aml3lyYawl8C63l_ke6EzN9zoTayy205a8RqMEUI0esY8EpvNAzur9HhN1FswDfdnUdYpv_2BITci6vHKS_1H6stzn_ZyVNQze2Ix-xTMJvi1Ykzxh_jHy0_923oGbNnYlg5ZQiTjM5XziDqdhp7lVm56Ntxpp_0BLJrcV6yuA7KIuOWXpqhJhlg1Tn7VSd3nwmnpH1cOsZ-A_I1VgJz2Je8sTSLE7g33XqyCmvtwgtltuLqmftBBMkO194FGHvT9bjH3vYpY9o_F3T9Tdcj6foBmVEvWZ9CiQsHAQBmTipbwGKGHdrU_hczvJMR0A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c5ad1a2f2a.mp4?token=bJyerNeJsP27ZSYsOjiF8qK4aml3lyYawl8C63l_ke6EzN9zoTayy205a8RqMEUI0esY8EpvNAzur9HhN1FswDfdnUdYpv_2BITci6vHKS_1H6stzn_ZyVNQze2Ix-xTMJvi1Ykzxh_jHy0_923oGbNnYlg5ZQiTjM5XziDqdhp7lVm56Ntxpp_0BLJrcV6yuA7KIuOWXpqhJhlg1Tn7VSd3nwmnpH1cOsZ-A_I1VgJz2Je8sTSLE7g33XqyCmvtwgtltuLqmftBBMkO194FGHvT9bjH3vYpY9o_F3T9Tdcj6foBmVEvWZ9CiQsHAQBmTipbwGKGHdrU_hczvJMR0A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
سنت‌کام ویدیو ای از حملات آمریکا به ایران منتشر کرد.
تصاویری از برخاستن یک جنگنده F/A-18F سوپر هورنت نیروی دریایی ایالات متحده — مجهز به بمب‌های گلایدکننده AGM-154 JSOW — از ناو هواپیمابر کلاس نیمیتز، و همچنین شلیک موشک‌های کروز BGM-109 تاماهاوک از ناوشکن‌های موشک‌انداز کلاس آرلی برک، در این مجموعه گنجانده شده است.
اهداف ثبت‌شده شامل یک سامانه پرتابگر متحرک (TEL) و یک پرتابگر پهپاد است.
@News_Hut</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/68624" target="_blank">📅 11:53 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68623">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/60340234e2.mp4?token=PKP4ucWphgWdYy5FwCpfUTsAXkyatjQIj08y54xSYuv8Y073Z6hJsMMIP9jbRnZ_zJJSYxAjUiQPu7CvK0DkAFm32ap19rEJED8zjiMfwcg2r6UOEjRLhfgFFi2xlI-skBMZm8-Uzh49Z2ozLojDeV3LZ8cNGaFINj8BWuPgoPfsaE_7VTRanxSgVWv5Ubc_VaBnPO505xeVWdcSAiIZMYHIjqti-X4fiy79g1Lmwt6yCrV7yT-HagqOSZq0WqS6l8g4WI8sTX43vn9vb1g2B8a9KpbgaG7MRNN17oAwGMTFeALczcW0hNWjLzWWenh7uVQVnlsn1tivhijxdXAL0Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/60340234e2.mp4?token=PKP4ucWphgWdYy5FwCpfUTsAXkyatjQIj08y54xSYuv8Y073Z6hJsMMIP9jbRnZ_zJJSYxAjUiQPu7CvK0DkAFm32ap19rEJED8zjiMfwcg2r6UOEjRLhfgFFi2xlI-skBMZm8-Uzh49Z2ozLojDeV3LZ8cNGaFINj8BWuPgoPfsaE_7VTRanxSgVWv5Ubc_VaBnPO505xeVWdcSAiIZMYHIjqti-X4fiy79g1Lmwt6yCrV7yT-HagqOSZq0WqS6l8g4WI8sTX43vn9vb1g2B8a9KpbgaG7MRNN17oAwGMTFeALczcW0hNWjLzWWenh7uVQVnlsn1tivhijxdXAL0Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
ترامپ در مورد ایران:
این کار بسیار بزرگتری است که ما انجام می‌دهیم. ما کار کوچکی برای جلوگیری از داشتن یک قابلیت خاص توسط آنها انجام می‌دادیم.
حالا ما فقط به آن پایان می‌دهیم. بنابراین واقعاً همان کار نیست. کاری که ما اکنون انجام می‌دهیم این است که هرگونه شانسی را که آنها بتوانند موشک هسته‌ای داشته باشند، از بین می‌بریم.
اگر به آن نگاه کنید، پس از یک هفته و نیم یا دو هفته [از شروع جنگ]، ما آنها را از [توسعه احتمالی] آن متوقف کردیم. اما من نمی‌خواهم از کلمه احتمالاً استفاده کنم.
@News_Hut</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/68623" target="_blank">📅 11:10 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68622">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hVi4uW7x6J6g69-LaYnhYQa12tUpi6VdUwpQSAm7RIdXzMmQTANKOs_M8C2HMq5WQudL3A6q9_J3PPSyP0HMTc3fTdNRYNZW9YRbQagNR5wRDnLWpelKJ6btkYMKAKvdl3AhCNasXghonyZZwED-zJQtG6Dk6-XDJSIU9RyKa-hJM8hmzHQZKteQSFW3Hp0QRdG3DRD4Q24kW0uma886p49bXbxEJaY-EI2NC7nLDP7N7D6n8icGkpBAyVNlPSruWCt6JHZn8W71zMCWjRTnHBJY9PKwUL5YTt5Vm6Si1s2iDCrXFP7WhIe5nyh9wWNLt9V7N2Xiejpk6G_rPliiLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📢
نیویورک تایمز:با نزدیک‌تر شدن دو طرف به یک جنگ گسترده‌تر، یک نیروی نظامی دیگر آمریکایی جان باخت.
پنتاگون روز یکشنبه اعلام کرد که سومین عضو ارتش آمریکا در جریان یک آخرهفته از حملات متقابل کشته شده است؛ در حالی که جنگ با ایران شدت گرفته و ایالات متحده شروع به اعزام هواپیماهای جنگی بیشتری به منطقه کرده است.
این سرباز در شمال عراق هنگام عملیات برای از بین بردن یک پهپاد تهاجمی ایرانی که سرنگون شده بود، کشته شد. این حادثه در میان زنجیره‌ای از حملات فزاینده رخ داد که تقریباً آتش‌بس حاصل‌شده در ماه گذشته را از بین برده است.
هیچ نشانه‌ای از دیپلماسی یا مذاکره میان دو طرف دیده نمی‌شد و مقام‌های آمریکایی که به شرط ناشناس ماندن صحبت کردند، گفتند که ایالات متحده در حال اعزام هواپیماهای جنگی بیشتر به خاورمیانه است؛ اقدامی که برنامه‌ریزی آن حتی پیش از کشته‌شدن‌های اخیر آغاز شده بود.
@News_Hut</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/68622" target="_blank">📅 10:32 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68621">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1ba03b9d75.mp4?token=Tmo_xIc11f1E9JsG4eRog9yFkxFu1bL774aZ8u8N0bHPWhpRIjj7Yat019xR0xKlateKRYUKYDFqiCefc5QXxJQxZKLCZmwbQrxEU12ZFmJ4xConqFmUut1YXEQ57oUh4Knks_I8Ggun-czqBSPZy-7mY6wsHhH3M_wBe6SK1FMSLOaoofFFyy8-_k2DVyaSSoiGlWkqBCchMtALWKk-avdGLY-B10v0s4hnU1F7di-FGbSVXhACqas0ZEv0F9X7EyR3asxyiv3MbW24Rm4jlFVpTeSxCRnzNlBJP_tltHhXFIsv_jUR6PXTu0_lLJGxEngv1O3wtMI6pP6e45KtwikGdoj5DjbkUK_CZ5HgmRi8LJl9MXbejYENyqtiD5MxWSO8dmbQZXsbxRZxHxdu9MBArxlFqgQK--NPkk2Lg3Qv_bl4Sw6sGJ5Gx4zaCO4xb_Cz-Jh-qQ1uoQugNZYl-vw93JJujAbyCt_F32kuMH1u_yBCH9B9q4ncWlfAfGcT-eUFn7uYxcatItNtKM_dVlYdptrqyc7yhLqQkOmkkJ9JG6IStOUYqEd3l07rp1pjMVxp3MRs0fANmWUNfJhKgQSvMNVKBDk1wn-zc4I0UYFaNVQx5QM3caXHHq7XHMtq9ClBTkSseD9VuMTerLY7dnLB2OXTMfLfJD81ZzTdZ5A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1ba03b9d75.mp4?token=Tmo_xIc11f1E9JsG4eRog9yFkxFu1bL774aZ8u8N0bHPWhpRIjj7Yat019xR0xKlateKRYUKYDFqiCefc5QXxJQxZKLCZmwbQrxEU12ZFmJ4xConqFmUut1YXEQ57oUh4Knks_I8Ggun-czqBSPZy-7mY6wsHhH3M_wBe6SK1FMSLOaoofFFyy8-_k2DVyaSSoiGlWkqBCchMtALWKk-avdGLY-B10v0s4hnU1F7di-FGbSVXhACqas0ZEv0F9X7EyR3asxyiv3MbW24Rm4jlFVpTeSxCRnzNlBJP_tltHhXFIsv_jUR6PXTu0_lLJGxEngv1O3wtMI6pP6e45KtwikGdoj5DjbkUK_CZ5HgmRi8LJl9MXbejYENyqtiD5MxWSO8dmbQZXsbxRZxHxdu9MBArxlFqgQK--NPkk2Lg3Qv_bl4Sw6sGJ5Gx4zaCO4xb_Cz-Jh-qQ1uoQugNZYl-vw93JJujAbyCt_F32kuMH1u_yBCH9B9q4ncWlfAfGcT-eUFn7uYxcatItNtKM_dVlYdptrqyc7yhLqQkOmkkJ9JG6IStOUYqEd3l07rp1pjMVxp3MRs0fANmWUNfJhKgQSvMNVKBDk1wn-zc4I0UYFaNVQx5QM3caXHHq7XHMtq9ClBTkSseD9VuMTerLY7dnLB2OXTMfLfJD81ZzTdZ5A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
«سرباز روح‌الله رضوی» مجری یکی از برنامه‌های شبکه خبر، اهل کشمیر هندوستانه
🇮🇳
و پدرش به خاطر علاقه‌ای که به روح‌الله خمینی داشته، اسمش رو گذاشته روح‌الله؛
⏺
حالا این ویدیو از این مجری حسابی وایرال شده:
🎙
روح‌الله رضوی:
با سنگ، تیرکمون، کوکتل مولوتوف و هرچی که میتونستیم، رفتیم واسه تعطیل کردن سفارت انگلیس...
🎙
دهباشی، مستند ساز:
به این حرکتتون میگن هرج و مرج طلبی، یه رفتاری انجام میدی که هزینش رو یه ملت باید بپردازه.
تو به عنوان یه مسلمون که به حق‌الناس اعتقاد داری، بنظرت میتونی کاری بکنی که هزینش رو میلیون‌ها نفر دیگه بدن؟
🎙
روح‌الله رضوی :
اسمش رو هرچی میخواید بذارید. وقتی همه‌ی مردم بخوان یه کار بد انجام بدن، شما سکوت میکنی؟ من اینجور مواقع نمی‌کشم کنار...
@News_Hut</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/68621" target="_blank">📅 10:04 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68620">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">⏸
ویدیو کامل مصاحبه جواد موگویی با عباس عراقچی درباره حوادث یک‌سال اخیر از مذاکرات تا اعتراضات دی‌ماه و جنگ:
@News_Hut</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/68620" target="_blank">📅 09:15 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68619">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SL812iVGJeTKcYQoojuk45XuSBTxaxaOlP3tnRU1qfEkXZ7Np25WzHjXSrgRkWPyG7XnRLMrMvgmQyUi3gpNhWMDpPTPyxuDNxgNwn8MoB4Wo8zTMOH7vB3uQ55qROtA3KC3l4tt83xPS7954xCjzsDNxYLQPZ0E8NNsddcevSdS2_udcMKiUXV2GiWdMgDbawZh6A5a3pSTGQX01iQMpXxcPOCFdHjx9EkwZlR7qiQnJxLFwjdD51ss5gNxN-2-DPIWYCNjWNPHFwE1mmMik-7kjI3C0C2ewUJhKcvyTqxzziQX1900lXJt-l2TjGoYA3FH_c4G0stFbEsmEDd7rA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
آنالیز
دقیق،
برد
تضمینی
!
📊
💵
حرفه‌ای‌ها دیگه حدس نمی‌زنن، آنالیز می‌کنن. توی
Pinbet
، ما آمار و ارقام رو به سود شما تبدیل می‌کنیم
✔️
با ما همیشه یه قدم جلوتر از بازی هستی
⌛
روی لینک زیر کلیک کن و تحلیل بازی‌های امشب رو ببین
👇
🔗
@Pinbet_official
🔗
@Pinbet_official
🔗
@Pinbet_official</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/news_hut/68619" target="_blank">📅 03:37 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68618">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ria_wO7gQJrdCjUq4BXaJw_ahk8fqxBu_t5sAtpPQiFzZ4Zvr7LxwOO0z7LB_On9UonhVlGWKqNyQwZJYF5CvSvmkGylKvSqLDyE-8KKU-nQ7ARMhbWQqcmA1crGDmMQc-yRLwBfL2t-tUNeXbRn8BzrvO83H3lsQP9PCm_uhm6XaAP_OBKkbCMCoJpk0WO0hDpWv3e-difUtivukHrayqBvgLQSdVhhHNGoOt2RN7ogRoDOQpXD49Qwmydzm5fMaar6e5jVHS-AwVvf3TBse5J6snItc5gBWb_aJj-n7SOcy9izOkO6Hq7WfeEpl5HqXB5IEhM1vmlPrNMLVqzsVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک کشتی در نزدیکی سواحل عمان مورد اصابت قرار گرفت و دچار آتش‌سوزی شد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/news_hut/68618" target="_blank">📅 03:30 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68617">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">🚨
انفجار شدید در جاسک
@News_Hut</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/news_hut/68617" target="_blank">📅 03:29 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68616">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">🚨
انفجار در خورموج استان بوشهر
@News_Hut</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/news_hut/68616" target="_blank">📅 03:28 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68615">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a00f692dfa.mp4?token=bAE_uFL-vyrv73ZSFqyTBTHChBpzNNqj5VDkoAWAn2qwluo1bbx4KoJIoRgOfy84XfrW51riBGRfKRUZsxjEkt5TrhiHW37uXf2xj0fkfgbxRPNo30FI_CkBnRqP1Y3xkT4MBMIeNldg6R2zkKaBcL6KYUBiCaWEqPPkUq4XYkX7qNjkah_Bpweyamy0ZxXbDBCok-a1piiell9HfpP3xqKJWPc0MydNcntfmGowAF1ld3VbThGvn9rSajwxHGPrlhpONUnnMZLW6Tn7OpYxqt9yT4tF0eL4XsOgfYuBrpXaMafe2YLaPaJY82Ge3BmLfXnIHI1kN_r2JaiisZayQw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a00f692dfa.mp4?token=bAE_uFL-vyrv73ZSFqyTBTHChBpzNNqj5VDkoAWAn2qwluo1bbx4KoJIoRgOfy84XfrW51riBGRfKRUZsxjEkt5TrhiHW37uXf2xj0fkfgbxRPNo30FI_CkBnRqP1Y3xkT4MBMIeNldg6R2zkKaBcL6KYUBiCaWEqPPkUq4XYkX7qNjkah_Bpweyamy0ZxXbDBCok-a1piiell9HfpP3xqKJWPc0MydNcntfmGowAF1ld3VbThGvn9rSajwxHGPrlhpONUnnMZLW6Tn7OpYxqt9yT4tF0eL4XsOgfYuBrpXaMafe2YLaPaJY82Ge3BmLfXnIHI1kN_r2JaiisZayQw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
پایگاه امام علی در چابهار مورد حمله قرار گرفت.
@News_Hut</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/68615" target="_blank">📅 03:23 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68614">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LWMcCaEbIMB-VKN29VcnMe26v7Mxv5sbEyQJVsLIQ5GqV3Kn3wgLZ-4xMHraFcR1OBUodjly36YvJTfWxr3bo7xswHPLkbqQG_FBs4LHUSpxZkFAurmAhDQT3Vg3dE9ShOZdgmwEqu7fTHwFwF6BoOveXAwlmcuoIvVk8ROMszF0wmTlsj8oPOwa74857Y-5SYNehHg1m362M4wtqnvS3cLysE1wl_WQffx3NId-EIh8IqxFuaPxTBjvkJbZL3gMl0c1b7p8dEHWoQLiJ0sTM1ePT-tJAYKGi04JVaCyezuRXLMdXyhodPuewkG972GHysr4c4mMM-AYO8G-Pmzr7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
ماهشهر
@News_Hut</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/68614" target="_blank">📅 03:21 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68613">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🚨
منابع حکومتی:
انفجارهای شدیدی در شهر رأس الخیمه، امارات متحده عربی، رخ داده است.
@News_Hut</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/68613" target="_blank">📅 03:20 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68611">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/521034efe8.mp4?token=ToRNC5PimQTweMxqDmRIn1tCAF6h5i8jj1_RiXNc6ZjcgT-qZKtA7BeMycneHGpvAI_i1NRSqElQlDW9OEL-HBD2fox-NA2nZ_PCkViex1F2sfXGZr2Hk_it16hcmh4lvo0lXhnRy8ZdK7pfmvyJWp5BXn5mRuee2aQ2nF-UUezp2L8ZtCFSsMInPd6VQ2h4S56gTgFQDhkIqdWHqtVfKlrqmiW1zI3UtXQNN3OmO2sJleXdhSgjSz68WjajEO-y2ZO4BUJMInVqkcShLwleR0wBA-fbEKUloalsKcHT-V0ryA1b62rzOBEAg9dE_k0iXpiChtEJi0q_fOCoWY_VBg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/521034efe8.mp4?token=ToRNC5PimQTweMxqDmRIn1tCAF6h5i8jj1_RiXNc6ZjcgT-qZKtA7BeMycneHGpvAI_i1NRSqElQlDW9OEL-HBD2fox-NA2nZ_PCkViex1F2sfXGZr2Hk_it16hcmh4lvo0lXhnRy8ZdK7pfmvyJWp5BXn5mRuee2aQ2nF-UUezp2L8ZtCFSsMInPd6VQ2h4S56gTgFQDhkIqdWHqtVfKlrqmiW1zI3UtXQNN3OmO2sJleXdhSgjSz68WjajEO-y2ZO4BUJMInVqkcShLwleR0wBA-fbEKUloalsKcHT-V0ryA1b62rzOBEAg9dE_k0iXpiChtEJi0q_fOCoWY_VBg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
وضعیت سربندر ، ماهشهر استان خوزستان
@News_Hut</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/news_hut/68611" target="_blank">📅 03:18 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68610">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/f087874ede.mp4?token=dPXyf93qSQp0yYNb2F8HS9bqge6Uix1AtByap_Aj2C_kz2uUrN-VdM8gMUfSpN2zOFYkHMDOWIKgKOKvCgjDji9OKEK0YIjP1qAdluvtxybdVdRB9kzdejCP8dircu_HoxsUwb5uuCoM9DHDD078d_GVwljPMFSecZVx8tKGP4m8TBmNkIpFfHWOU-V--LfWJbwDRDV8Mt12wQ7PRhAYNBiYIVF8gSBFK0q5_r92G-xGDMgL40eq4Df37zJEiw2S22ihApdZ9O2kSiAeM49EXU8IvbAhPnksx5XYd3BIg6_-x2u8qJ1hX1qZ0SitlhKELzsmsWKqq8cQLDZB-GWmPw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/f087874ede.mp4?token=dPXyf93qSQp0yYNb2F8HS9bqge6Uix1AtByap_Aj2C_kz2uUrN-VdM8gMUfSpN2zOFYkHMDOWIKgKOKvCgjDji9OKEK0YIjP1qAdluvtxybdVdRB9kzdejCP8dircu_HoxsUwb5uuCoM9DHDD078d_GVwljPMFSecZVx8tKGP4m8TBmNkIpFfHWOU-V--LfWJbwDRDV8Mt12wQ7PRhAYNBiYIVF8gSBFK0q5_r92G-xGDMgL40eq4Df37zJEiw2S22ihApdZ9O2kSiAeM49EXU8IvbAhPnksx5XYd3BIg6_-x2u8qJ1hX1qZ0SitlhKELzsmsWKqq8cQLDZB-GWmPw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
منتسب به تبریز
@News_Hut</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/68610" target="_blank">📅 03:16 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68609">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🚨
تسنیم:
دقایقی قبل صدای انفجار در شهرهای تبریز، چابهار، کنارک، بندر ماهشهر، بندر امام خمینی (ره) شنیده شده است.
@News_Hut</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/68609" target="_blank">📅 03:13 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68608">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🚨
🚨
مجدد انفجار در بندرامام و ماهشهر
@News_Hut</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/68608" target="_blank">📅 03:11 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68607">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🚨
🚨
چندین انفجار شدید در سیریک
@News_Hut</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/68607" target="_blank">📅 03:10 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68606">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a6436592f1.mp4?token=EGPg9G4zCM-Yu7jFDD-rKnKw3SJZrYnGUfttgolBLaKdkbMmvbKGDBqbWXFuFomScQURuRfzRBq_TEV0rJWmdPFbhuzUz81dxSZeXFBhh5yCkAEKLu00ymwBzd3pqiEtskgjVFbYuS8BAp_pAaNFSRzE8k0B6-vs8dITnlqkwI55d-nUoyzcHRJF86EWXW_A5k--AkjW5WygRmpyZoH3vf9GU_FMbpM-2YfWBvNq3KJB8U7Uhehntl2znbe3fPoFIakOZ86vCcSfuIbbEQympFkGCF4kmybAlp7EQ1ORY6Iv2d39c3Z5-DXmuQA3qER2ZNjw4W-KxdzVhsu9k1COCg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a6436592f1.mp4?token=EGPg9G4zCM-Yu7jFDD-rKnKw3SJZrYnGUfttgolBLaKdkbMmvbKGDBqbWXFuFomScQURuRfzRBq_TEV0rJWmdPFbhuzUz81dxSZeXFBhh5yCkAEKLu00ymwBzd3pqiEtskgjVFbYuS8BAp_pAaNFSRzE8k0B6-vs8dITnlqkwI55d-nUoyzcHRJF86EWXW_A5k--AkjW5WygRmpyZoH3vf9GU_FMbpM-2YfWBvNq3KJB8U7Uhehntl2znbe3fPoFIakOZ86vCcSfuIbbEQympFkGCF4kmybAlp7EQ1ORY6Iv2d39c3Z5-DXmuQA3qER2ZNjw4W-KxdzVhsu9k1COCg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
حمله موشکی آمریکا از مبدا کویت
@News_Hut</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/68606" target="_blank">📅 03:08 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68605">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🚨
خبرگزاری مهر:
یه پهباد رو زدیم سرنگون کردیم.
@News_Hut</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/68605" target="_blank">📅 03:04 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68604">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🚨
شنیده شدن صدای چند انفجار در بندر ماهشهر و بندرامام
@News_Hut</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/68604" target="_blank">📅 03:01 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68603">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f2e2ba6741.mp4?token=jn8PVodU7XsPBaUsSPhSaOsCx3YwFXiRW-D-z2OrfxzgVbC2IrwZBwzIraQy1lAST7D_U-DQdDPLemQnkl9P7solZXcmaQRrL9ZjacJw0qkzWf2grAx7zwqvB5D9BHyRmJKf8XyT3OBrA9oFTZwKXHGJrmHHEcYEbHWm8vzuM1tATZdjXa8SfUd9D8PGrFj6a9zLKdAsFSYbfsDRxK6eytXr6iUziyQHh44pqB1u1Olm9HdpcgxEgsXTUiriI4YdEGHsQQfBexPAkotAl3RfyovbrvGGSE23HoE4Mhazp-yMNSIc4cHJvxqigiVYvcLCIkrtFOoSn8lch5S24Rx3pA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f2e2ba6741.mp4?token=jn8PVodU7XsPBaUsSPhSaOsCx3YwFXiRW-D-z2OrfxzgVbC2IrwZBwzIraQy1lAST7D_U-DQdDPLemQnkl9P7solZXcmaQRrL9ZjacJw0qkzWf2grAx7zwqvB5D9BHyRmJKf8XyT3OBrA9oFTZwKXHGJrmHHEcYEbHWm8vzuM1tATZdjXa8SfUd9D8PGrFj6a9zLKdAsFSYbfsDRxK6eytXr6iUziyQHh44pqB1u1Olm9HdpcgxEgsXTUiriI4YdEGHsQQfBexPAkotAl3RfyovbrvGGSE23HoE4Mhazp-yMNSIc4cHJvxqigiVYvcLCIkrtFOoSn8lch5S24Rx3pA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
حملات آمریکا از کویت به ایران
@News_Hut</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/68603" target="_blank">📅 02:56 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68602">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hAvN-wd8csWaMXDT-eg5n0lXyPsuWy5L-JxcsGXLE8GiM6u2UD3Bk2pIGGDXPvjEl4c60W97QxtbskA8AMP36YQBF2K95J642LAdt8z294xVs0bpEZbyVMi0mnKUQrGHQeGlmarGzk9XO0pPdJzkmGQOXex5kFl8TXz2kZ5y64IcOp059mMK_mTCinnc_CYK3-kp4mwXhV_k-PkCAHxrfz2rPFs1_zJVH8H0QeeS5w0aE754-EcXQhVNTaAaBBx23j5_rI4lgkmZUVJ41Jy341uoSNmDqXW2ZqacZ5Or2Q7ByoBCJcT2w7XIdmgq-yRabBc8CT-A8lJUczPFa-M26g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
سنتکام:
امروز ساعت ۱۹:۰۰ به وقت شرقی، برای نهمین شب پیاپی، موج جدیدی از حملات علیه ایران را آغاز کرد. این حملات با هدف تضعیف مستمر توانمندی‌های نظامی ایران که برای حمله به کشتی‌های تجاری و دریانوردان غیرنظامیِ در حال عبور از تنگه هرمز به کار گرفته می‌شوند، ادامه خواهد یافت.
@News_Hut</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/68602" target="_blank">📅 02:52 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68601">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🚨
🚨
چندین انفجار شدید در کنارک
@News_Hut</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/68601" target="_blank">📅 02:48 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68600">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">🚨
🚨
🇺🇸
#فوری
؛سنتکام از آغاز شدن دور جدیدی از حملات آمریکا به ایران خبر داد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/68600" target="_blank">📅 02:47 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68599">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🚨
🚨
خرم‌آباد چندین انفجار
@News_Hut</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/68599" target="_blank">📅 02:45 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68598">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🚨
🚨
انفجار در بندرامام
@News_Hut</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/68598" target="_blank">📅 02:43 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68597">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c3c5e9c78c.mp4?token=e4dd76Y7KaLNOKRnwOqjCVIFiH-k3YqwIbrqIt1NmVX8norWtxQrmunXS5EXgo4oTCC14jrv7M7l1SQKmkhut7SjlivaxQ-CJMV5fbgRbg54HNUy6rcJIM-ScSUN5dWcd8O2lBpqXR8aj6zyCZEWCvn6stshe9N0xfsWUgODMz7_9Z7Zbzso7VGDLYRp0auRHEEhCWX_-1bYqtIWYtJn_rSyyXjSWx1uHCsXhO4SIsc-IL8hC76U-C4_5gMPBnGFumXBqXXBCsO0NU__l883GYQgkkTnLUcSZ7_dwGNEwrM62f80IGBXhVKU4X3qEEyZ-WnprJiPY_K7Y4pympwr4Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c3c5e9c78c.mp4?token=e4dd76Y7KaLNOKRnwOqjCVIFiH-k3YqwIbrqIt1NmVX8norWtxQrmunXS5EXgo4oTCC14jrv7M7l1SQKmkhut7SjlivaxQ-CJMV5fbgRbg54HNUy6rcJIM-ScSUN5dWcd8O2lBpqXR8aj6zyCZEWCvn6stshe9N0xfsWUgODMz7_9Z7Zbzso7VGDLYRp0auRHEEhCWX_-1bYqtIWYtJn_rSyyXjSWx1uHCsXhO4SIsc-IL8hC76U-C4_5gMPBnGFumXBqXXBCsO0NU__l883GYQgkkTnLUcSZ7_dwGNEwrM62f80IGBXhVKU4X3qEEyZ-WnprJiPY_K7Y4pympwr4Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
چهار انفجار در سایت موشکی تبریز
@News_Hut</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/68597" target="_blank">📅 02:42 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68596">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">🚨
🚨
صدای چندین انفجار در تبریز شنیده شده.
@News_Hut</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/68596" target="_blank">📅 02:41 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68595">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B4wWhrRQ4iUupYckoTt_UvqqFJMhxNXoCedWqSjRGdanUbtgMFyDHsREFojhQVlU1aTXO7oWZBPnpyD9tjjqsnZ_KpXodQnWwdPJxukp1HvhE6Jihq3jheIdx9m2uZGHbrpYDBJ1FwK5CxCat8aBI1xTzpv_7sPO8Gqg_raYIpEI1mAnYbejTiHjzUhtda8_v5e3ygztY8yC6sDCrbpd9tvCPzzcRuU1-QciiyA6EiWOYN9itXQVUYhn9YRpXOZTj8wi4_fe9r1Z0Xe_DmHr8c_kd5d0I4vGldb-LilIyx5SEpRsHFCA1SmDbcO_EiRC2ys07-ThEv2lQpUefXNeQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇺🇸
ترامپ بعد بازی:
از دو تیم ممنونم، بازی زیبایی رو به نمایش گذاشتن و تبریک میگم به تیم اسپانیا.
همچنین ایران سلاح هسته‌ای نخواهد داشت
🤣
@News_Hut</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/68595" target="_blank">📅 02:26 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68594">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/10cd1a4acc.mp4?token=LWEvt_U1F9JkOqlYkvSlOBPYPaN-eHZbY00pnQu-s62jQfVpRKXpC1Y7hi9kThLU1cjVtumYqDJCuI-z1p632HOPNYQcEIhw6gUk4wZtMYDXtgtFMshFcdBUt3MTDYYmzcWI8rA4wMdOl6l8kE36RK5qtGGHP3YrEiinTzWhuOepldpgjHGmyYcNs0dUujc_rL99eP53qGEffIRoF6yNKpywEW_AG5d8AFWCs9tPDsBixH6mkifHEoX60Rqv8BXbY3e1H00D0WN48GaiHexntQmq3KqSmpX5-y8Wi4jjECVhxwrIm1NK-_mTxURiWxqi2CsbacpIkONFgTo4f5awlw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/10cd1a4acc.mp4?token=LWEvt_U1F9JkOqlYkvSlOBPYPaN-eHZbY00pnQu-s62jQfVpRKXpC1Y7hi9kThLU1cjVtumYqDJCuI-z1p632HOPNYQcEIhw6gUk4wZtMYDXtgtFMshFcdBUt3MTDYYmzcWI8rA4wMdOl6l8kE36RK5qtGGHP3YrEiinTzWhuOepldpgjHGmyYcNs0dUujc_rL99eP53qGEffIRoF6yNKpywEW_AG5d8AFWCs9tPDsBixH6mkifHEoX60Rqv8BXbY3e1H00D0WN48GaiHexntQmq3KqSmpX5-y8Wi4jjECVhxwrIm1NK-_mTxURiWxqi2CsbacpIkONFgTo4f5awlw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💢
🏆
لحظه اهدا جام قهرمانی به تیم ملی اسپانیا توسط دونالد ترامپ
@News_Hut</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/68594" target="_blank">📅 02:18 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68593">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e5ecf5e7ca.mp4?token=jvW1FbBiPoUNFR6QdCNyRerSe8GBgzAFTUrJCDZEXs7a5Usc7Iu8c6WQaOPVmd1e3UAuQI-66rEC1v7vWsvwzYBjx1W7jv9Q5pG26Eb28E10tgLRJBvKUzWCi5iPvhGqKxsj2Whp6srqHOSx6rGVvAKU-JZqhJAFOkCMYF7uuwexAdjsBTPHZtfCx-pCs7MRGLmf9uuZ2WIzbnuLtGsbtsO0Z7UGjmecOsRMK-OyLBEXFFbH2ushdaA4w1zpM3Q0dKi31VeiKDjc17CtnGt5qz_JqO0DQtlxR8U9nTvQdkwqCXfo-CDN-fz6zWgvyiXehhNyV4x5YmTadMA-lhm29w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e5ecf5e7ca.mp4?token=jvW1FbBiPoUNFR6QdCNyRerSe8GBgzAFTUrJCDZEXs7a5Usc7Iu8c6WQaOPVmd1e3UAuQI-66rEC1v7vWsvwzYBjx1W7jv9Q5pG26Eb28E10tgLRJBvKUzWCi5iPvhGqKxsj2Whp6srqHOSx6rGVvAKU-JZqhJAFOkCMYF7uuwexAdjsBTPHZtfCx-pCs7MRGLmf9uuZ2WIzbnuLtGsbtsO0Z7UGjmecOsRMK-OyLBEXFFbH2ushdaA4w1zpM3Q0dKi31VeiKDjc17CtnGt5qz_JqO0DQtlxR8U9nTvQdkwqCXfo-CDN-fz6zWgvyiXehhNyV4x5YmTadMA-lhm29w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
لحظاتی از اهدای مدال نقره به تیم ملی آرژانتین توسط دونالد ترامپ
@News_Hut</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/68593" target="_blank">📅 02:10 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68592">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/067eca16ef.mp4?token=nTAsRNnI91RVnFXTrjzzg4TGzXUMhxlYNRlmvTMWyUrolGdPMeTk2YMvj1c3dmOao-0Gy67n00CYB0BAg91e62YG8Y3fbOwzrcpzhRY6k54bR804JmJZvlMRrsWY5eYVeQRdQwH5xQfzvCivMtCHNKFLBToYDTwsGq5Gw6mwzoS2tKx0axLE2h56IXC4ma9e9el1COz9ex9XbotyTlGuyR68piXw5VGK2lM_Q8L4v9zHzKyn8T4nqzEVzoqm5HUB_TnlVA8vLlXYbNYoU60Ru1mlUR00OE_NvolEGAEhT5wxggv2O2rp-pfVERogVoE6AI9VwzntqwIXYdAwODtxcw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/067eca16ef.mp4?token=nTAsRNnI91RVnFXTrjzzg4TGzXUMhxlYNRlmvTMWyUrolGdPMeTk2YMvj1c3dmOao-0Gy67n00CYB0BAg91e62YG8Y3fbOwzrcpzhRY6k54bR804JmJZvlMRrsWY5eYVeQRdQwH5xQfzvCivMtCHNKFLBToYDTwsGq5Gw6mwzoS2tKx0axLE2h56IXC4ma9e9el1COz9ex9XbotyTlGuyR68piXw5VGK2lM_Q8L4v9zHzKyn8T4nqzEVzoqm5HUB_TnlVA8vLlXYbNYoU60Ru1mlUR00OE_NvolEGAEhT5wxggv2O2rp-pfVERogVoE6AI9VwzntqwIXYdAwODtxcw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
دونالد ترامپ به منظور اهدای جام قهرمانی به تیم ملی اسپانیا وارد زمین مسابقه شد
.
@News_Hut</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/news_hut/68592" target="_blank">📅 02:06 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68591">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J-HkZ73LUinMqwO0KQeljL-3AQWfh7TFcZYRClu8ZYmeb9mTjLp_scP13ws0Foo-RbxXCgb6Pk4NCnO1HBOBlv-NxZ5bZmtC4DQ50WCumxQgp4Jj-T1rsutEve2eK482qtN6VqEUnSsVlH5MSzFkjz6cMB07ab1pbb8NHNKKl_rdEEn_R21VXQOR4dCDD4OnwDpksHFPgOB6ssmeUS0uiharrBKOVbLS2hU_gqA76qWVWgP9SxCwy8PlfR36AvbvetWvDayia_lDDPrq5LQFZd7j0Nqn8ukVi2hkp5pp3aBazqEHrEXySundAzCcucAKqm7t5BWm3bRBuEaah3iUaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
عرزشیا به زودی:
ژنرال فرنان تورِس، از جمهوری اسلامی اسپانیا، گلزن در مقابل آرژانتین
😟
@News_Hut</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/68591" target="_blank">📅 02:03 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68590">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RuhTSeaI5hFvpyFEEvlF33diMD83_cBkAOmjQCslTmwkxhVHd7h14g1kj5O2HZwhXL1OQfuzEHcAOEbvyTnpddnbbj3OuoUY_rV1N8-BRdYGrRURvbjl2u4YJzO3bjMPRSGsk5OBTMNw9y32yyBMGErWwy61KNQi6o4j7AFhdZDiM9Jt9sgVsuJpCj0c_BJddwlSLHJSX3VqqtI6dihOzf371dF9NhAwUFNP_30orDICCzikLEozEuWwv9-1F53EnEzElfuHWnwyi388ZvhnWehoiAX4HaqxXsUDm5i3Tjk-5PEJRMREFXBSJjea0tA1FYnNhxNy8fGVA0L3d_iqCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
ترامپ اومد تو زمین
@News_Hut</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/68590" target="_blank">📅 02:01 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68589">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">امشب سنتکام نمی‌زنه یعنی؟!
#hjAly‌</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/68589" target="_blank">📅 01:59 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68588">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/agciXSGYyzgq-FP5qCZl7ByLTgzZTtix43bxIFfaKZOsAyUH6bka9LBpppZZ_qmIc5dzX-PtPXtkOiXftLlDU8cQlTh2qzK4zqv3wuZIeeZyZj9m8d41kzAEsoGZ-kRHVQCezxPBDm2IR4IeE819ovG3HraT3HbmV1RCDdRZc2-TVBx61p7UU5wnmRbvBNhY2O_u4n7lYVmGq6FCwvwlKSuMYRIx9JXu5crLEveewT6rdvYMJLqMmK4DMAgKmacFH8QDOfnYEujJU7Kpb0k-uX2e78Ax5L6FczeMrV36dGiOjAbPHRveKQBMRdava27WCf8LgBeRkQyxrCnxc7YYsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
آقا تموم شد به راننده بگید حرکت کنه.
@News_Hut</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/68588" target="_blank">📅 01:54 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68587">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LzQrXWGzX7DDURxak8YVODtQ71rPQmzX8C8hCIckrqVDL5ra6YC5lPsfVQFhvxaHFXfy_omvl-nOqMvh0oVmysZi1OJ4FcG-1h0unW-KQ-sHtSaBFWlgASYH6SIFsITjLlx-Dueb_6_k4vZ0eoY8DGMGhOsY_hE7wXpMAeH2xSGgr8mGEFk5RL1X3MTgIFF-qhuGEKHJtSOSn-seOhwZDT8RrewQtnWmnIcEW8n-MZRCFpm-ezXXsxjDUAEAdboj5mh7-XLHcIIUhWLqQheRsbWaSxdVQl-ZLVpjPFcJdfCAV5P9DdYc92B92kryf42sCww4e4LJzuEOJijidHlhiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
جام جهانی 2026 هم با همه خنده‌ها و گریه‌ها تموم شد؛
قهرمان: اسپانیا
🇪🇸
نایب قهرمان: آرژانتین
🇦🇷
مقام سومی: انگلیس
🏴󠁧󠁢󠁥󠁮󠁧󠁿
آقای گل: امباپه
🇫🇷
آقای پاس‌گل: اولیسه
🇫🇷
@News_Hut</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/68587" target="_blank">📅 01:47 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68586">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f2-XYzev-bRYzd7KzHBAwMim7lVvYKoO6d1aS3PI_XrkecdMypIhebLGWlqXnoQdtermPIdPOacnyCTCvdXySueBxLq_hS1KIUJeIb-gK8NKnY4EiyiAIacpStO9U6mMf2FX315BXR6bUa6gkMoW0ROsaIrFw4aj7PsS8_qyaaQyDZbDDYDxLqby278r58pLnWn5GUPfNJVWM5i2gfxntcqcf6LULGmOrE327TFP5O3gUwsnfXzqUN0yTfMUiTyEd4RSRbro_gYOtRj8w2MgCvnf1YztmXi5KpPhsOmBc7w8qDHl4AWl_4q0BRkWYaPIp4DK4BtBgaYaZMRh98WM6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
💢
🏆
تماااام؛اسپانیا قهرمان جام‌جهانی 2026شد.
@News_Hut</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/68586" target="_blank">📅 01:32 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68585">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">اسپانیا خیلی بهتر بازی کرد انصافاً
🙁
#hjAly‌</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/68585" target="_blank">📅 01:17 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68584">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🇪🇸
گل اول اسپانیا به آرژانتین توسط تورس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/68584" target="_blank">📅 01:16 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68583">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🚨
🚨
گل اول اسپانیا به آرژانتین
@News_Hut</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/68583" target="_blank">📅 01:14 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68582">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LtVLML-nyAkSdRaNsU5G0LQxmxXrhbwQyoDoFr7PlVxZ_DaTbEcb-bc054WD9IFaRvPmOaIxTEeov57Rscfp7vkC8QUz0y8-G2AZtPElD-RBYHbxoDFEey_LjW0bQT4Ywhev_bufXQQY-v6ECQ6Z6nNbnpq4wkUmWRqAUkXIIKG9Tc_wQHcIHv5QWT7YATip93qnwuMVeNsJaJbHeqCQX4gkTnV_L_iz_SMh-LfyAsPPwhBuJX9PXrZAlM4j7_L1zhROXpm9-pZ7474IHpuvhuGQFp8w-iesdla0LeL9WZrdoNhcD8GMI3Aru-XXKUCvP-3GkwBZUXCe14roCPOcYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
پرچم شیروخورشید در ورزشگاه
@News_Hut</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/68582" target="_blank">📅 01:01 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68581">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">بازی که رفت ۱۲۰ دقیقه، نیروهای سنتکام هم دارن فینال رو می‌بینن، حملات امشب، نیم ساعت تاخیر داره
😁
#hjAly‌</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/68581" target="_blank">📅 00:56 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68580">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🚨
آرژانتین ده نفره شد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/68580" target="_blank">📅 00:41 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68579">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🚨
آژیر خطر در بحرین به صدا در آمد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/68579" target="_blank">📅 00:40 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68577">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a67fe75354.mov?token=SzJ_779NXnNTIqLsoINBBbs4_jpY8yKcyPhGpBResKWfgZT-P3kg40w6prgWFAvwdvQU5eIRS5kU7y08mAIxBHp5kYwkjzKVYEO9U2HOQqtWQec4l0gYSAI1EgxE5eeVAkl-o2mCWUFKxSftHRdCZA-O5KfH3so-QROEGbkiRevBT6bd60QytSrw1UfbMyx2TA5JaSmF5F3zaGf87kThC87EBe2bUXog7PnAmNzvX_MEjKrK8YYmaXor7RLRpn5uMtifJSzFpdgvcYFHJFR2m4YqXyMHAj3OnKtDlFvixTdHIyJHMjmN8vqepMv_93xYx2PSRs4TZbs6VbDPK6MHdQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a67fe75354.mov?token=SzJ_779NXnNTIqLsoINBBbs4_jpY8yKcyPhGpBResKWfgZT-P3kg40w6prgWFAvwdvQU5eIRS5kU7y08mAIxBHp5kYwkjzKVYEO9U2HOQqtWQec4l0gYSAI1EgxE5eeVAkl-o2mCWUFKxSftHRdCZA-O5KfH3so-QROEGbkiRevBT6bd60QytSrw1UfbMyx2TA5JaSmF5F3zaGf87kThC87EBe2bUXog7PnAmNzvX_MEjKrK8YYmaXor7RLRpn5uMtifJSzFpdgvcYFHJFR2m4YqXyMHAj3OnKtDlFvixTdHIyJHMjmN8vqepMv_93xYx2PSRs4TZbs6VbDPK6MHdQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
گویا از قم موشک‌ پرتاب کردن
@News_Hut</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/68577" target="_blank">📅 00:21 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68576">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i_aVG4sWa6_x8EooFSvGcXFhWuRWHRJm4dKa-kkG99P2cc8TxHkmrTLuMRPmE5ja4LkbGbnKbB9Cd09YcnNGIavMC_2oESectz7q2lbUof5qdbIJim9V84NRJLszQx6LM91dRPrplFVKYt7-kZ02M46KJY_XamauYbZkFDWMYrbGnGPjGeTc0nMw9ApA79asj5d5FIntEJDow3-syhMgjKoQCEJsifOHwRcAg5Zbpkg46ZiergA7UTvrJVRCaQ6SgKiWLDlRIZ3fITW23xo7SUAejSpqITJoj0xomAGHO-nkYHfK8CZogSp8mNNi2Ic2yuCFdh_yaTxMybVDyNgyOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عمو بیژن تو فینال
🔥
@News_Hut</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/68576" target="_blank">📅 00:16 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68574">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🚨
🏆
اجرای کامل شکیرا در بین‌ دو‌ نیمه
@News_Hut</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/news_hut/68574" target="_blank">📅 00:13 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68573">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🏆
🔞
🇱🇧
حضور میاخلیفه، پورن استار اهل کشور لبنان در آمریکا برای تماشای فینال  @HutNewsPlus</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/68573" target="_blank">📅 00:12 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68572">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🚨
🚨
🚨
انفجار در ساوه  @News_Hut</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/68572" target="_blank">📅 00:03 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68571">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">🚨
🚨
🚨
انفجار در ساوه
@News_Hut</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/news_hut/68571" target="_blank">📅 00:03 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68570">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/416fb2b432.mp4?token=uD7n51oxI7jt3eMZ0ZLgdz8eYd7pbFMa0SJfYPGoSL-cp1POjcTozqMdINfA3tYjzmOeG9AtIb0TPtaxg2rLI7buFb9G-M3jrPFNbUOYwMKG9lnVTVJc8wcMNrvzD-T4cR31p80MmDXwk2NJKB6-TmzJz-3pAdC81RwqCYrRJwudUvpfPbpuFC7Rfb-6C68we-mN7Vn156wzzWfDTm_QDW0-CdXlb7d_0KhEqtJONby2uiiz6vI-RAg16NFe5iR3A_syhigSHoNr5rgT8mkLNqmOAOMePJuLoZAx6WH9TG7goA-qVzr9V3NdIwzmMWaHnRN7xtUbLDs7PqozOSj_KQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/416fb2b432.mp4?token=uD7n51oxI7jt3eMZ0ZLgdz8eYd7pbFMa0SJfYPGoSL-cp1POjcTozqMdINfA3tYjzmOeG9AtIb0TPtaxg2rLI7buFb9G-M3jrPFNbUOYwMKG9lnVTVJc8wcMNrvzD-T4cR31p80MmDXwk2NJKB6-TmzJz-3pAdC81RwqCYrRJwudUvpfPbpuFC7Rfb-6C68we-mN7Vn156wzzWfDTm_QDW0-CdXlb7d_0KhEqtJONby2uiiz6vI-RAg16NFe5iR3A_syhigSHoNr5rgT8mkLNqmOAOMePJuLoZAx6WH9TG7goA-qVzr9V3NdIwzmMWaHnRN7xtUbLDs7PqozOSj_KQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🏆
اجرای عمو بیژن
@News_Hut</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/news_hut/68570" target="_blank">📅 23:50 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68569">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HGU5pKzne9x5ywJrLNSnPbzJ_oSKYldup4lc1RovkNQglxnbdlQxkfIAHuiMhHeTPfP4tJ6p3MqYvPBaFTGk7Rw22dN4ksa4wDX6VifABRcbQtdJIMCoo0ZChUDA0QdceDLR1GZv9lGV_09ObSGdFWihurnfnHg1wWFgGxwJ_N5O28iOwbf_rga4Q2Nz4MptCUAiDNf5LXWADJ1Y_c72Cce0qX5BVlMv-Z3qCqB9Kt8ANwscncgAEHIGUOVCRsUbT-t_3goYgr6O255MNnleP3VXoR_ZuIy0pDlhvpp0qrJqcNMWybRZqZ6-lR2dxwDzeNYTSmTyebCVBhoVJ7ke4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اوه آرژانتینا دارن کامل لخت می‌شن
🔥
👀
🔥
🔗
مشاهده ویدیوی لو رفته از دختر آرژانتینی
@News_Hut</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/68569" target="_blank">📅 23:50 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68567">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mBwn09ayqhS9Z6U9wivjWcbNSM9qUNlixd1pwCr2uzD1z1v0hSry7c66YjBtkPdy6Dx3fG6EbmhI76t3rotK6Onih0IY8RNjQNBJWYx1PlmRXjx71PWjumDKH9e6Agive8--g7SDU8kmIpepEI-9OC2HIcxD8qbp4m2R_2eDPScqlrvaSAL33SSuEA59kSD147PMst1AjBIdpr5MjM_27iyqiJpoDcysyo6uZM5EfxPFEXMEjmjERzi8dLoBg9UI0SS8ljtkcEluJxxycc0xjlHE6uYUKx2beaU7_TOBjYk6LFYS2BmjkG_3VlkqJ3MKLKLBJTA3LZQjjyAkekOC2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
فرماندهی مرکزی ایالات متحده:یک نظامی آمریکایی در شمال عراق در تاریخ ۱۸ ژوئیه و حین عملیات انهدام کنترل‌شدۀ مهمات عمل‌نکرده‌ی به‌جامانده از یک پهپاد تهاجمی یک‌طرفه (انتحاری) ایرانی، جان خود را از دست داد.
روز گذشته، فرماندهی مرکزی ایالات متحده (سنتکام) خبر جان‌باختن دو نظامی آمریکایی و مفقود شدن یک نظامی دیگر در اردن را، در پی حمله ایران در تاریخ ۱۷ ژوئیه، اعلام کرد.
پس از یک عملیات جستجوی دقیق، نیروهای نظامی آمریکا امروز بقایای جسدی را که هویت آن هنوز مشخص نشده است، در محل حادثه پیدا کردند.
فرآیند بررسی برای شناسایی و تأیید هویت این بقایا در جریان است.
در رویدادی جداگانه، یک نظامی آمریکایی در شمال عراق در تاریخ ۱۸ ژوئیه و حین عملیات انهدام کنترل‌شدۀ مهمات عمل‌نکرده‌ی به‌جامانده از یک پهپاد تهاجمی یک‌طرفه (انتحاری) ایرانی، جان خود را از دست داد.
نظامی دیگری نیز در این حادثه مجروح شد و همچنان برای درمان جراحتی سطحی تحت مراقبت‌های پزشکی قرار دارد.
سنتکام به احترام خانواده‌های این افراد و تا زمان تکمیل مراحل اطلاع‌رسانی به آن‌ها، از انتشار جزئیات بیشتر، از جمله هویت نظامیان مفقود و جان‌باخته، خودداری می‌کند.
@News_Hut</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/68567" target="_blank">📅 23:33 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68566">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g0oovhkuvRFZl8ggyxMeeVQVa8NH2K9eJk2N6gqz4pFo9ugIqVpo1B3LSjIC6kGWP--f_iVRsUKzak3Mx9caRd42YFu1KEd-aiIm3sgbK1vk8kR9z5-vlh6rx0NUFBcCVQ8Vrav2QcQacIUwrNqiSNN2D0MaZW_P0U3own60sG_53vwA7g3V6MkznSSFUNTZKl25Fsh3sU8Qtfsd7kQShQvH2WqP9vnJFOeoPE_qfayr886jv4kjPsZ6bPzF5ir9jp9TG1GRJsGJbRb_N41WnP1Xjtu6-66nkDkafhtpJYbQkXA2w6R_SZdgCJNk1m1QuWUnUfvQlk4m3TjrQK_lhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حالا کاری به کریس‌فن‌ها ندارم ولی هرچی چپول، عرزشی و فلسطینی‌فن توی دنیا هست امشب طرفدار اسپانیاست، به امید باخت این تیم کثیف و سراسر چرک #hjAly‌</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/68566" target="_blank">📅 23:27 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68565">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ce3cfd8ff5.mp4?token=oOGWvJGT6z-NJSodJsB8gZiWpWHpPfo7fbi-akxHO5wd-hIe7P4BP1hT0kD2oyei4lF87mMzrinRpfT8A8pnfVh-qmJsTrIW0IPkjvzbPpJsjkS6mmluKOxtx6RabOg-HtNNPSOdeOvqqd2LknyK-F_hkX7_nx1Tt-8cFOjlcX5awaENVRaWInRPfPCFNJL2q2lf0wqd5p_peccOwmdIMDu6qVrEY2TBp_5n2ExDJNiIW6g0F4_3PPQn0E1mAmnqKw3B-Vo93xotyFayRUar-z4TReXR3nd_zDVkz8kta0aBKR45fw-slRMrVJjfkB2og4kyKFoYLD6OKH2tR-KeGH9XHXwXUnYbvrsFQC6V3d-fp_Zs65vA7BWt3ldNpvGRZcFr4yi6LhGk4svc6Mxv_0HpTFZzHgKPhF5fpd_LDVnqhsHl1BXVrZaejfqtY-dRE_biZmMgiQrzw3pmCesm1VVn4LU5ui3PF5641yEO10AZ0f52NTc2iGsRGn-TupJ-vRu_TPQCyac-aCJvkd3GuBEd9hnzqCXIfZ3V2StiDWolvwTo1qxlbmVBtseEHhvHJuyv2RmxnaoeTKUQ3lRBSb-3ag03OJ5XiVCWVHpEUZ8hR8xlF4zK6TDZyn_QdLppwKzJlxhh6y9yVnR8a3joW7osW-aD0_n3lHj6mFCScWk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ce3cfd8ff5.mp4?token=oOGWvJGT6z-NJSodJsB8gZiWpWHpPfo7fbi-akxHO5wd-hIe7P4BP1hT0kD2oyei4lF87mMzrinRpfT8A8pnfVh-qmJsTrIW0IPkjvzbPpJsjkS6mmluKOxtx6RabOg-HtNNPSOdeOvqqd2LknyK-F_hkX7_nx1Tt-8cFOjlcX5awaENVRaWInRPfPCFNJL2q2lf0wqd5p_peccOwmdIMDu6qVrEY2TBp_5n2ExDJNiIW6g0F4_3PPQn0E1mAmnqKw3B-Vo93xotyFayRUar-z4TReXR3nd_zDVkz8kta0aBKR45fw-slRMrVJjfkB2og4kyKFoYLD6OKH2tR-KeGH9XHXwXUnYbvrsFQC6V3d-fp_Zs65vA7BWt3ldNpvGRZcFr4yi6LhGk4svc6Mxv_0HpTFZzHgKPhF5fpd_LDVnqhsHl1BXVrZaejfqtY-dRE_biZmMgiQrzw3pmCesm1VVn4LU5ui3PF5641yEO10AZ0f52NTc2iGsRGn-TupJ-vRu_TPQCyac-aCJvkd3GuBEd9hnzqCXIfZ3V2StiDWolvwTo1qxlbmVBtseEHhvHJuyv2RmxnaoeTKUQ3lRBSb-3ag03OJ5XiVCWVHpEUZ8hR8xlF4zK6TDZyn_QdLppwKzJlxhh6y9yVnR8a3joW7osW-aD0_n3lHj6mFCScWk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
🇺🇸
پرزیدنت ترامپ و بانوی اول ایوانکا ترامپ در کنار اینفانتینو در بخش وی آی پی استادیوم
@News_Hut</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/news_hut/68565" target="_blank">📅 23:23 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68564">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rPpIE1GyHkESZMWD2p_tPaiH8hPeLEkQY6DrekksJPM-gH-rh3sARi8EUSj0KUj0o_zi1SiQumYtODO-1ATEYjkfVbWbGiJnwQVoPPJppNVRT-GaoU_NqRRwJzNku-AcwbaXcS5MYjIP7bGwdp8l2AhxrwutiphgexA0gnfi2mJdVc0IY9CGAutbnxqI29K0Zh8fYJs3sEC2Ibg7JQjoR8xJHy6cwVIS-6IJNIv7Cns-o_68c_ndZTV6E8S0K9yo9-amx6t70RcEoi7JEVsE3b44pEuSZRQvgoE3QGruYMTQCw5Jk2uJETScWuPEYQ-Q_-WqQYR72qz08o3KO98uPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇺🇸
گزارشگر صداوسیما : هیچ تصویری از ترامپ کودک‌کش و جنایتکار نشون نمی‌دیم!
@News_Hut</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/68564" target="_blank">📅 23:22 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68563">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">حالا کاری به کریس‌فن‌ها ندارم ولی هرچی چپول، عرزشی و فلسطینی‌فن توی دنیا هست امشب طرفدار اسپانیاست، به امید باخت این تیم کثیف و سراسر چرک
#hjAly‌</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/68563" target="_blank">📅 22:33 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68562">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EbelFlGY7WM-Xq1Cn2BUXGzHtvbyUfuLrDIMWxzNnR6kNrUE9hreGGcI-YGbGvRITJOXYkLnbjSyijrU7qRth9PFyqxVDK-RuPldVgitNa2dNjlCU3qg2M3qnqyoNsbrUwvUTFpK0ICItzm9eGekBkHMb__xz-n0JzCAttmu51YWjOSs6bHXk0D2nrfG6zEoAPqkdj_yBlqX7YBPnwMUoWKsVI1abySRBA0Ze4kPc4EfL0UdbsPp3Xanxp7dUGeM2jqXekizpQ1gp9fafpm0B4vgSfA75biTGTgBxhRXMT1IBj9cKcZnitju9BxRRKlymWMPhYx0ghyfqUYkIfaUiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇺🇸
هم‌اکنون ترامپ پشت شیشه ضدگلوله
@News_Hut</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/68562" target="_blank">📅 22:31 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68561">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b-vCx0QysnivxmLP-EHRPVGjot3n4Pq1IhgxP175nA6DC8zPnppFR_f1WejkcbdQycKu4WIubNTWlyArX9zB8cr8cju2OTf7imar-A7pk_TWL8EvR-1Ckal6xt_92bfjflnGVQFMSAj5RsxXh5ebomKFfxCphG-J8fUj3AgQt6vehfDEIuiuGQxJByFT4Cgo0W__kNV2adjeZoSxbJnognGXv8Cxrxwr5zTYzRZbdLh16oYcvquoTDFZDr1kJRnQDH5oRY4JHAaUxqzlvgrK0qoAXKCPHWXe9iLIdRazbS2ppl5WmMD87G1Re2hCvaXaJPHaKG7oTgMP8TDCy5pJMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
فینال جام جهانی هم شروع شد
سپی
یه پلتفرم دست کرده به اسم چسفیل که علاوه بر خود بازی، تمرینات، ورود بازیکنا به ورزشگاه و… همرو
بدون سانسور و رایگان
میزاره
گفتم اینجا هم معرفی کنم شاید به دردتون بخوره.
هرکی خواست بازی رو با پوشش کامل‌تر دنبال کنه یه سر به چسفیل
بزنه
👇
لینک پخش بازی:
https://chosefil.com/fa/programs/318
ایدی کانال تلگرامش:
@officialchosefil</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/68561" target="_blank">📅 22:31 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68560">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c88de66012.mp4?token=FUXLAg44CXe8VbcmoK75cJgO8Z0krqFR4y02P0F3eT-OhvXkbvDwzZrfkoQeVwdTjm6vxnZJlV-zPbnY3Gf7NtY5L2baJyJamPenKg32JUrUjjpvB-muh__V74ZdaZxiTiq1wFem8xmBi2gp1g9AUDCuk_D-gs0EU8ZY948xmiCwd5xqysLuGoFE45kJ9Guv10bdwedEiSyezSPkztZItR13pwd-2HY9zEaD78W-ieCRGEKU3Fuym4xgI2dLdf-wBfbSCyXAwLNMyVozsZWKB91q0_Xded0ddtiZuchpjwyMEhiaVJZi_6aWK-IBJybUQwUfyIfFLaYPuOzn076XEA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c88de66012.mp4?token=FUXLAg44CXe8VbcmoK75cJgO8Z0krqFR4y02P0F3eT-OhvXkbvDwzZrfkoQeVwdTjm6vxnZJlV-zPbnY3Gf7NtY5L2baJyJamPenKg32JUrUjjpvB-muh__V74ZdaZxiTiq1wFem8xmBi2gp1g9AUDCuk_D-gs0EU8ZY948xmiCwd5xqysLuGoFE45kJ9Guv10bdwedEiSyezSPkztZItR13pwd-2HY9zEaD78W-ieCRGEKU3Fuym4xgI2dLdf-wBfbSCyXAwLNMyVozsZWKB91q0_Xded0ddtiZuchpjwyMEhiaVJZi_6aWK-IBJybUQwUfyIfFLaYPuOzn076XEA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
مجری حکومتی:مشهد در18و19دی پنج ساعت سقوط کرده بود.
عراقچی: اصلا انتظار اعتراضات ۱۸ و ۱۹ دی رو نداشتیم، جمعیت خیلی بیشتر از چیزی بود که فکر میکردیم
.
مجری: ترامپ درست می‌گفت، من رفتم آمارش رو درآوردم، مشهد در عرض چند ساعت سقوط کرده بود!
@News_Hut</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/68560" target="_blank">📅 22:26 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68559">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2c26a9bf5f.mp4?token=km5IrLRz0Nn5Wji6_dq_SVOrHutyzvocxSHVH3WErOWkqmc2VYT1V-VCJ8ziiQWCeNDmgJ8KKJ3twtZ5-YZ75E38YpTRJ-klTfoN__hM3_DHI_U_LW2aVXPd1ezJM9t8k-mXz6VdopNX_EMUAMgfhAcDvvENpwrEk8Milu1LCCNOYKTsNMqF17sYGHdkVJj-ndDYhKb3ICRDA5EWIDd4tJwk1ibEZ34W2bB8sZattTM5M-Sa0ZIp31dcaiEODePOQJy_KEvR6QdLumNKBE8prrYlT-DhAKyTiw7b1FWp7zOGaZstIlTk8OGMgbMVBXAfsOVXsZ83rNBmxa0IcqOQyA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2c26a9bf5f.mp4?token=km5IrLRz0Nn5Wji6_dq_SVOrHutyzvocxSHVH3WErOWkqmc2VYT1V-VCJ8ziiQWCeNDmgJ8KKJ3twtZ5-YZ75E38YpTRJ-klTfoN__hM3_DHI_U_LW2aVXPd1ezJM9t8k-mXz6VdopNX_EMUAMgfhAcDvvENpwrEk8Milu1LCCNOYKTsNMqF17sYGHdkVJj-ndDYhKb3ICRDA5EWIDd4tJwk1ibEZ34W2bB8sZattTM5M-Sa0ZIp31dcaiEODePOQJy_KEvR6QdLumNKBE8prrYlT-DhAKyTiw7b1FWp7zOGaZstIlTk8OGMgbMVBXAfsOVXsZ83rNBmxa0IcqOQyA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
پخش تلویزیونی اسرائیل؛مقامات امنیتی اسرائیل و ایالات متحده:
ایالات متحده در حال آماده‌سازی برای تشدید حملات خود به ایران است.
این هفته، خاورمیانه شاهد تعداد بی‌سابقه‌ای از هواپیماهای تانکر سوخت‌رسان خواهد بود، که این تعداد حتی در مقایسه با آمار ثبت‌شده در جنگ اخیر، غیرمعمول است.
@News_Hut</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/68559" target="_blank">📅 21:54 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68558">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">🚨
🚨
کانال ۱۳ اسرائیل :
دونالد ترامپ، رئیس‌جمهور ایالات متحده، پیامی به کشورهای حاشیه خلیج فارس ارسال کرده است که در آن تأکید شده است: اگر این هفته آتش‌بس برقرار نشود، این کشورها باید خود را برای تشدید تنش‌ها آماده کنند.
@News_Hut</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/news_hut/68558" target="_blank">📅 21:36 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68557">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🚨
استانداری خوزستان:
دقایقی پیش یکی از مناطق خارج از محدوده  شهر و حاشیه‌ شهرستان آبادان توسط دشمن آمریکایی مورد حمله موشکی قرار گرفت. این حمله تلفات جانی در پی نداشته است.
@News_Hut</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/news_hut/68557" target="_blank">📅 21:17 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68556">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">مسی و نتانیاهو
🇮🇱
یا یامال و فلسطین
🇵🇸
؟!</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/news_hut/68556" target="_blank">📅 21:03 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68554">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MATEROMNhZkODIRslyNp-GLh4_2u175FO-vR7HLpWSd677z2R1nWV2mR-DRnbp6FXVCKXZ2hXPi6vNgOYNZuDP_gf7fRTo_piIw0RMuK8kq3kjBngQCDBLGheSqcW07wprTXGBR_cd-1sp8pVZ0Zw9C-sH03Py0eNWXYHOayDjO_ezu8hARvJEGvgH-CmWLYtzqVYi6ARud0j1WYtapHiQJFdh41AgP40skY28pFNmP0_Wn6ZALBglieEVW31OTW9sQD-7Ww58GBBXHjMo9fgDrRhPQfkAMDNKSUIFtS0b95Crl8TWSPud-opGqcdxK5JadZntDgSVxt6_K_sPugww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/B8_Yl_W57d7t1cGr2_8m4WGROaXr2FISUH_9KLt8QrqzYuKfAKnLFqcWZQvhay0GcemZLTLDprcx5gYNu9DP6w_fWdvw4OqDS2l8XN2IzbvIc11Pl6kLTNbjJXATsxn7IFD8RuQdOxzGa0_a4AGFlw0WLEf8Nwd-2Ji3lrWnuWR7HKwbhbEs3DbiXGk_WrcvYs5P9zxGK1wLWedgCpOl8lZmQqL2rSiJ6hNlXneJfPwLrBYzf4l7ZKhkrBlo8WYkiHZzSpKE3s1jB9wVqW8EFUQGVmRQlF__XjdbnTt7msl5txH2lnkrSmJoy35mkoLLkGiutWeIKIeJa01PYy6PQA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">💢
🏆
فینال جام جهانی 2026؛ شماتیک ترکیب دوتیم ملی اسپانیا
🆚
آرژانتین؛ ساعت 22:30
@News_Hut</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/news_hut/68554" target="_blank">📅 20:55 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68553">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🚨
یک پیشنهاد جدید آتش‌بس ده روزه از سوی قطر ارائه شده:
• ایالات متحده حملات را متوقف خواهد کرد.
• ایران دو مسیر دریایی در تنگه هرمز را به مدت 10 روز باز خواهد کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/68553" target="_blank">📅 20:46 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68552">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/e08df79c06.mp4?token=djuWhPmI-6SBzEqvbHWpcyQLsQwspyzAxDj6OwosearPrlb28FIGxEQQ_EKVrN_ScJuwvt3QJvLt52dA5t61dZssTMZ3B2CXhCvjY-A7y1WMIwhZaiTAO1Fc5QYFLKkBDoQdqgeSQOvM4vaNe2CHZY1jvRkpNFVBsV1RT7CdCzsm6wL2XG2oy90LtpYM1rFgmXk0mJEGn81IhPsiMZNCgZOIWyJRO6L1pvzSYIMMl8PydeANanuy0vYi-i4Mu79HTpz9keyADizdvYh2t5PypTo-bJbLg6RIrX4Ti8zhko3y1q77uFVIjnaLhWkbTPTmTwXtIbZH3MG5HLe19NsVfg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/e08df79c06.mp4?token=djuWhPmI-6SBzEqvbHWpcyQLsQwspyzAxDj6OwosearPrlb28FIGxEQQ_EKVrN_ScJuwvt3QJvLt52dA5t61dZssTMZ3B2CXhCvjY-A7y1WMIwhZaiTAO1Fc5QYFLKkBDoQdqgeSQOvM4vaNe2CHZY1jvRkpNFVBsV1RT7CdCzsm6wL2XG2oy90LtpYM1rFgmXk0mJEGn81IhPsiMZNCgZOIWyJRO6L1pvzSYIMMl8PydeANanuy0vYi-i4Mu79HTpz9keyADizdvYh2t5PypTo-bJbLg6RIrX4Ti8zhko3y1q77uFVIjnaLhWkbTPTmTwXtIbZH3MG5HLe19NsVfg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
رئیس هلال احمر:
در تشییع میلیونی نه تنها یک فوتی هم نداشتیم بلکه شاهد چندین تولد نوزاد نیز بودیم
👅
@News_Hut</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/news_hut/68552" target="_blank">📅 20:30 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68551">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d7091c7c4c.mp4?token=LAZlAHGz_wo7Ig384zgVBYakcYgIECXguQH_zAsPqxt2zVaF0ThGD6QLSCXrmHUDSrkV8LvEAd-uu-b5uRAzuvltpUd23CdCapD3Sl-scIp79SekStYHVR-oWMh3tIzhoU8IJtTalHGPH6zofzeiIj27ctdOVMVPIJu6f6tcCpQs9bmBh7VSGNKryH8YhrxuvB5jo3lc3AqwEEvtbrPaFSDdCeGLMftRSXLTANnh3JnGH04FNskiUSSE1eBZVA0MMETfqrvD75QsZoD1pJ3B4Me9tQXtktqlptTxCT63tf7ghGCkbn_vgoIXLNHfAcZpuxYkClPkTL9z0dc-bwLPKQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d7091c7c4c.mp4?token=LAZlAHGz_wo7Ig384zgVBYakcYgIECXguQH_zAsPqxt2zVaF0ThGD6QLSCXrmHUDSrkV8LvEAd-uu-b5uRAzuvltpUd23CdCapD3Sl-scIp79SekStYHVR-oWMh3tIzhoU8IJtTalHGPH6zofzeiIj27ctdOVMVPIJu6f6tcCpQs9bmBh7VSGNKryH8YhrxuvB5jo3lc3AqwEEvtbrPaFSDdCeGLMftRSXLTANnh3JnGH04FNskiUSSE1eBZVA0MMETfqrvD75QsZoD1pJ3B4Me9tQXtktqlptTxCT63tf7ghGCkbn_vgoIXLNHfAcZpuxYkClPkTL9z0dc-bwLPKQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇱
نتانیاهو :
آرژانتین امشب قهرمان جام‌جهانی میشه.
@News_Hut</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/news_hut/68551" target="_blank">📅 19:56 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68550">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j3gDy_Lg7ttDxkWCo6P49mBuz5nJKkkAOrtoDs-qrjsFPQwLSCyJof8rZGVs8CCnHZfU9prwKtFqKRAfd6hcJ1dCoLOtlBadIuOxoRVJ04tN_s5qD0F51VAJbAzkNtGe0FRrAf8P92n0pCRJe-AsQieL47eZsldjHjxI6_g7ppcQVx6SjXaqyO0YXNF3D8lo3jAXozPb3J84lWIV6FNuryJR08hnkbpl7VPVgAfR2qkuGm4OoD6IWLYKsCinU_2Ow4sf3TBgWpB0-jAo3wdYuQYSp4S1zvhBaLV0JEg68klJwDm3SjCYFU8x5IYAgTvU3FWYJC1iuP08J4GcB0-mbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگه امشب نیروگاهی در ایران هدف قرار بگیره، مقصر اون فرماندهای زن‌جنده‌ی سپاهن که امروز برق کویت رو زدن. #hjAly‌</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/68550" target="_blank">📅 19:47 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68549">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">‼️
رسانه های عبری:
برآورد‌های امنیتی اسرائیل حاکی است که رهبری ایران دستور حمله به اسرائیل را صادر خواهد کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/news_hut/68549" target="_blank">📅 19:35 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68548">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🚨
هدف قرار‌گرفتن یک نیروگاه برق در کویت  @News_Hut</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/news_hut/68548" target="_blank">📅 19:15 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68547">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EN-w0P_zPgww6k636bYKvtqLyuESGtyDbYhblfAN7Nu8rV3nKTzdNOSJRiQvyn_5fhZhDL1P8ZJ6qCf4gpLyQV3vVEymLaAdOz9SIvD4P8PQ_8UIoOnrHDFSgomXDnIHtYwrowUYBuCyYdgvGp5VACiLbs_sl170b6p75P0BpFwqW8PkiLBxcaoP1vcJtonFof98VSXwTKc2UrvSW9BQwKtEyF3R41sgGv5_JkVSyVHtxgiZAMBqNT9Z86meb4JDLsN2wf4NSoXE662FqbKDXJFWjA_v2zMR5Bykj7BqeFbk3J_3WtLCfX3mtPhzIvCUzahp2pALwzsFzQb9Gup0vA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
فینال جام‌جهانی ۲۰۲۶ فوتبال
🇦🇷
آرژانتین
🆚
اسپانیا
🇪🇸
امشب ساعت 22:30
@News_Hut</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/68547" target="_blank">📅 19:05 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68546">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/798b52eeca.mp4?token=e4oMWfghz5NDAIr3F2hsQL2sInz74pfFTUaBqJENUHlG2M0c_i8CK4mW9i2-B4EHLhH49HYuNeC4b__0_hOAp6A5VupTds9Pxg7QBrB8U2GTk9VVvnwhFDS-lngUh2TWP_tZ4aCYFbFo6YNnX0ptZ45byHrgzAtVkwhSBDhlw2CwqPMsZnXCyd9QUsW3BJi4uH_g56t94mv3nJDV-lR2GQMebi3h_EvEg5s2PdLEq_dAOZ_L4CPTs_nEfFzjI_WIgR9xmrW5nUwFeeEsPgQ1z7y2ioT5cZ42S8WiMAQslDoH_herZAHz_hSYFXweoW6GK6aN0cBhpPYVZ3iiPn0i1Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/798b52eeca.mp4?token=e4oMWfghz5NDAIr3F2hsQL2sInz74pfFTUaBqJENUHlG2M0c_i8CK4mW9i2-B4EHLhH49HYuNeC4b__0_hOAp6A5VupTds9Pxg7QBrB8U2GTk9VVvnwhFDS-lngUh2TWP_tZ4aCYFbFo6YNnX0ptZ45byHrgzAtVkwhSBDhlw2CwqPMsZnXCyd9QUsW3BJi4uH_g56t94mv3nJDV-lR2GQMebi3h_EvEg5s2PdLEq_dAOZ_L4CPTs_nEfFzjI_WIgR9xmrW5nUwFeeEsPgQ1z7y2ioT5cZ42S8WiMAQslDoH_herZAHz_hSYFXweoW6GK6aN0cBhpPYVZ3iiPn0i1Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
هدف قرار‌گرفتن یک نیروگاه برق در کویت
@News_Hut</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/68546" target="_blank">📅 18:54 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68545">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🚨
🚨
🇮🇱
یسرائیل کاتز، وزیر دفاع اسرائیل:
«ما اعلام کرده‌ایم که اگر ایران جرات کند به اسرائیل حمله موشکی کند، ما با یک حمله قدرتمند، بدون هیچ قید و شرطی، پاسخ خواهیم داد.»
@News_Hut</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/68545" target="_blank">📅 18:53 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68544">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromYekbet Support</strong></div>
<div class="tg-text">🅰️
🅰️
🅰️
🅰️
🅰️
🅰️
🧾
امکان ویرایش شرط ثبت شده
💥
برداشت سریع با کد پریمیوم ووچر
💵
شرط بندی بدون محدودیت، بردهای نامحدود
🎁
جمعه و دوشنبه‌ها، شانس بردتان را دو برابر کنید
100% بانس میکس ورزشی تا سقف 30 میلیون ریال
🎁
با واریز کریپتو، سقف برداشت خود را به سطح جدیدی ببرید!
1️⃣
لینک بدون فیلتر
1️⃣
ورود به سایت با فیلترشکن
••••••••••••••••••••••••••••••••••
💠
لینک اخبار و هدایای سایت
👇
👇
🔸
https://t.me/+ioIBrQfqMLtmMmEy</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/68544" target="_blank">📅 18:53 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68543">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromYekbet Support</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YamJM9BcGW7pHJrKdDQed73PTVejHOCR53Pp8v2UgKneUffQ1XDbtz4drtm-XkdOjrSBTVxENnKRNRl-r5erPSgv1GGY4KGewvBzUn6q4ikkeWQk6Ps8DVnJG-creLrN6qQ46KAfyk9HXq8mZWONppfRL0ck2KvtDt6-JriotuL9ftsbq6CRmGExtR-zTeumKPcgB2vvFvmUSFUGCqoG7QKANw3C1m47gdbEzcIAgN3FJMRzaS880g9EvaOXgeso7JVWZeysA8G2fmUY3GdA8Vw_sRnoDxxecN3yCTW0awksO7CkI0O1uuIIR7420o8y2fvsNggztrDGvbPJ7A10UQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
فینال جام‌ جهانی 2026
⚽️
اسپانیا
🇪🇸
-
🇦🇷
آرژانتین
⏰
شروع بازی ساعت 22:30
✔️
امکان ثبت پیشبینی با مبلغ نامحدود
🫰
محاسبه نرخ دلار با قیمت 2.200.000 ریال
⭐️
فرصت استثناییی چالش‌های پیشبینی فوتبالی سایت یک توتو، با جایزه 500 میلیون ریال
1️⃣
لینک بدون فیلتر
1️⃣
ورود به سایت با فیلترشکن
📲
@yekbet</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/68543" target="_blank">📅 18:53 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68542">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/24db6b1462.mp4?token=GhDi7ALmCp1CdiC0-KZz0FCIwjU6K1Ivmpa9-2Ufw70FzCFtaZmaGXLg6CuBqudJnOsG9LsJ0AmDifYS8B8Ub-M2VV3KlFZYg1hPLGBfK_12JL0eQ1Gq6-2rhiWFCMKoGr2tBa7Yzg3SaMHpXozB-TdQ0dMNerrKElYBXlVjT5vQXBvFlNkMBUsqoRCY3T7oihGThioEldwlaBGMBZwls2HXltqUcp0Qwcl8n-Z3cZ9Mf2kqYf7PbsD0znqnRS4vtzSM-lLn49fMY6ChlWvWgiCcpIPNt-YPUslbhFCtxV-_q_NbH4Ly_CEMk7WnM-FFYNIBYjSE-Oq7eAXGSVmiJw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/24db6b1462.mp4?token=GhDi7ALmCp1CdiC0-KZz0FCIwjU6K1Ivmpa9-2Ufw70FzCFtaZmaGXLg6CuBqudJnOsG9LsJ0AmDifYS8B8Ub-M2VV3KlFZYg1hPLGBfK_12JL0eQ1Gq6-2rhiWFCMKoGr2tBa7Yzg3SaMHpXozB-TdQ0dMNerrKElYBXlVjT5vQXBvFlNkMBUsqoRCY3T7oihGThioEldwlaBGMBZwls2HXltqUcp0Qwcl8n-Z3cZ9Mf2kqYf7PbsD0znqnRS4vtzSM-lLn49fMY6ChlWvWgiCcpIPNt-YPUslbhFCtxV-_q_NbH4Ly_CEMk7WnM-FFYNIBYjSE-Oq7eAXGSVmiJw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
ستون دود در دزفول
@News_Hut</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/68542" target="_blank">📅 18:41 · 28 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
