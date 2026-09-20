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
<img src="https://cdn4.telesco.pe/file/q9EIGojXLT9w_yuw8Z0tEd2Be5zZ-5HPVIRK3qw0QwN5E-3Gc2k_9SjktQQQa1ZaJGoHe5iHzMeyMuv_f9IcNCLdwaiRTH-7Mnk5gpQXIjsDvw9965zEqlv_VRKUyhp_YBwP-FfeFOi6xSo-TSMSl7W0vCpFPPGHHTq4A38jwL7q7w0zEGuNvKm9uN-jlbiK3dUtYhi-u9MN82zNJZ5T3xIYp6N-goh8Rd9YgCysC8z4PkpmfCF9rnmUUP9mEx1H1JKYdmoc7ySIUKhn9Z4rG1sgPSnDXN2yNytohB7jFFNivM0NGgZIKJhhEjh58T30pT3N6UWLTSkSOxk1q0rnKg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 475K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@adspersianaکانال دوم رسانه مردمی پرشیانا:@Persiana_Plussپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-29 21:02:41</div>
<hr>

<div class="tg-post" id="msg-30146">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CgVSI9iV2ehoyJYrni7PTDjICY4Ghc7Rp0tElBhavYvGsO1sYXRBs1uMg0Ozs-IfCpK02T-l34oVe90twkDal8OGnpVr1gd9i2xZzJcFcwXacp2qR3Pagb2BvM_jWvq7jlUqjUVE1GIV3R5N2nO-4USMq9AJ2LI-xdiJBtxqbefvigPPCafZOyTjIdoWL-YANWUBUy0TytxenfxIpVTdOcezfaxO8cnJokez2P_DGWLh5Qlc3AL4E0_gTEZCNg7FUMj7htNeY0V5ItOELlWMaNUNK5E3hvVSkeN1zlfc5J7u2HPfNk2Rb8rYFiA5o3HgLG1xULtOKVDSG82iYqJn0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🤩
آندریاس کریستنسن مدافع‌میانی‌بارسا به دلیل مصدومیت دربازی‌شب‌گذشته مقابل سویا، شش هفته دور از میادین‌خواهدبود و به احتمال فردا دیدار سوم آبان مقابل رئال مادرید رو از دست میده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 2.12K · <a href="https://t.me/persiana_Soccer/30146" target="_blank">📅 21:01 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30145">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/584eeae99a.mp4?token=aaAn6iO77BmfaVKChCQW8anXQ7zSeeyeBBei995o4NqiDsf_LYIJ2rBGebefiVG0iSuTBxr1loZAoSGXmiewufFU0j0OPvI4yUUuR-sOlM3nVWEYTzdzUxqYgp_IA_sU_3sa9nxRwG3yDc8oBhZGzWBsMT2DSdMZ3dhXs0gvJBurNC4UpYfYDSXf_BSY-MAYXwr-nbB82sF9VEfWdiDbMYx1MwAFjEo41cJ3SGhFdPppoJK33l53pXkfE5nZxA8Ovlg2lhyYimBE0XVXxRk4F_n4nzHJquOdNcdbr-05xVTgbITRzECcSdrmITsxg0QPsIfSQoB24bJczHtb8vWnfHe2PZY7nj4cMsmhTSD7Gmcpq88Prf9MUGUC2aX_PvMLdxEVJG08EXcOeReWMYqAy6PCuBn4vXy3Vww6VqRy5SAGeho8VdG8meNbVsuENL5wfV9zQIxiGknKN5_4eAPGXrD9EdwQsPQ1aOC5C8P47SrO0szvl7Fh0_DkdSAtFoLisSeG6SIDJSyH2HnRvQobp8zIffyYvVSz8JPVlzC4GJ5vfOV2i-oUQ-pYEyhWvbWhXB3Jbos81zQ_9sxF3rDNYFPMkCLUFiyJtB4i6kivneP7XwPH0eBKoSI364rDZRI1cRGtHtoRY939bMvZAsVFZmNeYh9Yy8_8BOVrQN7nJAU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/584eeae99a.mp4?token=aaAn6iO77BmfaVKChCQW8anXQ7zSeeyeBBei995o4NqiDsf_LYIJ2rBGebefiVG0iSuTBxr1loZAoSGXmiewufFU0j0OPvI4yUUuR-sOlM3nVWEYTzdzUxqYgp_IA_sU_3sa9nxRwG3yDc8oBhZGzWBsMT2DSdMZ3dhXs0gvJBurNC4UpYfYDSXf_BSY-MAYXwr-nbB82sF9VEfWdiDbMYx1MwAFjEo41cJ3SGhFdPppoJK33l53pXkfE5nZxA8Ovlg2lhyYimBE0XVXxRk4F_n4nzHJquOdNcdbr-05xVTgbITRzECcSdrmITsxg0QPsIfSQoB24bJczHtb8vWnfHe2PZY7nj4cMsmhTSD7Gmcpq88Prf9MUGUC2aX_PvMLdxEVJG08EXcOeReWMYqAy6PCuBn4vXy3Vww6VqRy5SAGeho8VdG8meNbVsuENL5wfV9zQIxiGknKN5_4eAPGXrD9EdwQsPQ1aOC5C8P47SrO0szvl7Fh0_DkdSAtFoLisSeG6SIDJSyH2HnRvQobp8zIffyYvVSz8JPVlzC4GJ5vfOV2i-oUQ-pYEyhWvbWhXB3Jbos81zQ_9sxF3rDNYFPMkCLUFiyJtB4i6kivneP7XwPH0eBKoSI364rDZRI1cRGtHtoRY939bMvZAsVFZmNeYh9Yy8_8BOVrQN7nJAU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
نامزدجایزه‌پوشکاش سال؛ ضربه قیچی برگردان فوق‌‌العاده و تماشایی‌از میگل بورخا، مهاجم تیم کلاب آمریکا مقابل تیم گوادالاخارا؛ چی زد!!!! حتما ببینید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 4.85K · <a href="https://t.me/persiana_Soccer/30145" target="_blank">📅 20:55 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30144">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b82b6c09bf.mp4?token=n5-dbit72MmO1skr41V33iIXJIxzPapCEZ_FECQryy-KL-EOKeNRjkorlvaouP3v-1G-orOWws4CqATLU46SNN259Z4-T8yq9YC9zHpMaEzaYEq8WX5qGj8_9-kcJj6ATn-vIgmfzLUechnjTElKRFmjKH6tExl3dj2PkYq5IhrfXxOD4_E9DCO_DJD1zq8SlfGZ7UGJrKgI3KAldh1LzeogQxv7PrxcawFGfzqK7fFyn7yWLMdjSl1IWYJhLYIXfhKWgoKv-RuUOaWnBkBdAcqdnWDKlZE481KBo4G11e5e4m0V7qnRAmUW9xTGvQtzNCbokr_HuyFem1n6MrkA_w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b82b6c09bf.mp4?token=n5-dbit72MmO1skr41V33iIXJIxzPapCEZ_FECQryy-KL-EOKeNRjkorlvaouP3v-1G-orOWws4CqATLU46SNN259Z4-T8yq9YC9zHpMaEzaYEq8WX5qGj8_9-kcJj6ATn-vIgmfzLUechnjTElKRFmjKH6tExl3dj2PkYq5IhrfXxOD4_E9DCO_DJD1zq8SlfGZ7UGJrKgI3KAldh1LzeogQxv7PrxcawFGfzqK7fFyn7yWLMdjSl1IWYJhLYIXfhKWgoKv-RuUOaWnBkBdAcqdnWDKlZE481KBo4G11e5e4m0V7qnRAmUW9xTGvQtzNCbokr_HuyFem1n6MrkA_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
نامزدجایزه‌پوشکاش سال؛
ضربه قیچی برگردان فوق‌‌العاده و تماشایی‌از میگل بورخا، مهاجم تیم کلاب آمریکا مقابل تیم گوادالاخارا؛ چی زد!!!! حتما ببینید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/persiana_Soccer/30144" target="_blank">📅 20:13 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30143">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e2be5ebfb1.mp4?token=dgREOh5aCVjdPbfsWkuL8Ag-0f1K401KVU7cD6gjZhjasBIxvzm_c9WFO_Y8enc36-v2w9DNdoIQLQQVK8DGKUfbpowjeGPFC1WRU7d-mQXkYQFpWqK75hABreyx_ZobJI6UgrwiK5V36KjAKhjlrzJ6MdVxJL6Mhb8vYLGPfSwKVVI9KTEu03IYeYkLEs8EogIE6JLf7cqdFBhiTpvLooCbjDZEz_maSvd8YKlkvPRt4vtpEmy-5A31uf7EnvKbWI3eZ9i-F-CLkgvNeJhEJ63zZJUvtqMpM-ccpcm4PbzrANXlpd31d2SZBwPD8iETpxwQA6MS8c6TOdL7v9WIpw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e2be5ebfb1.mp4?token=dgREOh5aCVjdPbfsWkuL8Ag-0f1K401KVU7cD6gjZhjasBIxvzm_c9WFO_Y8enc36-v2w9DNdoIQLQQVK8DGKUfbpowjeGPFC1WRU7d-mQXkYQFpWqK75hABreyx_ZobJI6UgrwiK5V36KjAKhjlrzJ6MdVxJL6Mhb8vYLGPfSwKVVI9KTEu03IYeYkLEs8EogIE6JLf7cqdFBhiTpvLooCbjDZEz_maSvd8YKlkvPRt4vtpEmy-5A31uf7EnvKbWI3eZ9i-F-CLkgvNeJhEJ63zZJUvtqMpM-ccpcm4PbzrANXlpd31d2SZBwPD8iETpxwQA6MS8c6TOdL7v9WIpw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
هفته هفتم لالیگا|دومین شکست فصل شاگردان آقای خاص این‌بارمقابل اتلتیکو مادرید؛ اختلاف رئال مادرید باصدرجدول به شش‌امتیاز رسید. بارسا مدل هانسی فلیک قهرمان زود هنگام این فصل؟!
🔴
اتلتیکو مادرید
2️⃣
-
1️⃣
رئال مادرید
⚪️
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/persiana_Soccer/30143" target="_blank">📅 20:08 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30142">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l-S_H5Fv1CvXDfgfIk8neEVyx0XFq0JAcLYjU_eURVko4uxpi3ISxddS9fQ2RNpe3ZEcJm4hQm76PeOlGNf7YxEH5iyac1tcW6-w-1kw8RAD_kynJemqjIlgKIOh7acgr3eXM20pww5MU5u6r3O9K8_94B4_P0x9JxSzwm7NqPaUDGJrRutyqpHgIGJhKZCIMyWxnlLdxzX7Ra6RvdOQrX94_LT1p6HmQKn8VC7Vgqtdk_NbJrlhBNx5BgAAXjUgRCz3ea-rTG5f_TrXxQOYa6UHp8tSQnbU47nl4t9oly4aiS2m5MfIIriAbExgan7zLMDGMlCkqPOm1g4Vleiq1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته هفتم لالیگا|دومین شکست فصل شاگردان آقای خاص این‌بارمقابل اتلتیکو مادرید؛ اختلاف رئال مادرید باصدرجدول به شش‌امتیاز رسید. بارسا مدل هانسی فلیک قهرمان زود هنگام این فصل؟!
🔴
اتلتیکو مادرید
2️⃣
-
1️⃣
رئال مادرید
⚪️
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/persiana_Soccer/30142" target="_blank">📅 19:55 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30141">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zra0COy4NtdjDjemUCRDPOE-ppKOTYz3Wq7IpIWXubzasN-ZgET7AwGBeaJxTijDZTqGtT2L2LxpGeYqUE8pPePDMlPbxgSF3gaM4wRNS0kGuEy-NiuNx6dTscKj3akcKXalWgW4VPXco9fKkGCS8jcN21NSPrKm1VEIrWMyKnPOeOR_ZXwx_EGDn7fGimwbOahG1tRz7XrP_Wjr7NO2pF9uwuTrYOvxgj9G6TJrkFKxsOkz4gnBaBXN97Qec9N95MjpqPMnDvnM5TQi7Npit_ekc67dCiMb1nmF0kriewbrEmrZFhQa3nwE37-pN-X2CvhYdQC7Gi9VnBtPy0Y98g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌هفتم‌لالیگا|شماتیک ترکیب دوتیم رئال مادرید
🆚
اتلتیکو؛ ساعت 17:45 از پرشیانا
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/persiana_Soccer/30141" target="_blank">📅 19:48 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30140">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iNy3v7K1ulfSnn6HguAylNX7AAg-Q_x8xr7ge0bWWI_t0VIab1OHmcCY29VNvSgSMqERi9spv4EaoSq8mtcOZzXmMSKrDZ3v_USBLpUk3VMykjhhxGleMzn0Ruiz2_qDwLsAFOldqeh2ArfvsJzQyrgHoBq_HfqWuclAz1JnnsLcMRVvO8kJD8fWhUtBL4-EN6a2mjfeAvKJk7i8NuErRZDoi0NcG_XKuWNOO9B92_Hluoe6w59NB40UKrJNAVLCx1_9A4MMk9tdjp9DHQTylB1jwrGLCyHZqZLyC5wMz9L_sYV4jLovga9tqe-gfuOE1vjdNLVW3tJVNbF8-jK6bw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ باشگاه کاشیوا ریسول درروزهای اخیر پیشنهادی دو ساله به ارزش 4.5 میلیون دلار به یاسر آسانی ستاره‌آلبانیایی‌استقلال داده بود که این بازیکن بعد از مشورت با مدیر برنامه‌ های خود این آفر رو رد کرده و آمادگی کامل خود را برای تمدید قراردادش با باشگاه استقلال…</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/persiana_Soccer/30140" target="_blank">📅 19:45 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30139">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/43f4a8d8c8.mp4?token=FdIBpmKpy349MaHsrinWv-xnWJ7su5ZKfhgT-oFHe9t0ZRDSoXvJvuiWqYLkRuk5eGur6Ge1yyV3wNyWFSM3opw625O0xtB3keK2jNfXm7kp1uyJCiPgZ_Bm-714acKUuza2VTxKVh0iU9G5Tf69b5F1exqsWXPfF2I8l4P6qRFpE0TCybilryqMx86ywszzQykvNstBtFoz1zWFnwJOMjkWmy-Qyv7J0RSgdqcMkwkFIGjJcnQYQzxpfpFkRlMlI420f5Xdj-RsN9XxV11i6dq0LromYzvap4yF_Boyv-qOfDuYArARDpQgwbdyIr57uf7hczqvP3r43eqjJfUd2g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/43f4a8d8c8.mp4?token=FdIBpmKpy349MaHsrinWv-xnWJ7su5ZKfhgT-oFHe9t0ZRDSoXvJvuiWqYLkRuk5eGur6Ge1yyV3wNyWFSM3opw625O0xtB3keK2jNfXm7kp1uyJCiPgZ_Bm-714acKUuza2VTxKVh0iU9G5Tf69b5F1exqsWXPfF2I8l4P6qRFpE0TCybilryqMx86ywszzQykvNstBtFoz1zWFnwJOMjkWmy-Qyv7J0RSgdqcMkwkFIGjJcnQYQzxpfpFkRlMlI420f5Xdj-RsN9XxV11i6dq0LromYzvap4yF_Boyv-qOfDuYArARDpQgwbdyIr57uf7hczqvP3r43eqjJfUd2g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
خاطرات سمی امیرحسین قیاسی از مصاحبه با علیرضابیرانوند و جواد خیابانی؛ بدترین مصاحبه کل عمرم رو با علیرضا بیرانوند گلر تیم ملی داشتم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/persiana_Soccer/30139" target="_blank">📅 19:45 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30138">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g0ooSGJjLS3-T4OS58ugk92q6YxTo55YBVNb8vXy8PAsLREg5AYx57hhjHYzg1ZkPsgPwSN7xlkau1ngCA7EDxZY9tWI_XEnti4-QHQGOHxJ9z_-HaYBiHq91DPdXKJRa5tekVV7qyNfdLw7Q1JFtDJM66l78ETc59CpKdkWuuQlSHqU7oALBdgsasdoi5lRZT50s8QF4DcgHMOzew0V9UM2yFDlaNEr81gqs3vEzIlH9pSSz9pEZIbP26_SWMv0Bb_9gJvX8iU6p1o9ZkZRNun2YW6mPB-l7cByRr8dDCm4x2rVH77mkXCFqSffXoSMtWvKOugkQO6z1WNdmC7cPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💎
سایت پیشبینی Yekbet
💎
🅰️
🅰️
🅰️
🅰️
🅰️
🅰️
🔔
فرصت ویژه اولین واریز دلاری در یک بت
⭐️
یک واریز
🤩
دو جایزه
🎁
⚠️
یک انتخاب هوشمند، دو هدیه ویژه
تجربه متفاوت با اولین شارژ دلار
ی
🤩
🤩
🤩
فری‌بت ورزشی +
🤩
🤩
فری‌اسپین کازینو
👀
با اولین شارژ حساب از طریق ارز دیجیتال، یوتوپیا ووچر یا پرمیوم ووچر، هر دو جایزه رو دریافت کن
🗓
شرایط استفاده
🤩
⭐️
فری‌بت:شرط میکس حداقل ۲ مسابقه با ضریب حداقل ۱.۸۰ برای هر انتخاب
⭐️
فری‌اسپین:قابل استفاده در بازی Yummy از POPOK
﻿
🌐
لینک بدون فیلتر
🌐
ورودبه سایت بافیلترشکن
------------------------------------------------------
📱
کانال اخباروهدایا
🌟
g29
🔗
https://t.me/+ioIBrQfqMLtmMmEy</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/persiana_Soccer/30138" target="_blank">📅 19:45 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30137">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qZC4PPQ0295O54dfLKXe8QUya00uPgJRw3K69lXiw9Ohh6r5-29_EgLK2W2rLR7AFofj-RCgNk5qyzQg4_abZbYCrRFXXokZngyCWejKbuVHdcr3lploqDTWHbgEljnsSReIFYD4lPj0F2-qXnew9Q6XSAlVnyAvm6Ya4fIHCrYhiD-d4QXqtij9CrEEUg7k9jn0P2341hrWiXaoSsXAOEhkb6_3RWHTkdZ3dJPkksDp_3VRrOy3ifvN4NAiLfFbA_Yph_TeW5fIOiewELHSo1cHyk-FRey9DR19cxWh5GiqJNben-W5-FrD8DnvBfvnHacFJMioU_O61KMQD1dwag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌هفتم‌لالیگا|پیروزی شیرین شاگردان هانسی فلیک درشب درخشش خیره‌کننده غایب بزرگ لیست توپ طلا؛ رافینیا دیاز یه تنه با هتریک‌اش سه امتیاز مهم بازی رو برای آبی اناری‌ها به ارمغان آورد؛ هفت مسابقه، 21 امتیاز، 31 گل زده در لالیگا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/persiana_Soccer/30137" target="_blank">📅 19:30 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30136">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Dpz0r5bcsyom9ZOMGCs3BSxIG1AmXmiA6SY5NhAXVDvxiyiKN6pBg-ZLR-9KR4-i8SnAZslxdGkmUHRHZ2lvVbucPZuMqbqhoXjcKNALX9jWqI-39aTg3BKJOMX0W0_lDQjKiCfqQpQyhWrz8z_Y-OSy1x0LGCCKr1_4ZUgDwfgg7YtA22--n5MIQ1xWz30NkFQDf-A1iPwmbHjhXj9BZCtDEigaSJkqggc-HuVQFBr-vPaw9gPxpf0ctGnul8q5chvfRscUqLMKm80VPdXvhuszB-n0i4V8GjHWVcOIMpZyPZzV7eNsHwAWJlcQwK1VhOO2wDZ4DJeKcKoC5JDvCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
طبق پیگیری‌ های رسانه پرشیانا از نزدیکان اوستون اورونوف؛ برخلاف ادعای رسانه‌ های ازبکی باشگاه تراکتور تبریز هیچ گونه مذاکره‌ای با اوستون اورونوف ستاره‌ازبکستانی‌سرخپوشان نداشته است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/persiana_Soccer/30136" target="_blank">📅 19:21 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30134">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6eb0177e91.mp4?token=KMr99YRnzIQNK3SEJufzPrO1g0doniPd-Az12xQjqa-f8ghDSAysqHq3l1jLnB_xNLmrbzOpdSIniEu-fnkQjctu-dBwYCjz2I8QI-wGdn4cwdZb9nKJX3J43hIyu0sePiRsAAUT6gL2Rjb9Q7G-wH6UUZkaNWl9q4HiD31FP6oQNfSvWbFeRHcC0Pb56CwSlGhvadD_OEiEMcOzuuy8P7xUNut1SZe6Ehvre6N1w0ePkhCzLKthvIf6pVe53387gO80Jko6AOkZ3Y17lB8RMcICf34hlehTMGam39K8QZw8wtei2c2ePtw-prpjlGDc-pn76uQ87NXlUQ3JR7krNg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6eb0177e91.mp4?token=KMr99YRnzIQNK3SEJufzPrO1g0doniPd-Az12xQjqa-f8ghDSAysqHq3l1jLnB_xNLmrbzOpdSIniEu-fnkQjctu-dBwYCjz2I8QI-wGdn4cwdZb9nKJX3J43hIyu0sePiRsAAUT6gL2Rjb9Q7G-wH6UUZkaNWl9q4HiD31FP6oQNfSvWbFeRHcC0Pb56CwSlGhvadD_OEiEMcOzuuy8P7xUNut1SZe6Ehvre6N1w0ePkhCzLKthvIf6pVe53387gO80Jko6AOkZ3Y17lB8RMcICf34hlehTMGam39K8QZw8wtei2c2ePtw-prpjlGDc-pn76uQ87NXlUQ3JR7krNg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
هفته‌پنجم‌لیگ‌جزیره؛
پیروزی خفیف لک لک‌ ها در دیداری خارج از خانه و آتش بازی تماشایی سیتیزن ها در اتحاد با درخشش انزو فرناندز. گل‌های این دو مسابقه رو حتما ببینید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/persiana_Soccer/30134" target="_blank">📅 18:42 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30133">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PrzQfaRsTwnuhdBQdjRL1ERDb3CpznYv7OYg4fg1zGoVcg8Ba3xalqak81uXBJ-yIxGsMLVIOWGOjqm24T-TKfNpiEp3kT-b0c3UXLgDqQuXoGkvZwa2_RCQ_iDno72bIRMWSX1Ot9QEd96whnga5-20N3QSCZbzSIl-IekASS5bLJgjuQWTC4HF-cc5qjlZrb5z7alDWMNUrf5KdT9jHaYEA-37E9ayAHyCifPEfDBURy6PYntwFoBTB7wXCKxU3Xp4lNr-L-svFUl8nVZd-5j_rBfN1bvEWSL5tJGV-7ABk60-dpjK7MaH5IhPjoLWuv5tIDdy9X8Iub2LCKUwPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
رفتاریکه‌مایکل‌اولیسه بااونیکی خبرنگاره داشت این بنده خدا هم ترسید اولیسه اومد تو میسکدزون ازش پرسید گفت اجازه میدی که بغلت کنم؟!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/persiana_Soccer/30133" target="_blank">📅 18:10 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30132">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NYVjqW_y987KNRNe8QEweUXta6vM_Qr3svpAs4rs4HQrVGXcJ8UUEpjO31qYE7qn8_SSa7bI5m5up-eUxQBmCcpYCxbhihXnL7_1QSd72Labp0Jtfxj4L1SVxNDBtY1ZoQPc9mL9ybKD72mVoAkoZH-PLsNlyRpYBRnXwGg9vECR2I0JkchB9hA9HCz8U58lwWM-TX2o9VDmhAcCspCJmWmtAswGMXmqx0Zv6jDlegjLA6DVnpkJ8ElJuUq4y7PHxO3FYMbmv8tqlm9JETNp88oStXFosZ6j3Pzs3sqKNorcQZwmga4UspKWZplEVL-PKgxRky7egxRTba527w21jg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇪🇸
پارتنر لامین‌یامال:همه‌شواهدنشان میدهد که یامال شایسته‌ترین‌بازیکن‌برای گرفتن توپ طلا 2026 هست. اگه عدالت برقرار باشد یامال برنده توپ طلا خواهد شد او اسپانیا رو قهرمان جام جهانی کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/persiana_Soccer/30132" target="_blank">📅 17:50 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30130">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9d3be7a360.mp4?token=sqVyndeAzHHrMV9woT2k4ixA_5jkOx-N0_VmBA2q-bQssqWPhdTMpEH0qCSEMfqHgzGelgRZFoGNdZMH7jMccTL7cfeh7hTogIpe33T-sjYYStIc-nC4iq_jCxkq_jJ8hWgo3N-6jh7ym61q7qyTxHG3Hgio0Yh0F_WCEFgxIy26NMbtvVnN3lPnIwd0O8pjuE7_L291o2N9F8BVXnkz1SSzfJfbYX_taaIMVYBnqJj3fW9ta7P4UijCjZQYw0OjYqDl_7U-lSsfbmiS55SoXRsH39ULPlxJzdl8P1_dRIfOyHS8IbNSn-9eb_v3j4-IWQo5fbx2FiVyVK7FRcvvrQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9d3be7a360.mp4?token=sqVyndeAzHHrMV9woT2k4ixA_5jkOx-N0_VmBA2q-bQssqWPhdTMpEH0qCSEMfqHgzGelgRZFoGNdZMH7jMccTL7cfeh7hTogIpe33T-sjYYStIc-nC4iq_jCxkq_jJ8hWgo3N-6jh7ym61q7qyTxHG3Hgio0Yh0F_WCEFgxIy26NMbtvVnN3lPnIwd0O8pjuE7_L291o2N9F8BVXnkz1SSzfJfbYX_taaIMVYBnqJj3fW9ta7P4UijCjZQYw0OjYqDl_7U-lSsfbmiS55SoXRsH39ULPlxJzdl8P1_dRIfOyHS8IbNSn-9eb_v3j4-IWQo5fbx2FiVyVK7FRcvvrQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یادی‌کنیم‌ از مصاحبه‌ تاریخی‌وفوق‌العاده گزارش گر صداوسیما با یه‌کشاورز؛ خیلی خوبه حتما ببینید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/persiana_Soccer/30130" target="_blank">📅 17:11 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30129">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/37c2e1f8d1.mp4?token=YiQd4ABpkhZZpWbGWw3zgGCU5vzARSSI6mJA9IbDp-c2tVJHKyM_li8-qP5h9AMMjdGEqMgqrjBX1NhqvYvm_wlUveCmmKpZgs4O3nHUWb8HiZjqlGdmrz0s9USGrdxhJgEK1sMlpg9GJXNsrRt_qNU9afAfTojZSBORVNN541U7agWOcGujIs__3RFxBpAeL8IxCPec5nHJLVBpYiA9tbj57-ItXEH5YDPAWYsjnF3bL-ZQqhvE549Fd98I3q642T0Y8gNMMkOyOX8EdPXv8AuNQXEnBGtBLG3SiL6VyjCWDYSZ3OPqoWwPlx6bamRBgZFmgSUKnhSSNHzy-3-n_g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/37c2e1f8d1.mp4?token=YiQd4ABpkhZZpWbGWw3zgGCU5vzARSSI6mJA9IbDp-c2tVJHKyM_li8-qP5h9AMMjdGEqMgqrjBX1NhqvYvm_wlUveCmmKpZgs4O3nHUWb8HiZjqlGdmrz0s9USGrdxhJgEK1sMlpg9GJXNsrRt_qNU9afAfTojZSBORVNN541U7agWOcGujIs__3RFxBpAeL8IxCPec5nHJLVBpYiA9tbj57-ItXEH5YDPAWYsjnF3bL-ZQqhvE549Fd98I3q642T0Y8gNMMkOyOX8EdPXv8AuNQXEnBGtBLG3SiL6VyjCWDYSZ3OPqoWwPlx6bamRBgZFmgSUKnhSSNHzy-3-n_g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
توصیه مهم مهدوی‌کیا اسطوره فوتبال ایران به والدین درباره زبان‌انگلیسی؛ حسرتی که مسیم دارد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.3K · <a href="https://t.me/persiana_Soccer/30129" target="_blank">📅 16:53 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30127">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/m8xV_2g2kV19NZOBk3Y9w-qXpajAx4o9W4dW4gb1i7qnb2gxO_KqKzOB4pTdAIvtCIlv6TJFpHGcOWnw714r8dEWU8JeoNqF8xXIPeG-Mp1WcVfKvDLlcXUkn9mA5IfHZq0r9zLBYwW7_2Ef2JSYSE6z1alo4zYGfxIGETMG8bL9ybR2JHNBjYg_whQe2w990gm43OFZdZmh80m7EwqwVpXX3fMcZM5Q2k472xNdw0eEwDlhF4AW51wIQjqAUH0Ops35NUpW6vR8NxxtRZnXZwF_h30jFDJKAQUEWeegSv4BDZTZjI4wrW2glAUS5pLGeo1zBBm_jPRo-RXAQjKRIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NsIBT9s6pfIZE17JGfyKMN8RpI8XkBDYiLT0yGEAZ2FlMnD2DMUslSQOQPfA2knMVw2eKp1dqm9KDaNvrIL3SIOk44NWySiD4GNMsy0xCwoDu2XTQxMdCrDmzSqfUMIBZEhu7ct5fv4p-N0ee9NYpFk8TAa9MBHf9gZQX_H4vW_b2wntcXw2QM2RIt0lOOe-4A5mZUya8ThodStPJe18LKflDcfaKp9lGXR3qt2csA1AD1R_GLxJ-1v2W7-uvh_Ui1BdK-MQXW3sCj7D0oydmpLjTHTlNnKGAAJ9kw_IdCaFUCXNC8c8H7dojdRdQ_hgcGp8R-SneaDFqeBou2srTw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📊
آمار تقابل‌های لالیگایی اتلتیکو
🆚
رئال‌مادرید؛ کریستیانو رونالدو بهترین‌گلزن دربی؛ 22 گل؛ اتلتیکو در 10 دربی‌اخیر خانگی تنها 1 شکست داشته؛ 5 برد و 4 تساوی. مورینیو دربرابراتلتیکو:11 بازی و هشت پیروزی. سیمئونه در برابر رئال: 50 بازی و 14 برد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/persiana_Soccer/30127" target="_blank">📅 16:37 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30126">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j6_FpapALdvVM4ghWOtmwK_gSLqZbnB59WWHcVQXly7Tbp8w9KflokRN29nKRHmNpchLw3-PXrGSiQ6OpExTMP-1GVUUC0IcIcm9QGjchdR5bB4us3zleI4ytoNIXYrrysphyMixpjd2g843g5OTDUsqxiPUlQ66DeKo-eyAFx9pvmHll1VGzgV4vXY4099vTrz_vQ9FOYM43Bp-R1j2tTXqo0nn6djFf7IjRagpHPf9JvYuKoSMnmomYJLy3KIqQgszaZj-oGxDSxsWnfXi6Jt5nh1gfL8J9MSBxy4kQ-U6lU3sBLiezCS8FSRBrF0Fp2mapPUWXEPLAvNfx0Vbkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
آمار تقابل‌های لالیگایی اتلتیکو
🆚
رئال‌مادرید؛ کریستیانو رونالدو بهترین‌گلزن دربی؛ 22 گل؛ اتلتیکو در 10 دربی‌اخیر خانگی تنها 1 شکست داشته؛ 5 برد و 4 تساوی. مورینیو دربرابراتلتیکو:11 بازی و هشت پیروزی. سیمئونه در برابر رئال: 50 بازی و 14 برد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.6K · <a href="https://t.me/persiana_Soccer/30126" target="_blank">📅 16:30 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30125">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BTJ5sBfvalcmj9_safd0IEP8ugMRNhZ-dSYHGncmJPUDzahD58_wjBNkFGa0nZ7Ib4RCHb-iL5-1v-60EOuXLXbP1WoxdLuOvDqPf59BS-JABDooaDc0UhcFD3X702dDjG1cWAY7dfI0U-1ps_dTcbhMzYk22_rkOcRxReYrlIYCDtTwOaXPFPT4FCl-1l20Ziw1RX_f71hrjqqnIIvVumXUVdg523tCIUHOMbkXy_JbLW6jO5k3QRE8xzPuE0GaY6Ki6LF1BtcSN00-TFNqiZW33Fey_-IetFerWRwzdcjcpdy-O--lZTjMtvwCQe5Xl4Q1UQnvPfguA_Oe12LYnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
آمار تقابل‌های لالیگایی اتلتیکو
🆚
رئال‌مادرید؛
کریستیانو رونالدو بهترین‌گلزن دربی؛ 22 گل؛ اتلتیکو در 10 دربی‌اخیر خانگی تنها 1 شکست داشته؛ 5 برد و 4 تساوی. مورینیو دربرابراتلتیکو:11 بازی و هشت پیروزی. سیمئونه در برابر رئال: 50 بازی و 14 برد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/persiana_Soccer/30125" target="_blank">📅 16:06 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30124">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OJhv3DXz2gZlndqaJgHhgUn4q4aSwduyjJeVnSnt0OEdASgzULKSluOatgMhQcTMGG4R9if8OtXnbCtGw5u0Qc-sgWPGAu4n6eZyTng6yuzimQl3kotKmThms1cF7SyYrrIJe7KcgmHDueS_5kUj8MgUzsPe1-InINFnNQ-fRTzLAqfIoLwzGSFDP3VmW9S6AHtwll-fcmfEGgY2XWaQWGT7kQwT2fLQaJ-aylMveRShse9aqNURZ5MDB8BhDnfR37a20-8Cupx8jNI0u44fNvB1Z8dfV_GGOdBvivUxsUqFsJCs42Mxa_rTlsjt9GP6wneSLUtCRXOQ5OaiPI-ZPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#تکمیلی؛ طبق شنیده‌های پرشیانا؛ مدیریت استقلال و شخص‌علی‌تاجرنیا رئیس هیات مدیره آبی ها بعداز انتخاب‌مدیرعامل جدید آبی‌ها با مدیربرنامه‌ های یاسر آسانی برای تمدید قرار داد سه ساله ستاره آبی‌ها جلسه برگزارخواهدکرد. درباره مدیرعاملی هم چه فرشید سمیعی انتخاب…</div>
<div class="tg-footer">👁️ 39.6K · <a href="https://t.me/persiana_Soccer/30124" target="_blank">📅 15:14 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30123">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ujye6Y_nLJ9y2wOAbKEXOnU9Z6410YWVdsC7cEAuVs9Pi5inr8FmkdVv1YFWkdryTPqhxYaHJTie-pvmwT4x2-uejOIwMxLIHr2r_-ayenbpdV9aysqAt0JKs5OzN3BvosB3QrQpoW3bjAO0J8w6XCTye94jfVnvdOmwVPGRWaRS3jfAEIr83XHTr_bEsYqiyytFvWi0rdZlyKA60TNcoFipecUvbuOMWYbqbUp8ZnqVLYzRIkkSRHpOFSkWbEYNbrqPjRpU5aH1aKyEHOwvo8pCJebRy3Y8n3yt5Al-le2m5ogz3o6TmRozuLNy1gn88FUk0GAa58ljKdVlC2SJ-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
مقایسه عملکرد رابرت لواندوفسکی و هری کین در 150 مسابقه اول با پیراهن باشگاه بایرن مونیخ.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.1K · <a href="https://t.me/persiana_Soccer/30123" target="_blank">📅 14:53 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30122">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e09969a195.mp4?token=MluwmVJV3UjINIPVm5EWFBbcLHP1nX-pN4VAgLOf-JupQ9hz-MRNgQIqRKQuSizelLat6wWm_BMZjDG5Hw-6ztKHv2agCg6X2bao_v064xgeS8Ve6odwbGce6_syU3okRRMaI0vatqxbwRIgNxL1kHgOrTMghN7_i4uEYDhUeJvJYQwWIA-PZlrxEqcWrOO96ru8tGy7ph9Ej_gmS0pCGhEkBufXI8EQZqR_UWVqCopLZVi0PL5HJgvtxSeBLxWmR4QsQQZhNF9ysMspL6q-fPKLrRbkePT69eAsEijgUE3qV5Yz_6m4DWa3oEwcOs3d87SKNYONKg_nVBLYZ5S6oA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e09969a195.mp4?token=MluwmVJV3UjINIPVm5EWFBbcLHP1nX-pN4VAgLOf-JupQ9hz-MRNgQIqRKQuSizelLat6wWm_BMZjDG5Hw-6ztKHv2agCg6X2bao_v064xgeS8Ve6odwbGce6_syU3okRRMaI0vatqxbwRIgNxL1kHgOrTMghN7_i4uEYDhUeJvJYQwWIA-PZlrxEqcWrOO96ru8tGy7ph9Ej_gmS0pCGhEkBufXI8EQZqR_UWVqCopLZVi0PL5HJgvtxSeBLxWmR4QsQQZhNF9ysMspL6q-fPKLrRbkePT69eAsEijgUE3qV5Yz_6m4DWa3oEwcOs3d87SKNYONKg_nVBLYZ5S6oA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
صحبت‌های‌جالب‌ و شنیدنی این نابغه هفت ساله اهل شهر تبریز: در آینده میخوام پروفسور بشوم‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.4K · <a href="https://t.me/persiana_Soccer/30122" target="_blank">📅 14:33 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30121">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sJD06fYXFgazvIGMUfZBqXfB_uETzl5biV5nsgHZjgGoQ4imZ90qb6n_Tp7yH3GEgBQ6JDbKhnq0scJcpJ7TBlzAQ_o6DSxiTATXmUn6NZpTcBl7WTTb3SJ4BtxwiyuHgDQ4p-J84JKn1KFkXGSAezOAzbXacKJB5WyLi-XYdWf3CM-pIVTLTIu09lffWDkFQgp13JV_z6QWI5MZr62iB03y-RCxXtPTPzui5jucbmOEmM4mUFADi_qAtaqfXeRc6RQtbV2LYEdwFgvBPrY3fl_3WzQCUUBMfdCd1MOa27lpyxEj_k4RpaPdELsA5JKFbZr_iqhbxUUFUIseRWze4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
طبق اخبار پرشیانا؛ به احتمال زیاد سعید دقیقی سرمربی‌جدید نساجی میشه‌. فرهاد مجیدی که مجوز فعالیتش درلیگ صادرشده دیشب ضمن تشکر از مالک نساجی به آفر این باشگاه پاسخ منفی داده است.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 43.1K · <a href="https://t.me/persiana_Soccer/30121" target="_blank">📅 13:50 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30120">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NXvtCab2ZVyz2hzkkujE7ClS98CTdotEo4kcd-59jH9WRmGIgvJczPpGZltRlnDn5ROiNxZcqYGYqWSYbRLVhoxekTiLwGPIaG1An4S3fAR7k2_Q0_F0Z2pNzmcZMQGZOS5UtV1GofDoJAlFUYIA1CxHhexFP1rDV9hSVOYtlZ9IJ3VEXjyG5ZegCCGezEyrUS-bu3ksFV0GWiu4JL7tQlztxjtcZb6NVMahO5TZEvesr_2IJoP8ncMF-hdZLL8xq9qTFDEs5EeV38OBUd16V9kNRjggLqwT8VV0LkOmRnsu9n_cGef7gKOCyZTU8wICYD4aUbG0CEz1hfNFXPMzeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
فرشیداسماعیلی‌بازیکن‌سابق‌ آبی‌ها:
رفته بودیم اردوی کیش با چندتا ازبچه‌ها عکس گرفتیم بعد از ۳۰ ثانیه همون عکس بین فن پیجا پخش شد. از اینکه به این سرعت عکس پخش شده بود تعجب کرده بودیم. بعداً فهمیدیم که خودِ سید حسین حسینی ادمین فن پیج خودش بوده و اون عکس رو گذاشته بود. تعداد فالور های اون فن پیجش هم خیلی زیاد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.1K · <a href="https://t.me/persiana_Soccer/30120" target="_blank">📅 13:45 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30119">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7061b4b2b5.mp4?token=GccpSAhP0b9KA8YkufcZ0W4RzCpiwGsZCKGb3LhWK_JeJ3odoh8OvzRNjAkTKEwht3pdknzwYGwMstVJJSd8BvdGwSj_vqpJoIl97bcbpnJ-p2vNG8Xt0US6Hrbgs2RJO9IwYOiaXegZoM7BgluH_4-u2VNonoKDu_NFThJOEEwz3WKAUVGBKNEgbwsRS1aJNGEQzk093qQEmNr71j8P09MJtsuU_ZYMcFBEjSJmaT46DfN6AaRbhlgL9aVVNKBqWVDoIODoPNWIXTXA29uS7OOZfsJ_DYg4l452jdlXKrplGcDPjCIM3PTFAOhgrKnN6TozgoENLi_h1hZ_ezsjrA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7061b4b2b5.mp4?token=GccpSAhP0b9KA8YkufcZ0W4RzCpiwGsZCKGb3LhWK_JeJ3odoh8OvzRNjAkTKEwht3pdknzwYGwMstVJJSd8BvdGwSj_vqpJoIl97bcbpnJ-p2vNG8Xt0US6Hrbgs2RJO9IwYOiaXegZoM7BgluH_4-u2VNonoKDu_NFThJOEEwz3WKAUVGBKNEgbwsRS1aJNGEQzk093qQEmNr71j8P09MJtsuU_ZYMcFBEjSJmaT46DfN6AaRbhlgL9aVVNKBqWVDoIODoPNWIXTXA29uS7OOZfsJ_DYg4l452jdlXKrplGcDPjCIM3PTFAOhgrKnN6TozgoENLi_h1hZ_ezsjrA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
👤
#تقویم
؛ 20 سال‌پیش درچنین روزی؛
ژابی آلونسو ستاره اسپانیایی لیورپول این سوپر گل فوق العاده تماشایی رو درلیگ‌برتر انگلیس به ثمر رساند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.8K · <a href="https://t.me/persiana_Soccer/30119" target="_blank">📅 13:37 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30118">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lv4Pn1JBP_DtFOzkYICBj4miL8mLszgj0l7ZhXD_n_dknpES3B_z7PoKdUtVzLCEkvph0iexBIJwekGVMLuCTrO9BMh0CrkehsRspprEZGZlTAPytLEQpxwguVSHZJWGzeKOeiZBISBTVczoQS2epW_G_0auH1ex4dmqyUl41R3yU5E4m5xpQCWqMf0rN1dVVwil97NxMUj5JXRwpYjnElHJ2SkboWs2f-UZZuSDJ6HERsuj6HA4kOsf3fH289ZLRzZerKSbA41rdxqZPmWk-LqVsgk6hDr0i4Zmwj-91ZH9D6rIYxjG09CO_b6fltuHODqEKvhbrr4FJElpOlgzMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌هفتم‌لالیگا|پیروزی شیرین شاگردان هانسی فلیک درشب درخشش خیره‌کننده غایب بزرگ لیست توپ طلا؛ رافینیا دیاز یه تنه با هتریک‌اش سه امتیاز مهم بازی رو برای آبی اناری‌ها به ارمغان آورد؛ هفت مسابقه، 21 امتیاز، 31 گل زده در لالیگا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/persiana_Soccer/30118" target="_blank">📅 13:16 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30117">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fVU6ElnhcHCwOogQWFCa-xMwUgVDmtqDoUr6_NcFDW30AJ6ToxE2C3P96vOC6kF1-KpcBqGn37b59Q_wWNZeYT9LMvu5psiZNqHBCUFFr9lJY-kTzZmpQeJ32cmm2AcbZA0lgaV7wsvmdcC1QxlJ8oFTpwoN6CF86sLX4oJkn7cSoS871dGrmhovycMr_TUyoFFfR206K2fHqmEyu0OI7oBbLYxmy689QDXvIBV7BXzWy4JXDjQ8IpTd4_KEitfNmxjfyENLRdOsEn-J5TSDnYm1qHqpOAKPGCkG3OTqqD9i6CQDvaTLfiM8GEG0FRk0LAGw7Xjgnsz_86PKacq9Dg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
تاریخچه تقابل‌های دو تیم رئال مادرید و اتلتیکو در تمام رقابت‌ها به مناسبت بازی حساس امشب.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.2K · <a href="https://t.me/persiana_Soccer/30117" target="_blank">📅 12:48 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30116">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VePK8Bwk6nci8rGCuAVW8xLemTqr_Q3mg0xtM_56lm5McLV6wniBX_dy1EuJUuppfeKMqZ1-qXR2wPNY3VedOTD-T4UJKxkF5tnHFJ2rjq6uE9vgxlYegBo-Goy1d1DXnnhsNjXlEoPlhVTDN6hawCfbcT7XoXfOoqi4uag1rDLenhdex-JuCUjtfxFAlOU8zaXMcO-6kMTmuSHsgI3ufEd71hJCTT0KVew86DEtxvWRA_Z3UXDYt_yZbAdvKc2eBGEHQw0tn0W17OZMmsG4_lLNwFSnI5SIhz5-PxLYQb6WVFSTPDOatomuNGoK6Kb_2zbgCdMKjnszdFrtHLBBBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ عباس کهریزی وینگر20ساله آلومینیوم یکی دیگر از ستاره‌های‌جوان لیگ برتره که مدیربرنامه هاش درتلاش که در نیم فصل او رو به یکی از دو تیم استقلال یا پرسپولیس ببره. شانس سرخ‌ها برای‌جذب این‌ستاره 20 ساله کرمانشاهی در حال حاضر بیشتره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.2K · <a href="https://t.me/persiana_Soccer/30116" target="_blank">📅 12:27 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30115">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eWwZCh-ORmAflKjgt8Swt_P0Np_NYYa2WP_Wm4rPA91fDMWn4UcUehJHcSpXHlNfF2NhhNqApEAcOvHIFpova9wf4rv413RQ2WA9N7Z4qVif5009rAtaTs6T_SM6RZVenwz4vr_QnUTOCgRW37fskMwjwodhjJ4rhjwEcdOLhaXCJIIb9ev1h0BpLWcKYMc3h50eCYpp969t34tM6kencDDKQ-zqQ3utctNg_HObaFLSixKWjXu0yVrgnMrmhtGUR6LDC0xeIEP876AvkWJAhpSYG1kdCdvqYB_MYOPnFtRtuMqhCEXRPdEx9-IYPjAVZi6eqBIb4xT4XGtOQ4Ew6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇺🇿
لیست‌تیم‌ملی‌ازبکستان برای بازی دوستانه با ایران بدون حضور ستارگان استقلال و پرسپولیس! این‌مسابقه‌دوستانه روز دوم مهر ماه برگزار میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.2K · <a href="https://t.me/persiana_Soccer/30115" target="_blank">📅 12:22 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30114">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">✅
برنامه‌‌‌‌‌‌‌دیدارها‌ی‌‌‌‌‌‌‌امروز؛ از تقابل مارسی و PSG در لیگ فرانسه تا دوئل حساس مورینیو
🆚
سیمئونه پس از 12 سال؛ اختلاف با صدر زیاد میشود؟!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/persiana_Soccer/30114" target="_blank">📅 12:10 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30113">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZCVsVrcjTpZIEgIV7Dw4SbeyeXIgynf8UFyWvcOyyD8groxXqgIpXPdwpY91Tk2LNjfhekFekbzFEeeJaO9NA4dVyK3Wh91yK1NOtsTJPQmbkj_mB3WmKbZAXu3rtgy8iM26oD3sY4VADjED2-LLTC_Ov7erbsInjcfkoRtGGNnG8tzvGZI6lPR7Z2zno-_85ctLBh9kPhX6sQjTUPmTZobIJgTyJsUGp1h7Jjfq_bn8gpgDaecEnUDx0Lumyvv9tq_DF8Zc3N-3LitatizeiHAR4Noj7SLgSpwgBQyXIwvHakXsGD8LETBMfwxPirChre_Utw8MDikdAVXih88MLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
🔵
#اختصاصی‌پرشیانا #فوری؛باشگاه استقلال اواسط هفته آینده بامدیریت‌تیم فجرسپاسی جلسه‌ای مهم برگزار خواهدکرد و با پرداخت 50 میلیارد تومان رضایت‌نامه یادگار رستمی وینگر 22 ساله این تیم رو خواهد گرفت و رستمی آذر به جمع آبی ها میپیونده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/persiana_Soccer/30113" target="_blank">📅 11:53 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30112">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QmWHL6oJH7poRkYgW6SS68JCy42ru2qzJVkwkhHPJMBS4LoclSKP5LNkmZdYvA7Z9lqbOXN8cp-Tfd1zYh8pKGCAHKoXalFjOVA9P4lIBHvFwez-nYGOaiU5ePVzYlkrlWXayyLxkxGiIknG1bvyUSUBsAHck5cYi_PtM6Fg_ubzwS4OjuOw3ENnqrPq3DJGOZ9HBN2pzUngY6UWpnAfltYY198047k3vO9_S6pYs2xAVbJA_TYzc455VN0Ec7EO_O8Sb-10TCBKJ71bLc28f4ojOjy6uD8KGLKwNzV1ZKkc78oZutQUHZbbhNr9i7-RT6AulGqbtBmqJsABTjQqGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇧🇷
رافینیا دیاز تنها در یکقدمی رسیدن به رکورد رونالدینیو درجمع‌آبی‌اناری‌ها؛ از رونالدینیو تا رافینیا؛ ۲۰ سال بعد یک برزیلی دیگر در بارسلونا می‌درخشد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/persiana_Soccer/30112" target="_blank">📅 11:24 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30111">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KnMbVfUm5IaC_sb5je2UHA8VeYB-1TFVze3l0p8gzIDEs-gxlx9mHIfG0ibC1-wFiMqsIjKu75A2Mf8x85Jq2IKT9WTVkRWseSMp-p6JURc2C_sIxVpzsUkjRrlmWTVcwfT8cZgjpikJXgtT0YRIKcalzrXCnHoawobhzDR0gil41SOpW1srB_vUWwZP96w-s2N9_FJB3gWa_DMLUUNEJ-jXfomeSxEXrO3rJY7WBmRRHe-gV_38scXTRVbNg4WOKIVbqjEqVeJacpJgpdSkPMcRexBpXwDLlFMYWzfQmztrSyLzJY_I7YZKcZIRHMA_EhveAyXE-pdmi_CjitunHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
لیست‌آپدیت‌شده‌سرمربیان‌لیگ؛ مجتبی حسینی اولین سرمربی جداشده درفصل جدید لیگ؛ سرمربی بعدی نساجی‌به‌احتمال‌زیاد سعید دقیقی خواهد بود. فرهاد مجیدی آفر مالک نساجی رو رد کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.2K · <a href="https://t.me/persiana_Soccer/30111" target="_blank">📅 11:19 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30110">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vPgBOpaxFPSDi73cfgR3PiNR962bxugv7aEGToKmJW1LtvBavFSgWGiM3BIynZuf9KcPHamPNLngdGnaq3Uh_k6sawQSzvau1PL3wSH4MiL_vsFhO24zkbC9DrsKWuz7eOpaIyLrtTAdW697UJI0nbzWdMGKpK7c9SPy1FEK-9O5tymiDxmTvNzRMd1XHGKWCnBKgwU2nWEbEQpvpcbOuOG49ITGw_oSvSaTA9mAUR9pT4f5kwIA4oB-nfhK8Q6mKMzrsH3H57iraHz1p0DfnWCZWL6Vqbopyy3kBkPsCY9EOv55LYsftnvedHBvD98EyZxKKrwbxXxdj38olsqkEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
تیم منتخب هفته اول لیگ نخبگان آسیا در غیاب ایرانی‌ها با وجود درخشش ستاره‌های استقلال!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.2K · <a href="https://t.me/persiana_Soccer/30110" target="_blank">📅 11:19 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30109">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pLK5QnupFyZSNVUqLdg9sEwsHHxiS-JwqoRw0DKpV6ib6uxu52s5NwUvELnSt8_cfuvy6TDekU9vKgcavMt5ZfX-jfNdKvxv11burmROUst_4-D2AEUnm8ukaMD_DumBoAowLemDvaHSsrzS22PMZbanum9I9uWwJj_rUVhapLqsEv5AdlT_G9wGUCIzRzAJipTAAe9ickfb1xUMM7-07-QihJRqaLlxumseivKjhy9Y6kWImyHGROxju6iXJ3kh76aXKb60auuHg9itD4VotWFMmljuczE-yjcKY2gAgxNBzluKw0dD-XOiECyBV5fssx9QlOojX1AeqCl7U8Jfew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💎
سایت پیشبینی
YekBet
💎
🅰️
🅰️
🅰️
🅰️
🅰️
🅰️
⚽️
لیگ فرانسه
⏰
شروع بازی ساعت22:15
⚽️
مارسی
⚽️
🆚
🗼
پارسن ژرمن
⚽️
💯
اولین واریز، اولین برد بزرگ
شروعی هیجان‌انگیز با
🤩
🤩
🤩
🤩
هدیه خوش‌ آمدگویی ورزشی تا سقف 250 میلیون ریال
🖥
امکان ویرایش شرط ثبت شده
💥
برداشت سریع با روش های ارزی و دلاری
💵
شرط بندی بدون محدودیت، بردهای نامحدود
🎁
با هر واریزی
🤩
🤩
🤩
هدیه ورزشی شرط‌بندی میکس دریافت کنید
🌐
لینک بدون فیلتر
🌐
ورودبه سایت بافیلترشکن
------------------------------------------------------
📱
کانال اخباروهدایا
🌟
r29
🔗
https://t.me/+ioIBrQfqMLtmMmEy</div>
<div class="tg-footer">👁️ 37.3K · <a href="https://t.me/persiana_Soccer/30109" target="_blank">📅 11:19 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30108">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🇮🇹
در هفته پنجم سری‌آ؛ دیدار تماشایی و مهیج دو تیم آاس رم
🆚
اینترمیلان بانتیجه مساوی 2 بر 2 به پایان رسید. گرگ‌ها در نیمه اول دو هیچ‌ جلو افتادند اما در نیمه دوم افعی‌‌ها به خودشون اومدند و با دبل لائوتارو مارتینز سه امتیاز گاسپرینی رو پر پر کردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.6K · <a href="https://t.me/persiana_Soccer/30108" target="_blank">📅 10:20 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30107">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hBzFmoH6A8m2X0bljK_aK-gXLJq_ZXDydk795eU2fEIAOY6eqoZWjgm4Aruy6AW3MFZgPQ9CKKAIa1iFgwSb7QFkYJTDtQUgR8OFiBdKpC6xUzOBt2Hrfmf7-E3YTZiN09qYN5zQtsS9xAMRqdJdbDDFx6O_R-b1VPWKOm104gy8d8ZH2uy5YF2yYfOh_qi7r7RgnYNPzmrBg7Tp8dsbvY_0SsfKAeXWi8ODN1KftBYtDMg6H3LbWMiCsujrBgGocCkhnlFUiiSrJX5wyCVYgyAJngWXUnd1Vbrk4WPilUFnW61TG7v-oidYlu3tBFmX1NvAeytPwtc_AltTUZPEew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
شرکت EA پیش‌بینی جدید خود را برای جام جهانی منتشر کرده و بر این باوره که اسپانیا جام را به خانه میبرد‌. این شرکتم تاکنون دقت 100% داشته‌. ببینیم کدومشون درست درمیاد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.8K · <a href="https://t.me/persiana_Soccer/30107" target="_blank">📅 10:13 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30106">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zi-nzu3wbW9O5ndF1v7hr-ziYRmcrY1-sqELVXW5q47lo5ZkYNOlLF7tMi7i54z-jawpDIqod3s4Sh1RVvRf-gxpQGGu4YcRPApBEiif_Klw7yw3EZD0CTrrAGW3zj4EawprlYaKV8gVZxjaLuHig9rgkI7lN0smEaDoi3Z2-JqRGA5SUD6jQMXbLG08YAeKrvYMPD3mtew-erkgnLQW-7Lh9O_oImlr7RWDNzC-ridTNMoat96-Ty2u4D78yxr3I0ffv-cQCOZJPQRc16qumfk44Dtd4hAB3ycWmiBIoRgxyr_3yXMx8KMwhyQFMlOt_vUCPUJiY9m8SofJON1e8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
ژاوی اسپارت فولبک‌راست‌بارساکه‌دیروز به لوانته گل زد شروعی خیره کننده در این فصل را ثبت کرده. هزینه صفر و خودکفایی از سوی لاماسیا عاملی‌ست که شرایط اقتصادی بارسا را در سه سال اخیر بهبود داده است.  قرارداد بازیکن تا ۲۰۲۸؛ دستمزد بازیکن، هفتگی ۶ هزار یورو؛…</div>
<div class="tg-footer">👁️ 46.8K · <a href="https://t.me/persiana_Soccer/30106" target="_blank">📅 10:00 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30105">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k9e6-1VPGoGPUe4tH0VheyQ743sleEjqYcAKvOXVlGlO1k747WwlaXta9HzM4KlkrzclD5h7Oez6IyY0Ca9n_kMRflg6UXDwxpMy1J9rAuEgdOQFgXxAzXiJCYWZ1hrVkoCXv2kCFUukYn76NTisuCfswltdTFKqn2nWK69GpEuj-vLdQpNtknbAqkI0USWwIx3EXl9ljBhja2dimf38xL-TxKLntl-w0vk9RW6LgbZUWMTMTmmbOGBRbFe-ei63OpYeclU20Kz5AvldC48m0E7AgzYAZv-dwpjEIGiCGjbVDw2P84y89nEl00kR4DqTMkUnx_lbZoCUpzo5LQipgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛ محمد مهدی زارع مدافع میانی تیم پرسپولیس که‌هشت روزپیش پاش هشت بخیه خورد از اواخرهفته‌آینده به تمرینات سرخپوشان باز خواهد گشت و مشکلی برای همراهی تیم تارتار در بازی روز جمعه 17 مهر ماه با صنعت نفت نخواهد داشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.3K · <a href="https://t.me/persiana_Soccer/30105" target="_blank">📅 09:25 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30104">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eUFTXieoG-yxxXDYRWKQLdfaxROIjhAd1u-tdDiI4O9PcE8b6VRdT-wy9AdKS7GpWZcAssAf0uiMIOU3MfFennpOtkZNfzsbW3td72IsaHpVs0OXh0DG7c7KURDBa7L5IyhnKIhQNpT7q00bppgzBTiJ9P0zIgTJT9Lm3XtXQGGD5rTpsXDVhfAI62pmgH9KHZ0zsKgrRN5tbYE_ZZwhyoDSMkCDPeeE47BgJg2S0JywTeJUyvAtqPlLavlaxwQsrC0I_zw8OshhOVEi-in2ZJEjvKFuRA4KIQwODc5-Kpq-baqoowAXKJHHqtQHICczKbyAF8abkRPQnQOfVKB-cw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#تکمیلی؛ باشگاه‌ماخاچ‌قلعه‌روسیه به ایجنت‌ محمدجواد حسین‌نژاد اعلام کرده که در پنجره نقل و انتقالات ژانویه "نیم فصل" بادریافت یک میلیون دلار رضایت‌نامه حسین‌نژاد روصادر خواهند کرد. سعادتی این موضوع به مدیران استقلال و هلدینگ رسانده. حسین نژاد درپایان فصل…</div>
<div class="tg-footer">👁️ 53.5K · <a href="https://t.me/persiana_Soccer/30104" target="_blank">📅 01:30 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30102">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s3cOl_PxZpvQqewNuue5PEE5E4uASzpR_0h2hWoJzZDlGnjAmijxO72kKmaDWptdLxb2fvwXEYnSpjHe7Ig9SYfksfcsxFcp60B6pzg6ZswmO8b--sRehg5Maae-H_qNy6PI4zkC1wtyUT6I-7l9Z0T6L4T8gZKg0AfQ07cKTQyy9dhIzvR7qML4rEr2iJRRv3fDi4UwDb0qWl29-gb2QGhg8ilxf3_Fj8FJheGsSOHg126epCrtcabK2JJGJOJYxDEi6pBf2PqF4IG4Vp90DiMFlr-835dWl00a8Owp6cXu98xofFHpvphT3TjMNCHu7eywZV29PrZWeI8SnXSBpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌‌‌‌‌دیدارها‌ی‌‌‌‌‌‌‌امروز
؛ از تقابل مارسی و PSG در لیگ فرانسه تا دوئل حساس مورینیو
🆚
سیمئونه پس از 12 سال؛ اختلاف با صدر زیاد میشود؟!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.5K · <a href="https://t.me/persiana_Soccer/30102" target="_blank">📅 01:28 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30101">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kd70nD3ljtVDfIcIv3TQABEf03cgCuADS1uQJU8Rf4NhEUMmM_qov9TLI-kNdT0Xcunm3-lwTf_91DE9zbpxsKfGRQ6LVeaIU9G058bn0g2Y0Y6r-Bde8tzSkC9qlR-ZUXNIWa1LI5sI5Rl2FYMozspaaO2GemvVy8RHGRcAqXpLf_9LR5I-pmYENgLmurl4FqA79dS2_RwtSGcR60LSEjzhsJYNRpTkqb88OGvQsfrUK9CmsBMEmS6nWiBrB6QP7rA8CESek-o-j2j5c0gzH_IzoS2L7JqrZPqMUrM0Av3CWAaS_0blzoOGduS97PhSnus9IFK3rh7uOjmiWZ7Ogw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌‌‌‌‌دیدارهای‌‌‌‌دیروز؛
از برد بارسایی‌ها با هتریک رافینیا تا تساوی در دوئل آماده‌ترین تیم‌های سری‌آ
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.4K · <a href="https://t.me/persiana_Soccer/30101" target="_blank">📅 01:28 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30099">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eXMXjvUtylrdftmTPtYNnvh8zS57MpHe4DQz_lOCsAAZQqKpSKgeIq1ZFocEIs9wSuAaWkYCOmg3n_lImZJDTPx166h_NvEqhxd_cpN9U8y9Xk77IHenc9jARMYyzO6oaEfvyBB5zbhxqlId72puQFrtVhliTSqu3flxP5dC8WmIdP38jFIzEUPZPBjhcZT0gDC6RZh4Uy5J1vcHf4XykieoDoRg6BU45C0L1F9TTy_eoMai02xrZ245dqo7STKNkw0l6Qrmk0X0AtSF4quCsYF04bBBTFIFI8qfhmXrgJTquNIyx4KOy1awiXk_6hAWz3JZO8DWfo9w475mvlTiOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/q-UH_msEs5wRcau_cvTcjNJnIgd0Q2GYCBAEepETWiA3VC5qyeioT7a6TgvaUpGHk9JxTwLiX2OlFlZ_WuCE8mKChApb3BlUFNmgsgsdnohxEcIcH9mE3W6bFInwmFwfGYsBy7i4SCkeOYgA-wH1wV3GiBDGJmk-Xll58n_e_Z7sfnJFaBx3cGhipk8J7TfUCoVw7PjCzrBYYZFtjEot5kPw8xaNcWwvVh8C4kzBXKZ6v1P11dzVrpik5dq8YGDYAE2aZjrcz33PK2Cwg84JeHVIxS21WvuGPNR-OA0MLpja2BlHNXzjyvuqu2oLeBckxUaeIPetDarsQfVMSPQJ8Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇪🇸
عملکرد فوق‌العاده بارسلونا در این فصل در لالیگا و چمپیونزلیگ: 8 مسابقه، 8 پیروزی، 36 گل زده.
🇧🇷
عملکرد رافینیا این فصل درتمام‌مسابقات: 14 گل زده، 3 پاس گل، میانگین نمره 9.5 از فوتموب.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.8K · <a href="https://t.me/persiana_Soccer/30099" target="_blank">📅 01:14 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30098">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cczf3oHGa4ItK6rldVrteKCfx3WjorNl3ZUe2I-zXtNVDMXKlRdv9p8FAfh2nZZtF8i785nM01izez4CetHRWRrPk8_J3GxE3n_Z8vY8t5fRn0wOu6bgaJGaklQJBKdawSChStjE3y-LjUl8z0Jbj6sTG4c_QM8xfIHL_g9KcJBG9g0dAc1cS5A9zZ7kBitIUUtijyjPfdH4KRM1-1RCWdZhdD0iIaYWlsECkGjTHD1FLMssv7kgXNfSbD0tKonkgYB7-IUx8S9Oy9kG7r7BlBr7QYiKppnbWGZKq-yCV1tUu447HK1uv2peyhg6L1wKk81y8ljS7aIEfmn5FFd5UQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
عملکرد فوق‌العاده بارسلونا در این فصل در لالیگا و چمپیونزلیگ: 8 مسابقه، 8 پیروزی، 36 گل زده.
🇧🇷
عملکرد رافینیا این فصل درتمام‌مسابقات: 14 گل زده، 3 پاس گل، میانگین نمره 9.5 از فوتموب.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.8K · <a href="https://t.me/persiana_Soccer/30098" target="_blank">📅 01:14 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30096">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SwnzO1RwVTh_lOfBx3lpFQqzkj6wYr7iyiq0VW3KXPNArzj5QyCvZSEaHAw7CtvoOceS8TAJhR3VlZX6yhjmLM0tBXfQGPcd3eD8ksE4LiUAKR16VZ7t-Mlp9jbtvumgCC4tsSZaj4l6TVemrOozHDOxagcTxJ4n8hm_eruGP5LDhzZI5EVqXHkFoB9sf3abnV7Z2NtKDSxpDUkLNgk-j90hcVUz00xcUTw5rEStva3kWkjABWCAGeSGc-FHFRXXllotMUe8EUeRDvxCSKif3J2ATsmol3vMzh0PZFExma5bGZdVfR46na7tLKC8Wi-0ET3Vdts1To9BIIjRwupgdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌هفتم‌لالیگا|پیروزی شیرین شاگردان هانسی فلیک درشب درخشش خیره‌کننده غایب بزرگ لیست توپ طلا؛ رافینیا دیاز یه تنه با هتریک‌اش سه امتیاز مهم بازی رو برای آبی اناری‌ها به ارمغان آورد؛ هفت مسابقه، 21 امتیاز، 31 گل زده در لالیگا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/persiana_Soccer/30096" target="_blank">📅 00:40 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30095">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hvg2NyRCx4tgJf3fUiHzRhPDUVGCuTGPoh69vs_dl0y300nEjIEJk-SSZPMMAJZ1ym_gCmzZrbA2NgmDDQ06Ytc5eXLo-bX0TSFVzcrpnZkqOn2J3R6GuEfjtP7KpzrQ5unx2U21kl8Ur0LWoK98FdQB-fSe_2G2hkf47G2xog_q2v1tnVTiYaq8geUHpLJvOf14gZ4yj5OHwmTjTyxk2Eq2R_0yW1pS1mKrEMjRohfCusLoyBcdaXfiJ8KjK2TUY_CEhEGhO7b3BdgUPK7SsYp105qrWMy4JB36Qt4G1C6jH5-vNnqagg3ApIioQA-RyIyz9BCkbD8SfcIFyqGwHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
یه‌بنده خدایی تو سایت پلی مارکت ۶۴ هزار دلار بی زبون روی پیروزنشدن بارسلونا مقابل سویا شرط بسته. اگه‌این‌اتفاق بیوفته ۳۰۲ هزار دلار برنده میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.7K · <a href="https://t.me/persiana_Soccer/30095" target="_blank">📅 00:29 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30093">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZqJmLqgCqN1XhPo88bgZHsVCbUItP7mFzpCHzUpdqjAOobEfRqUjDqD-se8w-l8Qo1ITPjbmym2ixg4BdNDU2QI8JqQuRYptBi7uA7pUkC6zeiMVQmrwoYBg_075uTb075NS57xFg4cdq77boQEG_PKT81h56tCA1VEjlbZh9YvJ9sUlr-o_QdgZZV1JgzVoPG6XSuLnHDysNRIvmNsbIZMFPlvqicWw_JOJam8BCYxk9_z668KpezeW2_h7mPFGSoCai5AooVrTdubyz4LL29wcUYOzrzC1BGt6wI4zoM16yUQ-FwcAuOJpF7rww6uMkdnPyAnAsk9rQtMxBuuVKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
گلزنی دنیس درگاهی دربازی‌امشب استاندارد لیژ مقابل  سرکل‌بروخه درسوپرلیگ بلژیک؛ قلعه نویی تو جام جهانی 2026 میخ کوبش کرده بود رو نیمکت!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.2K · <a href="https://t.me/persiana_Soccer/30093" target="_blank">📅 00:15 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30092">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pKkzSFNCuyDs8mjE-W0YWN0f8YrFFtHN23MMoNuMl6vgc3RdLDWtLDQc0-wT_nUsSC_MaKpbf1-Tzf__1ig5A_fsgx6Gj6qn0N2QQXwY5tjY2W7riBehmJi51qH6UrVb3W6MQen4SMtWGFsB-Mq1nRYkmlSGDGmHljYfso5hT8ODgTDSaskk5q7k7nshIkduh42_loaHaLswBialO3T3oIMfm-VPUmbBj0SbgyBQaH8HqaKzT0l9A_PjrrFjTrLX-IIoL6-ZgwoNl8eGIjd0XdFJwcrn8CTsPw5XtTws5k2jB8zxXFgqv7DhcD1cnlJJatjKAV4iBrQoajHBc1epZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
یگانه اکبری و آیتک سلامت دو خرید جدید باشگاه استقلال برای تیم والیبال آبی‌ها هستند.  @Persiana_Pluss</div>
<div class="tg-footer">👁️ 51.8K · <a href="https://t.me/persiana_Soccer/30092" target="_blank">📅 23:39 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30091">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/onylzP1WjChArR373TBFiqEYy6hspV04RiNes6oZ6nxCKn_xP-HSeNoNNcebYO0RfeREfNzh0ua5PyeznfD6IrzvRnHG1hhIgg_mds-20_TutUVPJTAzxj0R-KP5G2ESU1h-26mnAWKhSFQVvRl1pMUIUfckkFhYrkMK27EVzYxI6P_xNo-kpBEKEwQ2tcLV6F4Vcr0en6efNuDjv_QrWbxbv7P_fQK_Ry5qFwoKJRK6kNvJYFrzRRsVlMnz_nHF3-fcvEdYP9xVJqA8B5Rsg4u_Us1mCIrfMMIdK-3Vs54C4YWF14RON0VaP_c9GKV7oOkGQVftbF0PYuaky3mc6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
سه مسابقه فوق العاده حساس در انتظار فوتبال دوستان همراه بامراسم داغ و جذاب فرانس فوتبال.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/persiana_Soccer/30091" target="_blank">📅 23:31 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30090">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">🇹🇷
🇪🇬
درشب پیروزی پر گل تیم تزابزون اسپور در سوپرلیگ‌ترکیه؛ محمد صلاح ستاره 34 ساله مصری این باشگاه باثبت یک‌گل و یک پاس گل و نمره فوق العاده 8.7 ازسایت فوتموب‌بهترین‌بازیکن‌زمین شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.5K · <a href="https://t.me/persiana_Soccer/30090" target="_blank">📅 23:23 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30089">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k8jju--SrzFZ35l4NM8wE5aV9ecvV_Ea7pSvM7lKeILWfRDqrMzpWV9BFC5yvYEO-_Z0cFztqX-gis3cph7GOY2a5YSpZB3r9i7X_l5gprrkTccOXq0pC5PtD6l7Vkl0_oGy95Oy43yNLQRvErNzoE40R314C6iUXLrl8siqx4XBEfZRMAvwy6EcLtobmnEugGI-oK9_Va-d369gzMZ2ktaeRUmZrPeDl7ZM6Hb_b-IqlmtPCJdNObzFo2iFgWub7rSJqVGsgJ9UnrRVLSEtzuyJ57hPhtjZiM9I1LshfVa5BbPzHfct8nag-3fXvyhJiM6OQNdXOMDFMA_WU-Qzag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#تکمیلی؛ مجتبی حسینی باعملکرد دوبرد، دو مساوی و سه‌باخت‌از هدایت تیم نساجی استعفا داد و بین محمد ربیعی و سعید دقیقی یکی‌بعنوان سرمربی جدید این باشگاه قائمشهری انتخاب خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.3K · <a href="https://t.me/persiana_Soccer/30089" target="_blank">📅 23:01 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30088">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hl8LrCXTT2rhIHFbPG_KfbjghS3eWFcvNqwiEUHncpYaB3zsKW9aVXBEkLw8A0-GUfySzFMloW_wb7t9Ld9gju4U_MSEhFF4NcnqkK2tme-07fHUvPufpfi5oi3z0dUeBQ2mOxuzRLDmSn9IL6tq0zaUFBx2ZUQ64qQmKidbRCbm5VaV5IsMHRzk7NfVGLkCMSxfy4DcZ0menHRhLpQc9UgFbfqVp7_g4tZn-gVsYbrTlohZKiqMVrjDvr0l4vMy5Y4NNPcvtUeoJMtXRbx9a1J5qeIb93h2MkUYEP34El6wBzrzVzP9QqtSowdLak09BUxzu0srV8ci7EUjSolfRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
درهفته‌چهارم‌بوندسلیگا؛بایرن‌مونیخ‌با درخشش اولیسه آتش‌بازی به راه‌انداخت و با هفت گل یونیون برلین درهم‌کوبید. هری‌کین‌به رکوردتاریخی 100 گل زده تنها در 98 مسابقه با پیراهن این تیم رسید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.3K · <a href="https://t.me/persiana_Soccer/30088" target="_blank">📅 22:49 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30087">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cvbB8DRjxjNR-_a5IPRs89ALMOWkg0ai8SohS6H3tERUiPLdxQIo53PgSB7HvODNXcMxP9d_aiXDvVAhtwUgn8ArdjFPF9XsHUSmSSWEBVOMl5K10jV4P8leHrbLiKioDa_J5PMQ9O0tjVgGNqLHylRJ_qlzcE6UJJj1FvA8QDFKRSTNtkW6ZfisansXRLXRk88PNQ2LKGerQoIYBSxBUO0MULDxysjs2cx1UTqRtg8XtjIoHqmocUW5T4lR1h9nZwr1UtYDrg6i0DzCHMi-TZ6x-9c3IzfXmOME82laRW8x2uofosjtiDXNW7sfspnF7_2Qc6Z8fKkLCkn0wEE6tw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
نگاهی‌بیندازیم‌ به‌ نتایج مرگبار حریفان بارسلونا مقابل تیم‌خوفناک‌هانسی‌فلیک؛ شش مسابقه، 34 گل زده خیلی‌خطریه‌خیلی! 38 روز دیگه الکلاسیکوعه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.4K · <a href="https://t.me/persiana_Soccer/30087" target="_blank">📅 22:34 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30086">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HFthzwII3K1NUrJJKV4gwNd2xl3VK34YYJrO7tZBtwPzn5PWoJBwZWyWIPpz1JF2RMSRsqyVezIyODtXdirtJ2f7lxlEFQ8g7vnr-rQpVWRQj-0OcbkT1zDV8P6fkZoAFcPhbUvsIzyZu9MY75G6Oj573yujMHp2awvEsCiACren4gbKSc-P3qcQ3gie9YKRbzyD85hSQNqCE5fe3Q85QfA-BH8u7t4mrzCOEX_kg_Dp-gBkXnTOWRF8IInz5HAFJLM53s3TqK3ca9ST5FtSg9l7at6nSUuVqmlxY_cMbCtFAeUHQt_6hD2yOVI_yqk04-MW2oFvlO-rzd4THqfYyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌هفتم‌لالیگا|شماتیک‌ترکیب‌تیم بارسلونا برای دیدار امشب مقابل سویا؛ ساعت 22:30 از پرشیانا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/persiana_Soccer/30086" target="_blank">📅 22:20 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30085">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rNLmIWyoYCfsiBx559-Z8tjU0Xg3ma6B_Vys50CI6NOgqdIBZrJWVZk3YZ0RDLx5WBc-55v3WIijwXGtMbbrru1KvEN7kqiHjrW0kyt2wgkRW4yaeSutjLGl69fJzdO13ehcZzTC1J08jWqzcelIYQPjw3r-gd7FWttoQmfUBcNguZdrXOTyCCvHSWabN3PKMstknZZeeR-zIv9W8vCDN64i0iV6ggNSOUD9KJ8Z2uj2LztezDsw2NAUTGTdBII8Xx-oeTiFmOiPbm1naAI7NVU2q17WDrcJP_Cpvy0Ft_j3nudLv_kXpNWeOBCtT0EHkRBuXV7AtrJW9gu98FId6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
دومین گل مهدی طارمی با پیراهن الوصل؛ درحالی الوصل امشب دردیداری خانگی دو بر صفر از العین پر قدرت عقب بود مهدی طارمی به این شکل از روی نقطه پنالتی گل اول تیمش رو به ثمر رساند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/persiana_Soccer/30085" target="_blank">📅 21:59 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30084">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OgbubG70pYAYZzPh4aiclW70IJ_EOGy_zXH3i3mJ0AQx0R7sJHyquBamuLTGw3dZ096Ia_YtnFjjinJhN4OXSMTiGhElSbvSJyrS2BejOYgX-ppcKibLv_5qL7n-D0kJubR1UQhb5TEZ1rcbTl3icLTb0KKpnvF9-Nh0zvh3-c1Eg-Rtm-uDypqqALWr-hPk5r0A7tsNyZpiaxnZTMpjeRum8f7Np0jvDCgMY96Tp8WTH_uojE1YC3HfKQmDZIjsSBsCjLra0O-o_hR7-4a0iTCZbNzhIl0lVC-AeQ3muwXmB_MZbXIIDnX1Ru7-opCXIFU-yUL8kcV_ukt3TrG1cg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇹
در هفته پنجم سری‌آ؛
دیدار تماشایی و مهیج دو تیم آاس رم
🆚
اینترمیلان بانتیجه مساوی 2 بر 2 به پایان رسید. گرگ‌ها در نیمه اول دو هیچ‌ جلو افتادند اما در نیمه دوم افعی‌‌ها به خودشون اومدند و با دبل لائوتارو مارتینز سه امتیاز گاسپرینی رو پر پر کردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.5K · <a href="https://t.me/persiana_Soccer/30084" target="_blank">📅 21:31 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30083">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CKQB6k5cfaCvGoAkW6zPqewgjF0xACUrm-yJChQwunbhroXT6WPnuRLDnKoA8TfSTLWioBDGp93sjLSmwCfCjOKQPq1BG4JEuTdX0fucAIIoY-b5ntcCbT_cKBz1uOtCvqz2OJTqs0M6tjFUAlIpPHzBQu1hRP_KWOFXEaQImYEjYV281qFa_nYbPz9IbVXPa1y27pNWK58iRX0bcSpeOwEtQa6IFZJrPRDWuSCCnm05bvID3Yc9vATw2emwNpchViTA7tQgIapQ23WXijmjLaUz_KunXVX98pFup3dYOJ2lD0KZsgaNwRTGzsTCJ39_6t-LUJ31MzyNQf_1W_BzRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌هفتم‌لالیگا
|شماتیک‌ترکیب‌تیم بارسلونا برای دیدار امشب مقابل سویا؛ ساعت 22:30 از پرشیانا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.5K · <a href="https://t.me/persiana_Soccer/30083" target="_blank">📅 21:24 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30082">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aRssfHSPXXSu0MNCW3oK-54GqAbSfg_cvucvP0ijIoWOFcerJcXGkksbTPkpr5tMvAlzfXMqSK4qmFPOnAi0VJGu7GurNcfOxJpn_EM6ExnvR_8q6Chm7Ou3cTfRwzatmodBu7VUg7vGCMoahQOKUOT9EjJ37fesVQ4sYQP06Qx9XgmXoXsijIdV6QMXMLd2ODQHuw-uhZFN8vEs_y6r0tm5kSby-JsBtLE8kemK39wbhWQVm9aXsCUYwiafQKp2HUOC-cbL4WYN1zrDfruCdIazrufZ3Tf4n6IVW4ih2ZnQ1xdPRygKJjFLZV2bQPNxLkTzPlB1eVrQNC4HoxoNOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇹🇷
ویدیویی‌جالب‌درباره زهرا گونش ستاره تیم ملی والیبال بانوان ترکیه و یکی از بهترین‌های تاریخ.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.9K · <a href="https://t.me/persiana_Soccer/30082" target="_blank">📅 21:20 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30081">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AoPP44hdNnr9oEu8XE2iHsxQN9BotC8JcK6BZD6pzlJRRfir0p2a2uDwmzDtfix6BaHysQlHR2jkAmL1islXJp_NhOXKgBG49l_d3vdG0shfyxeROAuh3qwSw9x68RBqoaUZa7QUTgANptXLAqP0qBc64d6LOGHok-8mKji80Gw7PR6GUChCYvq5NHP1ksbTL-yZYVFfx8-tfCK3pDxRQ2GfPq-BZKgbd4QyRDCC4TMUEWEdjyt00hA6rGC_6T6OwwvttUROKwVliR7_4ergM7MFOJuison3-OfZyhQPojCOFvfjRXCSawhTURjrDfJ9F0S7p-_enKV4ybcsSrRODw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
محمدرضااحمدی مجری فوتبال برتر از صداوسما انصراف داد و به مجموعه آپارات اسپرت اضافه شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.6K · <a href="https://t.me/persiana_Soccer/30081" target="_blank">📅 20:50 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30080">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d622da65b6.mp4?token=mZH4eOsHIv9h0AIs-1sb7rfyKfYWLGnMBdUoQ5z4yOFV07M8QUAS5sShdUpoSIjyllGjWF_gSAfe0Bv1YGpAqRBNv-KMN47X9wTyaIlzAOVko4QS2nkWTSv59P9gSVaFuyhWynFDAQxc9WlsPv6KUq0rtDGcQru4FySbR3_YsQSfkCre3g_UZzIsRiarZq3ig9yxTkfqcy_idMWvxx1Msv7bWkCYtBKKJR5-QhvXSrZH_xG0xzAIzmv_fvorKjqxLX1FwqipSkctpucZsCHIKPj6yaxM9dH2txER7UDcwD8bayp88ydwCemW4CzTYXVZq-_Ouj1_jiJJGBnOIvhGOA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d622da65b6.mp4?token=mZH4eOsHIv9h0AIs-1sb7rfyKfYWLGnMBdUoQ5z4yOFV07M8QUAS5sShdUpoSIjyllGjWF_gSAfe0Bv1YGpAqRBNv-KMN47X9wTyaIlzAOVko4QS2nkWTSv59P9gSVaFuyhWynFDAQxc9WlsPv6KUq0rtDGcQru4FySbR3_YsQSfkCre3g_UZzIsRiarZq3ig9yxTkfqcy_idMWvxx1Msv7bWkCYtBKKJR5-QhvXSrZH_xG0xzAIzmv_fvorKjqxLX1FwqipSkctpucZsCHIKPj6yaxM9dH2txER7UDcwD8bayp88ydwCemW4CzTYXVZq-_Ouj1_jiJJGBnOIvhGOA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟡
👤
اولین‌گل مهدی طارمی با پیراهن الوصل با یک ضربه سر دیدنی؛ گلزنی ستاره ایرانی الوصل در بازی امشب این تیم مقابل العین در لیگ برتر امارات.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.5K · <a href="https://t.me/persiana_Soccer/30080" target="_blank">📅 20:42 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30079">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dYdWEYPXBNf-oW6Piv4CsLpbv8mrVXDRprgC5_8c47X2T5zz6hNPlJKI3YAYN7L2QEnpjh99IPhoJL8NAYX7pssveZ6RdrBqTH2HA0WDGdC24mNDvTy_7WDGEiRx4ek6bTeCYuT1P54brG1DV-1HeQtk4N8B-DLi5oPUfC0ms4uVFZ8Y7QMObj6gKkZDXiXTxtPKtNKLyOZXYf-AE8DQKELEBfMnzxrZGkaWiK_lfHNf_XMBfPQOUoKCDBDJC1v7jcPSfjisaPBySu1UFpchso950bTFbnrz5Dz8PaoCa34L_Y05aaVzonU9TijIyju3YWoO0nUnc5iizDBTq3FSqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
شنیده‌میشود میلاد محمدی از وضعیت خود در لیگ بلاروس‌ راضی‌نیست و ازطریق نزدیکان خود در باشگاه پرسپولیس پالس‌های مثبتی نشون داده تا درصورت موافقت مهدی تارتار به این تیم برگردد.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 51.9K · <a href="https://t.me/persiana_Soccer/30079" target="_blank">📅 20:37 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30078">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R-BJqYTj5fGUxYLHghBae4T3RO0ybxU0gfvtt0xsMJTtSq3TH4u4rmZ0sSEuU0QZYEIA1xU4XPkVxH8SENnKIuFUBJEDNEbjT548taXZgKvvs7_zJTYJ4jTnH_N2GCtNO_Z2ynfB4s7OX1w-f86efCB821DM9eyI-7WdwfCTe56vEzWlhjxA_yxEnMwIsdQ5Pe-xi0Pza67EddK_oslvSTCB6pc5upgOTcjecrw9WehZhQkyzlHqrzzIZu66OXhl0l5fMv36WQ5zE2X4OVRGNB4JznRSngzbijnHF7kWLoJVQI4sHZEXwmysX30kSzbk85F09NP44T7nqWU_Q7vsTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇨🇮
ستاره‌جوان رئالی‌هانیومده صدرنشین شد؛ چهار بازیکن‌رکورددار بیشترین‌تعداد دریبل موفق در 90 دقیقه در رقابت‌های این فصل لالیگا. نکته جالب درباره دیومانده 19 ساله اینه که مورینیو فعلا زیاد بهش بازی نمیده اما این رکورد رو ثبت کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/persiana_Soccer/30078" target="_blank">📅 20:20 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30077">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tz6Y7BcwH8gT21JXUncqyXnCZMmFVim1-O1gSbRVU5GV0iZxoFrDPK4Kn1EfpzOw0L0_d_qGKbRW_cTCW2xrGlykK59sHn61HJZPA0g3p9gyJNNuRZjWgbCuTStTRIbhlvNCcqBg9EWQ8hbagLDM7UJ7bjV7zUN63cRUzj2tUtn1wMv-TOTfT8n4NdAQXkSoyC8Nhuvs-l2ZTUp_1IHA3attpfVvLcaOt53UaOzQu58EUfCfG3sSiqRjEOOWldg32Y1L2GiB7UoLqaEXB0dAXpu93Yhx_amqCYog7-dXd-2jLYhnAoyezXY2Ts5Q79Q0-EOyeDPkPcRsUxddWHhdKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
درآمد لیگ‌های معتبر اروپا از فروش حق پخش تلویزیونی در فصل جدید؛ نوار سبز میزان درآمد از فروش داخلی و نوار آبی درآمد از فروش خارجی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/persiana_Soccer/30077" target="_blank">📅 19:42 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30076">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🟣
در هفته پنجم لیگ برتر؛ شاگردان ژابی الونسو در در دیداری یک‌طرفه‌متحمل‌شکست سنگین سه بر صفر مقابل برنتفورد شدند. برنتفورد برای‌اولین‌بار بعداز 88 سال، تونست توی زمین‌خودش چلسی روشکست بده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/persiana_Soccer/30076" target="_blank">📅 19:28 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30075">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i9sHbtRcQZQs5L9a6lWIMaCqVEePoMbsXLRB8IpcN3REbaeYKiTiAMJv1tc796PFDilL8AVp8zlbd9VfOPKFV3PrYrsM6AjMFd5aFsfD305x99_o6yh_0rfCaNk53d-kPQGtM8ypaETffcGkCi_xwKWmJnf2NryIpRl6E6x8e4we9xhTmSxQfcHbXIeFJy2PFVK8Z96DloLUNqVVBBNCORCB-9lFtX2PwO1j_7GriHgX9m6BzqhPkSrz3w8L2AdBOHpWsr81ibrrgd8VoU2LhEjdkkvTNx0Lpf9RABws53-kWEmtiW44VcwdB9NIz0fqtf5gTfXX2rp1--YkPzcjOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
با اعلام دیوید اورنشتاین و رومانو؛ بعد از منتفی شدن حضور ژاکا در چلسی حالا این باشگاه به درخواست ژابی آلونسو درپی جذب جردن هندرسون کاپیتان 36 ساله سابق تیم ملی انگلیس است‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.6K · <a href="https://t.me/persiana_Soccer/30075" target="_blank">📅 19:16 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30074">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a5018b3d28.mp4?token=iauhPAvIE4Nky0iBWucawW_x8dQcGBXEDI6zNnGCeH9oWiogot7_tqbW9xXDkzlJcmN3lRc8u7ZOFubJy8bVbY7Gw-PmJaXbY5gQ4X5OZ5R5RVMKTbU4MxRdnS1CWS1lUXmJ8Xjvs1HJdwbUNZNI0yqDmHs1953j5OX1124sNV6v2yC0torXXAZsLjyZ7uSsZ2IwYSh9g0FVZfq59hNaAU4QFtKOcbcWj3dyKgFn7lstZj_p6IXhEBz6ifletldwrIntqj7nz8IeUv-8ShevDnBkzS0O8tdzlvKySWCDQBuYls78fY8sY21XhTdcT7FlNdcqmF5nYiortQUTK5LAxQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a5018b3d28.mp4?token=iauhPAvIE4Nky0iBWucawW_x8dQcGBXEDI6zNnGCeH9oWiogot7_tqbW9xXDkzlJcmN3lRc8u7ZOFubJy8bVbY7Gw-PmJaXbY5gQ4X5OZ5R5RVMKTbU4MxRdnS1CWS1lUXmJ8Xjvs1HJdwbUNZNI0yqDmHs1953j5OX1124sNV6v2yC0torXXAZsLjyZ7uSsZ2IwYSh9g0FVZfq59hNaAU4QFtKOcbcWj3dyKgFn7lstZj_p6IXhEBz6ifletldwrIntqj7nz8IeUv-8ShevDnBkzS0O8tdzlvKySWCDQBuYls78fY8sY21XhTdcT7FlNdcqmF5nYiortQUTK5LAxQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟡
👤
گلزنی‌سامان‌قدوس‌ستاره33ساله الاتحاد کلبا دربازی‌امروز این تیم مقابل خورفکان در لیگ امارات؛ در پیش فصل باشگاه پرسپولیس خیلی تلاش کرد که قدوس رو به این‌تیم‌بیاره اما مخالفت همسر او باعث شد که این انتقال انجام نشود. همانند مخالف همسر مونیر الحدادی برای بازگشت…</div>
<div class="tg-footer">👁️ 50.3K · <a href="https://t.me/persiana_Soccer/30074" target="_blank">📅 18:57 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30073">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u3WKiX1GQhsCH-MUhXFx7fzgndQCtRm_-W7xFIZaRfU9bhN0yLY9bYH4bHDQrAc-Fs1a9uXPf2n3FMpLa1kURGDqHelQc_b2TaWJdEwY7A2o9QMGpY8GKu9p0h2KVqEDzZOlAEQ2MR6VoAbgSJMjNUzMp75PzZ_mCxhx6UfQXCXfskZFiVLz4m6NiZ-pSQK_DyqFS7klfiqU99_9riHZrQqeimw845Y4Fv93zAVcXnkPqP87nBKDFINlAI3phFNuFEontZfbEAW3C4R2uiV7zdd_a6EgpOYim-ckzJfmxRjPQmurOEuE6FBrjdeWv-VsIy3FC67PnYRNcuLCYMIqlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
#تکمیلی؛ دستمزد بشار رسن در پاختاکور سالانه 600 هزاردلار بود. این‌بازیکن در نیم فصل قراردادش به‌پایان‌میرسه و علی‌رغم اینکه پاختاکور دنبال تمدید قراردادشه اما گفته علاقمندم که به تیم پرسپولیس برگردم و اگه باشگاه بخواهد حاضرم مذاکره کنم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.6K · <a href="https://t.me/persiana_Soccer/30073" target="_blank">📅 18:42 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30072">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9989fc3781.mp4?token=G7i6V8R8wEPK3ALR6N-LVguhlw-VzaImbi_Rp-1CjqqRiHw0kLVE8wIcODKc1Noh3AameCfSkQot-Qz0y7I4vlBV0HWQzptBdEUfDTQQQ4kvvUBBI_d8cck9voOO-x303XDPxT4pCIyKWfSmOCxq0ShLVhRj9NF7jKcikEG69uD-r5gYfVUvgx6n7wxqQR4NLpWclzR6secOI5fC1j8pvHO0NX20wUTY3NTTtTdTf8TERlEwZPm6CRx48-dDfsahWPTt4Icc1E2gFXyzNUI2WZBcxRouot1qkbo2F5U3guerVQ4jH7-X5KLkHVRqjngPzr8Iqa4YQZI0B7e2rVNbIQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9989fc3781.mp4?token=G7i6V8R8wEPK3ALR6N-LVguhlw-VzaImbi_Rp-1CjqqRiHw0kLVE8wIcODKc1Noh3AameCfSkQot-Qz0y7I4vlBV0HWQzptBdEUfDTQQQ4kvvUBBI_d8cck9voOO-x303XDPxT4pCIyKWfSmOCxq0ShLVhRj9NF7jKcikEG69uD-r5gYfVUvgx6n7wxqQR4NLpWclzR6secOI5fC1j8pvHO0NX20wUTY3NTTtTdTf8TERlEwZPm6CRx48-dDfsahWPTt4Icc1E2gFXyzNUI2WZBcxRouot1qkbo2F5U3guerVQ4jH7-X5KLkHVRqjngPzr8Iqa4YQZI0B7e2rVNbIQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📊
نتایج الطلبه و دهوک که تحت هدایت علی رضا منصوریان و گلمحمدی اند در فصل جدید لیگ عراق.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.6K · <a href="https://t.me/persiana_Soccer/30072" target="_blank">📅 18:25 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30071">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f0dx1sW7v9EI8cLOCnBEZnOCfeHB_fgfSbMLclF2K-x4lU9gf9qKS9c83lNzSN3_svyCGcQkackJ5-nJOYjcY7lmArRnoMWHnYvpzxgAXwOvBl5hP9hcQOhttysFL6yZmdJuumONP5mCGl2XRnnIZxdqDs4qSMdkv9g5Vmmgv5cVHpulLSV7aPYSPYdfnp8SZvXAhTooG63KVJ-LVeqwurszRxsPkfdGHM9BCCDub3SoqoUcBFTBYehS219KCudBGuXicfNyHV422mZkFq9wJcejF2kXmwA75q-QBQtzQF6u08kX8OT3bp2cDQzxhGDWD5OAe4z9GReE96WsfD9APQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
👤
احسان حاج صفی کاپیتان‌فعلی‌تیم ملی تنها دوبازی برای شکست رکورد بیشترین تعداد بازی در تیم ملی که دست جواد نکونامه فاصله داره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.9K · <a href="https://t.me/persiana_Soccer/30071" target="_blank">📅 18:16 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30070">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fw7TuXHEOfBaWWogvUAtSzki2bKQ5P0SNA8Ddh8_1Tv1r-c3w8IFvzZau2tg4LXLT-JsZ56q6nF7SpToEzx7fd1mxZ_43VSTksWlwAaOo1BUy8lCDLg5xHgdzcJma19rrBECG5B7lHqInLQII-eIZr_3ssRCeeE1T4f3tUXr6bUdtd8e_AszI9u7YMDSLhqLQPJVbX5vKqhadUVGg5bCchfBaAttgY2WaV9AIszuiOAMCO7i86N7Rqa35G3fNWLMgTzQEcv63DOv7ehe_8Mlfzu7J38kzRaj8gSTVQ6rFNGoJk8pDuWwTC0mG_mC8fBnZTkkUq7sFOvj-ctA7rStFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
روشنک مسئول مسابقات لیگ: یه چند روز صبر کنید مشخص می‌شود استقلال قهرمان‌ اعلام‌ میشود یاخیر! احتمالا امسال جام حذفی رو برگذار نکنیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.6K · <a href="https://t.me/persiana_Soccer/30070" target="_blank">📅 18:16 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30069">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dDm-mhPPChA7QlUJT3dVDzIsbwaDbQ3vkZHbAhx3XSNnW7iSVmItjNqO-QI1VCHh5yvpM7rDNvI9Gv_JdY-_dtK0B8iW7l56E_1FKxEB4dwyBH-Td2URWAv3InS2j86osnOsjrwLxsdww_8Hv3VEPsG7XbgfdY-0w5OVVWK5IL2-vSa93bZ7AvpnB2Vioep_hAKr3mKjTSjOjtrrU9zAH3I6S-XxHuAEUMBPNX2DLSmXMaMwzTlhTZdBoFbyaDeEqJEcg8km2fMitJ7KwsN37xcThGBmnrq8m5ABl9qb2sV3XpstBC9z0VYU2LlkNQxCAjtORmhNI3f7VArFLv83UA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💎
سایت پیشبینی Yekbet
💎
🅰️
🅰️
🅰️
🅰️
🅰️
🅰️
🔔
فرصت ویژه اولین واریز دلاری در یک بت
⭐️
یک واریز
🤩
دو جایزه
🎁
⚠️
یک انتخاب هوشمند، دو هدیه ویژه
تجربه متفاوت با اولین شارژ دلار
ی
🤩
🤩
🤩
فری‌بت ورزشی +
🤩
🤩
فری‌اسپین کازینو
👀
با اولین شارژ حساب از طریق ارز دیجیتال، یوتوپیا ووچر یا پرمیوم ووچر، هر دو جایزه رو دریافت کن
🗓
شرایط استفاده
🤩
⭐️
فری‌بت:شرط میکس حداقل ۲ مسابقه با ضریب حداقل ۱.۸۰ برای هر انتخاب
⭐️
فری‌اسپین:قابل استفاده در بازی Yummy از POPOK
﻿
🌐
لینک بدون فیلتر
🌐
ورودبه سایت بافیلترشکن
------------------------------------------------------
📱
کانال اخباروهدایا
🌟
g28
🔗
https://t.me/+ioIBrQfqMLtmMmEy</div>
<div class="tg-footer">👁️ 53.3K · <a href="https://t.me/persiana_Soccer/30069" target="_blank">📅 18:16 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30068">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/841d5e76bb.mp4?token=WTEmXoB6pQReN4elsT_UCarHaSWPmt8G-aarGmEcL0impkhkkXwy5ShbiA8k1_05dyTHvoMlBoNvEAx22EiZQY7WTQP7W7uxQC0nKCX7a95ywa6dXBlSTTYYQLAIHG5LyiCr3x7SWHLx9OlOcaq3n8MAmP8Ey6opALzaxuyq04OMnsnV8wLBj-O912aSmehP7pdoDhY2ei-9Ci7EgnmhnDeckGGzj0wfcSRKFgrw6g7qBnKYuNVf5knzmmp2bk8rqEjWFOIh7h-sCWFtTXL4BQJ1dr6GgnkfUCukn2xt7H0ATcESn4POUNhUcTHnTcS6xG-EokgJBtL2bFR3UJQ_Eg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/841d5e76bb.mp4?token=WTEmXoB6pQReN4elsT_UCarHaSWPmt8G-aarGmEcL0impkhkkXwy5ShbiA8k1_05dyTHvoMlBoNvEAx22EiZQY7WTQP7W7uxQC0nKCX7a95ywa6dXBlSTTYYQLAIHG5LyiCr3x7SWHLx9OlOcaq3n8MAmP8Ey6opALzaxuyq04OMnsnV8wLBj-O912aSmehP7pdoDhY2ei-9Ci7EgnmhnDeckGGzj0wfcSRKFgrw6g7qBnKYuNVf5knzmmp2bk8rqEjWFOIh7h-sCWFtTXL4BQJ1dr6GgnkfUCukn2xt7H0ATcESn4POUNhUcTHnTcS6xG-EokgJBtL2bFR3UJQ_Eg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
عملکرد لژیونرها در رقابت‌های باشگاهی امشب:
🔴
الشمال
2️⃣
-
1️⃣
السیلیه؛ پیروزی‌مهم یاران امید ابراهیمی مقابل حریف خود با گلزنی بغداد بونجاح!
🟡
اتحاد کلبا
1️⃣
-
1️⃣
العین؛توقف‌اتحاد کلبایی‌ها با وجود درخشش ستاره‌های‌ایرانی خود؛ سامان‌قدوس ستاره تیم ملی ایران زمینه‌ساز…</div>
<div class="tg-footer">👁️ 48.2K · <a href="https://t.me/persiana_Soccer/30068" target="_blank">📅 17:54 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30067">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qctMDPrj-4xqN2r_o1vF_Ko-vV2RPUY3JlZ4O_z0kcrRYvnUwXg5bocGejkZeicnH10QkLYNcfZaLJsSP1S79babUKrJw9AntZdvSscL9SZ7fDtcQO0vWcO5PfnocbG8WfEPOn32YSv5RBDQ0-Ejcn-Xw-bAlWJFEQA9iQ7ZmcvVVYN4kr7hmTnDxnS8jLho93grt2n0V6i6Rs5hdU-VUQDohU0JEqgC-H-6RTRPAZgAF8C9uUcAXUEsL2OoTLOE4khjfupNwQfbq49c5w4VxWpzeiUWCiCBW_0S14lJ7q-kY1bEDQPLOXxz_ZyEjdjICunPY9GIvUiBRnRPeD741g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
👤
🇧🇷
#تکمیلی؛ مدیران باشگاه بارسلونا بزودی مذاکرات خود را برای تمدید قرارداد رافینیا دیاز فوق ستاره برزیلی خود تا سال 2030 آغاز خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.4K · <a href="https://t.me/persiana_Soccer/30067" target="_blank">📅 17:47 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30066">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Uxl2sDmiVcEsSkePX1204hlzRkovzEPsBrYlVYPjs0CIMJMcTbHVMcjmCcopBzXYE81V0Lj6AgEWM3eZ0gmtS-rNGoUqRd1qFp4wKr1-xk2Og1VV3GK9dgHArtPnBQ3FqmlEKDL-7uHDWLlBYPnxekCLe2KZ_lj67ZwV_tPJDQxbH5OJsO0aVrj0SniscOICtAw_t3XvYirYzkB8QHAaTXMnySK9RCl6tmJyWi0-M0G9f5CaqI5RPgK-WB9Vx-tYH8t4jPyHsmVsA-D7EfmHQTkho5v0VKMqrBf4Tm8uNo9OGiSyXibeMy-dexPWMiI71Tj9YjC5ukGzh_K1MdvA1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
به مناسبت دعوت دوباره CR7 به پرتغال؛ نگاهی‌بیندازیم به‌عملکرد فوق العاده کریس رونالدو در تیم ملی پرتغال؛ نکته‌جالب اینه که پرتغال تموم افتخاراتش رو با حضور CR7 به دست آورده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.7K · <a href="https://t.me/persiana_Soccer/30066" target="_blank">📅 17:27 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30065">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QCks3t4yv-eyCO2NLjHGsnLmOcU2cRSqKFAJsFsPbw04ZBaY-0VQHxCgR2DirEfbBnqdetFYXQlYbKQglQcP6vSLZvFhJtsVG0uSLdf1nMqd9JA1uRnlfJJwUnTvdxdonNsQoXAPpTTFAdDDkCAJGDjAA0AeJ2Xz1qS4Pkk7rh9DJMxgzg54uKujsD4LPQS4gYo6s-EYxyEvXZQ5AQSkd2OoEF_L2opH7Dnci8T7MxcFRjzKhBzHuwGKskrtIbjPyJjQzZJsbcBxFlF-dv95vEtzaxYSfSnmwXAkYSTIiVI9yNUPgNIi1nx8YwWtFnjwvZufHfFtG7KEq9g5zCFvNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
عملکردفاجعه تاتنهام دی‌زربی در این فصل لیگ جزیره: 5 مسابقه، 3 شکست، 2 مساوی، 0 پیروزی، 8 گل خورده و تنها 2 گل زده در این فصل!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.2K · <a href="https://t.me/persiana_Soccer/30065" target="_blank">📅 17:18 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30064">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ufsvij-TjGYZSjuK9E-mvGj4KgOM9nP27t6_qlkeNu2b264mQsBAyI7lFx7Eurzorzsjnwx3kr_WYnKjHiZtCGfil9GgII48n4J-mkEyByBEA29y-JXv7Y_s1_dsdB_yMumFkP4qMliE__Sja2m9x4rSc_idlaiuLQYRcWHt1FCANrW-VLiz07t9QeaYvdAaPkZNapHGbsaNj6YxQ9P9KpjZnJ_P0wsGikjm1qxfAq5vQoeimYeK9NB4Ke3vsHEQhv6SeB-ichIDx4PxaJh8cSkXg_WC9RhDm8jqvWmkSjJclN3r5nStBwyYTp9_HH8bpxjkC6oLAPwutmmeCXbeAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تایید خبر اختصاصی شب گذشته پرشیانا
◽️
مجتبی حسینی سرمربی آلومینیوم با عقد قرار دادی دوساله سرمربی تیم‌نساجی شد. درحالی گفته بودن بافجر امضا کرده گفتیم فقط مذاکرات مثبتی انجام شده که دیشب مالک نساجی پیشنهاد خیلی سنگینی به حسینی داد و مستقیم رفت نساجی.
⚪️
…</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/persiana_Soccer/30064" target="_blank">📅 17:10 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30063">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a224e3381a.mp4?token=Ijqxg-YQgc-Lgpm4C11keBHRgONVk2oy7oiEXyfpAwZkjqF0cwKFRNwpJQzK3_9qjts7bgoqUYWXe2X8is1UrIUXrRrXRNALCJpdmlsm9Wmv7gFHw9F8_NkB3QKkyna83TP3c9JoiXQEl0VKW77kmx8QW6oQ7mIAaPVrCDOwQHRrzy31vBys32-98iDbMnyX7tMQlEwM29c9S5bjpRJFKgLvW0lIWx1-TyIOvfs22qSr2iayuKf62pUIIvQK6kKLNA4oUt_umi_hMmfnMQKZt7UXjnJSPP7VPKfb8KBfvMtyyP1WNHsWoFQKOuXYokfVsoQzEChPqZkdVFSFhDqwqp7FrVh4WHufRPtpsoeJ4GG-rMhuwiRFYmT9kWaNzZcQPVEyKBfaWPrrvEt-fBT5EPQdPTjo70GrEloAp0nxYIbXWCOZ9lAiusZZ_za4_pMhEfvZihkip_V0wTMHDcfpyPAfA9Up5L_MlDvCQTSZU8nyg1FMFOn-gKlyXR9bIiV-w2ZI6oDQRTlNuJfK2HJfIAVLJdpAFEgWDddr0cLfDnJlQod4hZ1Ry_KpXCSdnybRR6rnz1OsRTcdChGaYVHt5-4e8CA2XEyJ3kv2J9J8C3Rb5QiOozZv3Ffk2K8Cl2Sz8dIUNFhGWej_c0OpD030sYAKfoFv3djnFAeyWMiqNVU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a224e3381a.mp4?token=Ijqxg-YQgc-Lgpm4C11keBHRgONVk2oy7oiEXyfpAwZkjqF0cwKFRNwpJQzK3_9qjts7bgoqUYWXe2X8is1UrIUXrRrXRNALCJpdmlsm9Wmv7gFHw9F8_NkB3QKkyna83TP3c9JoiXQEl0VKW77kmx8QW6oQ7mIAaPVrCDOwQHRrzy31vBys32-98iDbMnyX7tMQlEwM29c9S5bjpRJFKgLvW0lIWx1-TyIOvfs22qSr2iayuKf62pUIIvQK6kKLNA4oUt_umi_hMmfnMQKZt7UXjnJSPP7VPKfb8KBfvMtyyP1WNHsWoFQKOuXYokfVsoQzEChPqZkdVFSFhDqwqp7FrVh4WHufRPtpsoeJ4GG-rMhuwiRFYmT9kWaNzZcQPVEyKBfaWPrrvEt-fBT5EPQdPTjo70GrEloAp0nxYIbXWCOZ9lAiusZZ_za4_pMhEfvZihkip_V0wTMHDcfpyPAfA9Up5L_MlDvCQTSZU8nyg1FMFOn-gKlyXR9bIiV-w2ZI6oDQRTlNuJfK2HJfIAVLJdpAFEgWDddr0cLfDnJlQod4hZ1Ry_KpXCSdnybRR6rnz1OsRTcdChGaYVHt5-4e8CA2XEyJ3kv2J9J8C3Rb5QiOozZv3Ffk2K8Cl2Sz8dIUNFhGWej_c0OpD030sYAKfoFv3djnFAeyWMiqNVU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
🇪🇸
لامین‌یامال زیراین ویدیو که یکی از فن پیج هاش گذاشته گفته همین‌کلیپ‌مشخص میکنه که من در حال حاضر بهترین بازیکن جهان هستم و مستحق بردن توپ طلا فوتبال جهان در سال 2026.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.6K · <a href="https://t.me/persiana_Soccer/30063" target="_blank">📅 16:30 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30061">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h20O21N6evy4G8SFgMj00oSXvyyPaCPTY3tKoizu1YBdObNKjNEaoypXviO2xRTwd7hKvxny-2Z2DBRin-hpsLu88MlmF96pLsj53Mpl-jjlX0-MlMxXE2zW_ghugmY6AuGowhkW22yG866IJf61pXFrrPtMhCJE6K1cwY-BrT8erjmJg-kUEQF5uTJZoHdkn8C2DMes9gzbMsKBQFOFe9TLOoB9_SYMkOYJ5GfWzldygLovszqy66ZDuGXB6_2RdVjPiRIgOQrL_fKFErZiuOOV3sI1uRC5AwVWm8RqfTn0nM7kmWqQU5dkMIrX9mcFPDuG8xOzpsPT6CXF_UAOBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟠
طبق‌شنیده‌های‌رسانه‌پرشیانا؛ باشگاه فولاد برای فروش یوسف مزرعه وینگر جوان این تیم در نقل و انتقالات نیم فصل 150 میلیارد درخواست کرده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.6K · <a href="https://t.me/persiana_Soccer/30061" target="_blank">📅 15:58 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30060">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uCweGr77a367MJY4fSoi4noJ9r0FSjq96RC2MpGvqbxW4pCMjahYnzvDVbpIEX-Co7X3GBUceI_xL_2iMpWzVQl_J5qsFclJ9J-6GD0ic6Fjx75v4Nb_DtQVnkyWyZCjv8pjsbg0pirJSUO_fpyGKjPzIIRneOzxwDIhUZJ-PGQQ_ENGEd4CyyFjCtH9cE5mnF0EWjVcElfxcMq1g_zL_3QLkmGQXrgj9d2jk9LCwLz7_6ni_ZZJnpqoi88XQR7XnLN-LxwY8y_SiBUNTSjGQQ_O1aQ0PhVpXCNsLQDPcNyoh_LupBW_O0f6mz_sq3kL5cWZeCmX4Qqebr2enReXDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛طبق‌اخباردریافتی‌پرشیانا؛رقم رضایت نامه عباس کهریزی 20ساله150 میلیاردتومان تعیین شده. حال‌باشگاه پرسپولیس میخواد که با رقم 110 میلیارد رضایت‌نامه کهریزی روقبل از پایان نیم فصل بگیره. کهریزی از استقلال نیز آفر دریافت کرده.
⚪️
Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.9K · <a href="https://t.me/persiana_Soccer/30060" target="_blank">📅 15:44 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30059">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TKvJa2vv2A5szafW8i20LlIujxH2xIpZyyhXV6rKNH0XAKocAEsy191dORDIXxUhrvOJPNszv4GJ5SRaKd25iXc8KLLTGYF23VdS3X14ZYHClXFYr7mnMJMRqzPib7VxSII8dlYRHllvfLBOpdgCMCVZajX9mJ0YPtfeb-KCx3nogrju_2JNwvXqbakWbXOAd12KC-OWrPgNlhmUfF8NTkc2YnKBVMQHdkTAQKhNY225by140qVVPwm77ZPyXuz_AqSgkXXPc43lvDDaPRwPfKB8ENckxra5tAJpxJLYW6mviBOxPK0DG24WPi36jI4UwO7UZ_Bp2tW-e6vKv0esDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
👤
خبرنگارت: بین کریس‌رونالدو
🆚
لیونل مسی انتخاب‌توکدومه؟ مارسلو: کریس‌رونالدو تا ابد. بنظرم بهترین بازیکن تاریخ بدون تعصب کریس رونالدوعه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.4K · <a href="https://t.me/persiana_Soccer/30059" target="_blank">📅 15:29 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30058">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C1FZ0ccQwm6D_1dRs2cPmpZhLsoLUHehYhlx-x2z34EyO3wj2tuwS4Yq2prtPyTqwjZLXvIBZQ17ZDVs11ohcvOJDyicl7GmJM0g5cO6Dl8aZ_QSzPj_0H0FGL85kf0-ws82MT5wsPdoz5YlpC1ey4uCHfeI6U2PVVdafwspXEnO8PMvh-JW9MljnCAMYYBw88kaV6bDpnk6JKbKfkJzAHgPctJT4zDwIxpR9KyrS7X_c9b4-64RfaoIF4bDkDRO_UukxyM7AFxRzg6EnHTCP9bKsP_h70t2eBhuOC5SpSrVdkoNwDXEiCWRNQQXyR0kDWz9wAiUxsV79_Zx8MNVrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
باشگاه پرسپولیس امروز مدارک جدیدی درباره قرارداد یاسر آسانی به کمیته استیناف ارائه کرده و قراره تا اواسط آبان حکم این کمیته اعلام بشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/persiana_Soccer/30058" target="_blank">📅 14:54 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30057">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cbb8zIQs-BAhwEaFcKpnmOuAJv7SkbRk8-aTude38XGxzA6FgelIcyJaGJZGpjsZYors0ypJ4qF4AF4N58zsConpwIdJPkMr9xnaj2Dxfm5A_kokHLqleQRJcPdScehmn7R1V1nfH0nKdAtV1bWek0wPTLY5vD_wlimwWxUvdh82oCDcE5bxUZj9MX36U625h5lEdFv-Tbbw8WI_Qfgsk9GUlh745b6WWRR9PKqMuwUp3RwK_IPs4IwXhKGof0m09JEbKpXVnm3snlACeut2gFBUWnPNpijbPa_nUUnSlHgFVFNIKWSztcyNG7-FS2i--iU17DM-biC_ypbrgGUUZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
بیانیه‌رسمی‌کمیته‌انضباطی‌درباره شکایت باشگاه پرسپولیس از یاسر آسانی و رد شدن این شکایت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.6K · <a href="https://t.me/persiana_Soccer/30057" target="_blank">📅 14:43 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30056">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WFTCmFQ8IUmf2yayddu2oLXVYrwlOLZbywOk-bVatAYO0_vzCmM6j4sMzIThX4QwgfjaACVkTueeFnPN_Mi2UoI6EI-6E3URlvuigzY5zrQD86wGHh3vSlBZXAGzQjduT91cDXjzkLBOl-sspavvQqTWA5XbQnew2CgX7iBS_hv6_zxU_jmAw29BMVm4Yp16XwLnAWiw_J6OOp3OBJdRJoHHbQ8Oy7nVnbXWSfuXeQegHEXLaXbVRaqmV1zm9-1k43gUdQleRKMejEZiCVtr4B_3ZZUWiIeCW2APq8HIJ7JvHwy-TSXSxM8LWEoU8ArFZ_djohQmrVybY71r6135ug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛مهدی‌تارتار سرمربی پرسپولیس در دوهفته‌اخیر بارها به مدیریت این باشگاه اعلام کرده بود بین امیر جعفری مدافع چپ گل گهر و ابوذر صفر زاده یکی رو جذب کنند که انتقال جعفری حدود 100 میلیارد تومان برای سرخ‌ها هزینه در برخواهد داشت اما انتقال صفرزاده به شکل…</div>
<div class="tg-footer">👁️ 53.7K · <a href="https://t.me/persiana_Soccer/30056" target="_blank">📅 14:01 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30055">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🔴
🇫🇷
در پایان بازی شب گذشته بایرن مونیخ که با هتریک مایکل اولیسه همراه شد بعد بازی ستاره فرانسوی باواریایی‌ها حسابی سورپرایز شد. نیمارجونیور کیت‌خودش رو برای اولیسه فرستاد و باعث‌شد‌ بالاخره اون هم یه بخندی بزنه و چند جمله‌ای با خبرنگار صحبت کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.4K · <a href="https://t.me/persiana_Soccer/30055" target="_blank">📅 13:52 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30054">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uD7Ch_5pfVgpmRawZtJJbIiMsodD9GOVi34EYMhIJE6isdXAMP1Ywb-z9JegXVhi8AzcUoXcuRacLs1KENE4AGK6HZn1myrDs6rXHR71B7ev3qKhzHVriVNQayOQG31ECVeIPsl0WirjF4SV1IzUJ6dK8-kw6cPmJoM84N7a1j6ESI1BKtGIRrZCh-61IzDvchaHTiKsNS_jNrZ52TLwYHkcdSBy2RoR6qmXGPkYiYVR9C51_o1-Sez3ZdzEgs5UWx34gc6fipQIWzWNpspKuPXMby3caZPtuq8nrlcy7CPFysdVXrvb_I9Rmav9ZNb3DScUBxEkh9KTBWKxIRZalw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
🇳🇱
وسلی اسنایدر سه گنجینه گرانبها از تاریخ حضورش در تیم هلند را برای مزایده گذاشت! توپ نقره‌ای جام جهانی ۲۰۱۰؛ مدال رتبه سوم سال ۲۰۱۴؛ توپ بازی هلند-برزیل درمرحله‌یک‌چهارم نهایی ۲۰۱۰
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.4K · <a href="https://t.me/persiana_Soccer/30054" target="_blank">📅 13:28 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30052">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bFlPYWtVvG_odq-rFt0K8Nk4S1Lv9nQolCdLGbmosC4b62Qtnm6jFlwn_RTQOC6_ZrXRYulU3SonibVMsGGvB3GbEno62Ejz9LJ6Bnx9HOMqe4qfnkJEBptqH30U26UUyKdNloiH0LUTxd7OJ3p98LrLe1E7zwHCsMLWV9pX8URVDqajC_QMyX-_rwCxSq9rNUt9-WPCHM0MJYhjst_LVTZ77QP4XeVNC6Pb15lUbr6ko998N-U75HnXqEgFfuuKsBxBUWGyYdJ_Ch2TZ1rryCV45unuE-qgIrovdVcCVj09fyPS4_2LhLHew0dOStSC8UCOKTxEc0VVpf7j2-kGQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/df5ef3d951.mp4?token=LbzCu7E5_iyQ6gBQ-za2JldIqmDQM3uWEg524ePYtbU3CD7yUdsd8ZL6RsXFKQQ55m029_9v24yYRwnM2_2Pcj4uEP7M_DAOZM0isYJuXwNZeXnNVpgkj1gUiJjIWVMXR8Gf5urxVSzK34qRfTB783cHZCIz70xKQnjB4H4ZV8DDz_U4zC2YH20dGVuGNcS0kGLTmQoxUr6kmt3b3HrQeMZnpCKoLlJDzmlMZEIjCf6wJoi9iOJYT-vw1Z6AUGPjTOV7nAm-eDB1WNVwzkiynSHUxqqVt-szo8BIltVyB8068KJW29awLHBpe2aJPBjVN9GvAnDzjp8DBzIt6D1eyQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/df5ef3d951.mp4?token=LbzCu7E5_iyQ6gBQ-za2JldIqmDQM3uWEg524ePYtbU3CD7yUdsd8ZL6RsXFKQQ55m029_9v24yYRwnM2_2Pcj4uEP7M_DAOZM0isYJuXwNZeXnNVpgkj1gUiJjIWVMXR8Gf5urxVSzK34qRfTB783cHZCIz70xKQnjB4H4ZV8DDz_U4zC2YH20dGVuGNcS0kGLTmQoxUr6kmt3b3HrQeMZnpCKoLlJDzmlMZEIjCf6wJoi9iOJYT-vw1Z6AUGPjTOV7nAm-eDB1WNVwzkiynSHUxqqVt-szo8BIltVyB8068KJW29awLHBpe2aJPBjVN9GvAnDzjp8DBzIt6D1eyQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
🇫🇷
در پایان بازی شب گذشته بایرن مونیخ که با هتریک مایکل اولیسه همراه شد بعد بازی ستاره فرانسوی باواریایی‌ها حسابی سورپرایز شد. نیمارجونیور کیت‌خودش رو برای اولیسه فرستاد و باعث‌شد‌ بالاخره اون هم یه بخندی بزنه و چند جمله‌ای با خبرنگار صحبت کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.7K · <a href="https://t.me/persiana_Soccer/30052" target="_blank">📅 13:07 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30051">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bLaC9Vdgt_-306MF72XPC-Kh3iJXw-N4-_JxUZXnnBf4HqEvXR2qQZwmwA3oNH4vxWz3OAIVKJ9OAWAJMzrlMn9faegZ2pNesu5VLFqQU2mgG0WlvyyFSY3VxcTww9tzx2Nlzx3pczYJGZ9aixsrUhuhFzcHv0ceIepYv8E_FOYg-m82bRKleIH1BYmGEIx_R-ruN0ZVfhOM0bnLibt3T_N0j-jGCWP9rVuF6tL4J16HmEJO0SO2htYjJGfBNNlsv6HmpFzZzglcJZLXbIs-UQXOM0b2LmTO8G040R_g5E95gwcB1KpCiQTnLMR2TxTWocJ4N7oxnAq1kfz9Y5o06w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇩🇪
هایلایتی‌ازعملکرددرخشان کریم آدیمی وینگر فوق‌العاده سرعتی‌ بارسا باپیراهن این‌تیم؛ آبی‌اناری‌ها برای جذب آدیمی تنها 20 میلیون یورو هزینه کردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.4K · <a href="https://t.me/persiana_Soccer/30051" target="_blank">📅 12:51 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30050">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6111cc9977.mp4?token=Q6sSdh2a9lAeVrO0rb0ZGRO8Pf_iWaA14gPyW22DgaFAwFLkORqo_xgKs-SymuQPlxv5JlWKe-sVqxE_5r_p2RTxGoG8mlkmp8M-rhZvFM7hEE6mULQuJszGYXZt2akPDfNLjVyU7sHEr7pOa1stiLJjsHw8_K2bU9cPtSojDggxdBUNM9rFLV9Ps67Tl4U-MWg_tXZsb3jsQC3jjLqNgESC1y6lWhkbtxAr9GUq8-gB4-VAxDCAk4miHYtXVFcn81FuI8Wzb-jr0rBTLDU8zCy5DhbfAEB7Cvtzh_9Nh5oF37zvIQdDbg2hGE43lePuRjJdPT7Bo-MJ4swsk-Q1NA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6111cc9977.mp4?token=Q6sSdh2a9lAeVrO0rb0ZGRO8Pf_iWaA14gPyW22DgaFAwFLkORqo_xgKs-SymuQPlxv5JlWKe-sVqxE_5r_p2RTxGoG8mlkmp8M-rhZvFM7hEE6mULQuJszGYXZt2akPDfNLjVyU7sHEr7pOa1stiLJjsHw8_K2bU9cPtSojDggxdBUNM9rFLV9Ps67Tl4U-MWg_tXZsb3jsQC3jjLqNgESC1y6lWhkbtxAr9GUq8-gB4-VAxDCAk4miHYtXVFcn81FuI8Wzb-jr0rBTLDU8zCy5DhbfAEB7Cvtzh_9Nh5oF37zvIQdDbg2hGE43lePuRjJdPT7Bo-MJ4swsk-Q1NA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟢
سوپرگل‌دیدنی‌فرانسیسکو ترینکائو ستاره الاهلی بعنوان بهترین گل هفته لیگ عربستان انتخاب شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.4K · <a href="https://t.me/persiana_Soccer/30050" target="_blank">📅 12:33 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30049">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a2wYgcD9IGVNmOXXqt-a4Iyl6oClJXGWQiQ870Pogzj0MEiEjVa5rWp86SVnnTzyooG1ZpGqPGK-v49M3FSa6GOs6Nlh-SqvJNPcXbqof64qM0qAz5Lxckpb2A27Ap6fxklTIGtEbjgGq-Hi-IdSvTXYzxt8Vvgmq_TBUSKJI5_D8768OpKNNwlDKjqzaYEOV9Ua8N0wpaplyDDBdsSDI-MBwJxaSoEthSqKdNHtJIBkOvyupsnUbWbpxwF9RO_jBNs0v2d-QVVMXbrpB-uNPGGcjZ7nXpzF33xcRjrs-0k4p8CRPYqDoyirJnL098PhlHbZZ_pKIYaljCoKIeQChA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
آندرانیک تیموریان دستیار قلعه نویی در تیم ملی بعد از سه سال کار با او از کادرفنی تیم ملی جدا شد.
طبق شنیده‌ های پرشیانا؛ در صورت موافقت سهراب بختیاری زاده آندو به کادر استقلال اضافه میشود‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.5K · <a href="https://t.me/persiana_Soccer/30049" target="_blank">📅 11:53 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30048">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D0K2M5Pyttn2Yq1Vr0tDyyTuFAvP7xEzX1B1_cMXPpoTEO0uOHuB0NC_SNQFOmMtUXZHnnTaJQK1FEvRx-DLs45TaZXgipknUuMwd0gkgW73TG4059xFm_j6AVY-h54uDyCjVykpvbL9tb28_wkYLNBaLX7Dlw1OVMFmjiQ9J6nMV6NxLlEOBOzMqo2gBkUVUcVCWGb4gffUQ8oBEiPQ3XLHH20-0_t3cB-tfi-gmq-lT8pzedEablRCbdEnJeWMITALNfikLiWH40pTLXYcH9Wiub9Dmm2GADWbtr58fuxpkiVpHue4PUBHQDqVzY4kzZop5IhMXaxdBDPtvD30YA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
توییت جالب یونیون برلین بعدِ گل هفتم بایرن؛ کاش این پسر 19 ساله بارسلونا دهنشو ببنده! کین و اولیسه امروز واقعاً روی فرم هستن و ثابت کردن که شایستگی قرار گرفتن تو جمع مدعیان توپ طلا رو دارن. واکنش اکانت بایرن مونیخ هم ببینید.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 52.8K · <a href="https://t.me/persiana_Soccer/30048" target="_blank">📅 11:25 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30047">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E3FhJo_0UgMhCsXVPJe3mtYMOn-wKpa40Vp8oRqVO--TcNmv5kPVrhlemAhazAv4sUdpAcy5Otp13t6PnSbHx3ZCSGk51Qd200nkDRNGrVI13lnEBaYKlA3vbR-FekxSxW6ThcGJtkj9njHfhxDdIdxFTlCSa_msCx-4r8Hmt0xJSQq80cTs0wHT0yhs7sFSk9GTtiNgYfigWS5QSRW4vjGH1o-S1_gpxtwJPZCc9MPHr1C1X5Z2ohe-BhFtdazMqtNDmBATnIQPJu_oEGrmUW2h_Qt4HXeEIwk4f8MaoRySdosCglwusvXkgqlg_a4Oq6RJkfFgRskk4iGr1Gma8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
👤
یه فلش‌بک بزنیم به زمانی که ژوزه مورینیو سرمربی‌پرتغالی‌رئال‌مادرید برای اینکه خشونت بازی پپه را کم بکنه. فرستادش با تیم زنان تمرین کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/persiana_Soccer/30047" target="_blank">📅 11:05 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30046">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IuxcluA4ftF_ka4h85vXvhpwbVNX-hD9zUC9CVjcoWB3oqvMobITrrWe5rfxGzen483NwcZbkuIKPoqse8RYeJIoUkA66LhDYRWqIDXGxn31nbkeLXLW6DjP8k50Vu9BGjC8PDHB9yoTImZghVBAk3f_x4E0a_iZO8JR1lNHk23pbkuksJChIykBjlAiMQxdfaBIBlsX2W0ne7VS58XtWS2Ay7cLZa5yDo-hvmWnc5iQJMopdAP16NzKJfWZuzFyE9FrMrZ6jOGvN1mFDKAOkxp8LOAMg0f9nkFOcPxOk7p-_9nptzjEUVwsTnx1UsEC8be1pWmIIKd9_Ej0WyUBQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
کری سنگین مارسلو ستاره سابق رئال مادرید: خودم به تنهایی اندازه بارسلونا، چمپیونزلیگ دارم!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/persiana_Soccer/30046" target="_blank">📅 10:59 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30045">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UkpgPNnNc5fdn91PZu748ZIGr5bMmqP9L6CAD2VRHCKixz59JtW008lOsEMCS3pyRoewIk6JEqD--Oeq0Ib3fMqrvgLV8MJg_nAZ3Iyb6SI2O32aM4eGNfoQa_YiChHqGZy5K4OpbH7UvrbsYEEDsLdpC4xwZvc1sh3KRprbUqpVDorb1mdDmlUMTbxDjU8X_Z1gDQWwWghATp5krDL86BgqwGgA1qNP2qWkLWkfnMfve_YITGyal_-49DbcdUALTYIw3Pqfk2D2uqw4Mgen_wwt2q4sN9vRgp1WppIc_WFUwHhafsgdweMvyZEfsX1Cj0hvWsvGpXwCrl-tZ1Vvuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
مقایسه‌تعدادفصل‌های‌الکس‌فرگوسن و لئو مسی برای رسیدن به 49 جام در کل دوران حرفه‌ایشون.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/persiana_Soccer/30045" target="_blank">📅 10:59 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30043">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/83a5244f7f.mp4?token=m6xcfrZ3dC5hsHtbOk1GA-iAtFWQmNOdMNFnPqmoYSttZdyPhImfMlnUWniu4qtK6zX2Qb9qjW2_2omQYBeF32aAOEkxi5OYzyN0SoCO1Yk-MV_jewi7lWkIjFjeCopdt-yl7hZ66E9lLGkfIBQtVU106PqojGp3RfTOH-5c4_JdGgkK6Ju_H_ft_C0qDh8naN8Y6SaU_Ln9Ez_bQcp0y-lwwJpP_gi4ELSuHY0yC8WRzd0X5sSWxP3itApGt2oEkYFtyx8FXIdlwfTYsVI0Pi6wbQ80WE4JXHSgHm_hfvQTDLjbnRT9MT8JWMAkvSom2HZLSERASWcL6LH4mKm-sA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/83a5244f7f.mp4?token=m6xcfrZ3dC5hsHtbOk1GA-iAtFWQmNOdMNFnPqmoYSttZdyPhImfMlnUWniu4qtK6zX2Qb9qjW2_2omQYBeF32aAOEkxi5OYzyN0SoCO1Yk-MV_jewi7lWkIjFjeCopdt-yl7hZ66E9lLGkfIBQtVU106PqojGp3RfTOH-5c4_JdGgkK6Ju_H_ft_C0qDh8naN8Y6SaU_Ln9Ez_bQcp0y-lwwJpP_gi4ELSuHY0yC8WRzd0X5sSWxP3itApGt2oEkYFtyx8FXIdlwfTYsVI0Pi6wbQ80WE4JXHSgHm_hfvQTDLjbnRT9MT8JWMAkvSom2HZLSERASWcL6LH4mKm-sA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
اولین واکنش امید عالیشاه به فحاشی ناموسی خداداد: وقتی گوش دادم. دچار شرم نیابتی شدم.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/persiana_Soccer/30043" target="_blank">📅 10:39 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30042">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oflUv2rnVhA3P_xWE5-jnInqij1kLDgxbT4zARRFljMEYJ-dzFMhMJ4kWJh4kcx9S1BeR32tNVFBxNwSyAZhuT1ZzJKy_rv7zpjXMNCKGorgm8PnKibY30UufuQL0NzVOELPKCxRxcGhkUOD_c6owAU5God-gZS7S-ThnD3fuW5DiZuqswsgvWsVjwXJHYnzk3qZ-dSgy4YlfECtpTqOanUnukUuWu0iNKgamBYKYzxoJUIx8a-iWXXCnXccG5pgUDky8vEtrL9hbzZ_GQGp1AMRIMby4TeoIUxXNpS0amJ1745vYg4chErNyuJusqIB7BKJOSwHjx1ezyp5fEVisg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇲🇦
🇪🇸
🇧🇷
ادعای نشریه NC اسپانیا:
باشگاه رئال مادرید بار دیگر مذاکرات رسمی خود را برای جذب عبدالله اوزان ستاره 17 ساله مراکشی برای رقابت با وینیسیوس جونیور ستاره کهکشانی آغاز کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.7K · <a href="https://t.me/persiana_Soccer/30042" target="_blank">📅 10:09 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30041">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZF9WzC5Fga-oneMW6vkmV002d9F1cmxdhL027IFY0wJLanXAt2crnSkxaX1k9ZZ36dWLd2XY7gEUW1eFQk04to1y2222qsIPN2HNrJu1tGZt9ZOgBv_Sf47pICCYaIKkPtLcVbCk3YzqX4OCmXY9OnKx-HgfBySiaZv4a4DznUynV6WFT-5O6YmER60WJn6qewYVBUw3KpTkqWPGvHVTro21YZMT7CmO8prJbmqE56ljrJXOmaaso_5Ues2J0FpVkg3yJ6XiwyW9pNlHS8Y0Gz74u_KW0fEtinuf-IobOJwUWUPqGxiQahCIrCLqYIBY0r2LxxVZBN6EzGao8P46Tg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
👤
یکی از مدیران باشگاه استقلال: محمد خلیفه و حبیب‌ فرعباسی دو‌گلر تیم‌استقلال هستند و فعلا هیج برنامه ای برای جذب گلر جدید نداریم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.6K · <a href="https://t.me/persiana_Soccer/30041" target="_blank">📅 09:46 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30040">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OgWazlZZpL6vmoigUeTTkzE-WmoWub5TmSbSd9YRzADDlD48X18Ckqu125lPwFB-LlK8RYKAP0iHOdEunfblvdSQsEVxrHHQVn6LTzeTeIp2cxIH6dPIQ8L2AVhE_zMGhwk479NqsP_7pacZ8mE2JwL80i1tWm10QMp0UlsZdH7zTz0hlxbeX5PCT7FwXk6kwpKK1RocohYAo7njjfC0LayZvdt4ZTM6gtB6ePTbb_QnW9q3UjYnbCY2nhT7kAl6MIAOJ3qU_IITQ5b-6FP8nhf71v5cC9WhsgBO_K3bmd5dCGvBEl5fXf9ZuYHAn8NNlARURcNwHh70_jX0S0_mhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔴
#تکمیلی؛ محمد قربانی ستاره‌الوحده امارات امشب دربین دوستان نزدیک‌خود گفته از وضعیتم در الوحده راضی‌نیستم و نیم فصل یا با پرسپولیس قرار داد میبندم یا استقلال؛ هرکدومشون‌پول رضایت نامه ام رو پرداخت کنید مشکلی برای عقد قرارداد ندارم.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 55.9K · <a href="https://t.me/persiana_Soccer/30040" target="_blank">📅 09:30 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30039">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/135cc26708.mp4?token=lewS4c_f9uvDXeViAltKLiu40jNKSjDx5EOZvw6jpHu-UkUAgKFFRoOn-m67wSL6K96CCZjCzlEINFS0lvZOrE2co4E752e69I7RLyX-fYlLAcieaTiadvjRebzR453N4kw4i6TqVq4xxEilb9Fyt8gH9GXa7V988bQGaKAjJyHojFSTkrdcfh-H-pPEHWA7OoHMauRilY0k6MbnZs6HP0P8Mqs8eUT-Po09q_6B2eVFmVNFsQkHtEdrF5NtO5z2XB9kkskm_aHJEL3M1vv1SHWYWygR0dC85fEKPDyOaBeoCpf4KYWwAvBf56WGkJxjioe0irM1VnVS9n5ju0OYng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/135cc26708.mp4?token=lewS4c_f9uvDXeViAltKLiu40jNKSjDx5EOZvw6jpHu-UkUAgKFFRoOn-m67wSL6K96CCZjCzlEINFS0lvZOrE2co4E752e69I7RLyX-fYlLAcieaTiadvjRebzR453N4kw4i6TqVq4xxEilb9Fyt8gH9GXa7V988bQGaKAjJyHojFSTkrdcfh-H-pPEHWA7OoHMauRilY0k6MbnZs6HP0P8Mqs8eUT-Po09q_6B2eVFmVNFsQkHtEdrF5NtO5z2XB9kkskm_aHJEL3M1vv1SHWYWygR0dC85fEKPDyOaBeoCpf4KYWwAvBf56WGkJxjioe0irM1VnVS9n5ju0OYng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تیکه‌سنگین مهران مدیری درقسمت سوم مرد سه هزار چهره درباره فرهنگ سازی تو جاده چالوس!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.4K · <a href="https://t.me/persiana_Soccer/30039" target="_blank">📅 09:25 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30037">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8ac719facd.mp4?token=ZrrQTepFkEsV6PrB_YQmRuIquCkpBF9J2_vW9QKqKT8XF0GpI46iVvhAAz7UgV0q--euPc77NBxRrsYrgmgRDhu8G1xpvdM-M-tkevzVWCkQn9yVxwtYAV1EY3FRN2M9kWuVWB6N_vb1Erk7c5joW9PH9es6wbTF7P1iaQH47-U-vjNta99rrAyABHk6y8jqNjOtmotshN21Io-1xAaizXyzh_cvKyhP_-qoPntzVl4lraFpqOnSadyUGzgQmNgZj-ZWJUDVtr5SZlzK1K9sixwqLoV9NDAJABmYFntdUSeL7faBcOo_qULTCvNbwrmAxgluAgqlfH_NPuVN6J-6l4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8ac719facd.mp4?token=ZrrQTepFkEsV6PrB_YQmRuIquCkpBF9J2_vW9QKqKT8XF0GpI46iVvhAAz7UgV0q--euPc77NBxRrsYrgmgRDhu8G1xpvdM-M-tkevzVWCkQn9yVxwtYAV1EY3FRN2M9kWuVWB6N_vb1Erk7c5joW9PH9es6wbTF7P1iaQH47-U-vjNta99rrAyABHk6y8jqNjOtmotshN21Io-1xAaizXyzh_cvKyhP_-qoPntzVl4lraFpqOnSadyUGzgQmNgZj-ZWJUDVtr5SZlzK1K9sixwqLoV9NDAJABmYFntdUSeL7faBcOo_qULTCvNbwrmAxgluAgqlfH_NPuVN6J-6l4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
صحبت‌های‌مهدی‌مهدوی‌کیااسطوره فوتبال ایران و باشگاه‌پرسپولیس‌درباره‌پیشنهاد 2.5 میلیون دلاری باشگاه چینی داریان که به آن پاسخ منفی داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.7K · <a href="https://t.me/persiana_Soccer/30037" target="_blank">📅 00:57 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30036">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DGlWT-V9NLnwmJ_FJIdKzfjvyDWdxhD9Gf5W3qZoSLjLkfCQG9YOY_6QO6P1oZfpu9GsUgdS9vWdQOlDXBBPPPvOwzwTKTXyumGA2l_fd00quidKtutbu6ipC1c3dCPu1B0p_SYOEHGs7fPk7UYZscffXYmWXNBRKCV6WMFL4tQpREZnErRoDHkVb02FLrWJVpSoeSwslBE0ryD27Y9W7lIsNQyknjhyTIc3nbNpCUu868MJ6uUnIFtHVflSZaW_-oCdSoBnX4FitQRT3M57uzuJ2ChE56difdZIuo-8mVnsQXyI_OJveJ9tvG-GN8r0La5ekLwKp5eOVGNTsm_kgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌‌‌‌‌دیدارها‌ی‌‌‌‌‌‌‌امروز
؛ دوئل‌تمام‌عیار یاران دیبالا vs لائوتارو مارتینز برای صدرنشینی در رقابت های سری‌آ و مصاف تماشایی شاگردان فلیک با سویا
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.4K · <a href="https://t.me/persiana_Soccer/30036" target="_blank">📅 00:57 · 28 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
