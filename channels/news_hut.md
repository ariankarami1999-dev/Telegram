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
<img src="https://cdn4.telesco.pe/file/O4y7_nVToHYxusaREwx8d8sM7w88xMfGmuipw6sHA4rsD13pkL1H8wz0s-2IEDirmsw4oNLAfBGEm5BxhFL8ArH7jiSRawffylSnKV7F4z885ms-dDmPB5VKZW2TGRlKC7P6W0VhhYhb-fPK4z9Jq2QVGGa0DC0w0iz6oq-rBVIG_5m7R_GrRgSNb3Nm9mhWSmvRZMvJIf6HEJLi20OUMYMiPhVWzQu8894Q9SOLda0nnQftnrMuxEk6AxuspOZm5jgfOCUFWK9Vg9hKz0pm_qF_u8ou-B3rT6DRadscfnnh1aC1OEas5PBmvA3tQr5jaXcH9vrbgLh6pump7ftLjg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 145K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-06 16:18:26</div>
<hr>

<div class="tg-post" id="msg-69117">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/T2LJ8gRU7eN-HBxowpaRj5oNuEN_mpJrj6S33x88WoXFTCm8pWb5Ziqi39bvbUQDyv5IvtgE4nqVIyN3bw6rKreiOPDo_ErcO_PZLsOVKnWPLl0HWQ1fB28KY93uuwg4F4h34vWgP5fGfaNXM0I17IwPPP7xIsxbsKoOf8CKJr4Ptu9QHJWljZnaAFMj7G-4FqpNiwhuFnvJGzoVleU-B_8p_fmNfu2h1j0lu5vq6RoX9uWtdCACYrcF1ZsUChSAv0AOJV98zb7m47MpIaVVfIU1H7XTXeqy2zIddmO0oWlDozBRcSG4wet5ELvxHZujdqRjNocobNNgMjqNbnEQag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bI1b1wQl3UKNjlFIIGai6wefuKMBc5o1ZIXmWHuUU3AwyD8jvHG2_ZYOzYzWFiLgf2c5rqc3hj2VifvBD9M5t26Fej0mk9fO_ojUOIAzF4oEr-1yVdiLtg-dbMhQCptMAXhMuEBasDw08Z7UwAUwdImEPeYX5duRsYbGJ756WSgC1CkTED4v3DG_YATxP0uHI9m8MN_o3d4JX-i0u4V8RxYEIoKy3zPYyYQyPjd6LelkRh4oMwuzgxe9v-LhtCA8PKUP9dL7NYV8GLgGft0VLpLKCMbyQSzkX0cALo7Yn-li1ODyKVLv6kVziVqF553ackyx92JVx4foMSkvdXJO8w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
🇺🇦
❌
🇷🇺
اوکراین بیش از ۳۹۰ پهپاد را در طول شب در منطقه مسکو به پرواز درآورد، که به نظر می‌رسد تلاش دیگری برای حمله به مراکز لجستیکی Wildberrys باشد، اما در واقع به جای دیگری اصابت کردند.
در Kaledino در نزدیکی Podolsk، یک پهپاد باعث آتش‌سوزی بزرگی در یک انبار لجستیک شخص ثالث به مساحت ۱۸۳۰۰ متر مربع شد که به Auchan، Magnit و سایر زنجیره‌ها خدمات ارائه می‌داد، درست در کنار یکی از بزرگترین مراکز Wildberrys که به گفته Wildberrys به طور عادی فعالیت می‌کند.
در Chekhov، یک پهپاد دیگر به طبقات بالای یک ساختمان مسکونی برخورد کرد و به بالکن‌ها و دو آپارتمان آسیب رساند، اما هیچ آسیبی گزارش نشده است. بقایای جداگانه باعث آتش‌سوزی تایر در یک کارخانه بازیافت لاستیک شد.
@News_Hut</div>
<div class="tg-footer">👁️ 1.17K · <a href="https://t.me/news_hut/69117" target="_blank">📅 16:15 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69116">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/0df10b659f.mp4?token=Uj1kKajg_P966IDzwOhTjB_e0cV0gbz9NvclMDpXmM5zIUmYv2IfQMPXnCveMhq6M5CFVntSkUmUQfvi4qeJt5geaFv_kTTPgFIyIKzAeyQJsS_7woBLUZzTAifhxLFEgvEmJnSaw4M1Sgq5CNFiTRDujI7bK9wRbij0pYWOiQ6UIpROieWcG8SGaZKx4yT6S4QcGjLDbmW2G5nwmV9KK9izIsVwIGm0qcuHSea_xP8h7mNMnMx0TFvwM0vKWVruZODaAOzuq7rNt5vA7vbu-voXP_5V9DQ3iMq9zjtjb-IslPnAjNy5p4Zs0VT7MoZgmGqDMYsGcnTi_3-KIKjnLoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/0df10b659f.mp4?token=Uj1kKajg_P966IDzwOhTjB_e0cV0gbz9NvclMDpXmM5zIUmYv2IfQMPXnCveMhq6M5CFVntSkUmUQfvi4qeJt5geaFv_kTTPgFIyIKzAeyQJsS_7woBLUZzTAifhxLFEgvEmJnSaw4M1Sgq5CNFiTRDujI7bK9wRbij0pYWOiQ6UIpROieWcG8SGaZKx4yT6S4QcGjLDbmW2G5nwmV9KK9izIsVwIGm0qcuHSea_xP8h7mNMnMx0TFvwM0vKWVruZODaAOzuq7rNt5vA7vbu-voXP_5V9DQ3iMq9zjtjb-IslPnAjNy5p4Zs0VT7MoZgmGqDMYsGcnTi_3-KIKjnLoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
بخشی از صحبت های دیروز ترامپ در میشیگان به زیر‌نویس فارسی:
@News_Hut</div>
<div class="tg-footer">👁️ 6.06K · <a href="https://t.me/news_hut/69116" target="_blank">📅 15:29 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69115">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/200b5b3122.mp4?token=OAfKiH9Up1dTO9vE-aSMhCXgfGgaEIMMf1A9f8WmmuyZLU4zkc7ZQEejrpMF4CKuhAupYY1JsXPp1eXjKkV7F65wSxnPyRhVOdYeBjG1m74HT7qh-rYeUVR0JNC_tuqj0N1L9GafaqjFbBATjFa3HIbXxO7SZxFILoT2FpyJqIdhyAnv43saMd14UIU56kDyx9pgJn2g5-nOXHDO2yGFPAYqtrzneZW0Q4Ck3-82v56dvTt8D8hxdsPo5BN3V6hgbJK9Ds0nwRqCWMTv_UYkhrc7C3lDFo6bBvo6RHvlKr6eITcIMDNkMNJhcO4M_3ftZ9FZYXLYvAVvfujEdzAyNA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/200b5b3122.mp4?token=OAfKiH9Up1dTO9vE-aSMhCXgfGgaEIMMf1A9f8WmmuyZLU4zkc7ZQEejrpMF4CKuhAupYY1JsXPp1eXjKkV7F65wSxnPyRhVOdYeBjG1m74HT7qh-rYeUVR0JNC_tuqj0N1L9GafaqjFbBATjFa3HIbXxO7SZxFILoT2FpyJqIdhyAnv43saMd14UIU56kDyx9pgJn2g5-nOXHDO2yGFPAYqtrzneZW0Q4Ck3-82v56dvTt8D8hxdsPo5BN3V6hgbJK9Ds0nwRqCWMTv_UYkhrc7C3lDFo6bBvo6RHvlKr6eITcIMDNkMNJhcO4M_3ftZ9FZYXLYvAVvfujEdzAyNA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
مراد ویسی تحلیلگر ارشد اینترنشنال:
جمهوری اسلامی فهمیده که ممکنه آمریکا و اسرائیل یه حمله شدید انجام بدن و همه مقامات رو ترور کنن.
بعدش مردم بریزن توی خیابون و انقلاب کنن، برای همین از قصد داره معترضین رو توی ملأعام اعدام میکنه که باعث ایجاد ترس بین مردم بشه.
@News_Hut</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/news_hut/69115" target="_blank">📅 14:50 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69114">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0c00215915.mp4?token=AJfXFaqyo4J6GWAtXrkLKJ-uBR2uVREAmGO0KtNMCOTbbQjGDfXh5PprKYv_OJ36XfGls_QWHcn_Xs-rZMLC07I6mDr99us7nwPM_Ta_usys2HCqLJuYlYHUlFsslA4QIe5YsA4dbd0EP2dLDg8P-nGjyOo-eYg7QDM66QmbSPzol4T59NnDPH4uhPVDOD0uPF6HVCXngvfR-hOgD0BQLwc1m42rohWIw2_Zg_xzSwZ2hw0IdNXsiS08x6wwkkEyh-gpDpjHcwPitvXZhUV8JO_eqTqcVAVEOWhpTtTzBKkJdZyLh5I-GAC8veQCcYbsW9R7rGqrr0iXvD6AgnPe8g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0c00215915.mp4?token=AJfXFaqyo4J6GWAtXrkLKJ-uBR2uVREAmGO0KtNMCOTbbQjGDfXh5PprKYv_OJ36XfGls_QWHcn_Xs-rZMLC07I6mDr99us7nwPM_Ta_usys2HCqLJuYlYHUlFsslA4QIe5YsA4dbd0EP2dLDg8P-nGjyOo-eYg7QDM66QmbSPzol4T59NnDPH4uhPVDOD0uPF6HVCXngvfR-hOgD0BQLwc1m42rohWIw2_Zg_xzSwZ2hw0IdNXsiS08x6wwkkEyh-gpDpjHcwPitvXZhUV8JO_eqTqcVAVEOWhpTtTzBKkJdZyLh5I-GAC8veQCcYbsW9R7rGqrr0iXvD6AgnPe8g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
مهاجرانی، سخنگوی دولت:
تو بنزین سهمیه‌ای فعلا تغییر قیمت نداریم، ولی هر وقت تصمیمی بگیریم، شفاف به مردم اعلام میکنیم و اونا هم همراهی میکنن.
فقط مقدار سهمیه دوم بنزنین (3,000 تومنی) از 70 لیتر به 50 لیتر تبدیل شده که اونم بخاطر حمله دشمن به مخزن انبار نفت‌مونه.
@News_Hut</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/news_hut/69114" target="_blank">📅 14:14 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69113">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fd184b2451.mp4?token=aKrsyiNK3DQR1fva1TH1l1sghot6Mi68ODCofjO6fRe-HtcYMZjhmW9Y-lx5WxqXH3IrI-OFYr7-G4hmqESc56VTsISRkCMM1KfRzvv9ztkUv6JMP2FPqp7EkWHpY7M7wJYo2VRPD-zMKCnA2pZ9BeEx5r_uNAQ3VMcqSDUJpMescSS8_roy78IxWXb5U00Q2i5GccE1OLlUcISMoTUzcOhwj-jRRtBkSH6Ru00m-HI3A3wZ4WTjEyDepdEOaa50PcBtWFhICrH-5t5VBAvnh1jDm3HN79oDn_rgQ9OqSNphAY-02uydDEX_UABaskgdpDvxZBYHe-pYWTUlO0gCXA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fd184b2451.mp4?token=aKrsyiNK3DQR1fva1TH1l1sghot6Mi68ODCofjO6fRe-HtcYMZjhmW9Y-lx5WxqXH3IrI-OFYr7-G4hmqESc56VTsISRkCMM1KfRzvv9ztkUv6JMP2FPqp7EkWHpY7M7wJYo2VRPD-zMKCnA2pZ9BeEx5r_uNAQ3VMcqSDUJpMescSS8_roy78IxWXb5U00Q2i5GccE1OLlUcISMoTUzcOhwj-jRRtBkSH6Ru00m-HI3A3wZ4WTjEyDepdEOaa50PcBtWFhICrH-5t5VBAvnh1jDm3HN79oDn_rgQ9OqSNphAY-02uydDEX_UABaskgdpDvxZBYHe-pYWTUlO0gCXA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇱
اسرائیل کاتس، وزیر دفاع اسرائیل:
نتانیاهو به دستاوردی رسید که چرچیل نتوانست به آن دست یابد.
او ترامپ را با ما همراه کرد تا به ایران حمله کنیم؛
بدین ترتیب، پیش از وقوع یک «پرل هاربر» دیگر، ایالات متحده را به اقدام نظامی واداشت.
@News_Hut</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/news_hut/69113" target="_blank">📅 13:42 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69112">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/136b2d25c6.mp4?token=Sn4XSz4Fj0FTVI6GdJonJ7NP8ui9Xa5kA6iRTeJyXEhHlEPfq0EC4yrznIeqg_D24Sj9qLxjSKc84nlvWZKcB9HEg-F73RUbcZ3pgH02yrwD6_-DAVhmxb0WN7GEeCn01pTm7ouO_qLcmbxyTEi36VwJWtFprzqyF6BQHxqJEljHeigmHvmoEdF0ZaQ9DY0L0H1reNyZ9AEQJrpU8zECvmeOspjq_Nscw6q5s6em7Qj-4GsDme39SHQ8m-x7sK88SqQTAb8ImBMw0B-8gIal0VUnvEKX5iIIaXkxD-oeh2JjQD-Ps63uAWIaC9qZmujsinK0cE3jt1hJsK4apTnzBQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/136b2d25c6.mp4?token=Sn4XSz4Fj0FTVI6GdJonJ7NP8ui9Xa5kA6iRTeJyXEhHlEPfq0EC4yrznIeqg_D24Sj9qLxjSKc84nlvWZKcB9HEg-F73RUbcZ3pgH02yrwD6_-DAVhmxb0WN7GEeCn01pTm7ouO_qLcmbxyTEi36VwJWtFprzqyF6BQHxqJEljHeigmHvmoEdF0ZaQ9DY0L0H1reNyZ9AEQJrpU8zECvmeOspjq_Nscw6q5s6em7Qj-4GsDme39SHQ8m-x7sK88SqQTAb8ImBMw0B-8gIal0VUnvEKX5iIIaXkxD-oeh2JjQD-Ps63uAWIaC9qZmujsinK0cE3jt1hJsK4apTnzBQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇱
اسرائیل کاتس، وزیر دفاع اسرائیل:
ما بسیار مشتاقیم که به تأسیسات انرژی ایران حمله کنیم.
ایالات متحده در حال حاضر با این کار موافقت نمی‌کند، زیرا نگران است که ایران به کشورهای همسایه حمله کرده و موجب بروز بحران جهانی نفت شود.
@News_Hut</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/news_hut/69112" target="_blank">📅 13:28 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69111">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">🚨
🇮🇱
کاتس، وزیر دفاع اسرائیل، به شبکه ۱۴:
جنگنده‌های آمریکایی برای انجام حملاتی در ایران از پایگاه‌هایی در اسرائیل به پرواز درمی‌آیند و ایران نیز از این موضوع آگاه است.
@News_Hut</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/news_hut/69111" target="_blank">📅 13:12 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69110">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">‼️
❌
آی‌24نیوز:
طی 48ساعت گذشته حدود ۲۰ پهپاد توسط شبه‌نظامیان مورد حمایت جمهوری اسلامی در عراق به سمت اسرائیل، اردن و عربستان سعودی شلیک شد.
@News_Hut</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/news_hut/69110" target="_blank">📅 12:39 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69109">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b2c6cefb08.mp4?token=EL3af6LH1MQ-YV6DlCQ71J-K0PygCZQ5kvGnYapDEX9wS4LD3ilEPrOMkvVohkVN13NaWSJKeKuIhQiydg-jnXCxwLpy_4NvjaHsotq9gX0l5bQkPFtKPnDIIY63g7udSQIwiVPxwe4UdwCX4s1UNpowpN4i3J90wNbhy15IKQy0se7EVF1uE6VY_tsPaooi5pq7jliw7QdjoRqUCXI73oaNNNT7WZrGmQKZyIQQ60dqaMWmPZplolifLatAv4lIbbPmMrO2_21aIklDjWaonzyBGpDsWEvEVF2VCgTlXV7ZqCcvKMZpL7qaij-OgtaJ05OQolMzjDJmawW50a0PPw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b2c6cefb08.mp4?token=EL3af6LH1MQ-YV6DlCQ71J-K0PygCZQ5kvGnYapDEX9wS4LD3ilEPrOMkvVohkVN13NaWSJKeKuIhQiydg-jnXCxwLpy_4NvjaHsotq9gX0l5bQkPFtKPnDIIY63g7udSQIwiVPxwe4UdwCX4s1UNpowpN4i3J90wNbhy15IKQy0se7EVF1uE6VY_tsPaooi5pq7jliw7QdjoRqUCXI73oaNNNT7WZrGmQKZyIQQ60dqaMWmPZplolifLatAv4lIbbPmMrO2_21aIklDjWaonzyBGpDsWEvEVF2VCgTlXV7ZqCcvKMZpL7qaij-OgtaJ05OQolMzjDJmawW50a0PPw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇺🇦
گویا زلنسکی هم در آمریکا حضور داره و قراره با ترامپ دیدار داشته باشه.
@News_Hut</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/news_hut/69109" target="_blank">📅 12:33 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69107">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RSKXfixdPdfbk5i_O0GyVU-5T7VCFSQsA6DvBBqiNGD39IecTWLgYg5ZERMMgGJdBVWTgoX87REh1SQXFOm346cVPDkbhGGW9p-8fI3AZHeCXy54ytRrSHIpkkABCM_Npn2wNAG1vqPXUY6EuRHNrtSg2fmASiPcsIZIm4zhNAFazd7P2MuoIa7iQFN75nRNxrWv5s5IBCSr5eN4NuZxFGCGThPDY1CkpJPh-kZ0QW1TukC600s0cxAE2FsIw4OTjkfi_l03TtDZQeZMCYONs-Z3TjEEPv4wFPg8t7aLFhcg1n4-bRT6egr3C24PKnKpkCfxYUyebS0dbdoMFjkvDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Pwq1AWS12VTaiz_uaHQUU-Nk8zNEps31Kl-OP6E5suYJlflBGquvMmzwvJ4-JhZFKsnVi9IiwgbXatG7P6HRf7N8K1hd8MJM6jybae2yRmvANjAGcUJkggWUtUaoCZ-OIZGu0dLzyyb7ztcyl6TYyix6XjugkbCH9OP8qKgcPU-e3RSld1U0QP9j1SVuaMBHhq_RBKEkfCmLtLkb_44CYTgejEfQUZ11aix0r2UJrJI6ulZTQXAp1uQ9T7zp2KFjPJ77QtcICmwkDvOXO2QsX55R1EK2_v6cwtF6RfcL2vo9kJQLRuJNWjNvk1q5bmvDXfU6Z5xp5uH_kOA4hCyGfg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
تو‌ جلدی که مجله اکونومیست از سال 2026 منتشر کرده بود؛
زلنسکی
🇺🇦
درحالی که دوربین دستشه، داره به یه کشتی ایرانی نگاه میکنه!
@News_Hut</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/news_hut/69107" target="_blank">📅 12:14 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69106">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1f0b26c19f.mp4?token=caKQiaUmb5vfGxQcskP4vzcmeG2XSYLjLCK04hjv2y29Uzpwm6JTi3B3AH8Aap_eY4lX3HNt4YvsSiw9s_PW4qlBi2TLGEZcFDPdDP_tau0er1Q-Eh7BRNVeyQIrxAh8riIGA5TSOI4QUfWvx7lLp3U1fe4u4H_VhZdPxlGhzWhPnbOWexx2EUdODatr0xAf_47Qetnc8aTXYevT9JIa2VL7tplQ7-MiFlj_NCN4Q9rFJKrE7zhWtqA4kFVMJZ4FM47XUenyl8MQlWuy0qAgNmrGa2xpQfW19dqz83HFMP0IiUC38cpXnpXWW6YMYfKbKVl9JVX59rxsFVJe85zbGQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1f0b26c19f.mp4?token=caKQiaUmb5vfGxQcskP4vzcmeG2XSYLjLCK04hjv2y29Uzpwm6JTi3B3AH8Aap_eY4lX3HNt4YvsSiw9s_PW4qlBi2TLGEZcFDPdDP_tau0er1Q-Eh7BRNVeyQIrxAh8riIGA5TSOI4QUfWvx7lLp3U1fe4u4H_VhZdPxlGhzWhPnbOWexx2EUdODatr0xAf_47Qetnc8aTXYevT9JIa2VL7tplQ7-MiFlj_NCN4Q9rFJKrE7zhWtqA4kFVMJZ4FM47XUenyl8MQlWuy0qAgNmrGa2xpQfW19dqz83HFMP0IiUC38cpXnpXWW6YMYfKbKVl9JVX59rxsFVJe85zbGQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇱
ساعاتی پیش بی‌بی‌نتانیاهو به واشنگتن رسید.
@News_Hut</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/news_hut/69106" target="_blank">📅 11:50 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69105">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e0eb0677cd.mp4?token=NZeI9DEaMOiYWw7gxG6J23elBWvVQym3sfRoJErBdwFyinHkJiEtzbEzxoFL9h-fuRgTDqnfqHJ8_m1_jpG0IpJQuP9yOvNtxdJ70IW6gMK--GULmHhM_tXPgzFkzdIZaIZ95qtaHRmiAsOr_-Q0p8rVFpPc3qi84npoW44anizBN0mKEpVC-UbHOg_DhDUHI0iTu4PNBs6Q4L2MiTcBKfs3yIvD_Eh3qX5wJKLaWUkSVrOlHgNA35Vykg7Wkb9NC2aNZMX3iXvcPal1z5Lb2wTcRh1R4P1J5HFX917eSoJ0HZud4LMJr1gSvlT1r_ZKkPVMQ3M0kmSSDjTGuTbkVzC-wTS88jwIVKmcTJBDwAU-OgFX22Yr24GjijZGdXAnSiLzBOJtDVjd0DrwZ5OflT6faB2wXuAcnP6urbOmhieDtIO_EY4RcLilnhzcCiHy57YJAnJXe3aMOAyUXtGca0oE3GdJLgEpWwaRY95souyVaGjds9S5C0EcHEQTLhwg2zan89yWBTML_fcj_tVUgG8AyT2_NMY6y1MOs0nUVZeXdeO0-rdkU7o5EFBhNf4xHFJuP-ox7zNKQsLzcJjFjmxFWnjQn6bL7FZWXFxmhVQuK7nHuOyTPHOckY1NGwSCexy-kr6K6w-51qgfxUn3kUUlBzlWlD5_fTxV7U4ACrk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e0eb0677cd.mp4?token=NZeI9DEaMOiYWw7gxG6J23elBWvVQym3sfRoJErBdwFyinHkJiEtzbEzxoFL9h-fuRgTDqnfqHJ8_m1_jpG0IpJQuP9yOvNtxdJ70IW6gMK--GULmHhM_tXPgzFkzdIZaIZ95qtaHRmiAsOr_-Q0p8rVFpPc3qi84npoW44anizBN0mKEpVC-UbHOg_DhDUHI0iTu4PNBs6Q4L2MiTcBKfs3yIvD_Eh3qX5wJKLaWUkSVrOlHgNA35Vykg7Wkb9NC2aNZMX3iXvcPal1z5Lb2wTcRh1R4P1J5HFX917eSoJ0HZud4LMJr1gSvlT1r_ZKkPVMQ3M0kmSSDjTGuTbkVzC-wTS88jwIVKmcTJBDwAU-OgFX22Yr24GjijZGdXAnSiLzBOJtDVjd0DrwZ5OflT6faB2wXuAcnP6urbOmhieDtIO_EY4RcLilnhzcCiHy57YJAnJXe3aMOAyUXtGca0oE3GdJLgEpWwaRY95souyVaGjds9S5C0EcHEQTLhwg2zan89yWBTML_fcj_tVUgG8AyT2_NMY6y1MOs0nUVZeXdeO0-rdkU7o5EFBhNf4xHFJuP-ox7zNKQsLzcJjFjmxFWnjQn6bL7FZWXFxmhVQuK7nHuOyTPHOckY1NGwSCexy-kr6K6w-51qgfxUn3kUUlBzlWlD5_fTxV7U4ACrk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تسنیم این فیلمو راجب
ملانیا زن ترامپ
منتشر کرده تا اگه کسی قصد ترورش رو داشت از این اطلاعات استفاده کنه
🙂
@News_Hut</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/69105" target="_blank">📅 11:15 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69104">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/76bcf42cd4.mp4?token=nPUhrXPfckz-vf3zt-gtGf2M42Kwfpe0O5o87D6lWSNfKbHB-gRDOxDtffQEEh_ThVfvJ6uqdxGHdTQ-vyKirW5h319Wd9pRm8_DDrsN6Q5XqLFI9FmzAoiNfO6NFGYyoMi1IQc96Ksj7IPfcxNA_iymFu11AVAWgqj1cvhW2LSEPKnL-0FIWMLrK-YiMQTk2InfdwIiJddZQ6lJA5ytMk02p8dKImL_Pmndj14Kf24PUM7Ff4hQGX7qrZ0Gr76VqReSjjSQ61nE_R1EPh6Om6p9YhXmEqAsnmjvqSBe2DwPW6GpJK39M8DssU-RMkrU19YJyFCkM6B8VNcj1_IbVg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/76bcf42cd4.mp4?token=nPUhrXPfckz-vf3zt-gtGf2M42Kwfpe0O5o87D6lWSNfKbHB-gRDOxDtffQEEh_ThVfvJ6uqdxGHdTQ-vyKirW5h319Wd9pRm8_DDrsN6Q5XqLFI9FmzAoiNfO6NFGYyoMi1IQc96Ksj7IPfcxNA_iymFu11AVAWgqj1cvhW2LSEPKnL-0FIWMLrK-YiMQTk2InfdwIiJddZQ6lJA5ytMk02p8dKImL_Pmndj14Kf24PUM7Ff4hQGX7qrZ0Gr76VqReSjjSQ61nE_R1EPh6Om6p9YhXmEqAsnmjvqSBe2DwPW6GpJK39M8DssU-RMkrU19YJyFCkM6B8VNcj1_IbVg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
مجری :
کراش فوتبالی تو دوران نوجوونی داشتی؟
⏺
غزاله اکرمی، بازیگر :
آره ، غلامرضا عنایتی
خیلی زیاد دوستش داشتم ، نمی‌دونم واقعا چرا به شدت روش کراش بودم!
@News_Hut</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/69104" target="_blank">📅 10:30 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69103">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vUV1bjPxGEc9pqIGg-5elzi4ghvuC9FDziNz_MTfWHN3qEe74xZNyCyFaNKzjo30XwRy8f4vxOUqC_T7eeQhJxdjFAi1BCV1yRVo4jwS4Eh2m_P5OIwDsobrF_Wv3IsGpwKZutPvNRNSKBZTPImopzi8XRnKaI21jfWnPIYJFVwvPxNUJdp69UXhFz3LmgA-R0QLbaxnRUKTJ7JJiSiKPU_ZbO21PMaGHjge86Zb-ZUGtLATN5BGenvwdWo9touG_YYTqvWWRTMGmAEYrQ-fDqCgztlQciMhIQd8yqrgkJTYxgjRiolydRvh4NjMYalCKWGwtqppEqro1_oC44fgdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به کشاورز زمین داد، چریک شد!
به زن‌ هویت داد، آنارشیست شد!
به کارگر سهام داد، کمونیست شد!
به هنرمند اعتبار داد، توده‌ای شد!
به مسلمان حرمت داد، تروریست شد!
به دانشجو بورسیه داد، مارکسیست شد!
به اقلیت حقوق برابر داد، جدایی‌طلب شد!
@News_Hut</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/69103" target="_blank">📅 10:04 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69102">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b88a652ec4.mp4?token=g6WXummbxzskFPSK935Yqr6tCHVedBxVdeM53MqQeoSFuOJFigbjqwBKyCUZYxMaRfWuGEmdNKpWXBVoDct1eDVX9jQRJ2JqnUlcQtzSpZMp_YJNjlclBs0i7m1fr955Hv_cBci0hh3xgVWvRK1OMxrBNqQFfAgYBwIUv1imTaCytRMZJfVhpucBrbaqjYGgccBZNli24rehVbU4vsqv4QXbZJMrDedGNfpQQlCHJJM8XbWTZsq3o4zeSzKjsCuT9Yg8pcQiOGNnFz3JBrkHH1aOXIFoCIHiN2vatNJ3ZeMD_u-rtz39wohzsyUt4YSZzT0Vv3a6l89f554LUwM63A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b88a652ec4.mp4?token=g6WXummbxzskFPSK935Yqr6tCHVedBxVdeM53MqQeoSFuOJFigbjqwBKyCUZYxMaRfWuGEmdNKpWXBVoDct1eDVX9jQRJ2JqnUlcQtzSpZMp_YJNjlclBs0i7m1fr955Hv_cBci0hh3xgVWvRK1OMxrBNqQFfAgYBwIUv1imTaCytRMZJfVhpucBrbaqjYGgccBZNli24rehVbU4vsqv4QXbZJMrDedGNfpQQlCHJJM8XbWTZsq3o4zeSzKjsCuT9Yg8pcQiOGNnFz3JBrkHH1aOXIFoCIHiN2vatNJ3ZeMD_u-rtz39wohzsyUt4YSZzT0Vv3a6l89f554LUwM63A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏸
ارزیابی رابرت پپ از سناریوی ورود نیروهای تفنگدار دریایی (Marines) به سواحل جنوبی برای تصرف محدود نقاط بنادر و عواقب آن.
@News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/69102" target="_blank">📅 09:15 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69099">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jdsbe81osTFb4pOrF4_Uo6icxw-Q09sFiWXlnPoajV_h0TDHeDQNoX5k8rZPDljX5bDu9Qy2--x0RoxUVlJULqhSzd54MhIJvcYKp2biD8L7n6XnvAEXpTKA--U3p8IgT2xRAFNO9pMEOUXPbmLjb42yJy1D_jG8AmzdO9TRxk6S4JH3yBC3ptHRjvnj1HKk-FZBoST-yVCC37fxCKefLxSumde51pChikq97NSTRkx7V2IEcC49bOswwRjskatp5LNEV_U8Uhh02wKywJ0Yl5xaY-yM3FQ10KVZ0fp235DRAhXCgaQahwf4Yf-mjtl_yrd-JZhwhBE8S1WVEUxFag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nuTsAa_5IKnvSpKWmhS3iYcWs6W8Nxk-Zm2IBu6rX6lPA0ElL-ra_APo9C44m75YTdxZUv_Lge1UwKVsCmshMSam7spnmdBlv4-jZw6YMI2qeFU5T-PfF1bI8bHniqC_HX4YprSbNn9RN3hxHd1KSNjS4wExIga36bwrDFIkWnfcGNrU5k65pkh4SSas3qtIDN_bMVa6oDkx1lvyYeJkGi-U-mpziCium9sLiqmy2Pzvk5oIrXG00giCQnDqxpR_v6OdcMSTFAb63ZQjXCVspRvLNNw8bo_iaqEGJ-qgTsqRrA0PJ-wa3FBUEimaBKJhIkUygCbNk4DaUA1pd-aNcQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">یادتان گرامی جانفدایان میهن
🖤
@News_Hut</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/69099" target="_blank">📅 05:56 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69098">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">#رسمی؛ جمهوری اسلامی دقایقی پیش، پس از اذان صبح، ابوالفضل سپاهی، علیرضا سپاهی و امیرحسین صفری را اعدام کرد.  @HutNewsPlus</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/69098" target="_blank">📅 05:56 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69097">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">#رسمی
؛ جمهوری اسلامی دقایقی پیش، پس از اذان صبح، ابوالفضل سپاهی، علیرضا سپاهی و امیرحسین صفری را اعدام کرد.
@HutNewsPlus</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/news_hut/69097" target="_blank">📅 05:17 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69096">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">متاسفم برا یه عده که ذره‌ای شعور ندارن و چند ساعته مدام در حال پخش انواع فیک نیوز هستند، بهتون کاپ طلا می‌دن که خبریو زودتر منتشر کنید؟!
#hjAly‌</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/69096" target="_blank">📅 05:10 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69095">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e9f40f91b5.mp4?token=ogt0YlaIZYKOiSgZnvcR5N8kChf2NkRD_4sCSGM5fh15APFfjByoGRp_1H8tmurXgG-crAwT_1KZftZcOpdw3KsnlhN4NsF7Y19nETOl7jfBD3ztLjIBlS59Jgn6vU250gbyQxqiElvtWENH2dVwsxNtsPX2XAnXRg2kJTqzZgmPUC-YH6yv6m2Md7IAF8swfYuHDkHlUSz9-2hhZWBbFUVg87VjBKQ7Q6DORCjzW28wCqiCO1UcPIjDUI-S-fd825_n31ershEB5ssv9jbA6Qic1Mq_NMc9AbB4tM3DphX8pi4_AQae4cwQicD9ow8htswBZ5bZLXyzn_GoA_UHzg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e9f40f91b5.mp4?token=ogt0YlaIZYKOiSgZnvcR5N8kChf2NkRD_4sCSGM5fh15APFfjByoGRp_1H8tmurXgG-crAwT_1KZftZcOpdw3KsnlhN4NsF7Y19nETOl7jfBD3ztLjIBlS59Jgn6vU250gbyQxqiElvtWENH2dVwsxNtsPX2XAnXRg2kJTqzZgmPUC-YH6yv6m2Md7IAF8swfYuHDkHlUSz9-2hhZWBbFUVg87VjBKQ7Q6DORCjzW28wCqiCO1UcPIjDUI-S-fd825_n31ershEB5ssv9jbA6Qic1Mq_NMc9AbB4tM3DphX8pi4_AQae4cwQicD9ow8htswBZ5bZLXyzn_GoA_UHzg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مردم دارن شعار سر میدن
@News_Hut</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/69095" target="_blank">📅 04:22 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69094">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">دفتر رضا پهلوی از جامعه جهانی خواسته هرچه زودتر برای جلوگیری از اعدام معترضان در اصفهان وارد عمل بشن!  @News_Hut</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/69094" target="_blank">📅 04:14 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69093">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">دفتر رضا پهلوی از جامعه جهانی خواسته هرچه زودتر برای جلوگیری از اعدام معترضان در اصفهان وارد عمل بشن!
@News_Hut</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/69093" target="_blank">📅 04:13 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69092">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">لحظه‌ی اذان صبح و آماده‌سازیِ شرایط اعدام، در میدان علیخانی اصفهان</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/69092" target="_blank">📅 04:06 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69091">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">باز می‌گن چرا مردم ایران دین‌زده شدن، شما یه نگا به کشورای عربی بندازین، مردم، حاکمانشون رو می‌پرستن، بعد این شیعه های مفتخورِ بی‌همه‌چیزِ خرافاتی، جوونای مملکت رو دارن تو ملا عام اعدام می‌کنند به بهانه ها و دروغ های مختلف، همونطور که ۱۴۰۰ ساله چیزی بجز دروغ…</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/69091" target="_blank">📅 03:29 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69090">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">باز می‌گن چرا مردم ایران دین‌زده شدن، شما یه نگا به کشورای عربی بندازین، مردم، حاکمانشون رو می‌پرستن، بعد این شیعه های مفتخورِ بی‌همه‌چیزِ خرافاتی، جوونای مملکت رو دارن تو ملا عام اعدام می‌کنند به بهانه ها و دروغ های مختلف، همونطور که ۱۴۰۰ ساله چیزی بجز دروغ و خرافات ندارن به مردم بگن
#hjAly‌</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/69090" target="_blank">📅 03:27 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69089">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/780d746559.mp4?token=o3cR4hdVHQ54pgK2L2_PGG1RJLnL8_LuivScw_I1LUR705mot7oKQFCQnvVJ7u2vl0IPnZ4wX--LC8rMAuGVS5_wStQYdaXQkNq9fc5eJJX2Dm_NcbmmciR3LwafM7_ngS6R_zwhFABqmghfJh7VahzxMbAjdDQUc78BZu1clZLd6IeLwnNfV45MBTkAOAL_DfnSmNiWJkl7sTsWy1AxzPnZNfnjyKRKquV3I400AfBm4l9uuFkX83syKm0akixmioq-eoE3qqrjnQNk7EjDyRWI_oSx3XXO7JdyfK1L6Q71lgSUokc3mHXUGWQ4q8-BMgKxT73orsMTtzu372gLnw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/780d746559.mp4?token=o3cR4hdVHQ54pgK2L2_PGG1RJLnL8_LuivScw_I1LUR705mot7oKQFCQnvVJ7u2vl0IPnZ4wX--LC8rMAuGVS5_wStQYdaXQkNq9fc5eJJX2Dm_NcbmmciR3LwafM7_ngS6R_zwhFABqmghfJh7VahzxMbAjdDQUc78BZu1clZLd6IeLwnNfV45MBTkAOAL_DfnSmNiWJkl7sTsWy1AxzPnZNfnjyKRKquV3I400AfBm4l9uuFkX83syKm0akixmioq-eoE3qqrjnQNk7EjDyRWI_oSx3XXO7JdyfK1L6Q71lgSUokc3mHXUGWQ4q8-BMgKxT73orsMTtzu372gLnw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">میدان علیخانی اصفهان
@News_Hut</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/news_hut/69089" target="_blank">📅 02:40 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69084">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vP7W83P0rLh3OmMV-YtY_G7tVNsPmq3N8du51W4GJJ_NziiQzhejhvmJxI0gy1xGzy-1vEykh1kINnpxKVx3sv9admR-FTaTP8ZaR_fySuuPjweSnza-37Av6B236aXIo2s7GzugAXw8fLw71EoaMPDku0Nvah4he9sWINPNXpCYGVBZcMSUNVYHKfI2LHpmRTcjDJiCcW-1J6WebssZGcwXKqRXXWfXE-PsUor8nWvS35YakqNzOhigsGYKpVrlQkg_5v4_Drc37ouillcCmkKP8_vZC5kvYOc3IqpvWgrLbeLF329jAphgcIvlOLes-jn2hcx3ib7Pgn1_axiXmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IEIu2Bx_W_7Y_Nfo72BYgFWS5rtMrNiY9E4wYT2T_ik3EPTt7eyxjPnaTZCc6TrepRO1ByWwbABcX-AoWgdeftAMv9qdLjMrmZG9nlT8InQm-vFPJNVsWbJ3DP-1y152y0395iaoJw2IkPGPcA2WHxrcEGxSA78KxiP9OaQtnrotpAJ6mPsDMgjJWBPehd4jqBRMWdcKVTplTmu3uH9s-oSpmVA06cQ-tx9ms8eMPDCaBvIOLiBbjYA_ErGarE-B0I1BhRwDGckkfa7a29nMWZAI_w2abQ8YClsZ8NRovsdZ5tIUnORCuasdLx4VkNYzM1J8zqiFMufB2oO7gWez3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/njwvBd1iyTfiUsNFckye0pYanyN_2u5hnGBlJhaCRp0dp5Sqmko5vV_3quYWfevKyQyGqnyPHXTe3Tm5Kv1nSq6GRB91jPOWJEeWPCny20BCBMWI3JW3ySACGuK-YnEI9LlMI-8e6oHEx0Z9EaDWosjOaphPwuRNeJGgddzLJ3Lti9W-zPI3gbUbWgsvuDBLBG6JeQ0pwJsiWEfFdR0hqiQLfV2e86PuUE6ozUBgh632yRMP0dFyHqrH9QcOBikfHa5COsjJ45DRbPp0syJsSk2VFt5ifFkQPMwdsmrNZ62Oa87dPuV-nkO9yQJfUeHfEYhgQs4yvJNGqNu0yaDe5A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/491b6de7b5.mp4?token=vh8KfWMzpOGfGoBCBpn1dcX2TaX196iCplPi1cqEVJmKXIxvBFilciVgPLUKY245tkiMNv1pI4C4c7WVl6ZyUiyBbPLSUFa2u-NC9FuFVJLwldXaZIWKakh4IAj3c_BvuWRGIZaNVlQ36pmWlNUUxv39lrjOCiiAt9JVJkK7AXHg1CAnsR6s1iYkSl4UYihbd3hhOjti70Ss31NYYbC9p5R6T3HsaIsvusOrC-avE0S6IyE_SCJ-Pah9Z9MxQRAAM8vm5GnhOGp3SF8cYYWQpfVXnJnT3Wco4WxZEYcKkmZxD7yr_wKtJpyr1XXXoVTFx7fdw1dvPiYKqzmJB9H-ow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/491b6de7b5.mp4?token=vh8KfWMzpOGfGoBCBpn1dcX2TaX196iCplPi1cqEVJmKXIxvBFilciVgPLUKY245tkiMNv1pI4C4c7WVl6ZyUiyBbPLSUFa2u-NC9FuFVJLwldXaZIWKakh4IAj3c_BvuWRGIZaNVlQ36pmWlNUUxv39lrjOCiiAt9JVJkK7AXHg1CAnsR6s1iYkSl4UYihbd3hhOjti70Ss31NYYbC9p5R6T3HsaIsvusOrC-avE0S6IyE_SCJ-Pah9Z9MxQRAAM8vm5GnhOGp3SF8cYYWQpfVXnJnT3Wco4WxZEYcKkmZxD7yr_wKtJpyr1XXXoVTFx7fdw1dvPiYKqzmJB9H-ow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بامداد سه‌شنبه؛ تصاویر از وضعیت میدان علیخانی اصفهان
@News_Hut</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/69084" target="_blank">📅 02:05 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69083">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b7f398a76c.mp4?token=lVptaHJR6ed32VEGqGEHL7I6mZxL1OasqXsk4Nrx3kYkRKGPR19NabJVbPK2-BGDY8ouHZqU0KBUmeSYQ_GveElQpHvLfN6OTAmioLtkE7ybkRXlV30j8g2wzz8Kgqu78W9hGG7pL8Sy6MPW7Q1Iq1cARToKBvRXj3JlHt1VJzp2JUZZOX8nzF2qfAYQkIFM5PojcMSS2naF0l3PaqI9QvAottqrj2Fv9ViC82sj-v4OkGMB1YOTcQMQb8e7y7KoD988dDK07jSuT-cV46mO0NHUUsTSgbsRt6XmOXJDJbQweD4vKM-7Gx78wgwdTF0E-i7g_w7aVSaqMUllJA31WQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b7f398a76c.mp4?token=lVptaHJR6ed32VEGqGEHL7I6mZxL1OasqXsk4Nrx3kYkRKGPR19NabJVbPK2-BGDY8ouHZqU0KBUmeSYQ_GveElQpHvLfN6OTAmioLtkE7ybkRXlV30j8g2wzz8Kgqu78W9hGG7pL8Sy6MPW7Q1Iq1cARToKBvRXj3JlHt1VJzp2JUZZOX8nzF2qfAYQkIFM5PojcMSS2naF0l3PaqI9QvAottqrj2Fv9ViC82sj-v4OkGMB1YOTcQMQb8e7y7KoD988dDK07jSuT-cV46mO0NHUUsTSgbsRt6XmOXJDJbQweD4vKM-7Gx78wgwdTF0E-i7g_w7aVSaqMUllJA31WQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">داربست رو نصب کردن و جرثقیل هم آوردن و متاسفانه با اذان صبح، این جوونا اعدام میشن
🖤
طبق گزارش شما مردم وقتی میرن میدون علیخانی و می بینن مامورا اسلحه دارن، جرعت نمی کنن کاری کنن و فقط نگاه میکنن.
@News_Hut</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/news_hut/69083" target="_blank">📅 01:32 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69082">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/316f36114d.mp4?token=ObWKNubyI9ywLc7p3M9ZwdNMjh2I53Q_cc2PkunWRG1O0O4OoFZBcebOF72DTSc3Ga3t-wgBlEwQ2eFgs54WqNiRLwFVVhSnH_WVn9YPnYRRwPqFFLEAjiWfbFfIS9z-8cVgxoRPX9oxgyY0JhFyGWH1ckyKkkZluwfmlY3CDamO-cenD8bbNY-GsYK9Aka1Pyey3KKeays6FkT3VfvGtnyMHbosfrjkKfxLc2Pe3OUCmyD1F-xruKs42NuMRJBSvrI1Pl7i2PIvbL-ZFRE1JQxHVRX7V8cerJn-mB0t9T-in9fg4fR9Ile36K8vgEb-4ezHhwdcziVVSBe3VKpiIg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/316f36114d.mp4?token=ObWKNubyI9ywLc7p3M9ZwdNMjh2I53Q_cc2PkunWRG1O0O4OoFZBcebOF72DTSc3Ga3t-wgBlEwQ2eFgs54WqNiRLwFVVhSnH_WVn9YPnYRRwPqFFLEAjiWfbFfIS9z-8cVgxoRPX9oxgyY0JhFyGWH1ckyKkkZluwfmlY3CDamO-cenD8bbNY-GsYK9Aka1Pyey3KKeays6FkT3VfvGtnyMHbosfrjkKfxLc2Pe3OUCmyD1F-xruKs42NuMRJBSvrI1Pl7i2PIvbL-ZFRE1JQxHVRX7V8cerJn-mB0t9T-in9fg4fR9Ile36K8vgEb-4ezHhwdcziVVSBe3VKpiIg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">از آمار تا پیش‌بینی
https://t.me/+L5I8ulM6jEc2YmE0</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/69082" target="_blank">📅 01:32 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69081">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rRvEW5dtBZ_QdHXQUSucjPRWBKqM4RhMn4rWbenvPsug65564QZTm3vfZVJdqmigBMk85edQS0yzHR6zW82zMRgb2t4_mt0MXfUTVwa0E5dbl3MXlYh4PNEseRXSBGXFx-JTKt3p6hQV14CyAbmJ5zJWFJbdy6eoqmLPS4MiboBBCg_Fit7QHk4KvaW5WfxbhvvEOykgebzjLfnWKsT5lYPkDDJSIL4aMWckQ6QF1m0RWrzwne5L5DmPHz0e1ygGhcFW9kqDQSKHrSka0XKWAjrLu4nlA8D67kJe0MfuuF5cQy76x6nPY8Lx_M5SggP-gDbSvSYUJp09G8YHjJ89DQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بنر نصب شده توی میدان علیخانی اصفهان:
«هیچ جرمی از نگاه قانون پنهان نمیمونه، دیر یا زود عدالت اجرا میشه»
@News_Hut</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/69081" target="_blank">📅 01:20 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69079">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/awxweG_TJmES5OI3G7okuQE5NOX6kmkt5ziE9GF41QfsaRlfzHEZj4BvuPZl8ZPwy5exCBPQREEkAD_c5svL_gKwSWF9JqcrmCZOcwcTwXbOA5zT-b1nhHr1PjLNVa0MtWj25d1fJpIBpYkzAapSPpjWnJuAGXbSjdUc8UJ9UIsNWAJ5wcMw1gL4D2WWuE4VonuEJCJPjGS_a9cFlX4w7R2iqNBbYbFxZl5Tq-EdbPPNfmyD3VI4MNJSjJgYCLMGBTtnYazEzTYCcwviO8UKN3x3F19cfc4Guo6NnWpKDyPvyGPNa1uQB1wS0e4E5k2La3egnXDc8Gvc_UL-Dfsspw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/S7LZ-dVbhIYEpOdA-3WYFESOk7bQ3c-jMTNGNCIx5EsKgyNLifgrBbLMhmsxXNctqsbnxd22tOndjgFfBu3NlUpsY0s-5GEOJTiev6-VSYuBal6iLX-Xv68I68eX1x5--TQdd8icH20gePSptLQ8GQMhDwfRXqSy6aRcW_tNjumpP30E-4nAfYosmb9fAOpQ0JOpb6Y07M0TLp1PrAZRUUkr63ua6KO3zUwA3GVxgkHO7PWbU2Hff_jf7BoHgur7BPhptQKL1a6HkL7rrsaQwr0KlSD_7A7Ta-2Oh_EwSFfbceObU3KNVylkXiD_DRgc_LFR22bB6OEJTjeYJEvOSg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">طبق گزارش ها
توی میدان علیخانی اصفهان داربست نصب کردن و جو به شدت امنیتی شده؛
طبق گزارشات ابوالفضل سپاهی، علیرضا سپاهی و امیرحسین صفری از معترضان دی‌ماه و پرونده میدان علیخانی اصفهان به انفرادی منتقل شدن و قراره توی ملاعام اعدام بشن!
طبق گزارش ها این سه عزیز آخرین دیدارشون رو با خونواده هاشون داشتن
🖤
@News_Hut</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/news_hut/69079" target="_blank">📅 01:05 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69078">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3738c7aef1.mp4?token=XvzpAeDisSguHmu2c8rLXCblGTAr4Ub-VCbeoBsapIbyUojs88ENLKZj-veRbJtHir_z0Lv8ALDIDGfz_74At3iHt_-OrgejEdQr2Tndz5YNNu41zMx9LvmmJSvfsQDCuD4lqDuxnAhNSRwmx1ZiXZ-NLfXDN50CZ-kGkzrUEEUskFib-WINyzXlJwQjJ_U-VE0yCSzXQuIRzSC2jwb6NMQnaO2tOZgJNuHCoQ4K8OUxZeXqPenQhwelilVoknhf6riOAd40Y59BLWxIWxnUE52je-Xe_R-fonhiWGOJnMOyl38kgNWhcdya3pKntEJFP7k0eoWhOw1KRpwoQDP1OA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3738c7aef1.mp4?token=XvzpAeDisSguHmu2c8rLXCblGTAr4Ub-VCbeoBsapIbyUojs88ENLKZj-veRbJtHir_z0Lv8ALDIDGfz_74At3iHt_-OrgejEdQr2Tndz5YNNu41zMx9LvmmJSvfsQDCuD4lqDuxnAhNSRwmx1ZiXZ-NLfXDN50CZ-kGkzrUEEUskFib-WINyzXlJwQjJ_U-VE0yCSzXQuIRzSC2jwb6NMQnaO2tOZgJNuHCoQ4K8OUxZeXqPenQhwelilVoknhf6riOAd40Y59BLWxIWxnUE52je-Xe_R-fonhiWGOJnMOyl38kgNWhcdya3pKntEJFP7k0eoWhOw1KRpwoQDP1OA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
پرزیدنت ترامپ:
همان اتفاقی که در ونزوئلا رخ داد، در ایران هم در حال وقوع است.
مردم فقط آن را نمی‌بینند.
نمی‌توانی به آن‌ها رشوه بدهی؛ باید شکستشان بدهی. و ما داریم حسابی آن‌ها را درهم می‌کوبیم.
مذاکرات دوستانه‌ای در جریان است. ایران می‌گوید: «خواهش می‌کنم، خواهش می‌کنم، محاصره‌ای در کار نباشد.»
سوخت برای مدتی پایین آمد. بعد، آن‌ها درست رفتار نکردند و من مجبور شدم برگردم. حالا دوباره دارند درست رفتار می‌کنند.
هرگاه کسی جلو آمد و پرسید: «چرا داریم این کار را می‌کنیم؟» فقط بگویید: «چون نمی‌توانیم اجازه دهیم ایران به سلاح هسته‌ای دست یابد.» خیلی ساده است. همین و بس؛ دیگر نیازی نیست چیزی بگویید.
@News_Hut</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/news_hut/69078" target="_blank">📅 00:01 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69076">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oAeB92iH8pnNMEilgSkLiLWAAnymjrDeKtijLdUQe_cMNX3ab51TnZxf0CBWQqSUiXwsJI2AOPxI6DBmEX-pF9YhQVRw-ZPdrkpofZZfUO4q_mLaAsd2d2BA07TIRNJVROzIs3Y5GcXUbXbmZqhyreSJHwDn2xAeR3O7yEfGGzwC1n0-5CIhyIiuitleekDpXUI7ZO8OO8ilbed5eKAnV0uoHuAWUiFWVvOnZzCGhnKSypfSb1n6mmuN7w9MrGTDcK9D5-kXmBVqkg0ATjZ5imDU_lz-uaoNq3KMdYLWLRY2_SZSOvhhTOBEWfE5AmH0HEdHRsEnWsqKTasINs9npQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
کانال 12 اسرائیل: دونالد ترامپ، رئیس‌جمهور آمریکا، روز دوشنبه در مصاحبه‌ای با شبکه ۱۲ اعلام کرد که تصمیم گرفته است حملات آمریکا علیه ایران را به تعویق بیندازد تا فرصتی دوباره برای مذاکره فراهم شود؛ با این حال تأکید کرد که در صورت شکست تلاش‌های دیپلماتیک، ممکن است دستور انجام اقدام نظامی شدیدتری را صادر کند.
- ترامپ در این مصاحبه گفت که ایالات متحده در حال انجام «مذاکراتی بسیار عمیق با ایران» است.
- ترامپ افزود: «اگر این مذاکرات به نتیجه نرسد، ما به اقدام نظامی قاطع بازخواهیم گشت.»
- رئیس‌جمهور توضیح داد که با درخواست میانجی‌هایی که از او خواسته بودند فرصتی برای مذاکره قائل شود، موافقت کرده است.
- وقتی از او پرسیده شد که تا چه مدت حاضر است به تلاش‌های دیپلماتیک فرصت دهد، پاسخ داد: «مدت زیادی نه. یا کارها سریع پیش می‌رود، یا اصلاً اتفاقی نخواهد افتاد.»
- ترامپ گفت که روز جمعه تصمیم به تعویق حملات گرفته است، زیرا کشورهایی که میان ایالات متحده و ایران قرار دارند و همچنین سایر کشورهای خاورمیانه، از او خواسته بودند فرصت دیگری برای مذاکره بدهد. (این کشورها و افراد شامل عمان، قطر، پاکستان، مصر و همچنین نمایندگان ترامپ، استیو ویتکاف و جرد کوشنر بودند.)
@News_Hut</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/news_hut/69076" target="_blank">📅 23:35 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69075">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🚨
قرارگاه مرکزی خاتم‌الانبیا:
آمریکا در تداوم شرارت و ناامنی در منطقه و به دنبال اجرای محاصره غیرقانونی دریایی ایران، طی سه روز گذشته اقدام به تهدید شناورها و کشتی های تجاری و نفتکش ایران در آب های ساحلی و سرزمینی کشور ما نموده است.
هشدار می‌دهیم این اقدام آمریکا به منزله توسعه جنگ در منطقه تلقی می گردد و همانطور که نیروهای مسلح جمهوری اسلامی ایران در میدان عمل ثابت نمودند هرگونه تهدید و شرارت ارتش تروریست آن کشور را بی پاسخ نمی گذارند و با آن برخورد خواهند نمود.
@News_Hut</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/69075" target="_blank">📅 22:43 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69074">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b46871a0cc.mp4?token=oXHay1CO5JmMd-AE1B-Pkm8uXrHerrRppVygFRRKDBCNBq8cWBDG_ZLsEvdMU44qJnkovy4YFuqxwYinBDYR13GrIHsRmMbviCCDmaTiZXastVje06O-dW3DpuHbnVL49PunGfw3yhMrjPq9XBzCXd0g-_Fb_KLZvuI1aMetWIGYFSJ9iIIjlZ9t80Yv_XhMP_LV1wE0iXdmpclm5-5XFT9tYYBZkmnrWtab9kwKvqq_YSVbJaL4l97nP3f5qUJ2y6VggJEdu5tps6IZba2WWjF7Ts3QbQKEAlgg41rFVUFXXoQBNu9mhboF7wILKbPis5ZfSkBBUeNSzSQlnrLkmIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b46871a0cc.mp4?token=oXHay1CO5JmMd-AE1B-Pkm8uXrHerrRppVygFRRKDBCNBq8cWBDG_ZLsEvdMU44qJnkovy4YFuqxwYinBDYR13GrIHsRmMbviCCDmaTiZXastVje06O-dW3DpuHbnVL49PunGfw3yhMrjPq9XBzCXd0g-_Fb_KLZvuI1aMetWIGYFSJ9iIIjlZ9t80Yv_XhMP_LV1wE0iXdmpclm5-5XFT9tYYBZkmnrWtab9kwKvqq_YSVbJaL4l97nP3f5qUJ2y6VggJEdu5tps6IZba2WWjF7Ts3QbQKEAlgg41rFVUFXXoQBNu9mhboF7wILKbPis5ZfSkBBUeNSzSQlnrLkmIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
زنده یاد مانوک خدابخشیان:
هر کس رفت سراغ s400 روسی, یعنی کارش تمومه!
@News_Hut</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/news_hut/69074" target="_blank">📅 22:30 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69073">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from𝗔𝗱𝗺𝗶𝗻 VPN</strong></div>
<div class="tg-text">💎
فرم نتیجه دقیق رایگان با ضرایب بالا
💎
بهشت سنگین زنا و افراد کم موجودی
👍
https://t.me/+LVbtmWdHFTdmN2Rk</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/69073" target="_blank">📅 22:23 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69072">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from𝗔𝗱𝗺𝗶𝗻 VPN</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m8TUZMHQY0dY862-ypUCC1yfpBZTZn3Nbj-l8Y7qoM9qJ3W0Lx1L_UfQD3qj0yXR071wcrZhCvHwWR4nuz4qNMKaF7qPZA7kpz4qytA96XE9PkF-VEtVUX8m4kqYUuDiITx7JXpdiaMCQvMtSLqVwXTeqKmUPZRUhZaoGeAkrrJ4TQrk-Mux1GCsx9azDOrFchzipAnFuDlWlQ09bI3bjE4tq5WefcDlw68Oh9qxumnGJA5HFxXVDilThtpiGdpyoL7xUZJMuyZlsxiM8GySWYWAX21IbDCl13pnr_n8fp1hWWMZvOWazZMQFTnVtH2FbOX2vV1K6s_sh8SqGslUMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💎
فرم نتیجه دقیق رایگان با ضرایب بالا
💎
بهشت سنگین زنا و افراد کم موجودی
👍
https://t.me/+LVbtmWdHFTdmN2Rk</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/69072" target="_blank">📅 22:23 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69069">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d4dc96cd73.mp4?token=WdPcj9S9zRxukJoi6bKp5JkS6UM-e0Dr0JuLUvF6P6-dU3Q27mxrhElkX2nTdNx07jdIVLFKCzCELk1XN6BBVQ9HlogE1STv1Zdf1cgakdNNvaA8ayzriBekvs1LTfGaJ0kSQ6t3n09Jj954lJdj4igZy0UhuRB9WBVfm1gajsdDUSWPoVrae_9kczXvQ48HTLFPHhYuR-HbuTvvvJj9CXWBWgSfU1e3RjfjrwOTgYDCaS5I_GKEPgziCBhmTxSgF7PLAAtN5z98uQ7_AmuWJypzPPGpylyk4ofjQQUCsXOA1vSbMZNpBbOsiCIKp0QMcMopDhZyfUgOkyOoUFgnPQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d4dc96cd73.mp4?token=WdPcj9S9zRxukJoi6bKp5JkS6UM-e0Dr0JuLUvF6P6-dU3Q27mxrhElkX2nTdNx07jdIVLFKCzCELk1XN6BBVQ9HlogE1STv1Zdf1cgakdNNvaA8ayzriBekvs1LTfGaJ0kSQ6t3n09Jj954lJdj4igZy0UhuRB9WBVfm1gajsdDUSWPoVrae_9kczXvQ48HTLFPHhYuR-HbuTvvvJj9CXWBWgSfU1e3RjfjrwOTgYDCaS5I_GKEPgziCBhmTxSgF7PLAAtN5z98uQ7_AmuWJypzPPGpylyk4ofjQQUCsXOA1vSbMZNpBbOsiCIKp0QMcMopDhZyfUgOkyOoUFgnPQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⏺
حسن روحانی درباره اعتراضات دانشجویی تیر ۱۳۸۲ (17خرداد 1392):
آقای قالیباف من دلم خیلی نمی‌خواست بگم، ولی شما من رو ناچار کردی. شما می‌گفتی دانشجوها بیان تا ما گازانبری برنامه داریم تا تمام کنیم.
ما می‌گفتیم راه این نیست که ما مجوز بدیم بعد بیاییم گازانبری این‌ها را دستگیر کنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/69069" target="_blank">📅 22:01 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69068">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1ab4cc3c2d.mp4?token=qT0rkXMXMGzoDjKC9-88HuVAvq4eO6JmV2Zb3X2Cg5y6UfL2ZPoSa9L-1Ddx8PvsjOOq_1kWklHwvC8Y3I40Qz4bAC2b1zy5NWGrQj0RB-ffi1heemEyyLlomDjC2qYlTzvTQcWHbMU9LX14xwXnYA2mvfG4zzd6mk-vhd_ToG7VCaIkYhuHAbZcUSAcyWN_AqQPy0MofNmZLucQYvZ1yG5WFLtKzi4TtOae38WnLN64Cyac3d8IOfvABt6NLon8Jqd1YhE0TiiHdlNTZT-gUuxW7Mxp-JiVxeGPqr0PVZQgBPEPoRfYy2dgdWycNdo68JH7puGF3tgaQ-xersTK_VKPEvZ37VAU20J1uvv8U1vF_lVzUGd5HCeWWfiuBNn8FjmlEChvGG4K2UvVY1N7Dcy3KdjCUohrYHT2OIO1A02IOPuKpeSj1gflRlGSjiyPB8I_E6-GzkES40A5vbXONTXrrtDGLFSxWCf3XfYsR7fZ0k3JirH6oRjImGK9iScW0WQBK9KH5tVO6zxNCSuS1Bmqz6FizTD_oKX-b5FpdSVnzrAU2Ulw_kDU0jgcK1a4dlBNuMI8NHPPR6wbKEpIfLyAMU-XH1HGjvogMJgVsqRJ3p2RQveRR_Nv8HysssCVYhjrUDQ7Qs-gBlNbhsR-zaSQhw9yKm9sKo_GUaNdSPs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1ab4cc3c2d.mp4?token=qT0rkXMXMGzoDjKC9-88HuVAvq4eO6JmV2Zb3X2Cg5y6UfL2ZPoSa9L-1Ddx8PvsjOOq_1kWklHwvC8Y3I40Qz4bAC2b1zy5NWGrQj0RB-ffi1heemEyyLlomDjC2qYlTzvTQcWHbMU9LX14xwXnYA2mvfG4zzd6mk-vhd_ToG7VCaIkYhuHAbZcUSAcyWN_AqQPy0MofNmZLucQYvZ1yG5WFLtKzi4TtOae38WnLN64Cyac3d8IOfvABt6NLon8Jqd1YhE0TiiHdlNTZT-gUuxW7Mxp-JiVxeGPqr0PVZQgBPEPoRfYy2dgdWycNdo68JH7puGF3tgaQ-xersTK_VKPEvZ37VAU20J1uvv8U1vF_lVzUGd5HCeWWfiuBNn8FjmlEChvGG4K2UvVY1N7Dcy3KdjCUohrYHT2OIO1A02IOPuKpeSj1gflRlGSjiyPB8I_E6-GzkES40A5vbXONTXrrtDGLFSxWCf3XfYsR7fZ0k3JirH6oRjImGK9iScW0WQBK9KH5tVO6zxNCSuS1Bmqz6FizTD_oKX-b5FpdSVnzrAU2Ulw_kDU0jgcK1a4dlBNuMI8NHPPR6wbKEpIfLyAMU-XH1HGjvogMJgVsqRJ3p2RQveRR_Nv8HysssCVYhjrUDQ7Qs-gBlNbhsR-zaSQhw9yKm9sKo_GUaNdSPs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❓
توضیحاتی درباره کوه کلنگ و چگونگی نفوذ به تاسیسات آن.
@News_Hut</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/69068" target="_blank">📅 21:15 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69067">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3cf7ba0e57.mp4?token=DrbfLfVe_vA70XsMiRGXH9NWKqgJa9Qc_887QKeppQ1iP1BWLYdaxecZAZ7Oi7t_5WmoMY5SbZ1Ns-9Gbxhu7ccNiiGRtBUlKUD3l3_cyv79lRlDcGnV4uNoiNNcylqUWXZNv8Qx86t8n499WxPVMHhvi5PCc6Xu4IJn-3qnOaAXXXKKdJ1Pn6J42rPL29CuCFYArG3S1CppT3E1qLvNmF0fJgvPsUJPjFY8jOA-E4AFeSpS9bKjWY6_Wi3xxZOJfPKDyY-g9BUAIl8oHBVUeBx3wB2P6Wx9KpPmxd7w0tqOAJpnEbMLzvuEJv853kVGFAfz6xPDdzw78YG2dGdogw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3cf7ba0e57.mp4?token=DrbfLfVe_vA70XsMiRGXH9NWKqgJa9Qc_887QKeppQ1iP1BWLYdaxecZAZ7Oi7t_5WmoMY5SbZ1Ns-9Gbxhu7ccNiiGRtBUlKUD3l3_cyv79lRlDcGnV4uNoiNNcylqUWXZNv8Qx86t8n499WxPVMHhvi5PCc6Xu4IJn-3qnOaAXXXKKdJ1Pn6J42rPL29CuCFYArG3S1CppT3E1qLvNmF0fJgvPsUJPjFY8jOA-E4AFeSpS9bKjWY6_Wi3xxZOJfPKDyY-g9BUAIl8oHBVUeBx3wB2P6Wx9KpPmxd7w0tqOAJpnEbMLzvuEJv853kVGFAfz6xPDdzw78YG2dGdogw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
خبرنگار:
آیا نتانیاهو می‌خواهد که شما با ایران به توافق برسید، یا می‌خواهد به حملات خود ادامه دهید؟
🇺🇸
رئیس‌جمهور ترامپ:
«بی‌بی» عالی بوده است. [قدرت] ایران به ۸ درصدِ آنچه چهار ماه پیش بود، رسیده است.
@News_Hut</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/69067" target="_blank">📅 20:46 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69066">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/73754cc159.mp4?token=bNFS3KbUqr2QqPzLvr-p7eJ2MEwQxulkEL-H-f3ri29E2ztWIdzK7uFcWheQM0za00MN6zhm2fjZmTCG-6MBFBQ8BW2sn2g9kGkPbS0SxoIh4Qwz0dvni9ifqpMhQZfTzZ3BIrS2-FeMK8dLmOPGnpDgYTGzXkzLCQHOG-WhEe0oCsUDkrAxIWUyragYsqNCRnGJYClZUFLkOcZgSV6zPVHHowoJ08cRNLMZUIGALjRPVfdWoFJmI1XJx0nWoXHVTTUpHVwfuOirQsEngswDDcKpoXabF_KcBeDmJ1J3T6QWNF8Gs52DSjAhuXPlsVgpgWXIb5NmHIk8ASiYTYqpqg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/73754cc159.mp4?token=bNFS3KbUqr2QqPzLvr-p7eJ2MEwQxulkEL-H-f3ri29E2ztWIdzK7uFcWheQM0za00MN6zhm2fjZmTCG-6MBFBQ8BW2sn2g9kGkPbS0SxoIh4Qwz0dvni9ifqpMhQZfTzZ3BIrS2-FeMK8dLmOPGnpDgYTGzXkzLCQHOG-WhEe0oCsUDkrAxIWUyragYsqNCRnGJYClZUFLkOcZgSV6zPVHHowoJ08cRNLMZUIGALjRPVfdWoFJmI1XJx0nWoXHVTTUpHVwfuOirQsEngswDDcKpoXabF_KcBeDmJ1J3T6QWNF8Gs52DSjAhuXPlsVgpgWXIb5NmHIk8ASiYTYqpqg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
خبرنگار:
درباره جنگ با ایران، از توصیه‌هایی که هگست در ابتدای کار به شما داد و نتیجه‌ای که داشت، ناامید شدید؟
🇺🇸
ترامپ:
نه، اون کارش رو عالی انجام داده.
ما ارتش ایران رو نابود کردیم.
اونا می‌خوان مذاکره کنن و ما هم داریم مذاکره می‌کنیم.
این احتمال وجود داره که به توافق برسیم.
اگه اون کاری که ما انجام دادیم نبود،
الان اصلاً حاضر نمی‌شدن با ما حرف بزنن.
هم از طریق واسطه‌ها و هم مستقیم،
خودشون درخواست دیدار دادن.
الان هم داریم مذاکره می‌کنیم و امیدوارم اتفاقات خوبی بیفته.
امروز قیمت نفت هم حسابی افت کرد.
مذاکرات خوب پیش میره و
احتمال زیادی هست که نتیجه مثبتی داشته باشه.
اما اگه توافقی حاصل نشه،
برمی‌گردیم به همون کاری که دو روز پیش انجام می‌دادیم.
🎙
خبرنگار:
شما و نتانیاهو درباره ایران هم‌نظر هستید؟
🇺🇸
ترامپ:
یه اختلاف‌نظر کوچیک بینمون هست،
ولی در کل تقریباً هم‌نظر هستیم.
ایران توی 14 روز گذشته ضربه سنگینی خورده.
اونا خیلی محترمانه از ما خواستن که
«لطفاً حملات رو متوقف کنید، بیاید مذاکره کنیم.»
الان دقیقاً توی همین مرحله هستیم؛ باید ببینیم آخرش چی میشه.
@News_Hut</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/69066" target="_blank">📅 20:22 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69065">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BDPLEtqOuuemfRzLQJfNtEAvJD8f9R5nMomUm8cbsuWdu4-oj-4ZCDGP-rEnHWT4JKVNvpvRZ6UjLfQxAOywb7scAFXV-18QZVAmoRQtbe9e8qB2eSHZZiO9EHJPevgCXlZdbc_LGa5fW_d7hrJVcgJCIVSuZToSYb0-QVYSK13yC-1CDmnAcpLJCvL36-ErLtfAu4zRI8vnpIflg1iTpq5gwfbVJ995V0q3xZV849F_kQUWM-M5VjPvupDOWSsbYMRQlVul25DG7wjO14nZCBibmuSgx_nilnB1wisZuouAObUm-1IPVM20U8gO1FIDHG2jP7T5k5QCNrgtrU89Jg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇺🇦
وزیر امور خارجه اوکراین:
تهدیدهای ایران غیرموجه و بی‌اساس است. رژیم تهران شریک مستقیم تجاوز روسیه به اوکراین است و با تأمین تسلیحاتی که از سال ۲۰۲۲ تاکنون موجب مرگ اوکراینی‌ها شده، به جنگ جنایتکارانه مسکو دامن می‌زند.
ایران هیچ جایگاهی برای وانمود کردن به اینکه قربانی است ندارد، چه رسد به اینکه بخواهد تهدیدهای خود را با استنادهای مضحک به منشور سازمان ملل توجیه کند.
ایران همچنین با این اظهارات تلاش می‌کند تا توجه‌ها را از اقدامات تروریستی روسیه علیه کشتی‌های غیرنظامی در دریای سیاه — که امنیت غذایی جهانی را تهدید می‌کند — منحرف سازد؛ اما در این کار موفق نخواهد شد.
حملات روسیه به آزادی کشتیرانی در کانون توجه نشست اضطراری امروز شورای امنیت سازمان ملل قرار خواهد داشت و ما انتظار واکنش‌های قاطع جامعه جهانی را داریم.
@News_Hut</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/69065" target="_blank">📅 20:02 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69064">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9ec0fc6074.mp4?token=rHlH23gNMEqQSJSrL4wLtumxs0uHrq5O6yrrGNGpVXLTatq8IqGGjecSF5pTdHQMwe8biRmwwW_Y9ufTKneR42OCMpqOA9RtTSpLXNk1f8qECi76SEIxvsKiAFUJa2H6XW6JktgdYcAJZVj0zS_J5NL-Ki1jeaNZZHk3WVNZYcwJceN2l7TbVB-qsL1fVRC3-7NTV7oZ4g6o6YdB6TjS8yd1BaapqSOpDgNTDSwOgIdW7VGoHLrmMq2LqYlfRbKVAIht6_t8kA5VBDcEIPyCbULuSwGXDq8oq6CYp5QYG1vUEPjstmmfiGGkRETRg28yrEyfwRmVzFb1APZHLsqmDg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9ec0fc6074.mp4?token=rHlH23gNMEqQSJSrL4wLtumxs0uHrq5O6yrrGNGpVXLTatq8IqGGjecSF5pTdHQMwe8biRmwwW_Y9ufTKneR42OCMpqOA9RtTSpLXNk1f8qECi76SEIxvsKiAFUJa2H6XW6JktgdYcAJZVj0zS_J5NL-Ki1jeaNZZHk3WVNZYcwJceN2l7TbVB-qsL1fVRC3-7NTV7oZ4g6o6YdB6TjS8yd1BaapqSOpDgNTDSwOgIdW7VGoHLrmMq2LqYlfRbKVAIht6_t8kA5VBDcEIPyCbULuSwGXDq8oq6CYp5QYG1vUEPjstmmfiGGkRETRg28yrEyfwRmVzFb1APZHLsqmDg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
محمدباقر قالیباف، (اردیبشهت 1392):
در اعتراضات کوی دانشگاه عکس‌ام روی موتور با چوب هست. جایی که لازم بوده چوب بزنیم کف خیابون چوب می‌زدیم. افتخارمون هم هست.
در شورای امنیت گفتم هرکسی بخواد بیاد کوی، منِ قالیباف لوله‌شون می‌کنم جمع‌شون می‌کنم.
محکم وایسادم مجوز تیراندازی در کوی رو گرفتم.
@News_Hut</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/69064" target="_blank">📅 19:25 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69063">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🚨
🚨
🇺🇸
پرزیدنت ترامپ به کانال12 اسرائیل: اگه مذاکرات با ایران جواب نده، دوباره حمله می‌کنیم
«الان داریم مذاکرات خیلی جدی و عمیقی با ایران انجام می‌دیم، ولی اگه به نتیجه نرسه، دوباره دست به یه اقدام نظامی خیلی سنگین می‌زنیم.
زیاد هم به دیپلماسی فرصت نمیدم؛ یا خیلی زود به نتیجه می‌رسه، یا کلاً بی‌خیالش می‌شیم.
همه کسایی که توی مذاکرات با ایران درگیرن ازم خواستن حمله نکنم. مدام می‌گفتن: "شلیک نکن."
برای همین تصمیم گرفتم فعلاً حملات آمریکا رو متوقف کنم و یه فرصت دیگه به دیپلماسی بدم.
به نظرم ایرانی‌ها می‌خوان به توافق برسن و منم قبول کردم حملات رو فعلاً متوقف کنم، چون نه چیزی برای از دست دادن هست، نه چیزی برای به دست آوردن.»
@News_Hut</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/69063" target="_blank">📅 18:47 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69060">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0b8aee1d66.mp4?token=rIDMNTSo3QBSBVcSGjhIkcQ4t7wM52-xUw-U0UGNDu2CvPG3Jp3XUdKfBg33Y324w1TSM9_cAMIXMkJH00rHwYeNYC0wkhx_eDoZ9EuccWqXPqxsfPdfZZPDyrONpQWnp41PL8lVQOM7eTWnQlegiXOJ4EvdkwZGJPXp_Dl_tDV_TbVEcTlEHO1wnZSU7VRu9qEc0aOVTqGpbCD-qAIgA5sD-KhOFQ8Ljix0qtxN7vB-BocPyQfTDCRy8XhJeFiKjdXNUtfaMeRSbsQ8-AEDevzD_uvT1PXo8-9BRsLXErpmuCgBtGX2e6j7ncFqBCUDLKxjeiOfrY7kZOCmfJg-GGQaXL4Rri6HY5EGnEAvRKRHIyY5e6ySrjZz54kq4R0lcxUhvPIYKbh441l8k4KiFe39gOJaoVx2_qbB0B_MCyOkiA0JCG9dXCc4SmeUEVRCbASH-ZJH8I9pnBYJcoOC1e9oWQMAxR0w7-mFjNryUTJUdvqU7Ybi3Qvvbxs3zbGnovozzULs7ctG1btIvEa9FMG-Hrj_TMz7ga55VY4lk7yf6UuYmOkwBSKY4U2bhqSoA_grtjlnPR1SHUfCZ-GJ5PHsENzuBSM0RNzzSQ3hOlV8JNN9vcFzMbIKX08hEVYtzhjXUSKsCe7e15d7ulOV6knEar0WZ5pYn7ijrFNEAas" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0b8aee1d66.mp4?token=rIDMNTSo3QBSBVcSGjhIkcQ4t7wM52-xUw-U0UGNDu2CvPG3Jp3XUdKfBg33Y324w1TSM9_cAMIXMkJH00rHwYeNYC0wkhx_eDoZ9EuccWqXPqxsfPdfZZPDyrONpQWnp41PL8lVQOM7eTWnQlegiXOJ4EvdkwZGJPXp_Dl_tDV_TbVEcTlEHO1wnZSU7VRu9qEc0aOVTqGpbCD-qAIgA5sD-KhOFQ8Ljix0qtxN7vB-BocPyQfTDCRy8XhJeFiKjdXNUtfaMeRSbsQ8-AEDevzD_uvT1PXo8-9BRsLXErpmuCgBtGX2e6j7ncFqBCUDLKxjeiOfrY7kZOCmfJg-GGQaXL4Rri6HY5EGnEAvRKRHIyY5e6ySrjZz54kq4R0lcxUhvPIYKbh441l8k4KiFe39gOJaoVx2_qbB0B_MCyOkiA0JCG9dXCc4SmeUEVRCbASH-ZJH8I9pnBYJcoOC1e9oWQMAxR0w7-mFjNryUTJUdvqU7Ybi3Qvvbxs3zbGnovozzULs7ctG1btIvEa9FMG-Hrj_TMz7ga55VY4lk7yf6UuYmOkwBSKY4U2bhqSoA_grtjlnPR1SHUfCZ-GJ5PHsENzuBSM0RNzzSQ3hOlV8JNN9vcFzMbIKX08hEVYtzhjXUSKsCe7e15d7ulOV6knEar0WZ5pYn7ijrFNEAas" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
دیروز بعد از 25 سال، قلعه‌ی الموتِ قزوین با رای مثبت داوران یونسکو، ثبت جهانی شد؛
قدمت این بنا برمیگرده به 1100 سال پیش، دوره‌ی دیلمیان، که ازش به عنوان یه مرکز استراتژیک استفاده میکردن.
سال 654 هجری‌قمری، حین حمله‌ی مغول، هلاکوخان دستور میده که این بنا رو به همراه کتابخونه‌ی ارزشمندش به آتیش بکشن.
امروز فقط خرابه‌هایی از دیوارها و پایه‌های قلعه مونده، ولی هنوز هم به عنوان یه جاذبه تاریخی-طبیعی خیلی معروفه.
قلعه الموت 30 اُمین اثر ایران تو میراث جهانی یونسکوئه.
@News_Hut</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/news_hut/69060" target="_blank">📅 18:14 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69059">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1028348d85.mp4?token=cYGbURSJi4qC5Ho0XO6Yz6FHCCNDRkzCwEM8f5PGcQiFdFa1cjn5rdIch5HWBQW5cmuXuR45XaxLpYEulst_4eHDPxhD__eNar8GW5bTvCamvxctxlNFAENsjCQGpGFqpV8DUUB1MrikAC-sHxRSaMFmhfp_ycx0h84JHIzO_6jk-hVKdsrhh_6naHWVwptR6aZcUmBrP73PY7XT05HEbfHkDylWsA9TKL7GxwEY7_XrRKGEiIuN29urtMtS1fpViM8QdeL51R-2kdpkU_842I5fKTiEx3cZgYuwHcUcvboU0lY8zK7QZzApQTFEZC3q0isahYvoy0WAh3_bRy1YJKbZlXk08M_KjImIlQo4FWssYYuZX5r9ddCYQ9s9ZKMgH3CRB6crF4LPC8d3dUCROGyiyJ2S3-tldkyeOaeY_g18IqyuTwQhulBVx9-1SPuEC8uKB9nn9suOhX0V2ClZ7mBf0mI8-VhxkFDK3fe16AbTPgh7Bs99lHCOpHe-Sdxjcku3Cb3_k0b_HQXFBuZMjXdE27Z_x509oLBU8_gMIKd3IyH_V6eSaFFPjNBv3o2W268gG4q4MU575oTe_gpER43VTL1FWvU52Xy4eW0raH5_xqMjHKs9fdyWmV66pWge5nLC7hFh3hMqiI37fubc-5JBarPiDfFfnEmYnuoon5o" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1028348d85.mp4?token=cYGbURSJi4qC5Ho0XO6Yz6FHCCNDRkzCwEM8f5PGcQiFdFa1cjn5rdIch5HWBQW5cmuXuR45XaxLpYEulst_4eHDPxhD__eNar8GW5bTvCamvxctxlNFAENsjCQGpGFqpV8DUUB1MrikAC-sHxRSaMFmhfp_ycx0h84JHIzO_6jk-hVKdsrhh_6naHWVwptR6aZcUmBrP73PY7XT05HEbfHkDylWsA9TKL7GxwEY7_XrRKGEiIuN29urtMtS1fpViM8QdeL51R-2kdpkU_842I5fKTiEx3cZgYuwHcUcvboU0lY8zK7QZzApQTFEZC3q0isahYvoy0WAh3_bRy1YJKbZlXk08M_KjImIlQo4FWssYYuZX5r9ddCYQ9s9ZKMgH3CRB6crF4LPC8d3dUCROGyiyJ2S3-tldkyeOaeY_g18IqyuTwQhulBVx9-1SPuEC8uKB9nn9suOhX0V2ClZ7mBf0mI8-VhxkFDK3fe16AbTPgh7Bs99lHCOpHe-Sdxjcku3Cb3_k0b_HQXFBuZMjXdE27Z_x509oLBU8_gMIKd3IyH_V6eSaFFPjNBv3o2W268gG4q4MU575oTe_gpER43VTL1FWvU52Xy4eW0raH5_xqMjHKs9fdyWmV66pWge5nLC7hFh3hMqiI37fubc-5JBarPiDfFfnEmYnuoon5o" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیو وایرال شده از یه هموطنمون که برق خونش رفته و کولر ماشین وصل کرده تو خونش
🙁
@News_Hut</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/69059" target="_blank">📅 17:29 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69058">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qmCW7-W0pmUyxp5CQHxlAW7Et25Z9rTfd7JUpM7Ie4dOkDvXHBeV1Y-F6iDOKn93RYgwAYeZabjXPDqyl1O9QR6FLTFF2h144mcVCQAT46yKF4pKCAHWXp10toIrtICrOkfr9enwWr0LjhHw4rxMZlzPwelha8nCzQVokcxh-bfk4OvX4JfYg1FdPaI92s_Jl3l47-PuCxn_gQ3zZMRCNANpjXpAKDnRNhioB0mN7FdL-i_NvGAS5sb8mzdsX7nwkx84DXJPiQOgPut3xen8kAbT-1R3M2qRxZsfIJbLtDipKs891K6BtaHHndAlAdgJn23SX1FPltP6M2FmKJaUxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇮🇷
قالیباف خطاب به مردم آمریکا:
دلتان برای قیمت فعلی بنزین تنگ می شود.
بنزین در آستانه لیتری ۱۰ تومان
!
@News_Hut</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/news_hut/69058" target="_blank">📅 17:15 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69057">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j1vmn3QxTq4kET4VkbkR2ZCD4QTD4V7yelOJFvc7zfIBuJCexrEQIAzXVJJBV0Yw7G59bGKkb-LJ2sVcLy4wFys818fgQ9L-mjMBaRE8ezS59IoX28tWS69O4f5vNkWjeut3NFcERmu4kHaZD_begf9cVhcjJGaOTLE3Irz27TuwCchwjbDRAT9Sb2fnsTrHKj2LVyCoZcZt0j-Ni3qAj2ZFskKEvFUyoLLCcg9KF7MaufKNa3H-iwS1TPK0EGb_EoHll5yRh65jmzbJnxLzuYsC3kEN31glfTb4e5gcm6YCzc-xQAySKjreib0ZLW00QJ96glyLVkE5Ge_odeNOhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⭕️
همشهری:
سران قوا با بنزین ۱۰ هزار تومانی برای «سهمیه سوم» موافقت کردند.
درحال حاضر، سهمیه سوم بنزین با قیمت ۵۰۰۰ تومان عرضه می شود.
@News_Hut</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/69057" target="_blank">📅 16:50 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69056">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H_P5KMTU7Gg3OUkRCH789pqITNDOdWm5dTYDoLB7rJ6OHfxM8ENy7w94SS-5VpqTM_D13z6jM2YygLpnDIODy2HFT55hrE11Tg3_DbXptgdZiMzAhTVxII4h01G6jlSHDG6264sNKua6AdrA3WfRmVFOKUX5S7GDDATskRykVP6oWWGlUbz2CflW9bDivh9u1XheiDuIikp_C8pEHAZmcRE1OW28F5uRST-G8NAy0QIP_2aw-F1kgMPVj1dAS8T5ECDt9oD_Jr_hPUC1d0_0q6NSbnPeb4GChkoYI-qsxsaeABTy_lyn7rrKmQ1okqgS98gJ-7es_DjjBvIP9WNyrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇸🇦
وزارت دفاع عربستان سعودی:
رهگیری و انهدام تعدادی پهپاد که از خاک عراق آمده بودند.
@News_Hut</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/69056" target="_blank">📅 16:27 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69055">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/69d958cc0a.mp4?token=bUZBcQ9D0p_PLmgAxI5qwvOLh9GZWGQQ8_59eBSuhL8jCRgVRc44zrGkBKlNW1dJZXrgvaxfQmSTDS2m-b1WrdSz5zjRlKKnpXiac7Ns0A3J4ZOfVxoGAsCUcBOiOb5UghkJJXuXs893DfGGjuCabvFbza5v8Md1LwO8TWPQQkSKW2aF3snHSPg2Ol453sn3DXMt6pQoID2J_k-lrXNOtPwf_7SpYJsyOAHgTEk4DYCpW7W6ZA7PqUFBmm7PKZlEgkxnsq1f1V0GaucG89ONJYok2yCvVHTEK2cIZcmmDve-tKVDFvIAfbJlazhwMS7syEZYmSmZ63UVmT8h-QNNjw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/69d958cc0a.mp4?token=bUZBcQ9D0p_PLmgAxI5qwvOLh9GZWGQQ8_59eBSuhL8jCRgVRc44zrGkBKlNW1dJZXrgvaxfQmSTDS2m-b1WrdSz5zjRlKKnpXiac7Ns0A3J4ZOfVxoGAsCUcBOiOb5UghkJJXuXs893DfGGjuCabvFbza5v8Md1LwO8TWPQQkSKW2aF3snHSPg2Ol453sn3DXMt6pQoID2J_k-lrXNOtPwf_7SpYJsyOAHgTEk4DYCpW7W6ZA7PqUFBmm7PKZlEgkxnsq1f1V0GaucG89ONJYok2yCvVHTEK2cIZcmmDve-tKVDFvIAfbJlazhwMS7syEZYmSmZ63UVmT8h-QNNjw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">برخورد صاعقه به موشک چينى در لحظه پرتاب‌
👀
@News_Hut</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/69055" target="_blank">📅 16:15 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69054">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e50eb610c7.mp4?token=Snxax_wwTdlN7_n77OE_IWYjW0xfzADB2MKUTUtUbTEX5t24sUsHM1qACqmZ3vwORbpOi1UNoX9GGYzwGdQO2FTWLpDh5wU9L5EPu1L05ttryYzvB6hlBIJYBny1u9ckVQrzbFndsOa7Yo85-9TlSYiLAb8feH0NRet-O9oD6X2Mx9l-QOkPmKJJRXv3zWlMiUTRtxhTCGbtYA_3fLDi92dvqtFkoIMxFFdHwQrNVhSXMKC-qFdJLYfn25nFsU_1PZfq5KtL8o2hr-5yLRKkilOaENTYCpc4k0h4BYhMUv5ticdwx3zcZx1zdIEfWWt1XdQDE3qPcAUHf4r2VTBF3Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e50eb610c7.mp4?token=Snxax_wwTdlN7_n77OE_IWYjW0xfzADB2MKUTUtUbTEX5t24sUsHM1qACqmZ3vwORbpOi1UNoX9GGYzwGdQO2FTWLpDh5wU9L5EPu1L05ttryYzvB6hlBIJYBny1u9ckVQrzbFndsOa7Yo85-9TlSYiLAb8feH0NRet-O9oD6X2Mx9l-QOkPmKJJRXv3zWlMiUTRtxhTCGbtYA_3fLDi92dvqtFkoIMxFFdHwQrNVhSXMKC-qFdJLYfn25nFsU_1PZfq5KtL8o2hr-5yLRKkilOaENTYCpc4k0h4BYhMUv5ticdwx3zcZx1zdIEfWWt1XdQDE3qPcAUHf4r2VTBF3Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇱
نخست‌وزیر نتانیاهو:
من در راه واشنگتن برای دیدار با دوستمان، دونالد ترامپ، رئیس جمهور ایالات متحده هستم.
این هشتمین دیدار من با او از زمان انتخابش به عنوان رئیس جمهور است، بیش از هر رهبر بین‌المللی دیگر. این یک امتیاز بزرگ است، اما همچنین یک مسئولیت بزرگ است.
بر اساس تجربه من به عنوان نخست وزیر، باید در این دوران پیچیده با عزم و اراده قوی و خرد فراوان عمل کرد.
ما تمام موضوعات دستور کار را که در صدر آنها ایران قرار دارد، مورد بحث قرار خواهیم داد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/69054" target="_blank">📅 15:13 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69053">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🚨
🇮🇷
اسماعیل بقایی سخنگوی وزارت خارجه:
«در حال حاضر هیچ مذاکره‌ای با ایالات متحده نداریم و به هیچ آتش‌بسی تعهد نداریم.»
@News_Hut</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/news_hut/69053" target="_blank">📅 14:51 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69052">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RCHqZ7gFW_CdguY_XNECzmf4PZ30-Ro5HpJoWdsrNJ5X6YDS0ITyPXy8g_MzUc6TT5f4U1pEqWSzKHieFtgibFIk0TT2qSpd-6C7AUpy1o-b1fIohwBXSBGgD9Hdf8taswkjN5p9XD_TeTSRhKtzFS-PWcjgkiv7vmMhJ6Z1AsJS9u9SVSrU5m5ixcsjs9R-gppQHdJMLuAgf8KFCLdFaY0jbSOCa1T2EF_5x5ZnTIDvD_Dovv1LPq_6UU0Rc2DjBNOclvAUOwSbJ55wKlp6P_nPmziOGzxLwXx9jg1FHk1ieOUVN82vEZNQ09A2yj7ophDCSgJdWiSnIdyz0EymXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇱
🇮🇱
🇺🇸
هواپیمای نتانیاهو عازم واشنگتن شد!
@News_Hut</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/69052" target="_blank">📅 14:17 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69051">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/daAxmCExWkNiBKTZ4jGoZnNHeve7Du4Y_QZ6d1qH9Y--6K8-wJGMKIEJVI7nFbeT0gxK_jHNApMxz4ExJ6Z2MNjdRhU2cmyjjnJD1V50AIIrUE6mA6SSmnvgXv8Q5AMtlgiCmDShO-Qj-dpLHR9CJKE6fN2vfRhyY-USzqHvog6vKXJvZ9ZuZpDqjkd-X6EBKJMfZvcukaBFVIDOQJPWZ9tyNtxDimY_ahw5QdyVutsvL3hnzblSNnMf2pmNxjGHy6fvdJmz8NAbtot_vuies5JGU5VZApZGleD8JNJsmlAG3QKvwGTFVIJA00ZmifAangQGxuIRIpjSP1YGUgVp0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
کروز AGM-129؛ موشک کروز پنهانکاری که از «بالا» نامرئی بود
موشک کروز هسته‌ای AGM-129 Advanced Cruise Missile (ACM) یکی از پیشرفته‌ترین تسلیحات دوران جنگ سرد بود؛ سلاحی که بسیاری آن را «یک هواپیمای رادارگریز بدون خلبان» می‌دانند. طراحی این موشک به‌گونه‌ای انجام شده بود که از زوایای بالا کمترین بازتاب راداری را داشته باشد؛ به همین دلیل ظاهر آن برای بسیاری شبیه یک هواپیمای وارونه به نظر می‌رسید.
برخلاف موشک‌های کروز متداول، سکان عمودی AGM-129 به سمت پایین قرار داشت، ورودی هوای موتور در زیر بدنه تعبیه شده بود و خروجی موتور نیز به‌گونه‌ای طراحی شده بود که امضای حرارتی و راداری آن از دید هواپیماهای آواکس و جنگنده‌های رهگیر شوروی تا حد امکان کاهش یابد. این طراحی نتیجه تغییر تهدیدات دهه ۱۹۸۰ و ظهور رادارهای «نگاه به پایین، شلیک به پایین» بود.
این موشک با بردی بیش از ۳۲۰۰ کیلومتر، سرعت نزدیک به صوت و سرجنگی هسته‌ای W80، از سامانه‌های ناوبری پیشرفته شامل ناوبری اینرسی، تطبیق عوارض زمین (TERCOM)، لیزر داپلر و حسگر LADAR بهره می‌برد که امکان پرواز دقیق و پنهان در ارتفاع پایین را فراهم می‌کرد. AGM-129 تنها توسط بمب‌افکن B-52 Stratofortress حمل می‌شد و هر فروند B-52 توان حمل ۲۰ فروند از این موشک را داشت.
با وجود فناوری بسیار پیشرفته، هزینه بالای نگهداری، کاهش تهدیدات پس از پایان جنگ سرد و تمرکز آمریکا بر جنگ‌های ضدتروریسم باعث شد این موشک بین سال‌های ۲۰۰۷ تا ۲۰۱۲ از خدمت خارج و تمامی نمونه‌های عملیاتی آن منهدم شوند. امروزه آمریکا برای جایگزینی آن در حال توسعه موشک هسته‌ای پنهانکار LRSO است؛ برنامه‌ای که میلیاردها دلار هزینه خواهد داشت.
@News_Hut</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/69051" target="_blank">📅 13:34 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69050">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WiHzzc6NP6SkfGuqZBZ9JrwZ5lU6BseS-hTFnP7dPYK_J4PM1kgDI0cAQS5PQAPTYq8jV1V5jWo-avR8FhR530SExeirGH39vjZ8rtH9E_exKtULEC2XPJnC8SSnBEOKX21tB8DwmmgwIFvMwEv1YRcNgU2EVY_QGaiC8WuLqKG9xPxboY0hI5uIhC_0hNAcVh-JOVLG6RmcIEobdp29EQUC5WxyO7GLLviakPYy-JHjNwM6LYkm0bvYQSNFViUakpPymdY_Y2wRFke1LAA12BP1n58mkSumV5J2te21A95ANfwxS2FMi0i6EzymyY12hL5KDfQukUouJK3eg5y8FA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
👑
شاهزاده رضا پهلوی:
چهل و شش سال از درگذشت پدرم می‌گذرد، اما او امروز زنده‌ترین چهره سیاسی در پیشگاه تاریخ و دل ایرانیان است.
شعله عشق ملت ایران به او روز به روز بلندتر و فروزان‌تر می‌شود. همان‌طور که جاویدنام مجیدرضا رهنورد به نیابت از میلیون‌ها جوان ایرانی نوشت: «نسلی عاشقت شد، که تو را هرگز ندید».
پدرم با تمام وجود، عاشقِ ایران بود. قلب او با طبیعت این خاک می‌تپید و باریدن باران بر دشت‌های ایران، برایش بهترین و زیباترین خبر بود.
او در ۲۲ سالگی، کشور را در شرایط دشوار اشغال متفقین تحویل گرفت و با تکیه بر میهن‌پرستی، ایران را به سوی دروازه‌های تمدن بزرگ هدایت کرد. اگر فاجعه ۵۷، مسیر تاریخ ما را منحرف نمی‌کرد، ایران امروز یکی از درخشان‌ترین قطب‌های رفاه و توسعه در جهان بود.
هم‌میهنانم، اگر به راه او باور داریم، مسئولیت بزرگی بر دوش ماست. برای وفاداری به نگاه او، ما باید ایران را از این فرقه تبهکار پس بگیریم و آن را دوباره بسازیم.
پاینده ایران
@News_Hut</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/69050" target="_blank">📅 12:59 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69049">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/743c9eadbb.mp4?token=PWkm83VtCm8RlmPidjdmjgfWQzV6cOCY7D9AOqxQ1SwB0UwbPwcc3QLaXit1invoBAwFMmPULAEyV8n7KsdX3XcqlK64tnvYOyb2_M0jGuKG4DyZkKu-mCZXGt2TqFsK2JgIKEFspA6vef13bmrq8piXwc8FWy8FpDbo8YjsP3Hw1erGo936WaZvW7rvRBYVlxDPWy6nNyMbqt8q2lDEldn7seaIK43cxnWdkICg9gSd0Ae0zAnz9n8JqE401whDJIgoKDiyCHOeMTqa4YQ3WEFlUX3C4O2MpEP4MMq4mG3SyBdipRZ0ukQ8MFaTQjujEb2DaBwURII8DzkoGMudkUZuwdwuxTdsl0AcqZ92prylwvMtsef7_ulOkUrKtzWt4AMgyq3X0H1zrgjYO9ypLnv8fzvrDCs18-hWFHDg0f3Nn9A5OMGts1Tz12e2oOxkLjx98QGDyApPsEXPDo99nnjfeE10to3VqgWNk_2tu8dkddQ-1iHRPl7N__ryNOBflr8wXQAUu27dO9ZqAmiGHDsc7TkMDxXR98bAJqYdeIgIH49MqYWUZULAoFzOVlygFYPkNdyw8IV118Mvff1hdCurccQHHMIgKR5wOUGcJepuEsYzdpvSRylbIzeA83X5wy2u7ofh8TQgQ4ALmPB6sfukvpMGBp92_hzdo4M9vE8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/743c9eadbb.mp4?token=PWkm83VtCm8RlmPidjdmjgfWQzV6cOCY7D9AOqxQ1SwB0UwbPwcc3QLaXit1invoBAwFMmPULAEyV8n7KsdX3XcqlK64tnvYOyb2_M0jGuKG4DyZkKu-mCZXGt2TqFsK2JgIKEFspA6vef13bmrq8piXwc8FWy8FpDbo8YjsP3Hw1erGo936WaZvW7rvRBYVlxDPWy6nNyMbqt8q2lDEldn7seaIK43cxnWdkICg9gSd0Ae0zAnz9n8JqE401whDJIgoKDiyCHOeMTqa4YQ3WEFlUX3C4O2MpEP4MMq4mG3SyBdipRZ0ukQ8MFaTQjujEb2DaBwURII8DzkoGMudkUZuwdwuxTdsl0AcqZ92prylwvMtsef7_ulOkUrKtzWt4AMgyq3X0H1zrgjYO9ypLnv8fzvrDCs18-hWFHDg0f3Nn9A5OMGts1Tz12e2oOxkLjx98QGDyApPsEXPDo99nnjfeE10to3VqgWNk_2tu8dkddQ-1iHRPl7N__ryNOBflr8wXQAUu27dO9ZqAmiGHDsc7TkMDxXR98bAJqYdeIgIH49MqYWUZULAoFzOVlygFYPkNdyw8IV118Mvff1hdCurccQHHMIgKR5wOUGcJepuEsYzdpvSRylbIzeA83X5wy2u7ofh8TQgQ4ALmPB6sfukvpMGBp92_hzdo4M9vE8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
ایلان ماسک : در سال ۲۰۳۶ پول دیگه اهمیتی نخواهد داشت.
پول رو برای چی می‌خوای؟ برای کالا و خدمات: غذا، مسکن، حمل‌ونقل، سرگرمی.
اگر ربات‌ها و هوش مصنوعی بیشتر از اون چیزی که هر انسانی بتونه مصرف کنه، کالا و خدمات تولید کنن، دیگه به پول نیازی نداری.
@News_Hut</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/69049" target="_blank">📅 12:00 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69048">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">و همچنین یادمون نره طبق اطلاعات موجود، آمریکا همچنان به تاسیسات زیرزمینی هسته‌ای ایران حمله نکرده، یعنی اورانیوم ها همچنان در دست ایران هستند، اون فتوای پدر بود که گفت بمب اتم نخواهیم ساخت، ولی الان مملکت افتاده دست پسر و تندرو های سپاه، پس آمریکا حتماً این رو در نظر داره اگه نیروی پیاده نظام برای نابودی تاسیسات هسته‌ای وارد نشه، ممکنه از طرف مجتبی خامنه‌ای با یک سورپرایز مواجه بشن!</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/69048" target="_blank">📅 11:18 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69047">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZnBSxS_67A1l9W3RRwA7OkD4lYqHQoWe3uXd4ttYYSm3WOgKsLPTQbFrMxW1FifFlMXafU4QgkFmyuXNxgT2P380J8YiJkoD0H-10s0FPQbM_F49EhqqCLTeKxUHuux6fHZRb8EuTRp659b7Duz8U5V0dfuBoQAYKZklo-a41EPg5weomOtPF6PYEnMGm-e2pTr_RcSniBXlq9L3K98eiRvwLGL4cqbHnCA5hJnclvm3z63Sd8VmrI_E9rH_8fJX9s7NDycJ7SpyzcYcgK5W95fnPtC2AucAFnk_P3gN1c0GQntilzGg3HABAQ1VU0QMdxXZJKJDJuoiF2xBMXfe9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
🇺🇸
وال استریت ژورنال:ترامپ حملات به ایران را متوقف کرد؛ در حالی که مقامات در حال بررسی کاهش ذخایر سامانه‌های پدافند هوایی هستند.
ترامپ برنامه‌های مربوط به یک عملیات هوایی گسترده ایالات متحده علیه ایران را متوقف کرده است؛ این در حالی است که مقامات، مسیر دیپلماسی را دنبال می‌کنند و نگرانی‌ها پیرامون کاهش ذخایر موشک‌های پدافند هوایی آمریکا را مورد ارزیابی قرار می‌دهند.
با وجود اینکه ارتش برای انجام حملاتی که می‌توانست تا دو هفته به طول انجامد آماده شده بود، اجرای این عملیات به تعویق افتاد.
در حالی که ترامپ تأکید دارد ذخایر تسلیحاتی آمریکا همچنان بیش از حدِ نیاز است، میان فرماندهان نظامی در خصوص اینکه آیا کاهش موجودی موشک‌های رهگیر «پاتریوت» خطری جدی محسوب می‌شود یا خیر، اختلاف نظر وجود دارد.
@News_Hut</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/69047" target="_blank">📅 11:15 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69046">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f112ef275e.mp4?token=A78c27mjPHqR2oBodW9h8G-CJNafd_r2a6JmSbU6GK4a1aZdTbTYMVoyyRjJRayiMoGpw9Z0QRvYDVPEdgHnlLQZX_E51ct-G8j6uzttd8sJHgZw_imPufBJKecrbXfXEyVGWNLk9V-fznBWfk56rQMaiQhA_BDpjTBCnbZMuOzxe3kXrnEgnewvxVej-kPln5KwFxJWWWzPjQQmmsss7jkktuth8CIA-XF1p1A0Y1WRifyatLRupsRG9mgkZJH7mQWS31nyrnlmGHwT6v0nOOL625AVe8vu-mSZznhSBnx3Nlm6uYLrfNt6T-oJv7goDyQrGtr6ygKt6LSj3au3pg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f112ef275e.mp4?token=A78c27mjPHqR2oBodW9h8G-CJNafd_r2a6JmSbU6GK4a1aZdTbTYMVoyyRjJRayiMoGpw9Z0QRvYDVPEdgHnlLQZX_E51ct-G8j6uzttd8sJHgZw_imPufBJKecrbXfXEyVGWNLk9V-fznBWfk56rQMaiQhA_BDpjTBCnbZMuOzxe3kXrnEgnewvxVej-kPln5KwFxJWWWzPjQQmmsss7jkktuth8CIA-XF1p1A0Y1WRifyatLRupsRG9mgkZJH7mQWS31nyrnlmGHwT6v0nOOL625AVe8vu-mSZznhSBnx3Nlm6uYLrfNt6T-oJv7goDyQrGtr6ygKt6LSj3au3pg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
در ۲۹ دسامبر ۲۰۲۵، خودروی آنتونی جاشوا در نیجریه با یک کامیون تصادف کرد. در این سانحه، سینا غمی، مربی آمادگی جسمانی و دوست نزدیک او، جان باخت. جاشوا پس از ۲۰۸ روز دوری از رینگ، با آهنگ «نقاب» از سیاوش قمیشی به یاد دوست از دست‌رفته‌اش بازگشت و در یک کامبک احساسی دوباره وارد رینگ شد.
@News_Hut</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/69046" target="_blank">📅 10:32 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69045">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M2ioOaRB6JJE0wpBoi2e0ZuUHUiukKpm2Am5LHlhgFE96gAfJeIK2JC10kz8M1NCCVHxmcIlAZbcfaPYuOm5zMZSrHIoCxXUQ05rBFsk3f-TDmJ_FN6Aa1NMTe9JYDql5-KMTb55sYOoXHIYQprgr9RxxZO7L8iiBn1xgUyWH3xOC6IQe_kpwGow0U1CdrKhl581Vu0HWxlhMAV8wHuF8H19meRhLP7SzvgyWI2n83OLemCaxhD211kIBLo49UHcLX23dFwccgjAzclCBnuaO6-ZWzU9OQqQfSLdal8g1Aznb752_7gnZmzYPGuHZ7JKU9QyztsVC52dhUexcyMWJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
دوش پرتاب میثاق ۲ / ۳ دست نیروهای رژیم جمهوری اسلامی:
⏺
نقاط ضعف میثاق-۲ و میثاق-۳:
برد و ارتفاع درگیری محدود
وابستگی به خط دید و اپراتور
آسیب‌پذیری بالای نیروی شلیک‌کننده
محدودیت در برابر اهداف سریع و مانوردهنده
عملکرد ضعیف‌تر در شرایط بد جوی
محدودیت در مقابله با پهپادهای کوچک و کم‌حرارت
ناتوانی در درگیری هم‌زمان با چند هدف
تعداد مهمات همراه محدود
فاقد سامانه دید حرارتی/شبانه پیشرفته برای کشف مستقل اهداف در تاریکی
@News_Hut</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/news_hut/69045" target="_blank">📅 10:01 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69042">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/UdCPuVqJ9wrP0JOt1IOAk-vPtBB8oiWNmOkvZroQPdzreLYik4aKtUU43BlRrbEQHj0WIrTFWTxUaQPJh3h9BcPEDCwYXfLZYiL27mxNpjGblO8rBNGLiVguaQHBJBVMvIVhFhZDOcdl5LowsGwIO5KDvCETNlV1X-Pv5fBv8wsNhJ1x5v71UdA_H4HWMN6YbqetuWy6jEocmvWhxhEBGC73mCBo3I-Ny8TNhFdkc_8_SXReQCH1wUKBZpc1oUly4Z9avvDcR96sK7bzbF6h-VIyVTFpubuzAcS_LIKfIQ06VxVf2OcWNzIQ6xduvbix6CFfjnS7v6XPMjIFgYU5Lw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/c8JRa3pfYbg9JTkD2urDSmzvYHcnOp9KiAJTLFaKDnUXHCDYEGXhNZWMbbUtZ2YrXef1UByaifFtHGZLgGECBZv4372vCy6OYyd8VqhJi1v6wDwVhuPlRLi1CX6gs51zvmKiMTDLiUXkOhqeYiZU9CQQmcEZAjxDSS-S_myer7F64DnCWxh9vLBtER_YIDcrAFln9SO8OWCKsZ6z8Gh0GbDG87iQy76Mh24PXCKhJEgqaN2OBwdUVFcPtF9ryXFlZLcYu1vps1vx_Q8bTeHBCwtpd51oB3sGYQrLamwAYSLbf7vszIimyyAc5y_o6CFDBMcaMJrt8KA3ygmLeZPJlg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/23b96717f5.mp4?token=Iupxgj6g30dBAkSoEWwsV9V0jMmGg9wIqhQCesdIF1zOCWCaJDv9B8B2XVZ75PzdyzuGmNJCC7EtcXqQfo1bfrEDNEPLWm2h4NDorHyt3lpfw7b4ltTtjl6aI7tkqIxnxCrCsKeIAcGEzAmTximGL1-JD65OPB0QWvvf0gmeAb2MlrplEXC6elHOHwe6BKeZ7OYXv5GvZA4KWtqrtWyCODUfskaVOGgJAH72rxH0VQs55b5R9ByCnuH75E-9PAbL2MZzWNXfEwk3bJ4kbdzf9A-KwuRpqFehuZQOpHEONMuDd-bSawwYX1m45LeaaLMcJ1irxpge7r_SxlnZM46DYw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/23b96717f5.mp4?token=Iupxgj6g30dBAkSoEWwsV9V0jMmGg9wIqhQCesdIF1zOCWCaJDv9B8B2XVZ75PzdyzuGmNJCC7EtcXqQfo1bfrEDNEPLWm2h4NDorHyt3lpfw7b4ltTtjl6aI7tkqIxnxCrCsKeIAcGEzAmTximGL1-JD65OPB0QWvvf0gmeAb2MlrplEXC6elHOHwe6BKeZ7OYXv5GvZA4KWtqrtWyCODUfskaVOGgJAH72rxH0VQs55b5R9ByCnuH75E-9PAbL2MZzWNXfEwk3bJ4kbdzf9A-KwuRpqFehuZQOpHEONMuDd-bSawwYX1m45LeaaLMcJ1irxpge7r_SxlnZM46DYw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👑
🤴
امروز ۵ ام مرداد، سالروز درگذشت محمدرضا شاه پهلویه.
@News_Hut</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/news_hut/69042" target="_blank">📅 09:15 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69041">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qXV405Ks7HY_mwfQgTwu_DzQYbFAz0-Ou_FYIDFCPyDbzZ2CTyDc_HHSLa7E4M4B6CiZw4V6E70FhYCX4DCruz7fmvGIsig1cLcam3wDfWw2JxB3iAzFs2Qct7ppJQhobTj7cA1jZMI7jXYqyGToX3FSixEdJStKA3fTeSV5sL55WY444t6_kygSvkPkd8j6lZtqemCrIsstCN7o_eoOG4MA7gcOqKxooge-xfQxPffEVHvjA87TxlH2k7nLFio4hUiVyfxlVpANeadILYx6Fm_x6R61duRNnYMFC6bEtdjh1VVfQw1FnM9mVWt4wGi_dkyX92f6QFqDLJOi9wcbbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
ابراهیم عزیزی رئیس کمیسیون امنیت ملی : هر حمله‌ای به ایران همیشه هزینه داشته و امروز هم همینطوره. آمریکا و اسرائیل این موضوع رو خوب می‌دونن.
اوکراین هم ممکنه به‌زودی بفهمه که ایران هیچ اقدامی رو بی‌پاسخ نمی‌ذاره.
فهرست اونایی که درباره ایران اشتباه محاسبه کردن، هر روز داره طولانی‌تر می‌شه.
@News_Hut</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/news_hut/69041" target="_blank">📅 01:46 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69040">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/euzHAJj2T1S9ryMA5ZLd7NaZvP6WPjIpfyqDJ9HorLktmsBMO46cpoYfN9m3aa2L0PRSEOWsseYam8zCrNdWNGnBZtuPF5_R0ZRB478frAJSK3BTyF5-GDnBHDQ8Iz-YhzOjVWLO59DOj4m9vGBCzoHnIzMAaVvvRkg86N0fRqw_4KgoGSMFTsM459znVBoE1lmyUy-UHS0IrUW_zTDGcXm-Dq8DZqEe42hrkTFcPBjJMd8kmcpiXIeqw05Huuhmzo4k3BwXSSCS_9JRpUSaJfIdioFlGGEIWDTlcNfn85QruYF5A2cegvlxnHRBo5WLJcOYjGCNIyAiCc5rQETP-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
ترامپ آمار تلفات نظامی در دوران ریاست‌جمهوری خودش رو با رؤسای‌جمهور دیگه مقایسه میکنه.
@News_Hut</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/news_hut/69040" target="_blank">📅 00:50 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69037">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dbxqqH1HC_yPCVoRrOhfTkNndpMsu5nvskcrVCjb9NVB9bJV1zUQCLUJhIyx7sg_XaN_980FF3BkalaU9ZXc32r5JVvyr3Uw6-mlWIcBgq3oUFXkqOOKHcsRFJHlxmoBR-rJT64CMea7di98Tw9si3ZgM6h7bNyA5IUu4xozj-x8bu7EU32LEU4j-4cWqyH1sVXiZPKOiGN63HuTptjA1Zpf0XSGdXiQrUJBD6taAB0JLftODcCZ2BUGsOIZiPqbjr2qkDBM-dCOdfY4u43cWNQsZLp50GsqX0GHtYwI1IALQ6QSh0xQJC6w5TZiHKS-nFMkWIWiXAW8Fl00Qa-F6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hAv0pcV6VRWERgOdPhEnXEyhI04n9s_dINRbqPQ8uyQX1DRNxlRG5J7dBmwWkeixaF19yK4leGlfkFNSztJttEmZWtRsz5BvmCfOgAR2m2h-YgvyW817lfz5lpQLD9NYZxMArVQLkIYRSEOAwu0ww4MyxsscRBkpEp1cuIv2tJhyrZDyMEPtgdUyYgfoQZiR8KA_irdiGdyuLP9C8zS75suljBVhFdoScXosQ083SbQjioKl14GMi3bn1WRyTgz4oTjKKbc8syyGvATKcqApGPHPoJ8o6YOWeJvR2LCIrA9ZcbSA9BUomIVgK-GaoXh5_I4sSgWg9wG-BThY-GaDrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XybHKj6RCcWYssTUQUby7Or_7ld_R_-7OcP5MbiBvg2mffIOjx_2vov-NuNOlw9yxkNwhgc9e8Ka8tH88_dG5mwhhTraHJ_MsQeppTRW6_Ad9WR2wpWX3aEvjlCNAoIG-knkzNxY7eWX5nevU-BkE3EE0Nv6qnVGRcsBDOPpWdRDkzFuyfU067VUExU_ZcUYwA1dOgm_NvgJDKQDuseBn-5TgApVl-nJXe_kEcJwMd0JQ7eH5debzNc7aMT2qUCBml5sLVMh8CqfBIVfi1_R4dgGQqcNqw3CLQRFNxMGoeByTjkbIZsI4gatR3de6AnnRrpkhrzFHaaLdHCxNbgbNw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇺🇸
ترامپ در تروث:
- به طرح اعتماد کنید
- وحشت در واشنگتن
- آمریکا بازگشته است
@News_Hut</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/news_hut/69037" target="_blank">📅 00:36 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69034">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/M9RvHu78kilABzMtAPdQe7o3sW5Rh0hEjJ2Ocj2PyVaW-CbHUI61uiv9zt03B5-m6cdRjh1UP_rkB5FYWFWUMgPD6iZ4vDbFLLFPnL-ItyhcTO3b0AZv94sCydBauODpYMgq8jK9KjFF8hTyv9UWz5Pcv8taYLR4RMQfjk6fZXXLZy82O0R-bAbtMHfkIVaAna8FyFcPs6gWQE6NTTPLt2IBQaQz4IHMhwHXcsCTcj-oO3L-LdaTxUZXyDQPVLY8LTRY0gZq7pcw7BVl6bo_9xm84P9zLqCpMad3VYuIwK40MY2a9Ccj08aK3HMzByrgLjAwpLakRBkuEf9BDLcEtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XIR4znQSoXrOQoZ_AzZHLEDxEs3AWAk6Jk0-3tLUShdDpxaW6CpOtLefLC98rzlwAxwt05PqbFxEy0Vkyv6e76qibuuDqvngTuyJIK1EWP2768ciZov8b-hRgTlhOTV-UjN83QkUuOrVFMD64aUlGn9NgJZfLSSCfV_SjJQ2WoUFuXw-No-BtknYC1ptSRZDfYdHty-G4G4M7jlrR0QkhDR8NkDLeJ6KI3AZSPkovKmeNh53izh8KHtp7UDmDB4sUsZzql5SgwerDVJpOa_-15525UY2cdsqZTHwlUGJ6yieWCdM_Pky21WEYymT0mNfp6VkFaag32uJKSsiYPsgUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WWGl8mkqG6QB-VlUAmmfBvxGfWj-HwGzcprrxrY_7bBBbwfNiZq8FAm78Y1aINcgpvgf8stL96RrFl1xyq8hv7Hvu4hmE5PHcq8BDbxdAvoG2kKf2xGWTpRXEOE8Txf7wFo6P2N1xSukBie-F0M2LM4tddXM6L6SfHTFT4Z_HjoB4OVNX-BM4TfliBo4l3YFpR4Pngxx3oYFOhtDS6LCkqcr50kJBdmZkD3dXJAjv62_KAEJj2mRkLNC6fSUfc9SNMREFtFAuZ2qgju_ll3tjqvWqSHnw12mIyMldDfdQ_j82W2auFXZEqv9_kCnUVSFe9ib_rYgu-L66RnZTDmN1g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">املاکیه دلقک
😂
@News_Hut</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/news_hut/69034" target="_blank">📅 00:24 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69032">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FqQKIoqdtNV37mBPwwilVJP3ZwINKLBkR7M82orp4rNI3aHEra8YqQV0KX1Tw3Ld1FwyTtodXI_R5TvVg9UmOSVPxLa9-F9xWT7MgKgWDeeva1MxelKvwaBUSxzDQDMEeeFv14AU972lDyk56QqedmSkyK7Bw3dW1ya1SddOwNOQkLfd88Kfj3GCGHqnfkqbkEjskAMdo5ihN-cIqXQcoD1_WtpkyXci88KO36_g_IZ04VQ0wkmrE5DLLyA2DQVVbPGszGVo8EZTM78mZRuS_68tpkC3FF-_xmblWU1LiKucqA-4zaaGHLlHI3n2BUZew4WLD2cr-EWXJc22LHzQ7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PwHbJ7ygMROECIoCGemKA-UsyJv_gKM9m966bxvX7ZbFdvKLpXS056rRLbvIFP2Qhj7JFKJ2utnJ_FRe6zf1TlcDiUiO7K_jeXTlWO4rbXF4AOWqzQKaNg5iRkKnJbiZWmLgaQTJmcfVepyfday-BudmZTE11f5a5-ADjrKT-Tdfwv8x8DvkLJDhL9kJB0D8ayO3W2-OtKD2bmgjlnamXbqQFFM1tfUea-3fhLgwcf3wAHU2F_V_Ku3mRUM0_fvNF7QIjGpA9ajEjl21hu7prTcOQQLb99spVKPOWgj5VgbX3rIXAV5JLIyOT686rBKps2OokA3fXjB8B1COsCFufQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🇺🇸
همچنان ترامپ
@News_Hut</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/news_hut/69032" target="_blank">📅 00:17 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69031">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">رفتیم تو 05/05/05 برنامتون چیه؟
🧐
#hjAly‌</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/news_hut/69031" target="_blank">📅 00:00 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69028">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/b_bdFcBKz4P_C7YNSbHzc2Vs380iu6kxUuL3c9eiALArTa4LkDUMPFlVowwvf3CySGTQXHGDkGJVX9FLlHSR2o2V9GXxmJWpwHPHuHvk9dZhEK0EszkWLEZP_f8DtMdzkLOh4qYs1rXT_dgSWX87RJMKyfimznbjHRbRIjIuLIM76a629svER_t9oQGlf5keq6gf0Ss9O7m2EBO-ZVfJqtOaSrdZrdJ0iG0P3MECqLoGxFLsP7ep547XzJFQFu_6t7Tvg7MjNd6xDzK-d5VXPCsTx6m5SEwFX3yxcG-JdrwbieFOZfkNkH_jwl79ShP6TlIMn1H9OE8l_9KwrYmk4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/G_WSyZt1J-zw6fmqlCRWx_MO35kXl2JUXAn59wDrTcMS8V7AL8pynlSX6M6knumZwyLDuO6g74vYaeEpyrbzCWetnOiqRPoz5jRtYhHo2McSUJTvRdhJEFiMCeOx8wOTrSef09vvxL-n5uLlbQFKfxcD0x59wcYqdkni9QzVriAcYbOgUWD4xdpn3mlU1rA8nf-lz0KDAVxx68jHKkTi7ExeX7KknO6E1AWucMA1bpxH4cPbMQyxjBT1apHSJLUDe8p2CgbXJjsjJ8EBkqMZgvt23M1J7DMruHfbAVgM1kSdx8Ct_FxZ4LLUMnBtK0P21frucetgL6iroDuab4iqxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SZqc-AVDH4O7xjHFq5uzzOyVwc0RgIzdPbMUO_NtlTy-MOQ2BjNO-ZyI7e7IHK1nz4SKfg191uKI6IhA-Rp9jD3ECAfc1lBPYrXzev65T-ZT-Z22e1I2vfiYtMs11necVBdcY0T8X6M6MySpTmSu5_-WeUDAPYVVupbZ1QCC4rSEbjODFP-j0n0uHwTnokava_Lw_xjPS36yt-77EEjbvlmPs3y4QsIXtYax3ppFlFpA2yjv_NYx6GItBasjzS5KlH-bPs-2RcKcCe0fcA_FSsZtszifRctrmj5JKpoaKgaOMxVehNEU5oH69Kw8l9YjpP-A-dfHPqt6QUDmGfPwfg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🇺🇸
تصاویر دیگری که ترامپ در تروث سوشال منتشر کرده!
@News_Hut</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/news_hut/69028" target="_blank">📅 23:28 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69027">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">🚨
تصویری که ترامپ منتشر کرد: حمله به خارک  @News_Hut</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/69027" target="_blank">📅 23:27 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69026">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cnjlvO2yK0Z0D9VemSQUpMDHrmleHf6V_RPmc26itVE-NjnyTPcnKMk7wddKwBz4xcFHvU8mfTQwRMkz2qXeGdzd6qtaWJdRk05_NAwF6bA7oLYsg52anDK0JH4cu_g9JGGJCgn19SDSDTRFUBBH4NH8fALkzvPxL7Bf0dW1QLs0gGNnmh8HC9huJJdaMMbp5g9NA7awcqDDciJfkJV594SHrSbihsiQEwbHrnWLLtrBlVEwimXVSvJsEALXdWvAWTxZZu5v3By6qumBcKsUoI17jpkaHzKwbyztWnfvBiQEVUhMMF5s92uiJRMShhFqEqPzeLyVOPWNlsRDpWtxeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
تصویری که ترامپ منتشر کرد:
حمله به خارک
@News_Hut</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/69026" target="_blank">📅 23:26 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69025">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1e3f5c86e5.mp4?token=T4nKF80hbkC7SCKTKAbmGmbRRXIhfCBUNSv9g97F-X36CVKEu90RVsCndFQtZ0z8asBrL4if1LPcjqrdN2vCiSWauQHYEWT9UqwfeyA5YXWhpGVlMMaPRp-aSilytN7W9Y6WhwBP_xRlbJ8inp8reLDgENLX2kkOFY99LjUHrfuygu7kqx0IqVGqgspqkpu9vEqlVabJRLqsJ4W6jfwhVNOU4AdYNal7J7UM0BJ4F0WWJlhc14r7CCMlsrmN2nEvgGu6k5Be9FErbJPH4WA36fzYFcuIM9UpqcR4BNYSC-tRoKa-nnBFDhtXSscn9BsZsbr2H-TRiNLtK4yhh5kiqQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1e3f5c86e5.mp4?token=T4nKF80hbkC7SCKTKAbmGmbRRXIhfCBUNSv9g97F-X36CVKEu90RVsCndFQtZ0z8asBrL4if1LPcjqrdN2vCiSWauQHYEWT9UqwfeyA5YXWhpGVlMMaPRp-aSilytN7W9Y6WhwBP_xRlbJ8inp8reLDgENLX2kkOFY99LjUHrfuygu7kqx0IqVGqgspqkpu9vEqlVabJRLqsJ4W6jfwhVNOU4AdYNal7J7UM0BJ4F0WWJlhc14r7CCMlsrmN2nEvgGu6k5Be9FErbJPH4WA36fzYFcuIM9UpqcR4BNYSC-tRoKa-nnBFDhtXSscn9BsZsbr2H-TRiNLtK4yhh5kiqQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
🇮🇷
سخنگوی ارتش درباره عدم حمله ایالات متحده به ایران طی دو روز گذشته:
«آمریکایی‌ها سردرگم شده‌اند و استراتژی مشخصی ندارند.
اهداف آن‌ها برای بازگشایی تنگه هرمز و نابودی توانمندی‌های نظامی ایران ناکام مانده است.
🇺🇸
ایالات متحده اکنون ممکن است یکی از سه گزینه را انتخاب کند:
عقب‌نشینی از جنگ
انجام یک عملیات هوایی گسترده
اعزام نیروی زمینی.
ما برای هر سه سناریو آمادگی داریم.»
@News_Hut</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/69025" target="_blank">📅 23:15 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69024">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BUYspi5BO0ShFRv28PHSDEMfQYueQB839PL0GRsfh9MT9hBZTsa_25Rrk-jBIBZ5jOUTXBsfUYCVVkgzcpSgPlskgLlpQQrONBSumoaFDrQ_Y0q9fNLmlblgoBp-kZLMS4NmR8M5Q3euAfLFgM1xMY1mcnU3EYlN0qRaYQKxHHS9JjBEHns0nqS3nPbMAnLEw7rZEY4tbNLkypnqXNWzo_GYzCt-0ospK16OWb6g0jvFUc1b7jCLQxRNLH8w1bpbf4dGx0lVmF4YjQ13qvlD8mdIZtXKkfuE2WK0GkFEIRZddYVPOdZ-URal0LWD38ioaW9DyPropjf5Dirt48-EBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
🇬🇧
🇺🇸
اکسیوس:آمریکا و بریتانیا برای برگزاری کنفرانسی بین‌المللی درباره تنگه هرمز برنامه‌ریزی می‌کنند.
دو دیپلمات اروپایی و دو منبع آگاه به وب‌سایت «اکسیوس» گفتند که ایالات متحده و بریتانیا قصد دارند هفته آینده نشستی سطح‌بالا در لندن برگزار کنند که بر تشکیل یک ائتلاف بین‌المللی احتمالی برای حفاظت از کشتیرانی در تنگه هرمز متمرکز خواهد بود.
بازگشایی این تنگه برای کشتیرانی تجاری، عنصری کلیدی در هرگونه راهبرد خروج ایالات متحده از جنگ با ایران و همچنین در تلاش‌ها برای ایجاد ثبات در بازارهای جهانی انرژی است.
به گفته دیپلمات‌های اروپایی، برنامه سفر و تاریخ آن همچنان در دست بررسی است و هنوز نهایی نشده؛ این رویداد احتمالاً وزرای دفاع و فرماندهان ارشد نظامی کشورهای غربی و کشورهای منطقه را گرد هم خواهد آورد.
پیت هگست، وزیر دفاع، و ژنرال دن کین، رئیس ستاد مشترک، احتمالاً در آن حضور خواهند یافت.
یک مقام کاخ سفید تأیید کرد که ایالات متحده و بریتانیا قصد دارند هفته آینده این کنفرانس را برگزار کنند. سفارت بریتانیا در واشنگتن از اظهار نظر در این باره خودداری کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/69024" target="_blank">📅 22:32 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69023">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PH7kQGSwWPs-Sua4GLJZTRTGzJC-415XGMaeMe89iFRXLRjliiKN725VP7w4ndPX0ROSRxp6FIelxeqQw8S2O9mNrpM-dHd1Vgq-fCBbY9cKLXTy5mYRYhYmeD0Lp8gPc_rJQndHwWYdVVfK5WVQXi7W4GlbY9zt9E9YleDcFPGBGDnnn4-3w6n6yIpm2jIj4rLMLk5sJw7z95FHbqH55YQH7cHA2NhZc8-ocrKOQkhZYuvA2Sg1txIlrfrP0bJ8eVtyyqjIx-rZuwH0WGkSjdejbEf_xb584P19bqQfL8PpvR5ZLE03_8mJVmjTa4XCNk3vsrlvvENYs_Rlfoui_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
آکسیوس: دریاسالار برد کوپر، فرمانده ارشد نظامی آمریکا در خاورمیانه، توصیه کرد که کارزار بمباران در اطراف تنگه هرمز متوقف شود، زیرا این عملیات به سقف کارایی خود رسیده است.
- این تصمیم پس از نشستی با مشاوران ارشد و مقامات نظامی اتخاذ شد؛ کسانی که طرح حمله جدیدی را برای آن روز به او ارائه کرده بودند.
- در روزهای پیش از این نشست، ترامپ تمایل داشت که به عملیات رزمی تمام‌عیار بازگردد، اما دیدگاه او از عصر پنجشنبه شروع به تغییر کرد.
- او تأکید کرد که دو هفته حملات در منطقه تنگه هرمز، توانایی ایران برای حمله به کشتی‌ها را به‌شدت تضعیف کرده است.
- کوپر خاطرنشان کرد که اهداف تعیین‌شده برای بمباران، عمدتاً تمام شده‌اند.
- فرمانده سنتکام گفت که گام احتمالی بعدی می‌تواند ازسرگیری عملیات رزمی تمام‌عیار برای تکمیل آن ۲۰ درصد از اهدافی باشد که ارتش آمریکا تعیین کرده بود، اما در جریان «عملیات خشم حماسی» (Operation Epic Fury) به آن‌ها حمله نکرده بود.
- او تأکید کرد که در صورت عدم تصمیم‌گیری برای بازگشت به عملیات رزمی تمام‌عیار، ادامه کارزار بمبارانِ دو هفته گذشته هیچ فایده‌ای نخواهد داشت.
@News_Hut</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/69023" target="_blank">📅 22:02 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69022">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vekRqgUCfN3ozDx0Kh2jdZQTxBRC5fXxDo4QvZMVz_xlY601U0AUsMrhU0168DXgQPZAlxqWWSljpvo5zdru3EWIRawMYJk4m8wUZNq8vZ-ACTUpuxMWBfJ24CC76TQBe2TP3FqT0kvunsljwdBgh3ZZ4j1jqtwLfXmN1ZlwlYcI5f0aioGFrohLWEYGuTpjf82LIJ6Ec30kLmNA4YgNZuLyS0E0YyW7JLU28qEk69kee_a_L0C5l8Sqt-iKMCS3SydQCJz32rPY0hxSUbaDGR4sP5BQTrXBJ-ZIDz0qRi-zeoOazDhXaE08LQECxbdwOG-dzADRfS2o8hjPNBCgoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
ان‌بی‌سی نیوز:
فرماندهان نظامی آمریکا عمداً به برخی از موشک‌ها و پهپادهای ایرانی اجازه عبور از پدافند هوایی خود را می‌دهند تا ذخایر رو به کاهش سامانه‌های رهگیر را حفظ کنند.
با توجه به اینکه ایران از آغاز جنگ نزدیک به ۹۰۰۰ موشک شلیک کرده است، فرماندهان اکنون فقط با تهدیدهایی که به سمت نیروهای آمریکایی می‌رود، مقابله می‌کنند - و اصابت به باند فرودگاه‌ها، رادارها و انبارهای سوخت را می‌پذیرند تا پاتریوت‌ها، تادها و رهگیرهای سری SM را که جایگزینی آنها سال‌ها طول می‌کشد، حفظ کنند.
@News_Hut</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/69022" target="_blank">📅 20:35 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69021">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xjfk5KmZ03YiPeY6qsTYFfeQKPDx_QAIxG35VFlKzPZBlO-ELfn0TwWjDAjf2HesZB_kwTOoLfI_pf_tR9buILpscLyuTfwrArSANmLzhxVAzs1mGxy4hoxyMtFyqC2lxFyGtTvlEuziAUJ3O-RmBW_QCfTyE44UZvLdCvpepFelg3JgBGpogFkWD8zVeDNhTcClNLCH0fx71fGXMh3WHclwd1gcTW9Ocasv5N0ngQfanASyX21LGrg2F_JGkI_nN4V66C8SpsqKnNMOLPFwY5jPHikDXq3GtW9t6fLwGZYW_y0lOSP4muKRJjqrcEDR-9jzs-zf0t39mWYSxerFmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
عراقچی:
زلنسکی به یک کشتی تجاری ایرانی حمله کرده و موجب کشته شدن یک دریانورد شده است؛ اقدامی که نقض آشکار منشور سازمان ملل و به دستور اسرائیل، با هدف کشاندن اروپا به جنگ آن صورت گرفته است.
در گفتگو با «کالاس» (نماینده عالی اتحادیه اروپا) و «لاوروف» (وزیر امور خارجه روسیه)، تصریح شد که اقدام آن عنصر مفت‌خور در کی‌یف، هرگز بی‌پاسخ نخواهد ماند.
@News_Hut</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/69021" target="_blank">📅 19:53 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69020">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d78921238e.mp4?token=Vk67PefnfQDIq-HJoJlovdvX5sb5G7y-j8MVeqwzkhGlmbFSKOiBIj4dsWYXAMY9LUJptjuPfaY6fI_QauDXRd8URg2XftbtxOiA3nMDk1YDLKn-IQL6yO3f9cC0LXqsZvln2b6yInAVwlsvqhLWn_qFJ9vNV7sJHOO41zs7oh5aiprkDKpqrMsksq-rpqrIamEsV-MVo_hTgUPKuFm1TZjIeiHycXEQrFIQtuvq8-o43MStYEqcPpRpNaXWI8SHkEHUL3ZPlzH1fHycXofky0v3nqO_JuKdHTiZmw8_b7Vn6Pm3eYy_jcMoHBUUZ9RoMT-Cv-7pD9qZmZyhlEloQg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d78921238e.mp4?token=Vk67PefnfQDIq-HJoJlovdvX5sb5G7y-j8MVeqwzkhGlmbFSKOiBIj4dsWYXAMY9LUJptjuPfaY6fI_QauDXRd8URg2XftbtxOiA3nMDk1YDLKn-IQL6yO3f9cC0LXqsZvln2b6yInAVwlsvqhLWn_qFJ9vNV7sJHOO41zs7oh5aiprkDKpqrMsksq-rpqrIamEsV-MVo_hTgUPKuFm1TZjIeiHycXEQrFIQtuvq8-o43MStYEqcPpRpNaXWI8SHkEHUL3ZPlzH1fHycXofky0v3nqO_JuKdHTiZmw8_b7Vn6Pm3eYy_jcMoHBUUZ9RoMT-Cv-7pD9qZmZyhlEloQg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دوتا جوون خواستن برن جزیره لارک دیدن قایق نیست برداشتن شتر هارو انداختن تو دریا دارن میرن
😟
@News_Hut</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/news_hut/69020" target="_blank">📅 19:30 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69019">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fd02960948.mp4?token=QWPxsRe30yGHYbDrlgF1oEupr9d0ut6kLMh0GcUROWzVrnl-t5QgTdbHCLQhK7bir7GjzErhnOYOvQRGR4GHz11atc6NA3_rjslzLA_hwOFvLdOMOtQnS25AAE_VdB74xSrbHdrB03n4QkU3Z9K4JozJ6VYeyWD0XMPhE2I0OUGYT7tubVewRTGhAkWc48kJifSZjtnW_14tFmGqRIEsrSL-NXhg8RIKWB6KfnDNiet-xC7GF6WSCQ3DwZFq0s-nCppKD7xRPs7MGJGk0I5aoQ5ZkFSdt8ZMqnyIIQHqmfHCDlbc1it6sleJIL-BdAv-CjlBe6X_NBX3zfkUVNzx8w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fd02960948.mp4?token=QWPxsRe30yGHYbDrlgF1oEupr9d0ut6kLMh0GcUROWzVrnl-t5QgTdbHCLQhK7bir7GjzErhnOYOvQRGR4GHz11atc6NA3_rjslzLA_hwOFvLdOMOtQnS25AAE_VdB74xSrbHdrB03n4QkU3Z9K4JozJ6VYeyWD0XMPhE2I0OUGYT7tubVewRTGhAkWc48kJifSZjtnW_14tFmGqRIEsrSL-NXhg8RIKWB6KfnDNiet-xC7GF6WSCQ3DwZFq0s-nCppKD7xRPs7MGJGk0I5aoQ5ZkFSdt8ZMqnyIIQHqmfHCDlbc1it6sleJIL-BdAv-CjlBe6X_NBX3zfkUVNzx8w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇺🇸
ویدئویی دست به دست شده با این مضمون که اگر فکر می‌کنید ترامپ واقعاً دنبال اینه مذاکره کنه با جمهوری اسلامی سخت در اشتباهید، این ویدئو رو ببینید تا متوجه بشید.
@News_Hut</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/news_hut/69019" target="_blank">📅 19:00 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69018">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1bca3e5bc1.mp4?token=Y8lyhufddOiYX7iMMaSm0QKDm7vvTCWREilWJCxVHsKTzMlN84FAXsD4cbF2eRNPxT6aqm1KLMWjWon6bRDNcMqtDW3eGIyfVBFAeKxZIPcvbh-ZVMUQY_iHdYADezSjTilja5lhCpQRdrX2zfVz_etYW200W4s3NaI7c9YrS2XNMAQrdn5pcq4OBnoIe1pKADj0MbSx7Zh9fllmO1xVam_UyHBZVsSkZFFlxmvOmxGyVhKJGjmKCaEVzI6bDtygtEQP578yJoA1CRh5TgNv62DtlgDJtxNDopzffb_SAbcpALiWxWXJzOPPRq3gH97cQnfcVthQ9yPO8Ebm-Sx-vQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1bca3e5bc1.mp4?token=Y8lyhufddOiYX7iMMaSm0QKDm7vvTCWREilWJCxVHsKTzMlN84FAXsD4cbF2eRNPxT6aqm1KLMWjWon6bRDNcMqtDW3eGIyfVBFAeKxZIPcvbh-ZVMUQY_iHdYADezSjTilja5lhCpQRdrX2zfVz_etYW200W4s3NaI7c9YrS2XNMAQrdn5pcq4OBnoIe1pKADj0MbSx7Zh9fllmO1xVam_UyHBZVsSkZFFlxmvOmxGyVhKJGjmKCaEVzI6bDtygtEQP578yJoA1CRh5TgNv62DtlgDJtxNDopzffb_SAbcpALiWxWXJzOPPRq3gH97cQnfcVthQ9yPO8Ebm-Sx-vQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇷
🇺🇸
مداح حکومتی خطاب به ترامپ:
"تو گوشِ کَرت اینو فرو کن، خارک‌و‌سه جزیره مال ایرانه"
@News_Hut</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/news_hut/69018" target="_blank">📅 18:15 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69017">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EGTZjz07FLTbWz5n7ijCBnen9IUXLgI0K6P7JxDg1-rnEEg2H09l3nGKi-gHdlS7P2jCUQwqGHeTfYkdgkc1Xb9xQkfMf16lKVVOOY2drrc_nMXX1ykjpU2UsK3Yr5lWt6O26bF5ymgnXj7-EBMdRmC6KU2Ek203qTZ51CzCE-4ptIN0-qJ7R2bbbIflFdfXGGS3UYS6yNt6VKvgoc9epvvYICN7wEGF_9la62eKI-8To1DvkfG4DTLGks4Gl8cHasYdIRX3vYSjJJgZGDJU1azCRay38VwuwU6noZUHzFCoNieMqPBs_zOYmgACYdq_i55GzMYWaI8nu7uoL5u__g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
🇺🇸
العربیه:
- ایران به پاکستان اطلاع داد که از مذاکرات خارج نشده، بلکه مشارکت خود در آنها را به حالت تعلیق درآورده است و تمایل خود را برای از سرگیری مذاکرات در دوحه، ژنو یا اسلام آباد ابراز کرد.
ایران به میانجیگران گفت که با ایجاد مسیر جدید در تنگه هرمز موافقت نخواهد کرد و به پاکستان تأکید کرد که باید طبق یادداشت تفاهم به مذاکرات بازگردد.
ایران خواستار آن است که مذاکرات ابتدا بر تنگه هرمز، سپس بر دارایی‌های مسدود شده و در نهایت بر مسئله هسته‌ای متمرکز شود.
@News_Hut</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/69017" target="_blank">📅 17:29 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69016">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6dcf952e60.mp4?token=TJ7rWTcjBwSs2e_HVovGX3rEf_BCRyM74w4WnusLlA6d29_hc1Q97mNZzPyW8UC133tVxmbyav63hBL0ZH3wlqMeiF3kuksIF-64zkdWr0fq6nvXXu00ggSz-mA5YYYnNPuCjH5Hld1rso1uKbh5zQRr1aaQ70mTZuNUtpsSZk5ZN2B_q8UupUHmrAPTrr1qNnXLI76klYEhNH8vk1LE_1hsdGABcRfqHt4_0XPvMzT1R_FjmQjqmBDJroGsdn4i-UQzCIxC6V3yO5HI221GaI0A5Z5R3_h8khfEYNofv2vAkQBM0Q5FJa10RdaXV6yN_0r9QDFXe8oznRTu_tw0I6jjw_720I7RbzUYTNaBzBI9OEdFVsj0LIgCiMsdPU8OmMRC5EzQX2dXJj91kLq4_XabRsURKEoiB6b9VA-1KQeTTKQesxInHm1iYiYa0CD-T49zBlkGo_eujMX-_e0ddADHSIiDQ7NL7baj3tm7M7OzB8O9Gdc7OpL1LrOlhJn9jRK9ehGPWBauQzCy1gmH0jUGWtm9OEwRi_GWWevCZ_sksX1nphKDJtabBO-PPIm7-xIL0sV1Rqm0KnsfIQaXMb0EP49Aag1HezRAHdV3_gVevcgHJ2J1YXKt4L55xjZFsos1e5MTLW1Dwc07PpSBCwD90qYNSVR0EUzCcxf1FXA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6dcf952e60.mp4?token=TJ7rWTcjBwSs2e_HVovGX3rEf_BCRyM74w4WnusLlA6d29_hc1Q97mNZzPyW8UC133tVxmbyav63hBL0ZH3wlqMeiF3kuksIF-64zkdWr0fq6nvXXu00ggSz-mA5YYYnNPuCjH5Hld1rso1uKbh5zQRr1aaQ70mTZuNUtpsSZk5ZN2B_q8UupUHmrAPTrr1qNnXLI76klYEhNH8vk1LE_1hsdGABcRfqHt4_0XPvMzT1R_FjmQjqmBDJroGsdn4i-UQzCIxC6V3yO5HI221GaI0A5Z5R3_h8khfEYNofv2vAkQBM0Q5FJa10RdaXV6yN_0r9QDFXe8oznRTu_tw0I6jjw_720I7RbzUYTNaBzBI9OEdFVsj0LIgCiMsdPU8OmMRC5EzQX2dXJj91kLq4_XabRsURKEoiB6b9VA-1KQeTTKQesxInHm1iYiYa0CD-T49zBlkGo_eujMX-_e0ddADHSIiDQ7NL7baj3tm7M7OzB8O9Gdc7OpL1LrOlhJn9jRK9ehGPWBauQzCy1gmH0jUGWtm9OEwRi_GWWevCZ_sksX1nphKDJtabBO-PPIm7-xIL0sV1Rqm0KnsfIQaXMb0EP49Aag1HezRAHdV3_gVevcgHJ2J1YXKt4L55xjZFsos1e5MTLW1Dwc07PpSBCwD90qYNSVR0EUzCcxf1FXA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
این ویدیو رو ببینید تا از انواع بمب سنگرشکن و هسته ای اگاه بشید.
@News_Hut</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/69016" target="_blank">📅 17:02 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69014">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ead75df70e.mp4?token=TDe6zJ9LQhGqk-9-npTso_F8dErKAbFEOEiZcI1DMaJK7PC0eAUoR6XfiSMweMUPnjPTXpkHPICMOvpAD5weGEogMLmyGXtiwCbOU4vgsUN1m7BIMpywEBdUasoR_OK9ObL_oACgeCLSXmlvrM-aZH7GGLSKmNhJrVOxVgdPHUDt77JWj-vUKxshuJqnVS0duCfJfHcUgsHopu3AIZuk9zzT3_ZiiGqlzoimD5IXxRj1xckB9WRfDLCFt4S6P6HzKWT2IQaQk0SunuwtHXJl96-NlgIJRfmQEk7ZfCHNZCDB1WE5OIoS1YOCIpq5StO4h3ZWyvmEG1aRK49TGh1BGw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ead75df70e.mp4?token=TDe6zJ9LQhGqk-9-npTso_F8dErKAbFEOEiZcI1DMaJK7PC0eAUoR6XfiSMweMUPnjPTXpkHPICMOvpAD5weGEogMLmyGXtiwCbOU4vgsUN1m7BIMpywEBdUasoR_OK9ObL_oACgeCLSXmlvrM-aZH7GGLSKmNhJrVOxVgdPHUDt77JWj-vUKxshuJqnVS0duCfJfHcUgsHopu3AIZuk9zzT3_ZiiGqlzoimD5IXxRj1xckB9WRfDLCFt4S6P6HzKWT2IQaQk0SunuwtHXJl96-NlgIJRfmQEk7ZfCHNZCDB1WE5OIoS1YOCIpq5StO4h3ZWyvmEG1aRK49TGh1BGw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
👑
شیوه برخورد با آخوندها در زمان رضاشاه از زبان خمینی.
رضاشاه، روحت‌شاد
👑
@News_Hut</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/news_hut/69014" target="_blank">📅 16:15 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69013">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AFFq8iwLEObAHM8q1wPBi_cI98U87mKoaZ8R-j6DnsJWdy-SHMoDxbPHdyT1w1sZ1htWxt-gdSwGbLKox2axi6ES9Azbotkfbgi1GR2Tk6TEKSSsiLeSt1QVzyxvI9wkKZOqWDbDSquLdIAT9qtQvdskDa0BgrX1_Lwr3ib8vC9A7A_345X570LprImlXDHye3hoPq6wHxjSEwHiI_6nJEInDAvRouZaWJCmdFaOAAbkooTPAvTtUJYqJ2rO_76j0BRmgYoA7Z3x6TuwLIZPxpXVABr374kIfJ3Ulw5KuPInfBbomV_xLMp5lnnrPbvldX_S3ym_1HpzYoHGle3zTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
العربیه:
آمریکا و ایران به پیشنهاد مشترک پاکستان و قطر برای ازسرگیری مذاکرات، پاسخ داده‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/news_hut/69013" target="_blank">📅 15:33 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69012">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IWgo3aEyOahOaDEjDBYcTA61dnnCUqCY-xT1tMHNOVbKjbMFCRbN1CdQW_cQoLfjRVDwcq-gdUx9cndO1D0LUHD_wmHEfrgchUdOGRbbdgGe6i2XOYzk7FhlPzp4XefUEnHMaYgiM0479mHNiYb43qbVUdcIJ459Pg9dJ_e1Yyg087WYwcddjVtfUearGv8Z6Hb7Ww2MJ3Vm4_j92mL7D1kY9vqwLR4eX57yv7SekZ77KH_bUGLE2AO-j5kwVzdMhINT_O7GjLTHRvXqaEIGwh6Nc5J51p_iIZJpbqxZQuGeU5izgpYmHlJkUxytsebeG1Ko8jIA4F5BjEavWodDZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
امجد‌طاها روزنامه‌نگار عرب:
ترامپ حملات علیه رژیم جمهوری اسلامی را نه به دلیل مذاکرات، بلکه ظاهراً برای انتظار جهت برگزاری جلسه رهبران اسرائیل و دریافت آخرین تحولات از سوی آن‌ها، به تعویق انداخت.
این وقفه بیشتر به خریدن زمان شباهت دارد تا تغییر مسیر؛
تأخیر به معنای توقف نیست و آخر هفتهٔ پیشِ رو می‌تواند سرنوشت‌ساز باشد.
@News_Hut</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/news_hut/69012" target="_blank">📅 14:59 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69011">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3998a4eda0.mp4?token=bG-FaluzagSHUWBGexB0-P6qa2icEMDI0w6c5ljFqQyhw-EIne1rQF-bJpKh1v_FszClnvrLyjbf2ucVGEwlPOyyodwplvqWn6Ijxccyi2q2wQ9sVUGShoLvwLZ8IdnmoGkQz5uZnWEx0yHQMEEhtjmROBUIKYktp-jO4d1pbONCjxMI9O2wKpaa1ywkD9V8N-o-SVlsAq9FRZNMopGlv5NwU1s-IN0dleUEIkvo6xyoGI8ddOYsmz4I5gC_8_lDRoazsebQaQ-fVURuSQ80lS-Z_W5_PVL1RvIL_v79uSOoP1EFqD8Ark3IeaYcr_wVgkbX4SIBMSLkV2LQ5O_iJQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3998a4eda0.mp4?token=bG-FaluzagSHUWBGexB0-P6qa2icEMDI0w6c5ljFqQyhw-EIne1rQF-bJpKh1v_FszClnvrLyjbf2ucVGEwlPOyyodwplvqWn6Ijxccyi2q2wQ9sVUGShoLvwLZ8IdnmoGkQz5uZnWEx0yHQMEEhtjmROBUIKYktp-jO4d1pbONCjxMI9O2wKpaa1ywkD9V8N-o-SVlsAq9FRZNMopGlv5NwU1s-IN0dleUEIkvo6xyoGI8ddOYsmz4I5gC_8_lDRoazsebQaQ-fVURuSQ80lS-Z_W5_PVL1RvIL_v79uSOoP1EFqD8Ark3IeaYcr_wVgkbX4SIBMSLkV2LQ5O_iJQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇱
🇺🇸
نخست‌وزیر نتانیاهو:
فردا به دعوت پرزیدنت ترامپ به واشنگتن سفر خواهم کرد تا با او ملاقات کنم.
پس از آن، در مراسمی به افتخار یکی از دوستان بزرگ اسرائیل، سناتور لیندسی گراهام، شرکت خواهم کرد. باید بگویم که او از زمان تأسیس اسرائیل یکی از بزرگترین دوستان اسرائیل بوده است و شایسته است که این افتخار را به او بدهیم.
من با رئیس جمهور ترامپ ملاقات خواهم کرد تا در مورد تمام مسائلی که در حال حاضر در دستور کار است، از جمله وضعیت ایران، گفتگو کنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/news_hut/69011" target="_blank">📅 14:14 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69008">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/n5DTXNGXrrGtk5GsBVp7XUj4BeznQqY5v7v8nbNlyZUiz1yUqaDkli5jmRPlnnbN2tmqu2B1Y_lnMxNTXPE2ukxIxe3uT4ZUa5k6JHFTod8y887aAVuzeQIoS1esnS8r7567VhoPxciQdHrFXEQ-Owp4GhkqS_uANsrDZoKBEGDXymXKo2HgkyADmciWM8DV1N3y1jQOFn1g0O6EWM3Fq4HNqRvUlwoIcOFm5B15vOS8r0V54hAUeCzntOni4yn_WUOKu7dyaKv0gxhIWQm7yarF_c-cu8eXaYCIrySdYR4NWqIfSCIxJWA8uqy_3KTyKEyk9dVzwCuc1UYr1ayObQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/KjRP3qfMl7RiDkLFLGxclnWsMxi3vVVEMsqBPcJL9FJ41VlhrDYlViMooi7IPDjJVyAfWktzsg5QQtto9LWScFn-b7i4RlFVTT9ZgZu2WJSshAUIqB-Q8MZ4E8DzKO10c-ETOwUTNiEYCqQXEhBA8eg7SToz94K6fLQlEONbNkP1f8uVZIQzDUKkBEphtmpQXIlB-qqdw1o_jRxywYbRDgQ8x_gn-UTsOZ7074wv51qTaxse-sgcuqUFe-we8pKWkMeS_aVZXFf1oRwDzvYhZVGcz4FXSutFJzRKWTh_NiRBPE0OZuWMCqJXRYJGZYx012oXa-PZIfuYrLnusybp9w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/eb51b8cf9a.mp4?token=TyG5yIH2U_qrds89Dcwl8zOFdE3YjK1OEOkmBDhBc50X6CHS0s14QeJUXHw4-JjwGyIwQawTArUSNl-XReiNKEcC6QtvLEgbV-kbgDrliaRBoPbkewEtMoCqO3qIXlQSB-jkiLHDHxB5OtIFyMNtkAUNXiTgjyMsDRypLe5R0tn0CRkVqkTpora7rrpzH9vBEcJVWrn4vqtwa39DFFXmGlWP-zTklF9y6-9oeM67ZsVhK1sQ1d3wLwws1omxmwhDyOWwFLBSgZMva9scywCABwD3-IGLJIeTDZPt9Zu3xYS0Ua20wvn282l4AQS_JU1wtnmGvUcg0I1Q680nO0CRUg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/eb51b8cf9a.mp4?token=TyG5yIH2U_qrds89Dcwl8zOFdE3YjK1OEOkmBDhBc50X6CHS0s14QeJUXHw4-JjwGyIwQawTArUSNl-XReiNKEcC6QtvLEgbV-kbgDrliaRBoPbkewEtMoCqO3qIXlQSB-jkiLHDHxB5OtIFyMNtkAUNXiTgjyMsDRypLe5R0tn0CRkVqkTpora7rrpzH9vBEcJVWrn4vqtwa39DFFXmGlWP-zTklF9y6-9oeM67ZsVhK1sQ1d3wLwws1omxmwhDyOWwFLBSgZMva9scywCABwD3-IGLJIeTDZPt9Zu3xYS0Ua20wvn282l4AQS_JU1wtnmGvUcg0I1Q680nO0CRUg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👑
🤴
امروز ۴ ام مرداد، سالروز درگذشت رضا شاه بزرگ؛ بنیانگذار سلسله پهلویه.
@News_Hut</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/news_hut/69008" target="_blank">📅 13:47 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69007">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🇮🇷
محبی سخنگوی سپاه یه لیست از خسارت های آمریکا گفته:
⏺
در حوزه راداری و پدافندی:
۷ مرکز فرماندهی و کنترل
۳ سامانه ارتباط ماهواره‌ای
۶ رادار پدافندی پاتریوت (سامانه‌های پاتریوت به قدری ضعیف شده است که موشکها و پهپادهای ایران بدون رهگیری به هدف می‌خورند)
۳ رادار کنترل و مانیتورینگ هوایی و دریایی
۸ سامانه راداری کشف و اخطار اولیه
۷ رادار دفاع موشکی هوایی
۳ سامانه راداری EPS
۲ رادار EPS 117
۵ رادار برد بلند
۲ رادار پدافندی
۱ مجوعه راداری تاکتیکی
⏺
در حوزه پشتیبانی و لجستیک به منظور کاهش توان عملیاتی:
۶ مرکز تعمیر و نگهداری جنگنده و بالگرد
۳ مرکز پشتیانی و لجستیک
۱۲ مخزن سوخت
۱۷ انبار پشتیبانی تسلیحاتی و قطعات شناورها و هواگردها
۶ زاغه موشکی
⏺
در حوزه زیرساختهای عملیاتی:
۶ آشیانه پهپاد ام کیو ۹
یک سوله آماده سازی جنگنده اف ۱۵
یک سوله پهپادی که ۸ پهپاد آکبند در آن بود
۲ مرکز فرماندهی
یک سکوی سوخت‌گیری ناو هواپیمابر
یک آشیانه هواپیمای پی ۸
۴ سکوی موشکی هایمارس
۵ آشیانه جنگنده
۴ مجتمع پدافند پاتریوت
۶ سکوی پرتاب موشکی
یک ایستگاه پمپاژ سوخت
۲ مرکز مخابرات سیگنالی
یک مرکز داده‌های اطلاعاتی
یک مرکز هوش مصنوعی، پایگاه مرکز پردازش داده مربوط به شرکت آمازون
یک مرکز دپوی شمپاد (شناور مدیریت‌پذیر از دور)
یک اسکله سوخت
۴ شلتر جنگنده
۶ رمپ پرواز و توقف
⏺
در حوزه عملیات هوایی:
۱۱ هواپیمای جنگنده و بالگرد (روی زمین)
۱۷ پهپاد شناساییی و عملیاتی (۸ تا آکبند بودند)
یک هواپیمای جنگنده اف ۱۵ داخل شلتر
یک هواپیمای پی ۸
یک هواپیمای ترابری سی ۱۷
۸ هواپیمای سوخت رسان
۴ بالگرد سنگین
۶ موشک ذخیره
@News_Hut</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/news_hut/69007" target="_blank">📅 13:00 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69006">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">⏺
🇮🇷
بقایی، سخنگوی وزارت خارجه جمهوری اسلامی:
مقامات ایران و عمان در تهران گفتگوهای سازنده‌ای درباره تنگه هرمز انجام دادند و رایزنی‌های فنی و سیاسی در این خصوص همچنان ادامه دارد.
چندین دور گفتگو در روزهای جمعه و شنبه در سطح معاونان وزرای امور خارجه برگزار شد. در شرایط کنونی، هیچ تغییری در تردد کشتیرانی در تنگه هرمز ایجاد نشده است.
@News_Hut</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/news_hut/69006" target="_blank">📅 12:01 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69005">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🇺🇦
❌
🇷🇺
ویدیوی تعجب انگیز از داخل هواپیمای یاک-۵۲ که در آن تیراندازِ صندلی عقبِ اوکراینی، از کابینِ روباز با استفاده از تفنگ خود، پهپادهای گران (Geran) روسیه را سرنگون می‌کند.
@News_Hut</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/news_hut/69005" target="_blank">📅 11:15 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69004">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/739d5c9e05.mp4?token=mflHgfB_cysNLsKFazP2xZ5uHcz_XlnM2tEnxWaBR5RMDrCsVaPkAFCmOJjfKuRcJJPhUtIr8ZE4w1dj7Og3z45SjcQnIQvoScvZnBhKajlMOV4QNRfrr5s2u0GeqdjpRaHziEF4DH7_UL_NlhToCG2sWWVcv0j9TGNW2pIfa9JqFW3UvLf0hzojxe0fQUuuVWY95KqE2WLJnOpYStu9MODCOOo7asmE1bkvIaWzkP1t7tB9oPNSTUk3L5392GFGxD5C-ObdgrnM1EEgVvLISIiLS-mPpNuwtO9XxlKIo7HHWR0z9Gjn-hmWmsWB5VvKyQAAec71tajwi4tM7BXfLQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/739d5c9e05.mp4?token=mflHgfB_cysNLsKFazP2xZ5uHcz_XlnM2tEnxWaBR5RMDrCsVaPkAFCmOJjfKuRcJJPhUtIr8ZE4w1dj7Og3z45SjcQnIQvoScvZnBhKajlMOV4QNRfrr5s2u0GeqdjpRaHziEF4DH7_UL_NlhToCG2sWWVcv0j9TGNW2pIfa9JqFW3UvLf0hzojxe0fQUuuVWY95KqE2WLJnOpYStu9MODCOOo7asmE1bkvIaWzkP1t7tB9oPNSTUk3L5392GFGxD5C-ObdgrnM1EEgVvLISIiLS-mPpNuwtO9XxlKIo7HHWR0z9Gjn-hmWmsWB5VvKyQAAec71tajwi4tM7BXfLQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
🇮🇷
اکبراعلمی: مزد خدا بود و پاداش الهی بود که مجتبی انتخاب شد
😐
خدا امسال سه ماه قبل از قدیر ؛ قدیر رو برای ما نهادینه کرد و خدا برای ما مجتبی انتخاب کرد.
شهادت میدم والله خدا انتخاب کرد مجتبی رو.
با این انتخاب خدا کاری کرد نه نام خامنه ای نه راه خامنه ای تعطیل نشود‌.
@News_Hut</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/news_hut/69004" target="_blank">📅 10:34 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69003">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1efc7d4c9e.mp4?token=iyKthlQXwFuSvWVnajMlO17Au-SeXfbnHuR0cYrs4rK8nhkmR9L1--kmT_Q2Ue90ofEt1kYvdli5hzb5MdrdhawfU5ZKv95wLGs2XwYsaE898mc0O2YUGHEKyMQjB5NKTotjoh87VjNTiuu9Gq6KG6_48TAjodnBk6JKpWV_mEi9EfDnX_qSahG-2RMQOeLp1NGRhOmuBJnTcHnA5wM6Rr1buT2kNTjMUoNKdqqu3gZ_r-kpfolBKo6W8H78-6ZmvgSALTo82k17NGDpNxCNFOWR-T7aFqQWo8Vc5ivInsQG7yPpwNU42WnaaSKg-bS82Nd51pTornFmIH-oLMQKLw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1efc7d4c9e.mp4?token=iyKthlQXwFuSvWVnajMlO17Au-SeXfbnHuR0cYrs4rK8nhkmR9L1--kmT_Q2Ue90ofEt1kYvdli5hzb5MdrdhawfU5ZKv95wLGs2XwYsaE898mc0O2YUGHEKyMQjB5NKTotjoh87VjNTiuu9Gq6KG6_48TAjodnBk6JKpWV_mEi9EfDnX_qSahG-2RMQOeLp1NGRhOmuBJnTcHnA5wM6Rr1buT2kNTjMUoNKdqqu3gZ_r-kpfolBKo6W8H78-6ZmvgSALTo82k17NGDpNxCNFOWR-T7aFqQWo8Vc5ivInsQG7yPpwNU42WnaaSKg-bS82Nd51pTornFmIH-oLMQKLw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قبل از مرگ خاطرات آدم میاد جلو چشماش
من موقع مُردن:
@News_Hut</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/news_hut/69003" target="_blank">📅 10:02 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69002">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q7687Ipy1lqPAtOqLI6gVOiL0s3E_fYq7vTdA7xsbCaRugIBrq7vvSxdhxx__OX_PziAUZ8L9p2u2aG5-MQxFb3sqvyX3JpumNXoTdMid2WpzGhWWHQggptBz5oJVWjq80h2evgj2q0eScEqAT9dMI1_p2GchSfHcBqbhFoZTI4ljVM4PGcSqyLGgRzchOXhorvI_VqIcaxYny3NB6soA3x_y-o1eJGrIfZ2Pjm_upYlah60rc1_dNAuJ4GjxLnVYvTOeH2mWO7mXOIIHge8uA-i8bqYqOs8WmVpoQ0mnqRgLt96pZPVFgw9E0l4FFHIMzRUTsV9q38dUWQsvSkqhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
نیویورک پست:آمریکا طرحی را برای ربودن اورانیوم غنی‌شده از تأسیسات هسته‌ای ایران بررسی می‌کند.
نیروهای عملیات ویژه آمریکا در حال آماده‌باش هستند تا «پیچیده‌ترین عملیات تاریخ نظامی» را برای تصاحب اورانیوم غنی‌شده ایران از تأسیسات هسته‌ای به‌شدت مستحکم‌شده، به اجرا درآورند.
جوزف راجرز، معاون مرکز مطالعات استراتژیک و بین‌المللی، گفت: «گفتنش برایم ناخوشایند است، اما فکر می‌کنم محتمل‌ترین راه برای خلاص شدن از شر مواد هسته‌ای ایران — دست‌کم آنچه اکنون در اختیار دارند — یک عملیات نظامی است؛ زیرا مذاکرات پیشرفت سریعی ندارند.»
یک منبع آگاه از برنامه‌ریزی نظامی روز جمعه به واشنگتن پست گفت: این عملیات بسیار پیچیده شامل هزاران نیروی زمینی خواهد بود که به تأسیسات هسته‌ای ایران حمله می‌کنند - از تله‌های انفجاری عبور می‌کنند، از خدمه ساختمانی استفاده می‌کنند و یک نیروی دفاعی بزرگ را در اطراف این سایت‌ها حفظ می‌کنند.
به گفته آن فرد، از آنجا یک تیم کوچک از نیروهای عملیات ویژه، عملیات واقعیِ بازیابی را انجام می‌دادند؛ فرآیندی که «بسیار خطرناک» توصیف شده است.
این یک عملیات لجستیکی سنگین و دشوار در یک محیط رقابتی خواهد بود. ارتش ایران کاملاً نابود شده است، اما آنها هنوز از افرادی که از مادورو محافظت می‌کردند، پیشرفته‌تر هستند.
بر اساس گزارش رسانه مستقل و مطلع «های ساید» (The High Side)، این گروه از نیروهای عملیات ویژه می‌تواند شامل «اسکادران نقره‌ای» (Silver Squadron) از تیم ۶ یگان ویژه نیروی دریایی (SEAL Team 6)، گردان دوم تکاوران (Ranger Battalion) و گروهان ۲۱ مهمات ارتش باشد.
@News_Hut</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/news_hut/69002" target="_blank">📅 09:15 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69001">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G7WoGhRm-YM80UnFJTf8Kca4F_6rBG8cR5-iS7hOZhDpkLKbXRm-WZROLBBhK8q_sdUKTMbb_f_Libb34gnag0pjFQrC85YRvjmv-x_VdQnKrfCySA7g2Co6Bx70CY7pfCKQjP7kaLfKoZfUUOOP6d6nqYma6BfUfNWuPUCwGfYXR9gXwTz5b5p3RV1A6wbDGZsHmF1vBvHBoKXoeVo_VcUSExdUxWCuexMI959reSZgxMtmHWQcF4pSoHOk93vaeZ9rD7KLsIsuadEjKJTqcVFJegV0gQ_7BiEIfyOsx4I6n7JZFxZIiYCKkRcDisaM9dfxghIPcepBFOjqy23amg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
🇮🇱
رادیو و تلویزیون اسرائیل:
با وجود تعویق حمله آمریکا به ایران در روز جمعه، روند پیوسته ورود هواپیماها و تسلیحات آمریکایی به اسرائیل همچنان ادامه دارد.
آمادگی‌های نظامی آمریکا، حتی پس از لغو حمله برنامه‌ریزی‌شده برای شب گذشته، همچنان در جریان است. این تقویت قوای نظامی، بخشی از تلاش گسترده‌تر آمریکا برای حفظ فشار و در عین حال، تلاش برای بازگشت به میز مذاکره محسوب می‌شود.
در حال حاضر، حدود ۹۰ فروند هواپیمای سوخت‌رسان هوایی به همراه یک اسکادران از جنگنده‌ها در اسرائیل مستقر هستند. طی روزهای اخیر، محموله‌های تسلیحاتی و موشک‌های رهگیر بیشتری نیز وارد شده‌اند که یادآور تدارکات و آمادگی‌های پیشین است.
@News_Hut</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/news_hut/69001" target="_blank">📅 02:34 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69000">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eae9373361.mp4?token=cKlu_FP2vTVMmMzF6SDB-78GCFeT9M1eDdq0Z5k34HiKNK9LX5GqlgkjYkZIEfUr6JnP2ghYks3nCa25PiXmzplpVIvsNVHkMPLIXZofBvECY_2VX-ndS6GbziaE9ZjewhprANufPzC1Sq-27RobYFUlnU-2Bvcxi7ZWg5b37Gxx2Lx_FZaxJDBA0p1Tpr5DgpzOPR55dG3WiGyaldz7LU6oxMWD6xpMCnOSaym5SWUIsuWsenc7XDdW-ljOukGqyjN92ztbkNWVWWMxQMLUT75f5VbZv5ivITgSriUeYm6COVLiCxVPzJ53m0yNDL8Hgr7mMDXc959G0CIicg61-g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eae9373361.mp4?token=cKlu_FP2vTVMmMzF6SDB-78GCFeT9M1eDdq0Z5k34HiKNK9LX5GqlgkjYkZIEfUr6JnP2ghYks3nCa25PiXmzplpVIvsNVHkMPLIXZofBvECY_2VX-ndS6GbziaE9ZjewhprANufPzC1Sq-27RobYFUlnU-2Bvcxi7ZWg5b37Gxx2Lx_FZaxJDBA0p1Tpr5DgpzOPR55dG3WiGyaldz7LU6oxMWD6xpMCnOSaym5SWUIsuWsenc7XDdW-ljOukGqyjN92ztbkNWVWWMxQMLUT75f5VbZv5ivITgSriUeYm6COVLiCxVPzJ53m0yNDL8Hgr7mMDXc959G0CIicg61-g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تو خاورمیانه همه دارن هر شب در هم میذارن.
🇮🇷
واکنش عباس داوینچی:
@News_Hut</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/news_hut/69000" target="_blank">📅 02:10 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68999">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c262408b6b.mp4?token=A5RpxwvBrBJUkO_TOCU7bRLeYmiU09ZAgYY-SZRHwBD8GJiRjTqUhJCYDMAaUG74fnf4y0LNogEaVfVATqtDQffVWW1WsFX6jd6Hvn6fcpJ_ya-H4NAxbDe-y-N_TzQJuQ3l0t7ehoCTGV_qIVhz17qaiSYgFlWvvPvQSWRfNZgvzXhDxfgkohsurLH-d3Hf7dC_scyxzdle9drbZiBLYbqpkZu_XRBrDoxQ4WhT0LXY5APjX9e4llQHp5msOId6TVqeOXCawRTyRHnkXxyru7qw9nX5zZzDRfPhcC5xqM95SqyqaRRDtIqgrWEL2lsuktak4Q-TBfgKiooAtZaxdQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c262408b6b.mp4?token=A5RpxwvBrBJUkO_TOCU7bRLeYmiU09ZAgYY-SZRHwBD8GJiRjTqUhJCYDMAaUG74fnf4y0LNogEaVfVATqtDQffVWW1WsFX6jd6Hvn6fcpJ_ya-H4NAxbDe-y-N_TzQJuQ3l0t7ehoCTGV_qIVhz17qaiSYgFlWvvPvQSWRfNZgvzXhDxfgkohsurLH-d3Hf7dC_scyxzdle9drbZiBLYbqpkZu_XRBrDoxQ4WhT0LXY5APjX9e4llQHp5msOId6TVqeOXCawRTyRHnkXxyru7qw9nX5zZzDRfPhcC5xqM95SqyqaRRDtIqgrWEL2lsuktak4Q-TBfgKiooAtZaxdQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
فرماندهی مرکزی ایالات متحده:
محاصره دریایی ایران توسط ایالات متحده همچنان با تمام قوا در حال اجراست. تا تاریخ ۲۵ ژوئیه، فرماندهی مرکزی ایالات متحده (سنتکام) مسیر ۱۲ کشتی تجاری را که قصد عبور از این محاصره را داشتند تغییر داده، ۲ کشتی را که از دستورات پیروی نکردند از کار انداخته و برای اطمینان از رعایت کامل مقررات، وارد عرشه ۲ کشتی دیگر شده است.
پیش‌تر در روز جاری، نیروهای آمریکایی عملیات بازرسی و تأیید وضعیت را بر روی نفتکش «چارمینار» (Charminar) با پرچم کومور در دریای عرب به انجام رساندند و این نفتکش اکنون به مسیر خود ادامه می‌دهد.
نیروهای سنتکام در تاریخ ۲۴ ژوئیه، نفتکش «لاوین» (Lavine) با پرچم موزامبیک را در دریای عمان از کار انداختند؛ این اقدام پس از آن صورت گرفت که خدمه کشتی چندین بار تلاش کردند محاصره را نقض کنند و هشدارهای مکرر را نادیده گرفتند. این کشتی دیگر به سمت ایران حرکت نمی‌کند.
نیروهای آمریکایی همچنان بسیار هوشیار، متمرکز، مرگبار و آماده هستند.
@News_Hut</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/news_hut/68999" target="_blank">📅 01:05 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68998">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FpTPBjE5z_77Ts_Rk0FJcKJuQjsLR8ujm6DB38JfT06gjJhhCGcamScAf4P1HMeeNBlCRCF35P6AeG978YTjqr-5na9xLKIX9ZIDQtzK-jntmWhpkHiKWyPFqHwp_2cVUOjkjWNt5BVp8j59xhj5B1xvii785xqYHR2lLJDpL89VroAvBjfFrC250RYMphoiG_CjxMyFl7EbW5u0bh9hCFltEQdRNUOLP4DRx-dau8GA3KI--1G5MMZjwjFiIYy3z43x3VQz4ho08vaYvnJ-AfP6e-JBeCWYxXfNH-cL7yZmwjkpPyUOOF5WrShJgRd4iuotM8Pfp8ZdPFB31uopKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۷ فروند هواپیمای سوخت‌رسان آمریکایی هم‌اکنون بر فراز خاورمیانه در حال پرواز هستند.
@News_Hut</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/news_hut/68998" target="_blank">📅 00:45 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68997">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">🚨
اوکراین، یک کشتی متعلق به جمهوری اسلامی را در دریای خزر هدف قرار داد!
تاکنون مرگ یک ملوان در این حمله تایید می‌شود، رئیس جمهور اوکراین می‌گوید این کشتی حامل محموله نظامی بود.
@News_Hut</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/news_hut/68997" target="_blank">📅 23:50 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68996">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0101d071e9.mp4?token=LYyR9IF8vFnAIurc0Cly-F0rozH_S_-UfaxQKnv6ASB01F1s5qOwGZxmsyn0Unj6rXkYmXnbvpS1Zkz6MM5u1yBdEk1XlsouEKKmgfpVvQMrwJz2RV2u3TGGAEnkUfh9ijwrfCHMMu5_qB18sElTdh3JGoRD-s54bFH1mN_9dYN_iMbuAXO1ldINQM8Lc2_dv_G2_de1MzVkDol3-b-FgWXNHAC4wRdXpqus-2t4BTwwaVIg9YlkTf-S5tdSQ4wKxZExjqrZebBoCrZqnZPxuPjzP8dzDOhX3oAjEvkgB5r_5bmVMh-TBmexPQ06LUV-_xTIX50n7iVl76tzWAnNOQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0101d071e9.mp4?token=LYyR9IF8vFnAIurc0Cly-F0rozH_S_-UfaxQKnv6ASB01F1s5qOwGZxmsyn0Unj6rXkYmXnbvpS1Zkz6MM5u1yBdEk1XlsouEKKmgfpVvQMrwJz2RV2u3TGGAEnkUfh9ijwrfCHMMu5_qB18sElTdh3JGoRD-s54bFH1mN_9dYN_iMbuAXO1ldINQM8Lc2_dv_G2_de1MzVkDol3-b-FgWXNHAC4wRdXpqus-2t4BTwwaVIg9YlkTf-S5tdSQ4wKxZExjqrZebBoCrZqnZPxuPjzP8dzDOhX3oAjEvkgB5r_5bmVMh-TBmexPQ06LUV-_xTIX50n7iVl76tzWAnNOQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
پیروزمند:
تا کی قراره ایشون ( مجتبی خامنه‌ای) بیرون نیاد؟
🎙
مجری:
تا نابودی کامل عوامل جنگ.
⏺
پیروزمند:
خب اینطوری شاید ده سال دیگه طول کشید خب ما تا کی اماممونو نبینیم؟ اینطوری همیشه در موضع ضعف میمونیم.
@News_Hut</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/news_hut/68996" target="_blank">📅 22:50 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68995">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CYrXA5LUhmcMCn4Pk3bPF0CkyMvarcYYn72qCXfMJGBLxne30gmbZer4OrquQ0uxI2ujP_i7h1qDXfwuCcCEFL3fJnREjmxzsJCQo-b0Gq6pj3rh7zUu2LM3AhOfzMYd1Nt-heAA8mpISE4TCHL8_n2Ig6xEFcHKCLqZUsgt_r3Mb2Us26SnMTwkcFa6EVuGw3TAk-pE_nGPPVHctMsJZ2Pb7Se48U2AAUM5Cq8ErxodZoczbvDLf9rFUp1T_tplO1M4n6k24CCVcdTi3okUvqiJbN3Tu9y72hiyGn00HTr6pgv0l9waSE_nWZ88_rtp6sHeniWi-ceY0NLOCGN_kw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇺🇸
پرزیدنت ترامپ در گفتگوی تلفنی با شبکه فرانسوی «ال‌سی‌آی» (LCI):
اگر «صددرصدِ آنچه را می‌خواهیم به دست نیاوریم»، «قطعاً» گزینه ازسرگیری جنگ تمام‌عیار علیه ایران را مد نظر دارم.
@News_Hut</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/news_hut/68995" target="_blank">📅 21:48 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68994">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kBYbo2w6-WS2g5cQySPCa1yrV8Us4-vWFxH5L6GtlfHWJbIQg_zJ8K7MPMMdu6noZGqcHgQ9MjjZw-lFLYs8LFeoK7ssEuGtm03uTsx5KP16rh9B3WeiPZb-yz4R4rqr7oVTUD2Dqwf9cnxgnhyNeKfIil6O2nP4UNo0V6jLswj6x0KI7QMBfgmp1FAFPthZ9psxbeuaElvaK5kMddvBIij4xC3uvudNaIGW_F4I7ZsZFHio1ybkDCoq_SptNnb9CDti9-GQlXmiD4SOSBnITJjN6px8zMr7qmw78upXAanAuZx3j_G1bxed9WltUl-_MUrLeUvXurMiUz-t-KCHng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
اکسیوس:
رئیس جمهور ترامپ روز جمعه به ارتش ایالات متحده دستور داد حملات به ایران را متوقف کند و به تقریباً دو هفته حملات روزانه پایان داد.
این تصمیم در حالی گرفته شد که مقامات عمانی در تهران مذاکراتی داشتند و گزارش‌ها حاکی از پیشرفت در جهت توافق احتمالی برای بازگشایی تنگه هرمز است.
@News_Hut</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/news_hut/68994" target="_blank">📅 21:15 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68992">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PWIePyXZ5gHQJ0EgxaCjqkm2zAGfa5hJ0CLdM2wZDDncxIO0b_Qdmze31Rr4vR5TvSv6E3W1CGXKR_CkVDK4ADJGHDv8XRJIBqECJnlZnadm68u57TIHf04nyQAFt1177mA3y_mv7nNk-afZLa-bBqhrWQp0ad5WtiiUy8JJeFM6mjOUe4nQ3Bjujx5iQzEzK5ayJ7n5HtZwd1RAv0IrhimT-vrz5rWoj2wAngRRPy3jdU5etqhfg5XKchY6wIok4M0QajP6iWArQWcJBBsKD4bJJmAQ2Yklxtn5zezyEPkEYKI2ArMRAAnUixjsvYlGsZgco8ta4HGGUDmG9TNR2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d601f15a28.mp4?token=f8Wm_E7QM9VUwMG5aM5GWXjXtpu2K5JGMsDE0Y6Utidr1b0uyyOwn9r_26C60UPQrM7g3cmvd-Ok6lgp7cnJy5WtS_MgS9a4t-kCSOPe6IP-mDLsp8BsBrEVGCml-Pbfy5MEfhHz2ENMzXwcEHtpWr0HMDd7sF-uoaPzt0wXGqmaCD93eZJ5JDI68ETQW8UIx2FhdwNCNFPnBddrs0O83FUIOVTHXFKZMGW7f_QqD-nHsTEe6VWMyK9VrONNoo4fCatqLvfqoFiNktd1EqXaCrJxFkLkz_ScGfDJwIz4ViaEbc0QtzqTl9BVR4ABIKKxpaSNczL28uBDrf1n1asMkA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d601f15a28.mp4?token=f8Wm_E7QM9VUwMG5aM5GWXjXtpu2K5JGMsDE0Y6Utidr1b0uyyOwn9r_26C60UPQrM7g3cmvd-Ok6lgp7cnJy5WtS_MgS9a4t-kCSOPe6IP-mDLsp8BsBrEVGCml-Pbfy5MEfhHz2ENMzXwcEHtpWr0HMDd7sF-uoaPzt0wXGqmaCD93eZJ5JDI68ETQW8UIx2FhdwNCNFPnBddrs0O83FUIOVTHXFKZMGW7f_QqD-nHsTEe6VWMyK9VrONNoo4fCatqLvfqoFiNktd1EqXaCrJxFkLkz_ScGfDJwIz4ViaEbc0QtzqTl9BVR4ABIKKxpaSNczL28uBDrf1n1asMkA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💢
ساعاتی پیش یک هواپیمای آمریکایی در فرودگاه جده فرود آمده است. به نظر می‌رسد این هواپیما یک هواپیمای آواکس مدل E-3Sentryباشد.
@News_Hut</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/news_hut/68992" target="_blank">📅 20:29 · 03 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
