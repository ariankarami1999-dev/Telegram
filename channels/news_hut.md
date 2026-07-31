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
<img src="https://cdn4.telesco.pe/file/W-GwR4AepoI8Gx9auHL2O1X5gcndJ8DnGa47vOLyHmIfm061-mSosy22_CxTXjtNpGzuaMTKIG4npt_N0M2-719YHdoBOwgNoY5Fcoql6sAmlJAatBL-GPfBN7P4sqFqnnD4QgIhbFopafN-zSRYIFjn6EBMNIxqdsHU0lzD_2Ul23BfM0KH48_G7m_9rDLPXUjsZK3KeS5Y341cSkSPEgSpTwo8LCHtwvyaqWCJ-BA3MC_x1jyNYcG8wRb6c82yJ0qoKDBn7gf_3yXFnahdPWqZl3Ft31gPMiWhBTF87Sp9T4bFLL7oLwdRWpoL0xaDI2MRTeWjwjInceSOPD2Q2g.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 139K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-09 23:44:28</div>
<hr>

<div class="tg-post" id="msg-69328">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rXk1itqMaVm3o8CBdTqlkSC06THVgXuYb8ONC1DeiHRl4UY9NRJHGoygdf1jWk-wVXY3AmIsQS95OK2N168PUZVmOgAov2AeQwQYpnQK9RJSn4OG9hFWrtZRJl04rcs4_UgLMupowA7yFznAhLzob75dtdg-KtvdOu7bsc4JLDuzM96O3jt8XW0ZJytIExm64OKWymxl-8SOVtI8nbtUWzLJ3TQzAuPqUG6f2mlQRG40W5s45vfPXyVNQUh_fSfCgti5GNoVryOcQDZBuJ4ToaHuuvFPGKUlRZXTjHlXzDJoWdooUCWpnE3xw5XHO66IsnNsdaEfJVkyc6OSpnJKLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
سنتکام برای بار هزارم:
تنگه هرمز بازه و ادعای سپاه مبنی بر بسته بودن تنگه هرمز دروغه.
@News_Hut</div>
<div class="tg-footer">👁️ 4.66K · <a href="https://t.me/news_hut/69328" target="_blank">📅 23:20 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69327">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cdfe35db6c.mp4?token=ppQqpHC5xYGw14vLcFyJSmrIx0NSGZE5U7I5aZf0ublpv0ZM0dtDki_kfRsRTuEyDfSjlSVtT12NrKvv1-9YT1buAcn6InmNIMV-XBGaXwr-Rt0Qh8kC2G7reDObkMOOLRhOpzRKgPb18PXVcxsvNT0i4ToclVuBYXbVViT4JyBiph7YCKKIWliIHQshiQdrxaWv_XRET8kO2h9eewb3PUedOtE7vx2iSJmP5wT9ZvcvTqKkKGz_AjUrQVYHStVWfLOjQSki-5XrsO5GMP_73s8YNE-LK3vpKoHEF6wEBymYbvWKRWN3UhKeDNTCVsBb9SB8wNoI4V9c2-Gd8XPJqw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cdfe35db6c.mp4?token=ppQqpHC5xYGw14vLcFyJSmrIx0NSGZE5U7I5aZf0ublpv0ZM0dtDki_kfRsRTuEyDfSjlSVtT12NrKvv1-9YT1buAcn6InmNIMV-XBGaXwr-Rt0Qh8kC2G7reDObkMOOLRhOpzRKgPb18PXVcxsvNT0i4ToclVuBYXbVViT4JyBiph7YCKKIWliIHQshiQdrxaWv_XRET8kO2h9eewb3PUedOtE7vx2iSJmP5wT9ZvcvTqKkKGz_AjUrQVYHStVWfLOjQSki-5XrsO5GMP_73s8YNE-LK3vpKoHEF6wEBymYbvWKRWN3UhKeDNTCVsBb9SB8wNoI4V9c2-Gd8XPJqw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
🇺🇸
پرزیدنت ترامپ:
«این‌ها خیلی وقت‌ها زیر قولشون می‌زنن.
توافق می‌کنن، بعد می‌گن باید
7 ساعت
درباره برنامه هسته‌ای مذاکره کنیم.
من می‌گم: "آخه چرا 7 ساعت؟ مگه نمی‌شه تو
10 دقیقه
جمعش کرد؟"
شما
5 دقیقه
وقت دارید که تکلیفتون رو روشن کنید.
آخرش هم فقط کله منو کیری می‌کنن!»
@News_Hut</div>
<div class="tg-footer">👁️ 8.98K · <a href="https://t.me/news_hut/69327" target="_blank">📅 22:43 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69326">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/379fea6ae8.mp4?token=G7HQJSjJuUVAyW9zSVnhH6kt_DBxQR21bgtWE1A8MehMz-Zh07qBz6oZhjlcJCJuWfotWBNAZL16qcTRxf3dgx8AVYebDNpJKKTFuqAtbRM5EJ5u2MjyFeRgwCLwYWEY2QSCTHyYEpFTbdUIPblqyzZjrfBRB3Pvf1CaJeWRTDCzG9Ptpe076Lh02hfm-9B37uZ8B_5vT2IAgiXgJA1UA6M-Y7J0UBZ5a6Pl6sOW9OZbIBSJvp9Im2k33RsbW9snUF16_Ofa3Ni32AJj1oK4DncuAsM22_lhw4SgG6NrxUVZTuI5W8w1Lf4M7gi8krifg4t3hJcbE03FJ2Tl8K0giQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/379fea6ae8.mp4?token=G7HQJSjJuUVAyW9zSVnhH6kt_DBxQR21bgtWE1A8MehMz-Zh07qBz6oZhjlcJCJuWfotWBNAZL16qcTRxf3dgx8AVYebDNpJKKTFuqAtbRM5EJ5u2MjyFeRgwCLwYWEY2QSCTHyYEpFTbdUIPblqyzZjrfBRB3Pvf1CaJeWRTDCzG9Ptpe076Lh02hfm-9B37uZ8B_5vT2IAgiXgJA1UA6M-Y7J0UBZ5a6Pl6sOW9OZbIBSJvp9Im2k33RsbW9snUF16_Ofa3Ni32AJj1oK4DncuAsM22_lhw4SgG6NrxUVZTuI5W8w1Lf4M7gi8krifg4t3hJcbE03FJ2Tl8K0giQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎤
خبرنگار:
سنتکام گفته حملات اخیر برای کم کردن توان ایران در مختل کردن تردد کشتی‌ها در تنگه هرمز بوده. به نظرتون چند حمله دیگه لازمه تا به این هدف برسید؟
🇺🇸
ترامپ:
«هیچ‌وقت نمی‌شه دقیق گفت.
بیشتر کشورها تا الان تسلیم شده بودن.
ایران هنوز تسلیم نشده و بابت همین باید بهشون اعتبار داد.
اونا همیشه به سرسخت بودن معروف بودن؛ واقعاً هم سرسختن.»
@News_Hut</div>
<div class="tg-footer">👁️ 9.48K · <a href="https://t.me/news_hut/69326" target="_blank">📅 22:38 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69325">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0d8357e0fa.mp4?token=RWcfWtdNQ1NDUmBnUhGoGR3ae_JKdVRasDGrfToJ0S5pgOTrrGxHfWF1v4VsWNtz4y_kzI3pzDIK6bnwJghqM9cTYsMAmhTwkQXAEbzJOCTjTeg8lIzEGBjrCzlY2-L_yhLGSWd04C8B9P_ypwZjEIbIxOtJNdqo4ruXm_mCco1IqXH4xQuSd_uzDObDCJ9OKe_Sipt0Ux5LznFDES4rMRwcCD4VhbDlxx3qAsmCyp2hJaU9Zo4jNELAH31eiQfiliB5A-oZnWz2bv5wdbdfCkJ5qLiAOEuhVJw2jDJMrbvJOaE6chxy4xJU6xi7GilP6mKVeYiy2g53F1fRcvEVUVBrwJwvItfhBxOzHC3vBF6I9kA75xgRWTImU1cvbzisGlt9XIBiTTtSAvKvtg_CZH9E1d7yrj6DXL34Q02GnkIPY8q8CY9v9aVz9d6WsvtxI9e3S7r4DO53dq6xJlXLbMj4yheIoeZ7LeYVPMBz7SjtubyqgDVZdaPUcl93WmQmXrzRRpGV3t8sSZnSAnYG_Axrw4KBqgiHfoacpcB_hxNTtLVayBzDhy-sFdJ6Lumd1rJtYfnZCh5FFqgsqxV5hldTrMFH9vAaKKEXkRYUKVOZgo2uNjRCgR6Wf9AZAz-iv_--vusLWzql5XwEWdi7K9uBIkxAUFNTSbtWMnoj8Pg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0d8357e0fa.mp4?token=RWcfWtdNQ1NDUmBnUhGoGR3ae_JKdVRasDGrfToJ0S5pgOTrrGxHfWF1v4VsWNtz4y_kzI3pzDIK6bnwJghqM9cTYsMAmhTwkQXAEbzJOCTjTeg8lIzEGBjrCzlY2-L_yhLGSWd04C8B9P_ypwZjEIbIxOtJNdqo4ruXm_mCco1IqXH4xQuSd_uzDObDCJ9OKe_Sipt0Ux5LznFDES4rMRwcCD4VhbDlxx3qAsmCyp2hJaU9Zo4jNELAH31eiQfiliB5A-oZnWz2bv5wdbdfCkJ5qLiAOEuhVJw2jDJMrbvJOaE6chxy4xJU6xi7GilP6mKVeYiy2g53F1fRcvEVUVBrwJwvItfhBxOzHC3vBF6I9kA75xgRWTImU1cvbzisGlt9XIBiTTtSAvKvtg_CZH9E1d7yrj6DXL34Q02GnkIPY8q8CY9v9aVz9d6WsvtxI9e3S7r4DO53dq6xJlXLbMj4yheIoeZ7LeYVPMBz7SjtubyqgDVZdaPUcl93WmQmXrzRRpGV3t8sSZnSAnYG_Axrw4KBqgiHfoacpcB_hxNTtLVayBzDhy-sFdJ6Lumd1rJtYfnZCh5FFqgsqxV5hldTrMFH9vAaKKEXkRYUKVOZgo2uNjRCgR6Wf9AZAz-iv_--vusLWzql5XwEWdi7K9uBIkxAUFNTSbtWMnoj8Pg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🗣️
حسین جنتی، شاعر : سقوطِ زندگیم جایی اتفاق افتاد که سال 89 جلوی علی خامنه‌ای شعر خوندم؛
من سال 89 دعوت شدم به شعرخوانی تو بیت رهبری و شب قبلش بهم گفتن 5 تا از شعراتو باید بدی ما نگاه کنیم، درنهایت یکیشو اجازه میدیم بخونی.
ولی من شعری که اجازه نداشتم رو اونجا خوندم:
گشته‌ام میدان به میدان شهر را، هرگوشه دردی هست
ارتفاع درد از پیچ شمیران میرود بالا
درد من هرچند درد خانه و پوشاک ارزان نیست
با بهای سکه در بازار تهران میرود بالا
گفتم که خواجه در رویای خود از پای‌بست خانه میگوید
ناگهان صدها ترک از نقش ایوان میرود بالا
گفتم جوجه‌های اعتقادم را کجا پنهان کنم
وقتی شک شبیه گربه از دیوار ایمان میرود بالا
فردا صبحش اومدن سراغم و گفتن تو غلط میکنی با ولی‌امر مسلمین شوخی کردی و سقوط آزاد زندگی من همونجا اتفاق افتاد و اصلا هم پشیمون نیستم از کاری که کردم.
@News_Hut</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/news_hut/69325" target="_blank">📅 22:25 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69324">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d259260d40.mp4?token=WCoK8amzfKwice_gIVbB-qnZxyYsNBaF-UzlQodkVpUqYECwXVJS-ibF0uxQjZ45oqpLsnHWg1XiQ3_flbuwJhFIgzcAHNb1eRZiY1SiY4FxPucxBxAHRJR9e-rfKXQP0FCuseCV9fPif9j_sgoWvT1s89F5gySAi8ftkHCr5ShRwhj6D1IE2iT3N5me2gwOtRhrHDxqzC_u8K-bfjX2I0FtNhb0tNybZTZPZrxXdsjpPN2au__0eccBEt-tvRpfwpaV4mqFGSPja4OqkaALasM2205l7NGON3npIjkihQ9a18rllqVNg_GPfapkmQR3qaLYvV-DACeD51pEP48lODzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d259260d40.mp4?token=WCoK8amzfKwice_gIVbB-qnZxyYsNBaF-UzlQodkVpUqYECwXVJS-ibF0uxQjZ45oqpLsnHWg1XiQ3_flbuwJhFIgzcAHNb1eRZiY1SiY4FxPucxBxAHRJR9e-rfKXQP0FCuseCV9fPif9j_sgoWvT1s89F5gySAi8ftkHCr5ShRwhj6D1IE2iT3N5me2gwOtRhrHDxqzC_u8K-bfjX2I0FtNhb0tNybZTZPZrxXdsjpPN2au__0eccBEt-tvRpfwpaV4mqFGSPja4OqkaALasM2205l7NGON3npIjkihQ9a18rllqVNg_GPfapkmQR3qaLYvV-DACeD51pEP48lODzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
صحبت های یک عرب درباره ایران:
ایران از جامعه عرب متنفر است، یک تنفر تاریخی.
همانگونه که اسرائیل از جامعه عرب تنفر دارد.
اگر کتاب فردوسی(کتاب شاهنامه و قوم پارس)رو بخونید شک ندارم که ممکنه باعث بشه بالا بیارید.
چرا؟چون عرب را به زشت‌ترین اوصاف وصف میکند.
مثلا فردوسی گفته:عرب در آن مکان خورنده ادرار شتر است،خورنده ملخ اس، ولگرد و کثیف است.
اما فردوسی میگوید اینجا در ایران حتی یک سگ در اصفهان از آب پاک و زلال رودخانه میخورد.
حتی یک سگ در اصفهان شریف تر از عرب در آن مکان است.
@News_Hut</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/news_hut/69324" target="_blank">📅 20:45 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69323">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ea4c431667.mp4?token=EV0Bdw8Kn9-FXOcHtc4FCx9FQNPegxE2exNLb5EPav0MbsMuFkn7eYjva_B3-qtvaExou0KlYBrHQ5C69nfHZXByiX6X5d-gAe8p2huw-qkz_JQ_TFpxzMP0lnN8hj4j-wqCrfUC9pXwyaEo502chBhYqHhP0nM5aus0Idd4DtIHrqe5YBRl7byDqk2qIL7g8hOCW7DbV4MmnwSrWX45Jo2Pb2WPT9k8U44V-USU3lL2vfEkVp1qsUoIuwfvVBLrCg__IKf_9F-Gc319xi9HpQM9PSuEkKrF14ye1mJPkWwLCm4TA8keigALnRcW_fnjm1cZS5KiPy5bwf0EXHD5Kg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ea4c431667.mp4?token=EV0Bdw8Kn9-FXOcHtc4FCx9FQNPegxE2exNLb5EPav0MbsMuFkn7eYjva_B3-qtvaExou0KlYBrHQ5C69nfHZXByiX6X5d-gAe8p2huw-qkz_JQ_TFpxzMP0lnN8hj4j-wqCrfUC9pXwyaEo502chBhYqHhP0nM5aus0Idd4DtIHrqe5YBRl7byDqk2qIL7g8hOCW7DbV4MmnwSrWX45Jo2Pb2WPT9k8U44V-USU3lL2vfEkVp1qsUoIuwfvVBLrCg__IKf_9F-Gc319xi9HpQM9PSuEkKrF14ye1mJPkWwLCm4TA8keigALnRcW_fnjm1cZS5KiPy5bwf0EXHD5Kg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👍
🤡
یه بخشی از صحبت های خیلی مهم ترامپ: بینگ بینگ بینگ بینگ بینگ بینگ بینگ بینگ بینگ بینگ  @HutNewsPlus</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/news_hut/69323" target="_blank">📅 19:58 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69322">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from[ 𝐇𝐨𝐭𝐍𝐞𝐰𝐬➕]</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/884550e186.mp4?token=r7cRMtTeCWbZJ4kZWDh2Z3ct1NnaUcXOcEulVJJ6NYocBzr8menBqWsl1QzTm0OK1-aUf1loxYh16Yetu2_UOxe8y0LcOS9P7Yu33Shxmm7CmlzWJT8Kcb52gIMSjhfru4T7TZeEtcBBRsfzBM6eLBQnynmeFgUJFA45cOLIt7yNYsIYqYvFQPD-pEv2NWHoSt7CIuNokzewAMvHAGS8vO2SOv-afDC58fKvlv-sorMa9Ng06aAP2ik0krKIg-QEjF9AOgxPpsR11GXImdta7khgFXp4MiYEiYZpi5n-A5Uah66Bt64cxTZgftR60lxTKsO24rsnn-7BFfnw6aiXQg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/884550e186.mp4?token=r7cRMtTeCWbZJ4kZWDh2Z3ct1NnaUcXOcEulVJJ6NYocBzr8menBqWsl1QzTm0OK1-aUf1loxYh16Yetu2_UOxe8y0LcOS9P7Yu33Shxmm7CmlzWJT8Kcb52gIMSjhfru4T7TZeEtcBBRsfzBM6eLBQnynmeFgUJFA45cOLIt7yNYsIYqYvFQPD-pEv2NWHoSt7CIuNokzewAMvHAGS8vO2SOv-afDC58fKvlv-sorMa9Ng06aAP2ik0krKIg-QEjF9AOgxPpsR11GXImdta7khgFXp4MiYEiYZpi5n-A5Uah66Bt64cxTZgftR60lxTKsO24rsnn-7BFfnw6aiXQg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👍
🤡
یه بخشی از صحبت های خیلی مهم ترامپ: بینگ بینگ بینگ بینگ بینگ بینگ بینگ بینگ بینگ بینگ
@HutNewsPlus</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/news_hut/69322" target="_blank">📅 19:56 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69321">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/caed943dd3.mp4?token=AvI_0iOjPaUPGOKYAhosLaWT2wbQm750Wz3Z5NqugBPr7icHo2yeQFfyQD6rPoXdGl3b7MBPrzM26vKi3RCtbgN1ia5DxWK_QNN1nthXIWM7_g0_Bet8U8BrdacVqfVe2szpq2UJHGuj5DiX9urXDLOvV8ZK3jws-JQ9vLOnTJGEiZm4Zf0KOGhhlNj2IsPTivvHEpCmb39tDlGcKsW37k9xQWqzurmBWar1GmR5Nt5v8HVkpBF5UUaFh6m0umzTuWVtOZz7ms_Touat0Srt53xZFQ4YuExYQaB4moAPFXqZnlwWPxlyVtYvPcxvv0kRw4IHMMhn7MIa_ltpIIEB1A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/caed943dd3.mp4?token=AvI_0iOjPaUPGOKYAhosLaWT2wbQm750Wz3Z5NqugBPr7icHo2yeQFfyQD6rPoXdGl3b7MBPrzM26vKi3RCtbgN1ia5DxWK_QNN1nthXIWM7_g0_Bet8U8BrdacVqfVe2szpq2UJHGuj5DiX9urXDLOvV8ZK3jws-JQ9vLOnTJGEiZm4Zf0KOGhhlNj2IsPTivvHEpCmb39tDlGcKsW37k9xQWqzurmBWar1GmR5Nt5v8HVkpBF5UUaFh6m0umzTuWVtOZz7ms_Touat0Srt53xZFQ4YuExYQaB4moAPFXqZnlwWPxlyVtYvPcxvv0kRw4IHMMhn7MIa_ltpIIEB1A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
خبرنگار:
در مورد ایران، گزارشی وجود دارد که نشان می‌دهد شما پیشنهادی از سوی ارتش برای گسترش چشمگیر فعالیت‌ها دریافت کرده‌اید.
ترامپ:
ما از قبل گسترش داشته‌ایم. منظور از "گسترش چشمگیر فعالیت‌ها" چیست؟
@News_Hut</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/news_hut/69321" target="_blank">📅 19:53 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69320">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">املاکی تو یه جمله همزمان گفت هم می‌خوایم خیلی شدید به اونا ضربه بزنیم و هم می‌خوایم خیلی مهربون باشیم باهاشون
🤡
#hjAly‌</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/news_hut/69320" target="_blank">📅 19:50 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69319">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b0411d5fa4.mp4?token=XkbIQrD2N1wbmy1g3-Dd65Z7s5SbHxTK2Zz_jcJXcXmtgRB60YCE-juaXge2_55p8waeq4h2xkEgiOmi6tUVvBKGnaFtWvxjhRm5ZSTVVp-ip2UAfNQz44sJLXufdaeDS7p-nwN_etlLLdpdLpy150ojwGnCvYUro8VVZ03F5uS_0eUxEJi_0tvMgznuzv7vcgdCpsGiETlF0QdR7OCcu2FD-lYLrJD8znNnXPoUBFBpxrQcku3obTV2NwgbQS-w5RRWT0JY5UmT2sD4tT2ByDudtizuxyYCHjBok6Zy6v2UtgPcZ5OhRZvsPFJqsov7TlBXwBedE9T09RC5qcpR1w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b0411d5fa4.mp4?token=XkbIQrD2N1wbmy1g3-Dd65Z7s5SbHxTK2Zz_jcJXcXmtgRB60YCE-juaXge2_55p8waeq4h2xkEgiOmi6tUVvBKGnaFtWvxjhRm5ZSTVVp-ip2UAfNQz44sJLXufdaeDS7p-nwN_etlLLdpdLpy150ojwGnCvYUro8VVZ03F5uS_0eUxEJi_0tvMgznuzv7vcgdCpsGiETlF0QdR7OCcu2FD-lYLrJD8znNnXPoUBFBpxrQcku3obTV2NwgbQS-w5RRWT0JY5UmT2sD4tT2ByDudtizuxyYCHjBok6Zy6v2UtgPcZ5OhRZvsPFJqsov7TlBXwBedE9T09RC5qcpR1w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
پرزیدنت ترامپ:
«ایران وضعیت خیلی بدی داره؛ واقعاً خیلی بد. اوضاعشون خیلی خراب شده و تحت فشار شدیدی هستن.
تعامل باهاشون هم خیلی سخت بوده؛ هم صادق نبودن، هم قابل اعتماد رفتار نکردن.
ولی این چیزی رو عوض نمی‌کنه؛ چون در هر صورت، حال و روزشون خیلی بده.
ما فقط پنج ماهه اونجا هستیم. اگه به جنگ ویتنام نگاه کنید، می‌بینید آمریکا بیست سال اونجا بود. کاری که الان علیه ایران انجام می‌دیم، از نظر من یک عملیات نظامیه، نه جنگ.
ایران هنوز چند تا موشک داره، اما خیلی کمتر از چهار پنج ماه پیش.
توان تولید موشک‌شون تقریباً از بین رفته و ظرفیت پهپادیشون هم تقریباً نابود شده.
البته هنوز مقداری از این توانایی‌ها رو دارن.»
@News_Hut</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/news_hut/69319" target="_blank">📅 19:45 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69318">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7b0ec710b6.mp4?token=e07J-KyaHIPycX3xWtVxe8qrgaSQljVou0QsZNwQS7InjYaAgm8yfYurEodzeUFozkc7x8CWBY1hEUtZepsewgu7969Ol8c5z0ICKohwFWRiUbXhvBHabQMrtK4iQ5edZ3XUhQYaHQvyeysg71CAyD_RLjPybvntARXf0iRQU2HoX2UOlQaPL_loKHVAFnfqe3Vvh42Aijco6aM4FaEodrD1nlCZQAECyGjExPaqj7fDOoclm5LNi3R8EfLzrA9Hk9-Joh1HMiGVBXiB0EWPOHRpddfm9L_bwcGwB1NELR-avN-Da0E56cQukUrAAh2_hTNTbU8A94CP5g4xsqTnfw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7b0ec710b6.mp4?token=e07J-KyaHIPycX3xWtVxe8qrgaSQljVou0QsZNwQS7InjYaAgm8yfYurEodzeUFozkc7x8CWBY1hEUtZepsewgu7969Ol8c5z0ICKohwFWRiUbXhvBHabQMrtK4iQ5edZ3XUhQYaHQvyeysg71CAyD_RLjPybvntARXf0iRQU2HoX2UOlQaPL_loKHVAFnfqe3Vvh42Aijco6aM4FaEodrD1nlCZQAECyGjExPaqj7fDOoclm5LNi3R8EfLzrA9Hk9-Joh1HMiGVBXiB0EWPOHRpddfm9L_bwcGwB1NELR-avN-Da0E56cQukUrAAh2_hTNTbU8A94CP5g4xsqTnfw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
پیت هگست:
اگر برایتان سؤال است که چرا حوثی‌ها، با وجود اینکه یکی از نیروهای نیابتی ایران هستند، وارد این درگیری نشده‌اند، دلیلش این است که به مدت ۴۵ روز، قدرت نظامی آمریکا را از نزدیک تجربه کردند.
@News_Hut</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/news_hut/69318" target="_blank">📅 19:45 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69314">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/64a849aad2.mp4?token=E4H1q2AJi7Xr_P0sPap6iGPtjJtpGXGSIXguFEReUhiWfbuGG9RiNvdkQAgISW4rXqPBWdfssoZawg45ZN3HGYYhG6UgwjE5DSPJ1hFcgPiw1xlKA7JAHoSw8Z8QrGzzYUTeUNtba9Yf2NwBJFf_jsmfszD5WpNFN-253_LIw4OIBy1h7AqVvtdKKbcskGdB6Ykx6__HX_0N7Q7VT5VRKEIUJ-HBLnn1snCnyVn-zDelLl4x_qvRS_Scxr5VRwKdqtkTj94V98G4lxbYqLLgkrR9CD8ZF3xCn1Qyb1WwbF2-Jh7gckENm8BOZ-H6DUr670Sr9zdzQSBXScE8JqNwUQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/64a849aad2.mp4?token=E4H1q2AJi7Xr_P0sPap6iGPtjJtpGXGSIXguFEReUhiWfbuGG9RiNvdkQAgISW4rXqPBWdfssoZawg45ZN3HGYYhG6UgwjE5DSPJ1hFcgPiw1xlKA7JAHoSw8Z8QrGzzYUTeUNtba9Yf2NwBJFf_jsmfszD5WpNFN-253_LIw4OIBy1h7AqVvtdKKbcskGdB6Ykx6__HX_0N7Q7VT5VRKEIUJ-HBLnn1snCnyVn-zDelLl4x_qvRS_Scxr5VRwKdqtkTj94V98G4lxbYqLLgkrR9CD8ZF3xCn1Qyb1WwbF2-Jh7gckENm8BOZ-H6DUr670Sr9zdzQSBXScE8JqNwUQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⁉️
🇪🇸
آخرین آپدیت از وضعیت اسپانیا:
- مهاجرین غیرقانونی همین‌جوری تو سطح شهر پخش شدن.
- چندین مورد دزدی از فروشگاه‌ها گزارش شده.
- کنترل اوضاع از دست پلیس اسپانیا خارج شده.
- مردمِ محلی گروه تشکیل دادن و دارن هرجا مهاجر می‌بینن، کتک‌شون میزنن!
- تو بارسلون هم مردم دارن خونه‌هاشون رو از ترس مهاجرین، سیم خاردار می‌کشن...
@News_Hut</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/news_hut/69314" target="_blank">📅 19:39 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69313">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🚨
🇺🇸
ترامپ: به زودی، دیگر چیزی از ظرفیت نظامی ایران باقی نخواهد ماند.
@News_Hut</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/news_hut/69313" target="_blank">📅 19:36 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69312">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🚨
🇺🇸
ترامپ: ایران در تعامل با ما صادق نبوده است
@News_Hut</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/news_hut/69312" target="_blank">📅 19:29 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69311">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/14e0b272c3.mp4?token=IYUBdSWLoYbnN1aaWJb_b-g4YoQh43KraozN3YglwvMSp3XvME8ioHA9OfPaYzoZ00x64BPAOTresDjS3lhTWgy4KGIRgqjpqPTSlVX5hAEXEE7H7OAftXn67ou7vDmV0iM8hdJ7S8USwAcb-eIGlEj7BVDPKwuHcph_7ZKcN_ImEfbMCOBqJPSw0CKrFtakmI-dq5wkFCYouuI_hSLzBaKW6BWCpknPEeSV7G07U7rk0mY5dyinxxSOKFenvva2RMmgUTp-wrUOmXWS3lqRNx2YmxQApniZLeePRKP4Y51BkVIOT34MkaThG0_P3yAypmhOoI4025HBAWY7HAy9zA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/14e0b272c3.mp4?token=IYUBdSWLoYbnN1aaWJb_b-g4YoQh43KraozN3YglwvMSp3XvME8ioHA9OfPaYzoZ00x64BPAOTresDjS3lhTWgy4KGIRgqjpqPTSlVX5hAEXEE7H7OAftXn67ou7vDmV0iM8hdJ7S8USwAcb-eIGlEj7BVDPKwuHcph_7ZKcN_ImEfbMCOBqJPSw0CKrFtakmI-dq5wkFCYouuI_hSLzBaKW6BWCpknPEeSV7G07U7rk0mY5dyinxxSOKFenvva2RMmgUTp-wrUOmXWS3lqRNx2YmxQApniZLeePRKP4Y51BkVIOT34MkaThG0_P3yAypmhOoI4025HBAWY7HAy9zA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🚨
ترامپ با بالگرد «مارین وان» (Marine One) وارد «کمپ دیوید» شد تا سیزدهمین جلسه کابینه دولت دوم خود را در آنجا برگزار کند.
فاصله کمپ دیوید تا کاخ سفید با بالگرد تنها ۳۰ دقیقه است و رؤسای جمهور آمریکا از زمان فرانکلین روزولت (FDR) در سال ۱۹۴۲ از این مکان استفاده کرده‌اند.
نام این مکان برگرفته از نام نوه‌ی آیزنهاور، یعنی «دیوید» است که توسط خود او انتخاب شده بود.
@News_Hut</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/news_hut/69311" target="_blank">📅 19:09 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69310">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TQTmxReds7fgMeWH9GnXjd-JT4rmg9K2NKc6oLpyi0n6KoIMkvRT4dGsk6rTVIAJ_TqX6AjK18z2-XDYYje6Ls1uFUgOfJ-teHqVvZAFE5eAU2wgf4PNPBD9ZHmQcFRm2fcomp55ecGSvF6MYC3YuQGiqLwbTqufnbYi3Pzfv3S4kmodOuRxSjiMp5yS-AHX4c777pVxxhA0H_OkPhfcEdqnNjlmIZvRdJNOCuhVCZmu96GuPXcwoPASPD2_rNKs_C8mynKpY9z50BKujZrHOWTz3AjVAY9viyNe76uYCNRQC0ZzWn1dJCJ8QrhGcASEPylrqpzycLebbZynRdR_vw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
نهاد مدیریت آبراهه خلیج فارس:
به علت تداوم اقدامات تجاوزکارانه نیروهای نظامی ایالات متحده در منطقه، تردد از تنگه هرمز امکان‌پذیر نمی‌باشد. به محض برقراری ثبات و آرامش، کلیه درخواستها بر اساس ترتیب و زمان‌بندی بررسی و مجوزها به مرور صادر خواهند شد.
@News_Hut</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/news_hut/69310" target="_blank">📅 18:54 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69309">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">🚨
حملات پهبادی به جزیره بوبیان کویت
@News_Hut</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/news_hut/69309" target="_blank">📅 18:40 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69308">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/31550cb053.mp4?token=CJivoSzLY7TDX9tCRdoHU3JG4cqxY7Zj7t8Fpj-fu4_EGxgPIrMR0mhzjpWbxL8TmqakaYZ9pDyh6xxXMZz9DCkkay-R5JQl6JR9z5OuS7N0wCBywteHWl953fpcEJNJwdF0TIVrW7DKfMEJnVL-q6DFolm4M8bpW7yebaMEToZyV8v1grzNOSbVEReZs-SA18OVcM6ZMtnB-95HMGvjUZ8SB5j-OFtvLOAakWAW_ZijVzuDG-4YyvixWDd71zx_zZ6XaTo6Dw4Y1YJeKmF2FvUf5ULnqd8lyFOjHeOV3nsoj6Cqyso2ydknyM5ix8vYN9A-O6C8lI7bFXJcqf5_DQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/31550cb053.mp4?token=CJivoSzLY7TDX9tCRdoHU3JG4cqxY7Zj7t8Fpj-fu4_EGxgPIrMR0mhzjpWbxL8TmqakaYZ9pDyh6xxXMZz9DCkkay-R5JQl6JR9z5OuS7N0wCBywteHWl953fpcEJNJwdF0TIVrW7DKfMEJnVL-q6DFolm4M8bpW7yebaMEToZyV8v1grzNOSbVEReZs-SA18OVcM6ZMtnB-95HMGvjUZ8SB5j-OFtvLOAakWAW_ZijVzuDG-4YyvixWDd71zx_zZ6XaTo6Dw4Y1YJeKmF2FvUf5ULnqd8lyFOjHeOV3nsoj6Cqyso2ydknyM5ix8vYN9A-O6C8lI7bFXJcqf5_DQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
رئیس‌جمهور ترامپ در گفتگو با فاکس‌نیوز:
«اوضاع خوب پیش می‌رود. تنها کاری که می‌توان کرد این است که به پیروزی ادامه دهیم؛
آن‌گاه سرانجام اتفاقی خواهد افتاد.
ما ضربات سختی به آن‌ها وارد می‌کنیم و آن‌ها را کاملاً گیج و سردرگم کرده‌ایم، و همچنان به پیروزی ادامه می‌دهیم.
سرانجام آن‌ها چاره‌ای جز بازگشت به خانه نخواهند داشت.»
@News_Hut</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/news_hut/69308" target="_blank">📅 18:14 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69307">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SqCy8ZAA6HL0F92EZE9p0YDCiJlnny-G1SoVJnXSUX0UfKvnaY0cI2HMpPFME_RuvmJPXlP1FSpgBhycsUjj8hS0uYfBLAm4ZHcrY7tfGywlixupyAVqmSXaBdiCEI5fmWuBb301KzFGB38J4Ptq3zID7H_K9Zy1szjl2FeZGl9Bom7YP8H-XwWC6C3bRUqb_n1a_h-qaBKPiM2VZE4_fWAzLdh0DxXm63skVg0AAunP6JFByqzSWFJm0Aaa70RD9qHiK2bnaDFMJbzvrHgY74WDgP4SudtBA2B8r_PZtGeDgtBYkwi0uCUhN5BvvkxD6jik1bNJ8fb7L2gnXmkYsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇰🇼
❌
🇮🇷
وزارت دفاع کویت:
نیروهای مسلح پهپادهای خصمانه‌ای که اوایل امروز وارد آسمان کویت شدند را رهگیری و نابود کردند.
حملات ایرانی همچنین چندین سایت نظامی و زیرساخت‌های حیاتی را هدف قرار دادند که باعث آسیب مادی ناشی از سقوط آوار شد، اما هیچ تلفاتی گزارش نشد.
@News_Hut</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/news_hut/69307" target="_blank">📅 17:49 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69306">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4497b03176.mp4?token=nqL1o3CD57Nay1zmQRLdZioWou-D9FenzmM16fOMaxNY9V-UCrGS0I8t0di99wH3dVbisCN8ZndOrbTLdkiTthzPq1HzTrLxbjxiKYvq4tKHMdG1y8wa8xuARrEQGCHxCMAMILYv9W6uZuNW11moeLFk7UfbHVXa_hUT7Ch_ew8fLTZ3tIWiBfeuCSXwN9NXK6uJlASyqOUlUSF7lEIHrvdMttRHtq7hX91CCmZyiFbtkg0dOvg9RinRotPF9qjP3GomSMhT-Df2iDb9zx0t4iwfhrpdNylh_3zObefgHDwuwqMA44HBvi729ttzSJqfwgpi7lCMtdLSlv2qGLJptA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4497b03176.mp4?token=nqL1o3CD57Nay1zmQRLdZioWou-D9FenzmM16fOMaxNY9V-UCrGS0I8t0di99wH3dVbisCN8ZndOrbTLdkiTthzPq1HzTrLxbjxiKYvq4tKHMdG1y8wa8xuARrEQGCHxCMAMILYv9W6uZuNW11moeLFk7UfbHVXa_hUT7Ch_ew8fLTZ3tIWiBfeuCSXwN9NXK6uJlASyqOUlUSF7lEIHrvdMttRHtq7hX91CCmZyiFbtkg0dOvg9RinRotPF9qjP3GomSMhT-Df2iDb9zx0t4iwfhrpdNylh_3zObefgHDwuwqMA44HBvi729ttzSJqfwgpi7lCMtdLSlv2qGLJptA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
کابینه ترامپ برای بررسی اقدام بعدی خود در قبال ایران به کمپ دیوید می‌رود.
این خبر ساعاتی پس از آن منتشر شد که ترامپ از توافقی «تاریخی» با میانجیگری مصر، قطر و ترکیه خبر داد که بر اساس آن حماس با خلع سلاح کامل موافقت کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/news_hut/69306" target="_blank">📅 17:20 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69304">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/006b9f5bfa.mp4?token=EI0auyaRKEFckshP2k9Ver8Yx7di4M8qGjkRZBqLjRuSe3-GfLDCsWfeNsIyYiejifPWXdorL98NEm6bf7DZKhkvBST1kvW94TpmC-xJia9EjD7C03luLWowxWIEP6OTYFRTTqBDZc8aCRPR_463J_ZM6WZaEvdDZwvNGo5fFOrbiBrWrSXIHMHLIU9YoKRbwwmnwLsaGZUQL4T2RteyoPFpejYW90NQGktCXoFlzY9v2926sQoK-4tC1sqJ4Plnlf9bKP-yM6f6vw0wT7deBgq_TY_kqciTB259gH-UQ_g-hrzXb3uFxujum88gFgvqSYtKA6JqFKEXNYATRKLMjA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/006b9f5bfa.mp4?token=EI0auyaRKEFckshP2k9Ver8Yx7di4M8qGjkRZBqLjRuSe3-GfLDCsWfeNsIyYiejifPWXdorL98NEm6bf7DZKhkvBST1kvW94TpmC-xJia9EjD7C03luLWowxWIEP6OTYFRTTqBDZc8aCRPR_463J_ZM6WZaEvdDZwvNGo5fFOrbiBrWrSXIHMHLIU9YoKRbwwmnwLsaGZUQL4T2RteyoPFpejYW90NQGktCXoFlzY9v2926sQoK-4tC1sqJ4Plnlf9bKP-yM6f6vw0wT7deBgq_TY_kqciTB259gH-UQ_g-hrzXb3uFxujum88gFgvqSYtKA6JqFKEXNYATRKLMjA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
شهر سئوتا، منطقه تحت کنترل اسپانیا در شمال آفریقا، با یه بحران جدی امنیتی و انسانی روبه‌رو شده.
فقط توی یک هفته گذشته، حدود
1500 مهاجر
با شنا خودشون رو از مراکش به سئوتا رسوندن.
رئیس دولت محلی سئوتا گفته مراکز پذیرش دیگه ظرفیت ندارن، صدها نفر مجبور شدن توی فضای باز بخوابن و مراکز نگهداری از
کودکان و نوجوانان بدون همراه
با
2400 درصد ظرفیت
در حال فعالیت هستن.
الان به‌طور میانگین
روزانه 300 نفر
وارد سئوتا می‌شن و مقام‌های اسپانیایی نگرانن که دوباره بحران سال
2021
تکرار بشه؛ زمانی که حدود
10 هزار مهاجر
فقط در چند روز وارد این منطقه شده بودن.
@News_Hut</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/news_hut/69304" target="_blank">📅 16:49 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69303">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lSXBLqVaTEa8Gitv5WJzFk5yzHNgkz9aQADYG9rcG8PDndxLsjUEqCQEBJhqbIde8NpxiM11LN9tLHqYsVmneNUzOQeG0jFCmygkyBz6NYBjYkWftW-F0NuIqWb2sH8h2mZaMKcRAavrtQO274oRkzxXNlcTgYsQyI1lz_t-oEAbVhCfUCPSoqaYQNoA9CQqZYkMCQnvxp1St7117UpzbVSeBahUSFhXbdcv6MU3mBe50fgGx9IL6kfUNPMPoR8DhX3kTB4ah8CZ7in9k5fFQFPNGqljGK3WCYkz-G7EBdrmYowGmGE8NVgi-9eWzFLsIn3SQEdXpHrQ-JW2zjxyHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
پسر رئیس بانک سپه که دهه هشتادیه معاون بانک دی شد.
@News_Hut</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/69303" target="_blank">📅 16:20 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69302">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jxQI_ZKVKkrSbnUo4dzgEPEnX2fOgvGd8_HMc5RJoG_h9I0zzI8Qt_aGWrqpu0w5yUzpqIdHwsau7Y_GgOA7ZzaQwmfd6XfUdYwhe9JK_1I7p6xZRiqFFXdOsw5ekHeIcOHA662dsDz2OFqIyxE2gjKBTZGQ9PRO9As6_zOlSoU1LVg7UaqHdNnmvUriP9eJKifhxN71XhyuAKjWmKCcF6YWcKoVRtGr_bxe4gXtaSN_s8t4vnmTz9aHNu9ucazx6gprzqmDL3Fc9BcInNtB7pzwcMcdzyhDepowQZ0j0hALYMbzwQXqgMP3BYh0v8X8pZpW5PlVRiPehrkn5Ie17Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⁉️
طبق داده های نت بلاکس دولت ترکیه اینترنت کل مردم رو قطع کرده.
@News_Hut</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/69302" target="_blank">📅 15:50 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69301">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TmD6U9pVXgTGW_7wTLelFPIKmk1HlKHCxYAY0COoyHtLlyqTiry0XyzsLjIkk5aJltJDx4ZRBM1GJlNwu9vD2E9jgIw5EgJppXkioCb0iKyGoWSNBvEm4ItCwtg63Ov3eGDZS9V67O240-0UXP_o5h2fVzO8yuT6I6-xS9NYjahH4eI0Z1FjqmjLAhB4TzUPpsLgWxkXZ9XKv7VroGPgC0v_KrWJU8I2_V1KAX_kjoPiVJz7bmvumU0z7mUYxOEPF-7DP06wt72YrGTA4lyFL7q2oB1y02TyBQp4_dNQkaZsvzhrODFr81KY60ZqvRSi0-JEvYSPWch1JF_e3bxL8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
گاردین:
عربستان داره خودشو برای یه عملیات نظامی گسترده دریایی و احتمالا زمینی، علیه حوثی‌های یمن آماده میکنه.
@News_Hut</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/69301" target="_blank">📅 15:13 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69300">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🚨
🇺🇸
رویترز:
پرزیدنت ترامپ امروز در کمپ دیوید با مقامات ارشد دولت، تیم امنیت ملی و فرماندهان نظامی دیدار خواهد کرد تا درباره مسائل مختلف و از جمله جنگ ایران گفتگو کنند.
@News_Hut</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/69300" target="_blank">📅 15:10 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69299">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eb0ff0fef7.mp4?token=nSXRi1IvyAWZPAYGoqxbVFiDWX3-afD2lZ6bDOn6sFEa84pkjdwZWfpPdQnL2j1GkHbBz8K08JfWl1aD12VGxPMd5Aq_3Jr9jA9X3rUFB4TsGPo0c4oyMauXE8zOLb1WL35dw75Xeh_4Np3u9hwCgQvR86C5eop89gaDv9336RLC9rvGZaD7pH7tDGQwHjbY8k160RN2oqFrUhvXR7tII5JdIApUUQ2xkugsT9IjikLQxbsKn8edclLdrrqCI5L1pha2J3Gk7P1a4FlMpoCCYLrc7lBL5ah_DTt1_KkabCUk4KDBlo2RipsDZ6SKco53ktAX4pXdglHrEGJ38S6bCA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eb0ff0fef7.mp4?token=nSXRi1IvyAWZPAYGoqxbVFiDWX3-afD2lZ6bDOn6sFEa84pkjdwZWfpPdQnL2j1GkHbBz8K08JfWl1aD12VGxPMd5Aq_3Jr9jA9X3rUFB4TsGPo0c4oyMauXE8zOLb1WL35dw75Xeh_4Np3u9hwCgQvR86C5eop89gaDv9336RLC9rvGZaD7pH7tDGQwHjbY8k160RN2oqFrUhvXR7tII5JdIApUUQ2xkugsT9IjikLQxbsKn8edclLdrrqCI5L1pha2J3Gk7P1a4FlMpoCCYLrc7lBL5ah_DTt1_KkabCUk4KDBlo2RipsDZ6SKco53ktAX4pXdglHrEGJ38S6bCA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇷
🇺🇸
🇮🇱
تلگراف:آمریکا و اسرائیل در حال بررسی طرح محاصره زمینی ایران هستند!
به گزارش روزنامه «تلگراف»، آمریکا و اسرائیل در حال بررسی احتمال اعمال محاصره زمینی علیه ایران هستند تا فشار اقتصادی بر این حکومت را تشدید کنند.
دونالد ترامپ و بنیامین نتانیاهو در جریان گفتگوهای خود در دفتر بیضی‌شکل کاخ سفید، درباره «ابزارهای نظامی (کینتیک) و غیرنظامی (غیرکینتیک)» بحث و تبادل نظر کردند؛
از جمله اعمال فشار بر همسایگانی نظیر عراق و پاکستان برای تشدید کنترل یا بستن گذرگاه‌های مرزی.
یک مقام ارشد اسرائیلی به تلگراف گفت: «اگر مسیرهای زمینی را مسدود کنیم چه می‌شود؟ فرض کنید ایران دیگر نتواند هیچ کالایی وارد یا صادر کند.»
@News_Hut</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/69299" target="_blank">📅 14:52 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69298">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🚨
🇮🇱
وزیر دفاع اسرائیل ، یسرائیل کاتز:
اگر ترامپ از ما بخواهد، به حمله به ايران ملحق خواهیم شد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/69298" target="_blank">📅 14:14 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69297">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/34cbdd236b.mp4?token=tC1rsMlUDHsVDALGsuJS3FuG6vQ9T1GYOVL9x9Im0SNA9Su6y-_5GS042UdPsGCiyPCWxMdZNRLGaXbGl1MXLpZIpLL_RXNANW0WCLJrkWuU1zuoHKnHCaifnKEvVBPZ9e3Gs3msUmHZEP0N96ke4LX04pEGlbGgAA6iW2Xe1gnhbcJo6WXJH_SddL8ys1Mx1EhPrQuboNw3_bp7k6YXWmJ2qV4v6WyFD7fTOXpw9QE72qaZJHQkJxxW6cIZRV7PJdGQ7pg6HUwxcpnVWcOUsSsSaO70-Ikn08jE_MNSXQqFC299u7eAk_WJaMWu6ndd7fOfUmLJVuFwwyY7Fnvs-A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/34cbdd236b.mp4?token=tC1rsMlUDHsVDALGsuJS3FuG6vQ9T1GYOVL9x9Im0SNA9Su6y-_5GS042UdPsGCiyPCWxMdZNRLGaXbGl1MXLpZIpLL_RXNANW0WCLJrkWuU1zuoHKnHCaifnKEvVBPZ9e3Gs3msUmHZEP0N96ke4LX04pEGlbGgAA6iW2Xe1gnhbcJo6WXJH_SddL8ys1Mx1EhPrQuboNw3_bp7k6YXWmJ2qV4v6WyFD7fTOXpw9QE72qaZJHQkJxxW6cIZRV7PJdGQ7pg6HUwxcpnVWcOUsSsSaO70-Ikn08jE_MNSXQqFC299u7eAk_WJaMWu6ndd7fOfUmLJVuFwwyY7Fnvs-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تو عراق اهو گرفتن بکشن بدن به زائرا
@News_Hut</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/news_hut/69297" target="_blank">📅 13:31 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69296">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/37edae9b59.mp4?token=jU3vEQ88Rl9dJVVFBhoDrqxDQpydxBpAItANs2ZFgHFGuBDHPaFYVMH_oiQSS2u2TSnbwbkNnEKYpRbkiUpXKYLCBwCAF398rkZnjIW1dlvdX9uTE4EqaOUDwoVwihqJEGmx8XcQhaOgVhLNf_MWBiUmNtff4F9x2M0j09hfKgjMafFO5YucslkMS2Pkoht1h0YPGC3510qgd3dQUszlc3rNNA-uyIRO24V0R6Yqin3XVIz7Pc8sNCBjdgXCooKZHC6kXrUx9zcCntNf1uf5hleX1ByPgOGWaE4slswmdNd7Uc0s9zH6ls0fqtvWxnQOW8QTuPl0Cn0XFtb5q46ojw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/37edae9b59.mp4?token=jU3vEQ88Rl9dJVVFBhoDrqxDQpydxBpAItANs2ZFgHFGuBDHPaFYVMH_oiQSS2u2TSnbwbkNnEKYpRbkiUpXKYLCBwCAF398rkZnjIW1dlvdX9uTE4EqaOUDwoVwihqJEGmx8XcQhaOgVhLNf_MWBiUmNtff4F9x2M0j09hfKgjMafFO5YucslkMS2Pkoht1h0YPGC3510qgd3dQUszlc3rNNA-uyIRO24V0R6Yqin3XVIz7Pc8sNCBjdgXCooKZHC6kXrUx9zcCntNf1uf5hleX1ByPgOGWaE4slswmdNd7Uc0s9zH6ls0fqtvWxnQOW8QTuPl0Cn0XFtb5q46ojw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇮🇷
روابط عمومی سپاه پاسداران:
ساعات ابتدایی امروز  ۲ نفتکش متخلف به خیال اینکه میتوانند از مسیر غیراعلامی ما، تحت اسکورت هوایی ارتش کودک‌کش امریکا عبور کنند، بدون توجه به اخطارهای ما، در مسیر ناامن و غیرقانونی حرکت کردند که مورد اصابت قرار گرفته و متوقف شدند.
@News_Hut</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/news_hut/69296" target="_blank">📅 13:06 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69294">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/mk958IZRPwfdxOOY3CZ93SEUw9hCLeqiG4-zFeAmkfkfsIQFt1mLBf8VXKMQhuI9P51eeNBkFFRT1XHh6kACxyTkRhk2bf0A-LOKIF3xytdgGRegH-yO1ElUfU_ct8buTNqMZ3wId2s4dTBziigBBhoVtjC9Ty7Kka7Z3A8ocUq7_At08EV5UwntKFew2g7rO4s00S9ZPMKnz1HsZ447GtK-4lAFe1FmPGqhivP5l2QgEh3O0R4sjpnua5kQT3Phd5fXt3CyjFbLhLzLJqHl3VDmwybcS6C9yx8s_b81ZRabFbIpjEXmDfmqnvnkoFwvU3kTVdNpw3PSMnigREeQaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/bb843e99ad.mp4?token=GPQUGaObmIzl2760Wz3-4ps_Zt91HEChTxkkBuDJwf3h8oQcBQdPvnPVDKC_htYPb0_dkRFixK_jUQ9NMb5-ovwFoDAbp2f26G2CS2ZpCXezNCTTlDwP5TMEr7q8KcuPc1pXIT1n4JcHBH4BIOrPlwV0B4fO2yzjQcQ8ZvjxShz2jZi0t7_AWWexp5hZu3uTF9W6MObM-pp-8tre_b_DgD-pIpv24CLpzAb4yowoelp0VH3_nq6Wmed-Pio-WfKPDj_UVlMBMbN2DPleCzhCy2NcrIrGN_IhpG6k-rchpok8vXutdjUw8VtrCCEssPvG-MvWAXJJJVm45D4gauFEGg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/bb843e99ad.mp4?token=GPQUGaObmIzl2760Wz3-4ps_Zt91HEChTxkkBuDJwf3h8oQcBQdPvnPVDKC_htYPb0_dkRFixK_jUQ9NMb5-ovwFoDAbp2f26G2CS2ZpCXezNCTTlDwP5TMEr7q8KcuPc1pXIT1n4JcHBH4BIOrPlwV0B4fO2yzjQcQ8ZvjxShz2jZi0t7_AWWexp5hZu3uTF9W6MObM-pp-8tre_b_DgD-pIpv24CLpzAb4yowoelp0VH3_nq6Wmed-Pio-WfKPDj_UVlMBMbN2DPleCzhCy2NcrIrGN_IhpG6k-rchpok8vXutdjUw8VtrCCEssPvG-MvWAXJJJVm45D4gauFEGg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">علی خامنه‌ای توی کربلا در حال پخش شربت دیده شده
🤣
@News_Hut</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/69294" target="_blank">📅 12:33 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69293">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sEJsSakApHQn_fCvm3pE1ModjI90eBd_l07yzFJ-4sITWshtOyJJ4VWPj3n-ZcK_JO4qXMS2mXt6bXt_6oLtYmKfGPaPMH-SAowkbKN8e_dWn5or02wr7SlR_Uyp8hvR6AJyXGg8kfnd6zHeStaVtS1JNzr9_bUPnVOmzNfGVNCn2a42iMdgAI8Xk6KmNKWw8WpGmq0MD73cFKXruw_GkTAZVtxVogu-h6MUrZdIG2RDwsC37Eruy8wzKrBAll0kXtyToHJjmV53_Cb2-YNVmC7deRcc4ALe0EmX5kAB0teLLeU5cbppBucS1yCnKzNOvaKGbznTCFJIhOtII4fHFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
گاردین:
یک موشک بالستیک روسی کارخانه تولید پهپاد در کی‌یف را که متعلق به شرکت «ترمینال اتونومی» (Terminal Autonomy) —شرکتی ثبت‌شده در ایالات متحده— بود، منهدم کرد؛ این نخستین حمله شناخته‌شده روسیه به شرکتی با مالکیت آمریکایی در اوکراین محسوب می‌شود.
این کارخانه پهپادهای تهاجمی مجهز به هوش مصنوعی تولید می‌کرد و گزارشی مبنی بر تلفات جانی در این حادثه منتشر نشده است.
@News_Hut</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/69293" target="_blank">📅 12:15 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69292">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P4sSqw4Li3PgrW9pSF2smJMjcPphOeTjIxmoAbRrbGbbeeX8JwT5TIa7fpGq_OmQ4lgujywDCgElnXozqiKTjCmB2I7ELIGzu9_qE_X-OIBAGJDfZV50Ew8z4vv-jiefLdTvT0xoJTIljzItp7H3BO47CjaCfDdiieM4tzSxhCnuzL_peY-XzJnFgpyD5TgUQcnTsKYbuD2SfbE9KGuGP2ar_iW_NeaIqEO9Gs4eU0Hkz69P5I4M1OsqP7DzIu4ut0xwP8o_BKPPEg0iWekVK-EBbQkV_NpKOvpjOtvlfWlIVZDVJFk2b28jCqW_c54jhhqVnJwHuPEGPbhGAPAijQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
باراک راوید:
به گفته یک منبع آگاه، مقامات سپاه پاسداران از هیئت حماس که برای مراسم خاکسپاری علی خامنه‌ای، رهبر عالی پیشین، به ایران سفر کرده بود، خواستند که در امضای توافق‌نامه عجله نکنند و وقت بخرند.
یک مقام ارشد آمریکایی مدعی شد که ایران تلاش کرد حماس را متقاعد کند تا این توافق را امضا نکند، اما این گروه تصمیم گرفت به این توصیه عمل نکند.
@News_Hut</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/69292" target="_blank">📅 11:31 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69291">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6a885a777d.mp4?token=gPGO3UnpOLHAteuIWBfodb77oJPjxLcFOOYH8PiAKIhX0qNhQ8Nwkd_1j3a7EdWbpUMpdQNyRGxac9Qdl3oOvVn1eWW4G2z0AS8hMxy5IWEX7RIWEngkoPuOKdXZKK_rxNoq-fFW4lmy7mvZoRm6ybEDe6CzKGpfiqzhAgU9_9qBtdg_B8BpSO94Fb0P5WT1QJZ-qoSlNvaoWaDwxUJtP4jUix1VV7nq0RkMPcisiW-1aYibAT75SWtKCwlJjEzY7zkhX0mgJKRyFEpMd9TpDikO5cDHglUPob25brnSpZI2CMndBJWrWwrZkkUiZZgneYmGliFfwWvgsYn9SYlPIw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6a885a777d.mp4?token=gPGO3UnpOLHAteuIWBfodb77oJPjxLcFOOYH8PiAKIhX0qNhQ8Nwkd_1j3a7EdWbpUMpdQNyRGxac9Qdl3oOvVn1eWW4G2z0AS8hMxy5IWEX7RIWEngkoPuOKdXZKK_rxNoq-fFW4lmy7mvZoRm6ybEDe6CzKGpfiqzhAgU9_9qBtdg_B8BpSO94Fb0P5WT1QJZ-qoSlNvaoWaDwxUJtP4jUix1VV7nq0RkMPcisiW-1aYibAT75SWtKCwlJjEzY7zkhX0mgJKRyFEpMd9TpDikO5cDHglUPob25brnSpZI2CMndBJWrWwrZkkUiZZgneYmGliFfwWvgsYn9SYlPIw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏸
ویدئو وایرال شده از یکی از مراسمات عجیب آفریقایی ها که با شمشیر همدیگه رو میزنن
🙂
@News_Hut</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/news_hut/69291" target="_blank">📅 11:15 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69290">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u8Ieut9sTHWkJ6nQtZvoNqWPBlTqRCIaoLMfbdVONptPBB3X9p_zzmEcj3Z2gE7Ifj7NPuGg_VpJqQCnnod2JDEQdCDbryB_JUKorOtwyaPzaK1D7xk-imlkGWALtehRUmk7xE75_9eOCRdZPki6Kasou9DhLg8uYT3a5yXvFvcct39_FtqCemmrxAy2A9pkF7y2vj-onvga074ITYWUD0FD_p4e9ABiJjQwbaCZd1n6IE5iXYf7EHTBsyo7Oszlrs6Dfbt11rkPaIl9MEoL8VrLyYgdKMSRVgS4Qu2lTh4yRGhGZffYJQwwPP8P4oDMMVzg8tuvYyLISQ6h0SjB2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
🇮🇱
🇮🇷
تایمز:سازمان سیا و موساد اسرائیل در حال تشدید جستجوی خود برای یافتن آیت‌الله مجتبی خامنه‌ای، رهبر جدید ایران، هستند که از زمان جانشینی پدرش پس از حمله هوایی فوریه ۲۰۲۶، در ملاء عام دیده نشده است.
مقامات اطلاعاتی معتقدند که او در این حمله به شدت مجروح شده است، بیش از ۱۵۰ روز از استفاده از تلفن یا لپ‌تاپ خودداری کرده و در یک پناهگاه زیرزمینی به شدت محافظت‌شده، احتمالاً در تهران یا نزدیک قم، پنهان شده است.
با توجه به اینکه نظارت الکترونیکی سرنخ‌های کمی به دست می‌دهد، جستجو از اطلاعات سایبری به اطلاعات انسانی تغییر یافته است.
مقامات سابق موساد می‌گویند که اعتقاد بر این است که مجتبی از طریق چندین لایه پیک ناخواسته که پیام‌های دست‌نویس حمل می‌کنند، ارتباط برقرار می‌کند و نفوذ به حلقه داخلی او تنها راه واقع‌بینانه برای تأیید موقعیت مکانی او - یا حتی اینکه آیا هنوز زنده است یا خیر - است.
برخی از چهره‌های اطلاعاتی گمان می‌کنند که سپاه پاسداران ممکن است مرگ او را پنهان کند، در حالی که برخی دیگر هشدار می‌دهند که رژیم ممکن است از بدل‌ها برای پنهان کردن حرکات او استفاده کند.
@News_Hut</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/69290" target="_blank">📅 10:34 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69289">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e9be197f29.mp4?token=PWKcxfxe_MnmA6vsAJ-dEkDdAmL1v-73CGuwu_8ncxof6n1PgyeNAXph3BSXLtma_NxIGpwZnZ5gqLuc8ZB8NgyrYbsV3tUh-FvtzGhWAptKB45JejwXzwdj5Ma7AMtAfYX_QO3uQZKeNvJS0bW-UnHrwXQqs3_gZ6zT8NAWZvHQ6AhZ_JssR2wtc55D0DVscSsh2IQ7nAj7-wWFC8au4TQcXeDayJ3TCVawhAkkR_qpZeN_Xv-6Aes0_fbP_PofP11YAqoU5a2a9AdJEWf8BNQTEg0FXthTkyVJeudzXFo_MKZaENPhSveF2br-8GmC32VBaMEcE6ZmmDFZnxcI1A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e9be197f29.mp4?token=PWKcxfxe_MnmA6vsAJ-dEkDdAmL1v-73CGuwu_8ncxof6n1PgyeNAXph3BSXLtma_NxIGpwZnZ5gqLuc8ZB8NgyrYbsV3tUh-FvtzGhWAptKB45JejwXzwdj5Ma7AMtAfYX_QO3uQZKeNvJS0bW-UnHrwXQqs3_gZ6zT8NAWZvHQ6AhZ_JssR2wtc55D0DVscSsh2IQ7nAj7-wWFC8au4TQcXeDayJ3TCVawhAkkR_qpZeN_Xv-6Aes0_fbP_PofP11YAqoU5a2a9AdJEWf8BNQTEg0FXthTkyVJeudzXFo_MKZaENPhSveF2br-8GmC32VBaMEcE6ZmmDFZnxcI1A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ویدیو وایرال شده از حمله عجیب طرفداران حکومت به بنر ترامپ و نتانیاهو
🤣
@News_Hut</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/news_hut/69289" target="_blank">📅 09:52 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69288">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">‼️
دلایل سقوط شوروی که صداوسیما پخش کرد در مقایسه با وضعیت الان ایران!
@News_Hut</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/news_hut/69288" target="_blank">📅 09:15 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69287">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/418bb6362d.mp4?token=FldTbxpAMZD8V4tXYaOmcq1h3iH4zQbxu3KWtzCApnJUzSRtEvfP3KRrMhTLsg2SHflm_Xgs158V5xPrQs_qTBx4DtPA2tYz15NvqYnG1q022jinuKIvrR9mmLJRQzp6J1lRnvPEATVTZzR-PEUS4pYvezFqzcYimOiK9ZmJtPXVAhqcA8OM0OkZxPZCZRUWhUPsUkhcjE3Tlf2BkvAEpaMXXzFHkCVMlJwHz5G9K-QXP_9xrbO7F_O5VhH9EOECPMoId3z4EvSXqY1dq2-Uw2HWSeji72VLnJOjxg_Obki4GmxNinZgfW3lRO3X6rL3JWKXBFakU1wHjD9Y9iUzJA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/418bb6362d.mp4?token=FldTbxpAMZD8V4tXYaOmcq1h3iH4zQbxu3KWtzCApnJUzSRtEvfP3KRrMhTLsg2SHflm_Xgs158V5xPrQs_qTBx4DtPA2tYz15NvqYnG1q022jinuKIvrR9mmLJRQzp6J1lRnvPEATVTZzR-PEUS4pYvezFqzcYimOiK9ZmJtPXVAhqcA8OM0OkZxPZCZRUWhUPsUkhcjE3Tlf2BkvAEpaMXXzFHkCVMlJwHz5G9K-QXP_9xrbO7F_O5VhH9EOECPMoId3z4EvSXqY1dq2-Uw2HWSeji72VLnJOjxg_Obki4GmxNinZgfW3lRO3X6rL3JWKXBFakU1wHjD9Y9iUzJA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
خبرنگار :
کشور های منطقه که مورد حمله ایران گرفتن آیا باهاتون تماس گرفتن و ارتباط گرفتن ؟؟
🇮🇱
نتانیاهو:
بیشتر از چیزی که فکر میکنی و بیشتر از چیزی که میتونم بگم اتفاق افتاده
.
⏺
خبرنگار:
هدفتون درباره حکومت چیه
.
🇮🇱
نتانیاهو:
خب هدف مشترک من و پرزیدنت ترامپ مشخصه اگه بتونیم تهدید ایران به طور جدی کاهش دهیم توافق های صلح زیادی انجام میشه
!
@News_Hut</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/news_hut/69287" target="_blank">📅 02:26 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69286">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ct91JfTsh0Mz9X4HnX-i5oJyhc6n7R__beDWwEsMlZAgXeQ71nFf6efKbus6siOZFvBRicwDx7OVqHT_TuT6dDVehCu8bUU_BLfeDAWJ06GVl_kV1s09ihTpje9D9MXpzF_dsP5_GdOHZzs6Ko_Zc2e7VACUQaYab-QuPBAIcLqMXTPlteV6Gxk47Iah7u_7_cqt7F24Oon_aCC12y6znhsZlyvJY0BPxqBVhAEVaGZ3pV57sFcH-mRAueFLXyzhfSAKIOqEZnwK3sMzBmssJ4n34M2bZlW51h-oC1T0NEaX7aKOitvQhzQkmDkoAHgSwd8g1NADlV3zfgQuM-WijQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇺🇸
پرزیدنت ترامپ:
امروز، «شورای صلح» به توافقی تاریخی برای خلع سلاح کامل حماس و تمامی دیگر گروه‌های مسلح در غزه دست یافت. این گامی عظیم به سوی صلح و امنیت پایدار است.
این توافق گامی حیاتی است تا غزه سرانجام تحت اداره یک دولت جدید فلسطینی قرار گیرد؛ دولتی که برای یاری رساندن به مردم فلسطین، همکاری نزدیکی با «شورای صلح» خواهد داشت. هم‌زمان، اسرائیل از امنیتی که شایسته آن است برخوردار خواهد شد و غزه دیگر به پایگاهی برای حملات تروریستی بدل نخواهد گشت.
این رویداد، نقطه عطفی بزرگ در اجرای «طرح ۲۰ ماده‌ای ترامپ» محسوب می‌شود. این توافق طی مراحلی با برنامه‌ریزی دقیق اجرا خواهد شد. هم‌زمان با تکمیل روند خلع سلاح، نیروهای اسرائیلی عقب‌نشینی خواهند کرد و «نیروی بین‌المللی ثبات‌بخش» با همکاری نیروی پلیس جدید فلسطین، مسئولیت تأمین امنیت غزه را برای ساکنان آن و همسایگانش بر عهده خواهد گرفت.
یک سال پیش، شاهد جنگی شدید و خونین، بحرانی انسانی و نگهداری گروگان‌ها در شرایط اسارتی بی‌رحمانه بودیم. ما به پیشرفت‌های تاریخی دست یافته‌ایم، هرچند هنوز کارهای بسیاری در پیش است.
می‌خواهم از میانجی‌ها — مصر، قطر و ترکیه — به خاطر تلاش‌های مهمشان و به‌ویژه از تیم فوق‌العاده‌ام که با تلاش‌های خستگی‌ناپذیر خود دستیابی به این موفقیت تاریخی را ممکن ساختند، تشکر کنم.
اجازه داده نخواهد شد تهدیدی که در ۷ اکتبر از سوی غزه سر برآورد، دوباره بازسازی شود!
بر اساس این توافق، غزه سرانجام در اختیار دولت جدید فلسطینی قرار خواهد گرفت که در خدمت مردم خود است.
این دستاورد شگفت‌انگیز را — که همگان دستیابی به آن را غیرممکن می‌دانستند — به همه تبریک می‌گویم!
@News_Hut</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/news_hut/69286" target="_blank">📅 02:04 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69284">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X9ROA_97NsEowmecbKRNBn-j1_72ovuAahO-7eDsmQ3PVCVv-DORcxR3djXtC8wqo8-Fy66J1O5EtqNWfoCYWqg0XqWe77_C4tEe6-IM04-x9MmJf-RmA4Tc8zA06dJddoxv__D326-blqYFUdy5glAEvaGwGeIGg0djpQVE2THJ73NZobXw2nT1N4vnDxDtjwk5zZxvRlObaQl36D2TyBD1tJ6KViGzyUwukCaJyzt8JEOBf9rG3SinrvbWxBJdPWNjQJRJYU2lT1IkapT6CTZmcpjeJgsbsLSBixyB0EWDbz51WfDmpkX-jxQMRZA3C3T-TmoJww2hpguCt0LHJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fad9bb4c4a.mp4?token=iCUmmWenFpQl-CbabNRnSJBEKKnTQ6KxOcaGg4Dqm6UV604muf54UrUW2wTAnmFQ3c6Tcer-YjXWb3sPsH03yrA7TuMBGTNH7JB3ErfNR_se4y5sOtJvCHiotnhGz9nI10Qlzdh3N64n82XCk5RgvAK1rWApVOrT8Kn5oZavUwwESc9YIzFjnRZwVKGxsydgRDGIfO6dHzo9HzEp9tdmGEnXxrtAehiMZWAB0ZGD0HmAk-GHyrE9ZCFPxTS1qq-QlawFT5RpIwuissk5RVGHL4ghisVs6JO6oT-WRErRSdeInGgCYRucLHWfjw2NzJFaEJECxmrYUC_bC4m4fsbgVQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fad9bb4c4a.mp4?token=iCUmmWenFpQl-CbabNRnSJBEKKnTQ6KxOcaGg4Dqm6UV604muf54UrUW2wTAnmFQ3c6Tcer-YjXWb3sPsH03yrA7TuMBGTNH7JB3ErfNR_se4y5sOtJvCHiotnhGz9nI10Qlzdh3N64n82XCk5RgvAK1rWApVOrT8Kn5oZavUwwESc9YIzFjnRZwVKGxsydgRDGIfO6dHzo9HzEp9tdmGEnXxrtAehiMZWAB0ZGD0HmAk-GHyrE9ZCFPxTS1qq-QlawFT5RpIwuissk5RVGHL4ghisVs6JO6oT-WRErRSdeInGgCYRucLHWfjw2NzJFaEJECxmrYUC_bC4m4fsbgVQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
دیدار عجیب نتانیاهو با یک سناتور!
امروز نتانیاهو با جان فترمن دیدار کرد و طرف با شرتک نشیته بود و سرش کلا تو گوشی بود
@News_Hut</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/news_hut/69284" target="_blank">📅 01:54 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69283">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">عجب سکوتیه، موشکی راکتی چیزی نداریم؟
🙁
#hjAly‌</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/news_hut/69283" target="_blank">📅 01:48 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69282">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromلیوه</strong></div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/news_hut/69282" target="_blank">📅 01:42 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69281">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">عجب سکوتیه، موشکی راکتی چیزی نداریم؟
🙁
#hjAly‌</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/news_hut/69281" target="_blank">📅 01:35 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69280">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">▶️
تیزر جدیدی از سینمایی Spider-Man: Brand New Day منتشر شده که دیدنش خالی از لطف نیست.
@News_Hut</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/news_hut/69280" target="_blank">📅 01:18 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69279">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IeEsqqnl11_XkM9n1UAEnVw0k-PLIw_UsmiRoEYH5e05UydlFVctEoh_j2BlpFvlhrGdpQqdlGjeNXtmZC6NZKcjY4-4Q5l70veFL8X2QG196Toe4snBys1lXLEwrHPn4KpRmfGTdT02S8jo8Ge0Vq882s42wkUOsAT1afzY1YpnThCFHH8n3uxCoC8crcehSfT085jZmP_KnZceFXTyz1ojHDK7CbuhEiPwFyDqUB6jRb6X7pRLiCac6AJ_MoftFQ71mCtnirMHPmXY4AagrAAwOXRz-fcKSE4sxFHtaHUU0hEbnWjMFwheKmY98HH_AXnEhcP0tR_CL20WQEXTjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
قالیباف:
«آمریکا هر روز یه جنایت جدید انجام میده. حمله به خونه‌های مردم عادی توی جزیره قشم، ادامه همون جنایت‌هاییه که قبلاً توی لبنان و غزه انجام داده.
آمریکایی‌ها عادت دارن هر وقت توی میدان نبرد کم میارن، با ریختن خون آدم‌های بی‌گناه جبرانش کنن.
ولی بابت این کارشون، تاوان پس میدن.
@News_Hut</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/news_hut/69279" target="_blank">📅 00:58 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69278">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cba260d124.mp4?token=AGM0odpYAO5zIipjfTGbuA8OBHbGDFfYN65PY-ITHo4SRtBmcqjbvnCbX1cDu4OK0fRvxQbmVHSu841RhSOHhG8tH7Hcgo6suZH1xDqyMScduw_v47infv8_WP57o8AASXyYeAT52pRBZ0ypyeFmSJkkWV4iPUoIfSRjqqRWJjJT1ETHwlIhVU_5nkHstqPo-5bUOb7PikcwsMOtjvdQioal5zcBIEvYrMqO78poUEayY71d57VJpMi8VqL9mfKE-TRTfU2AFEsEX4Fg5wbcPJKl3RfMr_fUem-pDXtI7bTD-f3K9JaO09hzt5kj9WB0TJXdPU1gytfDhy_aoi2esQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cba260d124.mp4?token=AGM0odpYAO5zIipjfTGbuA8OBHbGDFfYN65PY-ITHo4SRtBmcqjbvnCbX1cDu4OK0fRvxQbmVHSu841RhSOHhG8tH7Hcgo6suZH1xDqyMScduw_v47infv8_WP57o8AASXyYeAT52pRBZ0ypyeFmSJkkWV4iPUoIfSRjqqRWJjJT1ETHwlIhVU_5nkHstqPo-5bUOb7PikcwsMOtjvdQioal5zcBIEvYrMqO78poUEayY71d57VJpMi8VqL9mfKE-TRTfU2AFEsEX4Fg5wbcPJKl3RfMr_fUem-pDXtI7bTD-f3K9JaO09hzt5kj9WB0TJXdPU1gytfDhy_aoi2esQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
سنتکام:
یک فروند هواپیمای P-8 Poseidon(هواپیمای شناسایی تخصصی) نیروی دریایی ایالات متحده در حین گشت‌زنی در خاورمیانه، برای سوخت‌گیری به یک فروند هواپیمای KC-135 Stratotanker نیروی هوایی ایالات متحده نزدیک می‌شود.
@News_Hut</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/news_hut/69278" target="_blank">📅 00:25 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69277">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MPMBJOVObv3PwIag2mPErrvdfUUPYBa_92uwpNML9DnMLEfY2_iwKaavFm1MYLyY2OHTAllGMehGBJZ0ZSGVbw_YaLPy2VWR7n2-q0Ozjw4n6urGPdPp7ThwdX6-RujE3WWZxCZXNARAu--Uad59RmFjlVRsk7EpZUjQAKCS-nRtE1Zv6pV3Qi4Q8WGokUW5D_4qeHFHCdT3TwaSZUhu5qvY0g88P5sFGyKLxqLYeQrdhsDU9FE_ZkOLpgoKo_p7KA7zYKYfR2OitjHUrOJDzMLIdEnsA8jUMqpv5uZfkMAav6406rw9Z0aXzsgOBW3N21fl8r0IY9acsG4GAInlCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
آی‌24نیوز:
اسرائیل کاتس، وزیر دفاع اسرائیل، روز پنج‌شنبه به همراه ایال زامیر، رئیس ستاد کل ارتش، جلسه‌ای برای ارزیابی وضعیت امنیتی برگزار کرد.
در این جلسه، تصویری از وضعیت اطلاعاتی و عملیاتی، سطح آمادگی ارتش و طرح‌های عملیاتی برای سناریوهای گوناگون در عرصه‌های مختلف به کاتس ارائه شد.
@News_Hut</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/news_hut/69277" target="_blank">📅 23:54 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69276">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/89da715482.mp4?token=Edl79biCR02PRabkgro2JkEfjPhlBozPwuCIlvQkiBGhTL2wmKipQe3ZpFl817tUuA7W4WQTM4uxmi9nSZl3sQQHrErAR6WPgX1MI4CYfmD3q1ouF_TTmu3g44oX4dQ-EbDF7rzM-5jph3YuDZEmpkuARqx6CakoihyKOa4mkrZhYqkx5WInO4EdaxsxiC-1MF7rY2W-GfSlvzwnAoavcn6K6_wTlos6kwFpj7ZliSVUmrm2RoZcICDWcy8OnkRcCOE3Wi0kSUDD3gnXaI1VuHrXYDgU_PySXXodlaaTeXd5xeoD9N5T-tPgdKxPCmmQ4RSFcMEnNmbFhfVv9zAuIw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/89da715482.mp4?token=Edl79biCR02PRabkgro2JkEfjPhlBozPwuCIlvQkiBGhTL2wmKipQe3ZpFl817tUuA7W4WQTM4uxmi9nSZl3sQQHrErAR6WPgX1MI4CYfmD3q1ouF_TTmu3g44oX4dQ-EbDF7rzM-5jph3YuDZEmpkuARqx6CakoihyKOa4mkrZhYqkx5WInO4EdaxsxiC-1MF7rY2W-GfSlvzwnAoavcn6K6_wTlos6kwFpj7ZliSVUmrm2RoZcICDWcy8OnkRcCOE3Wi0kSUDD3gnXaI1VuHrXYDgU_PySXXodlaaTeXd5xeoD9N5T-tPgdKxPCmmQ4RSFcMEnNmbFhfVv9zAuIw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
چند روز پیش یه پسر بچه به اسم امیرحسین رو آورده بودن صداوسیما که اینجوری جواب سوال مجریا رو داد
:
مجری:
منو عروسیت دعوت میکنی؟
امیرحسین:
معلومه که نه
مجری:
کارشناس برنامه، خانم دکتر رو چی؟
امیرحسین:
فرقی نداره، اونم نه.
مجری:
مامانت چی؟ اونو که دیگه دعوت میکنی؟
امیرحسین:
وقتی زن بگیرم مامانمو میخوام چیکار
@News_Hut</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/news_hut/69276" target="_blank">📅 23:40 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69275">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/671ccf87ea.mp4?token=hK2zzTrH9wDBtWQSz3DPT2eORV3Kuix5N8U6suFT5-d87by6s7717tN6t6pOdGjdi9cRi94KfAEWtZUKQ_tZQovgJZtd7BPJJMQYXO6KXMLibtgFhXeFh6A8D37fDa2ci69swHi0Y3YL-7VkoH1FzeYZNy-BZJslOV24x6Pnorr9CbiEeercNeYsLI9ROnmI1R77rWvSWVyIZ1fztW0f0keIzs_1icd8gohg7il4g8akD8kmHuhzLCiWM2wcCfrPGjXCptcJikr8Kgeg9KeAeeIxL33wfN2uxjvHG6xbNU-mMVOfAQFA5gJwP40ECRxoXqCctJ2VVVpTeXrmsz-2sA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/671ccf87ea.mp4?token=hK2zzTrH9wDBtWQSz3DPT2eORV3Kuix5N8U6suFT5-d87by6s7717tN6t6pOdGjdi9cRi94KfAEWtZUKQ_tZQovgJZtd7BPJJMQYXO6KXMLibtgFhXeFh6A8D37fDa2ci69swHi0Y3YL-7VkoH1FzeYZNy-BZJslOV24x6Pnorr9CbiEeercNeYsLI9ROnmI1R77rWvSWVyIZ1fztW0f0keIzs_1icd8gohg7il4g8akD8kmHuhzLCiWM2wcCfrPGjXCptcJikr8Kgeg9KeAeeIxL33wfN2uxjvHG6xbNU-mMVOfAQFA5gJwP40ECRxoXqCctJ2VVVpTeXrmsz-2sA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
نقدعلی، نماینده مجلس:
با وضعیت حجاب میخوایم چیکار کنیم؟ والله جوابی برای خدا نداریم.
یه نماینده مجلس به من گفت از درد بی‌حجابی هر شب تو خونه گریه میکنه و خواب و خوراک نداره
😂
@News_Hut</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/news_hut/69275" target="_blank">📅 23:15 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69274">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dGVpWjV1xnqziJOGpHF3Vw9H1jfktTSumS99U6bsb5B3VWBE223yyLkDWhbS7VJg546qLapGRPU7MUaFy5RsRdIZO_KVLNexROIPuznB5f3IbBA7SP_w1qiGS61jM4x7wHGXfDlMtWHdAthEVP_20sEe_-iP7Ym607Bk2_Ow9xnsbMFwg_pE1YZ4mTpc-y2UExau25TEyVmF3MP-j9-go19C2Ml67O6UY7FSFSieILlAHX6SMJEQ4yX86BQ2ugKRIzGlMlGGU_KQ1vkysYOooyGIat6nEAiui02KINZXZXSEfZ7PKh6CqwYg0v5Ww8zvmrgAaVNVipZgvYj1c-Lw2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اعدام می‌کنید؟ به‌به چه کتلت های تر و تازه‌ای داریم امشب  #hjAly</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/69274" target="_blank">📅 23:04 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69273">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0b3fe31b5c.mp4?token=D_nMj9J2S-M2_2aUvqdOBl3t_2q2ZFjBlagMGSqY1wTwAZnE02vH4UAHMcroXgYp6KXFcwogfgyOu7L6AVoBGr-eFChiVIDtO4HM872vyvAgftADKStthu-wwOhvoV-xfH5awb_D6rZSUUcAiANQXvxpVSfaut3phFov5ify8MudS60TrJSvIHOg5IajkCjStnNjESQhzib47V3C7y8OXuISEPbQxGbasjvGqLA9tyW203Q_ipzhwuyLvhSmbYHXhJ47PT53qJqkVGH1IR9A4F-mka-G37oidKvlwqagRadCv4xeDVERPl63S9hx6fKg1YhjBnmStPLeA5o23NSi6h5OKeme4OjqWhy7We0D8UOwx2ZrEINmGI1s3n1_QVHpDxcMapkAR_OpjU2vGY_LMDAANb3_WTBq-6BXjQy9Jxi9Qz5EY8Sp7H1sRdWfJPa0EiyeteiLwZZZQRnAe2RQC-7S4wjmiqSzLa4zx4M2r5mQZMcrah7PioFsc2DvJ10wq9mp05cOjwkWC8jDHZjkdFKWr37yNToizcNAQkN1aXX3p-I79xCTv5Bguo_0XFsjVVvHqYi978DXxPwTf0ocMLkxfaUjuqlWrtfVpLuXKRN0Ad9xrwuaiORebVfA0cDiPA8VM7NbYzkO39c45diembr7rndhS4rxhlzVt4MVcQc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0b3fe31b5c.mp4?token=D_nMj9J2S-M2_2aUvqdOBl3t_2q2ZFjBlagMGSqY1wTwAZnE02vH4UAHMcroXgYp6KXFcwogfgyOu7L6AVoBGr-eFChiVIDtO4HM872vyvAgftADKStthu-wwOhvoV-xfH5awb_D6rZSUUcAiANQXvxpVSfaut3phFov5ify8MudS60TrJSvIHOg5IajkCjStnNjESQhzib47V3C7y8OXuISEPbQxGbasjvGqLA9tyW203Q_ipzhwuyLvhSmbYHXhJ47PT53qJqkVGH1IR9A4F-mka-G37oidKvlwqagRadCv4xeDVERPl63S9hx6fKg1YhjBnmStPLeA5o23NSi6h5OKeme4OjqWhy7We0D8UOwx2ZrEINmGI1s3n1_QVHpDxcMapkAR_OpjU2vGY_LMDAANb3_WTBq-6BXjQy9Jxi9Qz5EY8Sp7H1sRdWfJPa0EiyeteiLwZZZQRnAe2RQC-7S4wjmiqSzLa4zx4M2r5mQZMcrah7PioFsc2DvJ10wq9mp05cOjwkWC8jDHZjkdFKWr37yNToizcNAQkN1aXX3p-I79xCTv5Bguo_0XFsjVVvHqYi978DXxPwTf0ocMLkxfaUjuqlWrtfVpLuXKRN0Ad9xrwuaiORebVfA0cDiPA8VM7NbYzkO39c45diembr7rndhS4rxhlzVt4MVcQc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
کویتی‌پور، معروف‌ترین مداح دوران جنگ ایران و عراق، دیگه حتی مداحی گوش نمیده
@News_Hut</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/news_hut/69273" target="_blank">📅 22:33 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69272">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KRQvqjRSf-9FGDP5wnU5auljWfdQmPk4kxoxWKAcQORGnO433x2LlnaNgXVCMB4P7ZPTHK07QweW_Qk8eHfjCXHS-V9cOMaZkyCYOO0nnXwD7c6wzCcf7TVEWzbV8Gnwrw2J_yR8-2v__O8Ieyd3Zq4m90QBUiFc3IIhc2YP_st8sJ9V2eaQWkXUA9JQ_CFJ3uDAyGBcKW7oYbaATPqN4q-qoSku3Xdd3xkeJs_3wFjbqLYXcsdjWf3idpUBK3hF7NuVng9x9z3sEFyySU-3oox1sGKGsLGJM5h58nQHdyRoMhY1mG1evsXLLZDeyJLGTvT4EgUSolb7En_gnNiJyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😄
مالک تلگرام ، پاول دورف :  روسیه به‌دلیل اینکه حاضر نشدم خواسته‌هایش برای نظارت گسترده و سانسور در تلگرام را بپذیرم، مرا در فهرست «تروریست‌ها» قرار داده است. طبق قوانین روسیه، من از «انتشار هرگونه اطلاعات در اینترنت» منع شده‌ام.  ظاهراً مقام‌های روسیه هنوز…</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/news_hut/69272" target="_blank">📅 21:58 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69271">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/OWe-OaS7hFB-EeDVocOfvfswH1zkhWKdnTRr3pIqUincKfmju6UW3-sJKyLVWYpTVAjkaLNJJn6VqAAcsVLBjJA1CzLFCqE7x9NV2YAce43hhEdifhNM9rBAgciC94RFEeOKv39LWDEfDKkBfintCY-dtQY9xbJxGtnfTyczi7FkWWf13NgOvQYwfgh7cH3d0F_zLgyee0eiWdUNNb5Q3l39NjEufTOPf9t5JjB04BtzdV0h2hCKYVUDu6xUe5E7QpZ4K8LIMXOvlNeiyA4Agl889m5hNVdR1bUn-EhIZvGeSB8YcjvGtqMf1uleOXZhZlPBxN-BBc_lrBR_uKG-DA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😄
مالک تلگرام ، پاول دورف :
روسیه به‌دلیل اینکه حاضر نشدم خواسته‌هایش برای نظارت گسترده و سانسور در تلگرام را بپذیرم، مرا در فهرست «تروریست‌ها» قرار داده است.
طبق قوانین روسیه، من از «انتشار هرگونه اطلاعات در اینترنت» منع شده‌ام.
ظاهراً مقام‌های روسیه هنوز نمی‌دانند که چه کسی می‌تواند چه کسی را از اینترنت محروم کند.
@News_Hut</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/news_hut/69271" target="_blank">📅 21:39 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69270">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b7ad22e432.mp4?token=G-Q9acf0XDsyuR2Mz5yhagssa-n-JKG29MYFQPB6rnGSvT75_n5qimz6_b-yGwv5YOfmnP8WQRpp-pBKSMQcjJbMU7w1ONa-oxjnPTePWyUOC2crgBkccDtC9EUzqZt-GP8_ZWIgOOKn6iKmJlTHftZj5I1mSm1WShuDzBKTr1FwmfLGBHKpFAWiwYJtkAdWX9_xPhZioU_ywv8pjx4-Tn6cIoCHv5Ie--Fbmavqcuv9HA4KrzEhguMtKAhd3B0mMhMNYESL648oE-pAKihCp_A8MHlrcMXCylM1rfsH0LVLWgPB_ZJ1BxHjwkvB8iHFX_88T21OnIzjSwpUk1YPiA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b7ad22e432.mp4?token=G-Q9acf0XDsyuR2Mz5yhagssa-n-JKG29MYFQPB6rnGSvT75_n5qimz6_b-yGwv5YOfmnP8WQRpp-pBKSMQcjJbMU7w1ONa-oxjnPTePWyUOC2crgBkccDtC9EUzqZt-GP8_ZWIgOOKn6iKmJlTHftZj5I1mSm1WShuDzBKTr1FwmfLGBHKpFAWiwYJtkAdWX9_xPhZioU_ywv8pjx4-Tn6cIoCHv5Ie--Fbmavqcuv9HA4KrzEhguMtKAhd3B0mMhMNYESL648oE-pAKihCp_A8MHlrcMXCylM1rfsH0LVLWgPB_ZJ1BxHjwkvB8iHFX_88T21OnIzjSwpUk1YPiA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🔝
سنای آمریکا به طرح قطعنامه‌ای برای توقف عملیات نظامی علیه ایران، مگر با کسب مجوز از کنگره، رأی منفی داد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/news_hut/69270" target="_blank">📅 21:12 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69269">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/64cd6ef9d4.mp4?token=GCyAFbeKA3Xt8VQNGR-L4KQh_biRxUrjd_ZYh8PEKcmsdTv_YnUVdKfNqKY3kTGL8E7iv0IRgoRcY9pW0wXeUf6ApsF3ozCxY9V8kJTFC4aWYHnIAK78Oir5ek3ddg8nCp5vA2BIf7D9lPtycdwJ8CJoU5nuIL0dbATv-xmQFf-uO_wx0CXhgoUQZS45wNJLlnHX_WHGXY-Od_WOtVE4tPsnlZZb2ZifSF2zcZGPrzlYBt49vIZ4i3sMSemS2B8GppHe8uEvlUIdMOT2gUJt62nHDjegY7JElt4u-MzDghpSJ7LXcWPF9KVDYSgonuCJnQceX3TJ0nZHVoXGKuqOQQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/64cd6ef9d4.mp4?token=GCyAFbeKA3Xt8VQNGR-L4KQh_biRxUrjd_ZYh8PEKcmsdTv_YnUVdKfNqKY3kTGL8E7iv0IRgoRcY9pW0wXeUf6ApsF3ozCxY9V8kJTFC4aWYHnIAK78Oir5ek3ddg8nCp5vA2BIf7D9lPtycdwJ8CJoU5nuIL0dbATv-xmQFf-uO_wx0CXhgoUQZS45wNJLlnHX_WHGXY-Od_WOtVE4tPsnlZZb2ZifSF2zcZGPrzlYBt49vIZ4i3sMSemS2B8GppHe8uEvlUIdMOT2gUJt62nHDjegY7JElt4u-MzDghpSJ7LXcWPF9KVDYSgonuCJnQceX3TJ0nZHVoXGKuqOQQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
📚
عمران عباسی، عضو کمیسیون آموزش مجلس
:
قطعا تو مهرماه باز شدن مدارس رو نخواهیم داشت.
چون برگزاری آزمون‌ها تقریبا یک ماه تاخیر داشته.
حالا همه تلاش‌مون رو می‌کنیم که اول آبان یا تو خودِ آبان ماه مدارس رو باز کنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/news_hut/69269" target="_blank">📅 20:55 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69268">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1dca29ad7e.mp4?token=aR5AQi1uAIVr4kG__NaC01bhh9LofNv-J3D6c1GlOs0M0kHo7QSHExNWkKTYKF5nURFjFI-pQ2lzHSiiMdTAdQooNmc6R5Bsl_qgKrroSFu9ksmMcBLfwCSXnJLsuKADnJIS3xkPyRl9UvSY9RCCv20HR5fKBnq0v8sPz0FRnsCW5d2-oBQRxe_7nbIkbi8_uDr4eKvUbrQkIRiW1fLXVOPrPY8dQOyTvSl0Mqh_Xq13a9sKeWrEtzGc1hO4f-2upccU2g7ZqhGx7yIs6NePuxf390gcfI_efz0hAW7SLXXOIIlLHRu8fEuyPUHBpF37sHyCSEPtTOrcSTImyLXMhQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1dca29ad7e.mp4?token=aR5AQi1uAIVr4kG__NaC01bhh9LofNv-J3D6c1GlOs0M0kHo7QSHExNWkKTYKF5nURFjFI-pQ2lzHSiiMdTAdQooNmc6R5Bsl_qgKrroSFu9ksmMcBLfwCSXnJLsuKADnJIS3xkPyRl9UvSY9RCCv20HR5fKBnq0v8sPz0FRnsCW5d2-oBQRxe_7nbIkbi8_uDr4eKvUbrQkIRiW1fLXVOPrPY8dQOyTvSl0Mqh_Xq13a9sKeWrEtzGc1hO4f-2upccU2g7ZqhGx7yIs6NePuxf390gcfI_efz0hAW7SLXXOIIlLHRu8fEuyPUHBpF37sHyCSEPtTOrcSTImyLXMhQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⁉️
حکومت از امروز یه طرحی رو شروع کرده که بتونه فضای مجازی رو به صورت کامل به دست بگیره؛
طبق این طرح؛ قراره بلاگرها، اینفلوئنسرها و بقیه فعالای فضای مجازی ثبت و ساماندهی بشن.
در عوض می‌تونن از مزایایی مثل بیمه استفاده کنن، اما از اون طرف هم قراره نظارت روی محتوایی که منتشر می‌کنن بیشتر بشه و هر کسی خارج از چارچوب قوانین جمهوری اسلامی فعالیت کنه، صفحش بسته و با برخورد قانونی روبه‌رو میشه.
@News_Hut</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/news_hut/69268" target="_blank">📅 20:50 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69267">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/46911d7dc4.mp4?token=naPkooNxkiXC2lIm9SgfMwiQ-9GTReJtCtgXJoN563pQ1kDjrWJ6g3S5ec_6AZy2_ssA1EK3xoCb_mSXJHq932Uz2ffGH-x-DR4h6wM2hehLDHQ7PGgv9b36KY_Ua5icki1IyW6EKv2ll0UuhJA2xCc0muEiLtD8ir4Ak8eBbBjOlOqxkhrNOgxXqDivIIS2aCr0mxERA998lHssrWlZ1LKL2KxQeD4uP838ljLQHmYiaq2OOw5g4jSPp8AZKXtYGpFATB1D0UucDXGOGxDJI5PfkppbffHyarEiFCgotvchhPSF36iM3HFanzvf_4leKwY1iZYG-xemz1B_O0j1dw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/46911d7dc4.mp4?token=naPkooNxkiXC2lIm9SgfMwiQ-9GTReJtCtgXJoN563pQ1kDjrWJ6g3S5ec_6AZy2_ssA1EK3xoCb_mSXJHq932Uz2ffGH-x-DR4h6wM2hehLDHQ7PGgv9b36KY_Ua5icki1IyW6EKv2ll0UuhJA2xCc0muEiLtD8ir4Ak8eBbBjOlOqxkhrNOgxXqDivIIS2aCr0mxERA998lHssrWlZ1LKL2KxQeD4uP838ljLQHmYiaq2OOw5g4jSPp8AZKXtYGpFATB1D0UucDXGOGxDJI5PfkppbffHyarEiFCgotvchhPSF36iM3HFanzvf_4leKwY1iZYG-xemz1B_O0j1dw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
آفرود سواری هم تو ایران ممنوع شد؛سازمان منابع طبیعی:
از این به بعد هر کسی بدون مجوز یا خارج از مسیرهای مشخص وارد مناطق طبیعی بشه، باهاش برخورد می‌کنیم. اگه هم آفرود به‌عنوان یه ورزش به رسمیت شناخته بشه، براش دستورالعمل و چارچوب مشخص تعیین می‌کنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/69267" target="_blank">📅 20:14 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69266">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/acbbb58fbc.mp4?token=asUybxu1EgJrfN25tDdO_JMxCe7_TSsBpMGtHw8GsOmoeTcUmJx7L0P2VkWbOR0R-6NRdMvaie-Id8Aw4r2CRp4Ty7ImVL5F0kYb-oaeOTvAs5oaAkxycZYCApCZByT2BaUvapiVyCoKlWGSQ5ZTbc3GHdmOYyrD9smW7WT87JmWfbRYh-8Dq74RNnBfbNj8CH80T1uWgeNRuCpXkIfy89nUM97_Cc5LBMUtEQfSaTcM_wYi5WVGlWYjO45JBF6ZmXzlDWyKcbk1_hiP5DaGVFXG7iPMzCg-g-_xFgx94KFPgmuuPs6CaNcjgdm-HKAjLpzWDcabIddkDZ7nVpl_8FH_s83IJ-ntIvXkQ4ODOPMDOrhgbgbK_d2Jr1VbjXMFK3GCRYkbtn8F8P9fWZIvivA99NUp_-8sE2eiUm6FktHW7nBCeJm99HQvSHiQVle5PLTcnWJ17H1f5KTjtNPxZUrsAXQggcKSdmaaxiQovZyfaD1EGHQfoHyAByZ40TsB94kDQQb1-zApR_qsvEJESJUme4ZsMv-DYxk6l1oVEMoL1iQWrY8P4C6DO8Vs0o37sovW94IJdSSywC5aZ6ofV2vWXA4etb2e4lhk_FotB6warb-GFYwqjG9fFnsKCtYqc-5Qp-9ROSI0tNJG8SwDvhr7MZAGLDS0rzdeCsuBWws" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/acbbb58fbc.mp4?token=asUybxu1EgJrfN25tDdO_JMxCe7_TSsBpMGtHw8GsOmoeTcUmJx7L0P2VkWbOR0R-6NRdMvaie-Id8Aw4r2CRp4Ty7ImVL5F0kYb-oaeOTvAs5oaAkxycZYCApCZByT2BaUvapiVyCoKlWGSQ5ZTbc3GHdmOYyrD9smW7WT87JmWfbRYh-8Dq74RNnBfbNj8CH80T1uWgeNRuCpXkIfy89nUM97_Cc5LBMUtEQfSaTcM_wYi5WVGlWYjO45JBF6ZmXzlDWyKcbk1_hiP5DaGVFXG7iPMzCg-g-_xFgx94KFPgmuuPs6CaNcjgdm-HKAjLpzWDcabIddkDZ7nVpl_8FH_s83IJ-ntIvXkQ4ODOPMDOrhgbgbK_d2Jr1VbjXMFK3GCRYkbtn8F8P9fWZIvivA99NUp_-8sE2eiUm6FktHW7nBCeJm99HQvSHiQVle5PLTcnWJ17H1f5KTjtNPxZUrsAXQggcKSdmaaxiQovZyfaD1EGHQfoHyAByZ40TsB94kDQQb1-zApR_qsvEJESJUme4ZsMv-DYxk6l1oVEMoL1iQWrY8P4C6DO8Vs0o37sovW94IJdSSywC5aZ6ofV2vWXA4etb2e4lhk_FotB6warb-GFYwqjG9fFnsKCtYqc-5Qp-9ROSI0tNJG8SwDvhr7MZAGLDS0rzdeCsuBWws" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
زنده‌یاد مانوک خدابخشیان:
"اگر رژیم مذاکره کنه باخته و اگر مذاکره نکنه هم باخته"
@News_Hut</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/news_hut/69266" target="_blank">📅 19:36 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69265">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cce71ed1d1.mp4?token=L1faaUbqZ3WW7o0tYzkh7fkSErqh9SG_1B2HRoYSy9m19Om4cyfd34WwRqYJOhsOXfzmiOpo4fDLdvdYsAYpdvFmjdjrwHWNt2yFSknEoY-CKdbZiFVA8MrsrUvNhNKmsmkPNKXgwd59y1rrgGZCAsRCMt8KljOf-xd5FRYCVtq_G3P2kOw1AYPUJnTWl-3afOWiheNVROTuLPDNkrVRZKgQxVlkpimgvNYg5vdoWlVxzszlH8ru4-bRQ4obGKWzYBfpPcSj3yv68mzw2EOVnH2jLYjy5YRdFndBicRevBydDPsjtZCsSsuI0ALL0Y6Q4tULOpEiTXLts7f99JDiMg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cce71ed1d1.mp4?token=L1faaUbqZ3WW7o0tYzkh7fkSErqh9SG_1B2HRoYSy9m19Om4cyfd34WwRqYJOhsOXfzmiOpo4fDLdvdYsAYpdvFmjdjrwHWNt2yFSknEoY-CKdbZiFVA8MrsrUvNhNKmsmkPNKXgwd59y1rrgGZCAsRCMt8KljOf-xd5FRYCVtq_G3P2kOw1AYPUJnTWl-3afOWiheNVROTuLPDNkrVRZKgQxVlkpimgvNYg5vdoWlVxzszlH8ru4-bRQ4obGKWzYBfpPcSj3yv68mzw2EOVnH2jLYjy5YRdFndBicRevBydDPsjtZCsSsuI0ALL0Y6Q4tULOpEiTXLts7f99JDiMg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
⁉️
سنتکام:در ساعات گذشته، رسانه‌های دولتی ایران به انتشار ادعاهای نادرست سپاه پاسداران انقلاب اسلامی (IRGC) ادامه داده‌اند؛به‌ویژه سه مورد زیر:
❌
ادعای اول: سپاه پاسداران (بار دیگر) مدعی است که مسیرهای آزاد و باز در تنگه هرمز برای کشتی‌های تجاری خطرناک هستند.
✔️
واقعیت: خطرات فوری که کشتی‌های تجاری و خدمه غیرنظامی آن‌ها را تهدید می‌کند، ناشی از تهدیدهای لفظی و تلاش‌های سپاه برای انجام حمله است.
❌
ادعای دوم: سپاه پاسداران مدعی است که سه جنگنده رادارگریز اف-۳۵ (F-35) و سه فروند هواپیمای دیگرِ ایالات متحده در جریان حمله اخیر ایران به یک پایگاه هوایی آمریکا منهدم شده‌اند.
✔️
واقعیت: هیچ‌یک از هواپیماهای ایالات متحده در تلاش‌های اخیر ایران برای حمله، منهدم یا دچار آسیب نشده‌اند. تمامی موشک‌ها و پهپادها رهگیری شدند یا به مناطق هدف‌گذاری‌شده نرسیدند.
❌
ادعای سوم: رسانه‌های دولتی ایران گزارش می‌دهند که یک نفتکش تجاری به نام «ام‌تی نورا» (M/T Nora) موفق شده است محاصره ایالات متحده را بشکند.
✔️
واقعیت: این کشتی تجاری موفق به شکستن محاصره مستحکم (دیوار فولادی) ایالات متحده نشده است. بیش از ۲۰ ناو جنگی، صدها هواپیما و هزاران نیروی نظامی آمریکا همچنان هوشیارانه به اجرای کامل این محاصره ادامه می‌دهند.
@News_Hut</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/news_hut/69265" target="_blank">📅 19:04 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69264">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/906e47e12d.mp4?token=M2TsBo8ndHabLcMzw3IgYBvJoieir9LO2pZp_TKRPgFErZ5Jjt4FTOjahrpsf-llwMGXYa5oE4AEhLsFkGxcsKajdmEMO5GUvlhs0dEUsms1qFVdKqSQ5Ul-zqS-Biyp9a8jVI7gOkqi4Z1fQk5hZA6R0DzPtuyLH1-yxvhasvNau10q-vD_GwdSaaMEWX6NKr6rcvT_2uYDQ_lnsfdWUg-8v8sJBH7NIbtfdeOXvcPDsBu00vm2z3D0lIwYQvaN0HEjt0cUYriFpmQOkuErN3HEtvsrCa4e2bYqGa0H_nTQa8ceVA2yyicUND6TjyWjGmRwYKCHr7ei8Bqj9XRXfA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/906e47e12d.mp4?token=M2TsBo8ndHabLcMzw3IgYBvJoieir9LO2pZp_TKRPgFErZ5Jjt4FTOjahrpsf-llwMGXYa5oE4AEhLsFkGxcsKajdmEMO5GUvlhs0dEUsms1qFVdKqSQ5Ul-zqS-Biyp9a8jVI7gOkqi4Z1fQk5hZA6R0DzPtuyLH1-yxvhasvNau10q-vD_GwdSaaMEWX6NKr6rcvT_2uYDQ_lnsfdWUg-8v8sJBH7NIbtfdeOXvcPDsBu00vm2z3D0lIwYQvaN0HEjt0cUYriFpmQOkuErN3HEtvsrCa4e2bYqGa0H_nTQa8ceVA2yyicUND6TjyWjGmRwYKCHr7ei8Bqj9XRXfA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یه پسر جوون ایرانی رفت پشت فرمون ماشینش ی خر گذاشته رانندگی کنه خودشم داره از رانندگی خره فیلم‌ میگیره
😳
@News_Hut</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/69264" target="_blank">📅 18:33 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69263">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🚨
انفجارهایی در صنعا، پایتخت یمن رخ داد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/69263" target="_blank">📅 18:30 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69262">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OpRAMhHQpDrVCkAY5XG_PMOfPNdYDETZ9ZS5S90DEcJWVYhSNv6Fp3OmBD4SF8t2G9L3WLx0rZy-dD5nqgkHFrWqiAl_vGs6Nn2HbV9LTygRd04z_ZEvmH_7Liur6plt2KNXc9hhMsqSSuxaB16C92xuNwnGoOqhZ4-FcbEcZipZ4GI5r5VWfTHtfsvhHG8JOfd6K2vMWBt78kow8z7ncMdTg8PMMjWlx449G68BUaZVp1hpHdZZiqSr4Y3fL4_t9X_SAQ6MDe0cuzct14jBsSqCEi5n8xasgOskpsiHYYy0g3z3_daSf1ULBZjK8TUnY-FZX_eknK1mqq3EJcuCCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
سه تا از تروریستای مفعول حشد‌الشعبی که در حمله مشترک آمریکا و عربستان به عراق کشته شدن!
@News_Hut</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/news_hut/69262" target="_blank">📅 17:56 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69261">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M_GCc9_PqKCcKiIvSgqBZi17-hD8pekLzvNGMgJCGuh94tosXQyB4RtcR9EaXmTAnDjdE8_AP9VNFsDokBf0R-TGLJI_uLjuqEZh0rx2FEuOVNPGcyyUwfLAnz_ksnsllAgjMoaOzn7aNFOnvPJ3vwc2ZLsIrJBqLfVoMk6uHlY58S9IN-F-uPAN57xH5KrdVDQXuhxRWo3LOcUjN7n9YC_beRlSOwN_kXS0SSoDtQah3tm4NqxMB9IhNhbIMYRYTeBjNQdfoHo1GwSsMGC6G-trEeAa-a1wGBELvpf2lh67MqWDng-AKTw-2BJNCX9XjxI0xWCt2dDTJaaITMIGAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
روابط عمومی سپاه پاسداران؛اطلاعیه شماره ۵۶:
دو آشیانه پهپادی و یک مخزن سوخت هواپیما و بالگردهای نظامی در پایگاه علی السالم به آتش کشیده و منهدم شدند.
@News_Hut</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/69261" target="_blank">📅 17:44 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69260">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/262bb95a39.mp4?token=rFZOLJwDXcDI9kuJ6U1QBCSytRDHKXMybhh7o7lU8ZD35HS6Lii4-YbQfD0SR7anru02ChEk2e2kRftGfu1KTPq_Gs6qQwtB7Qsjwpz7an_nFAx_VBMKF-VZJGWwQH4yaLCy9u91iaNDCDazMhwaZfmDdhdl_vzpMoy4KtytoVnnTJvJIhFepPXd2Np4XTObzCmTM2qDpnWf9y3LqBdGvhqIa21A6mrm9Ai6LFoBt_I8Y9mHmVqUa1FOxIW7k2GCZN56zfkGunuI5aVRRuNuLPcfULIrLKKG0sSWTvyYlCbIhzYSj4QEFd3ZRmVOIZy2mnbJZNTB8zkP9NieuPTAvQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/262bb95a39.mp4?token=rFZOLJwDXcDI9kuJ6U1QBCSytRDHKXMybhh7o7lU8ZD35HS6Lii4-YbQfD0SR7anru02ChEk2e2kRftGfu1KTPq_Gs6qQwtB7Qsjwpz7an_nFAx_VBMKF-VZJGWwQH4yaLCy9u91iaNDCDazMhwaZfmDdhdl_vzpMoy4KtytoVnnTJvJIhFepPXd2Np4XTObzCmTM2qDpnWf9y3LqBdGvhqIa21A6mrm9Ai6LFoBt_I8Y9mHmVqUa1FOxIW7k2GCZN56zfkGunuI5aVRRuNuLPcfULIrLKKG0sSWTvyYlCbIhzYSj4QEFd3ZRmVOIZy2mnbJZNTB8zkP9NieuPTAvQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
ویدویی از لحظه دستگیریِ نوید زیادخان قره‌داغی وسط خیابون بعد از شلیک دو گلوله به پا؛ این همون شخصیه که تو لایو دخترارو کتک می‌زد و...
⚠️
‌ ‌ ‌
حاوی خون و خون‌ریزی
🔗
‌
مشاهده ویدیوی کامل بازداشت
@News_Hut</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/news_hut/69260" target="_blank">📅 17:24 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69257">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cea20ae2a1.mp4?token=nRBL-L2LPTrvrnjINXet8ekt-_Dz0Hcd4HUY-fgXSnvol1Q3GjHso9IoA7u-i23I0dl-lHAlftJAxVgk-jWdCZUyBLQqVNbGd9Ky_mqmw1q1T5DNhjnAWfOQegTCaBrdAzcUfDkZ68VGpH2b5ZT0K8DRk36KsUwXvZJOUF_1VL9RjYad-sXTJha1ilIw4ZfyRzx4IgdHlOcZItkL_unv5bhQTgb91cdzfFK_mRxeDspJVDB0jlOyw9yNJX_TUEQJQlSnTmyvSUY1f5dtI45zTj-ZscuzLTQsiKqe9L6HqWu6YovgwYme328N4RJJTqpghhLwH1a7cpRmx_Ban-90jQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cea20ae2a1.mp4?token=nRBL-L2LPTrvrnjINXet8ekt-_Dz0Hcd4HUY-fgXSnvol1Q3GjHso9IoA7u-i23I0dl-lHAlftJAxVgk-jWdCZUyBLQqVNbGd9Ky_mqmw1q1T5DNhjnAWfOQegTCaBrdAzcUfDkZ68VGpH2b5ZT0K8DRk36KsUwXvZJOUF_1VL9RjYad-sXTJha1ilIw4ZfyRzx4IgdHlOcZItkL_unv5bhQTgb91cdzfFK_mRxeDspJVDB0jlOyw9yNJX_TUEQJQlSnTmyvSUY1f5dtI45zTj-ZscuzLTQsiKqe9L6HqWu6YovgwYme328N4RJJTqpghhLwH1a7cpRmx_Ban-90jQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇷🇺
❌
🇺🇦
حملات شبانه سنگین روسیه به کی‌یف، پایتخت اوکراین
@News_Hut</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/news_hut/69257" target="_blank">📅 17:14 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69256">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d31a669dbb.mp4?token=ljmz4zW42PtGEfo_4-aZeBbvtKjv-f-27zirgZbErWTtGHSrx4eJWymCgeHojokBaGyFxTfkb4-UhtOGBALKaJ7g_R3zJLAkyXlrvZV5OcJz0Y1w4UdRf5gCQOqh4YhQ3ig0DYBD7zzXslz2IT2N5m3VtUIKIkawiCZqgggO4qjQfEDJFZnP9aBGWXfbmDqNtpWBGmvwQktrl-X-FIQlDfFTMy1uve8QoreRU-UrPSG_Le1-6Uheax0B9f_nPKEU_DLWFW0WNZFtw2g4ckAhdrPt3Mjp8GaTw9n_YL0zR0iwE5aHh4x6OHEADcQOLMIAho8kiUIMYc39BipxwsHWnw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d31a669dbb.mp4?token=ljmz4zW42PtGEfo_4-aZeBbvtKjv-f-27zirgZbErWTtGHSrx4eJWymCgeHojokBaGyFxTfkb4-UhtOGBALKaJ7g_R3zJLAkyXlrvZV5OcJz0Y1w4UdRf5gCQOqh4YhQ3ig0DYBD7zzXslz2IT2N5m3VtUIKIkawiCZqgggO4qjQfEDJFZnP9aBGWXfbmDqNtpWBGmvwQktrl-X-FIQlDfFTMy1uve8QoreRU-UrPSG_Le1-6Uheax0B9f_nPKEU_DLWFW0WNZFtw2g4ckAhdrPt3Mjp8GaTw9n_YL0zR0iwE5aHh4x6OHEADcQOLMIAho8kiUIMYc39BipxwsHWnw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
صبح امروز ارتش آمریکا به یک پایگاه پدافند هوایی سپاه‌پاسداران در اهواز حمله کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/news_hut/69256" target="_blank">📅 16:33 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69255">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/21d6f2f438.mp4?token=jD7pw5E8dqnCjwTq762OEYJbKfzLGCC0bsukhTGP-_ibfRxM5mUcML2H7XoS7PstORamwiTW0SCjRIfxX2bbVbcJurJ9Ew8lBfRu7OEI6__ANHPlLDhNh_gdM6ydDK-XDQzneBfN5VfVq2GjRhbTgcE2ZROnfHdRStSSBCDXOIHYXta9cR62i5mN3oRf_mbDmFj5rd9uJnzcNeOOdOPXiK2KvSHR5LgIaDnYfv7QJlvDiqta6ywAnk6AlIrXDbOIZmnSEfUfN2O7mbk2I-fCupZhB89VxFbqWiq8T1T3NBlKoRTb2LaefJkuF8Pd0DmsCAyrKqqGZehDVf7nYgXTng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/21d6f2f438.mp4?token=jD7pw5E8dqnCjwTq762OEYJbKfzLGCC0bsukhTGP-_ibfRxM5mUcML2H7XoS7PstORamwiTW0SCjRIfxX2bbVbcJurJ9Ew8lBfRu7OEI6__ANHPlLDhNh_gdM6ydDK-XDQzneBfN5VfVq2GjRhbTgcE2ZROnfHdRStSSBCDXOIHYXta9cR62i5mN3oRf_mbDmFj5rd9uJnzcNeOOdOPXiK2KvSHR5LgIaDnYfv7QJlvDiqta6ywAnk6AlIrXDbOIZmnSEfUfN2O7mbk2I-fCupZhB89VxFbqWiq8T1T3NBlKoRTb2LaefJkuF8Pd0DmsCAyrKqqGZehDVf7nYgXTng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
ویدویی از لحظه دستگیریِ نوید زیادخان قره‌داغی حرومزاده چهل پدر وسط خیابون:
@News_Hut</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/news_hut/69255" target="_blank">📅 15:55 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69254">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f1666d9190.mp4?token=LRmNAbiQE2CI5LP5QnifaO4Mhp-f1GsPTSiFx7NSqqdEa4-hzqQVn0PeNE_ZpJmr8sDjejxQzQdfPtDMMVoCkZrpCl5MUlqN1e16rdkSNnCkf6zFkEc6HaMRdVsQnY_EqwMLdkMQ_ff2pYTFT56Cy_z2QonG4pvp1HYJfdu1e5u62aOSF1YP5AWRUSAbeqgHqoMPbGoWqR3qP1HNz6PU6QBvJhk3r9uCKJn_BOm7uUpN73TCyZaVxB-eFpYsWBzriiJcgu-TPYCgqNKTq6iJESUWZZRzWoU91X_TUPOG3KzfYEeucyLYdOOTNA9y59q7aIlTUQIlX8zNzsAf9NSIgg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f1666d9190.mp4?token=LRmNAbiQE2CI5LP5QnifaO4Mhp-f1GsPTSiFx7NSqqdEa4-hzqQVn0PeNE_ZpJmr8sDjejxQzQdfPtDMMVoCkZrpCl5MUlqN1e16rdkSNnCkf6zFkEc6HaMRdVsQnY_EqwMLdkMQ_ff2pYTFT56Cy_z2QonG4pvp1HYJfdu1e5u62aOSF1YP5AWRUSAbeqgHqoMPbGoWqR3qP1HNz6PU6QBvJhk3r9uCKJn_BOm7uUpN73TCyZaVxB-eFpYsWBzriiJcgu-TPYCgqNKTq6iJESUWZZRzWoU91X_TUPOG3KzfYEeucyLYdOOTNA9y59q7aIlTUQIlX8zNzsAf9NSIgg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت صداوسیما بعد از هر حمله آمریکا
🤣
🤣
@News_Hut</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/news_hut/69254" target="_blank">📅 15:20 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69253">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">‼️
🇨🇳
🇮🇷
رویترز:به گفته منابع، ایران ظرف چند هفته آینده سامانه‌های موشکی دوش‌پرتاب چینی دریافت خواهد کرد.  ۲۹ ژوئیه (رویترز) - سه منبع آگاه از این قرارداد به رویترز گفتند که انتظار می‌رود ایران ظرف چند هفته آینده، نخستین محموله از مجموع ۴۰۰ دستگاه پرتابگر موشک…</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/news_hut/69253" target="_blank">📅 15:06 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69251">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/XBBY3nbWOsCg1BiHqQBLDsSbnbTiuO050bEx1VJ89176GxpQfNl1zMG7Hyad6fQHIaH1VIeLYZgA075QoxcIwnjwInpgb7NYnkEnBcugyNAa0Cg1F8HU9LhiSzxRP8YFXdbvsIY8Agp-P05U6WDzFqYxKSaFF1OuadqXOHIUf76843gRLTLWhL5lJ83h7B0HyZBBAbtA8dtE6q1KvxPwdrHME2ThVANltNhsSkgNsyOeS1ub9DLJnlOXaUz0jpE2Ady2ql_9hNlF-7pLn0m0AuZ_Exu24-DUZa8iVU2E91OJf3NG7bqHxMOx4muiXmY47iCkigS7XwYwWVxX2F5-mA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/8b887c1d39.mp4?token=kwculbq5GHs14a9JHdjRBwK8_UNjYEEu3AePs5cUQc8JWmnshVlSf50STl7PvcVCNG060YAfcLijnkSpCO_4W0kEruvuiTiA3xGs00tobsDeI4V8eRXO40KvjmXBJez3fpHdmt9PzMfoWmfJxeHTDUCmxfpIRi4iWnS_eWxnYbZ5hzVooalSclkAlKWOuthybx2HD5qlV7D3-bSg1eidEhz60rvpGAtYvm7_nQ6-P0I7kjgbbsxMGzN-xhZmqObBcg1JWwxAcx05SG4PwxwiEeTqVz1TlHSkt6m4IOek-kJgmh3bZI3uKL2mbPS2kgyweUvXUWMj0nx7zeske_V3pg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/8b887c1d39.mp4?token=kwculbq5GHs14a9JHdjRBwK8_UNjYEEu3AePs5cUQc8JWmnshVlSf50STl7PvcVCNG060YAfcLijnkSpCO_4W0kEruvuiTiA3xGs00tobsDeI4V8eRXO40KvjmXBJez3fpHdmt9PzMfoWmfJxeHTDUCmxfpIRi4iWnS_eWxnYbZ5hzVooalSclkAlKWOuthybx2HD5qlV7D3-bSg1eidEhz60rvpGAtYvm7_nQ6-P0I7kjgbbsxMGzN-xhZmqObBcg1JWwxAcx05SG4PwxwiEeTqVz1TlHSkt6m4IOek-kJgmh3bZI3uKL2mbPS2kgyweUvXUWMj0nx7zeske_V3pg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
مادر جاوید‌نام ابوالفضل سپاهی، که توی میدان علیخانی اصفهان اعدام شد:
خطاب به یه نفر به اسم هادی: بگم برات که تیر زده بودن تو پای ابوالفضل؟ بگم برات که زیر چشماشو با فندک اتمی سوزونده بودن؟
بگم برات که ۲۰ روز بهش آب ندادن؟ بگم برات که فکشو شکسته بودن؟ بگم برات که دماغشو له کرده بودن و آویزون شده بود؟
هنوزم تحمل شنیدنشو داری که بگم برات...؟
@News_Hut</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/news_hut/69251" target="_blank">📅 14:50 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69250">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🚨
🇮🇷
سپاه‌پاسداران:
تخریب کامل سه فروند هواپیمای اف 35 و ورود خسارت سنگین به سه فروند دیگر در الازرق در پاسخ به جنایت دشمن آمریکایی در قشم.
همچنین چند افسر و کادر فنی و تعمیرات دشمن نیز در این حمله کشته شدند.
@News_Hut</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/news_hut/69250" target="_blank">📅 14:20 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69249">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/daa6076311.mp4?token=PCysgEy5_rd1IWt82b96LCPGbvBZCaQEbHjw3DxQOSPrAc0Uc7yX8md5ryvHzsTGM80daOwkdJOca7hj5jvJb-p0-R3TExN91NJtyRNK3-oO3PhcVgfrFKOj9SGKhPgKGBzr3T8PMMRCdCi5uG80MdemIy5BxSQRB3RjxDuTfNGJm9wvLTlj0r8wmy_GOXJPjDfudnw220RiANagwOjsl8ArjKC1LKhxFSeI4nfoZdT4d-pD4CxvQqp7MZ6O-edvmjMqyO35JGGQhVuDJwpSEhD6-yIypSPAA0XX9KNqcTC6Lyppcg__CRir4fvWwCj85tJiY-4VUy4DLpHIkvj-ng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/daa6076311.mp4?token=PCysgEy5_rd1IWt82b96LCPGbvBZCaQEbHjw3DxQOSPrAc0Uc7yX8md5ryvHzsTGM80daOwkdJOca7hj5jvJb-p0-R3TExN91NJtyRNK3-oO3PhcVgfrFKOj9SGKhPgKGBzr3T8PMMRCdCi5uG80MdemIy5BxSQRB3RjxDuTfNGJm9wvLTlj0r8wmy_GOXJPjDfudnw220RiANagwOjsl8ArjKC1LKhxFSeI4nfoZdT4d-pD4CxvQqp7MZ6O-edvmjMqyO35JGGQhVuDJwpSEhD6-yIypSPAA0XX9KNqcTC6Lyppcg__CRir4fvWwCj85tJiY-4VUy4DLpHIkvj-ng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
فرود دیدنی یک F/A-18 Hornet بر روی ناو هواپیمابر.
@News_Hut</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/news_hut/69249" target="_blank">📅 14:14 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69248">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tBjAHuZHesAcve6GNOL6hbcqTprzPKs6k-plQ2eSIZQ5Q4dtECOE5pmyX9x_hU7Dx7c9IItNE5Pd488x0bkEZA5KmfD7hG1kej6YOfWYNq2Vs2uz-i_FEooDAh-bImUpGM8E2Ew_aHoBgxe8G47O1hmD-wkyL4MUUJ4QlHUxFANhM_SvetX2ukZotSamKuqkQtXaUIQv4qm9KQoLXw6us90QbXRWCcxVUfXnZg6000L5ioXK7o86Gqm_CzeW3yvWJKXXjoP8olJhyHnEQr9dRR5eCe4jmio43oAvcz2ntVXEI6WK7kvPolWL733la0rE4SG0TxfUspXFcW0-tHWiWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⁉️
⏺
ان‌بی‌سی‌ نیوز:
به گفته منابع آگاه، ترامپ در قبال مسئله ایران «به‌شدت کلافه» شده است، چرا که مقامات ارشد بر سر راهبرد واحدی توافق ندارند.
@News_Hut</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/news_hut/69248" target="_blank">📅 13:29 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69247">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/a176457914.mp4?token=DfxeGsbI5tVbrisnT6yzuRKNUl6I6j0xVh8t_jKal98jxix719OGxJkmgTvvmxCQV4T6EbjQMKnhkuZ2FtA0D5RLZdimk9QIsRfK63aIeA-TBdNAgsOM7GDHhE35qG1KwrMwZ6DCFenCqguDBu21sTLQw4YKIYoCatA1TOY6pvkxvE82ROao94GFzsDQ6JfPmFMF9PYfKj60mcIN2i9z655v8nkQ6IXbmJ5rkExeJntCC-gfjElSoWDUdvQGx1odb_AwnM88iDqwhoc_XhsBM1BoocdOPxaDINvp39gCZO0Z_gZ65x2z1elAxVv11jRP4NGfMOONevPQN_2kTiI1d7mYzqvgXioXRTvl85yQuD981wa08Ct0v36POEAosKhoSDreQP8Iwd78N0Uv-HgRnQW5dNZRLfJSa96TXbva3lzLjLAtJvROA37J-ApU6h_-1YWCVtHHHlQYzV3tb--cOfgRv4x-4aMV-twRIZPxY41WbYfP2e2x_VBn5gGIlIe4SMDgX2aHPg0XCaDsegjif7ifSJ8_crAbyNVD2CsSHvGwIaboFjGoog4Wiq1E8qW5NwgE6xYy4cBQk9XSItVOZtqk71KiFMDU95Bd5mkBmPYTd6bMLm46qLFUKSjEMZ_zBg1EQ4a-XdEchPzeQ5TGb_ON-vBRAUvChidIb1MQwIo" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/a176457914.mp4?token=DfxeGsbI5tVbrisnT6yzuRKNUl6I6j0xVh8t_jKal98jxix719OGxJkmgTvvmxCQV4T6EbjQMKnhkuZ2FtA0D5RLZdimk9QIsRfK63aIeA-TBdNAgsOM7GDHhE35qG1KwrMwZ6DCFenCqguDBu21sTLQw4YKIYoCatA1TOY6pvkxvE82ROao94GFzsDQ6JfPmFMF9PYfKj60mcIN2i9z655v8nkQ6IXbmJ5rkExeJntCC-gfjElSoWDUdvQGx1odb_AwnM88iDqwhoc_XhsBM1BoocdOPxaDINvp39gCZO0Z_gZ65x2z1elAxVv11jRP4NGfMOONevPQN_2kTiI1d7mYzqvgXioXRTvl85yQuD981wa08Ct0v36POEAosKhoSDreQP8Iwd78N0Uv-HgRnQW5dNZRLfJSa96TXbva3lzLjLAtJvROA37J-ApU6h_-1YWCVtHHHlQYzV3tb--cOfgRv4x-4aMV-twRIZPxY41WbYfP2e2x_VBn5gGIlIe4SMDgX2aHPg0XCaDsegjif7ifSJ8_crAbyNVD2CsSHvGwIaboFjGoog4Wiq1E8qW5NwgE6xYy4cBQk9XSItVOZtqk71KiFMDU95Bd5mkBmPYTd6bMLm46qLFUKSjEMZ_zBg1EQ4a-XdEchPzeQ5TGb_ON-vBRAUvChidIb1MQwIo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
فیلم گوه خوردن نوید حرومزاده هزارپدر که دخترا رو کتک میزد اومد بیرو
ن؛
از همه عذرخواهی میکنم ، گوه خوردم غلط کردم!
بذارید برم توبه کنم ، درمان بشم و برگردم به زندگیم برسم.
اتفاقاتی که بین من و اون خانم‌ها میفتاد رو تو ذهنم الکی بزرگ می‌کردم و دیگه کنترلم رو از دست میدادم.
خانم‌هایی که کتک میزدم، من رو درک میکردن و هیچ شکایتی ازم نمی‌کردن.
اتفاقا مردم خوب کاری کردن که انقدر واکنش نشون دادن؛ باعث شد یک بار واسه همیشه به خودم بیام و خیلی مسائل رو کنار بذارم.
از تَه قلبم از همه مردم عذرخواهی میکنم.
@News_Hut</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/news_hut/69247" target="_blank">📅 12:46 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69246">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ba1958bb40.mp4?token=VozjD87MXVVDb4Jh9BCmkLOdqDcfy1_rsYGDxzpyuB0FEGONeDM8MjGRZCwKfGLAk9D7oRBxeqnzBQo5Za3B7CZPBiCKKUYjjnnqhT3y6PlZV5oE3Sil7TCTtx7swaW3cgH5xbeiDXerDOqhNvYA2PWlJiAVhVYRA164MHpBvx2t12WWi0qeYf75qCeX9tqZiGzu8YloYWqRkFun5r1asK2zjgtC4i0Q1jb7YJx8-kRbX36CkuKdSkviFniyujXiWDkm4sHN8lRSy1k7W36R89OR4z5vDyzCpMpgYeoS-hawMi7tzX1D0BGMKAYVhUKI7PfqRSDB6p7VBWZnkp4aXw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ba1958bb40.mp4?token=VozjD87MXVVDb4Jh9BCmkLOdqDcfy1_rsYGDxzpyuB0FEGONeDM8MjGRZCwKfGLAk9D7oRBxeqnzBQo5Za3B7CZPBiCKKUYjjnnqhT3y6PlZV5oE3Sil7TCTtx7swaW3cgH5xbeiDXerDOqhNvYA2PWlJiAVhVYRA164MHpBvx2t12WWi0qeYf75qCeX9tqZiGzu8YloYWqRkFun5r1asK2zjgtC4i0Q1jb7YJx8-kRbX36CkuKdSkviFniyujXiWDkm4sHN8lRSy1k7W36R89OR4z5vDyzCpMpgYeoS-hawMi7tzX1D0BGMKAYVhUKI7PfqRSDB6p7VBWZnkp4aXw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
خبرنگار صداوسیما حین گزارش پرید توی آب و فاز کوسه گرفت.
@News_Hut</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/news_hut/69246" target="_blank">📅 12:13 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69245">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XrBdIDjexsDYgn7Rvs24e3HL_3GF6gufzQQy4kSQB7GnjA1Wswdn_goQXv60kigol2uVucRDix2RQ24wV5goCfkWt_DpMuiwSxFww5hlOE35MUb9P12o-7iWV0yguVDAvYbSRLhH4Yz3lNtnIKLyBrWpNYJXqbgkWaEmrBoxUt0oJnFcroaQJKpt2ewOMzj3t40wxx7DYNPCquG6bk7e0l9v1IqvMYNUol_1KJzsR5fokFxx3MHUaVQAkN_wGdZylGMWkNWcG-dqe1kyDsxt6gCHSlYYM3gSnXTVwDwlZ4hg2QcR-9c4dqAmMMAPhd2S1AYZnvxLJiGTxnt19EIpNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
سپاه پاسداران:
متجاوز رو همین امروز تنبیه میکنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/news_hut/69245" target="_blank">📅 11:36 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69243">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/POr-3_TBESUjEeGXGjFV_gc66a79uVaBRH_pyT4IWDUjCIxWSp0Ks0Ekx1bfvvEbHn3tzLhdsfgWiAh2JzeqE9XLv4LkxYB1XU94GG2yX-9McP1aJV19E-mZmTQiuW4wHPl2LIWGZNVcU0Tb1Qwbnq1MbXgXgs38QAI81Chsuv6eg814k1f49MtBdDb94ZLGkzUk5SI9ODNqxVDSm8DmkEZtcWIpreVg6ic7d59OTQkPZb4YZA5h-xO6ABuu8wUE9NZjqDUQIzQhh8cz3toXqqEv2_wYWceA7r_zbcwmfVLxvpnYCCsY7HGzjnHSW_xRANK5KA1opj9epXxMAUxkpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/854dca423a.mp4?token=shXGn4Xb7xWFCGPZi5Wr7Atk65OoN9XVy62I-VRQolvmYe_RRs19Y_xr4lBeG30xwmdVtFEqPVG-68TJ-z72CL0XzgkFnPaM8_eAeJUCC43jOBQkVpd_NnSPX464-YHzdimzjvJBFdliEd0AJGRndUh3GYqNH0twMtOBZ4xeVnICdeaJC5MlQsJvGmx8nzJR2ga7AjHEF5dK1GbrBsLTaOof5lupgHEfTbqk7WseoDSy783QLCUSe9XBKjdA9avZWrI2_a19s0vGXtZ9Yb2TpTQ-zn6SnE2j2xvUikR0J7nxdBouJHbQOPOloCVzPbYj_ERh-QR2phgBtP7jZzvHBA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/854dca423a.mp4?token=shXGn4Xb7xWFCGPZi5Wr7Atk65OoN9XVy62I-VRQolvmYe_RRs19Y_xr4lBeG30xwmdVtFEqPVG-68TJ-z72CL0XzgkFnPaM8_eAeJUCC43jOBQkVpd_NnSPX464-YHzdimzjvJBFdliEd0AJGRndUh3GYqNH0twMtOBZ4xeVnICdeaJC5MlQsJvGmx8nzJR2ga7AjHEF5dK1GbrBsLTaOof5lupgHEfTbqk7WseoDSy783QLCUSe9XBKjdA9avZWrI2_a19s0vGXtZ9Yb2TpTQ-zn6SnE2j2xvUikR0J7nxdBouJHbQOPOloCVzPbYj_ERh-QR2phgBtP7jZzvHBA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🔞
ویدیوی وحشتناک از یه حرومزاده به اسم «نوید زیادخان قره‌داغی» داره همه‌جا پخش می‌شه، تو لایو اینستاگرامش چند تا خانم رو خیلی بد کتک می‌زنه و کلی بهشون فحش می‌ده.  هنوز دقیقاً مشخص نیست چرا این کار رو کرده و اطلاعات موثقی بیرون نیومده، بعضی‌ها می‌گن دخترا…</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/news_hut/69243" target="_blank">📅 11:28 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69242">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/15118cd8c7.mp4?token=J0gMm3_xIwL7AiXnZsSkEhjm1L-Aq7fdZ7AuN040dVOcY5fiF4iHTBueoRSc7McWg02GrouFPQiHJvq2lrohQ5GHYwjfknxP-70R6U5JFMKAgbG4iAOR35EDOJ7d20fVTg9-cqSnujhSftjoa7sKfRCSBBmjVOsWM8qdVxgiEtzbnZObLeOYtF6_QUrXvkdUHJuoVGMhIgt2ajXF8snGs5FnWcof32y_r4nprMdsjeduherqRz5nDcHqVk7_XxJJ1uwXGPpOT9VZY-yxYgpe8T_M69p_gmFSTngqVkrJdFl_gDp2Y7X7OrET0O_c_b-b5ak0Q5C3MoW7YAmlL5pmcA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/15118cd8c7.mp4?token=J0gMm3_xIwL7AiXnZsSkEhjm1L-Aq7fdZ7AuN040dVOcY5fiF4iHTBueoRSc7McWg02GrouFPQiHJvq2lrohQ5GHYwjfknxP-70R6U5JFMKAgbG4iAOR35EDOJ7d20fVTg9-cqSnujhSftjoa7sKfRCSBBmjVOsWM8qdVxgiEtzbnZObLeOYtF6_QUrXvkdUHJuoVGMhIgt2ajXF8snGs5FnWcof32y_r4nprMdsjeduherqRz5nDcHqVk7_XxJJ1uwXGPpOT9VZY-yxYgpe8T_M69p_gmFSTngqVkrJdFl_gDp2Y7X7OrET0O_c_b-b5ak0Q5C3MoW7YAmlL5pmcA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
مصاحبه این خانم در الجزایر و تبریکش به یکی از کاندیدای انتخابات بابت پیروزیش خیلی وایرال شده.
"
منم کلی سوال دارم
🙂
"
@News_Hut</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/69242" target="_blank">📅 11:26 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69241">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🎙
خبرنگار:
نیویورک‌تایمز گزارش داده قبل از شروع جنگ، شما به ترامپ گفته بودید برنامه موشک‌های بالستیک ایران ظرف چند هفته نابود می‌شه، بدون اینکه تنگه هرمز بسته بشه و حتی ممکنه به تغییر رژیم هم منجر بشه.
اما الان بیشتر از پنج ماه از شروع جنگ گذشته، ایران هنوز موشک‌هاش رو داره، رژیم همچنان سر کاره و عملاً تنگه هرمز هم بسته شده. چرا ارزیابی اولیه‌تون این‌قدر اشتباه از آب دراومد؟
🇮🇱
نتانیاهو:
این اصلاً ارزیابی من نبود و چیزی که نقل کردید، درست نیست.
فقط یه پیش‌بینی می‌کنم؛ بعد از این شکاف عمیقی که بین مردم و حکومت ایجاد شده و اتفاقاتی که رخ داده، فکر می‌کنم این رژیم در نهایت سقوط خواهد کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/69241" target="_blank">📅 10:44 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69240">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e988916503.mp4?token=bqpkOw-4S68DBRKZF2x61t0Mibd06136FDt4eyVqYI0bX7GLEGsibJF5kDxMzSrAlWxYCJb6P-eDu829qRZhyHBmevxCoqagf7xxep4n1WOh6YHNjACxpEib81T__k10VkFffVI0DYzrUqwnWZMQ0wDzxgjW3WFrWtiPv6XeSwtnMpBTzenjkJBOPi36cSB2qNHyQ2ee9Xj_z6eobB9fe5rBqASxTclWgxkRU_jAj_74dbPoYvPdquqdidg8jUfxutG9i3mKAStcs1_OjK7tkByEFCb74WFYG-6inusnPf4xqyp6tgmv3Ots9L0cpIcs-XAzzFN4vA46PokW1XVJbQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e988916503.mp4?token=bqpkOw-4S68DBRKZF2x61t0Mibd06136FDt4eyVqYI0bX7GLEGsibJF5kDxMzSrAlWxYCJb6P-eDu829qRZhyHBmevxCoqagf7xxep4n1WOh6YHNjACxpEib81T__k10VkFffVI0DYzrUqwnWZMQ0wDzxgjW3WFrWtiPv6XeSwtnMpBTzenjkJBOPi36cSB2qNHyQ2ee9Xj_z6eobB9fe5rBqASxTclWgxkRU_jAj_74dbPoYvPdquqdidg8jUfxutG9i3mKAStcs1_OjK7tkByEFCb74WFYG-6inusnPf4xqyp6tgmv3Ots9L0cpIcs-XAzzFN4vA46PokW1XVJbQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
سؤال: آیا هدف شما همچنان تغییر رژیم است؟
🇮🇱
نتانیاهو:
هدف من این است که اطمینان حاصل کنم ایران، با وجود این رژیم، به سلاح هسته‌ای دست پیدا نمی‌کند.
این موضوعی است که من و ترامپ هر دو بر سر آن توافق داریم، چرا که در غیر این صورت، با دنیای متفاوتی روبرو خواهیم بود.
آن‌ها با سایر کشورها و جوامع دیگر متفاوت هستند.
🎙
سؤال:
همین دیروز گفتید که به نظر شما دستیابی به یک راه‌حل دیپلماتیک بعید است. چرا فکر می‌کنید ارزیابی‌های شما تا این حد با یکدیگر متفاوت است؟
🇮🇱
نتانیاهو:
خب، نمی‌دانم آیا واقعاً بعید است یا نه، اما می‌دانید، من نسبت به شیوه عملکرد ایران تردید دارم.
آن‌ها همیشه دروغ می‌گویند، همیشه تقلب می‌کنند و همیشه وقت‌کشی می‌کنند. آیا ممکن است این رویه با اعمال فشار کافی دیپلماتیک و اقتصادی تغییر کند؟ باید امتحان کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/69240" target="_blank">📅 10:38 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69239">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dF194lViZSC8hs0spG09MZ-yRAPB1FA5UE3O0IGcebeLPug6qWQRhc4N2hz-oWFrVBfsC0h3WZeJ29Z6FfYYhq7yuS-8DC_iSt9JJWgjEz1UX3HY0oCCLsDzNAiKyzcBNPf2UVWkz4sREOkLi6j5Swzv15lSuHTG4JTk_REatSoteaWons-dNghZe4e7u_4Rjcn2YlyYY3FAx6ISqT5EEOpFMvac6a-jYyXIrwZXFG92z6P_hkt3D1_c2cjcdzU6xrys-9f5wHa63RJnG3OkPim0bX4L3epUVirTaSu4zsyzPDsTWBZaRKeuEtl549R1fu6qNQ6Rpt2a4YbXNR_z2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⁉️
🇺🇸
تحلیل مرکز مطالعات استراتژیک و بین‌المللی (CSIS):
ایالات متحده اکنون تقریباً ۸۲۷ موشک پاتریوت و ۲۷۸ موشک رهگیر دفاع هوایی ارتفاع بالای ترمینال (THAAD) باقی مانده دارد که نسبت به تخمین‌های قبلی به ترتیب ۲۳۳۰ و ۴۵۲ کاهش یافته است.
تحلیلگران هشدار می‌دهند که با وجود تلاش‌های گسترده برای تولید، تکمیل مجدد این موجودی موشک‌های پیشرفته می‌تواند سال‌ها طول بکشد و در صورت بالا ماندن تقاضا، ظرفیت محدودی برای سایر موارد احتمالی عمده باقی می‌گذارد.
سی‌ان‌ان گزارش می‌دهد که منابع پنتاگون می‌گویند این تخمین‌ها نزدیک به ارقام داخلی هستند.
@News_Hut</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/news_hut/69239" target="_blank">📅 10:33 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69237">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8d926097b7.mp4?token=F3kP31ukWXbd1yNEs_Bu57my1GO1dW-GVD5JNNnl_OslcdtSQT97DWLe-jtH-FK7qVOKbmcBoiiKYMo11QDouqRCnAkfQxe0kvkO7r3rG15eURKWNZvf7hMiG9v-41ElhWt13bdbMNa-T10OdS8NMtdwPZXPNSacha16opPqRR2UaE5oy9xnUD6MfQ3Beoe6nr_Uk0ZHPIcqV6eLtIH3U4Z3p5aZJslH_CJqPYA59iVh3lelY6t2v_wxa0XYJqRMYW0rbc6caf99d2VTcMyqNq-ZtftfDDt6_zcAdwAwIUo0mheywtc-_dTiehzJHPp6gu7kJ-xwiUYnRHszxDg6qg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8d926097b7.mp4?token=F3kP31ukWXbd1yNEs_Bu57my1GO1dW-GVD5JNNnl_OslcdtSQT97DWLe-jtH-FK7qVOKbmcBoiiKYMo11QDouqRCnAkfQxe0kvkO7r3rG15eURKWNZvf7hMiG9v-41ElhWt13bdbMNa-T10OdS8NMtdwPZXPNSacha16opPqRR2UaE5oy9xnUD6MfQ3Beoe6nr_Uk0ZHPIcqV6eLtIH3U4Z3p5aZJslH_CJqPYA59iVh3lelY6t2v_wxa0XYJqRMYW0rbc6caf99d2VTcMyqNq-ZtftfDDt6_zcAdwAwIUo0mheywtc-_dTiehzJHPp6gu7kJ-xwiUYnRHszxDg6qg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
ویدیو ای از حملات دیشب آمریکا به نقاطی از کشور
@News_Hut</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/69237" target="_blank">📅 09:55 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69233">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/04e8c731a4.mp4?token=U8jGZFp0cQ8ethRDNCyA2sN1JFcCQMbgd0X64nZ9Cycc_7fNHcKqIz2Bwv0Dl_Blv6uKuOeWzarJl4q7M1BD6YusrdFFiHxA6KFgwp-9kTbdfu1hY7zYXdYzXgb4jbAUt-ogGWc46xzlLXhgttV631NeVw-E3NeqdRDNOFH1hHrCgf-oXY6uPjiYDwW_6TbSefGB2sv8KBo6lUKXJZ5GIZmazZbTEWAaYcWafOg74Vy9dtthGRrM5IEIMgI7ivGNf6ihQwVSCLW58UQznKPdO0xSi-RGE2KNTEauDILe_lM1rih7Fz2E-eM-ZiTb4t6oIg5sYxYv1duQoxzqvQLT7w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/04e8c731a4.mp4?token=U8jGZFp0cQ8ethRDNCyA2sN1JFcCQMbgd0X64nZ9Cycc_7fNHcKqIz2Bwv0Dl_Blv6uKuOeWzarJl4q7M1BD6YusrdFFiHxA6KFgwp-9kTbdfu1hY7zYXdYzXgb4jbAUt-ogGWc46xzlLXhgttV631NeVw-E3NeqdRDNOFH1hHrCgf-oXY6uPjiYDwW_6TbSefGB2sv8KBo6lUKXJZ5GIZmazZbTEWAaYcWafOg74Vy9dtthGRrM5IEIMgI7ivGNf6ihQwVSCLW58UQznKPdO0xSi-RGE2KNTEauDILe_lM1rih7Fz2E-eM-ZiTb4t6oIg5sYxYv1duQoxzqvQLT7w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
🇺🇸
هواپیمای باری C-2A Greyhound متعلق به نیروی دریایی ایالات متحده، دیروز آخرین پرواز خود را انجام داد و اکنون پس از حدود 60 سال خدمت، رسماً از خدمت نظامی خارج شده است.
🗣️
با از رده خارج شدن هواپیمای C-2A Greyhound، تمام هواپیماهای نظامی که توسط شرکت Grumman قبل از ادغام آن با شرکت Northrop Corporation ساخته شده بودند، اکنون از خدمت نظامی خارج شده‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/news_hut/69233" target="_blank">📅 09:15 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69232">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🔴
چالش ۳۰ روزه: از صفر تا سود مستمر با فوتبال!  ما یک چالش ۳۰ روزه رو شروع کردیم که توش با تحلیل‌های روزانه و مدیریت ریسک، موجودی حسابمون رو چند برابر کنیم. تمام تحلیل‌ها و فرم‌ها کاملاً رایگان در کانال قرار می‌گیره تا خودت روند سوددهی رو ببینی.
➕
پیش‌بینی…</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/news_hut/69232" target="_blank">📅 03:01 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69231">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/316f36114d.mp4?token=q9CdhtKzQ-2mD1ATvqBHLH0_x8lT3HK252VKDmRvaI3YMCQ_8ln5FhrTSiBMNbrqtYNvyb8yBn26piEOxDZDs7yhKCfNdSkIt6NQkoVcmXvZyEeywD4V961-BZCCaY4U5Mq_pWoQyC20PQSeMeidvTgEfct3rtJmjJDYtrR5BqkugGkCy5mD7mzLPa_l_l-0Smd5wzXGdaHe7rhVM4tuwPDhr19h3RFA6CE6Zhg2ZCr-J5SgFGpFFkxdybZUk3hgyyO1eJXiBZKKRsjfkYDZ3BjLfhTkpindh5y4aqN31xENLvpeRV2whDiWVL0Z4EE4zfegE9KYXtwDtYwlgMZ0Zg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/316f36114d.mp4?token=q9CdhtKzQ-2mD1ATvqBHLH0_x8lT3HK252VKDmRvaI3YMCQ_8ln5FhrTSiBMNbrqtYNvyb8yBn26piEOxDZDs7yhKCfNdSkIt6NQkoVcmXvZyEeywD4V961-BZCCaY4U5Mq_pWoQyC20PQSeMeidvTgEfct3rtJmjJDYtrR5BqkugGkCy5mD7mzLPa_l_l-0Smd5wzXGdaHe7rhVM4tuwPDhr19h3RFA6CE6Zhg2ZCr-J5SgFGpFFkxdybZUk3hgyyO1eJXiBZKKRsjfkYDZ3BjLfhTkpindh5y4aqN31xENLvpeRV2whDiWVL0Z4EE4zfegE9KYXtwDtYwlgMZ0Zg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
چالش ۳۰ روزه: از صفر تا سود مستمر با فوتبال!
ما یک چالش ۳۰ روزه رو شروع کردیم که توش با تحلیل‌های روزانه و مدیریت ریسک، موجودی حسابمون رو چند برابر کنیم. تمام تحلیل‌ها و فرم‌ها کاملاً رایگان در کانال قرار می‌گیره تا خودت روند سوددهی رو ببینی.
➕
پیش‌بینی تخصصی بازی‌های دوستانه باشگاهی و تورنمنت‌های معتبر
➕
فرم‌های گلزنی (بله/خیر) و گل بالا/پایین با تحلیل آماری
اگر می‌خوای از روز اول چالش همراه ما باشی، همین الان وارد شو:
🔗
https://t.me/+L5I8ulM6jEc2YmE0</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/news_hut/69231" target="_blank">📅 03:01 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69229">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CxWMJt8_J84tuM2VkEK65dM8wDHM5n6Di8Zv4oPKomX7Sx-zqvnJXsqQO5WBe_BxzZu-pMqdmb3b30dc4y06fC59BOFdKB_i7YGa9aua8VR8CDITmri_AprTp2Q7h2c7PIld9dTsh04_Uk44S11K3_1EMM7-5_VhXcmeJYLq3Sgc_VxBs65HOnusYzCQuyShsubFidZfLoIpV4RWnV4bw8amcc_NzAGm27Mg19BypIXmhzvPARWxByb8wLLlM9GEamYG_HP-uV5nhiEj8CGLmUg7zjDnxe0qVQkI1assktlMK8usGsJ4hTautTpkah3XIKKOZ1iMqvrb62eO3hmeVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jz4FY1iln9HRJlcKVH4F3e-KKzYDQeh0UX23F7B0zbuG9AVgFWq68ZuNgOjHade98tOkCUwCnBkiLrZLEEJQkpPLnvXbYgHDxCfNzynJksJMOkuJLLF1lqav2NAz9QPstG0VDDGfUEOlRDpyAfZnTFfr_-aGBq0m97fwmReFmgU5oAZDrD3sNDqpjukNbcSfmVwqeQpTwC95QAGlFQru6a0vv5ILyQ7IVw-ejWWcsGkTwGFqelpbKjFDUw7fv3F_60yum6Sn7YG0XtBn3MFkzH4aXXSRM_FyP6090X87FsbieOpWjgLkjOxK0UKhhwONcgfE26x4yxo3Pp5oMw7moQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
وال‌استریت ژورنال: دریاسالار برد کوپر گزینه‌ای را برای یک کارزار هوایی تنبیهی علیه ایران آماده کرده است که می‌تواند تا دو هفته به طول انجامد.
کوپر معتقد است اگر ایالات متحده خواهان اثربخشی اقدام نظامی است، باید برای شکستن بن‌بست موجود، حملات هوایی خود را تشدید کند تا بدین‌وسیله تهدید موشکی ایران را به‌طور قابل‌توجهی تضعیف نماید.
این رویکردِ «اقدام گسترده» — که یکی از چندین گزینه تدوین‌شده توسط اوست — نیاز آمریکا به استفاده از مهمات پدافندی را کاهش خواهد داد، زیرا توانایی ایران برای انجام حمله کمتر خواهد شد.
- مقامات گفته‌اند که در صورت تصمیم دولت ترامپ برای بازگشت به عملیات‌های رزمی عمده، نیروهای اسرائیلی نیز ممکن است در حمله بزرگ احتمالی آمریکا مشارکت داده شوند.
- کوپر در جریان تشریح گزینه‌های مربوط به یک کارزار هوایی شدید، از حمایت «هگ‌ست» برخوردار شده است.
@News_Hut</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/news_hut/69229" target="_blank">📅 02:45 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69228">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gWjXKx9bVxNirmLZ5NW49R2ubfZd9ex2CDPvedfgQLCfpqlMUulb7t4Ka2J5DAb3r4VL0iZrMBp_FHohtRKmfUH6WNS284OhzdtAvVbv3hSzlSG7nRyljJ5SnKvDa2ep_sKKJgHzdUwNLJNiWq94cRkpg2VJGT3mg-FmW2O7KXP4M02bjK6Kt09gX_sR8Ah-PVYhV1B8lvPagMOtKW4MOEK79eFubcU-z1gwbnxV2n1AGIIIOvs6alLc2UaIz4BTz31LN-k58YAQCf1qk5kMGnpJs7U2uPPJ7FO5dWVNORxYnnBG-TdApzYQG2QzMHL7C7Iw1zHeXo0CzMQJa-WVFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
#فوووری
؛باراک‌راوید:
یک مقام آمریکایی به من گفت که ارتش ایالات متحده در حال انجام حملات هوایی در ایران است.
@News_Hut</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/news_hut/69228" target="_blank">📅 02:44 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69227">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🚨
🚨
🚨
گزارش های اولیه از انفجار در نورآباد ممسنی استان فارس
@News_Hut</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/news_hut/69227" target="_blank">📅 02:28 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69225">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AClbX-ILldNdmIGIdxsGE3J5f54_djYYtEla4HXYRiNFo_8bqKpBiKnjVIHoC4ys313UjrOLRzhqrVDg5gvmAiIih8BF3jxTv2ZvSVdVJwzAJL8OwzmKH6YyByRpZ2aFpw9sMg7tijOJsJrXrdKsNA0x1xq_-PDZbw0nWS-xGJQ9GGxQkPe3aJL0SF7yMD8BZTN95Y146tj9igfIrJrANHI4UDuYzoAK_AAs-eyS2k4_OC-w9vvBQkU_GUazoIIvmYhgY1tNMCSAg4IDtwNmV9PQAk92ueJMhNv2kmK9YbvOMd50iozeAnhZEL8WpcVLcmQxaB9wCQn_OAzVtK1KLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
بعد از توییت عراقچی درباره اوکراین، خبرگزاری رجانیوز، عراقچی رو ماله‌کش خطاب کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/news_hut/69225" target="_blank">📅 01:56 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69224">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gKBHf3qskw9tp6M00gvVzzFHMzVvINWfl4EDYR4KQIYJK1MrSWj4b7oMmNd0gsA13LwgKZCye7dJCxB3H0-5dxiYuB748hZMgmTc1OinM_0wyQ4kStZBRmfxbckGksIXsuCYCbTiZIcBGzozCUtmLxGvNlL2akYZ-_mZUtFtQpnA8isY3xN8R8Zx7dyeNfmuA-VVC9MVuAbP0ZdrApvuapvgcxxxxCqMMxTvkVwh0GRccf51E_3nYfZsYOZqIFQL4pUVb68IMm_A7Uoj0pcZugjqnfiYs4agRrPfaRsdhHPGtJ_9gVXzDCR1KHZATZvYLpouMkNVSCxMUGY5EY4ZfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
حساب توییتر خبرگزاری تسنیم وابسته به سپاه بسته شد.
@News_Hut</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/news_hut/69224" target="_blank">📅 01:08 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69223">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H0XgP5HrSlM-xgEpG3dNes6MULozKXneEXXE6iZYcY108LBSstwerVsR6ZVYeW_SzhS6KMOqEhx-VdkZD08vSytn_KzEvy9eM9kfhJ3n5lflMbogcuWbUTMyQcyy6cpAVZ-by8oYb98y44xQs_LiO7Y2RiW8xikLD3bDVar9sRV21E2WNASMy5IN_yQu_h-aIo88CYYX9e7K4X66r6lLcSzQu1Wh7boPvRqg1ZWb24fR6i3rrg_pDKd9bv1yvIXhuHSehc5ObsTnpfPuGw6ACe8098RyW--AGdugalhYa2U_0XbKfj0zuk-dnf6_EPAp0y__4yOtdj6SKrEjax_V3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‏9 فروند هواپیمای تانکردار آمریکایی و یک فروند هواپیمای هشدار اولیه مدل E-3B در حال پرواز بر فراز خاورمیانه هستند.
@News_Hut</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/news_hut/69223" target="_blank">📅 01:03 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69222">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ILvqHxKH2xja10eDrXq0MDe0IaT8f-G9h8b08PyJzJMZqU2fnrl3e52IXx9MktK-UFvlbxORcv6V5s79e38bOmydSwEab-CDjO5s5e8o5n8rkcSfhX-99n86_8RcbePa7M-ZFmy26lNfT_0m229cE51pqboj3LOu67-WtJo1YRB9HM_dlVHj0szz61GdjApOsbP7hbWg8BDQpgMWG24Ylh6XVYt9tDaicKi0SYtYCh6bt4fQ35282IySvvm05SRwW9czBZdjEOHMruHqni2firFdKmsY1Vh3Pz7UxeYRk-BU8DAah7MXMETb3WCjvQh6U8AGTxNMVOtyWzI3X2i6Gg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
شش سوخت‌رسان آمریکایی در آسمان منطقه در حال پرواز هستند.
@News_Hut</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/news_hut/69222" target="_blank">📅 00:47 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69221">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🚨
🚨
🚨
❌
گزارش های غیر رسمی از شلیک موشک از یزد  @News_Hut</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/news_hut/69221" target="_blank">📅 00:44 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69220">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WXkOja7QieARbbKc8-SIGiKB4HRh6m0fT73B3yiLnx0UTxrgra1Y-txtb62FUaZGGD2RXCgp_m6Ry6u7Upf5BW25bLGKvx6jDVhlJof4TwOaDxGAYi9KuXony19UZZWVW8h5AC96Ai_1LM54aGf_kp4Ed5w7Yh0qLVCJEtjj0uJahNlNREuRCZyX3-W1pBL968Ls9rjGwRiw7_KzPncghKqk5AJPO_usdEqO4jj8UHnCGFhMLzuKOh7fKU7_AzWNN7WNUvgyhTlA8oGi7w1s32zRg7cPBs5ZJYiIMay1-aZ9S3Na0yX0KRwNLGRcBQMO64vFyIC9rJEptPgF9MgvSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
سپاه تو تلگرام یک کانال و اکانت ساخته بود گفته بود هرکی تو اردن و کویت تحرکاتی از نظامی های امریکایی دید گزارش بده؛
لحظاتی پیش تلگرام سیک اکانتشو زد.
@News_Hut</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/news_hut/69220" target="_blank">📅 00:39 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69219">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🚨
🚨
🚨
❌
گزارش های غیر رسمی از شلیک موشک از یزد
@News_Hut</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/news_hut/69219" target="_blank">📅 00:34 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69217">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/c08d37ce36.mp4?token=p0GnUuumtbYRiwNCdtaPytCHhc9XJ3Hn1FjRindL_9X7RBalws7Cuuar7Mmoekfu1mLfoOH3TV0R4NoPZIar1FT2SViu-nVZDJlXfmxro5ChdHYeY91cOJSzUIMf71Wgj1yWP1aZzjTNNBWSZasgflawZTSEUt9VC6GsnZWvA9Rw4V4G17Ae3JHe9Zk6rRaSA6zgpHMtvjmSacYtP69sETIkB5OBZCvP8R_Zqg27xQwuCJqF0RtgGWDJkKhgolZuHszYs8IOZXkVYsAD5T2NGlzsp9SxrZmJGry_dK08mScVmTixtb_mHNvxJB0__GzhY66a5-ZosjM1srl8cRwqpQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/c08d37ce36.mp4?token=p0GnUuumtbYRiwNCdtaPytCHhc9XJ3Hn1FjRindL_9X7RBalws7Cuuar7Mmoekfu1mLfoOH3TV0R4NoPZIar1FT2SViu-nVZDJlXfmxro5ChdHYeY91cOJSzUIMf71Wgj1yWP1aZzjTNNBWSZasgflawZTSEUt9VC6GsnZWvA9Rw4V4G17Ae3JHe9Zk6rRaSA6zgpHMtvjmSacYtP69sETIkB5OBZCvP8R_Zqg27xQwuCJqF0RtgGWDJkKhgolZuHszYs8IOZXkVYsAD5T2NGlzsp9SxrZmJGry_dK08mScVmTixtb_mHNvxJB0__GzhY66a5-ZosjM1srl8cRwqpQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
فیلمی عجیب از تجمعات چند شب پیش خرم آباد!
@News_Hut</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/news_hut/69217" target="_blank">📅 23:53 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69216">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">این گروه با گروهی که ما با آن سر و کار داریم فرق داشت. آنها قبلاً عذرخواهی کرده‌اند،</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/news_hut/69216" target="_blank">📅 23:21 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69215">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e6df873441.mp4?token=kthVUWicVXWT6hn1TesZLP0e4bujK3LIDLVFWxhLXkGhHEz9ClJ8NRJgk33UnMMxMH96L4UcV2pRAyTe-wBW8la51jmGNzoclHXZsf2PIEm5VqAG2u2byZOYP5bvrEK0fu4TIfPDSoHDyzJSfL2pV0Fg5OLnETfoj_vtAyboA44nl4DcNezfQZWypBk1tUCON5fME2w1jdBNsiP98B6lHSHmwuP9fx5t-iyKUy2A46Ei2j0c2eYvHW6mlrVyMn0qJeVtHcHcai_b1TKaZANpd8nIj5YUAxW4pNGf3i0e1_lYrTuGdpDytR14hzue6uZqq9mmxKpnUwDOaUcDl4DJDA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e6df873441.mp4?token=kthVUWicVXWT6hn1TesZLP0e4bujK3LIDLVFWxhLXkGhHEz9ClJ8NRJgk33UnMMxMH96L4UcV2pRAyTe-wBW8la51jmGNzoclHXZsf2PIEm5VqAG2u2byZOYP5bvrEK0fu4TIfPDSoHDyzJSfL2pV0Fg5OLnETfoj_vtAyboA44nl4DcNezfQZWypBk1tUCON5fME2w1jdBNsiP98B6lHSHmwuP9fx5t-iyKUy2A46Ei2j0c2eYvHW6mlrVyMn0qJeVtHcHcai_b1TKaZANpd8nIj5YUAxW4pNGf3i0e1_lYrTuGdpDytR14hzue6uZqq9mmxKpnUwDOaUcDl4DJDA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
پرزیدنت ترامپ درباره ایران:
ما ضربه بسیار سختی به آن‌ها خواهیم زد. این را می‌توانم بگویم، چرا که کار زیادی از دستشان برنمی‌آید.
این گروه با گروهی که ما با آن سر و کار داریم فرق داشت. آنها قبلاً عذرخواهی کرده‌اند، اما، می‌دانید، باید کمی آنها را تنبیه کنیم.
شی به شما گفته بود که چین هیچ‌گونه سلاحی به ایران نمی‌دهد یا نمی‌فروشد. گزارش جدیدی حاکی از آن است که ایران ۴۰۰ پرتابگر راکت از چین دریافت خواهد کرد. ترامپ: این موضوع تعجب‌آور خواهد بود. او به من گفته بود که در این کار مشارکت نمی‌کند. او می‌داند که من بسیار ناامید خواهم شد.
@News_Hut</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/news_hut/69215" target="_blank">📅 23:19 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69214">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ad144cccc8.mp4?token=tRhF0NI78U09PcDSsYqQZLkRYK2Yd9FFFsrgKKhdxg7Pwuv7Z8pTj29IVFAf_CQUQ0E89WP7PyemGEzdxbBs0nUhH2Vs9oYAfASPYMZ2CTrveXW51ceQJI7H0Uxvy4SFXk-Rina4XZGOjiq8ggbiHuVpWE83ZaAUiaJuPZhEZXOshmESom_u1AaeKmmMliwiQymz2p_4tBQJZ97soMKm8bqVLbKXwJrtxbWZSFNtB4iMwQ9qTi55ZHrF4uwhmVFzsA-La7chPRBvw43zsBi5kuQsGJlBTT__wQweED4q03cirXy0q1bt0Xixz_I3tO44ltDbBwQaBKzBwnVWIBghjw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ad144cccc8.mp4?token=tRhF0NI78U09PcDSsYqQZLkRYK2Yd9FFFsrgKKhdxg7Pwuv7Z8pTj29IVFAf_CQUQ0E89WP7PyemGEzdxbBs0nUhH2Vs9oYAfASPYMZ2CTrveXW51ceQJI7H0Uxvy4SFXk-Rina4XZGOjiq8ggbiHuVpWE83ZaAUiaJuPZhEZXOshmESom_u1AaeKmmMliwiQymz2p_4tBQJZ97soMKm8bqVLbKXwJrtxbWZSFNtB4iMwQ9qTi55ZHrF4uwhmVFzsA-La7chPRBvw43zsBi5kuQsGJlBTT__wQweED4q03cirXy0q1bt0Xixz_I3tO44ltDbBwQaBKzBwnVWIBghjw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
این ویدیو رو بفرستید واسه اون تعداد از رفیق‌هاتون که عشق دعوان:
دیه‌ی شکستن کامل بینی : 2 میلیارد و 100 میلیون تومن
شکستن فک بالا : 160 میلیون تومن
شکستن فک پایین : 640 میلیون تومن
شکستن هر دندون : 105 میلیون تومن
شکستن دست : 160 تا 210 میلیون تومن
شکستن سر : 120 میلیون تومن
شکستن پا : 210 میلیون تومن
شکستن گوش : 350 میلیون تومن
کبودی صورت : 6 میلیون تومن
@News_Hut</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/news_hut/69214" target="_blank">📅 23:14 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69213">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3687c44382.mp4?token=imnJtJZvh-7b2RR2HbLyukZb71X3Ewj2rqqEUKd56hhK24b_dwl3YtrZjiY5KPvCQbaOF3hf3id2gjaj8lvAUCWOqnwfpAB5KqZtNrF2I-Q0AhF-19J7R1C8buoujkA_jlntB9WajqwIesJj4zYyeNw200G-ZCi_Wj-MO89tuQA47qbhGCaFM3ogOvRJ8vjuOqSitA_eM3cFcJ8674LQgSZ5wrCVY2HLRofHryzywBmNQLuKrr7jihPhrI_OA8f0cNNplHf4LL9QpHsp7T0DhfMFGsl9dnmieLKg_BtVyzwz1pWs5OAZk-HV3LiYIXyEsurWhY6DhagEU5jOu3BaXA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3687c44382.mp4?token=imnJtJZvh-7b2RR2HbLyukZb71X3Ewj2rqqEUKd56hhK24b_dwl3YtrZjiY5KPvCQbaOF3hf3id2gjaj8lvAUCWOqnwfpAB5KqZtNrF2I-Q0AhF-19J7R1C8buoujkA_jlntB9WajqwIesJj4zYyeNw200G-ZCi_Wj-MO89tuQA47qbhGCaFM3ogOvRJ8vjuOqSitA_eM3cFcJ8674LQgSZ5wrCVY2HLRofHryzywBmNQLuKrr7jihPhrI_OA8f0cNNplHf4LL9QpHsp7T0DhfMFGsl9dnmieLKg_BtVyzwz1pWs5OAZk-HV3LiYIXyEsurWhY6DhagEU5jOu3BaXA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
پرزیدنت ترامپ درباره ایران:
ما ضربه بسیار سختی به آن‌ها خواهیم زد، چرا که نوبت ماست که به آن‌ها ضربه بزنیم.
آن‌ها می‌دانند که این اتفاق در راه است و از ما می‌خواهند که چنین کاری نکنیم.
آن‌ها دیشب تلاش کردند با ۵ راکت به ما شلیک کنند؛ ما همه آن‌ها را رهگیری کردیم.
@News_Hut</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/news_hut/69213" target="_blank">📅 23:07 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69212">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">ویدیو وایرال شده از یک پژو405 که درحال فرار از دست مامور هاست اونم بدون لاستیک!
@News_Hut</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/news_hut/69212" target="_blank">📅 22:34 · 07 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
