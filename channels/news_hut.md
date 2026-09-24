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
<img src="https://cdn4.telesco.pe/file/KVJmVVMvGxE_cIvCwsou34InN-tKimzrVg4jeze_6Z3DB2NGfPLzHAPoSlndf3vfKL6zIXWCHfIPh3QFeeI_yyGC6N3jB0_gh1rVdnS3EmufVZ4K2cVCK4CSJR5mUtLGZe_Uw4rT4KqkX8WJrEr5Ol7s5drh4jAh_odA9jJnekMGlNae0q9N4euogr3yTkAlg2Q7R6ZCC5pnYjhLLHjD26WnDKwUs0jirs_l0PpWrRxCaD1imNcDsfnHcqeSbhJLjdz629xi1hgDgx7mFBzq9uxcadwrIEJnDp_m8C-3q22Td0X7lj74pwAtH-GndMkyhgcDkMwJu8UbGyJYRZpmKg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 105K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-02 04:08:43</div>
<hr>

<div class="tg-post" id="msg-72155">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/72155" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 3.86K · <a href="https://t.me/news_hut/72155" target="_blank">📅 01:59 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72154">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dWBhKZ_QBQKomiZWBeNz0LmW4dWcDI6G9UWWYUY6GSuwcDOlziP-n5s1DraBSgWYGgsYho2I83ownXb5guY4mXLUaP2tBYx8RfUF9cF8Tms28s4dkL_4X3AQcAoz0FMCDzu99WK0_q8b-aL4pCoxwNULSkdx5mIOwQGqmvHUEgMQ5s9iLnxt5_K8RzK1oY6Nx8EGzqmEcgiCF2O8yrEEdYvZjjEghyxaBSPShmS6o3mCIFMsfWdjHTG1902uQ-UCqBdKAIfSuyPiJIeyfYNpx3JQUDhjCLcE25668mvWOs2_h1MFYG6CLm9RLAj-zhR574KGGvc-ot5_QfbvVUHzjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
فقط یک بازی از میکس‌ت لوز شده؟
پولت برمی‌گرده!
میکس می‌بندی، هیجان بالا میره، اما یکی از انتخاب‌هات خراب می‌شه؟
با پیشنهاد ویژه
TrexBet
، در صورت رعایت شرایط، می‌تونی
۱۰۰٪ مبلغ شرطت رو پس بگیری
.
همین الان وارد سایت شو و شرایط آسان‌ش رو مطالعه کن!
💰
🦖
🦖
🦖
🦖
🦖
بونوس صدرصدی اولین واریز
🦖
واریز آسان، برداشت سریع
🦖
سرعت بالا، طراحی حرفه ای و تجربه ای متفاوت
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 3.92K · <a href="https://t.me/news_hut/72154" target="_blank">📅 01:59 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72153">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5c59219ac7.mp4?token=qJd6XqSvRUNpMH-SPVz2oMWOoMZnDf3eNKQJzB2YM3VQVMnhFr9t-cyhGNFEGy8j-XAnwowj_hkyd6oY9-89vlT0dkZWQnuV4g2yAuJ5qmbEra7Mp89Qh6RgQlOQ3iHd4HtylelPSO7fqONuhnF6UWCA4M6Pla8SjchEsDza7TWtFgb65GCjCxahLt3asA2htMJuzbThI93gdHUT6aHWIkj_KHvyNKAyP-wf_sYcSCE8Ruw0Lo3WaC9V3bXpyxsbU0aw8eSV7HPysJVrpV099Rf0wis8yOYzQBoYfcMYFzUoQv2bF5wyhw-0Hk2s-UKU3Sg0LpSiXJt1cyyDmQhkXA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5c59219ac7.mp4?token=qJd6XqSvRUNpMH-SPVz2oMWOoMZnDf3eNKQJzB2YM3VQVMnhFr9t-cyhGNFEGy8j-XAnwowj_hkyd6oY9-89vlT0dkZWQnuV4g2yAuJ5qmbEra7Mp89Qh6RgQlOQ3iHd4HtylelPSO7fqONuhnF6UWCA4M6Pla8SjchEsDza7TWtFgb65GCjCxahLt3asA2htMJuzbThI93gdHUT6aHWIkj_KHvyNKAyP-wf_sYcSCE8Ruw0Lo3WaC9V3bXpyxsbU0aw8eSV7HPysJVrpV099Rf0wis8yOYzQBoYfcMYFzUoQv2bF5wyhw-0Hk2s-UKU3Sg0LpSiXJt1cyyDmQhkXA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یک فروند بمب‌افکن B-1 Lancer نیروی هوایی ایالات متحده، همزمان با استقبال پرزیدنت ترامپ از شی جین‌پینگ، رئیس‌جمهور چین، در واشنگتن، بر فراز این شهر پرواز کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 4.47K · <a href="https://t.me/news_hut/72153" target="_blank">📅 01:54 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72152">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1a5acb93e6.mp4?token=JoclJLIJySyKnrxy-QDSRZeOnLyyZ7WzyextMOOzBfs_2vDxoXZ5hZLU0T_QYA0RXXlqEg2NA5N3fhm1msFc3hOJ01f0vr5DA0K6pDcYkuXxsB8nvlKMMfi_JyMYmJxCtIzYjv9--36TbdKYUe9CiAA2G6PowHdM9MEpmcWFMqaZjn2aAc_4icQugi_mpZXv7d7isIpDH7j9nuva8AwU5CARMu5ICTIGutJ9PSauAMek6r5zcm8f3_0iYJ1Sv-_XNhsAx7EkEkzfhTAfYlh_KlTBuO-eTRW59YMA19TVCFAzI-dnJ9eF3xB6Injp8wHUlmwSDIw3hLall6DX_vwhvw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1a5acb93e6.mp4?token=JoclJLIJySyKnrxy-QDSRZeOnLyyZ7WzyextMOOzBfs_2vDxoXZ5hZLU0T_QYA0RXXlqEg2NA5N3fhm1msFc3hOJ01f0vr5DA0K6pDcYkuXxsB8nvlKMMfi_JyMYmJxCtIzYjv9--36TbdKYUe9CiAA2G6PowHdM9MEpmcWFMqaZjn2aAc_4icQugi_mpZXv7d7isIpDH7j9nuva8AwU5CARMu5ICTIGutJ9PSauAMek6r5zcm8f3_0iYJ1Sv-_XNhsAx7EkEkzfhTAfYlh_KlTBuO-eTRW59YMA19TVCFAzI-dnJ9eF3xB6Injp8wHUlmwSDIw3hLall6DX_vwhvw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شنیده شدن صدای تیراندازی در جهاد‌آباد سراوان
@News_Hut</div>
<div class="tg-footer">👁️ 5.08K · <a href="https://t.me/news_hut/72152" target="_blank">📅 01:48 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72151">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4470cff685.mp4?token=dH_HPuYGrAuijIlt5SpGMeUwnvKPLzTXVnffXsruilWyUbr2z0T8VQI2QTOcTW8RZNbhc-gSnMm8D4jP9ihPe-zng-1DjOxNUHxrx_Vp9pNxcrKpxqBhWm8Z-5CJ8JUUoPojpCgE1B4R1faod3FeuV49jAHZgtW1KlMNbv1_jwyeoDNvOl8vfH2Vw3R6Gfo7Xy4hgOTKEgVYTH56FDQOv0HUguwzzw6H9Flv4YzxXc9coM6uMSMfrHqoEAh3gq5011SwW2MRsdRPm_qUWXwwQvWjNl9AAQ6_K9t5QmqtdpkVAamogcHpY7KEDZrz192didh2MOPyYO6qKhi6VciKmg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4470cff685.mp4?token=dH_HPuYGrAuijIlt5SpGMeUwnvKPLzTXVnffXsruilWyUbr2z0T8VQI2QTOcTW8RZNbhc-gSnMm8D4jP9ihPe-zng-1DjOxNUHxrx_Vp9pNxcrKpxqBhWm8Z-5CJ8JUUoPojpCgE1B4R1faod3FeuV49jAHZgtW1KlMNbv1_jwyeoDNvOl8vfH2Vw3R6Gfo7Xy4hgOTKEgVYTH56FDQOv0HUguwzzw6H9Flv4YzxXc9coM6uMSMfrHqoEAh3gq5011SwW2MRsdRPm_qUWXwwQvWjNl9AAQ6_K9t5QmqtdpkVAamogcHpY7KEDZrz192didh2MOPyYO6qKhi6VciKmg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شی جین‌پینگ رئیس جمهور چین وارد ایالات متحده شد.
@News_Hut</div>
<div class="tg-footer">👁️ 6.06K · <a href="https://t.me/news_hut/72151" target="_blank">📅 01:34 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72150">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">رسانه‌ی حال‌وش :
دقایقی پیش تو محدوده‌ی جهادآبادِ سراوان تو سیستان و بلوچستان، درگیری مسلحانه‌ی سنگینی شکل گرفته به طوری که آرپی‌جی هم شلیک شده!
@News_Hut</div>
<div class="tg-footer">👁️ 6.97K · <a href="https://t.me/news_hut/72150" target="_blank">📅 01:25 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72147">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/d2cde76e35.mp4?token=GER1TuMtFghrH4wQ-cbWER4uUuZg5i_qtRJSvAoPJ1Zip6-ukseHf5688EkUO60r8ruuchHzgETS-DWRhkmnS3b1j7T8cRlozozZ_V_LOWWhvrYJCZKiAMWpyx-GabjqgRVAd0dX_TkMtqvAsTxA4DdkSN1P1QDzb020NMgnPzFYPs7JDmkFRLjzkr-w2ExQkycFqjzvdgIJaUY6t_es-EKdtz9pc8ZLepos4CXPVvlJr98Wdo0KsekHWmunmL6pjVxxjS4Q-aJQ9nI_9srXg9BJ9fpixN2YCzoqPneRm9ZF5jgpbSbww4zHdYPg3dO_bPR4hY6Dt-LCh4UM7qwC-w" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/d2cde76e35.mp4?token=GER1TuMtFghrH4wQ-cbWER4uUuZg5i_qtRJSvAoPJ1Zip6-ukseHf5688EkUO60r8ruuchHzgETS-DWRhkmnS3b1j7T8cRlozozZ_V_LOWWhvrYJCZKiAMWpyx-GabjqgRVAd0dX_TkMtqvAsTxA4DdkSN1P1QDzb020NMgnPzFYPs7JDmkFRLjzkr-w2ExQkycFqjzvdgIJaUY6t_es-EKdtz9pc8ZLepos4CXPVvlJr98Wdo0KsekHWmunmL6pjVxxjS4Q-aJQ9nI_9srXg9BJ9fpixN2YCzoqPneRm9ZF5jgpbSbww4zHdYPg3dO_bPR4hY6Dt-LCh4UM7qwC-w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">«اتحادیه دریانوردان هند» (Forward Seamen's Union of India) خبر مرگ یک دریانورد هندی را بر اثر حمله نیروی دریایی سپاه پاسداران با دو موشک کروز ضدکشتی به عرشه C و موتورخانه کشتی فله‌بر «MV CAPE DAO» اعلام کرد.
کشتی «MV CAPE DAO» متعلق به شرکت «ForthMarin Corp Ltd» است که در امارات متحده عربی مستقر می‌باشد.
@News_Hut</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/news_hut/72147" target="_blank">📅 23:35 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72146">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Rp28E_J__NrOIiiZvkXUHr7YD5I2oiV4qrIYWVBeTLKOr8wJSfQXY0bykeex0Mo2qhjphzLgznT5DxsCadps-RMdDYpDdHPwSnuXgYV8TiBLxzOnsmQ5ZVFTtudP2-WBYxNjGipeEOCU-g157feGzfdEZmJVQKbRpu7gtFdx1cZ6GOruWJ6BrwHRFlNkMERSbzUfn_QVBqgmEyuCYux79eoPJmOHkpYfQAcbvBvbRdTw8NGv8jYY5FCQAj-MhmqylFvM6vEJ84aDFE5fOXxOK__9bS6NyViO8LZFi7P4F5Tp2lzpq8QMOWWZM1Mx0HmN8joNBK5TnpavPWfmJGm-pw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سردار ظریفی فرمانده سپاه شهرستان سراوانِ سیستان و بلوچستان، توسط افراد مسلح ناشناس کشته شد
@News_Hut</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/news_hut/72146" target="_blank">📅 23:02 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72145">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/223e8fa625.mp4?token=uKTPb8sLwm2wzLev0EklKdPjcN2EaUqRfsHNLspVpVeR1JTmwa2Axw7X0rIHGxkbVbLLOW6NAkvFQUpCt9bsPkeyI0aZmkynEz1N9tNgD2LRVWYnMJXOJplo_rf0eTl7jWDPSXAMrMDpi-CUPH0rfD1DvGEphh9iVDJIGet7w5NofgWKvW7BcrGNqRSRicr29CKFieK914nz-P1riMHaUhtuqMi6O_b_Zs7XkZUi1eatC6J6v5Ezph2L-NXOn-Em3lqjCHfV9WWvS0ts4evC7qwpprDq-bFwm89cmUKNiXDypkTrs3rUzIBRQbh9UoG3YhXrDt3EuD1V52zcYa2vZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/223e8fa625.mp4?token=uKTPb8sLwm2wzLev0EklKdPjcN2EaUqRfsHNLspVpVeR1JTmwa2Axw7X0rIHGxkbVbLLOW6NAkvFQUpCt9bsPkeyI0aZmkynEz1N9tNgD2LRVWYnMJXOJplo_rf0eTl7jWDPSXAMrMDpi-CUPH0rfD1DvGEphh9iVDJIGet7w5NofgWKvW7BcrGNqRSRicr29CKFieK914nz-P1riMHaUhtuqMi6O_b_Zs7XkZUi1eatC6J6v5Ezph2L-NXOn-Em3lqjCHfV9WWvS0ts4evC7qwpprDq-bFwm89cmUKNiXDypkTrs3rUzIBRQbh9UoG3YhXrDt3EuD1V52zcYa2vZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خواننده رپ آرمین رابر، برگزار کننده میتینگ های خیابانی رپ در اطراف تهران بازداشت شده است. او پیش تر نیز به دلیل اجرای قطعه آقازاده بازداشت و به حبس و جریمه نقدی محکوم شده بود...
@News_Hut</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/news_hut/72145" target="_blank">📅 22:15 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72144">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">تسنیم گرفت رو عراقچی:
تعامل عباس عراقچی، وزیر امور خارجه، با استیو ویتکاف، نماینده آمریکا، بدون مجوز یا هماهنگی با مقامات ذی‌ربط ایرانی، از جمله شورای عالی امنیت ملی، صورت گرفته است.
ادعاهایی مبنی بر اینکه این تعامل از پیش به تأیید نهادهای سیاست‌گذار ایران رسیده بوده، نادرست است.
بر این اساس ضروری است که آقای عراقچی درباره این اقدام غلط که مخالف مصالح و‌ منافع ملی است به نهادهای مربوط و ملت ایران پاسخگو باشد که با چه محاسبه‌ای این خطای بزرگ را مرتکب شده است.
@News_Hut</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/news_hut/72144" target="_blank">📅 20:47 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72143">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1d86a283f5.mp4?token=hoMFc582Lc5UqUg6oy_zrPi9gEuh4XyynJUeK1zS62dceXX15n60-3FDA2DMpha-An5aTCCuD8NUOoWq8vrYHsnQkesAXCGP3_tWZxlMYgADy-DlcdzQhSQlFzncj-xnr-td7LBjZa0Mahl4dKKZ6G3ArlmwlkKVYQiCWXPCfy3qw6n9GLLe_dY-0u3ItZJVwgO-6aA8d8m98vxesBR7J55kudxX4It11oAotpNnbwKCZk0SNKbuRhYfG-CcR1HuRGXuDkisNy-TcLMCSfA0gw3r1Hee6p82zWbafXN_27gHEXvZo3jETKeTGd4TaWsdCT76foKEByTR4fqHmbJ5bA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1d86a283f5.mp4?token=hoMFc582Lc5UqUg6oy_zrPi9gEuh4XyynJUeK1zS62dceXX15n60-3FDA2DMpha-An5aTCCuD8NUOoWq8vrYHsnQkesAXCGP3_tWZxlMYgADy-DlcdzQhSQlFzncj-xnr-td7LBjZa0Mahl4dKKZ6G3ArlmwlkKVYQiCWXPCfy3qw6n9GLLe_dY-0u3ItZJVwgO-6aA8d8m98vxesBR7J55kudxX4It11oAotpNnbwKCZk0SNKbuRhYfG-CcR1HuRGXuDkisNy-TcLMCSfA0gw3r1Hee6p82zWbafXN_27gHEXvZo3jETKeTGd4TaWsdCT76foKEByTR4fqHmbJ5bA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پنتاگون ۶ مورد دیگر از فایل هایی که در آن اشیا پرنده و ناشناس به اصطلاح UFO دیده میشه رو منتشر کرد که دو مورد اولی در خاورمیانه ثبت شده هست.
@News_Hut</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/news_hut/72143" target="_blank">📅 20:37 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72142">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9819ac349a.mp4?token=LYffGtNxJCH9xFu8xlhBENBVsEKLRy4JOf7L6qLcibbhaeZyzzf-qFC3zq3chfYEMtRkiwDSragm7J-I4TKVo8eiIULgoWv-Pd2cPWH37tlr05Kl1gPhyyY22Kp6w8NUyDmsImGyFEIE9O_BCatPejRtV7jZchOgVhDoR2FQTuDbl87WeZUkgLEGiXWJSJhD36RiZ1Rr3Ttw-JIFZGXrfzEg047NXljArdtX5C40BDuUE5H87glYQVml9SZjgxouddTt4G_sOU0iIGs9-0vXYDc7n1J2nvD0-AZvK1swDsHRUHqN0XO_MfmfYdBrsVsGKzf6nSoYVps1XsXFyqtuNIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9819ac349a.mp4?token=LYffGtNxJCH9xFu8xlhBENBVsEKLRy4JOf7L6qLcibbhaeZyzzf-qFC3zq3chfYEMtRkiwDSragm7J-I4TKVo8eiIULgoWv-Pd2cPWH37tlr05Kl1gPhyyY22Kp6w8NUyDmsImGyFEIE9O_BCatPejRtV7jZchOgVhDoR2FQTuDbl87WeZUkgLEGiXWJSJhD36RiZ1Rr3Ttw-JIFZGXrfzEg047NXljArdtX5C40BDuUE5H87glYQVml9SZjgxouddTt4G_sOU0iIGs9-0vXYDc7n1J2nvD0-AZvK1swDsHRUHqN0XO_MfmfYdBrsVsGKzf6nSoYVps1XsXFyqtuNIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یکی از هموطن‌ها رفته یه مرسدس بنز خریده؛
همه منتظر بودن از خریدش ذوق کنه ولی صحبت‌هایی که بعدش کرد، جالب بود :
@News_Hut</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/news_hut/72142" target="_blank">📅 20:37 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72141">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">اگه هنوز دنبال یه کانال و گروهِ «واقعی» برای پیش‌بینی می‌گردی، درست اومدی!
👑
✅
تحلیل‌های اختصاصی و رایگان
✅
ضریب‌های طلایی
✅
گروهِ فعال برای تبادل نظر  وقتت رو با کانال‌های فیک تلف نکن. حرفه‌ای شو و با ما همراه باش.
👇
[لینک کانال] https://t.me/+fyrt-rnxFjNjMmQ0…</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/news_hut/72141" target="_blank">📅 20:36 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72140">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EYLbhtuH7M8iwb5CHV9-E0RlWzy-Qld76KPv-mg6YXuEaDx7RGNvIdyv620zwV11a0mxmCPOLKxxXgd44AGmeT0k1o2vaj03i9-gUmG7QZcKrn7Z9Q_5CB4-6M_x4ApKD2yNIWt-W4_UMIEtZMXrI0Suc_Q8528uzGpEU-H7jdvuW4BdiILUaek0i6RYTaQsNh-bMybNbj8wihkg7bmpuPVmVMZTOI9N6uFxAX3x5Af4qoU1RSLLBtjzgZYLMQWpQTTJScZP0uNOE1PS98Jdb_3HDEFJWQNxwY6lmvQJi4Cl2a9TqJyFAdcdx3AkeGUq3fWpiIY-1EgcEraABX4n_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگه هنوز دنبال یه کانال و گروهِ «واقعی» برای پیش‌بینی می‌گردی، درست اومدی!
👑
✅
تحلیل‌های اختصاصی و رایگان
✅
ضریب‌های طلایی
✅
گروهِ فعال برای تبادل نظر
وقتت رو با کانال‌های فیک تلف نکن. حرفه‌ای شو و با ما همراه باش.
👇
[
لینک کانال]
https://t.me/+fyrt-rnxFjNjMmQ0
[
لینک گروه
]
https://t.me/+jpSLBx8PcgBlMWI0
#TipsterPersian
#سود_تضمینی
#شرط_بندی_فوتبال
»</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/news_hut/72140" target="_blank">📅 20:36 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72139">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8fa977cc40.mp4?token=H0rRRxVG5ndWb_ZYG0UlmxOpcQBUd_BnsD9WupEtx1E2BsDyo0KiyWYpdvtoWs7tRKDbVyrnTyCzjo1tTVxN4aMo5zedgBJPqO3uAB__8CTzM80iuzGbkho6PB0DYdU_Fcp1uhhTMjEvApXxdj5-D54MFyqo9n8AxeaOfOFuBXsi7k_-wztLMcTl-_X0oyagIULvuT1uEVUHqtnshvbAQiYltSeUwi1J0l6pYMsaQj0WYApXGQjhOXwtuloXjj9ID4q_fUf0G7ZHrXluZ8YnVpWTusWImHPEaeQoIICYGrhr6zKhm-2rTFyHmI8MqwuhqZbfe2C3t6fw5oWbQoS2JQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8fa977cc40.mp4?token=H0rRRxVG5ndWb_ZYG0UlmxOpcQBUd_BnsD9WupEtx1E2BsDyo0KiyWYpdvtoWs7tRKDbVyrnTyCzjo1tTVxN4aMo5zedgBJPqO3uAB__8CTzM80iuzGbkho6PB0DYdU_Fcp1uhhTMjEvApXxdj5-D54MFyqo9n8AxeaOfOFuBXsi7k_-wztLMcTl-_X0oyagIULvuT1uEVUHqtnshvbAQiYltSeUwi1J0l6pYMsaQj0WYApXGQjhOXwtuloXjj9ID4q_fUf0G7ZHrXluZ8YnVpWTusWImHPEaeQoIICYGrhr6zKhm-2rTFyHmI8MqwuhqZbfe2C3t6fw5oWbQoS2JQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انتظار می‌رود سخنرانی نتانیاهو در سازمان ملل به شدت بر ایران متمرکز باشد و به گفته‌ی ایدز، این سخنرانی حاوی «غافلگیری‌های» نامشخصی خواهد بود.</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/news_hut/72139" target="_blank">📅 20:29 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72138">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">پزشکیان:
تو منطقه هیچ کشوری به تنهایی امنیت نخواهد داشت، یا باهم امنیت رو می‌سازیم یا باهم تو ناامنی زندگی می‌کنیم!
@News_Hut</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/news_hut/72138" target="_blank">📅 20:23 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72137">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/15be798879.mp4?token=MkL48lL5k60hV9Q12H6IpKA2606Jp8VDyA0Sik5FOr4gBB_BUODqL55Ib0hgJLmYUktXF4I6l3LRAgx1qbDZBIqMMrYZWD5stAulh06D8HK_C5v88aFCcdx37IbdTXiGR_mMzIYaqMQw2BqR1pDOvuU1IYsEobxZ3pNndv3A6fJ79oH9zoIIvf1Rsq_0UdNwKB9sg4Y5FKMcHNfsEkwos-RHcmhE56PCADyc-7Gp9-_0vaFu1N0Px1qUEnARGv6PkZjO9zguwVn-BSQe7AHZjwRS9mDU96zKTziFm52um2lbzVNNvTLl2Z2QCJwGu4xS6mOS-Whc4tFZt2T6iJNRdQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/15be798879.mp4?token=MkL48lL5k60hV9Q12H6IpKA2606Jp8VDyA0Sik5FOr4gBB_BUODqL55Ib0hgJLmYUktXF4I6l3LRAgx1qbDZBIqMMrYZWD5stAulh06D8HK_C5v88aFCcdx37IbdTXiGR_mMzIYaqMQw2BqR1pDOvuU1IYsEobxZ3pNndv3A6fJ79oH9zoIIvf1Rsq_0UdNwKB9sg4Y5FKMcHNfsEkwos-RHcmhE56PCADyc-7Gp9-_0vaFu1N0Px1qUEnARGv6PkZjO9zguwVn-BSQe7AHZjwRS9mDU96zKTziFm52um2lbzVNNvTLl2Z2QCJwGu4xS6mOS-Whc4tFZt2T6iJNRdQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این خانم معلم قبل از شروع مدارس، برگشته به اولیای دانش‌آموزا میگه؛
بعضی از دانش‌آموزا هستن که پدر، مادر یا هر دو رو ندارن ؛
پس وقتی میاید بچه‌تون رو از مدرسه بردارید انقد قربون صدقه‌ش نرید که دل اون بچه یتیم بشکنه، برید یه جای خلوت‌تر بهش ابراز محبت کنید
@News_Hut</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/news_hut/72137" target="_blank">📅 20:15 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72136">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/bcb578f315.mp4?token=laK-Dz9J7sg8MCR6jEgClvPX0cIgJiEQlP5R5udyNux2Lwwk5K09jneX0VkM3FbV2PFHkg1k-gWLn5qHvKEtbFSS3Xt0LOMqjbuUEWcfrDUFYNPUEhJcPxFwnIkHiEhR3pl_ouC8Sn5lPUlBJISwSL6bBkGBgTghIn5eK6rqvzcw3MefAOIykF6HC-w57akx3f3HkJXfv6b4lus_L340UaUrMPGOQUjPLL00-fhG_uheG8mHRXNwPLPwr_zPR9CSxrs7Bj3CUwxHu-lrNOQWhmQbP5SNwEPQSWIduyo-4n8aOcWvY-LLiJl1qkjpYnntMYrkWCNekbmk_t48GV0Q4A" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/bcb578f315.mp4?token=laK-Dz9J7sg8MCR6jEgClvPX0cIgJiEQlP5R5udyNux2Lwwk5K09jneX0VkM3FbV2PFHkg1k-gWLn5qHvKEtbFSS3Xt0LOMqjbuUEWcfrDUFYNPUEhJcPxFwnIkHiEhR3pl_ouC8Sn5lPUlBJISwSL6bBkGBgTghIn5eK6rqvzcw3MefAOIykF6HC-w57akx3f3HkJXfv6b4lus_L340UaUrMPGOQUjPLL00-fhG_uheG8mHRXNwPLPwr_zPR9CSxrs7Bj3CUwxHu-lrNOQWhmQbP5SNwEPQSWIduyo-4n8aOcWvY-LLiJl1qkjpYnntMYrkWCNekbmk_t48GV0Q4A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یه زنه با شوهرش رفته بود خرید که شوهرش این حرکتو زد و آبرو برای زنش نذاشت :))
@News_Hut</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/news_hut/72136" target="_blank">📅 19:33 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72135">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ff0aa24390.mp4?token=kYjqYW4iGaKT2gSWiX-_Z07vntpo8MEsjsiXD4VzyOJHjX9lcE9DlH6fTtkbPkTxXei-wAZ-hOCDsRYHZq-TtuFwysR2UM_wjwZQziGz4zr_Acqc99pxDthzNyvR15v6ceD81CpjHPhDKBHg-h_wzFTlJB7VY7oGCbfCf3XyzyLkLxZO-9EQwD89YK9XDJHI5nmYJKY7LTlJj1cfPQeGmB0JqggZMsGnxkr5eB_ZSS7_Q0h0oZLhedbosfbke5nUG4caEC6EXx1xwp9nk0xGJAKKIv25uzmNpOsHtryT9CeiiiYknxZUYlfB8PUnlda3BgmMvuOhtXtynGChz5Ns9g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ff0aa24390.mp4?token=kYjqYW4iGaKT2gSWiX-_Z07vntpo8MEsjsiXD4VzyOJHjX9lcE9DlH6fTtkbPkTxXei-wAZ-hOCDsRYHZq-TtuFwysR2UM_wjwZQziGz4zr_Acqc99pxDthzNyvR15v6ceD81CpjHPhDKBHg-h_wzFTlJB7VY7oGCbfCf3XyzyLkLxZO-9EQwD89YK9XDJHI5nmYJKY7LTlJj1cfPQeGmB0JqggZMsGnxkr5eB_ZSS7_Q0h0oZLhedbosfbke5nUG4caEC6EXx1xwp9nk0xGJAKKIv25uzmNpOsHtryT9CeiiiYknxZUYlfB8PUnlda3BgmMvuOhtXtynGChz5Ns9g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مسعود پزشکیان:
آقای ترامپ و کسانی که به دنبال زورگویی به ما هستند، باید ایران را بشناسند:
اینکه ما آماده گفتگو، دیپلماسی و مذاکره هستیم، اما زبان زور را نمی‌پذیریم.
@News_Hut</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/news_hut/72135" target="_blank">📅 18:29 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72134">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a80dd97167.mp4?token=r4whk5DPI0lGQexs0KJI2CCD-peSfJs9XsHjjDNtVpl3tcjC8B4qnhMOfg4Kh8j212KC3F1SMbVTkloz2Il8gy8Uk8KRnxJl5BcKYxdlcVnj1rj9dBr0pXcVupYn24lEF5cfqeRjhf9HGnrz6nSKS1u9lrJfsLZ_mZzTraKM67m_jl403Tq4Gsex7p_XHSHHxEFZ9DXSSseI-q_jSEBuL-eZIln_pnTuEsho2_IpkYcELnAGJt_53CGwdHWNLkmVTz3kSPGDJ82XY2goEz7uS9wyValMj6DFzABVPlcmYW9wgFevxfYmDdPrw-VJeoCbnEuL2QhOv9Mxmuvr8QN7zw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a80dd97167.mp4?token=r4whk5DPI0lGQexs0KJI2CCD-peSfJs9XsHjjDNtVpl3tcjC8B4qnhMOfg4Kh8j212KC3F1SMbVTkloz2Il8gy8Uk8KRnxJl5BcKYxdlcVnj1rj9dBr0pXcVupYn24lEF5cfqeRjhf9HGnrz6nSKS1u9lrJfsLZ_mZzTraKM67m_jl403Tq4Gsex7p_XHSHHxEFZ9DXSSseI-q_jSEBuL-eZIln_pnTuEsho2_IpkYcELnAGJt_53CGwdHWNLkmVTz3kSPGDJ82XY2goEz7uS9wyValMj6DFzABVPlcmYW9wgFevxfYmDdPrw-VJeoCbnEuL2QhOv9Mxmuvr8QN7zw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پزشکیان:
ترامپ باید بداند که مقاومت ملت ایران در برابر تحریم‌ها، افزایش فشارها و زورگویی‌ها، تنها بیشتر خواهد شد.
ما هرگز سر فرود نخواهیم آورد و زانو نخواهیم زد.
@News_Hut</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/news_hut/72134" target="_blank">📅 18:28 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72133">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">مسعود پزشکیان:
بمب‌های اتمی و هسته‌ای در اختیار رژیم اسرائیل است، اما از بازرسان خواسته می‌شود که به ایران بیایند.
اسرائیل بیش از ۷۰ هزار انسان بی‌گناه را در غزه به شکلی وحشیانه به قتل رسانده است، اما ایران در حالی که پای میز مذاکره بود، هدف بمباران قرار گرفت.
اسرائیل بمب و سلاح‌های کشتار جمعی در اختیار دارد، عضو «پیمان منع گسترش سلاح‌های هسته‌ای» (NPT) نیست و در طول حیات ننگین خود حتی اجازه یک مورد بازرسی را هم نداده است؛ با این حال، همه امکانات لازم در اختیارش قرار می‌گیرد تا بتواند هر پایتختی در منطقه را که بخواهد، بمباران کند.
@News_Hut</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/news_hut/72133" target="_blank">📅 18:10 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72132">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ff7f87b6f9.mp4?token=DlGruuGYxRtTgFdV4-1mGciYUNEPGpN15P_UOEzL3gL3DTstlwUCspyPlRF_X2_YYNdc4F-Ty_-N4sMYReWhrQOkEBAsKgfwKnrQKbRXPB0gksWe6976I12N27G41-rJDa_vSrgZ5gtywlNXkMeFkET9R479jOtGa09JOkotMRIWO6hEpJNBg5o-3oDSA5m2BVpyB51RqMZPxnYLzv8x9Pd0ntF71wS9yBpIBQ_taOy1ULxVg9Yu78YCUcLj9sliSH8927JJSG9616QyocHK8AeQRt6WLX6MbKoaTd34QwIgiIzK39AltMQaoJcC7pNA3oLfRODbJPmVQJfZv2inbYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ff7f87b6f9.mp4?token=DlGruuGYxRtTgFdV4-1mGciYUNEPGpN15P_UOEzL3gL3DTstlwUCspyPlRF_X2_YYNdc4F-Ty_-N4sMYReWhrQOkEBAsKgfwKnrQKbRXPB0gksWe6976I12N27G41-rJDa_vSrgZ5gtywlNXkMeFkET9R479jOtGa09JOkotMRIWO6hEpJNBg5o-3oDSA5m2BVpyB51RqMZPxnYLzv8x9Pd0ntF71wS9yBpIBQ_taOy1ULxVg9Yu78YCUcLj9sliSH8927JJSG9616QyocHK8AeQRt6WLX6MbKoaTd34QwIgiIzK39AltMQaoJcC7pNA3oLfRODbJPmVQJfZv2inbYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مسعود پزشکیان:
مسائل منطقه‌ای ما باید در درون منطقه و به دست کشورهای منطقه حل‌وفصل شود، بدون آنکه به ابزاری در دست متجاوزان خارجی بدل گردد.
هیچ‌گونه رابطه‌ای با یک قدرت خارجی نباید به ابزاری برای تهدید کشورهای همسایه در منطقه تبدیل شود.
@News_Hut</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/news_hut/72132" target="_blank">📅 18:03 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72131">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4be5f428e4.mp4?token=DOa2DSnRBVx4zawXnqgEe7nKA77RMcc-Tk-PusN30X-86G8nsq8ObowD-IreeretwjttzTnMyG5iTobYW2qlVRkdOpo7Uoq1uAaDo0nOOC5CZP4vrsTiVNd-GDXWo-zaNl1xc18gr9ZpagKoYW9IDztLJaAvOLxtv3Lph6D90VBdOL2wHbB9awUBOjzV8lHYSr-32VnioOlx4mA7nIP1ZtP2GoP2UyK7Rn88quQ8BR6S17kH_DEr1qA9xUPmQYc7tb1zl9Zpgy81bJcUN8KDwZ0VoBUp3bZ3H1xXIUi3pQS87VacuDRWhab2xYOtjaLBphQzSmAnzisidepqDMadAgmVYGoC9d8wC3JbR10-NNtdZ9MCagNM-FYoLajM_qq2sAqWtTkKCw5NmpurM86IvA2oMJBSyJyryRXeiInFUIZBH4xX43BHa1Zr8cwXyzzw0I8nUz95LGZHOXSHwh5HxOWzQJRVOYI9MBbT7y67eOO4zGiYlmesDtQ9cA10eg0AceptRoSKGHzJj8tq8y1IfWmxpmZXK5r6iIBIwjyeXW_7bYKeuPeWcvxbx1hv1-s-HMjqgkxgs8zGeRfnN0gtAoxBdklaxpGAts73FFkki1Wq-Ntdc9f3E1YkIE9WWsOpiT4pb1rYUXXhGAO1RJMrVL4m7Xi1Il2aS-WaV7qm3lk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4be5f428e4.mp4?token=DOa2DSnRBVx4zawXnqgEe7nKA77RMcc-Tk-PusN30X-86G8nsq8ObowD-IreeretwjttzTnMyG5iTobYW2qlVRkdOpo7Uoq1uAaDo0nOOC5CZP4vrsTiVNd-GDXWo-zaNl1xc18gr9ZpagKoYW9IDztLJaAvOLxtv3Lph6D90VBdOL2wHbB9awUBOjzV8lHYSr-32VnioOlx4mA7nIP1ZtP2GoP2UyK7Rn88quQ8BR6S17kH_DEr1qA9xUPmQYc7tb1zl9Zpgy81bJcUN8KDwZ0VoBUp3bZ3H1xXIUi3pQS87VacuDRWhab2xYOtjaLBphQzSmAnzisidepqDMadAgmVYGoC9d8wC3JbR10-NNtdZ9MCagNM-FYoLajM_qq2sAqWtTkKCw5NmpurM86IvA2oMJBSyJyryRXeiInFUIZBH4xX43BHa1Zr8cwXyzzw0I8nUz95LGZHOXSHwh5HxOWzQJRVOYI9MBbT7y67eOO4zGiYlmesDtQ9cA10eg0AceptRoSKGHzJj8tq8y1IfWmxpmZXK5r6iIBIwjyeXW_7bYKeuPeWcvxbx1hv1-s-HMjqgkxgs8zGeRfnN0gtAoxBdklaxpGAts73FFkki1Wq-Ntdc9f3E1YkIE9WWsOpiT4pb1rYUXXhGAO1RJMrVL4m7Xi1Il2aS-WaV7qm3lk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مسعود پزشکیان:
ما سر خم نخواهیم کرد و از حقی که ذاتاً متعلق به ماست، دست نخواهیم کشید.
صریح می‌گوییم: نه سلاح هسته‌ای و نه هیچ‌گونه محدودیتی برای فناوری صلح‌آمیز هسته‌ای.
@News_Hut</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/news_hut/72131" target="_blank">📅 17:58 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72130">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2213909800.mp4?token=bD6yq27gDQ8OM3UDuud_314V2IsyzJOArxAAwXzs_3OX9dOUdUw98dRaSrCYWC62mPdiLC6-5kM6vJewGFszARJc2zUp-sD1UYWfNyq-4UwYNIIwb25SCySZ5MigiOP86nJhT5tzzrTJwBC968RNCL41HlpkDL41fP4s8E114cHFPOJCzjwIMWNeyh-DHWnXxvxgNr7FQxYYwrZaCjkWUGU_8dosb8r7_xBCqCyhMLy-BTCY0VnZDq-NG8AKXVyrXb9gJ_cSGBoqMA7Mf9KWgwPF0f4mWHto_GQ5lxgfhIeGT9fgyq293ihEWIW1tGZyuHclro3W9ZHMifjeBM8hYlh3woes6oNZdas-avMwy1TxZE2kAIbAujL6rQmDV4FMg3G7uvgFzFfr9GEWjxkSo_Gwbb_TyZAlffKYt8JsuMjOzefprZbCBVJ6_nEVkv8UZujKCHcOKHi59dG2lGhxjb8tySodIH6y663YH6Jol-m4q33BMlXMgqXqLsgdIglh4T0IHfnukEl7KBkUx4XklaJPL6UzW_tOGzTEo-ilJ0zusgOdql49J5H8SBWHCvtG_nIBrrR_j8UWSsG5kyd2rw-KrGPxrena4w5BUr-expHBHPpeuaH4tsbSifHTqGHAFtzmaVJZsTgPGu-MVZLEdVwt-uA_OnBy_Uy67QeLDQs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2213909800.mp4?token=bD6yq27gDQ8OM3UDuud_314V2IsyzJOArxAAwXzs_3OX9dOUdUw98dRaSrCYWC62mPdiLC6-5kM6vJewGFszARJc2zUp-sD1UYWfNyq-4UwYNIIwb25SCySZ5MigiOP86nJhT5tzzrTJwBC968RNCL41HlpkDL41fP4s8E114cHFPOJCzjwIMWNeyh-DHWnXxvxgNr7FQxYYwrZaCjkWUGU_8dosb8r7_xBCqCyhMLy-BTCY0VnZDq-NG8AKXVyrXb9gJ_cSGBoqMA7Mf9KWgwPF0f4mWHto_GQ5lxgfhIeGT9fgyq293ihEWIW1tGZyuHclro3W9ZHMifjeBM8hYlh3woes6oNZdas-avMwy1TxZE2kAIbAujL6rQmDV4FMg3G7uvgFzFfr9GEWjxkSo_Gwbb_TyZAlffKYt8JsuMjOzefprZbCBVJ6_nEVkv8UZujKCHcOKHi59dG2lGhxjb8tySodIH6y663YH6Jol-m4q33BMlXMgqXqLsgdIglh4T0IHfnukEl7KBkUx4XklaJPL6UzW_tOGzTEo-ilJ0zusgOdql49J5H8SBWHCvtG_nIBrrR_j8UWSsG5kyd2rw-KrGPxrena4w5BUr-expHBHPpeuaH4tsbSifHTqGHAFtzmaVJZsTgPGu-MVZLEdVwt-uA_OnBy_Uy67QeLDQs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پزشکیان:
ایران در دو قرن گذشته به هیچ کشور یا سرزمینی حمله نکرده، اما همواره با صلابت از خود دفاع کرده است.
با این حال، اکنون ما به ایجاد بی‌ثباتی در منطقه متهم می‌شویم و برچسب تروریست به ما می‌زنند.
@News_Hut</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/news_hut/72130" target="_blank">📅 17:57 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72129">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">مسعود پزشکیان:
کسانی که خود تروریست هستند و تروریست‌ها را آموزش داده و از آن‌ها حمایت می‌کنند، ما را تروریست می‌خوانند. ما تنها از خود دفاع کرده‌ایم؛ ما تروریست نیستیم.
مردم بی‌گناه ما هدف حملات بزدلانه‌ای قرار گرفتند که بر کشورمان تحمیل شد. ما با نهایت قدرت از خود دفاع کردیم.
آمریکا و اسرائیل با پیشرفته‌ترین فناوری‌ها به ما حمله کردند. آن‌ها به ما ضربه زدند، اما ما سر تسلیم فرود نیاوردیم
@News_Hut</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/news_hut/72129" target="_blank">📅 17:55 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72128">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/baa7d4e9f3.mp4?token=nC3A9F2bOaVKbDgvUO4JVVGot3E6oEaj_Z8pHVi0C2KNhLY50u2fb9lPGe9RvihMjWmQufiQKCCZjDA_nTQZ-pi5m42Vkxd1Anjy6WgKoN5ilTUvz5kG8GTDZeabwzFp68-0jG5mm25kptd5lJSU1xX8vyuCFMb64-k9EIHgB3Y5gxLlM0y9GpRqq6dg12TxX3mhI7Zp6JhRl_KNCgLDZcRUBqzVkMKeltGwKYWAgZEPw7QdpUmk-1Mey8d-4rJk_VPSnw-_DxkXmhjNxUCSv2Cb8l66xG2a8aN0MAGItFz_reYNc5D1YH5JpPjEoer177vETM7s6VCVFR3FDCk56zY4liE-3OovDMI9MevTGM-cjZaYbH7cGNZr6WMgTmUyyvhwdqHEjJAsRN1KFTB-aVUPvNATJhEo0mQqo2jcJxCkYVuCX1yDkzh5igF0pFlBcJfDWYVb3DzQogNAiqFE3Yr4masOUByJOqdLq7yoByspx8Cmosq9cmx51AEXMX8PjXjSG7GjXGkQOIvs7WtfzbzfNBvuStO8F7EMm_295rEdfjVqJ5tFjZru7gwuVOlfIV44TetLtGOWK75_JW6cWE5MJZLzhc2Aks5FQG4Vly1yRvL0n8sezAqsNpdcaFlreKHecL7zp0CCYLQs7j3mX74bD4lpIY6iWcqUGbldWhU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/baa7d4e9f3.mp4?token=nC3A9F2bOaVKbDgvUO4JVVGot3E6oEaj_Z8pHVi0C2KNhLY50u2fb9lPGe9RvihMjWmQufiQKCCZjDA_nTQZ-pi5m42Vkxd1Anjy6WgKoN5ilTUvz5kG8GTDZeabwzFp68-0jG5mm25kptd5lJSU1xX8vyuCFMb64-k9EIHgB3Y5gxLlM0y9GpRqq6dg12TxX3mhI7Zp6JhRl_KNCgLDZcRUBqzVkMKeltGwKYWAgZEPw7QdpUmk-1Mey8d-4rJk_VPSnw-_DxkXmhjNxUCSv2Cb8l66xG2a8aN0MAGItFz_reYNc5D1YH5JpPjEoer177vETM7s6VCVFR3FDCk56zY4liE-3OovDMI9MevTGM-cjZaYbH7cGNZr6WMgTmUyyvhwdqHEjJAsRN1KFTB-aVUPvNATJhEo0mQqo2jcJxCkYVuCX1yDkzh5igF0pFlBcJfDWYVb3DzQogNAiqFE3Yr4masOUByJOqdLq7yoByspx8Cmosq9cmx51AEXMX8PjXjSG7GjXGkQOIvs7WtfzbzfNBvuStO8F7EMm_295rEdfjVqJ5tFjZru7gwuVOlfIV44TetLtGOWK75_JW6cWE5MJZLzhc2Aks5FQG4Vly1yRvL0n8sezAqsNpdcaFlreKHecL7zp0CCYLQs7j3mX74bD4lpIY6iWcqUGbldWhU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مسعود پزشکیان:
مردم بی‌گناه ما هدف حملات بزدلانه‌ای قرار گرفتند که بر کشورمان تحمیل شد. ما با تمام توان از خود دفاع کردیم.
آمریکا و اسرائیل با پیشرفته‌ترین فناوری‌ها به ما حمله کردند. آن‌ها به ما ضربه زدند، اما ما سر تسلیم فرود نیاوردیم.
@News_Hut</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/news_hut/72128" target="_blank">📅 17:53 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72127">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">مسعود پزشکیان:
دیروز ترامپ ما را تروریست خواند؛ در حالی که ما خود قربانی تروریسم بوده‌ایم.
من از ایرانی می‌آیم که در آن، رهبر عالی‌قدر ما بدون هیچ‌گونه مبنای قانونی یا دلیلی ترور شد.
من از ایرانی می‌آیم که در آن، مدرسه‌ای بمباران شد. این کودکان را می‌بینید؟ این کودکان بر اثر بمباران با تسلیحاتی که توسط آمریکا و اسرائیل به کار گرفته شده بود، جان باختند.
آن‌ها بی‌گناه بودند و هیچ جرمی مرتکب نشده بودند.
@News_Hut</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/news_hut/72127" target="_blank">📅 17:50 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72126">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1aca1a8c79.mp4?token=hk4CGH_2eJE12xp88s5D7bRQieGy1R-jrcWwjOxUZuaPEh0VDXSTuHPTawJLCi2gzthS3lDIRJ1RDVYzlFzrfyn50CB4MEkr4IsT6DuUQq6fkRQb8FgXlBMSB9dLznxGdWiMYDkUSshPHHAgjdb8fHIu_wmKJR7gm3K_OA-cK6uTk-I3JUdkvWdWbH37OIrpfCTceTBgNzkQzWpfWojcPal0XaYbQstm-iXnCaClsS6XQmRGt6furiPzzfBtL1HBufq_QhtoEo9vhtnXVLv2ZcBFSvzX4RYzeduG6wvDLFs72MRWnalPdgzYVuglxevj8NMiGrB3gCxpjgkgYA6P-oWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1aca1a8c79.mp4?token=hk4CGH_2eJE12xp88s5D7bRQieGy1R-jrcWwjOxUZuaPEh0VDXSTuHPTawJLCi2gzthS3lDIRJ1RDVYzlFzrfyn50CB4MEkr4IsT6DuUQq6fkRQb8FgXlBMSB9dLznxGdWiMYDkUSshPHHAgjdb8fHIu_wmKJR7gm3K_OA-cK6uTk-I3JUdkvWdWbH37OIrpfCTceTBgNzkQzWpfWojcPal0XaYbQstm-iXnCaClsS6XQmRGt6furiPzzfBtL1HBufq_QhtoEo9vhtnXVLv2ZcBFSvzX4RYzeduG6wvDLFs72MRWnalPdgzYVuglxevj8NMiGrB3gCxpjgkgYA6P-oWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هیئت نمایندگی ایالات متحده هم‌زمان با سخنرانی رئیس‌جمهور ایران، پزشکیان، صحن مجمع عمومی سازمان ملل را ترک می‌کند.
@News_Hut</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/news_hut/72126" target="_blank">📅 17:48 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72125">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/72125" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/news_hut/72125" target="_blank">📅 17:48 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72124">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fK3df6nuFNFO3s__nNultZAWE19qSm6QUYsMoTyepVCpzlXi7WowPF2iVjycTzTNuOIUUoUbB0OTPDmvoRta4wD_7BoyyoZ_caTmSHWkOmbDjYwW-IFZbpnxzXoBTbTQJEy-tZB_O_PGBR9lF51WxnXPJtJ4Zw7gZaIx8pjV_GQFI5An8SDnwnIed4SRcm5QK5cSJbAX3PUcGG7G_ud1oULmf731A4PtnXx4s_wXEz6ssyCFI23YmKHr_xknwoD07dlnCsNvQAPKNnBBUYfdvOKR-yMO3h68mmB1BrvEbITg69SE2vMP0tGLaTTeoW0WQG_iQl9EyBjhltxABhG-5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
با اولین واریز، بیشتر دریافت کن!  فقط در سایت جهانی
TrexBet
🦖
بسته خوش‌آمدگویی ویژه
TrexBet
تا ۱۰۰٪ بونوس واریز
🦖
تا ۱۵۰ چرخش رایگان در ۴ واریز اول
🥇
واریز اول:
۱۰۰٪ بونوس + ۳۰ چرخش رایگان
🥈
واریز دوم:
۵۰٪ بونوس + ۳۵ چرخش رایگان
🥉
واریز سوم:
۲۵٪ بونوس + ۴۰ چرخش رایگان
🏅
واریز چهارم:
۲۵٪ بونوس + ۴۵ چرخش رایگان
🦖
🦖
🦖
🦖
🦖
🦖
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/news_hut/72124" target="_blank">📅 17:48 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72123">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d4142dc5d8.mp4?token=Y4tpMLV6VSaBC0XrRWEP4i9s-NfRRx21NVKOpJvusyyuCPp-6ZwpigYB8PqVcxbIN1W66BRppHdH8to6JgCR3vdqzs0oddREnyklVo-F7ZQBnGkT5_AX10RE8zEU9FeEFZZQkynoTEG2eIMZArmQPpNZ0_c0Iwpqck0X9WEfrJgQJSDeTJDOmYFWg0r8isQcv_DOMNeljCAPOGdgJs7jFlNsLxcUilgJAar5KUZaHY26fYs0keFHYjr27LZnWHGHLMes8BmR70TbxpFhYGZA_MiGKgxD0EI1Nr2Xj0Bl4g3hVtwMloXJgqoCL_1RnDb7b8vyfbPi3bB-upVIYZ0nVA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d4142dc5d8.mp4?token=Y4tpMLV6VSaBC0XrRWEP4i9s-NfRRx21NVKOpJvusyyuCPp-6ZwpigYB8PqVcxbIN1W66BRppHdH8to6JgCR3vdqzs0oddREnyklVo-F7ZQBnGkT5_AX10RE8zEU9FeEFZZQkynoTEG2eIMZArmQPpNZ0_c0Iwpqck0X9WEfrJgQJSDeTJDOmYFWg0r8isQcv_DOMNeljCAPOGdgJs7jFlNsLxcUilgJAar5KUZaHY26fYs0keFHYjr27LZnWHGHLMes8BmR70TbxpFhYGZA_MiGKgxD0EI1Nr2Xj0Bl4g3hVtwMloXJgqoCL_1RnDb7b8vyfbPi3bB-upVIYZ0nVA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قیمت کوکائین در تهران چند؟
پلیس مواد مخدر تهران بزرگ ، یک بار بزرگ کوکایین کلمبیایی را قبل از پخش در پایتخت ، کشف کرد .
این کوکایین ها بیش از ۵۵۰ میلیارد تومان ارزش گذاری شده است.
گویا داداشی ها سهم  مامورا رو ندادن اونا هم بار رو لو دادن
@News_Hut</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/news_hut/72123" target="_blank">📅 17:34 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72122">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1dadfb7a92.mp4?token=IZXZ2I67FjU9lZVl9of6Yz6KqqkhEWXISo6KhcsodxTT15GfwGxCB7iOIVS83t80IMJ_2u6094qorKZmh30xmih6JfQWmPWRtYU7DVetz_NI4TBNnivjg2g-ozRrgAgPrpHzLJp5CQYzw4HuTeRmJWWdr4o5aWGkcgB8nEbsV3-tdWmBipLCV8LxjgX-vB2v5oJ1krgHFBLOrx7MF2aaLL4-vOJ8h2sP1dPw1ECLm2_Yo0-jxlejQ2vGrfbLOs5XmZPz4L2j4a-uygRjURCtNa12okTseEkySnAEJK7rQQYGmbbylyK3gBYs36OpgYzTEDSmsTCpjWTwfmLH4gABNg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1dadfb7a92.mp4?token=IZXZ2I67FjU9lZVl9of6Yz6KqqkhEWXISo6KhcsodxTT15GfwGxCB7iOIVS83t80IMJ_2u6094qorKZmh30xmih6JfQWmPWRtYU7DVetz_NI4TBNnivjg2g-ozRrgAgPrpHzLJp5CQYzw4HuTeRmJWWdr4o5aWGkcgB8nEbsV3-tdWmBipLCV8LxjgX-vB2v5oJ1krgHFBLOrx7MF2aaLL4-vOJ8h2sP1dPw1ECLm2_Yo0-jxlejQ2vGrfbLOs5XmZPz4L2j4a-uygRjURCtNa12okTseEkySnAEJK7rQQYGmbbylyK3gBYs36OpgYzTEDSmsTCpjWTwfmLH4gABNg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یه مادر توی کمد لباسای دخترش، کاستوم مخصوص سکس پیدا کرده، بعد دختره هم به این شکل مامانشو قانع کرد!
@News_Hut</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/news_hut/72122" target="_blank">📅 17:01 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72121">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EsLoHc4c_-ZhjnQqkukPq8sdk31b7ldDuEYA8FKm-KiJ8YKoPefG7HOjaEWzCCmVbalWHH-g2NNmClOsRZYBYA2n2HdQ_OBPQYfzbrXpL9N8ds9LFXDWmVuwOqS_Pq4ZxTHWyc_vJkmaXIJDx8xPLZKStn1-gsOHrnKt94oWwFdC3ih9N7gpHAyD2IgoD2teTJXfmOFB8NA5urH1qhFEypKVB19g8UEbkBUNfS0qSLxakyX1ju0vVykkTXvOnuWh8kuZ6Vcvx5WEg79vTAi3WjAi9a0RNO-CT29Gd4crGOute3RvGdKmQt9tNo6M2464g0jys3xHUfqrX7GKFwTLTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سازمان عملیات تجارت دریایی بریتانیا (UKMTO) اعلام کرد که یک کشتی باری در تنگه هرمز هدف اصابت پرتابه‌ای ناشناس قرار گرفته است.
این کشتی دچار آتش‌سوزی شده و بر روی آب سرگردان است. خدمه کشتی تخلیه شده‌اند و گزارش‌هایی از دو مورد تلفات منتشر شده است.
@News_Hut</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/news_hut/72121" target="_blank">📅 16:34 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72119">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/056cf75693.mp4?token=ailiX5nH3XKieGhKxIXAWNqB2Wof8K15SE7YByYmNAh4RO4aWO8Bn0apRnwR9rgMA4-ghFmY8eHh0mf8b3bzIDzavvVzUltNCjVP1Imz5eFILQLznM5lNONeAtP3uPwrgkE05LU4QZmJlhZNSCQlGfvL8dTF8J2D0jbmnHhhFVZskp6zGSNEiT5UkneWiCdQ3sFyLrIZa4SZweiDlMydzAwf3T22IPABJAa1qAQjoDG4degS_CdgcjDXoDf0lLU-I3gO7DiJiwezx87CQ1FuWjVjySDahv24dQuOqnzRMSp4QDUlVUQsxWbzge5fM8k8Y2yKVH3B5BEVZLHHJLi9dQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/056cf75693.mp4?token=ailiX5nH3XKieGhKxIXAWNqB2Wof8K15SE7YByYmNAh4RO4aWO8Bn0apRnwR9rgMA4-ghFmY8eHh0mf8b3bzIDzavvVzUltNCjVP1Imz5eFILQLznM5lNONeAtP3uPwrgkE05LU4QZmJlhZNSCQlGfvL8dTF8J2D0jbmnHhhFVZskp6zGSNEiT5UkneWiCdQ3sFyLrIZa4SZweiDlMydzAwf3T22IPABJAa1qAQjoDG4degS_CdgcjDXoDf0lLU-I3gO7DiJiwezx87CQ1FuWjVjySDahv24dQuOqnzRMSp4QDUlVUQsxWbzge5fM8k8Y2yKVH3B5BEVZLHHJLi9dQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دانیال عیوضی، مجروح کشتار کرج، پس از ماه‌ها تحمل درد و جراحات، در دی‌ماه ۱۴۰۴ ترکیه را به مقصد اروپا ترک کرد و امروز خود را به سازمان ملل رساند تا درباره مشاهداتش از کشتار و برخورد مأموران امنیتی جمهوری اسلامی شهادت دهد.
هیئت ایرانی تلاش کرد سخنان او را مغرضانه و تند جلوه دهد و مانع ادامه صحبت‌هایش شود؛ اما با دستور رئیس جلسه، عیوضی به سخنان خود ادامه داد.
@News_Hut</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/news_hut/72119" target="_blank">📅 15:59 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72118">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b96e8038a0.mp4?token=VCdLpTzQ9uGfq4uOJrvQTGZrtzx2Sm1j_WAKpEuyXdO85nnYzWaRIxeq2nOX0PaqSRW4t0kvKMgYSVY6DqUT0pdOxFyKlxbt-TseMwhLX8vTqO4AfMvpNeNZ6ZuHjXqdj7CQKUaLEo1t-xD73GzGLw3yq52gP6kh37edPDnfDv3kZ_muM3XxUvpC0wpDrlJJ2UvkOemCAM_ck6FrmmTEw_F2pPzFDSAvWkBfT6jH9aTUbXOgvQFHLCoM5WNMZuC9Ie4a_0gI1twfZ7N9dBJotth4MlirH3UJe2ScMK-ggk-zd-UUOdOhei50lIuU651U5hFJderWTdobzYlk7ESPWA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b96e8038a0.mp4?token=VCdLpTzQ9uGfq4uOJrvQTGZrtzx2Sm1j_WAKpEuyXdO85nnYzWaRIxeq2nOX0PaqSRW4t0kvKMgYSVY6DqUT0pdOxFyKlxbt-TseMwhLX8vTqO4AfMvpNeNZ6ZuHjXqdj7CQKUaLEo1t-xD73GzGLw3yq52gP6kh37edPDnfDv3kZ_muM3XxUvpC0wpDrlJJ2UvkOemCAM_ck6FrmmTEw_F2pPzFDSAvWkBfT6jH9aTUbXOgvQFHLCoM5WNMZuC9Ie4a_0gI1twfZ7N9dBJotth4MlirH3UJe2ScMK-ggk-zd-UUOdOhei50lIuU651U5hFJderWTdobzYlk7ESPWA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">استقرار پدافند هوایی روسیه وسط بزرگراه رو دریابید
@News_Hut</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/news_hut/72118" target="_blank">📅 15:21 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72115">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Mn4xbYJQsACO_VMOpNqRhVTFD58SSOa41WV_l_NARCUxT9AqXVeFgDOCZukWcTmfnuFfO-4WnDNs9kg0U1nHp7hBTzPaSSTk9IdCC-InZJmR9jmCDgNbIRmCPLWuinLg4FnmkD5_vqRJO3RsDBZJRchDovYnSkbmUKbB8KQ9ebCn1A5x5y31BHh604M623r6RS1S3twqVxxDAesXXdq1GoXSMkaKkc0jBxDx3diA8x29gnIVGdNU0bhMrunzcCTmwRigl0OlkTL_TUNdAMaW8dFf5DEZtR3ZRKFbTQN2rx1ZljThdqY6WJ44USgQkdBu5RVfj5gOcshSi6ou3HhzBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EmHXXNDNOLaqePx1Th-lTC8PmwHDhWcHg7a6L1e7Xb0kB268paPUUKhnLw5oEiwcHv35BqhgHVjodnB0vlYwtNSiwfPN1puMr0pbJQrAfzIgHSvzl4ndn_ESNcEZyjzN57tZ6sl7kIRmG5IfhCrwjPvsDy-2n4MvzEVuozCzGJjK1mgfDyJpRZIZhXGGCPSEjpl8ZJhlaN2eLLCHERdbaFTmLPgvGNhAmq13rCMgHxQq8clFe6cb2pOB4MN3lpXs3dXwhJXtDvkSgyM1jrUCgV_gcgXjZIBPLMDGu1PaXTNZkv_Nes6BXeWRaF94oY7RJrS0x3J5LbMnG8n1a0xMCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/V5PReDJ2yG0v12XtrpfRIgGwzCzijViuBGqcp3DvyYquL--Zt5QfHqJMB4X2usiJ038B76N7p7tXSbr9VmB3vQAEZoo61eiWMKkMpyKNRZV2sjHcDvqwsQcjP_iy-oN-hLpcSwJWIKHZrNs0nEtb_M1juCbJtgQ6w29cuabdw0JlF_EetJsjFUBYVFXifzO88LCgGCFlLiceo7lSpBaTUYoNhnq8JEfiFBtRzO7tJwz62Y8NoJO01RXnvmTbtlV0-BKeg6SpaSOpiN6Ck0MeHEFSHuI-bbYNKRxNIFaNNLJd8uwJJQGW9L2_Oy-W8yDb6rtx9ahZPP8X8Q9nfQAQPA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">این بیلی آیلیش هم روز به روز داره خوشگل تر و جذاب تر میشه هرشاتی از خودش منتشر می‌کنه کلی لایک میگیره :)
@News_Hut</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/news_hut/72115" target="_blank">📅 15:03 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72114">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">تحریم‌های جدید آمریکا علیه بخش هوانوردی ایران، چندین کشور را بر آن داشته است تا پروازهای ایران را محدود کنند.
محدودیت‌های تأیید/گزارش‌شده:
🇬🇪
گرجستان — ممنوعیت کلیه پروازهای ایران از ۲۱ سپتامبر.
🇦🇿
آذربایجان — ممنوعیت فعالیت شرکت‌های هواپیمایی ایرانی از ۲۲ سپتامبر.
🇮🇶
عراق — تعلیق پروازهای ایران به بغداد؛ احتمال تغییر مسیر برخی پروازها به نجف.
🇴🇲
عمان — توقف پروازهای ایران به مسقط.
🇶🇦
قطر — گزارش‌هایی مبنی بر تعلیق پروازها از مبدأ ایران.
🇹🇷
ترکیه — اعمال محدودیت‌های عمده.
برخی مسیرها همچنان فعال هستند:
🇨🇳
چین
🇦🇲
ارمنستان
🇦🇪
دبی/امارات
🇮🇶
نجف
@News_Hut</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/news_hut/72114" target="_blank">📅 14:25 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72113">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DHZ0uBGVXfc4yVBymTJ9OFg8rDFslmH1mbECxWek44iGWPfL86BdKcNt5A-HN6JYMUC9DX9V-YAacIZD94KYG90LXPBzG08LPZjKlElUa6h8Rm_wM4LcWtGzKUTL3jrqqHEeolZMr5AwrXrjDVv9D-VhSrVI8crRq1ECo1eg9Gm5dxzQivguquIg--C2A63MkOF0SL46fOwQZktLrRJrAlNlxaBbh2oz6k1Rmnw2H1gfHk9fHkGpP6u94FrACgMqvYBjqpgI46aoNC7er5us1Q912tTqvZzM7LpWwoI7HIonB07H3KX_XOFma_BvtXYOtJ7EDqjj6qYsHVwDwWFCEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ بازنشر کرد:«ائتلاف نتانیاهو در تازه‌ترین نظرسنجی انتخابات اسرائیل پیشتاز است.»
@News_Hut</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/news_hut/72113" target="_blank">📅 13:34 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72112">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/foADMWJC8ZipsZ_fhlX-ND1ald90TeqN9vObvN9QdwuRGUcQd0Tr0nV8DgToKeHp9tMNCdJVStDDXgiQMnAEYFur75N-Wf7vXkFPv_6rv5X3W9QDbGIUkrZHSayPTcdCu58WWzL0oc_rAdJx4AGz7izp20oYzpPJ27YhgfAgW2M0jSTuo4UVusUWwIMsAEF-jDasbm8TdtVAE5kXcQCge4Z7D2K3G6Gcquk2WNT9-zhZqYch198cH2Rp7kVzduIRVySXjIGm6gP1XzFtj1d82ESZ8DjsUycwsy2azOs5TfTO_W_ziFjpl4I3rPgDQy0xFDVwTjnrwt2y3jZTlbUl0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حال‌ و هوای یکی از دانش‌آموزان در جشن شروع سال تحصیلی جدید:
@News_Hut</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/72112" target="_blank">📅 13:13 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72111">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fb3684649a.mp4?token=eU_OFdvlc7GbDbj5wYDECjPdfC5HydsjA-Bro4FreduCu3lWajbVzY8E3m8tLwRwe9TrWjkbH8qe_TM-4VpM95Ct8YY5oqWNbFVuAWCdiVX-yBQERTahZKkY-TRUb2RgZgvFhmA_t0uzX72W236-xopBzIhiIcVOiiIHv0OPHN5oPwzgeRzEGPFF9jBCVOtQZ5T5qU_rseNe_tTLh_FW0uV2kSSn1qieXLD0JudxvJ7NMMa_ediRmWKLNaVf1HEq2MTBHTImu6Sok3htbfDtyQFGrh3RsCUuX6Xdz9PH-264XHBqbX4vepzvNXYfGQB38rKDdNiZbrKxgj86rYGCnIDEBQeNY5yasbYSZqkakRWoZpurBELgUvgPowQs_xCTrdIYPFTIuKP1TVXgcb1smZiAVtjI_paRNCST9VrI0s74P37_UI08NM666kGnnZrzLgyZKZdYZR1k058Gc9Tf8muEVOlYLNmzadfwvmN13xTzlhO5_c_Jtau0AUZGplbh6Hug_HFM6hjmAMHiG9PXJGRvuf-P-WHXWpT3n94RtmWf9DyFvzgmsN6WN62-vykNlujb7e-Jg3ndTvnNXlW2W1_tRblVHYatAdd4O08YK9hFfeKgZ4qxO5pi8OH1JkFuISmPgVbvVzpJqk7DqbzDNzMfpZp9We84hPfQHeRZyw8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fb3684649a.mp4?token=eU_OFdvlc7GbDbj5wYDECjPdfC5HydsjA-Bro4FreduCu3lWajbVzY8E3m8tLwRwe9TrWjkbH8qe_TM-4VpM95Ct8YY5oqWNbFVuAWCdiVX-yBQERTahZKkY-TRUb2RgZgvFhmA_t0uzX72W236-xopBzIhiIcVOiiIHv0OPHN5oPwzgeRzEGPFF9jBCVOtQZ5T5qU_rseNe_tTLh_FW0uV2kSSn1qieXLD0JudxvJ7NMMa_ediRmWKLNaVf1HEq2MTBHTImu6Sok3htbfDtyQFGrh3RsCUuX6Xdz9PH-264XHBqbX4vepzvNXYfGQB38rKDdNiZbrKxgj86rYGCnIDEBQeNY5yasbYSZqkakRWoZpurBELgUvgPowQs_xCTrdIYPFTIuKP1TVXgcb1smZiAVtjI_paRNCST9VrI0s74P37_UI08NM666kGnnZrzLgyZKZdYZR1k058Gc9Tf8muEVOlYLNmzadfwvmN13xTzlhO5_c_Jtau0AUZGplbh6Hug_HFM6hjmAMHiG9PXJGRvuf-P-WHXWpT3n94RtmWf9DyFvzgmsN6WN62-vykNlujb7e-Jg3ndTvnNXlW2W1_tRblVHYatAdd4O08YK9hFfeKgZ4qxO5pi8OH1JkFuISmPgVbvVzpJqk7DqbzDNzMfpZp9We84hPfQHeRZyw8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دنی دانون، سفیر اسرائیل در سازمان ملل:
ما می‌دانیم رهبران ایران کجا پنهان شده‌اند. ما می‌دانیم آن‌ها چه کار می‌کنند و چه می‌گویند.
به گمانم جانشان برایشان اهمیت دارد. آن‌ها دریافته‌اند که اگر به اسرائیل حمله کنند، تنها چند روز طول می‌کشد تا سراغشان برویم.
@News_Hut</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/news_hut/72111" target="_blank">📅 12:15 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72110">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/402f33620e.mp4?token=iTClk7YvGGUlVsJasreJCAzsDxxuNhWnLGRcYUx688aAVMmT-AUu7BkU5VKzZAepPfJ6aNdD2_opgFA9s2mGcWqTIt9pzwtDJsh4DtkmjZE0ncYZzXgk1Lq5AXXjEM_CQPAbmauiJlBOoXLFTwNpQeY8mB4ex33JwiJzwPhJ_w_BbNi4_GkFQhvEDdJUazCkbb9zS3dujRtnUVrhNhbVt_TQNncNVvORrYClGmMCYk1gK59xNzR5iYdyyGsnnmyee_YqQZzzMSGXOmrtlie_O3Q01jjidBXnwjafjYoisH4Rks1OmoLJiW7Wm1ZhhIayU1RwrD1PP2dEZ9uzMUDlSg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/402f33620e.mp4?token=iTClk7YvGGUlVsJasreJCAzsDxxuNhWnLGRcYUx688aAVMmT-AUu7BkU5VKzZAepPfJ6aNdD2_opgFA9s2mGcWqTIt9pzwtDJsh4DtkmjZE0ncYZzXgk1Lq5AXXjEM_CQPAbmauiJlBOoXLFTwNpQeY8mB4ex33JwiJzwPhJ_w_BbNi4_GkFQhvEDdJUazCkbb9zS3dujRtnUVrhNhbVt_TQNncNVvORrYClGmMCYk1gK59xNzR5iYdyyGsnnmyee_YqQZzzMSGXOmrtlie_O3Q01jjidBXnwjafjYoisH4Rks1OmoLJiW7Wm1ZhhIayU1RwrD1PP2dEZ9uzMUDlSg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">امروز یکم مهر ماه، بچه‌های میناب دیگه نیستن که برن مدرسه...
اما جاشون پیش خواهر برادرای بزرگترشون امنه
🤍
@News_Hut</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/news_hut/72110" target="_blank">📅 11:57 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72109">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b92a5ff67f.mp4?token=AsNjR0O5RvVyUFCg85qUE__kPsNvfMYMUNTJRr23zSbs9YD_Ab_xCfk-UtQizPNUAu32-ci61j-F18ENYoNAvmeg1m230IJKU08ZQOrdudHOqqUXAeUPMT1mqLbTHqyBe4_zMkHl98B8E3V6k7wx7wewd-ruVqXrzqzbEykAGxth8U8gFZmopxg1LGxas_idetjA5Hm7RgI82wuCmMgdfC50bK0yqiVbKjmyjHzi3VgvZ9V2A5lDNq2CNeokFc0tn3LXciomSQXSnRyllBJ1Q5TnKf7bkLMG_2V7WcRp9XW7rDO21LELuzZJLApP_huyLHBkpNr-GDFT18ZVvjXbN1iAUeK-t2VGz55es_QDG0Gv9WlXMWrPGFrjk9acLGdlIr9l_qYcRjvJdK2jtWMSI2AAwuZzIjXC9HeHtP34D1JUlk2s9mDXiw5fG_qYhFnmC3Ooh5ki5OhnoIAafGtwjAe1t_zTLjuHOG6uVEsRA_fdA7qb138USWbq3FaN-irQhdTmFjWMGPiphC9S8r026JopYyPKqDD6zzxqsMm-PW1MJjJMOlpPqu3QZFyLM1hcHf2YJenN4FTn6SYPPvyu3QTD_VO78yolHV108EcEvtSakPJ25JgVLCXjU12wgDnrNElkp78Ve-uwRWhNb-WO8TV7RfLUrYzGkZJIo3LPUpI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b92a5ff67f.mp4?token=AsNjR0O5RvVyUFCg85qUE__kPsNvfMYMUNTJRr23zSbs9YD_Ab_xCfk-UtQizPNUAu32-ci61j-F18ENYoNAvmeg1m230IJKU08ZQOrdudHOqqUXAeUPMT1mqLbTHqyBe4_zMkHl98B8E3V6k7wx7wewd-ruVqXrzqzbEykAGxth8U8gFZmopxg1LGxas_idetjA5Hm7RgI82wuCmMgdfC50bK0yqiVbKjmyjHzi3VgvZ9V2A5lDNq2CNeokFc0tn3LXciomSQXSnRyllBJ1Q5TnKf7bkLMG_2V7WcRp9XW7rDO21LELuzZJLApP_huyLHBkpNr-GDFT18ZVvjXbN1iAUeK-t2VGz55es_QDG0Gv9WlXMWrPGFrjk9acLGdlIr9l_qYcRjvJdK2jtWMSI2AAwuZzIjXC9HeHtP34D1JUlk2s9mDXiw5fG_qYhFnmC3Ooh5ki5OhnoIAafGtwjAe1t_zTLjuHOG6uVEsRA_fdA7qb138USWbq3FaN-irQhdTmFjWMGPiphC9S8r026JopYyPKqDD6zzxqsMm-PW1MJjJMOlpPqu3QZFyLM1hcHf2YJenN4FTn6SYPPvyu3QTD_VO78yolHV108EcEvtSakPJ25JgVLCXjU12wgDnrNElkp78Ve-uwRWhNb-WO8TV7RfLUrYzGkZJIo3LPUpI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اظهارات روته دبیر کل ناتو درباره ایران:
چرا برای از بین بردن توانمندی هسته‌ای ایران، حضور ایالات متحده ضروری بود؟ چرا اکنون در ماجرای حوثی‌ها در دریای سرخ، همه نگاه‌ها به ایالات متحده دوخته شده است؟
زیرا اروپایی‌ها به نوعی از توانمندی کافی برای انجام این کار به تنهایی برخوردار نبودند. آنجا حیاط خلوت اروپا محسوب می‌شود، نه حیاط خلوت ایالات متحده.
در آینده، دستاوردِ داشتنِ یک ناتوی قوی‌تر این خواهد بود که اروپایی‌ها می‌توانند خودشان به امور حیاط خلوتشان رسیدگی کنند.
@News_Hut</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/news_hut/72109" target="_blank">📅 11:43 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72108">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">اظهارات روته دبیر‌کل ناتو درباره ایران:
می‌توان گفت که اجرای عملیات «Epic Fury» بدون بهره‌گیری از اروپا به عنوان سکویی برای اعمال قدرت ایالات متحده، غیرممکن می‌بود.
از ۲۸ فوریه سال جاری تاکنون، ۵۰۰۰ فروند هواپیما در پشتیبانی از عملیات «Epic Fury» از پایگاه‌های اروپایی به پرواز درآمده‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/news_hut/72108" target="_blank">📅 11:36 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72107">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/72107" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/news_hut/72107" target="_blank">📅 11:36 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72106">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Nq8viAer5s88UPB_fq3KfJ77kUKK9PY3lltTZS6PmvGznswnzQvy3t2O-AT-j3fHsXJkFYBhlvbncQKwESurmu5-iwLIWC1uZOcIq8eZOXegGRwJsqZEKE3bAlTDmrunLJGn_QjzXCGy0t6vciaEffn84v-ZVFwaOyImv0_Ob6ohDYMveBbhP5O8rLl7CXVM102aM7CdCpy3xTITDeJNrOlHpaUES86keUhzaKXP0uUPhTWReH6Tw_CaldKejVCttXbVjbjNXmtMKDL_B8OLPTeO1okTnmqCca88snHLjLEOhVPyNI40A95lnceITx4nz1-WOtCwcmkFQ2Y9X4LW_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
هیجان مسابقات DOTA 2 را زنده در
TrexBet
دنبال کنید و با پیش‌بینی دقیق نتایج برنده شوید!
🦖
پوشش کامل تمام بازی‌های محبوب Esports:
‏CS2, DOTA 2, Valorant و ده‌ها گیم جذاب دیگر...
🦖
🦖
🦖
🦖
🦖
بونوس اولین واریز تا سقف ۱۰۰ یورو
🦖
بهترین ضرایب بین تمام سایت‌ها
🦖
واریز آسان و امن از طریق کارت به کارت
🦖
هیجان بازی، وقتی بیشتره که انتخابت حساب‌شده باشه!
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/news_hut/72106" target="_blank">📅 11:36 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72105">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">شلیک چندین موشک ضد کشتی به سمت شناورها در تنگه هرمز
@News_Hut</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/news_hut/72105" target="_blank">📅 11:34 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72104">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4629cd7c2a.mp4?token=VTZr3z5-Z2rMnSgwtTJiHdRqy1JIVfiHsilwcllcGTgNR25uJQPtC6GXSyeaO3iTmuI6vyCxCeA5VUcfHz4YCFLPfQxxbbxP17FtMLNczmnPgfc4fqjVpjIb_x5AJvVhQzNfDY4G4436hmgU0XeoBYnsunjS5kIxPmjGCS2Jm-GN7yWNVJtrbK5vzmHnUqWHwFm29bGkV_7WWm6PmaaKLhn2bjb2ewnUEi-kDjKuk1D66uOYUpNc8SqXucFXZiGema4k6RlGne5_nLglEXSfp9dS_soapBQiF2IB-fTLku2qvA9UYyAb04AuTYjHm81nuDcXxLvmU8q39QErbktAD0iTgxJaXlUzXwq8U0vFPYCBMSr1v2EEqeF-dSTeJI24ujxHbkp8dpN1v1arCi_nRoPObeA4qLtfrQJVnIAbpr7dO_mRkPGFClOqGm0vJ9J4eSea74WDvtQhIsms7gSIdT3pul4tkUFJEEMq-_ZrvtsVFiGSK7fP2w7W9DQNtSgfnui0TvP0-0oz8klKPOLorT_n0xpm-9OpIXXPRNyjvJlY3FmsxL8zI0ACOWvPxnSPdH0i1e23HhPF9RGH3gEsn-Eay6Iv4snYeQVxuDid_bELU7X3dmRthOb21EWy78LR11eslAeFHUm0fL99AZ97vz0bf3oVBlNpogoTbk_UQOE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4629cd7c2a.mp4?token=VTZr3z5-Z2rMnSgwtTJiHdRqy1JIVfiHsilwcllcGTgNR25uJQPtC6GXSyeaO3iTmuI6vyCxCeA5VUcfHz4YCFLPfQxxbbxP17FtMLNczmnPgfc4fqjVpjIb_x5AJvVhQzNfDY4G4436hmgU0XeoBYnsunjS5kIxPmjGCS2Jm-GN7yWNVJtrbK5vzmHnUqWHwFm29bGkV_7WWm6PmaaKLhn2bjb2ewnUEi-kDjKuk1D66uOYUpNc8SqXucFXZiGema4k6RlGne5_nLglEXSfp9dS_soapBQiF2IB-fTLku2qvA9UYyAb04AuTYjHm81nuDcXxLvmU8q39QErbktAD0iTgxJaXlUzXwq8U0vFPYCBMSr1v2EEqeF-dSTeJI24ujxHbkp8dpN1v1arCi_nRoPObeA4qLtfrQJVnIAbpr7dO_mRkPGFClOqGm0vJ9J4eSea74WDvtQhIsms7gSIdT3pul4tkUFJEEMq-_ZrvtsVFiGSK7fP2w7W9DQNtSgfnui0TvP0-0oz8klKPOLorT_n0xpm-9OpIXXPRNyjvJlY3FmsxL8zI0ACOWvPxnSPdH0i1e23HhPF9RGH3gEsn-Eay6Iv4snYeQVxuDid_bELU7X3dmRthOb21EWy78LR11eslAeFHUm0fL99AZ97vz0bf3oVBlNpogoTbk_UQOE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شاهزاده رضا پهلوی:
تولید ناخالص داخلی ایران در سال ۱۹۷۸ دو برابر کره جنوبی بود. امروز، تولید ناخالص داخلی کره جنوبی پنج برابر ایران است.
وضعیت اقتصاد ایران قابل تداوم نیست؛ پایدار نیست و در آستانه انفجار قرار دارد.
@News_Hut</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/news_hut/72104" target="_blank">📅 11:16 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72103">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/582ee3d494.mp4?token=jBhp87_-v8u_GV7o3OUWhzxuY5791RwKN1egDTBM_py3oU9sXrwmfXsyVAGFh8D5jCY3KOQbBBxO60Pg8mHe7sBzCmAjhtRAwYGm8RIm0rKvLFttJ9YOz79OHMkeHSyY56--VvDnFOa8jcgs3RKQwcc36s60YFbBpDaz3H5sHCeVv2M00L7PzX_uEEvWW3y0Ulr-ry68RXuuKTE3zpoCZMN_Tndgi1dirLelZ0mHQwe3J4yQaQy6fT8X6lzAHf9kBmM3ECMEJdBpciDBDteZ_dZbxA48Bdbes7Hz8kGkQQqsLEJGylYgasvzj9jhkCLqQC30hs9ouLyKK1l1LVGtHg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/582ee3d494.mp4?token=jBhp87_-v8u_GV7o3OUWhzxuY5791RwKN1egDTBM_py3oU9sXrwmfXsyVAGFh8D5jCY3KOQbBBxO60Pg8mHe7sBzCmAjhtRAwYGm8RIm0rKvLFttJ9YOz79OHMkeHSyY56--VvDnFOa8jcgs3RKQwcc36s60YFbBpDaz3H5sHCeVv2M00L7PzX_uEEvWW3y0Ulr-ry68RXuuKTE3zpoCZMN_Tndgi1dirLelZ0mHQwe3J4yQaQy6fT8X6lzAHf9kBmM3ECMEJdBpciDBDteZ_dZbxA48Bdbes7Hz8kGkQQqsLEJGylYgasvzj9jhkCLqQC30hs9ouLyKK1l1LVGtHg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ناوگان هواپیماهای باری نظامی، از جمله هواپیماهای «آنتونوف ۱۲۴» در حال فعالیت از فرودگاه لایپزیگ/هاله در آلمان مشاهده شده‌اند.
فرودگاه لایپزیگ/هاله یکی از مراکز مهم لجستیکی ناتو است که برای انتقال تجهیزات نظامی و محموله‌های فوق‌سنگین مورد استفاده قرار می‌گیرد.»
@News_Hut</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/news_hut/72103" target="_blank">📅 11:04 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72102">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/6c2bb73b79.mp4?token=D7rCpAnmbxM7EXoo4qXamRWNt4nSCJ5MD0Ut3ah23c0BpHCPalQ3S5sG63cMPScaox0I05J6c-IeUQ0ihu1V05W4U80Ob5_wom1nbC_9f5QnC8dGI_39uLceXEzePGf4LsThjT08QXf4ra_f2cPqWljf7uTInTnLUnM5zgi9ob2NQ3ZHjdTyq0ht2gHwTWhm_zSJ8a98tzolrWMlnigrECG9B9h_9VD48bnMnQLMu4iD1Sbu4oxzneUTjJo1Ki1Ylm-I1m4kd2q-SKuqjPm7-N7kcSdQ5hj65OLPvxOZFDa_BeGBQ7cxLfsIo-MtZ2pjDZgpn1EUIE_HwDbYwGb_Uw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/6c2bb73b79.mp4?token=D7rCpAnmbxM7EXoo4qXamRWNt4nSCJ5MD0Ut3ah23c0BpHCPalQ3S5sG63cMPScaox0I05J6c-IeUQ0ihu1V05W4U80Ob5_wom1nbC_9f5QnC8dGI_39uLceXEzePGf4LsThjT08QXf4ra_f2cPqWljf7uTInTnLUnM5zgi9ob2NQ3ZHjdTyq0ht2gHwTWhm_zSJ8a98tzolrWMlnigrECG9B9h_9VD48bnMnQLMu4iD1Sbu4oxzneUTjJo1Ki1Ylm-I1m4kd2q-SKuqjPm7-N7kcSdQ5hj65OLPvxOZFDa_BeGBQ7cxLfsIo-MtZ2pjDZgpn1EUIE_HwDbYwGb_Uw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کم‌ کم ربات‌های جای انسان‌ها رو دارن میگیرن....
برای اولین بار تو تاریخ، یه مبارزه رسمی بین انسان و ربات برگزار شد؛ که در آخرش ربات با یه لگد سنگین حریفشو انداخت رو زمین و ناک اوتش کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/news_hut/72102" target="_blank">📅 10:34 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72101">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/c2331092d7.mp4?token=kucDuc2blEchAdtrUGV_RQCs0BTstrulfTx0rrVIwm6-a8x_DRgmDTIgV54DXdgcGvFzat9LqL1qlfUSs05zFRKzCmvy0ezsPT8dU_C3wOJbZxdHRQWW18T6xW9pmoKaUwcTuaoLyHIGuOYLX4Pn7oQ-3hp5IR5TsymUf0lg3Rr56t04rJpplvEuxSG1wSDCps8MJYfr2oftwzqlBTMYLwjNhRJM9RUGW7vJoFVvQKIC48BLWRITx6AhGJFNUpS4vzuoE0yIF0xFMlKus-VNy0ZeOWG7KFGe8UX3HebdLNaiD8coviBTB-NAUqqDVB9uDNs5XPmS4EP_leZ--Nyscw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/c2331092d7.mp4?token=kucDuc2blEchAdtrUGV_RQCs0BTstrulfTx0rrVIwm6-a8x_DRgmDTIgV54DXdgcGvFzat9LqL1qlfUSs05zFRKzCmvy0ezsPT8dU_C3wOJbZxdHRQWW18T6xW9pmoKaUwcTuaoLyHIGuOYLX4Pn7oQ-3hp5IR5TsymUf0lg3Rr56t04rJpplvEuxSG1wSDCps8MJYfr2oftwzqlBTMYLwjNhRJM9RUGW7vJoFVvQKIC48BLWRITx6AhGJFNUpS4vzuoE0yIF0xFMlKus-VNy0ZeOWG7KFGe8UX3HebdLNaiD8coviBTB-NAUqqDVB9uDNs5XPmS4EP_leZ--Nyscw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">لمس ممه‌های دوس دخترتون واقعا زندگی شمارو نجات میده! این یه شوخی جنسی نیست، از لحاظ علمی این موضوع کاملا ثابت شده و اینکار مثل معجزه عمل می‌کنه!
@News_Hut</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/72101" target="_blank">📅 09:45 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72100">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/575ce7dd12.mp4?token=VPWazMMaeV6WNZZjLeGymgfmdFthHPUoTzdnNG6jnHqjOUE0GWwLqLE5SvE9ZMdC4qqhqGDMiJC6EehXfdEzHlmHe91gT7LSDEUfJj-_O0vXx0mYmMQ1m9vi5jaeD9MLDRywrcfxfQVr7aZFeedO0DgwnSZedBP-9hYER3apPtZzOsgEEAgUphnAL0bnKcrn2ond6iQ2_ioKgBTaj77WN4KYKGDSBHkiBLUZTP6rCEYrXMGwZqrwABpQ-nqXWw3eMSsswHsnlHtFa5GSM5iYY8x-1ofjFxr8LRAVcVcz-pZgyZR26b2eQTHUL2cfkjSD3ZLhesZgAvxUnolEGW1rcA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/575ce7dd12.mp4?token=VPWazMMaeV6WNZZjLeGymgfmdFthHPUoTzdnNG6jnHqjOUE0GWwLqLE5SvE9ZMdC4qqhqGDMiJC6EehXfdEzHlmHe91gT7LSDEUfJj-_O0vXx0mYmMQ1m9vi5jaeD9MLDRywrcfxfQVr7aZFeedO0DgwnSZedBP-9hYER3apPtZzOsgEEAgUphnAL0bnKcrn2ond6iQ2_ioKgBTaj77WN4KYKGDSBHkiBLUZTP6rCEYrXMGwZqrwABpQ-nqXWw3eMSsswHsnlHtFa5GSM5iYY8x-1ofjFxr8LRAVcVcz-pZgyZR26b2eQTHUL2cfkjSD3ZLhesZgAvxUnolEGW1rcA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">توی مشهد یه خانم حامی حکومت تو اتوبوس، به یه دختر بخاطر حجاب حمله‌ور شد!
@News_Hut</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/news_hut/72100" target="_blank">📅 09:04 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72099">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ad662c895d.mp4?token=lG1FQkM2drTgxqgoEWOPn1ZutjnVxWbfhmZObYROku3Vf1K8t3dVc_LW1w-Xi8MNU8qDLklkAwJyi04YB2jNcC9JOHdQzeBBl-5mM7p5udzs9SmWqYC_YUWq26UHvp_erK8MvVsu49jVEuscbv0s7f6Ieg55iB9M4XrPYZskd4LBOS8t78LJwUpeQnd98FVU2wkt3eDx_G3408-mimsSJBHF3btA0WKLY9psKh8Zh9ER097HBMK80wcBfJwZWNGNgV8311Ioyah2wWnE05Zoy7JLx7MQ1Ic7YWFOmiredvMEb9XXZjsrMzOwBboKGMlG39hi_oVJYaTbcWm9jF_aaA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ad662c895d.mp4?token=lG1FQkM2drTgxqgoEWOPn1ZutjnVxWbfhmZObYROku3Vf1K8t3dVc_LW1w-Xi8MNU8qDLklkAwJyi04YB2jNcC9JOHdQzeBBl-5mM7p5udzs9SmWqYC_YUWq26UHvp_erK8MvVsu49jVEuscbv0s7f6Ieg55iB9M4XrPYZskd4LBOS8t78LJwUpeQnd98FVU2wkt3eDx_G3408-mimsSJBHF3btA0WKLY9psKh8Zh9ER097HBMK80wcBfJwZWNGNgV8311Ioyah2wWnE05Zoy7JLx7MQ1Ic7YWFOmiredvMEb9XXZjsrMzOwBboKGMlG39hi_oVJYaTbcWm9jF_aaA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شاهزاده رضا پهلوی در استودیو فاکس‌نیوز با مارتا مک‌کالوم:
«وقتی من میلیون‌ها ایرانی را در ۳۱ استان کشور به آمدن به خیابان‌ها فراخواندم، آن‌ها به صورت میلیونی حاضر شدند و ضمن اعلام حمایت، شعار پایان دادن به این رژیم را سر دادند.
آن‌ها از تمامی اقشار جامعه ایران، اقوام، ادیان و گروه‌های اجتماعی گوناگون بودند؛
این جلوه‌ای عالی از اتحاد و تنوع است.
بنابراین، هر کس که ادعا می‌کند پس از ما ایران دچار جنگ داخلی خواهد شد [باید بداند که] عامل اصلی این تفرقه و اختلاف، همین رژیم است.
همه ایرانیان می‌دانند که این رژیم بذر دشمنی و خصومت را کاشته است.
اما ایرانیان دریافته‌اند که پس از دستیابی به آزادی، قادرند دوباره برخیزند؛ درست همان‌طور که قرن‌ها فارغ از تفاوت‌های قومی یا مذهبی، در صلح و آرامش در کنار یکدیگر زندگی کرده‌اند.
و انقلاب «شیر و خورشید» در راه است.»
@News_Hut</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/72099" target="_blank">📅 07:50 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72098">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/686ffe220e.mp4?token=Tx8l3DmBqzGsbGoit_M7gX_X1mrw_BuVztNl9XknHyYqQASgmiR2RFZH6DCB_tBQPzLeNVI8Orzs4KtYIBYCfl4D5BOKsuooeqmTxbpfLq0pUv2ZzT_UREr5UwQ5QIbEz5tOmpjBua15XlQZKoSnXK8WNQO4pJYpfutgJf__BzdRg1IGAnW9CJJFlM46ty0rTJGckOawkFQcZAoQmsmE_rZ9Nkuh8PMcKciOQcCUBKjNhyP7aPd_9DfCgB1DOksgPxSPiNFDnNdr_9jIaFDuHaa5xoI12v3Opion2YQWVUTF2EQkOMrX71jpm8tjPOxmpuuHiGXCTvRjvPKhPrEd1Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/686ffe220e.mp4?token=Tx8l3DmBqzGsbGoit_M7gX_X1mrw_BuVztNl9XknHyYqQASgmiR2RFZH6DCB_tBQPzLeNVI8Orzs4KtYIBYCfl4D5BOKsuooeqmTxbpfLq0pUv2ZzT_UREr5UwQ5QIbEz5tOmpjBua15XlQZKoSnXK8WNQO4pJYpfutgJf__BzdRg1IGAnW9CJJFlM46ty0rTJGckOawkFQcZAoQmsmE_rZ9Nkuh8PMcKciOQcCUBKjNhyP7aPd_9DfCgB1DOksgPxSPiNFDnNdr_9jIaFDuHaa5xoI12v3Opion2YQWVUTF2EQkOMrX71jpm8tjPOxmpuuHiGXCTvRjvPKhPrEd1Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شاهزاده رضا پهلوی در اجلاس سالانه «کنکوردیا» (Concordia)، پرسشی را مطرح کرد که دهه‌هاست در سیاست بین‌الملل نادیده گرفته شده است: چرا مردم ایران در کانون گفتگوها قرار ندارند؟
جمهوری اسلامی با مذاکرات بی‌پایان یا سیاست مماشات تغییر نخواهد کرد. ایرانیانی که به دست این رژیم قتل‌عام شدند، خواهان آزادی بودند، نه توافق هسته‌ای یا کنترل تنگه هرمز.
انتخاب روشن است: یا همچنان بر روی رژیمی سرمایه‌گذاری کنیم که عامل بی‌ثباتی و تروریسم است، و یا در کنار مردم ایران بایستیم؛ کسانی که شرکای طبیعی جهان آزاد برای ساختن آینده‌ای سرشار از صلح، امنیت و فرصت‌های اقتصادی بی‌سابقه هستند.
@News_Hut</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/72098" target="_blank">📅 07:31 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72097">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WY7RaS1aP4LRh8UU2zrNnG6upKee4SBqMFmJK5uzc8KHH-4cM7hsOBQChkQUJXgwEgNGAbAwHPULaZlt49aBuRq7fbRjk44VsL3XwPPAqeky2gDHpZ3xCb_f-fewH_4gNl3yesSftY1gB1_jLWYggKQMfjfYWwS6Rp1L-Dvybbbegj-TjJFVFjcp3EFc5_kLyqLNE8UhjaPOKoJUhHhwMvUxU4fM8_b14ERK0p5Vsak3-4PFcmrkMQJxhcbQpnWZ8PpgauJRpbQ7mmpXs5KBigfcTOq081hvP3IeFsy2-nlIpsSLWOzrc0F60-i8-aSAFOmdLZpaZ6EpHTt_QJpHkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#فوری
؛یک منبع آمریکایی به العربیه:
آمریکا درخواست ایران برای رفع محاصره را نپذیرفت.
فرصت‌های دست‌یابی به توافق محدود است.
اختلافات و موانع بزرگی همچنان میان دو طرف وجود دارد.
@News_Hut</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/72097" target="_blank">📅 07:04 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72096">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sW1ZfSwYvxAomp-C1kBtOS3QdXTHs7cPWer4KyyPlEE9mESjptxOjBY3WC_S75zlCudh63AmbrPKXqi8BFyThB6xG5oscAoSn0S39U_dXqefbk1nObTW3AOg5SjVHCzeJ_MdWh_HF1fJx4BDLlVRzkwOxhTU7yZ8LHKUTR9zRaMy_6IADCzQpsoTpM7wS7drZYNKKfR68iyLb_n1G2v40U3uq4EpB5zVI01GpjChLBkbNVRCTlXoobxyvPEVs7otuId9xQfjY1z7AqthEbDN3Eh3c11V25XV4TWyqlXhi9oNX-uJ_HEBAi-sRxYDe06RopHumdRrYmHn07ZgGOJZJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استیو ویتکاف:
امروز در حاشیه مجمع عمومی سازمان ملل، از طریق میانجی‌هایی که در طول روز میان دو طرف در رفت‌وآمد بودند، گفتگوهای مفصلی با هیئت ایرانی انجام دادیم.
آن‌ها یک دور از مذاکرات را با موفقیت به پایان رساندند؛ مذاکراتی که امیدواریم سازنده و نویدبخش باشد. میانجی‌ها به کار خود ادامه خواهند داد.
@News_Hut</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/72096" target="_blank">📅 06:50 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72095">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/83dc83eba1.mp4?token=Q07YIMwmAUHMHTXEqSYrZA19l6H286EZgPFcnjbH3liskXtObDYSC064DPI0dPHbBORb9dyoVP8e_nc5P6QJ5sMbuC7zk-blTei9cM9ZqL2om_Ktd73GpUm1I1lzQarB38wVxoAhkxebSbPl-UkhqQBSEEnyvyGB7yF_w_eC7tu-9ZCLIOJvi7djVA41lQRZ6QMWbkrdpqGps74D3u_bx5vDCmFgB0YllTqGBGCzQozKVUbDnE5VeyZkxXJg9SDxilYiJBag8RWHfAHsqhGELjhyneCvwjbf1IBJdh6n2oH3edlgLMkr1N3ad_gdh8jfnmf5l5SXwgJhaHUPR-tWow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/83dc83eba1.mp4?token=Q07YIMwmAUHMHTXEqSYrZA19l6H286EZgPFcnjbH3liskXtObDYSC064DPI0dPHbBORb9dyoVP8e_nc5P6QJ5sMbuC7zk-blTei9cM9ZqL2om_Ktd73GpUm1I1lzQarB38wVxoAhkxebSbPl-UkhqQBSEEnyvyGB7yF_w_eC7tu-9ZCLIOJvi7djVA41lQRZ6QMWbkrdpqGps74D3u_bx5vDCmFgB0YllTqGBGCzQozKVUbDnE5VeyZkxXJg9SDxilYiJBag8RWHfAHsqhGELjhyneCvwjbf1IBJdh6n2oH3edlgLMkr1N3ad_gdh8jfnmf5l5SXwgJhaHUPR-tWow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مسعود هم رسید نیویورک
@News_Hut</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/72095" target="_blank">📅 06:33 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72094">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">یه گروه همفکری بت زدیم مخصوص دوستان بت باز
😂
✅
https://t.me/+hgTgtcXHw1k4ODA8</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/72094" target="_blank">📅 01:30 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72093">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">یه گروه همفکری بت زدیم مخصوص دوستان بت باز
😂
✅
https://t.me/+hgTgtcXHw1k4ODA8</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/72093" target="_blank">📅 01:30 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72092">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">صدای دوانفجار جدید در تنگه هرمز
@News_Hut</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/72092" target="_blank">📅 01:23 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72091">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HbDGKqnkO41_jVUCKObF1hnuSlm1AuBRNUSXrFCz9_aK21yV_z7xC6eZ2mSKBQG7uEoatt6NkghhNFskpFFjDvW4rFTw9pLPTf32mEzBPNdISCmVxBYG7FLw4J_f6d48fnXeIXRsMrtUfoBCgOB1UYsL6eWxFjJr1FQvxdAS2rHwzQfJiVJ7Eo9tnW3KvOs44eYw0pBlevfNRhMAYzIuGKqo-eLM_noppkukzRaJtCOTd96544NmOmiOuXPGKLueSBJ2XFfOyNZFOElmcrf_06f83dXy1tLKTu9QrGvfzxovcqKfhIXE8s_8BUddhD1n-5BPGOwCt2cYbQIaaJxlSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وای‌نت:
انتظار می‌رود سخنرانی نتانیاهو در سازمان ملل به شدت بر ایران متمرکز باشد و به گفته‌ی ایدز، این سخنرانی حاوی «غافلگیری‌های» نامشخصی خواهد بود.
هیئت نمایندگی اسرائیل همچنین خود را برای احتمال مزاحمت یا خروج هماهنگ‌شده در طول سخنرانی آماده می‌کند.
@News_Hut</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/72091" target="_blank">📅 01:20 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72090">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">ایرنا: صدای انفجار در حوالی جزیره قشم به گوش رسید
@News_Hut</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/72090" target="_blank">📅 01:11 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72089">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3046a77aed.mp4?token=tY-XU1B1dEIp_tLNwwwu5ntR1xfDcuc4Krmrf_WTctqC8e_ekZC33VzrP71VdjdzCmlOkTqQQenmRNoervcYc5P_fK7pfZCNvocCyjoodH5KFOByfgylcbV6VtbRaTg1aIRZDKKv1HPVDgT0XUQv-_z12oRyBO9G10rr9VCcqiGpRA9Ft40a1O5cPfdiGpzApxFg_wfYEKq_DOsfE99sKo-kVlSGUy3Sf1B1U46Mhajout4xmHUcIW2gP4of0pnlbJDXSc9XJ7MfRJ718nt1TQSYGn5YR2iIQ6vVc3F-GGehjcw7vektTjWBOyjSqSuKgG6gSr9SWy_73rJPsF9-Yg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3046a77aed.mp4?token=tY-XU1B1dEIp_tLNwwwu5ntR1xfDcuc4Krmrf_WTctqC8e_ekZC33VzrP71VdjdzCmlOkTqQQenmRNoervcYc5P_fK7pfZCNvocCyjoodH5KFOByfgylcbV6VtbRaTg1aIRZDKKv1HPVDgT0XUQv-_z12oRyBO9G10rr9VCcqiGpRA9Ft40a1O5cPfdiGpzApxFg_wfYEKq_DOsfE99sKo-kVlSGUy3Sf1B1U46Mhajout4xmHUcIW2gP4of0pnlbJDXSc9XJ7MfRJ718nt1TQSYGn5YR2iIQ6vVc3F-GGehjcw7vektTjWBOyjSqSuKgG6gSr9SWy_73rJPsF9-Yg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پرزیدنت
ترامپ:
یا به توافق می‌رسیم، یا کار خیلی خیلی سریع تمام خواهد شد.
آن‌قدر سریع تمام می‌شود که سرتان گیج می‌رود.
@News_Hut</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/72089" target="_blank">📅 01:11 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72088">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/qw4mZavP9ILNgx2yRbUMoj1lVDGhDondmpu2r_mSqhfd0YIMqNyH_BY-Mo0gW2lDIAlToF1atGjo0k6lkjg-H9o4iBq6bloSXhe1j1NwZBNETzFhQaLxvkp2JknTNFFsQmzg8vgKDdCes_litKDavWTI-AbFa0VoYyIoYuDkbsL9-ysxixlcXLEGSHzkQ2eBnUfiIOIb_R7YfF7LLxhswO6-j4FQodyn1ol5DXeI3zALd-kwpw-OTbXthOmRYj-g1pRFgxqKBZO7WuNW70vGA-PRt7a0-3ysjoOxQc9M-IjMzLKn4cHLgIsjbH7og2288Eh-CKMVZtyUZd_BfGwAYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انتظاری که تندروهای جمهوری اسلامی از پزشکیان تو نشست سازمان ملل دارن:
@News_Hut</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/72088" target="_blank">📅 01:01 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72087">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">تابستون هم تموم شد و رسما وارد پاییز شدیم...
@News_Hut</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/72087" target="_blank">📅 00:56 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72086">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">ساعت ۰۰:۴۷ بامداد چهارشنبه؛ یک انفجار در محدوده تنگه هرمز رُخ داد.
@News_Hut</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/72086" target="_blank">📅 00:54 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72085">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/61a836832d.mp4?token=o7fbvRF330jWPVmARiTyfrh_86hESxF4yM_1m_I2jfIO1_BL5VJWQvytajEgxBRYgfqp2_4ua_5jDY7iw6fhGGqOW77VggsPJfcf4WA251oDwaRLIhe5de1ah4Se_DbJZkt1mukDXtb8k3bLFIh7PJluYEfIgdcVZls2XrFeSYOwefAwNCvJKuW0V26uyY3wWOtXLiPwudzmI_IDtwR7uEAA3kqU5JPvUBSullXTfXG0J0P4Q4mZU220dsiUb4JecE6GbL9Bmx-i9ROCkABGcTu6gcos_C9SteKp6gJubJEJwYnETrxdkTo4iYSd3xtARvIyiMXl1etuYtRmcFmY14i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/61a836832d.mp4?token=o7fbvRF330jWPVmARiTyfrh_86hESxF4yM_1m_I2jfIO1_BL5VJWQvytajEgxBRYgfqp2_4ua_5jDY7iw6fhGGqOW77VggsPJfcf4WA251oDwaRLIhe5de1ah4Se_DbJZkt1mukDXtb8k3bLFIh7PJluYEfIgdcVZls2XrFeSYOwefAwNCvJKuW0V26uyY3wWOtXLiPwudzmI_IDtwR7uEAA3kqU5JPvUBSullXTfXG0J0P4Q4mZU220dsiUb4JecE6GbL9Bmx-i9ROCkABGcTu6gcos_C9SteKp6gJubJEJwYnETrxdkTo4iYSd3xtARvIyiMXl1etuYtRmcFmY14i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره ایران:
استیو و جرد امروز جلسه بسیار پرباری با میانجی‌های ایران داشتند. باید دید در ادامه چه پیش می‌آید.
به گمانم انگیزه و شتاب زیادی برای دستیابی آن‌ها به توافق وجود دارد؛ این همان چیزی است که از همه می‌شنویم.
@News_Hut</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/72085" target="_blank">📅 00:49 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72084">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9e28a4d4c0.mp4?token=BqLHtGSqct5rvsac3ccJJZf9pD2dNAG1wd0t3Gbf5x9ehsLgC4ZFSTi0G9ZPLIdCc111kHRfxFskbBQTY2C5wculTEfGjneWwOCtSaKq9RHgh050ddVkFO4a9gbzVzNM0pMu-lc0wVOFXCVuQubstxO5AbVeK0CSEBrBPp4UxdaZKY5Kh-MJnNPUNrSuaSH_7IgUsM5JvZck25f_uMbdrbAH3NkLmLXZCemDovI002xdt_ELmVw6XROOt1AkdbuWisMsfJID0KXXKr4xivoAmtbeUUjgSr4iVS3qLdUu7nogY2jRGz7xAOOa0It6-ON3f6idSyNlrW8JYUkKJ9GzZg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9e28a4d4c0.mp4?token=BqLHtGSqct5rvsac3ccJJZf9pD2dNAG1wd0t3Gbf5x9ehsLgC4ZFSTi0G9ZPLIdCc111kHRfxFskbBQTY2C5wculTEfGjneWwOCtSaKq9RHgh050ddVkFO4a9gbzVzNM0pMu-lc0wVOFXCVuQubstxO5AbVeK0CSEBrBPp4UxdaZKY5Kh-MJnNPUNrSuaSH_7IgUsM5JvZck25f_uMbdrbAH3NkLmLXZCemDovI002xdt_ELmVw6XROOt1AkdbuWisMsfJID0KXXKr4xivoAmtbeUUjgSr4iVS3qLdUu7nogY2jRGz7xAOOa0It6-ON3f6idSyNlrW8JYUkKJ9GzZg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره ایران:
امیدوارم پیش از آنکه خیلی دیر شود، هرچه سریع‌تر کار درست را انجام دهند.
می‌دانید، زمانی فرا خواهد رسید که دیگر خیلی دیر شده باشد و ما دیگر فرصتی برای اینکه اجازه دهیم آن‌ها به عنوان یک ملت باقی بمانند، نخواهیم داشت.
@News_Hut</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/news_hut/72084" target="_blank">📅 00:47 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72083">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">تسنیم:
دیدار استیو ویتکوف، نماینده آمریکا، با عباس عراقچی، وزیر امور خارجه ایران، در حاشیه مجمع عمومی سازمان ملل متحد، پس از درخواست‌های مکرر طرف آمریکایی برگزار شد.
ایران اعلام کرد که از این جلسه برای بیان شرایط خود برای بازگشایی تنگه هرمز، از جمله لغو فوری محاصره دریایی، آزادسازی دارایی‌های مسدود شده ایران و پایان جنگ در همه جبهه‌ها، استفاده کرده است.
@News_Hut</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/72083" target="_blank">📅 00:43 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72082">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/61a836832d.mp4?token=YAADPdKKVAgQjNwd0ziDd7I3oaSbOqSV0GyHugFHclndHb82q9IcwRv9UdEz5g4Q0JPMU8eahelHdDWYchfwWfVfZb6nSjjU4WvwgcLQLBVTcGqoabgGJYmDj6faZ7SWMqsIjqyiL5ZrfTQoVBbCZTrgP2dD337c8DMSGb2uE09z2dTI7v6lEKvJs0uiFyQuyBsiK3ajdptW8AWzQNZSkJFMbjPBehfYBysUVnf2lk6oSMzbs0s7M6jLXcw6_AcPaoL9OfuV1WjukznIbATAC_tnjk8u47xr4MWuhGND1a3gSAh7-flHcwAtq7aohlU0Ki6H8ytOzTwkoiN30zHPL4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/61a836832d.mp4?token=YAADPdKKVAgQjNwd0ziDd7I3oaSbOqSV0GyHugFHclndHb82q9IcwRv9UdEz5g4Q0JPMU8eahelHdDWYchfwWfVfZb6nSjjU4WvwgcLQLBVTcGqoabgGJYmDj6faZ7SWMqsIjqyiL5ZrfTQoVBbCZTrgP2dD337c8DMSGb2uE09z2dTI7v6lEKvJs0uiFyQuyBsiK3ajdptW8AWzQNZSkJFMbjPBehfYBysUVnf2lk6oSMzbs0s7M6jLXcw6_AcPaoL9OfuV1WjukznIbATAC_tnjk8u47xr4MWuhGND1a3gSAh7-flHcwAtq7aohlU0Ki6H8ytOzTwkoiN30zHPL4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره ایران:
امروز یک نشست فوق‌العاده و مثبت بین کوشنر و ویتکاف با نمایندگان ایرانی داشتیم
واقعا در مسیر خوبی حرکت می‌کنیم اونا خیلی میخان توافق کنن اینو همه میگن
شتاب قابل توجهی برای مذاکره داشتیم
اقتصاد ایران رو منزوی کردیم اقتصاد اونارو نابود کردیم این خیلی خوبه
تنگه هرمز رو از مین ها پاکسازی کردیم و نفت جریان داره همین الان
@News_Hut</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/72082" target="_blank">📅 00:39 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72081">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cb4086006d.mp4?token=Yc1BF6D64N2yjHUKyYbHX6nZQ3RMRd3b7CHF3LXJ4PpzmwnoqHDXeOv1vTPSjVJbsVFYBjbzoEzJxYBIqX9pnMkFSTeuMLAIpbT1lFHErB0IoaYU9N4xRjR9VhJx9chzOGYoxUYDBrmU6ncSV-7e1TSv1Wbuuh3bjP1f1cnr0xv20yDYlRD62Iss8pxAohonEymtFARN7b-4ogoo3A5kegMPTNamw9-d-5manJHu92yWq0ntDtQn_5dR_-EybFg4tIAa7tdN2VphiFobRRCoENqQEV2tma-emYc3r1XaO_2mzHKN3-Br6VvFDAu08p1zzUPEk5E9ssq0R7wd9zhOHQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cb4086006d.mp4?token=Yc1BF6D64N2yjHUKyYbHX6nZQ3RMRd3b7CHF3LXJ4PpzmwnoqHDXeOv1vTPSjVJbsVFYBjbzoEzJxYBIqX9pnMkFSTeuMLAIpbT1lFHErB0IoaYU9N4xRjR9VhJx9chzOGYoxUYDBrmU6ncSV-7e1TSv1Wbuuh3bjP1f1cnr0xv20yDYlRD62Iss8pxAohonEymtFARN7b-4ogoo3A5kegMPTNamw9-d-5manJHu92yWq0ntDtQn_5dR_-EybFg4tIAa7tdN2VphiFobRRCoENqQEV2tma-emYc3r1XaO_2mzHKN3-Br6VvFDAu08p1zzUPEk5E9ssq0R7wd9zhOHQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کارشناس صداوسیما:
آمریکا داره آب خلیج فارس رو می‌ریزه تو امارات تا تنگه هرمز خشک بشه
😂
@News_Hut</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/72081" target="_blank">📅 23:31 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-72080">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/19a38b8192.mp4?token=l6zSBKaSRlrM7E5ItVUd5sHuISqOmY4G2hT4oNlgs-jqlYUpldmWK_z5n73kKVzZfoOOEz1AuaaHNMMxvu2l2A7V2lLWyuQAjeCWEBocTOrmvlCQwEavchqrUavV6E7lUWCB1S4VR2QRO-iEzhMNp4I2WyglLXKFveYUoOZXMs6cGQhGnFYJzDMxKU5BaVcjSbKQLcI5__adzs8rk0wIQ8U5298qAIf4mM9ARBw_UYeTDmcX2ayjjfErDZmiF2vOAjkNur2lG9juUeshHKIC6ElJFKURIt93v9ZOQaXVBYANZyWSIKonTIqAt1Sp24DUIulV-vYGYcoVCdLRHYG3fg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/19a38b8192.mp4?token=l6zSBKaSRlrM7E5ItVUd5sHuISqOmY4G2hT4oNlgs-jqlYUpldmWK_z5n73kKVzZfoOOEz1AuaaHNMMxvu2l2A7V2lLWyuQAjeCWEBocTOrmvlCQwEavchqrUavV6E7lUWCB1S4VR2QRO-iEzhMNp4I2WyglLXKFveYUoOZXMs6cGQhGnFYJzDMxKU5BaVcjSbKQLcI5__adzs8rk0wIQ8U5298qAIf4mM9ARBw_UYeTDmcX2ayjjfErDZmiF2vOAjkNur2lG9juUeshHKIC6ElJFKURIt93v9ZOQaXVBYANZyWSIKonTIqAt1Sp24DUIulV-vYGYcoVCdLRHYG3fg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">توی آلمان یه دختر تریان (انسان‌های که فکر می‌کنن حیوانن) به یه خانم حمله می‌کنه و گازش می‌گیره، به پلیس اطلاع داده شد، هر چقدر از دختر اسم و فامیل پرسیدن فقط پارس کرد، پلیس هم اون رو برد مرکز نگهداری از حیوانات
😐
@News_Hut</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/72080" target="_blank">📅 23:01 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-72079">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/956bc67dd9.mp4?token=rreyBrJcfr69OmacU_67GjErzFr_eM8660pNf9Ib1as_Fr-yjhhKB0RshyjR4Iq29adGNUJFdhIEP6f-PM0vjV_dkTWhGBZGlnr9d0VDjQ2p_zebWV0JiVTSgSmWInIsZ6zoZoUm9Fe99YlDyBvy2DnKn4eqRhosdi5EFEiiOJymieSMaKvr0w_eqGuuyezp8Wnv99MHaKu1FS9whJbma4QktNGUBb9tMrq5sbxnY1KBsgbN-rLyuNbDwN3ZceIbc69AScASsfajQjEMq8fL4VFj8_R6MnypmQMYjm6duA2jZmCCJYiLpaH5ASi4mdvhzO8qVL0f2cgXTC3OjHGaEg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/956bc67dd9.mp4?token=rreyBrJcfr69OmacU_67GjErzFr_eM8660pNf9Ib1as_Fr-yjhhKB0RshyjR4Iq29adGNUJFdhIEP6f-PM0vjV_dkTWhGBZGlnr9d0VDjQ2p_zebWV0JiVTSgSmWInIsZ6zoZoUm9Fe99YlDyBvy2DnKn4eqRhosdi5EFEiiOJymieSMaKvr0w_eqGuuyezp8Wnv99MHaKu1FS9whJbma4QktNGUBb9tMrq5sbxnY1KBsgbN-rLyuNbDwN3ZceIbc69AScASsfajQjEMq8fL4VFj8_R6MnypmQMYjm6duA2jZmCCJYiLpaH5ASi4mdvhzO8qVL0f2cgXTC3OjHGaEg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">علی فروتن، عمو فیتیله‌ای:
این روزا وقتی دختر، پسرا میخوان باهم دوست بشن، خیلی برای همدیگه لاف میزنن!
معیار انتخابم که شده پول، قیافه، خوش گذرونی و... به نظرتون گند نزدیم به عشق و عاشقی؟
یه زمانی آدما دنبال کسی بودن که نه تنها حرفشون، بلکه سکوتشون هم بفهمه. به خودت احترام بذار و با هرکسی وارد رابطه نشو.
@News_Hut</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/72079" target="_blank">📅 22:15 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-72078">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">امیر قطر در مورد غزه:  اسرائیل به نوبه خود باید به تعهدات خود به طور کامل عمل کند: توقف قطعی عملیات، خروج از نوار غزه، لغو محاصره و ارسال بی‌قید و شرط کمک‌های بشردوستانه.  @News_Hut</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/72078" target="_blank">📅 21:49 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-72077">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/88614b72e8.mp4?token=cZicgZJprQ31YJBGo2KffGS30XM3LYQX-0AkVqD7DO4KJvJJhWmpnWR6d_5Yn86EpK8AOMo9v9oRT-gOp37baUyNPqA9oS3scTbdJfBYzTYqWbynkMxqcBNtUMhyXC70WIJ9NaDQRxkfqbWuBA1rU9oMwhEwu8GlSGo1KG0d_VY92X9VPb2cIW7oaozMd_-6Iwreh34wz9FoaCWgIZAZV41S9gyclQYU7hZMzN6KS1VcuOMzyAyiQkNBNe0TLFmDqQmey1MLI0vNjBLPiixWejSw8bVLLPI6x73JedZ2XgcrNJ9xApQmzQlkdxTf3H43m5ZrUeTfx-EBhNSI-0m7bA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/88614b72e8.mp4?token=cZicgZJprQ31YJBGo2KffGS30XM3LYQX-0AkVqD7DO4KJvJJhWmpnWR6d_5Yn86EpK8AOMo9v9oRT-gOp37baUyNPqA9oS3scTbdJfBYzTYqWbynkMxqcBNtUMhyXC70WIJ9NaDQRxkfqbWuBA1rU9oMwhEwu8GlSGo1KG0d_VY92X9VPb2cIW7oaozMd_-6Iwreh34wz9FoaCWgIZAZV41S9gyclQYU7hZMzN6KS1VcuOMzyAyiQkNBNe0TLFmDqQmey1MLI0vNjBLPiixWejSw8bVLLPI6x73JedZ2XgcrNJ9xApQmzQlkdxTf3H43m5ZrUeTfx-EBhNSI-0m7bA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">امیر قطر در مورد غزه:
اسرائیل به نوبه خود باید به تعهدات خود به طور کامل عمل کند:
توقف قطعی عملیات، خروج از نوار غزه، لغو محاصره و ارسال بی‌قید و شرط کمک‌های بشردوستانه.
@News_Hut</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/72077" target="_blank">📅 21:48 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-72076">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9803dc4ebc.mp4?token=hcJ7-atKiH6aT6rSC5t_6pf39EZWHbJGCI69cqwxy6xj5yftmTuhYCV6rLIqdVG8fBlY_5shIKy9dYC6Z3UPg-Go4j-qJdR8OcPO13w6WLsf5-TSDJiv0ysmNh7Ce51Jk8lQWPaFQ1XfryxFH9jeytk6GWU6501YasERVqmsZvFj_H139ea_VU8pqTDIaUI34loLRHYBLyMm4k7954FGak4cuvu_BdJu-mIKw2C3PH9Hi7BF5zipkW0v6zpsXC4wlCdqOV9VKWCmyk5hJb5aiL8EGwyCHxXB9ftzZEgvBo2l5duCtK_84tMC7em6kHnnwbjawaxMTc_85QhJgiBcBA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9803dc4ebc.mp4?token=hcJ7-atKiH6aT6rSC5t_6pf39EZWHbJGCI69cqwxy6xj5yftmTuhYCV6rLIqdVG8fBlY_5shIKy9dYC6Z3UPg-Go4j-qJdR8OcPO13w6WLsf5-TSDJiv0ysmNh7Ce51Jk8lQWPaFQ1XfryxFH9jeytk6GWU6501YasERVqmsZvFj_H139ea_VU8pqTDIaUI34loLRHYBLyMm4k7954FGak4cuvu_BdJu-mIKw2C3PH9Hi7BF5zipkW0v6zpsXC4wlCdqOV9VKWCmyk5hJb5aiL8EGwyCHxXB9ftzZEgvBo2l5duCtK_84tMC7em6kHnnwbjawaxMTc_85QhJgiBcBA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره ایران:
آن‌ها دیداری بسیار خوب و سازنده داشتند. دیدار دیگری نیز برای آینده‌ای بسیار نزدیک برنامه‌ریزی شده است.
@News_Hut</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/72076" target="_blank">📅 21:37 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-72075">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c847d96020.mp4?token=EgLPXG73bCHyd00nbkq4ZKabFdY43-jWtwb7lFv03OErdu1Am_2K-H0W2YCjmPOiTh4aKpNRE6uTZmkiKB1xUgcQG6tk1Ej_8PNWCJ7EBgiOasxM6v3jd7pC2SrcKox-xgDtDQApPhwf8iB9_VnAgocplc5aHbnsaGmiBF4CsjNqhHYQ_sKyeUZkK2iZpl874wPuuod-9_3LuYZMM8UhVu4w-wY7wVPwU-a7aOuV7b7TrEMz3kg7TSP5ca1vFfJMq7HAt4y7bToPjCbatRwJBrtrqmSebK6OEWmTRi23sbBui-gBdVGjY6r023PSgiCwVWnNkJc47y6j1lG_Xbumeg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c847d96020.mp4?token=EgLPXG73bCHyd00nbkq4ZKabFdY43-jWtwb7lFv03OErdu1Am_2K-H0W2YCjmPOiTh4aKpNRE6uTZmkiKB1xUgcQG6tk1Ej_8PNWCJ7EBgiOasxM6v3jd7pC2SrcKox-xgDtDQApPhwf8iB9_VnAgocplc5aHbnsaGmiBF4CsjNqhHYQ_sKyeUZkK2iZpl874wPuuod-9_3LuYZMM8UhVu4w-wY7wVPwU-a7aOuV7b7TrEMz3kg7TSP5ca1vFfJMq7HAt4y7bToPjCbatRwJBrtrqmSebK6OEWmTRi23sbBui-gBdVGjY6r023PSgiCwVWnNkJc47y6j1lG_Xbumeg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره ایران:
امروز، حدود یک ساعت پیش، گفتگویی انجام شد. گفتگو بسیار خوب پیش رفت و یک ساعت پیش به پایان رسید.
این نشستی بود که سه ساعت به طول انجامید.
مسئله، عظمت — یا عظمتِ بالقوه — و یا نابودی است.
در یک حالت، صحبت از نابودی است؛ و گزینه دیگر، عظمتِ بالقوه است. [ایران] می‌تواند کشوری بزرگ باشد.
@News_Hut</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/news_hut/72075" target="_blank">📅 21:34 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-72074">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a9e59383b3.mp4?token=twcy4yuQeA1zGW81x-wu-4wNCjH0ZvhrcWsWRITxUWjIT-28jCCmsF0jy_8vZ1HD72VQSXy3bCPjcxmpftXHvs88m3SRLDgb6KA841_YWHmau_1ZSRQO9HxXDFA1ZOt12Zgf1LJl3PTGIs2ptisA2G14UyeN_1X6gtskzDOX2vYOtrIUgTqKW-m1lLB4RGuSr_hOvT22CxSGnj-hLEXR24xxuInt0Qf4zYJlLFp_FwdjQTM1QV5i1D8vC-Pk_IDJ_xJwPeZcyATxTtiSce9c-IpyzaJVB2qz9KdWMNdssAbuORx11DWLG2Rf15QGpeQutRCOu2cTKj_UCv6WRzhzXg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a9e59383b3.mp4?token=twcy4yuQeA1zGW81x-wu-4wNCjH0ZvhrcWsWRITxUWjIT-28jCCmsF0jy_8vZ1HD72VQSXy3bCPjcxmpftXHvs88m3SRLDgb6KA841_YWHmau_1ZSRQO9HxXDFA1ZOt12Zgf1LJl3PTGIs2ptisA2G14UyeN_1X6gtskzDOX2vYOtrIUgTqKW-m1lLB4RGuSr_hOvT22CxSGnj-hLEXR24xxuInt0Qf4zYJlLFp_FwdjQTM1QV5i1D8vC-Pk_IDJ_xJwPeZcyATxTtiSce9c-IpyzaJVB2qz9KdWMNdssAbuORx11DWLG2Rf15QGpeQutRCOu2cTKj_UCv6WRzhzXg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">به گفته خانم دکتر؛
مردهایی که به‌طور مداوم رابطه جنسی دارن، طول عمرشون تا 50 درصد افزایش پیدا می‌کنه و همچنین خطر ابتلا به بیماری‌های قلبی هم تا 45 درصد کاهش پیدا می‌کنه.
-در زنان هم باعث میشه سرطان سینه و کیست تخمدان نگیرین.
@News_Hut</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/news_hut/72074" target="_blank">📅 21:30 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-72073">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bc4e3a7b84.mp4?token=UVrWYPavUrclgZNNiftdEIXdFauwi4K1uq0JjzWhJ8biaZA2oeRh4nVxZu3la4tOdxqYWzxkR98mvKcNokeA97Tdy3H31qVMtRzj46zWjBluA-sccXvrVQIKgIBzLv9y68rWLZcpM0DQoEd5gxzFXBaymKKEEa8aFqyALHp8WsC7tVcj7z68hjOwc8kJWt9L_My9kQF-KKemJ0LjyBtzOVc1qaGG8gHMeQJAj1nIQ1CyNJsw6JfQ6okGaZmx0IfQGaje6A1MkgVp-vt_XbZtazr4FsUZWkfpDnfuk46G9SMjLOnXbgsSEeT33ATF5wMGo0KjKP7Fam-eKMu8NeGL9A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bc4e3a7b84.mp4?token=UVrWYPavUrclgZNNiftdEIXdFauwi4K1uq0JjzWhJ8biaZA2oeRh4nVxZu3la4tOdxqYWzxkR98mvKcNokeA97Tdy3H31qVMtRzj46zWjBluA-sccXvrVQIKgIBzLv9y68rWLZcpM0DQoEd5gxzFXBaymKKEEa8aFqyALHp8WsC7tVcj7z68hjOwc8kJWt9L_My9kQF-KKemJ0LjyBtzOVc1qaGG8gHMeQJAj1nIQ1CyNJsw6JfQ6okGaZmx0IfQGaje6A1MkgVp-vt_XbZtazr4FsUZWkfpDnfuk46G9SMjLOnXbgsSEeT33ATF5wMGo0KjKP7Fam-eKMu8NeGL9A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ: بانوی اول ما کجاست؟ یک جایی همین اطراف است.
ملانیا:
👋
@News_Hut</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/news_hut/72073" target="_blank">📅 20:50 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-72072">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">اکسیوس:
چند کشور عربی در تلاش‌اند زمینه برگزاری یک دیدار سطح‌بالا میان دونالد ترامپ و مقام‌های ایرانی را در حاشیه مجمع عمومی سازمان ملل در نیویورک فراهم کنند.
@News_Hut</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/news_hut/72072" target="_blank">📅 20:40 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-72067">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn5.telesco.pe/file/77b06fbdcc.mp4?token=hIOUDUNVWWaUXIRxwZdN8AKG-fpEgx1oiFLHuWlqm8dSyeXea1XbEJRGanLweWQnvuZ8livo0BjQE0mhGr37zCTB-O36mpDa9roqe-c5Vr-LlcHSnxm6K7FT5cnWYzCd5BMhT5QQDknmDflBDdcDQK6LiIG4AKOGDy8Snx4sWEuyNuOvBrElO_Q5wl_1Xprmg1MY0TDHR2oFsdu3_0MLFIAQBrwuYeIoNdi5Qa_rANjCoJecUK2eCnzDhNgC9FA6PVut1lV7uwhESASJvWqrBEZEUj4xCGszdaOcj_4j1KmPUnDZrRSMmNY2NXltCk1m4mpYl2pfoPxZ45I-1PnqUQ" type="video/mp4">
</video>
<br>
<a href="https://cdn5.telesco.pe/file/77b06fbdcc.mp4?token=hIOUDUNVWWaUXIRxwZdN8AKG-fpEgx1oiFLHuWlqm8dSyeXea1XbEJRGanLweWQnvuZ8livo0BjQE0mhGr37zCTB-O36mpDa9roqe-c5Vr-LlcHSnxm6K7FT5cnWYzCd5BMhT5QQDknmDflBDdcDQK6LiIG4AKOGDy8Snx4sWEuyNuOvBrElO_Q5wl_1Xprmg1MY0TDHR2oFsdu3_0MLFIAQBrwuYeIoNdi5Qa_rANjCoJecUK2eCnzDhNgC9FA6PVut1lV7uwhESASJvWqrBEZEUj4xCGszdaOcj_4j1KmPUnDZrRSMmNY2NXltCk1m4mpYl2pfoPxZ45I-1PnqUQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آتش‌سوزی در پایانه لجستیکی شرکت «نووا پوشتا» (Nova Poshta) در حومه روستای اوساتوو (Usatovo) در منطقه اودسا اوکراین، پس از حمله موشکی.
علاوه بر این، ممکن است انبارهای متعلق به شرکت‌های دیگر در آن نزدیکی نیز دچار حریق شده باشند؛ چرا که مجموعه‌ای کامل از انبارها در آن منطقه قرار دارد.
@News_Hut</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/news_hut/72067" target="_blank">📅 20:10 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-72066">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ik_Yn7oXv02QfJvi-tIHZNSrQORMMmjJoj_im0NxrK0QdFLy9fw-28Wwwo1gvjhlXwGL0UQZn01yrIGB7a2i51BXlOtQa3ErBZSANh1JcrHccMQSxckjhkUTLfMTv7cDRpazaZoaRaJVWNkZmDyi0muB2yY6GlCxAoKUNvasnliuE0LX9L-6gF4fBra9__0xRue-Uv0zCp6Qd72SkgVSGi4mPw9butQpfZ-rxaGBwISPTxYXXMcVcLti0lDBFSWCvDpe3sKMBIEnhSRNMLhtLEY5HNur4-wkRMm4xVTT9uXgWL8LnuB4XIiToOd_U4M7j6Gk5MQmhEnPcdQH0F5ymw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شاهزاده رضا پهلوی وارد نیویورک شده است؛ ایشان قرار است در «اجلاس کونکوردیا» سخنرانی کرده و دیدارهای خصوصی با نمایندگان دیپلماتیک کشورهای حاضر در مجمع عمومی سازمان ملل متحد داشته باشد.
با این حساب دونالد ترامپ، بنیامین نتانیاهو، مسعود پزشکیان و شاهزاده رضاپهلوی هم‌زمان توی نیویورک هستن.
@News_Hut</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/news_hut/72066" target="_blank">📅 19:34 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-72065">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">فعالیت مدارس استان هرمزگان ۲ هفته مجازی شد؛
معاون سیاسی، امنیتی و اجتماعی استاندار هرمزگان از مجازی شدن فعالیت آموزشی تمامی مدارس استان در همه مقاطع تحصیلی از شنبه به مدت دو هفته، با هدف صیانت از سلامت دانش‌آموزان و حفظ کیفیت فرآیند آموزشی خبر داد!
@News_Hut</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/news_hut/72065" target="_blank">📅 19:22 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-72064">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">در ۲۳ سپتامبر، فعالیت تمام شرکت‌های هواپیمایی ایران در سراسر جهان متوقف خواهد شد.</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/72064" target="_blank">📅 19:01 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-72063">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/079b2c614f.mp4?token=VHmxSPmNBXoRdKJok5YBQxVgh7nbuvSFAebK-K2oO7kkXOln7-iixaoW5s51hkk-zwDQnOWAW20pf5qvSJ2yV1VcAWEPh8VYzrAciR_r9x4GBHU-ZNESUxpNlKf083805gjVoB0FvEAEn-gQcHVgjH6Joy0sZXsxZxUtOxXN-PStOBMxjxZ2Nk2uPXy2SVYFaUIeVlCC1NPBbFZIQT1TTseCnmwcGeiNfxj7hgVYzgEWbVjYN5P3_lpb9DZbLuhlWlGoNK5Odcn4WCuyETL_r87nnuqHQaZ4juXNSLSik7oRoDu9SJWzQCcGfkrJ3uanwn2Yw5AYz97Gj3ANMMqPZxzOlHAdJwsbWC_DTSTD3XY4FwKG0iMoYwzhYax9S3zwk31sOhFCiISb1frvydpv7oZ0iRCSOb6eJi-1d1iqRe0OtkonBHYHWE5fPmIpR_66SYWmchu20wnhK8glvLWbR94CqgPi361jUAYGwss64AzOjUV6ERvmZZWCcPGxCNMhGviTDsdkSRsWYe4YmtaeEKO7qaoCbvh4R-NpTrf6NJJgd2h8gCdgZU_CsUImaB691XQn-rliIoRW7R408Iq0xMO7mxl6bSSN573qvuY2cQkAy6KdWkVX9aqf75MqS4aXpTWlKO8uUq5Wgf3QtvPuxjABzsJP1pxf9FwsfVge3lQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/079b2c614f.mp4?token=VHmxSPmNBXoRdKJok5YBQxVgh7nbuvSFAebK-K2oO7kkXOln7-iixaoW5s51hkk-zwDQnOWAW20pf5qvSJ2yV1VcAWEPh8VYzrAciR_r9x4GBHU-ZNESUxpNlKf083805gjVoB0FvEAEn-gQcHVgjH6Joy0sZXsxZxUtOxXN-PStOBMxjxZ2Nk2uPXy2SVYFaUIeVlCC1NPBbFZIQT1TTseCnmwcGeiNfxj7hgVYzgEWbVjYN5P3_lpb9DZbLuhlWlGoNK5Odcn4WCuyETL_r87nnuqHQaZ4juXNSLSik7oRoDu9SJWzQCcGfkrJ3uanwn2Yw5AYz97Gj3ANMMqPZxzOlHAdJwsbWC_DTSTD3XY4FwKG0iMoYwzhYax9S3zwk31sOhFCiISb1frvydpv7oZ0iRCSOb6eJi-1d1iqRe0OtkonBHYHWE5fPmIpR_66SYWmchu20wnhK8glvLWbR94CqgPi361jUAYGwss64AzOjUV6ERvmZZWCcPGxCNMhGviTDsdkSRsWYe4YmtaeEKO7qaoCbvh4R-NpTrf6NJJgd2h8gCdgZU_CsUImaB691XQn-rliIoRW7R408Iq0xMO7mxl6bSSN573qvuY2cQkAy6KdWkVX9aqf75MqS4aXpTWlKO8uUq5Wgf3QtvPuxjABzsJP1pxf9FwsfVge3lQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نظر ترامپ درباره هوش مصنوعی:
هر کس در حوزه هوش مصنوعی پیروز شود — باید این نکته را به خاطر داشته باشید — و حالا می‌گویم هر کس در حوزه «هوش برتر» (SI) پیروز شود، برنده نهایی است.
آن‌ها همان گروهی هستند که پیروز می‌شوند.
و ما در حال حاضر با اختلاف زیادی نسبت به چین و سایر کشورها پیشتاز هستیم. ما این وضعیت را حفظ خواهیم کرد؛ مسیری بسیار مستقیم و موضعی بسیار قدرتمند را در پیش خواهیم گرفت.
من نمی‌خواهم مانع رشد پدیده‌ای شوم که ابعاد آن از انقلاب صنعتی هم فراتر خواهد رفت.
بسیاری می‌گویند این تحول حتی از انقلاب صنعتی یا خودِ اینترنت هم بزرگ‌تر خواهد بود. و ما بسیار محتاط عمل خواهیم کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/news_hut/72063" target="_blank">📅 18:43 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-72062">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/36fc0e287a.mp4?token=idAC0EsNXxK9Ospshr4YWoSgXjgiiSh6s9VUIVpBd0siII8B6qqcGISEPyzPisIyfiJvCf908hTX40iVKSVOeuaHEyk3kYi_gtdh603UPN1NAe938tXkAA61i_5lzXExgmASUx0iztK-NV0fpbXzfPV6iQhQ_wxdQIyR40PVWaJA7SnkREbZ-jWbC82egjEUdYJmPURZWVyIEMk5a1OvHTeJbMUlEHzm5N5VyAqFjCf5WwHUOTn-3JfxoYg6t-N-zawRF1ytbECS-LUf-77rpT8xR_APd6uw_Q9yI8b2rYeZKpt-9q2kX0I5UUju_UyyGsNbKQLJGZNme8dtPXFNI55jf2XIK2NVlfvzdPmGb0VUm8t7qb1EXEnqrb7uaOva07VmqtBnc_MDIKE9aE5KhsbOAf13W9C5jMQKIkxkl4W1F-ELqf1JsYWLPm9t8qNhNerpDdozMIxFXWV1cIUR1SaAsxvwSOwdkdVP45Q2TFTorhqhAY6qwMoIg3UTZ_jQMvH1VoYBFAKMVlwyy71_ETBlMolNr6y_Ac4DbTBdpbh0ElG6RuGb-s_RKuayv3ZnFeelXAJ5cH4C9X3BMtfN_T9Nv8d9jt125YQCjPNY8MRQ_PO-S5ELt_DdpArMbhmcBA1bxs4Atc-tLgQQ1Qbd9DDcNH1ilc8dTxqIGPdwuw4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/36fc0e287a.mp4?token=idAC0EsNXxK9Ospshr4YWoSgXjgiiSh6s9VUIVpBd0siII8B6qqcGISEPyzPisIyfiJvCf908hTX40iVKSVOeuaHEyk3kYi_gtdh603UPN1NAe938tXkAA61i_5lzXExgmASUx0iztK-NV0fpbXzfPV6iQhQ_wxdQIyR40PVWaJA7SnkREbZ-jWbC82egjEUdYJmPURZWVyIEMk5a1OvHTeJbMUlEHzm5N5VyAqFjCf5WwHUOTn-3JfxoYg6t-N-zawRF1ytbECS-LUf-77rpT8xR_APd6uw_Q9yI8b2rYeZKpt-9q2kX0I5UUju_UyyGsNbKQLJGZNme8dtPXFNI55jf2XIK2NVlfvzdPmGb0VUm8t7qb1EXEnqrb7uaOva07VmqtBnc_MDIKE9aE5KhsbOAf13W9C5jMQKIkxkl4W1F-ELqf1JsYWLPm9t8qNhNerpDdozMIxFXWV1cIUR1SaAsxvwSOwdkdVP45Q2TFTorhqhAY6qwMoIg3UTZ_jQMvH1VoYBFAKMVlwyy71_ETBlMolNr6y_Ac4DbTBdpbh0ElG6RuGb-s_RKuayv3ZnFeelXAJ5cH4C9X3BMtfN_T9Nv8d9jt125YQCjPNY8MRQ_PO-S5ELt_DdpArMbhmcBA1bxs4Atc-tLgQQ1Qbd9DDcNH1ilc8dTxqIGPdwuw4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نظر ترامپ درباره هوش مصنوعی:
از این پس، تمام اسناد ایالات متحده — و به امید خدا اسناد سراسر جهان — تغییر خواهند کرد تا به جای واژه «مصنوعی» (Artificial)، از اصطلاح بسیار دقیق‌ترِ «اَبَر» (Super) استفاده شود.
به عبارت دیگر، به دنیای جدید «اَبَر-هوش» (Superintelligence) یا همان SI خوش آمدید.
باید دید این ایده چه بازخوردی خواهد داشت؛ هرچه باشد، خیلی بهتر به نظر می‌رسد.
@News_Hut</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/news_hut/72062" target="_blank">📅 18:41 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-72061">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6100a5cc1d.mp4?token=buK4nFgt0CR4F7-Ite0h7lkO67BXW_562hS7ygDZpC6dabn1eUeZ_yiiOntoYvTxWGqHQemR94oFNuKoc0P2xcJgVYF8qV8Xdog0ix1bGyvWwqzClp7SV_en3P5-IBWgUO558Zx5L-FC5IdV6C-a4qKiG440HsXmeYuAfs9688X80SqNMHYwlBr119AOebkGnQE6XH72ypVDa-DxOhOASG_lcdmXVRf1G9GPC0oN7EiPiCw5c73EA59RSaXqZxmyzW6JWv8ULc9Bzl6AT2lqGDy6YzQXrQ5CR4q6FlGaK5hNFfZoUdgYrt3bFTPJ5p8kcIpzO7L-x2EQ7o6-Eqr2yA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6100a5cc1d.mp4?token=buK4nFgt0CR4F7-Ite0h7lkO67BXW_562hS7ygDZpC6dabn1eUeZ_yiiOntoYvTxWGqHQemR94oFNuKoc0P2xcJgVYF8qV8Xdog0ix1bGyvWwqzClp7SV_en3P5-IBWgUO558Zx5L-FC5IdV6C-a4qKiG440HsXmeYuAfs9688X80SqNMHYwlBr119AOebkGnQE6XH72ypVDa-DxOhOASG_lcdmXVRf1G9GPC0oN7EiPiCw5c73EA59RSaXqZxmyzW6JWv8ULc9Bzl6AT2lqGDy6YzQXrQ5CR4q6FlGaK5hNFfZoUdgYrt3bFTPJ5p8kcIpzO7L-x2EQ7o6-Eqr2yA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ نام «هوش مصنوعی» (AI) را به «اَبَر‌هوش» (SI) تغییر می‌دهد.
او می‌گوید استفاده از واژه «مصنوعی» باعث می‌شود که هوش، «ساختگی» به نظر برسد.
@News_Hut</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/news_hut/72061" target="_blank">📅 18:39 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-72060">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/156037c15c.mp4?token=nRlGeZR3HzYukf_1sEwJTPgiZ_Cml7_VvMVQ_iOL5CoOV9nhOj6Xj3Er8LR0380s2tFNtmU0TK890Yg5YJR2NZ0ZjKdvkHIUYl2RhZShjpbg3WhfyBX2LjGh0ZWSZ8gxkfiSrGGPvWKJKg5YVpwFmakPLX8qGft3LLPQFDNZBVFHfzq-Zc6YjnNT3VRN8yS5Q39NHPPnWPEdD2VKMQUN9Xzm6_bqfLYmTwXu_HS34KHBCu96oPKDT3eVBlhPOE0y_fsSq9lRc3YDcSeq-BbV3U_XTWL1C24_X99xyp-Z8S0XxRJvMlWQR6tVvylItE0TkscMFg-UImtLXjJpiVn_6Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/156037c15c.mp4?token=nRlGeZR3HzYukf_1sEwJTPgiZ_Cml7_VvMVQ_iOL5CoOV9nhOj6Xj3Er8LR0380s2tFNtmU0TK890Yg5YJR2NZ0ZjKdvkHIUYl2RhZShjpbg3WhfyBX2LjGh0ZWSZ8gxkfiSrGGPvWKJKg5YVpwFmakPLX8qGft3LLPQFDNZBVFHfzq-Zc6YjnNT3VRN8yS5Q39NHPPnWPEdD2VKMQUN9Xzm6_bqfLYmTwXu_HS34KHBCu96oPKDT3eVBlhPOE0y_fsSq9lRc3YDcSeq-BbV3U_XTWL1C24_X99xyp-Z8S0XxRJvMlWQR6tVvylItE0TkscMFg-UImtLXjJpiVn_6Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پرزیدنت ترامپ درباره ایران:
نیروی دریایی ایالات متحده اخیراً بیش از یک میلیارد بشکه نفت را از تنگه هرمز اسکورت و عبور داده است و حجم نفت در حال عبور، بیش از هر زمان دیگری از آغاز جنگ است.
ما هر روز و هر شب، به ترتیب ۲۲، ۲۵، ۳۰، ۳۲ و ۳۷ کشتی را [از این مسیر] عبور می‌دهیم.
@News_Hut</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/news_hut/72060" target="_blank">📅 18:28 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-72059">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2433cb0d35.mp4?token=PqITahrehV9-_2nvNx8QDq_EEFemNzhsUQSrapQkMbbp6Ox0CDOgw_hg9nYXTRB8_QIiPfqlRkji3R_vRvCVmdVmj6SAXtsuwTnL0J8Ea91o2uEGFoaYXjml13mCWzoLIBfKScXz9fp6anRWCDEMQGPUEXC7B0ixYGUozJ3Dypux67khEobCGrhYsqCFz0Sra3_ar36FLE8fvmq-jv18JrFaO1DmCjzBs1ZF4LCqoVQpBxkzDNi0FAIwDC8mP2BqTlA1OO_gizs-Jd-buIeikjb3gEn39Zy9QcLs7xvYlteHz_rdIFopTvL79O479nBbRFg1xwErDcwimjhvnPlshg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2433cb0d35.mp4?token=PqITahrehV9-_2nvNx8QDq_EEFemNzhsUQSrapQkMbbp6Ox0CDOgw_hg9nYXTRB8_QIiPfqlRkji3R_vRvCVmdVmj6SAXtsuwTnL0J8Ea91o2uEGFoaYXjml13mCWzoLIBfKScXz9fp6anRWCDEMQGPUEXC7B0ixYGUozJ3Dypux67khEobCGrhYsqCFz0Sra3_ar36FLE8fvmq-jv18JrFaO1DmCjzBs1ZF4LCqoVQpBxkzDNi0FAIwDC8mP2BqTlA1OO_gizs-Jd-buIeikjb3gEn39Zy9QcLs7xvYlteHz_rdIFopTvL79O479nBbRFg1xwErDcwimjhvnPlshg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره ایران:
ایالات متحده و ایران قطعاً این کار را به سرانجام خواهند رساند. ما به هر طریقی که شده، این کار را انجام خواهیم داد. این کار انجام خواهد شد.
این کار به‌سرعت انجام خواهد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/news_hut/72059" target="_blank">📅 18:25 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-72058">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2e9a7cd318.mp4?token=vQHSjVf-T1h51eBoDJr5H7BL9BKhzMkWCiDIULTBRRVKSVHATA5uOr25_I56NTk5sG2p2ONX-U5GxCABuVD9J3HUzKMBg-mjI-dBxeVAyE_fVa5N5RjTYije7hWS5jPIAh4C6l1fODkxic7RtbrdYYWHInUlMn_a3EtGZmVPd1v9xNbBDmtLmNoqzJ2JJAulTx2QE_tuQovR8BM40tdmMm1z_0r5Xej63DochXC8H13cDN2PCHzljZfTtsCY1rx5IdO5Lud0iS6wAKS_dNU4xuJ7Dr5usTXh-P6yNJuGHDrUD3wsTvKChbKB2dswPR1Rb-jbLSWNOBBMIg5NE7zJGyJ6ScgUunh4vsgMl9rtGudTNAljWvTAPoT4SStlonanbkX_lB7BWt2lmmmCKhTSVX4N03oLBm-LgM88V-BE2XOIBjTZ_FGuzSNxLpNM6Op9-B2LUoVJ2ZUO_UcUyLpBgtE0_k03PZ6sWn2QiltpdoMc3l_C_FzAZwZqmt3v-ihxtXzWROJ3wJFShcaH__Hhzkkh_exBHw17JyVYA6n9k9OKLuQ3dLNCySJMaK48uJa5wYOXVpJLevJ-TS31IIsVkXmktA0MuFNOmJXIOfQcpGlwhYwUgOW0rA31Bp0p1KPXT_VpQ_L65OV7p4z9fXatmg0IORXHRhnyvv3RoL58TeE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2e9a7cd318.mp4?token=vQHSjVf-T1h51eBoDJr5H7BL9BKhzMkWCiDIULTBRRVKSVHATA5uOr25_I56NTk5sG2p2ONX-U5GxCABuVD9J3HUzKMBg-mjI-dBxeVAyE_fVa5N5RjTYije7hWS5jPIAh4C6l1fODkxic7RtbrdYYWHInUlMn_a3EtGZmVPd1v9xNbBDmtLmNoqzJ2JJAulTx2QE_tuQovR8BM40tdmMm1z_0r5Xej63DochXC8H13cDN2PCHzljZfTtsCY1rx5IdO5Lud0iS6wAKS_dNU4xuJ7Dr5usTXh-P6yNJuGHDrUD3wsTvKChbKB2dswPR1Rb-jbLSWNOBBMIg5NE7zJGyJ6ScgUunh4vsgMl9rtGudTNAljWvTAPoT4SStlonanbkX_lB7BWt2lmmmCKhTSVX4N03oLBm-LgM88V-BE2XOIBjTZ_FGuzSNxLpNM6Op9-B2LUoVJ2ZUO_UcUyLpBgtE0_k03PZ6sWn2QiltpdoMc3l_C_FzAZwZqmt3v-ihxtXzWROJ3wJFShcaH__Hhzkkh_exBHw17JyVYA6n9k9OKLuQ3dLNCySJMaK48uJa5wYOXVpJLevJ-TS31IIsVkXmktA0MuFNOmJXIOfQcpGlwhYwUgOW0rA31Bp0p1KPXT_VpQ_L65OV7p4z9fXatmg0IORXHRhnyvv3RoL58TeE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره ایران:
من از همه کشورها خواستم تا در اعمال
انزوای کامل اقتصادی ایران با ما همراه شوند؛ تا زمانی که آن‌ها حملات خود به کشتی‌های تجاری را متوقف کنند، از جاه‌طلبی‌های هسته‌ای خود دست بردارند و به حمایت از تروریسم پایان دهند.
این رژیم تروریستی نه به این دلیل که قدرتمند و با اعتمادبه‌نفس است، بلکه به این خاطر که ضعیف و درمانده است، چنین رفتار نامناسبی دارد.
@News_Hut</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/news_hut/72058" target="_blank">📅 18:23 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-72057">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/415b898f05.mp4?token=M75Zs_UqdzMMl4MWjzeF4hJlvS_GaYToBaT2ciDOAM3VUzxAFIhhyMGCTDlFVCQJ-R-hC3D7dIwkr4mx1DQwYDHO7FQQG8PwKHy6nEvFUUTlDs8onGcjm9MfJox-dYcKJO8KSOlXqFImV_FOEvrPvPityWeYwIjJo72rpTNsYizL04ZBUEd5qit7IrH7Dh_yok-jHIcuHfqqpWFmxYwZ77eE4gXevQy_RDqyNwwysm6Sl_XxeMlkEaz2wErLWdSmmvjzU1KrQiw30ixkx_m7sR_3RT8YOXv2EqF397qwKmL5b46DMftxA7sdqxrgMHNYSlxOYgPKT4yCkZ6s0-p_h1vMVyDw2QYsD4NxK6kW9bXrawfZ8pwHW07RIKLGLlUGZeiW_zv5VuodDbc6DC9lVaOUO2bFM9EKIHOujQ201pCopEx-1VTCXzSam7TzxU_sWGNNwgRiE7QitROjyBonLKc3jwsqt3BEG0YnICl93rnJFqrio6YWdSGx0Zvif3gAl67HWk_dr28h0ETVF5vT8D1YQiUIwRaOsYUZgLLME4uk_bjhRrOpJdMC0BBmg5uNcu3skJu362JodRVLjJq5EZ3IFGxFE-ZWUsIHUNp9XVoiTmV6jpTIC_1T2ibL656E8AyfvKDitEMjhdM3ouKbxdfxWB5D3QoXSRndFb0CrU8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/415b898f05.mp4?token=M75Zs_UqdzMMl4MWjzeF4hJlvS_GaYToBaT2ciDOAM3VUzxAFIhhyMGCTDlFVCQJ-R-hC3D7dIwkr4mx1DQwYDHO7FQQG8PwKHy6nEvFUUTlDs8onGcjm9MfJox-dYcKJO8KSOlXqFImV_FOEvrPvPityWeYwIjJo72rpTNsYizL04ZBUEd5qit7IrH7Dh_yok-jHIcuHfqqpWFmxYwZ77eE4gXevQy_RDqyNwwysm6Sl_XxeMlkEaz2wErLWdSmmvjzU1KrQiw30ixkx_m7sR_3RT8YOXv2EqF397qwKmL5b46DMftxA7sdqxrgMHNYSlxOYgPKT4yCkZ6s0-p_h1vMVyDw2QYsD4NxK6kW9bXrawfZ8pwHW07RIKLGLlUGZeiW_zv5VuodDbc6DC9lVaOUO2bFM9EKIHOujQ201pCopEx-1VTCXzSam7TzxU_sWGNNwgRiE7QitROjyBonLKc3jwsqt3BEG0YnICl93rnJFqrio6YWdSGx0Zvif3gAl67HWk_dr28h0ETVF5vT8D1YQiUIwRaOsYUZgLLME4uk_bjhRrOpJdMC0BBmg5uNcu3skJu362JodRVLjJq5EZ3IFGxFE-ZWUsIHUNp9XVoiTmV6jpTIC_1T2ibL656E8AyfvKDitEMjhdM3ouKbxdfxWB5D3QoXSRndFb0CrU8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره ایران:
بزدلان و خائنان بسیار دوست دارند بگویند که ذخایر مهمات ایالات متحده رو به اتمام است، اما این حرف صحت ندارد.
ما بیش از هر مقداری که حتی تصور استفاده از آن را داشته باشیم، مهمات در اختیار داریم و با سرعتی بی‌سابقه مشغول تولید آن‌ها هستیم. ما با سرعتی بیش از هر زمان دیگری در حال افزایش ذخایر خود هستیم؛ آن هم با تجهیزاتی که در بالاترین سطح کیفی قرار دارند.
علاوه بر این، در آینده‌ای بسیار نزدیک، کارخانه‌های عظیم تولید مهمات افتتاح خواهند شد. هم‌اکنون ۱۸ کارخانه از این دست توسط برترین شرکت‌های دفاعی جهان در حال ساخت هستند.
@News_Hut</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/news_hut/72057" target="_blank">📅 18:22 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-72056">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6cae4c2a3d.mp4?token=nKIKdk5c9eXgrL1gQeMSC1xHDxv4OiPjXnb5kqWl9IeBxpmf895DBdqqFgi5Bz8mLKIv3DNLmJ2yy611qk5fD-qIgi5UdwJJaXcjhAH5AgNP5HyWdao4352av8DtE_5JnSB-GVYOPRTWdJ2eH84CNC0MKF9OS6OrzqCtjI6U_QhSPVcMUbbfkZZdGonVgNmQt0N8-bBjBeWbQ4K1kuYyz_fAKGGGwcEExcbcQlUP_rb6T3VljL6HV7Y8j1DUKpIDgE7iUuDMgMvstkwbVITVE6HNkQwI1Uba2ww5AzB4jNLJmmAb7pwNrsZOwiOLFW4TlaQZ3dOWCyQNiNsqcG6dig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6cae4c2a3d.mp4?token=nKIKdk5c9eXgrL1gQeMSC1xHDxv4OiPjXnb5kqWl9IeBxpmf895DBdqqFgi5Bz8mLKIv3DNLmJ2yy611qk5fD-qIgi5UdwJJaXcjhAH5AgNP5HyWdao4352av8DtE_5JnSB-GVYOPRTWdJ2eH84CNC0MKF9OS6OrzqCtjI6U_QhSPVcMUbbfkZZdGonVgNmQt0N8-bBjBeWbQ4K1kuYyz_fAKGGGwcEExcbcQlUP_rb6T3VljL6HV7Y8j1DUKpIDgE7iUuDMgMvstkwbVITVE6HNkQwI1Uba2ww5AzB4jNLJmmAb7pwNrsZOwiOLFW4TlaQZ3dOWCyQNiNsqcG6dig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره ایران:
من برای انتخابات در مورد ایران مطلقاً هیچ اعتباری قائل نبوده‌ام و نخواهم بود؛ این موضوع حتی به ذهنم هم خطور نمی‌کند.
تنها چیزی که اهمیت دارد این است که ایران هرگز به سلاح هسته‌ای دست نخواهد یافت.
@News_Hut</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/news_hut/72056" target="_blank">📅 18:21 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-72055">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">#فوری
؛پرزیدنت ترامپ درباره ایران:باید تصمیم بزرگی بگیرم.
آیا توافقی با ایران صورت خواهد گرفت که به آن‌ها اجازه دهد کشورشان را بازسازی کنند و کشوری بسیار بزرگ‌تر از آنچه پیش‌تر بود بسازند؛ شاید حتی یکی از بزرگ‌ترین کشورهای خاورمیانه یا حتی جهان؟
یا اینکه جمهوری اسلامی را نابود کنم—آن هم به سرعت—و هرگز به آن‌ها فرصتی ندهم که دوباره دست به کشتار و ویرانی مردم و کشورها بزنند؟
آیا آن‌ها را به جهنم بفرستم، بدون هیچ شانس بقا و بدون هیچ امیدی به عظمت در نسل‌های آینده؟
اما معتقدم که بلافاصله پس از انتخابات به توافق خواهیم رسید، چرا که تن ندادن به آن برایشان منطقی نیست.
آن‌ها منتظرند ببینند عملکرد من در انتخابات میان‌دوره‌ای چگونه خواهد بود. چیزی که متوجه نیستند این است که من اصلاً نامزد آن انتخابات نیستم. من آن کار را قبلاً انجام داده و با اکثریتی قاطع پیروز شده‌ام.
@News_Hut</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/news_hut/72055" target="_blank">📅 18:20 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-72054">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b5ddeee9dd.mp4?token=Tca5GfszDG2fXGgLJ9jeR1WE88Wz6CC8cBEkk6wo_6ni-8TEBKz8uihI80_e2OHIasLFJHMNbHu4LaZYLm5s5QA7tbyTHM-_qvDbR8gVzElr4LJY-hMHYJs81iCF4rhRhjCbgNLuoaGUQSftz3vhwpl3VWv_YHS96syxBs2PS40dorTSUDBH51ZwXgz7Z2_1nHhY4-COjQ-Mbpur4HRCSx1-1uVTeboOoGeVeZFVRhXAHgpW6SR8CZhDKRPDjflBf1YO_ndoUJm4XuROGZD5G5MolP_-NuR9O890nzwO9U33DcWA14gSZjmo-8Lm3vPtyMG_Ff4PY90C_vUFrqdNXT5wvMujMMVnxsPgVsEKnCSidbwp8T1QSTsXaq5kNe7MiD0IYVJMme7OOgIj5bSY9_ii4BT7ZYFqVARF52dnLYWBwOZf3PA2cfnPWu4Maw4Vd0WcUP4GtpoXTT0vAMUANIFSmWQxELB-jSO6HK6tVX0r5jp8Td6zq1hLrrdSoJCjVsKcFYMzGUE1OBTcCTzrzju4r2zRQEjE7PO23qJ39OiNc3FBKagYaarAHEcVDjQDzwgbmG0jL_tDJwuB8dzJQLPK4tEO70TJ345XL02YeMthLDMVHCmmsLAjuggH1i0-EUSJV863E5LIDi4Nanjlq3UejPyGAanu14XS12HA7q0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b5ddeee9dd.mp4?token=Tca5GfszDG2fXGgLJ9jeR1WE88Wz6CC8cBEkk6wo_6ni-8TEBKz8uihI80_e2OHIasLFJHMNbHu4LaZYLm5s5QA7tbyTHM-_qvDbR8gVzElr4LJY-hMHYJs81iCF4rhRhjCbgNLuoaGUQSftz3vhwpl3VWv_YHS96syxBs2PS40dorTSUDBH51ZwXgz7Z2_1nHhY4-COjQ-Mbpur4HRCSx1-1uVTeboOoGeVeZFVRhXAHgpW6SR8CZhDKRPDjflBf1YO_ndoUJm4XuROGZD5G5MolP_-NuR9O890nzwO9U33DcWA14gSZjmo-8Lm3vPtyMG_Ff4PY90C_vUFrqdNXT5wvMujMMVnxsPgVsEKnCSidbwp8T1QSTsXaq5kNe7MiD0IYVJMme7OOgIj5bSY9_ii4BT7ZYFqVARF52dnLYWBwOZf3PA2cfnPWu4Maw4Vd0WcUP4GtpoXTT0vAMUANIFSmWQxELB-jSO6HK6tVX0r5jp8Td6zq1hLrrdSoJCjVsKcFYMzGUE1OBTcCTzrzju4r2zRQEjE7PO23qJ39OiNc3FBKagYaarAHEcVDjQDzwgbmG0jL_tDJwuB8dzJQLPK4tEO70TJ345XL02YeMthLDMVHCmmsLAjuggH1i0-EUSJV863E5LIDi4Nanjlq3UejPyGAanu14XS12HA7q0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پرزیدنت ترامپ:
ما در آمریکا به‌تازگی بیست‌ و پنجمین سالگرد بدترین حمله تروریستی تاریخ، یعنی ۱۱ سپتامبر را پشت سر گذاشتیم؛ حمله‌ای که جان سه هزار نفر را گرفت. درست در همین نزدیکی‌ها.
دو هفته دیگر، سومین سالگرد حمله ۷ اکتبر در اسرائیل را گرامی خواهیم داشت؛ حمله‌ای که در آن تروریست‌های تحت حمایت مالی ایران، ۱۲۰۰ غیرنظامی کاملاً بی‌گناه — از جمله ده‌ها آمریکایی و بسیاری از نوزادان؛ نوزادانی کوچک، ظریف و زیبا — را شکنجه کردند، مثله کردند و به قتل رساندند.
رهبر عالی ایران آن کشتار را جشن گرفت و آن را «خدمتی به بشریت» خواند.
@News_Hut</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/news_hut/72054" target="_blank">📅 18:16 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-72053">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/22f9289304.mp4?token=AniJgYRMa59Spa1Sd1xvqqVesL20KNPE6ANpC6i0hvJGg91teXhpXRtiEObG1DTTmaNoUplYMnLCVE_CZzjxQiXDZJDEmAdDzn00FYCdLrF2QbLKigkvrOuJBRluQouZn5wQGWPBS6OjQ-BqHLqpT2vhYeXEGCqYaaosntB-36o33o_ZFQXb2IopsF7zA8pIdHusa6aX9OCx5iNbGu9TN-Oz_zkUbPO1JT5LRLkNYz_NWkFZNwmzBGgnmjFuaFuLAG-0kuhEm37LuNw8671N-En6LtbOefQvY5y_bv5M6H4WJ-_yQrrXb5f79CZeWj8ncCB4_tXx-dB6oTVuTWibCA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/22f9289304.mp4?token=AniJgYRMa59Spa1Sd1xvqqVesL20KNPE6ANpC6i0hvJGg91teXhpXRtiEObG1DTTmaNoUplYMnLCVE_CZzjxQiXDZJDEmAdDzn00FYCdLrF2QbLKigkvrOuJBRluQouZn5wQGWPBS6OjQ-BqHLqpT2vhYeXEGCqYaaosntB-36o33o_ZFQXb2IopsF7zA8pIdHusa6aX9OCx5iNbGu9TN-Oz_zkUbPO1JT5LRLkNYz_NWkFZNwmzBGgnmjFuaFuLAG-0kuhEm37LuNw8671N-En6LtbOefQvY5y_bv5M6H4WJ-_yQrrXb5f79CZeWj8ncCB4_tXx-dB6oTVuTWibCA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره ایران:
این رژیم امسال بیش از ۷۲ هزار تن از شهروندان خود را به خاک و خون کشید.
تصور کنید چنین رژیم پلیدی قدرت آن را داشته باشد که از پشتِ سپرِ هسته‌ای، دست به حملات تروریستی گسترده بزند.
این واقعیتی بود که باید با آن روبرو می‌شدیم؛ واقعیتی که بسیاری ترجیح دادند آن را نادیده بگیرند. همه آن‌ها آن را نادیده گرفتند.
@News_Hut</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/news_hut/72053" target="_blank">📅 18:13 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-72052">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e271237b80.mp4?token=kjLfm8tma4NcygwmWtKSXz6bbBo4nwq2ITymubytDAXCfJabnmmxRqr7Usfm81DOPq0zn09lhnSoif_ppgMBuK2qNzbc5vIkzdOfXWvramtNDfssdadswl5yhvbk3u1v-G2W0ojopIydkO8PAN9HqcFxm38CYMLxM4RvTl7pYZmiN-S7xbi_jAhsrR7eqt6E9u1su6cJ7D_e7EJ5800W_mVXRZick9_p6DaJ4ShFETW7yiZdJQrT5y2mu6bC8j__nmkT7DOG9UFuG09tzBuc6iKiYy8e2aa419_kUSmRtoYwN6K-dlTmd_OU2caYjksvQFr4JvqcXhKZPQtf_b-5vQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e271237b80.mp4?token=kjLfm8tma4NcygwmWtKSXz6bbBo4nwq2ITymubytDAXCfJabnmmxRqr7Usfm81DOPq0zn09lhnSoif_ppgMBuK2qNzbc5vIkzdOfXWvramtNDfssdadswl5yhvbk3u1v-G2W0ojopIydkO8PAN9HqcFxm38CYMLxM4RvTl7pYZmiN-S7xbi_jAhsrR7eqt6E9u1su6cJ7D_e7EJ5800W_mVXRZick9_p6DaJ4ShFETW7yiZdJQrT5y2mu6bC8j__nmkT7DOG9UFuG09tzBuc6iKiYy8e2aa419_kUSmRtoYwN6K-dlTmd_OU2caYjksvQFr4JvqcXhKZPQtf_b-5vQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره ایران:
آن‌ها موشکی ساختند که قادر به هدف قرار دادن اروپا بود و به آن بسیار افتخار می‌کردند. امیدوارم اروپایی‌ها متوجه این موضوع باشند.
هدف ایران این بود که در پناهِ سپرِ موشک‌های بالستیک متعارف، ساخت بمب هسته‌ای خود را تکمیل کند.
اگر آن‌ها موفق می‌شدند، آن رژیم شرور آزاد بود که تا ابد به گسترش وحشت و مرگ بپردازد.
@News_Hut</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/news_hut/72052" target="_blank">📅 18:11 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-72051">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/380ee199f8.mp4?token=hNQgOlB78SBC1YrICyd53S0TpZ82A5VhEGY3akK8ccIufl0QsfGpyP_lDeuiKqbmdRMOMyEk9rU0PNHTRhg6jX5UfGb_enuGOTyOptqxFBWku8M52rBKCcomH2M_eHHmwWLlTccgFW5vxWjDtGSvjTXyWaunMtICWzQ3F0dDbURcqu4-Y4-FpRcQ7h1VSoI7MIrm-7Cu-nAVwwpREKK6Xm7Tbxp3iYGZH3e57a2oVrGnzWZq22IABlMZVBXz7BVR_4Y_FR_55Tbxaqro11U-SgoG3QDIzBlknu_G2Sm8izYPtPfZzh4r6c7iqc2efJr2qQc-qj0EuRydQcm7749WFQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/380ee199f8.mp4?token=hNQgOlB78SBC1YrICyd53S0TpZ82A5VhEGY3akK8ccIufl0QsfGpyP_lDeuiKqbmdRMOMyEk9rU0PNHTRhg6jX5UfGb_enuGOTyOptqxFBWku8M52rBKCcomH2M_eHHmwWLlTccgFW5vxWjDtGSvjTXyWaunMtICWzQ3F0dDbURcqu4-Y4-FpRcQ7h1VSoI7MIrm-7Cu-nAVwwpREKK6Xm7Tbxp3iYGZH3e57a2oVrGnzWZq22IABlMZVBXz7BVR_4Y_FR_55Tbxaqro11U-SgoG3QDIzBlknu_G2Sm8izYPtPfZzh4r6c7iqc2efJr2qQc-qj0EuRydQcm7749WFQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره ایران:
سال گذشته، پس از آغاز به کار، مذاکراتی را با ایران آغاز کردم و به آن‌ها پیشنهاد دادم که در ازای پایان دادن به برنامه هسته‌ای و حمایتشان از تروریسم، از همکاری کامل اقتصادی برخوردار شوند.
اما آن‌ها نپذیرفتند. این اشتباه بزرگی بود.
@News_Hut</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/news_hut/72051" target="_blank">📅 18:10 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-72050">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/29ba0a501a.mp4?token=hq_6DM5huaahsIgFgrB6sewKDIBwCxirr6H296k2Jj-X3Xc_fXKwr6wZcCGdAVWzSwxbKaPqVFZt60Cp1qAwk9EhATBChsiCRiNoKv4d2qUfebKCZ1pd2bN3S3hN2czfHpLIldQ7S00yER4GGoZpdifnRmP2AHTNPvSJeVsREOiaRmQi_L_uKsYz9IiYGKKywQbvjlmAqh-HLUSvbcfrfIuEwBT7v6sBKyq3Zwn-n87-zhHbqZ6SlF4y3XYYCreQwljUwJ2kyEe1posDGgGtzhnp-8STADGcp50Bctjk2gXM9fKDP2tC8gXMNhfhbHV6LR9-0nq9F2CQ1IfWM5V4Hg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/29ba0a501a.mp4?token=hq_6DM5huaahsIgFgrB6sewKDIBwCxirr6H296k2Jj-X3Xc_fXKwr6wZcCGdAVWzSwxbKaPqVFZt60Cp1qAwk9EhATBChsiCRiNoKv4d2qUfebKCZ1pd2bN3S3hN2czfHpLIldQ7S00yER4GGoZpdifnRmP2AHTNPvSJeVsREOiaRmQi_L_uKsYz9IiYGKKywQbvjlmAqh-HLUSvbcfrfIuEwBT7v6sBKyq3Zwn-n87-zhHbqZ6SlF4y3XYYCreQwljUwJ2kyEe1posDGgGtzhnp-8STADGcp50Bctjk2gXM9fKDP2tC8gXMNhfhbHV6LR9-0nq9F2CQ1IfWM5V4Hg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره ایران:
آن‌ها قلدرِ خاورمیانه بودند، اما دیگر قلدر نیستند.
از همان روز نخستِ ورودم به عرصه سیاست، موضعی تزلزل‌ناپذیر داشته‌ام:
هرگز اجازه نخواهم داد  ایران به سلاح هسته‌ای دست یابد.
@News_Hut</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/news_hut/72050" target="_blank">📅 18:09 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-72049">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/72a4eccca8.mp4?token=P_Or_lM8Dr5SzPnA0abj8FqCMTucRvPNdb86SmeEVtNKmJV7Ns9QJEQy8_V12SrrUmP1MqR6bQoa6HqXQ6QXRiDgurz7YID22-8v5t9DUa5VvgMgVAZk1eextlQyxbHpKIEeZ_Zn93nJUj_3hJ_U3GhPp_U3FdyuGh4ORSOxBD8H4cpQfrE4i_T0YVFcEVrMjU-gZ2n5Is_-dguciaV7x15Wk17Kpu8ckhjcTUTSoyal9zkuSgLLhhFHjs5xdW1PmYsPrXqbmvNhrt1QZNHXtIL4izuSXUgFxlFDv7NfrEouX1qaSLlQj7D0iGchuKyDjAHABkkzLhz-MbCOQBhVcg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/72a4eccca8.mp4?token=P_Or_lM8Dr5SzPnA0abj8FqCMTucRvPNdb86SmeEVtNKmJV7Ns9QJEQy8_V12SrrUmP1MqR6bQoa6HqXQ6QXRiDgurz7YID22-8v5t9DUa5VvgMgVAZk1eextlQyxbHpKIEeZ_Zn93nJUj_3hJ_U3GhPp_U3FdyuGh4ORSOxBD8H4cpQfrE4i_T0YVFcEVrMjU-gZ2n5Is_-dguciaV7x15Wk17Kpu8ckhjcTUTSoyal9zkuSgLLhhFHjs5xdW1PmYsPrXqbmvNhrt1QZNHXtIL4izuSXUgFxlFDv7NfrEouX1qaSLlQj7D0iGchuKyDjAHABkkzLhz-MbCOQBhVcg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پرزیدنت ترامپ:
من هیچ تمایلی ندارم که اجازه دهم خطرات، حتی یک روز دیگر هم رشد کنند. من به اینکه بگذاریم مشکلات وخیم‌تر شوند، اعتقادی ندارم؛ چرا که حل آن‌ها دشوارتر می‌شود.
بنابراین، در حالی که دیگران حرف می‌زدند، من عمل کردم.
در حالی که دیگران از صلح سخن می‌گفتند، من صلح را محقق ساختم.
در حالی که دیگران تهدیدها را نادیده می‌گرفتند، من با آن‌ها مقابله کردم.
@News_Hut</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/news_hut/72049" target="_blank">📅 18:07 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-72048">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fd7fee3bd0.mp4?token=ZtLJQuwQOtG7x9tyQ-4YkqJGxEqdBt9GsdI02aTgdyBqV-YNi_k1NlbEBhSU_KJ5k8z42-9__J8ZLFKDrZzzy68stGL0Gkmra1CBIJtJ50HLlvmZ9foGQHP74ZNFNK2pdtFzYfg7MlNAhCJe5mVFQV6TkznFWdmw1b0NssbGxeEJ_nGDkrB2hkEXUDQ3DT61chYZKI4JhAPu-ImsP0mquq-4Fy4Qu0RbN9wmRdPeTmwk5_Gwz5xALTBPT7v7XyIRguROuryKb-7CyjQz8l0RSU4rEqGqkkPn8DA8VKNYGWSmvf9kqWsv4Vsok9p9tlfU4eSg0GWr39GeHouCh44Zkw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fd7fee3bd0.mp4?token=ZtLJQuwQOtG7x9tyQ-4YkqJGxEqdBt9GsdI02aTgdyBqV-YNi_k1NlbEBhSU_KJ5k8z42-9__J8ZLFKDrZzzy68stGL0Gkmra1CBIJtJ50HLlvmZ9foGQHP74ZNFNK2pdtFzYfg7MlNAhCJe5mVFQV6TkznFWdmw1b0NssbGxeEJ_nGDkrB2hkEXUDQ3DT61chYZKI4JhAPu-ImsP0mquq-4Fy4Qu0RbN9wmRdPeTmwk5_Gwz5xALTBPT7v7XyIRguROuryKb-7CyjQz8l0RSU4rEqGqkkPn8DA8VKNYGWSmvf9kqWsv4Vsok9p9tlfU4eSg0GWr39GeHouCh44Zkw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رئیس‌جمهور ترامپ:
با افتخار به شما اعلام می‌کنم که آمریکا بازگشته است و کشور ما امروز قوی‌تر از هر زمان دیگری است.
اقتصاد ما مایه غبطه جهانیان است. ارتش ما قدرتمندترین ارتش روی زمین است.
فناوری ما بی‌همتاست و ما تقریباً در همه زمینه‌ها پیشتاز هستیم.
@News_Hut</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/news_hut/72048" target="_blank">📅 18:03 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-72047">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">سخنرانی دونالد ترامپ درمجمع عمومی سازمان ملل متحد در نیویورک آغاز شد.
@News_Hut</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/news_hut/72047" target="_blank">📅 18:02 · 31 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
